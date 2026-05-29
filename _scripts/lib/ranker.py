"""URL validation, redirect resolution, and OpenAI-based candidate ranking."""

import json
import os
import re
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests

_TIMEOUT = 10
_MAX_SNIPPET = 800
_HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; research-bot/1.0)"}

# URLs that resolve fine but contain no article content worth ingesting
_DROP_PATTERNS = [
    r'/PMTEC/$',
    r'/PMTEC/PMTEC-News/$',
    r'/PMTEC/News/$',
    r'dvidshub\.net/image/',           # DVIDS photo pages — sparse content, not articles
    r'pacom\.mil/Media/News/News-Article-View/',  # DNN JS-rendered shell, no article body
]


def resolve_and_validate(candidates: list[dict]) -> list[dict]:
    """
    For each candidate:
      - Follow redirects → replace with final URL
      - Fetch a content snippet for ranking
      - Discard 404s and known index pages
    Returns validated candidates (order preserved where possible).
    """
    with ThreadPoolExecutor(max_workers=10) as ex:
        future_map = {ex.submit(_check_one, c): i for i, c in enumerate(candidates)}
        results = {}
        for future in as_completed(future_map):
            idx = future_map[future]
            result = future.result()
            if result is not None:
                results[idx] = result
    # Preserve original ordering
    return [results[i] for i in sorted(results)]


def _check_one(candidate: dict) -> dict | None:
    url = candidate["url"]
    try:
        resp = requests.get(
            url, timeout=_TIMEOUT, allow_redirects=True,
            headers=_HEADERS, stream=True,
        )
    except Exception:
        # Network error — keep optimistically; operator will see on click
        return dict(candidate)

    if resp.status_code == 404:
        return None

    final_url = resp.url

    # Drop index/photo pages (resolved URL)
    for pattern in _DROP_PATTERNS:
        if re.search(pattern, final_url):
            return None

    updated = dict(candidate)
    updated["url"] = final_url  # replace redirect URL with real URL

    if resp.status_code == 403:
        # Blocked but probably real — no snippet available
        updated["_snippet"] = ""
        return updated

    # Read a content snippet
    raw = ""
    try:
        for chunk in resp.iter_content(chunk_size=8192, decode_unicode=True):
            if isinstance(chunk, bytes):
                chunk = chunk.decode("utf-8", errors="ignore")
            raw += chunk
            if len(raw) > _MAX_SNIPPET * 8:
                break
    except Exception:
        pass

    clean = re.sub(r'<[^>]+>', ' ', raw)
    clean = re.sub(r'\s+', ' ', clean).strip()
    updated["_snippet"] = clean[:_MAX_SNIPPET]
    return updated


def rank_candidates(
    candidates: list[dict],
    opp_context: str,
    api_key: str,
) -> list[dict]:
    """
    Score each candidate with gpt-4o-mini and return sorted highest-first.
    Adds '_score' (0-10), '_tier' (high/medium/low), '_rank_note' fields.
    """
    if not candidates:
        return []

    from openai import OpenAI
    client = OpenAI(api_key=api_key)

    scored = [dict(c) for c in candidates]

    with ThreadPoolExecutor(max_workers=6) as ex:
        future_map = {ex.submit(_score_one, client, c, opp_context): i
                      for i, c in enumerate(scored)}
        for future in as_completed(future_map):
            idx = future_map[future]
            try:
                result = future.result()
            except Exception:
                result = {"score": 5, "tier": "medium", "note": ""}
            scored[idx]["_score"] = result.get("score", 5)
            scored[idx]["_tier"] = result.get("tier", "medium")
            scored[idx]["_rank_note"] = result.get("note", "")

    return sorted(scored, key=lambda c: c.get("_score", 0), reverse=True)


_PROMPT = """\
You are a defense business development analyst. Score this candidate source for relevance to the research below.

RESEARCH CONTEXT:
{opp_context}

CANDIDATE:
Title: {title}
URL: {url}
Search query that found it: "{query}"
Model's stated reason: {reason}
Content preview: {snippet}

Scoring guide:
 9-10  Primary .mil/DVIDS source directly about the opportunity/program — specific, recent
 7-8   Trade press (Breaking Defense, DefenseNews, ExecutiveGov) directly covering the opportunity
 5-6   Useful background — related but tangential
 3-4   Weakly related or generic
 1-2   Off-topic, broken, or an index/list page

Respond in JSON only — no extra text:
{{"score": <integer 1-10>, "tier": "high|medium|low", "note": "<one sentence>"}}"""


def _score_one(client, candidate: dict, opp_context: str) -> dict:
    prompt = _PROMPT.format(
        opp_context=opp_context,
        title=candidate.get("title", ""),
        url=candidate.get("url", ""),
        query=candidate.get("query", ""),
        reason=candidate.get("reason", ""),
        snippet=candidate.get("_snippet", "")[:600],
    )
    msg = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=120,
        temperature=0,
    )
    text = msg.choices[0].message.content or ""
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        m = re.search(r'\{[^}]+\}', text, re.DOTALL)
        if m:
            try:
                return json.loads(m.group(0))
            except json.JSONDecodeError:
                pass
    return {"score": 5, "tier": "medium", "note": ""}


# ── Four-pillar capture-intelligence ranking ───────────────────────────────


_CAPTURE_PROMPT = """\
You are a senior defense market intelligence analyst scoring a single source for capture-intelligence value to a specific Navy opportunity. Score on a 1-9 scale (1 worthless, 9 actionable capture intel). Use the four-pillar rubric below.

OPPORTUNITY SCOPE:
{opp_scope}

THE FOUR PILLARS — score on whichever ONE pillar best fits the candidate.

PILLAR 1 — EXPEDITIONARY MAINTENANCE / FOREIGN-PORT REPAIR (the problem space)
The Navy actually conducting the problem the product addresses.
- 9: an article naming a commercial contractor delivering scenario design, wargaming, or staff-augmentation support to one of these specific Navy exercises or operations.
- 7-8: a primary-source (DVIDS, navy.mil, secnav.navy.mil) report of the Navy actually conducting a wartime-repair drill, foreign-port repair coordination, or BDAR exercise. Cap at 7 unless the article names the contractor or the tasking office.
- 5-6: trade-press summary of the same operation already covered by a primary source.
- 3-4: general Pacific-presence or ally-cooperation news that mentions repair only in passing.
- 1-2: random Pacific deployment news with no repair angle.

PILLAR 2 — DMO / WARGAMING / DECISION-REHEARSAL (the work-type)
The work-type the product is selling.
- 9: a specific Navy contract award, task order, or solicitation for scenario design, wargaming, modeling and simulation, or exercise injection at one of the named customer organizations.
- 7-8: USNI Proceedings, CIMSEC, Naval Institute, or comparable professional-community analysis of the wartime-repair training gap, decision-rehearsal gap, or staff-cell readiness gap (even when the article does not say "training" in the title). Joint Staff JExD or MTWS funding line. Distributed Maritime Operations C2 wargaming work named at a customer organization. AFRICOM, OSD, or MDA exercise-design contracts (procurement precedents that match the work-type even when they fall outside the Navy customer set).
- 5-6: general Navy training contract announcements not specific to BDAR or staff-cell decision-rehearsal. Defense serious-games industry events such as I/ITSEC.
- 3-4: individual-Sailor damage-control or fire-control training. Aircraft pilot training. Generic Live-Virtual-Constructive training infrastructure not at our customer organizations.
- 1-2: recruiting news. Schoolhouse curriculum (NETC, Sailor 2025, Ready Relevant Learning).

PILLAR 3 — COMMAND INTENT / PRIORITY SHIFTS (the customer signal)
Statements of intent from the customer that signal whether the proposal will be well received.
- 8-9: a DIRECT customer organization official makes a specific statement of intent toward decision-rehearsal training, scenario-injection, staff-cell readiness, or wartime-repair-team training. They have local OMN money and an immediate pain point.
- 6-7: an HQ or policy organization makes the same kind of statement. Senior testimony naming wartime-repair readiness as a funded line.
- 5: a pure personnel announcement at a customer organization without a statement of intent.
- 3-4: general Navy posture or readiness rhetoric not specific to wartime repair, BDAR, or decision-rehearsal.
- 1-2: personnel news at unrelated commands, ceremonial events, command-philosophy puff.

PILLAR 4 — CONTRACTOR DISCOVERY (the competitor signal)
Who is doing the work at the customer organizations. Contractor identities surface as outputs of this pillar; the rubric does not contain a pre-loaded contractor list.
- 8-9: a commercial contractor is named as awardee on a Navy contract at a direct customer organization for work plausibly adjacent to scenario design, wargaming, exercise support, decision-rehearsal, modeling and simulation, or staff augmentation.
- 6-7: a commercial contractor named on a Navy contract for adjacent work at an HQ or policy organization or at a Joint command. A Navy industry-day announcement naming the candidate work-types.
- 4-5: a contractor announcement at a Navy organization that is not one of our customer organizations (e.g., a NAVAIR aircraft-simulation award).
- 1-2: a contractor announcement unrelated to our customer organizations or work-types (e.g., a Navy IT helpdesk vehicle).

TECHNICAL-LIMITATION RULES (apply before pillar scoring):

RULE A — USAspending thin-snippet rule: if the candidate URL is on usaspending.gov AND the title contains any work-type keyword (exercise, wargame, scenario, modeling, simulation, staff augmentation, decision support, training, M&S, C5ISR), score 7-8 (depending on customer-org match) and START THE NOTE WITH "[THIN-SNIPPET — manual ingest required]".

RULE B — Big-PDF budget document rule: if the candidate URL is on comptroller.war.gov, comptroller.defense.gov, secnav.navy.mil/fmc/fmb, or congress.gov bill text, the score is CAPPED AT 7 — never 8 or 9 — even when the title is keyword-relevant. The ranker cannot tell whether the load-bearing line is on page 10 or page 2,000. START THE NOTE WITH "[BIG-PDF — targeted section search required]".

RULE C — Secondary trade-press cap at 6: if the candidate is a trade-press piece (NavalNews, Defense News, Breaking Defense, Aerotechnews, GovConWire) on an event that a primary source (DVIDS, navy.mil) is likely to also cover, cap at 6.

RULE D — Out-of-scope floor at 3: items in the OUT-OF-SCOPE categories listed in OPPORTUNITY SCOPE score MAX 3, even if they keyword-match.

CANDIDATE TO SCORE:
Title: {title}
URL: {url}
Search query that surfaced this: "{query}"
Prior reasoning: {reason}
Content snippet (may be truncated): {snippet}

Respond in JSON only, nothing else:
{{"score": <integer 1-9>, "pillar": <integer 1-4>, "note": "<one short sentence explaining the score>"}}"""


def load_capture_pillars(opp_dir) -> str | None:
    """Return the opportunity's _capture-pillars.md text if present, else None."""
    from pathlib import Path
    p = Path(opp_dir) / "_capture-pillars.md"
    if not p.exists():
        return None
    return p.read_text(encoding="utf-8")


def rank_candidates_capture(
    candidates: list[dict],
    opp_scope_text: str,
    api_key: str,
) -> list[dict]:
    """Four-pillar capture-intel ranker. Use when the opportunity has a
    `_capture-pillars.md` file defining its scope, customer hierarchy,
    work-type keywords, and out-of-scope list.

    Scores on a 1-9 scale. Adds '_score', '_pillar', '_rank_note' fields.
    """
    if not candidates:
        return []

    from openai import OpenAI
    client = OpenAI(api_key=api_key)

    scored = [dict(c) for c in candidates]

    with ThreadPoolExecutor(max_workers=6) as ex:
        future_map = {
            ex.submit(_score_capture_one, client, c, opp_scope_text): i
            for i, c in enumerate(scored)
        }
        for future in as_completed(future_map):
            idx = future_map[future]
            try:
                result = future.result()
            except Exception:
                result = {"score": 5, "pillar": 0, "note": ""}
            scored[idx]["_score"] = result.get("score", 5)
            scored[idx]["_pillar"] = result.get("pillar", 0)
            scored[idx]["_rank_note"] = result.get("note", "")
            # Tier mapping for compatibility with the legacy display:
            sc = scored[idx]["_score"]
            scored[idx]["_tier"] = "high" if sc >= 7 else ("medium" if sc >= 5 else "low")

    return sorted(scored, key=lambda c: c.get("_score", 0), reverse=True)


def _score_capture_one(client, candidate: dict, opp_scope_text: str) -> dict:
    prompt = _CAPTURE_PROMPT.format(
        opp_scope=opp_scope_text[:6000],
        title=candidate.get("title", "")[:200],
        url=candidate.get("url", ""),
        query=candidate.get("query", ""),
        reason=candidate.get("reason", "")[:400],
        snippet=candidate.get("_snippet", "")[:800],
    )
    msg = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=220,
        temperature=0,
    )
    text = msg.choices[0].message.content or ""
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        m = re.search(r'\{[^}]+\}', text, re.DOTALL)
        if m:
            try:
                return json.loads(m.group(0))
            except json.JSONDecodeError:
                pass
    return {"score": 5, "pillar": 0, "note": ""}


# ── SAM.gov candidate ranking ──────────────────────────────────────────────


_SAM_PROMPT = """\
You are a defense business development analyst. Score this SAM.gov notice for relevance to the research below.

RESEARCH CONTEXT:
{opp_context}

CANDIDATE (SAM.gov notice):
Title: {title}
URL: {url}
Notice type: {notice_type}
Set-aside: {set_aside}
NAICS code(s): {naics}
Department / subtier / office: {department} / {subtier} / {office}
Posted: {posted_date} | Response deadline: {response_deadline}
Search query that matched: "{query}"
Notice description preview: {snippet}

Scoring guide for SAM.gov solicitations:
 9-10  Active RFI or RFP directly matching the research opportunity — actionable as a candidate bid
 7-8   Active solicitation in adjacent capability area from the right organization (e.g., NSWC site running a relevant SBIR/STTR topic; NAVSEA contracting a capability that maps to the research)
 5-6   Useful market intelligence — same command, NAICS, or capability cluster, peripheral but informative
 3-4   Weakly related — keyword match only, wrong agency, generic services contract
 1-2   Off-topic, expired or cancelled, contract closeout / disposal / janitorial / food / transportation

Apply the lowest applicable bucket. Wrong agency plus weak capability fit equals 3-4 even when the keyword matches.

Respond in JSON only — no extra text:
{{"score": <integer 1-10>, "tier": "high|medium|low", "note": "<one-sentence reason>"}}"""


def rank_sam_candidates(
    candidates: list[dict],
    opp_context: str,
    api_key: str,
) -> list[dict]:
    """Score SAM.gov candidates with gpt-4o-mini. Returns sorted highest-first.

    Adds '_score' (1-10), '_tier' (high|medium|low), '_rank_note' fields. Uses
    a SAM-specific prompt tuned for solicitation taxonomy rather than the
    web-article prompt in rank_candidates().
    """
    if not candidates:
        return []

    from openai import OpenAI
    client = OpenAI(api_key=api_key)

    scored = [dict(c) for c in candidates]

    with ThreadPoolExecutor(max_workers=6) as ex:
        future_map = {ex.submit(_score_sam_one, client, c, opp_context): i
                      for i, c in enumerate(scored)}
        for future in as_completed(future_map):
            idx = future_map[future]
            try:
                result = future.result()
            except Exception:
                result = {"score": 5, "tier": "medium", "note": ""}
            scored[idx]["_score"] = result.get("score", 5)
            scored[idx]["_tier"] = result.get("tier", "medium")
            scored[idx]["_rank_note"] = result.get("note", "")

    return sorted(scored, key=lambda c: c.get("_score", 0), reverse=True)


def _score_sam_one(client, candidate: dict, opp_context: str) -> dict:
    naics = candidate.get("naics") or []
    naics_str = ", ".join(naics) if naics else "none"
    prompt = _SAM_PROMPT.format(
        opp_context=opp_context,
        title=candidate.get("title", ""),
        url=candidate.get("url", ""),
        notice_type=candidate.get("notice_type", ""),
        set_aside=candidate.get("set_aside", "None"),
        naics=naics_str,
        department=candidate.get("department", ""),
        subtier=candidate.get("subtier", ""),
        office=candidate.get("office", ""),
        posted_date=candidate.get("posted_date", ""),
        response_deadline=candidate.get("response_deadline", ""),
        query=candidate.get("query", ""),
        snippet=candidate.get("_snippet", "")[:600],
    )
    msg = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=120,
        temperature=0,
    )
    text = msg.choices[0].message.content or ""
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        m = re.search(r'\{[^}]+\}', text, re.DOTALL)
        if m:
            try:
                return json.loads(m.group(0))
            except json.JSONDecodeError:
                pass
    return {"score": 5, "tier": "medium", "note": ""}

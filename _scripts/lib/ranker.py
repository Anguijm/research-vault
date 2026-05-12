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

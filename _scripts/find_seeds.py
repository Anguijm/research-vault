#!/usr/bin/env python3
"""
find_seeds.py — V1 opportunity-seed discovery for the CACI BD research vault.

Queries three v1 sources for the prior 56 days, deduplicates against the
seeds ledger, ranks new candidates against the layered CACI capability
footprint defined in `_meta/caci-discovery-config.yaml`, and writes surfaced
candidates to `_meta/seeds-inbox.md` for operator triage.

Sources (v1):
  1. SAM.gov pre-solicitation notices (Sources Sought, RFI, Industry Day,
     Special Notice, Pre-Solicitation) — the actionability engine.
  2. War.gov daily contract announcements — the procurement-precedent
     engine. (Best-effort HTML scrape of war.gov/News/Contracts/.)
  3. DoD comptroller justification books — the upstream funding-signal
     engine. (v1 implements URL discovery and basic keyword flagging;
     full per-Program-Element section extraction deferred to v1.5.)

Ranker:
  Four pillars (customer signal, work-type match, scale signal,
  actionability window) with a layered CACI-footprint match — operator
  team layer gets 1.5x boost, extendable customers 1.3x, directional 1.2x,
  baseline 1.0x. Delivery-model-mismatch subtracts 0.1. Out-of-scope hits
  cap final score at 0.3.

Usage:
    python find_seeds.py
    python find_seeds.py --source sam-gov                 # SAM.gov only
    python find_seeds.py --source sam-gov --weekly        # 14-day lookback
    python find_seeds.py --lookback-days 28
    python find_seeds.py --dry-run                        # no file writes
"""

import argparse
import hashlib
import json
import os
import re
import sys
from collections import OrderedDict
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import urlparse

import requests
import yaml
from dotenv import load_dotenv

SCRIPT_DIR = Path(__file__).parent
VAULT_ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))
load_dotenv(SCRIPT_DIR / ".env")

from lib import sam_gov as sam_gov_lib

CONFIG_PATH = VAULT_ROOT / "_meta" / "caci-discovery-config.yaml"
SEEDS_INBOX = VAULT_ROOT / "_meta" / "seeds-inbox.md"
SEEDS_LEDGER = VAULT_ROOT / "_meta" / "seeds-ledger.json"
SEEDS_REJECTED = VAULT_ROOT / "_meta" / "seeds-rejected.md"
SEEDS_PROMOTED = VAULT_ROOT / "_meta" / "seeds-promoted.md"

DEFAULT_LOOKBACK_DAYS = 56  # 8 weeks
WEEKLY_LOOKBACK_DAYS = 14

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; caci-seed-finder/1.0; research-vault)",
    "Accept": "text/html,application/xhtml+xml",
}


# ── Config and ledger I/O ───────────────────────────────────────────────


def _load_config() -> dict:
    return yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8"))


def _load_ledger() -> dict:
    if not SEEDS_LEDGER.exists():
        return {"version": 1, "last_run_utc": "", "seeds": {}}
    try:
        return json.loads(SEEDS_LEDGER.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {"version": 1, "last_run_utc": "", "seeds": {}}


def _save_ledger(ledger: dict) -> None:
    SEEDS_LEDGER.parent.mkdir(parents=True, exist_ok=True)
    SEEDS_LEDGER.write_text(json.dumps(ledger, indent=2), encoding="utf-8")


def _utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _fingerprint(candidate: dict) -> str:
    """Generate a stable fingerprint for dedup."""
    source = candidate.get("source", "")
    if source == "sam_gov":
        return f"SAM:{candidate.get('notice_id', '')}"
    if source == "war_gov":
        return f"WAR:{candidate.get('article_id', '')}"
    if source == "comptroller":
        return f"COMPT:{candidate.get('document_id', '')}"
    # URL-hash fallback
    url = candidate.get("url", "")
    h = hashlib.sha256(url.encode()).hexdigest()[:16]
    return f"URL:{h}"


# ── Source 1: SAM.gov pre-solicitation notices ─────────────────────────


def _query_sam_gov(lookback_days: int) -> list[dict]:
    """Query SAM.gov for pre-solicitation, sources-sought, RFI, special notice,
    industry day notices in the lookback window.

    Routes every API call through `lib/sam_gov.py::execute_query` so the lib's
    2 req/sec throttle, 900/1000 daily safety-pause, and 429 retry-with-backoff
    are applied automatically. We do NOT issue direct `requests.get()` calls
    against the SAM.gov endpoint — that bypasses rate limiting and produces
    429 storms.
    """
    api_key = os.environ.get("SAM_GOV_API_KEY", "")
    if not api_key:
        print("  WARN: SAM_GOV_API_KEY not set — skipping SAM.gov source.")
        return []

    # Quota check before any calls — fail fast if today's quota is exhausted.
    quota = sam_gov_lib.load_quota()
    used = quota.get("requests_today", 0)
    if sam_gov_lib.quota_paused():
        print(f"  SAM.gov DAILY QUOTA PAUSE — used {used}/{sam_gov_lib.DAILY_LIMIT} today (safety pause at {sam_gov_lib.SAFETY_PAUSE_AT}).")
        print(f"  Resumes 00:00 UTC tomorrow. Skipping SAM.gov source for this run.")
        return []
    remaining_today = sam_gov_lib.DAILY_LIMIT - used
    print(f"  SAM.gov quota: {used}/{sam_gov_lib.DAILY_LIMIT} used today ({remaining_today} remaining, polite throttle at {sam_gov_lib.RATE_LIMIT_PER_SEC} req/sec).")

    # Consolidate all four notice types into a single API call via
    # comma-separated `ptype` codes. SAM.gov accepts multi-value ptype and
    # returns notices across all matching types in one response. This cuts
    # our daily SAM.gov spend by 4x — critical for non-federal API keys
    # capped at 10 requests/day.
    notice_types = ["Sources Sought", "Special Notice", "Presolicitation", "Combined Synopsis/Solicitation"]
    ptype_codes = [_sam_ptype_code(nt) for nt in notice_types if _sam_ptype_code(nt)]
    ptype_combined = ",".join(ptype_codes)
    params = {
        "ptype": ptype_combined,
        "deptname": "DEPT OF DEFENSE",
    }
    entry = {"params": params}
    full_params = sam_gov_lib.parse_search_entry(entry, lookback_days)
    candidates: list[dict] = []
    try:
        # max_candidates=1000 because SAM.gov caps at 1000 per call and we
        # only get one call per run for non-federal tier; pull as many as
        # the API will return so the dedup + ranker has a full window.
        notices = sam_gov_lib.execute_query(full_params, api_key, max_candidates=1000)
    except sam_gov_lib.SamGovKeyError as e:
        print(f"  SAM.gov KEY ERROR — {e}; aborting SAM.gov source for this run.")
        return candidates
    except Exception as e:
        print(f"  SAM.gov error: {e}")
        return candidates
    print(f"  SAM.gov [combined ptype={ptype_combined}]: {len(notices)} notices in one API call")
    for n in notices:
        # The lib's normalized notice carries `notice_type` from the API
        # response (e.g., "Sources Sought", "Special Notice"). Map it back
        # to our actionability labels.
        nt_label = _sam_label_from_lib_notice_type(n.get("notice_type", ""))
        candidates.append(_normalize_sam_notice_from_lib(n, nt_label))

    # Post-call quota status
    quota_after = sam_gov_lib.load_quota()
    used_after = quota_after.get("requests_today", 0)
    print(f"  SAM.gov quota after this run: {used_after}/{sam_gov_lib.DAILY_LIMIT} used today ({sam_gov_lib.DAILY_LIMIT - used_after} remaining).")
    return candidates


def _sam_label_from_lib_notice_type(api_notice_type: str) -> str:
    """Map a SAM.gov API notice-type string back to our canonical
    actionability label. The API returns full names (e.g., 'Sources Sought',
    'Special Notice') matching our labels, but normalize for safety."""
    api_lower = (api_notice_type or "").lower()
    if "sources sought" in api_lower:
        return "Sources Sought"
    if "special notice" in api_lower:
        return "Special Notice"
    if "presolicitation" in api_lower:
        return "Presolicitation"
    if "combined synopsis" in api_lower or "combined solicitation" in api_lower:
        return "Combined Synopsis/Solicitation"
    if "request for information" in api_lower or api_lower == "rfi":
        return "Request for Information"
    if "industry day" in api_lower:
        return "Industry Day"
    if "solicitation" in api_lower or "rfp" in api_lower:
        return "Solicitation"
    if "award" in api_lower:
        return "Award Notice"
    return api_notice_type or "Sources Sought"


def _normalize_sam_notice_from_lib(n: dict, notice_type_label: str) -> dict:
    """Normalize a sam_gov_lib-returned notice dict into our candidate shape.

    The lib's `_normalize_notice` returns a richer structured dict than the
    raw API payload. We map its fields to the find_seeds candidate shape.
    Note: the lib does NOT fetch the description text (that's a separate
    `fetch_description` call against the noticedesc endpoint that would
    double our SAM.gov API call count). For v1 we leave `snippet` empty and
    rely on the title + customer + notice type for ranking. The raw API
    payload is preserved in `n["raw"]` for fields the lib doesn't surface.
    """
    naics_list = n.get("naics") or []
    naics = naics_list[0] if isinstance(naics_list, list) and naics_list else ""
    raw = n.get("raw") or {}
    psc = (raw.get("classificationCode") or "").strip()
    return {
        "source": "sam_gov",
        "notice_id": n.get("notice_id", ""),
        "title": n.get("title", ""),
        "url": n.get("url") or f"https://sam.gov/opp/{n.get('notice_id', '')}/view",
        "notice_type": notice_type_label,
        "department": n.get("department", ""),
        "subtier": n.get("subtier", ""),
        "office": n.get("office", ""),
        "naics": naics,
        "psc": psc,
        "posted": n.get("posted_date", ""),
        "response_deadline": n.get("response_deadline", ""),
        "set_aside": n.get("set_aside", ""),
        "snippet": "",  # not fetched by default; clicking the URL pulls the full notice
    }


def _sam_ptype_code(notice_type: str) -> str:
    """SAM.gov uses single-letter notice-type codes. Map our labels."""
    mapping = {
        "Sources Sought": "r",
        "Special Notice": "s",
        "Presolicitation": "p",
        "Combined Synopsis/Solicitation": "k",
        "Industry Day": "g",
        "Request for Information": "r",
    }
    return mapping.get(notice_type, "")


# ── Source 2: war.gov daily contract announcements ─────────────────────


def _query_war_gov(lookback_days: int) -> list[dict]:
    """Best-effort scrape of war.gov contracts daily-listing pages.

    war.gov/News/Contracts/Contract/Article/{ID}/contracts-for-MMMM-DD-YYYY/
    has a daily contract listing. We iterate the prior N days and try to
    fetch each daily page. Returns the contracts listed."""
    candidates = []
    today = date.today()
    for n in range(lookback_days):
        d = today - timedelta(days=n)
        # The article IDs are not predictable from date alone; the URL pattern
        # is /contracts-for-MONTH-DD-YYYY/. We try the canonical slug.
        slug = f"contracts-for-{d.strftime('%B').lower()}-{d.day}-{d.year}"
        candidates.extend(_fetch_war_gov_daily(slug, d.isoformat()))
    return candidates


def _fetch_war_gov_daily(slug: str, iso_date: str) -> list[dict]:
    """Fetch one war.gov daily contracts page. Best-effort; many will 404.

    Note: war.gov pages have variable article IDs prepended (e.g.,
    /Article/4496900/contracts-for-may-20-2026/). Without a sitemap index,
    we can't construct the full URL deterministically. v1 returns empty for
    war.gov when called this way; v1.5 will add an index-page scrape that
    discovers the article IDs first."""
    return []


# ── Source 3: comptroller justification books ──────────────────────────


def _query_comptroller(lookback_days: int) -> list[dict]:
    """V1 stub: produces a fixed list of comptroller-book URLs the operator
    should check, but doesn't actually download or section-search the PDFs.

    The full per-Program-Element section extraction is a v1.5 enhancement
    using the BDR-developed big-PDF section-search pattern."""
    candidates = []
    # FY27 books that are public
    books = [
        {
            "title": "FY27 RDT&E Justification Book — Joint Staff (TJS)",
            "url": "https://comptroller.war.gov/Portals/45/Documents/defbudget/FY2027/budget_justification/pdfs/03_RDT_and_E/RDTE_TJS_PB_2027.pdf",
            "document_id": "FY27_RDTE_TJS",
            "scope": "Joint Staff RDT&E line items including Joint Exercise Division (JExD), AI scenario generation, MAGTF Tactical Warfare Simulation",
        },
        {
            "title": "FY27 Department of the Navy President's Budget Press Brief",
            "url": "https://www.secnav.navy.mil/fmc/fmb/Documents/27pres/DON_Press_Brief.pdf",
            "document_id": "FY27_DON_PB",
            "scope": "Navy FY27 funding posture including Ship Maintenance and SIOP",
        },
    ]
    for b in books:
        candidates.append({
            "source": "comptroller",
            "document_id": b["document_id"],
            "title": b["title"],
            "url": b["url"],
            "snippet": b["scope"] + " [V1 STUB: requires manual section search; v1.5 will add per-Program-Element extraction]",
            "posted": "N/A",
            "department": "DEPT OF DEFENSE",
            "subtier": "Comptroller",
            "naics": "",
            "psc": "",
        })
    return candidates


# ── Four-pillar layered ranker ─────────────────────────────────────────


def _score_candidate(c: dict, cfg: dict) -> dict:
    """Score a candidate via four pillars + layered boost + penalty + out-of-scope cap."""
    pillar_customer, customer_layer = _score_customer(c, cfg)
    pillar_worktype, worktype_layer = _score_worktype(c, cfg)
    pillar_scale = _score_scale(c, cfg)
    pillar_actionability = _score_actionability(c, cfg)

    # Weighted base score (0-1)
    w = cfg.get("ranker_weights", {})
    base = (
        pillar_customer * w.get("customer_signal", 0.35)
        + pillar_worktype * w.get("work_type_match", 0.35)
        + pillar_scale * w.get("scale_signal", 0.15)
        + pillar_actionability * w.get("actionability_window", 0.15)
    )

    # Layer boost — take the highest-matching layer across customer + worktype matches
    layer_boost = max(
        _layer_boost(customer_layer, cfg),
        _layer_boost(worktype_layer, cfg),
    )

    # Delivery-model penalty
    delivery_penalty = 0.0
    if _delivery_model_mismatch(c, cfg):
        delivery_penalty = w.get("delivery_model_mismatch_penalty", 0.10)

    # Final score (0-1 conceptually; can exceed 1.0 with layer boost)
    final = max(0.0, (base * layer_boost) - delivery_penalty)

    # Out-of-scope cap (Rule D from the BDR ranker)
    if _is_out_of_scope(c, cfg):
        final = min(final, 0.3)
        oos_flagged = True
    else:
        oos_flagged = False

    return {
        "pillar_customer": round(pillar_customer, 2),
        "pillar_worktype": round(pillar_worktype, 2),
        "pillar_scale": round(pillar_scale, 2),
        "pillar_actionability": round(pillar_actionability, 2),
        "base_score": round(base, 3),
        "layer_boost": round(layer_boost, 2),
        "layer_matched": customer_layer if _layer_boost(customer_layer, cfg) >= _layer_boost(worktype_layer, cfg) else worktype_layer,
        "delivery_penalty": round(delivery_penalty, 2),
        "out_of_scope_flagged": oos_flagged,
        "final_score": round(final, 3),
        "score_display": f"{int(round(final * 10))}/10",
    }


def _score_customer(c: dict, cfg: dict) -> tuple[float, str]:
    """Return (pillar_value, layer) for the customer signal pillar."""
    text = " ".join([
        c.get("department", ""),
        c.get("subtier", ""),
        c.get("office", ""),
        c.get("title", ""),
        c.get("snippet", ""),
    ]).lower()

    team = cfg.get("operator_team_layer", {})
    primary = team.get("team_primary_customer", "")
    if primary and primary.lower() in text:
        return 1.0, "operator_team_layer"

    for ext in team.get("team_extendable_customers", []) or []:
        # try a few simple keyword matches per extendable customer
        ext_l = ext.lower()
        # strip parenthetical acronyms for matching
        ext_main = re.sub(r"\s*\(.*\)\s*", "", ext_l).strip()
        if ext_main and ext_main in text:
            return 0.85, "operator_team_extendable"
        # try acronyms in parens
        m = re.search(r"\(([^)]+)\)", ext_l)
        if m and m.group(1).strip().lower() in text:
            return 0.85, "operator_team_extendable"

    baseline = cfg.get("baseline_caci_footprint", {}).get("customer_orgs", []) or []
    for entry in baseline:
        label = entry.get("label", "").split(" — ", 1)[0].lower() if isinstance(entry, dict) else str(entry).lower()
        if label and label in text:
            return 0.5, "baseline_caci_footprint"

    return 0.0, "none"


def _score_worktype(c: dict, cfg: dict) -> tuple[float, str]:
    text = " ".join([
        c.get("title", ""),
        c.get("snippet", ""),
        c.get("naics", ""),
        c.get("psc", ""),
    ]).lower()

    team = cfg.get("operator_team_layer", {})

    # Team work-types: high-confidence match
    for wt in team.get("team_work_types", []) or []:
        wt_l = wt.lower()
        # Match on a few key terms from each work-type description
        key_terms = re.findall(r"[a-zA-Z]{4,}", wt_l)
        # require at least 2 distinct key terms (avoid one-word over-match)
        hits = sum(1 for kt in set(key_terms) if kt in text)
        if hits >= 2:
            return 1.0, "operator_team_layer"

    # Active team pursuits: implication keywords
    for pursuit in team.get("active_team_pursuits", []) or []:
        impl = pursuit.get("seed_finder_implication", "").lower()
        key_terms = re.findall(r"[a-zA-Z]{5,}", impl)
        hits = sum(1 for kt in set(key_terms) if kt in text)
        if hits >= 3:
            return 0.9, "operator_team_layer"

    # Directional layer: keyword match in CACI growth signals
    directional = cfg.get("directional_caci_footprint", {}).get("growth_signals", []) or []
    for sig in directional[:30]:
        kw = sig.get("keyword", "").lower() if isinstance(sig, dict) else str(sig).lower()
        if kw and kw in text:
            return 0.6, "directional_caci_footprint"

    # Baseline layer: NAICS / PSC label match
    baseline = cfg.get("baseline_caci_footprint", {}).get("work_types", []) or []
    for entry in baseline:
        label = entry.get("label", "").lower() if isinstance(entry, dict) else str(entry).lower()
        if not label:
            continue
        # Match on the NAICS/PSC code prefix or a key term from the description
        parts = label.split(" — ", 1)
        code = parts[0].strip()
        if code and code in text:
            return 0.4, "baseline_caci_footprint"

    return 0.0, "none"


def _score_scale(c: dict, cfg: dict) -> float:
    """Estimate scale signal. SAM.gov notices rarely show dollar value;
    fall back to set-aside / NAICS heuristics."""
    thr = cfg.get("thresholds", {})
    prime_min = thr.get("prime_scale_min_usd", 50_000_000)
    precedent_min = thr.get("precedent_scale_min_usd", 10_000_000)

    # War.gov contracts almost always include the dollar amount in the
    # snippet. Look for it.
    snippet = c.get("snippet", "")
    m = re.search(r"\$\s?([\d,]+(?:\.\d+)?)\s*(million|billion|M|B)?", snippet, re.IGNORECASE)
    if m:
        amount = float(m.group(1).replace(",", ""))
        unit = (m.group(2) or "").lower()
        if unit.startswith("b"):
            amount *= 1_000_000_000
        elif unit.startswith("m"):
            amount *= 1_000_000
        if amount >= prime_min:
            return 1.0
        if amount >= precedent_min:
            return 0.7
        if amount > 0:
            return 0.3

    # SAM.gov: default to medium signal for any DoD pre-solicitation
    # (the size will be known later if it goes to RFP).
    if c.get("source") == "sam_gov":
        return 0.5

    # Comptroller stubs: scale-relevant because budget books are by definition
    # multi-line-item documents.
    if c.get("source") == "comptroller":
        return 0.6

    return 0.0


def _score_actionability(c: dict, cfg: dict) -> float:
    actionability = cfg.get("actionability_logic", {})
    notice_type = c.get("notice_type", "")
    if notice_type in actionability.get("high_priority", []):
        return 1.0
    if notice_type in actionability.get("medium_priority", []):
        return 0.6
    if notice_type in actionability.get("low_priority", []):
        return 0.2
    # War.gov contracts are awarded — by definition past the shaping window.
    if c.get("source") == "war_gov":
        return 0.2
    # Comptroller justification books are forward-looking; highest actionability.
    if c.get("source") == "comptroller":
        return 0.9
    return 0.4


def _layer_boost(layer_name: str, cfg: dict) -> float:
    w = cfg.get("ranker_weights", {})
    if layer_name == "operator_team_layer":
        return w.get("operator_team_layer_boost", 1.5)
    if layer_name == "operator_team_extendable":
        return w.get("operator_team_extendable_boost", 1.3)
    if layer_name == "directional_caci_footprint":
        return w.get("directional_layer_boost", 1.2)
    if layer_name == "baseline_caci_footprint":
        return w.get("baseline_layer_boost", 1.0)
    return 1.0


def _delivery_model_mismatch(c: dict, cfg: dict) -> bool:
    """Heuristic: flag mismatch if notice content names remote / standoff /
    contractor-isolated delivery requirements."""
    text = (c.get("snippet", "") + " " + c.get("title", "")).lower()
    mismatch_markers = ["remote work", "telework", "contractor facility", "off-site",
                        "vendor-hosted", "standoff delivery", "cleared facility"]
    return any(m in text for m in mismatch_markers)


def _is_out_of_scope(c: dict, cfg: dict) -> bool:
    text = (c.get("title", "") + " " + c.get("snippet", "")).lower()
    for oos in cfg.get("out_of_scope", []) or []:
        # Extract a few key terms from each out-of-scope phrase
        terms = re.findall(r"[a-zA-Z]{5,}", oos.lower())
        # require at least 2 distinct key terms
        hits = sum(1 for t in set(terms) if t in text)
        if hits >= 2:
            return True
    return False


# ── Triage status logic and inbox writing ──────────────────────────────


def _decide_status(score: dict, cfg: dict) -> str:
    thr = cfg.get("thresholds", {})
    final = score["final_score"]
    if final >= thr.get("min_score_to_promote", 0.75):
        return "promote-eligible"
    if final >= thr.get("min_score_to_monitor", 0.50):
        return "monitor-eligible"
    return "below-threshold"


def _seed_block(c: dict, score: dict, layer_matched: str) -> str:
    title = c.get("title", "(untitled)")[:160]
    url = c.get("url", "")
    src = c.get("source", "?")
    src_label = {"sam_gov": "sam.gov", "war_gov": "war.gov", "comptroller": "comptroller.war.gov"}.get(src, src)
    notice_type = c.get("notice_type", "")
    customer = " / ".join(filter(None, [c.get("department", ""), c.get("subtier", ""), c.get("office", "")]))[:120]
    posted = c.get("posted", "")
    deadline = c.get("response_deadline", "")
    naics = c.get("naics", "")
    psc = c.get("psc", "")
    snippet_short = (c.get("snippet", "")[:280]).replace("\n", " ")

    layer_label = {
        "operator_team_layer": "OPERATOR-TEAM (1.5x)",
        "operator_team_extendable": "TEAM-EXTENDABLE (1.3x)",
        "directional_caci_footprint": "DIRECTIONAL (1.2x)",
        "baseline_caci_footprint": "BASELINE (1.0x)",
        "none": "NO-LAYER-MATCH",
    }.get(layer_matched, layer_matched)

    oos_marker = " ⚑ OUT-OF-SCOPE" if score.get("out_of_scope_flagged") else ""
    dm_marker = " ⚑ DELIVERY-MODEL-MISMATCH" if score.get("delivery_penalty", 0) > 0 else ""

    lines = [
        f"- [ ] **[{title}]({url})** `{score['score_display']}` — {src_label}{oos_marker}{dm_marker}",
        f"  - Source: {src_label} ({notice_type or 'announcement'})",
        f"  - Customer: {customer}",
        f"  - Posted: {posted} | Response deadline: {deadline}" if (posted or deadline) else f"  - Posted: {posted}",
        f"  - NAICS: {naics} | PSC: {psc}",
        f"  - Layer matched: {layer_label}",
        f"  - Pillars: customer {score['pillar_customer']} / work-type {score['pillar_worktype']} / scale {score['pillar_scale']} / actionability {score['pillar_actionability']}  →  base {score['base_score']} × boost {score['layer_boost']} − penalty {score['delivery_penalty']} = final {score['final_score']}",
        f"  - Snippet: {snippet_short}",
        f"  - Triage: [ ] promote  [ ] drop  [ ] monitor",
        f"  - First-seen: {_utc_now()}",
        "",
    ]
    return "\n".join(lines)


def _write_inbox(new_seeds: list[dict], cfg: dict) -> None:
    """Prepend new seeds to seeds-inbox.md under a dated section."""
    if not SEEDS_INBOX.parent.exists():
        SEEDS_INBOX.parent.mkdir(parents=True, exist_ok=True)

    existing = SEEDS_INBOX.read_text(encoding="utf-8") if SEEDS_INBOX.exists() else ""
    if not existing:
        existing = "# Seeds Inbox — opportunity-seed discovery output\n\nGenerated by `_scripts/find_seeds.py`. Operator triages each seed by marking `[x]` on `promote`, `drop`, or `monitor`. `approve_seeds.py` processes the marked seeds.\n\n"

    ts = datetime.now().strftime("%Y-%m-%d %H:%M")
    block_lines = [f"\n## Seeds surfaced {ts}\n"]
    for item in new_seeds:
        block_lines.append(_seed_block(item["candidate"], item["score"], item["score"]["layer_matched"]))
    block = "\n".join(block_lines)

    SEEDS_INBOX.write_text(existing + block, encoding="utf-8")


def _update_ledger(ledger: dict, new_seeds: list[dict]) -> None:
    """Update the ledger with new fingerprints and timestamps."""
    now = _utc_now()
    for item in new_seeds:
        fp = item["fingerprint"]
        if fp not in ledger["seeds"]:
            ledger["seeds"][fp] = {
                "first_seen_utc": now,
                "last_seen_utc": now,
                "status": "in-inbox",
                "url": item["candidate"].get("url", ""),
                "title": item["candidate"].get("title", "")[:120],
                "final_score": item["score"]["final_score"],
            }
        else:
            ledger["seeds"][fp]["last_seen_utc"] = now
    ledger["last_run_utc"] = now


# ── Main ───────────────────────────────────────────────────────────────


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--source", choices=["sam-gov", "war-gov", "comptroller", "all"], default="all",
                    help="Limit to a single source. Default: all.")
    ap.add_argument("--lookback-days", type=int, default=None,
                    help="Override lookback window. Default 56; or 14 with --weekly.")
    ap.add_argument("--weekly", action="store_true",
                    help="Shorthand for --lookback-days 14. Useful with --source sam-gov.")
    ap.add_argument("--dry-run", action="store_true", help="Don't write inbox or ledger.")
    args = ap.parse_args()

    cfg = _load_config()
    ledger = _load_ledger()

    lookback = args.lookback_days or (WEEKLY_LOOKBACK_DAYS if args.weekly else DEFAULT_LOOKBACK_DAYS)

    print(f"find_seeds.py — source={args.source} lookback={lookback}d")
    print(f"Loaded {len(ledger.get('seeds', {}))} seeds in ledger.")

    candidates: list[dict] = []
    if args.source in ("sam-gov", "all"):
        print("\n→ SAM.gov pre-solicitation notices")
        sam_c = _query_sam_gov(lookback)
        print(f"  {len(sam_c)} candidates from SAM.gov")
        candidates.extend(sam_c)
    if args.source in ("war-gov", "all"):
        print("\n→ war.gov daily contracts")
        war_c = _query_war_gov(lookback)
        print(f"  {len(war_c)} candidates from war.gov (v1 stub — see note in code)")
        candidates.extend(war_c)
    if args.source in ("comptroller", "all"):
        print("\n→ DoD comptroller justification books")
        compt_c = _query_comptroller(lookback)
        print(f"  {len(compt_c)} candidates from comptroller (v1 stub — flags only)")
        candidates.extend(compt_c)

    print(f"\nTotal raw candidates: {len(candidates)}")

    # Dedup against ledger
    new_candidates = []
    skipped_dupe = 0
    for c in candidates:
        fp = _fingerprint(c)
        if fp in ledger.get("seeds", {}):
            skipped_dupe += 1
            ledger["seeds"][fp]["last_seen_utc"] = _utc_now()
            continue
        new_candidates.append((c, fp))
    print(f"After dedup: {len(new_candidates)} new candidates ({skipped_dupe} already in ledger)")

    # Score
    scored = []
    for c, fp in new_candidates:
        score = _score_candidate(c, cfg)
        status = _decide_status(score, cfg)
        scored.append({"candidate": c, "fingerprint": fp, "score": score, "status": status})

    # Surface promote-eligible + monitor-eligible to inbox
    surfaced = [s for s in scored if s["status"] in ("promote-eligible", "monitor-eligible")]
    surfaced.sort(key=lambda s: -s["score"]["final_score"])

    print(f"\nScored: {len(scored)} total")
    print(f"  Promote-eligible (≥ {cfg['thresholds']['min_score_to_promote']}): {sum(1 for s in scored if s['status'] == 'promote-eligible')}")
    print(f"  Monitor-eligible (≥ {cfg['thresholds']['min_score_to_monitor']}): {sum(1 for s in scored if s['status'] == 'monitor-eligible')}")
    print(f"  Below-threshold: {sum(1 for s in scored if s['status'] == 'below-threshold')}")

    if surfaced:
        print(f"\nSurfacing {len(surfaced)} to seeds-inbox:")
        for s in surfaced[:10]:
            print(f"  {s['score']['score_display']:8s} {s['candidate'].get('title', '')[:80]}")
        if len(surfaced) > 10:
            print(f"  ... and {len(surfaced) - 10} more")

    if not args.dry_run:
        if surfaced:
            _write_inbox(surfaced, cfg)
            print(f"\n✓ Wrote {len(surfaced)} seeds to {SEEDS_INBOX.relative_to(VAULT_ROOT)}")
        _update_ledger(ledger, scored)
        _save_ledger(ledger)
        print(f"✓ Updated ledger ({len(ledger.get('seeds', {}))} seeds tracked)")
    else:
        print("\n(dry-run: no files written)")


if __name__ == "__main__":
    main()

"""USAspending.gov API client.

Mirrors sam_gov.py's shape:
    parse_search_entry(entry, date_window_days)
    execute_query(params, max_candidates)
    fetch_award_by_id(generated_id_or_piid)
    ingest_award(opp_dir, candidate)

No API key required. Polite throttle (5 req/sec ceiling) and a daily counter
in _meta/usaspending-quota.json for visibility (no hard limit enforced).
"""

import json
import re
import sys
import time
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import requests

VAULT_ROOT = Path(__file__).parent.parent.parent
QUOTA_FILE = VAULT_ROOT / "_meta" / "usaspending-quota.json"

SEARCH_URL = "https://api.usaspending.gov/api/v2/search/spending_by_award/"
AWARD_URL = "https://api.usaspending.gov/api/v2/awards/{}/"

RATE_LIMIT_PER_SEC = 5
_MIN_INTERVAL = 1.0 / RATE_LIMIT_PER_SEC
_last_request_time = 0.0

# Contract award type codes per USAspending docs
_CONTRACT_TYPE_CODES = ["A", "B", "C", "D"]


# ── Search-entry parsing ────────────────────────────────────────────────

def parse_search_entry(entry, date_window_days: int) -> dict:
    """Normalize a usa_spending_searches entry into a filters dict.

    Entry forms:
        "Deloitte INDOPACOM"                          # bare string, treated as recipient keyword
        {"keywords": ["INDOPACOM Alpha"]}             # full-text on description
        {"recipient": "Deloitte"}                     # recipient name search
        {"recipient": "Deloitte", "state": "HI"}      # add place-of-performance filter
        {"piid": "47QFCA25F0010"}                     # specific award lookup
        {"keywords": [...], "recipient": "...", "state": "HI", "start": "2024-01-01"}
    """
    if isinstance(entry, str):
        entry = {"keywords": [entry]}

    if not isinstance(entry, dict):
        raise ValueError(f"Unrecognized usa_spending_searches entry: {entry!r}")

    return _build_filters(entry, date_window_days)


def _build_filters(entry: dict, date_window_days: int) -> dict:
    filters: dict = {"award_type_codes": _CONTRACT_TYPE_CODES}

    if entry.get("keywords"):
        kws = entry["keywords"]
        filters["keywords"] = kws if isinstance(kws, list) else [kws]

    if entry.get("recipient"):
        filters["recipient_search_text"] = [entry["recipient"]]

    if entry.get("piid"):
        # Search by PIID via keyword (USAspending doesn't have a piid filter on search)
        filters.setdefault("keywords", []).append(entry["piid"])

    if entry.get("state"):
        filters["place_of_performance_locations"] = [
            {"country": "USA", "state": entry["state"]}
        ]

    # Time window: prefer explicit start/end; else use date_window_days from today
    today = date.today()
    end = entry.get("end") or today.isoformat()
    start = entry.get("start") or (today - timedelta(days=date_window_days)).isoformat()
    filters["time_period"] = [{"start_date": start, "end_date": end}]

    return filters


# ── Query execution ─────────────────────────────────────────────────────

def execute_query(filters: dict, max_candidates: int = 100) -> list[dict]:
    """Search USAspending awards. Returns normalized candidate dicts."""
    body = {
        "filters": filters,
        "fields": [
            "Award ID", "Recipient Name", "Description", "Award Amount",
            "Awarding Agency", "Awarding Sub Agency",
            "Funding Agency", "Funding Sub Agency",
            "Start Date", "End Date",
            "Place of Performance State Code",
            "Place of Performance City Code",
            "Total Outlays",
            "generated_internal_id",
        ],
        "page": 1,
        "limit": min(int(max_candidates), 100),
        "sort": "Award Amount",
        "order": "desc",
    }

    _throttle()
    try:
        r = requests.post(SEARCH_URL, json=body, timeout=60)
    except requests.RequestException as e:
        raise RuntimeError(f"USAspending network error: {e}")
    _increment_quota()

    if r.status_code != 200:
        raise RuntimeError(f"USAspending HTTP {r.status_code}: {r.text[:300]}")

    raw_results = r.json().get("results") or []
    return [_normalize_award(row, filters) for row in raw_results]


def fetch_award_by_id(generated_id: str) -> dict | None:
    """Fetch full award detail by generated_internal_id."""
    if not generated_id:
        return None
    _throttle()
    try:
        r = requests.get(AWARD_URL.format(generated_id), timeout=60)
    except requests.RequestException as e:
        raise RuntimeError(f"USAspending network error: {e}")
    _increment_quota()

    if r.status_code == 404:
        return None
    if r.status_code != 200:
        raise RuntimeError(f"USAspending HTTP {r.status_code}: {r.text[:300]}")
    return r.json()


def find_award_by_piid(piid: str) -> dict | None:
    """Look up an award by its PIID (PIID is not a direct API filter — search by keyword)."""
    filters = {
        "award_type_codes": _CONTRACT_TYPE_CODES,
        "keywords": [piid],
        "time_period": [{"start_date": "2007-10-01",
                         "end_date": date.today().isoformat()}],
    }
    results = execute_query(filters, max_candidates=5)
    for r in results:
        if r.get("award_id") == piid:
            return r
    return None


def _throttle() -> None:
    global _last_request_time
    elapsed = time.time() - _last_request_time
    if elapsed < _MIN_INTERVAL:
        time.sleep(_MIN_INTERVAL - elapsed)
    _last_request_time = time.time()


# ── Quota tracking (visibility, no hard limit) ──────────────────────────

def load_quota() -> dict:
    if not QUOTA_FILE.exists():
        return _fresh_quota()
    try:
        q = json.loads(QUOTA_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return _fresh_quota()
    if q.get("date_utc") != _today_utc():
        return _fresh_quota()
    return q


def _increment_quota() -> None:
    q = load_quota()
    q["requests_today"] += 1
    q["last_request"] = datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")
    _save_quota(q)


def _fresh_quota() -> dict:
    return {"date_utc": _today_utc(), "requests_today": 0, "last_request": ""}


def _save_quota(q: dict) -> None:
    QUOTA_FILE.parent.mkdir(parents=True, exist_ok=True)
    QUOTA_FILE.write_text(json.dumps(q, indent=2), encoding="utf-8")


def _today_utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


# ── Normalization ───────────────────────────────────────────────────────

def _normalize_award(row: dict, filters: dict) -> dict:
    piid = (row.get("Award ID") or "").strip()
    title = row.get("Description") or piid or "(no description)"
    amount = row.get("Award Amount") or 0
    recipient = row.get("Recipient Name") or ""
    start = row.get("Start Date") or ""
    end = row.get("End Date") or ""
    state = row.get("Place of Performance State Code") or ""
    awarder_top = row.get("Awarding Agency") or ""
    awarder_sub = row.get("Awarding Sub Agency") or ""
    funder_top = row.get("Funding Agency") or ""
    funder_sub = row.get("Funding Sub Agency") or ""
    generated_id = row.get("generated_internal_id") or ""

    url = f"https://www.usaspending.gov/award/{generated_id}/" if generated_id else ""

    # Query string for inbox display
    q_label = ", ".join(filters.get("keywords") or []) or \
              (filters.get("recipient_search_text") or ["(structured)"])[0]

    return {
        "source_type": "usa_spending",
        "award_id": piid,                 # the PIID
        "generated_id": generated_id,     # used for dedup and detail fetch
        "title": title[:200],
        "url": url,
        "model": "usaspending.gov",
        "query": q_label,
        "reason": f'matched search "{q_label}"',
        "recipient": recipient,
        "amount_obligated": amount,
        "start_date": start,
        "end_date": end,
        "state": state,
        "awarder": f"{awarder_top} / {awarder_sub}".strip(" /"),
        "funder": f"{funder_top} / {funder_sub}".strip(" /"),
        "raw": row,
    }


# ── Ingestion (called from approve_inbox.py) ────────────────────────────

def ingest_award(opp_dir: Path, candidate: dict) -> tuple[bool, str]:
    """Build and write a source file for an approved USAspending award."""
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from lib.frontmatter import build_usaspending_frontmatter
    from lib.ledger import update_ledger
    from slugify import slugify

    generated_id = candidate.get("generated_id", "")
    if not generated_id:
        return False, "no generated_internal_id in candidate"

    detail = fetch_award_by_id(generated_id)
    if not detail:
        return False, f"award {generated_id} not found via API"

    captured = date.today().isoformat()
    piid = detail.get("piid") or candidate.get("award_id") or "unknown"
    title = (detail.get("description") or candidate.get("title", piid))[:120]
    slug = slugify(title, max_length=60, separator="-") or piid.lower()
    filename = f"{captured}_usaspending-gov_{slug}.md"

    sources_dir = opp_dir / "01_sources"
    sources_dir.mkdir(exist_ok=True)
    target = sources_dir / filename
    if target.exists():
        target = sources_dir / f"{captured}_usaspending-gov_{slug}-{piid[:8]}.md"

    frontmatter = build_usaspending_frontmatter(
        opportunity=opp_dir.name,
        captured=captured,
        detail=detail,
        candidate=candidate,
    )

    body = _format_body(detail, candidate)
    target.write_text(frontmatter + body, encoding="utf-8")

    research_file = opp_dir / "00_research-file.md"
    citation_slug = f"{captured}-{slug[:30]}"
    if research_file.exists():
        update_ledger(research_file, citation_slug,
                      f"https://www.usaspending.gov/award/{generated_id}/", filename)

    try:
        return True, str(target.resolve().relative_to(VAULT_ROOT))
    except ValueError:
        return True, str(target)


def _format_body(detail: dict, candidate: dict) -> str:
    """Render the award body as a structured markdown block."""
    rcpt = detail.get("recipient") or {}
    aw = detail.get("awarding_agency") or {}
    fa = detail.get("funding_agency") or {}
    pop = detail.get("place_of_performance") or {}
    parent = detail.get("parent_award") or {}

    parent_block = ""
    if parent:
        parent_block = (
            f"\n### Parent IDV / contract\n"
            f"- PIID: `{parent.get('piid', '')}`\n"
            f"- Description: {parent.get('idv_type_description') or ''} ({parent.get('type_of_idc_description') or ''})\n"
            f"- Multiple/Single Award: {parent.get('multiple_or_single_aw_desc') or ''}\n"
            f"- Agency: {parent.get('agency_name', '')} / sub {parent.get('sub_agency_name', '')}\n"
        )

    obl = detail.get("total_obligation")
    ceiling = detail.get("base_and_all_options_value")

    return (
        "\n## Summary\n\n"
        "\n\n"
        "## Award record\n\n"
        f"- **PIID:** `{detail.get('piid', '')}`\n"
        f"- **Type:** {detail.get('type_description', '')}\n"
        f"- **Category:** {detail.get('category', '')}\n"
        f"- **Description:** {detail.get('description', '')}\n"
        f"- **Recipient:** {rcpt.get('recipient_name', '')} (UEI {rcpt.get('recipient_uei', '')})\n"
        f"- **Awarding agency:** {aw.get('toptier_agency', {}).get('name', '')} / "
        f"{aw.get('subtier_agency', {}).get('name', '')}\n"
        f"- **Funding agency:** {fa.get('toptier_agency', {}).get('name', '')} / "
        f"{fa.get('subtier_agency', {}).get('name', '')}\n"
        f"- **Place of performance:** {pop.get('city_name') or ''}, "
        f"{pop.get('state_code') or ''} {pop.get('country_code') or ''}\n"
        f"- **Period start:** {detail.get('period_of_performance_start_date') or candidate.get('start_date', '')}\n"
        f"- **Period current end:** {detail.get('period_of_performance_current_end_date') or candidate.get('end_date', '')}\n"
        f"- **Total obligation:** ${obl:,.0f}\n" if isinstance(obl, (int, float)) and obl else
        f"- **Total obligation:** (not reported)\n"
    ) + (
        f"- **Base + all options value (ceiling):** ${ceiling:,.0f}\n" if isinstance(ceiling, (int, float)) and ceiling else
        f"- **Base + all options value (ceiling):** (not reported)\n"
    ) + parent_block + "\n## Notes\n\n"

"""SAM.gov opportunities API client.

Public functions:
    parse_search_entry(entry, date_window_days)
    execute_query(params, api_key, max_candidates)
    fetch_notice_by_id(notice_id, api_key)
    ingest_notice(opp_dir, candidate, api_key)
    load_quota()  /  quota_paused()

Quota is tracked per UTC day in _meta/sam-quota.json. Throttling enforces
a 5 req/sec ceiling (half the documented 10/sec) regardless of caller.
"""

import json
import os
import re
import sys
import time
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import requests

VAULT_ROOT = Path(__file__).parent.parent.parent
QUOTA_FILE = VAULT_ROOT / "_meta" / "sam-quota.json"

SAM_API_URL = "https://api.sam.gov/opportunities/v2/search"

DAILY_LIMIT = 1000
SAFETY_PAUSE_AT = 900
RATE_LIMIT_PER_SEC = 2   # conservative; SAM.gov burst-throttles below 10/sec
_MIN_INTERVAL = 1.0 / RATE_LIMIT_PER_SEC

_last_request_time = 0.0


# ── Search-entry parsing ────────────────────────────────────────────────

# UI param → API param mapping for keys whose names diverge
_UI_TO_API = {
    "is_active": None,        # handled separately (filters to active=Yes)
    "page": None,             # UI-only, no API equivalent
    "sort": None,
    "index": None,
    "modified_date.to": "modifiedTo",
    "modified_date.from": "modifiedFrom",
    "response_date.to": "rdlto",
    "response_date.from": "rdlfrom",
}

# API params we accept verbatim from URL query strings
_API_PARAMS = {
    "q", "noticeId", "solnum", "ncode", "ccode",
    "typeOfSetAside", "typeOfSetAsideDescription",
    "postedFrom", "postedTo",
    "rdlfrom", "rdlto",
    "modifiedFrom", "modifiedTo",
    "deptname", "subtier", "organizationCode",
    "state", "zip",
}


def parse_search_entry(entry, date_window_days: int) -> dict:
    """Normalize a sam_searches config entry to a dict of API parameters."""
    if isinstance(entry, str):
        return _parse_url(entry, date_window_days)
    if isinstance(entry, dict):
        if "url" in entry:
            return _parse_url(entry["url"], date_window_days)
        if "params" in entry:
            params = {k: v for k, v in (entry["params"] or {}).items() if v is not None}
            _normalize_list_params(params)
            _apply_default_dates(params, date_window_days)
            return params
    raise ValueError(f"Unrecognized sam_searches entry: {entry!r}")


def _parse_url(url: str, date_window_days: int) -> dict:
    parsed = urlparse(url)
    qs = parse_qs(parsed.query)
    params: dict = {}
    for key, values in qs.items():
        if key in _API_PARAMS:
            params[key] = ",".join(values) if len(values) > 1 else values[0]
            continue
        mapped = _UI_TO_API.get(key)
        if mapped:
            params[mapped] = values[0]
    _normalize_list_params(params)
    _apply_default_dates(params, date_window_days)
    return params


def _normalize_list_params(params: dict) -> None:
    """If a param is a list, convert to comma-separated string (SAM API style)."""
    for k, v in list(params.items()):
        if isinstance(v, list):
            params[k] = ",".join(str(x) for x in v)


def _apply_default_dates(params: dict, date_window_days: int) -> None:
    today = date.today()
    if not params.get("postedTo"):
        params["postedTo"] = today.strftime("%m/%d/%Y")
    if not params.get("postedFrom"):
        params["postedFrom"] = (today - timedelta(days=date_window_days)).strftime("%m/%d/%Y")


# ── Query execution ─────────────────────────────────────────────────────

class SamGovKeyError(Exception):
    """Raised when SAM.gov rejects the API key (401/403)."""


def execute_query(params: dict, api_key: str, max_candidates: int = 100) -> list[dict]:
    """Call the search endpoint once. Returns normalized candidate dicts.

    Raises SamGovKeyError on 401/403. Honors quota and rate-limit pauses.
    Performs one retry on 429 with backoff.
    """
    if quota_paused():
        return []

    call = dict(params)
    call["api_key"] = api_key
    call["limit"] = min(int(max_candidates), 1000)

    resp = _request_with_retry(SAM_API_URL, call)
    data = resp.json()
    notices = data.get("opportunitiesData") or []
    return [_normalize_notice(n, params) for n in notices]


def fetch_notice_by_id(notice_id: str, api_key: str) -> dict | None:
    """Re-query SAM.gov for a single notice at approval time.

    SAM.gov caps date ranges at 1 year; we sweep backwards in 360-day windows
    until the notice is found or we exhaust 5 years.
    """
    if quota_paused():
        return None
    today = date.today()
    for years_back in range(0, 5):
        to_dt = today - timedelta(days=years_back * 360)
        from_dt = to_dt - timedelta(days=360)
        params = {
            "api_key": api_key,
            "noticeId": notice_id,
            "limit": 1,
            "postedFrom": from_dt.strftime("%m/%d/%Y"),
            "postedTo": to_dt.strftime("%m/%d/%Y"),
        }
        try:
            resp = _request_with_retry(SAM_API_URL, params)
        except SamGovKeyError:
            raise
        except Exception:
            continue
        notices = (resp.json().get("opportunitiesData") or [])
        if notices:
            return _normalize_notice(notices[0], {"q": ""})
    return None


def fetch_description(desc_url: str, api_key: str) -> str:
    """Fetch the description text from the noticedesc endpoint."""
    if not desc_url:
        return ""
    try:
        _throttle()
        sep = "&" if "?" in desc_url else "?"
        r = requests.get(f"{desc_url}{sep}api_key={api_key}", timeout=30)
        _increment_quota()
        if r.status_code != 200:
            return ""
        body = r.json()
        if isinstance(body, dict):
            return body.get("description") or ""
        return ""
    except (requests.RequestException, json.JSONDecodeError):
        return ""


def _request_with_retry(url: str, params: dict) -> requests.Response:
    _throttle()
    try:
        r = requests.get(url, params=params, timeout=30)
    except requests.RequestException as e:
        raise RuntimeError(f"SAM.gov network error: {e}")
    _increment_quota()

    if r.status_code in (401, 403):
        raise SamGovKeyError(
            "SAM.gov API rejected key. Verify SAM_GOV_API_KEY in .env."
        )
    if r.status_code == 429:
        time.sleep(5.0)
        _throttle()
        r = requests.get(url, params=params, timeout=30)
        _increment_quota()

    r.raise_for_status()
    return r


def _throttle() -> None:
    global _last_request_time
    elapsed = time.time() - _last_request_time
    if elapsed < _MIN_INTERVAL:
        time.sleep(_MIN_INTERVAL - elapsed)
    _last_request_time = time.time()


# ── Quota tracking ──────────────────────────────────────────────────────

def load_quota() -> dict:
    """Return today's quota state (initializes if absent or stale)."""
    if not QUOTA_FILE.exists():
        return _fresh_quota()
    try:
        q = json.loads(QUOTA_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return _fresh_quota()
    if q.get("date_utc") != _today_utc():
        return _fresh_quota()
    return q


def quota_paused() -> bool:
    """True when we have hit the safety pause threshold."""
    q = load_quota()
    if q["requests_today"] >= SAFETY_PAUSE_AT:
        q["throttle_warnings"] = q.get("throttle_warnings", 0) + 1
        _save_quota(q)
        return True
    return False


def _increment_quota() -> None:
    q = load_quota()
    q["requests_today"] += 1
    q["last_request"] = datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")
    _save_quota(q)


def _fresh_quota() -> dict:
    return {
        "date_utc": _today_utc(),
        "requests_today": 0,
        "last_request": "",
        "throttle_warnings": 0,
    }


def _save_quota(q: dict) -> None:
    QUOTA_FILE.parent.mkdir(parents=True, exist_ok=True)
    QUOTA_FILE.write_text(json.dumps(q, indent=2), encoding="utf-8")


def _today_utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


# ── Normalization ───────────────────────────────────────────────────────

def _normalize_notice(n: dict, query_params: dict) -> dict:
    notice_id = (n.get("noticeId") or "").strip()
    title = (n.get("title") or "(untitled notice)").strip()
    notice_type = n.get("type") or n.get("baseType") or ""
    posted = (n.get("postedDate") or "")[:10]
    deadline = _short_date(n.get("responseDeadLine"))
    set_aside = (n.get("typeOfSetAsideDescription")
                 or n.get("typeOfSetAside") or "None")
    naics_codes = n.get("naicsCodes") or []
    naics = naics_codes if naics_codes else (
        [n["naicsCode"]] if n.get("naicsCode") else []
    )
    path = (n.get("fullParentPathName") or "").split(".")
    department = path[0] if path else ""
    subtier = path[1] if len(path) > 1 else ""
    office = ".".join(path[2:]) if len(path) > 2 else ""

    url = n.get("uiLink") or (
        f"https://sam.gov/opp/{notice_id}/view" if notice_id else ""
    )

    attachments = []
    for link in (n.get("resourceLinks") or []):
        if not link:
            continue
        name = link.rstrip("/").split("/")[-1]
        # The noticefile download URL ends in /download — strip query for name
        name = re.sub(r'\?.*$', '', name) or "attachment"
        if name == "download":
            name = "attachment"
        attachments.append({"name": name, "url": link})

    flags = []
    if (n.get("active") or "").strip().lower() == "no":
        flags.append("CLOSED")
    if "cancel" in (n.get("type", "").lower()):
        flags.append("CANCELLED")

    query_str = query_params.get("q") or "(structured query)"

    return {
        "source_type": "sam_gov",
        "notice_id": notice_id,
        "title": title,
        "url": url,
        "model": "sam.gov",
        "query": query_str,
        "reason": f'matched query "{query_str}"',
        "notice_type": notice_type,
        "posted_date": posted,
        "response_deadline": deadline,
        "set_aside": set_aside,
        "naics": naics,
        "department": department,
        "subtier": subtier,
        "office": office,
        "description_url": n.get("description") or "",
        "attachments": attachments,
        "flags": flags,
        "solicitation_number": n.get("solicitationNumber") or "",
        "active": n.get("active") or "",
        "raw": n,
    }


def _short_date(value) -> str:
    if not value:
        return ""
    return str(value)[:10]


# ── Ingestion (called from approve_inbox.py) ────────────────────────────

def ingest_notice(opp_dir: Path, candidate: dict, api_key: str) -> tuple[bool, str]:
    """Build and write a source file for an approved SAM.gov notice.

    Returns (success, message). Re-fetches the notice by ID for current metadata
    and pulls description text from the noticedesc endpoint.
    """
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from lib.frontmatter import build_sam_frontmatter
    from lib.ledger import update_ledger
    from slugify import slugify

    notice_id = candidate.get("notice_id", "")
    if not notice_id:
        return False, "no notice ID in candidate"

    fresh = fetch_notice_by_id(notice_id, api_key)
    if not fresh:
        return False, f"notice {notice_id} not found via API (may have been removed)"

    description = fetch_description(fresh.get("description_url", ""), api_key)

    captured = date.today().isoformat()
    title = fresh["title"]
    slug = slugify(title, max_length=60, separator="-") or notice_id[:12]
    filename = f"{captured}_sam-gov_{slug}.md"

    sources_dir = opp_dir / "01_sources"
    sources_dir.mkdir(exist_ok=True)
    target = sources_dir / filename
    if target.exists():
        # Append notice-id suffix to avoid collision
        target = sources_dir / f"{captured}_sam-gov_{slug}-{notice_id[:8]}.md"

    frontmatter = build_sam_frontmatter(
        opportunity=opp_dir.name,
        captured=captured,
        candidate=fresh,
    )

    body = (
        "\n## Summary\n\n"
        "\n\n"
        "## Notice description\n\n"
        f"{description.strip() or '(description not provided by SAM.gov)'}\n\n"
        "## Notes\n\n"
    )

    target.write_text(frontmatter + body, encoding="utf-8")

    # Update source ledger
    research_file = opp_dir / "00_research-file.md"
    citation_slug = f"{captured}-{slug[:30]}"
    if research_file.exists():
        update_ledger(research_file, citation_slug, fresh["url"], filename)

    try:
        return True, str(target.resolve().relative_to(VAULT_ROOT))
    except ValueError:
        return True, str(target)

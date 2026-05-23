#!/usr/bin/env python3
"""
audit_search_config.py — Catch named entities in _search-config.yaml queries
that don't appear in any ingested source.

Usage:
    python audit_search_config.py --opportunity BDR-FLEET-READINESS
    python audit_search_config.py --all

The script targets the pollution pattern where an analyst pre-loads a specific
commercial contractor name (or product, or named person) into a search query
based on inferred context. The downstream find_sources hits then look like
"organic" surfacing but are actually downstream of the analyst-seeded query.

The audit reads the named-entity watchlist at _meta/named-entities-watchlist.yaml
and flags any query in _search-config.yaml that contains a watchlist entity
which does NOT appear in any of the opportunity's ingested sources.

Exit code 0 if all queries are clean, 1 if any contaminated queries are found.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

SCRIPT_DIR = Path(__file__).parent
VAULT_ROOT = SCRIPT_DIR.parent
WATCHLIST_FILE = VAULT_ROOT / "_meta" / "named-entities-watchlist.yaml"


def _load_watchlist() -> list[str]:
    with open(WATCHLIST_FILE, encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    entities: set[str] = set()
    for _category, names in data.items():
        if isinstance(names, list):
            for n in names:
                if n and isinstance(n, str):
                    entities.add(n.strip())
    return sorted(entities, key=lambda s: (-len(s), s))


def _load_opportunity_allowlist(opp_dir: Path) -> dict[str, str]:
    """Read the per-opportunity allowlist file if it exists. Returns a dict
    mapping entity name to operator's reason. Empty dict if no allowlist."""
    path = opp_dir / "_entity-allowlist.yaml"
    if not path.exists():
        return {}
    try:
        with open(path, encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
    except Exception:
        return {}
    allowlist = data.get("allowlist") or {}
    if not isinstance(allowlist, dict):
        return {}
    return {str(k).strip(): str(v).strip() if v else "" for k, v in allowlist.items()}


def _count_in_text(entity: str, text: str) -> int:
    pattern = r'(?:^|[^A-Za-z0-9_])' + re.escape(entity) + r'(?=[^A-Za-z0-9_]|$)'
    return len(re.findall(pattern, text, re.IGNORECASE))


def _entity_in_sources(entity: str, opp_dir: Path) -> int:
    """Count total occurrences of entity across all ingested source files for
    this opportunity. Case-insensitive because the source files often have
    inconsistent capitalization."""
    sources_dir = opp_dir / "01_sources"
    if not sources_dir.exists():
        return 0
    total = 0
    for path in sources_dir.glob("*.md"):
        if "_quarantine" in str(path):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except Exception:
            continue
        total += _count_in_text(entity, text)
    return total


def _collect_query_strings(config: dict) -> list[tuple[str, str]]:
    """Pull every text query out of the search-config structure. Returns a
    list of (section, query_string) tuples for reporting."""
    queries: list[tuple[str, str]] = []

    for q in (config.get("ai_searches") or []):
        if isinstance(q, str):
            queries.append(("ai_searches", q))

    for entry in (config.get("sam_searches") or []):
        if isinstance(entry, dict):
            if "url" in entry:
                queries.append(("sam_searches", entry["url"]))
            elif "params" in entry:
                params = entry.get("params") or {}
                q = params.get("q")
                if q:
                    queries.append(("sam_searches", q))
                ncode = params.get("ncode")
                if ncode:
                    queries.append(("sam_searches.ncode", str(ncode)))
        elif isinstance(entry, str):
            queries.append(("sam_searches", entry))

    for entry in (config.get("usa_spending_searches") or []):
        if isinstance(entry, dict):
            kws = entry.get("keywords") or []
            for k in kws:
                queries.append(("usa_spending_searches.keywords", k))
            recipient = entry.get("recipient")
            if recipient:
                queries.append(("usa_spending_searches.recipient", recipient))
        elif isinstance(entry, str):
            queries.append(("usa_spending_searches", entry))

    return queries


def _audit_opportunity(opp_dir: Path, watchlist: list[str]) -> int:
    """Run the audit against one opportunity's search config. Returns count
    of contaminated queries (excluding operator-allowlisted entities)."""
    print(f"\n{'=' * 70}")
    print(f"Auditing search config: {opp_dir.name}")
    print(f"{'=' * 70}")

    cfg_path = opp_dir / "_search-config.yaml"
    if not cfg_path.exists():
        print(f"  No _search-config.yaml — skipping.")
        return 0

    with open(cfg_path, encoding="utf-8") as f:
        config = yaml.safe_load(f) or {}

    allowlist = _load_opportunity_allowlist(opp_dir)
    queries = _collect_query_strings(config)
    print(f"Total queries in config: {len(queries)}")
    print(f"Allowlisted entities:    {len(allowlist)}")

    contaminated: list[tuple[str, str, list[str]]] = []
    allowlisted_in_queries: list[tuple[str, str, list[str]]] = []

    for section, query in queries:
        not_in_sources_not_allowlisted: list[str] = []
        not_in_sources_allowlisted: list[str] = []
        for entity in watchlist:
            if _count_in_text(entity, query) > 0:
                source_count = _entity_in_sources(entity, opp_dir)
                if source_count == 0:
                    if entity in allowlist:
                        not_in_sources_allowlisted.append(entity)
                    else:
                        not_in_sources_not_allowlisted.append(entity)
        if not_in_sources_not_allowlisted:
            contaminated.append((section, query, not_in_sources_not_allowlisted))
        if not_in_sources_allowlisted:
            allowlisted_in_queries.append((section, query, not_in_sources_allowlisted))

    if contaminated:
        print(f"\n❌ CONTAMINATED — {len(contaminated)} query/queries naming non-allowlisted entities NOT in any ingested source:")
        for section, query, entities in contaminated:
            print(f"\n  [{section}]  {query[:100]}{'...' if len(query) > 100 else ''}")
            for e in entities:
                print(f"     ↳ entity not in sources and not allowlisted: {e}")
    else:
        print(f"\n✓ All queries are clean. No non-allowlisted watchlist entities appear in queries without source support.")

    if allowlisted_in_queries:
        print(f"\n✓ ALLOWLISTED — {len(allowlisted_in_queries)} query/queries naming allowlisted entities without source support:")
        print(f"   (these are operator-blessed and do not fail the audit)")
        for section, query, entities in allowlisted_in_queries:
            print(f"\n  [{section}]  {query[:100]}{'...' if len(query) > 100 else ''}")
            for e in entities:
                reason = allowlist.get(e, "")
                note = f" — {reason}" if reason else ""
                print(f"     ↳ {e}{note}")

    return len(contaminated)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Audit _search-config.yaml for queries naming entities that don't appear in any ingested source.",
    )
    parser.add_argument(
        "--opportunity",
        metavar="ID",
        help="Audit a single opportunity.",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Audit every opportunity folder.",
    )
    args = parser.parse_args()

    if not WATCHLIST_FILE.exists():
        print(f"ERROR: Watchlist file not found: {WATCHLIST_FILE}", file=sys.stderr)
        sys.exit(2)

    watchlist = _load_watchlist()
    print(f"Loaded {len(watchlist)} entity name(s) from {WATCHLIST_FILE.relative_to(VAULT_ROOT)}")

    total_contaminated = 0

    if args.opportunity:
        opp_dir = VAULT_ROOT / "opportunities" / args.opportunity
        if not opp_dir.exists():
            print(f"ERROR: Opportunity folder not found: {opp_dir}", file=sys.stderr)
            sys.exit(2)
        total_contaminated = _audit_opportunity(opp_dir, watchlist)
    elif args.all:
        opp_root = VAULT_ROOT / "opportunities"
        for opp_dir in sorted(opp_root.glob("*")):
            if opp_dir.is_dir():
                total_contaminated += _audit_opportunity(opp_dir, watchlist)
    else:
        print("ERROR: specify --opportunity ID or --all", file=sys.stderr)
        sys.exit(2)

    print(f"\n{'=' * 70}")
    if total_contaminated == 0:
        print(f"✓ AUDIT PASS — all search-config queries are clean.")
    else:
        print(f"❌ AUDIT FAIL — {total_contaminated} contaminated query/queries found.")
        print(f"   Remove the named entity from the query OR ingest a source that supports it.")
    print(f"{'=' * 70}\n")

    sys.exit(0 if total_contaminated == 0 else 1)


if __name__ == "__main__":
    main()

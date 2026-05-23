#!/usr/bin/env python3
"""
audit_named_entities.py — Catch named entities in vault analytical content
that don't appear in any ingested source.

Usage:
    python audit_named_entities.py --opportunity BDR-FLEET-READINESS
    python audit_named_entities.py --vault  # scan _meta/glossary.md against all opportunities

The audit catches the pattern where an analyst introduces a specific
commercial contractor, product, or program name into analytical content
(research file, glossary, points-of-contact directory) based on inferred
context rather than source content. The watchlist of tracked entities lives
at _meta/named-entities-watchlist.yaml.

The script reports three buckets:
  - CONTAMINATED: entity appears in analytical content but in zero sources
  - OK: entity appears in both analytical content and at least one source
  - SOURCE-ONLY: entity appears in sources but not yet in analytical content
                 (informational — may be worth incorporating)

Exit code 0 if no contaminated entries are found, 1 otherwise. This lets the
script run as a pre-commit hook or as part of sync.sh.
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
    """Read the watchlist file and flatten its categories into a deduplicated
    list of entity names, longest first so multi-word entries match before
    shorter substrings."""
    with open(WATCHLIST_FILE, encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    entities: set[str] = set()
    for _category, names in data.items():
        if isinstance(names, list):
            for n in names:
                if n and isinstance(n, str):
                    entities.add(n.strip())
    return sorted(entities, key=lambda s: (-len(s), s))


def _count_in_text(entity: str, text: str) -> int:
    """Case-sensitive whole-word count, allowing common punctuation around the
    entity. Uses word boundary regex so 'CACI' doesn't match inside 'CACIIs'."""
    pattern = r'(?:^|[^A-Za-z0-9_])' + re.escape(entity) + r'(?=[^A-Za-z0-9_]|$)'
    return len(re.findall(pattern, text))


def _scan_files(files: list[Path], entity: str) -> list[tuple[Path, int, str]]:
    """For each file, return a list of (path, line_number, line_content) hits.
    Returns at most one hit per file (the first occurrence)."""
    hits: list[tuple[Path, int, str]] = []
    for f in files:
        if not f.exists():
            continue
        try:
            lines = f.read_text(encoding="utf-8").splitlines()
        except Exception:
            continue
        for i, line in enumerate(lines, start=1):
            if _count_in_text(entity, line) > 0:
                hits.append((f, i, line.strip()))
                break
    return hits


def _analytical_files_for_opportunity(opp_dir: Path) -> list[Path]:
    """Files that count as analytical content for a given opportunity. NOT
    inclusive of 01_sources/ (those are checked separately) and NOT inclusive
    of _inbox.md or _rejected.md (those are operator-triage state, not
    analyst-authored prose)."""
    return [
        opp_dir / "00_research-file.md",
        opp_dir / "_glossary.md",
        opp_dir / "02_quotes.md",
        opp_dir / "03_pocs.md",
        opp_dir / "05_decision-log.md",
        opp_dir / "index.md",
    ]


def _source_files_for_opportunity(opp_dir: Path) -> list[Path]:
    sources_dir = opp_dir / "01_sources"
    if not sources_dir.exists():
        return []
    # Exclude the quarantine sub-directory; those files don't count as ingested
    return [p for p in sorted(sources_dir.glob("*.md")) if "_quarantine" not in str(p)]


def _config_files_for_opportunity(opp_dir: Path) -> list[Path]:
    return [opp_dir / "_search-config.yaml"]


def _audit_opportunity(opp_dir: Path, watchlist: list[str]) -> int:
    """Run the audit against one opportunity. Returns count of contaminated entries."""
    print(f"\n{'=' * 70}")
    print(f"Auditing opportunity: {opp_dir.name}")
    print(f"{'=' * 70}")

    analytical_files = _analytical_files_for_opportunity(opp_dir)
    source_files = _source_files_for_opportunity(opp_dir)
    config_files = _config_files_for_opportunity(opp_dir)

    print(f"Analytical files scanned: {sum(1 for f in analytical_files if f.exists())}")
    print(f"Source files scanned:     {len(source_files)}")
    print(f"Config files scanned:     {sum(1 for f in config_files if f.exists())}")

    contaminated: list[tuple[str, list[tuple[Path, int, str]]]] = []
    ok: list[tuple[str, int, int]] = []
    source_only: list[tuple[str, int]] = []

    for entity in watchlist:
        analytical_hits = _scan_files(analytical_files, entity)
        source_hits = _scan_files(source_files, entity)
        config_hits = _scan_files(config_files, entity)

        analytical_count = len(analytical_hits)
        config_count = len(config_hits)
        source_count = len(source_hits)
        appearing_in_writing = analytical_count + config_count

        if appearing_in_writing > 0 and source_count == 0:
            contaminated.append((entity, analytical_hits + config_hits))
        elif appearing_in_writing > 0 and source_count > 0:
            ok.append((entity, appearing_in_writing, source_count))
        elif appearing_in_writing == 0 and source_count > 0:
            source_only.append((entity, source_count))

    if contaminated:
        print(f"\n❌ CONTAMINATED — {len(contaminated)} entity name(s) in vault content but in ZERO sources:")
        for entity, hits in contaminated:
            print(f"\n  {entity}")
            for path, lineno, line in hits[:3]:
                rel = path.relative_to(VAULT_ROOT) if path.is_relative_to(VAULT_ROOT) else path
                snippet = line[:120] + ("..." if len(line) > 120 else "")
                print(f"     · {rel}:{lineno}")
                print(f"        {snippet}")
            if len(hits) > 3:
                print(f"     · ... and {len(hits) - 3} more file(s)")
    else:
        print(f"\n✓ No contaminated entities. All names in analytical/config content are source-backed.")

    if ok:
        print(f"\n✓ OK — {len(ok)} entity name(s) appearing in both vault content and ingested sources:")
        for entity, writing_count, source_count in ok:
            print(f"     {entity:<40}  writing={writing_count}  sources={source_count}")

    if source_only:
        print(f"\n· SOURCE-ONLY — {len(source_only)} entity name(s) in sources but not yet in vault content:")
        print(f"   (informational — these names appeared in ingested material but the analyst has not yet written them into the research file)")
        for entity, source_count in source_only:
            print(f"     {entity:<40}  sources={source_count}")

    return len(contaminated)


def _audit_vault(watchlist: list[str]) -> int:
    """Audit _meta/glossary.md against every opportunity's sources."""
    print(f"\n{'=' * 70}")
    print(f"Auditing vault-wide glossary against all opportunity sources")
    print(f"{'=' * 70}")

    glossary = VAULT_ROOT / "_meta" / "glossary.md"
    if not glossary.exists():
        print(f"WARN: {glossary} does not exist.")
        return 0

    opp_root = VAULT_ROOT / "opportunities"
    all_sources: list[Path] = []
    for opp_dir in sorted(opp_root.glob("*")):
        if opp_dir.is_dir():
            all_sources.extend(_source_files_for_opportunity(opp_dir))

    print(f"Glossary file: {glossary.relative_to(VAULT_ROOT)}")
    print(f"Sources across all opportunities: {len(all_sources)}")

    contaminated_count = 0
    for entity in watchlist:
        glossary_hits = _scan_files([glossary], entity)
        if not glossary_hits:
            continue
        source_hits = _scan_files(all_sources, entity)
        if not source_hits:
            contaminated_count += 1
            print(f"\n❌ {entity}")
            for path, lineno, line in glossary_hits[:1]:
                rel = path.relative_to(VAULT_ROOT)
                snippet = line[:120] + ("..." if len(line) > 120 else "")
                print(f"     · {rel}:{lineno}")
                print(f"        {snippet}")

    if contaminated_count == 0:
        print(f"\n✓ No contaminated entities in vault glossary.")

    return contaminated_count


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Audit vault content for named entities that don't appear in ingested sources.",
    )
    parser.add_argument(
        "--opportunity",
        metavar="ID",
        help="Audit a single opportunity. If omitted, audits the vault-wide glossary against all opportunities.",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Audit every opportunity folder, one after the other.",
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
        total_contaminated += _audit_vault(watchlist)
    else:
        total_contaminated = _audit_vault(watchlist)

    print(f"\n{'=' * 70}")
    if total_contaminated == 0:
        print(f"✓ AUDIT PASS — 0 contaminated entries found.")
    else:
        print(f"❌ AUDIT FAIL — {total_contaminated} contaminated entry/entries found.")
        print(f"   Either ingest a source that supports the entity claim, or remove the entity from analytical content.")
    print(f"{'=' * 70}\n")

    sys.exit(0 if total_contaminated == 0 else 1)


if __name__ == "__main__":
    main()

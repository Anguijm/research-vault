#!/usr/bin/env python3
"""
sort_inbox.py — Re-sort _inbox.md by score so the highest-value items are at
the top regardless of which find_sources pass surfaced them.

The default ordering of _inbox.md is by append-date — each pass adds a new
"## Candidates added YYYY-MM-DD HH:MM" section. Within a section, items are
score-sorted. But across sections the highest-scored items can be buried
under earlier lower-scored items.

This tool flattens the dated sections into a single list ordered by:
  1. State (pending first, approved next, rejected last — though rejected
     items should already be in _rejected.md, not the inbox)
  2. Score descending (so 9/10 surfaces above 8/10 above 7/10)
  3. Added-date descending (newer wins on score ties, so freshest evidence
     surfaces first)

The dated section headers are replaced with a single "## Candidates (sorted
by score)" header. Per-item "Added: YYYY-MM-DD" lines preserve the temporal
metadata.

Usage:
    python sort_inbox.py --opportunity BDR-FLEET-READINESS
    python sort_inbox.py --opportunity BDR-FLEET-READINESS --dry-run
    python sort_inbox.py --opportunity BDR-FLEET-READINESS --top 30  (show top N only, archive the rest)

The original inbox is backed up to _inbox.md.bak before rewriting.
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
VAULT_ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))

from lib.inbox import parse_items


def _score_of(item: dict) -> int:
    """Extract the integer score from the item's block. Returns 0 if no score tag is found."""
    block = item.get("block", "")
    m = re.search(r'`(\d+)/10`', block)
    if m:
        return int(m.group(1))
    return 0


def _added_dt(item: dict) -> datetime:
    """Parse the 'Added: ISO-timestamp' line; return datetime.min on failure so
    items without a date sort to the bottom of the date tiebreaker."""
    raw = item.get("added", "")
    if not raw:
        return datetime.min
    try:
        return datetime.fromisoformat(raw)
    except (ValueError, TypeError):
        return datetime.min


def _state_priority(state: str) -> int:
    """Pending (' ') first, approved ('x') next, rejected ('-') last.
    Rejected items shouldn't be in the inbox at all but we handle them
    defensively."""
    if state == " ":
        return 0
    if state.lower() == "x":
        return 1
    return 2


def _sort_key(item: dict) -> tuple:
    # Negative score so DESC. Negative timestamp ordinal so newer = first.
    score = _score_of(item)
    dt = _added_dt(item)
    return (
        _state_priority(item["state"]),
        -score,
        -dt.timestamp() if dt != datetime.min else 0,
    )


def _split_preamble(text: str) -> tuple[str, str]:
    """Split inbox text into preamble (frontmatter + intro) and body (the
    Candidates sections). The preamble ends at the first '## Candidates' or
    '## SAM.gov candidates' or '## USAspending candidates' header."""
    m = re.search(r'^## (?:Candidates|SAM\.gov candidates|USAspending candidates)', text, re.MULTILINE)
    if not m:
        return text, ""
    return text[: m.start()].rstrip() + "\n", text[m.start():]


def _rewrite_inbox(opp_dir: Path, dry_run: bool, top_n: int | None) -> None:
    inbox_path = opp_dir / "_inbox.md"
    if not inbox_path.exists():
        print(f"ERROR: {inbox_path} does not exist.")
        sys.exit(1)

    items = parse_items(opp_dir)
    if not items:
        print("Inbox has no items to sort.")
        return

    sorted_items = sorted(items, key=_sort_key)

    if top_n is not None and top_n > 0:
        sorted_items = sorted_items[:top_n]

    text = inbox_path.read_text(encoding="utf-8")
    preamble, _body = _split_preamble(text)

    # Update last_updated in the frontmatter
    ts_iso = datetime.now().isoformat(timespec="seconds")
    preamble = re.sub(
        r'^last_updated:.*$',
        f'last_updated: {ts_iso}',
        preamble,
        flags=re.MULTILINE,
    )

    new_section = f"\n## Candidates (sorted by score — {len(sorted_items)} items, re-sorted {ts_iso})\n\n"

    body_blocks = []
    for it in sorted_items:
        block = it["block"]
        if not block.endswith("\n"):
            block = block + "\n"
        body_blocks.append(block)

    new_inbox = preamble.rstrip() + "\n" + new_section + "\n".join(body_blocks)

    print(f"Sorted {len(items)} items → top score is {_score_of(sorted_items[0])}/10 — '{sorted_items[0]['title'][:80]}'")
    print(f"Score distribution: ", end="")
    score_counts: dict[int, int] = {}
    for it in sorted_items:
        s = _score_of(it)
        score_counts[s] = score_counts.get(s, 0) + 1
    for s in sorted(score_counts.keys(), reverse=True):
        print(f"{s}/10:{score_counts[s]} ", end="")
    print()

    if dry_run:
        print("(dry-run — not writing)")
        return

    backup = inbox_path.with_suffix(".md.bak")
    shutil.copy2(inbox_path, backup)
    inbox_path.write_text(new_inbox, encoding="utf-8")
    print(f"✓ Re-sorted {inbox_path.relative_to(VAULT_ROOT)}")
    print(f"  Backup: {backup.relative_to(VAULT_ROOT)}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Re-sort _inbox.md so the highest-scored items appear first."
    )
    parser.add_argument("--opportunity", required=True, metavar="ID")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print the sort summary but do not modify the inbox.")
    parser.add_argument("--top", type=int, default=None, metavar="N",
                        help="Show only the top N items (drops the rest from the inbox; "
                             "back up the original before doing this).")
    args = parser.parse_args()

    opp_dir = VAULT_ROOT / "opportunities" / args.opportunity
    if not opp_dir.exists():
        print(f"ERROR: Opportunity folder not found: {opp_dir}")
        sys.exit(1)

    _rewrite_inbox(opp_dir, args.dry_run, args.top)


if __name__ == "__main__":
    main()

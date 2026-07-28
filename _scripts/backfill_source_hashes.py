#!/usr/bin/env python3
"""
backfill_source_hashes.py — add content_sha256 to source files captured before
hashing existed.

New captures get content_sha256 from lib/frontmatter.py. This walks every
existing `*/01_sources/*.md` and adds the field where it is missing, so pages
compiled from older sources have a baseline to detect drift against.

Idempotent: a file that already has content_sha256 is left alone.

Usage:
    python backfill_source_hashes.py --dry-run
    python backfill_source_hashes.py
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lib.frontmatter import content_sha256  # noqa: E402

VAULT_ROOT = Path(__file__).parent.parent


def split_frontmatter(text: str):
    """Return (frontmatter_lines, body) or (None, text) if no frontmatter."""
    if not text.startswith("---"):
        return None, text
    parts = text.split("\n")
    if parts[0].strip() != "---":
        return None, text
    for i in range(1, len(parts)):
        if parts[i].strip() == "---":
            return parts[1:i], "\n".join(parts[i + 1:])
    return None, text


def hashable_body(body: str) -> str:
    """Hash the captured content, not the analyst's notes.

    Source files follow `## Summary` / `## Extracted content` / `## Notes`.
    Only the extracted content is the source; Summary and Notes are ours and
    change without the source changing.
    """
    if "## Extracted content" in body:
        after = body.split("## Extracted content", 1)[1]
        return after.split("\n## Notes", 1)[0]
    return body


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    files = sorted(VAULT_ROOT.glob("*/*/01_sources/**/*.md")) + \
        sorted(VAULT_ROOT.glob("*/*/*/01_sources/**/*.md"))
    files = sorted(set(f for f in files if f.is_file()))

    added = skipped = malformed = 0
    for f in files:
        text = f.read_text(encoding="utf-8", errors="replace")
        fm, body = split_frontmatter(text)
        if fm is None:
            malformed += 1
            print(f"  ! no frontmatter: {f.relative_to(VAULT_ROOT)}")
            continue
        if any(l.startswith("content_sha256:") for l in fm):
            skipped += 1
            continue
        h = content_sha256(hashable_body(body))
        fm = fm + [f"content_sha256: {h}", "backfilled_hash: true"]
        new = "---\n" + "\n".join(fm) + "\n---\n" + body
        if not args.dry_run:
            f.write_text(new, encoding="utf-8")
        added += 1

    print(f"\n{'(dry-run) would add' if args.dry_run else 'added'}: {added}"
          f"   already had: {skipped}   malformed: {malformed}"
          f"   scanned: {len(files)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

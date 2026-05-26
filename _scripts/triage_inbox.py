#!/usr/bin/env python3
"""
triage_inbox.py — Bulk-decline inbox items and optionally re-rank USAspending.

Two operations:
  --decline-below-ai N   Decline any item with an AI score `M/10` where M < N.
  --rank-usaspending     Run OpenAI ranker against USAspending items (which
                         currently carry no AI score) and add scores. Combined
                         with --decline-below-usa N, declines USA items below N.

Both operations write declined items to _rejected.md (the table at the top of
that file) and remove the corresponding blocks from _inbox.md. A backup of the
inbox is written to _inbox.md.bak before any changes.

Usage:
  python triage_inbox.py --opportunity BDR-FLEET-READINESS \
      --decline-below-ai 6 \
      --rank-usaspending --decline-below-usa 6

The --opp-context flag is optional and overrides the default scoping context
that the USAspending ranker uses. Default is the BDR-FLEET-READINESS 2026-05-26
corrected scope.
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import sys
from datetime import date
from pathlib import Path

from dotenv import load_dotenv

SCRIPT_DIR = Path(__file__).parent
VAULT_ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))

from lib import inbox as inbox_lib  # noqa: E402
from lib import ranker  # noqa: E402

load_dotenv(SCRIPT_DIR / ".env")


_DEFAULT_BDR_CONTEXT = (
    "BDR-FLEET-READINESS — CACI business-development research scoping gamified "
    "operational-decision scenarios for Navy repair-activity teams: the four "
    "public naval shipyards (Norfolk, Puget Sound, Pearl Harbor, Portsmouth), "
    "the Regional Maintenance Centers including forward-deployed (SRF-JRMC), "
    "the Naval Warfare Development Center (NWDC) as doctrinal authority, and "
    "the fleet-command training authorities (COMNAVSURFOR, FLTFORCOM, "
    "COMPACFLT, INDOPACOM J7). Product is scenario design / exercise injection / "
    "playbook content for the professional BDAR/BDAT team's operational "
    "decisions: port-selection for damaged ships, foreign-port emergency "
    "contracting, forward team mobilization, BDAR triage under combat tempo, "
    "BDAT-to-BDAR handoff, degraded-comms information access. The CACI lineage "
    "is INDOPACOM PMTEC exercise design translated down-vertical to naval-repair. "
    "Out of scope: schoolhouse / NETC pipeline / NAWCTSD training-systems / "
    "individual-Sailor curriculum. Evaluating each candidate (a USAspending "
    "contract award) for relevance to this scope: highest relevance = scenario/"
    "exercise design or training-systems work for the named repair activities; "
    "lower relevance = adjacent technical services at NSWC Carderock or related "
    "facilities; lowest = IT support / wireless / facilities / unrelated services."
)


def _read_score(block: str) -> int | None:
    m = re.search(r"`(\d+)/10`", block)
    return int(m.group(1)) if m else None


def _read_usa_snippet(block: str) -> str:
    """Pull recipient/amount/period/funder into a single ranker-friendly string."""
    parts: list[str] = []
    title_m = re.match(r"^- \[ \] \*\*\[(.+?)\]\(", block)
    if title_m:
        parts.append(title_m.group(1))
    for key in ("Recipient", "Amount obligated", "Period", "Place", "Awarder", "Funder"):
        m = re.search(rf"^\s*-\s*{re.escape(key)}:\s*(.+)$", block, re.MULTILINE)
        if m:
            parts.append(f"{key}: {m.group(1).strip()}")
    return " | ".join(parts)


def _format_rejected_row(item: dict, tag: str, reason: str) -> str:
    url = (item.get("url") or "").replace("|", "%7C")
    title = (item.get("title") or "").replace("|", "\\|").replace("\n", " ").strip()
    date_str = date.today().isoformat()
    return f"| {url} | {title} | {tag} | {date_str} | {reason} |"


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--opportunity", required=True)
    p.add_argument("--decline-below-ai", type=int, default=None)
    p.add_argument("--rank-usaspending", action="store_true")
    p.add_argument("--decline-below-usa", type=int, default=None)
    p.add_argument("--opp-context", default=None)
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()

    opp_dir = VAULT_ROOT / "opportunities" / args.opportunity
    if not opp_dir.is_dir():
        print(f"ERROR: opportunity not found: {opp_dir}")
        sys.exit(1)

    inbox_path = opp_dir / "_inbox.md"
    rejected_path = opp_dir / "_rejected.md"

    items = inbox_lib.parse_items(opp_dir)
    print(f"Inbox: {len(items)} items")

    declined_blocks: list[str] = []
    declined_rows: list[str] = []

    # ── Cut: decline AI items below threshold ──
    if args.decline_below_ai is not None:
        thresh = args.decline_below_ai
        cut = []
        for it in items:
            s = _read_score(it["block"])
            if s is not None and s < thresh:
                cut.append((it, s))
        print(f"  AI cut: {len(cut)} items with score < {thresh}")
        date_str = date.today().isoformat()
        for it, s in cut:
            tag = f"bulk-decline-ai-below-{thresh}-{date_str}"
            reason = (
                f"AI score {s}/10 from ranker, below operator threshold {thresh}/10 "
                f"(bulk-decline {date_str} inbox triage)."
            )
            declined_blocks.append(it["block"])
            declined_rows.append(_format_rejected_row(it, tag, reason))

    # ── Cut: rank USAspending and optionally decline below threshold ──
    if args.rank_usaspending:
        already_declined_urls = {it["url"] for it in items if it["block"] in declined_blocks}
        usa_items = [
            it for it in items
            if it.get("source_type") == "usa_spending"
            and it["url"] not in already_declined_urls
        ]
        if usa_items:
            api_key = os.environ.get("OPENAI_API_KEY", "")
            if not api_key:
                print("  WARN: OPENAI_API_KEY not set — skipping USA ranking.")
            else:
                ctx = args.opp_context or _DEFAULT_BDR_CONTEXT
                candidates = [
                    {
                        "title": it["title"],
                        "url": it["url"],
                        "query": it.get("found_by", ""),
                        "reason": it.get("reason", ""),
                        "_snippet": _read_usa_snippet(it["block"]),
                        "_inbox_item": it,
                    }
                    for it in usa_items
                ]
                print(f"  USA rank: ranking {len(candidates)} USAspending items with OpenAI...")
                ranked = ranker.rank_candidates(candidates, ctx, api_key)
                dist: dict[int, int] = {}
                for r in ranked:
                    s = r.get("_score", 0)
                    dist[s] = dist.get(s, 0) + 1
                print(f"  USA scores: {dict(sorted(dist.items(), reverse=True))}")
                if args.decline_below_usa is not None:
                    thresh = args.decline_below_usa
                    date_str = date.today().isoformat()
                    cnt = 0
                    for r in ranked:
                        s = r.get("_score", 5)
                        if s < thresh:
                            it = r["_inbox_item"]
                            tag = f"bulk-decline-usa-below-{thresh}-{date_str}"
                            note = r.get("_rank_note", "")
                            reason = (
                                f"USAspending re-rank score {s}/10 (gpt-4o-mini, "
                                f"corrected-scope context), below threshold {thresh}/10 "
                                f"(bulk-decline {date_str} inbox triage). Ranker note: {note}"
                            )
                            declined_blocks.append(it["block"])
                            declined_rows.append(_format_rejected_row(it, tag, reason))
                            cnt += 1
                    print(f"  USA cut: {cnt} items with score < {thresh}")

    print(f"\nTotal items to decline: {len(declined_blocks)}")
    if not declined_blocks:
        return

    if args.dry_run:
        print("(dry-run — no changes written)")
        return

    # Backup + rewrite inbox
    backup = inbox_path.with_suffix(".md.bak")
    shutil.copy2(inbox_path, backup)
    print(f"Backup: {backup.relative_to(VAULT_ROOT)}")

    inbox_text = inbox_path.read_text(encoding="utf-8")
    for block in declined_blocks:
        inbox_text = inbox_text.replace(block, "")
    inbox_text = re.sub(r"\n{3,}", "\n\n", inbox_text)
    inbox_path.write_text(inbox_text, encoding="utf-8")
    print(f"✓ Updated {inbox_path.relative_to(VAULT_ROOT)}")

    # Append to _rejected.md
    rejected_text = rejected_path.read_text(encoding="utf-8")
    rejected_text = rejected_text.rstrip() + "\n" + "\n".join(declined_rows) + "\n"
    rejected_path.write_text(rejected_text, encoding="utf-8")
    print(f"✓ Appended {len(declined_rows)} rows to {rejected_path.relative_to(VAULT_ROOT)}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Operator-driven inbox approval.

Workflow:
  1. In Obsidian: tap/click the checkbox on any item you want to approve.
     That is the ONLY action needed in Obsidian.
  2. Run this script: python approve_inbox.py <OPPORTUNITY_ID>
     - All checked [x] items are ingested automatically.
     - Then each remaining [unchecked] item is shown one at a time so you
       can approve, reject, or keep it — no Obsidian editing needed.
"""

import os
import subprocess
import sys
import textwrap
from pathlib import Path

from dotenv import load_dotenv

SCRIPT_DIR = Path(__file__).parent
VAULT_ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))

load_dotenv(SCRIPT_DIR / ".env")

from lib import inbox, sam_gov, usaspending

OPP_ROOT = VAULT_ROOT / "opportunities"
INGEST = SCRIPT_DIR / "ingest.py"
PYTHON = SCRIPT_DIR / ".venv" / "bin" / "python"

_W = 72  # display width


def _python() -> str:
    return str(PYTHON) if PYTHON.exists() else sys.executable


def _ingest(opp_id: str, item: dict) -> bool:
    # SAM.gov items: re-fetch via API and write source file directly
    if item.get("source_type") == "sam_gov":
        return _ingest_sam(opp_id, item)
    if item.get("source_type") == "usa_spending":
        return _ingest_usa(opp_id, item)

    url = item["url"]
    if not url:
        print(f"    SKIP — no URL in item")
        return False
    result = subprocess.run(
        [_python(), str(INGEST), url, "--opportunity", opp_id],
        capture_output=True,
        text=True,
        input="s\n",  # answer "skip" to any duplicate-file prompt from ingest.py
    )
    if result.returncode == 0:
        return True
    # Find the most useful error line (prefer "ERROR:" lines)
    all_out = (result.stderr.strip() + "\n" + result.stdout.strip()).splitlines()
    error_line = next((l for l in all_out if "ERROR:" in l), None)
    if not error_line:
        error_line = next((l.strip() for l in reversed(all_out) if l.strip()), "unknown error")
    print(f"    {error_line.strip()}")
    return False


def _ingest_sam(opp_id: str, item: dict) -> bool:
    api_key = os.environ.get("SAM_GOV_API_KEY", "")
    if not api_key:
        print("    ERROR: SAM_GOV_API_KEY not set — cannot ingest SAM.gov notice.")
        return False
    notice_id = item.get("notice_id", "")
    if not notice_id:
        print("    ERROR: inbox entry missing Notice ID.")
        return False
    opp_dir = OPP_ROOT / opp_id
    try:
        ok, msg = sam_gov.ingest_notice(opp_dir, item, api_key)
    except sam_gov.SamGovKeyError as e:
        print(f"    ERROR: {e}")
        return False
    except Exception as e:
        print(f"    ERROR: SAM.gov ingest failed — {e}")
        return False
    if ok:
        print(f"    → {msg}")
        return True
    print(f"    ERROR: {msg}")
    return False


def _ingest_usa(opp_id: str, item: dict) -> bool:
    generated_id = item.get("generated_id", "")
    if not generated_id:
        print("    ERROR: inbox entry missing Generated ID.")
        return False
    opp_dir = OPP_ROOT / opp_id
    try:
        ok, msg = usaspending.ingest_award(opp_dir, item)
    except Exception as e:
        print(f"    ERROR: USAspending ingest failed — {e}")
        return False
    if ok:
        print(f"    → {msg}")
        return True
    print(f"    ERROR: {msg}")
    return False


def _hr() -> None:
    print("─" * _W)


def _show_item(n: int, total: int, item: dict) -> None:
    _hr()
    import re
    score_m = re.search(r'`(\d+/10)`', item["block"])
    score = f"  [{score_m.group(1)}]" if score_m else ""

    is_sam = item.get("source_type") == "sam_gov"
    is_usa = item.get("source_type") == "usa_spending"
    tag = "  [SAM.gov]" if is_sam else "  [USAspending]" if is_usa else ""
    title = item["title"][:60] + ("…" if len(item["title"]) > 60 else "")
    print(f"  [{n}/{total}]{score}{tag}  {title}")
    print(f"  {item['url']}")
    if is_sam:
        block = item["block"]
        for label in ("Notice ID", "Notice type", "Posted", "Response deadline",
                      "Set-aside", "NAICS", "Department"):
            m = re.search(rf'^\s+- {re.escape(label)}:\s*(.+)$', block, re.MULTILINE)
            if m:
                print(f"  {label}: {m.group(1).strip()}")
        att_m = re.search(r'^\s+- Attachments:\s*(\d+)', block, re.MULTILINE)
        if att_m and att_m.group(1) != "0":
            print(f"  Attachments: {att_m.group(1)} (review after approval)")
    elif is_usa:
        block = item["block"]
        for label in ("Award ID", "Recipient", "Amount obligated", "Period",
                      "Awarder", "Funder", "Place"):
            m = re.search(rf'^\s+- {re.escape(label)}:\s*(.+)$', block, re.MULTILINE)
            if m:
                print(f"  {label}: {m.group(1).strip()}")
    if item.get("found_by"):
        print(f"  {item['found_by']}")
    if item.get("reason"):
        wrapped = textwrap.fill(item["reason"], width=_W - 4, initial_indent="  ", subsequent_indent="  ")
        print(wrapped)


def _prompt_pending(n: int, total: int, item: dict) -> str:
    _show_item(n, total, item)
    print()
    while sys.stdin.isatty():
        raw = input("  [a]pprove  [r]eject  [k]eep  [q]uit > ").strip().lower()
        if raw in ("a", "r", "k", "q"):
            return raw
        print("  Enter a, r, k, or q.")
    return "k"


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python approve_inbox.py <OPPORTUNITY_ID>")
        sys.exit(1)

    opp_id = sys.argv[1]
    opp_dir = OPP_ROOT / opp_id
    if not opp_dir.is_dir():
        print(f"ERROR: Opportunity folder not found: {opp_dir}")
        sys.exit(1)

    items = inbox.parse_items(opp_dir)
    if not items:
        print(f"Inbox is empty for {opp_id}.")
        return

    pre_approved = [i for i in items if i["state"] == "x"]
    pre_rejected = [i for i in items if i["state"] == "-"]  # manual [-] still works
    pending = [i for i in items if i["state"] == " "]

    print(f"\n{opp_id} inbox: {len(pre_approved)} pre-approved, "
          f"{len(pending)} pending, {len(pre_rejected)} pre-rejected\n")

    ingested = 0
    failed_items = []

    # ── 1. Process pre-approved (checkbox ticked in Obsidian) ──────────────
    if pre_approved:
        print("Ingesting pre-approved items…")
    for item in pre_approved:
        print(f"  → {item['title'][:60]}")
        if _ingest(opp_id, item):
            ingested += 1
            inbox.remove_block(opp_dir, item["block"])
            print(f"    ✓ ingested")
        else:
            failed_items.append(item)
            print(f"    ✗ failed — left in inbox for retry")

    # ── 2. Process pre-rejected (manually typed [-] in Obsidian) ───────────
    for item in pre_rejected:
        inbox.write_rejected(opp_dir, item["url"], item["title"],
                             "operator", "operator-rejected")
        inbox.remove_block(opp_dir, item["block"])

    # ── 3. Interactive review of pending items ──────────────────────────────
    if pending:
        _hr()
        if not sys.stdin.isatty():
            print(f"\n{len(pending)} item(s) still pending — run interactively to review.")
        elif input(f"\n{len(pending)} items still pending. Review them now? [y/N] ").strip().lower() != "y":
            print("Skipped. Run again to review later.")
        elif sys.stdin.isatty():
            print()
            for n, item in enumerate(pending, 1):
                choice = _prompt_pending(n, len(pending), item)
                if choice == "a":
                    print(f"  → Ingesting…")
                    if _ingest(opp_id, item):
                        ingested += 1
                        inbox.remove_block(opp_dir, item["block"])
                        print(f"    ✓ ingested")
                    else:
                        failed_items.append(item)
                        print(f"    ✗ failed — left in inbox")
                elif choice == "r":
                    inbox.write_rejected(opp_dir, item["url"], item["title"],
                                         "operator", "operator-rejected")
                    inbox.remove_block(opp_dir, item["block"])
                    print(f"    → Rejected")
                elif choice == "k":
                    print(f"    → Kept for later")
                elif choice == "q":
                    print(f"\n  Stopped. Remaining items left in inbox.")
                    break

    # ── 4. Expire stale items ───────────────────────────────────────────────
    expired = inbox.expire_old_items(opp_dir)

    # ── 5. Summary ──────────────────────────────────────────────────────────
    _hr()
    remaining = len(inbox.parse_items(opp_dir))
    print(f"\nDone.  ingested={ingested}  failed={len(failed_items)}  "
          f"expired={expired}  remaining={remaining}")
    if failed_items:
        print("\nFailed items (403 = download manually and re-ingest):")
        for item in failed_items:
            print(f"  {item['url']}")


if __name__ == "__main__":
    main()

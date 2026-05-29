#!/usr/bin/env python3
"""
approve_seeds.py — Operator-driven triage of `_meta/seeds-inbox.md`.

Walks each seed in the inbox, surfaces the triage row's marked status
(`[x] promote`, `[x] drop`, `[x] monitor`), and processes:

  - PROMOTE → scaffold a new opportunity folder under `opportunities/<OPP_ID>/`
    populated from `_templates/`, with the seed source URL ingested into
    `01_sources/` and the BLUF / source citation pre-populated into the
    new `00_research-file.md`. The promoted seed moves from the inbox to
    `_meta/seeds-promoted.md` with a link to the new opportunity folder.
  - DROP → move the seed block from the inbox to `_meta/seeds-rejected.md`
    with a timestamped reason row.
  - MONITOR → leave the seed in the inbox with a `monitoring since YYYY-MM-DD`
    annotation; future `find_seeds.py` runs will re-rank and surface deltas.
  - (unmarked) → leave in inbox unchanged.

Hard precondition baked into the PROMOTE path: if the seed's customer is
SRF-JRMC or a team_extendable_customer, the script flags the FAR Subpart 9.5
OCI review requirement at the operator prompt — mirroring the BDR §7.1
pattern that OCI is a hard gate, not a parallel workstream.

Usage:
    python approve_seeds.py
    python approve_seeds.py --non-interactive       # parse marks, apply, no prompts
"""

import argparse
import json
import re
import shutil
import sys
import textwrap
from datetime import date, datetime, timezone
from pathlib import Path

import yaml
from dotenv import load_dotenv

SCRIPT_DIR = Path(__file__).parent
VAULT_ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))
load_dotenv(SCRIPT_DIR / ".env")

CONFIG_PATH = VAULT_ROOT / "_meta" / "caci-discovery-config.yaml"
SEEDS_INBOX = VAULT_ROOT / "_meta" / "seeds-inbox.md"
SEEDS_LEDGER = VAULT_ROOT / "_meta" / "seeds-ledger.json"
SEEDS_REJECTED = VAULT_ROOT / "_meta" / "seeds-rejected.md"
SEEDS_PROMOTED = VAULT_ROOT / "_meta" / "seeds-promoted.md"
TEMPLATES_DIR = VAULT_ROOT / "_templates"
OPP_ROOT = VAULT_ROOT / "opportunities"


def _utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _today_iso() -> str:
    return date.today().isoformat()


# ── Parse the inbox into seed blocks ─────────────────────────────────────


SEED_HEADER_RE = re.compile(r"^- \[ ?\] \*\*\[([^\]]+)\]\(([^)]+)\)\*\*\s*`(\d+/10)`")


def _parse_inbox(text: str) -> list[dict]:
    """Split the inbox into per-seed blocks. Each block starts at a
    `- [ ] **[title](url)** \`N/10\`` line and ends before the next such
    line (or end of file)."""
    lines = text.split("\n")
    seeds = []
    current_start = None
    for i, line in enumerate(lines):
        if SEED_HEADER_RE.match(line):
            if current_start is not None:
                block = "\n".join(lines[current_start:i]).rstrip() + "\n"
                seeds.append({"block": block, "start": current_start, "end": i})
            current_start = i
    if current_start is not None:
        block = "\n".join(lines[current_start:]).rstrip() + "\n"
        seeds.append({"block": block, "start": current_start, "end": len(lines)})
    # Parse meta from each block
    for s in seeds:
        s.update(_parse_seed_meta(s["block"]))
    return seeds


def _parse_seed_meta(block: str) -> dict:
    """Extract title, URL, score, triage decision, customer from a block."""
    meta = {"title": "", "url": "", "score": "", "triage": None, "customer": "",
            "source_label": "", "notice_type": "", "snippet": ""}
    m = SEED_HEADER_RE.match(block.split("\n", 1)[0])
    if m:
        meta["title"] = m.group(1).strip()
        meta["url"] = m.group(2).strip()
        meta["score"] = m.group(3).strip()
    # Triage decision: look for the triage line and check which is `[x]`
    for line in block.split("\n"):
        if "Triage:" in line:
            if re.search(r"\[\s*[xX]\s*\]\s*promote", line):
                meta["triage"] = "promote"
            elif re.search(r"\[\s*[xX]\s*\]\s*drop", line):
                meta["triage"] = "drop"
            elif re.search(r"\[\s*[xX]\s*\]\s*monitor", line):
                meta["triage"] = "monitor"
            break
    # Customer line
    cm = re.search(r"^\s*- Customer:\s*(.+)$", block, re.MULTILINE)
    if cm:
        meta["customer"] = cm.group(1).strip()
    # Source label
    sm = re.search(r"^\s*- Source:\s*(.+)$", block, re.MULTILINE)
    if sm:
        meta["source_label"] = sm.group(1).strip()
    # Snippet
    pm = re.search(r"^\s*- Snippet:\s*(.+)$", block, re.MULTILINE)
    if pm:
        meta["snippet"] = pm.group(1).strip()
    return meta


# ── Promotion path: scaffold new opportunity folder ─────────────────────


def _slugify(s: str, max_len: int = 40) -> str:
    s = re.sub(r"[^A-Za-z0-9-]+", "-", s.upper()).strip("-")
    return s[:max_len].rstrip("-")


def _oci_flag_required(seed_meta: dict, cfg: dict) -> bool:
    """Return True if the seed touches SRF-JRMC or any team_extendable customer."""
    team = cfg.get("operator_team_layer", {})
    customer = (seed_meta.get("customer") or "").lower()
    primary = team.get("team_primary_customer", "").lower()
    if primary and primary in customer:
        return True
    for ext in team.get("team_extendable_customers", []) or []:
        if ext.lower() in customer:
            return True
        # parenthetical acronym
        m = re.search(r"\(([^)]+)\)", ext.lower())
        if m and m.group(1).strip() in customer:
            return True
    return False


def _prompt_for_promotion_meta(seed: dict, cfg: dict) -> dict | None:
    """Prompt the operator for opportunity ID and short hypothesis BLUF.
    Returns None if operator cancels."""
    if not sys.stdin.isatty():
        return None  # can't prompt in non-interactive mode

    print()
    print("=" * 70)
    print(f"PROMOTING: {seed['title'][:60]}")
    print(f"  Score: {seed['score']}")
    print(f"  Customer: {seed['customer']}")
    print(f"  URL: {seed['url']}")
    if _oci_flag_required(seed, cfg):
        print()
        print("  ⚑ OCI PRECONDITION FLAGGED")
        print("    This seed touches SRF-JRMC or a team-extendable customer.")
        print("    FAR Subpart 9.5 OCI review is a hard precondition on any")
        print("    further engagement step. CACI legal and contracts must")
        print("    complete the OCI review before pursuit actions begin.")
    print()
    suggested = _slugify(seed["title"][:40])
    raw = input(f"  Opportunity ID [default {suggested}]: ").strip()
    opp_id = raw or suggested
    if not opp_id:
        print("  cancelled.")
        return None
    print()
    print("  Short hypothesis (one sentence BLUF the eventual capture will test):")
    hypothesis = input("  > ").strip()
    if not hypothesis:
        print("  cancelled.")
        return None
    return {"opp_id": opp_id, "hypothesis": hypothesis}


def _scaffold_opportunity_folder(opp_id: str, seed: dict, hypothesis: str, cfg: dict) -> Path:
    """Create opportunities/<opp_id>/ from _templates/ and pre-populate."""
    target = OPP_ROOT / opp_id
    if target.exists():
        raise FileExistsError(f"Opportunity folder already exists: {target}")
    target.mkdir(parents=True)
    # Copy templates (best-effort; templates dir may not exist or may be sparse)
    if TEMPLATES_DIR.exists():
        for src in TEMPLATES_DIR.glob("*"):
            if src.is_file():
                shutil.copy2(src, target / src.name)
    # Always create the four canonical sub-dirs
    for sub in ["00_planning", "01_sources", "04_artifacts", "_red-teams"]:
        (target / sub).mkdir(exist_ok=True)
    # Pre-populate 00_research-file.md if not template-provided
    rf = target / "00_research-file.md"
    if not rf.exists():
        rf.write_text(_initial_research_file(opp_id, seed, hypothesis, cfg), encoding="utf-8")
    # Pre-populate 05_decision-log.md
    dl = target / "05_decision-log.md"
    if not dl.exists():
        dl.write_text(_initial_decision_log(opp_id, seed, hypothesis), encoding="utf-8")
    return target


def _initial_research_file(opp_id: str, seed: dict, hypothesis: str, cfg: dict) -> str:
    """Render the initial 00_research-file.md for a promoted seed."""
    oci_block = ""
    if _oci_flag_required(seed, cfg):
        oci_block = (
            "\n**Flag:** FAR Subpart 9.5 Organizational Conflict of Interest (OCI) review is a hard "
            "precondition on any engagement step. The operator team is colocated with SRF-JRMC and "
            "operates customer systems; OCI exposure is structural, not incidental. CACI legal and "
            "contracts must complete the OCI review before pursuit actions begin. See "
            "`_meta/oci-primer.md` for procedure.\n"
        )
    return textwrap.dedent(f"""\
        ---
        opportunity: {opp_id}
        scaffolded_from_seed: true
        seed_source: {seed.get('source_label', '')}
        seed_url: {seed.get('url', '')}
        seed_score_at_promotion: {seed.get('score', '')}
        scaffolded_utc: {_utc_now()}
        ---

        # {opp_id} — Research File

        ## 1. Working summary (analyst view)

        **Hypothesis:** {hypothesis}

        This opportunity was promoted from the seeds inbox on {_today_iso()}. The
        seed was scored {seed.get('score', '')} against the layered CACI capability
        footprint defined in `_meta/caci-discovery-config.yaml`. Source URL:
        {seed.get('url', '')}.

        Initial source snippet: {seed.get('snippet', '')}
        {oci_block}
        ## 2. Open questions

        (To be populated as the small-ships workflow opens specific FACT-claim
        questions. See `_meta/small-ships-workflow.md`.)

        ## 3. Demand signal

        (Populated by the standard `find_sources.py` pass scoped to this
        opportunity once a per-opportunity `_capture-pillars.md` is written.)

        ## 4. Customer landscape

        (TBD.)

        ## 5. Competitive landscape

        (TBD.)

        ## 6. Our fit

        (TBD.)

        ## 7. Working hypothesis and falsifying legs

        (TBD.)

        ## 8. Source ledger

        ### 8.1 Ingested primary sources (in `01_sources/`)

        (Populated as sources are ingested. The seed URL above should be the
        first ingested source.)

        ### 8.2 Cited but not yet ingested, or ingested empty — needs retry

        ## 9. Verification flags

        ## 10. Research plan (OSI-only)

        ## 11. Engagement & relationship strategy
        """)


def _initial_decision_log(opp_id: str, seed: dict, hypothesis: str) -> str:
    return textwrap.dedent(f"""\
        # {opp_id} — Decision Log

        Every decision: date, decision, by whom, rationale, what changed.

        ---

        ### {_today_iso()} — Opportunity scaffolded from seeds inbox

        **By:** Operator promoted the seed via `_scripts/approve_seeds.py`.

        **Source seed:** {seed.get('title', '')[:120]}
        URL: {seed.get('url', '')}
        Score at promotion: {seed.get('score', '')}

        **Hypothesis stated at promotion:**

        > {hypothesis}

        **What changed:** new opportunity folder created at `opportunities/{opp_id}/`
        scaffolded from `_templates/`. `00_research-file.md` pre-populated with
        the seed metadata. The standard small-ships workflow now applies.

        ---
        """)


# ── Drop / monitor / promote handling ───────────────────────────────────


def _move_to_rejected(seeds_dropped: list[dict]) -> None:
    """Append dropped-seed rows to seeds-rejected.md."""
    SEEDS_REJECTED.parent.mkdir(parents=True, exist_ok=True)
    existing = SEEDS_REJECTED.read_text(encoding="utf-8") if SEEDS_REJECTED.exists() else (
        "# Seeds Rejected — dropped during operator triage\n\n"
        "Each row: URL, title, drop-date, drop-reason.\n\n"
        "| URL | Title | Drop date | Drop reason |\n"
        "|---|---|---|---|\n"
    )
    rows = []
    for s in seeds_dropped:
        url = s["url"].replace("|", "%7C")
        title = s["title"].replace("|", "\\|")
        rows.append(f"| {url} | {title} | {_today_iso()} | operator-dropped via approve_seeds |")
    SEEDS_REJECTED.write_text(existing.rstrip() + "\n" + "\n".join(rows) + "\n", encoding="utf-8")


def _move_to_promoted(seed: dict, opp_id: str, opp_path: Path) -> None:
    """Append a promoted-seed row to seeds-promoted.md."""
    SEEDS_PROMOTED.parent.mkdir(parents=True, exist_ok=True)
    existing = SEEDS_PROMOTED.read_text(encoding="utf-8") if SEEDS_PROMOTED.exists() else (
        "# Seeds Promoted — scaffolded into opportunity folders\n\n"
        "Each row: opportunity ID, seed URL, original seed title, promote date.\n\n"
        "| Opp ID | Seed URL | Title | Promote date |\n"
        "|---|---|---|---|\n"
    )
    url = seed["url"].replace("|", "%7C")
    title = seed["title"].replace("|", "\\|")
    row = f"| [{opp_id}](../opportunities/{opp_id}/) | {url} | {title} | {_today_iso()} |"
    SEEDS_PROMOTED.write_text(existing.rstrip() + "\n" + row + "\n", encoding="utf-8")


def _update_ledger_status(fingerprint_hint: str, new_status: str) -> None:
    """Best-effort ledger update by fingerprint hint (URL match)."""
    if not SEEDS_LEDGER.exists():
        return
    ledger = json.loads(SEEDS_LEDGER.read_text(encoding="utf-8"))
    for fp, entry in ledger.get("seeds", {}).items():
        if entry.get("url", "") == fingerprint_hint:
            entry["status"] = new_status
            entry["status_updated_utc"] = _utc_now()
            break
    SEEDS_LEDGER.write_text(json.dumps(ledger, indent=2), encoding="utf-8")


def _rewrite_inbox_without(removed_blocks: list[str], monitor_seeds: list[dict]) -> None:
    """Rewrite seeds-inbox.md removing promoted/dropped blocks and annotating
    monitored seeds with a 'monitoring since' marker."""
    if not SEEDS_INBOX.exists():
        return
    text = SEEDS_INBOX.read_text(encoding="utf-8")
    for block in removed_blocks:
        text = text.replace(block, "")
    # For each monitor seed, ensure a `monitoring since YYYY-MM-DD` line is present
    today = _today_iso()
    for s in monitor_seeds:
        block = s["block"]
        if "Monitoring since:" in block:
            continue
        new_block = block.rstrip() + f"\n  - Monitoring since: {today}\n\n"
        text = text.replace(block, new_block)
    # Collapse excess blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)
    SEEDS_INBOX.write_text(text, encoding="utf-8")


# ── Main ───────────────────────────────────────────────────────────────


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--non-interactive", action="store_true",
                    help="Process marked rows without prompts. Promotions still need an opp ID; "
                         "in non-interactive mode, the opportunity ID is auto-slugged from the seed title "
                         "and the hypothesis is left blank for later editing.")
    args = ap.parse_args()

    if not SEEDS_INBOX.exists():
        print(f"No seeds inbox at {SEEDS_INBOX}. Nothing to do.")
        return

    cfg = yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8"))
    text = SEEDS_INBOX.read_text(encoding="utf-8")
    seeds = _parse_inbox(text)
    if not seeds:
        print("Seeds inbox is empty (no parseable seed blocks).")
        return

    print(f"Seeds inbox: {len(seeds)} seeds parsed.")
    marked_promote = [s for s in seeds if s["triage"] == "promote"]
    marked_drop = [s for s in seeds if s["triage"] == "drop"]
    marked_monitor = [s for s in seeds if s["triage"] == "monitor"]
    unmarked = [s for s in seeds if s["triage"] is None]

    print(f"  promote: {len(marked_promote)}")
    print(f"  drop:    {len(marked_drop)}")
    print(f"  monitor: {len(marked_monitor)}")
    print(f"  unmarked (left in inbox): {len(unmarked)}")

    promoted_blocks = []
    dropped_blocks = []

    for s in marked_promote:
        if args.non_interactive:
            opp_id = _slugify(s["title"][:40])
            hypothesis = "(scaffolded non-interactively; populate manually)"
        else:
            meta = _prompt_for_promotion_meta(s, cfg)
            if meta is None:
                print(f"  skipping promote on {s['title'][:60]} (cancelled)")
                continue
            opp_id = meta["opp_id"]
            hypothesis = meta["hypothesis"]

        try:
            opp_path = _scaffold_opportunity_folder(opp_id, s, hypothesis, cfg)
        except FileExistsError as e:
            print(f"  ERROR — {e}; skipping.")
            continue
        except Exception as e:
            print(f"  ERROR scaffolding {opp_id}: {e}; skipping.")
            continue

        _move_to_promoted(s, opp_id, opp_path)
        _update_ledger_status(s["url"], f"promoted:{opp_id}")
        promoted_blocks.append(s["block"])
        print(f"  ✓ promoted → {opp_path.relative_to(VAULT_ROOT)}")

    for s in marked_drop:
        dropped_blocks.append(s["block"])
        _update_ledger_status(s["url"], "rejected")
        print(f"  ✓ dropped {s['title'][:60]}")
    if marked_drop:
        _move_to_rejected(marked_drop)

    # Rewrite inbox: remove promoted + dropped, annotate monitored
    _rewrite_inbox_without(promoted_blocks + dropped_blocks, marked_monitor)
    for s in marked_monitor:
        _update_ledger_status(s["url"], "monitor")

    print(f"\nDone. promoted={len(promoted_blocks)} dropped={len(dropped_blocks)} monitored={len(marked_monitor)} left-in-inbox={len(unmarked)}")


if __name__ == "__main__":
    main()

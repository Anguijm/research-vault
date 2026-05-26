#!/usr/bin/env python3
"""Cron entrypoint: find new source candidates and queue them for operator approval."""

import argparse
import os
import re
import sys
from datetime import datetime
from pathlib import Path

import yaml
from dotenv import load_dotenv

SCRIPT_DIR = Path(__file__).parent
VAULT_ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))

from lib import cron_log, dedup, inbox, lock, ranker, sam_gov, searcher, usaspending

load_dotenv(SCRIPT_DIR / ".env")

OPP_ROOT = VAULT_ROOT / "opportunities"


def _check_api_keys() -> tuple[bool, bool, str, str]:
    has_claude = bool(os.environ.get("ANTHROPIC_API_KEY"))
    has_gemini = bool(os.environ.get("GEMINI_API_KEY"))
    openai_key = os.environ.get("OPENAI_API_KEY", "")
    sam_key = os.environ.get("SAM_GOV_API_KEY", "")
    if not has_claude:
        print("WARN: ANTHROPIC_API_KEY not set — skipping Claude calls.")
    if not has_gemini:
        print("WARN: GEMINI_API_KEY not set — skipping Gemini calls.")
    if not openai_key:
        print("WARN: OPENAI_API_KEY not set — skipping ranking, inbox order will be unranked.")
    if not sam_key:
        print("WARN: SAM_GOV_API_KEY not set — SAM.gov queries will be skipped.")
    return has_claude, has_gemini, openai_key, sam_key


def _discover_opportunities(opp_id: str | None) -> list[Path]:
    if opp_id:
        d = OPP_ROOT / opp_id
        if not d.is_dir():
            print(f"ERROR: Opportunity folder not found: {d}")
            sys.exit(1)
        return [d]
    opps = []
    for index in sorted(OPP_ROOT.glob("*/index.md")):
        text = index.read_text(encoding="utf-8")
        if re.search(r'^auto_find:\s*false', text, re.MULTILINE):
            continue
        opps.append(index.parent)
    return opps


def _load_config(opp_dir: Path) -> dict | None:
    cfg_path = opp_dir / "_search-config.yaml"
    if not cfg_path.exists():
        print(f"  No _search-config.yaml — skipping {opp_dir.name}")
        return None
    with open(cfg_path, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def _set_frontmatter_field(text: str, key: str, value: str) -> str:
    """Set or insert a YAML frontmatter field in the opening --- block."""
    if re.search(rf'^{re.escape(key)}:', text, re.MULTILINE):
        return re.sub(rf'^{re.escape(key)}:.*$', f'{key}: {value}', text, flags=re.MULTILINE)
    # Insert before the closing --- of the frontmatter block
    lines = text.split("\n")
    if lines[0].strip() != "---":
        return text
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        return text
    lines.insert(end, f"{key}: {value}")
    return "\n".join(lines)


def _update_index_frontmatter(opp_dir: Path, ts: str, ai_count: int,
                              sam_count: int, usa_count: int) -> None:
    index = opp_dir / "index.md"
    if not index.exists():
        return
    text = index.read_text(encoding="utf-8")
    text = _set_frontmatter_field(text, "last_find_run", ts)
    text = _set_frontmatter_field(text, "last_find_count_ai", str(ai_count))
    text = _set_frontmatter_field(text, "last_find_count_sam", str(sam_count))
    text = _set_frontmatter_field(text, "last_find_count_usa", str(usa_count))
    # Backfill: remove the obsolete single-counter field if present
    text = re.sub(r'^last_find_count:.*\n', '', text, flags=re.MULTILINE)
    index.write_text(text, encoding="utf-8")


def _process_opportunity(
    opp_dir: Path,
    use_claude: bool,
    use_gemini: bool,
    dry_run: bool,
    openai_key: str = "",
    sam_key: str = "",
) -> tuple[int, int, int, int, int]:
    """Returns (ai_count, sam_count, usa_count, deduped_count, error_count)."""
    opp_id = opp_dir.name
    prefix = "[DRY RUN] " if dry_run else ""
    print(f"\n{prefix}Processing {opp_id}...")

    cfg = _load_config(opp_dir)
    if not cfg:
        return 0, 0, 0, 0, 0

    queries = cfg.get("ai_searches", []) or []
    sam_searches = cfg.get("sam_searches", []) or []
    usa_searches = cfg.get("usa_spending_searches", []) or []
    if not queries and not sam_searches and not usa_searches:
        print(f"  No ai_searches, sam_searches, or usa_spending_searches configured — skipping.")
        return 0, 0, 0, 0, 0

    date_window = cfg.get("date_window_days", 7)
    max_candidates = cfg.get("max_candidates_per_run", 20)

    # ── AI search ──────────────────────────────────────────────────────
    ai_count = 0
    deduped_count = 0
    errors = 0
    if queries and (use_claude or use_gemini):
        ai_count, ai_deduped, ai_errors = _run_ai_search(
            opp_dir, opp_id, queries, date_window, max_candidates,
            use_claude, use_gemini, openai_key, dry_run,
        )
        deduped_count += ai_deduped
        errors += ai_errors
    elif queries:
        print(f"  No AI keys available — skipping AI search.")

    # ── SAM.gov search ─────────────────────────────────────────────────
    # Wrapped in try/except 2026-05-26 after the SAM description-fetch stage
    # silently killed a production pass before USAspending could run. If SAM
    # fails for any reason (429 cascade, ranker exception, hang) we print a
    # traceback and continue to USAspending rather than aborting the pass.
    sam_count = 0
    if sam_searches:
        if not sam_key:
            print(f"  SAM.gov skipped (no key).")
        else:
            sam_min_score = int(cfg.get("sam_min_score", 5))
            try:
                sam_count, sam_deduped, sam_errors = _run_sam_search(
                    opp_dir, opp_id, sam_searches, date_window, max_candidates,
                    sam_key, openai_key, sam_min_score, dry_run,
                )
                deduped_count += sam_deduped
                errors += sam_errors
            except Exception as e:
                import traceback
                print(f"  [SAM] FATAL: {type(e).__name__}: {e}")
                print(f"  [SAM] Traceback (continuing to USAspending):")
                traceback.print_exc()
                errors += 1

    # ── USAspending.gov search ─────────────────────────────────────────
    usa_count = 0
    if usa_searches:
        usa_count, usa_deduped, usa_errors = _run_usaspending_search(
            opp_dir, usa_searches, date_window, max_candidates, dry_run,
        )
        deduped_count += usa_deduped
        errors += usa_errors

    if not dry_run:
        ts = datetime.now().isoformat(timespec="seconds")
        _update_index_frontmatter(opp_dir, ts, ai_count, sam_count, usa_count)
        cron_log.append_opportunity(opp_id, ai_count + sam_count + usa_count, deduped_count, errors)

    return ai_count, sam_count, usa_count, deduped_count, errors


def _run_ai_search(
    opp_dir: Path, opp_id: str, queries: list[str],
    date_window: int, max_candidates: int,
    use_claude: bool, use_gemini: bool,
    openai_key: str, dry_run: bool,
) -> tuple[int, int, int]:
    """Run the AI search loop. Returns (new_count, deduped_count, error_count)."""
    known_urls = dedup.load_known_urls(opp_dir) | inbox.load_inbox_urls(opp_dir)
    raw_total = 0
    deduped_count = 0
    errors = 0
    seen_in_run: set[str] = set()
    new_candidates: list[dict] = []

    for query in queries:
        print(f"  [AI] Searching: {query}")
        try:
            results = searcher.search(query, date_window, max_candidates, use_claude, use_gemini)
        except Exception as e:
            print(f"  ERROR: {e}")
            errors += 1
            continue

        raw_total += len(results)
        for r in results:
            url = r["url"]
            if url in known_urls or url in seen_in_run:
                deduped_count += 1
                continue
            seen_in_run.add(url)
            new_candidates.append(r)

    print(f"  [AI] {raw_total} raw, {deduped_count} deduped, {len(new_candidates)} pre-validation")
    print(f"  [AI] Validating URLs...")
    validated = ranker.resolve_and_validate(new_candidates)
    dropped = len(new_candidates) - len(validated)
    if dropped:
        print(f"  [AI] Dropped {dropped} invalid/index URLs")

    known_urls_final = dedup.load_known_urls(opp_dir) | inbox.load_inbox_urls(opp_dir)
    validated = [c for c in validated if c["url"] not in known_urls_final]

    opp_context = f"{opp_id} — {', '.join(queries)}"
    if openai_key and validated:
        print(f"  [AI] Ranking {len(validated)} candidates with OpenAI...")
        validated = ranker.rank_candidates(validated, opp_context, openai_key)
        scores = [c.get('_score', '?') for c in validated]
        print(f"  [AI] Scores: {scores}")

    print(f"  [AI] {len(validated)} candidates queued")
    new_count = inbox.append_candidates(opp_dir, validated, dry_run=dry_run)
    return new_count, deduped_count, errors


def _run_sam_search(
    opp_dir: Path, opp_id: str, sam_searches: list,
    date_window: int, max_candidates: int,
    sam_key: str, openai_key: str, min_score: int, dry_run: bool,
) -> tuple[int, int, int]:
    """Run SAM.gov search loop with AI relevance ranking and a score threshold.

    Returns (new_count, deduped_count, error_count).
    """
    known_urls = dedup.load_known_urls(opp_dir) | inbox.load_inbox_urls(opp_dir)
    known_ids = dedup.load_known_notice_ids(opp_dir) | inbox.load_inbox_notice_ids(opp_dir)

    deduped_count = 0
    errors = 0
    seen_ids: set[str] = set()
    new_candidates: list[dict] = []
    query_labels: list[str] = []

    for entry in sam_searches:
        try:
            params = sam_gov.parse_search_entry(entry, date_window)
        except Exception as e:
            print(f"  [SAM] ERROR parsing entry {entry!r}: {e}")
            errors += 1
            continue

        label = params.get("q") or "(structured query)"
        query_labels.append(label)
        print(f"  [SAM] Searching: {label}")
        try:
            results = sam_gov.execute_query(params, sam_key, max_candidates)
        except sam_gov.SamGovKeyError as e:
            print(f"  [SAM] ERROR: {e}")
            return 0, deduped_count, errors + 1
        except Exception as e:
            print(f"  [SAM] ERROR: {e}")
            errors += 1
            continue

        new_this_query = 0
        for r in results:
            nid = r.get("notice_id", "")
            url = r.get("url", "")
            if (nid and (nid in known_ids or nid in seen_ids)) or (url and url in known_urls):
                deduped_count += 1
                continue
            if nid:
                seen_ids.add(nid)
            new_candidates.append(r)
            new_this_query += 1
        print(f"  [SAM] {len(results)} returned, {new_this_query} new")

    if not new_candidates:
        print(f"  [SAM] 0 candidates queued")
        return 0, deduped_count, errors

    # Fetch notice descriptions so the ranker has substantive content to score
    # against. Each description is a separate SAM.gov API call; the per-day
    # quota in _meta/sam-quota.json governs total volume.
    print(f"  [SAM] Fetching descriptions for {len(new_candidates)} notice(s)...")
    for c in new_candidates:
        desc = sam_gov.fetch_description(c.get("description_url", ""), sam_key)
        # Strip HTML tags for the ranker snippet
        clean = re.sub(r'<[^>]+>', ' ', desc or '')
        clean = re.sub(r'\s+', ' ', clean).strip()
        c["_snippet"] = clean[:800]

    if openai_key:
        opp_context = f"{opp_id} — SAM.gov solicitations matched by queries: {', '.join(query_labels)}"
        print(f"  [SAM] Ranking {len(new_candidates)} candidates with OpenAI...")
        new_candidates = ranker.rank_sam_candidates(new_candidates, opp_context, openai_key)
        scores_before = [c.get('_score', '?') for c in new_candidates]
        print(f"  [SAM] Scores (before threshold): {scores_before}")
        # Apply the score threshold
        filtered = [c for c in new_candidates if c.get('_score', 0) >= min_score]
        dropped = len(new_candidates) - len(filtered)
        if dropped:
            print(f"  [SAM] Dropped {dropped} candidate(s) below score {min_score}")
        new_candidates = filtered
    else:
        print(f"  [SAM] No OPENAI_API_KEY — skipping ranking (all candidates kept).")

    if not new_candidates:
        print(f"  [SAM] 0 candidates queued after ranking")
        return 0, deduped_count, errors

    print(f"  [SAM] {len(new_candidates)} candidate(s) queued")
    new_count = inbox.append_sam_candidates(opp_dir, new_candidates, dry_run=dry_run)
    return new_count, deduped_count, errors


def _run_usaspending_search(
    opp_dir: Path, usa_searches: list,
    date_window: int, max_candidates: int, dry_run: bool,
) -> tuple[int, int, int]:
    """Run USAspending search loop. Returns (new_count, deduped_count, error_count)."""
    known_urls = dedup.load_known_urls(opp_dir) | inbox.load_inbox_urls(opp_dir)
    known_award_ids = dedup.load_known_award_ids(opp_dir) | inbox.load_inbox_award_ids(opp_dir)

    deduped_count = 0
    errors = 0
    seen_ids: set[str] = set()
    new_candidates: list[dict] = []

    for entry in usa_searches:
        try:
            filters = usaspending.parse_search_entry(entry, date_window)
        except Exception as e:
            print(f"  [USA] ERROR parsing entry {entry!r}: {e}")
            errors += 1
            continue

        label = (filters.get("keywords") or filters.get("recipient_search_text") or ["(structured)"])[0]
        print(f"  [USA] Searching: {label}")
        try:
            results = usaspending.execute_query(filters, max_candidates)
        except Exception as e:
            print(f"  [USA] ERROR: {e}")
            errors += 1
            continue

        new_this_query = 0
        for r in results:
            piid = r.get("award_id", "")
            gid = r.get("generated_id", "")
            url = r.get("url", "")
            if (piid and (piid in known_award_ids or piid in seen_ids)) or \
               (gid and (gid in known_award_ids or gid in seen_ids)) or \
               (url and url in known_urls):
                deduped_count += 1
                continue
            if piid:
                seen_ids.add(piid)
            if gid:
                seen_ids.add(gid)
            new_candidates.append(r)
            new_this_query += 1
        print(f"  [USA] {len(results)} returned, {new_this_query} new")

    if not new_candidates:
        print(f"  [USA] 0 candidates queued")
        return 0, deduped_count, errors

    print(f"  [USA] {len(new_candidates)} candidates queued")
    new_count = inbox.append_usaspending_candidates(opp_dir, new_candidates, dry_run=dry_run)
    return new_count, deduped_count, errors


def main() -> None:
    parser = argparse.ArgumentParser(description="Find new source candidates via AI search.")
    parser.add_argument("--opportunity", metavar="ID", help="Process a single opportunity.")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print candidates to stdout; do not write files.")
    args = parser.parse_args()

    use_claude, use_gemini, openai_key, sam_key = _check_api_keys()
    if not use_claude and not use_gemini and not sam_key:
        print("ERROR: No API keys configured. Set ANTHROPIC_API_KEY, GEMINI_API_KEY, or SAM_GOV_API_KEY in .env.")
        sys.exit(1)

    if not lock.acquire():
        sys.exit(0)

    try:
        opps = _discover_opportunities(args.opportunity)
        if not opps:
            print("No opportunities to process.")
            return

        total_ai = 0
        total_sam = 0
        total_usa = 0
        for opp_dir in opps:
            ai_n, sam_n, usa_n, deduped, errors = _process_opportunity(
                opp_dir, use_claude, use_gemini, args.dry_run, openai_key, sam_key
            )
            total_ai += ai_n
            total_sam += sam_n
            total_usa += usa_n

        total_new = total_ai + total_sam + total_usa
        if not args.dry_run:
            cron_log.append_summary(len(opps), total_new)
        print(f"\nDone. {len(opps)} opp(s) processed, "
              f"{total_ai} AI + {total_sam} SAM + {total_usa} USA = {total_new} new candidate(s) queued.")

    finally:
        lock.release()


if __name__ == "__main__":
    main()

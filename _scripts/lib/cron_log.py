"""Append-only cron log writer with monthly rotation."""

import re
from datetime import datetime
from pathlib import Path

VAULT_ROOT = Path(__file__).parent.parent.parent
CRON_LOG = VAULT_ROOT / "_meta" / "cron-log.md"


def append_opportunity(opp_id: str, new: int, deduped: int, errors: int) -> None:
    ts = _ts()
    _write(f"[{ts}] {opp_id}: {new} new, {deduped} deduped, {errors} errors\n")


def append_summary(opp_count: int, total_new: int) -> None:
    ts = _ts()
    _write(f"[{ts}] [run summary] {opp_count} opps processed, {total_new} new candidates queued\n")


def _ts() -> str:
    return datetime.now().isoformat(timespec="seconds")


def _write(line: str) -> None:
    _rotate_if_needed()
    CRON_LOG.parent.mkdir(parents=True, exist_ok=True)
    with open(CRON_LOG, "a", encoding="utf-8") as f:
        f.write(line)


def _rotate_if_needed() -> None:
    if not CRON_LOG.exists() or not CRON_LOG.stat().st_size:
        return
    first_line = CRON_LOG.read_text(encoding="utf-8").splitlines()[0]
    m = re.search(r'\[(\d{4}-\d{2})', first_line)
    if not m:
        return
    log_month = m.group(1)
    current_month = datetime.now().strftime("%Y-%m")
    if log_month != current_month:
        archive = CRON_LOG.parent / f"cron-log-{log_month}.md"
        CRON_LOG.rename(archive)

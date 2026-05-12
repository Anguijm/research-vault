"""Lock file management for find_sources.py cron runs."""

from datetime import datetime, timedelta
from pathlib import Path

LOCK_FILE = Path(__file__).parent.parent / ".find-sources.lock"
MAX_AGE_HOURS = 2


def acquire() -> bool:
    """Try to acquire the lock. Returns True if acquired, False if held by a recent run."""
    if LOCK_FILE.exists():
        try:
            ts = datetime.fromisoformat(LOCK_FILE.read_text().strip())
            age = datetime.now() - ts
            if age < timedelta(hours=MAX_AGE_HOURS):
                print(f"Lock held (age: {int(age.total_seconds() // 60)}m). Exiting.")
                return False
            else:
                print(f"WARN: Stale lock found (age: {age}). Removing and proceeding.")
        except Exception:
            print("WARN: Malformed lock file. Removing and proceeding.")
    LOCK_FILE.write_text(datetime.now().isoformat())
    return True


def release() -> None:
    if LOCK_FILE.exists():
        LOCK_FILE.unlink()

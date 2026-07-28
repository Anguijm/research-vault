#!/usr/bin/env bash
# Weekly opportunity-screener run, invoked from cron.
#
# Deliberately boring: absolute paths, one log, no cleverness. find_seeds.py
# loads _scripts/.env by path (not by working directory), so a bare cron
# environment is fine.
#
# Schedule lives in crontab. Check it with `crontab -l`.
# Log: _meta/seeds-cron.log   Triage queue: _meta/seeds-inbox.md

set -uo pipefail

VAULT="/home/johnanguiano/research"
PY="$VAULT/_scripts/.venv/bin/python"
LOG="$VAULT/_meta/seeds-cron.log"

{
  echo ""
  echo "════════════════════════════════════════════════════════════"
  echo "  run: $(date '+%Y-%m-%d %H:%M:%S %Z')"
  echo "════════════════════════════════════════════════════════════"
} >> "$LOG"

"$PY" "$VAULT/_scripts/find_seeds.py" --source sam-gov --weekly >> "$LOG" 2>&1
rc=$?

if [ $rc -ne 0 ]; then
  echo "  !! find_seeds.py exited $rc" >> "$LOG"
fi

# Leave a one-line marker that is easy to grep for when catching up.
surfaced=$(grep -c '^- \[ \]' "$VAULT/_meta/seeds-inbox.md" 2>/dev/null || echo 0)
echo "  untriaged seeds now sitting in _meta/seeds-inbox.md: $surfaced" >> "$LOG"

exit $rc

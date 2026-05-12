#!/usr/bin/env bash
# sync.sh — Stage, commit, and push all vault changes to GitHub.
#
# Usage:
#   _scripts/sync.sh                    # default message: "Sync YYYY-MM-DD HH:MM"
#   _scripts/sync.sh "Custom message"   # use your own commit message
#
# Safety:
#   - Refuses to run if _scripts/.env somehow appears in git changes (leak guard)
#   - Exits cleanly if there's nothing to sync
#   - Shows what changed before committing

set -e

cd "$(dirname "$0")/.."

# Leak guard: real .env must never be tracked
if git status --porcelain | grep -qE '^\s*[MARC?]+\s+_scripts/\.env$'; then
  echo "ERROR: _scripts/.env is in git changes — that file holds API keys."
  echo "       Check .gitignore and 'git rm --cached _scripts/.env' if it slipped in."
  exit 1
fi

# Nothing to do?
if [ -z "$(git status --porcelain)" ]; then
  echo "Working tree clean — nothing to sync."
  exit 0
fi

# Show changes
echo "Changes:"
git status --short
echo

MSG="${1:-Sync $(date '+%Y-%m-%d %H:%M')}"

git add -A
git commit -m "$MSG"
git push

echo
echo "✓ Pushed to $(git remote get-url origin)"

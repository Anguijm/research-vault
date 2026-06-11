#!/usr/bin/env bash
# refresh-obsidian.sh — restart the Obsidian desktop app for the research vault so
# Obsidian Sync re-scans the latest on-disk changes after a commit/sync.
#
# Invoked manually and by the post-"git push" hook (see .claude/settings.json).
# Safe restart: matches Obsidian by process NAME (pgrep without -f, so it can never
# match the calling shell's command line), kills by PID, relaunches detached on the
# desktop display. Never uses `pkill -f` (that footgun once matched our own shell).
set -u

APPIMAGE="$(ls -t "$HOME"/Downloads/Obsidian-*.AppImage 2>/dev/null | head -1)"
if [ -z "$APPIMAGE" ]; then
  echo "refresh-obsidian: no Obsidian AppImage found in ~/Downloads" >&2
  exit 0
fi
DISP="${DISPLAY:-:1}"

# Stop any running instance (by name -> never matches this bash script).
PIDS="$(pgrep -i obsidian 2>/dev/null || true)"
if [ -n "$PIDS" ]; then
  kill -TERM $PIDS 2>/dev/null || true
  sleep 3
  PIDS="$(pgrep -i obsidian 2>/dev/null || true)"
  [ -n "$PIDS" ] && { kill -KILL $PIDS 2>/dev/null || true; sleep 1; }
fi

# Relaunch detached so the caller (or git hook) returns immediately.
DISPLAY="$DISP" setsid "$APPIMAGE" --no-sandbox >/tmp/obsidian-launch.log 2>&1 < /dev/null &
disown 2>/dev/null || true
echo "refresh-obsidian: relaunched ($(basename "$APPIMAGE") on DISPLAY=$DISP)"
exit 0

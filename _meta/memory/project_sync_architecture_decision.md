---
name: Sync architecture decision pending — next week
description: Dual-sync (git+Obsidian Sync) is fragile when Claude Code edits files via shell; operator wants to decide on a fix when back at the laptop next week.
type: project
originSessionId: 254eda7f-7db4-4f93-b460-1e14e2726754
---
The vault uses two independent sync mechanisms that don't coordinate:

1. **Claude Code → disk → git → GitHub** — backup and visibility, works any time
2. **Obsidian-the-app → Obsidian Sync → phone** — operator's reading workflow on mobile

They coexist fine when Obsidian-the-app is the only editor. They break when Claude Code edits files via shell because Obsidian's open-tab buffer holds the stale pre-edit content; disk and GitHub get updated but Obsidian Sync doesn't until Obsidian-the-app re-reads the file. On 2026-06-01 this bit the operator hard — Scenario 3 corrections were on disk and on origin/main but not visible in phone Obsidian. Resolved by killing and relaunching Obsidian on the laptop via shell.

**Why:** Operator was in San Diego on phone via remote control to a laptop in Japan. Could not interact with Obsidian-the-app directly. The dual-sync mechanism's failure mode (stale Obsidian tab buffer) became blocking. The operator's exact words: "Why did we set up this broken system?"

**How to apply:** Do NOT re-litigate this until the operator is back at the laptop next week (approximately 2026-06-08). Three options on the table for that conversation:

1. **Auto-restart Obsidian after Claude Code edits.** A small wrapper that kicks Obsidian's AppImage at session end. Low effort, reliable, ugly.
2. **Drop Obsidian Sync, use git everywhere.** Phone uses iOS git client (Working Copy or similar) to pull from GitHub. Single chain. Loses the "auto-sync" Obsidian phone workflow.
3. **Accept the manual restart as documented workaround** and add a CLAUDE.md note so future sessions know to do it.

Claude's vote was option 1 as highest-leverage. Operator did not decide; said keep this for next week.

Until decided: when the operator is reading from phone Obsidian and reports stale content, the working procedure is `kill <obsidian-pid> && nohup /home/johnanguiano/Downloads/Obsidian-1.12.7.AppImage > /tmp/obsidian-relaunch.log 2>&1 &` from the laptop's shell.

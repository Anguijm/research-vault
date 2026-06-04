---
name: GitHub push is OK — private remote is operator-configured backup
description: HANDOFF.md §11 prohibits "web publishing" and "cloud sync" but the configured GitHub remote (github.com/Anguijm/research-vault.git) is the operator's private repo used for backup and artifact access. Keep it updated; do not hesitate to push.
type: feedback
originSessionId: 254eda7f-7db4-4f93-b460-1e14e2726754
---
The vault has a GitHub remote configured at `https://github.com/Anguijm/research-vault.git`. The HANDOFF.md §11 binding rules say:

1. "Any web publishing. No GitHub Pages, no Quarto site, no static-site generator. The vault is local-only."
2. "Any cloud sync. No iCloud, Dropbox, OneDrive integration. Operator handles backup."

**Why:** Reading these rules strictly creates an apparent conflict with the configured GitHub remote. But the operator confirmed (2026-06-01) the remote is THEIR private repo used for (a) backup and (b) accessing artifacts when away from the local machine. The §11 rules were about preventing PUBLISHING (public web sites, public visibility) and AUTO-SYNC (consumer cloud services without operator control). A `git push` to a private remote that the operator explicitly set up is neither.

**How to apply:**
- Push to `origin/main` when commits accumulate, especially after substantive work the operator might want to access from another device.
- Use the existing "Sync YYYY-MM-DD HH:MM" commit-message convention.
- Do not push to other branches without operator approval; do not force-push.
- If you ever see a NEW GitHub Pages / Quarto / public-site setup proposed, that's still §11-violating — the rule remains in force for actual publishing.

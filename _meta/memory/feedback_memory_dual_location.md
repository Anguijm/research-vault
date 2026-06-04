---
name: Memory writes go to both the auto-memory directory and the vault
description: Every memory file must be written to both `~/.claude/projects/-home-johnanguiano-research/memory/` (Claude auto-load) and `/home/johnanguiano/research/_meta/memory/` (vault + git-tracked)
type: feedback
originSessionId: 254eda7f-7db4-4f93-b460-1e14e2726754
---
# Memory writes go to both the auto-memory directory and the vault

Every memory file (feedback, project, reference, user) must exist in **two locations**:

1. **Auto-memory directory (primary):** `/home/johnanguiano/.claude/projects/-home-johnanguiano-research/memory/`
   - Claude Code automatically loads from here at session start
   - This is what makes the memory available to me across conversations

2. **Vault mirror (operator-visible + git-tracked):** `/home/johnanguiano/research/_meta/memory/`
   - Operator can see and edit these in Obsidian
   - Git-tracked, so they sync to the private GitHub backup
   - This is the durable, operator-visible record

**Why:** Operator-flagged 2026-06-04 that the feedback memories I had been writing only existed in the auto-memory directory — invisible in Obsidian, not git-tracked, not backed up to the private GitHub remote. The auto-memory directory is Claude-internal state, not vault content. Memory entries belong in the vault.

**How to apply:**

- **When writing a new memory file:** create it in BOTH locations. Two `Write` tool calls or one `Write` followed by a `cp`.
- **When editing an existing memory file:** edit it in BOTH locations. Edits to one without the other create drift.
- **When updating `MEMORY.md` (the index):** update in BOTH locations.
- **The vault `_meta/memory/` directory is the canonical record for human review.** The auto-memory directory is operationally-required for Claude's auto-loading but is functionally a mirror of the vault.
- **Bias on conflict:** if the two diverge, treat the vault version as authoritative (operator may have edited it directly in Obsidian).

This rule is binding on all memory writes. It does not apply to other Claude Code state (transcripts, task outputs, hook logs, etc.) — only to the persistent memory system documented in CLAUDE.md.

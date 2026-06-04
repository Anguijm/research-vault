---
name: Karpathy four-rules CLAUDE.md — evaluate integration into vault
description: Operator wants to evaluate later whether to adopt forrestchang/andrej-karpathy-skills behavioral rules into the vault's CLAUDE.md
type: project
originSessionId: 254eda7f-7db4-4f93-b460-1e14e2726754
---
The operator shared the Sumit Pandey *Towards Deep Learning* article (2026-05-08) on the `forrestchang/andrej-karpathy-skills` repo — a single-file CLAUDE.md with four behavioral rules derived from Andrej Karpathy's observations on LLM coding failure modes. 91k stars on GitHub at the time of the article. Operator said *"See how to implement this in our processes later."*

**Why:** This is a "save for later" item — operator wants to evaluate whether the four rules belong in the vault's `CLAUDE.md` (or in a separate skills file) on a future session, not act on it now. The rules map cleanly to failure modes that have shown up in this vault's build (overcomplexity drift, scope creep across phase boundaries, scaffolding files when not asked).

**The four rules, paraphrased from the article:**

1. **Think before coding.** State assumptions out loud. If the request is ambiguous, ask. If a simpler approach exists, push back. Stop when confused and name what is unclear instead of picking an interpretation and running.
2. **Simplicity first.** Write the minimum code that solves the problem. No speculative abstractions, no flexibility nobody asked for. Test: would a senior engineer call this overcomplicated.
3. **Surgical changes.** Touch only what the task requires. Do not improve neighboring code. Do not refactor what is not broken. Every changed line should trace back to the request.
4. **Goal-driven execution.** Turn vague instructions into verifiable targets before writing a line. "Add validation" becomes "write tests for invalid inputs, then make them pass."

**How to apply:** When the operator returns to this in a future session, the integration paths to evaluate are (a) appending a "Behavioral Guidelines" section to `CLAUDE.md` with the four rules verbatim or paraphrased; (b) creating a separate skill file in `.claude/skills/` and referencing it from `CLAUDE.md`; (c) doing nothing because the existing vault CLAUDE.md already encodes most of these via the grill-me skill, the gray-box ownership model, and the phase-boundary rule. Cross-check what the vault's CLAUDE.md already covers before adopting verbatim — the operator's pattern is to avoid redundancy.

**References:**
- Article: Sumit Pandey, "A Single CLAUDE.md File Went Viral. The Reason Is Embarrassingly Simple." *Towards Deep Learning* (Medium), 2026-05-08
- Repo: `forrestchang/andrej-karpathy-skills` on GitHub
- The vault's existing alignment skill at `_meta/grill-me.md` already operationalizes part of rule 1 (stop, name what is unclear, get alignment before scaffolding)

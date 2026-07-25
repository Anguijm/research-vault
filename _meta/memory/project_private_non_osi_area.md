---
name: project-private-non-osi-area
description: the gitignored _private/ area holds non-OSI material the vault reasons from but never cites; the crossing rule and the named-entity corollary
metadata: 
  node_type: memory
  type: project
  originSessionId: 47b5ca29-ff88-45d9-8fa4-924c4cd2c690
---

The vault has a gitignored **`_private/`** area (created 2026-07-26) for material that is useful
but not open-source, so it cannot live in the vault proper under hard rule 1. Governance is in
`_private/README.md`.

**The crossing rule.** `_private/` is a **tasking layer, not a source layer**. It tells you where
to look; it is never cited. A claim crosses into the vault only when all three hold: an independent
open source supports it, that source is recorded in the relevant source ledger, and the vault
wording stands on the open source alone. If a claim cannot clear all three it stays private. It
does **not** get softened into an Assessment and slipped into a research file. "I know this but
cannot source it" is a legitimate end state.

**The named-entity corollary (the part the tooling cannot catch).** Both audits
(`_scripts/audit_named_entities.py`, `_scripts/audit_search_config.py`) check whether an ingested
source surfaced an entity before it appeared in analytical content. Private material defeats them:
the material genuinely does surface the name, but it is in no ledger and cannot be put in one, so
the audit passes on a provenance chain that does not exist. So any named entity reaching vault
analytical content by way of `_private/` needs its own independent open source recorded alongside
it. Companies, people, programs, and dollar figures all count.

**Operational note.** Verify with `git check-ignore` and grep the tracked diff for sensitive terms
before committing whenever private material has informed a session's work. Do not push without
confirming, since the push is the act that would expose a mistake. Relates to
[[project_world_class_planning]] (which item 19 traces to private material) and
[[feedback_named_contractor_discipline]].

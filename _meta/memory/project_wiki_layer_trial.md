---
name: project-wiki-layer-trial
description: two-week trial of a compiled entity-page layer at _meta/wiki/; review due 2026-08-12 with explicit keep/kill criteria
metadata: 
  node_type: memory
  type: project
  originSessionId: 47b5ca29-ff88-45d9-8fa4-924c4cd2c690
---

A **two-week trial** of a Karpathy-style compiled-memory layer, started 2026-07-29, **review due
2026-08-12**. Three hand-compiled entity pages in `_meta/wiki/`: `swrmc.md`, `srf-jrmc.md`,
`pae-industrial-operations.md`. Trial terms and keep/kill criteria are in `_meta/wiki/README.md`.

**Why it exists.** The vault's tracks are siloed by design (good for provenance, bad for recall).
Two failures on 2026-07-28 prompted it: `trip-reports/MEGARUST-2026/` held the SWRMC keynote for
eight weeks while the BDR capture brief carried a caveat saying no Navy demand signal existed, and
the same brief nearly cited a RAND study second-hand because the primary source sat in the operator's
separate brain vault. See [[feedback_check_other_tracks_for_sources]].

**Infrastructure that landed with it (keep regardless of the trial outcome).**
`lib/frontmatter.py` now has `content_sha256()` and `record_sha256()`, wired into all three
frontmatter builders. `_scripts/backfill_source_hashes.py` added the field to the 205 existing
captures (hashes only the `## Extracted content` section, not Summary/Notes, which are ours).
Every wiki page records the source hashes it compiled against; the README carries a shell one-liner
that detects drift.

**Deliberately NOT built:** `wiki_status.py` and a CLAUDE.md rule block. Those are step 3 and wait
on the trial result. Do not build them before 2026-08-12 without the operator saying the trial paid.

**Compilation gotcha worth remembering:** grepping `01_sources/` for an entity matches *our own
analyst commentary* appended inside source files, not only the source's extracted content. The RAND
source matched "SWRMC" purely because of a note we added. Compile from what the source says.

**The standing risk**, and the operator's own framing: this vault's documentation already outpaces
its verified work. Three pages that save time beat forty nobody reads. If the pages were written
once and never reopened, delete the folder — nothing is lost, since every claim restates a source.
Relates to [[project_karpathy_four_rules]].

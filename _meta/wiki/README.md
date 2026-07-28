---
type: wiki-index
title: Vault wiki — compiled entity pages (trial)
classification: internal
created: 2026-07-29
review_due: 2026-08-12
status: trial
---

# Vault wiki — compiled entity pages

**This is a two-week trial, not a committed layer.** Three pages exist. If they do not demonstrably
save time on the next piece of work, delete the folder and nothing is lost, because every claim on
every page is a restatement of something already in `01_sources/`.

## What this is for

The vault's tracks are siloed by design, which is correct for provenance and bad for recall. Two
concrete failures on 2026-07-28 prompted this: the MegaRust trip report held the SWRMC keynote for
eight weeks while the BDR capture brief carried a caveat saying no Navy demand signal existed, and
the same brief cited a RAND study second-hand because the primary source lived in a different vault.
Entities recur across tracks; the folders do not let them meet.

These pages hold **only** what is shared across tracks. Opportunity narrative stays in
`opportunities/<ID>/00_research-file.md`. Method reasoning stays in decision logs.

## Pages

| Page | Claims | Sources | Why it exists |
|---|---|---|---|
| [[swrmc]] | 6 | 1 | Built the Pacific container capability. Most visible executor of the mission BDR targets. |
| [[srf-jrmc]] | 7 | 4 | Appears in four tracks. Customer set, study subject, coordinating command, operator's workplace. |
| [[pae-industrial-operations]] | 6 | 1 | Invalidates NAVSEA 04 as a buying target and explains why no mission owner is nameable. |

## Rules these pages follow

1. **Compile, do not author.** Every FACT restates a source in `01_sources/`. If a claim needs a
   source that does not exist, fetch it first or do not make the claim.
2. **Cite what the extracted content says**, not what our own commentary inside a source file says.
   Caught during compilation: the RAND source file matched a grep for "SWRMC" only because of an
   analyst note appended to it, not because RAND mentions SWRMC.
3. **Record the hash you compiled against.** Every entry in `compiled_from` carries the source's
   `content_sha256` at compile time.
4. **State what is not established.** Every page has a "what is not established" section. The vault
   over-claimed mission ownership once already.
5. **Patch, do not rewrite.** Edit the specific claim and update that source's `compiled_from` entry.
6. `[[entity-id]]` links use the frontmatter `id`, never the display title.

## Checking staleness

No script yet; that was deliberately deferred. Until there is one, this detects drift:

```bash
_scripts/.venv/bin/python - <<'EOF'
import re, pathlib
for page in sorted(pathlib.Path('_meta/wiki').glob('*.md')):
    for sid, sha in re.findall(r'source_id: (\S+)\n\s+sha256: (\w+)', page.read_text()):
        f = pathlib.Path(sid)
        cur = re.search(r'^content_sha256: (\w+)', f.read_text(), re.M) if f.exists() else None
        cur = cur.group(1) if cur else None
        if cur != sha:
            print(f'STALE {page.name} <- {sid}')
EOF
```

Source hashes come from `lib/frontmatter.py` at capture; existing captures were backfilled by
`_scripts/backfill_source_hashes.py` on 2026-07-29 (205 files).

## Trial terms — decide by 2026-08-12

Keep the layer only if at least one of these is true by the review date:

- A page was **read before** writing a brief section or a decision-log entry, and shortened it.
- A page surfaced a cross-track connection that would otherwise have been missed, as the MegaRust
  and RAND cases were.
- The staleness check caught a source change that invalidated a claim already in a brief.

Kill it if all of these are true:

- The pages were written once and never opened again.
- Keeping them current cost more than the briefs gained.
- Claims drifted out of sync with the research files, creating a second version of the truth.

The failure mode to watch for is the one this vault already has: documentation outpacing verified
work. Three pages that save time beat forty nobody reads.

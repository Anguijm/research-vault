# Brief-build configs

This directory holds per-version YAML configs that drive `_scripts/build_brief.py`. Each YAML file describes one version-to-version transition for a Word brief: which source file to read, which output file to write, what text to strip, what to replace, what to insert, and how to bump the version stamp.

The point of the YAML-plus-driver pattern is that surgical .docx edits become data, not code. A new brief version is a new YAML file; the build logic stays in one place.

## Why this exists

Before 2026-05-22 the vault had five separate Python scripts in `_scripts/` for editing PMTEC brief versions (`build_pmtec_brief_v02.py`, `_v03.py`, `_v031.py`, plus two exec-brief equivalents). All five did the same five operations on different input data. That is the "shallow module" pattern — lots of tiny near-duplicates. The Yanli Liu article on AI-assisted code architecture (read 2026-05-22) called it out specifically: AI is exceptionally good at producing shallow modules and they create a navigation nightmare.

The consolidation: one driver (`build_brief.py`), one shared library (`lib/docx_surgery.py`), and one YAML config per version. The legacy `build_pmtec_*.py` scripts remain in place so prior brief lineage stays reproducible, but new brief versions should be built by writing a YAML config, not by copying a previous script.

## Directory layout

```
_scripts/briefs/
├── README.md                                ← this file
├── _schema.example.yaml                     ← annotated template for new configs
└── PMTEC-USINDOPACOM/                       ← one folder per opportunity
    ├── capture-v0.4.yaml                    ← will be created when v0.4 is built
    └── ...
```

## Running the driver

Single config:

```bash
_scripts/.venv/bin/python _scripts/build_brief.py \
    --config _scripts/briefs/PMTEC-USINDOPACOM/capture-v0.4.yaml
```

Multiple configs chained in one invocation (rebuilds the whole lineage in order):

```bash
_scripts/.venv/bin/python _scripts/build_brief.py \
    --config _scripts/briefs/PMTEC-USINDOPACOM/capture-v0.2.yaml \
    --config _scripts/briefs/PMTEC-USINDOPACOM/capture-v0.3.yaml \
    --config _scripts/briefs/PMTEC-USINDOPACOM/capture-v0.3.1.yaml
```

Dry-run (apply operations in memory, print the summary, do not write output):

```bash
_scripts/.venv/bin/python _scripts/build_brief.py \
    --config _scripts/briefs/PMTEC-USINDOPACOM/capture-v0.4.yaml \
    --dry-run
```

## Migration from the legacy scripts

The five legacy `build_pmtec_*.py` scripts are still present. They are the authoritative record of how versions 0.2 through 0.3.1 of the PMTEC briefs were built. Do not delete them.

For new brief versions:
1. Write a new YAML config in this directory under the opportunity sub-folder.
2. Use `_schema.example.yaml` as the starting template.
3. Run `build_brief.py --config <path> --dry-run` first to verify operations.
4. Run without `--dry-run` to produce the actual output.

If you ever need to rebuild a legacy version under the new system, port the contents of the legacy script into a YAML config and verify by diffing the new output against the existing artifact in `04_artifacts/`.

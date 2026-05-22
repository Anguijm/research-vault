#!/usr/bin/env python3
"""
build_brief.py — Single driver for surgical brief edits, replacing the
per-version build_pmtec_*.py scripts.

The driver reads a YAML config describing one version-to-version transition
(strip paragraphs, apply text replacements, insert sections, bump version
stamp) and applies the operations to a source Word document, writing the
result to the configured output path.

Usage:
    _scripts/.venv/bin/python _scripts/build_brief.py \\
        --config _scripts/briefs/PMTEC-USINDOPACOM/capture-v0.2.yaml

Multiple configs can be applied in sequence:
    --config a.yaml --config b.yaml --config c.yaml

The legacy build_pmtec_*.py scripts remain in place so prior brief lineage
stays reproducible. New brief versions should be built by writing a YAML
config and invoking this driver, not by copying a previous script.

Why this exists: the five legacy scripts share ~80% of their code. They are
the textbook "shallow module" pattern — lots of small variants with thin
interfaces. Consolidating them into one driver plus per-version configs is
the "deep module" version, per the 2026-05-22 workflow review of the Yanli
Liu article on AI-assisted code architecture.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml
from docx import Document

SCRIPT_DIR = Path(__file__).parent
VAULT_ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))

from lib.docx_surgery import apply_operations  # noqa: E402


def _resolve_path(p: str | Path) -> Path:
    """Resolve a path string from the config, treating bare paths as
    relative to the vault root rather than the current working directory.
    Absolute paths are returned unchanged."""
    path = Path(p)
    if path.is_absolute():
        return path
    return VAULT_ROOT / path


def _load_config(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        cfg = yaml.safe_load(f) or {}
    required = ("source", "output")
    missing = [k for k in required if k not in cfg]
    if missing:
        raise SystemExit(
            f"{path.name}: missing required key(s): {', '.join(missing)}"
        )
    return cfg


def _process_config(cfg_path: Path, dry_run: bool) -> None:
    cfg = _load_config(cfg_path)
    src = _resolve_path(cfg["source"])
    out = _resolve_path(cfg["output"])

    print(f"\n=== {cfg_path.name} ===")
    print(f"Source: {src.relative_to(VAULT_ROOT) if src.is_relative_to(VAULT_ROOT) else src}")
    print(f"Output: {out.relative_to(VAULT_ROOT) if out.is_relative_to(VAULT_ROOT) else out}")

    if not src.exists():
        raise SystemExit(f"Source docx not found: {src}")

    doc = Document(src)
    summary = apply_operations(doc, cfg)

    if summary["stripped"]:
        print(f"\nStripped {len(summary['stripped'])} paragraph(s):")
        for line in summary["stripped"]:
            print(f"  · {line}…")

    print(f"\nApplied {summary['replaced']} text replacement(s)")

    for inserted in summary["inserted"]:
        anchor = inserted["anchor"]
        n = inserted["paragraph_count"]
        loc = f"before {anchor!r}" if inserted["found_anchor"] else "at end (anchor not found)"
        print(f"Inserted {n} paragraph(s) {loc}")

    if summary["version_bumped"]:
        print(f"Bumped version stamp in {summary['version_bumped']} table cell(s)")

    for warning in summary["warnings"]:
        print(f"WARN: {warning}")

    if dry_run:
        print("\n(dry-run: not writing output)")
        return

    out.parent.mkdir(parents=True, exist_ok=True)
    doc.save(out)
    print(f"\n✓ Wrote {out.relative_to(VAULT_ROOT) if out.is_relative_to(VAULT_ROOT) else out}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Apply surgical edits to a Word brief from a YAML config."
    )
    parser.add_argument(
        "--config",
        action="append",
        required=True,
        type=Path,
        help="YAML config describing one version transition. Can be supplied "
             "multiple times to chain transitions in one invocation.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Apply operations in memory and print the summary, but do not write output.",
    )
    args = parser.parse_args()

    for cfg in args.config:
        _process_config(cfg, args.dry_run)


if __name__ == "__main__":
    main()

# Verifier reports

FACT-vs-source verifier reports for this research track. One file per `verify_facts.py` run.

The verifier compares every FACT-labeled claim in the research file or brief against the cited source's actual content, using a language model to read both and produce a structured agreement / partial / unsupported judgment. The output report lives here.

Filename convention: `YYYY-MM-DD.md` for a vault-wide research-file verification run, or `YYYY-MM-DD-vN.N.md` for a verification scoped to a specific brief version. For example, `2026-05-11.md` is a research-file verification run on 11 May 2026; `2026-07-15-v0.1.md` is a verification scoped to brief version 0.1 on 15 July 2026.

When the verifier writes inline status markers into the research file (the `[✓ INGESTED]` / `[⚑ PARTIAL]` / `[⚠ PENDING-INGEST]` / `[✗ UNSUPPORTED]` flags), those edits go directly into the research file and not here. This directory is the run-report archive only.

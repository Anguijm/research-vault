# Red-team reports

Cross-AI red-team passes against briefs for this research track. One file per pass.

The cross-AI red-team is described in the SOP at `_meta/sop.md` section 5.4 — the drafting model produces a brief, and a different model (the one not used for drafting) runs three personas in sequence: customer reviewer, competitor analyst, and skeptical executive. The output of each pass lands here.

Filename convention: `YYYY-MM-DD-model-version.md`. For example, `2026-07-15-gemini-3.1-pro-v0.1.md` is a Gemini 3.1 Pro red-team of a brief at version 0.1, run on 15 July 2026.

When the red-team output is also serialized as JSON (newer red-team script output), the JSON file uses the same base name with a `.json` extension and lives alongside the markdown version.

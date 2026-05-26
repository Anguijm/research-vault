---
type: red-team-dialogue
opportunity: BDR-FLEET-READINESS
scope: Capture brief v0.1 and executive brief v0.1 — distillation/integrity check after assembly from sealed §§3-7
drafting_model: Claude (Anthropic) Opus 4.7
reviewing_model: Gemini Pro (Google)
rounds_completed: 1
date: 2026-05-26
verdict: GO on both briefs as v0.1 drafts shippable for BD-team review and exec review respectively
---

# Brief-assembly red-team — v0.1 capture brief + v0.1 executive brief

## Context

This dialogue is the small-ships distillation pass per `_meta/small-ships-workflow.md`: after the §§3-7 small-ships have been sealed, the brief assembly itself runs through a red-team check to confirm the analytical line carried over cleanly into the deliverable artifacts. Per the operator's autonomous-run directive, this round is bounded — Gemini was asked for blocking-issues only, not stylistic nits, with the prior §3 and §§4-7 dialogue convergence as the established analytical baseline.

## Round 1 — three integrity checks, GO verdict

Claude built two artifacts:
- `04_artifacts/capture-brief-v0.1-draft.docx` — 10-section BD-team brief, ~12 pages, built from scratch by `_scripts/build_bdr_capture_brief_v01.py` (no prior version to surgically edit). Structure: BLUF / Demand Signal / Customer Landscape / Competitive Landscape / Our Fit / Working Hypothesis / Recommendation / Risks / Asks / Source Ledger.
- `04_artifacts/executive-brief-v0.1-draft.docx` — 1-page exec brief, ~450 words, built from `_scripts/build_bdr_exec_brief_v01.py` following the distillation prompt at `_meta/prompts/distillation-capture-to-exec.md`. Structure: BLUF / Why It Matters / Recommendation / Top Risks / Asks.

Gemini ran three integrity checks:

**Check 1 — BLUF integrity.** PASS. The capture brief BLUF and exec brief BLUF carry the same recommendation. A minor syntactical difference — the capture brief frames the SBIR/STTR/DIU pilot as a path-to-prime (sub first, prime later via pilot maturation), while the exec brief frames it as an alternative entry path (sub or pilot as parallel options). Gemini judged this not a blocker because in procurement reality both are true (a pilot is structurally a different entry door that confers prime status), and the exec-brief framing translates the capture-brief's sequenced logic into a clean A/B set of actionable doors that fits the distillation prompt's "no hedging" rule.

**Check 2 — capture-to-exec compression discipline.** PASS. The compression cleanly drops items an exec does not need (NAWCTSD 9-prime competitor map, the six falsifying legs of the hypothesis) while keeping the load-bearing takeaway (incumbent-lockout risk preserved in Top Risks, even though the names are not). Specific pathway names ("PACFLT or USFF N7/N4," "DIU/SBIR/STTR") added in the exec BLUF are strong distillations of the broader "fleet-command exercise-authority" and "procurement-pathway prototype" language from the capture brief. Everything in the exec brief traces back to capture-brief sections 2, 3, 4, and 7.

**Check 3 — new framing risk.** PASS. The small-ships discipline held. Scope stayed strictly anchored to the maintenance / readiness demand signal (SWARMEX-Cebu). The two-layer procurement model survived the translation (SRF-JRMC as sponsor cleanly decoupled from the contracting vehicle). ARKA boundaries rigidly maintained (threat-side only) with the HM&E bridge correctly flagged as dependency/risk rather than assumed capability. No "ghost" PEO C4I or PMW-160 pathways sneaked back into the text.

## Verdict

**GO on both v0.1 briefs.** Shippable as drafts for BD-team review (capture brief) and exec review (executive brief). No blocking issues. The analytical line from the §3 dialogue (3 rounds) and the §§4-7 multi-section dialogue (2 rounds + micro-fix) carried over cleanly into the deliverables.

Operator may iterate to v0.2 etc. based on BD-team feedback and the next find_sources pass results; the surgical-edit pattern at `_scripts/briefs/<OPPORTUNITY>/<artifact>-<version>.yaml` documented in `_scripts/briefs/README.md` is the right tool for version-to-version updates.

## Small-ships-workflow pilot timing

- Brief assembly + Gemini round-1 check: ~30 minutes wall-clock.
- Brief assembly used direct .docx construction via python-docx rather than the YAML-driven surgical-edit pattern, because there was no prior v0.1 to edit. v0.2+ should use `_scripts/build_brief.py` per `_scripts/briefs/README.md`.
- No verifier run on the briefs themselves — verify_facts.py operates against research-file FACT claims; the briefs derive their FACTs from already-verified research-file sections. Per the small-ships workflow, the verifier check happened inside the §§3-7 section loops; the brief inherits that verified state.

## Pilot total timing (BDR-FLEET-READINESS path-2 autonomous run, 2026-05-26)

- §3 single-section small-ship: ~90 minutes wall-clock, 3 Gemini rounds, GO.
- §§4-7 multi-section small-ship: ~120 minutes wall-clock, 2 Gemini rounds + 1 micro-fix, SEAL.
- Brief assembly + integrity check: ~30 minutes wall-clock, 1 Gemini round, GO on both artifacts.
- Total path-2 wall-clock from §3 ship-start to both briefs shippable: approximately 4 hours.

Compared to the PMTEC big-batch baseline (v0.1 → v0.3.1 across four full-brief revisions over several hours each — see `_meta/small-ships-workflow.md` motivation paragraph), the small-ships variant compressed the entire research-file-rebuild plus capture brief plus exec brief into a single ~4-hour autonomous run. Whether this generalizes to other opportunities and other operators depends on (a) the analytical scope stability — corrected-scope frame was held by the operator's explicit directives; (b) the cross-AI red-team convergence rate — Gemini Pro was an effective adversarial collaborator across all five rounds; (c) the source-corpus pre-work — the 96+ files in `01_sources/` had already been ingested before the small-ships pilot started, so each section had source-grounded FACTs to draft from. The pilot data is recorded here for the operator to evaluate when they return.

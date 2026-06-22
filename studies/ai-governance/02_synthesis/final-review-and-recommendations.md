---
type: synthesis
study: ai-governance-landscape
title: Final red-team review + recommendations for approval (whole package)
status: recommendations (awaiting operator final approval)
classification: internal
created: 2026-06-22
reviewed: instruction v0.10 + pilot memo + departmental template + cover sheet
red_team: Gemini (flash, high), 2 rounds, 2026-06-22
---

# Final review and recommendations

A two-round Gemini red-team dialogue across the whole package, with the vault's discipline
applied (settled decisions not reopened; Navy specifics verified; date-of-knowledge fenced).
Gemini's verdict after round 2: ready for routing once the accepted adds are folded in. These
are **recommendations awaiting operator final approval**; nothing below is folded into the
instruction yet.

## A. Recommended changes — fold in on approval (→ final version)

1. **§7.c — Export control / Foreign Disclosure (STRONG, command-critical).** Add: Local
   National access is subject to the existing Foreign Disclosure Office and export-control
   (ITAR/EAR, deemed-export) vetting, and no AI use case circumvents the command's Technology
   Control Plans. Closes a real gap for the MLA/IHA workforce; inherits existing FDO/TCP process.
2. **§6 — Technical-authority backstop for DFS (STRONG, protects the CHENG).** Add: AI output is
   not, by itself, engineering justification for a Departure from Specification; the technical
   authority adjudicates independently (AI "reasoning" is not a substitute).
3. **§12 / §15 — document the manual fallback.** The manual-fallback procedure must be written
   into the departmental plan (a fallback nobody wrote down is no fallback).
4. **§11.c — prompt-injection reporting.** Users report suspected prompt injection or
   manipulation as a cyber incident via the ISSM (ConMon already watches for it; this adds the
   user-reporting path).
5. **Pilot memo §3 — explicit read-only.** State that §7 write-actions are prohibited for the
   pilot duration, so a user reading only the instruction can't infer write is authorized.
6. **§2 — trim the contract-vehicle example.** Drop the specific "Army-managed Ask Sage IDIQ"
   example; keep the generic "a Department contract vehicle." (Consistent with the no-volatile-
   identifiers principle.)
7. **§14 — drop the "best-in-class" superlative.** Keep the NIST AI RMF + DoD AI Ethical
   Principles mapping and the annual review; remove the unsupported superlative.
8. **§4.f — reinforce CUI marking responsibility (correct terminology).** Strengthen: AI-
   generated content does not exempt the user, as the authorized holder, from correctly
   designating and marking CUI. **Do NOT use "derivative classifier"** — that is a classified-
   information term (EO 13526); CUI is designated/marked under DoDI 5200.48. (Code 200's
   derivative classifier in §5 is the correct, separate use of that term.)

## B. Instruction number (operator's question)

9. **"5239.1" is inherited from the original AI draft, not command-assigned.** SSIC 5239 is the
   Navy cybersecurity subject code (hence SECNAVINST 5239.3C). It is defensible, but an AI-*use*
   governance instruction may fit better under **SSIC 5230** (information-technology management /
   use of IT resources) or **5200** (management programs). **Recommendation:** mark the number
   `[command directives control / Code 1100 assigns the SSIC and sequential number]` rather than
   asserting 5239.1; let 1100 make the call. We have carried this unverified number for ten
   versions — worth fixing now.

## C. Rejected / no change (with reasons)

- **Code 400 (Logistics).** Gemini speculated it might exist; the operator confirmed there is no
  Code 400 (500 = Supply/Logistics). Gemini conceded. No change.
- **Halt-authority billet (ISSM/ED).** Deliberately a working-group-to-confirm item; not ours to
  assert. Gemini conceded. No change.
- **"No-reliance / veracity" clause.** Already covered by §3.b ("'The AI produced it' is never a
  justification for an error, a deviation, or a disclosure"). No new clause needed.
- **Annex A prompt library.** Keep — it is administrative-annex efficiency guidance (suggested/
  vetted), not a mandatory script.

## D. Optional (operator's call)

- **Host-nation / APPI / SOFA caveat.** Gemini flagged Japanese data-protection (APPI) / SOFA
  sensitivity for host-nation data. Mostly covered: MLC *personnel* data is PII, already
  prohibited (§4). Optional light add: a one-line Legal-consult caveat for host-nation-
  proprietary data. Low priority.
- **§9.e wording.** Minor: note that permanent time-savings tracking is finalized on the
  pilot-validated method. Already largely implied.

## Net

Eight folds (A1–A8) + the instruction-number fix (B9). Everything else either rejected with
reason (C) or optional (D). With A1–A8 folded, Gemini assessed the package "ready for routing."

---
type: decision-log
study: world-class-planning
classification: internal
created: 2026-06-23
---

# Decisions and direction

A running log of where the thinking has settled and what's still open. This is a thinking
project — "decisions" here are direction, not commitments.

## Settled direction (as of 2026-06-23)

1. **Frame.** The brief is world-class planning's shift from Cost-As-Independent-Variable to
   Schedule-As-Independent-Variable; the concrete question is a consistent early screen of
   incoming work against: 96-hour close-out? / 6-week CMAV fit? / splittable across windows? —
   done in AIM, which SRF uses and the other RMCs (on NMD) don't.
2. **The screen mostly already exists in SRF policy.** CMAV (2–6 wks) and the multi-WOO split are
   defined in 4700.1F; the 96-hour question is **not** in SRF's documents (fire-safety threshold
   only) and must be defined locally if adopted.
3. **Screen super early — at JCN induction.** Consequence: it runs before AIM's planned duration
   exists, on the brokered Class F (±40%) estimate plus history. Design it as a **three-bin sort**
   (deferrable / must-do / marginal), not a yes/no.
4. **Lead with the drydock cut.** Structural, readable at induction, needs no duration estimate,
   decides much of the "must-do" list on its own.
5. **Attribute labor, not span.** Labor adds up across bundled JCNs; Cycle Time does not. Recover
   per-JCN **labor** from history; convert to span downstream.
6. **Two estimation methods.** Simple: job-costing allocation (direct-attribute mappable CU Phases,
   allocate shared phases by Class F man-hours). Rigorous: regression disaggregation across all
   Job Summaries (recover per-bin labor, or a per-bin actual-to-estimate multiplier = PfCw, with
   confidence). Both in [estimate-attribution](02_synthesis/estimate-attribution.md).
7. **Predict standalone span for the screen** (conservative); calibrate the span conversion on
   clean one-JCN history; use bundled history only for labor.
8. **OSI-clean.** All sources are Distribution A.

## Open questions (operator's to resolve)
- **Data reach:** can Cycle Time and AQWP actually be queried by SWLIN / work type out of AIM-NT or
  the HIT Kit? Everything rests on this.
- **JCN ↔ SWLIN in bundles:** mostly one-to-one (so most labor direct-attributes) or do JCNs
  routinely share a SWLIN (so lean harder on allocation/regression)?
- **"96 hours":** define it (elapsed clock hours vs. work-shifts), and find its source (JFMM /
  TYCOM REDLINES / local) — or decide to drop it.
- **Where the screen runs:** fold into the existing Shop Screening Process (§9), or stand it up
  separately?
- **Project intent:** is the end state a thinking memo, a method/spec SRF could implement, or a
  brief to present? (Drives whether this stays a thinking track or grows a build.)

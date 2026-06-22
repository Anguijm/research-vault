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
9. **Bin at SWBS 3-digit (~100 bins); solve for a multiplier, not man-days.** Operator: the bundles
   live at the Ship Work Breakdown Structure (SWBS) level — the first three digits of the SWLIN,
   ~100 groups. Solve each bin for its **performance multiplier** (actual ÷ estimated labor =
   PfCw), which is size-independent, so the Class F estimate carries the size and ~100 bins is
   enough. Same-SWBS bundles then self-solve (total actual ÷ total Class F = the multiplier);
   regression is only for cross-SWBS bundles. Thin bins shrink toward the 1-digit SWBS parent.
10. **Two explicit conversions** (the gap the operator flagged): (1) estimate → expected actual
    labor = Class F × bin multiplier; (2) labor → span = a per-bin span model from clean one-JCN
    Cycle Time ≈ fixed wait (cure/test) + labor ÷ (crew × shifts/day). Span has a big non-labor
    component, so dividing labor by crew is not enough. Shortcut: where a bin has rich clean
    one-JCN span data, model Cycle Time directly and skip the labor middleman.
11. **Validate:** the multiplier is roughly constant within a SWBS group (split by size if not).

## Open questions (operator's to resolve)
- **Data reach:** can Cycle Time and AQWP actually be queried by SWLIN / work type out of AIM-NT or
  the HIT Kit? Everything rests on this.
- **Bundle level:** answered — bundles are at SWBS 3-digit (item 9). Remaining: does the
  per-SWBS multiplier hold across sizes, or do big jobs in a group run at a different ratio
  (→ split that group by size)?
- **"96 hours":** define it (elapsed clock hours vs. work-shifts), and find its source (JFMM /
  TYCOM REDLINES / local) — or decide to drop it.
- **Where the screen runs:** fold into the existing Shop Screening Process (§9), or stand it up
  separately?
- **Project intent:** is the end state a thinking memo, a method/spec SRF could implement, or a
  brief to present? (Drives whether this stays a thinking track or grows a build.)

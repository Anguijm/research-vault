---
type: backlog
study: world-class-planning
title: Future-state to-dos (deployment + open analytical items)
classification: internal
created: 2026-06-24
---

# Future state — to-dos

What this becomes once the fit is validated. Top item is the user-facing tool; the rest are the
known analytical follow-ons.

## 1. Power App screening calculator (the user-facing tool)

**Vision.** A user pastes incoming JCN rows (JCN, SWLIN, estimated man-days) and gets back a
predicted span and a screen verdict (deferrable / CMAV-capable / marginal / must-do) per JCN — no
Qlik, no analysis, just paste-and-read.

**The design principle that keeps it simple: decouple the model from the app.** The Qlik fit's only
output to the app is a small **coefficient table** — one row per SWBS: `SWBS, Slope, Intercept, n,
MedianSpan` — plus a 1-digit parent table, a global fallback, and the thresholds
(`v96Days`, `vCMAVDays`, `vMinN`). That table (~100 rows) *is* the model. The app never touches AIM.

**Where the table lives.** Qlik (or the Excel build) exports the refreshed coefficient table to a
**SharePoint list / Dataverse table / Excel-on-SharePoint** on a cadence (quarterly, as new
availabilities complete). Power Apps connects to that as its data source. Stamp it with a model
date so the app can show "model as of <date>."

**App flow (canvas app):**
1. A multi-line paste box (user copies JCN, SWLIN, est-man-days rows straight out of Excel).
2. Parse: `Split(Box.Text, Char(10))` for rows, `Split(row, Char(9))` for tab-separated columns;
   `ForAll(...)` into a working collection. Derive `SWBS = Left(SWLIN, 3)`.
3. Predict per row (shrink to parent/global if the SWBS is thin):
   ```
   With(
     { own: LookUp(SWBSModel, SWBS = inSWBS && n >= vMinN),
       par: LookUp(SWBSParent, SWBS1 = Left(inSWBS,1) && n >= vMinN) },
     With({ s: Coalesce(own.Slope, par.Slope, gSlope),
            b: Coalesce(own.Intercept, par.Intercept, gIntercept) },
       Max(0.5, b + s * inEstMD)))
   ```
4. Bin: `If(drydock, "Must-do (drydock)", If(pred <= v96Days, "Maybe – 96hr",
   If(pred <= vCMAVDays, "Maybe – CMAV", If(pred <= vCMAVDays*1.25, "Marginal", "Must-do – exceeds CMAV"))))`.
5. Results gallery: JCN, predicted span, bin, **which tier was used (own / parent / global) and the
   `n`** — so a user can see when a prediction rests on thin history.

**Governance:** show the model date and the per-row confidence (`n` / tier); re-export the
coefficient table on each re-fit; keep the prediction logic identical to the Qlik script so the app
and the analysis never diverge.

**Alternatives if Power Apps is heavier than needed:** the same coefficient table drives an **Excel
"screen-calculator" sheet** (XLOOKUP + the same formula) for a single-user tool, or a **Power BI
what-if** for a dashboard. Power Apps wins for the multi-user paste-and-go workflow.

**Depends on:** the fit being validated (run the tests first); the **drydock input** (the cleanest
override — needs either a pasted flag or a SWLIN→drydock rule); and the **"96 hours" unit**
decision.

## 2. Other open analytical to-dos (cross-ref `_decisions.md`)
- **Drydock override** in the screen (structural must-do) — also feeds the app's drydock input.
- **The true labor multiplier** via the AIM↔COST/STARS join (`COST_FJ40` actual hours by Job Order)
  — to de-bias the estimate itself; lets the app predict from a corrected estimate.
- **Define "96 hours"** (clock-hours vs work-shifts; not in 4700.1F) — sets the app's threshold.
- **Splittability** (the third screen question) — provisional by work type until planning produces
  the engineered steps.
- **Optional:** segment the fit by availability type (`PROJECT_TYPE_CD`) if spans differ
  systematically between CMAV and CNO work.

---
type: study-readme
study: world-class-planning
title: World-class planning — schedule-as-independent-variable work screening in AIM
status: thinking project (organizing; nothing built yet)
classification: internal
created: 2026-06-23
osi: yes — all source documents are Distribution Statement A (approved for public release)
---

# World-class planning — the early work-screening problem

A thinking project, not a deliverable pipeline (yet). It works through one question the
operator is organizing: **how SRF-JRMC could put consistent schedule estimates behind an
early screen of incoming work, the way the other Regional Maintenance Centers (RMCs) are
moving to — but inside AIM, which SRF uses and they don't.**

## The brief that started it
The operator was briefed on "world-class planning," whose theme is shifting from **Cost As an
Independent Variable (CAIV)** — fix the cost, let schedule and scope flex — to **Schedule As an
Independent Variable (SAIV)** — fix the delivery date, let cost and scope flex. The other RMCs
intend to screen each incoming work item for a Chief of Naval Operations (CNO) availability
against three questions:

1. Can we close it out within **96 hours**?
2. Can it fit in a **6-week Continuous Maintenance Availability (CMAV)**?
3. Can it be **broken up across multiple windows of opportunity**?

Their logic: **yes to all three → "maybe" pile** (it can be absorbed elsewhere, so it need not
consume the big availability); **no to any → "must-do" list** (nowhere else to do it, so it has
to be in the CNO work package). It is a schedule-protection filter — only let into the scarce
big window what genuinely can't live anywhere else.

## Why it's a real problem for SRF specifically
SRF-JRMC plans in **AIM (Advanced Industrial Management)**; the other RMCs plan in **NMD (Navy
Maintenance Database)**. So the screen, written in NMD/CMAV packaging terms, doesn't drop
straight into how SRF packages work. The project is about answering the three questions
*consistently* using AIM's own data.

## Where the thinking has landed so far
- Two of the three questions are **already defined in SRF's own Availability Management Manual**
  (NAVSHIPREPFACINST 4700.1F): the CMAV (2–6 weeks) and the multi-window split. The **96-hour**
  one is **not** in SRF's documents at all (it appears only as a fire-safety threshold). See
  [the grounding note](01_sources/aim-ng-grounding.md).
- The screen should run **super early — as Job Control Numbers (JCNs) arrive in AIM** — which
  means it runs before AIM's good duration estimate exists, on the rough brokered estimate plus
  history. See [the early-screen note](02_synthesis/early-jcn-screen.md).
- The hard part is **attributing historical actuals to individual JCNs** when several were
  bundled into one Job Summary. The fix is to attribute **labor (which adds up), not span (which
  doesn't)**, and there's a clean way to recover per-JCN labor from bundled history. See
  [the attribution note](02_synthesis/estimate-attribution.md) — including the plain-English
  walk-through of the method.
- **The bundling worry mostly dissolves in the tool.** Bin at the SWBS 3-digit level (~100 bins)
  and solve each for a size-independent **multiplier** (actual ÷ estimated labor); then
  `Σ(actual) ÷ Σ(estimate)` by SWBS needs **no per-JCN splitting at all**, because both sides sum
  to SWBS on their own. Two explicit conversions follow (estimate → labor → span). What fields to
  pull and how to crunch them in Excel/QlikView is in
  [the data & tooling note](03_build/data-fields-and-tooling.md).

## Files
- `01_sources/aim-ng-grounding.md` — what the AIM-NG manuals and 4700.1F actually say, distilled.
- `source-ledger.md` — the 13 Distribution-A source documents and where they live.
- `02_synthesis/early-jcn-screen.md` — the screen design: super-early at JCN induction.
- `02_synthesis/estimate-attribution.md` — the bundled-JCN attribution problem and the method.
- `03_build/data-fields-and-tooling.md` — what fields to pull from AIM and how to crunch them in
  Excel (Power Query + Power Pivot) or QlikView; the SWBS Σ/Σ trick that sidesteps the bundling;
  the real field map from the operator's Qlik environment (actuals live in COST/STARS, not AIM).
- `03_build/span-screen-qlik.md` — the first-cut screen as a runnable QlikView script (span fit
  per SWBS; no COST join needed).
- `03_build/span-screen-tests.md` — test harness for that script: in-script TRACE diagnostics
  (pass/fail counts to the reload log), the sheet objects to eyeball the fit, and acceptance
  criteria mapped to the [CONFIRM] items.
- `01_sources/qlik/` — the operator's raw Qlik artifacts (load script, data dictionary, field
  dump, Gemini build session).
- `_decisions.md` — direction and open questions.

## Notes on how this project runs
- **OSI-clean.** Every source document is Distribution Statement A (public release). No CUI.
- This is the operator **organizing thoughts**. Nothing is being built or delivered. The folder
  name and structure are provisional — rename freely.

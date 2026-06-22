---
type: build-note
study: world-class-planning
title: What to pull, and how to crunch it in Excel / QlikView
classification: internal
created: 2026-06-23
---

# Data fields and tooling

What fields to request from AIM, and how to do the analysis in one Excel workbook (or QlikView).
The headline: **if you target a SWBS-level multiplier, you never have to split the bundles by
hand — the tool does it by summing.**

## The trick that dissolves the bundling problem
The hard part was attributing actuals to individual JCNs inside a bundled Job Summary. You don't
have to. The bin's multiplier is just **total actual labor ÷ total estimated labor for the
SWBS group**, and both sides can be summed to SWBS *independently*:

- Sum **actual labor (AQWP)** over the CU Phases in a SWBS — CU Phases already carry the SWLIN, so
  this needs no JCN attribution at all.
- Sum the **estimate** over the same SWBS — group the estimates by the SWLIN/SWBS they belong to.

Divide the two. A bundled Job Summary just contributes its pieces to those two sums like everything
else. So in a PivotTable or a QlikView chart, the multiplier is `SUM(actual) / SUM(estimate)` by
SWBS — and the "hundred bundles" never have to be pulled apart. (Per-JCN attribution only comes back
if you later want per-JCN numbers, or to clean up work that sprawls across SWBS groups.)

## Fields to pull

Pull two tables and join them on **JCN**.

### Table 1 — the fact table, one row per CU Phase (Key Op)
This is the grain you named. Whatever your CU-Phase/Key-Op key is called locally (you said "ICN"),
that's the row key.

| Field | Why |
|-------|-----|
| JCN (Job Control Number) | links to Table 2; lets you count JCNs per Job Summary (the bundle flag) |
| Job Summary number | identifies bundles (multi-JCN summaries) and bounds the job's span |
| CU Phase / Key Op ID | the row key — the schedulable unit |
| CUI / Component Unit + Type | the component worked |
| **SWLIN** | derive **SWBS = first 3 digits** — the bin |
| **QAC** (Quantity at Completion, Resource-Days) | planned **estimate** of labor |
| **AQWP** (Actual Quantity of Work Performed, Resource-Days) | **actual** labor — the multiplier's numerator |
| DU (planned Duration, shifts) + Calendar Code | planned span + shift pattern (1-shift "15" vs 2-shift "25") |
| Crew size + man-hours by Shop / Trade Skill Designator | for the labor→span conversion |
| **ASD** (Actual Start) + **AFD** (Actual Finish) | compute **Cycle Time = AFD − ASD** (actual span) |
| CU Phase status (e.g., CRT = certified/closed) | filter actuals to **completed work only** |
| Work type (O / N / R / M) | Original / New / Rework / Missed — filter or segment |
| Phase letter (U/A/R/T/…) | flags test/cure/wait phases (the non-labor span) vs production |
| Mandatory flag; drydock/Key-Event ties (DD00/UD00) | the drydock cut and the must-do/deferrable split |
| Availability ID + type + ship/hull + completion date | context, recency weighting, drydock |

### Table 2 — the JCN table, one row per JCN
| Field | Why |
|-------|-----|
| JCN | the key |
| Primary SWLIN → SWBS | groups the estimate side by bin |
| **Class F estimate** (man-days, material $) | the **induction estimate** — what the screen will actually have, and the better denominator for the multiplier |
| Mandatory flag, work type | screening attributes |

**One basis decision:** the multiplier should ideally be `actual ÷ Class F`, because Class F is
what you'll have at induction. If Class F isn't reliably retained in history, fall back to
`actual ÷ QAC` and accept that your screen input (Class F) and your calibration base (QAC) differ
by the planning-refinement gap — note it, don't hide it.

## Doing it in Excel (one workbook, the right way)
Don't build this out of VLOOKUPs across giant sheets — it won't scale and it won't refresh. Use the
two engines already in Excel:

1. **Power Query (Get & Transform) to pull, join, and derive.** Point it at the extracts; join
   Table 1 to Table 2 on JCN; add derived columns there: `SWBS = Text.Start([SWLIN],3)`,
   `CycleTime = [AFD] - [ASD]`, and a `JCNsPerSummary` count. It's **refreshable** — re-pull, hit
   refresh, the whole model updates. This is the single biggest time-saver.
2. **Power Pivot / the Data Model for relationships and measures.** Load the tables into the Data
   Model, relate CU Phase → JCN. Write the multiplier as one measure:
   `Multiplier := DIVIDE( SUM(Fact[AQWP]), SUM(Estimate) )`, and `n := DISTINCTCOUNT(Fact[JCN])`.
   Handles millions of rows; no VLOOKUP chains.
3. **PivotTable the rollup.** SWBS down the rows; `Multiplier` and `n` as values. There's your
   per-bin table, bundling and all, in one pivot.
4. **Carry the count next to every multiplier**, and **shrink thin bins to their parent.** A simple
   rule: if `n ≥ threshold` use the SWBS multiplier, else use the 1-digit SWBS group's multiplier
   (or a global one). Put the threshold on the parameters sheet.
5. **Median, not mean, for spans.** Cycle Times are skewed; use MEDIAN / PERCENTILE and winsorize
   (cap) the wild outliers, or flag any job with a crazy actual÷estimate ratio for a human look.
6. **Filter actuals to closed work** (status = certified), drop zero-duration Level-of-Effort
   phases, and decide whether Rework/Missed work belongs in or out.
7. **A parameters sheet.** 96-hour definition, 6-week threshold, crew/shift assumptions, the
   shrink threshold — all live here, never hardcoded in a formula.
8. **A screen-calculator sheet.** Paste a new JCN's SWBS + Class F estimate; XLOOKUP the bin's
   multiplier and span model; return the three-bin verdict. That's the deliverable the screen runs.
9. **Workbook hygiene:** raw pulls on their own tabs, untouched and date-stamped; one direction of
   flow (raw → query → model → pivots → calculator); a fact table and small dimension tables (a
   star), even in Excel.

## Doing it in QlikView (better for slicing)
QlikView's associative model fits the relational shape better and handles the volume:
- In the **load script**, compute `SWBS = Left(SWLIN, 3)` and let QlikView associate Fact ↔ JCN ↔
  availability automatically.
- Multiplier as an expression in a straight table by SWBS: `Sum(AQWP) / Sum(ClassF)`.
- **Set analysis** for closed work only: `Sum({<Status={'CRT'}>} AQWP)`.
- `Count(DISTINCT JCN)` gives bundle sizing and the per-bin n for free.
- Use it to **explore** — slice by ship, availability type, work type, time — to see where the
  multiplier is stable and where it wanders. Lock the final model in Excel if Excel is the hand-off.

## Two span pieces Excel/QlikView still need
The multiplier gives you **labor**. For the **span model** (Conversion 2):
- From **single-JCN Job Summaries only**, take the job's actual span (Cycle Time) and fit, per SWBS,
  `span ≈ fixed_wait + labor ÷ (crew × shifts/day)`. The fixed wait is the cure/test floor; the
  slope is the labor rate. A scatter of span vs labor per SWBS (or just a median span and a median
  labor) gets you a usable first cut.
- Keep span built from **single-JCN** jobs (standalone span); use bundled data only for the labor
  multiplier. Mixing bundled spans in here understates the span.

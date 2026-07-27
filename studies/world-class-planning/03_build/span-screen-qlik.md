---
type: build-script
study: world-class-planning
title: First-cut screen — span fit per SWBS (QlikView load script)
classification: internal
created: 2026-06-23
status: draft script — verify the [CONFIRM] keys/fields against the live model before trusting output
---

# First screen: span fit per SWBS

A runnable QlikView load script for the first-cut screen — the **shortcut** path that needs no
COST/STARS actual-labor join. It learns, per SWBS, a span model from completed **single-JCN**
history and uses it to sort a candidate JCN. It works entirely off the published `AIM_*.qvd`
layer, in the style of the operator's own scripts.

**What it does, in one line:** for each completed single-JCN job, take its estimate (man-days) and
its actual standalone span (Cycle Time = Actual Completion − Actual Start); fit `span ≈ Intercept +
Slope × EstManDays` per SWBS (3-digit); then score a new JCN's estimate against that fit and bin it
deferrable / CMAV-capable / must-do.

> **STOP — this file is now the lineage copy, not the live script.** Two live runs have happened.
> The current working version is `Latest Script` in this folder; this file is kept because the
> vault keeps draft lineage, and because the `[CONFIRM]` list below is still the best record of the
> real field names.
>
> **Run 1 (2026-07-26):** reloaded cleanly, output unusable. All 2,699 candidates landed in
> `MUST-DO` because the fitted intercept was about **366 days** — `Span_Days` was measuring the
> availability-lifecycle envelope, not a job's execution window. Decision-log item 22.
>
> **Run 2 (2026-07-27):** SWBS mapping repaired by reading the code off the CU phase
> (`Mid(ICN,6,3)`, `badSWBS=0`), 17,829 training summaries, 233 bins, no synthetic keys. But the
> span-range diagnostic printed blank, so **it is still unknown whether the 366-day problem is
> fixed**, and a new defect loads the SWLIN code as the JCN identifier. Decision-log item 23 has
> the full list and the recommended order of attack.

## Verify before trusting (the [CONFIRM] list)
Items 1–4 were **confirmed against the live model on 2026-07-26** by a schema-dump reload; the real
field names are recorded here so this never has to be guessed again.
1. ~~**Actual-date field names.**~~ **CONFIRMED.** `AIM_CuPhase` exposes the friendly aliases
   **`Cu Phase Actual Start Date`** and **`Cu Phase Actual Completion Date`**. The
   `ACTUAL_*_DATE` raw names and the `..._EMPTY` flag fields **do not exist** in the published
   layer, so filter on the date fields directly rather than on empty-flags.
2. **`AIM_SWLIN` → CU-phase link on `%CuPhase_Key`: NOT CONFIRMED, and currently the main
   defect.** The join produces blanks for most CU phases, which starves every per-SWBS bin. Note
   the contrast: the candidate side maps SWBS fine from `JB_JCN SWLIN LI ID`, so SWLIN data exists
   at JCN grain. It is the CU-phase-keyed lookup that is not resolving. Diagnose this before
   anything else — the whole design premise is per-SWBS fits.
3. ~~**`%JobSumm_CuPhase_Key`**~~ **CONFIRMED** present on `AIM_CuPhase` and rolls a CU phase to its
   Job Summary. Related confirmed names: `CU_PHASE_SA_ID`, `MANHOUR_QY`, `Cu Phase Project ID`.
   The JCN bridge is `ALL_TABLES/JCN_CU_PHASE.qvd` on `CU_PHASE_SA_ID` / `JCN_SA_ID`.
4. ~~**Candidate source.**~~ **CONFIRMED.** `AIM_JB_JCN` exposes **`JB_JCN Est Man Days Qy`** and
   **`JB_JCN SWLIN LI ID`**; the JCN identifier is **`%JCN_Key`** (there is no `Job Control Number`
   field). `EST_MAN_DAYS_QY` / `SWLIN_LI_ID` are the dictionary names, not the app names.
   Still open: how to filter to "incoming / not-yet-done" (the run used only `> 0`, which scores
   the entire backlog rather than incoming work).
5. ~~**Window units.**~~ **RESOLVED 2026-07-26 (operator).** "96 hours" is **96 elapsed clock
   hours**, not work-shifts, so `v96Days = 4` calendar days is correct and no working-day
   conversion is needed. Span here is calendar days (ACC − ACS), which is the same clock, so
   history and threshold agree by construction. `vCMAVDays = 42` (6 weeks) likewise stays calendar.
   Still a local SRF definition, since "96 hours" is not in 4700.1F. **Caveat carried into the
   scoring step:** an elapsed clock runs through weekends, so a job near the four-day line passes
   or fails on its start day, which is unknown at induction. Prefer a margin below the threshold
   over a bare comparison. See "The unit definition, settled" in
   [early-jcn-screen](../02_synthesis/early-jcn-screen.md).

## The script

```qlik
// ===========================================================================
// WCP FIRST SCREEN — Span fit per SWBS (no COST/STARS join needed)
// Model: per SWBS, span_days ≈ Intercept + Slope × EstManDays, fit from
//        completed SINGLE-JCN history (clean standalone span).
// ===========================================================================

// ---------- Parameters ----------
SET vHomeport   = 'YOKOSUKA';
SET v96Days     = 4;     // CONFIRMED 2026-07-26: 96 ELAPSED clock hours = 4 calendar days
SET vCMAVDays   = 42;    // 6-week CMAV upper bound, calendar days
SET vMarginPct  = 1.25;  // marginal band = up to 1.25× the CMAV threshold
SET vMinN       = 8;     // min completed jobs to trust a SWBS's own fit; else shrink to parent

// ---------- 1. Scope: Yokosuka DDG/LCC, ALL availability types ----------
// No availability-type or completion filter here, on purpose - we want EVERY
// availability (CNO, CMAV, CM, EM, WOO). "Completed" is enforced at the CU-phase
// level below (certified flag + non-empty actual start/finish dates), which works
// the same regardless of availability type. Broaden the scope by relaxing the
// Match()/[Ship Home] below. (Optionally carry PROJECT_TYPE_CD if you later want to
// segment the fit by availability type.)
Ships_T:
LOAD %Proj_Ship_Key AS [%ShipKey]
FROM [lib://QVD-JRMC-AIM/AIM_Ship.qvd] (qvd)
WHERE [Ship Home]='$(vHomeport)' AND Match([Ship Type],'DDG','LCC');

CohortProjects:
LOAD [Project ID] AS PROJ_ID
FROM [lib://QVD-JRMC-AIM/AIM_Project.qvd] (qvd)
WHERE Exists([%ShipKey],[%Proj_Ship_Key]);
Map_Cohort: MAPPING LOAD PROJ_ID, 1 RESIDENT CohortProjects;

// ---------- 2. Certified (closed) CU phases ----------
Map_Certified:
MAPPING LOAD %CuPhase_Key, 1
FROM [lib://QVD-JRMC-AIM/AIM_CuPhase_Hist.qvd] (qvd)
WHERE [Approval Status CD]='CRT' AND [Current Flag Cd]='Y';

// ---------- 3. SWLIN line item per CU phase -> SWBS ----------
Map_SWLIN:
MAPPING LOAD %CuPhase_Key, [SWLIN Line Item]                        // [CONFIRM] link key
FROM [lib://QVD-JRMC-AIM/AIM_SWLIN.qvd] (qvd);

// ---------- 4. CU-phase facts: cohort + certified, with span ----------
CuPhase_T:
LOAD
    CU_PHASE_SA_ID,
    %JobSumm_CuPhase_Key                         AS JS_Key,
    MANHOUR_QY                                   AS Est_MH,        // estimate man-HOURS
    Num(ACTUAL_START_DATE)                        AS ACS,           // [CONFIRM name]
    Num(ACTUAL_COMPLETION_DATE)                   AS ACC,           // [CONFIRM name]
    Left( ApplyMap('Map_SWLIN', %CuPhase_Key, '') , 3) AS SWBS
FROM [lib://QVD-JRMC-AIM/AIM_CuPhase.qvd] (qvd)
WHERE ApplyMap('Map_Cohort',[Cu Phase Project ID],0)=1
  AND ApplyMap('Map_Certified',%CuPhase_Key,0)=1
  AND [Actual Start Date Empty]=0 AND [Actual Completion Date Empty]=0;  // [CONFIRM flag names]

// ---------- 5. JCN count per Job Summary (keep single-JCN summaries) ----------
JcnBridge:
LOAD CU_PHASE_SA_ID, JCN_SA_ID
FROM [lib://QVD-JRMC-AIM/ALL_TABLES/JCN_CU_PHASE.qvd] (qvd)
WHERE Exists(CU_PHASE_SA_ID, CU_PHASE_SA_ID);            // only CU phases we kept
LEFT JOIN (CuPhase_T) LOAD CU_PHASE_SA_ID, JCN_SA_ID RESIDENT JcnBridge;
DROP TABLE JcnBridge;

JS_Count:
LOAD JS_Key, Count(DISTINCT JCN_SA_ID) AS JCNsInJS
RESIDENT CuPhase_T GROUP BY JS_Key;
Map_JCNsInJS: MAPPING LOAD JS_Key, JCNsInJS RESIDENT JS_Count;
DROP TABLE JS_Count;

// ---------- 6. Roll up to the Job Summary: standalone span + estimate (single-JCN only) ----------
JS_History:
LOAD
    JS_Key,
    FirstSortedValue(SWBS, -Aggr(Count(CU_PHASE_SA_ID),SWBS,JS_Key)) AS SWBS,  // dominant SWBS [CONFIRM rule]
    (Max(ACC) - Min(ACS))                        AS Span_Days,       // standalone calendar span
    Sum(Est_MH)/8                                 AS Est_MD           // estimate man-DAYS
RESIDENT CuPhase_T
WHERE ApplyMap('Map_JCNsInJS', JS_Key, 99) = 1                       // single-JCN summaries only
GROUP BY JS_Key;

JS_Clean:
NOCONCATENATE LOAD * RESIDENT JS_History
WHERE Span_Days > 0 AND Est_MD > 0 AND Len(Trim(SWBS))=3;
DROP TABLE JS_History;

// ---------- 7. The per-SWBS span fit ----------
SWBS_Fit:
LOAD
    SWBS,
    Count(1)                       AS n,
    Median(Span_Days)              AS MedianSpan,
    LINEST_M(Span_Days, Est_MD)    AS Slope,        // days per man-day
    LINEST_B(Span_Days, Est_MD)    AS Intercept     // fixed-wait floor (days)
RESIDENT JS_Clean GROUP BY SWBS;

Parent_Fit:
LOAD
    Left(SWBS,1)                   AS SWBS1,
    Count(1)                       AS n1,
    LINEST_M(Span_Days, Est_MD)    AS Slope1,
    LINEST_B(Span_Days, Est_MD)    AS Intercept1
RESIDENT JS_Clean GROUP BY Left(SWBS,1);

Global_Fit:
LOAD LINEST_M(Span_Days, Est_MD) AS gS, LINEST_B(Span_Days, Est_MD) AS gI RESIDENT JS_Clean;
LET vgSlope = Peek('gS',0,'Global_Fit');
LET vgInt   = Peek('gI',0,'Global_Fit');
DROP TABLE Global_Fit;

// shrinkage maps: use a SWBS's own fit only if n>=vMinN, else null (Alt falls through)
Map_S:  MAPPING LOAD SWBS,  If(n  >= $(vMinN), Slope)     RESIDENT SWBS_Fit;
Map_I:  MAPPING LOAD SWBS,  If(n  >= $(vMinN), Intercept) RESIDENT SWBS_Fit;
Map_PS: MAPPING LOAD SWBS1, If(n1 >= $(vMinN), Slope1)    RESIDENT Parent_Fit;
Map_PI: MAPPING LOAD SWBS1, If(n1 >= $(vMinN), Intercept1)RESIDENT Parent_Fit;

// ---------- 8. Score candidate (incoming/open) JCNs ----------
// [CONFIRM] that AIM_JB_JCN holds the brokered estimate + SWLIN + JCN for open candidates,
// and add a filter that selects "incoming / not-yet-planned" JCNs.
Candidates:
LOAD
    [Job Control Number]            AS JCN,            // [CONFIRM field name]
    EST_MAN_DAYS_QY                 AS Est_MD,
    Left(SWLIN_LI_ID, 3)            AS SWBS
FROM [lib://QVD-JRMC-AIM/AIM_JB_JCN.qvd] (qvd)
WHERE EST_MAN_DAYS_QY > 0;                              // [CONFIRM open/active filter]

Scored:
LOAD *,
    RangeMax(0.5, Intercept_eff + Slope_eff * Est_MD) AS PredSpan_Days
;
LOAD
    JCN, SWBS, Est_MD,
    Alt(ApplyMap('Map_S', SWBS, Null()),  ApplyMap('Map_PS', Left(SWBS,1), Null()), $(vgSlope)) AS Slope_eff,
    Alt(ApplyMap('Map_I', SWBS, Null()),  ApplyMap('Map_PI', Left(SWBS,1), Null()), $(vgInt))   AS Intercept_eff
RESIDENT Candidates;
DROP TABLE Candidates;

// ---------- 9. The three-bin verdict ----------
Screen:
LOAD *,
    If(PredSpan_Days <= $(v96Days),                 'MAYBE - 96hr-capable',
      If(PredSpan_Days <= $(vCMAVDays),             'MAYBE - CMAV-capable',
        If(PredSpan_Days <= $(vCMAVDays)*$(vMarginPct), 'MARGINAL - verify at planning',
                                                    'MUST-DO - exceeds CMAV'))) AS Screen_Bin
RESIDENT Scored;
DROP TABLE Scored;

// NOTE: the structural DRYDOCK cut (DRYDOCK_FLAG_CD on AIM_Project, via the candidate's
// availability) should override to 'MUST-DO (drydock)'. Add it once the candidate->project
// link is confirmed.
```

## How to use it
- After reload, the **`SWBS_Fit`** table is your calibration: `n`, `MedianSpan`, `Slope`,
  `Intercept` per SWBS. Chart `Slope`/`Intercept` and eyeball a scatter of `Span_Days` vs `Est_MD`
  per SWBS first — if a group looks non-linear or wild, prefer its `MedianSpan` for now.
- The **`Screen`** table is the live screen: one row per candidate JCN with `PredSpan_Days` and
  `Screen_Bin`. Put `SWBS` and `Screen_Bin` on a chart, or list JCNs by bin.
- Sanity checks: a `Slope` near (1 ÷ typical crew) is reasonable; a negative `Intercept` or a
  near-zero `n` means that SWBS is thin — it's being shrunk to its parent, which is expected.

## Deliberately left for next steps
- **Drydock override** (one mapped flag) — the cleanest cut; add when the candidate→project link
  is confirmed.
- **The true labor multiplier** via the AIM↔COST/STARS join (`COST_FJ40` actual hours by Job Order)
  — to de-bias the estimate itself and to separate effort from calendar. Not needed for this first
  cut.
- **Splittability** (the third screen question) — needs the engineered steps, which don't exist
  until planning; provisional by work type only.

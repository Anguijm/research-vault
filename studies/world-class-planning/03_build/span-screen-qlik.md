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

## Verify before trusting (the [CONFIRM] list)
These are inferred from your data dictionary / dump; confirm against the live model:
1. **Actual-date field names** on `AIM_CuPhase`: dictionary shows `ACTUAL_START_DATE` /
   `ACTUAL_COMPLETION_DATE` (+ `..._EMPTY` flags); your field dump showed friendly aliases
   `Cu Phase Actual Start Date` / `...Completion Date`. Use whichever your app exposes.
2. **`AIM_SWLIN` → CU-phase link** on `%CuPhase_Key`, and that **`SWLIN Line Item` (`SWLIN_LI_ID`)
   first 3 digits = the SWBS group.** If the SWBS lives in a different slice of the SWLIN, change
   the `Left(...,3)`.
3. **`%JobSumm_CuPhase_Key`** rolls a CU phase to its Job Summary (it's on `AIM_CuPhase`).
4. **Candidate source** (Section 8): that `AIM_JB_JCN` holds `EST_MAN_DAYS_QY` + `SWLIN_LI_ID` +
   the Job Control Number for open/active JCNs, and how to filter to "incoming/not-yet-done."
5. **Window units:** span here is **calendar days** (ACC − ACS). `v96Days=4` and `vCMAVDays=42`
   assume 96 hours = 4 calendar days and a 6-week CMAV = 42 calendar days. Switch to working days
   if that's your convention. (And "96 hours" still isn't defined in 4700.1F — this is a placeholder.)

## The script

```qlik
// ===========================================================================
// WCP FIRST SCREEN — Span fit per SWBS (no COST/STARS join needed)
// Model: per SWBS, span_days ≈ Intercept + Slope × EstManDays, fit from
//        completed SINGLE-JCN history (clean standalone span).
// ===========================================================================

// ---------- Parameters ----------
SET vHomeport   = 'YOKOSUKA';
LET vToday      = Num(Today());
SET v96Days     = 4;     // [CONFIRM] "96 hours" as calendar days
SET vCMAVDays   = 42;    // 6-week CMAV upper bound, calendar days
SET vMarginPct  = 1.25;  // marginal band = up to 1.25× the CMAV threshold
SET vMinN       = 8;     // min completed jobs to trust a SWBS's own fit; else shrink to parent

// ---------- 1. Cohort: completed (Benchmark) CNO availabilities, Yokosuka DDG/LCC ----------
Map_CA00_Actual:
MAPPING LOAD [Event Proj ID], Num(Date([Event Actual Date]))
FROM [lib://QVD-JRMC-AIM/AIM_Key_Event_And_Milestones.qvd] (qvd)
WHERE [Event ID]='CA00' AND Len(Trim([Event Actual Date]))>0;

Ships_T:
LOAD %Proj_Ship_Key AS [%ShipKey]
FROM [lib://QVD-JRMC-AIM/AIM_Ship.qvd] (qvd)
WHERE [Ship Home]='$(vHomeport)' AND Match([Ship Type],'DDG','LCC');

CohortProjects:
LOAD [Project ID] AS PROJ_ID
FROM [lib://QVD-JRMC-AIM/AIM_Project.qvd] (qvd)
WHERE Exists([%ShipKey],[%Proj_Ship_Key])
  AND ApplyMap('Map_CA00_Actual',[Project ID],0) > 0               // has an actual completion
  AND ApplyMap('Map_CA00_Actual',[Project ID],0) <= $(vToday)      // and it's in the past = completed
  AND NOT WildMatch(Upper([Project Name]),'*CM*','*CMAV*','*EM*','*WOO*'); // CNO availabilities only
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

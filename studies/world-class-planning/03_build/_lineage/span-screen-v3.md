---
type: build-artifact
study: world-class-planning
title: Span screen v3 — three span definitions tested in one reload
classification: internal
created: 2026-07-27
supersedes: Latest Script (run 2, 2026-07-27)
---

# Span screen v3 — run this one

This is the script to try. It fixes everything decision-log items 22 and 23 turned up, and instead
of guessing which span definition is correct it **computes three of them side by side in a single
reload** and prints the numbers that tell you which one works. Every diagnostic uses `LET`, so they
will actually print this time.

## What changed from run 2

**The defects, fixed.** The JCN identifier is back to `%JCN_Key` rather than the SWLIN code. The
JCN-bridge join no longer fans out the CU-phase table, so `Sum(Est_MH)` stops over-counting; the
count is now derived through a lookup instead of a `LEFT JOIN`. Span is an inclusive day count
(`ACC − ACS + 1`), so a same-day job is one day rather than zero and is no longer deleted. Phases
that complete before they start are filtered explicitly. `FirstSortedValue` is gone, because it
returns null on ties, which may well have been eating Job Summaries silently; dominant SWBS is now
picked with a max-count join and an alphabetical tie-break.

**The three ideas being tested.** For every Job Summary the script computes:

| Name | Definition | The hypothesis it tests |
|------|-----------|--------------------------|
| `SpanEnv` | `Max(ACC) − Min(ACS) + 1` | The run-2 definition. The whole envelope from first phase start to last phase finish. |
| `SpanLong` | `Max(ACC − ACS + 1)` per phase | The longest single phase. If the envelope is inflated by planning phases sitting far from execution, this is the actual physical work window. |
| `SpanSum` | `Sum(ACC − ACS + 1)` | Total phase-days. What the job would take if its phases ran back to back with no waiting. |

If `SpanEnv` comes back around 366 days and `SpanLong` comes back around a week, that settles the
open method question immediately, and you should fit on `SpanLong`.

**Two model forms, also side by side.** Each span definition gets a linear fit
(`Intercept + Slope × EstManDays`) and a plain per-SWBS **median**. The harness always wanted a
look at whether the linear fit earns its keep. If the median predicts as well, use it, because it
cannot produce a negative intercept and it is far easier to explain to a planner.

**A SWBS reconciliation test.** The script derives the candidate SWBS **both** ways
(`JB_JCN SWLIN LI ID` and `SWLIN_SYS_ID`), and prints how many candidates match a trained SWBS bin
under each. This directly answers the item 23 risk that the two sides do not speak the same code.
Flip `vCandSWBSSrc` to whichever wins.

## How to read the output

Work down the TRACE block in this order and stop at the first thing that looks wrong.

1. `[dq]` — how much of the CU-phase data survived the date filter, and how many negative spans got
   dropped. If `kept` is a small fraction of `raw`, stop; the filter is too aggressive.
2. `[spans]` — **the number that matters.** Median of each of the three definitions. If the medians
   are 300-plus days, the interval is still wrong and no fit downstream is meaningful.
3. `[estbasis]` — median training estimate against median candidate estimate. These should be in
   the same ballpark. If training median is 2 and candidate median is 40, the model is being fit on
   one scale and applied to another, and every prediction is biased.
4. `[swbsmatch]` — how many of the candidates hit a trained bin under each derivation. If both are
   near zero, everything is falling through to the global fit and the per-SWBS design is not
   actually running.
5. `[fit]` — trusted bins and how many came out with a negative intercept or slope. Negative
   intercepts mean the linear form is misbehaving in that bin; prefer the median there.
6. `[bins-*]` — the three-bin verdict under each span definition. A usable screen is one where these
   are not all in a single bucket.

## The script

```qlik
// ===========================================================================
// WCP FIRST SCREEN v3
// Fits span ≈ f(estimated man-days) per SWBS, three span definitions at once,
// linear and median forms, with LET-based diagnostics that actually print.
// ===========================================================================

// ---------- Parameters ----------
SET vHomeport     = 'YOKOSUKA';
SET v96Days       = 4;     // 96 ELAPSED clock hours = 4 calendar days (confirmed 2026-07-26)
SET vCMAVDays     = 42;    // 6-week CMAV upper bound, calendar days
SET vMarginPct    = 1.25;  // marginal band = up to 1.25x the CMAV threshold
SET vMinN         = 8;     // min jobs before a SWBS's own fit is trusted
SET vHoursPerMD   = 8;     // man-hours per man-day  [CONFIRM against AIM convention]
SET vCandSWBSSrc  = 1;     // 1 = JB_JCN SWLIN LI ID, 2 = SWLIN_SYS_ID (see [swbsmatch])

// ---------- 1. Cohort: Yokosuka DDG/LCC, ALL availability types ----------
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

// ---------- 3. CU-phase facts ----------
CuPhase_Raw:
LOAD
    CU_PHASE_SA_ID,
    %JobSumm_CuPhase_Key                          AS JS_Key,
    MANHOUR_QY                                    AS Est_MH,
    Mid(ICN, 6, 3)                                AS SWBS,
    Num([Cu Phase Actual Start Date])             AS ACS,
    Num([Cu Phase Actual Completion Date])        AS ACC
FROM [lib://QVD-JRMC-AIM/AIM_CuPhase.qvd] (qvd)
WHERE ApplyMap('Map_Cohort',[Cu Phase Project ID],0)=1
  AND ApplyMap('Map_Certified',%CuPhase_Key,0)=1;

LET vRawCuP = NoOfRows('CuPhase_Raw');

CuPhase_T:
NOCONCATENATE LOAD
    CU_PHASE_SA_ID, JS_Key, Est_MH, SWBS, ACS, ACC,
    (ACC - ACS + 1)                               AS PhaseSpan   // INCLUSIVE: same-day = 1
RESIDENT CuPhase_Raw
WHERE IsNum(ACS) AND IsNum(ACC) AND ACS > 0 AND ACC > 0 AND ACC >= ACS;

DROP TABLE CuPhase_Raw;

// ---------- 4. JCNs per Job Summary — via lookup, NOT a join (no fan-out) ----------
Map_CuP_JS: MAPPING LOAD CU_PHASE_SA_ID, JS_Key RESIDENT CuPhase_T;

JS_JCN:
LOAD DISTINCT
    ApplyMap('Map_CuP_JS', CU_PHASE_SA_ID, '(none)') AS JS_Key,
    JCN_SA_ID
FROM [lib://QVD-JRMC-AIM/ALL_TABLES/JCN_CU_PHASE.qvd] (qvd)
WHERE Exists(CU_PHASE_SA_ID);

JS_Count:
LOAD JS_Key, Count(DISTINCT JCN_SA_ID) AS JCNsInJS
RESIDENT JS_JCN WHERE JS_Key <> '(none)' GROUP BY JS_Key;

Map_JCNsInJS: MAPPING LOAD JS_Key, JCNsInJS RESIDENT JS_Count;
DROP TABLE JS_JCN;

// ---------- 5. Dominant SWBS per Job Summary (no FirstSortedValue: it nulls on ties) ----------
JS_SWBS_Counts:
LOAD JS_Key, SWBS, Count(CU_PHASE_SA_ID) AS SWBS_Count
RESIDENT CuPhase_T GROUP BY JS_Key, SWBS;

JS_Best:
LOAD JS_Key, Max(SWBS_Count) AS BestCount
RESIDENT JS_SWBS_Counts GROUP BY JS_Key;

LEFT JOIN (JS_SWBS_Counts) LOAD JS_Key, BestCount RESIDENT JS_Best;
DROP TABLE JS_Best;

JS_Dom:
LOAD JS_Key, MinString(SWBS) AS Dominant_SWBS      // deterministic tie-break
RESIDENT JS_SWBS_Counts WHERE SWBS_Count = BestCount GROUP BY JS_Key;

Map_Dominant_SWBS: MAPPING LOAD JS_Key, Dominant_SWBS RESIDENT JS_Dom;
DROP TABLES JS_SWBS_Counts, JS_Dom;

// ---------- 6. Roll up to Job Summary: THREE span definitions ----------
JS_History:
LOAD
    JS_Key                                        AS T_JS,
    ApplyMap('Map_Dominant_SWBS', JS_Key, '')     AS T_SWBS,
    (Max(ACC) - Min(ACS) + 1)                     AS SpanEnv,    // A: full envelope
    Max(PhaseSpan)                                AS SpanLong,   // B: longest single phase
    Sum(PhaseSpan)                                AS SpanSum,    // C: phase-days summed
    Count(CU_PHASE_SA_ID)                         AS NPhases,
    Sum(Est_MH)/$(vHoursPerMD)                    AS T_EstMD
RESIDENT CuPhase_T
WHERE ApplyMap('Map_JCNsInJS', JS_Key, 99) = 1                   // single-JCN summaries only
GROUP BY JS_Key;

LET vNHist = NoOfRows('JS_History');

JS_Clean:
NOCONCATENATE LOAD *
RESIDENT JS_History
WHERE T_EstMD > 0 AND SpanEnv > 0 AND Len(Trim(T_SWBS)) = 3;

DROP TABLE JS_History;

// ---------- 7. Fits: per SWBS, per parent, global — for all three spans ----------
SWBS_Fit:
LOAD
    T_SWBS                          AS SWBS,
    Count(1)                        AS n,
    Median(SpanEnv)                 AS MedEnv,
    Median(SpanLong)                AS MedLong,
    Median(SpanSum)                 AS MedSum,
    LINEST_M(SpanEnv , T_EstMD)     AS mEnv,   LINEST_B(SpanEnv , T_EstMD) AS bEnv,
    LINEST_M(SpanLong, T_EstMD)     AS mLong,  LINEST_B(SpanLong, T_EstMD) AS bLong,
    LINEST_M(SpanSum , T_EstMD)     AS mSum,   LINEST_B(SpanSum , T_EstMD) AS bSum
RESIDENT JS_Clean GROUP BY T_SWBS;

Parent_Fit:
LOAD
    Left(T_SWBS,1)                  AS SWBS1,
    Count(1)                        AS n1,
    Median(SpanEnv)                 AS pMedEnv,
    Median(SpanLong)                AS pMedLong,
    Median(SpanSum)                 AS pMedSum,
    LINEST_M(SpanEnv , T_EstMD)     AS pmEnv,  LINEST_B(SpanEnv , T_EstMD) AS pbEnv,
    LINEST_M(SpanLong, T_EstMD)     AS pmLong, LINEST_B(SpanLong, T_EstMD) AS pbLong,
    LINEST_M(SpanSum , T_EstMD)     AS pmSum,  LINEST_B(SpanSum , T_EstMD) AS pbSum
RESIDENT JS_Clean GROUP BY Left(T_SWBS,1);

Global_Fit:
LOAD
    Median(SpanEnv)  AS gMedEnv,  Median(SpanLong) AS gMedLong, Median(SpanSum) AS gMedSum,
    LINEST_M(SpanEnv , T_EstMD) AS gmEnv,  LINEST_B(SpanEnv , T_EstMD) AS gbEnv,
    LINEST_M(SpanLong, T_EstMD) AS gmLong, LINEST_B(SpanLong, T_EstMD) AS gbLong,
    LINEST_M(SpanSum , T_EstMD) AS gmSum,  LINEST_B(SpanSum , T_EstMD) AS gbSum
RESIDENT JS_Clean;

LET vgMedEnv  = Alt(Peek('gMedEnv' ,0,'Global_Fit'), 1);
LET vgMedLong = Alt(Peek('gMedLong',0,'Global_Fit'), 1);
LET vgMedSum  = Alt(Peek('gMedSum' ,0,'Global_Fit'), 1);
LET vgmEnv    = Alt(Peek('gmEnv' ,0,'Global_Fit'), 0);  LET vgbEnv  = Alt(Peek('gbEnv' ,0,'Global_Fit'), 1);
LET vgmLong   = Alt(Peek('gmLong',0,'Global_Fit'), 0);  LET vgbLong = Alt(Peek('gbLong',0,'Global_Fit'), 1);
LET vgmSum    = Alt(Peek('gmSum' ,0,'Global_Fit'), 0);  LET vgbSum  = Alt(Peek('gbSum' ,0,'Global_Fit'), 1);

DROP TABLE Global_Fit;

// --- counts and fit sanity captured NOW, before the fit tables get joined away ---
LET vNFit = NoOfRows('SWBS_Fit');
LET vNPar = NoOfRows('Parent_Fit');

DIAG_Fit:
LOAD Count(1) AS Bins, Sum(If(n>=$(vMinN),1,0)) AS Trusted,
     Sum(If(bLong<0,1,0)) AS NegIntLong, Sum(If(mLong<0,1,0)) AS NegSlopeLong,
     Sum(If(bEnv <0,1,0)) AS NegIntEnv
RESIDENT SWBS_Fit;
LET vBins=Peek('Bins',0,'DIAG_Fit'); LET vTrust=Peek('Trusted',0,'DIAG_Fit');
LET vNIL=Peek('NegIntLong',0,'DIAG_Fit'); LET vNSL=Peek('NegSlopeLong',0,'DIAG_Fit');
LET vNIE=Peek('NegIntEnv',0,'DIAG_Fit');
DROP TABLE DIAG_Fit;

// ---------- 8. Candidates (both SWBS derivations, so we can compare) ----------
Cand_Raw:
LOAD
    %JCN_Key                        AS JCN,
    [JB_JCN Est Man Days Qy]        AS Est_MD,
    Left([JB_JCN SWLIN LI ID], 3)   AS SWBS_A,
    Left(SWLIN_SYS_ID, 3)           AS SWBS_B
FROM [lib://QVD-JRMC-AIM/AIM_JB_JCN.qvd] (qvd)
WHERE [JB_JCN Est Man Days Qy] > 0;                  // [CONFIRM] add an open/active filter

// how many candidates match a TRAINED bin under each derivation?
Cand_Match:
LOAD
    Count(1)                                    AS CandTot,
    Sum(If(Exists(T_SWBS, SWBS_A),1,0))         AS MatchA,
    Sum(If(Exists(T_SWBS, SWBS_B),1,0))         AS MatchB,
    Median(Est_MD)                              AS CandEstMed
RESIDENT Cand_Raw;

Candidates:
NOCONCATENATE LOAD
    JCN, Est_MD,
    If($(vCandSWBSSrc)=1, SWBS_A, SWBS_B)       AS SWBS,
    Left(If($(vCandSWBSSrc)=1, SWBS_A, SWBS_B),1) AS SWBS1
RESIDENT Cand_Raw;

DROP TABLE Cand_Raw;

// ---------- 9. Attach coefficients ----------
LEFT JOIN (Candidates)
LOAD SWBS, n, MedEnv, MedLong, MedSum, mEnv,bEnv, mLong,bLong, mSum,bSum RESIDENT SWBS_Fit;

LEFT JOIN (Candidates)
LOAD SWBS1, n1, pMedEnv, pMedLong, pMedSum, pmEnv,pbEnv, pmLong,pbLong, pmSum,pbSum RESIDENT Parent_Fit;

// drop the fit tables NOW: leaving them alongside Candidates (which just inherited
// SWBS, n, MedEnv, ...) would give Qlik multiple shared fields and a synthetic key.
DROP TABLES SWBS_Fit, Parent_Fit;

// ---------- 10. Predictions: 3 spans x (linear, median) ----------
Scored:
NOCONCATENATE LOAD
    JCN, SWBS, Est_MD, n, n1,
    RangeMax(0.5, Alt( If(n  >= $(vMinN), bEnv  + mEnv *Est_MD),
                       If(n1 >= $(vMinN), pbEnv + pmEnv*Est_MD),
                       $(vgbEnv)  + $(vgmEnv) *Est_MD))            AS Pred_Env,
    RangeMax(0.5, Alt( If(n  >= $(vMinN), bLong + mLong*Est_MD),
                       If(n1 >= $(vMinN), pbLong+ pmLong*Est_MD),
                       $(vgbLong) + $(vgmLong)*Est_MD))            AS Pred_Long,
    RangeMax(0.5, Alt( If(n  >= $(vMinN), bSum  + mSum *Est_MD),
                       If(n1 >= $(vMinN), pbSum + pmSum*Est_MD),
                       $(vgbSum)  + $(vgmSum) *Est_MD))            AS Pred_Sum,
    Alt( If(n>=$(vMinN), MedEnv ), If(n1>=$(vMinN), pMedEnv ), $(vgMedEnv) ) AS Pred_MedEnv,
    Alt( If(n>=$(vMinN), MedLong), If(n1>=$(vMinN), pMedLong), $(vgMedLong)) AS Pred_MedLong,
    If(n >= $(vMinN),'own SWBS', If(n1 >= $(vMinN),'parent','global'))       AS FitSource
RESIDENT Candidates;

DROP TABLE Candidates;

// ---------- 11. Three-bin verdicts, one per span definition ----------
Screen:
NOCONCATENATE LOAD *,
    If(Pred_Env  <= $(v96Days),'1 MAYBE 96hr', If(Pred_Env  <= $(vCMAVDays),'2 MAYBE CMAV',
      If(Pred_Env  <= $(vCMAVDays)*$(vMarginPct),'3 MARGINAL','4 MUST-DO')))  AS Bin_Env,
    If(Pred_Long <= $(v96Days),'1 MAYBE 96hr', If(Pred_Long <= $(vCMAVDays),'2 MAYBE CMAV',
      If(Pred_Long <= $(vCMAVDays)*$(vMarginPct),'3 MARGINAL','4 MUST-DO')))  AS Bin_Long,
    If(Pred_Sum  <= $(v96Days),'1 MAYBE 96hr', If(Pred_Sum  <= $(vCMAVDays),'2 MAYBE CMAV',
      If(Pred_Sum  <= $(vCMAVDays)*$(vMarginPct),'3 MARGINAL','4 MUST-DO')))  AS Bin_Sum
RESIDENT Scored;

DROP TABLE Scored;

// ===================== DIAGNOSTICS (all LET — these will print) =============
TRACE ================== WCP SCREEN v3 DIAGNOSTICS ==================;

LET vKeptCuP = NoOfRows('CuPhase_T');
LET vNClean  = NoOfRows('JS_Clean');
LET vNScreen = NoOfRows('Screen');
// note: vNFit / vNPar were captured back in section 7, before the fit tables were dropped
TRACE [counts] rawCuPhase=$(vRawCuP)  keptCuPhase=$(vKeptCuP)  singleJCNjobs=$(vNHist)  trainRows=$(vNClean)  swbsBins=$(vNFit)  parentBins=$(vNPar)  candidates=$(vNScreen);

LET vDropDQ = $(vRawCuP) - $(vKeptCuP);
LET vDropCl = $(vNHist)  - $(vNClean);
TRACE [dq] dropped by date/negative-span filter=$(vDropDQ)   dropped from history by est/SWBS filter=$(vDropCl);

// --- THE NUMBER THAT MATTERS: span distributions, all three definitions ---
DIAG_Spans:
LOAD
  Min(SpanEnv) AS EnvMin, Median(SpanEnv) AS EnvMed, Fractile(SpanEnv,0.9) AS EnvP90, Max(SpanEnv) AS EnvMax,
  Min(SpanLong) AS LngMin, Median(SpanLong) AS LngMed, Fractile(SpanLong,0.9) AS LngP90, Max(SpanLong) AS LngMax,
  Min(SpanSum) AS SumMin, Median(SpanSum) AS SumMed, Fractile(SpanSum,0.9) AS SumP90, Max(SpanSum) AS SumMax,
  Median(NPhases) AS PhMed, Median(T_EstMD) AS TrainEstMed
RESIDENT JS_Clean;

LET vEnvMin=Peek('EnvMin',0,'DIAG_Spans'); LET vEnvMed=Peek('EnvMed',0,'DIAG_Spans');
LET vEnvP90=Peek('EnvP90',0,'DIAG_Spans'); LET vEnvMax=Peek('EnvMax',0,'DIAG_Spans');
LET vLngMin=Peek('LngMin',0,'DIAG_Spans'); LET vLngMed=Peek('LngMed',0,'DIAG_Spans');
LET vLngP90=Peek('LngP90',0,'DIAG_Spans'); LET vLngMax=Peek('LngMax',0,'DIAG_Spans');
LET vSumMed=Peek('SumMed',0,'DIAG_Spans'); LET vSumP90=Peek('SumP90',0,'DIAG_Spans');
LET vPhMed =Peek('PhMed' ,0,'DIAG_Spans'); LET vTrEst =Peek('TrainEstMed',0,'DIAG_Spans');

TRACE [spans] ENVELOPE  min/med/p90/max = $(vEnvMin) / $(vEnvMed) / $(vEnvP90) / $(vEnvMax);
TRACE [spans] LONGEST   min/med/p90/max = $(vLngMin) / $(vLngMed) / $(vLngP90) / $(vLngMax);
TRACE [spans] SUMPHASE  med/p90         = $(vSumMed) / $(vSumP90);
TRACE [spans] median phases per job = $(vPhMed);

// --- estimate basis: are training and scoring on the same scale? ---
LET vCandTot=Peek('CandTot',0,'Cand_Match'); LET vMatchA=Peek('MatchA',0,'Cand_Match');
LET vMatchB=Peek('MatchB',0,'Cand_Match');   LET vCaEst =Peek('CandEstMed',0,'Cand_Match');
TRACE [estbasis] training median man-days=$(vTrEst)   candidate median man-days=$(vCaEst)  <-- should be comparable;
TRACE [swbsmatch] of $(vCandTot) candidates: match via JB_JCN SWLIN LI ID=$(vMatchA)   via SWLIN_SYS_ID=$(vMatchB)  <-- set vCandSWBSSrc to the winner;

// --- fit sanity (variables were captured back in section 7, before the joins) ---
TRACE [fit] bins=$(vBins)  trusted(n>=$(vMinN))=$(vTrust)  negIntercept env=$(vNIE) long=$(vNIL)  negSlope long=$(vNSL);

// --- where did candidates get their coefficients from? ---
DIAG_Src:
LOAD FitSource, Count(1) AS Cnt RESIDENT Screen GROUP BY FitSource;
FOR i = 0 TO NoOfRows('DIAG_Src')-1
  LET vS = Peek('FitSource', $(i), 'DIAG_Src'); LET vC = Peek('Cnt', $(i), 'DIAG_Src');
  TRACE [fitsource] $(vS) = $(vC);
NEXT i

// --- the verdict distributions, one per span definition ---
DIAG_BinEnv:  LOAD Bin_Env  AS B, Count(1) AS C RESIDENT Screen GROUP BY Bin_Env;
FOR i = 0 TO NoOfRows('DIAG_BinEnv')-1
  LET vB=Peek('B',$(i),'DIAG_BinEnv'); LET vC=Peek('C',$(i),'DIAG_BinEnv');
  TRACE [bins-ENVELOPE] $(vB) = $(vC);
NEXT i

DIAG_BinLong: LOAD Bin_Long AS B, Count(1) AS C RESIDENT Screen GROUP BY Bin_Long;
FOR i = 0 TO NoOfRows('DIAG_BinLong')-1
  LET vB=Peek('B',$(i),'DIAG_BinLong'); LET vC=Peek('C',$(i),'DIAG_BinLong');
  TRACE [bins-LONGEST] $(vB) = $(vC);
NEXT i

DIAG_BinSum:  LOAD Bin_Sum  AS B, Count(1) AS C RESIDENT Screen GROUP BY Bin_Sum;
FOR i = 0 TO NoOfRows('DIAG_BinSum')-1
  LET vB=Peek('B',$(i),'DIAG_BinSum'); LET vC=Peek('C',$(i),'DIAG_BinSum');
  TRACE [bins-SUMPHASE] $(vB) = $(vC);
NEXT i

TRACE ================== END DIAGNOSTICS ==================;

// ---------- Cleanup ----------
FOR EACH vT in 'DIAG_Spans','DIAG_Src','DIAG_BinEnv','DIAG_BinLong','DIAG_BinSum',
               'Cand_Match','JS_Clean','CuPhase_T','Ships_T','CohortProjects','JS_Count'
  IF Not IsNull(TableNumber('$(vT)')) THEN
    DROP TABLE [$(vT)];
  END IF
NEXT vT
```

## If it still comes out flat

Two fallbacks, in order.

**If all three span medians are large**, the problem is upstream of the span definition: the CU
phases attached to a Job Summary are not what we think they are. Add `CU_WORK_CAT_CD` and
`WORK_TYPE_CD` to `CuPhase_T`, group the span diagnostic by them, and find out which phase
categories are stretching the envelope. The AIM-NG chapters distinguish planning from execution
phases, so there should be a code that separates them.

**If `[swbsmatch]` shows near-zero matches under both derivations**, stop working on the model and
reconcile the codes. Load the distinct trained SWBS values and the distinct candidate values into
two tables and eyeball them side by side. If training is producing three characters off `ICN`
positions 6 to 8 and the candidates are producing something structurally different, one of the two
is not a SWBS.

## Known limitations, deliberately left in

The training estimate is still `MANHOUR_QY / 8` while scoring uses the JCN induction estimate. The
`[estbasis]` line will now show you how bad that mismatch is; fixing it properly means joining
history JCNs to their Class F estimate, which is a larger change and an operator decision (see the
open questions in `_decisions.md`). The candidate filter is still only `Est Man Days Qy > 0`, so
this scores the whole backlog rather than incoming work.

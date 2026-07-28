---
type: build-artifact
study: world-class-planning
title: Granularity test — how granular does work type need to be, and is the regression earning its keep?
classification: internal
created: 2026-07-28
---

# Granularity test — the first honest accuracy measurement

**In plain terms.** Until now nobody has checked whether these predictions are any good. This script
does that. It learns from half your finished jobs, then predicts the other half and counts how often
it put the job in the right pile. It repeats that at every level of work-type detail, from very
coarse to the full SWLIN, and it does it twice, once using a simple typical-value lookup and once
using the regression. When it finishes you will know two things you do not know now: how granular
the work type needs to be, and whether the regression is doing anything a plain median could not.

## The standard being used

A prediction **passes** if it puts the job in the same pile as its real duration **or a longer
one**. It **fails** if it puts the job in a shorter pile than it belonged in, because that is the
error that lets work overrun the window it was screened into. Predicting four weeks for a job that
took four days is safe but wasteful; predicting four days for a job that took four weeks is the one
that hurts. The script reports all three outcomes separately so the cost of being conservative is
visible:

- **optimistic** — predicted a shorter pile than reality. This is the failure rate. Drive it down.
- **exact** — same pile.
- **conservative** — predicted a longer pile. Safe, but wastes capacity by pushing work into the
  must-do list that could have been absorbed elsewhere.

## Why it splits the data

Fitting and testing on the same jobs would flatter the model, because each job helps set the very
median it is then judged against. So jobs are split into two halves by alternating row, the model
learns only from the first half, and every number reported comes from predicting the second half,
which the model has never seen. Alternating rows also keeps the two halves balanced across work
types rather than splitting them by date or by ship.

## What the granularity sweep does

The work-type code is the SWLIN identifier. Today the screen truncates it to three characters. The
script re-runs the whole fit-and-test cycle using one character, then two, then three, and so on up
to eight, which is past the full length so the last few levels are the complete code. At each level
it reports the failure rate, how many bins exist, and how many test jobs actually landed in a bin
with enough history to be trusted rather than falling back to a global average.

**That last column is the trap to watch.** Failure rate will tend to improve as bins get finer right
up until the bins get too small to be trusted, at which point most jobs quietly fall back to the
global fit and the apparent improvement is meaningless. Read the two columns together.

```qlik
// ===========================================================================
// GRANULARITY TEST — split-half accuracy of the span screen, by work-type detail
// Learns on fold A, scores fold B, never both.
// ===========================================================================

SET vHomeport      = 'YOKOSUKA';
SET v96Days        = 4;
SET vCMAVDays      = 42;
SET vMarginTop     = 52.5;    // 42 * 1.25
SET vMinN          = 8;
SET vHoursPerMD    = 8;
SET vNonProdMH     = 8;       // paperwork rule, same as v4
SET vNonProdSpan   = 60;
SET vMaxLevel      = 8;       // sweep Left(SWLIN,1) .. Left(SWLIN,8)

// ---------- Data prep (identical to v4) ----------
Ships_T:
LOAD %Proj_Ship_Key AS [%ShipKey]
FROM [lib://QVD-JRMC-AIM/AIM_Ship.qvd] (qvd)
WHERE [Ship Home]='$(vHomeport)' AND Match([Ship Type],'DDG','LCC');

CohortProjects:
LOAD [Project ID] AS PROJ_ID
FROM [lib://QVD-JRMC-AIM/AIM_Project.qvd] (qvd)
WHERE Exists([%ShipKey],[%Proj_Ship_Key]);
Map_Cohort: MAPPING LOAD PROJ_ID, 1 RESIDENT CohortProjects;

Map_Certified:
MAPPING LOAD %CuPhase_Key, 1
FROM [lib://QVD-JRMC-AIM/AIM_CuPhase_Hist.qvd] (qvd)
WHERE [Approval Status CD]='CRT' AND [Current Flag Cd]='Y';

CuPhase_Raw:
LOAD
    CU_PHASE_SA_ID, ICN, KO,
    MANHOUR_QY                                 AS Est_MH,
    CU_swlin_sys_id                            AS SWLINfull,     // FULL code, not truncated
    Num([Cu Phase Actual Start Date])          AS ACS,
    Num([Cu Phase Actual Completion Date])     AS ACC
FROM [lib://QVD-JRMC-AIM/AIM_CuPhase.qvd] (qvd)
WHERE ApplyMap('Map_Cohort',[Cu Phase Project ID],0)=1
  AND ApplyMap('Map_Certified',%CuPhase_Key,0)=1;

CuPhase_T:
NOCONCATENATE LOAD *, (ACC - ACS + 1) AS PhaseSpan
RESIDENT CuPhase_Raw
WHERE IsNum(ACS) AND IsNum(ACC) AND ACS>0 AND ACC>0 AND ACC>=ACS;
DROP TABLE CuPhase_Raw;

// paperwork detection, from the data
KO_Stats:
LOAD KO, Median(Est_MH) AS koMH, Median(PhaseSpan) AS koSpan
RESIDENT CuPhase_T GROUP BY KO;
Map_NonProd:
MAPPING LOAD KO, If(koMH <= $(vNonProdMH) AND koSpan >= $(vNonProdSpan),1,0) RESIDENT KO_Stats;
DROP TABLE KO_Stats;

// how long is a SWLIN, anyway?
DIAG_Len: LOAD Min(Len(SWLINfull)) AS L1, Median(Len(SWLINfull)) AS L2, Max(Len(SWLINfull)) AS L3
RESIDENT CuPhase_T;
LET vL1=Peek('L1',0,'DIAG_Len'); LET vL2=Peek('L2',0,'DIAG_Len'); LET vL3=Peek('L3',0,'DIAG_Len');
DROP TABLE DIAG_Len;

// ---------- Roll up to the job ----------
ICN_Hist:
LOAD
    ICN                                                            AS T_ICN,
    (Max(If(ApplyMap('Map_NonProd',KO,0)=0, ACC))
       - Min(If(ApplyMap('Map_NonProd',KO,0)=0, ACS)) + 1)         AS SpanProd,
    Sum(If(ApplyMap('Map_NonProd',KO,0)=0, Est_MH))/$(vHoursPerMD) AS T_EstMD,
    Sum(If(ApplyMap('Map_NonProd',KO,0)=0, 1))                     AS NProd
RESIDENT CuPhase_T GROUP BY ICN;

// dominant full SWLIN per job
ICN_SW: LOAD ICN, SWLINfull, Count(1) AS c RESIDENT CuPhase_T GROUP BY ICN, SWLINfull;
ICN_Bst: LOAD ICN, Max(c) AS bc RESIDENT ICN_SW GROUP BY ICN;
LEFT JOIN (ICN_SW) LOAD ICN, bc RESIDENT ICN_Bst;
DROP TABLE ICN_Bst;
ICN_Dom: LOAD ICN, MinString(SWLINfull) AS domSW RESIDENT ICN_SW WHERE c = bc GROUP BY ICN;
Map_DomSW: MAPPING LOAD ICN, domSW RESIDENT ICN_Dom;
DROP TABLES ICN_SW, ICN_Dom;

DROP TABLE CuPhase_T;

// ---------- Fold assignment: alternate rows, so folds stay balanced by work type ----------
Jobs:
NOCONCATENATE LOAD
    T_ICN,
    ApplyMap('Map_DomSW', T_ICN, '')   AS SW,
    SpanProd, T_EstMD,
    If(SpanProd <= $(v96Days),1,
      If(SpanProd <= $(vCMAVDays),2,
        If(SpanProd <= $(vMarginTop),3,4)))            AS ActualBin,
    Mod(RecNo(),2)                                     AS Fold
RESIDENT ICN_Hist
WHERE NProd > 0 AND T_EstMD > 0 AND SpanProd > 0;
DROP TABLE ICN_Hist;

LET vNJobs = NoOfRows('Jobs');

DIAG_Fold: LOAD Sum(If(Fold=0,1,0)) AS A, Sum(If(Fold=1,1,0)) AS B,
                Median(SpanProd) AS M, Fractile(SpanProd,0.9) AS P9 RESIDENT Jobs;
LET vFA=Peek('A',0,'DIAG_Fold'); LET vFB=Peek('B',0,'DIAG_Fold');
LET vMed=Peek('M',0,'DIAG_Fold'); LET vP90=Peek('P9',0,'DIAG_Fold');
DROP TABLE DIAG_Fold;

// global fallback learned from fold A only
DIAG_G: LOAD Median(SpanProd) AS gM, LINEST_M(SpanProd,T_EstMD) AS gS, LINEST_B(SpanProd,T_EstMD) AS gI
RESIDENT Jobs WHERE Fold=0;
LET vgM=Alt(Peek('gM',0,'DIAG_G'),1); LET vgS=Alt(Peek('gS',0,'DIAG_G'),0); LET vgI=Alt(Peek('gI',0,'DIAG_G'),1);
DROP TABLE DIAG_G;

TRACE ============== GRANULARITY TEST ==============;
TRACE [data] jobs=$(vNJobs)  foldA=$(vFA) foldB=$(vFB)  median production span=$(vMed)  p90=$(vP90);
TRACE [data] SWLIN length min/median/max = $(vL1)/$(vL2)/$(vL3);
TRACE [key] optimistic = predicted a SHORTER pile than reality = the failure that matters;
TRACE [sweep] level | bins | testJobs | ownBin% | MEDIAN: optimistic% exact% cons% | REGRESSION: optimistic% exact% cons%;

// ---------- The sweep ----------
FOR vLev = 1 TO $(vMaxLevel)

  FitL:
  LOAD
      Left(SW,$(vLev))              AS BK,
      Count(1)                      AS BN,
      Median(SpanProd)              AS BMed,
      LINEST_M(SpanProd,T_EstMD)    AS BS,
      LINEST_B(SpanProd,T_EstMD)    AS BI
  RESIDENT Jobs WHERE Fold=0 GROUP BY Left(SW,$(vLev));

  Map_Med: MAPPING LOAD BK, If(BN>=$(vMinN), BMed) RESIDENT FitL;
  Map_S:   MAPPING LOAD BK, If(BN>=$(vMinN), BS)   RESIDENT FitL;
  Map_I:   MAPPING LOAD BK, If(BN>=$(vMinN), BI)   RESIDENT FitL;
  Map_N:   MAPPING LOAD BK, BN                     RESIDENT FitL;
  LET vBins = NoOfRows('FitL');
  DROP TABLE FitL;

  EvalL:
  LOAD *,
      If(PredMed  <= $(v96Days),1, If(PredMed  <= $(vCMAVDays),2,
        If(PredMed  <= $(vMarginTop),3,4)))                       AS BinMed,
      If(PredReg  <= $(v96Days),1, If(PredReg  <= $(vCMAVDays),2,
        If(PredReg  <= $(vMarginTop),3,4)))                       AS BinReg
  ;
  LOAD
      ActualBin,
      If(ApplyMap('Map_N', Left(SW,$(vLev)), 0) >= $(vMinN),1,0)  AS OwnBin,
      Alt(ApplyMap('Map_Med', Left(SW,$(vLev)), Null()), $(vgM))  AS PredMed,
      RangeMax(0.5,
        Alt(ApplyMap('Map_I', Left(SW,$(vLev)), Null())
              + ApplyMap('Map_S', Left(SW,$(vLev)), Null())*T_EstMD,
            $(vgI) + $(vgS)*T_EstMD))                             AS PredReg
  RESIDENT Jobs WHERE Fold=1;

  SumL:
  LOAD
      Count(1)                                        AS T,
      Sum(OwnBin)                                     AS Own,
      Sum(If(BinMed < ActualBin,1,0))                 AS MOpt,
      Sum(If(BinMed = ActualBin,1,0))                 AS MExa,
      Sum(If(BinMed > ActualBin,1,0))                 AS MCon,
      Sum(If(BinReg < ActualBin,1,0))                 AS ROpt,
      Sum(If(BinReg = ActualBin,1,0))                 AS RExa,
      Sum(If(BinReg > ActualBin,1,0))                 AS RCon
  RESIDENT EvalL;

  LET vT=Peek('T',0,'SumL');  LET vOwn=Peek('Own',0,'SumL');
  LET vMO=Round(100*Peek('MOpt',0,'SumL')/$(vT),0.1); LET vME=Round(100*Peek('MExa',0,'SumL')/$(vT),0.1);
  LET vMC=Round(100*Peek('MCon',0,'SumL')/$(vT),0.1);
  LET vRO=Round(100*Peek('ROpt',0,'SumL')/$(vT),0.1); LET vRE=Round(100*Peek('RExa',0,'SumL')/$(vT),0.1);
  LET vRC=Round(100*Peek('RCon',0,'SumL')/$(vT),0.1);
  LET vOwnP=Round(100*$(vOwn)/$(vT),0.1);

  TRACE [sweep] $(vLev) | $(vBins) | $(vT) | $(vOwnP)% | MED: $(vMO)% $(vME)% $(vMC)% | REG: $(vRO)% $(vRE)% $(vRC)%;

  DROP TABLES EvalL, SumL;
NEXT vLev

TRACE ============== END ==============;

FOR EACH vT in 'Jobs','Ships_T','CohortProjects'
  IF Not IsNull(TableNumber('$(vT)')) THEN
    DROP TABLE [$(vT)];
  END IF
NEXT vT
```

## How to read the result

Look down the `optimistic%` column for whichever predictor is better and find where it stops
improving. That level is your granularity, and there is no need to go finer.

**Read `ownBin%` alongside it.** If the failure rate keeps dropping while `ownBin%` collapses toward
zero, the improvement is fake: the bins have gotten so small that almost every test job is being
scored by the global average, and you are measuring the global average, not the granularity.

**Compare `MED` against `REG`.** These are the two predictors at the same granularity. If the plain
median matches or beats the regression, the regression is not earning its keep and the screen should
be a lookup table, which is simpler to build, simpler to explain to a planner, and cannot produce a
negative prediction. Given that estimated man-days correlated only 0.22 with predicted span in the
last run, I would not be surprised if the median wins.

**Watch the conservative column too.** A model that never fails optimistically by calling everything
must-do is useless in a different way. If `optimistic%` is low but `cons%` is very high, the screen
is protecting the schedule by refusing to defer anything, which defeats the purpose.

## What this does not test

It only varies work-type granularity. It does not test the other dimensions worth trying, material
cost, work centre, casualty-report status, or availability type. Those need job attributes attached
to the history, which currently fails because the job-control-number lookup returns blank. If the
sweep shows granularity is not the answer, that is the next thing to fix, and it is the more likely
outcome given how much span varies inside a single work type.

It also inherits every open assumption from v4: the 8-hour man-day, and the mismatch between the
phase-level man-hours used to train and the job-level estimate used to score.

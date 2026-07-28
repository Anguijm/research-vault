---
type: build-artifact
study: world-class-planning
title: Span screen v4 — production-only spans, paperwork phases excluded
classification: internal
created: 2026-07-28
supersedes: span-screen-v3.md
---

# Span screen v4 — the one that should give real answers

**In plain terms.** Every job is made of steps. Some steps are paperwork: they open the day the job
is created, sit there for about a year, and carry almost no labour. Earlier versions measured a job
from its first step opening to its last step closing, so for three quarters of jobs they were
measuring paperwork rather than work. This version throws the paperwork steps out and measures only
the steps that carry real labour. It also reports how much of the remaining time is the job sitting
idle between steps, because that turned out to be about half of it.

## What changed from v3

**Paperwork steps are excluded, and the script works out which ones they are by itself.** No
hard-coded list of codes. It profiles every key operation in your own history and marks one as
non-production when its typical labour is at or below 8 man-hours *and* its typical duration is 60
days or more. In the last run that rule catches `S01`, `P01`, `S02`, `S03` and the rest of the S, P
and M families, which is 128,229 of 528,123 steps. The rule maintains itself as codes change, and
the script prints exactly which codes it excluded so you can sanity-check it.

**Jobs are grouped by ICN.** The diagnostic showed ICN and Job Summary are one-to-one, 28,478 of
each, so this is the same grouping as before but named the way you think about it.

**The estimate now comes from production steps only**, for the same reason as the span. Paperwork
steps contributed man-hours to the size estimate while contributing nothing to the work.

**Sum-of-phase-days is gone.** It put 88% of the backlog in must-do and predicted up to 5,222 days.
It double-counted steps that overlap in time. Not worth carrying further.

**The SWBS check is gone.** The two derivations agreed on all 528,123 steps, so that question is
closed. This version uses the SWLIN identifier on the phase.

**New: idle time.** For every job the script reports the production window, the total time the
individual steps were actually open, and the difference. That difference is waiting. In the last
run the individual steps ran 4 to 22 days while the whole production window ran about 50, so this
is worth measuring properly.

**New: an identifier probe.** The attempt to attach real job control numbers failed last run, every
lookup came back blank. Rather than guess again, the script prints sample values from both tables so
you can see what the keys actually look like.

```qlik
// ===========================================================================
// WCP SPAN SCREEN v4 — production-only span per ICN
// Paperwork phases identified from the data, not from a hard-coded list.
// ===========================================================================

// ---------- Parameters ----------
SET vHomeport      = 'YOKOSUKA';
SET v96Days        = 4;      // 96 ELAPSED clock hours = 4 calendar days
SET vCMAVDays      = 42;     // 6-week CMAV upper bound
SET vMarginPct     = 1.25;   // marginal band
SET vMinN          = 8;      // min jobs before a SWBS's own fit is trusted
SET vHoursPerMD    = 8;      // man-hours per man-day  [still unconfirmed]
SET vNonProdMH     = 8;      // a KO is NON-production if its median man-hours <= this ...
SET vNonProdSpan   = 60;     // ... AND its median span in days >= this

// ---------- 1. Cohort ----------
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

// ---------- 2. CU-phase facts ----------
CuPhase_Raw:
LOAD
    CU_PHASE_SA_ID,
    ICN,
    KO,
    MANHOUR_QY                                 AS Est_MH,
    Left(CU_swlin_sys_id,3)                    AS SWBS,
    Num([Cu Phase Actual Start Date])          AS ACS,
    Num([Cu Phase Actual Completion Date])     AS ACC
FROM [lib://QVD-JRMC-AIM/AIM_CuPhase.qvd] (qvd)
WHERE ApplyMap('Map_Cohort',[Cu Phase Project ID],0)=1
  AND ApplyMap('Map_Certified',%CuPhase_Key,0)=1;

LET vRaw = NoOfRows('CuPhase_Raw');

CuPhase_T:
NOCONCATENATE LOAD *,
    (ACC - ACS + 1)                            AS PhaseSpan
RESIDENT CuPhase_Raw
WHERE IsNum(ACS) AND IsNum(ACC) AND ACS>0 AND ACC>0 AND ACC>=ACS;
DROP TABLE CuPhase_Raw;
LET vKept = NoOfRows('CuPhase_T');

// ---------- 3. WORK OUT WHICH KEY OPERATIONS ARE PAPERWORK ----------
// A KO is non-production when it carries almost no labour AND runs a long time.
KO_Stats:
LOAD
    KO,
    Count(1)            AS koPhases,
    Median(Est_MH)      AS koMH,
    Median(PhaseSpan)   AS koSpan
RESIDENT CuPhase_T GROUP BY KO;

Map_NonProd:
MAPPING LOAD KO,
    If(koMH <= $(vNonProdMH) AND koSpan >= $(vNonProdSpan), 1, 0)
RESIDENT KO_Stats;

// ---------- 4. Roll up to the job (ICN) ----------
// IsProd flag is applied inside the aggregations.
ICN_Hist:
LOAD
    ICN                                                            AS T_ICN,
    // all phases (the old, broken definition — kept as a control)
    (Max(ACC) - Min(ACS) + 1)                                      AS SpanAll,
    // production only
    (Max(If(ApplyMap('Map_NonProd',KO,0)=0, ACC))
       - Min(If(ApplyMap('Map_NonProd',KO,0)=0, ACS)) + 1)         AS SpanProd,
    Max(If(ApplyMap('Map_NonProd',KO,0)=0, PhaseSpan))             AS SpanLongestProd,
    Sum(If(ApplyMap('Map_NonProd',KO,0)=0, PhaseSpan))             AS StepDaysProd,
    Sum(If(ApplyMap('Map_NonProd',KO,0)=0, Est_MH))/$(vHoursPerMD) AS T_EstMD,
    Sum(If(ApplyMap('Map_NonProd',KO,0)=0, 1))                     AS NProdPhases,
    Count(1)                                                       AS NPhases
RESIDENT CuPhase_T GROUP BY ICN;

LET vNICN = NoOfRows('ICN_Hist');

// dominant SWBS per ICN (Only() returns null when an ICN mixes SWBS values)
ICN_SWBS_Counts:
LOAD ICN, SWBS, Count(1) AS c RESIDENT CuPhase_T GROUP BY ICN, SWBS;
ICN_Best: LOAD ICN, Max(c) AS bestc RESIDENT ICN_SWBS_Counts GROUP BY ICN;
LEFT JOIN (ICN_SWBS_Counts) LOAD ICN, bestc RESIDENT ICN_Best;
DROP TABLE ICN_Best;
ICN_Dom: LOAD ICN, MinString(SWBS) AS domSWBS RESIDENT ICN_SWBS_Counts WHERE c = bestc GROUP BY ICN;
Map_DomSWBS: MAPPING LOAD ICN, domSWBS RESIDENT ICN_Dom;
DROP TABLES ICN_SWBS_Counts, ICN_Dom;

// ---------- 5. How many JCNs does an ICN carry? (bridge via lookup, no join) ----------
Map_CuP_ICN: MAPPING LOAD CU_PHASE_SA_ID, ICN RESIDENT CuPhase_T;

ICN_JCN:
LOAD DISTINCT
    ApplyMap('Map_CuP_ICN', CU_PHASE_SA_ID, '(none)') AS bICN,
    JCN_SA_ID
FROM [lib://QVD-JRMC-AIM/ALL_TABLES/JCN_CU_PHASE.qvd] (qvd);

ICN_JCNCount:
LOAD bICN, Count(DISTINCT JCN_SA_ID) AS JCNsInICN
RESIDENT ICN_JCN WHERE bICN <> '(none)' GROUP BY bICN;
Map_JCNsInICN: MAPPING LOAD bICN, JCNsInICN RESIDENT ICN_JCNCount;
DROP TABLE ICN_JCN;

// ---------- 6. Clean training set ----------
Train:
NOCONCATENATE LOAD
    T_ICN,
    ApplyMap('Map_DomSWBS', T_ICN, '')            AS T_SWBS,
    SpanAll, SpanProd, SpanLongestProd,
    StepDaysProd,
    RangeMax(0, SpanProd - StepDaysProd)          AS IdleDays,
    T_EstMD, NProdPhases, NPhases,
    ApplyMap('Map_JCNsInICN', T_ICN, 99)          AS JCNsInICN
RESIDENT ICN_Hist
WHERE NProdPhases > 0 AND T_EstMD > 0 AND SpanProd > 0;

DROP TABLE ICN_Hist;

// Separate the two reasons a job is excluded, so the reload log says which.
// Bundling is not random: a large structural job is likelier to be packaged
// with other JCNs into one ICN than a small inspection is, so a high bundle
// rate means training is biased toward simple work.
DIAG_Drop:
LOAD Count(1)                                        AS Tot,
     Sum(If(Len(Trim(T_SWBS))<>3,1,0))               AS NoSWBS,
     Sum(If(JCNsInICN > 1 AND JCNsInICN < 99,1,0))   AS Bundled,
     Sum(If(JCNsInICN = 99,1,0))                     AS NoBridge,
     Sum(If(JCNsInICN > 1 AND JCNsInICN < 99, JCNsInICN, 0)) AS JcnsInBundles
RESIDENT Train;
LET vDTot=Peek('Tot',0,'DIAG_Drop');   LET vDNoSW=Peek('NoSWBS',0,'DIAG_Drop');
LET vDBund=Peek('Bundled',0,'DIAG_Drop'); LET vDNoBr=Peek('NoBridge',0,'DIAG_Drop');
LET vDJcns=Peek('JcnsInBundles',0,'DIAG_Drop');
DROP TABLE DIAG_Drop;

Train_Clean:
NOCONCATENATE LOAD * RESIDENT Train
WHERE Len(Trim(T_SWBS)) = 3 AND JCNsInICN = 1;      // single-JCN jobs only
LET vTrainAll = NoOfRows('Train');
DROP TABLE Train;
LET vTrain = NoOfRows('Train_Clean');

// ---------- 7. Fit per SWBS: production envelope is PRIMARY ----------
SWBS_Fit:
LOAD
    T_SWBS                             AS SWBS,
    Count(1)                           AS n,
    Median(SpanProd)                   AS MedProd,
    Median(SpanLongestProd)            AS MedLong,
    Median(IdleDays)                   AS MedIdle,
    LINEST_M(SpanProd, T_EstMD)        AS mProd, LINEST_B(SpanProd, T_EstMD) AS bProd
RESIDENT Train_Clean GROUP BY T_SWBS;

Parent_Fit:
LOAD
    Left(T_SWBS,1)                     AS SWBS1,
    Count(1)                           AS n1,
    Median(SpanProd)                   AS pMedProd,
    Median(SpanLongestProd)            AS pMedLong,
    LINEST_M(SpanProd, T_EstMD)        AS pmProd, LINEST_B(SpanProd, T_EstMD) AS pbProd
RESIDENT Train_Clean GROUP BY Left(T_SWBS,1);

Global_Fit:
LOAD Median(SpanProd) AS gMedProd, Median(SpanLongestProd) AS gMedLong,
     LINEST_M(SpanProd, T_EstMD) AS gm, LINEST_B(SpanProd, T_EstMD) AS gb
RESIDENT Train_Clean;
LET vgMedProd = Alt(Peek('gMedProd',0,'Global_Fit'), 1);
LET vgMedLong = Alt(Peek('gMedLong',0,'Global_Fit'), 1);
LET vgm = Alt(Peek('gm',0,'Global_Fit'), 0);
LET vgb = Alt(Peek('gb',0,'Global_Fit'), 1);
DROP TABLE Global_Fit;

LET vNFit = NoOfRows('SWBS_Fit');
LET vNPar = NoOfRows('Parent_Fit');
DIAG_Fit:
LOAD Count(1) AS Bins, Sum(If(n>=$(vMinN),1,0)) AS Trusted,
     Sum(If(bProd<0,1,0)) AS NegInt, Sum(If(mProd<0,1,0)) AS NegSlope
RESIDENT SWBS_Fit;
LET vBins=Peek('Bins',0,'DIAG_Fit'); LET vTrust=Peek('Trusted',0,'DIAG_Fit');
LET vNegI=Peek('NegInt',0,'DIAG_Fit'); LET vNegS=Peek('NegSlope',0,'DIAG_Fit');
DROP TABLE DIAG_Fit;

// ---------- 8. Candidates ----------
Candidates:
LOAD
    %JCN_Key                        AS JCN_KEY,     // NOT a readable JCN — see [idprobe]
    [JB_JCN Est Man Days Qy]        AS Est_MD,
    Left(SWLIN_SYS_ID,3)            AS SWBS,
    Left(Left(SWLIN_SYS_ID,3),1)    AS SWBS1
FROM [lib://QVD-JRMC-AIM/AIM_JB_JCN.qvd] (qvd)
WHERE [JB_JCN Est Man Days Qy] > 0;

LEFT JOIN (Candidates) LOAD SWBS, n, MedProd, MedLong, MedIdle, mProd, bProd RESIDENT SWBS_Fit;
LEFT JOIN (Candidates) LOAD SWBS1, n1, pMedProd, pMedLong, pmProd, pbProd RESIDENT Parent_Fit;
DROP TABLES SWBS_Fit, Parent_Fit;

// ---------- 9. Predict and bin ----------
Screen:
NOCONCATENATE LOAD *,
    If(PredSpan <= $(v96Days),'1 MAYBE 96hr',
      If(PredSpan <= $(vCMAVDays),'2 MAYBE CMAV',
        If(PredSpan <= $(vCMAVDays)*$(vMarginPct),'3 MARGINAL','4 MUST-DO'))) AS Screen_Bin
;
LOAD
    JCN_KEY, SWBS, Est_MD, n, n1,
    RangeMax(0.5, Alt( If(n  >= $(vMinN), bProd  + mProd *Est_MD),
                       If(n1 >= $(vMinN), pbProd + pmProd*Est_MD),
                       $(vgb) + $(vgm)*Est_MD))                    AS PredSpan,
    Alt( If(n>=$(vMinN), MedProd), If(n1>=$(vMinN), pMedProd), $(vgMedProd) ) AS PredSpan_Median,
    Alt( If(n>=$(vMinN), MedLong), If(n1>=$(vMinN), pMedLong), $(vgMedLong) ) AS PredLongestStep,
    Alt( If(n>=$(vMinN), MedIdle), 0 )                             AS TypicalIdleDays,
    If(n >= $(vMinN),'own SWBS', If(n1 >= $(vMinN),'parent','global')) AS FitSource
RESIDENT Candidates;
DROP TABLE Candidates;

// ===================== DIAGNOSTICS =====================
TRACE ============== WCP SCREEN v4 ==============;
TRACE [rows] rawPhases=$(vRaw)  keptPhases=$(vKept)  jobs(ICN)=$(vNICN);
TRACE [train] usable jobs=$(vTrainAll)  after SWBS+singleJCN filter=$(vTrain);
TRACE [bundling] of $(vDTot) jobs: blankSWBS=$(vDNoSW)  BUNDLED(>1 JCN)=$(vDBund)  notInBridge=$(vDNoBr);
TRACE [bundling] JCNs sitting inside those bundles=$(vDJcns)   <-- if this is large, training is biased toward simple work;
TRACE [fit] bins=$(vBins) (parent=$(vNPar))  trusted(n>=$(vMinN))=$(vTrust)  negIntercept=$(vNegI)  negSlope=$(vNegS);

// --- which KOs were classified as paperwork? ---
NonProd_List:
LOAD KO, koPhases, koMH, koSpan RESIDENT KO_Stats
WHERE koMH <= $(vNonProdMH) AND koSpan >= $(vNonProdSpan);
LET vNP = NoOfRows('NonProd_List');
DIAG_NP: LOAD Sum(koPhases) AS ExPhases RESIDENT NonProd_List;
LET vExPh = Peek('ExPhases',0,'DIAG_NP'); DROP TABLE DIAG_NP;
TRACE [paperwork] $(vNP) key operations excluded, covering $(vExPh) of $(vKept) phases;
FOR i = 0 TO RangeMin(NoOfRows('NonProd_List'),15)-1
  LET vK=Peek('KO',$(i),'NonProd_List'); LET vKp=Peek('koPhases',$(i),'NonProd_List');
  LET vKm=Peek('koMH',$(i),'NonProd_List'); LET vKs=Peek('koSpan',$(i),'NonProd_List');
  TRACE [paperwork] $(vK): phases=$(vKp) medManhours=$(vKm) medSpan=$(vKs);
NEXT i
DROP TABLES NonProd_List, KO_Stats;

// --- THE headline: does excluding paperwork fix the span? ---
DIAG_Span:
LOAD Median(SpanAll) AS mAll, Median(SpanProd) AS mProdS, Fractile(SpanProd,0.9) AS pProd,
     Median(SpanLongestProd) AS mLong, Median(StepDaysProd) AS mStep, Median(IdleDays) AS mIdle,
     Median(T_EstMD) AS mEst, Median(NProdPhases) AS mNP
RESIDENT Train_Clean;
LET vmAll=Peek('mAll',0,'DIAG_Span');   LET vmProd=Peek('mProdS',0,'DIAG_Span');
LET vpProd=Peek('pProd',0,'DIAG_Span'); LET vmLong=Peek('mLong',0,'DIAG_Span');
LET vmStep=Peek('mStep',0,'DIAG_Span'); LET vmIdle=Peek('mIdle',0,'DIAG_Span');
LET vmEst=Peek('mEst',0,'DIAG_Span');   LET vmNP=Peek('mNP',0,'DIAG_Span');
TRACE [span] all-phase median=$(vmAll)   PRODUCTION median=$(vmProd)  p90=$(vpProd);
TRACE [span] longest single production step median=$(vmLong)   production steps per job=$(vmNP);
TRACE [idle] production window=$(vmProd)  sum of step durations=$(vmStep)  IDLE=$(vmIdle) days;
TRACE [span] median production man-days per job=$(vmEst);
DROP TABLE DIAG_Span;

// --- verdicts ---
DIAG_Bin: LOAD Screen_Bin AS B, Count(1) AS C RESIDENT Screen GROUP BY Screen_Bin;
FOR i = 0 TO NoOfRows('DIAG_Bin')-1
  LET vB=Peek('B',$(i),'DIAG_Bin'); LET vC=Peek('C',$(i),'DIAG_Bin');
  TRACE [bins] $(vB) = $(vC);
NEXT i
DROP TABLE DIAG_Bin;

DIAG_Src: LOAD FitSource AS S, Count(1) AS C RESIDENT Screen GROUP BY FitSource;
FOR i = 0 TO NoOfRows('DIAG_Src')-1
  LET vS=Peek('S',$(i),'DIAG_Src'); LET vC=Peek('C',$(i),'DIAG_Src');
  TRACE [fitsource] $(vS) = $(vC);
NEXT i
DROP TABLE DIAG_Src;

// --- identifier probe: what does a real job number look like? ---
DIAG_ID1:
FIRST 5 LOAD %JCN_Key AS a, [JB_JCN Job Seq Num] AS b, [JB_JCN Avail ID] AS c,
             Left(JCN_DESC_TX,28) AS d
FROM [lib://QVD-JRMC-AIM/AIM_JB_JCN.qvd] (qvd);
TRACE [idprobe] AIM_JB_JCN: pctJCNKey | JobSeqNum | AvailID | desc;
FOR i = 0 TO NoOfRows('DIAG_ID1')-1
  LET va=Peek('a',$(i),'DIAG_ID1'); LET vb=Peek('b',$(i),'DIAG_ID1');
  LET vc=Peek('c',$(i),'DIAG_ID1'); LET vd=Peek('d',$(i),'DIAG_ID1');
  TRACE [idprobe] JB_JCN: $(va) | $(vb) | $(vc) | $(vd);
NEXT i
DROP TABLE DIAG_ID1;

DIAG_ID2:
FIRST 5 LOAD %CuPhase_Key AS a, %JCN_Key AS b, [Job Control Number] AS c
FROM [lib://QVD-JRMC-AIM/AIM_JCN.qvd] (qvd);
TRACE [idprobe] AIM_JCN: pctCuPhaseKey | pctJCNKey | JobControlNumber;
FOR i = 0 TO NoOfRows('DIAG_ID2')-1
  LET va=Peek('a',$(i),'DIAG_ID2'); LET vb=Peek('b',$(i),'DIAG_ID2');
  LET vc=Peek('c',$(i),'DIAG_ID2');
  TRACE [idprobe] AIM_JCN: $(va) | $(vb) | $(vc);
NEXT i
DROP TABLE DIAG_ID2;

TRACE ============== END ==============;

FOR EACH vT in 'Train_Clean','CuPhase_T','Ships_T','CohortProjects','ICN_JCNCount'
  IF Not IsNull(TableNumber('$(vT)')) THEN
    DROP TABLE [$(vT)];
  END IF
NEXT vT
```

## What to look for

**`[span]` is the headline.** The all-phase median should come back around 310 days, matching what
the diagnostic already showed. The production median is the new number. If it lands in the tens of
days, the model finally measures work.

**`[bins]` answers the open question.** Until now essentially nothing reached the 96-hour pile, two
jobs out of 3,708. With paperwork removed, either that pile fills up or it stays empty because Navy
work genuinely does not close in four days. Both answers are useful; the current state, where we
could not tell which, is not.

**`[idle]` is the one that might matter most to the command.** It prints the production window, the
total time the individual steps were open, and the difference. That difference is the job waiting.
If it is roughly half the window, that is the schedule-compression target, and it is measurable per
SWBS from the same fit.

**`[paperwork]` is your sanity check.** It lists the codes the script decided were paperwork. `S01`,
`P01`, `S02` and the S/P/M families should appear. If something with real labour shows up there,
raise `vNonProdMH` or `vNonProdSpan`.

**`[idprobe]` is for the job-number problem.** It prints sample key values from both tables. Compare
the two `%CuPhase_Key` formats: if they look different, that is why the lookup returned blank for
every phase last run, and it tells us whether the readable job control number is reachable at all.

## Still unresolved, deliberately

The training estimate comes from phase-level man-hours divided by 8, while scoring uses the
job-level induction estimate. Different numbers at different grains. `[span]` prints the median
training man-days so you can compare it against the candidate median from the earlier run, which was
11. If those are far apart, this is doing real damage and needs the proper join.

The 8-hour man-day is still an assumption.

Candidates are still filtered only on a positive estimate, so this scores the whole backlog rather
than incoming work.

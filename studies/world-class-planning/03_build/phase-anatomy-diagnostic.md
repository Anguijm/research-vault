---
type: build-artifact
study: world-class-planning
title: Phase anatomy diagnostic — what do an ICN's phases actually look like?
classification: internal
created: 2026-07-27
---

# Phase anatomy diagnostic — run this before any more fitting

This script fits nothing and screens nothing. Its only job is to show what the data looks like so
we can decide, from evidence, which phases belong in a span. Run it, read the traces, and the
modelling question answers itself.

## Why this comes before another fit

Your read is that the JCN is tied across an ICN's phases and that not all phases are production,
with S01 typically being planning. If that is right it explains the ~366-day intercept completely:
the envelope from the earliest phase start to the latest phase finish begins at *planning*, so we
have been measuring planning-through-completion and calling it execution span. That is a better
explanation than the "longest single phase" idea I put in v3, because it keeps the multi-phase
production window intact instead of collapsing it to one phase. If a job has three production
phases running over three weeks, longest-phase understates it and production-envelope gets it
right.

So the target definition is probably **the envelope across an ICN's production phases**: earliest
production start to latest production finish, planning excluded. But we should not hard-code `S01`
on the strength of "usually." The script prints every key operation code with its behavioural
fingerprint, and planning phases will identify themselves.

## What it prints

1. **`[cardinality]`** — how ICNs, JCNs and Job Summaries actually relate. Confirms whether ICN is
   the right grouping grain before we switch to it.
2. **`[ko-profile]`** — one line per key operation code: how many phases, how many distinct ICNs,
   median man-hours, median phase span, and **median offset in days from its ICN's first start**.
   That last column is the tell. A planning phase sits at or near offset zero and carries low
   man-hours; production phases start later and carry the labour.
3. **`[sample]`** — a handful of complete ICNs dumped phase by phase in date order, with code,
   title, dates, span and man-hours. This is the "logic our way through it" view.
4. **`[spancompare]`** — median span per ICN three ways: all phases, production only (excluding
   whatever you list in `vPlanKO`), and the old Job-Summary envelope. The gap between the first two
   is the size of the planning-phase problem.

## Data links this uses, and why they changed

Both come out of the newly generated `qvd-field-inventory.md`.

**`AIM_JCN` replaces the JCN bridge.** It carries `%CuPhase_Key` and `%JCN_Key` together, so it
links phases to job control numbers directly. The `ALL_TABLES/JCN_CU_PHASE.qvd` bridge we were
using is what inflated the CU-phase table from 528,183 rows to 752,375. It also carries
`JCN Status` and `JCN Availability`, which is the open/active candidate filter we still owe.

**`CU_swlin_sys_id` replaces `Mid(ICN,6,3)` for SWBS.** It sits directly on the CU phase and is
defined as the SWLIN system identifier, the same concept as `SWLIN_SYS_ID` on `AIM_JB_JCN`. Using
one field on both sides makes the code spaces match by construction, which is the item 23 risk. The
script prints all three derivations side by side so you can see whether they agree before we commit.

```qlik
// ===========================================================================
// PHASE ANATOMY DIAGNOSTIC — no fit, no screen. Answers: which phases are production?
// ===========================================================================

SET vHomeport   = 'YOKOSUKA';
SET vSampleICNs = 8;          // how many example ICNs to dump phase-by-phase
SET vPlanKO     = 'S01';      // suspected PLANNING key ops; edit after reading [ko-profile]
                              // multiple: 'S01','S02'

// ---------- Cohort ----------
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

// ---------- JCN per CU phase, straight from AIM_JCN (no bridge, no fan-out) ----------
Map_CuP_JCN:
MAPPING LOAD %CuPhase_Key, [Job Control Number]
FROM [lib://QVD-JRMC-AIM/AIM_JCN.qvd] (qvd);

// ---------- CU-phase facts, with everything we might classify on ----------
CuPhase_Raw:
LOAD
    CU_PHASE_SA_ID,
    %JobSumm_CuPhase_Key                       AS JS_Key,
    ICN,
    KO,
    [Cu Phase Title]                           AS PhTitle,
    MANHOUR_QY                                 AS Est_MH,
    CU_swlin_sys_id                            AS SwlinSys,     // SWBS source, phase side
    [Cu Phase Group CD]                        AS GroupCD,      // "opportunity window group"
    WORK_TYPE_CD                               AS WorkType,
    CU_WORK_CAT_CD                             AS WorkCat,
    ApplyMap('Map_CuP_JCN', %CuPhase_Key, '')  AS JCN,
    Num([Cu Phase Actual Start Date])          AS ACS,
    Num([Cu Phase Actual Completion Date])     AS ACC
FROM [lib://QVD-JRMC-AIM/AIM_CuPhase.qvd] (qvd)
WHERE ApplyMap('Map_Cohort',[Cu Phase Project ID],0)=1
  AND ApplyMap('Map_Certified',%CuPhase_Key,0)=1;

LET vRaw = NoOfRows('CuPhase_Raw');

CuPhase_T:
NOCONCATENATE LOAD *,
    (ACC - ACS + 1)                            AS PhaseSpan,
    Left(SwlinSys,3)                           AS SWBS_fromSwlin,
    Mid(ICN,6,3)                               AS SWBS_fromICN
RESIDENT CuPhase_Raw
WHERE IsNum(ACS) AND IsNum(ACC) AND ACS>0 AND ACC>0 AND ACC>=ACS;

DROP TABLE CuPhase_Raw;
LET vKept = NoOfRows('CuPhase_T');

TRACE ============ PHASE ANATOMY DIAGNOSTIC ============;
TRACE [rows] rawPhases=$(vRaw)  keptPhases=$(vKept);

// ---------- 1. Cardinality: is ICN the right grain? ----------
DIAG_Card:
LOAD
    Count(DISTINCT ICN)      AS nICN,
    Count(DISTINCT JCN)      AS nJCN,
    Count(DISTINCT JS_Key)   AS nJS,
    Count(1)                 AS nPhase
RESIDENT CuPhase_T;
LET vnICN=Peek('nICN',0,'DIAG_Card'); LET vnJCN=Peek('nJCN',0,'DIAG_Card');
LET vnJS=Peek('nJS',0,'DIAG_Card');   LET vnPh=Peek('nPhase',0,'DIAG_Card');
TRACE [cardinality] phases=$(vnPh)  distinct ICN=$(vnICN)  distinct JCN=$(vnJCN)  distinct JobSummary=$(vnJS);
DROP TABLE DIAG_Card;

// how many ICNs does a JCN span, and vice versa?
ICN_per_JCN: LOAD JCN, Count(DISTINCT ICN) AS nI RESIDENT CuPhase_T WHERE Len(JCN)>0 GROUP BY JCN;
DIAG_IPJ: LOAD Median(nI) AS Med, Max(nI) AS Mx, Sum(If(nI>1,1,0)) AS Multi, Count(1) AS Tot RESIDENT ICN_per_JCN;
LET vM=Peek('Med',0,'DIAG_IPJ'); LET vX=Peek('Mx',0,'DIAG_IPJ');
LET vMu=Peek('Multi',0,'DIAG_IPJ'); LET vT=Peek('Tot',0,'DIAG_IPJ');
TRACE [cardinality] ICNs per JCN: median=$(vM) max=$(vX)  JCNs spanning >1 ICN=$(vMu) of $(vT);
DROP TABLES ICN_per_JCN, DIAG_IPJ;

JCN_per_ICN: LOAD ICN, Count(DISTINCT JCN) AS nJ RESIDENT CuPhase_T WHERE Len(JCN)>0 GROUP BY ICN;
DIAG_JPI: LOAD Median(nJ) AS Med, Max(nJ) AS Mx, Sum(If(nJ>1,1,0)) AS Multi, Count(1) AS Tot RESIDENT JCN_per_ICN;
LET vM=Peek('Med',0,'DIAG_JPI'); LET vX=Peek('Mx',0,'DIAG_JPI');
LET vMu=Peek('Multi',0,'DIAG_JPI'); LET vT=Peek('Tot',0,'DIAG_JPI');
TRACE [cardinality] JCNs per ICN: median=$(vM) max=$(vX)  ICNs with >1 JCN=$(vMu) of $(vT);
DROP TABLES JCN_per_ICN, DIAG_JPI;

// ---------- 2. KO profile: the behavioural fingerprint of each key operation ----------
ICN_Start: LOAD ICN, Min(ACS) AS ICNStart RESIDENT CuPhase_T GROUP BY ICN;
Map_ICNStart: MAPPING LOAD ICN, ICNStart RESIDENT ICN_Start;
DROP TABLE ICN_Start;

KO_Profile:
LOAD
    KO,
    Count(1)                                              AS Phases,
    Count(DISTINCT ICN)                                   AS ICNs,
    Median(Est_MH)                                        AS MedMH,
    Median(PhaseSpan)                                     AS MedSpan,
    Median(ACS - ApplyMap('Map_ICNStart', ICN, ACS))      AS MedOffset
RESIDENT CuPhase_T
GROUP BY KO;

TRACE [ko-profile] KO | phases | ICNs | medManhours | medPhaseSpan | medDaysAfterICNstart;
FOR i = 0 TO NoOfRows('KO_Profile')-1
  LET vKO=Peek('KO',$(i),'KO_Profile');       LET vP=Peek('Phases',$(i),'KO_Profile');
  LET vI=Peek('ICNs',$(i),'KO_Profile');      LET vMH=Peek('MedMH',$(i),'KO_Profile');
  LET vSp=Peek('MedSpan',$(i),'KO_Profile');  LET vOf=Peek('MedOffset',$(i),'KO_Profile');
  TRACE [ko-profile] $(vKO) | $(vP) | $(vI) | $(vMH) | $(vSp) | $(vOf);
NEXT i
DROP TABLE KO_Profile;

// ---------- 3. Sample ICNs, dumped phase by phase ----------
ICN_Size: LOAD ICN, Count(1) AS NP RESIDENT CuPhase_T GROUP BY ICN;

ICN_Sample:
LOAD ICN RESIDENT ICN_Size WHERE NP >= 3 AND NP <= 8;
DROP TABLE ICN_Size;

// keep only the first vSampleICNs of them.
// NOTE the rename: a one-argument Exists(ICN) would test against CuPhase_T's own
// ICN values and match every row, so the sample list needs its own field name.
ICN_Keep:
LOAD ICN AS SampleICN RESIDENT ICN_Sample WHERE RecNo() <= $(vSampleICNs);
DROP TABLE ICN_Sample;

Sample_Phases:
LOAD ICN, KO, PhTitle, Est_MH, PhaseSpan, ACS, ACC
RESIDENT CuPhase_T
WHERE Exists(SampleICN, ICN)
ORDER BY ICN, ACS;

TRACE [sample] ICN | KO | start | end | spanDays | manhours | title;
FOR i = 0 TO NoOfRows('Sample_Phases')-1
  LET vIc=Peek('ICN',$(i),'Sample_Phases');    LET vKo=Peek('KO',$(i),'Sample_Phases');
  LET vS =Date(Peek('ACS',$(i),'Sample_Phases'),'YYYY-MM-DD');
  LET vE =Date(Peek('ACC',$(i),'Sample_Phases'),'YYYY-MM-DD');
  LET vSp=Peek('PhaseSpan',$(i),'Sample_Phases');
  LET vMh=Peek('Est_MH',$(i),'Sample_Phases');
  LET vTi=Left(Peek('PhTitle',$(i),'Sample_Phases'),40);
  TRACE [sample] $(vIc) | $(vKo) | $(vS) | $(vE) | $(vSp) | $(vMh) | $(vTi);
NEXT i
DROP TABLES Sample_Phases, ICN_Keep;

// ---------- 4. Span comparison: all phases vs production only vs Job Summary ----------
ICN_Span:
LOAD
    ICN,
    (Max(ACC) - Min(ACS) + 1)                                          AS SpanAll,
    (Max(If(not Match(KO,$(vPlanKO)), ACC))
       - Min(If(not Match(KO,$(vPlanKO)), ACS)) + 1)                   AS SpanProd,
    Count(1)                                                           AS NP,
    Sum(If(Match(KO,$(vPlanKO)),1,0))                                  AS NPlan
RESIDENT CuPhase_T GROUP BY ICN;

JS_Span:
LOAD JS_Key, (Max(ACC) - Min(ACS) + 1) AS SpanJS
RESIDENT CuPhase_T GROUP BY JS_Key;

DIAG_SpanCmp:
LOAD
    Median(SpanAll)  AS MedAll,  Fractile(SpanAll,0.9)  AS P90All,
    Median(SpanProd) AS MedProd, Fractile(SpanProd,0.9) AS P90Prod,
    Sum(If(NPlan>0,1,0)) AS WithPlan, Count(1) AS TotICN
RESIDENT ICN_Span;
LET vMA=Peek('MedAll',0,'DIAG_SpanCmp');   LET vPA=Peek('P90All',0,'DIAG_SpanCmp');
LET vMP=Peek('MedProd',0,'DIAG_SpanCmp');  LET vPP=Peek('P90Prod',0,'DIAG_SpanCmp');
LET vWP=Peek('WithPlan',0,'DIAG_SpanCmp'); LET vTI=Peek('TotICN',0,'DIAG_SpanCmp');

DIAG_JS: LOAD Median(SpanJS) AS MedJS, Fractile(SpanJS,0.9) AS P90JS RESIDENT JS_Span;
LET vMJ=Peek('MedJS',0,'DIAG_JS'); LET vPJ=Peek('P90JS',0,'DIAG_JS');

TRACE [spancompare] ICN all-phase   median/p90 = $(vMA) / $(vPA);
TRACE [spancompare] ICN production  median/p90 = $(vMP) / $(vPP)   (excluding KO $(vPlanKO));
TRACE [spancompare] JobSummary      median/p90 = $(vMJ) / $(vPJ)   (the old v3 definition);
TRACE [spancompare] ICNs containing a suspected planning phase = $(vWP) of $(vTI);
DROP TABLES DIAG_SpanCmp, DIAG_JS, ICN_Span, JS_Span;

// ---------- 5. Do the three SWBS derivations agree? ----------
DIAG_SWBS:
LOAD
    Count(DISTINCT SWBS_fromSwlin)                          AS nSwlin,
    Count(DISTINCT SWBS_fromICN)                            AS nICNd,
    Sum(If(SWBS_fromSwlin = SWBS_fromICN,1,0))              AS Agree,
    Sum(If(Len(Trim(SWBS_fromSwlin))<>3,1,0))               AS BadSwlin,
    Sum(If(Len(Trim(SWBS_fromICN))<>3,1,0))                 AS BadICN,
    Count(1)                                                AS Tot
RESIDENT CuPhase_T;
LET vNS=Peek('nSwlin',0,'DIAG_SWBS'); LET vNI=Peek('nICNd',0,'DIAG_SWBS');
LET vAg=Peek('Agree',0,'DIAG_SWBS');  LET vBS=Peek('BadSwlin',0,'DIAG_SWBS');
LET vBI=Peek('BadICN',0,'DIAG_SWBS'); LET vTo=Peek('Tot',0,'DIAG_SWBS');
TRACE [swbs] distinct values: fromSWLIN=$(vNS)  fromICN=$(vNI);
TRACE [swbs] of $(vTo) phases: the two derivations agree on $(vAg);
TRACE [swbs] malformed (not 3 chars): fromSWLIN=$(vBS)  fromICN=$(vBI);
DROP TABLE DIAG_SWBS;

TRACE ============ END DIAGNOSTIC ============;

FOR EACH vT in 'CuPhase_T','Ships_T','CohortProjects'
  IF Not IsNull(TableNumber('$(vT)')) THEN
    DROP TABLE [$(vT)];
  END IF
NEXT vT
```

## How to reason from the output

**Read `[ko-profile]` first.** Sort your eye down the `medDaysAfterICNstart` column. Codes sitting
at or near zero with low man-hours are the front-end phases; that is planning identifying itself.
Codes with meaningful man-hours starting later are production. If `S01` behaves the way you expect,
you will see it immediately, and you will probably also find one or two more codes that belong in
the exclusion list.

**Then read `[sample]`.** Eight real ICNs, phases in date order. This is where you can apply
knowledge the data cannot express, like recognising a title as a test or certification step rather
than production. If a phase is a hold or a wait rather than work, that changes whether it belongs
in the span.

**Then check `[spancompare]`.** If the all-phase median is in the hundreds of days and the
production-only median is in the tens, the diagnosis is confirmed and the target definition is
production envelope per ICN. Put the winning `KO` list into `vPlanKO`, re-run, and confirm the
number settles.

**Finally `[swbs]` and `[cardinality]`** decide two structural questions: whether to derive SWBS
from the SWLIN identifier or the ICN string, and whether to group at ICN or keep Job Summary. If
JCNs routinely span several ICNs, the single-JCN filter we have been using is doing something
different from what we assumed and needs revisiting.

## What happens next

Once `vPlanKO` is settled, `span-screen-v3.md` gets a fourth span definition (production envelope
per ICN) and the other three become the control group. I would then expect the fit to be worth
running for the first time, because the intercept will finally represent a fixed wait inside a
production window rather than the distance from planning to delivery.

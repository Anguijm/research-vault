---
type: build-tests
study: world-class-planning
title: Test/validation artifacts for the span-fit screen
classification: internal
created: 2026-06-23
companion: 03_build/span-screen-qlik.md
---

# Tests for the span-fit screen

Two kinds of artifact: a **diagnostic block** you append to the load script (it prints pass/fail
counts to the reload log on every run), and a set of **sheet objects** to look at the fit before
trusting it. Part C maps each check back to the `[CONFIRM]` items so a red number tells you which
key/field is wrong.

## Part A — Diagnostic block (append to the end of the load script)

Paste this after Section 9. It reads the resident tables and TRACEs counts + data-quality flags;
it also leaves three small `DIAG_*` tables for charting. A clean reload should show the "look-for"
values in Part C.

```qlik
// ===================== WCP SCREEN — RELOAD DIAGNOSTICS =====================
TRACE ============================================================;

LET vNProj = NoOfRows('CohortProjects');
LET vNCuP  = NoOfRows('CuPhase_T');
LET vNHist = NoOfRows('JS_Clean');
LET vNFit  = NoOfRows('SWBS_Fit');
LET vNCand = NoOfRows('Screen');
TRACE [counts] projects=$(vNProj)  cuphases=$(vNCuP)  singleJCNjobs=$(vNHist)  SWBSbins=$(vNFit)  candidates=$(vNCand);

// --- CU-phase data quality (catches the SWLIN-join and actual-date [CONFIRM]s) ---
DIAG_CuP_DQ:
LOAD
    Count(1)                                     AS Tot,
    Sum(If(Len(Trim(SWBS))<>3,1,0))              AS BadSWBS,
    Sum(If(IsNull(ACS) or ACS=0,1,0))            AS BlankACS,
    Sum(If(IsNull(ACC) or ACC=0,1,0))            AS BlankACC,
    Sum(If(ACC<ACS,1,0))                         AS NegSpan
RESIDENT CuPhase_T;
LET vTot=Peek('Tot',0,'DIAG_CuP_DQ'); LET vBad=Peek('BadSWBS',0,'DIAG_CuP_DQ');
LET vBacs=Peek('BlankACS',0,'DIAG_CuP_DQ'); LET vBacc=Peek('BlankACC',0,'DIAG_CuP_DQ'); LET vNeg=Peek('NegSpan',0,'DIAG_CuP_DQ');
TRACE [cuphase DQ] of $(vTot): badSWBS=$(vBad)  blankACS=$(vBacs)  blankACC=$(vBacc)  negSpan=$(vNeg);

// --- Bundle distribution: how many summaries have 1, 2, 3+ JCNs ---
// (preceding load: the inner LOAD counts JCNs per summary, the outer buckets them)
DIAG_BundleDist:
LOAD JCNsInJS, Count(JS_Key) AS Summaries
GROUP BY JCNsInJS;
LOAD JS_Key, Count(DISTINCT JCN_SA_ID) AS JCNsInJS
RESIDENT CuPhase_T
GROUP BY JS_Key;
TRACE [bundles] see DIAG_BundleDist (1=clean single-JCN, 2+=bundled);

// --- History value ranges (catches unit problems in span / estimate) ---
DIAG_HistRange:
LOAD
    Min(Span_Days) AS SpanMin, Median(Span_Days) AS SpanMed, Max(Span_Days) AS SpanMax,
    Min(Est_MD)    AS EstMin,  Median(Est_MD)    AS EstMed,  Max(Est_MD)    AS EstMax
RESIDENT JS_Clean;
TRACE [history] span days min/med/max = $(=Peek('SpanMin',0,'DIAG_HistRange'))/$(=Peek('SpanMed',0,'DIAG_HistRange'))/$(=Peek('SpanMax',0,'DIAG_HistRange'));

// --- Fit sanity ---
DIAG_FitDQ:
LOAD
    Count(1)                          AS Bins,
    Sum(If(n>=$(vMinN),1,0))          AS Trusted,
    Sum(If(Intercept<0,1,0))          AS NegIntercept,
    Sum(If(Slope<0,1,0))              AS NegSlope
RESIDENT SWBS_Fit;
TRACE [fit] bins=$(=Peek('Bins',0,'DIAG_FitDQ'))  trusted(n>=$(vMinN))=$(=Peek('Trusted',0,'DIAG_FitDQ'))  negIntercept=$(=Peek('NegIntercept',0,'DIAG_FitDQ'))  negSlope=$(=Peek('NegSlope',0,'DIAG_FitDQ'));

// --- Candidate bin distribution ---
DIAG_BinDist:
LOAD Screen_Bin, Count(1) AS Candidates
RESIDENT Screen GROUP BY Screen_Bin;
TRACE [screen] candidate bins -> see DIAG_BinDist;

DROP TABLE DIAG_CuP_DQ, DIAG_HistRange, DIAG_FitDQ;   // keep DIAG_BundleDist + DIAG_BinDist for charts
TRACE ===================== END DIAGNOSTICS =====================;
```

*(If your Qlik build won't evaluate `$(=Peek(...))` inside TRACE, replace those with `LET` lines
like the first block and TRACE the variables.)*

## Part B — Sheet objects (build these to look at the fit)

1. **Fit review (straight table) — the calibration.** Source `SWBS_Fit`.
   - Dimension: `SWBS`
   - Expressions: `n` · `MedianSpan` · `Slope` · `Intercept` ·
     `=If(n>=$(vMinN),'own','shrunk-to-parent')` (Trust) ·
     `=If(Intercept<0 or Slope<0,'CHECK','ok')` (Flag)
   - Sort by `n` descending. Scan the CHECK rows and the low-`n` rows first.

2. **Per-SWBS scatter — eyeball the fit (the important one).** Source `JS_Clean`.
   - Chart type: scatter. Dimension: `JS_Key`. X = `Est_MD`, Y = `Span_Days`.
   - Add a **list box on `SWBS`** next to it; click one SWBS at a time.
   - Turn on a **linear trendline + show equation**. Cross-check: the trendline's slope/intercept
     should match `SWBS_Fit.Slope`/`Intercept` for that SWBS. If the cloud is clearly non-linear or
     fan-shaped, prefer `MedianSpan` for that SWBS.

3. **Span histogram — does the data straddle your thresholds?** Source `JS_Clean`.
   - Dimension: `=Class(Span_Days, 7)` (weekly buckets). Expression: `Count(JS_Key)`.
   - Drop reference lines at `$(v96Days)` and `$(vCMAVDays)` to see how much history lands in each bin.

4. **Candidate screen (straight table) — the output.** Source `Screen`.
   - Dimension: `JCN`. Expressions: `SWBS` · `Est_MD` · `PredSpan_Days` · `Screen_Bin`.

5. **Bin distribution (bar).** Source `DIAG_BinDist` (or `Screen`).
   - Dimension: `Screen_Bin`. Expression: `Count(JCN)` (or `Sum(Candidates)`).

6. **Bundle split (bar).** Source `DIAG_BundleDist`.
   - Dimension: `JCNsInJS`. Expression: `Sum(Summaries)`. Confirms how much history is clean
     single-JCN (bin 1) vs bundled.

## Part C — What "good" looks like (and what a red number means)

| Check (from the log) | Look for | If it's off |
|---|---|---|
| `projects` | > 0 | 0 → ship/homeport scope wrong, or `%ShipKey` join (relax `Match([Ship Type]...)`). |
| `cuphases` | a large number | 0 → cohort or certified filter killed everything; check `Map_Cohort` / `Approval Status CD='CRT'`. |
| `badSWBS / Tot` | ≈ 0 | high → **[CONFIRM #2]**: the `AIM_SWLIN`↔CU-phase key, or `Left(SWLIN Line Item,3)` isn't the SWBS. |
| `blankACS / blankACC` | ≈ 0 | high → **[CONFIRM #1]**: wrong actual-date field names (try the `Cu Phase Actual *` aliases). |
| `negSpan` | 0 | > 0 → ACS/ACC swapped or a date-parse issue. |
| `singleJCNjobs` | a usable count (hundreds+) | very low → the `JCN_CU_PHASE` bridge join or the single-JCN filter is off. |
| `span days med` | sane in **days** (e.g., single digits to tens) | thousands → dates loaded as serials/text; wrap in `Num(Date#(...))`. Tiny/0 → unit problem. |
| `SWBSbins` | ~100 | far off → SWBS derivation wrong (see badSWBS). |
| `trusted (n>=vMinN)` | a good share of bins | few → either thin history (lower `vMinN`) or the join is dropping rows. |
| `negIntercept / negSlope` | small handful | many → the linear fit is unstable for those SWBS; use `MedianSpan` there. |
| `candidate bins` | spread across bins, not all in one | all "must-do" → check `Est_MD` units on candidates (man-days vs man-hours) and the thresholds. |

Run order: get the **log counts** green first (they confirm the joins and units), then build object
**2 (the scatter)** to decide linear-fit vs median per SWBS, then look at **4/5** to see the screen
actually sort candidates.

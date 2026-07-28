---
type: handoff
study: world-class-planning
title: Qlik troubleshooting handoff — self-contained context for a fresh session
classification: internal
created: 2026-07-27
updated: 2026-07-29
audience: a helper session with no prior context
---

# Qlik troubleshooting handoff

**If you are a fresh assistant session reading this: this file is your entire context.** You do not
need any other file to help. Everything below is established from real reloads against the live
system. Where something is unverified it says so.

**Last updated 2026-07-29.** If the reload logs the operator shows you contradict this file, trust
the logs and say so.

---

## 1. What this is, in plain terms

A US Navy ship-repair activity plans maintenance work in a system called **AIM (Advanced Industrial
Management)**. Work arrives as **JCNs (Job Control Numbers)**. Before committing a JCN to a large
scheduled availability, the activity wants to screen it against three questions:

1. Can it be closed out within **96 hours**? (Defined locally as 96 **elapsed clock** hours, so four
   calendar days including nights and weekends.)
2. Can it fit in a **6-week CMAV (Continuous Maintenance Availability)**? (42 calendar days.)
3. Can it be split across multiple windows of opportunity?

The tool is a **Qlik load script** that learns from completed historical work how long a job of a
given size and type actually takes, then sorts incoming JCNs into bins: maybe-deferrable, marginal,
must-do.

**Your job.** The operator runs a script at work and pastes back the reload log. You interpret it and
fix the script. **You cannot query Qlik and neither can the operator from your session.** Everything
you learn arrives as `TRACE` output the operator pastes. So prefer changes that *print more
information* over changes that guess. Two earlier runs were lost to reasoning about values nobody
had looked at.

---

## 2. Where it actually stands (read this before proposing anything)

**The screen works.** As of the 28 July run it produces usable output. The long-running failure is
fixed. Do not propose fixes for it.

| Run | Date | Outcome |
|---|---|---|
| 1 | 2026-07-26 | Reloaded clean, output unusable. All 2,699 candidates in one bin; fitted intercept ~366 days. |
| 2 | 2026-07-27 | SWBS mapping repaired. Training rows 0 → 17,829, 233 bins. But the key diagnostic printed blank, so nothing could be concluded. |
| 3 | 2026-07-28 | **Working.** 3,708 candidates scored, 3,600 off their own SWBS fit, bins genuinely discriminating. |

**What was wrong, and it is settled.** A job's phases carry a `KO` (key operation) code. `S01` and
the rest of the S, P and M families are **paperwork**, not production: near-zero labour, median
duration around 350 days, opening at day zero. Span was measured as earliest phase start to latest
phase finish, so for three quarters of jobs the model was measuring paperwork.

Confirmed by the phase-anatomy diagnostic:

- ICN all-phase median span **310.7 days** (p90 751)
- Excluding `S01` alone: **50 days** (p90 372)
- Excluding the wider paperwork set: **32 days** (p90 214)
- `S01` appears in **21,700 of 28,478** ICNs, median 6 man-hours, median span 349.7 days, offset 0
- Production phases by contrast: `A01` 80 man-hours / 22 days, `H01` 64 / 9, `R01` 60 / 6, `E01` 20 / 4

**The current problem is different and smaller.** The model is effectively a SWBS lookup table:

- Correlation between estimated man-days and predicted span is **0.22** (longest-phase) / 0.28 (envelope)
- For **64 of 162** SWBS groups, predictions vary by under a day across every job in the group
- SWBS `123` alone holds **1,566 of 3,708** candidates, 42% of the backlog
- The 96-hour bin held **2 of 3,708** jobs

So the open question is no longer "why is it broken" but "does work type need to be finer, and does
the regression beat a plain median." That is what `granularity-test.md` measures.

---

## 3. The scripts, and what to run

All paths relative to `studies/world-class-planning/03_build/`. See `README.md` there for the full
folder map.

| Script | State | Purpose |
|---|---|---|
| `phase-anatomy-diagnostic.md` | **run, question answered** | Fits nothing. Prints each key operation's fingerprint and sample ICNs. Re-run only to retune the paperwork rule. |
| `span-screen-v4.md` | **current, not yet run** | The screen with paperwork phases excluded. Works out which KO codes are paperwork *from the data* (median labour ≤ 8 man-hours AND median span ≥ 60 days) rather than a hard-coded list, and prints which it excluded. Also reports idle time between production steps. |
| `granularity-test.md` | **current, not yet run** | Split-half accuracy. Learns on half the finished jobs, scores the other half, sweeps work-type granularity from 1 character of the SWLIN to 8. Reports median vs regression side by side. |
| `_lineage/span-screen-v3.md` | superseded | Tested three span definitions at once. Its sum-of-phase-days variant is dead (88% must-do, max prediction 5,222 days). |
| `_lineage/span-screen-v1.md` | superseded | First cut. Its `[CONFIRM]` list is the best record of how field names were established. |
| `_lineage/span-screen-test-harness.md` | folded into the scripts | Its warning about `$(=Peek(...))` is the single most useful line in the folder. |

**Accuracy standard, set by the operator.** A prediction **passes** if it puts the job in the same
bin as reality **or a longer one**. It **fails** if it puts the job in a shorter bin, because that is
the error that lets work overrun the window it was screened into. `granularity-test.md` reports
optimistic / exact / conservative separately so the cost of caution stays visible.

---

## 4. The environment

- Qlik reading QVDs via library connection **`lib://QVD-JRMC-AIM/`**, with a subfolder
  **`lib://QVD-JRMC-AIM/ALL_TABLES/`**.
- 50 QVDs across three schemas: **AIM** (planning, 482 fields), **COST** (actual labour and
  financials, 405), **MAT** (material, 293). Full inventory in `qvd-field-inventory.md`.
- **Actual expended labour does not exist in AIM.** It is in COST. Everything AIM holds is an
  estimate. The current scripts deliberately avoid COST by fitting against actual *dates*.
- Nuclear data is masked in the published layer. Do not chase it.

### Row counts as sanity anchors

| Stage | Rows |
|---|---|
| `AIM_Ship` filtered to cohort | 13 |
| `AIM_CuPhase` after cohort + certified filter | 528,183 (528,829 raw, 528,123 kept after date filter) |
| Distinct ICNs | 28,478 |
| Distinct Job Summaries | 28,478 (**ICN and Job Summary are 1:1**) |
| Distinct KO codes | 1,208 |
| Paperwork phases (S/P/M families) | 128,229 of 528,123 |
| Training rows after cleaning (run 2) | 17,829 |
| SWBS bins fit | 233 |
| Candidates scored | 3,708 |

If a run's numbers differ wildly from these, that is itself the finding.

---

## 5. Confirmed field names

Verified from an actual schema-dump reload. **The published layer uses friendly aliases with spaces,
not the underlying database column names.**

### `AIM_CuPhase.qvd` — one row per phase of work
```
%CuPhase_Key, %JobSumm_CuPhase_Key, %Act_Proj_Key, CU_PHASE_SA_ID, CU_SA_ID,
[Cu Phase Actual Start Date], [Cu Phase Actual Completion Date],
[Cu Phase Scheduled Start Date], [Cu Phase Scheduled Completion Date],
[Cu Phase Duration QY], [Cu Phase Group CD], ICN, KO, ICN_KO, MANHOUR_QY,
[Cu Phase Project ID], [Cu Phase Title], CU_swlin_sys_id, CU_WORK_CAT_CD,
WORK_TYPE_CD, [Total Float Qty], [Job Order #], COAR, PROGRESS_RT
```
- `ICN` = internal control number for a CU Phase
- `KO` = key operation assignment (**this is what separates paperwork from production**)
- `CU_swlin_sys_id` = SWLIN system identifier; `Left(...,3)` gives the SWBS
- `[Cu Phase Group CD]` = "the code that denotes opportunity window group" — possibly relevant to
  screening question 3, not yet investigated
- `WORK_TYPE_CD` = O/N/R (Original, New Work, Rework). Does **not** separate planning from production.

### `AIM_JB_JCN.qvd` — incoming JCNs (scoring side)
```
%JCN_Key, [JB_JCN Est Man Days Qy], [JB_JCN SWLIN LI ID], SWLIN_SYS_ID,
[JB_JCN Ship Board Wrk Ctr Cd], [JB_JCN Location ID], [JB_JCN CSMP_NM],
EQUIP_NOUN_NM, APL_AEL_CD, CASREP_CAT_CD, EST_MATERIAL_COST_QY,
TYPE_AVAILABLE_CD, TYCOM_SCREENING_CD, STATUS_CD, POP_Start, POP_End,
JCN_PRIORITY_CD, DEADLINE_DT
```
- **There is no `Job Control Number` field here.** The identifier is `%JCN_Key`, and it is a Qlik
  surrogate key, **not a readable JCN** — see the open bug in section 6.
- `STATUS_CD`, `TYCOM_SCREENING_CD`, `POP_Start`/`POP_End` are untested candidates for an
  "incoming / not-yet-done" filter, still an open item.

### Others
- `AIM_JCN.qvd` — carries `%CuPhase_Key`, `%JCN_Key`, `[Job Control Number]`, `[JCN Status]`.
  **The lookup on `%CuPhase_Key` returns blank for every phase.** See section 6.
- `AIM_CuPhase_Hist.qvd` — certified filter: `[Approval Status CD]='CRT'` and `[Current Flag Cd]='Y'`.
- `AIM_Ship.qvd` — `%Proj_Ship_Key`, `[Ship Home]`, `[Ship Type]`.
- `AIM_Project.qvd` — `[Project ID]`, `%Proj_Ship_Key`.
- `%ICNKOP_KEY` on `COST_FE05` is an ICN-plus-key-op key — the likely future bridge to actual
  labour. **Not yet tried.**

---

## 6. Open bugs and unknowns

1. **The JCN column is not a JCN.** The output's identifier column contains values like `8-130758`.
   `%JCN_Key` is a surrogate key. The readable field is `[Job Control Number]` on `AIM_JCN.qvd`, but
   joining that in **failed**: the diagnostic reported `distinct JCN=1`, meaning the lookup on
   `%CuPhase_Key` returned blank for all 528,123 phases. Before relying on it, have the operator dump
   five rows showing `%JCN_Key`, `[JB_JCN Job Seq Num]`, `JCN_DESC_TX` and the joined
   `[Job Control Number]` side by side, and check whether the two tables' `%CuPhase_Key` values even
   share a format. `span-screen-v4.md` includes an `[idprobe]` block that does this.
2. **Estimate basis mismatch.** Training uses `MANHOUR_QY / 8` at CU-phase level; scoring uses
   `[JB_JCN Est Man Days Qy]` at JCN level. Different estimates at different grains. v4 prints the
   training median so it can be compared against the candidate median (11 in run 3).
3. **The 8-hour man-day is an assumption**, never confirmed against AIM's own convention.
4. **Candidate filter** is only `Est Man Days Qy > 0`, so runs score the whole backlog rather than
   incoming work.
5. **Unverified Qlik functions** in the current scripts: `Fractile()` and `MinString()` in script-side
   aggregation. If one errors, substitute `Median()` for Fractile and `Min()` for MinString.

---

## 7. Qlik behaviours already discovered the hard way

Do not re-litigate these. Each cost a reload.

1. **`$(=Peek('X',0,'T'))` does not evaluate inside `TRACE`** on this build. It prints blank and
   silently destroys diagnostics. Always `LET vX = Peek('X',0,'T');` first, then `TRACE ... $(vX);`.
   This hid the decisive number for an entire run.
2. **A variable used inside `Match()` needs embedded quotes.** `SET vPlanKO = 'S01'` expands wrong;
   it must be `SET vPlanKO = '''S01''';` so `Match(KO, $(vPlanKO))` resolves. Operator found this.
3. **`FirstSortedValue()` returns NULL when two values tie** on sort weight. It was silently dropping
   groups. Replaced with a max-count join plus `MinString()` tie-break.
4. **Single-argument `Exists(Field)` tests against every already-loaded value of that field**,
   including the table being filtered, so it matches everything and looks like it works. Use the
   two-argument form with a renamed field.
5. **`LEFT JOIN` to the JCN bridge fans out rows**, 528,183 → 752,375, silently inflating any
   subsequent `Sum(MANHOUR_QY)`. Use `MAPPING LOAD` + `ApplyMap`, or pre-aggregate.
6. **Joining a coefficient table into another while the source still exists creates synthetic keys.**
   Drop fit tables immediately after the join; capture diagnostics from them *before*.
7. **The `[... Date Empty]` flag fields in the data dictionary do not exist** in the published layer.
   Filter on the date fields themselves.
8. **A clean reload means nothing about correctness.** Runs 1 and 2 both reloaded with zero errors
   and produced garbage. Always read the traces.

### Minimal field-probe script
If field names are ever in doubt, have the operator run this:
```qlik
FOR EACH vF in 'AIM_CuPhase','AIM_JB_JCN','AIM_JCN'
  TRACE ===== $(vF) =====;
  T: FIRST 1 LOAD * FROM [lib://QVD-JRMC-AIM/$(vF).qvd] (qvd);
  LET vN = NoOfFields('T');
  FOR i = 1 TO $(vN)
    LET vNm = FieldName($(i),'T');
    TRACE   field $(i): $(vNm);
  NEXT i
  DROP TABLE T;
NEXT vF
```

---

## 8. Failure triage

| Symptom | Likely cause | Next move |
|---|---|---|
| A `TRACE` line prints blank | `$(=Peek(...))` inside `TRACE` | Convert to `LET` first |
| `Field 'X' not found` | Dictionary name used instead of published alias | Run the probe in section 7 |
| A table loads 0 rows | A `WHERE` filter rejecting everything, usually a code-format mismatch | Load without the filter, `TRACE` sample values of the filtered field, compare formats |
| `Match()` matches nothing | Variable quoting | See gotcha 2 |
| Synthetic keys reported | Two tables sharing 2+ field names | Rename or drop the source right after joining |
| Row count inflates after a `JOIN` | One-to-many fan-out | Replace with `ApplyMap` or pre-aggregate |
| Predictions nearly identical across jobs | Everything falling through to the global fit | Check how many candidates matched a per-group fit; if near zero the two sides' group codes disagree |
| All jobs in one bin | Intercept dominates | Check the span distribution before touching anything else. This was runs 1 and 2. |
| Span medians in the hundreds of days | Paperwork phases not excluded | Check `[paperwork]` trace in v4 lists the S/P/M families |

**General principle:** when something is wrong, print the distribution of the suspect field rather
than reasoning about it.

---

## 9. Things already ruled out — do not suggest these

- **"The reload has an error."** It does not. All three runs completed with 0 forced errors.
- **"Use the `ACTUAL_START_DATE` raw column names."** Not in the published layer; the spaced aliases
  are correct.
- **"Filter on the date-empty flag fields."** Those fields do not exist.
- **"Relax the SWBS filter so rows get through."** Tried. Converts a loud failure into a silent one.
- **"Join `AIM_SWLIN` on `%CuPhase_Key` for the SWBS."** Tried; blanks for most phases.
  `CU_swlin_sys_id` sits directly on the CU phase. Note the two derivations
  (`Left(CU_swlin_sys_id,3)` and `Mid(ICN,6,3)`) were verified to **agree on all 528,123 phases**,
  so either works.
- **"Pull actual labour from AIM."** It is in COST.
- **"The span problem is unsolved."** It is solved. See section 2.
- **A previous session invented a nonexistent "Qlik linter."** Do not propose tooling you have not
  verified exists. If unsure whether a Qlik function is available on this build, say so and offer a
  fallback.

---

## 10. Open design questions — surface these, do not decide them

These are the operator's calls. If your fix depends on one, stop and ask.

1. **How granular should work type be?** `granularity-test.md` measures it. Read the `ownBin%` column
   alongside the failure rate: if failure rate improves while own-bin coverage collapses, the
   improvement is fake because everything is falling back to the global average.
2. **Does the regression earn its keep, or should this be a lookup table?** Same script answers it.
   Given a 0.22 correlation, a plain median may well win, and a lookup table is simpler to build and
   easier to defend to a planner.
3. **What else explains span?** Candidates, in the operator's and my rough order: material lead time
   (`EST_MATERIAL_COST_QY`), work centre (`[JB_JCN Ship Board Wrk Ctr Cd]`), casualty-report status
   (`CASREP_CAT_CD`), and availability type (`TYPE_AVAILABLE_CD`). **Do not nest bins** — with 162
   groups over ~17,800 rows a second dimension starves the cells. Fit global adjustment factors
   (actual ÷ SWBS-median, grouped by the dimension) and apply them on top.
4. **Availability-type pooling.** History deliberately pools CNO, CMAV, CM, EM and WOO. That pooling
   is a strong candidate for a large share of the within-SWBS variance.
5. **How much margin below 4 days** the 96-hour bin should require, since an elapsed clock makes the
   test start-day sensitive and the start day is unknown at screening time.
6. **Idle time.** v4 reports production window minus summed step durations. In run 3's data
   individual production steps ran 4 to 22 days while the production envelope ran ~50, so roughly
   half the window is waiting. That may be more valuable to the command than the screen itself.

---

## 11. Constants

- `96 hours` = **4 calendar days**, elapsed clock, weekends included. Local SRF definition, not in
  4700.1F. Confirmed by the operator 2026-07-26.
- `6-week CMAV` = **42 calendar days**.
- Marginal band = `1.25 ×` the CMAV threshold.
- A SWBS group needs `n >= 8` completed jobs before its own fit is trusted, else fall back to the
  1-digit parent, then global.
- Paperwork rule in v4: a KO is non-production if cohort median labour ≤ 8 man-hours **and** median
  span ≥ 60 days. Derived from the same data it filters, which is acceptable for a screening
  heuristic but is not independent validation.

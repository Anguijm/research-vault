---
type: handoff
study: world-class-planning
title: Qlik troubleshooting handoff — self-contained context for a fresh session
classification: internal
created: 2026-07-27
audience: a helper session with no prior context
---

# Qlik troubleshooting handoff

**If you are a fresh assistant session reading this: this file is your entire context.** You do not
need any other file to help. Everything below is established fact from real reloads against the
live system, not assumption. Where something is unverified it says so.

---

## 1. What this is, in plain terms

A US Navy ship-repair activity plans maintenance work in a system called **AIM (Advanced Industrial
Management)**. Work items arrive as **JCNs (Job Control Numbers)**. Before committing a JCN to a
large scheduled availability, the activity wants to screen it against three questions:

1. Can it be closed out within **96 hours**?
2. Can it fit in a **6-week CMAV (Continuous Maintenance Availability)**?
3. Can it be split across multiple windows of opportunity?

The goal is a **QlikView / Qlik Sense load script** that learns, from completed historical work, how
long a job of a given size and type actually takes, and then sorts incoming JCNs into three bins:
maybe-deferrable, marginal, must-do.

**The modelling idea.** Group history by work type (SWBS, a 3-digit Ship Work Breakdown Structure
code), and per group fit `span_days ≈ Intercept + Slope × estimated_man_days`. Then score each new
JCN's estimate against its group's fit and bin the predicted span against 4 days (96 elapsed clock
hours) and 42 days (6 weeks).

**Where it stands: the script reloads cleanly and the model is wrong.** Twice. Both times the fit
learned that essentially every job takes about a year. The current working theory, and the reason
for the diagnostic script, is in section 5.

**Your job.** The operator will run a script at work and paste back the reload log. You help
interpret it and fix the script. **Neither you nor the operator can give you direct data access
from this session — you cannot query Qlik.** Everything you learn comes from `TRACE` output the
operator pastes. So prefer changes that *print more information* over changes that guess.

---

## 2. The environment

- Qlik, reading from QVD files via a library connection named **`lib://QVD-JRMC-AIM/`**.
- A second folder under it: **`lib://QVD-JRMC-AIM/ALL_TABLES/`**.
- 50 QVDs across three schemas: **AIM** (planning/scheduling, 482 fields), **COST** (actual expended
  labour and financials, 405), **MAT** (material, 293).
- **Actual expended labour does not exist in AIM.** It lives in the COST schema. Everything AIM
  holds is an *estimate*. The current script deliberately avoids COST entirely by fitting against
  actual *dates* (which AIM does have) rather than actual *labour*.
- Nuclear-related data is masked in the published layer. Do not chase it.

### Observed row counts (useful as sanity anchors)

| Stage | Rows |
|---|---|
| `AIM_Ship` filtered to the cohort | 13 |
| `AIM_Project` cohort projects | 58,717 |
| `AIM_CuPhase_Hist` certified rows | 367,450 |
| `AIM_SWLIN` | 604,198 |
| `AIM_CuPhase` after cohort + certified filter | 528,183 |
| `ALL_TABLES/JCN_CU_PHASE` bridge | 186,378 |
| Distinct Job Summaries | 28,483 |
| Single-JCN Job Summaries | 23,646 |
| Training rows after cleaning (run 2) | 17,829 |
| SWBS bins fit (run 2) | 233 |
| Candidate JCNs scored | 2,724 → 3,708 |

If a future run's numbers differ wildly from these, that itself is the finding.

---

## 3. Confirmed field names

**These are verified from an actual schema-dump reload.** The published Qlik layer uses friendly
aliases with spaces, *not* the underlying database column names. A data dictionary exists listing
1,180 fields; the names below are the ones this script touches.

### `AIM_CuPhase.qvd` — the CU-phase fact table (one row per phase of work)
```
%JO_CuPhase_Key, %CuPhase_Key, %Cu_Phase_MAT_Key, %CuPhase_Component_Key,
%Act_Proj_Key, %JobSumm_CuPhase_Key, %Package_Key,
[Cu Phase Actual Completion Date], [Cu Phase Actual Start Date],
[Cu Phase Scheduled Completion Date], [Cu Phase Scheduled Start Date],
CU_PHASE.COMP_NM, CU_PHASE_SA_ID, [CU Phase Serial], CU_SA_ID,
[Cu Phase Duration QY], [Cu Phase Est Resolution Date], EST_RESOLUTION_DT,
[Cu Phase Group CD], ICN, JO_SERIAL_ID, KEY_TASK_SERIAL_ID, KO, ICN_KO,
MANHOUR_QY, cu_phase.mod_dt, PROGRESS_RT, [Cu Phase Project ID],
[Cu Phase Prepared by Date], PHASE_REPEAT_QY, RDU_CHANGE_DT, RDU_QY,
CU_PHASE_REMARKS, CU_swlin_sys_id, [TGI Code], [Cu Phase Title],
CU_WORK_CAT_CD, WORK_TYPE_CD, WPC_NOTES_TX, WS_REASON_CD,
[Float Type Cd], [Total Float Qty], [Job Order Title], COAR, [Job Order #],
job_order.mod_dt
```
Key definitions from the dictionary:
- `ICN` = "the internal control number for a CU Phase"
- `KO` = "the key operation assignment for a CU Phase"
- `ICN_KO` = the two combined
- `CU_swlin_sys_id` = "the identifier that denotes the SWLIN system identifier"
- `[Cu Phase Group CD]` = "the code that denotes opportunity window group"
- `WORK_TYPE_CD` = O (Original), N (New Work), R (Rework) — **does not** separate planning from production
- `CU_WORK_CAT_CD` = work category for funding purposes — also not planning-vs-production

### `AIM_JB_JCN.qvd` — incoming/backlog JCNs (the scoring side)
```
%Ship_JB_JCN_Key, %JCN_Key, [JB_JCN Job Seq Num], [JB_JCN Ship Board Wrk Ctr Cd],
[JB_JCN Location ID], [JB_JCN CSMP_NM], JCN_REVIEW_CD, [JB_JCN SWLIN LI ID],
FIRST_CONTACT_MAN_NM, EQUIP_SERIAL_NUM_ID, EQUIP_NOUN_NM, APL_AEL_CD,
[JB_JCN Received Date], [JB_JCN Est Man Days Qy], [JB_JCN Avail ID], JCN_DESC_TX,
[JB_JCN Remarks Desc], SECOND_CONTACT_MAN, TYPE_AVAILABLE_CD, TYCOM_SCREENING_CD,
[JB_JCN SWLIN LI TX], POP_Start, POP_End, ACTION_TAKEN_STATUS_NM, UNIT_ID_CD,
EQUIP_ID_CD, FUND_ACT_CD, EST_MAN_DAY_COST_QY, EST_MATERIAL_COST_QY,
JCN_PRIORITY_CD, STATUS_CD, DEADLINE_DT, EST_TOTAL_COST_QY, SHIP_SYS_ID,
CDMDOA_RIN_ID, CASREP_CAT_CD, CASREP_DATE_TIME_GRP_TXT, BROKER_FUND_ACT_CD,
SWLIN_SYS_ID, SWLIN_SERIAL_ID, INITIAL_CASREP_CD
```
**There is no `Job Control Number` field on this table** — the identifier is `%JCN_Key`.
`STATUS_CD`, `TYCOM_SCREENING_CD`, `ACTION_TAKEN_STATUS_NM`, `POP_Start` / `POP_End` are the
untested candidates for an "incoming / not-yet-done" filter, which is still an open item.

### `AIM_JCN.qvd` — links phases to job control numbers
Carries **both** `%CuPhase_Key` and `%JCN_Key`, plus `[Job Control Number]`, `[JCN Status]`,
`[JCN Status CD]`, `[JCN Availability]`, `[Received Date]`. This is a direct phase→JCN link.

### `AIM_CuPhase_Hist.qvd`
Used only to identify certified (closed) phases: filter `[Approval Status CD]='CRT'` and
`[Current Flag Cd]='Y'`, keyed on `%CuPhase_Key`.

### `AIM_Ship.qvd` / `AIM_Project.qvd`
`AIM_Ship`: `%Proj_Ship_Key`, `[Ship Home]`, `[Ship Type]`.
`AIM_Project`: `[Project ID]`, `%Proj_Ship_Key`.

### `AIM_SWLIN.qvd`
`%CuPhase_Key`, `[SWLIN Line Item]`, `[SWLIN Sys ID]`, `SSI`, `[Serial ID]`, `%SWLIN_LI_KEY`,
`%SWLIN_LI_CU_Phase_Key`, `SWLIN_TITLE`, `FAC`.

### Association keys worth knowing
- `%CuPhase_Key` appears in 11 AIM tables — the main spine.
- `%JCN_Key` appears in `AIM_JB_JCN`, `AIM_JCN`, `AIM_JCN_Addition`.
- `%ICNKOP_KEY` appears in `COST_FE05` and `COST_Overhead_JON_Ref` — an ICN-plus-key-op key. Since
  AIM carries `ICN` and `KO`, this is the likely future bridge to actual labour. **Not yet tried.**

---

## 4. Qlik behaviours already discovered the hard way

Do not re-litigate these. Each one cost a reload.

1. **`$(=Peek('X',0,'T'))` does not evaluate inside `TRACE`** on this build. It prints blank and
   silently destroys your diagnostics. **Always** assign with `LET vX = Peek('X',0,'T');` first,
   then `TRACE ... $(vX);`. This single issue hid the most important number for a whole run.
2. **`FirstSortedValue()` returns NULL when two values tie on sort weight.** It was being used to
   pick a dominant code per group and may have been silently dropping groups. Replaced with a
   max-count join plus `MinString()` as a deterministic tie-break.
3. **Single-argument `Exists(FieldName)` tests against every already-loaded value of that field,
   including the table you are currently filtering.** It will match everything and look like it
   works. Use the two-argument form `Exists(SampleField, TargetField)` with a *renamed* field.
4. **`LEFT JOIN` to the JCN bridge fans out rows.** The CU-phase table went from 528,183 to 752,375
   rows, a 42% inflation, which silently over-counts any subsequent `Sum(MANHOUR_QY)`. Use a
   `MAPPING LOAD` + `ApplyMap` lookup instead of a join, or aggregate the bridge separately.
5. **Joining a coefficient table into another table while the source table still exists creates
   synthetic keys** (they shared `SWBS`, `n`, and several coefficient columns). Drop the fit tables
   immediately after the join, and capture any diagnostics from them *before* the join.
6. **The `[... Date Empty]` flag fields referenced in the data dictionary do not exist** in the
   published layer. Filter on the date fields themselves.
7. **A "successful reload with 0 errors" means nothing about correctness here.** Both failed runs
   reloaded cleanly. Always read the traces.
8. **Unverified in this environment:** `Fractile()` and `MinString()` in a script-side aggregation,
   and `LOAD ... ORDER BY <aggregate>` (that last one was removed as unsafe). If a script fails on
   one of these, substitute: `Fractile` → drop it or use `Median`; `MinString` → `Min()` if the
   codes are numeric.

### A minimal probe script
If field names are ever in doubt, have the operator run this and paste the output. It is how the
current field list was established.
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

## 5. Failure history, and the current theory

### Run 1
Reloaded cleanly. Scored 2,699 candidates and put **100% of them in the "must-do" bin**. Predicted
spans ran 366 to 733 days, with 98.4% between 360 and 372, against estimates ranging from 1 to
9,361 man-days. The fit had learned an **intercept of about 366 days and a slope near 0.04 days per
man-day**, so a 1-man-day job and a 9,361-man-day job were predicted within days of each other.

An earlier attempt in the same session had the training table load **0 rows**, because the SWBS
lookup returned blanks and a `Len(Trim(SWBS))=3` filter then rejected everything. The fix applied at
the time *relaxed the filter to let blanks through*, which did not repair the mapping — it let blank
rows train a global model instead.

### Run 2
SWBS was fixed properly by reading the code off the CU phase as `Mid(ICN, 6, 3)` instead of joining
to the SWLIN table. Result: `badSWBS=0`, training rows went 0 → 17,829, 233 bins fit, 0 synthetic
keys. Real progress.

**But the span-distribution trace printed blank** (cause: item 1 in section 4), so it is still
unknown whether the ~366-day problem is fixed. Also introduced a regression: the candidate
identifier was loaded as `[JB_JCN SWLIN LI ID]` instead of `%JCN_Key`, so output could not be traced
back to individual jobs.

### The current theory — and it is the operator's, and it is probably right

**The span is being measured from the wrong starting point.** The script computes a job's span as
`Max(actual completion) − Min(actual start)` across all the CU phases belonging to a job. But a
job's phases are not all production work: the **`KO` (key operation) code distinguishes them, and
`S01` is typically a planning phase**. A planning phase starts long before production does. So the
"span" being measured runs from *planning start* to *production finish*, which is exactly the shape
that produces a ~366-day intercept.

If this is right, the correct definition is the **envelope across an ICN's production phases only**:
earliest production start to latest production finish, planning excluded. Note this is deliberately
*not* "the longest single phase," because a job with three production phases spread over three weeks
should score three weeks, not the length of its biggest phase.

**This has not yet been confirmed against data.** That is what the diagnostic script exists to do.

---

## 6. What the operator is running, and in what order

### Step 1 — `phase-anatomy-diagnostic.md` (run this first)
Fits nothing, screens nothing. It exists purely to answer "which phases are production?" It prints:

- `[cardinality]` — counts of phases, distinct ICNs, distinct JCNs, distinct Job Summaries, plus how
  many ICNs a JCN spans and vice versa. Tells us whether ICN is the right grouping grain.
- `[ko-profile]` — one line per `KO` code: phase count, distinct ICNs, median man-hours, median
  phase span, and **median days after its ICN's first start**. This is the money output. A planning
  phase should show a near-zero offset and low man-hours.
- `[sample]` — up to 8 complete ICNs dumped phase by phase in date order with code, title, dates,
  span, man-hours. For eyeballing real jobs.
- `[spancompare]` — median and 90th percentile span per ICN three ways: all phases, production only
  (excluding whatever `KO` codes are listed in the `vPlanKO` variable), and the old Job-Summary
  envelope.
- `[swbs]` — whether SWBS derived from `CU_swlin_sys_id` agrees with SWBS derived from
  `Mid(ICN,6,3)`, and how many of each are malformed.

**Expected if the theory is right:** all-phase median in the hundreds of days, production-only
median in the tens or less, and one or more `KO` codes sitting at offset ~0 with low man-hours.

### Step 2 — `_lineage/span-screen-v3.md`
The actual screen. Computes three span definitions at once (full envelope, longest single phase, sum
of phase-days), fits each per SWBS in both linear and median form, and prints the bin distribution
under each. Once step 1 identifies the planning codes, this gains a fourth definition (production
envelope) and the other three become controls.

Both files are in the same folder as this one and contain the full scripts in fenced code blocks.

---

## 7. Failure triage — symptom to next move

| Symptom | Most likely cause | What to do |
|---|---|---|
| A `TRACE` line prints blank | `$(=Peek(...))` used inside `TRACE` | Convert to `LET` first (section 4, item 1) |
| `Field 'X' not found` | Dictionary name used instead of the published alias | Run the probe script in section 4 and match exactly |
| A table loads 0 rows | A `WHERE` filter rejecting everything, usually a code-format mismatch | Load the table *without* the filter, `TRACE` a few sample values of the filtered field, compare formats |
| Synthetic keys reported | Two tables sharing 2+ field names | Rename fields on one side, or drop the source table right after joining |
| Row count inflates after a `JOIN` | One-to-many fan-out | Replace the join with `MAPPING LOAD` + `ApplyMap`, or pre-aggregate |
| Predicted spans all nearly identical | Everything is falling through to the global fit | Check how many candidates matched a per-group fit; if near zero, the two sides' group codes disagree |
| Predictions are all one bin | Intercept dominates the slope | This is the known failure. Check the span distribution before touching anything else |
| `Fractile` / `MinString` errors | Function unsupported in script aggregation on this build | Substitute per section 4, item 8 |

**General principle for this system:** when something is wrong, the fastest path is almost always to
print the distribution of the suspect field rather than to reason about it. Two runs were lost to
reasoning about values nobody had looked at.

---

## 8. Things already ruled out — do not suggest these

- **"The reload has an error."** It does not. Both failed runs completed with 0 forced errors.
- **"Use the `ACTUAL_START_DATE` / `ACTUAL_COMPLETION_DATE` raw column names."** They are not in the
  published layer. The aliases with spaces are correct.
- **"Filter on the date-empty flag fields."** Those fields do not exist.
- **"Relax the SWBS filter so rows get through."** This was tried. It converts a loud failure into a
  silent one by letting blank-coded rows train a global model.
- **"Join `AIM_SWLIN` on `%CuPhase_Key` to get the SWBS."** Tried; produced blanks for most phases.
  `CU_swlin_sys_id` sits directly on the CU phase and is the better source.
- **"Pull actual labour hours from AIM."** They are not there; they are in the COST schema.
- **A previous assistant session invented a nonexistent "Qlik linter" tool.** Do not propose tooling
  that has not been verified to exist. If you are unsure whether a Qlik function is available on
  this build, say so and offer a fallback.

---

## 9. Open design questions — surface these, do not decide them

These are the operator's calls. If your fix depends on one, stop and ask.

1. **What interval should the span measure?** Production envelope per ICN is the leading theory but
   is unconfirmed. Alternatives are the full envelope, the longest single phase, and the sum of
   phase durations.
2. **Which `KO` codes are planning?** `S01` is the operator's expectation. The diagnostic exists to
   confirm and to find any others.
3. **Group at ICN or at Job Summary?** The script currently groups at Job Summary and filters to
   single-JCN summaries. The `[cardinality]` trace informs this.
4. **The training and scoring estimates are different fields.** Training uses `MANHOUR_QY / 8` from
   the CU-phase level; scoring uses `[JB_JCN Est Man Days Qy]` at JCN level. These are different
   estimates at different grains, so the model is fit on one scale and applied to another. Fixing it
   properly means joining history to the induction-grade estimate, which is a larger change.
5. **How to filter candidates to genuinely incoming work.** Currently the only filter is
   `[JB_JCN Est Man Days Qy] > 0`, which scores the entire backlog.
6. **How much margin below 4 days the "96-hour" bin should require.** 96 hours has been defined as
   96 *elapsed clock* hours, so 4 calendar days including nights and weekends. That makes the test
   sensitive to which day of the week a job starts, which is unknown at screening time, so a bare
   `predicted <= 4` will over-promise.

---

## 10. Useful constants

- `96 hours` = **4 calendar days**, elapsed clock, weekends included. Confirmed decision.
- `6-week CMAV` = **42 calendar days**.
- Marginal band currently `1.25 ×` the CMAV threshold.
- A SWBS group needs `n >= 8` completed jobs before its own fit is trusted; otherwise the script
  falls back to the 1-digit parent group, then to a global fit.
- Man-day conversion currently assumes **8 man-hours per man-day**. Unverified against the system's
  own convention.

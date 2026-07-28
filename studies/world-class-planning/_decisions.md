---
type: decision-log
study: world-class-planning
classification: internal
created: 2026-06-23
---

# Decisions and direction

A running log of where the thinking has settled and what's still open. This is a thinking
project — "decisions" here are direction, not commitments.

## Settled direction (as of 2026-06-23)

1. **Frame.** The brief is world-class planning's shift from Cost-As-Independent-Variable to
   Schedule-As-Independent-Variable; the concrete question is a consistent early screen of
   incoming work against: 96-hour close-out? / 6-week CMAV fit? / splittable across windows? —
   done in AIM, which SRF uses and the other RMCs (on NMD) don't.
2. **The screen mostly already exists in SRF policy.** CMAV (2–6 wks) and the multi-WOO split are
   defined in 4700.1F; the 96-hour question is **not** in SRF's documents (fire-safety threshold
   only) and must be defined locally if adopted.
3. **Screen super early — at JCN induction.** Consequence: it runs before AIM's planned duration
   exists, on the brokered Class F (±40%) estimate plus history. Design it as a **three-bin sort**
   (deferrable / must-do / marginal), not a yes/no.
4. **Lead with the drydock cut.** Structural, readable at induction, needs no duration estimate,
   decides much of the "must-do" list on its own.
5. **Attribute labor, not span.** Labor adds up across bundled JCNs; Cycle Time does not. Recover
   per-JCN **labor** from history; convert to span downstream.
6. **Two estimation methods.** Simple: job-costing allocation (direct-attribute mappable CU Phases,
   allocate shared phases by Class F man-hours). Rigorous: regression disaggregation across all
   Job Summaries (recover per-bin labor, or a per-bin actual-to-estimate multiplier = PfCw, with
   confidence). Both in [estimate-attribution](02_synthesis/estimate-attribution.md).
7. **Predict standalone span for the screen** (conservative); calibrate the span conversion on
   clean one-JCN history; use bundled history only for labor.
8. **OSI-clean.** All sources are Distribution A.
9. **Bin at SWBS 3-digit (~100 bins); solve for a multiplier, not man-days.** Operator: the bundles
   live at the Ship Work Breakdown Structure (SWBS) level — the first three digits of the SWLIN,
   ~100 groups. Solve each bin for its **performance multiplier** (actual ÷ estimated labor =
   PfCw), which is size-independent, so the Class F estimate carries the size and ~100 bins is
   enough. Same-SWBS bundles then self-solve (total actual ÷ total Class F = the multiplier);
   regression is only for cross-SWBS bundles. Thin bins shrink toward the 1-digit SWBS parent.
10. **Two explicit conversions** (the gap the operator flagged): (1) estimate → expected actual
    labor = Class F × bin multiplier; (2) labor → span = a per-bin span model from clean one-JCN
    Cycle Time ≈ fixed wait (cure/test) + labor ÷ (crew × shifts/day). Span has a big non-labor
    component, so dividing labor by crew is not enough. Shortcut: where a bin has rich clean
    one-JCN span data, model Cycle Time directly and skip the labor middleman.
11. **Validate:** the multiplier is roughly constant within a SWBS group (split by size if not).
12. **The SWBS Σ/Σ trick — no per-JCN attribution needed for the multiplier.** Multiplier =
    Σ(actual labor, AQWP) ÷ Σ(estimate) by SWBS; both sides sum to SWBS independently (CU Phases
    carry the SWLIN), so bundles never have to be pulled apart in the tool. Per-JCN attribution
    only returns for cross-SWBS sprawl or if per-JCN detail is wanted.
13. **Pull at the CU-Phase / Key-Op grain.** A fact table (one row per CU Phase) joined to a JCN
    dimension table on JCN. Calibrate on **closed (certified) work only**; basis = actual ÷ Class F
    where Class F is retained, else actual ÷ QAC (note the planning-refinement gap). Span model
    fit from **single-JCN summaries only**. Full field list in
    `03_build/data-fields-and-tooling.md`.
14. **Tooling:** Excel (Power Query to pull/join/derive; Power Pivot Data Model for the multiplier
    measure; pivot by SWBS with the count + shrink-to-parent) or QlikView (associative model; set
    analysis for closed work). Excel to lock the model; QlikView to explore.
15. **Actuals are in the COST/STARS schema, not AIM (2026-06-23, from the operator's Qlik pull).**
    AIM_* carries only estimates (`MANHOUR_QY`, `MANHOUR_EST_QY`, `EST_MAN_DAYS_QY`); actual
    expended labor is `COST_FJ40` (straight+OT+holiday hours by Job Order) / `COST_FE75` (keyop
    closed-to-labor). The multiplier therefore needs an **AIM↔COST join on Job Order / Key Op**
    (this is what defeated the Gemini session — it reused one AIM estimate field as both sides →
    multiplier 1.0). Actual *span* is in AIM (`ACTUAL_START_DATE`/`ACTUAL_COMPLETION_DATE`).
    **Shortcut:** fit `actual span ≈ f(EST_MAN_DAYS_QY)` per SWBS from completed single-JCN
    summaries — no COST actual-labor needed for a first cut. Real field map + join in
    `03_build/data-fields-and-tooling.md`. NNPI is masked in the published AIM layer.

16. **First-cut screen written as a QlikView script (2026-06-23):** `03_build/span-screen-qlik.md` —
    the span-fit-per-SWBS shortcut (no COST join). Fits `span ≈ Intercept + Slope × EstManDays` per
    SWBS from completed single-JCN history (LINEST_M/B, shrink thin bins to the 1-digit parent),
    scores candidates, three-bin sort. Carries a [CONFIRM] list for the inferred keys/fields/units.
    Operator cleared the raw Qlik artifacts for the vault — now in `01_sources/qlik/`. Next:
    drydock override, then the AIM↔COST multiplier. **History pools ALL availability types** (CNO +
    CMAV + CM + EM + WOO) per operator — the CNO-only filter from the example MRQT script was
    removed; "completed" is enforced at the CU-phase level (certified + actual dates), not by a
    CNO-specific CA00 cohort.
17. **Test harness written (2026-06-23):** `03_build/span-screen-tests.md` — a diagnostic TRACE
    block (stage counts + data-quality flags to the reload log), six validation sheet objects
    (incl. the per-SWBS scatter to choose linear-fit vs median), and acceptance criteria that map
    each red number back to the right [CONFIRM]. Operator to run the fit next.
18. **Future-state captured (2026-06-24):** `future-state.md` — a **Power App** screening
    calculator where a user pastes JCN/SWLIN/est-man-days and gets a span + verdict. Design
    principle: **decouple** — the Qlik fit exports a small per-SWBS coefficient table (SWBS →
    Slope/Intercept/n + parent/global + thresholds) to SharePoint/Dataverse; the app is a thin
    paste-and-predict calculator over it, re-fit on a cadence. Depends on a validated fit + the
    drydock input + the "96 hours" definition. (Excel/Power BI are lighter alternatives.)
19. **Who authors and maintains AIM-NG is an open question, and it bears on end state
    (2026-07-26).** The study has treated the AIM-NG process manual as a given: a stable
    Distribution A framework to build a screen inside. It has never asked who wrote those eleven
    chapters, who maintains the shipyard metric suite that accompanies them, or who delivers the
    project-management training built on them. That matters, because SRF-JRMC is an AIM user that
    is **not** one of the four public naval shipyards the manual was written around. If the process
    framework, its metrics, and its training are authored and sustained by an identifiable party
    under a NAVSEA sponsor, then a schedule-driven early work screen at SRF-JRMC is not only an
    SRF-internal improvement; it is an **extension of an existing process framework to a
    forward-deployed repair facility**, which is a different and more specific end state than the
    three the project-intent question currently offers. **Nothing is settled here.** The next step
    is cheap: check the front matter, record-of-changes, and title pages of the AIM-NG chapter PDFs
    already in the Drive `AIM NG` folder for a preparer or support-contractor credit, and check
    USAspending for maintenance-and-process support obligations under the relevant NAVSEA sponsor
    (`lib/usaspending.py`). Both are open sources and would settle it either way. *(This question
    was prompted by non-OSI material held in `_private/`, which is not citable and has not been
    relied on for anything above. If the open-source check comes back empty, the question stays
    open rather than being answered from the private material.)*

20. **Item 19 checked, and it splits (2026-07-26).** Both open-source checks were run. Result: the
    *governance* half is confirmed and the *contractor-attribution* half is not.
    - **FACT (AIM-NG Chapter 1A, §1.1 "Purpose and Scope," Rev 7 — already in the source ledger,
      Distribution A).** The AIM-NG Process Manual is developed "under the sponsorship of Naval Sea
      Systems Command, Industrial Operations Directorate (SEA 04X)," by the **Ship Maintenance
      Performance Group (SMPG)** together with the **Project Management National Value Stream
      (PM NVS)**. The same section names SMPG "as Champion for the AIM-NG Process, training, and
      software functional requirements," and states that all chapters except Resource Allocation
      are "developed and managed by the PM NVS." So the framework, its training, and its software
      requirements have a single identifiable owner under a NAVSEA sponsor. This was sitting in a
      document the study has cited since day one; it was simply never asked.
    - **NOT ESTABLISHED.** Who staffs or supports SMPG. Chapter 1A names no contractor (its only
      "contractor" references are to ship-repair contractors as a work category). USAspending
      returns **zero** awards on "Ship Maintenance Performance Group," "AIM-NG," "Project
      Management National Value Stream," or "naval shipyard project management process." Queries
      were run on process vocabulary only, deliberately not on any company name, since seeding a
      name and then calling the matches organic is the contamination pattern the vault's
      entity-provenance rules forbid.
    - **Incidental OSI finding, worth keeping.** "Advanced Industrial Management" does return a
      cluster of Navy awards, but they are a *different work-type*: planning-yard marine design and
      engineering task orders to prepare AIM planning and technical work documents and staff
      project trouble desks, at Pearl Harbor Naval Shipyard and Puget Sound Naval Shipyard and IMF.
      Recipients surfaced organically by that query were Life Cycle Engineering, Gryphon Marine,
      and HII Fleet Support Group. **Assessment:** there are two distinguishable layers around AIM,
      an *authorship/governance* layer (SMPG / PM NVS under SEA 04X) and a *work-document
      production* layer (planning-yard task orders at individual shipyards). Conflating them would
      be an analytical error. The second layer is visible in procurement data; the first is not.
    - **Consequence for the fourth end state.** It is still available but still unresolved. The
      framework demonstrably has an owner and a sponsor, which is what the "extension to a
      forward-deployed repair facility" framing needs. Who would actually perform such an extension
      remains unsourced, and per the crossing rule in `_private/README.md` it does not get filled in
      from non-OSI material. Next open-source avenue if the operator wants it pursued: FPDS or
      USAspending by NAISC/PSC under the SEA 04X sponsor rather than by keyword, or SMPG's own
      published materials if any exist.

21. **"96 hours" defined: elapsed clock hours (operator, 2026-07-26).** Not work-shifts. Ninety-six
    elapsed hours is **four calendar days**, with the clock running through nights, weekends, and
    holidays. Since the threshold appears nowhere in 4700.1F, this is a **local SRF definition**
    and the operator is its source. Consequences, worked through in
    [early-jcn-screen](02_synthesis/early-jcn-screen.md) under "The unit definition, settled":
    - **No conversion needed, and the `[CONFIRM]` on `v96Days` is closed.** AIM Cycle Time is
      claimed actual start to claimed actual finish, and the fit uses
      `Max(ACTUAL_COMPLETION) − Min(ACTUAL_START)`, so both the history and the threshold are on
      the same elapsed clock. Weekend and holiday effects are already inside the fitted history.
      `v96Days = 4` in `03_build/span-screen-qlik.md` is now confirmed rather than a placeholder.
    - **Assessment: the 96-hour bin is governed by the per-SWBS Intercept, not the Slope.** The
      intercept is the fixed-wait floor for a work type. Where it alone exceeds four days, nothing
      in that SWBS group can pass at any size and the estimate stops mattering. So the first
      question is better read as *which SWBS groups are 96-hour-capable at all*, with the per-job
      estimate discriminating only inside those groups. This also gives the validation scatter in
      `03_build/span-screen-tests.md` a sharper job: the intercept per bin is now a headline
      output, not a fitting by-product.
    - **Assessment: the test is start-day sensitive, and the start day is unknown at induction.**
      A four-day elapsed window starting Friday eats a weekend; starting Monday it does not. Since
      decision 3 puts this screen at Job Control Number induction, the sort should require a margin
      below four days rather than comparing against the central fit, or the "96-hour capable" bin
      will over-promise on jobs that land badly in the week.

22. **First live run: the screen reloads cleanly and the output is unusable (2026-07-26).** The
    operator ran the span screen against the live Qlik model, debugging field names with Gemini
    along the way (transcript and output in `03_build/`: `Recent Gemini`,
    `SWBS Sample Output.xlsx`). Real progress was made and the schema is now pinned down (see the
    updated `[CONFIRM]` list in `03_build/span-screen-qlik.md`). But the result must not be treated
    as a fit.
    - **What the output says.** 2,699 candidate JCNs scored, **100% in `MUST-DO - exceeds CMAV`**.
      Zero reached the 96-hour or CMAV bins. Predicted spans run 366.4 to 733.3 days, with 98.4%
      between 360 and 372, against estimates from 1 to 9,361 man-days. A screen that puts every job
      in one bin is not screening.
    - **Diagnosis.** The fit did run; this is not a null artifact. It learned an **intercept of
      about 366 days and a slope near 0.04 days per man-day**, so the fixed term swamps the
      estimate entirely and a 1-man-day job and a 9,361-man-day job are predicted within days of
      each other. The intercept is a year because `Span_Days = Max(ACC) − Min(ACS)` over all CU
      phases on a Job Summary is **not the job's execution window**. It is the distance from the
      earliest actual start to the latest actual completion across phases that evidently stretch
      over the availability lifecycle, planning included. **Assessment:** the model is measuring the
      wrong interval, correctly. That is why it reloads with zero errors and still tells you
      nothing.
    - **Three defects to fix before re-running, in priority order.**
      1. **SWBS is not mapping on the history side.** `Left(ApplyMap('Map_SWLIN', %CuPhase_Key, ''), 3)`
         returns blank for most CU phases. The first run failed loudly on this (`JS_Clean` loaded
         **0 rows**, which emptied all three fit tables). The fix applied in the session **relaxed
         the filter to let blank-SWBS rows through**, which does not repair the mapping, it hides
         it: blanks now train the global model while the per-SWBS bins stay starved, and nearly
         every candidate falls through to the global fit. **That relaxation should be reverted**,
         and the CU-phase-to-SWLIN join diagnosed instead. The candidate side maps SWBS fine from
         `JB_JCN SWLIN LI ID`, so the data exists; the CU-phase-keyed lookup is the broken link.
      2. **`Span_Days > 0` silently deletes same-day jobs** — which is precisely the
         96-hour-capable population that item 21 says the intercept governs. Every job that starts
         and finishes on one day is dropped from training, biasing the intercept upward and making
         the 96-hour bin under-populated by construction. Span should be an inclusive day count
         (`ACC − ACS + 1`) or use `>= 0` with a floor. **This is our defect, present in the script
         since it was written, not something the run introduced.**
      3. **The estimate basis differs between training and scoring.** Training fits on
         `Sum(MANHOUR_QY)/8`, a CU-phase planning estimate converted to man-days. Scoring uses
         `JB_JCN Est Man Days Qy`, the JCN-grain induction estimate. Those are different estimates
         at different grains, so the model is fit on one scale and applied to another.
         `03_build/data-fields-and-tooling.md` already flags this hazard for the multiplier
         ("your screen input (Class F) and your calibration base (QAC) differ"); the same hazard is
         in the span script and was never resolved. **This one needs an operator decision**, since
         the two options differ in effort: join history JCNs to their Class F estimate so training
         and scoring share a basis, or accept the mismatch and document the bias.
    - **Process note.** `03_build/span-screen-tests.md` was written for exactly this. Its TRACE
      block prints `singleJCNjobs=` and a `badSWBS=` count, either of which would have shown the
      0-row collapse and the SWBS mapping failure in one line. It was not run. **Run the harness
      first next time, before reading any output.**
    - **Also open:** the candidate filter is only `Est Man Days Qy > 0`, so the run scored the whole
      backlog rather than incoming work; and the session reported 3 synthetic keys, since resolved
      by renaming the training fields.

23. **Second live run (2026-07-27): real repairs, but the verdict number still did not print.**
    Files: `03_build/Latest Script`, `03_build/latest output`, `03_build/QLIK_Tables`. This run is a
    clear step forward and it is still not a trustworthy fit.
    - **Genuinely fixed.** The SWBS mapping now works: `Map_SWLIN` was abandoned in favour of
      pulling the code straight off the CU phase as `Mid(ICN, 6, 3)`, and the diagnostic confirms
      **`badSWBS=0`** of 752,375 rows. `JS_Clean` went from 0 to **17,829** single-JCN summaries,
      **233** SWBS bins fit, 9 parent bins, and the run finished with **0 synthetic keys**. The
      relaxed blank-SWBS filter from run 1 is no longer doing the work, so item 22's first defect
      is genuinely closed rather than hidden. The test harness from `span-screen-tests.md` was also
      embedded and run this time, which is how we know any of this.
    - **The blocking unknown.** `[history] span days min/med/max =` printed **blank**, as did the
      whole `[fit] bins= trusted= negIntercept= negSlope=` line. Cause is known and harmless: the
      `$(=Peek(...))` form does not evaluate inside `TRACE` on this Qlik build, which is the exact
      caveat already written at the bottom of `span-screen-tests.md`. Replace those two lines with
      `LET` assignments like the ones above them. **Until the span range prints, we cannot say
      whether the ~366-day intercept from item 22 is fixed**, and that single number decides
      whether anything else here matters. Do this first; it is a five-minute change.
    - **New defect, and it is significant.** In section 8 the candidate identifier is loaded as
      `[JB_JCN SWLIN LI ID] AS JCN`. That is the SWLIN line-item code, **not** the job control
      number; run 1 correctly used `%JCN_Key`. As written, the output cannot be traced back to
      individual jobs and distinct JCNs sharing a SWLIN collapse together. Revert to `%JCN_Key`.
    - **New risk: the two sides may not speak the same SWBS.** Training derives SWBS as
      `Mid(ICN, 6, 3)` from `AIM_CuPhase`; scoring derives it as `Left(SWLIN_SYS_ID, 3)` from
      `AIM_JB_JCN`. Different fields, different tables, different derivations. If the two code
      spaces do not coincide, every candidate lookup misses, everything falls through to the global
      fit, and the screen reproduces run 1's flat behaviour for an entirely different reason.
      **Assessment:** the bin count is mild evidence of trouble already, since 233 three-character
      values is roughly double the ~100 SWBS groups decision 9 expects, which suggests
      `Mid(ICN,6,3)` is picking up more than the SWBS. Diagnostic: list the distinct values on both
      sides and count how many candidates hit a per-SWBS fit rather than falling through.
    - **Probable inflation of the training estimate.** `CuPhase_T` loads 528,183 rows but the
      diagnostic counts **752,375** after the `LEFT JOIN` to the JCN bridge, so CU phases with
      multiple bridge rows are duplicated. `Sum(Est_MH)` then over-counts man-hours, which biases
      the slope down and lets the intercept dominate. Check `Count(CU_PHASE_SA_ID)` against
      `Count(DISTINCT CU_PHASE_SA_ID)` and de-duplicate before the roll-up.
    - **Carried over from item 22, still unfixed.** `Span_Days > 0` still deletes same-day jobs, and
      the cost is now measurable: `JS_History` 23,646 to `JS_Clean` 17,829, so **5,817 summaries,
      about a quarter of the training set, are being discarded** between those two steps. The
      same-day jobs among them are the 96-hour population item 21 identified. The
      training-versus-scoring estimate-basis mismatch is also unchanged. And `negSpan=72` CU phases
      complete before they start, which should be filtered explicitly rather than left to
      `Max`/`Min`.
    - **Recommended order:** print the span range, fix the JCN field, prove the SWBS code spaces
      match, then de-duplicate the bridge, then the same-day and basis questions.

24. **The planning-phase hypothesis, and a proper field inventory (2026-07-27).** The operator's
    read: the JCN is tied across an ICN's phases, and not all phases are production — `S01` is
    typically the planning phase. **Assessment: this very likely explains the ~366-day intercept
    outright.** An envelope from earliest phase start to latest phase finish begins at *planning*,
    so items 22 and 23 were measuring planning-through-delivery and calling it execution span. It
    is also a better hypothesis than the "longest single phase" variant in `span-screen-v3.md`,
    because it preserves a genuine multi-phase production window instead of collapsing it to one
    phase. Target definition is therefore probably **the production envelope per ICN**. Not
    hard-coding `S01` on "usually": `03_build/phase-anatomy-diagnostic.md` prints every key
    operation's behavioural fingerprint (count, median man-hours, median span, and median day
    offset from its ICN's first start) plus a phase-by-phase dump of sample ICNs, so the planning
    codes identify themselves before anything is excluded.
    - **`03_build/qvd-field-inventory.md` now exists** — all 50 QVDs and 1,180 fields with source
      and definition, generated from `01_sources/qlik/QLIK Data Dictionary.xlsx`, plus a
      cross-reference of the 59 `%` association keys showing which tables each one links. This is
      the "what can actually join to what" reference the build has been missing.
    - **Better links found in that inventory, all three replacing something we were doing worse.**
      (a) **`AIM_JCN` carries `%CuPhase_Key` and `%JCN_Key` together**, so it maps phases to job
      control numbers directly; the `ALL_TABLES/JCN_CU_PHASE.qvd` bridge is what inflated the
      CU-phase table by 42% (item 23). It also carries `JCN Status` and `JCN Availability`, which
      is the open/active candidate filter still outstanding since item 22.
      (b) **`CU_swlin_sys_id` sits directly on `AIM_CuPhase`**, defined as the SWLIN system
      identifier — the same concept as `SWLIN_SYS_ID` on `AIM_JB_JCN`. Deriving SWBS from one field
      on both sides makes the code spaces match by construction, which retires the item 23 risk
      more cleanly than reconciling `Mid(ICN,6,3)` against `Left(SWLIN_SYS_ID,3)`.
      (c) **`%ICNKOP_KEY` exists on `COST_FE05` and `COST_Overhead_JON_Ref`** — an ICN-plus-key-op
      key on the COST side. AIM carries `ICN` and `KO`, so this is a candidate bridge for the
      AIM↔COST join the multiplier work needs (item 15). Not chased yet, but recorded.
    - **Incidental, and worth its own look later:** `Cu Phase Group CD` is defined as "the code that
      denotes opportunity window group." The third screening question is whether work can be broken
      across windows of opportunity, and there may already be a field carrying that grouping.
    - **Sequencing decision.** The diagnostic runs *before* any more fitting. Two runs have now
      produced clean reloads and unusable models because the span definition was wrong; a third
      guess is worse value than one run that shows what the phases actually are.

25. **THE SCREEN WORKS (2026-07-28). First usable output, and it exposes the next real problem.**
    The operator fixed the `vPlanKO` quoting (`'''S01'''`, so the `Match()` expansion resolves),
    repaired the load errors, and ran v3 to completion. Output is `03_build/New table.xlsx`, 3,708
    candidates scored. **The ~366-day intercept is gone.** Predictions now vary by job, 3,600 of
    3,708 candidates score off their own SWBS fit rather than falling through to a parent or global
    fit, and the bins genuinely discriminate. Items 22 and 23 are closed.
    - **Bin distributions.** Envelope: 1% within 96 hours, 14% CMAV-capable, 45% marginal, 40%
      must-do. Longest-phase: 0% / 73% / 11% / 16%. Sum-of-phases: 1% / 8% / 3% / 88%.
    - **Drop the sum-of-phase-days definition.** It puts 88% in must-do and its maximum prediction
      is 5,222 days. It double-counts phases that overlap in time, which is most of them. Dead end;
      keep it only as a control.
    - **Longest-phase currently looks the most usable**, median prediction 32 days against the
      envelope's 50. But neither is validated yet, and the production-envelope definition (item 24)
      is still not implemented, so the real comparison has not happened.
26. **The model is effectively a SWBS lookup table (2026-07-28) — this is now the central problem.**
    The operator's observation, that each SWBS holds many jobs with widely varying spans, is correct
    and measurable in the output.
    - **The estimate barely moves the prediction.** Correlation between estimated man-days and
      predicted span is **0.22** for longest-phase, 0.28 for envelope. The interquartile range of
      the envelope prediction is 49 to 64 days, so for most jobs the model says "about fifty days"
      regardless of size.
    - **For 64 of 162 SWBS groups, predictions vary by less than one day across every job in the
      group**, including groups whose estimates range from 1 to 100 man-days. In those groups the
      model is a constant.
    - **One bin dominates.** SWBS 123 holds 1,566 of 3,708 candidates, 42% of the whole backlog.
      Any accuracy claim about the screen is mostly a claim about that one group.
    - **Assessment: size is not the missing variable, and adding more size-like precision will not
      help.** Span is being driven by something the model cannot see. The candidates worth testing
      are material lead time, work center, casualty-report urgency, and availability type.
    - **Method warning: do not nest bins.** With 162 SWBS groups over ~17,800 training rows, and a
      minimum of 8 jobs before a group's own fit is trusted, splitting SWBS by a second dimension
      multiplicatively starves the cells. The right shape is a **global adjustment factor per
      dimension**: fit `actual ÷ SWBS-median` across all SWBS at once, then apply the factors on top
      of the SWBS prediction. Each factor then has thousands of observations behind it instead of a
      handful.
    - **Callback to decision 16.** History deliberately pools **all** availability types (CNO, CMAV,
      CM, EM, WOO). A job executed inside a year-long CNO availability and the same job executed in
      a 6-week CMAV have structurally different spans, so that pooling is a strong candidate for a
      large share of the within-SWBS variance now visible. Segmenting or adjusting by
      `TYPE_AVAILABLE_CD` may be the single highest-value change available.
27. **The JCN column is not a JCN (2026-07-28).** Operator-reported and confirmed: the current
    script loads `%JCN_Key AS JCN`, and the output column contains values like `8-130758`. Run 1
    produced values like `AP40L467` from the same field name, so the association is resolving
    differently now. **`%JCN_Key` is a Qlik surrogate key, not the readable Job Control Number.**
    The readable field is `[Job Control Number]` on `AIM_JCN.qvd`, which also carries `%JCN_Key`, so
    the fix is a lookup from the candidate table into `AIM_JCN` rather than displaying the key.
    Before committing to that, print candidates: dump five rows showing `%JCN_Key`,
    `[JB_JCN Job Seq Num]`, `JCN_DESC_TX` and the joined `[Job Control Number]` side by side and
    pick the one that looks like a job control number. Without a real JCN the output cannot be
    handed to a planner, so this blocks use even though it does not affect the model.

## Open questions (operator's to resolve)
- **Data reach:** largely answered (item 15). Cycle Time (AIM `ACTUAL_*_DATE`), estimates
  (`EST_MAN_DAYS_QY` / `MANHOUR_QY`), SWLIN, drydock, crew, and the certified filter are all
  reachable in the operator's Qlik QVDs. The one piece needing work: the **AIM↔COST/STARS join on
  Job Order/Key Op** to pull actual labor — and confirm the keyop join lines up across the two
  systems.
- **Bundle level:** answered — bundles are at SWBS 3-digit (item 9). Remaining: does the
  per-SWBS multiplier hold across sizes, or do big jobs in a group run at a different ratio
  (→ split that group by size)?
- **What interval should `Span_Days` actually measure? (new 2026-07-26, item 22 — the blocker.)**
  The first live run learned a ~366-day intercept because the current definition spans a Job
  Summary's whole phase history rather than its execution window. Options: restrict to execution
  CU phases only (needs a phase-type or work-category filter, `CU_WORK_CAT_CD` / `WORK_TYPE_CD`
  are both present); use the longest single-phase span rather than the summary envelope; or keep
  the envelope and accept it measures something else. This is a **method** decision, not a code
  fix, and nothing downstream is trustworthy until it is made.
- **Training/scoring estimate basis (new 2026-07-26, item 22).** Fit on CU-phase `MANHOUR_QY`/8 and
  score on JCN `Est Man Days Qy`, or join history to Class F so both sides share a basis? Effort
  differs materially; the second is more correct.
- ~~**"96 hours":** define it (elapsed clock hours vs. work-shifts).~~ **ANSWERED 2026-07-26
  (item 21): elapsed clock hours, four calendar days, local SRF definition.** What remains is a
  design choice rather than a definition: how much margin below four days the "96-hour capable"
  bin should require, given that the start day is unknown at induction. Item 21 recommends a
  margin; the size of it is the operator's call and is best set after the fit is run and the
  per-SWBS intercepts are visible.
- **Where the screen runs:** fold into the existing Shop Screening Process (§9), or stand it up
  separately?
- **Project intent:** is the end state a thinking memo, a method/spec SRF could implement, or a
  brief to present? (Drives whether this stays a thinking track or grows a build.) **Item 19 adds
  a fourth candidate** — a demonstration that the AIM-NG framework extends to a forward-deployed
  repair facility — but that one only becomes available if the authorship question closes on open
  sources, and it carries an organizational-conflict-of-interest question that
  `_meta/oci-primer.md` would have to test first.
- **AIM-NG authorship and maintenance (new 2026-07-26, item 19):** who wrote the chapters, who
  sustains the metric suite, who teaches the associated course. Two cheap open-source checks named
  in item 19. Until one of them lands, the fourth end-state option above is not on the table.

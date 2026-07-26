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

## Open questions (operator's to resolve)
- **Data reach:** largely answered (item 15). Cycle Time (AIM `ACTUAL_*_DATE`), estimates
  (`EST_MAN_DAYS_QY` / `MANHOUR_QY`), SWLIN, drydock, crew, and the certified filter are all
  reachable in the operator's Qlik QVDs. The one piece needing work: the **AIM↔COST/STARS join on
  Job Order/Key Op** to pull actual labor — and confirm the keyop join lines up across the two
  systems.
- **Bundle level:** answered — bundles are at SWBS 3-digit (item 9). Remaining: does the
  per-SWBS multiplier hold across sizes, or do big jobs in a group run at a different ratio
  (→ split that group by size)?
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

---
name: project-world-class-planning
description: thinking project on schedule-as-independent-variable early work screening in AIM; the bundled-JCN attribution problem and the labor-vs-span method
metadata: 
  node_type: memory
  type: project
  originSessionId: f85e879c-0691-46b5-a1af-9c6f26ff57cd
---

New `studies/world-class-planning/` track (created 2026-06-23) — a **thinking project**, not a
delivery pipeline. Topic: a "world-class planning" brief on shifting from Cost-As-Independent-
Variable (CAIV) to Schedule-As-Independent-Variable (SAIV). The other RMCs will screen incoming
work for a CNO availability against three questions — 96-hr close-out? / 6-wk CMAV fit? /
splittable across windows of opportunity? — and SRF-JRMC wants to answer them consistently in
**AIM (Advanced Industrial Management)**, which SRF uses while the other RMCs use NMD.

Grounded in 13 **Distribution-A** (public) docs in the operator's Drive `AIM NG` folder
(ID `1ux5NHt1txSvgCDej4jr64L3J6qDiiMeQ`): AIM-NG chapters 01A–11A + NAVSHIPREPFACINST 4700.1F +
the C200 Process Guide. All read.

Key conclusions so far: CMAV (2–6 wks) and the multi-WOO split are already defined in SRF's own
4700.1F; **"96 hours" is NOT** in SRF docs (fire-safety threshold only — must be defined locally).
**Decision: screen super-early at JCN induction** → runs on the brokered Class F (±40%) estimate
+ history, before AIM's planned duration exists; design as a **three-bin sort**; lead with the
drydock cut (structural). The hard part — attributing actuals to individual JCNs when several are
**bundled into one Job Summary** — is solved by **attributing labor (additive), not Cycle-Time
span (not additive)**, via job-costing allocation (simple) or **regression disaggregation**
(rigorous: write each summary as "mix-of-bins → total labor," solve all together for per-bin
labor or a per-bin actual/estimate multiplier = PfCw). **Refined 2026-06-23:** bin at **SWBS
3-digit (~100)**; solve each bin for a size-independent **multiplier** (actual÷estimate labor) so
the Class F estimate carries size. **Σ/Σ trick:** multiplier = Σ(actual AQWP)/Σ(estimate) by SWBS —
both sum to SWBS independently, so **bundles need NO per-JCN splitting** (the attribution worry
largely dissolves); regression only for cross-SWBS sprawl. Two explicit conversions: (1) estimate ×
multiplier → expected labor; (2) labor → span via a per-bin model from single-JCN Cycle Time ≈
fixed wait + labor/(crew×shifts). **Tooling:** Excel (Power Query + Power Pivot) or QlikView; pull
a CU-Phase/Key-Op fact table + JCN dimension, closed-work only — fields in
`03_build/data-fields-and-tooling.md`.

**Data reach (2026-06-23, operator's Qlik pull — KATS load script + 1,181-field data dictionary +
a Gemini build session, all in the Drive `AIM NG` folder):** Cycle Time (AIM `ACTUAL_START/
COMPLETION_DATE`), estimates (`EST_MAN_DAYS_QY` JCN-grain / `MANHOUR_QY` CU-phase), SWLIN→SWBS
(`SWLIN_LI_ID`), drydock (`DRYDOCK_FLAG_CD`), crew, certified filter (`Approval Status CD`='CRT')
all reachable. **KEY FINDING: actual labor is NOT in AIM — it's in the COST/STARS schema**
(`COST_FJ40` straight+OT+holiday hours by Job Order; `COST_FE75` keyop). The multiplier needs an
**AIM↔COST join on Job Order/Key Op** — this is what made Gemini's multiplier come out 1.0 (it
reused an AIM estimate field as both sides). **Shortcut:** fit span ≈ f(EST_MAN_DAYS_QY) per SWBS
from completed single-JCN summaries — no COST actuals needed for a first cut. NNPI is masked in the
published AIM layer. Raw Qlik scripts kept OUT of the git vault (operator's classification call;
vault pushes to GitHub). Gemini fabricated a "Qlik linter" — disregard. **First-cut screen written as a QlikView script
(`03_build/span-screen-qlik.md` — span fit per SWBS, LINEST per SWBS, no COST join); raw Qlik
artifacts now in `01_sources/qlik/` (operator cleared for vault/GitHub).** Still open: define "96
hours" (clock vs shifts; not in 4700.1F); add the drydock override; then the AIM↔COST multiplier.
**Future state (`future-state.md`):** a Power App where users paste JCN/SWLIN/est-man-days → span +
verdict; the Qlik fit exports a small per-SWBS coefficient table (the model) that the app consumes
— decoupled, re-fit on a cadence. **New open question (2026-07-26, decision-log item 19):** the
study has always treated the AIM-NG process manual as a given and never asked **who authors and
maintains it** (the eleven chapters, the shipyard metric suite, the associated project-management
course). It matters because SRF-JRMC is an AIM user **outside** the four public naval shipyards the
manual was written around, so if that framework is authored/sustained under a NAVSEA sponsor, the
SAIV screen becomes an **extension of an existing framework to a forward-deployed repair facility**
— a fourth candidate end state beyond memo/spec/brief, and one that would trip the OCI question in
`_meta/oci-primer.md`. Two cheap OSI checks named: AIM-NG chapter front matter / record-of-changes
for a preparer credit, and USAspending for process-support obligations under the NAVSEA sponsor.
Nothing asserted until one lands. (Question was prompted by non-OSI material; see
[[project_private_non_osi_area]] for why it cannot be answered from that material.)
See `studies/world-class-planning/` ([[project-ai-governance-study]]
is the sibling study track). Related operator context: [[project_uss_rmc_vs_usns_msc]],
[[reference_srf_jrmc_department_structure]].

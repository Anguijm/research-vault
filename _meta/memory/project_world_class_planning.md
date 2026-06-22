---
name: project-world-class-planning
description: thinking project on schedule-as-independent-variable early work screening in AIM; the bundled-JCN attribution problem and the labor-vs-span method
metadata:
  type: project
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
labor or a per-bin actual/estimate multiplier = PfCw). Convert labor→span downstream; predict
**standalone** span (conservative), calibrate on clean one-JCN history.

Open: is Cycle-Time/AQWP queryable by SWLIN/work-type out of AIM-NT? Is JCN↔SWLIN ~1:1 in
bundles? Define "96 hours." See `studies/world-class-planning/` ([[project-ai-governance-study]]
is the sibling study track). Related operator context: [[project_uss_rmc_vs_usns_msc]],
[[reference_srf_jrmc_department_structure]].

---
type: study
study: ai-governance-landscape
title: AI Governance Landscape — what military and corporate organizations actually do
status: research
classification: internal
created: 2026-06-19
last_revised: 2026-06-19
---

# AI Governance Landscape

This folder is a **research study**, not a business opportunity and not a trip
report. It exists to answer one question for the operator: when standing up an
AI governance policy for SRF-JRMC (built around the agentic askSage platform),
what are other military commands, federal agencies, and corporations actually
doing — so the operator's own instruction is informed by practice rather than
written from a blank page.

This is the first deliverable: an **audience-agnostic landscape report**. It
documents what others do. It deliberately does **not** map findings back onto
any draft instruction yet — that comparison is a separate, later pass.

## Scope (operator-confirmed 2026-06-19, via grill-me)

- **Source mix:** military/government **and** corporate (broad aperture).
- **Deliverable:** landscape only. No gap-analysis-against-the-draft this pass.
- **Agentic focus:** balanced — general AI-governance foundations plus the
  agentic-specific layers (token budgets, write-action gating, runaway-loop
  control, human-on-the-loop, agent observability) that an agentic platform
  introduces.
- **Depth:** thorough, multi-source.

## Standing discipline (inherited from the vault)

- **OSI only.** Public sources. No CUI, no command-internal material in this study.
- **FACT / Assessment / Speculation labeled.** A claim about what an organization
  does is a FACT only with a citation; interpretation is Assessment.
- **Never invent a citation.** Every claim traces to a real, fetched URL captured
  in `01_sources/` and indexed in `source-ledger.md`.
- **Paywalled sources** (notably McKinsey and HBR) are captured as public
  abstract + URL and flagged, for the operator to pull full text behind their
  subscription.

## Layout

```
studies/ai-governance/
  README.md             ← this file (scope + alignment record)
  source-ledger.md      ← slug → URL → publisher/date → 01_sources/ file
  01_sources/           ← one capture file per source
  02_synthesis/
    landscape-report.md ← the deliverable (audience-agnostic, cited)
```

## Research streams (this pass)

1. **DoD / U.S. military AI governance** — DoD Responsible AI strategy, CDAO,
   DoD AI ethical principles, service-level (Navy/Army/Air Force) AI policy,
   generative-AI use guidance.
2. **Corporate / enterprise frameworks** — McKinsey and HBR public articles,
   NIST AI RMF, ISO/IEC 42001, enterprise responsible-AI operating models.
3. **Agentic-AI-specific governance** — autonomy gates, least-privilege agent
   permissions, write-action approval, cost/loop controls, agent observability.
4. **Regulated-industry + federal-government + standards** — financial-services
   model-risk practice, OMB federal-AI policy, GAO AI accountability framework,
   OWASP/EU references.

## Decision log

- **2026-06-19** — Study scaffolded. Alignment run via `_meta/grill-me.md`
  (four-question batch; answers recorded under Scope above). Operator chose
  broad source mix, landscape-only deliverable, balanced agentic focus, thorough
  depth. Placed under new top-level `studies/` rather than `research/` to avoid a
  confusing `~/research/research/` path.
- **2026-06-19** — First pass complete. Four parallel web-research streams ran
  (DoD/military, corporate/enterprise, agentic, regulated/federal); raw packs
  saved verbatim in `01_sources/`, indexed in `source-ledger.md`. Synthesis
  drafted: `02_synthesis/landscape-report.md` (v0.1). Reliability discipline held:
  McKinsey bodies un-fetchable (abstracts only, flagged for subscription pull);
  several `.mil`/`.gov` primaries blocked (sourced via secondaries that quote
  them); one fabricated GAO citation caught and discarded by the research agent.
  Gemini draft NOT graded this pass (kept as grounding only). **Next pass
  (operator's call):** gap analysis of the draft against the seven primitives +
  five agentic controls; pull McKinsey/HBR full texts first.
- **2026-06-19 (later)** — Operator pulled both HBR articles. Read in full from
  PDFs, captured as dedicated sources (`01_sources/hbr-rai-checklist.md`,
  `01_sources/hbr-agentic-risks.md`; PDFs under `01_sources/hbr/`), upgraded to
  tier 1 in the ledger. Landscape report bumped to **v0.2** (v0.1 archived under
  `02_synthesis/archive/`): folded in the design-then-phase principle + the
  eight-question readiness checklist (Section 2) and the five-stage agentic
  staircase + six hardening factors (Section 3). McKinsey set still pending pull.
- **2026-06-19 (gap analysis)** — Ran the gap analysis the operator requested
  (draft NOT edited). `02_synthesis/gap-analysis.md`: Part A component-by-component
  breakdown of the draft; Part B coverage against the 7 primitives + 5 agentic
  controls + HBR checklist. Then a 2-round red-team dialogue with Gemini
  (`02_synthesis/red-team-dialogue.md`), curated per the vault's "treat as input,
  verify state-of-world" rules — rejected Gemini's inferred command code numbers /
  "CHENG" / "Suite B"(stale)/"DAO", kept the concepts. Gap analysis bumped to
  **v0.2** with Part F (converged, command-grounded). Headline: draft is strong on
  data-handling, human-in-the-loop, and cost control; thin or silent on the
  governance spine (independent challenge, inventory, owner, quality monitoring) and
  missing a cluster of command-specific controls (Technical Authority supremacy,
  records/legal-hold, MLA/SOFA labor, mosaic access-scoping, DDIL manual-fallback,
  KB recertification, NCIS-vs-JAGMAN incident split). Fixes reframed through existing
  Navy authorities (ISSM ConMon + Technical Warrant Holder chain), not new boards.
  **Pending operator calls:** GenAI.mil-vs-standalone, PII/PHI authorization, maturity
  target, data residency; plus mapping generic roles to real command billets/codes.
- **2026-06-19 (the fix)** — Wrote the instruction rewrite (third product). New
  folder `03_instruction/`: `instruction-v0.1.md` (full draftable instruction from
  gap-analysis Part F + the operator decisions; token/compute demoted to Annex A;
  command decisions left as visible `[COMMAND DECISION]` markers). Then a Gemini
  logic/consistency red-team (`instruction-red-team.md`) — 9 findings, all accepted
  with terminology filtering; sharpest was a real records-vs-spillage contradiction.
  `instruction-v0.2.md` folds them in (reordered KB up, out-of-band verification,
  ingress DLP for PII/PHI, resolved spillage/records deadlock, access-segmented index
  for cross-caveat/Local-National protection, CHENG concurrence over Dept-Head
  proposals, CO as accountable authority with distributed responsibilities, quarterly
  manual-reversion drill, mission-critical compute override). Draft instruction is a
  STUDY work-product, not promulgated; reference identifiers + command codes still
  need verification. Original Gemini draft never edited.
- **2026-06-19 (v0.3)** — Operator answered the Section-A strategic open items via
  `_open-items.md`. `instruction-v0.3.md` folds them in: standalone askSage instance,
  IL5, best-in-class maturity (mapped to DoD AI Ethical Principles + NIST AI RMF, annual
  review), Department-Heads-quarterly governance forum, immediate manual fallback,
  aggregation agent-scoping dropped, data residency assumed-covered (left as [CONFIRM]).
  Section B (confirmations) and C (command-specific code/role mappings) deferred to the
  working group; they remain as [CONFIRM]/[MAP TO COMMAND] markers. Decisions logged in
  `_decisions.md` items 8–14.
- **2026-06-19 (routing package)** — Built the working-group routing artifact in
  `03_instruction/routing/`: a clean instruction (`instruction-clean.md`, study
  scaffolding stripped, markers reframed as "Working group to resolve" callouts), a
  one-page cover/comment sheet (`cover-routing-sheet.md`), and a combined Word document
  (`SRF-JRMC-INST-5239.1-DRAFT-working-group.docx`, cover + page break + instruction)
  for track-changes markup. Freshened all three main products (gap-analysis F.5 marked
  the strategic questions resolved; landscape report given a downstream pointer) and
  pushed the whole study to the GitHub backup (HBR PDFs excluded for copyright).

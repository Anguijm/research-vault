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
- **2026-06-19 (v0.4)** — Per operator, generalized the authoritative-evaluation model:
  AI output is evaluated by the cognizant domain authority (technical→CHENG, IT→CIO,
  business/strategic→BSPO, other→cognizant authority), and each department designates an
  authoritative AI content evaluator (anything technical routes to the CHENG chain).
  `instruction-v0.4.md` (§6 generalized + new §6.b, §8.e, §7.b); routing package
  (`instruction-clean.md`, cover sheet, `.docx`) rebuilt from v0.4. Decision logged as
  `_decisions.md` item 15.
- **2026-06-19 (v0.5)** — Operator supplied the real department structure (Codes 100–1200;
  no 400/800/1000) and three corrections: (1) the AI changes no existing process —
  responsibility falls along established lines, so the overbearing "route technical to CHENG"
  language is deleted and each department is the authoritative evaluator for its own domain
  (§6.a department table; §3.e capstone); (2) federated knowledge base — each dept owns/feeds/
  controls its repository, 200 owns the technical library + derivative classifier, CIO/ISSM is
  platform custodian (§5, §8.b, §8.e); (3) records/directives generalized to the command SORM.
  `instruction-v0.5.md` + new study `_glossary.md`; routing package rebuilt from v0.5;
  `_decisions.md` item 16; reference memory added for the department structure. Planned in
  plan mode (`.claude/plans/let-me-just-tell-zany-corbato.md`, approved).
- **2026-06-19 (v0.6)** — Two operator corrections: (1) the command uses **both askSage and
  GenAI.mil** (not standalone) — §2 reframed with the recommended split (GenAI.mil for general
  questions, askSage for agentic work, prototype on GenAI.mil to save askSage tokens);
  instruction stays askSage-specific. (2) **Removed the entire §2 "out of scope" block** as
  wordy/redundant (data stays in §4, the "AI is not an authority" principle stays in §3/§6;
  digital supervision dropped). `instruction-v0.6.md`; routing package + cover sheet rebuilt;
  `_decisions.md` items 17–18; memory updated. Planned + approved in plan mode.
- **2026-06-19 (research)** — Operator question: how do DoD/DoW activities run askSage given the
  GenAI.mil mandate, and do any Navy activities use it? Two web-research streams →
  `01_sources/asksage-genai-mil-adoption.md` + ledger rows. Findings: GenAI.mil is the enterprise
  DEFAULT, not an exclusive ban (so dual-platform is sound; askSage runs as a separately
  authorized capability + acquisition vehicle, e.g. the Army's IL5/IDIQ workspace);
  **BigBear.ai acquired askSage ($250M, closed 2025-12-31) and founder Chaillan departed Feb
  2026.** Then a USASpending check via `lib/usaspending.py` (the news sweep had missed this):
  Ask Sage has 46 contract actions + the Army "Decentralized IDIQ" (W9128Z25DA001), and **two
  are Navy task orders off that IDIQ — NSWC Corona ($475K) and Naval Research Lab ($24.75K)** —
  the concrete vehicle a Navy command (likely incl. SRF-JRMC) uses. Source pack Part 4 +
  context note in `_decisions.md`.
- **2026-06-19 (v0.7)** — Folded the concrete askSage authority/acquisition basis into §2:
  GenAI.mil is the enterprise default not an exclusive bar; askSage holds its own IL5
  authorization, acquired via decentralized task orders against the Army Ask Sage IDIQ
  (W9128Z25DA001), the vehicle other Navy activities use. §2 `[CONFIRM]` now asks for the
  command's own task-order PIID. `instruction-v0.7.md`; routing package + cover sheet rebuilt;
  `_decisions.md` item 19.
- **2026-06-20 (v0.8)** — Operator: a command instruction shouldn't embed a contract PIID (it
  churns and would force instruction updates). Removed the PIID from §2; it now states the
  durable mechanism only (separately IL5-authorized; acquired via a Department contract vehicle,
  e.g. the Army-managed Ask Sage IDIQ), with specifics held in command cybersecurity/contracting
  records. PIIDs remain only in the dated research/decision records. `instruction-v0.8.md`;
  routing rebuilt; `_decisions.md` item 20.
- **2026-06-20 (v0.9)** — Added §15, Departmental information-governance plans: each department
  must develop its own AI-use/information-governance plan (common high-level expectations
  grounded in the NIST AI RMF + the DoD AI Ethical Principles) before its personnel get askSage
  access — a department-level gate alongside individual training (§13). §8.e updated; a
  `[MAP TO COMMAND]` flags a one-page departmental-plan template. `instruction-v0.9.md`; routing
  rebuilt; `_decisions.md` item 21.
- **2026-06-20 (template)** — Built the departmental-plan template
  (`03_instruction/departmental-governance-plan-template.md` + `Departmental-AI-Governance-Plan-TEMPLATE.docx`):
  a one-page fill-in form mapped to the six §15.b expectation areas, with a use-case table,
  acknowledgments, and a Department Head approval block. Draft for working-group adoption; cover
  sheet item 10 + routing docx refreshed to point to it. `_decisions.md` item 22.
- **2026-06-21 (Gemini advisory + v0.10)** — Pulled a Gemini advisory from the operator's Drive
  (`01_sources/gemini-advisory-2026-06-finalizing-askSage-framework.txt`), reconciled it
  (`02_synthesis/gemini-advisory-reconciliation.md`): **PII/PHI and NNPI reopenings rejected**
  (operator, firm). Verified its references via web + USASpending and folded them into
  **`instruction-v0.10.md`** (added SECNAVINST 5239.19A/5510.36B, SECNAV M-5210.1, OPNAVINST
  3120.32D=SORM; resolved §5.a/§10 SORM + §11.a 36 CFR 1229.10 markers). Billet delegations →
  working-group-to-confirm (§8.a); per-project time-savings tracking added (§9.e/§14.b). NIST
  Govern/Map/Measure/Manage enrichment HELD for operator discussion; Gemini's invented risk/token
  math declined. Routing package rebuilt; `_decisions.md` items 23–27. (Cattle Drive = the DON CIO
  IT-consolidation initiative behind the GenAI.mil mandate.)

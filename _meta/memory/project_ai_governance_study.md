---
name: project-ai-governance-study
description: New studies/ track researching AI-governance practice to inform the operator's own SRF-JRMC askSage governance instruction
metadata:
  type: project
---

The operator is drafting an AI governance instruction for SRF-JRMC, built around
**askSage** (an agentic AI platform the command is adopting). This spawned a new
vault area: `studies/` (top-level, peer to `opportunities/` and `trip-reports/`),
for non-opportunity, non-trip-report research. First study:
`studies/ai-governance/`.

Key facts to carry forward:
- This is **research, not a business opportunity** — it does not run the SOP
  pipeline. It uses a lightweight study layout (README + source-ledger +
  01_sources/ raw packs + 02_synthesis/landscape-report.md).
- A Gemini-generated draft instruction (SRF-JRMC INST 5239.1 DRAFT) exists as
  grounding only; it has NOT been graded. The 2026-06-19 pass was **landscape
  only** by operator choice.
- **Gap analysis DONE (2026-06-19):** `02_synthesis/gap-analysis.md` v0.2 +
  `red-team-dialogue.md` (2-round Gemini red-team, curated). Draft strong on
  data-handling / human-in-the-loop / cost control; thin on the governance spine
  (independent challenge, inventory, owner, quality monitoring) and missing
  command-specific controls: Technical Authority supremacy (AI = clerical aid, not
  technical authority; route spec changes through DFS), records/legal-hold,
  MLA/SOFA labor (no AI digital-supervisor over Local Nationals; MLA = Master Labor
  Agreement, formerly Master Labor Contract/MLC), mosaic
  access-scoping, DDIL manual-fallback, knowledge-base recertification,
  NCIS-vs-JAGMAN incident split. Fixes go through EXISTING Navy authorities (ISSM
  ConMon + Technical Warrant Holder chain), not new boards. Both HBR full texts
  ingested (tier 1); McKinsey set still pending pull.
- **Operator decisions 2026-06-19 (`studies/ai-governance/_decisions.md`):** PII/PHI
  are OUT for askSage (match the GenAI.mil bar, not allow-as-CUI). Technical
  adjudication (weld spec etc.) belongs to the **CHENG (Chief Engineer) and chain** —
  operator confirmed the CHENG billet the study had declined to assert; that chain is
  the technical human-in-the-loop. IT + INFOSEC = **CIO/ISSM**. Ownership is a
  combination of people, not one. Record retention/legal hold needs a **Legal chop**.
  **Digital supervision is OUT OF SCOPE** for the whole AI implementation (cleaner than
  a per-MLA control; removes most MLA/SOFA labor exposure).
- **The fix (instruction rewrite) DONE 2026-06-19:** `03_instruction/instruction-v0.2.md`
  (third product) + `instruction-v0.1.md` (prior) + `instruction-red-team.md` (Gemini
  logic pass, 9 findings all accepted). Structured as a DON command instruction
  governing USE of askSage; token/compute demoted to Annex A; CO accountable with
  distributed roles (CIO/ISSM = IT/INFOSEC + ConMon + ingress DLP; CHENG chain =
  technical adjudication + concurrence; Legal = records/labor); access-segmented index
  to stop cross-caveat (NOFORN/ITAR) leakage via agents to Local National users;
  records-vs-spillage contradiction resolved. STILL A STUDY DRAFT, not promulgated —
  reference identifiers + actual command code numbers need verification; original
  Gemini draft never edited.
- **Command context (operator, 2026-06-19) — SRF-JRMC is mature at source-doc handling.**
  NOFORN is already barred from the SRF-JRMC network share; ALL technical direction
  (drawings, policy, manuals) is screened by a **derivative classifier** who redacts/denies
  unreleasable info before it reaches the share. So the askSage knowledge base INHERITS an
  already-releasability-screened corpus — don't design AI controls that rebuild this. The
  only residual: index only the screened corpus + prohibit un-screened uploads (so AI isn't
  a screening bypass). Folded into instruction v0.2.1 (§5.c/§7.c). General lesson: inherit
  existing command processes (screening, QA, security), don't duplicate them.
- **Section-A strategic decisions made 2026-06-19 → instruction v0.3** (`03_instruction/instruction-v0.3.md`):
  **standalone askSage** (not GenAI.mil) — rationale: GenAI.mil not yet mature enough to
  converge; askSage is **ATO'd at IL5 and connects to Navy Flank Speed shares**; processes
  built in askSage are transferable to GenAI.mil when warranted. Command operates UNDER
  askSage's IL5 ATO (vendor-provided accredited platform), owns the governance layer (NOT
  "owns the ATO"). **IL5**, **best-in-class** maturity (now maps to
  DoD AI Ethical Principles + NIST AI RMF, annual review cadence), data residency assumed
  covered by existing accreditation (left as [CONFIRM], not closed), governance forum =
  **Department Heads quarterly**, manual fallback = **immediate**, aggregation agent-scoping
  **dropped**. See `_decisions.md` items 8–14.
- **Instruction v0.4 (2026-06-19):** generalized authoritative evaluation — AI output is
  evaluated by the **cognizant domain authority** (technical→CHENG chain, IT/security→CIO,
  business/strategic→**BSPO**, other→cognizant authority), and **each department designates
  an authoritative AI content evaluator** (anything technical routes to CHENG). `_decisions.md`
  item 15. Routing package (clean instruction + cover + .docx) in `03_instruction/routing/`,
  rebuilt from v0.4.
- **Still pending — deferred to the working group:** Section B confirmations (reference
  identifiers, spillage/records authority, screening process) + Section C command-specific
  mappings (eng/QA codes, SCG names, systems of record, named authorities) — remain as
  [CONFIRM]/[MAP TO COMMAND] markers in v0.3; resolved during working-group review.
- Closest public analog to SRF-JRMC's situation: the **U.S. Army Enterprise LLM
  Workspace**, also powered by Ask Sage, CUI/IL5-accredited, governed via
  CIO-controlled token-based billing. Note the tension: DoD-wide direction is
  toward **GenAI.mil** as the single CDAO-governed CUI/IL5 platform (Navy mandated
  transition by 2026-04-30), so a separate command askSage instance is a strategic
  question, not a settled one.

Web research now works from Claude Code via WebSearch/WebFetch (the old "no web
access" line in CLAUDE.md is stale for this kind of task). Caveats: mckinsey.com
and many `.mil`/`.gov` pages hard-block the fetcher; route via secondaries or the
operator's subscription. Related: [[reference_fetching_403_blocked_domains]],
[[feedback_avoid_em_dash_tell]], [[feedback_keep_draft_versions]].

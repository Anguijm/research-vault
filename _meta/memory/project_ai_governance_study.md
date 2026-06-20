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
- **Instruction v0.5 (2026-06-19):** embedded the real department structure (see
  [[reference_srf_jrmc_department_structure]]); **DELETED** the overbearing "route technical
  to CHENG" language — governing principle is **"the AI changes no existing process;
  responsibility falls along established command lines"** (§3.e capstone). Flipped §5 to a
  **federated** knowledge base (each dept owns/feeds/controls its repo; 200 owns the technical
  library + derivative classifier; CIO/ISSM = platform custodian + connection registry, not
  content). Records/directives generalized to "per the command SORM." Added study
  `_glossary.md`. `_decisions.md` item 16; routing package rebuilt from v0.5.
- **Instruction v0.6 (2026-06-19) — DUAL-PLATFORM (supersedes the earlier "standalone askSage,
  not GenAI.mil" framing).** The command uses **both askSage and GenAI.mil**. Recommended
  split: GenAI.mil for general questions; askSage for agentic work; prototype agents/prompts
  on GenAI.mil first to save askSage tokens. Instruction stays askSage-specific (GenAI.mil
  under DoD enterprise governance). Also **removed the §2 "out of scope" block entirely**
  (digital supervision no longer stated — operator: nobody uses AI to supervise; residual MLA
  concern still covered by §7.c least-privilege); prohibited data stays in §4. `_decisions.md`
  items 17–18; routing package rebuilt from v0.6.
- **USASpending check + instruction v0.7 (2026-06-19):** Ask Sage (UEI W9X4EWLUBAW1) has 46
  contract actions + the Army "Decentralized IDIQ" **W9128Z25DA001**; **two are Navy task
  orders** off it — **NSWC Corona** ($475K, N6426725F0007) and **Naval Research Lab** ($24.75K,
  N0017326F0400) — which corrects the news sweep's "no Navy adopter." v0.7 folds this into §2 as
  the askSage authority/acquisition basis (enterprise-default-not-exclusive + the Army IDIQ
  vehicle); §2 `[CONFIRM]` now asks for the command's own task-order PIID. `_decisions.md` item
  19. Source pack: `01_sources/asksage-genai-mil-adoption.md` Part 4 (via `lib/usaspending.py`).
- **Instruction v0.8 (2026-06-20):** removed the contract PIID from §2 — operator principle: a
  command instruction should NOT embed volatile identifiers (PIIDs, contract/ATO numbers) that
  churn and force instruction updates. §2 states the durable mechanism (separately IL5-authorized;
  acquired via a Department contract vehicle, e.g. the Army-managed Ask Sage IDIQ); specifics live
  in the command's cybersecurity/contracting records. PIIDs stay only in the dated research/decision
  records. `_decisions.md` item 20. **Apply this principle to all future vault instructions.**
- **Instruction v0.9 (2026-06-20):** added §15, Departmental information-governance plans —
  each department must develop its own AI-use/information-governance plan (common high-level
  expectations grounded in NIST AI RMF + DoD AI Ethical Principles) BEFORE its personnel get
  askSage access (department-level gate alongside §13 individual training). §8.e updated.
  `[MAP TO COMMAND]` for a one-page departmental-plan template — **BUILT 2026-06-20**:
  `03_instruction/departmental-governance-plan-template.md` + `Departmental-AI-Governance-Plan-TEMPLATE.docx`
  (fill-in form on the six §15.b areas; draft for WG adoption). `_decisions.md` items 21–22.
- **Gemini advisory + instruction v0.10 (2026-06-21):** operator's Drive (folder
  1ezx8DV3SsSDS6KHgr5lyIFAo0ffgvsnP, SRFSG subfolder) held a Gemini advisory ("Finalizing the
  askSage Framework"); pulled via gdown, reconciled (`02_synthesis/gemini-advisory-reconciliation.md`).
  **PII/PHI + NNPI reopenings REJECTED (operator firm).** Verified refs (web + USASpending) folded
  into v0.10: SECNAVINST 5239.19A/5510.36B, SECNAV M-5210.1, OPNAVINST 3120.32D (SORM), 36 CFR
  1229.10/.12; §11.a emergency-destruction authority resolved. Billet delegations → WG-confirm (§8.a);
  per-project time-savings tracking added (§9.e/§14.b). NIST Govern/Map/Measure/Manage enrichment
  RESOLVED 2026-06-21: operator kept the light GMMM references (§14.c/§15.b) as-is — no re-skin, no
  strip (GMMM = the four NIST AI RMF functions; the six plain-English §15.b areas already implement
  it). Gemini's invented R_E/token math declined. `_decisions.md` items 23–27. Cattle Drive = DON CIO
  IT-consolidation initiative (verified).
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

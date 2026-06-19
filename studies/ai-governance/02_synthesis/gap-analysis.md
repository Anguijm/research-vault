---
type: synthesis
study: ai-governance-landscape
title: Gap analysis — SRF-JRMC askSage governance draft vs. the landscape
status: draft v0.2.1 (post-red-team, operator decisions folded)
classification: internal
created: 2026-06-19
revised: 2026-06-19
analyzes: SRF-JRMC INST 5239.1 [DRAFT] (Gemini-generated)
yardstick: 02_synthesis/landscape-report.md
red_team: 02_synthesis/red-team-dialogue.md
decisions: _decisions.md
changelog: v0.2 folds in the 2-round red-team dialogue. v0.2.1 folds in the operator decisions of 2026-06-19 (PII/PHI prohibited; technical adjudication = CHENG chain; IT/INFOSEC = CIO; Legal chop on records; digital supervision out of scope) — see _decisions.md. Parts A–B stand; Parts C–E SUPERSEDED by Part F.
---

> **v0.2 note:** Parts A and B below (the component breakdown and the
> landscape-yardstick coverage) still stand. **Parts C, D, and E are superseded by
> Part F**, which reprioritizes around this specific command after the red-team
> dialogue and reframes every fix through existing Navy structures rather than new
> corporate-style bodies. Read Part F as the conclusion.

# Gap analysis: the draft vs. what everyone else does

This breaks the Gemini-drafted SRF-JRMC askSage instruction into its components and
holds each against the landscape yardstick. The point is not to grade the draft for
its own sake; it is to make sure nothing critical is missing before the command
commits to a governance posture. The draft is not edited here. This is the substrate
for the red-team dialogue; a v0.2 will fold in that dialogue.

**The yardstick** (from the landscape report): the **seven primitives** every regime
shares (1 accountable owner + standing body, 2 use-case inventory bound to risk tier,
3 risk tiering drives proportional controls, 4 human review before consequential
action, 5 strict data-handling boundaries, 6 lifecycle monitoring, 7 independent
challenge and audit); the **five agentic controls** (A autonomy tiered to oversight,
B least-privilege write-gating, C runaway-loop/cost control, D per-agent identity +
observability, E kill switch/containment); and the **HBR readiness checklist** plus
its design-then-phase rule.

**Status vocabulary:** STRONG (present and well-built), PARTIAL (present but thin or
coarse), GAP (absent), OVER-WEIGHTED (more built-out than its risk warrants relative
to the gaps).

---

## Part A — Component-by-component breakdown of the draft

The draft has nine numbered sections plus tactical rollout advice. Here is what each
covers and how it scores.

| # | Draft section | What it does | Maps to | Status |
|---|---------------|--------------|---------|--------|
| 1 | Purpose | States intent: secure, effective, fiscally responsible askSage use; names the three risk vectors (INFOSEC, automation bias, compute exhaustion) | — | Adequate, but narrow (see gaps: no stated maturity objective) |
| 2 | Scope | Covers military, US civilian, Local National (MLA/IHA), contractors; Yokosuka + Sasebo | — | STRONG, and command-specific (the Local National inclusion is right) |
| 3 | INFOSEC / CUI handling | Authorized data (IL4/IL5), zero-classified tolerance, NNPI bar, mosaic/aggregation risk, CUI marking | Primitive 5 | STRONG (aggregation point is sophisticated). One discrepancy flagged below (PII/PHI). |
| 4 | Mitigating over-reliance (automation bias) | Human-in-the-loop mandate, authoritative precedence (verify vs JFMM / NAVSEA Standard Items / tech manuals), ultimate accountability on the user | Primitive 4; agentic A | STRONG |
| 5 | Managing agentic autonomy | Read-only default; write actions require a human-on-the-loop confirmation prompt | Primitives 3,4; agentic A,B,E | PARTIAL (binary, not tiered; coarse approval) |
| 6 | Token budget / fiscal | Iteration cap (max steps), departmental quotas via CIO/Code 109, 75/90/100% alerts, prompt efficiency | Agentic C | STRONG, arguably OVER-WEIGHTED |
| 7 | Roles and responsibilities | CIO (Code 109)/ISSM, Department Heads, End Users | Primitive 1 (partial) | PARTIAL (admin roles, no governance body or senior AI owner) |
| 8 | Incident reporting | Data spillage protocol; rogue-agent stop/halt + report | Primitives 6,7 (partial); agentic E | PARTIAL (reactive only; no independent audit) |
| 9 | Mandatory training | Responsible AI + prompt engineering module before account issuance | HBR Q4/Q5 (partial) | PARTIAL (trains users, not the oversight function) |
| — | Tactical rollout advice | Centralize knowledge base; prompt library; show a real hallucination; watch MLA/IHA export controls | several | Good instincts, but two of these are policy-grade, not "advice" (see gaps) |

**Assessment.** The draft is strong exactly where the landscape says the problem is
already mostly solved (data-handling, human-in-the-loop, cost control) and thin or
silent exactly where the landscape says maturity actually lives (governance body,
inventory, risk tiering, independent challenge, audit/observability). That is the
headline finding.

---

## Part B — Yardstick coverage

### The seven primitives

1. **Accountable owner + standing governance body — PARTIAL/GAP.** The draft names an
   ISSM/administrator (Code 109) and gives Department Heads use-case approval, but
   there is no single senior accountable AI owner (a Chief-AI-Officer equivalent) and
   no standing AI governance body that meets on a cadence to review use cases, risks,
   and the policy itself. Every regime has both: CDAO + CDAO Council `[dod-caio-statement]`,
   agency CAIO + governance board `[omb-m-25-21]`, the Fed Board's layered committees
   `[fed-m25-21-compliance]`, the enterprise committee `[diligent-ai-gov]`. Code 109 as
   ISSM is the *administrator*, not the *governance chair*. **This is gap #1.**
2. **AI use-case inventory bound to risk tier — GAP.** The draft has no register of
   where askSage is used across the command, and no risk classification of those uses.
   Inventories are the universal intake gate `[omb-m-25-21]` `[diligent-ai-gov]`
   `[sr-11-7]`. Without one you cannot apply primitive 3 at all. **This is gap #2.**
3. **Risk tiering drives proportional controls — GAP.** The draft's only graduation is
   read-only vs write (Section 5). There is no notion of high-impact vs routine use,
   so a maintenance-planning recommendation and a cafeteria-menu draft get the same
   controls. The landscape ties control intensity to use-case risk `[eu-ai-act]`
   `[sg-model-ai-gov]` `[csa-nist-rmf-agentic]`. **Gap, tied to #2.**
4. **Human review before consequential action — STRONG.** Sections 4 and 5 cover this
   well: HITL mandate, authoritative-source precedence, write-action confirmation.
   Possibly the strongest part of the draft. Refinement only: approvals are bare
   ("click Approve"), where the landscape wants structured approval (intent, data
   lineage, permissions, blast radius, rollback) `[strata-hitl]`.
5. **Strict data-handling boundaries — STRONG, one discrepancy.** Section 3 is good.
   **Discrepancy to resolve:** the draft authorizes "standard CUI" including PII and
   PHI at IL4/IL5, but the DoD enterprise platform GenAI.mil *prohibits* PII/PHI even
   at IL5 `[navy-genai-mil]` `[dod-genai-mil-rollout]`. Is your askSage instance
   actually authorized for PII/PHI, or should it match the GenAI.mil bar? **Also
   missing:** a contractual control on vendor use/retention of command data, which
   DoDI 5400.19 requires `[dodi-5400.19]`.
6. **Lifecycle monitoring — PARTIAL/GAP.** The draft monitors *cost* (token alerts)
   and *incidents*, but not *quality*: no continuous monitoring of hallucination rate,
   model drift, or output quality, no pre-use assessment of new tools/use cases, and
   no scheduled reassessment cadence. DoD's own AI cyber guidance requires continuous
   monitoring for AI-specific threats (drift, data poisoning) `[dod-ai-cyber-rmf]`;
   GAO and FDA both center monitoring `[gao-21-519sp]` `[fda-ai-device]`. **Gap.**
7. **Independent challenge and audit — GAP.** The draft rests entirely on the end
   user's self-verification (HITL). There is no second line of defense, no
   independent validation or "effective challenge" by someone separate from the user,
   and no audit function reviewing AI use independent of the using department. The
   landscape calls this the single function that separates a mature regime from a
   paper policy `[sr-11-7]` `[gao-21-519sp]`; where it is weakest, governance is
   judged weakest `[hospital-ai-gov]`. **This is gap #3, and the most consequential.**

### The five agentic controls

- **A. Autonomy tiered to oversight — PARTIAL.** Read-only/write is binary. The
  landscape wants tiers (fully supervised / constrained autonomy / autonomous) keyed
  to use-case risk, with oversight as "a property of the decision" `[csa-nist-rmf-agentic]`
  `[strata-hitl]`.
- **B. Least-privilege write-gating — PARTIAL, with a command-specific hole.** Read-only
  default is the right instinct. Missing: per-tool scoping, sandboxing, separating
  generation from execution `[teleport-agentic-mitigations]`, and the principle that an
  agent inherits the invoking user's permissions `[msft-agent-governance]`. That last
  one is acute here: a Local National user's agent would inherit a Local National's
  access, which is exactly the ITAR/export-control problem the draft buried in
  "tactical advice." **Elevate it.**
- **C. Runaway-loop / cost control — STRONG.** Section 6 is ahead of most of the field.
  Minor add-ons available (no-progress detection, wall-clock timeout, circuit breakers)
  `[bswen-loop-control]`, but the core is solid.
- **D. Per-agent identity + observability/audit logs — GAP.** No agent registry, no
  per-agent/per-user action audit logs, no behavioral monitoring. "Identity as the
  control plane" is absent `[owasp-state-agentic-gov]` `[msft-agent-governance]`.
  Ties to gap #3 (you cannot audit what you do not log).
- **E. Kill switch / containment — PARTIAL.** Section 8 has a manual "Stop/Halt." Missing:
  who can invoke it, how fast, credential revocation, and any automated suspension for
  severe patterns `[csa-nist-rmf-agentic]`.

### HBR readiness checklist (design-then-phase)

The draft reads as a "mini RAI program" (use-rules) more than a fully designed
program, which is exactly the pattern HBR warns against `[hbr-rai-checklist]`. Of the
eight readiness questions: Q1 strategic objective — **not stated**; Q2 values→procedures
— mostly yes; Q3 program metrics (is governance working? awareness, compliance,
impact) — **GAP**; Q4/Q5 trained oversight people + validation personnel — **GAP**;
Q6 harmonization with cyber/privacy/IT — partial; Q7 strategic roadmap / phased rollout
— **GAP**; Q8 implementation playbook — partial (the tactical advice). **Design-then-phase:**
the draft is a single instruction with no rollout-design behind it.

---

## Part C — Critical gaps, prioritized

1. **No independent challenge / audit function (primitive 7, agentic D).** The whole
   model leans on the individual user. Add a second line: an independent reviewer or
   audit of AI use, and the audit logging that makes it possible.
2. **No AI use-case inventory + risk tiering (primitives 2, 3).** Stand up a register
   and classify uses (e.g., high-impact = anything touching seaworthiness, QA,
   tag-out, contract obligations) so controls scale.
3. **No standing AI governance body / named senior owner (primitive 1).** Code 109 as
   ISSM is not a governance board. Name an owner and a body with a review cadence.
4. **Quality monitoring is missing (primitive 6).** Cost is watched; correctness/drift
   is not. Add output-quality and drift monitoring and a reassessment cadence.
5. **The Local-National / ITAR permission-inheritance problem is policy, not advice
   (agentic B).** Given Yokosuka/Sasebo, an agent inheriting a foreign-national user's
   access to query foundation models about US naval ship designs is a first-order
   control, not a footnote.
6. **No program metrics, roadmap, or trained oversight cadre (HBR Q3/Q5/Q7).** No way
   to tell if the governance is working, no phased rollout design, no validators.

## Part D — Where the draft may be over-weighted

- **Token/fiscal control (Section 6)** is the most built-out section and the most
  "solved" problem in the landscape. **Assessment:** keep it, but it should not be one
  of three headline pillars while independent audit and inventory are absent. Cost
  control is a guardrail, not a governance spine.

## Part E — Strategic questions for the operator (not mine to decide)

1. **GenAI.mil vs a standalone askSage instance.** DoD-wide direction is consolidation
   onto GenAI.mil (Navy mandated transition by 2026-04-30) `[navy-genai-mil]`. The
   Army runs Ask Sage as its Enterprise LLM Workspace `[army-camogpt-asksage]`. Where
   does an SRF-JRMC askSage instance sit relative to that? This shapes the whole policy.
2. **Is askSage authorized for PII/PHI at your IL?** Resolves the Section 3 discrepancy.
3. **What is the maturity target (HBR Q1)?** Compliance-minimum, or best-in-class? The
   answer changes how heavy the build should be.

---

---

## Part F — Post-red-team synthesis (the converged view)

This part supersedes Parts C–E. It folds in the two-round red-team dialogue with
Gemini (`red-team-dialogue.md`). The dialogue did two things: it surfaced gaps that
were invisible from the corporate/landscape frame because they are specific to a
forward-deployed Navy ship-repair command, and it corrected the *implementation* of
my structural findings, realizing them through existing Navy authorities instead of
new boards. I held the structural gaps; I let the red team sharpen how they get fixed.

### F.1 — New gaps the dialogue surfaced (command-specific, not in v0.1)

Plain-English first: the biggest things the landscape frame could not see are that
this is a safety-of-life industrial command, on foreign soil, with a foreign-national
workforce, that runs on Navy technical-authority and quality systems already.

1. **Technical Authority collision (safety-of-life).** An agentic tool that "reasons"
   about a weld spec, a torque value, or a tag-out is colliding with NAVSEA Technical
   Authority. The information owner (CIO/ISSM) does not own interpretation of a
   technical requirement; the Technical Warrant Holder chain (Engineering / Quality
   Assurance) does. **Control:** designate all AI technical output as a
   "non-authoritative clerical draft" that a Technical Warrant Holder must sign before
   work; any AI suggestion that touches a specification routes through the existing
   Departure-from-Specification (DFS) process. *(Operator: map "Technical Warrant
   Holder" to your command's actual engineering/QA billets — I am not asserting
   specific code numbers.)*
2. **Records / legal hold.** Agentic chain-of-thought logs are Federal Records and
   potential evidence in a JAGMAN (JAG Manual) safety or mishap investigation. They
   are not ephemeral chat. **Control:** long-term log retention per the records
   schedule, with legal-hold capability. This also supplies the audit trail that
   primitive 7 needs.
3. **Host-nation labor boundary (MLA/SOFA).** Using agentic AI as a "digital
   supervisor" that monitors, tasks, or evaluates Local National (Master Labor
   Agreement, MLA — formerly Master Labor Contract) staff could violate the labor
   agreement, the Status of Forces Agreement, or host-nation law. **RESOLVED by
   operator decision 2026-06-19 (`../_decisions.md`):** digital supervision is OUT OF
   SCOPE for the AI implementation entirely — the AI will not be a digital supervisor
   of anyone. That removes most of this exposure at the root. The residual concern is
   narrower: a Local National user's agent inheriting that user's data access (the
   ITAR / least-privilege point at agentic control B), not AI-as-supervisor.
4. **Mosaic / aggregation access-scoping.** The draft names the mosaic risk; the fix
   is concrete. An agent with horizontal access to casualty reports (CASREPs) plus the
   availability schedule plus manpower logs can synthesize a fleet-readiness picture
   that is effectively classified under the Security Classification Guide, even though
   every input is CUI. **Control:** limit each agent's horizontal data scope;
   compartment instances so no single agent can build the "God view."
5. **Operational resiliency (DDIL).** Ship repair happens inside a steel box with
   intermittent connectivity. A use case that *depends* on cloud AI becomes a
   production bottleneck when the link drops. **Control:** a manual-fallback rule — no
   work center may adopt an AI workflow it cannot revert to manual quickly.
6. **Knowledge-base recertification.** The JFMM and NAVSEA Standard Items change by
   transmittal; an AI indexed to a stale version is a safety hazard, not just wrong.
   **Control:** a recertification cycle that re-syncs the indexed authoritative
   documents to current change transmittals, with a named owner.
7. **Incident-chain split.** A *hallucination* that causes a safety mishap is an
   internal JAGMAN/Safety investigation; a *spillage* (classified data pasted into a
   prompt) is an NCIS/security violation. **Control:** Section 8 of the draft must
   split these two reporting chains explicitly.
8. **Data residency / sovereignty.** Where the IL5 data physically lives, whether any
   local/edge hardware gives host-nation staff administrative access (a SOFA issue),
   and whether traffic over host-nation network backbones meets approved cryptographic
   standards (current CNSA-suite guidance, not the older "Suite B"). **Strategic +
   control:** confirm with the cognizant authority.

### F.2 — How the structural gaps get fixed (Navy-native, no new boards)

The v1 structural gaps (owner, inventory, risk tiering, monitoring, independent
challenge) survive, but the fix is to extend existing authorities, not to build a
corporate governance board:

- **Bifurcated ownership (operator-confirmed 2026-06-19, see `../_decisions.md`).**
  The split runs along the line the operator drew: the **CIO** owns the information-
  technology and information-security side (the Information System Security Manager,
  ISSM, runs the model/instance inventory and a Continuous Monitoring (ConMon) program
  extended to AI-specific signals — CUI leakage, prompt injection, model drift, shadow
  AI). The **CHENG (Chief Engineer) and the CHENG's chain** own technical / functional
  adjudication — which use cases are approved, at what risk, and the technical
  human-in-the-loop call on any AI output touching a specification. It will likely be a
  **combination of people**, not one owner, with a **Legal chop** on record retention
  and legal hold. This is the realized form of primitive 7 (independent challenge),
  split correctly: work-product verification stays in the existing Quality Assurance
  checkpoint system and the CHENG chain; AI-system-use oversight becomes a CIO/ISSM
  cybersecurity function.
- **Inventory + risk tiering through existing categories.** Keep an AI use-case
  inventory, but classify each use against the Navy's *existing* controlled-work risk
  categories (for example Level I / critical vs. non-critical; SUBSAFE is its own
  controlled regime), not a new corporate tier scheme.
- **Governance forum, not a new committee.** Review the use-case inventory for
  "continuance of approval" on a set cadence inside an existing command forum (e.g.,
  an Executive Steering Committee). "A new slide in an existing deck," not a new board.
  *(Operator: name the actual forum.)*
- **Named owner via an existing role.** Anchor accountability in the Authorizing
  Official (AO) / ISSM scope rather than inventing a Chief AI Officer billet.

### F.3 — Confirmed re-weighting

- **Demote token/fiscal control.** Move Section 6 from a headline pillar to an annex
  or IT standard operating procedure. In a command where a missed undock date costs
  far more than any plausible token spend, fiscal control is a guardrail, not a
  governance pillar. Keep the iteration cap as a safety control, not a budget centerpiece.
- **Reframe automation bias and agentic autonomy as one risk: confirmation fatigue.**
  Under click-to-approve, the failure mode is a tired human rubber-stamping agent
  steps. The fix is structured approval (show intent, data lineage, source citation,
  blast radius, rollback), not a bare Approve button.

### F.4 — Converged priority stack for THIS command

Plain-English: lead with safety and security, because this is a safety-of-life command
on foreign soil; fold the governance machinery into existing Navy structures; treat
cost control as housekeeping.

1. **Technical Authority supremacy (safety-of-life).** AI output is a non-authoritative
   clerical draft; a Technical Warrant Holder signs before work; spec-touching
   suggestions go through DFS. *(Closes the category error; primitive 4 done right.)*
2. **Export-control / NOFORN + mosaic access-scoping (security).** Enforce the ITAR /
   NOFORN boundary at the Local-National line and scope agent data-access to prevent
   CUI-to-classified aggregation. *(The binary "go to jail" risk; primitive 5 hardened.)*
3. **Bifurcated ownership + independent-use oversight (the governance spine).** ISSM
   owns inventory + AI ConMon; Technical Authority owns functional-use approval;
   existing forum reviews quarterly; risk mapped to existing Navy categories.
   *(Closes primitives 1, 2, 3, 6, 7 in Navy-native form — the largest single gap-closer.)*
4. **Records, legal hold, and a split incident chain.** Retain agentic logs as Federal
   Records with legal hold; route spillage to NCIS/security and hallucination mishaps
   to JAGMAN/Safety. *(Closes the records gap and fixes Section 8.)*
5. **Operational resiliency + knowledge-base currency.** A manual-fallback rule for
   every use case, and a recertification cycle keeping the indexed JFMM/Standard Items
   current. *(Two safety controls the draft lacked.)*

Cross-cutting, below the top 5 but to be written in: structured approvals (anti
confirmation-fatigue), program-level metrics (is the governance actually working —
awareness, compliance, incident trend), and a phased rollout design (HBR
design-then-phase). *(The host-nation labor concern is now handled by scope, not a
control: digital supervision is out of scope per operator decision — see `../_decisions.md`.)*

### F.5 — Strategic questions (all now answered; see `../_decisions.md` and `../_open-items.md`)

These were the operator-only calls. As of 2026-06-19 they are decided and folded into
instruction **v0.3**:

1. ~~**GenAI.mil vs. a standalone askSage instance?**~~ **RESOLVED → askSage (standalone).**
   GenAI.mil is not yet mature enough to merit convergence; askSage is already ATO'd at IL5
   and connects to the Navy's Flank Speed shares; processes are transferable to GenAI.mil
   when warranted. The command operates under askSage's IL5 ATO and owns the governance layer.
2. ~~**Authorized for PII/PHI?**~~ **RESOLVED → no.** CUI stays authorized to IL5; the
   Privacy (PII) and Health (PHI) categories are carved out, matching the GenAI.mil line.
3. ~~**Maturity target?**~~ **RESOLVED → best-in-class.** Instruction now maps to the DoD
   AI Ethical Principles + NIST AI RMF and adds an annual review cadence.
4. ~~**Data residency?**~~ **WORKING ASSUMPTION → covered by the Flank Speed + askSage IL5
   ATO accreditations; working group confirms.**

*Also resolved (see `../_decisions.md`): the CHENG-chain vs. CIO ownership split, the Legal
chop on records, digital supervision out of scope, governance forum = Department Heads
quarterly, manual fallback = immediate, aggregation agent-scoping dropped. Remaining open
work is Section B/C of `../_open-items.md` (reference identifiers, screening/spillage
confirmations, and mapping generic roles to the command's actual billets/codes) — deferred
to the working group.*

*Operator confirmations since: the CHENG chain owns technical adjudication, the governance
forum is the Department Heads (quarterly), and accountability rests with the Commanding
Officer. Still left to the working group: the command's actual engineering/QA code numbers
and Technical Warrant Holder billets. The study uses verified-generic Navy terms and leaves
the code-level mapping to the command.*

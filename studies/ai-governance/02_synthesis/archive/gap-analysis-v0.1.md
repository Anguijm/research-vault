---
type: synthesis
study: ai-governance-landscape
title: Gap analysis — SRF-JRMC askSage governance draft vs. the landscape
status: draft v0.1 (pre-red-team)
classification: internal
created: 2026-06-19
analyzes: SRF-JRMC INST 5239.1 [DRAFT] (Gemini-generated)
yardstick: 02_synthesis/landscape-report.md
---

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
| 2 | Scope | Covers military, US civilian, Local National (MLC/IHA), contractors; Yokosuka + Sasebo | — | STRONG, and command-specific (the Local National inclusion is right) |
| 3 | INFOSEC / CUI handling | Authorized data (IL4/IL5), zero-classified tolerance, NNPI bar, mosaic/aggregation risk, CUI marking | Primitive 5 | STRONG (aggregation point is sophisticated). One discrepancy flagged below (PII/PHI). |
| 4 | Mitigating over-reliance (automation bias) | Human-in-the-loop mandate, authoritative precedence (verify vs JFMM / NAVSEA Standard Items / tech manuals), ultimate accountability on the user | Primitive 4; agentic A | STRONG |
| 5 | Managing agentic autonomy | Read-only default; write actions require a human-on-the-loop confirmation prompt | Primitives 3,4; agentic A,B,E | PARTIAL (binary, not tiered; coarse approval) |
| 6 | Token budget / fiscal | Iteration cap (max steps), departmental quotas via CIO/Code 109, 75/90/100% alerts, prompt efficiency | Agentic C | STRONG, arguably OVER-WEIGHTED |
| 7 | Roles and responsibilities | CIO (Code 109)/ISSM, Department Heads, End Users | Primitive 1 (partial) | PARTIAL (admin roles, no governance body or senior AI owner) |
| 8 | Incident reporting | Data spillage protocol; rogue-agent stop/halt + report | Primitives 6,7 (partial); agentic E | PARTIAL (reactive only; no independent audit) |
| 9 | Mandatory training | Responsible AI + prompt engineering module before account issuance | HBR Q4/Q5 (partial) | PARTIAL (trains users, not the oversight function) |
| — | Tactical rollout advice | Centralize knowledge base; prompt library; show a real hallucination; watch MLC/IHA export controls | several | Good instincts, but two of these are policy-grade, not "advice" (see gaps) |

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

*Next: take Parts B–E into a red-team dialogue with Gemini, then publish v0.2. Note
for the dialogue: Gemini's training may pre-date the 2026 facts in this study
(GenAI.mil, OMB M-25-21, the SR-26-02 lead). Verify any state-of-the-world pushback
against the vault sources before accepting it.*

---
type: instruction-draft
study: ai-governance-landscape
title: SRF-JRMC askSage governance instruction — rewrite v0.1
status: draft v0.1 (pre-red-team)
classification: internal
created: 2026-06-19
derives_from: 02_synthesis/gap-analysis.md (Part F) + _decisions.md
supersedes_draft: original Gemini SRF-JRMC INST 5239.1 [DRAFT] (NOT edited; preserved)
note: This is a study work-product, not a promulgated instruction. Bracketed markers — [COMMAND DECISION], [CONFIRM], [MAP TO COMMAND] — flag items only the command can resolve. Reference identifiers must be verified before promulgation.
---

# Reader's note (not part of the instruction)

This is the "fix" — the gap analysis turned into a draftable instruction. It keeps
what the original draft did well (data-handling discipline, human-in-the-loop, a cost
guardrail), closes the gaps the analysis and red-team found, and folds in the
operator's decisions of 2026-06-19. Where a real command decision is still open, the
text carries a visible marker rather than a silent assumption. Acronyms are expanded
on first use. The token/compute material is demoted to an annex, where it belongs.

---

# DEPARTMENT OF THE NAVY
**U.S. NAVAL SHIP REPAIR FACILITY AND JAPAN REGIONAL MAINTENANCE CENTER**
**PSC 473 BOX 8**
**FPO AP 96349-0008**

**SRF-JRMC INSTRUCTION 5239.1 [DRAFT — REWRITE v0.1]**

**From:** Commanding Officer, U.S. Naval Ship Repair Facility and Japan Regional Maintenance Center
**Subj:** GOVERNANCE, SECURITY, AND USE OF THE ASKSAGE ARTIFICIAL INTELLIGENCE PLATFORM

**Ref:**
- (a) DoDI 5200.48, Controlled Unclassified Information
- (b) SECNAVINST 5239.3C, Department of the Navy Cybersecurity Policy
- (c) COMUSFLTFORCOMINST 4790.3 (Joint Fleet Maintenance Manual, JFMM)
- (d) DoD Responsible Artificial Intelligence Strategy and Implementation Pathway (2022)
- (e) DoDI 5400.19, Public Affairs Use of Artificial Intelligence (2025) *[verify identifier]*
- (f) DoD CDAO Memorandum, Guidelines and Guardrails to Inform Governance of Generative Artificial Intelligence (12 July 2024) *[verify identifier]*
- (g) DON CIO generative-AI / GenAI.mil guidance *[insert exact memo identifiers]*
- (h) NIST AI Risk Management Framework 1.0 and Generative AI Profile
- (i) The Privacy Act of 1974; HIPAA (for the PII/PHI prohibition)

*[CONFIRM — reference list: identifiers in (e), (f), (g) are from open-source
research and must be verified against the actual issuances before promulgation. Add
the command's cognizant cybersecurity and records-management references.]*

---

## 1. Purpose

To establish command policy, responsibilities, and controls for the secure, safe, and
effective use of the askSage artificial intelligence (AI) platform across SRF-JRMC.
askSage is an *agentic* AI capability: it can reason over multiple steps, retrieve
data across command processes, and take actions. This instruction governs how the
command uses that capability so that it strengthens maintenance and administrative
work while protecting information security, the authority of the command's technical
chain, safety of life and seaworthiness, and compliance with U.S. and host-nation law.

This instruction treats AI as decision **support**. It does not transfer any technical,
quality, contractual, or supervisory authority to a machine. Accountability remains
with people.

## 2. Scope and applicability

This instruction applies to all military, U.S. civilian, Local National (Master Labor
Agreement, MLA, and Indirect Hire Agreement, IHA), and authorized contractor personnel
at SRF-JRMC and its detachments (Yokosuka and Sasebo) who use askSage.

**Explicitly out of scope (the command will not use askSage for these):**
- **Digital supervision.** askSage will not be used as a supervisory or evaluative
  authority over any person (this is a command decision; it also keeps the command
  clear of Master Labor Agreement and Status of Forces Agreement labor concerns).
- **Prohibited data** as defined in Section 4 (classified information, Naval Nuclear
  Propulsion Information, Personally Identifiable Information, and Protected Health
  Information).
- **Final technical, quality, contractual, or disbursement authority.** AI output is
  always a draft for a qualified human to adjudicate (Sections 5 and 6).

*[COMMAND DECISION — instance basis: this instruction is written to govern the
command's USE of askSage regardless of whether the instance is (a) command-standalone
or (b) provided through the DoD enterprise platform GenAI.mil. If (b), the Authority
to Operate, vendor data-handling terms, and platform-level monitoring are inherited
from the enterprise provider rather than owned by the command; mark those paragraphs
accordingly. Resolve this before promulgation.]*

## 3. Policy

a. **AI is a clerical and analytic aid, not a technical authority.** No AI output is
authoritative. Any AI product that bears on a technical requirement, a quality
outcome, a contractual obligation, seaworthiness, or safety of life is a
non-authoritative draft until a qualified human in the cognizant authority chain
adjudicates it (Section 5).

b. **Accountability stays with people.** The human who initiates an AI task owns the
accuracy, safety, legality, and compliance of the result. "The AI produced it" is
never a justification for an error, a deviation, or a disclosure.

c. **Use is bounded by data sensitivity** (Section 4), **by technical authority**
(Section 5), **by least privilege** (Section 6), and **by host-nation and U.S. law.**

d. **Governance uses existing command structures.** This instruction assigns AI
responsibilities to existing roles and forums rather than creating new boards.

## 4. Authorized and prohibited information

a. **Authorized.** askSage is authorized for Controlled Unclassified Information (CUI)
up to the approved DoD Impact Level [IL4 / IL5 — confirm]. This includes routine CUI
and Controlled Technical Information (CTI, marked CUI//SP-CTI), which covers most of
the command's maintenance, engineering, and administrative work.

b. **Prohibited — shall not be entered into askSage under any circumstances:**
   1. Classified National Security Information (CONFIDENTIAL, SECRET, TOP SECRET).
   2. Naval Nuclear Propulsion Information (NNPI).
   3. **Personally Identifiable Information (PII).**
   4. **Protected Health Information (PHI).**

   PII and PHI are categories of CUI, but they carry independent legal regimes (the
   Privacy Act for PII, HIPAA for PHI) and are the worst case for the aggregation risk
   in paragraph (d). They are therefore carved out of the otherwise-authorized CUI,
   matching the DoD enterprise (GenAI.mil) line. Personnel, manpower, and medical-
   readiness workflows are not askSage use cases.

c. **Commercial / non-DoD AI tools** remain unauthorized for any non-public command
information, consistent with reference (e).

d. **Aggregation (the "mosaic" effect).** Agentic AI can synthesize many unclassified
inputs into an output that is effectively classified. Aggregating maintenance
schedules, casualty reports (CASREPs), material deficiencies, and manpower data could
reveal a fleet-readiness picture protectable under the applicable Security
Classification Guide even though every input is CUI. **Control:** an agent's
horizontal data access shall be scoped to its approved use case; instances handling
broad cross-process data shall be compartmented so that no single agent can build an
all-source "readiness" view. *[MAP TO COMMAND — name the cognizant Security
Classification Guide(s).]*

e. **Marking.** AI does not reliably apply CUI markings. Personnel are responsible for
portion-marking any AI-generated product that contains CUI in accordance with
reference (a) before storing or transmitting it.

## 5. Technical authority and the human-in-the-loop

a. **Technical adjudication belongs to the Chief Engineer (CHENG) and the CHENG's
chain.** Any AI output that bears on a technical requirement — a weld specification, a
torque value, a tag-out, a NAVSEA Standard Item interpretation, a repair procedure —
is a non-authoritative clerical draft. The technical human-in-the-loop adjudication is
performed by a qualified person in the CHENG's chain, not by the general end user and
not by the Command Information Officer (CIO). *[MAP TO COMMAND — confirm the engineering
and quality-assurance codes and the Technical Warrant Holder assignments.]*

b. **Departures from specification.** Any AI suggestion that would depart from a
controlling specification (JFMM, NAVSEA Standard Item, technical manual) shall be
processed through the command's existing Departure-from-Specification (DFS) process. AI
does not create an alternate path around the technical authority chain.

c. **Verification against authoritative sources.** AI output that cites a technical
requirement shall be verified against the controlling document, by reference to its
specific paragraph and current change number, before any work is performed.

d. **Structured approval (fight confirmation fatigue).** Where a human approval is
required (this section and Section 6), the approval shall present what is being
approved — intent, the source(s) relied on, the scope of the action, and how it is
reversed — not a bare "Approve" prompt. The risk under click-to-approve is a tired
human rubber-stamping agent steps; the structured prompt and the requirement that the
*right qualified person* (not just any person) approve are the mitigations.

## 6. Agentic autonomy controls

a. **Read-only by default.** askSage agents operate with read-only access unless a
write capability is specifically approved for a use case.

b. **Write-action gating.** Any agent action that changes a record, sends official
correspondence, modifies a schedule, or otherwise changes the state of a command
system requires a structured human approval (paragraph 5.d) before execution. The AI
shall not take a final, state-changing action autonomously.

c. **Least privilege and permission inheritance.** An agent receives only the data and
tools its approved use case requires. An agent acting on a user's behalf inherits that
user's access and no more. **This is a first-order control for the command's Local
National workforce:** an agent acting for a Local National user inherits that user's
authorizations, so export-controlled (ITAR) and NOFORN material must be protected at
the data-access layer, not assumed away. *[MAP TO COMMAND — align with the command's
existing NOFORN / export-control access controls.]*

d. **Autonomy tiered to existing risk categories.** The level of human oversight scales
with the risk of the use case, mapped to the command's existing controlled-work risk
categories (for example Level I / critical versus non-critical) rather than a new
scheme. Higher-risk use cases require closer human control and CHENG-chain approval.

e. **Separation and containment.** Where an agent generates and then executes work,
generation and execution shall be separated by an approval gate. A means to halt an
agent and revoke its access shall exist and be exercisable by [the ISSM / watch — MAP
TO COMMAND].

## 7. Roles, responsibilities, and governance

Governance is a deliberate split across existing roles. It will be a combination of
people, not a single owner.

a. **Command Information Officer (CIO) and Information System Security Manager (ISSM).**
Own the information-technology and information-security side: platform administration,
access and identity management, the model/instance and use-case inventory, the
Continuous Monitoring program (Section 8), and first response to AI security incidents
(Section 10).

b. **Chief Engineer (CHENG) and chain.** Own technical and functional adjudication:
which use cases that touch shipboard systems, technical products, or quality outcomes
are approved, at what risk, and the technical human-in-the-loop call (Section 5).

c. **Staff Judge Advocate / Office of Counsel (Legal).** Reviews and concurs on records
retention, legal hold, and host-nation/labor and export-control questions before the
related provisions take effect.

d. **Department Heads.** Approve specific use cases within their departments, enforce
the human-in-the-loop and least-privilege requirements, and submit their use cases to
the inventory.

e. **End Users.** Verify every AI output against authoritative sources, apply CUI
markings, use only authorized data, and report anomalies and incidents.

f. **Governance forum and inventory.** The command shall maintain an **AI use-case
inventory**, with each use case classified by risk (paragraph 6.d). The inventory is
reviewed for continuance of approval on a set cadence (recommend quarterly) within an
existing command forum rather than a new committee. *[COMMAND DECISION — name the
forum, e.g., an existing Executive Steering Committee; set the cadence.]*

## 8. Monitoring and oversight

a. **Continuous Monitoring (ConMon).** The ISSM extends the command's continuous-
monitoring program to AI-specific signals: CUI/PII/PHI leakage, prompt injection,
model drift, anomalous or unexpected outputs, and shadow (unapproved) AI use. This is
the independent oversight of AI **system use** — distinct from verifying a work product.

b. **Work-product verification stays in Quality Assurance.** Verifying an AI-influenced
work product is performed through the command's existing Quality Assurance checkpoint
system and the CHENG chain. The command does not stand up a separate AI audit shop.

c. **Quality and drift.** Monitoring covers not only cost (Annex A) but output quality
and model drift. Repeated or unexpected AI outputs, and the prompts that produced them,
are reported to the ISSM as possible indicators of a model or security problem.

d. **Program metrics.** The command tracks whether the governance is working — user
awareness, compliance, and incident trend — not only platform usage.

## 9. Records management and legal hold

a. **Agentic logs are Federal Records.** An agent's prompts and chain-of-thought are
decision-support artifacts and potential evidence in a Judge Advocate General Manual
(JAGMAN) safety or mishap investigation, and are subject to Freedom of Information Act
(FOIA) and records obligations. They are not ephemeral chat.

b. **Retention and hold.** AI interaction logs shall be retained per the applicable
records schedule, with a legal-hold capability. Using AI does not waive any records,
FOIA, or privacy obligation. **Legal concurs** on the retention and hold provisions
(paragraph 7.c).

## 10. Incident reporting

The reporting chain depends on the type of incident:

a. **Spillage (security).** If classified information or NNPI is entered into askSage,
or the AI outputs apparent classified material through aggregation, the user
immediately stops the session, does not delete the prompt (preserve it for forensics),
and notifies the Security Manager and ISSM. Security spillage is reported through
security channels, including the Naval Criminal Investigative Service (NCIS) as
required.

b. **Safety mishap (hallucination-driven).** If an AI error contributes to a safety or
quality mishap, it is reported and investigated through the command's safety and
JAGMAN channels.

c. **Rogue or anomalous agent behavior.** If an agent loops, behaves erratically, or
attempts unauthorized access, the user halts it (Section 6.e) and reports to the IT
help desk and ISSM.

## 11. Authoritative knowledge base management

a. **Centralized, version-controlled sources.** Authoritative references the command
preloads for askSage (the JFMM, NAVSEA Standard Items, technical manuals) shall be
centrally indexed by the CIO/ISSM rather than uploaded ad hoc by individual users (this
also conserves compute, Annex A).

b. **Recertification.** A stale authoritative source is a safety hazard, not merely an
error. The indexed references shall be recertified on a defined cycle and upon change
transmittal, with a named owner, so the AI is never reasoning from a superseded
version. *[MAP TO COMMAND — assign the recertification owner and cadence.]*

## 12. Operational resiliency (DDIL)

Ship repair occurs in connectivity-degraded spaces (Disconnected, Degraded,
Intermittent, Low-bandwidth, DDIL). No work center shall adopt an askSage-dependent
workflow that cannot be reverted to a manual procedure quickly. Production shall never
depend on AI-system availability. *[MAP TO COMMAND — set the manual-fallback standard,
e.g., revertible within one working hour.]*

## 13. Training

a. No account is issued before the user completes the command "Responsible AI and Use"
training, covering authorized vs. prohibited data (Section 4), the human-in-the-loop
and technical-authority rules (Section 5), recognizing AI errors (hallucinations),
incident reporting (Section 10), and efficient use.

b. Training is role-aware and is not limited to end users. The oversight roles
(CIO/ISSM, CHENG-chain approvers, Department Heads) are trained for their governance
responsibilities. Training is recurring, not one-and-done.

c. Recommended technique: demonstrate a real AI error (for example a fabricated
torque value or a non-existent reference) during onboarding to inoculate against
automation bias.

## 14. Implementation

a. **Design first, then phase.** This instruction is the full design. Roll it out in
phases by use case and department, not by shipping a partial policy and adding controls
later.

b. **Pilot.** Begin with a small set of low-risk, high-value, read-only use cases to
exercise the governance before extending to write-enabled or higher-risk uses.

c. **Open command decisions** (resolve before or during phased rollout): the instance
basis (Section 2 marker), the approved Impact Level (Section 4), the governance forum
and cadence (Section 7.f), data residency and host-nation cryptographic compliance,
and the maturity target. *[COMMAND DECISION block.]*

---

## Annex A — Token and compute management (administrative)

Cost control is a guardrail, not a governance pillar, and is administered as an IT
standard operating procedure. In a command where a missed undocking date costs far
more than any plausible compute spend, these controls exist to prevent runaway agents
and waste, not to ration mission work.

- **Runaway protection.** Autonomous agent workflows run with a maximum-step (iteration)
  cap and an absolute time limit, so a stuck agent halts itself.
- **Budgets and alerts.** The CIO sets departmental compute budgets; usage alerts fire
  as a department approaches its allocation. Exhaustion restricts non-essential
  agentic use until reset or waiver, with an operational-waiver path.
- **Efficiency.** Centralized indexing of large references (Section 11) and a shared,
  vetted prompt library reduce waste.

---

*End of draft v0.1. Next step per operator: red-team this with Gemini for logic,
internal consistency, and completeness, accounting for Gemini's date-of-knowledge
limits (do not let it relitigate the 2026 facts already verified in this study).*

---
type: instruction-draft
study: ai-governance-landscape
title: SRF-JRMC askSage governance instruction — rewrite v0.3
status: draft v0.3 (Section-A strategic decisions resolved; B/C pending working group)
classification: internal
created: 2026-06-19
derives_from: 02_synthesis/gap-analysis.md (Part F) + _decisions.md + _open-items.md
red_team: 03_instruction/instruction-red-team.md
prior_version: 03_instruction/instruction-v0.2.md
v0.3_change: folds in the operator's Section-A answers (2026-06-19) — standalone askSage instance (not GenAI.mil); Impact Level IL5; maturity target best-in-class (added framework alignment + annual review cadence); data residency treated as covered by existing accreditation (working-group confirm); governance forum = Department Heads, quarterly; manual fallback = immediate; aggregation agent-scoping DROPPED. Section B (confirmations) and C (command-specific code/role mappings) remain for the working group. Later same day: folded in the operator's standalone rationale (askSage is ATO'd at IL5 and connects to Flank Speed; GenAI.mil not yet mature enough for convergence; processes transferable to GenAI.mil when warranted), corrected the ATO framing (command operates UNDER askSage's IL5 ATO, not owns one), and tied data residency to the Flank Speed + askSage ATO boundaries.
v0.2.1_change: per operator command-context — (1) NOFORN already barred from the SRF-JRMC share + all technical direction screened by a derivative classifier before reaching the share; §5.c/§7.c refined to INHERIT that control (index only the screened authoritative corpus; no un-screened uploads) instead of a new AI access-segmentation mechanism. (2) Aggregation/classification-by-compilation is NOT a new AI risk (a human with the same access could compile manually; the SCG already governs it); §4.e reframed to inherit the SCG + spillage procedure, the only AI delta being likelihood/inadvertence handled via training + user recognition; the agent-scoping control demoted to an optional defense-in-depth COMMAND DECISION.
changelog: v0.2 folds in the 9 logic/consistency findings from the Gemini red-team — reordered Knowledge Base up; out-of-band verification; ingress DLP for PII/PHI; resolved the records-vs-spillage deadlock; access-segmented index (cross-caveat synthesis bar); CHENG concurrence over Dept-Head proposals; single accountable authority (CO) with distributed responsibilities; quarterly manual-reversion drill; mission-critical compute override.
note: Study work-product, not a promulgated instruction. [COMMAND DECISION] / [CONFIRM] / [MAP TO COMMAND] mark items only the command resolves. Reference identifiers must be verified before promulgation.
---

# Reader's note (not part of the instruction)

v0.3 resolves the strategic decisions (Section A of `_open-items.md`): this is a
**command-standalone askSage instance at Impact Level 5**, built to a **best-in-class**
maturity target. Two categories of marker remain, deliberately, for the working group:
`[CONFIRM]` items (verify reference identifiers, the spillage/records-destruction
authority, the screening process) and `[MAP TO COMMAND]` items (substitute the command's
real engineering/QA codes, Security Classification Guide names, systems of record, and
named authorities). Acronyms expanded on first use.

---

# DEPARTMENT OF THE NAVY
**U.S. NAVAL SHIP REPAIR FACILITY AND JAPAN REGIONAL MAINTENANCE CENTER**
**PSC 473 BOX 8**
**FPO AP 96349-0008**

**SRF-JRMC INSTRUCTION 5239.1 [DRAFT — REWRITE v0.2]**

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
- (i) The Privacy Act of 1974; HIPAA (PII/PHI prohibition)
- (j) 36 CFR 1229, Emergency authorization to destroy records *[verify citation; for spillage cleanup, para 11.a]*

*[CONFIRM — identifiers (e), (f), (g), (j) are from open-source research and must be
verified against the actual issuances before promulgation. Add the command's cognizant
cybersecurity, records-management, and security-spillage references.]*

---

## 1. Purpose

To establish command policy, responsibilities, and controls for the secure, safe, and
effective use of the askSage artificial intelligence (AI) platform across SRF-JRMC.
askSage is an *agentic* AI capability: it can reason over multiple steps, retrieve data
across command processes, and take actions. This instruction governs how the command
uses that capability so that it strengthens maintenance and administrative work while
protecting information security, the authority of the command's technical chain, safety
of life and seaworthiness, and compliance with U.S. and host-nation law.

AI is decision **support**. It transfers no technical, quality, contractual, or
supervisory authority to a machine. Accountability remains with people.

## 2. Scope and applicability

This instruction applies to all military, U.S. civilian, Local National (Master Labor
Agreement, MLA, and Indirect Hire Agreement, IHA), and authorized contractor personnel
at SRF-JRMC and its detachments (Yokosuka and Sasebo) who use askSage.

**Explicitly out of scope (the command will not use askSage for these):**
- **Digital supervision.** askSage will not act as a supervisory or evaluative authority
  over any person. This also keeps the command clear of Master Labor Agreement and
  Status of Forces Agreement labor concerns.
- **Prohibited data** (Section 4): classified information, Naval Nuclear Propulsion
  Information, Personally Identifiable Information, Protected Health Information.
- **Final technical, quality, contractual, or disbursement authority.** AI output is
  always a draft for a qualified human to adjudicate (Sections 6 and 7).

**Instance basis (decided): the command uses askSage, not the DoD enterprise platform
(GenAI.mil).** Rationale: askSage already provides Authority-to-Operate (ATO)
functionality at Impact Level 5 and connects to the Navy's Flank Speed shares, so it
delivers an accredited, integrated capability today; GenAI.mil is not yet mature enough
to merit convergence. Convergence to GenAI.mil remains a future option, and any process
built in askSage is intended to be transferable to GenAI.mil when that is warranted. The
command operates **under askSage's IL5 ATO** and owns the governance layer — use-case
approval, data controls, monitoring configuration, and the controls in this instruction —
within the platform's accredited capabilities. *[CONFIRM — working group records the
specific askSage ATO reference and the Flank Speed connection authority.]*

## 3. Policy

a. **AI is a clerical and analytic aid, not a technical authority.** No AI output is
authoritative. Any AI product bearing on a technical requirement, a quality outcome, a
contractual obligation, seaworthiness, or safety of life is a non-authoritative draft
until a qualified human in the cognizant authority chain adjudicates it (Section 6).

b. **Accountability stays with people.** The human who initiates an AI task owns the
accuracy, safety, legality, and compliance of the result. "The AI produced it" is never
a justification for an error, a deviation, or a disclosure.

c. **Use is bounded** by data sensitivity (Section 4), the authoritative knowledge base
(Section 5), technical authority (Section 6), least privilege (Section 7), and U.S. and
host-nation law.

d. **Governance uses existing command structures and roles** rather than new boards
(Section 8).

## 4. Authorized and prohibited information

a. **Authorized.** askSage is authorized for Controlled Unclassified Information (CUI)
up to DoD Impact Level 5 (IL5), including routine CUI and Controlled Technical
Information (CTI, marked CUI//SP-CTI). This covers most of the command's maintenance,
engineering, and administrative work.

b. **Prohibited — shall not be entered into askSage under any circumstances:**
   1. Classified National Security Information (CONFIDENTIAL, SECRET, TOP SECRET).
   2. Naval Nuclear Propulsion Information (NNPI).
   3. **Personally Identifiable Information (PII).**
   4. **Protected Health Information (PHI).**

   PII and PHI are categories of CUI, but they carry independent legal regimes (the
   Privacy Act for PII, HIPAA for PHI) and are the worst case for the aggregation risk
   in paragraph (d). They are carved out of the otherwise-authorized CUI, matching the
   DoD enterprise (GenAI.mil) line. Personnel, manpower, and medical-readiness workflows
   are not askSage use cases.

c. **Enforcement of the data boundary is architectural, not honor-based.** A stated
"do not enter" rule is necessary but not sufficient. The CIO is responsible for
configuring, within askSage's capabilities, Data Loss Prevention (DLP) or
sensitive-pattern interception at the prompt-ingress layer to intercept PII, PHI, and
prohibited-data patterns before they reach the model. Detection of what gets through is
covered by Continuous Monitoring (Section 9).

d. **Commercial / non-DoD AI tools** remain unauthorized for any non-public command
information, consistent with reference (e).

e. **Aggregation / classification by compilation.** Aggregating many individually-
releasable CUI items (maintenance schedules, casualty reports (CASREPs), material
deficiencies, manpower data) can produce a fleet-readiness picture that is classified by
compilation. **This risk is not new and is not created by askSage.** Any person with the
same share access can compile the same picture by hand, and it is already governed by the
applicable Security Classification Guide (SCG) and the command's classification and
spillage procedures, which apply to AI-assisted work exactly as to manual analysis. What
askSage changes is **likelihood, not the rule**: it can compile across many sources in one
step, so a user may produce a compiled-classified result quickly and without realizing it.
The controls are therefore: (1) **user recognition** — personnel apply the same compilation
judgment to AI output that they apply to their own analysis, per the SCG; (2) **training**
(Section 13) covers classification by compilation in an AI context; and (3) a
compiled-classified output is handled under the existing **spillage procedure**
(Section 11.a). The optional agent-scoping defense-in-depth measure considered in an
earlier draft was deliberately not adopted: it adds friction without reducing the
underlying risk, since a user with the same access could compile manually regardless.
*[MAP TO COMMAND — name the cognizant SCG(s).]*

f. **Marking.** AI does not reliably apply CUI markings. Personnel portion-mark any
AI-generated product containing CUI per reference (a) before storing or transmitting it.

## 5. Authoritative knowledge base

a. **Centralized, version-controlled sources.** Authoritative references the command
preloads for askSage (the JFMM, NAVSEA Standard Items, technical manuals) are centrally
indexed by the CIO/ISSM, not uploaded ad hoc by individual users. This protects accuracy
and conserves compute (Annex A).

b. **Recertification.** A stale authoritative source is a safety hazard, not merely an
error. Indexed references are recertified on a defined cycle and upon change transmittal,
with a named owner, so the AI never reasons from a superseded version. *[MAP TO COMMAND —
assign the recertification owner and cadence.]*

c. **Releasability rests on the command's existing screening, not a new AI mechanism.**
SRF-JRMC already bars NOFORN material from its network share and screens all technical
direction (drawings, policy, manuals) through a derivative classifier, who redacts or
denies any unreleasable information before it reaches the share. The askSage knowledge
base **inherits** that control: it shall index only from the command's already-screened
authoritative corpus. The AI is neither a new releasability authority nor a substitute
for the derivative classifier. The one new risk is that the AI could become a *bypass* of
that screening, so **ad hoc ingestion of un-screened source documents into askSage is
prohibited** — source material enters the knowledge base only after the existing
screening, through the centralized index (5.a). *[MAP TO COMMAND — confirm the screening
process and name the screened authoritative-corpus source.]*

## 6. Technical authority and the human-in-the-loop

a. **Technical adjudication belongs to the Chief Engineer (CHENG) and the CHENG's chain.**
Any AI output bearing on a technical requirement — a weld specification, a torque value,
a tag-out, a NAVSEA Standard Item interpretation, a repair procedure — is a
non-authoritative clerical draft. The technical human-in-the-loop adjudication is
performed by a qualified person in the CHENG's chain, not by the general end user and not
by the Command Information Officer (CIO). *[MAP TO COMMAND — confirm the engineering and
quality-assurance codes and the Technical Warrant Holder assignments.]*

b. **Departures from specification.** Any AI suggestion that would depart from a
controlling specification (JFMM, NAVSEA Standard Item, technical manual) is processed
through the command's existing Departure-from-Specification (DFS) process. AI does not
create a path around the technical authority chain.

c. **Out-of-band verification.** AI output that cites a technical requirement is verified
against the controlling document through a non-AI authoritative source (the official
technical library / source of record), confirming the specific paragraph wording and
current change number. **The AI's own retrieved snippet is not a sufficient verification
source** — relying on it re-introduces the hallucination it is meant to catch.
*[MAP TO COMMAND — name the authoritative source-of-record system.]*

d. **Structured approval (fight confirmation fatigue).** Where a human approval is required
(this section and Section 7), the approval presents what is being approved — intent, the
source(s) relied on, the scope of the action, and how it is reversed — not a bare
"Approve." The risk under click-to-approve is a tired human rubber-stamping agent steps;
the structured prompt, plus the requirement that the **right qualified person** approve,
are the mitigations.

## 7. Agentic autonomy controls

a. **Read-only by default.** Agents operate read-only unless a write capability is
specifically approved for a use case.

b. **Write-action gating.** Any agent action that changes a record, sends official
correspondence, modifies a schedule, or otherwise changes the state of a command system
requires a structured human approval (Section 6.d) before execution. The AI does not
take a final, state-changing action autonomously.

c. **Least privilege and permission inheritance.** An agent receives only the data and
tools its approved use case requires, and an agent acting on a user's behalf inherits that
user's access and no more. For the Local National workforce this rests on an existing
control: the command's network share is already releasability-screened and NOFORN is
excluded from it (Section 5.c), so an agent drawing on the screened corpus for a Local
National user is bounded by that user's already-screened access. The residual control is
simply to keep askSage inside that screened corpus and prevent un-screened side-channel
uploads (Section 5.c), not to re-adjudicate releasability at the AI layer.

d. **Autonomy tiered to existing risk categories.** Human-oversight intensity scales with
the risk of the use case, mapped to the command's existing controlled-work risk categories
(for example Level I / critical versus non-critical) rather than a new scheme. Higher-risk
use cases require closer human control and CHENG-chain concurrence (Section 8).

e. **Separation and containment.** Where an agent generates and then executes work,
generation and execution are separated by an approval gate. A means to halt an agent and
revoke its access exists and is exercisable by [the ISSM / the command duty IT watch —
MAP TO COMMAND].

## 8. Roles, responsibilities, and governance

a. **Accountability.** The **Commanding Officer** retains overall accountability for
AI-augmented command outcomes, as for all command activity. Responsibilities are
distributed across the existing roles below; this is a deliberate combination of
authorities, not a single new owner and not a new board. *[MAP TO COMMAND — delegate as
appropriate, e.g., to the Executive Director.]*

b. **Command Information Officer (CIO) and Information System Security Manager (ISSM).**
Own the information-technology and information-security side: platform administration,
access and identity management, the model/instance and use-case inventory, the central
knowledge-base index (Section 5), the Continuous Monitoring program (Section 9), the
ingress data-loss controls (Section 4.c), and first response to AI security incidents
(Section 11). The CIO validates platform and security suitability of proposed use cases.

c. **Chief Engineer (CHENG) and chain.** Own technical and functional adjudication. The
CHENG **concurs** on any use case that touches technical specifications, tag-outs, work
authorization, quality outcomes, or shipboard systems, and owns the technical
human-in-the-loop call (Section 6). A use case is not approved over a CHENG non-concurrence
on technical grounds.

d. **Staff Judge Advocate / Office of Counsel (Legal).** Concurs on records retention,
legal hold, spillage records-disposition (Section 11), and host-nation labor and
export-control questions before the related provisions take effect.

e. **Department Heads.** **Propose** use cases for their departments (CHENG concurs on
technical scope per 8.c; CIO validates platform/security), enforce the human-in-the-loop
and least-privilege requirements, and submit their use cases to the inventory.

f. **End Users.** Verify every AI output against authoritative sources (Section 6.c),
apply CUI markings, use only authorized data, and report anomalies and incidents.

g. **AI use-case inventory and governance forum.** The command maintains an AI use-case
inventory, each use case classified by risk (7.d). The **Department Heads review the
inventory for continuance of approval quarterly**, as the command's AI governance forum;
no new committee is created.

## 9. Monitoring and oversight

a. **Continuous Monitoring (ConMon).** The ISSM extends the command's continuous-monitoring
program to AI-specific signals: CUI/PII/PHI leakage, prompt injection, model drift,
anomalous or unexpected outputs, and shadow (unapproved) AI use. This is independent
oversight of AI **system use**, distinct from verifying a work product, and it is the
detection layer behind the ingress controls in Section 4.c.

b. **Work-product verification stays in Quality Assurance.** Verifying an AI-influenced
work product is performed through the command's existing Quality Assurance checkpoint
system and the CHENG chain. The command does not stand up a separate AI audit shop.

c. **Quality and drift.** Monitoring covers output quality and model drift, not only cost
(Annex A). Repeated or unexpected outputs, and the prompts that produced them, are reported
to the ISSM as possible model or security indicators.

d. **Program metrics.** The command tracks whether the governance is working — user
awareness, compliance, and incident trend — not only platform usage.

## 10. Records management and legal hold

a. **Agentic logs are Federal Records.** An agent's prompts and chain-of-thought are
decision-support artifacts and potential evidence in a Judge Advocate General Manual
(JAGMAN) safety or mishap investigation, subject to Freedom of Information Act (FOIA) and
records obligations. They are not ephemeral chat.

b. **Retention and hold.** AI interaction logs are retained per the applicable records
schedule, with a legal-hold capability. Using AI does not waive any records, FOIA, or
privacy obligation. **Legal concurs** on retention and hold. (For the spillage exception
to ordinary retention, see Section 11.a.)

## 11. Incident reporting

The reporting chain depends on the type of incident:

a. **Spillage (security).** If classified information or NNPI is entered into askSage, or
the AI outputs apparent classified material through aggregation, the user immediately
stops the session and **does not delete the prompt** (preserve it for forensics), and
notifies the Security Manager and ISSM. The spilled material is then **isolated and routed
to the formal security spillage-cleanup and records-disposition process** — including
emergency destruction of the affected records where authorized — **only after Security
Manager and Legal adjudication.** This is the deliberate exception to ordinary records
retention (Section 10): a spilled classified record is not preserved as a permanent record
inside the CUI/IL5 store. Report through security channels, including the Naval Criminal
Investigative Service (NCIS) as required. *[CONFIRM — align with the command's security
spillage procedures and the records-destruction authority, ref (j).]*

b. **Safety mishap (hallucination-driven).** If an AI error contributes to a safety or
quality mishap, it is reported and investigated through the command's safety and JAGMAN
channels.

c. **Rogue or anomalous agent behavior.** If an agent loops, behaves erratically, or
attempts unauthorized access, the user halts it (Section 7.e) and reports to the IT help
desk and ISSM.

## 12. Operational resiliency (DDIL)

a. Ship repair occurs in connectivity-degraded spaces (Disconnected, Degraded,
Intermittent, Low-bandwidth, DDIL). No work center shall adopt an askSage-dependent
workflow that cannot be reverted to a manual procedure **immediately**. Every AI-enabled
workflow must have an immediately-available manual fallback; production never depends on
AI-system availability.

b. **Manual-reversion certification.** On a set cadence (recommend quarterly), Department
Heads certify that each AI-enhanced workflow in their department can be executed on the
minimum baseline (manual or legacy IT) if the platform or off-island connectivity is lost.
AI-generated templates and scripts must be maintainable by human staff offline.

## 13. Training

a. No account is issued before the user completes the command "Responsible AI and Use"
training: authorized vs. prohibited data (Section 4), recognizing classification by
compilation in AI output (Section 4.e), the human-in-the-loop and technical-authority
rules (Section 6), recognizing AI errors (hallucinations), incident reporting
(Section 11), and efficient use.

b. Training is role-aware and not limited to end users. The oversight roles (CIO/ISSM,
CHENG-chain approvers, Department Heads) are trained for their governance
responsibilities. Training recurs; it is not one-and-done.

c. Recommended technique: demonstrate a real AI error (for example a fabricated torque
value or a non-existent reference) during onboarding to inoculate against automation bias.

## 14. Implementation

a. **Design first, then phase.** This instruction is the full design. Roll it out in
phases by use case and department, not by shipping a partial policy and adding controls
later.

b. **Pilot.** Begin with a small set of low-risk, high-value, read-only use cases to
exercise the governance before extending to write-enabled or higher-risk uses.

c. **Maturity target: best-in-class.** The command's intent is a best-in-class posture,
not a compliance minimum. Accordingly this instruction is mapped to recognized frameworks
for defensibility — the DoD AI Ethical Principles and the NIST AI Risk Management
Framework functions (Govern, Map, Measure, Manage) — and it is reviewed and updated at
least annually and upon any significant change (a new use-case class, a platform change,
or a change in governing policy). The CIO, with the CHENG and Legal, owns the review.

d. **Data residency.** Source data resides in the Navy's Flank Speed environment, which
askSage connects to, and AI processing occurs within askSage's IL5 ATO boundary — both
accredited — so residency and host-nation cryptographic requirements are expected to be
covered by those existing accreditations. *[CONFIRM — working group verifies with the
cognizant authority that the askSage ATO boundary and the Flank Speed connection satisfy
the data-residency and encryption posture.]*

e. **Working-group items.** The confirmations (reference identifiers, the spillage and
records-destruction authority, the screening process) and the command-specific mappings
(engineering/QA codes, Security Classification Guide names, systems of record, named
authorities) carried as `[CONFIRM]` and `[MAP TO COMMAND]` markers are resolved during
working-group review, before promulgation.

---

## Annex A — Token and compute management (administrative)

Cost control is a guardrail, not a governance pillar, administered as an IT standard
operating procedure. In a command where a missed undocking date costs far more than any
plausible compute spend, these controls exist to prevent runaway agents and waste, not to
ration mission work.

- **Runaway protection.** Autonomous agent workflows run with a maximum-step (iteration)
  cap and an absolute time limit, so a stuck agent halts itself.
- **Budgets and alerts.** The CIO sets departmental compute budgets; usage alerts fire as
  a department approaches its allocation.
- **Mission-critical override.** Departmental compute caps are for fiscal planning, not
  operational denial. During emergent repairs or surge periods, the CIO is authorized to
  reallocate compute to high-priority work (for example Level I components) regardless of
  the initial departmental budget. Caps shall never stop mission-essential repair work.
- **Efficiency.** Centralized indexing of large references (Section 5) and a shared, vetted
  prompt library reduce waste.

---

*End of draft v0.2. Prior version retained at instruction-v0.1.md; logic-pass record at
instruction-red-team.md.*

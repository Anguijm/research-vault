---
type: instruction-draft
study: ai-governance-landscape
title: SRF-JRMC askSage governance instruction — rewrite v0.11 (final-review edits)
status: draft v0.11 (final red-team edits folded in; ready for working-group routing)
classification: internal
created: 2026-06-19
revised: 2026-06-22
derives_from: 02_synthesis/gap-analysis.md (Part F) + _decisions.md + _open-items.md + 01_sources/asksage-genai-mil-adoption.md + 02_synthesis/gemini-advisory-reconciliation.md + 02_synthesis/final-review-and-recommendations.md
red_team: 03_instruction/instruction-red-team.md + 02_synthesis/final-review-and-recommendations.md
prior_version: 03_instruction/instruction-v0.10.md
glossary: _glossary.md
v0.11_change: operator-approved final-review edits (02_synthesis/final-review-and-recommendations.md). Added §7.c export-control/Foreign-Disclosure clause for Local Nationals; §6 technical-authority backstop (AI output is not by itself DFS justification); §12/§15 document the manual fallback in the departmental plan; §11.c prompt-injection reporting. Trimmed the specific "Army Ask Sage IDIQ" example from §2 (generic "Department contract vehicle"); dropped the "best-in-class" superlative from §14/reader-note (kept the NIST/DoD-RAI mapping + annual review); reinforced §4.f (user = authorized holder responsible for CUI designation/marking — NOT "derivative classifier"). Instruction number flagged as Code-1100-assigned (SSIC 5239 vs 5230 — directives-control call), no longer asserted.
v0.10_change: per operator (2026-06-21), from the Gemini-advisory reconciliation. (1) Folded in the VERIFIED references — removed the [verify] markers on DoDI 5400.19 / CDAO memo / 36 CFR 1229 and the DON CIO GenAI.mil memos, and added the command-cognizant references (SECNAVINST 5239.19A cyber-incident; SECNAVINST 5510.36B + SECNAV M-5510.36 info-security; SECNAV M-5210.1 records; OPNAVINST 3120.32D = the SORM). §5.a/§10 SORM and §11.a records-destruction markers resolved (36 CFR 1229.10 + SECNAV M-5210.1). (2) Billet delegations (ED chairs the forum, XO owns training, etc.) NOT asserted — added as a working-group-to-confirm task in §8. (3) Added a per-project time-savings tracking requirement (§9.e), exercised in the pilot (§14.b), per the March-2026 DON CIO direction. NOT folded: the NIST Govern/Map/Measure/Manage enrichment (held for operator discussion) and Gemini's invented risk/token math (declined). PII/PHI and NNPI remain prohibited (rejected Gemini's reopenings).
v0.9_change: per operator — added Section 15, Departmental information-governance plans. Each department must develop its own departmental AI-use/information-governance plan (reflecting common high-level expectations grounded in the NIST AI RMF + the DoD AI Ethical Principles) before its personnel receive askSage access — a department-level access gate complementing the individual training gate (§13). §8.e updated; a [MAP TO COMMAND] flags a one-page departmental-plan template.
v0.8_change: per operator — removed the specific contract PIID from §2. A command instruction should not embed a contract number that ends/renews/changes (it would force instruction updates). §2 now states the durable mechanism (askSage is separately IL5-authorized and acquired through a Department contract vehicle, e.g. the Army-managed Ask Sage IDIQ that other Navy activities use); the specific current ATO and acquisition instrument are kept in the command's cybersecurity and contracting records, not restated here. The §2 [CONFIRM] now asks the cognizant authorities to confirm those remain current, not to embed a PIID. (The specific PIIDs remain in the research source pack / decision log, which are dated records.)
v0.7_change: per operator — folded the concrete askSage authority/acquisition basis into §2, from the USASpending check: GenAI.mil is the enterprise default (not an exclusive bar); askSage holds its own IL5 authorization and is acquired DoD-wide as decentralized task orders against the Army's Ask Sage IDIQ (PIID W9128Z25DA001). The §2 [CONFIRM] marker now asks the working group to record the command's own task-order PIID + the IL5 ATO + the Flank Speed connection authority.
v0.6_change: per operator — (1) the command uses BOTH askSage and GenAI.mil (not standalone); §2 reframed with the recommended split (GenAI.mil for general questions; askSage for agentic work; GenAI.mil to prototype agents/prompts before spending askSage tokens). Instruction stays askSage-specific; GenAI.mil runs under its DoD enterprise governance. (2) Deleted the entire §2 "Explicitly out of scope" block as wordy/redundant — prohibited data stays in §4, the "AI output is always a draft / not an authority" principle stays in §3.a and §6.a; digital supervision dropped (residual MLA/SOFA concern still covered by least-privilege, §7.c). Added a "prototype on GenAI.mil to save askSage tokens" note to Annex A.
v0.5_change: per operator — embedded the real SRF-JRMC department structure (Codes 100–1200; no 400/800/1000) as the evaluation-domain map; DELETED the overbearing "technical bar is highest / route everything to CHENG" language (the AI does not change existing processes; responsibility falls along established command lines); flipped §5 to a FEDERATED knowledge base (each department owns/feeds/controls access to its own repository; 200 owns the technical library + derivative classifier; CIO/ISSM is platform custodian with a connection registry, not the content owner); generalized records/directives to "in accordance with the command SORM" rather than granular Code-1100 mechanics. Added §3 capstone: this instruction changes no existing authority or line of responsibility.
v0.4_change: per operator — generalized Section 6 from "technical adjudication → CHENG" to "authoritative evaluation by the cognizant DOMAIN authority" (technical→CHENG chain, IT/security→CIO, business/strategic→BSPO, other→cognizant functional authority), and added the requirement that EACH DEPARTMENT designate, in writing, an authoritative AI content evaluator (who routes anything technical to the CHENG chain). Updated §8.e and the §7.b cross-reference.
v0.3_change: folds in the operator's Section-A answers (2026-06-19) — standalone askSage instance (not GenAI.mil); Impact Level IL5; maturity target best-in-class (added framework alignment + annual review cadence); data residency treated as covered by existing accreditation (working-group confirm); governance forum = Department Heads, quarterly; manual fallback = immediate; aggregation agent-scoping DROPPED. Section B (confirmations) and C (command-specific code/role mappings) remain for the working group. Later same day: folded in the operator's standalone rationale (askSage is ATO'd at IL5 and connects to Flank Speed; GenAI.mil not yet mature enough for convergence; processes transferable to GenAI.mil when warranted), corrected the ATO framing (command operates UNDER askSage's IL5 ATO, not owns one), and tied data residency to the Flank Speed + askSage ATO boundaries.
v0.2.1_change: per operator command-context — (1) NOFORN already barred from the SRF-JRMC share + all technical direction screened by a derivative classifier before reaching the share; §5.c/§7.c refined to INHERIT that control (index only the screened authoritative corpus; no un-screened uploads) instead of a new AI access-segmentation mechanism. (2) Aggregation/classification-by-compilation is NOT a new AI risk (a human with the same access could compile manually; the SCG already governs it); §4.e reframed to inherit the SCG + spillage procedure, the only AI delta being likelihood/inadvertence handled via training + user recognition; the agent-scoping control demoted to an optional defense-in-depth COMMAND DECISION.
changelog: v0.2 folds in the 9 logic/consistency findings from the Gemini red-team — reordered Knowledge Base up; out-of-band verification; ingress DLP for PII/PHI; resolved the records-vs-spillage deadlock; access-segmented index (cross-caveat synthesis bar); CHENG concurrence over Dept-Head proposals; single accountable authority (CO) with distributed responsibilities; quarterly manual-reversion drill; mission-critical compute override.
note: Study work-product, not a promulgated instruction. [COMMAND DECISION] / [CONFIRM] / [MAP TO COMMAND] mark items only the command resolves. Reference identifiers must be verified before promulgation.
---

# Reader's note (not part of the instruction)

The command uses **askSage and GenAI.mil** together — GenAI.mil for general questions,
**askSage for agentic work** at Impact Level 5 — and the instruction maps to recognized
frameworks (the DoD AI Ethical Principles and the NIST AI Risk Management Framework) for
defensibility. This instruction governs askSage. v0.5 embeds the command's real department structure
(Section 6.a) and is built on one organizing principle: **askSage changes no existing
command process** — it governs AI use within the established lines of authority, quality,
security, and records. The knowledge base is **federated** (each department owns and feeds
its own repository; the CIO/ISSM is custodian of the platform, not the content). Remaining
`[CONFIRM]` and `[MAP TO COMMAND]` markers are deliberate working-group items (reference
identifiers, the SORM/records and spillage authorities, the Security Classification Guide,
systems of record, and a few named authorities). Acronyms expanded on first use.

---

# DEPARTMENT OF THE NAVY
**U.S. NAVAL SHIP REPAIR FACILITY AND JAPAN REGIONAL MAINTENANCE CENTER**
**PSC 473 BOX 8**
**FPO AP 96349-0008**

**SRF-JRMC INSTRUCTION 5239.[__] [DRAFT — REWRITE v0.11]**

*[The Standard Subject Identification Code (SSIC) and sequential number are assigned by the
command directives control point (Code 1100). The "5239" used in prior drafts (the Navy
cybersecurity SSIC) is a placeholder; an AI-use instruction may instead fit SSIC 5230
(information-technology management). 1100 makes the call.]*

**From:** Commanding Officer, U.S. Naval Ship Repair Facility and Japan Regional Maintenance Center
**Subj:** GOVERNANCE, SECURITY, AND USE OF THE ASKSAGE ARTIFICIAL INTELLIGENCE PLATFORM

**Ref:**
- (a) DoDI 5200.48, Controlled Unclassified Information
- (b) SECNAVINST 5239.3C, Department of the Navy Cybersecurity Policy
- (c) COMUSFLTFORCOMINST 4790.3 (Joint Fleet Maintenance Manual, JFMM)
- (d) DoD Responsible Artificial Intelligence Strategy and Implementation Pathway (2022)
- (e) DoDI 5400.19, Public Affairs Use of Artificial Intelligence (28 July 2025)
- (f) DoD CDAO Memorandum, Guidelines and Guardrails to Inform Governance of Generative Artificial Intelligence (12 July 2024)
- (g) DON CIO Memorandum, Enterprise IT Service Designation for GenAI.mil (28 January 2026); and DON CIO Memorandum, Accelerating AI Adoption / Free Training Resources / Measuring Time Savings (March 2026)
- (h) NIST AI Risk Management Framework 1.0 and Generative AI Profile
- (i) The Privacy Act of 1974; HIPAA (PII/PHI prohibition)
- (j) 36 CFR §§ 1229.10 and 1229.12, NARA emergency destruction of records (for spillage cleanup, para 11.a)
- (k) SECNAVINST 5239.19A, Department of the Navy Computer Network Incident Response and Reporting Requirements
- (l) SECNAVINST 5510.36B and SECNAV M-5510.36, Department of the Navy Information Security Program
- (m) SECNAV M-5210.1, Department of the Navy Records Management Manual
- (n) OPNAVINST 3120.32D, Standard Organization and Regulations of the U.S. Navy (the SORM)

*Reference identifiers (e)–(n) verified against the issuances 2026-06-21. [CONFIRM — substitute
the command's local references where they exist (its command SORM derived from (n), and its
local cybersecurity-incident / spillage standard operating procedure); confirm the exact date of
the March-2026 DON CIO memo in (g).]*

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

**Two platforms, with a recommended division of labor.** The command uses both askSage and
the DoD enterprise platform **GenAI.mil**. Recommended use: **GenAI.mil for general
questions; askSage for agentic work** (its agentic capability is why this instruction
exists). GenAI.mil may also be used to develop and refine agents and agentic-workflow
prompts before expending askSage tokens. GenAI.mil is not yet mature enough to host the
command's agentic work, so askSage carries that load for now; the command intends to
transfer agentic work to GenAI.mil when it can support it. **This instruction governs the
command's use of askSage**; GenAI.mil is used under its DoD enterprise governance. askSage
operates under its Authority-to-Operate (ATO) at Impact Level 5, connected to the Navy's
Flank Speed shares, and the command owns the askSage governance layer — use-case approval,
data controls, monitoring configuration, and the controls in this instruction — within the
platform's accredited capabilities.

**Authority and acquisition basis.** Running askSage alongside GenAI.mil is consistent with
Department direction: GenAI.mil is the enterprise *default*, not an exclusive bar, and service
guidance permits separately-authorized tools. askSage is separately authorized at Impact Level
5 and is acquired through a Department contract vehicle for askSage that other Navy activities
already use. The specific current authorization (the IL5
ATO) and acquisition instrument are kept in the command's cybersecurity and contracting
records, not restated in this instruction, so a contract renewal or replacement does not
require changing this instruction. *[CONFIRM — the cognizant cybersecurity and contracting
authorities confirm askSage's IL5 authorization and the command's acquisition instrument are
current and valid.]*

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

e. **This instruction changes no existing process.** It does not alter the command's
existing authorities, responsibilities, technical authority, quality, security, or records
processes, or its lines of responsibility. It governs the use of askSage within them. Where
this instruction names who is responsible for something, it restates the established line,
it does not create a new one.

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

f. **Marking and the user's responsibility.** AI does not reliably apply CUI markings.
AI-generated content does not exempt the user, as the **authorized holder**, from correctly
designating and portion-marking any CUI in that output per reference (a) before storing or
transmitting it. ("AI produced it" is never a defense for a mismarked or inaccurate product;
see Section 3.b.) *(This is CUI designation/marking under reference (a) — not derivative
classification, which is a classified-information function and is separate.)*

## 5. Authoritative knowledge base

a. **Departments own their repositories; the command owns the platform.** Each department
owns, feeds, and controls access to its own document repository (its SharePoint or
equivalent) and is responsible for the content and releasability of what it places there.
askSage draws on those repositories under each user's existing access. The Command
Information Officer (CIO) and Information System Security Manager (ISSM) are custodians of
the **platform**: they maintain a registry of the repositories connected to askSage and
manage platform access and identity, but they do not own the content. Records, directives,
and information are managed in accordance with the Standard Organization and Regulations of
the U.S. Navy (the SORM, reference (n)) and the records program (reference (m)).

b. **Authoritative technical sources and recertification.** Code 200 (Engineering and
Planning) owns the authoritative technical library — the Joint Fleet Maintenance Manual
(JFMM), NAVSEA Standard Items, and technical manuals — and keeps it current. A stale
authoritative source is a safety hazard, not merely an error, so each repository owner
recertifies its content on a defined cycle and upon change transmittal, so the AI never
reasons from a superseded version.

c. **Releasability rests on existing screening, by the owning department.** Each department
is responsible for the releasability of its own repository. For technical direction
(drawings, policy, manuals), Code 200 already screens content through a derivative
classifier, who redacts or denies any unreleasable information, and NOFORN is already barred
from the command's network share. The askSage knowledge base **inherits** these controls;
the AI is neither a new releasability authority nor a substitute for the derivative
classifier. The one new risk is that the AI could become a *bypass* of that screening, so
**ad hoc ingestion of un-screened documents into askSage is prohibited** — material enters a
repository only through the owning department's established feed.

## 6. Authoritative evaluation of AI output (the human-in-the-loop)

a. **AI output is authoritatively evaluated by the cognizant authority, along the command's
existing lines of responsibility.** No AI output is authoritative on its own. A qualified
person who owns the relevant subject matter evaluates AI-produced content before it is used
or released — the same person who would own that work product if a human had produced it.
askSage does not change who is responsible; responsibility follows the established command
organization:

| Code | Department | Authoritative for AI content in |
|------|------------|---------------------------------|
| 100 | Command (CO, XO, Executive Director, Legal, Warfighting Readiness) | command, legal, and warfighting-readiness matters |
| 200 | Engineering and Planning (CHENG; engineers, planners) | technical and engineering matters; owns the technical library and derivative classifier |
| 300 | Waterfront Operations | availability execution, scheduling, project management |
| 500 | Supply | supply and logistics |
| 600 | Financial | budget, accounting, cost estimates |
| 700 | Crane and Rigging | crane, rigging, and lift planning |
| 900 | Production | production |
| 1100 | Manpower | manpower, training, and industrial security |
| 1200 | Business and Strategic Planning Office (BSPO) | business, strategic planning, and contracting (requirements packages) |

There is no Code 400, 800, or 1000. Quality assurance is an existing function and is
exercised as such (Section 9.b).

b. **Each department designates an authoritative AI content evaluator.** Every department
designates, in writing, a qualified person responsible for the authoritative evaluation of
AI-produced content used in that department's area of responsibility. The designated
evaluator is recorded with the department's use cases in the inventory (Section 8).

c. **Departures from specification.** Any AI suggestion that would depart from a
controlling specification (JFMM, NAVSEA Standard Item, technical manual) is processed
through the command's existing Departure-from-Specification (DFS) process. AI does not
create a path around the technical authority chain. **AI output is not, by itself,
engineering justification for a DFS** — the technical authority adjudicates independently,
on its own analysis and reference verification; AI "reasoning" is not a substitute.

d. **Out-of-band verification.** AI output that cites a technical requirement is verified
against the controlling document through a non-AI authoritative source (the official
technical library / source of record), confirming the specific paragraph wording and
current change number. **The AI's own retrieved snippet is not a sufficient verification
source** — relying on it re-introduces the hallucination it is meant to catch.
*[MAP TO COMMAND — name the authoritative source-of-record system.]*

e. **Structured approval (fight confirmation fatigue).** Where a human approval is required
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
requires a structured human approval (Section 6.e) before execution. The AI does not
take a final, state-changing action autonomously.

c. **Least privilege and permission inheritance.** An agent receives only the data and
tools its approved use case requires, and an agent acting on a user's behalf inherits that
user's access and no more. For the Local National workforce this rests on an existing
control: the command's network share is already releasability-screened and NOFORN is
excluded from it (Section 5.c), so an agent drawing on the screened corpus for a Local
National user is bounded by that user's already-screened access. The residual control is
simply to keep askSage inside that screened corpus and prevent un-screened side-channel
uploads (Section 5.c), not to re-adjudicate releasability at the AI layer.

Local National access is additionally subject to the command's existing **Foreign Disclosure**
and **export-control** processes. No askSage use case circumvents the command's Technology
Control Plans or the deemed-export rules: export-controlled (ITAR/EAR) technical data is not
exposed to a foreign national through an agent any more than it would be directly. *[MAP TO
COMMAND — name the cognizant Foreign Disclosure Officer / export-control authority.]*

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
authorities, not a single new owner and not a new board. *[WORKING GROUP TO CONFIRM the
specific billet delegations against the command SORM — for example: the Executive Director to
chair the Department Heads governance forum (Section 8.g) and maintain the AI use-case
inventory; the Executive Officer to coordinate command training (Section 13) and the
manual-reversion bills (Section 12); the CHENG as the cognizant Technical Warrant Holder; the
ISSM as the halt/revoke authority (Section 7.e).]*

b. **Command Information Officer (CIO) and Information System Security Manager (ISSM).**
Custodians of the platform, not of department content (Section 5): platform administration,
access and identity management, the model/instance and use-case inventory, the registry of
repositories connected to askSage, the Continuous Monitoring program (Section 9), the
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

e. **Department Heads.** **Own, feed, and control access to their department's repository
(Section 5.a)** and are responsible for its content and releasability; **propose** use cases
for their departments (CHENG concurs on technical scope per 8.c; CIO validates
platform/security); **designate the department's authoritative AI content evaluator
(Section 6.b)** and own the authoritative evaluation of their department's AI content;
enforce the human-in-the-loop and least-privilege requirements; submit their use cases
to the inventory; and **develop and maintain the department's information-governance plan
before access (Section 15)**.

f. **End Users.** Verify every AI output against authoritative sources (Section 6.d),
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

e. **Time-savings tracking (per project).** Consistent with Department of the Navy direction
(reference (g)), each approved use case tracks its own baseline (manual) versus AI-assisted
task time and reports the result through the department's plan (Section 15) and the governance
forum (Section 8.g). The pilot (Section 14) establishes the baselines and the tracking method.

## 10. Records management and legal hold

a. **Agentic logs are Federal Records.** An agent's prompts and chain-of-thought are
decision-support artifacts and potential evidence in a Judge Advocate General Manual
(JAGMAN) safety or mishap investigation, subject to Freedom of Information Act (FOIA) and
records obligations. They are not ephemeral chat.

b. **Retention and hold.** AI interaction logs are retained per the applicable records
schedule, with a legal-hold capability, and are managed in accordance with the records
program (reference (m)) and the SORM (reference (n)). Using AI does not waive any records,
FOIA, or privacy obligation. **Legal concurs** on retention and hold. (For the spillage
exception to ordinary retention, see Section 11.a.)

## 11. Incident reporting

The reporting chain depends on the type of incident:

a. **Spillage (security).** If classified information or NNPI is entered into askSage, or
the AI outputs apparent classified material through aggregation, the user immediately
stops the session and **does not delete the prompt** (preserve it for forensics), and
notifies the Security Manager and ISSM. The spilled material is then **isolated and routed
to the formal security spillage-cleanup and records-disposition process** — including
emergency destruction of the affected records where authorized — **only after Security
Manager and Legal adjudication.** Emergency destruction of a spilled record that is a
continuing menace is authorized under 36 CFR § 1229.10 and the emergency-destruction
provisions of the records program (references (j) and (m)); cyber-incident reporting follows
reference (k). This is the deliberate exception to ordinary records retention (Section 10): a
spilled classified record is not preserved as a permanent record inside the CUI/IL5 store.
Report through security channels, including the Naval Criminal Investigative Service (NCIS) as
required. *[CONFIRM — align this flow with the command's own spillage standard operating
procedure.]*

b. **Safety mishap (hallucination-driven).** If an AI error contributes to a safety or
quality mishap, it is reported and investigated through the command's safety and JAGMAN
channels.

c. **Rogue or anomalous agent behavior, or suspected prompt injection.** If an agent loops,
behaves erratically, attempts unauthorized access, or appears to have been manipulated —
**suspected prompt injection** (input crafted to make the AI bypass its safeguards or execute
unauthorized logic) — the user halts it (Section 7.e) and reports it to the IT help desk and
ISSM as a cybersecurity incident.

## 12. Operational resiliency (DDIL)

a. Ship repair occurs in connectivity-degraded spaces (Disconnected, Degraded,
Intermittent, Low-bandwidth, DDIL). No work center shall adopt an askSage-dependent
workflow that cannot be reverted to a manual procedure **immediately**. Every AI-enabled
workflow must have an immediately-available manual fallback, **documented in the department's
information-governance plan (Section 15)**; production never depends on AI-system availability.

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
exercise the governance before extending to write-enabled or higher-risk uses. The pilot
establishes task baselines and the per-project time-savings tracking method (Section 9.e).

c. **Framework alignment and review.** This instruction is mapped to recognized frameworks for
defensibility — the DoD AI Ethical Principles and the NIST AI Risk Management Framework
functions (Govern, Map, Measure, Manage) — and it is reviewed and updated at least annually and
upon any significant change (a new use-case class, a platform change, or a change in governing
policy). The CIO, with the CHENG and Legal, owns the review.

d. **Data residency.** Source data resides in the Navy's Flank Speed environment, which
askSage connects to, and AI processing occurs within askSage's IL5 ATO boundary — both
accredited — so residency and host-nation cryptographic requirements are expected to be
covered by those existing accreditations. *[CONFIRM — working group verifies with the
cognizant authority that the askSage ATO boundary and the Flank Speed connection satisfy
the data-residency and encryption posture.]*

e. **Working-group items.** The remaining items carried as `[CONFIRM]` and
`[MAP TO COMMAND]` markers — verifying reference identifiers, the SORM / records reference,
the spillage and records-destruction authority, the cognizant Security Classification
Guide(s), the systems of record, and named authorities (the halt authority and any
accountability delegation) — are resolved during working-group review, before promulgation.
The department structure is now embedded (Section 6.a).

---

## 15. Departmental information-governance plans

Each department stands up its own short information-governance plan for askSage, reflecting
common command expectations, before its people receive access. This instruction sets the
common floor; each code tailors it to its own work.

a. **Access prerequisite.** Before a department's personnel are granted askSage access, the
department develops a departmental information-governance plan for askSage, approved by the
Department Head. This complements individual training (Section 13): training qualifies the
*user*; the plan qualifies the *department*.

b. **High-level expectations the plan reflects.** The plan is the department's local
implementation of this instruction, grounded in industry best practice (the NIST AI Risk
Management Framework — Govern, Map, Measure, Manage) and Department practice (the DoD AI
Ethical Principles). At a minimum it addresses:
   - **Accountability and evaluation** — the department's accountable owner and its designated
     authoritative AI content evaluator (Section 6.b).
   - **Use cases and risk** — the department's approved askSage use cases, each classified by
     risk (Section 7.d) and entered in the command inventory (Section 8.g).
   - **Data boundaries** — the authorized data its use cases touch, and the prohibited-data
     line (Section 4).
   - **Repository and access** — the department's repository, what it feeds into it, and who
     may access it (Section 5).
   - **Human-in-the-loop** — how the department applies authoritative evaluation and structured
     approval to its AI output (Section 6).
   - **Monitoring and records** — how the department supports continuous monitoring (Section 9)
     and meets records and retention obligations (Section 10).
   - **Manual fallback** — the documented immediate-reversion procedure for each AI-enabled
     workflow (Section 12).

c. **Living document.** The plan is maintained as the department's use cases change and is
reviewed alongside the use-case inventory in the governance forum (Section 8.g). *[MAP TO
COMMAND — provide a one-page departmental information-governance plan template so the plans are
consistent across codes.]*

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
- **Efficiency.** Indexing large references once at the repository level (Section 5) and a
  shared, vetted prompt library reduce waste. Develop and test agents and agentic-workflow
  prompts on GenAI.mil first, then run the finished workflow on askSage, to conserve askSage
  tokens (Section 2).

---

*End of draft v0.11. Prior versions retained at instruction-v0.1.md … v0.10.md;
logic-pass record at instruction-red-team.md; department glossary at _glossary.md. Clean
working-group routing package at routing/ (rebuilt from this version).*

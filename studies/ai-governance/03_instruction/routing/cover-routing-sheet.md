# SRF-JRMC askSage Governance Instruction — Working-Group Routing & Comment Sheet

**Subject:** Draft SRF-JRMC Instruction 5239.1, *Governance, Security, and Use of the
askSage Artificial Intelligence Platform*

**From:** [Originator] · **To:** AI Governance Working Group · **Date:** ______ ·
**Comments due:** ______

---

## What this is

A working draft of the command instruction governing how SRF-JRMC uses askSage. It is
**for review and markup**, not yet for signature. Please read the attached draft, mark it
with track-changes and comments, and return by the date above. The draft is built to a
**best-in-class** posture and maps to the DoD AI Ethical Principles and the NIST AI Risk
Management Framework so it is defensible on its face.

## What is already decided (please do not relitigate without a substantive reason)

- **Platforms:** the command uses **both askSage and GenAI.mil**. Recommended split:
  GenAI.mil for general questions, **askSage for agentic work** (prototype agents/prompts on
  GenAI.mil first to save askSage tokens). askSage is ATO'd at IL5 and connects to Flank
  Speed; this instruction governs askSage, GenAI.mil runs under its DoD enterprise governance.
  GenAI.mil is the enterprise *default*, not an exclusive bar — askSage is separately
  authorized and acquired via decentralized task orders against the **Army Ask Sage IDIQ
  (W9128Z25DA001)**, the same vehicle other Navy activities (NSWC Corona, NRL) already use.
- **Data:** **CUI authorized up to IL5; PII and PHI prohibited** (carved out), as are
  classified and NNPI.
- **The AI changes no existing process.** It governs askSage use within the command's
  established authorities, quality, security, and records processes. Where it names who is
  responsible, it restates the established line.
- **AI is decision support, not authority:** AI output is authoritatively evaluated by the
  cognizant authority **along existing lines of responsibility** — the department that owns
  that subject matter (the Code 100–1200 map is embedded in §6.a) — and **each department
  designates an authoritative AI content evaluator**. AI output is always a non-authoritative
  draft.
- **Knowledge base is federated:** each department owns, feeds, and controls access to its
  own repository; Code 200 owns the technical library and the derivative-classifier
  screening; the CIO/ISSM is custodian of the platform (connection registry, access,
  monitoring), not the content.
- **Governance is run through existing structures:** Legal concurs on records; **Department
  Heads are the governance forum, reviewing the use-case inventory quarterly.** No new board.
  Records and directives are managed per the command SORM.
- **Other settled calls:** immediate manual fallback (DDIL); token/compute control demoted
  to an administrative annex with a mission-critical override; aggregation handled through
  the existing Security Classification Guide and spillage procedures.

## What we need from the working group

Substantive review on feasibility and correctness, and resolution of the items the draft
flags inline as **"Working group to resolve"** (also listed here):

1. Verify the reference identifiers (refs e, f, g, j) and add the command's cognizant
   cybersecurity, records-management, and security-spillage references.
2. Record the command's askSage acquisition instrument — its task-order PIID off the Army Ask
   Sage Decentralized IDIQ (W9128Z25DA001) — plus the IL5 ATO reference and the Flank Speed
   connection authority (§2).
3. Name the governing SORM / records-management reference (§5.a) and the cognizant Security
   Classification Guide(s) (§4.e).
4. Each department names its authoritative AI content evaluator; confirm the Technical
   Warrant Holder billets within Code 200 (§6). *(The Code 100–1200 structure is already
   embedded in §6.a.)*
5. Name the authoritative source-of-record system used for out-of-band verification (§6.d).
6. Name the halt/revoke authority for a rogue agent (§7.e).
7. Confirm any delegation of accountability (e.g., to the Executive Director) (§8.a).
8. Align the spillage flow with the command's actual spillage and records-destruction
   procedures (§11.a).
9. Verify the data-residency and encryption posture with the cognizant authority (§14.d).

Beyond these, flag anything that conflicts with existing command process, is not feasible
as written, or is missing.

## Comment resolution (working group use)

| # | Section | Reviewer | Comment | Disposition |
|---|---------|----------|---------|-------------|
|   |         |          |         |             |
|   |         |          |         |             |
|   |         |          |         |             |

---

*Attachment: Draft SRF-JRMC Instruction 5239.1 (for working-group review).*

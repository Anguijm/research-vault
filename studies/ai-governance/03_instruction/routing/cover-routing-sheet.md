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
  authorized at IL5 and acquired through a Department contract vehicle for askSage (e.g., the
  Army-managed Ask Sage IDIQ that NSWC Corona and NRL already use). The specific ATO and
  contract are held in command records, not in the instruction (which stays stable as contracts
  renew).
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
- **Each department stands up its own information-governance plan before askSage access** (§15)
  — common high-level expectations (grounded in the NIST AI RMF + the DoD AI Ethical Principles),
  tailored by each code; a department-level access gate alongside individual training.
- **Per-project time-savings tracking** (§9.e): each approved use case tracks its own baseline-
  vs-AI-assisted time and reports it, per the March-2026 DON CIO direction; the pilot establishes
  the baselines and method.
- **Other settled calls:** immediate manual fallback (DDIL); token/compute control demoted
  to an administrative annex with a mission-critical override; aggregation handled through
  the existing Security Classification Guide and spillage procedures.

## What we need from the working group

Substantive review on feasibility and correctness, and resolution of the items the draft
flags inline as **"Working group to resolve"** (also listed here):

1. References (e)–(n) are now **verified and folded in** (incl. SECNAVINST 5239.19A, SECNAVINST
   5510.36B / SECNAV M-5510.36, SECNAV M-5210.1, OPNAVINST 3120.32D = the SORM). Working group:
   substitute the command's *local* references (its command SORM and local spillage SOP) and
   confirm the exact date of the March-2026 DON CIO memo in (g).
2. Confirm askSage's IL5 authorization (ATO) and the command's acquisition instrument are
   current and valid — held in the command's cybersecurity and contracting records, not in the
   instruction — and confirm the Flank Speed connection authority (§2).
3. Name the cognizant Security Classification Guide(s) (§4.e). *(The SORM/records references
   are now cited — OPNAVINST 3120.32D and SECNAV M-5210.1; substitute the local command SORM.)*
4. Each department names its authoritative AI content evaluator; confirm the Technical
   Warrant Holder billets within Code 200 (§6). *(The Code 100–1200 structure is already
   embedded in §6.a.)*
5. Name the authoritative source-of-record system used for out-of-band verification (§6.d).
6. Name the halt/revoke authority for a rogue agent (§7.e).
7. **Confirm the specific billet delegations against the command SORM** (§8.a) — e.g., Executive
   Director to chair the governance forum + own the inventory; XO for training + manual-reversion
   bills; CHENG as Technical Warrant Holder; ISSM as halt/revoke authority.
8. Align the spillage flow with the command's own spillage SOP (§11.a). *(The legal authority —
   36 CFR 1229.10 + SECNAV M-5210.1 emergency destruction — is now cited.)*
9. Verify the data-residency and encryption posture with the cognizant authority (§14.d).
10. Adopt/finalize the one-page departmental information-governance plan template (§15.c). **A
    draft template is provided** (`Departmental-AI-Governance-Plan-TEMPLATE.docx`); the working
    group reviews and adopts it so the codes' plans are consistent.

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

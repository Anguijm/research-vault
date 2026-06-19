# Open items worksheet — askSage instruction

**One place to resolve everything the instruction left to the command.** Fill in the
`ANSWER:` lines (in Obsidian, on any device), **or** just tell Claude the answers in
chat — either way, Claude records them in `_decisions.md` and replaces the matching
markers in the instruction to produce v0.3. Section references point into
`03_instruction/instruction-v0.2.md`.

Status key: ☐ open · ☑ answered.

**Status 2026-06-19:** Section A answered and folded into instruction **v0.3**
(`03_instruction/instruction-v0.3.md`) and `_decisions.md` (items 8–14). Sections B and
C are **deferred to the working group** per the operator and remain as `[CONFIRM]` /
`[MAP TO COMMAND]` markers in v0.3.

---

## A. Strategic decisions (these shape the whole instruction)

☑ **A1. Instance basis — standalone askSage, or ride GenAI.mil?** (§2)
Does the command stand up its own askSage instance, or use the DoD enterprise platform
(GenAI.mil) and inherit its Authority to Operate, vendor data terms, and platform
guardrails? This changes several paragraphs.
ANSWER: standalone AskSage______________________________________________

☑ **A2. Approved Impact Level — IL4 or IL5?** (§4.a)
ANSWER: il5______________________________________________

☑ **A3. Maturity target — compliance-minimum or best-in-class?** (§14; gap-analysis F.5)
Sets how heavy the build is.
ANSWER: best in class______________________________________________

☑ **A4. Data residency / host-nation cryptographic compliance.** (§14)
Where the IL5 data physically lives; any host-nation admin-access or encryption
constraints. Confirm with the cognizant authority.
ANSWER: covered by existing processes, I'd think______________________________________________

☑ **A5. Governance forum + review cadence.** (§8.g)
Which existing command forum reviews the AI use-case inventory, and how often (recommend
quarterly)?
ANSWER: Department Heads Quarterly ______________________________________________

☑ **A6. Manual-fallback standard (DDIL).** (§12)
The revert-to-manual time standard for any AI-enabled workflow (e.g., within one working
hour).
ANSWER: Immediately ______________________________________________

☑ **A7. Aggregation agent-scoping — keep or drop?** (§4.e)
Optional defense-in-depth: scope an agent's default horizontal data reach below the
user's full access to lower inadvertent one-prompt compilation. Lowers inadvertence at a
friction cost; does not reduce the underlying risk. Keep or drop?
ANSWER: drop______________________________________________

---

## B. Confirmations / verifications (check against authoritative sources) — *deferred to working group*

☐ **B1. Reference identifiers.** (References, esp. (e) DoDI 5400.19, (f) the CDAO July-2024
GenAI guidance, (g) the DON CIO / GenAI.mil memos, (j) 36 CFR 1229.) These came from
open-source research and must be verified against the actual issuances before promulgation.
ANSWER / corrections: ______________________________________________

☐ **B2. Security spillage + records-destruction alignment.** (§11.a)
Confirm the §11.a spillage flow (stop, don't delete, isolate, route to cleanup/emergency
destruction after Security Manager + Legal) matches the command's actual spillage
procedure and records-destruction authority.
ANSWER: ______________________________________________

☐ **B3. Screening process + authoritative-corpus source.** (§5.c)
Confirm the derivative-classifier screening of technical direction as described, and name
the screened authoritative-corpus source the knowledge base will index from.
ANSWER: ______________________________________________

---

## C. Command-specific mappings (swap the generic placeholders for real structure) — *deferred to working group*

☐ **C1. Cognizant Security Classification Guide(s).** (§4.e)
ANSWER: ______________________________________________

☐ **C2. Knowledge-base recertification owner + cadence.** (§5.b)
ANSWER: ______________________________________________

☐ **C3. Engineering & Quality-Assurance codes + Technical Warrant Holder assignments.** (§6.a)
The real codes for the CHENG chain — Claude did not assert these.
ANSWER: ______________________________________________

☐ **C4. Authoritative source-of-record system for out-of-band verification.** (§6.c)
The non-AI technical library / system of record users verify against.
ANSWER: ______________________________________________

☐ **C5. Halt / revoke authority.** (§7.e)
Who can halt an agent and revoke its access (ISSM, duty IT watch, etc.)?
ANSWER: ______________________________________________

☐ **C6. Accountability delegation.** (§8.a)
The CO is named as accountable authority; delegate as appropriate (e.g., Executive
Director)?
ANSWER: ______________________________________________

---

*When these are answered, Claude folds them into `_decisions.md`, replaces the markers
in the instruction, and produces a promulgation-shaped v0.3. The "Still open" list in
`_decisions.md` is the short version of Section A above.*

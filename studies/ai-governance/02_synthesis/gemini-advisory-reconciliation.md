---
type: synthesis
study: ai-governance-landscape
title: Reconciliation — Gemini "Finalizing the askSage Framework" advisory vs. our instruction
status: v1.0
classification: internal
created: 2026-06-21
reconciles: 01_sources/gemini-advisory-2026-06-finalizing-askSage-framework.txt
against: 03_instruction/instruction-v0.9.md + _decisions.md
verification: 2 web-research subagents + USASpending (lib/usaspending.py), 2026-06-21
---

# Reconciliation of the Gemini advisory

A claim-by-claim disposition of the Gemini report (`report.txt` from the operator's Drive)
against our instruction and the operator's decisions. Per the vault's cross-AI verification
rule, nothing in Gemini's output is adopted without checking against a primary/authoritative
source. **Headline:** Gemini's factual research (references, contract data) is largely solid;
its two policy *recommendations* (reopening PHI/PII, relaxing NNPI) are rejected by operator
decision.

## A. REJECTED — operator decisions (firm)

1. **Reopen the PHI/PII prohibition — REJECTED.** Operator 2026-06-21: "PII/PHI still out. No
   question." Gemini argued the carve-out is mere "command risk tolerance" because Ask Sage got
   a Defense Health Agency (DHA) PHI authorization. *Verification:* the DHA agreement is real
   (GlobeNewswire, 2025-12-08), but the "first/only IL5-authorized to process PHI" superlative
   is **vendor-press-release only — no government confirmation.** Either way it does not move the
   command's position. PII/PHI remain prohibited (§4.b unchanged).
2. **Relax the NNPI ban to allow Unclassified NNPI (U-NNPI) — REJECTED.** Operator: "NNPI
   completely off limits." *Verification:* the underlying capability is actually **real** —
   PEO Digital deployed Microsoft Purview sensitivity labels to the NNPI community of interest in
   Flank Speed (late Aug 2024), enabling authorized U-NNPI handling. But the command's absolute
   prohibition is a **deliberate, defensible risk-tolerance decision** (avoiding aggregation risk
   on an industrial ship-repair network). NNPI stays fully prohibited (§4.b unchanged).

*(Both are also vendor/marketing-tinged where Gemini overstates; but the operator decision is
the controlling reason.)*

## B. VERIFIED + ACCEPT — fold into the instruction (a v0.10)

3. **Reference identifiers — VERIFIED, resolve the §14.e / references markers.** All check out:
   - DoDI 5400.19 (Public Affairs Use of AI), CDAO "Guidelines and Guardrails" (12 Jul 2024),
     DON CIO GenAI.mil designation (28 Jan 2026) — already in our refs, now confirmed.
   - **SECNAVINST 5239.19A** — DON Computer Network Incident Response & Reporting (2019). ✓
   - **SECNAVINST 5510.36B** — DON Information Security Program (2019); **SECNAV M-5510.36** is the
     implementing manual. ✓
   - **SECNAV M-5210.1** — DON Records Management Manual (disposition schedules). ✓
   - **OPNAVINST 3120.32D** — Standard Organization and Regulations of the U.S. Navy (the SORM),
     current revision **D** w/ CH-1 (2017). ✓ *(Note: cite the command's local SORM where it
     exists, with 3120.32D as the Navy-wide parent.)*
   - **36 CFR 1229.10** (records a "continuing menace") and **36 CFR 1229.12** (destruction
     outside U.S. during war; NARA report within 6 months). ✓ — Gemini's descriptions match eCFR.
4. **Records-vs-spillage emergency-destruction authority — VERIFIED, resolves our §11.a [CONFIRM].**
   36 CFR 1229.10 (+ SECNAV M-5210.1 emergency-destruction provisions) is the real legal basis for
   the "isolate then destroy the spilled record" step our §11.a already describes. Fold the citation
   in.
5. **Authority/waiver basis + Cattle Drive context — ACCEPT as context (see §2).** Gemini's point
   that the command should register the askSage use case with the DON CIO GenAI Task Force and
   document the agentic-capability gap as the justification for an exception is sound and aligns
   with our §2 authority basis. *(This is a command action; the instruction can note it.)*
6. **Billet/role map — ACCEPT with operator confirmation.** Gemini maps: CO (accountable),
   Executive Director (chairs the Dept-Heads governance forum + owns the inventory), XO (training +
   manual-reversion bills), CHENG (Technical Warrant Holder), ISSM (platform custodian, halt/revoke),
   Dept Heads (own repos), evaluators (designated SMEs, out-of-band verification). This is consistent
   with our §6/§8. **Operator confirms** the specific delegations (esp. ED chairing the forum, XO
   owning training) before they go in.

## C. VERIFIED-BUT-CORRECT / FLAG (do not import as-is)

7. **OPNAVSTAFFINST 5510.168 — exists, but WRONG INSTRUMENT.** It is the *OPNAV-staff-internal*
   "Cybersecurity Violation and Remediation Policy," not a Navy-wide or command spillage authority.
   Do not cite it as SRF-JRMC's spillage procedure; use the command's own/echelon spillage process
   plus SECNAVINST 5239.19A. **Gemini misapplied this one.**
8. **askSage "IL6 / Top Secret / processes classified" — vendor-asserted, UNVERIFIED, and
   irrelevant.** The IL6/TS line traces to Ask Sage marketing (Breaking Defense says it "boasts");
   no government confirmation, and IL6 = SECRET (not TS) anyway. Our instance is IL5 and classified
   is prohibited — do **not** import the IL6/TS framing.
9. **"March 16, 2026" DON CIO AI-adoption memo — real, confirm specifics.** The memo exists
   (accelerating AI adoption, free training, time-savings tracking, DON AI Efficiency Challenge);
   the exact date, the "NPS Harnessing AI" course name, and the literal "AI Time Savings Survey"
   label could not be independently confirmed (pages blocked) — confirm against the issuance.
10. **Cattle Drive ownership — correct it.** Run by the **DON CIO**, not "PEO Digital" as Gemini
    stated. (See the Cattle Drive note below.)

## D. GEMINI CONSTRUCTS — not adopted (consistent with prior decisions)

11. **"Risk Exposure Score" (R_E = L × I_max, ≥15 = high-risk) — NOT ADOPTED.** This is Gemini's
    invented math with false precision. We already decided to **map risk to existing Navy
    controlled-work categories** (Level I / critical), not invent a parallel scoring scheme
    (`_decisions.md` item 16). Keep our approach.
12. **"Token Efficiency Ratio" — NOT ADOPTED.** Another Gemini construct; Annex A already handles
    cost as a guardrail, not a governance pillar.
13. **Optional, operator's call (low-stakes):** the 5-part prompt model (Persona/Context/Ask/
    Constraints/Validation) as a training aid; tracking/reporting time savings per the March-2026
    DON memo; enriching our departmental template with NIST-RMF (Govern/Map/Measure/Manage) framing
    and a primary/alternate-evaluator field. These are reasonable adds if the operator wants them.

## E. Contract data — VERIFIED against USASpending (authoritative)

Gemini's contract facts check out:
- **W9128Z25DA001** — USASpending description confirms "SMALL BUSINESS INNOVATIVE RESEARCH PHASE
  III INDEFINITE DELIVERY INDEFINITE QUANTITY CONTRACT." Contracting office = **ACC-APG** (RCCTO is
  the sponsoring org; the W9128Z code is RCCTO's). The "$49M ceiling / Feb-2030 end" are from
  secondary sources (not in the API field) but consistent.
- **FA489025F0102** — $49,500, Air Force (HQ ACC AMIC), "ASK SAGE ARMY DECENTRALIZED IDIQ… annual
  subscription, 100M tokens." ✓ matches Gemini.
- **W9128Z25FA004** — $81,120, Army, "in support of ASA(ALT) HQ." ✓ matches Gemini.
- **N0017326F0400** — $24,750, Navy (Naval Research Laboratory), Org 6300. ✓ (our prior finding).

## Bottom line

Fold into v0.10: the verified references (item 3), the §11.a records-destruction CFR authority
(item 4), and the Cattle-Drive/waiver context for §2 (item 5). Confirm-then-fold: the billet
delegations (item 6). Reject: PHI/PII and NNPI (A). Correct/flag, don't import: OPNAVSTAFFINST
5510.168, the IL6/TS framing, the Cattle-Drive-ownership error (C). Decline: the R_E and
Token-Efficiency math (D). Operator's call: the optional training/template adds (item 13).

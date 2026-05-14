---
type: red_team_report
opportunity: PMTEC-USINDOPACOM
reviewed: capture-brief-v0.3-draft.docx
model: gemini-3.1-pro-preview
date: 2026-05-14
prompt_source: _meta/prompts/cross-ai-red-team.md
raw_json: _red-team-2026-05-14-gemini-3.1-pro-preview.json
---

# Red-Team Review — PMTEC-USINDOPACOM

**Subject:** `capture-brief-v0.3-draft.docx`  ·  **Reviewer:** `gemini-3.1-pro-preview`  ·  **Generated:** 2026-05-14T12:14:54

## At a glance

| Verdict | Total | 🔥 Critical | 🔴 High | 🟡 Medium | 🟢 Low |
|---|---|---|---|---|---|
| **🔁 ITERATE** | 5 | 1 | 2 | 1 | 1 |

**SOP threshold:** more than 2 findings → brief not yet ready (see `_meta/prompts/cross-ai-red-team.md`).

## TL;DR

> The brief identifies strong capability overlaps but fails on execution mechanics and internal consistency. It asks the government to do the heavy lifting on declassification (Play 1), dictates inefficient split-procurements to avoid teaming (Play 3), and pitches unproven cross-integration of a 2-month-old $2.6B acquisition (ARKA). Furthermore, the BLUF contradicts the actual executive asks regarding Play 1 funding.

---

## 🔥 CRITICAL  (1)

### #1  ·  §1 · §9 · §10.3  ·  Contradictory capture asks and poor worst-case ROI

*Flagged by: Skeptical exec*

**Issue.** The BLUF requests immediate B&P funding for Plays 1-3, but §9 explicitly states Play 1 is gated behind a 30-day TAM exercise. Additionally, asking for up to $3M in B&P against a worst-case expected revenue of $15M is a massive red flag.

**Why it matters.** An executive will reject the brief immediately if the upfront ask contradicts the decision gates, or if the downside financial risk (5x topline, meaning negative profit ROI) is not mitigated.

**Fix.** Align the BLUF to match §9 (Plays 2 & 3 only, Play 1 gated). Gate the $1.5M-$3M B&P spend into tranches, releasing the bulk only after the 30-day TAM validation.

> _“Investment ask: B&P for plays (a)–(c) capture activation”_ — from the brief

---

## 🔴 HIGH  (2)

### #2  ·  §7.1  ·  Pitching a solution that assigns homework to the customer

*Flagged by: J7 staffer*

**Issue.** Play 1 (Spectral-Lite) requires the government to handle IC declassification, J6 frequency allocation, and PEO IWS deconfliction before CACI can build the solution.

**Why it matters.** J7 wants turnkey training solutions, not massive interagency coordination hurdles. Telling the customer that their effort is a 'precondition' to your play will result in immediate pushback.

**Fix.** Reframe Play 1 to demonstrate how CACI will facilitate these approvals using existing cleared personnel and established range spectrum playbooks, rather than making it the government's problem.

> _“the government, not CACI, must define what UNCLASSIFIED reduced-fidelity dataset is releasable... J6 partnership and IC declassification scoping is a precondition”_ — from the brief

### #3  ·  §6.2 · §7.1 · §8  ·  Premature and unproven ARKA integration claims

*Flagged by: Competitor · Skeptical exec · J7 staffer*

**Issue.** The brief maps ARKA's 'Agentic AI' to SIGINT digital twins, despite the acquisition closing just two months ago (March 2026).

**Why it matters.** Competitors will easily ghost this as vaporware. Execs will reject pitching an unintegrated asset for cross-domain SIGINT. Customers will see through 'Agentic AI' buzzwords applied outside their proven EO/IR scope.

**Fix.** Strip claims about ARKA processing SIGINT for digital twins. Focus strictly on ARKA's existing, proven EO/IR commercial capabilities as a standalone wedge for the DIU HSA demo.

> _“autonomous threat-classification models running over EO/IR/hyperspectral and SIGINT data”_ — from the brief

---

## 🟡 MEDIUM  (1)

### #4  ·  §7.1  ·  Dictating a split procurement for C-UAS instead of teaming

*Flagged by: Competitor · Skeptical exec*

**Issue.** Play 3 tells the government to issue a separate OPFOR swarm award because CACI doesn't want to grade its own homework, rather than offering a unified solution.

**Why it matters.** Competitors will offer a turnkey OPFOR + grading solution to make procurement easy. Execs will question why CACI isn't forming a prime/sub team with an OPFOR vendor and managing the OCI via internal firewalls.

**Fix.** Propose a teaming arrangement with an OPFOR vendor (e.g., Shield AI) with a strict internal firewall, offering the government a single, easy-to-buy contract vehicle.

> _“EXPLICITLY recommend the government issue a SEPARATE, INDEPENDENT OPFOR swarm-target award”_ — from the brief

---

## 🟢 LOW  (1)

### #5  ·  §6.1  ·  Relying on external OSINT for a contract CACI is already on

*Flagged by: Skeptical exec*

**Issue.** The brief relies on HigherGov for the $467M ceiling of the Deloitte INDOPACOM Alpha contract, despite CACI being an active subcontractor on it.

**Why it matters.** It shows a lack of internal coordination. If CACI is billing on this contract, the capture team should have exact ceiling and headroom numbers from their own delivery PM.

**Fix.** Contact the internal CACI delivery lead for the Deloitte subcontract to verify the ceiling, remaining headroom, and actual task order dynamics.

> _“$467M ceiling... remain industry-reported (HigherGov) only”_ — from the brief

---

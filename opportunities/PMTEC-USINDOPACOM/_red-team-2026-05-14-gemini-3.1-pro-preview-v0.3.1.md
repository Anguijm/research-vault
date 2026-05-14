---
type: red_team_report
opportunity: PMTEC-USINDOPACOM
reviewed: capture-brief-v0.3.1-draft.docx
model: gemini-3.1-pro-preview
date: 2026-05-14
prompt_source: _meta/prompts/cross-ai-red-team.md
raw_json: _red-team-2026-05-14-gemini-3.1-pro-preview-v0.3.json
---

# Red-Team Review — PMTEC-USINDOPACOM

**Subject:** `capture-brief-v0.3.1-draft.docx`  ·  **Reviewer:** `gemini-3.1-pro-preview`  ·  **Generated:** 2026-05-14T13:55:59

## At a glance

| Verdict | Total | 🔥 Critical | 🔴 High | 🟡 Medium | 🟢 Low |
|---|---|---|---|---|---|
| **🔁 ITERATE** | 5 | 1 | 2 | 2 | 0 |

**SOP threshold:** more than 2 findings → brief not yet ready (see `_meta/prompts/cross-ai-red-team.md`).

## TL;DR

> The brief identifies strong tactical alignment with PMTEC gaps but fails the exec and customer tests due to internal contradictions, incomplete homework, and arrogant posturing. It contradicts itself on ARKA's SIGINT capabilities, asks the government to solve CACI's product feasibility issues, and requests $3M in immediate B&P funding based on unverified, low-confidence TAMs.

---

## 🔥 CRITICAL  (1)

### #1  ·  §6.1 · §6.2  ·  Contradiction on ARKA SIGINT capabilities

*Flagged by: Competitor · Skeptical exec*

**Issue.** Section 6.1 explicitly states ARKA does not market SIGINT, but the table in Section 6.2 claims ARKA's AI models run over SIGINT data.

**Why it matters.** Competitors will ghost CACI for selling vaporware, and an exec will reject the brief for internal contradictions regarding a newly acquired $2.6B asset.

**Fix.** Remove references to ARKA's AI running over SIGINT data in §6.2, or explicitly clarify that CACI must build this integration post-acquisition.

> _“autonomous threat-classification models running over EO/IR/hyperspectral and SIGINT data”_ — from the brief

---

## 🔴 HIGH  (2)

### #2  ·  §7.1  ·  Asking the customer to solve product feasibility

*Flagged by: J7 staffer · Competitor*

**Issue.** The 'Spectral-Lite' play requires the government (J6/J7) to figure out classification, frequency allocation, and deconfliction before CACI even builds the solution.

**Why it matters.** A J7 customer will reject this as 'the contractor asking us to do their homework,' and competitors with existing unclassified training EW systems will win easily.

**Fix.** Shift the burden to CACI. Propose a funded study or use internal IRAD to determine classification and spectrum feasibility before asking the customer to commit.

> _“the government, not CACI, must define what UNCLASSIFIED reduced-fidelity dataset is releasable”_ — from the brief

### #3  ·  §9 · §10.3  ·  Premature B&P funding request with low ROI confidence

*Flagged by: Skeptical exec*

**Issue.** Asking for immediate authorization of $1.5M-$3M in B&P for Plays 2 and 3 when the TAM is highly speculative and the lower-bound expected revenue is only $15M.

**Why it matters.** An exec will not authorize $3M in capture funds for a 'LOW confidence' TAM where the worst-case revenue barely clears a 5x multiple.

**Fix.** Gate all capture activation funding behind the 30-day TAM-sizing exercise, rather than asking for immediate authorization for Plays 2 and 3.

> _“Authorize capture team activation for Plays 2... and 3... IMMEDIATELY.”_ — from the brief

---

## 🟡 MEDIUM  (2)

### #4  ·  §7.2  ·  Incomplete intelligence on JHU partnership

*Flagged by: Skeptical exec · Competitor*

**Issue.** The brief proposes a partner play with JHU but admits it doesn't even know which JHU unit is involved, guessing it might be APL.

**Why it matters.** Shows a lack of basic capture homework. A 4-minute exec read will flag this as unpreparedness and say 'come back when you know who we are partnering with.'

**Fix.** Remove the JHU partner play from the decision brief until the 30-day outreach confirms the unit and actual partnership scope.

> _“specific JHU unit unconfirmed in ingested sources”_ — from the brief

### #5  ·  §7.1  ·  Dictating acquisition strategy to the customer

*Flagged by: J7 staffer*

**Issue.** Recommending the government issue a separate, independent OPFOR award just to accommodate CACI's OCI and product limitations on C-UAS.

**Why it matters.** J7 will view this as arrogant and self-serving, pushing back on a vendor trying to complicate their procurement to fit a specific bid strategy.

**Fix.** Frame the independent OPFOR as a best-practice for objective validation (Red vs Blue separation) rather than an EXPLICIT demand to accommodate CACI.

> _“EXPLICITLY recommend the government issue a SEPARATE, INDEPENDENT OPFOR swarm-target award”_ — from the brief

---

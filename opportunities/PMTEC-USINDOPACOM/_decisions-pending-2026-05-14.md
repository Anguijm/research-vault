---
type: decisions_pending
opportunity: PMTEC-USINDOPACOM
date: 2026-05-14
status: blocking_brief_v0.4
---

# Decisions pending — PMTEC capture brief v0.3 → v0.4

After three Gemini 3.1 Pro red-team passes (v0.1 → v0.3, 14 → 13 → 12 findings)
the remaining issues are **business decisions, not editorial fixes**. This memo
names the five decisions, who owns them, and what unblocks each.

Pick this up at the BD-team meeting (or wherever the call sheet lands). v0.4
is gated on **decisions A + B answered**; the other three improve quality but
don't block the next red-team.

---

## Decision A — Phone calls before paperwork *(blocks Play 1 ask)*

**What to do:** Two ~30-minute phone conversations in the next ~5 business days.

### A.1 — Brent Parker (PMTEC Industry Engagement Lead)

- **Contact:** `brent.m.parker2.ctr@us.navy.mil` (verify .ctr address still active before sending; he's contractor staff, address tied to contract period)
- **Goal:** Determine how PMTEC will actually procure non-kinetic effects simulation (Play 1)
- **Specific questions to ask:**
  1. Is the non-kinetic effects simulation gap most likely to be procured via DIU OTA, an OASIS task order, a new PMTEC-specific vehicle, or rolled under JFDD/JDECC Navy line items?
  2. What's the realistic FY26/FY27 RFP cadence for PMTEC priority gaps? (We're estimating Q1 FY27 based on quarterly-meeting cadence — confirm.)
  3. Are there any pre-RFP industry days, RFIs, or sources-sought notices in the next 90 days we should prepare for?
  4. Who else on the J7 / J83 side is the formal acquisition POC vs. the technical POC for each play?
- **What success looks like:** specific vehicle + estimated dollar range + RFP-drop timing window
- **What to do with the answer:** updates §10.1 TAM (Play 1), unlocks §9 Play 1 capture-team authorization with real numbers

### A.2 — Stridiron's office (PMTEC Program Manager)

- **Contact:** via Brent Parker or via DIU OnRamp Hub: Hawaii (Larry Jordan — warm intro)
- **Goal:** Confirm the Johns Hopkins University partnership specifics
- **Specific questions to ask:**
  1. Which JHU unit is the AI / digital-twin research partner? APL? Whiting School? SAIS? Other?
  2. Is the partnership scope public, NDA-only, or under formal CRADA?
  3. Is there a role for industry data contribution (CACI's SIGINT/EW telemetry as model input), and if so via what mechanism?
- **What success looks like:** named JHU unit + scope + industry-engagement mechanism (NDA / CRADA / open)
- **What to do with the answer:** updates §3.1 priority #5 + §7.2 + §9 + Appendix A.5; eliminates 2 red-team findings flagged across v0.2 and v0.3 as guessing

---

## Decision B — Financial-credibility framing *(blocks the exec ask)*

**The math problem Gemini exposed:**

> Lower-bound case: $15M revenue × 10–15% defense-services gross margin = $1.5M–$2.25M gross profit; minus $3M B&P = NET LOSS at the lower-bound capture probability.

Three honest paths forward. Pick one before v0.4.

| Path | What it means | Who owns the change |
|---|---|---|
| **B.1 Narrow scope** | Drop Play 1 from the capture-activation ask. Activate only Plays 2 + 3 (which had MEDIUM confidence in §10). Re-quote a tighter B&P number for 2 plays vs. 3. | Operator + capture lead |
| **B.2 Defend higher capture probability** | Quote a higher lower-bound capture probability (e.g., 25–35% instead of 10–30%) using internal CACI win-rate data on similar EW/SIGINT plays. Defend with specifics, not optimism. | Operator + BD analytics |
| **B.3 Strategic-positioning framing** | Re-cast plays 1–3 not as standalone ROI bids but as ARKA-integration market validation. The metric becomes "post-ARKA market repositioning" not "FY27 revenue ÷ B&P." Requires C-suite to accept positioning-investment framing. | Operator + C-suite |

Most defensible: **B.1 (narrow scope)** combined with a smaller follow-on
ask for Play 1 once Decision A answers come back. This is also what Gemini's
"Skeptical Exec" voice is pushing toward.

---

## Decision C — Spectral-Lite concept *(reduces v0.4 finding count)*

The current Play 1 framing asks the customer to lead an interagency
declassification effort to release reduced-fidelity EW data to a coalition
training enclave. Gemini's J7 staffer reframed this as *"a massive
interagency declassification science project, not a procurable solution."*

Two paths:

| Path | What changes |
|---|---|
| **C.1 Synthetic-signatures Phase 1** | Drop "reduced-fidelity Spectral data" entirely. Lead with synthesized / modeled EW signatures (built from open-source threat libraries + CACI's own threat-modeling). Declassification not required. Phase 2 (live Spectral data) follows after government leads a declassification scoping effort. |
| **C.2 Sub-only on Play 1** | Drop Play 1 from CACI's prime list entirely. Offer it as a sub to a primary EW prime that already has the appropriate clearances + customer relationships for the declassification path. |

C.1 is more aligned with current brief structure (still a prime play, just
re-scoped). C.2 simplifies the brief but cedes the prime position.

---

## Decision D — Lockheed JFN strategy *(quality, not blocking)*

L3Harris has two years of integration reps on JFN at VS24/VS26. v0.3
acknowledges this and proposes complementary plug-ins on post-ARKA
space-to-JFN feeds.

Gemini still flags this as ghostable. Real fix: pick the JFN play L3Harris
*isn't* already integrated on:

| Option | Defensibility |
|---|---|
| **D.1 EW thread sub to Lockheed** | Uphill — L3Harris has the inside track. Don't pursue. |
| **D.2 Space-to-JFN feed sub via ARKA** | Cleaner — L3Harris isn't on this thread. Pursue and frame as the actual play. |
| **D.3 Drop JFN sub from the brief entirely** | Honest if the analysis says CACI can't win it. Frees focus for Plays 1–3. |

Recommend **D.2**; cleanest defensible position.

---

## Decision F — Strip ARKA SIGINT scope claims *(NEW — from v0.3 clean red-team #3)*

**The factual issue:** v0.3 brief in places said *"autonomous threat-classification models running over EO/IR/hyperspectral and SIGINT data."* ARKA's actually-proven product scope per the CACI press release and 10-Q is **EO/IR + hyperspectral imaging only** — ARKA does not market a SIGINT offering. The SIGINT inference was our own bridge between ARKA's autonomous-AI capability and CACI's separate legacy SIGINT products (Spectral, Trojan).

**Path forward (recommended F.1):** Strip every "ARKA … SIGINT" combination from external materials. Keep SIGINT discussion strictly in CACI-legacy contexts (Spectral, Trojan). When pitching ARKA, stay in the EO/IR + hyperspectral + autonomous threat-classification lane. The research file §6.1 ARKA FACT has been updated with the scope correction; the capture brief §6.2 / §7.1 / §8 ARKA references will need a v0.4 pass with this same constraint.

**Already applied to:** `00_research-file.md` §6.1 ARKA FACT + §6.2 capability map cells (2026-05-14). **Still needs v0.4:** capture brief §6.2 table cell + §7.1 Play 2 description + §8 ARKA risk paragraph (these were written assuming the SIGINT bridge).

---

## Decision G — Internal CACI delivery PM call *(NEW — from v0.3 clean red-team #5)*

**The credibility issue:** The brief quotes HigherGov for the $467M ceiling and $58.9M obligation on Deloitte INDOPACOM Alpha — but CACI is **the sub on that contract**. There's a CACI delivery PM at Camp H.M. Smith with the actual numbers: real ceiling, remaining headroom, task-order dynamics, embed-staff utilization. Quoting external OSINT for a contract CACI is on signals the capture team isn't talking to the delivery team.

**Path forward (recommended G.1):** Add to the operator's first-30-days call list: contact the CACI INDOPACOM Alpha delivery PM (the embedded staff lead at Camp H.M. Smith). Capture: real ceiling, remaining headroom, task-order trajectory, J7-flavored task work pulled to date, relationship temperature with Deloitte program leadership.

**Update path:** v0.4 §6.1 Deloitte FACT replaces "industry-reported" framing with internal-PM-confirmed numbers; v0.4 §7.2 Sub plays adds an explicit "leverage delivery-PM relationship as the J7 listening post" angle.

---

## Decision E — Play 3 OPFOR framing *(quality, not blocking)*

v0.3 takes the honest path (independent OPFOR award, no OCI) but creates
multi-contract management overhead the customer may dislike. v0.2 had the
turnkey 2-vendor framing that Gemini called "self-licking."

The actual customer preference here is unknowable without asking. Three
patterns:

| Option | Trade-off |
|---|---|
| **E.1 Independent OPFOR (v0.3 current)** | Honest, no OCI; multi-contract management cost on the customer. |
| **E.2 Turnkey consortium with OCI mitigation plan** | Single throat to choke; requires a robust OCI mitigation document and probably customer-required organizational firewall. |
| **E.3 Bid as defensive C-UAS validator only, silent on OPFOR** | CACI bids what it has; customer figures out OPFOR independently. Simplest. |

Recommend **E.3** for the brief; let the customer surface OPFOR preference
during pre-RFP industry day.

---

## Re-red-team trigger

**Don't re-red-team v0.4 until Decisions A.1 + A.2 + B are answered.**
Reason: those three answers move 5 of the 12 v0.3 findings, and without
them the v0.4 red-team will surface the same speculations Gemini already
flagged. Wait for facts.

**When ready, re-run:**
```bash
_scripts/.venv/bin/python _scripts/red_team.py --opportunity PMTEC-USINDOPACOM
```

Tool auto-picks the latest `capture-brief-v*.docx`.

---

## Current state — what you're picking up

| | Value |
|---|---|
| Latest capture brief | `04_artifacts/capture-brief-v0.3-draft.docx` |
| Latest exec brief | `04_artifacts/executive-brief-v0.1-draft.docx` (not yet re-rolled to match v0.3 capture) |
| Ingested primary sources | 34 files in `01_sources/` |
| Verification status | 3 SUPPORTS, 18 PARTIAL, 0 DOES_NOT_SUPPORT, 0 UNVERIFIABLE (21 FACTs) |
| Red-team reports | `_red-team-2026-05-14-gemini-3.1-pro-preview-v0.{1,2,3}.md` |
| GitHub repo | `Anguijm/research-vault` (private), latest commit `4b84af8` |
| Vault on phone | GitHub Mobile → `Anguijm/research-vault` |

## Operator action checklist (in order)

**Phone calls (first 30 days):**
- [ ] **Call Brent Parker** (Decision A.1) — 4 questions on PMTEC procurement model
- [ ] **Call / email Stridiron's office** (Decision A.2) — confirms JHU unit
- [ ] **Call CACI INDOPACOM Alpha delivery PM** at Camp H.M. Smith (Decision G) — real ceiling + headroom + J7-task-work trajectory

**Decisions to make:**
- [ ] B path — financial framing (B.1 narrow scope recommended)
- [ ] C path — Spectral-Lite concept (C.1 synthetic-signatures recommended)
- [ ] D path — JFN strategy (D.2 space-to-JFN feed recommended)
- [ ] E path — Play 3 OPFOR framing (E.3 silent on OPFOR recommended)
- [ ] F path — ARKA SIGINT scope (F.1 strip recommended — already applied to research file; v0.4 brief still needs it)
- [ ] G path — internal-PM data integration (G.1 recommended — gated on the call landing)

**Brief work:**
- [ ] Roll v0.4 capture brief with the answers + decisions A-G applied
- [ ] Roll v0.4 exec brief to match
- [ ] Run `red_team.py --opportunity PMTEC-USINDOPACOM` — expect ≤ 3 findings if A + B + F + G done
- [ ] Update `index.md` `gate` field if v0.4 supports Gate 2 (Pursue) decision
- [ ] Re-build the share zip for the BD-team meeting

---

*Generated 2026-05-14 by Claude (Opus 4.7) following three iterations of
Gemini 3.1 Pro red-team on the PMTEC capture brief. The full red-team
findings for each version are preserved in the three sibling
`_red-team-*-v0.{1,2,3}.md` files.*

---
type: red_team_report
opportunity: PMTEC-USINDOPACOM
reviewed: capture-brief-v0.2-draft.docx
model: gemini-3.1-pro-preview
date: 2026-05-14
prompt_source: _meta/prompts/cross-ai-red-team.md
---

# Cross-AI Red Team — PMTEC-USINDOPACOM

*Reviewer: `gemini-3.1-pro-preview`  ·  Subject: `capture-brief-v0.2-draft.docx`  ·  Generated: 2026-05-14T06:24:14*

Run via `_scripts/red_team.py` using the prompt at `_meta/prompts/cross-ai-red-team.md`. Three passes per SOP §2.1 rule 5: Customer / Competitor / Skeptical Exec.

---

Here is the three-pass red-team review of the capture brief, conducted from the requested perspectives.

### Pass 1 — Customer reviewer (USINDOPACOM J7 Staffer)
*Perspective: I own these gaps. I want operational realism, not vendor buzzwords. I am highly sensitive to classification boundaries and self-serving vendor pitches.*

*   **§7.1 (Non-kinetic effects simulation):** You are proposing "Spectral-Lite" and "Trojan-Lite" by partnering with J6 to "define a training-enclave UNCLASSIFIED reduced-fidelity dataset." As a J7 staffer, I will push back hard on this. J6 does not magically approve unclassified EW/SIGINT datasets for coalition ranges just because a vendor asks. Furthermore, your plan to "pre-coordinate with PEO IWS for ship-borne Spectral platforms" assumes you can dictate fleet availability for Valiant Shield '28. That is our job, not yours. 
*   **§7.1 (C-UAS Blue-Cell Validation):** You are proposing a "2-vendor consortium" where you bring the defensive C-UAS and your buddy (Shield AI/DroneShield) brings the OPFOR swarm targets to test your system. This is a self-licking ice cream cone. We named "realistic training targets" as a gap (Gap 6) because we need objective, independent OPFOR replication, not a vendor grading their own homework against a hand-picked partner.
*   **§6.2 (AI & digital twin):** You explicitly state that ARKA brings concrete inputs and "not generic 'agentic AI'." However, your own corporate press release (Fact 21) literally markets ARKA as providing "Agentic AI-based software." If you are contradicting your own corporate messaging to sound edgy to me, I assume you don't actually understand the tech you just bought.
*   **§7.2 (Johns Hopkins University):** You are guessing that our JHU partnership is with APL ("specific JHU unit unverified — likely APL"). Do not build a strategy document for my command based on a guess. If you had actually attended the POST 2026 panel or done your homework, you would know which JHU unit Dr. Stridiron was talking about. 

### Pass 2 — Competitor analyst (Competing Prime - e.g., L3Harris or Lockheed)
*Perspective: How do I kill CACI's bid? Where are their vulnerabilities, and how can I exploit them to the customer?*

*   **§7.2 (Lockheed JFN sub):** CACI assumes they can "plug in cleanly" to the Joint Fires Network because it has an "open architecture." I would exploit this immediately. The facts (Facts 12 & 13) show that L3Harris already natively integrated their DiSCO EW architecture with JFN at Valiant Shield 24. CACI's "30-day urgency" to initiate teaming is already months too late. I would ghost CACI to the customer as being entirely on the outside of the JFN/CJADC2 integration loop.
*   **§8 & §7.1 (ARKA integration risk):** CACI admits the $2.6B ARKA acquisition just closed in March 2026 and integration isn't proven. Their mitigation is to pitch "commercially-available sensors" via DIU to bypass integration. I would hammer this to the J7 and SDA: "CACI is selling you a disjointed commercial data feed from a company they just bought, not a natively integrated military space architecture. We (Lockheed/Northrop) have legacy, integrated theater space presence."
*   **§6.1 & §8 (Incumbent inertia):** CACI is relying on their position as a *subcontractor* to Deloitte on the INDOPACOM Alpha task order to "socialize priority gaps internally" (§7.3). As a competitor, I know subs have very little power to steer prime task orders. I would highlight to the customer that CACI lacks a prime advisory vehicle for PMTEC, making them a risky choice for enterprise-level J7 work.
*   **§10.1 (TAM Play 1):** CACI estimates a $100M ceiling for "Spectral-Lite" by assuming multi-service expansion (Army DEVCOM, Navy NIWC, USAF 53rd). I would challenge this scale internally. PMTEC does not buy for DEVCOM or NIWC. CACI is artificially inflating their TAM to justify their B&P spend; their actual addressable PMTEC market for this is closer to their $10M floor.

### Pass 3 — Skeptical exec (Defense pure-play exec)
*Perspective: I have 4 minutes. I control the B&P budget. Is this actionable, or is this a half-baked draft?*

*   **§1, §2.3, §4.3, §5.2, §7.3 (AI Prompts):** You left your raw AI prompts in the brief. ("AI PROMPT — Draft this section LAST...", "AI PROMPT — Use Claude or Gemini..."). Come back when you've done your homework, proofread your document, and actually written the brief yourself. I am not approving a $3M B&P budget for a copy-paste AI draft.
*   **§9 vs. §10.3 (Decision Asks vs. Confidence):** In §9, you ask me to authorize capture teams for Play 1 (Non-kinetic sim) "immediately." But in §10, you explicitly state: "Confidence is LOW for play 1 (PMTEC procurement model unclear)." Why would I authorize immediate capture activation and spend millions in B&P when you don't even know how the customer is going to buy it? Figure out the procurement model first.
*   **§10.3 (ROI Calculation):** You claim an "ROI floor ~7x" based on $20M expected revenue against $3M in B&P costs. That is a 7x *revenue* multiple, not ROI. Once you factor in the actual cost of delivery, labor, and materials, the profit ROI on a $20M win with a $3M B&P sink is likely negative. Fix your math before pitching financial metrics to the C-suite.
*   **§7.2 (UARC Teaming):** You state "APL is a UARC... they will NOT sign capture-team MOUs" and advise against proposing one. This is basic GovCon 101. The fact that you felt the need to explicitly state this makes me question the baseline experience level of this capture team. 
*   **§9 (ARKA Play):** You want immediate authorization for the ARKA space play via DIU, explicitly stating "do NOT wait for Q3 2026 integration milestone." Given we *just* closed this $2.6B acquisition weeks ago (March 2026), pushing unintegrated tech to DIU risks our corporate reputation if ARKA and legacy CACI teams trip over each other. I need a sign-off from the ARKA transition lead before I approve this.

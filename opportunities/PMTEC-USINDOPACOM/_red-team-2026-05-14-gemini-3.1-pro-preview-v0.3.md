---
type: red_team_report
opportunity: PMTEC-USINDOPACOM
reviewed: capture-brief-v0.3-draft.docx
model: gemini-3.1-pro-preview
date: 2026-05-14
prompt_source: _meta/prompts/cross-ai-red-team.md
---

# Cross-AI Red Team — PMTEC-USINDOPACOM

*Reviewer: `gemini-3.1-pro-preview`  ·  Subject: `capture-brief-v0.3-draft.docx`  ·  Generated: 2026-05-14T09:53:59*

Run via `_scripts/red_team.py` using the prompt at `_meta/prompts/cross-ai-red-team.md`. Three passes per SOP §2.1 rule 5: Customer / Competitor / Skeptical Exec.

---

Here is the three-pass red-team review of the capture brief, conducted from the perspectives of a USINDOPACOM J7 customer, a competitor analyst, and a skeptical CACI executive.

***

### Pass 1 — Customer reviewer (USINDOPACOM J7 staffer)
*Focus: What is wrong, oversimplified, or sounds like marketing? What would you push back on?*

*   **§7.1 (Non-kinetic effects simulation):** You are fundamentally misunderstanding our bandwidth and authorities. You state that "J6 partnership and IC declassification scoping is a precondition to the play, not a deliverable." As a J7 staffer, I am trying to *buy* a solution, not take on a massive interagency declassification science project. If your "Spectral-Lite" requires INDOPACOM to fight the IC and NAVWAR for releasability to a coalition enclave before you can even build it, your solution is not viable for our timeline. 
*   **§4.1 & §2.1 (Funding environment):** You are throwing around the "$10.0B PDI request" to make this look like a mega-program. PMTEC is a federated enterprise funded across disparate service lines (Army JPMRC, Navy JFDD, Air Force ops). We do not have a single $10B checkbook. Stop quoting the macro PDI number; it shows you don't understand how our specific range integration dollars are actually appropriated.
*   **§7.1 (Space integration / ARKA):** Pitching "Agentic AI-based" software sounds like pure marketing buzzword bingo. I don't care about your recent M&A activity. PMTEC is about multi-domain *integration*. If you are pitching ARKA as a standalone commercial sensor feed because you haven't integrated it with your own CACI ground systems yet, you aren't solving my multi-domain problem; you're just selling me another siloed data feed.
*   **§7.2 (Johns Hopkins University partnership):** You assume the JHU partnership announced by Dr. Stridiron is with the Applied Physics Lab (APL) because it's the "obvious defense-research candidate." That is a massive leap. It could easily be the JHU Whiting School of Engineering or SAIS. Don't build a whole non-traditional UARC NDA strategy based on a guess.

***

### Pass 2 — Competitor analyst (L3Harris / Lockheed Martin)
*Focus: Where are the weakest parts of the recommendation? What facts could be challenged?*

*   **§7.2 & §5.2 (Lockheed JFN sub):** CACI's plan to sub to Lockheed on JFN by offering "complementary SIGINT-to-targeting plug-ins" is highly vulnerable. Fact 13 shows that we (L3Harris) already demonstrated our DiSCO EW architecture fully integrated at Valiant Shield 24. CACI admits we have the "inside track." If I see this, I will aggressively ghost CACI to Lockheed and J7 by highlighting that CACI's post-ARKA space data is unproven in the JFN architecture, whereas our EW payloads have two years of live Pacific exercise reps.
*   **§8 & §7.1 (ARKA integration risk):** CACI closed the $2.6B ARKA acquisition literally weeks ago (March 2026). They are directing their team to pitch DIU in 30 days using "pre-acquisition capabilities" to hide the lack of integration. I would exploit this immediately. I'd tell the customer: "CACI is selling you a PowerPoint of an unintegrated company. Their space sensors don't talk to their ground EW yet, and they are figuring out their org chart. Go with a prime that has native, legacy theater space presence."
*   **§7.1 (C-UAS Blue-Cell Validation):** CACI is explicitly refusing to bid the OPFOR swarm target role to avoid an OCI, recommending the government issue a "separate, independent OPFOR swarm-target award." I will exploit this by bidding a fully integrated, turnkey Red/Blue C-UAS validation package. I will frame CACI's approach as forcing the government to manage multiple contracts and play referee, whereas my company offers a single throat to choke.
*   **§6.1 (Existing Pacific footprint):** CACI is leaning hard on the Deloitte INDOPACOM Alpha task order for operational credibility. But they are just a sub, and USAspending shows the base and all options value is null (relying only on HigherGov for the $467M ceiling). I would remind the customer that providing staff-augmentation professional services under Deloitte does not equate to the engineering chops required to network live-virtual-constructive ranges.

***

### Pass 3 — Skeptical exec (Defense pure-play exec)
*Focus: Is the recommendation clear? Is the ask actionable? What would make you say "come back when you've done more homework"?*

*   **§10.3 (Aggregate TAM & B&P ROI):** You are asking for $1.5M–$3M in B&P over 12 months. You state the revenue-to-B&P multiple at the lower bound is ~5x. That is an atrocious return on investment. If we win $15M in revenue on $3M of B&P, and our gross margin is the typical 10-15% you cited, *we are losing money on this capture*. Redo your math or kill the bid. Come back when you have a path to a profitable ROI.
*   **§9 (Decision asks - Play 1):** You are asking me to authorize capture activation for Play 1, but you explicitly state it is "GATED on... a customer-procurement-model confirmation conversation with Brent Parker." Why is this in front of me for an executive decision *before* you've had the conversation? Go have the coffee with Parker, figure out if this is an OTA or an OASIS task order, size the TAM, and *then* ask for my approval.
*   **§7.2 (JHU Partnership):** "If the partnered unit is APL... If the partnered unit is one of JHU's other defense-relevant programs..." This is pure speculation (and violates your own Appendix E standards). Do not ask me to approve teaming outreach when you don't even know which part of the university the customer is working with. Make the phone call, get the fact, and come back.
*   **§9 & §8 (ARKA Authorization):** You want immediate authorization to pitch ARKA to DIU, but you include a precondition that the pitch must be reviewed by the ARKA transition lead so we don't "prematurely claim integration that is not yet real." This tells me you are rushing. You are risking our reputation with DIU by pitching a newly acquired $2.6B asset before the transition team even knows what the joint value proposition is. Stand down on the 30-day DIU pitch until the ARKA transition lead actually briefs *us* on what is ready for market.

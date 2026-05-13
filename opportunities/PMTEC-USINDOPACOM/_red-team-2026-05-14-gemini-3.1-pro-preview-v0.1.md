---
type: red_team_report
opportunity: PMTEC-USINDOPACOM
reviewed: capture-brief-v0.1-draft.docx
model: gemini-3.1-pro-preview
date: 2026-05-14
prompt_source: _meta/prompts/cross-ai-red-team.md
---

# Cross-AI Red Team — PMTEC-USINDOPACOM

*Reviewer: `gemini-3.1-pro-preview`  ·  Subject: `capture-brief-v0.1-draft.docx`  ·  Generated: 2026-05-14T04:59:50*

Run via `_scripts/red_team.py` using the prompt at `_meta/prompts/cross-ai-red-team.md`. Three passes per SOP §2.1 rule 5: Customer / Competitor / Skeptical Exec.

---

Here is the three-pass red-team review of the capture brief, conducted from the requested perspectives.

***

### Pass 1 — Customer Reviewer (USINDOPACOM J7 Staffer)
*Mindset: I need operational realism, not buzzwords. I know the actual budget and technical constraints of the theater.*

*   **§4.1 (Funding inaccuracy):** You cite the FY26 PDI request as $9.9B. The actual FY26 PDI budget book explicitly states $10.0B. Furthermore, you are conflating the macro PDI budget with PMTEC’s actual funding. The Army O&M line for JPMRC *and* PMTEC combined is $851M. Stop waving the $10B flag; it shows you don't understand our actual checkbook.
*   **§7.1 (C-UAS as adversary target):** This is technically nonsensical. PMTEC’s gap (§2.2) is for "realistic training targets." You are proposing to repackage SkyTracker, CORIAN, and X-MADIS—which are *Counter*-UAS (defensive/jamming) systems—as an "adversary UAS swarm stimulator." You cannot simply reverse a defensive jammer/detector and call it a flying target swarm. I would throw this white paper in the trash.
*   **§7.1 & §6.1 (Buzzword bingo):** You use the phrase "agentic AI" three times to describe the ARKA acquisition. How does "agentic AI" actually stimulate a training range or solve the SDA PWSA integration gap? This sounds like pure corporate marketing. We need to know how your satellite sensors feed into our Pacific Impact Zone data architecture, not what buzzwords your M&A team used.
*   **§7.2 (Johns Hopkins APL):** You propose a "teaming MOU" with JHU APL. APL is a University Affiliated Research Center (UARC). They act as a trusted agent and technical evaluator for the government. They do not sign traditional capture teaming MOUs with primes to bid on our work. This shows a fundamental misunderstanding of our acquisition ecosystem.
*   **§7.1 (Live Red-Team as a Service):** You propose using Spectral and Trojan to inject EW into exercises. These are operational, highly classified Navy and Army systems. Have you considered the deconfliction, classification, and frequency allocation nightmares of using operational tactical EW systems on a coalition training range? 

***

### Pass 2 — Competitor Analyst (Competing Prime - e.g., L3Harris or Lockheed)
*Mindset: Where are CACI's blind spots? How do we ghost them to the customer and lock them out of the team?*

*   **§6.1 & §8 (Incumbent weakness):** CACI is only a *sub* to Deloitte on the INDOPACOM Alpha vehicle. They do not own the primary J7 advisory relationship. We can exploit this by engaging J7 directly through our own prime vehicles, boxing CACI into a narrow IT/staff-augmentation corner.
*   **§7.1 (Space integration integration risk):** CACI is hanging their entire Space/SDA play on ARKA, an acquisition that *just closed* in March 2026. We will heavily ghost their integration risk. We can point out to the customer that CACI is trying to figure out its own internal org chart while we (Lockheed/Northrop) have legacy, proven space integration in the theater.
*   **§7.2 (LVC Content):** CACI admits they are weak on LVC and want to sub to HII. But LVC integration is PMTEC's #1 gap (§2.2). If they don't own the LVC backbone, they are just a niche payload provider. We can position our own EW/cyber effects as natively integrated into the LVC environment, making CACI's bolt-on approach look clunky.
*   **§7.3 (Teaming naivete):** CACI plans to "pre-position with HII and SOSi for teaming letters" in the next 30-90 days. Why would HII or SOSi team with CACI for EW/SIGINT when L3Harris already successfully demonstrated the DiSCO EW architecture at Valiant Shield 24 (Fact 13)? We (the competitors) already have the proven integration reps in the Pacific. We will lock up HII and SOSi before CACI even gets a meeting.

***

### Pass 3 — Skeptical Exec (Defense Pure-Play Exec)
*Mindset: I have 4 minutes. Show me the ROI, the vehicle, and the addressable market. Do not waste my B&P budget on fishing expeditions.*

*   **§1 & §9 (The Ask vs. The Vehicle):** You are asking me to "activate a capture team" for plays 1-3. For what RFP? Section 4.2 lists a bunch of DIU OTAs and a 2027 OSD modernization target, but there is no actual PMTEC procurement vehicle identified. You are asking for B&P money to capture a *concept*, not a contract. Come back when you have a draft RFP or a specific OTA drop.
*   **§7.1.3 (C-UAS repackaging cost):** You want to pivot our C-UAS systems into adversary targets. How much IRAD (Internal Research and Development) funding is required to re-engineer these systems? You ask for a white paper, but you haven't sized the engineering investment required to make this pivot reality. 
*   **§7.3 (Timeline sluggishness):** We just spent $2.6B acquiring ARKA to be a space powerhouse. Your timeline says we should wait 90-180 days to write an "ARKA-led space white paper." Meanwhile, §4.2 says DIU Hybrid Space Architecture demos are *underway right now*. Why are we waiting 3 to 6 months to pitch a $2.6B capability on an active demand signal?
*   **§9 (Decision asks):** "Allocate analyst time for monthly SAM.gov / DIU / DVIDS scan." This is basic BD pipeline hygiene, not an executive decision. If your team needs my permission to set up a SAM.gov alert, we have the wrong team on this account.
*   **§4.1 vs §6.2 (Addressable Market):** You list $9.9B in PDI funding, but you haven't sized the actual Total Addressable Market (TAM) for CACI. If we win the "non-kinetic effects simulation" piece, is that a $5M OTA or a $50M task order? I will not authorize a capture team until you tell me what the actual revenue ceiling is for these specific plays.

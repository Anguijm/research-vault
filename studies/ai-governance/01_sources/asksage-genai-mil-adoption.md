---
type: source-pack
study: ai-governance-landscape
stream: askSage authority basis vs the GenAI.mil mandate; BigBear.ai ownership; Navy/DoD adopters
captured: 2026-06-19
method: web-research subagents (WebSearch + WebFetch), raw findings preserved + labeled
classification: internal
relevance: directly informs §2 of the instruction (the dual-platform / authority-basis rationale)
---

# askSage vs GenAI.mil — authority basis, ownership, adopters

Two web-research streams answering the operator's questions: (1) how DoD/DoW activities run
askSage in light of the GenAI.mil mandate, and (2) the BigBear.ai/Ask Sage relationship plus
which Navy/DoD activities use askSage. Every claim ties to a real fetched URL; `.mil`/`.gov`
primaries that bot-blocked are flagged and sourced via reputable secondaries.

## Part 1 — Is the GenAI.mil mandate exclusive? (No — enterprise default, not a flat ban)

**Assessment.** GenAI.mil is the DoD/Navy **enterprise default / "preferred" / "mandated
enterprise" platform — not a prohibition on all other authorized tools.** Commands legitimately
run askSage as a **separately authorized capability** (its own ATO/RMF accreditation) procured
through an **acquisition vehicle**. GenAI.mil is meant to absorb *duplicative, general-purpose*
usage, not displace every separately-authorized, mission-specific tool.

Evidence (FACT, sourced):
- **DON CIO designation (Jan 28, 2026)** "mandates" GenAI.mil as the DON CUI/IL5 platform;
  "transition to GenAI.mil… no later than April 30, 2026." Primary `doncio.navy.mil` page
  BLOCKED (403); from search snippet + secondaries. https://www.doncio.navy.mil/ContentView.aspx?ID=20455
- **Marine Corps message (decisive on exclusivity):** "prioritization of GenAI.mil does not
  limit the use of other LLMs, such as the Army-managed CamoGPT." (DefenseScoop, Jan 22, 2026)
  https://defensescoop.com/2026/01/22/marine-corps-genai-mil-enterprise-ai-platform/
- **Air Force memo:** users move to GenAI.mil "or other approved systems"; "GenAI.mil may not
  meet every specific need… mission-specific solutions." (DefenseScoop, Dec 18, 2025)
  https://defensescoop.com/2025/12/18/air-force-sunsetting-niprgpt-generative-ai-platform/
- **Federal News Network (May 2026):** GenAI.mil is each service's "preferred enterprisewide AI
  platform" (preferred, not exclusive).
  https://federalnewsnetwork.com/navy/2026/05/navy-tracking-efficiency-gains-as-part-of-ai-training-efforts/
- **5 of 6 branches adopted GenAI.mil; legacy/other tools continue** (Army keeps frontier models;
  AF sunsetting NIPRGPT on contract end; Coast Guard building its own "Ask Hamilton").
  (DefenseScoop, Feb 2, 2026) https://defensescoop.com/2026/02/02/military-branches-genai-mil-enterprise-ai-adoption/
- **The basis for running askSage:** Ask Sage describes itself as the "first FedRAMP High, IL5,
  IL6 and Top Secret authorized solution," model-agnostic; "15,000+ government teams across 27
  agencies." (GlobeNewswire, June 20, 2025)
  https://www.globenewswire.com/news-release/2025/06/20/3102728/0/en/Ask-Sage-Partners-with-DoD-CDAO-and-U-S-Army-...html
- **The Army's worked example:** Army Enterprise LLM Workspace, "powered by Ask Sage IL5 SaaS,"
  "CUI accredited," hosted in **cArmy Cloud**, **token-based billing**, bought via an **Army IDIQ
  ($49M ceiling, 5-yr)**; plus a separate **$10M CDAO partnership** extending access to all
  COCOMs/Joint Staff/OSD. (army.mil + Breaking Defense, May–June 2025)
  https://www.army.mil/article/285537/ ; https://breakingdefense.com/2025/06/pentagon-ai-office-army-award-ask-sage-10m-for-genai-expansion/

**Unverified (flagged):** DON memo "report all current/planned GenAI capabilities to the GenAI
Task Force within 15 days" clause (search snippet only). Ask Sage's IL5/IL6/TS + FedRAMP-High
claims are corroborated by the vendor release + the fact CDAO/Army contracted it, but no
government ATO letter / FedRAMP Marketplace entry was retrieved. IL4-specific authorization not
stated in any fetched source.

## Part 2 — BigBear.ai owns Ask Sage now; founder has left

**FACT (well-sourced).** BigBear.ai (NYSE: BBAI) **acquired Ask Sage outright** — definitive
agreement announced **Nov 10–12, 2025**, **closed Dec 31, 2025, $250M all cash.** Founder
**Nicolas Chaillan** (ex-Air Force/Space Force Chief Software Officer) became BigBear.ai **CTO on
close but departed "for personal reasons" effective Feb 28, 2026.** askSage is now a
**wholly-owned BigBear.ai product, no longer led by its founder.**
- https://bigbear.ai/newsroom/bigbear-ai-announces-third-quarter-2025-results-and-definitive-agreement-to-acquire-ask-sage/
- https://bigbear.ai/newsroom/bigbear-ai-finalizes-250m-acquisition-of-ask-sage/
- https://ir.bigbear.ai/news-events/press-releases/detail/137/personnel-update (Chaillan departure, Feb 28, 2026)
- Corroboration: https://www.washingtontechnology.com/companies/2025/11/bigbear-pushes-agentic-ai-arena-250m-acquisition/409461/

## Part 3 — Adopters: Army yes; Navy none found

- **U.S. Army — CONFIRMED.** Army Enterprise LLM Workspace (powered by Ask Sage), launched May 15,
  2025; ~19,000 users "in less than 45 days" (Army CIO Garciga, Breaking Defense). Sources above.
- **CDAO + all COCOMs + Joint Staff + OSD — CONFIRMED collectively** (the $10M expansion); **no
  individual COCOM named.**
- **U.S. NAVY — NO Navy-command askSage adopter found in any fetched source.** Searched NAVSEA,
  NAVWAR, NAVAIR, NIWC, fleet commands, shipyards/RMCs. The Navy's enterprise bet is **GenAI.mil**
  (Gemini/xAI/OpenAI/Anthropic), a separate Pentagon platform — askSage appears in Navy coverage
  only as a *legacy* system, never as a Navy adoption.
- **Defense Health Agency — PROBABLE, not verified** (press-release headline exists; body 403-blocked).
- **Air Force/Space Force — no named adopter** (vendor "all-branches" marketing only).

## Assessment — what this means for the study / SRF-JRMC

1. **The dual-platform framing in §2 (v0.6) is well-supported.** GenAI.mil is the enterprise
   default, not an exclusive bar; running askSage alongside is legitimate when separately
   authorized. So the v0.6 reframe is on solid ground.
2. **The §2 [CONFIRM] authority-basis marker is now the load-bearing item.** The legitimate basis
   = askSage's own IL5 (FedRAMP-High) authorization + an acquisition vehicle (the Army IDIQ is the
   public model). SRF-JRMC should document *which* authorization/vehicle its askSage access rides
   on, especially because the **DON mandate is the strongest of the services** ("mandated platform
   for… all DON users") and **no Navy command is a public askSage adopter** — SRF-JRMC is early/
   unusual for the Navy, which raises the bar on documenting the authority.
3. **Vendor change is material.** askSage is now a BigBear.ai product and lost its founder-CTO
   (Feb 2026). Vendor continuity/risk is worth a line in the instruction's platform-governance
   posture and in the working-group authority confirmation.

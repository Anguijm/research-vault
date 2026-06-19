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
- **U.S. NAVY — the news sweep found no adopter, but USASpending DID (see Part 4 — this is a
  correction).** Open-source *news* searched (NAVSEA, NAVWAR, NAVAIR, NIWC, fleet commands,
  shipyards/RMCs) surfaced nothing, and the Navy's enterprise bet is **GenAI.mil** — but the
  authoritative federal award data shows **two Navy Ask Sage task orders** (NSWC Corona; Naval
  Research Laboratory). The news-only method missed them; the award data caught them.
- **Defense Health Agency — PROBABLE, not verified** (press-release headline exists; body 403-blocked).
- **Air Force/Space Force — no named adopter** (vendor "all-branches" marketing only).

## Part 4 — USASpending award data (AUTHORITATIVE; corrects Part 3)

Queried 2026-06-19 via the vault's `_scripts/lib/usaspending.py` API client (boring, citable,
not site-scraping), recipient = "Ask Sage" / "ASK SAGE, INC." (UEI **W9X4EWLUBAW1**), award
types contracts + IDVs, 2019→present. **Result: 46 contract actions + 1 IDV vehicle.** Total
DoD footprint is broad: heavy **Army** and **Air Force** task orders, **Defense Health Agency**,
**Missile Defense Agency**, and a $0 **Coast Guard (DHS)** action. Largest single: PIID
**W9128Z25FA003**, ~$10.9M, Army, Mar 2025.

**The acquisition vehicle (FACT):** the Army holds an Ask Sage **"Decentralized IDIQ"**, PIID
**W9128Z25DA001** (Department of the Army, effective 2025-02-03). The "decentralized" structure
lets any DoD activity place its own task order against it. This is the concrete mechanism behind
"how DoD activities run askSage."

**Two U.S. NAVY task orders (FACT — corrects the Part 3 news finding of "none"):**
- **NSWC Corona Division** — PIID **N6426725F0007**, **$475,000**, awarding office **NAVAL
  SURFACE WARFARE CENTER**, POP California. Description: *"ASK SAGE ARMY DECENTRALIZED IDIQ TASK
  ORDER CLIN 0013 FOR NSWC, CORONA DIVISION."* (Task order off the Army IDIQ W9128Z25DA001.)
  https://www.usaspending.gov/award/CONT_AWD_N6426725F0007_9700_W9128Z25DA001_9700/
- **Naval Research Laboratory (NRL)** — PIID **N0017326F0400**, **$24,750**, awarding office
  **NAVAL RESEARCH LABORATORY**, POP Maryland. Description: *"TOKENS FOR ORGANIZATION 6300 -
  MATERIAL SCIENCE AND TECHNOLOGY."* (Also a task order off the Army IDIQ W9128Z25DA001.)
  https://www.usaspending.gov/award/CONT_AWD_N0017326F0400_9700_W9128Z25DA001_9700/

**Assessment:** both Navy buys are **token purchases placed as task orders against the Army's
Ask Sage Decentralized IDIQ** — i.e., a Navy activity rides the Army's enterprise vehicle rather
than standing up its own contract. That is the most likely path for SRF-JRMC's askSage as well,
and it is exactly what the §2 `[CONFIRM]` authority-basis marker should capture.

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

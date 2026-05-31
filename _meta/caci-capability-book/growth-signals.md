---
schema_version: 1
session: 3
last_updated_utc: '2026-05-31'
source-anchor: caci-10k-fy25-2026-05-31
purpose: Growth-signal annotations sourced from the FY25 10-K MD&A — what
  CACI's executives spotlight as growth-relevant for investors, mapped where
  possible to capability areas in capability-areas.md.
notes-on-coverage: Quarterly earnings-call transcripts were not accessible
  via investor.caci.com (JavaScript-loaded). Session 3 uses the FY25 10-K
  MD&A as the consolidated annual-level signal. A future refresh pass could
  add quarterly granularity from 10-Q filings or paid transcript services.
---

# Growth signals — FY25 MD&A

This file captures what CACI's management explicitly identifies as growth-relevant in the most recent annual 10-K. It is the scoring layer's input for "what is CACI emphasizing in 2025?" — answering questions like "is a notice in the cyber domain higher-priority because cyber is a named focus area?" and "what does the budget environment imply for opportunity volume in the next 12 months?"

## §1 — Headline financial signals (FY25)

> **FACT.** Total revenues grew 12.6% to $8.6 billion in FY25 from $7.7 billion in FY24, with organic growth of 7.2% (balance from acquisitions). Net income grew 19.0% to $499.8 million. `[caci-10k-fy25-2026-05-31]`

> **FACT.** Total backlog as of 2025-06-30 was $31.4 billion (down 0.6% from prior year), with funded backlog of $4.2 billion. The total backlog represents approximately 3.6 years of revenue at FY25 run-rate. `[caci-10k-fy25-2026-05-31]`

> **FACT.** Contract-type mix: cost-plus-fee 60.5%, fixed-price 26.3%, time-and-materials 13.2%. `[caci-10k-fy25-2026-05-31]`

> **Assessment.** A 60%+ cost-plus mix is structurally important for the opportunity scoring layer — cost-plus contracts are predominantly long-term IDIQs and program-of-record support, not short-cycle competitive bids. CACI's revenue base is anchored in steady-state program performance, not transaction-driven wins. Operator's AF IDIQ task order (FA807518D0006) fits this pattern.

## §2 — Customer-segment growth (FY25)

> **FACT.** Customer-type revenue breakdown for FY25:
>
> - **Department of Defense (DoD): $6.508B = 75.4%** (up from 74.4% in FY24)
> - **Federal Civilian Agencies: $1.752B = 20.3%** (down from 20.7%)
> - **Commercial and other: $0.368B = 4.3%** (down from 4.9%)
>
> Federal civilian agencies named in the 10-K include "intelligence agencies and Departments of Justice, Agriculture, Health and Human Services, and State." `[caci-10k-fy25-2026-05-31]`

> **Assessment.** The DoD-share growth from 74.4% → 75.4% is a strategic signal — CACI is leaning further into defense as the company scales. The operator-team's Navy/Air Force Pacific focus is fully aligned with this direction. The 4.3% commercial share confirms that commercial pursuits are not where the operator should focus scoring weight.

## §3 — Named growth-domain priorities (executive language)

The 10-K MD&A names **eight market-trend themes** CACI believes will drive U.S. government spending in CACI's addressable market over the next several years. This is the most actionable list in the document for capability-area-to-trend mapping.

| # | Trend (verbatim from 10-K) | Capability area mapping |
|---|---|---|
| 1 | "A stable-to-higher U.S. government budget environment, particularly in national security-related areas (defense, intelligence, and border security)" | All seven areas |
| 2 | "Increased focus on cyber, space, and the electromagnetic spectrum as key domains for national security" | Cyber (§2), Space (§6), Spectrum Superiority (§7) |
| 3 | "Increased spend on network and application modernization and enhancements to cyber security posture" | Enterprise IT (§4), Digital Solutions (§3), Cyber (§2) |
| 4 | "Increased investments in advanced technologies (e.g., AI), particularly software-based technologies" | AI is cross-cutting (sub-capability of all 7 areas per Session 1) |
| 5 | "Increasing focus on near-peer competitors and other nation state threats" | C3I (§1), Mission and Engineering Support (§5), Cyber (§2), Spectrum Superiority (§7) |
| 6 | "Increasing focus on application of technologies to defend the homeland" | Enterprise IT (§4), Cyber (§2) — primarily relevant to non-Pacific homeland-defense customers |
| 7 | "Continued focus on counterterrorism, counterintelligence, and counter proliferation as key U.S. security concerns" | Mission and Engineering Support (§5), Cyber (§2), C3I (§1) |
| 8 | "Increased demand for innovation and speed of delivery" | Cross-cutting — affects how all areas are delivered |

`[caci-10k-fy25-2026-05-31]`

> **Assessment.** Trend #5 ("near-peer competitors and nation state threats") is the single most operator-team-relevant signal in this list. The Indo-Pacific theater is the primary U.S. near-peer-competition AOR (China, North Korea). CACI naming this as a growth focus reinforces that Pacific Navy/Air Force opportunity work aligns with CACI's stated strategic direction. The operator-team is in CACI's strategically prioritized geography.

> **Assessment.** Trend #6 ("defend the homeland") is the only listed trend that's largely NOT operator-team-relevant — homeland defense work is CONUS-focused (border, infrastructure, FEMA-adjacent) and doesn't align with the Pacific operational theater. Score notices that lean homeland-defense lower for this operator unless the customer is a Pacific command.

## §4 — Budget environment (FY25 → FY26)

> **FACT.** "On March 15, 2025, President Trump signed a CR that extended government funding through September 30, 2025, the remainder of GFY25 (a full-year CR). This is the first time that the Department of Defense (DoD) has been funded by a full-year CR." The CR included anomalies: new appropriations levels (not GFY24 levels); DoD allowed to start certain new programs; DoD given expanded transfer authority to reallocate funding. `[caci-10k-fy25-2026-05-31]`

> **FACT.** Defense spending in the full-year CR was raised to $893 billion, "just under the $895 billion President Biden requested for GFY25." `[caci-10k-fy25-2026-05-31]`

> **FACT.** "On May 2, 2025, President Trump submitted the GFY26 Presidential Budget Request (PBR) to Congress, which held defense spending at the GFY25 enacted level (a full-year CR) of $893 billion." `[caci-10k-fy25-2026-05-31]`

> **FACT.** "On July 4, 2025, President Trump signed the One Big Beautiful Bill Act (OBBBA), which provides additional funding above and beyond the PBR." OBBBA is a reconciliation bill separate from regular appropriations. OBBBA provides approximately **$156 billion in defense funding** (including **$25 billion for the Golden Dome initiative**) and approximately **$170 billion for border security and immigration**. `[caci-10k-fy25-2026-05-31]`

> **FACT.** "When combined with the President's GFY26 PBR, this represents growth of approximately 13% over GFY25 enacted levels for defense." Because OBBBA is direct funding via reconciliation, "these funds will be available in GFY26 and beyond whether normal appropriations or a CR is passed." `[caci-10k-fy25-2026-05-31]`

> **Assessment.** The ~13% defense funding growth in GFY26 is the strongest near-term tailwind for the opportunity pipeline. Combined with the operator's Air Force IDIQ vehicle, the FY26 task-order volume on FA807518D0006 should reasonably be expected to increase. The pipeline's volume estimates from Day-1 baseline data may understate FY26 surfacing volume.

> **Assessment.** The "Golden Dome initiative" ($25B in OBBBA) is a named program category worth tracking. The name suggests homeland missile defense (analogous to Israel's Iron Dome) — likely DoW funded, multi-service. Capability mapping: Space (§6) + C3I (§1) + Spectrum Superiority (§7). Not directly operator-team-relevant but a corporate-level CACI opportunity area worth monitoring as a Tier-2 relationship-lead signal.

## §5 — M&A pace and capability addition pattern

> **FACT.** Seven acquisitions in three fiscal years — three in FY25, three in FY24, one in FY23. FY25 acquisitions "expanded our software-defined offerings, specialized technologies, and customer presence." FY23 acquisition added "software engineering, data analysis, and cyber services to the national security sector" (UK-based). `[caci-10k-fy25-2026-05-31]`

> **FACT.** Net cash used in investing activities increased $1.6 billion in FY25 vs FY24, "primarily due to cash used in acquisitions." `[caci-10k-fy25-2026-05-31]`

> **Assessment.** M&A is structural to CACI's capability expansion pattern — 2-3 acquisitions per year. The operator-team should expect new capability areas to emerge between annual capability-book refreshes; the book needs an M&A-driven update cadence beyond annual. Session 4 (press releases) should attempt to identify the seven specific acquisitions by name to inform the capability-area attribution.

## §6 — Risks and dampeners

> **FACT.** "Many of our federal government contracts require us to employ personnel with security clearances, specific levels of education, and specific past work experience. Depending on the level of clearance, security clearances can be difficult and time-consuming to obtain and competition for skilled personnel in the industry is intense." `[caci-10k-fy25-2026-05-31]`

> **FACT.** "Changes in set-asides for small businesses and budgetary priorities, including efficiency initiatives like the Department of Government Efficiency, limiting, delaying, or reducing federal government spending in general" are identified risk factors. `[caci-10k-fy25-2026-05-31]`

> **FACT.** "Our customers' use of lowest price/technically acceptable (LPTA) procurements, which contributed to pricing pressures in past years, has moderated, though price still remains an important factor." `[caci-10k-fy25-2026-05-31]`

> **Assessment.** LPTA moderating is a positive signal for CACI's bid posture — best-value source selection is becoming more common, which favors CACI's "Expertise" differentiation framing over commodity pricing competition. For the operator, this means past-performance and capability narrative carry more weight in pursuits.

## §7 — Cross-references to capability areas

The growth signals above map back to `capability-areas.md` as follows:

- **Cyber (§2)** — explicitly named twice in the trend list (cyber security posture, cyber security threats). Highest growth-tailwind signal of all seven areas.
- **Space (§6)** — named once explicitly; Golden Dome adds an estimated $25B program-anchor opportunity.
- **Spectrum Superiority (§7)** — named once (electromagnetic spectrum). Aligns with near-peer competition trend.
- **C3I (§1)** — implied by near-peer competition + counterintelligence trends. Not explicitly named.
- **Mission and Engineering Support (§5)** — implied by counterterrorism + counterintelligence trends. Not explicitly named.
- **Enterprise IT (§4)** — implied by network/application modernization and homeland defense trends.
- **Digital Solutions (§3)** — implied by application modernization + AI in software trends.

> **Assessment.** Cyber, Space, and Spectrum Superiority are the three areas with explicit named-trend coverage. These have the strongest 12-month growth tailwinds. The operator-team's work in Mission and Engineering Support and Enterprise IT is positioned via implication rather than explicit naming — which suggests these areas are stable rather than fast-growing in CACI's portfolio.

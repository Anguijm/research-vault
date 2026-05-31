---
schema_version: 1
session: 2
last_updated_utc: '2026-05-31'
source-anchor: caci-10k-fy25-2026-05-31
purpose: CACI corporate-structure and business-overview facts from the FY25
  10-K Business section. Content here is corporate context that doesn't
  attach to a single capability area; capability-area-specific 10-K excerpts
  are in capability-areas.md §1-§7.
---

# CACI corporate business overview — FY25 (fiscal year ended 2025-06-30)

This file collects corporate-level facts from CACI's most recent 10-K that inform the scoring layer without belonging to a single capability area. Every claim cites the 10-K Business section unless otherwise noted.

## §1 — The "Expertise + Technology" framing

> **FACT.** The 10-K uses "Expertise" and "Technology" as a two-part top-level frame that cuts across the seven market areas. `[caci-10k-fy25-2026-05-31]`

CACI describes Expertise as "talent with the specific technical and functional knowledge to support agency operations. Examples include individuals with talents such as software development, data and business analysis, operations support, **naval architecture**, engineering, life cycle support, intelligence and special operations support, and network exploitation analysis." `[caci-10k-fy25-2026-05-31]`

CACI describes Technology as agile software development using open modern architectures and DevSecOps; advanced data platforms and applications augmented by AI; Enterprise Resource Planning (ERP) systems; Electromagnetic Spectrum (EMS) capabilities; photonics; and network modernization. `[caci-10k-fy25-2026-05-31]`

> **Assessment.** The 10-K's explicit naming of **naval architecture** as a CACI Expertise area is materially relevant to the operator's team work. SRF-JRMC availability planning and the team's Waterfront Operations sub-team (SRA/DSRA/SIA advance planning, IPTD, dry-dock coordination) sit squarely in the naval-architecture skill domain. This is direct corroboration that the operator-team's work-types are within CACI corporate's stated Expertise areas — not a stretch extension.

## §2 — Corporate structure and scale

> **FACT.** CACI International Inc is a Delaware holding company founded in 1962 as a simulation technology company. Operations are conducted through subsidiaries primarily located in the United States and Europe. Employee count as of 2025-06-30 was approximately 25,000 full and part-time. `[caci-10k-fy25-2026-05-31]`

> **FACT.** The Company reports in two segments: Domestic Operations (97.0% of FY25 revenues) and International Operations (3.0%). International Operations are conducted through CACI Limited and CACI BV, headquartered in London, serving the UK, continental Europe, and other international markets. `[caci-10k-fy25-2026-05-31]`

> **FACT.** Top ten revenue-producing contracts in FY25 accounted for 46.4% of revenues, equal to $4.0 billion. `[caci-10k-fy25-2026-05-31]`

> **Assessment.** The $4.0B / 46.4% ratio implies total FY25 revenue of approximately $8.6 billion. This is the corporate scale CACI operates at — material context when assessing whether a $X-million SAM.gov opportunity is bid-relevant. A $5M SS notice represents <0.1% of revenue, which informs why CACI prioritizes the $10M+ tier (the `prime_scale_min_usd: 50000000` threshold in `caci-discovery-config.yaml` is consistent with this scale).

## §3 — Customer base

> **FACT.** "Our customers are primarily agencies and departments of the U.S. government as well as foreign governments and commercial enterprises." `[caci-10k-fy25-2026-05-31]`

> **FACT.** The Enterprise IT market area serves "approximately 50 federal agencies." `[caci-10k-fy25-2026-05-31]`

The 10-K Business section does NOT enumerate specific named federal customers in the Markets discussion. (Customer-org share data lives elsewhere — the `baseline_caci_footprint` in `_meta/caci-discovery-config.yaml` is derived from USAspending awards and provides the percentage shares.)

## §4 — Contract instruments

> **FACT.** CACI's contracts and subcontracts include fixed-price, cost reimbursement, time-and-materials, indefinite delivery / indefinite quantity (IDIQ), and government-wide acquisition contracts (GWACs) such as General Services Administration (GSA) schedule contracts. By company policy, "significant" fixed-price contracts require approval of at least two executives. `[caci-10k-fy25-2026-05-31]`

> **FACT.** "Essentially all contracts with the U.S. government, and many contracts with other government entities, permit the government customer to terminate the contract at any time for the convenience of the government or for default by the contractor." `[caci-10k-fy25-2026-05-31]`

## §5 — Recent acquisitions (last 3 fiscal years)

> **FACT.** "During the past three fiscal years, we completed a total of seven acquisitions." `[caci-10k-fy25-2026-05-31]`

> **FACT.** FY25 — three acquisitions "that expanded our software-defined offerings, specialized technologies, and customer presence." `[caci-10k-fy25-2026-05-31]`

> **FACT.** FY24 — three acquisitions "that enhance our capabilities and customer relationships." `[caci-10k-fy25-2026-05-31]`

> **FACT.** FY23 — one UK acquisition of "a business that provides software engineering, data analysis, and cyber services to the national security sector." `[caci-10k-fy25-2026-05-31]`

The 10-K Business section does NOT name the acquired entities. The Spectrum Superiority capability page on caci.com references "Azure Summit acquisition" as the origin of some SIGINT/EW/ISR technology `[caci-spectrum-superiority-2026-05-31]` but the 10-K Business section itself does not confirm the name. Session 4 (press releases) should attempt to enumerate the 7 acquisitions by name and align them to capability areas.

## §6 — Strategy and growth posture

> **FACT.** "We have a relatively small share of the addressable market for our Expertise and Technology and intend to achieve growth and increase market share both organically and through strategic acquisitions." `[caci-10k-fy25-2026-05-31]`

> **FACT.** CACI faces "indirect competition from certain government agencies that perform services for themselves similar to those marketed by us." `[caci-10k-fy25-2026-05-31]`

> **FACT.** "Non-traditional players have entered the market and have established positions related to such areas as cloud computing, cyber, satellite operations, and business systems." `[caci-10k-fy25-2026-05-31]`

## §7 — Center for Research, Application, Development, Learning, and Engagement (CRADLE)

> **FACT.** CRADLE is CACI's "state-of-the-art collaboration facility that provides customers with an enhanced engagement experience, built to foster innovation, creative designs, and unique solutions. The CRADLE brings together customers, industry partners, academia, and CACI personnel to explore and discover new ways to solve complex problems and challenges." `[caci-10k-fy25-2026-05-31]`

> **Assessment.** CRADLE is a named CACI corporate asset. If an operator-team Pacific opportunity has a customer-engagement / problem-solving framing where a CRADLE-style engagement could be offered, that's a differentiator. Currently the CRADLE facility's location is not specified in the 10-K Business section; verify in Session 4 press releases.

## §8 — Fiscal-year and budget cycle relevance

> **FACT.** "The U.S. government's fiscal year ends on September 30 of each year. It is not uncommon for government agencies to award extra tasks or complete other contract actions in the weeks before the end of a fiscal year in order to avoid the loss of unexpended funds." `[caci-10k-fy25-2026-05-31]`

> **Assessment.** This corroborates Gemini's red-team Round 2 observation about September-15-to-30 posting overflow — the FY-end dynamic is real and CACI itself acknowledges it as a contract-action concentration window. The pipeline's `daily_delta` slice should be expected to spike in volume during that window every September.

## Cross-links

- The seven capability area summaries from this 10-K are quoted in `capability-areas.md` §1-§7, alongside the caci.com marketing language for the same areas. The two sources reinforce the taxonomy.
- The FY25 acquisitions point to Session 4 follow-up via press releases (7 named acquisitions to identify).
- The 25,000-employee, $8.6B-revenue scale point informs the `prime_scale_min_usd` threshold in `caci-discovery-config.yaml`.

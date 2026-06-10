---
schema_version: 1
session: 4
last_updated_utc: '2026-05-31'
source-anchor: caci-contracts-page-2026-05-31
purpose: Canonical inventory of the IDIQs, GWACs, and GSA Schedules CACI
  holds as prime, with explicit attention to the operator-team's vehicle
  (DTIC IAC MAC, FA807518D0006) and its recompete cliff.
---

# CACI contract vehicles

CACI publishes its complete prime-contract-vehicle inventory at `caci.com/contracts`. This file mirrors that inventory with explicit annotation of which holder entity carries each vehicle and which capability areas the vehicle services. The most operationally important entry — the operator-team's contract — is §1.

## §1 — Operator-team's contract: DTIC IAC MAC

> **FACT.** The operator-team is performing under task order(s) against the **DTIC IAC MAC** (Defense Technical Information Center Information Analysis Center Multiple Award Contract). Contract number **FA807518D0006**, held by **CACI, Inc. - Federal**. Period of performance **2018-09-30 to 2027-09-29**. `[caci-contracts-page-2026-05-31]`

> **Assessment.** Two material facts here:
>
> 1. **The vehicle is an Air Force-managed IDIQ that sponsors task orders from across DoD.** The "FA" prefix indicates an Air Force contracting office (consistent with the operator's earlier statement that the contract is "Air Force-owned"). DTIC IAC MAC is the multi-award IDIQ that supports DTIC's Information Analysis Center program — meaning the vehicle is designed to task-order to any DoD organization needing IAC-aligned technical analysis. The operator-team's specific task order is one of potentially many active task orders against this IDIQ; CACI is one of multiple primes on the MAC.
> 2. **The IDIQ recompetes in ~16 months from today (2026-05-31).** PoP ends 2027-09-29. Continuity for the operator-team beyond that date depends on CACI's position on the follow-on competition OR migration to a different vehicle before expiration. The recompete will likely be announced 6-18 months before the PoP end — i.e., between approximately late 2025 (already passed) and early 2027. This is the single most important strategic-timing fact for the operator-team's contract continuity.

> **Assessment.** "DTIC IAC MAC" is the IDIQ family name. The DTIC Information Analysis Center program organizes its task orders by technical focus area (each IAC has a thematic focus — cybersecurity, defense systems, homeland defense, etc.). The operator-team's specific task order falls under one of those technical IACs; identifying which IAC and which sponsoring agency for the team's task order is a research gap — this requires either internal contract documentation OR the USAspending IDV-family pull Gemini recommended (still pending in the slice plan work).

## §1.1 — Task-order family under DTIC IAC MAC (what the operator-team's vehicle actually carries)

On 2026-06-07 a child-award pull on the IDV `CONT_IDV_FA807518D0006_9700` returned the **full set of 12 task orders** CACI holds under DTIC IAC MAC, with obligated amounts. This closes the Session-1–4 gap "what other task orders exist under FA807518D0006" — the book previously had only one data point (the digital-engineering TO).

| TO PIID | Obligated | Period | Scope (USAspending description) |
|---|---|---|---|
| FA807522F0030 | $468.3M | 2022-05 → 2027-05 | Digital Engineering and Digital Transformation Research, Analysis, and Development |
| FA807524F0060 | $244.8M | 2024-09 → 2029-09 | **Advanced Product Innovation and Delivery for NavalX** |
| FA807522F0054 | $125.6M | 2022-08 → 2027-08 | **Design, Maintenance, Quality, Extension Engineering, and Shipyard Quality Assurance** (MSC N7) — **THIS IS THE OPERATOR-TEAM'S TASK ORDER** |
| FA807521F0077 | $78.1M | 2021-09 → 2026-09 | Counter-Unmanned Aircraft Systems R&D and Sustainment |
| FA807520F0037 | $68.7M | 2020-05 → 2025-05 | Research/analysis of technical, logistics, business operations, contingency ops |
| FA807524F0042 | $68.0M | 2024-08 → 2029-08 | **Naval Undersea Warfare Center (NUWC) engineering and modernization operations analysis** |
| FA807522F0033 | $42.9M | 2022-07 → 2027-07 | Assured PNT and Space Cross-Functional Team research/analysis |
| FA807521F0027 | $32.8M | 2021-02 → 2026-02 | Research/engineering for intel technology & architecture (CCDC) |
| FA807524F0015 | $16.4M | 2024-03 → 2027-03 | **Enterprise Application Innovation for Commander, Navy Reserve Forces Command N6** |
| FA807525F0033 | $7.4M | 2025-03 → 2030-03 | Research/analysis of technical, logistics, business activities, contingency ops |
| FA807525F0014 | $2.8M | 2025-02 → 2030-02 | Electromagnetic sensors / communications security systems analysis |
| FA807518F0006 | $3,600 | 2018-09 → 2018-10 | IAC MAC base administrative line |

`[caci-usaspending-refresh-2026-06-07]`

> **FACT (operator-confirmed 2026-06-07).** The operator-team's own task order is **FA807522F0054** (MSC N7 Engineering Directorate). One TO, multiple non-overlapping contingents: the operator's team performs **USS** repair support at **SRF-JRMC, Japan**, while a separate worldwide contingent on the same TO performs **USNS** shipyard-QA / maintenance-engineering at MSC ship availabilities. The operator has met some of the USNS contingent (San Diego); the two do not operationally overlap.

> **FACT.** Four of the twelve DTIC IAC MAC task orders are explicitly Navy/maritime: NavalX advanced product innovation ($244.8M), the MSC machinery/structural-maintenance + shipyard-QA engineering TO ($125.6M), NUWC engineering and modernization ($68.0M), and Navy Reserve Forces Command N6 enterprise applications ($16.4M). `[caci-usaspending-refresh-2026-06-07]`

> **Assessment.** This is the strongest empirical corroboration yet of the operator's standing intuition that the team's vehicle has "much more reach than we're using." The team performs at SRF-JRMC Yokosuka, but the *same IDIQ* already carries ~$455M of Navy engineering work (NavalX product innovation, NUWC modernization, MSC shipyard QA, Navy Reserve apps) plus C-UAS, PNT/Space, and intel-architecture lines. DTIC IAC MAC is functionally a broad Navy-and-defense technical-services routing path, not a narrow analysis vehicle — exactly the cross-area flexibility the §4 mapping implies.

> **Assessment (cross-link to the Hanwha Ocean track).** TO **FA807522F0054** — "Design, Maintenance, Quality, Extension Engineering, and Shipyard Quality Assurance" for Military Sealift Command, with "worldwide deployments to shipyards during MSC ship availabilities" — is **on this vehicle**. The `HANWHAOCEAN-DOD` opportunity's pull-through thesis (as MSC pushes ship availabilities into Korean yards, demand grows for the government-side maintenance-engineering/QA work CACI already does for MSC) therefore runs *through the operator-team's own IDIQ*, not a separate corporate vehicle. See `opportunities/HANWHAOCEAN-DOD/00_research-file.md` §6.

## §2 — Other CACI IDIQs (vehicles the operator-team does NOT directly perform under)

The following are CACI's other prime IDIQ vehicles. The operator-team cannot task-order against these directly, but knowing the inventory matters because:
- A SAM.gov notice referencing one of these vehicles signals "CACI has a path to bid this work" even if not via the operator-team's vehicle.
- The relationship-lead pattern (Tier-2 surfacing) applies — the operator can introduce CACI corporate to the right vehicle holder.

| Vehicle | Holder entity | Contract number | Period of performance | Customer scope |
|---|---|---|---|---|
| **CIO-SP3** | CACI Enterprise Solutions, LLC | HHSN316201200009W | 2012-06-01 to 2026-10-29 | NIH-managed government-wide IT |
| **CIO-SP3** | CACI NSS, LLC | HHSN316201200032W | 2012-06-01 to 2026-10-29 | NIH-managed government-wide IT |
| **Encore III** | CACI, Inc. - Federal | HC1028-18-D-0007 | 2017-11-02 to 2027-03-11 | DISA / DoD IT |
| **ITES-3S** | CACI-ISS, LLC | W52P1J-18-D-A138 | 2018-09-25 to 2027-09-24 | U.S. Army Information Technology Enterprise Solutions — Services |
| **Mega 5** | CACI, LLC-Commercial | 15JPSS20D00000368 | 2020-12-01 to 2027-05-31 | (DOJ Mega series — commercial/civilian) |
| **RS3** | CACI Technologies, LLC | W15P7T-19-D-0157 | 2022-05-14 to 2027-05-14 | U.S. Army Responsive Strategic Sourcing for Services |
| **SeaPort NxG** | CACI, Inc. - Federal | N0017819D7295 | 2019-01-02 to 2029-01-01 | **U.S. Navy professional services** |

`[caci-contracts-page-2026-05-31]`

> **Assessment.** **SeaPort NxG (N0017819D7295) is the highest-relevance vehicle for the operator's region**. SeaPort NxG is the U.S. Navy's professional-services IDIQ — the same Navy-customer space as SRF-JRMC. If the operator surfaces a Navy opportunity that the team's DTIC IAC MAC task order doesn't cover, SeaPort NxG is the natural alternate routing path. The CACI prime holder is CACI, Inc. - Federal (same entity as DTIC IAC MAC), which means the holder coordination is between two contracts within the same CACI legal entity. SeaPort NxG runs through 2029-01-01 — significantly longer runway than DTIC IAC MAC.

> **Assessment.** **CIO-SP3 (both NSS and Enterprise Solutions) recompetes in late October 2026.** Two CACI subsidiary entities hold separate prime positions on this IT-services GWAC. Recompete is imminent; expect a wave of CIO-SP3 follow-on activity in the next 18 months that could affect CACI's broader IT positioning.

## §3 — GSA Schedule vehicles

| Schedule | Contract number | Period of performance | Service category |
|---|---|---|---|
| **Alliant 2** | 47QTCK18D0009 | 2018-07-01 to 2028-06-30 | IT solutions |
| **Alliant 3** | 47QTCB26D0006 | 2026-03-10 to 2031-03-09 | IT solutions (next-gen) |
| **ASTRO** | 47QFCA22D0009 (multiple pools) | 2021-11-15 to 2026-11-14 | Unmanned and AI-enabled solutions |
| **OASIS+** | 47QRCA25DU060 | 2024-12-17 to 2029-12-16 | Professional services |
| **IT Schedule 70** | GS-35F-349CA | 2015-06-02 to 2030-06-01 | IT products and services |
| **Schedule 00Corp** | GS-00F-268CA | 2015-08-18 to 2030-08-17 | Multiple Award Schedule (consolidated) |

`[caci-contracts-page-2026-05-31]`

> **Assessment.** **ASTRO** (47QFCA22D0009) is GSA's vehicle for unmanned and AI-enabled solutions, with a PoP ending 2026-11-14 — also recompeting imminently. Relevant for capability areas Cyber (§2), Spectrum Superiority (§7), and Space (§6) which CACI markets with AI sub-capabilities throughout. **OASIS+** (47QRCA25DU060) covers professional services through 2029 — a longer-runway vehicle for non-IT work.

## §4 — Vehicle-to-capability-area mapping

For the scoring layer, an opportunity matching a capability area can be cross-referenced to a candidate CACI vehicle that could deliver it:

| Capability area | Primary CACI vehicles |
|---|---|
| C3I (§1) | DTIC IAC MAC; ITES-3S; SeaPort NxG; Alliant 2/3 |
| Cyber (§2) | DTIC IAC MAC; ASTRO; ITES-3S; CIO-SP3 |
| Digital Solutions (§3) | OASIS+; CIO-SP3; ITES-3S; Alliant 2/3 |
| Enterprise IT (§4) | CIO-SP3; Alliant 2/3; IT Schedule 70; Encore III; ITES-3S |
| Mission and Engineering Support (§5) | DTIC IAC MAC; SeaPort NxG; RS3; OASIS+ |
| Space (§6) | DTIC IAC MAC; OASIS+; ASTRO |
| Spectrum Superiority (§7) | DTIC IAC MAC; ASTRO |

> **Assessment.** **DTIC IAC MAC (the operator-team's vehicle) is the highest-utility cross-area IDIQ** — it appears in the candidate path for five of seven capability areas, more than any other vehicle. This is structurally important: the operator-team's contract is not narrowly scoped to one capability area but can serve as a routing path for multiple kinds of work. This corroborates the operator's earlier intuition that "there's a lot more flexibility maybe than what we're allowing ourselves here." The flexibility is real and structural.

## §5 — USAspending-observed vehicles (the broader "where CACI gets paid" lens)

`caci.com/contracts` lists CACI's marketed prime IDIQ and GSA positions. A complementary lens — every vehicle under which CACI has actually received award dollars — comes from the USAspending pass that populated `_meta/caci-discovery-config.yaml`'s `baseline_caci_footprint.vehicles` section. Sixteen distinct vehicles by contract number appear in CACI's top award shares; **only two of those 16 are also on the caci.com/contracts marketed list** (HHSN316201200009W = CIO-SP3 CACI Enterprise Solutions; GS-35F-349CA = IT Schedule 70).

All 16 were resolved on 2026-06-07 via per-PIID IDV lookups against USAspending (office name from the award-detail endpoint; IDIQ scope from the IDV description). They are **CACI prime IDV/BPA positions**, not subcontracts — most are real IDIQs or agency BPAs that CACI simply does not foreground on its marketed `caci.com/contracts` list.

| Contract number | USAspending share | Identity (resolved 2026-06-07) — contracting office / IDIQ scope |
|---|---|---|
| HHSN316201200009W | 9.0% | **NITAAC CIO-SP3** (NIH NITAAC) — confirmed; CACI Enterprise Solutions |
| SP470917D0009 | 7.0% | **DLA Contracting Services Office (DCSO) Philadelphia** — DLA IT services IDIQ (parent of the DAI app-dev TO; "JETS / IT audit" scope) |
| FA822417D0004 | 7.0% | **Air Force Sustainment Center (FA8224, AFSC OL-H PZIM)** — engineering services for integration/update/consolidation |
| SP470121D8002 | 6.5% | **DCSO Philadelphia (DLA)** — PIEE (Procurement Integrated Enterprise Environment) COE support services |
| 70RTAC20A00000003 | 6.0% | **DHS Info Tech Acquisition Center** — BPA supporting DHS HQ OCIO (Federal Civilian, not CBP as previously guessed) |
| GS00Q14OADU121 | 5.5% | **GSA OASIS Pool 1** — confirmed |
| GS00Q09BGD0037 | 5.5% | **GSA Alliant 1 GWAC** — confirmed (the book's prior guess was correct; predecessor to Alliant 2) |
| SP470116D2001 | 5.0% | **DCSO Philadelphia (DLA)** — WAWF/EDA sustainment and development support |
| W91QUZ12D0010 | 3.5% | **DCSO-Richmond (Army)** — programmatic support |
| FA872622A0001 | 3.0% | **AFLCMC (FA8726, HNK C3IN)** — EITAAS Wave 1 BPA (Air Force Enterprise IT-as-a-Service) on GSA MAS IT Schedules |
| H9222211D0008 | 2.5% | **USSOCOM (admin DCMA Mid-Atlantic)** — SITEC distributed computing services |
| GS35F349CA | 2.0% | **GSA IT Schedule 70 (FSS)** — confirmed |
| HC102808D2021 | 2.0% | **DISA Encore II** IT support MAC (predecessor to Encore III in §2) |
| HSHQDC14A00010 | 2.0% | **DHS Info Tech Acquisition Center** — Desktop Support Services (DSS) |
| FA873015D0002 | 2.0% | **AFLCMC Kessel Run (FA8730, HBBK)** — FPS3 Force Protection Site Security Systems / Integrated Base Defense |
| IND14PC00002 | 2.0% | **DOI Interior Business Center (IBC)** — Business Integration Office assistance |

`[caci-usaspending-refresh-2026-06-07]`

> **Assessment.** Three corrections to the prior (prefix-guessed) picture: (1) the **SP47-family is DLA Contracting Services Office Philadelphia, not "DLA Land and Maritime"** — it is CACI's DLA *IT/enterprise-software* franchise (DAI, PIEE, WAWF/EDA), which is where DLA's 24.5% customer-org share actually lives; (2) **70RTAC is DHS HQ OCIO, not CBP**; (3) **GS00Q09BGD0037 is confirmed Alliant 1**, and **HC102808D2021 is confirmed DISA Encore II** (the predecessor to the Encore III in §2). Net: the "16 observed vehicles" are CACI prime positions spread across DLA (DCSO Philadelphia), three Air Force AFLCMC/AFSC offices (FA8224, FA8726, FA8730), DISA, DHS, USSOCOM, GSA, and DOI — a broad multi-agency IDIQ footprint, none of it Pacific-specific.

> **Assessment.** For the scoring layer, the resolved identities matter because several map to capability areas already in the taxonomy: EITAAS and the DHS desktop/OCIO work are **Enterprise IT (§4)**; SITEC and the AFSC engineering IDIQ touch **C3I (§1)** / **Mission and Engineering Support (§5)**; FPS3 (integrated base defense) is a physical-security/**C3I** adjacency. The DLA IT franchise (DAI/PIEE/WAWF) is **Digital Solutions (§3)**. This is the gap that was deferred to "the USAspending top-50 pull" — now closed.

## §6 — Operator-team layer vehicles (CACI NSS-held)

The operator-team-layer's `team_vehicles_held_by_caci_nss` field in `_meta/caci-discovery-config.yaml` enumerates vehicles held by the **CACI NSS, LLC** subsidiary — distinct from the DTIC IAC MAC vehicle which is held by **CACI, Inc. - Federal** (a different CACI subsidiary):

- **GSA OASIS Pool 1** — parent IDC GS00Q14OADU121
- **NITAAC CIO-SP3** — parent IDC HHSN316201200032W (the CACI NSS variant of CIO-SP3; distinct from the 009W variant held by CACI Enterprise Solutions)
- **GSA Multiple Award Schedule** — GS-35F-349CA (= IT Schedule 70)

> **Assessment.** The CACI NSS-held vehicles are organizationally adjacent to the operator-team but not the team's direct vehicle. They become relevant if the team's reach extends to work that natively fits NITAAC CIO-SP3 (NIH-managed IT IDIQ — broader federal IT scope than DTIC IAC MAC) or OASIS+ (professional services). Cross-subsidiary coordination within CACI (CACI, Inc. - Federal ↔ CACI NSS, LLC) is a known corporate pattern. The relationship-lead classification (Tier-2 surfacing) applies here — if an opportunity fits a CACI NSS-held vehicle better than DTIC IAC MAC, the operator's role is to surface the opportunity to the right CACI subsidiary, not to bid it directly through their team.

## §7 — Research gaps

- **Identify the specific IAC** the operator-team's task order falls under (CSIAC = Cyber Security; DSIAC = Defense Systems; HDIAC = Homeland Defense; or other DTIC IAC). This affects which technical-focus-area opportunities to prioritize.
- **Identify the sponsoring agency** for the operator-team's specific task order (the task order's customer, distinct from the IDIQ's administering Air Force contracting office).
- **Identify the 14 USAspending-observed vehicles** by IDIQ name and scope (§5 table). Highest leverage: SP470917D0009, FA822417D0004, SP470121D8002 (combined ~20% of CACI's USAspending share).
- **Verify CIO-SP3 recompete timeline** — both CACI subsidiaries hold prime positions; follow-on competition timing affects FY26-FY27 portfolio shape.
- **Verify ASTRO recompete timeline** — PoP ends 2026-11-14; follow-on competition expected in CY2026.

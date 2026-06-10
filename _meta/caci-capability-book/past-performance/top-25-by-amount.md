---
schema_version: 1
session: 5
last_updated_utc: '2026-05-31'
source-anchor: caci-usaspending-top25-2026-05-31
purpose: Past-performance citations populated from USAspending top-25 CACI
  awards by amount over the last 7 fiscal years (window 2019-06 to
  2026-05). Closes the past-performance gap identified in the Session 1-4
  audit. Cross-references each award to a capability area in
  capability-areas.md where the program description supports attribution.
refresh: '2026-06-07 — re-pulled with the now-live programmatic USAspending
  access. Dollar amounts now populate correctly (the 2026-05-31 pass returned
  null amounts, so its "by amount" ranking was unreliable and is superseded).
  Extended from top-25 to the top-50 window; two Acacia Center for Justice rows
  (substring false-positives on "aCACIa") were excluded, leaving 48 genuine CACI
  awards. See source-ledger caci-usaspending-refresh-2026-06-07.'
---

# Top CACI awards by amount (USAspending, last 7 fiscal years)

> **Refreshed 2026-06-07.** Originally a top-25 ordinal snapshot with null dollar amounts; re-pulled with the live USAspending client to add **real obligated amounts** and extend to the top-50 window (48 genuine CACI awards after excluding two Acacia Center for Justice false-positives). The §2 table below is the current data; the §1 attribution summary and §3 observations below were written against the original top-25 and remain broadly valid (the programs are unchanged) except where §2/§4 note a correction. Filename kept as-is for lineage.

This file is the seventh capability-book artifact and the first to fill the past-performance directory. Awards are sorted by obligated amount descending. Most entries are task orders against a parent IDIQ vehicle, named in the "Parent IDV" column to cross-reference `vehicles.md`.

## §1 — Capability-area attribution summary

Of the 25 top awards, attribution-by-program-language maps as follows. Where a program clearly spans two areas, both are tagged.

| Capability area | Award count in top-25 | Notable programs |
|---|---|---|
| C3I (§1) | 4 | DCGS Enterprise Product Support; FEDND DEFEND A; TENCAP E3I; JIDA FS/DE |
| Cyber (§2) | 3 | CDM DEFEND Group A Bridge; FEDND DEFEND A; DTRA Counter-WMD Analytical Services |
| Digital Solutions (§3) | 4 | DAI Application Development; WBSCM 3; ELITE Enterprise IT; Background Investigations Fieldwork (×2) |
| Enterprise IT (§4) | 4 | Communication and IT Services III; ELITE; Background Investigations Fieldwork; CBTA (commercial-based technology analysis) |
| Mission and Engineering Support (§5) | 6 | Ship Design Services; Integrated Personnel and Pay System-Army (IPPS-A); AFSCN Maintenance and Modification; Beagle task order; Digital Engineering and Transformation; Border Enforcement Applications |
| Space (§6) | 1 | AFSCN Maintenance and Modification (also fits MES §5) |
| Spectrum Superiority (§7) | 2 | Full-Spectrum ISR Innovation (2019); Full-Spectrum ISR Innovation (2023 follow-on) |
| SOF / Counter-threat (cross-area) | 2 | SOF Emerging Threats Operations; DTRA Counter-WMD |

> **Assessment.** Mission and Engineering Support (§5) is the single capability area with the most top-25 award presence — six of 25. This is consistent with two facts from earlier sessions: (a) the 10-K explicitly names "naval architecture, training and simulation services, logistics engineering" under MES; (b) MES is the area with the strongest direct adjacency to the operator-team's work. The empirical award data corroborates that MES is a core CACI delivery area, not a peripheral one.

> **Assessment.** **Award EH02 ("SHIP DESIGN SERVICES", 2008-2018, DC place-of-performance)** is the most operator-team-relevant past-performance entry in the top-25. Ship design services for the U.S. Navy is exactly the naval-architecture work CACI corporate signals it can deliver — and CACI has a 10-year ship-design contract on record. This is foundational past-performance for the operator-team's Waterfront Operations sub-team work, even though the contract itself predates the operator's contract vehicle.

## §2 — The awards, ranked by obligated amount (top-50 window → 48 CACI awards)

Re-pulled 2026-06-07 with **real obligated amounts** (the 2026-05-31 pass had null amounts, so its "by amount" ordering was unreliable and is superseded). Sorted by obligated amount descending, FY2019–FY2026 window. Two **Acacia Center for Justice** rows (140D0422C0009, 75P00125C00016) were excluded as substring false-positives. Parent-IDV column names the vehicle where resolved; `(prime)` = prime contract, not a task order; `*` = the operator-team's own DTIC IAC MAC vehicle.

| # | Recipient (CACI subsidiary) | PIID | Obligated | PoP | Parent IDV | Description (first ~54 chars) |
|---|---|---|---|---|---|---|
| 1 | CACI, Inc. - Federal | GSQ0017AJ0006 | $960.0M | VA | OASIS Pool (407) | JIDA FS/DE task order |
| 2 | CACI, Inc. - Federal | 47QFCA19F0006 | $929.1M | VA | Alliant 2 | IGF::OT::IGF |
| 3 | CACI, Inc. - Federal | 47QFCA20F0010 | $824.3M | VA | Alliant 2 | BEAGLE task order award |
| 4 | CACI, Inc. - Federal | 47QFRA24F0005 | $762.6M | VA | Alliant 2 | CDM DEFEND Group A bridge task order |
| 5 | CACI NSS, LLC | 47QFCA21F0087 | $758.9M | NC | OASIS Pool 1 | SOF Emerging Threats Operations and Planning |
| 6 | CACI-ISS, LLC | W15QKN15C0049 | $733.7M | VA | (prime) | System integrator, IPPS-A Increment II |
| 7 | CACI, Inc. - Federal | HS002123F0020 | $716.5M | VA | DCSA backgrnd | Background investigation fieldwork services |
| 8 | CACI, Inc. - Federal | 47QFRA19F0011 | $708.3M | VA | Alliant 1 | FEDND DEFEND A (network defense) |
| 9 | CACI, Inc. - Federal | 47QFMA19F0013 | $674.9M | — | Alliant 2 | Communication and IT Services III |
| 10 | CACI NSS, LLC | FA882316C0004 | $600.7M | CO | (prime) | Consolidated AF Satellite Control Network maint |
| 11 | CACI NSS, LLC | FA875019F1000 | $578.4M | VA | AF ISR IDV | Full-Spectrum ISR Innovation |
| 12 | CACI Premier Technology, LLC | HS002119F0138 | $576.8M | VA | DCSA backgrnd | Background investigations fieldwork |
| 13 | CACI, Inc. - Federal | 47QFMA24F0014 | $535.6M | — | Alliant 2 | Enterprise Level IT Expertise (ELITE) |
| 14 | CACI, Inc. - Federal | 70B04C24F00001129 | $469.0M | VA | Alliant 2 | Border Enforcement Applications (GLEIT) |
| 15 | CACI, Inc. - Federal | FA807522F0030 | $468.3M | MD | DTIC IAC MAC* | Digital Engineering and Digital Transformation |
| 16 | CACI, Inc. - Federal | 47QFCA19F0050 | $451.5M | MD | OASIS Pool (407) | Commercial Based Technology Analysis (CBTA) |
| 17 | CACI NSS, LLC | GST0013AJ0065 | $424.4M | VA | Alliant 1 | Performance-based information services |
| 18 | CACI NSS, LLC | 47QFCA21F0057 | $399.6M | VA | OASIS Pool 1 | DTRA IMAX DA |
| 19 | CACI, Inc. - Federal | EH02 | $391.2M | DC | SeaPort-e | **SHIP DESIGN SERVICES** |
| 20 | CACI, Inc. - Federal | FA875023F0080 | $340.0M | VA | OASIS Pool (309) | Full-Spectrum ISR Innovation (follow-on) |
| 21 | CACI NSS, LLC | HDTRA123F0020 | $302.5M | VA | OASIS Pool 1 | DTRA Counter-WMD professional/analytical svcs |
| 22 | CACI, Inc. - Federal | 47QFCA19F0034 | $299.1M | VA | OASIS Pool (407) | TENCAP E3I award |
| 23 | CACI, Inc. - Federal | 47QFCA24F0011 | $284.3M | GA | OASIS Pool (309) | DCGS Enterprise Product Support |
| 24 | CACI, Inc. - Federal | 47QFCA21F0019 | $283.7M | NY | Alliant 2 | WBSCM 3 task order |
| 25 | CACI Enterprise Solutions | SP470922F0028 | $248.3M | VA | DLA (DAI) | DAI Application Development and Sustainment |
| 26 | CACI Premier Technology, LLC | 24362018F0104 | $247.4M | VA | OPM backgrnd | Background investigations TO #2 |
| 27 | CACI, Inc. - Federal | FA807524F0060 | $244.8M | VA | DTIC IAC MAC* | **Advanced Product Innovation and Delivery for NavalX** |
| 28 | CACI Technologies, LLC | 0127 | $238.5M | VA | Army S3 | PEO C3T engineering (S3R-043) |
| 29 | CACI NSS, LLC | 36C10B20F0250 | $234.5M | VA | IT Schedule 70 | VA FMBT/iFAMS interface development |
| 30 | CACI NSS, LLC | 70RTAC21FC0000006 | $215.3M | VA | DHS OCIO BPA | DHS OCIO services BPA call |
| 31 | CACI, Inc. - Federal | N6523610C2843 | $213.9M | VA | (prime) | IT Business Support Services (Navy) |
| 32 | CACI NSS, LLC | H9222210C0005 | $212.8M | NC | (prime) | USSOCOM labor (cost CLINs) |
| 33 | CACI, Inc. - Federal | 80TECH24CA002 | $212.7M | VA | (prime) | NASA Consolidated Application & Platform (NCAPS) |
| 34 | CACI Technologies, LLC | W56KGU20F0012 | $201.6M | VA | Army RS3 | Army RS3 five-year task order |
| 35 | CACI NSS, LLC | FA872623FB093 | $201.1M | VA | AF EITAAS | Enterprise Service Desk / Unified Endpoint |
| 36 | CACI Technologies, LLC | 0096 | $196.3M | VA | Army S3 | PEO C3T support |
| 37 | CACI NSS, LLC | 47QFCA20F0002 | $194.0M | — | OASIS Pool 1 | Plans/operations/logistics support |
| 38 | CACI Enterprise Solutions | N0003919F0202 | $193.1M | VA | CIO-SP3 | **MyNavy HR** |
| 39 | CACI, Inc. - Federal | H9240221C0005 | $190.7M | NC | (prime) | Geospatial intelligence services |
| 40 | CACI, Inc. - Federal | N0016417F3007 | $190.3M | VA | SeaPort-e | **Navy program management support** |
| 41 | CACI, Inc. - Federal | FA882124FB001 | $185.2M | CO | Alliant 2 | Data transport product support/sustainment |
| 42 | CACI, Inc. - Federal | EH07 | $180.5M | VA | SeaPort-e | **Navy (SeaPort-e task order)** |
| 43 | CACI, Inc. - Federal | GSQ0016AJ0002 | $179.0M | VA | Alliant 1 | WBSCM services |
| 44 | CACI Technologies, LLC | FK11 | $178.8M | VA | SeaPort-e | **NAVAL FORCES LOGISTICS SUPPORT** |
| 45 | CACI-Athena, LLC | H9222216C0029 | $176.5M | NC | (prime) | USSOCOM ODCS |
| 46 | CACI Technologies, LLC | W56KGU23F0009 | $172.4M | MD | Army RS3 | Replication/exploitation/analysis of threats |
| 47 | CACI Inc - Federal | 70T03018F2BCIO660 | $170.9M | DC | DHS EAGLE II | IT management/performance analysis |
| 48 | CACI, Inc. - Federal | EH03 | $168.0M | MD | SeaPort-e | **Navy (SeaPort-e task order)** |

`[caci-usaspending-refresh-2026-06-07]`

> **FACT.** Five awards in the top-48 sit under the Navy **SeaPort-e** IDV (N0017804D4030 / N0017804D4026), totaling ~$1.11B: EH02 Ship Design Services ($391.2M), N0016417F3007 Navy program management ($190.3M), EH07 ($180.5M), FK11 Naval Forces Logistics Support ($178.8M), and EH03 ($168.0M). `[caci-usaspending-refresh-2026-06-07]`

> **Assessment.** This SeaPort-e cluster is the most operator-relevant block in the entire top-48: it is CACI's Navy professional-services past performance — ship design, naval forces logistics, Navy program management — and its successor vehicle, **SeaPort NxG (N0017819D7295), is in `vehicles.md §2`** as the highest-relevance alternate routing path for the operator's region. So CACI's biggest Navy past performance and a live, long-runway Navy vehicle line up. Note the 2026-05-31 pass mis-tagged EH02 as a "prime contract" — it is in fact a SeaPort-e task order, now corrected.

## §2.1 — Awarding (administering) office vs. funding office (the true customer)

Pulled 2026-06-07 via per-award detail calls. The **administering office** issues the contract; the **funding office** is the real customer paying for the work — and for the many GSA-assisted awards the two diverge sharply. Same PIID order as §2.

| PIID | Administering office | Funding office (true customer) |
|---|---|---|
| GSQ0017AJ0006 | GSA FEDSIM | DTRA |
| 47QFCA19F0006 | GSA FEDSIM | Army Info Systems Engineering Cmd (W248) |
| 47QFCA20F0010 | GSA FEDSIM | VA Office of Information & Technology |
| 47QFRA24F0005 | GSA AAS Region 8 | CISA |
| 47QFCA21F0087 | GSA FEDSIM | Army Special Operations Command (W45V) |
| W15QKN15C0049 | ACC-PICA | PEO Enterprise (Army, IPPS-A) |
| HS002123F0020 | DCSA | DCSA |
| 47QFRA19F0011 | GSA AAS Region 8 | CISA |
| 47QFMA19F0013 | GSA AAS Region 3 | DFAS-INDY (GFEBS) |
| FA882316C0004 | FA8821 Sustainment BMC3 SSC | SMC Det 11 (Space) |
| FA875019F1000 | FA8750 AFRL RIK | AFRL RIEB |
| HS002119F0138 | DCSA | DCSA |
| 47QFMA24F0014 | GSA AAS Region 3 | DFAS-INDY (GFEBS) |
| 70B04C24F00001129 | CBP IT Contracting Div | VA Office of Information & Technology |
| FA807522F0030 | FA8075 774 ESS (DTIC IAC MAC) | OUSD(AT&L) |
| 47QFCA19F0050 | GSA FEDSIM | CCDC C5ISR Center (W4G8) |
| GST0013AJ0065 | GSA FEDSIM | Army Info Systems Engineering Cmd (W248) |
| 47QFCA21F0057 | GSA FEDSIM | DTRA |
| EH02 | **NAVSEA HQ** | **NAVSEA HQ** |
| FA875023F0080 | FA8750 AFRL RIK | AFRL RIEE |
| HDTRA123F0020 | DTRA | DTRA |
| 47QFCA19F0034 | GSA FEDSIM | PEO IEW&S Alexandria (W6DP) |
| 47QFCA24F0011 | GSA FEDSIM | AFLCMC ESG |
| 47QFCA21F0019 | GSA FEDSIM | USDA Food & Nutrition |
| SP470922F0028 | DCSO Philadelphia (DLA) | DCSO Philadelphia (DLA) |
| 24362018F0104 | OPM Boyers (FISD) | National Background Investigations Bureau |
| FA807524F0060 | FA8075 774 ESS (DTIC IAC MAC) | **Naval Air Systems Command (NAVAIR)** |
| 0127 | ACC-APG | Army HQ Comm-Electronics Cmd (W4GV) |
| 36C10B20F0250 | VA Technology Acquisition Center NJ | VA Technology Acquisition Center NJ |
| 70RTAC21FC0000006 | DHS Info Tech Acq Center | DHS Chief Information Officer |
| N6523610C2843 | **NIWC Atlantic** | **NIWC Atlantic** |
| H9222210C0005 | DCMA Southeast | HQ USSOCOM |
| 80TECH24CA002 | NASA IT Procurement Office | NASA IT Procurement Office |
| W56KGU20F0012 | ACC-APG | CCDC C5ISR Center (W4G8) |
| FA872623FB093 | FA8726 AFLCMC HNK C3IN | AFLCMC HNI |
| 0096 | ACC-APG | CCDC C5ISR Center (W4G8) |
| 47QFCA20F0002 | GSA FEDSIM | US Africa Command (W6L6) |
| N0003919F0202 | **NAVWAR** | **NAVWAR** (MyNavy HR) |
| H9240221C0005 | HQ USSOCOM | HQ USSOCOM |
| N0016417F3007 | DCMA Mid-Atlantic | **NAVSEA HQ** |
| FA882124FB001 | FA8821 Sustainment BMC3 SSC | SMC Det 11 (Space) |
| EH07 | **NSWC Crane** | **NAVSEA HQ** |
| GSQ0016AJ0002 | GSA FEDSIM | USDA Food & Nutrition |
| FK11 | **NAVSUP FLC Norfolk** | **Submarine Force Atlantic Fleet** |
| H9222216C0029 | HQ USSOCOM | HQ USSOCOM |
| W56KGU23F0009 | ACC-APG | SAF Financial Mgmt (F59900) |
| 70T03018F2BCIO660 | (closed out) | Acquisition Program Mgmt |
| EH03 | DCMA HQ | **PEO Submarines** |

`[caci-usaspending-refresh-2026-06-07]`

> **Assessment (the FEDSIM pattern).** About a dozen of CACI's largest awards are *administered* by **GSA FAS AAS FEDSIM** (GSA's assisted-acquisition shop) but *funded* by the real customer — DTRA, Army ISEC, Army Special Operations, CCDC C5ISR, PEO IEW&S, AFRICOM, AFLCMC, USDA. For the scoring layer this matters: the administering office tells you nothing about the customer. This is the general form of the capability book's "sponsoring agency vs. administering office" gap — and it resolves the operator-team's own case: **DTIC IAC MAC task orders are administered by FA8075 / 774 ESS (Air Force) but funded by the actual customer** (e.g., FA807522F0030 by OUSD(AT&L); the NavalX TO FA807524F0060 by NAVAIR).

> **Assessment (the Navy cluster — most operator-relevant).** CACI's Navy past performance concentrates in two customer hubs: (1) **NAVSEA HQ and the submarine enterprise** — EH02 Ship Design and N0016417F3007 funded by NAVSEA HQ, EH07 by NAVSEA HQ via NSWC Crane, FK11 Naval Forces Logistics by Submarine Force Atlantic Fleet, EH03 by **PEO Submarines**; and (2) **NAVWAR / NIWC** — MyNavy HR (NAVWAR) and IT Business Support (NIWC Atlantic). So beyond the SeaPort-e *vehicle* cluster, the *customers* are NAVSEA, the submarine PEOs/forces, and NAVWAR — the spine of the Navy technical-services world the operator-team sits adjacent to. Note also that the highest-value Navy line on the team's own DTIC IAC MAC vehicle (NavalX, $244.8M) is **NAVAIR-funded**.

## §3 — Highest-priority observations

### §3.1 — Operator-team-relevant past performance

> **FACT.** **Award #15 (CACI, Inc. - Federal, PIID FA807522F0030) is a task order against the DTIC IAC MAC vehicle (FA807518D0006)** — the operator-team's own IDIQ. Scope: "Digital Engineering and Digital Transformation Research, Analysis, and Development." Place of performance: MD. Period: 2022-05 to 2027-05. `[caci-usaspending-top25-2026-05-31]`

> **Assessment.** This is the first concrete data point I have on what other task orders exist under FA807518D0006. It confirms the DTIC IAC MAC vehicle is used for technical research-and-development work, with a MD (likely Aberdeen / Patuxent / Naval Surface Warfare Center area) place-of-performance and a five-year POP. The operator's task order at SRF-JRMC Yokosuka is therefore one of multiple distinct customers/locations under the same parent IDIQ. The "Digital Engineering and Digital Transformation" framing of TO #15 is also relevant to the operator-team's active Big Bear AI engagement for DFS workflow automation and additive manufacturing — that's the kind of digital engineering scope.

> **FACT.** **Award #19 (CACI, Inc. - Federal, PIID EH02) is "SHIP DESIGN SERVICES"** — a 10-year prime contract (2008-12-19 to 2018-09-01) with place of performance in DC. `[caci-usaspending-top25-2026-05-31]`

> **Assessment.** This is the past-performance citation that anchors CACI's "naval architecture" Expertise claim (from the FY25 10-K Mission and Engineering Support market area). A decade-long ship-design contract demonstrates CACI has real capability in the operator-team's Waterfront Operations sub-team domain. The contract itself ended in 2018-09 — the same month the DTIC IAC MAC vehicle started — so there's a potential bridging story (the operator-team's vehicle may be the successor delivery mechanism for similar work, though this requires verification).

### §3.2 — Capability-area-specific past performance

**C3I (§1)** — confirmed via:
- Award #23 — DISTRIBUTED COMMON GROUND SYSTEM (DCGS) ENTERPRISE PRODUCT SUPPORT, 2024-2026 (GA place of performance). Directly confirms the DCGS program from the caci.com C3I page.
- Award #22 — TENCAP E3I (Air Force Tactical Exploitation of National Capabilities Program), 2019-2024.
- Award #1 — JIDA FS/DE Task Order, "Full-Spectrum / Data Engineering" for Joint Improvised Threats Defeat Agency. ~$1.77B not-to-exceed ceiling per description.

**Cyber (§2)** — confirmed via:
- Award #5 — CDM DEFEND GROUP A BRIDGE TASK ORDER (DHS Continuous Diagnostics and Mitigation program), 2024-2027.
- Award #7 — FEDND DEFEND A (Federal Enterprise Network Defense), 2019-2024 (predecessor to CDM).
- Award #21 — DTRA Counter-WMD Professional and Analytical Services, 2023-2026.

**Digital Solutions (§3) / Enterprise IT (§4)** — overlapping confirmation via:
- Award #25 — DAI Application Development and Sustainment Support (DLA Defense Agencies Initiative ERP), 2022-2026.
- Award #24 — WBSCM 3 (USDA Web-Based Supply Chain Management), 2021-2027.
- Award #13 — ELITE (Enterprise Level IT Expertise), 2024-2029.
- Award #8 — Communication and Information Technology Services III, 2019-2024.

**Mission and Engineering Support (§5)** — confirmed via:
- Award #19 — SHIP DESIGN SERVICES (naval architecture, 2008-2018).
- Award #6 — IPPS-A System Integrator (Integrated Personnel and Pay System-Army), 2015-2025, Increment II.
- Award #10 — AFSCN Maintenance and Modification (Consolidated Air Force Satellite Control Network), 2016-2025.

**Space (§6)** — confirmed via:
- Award #10 (cross-tagged with MES) — Air Force Satellite Control Network operations.

**Spectrum Superiority (§7)** — confirmed via:
- Award #11 + Award #20 — FULL-SPECTRUM INTELLIGENCE, SURVEILLANCE, AND RECONNAISSANCE (ISR) INNOVATION (Air Force), 2019-2024 plus 2023-2028 follow-on. Two consecutive contracts on the same program demonstrate sustained Air Force ISR relationship — likely Azure Summit-relevant (Azure Summit acquired October 2024, contributes RF/EW/ISR engineering).

### §3.3 — Vehicle attribution updates for vehicles.md §5

The USAspending URLs reveal parent IDV cross-references that improve identification of the 14 unnamed USAspending-observed vehicles:

- **47QTCK18D0009 (Alliant 2)** is the parent of awards #2, #3, #5, #7, #8, #13, #16, #22, #23, #24 — ten of 25 top awards. **Alliant 2 is the most heavily-used CACI vehicle by award count in the top-25.** This is a meaningful empirical correction: Alliant 2 may be more important to CACI's delivery model than the relatively-modest 2.0% share statistic in `baseline_caci_footprint.vehicles` suggests (note: that statistic was at the parent-IDV level not aggregating task orders).
- **GS00Q14OADU121 (OASIS Pool 1)** is the parent of award #4 — confirming the team_vehicles_held_by_caci_nss attribution.
- **GS00Q14OADU407 (a different OASIS pool)** is the parent of award #1 (JIDA FS/DE). New IDV identification.
- **DTIC IAC MAC (FA807518D0006)** — the operator-team's vehicle — is the parent of award #15.
- **SP47-family** (DLA Land and Maritime) is the parent of award #25 (DAI).

### §3.4 — Newly-discovered CACI subsidiary

> **FACT.** **CACI Premier Technology, LLC** appears in the top-25 (award #12, Background Investigations Fieldwork Services for DHS). Previously not enumerated in the vault. `[caci-usaspending-top25-2026-05-31]`

> **Assessment.** CACI Premier Technology specializes in background investigations. This is a distinct capability domain — DCSA/DOJ-aligned personnel investigations — not represented in the caci.com seven-area taxonomy. Either it's a "below-the-line" specialty subsidiary not foregrounded in CACI's corporate capability marketing, or it falls under Mission and Engineering Support (§5)'s "Intelligence analysis and operations" sub-capability with a security-clearance specialization. Worth noting that the Cyber (§2) area also has potential affinity given clearance-process work.

## §4 — Research gaps (updated 2026-06-07)

Closed in the 2026-06-07 refresh:
- **Dollar amounts** — now populated for all 48 (the §2 table). The "by amount" ranking is now trustworthy.
- **Sub-25 awards** — extended to the top-50 window (48 CACI awards after Acacia exclusion).
- **Vehicle attribution** — parent IDVs resolved across the table (Alliant 1/2, OASIS pools, SeaPort-e, DTIC IAC MAC, Army S3/RS3, DLA, AF EITAAS, DHS, etc.); cross-references `vehicles.md §5`.

Closed (continued):
- **Per-award awarding/funding office** — done for all 48 (§2.1). Surfaced the GSA-FEDSIM administering-vs-funding split and CACI's NAVSEA/submarine + NAVWAR Navy customer cluster.

Still open / newly surfaced:
- **CACI Premier Technology's full portfolio** — still only seen via background-investigations awards (#12, #26). A targeted recipient search would surface its scope. (Also newly noted: **CACI-Athena, LLC** at #45 — another subsidiary not yet documented.)
- **Place-of-performance Pacific representation.** Of the top 48 by amount, ZERO have a Pacific place of performance (no HI/GU/JA in the state field) — all National Capital Region (VA/DC/MD) and CONUS. The operator-team's Pacific footprint remains a deliberate geographic extension invisible in top-award analytics — empirical support for the "team is a strategic geographic outpost" framing. (Caveat: place of performance for IDIQ-wide task orders is often recorded at the contracting/HQ location, not the actual work site, so this understates true Pacific delivery.)

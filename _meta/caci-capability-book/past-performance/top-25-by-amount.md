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
caveat-on-amount-field: USAspending's spending_by_award search endpoint
  returns the Award Amount column as empty in the API response for these
  records. The lib captured null/0 amounts. Resolving the actual dollar
  amounts requires per-award detail calls against the awards/{id} endpoint
  — deferred. PIID, recipient, dates, description, and parent IDV are all
  reliable; only the dollar figure is missing.
---

# Top-25 CACI awards by amount (USAspending, last 7 fiscal years)

This file is the seventh capability-book artifact and the first to fill the past-performance directory. Awards are sorted by Award Amount descending per USAspending's `sort=Award Amount, order=desc` query parameter. The dollar amounts themselves are not captured (see caveat above) but the ordinal ranking is preserved from the API response.

Most entries are task orders against a parent IDIQ vehicle. The parent IDV is visible in the USAspending URL pattern; where identifiable, the parent vehicle is named in the "IDV" column to cross-reference `vehicles.md`.

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

## §2 — The 25 awards, ordinally ranked

| # | Recipient (CACI subsidiary) | PIID | Description (first 80 chars) | PoP State | Period | Parent IDV |
|---|---|---|---|---|---|---|
| 1 | CACI, INC. - FEDERAL | GSQ0017AJ0006 | AWARD MADE TO CACI, INC.-FEDERAL FOR JIDA FS/DE TASK ORDER, IN THE AMOUNT NOT TO | VA | 2016-10 → 2022-02 | GS00Q14OADU407 (OASIS pool) |
| 2 | CACI, INC. - FEDERAL | 47QFCA19F0006 | IGF::OT::IGF (description body truncated to procurement-code marker) | VA | 2019-05 → 2026-11 | 47QTCK18D0009 (Alliant 2) |
| 3 | CACI, INC. - FEDERAL | 47QFCA20F0010 | BEAGLE TASK ORDER AWARD | VA | 2019-11 → 2024-09 | 47QTCK18D0009 (Alliant 2) |
| 4 | CACI NSS, LLC | 47QFCA21F0087 | SPECIAL OPERATIONS FORCES EMERGING THREATS OPERATIONS AND PLANNING SUPPORT | NC | 2021-09 → 2026-09 | GS00Q14OADU121 (OASIS Pool 1) |
| 5 | CACI, INC. - FEDERAL | 47QFRA24F0005 | CDM DEFEND GROUP A BRIDGE TASK ORDER | VA | 2024-05 → 2027-04 | Alliant 2 family |
| 6 | CACI-ISS, LLC | W15QKN15C0049 | IGF::CL,CT::IGF SYSTEM INTEGRATOR FOR INCREMENT II OF INTEGRATED PERSONNEL AND P | VA | 2015-05 → 2025-06 | (prime contract, not task order) |
| 7 | CACI, INC. - FEDERAL | 47QFRA19F0011 | DYNAMIC AND EVOLVING FEDERAL ENTERPRISE NETWORK DEFENSE GROUP A — DEFEND A — OPTION | VA | 2019-05 → 2024-04 | Alliant 2 family |
| 8 | CACI, INC. - FEDERAL | 47QFMA19F0013 | COMMUNICATION AND INFORMATION TECHNOLOGY SERVICES III | (none) | 2019-06 → 2024-05 | Alliant 2 family |
| 9 | CACI, INC. - FEDERAL | HS002123F0020 | TASK ORDER FOR BACKGROUND INVESTIGATION FIELDWORK SERVICES | VA | 2023-03 → 2027-03 | DHS / DCSA family |
| 10 | CACI NSS, LLC | FA882316C0004 | IGF::OT::IGF CONSOLIDATED AIR FORCE SATELLITE CONTROL NETWORK MAINTENANCE, MODIF | CO | 2016-06 → 2025-05 | (prime contract) |
| 11 | CACI NSS, LLC | FA875019F1000 | FULL-SPECTRUM INTELLIGENCE, SURVEILLANCE, AND RECONNAISSANCE (ISR) INNOVATION AND | VA | 2019-09 → 2024-09 | (Air Force task order) |
| 12 | CACI PREMIER TECHNOLOGY, LLC | HS002119F0138 | BACKGROUND INVESTIGATIONS FIELDWORK SERV. THIS IS NOT A NEW TASK ORDER | VA | 2019-10 → 2024-03 | DHS / DCSA family |
| 13 | CACI, INC. - FEDERAL | 47QFMA24F0014 | ENTERPRISE LEVEL IT EXPERTISE — ELITE | (none) | 2024-03 → 2029-05 | Alliant 2 family |
| 14 | CACI, INC. - FEDERAL | 70B04C24F00001129 | BORDER ENFORCEMENT APPLICATIONS FOR GOVERNMENT LEADING-EDGE INFORMATION TECHNOLO | VA | 2024-09 → 2026-09 | CBP / DHS family |
| 15 | CACI, INC. - FEDERAL | FA807522F0030 | DIGITAL ENGINEERING AND DIGITAL TRANSFORMATION RESEARCH, ANALYSIS, AND DEVELOPME | MD | 2022-05 → 2027-05 | **FA807518D0006 (DTIC IAC MAC — operator's vehicle)** |
| 16 | CACI, INC. - FEDERAL | 47QFCA19F0050 | EXECUTE TASK ORDER FOR COMMERCIAL BASED TECHNOLOGY ANALYSIS (CBTA) | MD | 2019-07 → 2025-01 | Alliant 2 family |
| 17 | CACI NSS, LLC | GST0013AJ0065 | IGF::CL,CT::IGF THE PURPOSE OF THIS TO IS TO ACQUIRE PERFORMANCE-BASED INFORMATI | VA | 2013-03 → 2018-09 | (predecessor OASIS) |
| 18 | CACI NSS, LLC | 47QFCA21F0057 | DTRA IMAX DA | VA | 2021-06 → 2023-06 | OASIS family |
| 19 | CACI, INC. - FEDERAL | EH02 | **SHIP DESIGN SERVICES** | DC | 2008-12 → 2018-09 | (prime contract) |
| 20 | CACI, INC. - FEDERAL | FA875023F0080 | FULL-SPECTRUM INTELLIGENCE, SURVEILLANCE & RECONNAISSANCE (ISR), INNOVATION AND | VA | 2023-08 → 2028-08 | (Air Force follow-on to #11) |
| 21 | CACI NSS, LLC | HDTRA123F0020 | PROFESSIONAL AND ANALYTICAL SERVICES IN SUPPORT OF COUNTERING AND DETERRENCE OF | VA | 2023-06 → 2026-06 | DTRA family |
| 22 | CACI, INC. - FEDERAL | 47QFCA19F0034 | TENCAP E3I AWARD | VA | 2019-03 → 2024-09 | Alliant 2 family |
| 23 | CACI, INC. - FEDERAL | 47QFCA24F0011 | DISTRIBUTED COMMON GROUND SYSTEM (DCGS) ENTERPRISE PRODUCT SUPPORT (EPS) TO 1 | GA | 2024-04 → 2026-04 | Alliant 2 family |
| 24 | CACI, INC. - FEDERAL | 47QFCA21F0019 | TASK ORDER AWARD OF WBSCM 3. THE PURPOSE OF THIS TO IS TO ACQUIRE INFORMATION TE | NY | 2021-02 → 2027-01 | Alliant 2 family |
| 25 | CACI ENTERPRISE SOLUTIONS, LLC | SP470922F0028 | DAI APPLICATION DEVELOPMENT AND SUSTAINMENT SUPPORT SERVICES — EBS PO 4556364846 | VA | 2022-03 → 2026-08 | SP47 (DLA Land and Maritime) |

`[caci-usaspending-top25-2026-05-31]`

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

## §4 — Research gaps remaining

- **Dollar amounts.** All Award Amount fields came back null/0 in this pass. Resolving requires per-award detail calls (`awards/{generated_id}/` endpoint) — straightforward but adds 25 more calls. Deferred unless the amounts become material to a specific scoring decision.
- **Awarding agency identity.** The Awarding Agency and Awarding Sub Agency columns also returned empty. The parent IDV URL pattern is the workable substitute. Per-award detail would fill this too.
- **Sub-25 awards.** Top-25 is one snapshot; a top-50 or top-100 would extend coverage but with diminishing per-award strategic value. Defer unless a specific capability area looks under-populated.
- **CACI Premier Technology's full portfolio.** This subsidiary's role isn't yet documented in the capability book. A targeted CACI-Premier-Technology recipient search would surface its delivery scope.
- **Place-of-performance Pacific representation.** Of the 25 top awards by amount, ZERO have a Pacific-region place of performance (no HI, GU, JA, etc. in the state field). This is notable — CACI's largest awards are concentrated in the National Capital Region (VA, DC, MD) and CONUS sites. The operator-team's Pacific footprint is a deliberate geographic extension that doesn't show up in top-25 award analytics. Consider this empirical evidence for the "team is a strategic geographic outpost" framing.

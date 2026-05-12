# FACT Verification Report — PMTEC-USINDOPACOM

*Generated 2026-05-12T17:22:50 by `verify_facts.py` (model: `claude-sonnet-4-6`)*

## Summary

- **14** FACT claims scanned
- **3** SUPPORTS — claim is corroborated by an ingested source
- **10** PARTIAL — some elements supported by an ingested source
- **1** DOES_NOT_SUPPORT — ingested source contradicts or omits the claim
- **0** UNVERIFIABLE — cited source(s) not yet in 01_sources/

## Verifications

### ⚑ FACT #1 §3  —  **PARTIAL**

**Claim:**
> At a PMTEC quarterly industry meeting, USINDOPACOM J7 — through its named program leads — laid out the following technology priorities and gaps for industry engagement [s.2026-05-12-usindopacom-seeks-industry-par]: 1. **Live-Virtual-Constructive (LVC) integration** — connecting live forces with simulated elements for comprehensive training scenarios. 2. **Data analytics and assessment tools** — to…

**Citations:** [s.2026-05-12-usindopacom-seeks-industry-par] [s.2026-04-22-pacom]

**Sources checked:**
- `[s.2026-05-12-usindopacom-seeks-industry-par]` → `01_sources/2026-05-12_pacom-mil_usindopacom-seeks-industry-partners-to-address-modern-milita.md` — verdict: **PARTIAL** ([source](https://www.pacom.mil/About-USINDOPACOM/PMTEC/Article/4467480/usindopacom-seeks-industry-partners-to-address-modern-military-challenges/))
- `[s.2026-04-22-pacom]` → ⚠ not in `01_sources/` (cited only in §8.2)
  > _"USINDOPACOM's technology priorities include live-virtual-constructive integration—connecting live forces with simulated elements to create comprehensive training scenarios; data analytics and assessment tools to process and analyze training data to improve performance evaluation; non-kinetic effects simulation tools to replicate cyber-attacks, electronic warfare, and information operations in trai…"_
  - Missing in this source: 1) The claim attributes item 5 (AI and digital-twin technologies) to Mary Ann Swendsen on the AI need AND to Stridiron announcing the APL (Applied Physics Laboratory) partnership — the source says Stridiron announced a Johns Hopkins University partnership (APL is part of JHU but is not named in the source); Swendsen is associated with AI strategy support in the source but the claim's specific attribution framing ('experimentation integrator, on the AI need') is a reasonable match. 2) The claim states Stridiron 'announced the APL partnership' — the source says 'a new research partnership with Johns Hopkins University' without naming APL specifically. 3) The claim references a 'PMTEC quarterly industry meeting' and an earlier planning note mentions '13 March 2026 Quarterly Commercial Industry Update' — neither the specific date nor the literal 'eight gaps' framing appears in the source. 4) The claim frames items 1–4 as 'technology priorities' and items 5–8 as narrative gaps — this structural framing is a reasonable interpretation of the source but the source does not use the word 'gaps' or enumerate exactly eight items. 5) The Department referenced in the source for AI strategy is 'Department of War' (likely a source error for Department of Defense), not verified in the claim.
  - Model note: The source explicitly supports items 1–4 (LVC, data analytics, non-kinetic effects, multi-level secure sharing), items 5–8 with named personnel (Stridiron/JHU partnership, Swendsen/AI, Bednarcik/Cobra Gold targets, Emslie/Hannah/PWSA, Matsunaka/Hall/RJTI), but the claim's reference to 'APL' is not in the source (only 'Johns Hopkins University' is named), and the specific event date and 'eight gaps' framing are absent from the source.

### ⚑ FACT #2 §3  —  **PARTIAL**

**Claim:**
> FY26 PDI request: **$10.0B** (Grand Total $10,004,542 thousand per primary source — the FY26 PDI budget book). FY25 baseline appears to be ~$9.4B (Grand Total column 2 in the same book). PMTEC is a named line item across multiple PB sub-accounts [s.2026-fy26-comptroller] [s.2026-05-12-fy2026-pacific-deterrence-init]. *Correction 2026-05-12: planning-conversation figure was "$9.9B" — primary source…

**Citations:** [s.2026-fy26-comptroller] [s.2026-05-12-fy2026-pacific-deterrence-init]

**Sources checked:**
- `[s.2026-fy26-comptroller]` → ⚠ not in `01_sources/` (cited only in §8.2)
- `[s.2026-05-12-fy2026-pacific-deterrence-init]` → `01_sources/2026-05-12_comptroller-war-gov_fy2026-pacific-deterrence-initiative.md` — verdict: **PARTIAL** ([source](https://comptroller.war.gov/Portals/45/Documents/defbudget/FY2026/FY2026_Pacific_Deterrence_Initiative.pdf))
  > _"The DoD is focused on maintaining and extending our military advantage in the region, paced to threats posed by China. The FY 2026 PDI request is $10.0 billion; these investments and activities demonstrate U.S. commitment to deterring China. ... Grand Total 7,842,993 2,161,549 10,004,542"_
  - Missing in this source: The FY25 baseline figure of ~$9.4B is not present anywhere in the source content provided. PMTEC as a named line item across multiple PB sub-accounts is not evidenced in the extracted source content.
  - Model note: The source explicitly supports the FY26 PDI request of $10.0B ($10,004,542 thousand grand total), but provides no FY25 baseline figures and no mention of PMTEC as a line item in the extracted content.

### ✗ FACT #3 §3  —  **DOES_NOT_SUPPORT**

**Claim:**
> The FY26 PDI book funds PMTEC across three service components within the "Exercises, Training, Experimentation, and Innovation" PDI category [s.2026-05-12-fy2026-pacific-deterrence-init]: - **Department of the Army ($851M total)** — Operation & Maintenance funds *"rotations at the Joint Pacific Multinational Readiness Training Center (JPMRC) and the Pacific Multi-Domain Training and Experimentatio…

**Citations:** [s.2026-05-12-fy2026-pacific-deterrence-init]

**Sources checked:**
- `[s.2026-05-12-fy2026-pacific-deterrence-init]` → `01_sources/2026-05-12_comptroller-war-gov_fy2026-pacific-deterrence-initiative.md` — verdict: **DOES_NOT_SUPPORT** ([source](https://comptroller.war.gov/Portals/45/Documents/defbudget/FY2026/FY2026_Pacific_Deterrence_Initiative.pdf))
  - Missing in this source: All specific PMTEC-related claims are absent from the provided source content: (1) Army $851M total with JPMRC/PMTEC language; (2) Navy $588M total with Pacific Fixed Arrays/PMTEC studies/live-fire target support/JFDD/JDECC language; (3) Air Force $752M total with 'PMTEC Operations' sub-category and 0207429F Combat Training Ranges at $147.2M; (4) Joint Staff $310M slice covering JTEEP and Theater Forces. None of the 'Exercises, Training, Experimentation, and Innovation' section content is present in the extracted pages.
  - Model note: The source content provided does not include the 'Exercises, Training, Experimentation, and Innovation' section (pages ~19-24 per the table of contents), which is where PMTEC funding descriptions would appear; the extracted pages only cover through the Improved Logistics section and therefore contain no text supporting any element of the PMTEC claim.

### ⚑ FACT #4 §3  —  **PARTIAL**

**Claim:**
> PMTEC runs a Quarterly Commercial Industry Update (most recent: 13 March 2026, Honolulu, hosted with Defense Innovation OnRamp Hub: Hawaii) [s.2026-04-22-pacom] [s.2026-05-12-usindopacom-seeks-industry-par].

**Citations:** [s.2026-04-22-pacom] [s.2026-05-12-usindopacom-seeks-industry-par]

**Sources checked:**
- `[s.2026-04-22-pacom]` → ⚠ not in `01_sources/` (cited only in §8.2)
- `[s.2026-05-12-usindopacom-seeks-industry-par]` → `01_sources/2026-05-12_pacom-mil_usindopacom-seeks-industry-partners-to-address-modern-milita.md` — verdict: **PARTIAL** ([source](https://www.pacom.mil/About-USINDOPACOM/PMTEC/Article/4467480/usindopacom-seeks-industry-partners-to-address-modern-military-challenges/))
  > _"The event, hosted by USINDOPACOM J7 Pacific Multi-Domain Training and Experimentation Capability (PMTEC) and the Defense Innovation OnRamp Hub: Hawaii, a program of the Defense Innovation Unit, connected military leaders with industry representatives to outline a path toward a more integrated, all-domain training and operations ecosystem in the region."_
  - Missing in this source: The source confirms a quarterly industry meeting hosted with Defense Innovation OnRamp Hub: Hawaii, but does not specify the date as 13 March 2026, nor does it mention Honolulu as the location, nor does it use the specific title 'Quarterly Commercial Industry Update'.
  - Model note: The source confirms PMTEC holds quarterly industry meetings co-hosted with Defense Innovation OnRamp Hub: Hawaii, but the specific date (13 March 2026), location (Honolulu), and event title ('Quarterly Commercial Industry Update') are not explicitly stated in the source text.

### ✓ FACT #5 §3  —  **SUPPORTS**

**Claim:**
> Formal industry intake channel: pacom.mil/Contact/Industry-Engagements/ [s.2026-04-22-pacom] [s.2026-05-12-usindopacom-seeks-industry-par].

**Citations:** [s.2026-04-22-pacom] [s.2026-05-12-usindopacom-seeks-industry-par]

**Sources checked:**
- `[s.2026-04-22-pacom]` → ⚠ not in `01_sources/` (cited only in §8.2)
- `[s.2026-05-12-usindopacom-seeks-industry-par]` → `01_sources/2026-05-12_pacom-mil_usindopacom-seeks-industry-partners-to-address-modern-milita.md` — verdict: **SUPPORTS** ([source](https://www.pacom.mil/About-USINDOPACOM/PMTEC/Article/4467480/usindopacom-seeks-industry-partners-to-address-modern-military-challenges/))
  > _"He directed potential partners to the command's online portal at https://www.pacom.mil/Contact/Industry-Engagements/"_
  - Model note: The source explicitly identifies https://www.pacom.mil/Contact/Industry-Engagements/ as the formal industry intake portal, directed by Maj. Tuan Nguyen for companies interested in working with USINDOPACOM.

### ⚑ FACT #6 §3  —  **PARTIAL**

**Claim:**
> Maj. Tuan Nguyen (J83 Joint Validation Division) is the formal industry intake POC [s.2026-04-22-pacom] [s.2026-05-12-usindopacom-seeks-industry-par].

**Citations:** [s.2026-04-22-pacom] [s.2026-05-12-usindopacom-seeks-industry-par]

**Sources checked:**
- `[s.2026-04-22-pacom]` → ⚠ not in `01_sources/` (cited only in §8.2)
- `[s.2026-05-12-usindopacom-seeks-industry-par]` → `01_sources/2026-05-12_pacom-mil_usindopacom-seeks-industry-partners-to-address-modern-milita.md` — verdict: **PARTIAL** ([source](https://www.pacom.mil/About-USINDOPACOM/PMTEC/Article/4467480/usindopacom-seeks-industry-partners-to-address-modern-military-challenges/))
  > _"Maj. Tuan Nguyen, who represents industry engagement for the J83 Joint Validation Division, provided guidance for companies interested in working with USINDOPACOM. He directed potential partners to the command's online portal at https://www.pacom.mil/Contact/Industry-Engagements/ and emphasized the importance of understanding military requirements before submitting proposals."_
  - Missing in this source: The source does not describe Maj. Nguyen as the 'formal industry intake POC'; it describes him as representing 'industry engagement' for J83 and providing guidance, but does not use the term 'formal' or explicitly designate him as the primary/formal point of contact for industry intake.
  - Model note: The source confirms Maj. Nguyen's role in industry engagement for J83 Joint Validation Division and his guidance function, but does not explicitly characterize him as the 'formal industry intake POC,' making the claim only partially supported.

### ⚑ FACT #7 §3  —  **PARTIAL**

**Claim:**
> Brent Parker (PMTEC Commercial Industry Engagement Lead, contractor) is the working-level POC; email brent.m.parker2.ctr@us.navy.mil [s.2026-04-22-pacom] [s.2026-05-12-usindopacom-seeks-industry-par]. *Role title and identity confirmed via ingested [s.2026-05-11-driving-readiness-indopacom-j7] which names him "PMTEC Industry Engagement Lead" moderating the POST 2026 panel. The .ctr email is single…

**Citations:** [s.2026-04-22-pacom] [s.2026-05-12-usindopacom-seeks-industry-par] [s.2026-05-11-driving-readiness-indopacom-j7]

**Sources checked:**
- `[s.2026-04-22-pacom]` → ⚠ not in `01_sources/` (cited only in §8.2)
- `[s.2026-05-12-usindopacom-seeks-industry-par]` → `01_sources/2026-05-12_pacom-mil_usindopacom-seeks-industry-partners-to-address-modern-milita.md` — verdict: **PARTIAL** ([source](https://www.pacom.mil/About-USINDOPACOM/PMTEC/Article/4467480/usindopacom-seeks-industry-partners-to-address-modern-military-challenges/))
- `[s.2026-05-11-driving-readiness-indopacom-j7]` → `01_sources/2026-05-11_dvidshub-net_driving-readiness-indopacom-j7-outlines-all-domain-training.md` — verdict: **PARTIAL** ([source](https://www.dvidshub.net/news/561976/driving-readiness-indopacom-j7-outlines-all-domain-training-strategy-post-2026))
  > _""For companies with relevant capabilities, PMTEC offers an opportunity to contribute to defense preparedness while testing and refining their technologies in operational environments," said PMTEC Industry Engagement Lead, Brent Parker. For more information on PMTEC Industry Engagement events and activities, contact Brent Parker at brent.m.parker2.ctr@us.navy.mil"_
  - Missing in this source: The claim states the role title and email are 'single-sourced to the un-ingested pacom.mil article' and that identity was 'confirmed via ingested [source] which names him PMTEC Industry Engagement Lead moderating the POST 2026 panel.' The source does confirm the name, title ('PMTEC Industry Engagement Lead'), and email (brent.m.parker2.ctr@us.navy.mil) directly. However, the claim also asserts the contractor designation (the .ctr suffix implies contractor status but the source does not explicitly state 'contractor'), and the claim's assertion about a separate ingested source confirming him moderating a 'POST 2026 panel' is not evidenced in this source.
  - Model note: The source directly supports the name, title, and email address, but does not explicitly confirm the 'contractor' role designation nor the 'POST 2026 panel moderation' referenced as coming from a separately ingested source.
  > _"The panel, moderated by PMTEC Industry Engagement Lead Brent Parker, featured insights from USINDOPACOM's J7 Director, Brig. Gen. Richard Goodman; J7 Director of Staff and Training, Andrew Merz; PMTEC Program Manager Dr. Andre Stridiron, and Technical Director of the K. Mark Takai Pacific Warfighting Center, Allan Grove."_
  - Missing in this source: The source confirms Brent Parker's name and role title ('PMTEC Industry Engagement Lead') and his moderation of the POST 2026 panel, but does NOT contain his email address (brent.m.parker2.ctr@us.navy.mil), his contractor status, or the descriptor 'Commercial Industry Engagement Lead' (the source uses 'Industry Engagement Lead' without 'Commercial').
  - Model note: The ingested source supports Parker's identity and role title as moderator of the POST 2026 panel, but the email address and contractor designation are not present in this source, consistent with the claim's own caveat that the email is single-sourced to an un-ingested pacom.mil article.

### ⚑ FACT #8 §4  —  **PARTIAL**

**Claim:**
> PMTEC was established in 2022 by USINDOPACOM J7 [s.2026-04-22-pacom] [s.2026-05-12-usindopacom-seeks-industry-par]. *Corroborated by ingested primary source [s.2026-05-11-multinational-forces-destroy-d] (pacom.mil PMTEC Article 4478558), which states: "About PMTEC: Established in 2022, the Pacific Multi-Domain Training and Experimentation Capability is a transformative enterprise funded and resour…

**Citations:** [s.2026-04-22-pacom] [s.2026-05-12-usindopacom-seeks-industry-par] [s.2026-05-11-multinational-forces-destroy-d]

**Sources checked:**
- `[s.2026-04-22-pacom]` → ⚠ not in `01_sources/` (cited only in §8.2)
- `[s.2026-05-12-usindopacom-seeks-industry-par]` → `01_sources/2026-05-12_pacom-mil_usindopacom-seeks-industry-partners-to-address-modern-milita.md` — verdict: **PARTIAL** ([source](https://www.pacom.mil/About-USINDOPACOM/PMTEC/Article/4467480/usindopacom-seeks-industry-partners-to-address-modern-military-challenges/))
- `[s.2026-05-11-multinational-forces-destroy-d]` → `01_sources/2026-05-11_pacom-mil_multinational-forces-destroy-dynamic-threat-targets-during-b.md` — verdict: **PARTIAL** ([source](https://www.pacom.mil/About-USINDOPACOM/PMTEC/Article/4478558/))
  > _"About PMTEC: Established in 2022, the Pacific Multi-Domain Training and Experimentation Capability is a transformative enterprise funded and resourced by the United States Indo-Pacific Command"_
  - Missing in this source: The claim states PMTEC was 'established in 2022 by USINDOPACOM J7,' but the source attributes establishment/funding/resourcing to USINDOPACOM broadly, not specifically J7. The source describes J7 as overseeing/hosting PMTEC but does not state J7 established it.
  - Model note: The source confirms PMTEC was established in 2022 and is funded/resourced by USINDOPACOM, but attributes establishment to USINDOPACOM as a whole, not specifically to J7, making the 'by USINDOPACOM J7' element unsupported.
  > _"About PMTEC: Established in 2022, the Pacific Multi-Domain Training and Experimentation Capability is a transformative enterprise funded and resourced by the United States Indo-Pacific Command"_
  - Missing in this source: The claim states PMTEC was established 'by USINDOPACOM J7,' but the source only states it was 'funded and resourced by the United States Indo-Pacific Command' — the J7 directorate is not identified as the establishing authority in the source text.
  - Model note: The source confirms PMTEC was established in 2022 and is associated with USINDOPACOM, but does not attribute its establishment specifically to the J7 directorate; J7 is only mentioned as the operator/supporter of PMTEC events, not as the founding entity.

### ✓ FACT #9 §4  —  **SUPPORTS**

**Claim:**
> PMTEC integrates geographically distributed ranges and training areas across the Indo-Pacific — described by program leadership as the world's largest coalition range system [s.2026-04-03-dvids-post]. *Corroborated by ingested primary source [s.2026-05-11-multinational-forces-destroy-d] (pacom.mil PMTEC Article 4478558): "It has created and is constantly enhancing the largest coalition range syste…

**Citations:** [s.2026-04-03-dvids-post] [s.2026-05-11-multinational-forces-destroy-d]

**Sources checked:**
- `[s.2026-04-03-dvids-post]` → ⚠ not in `01_sources/` (cited only in §8.2)
- `[s.2026-05-11-multinational-forces-destroy-d]` → `01_sources/2026-05-11_pacom-mil_multinational-forces-destroy-dynamic-threat-targets-during-b.md` — verdict: **SUPPORTS** ([source](https://www.pacom.mil/About-USINDOPACOM/PMTEC/Article/4478558/))
  > _"It has created and is constantly enhancing the largest coalition range system in the world, linking geographically distributed ranges and training areas across the Indo-Pacific theater and beyond."_
  - Model note: The source explicitly states PMTEC has created 'the largest coalition range system in the world' linking 'geographically distributed ranges and training areas across the Indo-Pacific theater and beyond,' which directly supports all substantive elements of the claim, and the parenthetical note in the claim itself acknowledges the exact wording match and instructs use of the .mil wording.

### ⚑ FACT #10 §6  —  **PARTIAL**

**Claim:**
> Deloitte holds GSA OASIS delivery order **PIID `47QFCA25F0010`** (parent IDIQ `GS00Q14OADU113`, the OASIS Unrestricted Pool Professional Services Multiple Agency Contract) supporting USINDOPACOM with enterprise-wide professional services. Period start **2025-03-01**; current period end (Year 1) **2026-07-31**; place of performance **Hawaii** (Camp H.M. Smith). Obligated to date: **$58,923,548** [s…

**Citations:** [s.2026-05-11-indopacom-alpha-deloitte]

**Sources checked:**
- `[s.2026-05-11-indopacom-alpha-deloitte]` → `01_sources/2026-05-11_usaspending-gov_indopacom-alpha-deloitte.md` — verdict: **PARTIAL** ([source](https://www.usaspending.gov/award/CONT_AWD_47QFCA25F0010_4732_GS00Q14OADU113_4732/))
  > _"PIID: 47QFCA25F0010 ... Parent IDIQ (vehicle): PIID: GS00Q14OADU113 ... Description: 'ONE ACQUISITION SOLUTION FOR INTEGRATED SERVICES (OASIS) PROFESSIONAL SERVICES MULTIPLE AGENCY CONTRACT' ... Recipient Name: DELOITTE CONSULTING LLP ... Total obligation to date: $58,923,548 ... Place of performance: Hawaii (state code HI) ... Period start: 2025-03-01 ... Period current end (Year 1): 2026-07-31"_
  - Missing in this source: The claim states the parent IDIQ is specifically 'the OASIS Unrestricted Pool Professional Services Multiple Agency Contract' — the source confirms OASIS but labels the parent IDIQ type as 'INDEFINITE DELIVERY / REQUIREMENTS, MULTIPLE AWARD' and notes 'Vehicle: GSA OASIS (Unrestricted Pool)' in an analyst-added field rather than a direct USAspending API quote, so this is partially inferential. More critically, the claim specifies place of performance as 'Camp H.M. Smith' — the source confirms Hawaii but explicitly states 'city code not reported,' with Camp H.M. Smith noted only as analyst inference. These are minor gaps; all core elements (PIID, parent IDIQ PIID, awardee, vehicle type, customer, state-level place of performance, start date, current period end, and obligated amount) are directly supported.
  - Model note: The source explicitly corroborates all primary claim elements (PIID, parent IDIQ, awardee, OASIS vehicle, USINDOPACOM customer, Hawaii performance location, $58,923,548 obligation, 2025-03-01 start, and 2026-07-31 Year 1 end), but the specific city-level place of performance (Camp H.M. Smith) is inferred by the analyst rather than stated in the API data, warranting a PARTIAL finding.

### ⚑ FACT #11 §6  —  **PARTIAL**

**Claim:**
> PACAF Base Area Network modernization — $180M, 5-yr task order on AFBIM IDIQ awarded Sep 2025. Direct PACAF/INDOPACOM IT backbone with Zero Trust foundation [s.govconwire-sep2025-caci-afbim] [s.2026-05-12-caci-to-modernize-air-force-ba]. *Single-sourced — verify via USAspending (search Deloitte/CACI AFBIM 2025) and CACI IR.*

**Citations:** [s.govconwire-sep2025-caci-afbim] [s.2026-05-12-caci-to-modernize-air-force-ba]

**Sources checked:**
- `[s.govconwire-sep2025-caci-afbim]` → ⚠ not in `01_sources/` (cited only in §8.2)
- `[s.2026-05-12-caci-to-modernize-air-force-ba]` → `01_sources/2026-05-12_washingtonexec-com_caci-to-modernize-air-force-base-networks-in-pacific-under-1.md` — verdict: **PARTIAL** ([source](https://washingtonexec.com/2025/09/caci-to-modernize-air-force-base-networks-in-pacific-under-180m-task-order/))
  > _"CACI International has received a 5-year task order worth up to $180 million to provide secure and stable network operations for Pacific Air Forces in support of U.S. Indo-Pacific Command."_
  - Missing in this source: The claim states the award was on the 'AFBIM IDIQ' and awarded 'Sep 2025' — the source confirms Sep 2025 publication but does not explicitly state the award date or confirm it is an IDIQ vehicle. The claim also references 'Deloitte' as a potential awardee to verify against, which is not mentioned in the source. The source does not explicitly confirm the contract is 'single-sourced' or provide USAspending/CACI IR verification.
  - Model note: The source supports the core elements ($180M, 5-year task order, PACAF/INDOPACOM IT backbone, Zero Trust foundation, Base Area Network modernization under Base Infrastructure Modernization contract) but does not explicitly confirm the IDIQ vehicle name, the precise award date, or address the single-source verification caveat.

### ⚑ FACT #12 §6  —  **PARTIAL**

**Claim:**
> Spectral (NAVWAR) — $1.2B ceiling, shipboard SIGINT/EW/IO. $143M Spectral Enabling Kits delivery order May 2025 [s.bizwire-may2025-spectral] [s.2026-05-12-caci-mission-critical-technolo]. *Single-sourced — verify via CACI IR.*

**Citations:** [s.bizwire-may2025-spectral] [s.2026-05-12-caci-mission-critical-technolo]

**Sources checked:**
- `[s.bizwire-may2025-spectral]` → ⚠ not in `01_sources/` (cited only in §8.2)
- `[s.2026-05-12-caci-mission-critical-technolo]` → `01_sources/2026-05-12_businesswire-com_caci-mission-critical-technology-will-accelerate-delivery-of.md` — verdict: **PARTIAL** ([source](https://www.businesswire.com/news/home/20250507187909/en/CACIs-Mission-Critical-Technology-will-Accelerate-the-Delivery-of-Electronic-Warfighting-Capabilities-to-the-U.S.-Navys-Existing-Fleet))
  > _"The $143 million firm-fixed-price delivery order represents a new phase of work on the CACI's existing Spectral contract with the Naval Information Warfare Systems Command (NAVWAR) which is authorized with a $1.2 billion ceiling value."_
  - Missing in this source: The claim states the delivery order was awarded 'May 2025'; the source article is published on businesswire dated 20250507 (May 7, 2025) but no explicit date for the delivery order itself is stated in the extracted text. Additionally, the 'Single-sourced — verify via CACI IR' notation is an editorial flag not verifiable from the source. The publication date field in the metadata is blank, though the URL timestamp and capture date support a May 2025 timeframe.
  - Model note: The source explicitly confirms the $1.2B ceiling, NAVWAR, shipboard SIGINT/EW/IO mission, and $143M delivery order for Spectral Enabling Kits; the May 2025 date is strongly implied by the URL timestamp (20250507) but not explicitly stated as the award date within the article text, and the single-source verification flag is an internal editorial note not addressed by the source.

### ✓ FACT #13 §6  —  **SUPPORTS**

**Claim:**
> Trojan EATS (Army DEVCOM, OASIS) — $382M, 5-yr; SIGINT/EW open-architecture systems [s.caci-ir-trojan-2024] [s.2026-05-12-u-s-army-selects-caci-for-382-].

**Citations:** [s.caci-ir-trojan-2024] [s.2026-05-12-u-s-army-selects-caci-for-382-]

**Sources checked:**
- `[s.caci-ir-trojan-2024]` → ⚠ not in `01_sources/` (cited only in §8.2)
- `[s.2026-05-12-u-s-army-selects-caci-for-382-]` → `01_sources/2026-05-12_businesswire-com_u-s-army-selects-caci-for-382-million-signals-intelligence-a.md` — verdict: **SUPPORTS** ([source](https://www.businesswire.com/news/home/20240123940984/en/U.S.-Army-Selects-CACI-for-%24382-Million-Signals-Intelligence-and-Electronic-Warfare-Systems-Task-Order))
  > _"CACI International Inc (NYSE: CACI) announced today that it won a five-year, single-award task order valued at up to $382 million to provide technology to the U.S. Army Combat Capabilities Development Command (DEVCOM) Engineering and Systems Integration Directorate (ESID) Trojan Engineering and Systems Integration (ESI) Advancement of Trojan Systems (EATS). This work is part of the One Acquisition…"_
  - Model note: The source explicitly confirms all elements of the claim: Trojan EATS program, Army DEVCOM, OASIS contract vehicle, $382M value, 5-year duration, and SIGINT/EW open-architecture systems focus.

### ⚑ FACT #14 §6  —  **PARTIAL**

**Claim:**
> ARKA acquisition closed March 2026 ($2.6B) — adds satellite sensors + agentic AI for SIGINT/EW [s.caci-ir-arka-2026] [s.2026-05-12-caci-completes-acquisition-of-] [s.2026-05-12-caci-q3-fy2026-earnings-call-t] [s.2026-05-12-caci-8-k-arka-agreement] [s.2026-05-12-caci-international-form-10-q-q].

**Citations:** [s.caci-ir-arka-2026] [s.2026-05-12-caci-completes-acquisition-of-] [s.2026-05-12-caci-q3-fy2026-earnings-call-t] [s.2026-05-12-caci-8-k-arka-agreement] [s.2026-05-12-caci-international-form-10-q-q]

**Sources checked:**
- `[s.caci-ir-arka-2026]` → ⚠ not in `01_sources/` (cited only in §8.2)
- `[s.2026-05-12-caci-completes-acquisition-of-]` → `01_sources/2026-05-12_nasdaq-com_caci-completes-acquisition-of-arka-group-2-6b-close-2026-03.md` — verdict: **PARTIAL** ([source](https://www.nasdaq.com/press-release/caci-completes-acquisition-arka-group-2026-03-09))
- `[s.2026-05-12-caci-q3-fy2026-earnings-call-t]` → `01_sources/2026-05-12_fool-com_caci-q3-fy2026-earnings-call-transcript-april-23-2026-motley.md` — verdict: **PARTIAL** ([source](https://www.fool.com/earnings/call-transcripts/2026/04/23/caci-caci-q3-2026-earnings-call-transcript/))
- `[s.2026-05-12-caci-8-k-arka-agreement]` → `01_sources/2026-05-12_sec-gov_caci-8-k-definitive-agreement-to-acquire-arka-group-dec-22-2.md` — verdict: **DOES_NOT_SUPPORT** ([source](https://www.sec.gov/Archives/edgar/data/16058/000162828025059047/caci-20251219.htm))
- `[s.2026-05-12-caci-international-form-10-q-q]` → `01_sources/2026-05-12_sec-gov_caci-international-form-10-q-quarterly-report-for-q3-fy2026.md` — verdict: **PARTIAL** ([source](https://www.sec.gov/Archives/edgar/data/16058/000162828026026802/caci-20260331.htm))
  > _"CACI International Inc (NYSE: CACI) announced today that it has completed its acquisition of ARKA Group L.P. (ARKA) in an all-cash transaction for $2.6 billion. ARKA provides industry-leading electro-optical/infrared (EO/IR) and hyperspectral imaging capabilities, and Agentic AI-based software, that deliver robust geospatial intelligence for critical national security missions."_
  - Missing in this source: The claim states ARKA adds capabilities for 'SIGINT/EW' (Signals Intelligence / Electronic Warfare). The source mentions ARKA adds space-based sensors (EO/IR and hyperspectral imaging) and Agentic AI, and notes these complement CACI's existing SIGINT position, but does not attribute SIGINT or EW capabilities directly to ARKA itself.
  - Model note: The source supports the acquisition closing date (March 9, 2026), the $2.6B price, satellite/space-based sensors, and agentic AI, but the SIGINT/EW attribution is described as CACI's pre-existing capability that ARKA's geospatial intelligence complements, not a capability ARKA itself adds.
  > _"During the third quarter, we closed the acquisition of ARKA, a leading technology company focused on national security missions in the space domain. ARKA brings exquisite space-based imaging sensor technology with high technical barriers to entry, agentic AI-based ground processing software, and deep customer relationships built over decades of strong performance."_
  - Missing in this source: The claim states the acquisition closed in 'March 2026' at '$2.6B'. The source confirms the acquisition closed 'during the third quarter' (Q3 FY2026, which based on context appears to include the period around April 2026) but does not specify March 2026 as the closing month, nor does it state the acquisition price of $2.6B anywhere in the transcript. The source also describes 'space-based imaging sensor technology' rather than broadly 'satellite sensors,' and does not specifically mention SIGINT in connection with ARKA (SIGINT is mentioned separately in relation to the SPECTRAL program).
  - Model note: The source supports the acquisition closing in Q3 FY2026 and adding space-based imaging sensors and agentic AI, but does not confirm the specific closing month of March 2026, the $2.6B price tag, or explicitly linking ARKA's capabilities to SIGINT/EW (those are associated with SPECTRAL, not ARKA).
  - Missing in this source: The source contains no mention of ARKA Group, no acquisition closing date of March 2026, no $2.6B acquisition price, no satellite sensors, and no agentic AI for SIGINT/EW. The document is solely about an amendment to a Master Accounts Receivable Purchase Agreement.
  - Model note: Despite the metadata labeling this as 'CACI 8-K — Definitive Agreement to Acquire ARKA Group (Dec 22, 2025, $2.6B)', the actual extracted source content discusses only an amendment to a receivables purchase agreement with MUFG Bank and contains no information whatsoever about an ARKA acquisition, its closing date, price, or capabilities.
  > _"On March 9, 2026, CACI acquired all of the equity interests of ARKA Group L.P. (ARKA) for purchase consideration of approximately $2,642.7 million, net of cash acquired, subject to post closing adjustments. This acquisition will enhance CACI's ability to deliver advanced technology for its national security customers in the space domain."_
  - Missing in this source: The source confirms the acquisition closed in March 2026 at approximately $2.6B (close enough rounding), but does not mention 'satellite sensors,' 'agentic AI,' 'SIGINT,' or 'EW (Electronic Warfare)' as specific capabilities added. The source only references 'advanced technology for national security customers in the space domain.'
  - Model note: The date and dollar amount of the ARKA acquisition are supported, but the specific capability descriptors (satellite sensors, agentic AI, SIGINT/EW) are not mentioned anywhere in the source text.


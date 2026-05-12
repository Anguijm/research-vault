# FACT Verification Report — PMTEC-USINDOPACOM

*Generated 2026-05-12T11:08:54 by `verify_facts.py` (model: `claude-sonnet-4-6`)*

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
  - Missing in this source: 1) The claim attributes item 5 (AI/digital-twin) to Swendsen for the AI need AND to Stridiron for the APL (Johns Hopkins APL) partnership — the source says Stridiron announced the Johns Hopkins partnership and Swendsen mentioned AI strategy support, but the source does not use the term 'APL' or explicitly link the partnership to Johns Hopkins APL specifically, only to 'Johns Hopkins University.' 2) The claim states Cobra Gold 2026 'surfaced' the realistic-targets need — the source says Bednarcik discussed Cobra Gold 2026 and identified a need for realistic targets, but does not explicitly say the gap was surfaced via that exercise. 3) The claim references a 'PMTEC quarterly industry meeting' and a specific date of '13 March 2026' — the source confirms a quarterly industry meeting but does not state the date. 4) The claim frames all eight items as 'technology priorities' formally named at the event; the source enumerates only four explicit 'technology priorities' and presents items 5–8 in narrative form, not as a formal enumerated list of priorities. 5) The source does not use the phrase 'Department of War' — it says 'Department of War's AI strategy' per the claim but the source reads 'Department of War's AI strategy' which matches, though this appears to be a non-standard department name not verified here.
  - Model note: The source supports the substance of all eight items and the named individuals, but the claim's framing of all eight as formally enumerated 'technology priorities,' the specific event date of 13 March 2026, and the 'APL' specification for the Johns Hopkins partnership are not explicitly present in the source text.

### ⚑ FACT #2 §3  —  **PARTIAL**

**Claim:**
> FY26 PDI request: **$10.0B** (Grand Total $10,004,542 thousand per primary source — the FY26 PDI budget book). FY25 baseline appears to be ~$9.4B (Grand Total column 2 in the same book). PMTEC is a named line item across multiple PB sub-accounts [s.2026-fy26-comptroller] [s.2026-05-12-fy2026-pacific-deterrence-init]. *Correction 2026-05-12: planning-conversation figure was "$9.9B" — primary source…

**Citations:** [s.2026-fy26-comptroller] [s.2026-05-12-fy2026-pacific-deterrence-init]

**Sources checked:**
- `[s.2026-fy26-comptroller]` → ⚠ not in `01_sources/` (cited only in §8.2)
- `[s.2026-05-12-fy2026-pacific-deterrence-init]` → `01_sources/2026-05-12_comptroller-war-gov_fy2026-pacific-deterrence-initiative.md` — verdict: **PARTIAL** ([source](https://comptroller.war.gov/Portals/45/Documents/defbudget/FY2026/FY2026_Pacific_Deterrence_Initiative.pdf))
  > _"The DoD is focused on maintaining and extending our military advantage in the region, paced to threats posed by China. The FY 2026 PDI request is $10.0 billion; these investments and activities demonstrate U.S. commitment to deterring China. ... Grand Total 7,842,993 2,161,549 10,004,542"_
  - Missing in this source: The claim references an FY25 baseline of ~$9.4B (described as 'Grand Total column 2 in the same book'), but the source content provided contains no FY25 comparison column or FY25 figures. The claim also states 'PMTEC is a named line item across multiple PB sub-accounts,' but no mention of 'PMTEC' appears anywhere in the extracted source content.
  - Model note: The source explicitly supports the FY26 PDI request of $10.0B ($10,004,542 thousand grand total), but does not contain FY25 baseline figures or any reference to 'PMTEC' as a named line item.

### ✗ FACT #3 §3  —  **DOES_NOT_SUPPORT**

**Claim:**
> The FY26 PDI book funds PMTEC across three service components within the "Exercises, Training, Experimentation, and Innovation" PDI category [s.2026-05-12-fy2026-pacific-deterrence-init]: - **Department of the Army ($851M total)** — Operation & Maintenance funds *"rotations at the Joint Pacific Multinational Readiness Training Center (JPMRC) and the Pacific Multi-Domain Training and Experimentatio…

**Citations:** [s.2026-05-12-fy2026-pacific-deterrence-init]

**Sources checked:**
- `[s.2026-05-12-fy2026-pacific-deterrence-init]` → `01_sources/2026-05-12_comptroller-war-gov_fy2026-pacific-deterrence-initiative.md` — verdict: **DOES_NOT_SUPPORT** ([source](https://comptroller.war.gov/Portals/45/Documents/defbudget/FY2026/FY2026_Pacific_Deterrence_Initiative.pdf))
  - Missing in this source: All specific PMTEC-related claims: Army $851M total with JPMRC/PMTEC O&M description, Navy $588M total with PMTEC studies/live-fire/JFDD/JDECC description, Air Force $752M total with standalone PMTEC Operations sub-category and 0207429F Combat Training Ranges at $147.2M, Joint Staff $310M slice covering JTEEP and Theater Forces, and the correction note about funding distribution — none of these appear in the extracted source content.
  - Model note: The provided source content covers only Pages 1–18 of the PDI document (through the beginning of the Logistics section), and does not contain the 'Exercises, Training, Experimentation, and Innovation' section (which begins on page 19 per the Table of Contents) where PMTEC funding details would appear; therefore none of the specific dollar figures, descriptions, or program element numbers cited in the claim can be verified from the extracted content.

### ⚑ FACT #4 §3  —  **PARTIAL**

**Claim:**
> PMTEC runs a Quarterly Commercial Industry Update (most recent: 13 March 2026, Honolulu, hosted with Defense Innovation OnRamp Hub: Hawaii) [s.2026-04-22-pacom] [s.2026-05-12-usindopacom-seeks-industry-par].

**Citations:** [s.2026-04-22-pacom] [s.2026-05-12-usindopacom-seeks-industry-par]

**Sources checked:**
- `[s.2026-04-22-pacom]` → ⚠ not in `01_sources/` (cited only in §8.2)
- `[s.2026-05-12-usindopacom-seeks-industry-par]` → `01_sources/2026-05-12_pacom-mil_usindopacom-seeks-industry-partners-to-address-modern-milita.md` — verdict: **PARTIAL** ([source](https://www.pacom.mil/About-USINDOPACOM/PMTEC/Article/4467480/usindopacom-seeks-industry-partners-to-address-modern-military-challenges/))
  > _"The event, hosted by USINDOPACOM J7 Pacific Multi-Domain Training and Experimentation Capability (PMTEC) and the Defense Innovation OnRamp Hub: Hawaii, a program of the Defense Innovation Unit, connected military leaders with industry representatives to outline a path toward a more integrated, all-domain training and operations ecosystem in the region."_
  - Missing in this source: The source confirms PMTEC hosts quarterly industry meetings and the co-host (Defense Innovation OnRamp Hub: Hawaii), but does not specify the date '13 March 2026' or the location 'Honolulu' for the most recent event. The claim also uses the specific title 'Quarterly Commercial Industry Update' which does not appear verbatim in the source (the source refers to 'PMTEC's quarterly industry meeting').
  - Model note: The source supports the existence of a quarterly industry meeting co-hosted with Defense Innovation OnRamp Hub: Hawaii, but does not confirm the specific date of 13 March 2026, the location of Honolulu, or the precise title 'Quarterly Commercial Industry Update.'

### ✓ FACT #5 §3  —  **SUPPORTS**

**Claim:**
> Formal industry intake channel: pacom.mil/Contact/Industry-Engagements/ [s.2026-04-22-pacom] [s.2026-05-12-usindopacom-seeks-industry-par].

**Citations:** [s.2026-04-22-pacom] [s.2026-05-12-usindopacom-seeks-industry-par]

**Sources checked:**
- `[s.2026-04-22-pacom]` → ⚠ not in `01_sources/` (cited only in §8.2)
- `[s.2026-05-12-usindopacom-seeks-industry-par]` → `01_sources/2026-05-12_pacom-mil_usindopacom-seeks-industry-partners-to-address-modern-milita.md` — verdict: **SUPPORTS** ([source](https://www.pacom.mil/About-USINDOPACOM/PMTEC/Article/4467480/usindopacom-seeks-industry-partners-to-address-modern-military-challenges/))
  > _"He directed potential partners to the command's online portal at https://www.pacom.mil/Contact/Industry-Engagements/"_
  - Model note: The source explicitly identifies https://www.pacom.mil/Contact/Industry-Engagements/ as the formal industry intake channel, matching the claim exactly.

### ⚑ FACT #6 §3  —  **PARTIAL**

**Claim:**
> Maj. Tuan Nguyen (J83 Joint Validation Division) is the formal industry intake POC [s.2026-04-22-pacom] [s.2026-05-12-usindopacom-seeks-industry-par].

**Citations:** [s.2026-04-22-pacom] [s.2026-05-12-usindopacom-seeks-industry-par]

**Sources checked:**
- `[s.2026-04-22-pacom]` → ⚠ not in `01_sources/` (cited only in §8.2)
- `[s.2026-05-12-usindopacom-seeks-industry-par]` → `01_sources/2026-05-12_pacom-mil_usindopacom-seeks-industry-partners-to-address-modern-milita.md` — verdict: **PARTIAL** ([source](https://www.pacom.mil/About-USINDOPACOM/PMTEC/Article/4467480/usindopacom-seeks-industry-partners-to-address-modern-military-challenges/))
  > _"Maj. Tuan Nguyen, who represents industry engagement for the J83 Joint Validation Division, provided guidance for companies interested in working with USINDOPACOM. He directed potential partners to the command's online portal at https://www.pacom.mil/Contact/Industry-Engagements/ and emphasized the importance of understanding military requirements before submitting proposals."_
  - Missing in this source: The source does not describe Maj. Nguyen as the 'formal industry intake POC'; it describes him as representing 'industry engagement for the J83 Joint Validation Division' and directing companies to an online portal, but the article also names Brent Parker as the 'PMTEC Industry Engagement Lead' with a direct contact email, suggesting shared or divided POC responsibilities.
  - Model note: The source confirms Maj. Nguyen's name, rank, and J83 Joint Validation Division affiliation and his role in providing industry intake guidance, but does not use the term 'formal industry intake POC,' and the presence of Brent Parker as a named contact with an email address complicates an exclusive POC designation for Nguyen.

### ⚑ FACT #7 §3  —  **PARTIAL**

**Claim:**
> Brent Parker (PMTEC Commercial Industry Engagement Lead, contractor) is the working-level POC; email brent.m.parker2.ctr@us.navy.mil [s.2026-04-22-pacom] [s.2026-05-12-usindopacom-seeks-industry-par]. *Role title and identity confirmed via ingested [s.2026-05-11-driving-readiness-indopacom-j7] which names him "PMTEC Industry Engagement Lead" moderating the POST 2026 panel. The .ctr email is single…

**Citations:** [s.2026-04-22-pacom] [s.2026-05-12-usindopacom-seeks-industry-par] [s.2026-05-11-driving-readiness-indopacom-j7]

**Sources checked:**
- `[s.2026-04-22-pacom]` → ⚠ not in `01_sources/` (cited only in §8.2)
- `[s.2026-05-12-usindopacom-seeks-industry-par]` → `01_sources/2026-05-12_pacom-mil_usindopacom-seeks-industry-partners-to-address-modern-milita.md` — verdict: **PARTIAL** ([source](https://www.pacom.mil/About-USINDOPACOM/PMTEC/Article/4467480/usindopacom-seeks-industry-partners-to-address-modern-military-challenges/))
- `[s.2026-05-11-driving-readiness-indopacom-j7]` → `01_sources/2026-05-11_dvidshub-net_driving-readiness-indopacom-j7-outlines-all-domain-training.md` — verdict: **PARTIAL** ([source](https://www.dvidshub.net/news/561976/driving-readiness-indopacom-j7-outlines-all-domain-training-strategy-post-2026))
  > _""For companies with relevant capabilities, PMTEC offers an opportunity to contribute to defense preparedness while testing and refining their technologies in operational environments," said PMTEC Industry Engagement Lead, Brent Parker. For more information on PMTEC Industry Engagement events and activities, contact Brent Parker at brent.m.parker2.ctr@us.navy.mil"_
  - Missing in this source: The claim states his title is 'PMTEC Commercial Industry Engagement Lead' and that he is a contractor; the source only says 'PMTEC Industry Engagement Lead' (no 'Commercial' prefix). The claim also references confirmation via a separately 'ingested' source naming him moderator of a 'POST 2026 panel' — that ingested source is not the pacom.mil article provided here and cannot be evaluated. The contractor (.ctr) status is implied by the .ctr email suffix but not explicitly stated in the source text.
  - Model note: The source directly confirms Brent Parker's name, the title 'PMTEC Industry Engagement Lead' (not 'Commercial Industry Engagement Lead'), and the exact email address, but does not explicitly confirm contractor status or the 'Commercial' qualifier in his title, and the panel-moderator reference cannot be verified from this source alone.
  > _"The panel, moderated by PMTEC Industry Engagement Lead Brent Parker"_
  - Missing in this source: The email address brent.m.parker2.ctr@us.navy.mil and the contractor (.ctr) designation are not present in this source. The claim's note that the role title was confirmed via 'ingested' source is accurate, but the email is explicitly flagged as single-sourced to an un-ingested pacom.mil article, which is not this source.
  - Model note: The source confirms Brent Parker's name and role title ('PMTEC Industry Engagement Lead') moderating the POST 2026 panel, but does not contain any email address or contractor designation, leaving those elements unsupported by this source.

### ⚑ FACT #8 §4  —  **PARTIAL**

**Claim:**
> PMTEC was established in 2022 by USINDOPACOM J7 [s.2026-04-22-pacom] [s.2026-05-12-usindopacom-seeks-industry-par]. *Corroborated by ingested primary source [s.2026-05-11-multinational-forces-destroy-d] (pacom.mil PMTEC Article 4478558), which states: "About PMTEC: Established in 2022, the Pacific Multi-Domain Training and Experimentation Capability is a transformative enterprise funded and resour…

**Citations:** [s.2026-04-22-pacom] [s.2026-05-12-usindopacom-seeks-industry-par] [s.2026-05-11-multinational-forces-destroy-d]

**Sources checked:**
- `[s.2026-04-22-pacom]` → ⚠ not in `01_sources/` (cited only in §8.2)
- `[s.2026-05-12-usindopacom-seeks-industry-par]` → `01_sources/2026-05-12_pacom-mil_usindopacom-seeks-industry-partners-to-address-modern-milita.md` — verdict: **PARTIAL** ([source](https://www.pacom.mil/About-USINDOPACOM/PMTEC/Article/4467480/usindopacom-seeks-industry-partners-to-address-modern-military-challenges/))
- `[s.2026-05-11-multinational-forces-destroy-d]` → `01_sources/2026-05-11_pacom-mil_multinational-forces-destroy-dynamic-threat-targets-during-b.md` — verdict: **PARTIAL** ([source](https://www.pacom.mil/About-USINDOPACOM/PMTEC/Article/4478558/))
  > _"About PMTEC: Established in 2022, the Pacific Multi-Domain Training and Experimentation Capability is a transformative enterprise funded and resourced by the United States Indo-Pacific Command..."_
  - Missing in this source: The claim states PMTEC was established 'by USINDOPACOM J7,' but the source states it was 'funded and resourced by the United States Indo-Pacific Command' (not specifically J7). The source describes J7 as hosting events and overseeing PMTEC, but does not state J7 established it.
  - Model note: The source confirms PMTEC was established in 2022 and is funded/resourced by USINDOPACOM, but attributes establishment to USINDOPACOM broadly rather than specifically to USINDOPACOM J7 as the claim asserts.
  > _"About PMTEC: Established in 2022, the Pacific Multi-Domain Training and Experimentation Capability is a transformative enterprise funded and resourced by the United States Indo-Pacific Command"_
  - Missing in this source: The claim states PMTEC was established 'by USINDOPACOM J7'; the source states it was 'funded and resourced by the United States Indo-Pacific Command' but does not specify J7 as the establishing entity. The source separately references 'U.S. Indo-Pacific Command J7 Pacific Multi-Domain Training and Experimentation Capability' in an operational context, but does not explicitly attribute the establishment of PMTEC to J7.
  - Model note: The source confirms PMTEC was established in 2022 and is associated with USINDOPACOM, but does not explicitly state it was established 'by USINDOPACOM J7' — J7 is mentioned only as an operational supporting element, not as the founding authority.

### ✓ FACT #9 §4  —  **SUPPORTS**

**Claim:**
> PMTEC integrates geographically distributed ranges and training areas across the Indo-Pacific — described by program leadership as the world's largest coalition range system [s.2026-04-03-dvids-post]. *Corroborated by ingested primary source [s.2026-05-11-multinational-forces-destroy-d] (pacom.mil PMTEC Article 4478558): "It has created and is constantly enhancing the largest coalition range syste…

**Citations:** [s.2026-04-03-dvids-post] [s.2026-05-11-multinational-forces-destroy-d]

**Sources checked:**
- `[s.2026-04-03-dvids-post]` → ⚠ not in `01_sources/` (cited only in §8.2)
- `[s.2026-05-11-multinational-forces-destroy-d]` → `01_sources/2026-05-11_pacom-mil_multinational-forces-destroy-dynamic-threat-targets-during-b.md` — verdict: **SUPPORTS** ([source](https://www.pacom.mil/About-USINDOPACOM/PMTEC/Article/4478558/))
  > _"It has created and is constantly enhancing the largest coalition range system in the world, linking geographically distributed ranges and training areas across the Indo-Pacific theater and beyond."_
  - Model note: The source explicitly states PMTEC has created 'the largest coalition range system in the world' by 'linking geographically distributed ranges and training areas across the Indo-Pacific theater and beyond,' which directly supports all elements of the claim, including the note about correct wording (no 'fully instrumented' modifier).

### ⚑ FACT #10 §6  —  **PARTIAL**

**Claim:**
> Deloitte holds GSA OASIS delivery order **PIID `47QFCA25F0010`** (parent IDIQ `GS00Q14OADU113`, the OASIS Unrestricted Pool Professional Services Multiple Agency Contract) supporting USINDOPACOM with enterprise-wide professional services. Period start **2025-03-01**; current period end (Year 1) **2026-07-31**; place of performance **Hawaii** (Camp H.M. Smith). Obligated to date: **$58,923,548** [s…

**Citations:** [s.2026-05-11-indopacom-alpha-deloitte]

**Sources checked:**
- `[s.2026-05-11-indopacom-alpha-deloitte]` → `01_sources/2026-05-11_usaspending-gov_indopacom-alpha-deloitte.md` — verdict: **PARTIAL** ([source](https://www.usaspending.gov/award/CONT_AWD_47QFCA25F0010_4732_GS00Q14OADU113_4732/))
  > _"PIID: 47QFCA25F0010 ... Parent IDIQ (vehicle): GS00Q14OADU113 ... Description: ONE ACQUISITION SOLUTION FOR INTEGRATED SERVICES (OASIS) PROFESSIONAL SERVICES MULTIPLE AGENCY CONTRACT ... Recipient Name: DELOITTE CONSULTING LLP ... Place of performance: Hawaii (state code HI) ... Period start: 2025-03-01 ... Period current end (Year 1): 2026-07-31 ... Total obligation to date: $58,923,548"_
  - Missing in this source: The source does not confirm 'Camp H.M. Smith' as the specific place of performance (only 'Hawaii' is stated; city code not reported). The source also explicitly notes that 'base_and_all_options_value' is null, meaning the parent IDIQ description as 'OASIS Unrestricted Pool Professional Services Multiple Award Contract' is supported but the characterization of it as a 'Multiple Agency Contract' is a paraphrase of the source's 'MULTIPLE AWARD' designation. All core elements (PIID, parent IDIQ PIID, awardee, vehicle, customer, place of performance as Hawaii, start date, current period end, and obligated amount) are directly supported; the only minor gap is Camp H.M. Smith specificity.
  - Model note: The source explicitly supports all primary claim elements (PIID, parent IDIQ, Deloitte as awardee, OASIS vehicle, USINDOPACOM customer, Hawaii as place of performance, 2025-03-01 start date, 2026-07-31 current period end, and $58,923,548 obligated), but does not confirm the specific sub-location of Camp H.M. Smith, making the claim very nearly fully supported with only that minor geographic specificity unverified.

### ⚑ FACT #11 §6  —  **PARTIAL**

**Claim:**
> PACAF Base Area Network modernization — $180M, 5-yr task order on AFBIM IDIQ awarded Sep 2025. Direct PACAF/INDOPACOM IT backbone with Zero Trust foundation [s.govconwire-sep2025-caci-afbim] [s.2026-05-12-caci-to-modernize-air-force-ba]. *Single-sourced — verify via USAspending (search Deloitte/CACI AFBIM 2025) and CACI IR.*

**Citations:** [s.govconwire-sep2025-caci-afbim] [s.2026-05-12-caci-to-modernize-air-force-ba]

**Sources checked:**
- `[s.govconwire-sep2025-caci-afbim]` → ⚠ not in `01_sources/` (cited only in §8.2)
- `[s.2026-05-12-caci-to-modernize-air-force-ba]` → `01_sources/2026-05-12_washingtonexec-com_caci-to-modernize-air-force-base-networks-in-pacific-under-1.md` — verdict: **PARTIAL** ([source](https://washingtonexec.com/2025/09/caci-to-modernize-air-force-base-networks-in-pacific-under-180m-task-order/))
  > _"CACI International has received a 5-year task order worth up to $180 million to provide secure and stable network operations for Pacific Air Forces in support of U.S. Indo-Pacific Command."_
  - Missing in this source: The claim states the task order was awarded 'Sep 2025' — the source is dated 2025-09-17 which supports this, but the claim also references 'AFBIM IDIQ' as the vehicle name and states it was 'single-sourced'; the source does not explicitly confirm single-source justification or name the specific IDIQ vehicle as 'AFBIM IDIQ'. Additionally, the claim mentions 'Deloitte/CACI AFBIM 2025' for verification purposes, implying Deloitte involvement, which is not mentioned in the source.
  - Model note: The source supports the core facts ($180M, 5-year task order, PACAF/INDOPACOM IT backbone, Zero Trust foundation, CACI, Base Area Network/Base Infrastructure Modernization contract, September 2025), but does not confirm single-source award justification, the specific IDIQ vehicle name, or any Deloitte involvement.

### ⚑ FACT #12 §6  —  **PARTIAL**

**Claim:**
> Spectral (NAVWAR) — $1.2B ceiling, shipboard SIGINT/EW/IO. $143M Spectral Enabling Kits delivery order May 2025 [s.bizwire-may2025-spectral] [s.2026-05-12-caci-mission-critical-technolo]. *Single-sourced — verify via CACI IR.*

**Citations:** [s.bizwire-may2025-spectral] [s.2026-05-12-caci-mission-critical-technolo]

**Sources checked:**
- `[s.bizwire-may2025-spectral]` → ⚠ not in `01_sources/` (cited only in §8.2)
- `[s.2026-05-12-caci-mission-critical-technolo]` → `01_sources/2026-05-12_businesswire-com_caci-mission-critical-technology-will-accelerate-delivery-of.md` — verdict: **PARTIAL** ([source](https://www.businesswire.com/news/home/20250507187909/en/CACIs-Mission-Critical-Technology-will-Accelerate-the-Delivery-of-Electronic-Warfighting-Capabilities-to-the-U.S.-Navys-Existing-Fleet))
  > _"The $143 million firm-fixed-price delivery order represents a new phase of work on the CACI's existing Spectral contract with the Naval Information Warfare Systems Command (NAVWAR) which is authorized with a $1.2 billion ceiling value."_
  - Missing in this source: The claim states the delivery order was awarded in 'May 2025'; the source article URL contains '20250507' suggesting a May 7, 2025 publication date but the publication_date field is blank, so the date cannot be formally confirmed from the source metadata. Additionally, the claim notes 'Single-sourced — verify via CACI IR,' which is an editorial annotation not verifiable from this source. The claim describes Spectral as 'shipboard SIGINT/EW/IO' which is supported, but the exact phrase used in the source is 'shipboard signals intelligence (SIGINT), electronic warfare (EW), and information operations (IO) weapon system.'
  - Model note: The source explicitly supports the $1.2B ceiling, NAVWAR contracting authority, $143M delivery order, and shipboard SIGINT/EW/IO mission description; the only gap is the formal confirmation of the May 2025 date from source metadata (though the URL strongly implies it) and the editorial 'single-sourced' notation which is unverifiable from this source alone.

### ✓ FACT #13 §6  —  **SUPPORTS**

**Claim:**
> Trojan EATS (Army DEVCOM, OASIS) — $382M, 5-yr; SIGINT/EW open-architecture systems [s.caci-ir-trojan-2024] [s.2026-05-12-u-s-army-selects-caci-for-382-].

**Citations:** [s.caci-ir-trojan-2024] [s.2026-05-12-u-s-army-selects-caci-for-382-]

**Sources checked:**
- `[s.caci-ir-trojan-2024]` → ⚠ not in `01_sources/` (cited only in §8.2)
- `[s.2026-05-12-u-s-army-selects-caci-for-382-]` → `01_sources/2026-05-12_businesswire-com_u-s-army-selects-caci-for-382-million-signals-intelligence-a.md` — verdict: **SUPPORTS** ([source](https://www.businesswire.com/news/home/20240123940984/en/U.S.-Army-Selects-CACI-for-%24382-Million-Signals-Intelligence-and-Electronic-Warfare-Systems-Task-Order))
  > _"CACI International Inc (NYSE: CACI) announced today that it won a five-year, single-award task order valued at up to $382 million to provide technology to the U.S. Army Combat Capabilities Development Command (DEVCOM) Engineering and Systems Integration Directorate (ESID) Trojan Engineering and Systems Integration (ESI) Advancement of Trojan Systems (EATS). This work is part of the One Acquisition…"_
  - Model note: The source explicitly confirms all elements of the claim: Trojan EATS program name, Army DEVCOM, OASIS contract vehicle, $382M value, 5-year duration, and SIGINT/EW open-architecture systems focus.

### ⚑ FACT #14 §6  —  **PARTIAL**

**Claim:**
> ARKA acquisition closed March 2026 ($2.6B) — adds satellite sensors + agentic AI for SIGINT/EW [s.caci-ir-arka-2026] [s.2026-05-12-caci-completes-acquisition-of-].

**Citations:** [s.caci-ir-arka-2026] [s.2026-05-12-caci-completes-acquisition-of-]

**Sources checked:**
- `[s.caci-ir-arka-2026]` → ⚠ not in `01_sources/` (cited only in §8.2)
- `[s.2026-05-12-caci-completes-acquisition-of-]` → `01_sources/2026-05-12_nasdaq-com_caci-completes-acquisition-of-arka-group-2-6b-close-2026-03.md` — verdict: **PARTIAL** ([source](https://www.nasdaq.com/press-release/caci-completes-acquisition-arka-group-2026-03-09))
  > _"CACI International Inc (NYSE: CACI) announced today that it has completed its acquisition of ARKA Group L.P. (ARKA) in an all-cash transaction for $2.6 billion. ARKA provides industry-leading electro-optical/infrared (EO/IR) and hyperspectral imaging capabilities, and Agentic AI-based software, that deliver robust geospatial intelligence for critical national security missions."_
  - Missing in this source: The claim states ARKA adds capabilities for 'SIGINT/EW' (signals intelligence / electronic warfare). The source mentions ARKA adds space-based sensors (EO/IR and hyperspectral imaging) and Agentic AI, and notes ARKA's geospatial intelligence 'complements CACI's strong position providing signals intelligence,' but does not explicitly state ARKA itself provides SIGINT or EW capabilities. The source describes ARKA's sensors as satellite/space-based rather than explicitly 'satellite sensors' in a SIGINT/EW context.
  - Model note: The source supports the $2.6B acquisition closing on 2026-03-09 and the addition of space-based sensors and agentic AI, but ARKA's capabilities are described as EO/IR hyperspectral imaging for geospatial intelligence rather than SIGINT/EW, making the SIGINT/EW characterization only indirectly supported at best.


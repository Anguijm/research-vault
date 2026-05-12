# FACT Verification Report — PMTEC-USINDOPACOM

*Generated 2026-05-12T20:29:24 by `verify_facts.py` (model: `claude-sonnet-4-6`)*

## Summary

- **21** FACT claims scanned
- **3** SUPPORTS — claim is corroborated by an ingested source
- **18** PARTIAL — some elements supported by an ingested source
- **0** DOES_NOT_SUPPORT — ingested source contradicts or omits the claim
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
  - Missing in this source: 1) The claim attributes item 5 (AI/digital-twin) to Mary Ann Swendsen for the AI need and Stridiron for the APL partnership — the source says Stridiron announced a Johns Hopkins University (not APL) partnership, and Swendsen discussed AI strategy needs, so 'APL' is not mentioned in the source at all; the source says 'Johns Hopkins University' not 'APL.' 2) The claim states the event was a 'quarterly industry meeting' — the source confirms this. 3) The claim references 'USINDOPACOM J7' hosting — supported. 4) The claim references 'eight gaps publicly named at the 13 March 2026 Quarterly Commercial Industry Update' in the verification note — the source does not mention the date '13 March 2026' or the literal framing of 'eight gaps.' 5) The claim's verification note itself acknowledges the event date and 'eight' framing are not in the ingested article, which is consistent with this finding.
  - Model note: The source supports items 1–4 (technology priorities) and items 6–8 (named personnel and details) closely, but the claim incorrectly attributes the Johns Hopkins partnership to 'APL' (Applied Physics Laboratory) when the source says only 'Johns Hopkins University,' and the precise event date (13 March 2026) and literal 'eight gaps' framing are absent from the source.

### ⚑ FACT #2 §3  —  **PARTIAL**

**Claim:**
> FY26 PDI request: **$10.0B** (Grand Total $10,004,542 thousand per primary source — the FY26 PDI budget book). FY25 baseline appears to be ~$9.4B (Grand Total column 2 in the same book). PMTEC is a named line item across multiple PB sub-accounts [s.2026-fy26-comptroller] [s.2026-05-12-fy2026-pacific-deterrence-init]. *Correction 2026-05-12: planning-conversation figure was "$9.9B" — primary source…

**Citations:** [s.2026-fy26-comptroller] [s.2026-05-12-fy2026-pacific-deterrence-init]

**Sources checked:**
- `[s.2026-fy26-comptroller]` → ⚠ not in `01_sources/` (cited only in §8.2)
- `[s.2026-05-12-fy2026-pacific-deterrence-init]` → `01_sources/2026-05-12_comptroller-war-gov_fy2026-pacific-deterrence-initiative.md` — verdict: **PARTIAL** ([source](https://comptroller.war.gov/Portals/45/Documents/defbudget/FY2026/FY2026_Pacific_Deterrence_Initiative.pdf))
  > _"Grand Total 7,842,993 2,161,549 10,004,542 ... Grand Total 8,614,459 9,410,580 10,004,542 ... The DoD is focused on maintaining and extending our military advantage in the region, paced to threats posed by China. The FY 2026 PDI request is $10.0 billion"_
  - Missing in this source: The claim states the FY25 baseline is ~$9.4B (described as 'Grand Total column 2 in the same book') — this IS supported ($9,410,580 thousand). The claim that PMTEC is 'a named line item across multiple PB sub-accounts' is only partially supported: PMTEC appears explicitly in Army and Navy/Air Force descriptions and Air Force funding tables, but is not confirmed as a named budget line item across 'multiple PB sub-accounts' in the strict sense — it appears as a program description reference rather than a discrete named line item in all tables. The '$9.9B' correction note is editorial and not verifiable from source.
  - Model note: The source fully supports the FY26 Grand Total of $10,004,542 thousand (~$10.0B) and FY25 of $9,410,580 thousand (~$9.4B), and confirms PMTEC is referenced across Army, Navy, and Air Force sections, but PMTEC appears more as a program description than a discrete named budget line item across multiple sub-accounts.

### ⚑ FACT #3 §3  —  **PARTIAL**

**Claim:**
> The FY26 PDI book funds PMTEC across three service components within the "Exercises, Training, Experimentation, and Innovation" PDI category [s.2026-05-12-fy2026-pacific-deterrence-init]: - **Department of the Army ($851M total)** — Operation & Maintenance funds *"rotations at the Joint Pacific Multinational Readiness Training Center (JPMRC) and the Pacific Multi-Domain Training and Experimentatio…

**Citations:** [s.2026-05-12-fy2026-pacific-deterrence-init]

**Sources checked:**
- `[s.2026-05-12-fy2026-pacific-deterrence-init]` → `01_sources/2026-05-12_comptroller-war-gov_fy2026-pacific-deterrence-initiative.md` — verdict: **PARTIAL** ([source](https://comptroller.war.gov/Portals/45/Documents/defbudget/FY2026/FY2026_Pacific_Deterrence_Initiative.pdf))
  > _"Operation and Maintenance: Funds exercises and activities which build strategic readiness and operations with allies and partners in the USINDOPACOM Area of Responsibility. Specifically, this account funds transportation, travel, repair parts, supplies and materials, and contracts for units participating in Operation Pathways exercises. Also, the account funds rotations at the Joint Pacific Multin…"_
  - Missing in this source: 1) The claim states Army total is '$851M' — source shows $850,875K which rounds to $851M, acceptable. 2) The claim states Navy total is '$588M' — source shows $587,565K, acceptable. 3) The claim states Air Force total is '$752M' — source shows $751,919K, acceptable. 4) The claim states the Air Force line item '0207429F Combat Training Ranges' is at '$147.2M' — source shows this is under 'Other Procurement, Air Force' at $147,183K (~$147.2M), acceptable. 5) However, the claim states The Joint Staff funds '$310M' covering 'JTEEP and Theater Forces line items' — the source shows only one Joint Staff line item (JTEEP at $310,272K); 'Theater Forces' is a U.S. Special Operations Command line item ($10,476K) under a different sub-section, not a Joint Staff line item. 6) The source does not contain the 'Editor note' text — that is internal claim metadata, not verifiable from source. 7) The claim describes Army 'Other Army PDI funding supports JPMRC-IS distributed instrumented LVC training and Kwajalein test-range infrastructure' — this is supported by the source text.
  - Model note: The source supports the three PMTEC service-component descriptions (Army, Navy, Air Force) and dollar totals accurately, and supports the Joint Staff $310M JTEEP figure, but the claim incorrectly characterizes the Joint Staff slice as covering both 'JTEEP and Theater Forces line items' when Theater Forces ($10,476K) belongs to U.S. Special Operations Command, not The Joint Staff.

### ⚑ FACT #4 §3  —  **PARTIAL**

**Claim:**
> PMTEC runs a Quarterly Commercial Industry Update (most recent: 13 March 2026, Honolulu, hosted with Defense Innovation OnRamp Hub: Hawaii) [s.2026-04-22-pacom] [s.2026-05-12-usindopacom-seeks-industry-par].

**Citations:** [s.2026-04-22-pacom] [s.2026-05-12-usindopacom-seeks-industry-par]

**Sources checked:**
- `[s.2026-04-22-pacom]` → ⚠ not in `01_sources/` (cited only in §8.2)
- `[s.2026-05-12-usindopacom-seeks-industry-par]` → `01_sources/2026-05-12_pacom-mil_usindopacom-seeks-industry-partners-to-address-modern-milita.md` — verdict: **PARTIAL** ([source](https://www.pacom.mil/About-USINDOPACOM/PMTEC/Article/4467480/usindopacom-seeks-industry-partners-to-address-modern-military-challenges/))
  > _"The event, hosted by USINDOPACOM J7 Pacific Multi-Domain Training and Experimentation Capability (PMTEC) and the Defense Innovation OnRamp Hub: Hawaii, a program of the Defense Innovation Unit, connected military leaders with industry representatives to outline a path toward a more integrated, all-domain training and operations ecosystem in the region."_
  - Missing in this source: The source confirms PMTEC holds quarterly industry meetings and the event was co-hosted with Defense Innovation OnRamp Hub: Hawaii, but does not specify the date as 13 March 2026 or the location as Honolulu.
  - Model note: The source supports the existence of PMTEC's quarterly industry meetings and the co-hosting arrangement with Defense Innovation OnRamp Hub: Hawaii, but does not explicitly state the date (13 March 2026) or the city (Honolulu) for the most recent event.

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
  - Missing in this source: The source does not describe Maj. Nguyen as the 'formal industry intake POC'; it describes him as representing 'industry engagement' for J83 and providing guidance, but the specific designation as 'formal industry intake POC' is not explicitly stated. Additionally, the source identifies Brent Parker as the 'PMTEC Industry Engagement Lead' with a contact email, suggesting Parker may share or hold a primary POC role.
  - Model note: The source confirms Maj. Nguyen's name, rank, and J83 Joint Validation Division affiliation and his role in guiding industry engagement, but does not use the term 'formal industry intake POC,' and the source simultaneously identifies Brent Parker as the contact for PMTEC industry engagement events.

### ⚑ FACT #7 §3  —  **PARTIAL**

**Claim:**
> Brent Parker (PMTEC Commercial Industry Engagement Lead, contractor) is the working-level POC; email brent.m.parker2.ctr@us.navy.mil [s.2026-04-22-pacom] [s.2026-05-12-usindopacom-seeks-industry-par]. *Role title and identity confirmed via ingested [s.2026-05-11-driving-readiness-indopacom-j7] which names him "PMTEC Industry Engagement Lead" moderating the POST 2026 panel. The .ctr email is single…

**Citations:** [s.2026-04-22-pacom] [s.2026-05-12-usindopacom-seeks-industry-par] [s.2026-05-11-driving-readiness-indopacom-j7]

**Sources checked:**
- `[s.2026-04-22-pacom]` → ⚠ not in `01_sources/` (cited only in §8.2)
- `[s.2026-05-12-usindopacom-seeks-industry-par]` → `01_sources/2026-05-12_pacom-mil_usindopacom-seeks-industry-partners-to-address-modern-milita.md` — verdict: **PARTIAL** ([source](https://www.pacom.mil/About-USINDOPACOM/PMTEC/Article/4467480/usindopacom-seeks-industry-partners-to-address-modern-military-challenges/))
- `[s.2026-05-11-driving-readiness-indopacom-j7]` → `01_sources/2026-05-11_dvidshub-net_driving-readiness-indopacom-j7-outlines-all-domain-training.md` — verdict: **PARTIAL** ([source](https://www.dvidshub.net/news/561976/driving-readiness-indopacom-j7-outlines-all-domain-training-strategy-post-2026))
  > _""For companies with relevant capabilities, PMTEC offers an opportunity to contribute to defense preparedness while testing and refining their technologies in operational environments," said PMTEC Industry Engagement Lead, Brent Parker. For more information on PMTEC Industry Engagement events and activities, contact Brent Parker at brent.m.parker2.ctr@us.navy.mil"_
  - Missing in this source: The claim states his role title is 'PMTEC Commercial Industry Engagement Lead' but the source only calls him 'PMTEC Industry Engagement Lead' (no 'Commercial' modifier). The claim also states his role was confirmed via a separately ingested document naming him 'PMTEC Industry Engagement Lead moderating the POST 2026 panel' — that secondary confirmation is not present in this source. The 'contractor' designation is implied by the .ctr email suffix but not explicitly stated in the source text.
  - Model note: The source directly provides Brent Parker's name, role title (partially matching), and email address, but the exact role title 'PMTEC Commercial Industry Engagement Lead' and the 'contractor' designation are not explicitly confirmed in this source, and the claim's assertion that the email is 'single-sourced to the un-ingested pacom.mil article' is contradicted — this ingested source does contain the email.
  > _"The panel, moderated by PMTEC Industry Engagement Lead Brent Parker"_
  - Missing in this source: The claim's role title 'PMTEC Commercial Industry Engagement Lead' is slightly different from the source's 'PMTEC Industry Engagement Lead' (minor discrepancy). The 'contractor' designation and the .ctr email address (brent.m.parker2.ctr@us.navy.mil) are entirely absent from this source — the claim itself acknowledges the email is single-sourced to an un-ingested pacom.mil article.
  - Model note: The source confirms Brent Parker's name and role as 'PMTEC Industry Engagement Lead' moderating the POST 2026 panel, but does not contain any email address, contractor status, or the exact title wording 'Commercial Industry Engagement Lead' cited in the claim.

### ⚑ FACT #8 §4  —  **PARTIAL**

**Claim:**
> PMTEC was established in 2022 by USINDOPACOM J7 [s.2026-04-22-pacom] [s.2026-05-12-usindopacom-seeks-industry-par]. *Corroborated by ingested primary source [s.2026-05-11-multinational-forces-destroy-d] (pacom.mil PMTEC Article 4478558), which states: "About PMTEC: Established in 2022, the Pacific Multi-Domain Training and Experimentation Capability is a transformative enterprise funded and resour…

**Citations:** [s.2026-04-22-pacom] [s.2026-05-12-usindopacom-seeks-industry-par] [s.2026-05-11-multinational-forces-destroy-d]

**Sources checked:**
- `[s.2026-04-22-pacom]` → ⚠ not in `01_sources/` (cited only in §8.2)
- `[s.2026-05-12-usindopacom-seeks-industry-par]` → `01_sources/2026-05-12_pacom-mil_usindopacom-seeks-industry-partners-to-address-modern-milita.md` — verdict: **PARTIAL** ([source](https://www.pacom.mil/About-USINDOPACOM/PMTEC/Article/4467480/usindopacom-seeks-industry-partners-to-address-modern-military-challenges/))
- `[s.2026-05-11-multinational-forces-destroy-d]` → `01_sources/2026-05-11_pacom-mil_multinational-forces-destroy-dynamic-threat-targets-during-b.md` — verdict: **PARTIAL** ([source](https://www.pacom.mil/About-USINDOPACOM/PMTEC/Article/4478558/))
  > _"About PMTEC: Established in 2022, the Pacific Multi-Domain Training and Experimentation Capability is a transformative enterprise funded and resourced by the United States Indo-Pacific Command"_
  - Missing in this source: The claim states PMTEC was 'established in 2022 by USINDOPACOM J7,' but the source only says it was funded and resourced by USINDOPACOM; J7 is described as hosting/overseeing PMTEC, not as the entity that established it.
  - Model note: The source confirms the 2022 establishment date and USINDOPACOM funding/resourcing, but does not explicitly state that J7 (as opposed to USINDOPACOM broadly) established PMTEC; J7 is described as the host and overseer, not the founding entity.
  > _"About PMTEC: Established in 2022, the Pacific Multi-Domain Training and Experimentation Capability is a transformative enterprise funded and resourced by the United States Indo-Pacific Command"_
  - Missing in this source: The claim states PMTEC was established 'by USINDOPACOM J7'; the source says it was 'funded and resourced by the United States Indo-Pacific Command' but does not attribute its establishment specifically to the J7 directorate.
  - Model note: The source confirms PMTEC was established in 2022 and is associated with USINDOPACOM, but it does not specify that the J7 directorate was the establishing authority — only that J7 PMTEC supports exercises, and that USINDOPACOM funds and resources the enterprise.

### ✓ FACT #9 §4  —  **SUPPORTS**

**Claim:**
> PMTEC integrates geographically distributed ranges and training areas across the Indo-Pacific — described by program leadership as the world's largest coalition range system [s.2026-04-03-dvids-post]. *Corroborated by ingested primary source [s.2026-05-11-multinational-forces-destroy-d] (pacom.mil PMTEC Article 4478558): "It has created and is constantly enhancing the largest coalition range syste…

**Citations:** [s.2026-04-03-dvids-post] [s.2026-05-11-multinational-forces-destroy-d]

**Sources checked:**
- `[s.2026-04-03-dvids-post]` → ⚠ not in `01_sources/` (cited only in §8.2)
- `[s.2026-05-11-multinational-forces-destroy-d]` → `01_sources/2026-05-11_pacom-mil_multinational-forces-destroy-dynamic-threat-targets-during-b.md` — verdict: **SUPPORTS** ([source](https://www.pacom.mil/About-USINDOPACOM/PMTEC/Article/4478558/))
  > _"It has created and is constantly enhancing the largest coalition range system in the world, linking geographically distributed ranges and training areas across the Indo-Pacific theater and beyond."_
  - Model note: The source explicitly states PMTEC created 'the largest coalition range system in the world' by 'linking geographically distributed ranges and training areas across the Indo-Pacific theater and beyond,' which directly supports all elements of the claim, and the parenthetical note in the claim accurately flags the absence of 'fully instrumented' modifier in the .mil wording.

### ⚑ FACT #10 §5  —  **PARTIAL**

**Claim:**
> Huntington Ingalls Industries (HII) reported FY2025 (year ended December 31, 2025) results via 10-K; Mission Technologies segment develops integrated technology solutions and products that enable the connected, all-domain force. As of December 31, 2024, total backlog was approximately $48.7 billion, with approximately 21% of backlog expected to convert to sales in 2025; HII had over 44,000 employe…

**Citations:** [s.2026-05-12-huntington-ingalls-industries-]

**Sources checked:**
- `[s.2026-05-12-huntington-ingalls-industries-]` → `01_sources/2026-05-12_sec-gov_huntington-ingalls-industries-form-10-k-fiscal-year-ended-de.md` — verdict: **PARTIAL** ([source](https://www.sec.gov/Archives/edgar/data/1501585/000150158526000006/hii-20251231.htm))
  > _"Our Mission Technologies segment develops integrated technology solutions and products that enable today's connected, all-domain force. ... We have approximately 44,000 employees."_
  - Missing in this source: The claim states total backlog was approximately $48.7 billion as of December 31, 2024, with approximately 21% expected to convert to sales in 2025. The source does not contain any backlog figures or backlog conversion percentages. Also, the claim states the filing is for FY2025 (year ended December 31, 2025), which is correct per the source, but the backlog date referenced in the claim is December 31, 2024, which would be from the prior year's 10-K — this data is not present in the source at all.
  - Model note: The source supports the Mission Technologies description and the ~44,000 employees figure, but contains no mention of total backlog of $48.7 billion or the 21% conversion rate, making the claim only partially supported.

### ⚑ FACT #11 §5  —  **PARTIAL**

**Claim:**
> SOSi (SOS International) engineers and operates the **INDOPACOM Mission Network (IMN)** as a managed-service Mission Partner Environment solution under task orders from the Mission Partner Environment Network Engineering Services IDIQ [s.2026-05-12-sosi-indopacom-mission-network]. The IMN replaces a stack of partner-nation networks with a single Zero-Trust, data-centric platform; it was tested for…

**Citations:** [s.2026-05-12-sosi-indopacom-mission-network] [s.2026-05-12-indopacom-is-replacing-a-pile-]

**Sources checked:**
- `[s.2026-05-12-sosi-indopacom-mission-network]` → `01_sources/2026-05-12_sosi-com_sosi-indopacom-mission-network-imn-program-page.md` — verdict: **DOES_NOT_SUPPORT** ([source](https://www.sosi.com/digital-infrastructure/cloud/indopacom-mission-partner-environment-mpe/))
- `[s.2026-05-12-indopacom-is-replacing-a-pile-]` → `01_sources/2026-05-12_defenseone-com_indopacom-is-replacing-a-pile-of-partner-nation-networks-wit.md` — verdict: **PARTIAL** ([source](https://www.defenseone.com/defense-systems/2024/11/indopacom-replacing-pile-partner-nation-networks-just-one/401129/))
  - Missing in this source: The source does not mention: SOSi engineering or operating the IMN; the Mission Partner Environment Network Engineering Services IDIQ or task orders; the IMN replacing a stack of partner-nation networks; Zero-Trust data-centric platform; Balikatan 2026 testing; connected nations (Philippines, Australia, Japan, New Zealand, Canada); full operational capability during Pacific Sentry in summer 2025; or any specific details about the IMN program itself.
  - Model note: The source only provides general background on DISA's mission to develop standardized information-sharing infrastructure for USINDOPACOM and its allies, without mentioning SOSi, the IMN by name, any contract vehicles, exercises, partner nations, or any of the specific technical or programmatic details contained in the claim.
  > _"This INDOPACOM Mission Network, or IMN, is meant to replace the current unwieldy situation with a single seamless and secure platform... Once IMN gains approval by the National Security Agency, the admiral said, its zero trust architecture 'will be operationalized with our allies and partners.'... 'by 2025, in the summer, our mission network will reach full operational capability during Exercise P…"_
  - Missing in this source: 1) SOSi/SOS International is not mentioned anywhere in the source as the engineer or operator of the IMN. 2) The 'Mission Partner Environment Network Engineering Services IDIQ' contract vehicle and SOSi's task orders are not mentioned. 3) The claim that IMN was 'tested for the first time during Balikatan 2026 (April–May 2026)' is not supported; the source says the IMN first stood up in February (Keen Edge) and was used in June's Valiant Shield — no mention of Balikatan 2026. 4) The claim describes the IMN as 'data-centric' which is not explicitly stated. 5) Japan and Philippines are not listed in the source as already connected at the time of the article (Philippines was listed as 'next up'). 6) Canada is not separately listed as a connected nation beyond Five Eyes membership.
  - Model note: The source supports several elements (single-network replacement of multiple partner networks, zero-trust architecture, Five Eyes nations, Pacific Sentry FOC in summer 2025) but does not mention SOSi at all, does not reference the contract vehicle, and contradicts the claim about Balikatan 2026 being the first test.

### ⚑ FACT #12 §5  —  **PARTIAL**

**Claim:**
> Lockheed Martin demonstrated its digital C2 platform integrated with the first **Joint Fires Network (JFN)** prototype at USINDOPACOM's Valiant Shield 2024 exercise (June 2024). JFN is an INDOPACOM initiative to network any sensor to any weapon system; a "combat-representative 1.0" version was targeted for end of 2024 [s.2026-05-12-lockheed-martin-integrates-c2-]. Lockheed publicly frames its Indo…

**Citations:** [s.2026-05-12-lockheed-martin-integrates-c2-] [s.2026-05-12-lockheed-martin-all-in-in-the-]

**Sources checked:**
- `[s.2026-05-12-lockheed-martin-integrates-c2-]` → `01_sources/2026-05-12_news-lockheedmartin-com_lockheed-martin-integrates-c2-with-first-joint-fires-network.md` — verdict: **PARTIAL** ([source](https://news.lockheedmartin.com/2024-06-20-Lockheed-Martin-Integrates-Command-and-Control-Capabilities-with-First-Joint-Fires-Network-Prototype))
- `[s.2026-05-12-lockheed-martin-all-in-in-the-]` → `01_sources/2026-05-12_lockheedmartin-com_lockheed-martin-all-in-in-the-indo-pacific-feature-2024.md` — verdict: **PARTIAL** ([source](https://www.lockheedmartin.com/en-us/news/features/2024/lockheed-martin-all-in-in-the-Indo-Pacific.html))
  > _"Lockheed Martin (NYSE: LMT) successfully integrated digital command and control (C2) capabilities with the first version of the Department of Defense's Joint Fires Network during the U.S. Indo-Pacific Command's (INDOPACOM) Valiant Shield exercise."_
  - Missing in this source: 1) The claim states a 'combat-representative 1.0' version was targeted for end of 2024 — the source does not mention this milestone or timeline. 2) The claim references Lockheed's 'All In' framing with specific investments in JADC2, Aegis, F-35, hypersonics, and partner-nation programs across Australia, Japan, ROK, and other allies — the source only mentions 'Lockheed Martin All In in the Indo Pacific' as a link reference without detailing those specific program areas or partner nations.
  - Model note: The source clearly supports the core claim about LM integrating digital C2 with the first JFN prototype at Valiant Shield 2024 and JFN being an INDOPACOM initiative to network sensors to weapon systems, but does not contain evidence for the 'combat-representative 1.0' end-of-2024 target or the specific 'All In' program details (Aegis, F-35, hypersonics, Australia, Japan, ROK).
  > _"Lockheed Martin successfully integrated digital command and control (C2) capabilities with the first version of the Pentagon's Joint Fires Network during the exercise. [...] Valiant Shield marks the first test of the initial Joint Fires Network prototype, which will provide crucial insights for the Pentagon's ongoing CJADC2 efforts."_
  - Missing in this source: 1) The claim describes JFN as 'an INDOPACOM initiative to network any sensor to any weapon system' — the source attributes JFN to 'the Pentagon,' not INDOPACOM specifically. 2) The claim states a 'combat-representative 1.0' version was targeted for end of 2024 — this language and timeline does not appear in the source. 3) The claim lists specific partner-nation programs across Australia, Japan, ROK as part of the 'All In' framing, along with Aegis, F-35, and hypersonics — the source does not mention these specific programs or nations.
  - Model note: The source confirms the digital C2/JFN prototype integration at Valiant Shield 2024 and the 'All In' framing, but attributes JFN to the Pentagon rather than INDOPACOM, omits the 'combat-representative 1.0' end-of-2024 target, and does not enumerate the specific partner nations or weapon systems cited in the claim.

### ⚑ FACT #13 §5  —  **PARTIAL**

**Claim:**
> L3Harris demonstrated its **Distributed Spectrum Collaboration and Operations (DiSCO™)** cloud-connected Electromagnetic Spectrum Operations architecture at Valiant Shield 2024 — sharing real-time RF signal data between Joint Base Pearl Harbor-Hickam (Hawaii) and EW payloads in Hawaii and San Diego, including small payloads on two Seasats Lightfish autonomous surface vehicles [s.2026-05-12-l3harri…

**Citations:** [s.2026-05-12-l3harris-demonstrates-disco-el] [s.2026-05-12-l3harris-demonstrates-autonomo]

**Sources checked:**
- `[s.2026-05-12-l3harris-demonstrates-disco-el]` → `01_sources/2026-05-12_l3harris-com_l3harris-demonstrates-disco-electronic-warfare-operations-du.md` — verdict: **PARTIAL** ([source](https://www.l3harris.com/newsroom/press-release/2024/07/l3harris-demonstrates-electronic-warfare-valiant-shield-2024))
- `[s.2026-05-12-l3harris-demonstrates-autonomo]` → `01_sources/2026-05-12_l3harris-com_l3harris-demonstrates-autonomous-ew-capability-with-shield-a.md` — verdict: **PARTIAL** ([source](https://www.l3harris.com/newsroom/press-release/2026/04/l3harris-demonstrates-autonomous-electronic-warfare-capability))
  > _"During the exercise, DiSCO successfully shared real-time radio frequency signal data between Joint Base Pearl Harbor-Hickam, Hawaii, and multiple EW payloads operating in Hawaii and in San Diego, California. Small form-factor payloads operated on two Seasats' autonomous surface vehicles along with satellite communications links at both locations."_
  - Missing in this source: The source does not mention 'Lightfish' as the model name of the Seasats autonomous surface vehicles (only 'Seasats' autonomous surface vehicles'). More critically, the source contains no information about the April 2026 demonstration of DiSCO integrated with Shield AI's Hivemind autonomy software for autonomous EW.
  - Model note: The source supports the Valiant Shield 2024 portion of the claim well (DiSCO, real-time RF sharing, JBPHH, Hawaii/San Diego payloads, two Seasats ASVs), but does not reference 'Lightfish' by name and contains absolutely no evidence for the April 2026 L3Harris/Shield AI Hivemind integration claim.
  > _"Operating within the Distributed Spectrum Collaboration and Operations (DiSCO™) ecosystem, the Deceptor system enabled coordinated, AI-enabled sensing and effects across the battlespace. The integrated system also detected and geolocated radio frequency (RF) threats, fused data from multiple sensors in real time, and executed RF jamming to neutralize those threats."_
  - Missing in this source: 1) The source does not mention Shield AI or Hivemind autonomy software at all — the April 2026 demonstration is attributed to a 'U.S. Army experiment' with no mention of Shield AI integration. 2) The source does not mention Valiant Shield 2024, Joint Base Pearl Harbor-Hickam, San Diego, or Seasats Lightfish autonomous surface vehicles. 3) The source mentions Deceptor on unmanned aerial systems (UAS), not surface vehicles. 4) The source does not describe the Hawaii-to-San Diego cloud-connected RF data sharing described in the claim.
  - Model note: The source supports the April 2026 DiSCO autonomous EW demonstration concept (detect, analyze, respond to RF threats without human intervention) but does not mention Shield AI or Hivemind, and the Valiant Shield 2024 details with Seasats Lightfish and geographic data-sharing elements are entirely absent from the source.

### ⚑ FACT #14 §5  —  **PARTIAL**

**Claim:**
> Northrop Grumman demonstrated capabilities in Indo-Pacific region exercises enabling joint force detection, location, tracking and engagement of adversarial threats at sea, in the air, on land, and in cyberspace [s.2026-05-12-northrop-grumman-demonstrates-]. In April 2026, Japan announced a collaboration with Northrop Grumman to enhance EW capabilities including data optimization, threat simulatio…

**Citations:** [s.2026-05-12-northrop-grumman-demonstrates-] [s.2026-05-12-japan-teams-with-northrop-grum]

**Sources checked:**
- `[s.2026-05-12-northrop-grumman-demonstrates-]` → `01_sources/2026-05-12_news-northropgrumman-com_northrop-grumman-demonstrates-critical-capabilities-in-indo.md` — verdict: **PARTIAL** ([source](https://news.northropgrumman.com/global/northrop-grumman-demonstrates-critical-capabilities-in-indo-pacific-region-exercises))
- `[s.2026-05-12-japan-teams-with-northrop-grum]` → `01_sources/2026-05-12_thedefensepost-com_japan-teams-with-northrop-grumman-to-boost-electronic-warfar.md` — verdict: **PARTIAL** ([source](https://thedefensepost.com/2026/04/28/japan-northrop-grumman-electronic-warfare/))
  > _"Capabilities enabled by Northrop Grumman technologies allowed the Joint Force to practice real-world efficiency in detecting, locating, tracking and engaging adversarial threats at sea, in the air, on land and in cyberspace."_
  - Missing in this source: The claim's second sentence — that in April 2026 Japan announced a collaboration with Northrop Grumman to enhance EW capabilities including data optimization, threat simulation, and the full EW cycle (detection, exploitation, deception, denial, protection), explicitly motivated by Indo-Pacific tensions with China around Taiwan and the South China Sea — is entirely absent from the source.
  - Model note: The source supports the first part of the claim about Indo-Pacific exercise capabilities, but contains no mention of a Japan-Northrop Grumman EW collaboration, April 2026 announcement, or any reference to China, Taiwan, or the South China Sea.
  > _"Japan is moving towards further enhancing its electronic warfare (EW) capabilities through a collaboration with US defense giant Northrop Grumman. Both are exploring joint efforts to build local capabilities, as well as data optimization and threat simulation, to strengthen Tokyo's ability to handle the entire EW cycle from enemy detection, exploitation, deception, and denial, as well as protectio…"_
  - Missing in this source: The first part of the claim regarding Northrop Grumman demonstrating capabilities in Indo-Pacific region exercises enabling joint force detection, location, tracking and engagement of adversarial threats at sea, in the air, on land, and in cyberspace is not supported anywhere in the source text.
  - Model note: The source fully supports the Japan-Northrop Grumman EW collaboration elements of the claim (data optimization, threat simulation, full EW cycle, Indo-Pacific/China/Taiwan/South China Sea motivation) but contains no mention of Indo-Pacific exercises enabling joint force detection, location, tracking, and engagement across sea, air, land, and cyberspace domains.

### ⚑ FACT #15 §5  —  **PARTIAL**

**Claim:**
> RTX (Raytheon) delivered the first Next Generation Jammer (NGJ) shipsets to the Royal Australian Air Force in April 2026; NGJ is a cooperative U.S.–RAAF development program providing airborne electronic attack via active electronically scanned arrays in the mid-band frequency range, disrupting enemy radars and comms to keep aircrew undetected [s.2026-05-12-rtx-raytheon-delivers-first-ne]. RTX's Ad…

**Citations:** [s.2026-05-12-rtx-raytheon-delivers-first-ne] [s.2026-05-12-rtx-advanced-electronic-warfar]

**Sources checked:**
- `[s.2026-05-12-rtx-raytheon-delivers-first-ne]` → `01_sources/2026-05-12_rtx-com_rtx-raytheon-delivers-first-next-generation-jammer-shipsets.md` — verdict: **PARTIAL** ([source](https://www.rtx.com/news/news-center/2026/04/20/rtxs-raytheon-delivers-first-next-generation-jammer-shipsets-to-the-royal-austra))
- `[s.2026-05-12-rtx-advanced-electronic-warfar]` → `01_sources/2026-05-12_rtx-com_rtx-advanced-electronic-warfare-prototype-for-f-a-18e-f-supe.md` — verdict: **PARTIAL** ([source](https://www.rtx.com/news/news-center/2025/09/22/rtxs-advanced-electronic-warfare-prototype-for-f-a-18e-f-super-hornet-passes-cri))
  > _"Raytheon, an RTX (NYSE: RTX) business, has delivered its first Next Generation Jammer (NGJ) pods to the Royal Australian Air Force. NGJ is a cooperative development and production program with the Royal Australian Air Force (RAAF). It is an airborne electronic attack system containing active electronically scanned arrays that radiate in the mid-band frequency range. By disrupting enemy radars and …"_
  - Missing in this source: The claim states delivery occurred 'in April 2026'; the source press release is dated April 20, 2026, but the source text itself states 'This first delivery of shipsets occurred ahead of schedule in September 2025' — meaning the actual delivery date was September 2025, not April 2026 (April 2026 is the announcement date). Additionally, the claim about RTX's ADVEW prototype for the F/A-18E/F Super Hornet passing critical review in September 2025 is entirely absent from the source.
  - Model note: The source supports the NGJ program description (cooperative U.S.-RAAF, airborne EAW, AESA, mid-band, disrupts radars/comms) but contradicts the claimed April 2026 delivery date (actual delivery was September 2025 per the source), and contains no mention of the ADVEW prototype or its critical review.
  > _"Raytheon, an RTX (NYSE: RTX) business, has successfully completed a major review of its new Advanced Electronic Warfare (ADVEW) prototype for the U.S. Navy's F/A-18E/F Super Hornet. This new system is set to replace current electronic warfare systems on the aircraft to enhance its defensive capabilities and survivability."_
  - Missing in this source: The source contains no mention of NGJ (Next Generation Jammer), no mention of delivery to the Royal Australian Air Force, no mention of April 2026 delivery, no mention of RAAF cooperative development, no mention of active electronically scanned arrays, no mention of mid-band frequency range, and no mention of disrupting enemy radars/comms. The ADVEW critical review date of September 2025 is supported, as is ADVEW being positioned to replace current EW systems on the F/A-18E/F.
  - Model note: The source supports only the ADVEW-related portions of the claim (September 2025 critical review passage and replacement of current EW systems on the Super Hornet), while the entire NGJ/RAAF portion of the claim is wholly absent from the source.

### ⚑ FACT #16 §5  —  **PARTIAL**

**Claim:**
> PMTEC has a public AI / digital-twin research partnership with **Johns Hopkins University**. The pacom.mil "USINDOPACOM Seeks Industry Partners" article quotes PMTEC PM Dr. Andre Stridiron announcing "a new research partnership with Johns Hopkins University focused on artificial intelligence and digital twin technologies" [s.2026-05-12-usindopacom-seeks-industry-par]. The January 2026 *Indo-Pacifi…

**Citations:** [s.2026-05-12-usindopacom-seeks-industry-par] [s.2026-05-12-pmtec-pioneers-ai-enabled-warf]

**Sources checked:**
- `[s.2026-05-12-usindopacom-seeks-industry-par]` → `01_sources/2026-05-12_pacom-mil_usindopacom-seeks-industry-partners-to-address-modern-milita.md` — verdict: **PARTIAL** ([source](https://www.pacom.mil/About-USINDOPACOM/PMTEC/Article/4467480/usindopacom-seeks-industry-partners-to-address-modern-military-challenges/))
- `[s.2026-05-12-pmtec-pioneers-ai-enabled-warf]` → `01_sources/2026-05-12_ipdefenseforum-com_pmtec-pioneers-ai-enabled-warfare-capabilities-indo-pacific.md` — verdict: **PARTIAL** ([source](https://ipdefenseforum.com/2026/01/pmtec-pioneers-ai-enabled-warfare-capabilities/))
  > _"He highlighted the upcoming Valiant Shield 26 exercise as a key milestone and announced a new research partnership with Johns Hopkins University focused on artificial intelligence and digital twin technologies."_
  - Missing in this source: The claim references a January 2026 *Indo-Pacific Defense FORUM* article titled 'PMTEC pioneers AI-enabled warfare capabilities' as providing additional context — this secondary source is not present in the provided source text and cannot be verified from it.
  - Model note: The pacom.mil source fully supports the core claim (PMTEC PM Dr. Andre Stridiron announcing a Johns Hopkins University AI/digital-twin partnership), but the claim also asserts a specific January 2026 Indo-Pacific Defense FORUM article provides additional context, which cannot be confirmed from the single source provided.
  > _"PMTEC's AI experimentation is supported through collaboration with the U.S. Department of War's Defense Innovation Unit and the Pacific Impact Zone, a Hawaii-based defense innovation hub."_
  - Missing in this source: The source does not mention Johns Hopkins University at all, does not name Dr. Andre Stridiron, and does not reference any research partnership focused on artificial intelligence and digital twin technologies with Johns Hopkins University. The source also does not mention digital twin technologies explicitly.
  - Model note: The source confirms PMTEC's AI integration activities broadly, which is consistent with the claim's secondary assertion that the Indo-Pacific Defense FORUM article 'provides additional context on PMTEC's AI integration but does not name the Johns Hopkins partnership explicitly' — this part of the claim is actually SUPPORTS, but the primary claim about a Johns Hopkins University partnership quoted from pacom.mil finds zero support in this source.

### ⚑ FACT #17 §6  —  **PARTIAL**

**Claim:**
> Deloitte holds GSA OASIS delivery order **PIID `47QFCA25F0010`** (parent IDIQ `GS00Q14OADU113`, the OASIS Unrestricted Pool Professional Services Multiple Agency Contract) supporting USINDOPACOM with enterprise-wide professional services. Period start **2025-03-01**; current period end (Year 1) **2026-07-31**; place of performance **Hawaii** (Camp H.M. Smith). Obligated to date: **$58,923,548** [s…

**Citations:** [s.2026-05-11-indopacom-alpha-deloitte]

**Sources checked:**
- `[s.2026-05-11-indopacom-alpha-deloitte]` → `01_sources/2026-05-11_usaspending-gov_indopacom-alpha-deloitte.md` — verdict: **PARTIAL** ([source](https://www.usaspending.gov/award/CONT_AWD_47QFCA25F0010_4732_GS00Q14OADU113_4732/))
  > _"PIID: 47QFCA25F0010 ... Parent IDIQ (vehicle): PIID: GS00Q14OADU113 ... Description: ONE ACQUISITION SOLUTION FOR INTEGRATED SERVICES (OASIS) PROFESSIONAL SERVICES MULTIPLE AGENCY CONTRACT ... Recipient Name: DELOITTE CONSULTING LLP ... Total obligation to date: $58,923,548 ... Place of performance: Hawaii (state code HI) ... Period start: 2025-03-01 ... Period current end (Year 1): 2026-07-31"_
  - Missing in this source: The claim states 'Camp H.M. Smith' as the place of performance, but the source only confirms Hawaii (state code HI; city code not reported) — Camp H.M. Smith is noted parenthetically as an inference, not as an explicit data field in the record. All other elements (PIID, parent IDIQ PIID, OASIS Unrestricted Pool vehicle, Deloitte as awardee, USINDOPACOM customer, period start 2025-03-01, current period end 2026-07-31, obligation $58,923,548, Hawaii place of performance, and USAspending API corroboration of awardee/vehicle/customer/place of performance/start date) are explicitly supported.
  - Model note: The source supports every numerical, date, and descriptive element of the claim except that 'Camp H.M. Smith' as a specific city/installation is inferred commentary in the source rather than an explicitly reported data field, making the claim partially but not fully supported on that specific detail.

### ⚑ FACT #18 §6  —  **PARTIAL**

**Claim:**
> PACAF Base Area Network modernization — $180M, 5-yr task order on AFBIM IDIQ awarded Sep 2025. Direct PACAF/INDOPACOM IT backbone with Zero Trust foundation [s.govconwire-sep2025-caci-afbim] [s.2026-05-12-caci-to-modernize-air-force-ba]. *Single-sourced — verify via USAspending (search Deloitte/CACI AFBIM 2025) and CACI IR.*

**Citations:** [s.govconwire-sep2025-caci-afbim] [s.2026-05-12-caci-to-modernize-air-force-ba]

**Sources checked:**
- `[s.govconwire-sep2025-caci-afbim]` → ⚠ not in `01_sources/` (cited only in §8.2)
- `[s.2026-05-12-caci-to-modernize-air-force-ba]` → `01_sources/2026-05-12_washingtonexec-com_caci-to-modernize-air-force-base-networks-in-pacific-under-1.md` — verdict: **PARTIAL** ([source](https://washingtonexec.com/2025/09/caci-to-modernize-air-force-base-networks-in-pacific-under-180m-task-order/))
  > _"CACI International has received a 5-year task order worth up to $180 million to provide secure and stable network operations for Pacific Air Forces in support of U.S. Indo-Pacific Command."_
  - Missing in this source: The claim states the award was on the 'AFBIM IDIQ' and awarded 'Sep 2025' — the source confirms the program name (Base Infrastructure Modernization) and the $180M/5-year figures but does not explicitly state the award date or confirm it is an IDIQ vehicle. The claim also mentions 'Deloitte/CACI AFBIM' suggesting Deloitte involvement, which is not mentioned in the source. The 'single-sourced — verify via USAspending' caveat is a meta-note not verifiable from the source itself.
  - Model note: The source supports the core facts ($180M, 5-year, PACAF/INDOPACOM, Zero Trust foundation, CACI, Base Area Network modernization under Base Infrastructure Modernization contract) but does not confirm the September 2025 award date, the IDIQ vehicle structure, or any Deloitte connection mentioned in the claim's verification note.

### ⚑ FACT #19 §6  —  **PARTIAL**

**Claim:**
> Spectral (NAVWAR) — $1.2B ceiling, shipboard SIGINT/EW/IO. $143M Spectral Enabling Kits delivery order May 2025 [s.bizwire-may2025-spectral] [s.2026-05-12-caci-mission-critical-technolo]. *Single-sourced — verify via CACI IR.*

**Citations:** [s.bizwire-may2025-spectral] [s.2026-05-12-caci-mission-critical-technolo]

**Sources checked:**
- `[s.bizwire-may2025-spectral]` → ⚠ not in `01_sources/` (cited only in §8.2)
- `[s.2026-05-12-caci-mission-critical-technolo]` → `01_sources/2026-05-12_businesswire-com_caci-mission-critical-technology-will-accelerate-delivery-of.md` — verdict: **PARTIAL** ([source](https://www.businesswire.com/news/home/20250507187909/en/CACIs-Mission-Critical-Technology-will-Accelerate-the-Delivery-of-Electronic-Warfighting-Capabilities-to-the-U.S.-Navys-Existing-Fleet))
  > _"The $143 million firm-fixed-price delivery order represents a new phase of work on the CACI's existing Spectral contract with the Naval Information Warfare Systems Command (NAVWAR) which is authorized with a $1.2 billion ceiling value."_
  - Missing in this source: The claim states the delivery order was awarded 'May 2025'; the source article is dated with a URL timestamp of 20250507 but the publication_date field is blank, so the date is only inferrable, not explicitly stated in the extracted content. Additionally, the claim characterizes Spectral as 'single-sourced' and directs verification via 'CACI IR' — neither of these elements is addressed in the source. The source does confirm SIGINT/EW/IO and shipboard nature, $1.2B ceiling, $143M delivery order, and NAVWAR.
  - Model note: The source explicitly supports the $1.2B ceiling, $143M SEK delivery order, NAVWAR contracting authority, and shipboard SIGINT/EW/IO mission description, but does not confirm the May 2025 date in the article body text, nor the 'single-sourced' characterization noted in the claim.

### ✓ FACT #20 §6  —  **SUPPORTS**

**Claim:**
> Trojan EATS (Army DEVCOM, OASIS) — $382M, 5-yr; SIGINT/EW open-architecture systems [s.caci-ir-trojan-2024] [s.2026-05-12-u-s-army-selects-caci-for-382-].

**Citations:** [s.caci-ir-trojan-2024] [s.2026-05-12-u-s-army-selects-caci-for-382-]

**Sources checked:**
- `[s.caci-ir-trojan-2024]` → ⚠ not in `01_sources/` (cited only in §8.2)
- `[s.2026-05-12-u-s-army-selects-caci-for-382-]` → `01_sources/2026-05-12_businesswire-com_u-s-army-selects-caci-for-382-million-signals-intelligence-a.md` — verdict: **SUPPORTS** ([source](https://www.businesswire.com/news/home/20240123940984/en/U.S.-Army-Selects-CACI-for-%24382-Million-Signals-Intelligence-and-Electronic-Warfare-Systems-Task-Order))
  > _"CACI International Inc (NYSE: CACI) announced today that it won a five-year, single-award task order valued at up to $382 million to provide technology to the U.S. Army Combat Capabilities Development Command (DEVCOM) Engineering and Systems Integration Directorate (ESID) Trojan Engineering and Systems Integration (ESI) Advancement of Trojan Systems (EATS). This work is part of the One Acquisition…"_
  - Model note: The source explicitly confirms all key elements of the claim: Trojan EATS program, Army DEVCOM, OASIS contract vehicle, $382M value, 5-year duration, and SIGINT/EW open-architecture systems context.

### ⚑ FACT #21 §6  —  **PARTIAL**

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
  - Missing in this source: The claim states the acquisition adds satellite sensors for 'SIGINT/EW' (signals intelligence and electronic warfare). The source confirms space-based sensors and agentic AI, and mentions SIGINT only as an existing CACI strength that ARKA's geospatial intelligence complements — not as a capability ARKA itself adds. Additionally, EW (electronic warfare) is not mentioned in the source at all. The sensors described are EO/IR and hyperspectral imaging, not explicitly 'satellite sensors for SIGINT/EW.'
  - Model note: The source supports the closing date (March 9, 2026), the $2.6B price, space-based sensors, and agentic AI, but the claim's characterization of the sensors as being for SIGINT/EW is not directly supported — SIGINT is CACI's existing capability, and EW is not mentioned.
  > _"During the third quarter, we closed the acquisition of ARKA, a leading technology company focused on national security missions in the space domain. ARKA brings exquisite space-based imaging sensor technology with high technical barriers to entry, agentic AI-based ground processing software, and deep customer relationships built over decades of strong performance."_
  - Missing in this source: The $2.6B acquisition price is not mentioned in the source. The specific claim about 'satellite sensors + agentic AI for SIGINT/EW' is partially supported (agentic AI and space-based imaging sensors are confirmed, but SIGINT/EW is not explicitly tied to ARKA's capabilities in the source). The closing date of 'March 2026' is not explicitly stated; the source only says the acquisition closed 'during the third quarter' (CACI's Q3 FY2026).
  - Model note: The source confirms ARKA closed in Q3 FY2026 and adds space-based imaging sensors and agentic AI, but does not specify the $2.6B price or explicitly link ARKA's capabilities to SIGINT/EW; the closing month of March 2026 is consistent with Q3 FY2026 (Jan-Mar 2026) but not explicitly stated.
  - Missing in this source: The source contains no mention of ARKA Group, any acquisition closing in March 2026, a $2.6B deal, satellite sensors, or agentic AI for SIGINT/EW. The 8-K filing is solely about an amendment to a Master Accounts Receivable Purchase Agreement.
  - Model note: Despite the source metadata title referencing 'ARKA Group' and '$2.6B', the actual extracted content of this SEC 8-K filing contains no information about an ARKA acquisition — it exclusively addresses an amendment extending a receivables purchase agreement termination date.
  > _"On March 9, 2026, CACI acquired all of the equity interests of ARKA Group L.P. (ARKA) for purchase consideration of approximately $2,642.7 million, net of cash acquired, subject to post closing adjustments. This acquisition will enhance CACI's ability to deliver advanced technology for its national security customers in the space domain."_
  - Missing in this source: The claim states the acquisition adds 'satellite sensors + agentic AI for SIGINT/EW.' The source mentions 'space domain' and lists intangible assets of 'customer relationships' and 'technology,' but does not specifically mention satellite sensors, agentic AI, SIGINT, or EW capabilities. The $2.6B figure is supported (~$2,642.7M rounds to ~$2.6B) and the March 2026 close date is confirmed (March 9, 2026).
  - Model note: The source confirms the ARKA acquisition closed in March 2026 for approximately $2.6B, but does not explicitly mention satellite sensors, agentic AI, SIGINT, or EW as capabilities added by the acquisition.


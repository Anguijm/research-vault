# FACT Verification Report — PMTEC-USINDOPACOM

*Generated 2026-05-12T20:18:01 by `verify_facts.py` (model: `claude-sonnet-4-6`)*

## Summary

- **21** FACT claims scanned
- **3** SUPPORTS — claim is corroborated by an ingested source
- **16** PARTIAL — some elements supported by an ingested source
- **2** DOES_NOT_SUPPORT — ingested source contradicts or omits the claim
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
  - Missing in this source: 1) The claim attributes item 5 (AI and digital-twin) to Mary Ann Swendsen for the AI need and Stridiron for the APL (Johns Hopkins APL) partnership — the source says Stridiron announced the Johns Hopkins partnership but does NOT identify it as 'APL'; the source attributes AI/digital-twin lessons to Swendsen but does not explicitly assign the 'AI need' framing to her as a named gap. 2) The claim states the event was a 'quarterly industry meeting' — the source confirms 'PMTEC's quarterly industry meeting' but does NOT specify the date as '13 March 2026' or use the framing of 'eight gaps publicly named,' consistent with the verification note. 3) The claim frames items 1–4 as explicitly enumerated gaps and items 5–8 as separately structured; the source presents items 1–4 as a listed paragraph and items 5–8 in narrative form, which the claim accurately reflects, but the 'eight gaps' framing is not literal in the source. 4) The source does not name the event as a 'Quarterly Commercial Industry Update' — it is called a 'quarterly industry meeting.' All named individuals and their roles/contributions are otherwise accurately reflected in the source.
  - Model note: The source supports the substance of all eight items and the named individuals with their attributed contributions, but does not confirm the specific event date of 13 March 2026, the 'eight gaps' literal framing, or the 'APL' (Applied Physics Laboratory) identification for the Johns Hopkins partnership, making the claim partially but not fully supported.

### ⚑ FACT #2 §3  —  **PARTIAL**

**Claim:**
> FY26 PDI request: **$10.0B** (Grand Total $10,004,542 thousand per primary source — the FY26 PDI budget book). FY25 baseline appears to be ~$9.4B (Grand Total column 2 in the same book). PMTEC is a named line item across multiple PB sub-accounts [s.2026-fy26-comptroller] [s.2026-05-12-fy2026-pacific-deterrence-init]. *Correction 2026-05-12: planning-conversation figure was "$9.9B" — primary source…

**Citations:** [s.2026-fy26-comptroller] [s.2026-05-12-fy2026-pacific-deterrence-init]

**Sources checked:**
- `[s.2026-fy26-comptroller]` → ⚠ not in `01_sources/` (cited only in §8.2)
- `[s.2026-05-12-fy2026-pacific-deterrence-init]` → `01_sources/2026-05-12_comptroller-war-gov_fy2026-pacific-deterrence-initiative.md` — verdict: **PARTIAL** ([source](https://comptroller.war.gov/Portals/45/Documents/defbudget/FY2026/FY2026_Pacific_Deterrence_Initiative.pdf))
  > _"Grand Total 7,842,993 2,161,549 10,004,542  The FY 2026 PDI request is $10.0 billion"_
  - Missing in this source: The FY25 baseline of ~$9.4B is not present in the extracted source content; PMTEC as a named line item across multiple PB sub-accounts is not visible in the extracted pages; the correction note referencing a prior '$9.9B' planning figure is not verifiable from the source.
  - Model note: The source explicitly confirms the FY26 PDI Grand Total of $10,004,542 thousand (~$10.0B), but contains no FY25 comparison column or PMTEC line-item references in the extracted pages provided.

### ✗ FACT #3 §3  —  **DOES_NOT_SUPPORT**

**Claim:**
> The FY26 PDI book funds PMTEC across three service components within the "Exercises, Training, Experimentation, and Innovation" PDI category [s.2026-05-12-fy2026-pacific-deterrence-init]: - **Department of the Army ($851M total)** — Operation & Maintenance funds *"rotations at the Joint Pacific Multinational Readiness Training Center (JPMRC) and the Pacific Multi-Domain Training and Experimentatio…

**Citations:** [s.2026-05-12-fy2026-pacific-deterrence-init]

**Sources checked:**
- `[s.2026-05-12-fy2026-pacific-deterrence-init]` → `01_sources/2026-05-12_comptroller-war-gov_fy2026-pacific-deterrence-initiative.md` — verdict: **DOES_NOT_SUPPORT** ([source](https://comptroller.war.gov/Portals/45/Documents/defbudget/FY2026/FY2026_Pacific_Deterrence_Initiative.pdf))
  - Missing in this source: All four component-level PMTEC claims (Army $851M with JPMRC/PMTEC language; Navy $588M with Pacific Fixed Arrays/PMTEC studies/live-fire/JFDD/JDECC language; Air Force $752M with PMTEC Operations sub-category and PE 0207429F at $147.2M; Joint Staff $310M with JTEEP/Theater Forces) are not present in the extracted source content provided.
  - Model note: The extracted source pages stop before reaching the 'Exercises, Training, Experimentation, and Innovation' section (page 19 per the TOC), so none of the PMTEC-specific claims can be verified from the content actually provided.

### ⚑ FACT #4 §3  —  **PARTIAL**

**Claim:**
> PMTEC runs a Quarterly Commercial Industry Update (most recent: 13 March 2026, Honolulu, hosted with Defense Innovation OnRamp Hub: Hawaii) [s.2026-04-22-pacom] [s.2026-05-12-usindopacom-seeks-industry-par].

**Citations:** [s.2026-04-22-pacom] [s.2026-05-12-usindopacom-seeks-industry-par]

**Sources checked:**
- `[s.2026-04-22-pacom]` → ⚠ not in `01_sources/` (cited only in §8.2)
- `[s.2026-05-12-usindopacom-seeks-industry-par]` → `01_sources/2026-05-12_pacom-mil_usindopacom-seeks-industry-partners-to-address-modern-milita.md` — verdict: **PARTIAL** ([source](https://www.pacom.mil/About-USINDOPACOM/PMTEC/Article/4467480/usindopacom-seeks-industry-partners-to-address-modern-military-challenges/))
  > _"The event, hosted by USINDOPACOM J7 Pacific Multi-Domain Training and Experimentation Capability (PMTEC) and the Defense Innovation OnRamp Hub: Hawaii, a program of the Defense Innovation Unit, connected military leaders with industry representatives to outline a path toward a more integrated, all-domain training and operations ecosystem in the region."_
  - Missing in this source: The source confirms PMTEC holds a quarterly industry meeting and that it was co-hosted with Defense Innovation OnRamp Hub: Hawaii, but does not specify the date '13 March 2026' or the location 'Honolulu' for this event. The event title 'Quarterly Commercial Industry Update' is also not explicitly named in the source.
  - Model note: The source supports the existence of PMTEC's quarterly industry meeting co-hosted with Defense Innovation OnRamp Hub: Hawaii, but does not provide the specific date (13 March 2026), location (Honolulu), or the exact event title ('Quarterly Commercial Industry Update') stated in the claim.

### ✓ FACT #5 §3  —  **SUPPORTS**

**Claim:**
> Formal industry intake channel: pacom.mil/Contact/Industry-Engagements/ [s.2026-04-22-pacom] [s.2026-05-12-usindopacom-seeks-industry-par].

**Citations:** [s.2026-04-22-pacom] [s.2026-05-12-usindopacom-seeks-industry-par]

**Sources checked:**
- `[s.2026-04-22-pacom]` → ⚠ not in `01_sources/` (cited only in §8.2)
- `[s.2026-05-12-usindopacom-seeks-industry-par]` → `01_sources/2026-05-12_pacom-mil_usindopacom-seeks-industry-partners-to-address-modern-milita.md` — verdict: **SUPPORTS** ([source](https://www.pacom.mil/About-USINDOPACOM/PMTEC/Article/4467480/usindopacom-seeks-industry-partners-to-address-modern-military-challenges/))
  > _"He directed potential partners to the command's online portal at https://www.pacom.mil/Contact/Industry-Engagements/"_
  - Model note: The source explicitly identifies https://www.pacom.mil/Contact/Industry-Engagements/ as the formal industry intake channel, described as the command's online portal for companies interested in working with USINDOPACOM.

### ⚑ FACT #6 §3  —  **PARTIAL**

**Claim:**
> Maj. Tuan Nguyen (J83 Joint Validation Division) is the formal industry intake POC [s.2026-04-22-pacom] [s.2026-05-12-usindopacom-seeks-industry-par].

**Citations:** [s.2026-04-22-pacom] [s.2026-05-12-usindopacom-seeks-industry-par]

**Sources checked:**
- `[s.2026-04-22-pacom]` → ⚠ not in `01_sources/` (cited only in §8.2)
- `[s.2026-05-12-usindopacom-seeks-industry-par]` → `01_sources/2026-05-12_pacom-mil_usindopacom-seeks-industry-partners-to-address-modern-milita.md` — verdict: **PARTIAL** ([source](https://www.pacom.mil/About-USINDOPACOM/PMTEC/Article/4467480/usindopacom-seeks-industry-partners-to-address-modern-military-challenges/))
  > _"Maj. Tuan Nguyen, who represents industry engagement for the J83 Joint Validation Division, provided guidance for companies interested in working with USINDOPACOM. He directed potential partners to the command's online portal at https://www.pacom.mil/Contact/Industry-Engagements/ and emphasized the importance of understanding military requirements before submitting proposals."_
  - Missing in this source: The source does not describe Maj. Nguyen as the 'formal industry intake POC'; it describes him as representing 'industry engagement' for J83 and directing companies to an online portal, but does not use the term 'formal' or explicitly designate him as the primary/official point of contact for industry intake.
  - Model note: The source confirms Maj. Nguyen's role in J83 Joint Validation Division and his industry engagement function, but does not use the specific characterization 'formal industry intake POC,' making the claim a slight overstatement of what the source explicitly states.

### ⚑ FACT #7 §3  —  **PARTIAL**

**Claim:**
> Brent Parker (PMTEC Commercial Industry Engagement Lead, contractor) is the working-level POC; email brent.m.parker2.ctr@us.navy.mil [s.2026-04-22-pacom] [s.2026-05-12-usindopacom-seeks-industry-par]. *Role title and identity confirmed via ingested [s.2026-05-11-driving-readiness-indopacom-j7] which names him "PMTEC Industry Engagement Lead" moderating the POST 2026 panel. The .ctr email is single…

**Citations:** [s.2026-04-22-pacom] [s.2026-05-12-usindopacom-seeks-industry-par] [s.2026-05-11-driving-readiness-indopacom-j7]

**Sources checked:**
- `[s.2026-04-22-pacom]` → ⚠ not in `01_sources/` (cited only in §8.2)
- `[s.2026-05-12-usindopacom-seeks-industry-par]` → `01_sources/2026-05-12_pacom-mil_usindopacom-seeks-industry-partners-to-address-modern-milita.md` — verdict: **PARTIAL** ([source](https://www.pacom.mil/About-USINDOPACOM/PMTEC/Article/4467480/usindopacom-seeks-industry-partners-to-address-modern-military-challenges/))
- `[s.2026-05-11-driving-readiness-indopacom-j7]` → `01_sources/2026-05-11_dvidshub-net_driving-readiness-indopacom-j7-outlines-all-domain-training.md` — verdict: **PARTIAL** ([source](https://www.dvidshub.net/news/561976/driving-readiness-indopacom-j7-outlines-all-domain-training-strategy-post-2026))
  > _""For companies with relevant capabilities, PMTEC offers an opportunity to contribute to defense preparedness while testing and refining their technologies in operational environments," said PMTEC Industry Engagement Lead, Brent Parker. For more information on PMTEC Industry Engagement events and activities, contact Brent Parker at brent.m.parker2.ctr@us.navy.mil"_
  - Missing in this source: The claim states his title is 'PMTEC Commercial Industry Engagement Lead' and that he is a contractor — the source only says 'PMTEC Industry Engagement Lead' (no 'Commercial' modifier; contractor status is implied by the .ctr email suffix but not explicitly stated). The claim also references confirmation via a separately 'ingested' document naming him moderating a 'POST 2026 panel,' which is not present in this source.
  - Model note: The source directly supports Brent Parker's name, role title (with minor wording difference — no 'Commercial'), and .ctr email address, but does not confirm contractor status explicitly, the 'Commercial' modifier in the title, or the panel moderation detail referenced in the claim.
  > _"The panel, moderated by PMTEC Industry Engagement Lead Brent Parker, featured insights from USINDOPACOM's J7 Director, Brig. Gen. Richard Goodman; J7 Director of Staff and Training, Andrew Merz; PMTEC Program Manager Dr. Andre Stridiron, and Technical Director of the K. Mark Takai Pacific Warfighting Center, Allan Grove."_
  - Missing in this source: The source does not contain Brent Parker's email address (brent.m.parker2.ctr@us.navy.mil), his contractor status (.ctr designation), or his full role title as 'PMTEC Commercial Industry Engagement Lead' (source uses 'PMTEC Industry Engagement Lead' without 'Commercial').
  - Model note: The source confirms Brent Parker's name and role as 'PMTEC Industry Engagement Lead' moderating the POST 2026 panel, but does not support his contractor status, the specific email address, or the word 'Commercial' in his title.

### ⚑ FACT #8 §4  —  **PARTIAL**

**Claim:**
> PMTEC was established in 2022 by USINDOPACOM J7 [s.2026-04-22-pacom] [s.2026-05-12-usindopacom-seeks-industry-par]. *Corroborated by ingested primary source [s.2026-05-11-multinational-forces-destroy-d] (pacom.mil PMTEC Article 4478558), which states: "About PMTEC: Established in 2022, the Pacific Multi-Domain Training and Experimentation Capability is a transformative enterprise funded and resour…

**Citations:** [s.2026-04-22-pacom] [s.2026-05-12-usindopacom-seeks-industry-par] [s.2026-05-11-multinational-forces-destroy-d]

**Sources checked:**
- `[s.2026-04-22-pacom]` → ⚠ not in `01_sources/` (cited only in §8.2)
- `[s.2026-05-12-usindopacom-seeks-industry-par]` → `01_sources/2026-05-12_pacom-mil_usindopacom-seeks-industry-partners-to-address-modern-milita.md` — verdict: **PARTIAL** ([source](https://www.pacom.mil/About-USINDOPACOM/PMTEC/Article/4467480/usindopacom-seeks-industry-partners-to-address-modern-military-challenges/))
- `[s.2026-05-11-multinational-forces-destroy-d]` → `01_sources/2026-05-11_pacom-mil_multinational-forces-destroy-dynamic-threat-targets-during-b.md` — verdict: **PARTIAL** ([source](https://www.pacom.mil/About-USINDOPACOM/PMTEC/Article/4478558/))
  > _"About PMTEC: Established in 2022, the Pacific Multi-Domain Training and Experimentation Capability is a transformative enterprise funded and resourced by the United States Indo-Pacific Command"_
  - Missing in this source: The claim states PMTEC was 'established in 2022 by USINDOPACOM J7'; the source confirms it was established in 2022 and funded/resourced by USINDOPACOM, but describes J7 as overseeing/hosting PMTEC rather than as its founder or establisher.
  - Model note: The source confirms the 2022 establishment date and USINDOPACOM as the funding/resourcing authority, but attributes establishment to USINDOPACOM broadly rather than specifically to USINDOPACOM J7, making the 'by USINDOPACOM J7' attribution only partially supported.
  > _"About PMTEC: Established in 2022, the Pacific Multi-Domain Training and Experimentation Capability is a transformative enterprise funded and resourced by the United States Indo-Pacific Command"_
  - Missing in this source: The claim states PMTEC was established 'by USINDOPACOM J7'; the source says it was 'funded and resourced by' USINDOPACOM but does not attribute its establishment specifically to the J7 directorate.
  - Model note: The source confirms PMTEC was established in 2022 and is associated with USINDOPACOM, but does not state it was established 'by USINDOPACOM J7' — J7 is mentioned only as the operator/supporter of PMTEC activities, not as the founding entity.

### ✓ FACT #9 §4  —  **SUPPORTS**

**Claim:**
> PMTEC integrates geographically distributed ranges and training areas across the Indo-Pacific — described by program leadership as the world's largest coalition range system [s.2026-04-03-dvids-post]. *Corroborated by ingested primary source [s.2026-05-11-multinational-forces-destroy-d] (pacom.mil PMTEC Article 4478558): "It has created and is constantly enhancing the largest coalition range syste…

**Citations:** [s.2026-04-03-dvids-post] [s.2026-05-11-multinational-forces-destroy-d]

**Sources checked:**
- `[s.2026-04-03-dvids-post]` → ⚠ not in `01_sources/` (cited only in §8.2)
- `[s.2026-05-11-multinational-forces-destroy-d]` → `01_sources/2026-05-11_pacom-mil_multinational-forces-destroy-dynamic-threat-targets-during-b.md` — verdict: **SUPPORTS** ([source](https://www.pacom.mil/About-USINDOPACOM/PMTEC/Article/4478558/))
  > _"It has created and is constantly enhancing the largest coalition range system in the world, linking geographically distributed ranges and training areas across the Indo-Pacific theater and beyond."_
  - Model note: The source explicitly states that PMTEC has created the largest coalition range system in the world by linking geographically distributed ranges and training areas across the Indo-Pacific, directly and fully supporting the claim, and the parenthetical note in the claim correctly acknowledges the .mil wording omits 'fully instrumented'.

### ⚑ FACT #10 §5  —  **PARTIAL**

**Claim:**
> Huntington Ingalls Industries (HII) reported FY2025 (year ended December 31, 2025) results via 10-K; Mission Technologies segment develops integrated technology solutions and products that enable the connected, all-domain force. As of December 31, 2024, total backlog was approximately $48.7 billion, with approximately 21% of backlog expected to convert to sales in 2025; HII had over 44,000 employe…

**Citations:** [s.2026-05-12-huntington-ingalls-industries-]

**Sources checked:**
- `[s.2026-05-12-huntington-ingalls-industries-]` → `01_sources/2026-05-12_sec-gov_huntington-ingalls-industries-form-10-k-fiscal-year-ended-de.md` — verdict: **PARTIAL** ([source](https://www.sec.gov/Archives/edgar/data/1501585/000150158526000006/hii-20251231.htm))
  > _"Our Mission Technologies segment develops integrated technology solutions and products that enable today's connected, all-domain force. Headquartered in Newport News, Virginia, we employ over 44,000 people domestically and internationally."_
  - Missing in this source: The claim states 'total backlog was approximately $48.7 billion, with approximately 21% of backlog expected to convert to sales in 2025' as of December 31, 2024. The claim also omits the word 'today's' before 'connected, all-domain force' (a minor paraphrase difference). The backlog figures ($48.7 billion and 21% conversion) are not present anywhere in the extracted source content provided.
  - Model note: The source confirms the Mission Technologies description (with 'today's' in the original) and the 44,000+ employees figure, but the extracted source content does not contain any backlog figures ($48.7 billion or 21% conversion rate), so those elements of the claim cannot be verified from the provided text.

### ⚑ FACT #11 §5  —  **PARTIAL**

**Claim:**
> SOSi (SOS International) engineers and operates the **INDOPACOM Mission Network (IMN)** as a managed-service Mission Partner Environment solution under task orders from the Mission Partner Environment Network Engineering Services IDIQ [s.2026-05-12-sosi-indopacom-mission-network]. The IMN replaces a stack of partner-nation networks with a single Zero-Trust, data-centric platform; it was tested for…

**Citations:** [s.2026-05-12-sosi-indopacom-mission-network] [s.2026-05-12-indopacom-is-replacing-a-pile-]

**Sources checked:**
- `[s.2026-05-12-sosi-indopacom-mission-network]` → `01_sources/2026-05-12_sosi-com_sosi-indopacom-mission-network-imn-program-page.md` — verdict: **DOES_NOT_SUPPORT** ([source](https://www.sosi.com/digital-infrastructure/cloud/indopacom-mission-partner-environment-mpe/))
- `[s.2026-05-12-indopacom-is-replacing-a-pile-]` → `01_sources/2026-05-12_defenseone-com_indopacom-is-replacing-a-pile-of-partner-nation-networks-wit.md` — verdict: **PARTIAL** ([source](https://www.defenseone.com/defense-systems/2024/11/indopacom-replacing-pile-partner-nation-networks-just-one/401129/))
  - Missing in this source: SOSi engineering/operating the IMN, managed-service Mission Partner Environment solution, task orders from Mission Partner Environment Network Engineering Services IDIQ, IMN replacing a stack of partner-nation networks, Zero-Trust data-centric platform, testing during Balikatan 2026, connected forces from U.S./Philippines/Australia/Japan/New Zealand/Canada, full operational capability during Pacific Sentry exercise in summer 2025
  - Model note: The source only describes DISA's general mission to develop standardized information-sharing infrastructure for USINDOPACOM and allied partners; it contains no specific information about SOSi's role, the IMN program details, Balikatan 2026, Pacific Sentry, Zero-Trust architecture, or any of the specific claim elements.
  > _"By 2025, in the summer, our mission network will reach full operational capability during Exercise Pacific Sentry... Once IMN gains approval by the National Security Agency, the admiral said, its zero trust architecture 'will be operationalized with our allies and partners.'... In February, the IMN stood up with initial operating capacity for Keen Edge... The network was subsequently approved for …"_
  - Missing in this source: 1) SOSi/SOS International is never mentioned as the engineer or operator of IMN; 2) The 'Mission Partner Environment Network Engineering Services IDIQ' contract vehicle is not mentioned; 3) Balikatan 2026 as the first test is not supported — the source states Keen Edge (February 2024) was the first use and does not mention Balikatan 2026; 4) The claim states Balikatan 2026 was April–May 2026 as the first test, contradicting the source; 5) Japan is not mentioned as connected via IMN (only U.S., U.K., Australia, New Zealand, Canada, South Korea, Philippines are referenced); 6) The 'data-centric' descriptor is not in the source.
  - Model note: The source supports the general concept of IMN replacing multiple partner-nation networks with a single zero-trust platform and FOC during Pacific Sentry in summer 2025, but does not mention SOSi, the IDIQ contract, and explicitly contradicts the claim that Balikatan 2026 was the first test (Keen Edge in February 2024 was).

### ⚑ FACT #12 §5  —  **PARTIAL**

**Claim:**
> Lockheed Martin demonstrated its digital C2 platform integrated with the first **Joint Fires Network (JFN)** prototype at USINDOPACOM's Valiant Shield 2024 exercise (June 2024). JFN is an INDOPACOM initiative to network any sensor to any weapon system; a "combat-representative 1.0" version was targeted for end of 2024 [s.2026-05-12-lockheed-martin-integrates-c2-]. Lockheed publicly frames its Indo…

**Citations:** [s.2026-05-12-lockheed-martin-integrates-c2-] [s.2026-05-12-lockheed-martin-all-in-in-the-]

**Sources checked:**
- `[s.2026-05-12-lockheed-martin-integrates-c2-]` → `01_sources/2026-05-12_news-lockheedmartin-com_lockheed-martin-integrates-c2-with-first-joint-fires-network.md` — verdict: **PARTIAL** ([source](https://news.lockheedmartin.com/2024-06-20-Lockheed-Martin-Integrates-Command-and-Control-Capabilities-with-First-Joint-Fires-Network-Prototype))
- `[s.2026-05-12-lockheed-martin-all-in-in-the-]` → `01_sources/2026-05-12_lockheedmartin-com_lockheed-martin-all-in-in-the-indo-pacific-feature-2024.md` — verdict: **PARTIAL** ([source](https://www.lockheedmartin.com/en-us/news/features/2024/lockheed-martin-all-in-in-the-Indo-Pacific.html))
  > _"Lockheed Martin (NYSE: LMT) successfully integrated digital command and control (C2) capabilities with the first version of the Department of Defense's Joint Fires Network during the U.S. Indo-Pacific Command's (INDOPACOM) Valiant Shield exercise."_
  - Missing in this source: The claim states a 'combat-representative 1.0' version was targeted for end of 2024 — this is not mentioned in the source. The claim also references Lockheed's 'All In' framing with specific investments in JADC2, Aegis, F-35, hypersonics, and partner-nation programs across Australia, Japan, ROK, and other allies — the source only links to an 'All In in the Indo Pacific' page without detailing those specific programs or allies. The source does not describe JFN as an 'INDOPACOM initiative to network any sensor to any weapon system' in those exact terms, though it closely paraphrases this concept.
  - Model note: The source supports the core claim about Lockheed integrating digital C2 with the first JFN prototype at Valiant Shield 2024 (June 2024) and JFN's sensor-to-weapon-system purpose, but does not mention the 'combat-representative 1.0' end-of-2024 target or the specific 'All In' program details (Aegis, F-35, hypersonics, Australia, Japan, ROK).
  > _"Lockheed Martin successfully integrated digital command and control (C2) capabilities with the first version of the Pentagon's Joint Fires Network during the exercise... Valiant Shield marks the first test of the initial Joint Fires Network prototype, which will provide crucial insights for the Pentagon's ongoing CJADC2 efforts."_
  - Missing in this source: 1) The claim that JFN is specifically an 'INDOPACOM initiative' — the source calls it 'the Pentagon's Joint Fires Network,' not an INDOPACOM initiative. 2) The claim that JFN is designed to network 'any sensor to any weapon system' — not stated in the source. 3) The targeted 'combat-representative 1.0' version by end of 2024 — not mentioned in the source. 4) The 'All In' framing with explicit investment callouts for JADC2, Aegis, F-35, hypersonics, and specific partner nations (Australia, Japan, ROK) — the source uses 'All In' in the title but does not explicitly enumerate these programs and nations in the extracted content.
  - Model note: The source supports the core claim about Lockheed integrating its digital C2 platform with the first JFN prototype at Valiant Shield 2024 in June 2024 and the 'All In' framing, but does not support several specific sub-claims including JFN being an INDOPACOM (vs. Pentagon) initiative, the 'any sensor to any weapon' description, the end-of-2024 'combat-representative 1.0' target, or the explicit enumeration of programs and partner nations.

### ⚑ FACT #13 §5  —  **PARTIAL**

**Claim:**
> L3Harris demonstrated its **Distributed Spectrum Collaboration and Operations (DiSCO™)** cloud-connected Electromagnetic Spectrum Operations architecture at Valiant Shield 2024 — sharing real-time RF signal data between Joint Base Pearl Harbor-Hickam (Hawaii) and EW payloads in Hawaii and San Diego, including small payloads on two Seasats Lightfish autonomous surface vehicles [s.2026-05-12-l3harri…

**Citations:** [s.2026-05-12-l3harris-demonstrates-disco-el] [s.2026-05-12-l3harris-demonstrates-autonomo]

**Sources checked:**
- `[s.2026-05-12-l3harris-demonstrates-disco-el]` → `01_sources/2026-05-12_l3harris-com_l3harris-demonstrates-disco-electronic-warfare-operations-du.md` — verdict: **PARTIAL** ([source](https://www.l3harris.com/newsroom/press-release/2024/07/l3harris-demonstrates-electronic-warfare-valiant-shield-2024))
- `[s.2026-05-12-l3harris-demonstrates-autonomo]` → `01_sources/2026-05-12_l3harris-com_l3harris-demonstrates-autonomous-ew-capability-with-shield-a.md` — verdict: **PARTIAL** ([source](https://www.l3harris.com/newsroom/press-release/2026/04/l3harris-demonstrates-autonomous-electronic-warfare-capability))
  > _"During the exercise, DiSCO successfully shared real-time radio frequency signal data between Joint Base Pearl Harbor-Hickam, Hawaii, and multiple EW payloads operating in Hawaii and in San Diego, California. Small form-factor payloads operated on two Seasats' autonomous surface vehicles along with satellite communications links at both locations."_
  - Missing in this source: The source does not mention 'Lightfish' as the name of the Seasats autonomous surface vehicles (refers to them only as 'Seasats' autonomous surface vehicles'). More significantly, the source contains no information about the April 2026 demonstration with Shield AI integrating DiSCO with Shield AI's Hivemind autonomy software for autonomous EW — detecting, analyzing and responding to electromagnetic threats without human intervention.
  - Model note: The source fully supports the Valiant Shield 2024 portion of the claim (DiSCO, cloud-connected EMSO architecture, real-time RF data sharing between JBPHH and Hawaii/San Diego, two Seasats ASVs) except for the specific 'Lightfish' vehicle name, but contains no reference whatsoever to the April 2026 Shield AI/Hivemind integration described in the second sentence of the claim.
  > _"Operating within the Distributed Spectrum Collaboration and Operations (DiSCO™) ecosystem, the Deceptor system enabled coordinated, AI-enabled sensing and effects across the battlespace. The integrated system also detected and geolocated radio frequency (RF) threats, fused data from multiple sensors in real time, and executed RF jamming to neutralize those threats."_
  - Missing in this source: 1) The source does not mention Shield AI or Hivemind autonomy software at all. 2) The source does not mention Valiant Shield 2024, Joint Base Pearl Harbor-Hickam, San Diego, or Seasats Lightfish autonomous surface vehicles. 3) The source describes a 'U.S. Army experiment' with UAVs (Deceptor on unmanned aerial systems), not cloud-connected architecture sharing RF signal data between Hawaii and San Diego. 4) The April 2026 date is supported, but the specific Shield AI/Hivemind integration claim is entirely absent from the source.
  - Model note: The source confirms the April 2026 DiSCO autonomous EW demonstration involving detection, analysis, and RF jamming of threats, but does not mention Shield AI, Hivemind, Valiant Shield 2024, the Hawaii/San Diego geographic elements, or the Seasats Lightfish vehicles that are central to the claim.

### ⚑ FACT #14 §5  —  **PARTIAL**

**Claim:**
> Northrop Grumman demonstrated capabilities in Indo-Pacific region exercises enabling joint force detection, location, tracking and engagement of adversarial threats at sea, in the air, on land, and in cyberspace [s.2026-05-12-northrop-grumman-demonstrates-]. In April 2026, Japan announced a collaboration with Northrop Grumman to enhance EW capabilities including data optimization, threat simulatio…

**Citations:** [s.2026-05-12-northrop-grumman-demonstrates-] [s.2026-05-12-japan-teams-with-northrop-grum]

**Sources checked:**
- `[s.2026-05-12-northrop-grumman-demonstrates-]` → `01_sources/2026-05-12_news-northropgrumman-com_northrop-grumman-demonstrates-critical-capabilities-in-indo.md` — verdict: **PARTIAL** ([source](https://news.northropgrumman.com/global/northrop-grumman-demonstrates-critical-capabilities-in-indo-pacific-region-exercises))
- `[s.2026-05-12-japan-teams-with-northrop-grum]` → `01_sources/2026-05-12_thedefensepost-com_japan-teams-with-northrop-grumman-to-boost-electronic-warfar.md` — verdict: **PARTIAL** ([source](https://thedefensepost.com/2026/04/28/japan-northrop-grumman-electronic-warfare/))
  > _"Capabilities enabled by Northrop Grumman technologies allowed the Joint Force to practice real-world efficiency in detecting, locating, tracking and engaging adversarial threats at sea, in the air, on land and in cyberspace."_
  - Missing in this source: The source contains no mention of: (1) Japan announcing a collaboration with Northrop Grumman in April 2026; (2) any EW (electronic warfare) capabilities collaboration including data optimization, threat simulation, or the full EW cycle; (3) any explicit motivation related to Indo-Pacific tensions with China around Taiwan or the South China Sea.
  - Model note: The source supports the first part of the claim regarding joint force detection, location, tracking, and engagement of adversarial threats in multiple domains during Indo-Pacific exercises, but contains no evidence whatsoever for the April 2026 Japan-Northrop Grumman EW collaboration or its stated geopolitical motivations.
  > _"Japan is moving towards further enhancing its electronic warfare (EW) capabilities through a collaboration with US defense giant Northrop Grumman. Both are exploring joint efforts to build local capabilities, as well as data optimization and threat simulation, to strengthen Tokyo's ability to handle the entire EW cycle from enemy detection, exploitation, deception, and denial, as well as protectio…"_
  - Missing in this source: The first part of the claim — that Northrop Grumman demonstrated capabilities in Indo-Pacific region exercises enabling joint force detection, location, tracking and engagement of adversarial threats at sea, in the air, on land, and in cyberspace — is not mentioned anywhere in the source. The source also does not specify 'April 2026' as the date Japan announced the collaboration (the article is dated April 28, 2026, but does not explicitly state the announcement was made in April 2026).
  - Model note: The source supports the Japan-Northrop Grumman EW collaboration details and the Indo-Pacific/China/Taiwan/South China Sea motivations, but does not contain any reference to multi-domain (sea, air, land, cyberspace) exercise demonstrations described in the first sentence of the claim.

### ⚑ FACT #15 §5  —  **PARTIAL**

**Claim:**
> RTX (Raytheon) delivered the first Next Generation Jammer (NGJ) shipsets to the Royal Australian Air Force in April 2026; NGJ is a cooperative U.S.–RAAF development program providing airborne electronic attack via active electronically scanned arrays in the mid-band frequency range, disrupting enemy radars and comms to keep aircrew undetected [s.2026-05-12-rtx-raytheon-delivers-first-ne]. RTX's Ad…

**Citations:** [s.2026-05-12-rtx-raytheon-delivers-first-ne] [s.2026-05-12-rtx-advanced-electronic-warfar]

**Sources checked:**
- `[s.2026-05-12-rtx-raytheon-delivers-first-ne]` → `01_sources/2026-05-12_rtx-com_rtx-raytheon-delivers-first-next-generation-jammer-shipsets.md` — verdict: **PARTIAL** ([source](https://www.rtx.com/news/news-center/2026/04/20/rtxs-raytheon-delivers-first-next-generation-jammer-shipsets-to-the-royal-austra))
- `[s.2026-05-12-rtx-advanced-electronic-warfar]` → `01_sources/2026-05-12_rtx-com_rtx-advanced-electronic-warfare-prototype-for-f-a-18e-f-supe.md` — verdict: **PARTIAL** ([source](https://www.rtx.com/news/news-center/2025/09/22/rtxs-advanced-electronic-warfare-prototype-for-f-a-18e-f-super-hornet-passes-cri))
  > _"Raytheon, an RTX (NYSE: RTX) business, has delivered its first Next Generation Jammer (NGJ) pods to the Royal Australian Air Force. NGJ is a cooperative development and production program with the Royal Australian Air Force (RAAF). It is an airborne electronic attack system containing active electronically scanned arrays that radiate in the mid-band frequency range. By disrupting enemy radars and …"_
  - Missing in this source: The claim states delivery occurred 'in April 2026,' but the source states 'This first delivery of shipsets occurred ahead of schedule in September 2025' — the April 2026 date in the claim appears to be the press release/announcement date, not the delivery date. Additionally, the claim about RTX's Advanced Electronic Warfare (ADVEW) prototype for the F/A-18E/F Super Hornet passing critical review in September 2025 and being positioned to replace current EW systems is entirely absent from the source.
  - Model note: The source supports the NGJ program description (cooperative U.S.-RAAF, airborne EW, AESA, mid-band, disrupting radars/comms) but contradicts the claimed April 2026 delivery date (source says September 2025), and contains no mention whatsoever of the ADVEW prototype or its critical review.
  > _"Raytheon, an RTX (NYSE: RTX) business, has successfully completed a major review of its new Advanced Electronic Warfare (ADVEW) prototype for the U.S. Navy's F/A-18E/F Super Hornet. This new system is set to replace current electronic warfare systems on the aircraft to enhance its defensive capabilities and survivability."_
  - Missing in this source: The source contains no mention of: (1) RTX delivering the first Next Generation Jammer (NGJ) shipsets to the Royal Australian Air Force in April 2026; (2) NGJ being a cooperative U.S.–RAAF development program; (3) NGJ using active electronically scanned arrays in the mid-band frequency range; (4) NGJ disrupting enemy radars and comms. The source also does not specify 'September 2025' as the date of the critical review (though the URL and press release date of Sept. 22, 2025 imply it), and it does not describe ADVEW as being 'positioned to replace current EW systems' in those exact terms (though it does say the system is 'set to replace current electronic warfare systems').
  - Model note: The source fully supports the ADVEW portion of the claim (critical review passed, September 2025, replaces current EW systems on F/A-18E/F), but contains absolutely no information about the NGJ program, the RAAF delivery, cooperative development, AESA technology, or mid-band frequency range described in the first part of the claim.

### ✗ FACT #16 §5  —  **DOES_NOT_SUPPORT**

**Claim:**
> Johns Hopkins APL is publicly named as a PMTEC partner. The January 2026 Indo-Pacific Defense FORUM article *"PMTEC pioneers AI-enabled warfare capabilities"* documents APL's role in PMTEC's AI/digital-twin research [s.2026-05-12-pmtec-pioneers-ai-enabled-warf].

**Citations:** [s.2026-05-12-pmtec-pioneers-ai-enabled-warf]

**Sources checked:**
- `[s.2026-05-12-pmtec-pioneers-ai-enabled-warf]` → `01_sources/2026-05-12_ipdefenseforum-com_pmtec-pioneers-ai-enabled-warfare-capabilities-indo-pacific.md` — verdict: **DOES_NOT_SUPPORT** ([source](https://ipdefenseforum.com/2026/01/pmtec-pioneers-ai-enabled-warfare-capabilities/))
  - Missing in this source: The source does not mention Johns Hopkins APL (Applied Physics Laboratory) anywhere in the article, nor does it reference APL's role in PMTEC's AI or digital-twin research. The article's collaborative partners mentioned are the Defense Innovation Unit and the Pacific Impact Zone, with no mention of APL.
  - Model note: The source article covers PMTEC's AI integration activities but makes no reference to Johns Hopkins APL as a named partner or contributor to any AI/digital-twin research.

### ⚑ FACT #17 §6  —  **PARTIAL**

**Claim:**
> Deloitte holds GSA OASIS delivery order **PIID `47QFCA25F0010`** (parent IDIQ `GS00Q14OADU113`, the OASIS Unrestricted Pool Professional Services Multiple Agency Contract) supporting USINDOPACOM with enterprise-wide professional services. Period start **2025-03-01**; current period end (Year 1) **2026-07-31**; place of performance **Hawaii** (Camp H.M. Smith). Obligated to date: **$58,923,548** [s…

**Citations:** [s.2026-05-11-indopacom-alpha-deloitte]

**Sources checked:**
- `[s.2026-05-11-indopacom-alpha-deloitte]` → `01_sources/2026-05-11_usaspending-gov_indopacom-alpha-deloitte.md` — verdict: **PARTIAL** ([source](https://www.usaspending.gov/award/CONT_AWD_47QFCA25F0010_4732_GS00Q14OADU113_4732/))
  > _"PIID: 47QFCA25F0010 ... Parent IDIQ (vehicle): PIID: GS00Q14OADU113 ... Description: ONE ACQUISITION SOLUTION FOR INTEGRATED SERVICES (OASIS) PROFESSIONAL SERVICES MULTIPLE AGENCY CONTRACT ... Recipient Name: DELOITTE CONSULTING LLP ... Total obligation to date: $58,923,548 ... Place of performance: Hawaii (state code HI) ... Period start: 2025-03-01 ... Period current end (Year 1): 2026-07-31"_
  - Missing in this source: The claim states the parent IDIQ is specifically 'OASIS Unrestricted Pool Professional Services Multiple Agency Contract' — the source confirms OASIS but does not explicitly label it as 'Unrestricted Pool' in the extracted FPDS description. The claim also states place of performance as 'Camp H.M. Smith' specifically — the source shows only Hawaii (state HI; city not reported), with Camp H.M. Smith noted as an inference. The source explicitly notes that 'base_and_all_options_value' is null, so the ceiling and final option-period end date beyond Year 1 are not verified by the USAspending record. The claim's statement that the USAspending API record 'corroborates awardee, vehicle, customer, place of performance, and start date' is itself supported, but the specific 'Unrestricted Pool' label and 'Camp H.M. Smith' city-level place of performance are not explicitly confirmed.
  - Model note: The source supports all core numerical and identifier elements of the claim (PIID, parent IDIQ, awardee, obligation, period start, Year 1 end, Hawaii PoP, USINDOPACOM customer) but does not explicitly confirm the 'Unrestricted Pool' pool designation or the specific Camp H.M. Smith location, only inferring the latter.

### ⚑ FACT #18 §6  —  **PARTIAL**

**Claim:**
> PACAF Base Area Network modernization — $180M, 5-yr task order on AFBIM IDIQ awarded Sep 2025. Direct PACAF/INDOPACOM IT backbone with Zero Trust foundation [s.govconwire-sep2025-caci-afbim] [s.2026-05-12-caci-to-modernize-air-force-ba]. *Single-sourced — verify via USAspending (search Deloitte/CACI AFBIM 2025) and CACI IR.*

**Citations:** [s.govconwire-sep2025-caci-afbim] [s.2026-05-12-caci-to-modernize-air-force-ba]

**Sources checked:**
- `[s.govconwire-sep2025-caci-afbim]` → ⚠ not in `01_sources/` (cited only in §8.2)
- `[s.2026-05-12-caci-to-modernize-air-force-ba]` → `01_sources/2026-05-12_washingtonexec-com_caci-to-modernize-air-force-base-networks-in-pacific-under-1.md` — verdict: **PARTIAL** ([source](https://washingtonexec.com/2025/09/caci-to-modernize-air-force-base-networks-in-pacific-under-180m-task-order/))
  > _"CACI International has received a 5-year task order worth up to $180 million to provide secure and stable network operations for Pacific Air Forces in support of U.S. Indo-Pacific Command."_
  - Missing in this source: The source does not explicitly confirm the IDIQ vehicle name as 'AFBIM IDIQ', does not confirm the award date as September 2025 (article is dated September 17, 2025, but no explicit award date is stated in the extracted content), and does not mention 'single-sourced' or reference Deloitte. The Zero Trust foundation element is supported by the CEO quote as a future capability ('lay the foundation for enhanced capabilities like Zero Trust security') rather than a current foundational element.
  - Model note: The source supports the core facts ($180M, 5-year, CACI, PACAF/INDOPACOM, Base Area Network modernization, Zero Trust mentioned) but does not explicitly name the IDIQ as 'AFBIM IDIQ' by that exact designation, nor confirm a specific September 2025 award date beyond the article's publication date.

### ⚑ FACT #19 §6  —  **PARTIAL**

**Claim:**
> Spectral (NAVWAR) — $1.2B ceiling, shipboard SIGINT/EW/IO. $143M Spectral Enabling Kits delivery order May 2025 [s.bizwire-may2025-spectral] [s.2026-05-12-caci-mission-critical-technolo]. *Single-sourced — verify via CACI IR.*

**Citations:** [s.bizwire-may2025-spectral] [s.2026-05-12-caci-mission-critical-technolo]

**Sources checked:**
- `[s.bizwire-may2025-spectral]` → ⚠ not in `01_sources/` (cited only in §8.2)
- `[s.2026-05-12-caci-mission-critical-technolo]` → `01_sources/2026-05-12_businesswire-com_caci-mission-critical-technology-will-accelerate-delivery-of.md` — verdict: **PARTIAL** ([source](https://www.businesswire.com/news/home/20250507187909/en/CACIs-Mission-Critical-Technology-will-Accelerate-the-Delivery-of-Electronic-Warfighting-Capabilities-to-the-U.S.-Navys-Existing-Fleet))
  > _"The $143 million firm-fixed-price delivery order represents a new phase of work on the CACI's existing Spectral contract with the Naval Information Warfare Systems Command (NAVWAR) which is authorized with a $1.2 billion ceiling value."_
  - Missing in this source: The claim states the delivery order was awarded 'May 2025'; the source does not include a publication date to confirm this. The 'single-sourced — verify via CACI IR' notation is a meta-instruction not verifiable from the source itself.
  - Model note: The source explicitly confirms the $1.2B ceiling, NAVWAR, shipboard SIGINT/EW/IO mission, and $143M Spectral Enabling Kits delivery order, but the publication date field is blank so the 'May 2025' date cannot be confirmed from the source text alone.

### ✓ FACT #20 §6  —  **SUPPORTS**

**Claim:**
> Trojan EATS (Army DEVCOM, OASIS) — $382M, 5-yr; SIGINT/EW open-architecture systems [s.caci-ir-trojan-2024] [s.2026-05-12-u-s-army-selects-caci-for-382-].

**Citations:** [s.caci-ir-trojan-2024] [s.2026-05-12-u-s-army-selects-caci-for-382-]

**Sources checked:**
- `[s.caci-ir-trojan-2024]` → ⚠ not in `01_sources/` (cited only in §8.2)
- `[s.2026-05-12-u-s-army-selects-caci-for-382-]` → `01_sources/2026-05-12_businesswire-com_u-s-army-selects-caci-for-382-million-signals-intelligence-a.md` — verdict: **SUPPORTS** ([source](https://www.businesswire.com/news/home/20240123940984/en/U.S.-Army-Selects-CACI-for-%24382-Million-Signals-Intelligence-and-Electronic-Warfare-Systems-Task-Order))
  > _"CACI International Inc (NYSE: CACI) announced today that it won a five-year, single-award task order valued at up to $382 million to provide technology to the U.S. Army Combat Capabilities Development Command (DEVCOM) Engineering and Systems Integration Directorate (ESID) Trojan Engineering and Systems Integration (ESI) Advancement of Trojan Systems (EATS). This work is part of the One Acquisition…"_
  - Model note: The source explicitly confirms all elements of the claim: Trojan EATS program name, Army DEVCOM, OASIS contract vehicle, $382M value, 5-year duration, and SIGINT/EW open-architecture systems focus.

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
  - Missing in this source: The claim states ARKA adds capabilities for 'SIGINT/EW' (Signals Intelligence / Electronic Warfare). The source mentions ARKA's geospatial intelligence 'complements CACI's strong position providing signals intelligence,' but does not state ARKA itself adds SIGINT or EW capabilities — only EO/IR, hyperspectral imaging, and Agentic AI for geospatial intelligence. The claim's characterization of satellite sensors as SIGINT/EW is not explicitly supported; the source describes space-based sensors as EO/IR and hyperspectral (optical/imaging), not SIGINT or EW sensors.
  - Model note: The source supports the acquisition close date (March 9, 2026), the $2.6B price, space-based sensors, and agentic AI, but the claim's attribution of SIGINT/EW capabilities to ARKA is not explicitly supported — the source ties SIGINT to CACI's existing portfolio, not ARKA's added capabilities, and ARKA's sensors are optical/imaging rather than SIGINT/EW.
  > _"During the third quarter, we closed the acquisition of ARKA, a leading technology company focused on national security missions in the space domain. ARKA brings exquisite space-based imaging sensor technology with high technical barriers to entry, agentic AI-based ground processing software, and deep customer relationships built over decades of strong performance."_
  - Missing in this source: The claim states the acquisition closed in 'March 2026' and cost '$2.6B'. The source confirms the acquisition closed 'during the third quarter' (CACI's Q3 FY2026, which ended around March 2026) but does not explicitly state March 2026 as the closing month. The source also does not mention a $2.6B acquisition price anywhere. Additionally, the claim specifically mentions 'SIGINT/EW' as a capability added, but the source describes space-based imaging sensors and agentic AI for ground processing, not explicitly SIGINT/EW (though SPECTRAL is a separate SIGINT/EW program unrelated to ARKA).
  - Model note: The source supports the acquisition closing in Q3 FY2026 and the addition of satellite/space-based imaging sensors and agentic AI, but does not provide the $2.6B price or explicitly link ARKA to SIGINT/EW capabilities.
  - Missing in this source: The source contains no mention of ARKA acquisition, $2.6B deal, March 2026 close date, satellite sensors, agentic AI, SIGINT, or EW. The 8-K is solely about an amendment to a Master Accounts Receivable Purchase Agreement.
  - Model note: The source document is a CACI 8-K filed December 29, 2025 regarding Amendment No. 7 to a receivables purchase agreement with MUFG Bank, and contains absolutely no content related to an ARKA Group acquisition or any of the claim's elements.
  > _"On March 9, 2026, CACI acquired all of the equity interests of ARKA Group L.P. (ARKA) for purchase consideration of approximately $2,642.7 million, net of cash acquired, subject to post closing adjustments. This acquisition will enhance CACI's ability to deliver advanced technology for its national security customers in the space domain."_
  - Missing in this source: The source does not mention 'satellite sensors,' 'agentic AI,' 'SIGINT,' or 'EW (Electronic Warfare)' capabilities as part of the ARKA acquisition. The source only references 'advanced technology for national security customers in the space domain.' The $2.6B figure is supported (~$2,642.7M rounds to ~$2.6B) and the March 2026 close date is confirmed (March 9, 2026).
  - Model note: The source confirms the acquisition date (March 9, 2026) and approximate price ($2,642.7M ≈ $2.6B), but does not explicitly mention satellite sensors, agentic AI, SIGINT, or EW as capabilities added through the ARKA acquisition.


# FACT Verification Report — BDR-FLEET-READINESS

*Generated 2026-05-26T12:52:24 by `verify_facts.py` (model: `claude-sonnet-4-6`)*

## Summary

- **38** FACT claims scanned
- **20** SUPPORTS — claim is corroborated by an ingested source
- **14** PARTIAL — some elements supported by an ingested source
- **4** DOES_NOT_SUPPORT — ingested source contradicts or omits the claim
- **0** UNVERIFIABLE — cited source(s) not yet in 01_sources/

## Verifications

### ✓ FACT #1 §3  —  **SUPPORTS**

**Claim:**
> Admiral Daryl L. Caudle, the Chief of Naval Operations, delivered a Statement on the Posture of the United States Navy before the House Armed Services Committee (HASC) on 14 May 2026, addressing FY27 budget content [s.2026-05-26-2026-05-14-caudle-testimony].

**Citations:** [s.2026-05-26-2026-05-14-caudle-testimony]

**Sources checked:**
- `[s.2026-05-26-2026-05-14-caudle-testimony]` → `01_sources/2026-05-26_armedservices-house-gov_2026-05-14-caudle-testimony.md` — verdict: **SUPPORTS** ([source](https://armedservices.house.gov/uploadedfiles/2026-05-14_caudle_testimony.pdf))
  > _"STATEMENT OF ADMIRAL DARYL L. CAUDLE CHIEF OF NAVAL OPERATIONS ON THE POSTURE OF THE UNITED STATES NAVY BEFORE THE HOUSE ARMED SERVICES COMMITTEE May 14, 2026"_
  - Model note: The source explicitly confirms Admiral Daryl L. Caudle as Chief of Naval Operations delivered a Statement on the Posture of the United States Navy before the House Armed Services Committee on May 14, 2026, and the document contains FY27 budget content throughout (e.g., 'CNO Investment Objectives for Fiscal Year 2027' and multiple 'PB-27' references).

### ✓ FACT #2 §3  —  **SUPPORTS**

**Claim:**
> The Caudle HASC testimony announces a planned deliberate study of Navy yard capacity, examining shortfalls, future force requirements, and operational considerations, and emphasizes maintenance as a warfighting requirement [s.2026-05-26-2026-05-14-caudle-testimony].

**Citations:** [s.2026-05-26-2026-05-14-caudle-testimony]

**Sources checked:**
- `[s.2026-05-26-2026-05-14-caudle-testimony]` → `01_sources/2026-05-26_armedservices-house-gov_2026-05-14-caudle-testimony.md` — verdict: **SUPPORTS** ([source](https://armedservices.house.gov/uploadedfiles/2026-05-14_caudle_testimony.pdf))
  > _"We're also taking a hard look at whether we need a new public Navy Yard. In the FY27 budget, we've resourced a deliberate study to close the gap between the maintenance capacity we have and the maintenance demand we know is coming. That work looks at three things: the shortfall we're carrying today, the requirements of the future force, and where a new yard would make operational sense - based on …"_
  - Model note: The source directly and explicitly supports all elements of the claim: a deliberate study is resourced in FY27, it examines shortfalls, future force requirements, and operational considerations (where a new yard would make operational sense), and the testimony explicitly states 'Maintenance is not a back-end function - it is a warfighting requirement.'

### ✓ FACT #3 §3  —  **SUPPORTS**

**Claim:**
> The Department of the Navy's FY 2027 President's Budget Press Brief, dated 28 April 2026, funds Ship Maintenance at $17.0 billion (including Other Procurement, Navy) explicitly to drive the fleet toward an *"80% Combat Surge Ready (CSR) posture by reducing maintenance delays and applying a disciplined focus across manning, training, modernization, and sustainment"* [s.2026-05-26-don-fy27-press-bri…

**Citations:** [s.2026-05-26-don-fy27-press-brief]

**Sources checked:**
- `[s.2026-05-26-don-fy27-press-brief]` → `01_sources/2026-05-26_secnav-navy-mil_don-fy27-press-brief.md` — verdict: **SUPPORTS** ([source](https://www.secnav.navy.mil/fmc/fmb/Documents/27pres/DON_Press_Brief.pdf))
  > _"Ship Maintenance, $17.0B (Includes OPN): We are driving platform readiness towards an 80% Combat Surge Ready (CSR) posture by reducing maintenance delays and applying a disciplined focus across manning, training, modernization, and sustainment."_
  - Model note: The source explicitly states the $17.0B Ship Maintenance figure (including OPN), the 80% CSR posture goal, the mechanism of reducing maintenance delays, and the four focus areas (manning, training, modernization, and sustainment), in a document dated 28 April 2026 from the Department of the Navy PB 2027 Press Brief — all elements of the claim are directly supported verbatim.

### ⚑ FACT #4 §3  —  **PARTIAL**

**Claim:**
> The DON FY27 Press Brief includes a separate $0.6 billion line item for Contested Logistics, justified explicitly because *"adversaries will target supply lines, ports, and communications"* [s.2026-05-26-don-fy27-press-brief]. *Scope note:* the Contested Logistics line item funds physical logistics resilience (spares, fuel distribution, lift capability, port-security assets), not training scenario…

**Citations:** [s.2026-05-26-don-fy27-press-brief]

**Sources checked:**
- `[s.2026-05-26-don-fy27-press-brief]` → `01_sources/2026-05-26_secnav-navy-mil_don-fy27-press-brief.md` — verdict: **PARTIAL** ([source](https://www.secnav.navy.mil/fmc/fmb/Documents/27pres/DON_Press_Brief.pdf))
  > _"Contested Logistics $0.6B: Logistics are vulnerable in a contested environment as adversaries will target supply lines, ports, and communications. Shifting to a resilient, AI-enabled, "just-in-case" logistics network is essential to sustain forces under attack. Leveraging the C-C5ISR-T umbrella and defending against cyber disruption enhances logistics command and control and self-sufficiency."_
  - Missing in this source: The scope note in the claim asserts that the Contested Logistics line item 'funds physical logistics resilience (spares, fuel distribution, lift capability, port-security assets), not training scenarios.' The source does not explicitly enumerate those sub-categories (spares, fuel distribution, lift capability, port-security assets) nor does it explicitly exclude training scenarios; the source text emphasizes a 'resilient, AI-enabled, just-in-case logistics network,' cyber defense, and C2 self-sufficiency, which does not fully confirm or deny the physical-logistics-only scope described in the claim's scope note.
  - Model note: The $0.6B figure, the separate line-item status, and the verbatim justification quote ('adversaries will target supply lines, ports, and communications') are all directly supported by Page 13 of the source, but the claim's scope note characterizing the line item as funding only physical logistics resilience (and not training) is an interpretive assertion not explicitly stated in the source.

### ✓ FACT #5 §3  —  **SUPPORTS**

**Claim:**
> The DON FY27 Press Brief lists 37 Forward Deployed Naval Forces (FDNF) ships per the same artifact [s.2026-05-26-don-fy27-press-brief]. **Assessment.** Senior leadership is naming Combat Surge Ready posture as the target readiness metric and naming contested logistics as the threat environment for fleet sustainment. Both signals describe the operational context the corrected-scope product would tr…

**Citations:** [s.2026-05-26-don-fy27-press-brief]

**Sources checked:**
- `[s.2026-05-26-don-fy27-press-brief]` → `01_sources/2026-05-26_secnav-navy-mil_don-fy27-press-brief.md` — verdict: **SUPPORTS** ([source](https://www.secnav.navy.mil/fmc/fmb/Documents/27pres/DON_Press_Brief.pdf))
  > _"37 FORWARD DEPLOYED NAVAL FORCES"_
  - Model note: Page 4 of the source explicitly states '37 FORWARD DEPLOYED NAVAL FORCES' matching the claim's figure exactly, and the source is confirmed to be the DON FY27 Press Brief.

### ⚑ FACT #6 §3  —  **PARTIAL**

**Claim:**
> U.S. Seventh Fleet, the Ship Repair Facility–Japan Regional Maintenance Center (SRF-JRMC), U.S. Pacific Command (USINDOPACOM), and U.S. Pacific Fleet (COMPACFLT) all published parallel releases announcing that USS Ashland (LSD 48) completed Ship Wartime Repair and Maintenance in Cebu, Philippines, in coordination with Philippine Navy partners and local Philippine contractors [s.2026-05-26-uss-ashl…

**Citations:** [s.2026-05-26-uss-ashland-completes-ship-war]

**Sources checked:**
- `[s.2026-05-26-uss-ashland-completes-ship-war]` → `01_sources/2026-05-26_cpf-navy-mil_uss-ashland-completes-ship-wartime-repair-and-maintenance-ex.md` — verdict: **PARTIAL** ([source](https://www.cpf.navy.mil/Newsroom/News/Article/4452493/uss-ashland-completes-ship-wartime-repair-and-maintenance-in-philippines/))
  > _"Ashland and embarked Marines from I Marine Expeditionary Force make up Task Force (TF) Ashland, which is conducting routine operations in U.S. 7th Fleet."_
  - Missing in this source: The source only mentions U.S. 7th Fleet as the publishing/relevant command; it does not mention SRF-JRMC, USINDOPACOM, or COMPACFLT publishing parallel releases. The source also does not explicitly name Cebu as the location, does not mention 'local Philippine contractors,' and refers to the event as an 'Exercise' (Ship Wartime Repair and Maintenance Exercise) rather than simply 'Ship Wartime Repair and Maintenance' as stated in the claim.
  - Model note: The source confirms USS Ashland completed a Ship Wartime Repair and Maintenance exercise in the Philippines with Philippine allies under U.S. 7th Fleet, but does not support the claim that SRF-JRMC, USINDOPACOM, and COMPACFLT all published parallel releases, does not specify Cebu as the location, and does not mention local Philippine contractors.

### ✓ FACT #7 §3  —  **SUPPORTS**

**Claim:**
> Naval News covered the same SWARMEX-Cebu event and named Philippine Naval Sea Systems Command participation [s.2026-05-26-u-s-navy-rehearses-wartime-rep].

**Citations:** [s.2026-05-26-u-s-navy-rehearses-wartime-rep]

**Sources checked:**
- `[s.2026-05-26-u-s-navy-rehearses-wartime-rep]` → `01_sources/2026-05-26_navalnews-com_u-s-navy-rehearses-wartime-repairs-in-central-philippine-por.md` — verdict: **SUPPORTS** ([source](https://www.navalnews.com/naval-news/2026/04/u-s-navy-rehearses-wartime-repairs-in-central-philippine-port/))
  > _"Philippine Naval Sea Systems Command personnel and local contractors participated in the exercise."_
  - Model note: The Naval News source explicitly covers the SWARMEX-Cebu event (wartime repairs exercise at Cebu South Port) and names Philippine Naval Sea Systems Command participation, directly supporting both elements of the claim.

### ✓ FACT #8 §3  —  **SUPPORTS**

**Claim:**
> The SWARMEX-Cebu exercise involved an amphibious warfare ship operating at a foreign port, host-nation contractor coordination for repair work, and Philippine naval participation [s.2026-05-26-u-s-navy-rehearses-wartime-rep].

**Citations:** [s.2026-05-26-u-s-navy-rehearses-wartime-rep]

**Sources checked:**
- `[s.2026-05-26-u-s-navy-rehearses-wartime-rep]` → `01_sources/2026-05-26_navalnews-com_u-s-navy-rehearses-wartime-repairs-in-central-philippine-por.md` — verdict: **SUPPORTS** ([source](https://www.navalnews.com/naval-news/2026/04/u-s-navy-rehearses-wartime-repairs-in-central-philippine-port/))
  > _"USS Ashland (LSD-48), a Whidbey Island-class landing ship dock, conducted the simulated wartime repairs at Cebu South Port... Philippine Naval Sea Systems Command personnel and local contractors participated in the exercise."_
  - Model note: The source confirms all three elements of the claim: an amphibious warfare ship (USS Ashland, LSD-48) operating at a foreign port (Cebu South Port, Philippines), host-nation contractor coordination for repair work (local contractors), and Philippine naval participation (Philippine Naval Sea Systems Command personnel).

### ⚑ FACT #9 §3  —  **PARTIAL**

**Claim:**
> A Defense Visual Information Distribution Service (DVIDS) news release covered USS Iwo Jima's damage controlmen training the crew in simulated casualty scenarios (flooding, fire, hull rupture) for shipboard damage control [s.2026-05-26-dvids-news-dont-give-up-the-sh]. *Scope note:* This is shipboard organic damage control at the deck-plate level, which is exactly the layer the 2026-05-26 scope cor…

**Citations:** [s.2026-05-26-dvids-news-dont-give-up-the-sh]

**Sources checked:**
- `[s.2026-05-26-dvids-news-dont-give-up-the-sh]` → `01_sources/2026-05-26_dvidshub-net_dvids-news-dont-give-up-the-ship-how-iwo-jimas-damage-contro.md` — verdict: **PARTIAL** ([source](https://www.dvidshub.net/news/563966/dont-give-up-ship-iwo-jimas-damage-controlmen-prepare-crew-engage-casualties))
  > _"This is one of the training scenarios ran during a damage control training evolution aboard Wasp-class amphibious assault ship USS Iwo Jima (LHD 7). Each evolution is meticulously designed to enhance a Sailor's understanding and reaction to real-world events such as flooding, fire, gas leak, or a hull rupture."_
  - Missing in this source: The source does not contain any content about SWARMEX-Cebu, forward team mobilization to damaged ships, emergency contracting in foreign ports, host-nation legal and operational frameworks, the §1 decision moments, the §11.3 BDAT pipeline, or any assessment-team/repair-team operational-decision layer. The claim's 'Assessment' paragraph about SWARMEX-Cebu mapping onto decision moments and the §11.3 rebuild around SWARMEX-class exercises is entirely unsupported by the source.
  - Model note: The source supports only the narrow factual assertion that DVIDS published a news release about USS Iwo Jima's damage controlmen training the crew in simulated casualty scenarios (flooding, fire, hull rupture); the extensive 'Assessment' portion of the claim referencing SWARMEX-Cebu, the six decision moments, and the §11.3 BDAT pipeline finds zero support in the source.

### ✓ FACT #10 §3  —  **SUPPORTS**

**Claim:**
> The U.S. Naval Institute's professional journal Proceedings published an article titled *"Fix the Navy's Expeditionary Repair"* arguing that the current expeditionary repair capability is inadequate to support fleet operations under wartime contestation conditions [s.2026-05-26-fix-the-navys-expeditionary-re].

**Citations:** [s.2026-05-26-fix-the-navys-expeditionary-re]

**Sources checked:**
- `[s.2026-05-26-fix-the-navys-expeditionary-re]` → `01_sources/2026-05-26_usni-org_fix-the-navys-expeditionary-repair.md` — verdict: **SUPPORTS** ([source](https://www.usni.org/magazines/proceedings/2025/march/fix-navys-expeditionary-repair))
  > _"Of those, repair is the least understood and most in need of the Navy's attention... a shortage of organic expeditionary repair capability... The Navy must change its approach to the repair vector and make the necessary doctrinal and organizational changes to enable this capability."_
  - Model note: The source is the article 'Fix the Navy's Expeditionary Repair' published in USNI Proceedings (March 2025), and it explicitly argues that current expeditionary repair capability is inadequate to sustain fleet operations under contested/wartime conditions, supporting all elements of the claim.

### ⚑ FACT #11 §3  —  **PARTIAL**

**Claim:**
> The Center for International Maritime Security (CIMSEC) published *"If the U.S. Navy Can't Repair Ships in Peacetime, How Will It Do So in War?"* — arguing that current peacetime repair throughput is the floor and wartime repair throughput needs to be higher [s.2026-05-26-if-the-u-s-navy-cant-repair-sh]. **Assessment.** When USNI Proceedings and CIMSEC pipelines converge on the same gap independen…

**Citations:** [s.2026-05-26-if-the-u-s-navy-cant-repair-sh]

**Sources checked:**
- `[s.2026-05-26-if-the-u-s-navy-cant-repair-sh]` → `01_sources/2026-05-26_cimsec-org_if-the-u-s-navy-cant-repair-ships-in-peacetime-how-will-it-d.md` — verdict: **PARTIAL** ([source](https://cimsec.org/if-the-u-s-navy-cant-repair-ships-in-peacetime-how-will-it-do-so-in-war/))
  > _"All these shortfalls come during planned, peacetime maintenance periods. If the U.S. Navy needs to make repairs to battle damage in a major conflict, they do not have the salvage capabilities to conduct repairs at sea or forward deployed, they do not have the industrial base to support the additional work, and they do not have the open shipyard space to put the damaged ships."_
  - Missing in this source: The claim specifically characterizes the article's argument as 'current peacetime repair throughput is the floor and wartime repair throughput needs to be higher.' The source does not use that precise framing of 'peacetime as the floor'; it argues that peacetime repair is already failing and wartime demands would be even greater, which is directionally consistent but not an explicit 'floor' argument. Additionally, the Assessment portion of the claim — about USNI Proceedings and CIMSEC converging independently and the §11.1 engagement-surface inventory — is entirely editorial/analytical content not present in or supported by the source.
  - Model note: The source supports the core factual claim that CIMSEC published the named article arguing peacetime repair shortfalls will be compounded in wartime, but the specific 'peacetime as the floor' framing is an inference rather than an explicit statement in the source, and the Assessment commentary about USNI Proceedings convergence has no basis in the source text.

### ✓ FACT #12 §3  —  **SUPPORTS**

**Claim:**
> The DON FY27 Press Brief funds the Shipyard Infrastructure Optimization Program (SIOP) at $1.8 billion and the broader Maritime Industrial Base (MIB) at $7.0 billion for FY27 [s.2026-05-26-don-fy27-press-brief].

**Citations:** [s.2026-05-26-don-fy27-press-brief]

**Sources checked:**
- `[s.2026-05-26-don-fy27-press-brief]` → `01_sources/2026-05-26_secnav-navy-mil_don-fy27-press-brief.md` — verdict: **SUPPORTS** ([source](https://www.secnav.navy.mil/fmc/fmb/Documents/27pres/DON_Press_Brief.pdf))
  > _"$7.0B in Maritime Industrial Base (MIB) investments in Supplier Development, Shipyard Infrastructure, and Workforce Development, including $3.2B for nuclear shipbuilders, $2.5B for SIB, $1.3B for SSIB... $1.8B for Shipyard Infrastructure Optimization Program (SIOP) to expand shipyard capacity and optimize shipyards"_
  - Model note: The source explicitly states both the $1.8B SIOP figure and the $7.0B MIB figure for FY27 on Page 8, directly supporting all elements of the claim.

### ✓ FACT #13 §3  —  **SUPPORTS**

**Claim:**
> The FY27 Military Construction (MILCON) budget invests in six SIOP projects per the DON FY27 Press Brief [s.2026-05-26-don-fy27-press-brief].

**Citations:** [s.2026-05-26-don-fy27-press-brief]

**Sources checked:**
- `[s.2026-05-26-don-fy27-press-brief]` → `01_sources/2026-05-26_secnav-navy-mil_don-fy27-press-brief.md` — verdict: **SUPPORTS** ([source](https://www.secnav.navy.mil/fmc/fmb/Documents/27pres/DON_Press_Brief.pdf))
  > _"Invests in construction for 6 SIOP projects"_
  - Model note: Page 16 of the source explicitly states that the FY27 MILCON budget 'Invests in construction for 6 SIOP projects,' directly supporting the claim.

### ✓ FACT #14 §3  —  **SUPPORTS**

**Claim:**
> Norfolk Naval Shipyard began a $442 million drydock modernization in May 2026 [s.2026-05-26-norfolk-naval-shipyard-begins-].

**Citations:** [s.2026-05-26-norfolk-naval-shipyard-begins-]

**Sources checked:**
- `[s.2026-05-26-norfolk-naval-shipyard-begins-]` → `01_sources/2026-05-26_workboat-com_norfolk-naval-shipyard-begins-442-million-drydock-modernizat.md` — verdict: **SUPPORTS** ([source](https://www.workboat.com/norfolk-naval-shipyard-begins-442-million-drydock-modernization))
  > _"Norfolk Naval Shipyard has begun a $442 million modernization of Dry Dock 3, a major infrastructure project aimed at improving the maintenance and modernization of Virginia-class submarines as part of the Navy's Shipyard Infrastructure Optimization Program (SIOP)."_
  - Model note: The source confirms Norfolk Naval Shipyard began a $442 million drydock modernization, and the capture date of 2026-05-26 places this in May 2026, satisfying all elements of the claim within acceptable rounding and date matching.

### ⚑ FACT #15 §3  —  **PARTIAL**

**Claim:**
> Pacific Naval Facilities Engineering Command (NAVFAC) published a SIOP brief documenting Puget Sound Naval Shipyard and Subordinate Bases (PSNS-SBS) infrastructure investments [s.2026-05-26-siop-brief-psns-sbs-2025-1]. **Assessment.** The §3.4 dollar flow is evidence that Navy senior leadership is willing to commit volume to repair-activity capability at the infrastructure level. It is NOT a procu…

**Citations:** [s.2026-05-26-siop-brief-psns-sbs-2025-1]

**Sources checked:**
- `[s.2026-05-26-siop-brief-psns-sbs-2025-1]` → `01_sources/2026-05-26_pacific-navfac-navy-mil_siop-brief-psns-sbs-2025-1.md` — verdict: **PARTIAL** ([source](https://pacific.navfac.navy.mil/Portals/72/Northwest/Documents/SIOP-Brief-PSNS-SBS-2025-1.pdf))
  > _"Shipyard Infrastructure Optimization Program Program Executive: Mr. Mark Edelson, PEO Industrial Infrastructure Program Manager: CAPT Luke Greene, PMO 555 (SIOP) Briefier: Dave Sweet, Director, SIOP Department at Puget Sound Naval Shipyard (PSNS) 15 April 2025"_
  - Missing in this source: The claim states the publisher is 'Pacific Naval Facilities Engineering Command (NAVFAC)' and the document covers 'Puget Sound Naval Shipyard and Subordinate Bases (PSNS-SBS)'. The source URL references pacific.navfac.navy.mil and the content confirms PSNS coverage, supporting those elements. However, the document title in the source metadata is 'SIOP Brief PSNS SBS 2025 1' which aligns with the claim, but the brief itself is presented as a SIOP program brief under PEO Industrial Infrastructure/PMO 555, not explicitly attributed to NAVFAC Pacific as publisher within the document text. Additionally, the document date is 15 April 2025 in the content but 2025-04-10 in metadata, a minor discrepancy. The 'Subordinate Bases (SBS)' portion of the title appears in the URL/metadata but is not explicitly confirmed in the extracted document text.
  - Model note: The source URL and metadata confirm a SIOP brief associated with PSNS-SBS published via pacific.navfac.navy.mil, supporting the core claim, but the document text itself does not explicitly identify NAVFAC Pacific as the publisher nor explicitly reference 'Subordinate Bases' within the extracted content, making this only partial support.

### ✗ FACT #16 §3  —  **DOES_NOT_SUPPORT**

**Claim:**
> The FY27 Department of Defense budget justification book funds, as part of the Marine Air-Ground Task Force (MAGTF) Tactical Warfare Simulation, *"developing an exercise planning, design, implementation, execution, and control tool ... enabling exercise designers the ability to rapidly build new scenarios and incorporate human geography elements into the training scenarios"* [s.2026-05-26-justific…

**Citations:** [s.2026-05-26-justification-book]

**Sources checked:**
- `[s.2026-05-26-justification-book]` → `01_sources/2026-05-26_comptroller-war-gov_justification-book.md` — verdict: **DOES_NOT_SUPPORT** ([source](https://comptroller.war.gov/Portals/45/Documents/defbudget/FY2027/budget_justification/pdfs/03_RDT_and_E/RDTE_TJS_PB_2027.pdf))
  - Missing in this source: The source contains no mention of the Marine Air-Ground Task Force (MAGTF) Tactical Warfare Simulation, nor any language about 'developing an exercise planning, design, implementation, execution, and control tool ... enabling exercise designers the ability to rapidly build new scenarios and incorporate human geography elements into the training scenarios'.
  - Model note: The source document covers The Joint Staff RDT&E programs (PE 0604826J, PE 0205401JCA, PE 0603829J, PE 0605126J, PE 0204571J, PE 0305248J, PE 0804768J) and contains no reference whatsoever to MAGTF Tactical Warfare Simulation or the quoted language about exercise planning tools and human geography elements.

### ✗ FACT #17 §3  —  **DOES_NOT_SUPPORT**

**Claim:**
> The same FY27 justification book initiates *"design and development of a joint exercise design and control tool ... providing exercise planning, design and control within various joint simulation constructs"* [s.2026-05-26-justification-book].

**Citations:** [s.2026-05-26-justification-book]

**Sources checked:**
- `[s.2026-05-26-justification-book]` → `01_sources/2026-05-26_comptroller-war-gov_justification-book.md` — verdict: **DOES_NOT_SUPPORT** ([source](https://comptroller.war.gov/Portals/45/Documents/defbudget/FY2027/budget_justification/pdfs/03_RDT_and_E/RDTE_TJS_PB_2027.pdf))
  - Missing in this source: The specific quoted language about 'design and development of a joint exercise design and control tool ... providing exercise planning, design and control within various joint simulation constructs' does not appear anywhere in the source content provided.
  - Model note: The source (RDTE_TJS_PB_2027) covers programs including Joint C5 Capability Development, Counter-sUAS, Joint Capability Experimentation, JIAMDO, Joint Staff Analytical Support, Joint Staff CDAO, and JTEEP, but none of the extracted pages contain the specific language about a 'joint exercise design and control tool' with 'exercise planning, design and control within various joint simulation constructs' as claimed.

### ✗ FACT #18 §3  —  **DOES_NOT_SUPPORT**

**Claim:**
> The same FY27 justification book funds Scenario Generation as a named capability line — *"Delivery of AI-powered scenario generation capability within JTT [Joint Training Tools]. This will be a massive education and training effort to get JExD [Joint Exercise Design] and exercise planners up to speed with new capability"* [s.2026-05-26-justification-book]. **Assessment.** The Joint / USMC exercise…

**Citations:** [s.2026-05-26-justification-book]

**Sources checked:**
- `[s.2026-05-26-justification-book]` → `01_sources/2026-05-26_comptroller-war-gov_justification-book.md` — verdict: **DOES_NOT_SUPPORT** ([source](https://comptroller.war.gov/Portals/45/Documents/defbudget/FY2027/budget_justification/pdfs/03_RDT_and_E/RDTE_TJS_PB_2027.pdf))
  - Missing in this source: The specific quoted language about 'Delivery of AI-powered scenario generation capability within JTT [Joint Training Tools]', 'massive education and training effort', 'JExD [Joint Exercise Design]', and 'exercise planners up to speed with new capability' is entirely absent from the source. The source does not contain any program element or project titled 'Scenario Generation' as a named capability line, nor does it mention JTT, JExD, or AI-powered scenario generation in any context.
  - Model note: The source (RDTE_TJS_PB_2027) covers Joint Staff RDT&E programs including JTEEP (PE 0804768J) in the table of contents but the extracted content does not include the JTEEP section pages, and none of the extracted pages contain the verbatim or paraphrased language cited in the claim about AI-powered scenario generation, JTT, JExD, or exercise planners.

### ✓ FACT #19 §3  —  **SUPPORTS**

**Claim:**
> Per the USAspending award record, Invictus Associates LLC has a Navy delivery order obligating $19,384,385 for Professional Support Services (PSS) — specifically Fleet Readiness Support for Commander, Navy Regional Maintenance Center (CNRMC), its subordinate Regional Maintenance Centers (RMCs), and Surface Team One (ST1) [s.2026-05-26-professional-support-services-]. *Note: the award record does n…

**Citations:** [s.2026-05-26-professional-support-services-]

**Sources checked:**
- `[s.2026-05-26-professional-support-services-]` → `01_sources/2026-05-26_usaspending-gov_professional-support-services-pss-specifically-fleet-readine.md` — verdict: **SUPPORTS** ([source](https://www.usaspending.gov/award/CONT_AWD_N0016424F3006_9700_N0017819D7883_9700/))
  > _"PROFESSIONAL SUPPORT SERVICES (PSS), SPECIFICALLY FLEET READINESS SUPPORT FOR COMMANDER, NAVY REGIONAL MAINTENANCE CENTER (CNRMC), ITS SUBORDINATE REGIONAL MAINTENANCE CENTERS (RMCS), AND SURFACE TEAM ONE (ST1). ... Recipient: INVICTUS ASSOCIATES, LLC ... Type: DELIVERY ORDER ... Total obligation: $19,384,385 ... Period start: [blank] ... Period current end: [blank]"_
  - Model note: The source explicitly confirms all elements of the claim: recipient (Invictus Associates LLC), award type (delivery order), obligation amount ($19,384,384.65, which rounds to $19,384,385), full description matching PSS/Fleet Readiness/CNRMC/RMCs/ST1, Navy awarding agency, and the absence of period start/end dates — consistent with the claim's note about active-status not being confirmable.

### ✓ FACT #20 §3  —  **SUPPORTS**

**Claim:**
> The Invictus delivery order is identified by Procurement Instrument Identifier (PIID) N0016424F3006 against an existing Multiple-Award Indefinite Delivery Contract (parent PIID N0017819D7883), with place of performance in Norfolk, Virginia [s.2026-05-26-professional-support-services-].

**Citations:** [s.2026-05-26-professional-support-services-]

**Sources checked:**
- `[s.2026-05-26-professional-support-services-]` → `01_sources/2026-05-26_usaspending-gov_professional-support-services-pss-specifically-fleet-readine.md` — verdict: **SUPPORTS** ([source](https://www.usaspending.gov/award/CONT_AWD_N0016424F3006_9700_N0017819D7883_9700/))
  > _"**PIID:** `N0016424F3006` ... **Type:** DELIVERY ORDER ... **Recipient:** INVICTUS ASSOCIATES, LLC ... **Place of performance:** NORFOLK, VA ... PIID: `N0017819D7883` ... IDC (INDEFINITE DELIVERY / INDEFINITE QUANTITY) ... Multiple/Single Award: MULTIPLE AWARD"_
  - Model note: The source explicitly confirms PIID N0016424F3006 is a delivery order awarded to Invictus Associates LLC, with parent PIID N0017819D7883 identified as a Multiple Award IDC (IDIQ), and place of performance in Norfolk, VA, supporting all elements of the claim.

### ✓ FACT #21 §3  —  **SUPPORTS**

**Claim:**
> The funder of the Invictus contract is the Department of Defense / Department of the Navy [s.2026-05-26-professional-support-services-]. **Assessment.** The Invictus contract has two analytical functions in §3. **First**, it confirms that CNRMC (the parent command of the RMCs §1 names as candidate customers) does procure contractor-supplied support, naming Surface Team One (the Navy's surface read…

**Citations:** [s.2026-05-26-professional-support-services-]

**Sources checked:**
- `[s.2026-05-26-professional-support-services-]` → `01_sources/2026-05-26_usaspending-gov_professional-support-services-pss-specifically-fleet-readine.md` — verdict: **SUPPORTS** ([source](https://www.usaspending.gov/award/CONT_AWD_N0016424F3006_9700_N0017819D7883_9700/))
  > _"Funding agency: Department of Defense / Department of the Navy"_
  - Model note: The source explicitly states that both the funding agency and funding subtier for the Invictus contract are Department of Defense and Department of the Navy respectively, directly supporting the claim.

### ⚑ FACT #22 §3  —  **PARTIAL**

**Claim:**
> CACI NSS LLC holds a $194 million contract for *"Plans, Operations, Logistics, Engagement, Training, Exercise, and Assessment Support to AFRICOM"* — Department of Defense / Department of the Army funder, General Services Administration awarder, GSA OASIS-style indefinite-delivery vehicle [s.2026-05-26-the-purpose-of-this-award-is-t].

**Citations:** [s.2026-05-26-the-purpose-of-this-award-is-t]

**Sources checked:**
- `[s.2026-05-26-the-purpose-of-this-award-is-t]` → `01_sources/2026-05-26_usaspending-gov_the-purpose-of-this-award-is-to-provide-plans-operations-log.md` — verdict: **PARTIAL** ([source](https://www.usaspending.gov/award/CONT_AWD_47QFCA20F0002_4732_GS00Q14OADU121_4732/))
  > _"THE PURPOSE OF THIS AWARD IS TO PROVIDE PLANS, OPERATIONS, LOGISTICS, ENGAGEMENT, TRAINING, EXERCISE, AND ASSESSMENT SUPPORT TO AFRICOM. ... Recipient: CACI NSS, LLC ... Awarding agency: General Services Administration / Federal Acquisition Service ... Funding agency: Department of Defense / Department of the Army ... Total obligation: $194,034,792"_
  - Missing in this source: The claim describes the vehicle as 'GSA OASIS-style indefinite-delivery vehicle,' but the source identifies the parent award GS00Q14OADU121 as an 'IDC (INDEFINITE DELIVERY / REQUIREMENTS)' vehicle — it does not explicitly name it as 'OASIS.' The parent PIID GS00Q14OADU121 is consistent with a GSA OASIS contract but the source does not use the word 'OASIS.'
  - Model note: All core elements of the claim (recipient CACI NSS LLC, contract description, $194M obligation, DoD/Army funder, GSA awarder, indefinite-delivery vehicle) are supported by the source, but the specific characterization of the vehicle as 'OASIS-style' is not explicitly stated in the source text.

### ✓ FACT #23 §3  —  **SUPPORTS**

**Claim:**
> Parsons Government Services Inc. holds a $556.8 million Command, Control, Communications, Computers, Combat Systems, Intelligence, Surveillance, Reconnaissance, and Targeting (C5ISR) / Exercises / Operations / Information Services (CEOIS) task order providing near real-time situational awareness and decision support to the Department of Defense Combatant Commands — Office of the Secretary of Defen…

**Citations:** [s.2026-05-26-the-purpose-of-this-award-is-f]

**Sources checked:**
- `[s.2026-05-26-the-purpose-of-this-award-is-f]` → `01_sources/2026-05-26_usaspending-gov_the-purpose-of-this-award-is-for-the-c5isr-exercises-operati.md` — verdict: **SUPPORTS** ([source](https://www.usaspending.gov/award/CONT_AWD_47QFCA21F0042_4732_GS00Q14OADU127_4732/))
  > _"THE PURPOSE OF THIS AWARD IS FOR THE C5ISR, EXERCISES, OPERATIONS, AND INFORMATION SERVICES (CEOIS) TASK ORDER IS TO PROVIDE NEAR REAL-TIME SITUATIONAL AWARENESS AND DECISION SUPPORT TO THE DOD COMBATANT COMMANDS (CCMDS)"_
  - Model note: The source explicitly confirms Parsons Government Services Inc. holds the CEOIS task order providing near real-time situational awareness and decision support to DOD Combatant Commands, with a total obligation of $556,853,906 (rounds to $556.8M), awarded by GSA and funded by the Immediate Office of the Secretary of Defense, all matching the claim within acceptable rounding and paraphrase tolerance.

### ✓ FACT #24 §3  —  **SUPPORTS**

**Claim:**
> Axient LLC holds a $233.8 million Test, Exercise and Wargames Support contract — Missile Defense Agency funder [s.2026-05-26-test-exercise-and-wargames-sup]. **Assessment.** When the Department of Defense decides to buy exercise design, wargames support, decision support, or training scenarios, it buys it under EXPLICITLY-NAMED vehicles — the AFRICOM "Plans, Operations, Logistics, Engagement, Trai…

**Citations:** [s.2026-05-26-test-exercise-and-wargames-sup]

**Sources checked:**
- `[s.2026-05-26-test-exercise-and-wargames-sup]` → `01_sources/2026-05-26_usaspending-gov_test-exercise-and-wargames-support-igf-ot-igf.md` — verdict: **SUPPORTS** ([source](https://www.usaspending.gov/award/CONT_AWD_HQ014716C0034_9700_-NONE-_-NONE-/))
  > _"recipient_name: AXIENT LLC ... award_type: DEFINITIVE CONTRACT ... total_obligation: 233761710.98 ... awarding_subtier: Missile Defense Agency ... TEST, EXERCISE AND WARGAMES SUPPORT IGF::OT::IGF"_
  - Model note: The source explicitly confirms Axient LLC holds a definitive contract titled 'TEST, EXERCISE AND WARGAMES SUPPORT' with a total obligation of $233,761,711 (rounds to $233.8M) awarded by the Missile Defense Agency, directly supporting all elements of the claim.

### ⚑ FACT #25 §4  —  **PARTIAL**

**Claim:**
> Acting Secretary of the Navy Hung Cao signed the foreword of the Navy's May 2026 Shipbuilding Plan and the cover of the Department of the Navy FY27 President's Budget Press Brief dated 28 April 2026 [s.2026-05-26-don-fy27-press-brief].

**Citations:** [s.2026-05-26-don-fy27-press-brief]

**Sources checked:**
- `[s.2026-05-26-don-fy27-press-brief]` → `01_sources/2026-05-26_secnav-navy-mil_don-fy27-press-brief.md` — verdict: **PARTIAL** ([source](https://www.secnav.navy.mil/fmc/fmb/Documents/27pres/DON_Press_Brief.pdf))
  > _"Department of the Navy FY 2027 President's Budget Press Brief, dated 28 April 2026. 17-page slide deck signed at the policy level by Acting Secretary of the Navy Hung Cao."_
  - Missing in this source: The source does not contain any evidence regarding Hung Cao signing the foreword of a 'Navy's May 2026 Shipbuilding Plan.' The source only supports his association with the DON FY27 President's Budget Press Brief dated 28 April 2026.
  - Model note: The source explicitly supports Hung Cao's signing of the DON PB2027 Press Brief dated 28 April 2026, but contains no mention of a 'Navy's May 2026 Shipbuilding Plan' or any foreword signed by him in connection with such a document.

### ✓ FACT #26 §4  —  **SUPPORTS**

**Claim:**
> Admiral Daryl L. Caudle, the Chief of Naval Operations, delivered a Statement on the Posture of the United States Navy before the House Armed Services Committee on 14 May 2026, naming maintenance as a warfighting requirement and announcing a planned deliberate study of Navy yard capacity [s.2026-05-26-2026-05-14-caudle-testimony].

**Citations:** [s.2026-05-26-2026-05-14-caudle-testimony]

**Sources checked:**
- `[s.2026-05-26-2026-05-14-caudle-testimony]` → `01_sources/2026-05-26_armedservices-house-gov_2026-05-14-caudle-testimony.md` — verdict: **SUPPORTS** ([source](https://armedservices.house.gov/uploadedfiles/2026-05-14_caudle_testimony.pdf))
  > _"We're also taking a hard look at whether we need a new public Navy Yard. In the FY27 budget, we've resourced a deliberate study to close the gap between the maintenance capacity we have and the maintenance demand we know is coming... This is about combat credibility. Maintenance is not a back-end function - it is a warfighting requirement."_
  - Model note: The source is Admiral Daryl L. Caudle's testimony titled 'Statement on the Posture of the United States Navy' before the House Armed Services Committee dated May 14, 2026, and it explicitly states both that maintenance is a warfighting requirement and that a deliberate study of Navy yard capacity has been resourced in the FY27 budget.

### ⚑ FACT #27 §4  —  **PARTIAL**

**Claim:**
> Caudle's HASC testimony frames the FY27 posture around four named priorities — "Lethal & Effective Force," "Total Force Readiness," "Capable & Resilient Warfighter," and "Industrial & Logistics Capacity" — with the second priority (Total Force Readiness) explicitly covering Infrastructure, Maintenance, Operations, and Spares [s.2026-05-26-2026-05-14-caudle-testimony]. **Assessment.** The strategic…

**Citations:** [s.2026-05-26-2026-05-14-caudle-testimony]

**Sources checked:**
- `[s.2026-05-26-2026-05-14-caudle-testimony]` → `01_sources/2026-05-26_armedservices-house-gov_2026-05-14-caudle-testimony.md` — verdict: **PARTIAL** ([source](https://armedservices.house.gov/uploadedfiles/2026-05-14_caudle_testimony.pdf))
  > _"To deliver a Navy that is ready to deter aggression and win in conflict, the Fiscal Year 2027 budget prioritizes four critical areas: 1. Battle Ready Sailors – Quality of Service and Warfighter Competency. 2. Total Force Readiness – Infrastructure, Maintenance, Operations, and Spares. 3. Maritime Kill Chain – Command and Control, Counter-Targeting, and Long-Range Fires. 4. Golden Fleet Initiative …"_
  - Missing in this source: The claim names the first priority as 'Lethal & Effective Force' and the fourth as 'Industrial & Logistics Capacity', but the source names them as 'Battle Ready Sailors – Quality of Service and Warfighter Competency' and 'Golden Fleet Initiative – Future Force Design and Scalable Combat Power' respectively. The claim's labels for priorities 1 and 4 do not match the source.
  - Model note: The source fully supports priority 2 (Total Force Readiness – Infrastructure, Maintenance, Operations, and Spares) and its position as second, but the names given for priorities 1 and 4 in the claim do not match the source's actual labels.

### ✓ FACT #28 §4  —  **SUPPORTS**

**Claim:**
> The four public naval shipyards are Norfolk Naval Shipyard (NNSY), Puget Sound Naval Shipyard (PSNS), Portsmouth Naval Shipyard (PNSY), and Pearl Harbor Naval Shipyard (PHNS), as named in CNO Caudle's HASC testimony [s.2026-05-26-2026-05-14-caudle-testimony].

**Citations:** [s.2026-05-26-2026-05-14-caudle-testimony]

**Sources checked:**
- `[s.2026-05-26-2026-05-14-caudle-testimony]` → `01_sources/2026-05-26_armedservices-house-gov_2026-05-14-caudle-testimony.md` — verdict: **SUPPORTS** ([source](https://armedservices.house.gov/uploadedfiles/2026-05-14_caudle_testimony.pdf))
  > _"To date, SIOP has completed 54 projects across all four shipyards – Pearl Harbor Naval Shipyard (PHNS), Puget Sound Naval Shipyard (PSNS), Portsmouth Naval Shipyard (PNSY), Norfolk Naval Shipyard (NNSY) – totaling over $1.4B."_
  - Model note: The source explicitly names all four public naval shipyards with their exact abbreviations (PHNS, PSNS, PNSY, NNSY) in the SIOP section, fully supporting the claim about all four shipyard names and abbreviations as stated in CNO Caudle's HASC testimony.

### ✓ FACT #29 §4  —  **SUPPORTS**

**Claim:**
> Norfolk Naval Shipyard began a $442 million drydock modernization in May 2026 [s.2026-05-26-norfolk-naval-shipyard-begins-].

**Citations:** [s.2026-05-26-norfolk-naval-shipyard-begins-]

**Sources checked:**
- `[s.2026-05-26-norfolk-naval-shipyard-begins-]` → `01_sources/2026-05-26_workboat-com_norfolk-naval-shipyard-begins-442-million-drydock-modernizat.md` — verdict: **SUPPORTS** ([source](https://www.workboat.com/norfolk-naval-shipyard-begins-442-million-drydock-modernization))
  > _"Norfolk Naval Shipyard has begun a $442 million modernization of Dry Dock 3"_
  - Model note: The source confirms Norfolk Naval Shipyard began a $442 million drydock modernization, and the capture date of 2026-05-26 places the event in May 2026, consistent with the claim.

### ⚑ FACT #30 §4  —  **PARTIAL**

**Claim:**
> Pacific Naval Facilities Engineering Command published a Shipyard Infrastructure Optimization Program brief covering Puget Sound Naval Shipyard and Subordinate Bases (PSNS-SBS) infrastructure investments [s.2026-05-26-siop-brief-psns-sbs-2025-1].

**Citations:** [s.2026-05-26-siop-brief-psns-sbs-2025-1]

**Sources checked:**
- `[s.2026-05-26-siop-brief-psns-sbs-2025-1]` → `01_sources/2026-05-26_pacific-navfac-navy-mil_siop-brief-psns-sbs-2025-1.md` — verdict: **PARTIAL** ([source](https://pacific.navfac.navy.mil/Portals/72/Northwest/Documents/SIOP-Brief-PSNS-SBS-2025-1.pdf))
  > _"Shipyard Infrastructure Optimization Program Briefer: Dave Sweet, Director, SIOP Department at Puget Sound Naval Shipyard (PSNS) 15 April 2025"_
  - Missing in this source: The claim specifies 'Puget Sound Naval Shipyard and Subordinate Bases (PSNS-SBS)' as the scope, but the source covers all four public shipyards (PSNS, PNSY, PHNS, NNSY) broadly; the source URL references 'PSNS-SBS' but the document content does not explicitly use the 'PSNS-SBS' designation or explicitly state the brief covers 'Subordinate Bases.' Additionally, the publisher domain is 'pacific.navfac.navy.mil' (Pacific Naval Facilities Engineering Command), which is consistent with the claim, but the document itself does not explicitly identify Pacific NAVFAC as the publisher within its content.
  - Model note: The source is a SIOP brief hosted on the Pacific NAVFAC domain and covers PSNS infrastructure investments, partially supporting the claim, but the document does not explicitly use the 'PSNS-SBS' (Subordinate Bases) designation within its extracted content, and coverage extends to all four shipyards rather than being PSNS-SBS-specific as implied by the claim.

### ⚑ FACT #31 §4  —  **PARTIAL**

**Claim:**
> The DON FY27 Press Brief funds six SIOP construction projects in FY27 across the four public shipyards [s.2026-05-26-don-fy27-press-brief]. **Assessment.** The four public shipyards are the heaviest-investment repair-activity nodes in the Navy enterprise — each receives multi-hundred-million-dollar infrastructure investment and each houses a workforce of thousands. They are the most likely site fo…

**Citations:** [s.2026-05-26-don-fy27-press-brief]

**Sources checked:**
- `[s.2026-05-26-don-fy27-press-brief]` → `01_sources/2026-05-26_secnav-navy-mil_don-fy27-press-brief.md` — verdict: **PARTIAL** ([source](https://www.secnav.navy.mil/fmc/fmb/Documents/27pres/DON_Press_Brief.pdf))
  > _"Invests in construction for 6 SIOP projects"_
  - Missing in this source: The claim states these 6 SIOP construction projects are 'across the four public shipyards.' The source does not mention the four public shipyards in connection with the 6 SIOP projects, nor does it specify where the projects are located.
  - Model note: The source confirms 6 SIOP construction projects funded in FY27 under MILCON, but does not attribute them to 'the four public shipyards' or specify their locations at all.

### ⚑ FACT #32 §4  —  **PARTIAL**

**Claim:**
> Commander, Navy Regional Maintenance Center (CNRMC) is the parent command of the subordinate Regional Maintenance Centers (RMCs), per the Invictus Associates Navy Professional Support Services contract scope [s.2026-05-26-professional-support-services-].

**Citations:** [s.2026-05-26-professional-support-services-]

**Sources checked:**
- `[s.2026-05-26-professional-support-services-]` → `01_sources/2026-05-26_usaspending-gov_professional-support-services-pss-specifically-fleet-readine.md` — verdict: **PARTIAL** ([source](https://www.usaspending.gov/award/CONT_AWD_N0016424F3006_9700_N0017819D7883_9700/))
  > _"PROFESSIONAL SUPPORT SERVICES (PSS), SPECIFICALLY FLEET READINESS SUPPORT FOR COMMANDER, NAVY REGIONAL MAINTENANCE CENTER (CNRMC), ITS SUBORDINATE REGIONAL MAINTENANCE CENTERS (RMCS), AND SURFACE TEAM ONE (ST1)."_
  - Missing in this source: The source confirms CNRMC has subordinate RMCs within the contract scope, but does not explicitly use the word 'parent command' to describe CNRMC's relationship to the RMCs. The term 'parent command' is the claim's characterization, not language found in the source.
  - Model note: The source confirms that CNRMC has subordinate RMCs within the Invictus Associates contract scope, which supports the organizational hierarchy implied by the claim, but the specific term 'parent command' is not present in the source text.

### ✓ FACT #33 §4  —  **SUPPORTS**

**Claim:**
> Surface Team One (ST1) is named as a covered customer in the Invictus contract alongside CNRMC and the subordinate RMCs [s.2026-05-26-professional-support-services-].

**Citations:** [s.2026-05-26-professional-support-services-]

**Sources checked:**
- `[s.2026-05-26-professional-support-services-]` → `01_sources/2026-05-26_usaspending-gov_professional-support-services-pss-specifically-fleet-readine.md` — verdict: **SUPPORTS** ([source](https://www.usaspending.gov/award/CONT_AWD_N0016424F3006_9700_N0017819D7883_9700/))
  > _"PROFESSIONAL SUPPORT SERVICES (PSS), SPECIFICALLY FLEET READINESS SUPPORT FOR COMMANDER, NAVY REGIONAL MAINTENANCE CENTER (CNRMC), ITS SUBORDINATE REGIONAL MAINTENANCE CENTERS (RMCS), AND SURFACE TEAM ONE (ST1)."_
  - Model note: The source's award description explicitly names CNRMC, its subordinate RMCs, and Surface Team One (ST1) as covered customers in the Invictus contract N0016424F3006.

### ⚑ FACT #34 §4  —  **PARTIAL**

**Claim:**
> SRF-JRMC, U.S. Seventh Fleet, U.S. Pacific Command, and U.S. Pacific Fleet executed the SWARMEX exercise on USS Ashland (LSD 48) at Cebu, Philippines, in coordination with Philippine Navy partners and local Philippine contractors [s.2026-05-26-uss-ashland-completes-ship-war].

**Citations:** [s.2026-05-26-uss-ashland-completes-ship-war]

**Sources checked:**
- `[s.2026-05-26-uss-ashland-completes-ship-war]` → `01_sources/2026-05-26_cpf-navy-mil_uss-ashland-completes-ship-wartime-repair-and-maintenance-ex.md` — verdict: **PARTIAL** ([source](https://www.cpf.navy.mil/Newsroom/News/Article/4452493/uss-ashland-completes-ship-wartime-repair-and-maintenance-in-philippines/))
  > _"This exercise allowed us to work shoulder-to-shoulder with our Philippine allies to conduct complex repairs while keeping USS Ashland ready to respond to any contingency in the region"_
  - Missing in this source: The source does not mention: (1) the exercise name 'SWARMEX', (2) SRF-JRMC as a participating organization, (3) U.S. Pacific Command as a participating organization, (4) U.S. Pacific Fleet as a participating organization, (5) Cebu, Philippines as the specific location, (6) local Philippine contractors as participants. The source references U.S. 7th Fleet and Philippine allies but not the other named organizations or the specific location.
  - Model note: The source confirms a ship wartime repair and maintenance exercise on USS Ashland involving Philippine allies and U.S. 7th Fleet, but does not name the exercise 'SWARMEX,' specify Cebu as the location, or mention SRF-JRMC, U.S. Pacific Command, U.S. Pacific Fleet, or local Philippine contractors.

### ⚑ FACT #35 §4  —  **PARTIAL**

**Claim:**
> Naval News identified Philippine Naval Sea Systems Command participation in SWARMEX-Cebu [s.2026-05-26-u-s-navy-rehearses-wartime-rep]. **Assessment.** CNRMC is the parent-command anchor that ties the RMCs together; SRF-JRMC is the operationally-most-exposed RMC because of its forward-deployed posture and active SWARMEX execution history. The Invictus contract confirms CNRMC procures contractor-su…

**Citations:** [s.2026-05-26-u-s-navy-rehearses-wartime-rep]

**Sources checked:**
- `[s.2026-05-26-u-s-navy-rehearses-wartime-rep]` → `01_sources/2026-05-26_navalnews-com_u-s-navy-rehearses-wartime-repairs-in-central-philippine-por.md` — verdict: **PARTIAL** ([source](https://www.navalnews.com/naval-news/2026/04/u-s-navy-rehearses-wartime-repairs-in-central-philippine-port/))
  > _"Philippine Naval Sea Systems Command personnel and local contractors participated in the exercise."_
  - Missing in this source: The claim refers to the exercise as 'SWARMEX-Cebu,' but the source does not use that name anywhere; the exercise is described generically as a wartime repairs exercise at Cebu South Port.
  - Model note: The source confirms Naval News reported Philippine Naval Sea Systems Command participation in an exercise at Cebu, but the specific designation 'SWARMEX-Cebu' does not appear in the source text.

### ✓ FACT #36 §4  —  **SUPPORTS**

**Claim:**
> U.S. Fleet Forces Command (FLTFORCOM) is developing the Global Maritime Response Plan as the wartime force-generation counterpart to the peacetime Optimized Fleet Response Plan, with explicit intent *"to prepare the Fleet for Battle Stations—to ensure that the Navy is on a wartime footing capable of transitioning to 'General Quarters'"* [s.2026-05-26-fix-the-navys-expeditionary-re].

**Citations:** [s.2026-05-26-fix-the-navys-expeditionary-re]

**Sources checked:**
- `[s.2026-05-26-fix-the-navys-expeditionary-re]` → `01_sources/2026-05-26_usni-org_fix-the-navys-expeditionary-repair.md` — verdict: **SUPPORTS** ([source](https://www.usni.org/magazines/proceedings/2025/march/fix-navys-expeditionary-repair))
  > _"To address force generation challenges for wartime, U.S. Fleet Forces Command is developing the Global Maritime Response Plan "to prepare the Fleet for Battle Stations—to ensure that the Navy is on a wartime footing capable of transitioning to 'General Quarters,'" to generate combat forces, and to "provide Operational Commanders with the most capable and ready players on the field." ... Force gene…"_
  - Model note: The source explicitly states that the Optimized Fleet Response Plan governs peacetime force generation, that FLTFORCOM is developing the Global Maritime Response Plan as the wartime force-generation counterpart, and includes the exact quoted language about 'Battle Stations' and 'General Quarters' attributed to ADM Daryl Caudle's September 2024 speech.

### ⚑ FACT #37 §4  —  **PARTIAL**

**Claim:**
> The peacetime Optimized Fleet Response Plan is governed by COMUSFLTFORCOM/COMPACFLT INST 3000.15B, dated 20 October 2020 [s.2026-05-26-fix-the-navys-expeditionary-re].

**Citations:** [s.2026-05-26-fix-the-navys-expeditionary-re]

**Sources checked:**
- `[s.2026-05-26-fix-the-navys-expeditionary-re]` → `01_sources/2026-05-26_usni-org_fix-the-navys-expeditionary-repair.md` — verdict: **PARTIAL** ([source](https://www.usni.org/magazines/proceedings/2025/march/fix-navys-expeditionary-repair))
  > _"Department of the Navy, COMUSFLTFORCOM/COMPACFLT INST 3000.15B/COMUSNAVEUR/COMUSNAVAFINST 300.15: Optimized Fleet Response Plan, 20 October 2020, 42."_
  - Missing in this source: The claim states the instruction is 'COMUSFLTFORCOM/COMPACFLT INST 3000.15B' only, but the source shows it is a joint instruction also designated 'COMUSNAVEUR/COMUSNAVAFINST 300.15'. The claim omits the COMUSNAVEUR/COMUSNAVAFINST 300.15 co-designation. Additionally, the claim does not mention it governs 'force generation' specifically but describes it as governing the 'peacetime Optimized Fleet Response Plan,' which is supported by the source text saying 'Force generation is governed in peacetime by the Optimized Fleet Response Plan.'
  - Model note: The source confirms the document number, date, and subject (Optimized Fleet Response Plan governing peacetime force generation), but the claim omits the co-designation COMUSNAVEUR/COMUSNAVAFINST 300.15 that the source includes as part of the full instruction title.

### ✗ FACT #38 §4  —  **DOES_NOT_SUPPORT**

**Claim:**
> U.S. Pacific Command (USINDOPACOM) and Commander, U.S. Pacific Fleet (COMPACFLT) published parallel press releases for the SWARMEX-Cebu event, naming the exercise as a Pacific Fleet activity [s.2026-05-26-uss-ashland-completes-ship-war]. **Assessment.** FLTFORCOM and COMPACFLT are the joint owners of the peacetime force-generation framework and the developing wartime Global Maritime Response Plan.…

**Citations:** [s.2026-05-26-uss-ashland-completes-ship-war]

**Sources checked:**
- `[s.2026-05-26-uss-ashland-completes-ship-war]` → `01_sources/2026-05-26_cpf-navy-mil_uss-ashland-completes-ship-wartime-repair-and-maintenance-ex.md` — verdict: **DOES_NOT_SUPPORT** ([source](https://www.cpf.navy.mil/Newsroom/News/Article/4452493/uss-ashland-completes-ship-wartime-repair-and-maintenance-in-philippines/))
  - Missing in this source: The source contains no mention of USINDOPACOM, COMPACFLT, SWARMEX-Cebu, parallel press releases, or any characterization of an exercise as a Pacific Fleet activity; it covers USS Ashland's Ship Wartime Repair and Maintenance Exercise in the Philippines under U.S. 7th Fleet.
  - Model note: The source is entirely about a different exercise (ship wartime repair and maintenance) involving USS Ashland and has no content related to the claim's subject matter of SWARMEX-Cebu or USINDOPACOM/COMPACFLT press releases.


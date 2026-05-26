# Battle Damage Repair (BDR) modeling integration into multidomain fleet training and PAE-IO repair-capacity planning — Research File

**Customer:** Multi-customer research track (confirmed by operator 2026-05-21; candidate downstream customers if/when the track resolves to a named opportunity: NSWC Carderock Division as modeling source, NAVSEA as parent command, OPNAV / N9 as fleet-readiness demand-side, the Navy's PAE Industrial Operations consolidated structure as the ship-repair-and-maintenance organization)
**Opportunity ID:** BDR-FLEET-READINESS
**Gate:** Identify
**Started:** 2026-05-21
**Last updated:** 2026-05-21

> **Verification status legend** (applies to all FACT entries below as they are added):
> `[✓ INGESTED]` — claim is supported by a primary source file in `01_sources/`.
> `[⚑ PARTIAL]` — some elements verified by ingested source(s); others single-sourced or unverified.
> `[⚠ PENDING-INGEST]` — claim is cited but the cited source has not yet been ingested.
> Per the Standard Operating Procedure (`_meta/sop.md`), every claim in this file must carry one of three labels: **FACT** (supported by an ingested primary source), **Assessment** (the analyst's judgment, clearly flagged as such), or **Speculation** (forward-looking guess, clearly flagged as such).

> **Acronyms used in this file** — plain-English on first encounter so the file reads cleanly on a phone weeks later. Acronyms below are used freely in the prose that follows.
>
> | Term | What it means |
> |---|---|
> | OSI | Open-source intelligence — material anyone can read without a clearance. The only kind of source allowed in this vault. |
> | BDAR | Battle Damage Assessment and Repair — the formal U.S. military term for the unified cycle of assessing damage on a struck platform, classifying it, prioritizing repair, and executing it. **The primary scope frame for this research track** as tightened by the operator on 2026-05-24. |
> | BDAT | Battle Damage Assessment Team — the personnel cell that performs the assessment side of BDAR on a hit platform. BDAT training (§11.3) is the upstream-skill counterpart to the repair-side training (§11.2). |
> | BDR | Battle damage repair — the narrower term for the repair half of BDAR. Used in the folder ID and in earlier vault content; superseded by BDAR as the primary scope frame on 2026-05-24. |
> | BDA | Battle damage assessment — the diagnostic work of figuring out what is broken on a hit platform. Subsumed under BDAR. |
> | FDSRT | Forward Deployed Ship Repair Teams — government repair teams attached to forward-deployed fleets, named in the SRF-JRMC press release as the personnel cohort SWARMEX is designed to train in BDAR. |
> | SIMA | Shore Intermediate Maintenance Activity. The Navy is standing up new SIMAs in Norfolk and San Diego per CNO Caudle's HASC testimony 14 May 2026, explicitly to provide hands-on training in advanced ship repair using AI/ML, advanced manufacturing, workflow monitoring, and robotic systems. Closest primary-source language to the BDAR training pipeline this research proposes. |
> | SIOP | Shipyard Infrastructure Optimization Program — Navy's generational investment program in the four public shipyards. |
> | NSWC Carderock | A division of the Naval Surface Warfare Center, located in Maryland, that does ship survivability and damage modeling. The single most important named organization in this research track. |
> | NAVSEA | Naval Sea Systems Command — the Navy organization that owns NSWC Carderock, the public shipyards, and most ship-repair contracting. |
> | OPNAV / N9 | The Chief of Naval Operations' staff. N9 is the Warfare Systems directorate, which owns much of the fleet-readiness demand picture. |
> | NWDC | Naval Warfare Development Command — the Navy's doctrine and tactical-training authority. |
> | PAE-IO | PAE Industrial Operations — a Navy-internal organizational consolidation described in the May 2026 Navy Shipbuilding Plan combining the Navy Regional Maintenance Centers, NAVSEA's Industrial Operations Directorate, and the four public Navy Shipyards. Not a commercialization; not a private contractor. Acronym expansion not stated in the source. |
> | LVC | Live, virtual, constructive — a category of military simulation training that mixes real units, simulator pilots, and computer-generated forces. **Scope note added 2026-05-25.** Within this vault's BDAR/BDAT research context, LVC specifically refers to NCTE-compliant (Navy Continuous Training Environment) Fleet Synthetic Training architecture using HLA / DIS interoperability standards — not generic commercial AR/VR or off-the-shelf gaming-engine simulators. The distinction matters: a BDAR/BDAT simulation product that does not federate into the Navy's existing fleet synthetic training architecture is not "Navy LVC" in the customer's terms even if it is technically live/virtual/constructive in the generic sense. See `_red-teams/2026-05-25-gemini-pro-corpus-cleanup-dialogue.md` and the 2026-05-25 decision log entry. |
> | M&S | Modeling and simulation. |
> | SBIR / STTR | Small Business Innovation Research and Small Business Technology Transfer — federal R&D contracting paths that often serve as a low-friction first engagement with Navy labs. |
> | COMPTUEX | Composite Training Unit Exercise — a large Navy training event each strike group runs before deploying. |
> | RIMPAC | Rim of the Pacific — the world's largest international maritime exercise, held every two years. |
> | LSE | Large-Scale Exercise — a Navy series introduced in 2021 that strings multiple exercises together to test distributed fleet operations. |
> | SWARMEX | Ship Wartime Repair and Maintenance Exercise — a specific 2025 NAVSEA program first run by SRF-JRMC. The top-scoring hit from the 2026-05-21 source pass. |
> | SRF-JRMC | Ship Repair Facility, Japan Regional Maintenance Center — the Navy organization in Japan that ran the first SWARMEX. |
> | DON | Department of the Navy — the civilian-led department that includes both the U.S. Navy and the U.S. Marine Corps. |
> | GAO | Government Accountability Office — Congress's auditor, which publishes oversight reports we treat as primary sources. |
> | CRS | Congressional Research Service — Congress's in-house research arm; its reports are public and citation-quality. |
> | SASC / HASC | Senate Armed Services Committee / House Armed Services Committee. |

---

## 1. Working summary (analyst view)

This is a research track examining whether the U.S. Navy has a real business opportunity for CACI in **gamified operational-decision scenarios for the Battle Damage Assessment and Repair (BDAR) teams that work at Navy repair activities** — the four public naval shipyards (Norfolk, Puget Sound, Pearl Harbor, Portsmouth), the Regional Maintenance Centers (RMCs) including the forward-deployed Ship Repair Facility–Japan Regional Maintenance Center (SRF-JRMC), and the related forward-deployed repair organizations. The scope was last corrected on 2026-05-26 to make this explicit, replacing earlier framings that pointed at the Navy's schoolhouse / individual-Sailor training pipeline. See the 2026-05-26 decision log entry for the structural correction, and `_red-teams/2026-05-25-gemini-pro-right-to-win-reframe-dialogue.md` for the prior framing that this supersedes.

The audience for the product is the **professional repair-activity team** — team leaders, staff cells, and commanders making operational decisions in the moments after a ship is hit — not the individual Sailor learning damage-control hand-skills on a schoolhouse pipeline. CACI does not build schoolhouse curriculum; CACI builds situational exercise content for operational decision-makers. The known capability lineage is the U.S. Indo-Pacific Command (INDOPACOM) Pacific Multi-Domain Training and Experimentation Capability (PMTEC) exercise-design work that CACI already executes; this research asks whether that capability can be translated down-vertical to the naval-repair domain.

The operational-decision moments that this research treats as candidate scenario content are concrete:

- **Port-selection decisions** for a damaged ship. Which port to bring her to, given proximity versus repair capability versus security posture versus alliance access. This decision sits jointly between the fleet commander (the tactical operator who owns the ship) and the repair activity that has to receive and mobilize against the work.
- **Forward team mobilization** to where the damaged ship actually is. Transport, equipment sourcing, badge sponsorship, rules of engagement (ROE) for working a foreign port, host-nation legal frameworks.
- **Emergency contracting in a foreign port** when the ship cannot reach a U.S. or treaty-ally facility. Host-nation legal frameworks, currency, language, port-agent arrangements, customs clearance for repair equipment.
- **BDAR triage under combat tempo.** Sequencing which repairs matter when the ship still has to fight or transit out under threat.
- **BDAT-to-BDAR handoff.** The Battle Damage Assessment Team (BDAT) telling the repair team what is most important to fix first, and how the repair team's progress changes the assessment.
- **Degraded-communications information-resource access.** What data the team can pull when the ship is steaming dark, including legacy drawings, prior repair records, and technical-authority contacts.

Each scenario is designed for the operational team to play against in a serious-game / exercise-injection / playbook format — not delivered as a curriculum module to a new-Sailor cohort.

The candidate customer organizations are correspondingly different from the prior schoolhouse framing. The **public naval shipyards** (Norfolk, Puget Sound, Pearl Harbor, Portsmouth) sit on the receiving side for damaged ships, along with the **RMCs** (Hampton Roads, Mid-Atlantic, Southwest, Northwest, and Pacific RMCs) and their forward-deployed counterparts (SRF-JRMC, plus the Bahrain and Guam-area facilities). The **Naval Warfare Development Center (NWDC)** sits behind those activities as the doctrinal authority that owns the Naval Tactics, Techniques, and Procedures (NTTPs) and Tactical Memorandums (TACMEMOs) that scenario content has to be written against. The **fleet-command training authorities** — Commander, Naval Surface Forces (COMNAVSURFOR); U.S. Fleet Forces Command (FLTFORCOM); Commander, U.S. Pacific Fleet (COMPACFLT); and the joint exercise authorities at U.S. Indo-Pacific Command Joint Operations Directorate (INDOPACOM J7) — own how these activities train in fleet exercises like the Composite Training Unit Exercise (COMPTUEX), the Rim of the Pacific Exercise (RIMPAC), the Navy's Large-Scale Exercise (LSE) series, and the NAVSEA Ship Wartime Repair and Maintenance Exercise (SWARMEX) program.

The four research threads under the corrected scope:

1. **Is there a real demand signal for contractor-provided operational-decision scenarios at the Navy repair-activity level?** The most direct primary-source signal so far is the SRF-JRMC SWARMEX press release, which describes exactly this kind of exercise — Forward Deployed Ship Repair Teams (FDSRTs) practicing wartime-condition repair in a contested port environment. The CNO's May 2026 House Armed Services Committee (HASC) testimony about Shore Intermediate Maintenance Activities (SIMAs) standing up in Norfolk and San Diego is a secondary signal that the Navy is investing in repair-activity capability. Both signals carry press-release-versus-capability-building ambiguity that the next find_sources pass is designed to test.

2. **What does the right operational-decision scenario portfolio look like?** Concretely — how many scenarios are needed, at what fidelity, against which exercise events, for which audience tier (team-leader versus staff-cell versus commander). The six decision moments listed above are the working starter set. The research has to triangulate whether the Navy's exercise authorities are buying scenario content from contractors today, and if so, in what shape — directly via training-systems vehicles, indirectly via fleet exercise-planning support contracts, or organically by Navy staff.

3. **What does the gamified-simulation delivery layer look like?** The scenario content has to be delivered against something — physical tabletops, serious-game software, federated synthetic training, hardware-in-the-loop benches, or some mix. The Live, Virtual, Constructive (LVC) framing at §11.3 still applies, but the customer interpretation now is the operational exercise authority's preferred federation standards (Navy Continuous Training Environment compatibility may matter at fleet-exercise scale; commercial augmented-reality / virtual-reality may not), not the schoolhouse pipeline's preferences.

4. **How does CACI get in the room with these specific customer organizations?** The customer chain runs through fleet-command exercise authorities, NWDC doctrinal sponsors, and the repair activities themselves — not through the Naval Education and Training Command (NETC) / Naval Air Warfare Center Training Systems Division (NAWCTSD) schoolhouse-procurement chain that the 2026-05-25 right-to-win-reframe dialogue tested and that the 2026-05-25 find_sources diagnostic disconfirmed at the AI-search level. The engagement strategy in section 11 will be updated once the next find_sources pass produces source-grounded customer-organization identification under the corrected scope.

This research track was initiated based on a working observation shared by a working-level Navy ship-repair contact, captured anonymously per section 9.3. Everything in this file is supported by public sources alone; the contact is not named and is not the source of any factual claim.

**What is out of scope after the 2026-05-26 correction.** Schoolhouse / individual-Sailor curriculum delivery through the NETC pipeline, Ready Relevant Learning (RRL) / Sailor 2025 / NAWCTSD training-systems content development, and surface-warfare schoolhouse curriculum work generally. The 2026-05-25 right-to-win-reframe dialogue tested those framings; the next-day correction explicitly moved the scope away from them. They remain in `_red-teams/` for analytical lineage but are no longer load-bearing for the recommendation. Also out of scope after the 2026-05-24 narrowing: the broader ship-repair industrial base, the shipbuilding-capacity question, private ship-repair contractor competition, surge-repair capacity planning at scale, and the U.S.-Japan industrial partnership thread (Stimson Center Military Shipbuilding, Maintenance, and Repair Operations Task Force).

The hypothesis in section 7 is one possible outcome of this research — not a finding. The research plan in section 10 deliberately includes evidence that would falsify the hypothesis. The engagement strategy in section 11 is sequenced so that the relationship-development work proceeds in parallel with the hypothesis-testing work. Sections 7 and 11 will be rewritten end-to-end after the next find_sources pass produces ingested primary sources grounding the corrected scope.

## 2. Open questions

Listed with explicit disconfirming-evidence items per the scaffolding instruction. Items with the prefix **[DISCONFIRMING]** are the questions whose answers, if affirmative, would falsify the working hypothesis in §7 — and therefore should be answered EARLY in the research process before further investment.

- [ ] What is NSWC Carderock Division's publicly-discussed scope of work on BDR and ship survivability modeling? (NAVSEA publications, public RFP/RFI history, GAO reports referencing Carderock.)
- [ ] What battle-damage rate, damage type distribution, and repair-time assumptions are currently used in Navy / joint training exercises that involve multidomain elements? (Joint LVC programs, INDOPACOM J7 PMTEC overlap, Naval Warfare Development Command publications.)
- [ ] What repair-capacity assumptions are visible in public PAE-IO contract awards, congressional testimony, GAO reports on ship maintenance, and DoD industrial-base assessments?
- [ ] **[DISCONFIRMING]** Do current Navy fleet training documents or DON Strategic Readiness Plans already explicitly assume warfighting-scale attrition and battle damage? If yes, the "training assumptions understate wartime damage" leg of the hypothesis fails.
- [ ] **[DISCONFIRMING]** Are PAE-IO's planning assumptions visibly aligned with realistic warfighting attrition rates (per testimony, IDIQ task-order language, or industrial-base assessments)? If yes, the "IO industrial planning understates demand" leg of the hypothesis fails.
- [ ] **[DISCONFIRMING]** Is the OSI-releasable subset of Carderock's BDR modeling sufficiently high-fidelity to drive operationally-meaningful training injection? If the public version is purely doctrinal or coarse-grained, the "Carderock can quantify the gap" leg of the hypothesis fails — the actually-useful modeling lives behind classification and is unavailable to this research track.
- [ ] **[DISCONFIRMING]** Are there already named programs, partnerships, or joint LVC efforts that integrate Carderock survivability/BDR modeling into multidomain training? If yes, the "integration is needed" framing of the hypothesis is wrong; the integration may already be done, in which case the research track pivots to "how is it currently done, and is it working."
- [ ] What is the actual classification gradient of naval BDR / ship survivability modeling, and what subset is OSI-releasable? (Pre-research scoping; may require direct outreach to NAVSEA Public Affairs.)
- [ ] Is this research track better framed as a CACI capability investment, a teaming-opportunity scan, or a customer-education paper for NAVSEA / NWDC / OPNAV?

### Training-design questions (added 2026-05-21 scope expansion)

- [ ] What does a robust training-progression model look like for BDR — tabletop scenarios → guided site visits → pilot repair operations? What are the right learning objectives at each phase, and which audiences (junior officers, damage-control teams, repair-yard supervisors, multi-domain joint planners) get which content?
- [ ] What existing Navy / Joint training programs already use a tabletop-to-pilot progression model that could be a template or partner (e.g., Naval War College wargames, NSWCD damage-control schools, MARFOR readiness exercises)?
- [ ] Where would tabletop content draw from at OSI fidelity, given the §9.1 classification gradient? (Open-source threat libraries; sanitized vignettes from public NAVSEA / Carderock material; historical case studies — USS Cole, USS Stark, USS Fitzgerald, HMS Sheffield, Moskva — these are factually OSI and the lessons-learned are public.)
- [ ] What facilities support guided site visits at the next fidelity step? (NSWC Carderock proper; NSWC Philadelphia; intermediate maintenance activities; the four public naval shipyards; major private repair facilities — specific contractor names added only as sources surface them.)
- [ ] What does "pilot repair operations" look like at the top of the training progression — simulator-based, real-equipment-on-instrumented-test-bed, or live operations on training hulls? Which model is feasible at unclassified level?
- [ ] **[DISCONFIRMING]** Is there an existing Navy training program that already does the full tabletop→site-visit→pilot progression for BDR? If yes, the gap is execution / scaling, not design — the recommendation shape changes.

### BDA team preparedness questions (added 2026-05-21 scope expansion #2)

- [ ] What is the Navy's current BDA training pipeline? Who owns it — Naval Warfare Development Command (NWDC), Surface Force Training and Readiness Manual (SFTRM) authorities at COMNAVSURFOR, AFLOATRAFOR, fleet-specific shops, or some combination?
- [ ] **[DISCONFIRMING]** Is there already a mature DoD-funded BDA serious-game or instrumented-sim product? Search SBIR Phase II/III awards (`sbir.gov`), NWDC product catalog, Naval Postgraduate School / Naval War College thesis library, MORS conference papers. If a usable product exists, the play shifts from "build a BDA-sim platform" to "integrate / extend an existing one."
- [ ] **[DISCONFIRMING]** Is BDA-team training already deeply embedded in fleet exercises (COMPTUEX, RIMPAC, Large-Scale Exercise / LSE, ANTX, Trident Warrior)? If yes, the real-world-exercise leg of this scope is execution-only, not opportunity-creation.
- [ ] What commercial or government-off-the-shelf serious-game and simulation engines are candidate platforms for a Navy BDA training pipeline? Specific platforms to be named as sources surface them or as the operator scopes a vendor inquiry; cost, classification, and intellectual-property posture of each platform are open questions.
- [ ] What AR / VR or hardware-in-the-loop sim products exist for damage-control / BDA today? (Trade-show coverage at I/ITSEC; SBIR award database; vendor public press.)
- [ ] Can ARKA EO/IR / hyperspectral sensor signature libraries (or other CACI legacy ISR data products) plausibly feed a BDA training-game scenario engine with realistic threat-effect signatures? If so, that is a near-unique differentiator vs. the SAIC / Leidos / HII Mission Technologies incumbents.
- [ ] Where does a gamified-sim-then-real-world progression live administratively — under a training contract (e.g., AFLOATRAFOR), an R&D vehicle (Carderock RDT&E), an SBIR sequence, or a NAVWARDEVCOM doctrine product? Each implies a different acquisition pathway and a different prime / sub posture.
- [ ] What is the audience scoping for BDA teams: ship-level damage-control teams, fleet-level BDA cells, joint multidomain BDA staff at Combatant Commands, or all three at different depths?

### NSWC relationship-development questions (added 2026-05-21 scope expansion)

- [ ] Who are the named technical and engagement leads at NSWC Carderock Division for BDR / ship survivability modeling? (Public sources: NSWCD command directory, NAVSEA org chart, recent Carderock-authored conference papers, SBIR / STTR topic-author bylines.)
- [ ] What is Carderock's standing industry-engagement posture — industry days, SBIR / STTR cadence, BAA topics, Federal Lab Consortium tech-transfer queue? (Inventory all public engagement-on-ramps before pursuing custom outreach.)
- [ ] What warm-intro paths does CACI have to NSWC Carderock today? (Audit: CACI prior Carderock contracts via USAspending, CACI personnel with NSWCD work history, CACI Navy lab relationships at adjacent NSWC sites — Dahlgren, Crane, Indian Head — that might bridge.)
- [ ] What adjacent CACI relationships might broker introductions: NAVSEA leadership, ONR program officers, NWDC, Naval War College, Naval Academy faculty, SNAME, ASNE?
- [ ] **[DISCONFIRMING]** Does CACI already have an active, productive Carderock relationship that the operator was unaware of? (Internal CACI BD database check.)
- [ ] What is the realistic timeline for relationship-development given Carderock's typical engagement cadence — months, not weeks; multi-touch sequence; formal industry-day plus follow-on technical engagements?
- [ ] What is the right CACI entry-vehicle — SBIR proposal, BAA white paper, sub-tier role on an existing Carderock vehicle, or direct NDA-only technical exchange?

## 3. Demand signal — what the Navy is publicly saying and buying that maps to the operational-decision-scenario scope

This section captures the public-record demand signal under the 2026-05-26 corrected scope at §1 — gamified operational-decision scenarios for the professional Battle Damage Assessment and Repair (BDAR) team at Navy repair activities. The section answers four overlapping questions. What is senior Navy leadership publicly saying about wartime and contested repair? What exercises is the Navy publicly running that have the same shape as the proposed scenario portfolio? What is the open-source defense policy community amplifying as a gap? And where is contractor procurement actually happening today at the specific customer organizations §1 names as candidates? The section was drafted as the first small-ship under the workflow at `_meta/small-ships-workflow.md`, with FACT claims listed before prose and the verifier run against the claim list before red-team.

The picture is consistent across the four signals. The Navy is publicly committing dollar volume to combat surge readiness and naming contested logistics as the threat environment. The Navy is publicly executing the most directly relevant exercise type (Ship Wartime Repair and Maintenance Exercise, SWARMEX) in the most directly relevant venue (forward Pacific port, allied participation, contractor coordination). The defense policy community is publicly pressing the gap. And the Navy is already procuring contractor-supplied professional support services at the Commander, Navy Regional Maintenance Center (CNRMC) — the parent command of the Regional Maintenance Centers (RMCs) that §1 names as candidate customers. The four signals converge to give the §7 working hypothesis prior weight; what the rest of the research has to produce is the open question of whether CACI's specific entry path is via the existing CNRMC professional-services vehicle, via a separate procurement at one of the named customer organizations, or via the fleet-command exercise authorities outside the CNRMC chain.

### 3.1 Senior-leadership signal

Senior Navy leadership names wartime repair and combat surge readiness as load-bearing for FY27 across two independent public artifacts. The Chief of Naval Operations testifies to ship maintenance as a "warfighting requirement," and the Department of the Navy's FY27 President's Budget Press Brief commits dollar volume to surge readiness and names contested logistics as the threat environment.

**FACT:** Admiral Daryl L. Caudle, the Chief of Naval Operations, delivered a Statement on the Posture of the United States Navy before the House Armed Services Committee (HASC) on 14 May 2026, addressing FY27 budget content [s.2026-05-26-2026-05-14-caudle-testimony].

**FACT:** The Caudle HASC testimony announces a planned deliberate study of Navy yard capacity, examining shortfalls, future force requirements, and operational considerations, and emphasizes maintenance as a warfighting requirement [s.2026-05-26-2026-05-14-caudle-testimony].

**FACT:** The Department of the Navy's FY 2027 President's Budget Press Brief, dated 28 April 2026, funds Ship Maintenance at $17.0 billion (including Other Procurement, Navy) explicitly to drive the fleet toward an *"80% Combat Surge Ready (CSR) posture by reducing maintenance delays and applying a disciplined focus across manning, training, modernization, and sustainment"* [s.2026-05-26-don-fy27-press-brief].

**FACT:** The DON FY27 Press Brief includes a separate $0.6 billion line item for Contested Logistics, justified explicitly because *"adversaries will target supply lines, ports, and communications"* [s.2026-05-26-don-fy27-press-brief]. *Scope note:* the Contested Logistics line item funds physical logistics resilience (spares, fuel distribution, lift capability, port-security assets), not training scenarios. Cited here as background environment, not as procurement signal for the corrected-scope product.

**FACT:** The DON FY27 Press Brief lists 37 Forward Deployed Naval Forces (FDNF) ships per the same artifact [s.2026-05-26-don-fy27-press-brief].

**Assessment.** Senior leadership is naming Combat Surge Ready posture as the target readiness metric and naming contested logistics as the threat environment for fleet sustainment. Both signals describe the operational context the corrected-scope product would train against — but neither names training scenarios or exercise-injection content as a specific procurement line. The procurement-evidence weight for the corrected-scope product is at §3.5 (Joint / USMC exercise-design funding) and §3.6 (vehicle-taxonomy prototype), not §3.1.

### 3.2 Navy public exercise events

The single most directly scope-relevant artifact is the Ship Wartime Repair and Maintenance Exercise (SWARMEX) — a Navy-named, Navy-executed exercise event that rehearses exactly the decision moments §1 lists as candidate scenario content.

**FACT:** U.S. Seventh Fleet, the Ship Repair Facility–Japan Regional Maintenance Center (SRF-JRMC), U.S. Pacific Command (USINDOPACOM), and U.S. Pacific Fleet (COMPACFLT) all published parallel releases announcing that USS Ashland (LSD 48) completed Ship Wartime Repair and Maintenance in Cebu, Philippines, in coordination with Philippine Navy partners and local Philippine contractors [s.2026-05-26-uss-ashland-completes-ship-war].

**FACT:** Naval News covered the same SWARMEX-Cebu event and named Philippine Naval Sea Systems Command participation [s.2026-05-26-u-s-navy-rehearses-wartime-rep].

**FACT:** The SWARMEX-Cebu exercise involved an amphibious warfare ship operating at a foreign port, host-nation contractor coordination for repair work, and Philippine naval participation [s.2026-05-26-u-s-navy-rehearses-wartime-rep].

**FACT:** A Defense Visual Information Distribution Service (DVIDS) news release covered USS Iwo Jima's damage controlmen training the crew in simulated casualty scenarios (flooding, fire, hull rupture) for shipboard damage control [s.2026-05-26-dvids-news-dont-give-up-the-sh]. *Scope note:* This is shipboard organic damage control at the deck-plate level, which is exactly the layer the 2026-05-26 scope correction moved away from. Included here only as evidence that the Navy publicly catalogs damage-related training content; the corrected-scope product targets the assessment-team and repair-team operational-decision layer above the deck-plate damage-control layer, not the deck-plate layer itself.

**Assessment.** The SWARMEX-Cebu artifact maps onto three of the six decision moments named in §1: forward team mobilization to where the damaged ship actually is, emergency contracting in a foreign port, and host-nation legal and operational framework navigation. It is a Navy-executed exercise that literally rehearses the operational-decision moments the recommendation will eventually propose as a scenario portfolio. The §11.3 BDAT pipeline section will be rebuilt around SWARMEX-class exercises as the anchor training event, with the proposed contractor product being the scenario-design and exercise-injection content these events run on.

### 3.3 Policy-community pressure

The open-source defense policy community is publicly arguing that the Navy's expeditionary repair capability is undersized for wartime operations.

**FACT:** The U.S. Naval Institute's professional journal Proceedings published an article titled *"Fix the Navy's Expeditionary Repair"* arguing that the current expeditionary repair capability is inadequate to support fleet operations under wartime contestation conditions [s.2026-05-26-fix-the-navys-expeditionary-re].

**FACT:** The Center for International Maritime Security (CIMSEC) published *"If the U.S. Navy Can't Repair Ships in Peacetime, How Will It Do So in War?"* — arguing that current peacetime repair throughput is the floor and wartime repair throughput needs to be higher [s.2026-05-26-if-the-u-s-navy-cant-repair-sh].

**Assessment.** When USNI Proceedings and CIMSEC pipelines converge on the same gap independently, the Navy professional community is signaling that the gap is a legitimate Navy-operational concern, not just a budget-process talking point. The §11.1 engagement-surface inventory will use both publications as engagement anchors — both have established readership inside the customer organizations §1 names as candidates.

### 3.4 Navy physical-plant investment (environmental context, not procurement signal)

The dollar flows behind the senior-leadership signal land at the physical-plant layer of the corrected-scope customer organizations — public shipyards getting drydock modernization and infrastructure investment. This is environmental context for the research, not procurement-demand evidence for the corrected-scope product. SIOP and MILCON are wrong color of money for scenario design or wargaming; the recommendation will not chase that funding directly.

**FACT:** The DON FY27 Press Brief funds the Shipyard Infrastructure Optimization Program (SIOP) at $1.8 billion and the broader Maritime Industrial Base (MIB) at $7.0 billion for FY27 [s.2026-05-26-don-fy27-press-brief].

**FACT:** The FY27 Military Construction (MILCON) budget invests in six SIOP projects per the DON FY27 Press Brief [s.2026-05-26-don-fy27-press-brief].

**FACT:** Norfolk Naval Shipyard began a $442 million drydock modernization in May 2026 [s.2026-05-26-norfolk-naval-shipyard-begins-].

**FACT:** Pacific Naval Facilities Engineering Command (NAVFAC) published a SIOP brief documenting Puget Sound Naval Shipyard and Subordinate Bases (PSNS-SBS) infrastructure investments [s.2026-05-26-siop-brief-psns-sbs-2025-1].

**Assessment.** The §3.4 dollar flow is evidence that Navy senior leadership is willing to commit volume to repair-activity capability at the infrastructure level. It is NOT a procurement signal for the operational-decision-scenario product set — SIOP is MILCON, the broader MIB investment is shipbuilding industrial base, and neither pays for training scenarios or scenario-design contractor work. The procurement-evidence weight for the corrected-scope product is at §3.5.

### 3.5 Contractor-procurement signal for exercise design and scenario generation

The procurement evidence for the corrected-scope product set splits into two layers — a Joint / Marine Corps layer that demonstrates the federal procurement budget does fund contractor-delivered exercise design and scenario generation, and a Navy-customer layer (Invictus / CNRMC) that demonstrates the named customer organizations procure contractor support but not yet through the right vehicle for this work.

**Joint / USMC level — direct procurement-evidence weight.** The Department of Defense FY27 budget justification book funds contractor-delivered exercise design and scenario generation as explicit capability lines.

**FACT:** The FY27 Department of Defense budget justification book funds, as part of the Marine Air-Ground Task Force (MAGTF) Tactical Warfare Simulation, *"developing an exercise planning, design, implementation, execution, and control tool ... enabling exercise designers the ability to rapidly build new scenarios and incorporate human geography elements into the training scenarios"* [s.2026-05-26-justification-book].

**FACT:** The same FY27 justification book initiates *"design and development of a joint exercise design and control tool ... providing exercise planning, design and control within various joint simulation constructs"* [s.2026-05-26-justification-book].

**FACT:** The same FY27 justification book funds Scenario Generation as a named capability line — *"Delivery of AI-powered scenario generation capability within JTT [Joint Training Tools]. This will be a massive education and training effort to get JExD [Joint Exercise Design] and exercise planners up to speed with new capability"* [s.2026-05-26-justification-book].

**Assessment.** The Joint / USMC exercise-design funding lines in the FY27 budget justification book are direct primary-source evidence that the Department of Defense procures contractor-delivered exercise design and scenario generation, names "exercise planners" and "Joint Exercise Designers" (JExD) as a workforce category, and is funding AI-powered scenario-generation capability development. This is the procurement-evidence baseline. The §5 and §7 investigation has to identify which Navy fleet-command authorities procure analogous work for fleet exercises.

**Navy-customer level — CNRMC procures contractor support, but not through this vehicle.** The Invictus Associates contract is the single direct public-record evidence that the parent command of the corrected-scope customer set (CNRMC) procures contractor support. The contract is NOT direct evidence for the corrected-scope product — the vehicle category (Professional Support Services on a SeaPort-NxG Multiple-Award Contract) is the wrong color of money for wargaming or scenario design — but the customer-naming is load-bearing.

**FACT:** Per the USAspending award record, Invictus Associates LLC has a Navy delivery order obligating $19,384,385 for Professional Support Services (PSS) — specifically Fleet Readiness Support for Commander, Navy Regional Maintenance Center (CNRMC), its subordinate Regional Maintenance Centers (RMCs), and Surface Team One (ST1) [s.2026-05-26-professional-support-services-]. *Note: the award record does not include period start/end dates, so active-status cannot be confirmed from this source alone.*

**FACT:** The Invictus delivery order is identified by Procurement Instrument Identifier (PIID) N0016424F3006 against an existing Multiple-Award Indefinite Delivery Contract (parent PIID N0017819D7883), with place of performance in Norfolk, Virginia [s.2026-05-26-professional-support-services-].

**FACT:** The funder of the Invictus contract is the Department of Defense / Department of the Navy [s.2026-05-26-professional-support-services-].

**Assessment.** The Invictus contract has two analytical functions in §3. **First**, it confirms that CNRMC (the parent command of the RMCs §1 names as candidate customers) does procure contractor-supplied support, naming Surface Team One (the Navy's surface readiness organization) alongside CNRMC and the subordinate RMCs as covered customers. That is direct evidence that contractor procurement reaches the corrected-scope customer set today. **Second**, the vehicle category — Professional Support Services as administered through the parent SeaPort-NxG Multiple-Award Contract identified by PIID N0017819D7883 — is the Navy's generic-services contracting vehicle. PSS through SeaPort-NxG buys staff augmentation, program management, administrative support, and metrics tracking; it does not by category buy wargaming or scenario design. The Invictus contract is therefore evidence the right customer procures contractor support and evidence the wrong vehicle is the wrong vehicle. The §5 and §7 investigation has to identify the Navy fleet-command equivalent of the named Exercise / Wargames / Decision-Support vehicles surfaced in §3.6 — the procurement-pathway prototype that tells us what kind of vehicle to hunt for.

### 3.6 Procurement Pathway Prototype — vehicle taxonomy baseline for §5 and §7

This subsection is in §3 deliberately. Three large federal contracts surfaced during the 2026-05-25 USAspending triage are NOT Navy-funded and NOT §3 Navy demand-signal evidence. They are in §3 as the **vehicle-taxonomy baseline** — examples of how the Department of Defense buys contractor-delivered exercise design, wargames support, and Combatant Command decision support when it decides to buy this work. The §5 (competitive landscape) and §7 (working hypothesis) investigations need to hunt for the Navy-equivalent named vehicles. The non-Navy contracts tell us what the right vehicle-shape looks like.

**FACT:** CACI NSS LLC holds a $194 million contract for *"Plans, Operations, Logistics, Engagement, Training, Exercise, and Assessment Support to AFRICOM"* — Department of Defense / Department of the Army funder, General Services Administration awarder, GSA OASIS-style indefinite-delivery vehicle [s.2026-05-26-the-purpose-of-this-award-is-t].

**FACT:** Parsons Government Services Inc. holds a $556.8 million Command, Control, Communications, Computers, Combat Systems, Intelligence, Surveillance, Reconnaissance, and Targeting (C5ISR) / Exercises / Operations / Information Services (CEOIS) task order providing near real-time situational awareness and decision support to the Department of Defense Combatant Commands — Office of the Secretary of Defense funder via GSA [s.2026-05-26-the-purpose-of-this-award-is-f].

**FACT:** Axient LLC holds a $233.8 million Test, Exercise and Wargames Support contract — Missile Defense Agency funder [s.2026-05-26-test-exercise-and-wargames-sup].

**Assessment.** When the Department of Defense decides to buy exercise design, wargames support, decision support, or training scenarios, it buys it under EXPLICITLY-NAMED vehicles — the AFRICOM "Plans, Operations, Logistics, Engagement, Training, Exercise, and Assessment Support" task order; the OSD CEOIS "Exercises, Operations, and Information Services" task order; the MDA "Test, Exercise and Wargames Support" definitive contract. These names are the procurement-pathway prototype. The §5 and §7 investigation has to identify the Navy-equivalent named vehicle for the corrected-scope product — somewhere in the fleet-command (FLTFORCOM / COMPACFLT / COMPTUEX / RIMPAC / Large-Scale Exercise) procurement ecosystem, or possibly through SRF-JRMC's own wartime-readiness procurement directly. The named-vehicle gap is the contracting-pathway gap the recommendation has to close.

### 3.7 Convergence assessment

The five signals — senior-leadership statements (§3.1), the SWARMEX-Cebu exercise artifact (§3.2), the USNI / CIMSEC policy-community pressure (§3.3), the Joint / USMC contractor-exercise-design funding lines in the FY27 comptroller justification book and the CNRMC contractor-support footprint via Invictus (§3.5), and the non-Navy Procurement Pathway Prototype that tells us what vehicle-shape to hunt for in Navy (§3.6) — converge on a coherent picture under the corrected scope. Senior Navy leadership is publicly committing to wartime repair capability and combat surge readiness. The Navy is publicly executing the most directly relevant exercise type in the most directly relevant venue (SWARMEX-Cebu). The Navy professional community is publicly arguing the gap is real. The Department of Defense procures contractor-delivered exercise design and scenario generation at the Joint and Marine Corps levels — that procurement pattern is real and named in the FY27 budget. CACI specifically is already executing exercise / training / operations support work at AFRICOM and adjacent COCOMs at multi-hundred-million-dollar scale.

What §3 does NOT yet establish — and what §5 (competitive landscape) and §7 (working hypothesis) have to test as the load-bearing analytical work — is the specific Navy fleet-command vehicle under which a **1-hour turn-based gamified decision-scenario session for a staff cell or wardroom audience** would be procured. The DoD knows how to buy a multi-month, multi-million-dollar contractor team to plan and execute a Pacific Fleet SWARMEX; what is less obvious is how a local SRF commander or RMC training-cell head buys a short-form, high-fidelity decision-rehearsal session for a small repair-leadership audience under combat-tempo or contested-port conditions. The format-and-cadence distinction — short-form, high-fidelity, decision-tier audience, executed inside the rhythm of fleet exercise events rather than as a standalone training pipeline — is the specific sub-product whose Navy procurement pathway is the open question. §5 and §7 carry the burden of closing this gap.

Material from the prior §3 framing — Stimson Center MSMRO Task Force, GAO shipbuilding-oversight testimony, the FY27 shipbuilding $65 billion total, the White House Maritime Action Plan, the U.S.-Japan trade arrangement, and the Maritime Administration Port Infrastructure Development Program — is preserved in git history and in the 2026-05-25 corpus-cleanup dialogue. Under the corrected scope these are context-level rather than load-bearing for the recommendation.

<!-- ship: 2026-05-26 claude-opus-4-7 -->
<!-- pilot-section: first small-ship under _meta/small-ships-workflow.md -->
<!-- claim-count: 22 FACT + 7 Assessment + 0 Speculation. Verifier run 2026-05-26 (17 SUPPORTS / 4 PARTIAL / 0 DOES_NOT_SUPPORT / 0 UNVERIFIABLE). Red-team Gemini Pro Round 3 verdict: GO (3-round dialogue, see _red-teams/2026-05-26-gemini-pro-section-3-red-team-dialogue.md). Sealed 2026-05-26. -->


## 4. Customer landscape

> **Scope note added 2026-05-25.** This section was drafted around the prior NAVSEA / Carderock framing of the research. The 2026-05-25 right-to-win-reframe dialogue surfaced an alternative training-systems-chain hypothesis for BDAR/BDAT training procurement — see `_red-teams/2026-05-25-gemini-pro-right-to-win-reframe-dialogue.md` and decision log entry 2026-05-25. The named-customer mapping below remains in the vault as the prior-framing customer set; if the next find_sources pass produces ingested sources naming the alternative training-systems-chain organizations, this section will be expanded (not retroactively edited) to cover both customer chains.

This section maps the candidate downstream customers for this research track. Each claim below is sourced from an ingested primary source and carries a citation tag. Names of specific commercial contractors are deliberately scoped to what sources surface organically; the per-opportunity allowlist at `_entity-allowlist.yaml` documents any operator-blessed exceptions. Cross-reference to `03_pocs.md` for the points-of-contact table as it gets populated.

### 4.1 Senior civilian and uniformed leadership at the top

**Department of the Navy leadership as named in the May 2026 Shipbuilding Plan and the May 14, 2026 CNO testimony to the House Armed Services Committee.** Acting Secretary of the Navy Hung Cao signed the foreword of the Navy's May 2026 Shipbuilding Plan [s.2026-05-23-navy-shipbuilding-plan-2026]. **FACT.** The 34th Chief of Naval Operations, Admiral Daryl L. Caudle, signed the same plan's CNO foreword and delivered the FY27 budget posture statement to the House Armed Services Committee on 14 May 2026 [s.2026-05-23-navy-shipbuilding-plan-2026][s.2026-05-14-caudle-testimony]. **FACT.** General Eric M. Smith, the 39th Commandant of the Marine Corps, signed the Marine Corps foreword [s.2026-05-23-navy-shipbuilding-plan-2026]. **FACT.**

**U.S. Secretary of the Navy John Phelan** chose Japan as his first foreign trip destination and publicly supported a greater Japanese role in maintenance, repair, and overhaul for the U.S. Navy [s.2026-05-23-the-time-is-ripe-for-next-step]. **FACT.** Phelan also expressed interest in working with Japan to co-develop and co-produce dual-use ships [s.2026-05-23-the-time-is-ripe-for-next-step]. **FACT.**

### 4.2 The NAVSEA organizational structure consolidated under PAE Industrial Operations

**The Navy's May 2026 Shipbuilding Plan describes a Navy-internal organizational consolidation, called PAE Industrial Operations, that combines the Navy Regional Maintenance Centers, NAVSEA's Industrial Operations Directorate, and the four public Navy Shipyards into a single structure** [s.2026-05-23-navy-shipbuilding-plan-2026]. **FACT.** The plan describes the intent of this structure as tying "the contracting functions for maintenance work with the fleet components that must have responsibility for the ships themselves" [s.2026-05-23-navy-shipbuilding-plan-2026]. **FACT (direct quotation).**

The four public Navy shipyards under this structure are named in CNO Caudle's testimony as Pearl Harbor Naval Shipyard (PHNS), Puget Sound Naval Shipyard (PSNS), Portsmouth Naval Shipyard (PNSY), and Norfolk Naval Shipyard (NNSY) [s.2026-05-14-caudle-testimony]. **FACT.**

### 4.3 NSWC Carderock — modeling source

NSWC Carderock Division is the most-named candidate downstream customer for this research track. The vault glossary at `_meta/glossary.md` defines Carderock as the NAVSEA Naval Surface Warfare Center division responsible for ship survivability and damage modeling. Specific Carderock leadership and POCs remain a research target — the §11.1 engagement-surface inventory has not yet been populated.

### 4.4 OPNAV / N9 — fleet-readiness demand-side

OPNAV (the Office of the Chief of Naval Operations) and specifically N9 (the Warfare Systems directorate) own the fleet-readiness demand picture. CNO Caudle's testimony frames the FY27 posture around four named priorities: "Lethal & Effective Force" (Force Structure), "Total Force Readiness" (Infrastructure, Maintenance, Operations, and Spares), "Capable & Resilient Warfighter," and "Industrial & Logistics Capacity" [s.2026-05-14-caudle-testimony]. **FACT.** The second priority directly governs the maintenance budgets and shipyard work that this research track is concerned with.

### 4.5 The Pacific Fleet engagement layer — SRF-JRMC and adjacent organizations

The Ship Repair Facility, Japan Regional Maintenance Center (SRF-JRMC) ran the first Japan Ship Wartime Repair and Maintenance Exercise (SWARMEX) on USS FITZGERALD (DDG 62) in cooperation with the Japan Maritime Self-Defense Force (JMSDF) and Japan Maritime United (JMU), per a NAVSEA Public Affairs release [s.2026-05-23-swarmex-srf-jrmc]. **FACT.** Per the research-discipline note in §9.3, SRF-JRMC and adjacent Pacific Fleet ship-repair organizations are research subjects engaged via standard public-facing paths only.

The Stimson Center's U.S.-Japan Task Force on Military Shipbuilding, Maintenance, and Repair Operations (MSMRO) released recommendations on 25 March 2026 calling for increased Repair, Maintenance, and Industrial work in Japan and adjacent third-country locations including the Philippines, Australia, and Guam [s.2026-05-23-the-time-is-ripe-for-next-step]. **FACT.** The Task Force was co-led by Andrew Oros (Stimson Senior Fellow, Director, Japan Program) and Steve Brock (former Senior Advisor to the Secretary of the Navy, April 2022 to January 2025) [s.2026-05-23-the-time-is-ripe-for-next-step]. **FACT.** *Scope note 2026-05-25:* same context-level qualifier as §3.1 — the Stimson MSMRO thread is environmental context for understanding the Pacific repair-capacity picture, not load-bearing for the BDAR/BDAT training procurement question.

### 4.6 Maritime Action Plan governance and the Department of War rebranding

The Trump administration's Maritime Action Plan designates the Department of Commerce as the lead on foreign investment in the shipbuilding sector and designates the Department of the Navy in a formal advisory role in that process [s.2026-05-23-the-time-is-ripe-for-next-step]. **FACT.** Executive Order 14269 ("Restoring America's Maritime Dominance") and Executive Order 14372 ("Prioritizing the Warfighter in Defense Contracting") frame the broader policy direction [s.2026-05-23-navy-shipbuilding-plan-2026]. **FACT.**

The defense.gov → war.gov server migration has been visible throughout this research — multiple Navy and Department of War PDFs and transcripts could not be ingested through their original defense.gov URLs because the war.gov redirects 404. This is documented in §8.2 of the source ledger. **Assessment:** the rebranding is operationally consequential because publication paths are not yet stable across the migration; future research should expect URL volatility for any DON document published through 2026.

### 4.7 Assessment of the customer landscape

The customer landscape is not a single organization but a layered set, and the layering matters for any future capture decision.

At the top is the strategic-direction layer — the White House, the Maritime Action Plan, the Acting Secretary of the Navy, and the CNO. They set the priorities and the dollar scale. The May 2026 Shipbuilding Plan and the May 14 CNO testimony are the two most consequential primary-source documents in this layer.

Underneath that is the execution layer — NAVSEA, the PAE Industrial Operations consolidated structure that ties together the Navy Regional Maintenance Centers, NAVSEA's Industrial Operations Directorate, and the four public Navy shipyards. This is where ship repair and maintenance work actually happens. The CNO's stated priorities about workforce, SIOP investment, and the SIMA stand-up all live in this layer.

Underneath that is the demand layer — the deployed and forward-deployed fleet that needs the repair capacity. This is where SRF-JRMC, the Seventh Fleet, and U.S. Pacific Fleet show up. The SWARMEX program is a Pacific Fleet demand signal materialized as an exercise.

The research-discipline note in §9.3 governs how the SRF-JRMC layer is engaged. Engagement at the strategic and execution layers proceeds through standard public-facing paths (industry days, formal SBIR/STTR responses, NAVSEA-hosted touchpoints), and the §11.1 engagement-surface inventory is the work stream that maps those touchpoints. The research-discipline note also makes clear that engagement at the demand layer does not leverage the operator's working-level contact — that channel stays outside the vault per §9.3.

## 5. Competitive landscape

<!-- sensitivity:internal -->

This section catalogues the named competitive actors that appear in ingested sources, plus the operator-allowlisted naval modeling-and-simulation incumbents required by the §7 hypothesis. Per the named-contractor discipline at `_meta/feedback_named_contractor_discipline.md`, specific commercial entities appear here only when a source has surfaced them organically or the per-opportunity allowlist documents why they are allowed.

### 5.1 Shipbuilders named in the May 2026 Navy Shipbuilding Plan

> **Re-framing added 2026-05-25 from corpus-cleanup dialogue.** The shipbuilders below are listed here as background context for the new-construction industrial base. The 2026-05-25 corpus-cleanup dialogue surfaced an analytical question about whether any of these shipbuilders might be a competitor for BDAR/BDAT training procurement in a different way: as platform-sustainment primes whose existing platform contracts could **bundle** BDAR/BDAT training-and-simulation content into broader sustainment work. This is the **Platform-Sustainment Bundling Hypothesis** — BDAR/BDAT training rides into the fleet on existing platform-sustainment contracts held by shipbuilders or their integration subs. The competing hypothesis is the **NAWCTSD Training-Prime Hypothesis** — BDAR/BDAT training procures separately through the Navy training-systems chain (training-systems prime via a training-systems program office, executed against Surface Warfare Schools Command or similar Navy training-organization requirements). Both hypotheses are unverified; the next find_sources pass is designed to test both. Neither hypothesis is endorsed in this section yet. See `_red-teams/2026-05-25-gemini-pro-corpus-cleanup-dialogue.md` item C and decision log entry 2026-05-25.

The Shipbuilding Plan's appendices and program-specific sections name the following shipbuilders as the production base for the PB27 Five-Year Defense Program. None of these are direct competitors for the BDR research's modeling-and-simulation thread — they are the new-construction shipbuilding industrial base — but they are load-bearing for the §3 demand-signal picture about industrial capacity and surge planning.

- **Huntington Ingalls Industries (HII)** is described in the plan as a shipbuilder employing wage increases at its Newport News Shipbuilding subsidiary funded by the U.S. Government [s.2026-05-23-navy-shipbuilding-plan-2026]. **FACT.** HII Ingalls Shipbuilding is named as the builder of the LPD-17 Flight II class amphibious warships [s.2026-05-23-navy-shipbuilding-plan-2026]. **FACT.**
- **General Dynamics NASSCO**, San Diego, California, is named as the builder of the T-AO 205 class Fleet Replenishment Oilers; the first five hulls (T-AO 205-209) have delivered and T-AO 210 is planned to deliver in summer 2026 [s.2026-05-23-navy-shipbuilding-plan-2026]. **FACT.** The Navy plans to procure 20 ships in this class [s.2026-05-23-navy-shipbuilding-plan-2026]. **FACT.**
- **Electric Boat** is referenced in the plan as a beneficiary of the U.S. Government-funded wage increases driving improved hiring rates and reduced attrition at the submarine builders [s.2026-05-23-navy-shipbuilding-plan-2026]. **FACT.**
- **Bollinger** is named as the directed first-hull contractor for the Medium Landing Ship (LSM) class [s.2026-05-23-navy-shipbuilding-plan-2026]. **FACT.**
- **Fincantieri Marinette Marine** is named as the directed contractor for the next four LSM hulls; the remaining LSM hulls will be competitively awarded [s.2026-05-23-navy-shipbuilding-plan-2026]. **FACT.**
- **Austal USA** in Mobile, Alabama, is named as the contractor designing the T-AGOS 25 Class General Ocean Surveillance Ship, with construction planned to begin in late 2027 [s.2026-05-23-navy-shipbuilding-plan-2026]. **FACT.** The T-AGOS 25 program includes a planned class of 10 ships [s.2026-05-23-navy-shipbuilding-plan-2026]. **FACT.**

### 5.2 Naval modeling-and-simulation incumbents — operator-blessed per the hypothesis

The §7 working hypothesis leg 5 names three canonical naval-services incumbents whose existing Carderock-adjacent relationships could constrain CACI's entry timeline into this research's eventual recommendation. The per-opportunity entity allowlist at `_entity-allowlist.yaml` blesses these three names for analytical use without requiring source backing per appearance; specific FACT claims about any of them still require source backing per the SOP.

- **HII Mission Technologies** inherited prior naval modeling-and-simulation work via a 2021 corporate acquisition. *Assessment (cross-opportunity carry-over, not yet sourced for BDR):* HII Mission Technologies is the most directly competitive incumbent for Carderock-adjacent modeling capability and is the dominant unknown in §7 leg 5.
- **SAIC** is a canonical naval-services incumbent named in the §7 hypothesis. *Assessment:* SAIC's specific role in Carderock-adjacent modeling work is not yet sourced; ingest is open research.
- **Leidos** is a canonical naval-services incumbent named in the §7 hypothesis. *Assessment:* same as SAIC — specific role not yet sourced; ingest is open research.

No primary source ingested into this opportunity's `01_sources/` directory names any of these three in a Carderock-adjacent modeling context yet. The naming above carries the operator's blessing from the allowlist; the supporting FACTs remain to be developed through further source ingestion.

### 5.3 International partnership candidates — the Japan thread

The Stimson Center's U.S.-Japan MSMRO Task Force frames an alliance-level partnership thread that is structurally different from the U.S.-only competitive picture above. *Scope note 2026-05-25:* per the 2026-05-25 corpus-cleanup dialogue, the Stimson MSMRO material is treated as context-level for the broader Pacific repair-capacity question, not load-bearing for the BDAR/BDAT training-procurement question that drives the research recommendation.

- **Japan Maritime United (JMU)** is named in the SWARMEX press release as the host private shipbuilder for the first Japan SWARMEX exercise [s.2026-05-23-swarmex-srf-jrmc]. **FACT.** The exercise relocated from JMU's Maizuru Yard to the neighboring Japan Maritime Self-Defense Force (JMSDF) Maizuru facility due to mooring difficulties [s.2026-05-23-swarmex-srf-jrmc]. **FACT.**
- **The Japanese shipbuilding industry as a whole** is described by the Stimson Task Force as having declined from nearly half the global commercial-shipbuilding market share in the 1980s to just over 10 percent today, with Japan now aiming to double its shipbuilding output by 2035 under an initiative launched by Prime Minister Sanae Takaichi [s.2026-05-23-the-time-is-ripe-for-next-step]. **FACT.**
- **The July 2025 U.S.-Japan trade arrangement** includes $550 billion in Japanese government investment in strategic U.S. industries, including shipbuilding [s.2026-05-23-the-time-is-ripe-for-next-step]. **FACT.**

**Assessment:** the Japan-side actors are not direct competitors for the BDR research's modeling-and-simulation thread, but they are the most consequential partnership angle that emerged from the source pass. If the §7 hypothesis survives disconfirming checks and the recommendation shape eventually includes any forward-repair component, the Japan thread is where the alliance-side participation would come from.

### 5.4 What this section does not yet know

Three competitive layers are visible in the demand signal but not yet sourced at competitor level for this research.

- **Private U.S. ship-repair contractors** competing for Navy maintenance work are visible at the dollar-flow level (the §3.2 budget figures) but the specific contractor mix is not yet ingested. The next source-finder pass should target USAspending recipient data without pre-naming entities.
- **Carderock-adjacent technical partners** — the §7 leg 5 hypothesis names three (SAIC, Leidos, HII Mission Technologies) but the specific contract footprint of each at Carderock is open research. NAVSEA contracting data should resolve this when ingested.
- **Commercial simulation-platform vendors** for any future BDA training pipeline (§11.3) are explicitly an open research thread — section 11.3 of this file was rewritten on 2026-05-23 to remove all pre-named vendors and reads "specific platforms named only as sources surface them or as the operator scopes a vendor inquiry." Next steps for §11.3 are operator-initiated outreach (I/ITSEC, DoD SBIR Phase II catalogs, NWDC product listings) rather than further automated source searches against contractor names.

### 5.5 Assessment of the competitive landscape

The competitive picture is not yet sharp. What is clear from the ingested sources is the new-construction shipbuilding industrial base — HII, General Dynamics NASSCO, Bollinger, Fincantieri Marinette Marine, Austal USA, and Electric Boat are all named in the Navy's own May 2026 Shipbuilding Plan with specific program assignments. What is NOT yet clear from the sources is the ship-repair and modeling-and-simulation competitive picture, which is the actual layer of competition for any BDR research recommendation.

The §7 hypothesis names SAIC, Leidos, and HII Mission Technologies as the canonical incumbents to beat; the supporting FACTs to back specific capability claims about any of the three remain open research. The Japan-side partnership thread surfaced from the Stimson and SWARMEX sources is the most distinctive shape in the data and is more clearly a partnership angle than a competition angle.

The right next move on this section is targeted ingestion of NAVSEA contracting data (via USAspending), NSWC Carderock recent SBIR/STTR awards, and any DoD-level industry days on naval simulation-and-modeling vehicles. Until those land, this section is a scaffold with the new-construction shipbuilders confirmed and the BDR-specific competitive picture intentionally unfilled.

<!-- /sensitivity -->

## 6. Our fit

<!-- sensitivity:internal -->

*[Section reserved — populate after deciding (a) the customer field and (b) whether this is a CACI capture, a research-only track informing other captures, or a customer-education paper. The fit assessment depends on which framing is selected.]*

### 6.1 Existing footprint

*[To be populated. Relevant prior work in M&S, naval IT, training systems integration, etc.]*

### 6.2 Capability map

*[To be populated against whatever stated priority gaps emerge from §3.]*

<!-- /sensitivity -->

## 7. Working hypothesis

<!-- sensitivity:internal -->

This is the analyst's current best guess at what the research will show. It is a **hypothesis**, not a finding — flagged as an Assessment, not a FACT. It is here so the rest of the file has a target to test against. The research plan in section 10 is deliberately designed to try to break this hypothesis; whatever survives that effort gets promoted to a recommendation.

**The hypothesis in one paragraph:**

Current fleet training scenarios and PAE Industrial Operations' planning assumptions both significantly understate how badly ships get damaged in a real war. NSWC Carderock's damage modeling — to the extent it can be shared at unclassified level — can quantify that gap and become the source material for a new kind of training program. The program would step up in three stages: classroom-style tabletop scenarios first, then guided visits to repair facilities, then hands-on practice on instrumented training rigs. The step-up structure matters because each step can independently bring more classified content into the room, so the program can start fully unclassified and only graduate to classified material where it adds real value.

**Why this is still a hypothesis and not a recommendation:**

Acting on this would mean CACI investing in capture work, possibly hiring or partnering, and committing capital. Before any of that happens, the hypothesis has to survive a deliberate effort to disconfirm it — pulling the sources most likely to show that the gap does not exist, that the modeling is not releasable, that the program already exists, or that CACI cannot get in the door. The research plan in section 10 lists those disconfirming-evidence threads in priority order. The hypothesis should be re-evaluated after the first round of source ingestion, and either upgraded to a FACT-supported recommendation or revised or dropped.

There is also a relationship constraint that any recommendation has to clear: CACI does not currently have a working relationship with the Carderock damage-modeling team. The engagement work in section 11 has to make real progress in parallel with the source research, or the hypothesis surviving its disconfirming checks is academic.

**The six things that could falsify this hypothesis — refocused on BDAR/BDAT scope (2026-05-24):**

The hypothesis breaks into six separate claims, each of which can be tested against public sources. If any one of them fails, the corresponding part of the hypothesis is dead and the recommendation shape has to change. These legs were refocused on 2026-05-24 to match the BDAR/BDAT scope tightening; the prior framing was broader (general battle-damage-repair and industrial-base) and is preserved in the decision log entry for that date.

1. **The BDAR/BDAT training-and-simulation demand gap.** *Claim:* the Navy has a real and acknowledged gap in BDAR/BDAT training capability that is large enough to warrant new contractor solutions, visible in senior-leadership signals like the SRF-JRMC SWARMEX program description and the CNO's SIMA stand-up testimony. *What kills it:* the program descriptions turn out to be ceremonial or marketing rather than capability-building signals, and a closer reading shows that established Navy training pipelines already cover what BDATs need. The strongest counter-evidence would be a current NWDC product catalog or fleet schoolhouse curriculum document that explicitly addresses BDAR/BDAT training to a degree that closes the gap. *Note:* the working observation that initiated this research is consistent with this leg being true. That observation is informal and does not relax the requirement that public-source triangulation produce citable evidence before any recommendation. See section 9.3.

2. **The procurement-path reality — contractor vs. organic.** *Claim:* the Navy is acquiring BDAR/BDAT training-and-simulation capability through contractor solutions, not solely through organic Navy work. *What kills it:* BDAR/BDAT training is exclusively organic Navy work — performed by Sailors at SIMAs, NWDC personnel, fleet schoolhouse instructors, and other government-uniformed workforce — with no contractor procurement signal in NAVSEA, ONR, NWDC, or DoD-wide acquisition data. This leg replaces the earlier "industrial-planning gap" leg, which addressed the broader ship-repair industrial base and is now out of scope per the 2026-05-24 narrowing.

3. **Modeling-fidelity availability — Carderock's unclassified subset.** *Claim:* NSWC Carderock's damage-modeling work has a useful unclassified subset that can be transformed into BDAR/BDAT training scenarios at operationally-meaningful fidelity. *What kills it:* the unclassified version is doctrinal or coarse-grained only, and the operationally-useful modeling lives behind a classification gradient this research cannot reach. If that is true, the deliverable changes shape entirely, from "build an unclassified BDAR/BDAT scenario product" to "engage Navy customers about a classified collaboration."

4. **BDAR repair-side training-progression viability.** *Claim:* the tabletop → guided site visit → hands-on instrumented-test-bed progression is a feasible program design for repair-side training that does not already exist end-to-end. *What kills it:* (a) some existing Navy program already runs this exact progression (most likely candidates: NWDC product, SIMA curriculum, or a Naval Postgraduate School program), in which case the play is helping execute or scale that program rather than designing a new one; or (b) the legal and operational hurdles of moving cohorts from unclassified content up to classified instrumented test-bed work are prohibitive. *Scope note:* this is the BDAR repair-side pipeline that lives in section 11.2; the BDAT assessment-side pipeline is leg 6.

5. **Relationship feasibility — CACI can be positioned at the right Navy organizations.** *Claim:* CACI can realistically build or expand the relationships needed to execute a BDAR/BDAT capability bid, on a timeline shorter than the customer demand window. *What kills it:* the relevant Navy customer organizations (NSWC Carderock for the modeling input; NAVSEA and the SRF/RMC system for the consuming customer; NWDC or fleet schoolhouses for the curriculum and doctrine owner) have their engagement bandwidth locked up by canonical naval-services incumbents to a degree that CACI's entry timeline runs past the demand window. **Refined 2026-05-25 from corpus-cleanup dialogue:** among the three names previously listed here together — SAIC, Leidos, and HII Mission Technologies — HII Mission Technologies is specifically the most plausible incumbent for the BDAR/BDAT training-systems space because of the dialogue-surfaced (but not yet vault-source-grounded) claim that HII Mission Technologies is the network-architecture prime on the Navy Continuous Training Environment. The next find_sources pass will test that claim against primary sources before it is treated as FACT. SAIC and Leidos remain canonical naval-services incumbents at the broader level; their specific BDAR/BDAT-relevant contract footprints are not yet source-grounded for this research track and are open research. If true that one or more of these incumbents dominate the customer-organization engagement bandwidth in BDAR/BDAT training, this is a partnering decision, not a prime-position decision. *Note:* per the section 9.3 contact-protection discipline and the OCI primer at `_meta/oci-primer.md`, the operator's working-level knowledge about CACI's current contract footprint at any Navy organization is operator-side context and does not enter this leg's falsifier reasoning. The leg is framed at the general competitive level.

6. **BDAT training-pipeline viability.** *Claim:* the proposed two-phase pipeline for BDATs — gamified simulation as a high-frequency repetition layer, then real-world exercise injects in fleet training events — is a feasible program model that is not already saturated. *What kills it:* any one of three things — (a) the Department of Defense has already funded a BDAT serious-game or instrumented-sim product mature enough that the play would be a me-too entry rather than a new pipeline (evidence for this lives in SBIR Phase II and Phase III award databases, the NWDC product catalog, and DIU active-portfolio listings); (b) BDAT training is already deeply embedded in fleet exercises like COMPTUEX, RIMPAC, and Large-Scale Exercise at a depth that leaves no gap for a contractor-provided pipeline to fill; or (c) the simulation layer cannot achieve operationally-meaningful realism at unclassified level, which is the same classification-gradient problem as leg 3 but applied specifically to simulation content rather than to source modeling.

**Recommendation (draft):** to be determined — pending source ingestion, the disconfirming-evidence checks above, and the engagement-surface inventory in section 11.

<!-- /sensitivity -->

## 8. Source ledger

Citations in this file use the format `[s.YYYY-MM-DD-slug]` where the date is the capture date and the slug is derived from the source title. Each entry resolves to a file in `01_sources/`. Sources are added to §8.1 when ingested successfully with usable content; failed fetches and empty-ingest cases land in §8.2 for retry or manual download.

### 8.1 Ingested primary sources (in `01_sources/`)

Substantive content captured 2026-05-23 from the first source-finder pass:

- [s.2026-05-23-swarmex-srf-jrmc] https://www.navsea.navy.mil/Home/RMC/SRF-JRMC/STORY/  →  `01_sources/2026-05-23_navsea-navy-mil_ship-wartime-repair-and-maintenance-exercise-swarm-ex-in-japan.md` (SRF-JRMC press release — first Japan SWARMEX on USS FITZGERALD; manually pasted by operator after original Article 3748283 URL returned 404)
- [s.2026-05-23-navy-shipbuilding-plan-2026] https://media.defense.gov/2026/May/11/2003928909/-1/-1/1/NAVY%20SHIPBUILDING%20PLAN%20MAY%202026.PDF  →  `01_sources/2026-05-23_navy-mil_navy-shipbuilding-plan-may-2026.md` (Navy May 2026 Shipbuilding Plan — Acting SECNAV / CNO / CMC signatures; 60-page PDF binary also in `01_sources/2026-05-23_navy-mil_navy-shipbuilding-plan-may-2026.pdf`; manually downloaded by operator after both candidate URLs 404'd from the war.gov migration)
- [s.2026-05-23-gao-26-109068-navy-and-coast-g] https://www.gao.gov/assets/gao-26-109068.pdf  →  `01_sources/2026-05-23_gao-gov_gao-26-109068-navy-and-coast-guard-shipbuilding-a-discipline.md` (GAO testimony, 22 Apr 2026 — Navy and Coast Guard Shipbuilding)
- [s.2026-05-23-gao-26-108140-weapon-system-su] https://www.gao.gov/assets/gao-26-108140.pdf  →  `01_sources/2026-05-23_gao-gov_gao-26-108140-weapon-system-sustainment-dod-identified-criti.md` (GAO report, Apr 2026 — Weapon System Sustainment)
- [s.2026-05-23-the-time-is-ripe-for-next-step] https://www.stimson.org/2026/the-time-is-ripe-for-next-steps-on-us-japan-military-shipbuilding-cooperation/  →  `01_sources/2026-05-23_stimson-org_the-time-is-ripe-for-next-steps-on-us-japan-military-shipbui.md` (Stimson Center, 23 Apr 2026 — US-Japan MSMRO Task Force)
- [s.2026-05-23-is-the-united-states-prepared-] https://www.csis.org/analysis/united-states-prepared-war-china  →  `01_sources/2026-05-23_csis-org_is-the-united-states-prepared-for-a-war-with-china.md` (CSIS analysis — Is the United States Prepared for War with China)
- [s.2026-05-23-dvids-news-integrated-training] https://www.dvidshub.net/news/565496/integrated-training-expeditionary-strike-group-2-completes-dynamic-exercise  →  `01_sources/2026-05-23_dvidshub-net_dvids-news-integrated-training-expeditionary-strike-group-2.md` (DVIDS, May 2026 — Expeditionary Strike Group 2 dynamic exercise)
- [s.2026-05-23-port-infrastructure-developmen] https://www.maritime.dot.gov/PIDPgrants  →  `01_sources/2026-05-23_maritime-dot-gov_port-infrastructure-development-program.md` (Maritime Administration — Port Infrastructure Development Program)
- [s.2026-05-23-don26tz01-sttr-release-1-sensi] https://www.navysbir.com/n26_1s/DON26TZ01-NV012.htm  →  `01_sources/2026-05-23_navysbir-com_don26tz01-sttr-release-1-sensing-to-measure-and-validate-cor.md` (Navy SBIR/STTR topic DON26TZ01 — Sensing for Corrosion in Naval Systems)
- [s.2026-05-23-advanced-materials-nta-org] https://nta.org/advanced-materials/  →  `01_sources/2026-05-23_nta-org_advanced-materials-nta-org.md` (NTA — Advanced Materials)
- [s.2026-05-23-shortfalls-in-u-s-naval-shipbu] https://rmcglobal.com/shortfalls-in-u-s-naval-shipbuilding-capability/  →  `01_sources/2026-05-23_rmcglobal-com_shortfalls-in-u-s-naval-shipbuilding-capability-rmc.md` (RMC Global private analysis — Shortfalls in US Naval Shipbuilding Capability; tier 4, click-verify before any FACT use)
- [s.2026-05-23-u-s-navy-logistics-pacific-rep] https://list25.com/us-navy-logistics-pacific-sustainment/  →  `01_sources/2026-05-23_list25-com_u-s-navy-logistics-pacific-repair-forward-sustainment.md` (list25 — US Navy Pacific Repair / Forward Sustainment; tier 4, click-verify before any FACT use)
- [s.2026-05-23-10-commercial-angles-hidden-in] https://www.shipuniverse.com/naval/10-commercial-angles-hidden-inside-naval-maintenance-backlogs-and-depot-capacity-strain/  →  `01_sources/2026-05-23_shipuniverse-com_10-commercial-angles-hidden-inside-naval-maintenance-backlog.md` (ShipUniverse — 10 Commercial Angles in Naval Maintenance Backlogs; tier 4, click-verify before any FACT use)

### 8.2 Cited but not yet ingested, or ingested empty — needs retry or manual download

The first ingest pass left these in incomplete state. They are listed here so future research that wants to cite them does so with the awareness that the public source has not been captured in the vault.

**Genuine 404 at the server (URL is dead or relocated):**

- ~~The SRF-JRMC SWARMEX article previously at `https://www.navsea.navy.mil/Media/News/Article/3748283/...`~~ — **RECOVERED 2026-05-23.** Operator manually located the article at the SRF-JRMC story index page and pasted the body text. Now ingested as `[s.2026-05-23-swarmex-srf-jrmc]` — see §8.1.
- ~~The defense.gov PDF of the Navy Shipbuilding Plan May 2026~~ — **RECOVERED 2026-05-23.** Operator manually downloaded the 9.4 MB PDF and uploaded it. Now ingested as `[s.2026-05-23-navy-shipbuilding-plan-2026]` with the binary stored in `01_sources/2026-05-23_navy-mil_navy-shipbuilding-plan-may-2026.pdf` — see §8.1.
- Two NSWC / NAVSEA Public Affairs article URLs are still returning 404 (article IDs 3774844 Vertical Launching System tool, 3750059 Carderock Orion Recovery). The SWARMEX 404 plus these two suggests a site-pattern change parallel to the defense.gov → war.gov migration. Recovery via the SRF-JRMC story index pattern is possible but lower-priority than the SWARMEX article was.

**Bot-detection 403 (manual download required):**

- One GovConWire article surfaced by the source-finder returned HTTP 403 from Cloudflare for both `curl_cffi` browser-TLS impersonation and the Playwright headless-Chromium fallback. The script's bot-detection fallback layer is in place but does not defeat Cloudflare's most aggressive tier. The article was reviewed by the operator on 2026-05-24 and judged not applicable to the BDAR/BDAT scope; the inbox entry has been rejected. Manual save from a logged-in browser session remains the recovery path for any future Cloudflare-protected article that IS in scope.

**Ingest succeeded but content was empty / wrong / 404-as-200:**

- `01_sources/2026-05-23_defense-gov_us-navys-shipbuilding-plan-for-2025-2026.md` — the defense.gov transcript URL served a 200 HTML response whose body is the site's "page not found" message. Content is unusable as a citation; file is essentially a 404-rendered-as-200.
- `01_sources/2026-05-23_marines-mil_content-not-found.md` — same problem; the filename literally captures the page's error string. The Marine Corps Order 4700.4A on Advanced Manufacturing Policy is the target source and needs a working URL.
- `01_sources/2026-05-23_researchgate-net_a-fourier-spectral-immersed-boundary-method-with-exact-trans.md` — the source-ranker pointed at a ResearchGate URL whose page actually loads an unrelated paper on Fourier spectral methods rather than the virtual-reality naval-engagement paper the inbox entry referenced. The ResearchGate URL ID does not match the title of the inbox entry; the original inbox record may have had a mismatched URL.

All three empty-ingest files should be moved to `01_sources/_quarantine/` and the correct sources re-found in the next source-finder pass.
- [s.2026-05-23-2026-05-14-caudle-testimony] https://armedservices.house.gov/uploadedfiles/2026-05-14_caudle_testimony.pdf  →  `01_sources/2026-05-23_armedservices-house-gov_2026-05-14-caudle-testimony.md`
- [s.2026-05-23-error-aspx] https://docs.house.gov/committee/Error/Error.aspx?Code=404  →  `01_sources/2026-05-23_docs-house-gov_error-aspx.md`
- [s.2026-05-24-arcs-aviation-awarded-sbir-pha] https://www.arcsaviation.com/07/arcs-aviation-awarded-sbir-phase-ii-by-u-s-navy/  →  `01_sources/2026-05-24_arcsaviation-com_arcs-aviation-awarded-sbir-phase-ii-by-u-s-navy.md`
- [s.2026-05-24-calendar] https://armedservices.house.gov/calendar/  →  `01_sources/2026-05-24_armedservices-house-gov_calendar.md`
- [s.2026-05-24-2026-05-14-caudle-testimony] https://armedservices.house.gov/uploadedfiles/2026-05-14_caudle_testimony.pdf  →  `01_sources/2026-05-24_armedservices-house-gov_2026-05-14-caudle-testimony.md`
- [s.2026-05-24-department-of-the-navy-release] https://www.navy.mil/Press-Office/News-Stories/Article/3769970/department-of-the-navy-releases-fiscal-year-2027-shipbuilding-plan/  →  `01_sources/2026-05-24_navy-mil_department-of-the-navy-releases-fiscal-year-2027-shipbuildin.md`
- [s.2026-05-24-budget-hearing-united-states-n] https://appropriations.house.gov/events/hearings/budget-hearing-united-states-navy-and-marine-corps  →  `01_sources/2026-05-24_appropriations-house-gov_budget-hearing-united-states-navy-and-marine-corps.md`
- [s.2026-05-24-weapon-system-sustainment-dod-] https://www.gao.gov/products/gao-26-108140  →  `01_sources/2026-05-24_gao-gov_weapon-system-sustainment-dod-identified-critical-cost-growt.md`
- [s.2026-05-24-weekly-update-for-government-c] https://www.pmpc.com/news-events/weekly-update-for-government-contractors-and-commercial-businesses-april-2026-5/  →  `01_sources/2026-05-24_pmpc-com_weekly-update-for-government-contractors-and-commercial-busi.md`
- [s.2026-05-24-u-s-senator-elizabeth-warren] https://www.warren.senate.gov/newsroom/press-releases/warren-sheehy-push-armed-services-leaders-in-congress-to-get-military-right-to-repair-done  →  `01_sources/2026-05-24_warren-senate-gov_u-s-senator-elizabeth-warren.md`
- [s.2026-05-24-u-s-pacific-fleet-announces-30] https://www.cpf.navy.mil/Newsroom/News/Article/4465055/us-pacific-fleet-announces-30th-rimpac-exercise/  →  `01_sources/2026-05-24_cpf-navy-mil_u-s-pacific-fleet-announces-30th-rimpac-exercise.md`
- [s.2026-05-24-private-sector-services-that-c] https://www.shipuniverse.com/naval/private-sector-services-that-could-become-critical-as-naval-maintenance-backlogs-deepen/  →  `01_sources/2026-05-24_shipuniverse-com_private-sector-services-that-could-become-critical-as-naval.md`
- [s.2026-05-24-why-the-united-states-south-ko] https://www.rand.org/pubs/commentary/2025/05/why-the-united-states-south-korea-and-japan-must-cooperate.html  →  `01_sources/2026-05-24_rand-org_why-the-united-states-south-korea-and-japan-must-cooperate-o.md`
- [s.2026-05-24-identifying-pathways-for-u-s-s] https://www.csis.org/analysis/identifying-pathways-us-shipbuilding-cooperation-northeast-asian-allies  →  `01_sources/2026-05-24_csis-org_identifying-pathways-for-u-s-shipbuilding-cooperation-with-n.md`
- [s.2026-05-24-artificial-intelligence-and-ma] https://spie.org/DS/conferencedetails/artificial-intelligence-and-machine-learning-for-mdo-applications  →  `01_sources/2026-05-24_spie-org_artificial-intelligence-and-machine-learning-for-multi-domai.md`
- [s.2026-05-24-afdp-3-60-targeting-air-force-] https://www.doctrine.af.mil/Portals/61/documents/AFDP_3-60/3-60-AFDP-TARGETING.pdf  →  `01_sources/2026-05-24_doctrine-af-mil_afdp-3-60-targeting-air-force-doctrine-publication.md`
- [s.2026-05-24-opening-the-training-bottlenec] https://www.diu.mil/latest/opening-the-training-bottleneck-how-dius-xr-devices-deliver-increased-access-and-readiness  →  `01_sources/2026-05-24_diu-mil_opening-the-training-bottleneck-how-diu-s-xr-devices-deliver.md`
- [s.2026-05-24-chairman-wicker-leads-sasc-hea] https://www.wicker.senate.gov/2026/5/chairman-wicker-leads-sasc-hearing-on-department-of-the-navy-posture-for-fiscal-year-2027  →  `01_sources/2026-05-24_wicker-senate-gov_chairman-wicker-leads-sasc-hearing-on-department-of-the-navy.md`
- [s.2026-05-24-c3f-and-international-partners] https://www.c3f.navy.mil/News/Article/4461121/c3f-and-international-partners-conclude-final-planning-for-rimpac-2026-exercise/  →  `01_sources/2026-05-24_c3f-navy-mil_c3f-and-international-partners-conclude-final-planning-for-r.md`
- [s.2026-05-24-nswc-crane-to-receive-two-nati] https://www.navsea.navy.mil/Media/News/Article/4187898/nswc-crane-to-receive-two-nationwide-federal-laboratory-consortium-awards-for-s/  →  `01_sources/2026-05-24_navsea-navy-mil_nswc-crane-to-receive-two-nationwide-federal-laboratory-cons.md`
- [s.2026-05-24-damage-control-training-invent] https://www.ziprecruiter.com/c/Phoenix-Group-of-Virgina,-Inc./Job/Damage-Control-Training-&-Inventory-Control/-in-Chesapeake,VA?jid=88cf337c16cea358  →  `01_sources/2026-05-24_ziprecruiter-com_damage-control-training-inventory-control-job-in-chesapeake.md`
- [s.2026-05-24-transitions-spring-2026] https://www.navysbir.com/docs/Transitions_Spring-2026.pdf  →  `01_sources/2026-05-24_navysbir-com_transitions-spring-2026.md`
- [s.2026-05-24-pressure-points-training-cic-c] https://euro-sd.com/2026/04/allgemein/50613/pressure-points-training-cic-crews/  →  `01_sources/2026-05-24_euro-sd-com_pressure-points-training-cic-crews-european-security-defence.md`
- [s.2026-05-24-a-new-strategy-for-high-perfor] https://www.navsea.navy.mil/Media/News/Article-View/Article/4196134/a-new-strategy-for-high-performance-computing-at-carderock/  →  `01_sources/2026-05-24_navsea-navy-mil_a-new-strategy-for-high-performance-computing-at-carderock-n.md`
- [s.2026-05-24-northrop-grumman-uses-ar-and-v] https://defence-industry.eu/northrop-grumman-uses-augmented-and-virtual-reality-tools-to-improve-e-2d-advanced-hawkeye-readiness/  →  `01_sources/2026-05-24_defence-industry-eu_northrop-grumman-uses-ar-and-vr-tools-to-improve-e-2d-advanc.md`
- [s.2026-05-26-don-fy27-press-brief] https://www.secnav.navy.mil/fmc/fmb/Documents/27pres/DON_Press_Brief.pdf  →  `01_sources/2026-05-26_secnav-navy-mil_don-fy27-press-brief.md`
- [s.2026-05-26-naval-sea-systems-command] https://www.navsea.navy.mil/Home/Warfare-Centers/NSWC-Carderock/Business/Technology-Transfer-Office/  →  `01_sources/2026-05-26_navsea-navy-mil_naval-sea-systems-command.md`
- [s.2026-05-26-356605] https://www.grants.gov/search-results-detail/356605  →  `01_sources/2026-05-26_grants-gov_356605.md`
- [s.2026-05-26-dvids-news-dont-give-up-the-sh] https://www.dvidshub.net/news/563966/dont-give-up-ship-iwo-jimas-damage-controlmen-prepare-crew-engage-casualties  →  `01_sources/2026-05-26_dvidshub-net_dvids-news-dont-give-up-the-ship-how-iwo-jimas-damage-contro.md`
- [s.2026-05-26-2022-20alnavresfor-20020-20nav] https://www.navyreserve.navy.mil/Portals/35/2022%20ALNAVRESFOR%20020%20NAVY%20RESERVE%20FIGHTING%20INSTRUCTIONS.pdf  →  `01_sources/2026-05-26_navyreserve-navy-mil_2022-20alnavresfor-20020-20navy-20reserve-20fighting-20instr.md`
- [s.2026-05-26-united-states-navy] https://www.navy.mil/Press-Office/News-Stories/Term/3087/  →  `01_sources/2026-05-26_navy-mil_united-states-navy.md`
- [s.2026-05-26-uss-ashland-completes-ship-war] https://www.navy.mil/Press-Office/News-Stories/display-news/Article/4452022/uss-ashland-completes-ship-wartime-repair-and-maintenance-in-the-philippines/  →  `01_sources/2026-05-26_navy-mil_uss-ashland-completes-ship-wartime-repair-and-maintenance-ex.md`
- [s.2026-05-26-uss-ashland-completes-ship-war] https://www.c7f.navy.mil/Media/News/Display/Article/4451961/uss-ashland-completes-ship-wartime-repair-and-maintenance-in-the-philippines/  →  `01_sources/2026-05-26_c7f-navy-mil_uss-ashland-completes-ship-wartime-repair-and-maintenance-ex.md`
- [s.2026-05-26-uss-ashland-completes-ship-war] https://www.pacom.mil/Media/News/News-Articles/Article/4452848/uss-ashland-completes-ship-wartime-repair-and-maintenance-in-the-philippines/  →  `01_sources/2026-05-26_pacom-mil_uss-ashland-completes-ship-wartime-repair-and-maintenance-in.md`
- [s.2026-05-26-u-s-navy-rehearses-wartime-rep] https://www.navalnews.com/naval-news/2026/04/u-s-navy-rehearses-wartime-repairs-in-central-philippine-port/  →  `01_sources/2026-05-26_navalnews-com_u-s-navy-rehearses-wartime-repairs-in-central-philippine-por.md`
- [s.2026-05-26-uss-ashland-completes-ship-war] https://www.cpf.navy.mil/Newsroom/News/Article/4452493/uss-ashland-completes-ship-wartime-repair-and-maintenance-in-philippines/  →  `01_sources/2026-05-26_cpf-navy-mil_uss-ashland-completes-ship-wartime-repair-and-maintenance-ex.md`
- [s.2026-05-26-cno-remarks-at-modern-day-mari] https://www.navy.mil/Press-Office/Speeches-Remarks/display-speeches/Article/3757304/cno-remarks-at-modern-day-marine-as-prepared/  →  `01_sources/2026-05-26_navy-mil_cno-remarks-at-modern-day-marine-as-prepared.md`
- [s.2026-05-26-siop-brief-psns-sbs-2025-1] https://pacific.navfac.navy.mil/Portals/72/Northwest/Documents/SIOP-Brief-PSNS-SBS-2025-1.pdf  →  `01_sources/2026-05-26_pacific-navfac-navy-mil_siop-brief-psns-sbs-2025-1.md`
- [s.2026-05-26-navy-marine-corps-back-longer-] https://breakingdefense.com/2026/05/navy-marine-corps-back-longer-amphib-readiness-cycles-request-more-ships/  →  `01_sources/2026-05-26_breakingdefense-com_navy-marine-corps-back-longer-amphib-readiness-cycles-reques.md`
- [s.2026-05-26-dvids-news-navfac-atlantic-awa] https://www.dvidshub.net/news/566002/navfac-atlantic-awards-512-million-crane-modification-portsmouth-naval-shipyard  →  `01_sources/2026-05-26_dvidshub-net_dvids-news-navfac-atlantic-awards-51-2-million-crane-modific.md`
- [s.2026-05-26-sea-air-space-news-next-gen-ba] https://www.nationaldefensemagazine.org/articles/2026/4/22/nextgen-battleship-a-golden-fleet-necessity-phelan-says  →  `01_sources/2026-05-26_nationaldefensemagazine-org_sea-air-space-news-next-gen-battleship-a-golden-fleet-necess.md`
- [s.2026-05-26-military-readiness-dod-should-] https://www.gao.gov/products/gao-26-108888  →  `01_sources/2026-05-26_gao-gov_military-readiness-dod-should-take-further-actions-to-addres.md`
- [s.2026-05-26-lvc-training-for-navy-fleet-re] https://militaryembedded.com/cyber/cybersecurity/lvc-training-for-navy-fleet-readiness-contract-signed-with-saic  →  `01_sources/2026-05-26_militaryembedded-com_lvc-training-for-navy-fleet-readiness-contract-signed-with-s.md`
- [s.2026-05-26-marine-log-s-ship-repair-usa-2] https://www.marinelog.com/shiprepairusa2026/  →  `01_sources/2026-05-26_marinelog-com_marine-log-s-ship-repair-usa-2026-marine-log.md`
- [s.2026-05-26-us-navy-awards-183-million-con] https://www.armyrecognition.com/news/navy-news/2026/us-navy-awards-183-million-contract-to-repair-uss-truxtun-destroyer-after-collision-in-the-caribbean  →  `01_sources/2026-05-26_armyrecognition-com_us-navy-awards-183-million-contract-to-repair-uss-truxtun-de.md`
- [s.2026-05-26-if-the-u-s-navy-cant-repair-sh] https://cimsec.org/if-the-u-s-navy-cant-repair-ships-in-peacetime-how-will-it-do-so-in-war/  →  `01_sources/2026-05-26_cimsec-org_if-the-u-s-navy-cant-repair-ships-in-peacetime-how-will-it-d.md`
- [s.2026-05-26-us-navy-amphibious-ship-practi] https://www.navaltoday.com/2026/04/07/us-navy-amphibious-ship-practices-wartime-repairs-in-philippines/  →  `01_sources/2026-05-26_navaltoday-com_us-navy-amphibious-ship-practices-wartime-repairs-in-philipp.md`
- [s.2026-05-26-the-diplomat-asia-pacific-curr] https://thediplomat.com/  →  `01_sources/2026-05-26_thediplomat-com_the-diplomat-asia-pacific-current-affairs-magazine.md`
- [s.2026-05-26-navy-issues-contracts-for-carr] https://www.workboat.com/navy-issues-contracts-for-carrier-maintenance-yrbms-and-portsmouth-repairs  →  `01_sources/2026-05-26_workboat-com_navy-issues-contracts-for-carrier-maintenance-yrbms-and-port.md`
- [s.2026-05-26-contract-briefs-aerotech-news-] https://www.aerotechnews.com/blog/2026/05/18/contract-briefs-736/  →  `01_sources/2026-05-26_aerotechnews-com_contract-briefs-aerotech-news-review.md`
- [s.2026-05-26-fix-the-navys-expeditionary-re] https://www.usni.org/magazines/proceedings/2025/march/fix-navys-expeditionary-repair  →  `01_sources/2026-05-26_usni-org_fix-the-navys-expeditionary-repair.md`
- [s.2026-05-26-full-committee-hearing-departm] https://democrats-armedservices.house.gov/2026/5/full-committee-hearing-department-of-the-navy-fy27-budget-request  →  `01_sources/2026-05-26_democrats-armedservices-house-gov_full-committee-hearing-department-of-the-navy-fy27-budget-re.md`
- [s.2026-05-26-industrial-rebuild-betting-on-] https://thefinancialpen.substack.com/p/industrial-rebuild-betting-on-scarce  →  `01_sources/2026-05-26_thefinancialpen-substack-com_industrial-rebuild-betting-on-scarce-aerospace-and-defence-c.md`
- [s.2026-05-26-us-navy-unveils-30-year-golden] https://thedefensepost.com/2026/05/13/us-golden-fleet-plan/  →  `01_sources/2026-05-26_thedefensepost-com_us-navy-unveils-30-year-golden-fleet-modernization-plan-to-r.md`
- [s.2026-05-26-department-of-the-navy-s-may-2] https://natlawreview.com/article/navy-shipbuilding-plan-signals-industrial-shift  →  `01_sources/2026-05-26_natlawreview-com_department-of-the-navy-s-may-2026-shipbuilding-plan.md`
- [s.2026-05-26-to-build-the-golden-fleet] https://www.heritage.org/defense/report/build-the-golden-fleet  →  `01_sources/2026-05-26_heritage-org_to-build-the-golden-fleet.md`
- [s.2026-05-26-hearings] https://appropriations.house.gov/schedule/hearings  →  `01_sources/2026-05-26_appropriations-house-gov_hearings.md`
- [s.2026-05-26-norfolk-naval-shipyard-begins-] https://www.workboat.com/norfolk-naval-shipyard-begins-442-million-drydock-modernization  →  `01_sources/2026-05-26_workboat-com_norfolk-naval-shipyard-begins-442-million-drydock-modernizat.md`
- [s.2026-05-26-graphics-analyst-sea04-washing] https://www.clearancejobs.com/jobs/8923075/graphics-analyst-sea04-washington-dc  →  `01_sources/2026-05-26_clearancejobs-com_graphics-analyst-sea04-washington-d-c-jobs-clearancejobs.md`
- [s.2026-05-26-odysight-ai-r-signs-crada-with] https://www.odysight.ai/press/odysight-ai-signs-crada-with-u-s-navy-to-advance-ai-driven-visual-sensing-supporting-condition-based-maintenance-operations/  →  `01_sources/2026-05-26_odysight-ai_odysight-ai-r-signs-crada-with-u-s-navy-to-advance-ai-driven.md`
- [s.2026-05-26-navy-marine-corps-weighing-for] https://breakingdefense.com/2026/04/navy-marine-corps-weighing-force-generation-model-revamp-for-amphibs/  →  `01_sources/2026-05-26_breakingdefense-com_navy-marine-corps-weighing-force-generation-model-revamp-for.md`
- [s.2026-05-26-the-us-navys-next-supercarrier] https://www.forbes.com/sites/petersuciu/2026/05/08/the-us-navys-next-supercarriers-face-lengthy-delays/  →  `01_sources/2026-05-26_forbes-com_the-us-navys-next-supercarriers-face-lengthy-delays.md`
- [s.2026-05-26-virginia-tajikistan-state-part] https://www.navy.mil/Press-Office/News-Stories/Article/3773173/warfare-center-develops-new-tool-to-help-sailors-keep-vertical-launching-system-latch-rods-moving/  →  `01_sources/2026-05-26_navy-mil_virginia-tajikistan-state-partnership-reaches-out-to-childre.md`
- [s.2026-05-26-us-navy-returns-uss-ralph-john] https://www.armyrecognition.com/news/navy-news/2026/us-navy-returns-uss-ralph-johnson-arleigh-burke-class-destroyer-to-indo-pacific-duty-after-major-overhaul  →  `01_sources/2026-05-26_armyrecognition-com_us-navy-returns-uss-ralph-johnson-arleigh-burke-class-destro.md`
- [s.2026-05-26-251103-n-n2246-1001] https://www.navsea.navy.mil/Home/RMC/SERMC/IT/igphoto/2003932652/  →  `01_sources/2026-05-26_navsea-navy-mil_251103-n-n2246-1001.md`
- [s.2026-05-26-us-navy-awards-183m-contract-f] https://thedefensewatch.com/naval-maritime/us-navy-awards-183m-contract-for-uss-truxtun-repair-after-collision/  →  `01_sources/2026-05-26_thedefensewatch-com_us-navy-awards-183m-contract-for-uss-truxtun-repair-after-co.md`
- [s.2026-05-26-navy-pushes-congress-to-back-c] https://breakingdefense.com/2026/05/navy-pushes-congress-to-back-constructing-auxiliary-ships-overseas/  →  `01_sources/2026-05-26_breakingdefense-com_navy-pushes-congress-to-back-constructing-auxiliary-ships-ov.md`
- [s.2026-05-26-us-navy-open-to-building-ships] https://www.navytimes.com/news/your-navy/2026/05/12/us-navy-open-to-building-ships-overseas-new-plan-says/  →  `01_sources/2026-05-26_navytimes-com_us-navy-open-to-building-ships-overseas-new-plan-says.md`
- [s.2026-05-26-revisiting-the-relationship-be] https://www.csis.org/analysis/revisiting-relationship-between-economic-and-sea-power  →  `01_sources/2026-05-26_csis-org_revisiting-the-relationship-between-economic-and-sea-power.md`
- [s.2026-05-26-a-first-look-at-the-navy-s-new] https://defensescoop.com/2025/05/22/navy-plan-consolidate-legacy-it-networks-cio-jane-rathbun/  →  `01_sources/2026-05-26_defensescoop-com_a-first-look-at-the-navy-s-new-plan-to-drastically-consolida.md`
- [s.2026-05-26-how-the-navy-is-removing-barri] https://federalnewsnetwork.com/ask-the-cio/2025/03/how-the-navy-is-removing-barriers-to-it-modernization/  →  `01_sources/2026-05-26_federalnewsnetwork-com_how-the-navy-is-removing-barriers-to-it-modernization.md`
- [s.2026-05-26-enterprise-services-help-navy-] https://federalnewsnetwork.com/navy/2025/04/enterprise-services-help-navy-increase-value-per-user/  →  `01_sources/2026-05-26_federalnewsnetwork-com_enterprise-services-help-navy-increase-value-per-user.md`
- [s.2026-05-26-technical-interoperability-in-] https://cimsec.org/technical-interoperability-in-contested-environments-is-a-must/  →  `01_sources/2026-05-26_cimsec-org_technical-interoperability-in-contested-environments-is-a-mu.md`
- [s.2026-05-26-10-reasons-technical-data-and-] https://www.shipuniverse.com/naval/10-reasons-technical-data-and-lifecycle-support-are-getting-harder-to-ignore-in-naval-programs/  →  `01_sources/2026-05-26_shipuniverse-com_10-reasons-technical-data-and-lifecycle-support-are-getting.md`
- [s.2026-05-26-justification-book] https://comptroller.war.gov/Portals/45/Documents/defbudget/FY2027/budget_justification/pdfs/03_RDT_and_E/RDTE_TJS_PB_2027.pdf  →  `01_sources/2026-05-26_comptroller-war-gov_justification-book.md`
- [s.2026-05-26-defense-ped-processing-exploit] https://www.defenseadvancement.com/suppliers/processing-exploitation-and-dissemination/  →  `01_sources/2026-05-26_defenseadvancement-com_defense-ped-processing-exploitation-dissemination-technology.md`
- [s.2026-05-26-dvids-video-navy-department-le] https://www.dvidshub.net/video/1006895/navy-department-leaders-testify-house-fy27-budget-request-part-1  →  `01_sources/2026-05-26_dvidshub-net_dvids-video-navy-department-leaders-testify-to-house-on-fy27.md`
- [s.2026-05-26-citi-subcommittee-hearing-scie] https://armedservices.house.gov/calendar/eventsingle.aspx?EventID=6466  →  `01_sources/2026-05-26_armedservices-house-gov_citi-subcommittee-hearing-science-technology-and-innovation.md`
- [s.2026-05-26-volume-1-issue-5-full-issue-st] https://digital-commons.usnwc.edu/cmsi-quarterly-review/vol1/iss5/1/  →  `01_sources/2026-05-26_digital-commons-usnwc-edu_volume-1-issue-5-full-issue-strategic-projection-and-operati.md`
- [s.2026-05-26-a-u-s-navy-nuclear-attack-subm] https://nationalsecurityjournal.org/a-u-s-navy-nuclear-attack-submarine-hit-an-underwater-mountain-head-on-at-flank-speed-and-the-pressure-hull-held/  →  `01_sources/2026-05-26_nationalsecurityjournal-org_a-u-s-navy-nuclear-attack-submarine-hit-an-underwater-mounta.md`
- [s.2026-05-26-doge-reviewing-navy-software-e] https://defensescoop.com/2025/04/08/doge-reviewing-navy-software-enterprise/  →  `01_sources/2026-05-26_defensescoop-com_doge-reviewing-navy-software-enterprise.md`
- [s.2026-05-26-9-naval-supplier-niches-growin] https://www.shipuniverse.com/naval/9-naval-supplier-niches-growing-as-shipyards-struggle-to-add-throughput/  →  `01_sources/2026-05-26_shipuniverse-com_9-naval-supplier-niches-growing-as-shipyards-struggle-to-add.md`
- [s.2026-05-26-cont-awd-n0016424f3006-9700-n0] https://www.usaspending.gov/award/CONT_AWD_N0016424F3006_9700_N0017819D7883_9700/  →  `01_sources/2026-05-26_usaspending-gov_cont-awd-n0016424f3006-9700-n0017819d7883-9700.md`
- [s.2026-05-26-cont-awd-47qfca21f0042-4732-gs] https://www.usaspending.gov/award/CONT_AWD_47QFCA21F0042_4732_GS00Q14OADU127_4732/  →  `01_sources/2026-05-26_usaspending-gov_cont-awd-47qfca21f0042-4732-gs00q14oadu127-4732.md`
- [s.2026-05-26-cont-awd-hq014716c0034-9700-no] https://www.usaspending.gov/award/CONT_AWD_HQ014716C0034_9700_-NONE-_-NONE-/  →  `01_sources/2026-05-26_usaspending-gov_cont-awd-hq014716c0034-9700-none-none.md`
- [s.2026-05-26-cont-awd-47qfca20f0002-4732-gs] https://www.usaspending.gov/award/CONT_AWD_47QFCA20F0002_4732_GS00Q14OADU121_4732/  →  `01_sources/2026-05-26_usaspending-gov_cont-awd-47qfca20f0002-4732-gs00q14oadu121-4732.md`
- [s.2026-05-26-2026-05-14-caudle-testimony] https://armedservices.house.gov/uploadedfiles/2026-05-14_caudle_testimony.pdf  →  `01_sources/2026-05-26_armedservices-house-gov_2026-05-14-caudle-testimony.md`
- [s.2026-05-26-the-purpose-of-this-award-is-t] https://www.usaspending.gov/award/CONT_AWD_47QFCA20F0002_4732_GS00Q14OADU121_4732/  →  `01_sources/2026-05-26_usaspending-gov_the-purpose-of-this-award-is-to-provide-plans-operations-log.md`
- [s.2026-05-26-the-purpose-of-this-award-is-f] https://www.usaspending.gov/award/CONT_AWD_47QFCA21F0042_4732_GS00Q14OADU127_4732/  →  `01_sources/2026-05-26_usaspending-gov_the-purpose-of-this-award-is-for-the-c5isr-exercises-operati.md`
- [s.2026-05-26-test-exercise-and-wargames-sup] https://www.usaspending.gov/award/CONT_AWD_HQ014716C0034_9700_-NONE-_-NONE-/  →  `01_sources/2026-05-26_usaspending-gov_test-exercise-and-wargames-support-igf-ot-igf.md`
- [s.2026-05-26-professional-support-services-] https://www.usaspending.gov/award/CONT_AWD_N0016424F3006_9700_N0017819D7883_9700/  →  `01_sources/2026-05-26_usaspending-gov_professional-support-services-pss-specifically-fleet-readine.md`

## 9. Verification flags

Initialized at scaffold time, 2026-05-21. Will be expanded as research proceeds.

### 9.1 The classification gradient is a load-bearing constraint on this entire research track

Naval damage and ship-survivability data has a steep classification gradient, and the publicly-available material is only a thin slice of what the Navy actually knows. This is the single most important constraint shaping what this research can and cannot do, and it shows up in almost every section that follows.

The substantive operational content — how damage actually propagates through a specific ship class, which systems are vulnerable to which weapons, and validated distributions of how long real repairs actually take — almost certainly lives at SECRET or higher classification and is not available at unclassified level. What we **can** see at unclassified level is necessarily limited: doctrine documents, public congressional testimony framing the work, generalized methodology descriptions, sanitized vignettes from historical incidents, and academic or NAVSEA-published unclassified abstracts.

What this means for the research:

- Every claim we make from public Carderock material has to be explicitly tagged as unclassified-only, and we cannot let language imply that what we see is the full operational picture.
- The research can usefully establish four things: that the modeling exists at all, what NAVSEA and Carderock publicly say about its scope, what GAO and congressional oversight have written about the associated capabilities and gaps, and what the unclassified methodology implies about whether training injection is feasible in principle.
- The research **cannot** usefully establish actual damage-rate predictions, specific ship-system vulnerability data, or repair-time distributions at operationally-meaningful fidelity. Any such claim would either require classified access (out of scope for this vault) or it would be speculation (labeled accordingly).
- Any recommendation that comes out of this work has to respect the gradient. For example, the recommendation may end up being "engage NAVSEA and Carderock to scope a classified collaboration" rather than "build an unclassified training-injection module," because the latter may not be possible at the fidelity the customer actually needs.

### 9.2 Standing verification posture

- All claims labeled per SOP §2.1 rule 4: **FACT**, **Assessment**, or **Speculation**.
- All FACTs must carry an `[s.YYYY-MM-DD-slug]` citation tag pointing to an ingested source.
- Two-source rule applies to non-trivial claims (money, timelines, named people, attribution) per SOP §2.1 rule 2.
- Re-verify POCs every 90 days per SOP §2.1 rule 3.

### 9.3 The research origin is non-public; the contact is not citable — load-bearing constraint

This research track was initiated based on a working observation from a working-level Navy ship-repair contact. That contact is not named in this file, will not be named in any brief derived from this file, and is not the source of any FACT, Assessment, or Speculation entry. Their framing informs what to look for; it does not enter the FACT chain.

The discipline that follows from this constraint:

- Every claim in this research file and in any derived brief must be supported by public sources alone, per the FACT-Assessment-Speculation labeling in the SOP. The contact's framing is treated as analyst-side intuition that scopes the research, not as evidence within the research.
- No identifying detail about the contact — their organization, their role, the team they sit on, the specific exercise program they are involved with — goes into any artifact at any sensitivity tier. If a reference is needed at all, the standard generic phrasing is "a working-level Navy ship-repair contact."
- The contact's organization is reachable via standard public-facing engagement paths. The play is to use those public paths (industry days, formal SBIR or STTR responses, NAVSEA-hosted touchpoints) and not to leverage the contact's working-level channel directly. See section 11 for the engagement implications.
- If a future deliverable benefits from a quote or framing that originates with the contact, that framing must first be matched against a public source — either a public statement by a named individual at the relevant Navy organization or an analytical assessment that the operator is comfortable labeling as such. The contact themselves stays out of the brief.
- This constraint is parallel to the classification gradient in section 9.1. Both are sensitivity disciplines that limit what can be said in derived artifacts. Both are load-bearing on the integrity of the eventual recommendation.

### 9.4 "PAE Industrial Operations" terminology — RESOLVED 2026-05-23

The May 2026 Navy Shipbuilding Plan (page 34) uses the term "PAE Industrial Operations" to describe a Navy-internal organizational consolidation that combines the Navy Regional Maintenance Centers, NAVSEA's Industrial Operations Directorate, and the four public Navy Shipyards into a single structure.

**Operator confirmed 2026-05-23:** PAE Industrial Operations as used in the Navy Shipbuilding Plan is a Navy reorganization, not a commercialization of the public shipyards and Regional Maintenance Centers, and not a private contractor.

**Discipline going forward:**

- PAE-IO in this research file and in any derived deliverable refers exclusively to the Navy organizational structure described above.
- The acronym expansion of "PAE" in this Navy-internal context is not given in the primary source. If a NAVSEA or Office of the Secretary of the Navy organizational announcement that expands the acronym appears, it should be added to the glossary.
- Specific commercial contractors in the Navy ship-repair-and-overhaul space should be named in the research file only when they surface organically in ingested sources, not pre-emptively assumed.

---

## 10. Research plan (OSI-only)

This plan is the scaffolded starting point — refine after initial scoping.

### 10.1 Primary-source ingest targets (priority order)

1. **NAVSEA / NSWC Carderock Division publications and public materials.**
   - NAVSEA Public Affairs releases mentioning Carderock BDR / survivability work.
   - NSWC Carderock public technical publications (the Naval Engineers Journal and SNAME-presented papers historically have NAVSEA-authored unclassified content on survivability methodology).
   - DVIDS for Carderock-related coverage and event imagery.

2. **Congressional oversight — fleet readiness and ship maintenance.**
   - SASC and HASC public hearings on fleet readiness, ship maintenance backlog, depot capacity (`armed-services.senate.gov`, `armed-services.house.gov`). Recent hearings on CNO posture, Navy readiness, and OSD acquisition transformation are likely sources.
   - SASC/HASC reports accompanying NDAA markup (specifically the Seapower and Readiness subcommittee marks).

3. **GAO reports.**
   - GAO has a multi-year history of reports on Navy ship maintenance, depot capacity, and the public-private shipyard mix. Targeted searches: "ship maintenance backlog," "depot capacity," "Navy industrial base," "private shipyard capacity."
   - GAO reports on Navy LVC training and joint training architecture are an adjacent thread.

4. **CRS reports.**
   - `crsreports.congress.gov` for "Navy ship maintenance," "Pacific Deterrence Initiative ship repair," "industrial base shipbuilding and repair," and any product on attrition / wargaming assumptions.

5. **Budget books and budget justifications.**
   - DoD comptroller (`comptroller.war.gov`) FY26 and prior — Navy O&M and ship-depot maintenance line items.
   - Navy budget exhibits for ship maintenance and Carderock-relevant RDT&E line items.

6. **Adjacent / context (tier 4 trade press; use sparingly).**
   - USNI News, Defense News, Breaking Defense, Naval News for context and named-personality quotes (with click-verify per SOP rule 6).

7. **PAE Industrial Operations consolidated structure — public footprint.**
   - NAVSEA and Office of the Secretary of the Navy organizational announcements that name PAE-IO and define its scope.
   - Navy Regional Maintenance Center and public Navy Shipyard contracting activity that flows through PAE-IO (via the existing vault tooling: `usaspending.py` and `sam_gov.py`).
   - Public testimony and trade-press coverage of the consolidation and its effect on ship-repair capacity.
   - Specific commercial ship-repair contractors named in the research file should appear only when they surface organically in ingested sources, not pre-emptively assumed.

### 10.2 Two strongest counter-arguments a skeptical reviewer would raise

A reviewer who wanted to kill this research track would raise the following two arguments. The research plan must answer each, with primary-source evidence, before the working hypothesis can be promoted to a recommendation.

1. **"The fleet and the industrial base already plan for warfighting attrition; the gap you're claiming doesn't exist."**
   - Counter-evidence shape: DON Strategic Readiness Plan, recent SASC/HASC testimony from the CNO and NAVSEA Commander, and the FY26 Navy budget justifications already explicitly discuss warfighting-scale attrition and repair-capacity demand. If the public record shows the planning assumptions ALREADY incorporate realistic damage rates, then the "training assumptions and IO planning understate damage" leg is wrong — there is no gap to close, only an execution problem on already-known requirements.
   - This is the highest-priority disconfirming check. Pull SASC/HASC testimony and the Navy FY26 OSP/exhibit text first.

2. **"OSI-grade Carderock modeling can't drive operationally-meaningful training injection; the useful modeling is classified."**
   - Counter-evidence shape: NAVSEA / Carderock public materials make clear that the publicly-discussed BDR work is methodology and doctrine rather than damage-rate predictions or vulnerability data. GAO reports referencing Carderock's modeling discuss it at the program-management level, not at the technical-output level. Any training-injection use of OSI-derived Carderock material would necessarily be at a vignette-level fidelity, not at a quantified damage-rate level.
   - If this counter is correct, the research track's deliverable shifts from "OSI-based training injection module" to "engagement strategy for classified collaboration with NAVSEA / Carderock," which is a meaningfully different opportunity shape.

A third possible counter — that PAE-IO's "understatement" may be deliberate budgeting posture rather than a planning blind spot — should be tracked but is not a falsifier; even if planning is deliberately conservative, the training-injection question remains separable.

### 10.3 Sequencing

1. **Week 1:** Scope source-finding. Add `_search-config.yaml` for this opportunity with target NAVSEA / Carderock / SASC / GAO / CRS queries. Pull the two disconfirming-evidence sources first (DON Strategic Readiness Plan, FY26 Navy budget) to test the hypothesis early. **In parallel:** begin §11.1 engagement-surface inventory (no outreach yet, just public-source mapping of POCs and on-ramps).
2. **Week 2:** If hypothesis survives Week 1 disconfirmation, broaden to Carderock public materials and PAE-IO industrial footprint. Begin §11.2 training-progression design at concept level (tabletop curriculum outline; site-visit logistics scoping; pilot-operations feasibility frame).
3. **Week 3:** Synthesize into a research-file update with FACT-labeled findings, revised hypothesis or recommendation, and a Gate 1 brief decision (continue / pivot / drop). Cross-reference §11.1 engagement inventory and §11.2 training-design concept against the recommendation.

---

## 11. Engagement & relationship strategy

<!-- sensitivity:internal -->

This section addresses the scope-expansion items added 2026-05-21: (a) design of robust training from tabletop scenarios to pilot repair operations, and (b) developing NSWC Carderock relationships, which are assumed not to exist at scaffold time.

The engagement work stream proceeds **in parallel with** the primary-source research in §10 — not blocking on it — because relationship cadence at Navy labs is months-to-years, and starting the inventory and on-ramp scoping early is low-cost and unaffected by whether the §7 hypothesis ultimately survives disconfirming checks.

**Engagement-paths discipline (load-bearing).** The Ship Repair Facility Japan Regional Maintenance Center (SRF-JRMC) and adjacent Pacific Fleet ship-repair organizations are research subjects in this track because the public Ship Wartime Repair and Maintenance Exercise program (SWARMEX) described in NAVSEA Public Affairs releases is core to the working hypothesis (see sections 1, 7 leg 1, and 9.3). Engagement with SRF-JRMC and its peer organizations proceeds via standard public-facing paths only — published industry days, formal SBIR or STTR responses, NAVSEA-hosted touchpoints. The track explicitly does not leverage working-level channels at these organizations. The 11.1 inventory below applies to these Pacific Fleet repair organizations as much as it does to NSWC Carderock; the Carderock side starts from zero, and the Pacific Fleet side is to be approached as if it also starts from zero in any artifact that names a specific organization.

### 11.1 Engagement-surface inventory (Week 1, parallel to §10)

> **Scope note added 2026-05-25.** This inventory was built around the prior NAVSEA / Carderock customer framing. The engagement-paths target set is expected to broaden once the alternative training-systems-chain customer hypothesis is source-grounded in the next find_sources pass — likely adding Navy training-organization industry days, Sailor 2025 / Ready Relevant Learning engagement forums, and training-system program-office touchpoints to the on-ramp map. See `_red-teams/2026-05-25-gemini-pro-right-to-win-reframe-dialogue.md` and decision log entry 2026-05-25. The current inventory remains in place as the prior-framing on-ramp map.

**Goal:** map all public-source on-ramps to NSWC Carderock Division and adjacent Navy labs / sponsors. NO outreach yet — this is desk research only.

**Targets:**
- Carderock command directory and public technical-engagement office contacts (`navsea.navy.mil/Home/Warfare-Centers/NSWC-Carderock/`).
- Recent NSWCD-authored conference papers (ASNE Day, SNAME annual meeting, NDIA Combat Systems Conference) — extract author bylines + affiliations for the BDR / survivability-modeling line of work.
- SBIR / STTR topic authorship — Carderock topics on `sbir.gov` over the last 3 years, particularly those touching BDR, survivability, structural modeling, M&S.
- Federal Lab Consortium tech-transfer queue for any Carderock entries.
- Naval lab industry days, NAVSEA Industry Engagement Day, ASNE Day, SNAME annual — schedule mapping for next 12 months.
- NAVSEA HQ engagement portals — Industry Engagement Day, NSPS / Naval Sustainment System leadership.

**Adjacent intro paths to audit:**
- Existing CACI / Carderock contract history via USAspending (PIID search for CACI and ARKA legacy contracts at the NSWCD UEI).
- CACI personnel with NSWCD work history — internal LinkedIn / HR check (operator-side; not in this research track).
- CACI relationships at adjacent NSWC sites: Dahlgren, Crane, Indian Head, Port Hueneme, Panama City. Lateral relationships at these sites often produce warm intros to Carderock.
- ONR program officers in the relevant portfolios (Sea Warfare and Weapons, Force Health Protection, Code 33/35).
- Naval War College, Naval Postgraduate School, US Naval Academy faculty who have collaborated with Carderock on BDR or survivability research.
- Professional society relationships: SNAME (Society of Naval Architects and Marine Engineers), ASNE (American Society of Naval Engineers), MORS (Military Operations Research Society).

**Output:** a `03_pocs.md` POC table populated with named individuals + public-source URLs + which on-ramp they sit on. **No outreach until the table is complete and the operator green-lights specific contacts.**

### 11.2 BDAR repair-side training pipeline — classroom, then facility visits, then hands-on

> **Re-scope added 2026-05-25 from corpus-cleanup dialogue.** The earlier draft of this section treated NSWC Carderock as if it were a single all-purpose customer organization spanning damage modeling, BDAR doctrine, and a hands-on training venue. The 2026-05-25 corpus-cleanup dialogue with Gemini Pro corrected that conflation. The two roles split as follows. **Carderock (NSWCCD)** is the Navy's ship-survivability and structural-mechanics technical authority — Live Fire Test & Evaluation, computational shock/damage modeling, structural test rigs — which makes it a plausible source for **scenario inputs** (the physics and survivability data behind a damage vignette), not a doctrine writer and not principally a schoolhouse. **Naval Warfare Development Center (NWDC)** writes Naval Tactics, Techniques, and Procedures (NTTPs) and Tactical Memorandums (TACMEMOs) — which makes it the more plausible **BDAR doctrine writer** for the curriculum content that this pipeline delivers. Hands-on **damage-control wet-trainer venues** in the fleet (USS Buttercup, USS Trayer, Surface Warfare Engineering School Command and similar Navy schoolhouses) are the conventional hands-on practice path for organic-Navy DC training; whether they are also the right delivery venues for contractor-supplied BDAR/BDAT scenario products is one of the questions the next find_sources pass is designed to answer. The named entities in this re-scope (NWDC, NSWCCD, SWESC, USS Buttercup, USS Trayer) are not new entities to the vault — they appear in the acronym table, the dialogue files, or existing FACTs — and the re-scope itself is a structural reorganization of where this section assigns each role, not a new named-contractor claim. See `_red-teams/2026-05-25-gemini-pro-corpus-cleanup-dialogue.md` Pushback 1 and decision log entry 2026-05-25. The pipeline text below retains the prior framing for now and will be rewritten end-to-end after the next find_sources pass produces ingested primary sources naming the actual training-organization owners.

This section covers training for the people who actually do the repair work after a ship is hit. The next section, 11.3, covers the separate pipeline for the damage-assessment teams who tell the repair crews what to fix first.

The proposed pipeline is a three-step ladder, with each step a fidelity step-up and also potentially a classification step-up. The point of designing this at the concept level now — even before the hypothesis in section 7 has cleared its disconfirming checks — is so that the gate-1 brief in week 3 can describe a concrete program shape rather than just asserting that a program is needed.

**Step 1 — tabletop scenarios, classroom format, fully unclassified.** The first step is paper-and-discussion, run by an instructor. Trainees work through realistic damage scenarios without any equipment in the room.

- Learning objectives at this step: sequencing the damage-control response, triaging which repair actions matter most, identifying supply-chain pressure points, and working through multidomain scenarios where the ship is also being attacked through cyber, electronic warfare, or space-disrupted communications channels.
- Source material can come from public case studies — USS Stark, USS Cole, USS Fitzgerald, HMS Sheffield, the Moskva sinking — open-source threat libraries, public NAVSEA and Carderock methodology papers, and sanitized vignettes built from the above.
- Audiences run from junior officers to damage-control teams to repair-yard supervisors to multidomain joint planners, with different content depth for each.
- Format options include scenario card decks, instructor-led workshops, and multi-week curricula.

**Step 2 — guided site visits to actual repair facilities.** Once trainees have the classroom foundation, the next step is taking them to where the work actually happens.

- Candidate facilities are NSWC Carderock itself (with its full-scale tank facility and structural-test rigs), NSWC Philadelphia (which handles ship machinery), the intermediate maintenance activities at fleet ports, the four public naval shipyards at Norfolk, Portsmouth, Puget Sound, and Pearl Harbor, and selected private repair yards. Specific private contractor names are added only as ingested sources surface them.
- Classification typically steps up at this step. Tabletops can stay fully unclassified, but facility tour content usually begins at controlled-unclassified-information level, and walking trainees through instrumented test-beds may require a security agreement.
- Logistics matter as much as program design. Travel planning, badge sponsorship, escort coverage, and clear limits on what can be discussed — these are real operational tasks, not afterthoughts.

**Step 3 — hands-on practice on a real or instrumented platform.** The top of the ladder is the trainee actually performing assessment and repair planning on something that responds like a damaged ship system.

Three feasibility models, in increasing order of realism and difficulty:

- A simulator-only setup — a digital twin of damage propagation, no live equipment in the room.
- An instrumented test-bed — a real damaged subsystem on a controlled rig, where the training cohort performs assessment and repair planning against actual hardware.
- Live operations on a training hull — the most realistic, also the most operationally demanding. This would require Navy training-hull access, possibly through the Naval Sea Cadet Corps fleet or ex-service-vessel partnerships, each of which is a separate scoping problem.

The instrumented test-bed at NSWC Carderock or a partner site is the highest fidelity that is realistic to achieve at unclassified level.

### 11.3 BDAT training pipeline — gamified simulation first, then real-world exercises

> **LVC scope note added 2026-05-25.** Where this section refers to "live, virtual, constructive" or to simulation platforms, the Navy-customer interpretation is specifically Navy Continuous Training Environment (NCTE)-compliant Fleet Synthetic Training using HLA / DIS federation standards — not generic commercial AR/VR or stand-alone gaming engines. Per the 2026-05-25 corpus-cleanup dialogue with Gemini Pro, a BDAT simulation product that does not federate into the existing Navy synthetic training architecture is unlikely to be procured as "Navy LVC" even if it is technically live/virtual/constructive in the generic sense. The next find_sources pass is testing whether NCTE-compliance is a hard requirement or a strong preference, and where the BDAT training-system program-of-record sits if one exists. See `_red-teams/2026-05-25-gemini-pro-corpus-cleanup-dialogue.md` and decision log entry 2026-05-25.

This section covers training for the people who **assess** damage, which is a different skill from doing the actual repair work covered in the previous section.

When a ship gets hit, a damage-assessment team has to look at what just happened and answer four questions fast: how bad is the damage, can the ship still fight, what needs fixing first, and where should the repair team start. The repair team can only act on what the assessment team tells them, which is why we treat this as a separate, earlier training pipeline rather than rolling it into the repair training in section 11.2. Same overall mission, different audience, different cadence of practice, and different fidelity ramp.

The proposed pipeline has two phases, in this order:

**Phase 1 — high-frequency gamified practice between live exercises.** The point of this phase is volume. Damage-assessment skill decays without practice, and live exercises happen rarely. A gamified simulation layer — running on software platforms, on instrumented training rigs, or both — gives assessment teams enough repetitions to stay sharp.

Candidate software platforms are open research — specific commercial military training platforms, simulation engines, and serious-game toolchains should be named only as ingested sources surface them or as the operator scopes a vendor inquiry. The 2026-05-21 and 2026-05-23 source-finder passes did not surface a clear set of platform options; this is an open research thread that requires either targeted operator-initiated outreach (industry days at I/ITSEC, DoD SBIR Phase II award catalogs, NWDC product listings) or further source ingestion. Categories of platforms worth investigating once sources surface them: commercial military training simulation engines, federated-simulation toolchains (DIS / HLA protocol families), digital-twin / scenario-engine pipelines, and tabletop digital-wargame engines used as gamification-mechanic references.

Candidate hardware-in-the-loop or instrumented simulation paths:

- Carderock's existing structural shock-and-vibration rigs, repurposed in a controlled training mode rather than R&D mode.
- Augmented-reality or virtual-reality headset stacks that overlay damage on a digital twin of a known ship class.
- Tabletop instrumented training boards — physical mock-ups with embedded sensors that generate live-feed damage signatures the trainee has to classify.

Gamification mechanics that are pedagogical rather than cosmetic:

- Scenario branching keyed to the trainee's first-call damage classification, so a wrong call triggers cascading downstream consequences in later repetitions and the trainee experiences the cost of getting the assessment wrong.
- Scoring and after-action replay compared to the ground-truth damage state.
- Leaderboards across ships, squadrons, or training cohorts to drive practice volume.
- Replay archives that feed back into doctrine-update loops at NWDC and surface-force training authorities.

Audience scoping — three different cohorts at three different intensities:

- **Ship-level damage-control teams.** Highest volume of practice, shortest individual scenarios.
- **Fleet-level damage-assessment cells** sitting at numbered-fleet staffs. Longer scenarios with more emphasis on triaging the mission impact, not just the physical damage.
- **Joint damage-assessment staff at Combatant Command level.** Cross-domain scenarios — kinetic damage on a ship combined with simultaneous cyber, electronic-warfare, and space-disrupted-communications problems. This is the multidomain framing that links back to the scope statement in section 1.

**Phase 2 — real-world exercises that the simulation layer cannot replace.** Once teams are practicing reliably in simulation, the pipeline graduates them into real exercises where the cost-per-repetition is much higher but the fidelity is also much higher.

Three modalities:

- **Embedded damage-assessment injects in existing fleet exercises** — COMPTUEX, RIMPAC, Large-Scale Exercise, and smaller events like ANTX (Advanced Naval Technology Exercise) and Trident Warrior. The approach is to add a small assessment-cell module that runs in parallel with the parent exercise rather than replacing existing scenarios, because nobody wants to redesign COMPTUEX around a new training module.
- **Carderock-instrumented controlled events.** These are the bridge between pure simulation and full live exercise: ground-truth damage state is known because Carderock controls the rig, but the participating team experiences it as real.
- **Joint red-team / blue-team evolutions.** A red team generates realistic damage signatures from a known threat library; the assessment cohort classifies them in operationally-realistic time pressure. Useful at multidomain level because the threat library can include non-kinetic effects.

**Why simulation goes first and live exercises second.** This is the proposed order for two reasons. First, skill retention is driven by repetition, and only the simulation layer can supply repetitions at a usable cadence — a single live exercise can be a year apart. Second, each live exercise costs orders of magnitude more than a simulation repetition, so live time should be reserved for scenarios that the simulation cannot replicate. There is also a classification angle that mirrors the same step-up logic as the repair-side training in section 11.2: simulation content can be designed unclassified or at controlled-unclassified-information level, and live exercises can step up to classified ground-truth only when the participant cohort is cleared and the venue is approved.

**The differentiator hook to watch.** If ARKA's electro-optical, infrared, and hyperspectral sensor signature libraries can be released for training use, they could feed the simulation engine with realistic threat-effect signatures that the incumbent training competitors — SAIC, Leidos, HII Mission Technologies — cannot easily source. This is a hypothesis to test against ARKA's intellectual-property and release-authority constraints, not a finding. It is the most likely way the engagement strategy in this section turns into a real differentiator at the recommendation stage.

**Three ways this whole subsection could be wrong.** Cross-listed with the open questions in section 2:

- A Department of Defense-funded damage-assessment serious-game already exists at sufficient maturity that this pipeline would be a me-too entry. The places to look are SBIR Phase II and Phase III award databases, the NWDC product catalog, and Naval Postgraduate School and Naval War College thesis libraries.
- Damage-assessment training is already deeply embedded in COMPTUEX, RIMPAC, and LSE at a depth that leaves no gap for a new pipeline.
- The simulation layer cannot achieve operationally-meaningful realism at unclassified level — which is the same classification-gradient problem that threatens leg 3 of the hypothesis in section 7, applied specifically to simulation content.

### 11.4 Engagement timeline assumption

- **Months 1-2:** §11.1 engagement-surface inventory complete; first concrete targets identified for outreach.
- **Months 3-4:** First-touch outreach via the lowest-friction on-ramp (typically an SBIR / STTR proposal response or industry-day attendance). Goal at this stage is a recurring conversation, not a contract.
- **Months 6-9:** Conversation-to-pilot conversion. A small SBIR Phase I or NDA-only technical exchange would be a realistic Month-9 milestone.
- **Months 12-18:** Pilot training-design engagement, possibly under an SBIR Phase II, BAA, or sole-source justification if Carderock has determined CACI / ARKA is uniquely positioned.

Treat all month numbers as Speculation per SOP §2.1 rule 4 until corroborated by Carderock's actual public engagement cadence.

### 11.5 Risks specific to the engagement work stream

| Risk | Mitigation |
|---|---|
| Carderock's engagement bandwidth is locked up by incumbent technical partners | Lead with a differentiated capability hook (ARKA EO/IR + Agentic-AI-based threat classification has no direct Carderock-side equivalent — could create a real "this is new, talk to us" entry) |
| Outreach treated as marketing rather than substantive technical engagement | First-touch must be substantive — an SBIR proposal, BAA white paper, or published technical question, not a generic capability brief |
| Multi-touch sequence is required, and operator cadence may not sustain it | Acknowledge upfront — engagement plan is months not weeks; mid-cycle slippage is normal and not a kill signal |
| CACI may not have the right Navy-lab cultural credentials | Audit early via §11.1 adjacent-relationship mapping; if no warm path exists, a longer first-touch via SBIR Phase I is the right entry |
| BDA serious-game space may already be saturated by canonical incumbents (SAIC, Leidos, and Carderock-adjacent simulation vendors named only as sources surface them) | Lead with an ARKA-signature-library differentiator (§11.3) rather than a generic platform pitch; if no differentiator survives §2 disconfirming checks, the BDA pipeline scope should be dropped rather than pursued as a me-too entry |
| Sim-vs-live progression order is mistaken — Navy training authorities may insist live-exercise-first | Treat the "sim-first" claim as a §7-leg-6 hypothesis to be tested; if Navy training doctrine inverts the order, redesign §11.3 around live-exercise lead with sim as remediation tooling |

<!-- /sensitivity -->

---

*This research file was scaffolded on 2026-05-21 and expanded twice the same day to cover a three-step repair-team training pipeline plus a parallel relationship-development work stream (sections 11.1 and 11.2), and a separate damage-assessment team training pipeline progressing from gamified simulation to real-world exercises (section 11.3). The operator authorized source research on 2026-05-21 and the first source-finding pass ran the same day, queuing 67 candidates in `_inbox.md`. Research was paused on 2026-05-22 to apply a readability fix across the vault and to fold lessons from a Medium article on software-fundamentals applied to AI workflows into the process. See the decision log for the full chain.*

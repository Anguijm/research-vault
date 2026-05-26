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

This research track examines whether the U.S. Navy has a real business opportunity for CACI in **a five-level analog-first progression of gamified operational-decision scenarios for the Battle Damage Assessment and Repair (BDAR) team and the operational commanders the team supports**. The customer set sits at the Navy repair activities — the four public naval shipyards (Norfolk, Puget Sound, Pearl Harbor, Portsmouth), the Regional Maintenance Centers (RMCs) including the forward-deployed Ship Repair Facility–Japan Regional Maintenance Center (SRF-JRMC), and the related forward-deployed repair organizations — plus the fleet commanders who decide where damaged ships go. The full progression is documented at §11.3. The scope was last corrected on 2026-05-26, replacing earlier framings that pointed at the Navy's schoolhouse / individual-Sailor training pipeline. See the 2026-05-26 decision log entries for the structural corrections.

The product is a five-level progression, not a single 1-hour session. Level 1 is 5 to 15 minute flash drills on printed cards. Level 2 is 30 to 45 minute linked-decision sequences. Level 3 is the 1-hour full gamified wardroom session that integrates all six decision moments. Level 4 is a 2 to 4 hour multi-session campaign across a deployment cycle. Level 5 is software-driven scenario injection into live fleet exercises (COMPTUEX, RIMPAC, Large-Scale Exercise, SWARMEX). Each level can be procured separately. Each level builds a reference for the next. The analog-first design lowers technical risk, iterates faster on scenario content, and proves the concept with the customer before CACI commits to game-engine investment. The AI scenario engine pays for itself starting at Level 4 when the customer commits to scale.

There are two audiences for the same scenario base. The **repair-activity wardroom** at a public shipyard, RMC, or SRF-JRMC is one audience — they prepare to receive a damaged ship and mobilize against the work. The **fleet commander** who owns the damaged ship is the other audience — they decide where to send her based on proximity, repair capability, security posture, and alliance access. The port-selection scenario in particular runs naturally for both audiences. Same scenario content, different decision-maker focus, different format depending on which level of the progression the customer is buying.

CACI does not build schoolhouse curriculum. CACI builds situational exercise content for operational decision-makers. The known capability lineage is the U.S. Indo-Pacific Command (INDOPACOM) Pacific Multi-Domain Training and Experimentation Capability (PMTEC) exercise-design work that CACI already executes. CACI also already holds the federal contracting vehicles the Navy can issue task orders against — OASIS, CIO-SP3, and GSA Multiple Award Schedule, all held by the CACI NSS, LLC subsidiary. The procurement-pathway question is therefore not "find a new Navy vehicle" but "convince a Navy fleet command to issue a task order against vehicles CACI already holds." This research asks whether that conversation can be turned into actual procurement.

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

This subsection is in §3 deliberately. Three large federal contracts surfaced during the 2026-05-25 USAspending triage are NOT Navy-funded. They tell us how the Department of Defense buys related work-types when it decides to buy them. The three are NOT all the same work-type — they split into three distinct categories. The §5 and §7 investigations need this categorization to identify which Navy contracting pathway matches the corrected-scope sub-product.

**FACT:** CACI NSS, LLC holds a $194 million task order (PIID 47QFCA20F0042) for *"Plans, Operations, Logistics, Engagement, Training, Exercise, and Assessment Support to AFRICOM"* — Department of Defense / Department of the Army funder, awarded via the General Services Administration Federal Acquisition Service against parent IDC GS00Q14OADU121 (an OASIS-equivalent governmentwide acquisition contract) [s.2026-05-26-the-purpose-of-this-award-is-t]. The CACI NSS, LLC subsidiary additionally holds CIO-SP3 (NITAAC IT services) and GSA Multiple Award Schedule (GS-35F-349CA) — both governmentwide vehicles against which any federal customer (including any Navy fleet command) can issue task orders directly.

**FACT:** Parsons Government Services Inc. holds a $556.8 million Command, Control, Communications, Computers, Combat Systems, Intelligence, Surveillance, Reconnaissance, and Targeting (C5ISR) / Exercises / Operations / Information Services (CEOIS) task order providing near real-time situational awareness and decision support to the Department of Defense Combatant Commands — Office of the Secretary of Defense funder via GSA [s.2026-05-26-the-purpose-of-this-award-is-f].

**FACT:** Axient LLC holds a $233.8 million Test, Exercise and Wargames Support contract — Missile Defense Agency funder, place of performance Huntsville, Alabama [s.2026-05-26-test-exercise-and-wargames-sup].

**Assessment.** The three contracts are NOT three examples of the same work-type. They are three distinct categories that the corrected-scope sub-product brushes against, and the analytical value lies in keeping them separate.

The **CACI NSS at AFRICOM** contract is broad professional services that explicitly includes exercise, training, and operations support as named scope elements. It is the closest analog to the corrected-scope sub-product. The contract demonstrates the work-type at multi-hundred-million-dollar scale on a GSA-side governmentwide vehicle. Importantly, the CACI NSS, LLC subsidiary already holds the vehicles a Navy fleet command can issue task orders against (OASIS, CIO-SP3, GSA MAS). The Navy procurement pathway is therefore not "find a new Navy vehicle" — it is "convince a Navy fleet command to issue a task order against a CACI vehicle that already exists." This is a sharper procurement story than the prior framing of §3.6.

The **Parsons CEOIS at OSD** contract is decision support for active commanders — software and contractor staff embedded at Combatant Commands helping the four-star and the J-staff make calls in real time. It is NOT exercise design. It is a different work-type. The Navy could buy similar work for fleet commanders making port-selection or other operational calls in real time, but that is not the corrected-scope sub-product directly — it is an adjacent product.

The **Axient at MDA** contract is exercise and wargames work specifically for missile defense testing and operator training. It is the closest analog to the corrected-scope sub-product in work-type but in a completely different domain (missile defense, not naval repair). It demonstrates that a single DoD agency can procure a multi-hundred-million-dollar exercise-and-wargames contract — relevant precedent for a Navy fleet command or SYSCOM authority procuring similar work for the naval-repair domain.

The procurement-pathway gap §5 and §7 carry forward is therefore narrower than the prior framing claimed. The Navy does not need to invent a new contracting vehicle. The Navy fleet commands can issue a task order against CACI NSS, LLC's existing OASIS or CIO-SP3 holdings for the corrected-scope sub-product. The §5 and §7 investigations should identify which Navy fleet command will be willing to do that and on what scope language.

### 3.7 Convergence assessment

The five signals — senior-leadership statements (§3.1), the SWARMEX-Cebu exercise artifact (§3.2), the USNI / CIMSEC policy-community pressure (§3.3), the Joint / USMC contractor-exercise-design funding lines in the FY27 comptroller justification book and the CNRMC contractor-support footprint via Invictus (§3.5), and the non-Navy Procurement Pathway Prototype that tells us what vehicle-shape to hunt for in Navy (§3.6) — converge on a coherent picture under the corrected scope. Senior Navy leadership is publicly committing to wartime repair capability and combat surge readiness. The Navy is publicly executing the most directly relevant exercise type in the most directly relevant venue (SWARMEX-Cebu). The Navy professional community is publicly arguing the gap is real. The Department of Defense procures contractor-delivered exercise design and scenario generation at the Joint and Marine Corps levels — that procurement pattern is real and named in the FY27 budget. CACI specifically is already executing exercise / training / operations support work at AFRICOM and adjacent COCOMs at multi-hundred-million-dollar scale.

What §3 does NOT yet establish — and what §5 (competitive landscape) and §7 (working hypothesis) have to test as the load-bearing analytical work — is the specific Navy fleet-command vehicle under which a **1-hour turn-based gamified decision-scenario session for a staff cell or wardroom audience** would be procured. The DoD knows how to buy a multi-month, multi-million-dollar contractor team to plan and execute a Pacific Fleet SWARMEX; what is less obvious is how a local SRF commander or RMC training-cell head buys a short-form, high-fidelity decision-rehearsal session for a small repair-leadership audience under combat-tempo or contested-port conditions. The format-and-cadence distinction — short-form, high-fidelity, decision-tier audience, executed inside the rhythm of fleet exercise events rather than as a standalone training pipeline — is the specific sub-product whose Navy procurement pathway is the open question. §5 and §7 carry the burden of closing this gap.

Material from the prior §3 framing — Stimson Center MSMRO Task Force, GAO shipbuilding-oversight testimony, the FY27 shipbuilding $65 billion total, the White House Maritime Action Plan, the U.S.-Japan trade arrangement, and the Maritime Administration Port Infrastructure Development Program — is preserved in git history and in the 2026-05-25 corpus-cleanup dialogue. Under the corrected scope these are context-level rather than load-bearing for the recommendation.

<!-- ship: 2026-05-26 claude-opus-4-7 -->
<!-- pilot-section: first small-ship under _meta/small-ships-workflow.md -->
<!-- claim-count: 22 FACT + 7 Assessment + 0 Speculation. Verifier run 2026-05-26 (17 SUPPORTS / 4 PARTIAL / 0 DOES_NOT_SUPPORT / 0 UNVERIFIABLE). Red-team Gemini Pro Round 3 verdict: GO (3-round dialogue, see _red-teams/2026-05-26-gemini-pro-section-3-red-team-dialogue.md). Sealed 2026-05-26. -->


## 4. Customer landscape — Navy repair-activity ecosystem under the corrected scope

This section maps the candidate customer organizations for the corrected-scope product (gamified operational-decision scenarios for BDAR/BDAT teams at Navy repair activities, per §1). The customer-set is layered. At the strategic-direction layer sit the Secretary of the Navy and the Chief of Naval Operations. At the repair-activity layer sit the four public naval shipyards, the Regional Maintenance Centers (RMCs) including the forward-deployed Ship Repair Facility–Japan Regional Maintenance Center (SRF-JRMC), and Commander, Navy Regional Maintenance Center (CNRMC) as the parent command. At the doctrinal layer sits the Naval Warfare Development Center (NWDC) as the authority for the tactics, techniques, and procedures that any scenario content must be written against. At the fleet-command training-authority layer sit Commander, U.S. Fleet Forces Command (FLTFORCOM), Commander, U.S. Pacific Fleet (COMPACFLT), Commander, Naval Surface Forces (COMNAVSURFOR), and the U.S. Indo-Pacific Command Joint Operations Directorate (INDOPACOM J7). The §5 (competitive landscape) and §7 (working hypothesis) investigations have to identify which of these layers is the most accessible procurement-pathway for the corrected-scope sub-product.

### 4.1 Strategic-direction layer — SECNAV and CNO

The strategic-direction layer sets readiness priorities and approves budget direction. It is not the procurement-authority layer for the corrected-scope product, but the priorities it names determine what gets funded downstream.

**FACT:** Acting Secretary of the Navy Hung Cao signed the foreword of the Navy's May 2026 Shipbuilding Plan and the cover of the Department of the Navy FY27 President's Budget Press Brief dated 28 April 2026 [s.2026-05-26-don-fy27-press-brief].

**FACT:** Admiral Daryl L. Caudle, the Chief of Naval Operations, delivered a Statement on the Posture of the United States Navy before the House Armed Services Committee on 14 May 2026, naming maintenance as a warfighting requirement and announcing a planned deliberate study of Navy yard capacity [s.2026-05-26-2026-05-14-caudle-testimony].

**FACT:** Caudle's HASC testimony frames the FY27 posture around four named priorities — "Lethal & Effective Force," "Total Force Readiness," "Capable & Resilient Warfighter," and "Industrial & Logistics Capacity" — with the second priority (Total Force Readiness) explicitly covering Infrastructure, Maintenance, Operations, and Spares [s.2026-05-26-2026-05-14-caudle-testimony].

**Assessment.** The strategic-direction layer is naming the right problem — wartime repair and combat surge readiness — at the right level of priority. The corrected-scope product addresses the readiness side of those four priorities. The procurement signal for this product does not originate in the strategic-direction layer; the strategic-direction layer authorizes the framework under which the repair-activity layer and the fleet-command training-authority layer make procurement decisions.

### 4.2 Repair-activity layer — the four public naval shipyards

The four public naval shipyards are the receiving-side activities for U.S. Navy ships that need depot-level maintenance, modernization, and battle damage repair. They are named in CNO Caudle's testimony and in the DON FY27 Press Brief.

**FACT:** The four public naval shipyards are Norfolk Naval Shipyard (NNSY), Puget Sound Naval Shipyard (PSNS), Portsmouth Naval Shipyard (PNSY), and Pearl Harbor Naval Shipyard (PHNS), as named in CNO Caudle's HASC testimony [s.2026-05-26-2026-05-14-caudle-testimony].

**FACT:** Norfolk Naval Shipyard began a $442 million drydock modernization in May 2026 [s.2026-05-26-norfolk-naval-shipyard-begins-].

**FACT:** Pacific Naval Facilities Engineering Command published a Shipyard Infrastructure Optimization Program brief covering Puget Sound Naval Shipyard and Subordinate Bases (PSNS-SBS) infrastructure investments [s.2026-05-26-siop-brief-psns-sbs-2025-1].

**FACT:** The DON FY27 Press Brief funds six SIOP construction projects in FY27 across the four public shipyards [s.2026-05-26-don-fy27-press-brief].

**Assessment.** The four public shipyards are the heaviest-investment repair-activity nodes in the Navy enterprise — each receives multi-hundred-million-dollar infrastructure investment and each houses a workforce of thousands. They are the most likely site for a high-fidelity operational-decision-scenario exercise involving senior repair-leadership audiences. The procurement-authority layer for training and exercise content at the shipyard level is not yet source-grounded in the vault; the §5 competitive-landscape investigation has to map which authority within each shipyard (Production Department, Training Department, Operations) can directly procure exercise-injection content versus which has to route through CNRMC or NAVSEA.

### 4.3 Repair-activity layer — Regional Maintenance Centers and forward-deployed SRF-JRMC

The Regional Maintenance Centers (RMCs) execute intermediate-level maintenance at fleet concentration areas. The forward-deployed SRF-JRMC is the most consequential RMC for the corrected scope because it is the only one publicly executing wartime-repair exercises at a foreign port today.

**FACT:** Commander, Navy Regional Maintenance Center (CNRMC) is the parent command of the subordinate Regional Maintenance Centers (RMCs), per the Invictus Associates Navy Professional Support Services contract scope [s.2026-05-26-professional-support-services-].

**FACT:** Surface Team One (ST1) is named as a covered customer in the Invictus contract alongside CNRMC and the subordinate RMCs [s.2026-05-26-professional-support-services-].

**FACT:** SRF-JRMC, U.S. Seventh Fleet, U.S. Pacific Command, and U.S. Pacific Fleet executed the SWARMEX exercise on USS Ashland (LSD 48) at Cebu, Philippines, in coordination with Philippine Navy partners and local Philippine contractors [s.2026-05-26-uss-ashland-completes-ship-war].

**FACT:** Naval News identified Philippine Naval Sea Systems Command participation in SWARMEX-Cebu [s.2026-05-26-u-s-navy-rehearses-wartime-rep].

**Assessment.** CNRMC is the parent-command anchor that ties the RMCs together; SRF-JRMC is the operationally-most-exposed RMC because of its forward-deployed posture and active SWARMEX execution history. The Invictus contract confirms CNRMC procures contractor-supplied professional support services for itself, its subordinate RMCs, and Surface Team One — but as established in §3.5, the vehicle category (PSS on SeaPort-NxG) is not the right color of money for wargaming or scenario design. The procurement-authority pathway for the corrected-scope product at this layer is one of three possibilities the §5 and §7 investigations have to disambiguate: (a) a new task order against an existing CNRMC vehicle that bundles scenario design under "Fleet Readiness Support," (b) a separate procurement at the individual RMC level with the RMC's own contracting authority, or (c) direct SRF-JRMC wartime-readiness procurement with forward contracting authority. Per the §9.3 contact-protection discipline, the SRF-JRMC layer in particular is engaged via standard public-facing paths only.

### 4.4 Doctrinal authority — Naval Warfare Development Center

NWDC owns the doctrinal authority for Navy Tactics, Techniques, and Procedures (NTTPs) and Tactical Memorandums (TACMEMOs) that govern how the surface fleet fights and how repair activities support it. NWDC is not a procurement customer for the corrected-scope product directly — it is the doctrinal-content authority that any scenario portfolio must be written against to be operationally credible.

**Assessment.** The vault has not yet ingested a primary-source artifact that specifically establishes NWDC's role in BDAR/BDAT doctrine under the corrected scope. The 2026-05-25 corpus cleanup established NWDC as the BDAR doctrine writer (corrected from the prior framing that overcredited NSWC Carderock with both modeling-source and doctrine-writer roles). The §5 investigation should pull an NWDC product catalog or recent NTTP listing to verify what BDAR-related doctrine NWDC currently maintains.

### 4.5 Fleet-command training authorities

The fleet-command training-authority layer owns how the repair-activity teams train in fleet exercises. The §3.7 narrowed-gap analysis identified this layer as the most likely procurement-authority candidate for the corrected-scope sub-product (1-hour turn-based gamified decision-scenario sessions for staff-cell or wardroom audiences inside fleet exercise rhythm).

**FACT:** U.S. Fleet Forces Command (FLTFORCOM) is developing the Global Maritime Response Plan as the wartime force-generation counterpart to the peacetime Optimized Fleet Response Plan, with explicit intent *"to prepare the Fleet for Battle Stations—to ensure that the Navy is on a wartime footing capable of transitioning to 'General Quarters'"* [s.2026-05-26-fix-the-navys-expeditionary-re].

**FACT:** The peacetime Optimized Fleet Response Plan is governed by joint instruction COMUSFLTFORCOM/COMPACFLT INST 3000.15B / COMUSNAVEUR/COMUSNAVAFINST 300.15, dated 20 October 2020 [s.2026-05-26-fix-the-navys-expeditionary-re].

**FACT:** Commander, U.S. Pacific Fleet (COMPACFLT) published a press release noting USS Ashland's wartime repair and maintenance exercise was conducted alongside Philippine allies and U.S. 7th Fleet [s.2026-05-26-uss-ashland-completes-ship-war].

**Assessment.** FLTFORCOM and COMPACFLT are the joint owners of the peacetime force-generation framework and the developing wartime Global Maritime Response Plan. They are the most likely procurement-authority layer for fleet-exercise content under the corrected scope because they own the COMPTUEX, RIMPAC, and Large-Scale Exercise event rhythm that the corrected-scope sub-product (short-form decision rehearsal inside fleet exercise events) plugs into. The §5 and §7 investigations should target the specific contracting offices supporting these commands — the FLTFORCOM N7 (training and readiness) cell and the COMPACFLT N7 cell are the natural starting points for the §11.1 engagement-surface inventory.

### 4.6 Assessment of the customer landscape

The corrected-scope customer landscape is layered, with strategic-direction at top, repair-activity in the middle, fleet-command training-authority in parallel with the middle layer, and doctrinal authority feeding the middle layer's scenario content. The §3.5 procurement evidence (Joint / USMC exercise-design funding lines in the FY27 comptroller justification book; CNRMC procures contractor support today through PSS-on-SeaPort-NxG) plus the §3.6 vehicle taxonomy prototype (AFRICOM / Parsons / Axient explicitly-named Exercise / Wargames / Decision-Support vehicles) together suggest the corrected-scope sub-product will be procured at the fleet-command training-authority layer — most likely through a FLTFORCOM, COMPACFLT, or directly-by-SRF-JRMC vehicle that needs to be identified.

The procurement-authority candidate ranking the §5 investigation has to test is split into two layers — end-user / sponsor (who needs the sub-product and can advocate for it) and contracting-authority / pathway (who has the budget color and acquisition authority to actually buy it). The 2026-05-26 Gemini Pro red-team correction surfaced that conflating these layers was an error in the prior framing; SRF-JRMC is the most-likely end-user but probably does not directly hold the RDT&E / OPN budget authority required to procure a net-new gamified software platform — that authority more likely sits at Fleet (PACFLT N7 / N4 or FLTFORCOM N7 / N4) or SYSCOM (NAVSEA 04 or PEO IWS / PMS 408 equivalents) level.

**End-user / sponsor ranking** (who has the operational pull and authorizes the requirement):
1. **SRF-JRMC wartime readiness cell** — forward-deployed, operationally-most-exposed, operator-side §9.3-protected ground truth confirms contractor exercise planners are on contract here, audience and venue match the corrected-scope sub-product.
2. **CNRMC + subordinate RMCs + Surface Team One** — Navy-wide repair-activity layer, named in the Invictus contract, broader audience than SRF-JRMC alone.
3. **Public naval shipyards (NNSY, PSNS, PNSY, PHNS)** — heaviest-investment repair activities, longer procurement cycles, better-suited as second-customer once initial reference established.

**Contracting-authority / pathway ranking** (who can actually buy the sub-product):
1. **PACFLT N7 / N4 or FLTFORCOM N7 / N4** — owns COMPTUEX / RIMPAC / Large-Scale Exercise rhythm, has fleet-exercise contracting authority and the right budget color (OPN, RDT&E, or O&M depending on procurement structure), can sponsor the sub-product as an inject into existing fleet-exercise contracts.
2. **DIU, SBIR, or STTR pilot vehicle** — the standard new-technology-acquisition first-step path; lower per-engagement scale but unblocks the procurement-pathway-doesn't-exist-yet problem if a fleet-command vehicle is not immediately available.
3. **NAVSEA 04 or PEO IWS / equivalent SYSCOM authority** — owns the Navy training-systems acquisition apparatus at the SYSCOM level; longer procurement cycle than fleet-command direct but applicable if the sub-product needs to be procured as part of a broader training-systems program of record.
4. **INDOPACOM J7 joint-exercise vehicle** — owns joint multi-domain exercise procurement; cross-vault PMTEC opportunity establishes CACI as an active engaged participant. Most natural path if the sub-product enters as part of a joint-exercise contract that includes naval-repair scenarios.
5. **CNRMC parent-command via a non-PSS vehicle** — the PSS / SeaPort-NxG IDC is the wrong color of money but a separate CNRMC procurement on a different IDC is feasible if budget authority and color align.

NWDC remains as the doctrinal-sponsorship collaborator across both layers — not a buyer per se but the natural collaborator for scenario-content credibility regardless of which contracting authority procures the sub-product.

This two-layer ranking is the working hypothesis the §5 competitive-landscape and §7 working-hypothesis investigations will test against ingested primary sources and the disconfirming-evidence questions in §2.

<!-- ship: 2026-05-26 claude-opus-4-7 -->
<!-- small-ship: §4 sealed under the small-ships-workflow; Gemini Pro multi-section red-team CONDITIONAL-GO Round 2 (4 findings addressed: ARKA threat-vs-repair split, §5.3 candidate-set Assessment-tagging, end-user-vs-contracting-authority split, sub-product moat shift to gamified-software engine). See _red-teams/2026-05-26-gemini-pro-sections-4-to-7-red-team-dialogue.md. -->

## 5. Competitive landscape — contractor base for the corrected-scope sub-product

<!-- sensitivity:internal -->

This section maps the contractor base for the corrected-scope product (gamified operational-decision scenarios for BDAR / BDAT teams at Navy repair activities). The competitive picture under the corrected scope splits into four layers — a cross-customer Exercise / Wargames / Decision-Support incumbency that establishes the work-type at federal scale (§5.1), a Navy training-systems incumbency that is adjacent but not directly competitive under the corrected scope (§5.2), a Navy fleet-command exercise-planning incumbency that is under-mapped in public sources but is the most likely layer of direct competition (§5.3), and a Navy-customer professional-services incumbency at the corrected-scope customer (§5.4). The new-construction shipbuilder set and the international-partnership thread from the prior §5 framing have been moved to context-level cross-references per the 2026-05-26 scope correction; they remain in git history but are not load-bearing under the corrected scope.

### 5.1 Three distinct adjacent-work-type incumbents — keep them separate

The three large non-Navy federal contracts surfaced at §3.6 are NOT a single category. They split into three distinct work-types and the competitive analysis should reflect that.

**FACT:** CACI NSS, LLC holds a $194 million task order for broad professional services to AFRICOM with exercise, training, and operations support as named scope. Awarded via GSA Federal Acquisition Service against a governmentwide OASIS-equivalent vehicle (parent IDC GS00Q14OADU121) [s.2026-05-26-the-purpose-of-this-award-is-t].

**FACT:** Parsons Government Services Inc. holds a $556.8 million CEOIS task order providing near real-time decision support to the Department of Defense Combatant Commands — OSD funder via GSA [s.2026-05-26-the-purpose-of-this-award-is-f].

**FACT:** Axient LLC holds a $233.8 million Test, Exercise and Wargames Support contract for missile defense testing and operator training — MDA funder [s.2026-05-26-test-exercise-and-wargames-sup].

**Assessment.** CACI NSS, LLC at AFRICOM is the only one of the three that maps directly onto the corrected-scope work-type. Broad professional services that name exercise, training, and operations support. The other two are adjacent but distinct. Parsons CEOIS is decision support for active commanders, which is software plus contractor staff embedded at Combatant Commands — a different product than gamified scenario rehearsal. Axient at MDA is exercise and wargames work but for missile defense, not naval repair. None of the three are direct competitors for the corrected-scope sub-product at the Navy repair-activity level. CACI NSS is the same-vendor capability-lineage anchor. Parsons CEOIS is a procurement-precedent for OSD buying decision-support work at scale and is not a Navy demand signal. Axient at MDA is a procurement-precedent for a single DoD agency buying contractor-supplied exercise and wargames work at multi-hundred-million-dollar scale and is the closest work-type precedent for what a Navy fleet command or SYSCOM authority would procure under the corrected scope.

### 5.2 Navy training-systems incumbents — adjacent scope, not direct competition

The Naval Air Warfare Center Training Systems Division (NAWCTSD) administers a $2.51 billion Multiple-Award IDIQ vehicle for Navy training-systems sustainment and instructional services. The nine prime contractors on this vehicle constitute the Navy training-systems incumbent base.

**FACT:** On 31 March 2026, the Navy modified the NAWCTSD-managed training-systems support IDIQ to add $1.2 billion in ceiling, raising the total contract value to $2.51 billion, with nine companies selected to compete for task orders — BGI-Aero Simulation JV, CAE USA, Delaware Resource Group of Oklahoma, Engineering Support Personnel, Fidelity Technologies, FlightSafety Defense, LB&B Associates, LTSS JV, and Valiant Global Defense Services [s.2026-05-26-navy-selects-nine-contractors-1-2b].

**FACT:** The NAWCTSD-managed work covers sustainment and training support for fielded systems, including operating and maintaining training simulators, instructional services, simulator enhancements and relocations, systems management, engineering support, and logistics — across installations in Connecticut, Florida, Louisiana, Nevada, New Jersey, New Orleans, North Carolina, Texas, Virginia, and Washington — with period of performance running through August 2027 [s.2026-05-26-navy-selects-nine-contractors-1-2b].

**Assessment.** This is the Navy training-systems incumbent base for simulator sustainment and instructional services. Under the 2026-05-26 scope correction, the corrected-scope product is NOT this work-type — it is operational-decision-scenario design for repair-activity team leaders, not simulator sustainment for new-Sailor instructional pipelines. So the nine NAWCTSD primes are adjacent incumbents (they have Navy training relationships, contracting vehicles, and Navy installation access) but not direct competitors for the corrected-scope sub-product. Three of the nine — CAE USA, FlightSafety Defense, and BGI-Aero Simulation JV — have known capability in scenario design from adjacent aviation training contracts and could plausibly pivot to the corrected-scope sub-product if the procurement vehicle existed. The §11.1 engagement-surface inventory should monitor NAWCTSD vehicle modifications for scope expansion that bridges into the corrected-scope product.

### 5.3 Navy fleet-command exercise-planning incumbents — under-mapped, most likely direct-competition layer

The largest research-gap in §5 is the contractor base supporting fleet-command exercise authorities — FLTFORCOM, COMPACFLT, INDOPACOM J7, and the forward-deployed SRF-JRMC wartime-readiness cells. These commands procure exercise-planning support for COMPTUEX, RIMPAC, Large-Scale Exercise, SWARMEX, and unit-level workups, but the specific contractor incumbencies are not yet ingested as primary sources in the vault.

**Assessment (high-confidence, source-gap acknowledged).** Operator-side §9.3-protected knowledge confirms contractor exercise planners exist at SRF-JRMC's wartime readiness group; that ground truth informs the analytical direction of §5 without entering the vault as a citable claim. The 2026-05-26 Gemini Pro Round 2 red-team conceded that "fleet-command exercise-authority procurement (FLTFORCOM / COMPACFLT / SRF-JRMC direct) is a third valid path" beyond the NAWCTSD and NWDC pipelines.

**Assessment (Master Scenario Events List incumbent set, pending source-grounding).** The typical prime base for fleet-command and joint-exercise Master Scenario Events List (MSEL) contracts under similar procurement vehicles at adjacent Combatant Commands includes Booz Allen Hamilton, SAIC, and HII Mission Technologies (the operator-allowlisted set per `_entity-allowlist.yaml`) plus specialized exercise-design sub-tier players. The actual subset active at FLTFORCOM N7, COMPACFLT N7, INDOPACOM J7, and the SRF-JRMC wartime-readiness cell is NOT yet source-grounded in vault content — naming specific incumbents in this Assessment is candidate identification for source-targeting in the next find_sources pass, NOT a load-bearing FACT claim per the named-contractor discipline at `_meta/feedback_named_contractor_discipline.md`. The §7 leg 5 falsifier reasoning therefore frames the customer-access pathway feasibility question at the candidate-set level, with the specific incumbent subset to be source-grounded before any partnering or capture decision.

The §11.1 engagement-surface inventory has to map the specific contracting offices at FLTFORCOM N7, COMPACFLT N7, and SRF-JRMC's wartime-readiness cell, and identify the active contractor incumbents through SAM.gov solicitation history and USAspending recipient data targeting MSEL, JExD, exercise-planning, and decision-support task orders at these commands. The disconfirming-evidence questions in §2 already include items that test this layer; the next find_sources pass against fleet-command exercise-planning queries should produce ingestable evidence.

### 5.4 Navy professional-services incumbents at the corrected-scope customer — right customer, wrong vehicle

CNRMC procures contractor-supplied professional support services from Invictus Associates as established at §3.5. The parent vehicle (SeaPort-NxG Multiple-Award IDC, PIID N0017819D7883) hosts other primes that compete for similar PSS task orders at CNRMC and its subordinate RMCs.

**FACT:** Invictus Associates LLC holds the Navy delivery order PIID N0016424F3006 against parent IDC N0017819D7883 for Professional Support Services — Fleet Readiness Support for CNRMC, subordinate RMCs, and Surface Team One; total obligation $19,384,385; Norfolk, VA place of performance; Department of the Navy funder [s.2026-05-26-professional-support-services-].

**Assessment.** The SeaPort-NxG IDC has hundreds of prime contractors at multiple unrestricted and small-business pools. The relevant competitive set for §5.4 is the subset of SeaPort-NxG primes that hold delivery orders at CNRMC, the RMCs, or Surface Team One specifically. That subset is not yet enumerated in vault content. The PSS category as established at §3.5 is the wrong color of money for the corrected-scope product; Invictus and the broader PSS-at-CNRMC incumbents are therefore evidence of contractor access to the customer organization, not direct competition for the corrected-scope sub-product. The §11.1 engagement-surface inventory should map the SeaPort-NxG / CNRMC overlap as a potential subcontracting or partnering path if CACI's entry to CNRMC is not through a direct prime relationship.

### 5.5 Carderock-adjacent technical services contractors — environmental context

The 2026-05-26 USAspending re-ranking pass surfaced significant Navy contractor footprint at NSWC Carderock under the prior research framing. Under the corrected scope, Carderock is NOT a customer for the operational-decision-scenario product; these contracts are environmental context for the Navy contractor landscape, not direct competition.

**FACT:** Significant Carderock-keyword contracts surfaced in the 2026-05-26 USAspending re-ranking include Science Applications International Corporation (SAIC) at $50.9 million, ManTech Advanced Systems International at $45.6 million for submarine and surface ship acoustic signature trials, Leidos Inc. at $41.4 million for signature training systems development, Noblis MSD LLC at $39 million for Carderock engineering services, and American Systems Corporation at $33 million for NSWCCD Code 70 scientific, engineering, and programmatic support [USAspending re-ranking results in `_red-teams/2026-05-25-find_sources-diagnostic-output.md`; individual source files in `01_sources/` per the 2026-05-26 batch ingest].

**Assessment.** SAIC, ManTech, and Leidos are operator-allowlisted (per `_entity-allowlist.yaml`) as canonical naval-services incumbents. Their Carderock contract footprint confirms their Navy-services access but does NOT establish direct competition for the corrected-scope sub-product. Under the 2026-05-26 scope correction, Carderock is the source for survivability modeling that may feed scenario content, not a customer for the scenario content itself. These incumbents are tracked here as environmental context; their conversion to direct competitive threat under the corrected scope depends on their identifying the same fleet-command exercise-planning procurement pathway §5.3 names and pivoting capability into it.

### 5.6 Material from the prior §5 framing — moved to context-only

The new-construction shipbuilder set (HII, General Dynamics NASSCO, Electric Boat, Bollinger, Fincantieri Marinette Marine, Austal USA) and the U.S.-Japan partnership thread (Japan Maritime United, the Stimson MSMRO Task Force, the July 2025 U.S.-Japan trade arrangement) were load-bearing under the prior NAVSEA / industrial-base framing of §5. Under the 2026-05-26 corrected scope they are context-level for the broader Navy environment, not load-bearing for the corrected-scope product's competitive picture. Material is preserved in git history and in the 2026-05-25 corpus-cleanup dialogue. The Platform-Sustainment Bundling Hypothesis vs. NAWCTSD Training-Prime Hypothesis framing from the 2026-05-25 corpus cleanup is itself superseded by the 2026-05-26 correction — neither hypothesis frames the corrected-scope competitive picture; §5.3 (fleet-command exercise-planning incumbents) is the load-bearing layer.

### 5.7 Assessment of the competitive landscape under the corrected scope

The competitive picture under the corrected scope is layered, with one heavyweight CACI-favorable signal (§5.1: CACI NSS LLC at AFRICOM is the dominant cross-customer incumbent for the work-type), one large adjacent-but-not-direct-competition incumbent base (§5.2: the nine NAWCTSD primes), one critical research gap that is operator-validated but not yet source-grounded (§5.3: fleet-command exercise-planning incumbents at FLTFORCOM, COMPACFLT, SRF-JRMC), and one customer-access incumbent base that does not directly compete on the work-type (§5.4: Invictus and other PSS-at-CNRMC primes on SeaPort-NxG).

The §7 working hypothesis carries this forward as the central competitive uncertainty: the fleet-command exercise-planning incumbent base is real but opaque to public sources, and the disconfirming-evidence question is whether that base is large enough and capable enough to crowd out a CACI entry into the corrected-scope sub-product, or sparse enough that a CACI offering establishes a meaningful first-mover position. The §11.1 engagement-surface inventory and the next find_sources pass against fleet-command-exercise-planning queries are the load-bearing research tasks to resolve this question.

<!-- /sensitivity -->

<!-- ship: 2026-05-26 claude-opus-4-7 -->
<!-- small-ship: §5 sealed under the small-ships-workflow alongside §§4, 6, 7 as a multi-section ship. -->


## 6. Our fit — CACI right-to-win under the corrected scope

<!-- sensitivity:internal -->

This section assesses CACI's right to win on the corrected-scope product (gamified operational-decision scenarios for BDAR / BDAT teams at Navy repair activities, with a 1-hour turn-based decision-rehearsal sub-product as the differentiated wedge per §3.7). Under the corrected scope, the right-to-win story rests on three pillars — an existing federal contract footprint in the exact work-type at multi-hundred-million-dollar scale (§6.1), an applied capability lineage that translates down-vertical from a sister combatant command to the Navy repair-activity domain (§6.2), and a sensor / signature-library differentiator from the 2026 ARKA acquisition that maps directly onto BDAR scenario realism (§6.3). The fit assessment closes with the OCI and contact-protection considerations that the recommendation has to navigate (§6.4).

### 6.1 Existing CACI federal-vehicle footprint and the AFRICOM task-order precedent

CACI's right to win on the corrected-scope sub-product is grounded in two related facts. First, CACI is already executing exercise-design and operations-support work at multi-hundred-million-dollar scale at a sister Combatant Command. Second, CACI already holds the governmentwide contracting vehicles a Navy fleet command can issue task orders against — without setting up a new Navy-specific contract.

**FACT:** CACI NSS, LLC is a CACI subsidiary that holds multiple federal contracting vehicles, including GSA OASIS, NITAAC CIO-SP3, and GSA Multiple Award Schedule (GS-35F-349CA). These are governmentwide acquisition contracts open to any federal customer.

**FACT:** CACI NSS, LLC holds task order PIID 47QFCA20F0042 against parent IDC GS00Q14OADU121 (an OASIS-equivalent GSA governmentwide vehicle) for *"Plans, Operations, Logistics, Engagement, Training, Exercise, and Assessment Support to AFRICOM"* — total obligation $194,034,792, Department of the Army funder via GSA Federal Acquisition Service [s.2026-05-26-the-purpose-of-this-award-is-t].

**FACT:** The AFRICOM task order scope covers the full work-type stack named in the corrected-scope product description: plans, operations, logistics, engagement, training, exercise, and assessment support [s.2026-05-26-the-purpose-of-this-award-is-t].

**Assessment.** This pair of facts reshapes the procurement-pathway story for the recommendation. The AFRICOM task order demonstrates that CACI has been executing the corrected-scope work-type at multi-hundred-million-dollar scale to a Combatant Command customer since 2020. The CACI NSS, LLC vehicle holdings demonstrate that the contracting infrastructure CACI needs to compete for similar Navy work already exists. The Navy fleet commands (FLTFORCOM, COMPACFLT, INDOPACOM J7) and Navy SYSCOM authorities (NAVSEA 04, PEO IWS / equivalent) can issue task orders against CACI NSS, LLC's existing OASIS, CIO-SP3, or GSA MAS holdings. The procurement-pathway question is therefore narrower than the prior §3.6 framing implied. The Navy does not need to invent a new vehicle. The Navy needs to be convinced to issue a task order against a vehicle CACI already holds. That is a sharper procurement story and a faster path than building a new vehicle from scratch.

The salesmanship implication: a CACI executive walking into a meeting with PACFLT N7 or FLTFORCOM N7 can offer a concrete contracting path on day one. "Here is the work-type. Here is the AFRICOM precedent. Here are the GSA-wide vehicles we already hold. Issue a Level 1 pilot task order against our OASIS or CIO-SP3 holdings. Customer commits no new procurement infrastructure." That is a materially easier pitch than asking the customer to fund a new contract vehicle.

### 6.2 Applied capability lineage — PMTEC exercise-design translation

CACI's known capability lineage in the exercise-design / operational-decision-scenario space is the INDOPACOM Pacific Multi-Domain Training and Experimentation Capability (PMTEC) work tracked in the parallel `PMTEC-USINDOPACOM` opportunity in this vault.

**Assessment.** The PMTEC opportunity research (cross-reference `opportunities/PMTEC-USINDOPACOM/00_research-file.md`) documents the USINDOPACOM J7 multi-domain exercise-design ecosystem in which CACI is an active engaged participant. The capabilities being developed and demonstrated under PMTEC — Live-Virtual-Constructive integration, scenario design for multi-domain decision-making, AI and digital-twin technologies, and Regional Joint Training Infrastructure — are directly transferable down-vertical to the naval-repair domain. The corrected-scope sub-product (1-hour turn-based gamified decision rehearsal for repair-activity team leaders) is a focused sub-application of the broader multi-domain exercise-design capability CACI demonstrates under PMTEC. The right-to-win argument is that CACI does not have to build a new capability for the corrected-scope product — it has to translate an existing capability to a tighter vertical (naval repair activities) and a smaller delivery format (short-form decision-tier sessions inside fleet exercise rhythm).

### 6.3 ARKA acquisition — threat-environment realism, not repair-side realism

The March 2026 ARKA acquisition gives CACI a sensor-signature library asset that is relevant to ONE side of operational-decision-scenario realism — the threat / attack-vector side — but not the other side, which is the Hull, Mechanical, and Electrical (HM&E) engineering and logistics data that drives repair-side realism. This distinction matters for the right-to-win story and is rebuilt here from a 2026-05-26 Gemini Pro red-team correction.

**Assessment (cross-opportunity carry-over from `_meta/glossary.md`).** ARKA is the defense subsidiary CACI acquired in early 2026 for approximately $2.6 billion net of cash, closed 9 March 2026. ARKA brings electro-optical, infrared, and hyperspectral sensor signature libraries derived from intelligence, surveillance, and reconnaissance (ISR) and space-domain work. For the corrected-scope product, signature-library content drives scenario realism on the **threat / attack-vector side** of an operational-decision rehearsal — what a damaged ship's sensors would actually report under specific damage profiles, what threat indicators the team would see in the moments after a hit, what the operational picture looks like when the ship is steaming with degraded sensors. ARKA does NOT directly drive **repair-side** scenario realism — pump-out status, bulkhead compromise, drydock blocking availability, supply-chain routing for replacement valves, MFOM (Material Financial Operations Management) or NMD (Navy Maintenance Database) data. Repair-side realism requires a bridge to NAVSEA / SYSCOM technical-authority data, ship-class engineering documents, or HM&E databases that CACI must source separately — through partnering with an HM&E-data-holding prime, through CACI's own naval-IT footprint, or through Government Furnished Information (GFI) negotiated as part of any contract that procures the sub-product.

The hypothesis under §11.3 is that ARKA-released signature-library content is a near-unique threat-side differentiator versus the canonical naval-services incumbents (SAIC, Leidos, HII Mission Technologies), and that the repair-side realism gap is closeable through a teaming or GFI arrangement. That is a hypothesis to test, not a finding — ARKA's intellectual-property and release-authority constraints on the signature libraries are open research, and the HM&E-data bridge approach is operator-side scoping work that does not enter the vault directly.

### 6.4 OCI and contact-protection considerations

The corrected scope and the operator's research-origin context together raise specific Organizational Conflict of Interest (OCI) and contact-protection considerations under FAR 9.5 (per `_meta/oci-primer.md`) and the §9.3 contact-protection discipline.

**Assessment (operator-owned per the gray-box model).** The operator has direct knowledge of contractor exercise planners at SRF-JRMC's wartime readiness group, including awareness of a specific individual's existence and role. Per §9.3, that channel does not enter the vault as a citable claim; per the OCI primer, the awareness itself may trigger OCI analysis under FAR 9.5 depending on whether CACI's competitive position would unfairly advantage from the operator's knowledge. The OCI analysis is operator-owned per the gray-box model and is documented separately from this research file. For the purposes of §6 fit assessment, the §9.3 discipline keeps any operator-side knowledge from contaminating analytical content; the recommendation in §7 will name only OSI-sourced claims as load-bearing, and any operator-side direction informs which OSI sources to pursue without entering the recommendation chain directly.

### 6.5 Assessment of CACI's right to win

The right-to-win story under the corrected scope is multi-pillar but coherent. CACI has the work-type at scale via NSS LLC at AFRICOM. CACI has the applied capability lineage via the PMTEC INDOPACOM work. CACI has the signature-library differentiator via the 2026 ARKA acquisition. The Navy customer is identifying itself publicly via SWARMEX-Cebu and the FLTFORCOM Global Maritime Response Plan development. The DoD procurement pattern for the work-type is established at the Joint, Marine Corps, AFRICOM, OSD, and MDA levels. What §6 does NOT establish — and what §7 (working hypothesis) carries forward as the load-bearing uncertainty — is the specific Navy fleet-command contracting vehicle under which the corrected-scope sub-product would be procured, and whether the existing fleet-command exercise-planning contractor base (§5.3 research gap) is crowded enough to require partnering or sparse enough to allow a CACI prime entry.

The right-to-win confidence under the corrected scope is materially higher than under the prior schoolhouse / NAWCTSD-pipeline framing it superseded. The prior framing positioned CACI as a new entrant fighting through an established training-systems pipeline; the corrected framing positions CACI as a capability-lineage holder translating existing capability down-vertical to a tighter Navy customer set. The §11.1 engagement-surface inventory and the next find_sources pass will resolve the remaining procurement-vehicle uncertainty.

<!-- /sensitivity -->

<!-- ship: 2026-05-26 claude-opus-4-7 -->
<!-- small-ship: §6 sealed under the small-ships-workflow alongside §§4, 5, 7 as a multi-section ship. -->

<!-- /sensitivity -->

## 7. Working hypothesis — rebuilt under the corrected scope

<!-- sensitivity:internal -->

This is the analyst's current best assessment of what the research will show under the 2026-05-26 corrected scope. It is a **hypothesis**, not a finding — flagged as Assessment, not FACT. It is here so the rest of the file has a target to test against. The research plan in §10 is deliberately designed to try to break this hypothesis; whatever survives that effort gets promoted to a recommendation. The hypothesis was refocused on 2026-05-24 (BDAR/BDAT tightening), refined on 2026-05-25 (right-to-win-reframe dialogue), and rebuilt on 2026-05-26 under the corrected scope (operational-decision-scenario product for repair-activity teams, not schoolhouse curriculum). The prior framings are preserved in git history and in the decision log entries for those dates.

**The hypothesis in one paragraph (corrected-scope version):**

The Navy has a real and publicly-signaled demand for contractor-supplied operational-decision-scenario content for its Battle Damage Assessment and Repair (BDAR) team at Navy repair activities — the four public naval shipyards, the Regional Maintenance Centers, the forward-deployed Ship Repair Facility–Japan Regional Maintenance Center, and the wartime-readiness cells that support them. The specific corrected-scope sub-product is a 1-hour turn-based gamified decision-rehearsal session for staff-cell or wardroom audiences, executed inside the rhythm of fleet exercise events rather than as a standalone training pipeline. CACI's right to win on this sub-product is grounded in three pillars — the existing NSS LLC contract at AFRICOM that demonstrates the work-type at multi-hundred-million-dollar scale, the applied PMTEC capability lineage that translates down-vertical to the naval-repair domain, and the 2026 ARKA acquisition signature libraries that map onto BDAR scenario realism. The most-likely procurement-pathway is at the fleet-command exercise-authority layer (FLTFORCOM, COMPACFLT, INDOPACOM J7) or direct SRF-JRMC wartime-readiness procurement, rather than at the NAWCTSD training-systems pipeline or CNRMC professional-services-on-SeaPort-NxG that adjacent §5 layers occupy.

**Why this is still a hypothesis and not a recommendation:**

Acting on this would mean CACI investing in capture work, possibly hiring or partnering, and committing capital. Before any of that happens, the hypothesis has to survive a deliberate effort to disconfirm it. The §10 research plan and the §11.1 engagement-surface inventory are the load-bearing investigations that have to complete before the hypothesis is upgraded to a FACT-supported recommendation.

**The six things that could falsify this hypothesis under the corrected scope:**

The hypothesis breaks into six separate claims. If any one of them fails, the corresponding part of the hypothesis is dead and the recommendation shape has to change. These legs are rebuilt from the 2026-05-24 BDAR/BDAT-tightened legs and the 2026-05-25 corpus-cleanup refinements to reflect the 2026-05-26 corrected scope.

1. **The Navy operational-decision-scenario demand gap.** *Claim:* the Navy has a real and acknowledged gap in operational-decision-scenario content for the BDAR / BDAT team at repair activities, visible in senior-leadership signals (Caudle HASC testimony emphasizing maintenance as a warfighting requirement; DON FY27 Press Brief funding ship maintenance at $17.0B to drive 80% Combat Surge Ready posture) and in publicly-executed exercise artifacts (SWARMEX-Cebu rehearsing forward-port wartime repair with host-nation contractor coordination). *What kills it:* the senior-leadership signals are ceremonial or marketing rather than capability-building signals AND a closer reading shows the Navy's existing fleet-exercise rhythm (COMPTUEX, RIMPAC, Large-Scale Exercise, SWARMEX) already injects operational-decision-scenario content via organic Navy staff or existing contractors at a depth that closes the gap. Strongest counter-evidence: a fleet-command training-readiness instruction or AAR (after-action report) that documents existing scenario-design coverage for the corrected-scope sub-product.

2. **The sub-product moat — gamified-software engine vs. analog tabletop.** *Claim:* the corrected-scope sub-product's defensible moat is the gamified-software engine and automated scenario-generation capability (tying back to the FY27 comptroller justification book AI-powered scenario-generation funding line), not the 1-hour duration alone. Fleet-command exercise planners do already inject 1-hour Tabletop Exercises (TTXs) and localized drill modules into the Fleet Response Plan — the duration alone is not a defensible differentiator. *What kills it:* (a) incumbents replicate the gamified-software form factor using lightweight analog TTXs and neutralize the gamification advantage, OR (b) the AI scenario-generation capability matures rapidly enough among incumbents (via the FY27 comptroller-funded JExD scenario-generation work) that CACI's PMTEC-leveraged head start does not translate to a moat by the time the corrected-scope sub-product reaches procurement. Strongest counter-evidence: a FY27 or FY28 SAM.gov solicitation that procures gamified scenario generation at the fleet-command level with an incumbent prime already developing the AI scenario-generation engine.

3. **CACI capability transferability — PMTEC to naval-repair.** *Claim:* the exercise-design capability CACI demonstrates under the PMTEC INDOPACOM J7 work transfers down-vertical to the naval-repair domain at the sub-product fidelity required. *What kills it:* the PMTEC exercise-design work is structurally different from naval-repair operational-decision rehearsal in ways that prevent direct capability transfer — for instance, PMTEC operates at multi-domain Combatant Command staff levels where naval-repair operational decisions are made at smaller staff-cell scales with different decision-tier audiences, different time pressures, and different fidelity expectations. The capability does not transfer cleanly; CACI would need to rebuild rather than translate. Strongest counter-evidence: a PMTEC after-action report or capability description that documents the multi-domain Combatant Command focus as distinct from small-unit decision-rehearsal scale.

4. **ARKA signature-library differentiator viability — threat-side only, plus the repair-side bridge.** *Claim:* CACI's ARKA-acquired electro-optical, infrared, and hyperspectral sensor signature libraries can be released for training use and drive **threat-environment scenario realism** for BDAR / BDAT decision rehearsal in ways the canonical naval-services incumbents (SAIC, Leidos, HII Mission Technologies) cannot match. ARKA does NOT directly drive **repair-side scenario realism** (HM&E, logistics, drydock blocking, replacement-valve supply chain) — that requires a bridge to NAVSEA / SYSCOM technical-authority data, ship-class engineering documents, or HM&E databases (MFOM, NMD) via partnering, CACI naval-IT footprint, or Government Furnished Information (GFI) arrangement. *What kills it:* (a) ARKA's intellectual-property posture prevents release of signature libraries to a training context, OR (b) the signature-library content is not in fact distinctive — comparable signature data is available to the canonical incumbents through other means, OR (c) the HM&E-data bridge cannot be closed — no teaming partner, no GFI, no internal naval-IT data — leaving CACI with a threat-side-only differentiator that is insufficient for a credible BDAR scenario portfolio, OR (d) the bureaucratic friction of securing GFI / Authority to Operate (ATO) for Navy maintenance systems of record (Material Financial Operations Management, Navy Maintenance Database) for a gamified non-system-of-record environment introduces a 12-18 month schedule delay that effectively neutralizes the PMTEC-leveraged head start before procurement. *Scope note:* this leg was rebuilt 2026-05-26 from the Gemini Pro red-team correction noting that ARKA's ISR/EO/IR signature work is fundamentally distinct from the HM&E / industrial-logistics realism that drives the repair side of BDAR. The OCI and intellectual-property analyses for the ARKA-signature-release path are owned by the operator per §9.3 and the gray-box model and do not enter this leg's falsifier reasoning at the vault analytical level.

5. **Customer-access pathway feasibility.** *Claim:* CACI can build or expand the relationships needed to execute the corrected-scope sub-product bid via one of the §4 customer-set candidates — most likely SRF-JRMC's wartime readiness cell, FLTFORCOM N7, COMPACFLT N7, or a CNRMC follow-on task order — on a timeline shorter than the customer demand window. *What kills it:* the relevant customer organizations have their engagement bandwidth locked up by existing fleet-command exercise-planning incumbents (the §5.3 research-gap layer) to a degree that CACI's entry timeline runs past the demand window, or the existing incumbents have a contractual right-of-first-refusal that prevents new-entrant access. *Note:* per §9.3 and `_meta/oci-primer.md`, operator-side knowledge about CACI's current contract footprint at any Navy organization is operator-side context and does not enter this leg's falsifier reasoning. The leg is framed at the general competitive level.

6. **Sub-product viability — 1-hour decision rehearsal as a fundable line.** *Claim:* the specific corrected-scope sub-product (1-hour turn-based gamified decision-rehearsal for staff-cell / wardroom audiences inside fleet exercise rhythm) is a coherent, fundable procurement line — there exists a procurement vehicle that can buy it at a meaningful per-engagement scale and a customer organization that can authorize that vehicle. *What kills it:* (a) the sub-product is too small to be a standalone procurement line and only exists as an embedded element of multi-day exercise-design contracts, in which case the recommendation is to partner with a fleet-command-exercise-planning incumbent rather than prime; or (b) the sub-product is too specialized to attract a procurement vehicle at all, in which case the recommendation is to fund a pilot through SBIR / STTR / DIU mechanisms before pursuing a traditional contract. Strongest counter-evidence: a SAM.gov pattern showing fleet-command exercise contracts at the procurement-line level either always bundle larger or always exclude the corrected-scope sub-product.

**Recommendation (draft, contingent on §10 disconfirming-evidence resolution and §11.1 engagement-surface inventory):**

Position CACI as a candidate prime for the five-level progression documented at §11.3, with the analog Levels 1 through 3 as the initial entry product and Levels 4 and 5 as follow-on scale. The two-layer customer-procurement model holds: **SRF-JRMC as the most-likely end-user / sponsor**, with **PACFLT N7 / N4 or FLTFORCOM N7 / N4 as the most-likely contracting authority**. The procurement path is sharper than the prior framing implied. The Navy does NOT need to invent a new contracting vehicle. CACI NSS, LLC already holds GSA OASIS, NITAAC CIO-SP3, and GSA Multiple Award Schedule. Any Navy fleet command or SYSCOM authority can issue a task order against those vehicles directly. The CACI NSS, LLC AFRICOM task order ($194M against parent IDC GS00Q14OADU121) is the precedent — Army funds, GSA awards, vehicle CACI already holds. The Navy equivalent is "PACFLT N7 funds, GSA awards, vehicle CACI already holds." Same shape, different funder.

The pitch from CACI to the Navy customer is concrete on day one. Here is the work-type. Here is the AFRICOM precedent demonstrating CACI executes this work at scale. Here are the GSA-wide vehicles we already hold. Issue a Level 1 pilot task order against our OASIS or CIO-SP3 holdings. The customer commits no new procurement infrastructure. This is the salesmanship step §11.3.7 describes — CACI executives have to make this pitch in person to PACFLT N7, FLTFORCOM N7, INDOPACOM J7, NAVSEA 04, or SRF-JRMC leadership. The Navy is not running an RFP for this today.

Capability differentiators: the PMTEC INDOPACOM J7 work is the applied lineage for the exercise-design capability translated down-vertical. The ARKA acquisition signature libraries are the threat-environment differentiator; the repair-side realism gap (HM&E, logistics, drydock data) needs a bridge through partnering with an HM&E-data-holding prime, leveraging CACI's existing naval-IT footprint, or negotiating Government Furnished Information as part of the task order. The dual-audience design means the same scenario content serves both the repair-activity wardroom and the fleet commander making the port-selection call.

Alternative entry path if the direct task-order pitch does not produce procurement inside the planning horizon: DIU, SBIR, or STTR pilot for Level 1 or Level 2 scope at smaller per-engagement scale, producing reference customers for follow-on task-order competition.

The recommendation shape will be reassessed after (a) the next find_sources pass against fleet-command-exercise-planning queries completes and produces source-grounded incumbent identification at the §5.3 layer, (b) the §11.1 engagement-surface inventory maps the specific contracting offices and active solicitations at FLTFORCOM N7 / N4, PACFLT N7 / N4, SRF-JRMC, and the relevant SYSCOM authorities (NAVSEA 04, PEO IWS / equivalent), and (c) the operator's OCI analysis closes per the FAR 9.5 procedure documented in `_meta/oci-primer.md`. The HM&E-data bridge approach is operator-side scoping work that runs parallel to but outside the vault analytical chain per §9.3.

<!-- /sensitivity -->

<!-- ship: 2026-05-26 claude-opus-4-7 -->
<!-- small-ship: §7 sealed under the small-ships-workflow alongside §§4, 5, 6 as a multi-section ship. Gemini Pro Round 2 CONDITIONAL-GO, micro-fix on Leg 4 (GFI/ATO schedule risk) applied. -->


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
- [s.2026-05-26-navy-selects-nine-contractors-1-2b] https://www.govconwire.com/articles/navy-nine-contractors-training-system  →  `01_sources/2026-05-26_govconwire-com_navy-selects-nine-contractors-1-2b-training-system-mod.md`
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

### 11.3 BDAT and BDAR training pipeline — five-level analog-first progression under the corrected scope

This section was rewritten on 2026-05-26 to replace the prior two-phase model. The corrected-scope product is not a single 1-hour gamified session by itself. It is a five-level progression that builds wardroom and staff-cell decision-making skills over time. The progression starts analog and small. It builds toward software-driven scenarios injected into live fleet exercises. The reason it starts analog is straightforward. Analog has lower technical risk. Analog iterates faster on content. Analog proves the concept with the customer before CACI commits to the game-engine investment. The AI scenario engine pays for itself starting at Level 4 when the customer commits to scale. Before that, analog beats software.

The audience for the progression is the wardroom and staff cell at a Navy repair activity. That means the commanding officer, executive officer, department heads, training officer, and visiting fleet liaisons at a public naval shipyard, a Regional Maintenance Center, or the forward-deployed Ship Repair Facility Japan. It does not mean individual Sailors learning damage-control hand skills. The 2026-05-26 scope correction is binding.

The progression covers both sides of the work. The assessment team learns what to look for and how to classify damage. The repair team learns how to translate the assessment into a triage plan, mobilize forward, contract local, and execute under combat tempo. The two sides have separate audiences but the same scenario base. Each level can run for either audience independently or for both audiences in a coordinated session.

#### 11.3.1 Level 1 — flash drills

Five to fifteen minutes. One decision per drill. Printed scenario card or single tabletop sheet. The wardroom picks an answer and defends it in 60 seconds.

Example. A destroyer takes shock damage 800 miles from three friendly ports. Each port has different repair capability, different security posture, and different host-nation contracting friction. Here are the five variables. Pick the port. Defend the choice.

The goal is pattern recognition. The wardroom builds an instinct for which variables actually matter and which are noise. The cost per drill is near zero. The Navy customer can run 20 drills in a month at no marginal cost beyond a moderator. This is the cheapest level to procure and the easiest entry point to sell to a first customer.

#### 11.3.2 Level 2 — linked-decision sequences

Thirty to forty-five minutes. Three to five decisions in a row. Each decision changes the next one.

Example. Port chosen in decision one. Now stage the forward repair team. Now hire local welders under the Acquisition and Cross-Servicing Agreement. Now handle host-nation customs paperwork for the replacement valves. Each decision narrows the options for the next.

The goal is awareness that early decisions box you in later. This is the cognitive skill the corrected-scope product is trying to build. The wardroom learns that the port-selection call has downstream consequences for the contracting environment, the legal environment, and the security environment. A short-sighted port choice in decision one creates an unsolvable problem in decision four.

Delivery is still analog. A moderator runs the session with printed scenario inserts and a simple decision-tracking sheet. Software helps but is not required.

#### 11.3.3 Level 3 — full one-hour gamified wardroom session

This is the sub-product the brief has been calling the differentiated wedge. Full scenario. Multi-disciplinary audience. Turn-based gamification. Still analog or analog-plus-software-aid.

The scenario covers all six operational-decision moments from §1 in one integrated session. Port selection, forward team mobilization, foreign-port emergency contracting, BDAR triage under combat tempo, BDAT-to-BDAR handoff, and information-resource access in degraded comms. The wardroom plays the scenario as a team with a moderator running the clock and injecting events.

The goal is to integrate decisions across all six moments under time pressure. The 60-minute time box matches the realistic decision window in an actual damage event. The wardroom finishes the session having played through a complete decision sequence in real time.

This level is where the procurement vehicle question gets pointed. A 1-hour session inside a fleet exercise event runs against a different vehicle than a multi-day exercise contract. The recommendation in §7 targets PACFLT or FLTFORCOM N7/N4 as the contracting authority for this level.

#### 11.3.4 Level 4 — multi-session campaign exercise

Two to four hours of total play, broken into multiple sessions over a deployment cycle. Decisions from session one carry into session two. The campaign simulates a six-month deployment with multiple damage events.

This is where the AI scenario engine starts to pay for itself. Each participating wardroom needs a different variant because their decision history is different. The Joint Exercise Design workforce and AI scenario generation funding in the FY27 comptroller justification book funds exactly this kind of capability for joint exercises. The Navy fleet-command equivalent is what the next find_sources pass is trying to find.

The goal at this level is consequence reasoning and leadership continuity. The wardroom builds memory of how its own prior choices shaped its current situation. This is the cognitive skill that traditional one-off exercises cannot build because they reset between events.

#### 11.3.5 Level 5 — live exercise injection

Scenarios injected into actual fleet exercises. COMPTUEX. RIMPAC. Large-Scale Exercise. SWARMEX. Software-driven so the scenario reacts to live exercise events in real time.

This is the endgame product. The customer is the fleet-command training authority that owns the parent exercise. The Navy professional society community sees the value at this level because the scenario content shows up in after-action reports and lessons-learned documents.

Level 5 is the natural follow-on once Levels 1 through 4 have established CACI as a known scenario-content provider. It is also the highest-margin level because the scenario IP, the software engine, and the customer relationship all carry forward from earlier levels.

#### 11.3.6 Analog-first scaling — when software pays for itself

The five-level progression is designed to start analog and graduate to software at the point where the customer commits to scale. The decision points are:

- Levels 1 and 2 should never be software-first. The customer learning curve is in the scenario content, not the delivery technology.
- Level 3 can be analog or hybrid. The choice depends on how many simultaneous sessions the customer wants to run. One wardroom at a time, analog wins. Five wardrooms at a time, hybrid starts to make sense.
- Level 4 needs software. Variant generation across multiple participating wardrooms is the breakpoint. The AI scenario generation funding line in the FY27 comptroller book is the procurement signal for this level at the Joint Staff side.
- Level 5 needs software. The live exercise event runs on Navy synthetic training architecture and the scenario content has to federate into it. This is where the LVC scope note from the 2026-05-25 corpus cleanup applies — Navy Continuous Training Environment compatibility is the customer requirement at this level, not generic commercial gaming tech.

The capture strategy follows the same shape. Start with a small Level-1 or Level-2 pilot at one Navy customer site. Prove the analog version works. Iterate on scenario content with the customer in the room. Use the analog success to justify the Level-3 contract. Use the Level-3 reference to justify the Level-4 software investment. Use the Level-4 capability to compete for the Level-5 fleet-exercise injection follow-on.

This is what the brief means by "subcontractor first, prime contingent on a new vehicle or pilot maturation." The pilot path runs through Levels 1 through 3 at analog and small scale. The prime path runs through Levels 4 and 5 at software and fleet-exercise scale.

#### 11.3.7 Why the Navy will likely have to be sold this, not just pitched it

A practical note on the recommendation. The sources prove the Navy has a problem with wartime repair readiness. The sources prove the rest of the Defense Department buys exercise design and scenario content from contractors at multi-hundred-million-dollar scale. The sources do not yet prove a Navy fleet-command procurement vehicle exists today for the specific corrected-scope sub-product. The next find_sources pass is trying to find one.

The honest read is that this is a hypothesis. The Navy probably does need this. The Defense Department definitely buys this kind of work from contractors. So the Navy should buy this kind of work too. But "should" is not "is procuring." There is a salesmanship step between the hypothesis and the procurement.

That step is real BD work, not desk research. CACI executives have to pitch the concept to PACFLT N7, FLTFORCOM N7, INDOPACOM J7, or SRF-JRMC leadership directly. They have to show the value of the analog Level 1 and Level 2 starting point. They have to make the case for why this fits inside the fleet-exercise rhythm rather than competing with it. The relationship-development work in §11.1 has to set up those meetings. The OCI analysis in §6.4 has to be closed before the meetings happen. The capture brief itself is one of the artifacts the BD team brings to those meetings.

This is a capture strategy that requires CACI to lead the customer, not wait for the customer to lead CACI. That is operator-owned to execute. The research file documents the hypothesis, the candidate customer set, and the recommended progression. The execution is on the BD team and CACI executive leadership.

#### 11.3.8 Material from the prior two-phase framing — preserved for lineage

This subsection holds the prior framing of §11.3 that was written under the 2026-05-21 scope-expansion-#2 scaffolding and updated through the 2026-05-25 corpus cleanup. The prior framing had a two-phase model: Phase 1 high-frequency gamified practice between live exercises; Phase 2 real-world exercises that the simulation layer cannot replace. The phase content is preserved in git history. Specific elements that carry forward into the new five-level model:

- The Phase-1 candidate gamification mechanics (scenario branching, scoring with after-action replay, leaderboards across cohorts, replay archives feeding NWDC doctrine-update loops) map directly into Level 4 of the new model where the AI scenario engine pays for itself.
- The Phase-2 modalities (embedded damage-assessment injects in fleet exercises, Carderock-instrumented controlled events, joint red-team / blue-team evolutions) map directly into Level 5 of the new model.
- The audience scoping (ship-level damage-control teams, fleet-level damage-assessment cells, joint Combatant Command staff) maps into the wardroom and staff-cell audience set the corrected-scope product addresses, with the deck-plate damage-control tier explicitly excluded per the 2026-05-26 scope correction.
- The ARKA differentiator hook from the prior framing is now decomposed in §6.3 into threat-side realism (ARKA) and repair-side realism (HM&E bridge needed separately).
- The three "ways this whole subsection could be wrong" map onto §7 falsifying legs 1, 2, and 6 under the corrected scope.

The full prior text is in git history and in `_red-teams/2026-05-25-gemini-pro-corpus-cleanup-dialogue.md`. The new five-level model in §11.3.1 through §11.3.7 is the load-bearing version for the recommendation and the briefs.

<!-- ship: 2026-05-26 claude-opus-4-7 — five-level progression added per operator's 2026-05-26 brainstorm. Replaces the prior two-phase framing as load-bearing content; prior framing preserved at §11.3.8 for lineage. -->

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

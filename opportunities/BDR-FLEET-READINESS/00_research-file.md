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
> | LVC | Live, virtual, constructive — a category of military simulation training that mixes real units, simulator pilots, and computer-generated forces. |
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

This is a research track, not yet a named capture opportunity. The scope was tightened on 2026-05-24 to focus specifically on **Battle Damage Assessment and Repair (BDAR)** and **Battle Damage Assessment Team (BDAT) training, simulation, and exercises**. Earlier framing under the broader "BDR" umbrella included industrial-base, shipbuilding-capacity, and ship-repair contracting threads that have been narrowed out of scope; those threads remain in this file as background context but are no longer load-bearing for the research direction.

The question we are trying to answer, using only publicly-available material, is whether the Navy's evolving BDAR / BDAT training requirement — visible most clearly in NAVSEA's SWARMEX exercise series and in the CNO's May 2026 testimony about Shore Intermediate Maintenance Activities (SIMA) standing up in Norfolk and San Diego — represents a real business opportunity for CACI in the **training, simulation, and exercises** space.

There are four threads inside that question, and the research has to address all four before any recommendation makes sense:

1. **Is there a real BDAR/BDAT training-and-simulation gap that the Navy is publicly signaling?** The most direct primary-source language so far is CNO Caudle's HASC testimony about the SIMA stand-up explicitly featuring "hands-on training in advanced ship repair" with AI/ML, advanced manufacturing, workflow monitoring, and robotic systems, plus the SRF-JRMC SWARMEX press release framing the program as Forward Deployed Ship Repair Teams (FDSRT) training in battle damage assessment and repair. The research's job is to triangulate whether these signals add up to a procurement opportunity in BDAR/BDAT training, or whether they describe internal-organic Navy work with no contractor entry-point.

2. **What does a robust BDAR training program look like?** The working concept is a three-step progression — tabletop scenarios in a classroom, then guided site visits to actual repair facilities (including instrumented test-beds at NSWC Carderock or equivalent labs), then hands-on pilot operations. Each step is a fidelity step-up and can also be a classification step-up. This is the BDAR (repair-side) training pipeline — section 11.2 of this file.

3. **What does a robust BDAT training program look like?** Distinct from the repair-team pipeline because the audience (assessment-team personnel), the cadence (high-frequency reps between live events), and the fidelity ramp are all different. The proposal here is a gamified-software/hardware simulation layer (serious games, instrumented training rigs, AR/VR, hardware-in-the-loop benches) that keeps BDAT cohorts sharp between live exercises, transitioning to real-world exercise injects in fleet training events like COMPTUEX, RIMPAC, and Large-Scale Exercise. This is the BDAT (assessment-side) training pipeline — section 11.3 of this file.

4. **How does CACI get in the room?** Assumed at scaffold time that CACI does not currently have a working relationship with the NSWC Carderock damage-modeling team or with the Navy organizations standing up the SIMAs. A parallel work stream of the research maps out who to approach, what existing engagement on-ramps Navy labs offer (industry days, SBIR/STTR cycles, NAVSEA-hosted touchpoints), and what intro paths might exist through adjacent Navy lab relationships. The engagement strategy is section 11.

This research track was initiated based on a working observation shared by a working-level Navy ship-repair contact. Their framing informs the research direction — specifically the view that BDAR/BDAT training is an underdeveloped area worth examining. Everything in this file must be supported by public sources alone; the contact is not named here and is not the source of any factual claim. See section 9.3 for the verification discipline this implies.

**What is out of scope after the 2026-05-24 narrowing.** The broader ship-repair industrial base, the shipbuilding-capacity question, private ship-repair contractor competition, surge-repair capacity planning at scale, and the U.S.-Japan industrial partnership thread (Stimson MSMRO Task Force) are no longer load-bearing for the recommendation. They remain in sections 3, 4, and 5 of this file as context — useful for understanding the Navy environment the BDAR/BDAT opportunity sits inside — but the recommendation will be specifically about training, simulation, and exercise products and services, not about ship-repair industrial-base policy. If the research surfaces evidence that BDAR/BDAT training is being acquired through one of these broader vehicles, the relevant context-section material will get pulled forward into the recommendation.

This summary states the scope neutrally. The hypothesis in section 7 is one possible outcome of this research — not a finding. The research plan in section 10 deliberately includes evidence that would falsify the hypothesis. The engagement strategy in section 11 is sequenced so that the relationship-development work proceeds in parallel with the hypothesis-testing work.

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

## 3. Demand signal — what the customer is publicly saying about wartime ship repair

This section captures the public-record signal from the first round of source ingestion (14 sources ingested 2026-05-23 from the find_sources pass run 2026-05-21). Each claim carries a FACT or Assessment label per the SOP at `_meta/sop.md` and a citation tag pointing to a source in `01_sources/`. The claims have not yet been verified against the cited sources by `verify_facts.py` — that is the next mechanical step in the small-ships workflow.

The picture from the public record is consistent: shipbuilding and ship-repair capacity is in active senior-leadership focus across the executive branch and Congress, the funding being committed is large, and the policy-community framing of why this matters explicitly includes wartime repair under conflict conditions. This is supportive of the working hypothesis in section 7 — particularly leg 1 (the training-assumption gap) and leg 2 (the industrial-planning gap) — but does not yet close out the disconfirming-evidence questions in section 2.

### 3.1 Stated priorities

The senior-leadership and oversight signal that wartime ship repair capacity is a strategic constraint shows up across three independent threads.

**The policy community is treating forward repair capacity as a wartime-preparation question, not a peacetime-efficiency question.** The Stimson Center convened a bi-national U.S.-Japan Task Force on Military Shipbuilding, Maintenance, and Repair Operations (MSMRO) that engaged from January to March 2026 and released its recommendations on 25 March 2026 [s.2026-05-23-the-time-is-ripe-for-next-step]. **FACT.** The Task Force's policy claim on why forward repair capacity matters is framed explicitly around battle damage and conflict timing: *"Such operations can extend the number of facilities available to vessels from both countries as well as diverse and secure locations to repair battle damage when needed, recognizing that such capabilities cannot effectively be established after the outbreak of conflict"* [s.2026-05-23-the-time-is-ripe-for-next-step]. **FACT (direct quotation).**

**Senior administration engagement on the issue is visible and recent.** U.S. Secretary of the Navy John Phelan chose Japan as his first foreign trip destination, where he expressed support for Japan assuming a greater role in maintenance, repair, and overhaul for the U.S. Navy [s.2026-05-23-the-time-is-ripe-for-next-step]. **FACT.** Congress has directed the Secretary of the Navy to urgently assess ship repair improvements in U.S. territories in the Western Pacific, and the policy-community framing notes that Guam specifically lacks dry dock capability for allied-vessel major maintenance [s.2026-05-23-the-time-is-ripe-for-next-step]. **FACT.**

**Independent oversight is pointing at the same structural problem.** The Government Accountability Office testified to the House Armed Services Subcommittee on Seapower and Projection Forces and the House Transportation and Infrastructure Subcommittee on Coast Guard and Maritime Transportation on 22 April 2026 that *"Navy and Coast Guard shipbuilding programs have consistently fallen short of expectations over the last 2 decades. Collectively, they are billions of dollars over cost and years behind schedule"* [s.2026-05-23-gao-26-109068-navy-and-coast-g]. **FACT (direct quotation).** Since 2016, GAO has made 92 recommendations to the Navy and 45 to the Coast Guard on shipbuilding programs; implementation has been mixed [s.2026-05-23-gao-26-109068-navy-and-coast-g]. **FACT.** As one specific illustration, the Navy announced a strategic shift away from the Constellation class frigate program in 2025, after previously exercising contract options valued at over $3 billion [s.2026-05-23-gao-26-109068-navy-and-coast-g]. **FACT.**

**Sustainment cost growth across the Department of Defense weapon-system portfolio is a documented, accelerating problem.** In a separate April 2026 report, GAO documented that the Department of Defense identified 14 systems with critical operating and support cost growth out of 36 weapon system sustainment reviews conducted for fiscal years 2023 and 2024, where "critical" means at least a 25 percent increase compared with the most recent independent cost estimate or at least 50 percent compared with the original baseline [s.2026-05-23-gao-26-108140-weapon-system-su]. **FACT.**

**Assessment.** The four threads above are independent — administration policy direction, allied policy-community proposals, congressional direction to assess, and independent GAO oversight — and they converge on the same picture: that wartime ship repair capacity is being treated as a strategic problem in active executive and legislative attention. This convergence is what gives section 7 leg 1 (the training-assumption gap) and leg 2 (the industrial-planning gap) some prior weight. But none of these sources is a primary statement of "the Navy training pipeline understates wartime damage." That specific claim is what the rest of the research has to produce or fail to produce from public sources.

### 3.2 Funding — money flowing toward the problem

The dollar amounts being committed to shipbuilding and sustainment in the near term are large enough that the funding picture is not the constraint on this research track. The constraint is on knowing what specific buckets the money will land in and which procurement vehicles will carry the spend.

**Department of Defense and Coast Guard shipbuilding funding at scale.** The President's Budget for fiscal year 2027, released in April 2026, requested over $65 billion in shipbuilding funding [s.2026-05-23-gao-26-109068-navy-and-coast-g]. **FACT.** The Coast Guard plans to invest over $40 billion to replace and expand its current fleet of ships [s.2026-05-23-gao-26-109068-navy-and-coast-g]. **FACT.**

**Cross-government policy direction on the maritime industrial base.** The White House released America's Maritime Action Plan in February 2026, setting out common challenges and policy options for the maritime industrial base across government and commercial shipbuilding [s.2026-05-23-gao-26-109068-navy-and-coast-g]. **FACT.** The Maritime Action Plan designates the Department of Commerce as the lead on foreign investment in the shipbuilding sector and designates the Department of the Navy in a formal advisory role in that process [s.2026-05-23-the-time-is-ripe-for-next-step]. **FACT.**

**Allied investment as a force multiplier.** The July 2025 U.S.-Japan trade arrangement included $550 billion in Japanese government investment in strategic U.S. industries, including shipbuilding [s.2026-05-23-the-time-is-ripe-for-next-step]. **FACT.**

**Adjacent federal funding stream.** The Maritime Administration administers the Port Infrastructure Development Program, a federal grant program for port infrastructure projects that includes language relevant to naval repair capacity [s.2026-05-23-port-infrastructure-developmen]. **FACT.**

**Assessment.** The dollar scale is decisive. The capture question is not whether money will be spent on shipbuilding and sustainment — it will — but whether the specific procurement vehicles, contract structures, and prime-or-sub positions for CACI align with the training and modeling work that section 7 hypothesizes might be a real opportunity. That alignment question is what the §3.3 engagement-mechanism work has to surface.

### 3.3 Engagement mechanism — how the customer is reaching the market

This subsection is the thinnest of the three because the first source-finder pass under-surfaced engagement-mechanism material. The targeted second pass (queued 2026-05-23 with USNI / SRF-JRMC / Pacific-Fleet-forward-sustainment / war.gov queries) is intended to fill more of this in. For now, two concrete touchpoints are recorded; the full inventory remains a §11.1 task.

**Open Navy SBIR / STTR cycle relevant to the sustainment thread.** The Navy's FY2026 SBIR/STTR cycle includes topic DON26TZ01, "Sensing to Measure and Validate Corrosion in Naval Systems" [s.2026-05-23-don26tz01-sttr-release-1-sensi]. **FACT.** This is adjacent rather than directly on the battle-damage-repair thread, but it is evidence that the corrosion / structural-health side of the sustainment problem is being researched through Navy SBIR/STTR pathways — a relevant signal for any future CACI engagement strategy that uses small-business R&D vehicles as a first-touch.

**Federal port-infrastructure grant program.** The Maritime Administration's Port Infrastructure Development Program is administered as a competitive grant program with public funding cycles [s.2026-05-23-port-infrastructure-developmen]. **FACT.** Touchpoint relevance: lower-priority than the Navy-direct engagement work in §11.1, but a candidate path for partnered-with-port-authority engagement in territories where the Navy needs forward repair capacity (e.g., Guam).

**Assessment.** A more complete engagement-mechanism inventory belongs in §11.1, which is still in early-stage desk research. Standard NAVSEA touchpoints (industry days, broad agency announcements, formal SBIR/STTR cycles) and NSWC-Carderock-specific public-engagement materials need to be ingested before §3.3 can be filled out properly. The second find_sources pass running 2026-05-23 is the next input to this work.

## 4. Customer landscape

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

The Stimson Center's U.S.-Japan Task Force on Military Shipbuilding, Maintenance, and Repair Operations (MSMRO) released recommendations on 25 March 2026 calling for increased Repair, Maintenance, and Industrial work in Japan and adjacent third-country locations including the Philippines, Australia, and Guam [s.2026-05-23-the-time-is-ripe-for-next-step]. **FACT.** The Task Force was co-led by Andrew Oros (Stimson Senior Fellow, Director, Japan Program) and Steve Brock (former Senior Advisor to the Secretary of the Navy, April 2022 to January 2025) [s.2026-05-23-the-time-is-ripe-for-next-step]. **FACT.**

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

The Stimson Center's U.S.-Japan MSMRO Task Force frames an alliance-level partnership thread that is structurally different from the U.S.-only competitive picture above.

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

5. **Relationship feasibility — CACI can be positioned at the right Navy organizations.** *Claim:* CACI can realistically build or expand the relationships needed to execute a BDAR/BDAT capability bid, on a timeline shorter than the customer demand window. *What kills it:* the relevant Navy customer organizations (NSWC Carderock for the modeling input; NAVSEA and the SRF/RMC system for the consuming customer; NWDC or fleet schoolhouses for the curriculum and doctrine owner) have their engagement bandwidth locked up by canonical naval-services incumbents — SAIC, Leidos, HII Mission Technologies — to a degree that CACI's entry timeline runs past the demand window. If true, this is a partnering decision, not a prime-position decision. *Note:* per the section 9.3 contact-protection discipline and the OCI primer at `_meta/oci-primer.md`, the operator's working-level knowledge about CACI's current contract footprint at any Navy organization is operator-side context and does not enter this leg's falsifier reasoning. The leg is framed at the general competitive level.

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

# Battle Damage Repair (BDR) modeling integration into multidomain fleet training and PAE-IO repair-capacity planning — Research File

**Customer:** Multi-customer research track (confirmed by operator 2026-05-21; candidate downstream customers if/when the track resolves to a named opportunity: NSWC Carderock Division as modeling source, NAVSEA as parent command, OPNAV / N9 as fleet-readiness demand-side, PAE-IO / Amentum as industrial supply-side)
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
> | BDR | Battle damage repair — the engineering work of fixing a ship that has been hit. |
> | BDA | Battle damage assessment — the diagnostic work of figuring out what is broken on a hit ship and how bad it is. Upstream of BDR. |
> | NSWC Carderock | A division of the Naval Surface Warfare Center, located in Maryland, that does ship survivability and damage modeling. The single most important named organization in this research track. |
> | NAVSEA | Naval Sea Systems Command — the Navy organization that owns NSWC Carderock, the public shipyards, and most ship-repair contracting. |
> | OPNAV / N9 | The Chief of Naval Operations' staff. N9 is the Warfare Systems directorate, which owns much of the fleet-readiness demand picture. |
> | NWDC | Naval Warfare Development Command — the Navy's doctrine and tactical-training authority. |
> | PAE-IO | PAE Industrial Operations — the ship-repair business now owned by Amentum after a 2024 acquisition. The industrial-supply-side actor we are tracking. |
> | LVC | Live, virtual, constructive — a category of military simulation training that mixes real units, simulator pilots, and computer-generated forces. |
> | M&S | Modeling and simulation. |
> | SBIR / STTR | Small Business Innovation Research and Small Business Technology Transfer — federal R&D contracting paths that often serve as a low-friction first engagement with Navy labs. |
> | COMPTUEX | Composite Training Unit Exercise — a large Navy training event each strike group runs before deploying. |
> | RIMPAC | Rim of the Pacific — the world's largest international maritime exercise, held every two years. |
> | LSE | Large-Scale Exercise — a Navy series introduced in 2021 that strings multiple exercises together to test distributed fleet operations. |
> | SWARMEX | Ship Wartime Repair and Maintenance Exercise — a specific 2025 NAVSEA program first run by SRF-JRMC. The top-scoring hit from the 2026-05-21 source pass. |
> | SRF-JRMC | Ship Repair Facility, Japan Regional Maintenance Center — the Navy organization in Japan that ran the first SWARMEX. |
> | VBS4 / MAK ONE | Commercial military training simulation platforms used widely in DoD. Candidate platforms for a BDA serious-game pipeline. |
> | DON | Department of the Navy — the civilian-led department that includes both the U.S. Navy and the U.S. Marine Corps. |
> | GAO | Government Accountability Office — Congress's auditor, which publishes oversight reports we treat as primary sources. |
> | CRS | Congressional Research Service — Congress's in-house research arm; its reports are public and citation-quality. |
> | SASC / HASC | Senate Armed Services Committee / House Armed Services Committee. |

---

## 1. Working summary (analyst view)

This is a research track, not yet a named capture opportunity. The question we are trying to answer, using only publicly-available material, is whether NSWC Carderock's ship-damage modeling work is the foundation of a real business opportunity for CACI — and if so, what shape that opportunity takes.

There are five threads inside that question, and the research has to address all five before any recommendation makes sense:

1. **Is Carderock's modeling actually useful for fleet training?** That is, can the Navy's ship-damage modeling work be folded into multidomain training events at a fidelity that operators would actually use?

2. **Is there a gap on either side of that modeling?** Specifically, do current fleet training scenarios understate how badly ships get hit in a real fight, and does the industrial-supply side (PAE Industrial Operations / Amentum) plan for steady-state repair when the actual demand under wartime conditions would be much higher?

3. **What does the training program itself look like?** The working concept is a three-step progression — start with tabletop scenarios in a classroom, then guided site visits to actual repair facilities, then hands-on pilot operations on instrumented training rigs. Each step is a fidelity step-up and can also be a classification step-up.

4. **How does CACI even get in the room?** We are assuming at scaffold time that CACI does not currently have a working relationship with the Carderock damage-modeling team. So a parallel work stream of the research is mapping out who to approach, what existing engagement on-ramps Carderock offers, and what intro paths CACI might have through adjacent Navy lab relationships.

5. **A separate training pipeline for damage-assessment teams** — distinct from the repair-side training in thread 3. Damage assessment is the diagnostic skill upstream of repair: when a ship is hit, the assessment team has to classify the damage and decide what gets fixed first before the repair team can act. The proposal here is a high-frequency gamified-simulation layer (serious games, instrumented training rigs, augmented/virtual reality, hardware-in-the-loop benches) that keeps assessment teams sharp between live exercises, followed by real-world exercise injects in fleet training events. The reason it is a separate thread from thread 3 is that the audience, the cadence of practice, and the fidelity ramp are all different.

This research track was initiated based on a working observation shared by a working-level Navy ship-repair contact. Their framing informs the research direction — specifically the view that wartime ship repair capability and the training around it are an underdeveloped area worth examining. Everything in this file must be supported by public sources alone; the contact is not named here and is not the source of any factual claim. See section 9.3 for the verification discipline this implies.

This summary states the scope neutrally. The hypothesis in section 7 is one possible outcome of this research — not a finding. The research plan in section 10 deliberately includes evidence that would falsify the hypothesis, because pulling that evidence first is the most efficient way to either kill the track early or commit to it with confidence. The engagement strategy in section 11 is sequenced so that the relationship-development work proceeds in parallel with the hypothesis-testing work, since relationship cadence at Navy labs is months-to-years and starting early costs nothing if the hypothesis later fails.

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
- [ ] What facilities support guided site visits at the next fidelity step? (NSWC Carderock proper; NSWC Philadelphia; intermediate maintenance activities; the four public naval shipyards; selected private repair facilities operated by HII Newport News, BAE Norfolk, GD NASSCO, Vigor / Titan Acquisitions.)
- [ ] What does "pilot repair operations" look like at the top of the training progression — simulator-based, real-equipment-on-instrumented-test-bed, or live operations on training hulls? Which model is feasible at unclassified level?
- [ ] **[DISCONFIRMING]** Is there an existing Navy training program that already does the full tabletop→site-visit→pilot progression for BDR? If yes, the gap is execution / scaling, not design — the recommendation shape changes.

### BDA team preparedness questions (added 2026-05-21 scope expansion #2)

- [ ] What is the Navy's current BDA training pipeline? Who owns it — Naval Warfare Development Command (NWDC), Surface Force Training and Readiness Manual (SFTRM) authorities at COMNAVSURFOR, AFLOATRAFOR, fleet-specific shops, or some combination?
- [ ] **[DISCONFIRMING]** Is there already a mature DoD-funded BDA serious-game or instrumented-sim product? Search SBIR Phase II/III awards (`sbir.gov`), NWDC product catalog, Naval Postgraduate School / Naval War College thesis library, MORS conference papers. If a usable product exists, the play shifts from "build a BDA-sim platform" to "integrate / extend an existing one."
- [ ] **[DISCONFIRMING]** Is BDA-team training already deeply embedded in fleet exercises (COMPTUEX, RIMPAC, Large-Scale Exercise / LSE, ANTX, Trident Warrior)? If yes, the real-world-exercise leg of this scope is execution-only, not opportunity-creation.
- [ ] What commercial / GOTS serious-game and sim engines are candidate platforms (Bohemia Interactive Simulations VBS4, Improbable, NVIDIA Omniverse digital twins, MAK ONE, Unity / Unreal toolchains used in DoD training, hardware-in-the-loop benches at Carderock or partner labs)? Cost / classification / IP posture of each?
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

## 3. Demand signal — what the customer (when defined) is saying

*[Section reserved — populate after source ingestion. Will include public NAVSEA / NSWC Carderock priorities, OPNAV fleet-readiness public testimony, and any named gap statements parallel to PMTEC's "eight named priority gaps." Until then, this section is empty by design — do not back-fill speculative content here.]*

### 3.1 Stated priorities

*[To be populated after source ingestion. Each entry must carry an `[s.YYYY-MM-DD-slug]` citation tag.]*

### 3.2 Funding

*[To be populated. Likely sources: NAVSEA FY budget exhibits, Navy O&M lines for maintenance and modernization, congressional appropriations marks.]*

### 3.3 Engagement mechanism

*[To be populated. Likely sources: NAVSEA SBIR/STTR public solicitations, ONR BAAs, Carderock industry-engagement public materials.]*

## 4. Customer landscape

*[Section reserved — populate after the customer-field decision is made and after source ingestion. Will include NAVSEA / NSWC structure, named POCs, reporting lines. Cross-ref to `03_pocs.md` for details.]*

## 5. Competitive landscape

<!-- sensitivity:internal -->

*[Section reserved — populate after source ingestion. Likely competitive entities to scope: incumbents on naval survivability / BDR M&S work (e.g., HII Mission Technologies / former Alion which has historic Carderock-adjacent M&S history; SAIC; Booz Allen; Leidos), Navy Lab partnerships, and PAE-IO direct competitors in ship repair (BAE Systems Ship Repair, General Dynamics NASSCO, HII Newport News / Ingalls, Vigor / Titan Acquisitions).]*

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

**The six things that could falsify this hypothesis:**

The hypothesis breaks into six separate claims, each of which can be tested against public sources. If any one of them fails, the corresponding part of the hypothesis is dead and the recommendation shape has to change.

1. **The training-assumption gap.** *Claim:* current Navy and joint fleet training scenarios assume ships take much less damage than realistic wartime modeling would predict. *What kills it:* Department of the Navy Strategic Readiness Plans or named fleet exercise scenarios already explicitly assume wartime-scale damage rates. If the Navy is already training to realistic damage, there is no gap to close on this side. *Note:* the working observation that initiated this research is consistent with this leg being true. That observation is informal and does not relax the requirement that public-source triangulation produce citable evidence before any recommendation. See section 9.3.

2. **The industrial-planning gap.** *Claim:* PAE Industrial Operations' public-facing planning posture is built around peacetime steady-state repair demand, not a wartime surge. *What kills it:* PAE-IO testimony, contract task-order language, or industrial-base assessments already incorporate realistic wartime attrition assumptions. If the industrial side is already planning for surge, there is no gap to close on this side.

3. **Modeling-fidelity availability.** *Claim:* Carderock's damage-modeling work has a useful unclassified subset — enough to actually drive training scenarios. *What kills it:* the unclassified version is doctrinal or coarse-grained only, and the operationally-useful modeling lives behind a classification gradient this research cannot reach. If that is true, the deliverable changes shape entirely, from "build an unclassified training module" to "engage Navy customers about a classified collaboration."

4. **Training-progression viability.** *Claim:* the tabletop → site-visit → hands-on progression is a feasible program design that does not already exist end-to-end. *What kills it:* (a) some existing Navy program already runs this exact progression, in which case the play is helping execute or scale that program rather than designing a new one, or (b) the legal and operational hurdles of moving cohorts from unclassified content up to classified instrumented test-bed work are prohibitive.

5. **Relationship feasibility.** *Claim:* CACI can realistically build the Carderock relationships needed to execute, on a timeline shorter than the customer's actual demand window. *What kills it:* Carderock's engagement bandwidth is locked up by incumbent technical partners — HII Mission Technologies (which inherited the Alion damage-modeling work), SAIC, Leidos — to a degree that CACI's entry timeline runs past the demand window. If true, this is a partnering decision, not a prime-position decision.

6. **The damage-assessment training pipeline is viable.** *Claim:* the proposed two-phase pipeline for damage-assessment teams (gamified simulation first, real-world exercises second) is a feasible program model that does not already exist. *What kills it:* any one of three things — (a) the Department of Defense has already funded a damage-assessment serious-game product mature enough that the play would be a me-too entry rather than a new pipeline, evidence for this lives in SBIR Phase II and Phase III award databases and the Naval Warfare Development Command product catalog; (b) damage-assessment training is already deeply embedded in fleet exercises like COMPTUEX, RIMPAC, and LSE at a depth that leaves no gap for a new pipeline to fill; or (c) the simulation layer cannot achieve operationally-meaningful realism at unclassified level, which is the same classification-gradient problem as leg 3 but applied specifically to simulation content rather than to source modeling.

**Recommendation (draft):** to be determined — pending source ingestion, the disconfirming-evidence checks above, and the engagement-surface inventory in section 11.

<!-- /sensitivity -->

## 8. Source ledger

*[Empty — no sources ingested yet. As sources are added via `_scripts/ingest.py`, citations will be auto-appended here in `[s.YYYY-MM-DD-slug]` format.]*

### 8.1 Ingested primary sources (in `01_sources/`)

*[None yet.]*

### 8.2 Cited but not yet ingested — needs ingest before external use

*[None yet.]*

---

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

7. **PAE-IO public footprint.**
   - PAE Industrial Operations contract history on USAspending and SAM.gov (via the existing vault tooling: `usaspending.py` and `sam_gov.py`).
   - Amentum (parent of PAE post-acquisition) investor materials referencing the IO business.
   - Public testimony and trade-press coverage of PAE-IO repair-capacity work.

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

### 11.2 Repair-team training — classroom, then facility visits, then hands-on

This section covers training for the people who actually do the repair work after a ship is hit. The next section, 11.3, covers the separate pipeline for the damage-assessment teams who tell the repair crews what to fix first.

The proposed pipeline is a three-step ladder, with each step a fidelity step-up and also potentially a classification step-up. The point of designing this at the concept level now — even before the hypothesis in section 7 has cleared its disconfirming checks — is so that the gate-1 brief in week 3 can describe a concrete program shape rather than just asserting that a program is needed.

**Step 1 — tabletop scenarios, classroom format, fully unclassified.** The first step is paper-and-discussion, run by an instructor. Trainees work through realistic damage scenarios without any equipment in the room.

- Learning objectives at this step: sequencing the damage-control response, triaging which repair actions matter most, identifying supply-chain pressure points, and working through multidomain scenarios where the ship is also being attacked through cyber, electronic warfare, or space-disrupted communications channels.
- Source material can come from public case studies — USS Stark, USS Cole, USS Fitzgerald, HMS Sheffield, the Moskva sinking — open-source threat libraries, public NAVSEA and Carderock methodology papers, and sanitized vignettes built from the above.
- Audiences run from junior officers to damage-control teams to repair-yard supervisors to multidomain joint planners, with different content depth for each.
- Format options include scenario card decks, instructor-led workshops, and multi-week curricula.

**Step 2 — guided site visits to actual repair facilities.** Once trainees have the classroom foundation, the next step is taking them to where the work actually happens.

- Candidate facilities are NSWC Carderock itself (with its full-scale tank facility and structural-test rigs), NSWC Philadelphia (which handles ship machinery), the intermediate maintenance activities at fleet ports, the four public naval shipyards at Norfolk, Portsmouth, Puget Sound, and Pearl Harbor, and selected private repair yards run by HII Newport News, BAE Norfolk, General Dynamics NASSCO, and Vigor / Titan Acquisitions.
- Classification typically steps up at this step. Tabletops can stay fully unclassified, but facility tour content usually begins at controlled-unclassified-information level, and walking trainees through instrumented test-beds may require a security agreement.
- Logistics matter as much as program design. Travel planning, badge sponsorship, escort coverage, and clear limits on what can be discussed — these are real operational tasks, not afterthoughts.

**Step 3 — hands-on practice on a real or instrumented platform.** The top of the ladder is the trainee actually performing assessment and repair planning on something that responds like a damaged ship system.

Three feasibility models, in increasing order of realism and difficulty:

- A simulator-only setup — a digital twin of damage propagation, no live equipment in the room.
- An instrumented test-bed — a real damaged subsystem on a controlled rig, where the training cohort performs assessment and repair planning against actual hardware.
- Live operations on a training hull — the most realistic, also the most operationally demanding. This would require Navy training-hull access, possibly through the Naval Sea Cadet Corps fleet or ex-service-vessel partnerships, each of which is a separate scoping problem.

The instrumented test-bed at NSWC Carderock or a partner site is the highest fidelity that is realistic to achieve at unclassified level.

### 11.3 Damage-assessment team training — gamified simulation first, then real-world exercises

This section covers training for the people who **assess** damage, which is a different skill from doing the actual repair work covered in the previous section.

When a ship gets hit, a damage-assessment team has to look at what just happened and answer four questions fast: how bad is the damage, can the ship still fight, what needs fixing first, and where should the repair team start. The repair team can only act on what the assessment team tells them, which is why we treat this as a separate, earlier training pipeline rather than rolling it into the repair training in section 11.2. Same overall mission, different audience, different cadence of practice, and different fidelity ramp.

The proposed pipeline has two phases, in this order:

**Phase 1 — high-frequency gamified practice between live exercises.** The point of this phase is volume. Damage-assessment skill decays without practice, and live exercises happen rarely. A gamified simulation layer — running on software platforms, on instrumented training rigs, or both — gives assessment teams enough repetitions to stay sharp.

Candidate software platforms to investigate (these are research targets, not endorsements, and the source pass on 2026-05-21 turned up only thin coverage on most of them):

- **VBS4** by Bohemia Interactive Simulations. Already used widely in DoD training and supports custom damage and effects scripting.
- **MAK ONE / VR-Forces.** Used in joint live-virtual-constructive simulation. Has damage models and supports federated simulation through the DIS and HLA protocols.
- **Unreal Engine and Unity toolchains.** Several recent SBIR-funded serious-game vendors build on these rather than on military-specific platforms. Cost-of-build versus commercial-off-the-shelf engine is one of the open trade-offs.
- **NVIDIA Omniverse digital-twin pipelines.** For modeling hull and system damage at high fidelity. The relevant question is whether the fidelity is operationally meaningful, not whether it looks good on screen.
- **Tabletop digital-wargame engines** from the commercial educational space. These are useful as a reference point for what gamification mechanics actually work, not as a deployment target.

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
| BDA serious-game space is already saturated by incumbents (SAIC, Leidos, BISim, MAK) | Lead with an ARKA-signature-library differentiator (§11.3) rather than a generic platform pitch; if no differentiator survives §2 disconfirming checks, the BDA pipeline scope should be dropped rather than pursued as a me-too entry |
| Sim-vs-live progression order is mistaken — Navy training authorities may insist live-exercise-first | Treat the "sim-first" claim as a §7-leg-6 hypothesis to be tested; if Navy training doctrine inverts the order, redesign §11.3 around live-exercise lead with sim as remediation tooling |

<!-- /sensitivity -->

---

*This research file was scaffolded on 2026-05-21 and expanded twice the same day to cover a three-step repair-team training pipeline plus a parallel relationship-development work stream (sections 11.1 and 11.2), and a separate damage-assessment team training pipeline progressing from gamified simulation to real-world exercises (section 11.3). The operator authorized source research on 2026-05-21 and the first source-finding pass ran the same day, queuing 67 candidates in `_inbox.md`. Research was paused on 2026-05-22 to apply a readability fix across the vault and to fold lessons from a Medium article on software-fundamentals applied to AI workflows into the process. See the decision log for the full chain.*

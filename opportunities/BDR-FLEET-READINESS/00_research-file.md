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
> Per SOP §2.1, every claim must carry one of three labels: **FACT**, **Assessment**, or **Speculation**.

---

## 1. Working summary (analyst view)

This is a research track, not yet a capture opportunity. The scope is to determine, against open-source intelligence (OSI) only:

1. Whether NSWC Carderock Division's battle damage and repair (BDR) modeling and ship survivability modeling can and should be integrated into multidomain service training.
2. What that modeling, if releasable at OSI fidelity, implies about (a) the realism of current fleet training assumptions regarding wartime battle damage and (b) the demand assumptions in PAE Industrial Operations (PAE-IO) repair-capacity planning.
3. **What a robust training program built on that modeling would look like** — progressing from tabletop scenarios (OSI-fidelity content, classroom format) through guided site visits (NSWC Carderock or partner facilities) to pilot repair operations (hands-on training using simulated or instrumented damage scenarios).
4. **How CACI would build the NSWC Carderock relationships needed to execute** — assumed at scaffold time that CACI does not currently have direct working relationships with the Carderock BDR / survivability program leads. The research track therefore includes a parallel work stream on engagement-surface mapping and warm-intro paths.
5. **A separate battle-damage-assessment (BDA) team preparedness pipeline**, distinct from the repair-operations training in (3): a gamified-software/hardware simulation layer (serious games, instrumented sim rigs, AR/VR, hardware-in-the-loop) used to keep BDA teams sharp between events, transitioning to real-world exercises (embedded BDA-team injects into existing fleet exercises and Carderock-instrumented test events). Justification: BDA is an assessment skill (rapid classification of damage, mission-impact triage, repair-priority sequencing) that LOGICALLY PRECEDES the repair-team activation covered in (3) — different audience, different cadence, different fidelity ramp.

The scope is stated NEUTRALLY at this stage. The hypothesis in §7 is one possible outcome of the research, not a finding. The research plan in §10 includes evidence that would DISCONFIRM the hypothesis. The engagement strategy in §11 (new this scope expansion) is sequenced so that relationship-development can proceed in parallel with hypothesis-testing rather than blocking on it.

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

**Assessment (hypothesis to be tested, not a finding):**

Current fleet training assumptions and PAE-IO industrial planning materially understate wartime battle-damage rates, damage types, and repair-capacity demand. NSWC Carderock Division's BDR and ship survivability modeling — to the fidelity it can be released at OSI level — can quantify that gap and serve as a training-injection source to close it. A robust training program built on that modeling would progress from **tabletop scenarios** (OSI-fidelity content, classroom format) through **guided site visits** (NSWC Carderock or partner facilities) to **pilot repair operations** (hands-on training using simulated or instrumented damage scenarios). The progression itself is operationally meaningful because each step can independently step up classification access, allowing the program to start at OSI and graduate to classified content only where and when warranted.

**Stance:** This is a hypothesis to be tested against primary sources. It is NOT yet a finding. The research plan in §10 includes the specific disconfirming evidence (also enumerated in §2 with `[DISCONFIRMING]` prefixes) that would falsify each leg of this hypothesis. The hypothesis should be revisited and either upgraded to a FACT-supported recommendation or revised/abandoned after the first round of OSI source ingestion. **Execution of any recommendation also depends on a relationship-development work stream with NSWC Carderock that does not yet exist — see §11.**

**Six falsifiable legs of the hypothesis:**

1. *Training-assumption gap.* Navy / joint fleet training documents currently assume attrition and battle-damage rates significantly below what wartime modeling would predict. → Falsified if DON Strategic Readiness Plans or fleet exercise scenarios already assume warfighting-scale damage.
2. *Industrial-planning gap.* PAE-IO's public-facing planning posture assumes peacetime / steady-state repair demand rather than warfighting surge. → Falsified if PAE-IO testimony, contract task-order language, or industrial-base assessments already assume realistic attrition.
3. *Modeling-fidelity availability.* Carderock's BDR/survivability modeling has an OSI-releasable subset of useful operational fidelity. → Falsified if the OSI-releasable version is doctrinal/coarse only, and the operationally-useful modeling is behind a classification gradient inaccessible to this research.
4. *Training-progression viability.* A tabletop→site-visit→pilot-operations progression is a feasible and not-already-implemented program model. → Falsified if (a) an existing Navy program already does this end-to-end, in which case the play is execution / scaling rather than design, OR (b) the progression cannot legally / operationally clear the classification stair-step from OSI tabletops up to instrumented repair pilots.
5. *Relationship feasibility.* CACI can realistically build the NSWC Carderock relationships needed to execute, on a timeline shorter than the demand window. → Falsified if Carderock's engagement posture is locked up by incumbent technical partners (e.g., HII Mission Technologies' Alion-inheritance, SAIC, Leidos) such that CACI's entry timeline exceeds the customer-demand timeline.
6. *BDA-preparedness pipeline viability.* A gamified-sim-then-real-world progression is a feasible and not-already-saturated training-program model for BDA teams. → Falsified if (a) a DoD-funded serious-game / instrumented-sim product for BDA already exists at sufficient maturity (search SBIR Phase II/III awards, NWDC products, Naval Warfare Development Command training catalog), OR (b) BDA training is already embedded in fleet exercises (COMPTUEX, RIMPAC, LSE) at a depth that leaves no gap, OR (c) the gamified-sim layer cannot achieve operationally-meaningful realism at OSI fidelity (parallel to leg-3 classification-gradient constraint, applied to BDA-sim content).

**Recommendation (draft):** TBD — pending source ingestion, disconfirming-evidence check, and engagement-surface inventory.

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

### 9.1 Classification gradient — load-bearing constraint

**Naval BDR and ship survivability data has a steep classification gradient.** The substantive operational fidelity of Carderock's modeling — damage propagation, specific hull and system vulnerability data, validated repair-time distributions — almost certainly lives at SECRET or higher and is NOT available at OSI level. The OSI-releasable version is necessarily LIMITED-FIDELITY and may consist of: doctrine, public testimony framing, generalized methodology descriptions, sanitized vignettes, and academic / NAVSEA-published unclassified abstracts.

**Implication for this research track:**
- Every claim drawn from public Carderock material must be explicitly tagged as OSI-only and **must not be presented as if it reflects the full operational modeling capability.**
- The research can usefully establish: that the modeling exists; what NAVSEA / Carderock publicly say about its scope; what GAO and congressional oversight have said about associated capabilities and gaps; and what the OSI-published methodology suggests about training-injection feasibility in principle.
- The research CANNOT usefully establish: actual damage-rate predictions, specific vulnerability data, or repair-time distributions at operationally meaningful fidelity. Any such claim would either require classified access (out of scope) or would be speculation (labeled accordingly).
- A recommendation flowing from this research must respect this gradient — e.g., the recommendation may be "engage NAVSEA / Carderock to scope a classified collaboration" rather than "deliver an OSI-grade training injection module."

### 9.2 Standing verification posture

- All claims labeled per SOP §2.1 rule 4: **FACT**, **Assessment**, or **Speculation**.
- All FACTs must carry an `[s.YYYY-MM-DD-slug]` citation tag pointing to an ingested source.
- Two-source rule applies to non-trivial claims (money, timelines, named people, attribution) per SOP §2.1 rule 2.
- Re-verify POCs every 90 days per SOP §2.1 rule 3.

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

### 11.2 Training-progression design — repair operations (Week 2-3, contingent on §7 hypothesis survival)

**Goal:** design the tabletop → site-visit → pilot training progression at concept level so that the Gate 1 brief in Week 3 can include a concrete program shape, not just an assertion that a program is needed.

This subsection covers the **repair-team** training pipeline. The **BDA-team** training pipeline is structurally distinct and is covered separately in §11.3.

**Tabletop phase (OSI-fidelity, classroom format):**
- Learning objectives: damage-control sequencing, repair triage, supply-chain stress points, multi-domain damage scenarios (kinetic + cyber + EW + space-disrupted comms).
- Content sources at OSI fidelity: historical case studies (USS Stark, USS Cole, USS Fitzgerald, HMS Sheffield, Moskva), open-source threat libraries, public NAVSEA / Carderock methodology papers, sanitized vignettes.
- Audience: junior officers, damage-control teams, repair-yard supervisors, multi-domain joint planners. Different audiences get different content depths.
- Format: scenario card decks, instructor-led workshops, multi-week curriculum.

**Site-visit phase (guided facility immersion):**
- Candidate facilities: NSWC Carderock proper (full-scale tank facility, structural-test facilities); NSWC Philadelphia (machinery); intermediate maintenance activities; the four public naval shipyards (Norfolk, Portsmouth, Puget Sound, Pearl Harbor); private repair facilities operated by HII Newport News, BAE Norfolk, GD NASSCO, Vigor / Titan Acquisitions.
- Classification step-up: tabletops are OSI; site visits begin at controlled-unclassified (CUI) for facility tour content; instrumented test-bed walk-throughs may require security agreement.
- Logistics: travel planning, badge sponsorship, escort coverage, content scope-of-discussion limits — all real operational items, not just program design.

**Pilot repair operations (hands-on, top of progression):**
- Feasibility models: (i) simulator-only (e.g., a digital twin of damage propagation, no live equipment); (ii) instrumented test-bed (a real damaged subsystem on a controlled rig, training cohort performs assessment and repair planning); (iii) live operations on a training hull (extreme model — would require Navy training-hull access, possibly via the Naval Sea Cadet Corps fleet or ex-service vessel partnerships, all of which need separate scoping).
- Highest unclassified fidelity is probably (ii) instrumented test-bed at NSWC Carderock or a partner site.

### 11.3 BDA team preparedness — gamified-then-real-world progression (Week 2-3, parallel to §11.2)

**Goal:** design a separate BDA-team training pipeline, structurally distinct from the repair-team progression in §11.2. BDA is the upstream assessment skill (rapid damage classification, mission-impact triage, repair-priority sequencing) that drives WHEN and WHAT the §11.2 repair pipeline activates. The progression model here is **gamified-software/hardware sim → real-world exercises**, in that order, because BDA reps need high frequency / low friction / instant-replay characteristics that only a gamified layer can supply between live events.

**Phase 1 — Gamified-software / gamified-hardware sim layer (high-frequency reps between live exercises):**

- *Software candidate platforms (OSI-research targets, not endorsements):*
  - Bohemia Interactive Simulations VBS4 (used widely in DoD training; supports custom damage / effects scripting).
  - MAK ONE / VR-Forces (used in joint LVC; damage models and federated simulation via DIS / HLA).
  - Unreal / Unity toolchains as used by recent SBIR / serious-game vendors (cost of bespoke build vs. COTS engine).
  - NVIDIA Omniverse digital-twin pipelines for hull / system damage modeling (operationally-relevant fidelity question — separate from photorealism).
  - Commercial educational tabletop digital wargame engines as a frame-of-reference, not as a deployment target.
- *Hardware-in-the-loop / instrumented-sim candidates:*
  - Carderock's existing structural shock-and-vibration rigs in a controlled training-mode.
  - AR / VR headset stacks with damage-overlay content keyed to ship-class digital twins.
  - Tabletop instrumented BDA "reps" — physical mock-up boards with embedded sensors generating live-feed damage signatures the trainee must classify.
- *Gamification mechanics (pedagogical, not cosmetic):*
  - Scenario branching keyed to the trainee's first-call damage classification — wrong classification triggers cascading downstream consequences that surface in subsequent reps.
  - Scoring + after-action replay against ground-truth damage state.
  - Cohort leaderboards across ships, squadrons, or training cohorts to drive practice volume.
  - Replay archives that feed into doctrine-update loops at NWDC / SFTRM authorities.
- *Audience scoping:*
  - Ship-level damage-control teams (highest volume, lowest individual-rep duration).
  - Fleet-level BDA cells at numbered-fleet staffs (longer scenarios, higher mission-impact-triage emphasis).
  - Joint multidomain BDA staff at Combatant Command level (cross-domain scenarios — kinetic + cyber + EW + space-disrupted comms, parallel to §11.2 tabletop content).

**Phase 2 — Real-world exercises (lower frequency, higher fidelity, embedded with the live fleet):**

- *Embedded BDA injects in existing fleet exercises* — COMPTUEX, RIMPAC, Large-Scale Exercise (LSE), ANTX, Trident Warrior. Approach: a small BDA-cell add-on that runs in parallel with the parent exercise rather than replacing existing scenarios.
- *Carderock-instrumented controlled events* — bridge between sim and live; high-fidelity ground-truth available for after-action.
- *Joint red-team / blue-team BDA evolutions* — red team generates realistic damage signatures (kinetic + non-kinetic) from a known threat library; BDA cohort classifies in operationally-realistic time pressure.
- *Cross-service exercises with USMC, Army, USAF BDA equivalents* if the multidomain framing in the §1 scope statement holds.

**Why this progression order (sim first, real-world second):**

- High-frequency reps are the engine of skill retention; only the gamified layer supplies them at a usable cadence.
- Each live exercise costs orders of magnitude more than a sim rep, so live exercises should be reserved for scenarios that the sim layer cannot replicate.
- The classification stair-step in §7-leg-3 applies here too: sim content can be designed for OSI / CUI release; live exercises step up to classified ground-truth when the participant cohort is cleared and the venue is approved.

**Differentiator-hook check (cross-link to §11.4 risks):**

- ARKA EO/IR / hyperspectral signature libraries — if releasable for training use — could feed the gamified-sim scenario engine with operationally-realistic threat-effect signatures that the SAIC / Leidos / HII Mission Technologies incumbents cannot easily source. This is a hypothesis to be tested against ARKA IP / release-authority constraints, not a finding.

**Disconfirming checks specific to this subsection (cross-listed in §2 BDA questions):**

- DoD-funded BDA serious-game already exists at sufficient maturity (SBIR Phase II/III, NWDC catalog, NPS / NWC thesis library).
- BDA training already embedded in fleet exercises at depth that closes the gap.
- OSI-fidelity sim content cannot achieve operationally-meaningful realism — same constraint that applies to §11.2 tabletops.

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

*Scaffold created 2026-05-21. Scope expanded 2026-05-21 to include (a) training-progression design (§11.2) and NSWC relationship-development (§11.1), and (b) BDA team preparedness pipeline — gamified-sim-then-real-world progression (§11.3, scope expansion #2). Operator authorized "begin research" 2026-05-21; `auto_find:true` set in index.md and `_search-config.yaml` drafted. First `find_sources.py` pass not yet executed — pending operator answer on scope-of-first-pass and BDA-query insertion. See decision log.*

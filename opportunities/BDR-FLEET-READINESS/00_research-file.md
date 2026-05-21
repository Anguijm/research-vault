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

This is a research track, not yet a capture opportunity. The scope is to determine, against open-source intelligence (OSI) only, whether NSWC Carderock Division's battle damage and repair (BDR) modeling and ship survivability modeling can and should be integrated into multidomain service training as a training injection — and what that modeling, if releasable at OSI fidelity, implies about (a) the realism of current fleet training assumptions regarding wartime battle damage and (b) the demand assumptions in PAE Industrial Operations (PAE-IO) repair-capacity planning.

The scope is stated NEUTRALLY at this stage. The hypothesis in §7 is one possible outcome of the research, not a finding. The research plan in §10 includes evidence that would DISCONFIRM the hypothesis.

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

Current fleet training assumptions and PAE-IO industrial planning materially understate wartime battle-damage rates, damage types, and repair-capacity demand. NSWC Carderock Division's BDR and ship survivability modeling — to the fidelity it can be released at OSI level — can quantify that gap and serve as a training-injection source to close it.

**Stance:** This is a hypothesis to be tested against primary sources. It is NOT yet a finding. The research plan in §10 includes the specific disconfirming evidence (also enumerated in §2 with `[DISCONFIRMING]` prefixes) that would falsify each leg of this hypothesis. The hypothesis should be revisited and either upgraded to a FACT-supported recommendation or revised/abandoned after the first round of OSI source ingestion.

**Three falsifiable legs of the hypothesis:**

1. *Training-assumption gap.* Navy / joint fleet training documents currently assume attrition and battle-damage rates significantly below what wartime modeling would predict. → Falsified if DON Strategic Readiness Plans or fleet exercise scenarios already assume warfighting-scale damage.
2. *Industrial-planning gap.* PAE-IO's public-facing planning posture assumes peacetime / steady-state repair demand rather than warfighting surge. → Falsified if PAE-IO testimony, contract task-order language, or industrial-base assessments already assume realistic attrition.
3. *Modeling-fidelity availability.* Carderock's BDR/survivability modeling has an OSI-releasable subset of useful operational fidelity. → Falsified if the OSI-releasable version is doctrinal/coarse only, and the operationally-useful modeling is behind a classification gradient inaccessible to this research.

**Recommendation (draft):** TBD — pending source ingestion and disconfirming-evidence check.

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

1. **Week 1:** Scope source-finding. Add `_search-config.yaml` for this opportunity with target NAVSEA / Carderock / SASC / GAO / CRS queries. Pull the two disconfirming-evidence sources first (DON Strategic Readiness Plan, FY26 Navy budget) to test the hypothesis early.
2. **Week 2:** If hypothesis survives Week 1 disconfirmation, broaden to Carderock public materials and PAE-IO industrial footprint.
3. **Week 3:** Synthesize into a research-file update with FACT-labeled findings, revised hypothesis or recommendation, and a Gate 1 brief decision (continue / pivot / drop).

---

*Scaffold created 2026-05-21. No research performed yet. Source ingestion and verifier runs are blocked until operator confirms: (a) folder ID, (b) customer field, (c) PMTEC cross-link decision. See decision log.*

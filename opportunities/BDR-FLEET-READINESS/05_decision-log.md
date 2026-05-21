# BDR-FLEET-READINESS — Decision Log

Every decision: date, decision, by whom, rationale, what changed.

---

### 2026-05-21 — Research track scaffolded (no research started)

**By:** operator (instruction via `/remote-control`) + Claude Code (Opus 4.7) executing scaffold
**Rationale:** Open a new research track to examine whether NSWC Carderock Division's BDR / ship survivability modeling can be integrated into multidomain service training and what that modeling implies about current fleet training assumptions and PAE-IO repair-capacity planning. Scaffold only — no source ingestion or research performed.
**What changed:** Created folder `opportunities/BDR-FLEET-READINESS/` with standard structure (index.md, 00_research-file.md, 01_sources/, 02_quotes.md, 03_pocs.md, 04_artifacts/, 05_decision-log.md). Seeded 00_research-file.md with neutral working summary, falsifiable hypothesis labeled `Assessment:` in §7, open-questions list including explicit `[DISCONFIRMING]` items in §2, OSI-only research plan in §10, and a load-bearing classification-gradient flag in §9.1. `auto_find: false` set in index.md so the vault's automated source-finder will NOT run against this folder until operator confirms scaffold + makes three pending decisions (folder ID, customer field, PMTEC cross-link).

**Pending operator decisions before research begins:**
1. Confirm folder ID `BDR-FLEET-READINESS` (note: deviates from standard `[OPPORTUNITY]-[CUSTOMER]` pattern since no customer is specified yet).
2. Confirm customer field — candidates flagged in `index.md`: NSWC Carderock Division (modeling source), NAVSEA (parent command), or treat as a multi-customer research track.
3. Decide whether to cross-link to PMTEC given the multidomain-training overlap (e.g., backlinking from PMTEC's §3.1 priority #6 "Realistic training targets" or priority #4 "Multi-level secure information sharing" given training-injection adjacency).

---

### 2026-05-21 — Scaffold decisions A/B/C confirmed

**By:** operator (confirmation via `/remote-control` chat)
**Rationale:** Three scaffold decisions flagged in the 2026-05-21 scaffold report were answered: (A) keep folder ID `BDR-FLEET-READINESS` despite deviation from `[OPPORTUNITY]-[CUSTOMER]` pattern; (B) customer field = `multi-customer research track`; (C) cross-link to PMTEC = yes.
**What changed:**
- `index.md` — `customer:` field set to "multi-customer research track" with candidate downstream customers (NSWC Carderock, NAVSEA, OPNAV/N9, PAE-IO/Amentum) noted as an inline comment for when the track resolves.
- `index.md` — added "Related research tracks" section linking to `PMTEC-USINDOPACOM/index`.
- `00_research-file.md` — header `Customer:` field updated to reflect Decision B.
- `PMTEC-USINDOPACOM/00_research-file.md` §3.1 priority #6 ("Realistic training targets") — added inline cross-link to this track so the connection is discoverable from both directions.
- `auto_find:` remains `false` in `index.md` — pending operator's explicit "begin research" trigger before source ingestion starts.

**Next pending decision:** Operator says "begin research" to flip `auto_find:true`, configure `_search-config.yaml` (NAVSEA / Carderock / SASC / GAO / CRS / DoD comptroller queries), and start running disconfirming-evidence checks per §10.3 sequencing.

---

### 2026-05-21 — Scope expansion: training-design progression + NSWC relationship-development

**By:** operator (instruction via `/remote-control` chat) + Claude Code (Opus 4.7) executing edits
**Rationale:** Operator broadened the BDR-FLEET-READINESS scope to include (a) design of a robust training program progressing from tabletop scenarios through guided site visits to pilot repair operations, and (b) explicit assumption that CACI does not currently have NSWC Carderock working relationships — therefore the research track includes a parallel engagement / relationship-development work stream.
**What changed:**
- `index.md` — added `training-design` to `capability_tags` (now 7 tags).
- `00_research-file.md` §1 working summary — expanded from a two-point scope to a four-point scope explicitly naming the training-progression dimension and the relationship-development dimension.
- `00_research-file.md` §2 — added two new question groups: "Training-design questions" and "NSWC relationship-development questions" with `[DISCONFIRMING]` items in each group (e.g., is there already a Navy program doing the full tabletop→pilot progression; does CACI already have an active Carderock relationship the operator was unaware of).
- `00_research-file.md` §7 hypothesis — expanded from three to five falsifiable legs adding (4) training-progression viability and (5) relationship feasibility. Hypothesis prose now names the tabletop→site-visit→pilot model and acknowledges the classification stair-step that the progression enables.
- `00_research-file.md` §10.3 sequencing — parallel work-stream language added (engagement-surface inventory starts Week 1 alongside hypothesis disconfirmation).
- `00_research-file.md` §11 (new) — Engagement & relationship strategy section covering §11.1 engagement-surface inventory (Carderock command directory, conference papers, SBIR/STTR topic authorship, FLC tech-transfer queue, NAVSEA industry days, adjacent CACI / NSWC site relationships); §11.2 training-progression design (tabletop / site-visit / pilot phase definitions with candidate facilities and feasibility models); §11.3 engagement timeline assumption (Speculation-labeled month-by-month plan); §11.4 risks specific to the engagement work stream.

**No research performed.** `auto_find:` remains `false`. The next pending decision is unchanged: operator says "begin research" to start §10 source ingestion + §11.1 desk-research engagement inventory.

---

### 2026-05-21 — Begin research authorized; search-config drafted

**By:** operator (instruction: "Begin research") + Claude Code (Opus 4.7) executing config
**Rationale:** Operator gave explicit "begin research" trigger. Per the previous decision-log entry, this flips `auto_find:` to `true`, configures `_search-config.yaml`, and starts §10.3 Week 1 disconfirming-evidence checks.
**What changed:**
- `index.md` — `auto_find:` flipped `false` → `true`.
- `index.md` — `next_action` updated to "Run first find_sources pass (Week 1 disconfirming-evidence queries) and triage inbox."
- `_search-config.yaml` (new) — ordered to match §10.3 sequencing. First five `ai_searches` are the two §10.2 disconfirming-evidence threads (DON Strategic Readiness Plan + FY26 Navy budget + SASC/HASC fleet-readiness testimony for counter #1; Carderock public methodology materials for counter #2). Subsequent queries broaden to GAO / CRS oversight, PAE-IO / Amentum footprint, and §11.1 engagement-surface inventory feeders. `sam_searches` cover Carderock SBIR/STTR + NAVSEA depot-repair vehicles + LVC training. `usa_spending_searches` cover PAE / Amentum / Carderock obligations history with a 2023-01-01 start so the contract base is visible.

**Open before `find_sources.py` first run:**
- Operator review of the search-config (especially the AI-query ordering: are the disconfirming threads in the right priority).
- Confirm whether to run all queries on first pass or limit to Week 1 disconfirming threads only (queries 1-5) to avoid burning API quota on broadening queries before disconfirmation completes.

---

### 2026-05-21 — Scope expansion #2: BDA team preparedness pipeline (gamified-sim → real-world)

**By:** operator (instruction: "Add battle damage assessment team preparedness exercises and simulation. Again think gamified software or hardware. Followed by real world exercises") + Claude Code (Opus 4.7) executing edits
**Rationale:** Operator added a second scope dimension distinct from the repair-operations training in §11.2: a battle-damage-ASSESSMENT (BDA) team preparedness pipeline using a gamified-software/hardware sim layer for high-frequency reps, transitioning to real-world exercises (embedded BDA-team injects in fleet exercises and Carderock-instrumented test events). BDA is structurally separate from repair: different audience (damage-control / fleet-BDA cells / joint multidomain BDA staff), different cadence (high-frequency reps between live events), different fidelity ramp (sim → live, with the gamified layer providing the rep volume).
**What changed:**
- `index.md` — `capability_tags` +`BDA` and +`serious-games` (now 9 tags).
- `00_research-file.md` §1 — added scope point #5 (BDA team preparedness pipeline; gamified-then-real-world; logical-precedence rationale).
- `00_research-file.md` §2 — new "BDA team preparedness questions" block with two `[DISCONFIRMING]` items (existing DoD-funded BDA serious-game maturity; BDA training already embedded in fleet exercises at depth that closes the gap).
- `00_research-file.md` §7 — hypothesis expanded from five to six falsifiable legs; new leg-6 = "BDA-preparedness pipeline viability" with three falsifier conditions (existing product saturation; existing fleet-exercise embed depth; OSI-fidelity sim realism).
- `00_research-file.md` §11.2 — retitled "Training-progression design — repair operations" and added pointer to new §11.3 for the BDA-team pipeline.
- `00_research-file.md` §11.3 (new) — "BDA team preparedness — gamified-then-real-world progression" with Phase 1 (sim layer: software platforms, hardware-in-the-loop, gamification mechanics, audience scoping), Phase 2 (real-world: embedded injects in COMPTUEX / RIMPAC / LSE / ANTX / Trident Warrior plus Carderock-instrumented controlled events plus joint red-team / blue-team evolutions), progression-order rationale (sim-first because high-frequency reps are the engine of skill retention), differentiator-hook check (ARKA EO/IR signature libraries), and disconfirming checks cross-listed in §2.
- `00_research-file.md` §11.3 timeline → renumbered to §11.4; §11.4 risks → renumbered to §11.5. Two new rows added to the §11.5 risk table: incumbent saturation in the BDA-serious-game space; sim-vs-live progression-order risk if Navy training authorities invert the order.
- `_search-config.yaml` — inserted four new Week 1 disconfirming-evidence AI queries for §7-leg-6 (NWDC BDA training pipeline; SBIR Phase II/III BDA serious games; COMPTUEX/RIMPAC/LSE BDA injects; I/ITSEC vendor coverage). Added three more AI queries in the Week 2/3 broadening band for the BDA-platform vendor landscape (VBS4; MAK ONE; NPS thesis library). Added three SAM searches (BDA training simulation; serious game damage control; AR/VR damage control). Added four USAspending searches (BDA + training keywords; serious game + Navy; recipient = Bohemia Interactive Simulations; recipient = MAK Technologies).

**Open before `find_sources.py` first run** (unchanged from prior entry, plus one new item):
- Original two open items (scope-of-first-pass; query ordering) still stand.
- Confirm whether the four new §7-leg-6 disconfirming queries (now slotted as Week 1 queries 6-9 in the AI list) should run in the same first pass as the original disconfirming queries 1-5, or be deferred to a second pass.

---

### 2026-05-21 — First `find_sources.py` pass executed (all 22 AI / 8 SAM / 9 USAspending queries)

**By:** operator (instruction: "1 all / 2 sure....? / 3 yes?") + Claude Code (Opus 4.7) executing the script
**Rationale:** Operator authorized running ALL queries on the first pass (per the three open items in the previous log entry). `_scripts/find_sources.py --opportunity BDR-FLEET-READINESS` invoked via the project venv.
**Result:** 67 new candidates queued in `_inbox.md` — **42 AI + 25 SAM + 0 USAspending**.

**AI score distribution (42 ranked candidates, OpenAI scoring 1-10):**
- 9/10 — 1 candidate
- 8/10 — 13 candidates
- 7/10 — 14 candidates
- 6/10 — 5 candidates
- 5/10 — 9 candidates

**Top hit (9/10):**
- SRF-JRMC SWARMEX — Ship Repair Facility Japan Regional Maintenance Center, first wartime ship-repair-and-maintenance exercise (NAVSEA Public Affairs primary source, `navsea.navy.mil`). This is load-bearing for §7-leg-1 (training-assumption gap) AND §11.3-Phase-2 (real-world exercises) — partial falsifier candidate for the hypothesis that "the Navy doesn't already exercise wartime repair," depending on scope. **Read first.**

**Notable 8/10 cluster:**
- GAO-26-109068 "Navy and Coast Guard Shipbuilding" (testimony + PDF + product page — 3 URL variants for the same product; dedup opportunity).
- Navy Shipbuilding Plan 2025-2026 transcript (`defense.gov`) — Amphibious Force Readiness Board chaired by VCNO.
- ESG-2 dynamic exercise (DVIDS, May 2026) — TTX with realistic injects + C2 stress testing; relevant to §11.3 real-world exercises.
- MHI $111M NAVSEA ship-repair contract (GovConWire) — Navy ship-repair vehicle exemplar.

**Query coverage signals (zero-hit BDA queries are themselves data):**
- The four §7-leg-6 disconfirming queries (BDA pipeline / SBIR Phase II-III BDA / I/ITSEC vendor / Bohemia / NPS thesis) returned **almost nothing** at high score. Only 1 hit on the COMPTUEX/RIMPAC/LSE BDA-inject query and 2 hits on MAK ONE. **Interpretation (Assessment, not finding):** AI-search did not surface a saturated DoD-funded BDA serious-game / sim-product market for these specific phrasings. That is WEAK evidence the BDA-pipeline space (§11.3) is NOT pre-saturated — but it is NOT strong: re-query with different phrasings is needed before the leg-6-(a) falsifier is closed.

**SAM coverage:** All 25 SAM hits came from the single "NSWC Carderock" keyword query. The next 7 SAM queries returned dedup-zero or empty. That's expected (Carderock SBIR/STTR topic feed is the dominant SAM signal).

**USAspending status — API outage, NOT a config bug:**
- The first query (`ship repair` + recipient `PAE Applied Technologies` + 2023-01-01 start) returned 0 candidates normally.
- All subsequent 8 queries returned **HTTP 500** from USAspending.gov. This is a server-side issue (the API was healthy when we verified the Deloitte INDOPACOM Alpha PIID earlier in PMTEC work). **Action: retry USAspending pass once the API is healthy.**

**Source-quality observation (for inbox triage):**
- Strong primary tier: NAVSEA (5), GAO (4), defense.gov (2), navy.mil (2), navysbir.com (2), DVIDS (1), CBO (1).
- Tier-3 advocacy / think tank: CSIS (1), Stimson (1).
- Tier-4 trade press: GovConWire (2), Euro-SD (2), DefenseTechAndAcquisition (1), 19fortyfive (1).
- Watch for credibility-tier issues: `rmcglobal.com`, `list25.com`, `shipuniverse.com` showed up at 8/10 — these are private analysis sites and need click-verify per SOP rule 6 before any FACT use.

**Next operator step:**
- Tap inbox checkboxes in Obsidian to approve the 9/10 SWARMEX item and the 8/10 primary-tier items first (focus on the disconfirming threads: SWARMEX falsifier check, GAO-26-109068, Navy Shipbuilding Plan transcript), then run `python _scripts/approve_inbox.py BDR-FLEET-READINESS` to ingest.
- After ingest, re-verify §7 leg-1 (training-assumption gap) against the SWARMEX article specifically — that's the highest-leverage disconfirming check from this pass.

---

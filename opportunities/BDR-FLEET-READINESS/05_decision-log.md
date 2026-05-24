# BDR-FLEET-READINESS — Decision Log

Every decision: date, decision, by whom, rationale, what changed.

---

### 2026-05-25 — Pre-pass corpus cleanup executed via iterated Gemini Pro red-team dialogue

**By:** operator (instruction "Before we do that pass, let's review and make sure we aren't still propagating old, inaccurate or misunderstood facts and sources into corpus. Clean all garbage and fix stale docs then run the pass. All garbage cleaning and stale docs need to be part of a red team iterate dialog session.") + Claude Code (Opus 4.7) executing the cleanup against the converged plan + Gemini Pro (Google) reviewing the cleanup inventory across two rounds.

**Rationale:** Yesterday's right-to-win-reframe dialogue (separate decision log entry, 2026-05-25) surfaced an alternative training-systems procurement-chain hypothesis to test against the prior NAVSEA / Carderock framing. Running the next find_sources pass without first cleaning out the stale framing would source-ground new claims on top of a partly-invalidated analytical foundation, producing contradictions inside the vault. The operator required the cleanup itself to go through the iterated cross-AI red-team discipline so that staleness was identified by adversarial review rather than by Claude's unaided judgment.

**What changed:**

- **Iterated dialogue file added** at `_red-teams/2026-05-25-gemini-pro-corpus-cleanup-dialogue.md`. Two rounds. Claude proposed a 13-item cleanup inventory; Gemini reviewed, classified, and surfaced two missing items (LVC scope-restriction; BDAR capability-gap framing). Claude pushed back on three Gemini Round-1 adjustments; Gemini conceded all three. The three Claude pushbacks that landed: (1) Carderock = ship-survivability modeling source vs. NWDC = BDAR doctrine writer — a two-organization split replaces Gemini's "Doctrine/T&E origin point" overstatement; (2) §1 working summary Thread 4 rewrites to "pivot-point" framing without naming the alternative-hypothesis entities — preserves the named-contractor discipline against Gemini's proposal to hard-code NETC/NAWCTSD into §1 before source ingestion; (3) BDAR capability-gap framing added to glossary entries WITH an explicit `[Structural Inference (Gemini Pro red-team, 2026-05-25) — Pending Source-Grounding]` tag rather than as a bare fact.

- **Block 1 (pre-pass must-do) executed.** `_search-config.yaml` updated — added BDAR/BDAT-targeted queries for the dialogue-surfaced buyer triad (NETC, NAWCTSD, SWSC, NWDC, ATG, NCTE, RRL, STAVE, SMMTT, NSST) with inline notes that the queries are TESTING-not-ASSERTING the dialogue's claims; off-scope shipbuilding queries removed. §1 working summary Thread 4 rewritten to "pivot-point" framing without naming new entities. §1 SWARMEX framing softened from "visible most clearly" to "publicly signaled" with press-release-versus-capability-building ambiguity note. BDAR definition updated in both the per-opportunity `_glossary.md` and the vault-wide `_meta/glossary.md` with the capability-gap framing under the structural-inference tag.

- **Block 2 (pre-pass fast quarantines) executed.** Scope notes added at the top of §3 (Demand signal), §4 (Customer landscape), and §11.1 (Engagement-surface inventory) flagging the prior-NAVSEA/Carderock framing as under reconsideration vs. the alternative training-systems-chain hypothesis. Stimson MSMRO citations in §3.1, §4.5, and §5.3 carry explicit "context-level, not load-bearing" qualifiers. §7 leg 5 refined — HII Mission Technologies specifically as the dialogue-surfaced NCTE network-architecture prime (still to be source-grounded); SAIC and Leidos remain broader canonical-incumbents with BDAR-relevant footprints not yet sourced. LVC scope note added to the acronym table and §11.3 restricting LVC to NCTE-compliant Fleet Synthetic Training architecture, not generic AR/VR. Phoenix Group of Virginia damage-control SkillBridge source carries a downgrade note inside the source file itself — evidence for DC-adjacent contractor base, not BDAR/BDAT procurement signal.

- **Block 3 (deep cleans) executed.** §11.2 re-scoped with the Carderock/NWDC split — Carderock = survivability modeling source for scenario inputs; NWDC = BDAR doctrine writer (NTTPs, TACMEMOs); SWESC and wet trainers (USS Buttercup, USS Trayer) = hands-on damage-control venues. SIMA per-opportunity glossary entry carries an `[Prior Hypothesis: SIMA as contractor entry point. Status: Invalidated by 2026-05-24 dialogue]` breadcrumb. §5.1 shipbuilders treatment re-framed as the **Platform-Sustainment Bundling Hypothesis** (BDAR/BDAT training bundles into existing platform-sustainment contracts) versus the **NAWCTSD Training-Prime Hypothesis** (BDAR/BDAT procures separately through the training-systems chain), with both labeled unverified and slated for testing in the next find_sources pass.

- **Over-cleaning safeguards preserved.** Past decision log entries are append-only — no retroactive edits. The prior NAVSEA / industrial-base hypothesis is not deleted; it is quarantined via scope notes and breadcrumbs that retain the analytical lineage. New entities surfaced in the right-to-win-reframe dialogue (NETC, NAWCTSD, SWSC, etc.) remain absent from analytical content as FACT claims; they appear only in `_search-config.yaml` queries (testing-not-asserting), in the BDAR definition's structural-inference tag, in decision log narrative, and in the dialogue files. They become vault-citable only after a find_sources pass produces ingested primary sources naming them.

**What this enables:** the corpus is now ready for the next find_sources pass against the refreshed `_search-config.yaml` queries. The pass tests both the prior NAVSEA / Carderock framing and the alternative training-systems-chain hypothesis. The named-contractor discipline at `_meta/feedback_named_contractor_discipline.md` is preserved throughout — the alternative-hypothesis entities are not pre-installed as ground truth before the empirical test runs.

**Cross-references:** `_red-teams/2026-05-25-gemini-pro-corpus-cleanup-dialogue.md` (this session's dialogue), `_red-teams/2026-05-25-gemini-pro-right-to-win-reframe-dialogue.md` (yesterday's reframe dialogue), `_meta/feedback_named_contractor_discipline.md` (the discipline Claude weaponized against Gemini's Pushback-2 entity proposal).

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

### 2026-05-22 — Research paused for readability fix and workflow review

The operator paused all active research on this track. The pause is not a kill signal; it is a deliberate break to fix two things before the inbox triage continues.

**By:** operator, who told me the chat responses and the research files themselves were "laden with symbols and acronyms and references to parts that a human reader has long since forgotten." The operator asked for (a) a structural readability fix that applies to every file and every chat response going forward, and (b) a workflow review based on a Medium article by Yanli Liu titled *Code Is Not Cheap: How to Multiply Your AI's Output With Software Fundamentals*.

**What is paused:**
- The `auto_find` flag in `index.md` is set back to `false` so the cron will not pull new candidates while the pause is active.
- The 67 candidates already in `_inbox.md` from the 2026-05-21 first pass remain queued but untriaged. They are not lost; they will be the first thing the operator triages on resume.
- No further `find_sources.py`, `ingest.py`, `verify_facts.py`, or `red_team.py` runs against this track until the pause lifts.

**What is happening during the pause:**
1. A new "Writing for the human reader" section was added to the project `CLAUDE.md` so the readability rule is binding on every future session.
2. A `feedback_readability.md` memory was saved in the Claude Code auto-memory so the rule survives across sessions even if the `CLAUDE.md` rule is later reorganized.
3. A readability pass is being applied to this research file and this decision log so the operator can read them on first encounter without holding the section structure in their head.
4. The Yanli Liu article is being read so that any process-level lessons can be folded into the vault workflow (scripts, prompts, SOP) before more research is generated under the old workflow.

**What resumes the research:**
- Operator flips `auto_find` back to `true` in `index.md`, OR
- Operator runs `approve_inbox.py BDR-FLEET-READINESS` to start triaging the queued candidates.

Either action signals that the pause is lifted.

---

### 2026-05-23 — First inbox triage + ingest pass; Playwright fallback wired; section 3 populated

The operator approved 19 inbox candidates and the ingest pipeline produced 14 source files in `01_sources/`. After the second pass against re-tried URLs:

**14 source files written.** Eight are substantive primary or secondary sources — both April 2026 GAO reports (Navy and Coast Guard shipbuilding, weapon system sustainment), the Stimson Center US-Japan Task Force on Military Shipbuilding, Maintenance, and Repair Operations (MSMRO) recommendations from April 2026, the CSIS analysis of war-with-China preparedness, a DVIDS article on Expeditionary Strike Group 2 training, the Maritime Administration Port Infrastructure Development Program page, the Navy SBIR/STTR topic DON26TZ01 on corrosion sensing, and the National Tooling and Manufacturing Association advanced-materials page. Three are tier-4 trade-press / private-analysis files (RMC Global, list25, ShipUniverse) that must be click-verified before any FACT claim is drawn from them. Three were ingested as "200 OK" but the actual content is a 404 error page — defense.gov shipbuilding plan transcript, marines.mil MCO 4700.4A, and a ResearchGate URL that pointed at the wrong paper. Those three have been moved to `01_sources/_quarantine/`.

**Five inbox items failed for three distinct reasons** and remain in §8.2 as cited but not yet ingested.

The SRF-JRMC SWARMEX article (the 9/10-ranked top hit from the first source-finder pass) is genuinely dead at `navsea.navy.mil/Media/News/Article/3748283/...` — 404 from both `curl_cffi` and system `curl`, and no Wayback Machine snapshot. Two other NAVSEA Public Affairs article URLs (Vertical Launching System tool 3774844 and Carderock Orion Recovery 3750059) also returned 404. Three NAVSEA 404s on different article IDs suggests a site-pattern change parallel to the `defense.gov → war.gov` migration. Manual recovery is in the operator's queue.

The defense.gov May 2026 Navy Shipbuilding Plan PDF redirects to a war.gov path that returns 404. The transcript version was attempted at a different defense.gov URL; the server returned HTTP 200 with the site's "page not found" body — a 404-rendered-as-200 case that the ingest validation does not catch (because content was non-empty). The MHI $111M GovConWire article returns 403 from Cloudflare even with `curl_cffi` browser-TLS impersonation and the Playwright headless-Chromium fallback. Cloudflare's most aggressive bot-detection tier defeats both layers.

**Playwright fallback landed in the ingest pipeline.** `_scripts/lib/fetchers/playwright_browser.py` is a new fetcher module that launches headless Chromium with `--disable-blink-features=AutomationControlled` and a realistic user-agent string. `_scripts/lib/fetchers/web.py` now calls Playwright as a fallback whenever `curl_cffi` returns 403 or 429 after its retry. Tested live against the GovConWire URL: the fallback triggers correctly, runs Chromium, attempts navigation, and gets a 403 from Cloudflare — same outcome as `curl_cffi`. The architectural layer is in place and will defeat most Akamai-class bot detection; Cloudflare's strongest tier still requires manual download.

**Section 3 of the research file is populated.** 3.1 Stated priorities walks through four independent threads of senior-leadership and oversight signal — Stimson Task Force policy framing, Secretary of the Navy first-foreign-trip choice and congressional direction to assess Western Pacific repair, GAO testimony on shipbuilding cost and schedule failure, and GAO weapon-system sustainment cost growth. 3.2 Funding documents the dollar scale (FY27 PB request over $65 billion in shipbuilding, $40 billion Coast Guard fleet replacement, $550 billion July 2025 US-Japan trade arrangement) and notes that the constraint on this research is procurement-vehicle alignment, not money. 3.3 Engagement mechanism is thin (Navy SBIR topic DON26TZ01 on corrosion sensing, Maritime Administration Port Infrastructure Development Program) and depends on the §11.1 inventory work that is still desk-research-only.

Every claim in section 3 carries a FACT or Assessment label per the SOP and a `[s.2026-05-23-slug]` citation tag. The claims have not been verified against the cited sources by `verify_facts.py` yet — that is the next mechanical step. Some sources are tier 4 (RMC Global, list25, ShipUniverse) and need SOP-rule-6 click-verification before any FACT claim against them can stand.

**Bug to surface (not a blocker).** `_scripts/lib/ledger.py` inserts new citation entries between `## 8. Source ledger` and `## 9. Verification flags`, but it inserts them BELOW the section's closing `---` separator and outside any subsection. The intended target is `### 8.1 Ingested primary sources`. The first batch of entries written today were corralled into 8.1 manually as part of this work; future ingests will need the same cleanup, or `ledger.py` should be patched to write into 8.1 directly. Similarly, `ingest.py` does not detect "200 OK with 404-shaped body" as a failure — needs validation against common page-not-found phrases. Both fixes can wait until friction demands them.

**Second `find_sources` pass started 2026-05-23 with four new targeted queries.** USNI naval repair overseas, SRF-JRMC commanding officer relieved, Pacific Fleet forward sustainment industrial base wartime, and Department of War Navy shipbuilding plan FY27. The USAspending API outage from the first pass is presumed resolved and the second pass will retry those queries. Results land in `_inbox.md` for operator triage.

---

### 2026-05-25 — Five-round iterated Gemini Pro red-team of operator's right-to-win reframe

Operator proposed a substantive reframe of CACI's right-to-win on 2026-05-25: pivot from "CACI as ship-damage simulation platform builder" to "CACI as scenario-based war-game designer and operational training curriculum developer for BDAR/BDAT teams at RMCs, leveraging C4ISR and ARKA strengths." Operator authorized an iterated red-team with up to 10-15 rounds of Claude-challenges-Gemini and Gemini-challenges-Claude, ending in a clean list of unresolved disagreements. Five rounds were sufficient to converge; the full dialogue is captured at `_red-teams/2026-05-25-gemini-pro-right-to-win-reframe-dialogue.md`.

**Round-by-round outcomes:** Round 1 produced Gemini's initial critique (BAH wargaming dominance, SAIC/HII surface training, OCI Biased Ground Rules trap, commoditization). Round 2 had Claude challenge each unsupported assertion; Gemini conceded BAH dominance (BDAR is white space), OCI trap (mitigable under FAR 9.5), commoditization (C4ISR + ARKA + tech-enabled delivery is genuinely differentiated). Round 3 had Claude demand verification of the still-asserted SAIC FDTPS contract and the HII NCTE claim; Gemini conceded FDTPS as a hallucination/mashup, conceded that white-space-vs-competitive-territory means CACI can bid as prime on SeaPort-NxG / NAWCTSD vehicles, conceded Element 7 (foreign-port procurement planning) is valid training audience-alignment, conceded RMC-budget inference and surfaced multiple alternative funding paths (DIU CSO, NavalX, PACFLT). Round 4 had Claude demand truth-labeling; Gemini produced verifiable evidence for NCTE/HII (specific contract values), Ready, Relevant Learning (NETC program of record), NAWCTSD as surface-and-subsurface training execution authority (executing STAVE and SMMTT), and the buyer-triad pattern (post-Fitzgerald/McCain NSST upgrades as historical analog). Round 5 had Gemini steelman the kill-case using only verified facts and surface remaining nagging concerns.

**Outcome — no residual Claude/Gemini disagreements after five rounds.** The dialogue converged completely. Gemini conceded substantially on every critique that rested on un-evidenced incumbency or competitive moats. What remains is empirical questions (three open research questions for operator-side verification), strategic decisions (three kill-case requirements for any forward capture plan), and scope concerns (three nagging structural items). All require operator-side resolution, not further AI dialogue.

**Most consequential verified findings:**

- **NCTE (Navy Continuous Training Environment)** is a real program with HII Mission Technologies as prime via the Alion acquisition. Specific contract values: $772M 2018 award, $274M 2023 task order at NSWC Corona. Scope is the network backbone for Fleet Synthetic Training (not "all" Navy LVC as Gemini initially overstated). HLA/DIS standards-based — meaning third-party plug-ins are technically possible but face standard ATO/RMF queue managed by the incumbent.
- **NAWCTSD is the surface and subsurface training-systems execution authority**, not just aviation. Executes STAVE (Surface Training Advanced Virtual Environment) for SWSC and SMMTT (Submarine Multi-Mission Team Trainer). Acts on behalf of NETC and SWSC requirements, not in a vacuum. This corrects Gemini's Round 1 overstatement of NAWCTSD as "sole" training buyer and the operator's correct push-back yesterday.
- **The buyer-triad pattern** (Fleet sponsor + NETC curriculum requirement + NAWCTSD execution vehicle) has a verified historical analog: the post-Fitzgerald/McCain Navigation, Seamanship, and Shiphandling Trainer (NSST) upgrades from 2017+. PACFLT/USFF urgency → SWSC/NETC requirement rewrite → NAWCTSD contract execution.

**Three open research questions for operator verification:**

1. Who is the actual Operational Sponsor for BDAR? PACFLT N4 (Logistics/Maintenance), NAVSEA Code 05 (Engineering), NECC (Expeditionary), or someone else?
2. Does a Master Training Task List for BDAR currently exist within NETC/RRL? If yes, the work can sell through NAWCTSD now. If no, the operator faces a year-long requirements-definition lobbying effort.
3. Is the target an NCTE network integration or a standalone STAVE schoolhouse deployment? This single decision dictates the engineering roadmap, the HII teaming question, and the ATO/RMF risk profile.

**Three kill-case requirements that any forward capture plan must answer:**

1. Scope/Over-engineering Trap — networked LVC vs. standalone schoolhouse trainer.
2. Prime Vehicle Trap — why doesn't the work get ECP'd to HII as the NCTE prime?
3. Timeline/Funding Trap — what funded Program Element makes NAWCTSD able to buy this?

**Three nagging structural concerns:**

1. The Physics of BDAR — XR is plausibly strong for Assessment but likely weak for Repair (which is physical/tactile, traditionally trained on wet trainers like USS Buttercup and USS Trayer). Scope may need to narrow to the BDA side.
2. The ATO / RMF accreditation timeline (12-24 months for new training systems on Navy networks).
3. The Hardware Agnosticism Paradox — NAWCTSD training contracts often bundle software + hardware, which would force CACI into hardware reseller and lifecycle-manager roles.

**Recommended next moves before §7 rewrite:**

- Run a targeted find_sources pass against the named research targets (NCTE, RRL, STAVE, SMMTT, NSST, JSAF, NAWCTSD charters, NETC/SWSC/NWDC org structure). These cannot enter analytical content until ingested.
- Resolve the network-vs-standalone scope question. If standalone STAVE, the §7 hypothesis simplifies dramatically. If NCTE integration, the HII teaming question becomes load-bearing.
- Identify the BDAR operational sponsor with a funded line. Without one, the rest of the analysis is academic.

**Process discipline observation:** the iterated red-team pattern produced substantially more analytical value than the single-pass red-team from 2026-05-24. The single pass surfaced concerns (some valid, some hallucinated). The five-round iteration separated verified facts from unverified assertions, killed the SAIC FDTPS hallucination, corrected the NAWCTSD overstatement, and produced a clean operator decision artifact with three kinds of unresolved items (empirical, strategic, scope). Going forward, every analytical reframe that would land in the research file should run through this iterated pattern before §7 / §3 / §4 / §5 get rewritten.

---

### 2026-05-24 — Gemini Pro red-team of §7 hypothesis surfaces material analytical errors

Operator flagged that the small-ships workflow's per-section red-team discipline had been ignored across §3 / §4 / §5 drafting and the §7 hypothesis refocus. Ran the first cross-AI red-team on §7 using Gemini Pro with the cross-ai-red-team.md three-persona prompt structure (Navy customer reviewer, competitor analyst, skeptical exec). Full output captured at `_red-teams/2026-05-24-gemini-pro-section-7-hypothesis.md`.

**The catch that most invalidates current analytical content:** the Navy's actual contracting center for simulators, serious games, and training pipelines is NAWCTSD (Naval Air Warfare Center Training Systems Division, Orlando) — not NAVSEA or NSWC Carderock. The §3 customer-landscape and §5 competitive-landscape sections have been drafted around the wrong customer organization. Carderock is R&D and T&E (specifically LFT&E — Live Fire Test & Evaluation), not a schoolhouse. The §11.2 BDAR repair-side training pipeline names Carderock as a candidate site for hands-on instrumented-test-bed training; per Gemini, the actual Navy training infrastructure for damage-control is wet trainers (e.g., the "Buttercup" trainer), ex-service hulks, RMCs, public shipyards, and Surface Warfare Engineering Schools Command (SWESC). Multiple analytical corrections are required.

**Three disconfirming threads Gemini surfaced that the §7 hypothesis missed entirely:**

1. The Technical Data Package (TDP) / data-rights wall. Cannot train assessment teams on a specific ship class without OEM shipbuilder ship-blueprint data, which is tightly controlled by NAVSEA and OEMs. CACI has no path to access this data.
2. NAWCTSD is the actual buyer for training systems, not NAVSEA. This is the structural scope error noted above.
3. Teaming necessity. CACI's gap in maritime deckplate experience means a prime-position bid is not credible. The research has to add a teaming-feasibility leg.

**The single most important Gemini critique to address before further investment:** "Does CACI actually have a right-to-win here, or is this just an interesting Navy problem?" If CACI's plausible role is "build the network architecture / data pipeline / scenario engine that someone else's training program runs on" (leveraging CACI's actual C4ISR / cyber / enterprise-IT strengths), that's a fundamentally different opportunity shape than the current §7 hypothesis assumes. The hypothesis as written points at a ship-repair training capability that CACI does not credibly have the deckplate experience to deliver.

**Named entities Gemini surfaced that are NOT yet source-grounded:** NAWCTSD, MOTISS (the legacy ship-damage simulation model), SURFMEPP, TTGP (Tactical Training Group Pacific), TTGL (Atlantic), FST (Fleet Synthetic Training), SWESC, GDIT (as FST incumbent), Buttercup (wet trainer), SeaPort-NxG, NAVSEA Code 04 / Code 05, NAVSEA-OEM teaming agreements. Per the named-contractor discipline at `_meta/feedback_named_contractor_discipline.md`, none of these can enter the analytical research file as FACT claims yet. They are the priority targets for the next find_sources pass — particularly NAWCTSD, which may reorient the entire research direction.

**Recommended next moves (per the red-team file, deferred for operator decision):**

1. Fix §11.2 to remove Carderock-as-hands-on-test-bed framing; replace with Navy wet-trainer / hulk / schoolhouse infrastructure once source-verified.
2. Refocus §7 leg 3 to make explicit that Carderock is a modeling SOURCE, not a training VENUE.
3. Add a new §7 leg 7 (teaming feasibility) — explicit falsifier on whether CACI can secure a prime / sub relationship with HII, GD, or a maritime firm.
4. Reframe §7 leg 1 (demand gap) to be specific about WHICH gap is being signaled — Gemini reads SIMA stand-up as industrial-workforce capacity, not training-content gap.
5. Target the next find_sources pass at NAWCTSD specifically.
6. Pause further analytical drafting on §3 / §4 / §5 until §7 is reshaped. The current §3-§5 target the wrong customer organization.

**Process lesson recorded:** every drafting session that adds analytical content (FACT claims, scope statements, hypothesis modifications) should run a cross-AI red-team before that content lands in the research file. The small-ships workflow's per-section red-team step exists for exactly this reason; we ignored it for §3, §4, §5, the §7 refocus, and the §11 reframe. The cost of the discipline is ~5 minutes of Gemini quota per section; the cost of skipping it is shown by this red-team — several analytical positions need rework now that we've spent days operating on incorrect framings.

---

### 2026-05-24 — Section 7 hypothesis legs refocused on BDAR/BDAT scope; OCI primer captured

Two changes following the BDAR/BDAT scope narrowing and the brainstorming session.

**Section 7 hypothesis legs rewritten** to match the BDAR/BDAT-and-training-simulation-exercises scope. The prior six-leg framing was broader BDR / industrial-base; the refocused six legs are: (1) the BDAR/BDAT training-and-simulation demand gap; (2) the procurement-path reality — Navy is acquiring this through contractors not solely organically; (3) NSWC Carderock unclassified modeling fidelity; (4) BDAR repair-side training-progression viability; (5) relationship feasibility — CACI can be positioned at the right Navy organizations, framed at the general competitive level without operator-side knowledge entering the leg; (6) BDAT training-pipeline viability — gamified-sim plus real-world-exercise model is not already saturated. Each leg retains the falsifier structure and is testable against public sources. The "industrial-planning gap" leg from the prior framing is replaced by the new "procurement-path reality" leg, which is the BDAR/BDAT-specific analog.

**OCI primer captured at `_meta/oci-primer.md`** as a vault-wide reference. The primer covers the three flavors of Organizational Conflict of Interest (unequal access to information, biased ground rules, impaired objectivity), the standard four-component mitigation pattern (documented organizational firewall, public-information-only proposal content, formal disclosure to the contracting officer, written letter authorizing the bid), how the vault's existing disciplines map to OCI hygiene, what to clear with contractor contracts and legal teams before any bid work, and where the OCI rule does NOT apply. The primer is referenced from section 7 leg 5 as the discipline that governs how operator-side knowledge about CACI's current contract footprint stays out of analytical content. CLAUDE.md was updated to point at the primer.

The primer is intentionally vault-wide rather than BDR-specific because the OCI discipline applies to every opportunity in the vault. Future opportunity scaffolds can reference the primer without needing to re-explain the concept.

---

### 2026-05-24 — Scope tightened to BDAR + BDAT (training, simulation, exercises); MHI scrubbed

Operator narrowed the research scope to two pillars: Battle Damage Assessment and Repair (BDAR) and Battle Damage Assessment Team (BDAT), specifically in the training, simulation, and exercises space. The earlier broader "BDR" framing included industrial-base, shipbuilding-capacity, and ship-repair contracting threads that are now out of load-bearing scope.

**What this changes in the research direction:**

- The recommendation, when it comes, will be specifically about BDAR/BDAT training, simulation, and exercise products and services — not about ship-repair industrial-base policy.
- The two load-bearing sections of the research are now §11.2 (BDAR repair-side training pipeline) and §11.3 (BDAT training pipeline). Both already existed under different titles and have been renamed.
- The primary-source language that anchors the new scope is two specific claims that are already ingested: (a) the SRF-JRMC SWARMEX press release framing the program as "Forward Deployed Ship Repair Teams (FDSRT) in battle damage assessment and repair," and (b) CNO Caudle's 14 May 2026 HASC testimony framing the Norfolk and San Diego SIMA stand-up as "hands-on training in advanced ship repair" using AI/ML, advanced manufacturing, workflow monitoring, and robotic systems.

**What is now out of scope:**

- The broader ship-repair industrial base picture.
- Shipbuilding capacity and the 64-ship shortfall between current battle force and the statutory 355-ship requirement.
- Private ship-repair contractor competition for Navy maintenance dollars.
- The U.S.-Japan shipbuilding industrial partnership thread (Stimson MSMRO Task Force).
- Surge-repair capacity planning at scale.

Material on these threads remains in §3, §4, and §5 of this file as background context. If subsequent research surfaces evidence that BDAR/BDAT training is being acquired through one of these broader vehicles, the relevant context material will get pulled forward into the recommendation.

**What changed in the files:**

- `_meta/glossary.md` — added BDAR and BDAT as formal terms; tightened BDR and BDA definitions to point at the new umbrella.
- `_glossary.md` (per-opportunity) — added BDAR, BDAT, FDSRT, SWARMEX, SIMA, and SIOP as active entries with last-verified dates.
- `00_research-file.md` acronym table — added BDAR, BDAT, FDSRT, SIMA, SIOP; clarified that BDR is superseded by BDAR as the primary scope frame.
- `00_research-file.md` §1 working summary — rewritten to use BDAR/BDAT framing, narrowed from five threads to four (the prior "gap on either side of modeling" thread split into training-and-simulation-specific questions), and explicit out-of-scope statement.
- `00_research-file.md` §11.2 — renamed to "BDAR repair-side training pipeline" (was "Repair-team training").
- `00_research-file.md` §11.3 — renamed to "BDAT training pipeline" (was "Damage-assessment team training").
- The folder ID `BDR-FLEET-READINESS` is unchanged. Folder names are stable identifiers; the prose inside uses the new BDAR/BDAT framing.

**Deferred edits:** §7 hypothesis legs were written in the broader BDR framing and need refocusing on training/simulation/exercises specifically. §3 demand signal, §4 customer landscape, and §5 competitive landscape contain substantial material that is now context-level rather than recommendation-level — they don't need to be torn down but may benefit from a "see also" pointer to the new scope frame. §10 research plan should be re-prioritized to target BDAR/BDAT-specific sources first. These edits can wait until the operator picks them up.

**MHI scrubbed.** The operator confirmed on 2026-05-24 that the GovConWire article on the MHI $111M ship-repair contract is not applicable to the BDAR/BDAT scope, even at the meta-context level it was being preserved in §8.2. MHI was removed from the per-opportunity allowlist; §8.2 was rewritten to describe the Cloudflare-protected ingest failure without naming MHI; the inbox entry was moved to `_rejected.md` with rejection reason "out-of-scope-bdar-bdat — Operator-rejected 2026-05-24."

---

### 2026-05-23 — Section 4 (Customer landscape) and Section 5 (Competitive landscape) populated from ingested sources

Both sections drafted under the named-contractor discipline and verified by both audits before sync.

**Section 4 (Customer landscape) — six subsections drawn from primary sources.**

4.1 Senior leadership names Hung Cao (Acting SECNAV), Admiral Daryl Caudle (34th CNO), General Eric M. Smith (39th CMC), and Secretary of Navy John Phelan — all from the May 2026 Shipbuilding Plan and the Stimson Task Force recommendations. 4.2 covers the NAVSEA organizational structure consolidated under PAE Industrial Operations, with the four public Navy shipyards named per Caudle's testimony: Pearl Harbor Naval Shipyard (PHNS), Puget Sound Naval Shipyard (PSNS), Portsmouth Naval Shipyard (PNSY), and Norfolk Naval Shipyard (NNSY). 4.3 frames NSWC Carderock as the modeling-source customer with leadership still a research target. 4.4 covers OPNAV/N9 demand-side framing per Caudle's four-priority structure (Lethal & Effective Force; Total Force Readiness; Capable & Resilient Warfighter; Industrial & Logistics Capacity). 4.5 covers the Pacific Fleet engagement layer — SRF-JRMC, SWARMEX, JMSDF, JMU, and the Stimson Task Force co-leads (Andrew Oros, Steve Brock). 4.6 records the Maritime Action Plan governance (DoC lead, DoN advisory) and notes the defense.gov → war.gov migration's operational consequence for source ingestion. 4.7 closes with an Assessment of the three customer-landscape layers (strategic, execution, demand) and ties back to the §9.3 contact-protection discipline.

**Section 5 (Competitive landscape) — five subsections.**

5.1 lists the new-construction shipbuilders named in the May 2026 Shipbuilding Plan with their specific program assignments: Huntington Ingalls Industries (LPD-17 Flight II via Ingalls; wage increases at Newport News), General Dynamics NASSCO (T-AO 205 class, 20 ships planned), Electric Boat (workforce wage increases), Bollinger (first LSM hull), Fincantieri Marinette Marine (LSM hulls 2-5), Austal USA (T-AGOS 25 class, 10 ships). 5.2 documents the operator-allowlisted naval modeling-and-simulation incumbents from §7 leg 5 (SAIC, Leidos, HII Mission Technologies) with explicit Assessment flags that specific capability claims about any of them remain open research. 5.3 covers the international partnership thread — Japan Maritime United, JMSDF, the broader Japanese shipbuilding industry, the $550B July 2025 trade arrangement. 5.4 documents what the section explicitly does not yet know — private U.S. ship-repair contractor mix, Carderock-adjacent technical-partner contract footprints, commercial simulation-platform vendors for any future BDA pipeline. 5.5 closes with the Assessment that the competitive picture is unsharp at the ship-repair and modeling-and-simulation layers (which is where any BDR recommendation would compete) and identifies the next targeted source-ingestion moves.

**Two small source-file updates supporting the §4 + §5 work.** The Navy May 2026 Shipbuilding Plan source-companion markdown gained three verbatim passages I had previously excluded — the LSM section (page 28, naming Bollinger and Fincantieri Marinette Marine), the T-AO 205 section (page 31-32, naming General Dynamics NASSCO with the 20-ship plan), and the T-AGOS 25 section (page 33, naming Austal USA). These were already in the PDF binary at `01_sources/2026-05-23_navy-mil_navy-shipbuilding-plan-may-2026.pdf` but had not been extracted into the searchable markdown summary; without the markdown extraction, the entity audit could not see the source backing.

**Both audits PASS after the work:** `audit_named_entities.py` 0 contaminated / 7 allowlisted / source-only set updated; `audit_search_config.py` 0 contaminated. The new entries in the source-only bucket are Japan Maritime United (the full name; JMU short form is now in writing) and GD NASSCO (shorthand appears once in §5.5 wording — handled by using the full name "General Dynamics NASSCO" in the actual claim).

**Section 6 (Our fit) is the natural next analytical move.** It requires more Assessment synthesis than §4 or §5 because it maps CACI / ARKA capabilities against the demand signals in §3 and the competitive picture in §5. Deferred to the next pass.

---

### 2026-05-23 — Full entity-pollution triage executed; both audits PASS

Following the audit-tooling build and the prior Amentum cleanup, the operator approved a four-part triage of the remaining 23 contaminated entries flagged by `_scripts/audit_named_entities.py`.

**Action 1 — Audit-code scope fix.** `audit_named_entities.py` was modified to exclude `05_decision-log.md` from the analytical-content scope. The decision log is append-only historical record, and naming an entity in the context of recounting past work (e.g., "the prior Amentum confusion") is appropriate use, not contamination. This cleared three flagged entries (Amentum, Deloitte, PAE Applied Technologies) that were over-flagged because they appeared in historical log entries.

**Action 2 — Allowlist three canonical incumbents.** SAIC, Leidos, and HII Mission Technologies were added to the per-opportunity allowlist with the reason "Canonical naval-services incumbent. Operator-blessed for §7 hypothesis leg 5 — Carderock-adjacent technical partner whose existing relationships shape CACI's entry timeline. Specific claims about [entity] capability still need source backing." The hypothesis leg 5 falsifier condition (that these three incumbents could lock CACI out of Carderock) is load-bearing for the research and the entities are too canonical to require source pre-discovery.

**Action 3 — Strip pre-named entities from §5, §11.2, §11.3, and the search config.** 16 entries removed by deliberate excision: the §5 competitive-landscape placeholder (BAE Systems, Booz Allen, Alion), the §11.2 candidate site-visit facility list (HII Newport News, BAE Norfolk, GD NASSCO, Vigor, Titan Acquisitions), and the §11.3 candidate simulation platform list (Bohemia Interactive Simulations, BISim, VBS4, MAK ONE, MAK Technologies, VR-Forces, NVIDIA Omniverse, Improbable). The §7 hypothesis leg 5 prose was edited to remove "Alion-inheritance" wording. Four contaminated search-config queries were removed: two AI queries naming BISim/VBS4 and MAK ONE/VR-Forces, and two USAspending recipient queries (Bohemia Interactive Simulations, MAK Technologies). All affected sections were rewritten to use generic capability or organization language with the note "specific contractor names added only as ingested sources surface them." The declined entities were recorded in a documented-removal section at the bottom of `_entity-allowlist.yaml` so a future analyst doesn't re-introduce them without a source.

**Action 4 — Move 4 contaminated inbox entries to `_rejected.md`.** Inbox entries that came from the now-removed BISim/VBS4/MAK platform queries were moved to `_rejected.md` with reason "Analyst-seeded simulation-platform query (BISim/VBS4/MAK) — not source-surfaced organically; removed 2026-05-23." The rejected list is sticky and these URLs will not be re-queued by future `find_sources` runs.

**Two further allowlist entries added for historical-context cases:** Amentum and MHI. Both appeared only in meta-context (a search-config comment documenting Amentum's removal, and §8.2 of the research file documenting a failed GovConWire ingest). Allowlisted with explicit reasons explaining that these are NOT active analytical claims; if the situations resolve (e.g., a primary source for the MHI contract is found), the allowlist entries should be re-evaluated.

**Audit state after triage:**

- `audit_named_entities.py --opportunity BDR-FLEET-READINESS` → **PASS** (0 contaminated, 5 allowlisted, 2 ok, 8 source-only).
- `audit_search_config.py --opportunity BDR-FLEET-READINESS` → **PASS** (0 contaminated queries, 45 total queries, 12 allowlisted entities).

The 8 source-only entities (Huntington Ingalls Industries, Newport News Shipbuilding, General Dynamics NASSCO, Ingalls Shipbuilding, Japan Maritime United, General Dynamics, Bollinger, JMU) are entities that appear in ingested sources but not yet in analytical content. These are eligible to be written into analytical prose with citation when relevant — the source-only bucket is informational, not contaminated.

---

### 2026-05-23 — Named-contractor discipline: do not introduce names unless sources do

Operator clarified that specific commercial contractor names should not appear in vault analytical content unless they surface organically in ingested sources. The vault was previously naming "Amentum" as the industrial-supply-side actor across the research file, glossary, points-of-contact directory, index.md frontmatter, and source-file notes — but a grep of the 13 ingested source files confirmed that Amentum appears in exactly zero of them. Every Amentum reference in the vault was analyst-introduced, not source-supported.

What changed:

- `_meta/glossary.md` — the Amentum entry was removed entirely. The PAE-IO entry was simplified to no longer reference Amentum in the negation ("not an Amentum subsidiary" framing dropped because that requires naming Amentum to say it isn't).
- `00_research-file.md` header `Customer:` field — "PAE-IO / Amentum as industrial supply-side" rewritten to "the Navy's PAE Industrial Operations consolidated structure as the ship-repair-and-maintenance organization."
- `00_research-file.md` acronym table — PAE-IO row corrected to describe the Navy consolidation.
- `00_research-file.md` §1 thread 2 — "Amentum and other major Navy MRO contractors" replaced with "the private ship-repair contractor base."
- `00_research-file.md` §9.4 — Amentum mentions removed; the discipline now reads as "specific commercial contractors should be named only when they surface organically in sources."
- `00_research-file.md` §10.1 PAE-IO public footprint — research-target bullets rewritten to remove the assumption that PAE-IO has a private contractor's research footprint (USAspending contract history of "PAE-IO" doesn't fit a Navy reorg).
- `index.md` `customer:` frontmatter — same correction as the research file header.
- `03_pocs.md` POCs-to-scope note — "PAE-IO (Amentum) program leadership" replaced with "leadership of the Navy's PAE Industrial Operations consolidated structure."
- `01_sources/2026-05-23_navy-mil_navy-shipbuilding-plan-may-2026.md` — the two analytical notes that referenced Amentum were rewritten.

What is left unchanged:

- Historical decision-log entries that record the previous Amentum confusion (this entry above and the entry below describing the PAE-IO resolution) are preserved as the record of what happened. The decision log is append-only and shouldn't be rewritten to hide prior errors.

**Correction (same day, 2026-05-23):** the earlier draft of this entry claimed that the Amentum mentions remaining in `_inbox.md` were "organic find_sources surfacing" and "operator-decided at triage." That mischaracterized what happened. The operator caught it. The Amentum inbox hits came from two queries that I had added to `_search-config.yaml` (`"PAE Industrial Operations Amentum Navy ship repair contract public testimony"` and `"Amentum investor materials industrial operations ship repair revenue segment"`), plus two USAspending recipient queries (`"PAE Applied Technologies"` and `"Amentum"`). Those queries were themselves expressions of the same incorrect Amentum-as-PAE-IO-parent assumption that contaminated the analytical content. Calling the downstream inbox hits "organic" obscured that the find_sources output is only as organic as the queries that drive it.

What changed as a result of the correction:

- `_search-config.yaml` — the four Amentum / PAE-named queries were removed. The Week 2 AI-search section is now keyed on Navy Regional Maintenance Centers and NAVSEA Industrial Operations Directorate instead of specific commercial contractors. The USAspending recipient queries naming Amentum, PAE Applied Technologies, and PAE were removed; only keyword-only queries (Carderock, battle damage repair, Navy Regional Maintenance Center) remain. Inline comments in the config explain why named-contractor queries were removed, so a future analyst doesn't add them back without a source-based reason.
- `_inbox.md` — 15 contaminated pending entries that came from the removed queries (mostly Amentum corporate content — earnings calls, job postings, executive announcements, NASA contract news) were moved to `_rejected.md` with rejection-reason "Analyst-seeded query (Amentum) — not source-surfaced organically." The `_rejected.md` file is sticky and these URLs will not be re-queued by future `find_sources` runs.
- `feedback_named_contractor_discipline.md` memory updated to capture the finer lesson: organic surfacing requires the search queries themselves to be organic, not just the downstream API responses.

**Process lesson:** introducing a named entity into vault analytical content based on inferred context (rather than source content) is a recurring SOP rule 4 hazard, AND the same hazard applies to search-config queries. Pre-loading a contractor name into a query and then calling the resulting matches "organic" is a circular validation. The discipline going forward is to keep search queries general (capability terms, organization terms, contract-vehicle terms) and let actual entity names enter the vault only through source content.

---

### 2026-05-23 — PAE-IO terminology resolved by operator

The §9.4 verification flag added earlier today is closed. Operator confirmed that PAE Industrial Operations as used in the May 2026 Navy Shipbuilding Plan is a Navy reorganization, not a commercialization of the public shipyards or Regional Maintenance Centers, and is not the same thing as any Amentum-owned defense services subsidiary.

The vault was previously conflating two unrelated entities under the PAE-IO acronym. That framing came from incorrect context I held about an Amentum acquisition of "PAE Industrial Operations" — there is no primary source for that link, and the operator has now corrected it. This was a SOP rule 4 violation that escaped detection earlier: an Assessment-level claim about Amentum's structure had been written into the glossary as if it were a FACT.

What changed:

- `_meta/glossary.md` PAE-IO entry rewritten to describe the Navy organizational consolidation. The acronym expansion is left blank because the primary source does not give it.
- `_meta/glossary.md` Amentum entry rewritten to describe Amentum as an independent Navy services contractor, with an explicit note that the prior PAE-IO parent-company framing was incorrect.
- `00_research-file.md` §1 thread 2 rewritten to separate Amentum (the industrial-supply-side contractor we track) from the PAE-IO Navy consolidation. Both are mentioned because both matter to the research, but they are now correctly distinguished.
- `00_research-file.md` §9.4 retitled and rewritten to show the flag as resolved rather than open.
- `01_sources/2026-05-23_navy-mil_navy-shipbuilding-plan-may-2026.md` provenance note rewritten to reflect the resolution.

Out of scope this session: the index.md frontmatter `customer:` field still reads "PAE-IO / Amentum as industrial supply-side" in the candidate-customers list. That language carries forward the incorrect framing. It should be rewritten on the next edit pass to separate the two. Deferred because the file is operator-touched and a quick edit risks crossing the readability pass.

---

### 2026-05-23 — Two load-bearing sources recovered via manual operator paste

The operator manually recovered two sources that the automated ingest pipeline could not reach.

**SRF-JRMC SWARMEX article.** Operator navigated to the SRF-JRMC story index page and copied the article body text into chat. The original `navsea.navy.mil/Media/News/Article/3748283/...` URL remains 404 from both browser and script access. Ingested as `[s.2026-05-23-swarmex-srf-jrmc]` at `01_sources/2026-05-23_navsea-navy-mil_ship-wartime-repair-and-maintenance-exercise-swarm-ex-in-japan.md`. The article confirms what the research has been hypothesizing about SWARMEX: Ship Wartime Repair and Maintenance Exercises are an ongoing series in the U.S. Seventh Fleet Area of Responsibility, designed to give Forward Deployed Ship Repair Teams experience in "battle damage assessment and repair" (verbatim) and to develop partnerships with local ship-repair industry for maintenance and repair resiliency. The first Japan exercise was held at the Japan Maritime United Maizuru Yard with maintenance executed on USS FITZGERALD (DDG 62), and JMSDF stepped in when mooring at JMU failed. The article also surfaces a new term — Forward Deployed Ship Repair Teams (FDSRT) — that should land in the per-opportunity glossary.

**Navy May 2026 Shipbuilding Plan PDF.** Operator manually downloaded and uploaded the 9.4 MB PDF after both candidate URLs (`navy.mil/Portals/1/Documents/...` and `media.defense.gov/2026/May/11/...`) returned 404 from the war.gov migration. The binary is stored at `01_sources/2026-05-23_navy-mil_navy-shipbuilding-plan-may-2026.pdf` and the citation-companion markdown at `01_sources/2026-05-23_navy-mil_navy-shipbuilding-plan-may-2026.md`. The plan is signed by Acting SECNAV Hung Cao, the 34th CNO (Admiral Daryl Caudle), and the 39th CMC (Gen. Eric M. Smith). Multiple load-bearing passages for this research track: a Ship Repair and Maintenance section on page 34 that explicitly states "the Navy and Marine Corps must have the right to repair their own equipment," describes the planned shift to a maintenance continuum with AI / machine learning predictive maintenance and ship digital twins, and announces a "PAE Industrial Operations" organizational consolidation that controls the Navy Regional Maintenance Centers + NAVSEA's Industrial Operations Directorate + the four public Navy Shipyards.

**PAE-IO terminology ambiguity flagged.** The Navy plan uses "PAE Industrial Operations" to describe a Navy organizational structure. The vault glossary currently defines PAE-IO as the Amentum-owned ship-repair subsidiary. These are either (a) the same entity with the Amentum subsidiary now operating the Navy shipyards, (b) a different entity with the same name, or (c) the Amentum subsidiary contracted to run the consolidated organization. A new subsection 9.4 of the research file records the ambiguity and the discipline that follows from it. The glossary entry for PAE-IO is NOT being edited until this is resolved by a primary source.

**Connection to the Warren / Sheehy 'Military Right to Repair' inbox hit.** The 8/10-scored Warren / Sheehy Senate press release on military right-to-repair surfaced in the second find_sources pass. The Navy Shipbuilding Plan's page-34 statement that "the Navy and Marine Corps must have the right to repair their own equipment" is independent primary-source support for the same policy push. The Senate push and the Navy plan are aligned, not in tension. The right-to-repair thread is now a load-bearing claim supported by two independent primary sources from the executive and legislative branches.

**Source ledger restructure.** §8.1 of the research file gained two new entries at the top of the list. §8.2 (failed ingests) was updated: SWARMEX and the Shipbuilding Plan PDF entries moved out of the failed list (strikethrough kept for reference) and noted as recovered. The two remaining NAVSEA 404s (Vertical Launching System tool, Carderock Orion Recovery) remain in §8.2 as lower-priority recoveries.

**Out of scope this session:** the empty-ingest defense.gov shipbuilding plan transcript file in `01_sources/` (which was the same content but as a 404-rendered-as-200) is now redundant with the recovered PDF. It should be moved to `01_sources/_quarantine/` along with the other broken ingests. Cleanup deferred.

---

### 2026-05-23 — SAM ranker built and tested

(See `f700634` commit.) `lib/ranker.rank_sam_candidates()` and the SAM-specific gpt-4o-mini prompt added; `find_sources._run_sam_search` now fetches each notice's description from the SAM API, packages a candidate dict with full metadata, ranks each via OpenAI, and drops anything below `sam_min_score` (default 5, configurable per opportunity). `inbox.append_sam_candidates` now renders the score tag. Validated against three synthesized cases (BDR training RFI 8/10, Long Beach disposal 3/10, janitorial services 1/10). The 50 SAM candidates currently in the inbox were NOT re-ranked retroactively; offered a one-shot rerank script as follow-up.

---

### 2026-05-23 — Research origin and contact-protection discipline recorded

The operator disclosed that this research track was initiated based on a working observation from a working-level Navy ship-repair contact. The operator and Claude agreed on two sensitivity questions:

1. **How much insider context goes into the file:** a short anonymized note in section 1 plus a load-bearing verification-flag entry in section 9. Enough for any future reader to understand why the track exists, without exposing the individual.
2. **What generic framing to use:** "a working-level Navy ship-repair contact." More generic than naming an organization or a team.

**What changed:**
- Section 1 — added a paragraph noting the research origin in generic terms and pointing at section 9.3 for the verification discipline.
- Section 7 — added a one-sentence note to leg 1 (the training-assumption gap) acknowledging that the working observation is consistent with the leg being true, while preserving the public-source-triangulation requirement.
- Section 9 — added a new subsection 9.3 ("The research origin is non-public; the contact is not citable") as a load-bearing constraint parallel to the classification gradient in 9.1. The subsection specifies the discipline: contact is not named in any artifact at any sensitivity tier; their framing scopes the research but does not enter the FACT chain; engagement with the contact's organization proceeds via standard public-facing paths only; any future quote or framing that originates with the contact must be matched against a public source before it can appear in a deliverable.
- Section 11 — added an engagement-paths discipline note in the section intro: SRF-JRMC and adjacent Pacific Fleet repair organizations are research subjects engaged via public paths only, never via working-level channels. The 11.1 inventory applies to these organizations the same way it applies to NSWC Carderock — start from zero in any artifact that names a specific organization.

**What is NOT in this file or in any derived artifact:**
- The contact's name, organization, role, or team.
- Any indication that an existing working-level channel exists at any specific Navy organization.
- Anything that would narrow the field of plausible individuals.

The operator's private knowledge about who the contact is and where they sit is OUT OF SCOPE for this vault. If the operator wants to track that channel for their own reference, they should do so outside the vault (a personal note, a private file explicitly marked never-share). The vault must remain shareable up to its sensitivity tier without compromising the contact.

---

### 2026-05-22 — Folder restructure (deep-module layout) + research resumed

This entry covers two changes the operator authorized together.

**The restructure.** The folder gained four sub-directories — `_decisions/`, `_plays/`, `_red-teams/`, and `_verifications/` — each with a one-paragraph `README.md` explaining what goes there and the filename convention. A per-opportunity glossary stub at `_glossary.md` was also added.

The reason for the restructure is the principle-4 (deep modules, not shallow) lesson from the 2026-05-22 workflow review. Previously every red-team report, verifier report, pending-decisions document, and play card would land as an underscore-prefixed peer at the top level of an opportunity folder. The PMTEC folder accumulated nineteen items at the top level that way and was becoming hard to scan. BDR is being structured up-front so it does not accumulate the same flat-folder problem as it grows. PMTEC was deliberately left in its existing flat layout for now — the script changes that point at the new sub-directories will need to handle both layouts during the transition, but for BDR the sub-directories exist from day one.

The frequently-touched files (`_inbox.md`, `_rejected.md`, `_search-config.yaml`, `_glossary.md`) stay at the top level because the operator interacts with them constantly. The canonical numbered files (`00_research-file.md`, `01_sources/`, `02_quotes.md`, `03_pocs.md`, `04_artifacts/`, `05_decision-log.md`) also stay at the top — unchanged.

**The resume.** The pause that began 2026-05-22 is now lifted. `auto_find` in `index.md` is back to `true`. The `next_action` field is updated to point at inbox triage. The 67 candidates queued from the 2026-05-21 source-finder pass are still in `_inbox.md` and are the next thing to look at.

The recommended triage order (carry-over from the 2026-05-21 entry above and unchanged): the 9/10 SWARMEX article first (Ship Repair Facility Japan Regional Maintenance Center wartime repair exercise — most consequential single hit, potential partial falsifier of section 7 leg 1), then the 8/10 cluster (GAO-26-109068 Navy and Coast Guard Shipbuilding report, Navy Shipbuilding Plan 2025-2026 transcript, ESG-2 dynamic exercise on DVIDS, MHI $111M NAVSEA ship-repair contract).

Two things to watch as research proceeds:

1. `verify_facts.py` and `red_team.py` are not yet updated to write into `_verifications/` and `_red-teams/`. They will need updating before the first verifier or red-team run for this track. The deferred update is intentional — the next steps for BDR are source ingestion and research-file updates, neither of which touches those scripts. The script updates can be made when the work actually demands them, per the SOP §8 principle of "build infrastructure when the work demands it."
2. The USAspending API was returning HTTP 500 errors on 2026-05-21 and only the SAM keyword query against "NSWC Carderock" produced results on that pass. A second `find_sources.py` pass against this track should be queued for 7-14 days from now to pick up any USAspending data and any AI-search results that became available after the API recovery.

---

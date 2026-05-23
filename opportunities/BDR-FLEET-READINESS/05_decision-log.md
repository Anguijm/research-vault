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

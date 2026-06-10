# Hanwha Ocean — Decision Log

Every decision: date, decision, by whom, rationale, what changed.

---

### 2026-06-07 — Opportunity opened (exploratory sandbox)

**By:** operator
**Rationale:** Operator opened Hanwha Ocean as an exploratory study. Alignment
was run via the grill-me skill (`_meta/grill-me.md`) before scaffolding. The
operator could not yet state a working hypothesis and explicitly said that is
what the research is for, so this folder is scaffolded as a research sandbox
rather than a brief-pointed opportunity.
**What changed:** Folder `HANWHAOCEAN-DOD` initialized from blank templates;
Gate 1 (identify) research begun.

**Alignment captured (grill-me):**

- **Folder ID:** `HANWHAOCEAN-DOD` — operator's write-in. Opportunity = Hanwha
  Ocean; customer = DoD (broad, to avoid pre-committing a service).
- **Role of Hanwha Ocean:** undetermined — possibly customer, teaming partner,
  and/or customer-adjacent intel to the operator's SRF-JRMC ship-repair world;
  competitor lens judged least likely ("all of the above, though less of a
  competitor").
- **Buyer:** TBD ("maybe all of the above") — recorded as `customer: tbd`.
- **Hypothesis:** deliberately open; finding it is the research goal.
- **Deliverable:** one-page executive brief, *eventual* output, not near-term.
- **Sensitivity:** shareable.
- **Out of scope:** nothing initially; narrow as research surfaces it.
- **auto_find:** set to `false` (operator controls begin/pause).
- **capability_tags:** provisional (`naval-MRO`, `shipbuilding`) — revise once
  the role and DoD intersection are known.
- **Named-entity discipline:** no Hanwha subsidiary names, hull numbers, or
  contract specifics seeded into analytical files or search config until an
  ingested source surfaces them.

---

### 2026-06-07 — First source-development pass (Claude-run)

**By:** Claude (tactical), at operator's instruction to "develop sources on your own"
**Rationale:** Operator directed autonomous source gathering. The CLAUDE.md
"no web access" note predates the web/search tools now in-session, so those
were used, with every item run through the verification discipline.
**What changed:** Ten sources captured into `01_sources/` and the §8 ledger;
research file §3 (demand signal) and §5 (context landscape) populated with
FACT-labeled, cited claims; §6 (our fit) and §7 (hypothesis) left open per the
exploratory framing; named-entity audit run and passed (CACI allowlisted as the
home-company baseline via `_entity-allowlist.yaml`).

**What the sources establish (two coherent threads):**
- MRO line: Hanwha Ocean signed an MSRA with NAVSUP (22 Jul 2024) and has done
  three USNS auxiliary availabilities in Korea (Wally Schirra, Yukon, Charles
  Drew), with MSC Office Korea as operational touchpoint.
- Construction line: Hanwha bought Philly Shipyard (~$100M), pledged ~$5B to
  expand it, and won a first U.S. Navy NGLS subcontract.
- Macro: all of this sits under the U.S.–Korea "MASGA" framework; HD Hyundai
  and HJ Shipbuilding are also entering — so the right unit of analysis (single
  firm vs. trend) is an open operator framing call (see research file §5, §7).

**What this pass did NOT establish:** any CACI intersection. No source connects
Hanwha's activity to a CACI capability area. The hypothesis stays open.

**Pending operator action (surfaced, not resolved by Claude):**
1. Three Tier-1 `.mil` primaries are identified but 403-block this environment
   (navy.mil Wally Schirra article; MSC "Korea and Singapore Ship Repair
   Industry Day"; MSC 2025 Annual Report PDF). Need operator capture.
2. WebFetch-mediated quotes (Del Toro, Moore, Kim) are flagged UNVERIFIED —
   confirm verbatim before any brief use.
3. Framing decision: Hanwha-the-firm vs. MASGA-the-trend as the subject.

---

### 2026-06-07 — Second source pass: headed Playwright + USAspending (Claude-run)

**By:** Claude (tactical), at operator's instruction to use Playwright on the
403-blocked domains and to pull USAspending awards.
**Rationale:** Operator confirmed the firm-vs-trend framing (subject = Hanwha the
firm, with the MASGA/Korea-yard trend as context and a CACI-intersection
workstream) and directed live-page verification plus an awards search.
**What changed:**
- **Headed Playwright** (venv playwright, DISPLAY :1, light stealth, ~20–38s
  between fetches) defeated the Akamai/Cloudflare 403s that block ingest.py and
  WebFetch. Captured navy.mil (Wally Schirra ROH), the MSC-FLCY Industry Day
  page, and USNI ($5B Philly). One second USNI page hit a Cloudflare challenge
  and was skipped as redundant with the navy.mil primary.
- **Quotes verified/corrected:** navy.mil confirmed verbatim Koprowski and Moore
  quotes; the WebFetch-derived Naval News Moore quote was marked SUPERSEDED.
  Verified quotes written to `02_quotes.md` (Koprowski, Moore, David Kim). The
  Del Toro SECNAV quote remains UNVERIFIED.
- **USAspending (lib/usaspending.py API client):** searched HANWHA / HD HYUNDAI /
  PHILLY SHIPYARD / HJ SHIPBUILDING. Ingested 8 federal award records — Hanwha
  Ocean's three big ROHs (~$26–27M each: Wally Schirra N4034524F0559, Yukon
  N6264925FL025, Charles Drew N6264925CL015), plus Wally Schirra MTA, USNS
  Richard E. Byrd voyage repair at Chinhae, and emergent repair services; and
  two HD Hyundai ROHs (Alan Shepard, Cesar Chavez) for the trend. The award data
  independently confirms the contracts and surfaced availabilities the press
  never named. Contracting activity N40345 = NAVSUP FLC Yokosuka (operator's
  world); N62649 not yet identified.
- Research file §3–§9 rewritten with the authoritative figures; §6 now carries
  the CACI-intersection hypotheses (all Assessment/Speculation — no source ties
  CACI to this). Named-entity audit re-run: PASS (21 sources, Vigor now
  source-backed).

**Note on method:** the chosen approach for this environment is headed Playwright
for 403-blocked .mil/USNI pages and the USAspending API client for awards — not
UI-scraping usaspending.gov (the API is the authoritative, citable, boring-tool
path for the same data).

---

### 2026-06-07 — Third pass: MSC documents, contracting chain, CACI thread (Claude-run)

**By:** Claude (tactical), at operator's instruction to do all three next steps in order.
**Rationale:** Operator approved chasing (1) the MSC-FLCY linked PDFs, (2) the
N62649 code, and (3) the FLC-Yokosuka CACI thread.
**What changed (all three, in order):**

1. **MSC-FLCY Industry Day documents pulled** — extracted anchor links from the
   403-blocked hub page, then downloaded all 8 documents (deck, overview, welcome
   letter, Korea/Singapore agendas, attendees xlsx, conference pptx, annual-
   submittals pptm) through Playwright's browser network context; parsed PDFs
   (pypdf) and Office files (stdlib zip/XML). Captured two new Tier-1 source
   files: the **acquisition model** and the **attendee competitive field**.
   Key facts: MSC Pacific ship repair is **full-and-open, FFP, LPTA**, posted on
   SAM.gov/AsiaNeco; **USNS platforms no longer require an MSRA/ABR** (only USS
   do); the field is ~30 Asian/Pacific shipyards (no services firms).
2. **N62649 resolved** — via USAspending award detail, both N62649 and N40345
   PIID families are awarded by **NAVSUP Fleet Logistics Center Yokosuka**;
   funding office is **Military Sealift Fleet Support Command**. Full contracting
   chain now sourced.
3. **CACI thread tested — and it hit.** CACI is already an MSC prime: USAspending
   PIID **FA807522F0054** (~$125.6M; $174M announced) for **machinery/structural-
   maintenance engineering, shipyard QA, and Condition-Based Maintenance**, via a
   DoD IAC vehicle, with "worldwide deployments to shipyards during MSC ship
   availabilities" (CACI IR release ingested; USAspending award ingested). Plus
   trade-sourced ~$69.2M MSC worldwide-logistics and ~$113.8M MSC business-systems
   contracts. The CACI intersection moved from Speculation to a **sourced
   pull-through thesis** (§6): as MSC pushes availabilities into Korean yards,
   demand grows for the government-side engineering/QA/CBM work CACI already does
   for MSC. CACI and Hanwha are on the same side of the table.

Research file §2–§9 updated; candidate hypothesis now stated in §7 (still
identify-stage, recommendation TBD). Source corpus = 25; named-entity audit PASS
(CACI now source-backed in 4 sources, not just allowlisted).

**Open validation question:** does CACI's MSC maintenance-engineering scope reach
the Far East / FLC-Yokosuka availabilities, or only CONUS/Norfolk? That gates the
hypothesis and is the natural next research step.

---

### 2026-06-07 — Demand-signal shoring pass (Claude-run)

**By:** Claude (tactical), at operator's instruction to shore up demand-signal sources.
**What changed (three items, all done):**
1. **Del Toro SECNAV quote VERIFIED** — headed-Playwright capture of the live
   Naval News page confirmed "Hanwha's acquisition of Philly Shipyard is a
   game-changing milestone in our new Maritime Statecraft" verbatim. `02_quotes.md`
   updated from UNVERIFIED to verified.
2. **MSC 2025 Annual Report captured** (headed Playwright, 33pp PDF). Supplies the
   strongest demand-signal statement in the corpus — MSC's own framing of the
   Hanwha/Korea ROH as "a building block for the Navy's vision to broaden ship
   maintenance and repair in the Indo-Pacific." Added to §3.3.
3. **CACI's other two MSC contracts ingested as primaries** (USAspending): MSC
   Integrated Business Systems (N3220519F1044, ~$165M, on CIO-SP3) and MSC
   Worldwide Logistics Services (N3220524C4115, 2024). §6.1 upgraded from
   "trade-sourced" to primary-sourced — CACI now shown across MSC's maintenance-
   engineering, business-systems, and logistics layers.

Corpus = 28 sources; named-entity audit PASS. The §7 validation question (does
CACI's MSC maintenance-engineering reach the Far East specifically?) remains the
single open gate — deferred by operator choice this pass.

---

### 2026-06-07 — Validation question answered: WHITE SPACE, not incumbency (Claude-run)

**By:** Claude (tactical), at operator's instruction to settle the §7 gate.
**Method:** USAspending — FA807522F0054 place-of-performance + subawards; CACI
awards filtered to JPN/KOR place-of-performance across ship/maintenance/sealift/
NAVSEA scopes and (broadened) any scope; plus web/IR.
**Finding:** Contractually possible, empirically unrealized. FA807522F0054 is
performed from Norfolk VA ("worldwide deployment" scope language). CACI has **zero**
ship-maintenance/MSC/NAVSEA awards with a Japan/Korea place of performance; its
entire Pacific federal footprint is Air Force/Army IT and exercise support (USFK
exercise planner, SharePoint, rugged laptops). The Korea-ROH government oversight
appears MSC-organic (MSCO Korea).
**Consequence:** §7 reframed from "automatic pull-through" to a **deliberate
white-space pursuit** — CACI holds the MSC maintenance-engineering franchise +
vehicle, the Navy is standing up a Pacific MRO enterprise, and CACI's support is
not yet extended there. The operator-team's FLC-Yokosuka/Pacific footprint is the
bridge. §2 and §7 updated.
**Next (operator-set):** step back and think about CACI opportunities to work
with either DoD or Hanwha — the validation result is the input to that.

---

### 2026-06-07 — PIVOTAL operator correction: the team's TO is FA807522F0054 (MSC N7)

**By:** operator (authoritative on own contract); recorded by Claude.
**What the operator stated:** "My task order is FA807522F0054." It is sponsored by
**MSC N7 (Engineering Directorate)** — confirmed N7 = MSC's Engineering Directorate
via MSC org sources. The operator's team does **USS** repair support at **SRF-JRMC,
Japan**. A *separate* contingent on the **same task order** does **USNS** ship work
for MSC worldwide (deploying to MSC availabilities). The operator has met some of
that USNS contingent in San Diego; the two do not operationally overlap. The
operator confirms the facts but not the contracting mechanism (how an MSC-funded TO
also covers USS/SRF-JRMC work).
**Why pivotal — it overturns the prior "white space" conclusion:** the earlier
read treated FA807522F0054's Norfolk place-of-performance as proof of no Pacific
CACI footprint. That was a contracting-HQ artifact. CACI *does* field the USNS
shipyard-QA contingent that would service the Korea/Hanwha USNS availabilities —
and it sits on the operator's own contract. So the Hanwha/USNS opportunity is an
**incumbency-extension** for CACI's USNS contingent, surfaced via the operator as an
**internal, warm relationship-lead** — NOT the operator-team's direct-execute (that
lane is USS/SRF-JRMC, non-overlapping) and NOT a cold corporate intro.
**Records updated:** §2, §7 (research file); capability book README (gap closed),
vehicles.md §1.1 (operator TO tagged); memory [[project_team_uss_rmc_vs_usns_msc]].

---

### 2026-06-07 — Two new candidate opportunity shapes opened (§10)

**By:** operator endorsed two directions ("love them both"); Claude developed them.
**Alignment (grill-me-lite before writing):** operator chose to (1) develop both
**inside** this Hanwha track (not scaffold separate folders yet), and (2) treat
"sell CACI services to Hanwha" as an **open scope decision** — develop both the
sell-to-Hanwha and teaming framings, mark the scope question open.
**What changed:** added research-file §10 with two Speculation-labeled shapes —
(A) cyber / CMMC / supply-chain assurance, Hanwha-facing (with the sell-to vs.
teaming fork flagged); (B) government-side oversight/QA/assurance of the
foreign-yard USN MRO enterprise (Navy customer, scales with the Korea-yard trend,
distinct from the parked MSC N7 TO). Both gated by an explicit **OCI**
(Organizational Conflict of Interest) constraint — CACI cannot both assure foreign
yards and sell to them; see `_meta/oci-primer.md`. The MSC N7 maintenance-
engineering thread (§6) is parked, not dropped.
**Next:** operator to react / pick which shape (if any) to research further; the
sell-to-Hanwha scope decision is the operator's to settle.

---

### 2026-06-08 — Play 1 drafted: government-side foreign-yard assurance

**By:** operator directed "develop a Hanwha-driven play from the government side"; Claude drafted.
**What changed:** created `_play-1-foreign-yard-assurance-2026-06-08.md` (play-card
template) — CACI as the Navy's independent QA / technical / security-SCRM assurance
agent for USN ship work at foreign (Korean) yards, sold to the Navy (MSC N7 / NAVSUP
FLCY / NAVSEA), never to the yards. Status: **ideation**; TAM speculative (~$10–60M,
low confidence). Built on CACI's existing MSC N7 shipyard-QA incumbency (FA807522F0054)
and SeaPort/NAVSEA past performance.
**Key strategic point:** choosing the government-side play *resolves* the OCI conflict
— committing CACI to assure the Navy and not serve the yards makes the OCI constraint
the positioning (impartial assurance over all foreign yards). The demand research
(§10.3) supports this over the Hanwha-facing thread, since Hanwha isn't shopping for
US services and the yard's digital edge is self-supplied.
**Gating questions (in the card):** will the Navy *contract* assurance or keep it
organic (MSCO Korea today)?; fit FA807522F0054 scope or a new SeaPort NxG TO?; operator
to settle sell-to-Hanwha as government-side-only (the OCI firewall). Demand-side
research also added (§10.3) with two sources (Hanwha smart-yard feature, David Kim
interview); corpus = 30, audit PASS.

---

### 2026-06-10 — Play 1 TAM sized from award data (honest about the bet)

**By:** operator directed "size the realistic USN MRO ceiling," then "write it up but be honest about the bet"; Claude sized and wrote.
**What changed:** Replaced Play 1's speculative TAM with a bottom-up sizing from the §3.1 USAspending award data, and added a SIZED bullet to §10.2. Findings: observed Korea-yard USN auxiliary MRO ≈ **$103M / ~8 availabilities / ~18 months** (~$60–90M/yr run-rate, corpus-limited); realistic market ceiling **~$100–200M/yr** (auxiliaries only — every observed availability is USNS, no combatants); CACI's government-side assurance slice ≈ **a few $M/yr** (~$15–80M over a 5-yr vehicle at the ceiling). Corrected the per-availability anchor from $26M (Hanwha-only) to **~$13–19M blended** (HD Hyundai ROHs run $7–8.5M).
**The bet, stated plainly:** Play 1 is an **incumbency extension and cheap positioning, not a franchise** — small against CACI's existing $125.6M MSC N7 TO. The only upside that breaks the ceiling is USS combatants moving to Korean yards (Speculation; not happening today). Two soft drivers compound: the assurance percentage and the contracted-vs-organic gate.
**Unchanged:** status stays ideation; the top gate (will the Navy contract assurance vs. keep it organic) is still unanswered; next_action_due 2026-06-21.

---

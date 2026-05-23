---
type: glossary
purpose: Vault-wide vocabulary so the AI and the operator use the same words to mean the same things
last_revised: 2026-05-22
---

# Vault glossary

This file is the vault's ubiquitous language. The idea comes from Eric Evans' Domain-Driven Design — a shared vocabulary that the operator, the AI, and the artifacts in the vault all use consistently. Without it, every prompt burns context on figuring out what words mean, and the AI guesses. With it, prose stays tighter and the generated content matches what was planned.

When you add a new term, define it here first. When you write a new file, link the terms back to this glossary on first use if there is any chance the future reader will not recognize them.

Per-opportunity glossaries can live at `opportunities/<ID>/_glossary.md` for customer-specific terms that do not belong in the vault-wide list — see the convention note at the bottom.

---

## Vault structure and workflow

These terms describe how this vault is organized and how a piece of research moves through it.

**Opportunity.** A specific defense business-development target — a customer, a program, a contract vehicle, or a research track without a named customer yet. Each opportunity gets its own folder under `opportunities/<ID>/`.

**Research track.** A folder structured like an opportunity but explicitly NOT yet a capture target. Used for exploratory work that may or may not resolve into a named capture later. Example: `BDR-FLEET-READINESS`.

**Capture brief.** The 10-12 page Word document produced for the BD team for a given opportunity. The primary deliverable of this vault. Lives in `opportunities/<ID>/04_artifacts/` with filenames like `capture-brief-v1.0-internal.docx`.

**Executive brief.** The 1-2 page Word document derived from the capture brief, written for a defense pure-play executive who reads on a phone. The secondary deliverable.

**Play card.** A focused 1-2 page markdown analysis of a specific business-development play within an opportunity — for example, a single teaming partner option, a single capability bid, or a specific contract vehicle. PMTEC has multiple play cards. The template lives at `_templates/play-card.md`.

**Gate.** Where an opportunity sits in the simplified 3-gate process: **identify**, **pursue**, **bid**. Plus terminal states **won**, **lost**, **dropped**. Set in the opportunity's `index.md` frontmatter.

**Status.** Where the *work* sits, independent of the gate: **triaged**, **research**, **drafting**, **review**, **shipped**, **stalled**. Set in the opportunity's `index.md` frontmatter.

**Sensitivity tier.** How widely a section of work can be shared: **internal** (operator-only), **shareable** (can be released to a teaming partner with attribution control), **public** (cleared for any audience). Marked with HTML comments `<!-- sensitivity:internal -->` ... `<!-- /sensitivity -->` around the affected content. The shareable version of a brief is generated *by deletion* from the internal version, not by rewriting.

**Source ledger.** Section 8 of every research file. The list of sources cited in that file, in the format `[s.YYYY-MM-DD-slug]` — see "citation tag" below.

**Decision log.** File `05_decision-log.md` inside each opportunity folder. Every non-trivial decision affecting the opportunity gets an entry: date, decision, by whom, rationale, what changed. Append-only.

**POC directory.** File `03_pocs.md` inside each opportunity folder. The named people relevant to the opportunity, with public-source URLs, contact info if public, and a last-verified date.

**Inbox.** File `_inbox.md` inside an opportunity folder. The queue of source candidates surfaced by `find_sources.py`, awaiting operator approval. Approve by tapping the checkbox in Obsidian; ingest with `approve_inbox.py`.

**Source-finder pass.** A single run of `find_sources.py` against an opportunity. Burns AI quota (Claude and Gemini), SAM.gov quota, and USAspending requests. Not free; do not run casually.

**Capture cycle.** The full sequence from opening an opportunity folder through shipping the capture brief and executive brief. Target cadence is one cycle per month, twelve per year.

---

## Verification discipline

These are the labels and rules from the SOP at `_meta/sop.md` and the printable rules at `_meta/verification-rules.md`. Definitions here are short; the SOP is the authoritative source for the rules themselves.

**FACT.** A claim traceable to a primary source, with an inline citation tag. The strongest claim type. The two-source rule applies to FACTs about money, timelines, named people, or organizational reporting.

**Assessment.** The operator's reasoned judgment based on multiple facts. Must be labeled `Assessment:` in prose. Cannot be cited as if it were a FACT.

**Speculation.** Forward-looking inference not yet supported by evidence. Must be labeled `Speculation:` in prose and flagged for later review. Most month numbers, future-state predictions, and "we expect" statements fall here.

**Two-source rule.** Anything about money, timelines, named people, or organizational reporting needs two independent sources. Single-sourced claims must be marked as such. See SOP rule 2.

**Click-verify.** The discipline of opening every AI-supplied URL before accepting the citation. AIs hallucinate citations. See SOP rule 6.

**Primary source hierarchy.** The ranked list of source types from strongest (`.mil` sites, DVIDS, SAM.gov, USAspending.gov, comptroller PB books, GAO reports, congressional testimony, CRS reports) down to weakest (blogs, social media, single-author commentary). See SOP rule 1 for the full list.

**Citation tag.** The inline reference format used in research files and briefs: `[s.YYYY-MM-DD-slug]`, where the date is when the source was captured and the slug is a short identifier. Example: `[s.2026-04-22-pacom]`. The tag resolves to a file in `01_sources/`.

**Verification status marker.** A status flag attached to a FACT entry that says whether the cited source is actually in the vault yet:
- `[✓ INGESTED]` — source file exists in `01_sources/` and supports the claim.
- `[⚑ PARTIAL]` — some elements of the claim are verified by ingested sources, others are not.
- `[⚠ PENDING-INGEST]` — the source is cited but the file has not been ingested yet.
- `[✗ UNSUPPORTED]` — the verifier looked and the source does not actually back the claim.

**Adversarial review / red team.** The pass where someone (a human SME, or another AI playing customer / competitor / skeptical exec) tries to break the brief. See SOP rule 5 and the `cross-ai-red-team.md` prompt.

**90-day re-verification.** Defense roles rotate and contract data ages fast. Every POC entry and every contract data point on an active opportunity must be re-checked every 90 days. See SOP rule 3.

---

## Article-derived process terms

These are the workflow concepts adopted on 2026-05-22 from the Yanli Liu article *Code Is Not Cheap: How to Multiply Your AI's Output With Software Fundamentals* (republished from Matt Pocock's AI Hero conference talk and Andrej Karpathy's "agentic engineering" post). They are vault-wide methodology, not opportunity-specific.

**Grill-me skill.** The alignment skill at `_meta/grill-me.md`. Forces the AI to interview the operator until a shared mental model exists, before any new scaffold or new brief draft begins. Borrowed from Matt Pocock's open-source Claude Code skill of the same name.

**Ubiquitous language.** This glossary file. The shared vocabulary the operator, the AI, and the vault artifacts all use consistently.

**Gray-box model.** The split between operator (strategic layer — decisions, FACT calls, scope, delivery) and Claude (tactical layer — drafting, source synthesis, scaffolding, script execution). Codified in `CLAUDE.md` under "Who owns what."

**Small-ships workflow.** The verifier-first, section-by-section approach to brief drafting that replaces the current big-batch draft-then-red-team pattern. Documented in `_meta/small-ships-workflow.md`.

**Deep module / shallow module.** Ousterhout's distinction. A deep module hides functionality behind a simple interface; a shallow module exposes a complex interface over thin functionality. AI tends to generate shallow modules. We prefer deep ones because they are easier for the next AI session to reason about.

**Writer / reviewer pattern.** Anthropic's recommended pattern for AI-assisted code: one Claude writes tests, a second Claude writes code to pass them. The vault analog is: one model drafts a section; the other model red-teams it. The cross-AI red-team rule (SOP rule 5) is already this pattern.

---

## Defense industry — sources and oversight

Terms used constantly in source ingestion and verification work.

**OSI.** Open-source intelligence. Material that anyone can read without a clearance or a contract. The only source class allowed in this vault.

**CUI.** Controlled Unclassified Information. A sensitivity tier below classified but above public. Not allowed in this vault.

**SAM.gov.** The federal government's official contracting opportunities and award database. Public, primary-source quality. Accessed by `_scripts/lib/sam_gov.py`.

**USAspending.gov.** The federal government's official obligations and outlay database. Public, primary-source quality. Accessed by `_scripts/lib/usaspending.py`.

**HigherGov.** A commercial aggregator of federal contracting data. Tier 3 — derived from primary sources, useful for the index but the primary should always be checked.

**DVIDS.** Defense Visual Information Distribution Service (`dvidshub.net`). The Pentagon's clearinghouse for command-issued press releases, imagery, and video. Primary-source quality for command announcements.

**GAO.** Government Accountability Office. Congress's auditor. Publishes oversight reports we treat as primary sources.

**CRS.** Congressional Research Service. Congress's in-house research arm. Reports are public and citation-quality.

**SASC / HASC.** Senate Armed Services Committee / House Armed Services Committee.

**NDAA.** National Defense Authorization Act. The annual bill that authorizes Department of Defense spending and policy.

**PB book.** The comptroller's annual Procurement and Budget justification book — for example, the FY2026 PB book is the budget request submitted to Congress in spring 2025. Primary source for funding lines.

**PDI.** Pacific Deterrence Initiative. The funding line for Indo-Pacific posture, training ranges, and infrastructure. Multi-billion-dollar annual line; the FY26 figure is $10.0B per primary source.

**10-K, 10-Q, 8-K.** Annual, quarterly, and event-driven filings that publicly-traded companies file with the U.S. Securities and Exchange Commission (SEC). Primary-source quality for company-disclosed facts.

---

## Defense industry — organizations

Acronyms expand to plain English here; the relationship between them is the part most people forget.

**DoD.** Department of Defense. The Pentagon as a whole.

**DON.** Department of the Navy. Includes both the U.S. Navy and the U.S. Marine Corps under a civilian Secretary of the Navy.

**OSD.** Office of the Secretary of Defense. The civilian leadership layer above the military departments.

**NAVSEA.** Naval Sea Systems Command. The Navy organization that builds, modernizes, and repairs ships. Parent of the warfare centers (NSWC, NUWC).

**NSWC.** Naval Surface Warfare Center. NAVSEA's surface-ship technical-development arm. Has several divisions:
- **NSWC Carderock** (Maryland) — ships and submarines hydrodynamics, structural mechanics, damage modeling.
- **NSWC Dahlgren** (Virginia) — surface combat systems.
- **NSWC Indian Head** (Maryland) — energetics.
- **NSWC Crane** (Indiana) — electronics, expeditionary warfare.
- **NSWC Philadelphia** (Pennsylvania) — ship machinery.
- **NSWC Port Hueneme** (California) — combat systems lifecycle.
- **NSWC Panama City** (Florida) — coastal warfare.

**OPNAV.** Office of the Chief of Naval Operations. The CNO's staff. Divided into directorates **N1** (manpower) through **N9** (warfare systems).

**NWDC.** Naval Warfare Development Command. The Navy's doctrine and tactical-training authority.

**Combatant Command (CCMD).** A joint-service operational command organized by region or function. The geographic ones include:
- **USINDOPACOM** — Indo-Pacific Command (Hawaii).
- **USEUCOM** — European Command.
- **USCENTCOM** — Central Command.
- **USAFRICOM** — Africa Command.
- **USNORTHCOM** — Northern Command.
- **USSOUTHCOM** — Southern Command.

The functional ones include:
- **USSOCOM** — Special Operations Command.
- **USTRANSCOM** — Transportation Command.
- **USSTRATCOM** — Strategic Command.
- **USSPACECOM** — Space Command.
- **USCYBERCOM** — Cyber Command.

**Service branches.** USA (Army), USN (Navy), USAF (Air Force), USMC (Marine Corps), USSF (Space Force), USCG (Coast Guard, under Homeland Security in peacetime).

---

## Defense industry — contracting and acquisition

**FAR.** Federal Acquisition Regulation. The base rulebook for U.S. government contracting.

**DFARS.** Defense Federal Acquisition Regulation Supplement. The Department of Defense additions to the FAR.

**RFI.** Request for Information. The customer is gathering market intelligence; no contract is being awarded yet.

**RFP.** Request for Proposal. The customer is inviting bids for a specific contract.

**BAA.** Broad Agency Announcement. A standing solicitation for research proposals across a wide topic area.

**IDIQ.** Indefinite-Delivery, Indefinite-Quantity. A contract vehicle that lets the customer place task orders against a pre-awarded ceiling.

**Task order.** A specific work assignment under an IDIQ contract.

**SBIR.** Small Business Innovation Research. A federal contracting pathway with three phases — Phase I (feasibility, ~$250K), Phase II (development, ~$2M), Phase III (commercial transition, unlimited).

**STTR.** Small Business Technology Transfer. Like SBIR but requires partnership with a research institution.

**Prime.** The contractor with the direct contract with the government on a given vehicle.

**Sub / subcontractor.** A contractor working under the prime, with no direct government contract on that vehicle.

**Teaming partner.** A company working with another (often two primes splitting scope) under a formal teaming agreement.

**Capture.** The business-development work between identifying an opportunity and bidding it. The output of capture is a winning bid.

---

## Defense industry — training, exercises, modeling

**LVC.** Live, virtual, constructive. A category of military simulation training that mixes real units (live), human-operated simulators (virtual), and computer-generated forces (constructive).

**M&S.** Modeling and simulation.

**BDR.** Battle damage repair. The engineering work of fixing a ship (or aircraft, or vehicle) that has been hit. Distinct from BDA below.

**BDA.** Battle damage assessment. The diagnostic work of figuring out what is broken on a hit platform and how bad it is. Upstream of BDR.

**COMPTUEX.** Composite Training Unit Exercise. A large Navy training event each carrier strike group runs before deploying.

**RIMPAC.** Rim of the Pacific. The world's largest international maritime exercise, held every two years from Hawaii.

**LSE.** Large-Scale Exercise. A Navy exercise series introduced in 2021 that strings multiple exercises together to test distributed fleet operations.

**ANTX.** Advanced Naval Technology Exercise. A Navy exercise format that tests new technologies in operational settings.

**Trident Warrior.** A recurring Navy fleet experimentation event for command, control, computers, communications, and intelligence systems.

**SWARMEX.** Ship Wartime Repair and Maintenance Exercise. A specific 2025 NAVSEA program first run by SRF-JRMC (Ship Repair Facility, Japan Regional Maintenance Center).

---

## Vault scripts and lib modules

What lives in `_scripts/`. These are referenced often in research-file footers and decision logs.

- **`find_sources.py`** — runs the AI / SAM.gov / USAspending source-finder pass against an opportunity. Reads `_search-config.yaml`. Writes candidates to `_inbox.md`.
- **`approve_inbox.py`** — ingests operator-approved inbox items into `01_sources/`.
- **`ingest.py`** — manual single-source ingest tool. Operator pastes source content; script creates the properly-formatted source file.
- **`verify_facts.py`** — runs the LLM-based FACT-vs-source verifier. Produces a markdown verification report.
- **`red_team.py`** — runs the cross-AI red-team passes on a brief (customer / competitor / skeptical exec personas).
- **`refresh_brief_sources.py`** — auto-syncs the source appendix on a Word brief to the current state of `01_sources/`.
- **`sync.sh`** — git commit and push helper with secrets-leak guard.
- **`_scripts/lib/`** — shared modules: `sam_gov.py`, `usaspending.py`, `inbox.py`, `dedup.py`, `frontmatter.py`, `web.py`, `cron_log.py`, `lock.py`, `ranker.py`, `searcher.py`.

---

## Company / market terms used in this vault

These are perspective-dependent and reflect the operator's current business-development context. They will need updating if the operator's company changes.

**CACI.** The publicly-traded defense services company whose perspective this vault is mostly written from. SEC central index key (CIK) 0000016058. Ingested 10-K, 10-Q, and 8-K filings live under each opportunity's source folder as appropriate.

**ARKA.** A defense subsidiary CACI acquired in early 2026 for ~$2.6B net of cash, closed 9 March 2026. ARKA brings electro-optical, infrared, and hyperspectral sensor capability. Frequently mentioned as a differentiator hook for opportunities that need realistic threat signature libraries.

**PAE-IO.** PAE Industrial Operations — a Navy-internal organizational consolidation described in the May 2026 Navy Shipbuilding Plan (page 34) that combines the Navy Regional Maintenance Centers, NAVSEA's Industrial Operations Directorate, and the four public Navy Shipyards into a single structure tying contracting functions for maintenance work to the fleet components responsible for the ships. NOT a commercialization of the public shipyards, NOT an Amentum subsidiary, and NOT a private contractor. The acronym expansion of "PAE" in this Navy-internal context is not stated in the primary source. (Operator confirmed 2026-05-23 after the vault was previously conflating this term with an unrelated Amentum framing.)

**HII Mission Technologies.** Huntington Ingalls Industries' services arm. Inherited Alion's ship-damage modeling work via a 2021 acquisition (commonly confused with CACI, see SOP rule 6 note). A primary competitor in naval modeling and simulation.

**Amentum.** A defense services company that is a major Navy services contractor in maintenance, repair, and overhaul. Originally referenced in this vault as the parent of "PAE Industrial Operations" — that framing was incorrect. PAE-IO is a Navy organizational consolidation, not an Amentum subsidiary. Amentum's actual role in the BDR-FLEET-READINESS research is as the industrial-supply-side contractor whose public-facing planning assumptions we are tracking, independent of the PAE-IO label.

---

## Convention for per-opportunity glossaries

Customer-specific or opportunity-specific vocabulary lives at `opportunities/<ID>/_glossary.md`. Examples of terms that belong in a per-opportunity glossary, not this one:

- PMTEC's eight stated priority gaps (each gap is a named term in the brief).
- The internal structure of USINDOPACOM J7 — specific division names, branch heads, named subordinate cells.
- PMTEC-specific funding lines and named contract vehicles (e.g., the Deloitte "INDOPACOM Alpha" PIID).
- Per-opportunity competitor mappings if they would be confusing without the customer context.

The per-opportunity glossary file should follow the same format as this one: frontmatter, plain-English definitions, no cross-references to terms that have not been defined in either glossary.

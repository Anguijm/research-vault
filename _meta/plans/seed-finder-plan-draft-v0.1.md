---
title: Opportunity seed-finder — plan draft v0.1
date: 2026-05-29
analyst: jma + Claude
status: pre-Gemini-iteration draft
purpose: Design a monthly-run discovery pipeline that surfaces candidate Navy / DoD opportunities from public sources, ranks them against CACI's public capability footprint, and produces a lightweight seeds inbox the operator can triage into either a new opportunity capture or a drop.
---

## Why this exists

The vault's current tooling is opportunity-scoped: `find_sources.py` and the four-pillar ranker run against a specific opportunity's `_capture-pillars.md`. There is no upstream discovery layer that surfaces NEW candidate opportunities from the wider public-record stream. The two opportunities in the vault (PMTEC-USINDOPACOM and BDR-FLEET-READINESS) both came from ad-hoc operator / executive / coworker referrals. Neither came from a systematic scan of the public record. The seed-finder fills that gap so the operator can see what the public record is telegraphing before someone refers it.

## What "seed" means

A seed is the minimum evidence needed to decide whether a candidate opportunity is worth scaffolding into a full capture. It is NOT a capture brief. It is NOT a research file. It is a one-paragraph candidate record with the source citation, a CACI-fit score, and a triage flag. The operator triages the seeds inbox at whatever cadence makes sense (monthly to start) and promotes the worthwhile candidates into the existing opportunity-folder structure via `approve_seeds.py`. Dropped seeds get logged to a rejected ledger.

## Goal

Build a monthly-run discovery pipeline that:

1. Queries a small set of high-signal public sources for the prior 56 days (eight-week lookback so a four-week overlap with the prior run catches updates without re-surfacing items already seen).
2. Filters each candidate against a CACI public capability footprint defined in `_meta/caci-capture-pillars.yaml`.
3. Ranks each candidate on a four-pillar capture-intelligence rubric adapted to the CACI-wide footprint (not opportunity-specific).
4. Writes the surfaced candidates to `_meta/seeds-inbox.md` with a triage checkbox for each.
5. Promotes operator-approved seeds into new opportunity folders scaffolded from `_templates/`.

## Sources to query

Three high-signal sources first; two more in v2 once we see the noise floor.

### v1 sources

1. **SAM.gov pre-solicitation notices** — Sources Sought (notice type S), Requests for Information (R), Special Notices (O), and Industry Day announcements (Y). These are the highest-signal feed because the government is explicitly market-testing 6-to-18 months before the actual Request for Proposal. Filter by customer org (Department of the Navy, Department of the Air Force, Department of the Army, Office of the Secretary of Defense, Joint Staff, Combatant Commands) and by work-type-relevant NAICS / Product Service Codes derived from the CACI capability footprint.
2. **DoD daily contract announcements** at `https://www.war.gov/News/Contracts/` (and the legacy defense.gov equivalent). Every contract over $7.5 million is announced publicly here. The signal is "competitor just won adjacent work" — useful for confirming a pattern and for finding the procurement precedents that fed the BDR §2.4 work.
3. **Senior leadership testimony + Service press releases** — Congressional hearings (House Armed Services Committee, Senate Armed Services Committee, House Appropriations Committee, Senate Appropriations Committee), CNO / SECNAV / CSAF / SECAF / SECDEF posture statements, and Service-branch press releases (navy.mil, army.mil, af.mil, war.gov). This layer is lower-signal but catches the 18-month-ahead-of-RFP intent that does not surface on SAM.gov yet. Caudle's HASC testimony on wartime repair is the example of how this turns into a capture two cycles later.

### v2 sources (defer until v1 noise floor is known)

4. USAspending recent-awards scan — lagging indicator. Useful for confirming a pattern, less useful for early-stage seed-finding.
5. Defense industry press releases (Booz Allen, SAIC, HII, Leidos, BAH, GD, Lockheed, Northrop, Raytheon investor relations + newsrooms) — competitor announcements that point at where money is going. Subject to named-entity discipline; only contractors the operator has allowlisted should drive query terms.

## CACI public capability footprint — the ranking anchor

The biggest design piece. The seed-finder ranks each candidate against `_meta/caci-capture-pillars.yaml`. That file defines CACI's capability footprint as work-types and customer-org categories, all sourced from PUBLIC RECORD only. Internal CACI strategic-priority knowledge stays out.

### Construction approach

1. **USAspending pass on CACI entities.** Query USAspending for awards to `CACI INC`, `CACI NSS LLC`, `CACI ENTERPRISE SOLUTIONS LLC`, and `ARKA GROUP INC` (and any other CACI subsidiaries the operator names). Group by NAICS, PSC, awarding agency, awarding sub-tier. Identify the heavy concentrations.
2. **CACI corporate marketing pass.** Ingest CACI's public contract listings page (`caci.com/contracts`), CACI investor relations capability descriptions, and selected CACI press releases from the prior 24 months. The marketing framing tells us how CACI positions its capabilities even where the public-record work hasn't yet materialized.
3. **Operator-team layer (optional).** The operator's team specifically can edit a separate layer of the YAML to add work-types and customer relationships the operator can speak to directly. This layer is operator-side knowledge the operator chooses to share with the vault. Default empty; operator populates as they see fit.

### YAML schema (proposed)

```yaml
work_type_pillars:
  - name: Exercise design and wargaming
    description: Live-virtual-constructive scenario design, master scenario events list (MSEL) development, decision-rehearsal training, wargames support.
    public_evidence:
      - AFRICOM Plans/Operations/Logistics/Engagement/Training/Exercise/Assessment Support — $194M, CACI NSS LLC, GSA OASIS Pool 1 (PIID 47QFCA20F0002)
      - INDOPACOM J7 PMTEC participation
    related_naics: [541330, 541611, 611430]
    related_psc: [R408, R425, R499]

  - name: C5ISR and decision support
    description: ...
    public_evidence: [...]

  - name: Intelligence, signal, cyber
    description: ...

  - name: Naval IT and software development
    description: ...

customer_org_clusters:
  - name: Combatant Commands
    organizations: [USINDOPACOM, AFRICOM, OSD, Joint Staff]
    public_evidence: [...]
  - name: Navy fleet and SYSCOM
    organizations: [PACFLT, FLTFORCOM, NAVSEA, NAVAIR, ...]
  - name: Army and Air Force adjacent
    organizations: [USAR, AFC, AFMC]

operator_team_layer:
  # Optional. Operator populates from their own team's work and relationships.
  team_work_types: []
  team_customer_relationships: []

out_of_scope:
  # CACI capabilities that exist in the public record but are not pursued by
  # this seed-finder. The operator decides what is out of scope for their BD
  # role. Default examples: CACI's commercial cyber products if the operator's
  # focus is exclusively DoD; CACI's federal civil work if focus is exclusively
  # DoD.
  - ...
```

## find_seeds.py architecture

Parallel to `find_sources.py`, not a fork.

1. Load `_meta/caci-capture-pillars.yaml` and `_meta/seeds-ledger.json` (the fingerprint ledger).
2. For each v1 source:
   - SAM.gov: hit the search API with NAICS / PSC filters derived from the YAML, scoped to the last 56 days.
   - DoD contracts: scrape the war.gov contracts daily-listing page for the last 56 days. Each contract is a structured row.
   - Senior leadership / press releases: query a configured list of RSS feeds and HTML index pages (HASC calendar, navy.mil press office, etc.). Less structured; fall back to the existing `ranker.resolve_and_validate` pipeline for URL hydration.
3. Dedupe each candidate against `_meta/seeds-ledger.json` by fingerprint (SAM.gov notice ID, war.gov article ID, URL hash). Skip anything already in the ledger.
4. Rank each remaining candidate via a CACI-wide four-pillar ranker adapted from `lib/ranker.py::rank_candidates_capture()`. The pillars are now CACI-wide rather than opportunity-specific:
   - Pillar 1: Customer signal — is the candidate from a customer organization in the YAML's customer_org_clusters?
   - Pillar 2: Work-type match — does the candidate name a work-type in the YAML's work_type_pillars?
   - Pillar 3: Scale signal — is the candidate at a scale CACI typically operates ($10M+ for primes, $1M+ for niche)?
   - Pillar 4: Timing signal — is this a pre-solicitation (sources sought / RFI) or an announced contract? Pre-solicitation is higher-signal because it's pre-RFP.
5. Write surfaced candidates to `_meta/seeds-inbox.md` with the standard inbox-block format adapted for seeds.
6. Update `_meta/seeds-ledger.json` with the new fingerprints and timestamps.

## seeds-inbox.md format (proposed)

```markdown
## Seeds surfaced YYYY-MM-DD

- [ ] **[Notice title or contract description](URL)** `8/10` — sam.gov
  - Source: SAM.gov Sources Sought
  - Customer: USINDOPACOM J7 (Combatant Commands cluster)
  - Work-type: Exercise design and wargaming
  - Scale: estimated $25M-$50M based on response-period size
  - Response deadline: YYYY-MM-DD
  - Why it scored: matches CACI work-type pillar X and customer org cluster Y; pre-RFP signal at scale
  - Triage: [ ] promote  [ ] drop  [ ] hold
  - First-seen: YYYY-MM-DD HH:MM
```

The triage row is the operator action. If `promote` is checked, `approve_seeds.py` scaffolds a new opportunity folder. If `drop` is checked, the seed moves to `_meta/seeds-rejected.md`. If `hold` is checked or left unchecked, the seed stays in the inbox for the next cycle.

## approve_seeds.py workflow

Mirrors `approve_inbox.py` but operates on `_meta/seeds-inbox.md` and produces NEW opportunity folders.

1. Parse `_meta/seeds-inbox.md` for promoted seeds.
2. For each promoted seed, prompt the operator for:
   - Opportunity ID (the directory name; e.g., `NAVAIR-LVC-SCENARIO-2026`)
   - Short hypothesis (one sentence; the BLUF the capture will test)
3. Scaffold the opportunity folder from `_templates/` with the seed source already ingested into `01_sources/` and the seed metadata pre-populated into `00_research-file.md` §1.
4. Move the seed block from `seeds-inbox.md` to `_meta/seeds-promoted.md` with a link to the new opportunity folder.

The new opportunity then runs through the standard small-ships workflow.

## Cadence and dedup

Monthly operator-initiated runs. Eight-week lookback per run. Dedup by fingerprint in `_meta/seeds-ledger.json`:

```json
{
  "version": 1,
  "last_run_utc": "2026-XX-XXTHH:MM:SSZ",
  "seeds": {
    "SAM:NOTICE-ID-123": {
      "first_seen_utc": "2026-XX-XX...",
      "last_seen_utc": "2026-XX-XX...",
      "status": "in-inbox | promoted | rejected"
    },
    "WAR:article-id-4496900": {...},
    "URL:sha256:abc...": {...}
  }
}
```

The four-week overlap window between runs catches items updated near month-end without re-surfacing items already seen. Net cost: an extra API hit per run. Negligible.

## Failure modes to design around

1. **Noise floor unknown.** The volume of SAM.gov pre-sol notices and DoD daily contracts is significant. The CACI capability footprint has to be tight enough that ranking floor for surfacing is high enough to avoid drowning the inbox.
2. **Capability-footprint encoding is the biggest risk.** Too narrow misses real seeds; too wide drowns. Initial encoding should err narrow with a known feedback loop (operator dropping seeds as "wrong fit" feeds back into footprint tuning).
3. **Press release / news layer has the lowest signal-to-noise.** Defer or rate-limit at v1.
4. **Named-entity discipline still applies to seed-finder.** Competitor announcements that name specific contractors should be handled the same way the existing audit catches contamination — the ranker doesn't pre-load contractor names into queries, and named contractors surfacing in seeds are discoveries to log, not pursuit targets.
5. **The seed-finder is a discovery tool, not a decision tool.** Operator decides every promote / drop call. The score is advisory; the decision is judgment.

## v1 → v2 phasing

**v1 (minimum viable, ~one day of build):**
- `_meta/caci-capture-pillars.yaml` built from a USAspending pass on CACI entities + CACI corporate marketing pages
- `find_seeds.py` querying SAM.gov pre-sol notices + DoD daily contracts
- `_meta/seeds-inbox.md` + `_meta/seeds-ledger.json` + `_meta/seeds-rejected.md` + `_meta/seeds-promoted.md`
- `approve_seeds.py` with opportunity-scaffolding

**v2 (after v1 noise floor is understood):**
- Senior leadership testimony + Service press releases as a third source
- USAspending recent-awards confirmation pass
- Operator-team layer activated in the YAML
- Optional: simple cron / scheduled-trigger mode if monthly cadence proves too slow

**v3 (deferred, design space only):**
- Defense industry press releases (named-entity discipline carefully observed)
- News domain ingestion (Defense News, Breaking Defense, etc.)
- AI-summarization layer that produces a per-seed "what this means" paragraph beyond the raw notice content

## What's next

1. Operator reviews this plan and pushes back on anything unclear or wrong.
2. Iterate the plan with Gemini Flash for red-team. Convergence target: agree on the v1 scope, the YAML schema, and the failure-mode handling before any code is written.
3. After Gemini convergence, build v1 in one day.

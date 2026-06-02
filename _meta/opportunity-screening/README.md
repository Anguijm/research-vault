---
type: system-index
system: Opportunity Screening
canonical_name: Opportunity Screening
last_updated_utc: '2026-06-02'
---

# Opportunity Screening

Opportunity Screening is the front-end of the vault's capture pipeline. Its job is to pull notices from SAM.gov, score them against CACI's footprint and the operator-team's reach, surface ranked candidates to a triage inbox, and let the operator promote / drop / monitor each one. Promoted candidates become full opportunity folders under `opportunities/`; the rest stay in the screening layer or get dropped.

The system was named on 2026-06-02. Prior to that the pieces existed but were referred to ad-hoc as "the SAM.gov pipeline," "the seed-finder," "the slice plan," and similar. This README is the canonical index.

## What Opportunity Screening is, in one paragraph

Eight SAM.gov query slices anchored on `organizationName` text search pull notices from named Pacific contracting offices (NAVSUP FLC Yokosuka, Pearl Harbor, San Diego, Puget Sound; SRF-JRMC direct; NSWC Corona; 374 CONS Yokota; 18 CONS Kadena). The lib paginates per slice, polite-throttles, and tracks daily quota. Returned notices are fingerprinted, deduped against a ledger, scored on five pillars (customer signal, work-type match, capability-area match, scale signal, actionability window) with a layered boost (operator-team / team-extendable / directional / baseline) and a three-way classification (direct_execute / relationship_lead / customer_intel / low_match). An out-of-scope gate caps known-noise patterns at 0.3. Candidates clearing the monitor threshold (0.5) land in the inbox as markdown plus a CSV row. The operator triages by marking `[x]` on promote, drop, or monitor. `approve_seeds.py` processes the marked entries — promoted seeds scaffold into `opportunities/<ID>/` folders; drops get a rejected-log entry; monitors stay in the inbox.

## Components and where they live

### Configuration (operator-edited)

- **`_meta/caci-discovery-config.yaml`** — single config file with every input the screening system reads. Sections:
  - `ranker_weights:` — pillar weights, layer-boost multipliers, classification thresholds
  - `actionability_logic:` — notice-type priority tiers
  - `thresholds:` — promote / monitor / scale floors
  - `baseline_caci_footprint:` — USAspending-derived NAICS/PSC/customer/vehicle shares (regenerated periodically; operator does not edit by hand)
  - `directional_caci_footprint:` — careers/IR scrape keywords (regenerated periodically; operator does not edit by hand)
  - `operator_team_layer:` — primary customer, secondary, extendable, team work-types, delivery model, active pursuits (operator-edited)
  - `sam_searches:` — eight organizationName-anchored query slices
  - `capability_areas:` — structured machine-readable projection of `_meta/caci-capability-book/` used by the scorer's capability-area pillar
  - `out_of_scope:` — closure rules. Each rule is a one-line phrase; rules with NAICS or PSC codes anchored in their text require both code match and ≥1 keyword overlap; categorical rules require ≥3 keyword overlaps.

### Scoring layer

- **`_meta/caci-capability-book/`** — the corporate-level CACI capability documentation that informs the capability-area pillar. Seven capability areas (C3I, Cyber, Digital Solutions, Enterprise IT, Mission and Engineering Support, Space, Spectrum Superiority) with dual-language coverage (caci.com marketing + FY25 10-K + FY26 Q3 10-Q current state), corporate overview, growth signals, acquisitions, contract vehicles, top-25 past performance, and a source ledger. The capability book is the human-readable source of truth; the `capability_areas:` block in the discovery config is its machine-readable projection. See `_meta/caci-capability-book/README.md` for the book's internal structure.

### Triage state

- **`_meta/seeds-inbox.md`** — surfaced candidates awaiting operator triage. Each seed has a `[ ] promote  [ ] drop  [ ] monitor` checkbox line.
- **`_meta/seeds-inbox.csv`** — cumulative CSV of every surfaced seed across all runs. One row per seed with score breakdown, capability-area matches, classification, NAICS/PSC, and identifiers. Used for cluster-triage outside Obsidian (sort by NAICS/PSC in a spreadsheet to find noise clusters that warrant closure-rule additions).
- **`_meta/seeds-ledger.json`** — fingerprint dedup ledger. Maps stable seed fingerprints to first-seen / last-seen / status. Prevents re-surfacing already-triaged seeds.
- **`_meta/seeds-rejected.md`** — append-only log of dropped seeds.
- **`_meta/seeds-promoted.md`** — append-only log of promoted seeds with pointers to the opportunity folder they became.
- **`_meta/sam-quota.json`** — daily SAM.gov request count, tier-aware (federal / non-federal).
- **`_meta/usaspending-quota.json`** — daily USAspending request count (visibility only; no hard cap).

### Executors

- **`_scripts/find_seeds.py`** — entry point. Loads the config, loops over the `sam_searches` slices, calls the SAM.gov lib per slice, fingerprint-dedups against the ledger, scores via the five-pillar ranker, applies out-of-scope cap and three-way classification, writes the inbox markdown + CSV, updates the ledger.
- **`_scripts/approve_seeds.py`** — triage processor. Reads `seeds-inbox.md`, sees which seeds the operator marked. Promotes (scaffolds `opportunities/<ID>/`), drops (appends to `seeds-rejected.md`), or moves to monitor.
- **`_scripts/derive_caci_baseline.py`** — regenerates the `baseline_caci_footprint:` block from a USAspending pass on CACI entities. Operator-triggered, not automatic.
- **`_scripts/derive_caci_directional.py`** — regenerates the `directional_caci_footprint:` block from a CACI careers / IR scrape.

### Libraries

- **`_scripts/lib/sam_gov.py`** — SAM.gov v2 search API client. Tier-aware daily quota tracking, polite throttle, 429 retry-with-backoff, pagination via offset, posted-date span logging.
- **`_scripts/lib/usaspending.py`** — USAspending search API client. Polite throttle, daily counter.

## Data flow

```
SAM.gov v2 search API
       ↓ (8 slices via lib/sam_gov.py)
find_seeds.py
       ↓ (fingerprint dedup against seeds-ledger.json)
       ↓ (5-pillar scoring against caci-discovery-config.yaml)
       ↓ (out-of-scope cap)
       ↓ (3-way classification)
seeds-inbox.md  +  seeds-inbox.csv
       ↓ (operator marks [x] promote / drop / monitor)
approve_seeds.py
       ↓
opportunities/<ID>/  OR  seeds-rejected.md  OR  (stays in inbox)
```

## Operational commands

```bash
# Full 8-slice batch (default — all slices, 56-day lookback, paginated)
SAM_GOV_TIER=non_federal python3 _scripts/find_seeds.py --source sam-gov

# Single slice (validation / debugging)
SAM_GOV_TIER=non_federal python3 _scripts/find_seeds.py --source sam-gov --slices nav_yokosuka

# Process triaged seeds (after operator marks them in seeds-inbox.md)
python3 _scripts/approve_seeds.py

# Regenerate baseline footprint from USAspending
python3 _scripts/derive_caci_baseline.py
```

## What's empirically verified

| Slice | Status | Notes |
|---|---|---|
| `nav_yokosuka` | **Verified 2026-05-31** — 29 records over 56 days |
| `af_yokota` (374 CONS) | **Verified 2026-06-01** — 18 records over 56 days; PACAF Yokota AB; cross-service coverage (Camp Zama work) |
| `nav_pearl_harbor` | Candidate, not yet run |
| `nav_san_diego` | Candidate, not yet run |
| `nav_puget_sound` | Candidate, not yet run |
| `nav_srf_jrmc` | Candidate, not yet run |
| `nav_nswc_corona` | Candidate, not yet run |
| `af_kadena` (18 CONS) | Candidate, not yet run |

### What's NOT verified

- The full 8-slice batch has never run end-to-end with the current organizationName-anchored config.
- The capability-area scoring layer has never seen real surfaced notices — only synthetic tests.
- The OOS gate's tightened thresholds (≥3 keyword overlap on categorical rules; code+keyword on code-anchored rules) are validated against synthetic seeds only. The 12 rounds of closure rules accumulated against a 3-day data window; new 56-day data will surface false-positive shapes the existing rules don't catch.

## SAM.gov v2 parameters — what works, what doesn't

Empirical findings as of 2026-05-31:

| Parameter | Status | Notes |
|---|---|---|
| `organizationName` | **Works** — text-substring match on the awarding org name | Primary slice filter |
| `ptype` | Works | Multi-value comma-separated, e.g. `r,s,p,k` for Sources Sought + Special Notice + Presolicitation + Combined Synopsis |
| `deptname` | Works (deprecated in v2 docs but still honored) | Currently not used in slices since `organizationName` is more selective |
| `subtier` | Works (deprecated in v2 docs but still honored) | Not currently used |
| `state` | Works (US-only two-letter codes) | Not currently used |
| `postedFrom` / `postedTo` | Works | Format `MM/DD/YYYY` |
| `limit` / `offset` | Works | Used for pagination |
| `ncode` (NAICS) | **Silently ignored** | Returns the unfiltered pool with totalRecords matching the no-filter call |
| `naicsCode` (NAICS, SDK form) | **Silently ignored** | Same as above |
| `ccode` (PSC) | **Silently ignored** | Not honored |
| `q` (keyword) | **Silently ignored** | Returns unfiltered pool regardless of input |
| `placeOfPerformanceCountry` | **Silently ignored** | Confirmed via direct test 2026-05-31 |

A query with an unrecognized parameter does NOT error — it returns the unfiltered result. This is what made the v2 API documentation gap especially expensive to discover.

## Recent design history

- **Sessions 2026-05-29 to 2026-05-31:** Built the seed-finder pipeline, 12 rounds of closure-rule triage (88 surfaced seeds → 0 unmarked + 4 monitors), discovered SAM.gov v2 silently ignores `ncode` / `ccode` / `q` parameters.
- **2026-05-31:** Added pagination to `lib/sam_gov.py`. Discovered the 1000-record per-page cap binds at ~3 days of the 56-day window (totalRecords=20,678 for unfiltered DoD; pagination needed for full coverage).
- **2026-05-31:** Three rounds of Gemini red-team on the slice plan. Verified `organizationName` is the only working filter. Rewrote `sam_searches` around organizationName-anchored slices for Pacific Navy and Air Force offices.
- **2026-06-01:** Built the CACI capability book (`_meta/caci-capability-book/`). Wired it into the scorer as a fifth pillar (`pillar_capability_area`) + three-way classification. Tightened the OOS gate after a structural false-positive on a legitimate naval-architecture notice.
- **2026-06-02:** System named "Opportunity Screening" and this README created.

## Known issues and limitations

- **Closure rules calibrated against thin data.** See "What's NOT verified" above. Plan is cluster-triage via `seeds-inbox.csv` after the first 8-slice batch.
- **Six of eight organizationName slices unverified.** First batch run will reveal whether the candidate names work.
- **No daily-delta slice.** The original plan had a short-lookback daily-delta slice for continuous monitoring; it was dropped when we pivoted to org-name anchoring. Could be re-added if needed.
- **Triage UX is binary-on-three-classifications.** The scorer surfaces direct_execute / relationship_lead / customer_intel labels but the operator's triage actions remain promote / drop / monitor. Whether the three classifications get differentiated downstream paths is a design question deferred until real notices flow through.
- **Vault gap closures pending.** Two unnamed FY24 CACI acquisitions, USAspending per-award dollar amounts, specific IAC under DTIC IAC MAC. None block the pipeline.

## Related skills and references

- `_meta/grill-me.md` — alignment skill (run before any new opportunity scaffolding)
- `_meta/entity-provenance-check.md` — named-entity audit
- `_meta/oci-primer.md` — FAR 9.5 OCI background (relevant for any SRF-JRMC pursuit promotion)
- `_meta/small-ships-workflow.md` — section-by-section brief drafting
- `_meta/named-entities-watchlist.yaml` — vault-wide named-entity vigilance list

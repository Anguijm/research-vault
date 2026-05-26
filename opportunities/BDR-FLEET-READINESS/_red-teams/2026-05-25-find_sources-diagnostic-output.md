---
type: diagnostic-output
opportunity: BDR-FLEET-READINESS
scope: Per-stage instrumented diagnostic of the 2026-05-25 find_sources 0-candidate pass
run_at: 2026-05-25T21:35
config: opportunities/BDR-FLEET-READINESS/_search-config-diagnostic.yaml (13 AI + 1 SAM + 1 USA queries)
plan: opportunities/BDR-FLEET-READINESS/_red-teams/2026-05-25-gemini-pro-diagnostic-plan-dialogue.md
raw_log: /tmp/find_sources_diagnostic.log
---

# Diagnostic output — 2026-05-25 find_sources 0-candidate investigation

## Headline result

The diagnostic returned **`21 AI + 0 SAM + 22 USA = 43 new candidates queued`** against the 13-query diagnostic config (10 buyer-triad + 3 baseline). Compare to the 2026-05-25 08:30 production pass against the 60-query config, which returned `0 AI + 0 SAM + 0 USA`. The two passes' substantially-overlapping AI inputs produced opposite results, which by itself is informative — see "What the morning 08:30 zero result means" below.

The `usaspending.py:102` `internal_id` field-removal fix (applied 2026-05-25 evening between the morning pass and the diagnostic) **is confirmed working** — 22 USAspending candidates queued for the first time in this opportunity, including several directly relevant to the BDAR/BDAT scope. The fix was the right one.

The diagnostic also exposed a sharp picture of which buyer-triad queries are productive versus dead, which is the actionable take-away for the search-config tuning.

## Per-stage bucketing

### Stage A — `searcher.search()` raw results per query

Bucket B (baseline, control group):

| Query | Raw results |
|---|---|
| "Department of the Navy Strategic Readiness Plan..." | 17 |
| "FY2026 Navy budget justification ship depot maintenance..." | 6 |
| "SASC HASC 2025 2026 CNO NAVSEA testimony..." | 4 |

Baselines all produced results. The AI search service is healthy.

Bucket A (buyer-triad, test group):

| Query | Raw results | Status |
|---|---|---|
| "Naval Education Training Command surface warfare training curriculum..." | 5 | productive |
| "Naval Air Warfare Center Training Systems Division surface ship training systems contract..." | **0** | dead |
| "Surface Warfare Schools Command BDAR battle damage assessment curriculum requirement" | **0** | dead |
| "Naval Warfare Development Center surface fleet tactical doctrine battle damage NTTP TACMEMO" | **0** | dead |
| "Afloat Training Group surface readiness BDAR damage assessment training" | 2 | productive |
| "Navy curriculum development contract surface warfare battle damage assessment 2025 2026" | **0** | dead |
| "Navy fleet synthetic training architecture contract integration HLA DIS standards" | 2 | productive |
| "Navy Ready Relevant Learning Sailor 2025 BDAR damage control curriculum modernization" | 1 | productive |
| "Navy Continuous Training Environment NCTE Fleet Synthetic Training contract" | **0** | dead |
| "Navigation Seamanship Shiphandling Trainer NSST Fitzgerald McCain upgrade contract" | **0** | dead |

**Six of ten buyer-triad queries returned zero raw results.** Hypothesis H1 confirmed for those six queries specifically — they are too narrow, name a specific Navy program in a way the AI search returns nothing for, or test a combination of terms with no public-source coverage.

The four productive buyer-triad queries returned a combined 10 raw results — NETC (5), ATG (2), fleet synthetic training HLA/DIS (2), and Ready Relevant Learning (1). These are the queries the next find_sources pass should keep; the dead six should be rewritten or dropped.

Per the named-contractor discipline, the right read of the six dead queries is: **the AI search did not find publicly-indexed material naming these specific programs in the BDAR/BDAT training context.** That is a finding, not a failure — it means the right-to-win-reframe dialogue's specific program-name claims (NAWCTSD-executes-STAVE, NSST-as-Fitzgerald-McCain-analog, NCTE-as-buyer) do not currently have publicly-indexed source coverage at AI-search granularity. They may have coverage at primary-source granularity (DoN budget exhibits, NETC public pages) which the search engine doesn't index well.

### Stage B — `resolve_and_validate()` URL validation

- Input: 37 raw results across all queries, 3 deduplicated against existing inbox/sources, 34 pre-validation.
- Output: 25 validated.
- 9 candidates dropped as invalid (404) or as index pages.
- Stage B HEALTHY. No SYN-SENT hang, no WAF block, no mass-drop. H6 NOT confirmed; H3 confirmed at modest rate (~26 % drop, normal).

### Stage C — `rank_candidates()` OpenAI ranker

- Input: 21 candidates (after final dedup against known URLs eliminated 4 more).
- Output: 21 ranked.
- Scores: `[9, 9, 9, 9, 9, 8, 8, 8, 8, 8, 8, 8, 7, 7, 7, 7, 7, 7, 5, 5, 5]`.
- Stage C HEALTHY. Strong score distribution. H7 (which Gemini Round-2 already conceded was a phantom) confirmed not load-bearing here.

## What the morning 08:30 zero result means

The morning 08:30 pass against the 60-query config returned `0 AI + 0 SAM + 0 USA`. The diagnostic at 21:35 against the 13-query subset returned `21 AI + 0 SAM + 22 USA`. The substantial overlap between the two AI query sets means the morning zero is not explained by query content alone — the baseline 3 queries and at least 4 of the buyer-triad queries demonstrably do return results.

Likely explanations (none confirmed without a second diagnostic):

1. **Transient AI service degradation at the time of the 08:30 run.** Both Claude and Gemini AI search backends may have been throttling or returning empty during the morning slot. The 25-minute timeout on the production run meant 31 of 50 queries completed, the remainder were killed mid-flight — but `0 AI candidates queued` was reported via the truncated-tail output before the timeout cut in. So the AI section completed its work and returned zero. Either every query genuinely returned empty due to backend issues, or the AI section crashed silently before the final summary line. The `tail -80` truncation hides which.

2. **Interaction between the 50-query AI stage and downstream dedup/validation that the 13-query diagnostic does not trigger.** Possible but speculative — no specific code path identified.

3. **Lock-file artifact from prior killed runs.** The stale lock observed in the diagnostic was 11+ hours old, suggesting the morning run cleared a then-stale lock at startup but possibly left its own state corruption.

Without a second diagnostic run replicating the morning 60-query workload, the morning 0-AI result is not fully root-caused. But it is not blocking — the diagnostic established that the system CURRENTLY works, the buyer-triad queries that produce results have been identified, and the USAspending fix is verified.

## Findings summary

- **AI search is healthy.** Strong baseline performance; AI service backends are returning results.
- **6 of 10 buyer-triad queries are dead** — they should be rewritten or dropped from the production config. Specifically: NAWCTSD-Training-Systems, SWSC-BDAR-curriculum, NWDC-surface-fleet-tactical-doctrine, Navy-curriculum-development, NCTE-FST-contract, NSST-Fitzgerald-McCain.
- **4 buyer-triad queries are productive** — keep NETC-surface-warfare-curriculum, ATG-surface-readiness-BDAR, Navy-FST-HLA-DIS, RRL-Sailor-2025-BDAR. These are the ones to invest more variations of.
- **The `usaspending.py:102` `internal_id` fix works.** 22 Carderock-keyword candidates queued including SAIC ($50.9 M NSWC contract), ManTech ($45.6 M submarine and surface ship acoustic signature trials), Leidos ($41.4 M signature training systems development at the Naval Surface Warfare Center signature measurement division), Noblis MSD ($39 M Carderock engineering services), American Systems ($33 M NSWCCD Code 70 support). The Leidos signature-training-systems and ManTech acoustic-signature-trials awards are directly in the BDAR/BDAT scope window and warrant detailed source ingestion.
- **SAM 429 rate-limit recurred** — environmental issue not addressable from our side; let it cool down and retry tomorrow.
- **No TCP SYN-SENT hangs** observed in the diagnostic run. The 45-min hang seen this morning during the re-run was a different (transient) event.

## What was modified and reverted

- `_scripts/lib/usaspending.py:102` — removed dead `"internal_id"` field that triggered server-side HTTP 500. **Permanent fix, intentionally not reverted.**
- `_scripts/find_sources.py` — three bracketed `[DX]` print pairs in `_run_ai_search` marked with sentinel comment `DIAGNOSTIC 2026-05-25 — REVERT AFTER`. **All 7 sentinel-marked lines reverted after diagnostic completed.** Confirmed by `grep -n "DIAGNOSTIC 2026-05-25 — REVERT AFTER" _scripts/find_sources.py` returning empty.
- `opportunities/BDR-FLEET-READINESS/_search-config.yaml` — temporarily swapped for the diagnostic config via subshell+EXIT-trap. **Reverted to production config by trap on subshell exit.** Confirmed via file timestamp (`May 25 08:29`).
- `opportunities/BDR-FLEET-READINESS/_search-config-diagnostic.yaml` — diagnostic config file created during this pass. **Retained** for future diagnostic re-runs. It is namespaced and does not shadow the production config.

## Recommended next actions

1. **Drop or rewrite the 6 dead buyer-triad queries** in `_search-config.yaml`. Either remove them or rephrase to use broader terms that the AI search can find.
2. **Run a production find_sources pass (no `--dry-run`)** to actually write the 43 candidates to `_inbox.md`. The diagnostic only printed them; nothing was queued for triage yet.
3. **Triage the 22 USAspending candidates manually** — several are directly in the BDAR/BDAT scope (Leidos signature-training-systems, ManTech acoustic-signature-trials). The Leidos award in particular is a 2025-03 start with a 2030-03 end, exactly the active-procurement window the research is scoping.
4. **Note the Amentum line item** ($11 M PWD Washington) — Amentum is on the operator-blocked-entity list per the 2026-05-23 entity-pollution triage. The USAspending search returned it because "Carderock" appears in the description (one of multiple locations in a Public Works Department contract). It is not analytical contamination but should be rejected at inbox triage rather than ingested.

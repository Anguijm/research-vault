# Defense Research Vault — Dashboard

**Last updated:** 2026-06-01
**Operator:** John Anguiano (anguijm)
**SOP:** [[_meta/sop]]  |  **Verification rules:** [[_meta/verification-rules]]

---

## Active opportunities

```dataview
TABLE WITHOUT ID
  file.link AS Opportunity,
  customer AS Customer,
  gate AS Gate,
  status AS Status,
  next_action AS "Next Action",
  next_action_due AS Due,
  last_updated AS Updated
FROM "opportunities"
WHERE type = "opportunity" AND gate != "won" AND gate != "lost" AND gate != "dropped"
SORT next_action_due ASC
```

---

## This month's focus

```dataview
TABLE WITHOUT ID link(file.path, id) AS Opportunity, status AS Status, next_action AS "Next action", next_action_due AS Due
FROM "opportunities"
WHERE type = "opportunity" AND focus_month AND focus_month.year = date(today).year AND focus_month.month = date(today).month
```

---

## Stalled (no update in 14+ days)

```dataview
TABLE WITHOUT ID
  file.link AS Opportunity,
  status AS Status,
  last_updated AS "Last Updated"
FROM "opportunities"
WHERE type = "opportunity" AND last_updated < date(today) - dur(14 days) AND gate != "won" AND gate != "lost" AND gate != "dropped"
SORT last_updated ASC
```

---

## Re-verification queue (POCs due within 7 days)

```dataview
TABLE WITHOUT ID
  file.link AS "POC File",
  opportunity AS Opportunity,
  last_reviewed AS "Last Reviewed",
  review_due AS "Review Due"
FROM ""
WHERE type = "pocs" AND review_due <= date(today) + dur(7 days)
SORT review_due ASC
```

---

## Pipeline by capability area

```dataview
TABLE WITHOUT ID
  length(rows) AS Count
FROM "opportunities"
WHERE type = "opportunity" AND gate != "lost" AND gate != "dropped"
FLATTEN capability_tags AS tag
GROUP BY tag
SORT Count DESC
```

---

## Auto-find status

```dataview
TABLE WITHOUT ID
  link(file.path, id) AS Opportunity,
  auto_find AS Enabled,
  last_find_run AS "Last Run",
  last_find_count_ai AS "AI Hits",
  last_find_count_sam AS "SAM Hits",
  last_find_count_usa AS "USA Hits",
  choice(last_find_run AND date(today) - date(last_find_run) > dur(1 day), "⚠️ STALE", "✓") AS Status
FROM "opportunities"
WHERE type = "opportunity" AND auto_find != false
SORT last_find_run DESC
```

---

## Seeds-inbox state

The seed-finder pipeline (`_scripts/find_seeds.py`) surfaces candidate Navy / DoD opportunities from SAM.gov, war.gov, and DoD Comptroller justification books. Operator triages candidates into one of three states: promote (creates an opportunity folder), drop (added to seeds-rejected.md), or monitor (kept in inbox for later review).

- **Inbox:** [[_meta/seeds-inbox|seeds-inbox.md]]
- **Rejected log:** [[_meta/seeds-rejected|seeds-rejected.md]]
- **Ledger (fingerprint dedup):** `_meta/seeds-ledger.json`
- **Discovery config (slice plan + closure rules):** [[_meta/caci-discovery-config|caci-discovery-config.yaml]]

> **2026-06 note:** SAM.gov query layer is partially broken. Empirical testing on 2026-05-31 confirmed v2 search ignores `ncode`, `ccode`, and `q` parameters; only `organizationName` filters. Slice plan needs rewrite around organizationName-anchored queries for Pacific Navy + Air Force contracting offices. The 12 rounds of out-of-scope closure rules in `caci-discovery-config.yaml` were calibrated against the 3-day data window the broken slices were returning — recalibration expected after the slice-plan rewrite.

---

## CACI capability book

Corporate-level scoring-layer asset. Eight files documenting CACI's seven capability areas (C3I, Cyber, Digital Solutions, Enterprise IT, Mission and Engineering Support, Space, Spectrum Superiority), FY25/FY26 financial context, growth signals, acquisitions, contract vehicles, and top-25 past performance.

- **Index:** [[_meta/caci-capability-book/README|capability book README]]
- **7-area taxonomy:** [[_meta/caci-capability-book/capability-areas|capability-areas.md]]
- **Current-state growth signals (FY26 Q3):** [[_meta/caci-capability-book/growth-signals|growth-signals.md]]
- **Vehicles:** [[_meta/caci-capability-book/vehicles|vehicles.md]] — includes the operator-team's DTIC IAC MAC (FA807518D0006), recompete 2027-09-29
- **Acquisitions:** [[_meta/caci-capability-book/acquisitions|acquisitions.md]] — 8 identified, 2 unnamed FY24 entries pending
- **Past performance:** [[_meta/caci-capability-book/past-performance/top-25-by-amount|top-25-by-amount.md]]

---

## Quick links

- [[_meta/sop|SOP]]
- [[_meta/verification-rules|Verification rules (printable)]]
- [[_meta/glossary|Vault glossary]]
- [[_meta/oci-primer|OCI primer]]
- [[_meta/grill-me|Grill-me alignment skill]]
- [[_meta/small-ships-workflow|Small-ships brief workflow]]
- [[_meta/entity-provenance-check|Entity-provenance-check skill]]
- [[_meta/prompts/README|Prompt library README]]
- [[_meta/monthly-log|Monthly log]]
- [[_meta/cron-log|Cron log (automated find_sources runs)]]

**Starting a new opportunity?** Clone the folder structure using [[_templates/new-opportunity-instructions|new opportunity instructions]] — but FIRST run the [[_meta/grill-me|grill-me alignment skill]] (CLAUDE.md mandates this before any work that produces a durable artifact).

**Beginning research on an opportunity?** Start with [[_meta/prompts/source-gathering|source-gathering prompt]] (Gemini).

**Extracting quotes from a source?** Use [[_meta/prompts/quote-extraction|quote-extraction prompt]] (Claude).

**Extracting POCs from a source?** Use [[_meta/prompts/poc-extraction|poc-extraction prompt]] (Claude).

**Drafting a brief?** Use the [[_meta/small-ships-workflow|small-ships workflow]] — section-by-section: FACT list → `verify_facts.py` → prose → red-team per section. Do not draft a full v0.1 and then red-team the whole thing.

**Building a brief artifact (.docx)?** Use `_scripts/build_brief.py` with a per-version YAML config in `_scripts/briefs/<OPPORTUNITY>/`. Do not copy a previous `build_pmtec_*.py` script.

**Ready to red-team a draft?** Use [[_meta/prompts/cross-ai-red-team|cross-AI red team prompt]] (the other model). Note: cross-AI red-team can pull brainstorms off-course — treat critique as input, not directive.

**Distilling to exec brief?** Use [[_meta/prompts/distillation-capture-to-exec|distillation prompt]] (Claude).

**Monday triage scan?** Use [[_meta/prompts/weekly-scan|weekly scan prompt]] (Gemini).

# Defense Research Vault — Dashboard

**Last updated:** (update manually each session, or install Templater for auto-date)
**Operator:** [your name]
**SOP:** [[_meta/sop]]  |  **Verification rules:** [[_meta/verification-rules]]

---

## This month's focus

```dataview
TABLE WITHOUT ID link(file.path, id) AS Opportunity, status AS Status, next_action AS "Next action", next_action_due AS Due
FROM "opportunities"
WHERE type = "opportunity" AND focus_month AND focus_month.year = date(today).year AND focus_month.month = date(today).month
```

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

## Quick links

- [[_meta/sop|SOP]]
- [[_meta/verification-rules|Verification rules (printable)]]
- [[_meta/prompts/README|Prompt library README]]
- [[_meta/monthly-log|Monthly log]]

**Starting a new opportunity?** Clone the folder structure using [[_templates/new-opportunity-instructions|new opportunity instructions]].

**Beginning research on an opportunity?** Start with [[_meta/prompts/source-gathering|source-gathering prompt]] (Gemini).

**Extracting quotes from a source?** Use [[_meta/prompts/quote-extraction|quote-extraction prompt]] (Claude).

**Extracting POCs from a source?** Use [[_meta/prompts/poc-extraction|poc-extraction prompt]] (Claude).

**Ready to red-team a draft?** Use [[_meta/prompts/cross-ai-red-team|cross-AI red team prompt]] (the other model).

**Distilling to exec brief?** Use [[_meta/prompts/distillation-capture-to-exec|distillation prompt]] (Claude).

**Monday triage scan?** Use [[_meta/prompts/weekly-scan|weekly scan prompt]] (Gemini).

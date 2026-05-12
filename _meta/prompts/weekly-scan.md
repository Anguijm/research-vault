---
type: prompt
name: weekly-scan
recommended_model: gemini
last_revised: 2026-05-11
---

# Weekly / Monday triage scan

**When to use:** Week 1 of each monthly cadence (triage week). Run across SAM.gov, DIU, DVIDS, and Apex Innovates to surface new opportunity signals. Pick one focus opportunity for the month.

**Recommended model:** Gemini (broader/fresher web reach for opportunity discovery).

**The prompt:**

```
You are conducting the Monday weekly triage scan for a defense BD intelligence
operation. Goal: identify new opportunities, signals, or developments from the
past 7 days that warrant a closer look.

Search the following sources for anything dated in the last 7 days:
  1. SAM.gov — new opportunities matching: [paste current saved-search terms]
  2. DIU open solicitations page (diu.mil/work-with-us/open-solicitations)
  3. DVIDS news (dvidshub.net) — filter to relevant commands: [paste list, e.g., USINDOPACOM, USSPACEFORCE]
  4. Apex Innovates events (apex-innovates.org/events)
  5. Trade press headlines from: Breaking Defense, Defense News, DefenseScoop, Inside Defense
  6. Comptroller press releases for any budget reprogramming or FY actions

For each finding, give me:
  - Source and date
  - 1-sentence what
  - 1-sentence why it matters to our portfolio (capability areas: [paste tags])
  - Direct URL
  - Suggested action: monitor / open opportunity folder / dig deeper

Group findings into three buckets:
  - HIGH SIGNAL — directly maps to our portfolio, action recommended.
  - WATCHLIST — adjacent, worth tracking, no action this week.
  - CONTEXT — broader news, no action.

End with a one-paragraph "What changed this week" synthesis covering the most
important 2-3 items. If nothing meaningful happened, say so.

Do not invent sources. If a section returns nothing, say "No findings."
```

**Notes:**
- The SAM.gov saved searches relevant to PMTEC/INDOPACOM are documented in `opportunities/PMTEC-USINDOPACOM/00_research-file.md` Appendix D — paste those terms into `[paste current saved-search terms]`.
- Output of the triage scan feeds into `_meta/monthly-log.md` (Week 1 notes).
- Pick **one** focus opportunity per month. Trying to research two at this team size always fails one of them (per SOP §4).

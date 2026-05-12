---
type: prompt
name: source-gathering
recommended_model: gemini
last_revised: 2026-05-10
---

# Source gathering

**When to use:** At the start of research on a new opportunity, to identify primary sources across a 24-month window. Run this in Week 1–2 of the monthly cadence.

**Recommended model:** Gemini (broader/fresher web reach across DVIDS, trade press, GovConWire, .mil sites).

**The prompt:**

```
You are a defense market intelligence analyst. I am researching [OPPORTUNITY]
for a capture brief. The eight stated priority areas are: [paste].

Find me publicly available primary sources from the past 24 months on this
opportunity, prioritizing in this order:
  1. .mil sites and DVIDS press releases
  2. Comptroller PB justification books
  3. SAM.gov, USAspending.gov, HigherGov contract records
  4. Congressional testimony and GAO reports
  5. Company SEC filings and press releases
  6. Trade press only for context

For each source, give me:
  - Title
  - Publication date
  - Direct URL
  - 2–3 sentence summary of why it's relevant
  - The single most useful verbatim quote (with attribution)

Do not invent sources. If you are uncertain whether a source exists, say so.
```

**Notes:**
- Always verify every URL returned before saving. AIs hallucinate citations — click every link (Rule 6).
- Save raw captures to `01_sources/` only after click-verification. Use `_scripts/ingest.py` (Phase 3) to create properly formatted source files.
- Replace `[OPPORTUNITY]` with the opportunity name (e.g., "USINDOPACOM PMTEC — multi-domain training and experimentation") and `[paste]` with the actual list of stated priority gaps from the customer.

---
type: prompt
name: quote-extraction
recommended_model: claude
last_revised: 2026-05-10
---

# Quote extraction

**When to use:** After capturing a source, to extract all verbatim quotes attributable to named people. Run during Week 2–3 (research phase), one source at a time. Paste results into `02_quotes.md`.

**Recommended model:** Claude (better at "verbatim, with attribution" discipline).

**The prompt:**

```
Here is a source: [paste full source text or URL].

Extract every verbatim quote attributable to a named person, with:
  - Speaker name and exact title
  - Date of statement (or publication date if unclear)
  - Venue (speech, interview, press release, etc.)
  - The quote, exact wording, in quotes
  - Source URL

Do not paraphrase. Do not invent attribution. If a quote in the text is
unattributed in the source, note it as "unattributed in source."
```

**Notes:**
- After running this prompt, open the source URL and verify each extracted quote word-for-word before pasting into `02_quotes.md`. This is non-negotiable (Rule 6).
- Format results in `02_quotes.md` per the schema in `_handoff/HANDOFF.md` §3.3 and the template in `_templates/quotes.md`.
- Set `key_quotes_extracted: true` in the source file's frontmatter once this step is complete.

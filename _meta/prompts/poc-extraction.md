---
type: prompt
name: poc-extraction
recommended_model: claude
last_revised: 2026-05-11
---

# POC extraction

**When to use:** After capturing a source that contains named people, roles, or org information. Run during Week 2–3 (research phase). Paste results into `03_pocs.md`.

**Recommended model:** Claude (better at structured extraction from .mil pages and press releases).

**The prompt:**

```
You are extracting points of contact (POCs) from a defense source document.

Input: a press release, speech, .mil page, news article, or transcript.
Output: a structured list of named individuals, one entry per person.

For each named person in the source, extract:
  - Full name (with rank or honorific if used)
  - Exact role and title as stated in the source
  - Organization
  - Any contact info present in the source (email, phone, portal URL)
  - The verbatim sentence or fragment where they were named (for traceability)
  - Source URL
  - Date of the source

Rules:
  - Only extract people who are explicitly named. No paraphrase, no inference about who "the J7 director" is if not named.
  - If a title is implied but not stated verbatim, mark it [implied].
  - Do not extract authors of news articles unless they are subject-matter participants.
  - If the same person appears in multiple roles, list once with both roles noted.
  - Output as a markdown table with columns: Name | Role | Org | Contact | Quote | Source | Date.

If the source contains no named individuals, return: "No POCs found in this source."
```

**Notes:**
- Format results in `03_pocs.md` per the table schema in `_handoff/HANDOFF.md` §3.3.
- Re-verify all POC entries every 90 days — defense roles rotate. The `review_due` field in `03_pocs.md` frontmatter tracks this.
- Click every source URL before adding a POC to the table (Rule 6).

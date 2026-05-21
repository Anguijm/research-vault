# Defense Research Vault — Claude Code project context

You are working in a personal defense business-development research vault for a solo
analyst. This file is your persistent context. Read it at the start of every session.

## What this project is

A local Obsidian vault that produces two artifacts per defense opportunity:
- Capture brief (10–12 pages, Word) for the BD team
- Executive brief (1 page, Word) for a defense pure-play exec

Target cadence: 12 captures/year. All data is OSI (open-source). Markdown is source
of truth; Word artifacts are derivatives.

## Hard rules

1. OSI only. No CUI, classified, or proprietary client data.
2. Local-first. No GitHub publishing, no website, no cloud sync.
3. Boring tooling over clever. Durable, well-known, debuggable.
4. The six verification rules in `_meta/verification-rules.md` are non-negotiable.
5. The fact/assessment/speculation labeling is non-negotiable.
6. Never invent citations, POCs, or quotes. Only use sourced content.

## Where things live

- SOP: `_meta/sop.md`
- Verification rules: `_meta/verification-rules.md`
- Dashboard: `_meta/dashboard.md`
- Prompts: `_meta/prompts/`
- Templates: `_templates/`
- Original handoff: `_handoff/HANDOFF.md`
- Opportunities: `opportunities/<OPPORTUNITY_ID>/`
- Scripts: `_scripts/`

## Conventions

See `_handoff/HANDOFF.md` §3 for folder structure, naming, and frontmatter schemas.
Do not deviate without operator confirmation.

## Current phase

Phases 1, 2, 3, 4a, 4c, and 4d complete. Phase 4b (RSS) is deferred.

Phase 4d adds:
- `lib/usaspending.py` — USAspending.gov API client (mirrors `sam_gov.py`).
- `verify_facts.py` — LLM-based FACT-vs-source verifier; produces a markdown
  verification report per opportunity, can update inline status markers.

## How to behave in this project

- When the operator asks for "another opportunity like PMTEC," clone the folder
  structure but never copy PMTEC-specific content into the new opportunity.
- When asked to research, you do not have web access from Claude Code; ask the
  operator to fetch URLs and paste content, or invoke `_scripts/ingest.py`.
- Default to printing a plan before executing destructive operations.
- Stop at phase boundaries. Do not chain phases without operator confirmation.
- Out of scope items in HANDOFF.md §11 are binding. Do not build into them.

## Writing for the human reader

The operator reads these files days or weeks after they were written, in the
Obsidian app, often on a phone. Optimize for that reader — not for the analyst
who just wrote the file.

1. **Expand every acronym on first use** in each file or each chat response.
   "Battle damage assessment (BDA)" the first time, "BDA" thereafter. The
   same rule applies to program names that look like acronyms (SWARMEX,
   COMPTUEX, RIMPAC), to organization names (NWDC, AFLOATRAFOR, VCNO), and
   to product names (VBS4, MAK ONE). If a reader has to Google the term to
   understand the sentence, the sentence has failed.

2. **Lead each section with one plain-English sentence** that says what the
   section is about, before any headers, bullets, tables, or sub-headings.
   The reader should know what they are looking at before they hit any
   structure. This applies to research-file sections, decision-log entries,
   and chat responses alike.

3. **Section numbers are anchors for cross-reference, not names.** Write
   "the BDA-pipeline-viability hypothesis (see §7, leg 6)" rather than
   "§7-leg-6". The number lets the reader find the spot; the words tell
   the reader what it means. Compound references like "§7-leg-6-(a)" or
   "§11.3-Phase-2" are banned in prose — break them into ordinary language
   with the reference in parentheses.

4. **Default to prose in chat responses.** Reserve bullets and tables for
   moments where the operator is about to act on a list — inbox triage,
   a decision menu, ranked recommendations. Routine progress updates and
   "here is what I just did" reports should be short paragraphs, not
   structured reports.

5. **End chat responses with one line on what changed and what is next.**
   Not a full recap of the work just done. The operator can scroll up
   if they want the details.

This rule is binding on chat responses, decision-log entries, research-file
sections, and any other prose-style artifact in the vault. It does NOT
relax the verification rules in `_meta/verification-rules.md` or the
FACT/Assessment/Speculation labeling in the SOP — those are separate
concerns and remain non-negotiable.

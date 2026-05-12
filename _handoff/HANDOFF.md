# HANDOFF.md — Defense Research Vault, Phase 1–3 build

**Audience:** Claude Code, taking over a personal research-operations build from a planning conversation.
**Operator:** [you] — solo defense BD analyst, AI-fluent, Linux user, never operationalized Obsidian.
**Goal of this document:** give Claude Code everything it needs to scaffold the system in 1–3 focused sessions without asking the operator decision questions mid-build.

---

## 0. How to read this document

1. Read §1 (mission and constraints) first. Internalize the guardrails. They are load-bearing.
2. Read §2 (SOP) and §3 (conventions) — these are the operating rules of the system you're building.
3. Execute phases in order. Phase 1 → check in → Phase 2 → check in → Phase 3. **Stop at each phase boundary.** Do not chain phases without operator confirmation.
4. Anything not specified is the operator's choice, not yours. Ask, or default to the most conservative option (boring, durable, reversible).
5. The "OUT OF SCOPE" list in §11 is binding. Do not build into those directions even if it would be "easy" or "useful."

---

## 1. Mission and constraints

### 1.1 What we're building

A local Obsidian-based research vault for a one-person defense business-development intelligence operation. The vault produces two artifacts per opportunity:

- **Capture brief** (10–12 pages, Word) for the BD team
- **Executive brief** (1 page, Word) for a defense pure-play exec

Target cadence: **12 capture briefs per year** (≈1/month). The operator works alone with AI assistance (Claude, Gemini) and occasional on-call SMEs.

### 1.2 Hard constraints

- **OSI only.** All data is open-source intelligence. No CUI, no classified, no proprietary client data ever stored here.
- **Local-first.** Vault lives on the operator's Linux machine. No GitHub publishing, no website, no cloud sync as part of this build. Operator's own backup discipline applies.
- **Markdown as source of truth.** Word artifacts are derivatives. Never store working content in proprietary formats.
- **Boring tooling.** Choose durable, well-known tools over clever ones. The operator should be able to grep this vault on a plane in 2030.
- **Python for scripts.** Operator confirmed.
- **Linux conventions.** XDG paths where appropriate. POSIX shell. No Mac/Windows-isms.

### 1.3 The friction this is solving

Operator's stated highest friction: **source gathering**. Reading articles, capturing them in a structured way, naming them consistently, extracting quotes and POCs, updating ledgers — all currently manual and slow. Phase 3 directly attacks this.

Lower-friction but still worth automating: status tracking across opportunities, prompt consistency, 90-day re-verification reminders.

NOT a current friction: the writing itself, the recommendation calls, the human judgment. Do not try to automate those.

### 1.4 What "good" looks like at the end of Phase 3

- Operator opens Obsidian, sees a dashboard with all active opportunities and their state.
- Operator pastes a URL into a terminal command, gets a properly-formatted source file in the right opportunity's folder, with frontmatter, attribution, and a source-ledger entry.
- Operator opens a prompt from `_meta/prompts/`, copies it into Claude or Gemini, gets consistent outputs.
- Templates for capture brief and exec brief are available, properly linked.
- The PMTEC opportunity from the planning conversation exists as a working example folder.

---

## 2. The Standard Operating Procedure (SOP)

This is the operator's existing SOP. **Treat it as authoritative.** The vault and tooling must support this workflow, not replace it. Do not propose changes to the SOP without flagging them explicitly as proposed changes.

### 2.1 The six verification rules (non-negotiable)

1. **Primary source over secondary.** .mil sites, DVIDS, SAM.gov, USAspending.gov, comptroller PB books, GAO reports, congressional testimony, SEC filings. Trade press is for color, not as the only citation for factual claims.
2. **Two-source rule for non-trivial claims.** Money, timelines, named people, org reporting all need two independent sources. Single-sourced claims get marked.
3. **Date-stamp everything.** Every fact carries `[verified YYYY-MM-DD]`. Re-verify POCs and contract data every 90 days.
4. **Label fact / assessment / speculation explicitly.** Three labels, used by name in every brief and research file.
5. **Adversarial review before shipping.** Human on-call analyst or cross-AI red team.
6. **Click every link.** AIs hallucinate citations. The 30-second verification is the difference between intel and a blog post.

### 2.2 Three-gate process

- **Gate 1 — Identify:** opportunity is real and fits portfolio. Output: capture brief v0.x, exec brief draft.
- **Gate 2 — Pursue:** worth pursuit investment. Output: capture brief v1.0, exec recommendation, teaming letters in motion.
- **Gate 3 — Bid:** RFP out, bid/no-bid decision. Output: bid memo.

Status values in frontmatter must include these gates plus working states (see §3.3).

### 2.3 Monthly cadence

- **Week 1 — Triage:** scan SAM.gov, DIU, DVIDS, Apex Innovates. Pick focus opportunity.
- **Weeks 2–3 — Research:** source gathering, quote/POC extraction, working analysis.
- **Week 4 — Distill and ship:** draft capture brief, cross-AI red team, human review, derive exec brief, ship.

### 2.4 Sensitivity tiers

Every section of a capture brief is tagged with one of three sensitivity tiers. The shareable version is generated by deletion, not rewrite.

- **Internal:** competitive assessments, strategy, pricing posture. Never leaves the company.
- **Shareable:** customer landscape, demand signal, opportunity description, public-source competitive context. OK for NDA'd partner conversations.
- **Public:** facts already in the public domain. OK for thought leadership.

---

## 3. Vault structure and conventions

### 3.1 Folder structure

```
~/research/                           # vault root (operator may rename)
├── _meta/
│   ├── sop.md                        # the full SOP
│   ├── verification-rules.md         # the six rules, printable
│   ├── dashboard.md                  # live dashboard, Dataview queries
│   ├── monthly-log.md                # what was worked on each week
│   └── prompts/
│       ├── source-gathering.md
│       ├── quote-extraction.md
│       ├── cross-ai-red-team.md
│       ├── distillation-capture-to-exec.md
│       ├── poc-extraction.md
│       └── weekly-scan.md
├── _templates/
│   ├── opportunity-index.md
│   ├── research-file.md
│   ├── quotes.md
│   ├── pocs.md
│   ├── decision-log.md
│   ├── source.md
│   ├── capture-brief-template.docx
│   └── executive-brief-template.docx
├── _handoff/                         # original artifacts from planning
│   ├── HANDOFF.md                    # this file
│   ├── capture_brief_template.docx
│   ├── executive_brief_template.docx
│   └── research_workflow_sop.md
├── _scripts/
│   ├── ingest.py                     # Phase 3
│   ├── lib/
│   │   ├── __init__.py
│   │   ├── frontmatter.py
│   │   ├── routing.py
│   │   ├── fetchers/
│   │   │   ├── __init__.py
│   │   │   ├── web.py
│   │   │   ├── pdf.py
│   │   │   └── youtube.py
│   │   └── ledger.py
│   ├── requirements.txt
│   ├── .env.example
│   └── README.md
└── opportunities/
    └── PMTEC-USINDOPACOM/            # one folder per opportunity
        ├── index.md                  # YAML frontmatter, working summary
        ├── 00_research-file.md
        ├── 01_sources/
        │   └── [YYYY-MM-DD]_[domain]_[slug].md
        ├── 02_quotes.md
        ├── 03_pocs.md
        ├── 04_artifacts/
        │   ├── capture-brief-v0.1-draft.docx
        │   ├── capture-brief-v1.0-internal.docx
        │   ├── capture-brief-v1.0-shareable.docx
        │   └── executive-brief-v1.0.docx
        └── 05_decision-log.md
```

### 3.2 Naming conventions

- **Opportunity folders:** `[OPPORTUNITY]-[CUSTOMER]` in caps, hyphenated. Example: `PMTEC-USINDOPACOM`.
- **Source files:** `[YYYY-MM-DD]_[domain]_[short-slug].md` where the date is the capture date (when YOU saved it), not the publication date. Example: `2026-04-22_pacom-mil_industry-partners.md`.
- **Artifact versioning:** `v0.x` drafts, `v1.0` first shipped, `v1.1` minor edits, `v2.0` re-research at next gate. Suffix sensitivity tier: `-internal`, `-shareable`, `-public`.

### 3.3 Frontmatter schemas

Every file with structure carries YAML frontmatter. The schemas below are binding — Dataview queries depend on them.

#### Opportunity `index.md`

```yaml
---
type: opportunity
id: PMTEC-USINDOPACOM
title: USINDOPACOM PMTEC — multi-domain training & experimentation
customer: USINDOPACOM J7
gate: identify           # identify | pursue | bid | won | lost | dropped
status: research         # triaged | research | drafting | review | shipped | stalled
recommendation:          # pursue-prime | pursue-sub | pass | tbd
  - tbd
capability_tags:
  - LVC
  - EW
  - C5ISR
  - space
  - C-UAS
sensitivity: internal
opened: 2026-05-08
last_updated: 2026-05-10
next_action: Send brief to exec for review
next_action_due: 2026-05-20
focus_month: 2026-05
---
```

#### Source file

```yaml
---
type: source
opportunity: PMTEC-USINDOPACOM
title: USINDOPACOM Seeks Industry Partners to Address Modern Military Challenges
url: https://www.pacom.mil/About-USINDOPACOM/PMTEC/Article/4467480/...
publisher: pacom.mil
publication_date: 2026-04-22
captured: 2026-05-10
captured_by: operator                 # operator | ingest.py
source_tier: 1                        # 1=primary .mil/gov | 2=SEC/IR | 3=aggregator | 4=trade press | 5=think-tank | 6=blog/social
content_type: article                 # article | press_release | speech | transcript | pdf | youtube | other
key_quotes_extracted: false           # set true once 02_quotes.md updated
verified: 2026-05-10
---
```

#### POC entry (table row format in `03_pocs.md`)

POCs live as a markdown table inside `03_pocs.md` rather than separate files. The table columns are fixed:

```
| Name | Role | Org | Email/Contact | Source URL | Verified |
```

A separate frontmatter block at the top of `03_pocs.md`:

```yaml
---
type: pocs
opportunity: PMTEC-USINDOPACOM
last_reviewed: 2026-05-10
review_due: 2026-08-08
---
```

#### Quotes file (`02_quotes.md`)

Frontmatter at top:

```yaml
---
type: quotes
opportunity: PMTEC-USINDOPACOM
last_updated: 2026-05-10
---
```

Body is structured markdown with each quote as a level-2 section:

```markdown
## [Speaker name], [Role]

> "[exact verbatim quote]"

— [Venue], [Date]. Source: [URL]. Verified [YYYY-MM-DD]. Tier: [1-6].
```

### 3.4 Sensitivity tags inline

When marking sections within a brief or research file for sensitivity, use HTML comments:

```markdown
<!-- sensitivity:internal -->
This section contains competitive assessment and never leaves the company.
<!-- /sensitivity -->
```

This survives markdown rendering, is easy to grep, and a future script can use it to generate the shareable version.

### 3.5 Fact / Assessment / Speculation labels

In research files and brief drafts:

```markdown
**FACT:** PMTEC was established in 2022 by USINDOPACOM J7 [s.2026-04-22-pacom].
**Assessment:** CACI's post-ARKA capability stack is a credible fit for SDA PWSA pull-through.
**Speculation:** PMTEC's FY27 funding will exceed FY26 by 15–20%; needs corroboration.
```

The `[s.YYYY-MM-DD-slug]` pattern is the inline source citation — a shortcode pointing to a file in `01_sources/`.

---

## 4. Dashboard design

The dashboard lives at `_meta/dashboard.md` and uses the Dataview plugin. Build the queries to be tolerant of missing fields — opportunities being initialized may not have all frontmatter filled in yet.

### 4.1 Queries to build

**Active opportunities table:**
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

**This month's focus:**
```dataview
LIST
FROM "opportunities"
WHERE type = "opportunity" AND focus_month = "2026-05"
```
(The "2026-05" should be templated or replaceable; consider making it dynamic via a Templater plugin variable in a future phase.)

**90-day re-verification queue (POCs):**
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

**Pipeline by capability area:**
```dataview
TABLE WITHOUT ID
  length(rows) AS Count
FROM "opportunities"
WHERE type = "opportunity" AND gate != "lost" AND gate != "dropped"
FLATTEN capability_tags AS tag
GROUP BY tag
SORT Count DESC
```

**Stalled (no update in 14+ days):**
```dataview
TABLE WITHOUT ID
  file.link AS Opportunity,
  status AS Status,
  last_updated AS "Last Updated"
FROM "opportunities"
WHERE type = "opportunity" AND last_updated < date(today) - dur(14 days) AND gate != "won" AND gate != "lost" AND gate != "dropped"
SORT last_updated ASC
```

### 4.2 Dashboard structure

The dashboard note should have these sections, in order:

1. **Header** — today's date (auto via Templater if available, else manual), operator name, link to SOP.
2. **This month's focus** — single opportunity, link to its folder.
3. **Active opportunities** — the table.
4. **Stalled** — the stalled table.
5. **Re-verification queue** — POCs and contract data due for review.
6. **Pipeline by capability** — the grouped count.
7. **Quick links** — to `_meta/sop.md`, `_meta/verification-rules.md`, `_meta/prompts/`, and the most recent monthly log.

---

## 5. Prompt library

The prompt library lives at `_meta/prompts/` with one markdown file per reusable prompt. Each file has the prompt text in a code block, plus brief notes on when to use it and which model to use.

### 5.1 Required prompts to scaffold in Phase 2

1. **`source-gathering.md`** — broad scan for an opportunity (use Gemini for breadth).
2. **`quote-extraction.md`** — verbatim quotes from a source (use Claude).
3. **`cross-ai-red-team.md`** — three-pass red team (customer / competitor / skeptical exec).
4. **`distillation-capture-to-exec.md`** — capture brief → 1-page exec brief.
5. **`poc-extraction.md`** — structured POC extraction from a source.
6. **`weekly-scan.md`** — Monday triage scan across SAM.gov / DIU / DVIDS / Apex Innovates.

Full prompt text for each is in the operator's existing SOP at `_handoff/research_workflow_sop.md` — copy from there. Do not invent new prompts in Phase 2.

### 5.2 Format for each prompt file

```markdown
---
type: prompt
name: source-gathering
recommended_model: gemini
last_revised: 2026-05-10
---

# Source gathering

**When to use:** at the start of research on a new opportunity, to identify primary sources across a 24-month window.

**Recommended model:** Gemini (broader web reach for fresh content).

**The prompt:**

​```
You are a defense market intelligence analyst...
[full prompt body here]
​```

**Notes:**
- Always verify every URL returned. AIs hallucinate citations.
- Save raw responses to `01_sources/` only after click-verification.
```

---

## 6. PHASE 1 — Vault scaffold

**Goal:** create the folder structure, templates, SOP files, and a working PMTEC opportunity folder seeded with content from the planning conversation. Operator can open Obsidian and see something usable.

**Session target:** 1–2 hours.

### 6.1 Tasks

1. **Pre-flight check.** Confirm operator's `~/research/` (or chosen vault path) does not already exist with conflicting content. If it does, ask before overwriting.
2. **Create folder structure** per §3.1. Use `mkdir -p`.
3. **Write `_meta/sop.md`** — copy the operator's existing SOP from `_handoff/research_workflow_sop.md`. Do not paraphrase or edit.
4. **Write `_meta/verification-rules.md`** — extract just §3 of the SOP (the six rules) as a printable one-page document.
5. **Write `_meta/dashboard.md`** — per §4 above, all five Dataview queries, with the structure described in §4.2. Use a clearly marked placeholder for `focus_month` value the operator updates monthly.
6. **Write `_meta/monthly-log.md`** — a starter template with sections for each upcoming month, currently just `## 2026-05`.
7. **Create `_templates/`** files per §3.3 frontmatter schemas. The .docx templates are copied from `_handoff/` — do not regenerate them; they're already validated.
8. **Migrate PMTEC content into `opportunities/PMTEC-USINDOPACOM/`.** Source material:
   - The existing `_handoff/capture_brief_template.docx` IS the PMTEC capture brief content — place a copy at `04_artifacts/capture-brief-v0.1-draft.docx`.
   - The `_handoff/executive_brief_template.docx` similarly → `04_artifacts/executive-brief-v0.1-draft.docx`.
   - Build `index.md` with the YAML frontmatter from §3.3 populated from the PMTEC research.
   - Build `00_research-file.md` per §3.5 patterns, populated from the PMTEC content in the planning conversation. Include the eight priority gaps, the customer landscape, the funding signal, the competitive landscape, the CACI fit assessment, and the recommendation — using FACT/Assessment/Speculation labels.
   - Build `02_quotes.md` with at least the quotes attributed to Brent Parker, Dr. Andre Stridiron, and Mary Ann Swendsen from the planning research. Frontmatter at top.
   - Build `03_pocs.md` with the full POC table from §3 of the planning conversation (Brent Parker, Stridiron, Bednarcik, Swendsen, Emslie, Hannah, Matsunaka, Hall, Nguyen, Goodman, Jordan). Frontmatter with `last_reviewed: 2026-05-10` and `review_due: 2026-08-08`.
   - Build `05_decision-log.md` with the first entry: "2026-05-10 — Opportunity opened, initial research complete, Gate 1 brief drafted."
9. **Create `_scripts/` skeleton** — empty directory with a `README.md` placeholder stating "Phase 3 will populate this directory."
10. **Write `CLAUDE.md`** at vault root — see §10 for the exact content.
11. **Print a summary** for the operator: what was created, what to do next (install Obsidian + Dataview, open vault, verify dashboard renders, check PMTEC folder).

### 6.2 Phase 1 stop point

After completing Phase 1, **stop**. Print a summary including:
- List of files created (counts by folder)
- Confirmation that PMTEC folder is populated
- Verification that all YAML frontmatter is valid
- Recommended operator checks before proceeding to Phase 2

Wait for operator confirmation before starting Phase 2.

### 6.3 What Phase 1 must NOT do

- Do not install Obsidian, Dataview, or any external software. Operator does that.
- Do not push to git or any remote. No version control yet.
- Do not write any Python scripts. That's Phase 3.
- Do not invent new POCs, quotes, or facts. Only use content from the planning conversation already in `_handoff/`.

---

## 7. PHASE 2 — Dashboard polish and prompt library

**Goal:** dashboard renders correctly with PMTEC populated, prompt library is operator-usable.

**Session target:** 1–2 hours.

### 7.1 Tasks

1. **Verify the dashboard renders.** This may require operator to confirm Dataview is installed; if queries fail, debug syntax. Verify each of the five queries produces sensible output for the PMTEC sample data.
2. **Build the six prompts** in `_meta/prompts/` per §5. Pull prompt bodies verbatim from the SOP (§5 of `_handoff/research_workflow_sop.md`).
3. **Add a `_meta/prompts/README.md`** explaining the model recommendations and when to use which prompt.
4. **Add cross-references in the dashboard** to the prompt library — "Start a new opportunity? Use [[_meta/prompts/source-gathering]]."
5. **Add a Templater-friendly stub** for new opportunity creation (a Markdown file at `_templates/new-opportunity-instructions.md`) that documents how to clone the PMTEC folder structure for a new opportunity. Operator will use this manually until/unless Templater is installed.
6. **Test the full opportunity-to-dashboard loop** — modify one frontmatter field in PMTEC `index.md`, confirm dashboard reflects the change.

### 7.2 Phase 2 stop point

Same as Phase 1. Summary, operator checks, wait for confirmation.

### 7.3 What Phase 2 must NOT do

- Do not write the ingestion script. Phase 3.
- Do not propose alternate dashboard tools. Obsidian + Dataview is decided.
- Do not propose adding plugins beyond Dataview unless operator asks.

---

## 8. PHASE 3 — Source ingestion script

**Goal:** operator can run `python ingest.py <url> --opportunity PMTEC-USINDOPACOM` and get a properly-formatted source file in the right folder, with frontmatter, with an entry added to a source ledger.

**Session target:** 2–4 hours, possibly split across two sessions.

### 8.1 Behavior spec

The script lives at `_scripts/ingest.py`. Invocation:

```bash
python ingest.py <URL> --opportunity <OPPORTUNITY_ID> [--type article|pdf|youtube|auto] [--title "Optional override"]
```

Behavior, step by step:

1. **Validate inputs.** Confirm the opportunity folder exists. Confirm the URL is well-formed.
2. **Route by URL type** (`lib/routing.py`):
   - `youtube.com` or `youtu.be` → YouTube fetcher (`lib/fetchers/youtube.py`)
   - URL ending in `.pdf` or content-type `application/pdf` → PDF fetcher (`lib/fetchers/pdf.py`)
   - Anything else → web fetcher (`lib/fetchers/web.py`)
   - `--type` flag overrides auto-detection.
3. **Fetch and clean** (per fetcher):
   - **Web:** use `requests` + `readability-lxml` or `trafilatura` to extract main article text. Save as cleaned markdown. Preserve link references where reasonable.
   - **PDF:** use `pypdf` (NOT pypdf2, which is deprecated). Extract text by page. If PDF has no extractable text (image-based), warn the operator and save a stub with a note that OCR is needed.
   - **YouTube:** call Supadata API with `SUPADATA_API_KEY` from `.env`. Save transcript as markdown with speaker/timestamp annotations where Supadata provides them.
4. **Extract metadata:**
   - Title — from `<title>` for web, document metadata for PDF, video title from Supadata for YouTube.
   - Publisher — from URL domain.
   - Publication date — from page metadata (`<meta property="article:published_time">`, OpenGraph, Dublin Core), PDF metadata, or YouTube upload date. If unavailable, leave blank and warn.
   - Source tier — heuristic by domain (`.mil`, `.gov` → tier 1; `sec.gov` company filings → tier 2; known aggregators → tier 3; etc.). Maintain the domain-to-tier map in `lib/routing.py`. When unknown, default to tier 4 and warn.
5. **Build the filename** per §3.2: `[YYYY-MM-DD]_[domain]_[slug].md` where date is today's date, domain is sanitized (dots → hyphens, drop www.), slug is title-derived (lowercased, alphanumeric + hyphens, max 60 chars).
6. **Write the file** to `opportunities/<OPPORTUNITY_ID>/01_sources/<filename>`. Frontmatter per §3.3 source schema, followed by:
   - `## Summary` (blank — operator or future script fills in)
   - `## Extracted content` (the cleaned text)
   - `## Notes` (blank)
7. **Update the source ledger** at `opportunities/<OPPORTUNITY_ID>/00_research-file.md`. Append the source citation tag `[s.YYYY-MM-DD-slug]` and source filename to the §8 "Source ledger" section. If §8 doesn't exist, create it.
8. **Print confirmation** with filename, source tier, and a warning list (missing date, image-only PDF, low-tier source, etc.).

### 8.2 Module layout

```
_scripts/
├── ingest.py                    # CLI entry
├── lib/
│   ├── __init__.py
│   ├── frontmatter.py           # YAML frontmatter read/write helpers
│   ├── routing.py               # URL → fetcher dispatch + domain→tier map
│   ├── ledger.py                # source ledger update
│   └── fetchers/
│       ├── __init__.py
│       ├── base.py              # abstract fetcher class
│       ├── web.py
│       ├── pdf.py
│       └── youtube.py
├── requirements.txt
├── .env.example
└── README.md
```

### 8.3 `requirements.txt`

```
requests>=2.31
trafilatura>=1.12
pypdf>=4.0
python-dotenv>=1.0
python-frontmatter>=1.1
python-slugify>=8.0
```

(Do NOT add `whisper`, `assemblyai`, or video-transcription deps. Out of scope. Phase 3.5 territory.)

### 8.4 `.env.example`

```
# Required for source ingestion
ANTHROPIC_API_KEY=
GEMINI_API_KEY=
SUPADATA_API_KEY=

# Optional — provision now, use when needed
OPENAI_API_KEY=

# Future phases — slot reserved, not yet used
HIGHERGOV_API_KEY=
SAM_GOV_API_KEY=
```

Also create `.gitignore` with `.env` (even though no git in use yet — defensive).

### 8.5 Error handling principles

- **Fail loudly but safely.** Never write a malformed file. If anything is uncertain, write to a `_quarantine/` subfolder inside `01_sources/` and warn the operator.
- **Fail gracefully on missing keys.** If `SUPADATA_API_KEY` is missing and the URL is YouTube, fail with a clear message — don't crash with an opaque API error.
- **Never silently swallow errors.** Print warnings even on success.
- **Idempotency:** if the same URL is ingested twice on the same day, prompt the operator (replace? skip? new file?).

### 8.6 Testing

Build with these test URLs:

- **Web (Tier 1):** https://www.pacom.mil/About-USINDOPACOM/PMTEC/Article/4467480/usindopacom-seeks-industry-partners-to-address-modern-military-challenges/
- **Web (Tier 4):** https://www.executivegov.com/articles/usindopacom-industry-support-training-tech
- **PDF (Tier 1):** any FY26 PB book from comptroller.war.gov
- **YouTube:** any DVIDS or .mil YouTube clip (test only if Supadata key is provisioned; otherwise stub-test the routing).

Write a `_scripts/README.md` documenting these test cases.

### 8.7 Phase 3 stop point

Same pattern. Summary, demonstrate working ingestion against the test URLs, wait for operator confirmation before any further work.

### 8.8 What Phase 3 must NOT do

- **No agentic loops.** This is a script, not an agent. It takes input, produces output, exits.
- **No LLM calls.** The script does not summarize content or extract quotes. Those are operator-driven prompt-library tasks. (A future Phase 4 could add an `--summarize` flag.)
- **No video transcription beyond YouTube/Supadata.** Non-YouTube video is Phase 3.5, separate handoff.
- **No web crawling.** Single-URL ingestion only. Operator drives.
- **No MCP server wrapping.** Phase 5 territory.

---

## 9. Phases 4 and 5 — future, not in this build

**Phase 3.5 — Non-YouTube video transcription.** Separate utility script using `yt-dlp` + `ffmpeg` + local Whisper. Triggered when operator identifies a video-only source with no text companion. Defer until felt as friction.

**Phase 4 — Verification helpers.**
- Claim verifier — scan a brief draft for FACT/Assessment/Speculation labels, cross-reference inline citations against `01_sources/`, flag single-sourced or unsourced claims.
- POC staleness reminder — surface POCs older than 90 days via dashboard query or CLI.
- Cross-opportunity search beyond simple grep.

**Phase 5 — MCP / agentic layer.**
- Wrap ingest, quote extraction, POC extraction as MCP tools callable from Claude/Gemini.
- MemPalace integration as one of several MCP servers, if it has earned its place.
- Anything genuinely improved by being agentic rather than scripted.

Do not build into Phases 4 or 5 during this handoff. They are listed only to make scope explicit.

---

## 10. CLAUDE.md (project context file)

Write the following to `<vault-root>/CLAUDE.md`:

```markdown
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

[Update this manually as phases complete. Start as: "Phase 1 in progress."]

## How to behave in this project

- When the operator asks for "another opportunity like PMTEC," clone the folder
  structure but never copy PMTEC-specific content into the new opportunity.
- When asked to research, you do not have web access from Claude Code; ask the
  operator to fetch URLs and paste content, or invoke `_scripts/ingest.py`.
- Default to printing a plan before executing destructive operations.
- Stop at phase boundaries. Do not chain phases without operator confirmation.
- Out of scope items in HANDOFF.md §11 are binding. Do not build into them.
```

---

## 11. What's explicitly out of scope (binding)

Do not build, propose, or "while I'm here, also" any of the following:

1. **Any web publishing.** No GitHub Pages, no Quarto site, no static-site generator. The vault is local-only.
2. **Any cloud sync.** No iCloud, Dropbox, OneDrive integration. Operator handles backup.
3. **Any database beyond markdown + frontmatter.** No SQLite, no Postgres, no embedding store. Dataview reads the markdown directly.
4. **Any agentic loops or autonomous workflows.** Scripts are scripts. Operator drives.
5. **Any non-Obsidian dashboards.** No Streamlit, no Grafana, no web UI. The dashboard is an Obsidian note.
6. **Any new prompt invention.** Use only the prompts from the existing SOP. Variations are operator decisions.
7. **Any video transcription beyond YouTube via Supadata.** Phase 3.5, separate handoff.
8. **Any MCP server.** Phase 5 if ever.
9. **MemPalace, vector DBs, or "AI memory" tools.** Phase 5 if ever.
10. **Web crawling, scraping pipelines, or bulk download.** Single-URL ingestion only.
11. **Authentication-gated source ingestion.** If a URL requires login, the script reports it and stops. Operator handles auth manually.
12. **Modifying existing .docx templates from `_handoff/`.** They're validated; treat as read-only inputs.
13. **Changes to the SOP.** The SOP is authoritative. Propose changes, do not unilaterally make them.
14. **Anything that requires the operator to learn a new tool** beyond: Obsidian, the Dataview plugin, and Python script invocation. No Templater, Tasks plugin, etc. unless explicitly requested.

---

## 12. Stop points

At the end of each phase, **stop** and present:

1. **What was created** — file count by folder, key files highlighted.
2. **What was verified** — what tests/checks were run.
3. **What the operator should check** — concrete verification steps the operator should perform before continuing.
4. **What's next** — the next phase summary.
5. **Outstanding questions** — anything you encountered that needed an operator decision but you deferred (with your best-guess default and rationale).

Then **wait for explicit operator confirmation** before starting the next phase.

If you encounter a decision mid-phase that wasn't anticipated in this document, **stop and ask**, with your best-guess default and reasoning. Do not make material decisions silently.

---

## 13. Final notes

- The operator is AI-fluent but new to Obsidian. Default to verbose operator-facing summaries.
- The operator's stated friction is source gathering — Phase 3 is the highest-value phase. Phases 1 and 2 are necessary scaffolding to make Phase 3 land in the right place.
- The operator is the analyst, verifier, and decision-maker. This tooling makes the manual parts faster; it does not replace judgment.
- If something in this document is ambiguous or contradicts itself, flag it and propose a resolution rather than guessing.

End of HANDOFF.md.

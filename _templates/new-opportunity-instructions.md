# How to start a new opportunity

Follow these steps manually each time you open a new opportunity. This is a manual process until Templater is installed (which is out of scope for this build).

---

## Step 1 — Create the folder

```bash
mkdir -p ~/research/opportunities/NEWOPPORTUNITY-CUSTOMER/01_sources
mkdir -p ~/research/opportunities/NEWOPPORTUNITY-CUSTOMER/04_artifacts
```

Replace `NEWOPPORTUNITY-CUSTOMER` with the real ID in the format `[OPPORTUNITY]-[CUSTOMER]` in caps, hyphenated. Example: `FORGE-STRATCOM`.

## Step 2 — Copy the template files

```bash
cd ~/research
cp _templates/opportunity-index.md    opportunities/NEWOPPORTUNITY-CUSTOMER/index.md
cp _templates/research-file.md        opportunities/NEWOPPORTUNITY-CUSTOMER/00_research-file.md
cp _templates/quotes.md               opportunities/NEWOPPORTUNITY-CUSTOMER/02_quotes.md
cp _templates/pocs.md                 opportunities/NEWOPPORTUNITY-CUSTOMER/03_pocs.md
cp _templates/decision-log.md         opportunities/NEWOPPORTUNITY-CUSTOMER/05_decision-log.md
```

Do **not** copy `_templates/source.md` here — individual source files are created by `_scripts/ingest.py` (Phase 3).

## Step 3 — Edit `index.md` frontmatter

Open `opportunities/NEWOPPORTUNITY-CUSTOMER/index.md` and fill in every field:

```yaml
id: NEWOPPORTUNITY-CUSTOMER
title: [full descriptive title]
customer: [org, e.g., USSOCOM J5]
gate: identify
status: triaged
recommendation:
  - tbd
capability_tags:
  - [TAG1]
  - [TAG2]
opened: [today's date YYYY-MM-DD]
last_updated: [today's date YYYY-MM-DD]
next_action: [first concrete action]
next_action_due: [YYYY-MM-DD]
focus_month: [YYYY-MM]
```

## Step 4 — Edit `03_pocs.md` frontmatter

```yaml
opportunity: NEWOPPORTUNITY-CUSTOMER
last_reviewed: [today's date]
review_due: [90 days from today]
```

## Step 5 — Edit `02_quotes.md` frontmatter

```yaml
opportunity: NEWOPPORTUNITY-CUSTOMER
last_updated: [today's date]
```

## Step 6 — Add a first decision-log entry

In `05_decision-log.md`, add:

```markdown
### [YYYY-MM-DD] — Opportunity opened

**By:** operator
**Rationale:** [1–2 sentences on why this opportunity was selected for the month]
**What changed:** Opportunity folder initialized; Gate 1 research begun.
```

## Step 7 — Verify the dashboard

Open `_meta/dashboard.md` in Obsidian. Confirm the new opportunity appears in the Active Opportunities table and in "This month's focus" (if `focus_month` matches the current month).

---

## What NOT to copy from PMTEC

The `opportunities/PMTEC-USINDOPACOM/` folder contains PMTEC-specific content (POCs, quotes, research, artifacts). Do not copy any of it into a new opportunity folder. Use only the blank templates from `_templates/`.

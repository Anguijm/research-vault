# Research workflow & verification SOP

**Owner:** [you]
**Last updated:** [YYYY-MM-DD]
**Cadence target:** 12 capture briefs per year (≈1 per month)
**Team:** primary analyst (you) + Claude + Gemini + 1–2 on-call SMEs for surge
**Data classification:** OSI / public-domain only

---

## 1. What this SOP is for

This is the operating manual for producing defense capture briefs and executive briefs at a sustainable monthly cadence using AI assistance. It defines the repository structure, the verification standard, the monthly cadence, and the AI prompting patterns. Read it once end-to-end before starting your first capture. Refer back to it when you hit friction.

This SOP assumes:

- You are producing two artifacts per opportunity — a **capture brief** for the BD team and an **executive brief** derived from it. The original SOP target was 10-12 pages for the capture brief and 1-2 pages for the executive brief; that target was retired 2026-05-28 against the BDR-FLEET-READINESS v1.0-candidate measurement, which produces a 23-page capture and a 3-page exec under the `build_brief.py` default layout (1" margins, 11pt body, default paragraph spacing). The v1.0-quality content set requires the larger footprint; cutting to the original target was found to drop content that an external red-team specifically requested. Treat page count as a quality-of-rendering check, not a quality-of-content gate. If a future opportunity wants tighter page counts, change the docx layout (margins / font / spacing in the build script) before cutting content.
- All research is **OSI** (open-source intelligence). No CUI, no classified, no proprietary client data.
- You operate a **simplified 3-gate process**: Identify → Pursue → Bid.
- The repository lives **locally** on your machine, with whatever backup discipline you already have for important work.
- Storage is boring (local markdown + Word). Retrieval may be experimental (MemPalace, Obsidian, project memory). **Never conflate the two.**

---

## 2. Repository structure

One folder per opportunity. Same shape every time. Markdown for working files, Word for final artifacts.

```
~/research/
├── _meta/
│   ├── sop.md                          ← this file
│   ├── verification-rules.md           ← the six rules, printable
│   ├── ai-prompts.md                   ← reusable prompt library
│   └── monthly-log.md                  ← what you worked on each week
├── _templates/
│   ├── capture_brief_template.docx
│   ├── executive_brief_template.docx
│   ├── research_file_template.md
│   ├── quotes_template.md
│   ├── pocs_template.md
│   └── decision_log_template.md
└── opportunities/
    └── PMTEC-USINDOPACOM/              ← one folder per opportunity
        ├── 00_research-file.md         ← working analysis
        ├── 01_sources/                 ← raw source captures
        │   ├── 2026-04-22_pacom-mil-4467480.md
        │   ├── 2026-03-15_executivegov-summary.md
        │   ├── 2025-09-18_govconwire-caci-pacaf.md
        │   └── ...
        ├── 02_quotes.md                ← extracted verbatim quotes with attribution
        ├── 03_pocs.md                  ← named people, roles, contacts
        ├── 04_artifacts/
        │   ├── capture-brief-v0.1-draft.docx
        │   ├── capture-brief-v1.0-internal.docx
        │   ├── capture-brief-v1.0-shareable.docx
        │   └── executive-brief-v1.0.docx
        └── 05_decision-log.md          ← what was decided when, by whom
```

**Naming conventions:**

- Folder names: `[OPPORTUNITY]-[CUSTOMER]` in caps, hyphenated (e.g., `PMTEC-USINDOPACOM`).
- Source files in `01_sources/`: `[YYYY-MM-DD]_[domain]_[short-slug].md` — the date is the date you captured it, not the date the source was published.
- Artifact versioning: `v0.x` for drafts, `v1.0` for first shipped, `v1.1` for minor edits, `v2.0` for a re-research at next gate.
- Sensitivity tags in artifact filenames: `-internal`, `-shareable`, `-public`.

**Why local markdown:**

Markdown survives every AI tool transition, every cloud-app shutdown, every laptop migration. You can grep it, version-control it, paste it into Claude or Gemini, and read it on a plane. The boring choice is the durable choice.

**Why no GitHub/website yet:**

You don't have a discoverability problem yet — you have an output problem. Build infrastructure when the friction tells you to, not before. After ~6 capture briefs, you'll know what tooling you actually need. Likely candidates by then: Zotero for citation management, Obsidian for the markdown layer with backlinks, MemPalace as an AI memory layer if it earns its place.

---

## 3. The six verification rules

Print these. Tape them above your desk. Do not skip any of them.

### Rule 1 — Primary source over secondary

If Breaking Defense quotes a general, find the speech transcript on the .mil site or DVIDS and cite **that**. If a press release cites a contract value, find the SAM.gov / USAspending.gov / HigherGov record and cite **that**. Trade press is fine for color and analysis. It is not fine as the only citation for a factual claim.

**Primary sources hierarchy (best to worst):**

1. .mil sites, DVIDS, SAM.gov, USAspending.gov, comptroller PB books, GAO reports, congressional testimony, CRS reports
2. Company SEC filings (10-K, 10-Q, 8-K), investor day decks, official press releases
3. HigherGov, OrangeSlices.ai, GovTribe (these aggregate primaries)
4. Trade press: Breaking Defense, Defense News, DefenseScoop, Inside Defense, ExecutiveBiz, GovConWire
5. Think tank analysis: CSIS, RAND, CNAS, Hudson, AEI
6. Blogs, social media, single-author commentary

### Rule 2 — Two-source rule for non-trivial claims

Anything about money, timelines, named people, or organizational reporting needs two independent sources. If you can only find it once, mark it **\"single-sourced\"** in the brief.

Common single-source traps: contract ceiling values cited only by the awarded contractor; org charts derived from LinkedIn alone; dates pulled from secondary press without checking the primary release.

### Rule 3 — Date-stamp everything

Every fact in the research file gets a `[verified YYYY-MM-DD]` tag. POCs, contract ceilings, budget figures, org reporting lines — all of it rots fast. A fact verified six months ago is a hypothesis today. Re-verify all POCs and contract data **every 90 days** for active opportunities.

### Rule 4 — Label fact / assessment / speculation explicitly

Use the words. Every claim in your research file and your brief carries one of three labels:

- **FACT:** traceable to a primary source (cite inline).
- **ASSESSMENT:** your reasoned judgment based on multiple facts. Prefix with \"Assessment:\".
- **SPECULATION:** forward-looking inference not yet supported by evidence. Prefix with \"Speculation:\" and flag for review.

Reviewers should challenge any claim that does not carry one of the three labels. This is the single biggest defense against AI-induced overconfidence.

### Rule 5 — Adversarial review before any artifact ships

Before the capture brief or exec brief leaves your machine, someone else (the on-call analyst, ideally) tries to break it. Specifically: \"find one claim you think is wrong or weakly sourced.\" If they find one, you fix it. If they find more than two, the brief isn't ready.

If no human is available, run the cross-AI red team described in §5.4. It's not a substitute, but it's better than nothing.

### Rule 6 — Click every link

When AI gives you a citation, **open the link**. AIs hallucinate citations, including credible-looking ones. The 30-second click is the difference between professional intel and a blog post. This is non-negotiable.

> Note: an AI made one error in this thread's prior research — incorrectly attributing Alion's acquisition to CACI rather than HII. A 30-second click on the source would have caught it. Bake \"click every link\" into your habit; do not assume AI's confidence equals accuracy.

---

## 4. Monthly cadence (one capture brief per month)

The cadence is paced to be sustainable solo. If a month gets compressed, cut scope before quality.

### Week 1 — Triage (4–8 hours)

- Review the **monthly log** (`_meta/monthly-log.md`) for last month's open threads.
- Run the SAM.gov / DIU / DVIDS / Apex Innovates saved searches. Capture new opportunity signals.
- If you maintain an opportunity sheet list: refresh it. Drop dead ones, add new ones.
- **Pick the focus opportunity for the month.** Pick one. Trying to research two in a month at this team size always fails one of them.
- Open a new opportunity folder. Initialize the six files from the templates.

### Weeks 2–3 — Research (12–20 hours)

This is where AI does the heavy lifting and you do the verification.

- **Day 1–2:** broad gather. Use Gemini for breadth (web reach across DVIDS, trade press, GovConWire, .mil sites). Save raw captures into `01_sources/`. Tag each capture with date and source URL.
- **Day 3:** quote and POC extraction. Use Claude to extract verbatim quotes from sources into `02_quotes.md`. Build `03_pocs.md`. **Click every link.**
- **Day 4–5:** funding, vehicles, incumbents. Look at PB books, USAspending, HigherGov for contract awards. Identify likely incumbents and primes for each play.
- **Day 6:** capability map. If the brief is about your company's fit, build the gap-vs-capability matrix. Honest about the gaps.
- **Day 7–10:** write the working analysis in `00_research-file.md`. Two-source rule applied throughout. Fact / assessment / speculation labels used explicitly. Surge to on-call SME for any technical area you can't credibly assess solo.

### Week 4 — Distill and ship (8–12 hours)

- **Day 1:** copy the capture brief template to `04_artifacts/capture-brief-v0.1-draft.docx`. Populate from the research file. Each section gets its own AI-assisted drafting pass (see §5).
- **Day 2:** cross-AI red team. Hand the v0.1 to the second AI (whichever you didn't use for drafting). Ask it to play the role of a customer reviewer, a competitor, and a skeptical exec, in three separate prompts. Hardener pass on the brief.
- **Day 3:** human adversarial review with the on-call SME. Address findings.
- **Day 4:** derive the executive brief. Write it last; cut ruthlessly to one page.
- **Day 5:** final polish. Save `-internal` and `-shareable` versions of the capture brief (sensitivity sections clearly marked). Update `05_decision-log.md`. Ship.

### End-of-month: log and learn

- Update `_meta/monthly-log.md`: what you produced, what was painful, what improved.
- If a friction point appeared three months in a row, that's your next infrastructure investment.

---

## 5. AI prompting patterns

Use Claude and Gemini for different things. They have different strengths, and using them as a check on each other catches more errors than either alone.

### 5.1 Division of labor

| Task | Best tool | Why |
|---|---|---|
| Broad web scan for new opportunities | Gemini | Generally broader/fresher web reach |
| Summarizing speeches, press releases | Either | Both competent |
| Extracting quotes from a source | Claude | Better at \"verbatim, with attribution\" discipline |
| Building the POC table from .mil pages | Claude | Better at structured extraction |
| First-draft synthesis of a section | Claude | Better at long-form analytical prose |
| Red-teaming a draft | The other one | Cross-model disagreement is the value |
| Distilling capture brief → exec brief | Claude | Stronger at ruthless compression |
| Cross-checking citations | Both, in sequence | Belt and suspenders |

This is a starting point, not gospel. Notice which tool wins on which task in your own work and update the table.

### 5.2 Source-gathering prompt

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

### 5.3 Quote extraction prompt

```
Here is a source: [paste full source text or URL].

Extract every verbatim quote attributable to a named person, with:
  - Speaker name and exact title
  - Date of statement (or publication date if unclear)
  - Venue (speech, interview, press release, etc.)
  - The quote, exact wording, in quotes
  - Source URL

Do not paraphrase. Do not invent attribution. If a quote in the text is
unattributed in the source, note it as \"unattributed in source.\"
```

### 5.4 Cross-AI red team prompt

After producing a v0.1 draft, run this on the OTHER model:

```
You are reviewing this capture brief in three roles, in three separate passes.

Pass 1 — Customer reviewer: You are a J7 staffer at USINDOPACOM. What in this
brief is wrong, oversimplified, or sounds like marketing? What would you push
back on?

Pass 2 — Competitor analyst: You work at a competing prime. Where are the
weakest parts of the recommendation? What facts could be challenged? What
would you exploit if you saw this?

Pass 3 — Skeptical exec: You are a defense pure-play exec with 4 minutes to
read this. Is the recommendation clear? Is the ask actionable? What would
make you say \"come back when you've done more homework\"?

Be specific. Cite the section number for each critique.
```

### 5.5 Distillation prompt (capture → exec brief)

```
Here is a 12-page capture brief. Distill it into a 1-page executive brief
for a defense pure-play exec who reads on a phone.

Constraints:
  - BLUF first: 3–5 sentences. The opportunity, the recommendation, the ask.
  - \"Why it matters\" — 3–5 bullets.
  - Recommendation — 2–3 bullets.
  - Top risks — 2–3 bullets.
  - Asks — 2–3 bullets.
  - No methodology section. No bibliography. No hedging.
  - Prose with bullets, not all bullets. One chart maximum.
  - Cut anything not decision-relevant. If in doubt, cut it.

Maintain the fact / assessment / speculation labels from the source.
```

### 5.6 POC extraction prompt

*Added 2026-05-11, post-handoff. Authoritative addition to the SOP.*

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

### 5.7 Weekly triage scan prompt

*Added 2026-05-11, post-handoff. Authoritative addition to the SOP.*

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

---

## 6. Templates

Three templates ship with this SOP. Copy them into a new opportunity folder; do not edit the originals.

### 6.1 `00_research-file.md` starter

```markdown
# [Opportunity Name] — Research File

**Customer:** [e.g., USINDOPACOM J7]
**Opportunity ID:** [your internal ID]
**Gate:** Identify | Pursue | Bid
**Started:** [YYYY-MM-DD]
**Last updated:** [YYYY-MM-DD]

---

## 1. Working summary (analyst view)

[Living paragraph — what is this opportunity, what's the core question. Update as research deepens.]

## 2. Open questions

- [ ] Question 1
- [ ] Question 2

## 3. Demand signal — what the customer is saying

### 3.1 Stated priorities
[bulleted list with citation tags like [s.2026-04-22-pacom]]

### 3.2 Funding
[PDI line items, contract awards, FY money]

### 3.3 Engagement mechanism
[How to get in — POCs, portals, conferences]

## 4. Customer landscape

[Org structure, named POCs, reporting lines. Cross-ref to 03_pocs.md for details.]

## 5. Competitive landscape

[Likely primes, incumbents, recent awards by play.]

## 6. Our fit

### 6.1 Existing footprint
[Contracts, embeds, capabilities already in this AOR.]

### 6.2 Capability map
[For each stated priority gap, our fit: strong / moderate / weak. Why.]

## 7. Working hypothesis

**Recommendation (draft):** [PURSUE prime / PURSUE sub / PASS]
**Reasoning:** [3–5 sentences]
**Top risks:** [bulleted]

## 8. Source ledger

[Running list of sources consumed. Cross-ref 01_sources/ folder.]
- [s.2026-04-22-pacom] pacom.mil/...
- [s.2026-03-13-executivegov] executivegov.com/...

## 9. Verification flags

[Things you couldn't verify, things single-sourced, things that need re-verification.]
```

### 6.2 `02_quotes.md` starter

```markdown
# [Opportunity] — Verbatim quotes

Every quote: speaker, role, date, venue, source URL, last-verified date.
Pull from here into briefs as needed; do not edit quotes inline.

---

## [Speaker name], [role]

> \"[exact quote]\"

— [Venue], [date]. Source: [URL]. Verified [YYYY-MM-DD].

---

## [Next speaker]

> \"[exact quote]\"

— [Venue], [date]. Source: [URL]. Verified [YYYY-MM-DD].
```

### 6.3 `03_pocs.md` starter

```markdown
# [Opportunity] — POC Directory

Re-verify all entries every 90 days. Defense roles rotate.

| Name | Role | Org | Email/contact | Source | Verified |
|---|---|---|---|---|---|
| [Name] | [Role] | [Org] | [contact if public] | [URL] | [YYYY-MM-DD] |

## Notes

- [Any context on relationships, recent moves, sensitivities]
```

### 6.4 `05_decision-log.md` starter

```markdown
# [Opportunity] — Decision Log

Every decision: date, decision, by whom, rationale, what changed.

---

### [YYYY-MM-DD] — [Decision]

**By:** [name(s)]
**Rationale:** [1–2 sentences]
**What changed:** [what action was authorized, what artifact was shipped, etc.]

---
```

---

## 7. Common failure modes (and how to avoid them)

**Failure mode 1: Infrastructure overbuilds.** Spending six weeks setting up the perfect Notion/Obsidian/MemPalace/Quarto stack and producing zero briefs. **Fix:** ship two briefs in plain markdown + Word first. Then add infrastructure where you felt friction.

**Failure mode 2: AI hallucinated citation.** AI cites a paper, article, or contract that doesn't exist or doesn't say what AI claims. **Fix:** click every link (Rule 6). If a citation is uncheckable, drop it.

**Failure mode 3: Single-sourced confidence.** One press release becomes the foundation for a 12-page brief. **Fix:** Rule 2. Mark single-sourced claims explicitly and downgrade confidence accordingly.

**Failure mode 4: Stale POC table.** You ship a brief naming a Brigadier General who PCS'd six months ago. **Fix:** Rule 3. 90-day re-verification on every active opportunity.

**Failure mode 5: Trying to make one brief serve both audiences.** The exec drowns and the BD team starves. **Fix:** write the long one first, distill to the short one. Two artifacts, one research file.

**Failure mode 6: No human red team.** AI red-teaming catches some things but misses what a real defense BD person would notice. **Fix:** Rule 5. The on-call analyst is your most valuable resource — use them.

**Failure mode 7: Coopetition leak.** Internal recommendations end up in a deck that goes to a teaming partner. **Fix:** sensitivity tags on every section of the capture brief from day one. Generate the shareable version by deletion, not by rewrite.

---

## 8. When to revisit this SOP

After every 3 capture briefs (so quarterly at this cadence), spend 30 minutes asking:

- What did I do that the SOP doesn't describe? (Add it.)
- What does the SOP tell me to do that I'm skipping? (Either fix the SOP or commit to the discipline.)
- What tool friction kept showing up? (Maybe time for that infrastructure investment.)
- Has the cross-AI division of labor (§5.1) changed?

The SOP is a living document. The tape on the wall is the six rules. Everything else is editable.

---

## Appendix — Tool list (boring on purpose)

- **Storage:** local filesystem
- **Final artifacts:** Microsoft Word (.docx) — opens everywhere, prints cleanly, distributes as PDF
- **Working files:** Markdown (.md) — portable forever, AI-readable, greppable
- **AI assistants:** Claude (synthesis, structured extraction, distillation), Gemini (broad web reach, cross-checks)
- **Citation management:** TBD — start with markdown source ledger; consider Zotero after ~5 captures
- **Backup:** whatever you already trust for important work
- **Collaboration:** email or Teams/Slack for distribution; Word track changes for review
- **Scheduling:** your calendar, the monthly cadence in §4

Tools to consider AFTER 6+ briefs, only if friction demands it:

- Zotero (citation management at scale)
- Obsidian (markdown with backlinks and graph view)
- MemPalace (cross-session AI memory layer)
- Quarto (publishable research site, if external distribution becomes a need)
- A scraping pipeline (if you start tracking 50+ live opportunities)

The point is: build infrastructure when the work demands it, not before. Most defense capture functions of your size never need anything more than this list.

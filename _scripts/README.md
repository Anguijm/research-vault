# _scripts/ — Source ingestion

## Usage

```bash
cd ~/research/_scripts
source .venv/bin/activate   # each new terminal session

# Web article (auto-detect)
python3 ingest.py <URL> --opportunity PMTEC-USINDOPACOM

# Force type
python3 ingest.py <URL> --opportunity PMTEC-USINDOPACOM --type pdf
python3 ingest.py <URL> --opportunity PMTEC-USINDOPACOM --type youtube

# Override extracted title
python3 ingest.py <URL> --opportunity PMTEC-USINDOPACOM --title "FY26 PDI Budget Book"
```

## First-time setup

```bash
cd ~/research/_scripts
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env and add keys (SUPADATA_API_KEY required for YouTube)
```

## What it does

1. Validates the URL and confirms the opportunity folder exists.
2. Routes to the right fetcher: web (requests + trafilatura), PDF (pypdf), or YouTube (Supadata API).
3. Extracts title, content, publication date, and publisher.
4. Assigns a source tier based on domain (1 = .mil/gov, 4 = trade press, etc.).
5. Writes a formatted source file to `opportunities/<ID>/01_sources/<filename>.md`.
6. Appends a citation entry to `§8 Source ledger` in `00_research-file.md`.
7. Prints a summary with tier, citation tag, and any warnings.

Files with no extractable content are quarantined to `01_sources/_quarantine/` rather than written to the main sources folder.

If you ingest the same URL twice on the same day, you are prompted: replace / skip / new file with timestamp suffix.

## Source tier map

| Tier | Examples |
|---|---|
| 1 | .mil sites, DVIDS, SAM.gov, USAspending.gov, comptroller.war.gov, GAO, Congress |
| 2 | SEC.gov filings |
| 3 | HigherGov, GovTribe, OrangeSlices.ai |
| 4 | Breaking Defense, Defense News, ExecutiveGov, GovConWire, C4ISRNET |
| 5 | CSIS, RAND, CNAS, Hudson, AEI |
| 6 | Blogs, social media |

Unknown domains default to tier 4 with a warning. Add recurring sources to `DOMAIN_TIER_MAP` in `lib/routing.py`.

## Test cases

| Type | URL | Expected tier | Notes |
|---|---|---|---|
| Web / Tier 1 | https://www.dvidshub.net/news/561976/... | 1 | Confirmed working |
| Web / Tier 1 | https://www.pacom.mil/About-USINDOPACOM/PMTEC/... | 1 | Returns 403 — download manually |
| Web / Tier 4 | https://www.executivegov.com/... | 4 | Returns 403 — download manually |
| PDF / Tier 1 | Any FY26 PB book from comptroller.war.gov | 1 | Requires --type pdf if URL doesn't end in .pdf |
| YouTube | Any DVIDS or .mil YouTube clip | 1 | Requires SUPADATA_API_KEY in .env |

## Known limitations

- .mil sites and some trade press block automated fetching (HTTP 403). Download the page and ingest from a local copy, or paste content manually into a source file using `_templates/source.md`.
- PDF text extraction fails on image-based PDFs (scanned documents). OCR required; file is quarantined with a warning.
- YouTube transcription requires a Supadata API key. Without it, the script exits cleanly with a clear error.
- No LLM calls, no summarization, no agentic behavior. This is a single-URL fetch-and-format tool.

## AI source-finding (Phase 4a)

Automated source discovery via Gemini (with Google Search grounding). Candidates land in `_inbox.md` for operator approval before any ingestion.

```bash
# Find new sources for one opportunity (writes to _inbox.md)
python3 find_sources.py --opportunity PMTEC-USINDOPACOM

# Dry-run: print candidates to stdout, no files written
python3 find_sources.py --opportunity PMTEC-USINDOPACOM --dry-run

# Process inbox: ingest approved [x], log rejected [-], leave pending [ ]
python3 approve_inbox.py PMTEC-USINDOPACOM
```

Configure per-opportunity search terms in `opportunities/<ID>/_search-config.yaml`.

Required `.env` keys: `ANTHROPIC_API_KEY`, `GEMINI_API_KEY`.
If one key is missing, the script continues with the other. If both missing, it exits with an error.

Known behavior: Claude (claude-haiku) lacks real-time web search and typically returns 0 candidates. Gemini uses Google Search grounding and returns real, recent results. Both models are retained so Claude can be swapped for a search-capable model if Anthropic adds that capability.

Cron setup (add manually via `crontab -e`):
```
0 4,16 * * * cd /home/johnanguiano/research && _scripts/.venv/bin/python _scripts/find_sources.py >> _meta/cron-log.md 2>&1
```

## FACT verification (Phase 4d)

`verify_facts.py` reads every `**FACT:**` claim in `<opportunity>/00_research-file.md`,
resolves its `[s.xxx]` citations against the source ledger, loads any ingested source
files, and asks Claude whether the source actually supports the claim.

```bash
# Generate a verification report (writes to opportunities/<ID>/_verification-<date>.md)
python3 verify_facts.py --opportunity PMTEC-USINDOPACOM

# Same, but also rewrite the inline status markers in 00_research-file.md
python3 verify_facts.py --opportunity PMTEC-USINDOPACOM --update-markers

# Use a different model
python3 verify_facts.py --opportunity PMTEC-USINDOPACOM --model claude-opus-4-7
```

Per-FACT verdicts:

| Status | Meaning |
|---|---|
| `SUPPORTS` | At least one ingested source explicitly supports the claim. |
| `PARTIAL` | Ingested source(s) support some elements; others are missing or paraphrased loosely. |
| `DOES_NOT_SUPPORT` | Ingested source contradicts or fails to mention the claim. |
| `UNVERIFIABLE` | No ingested source for any of the claim's citations — gap to be filled by ingesting the cited source. |

The report includes the model's supporting quote and missing-elements analysis for each
PARTIAL/SUPPORTS verdict. Verdicts are advisory; the operator owns the final decision
about whether a claim is brief-ready.

Required `.env` key: `ANTHROPIC_API_KEY`.

## Sync sources into Word briefs (Phase 4d)

`refresh_brief_sources.py` reads frontmatter from every file in `01_sources/`
and appends an auto-generated "Sources" section to each `.docx` in
`04_artifacts/`. Each entry is a real Word hyperlink to the source URL plus
a metadata line (publisher, tier, capture date, local file).

```bash
# Update both capture and executive briefs for an opportunity
python3 refresh_brief_sources.py --opportunity PMTEC-USINDOPACOM

# Dry-run (report only)
python3 refresh_brief_sources.py --opportunity PMTEC-USINDOPACOM --dry-run
```

The section is delimited by sentinel paragraphs, so re-running the script
replaces the prior auto-block rather than duplicating it. Idempotent.

Run after every cron / approval / verification pass to keep the briefs'
Sources section in sync with what's actually in `01_sources/`.

## USAspending.gov contract discovery (Phase 4d)

`find_sources.py` queries USAspending.gov alongside AI and SAM.gov. USAspending is the
authoritative record for contract obligations, periods, and recipients — best used to
verify or surface relevant award data tied to an opportunity.

Configure `usa_spending_searches:` in `_search-config.yaml`:

```yaml
usa_spending_searches:
  # Plain keyword string — searches descriptions
  - "INDOPACOM Alpha"

  # Structured search
  - keywords: ["INDOPACOM"]
    recipient: "Deloitte"
    state: "HI"

  # Specific PIID lookup (tracks obligation growth over time)
  - piid: "47QFCA25F0010"
```

No API key required. Polite throttle at 5 req/sec; daily request count is recorded in
`_meta/usaspending-quota.json` for visibility (no hard limit).

Approved USAspending candidates ingest with `content_type: contract_record` and a rich
frontmatter schema (PIID, recipient UEI, total_obligation, base_and_all_options_value,
periods, awarding/funding agencies, parent IDIQ).

## SAM.gov opportunity discovery (Phase 4c)

`find_sources.py` also queries the SAM.gov public API after AI search. Matching opportunity
notices land in the same `_inbox.md` with `Found by: sam.gov`. The operator approves identically
to AI candidates; approved notices ingest as `content_type: sam_gov_notice` with full structured
metadata (notice ID, deadline, NAICS, set-aside, department, attachment list, etc.).

Configure per-opportunity SAM.gov searches in `_search-config.yaml` under `sam_searches:`.
Each entry is either:

```yaml
sam_searches:
  # Format A — paste a SAM.gov browser search URL
  - url: "https://sam.gov/search/?q=PMTEC&is_active=true"

  # Format B — structured API parameters
  - params:
      q: "USINDOPACOM J7 training"
      ncode: ["541330", "541512"]
      typeOfSetAside: null
      postedFrom: null         # null = use date_window_days
```

Required `.env` key: `SAM_GOV_API_KEY` (register at sam.gov → account → API key).

Quota tracking: `_meta/sam-quota.json` records daily request count (resets at UTC midnight).
Script throttles to 2 req/sec and pauses new queries at ≥900 requests/day (10% safety margin
under the 1000/day free-tier limit).

Notice attachments are NOT auto-downloaded. The inbox entry lists them; approved notices store
the attachment list in frontmatter with `ingested: false`. To ingest an attachment, the operator
runs `ingest.py <attachment-url> --opportunity <ID>` manually.

Closed/cancelled notices (where `active: No` or `type: cancellation`) are not filtered out —
they appear in the inbox with `[CLOSED]` or `[CANCELLED]` prefix on the title for operator triage.

## Module layout

```
_scripts/
├── ingest.py                    # CLI entry point (Phase 3)
├── find_sources.py              # AI + SAM + USAspending cron entrypoint (Phase 4a/4c/4d)
├── approve_inbox.py             # Operator approval workflow (Phase 4a)
├── verify_facts.py              # LLM-based FACT-vs-source verifier (Phase 4d)
├── refresh_brief_sources.py     # Sync 01_sources/ into Word briefs as hyperlinked appendix (Phase 4d)
├── lib/
│   ├── frontmatter.py           # YAML frontmatter builder
│   ├── routing.py               # URL → fetcher dispatch + domain→tier map
│   ├── ledger.py                # source ledger update
│   ├── searcher.py              # Claude/Gemini search dispatcher (Phase 4a)
│   ├── inbox.py                 # _inbox.md read/write/expire (Phase 4a)
│   ├── dedup.py                 # URL deduplication (Phase 4a)
│   ├── lock.py                  # lock file management (Phase 4a)
│   ├── cron_log.py              # _meta/cron-log.md writer (Phase 4a)
│   ├── ranker.py                # URL validation + OpenAI ranking (Phase 4a)
│   ├── sam_gov.py               # SAM.gov API client + ingestion (Phase 4c)
│   ├── usaspending.py           # USAspending.gov API client + ingestion (Phase 4d)
│   └── fetchers/
│       ├── base.py              # abstract base class
│       ├── web.py               # requests + trafilatura
│       ├── pdf.py               # pypdf
│       └── youtube.py           # Supadata API
├── requirements.txt
├── .env.example                 # copy to .env, add keys
└── README.md                    # this file
```

---
schema_version: 1
purpose: Citation index for the CACI capability book. Every claim in any
  capability-book file MUST reference an entry here.
---

# Source ledger

Each ingested source gets one entry below with a stable citation slug.
Files in the capability book reference these slugs inline (e.g.,
`[caci-c3i-2026-05-31]`).

## Citation format

```
### <citation-slug>

- URL: <url>
- Fetched: <YYYY-MM-DD>
- Source-type: <web-page | sec-filing | earnings-call | press-release | usaspending-award>
- Title: <as published>
- Sections used: <comma-separated section names or quotes>
- Notes: <any caveats — e.g., paywall, broken-link risk, deprecation>
```

## Sources

### caci-home-2026-05-31

- URL: https://www.caci.com/
- Fetched: 2026-05-31
- Source-type: web-page
- Title: CACI International Inc — homepage
- Sections used: top navigation "What we do", seven capability area links
- Notes: Source for the top-level capability taxonomy. CACI organizes capabilities under "What we do" with seven primary areas at the top-nav level: C3I, Cyber, Digital Solutions, Enterprise IT, Mission and Engineering Support, Space, Spectrum Superiority.

### caci-c3i-2026-05-31

- URL: https://www.caci.com/c3i
- Fetched: 2026-05-31
- Source-type: web-page
- Title: C3I — CACI capability page
- Sections used: summary paragraph, sub-capability list, named customers, named products
- Notes: Sub-capabilities include AI as a cross-cutting theme (pattern across all 7 capability pages).

### caci-cyber-2026-05-31

- URL: https://www.caci.com/cyber
- Fetched: 2026-05-31
- Source-type: web-page
- Title: Cyber — CACI capability page
- Sections used: summary paragraph, sub-capability list, named customers, named products
- Notes: References "Department of War" rather than "Department of Defense" — DoW is the renamed parent agency (rename effective approximately 2025-09 per general knowledge; verify against vault before relying on date specifics).

### caci-digital-solutions-2026-05-31

- URL: https://www.caci.com/digital-solutions
- Fetched: 2026-05-31
- Source-type: web-page
- Title: Digital Solutions — CACI capability page
- Sections used: summary paragraph, sub-capability list, named customers, named products

### caci-enterprise-it-2026-05-31

- URL: https://www.caci.com/enterprise-it
- Fetched: 2026-05-31
- Source-type: web-page
- Title: Enterprise IT — CACI capability page
- Sections used: summary paragraph, sub-capability list, named customers
- Notes: No named CACI products or platforms on this page (unlike Space, Cyber, C3I which all named specific products).

### caci-mission-engineering-2026-05-31

- URL: https://www.caci.com/mission-and-engineering-support
- Fetched: 2026-05-31
- Source-type: web-page
- Title: Mission and Engineering Support — CACI capability page
- Sections used: summary paragraph, sub-capability list, named customers, named products
- Notes: Names "U.S. Navy Naval Surface Warfare Center (NSWC)" as a customer — directly relevant to the operator's NSWC-Corona secondary-customer relationship.

### caci-space-2026-05-31

- URL: https://www.caci.com/space
- Fetched: 2026-05-31
- Source-type: web-page
- Title: Space — CACI capability page
- Sections used: summary paragraph, sub-capability list, named customers, named products

### caci-spectrum-superiority-2026-05-31

- URL: https://www.caci.com/spectrum-superiority
- Fetched: 2026-05-31
- Source-type: web-page
- Title: Spectrum Superiority — CACI capability page
- Sections used: summary paragraph, sub-capability list, named customers, named products
- Notes: References "Azure Summit acquisition" as the origin of certain SIGINT/EW/ISR technology — M&A-derived capability worth verifying in the Session 4 press-release pass.

### caci-10k-fy25-2026-05-31

- URL: https://www.sec.gov/Archives/edgar/data/16058/000162828025038739/caci-20250630.htm
- Fetched: 2026-05-31
- Source-type: sec-filing
- Title: CACI International Inc — Form 10-K for fiscal year ended June 30, 2025
- Sections used: Item 1. Business (Overview, Expertise/Technology framing, Our Markets — Domestic Operations + International Operations, Competition, Strengths and Strategy, Recent Acquisitions, Human Capital, Patents/Trademarks); Item 7. Management's Discussion and Analysis (Overview, Budgetary Environment, Market Environment, Results of Operations, Customer-type revenue breakdown, Contract Backlog, Revenues by Contract Type, Liquidity)
- Notes: Filed 2025-08-07. Local extracted plaintext cached at `/tmp/caci-10k-fy25.txt` and section extracts at `/tmp/caci-10k-business.txt` and `/tmp/caci-10k-mda.txt` during this session (not persisted — re-extract from SEC URL if needed later). The 10-K Business section reaffirms the 7 capability areas from caci.com but uses a different top-level frame ("Expertise" + "Technology" as two foundational categories that cut across the 7 market areas). The MD&A section provides FY25 financial detail, customer-type revenue breakdown, and named market trends (AI, cyber, space, EMS, near-peer competitors).

### caci-investor-quarterly-results-page-2026-05-31

- URL: https://investor.caci.com/financials/quarterly-results/default.aspx
- Fetched: 2026-05-31
- Source-type: web-page
- Title: CACI Investor Relations — Quarterly Results
- Sections used: page structure only; quarterly data not rendered (JavaScript-loaded)
- Notes: Page navigation exists but per-quarter content not visible via WebFetch. Session 3 quarterly granularity beyond the FY25 10-K MD&A would require either pulling 10-Q filings from SEC EDGAR or accessing earnings call transcripts via paid third-party services (Seeking Alpha, Motley Fool). Deferred — the 10-K MD&A's named growth themes are sufficient for Session 3's stated purpose.

### caci-azure-summit-acquisition-2026-05-31

- URL: https://www.businesswire.com/news/home/20241030714385/en/CACI-Completes-Acquisition-of-Azure-Summit-Technology
- Fetched: 2026-05-31 (via web search; original publication date 2024-10-30)
- Source-type: press-release
- Title: CACI Completes Acquisition of Azure Summit Technology
- Sections used: Announcement summary — acquired entity, deal size, capability added, employee headcount, locations, transaction structure
- Notes: $1.275B all-cash; 300+ employees; locations Fairfax VA and Melbourne FL; capability area: RF technology, ISR/EW/SIGINT/EMS. Confirms the Spectrum Superiority (§7) capability page's reference to "Azure Summit acquisition." Closing date 2024-10-30 places it in CACI FY25 Q1.

### caci-applied-insight-acquisition-2026-05-31

- URL: https://investor.caci.com/news/news-details/2024/CACI-Acquires-Applied-Insight/default.aspx
- Fetched: 2026-05-31 (via web search; original publication date 2024-10-01)
- Source-type: press-release
- Title: CACI Acquires Applied Insight
- Sections used: Announcement summary — acquired entity, transaction structure, capability added, customer footprint
- Notes: All-cash; Northern Virginia-based; previously owned by Acacia Group; capability area: cloud migration / adoption / transformation; DoD and Intelligence Community customer base. Closing in FY25 Q1 / Q2.

### caci-bitweave-acquisition-2026-05-31

- URL: https://www.prnewswire.co.uk/news-releases/caci-acquires-bitweave-to-upweight-national-security-intelligence-services-301815879.html
- Fetched: 2026-05-31 (via web search; original publication date approximately 2023-05)
- Source-type: press-release
- Title: CACI Acquires Bitweave to Upweight National Security Intelligence Services
- Sections used: Announcement summary — acquired entity, capability added, organizational placement
- Notes: UK acquisition; acquired by CACI Limited (UK subsidiary); capability area: software engineering, data analysis, cyber services to national security sector. This is the FY23 UK acquisition referenced in the FY25 10-K Business section.

### caci-cyber-duck-acquisition-2026-05-31

- URL: (via web search aggregation; CACI investor relations page not directly fetched)
- Fetched: 2026-05-31
- Source-type: press-release (via web-search summary)
- Title: CACI (UK) Acquires Cyber-Duck — digital transformation / UX
- Sections used: Announcement summary
- Notes: November 2023 timing places this in FY24. UK-based digital transformation agency specializing in UX and open-source technologies. Acquired by CACI Limited (UK subsidiary). Future Session 4 refresh should fetch the canonical press release URL.

### caci-usaspending-top25-2026-05-31

- URL: USAspending API endpoint `https://api.usaspending.gov/api/v2/search/spending_by_award/` queried via `_scripts/lib/usaspending.py`
- Fetched: 2026-05-31
- Source-type: usaspending-award (API query, multiple results)
- Title: CACI top-25 awards by amount, FY2019-2026 window
- Sections used: PIID (Award ID), Recipient Name, Description, Period (Start/End Date), Place of Performance State, Parent IDV (extracted from `generated_internal_id`-derived URL)
- Notes: Query filters: `recipient_search_text=CACI` (substring match), `time_period=[2019-06-02 → 2026-05-31]`, `award_type_codes=[A,B,C,D]` (contracts), `sort=Award Amount desc`, limit=50. After substring filter for "CACI"-prefix recipients (to avoid Acacia-family false positives), 48 results remained; top 25 captured. **Caveat**: Award Amount field returned null/empty for all 25 records — USAspending's spending_by_award endpoint does not populate the amount column for the queried fields list. Awarding Agency / Funding Agency fields also empty. PIID, recipient, description, place of performance, dates, and parent IDV (from URL path) are all reliable. Resolving dollar amounts requires per-award detail calls against `awards/{generated_id}/` endpoint — deferred unless material.

### caci-contracts-page-2026-05-31

- URL: https://www.caci.com/contracts
- Fetched: 2026-05-31
- Source-type: web-page
- Title: CACI Contract Vehicles — Federal Contracts page
- Sections used: complete IDIQ list (eight vehicles), complete GSA vehicle list (six vehicles); contract numbers, holder entity (CACI subsidiary), and period-of-performance dates for each
- Notes: Identifies CACI's eight IDIQs and six GSA vehicles by contract number. Includes **DTIC IAC MAC (FA807518D0006)** — the operator team's contract vehicle — held by CACI, Inc. - Federal, with PoP 2018-09-30 to 2027-09-29. This is the canonical source for CACI's contract-vehicle inventory.

### caci-arka-acquisition-2026-05-31

- URL: https://www.washingtontechnology.com/companies/2025/12/caci-acquire-space-tech-outfit-26b/410336/ (agreement announcement) + verification via web search 2026-05-31 of close status
- Fetched: 2026-05-31 (via web search; agreement announcement 2025-12-22; close completed 2026-03-09)
- Source-type: press-release / news
- Title: CACI Enters into Definitive Agreement to Acquire ARKA Group L.P. (Dec 2025); CACI Completes Acquisition of ARKA Group (Mar 2026)
- Sections used: Announcement and close-confirmation summaries — deal size, capability added, seller, transaction structure, close date
- Notes: $2.6B all-cash from Blackstone Tactical Opportunities; announced 2025-12-22; **closed 2026-03-09**. Capability area: electro-optical/infrared (EO/IR), hyperspectral imaging, Agentic AI-based software for geospatial intelligence. Closed AFTER the FY25 10-K filing (2025-08-07), so not counted in the "seven acquisitions in last three years" 10-K figure — but ARKA is in CACI's portfolio AS OF 2026-03-09, so the Space (§6) area's present-day reach is larger than the FY25 10-K documents.

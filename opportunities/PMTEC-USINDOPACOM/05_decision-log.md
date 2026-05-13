# PMTEC-USINDOPACOM — Decision Log

Every decision: date, decision, by whom, rationale, what changed.

---

### 2026-05-10 — Opportunity opened, initial research complete, Gate 1 brief drafted

**By:** operator
**Rationale:** PMTEC named eight public technology gaps at the 13 March 2026 Quarterly Commercial Industry Update; CACI existing Pacific footprint and post-ARKA capability stack suggest a viable hybrid prime/sub posture for at least three of the eight plays.
**What changed:** Opportunity folder initialized; index.md, research file, quotes, POC table, and capture brief v0.1 draft created. Gate 1 complete; Gate 2 (Pursue) decision pending exec review.

---

### 2026-05-11 — End-to-end FACT verification review

**By:** operator + Claude Code assist
**Rationale:** Audit every FACT claim in `00_research-file.md` against ingested primary sources before any external use. Tagged each claim `[✓ INGESTED]`, `[⚑ PARTIAL]`, or `[⚠ PENDING-INGEST]` so future readers can see at a glance which claims are vault-grounded.
**What changed:**
- Added new ingested primary source: `01_sources/2026-05-11_usaspending-gov_indopacom-alpha-deloitte.md` — USAspending.gov record for Deloitte INDOPACOM Alpha (PIID `47QFCA25F0010`, OASIS parent IDIQ `GS00Q14OADU113`).
- Split the original single-sourced Deloitte INDOPACOM Alpha FACT into a verified FACT (awardee, vehicle, customer, place, start date, $58.9M obligated) and a PARTIAL Assessment ($467M ceiling and 28 Feb 2030 end date remain single-sourced to HigherGov; USAspending's `base_and_all_options_value` is null).
- Confirmed via ingested sources: PMTEC established 2022; "largest coalition range system in the world" claim; Goodman as J7 Director; Stridiron as PMTEC PM; Brent Parker as Industry Engagement Lead.
- Flagged for ingest backlog: pacom.mil PMTEC Article 4467480 (carries the eight priority gaps), comptroller FY26 PDI book, CACI IR docs for Trojan/ARKA/Azure Summit/Spectral, GovConWire AFBIM article. None of these are in `01_sources/` yet, so claims resting on them are single-sourced.
- Restructured §8 source ledger into §8.1 (ingested) and §8.2 (cited but not ingested).
- Restructured §9 verification flags into status buckets (verified / partial / pending / re-verify / speculative / ingest priorities).
- Opened follow-ups: SAM.gov retry tomorrow once new-key throttle clears; ingest pacom.mil 4467480 via curl_cffi-enabled fetcher.

**No FACT was added, removed, or rephrased semantically.** Only verification annotations and one previously-single-sourced FACT split into FACT + Assessment per the new evidence.

---

### 2026-05-12 — Second verification pass: cleared blockers + ingested 6 new primary sources

**By:** operator + Claude Code assist
**Rationale:** Drive the remaining 6 UNVERIFIABLE FACTs to a vault-grounded state by ingesting their cited primary sources, then re-verify and tighten claim wording to match what the source actually says.
**What changed:**
- **6 new ingested primary sources** (all tier 1 or BusinessWire / CACI-investor tier-4 mirrors):
  - `2026-05-12_pacom-mil_usindopacom-seeks-industry-partners-to-address-modern-milita.md` — the canonical 8-priorities article (Akamai-bypassed via curl_cffi)
  - `2026-05-12_comptroller-war-gov_fy2026-pacific-deterrence-initiative.md` — FY26 PDI budget book PDF (the authoritative funding source)
  - `2026-05-12_businesswire-com_u-s-army-selects-caci-for-382-million-signals-intelligence-a.md` — Trojan EATS $382M (Jan 2024)
  - `2026-05-12_businesswire-com_caci-mission-critical-technology-will-accelerate-delivery-of.md` — Spectral SEK $143M (May 2025)
  - `2026-05-12_washingtonexec-com_caci-to-modernize-air-force-base-networks-in-pacific-under-1.md` — PACAF AFBIM $180M (Sep 2025)
  - `2026-05-12_nasdaq-com_caci-completes-acquisition-of-arka-group-2-6b-close-2026-03.md` — ARKA $2.6B close (9 Mar 2026)
  - `2026-05-12_s21-q4cdn-com_caci-azure-summit-technology-acquisition-investor-presentati.md` — Azure Summit $1.28B (Sep 2024 investor deck)
  - Plus 2 inbox-approved DVIDS additions earlier in the day.
- **3 inline FACT rewrites** based on what the ingested sources actually contain:
  - FACT #1 (eight gaps) — reframed to match the article's narrative attribution to named program leads; dropped the "eight" count and the specific "13 March 2026" date that don't appear in the ingested article.
  - FACT #2 (FY26 PDI) — corrected from $9.9B → **$10.0B** ($10,004,542 thousand per primary source), with FY25 baseline noted as ~$9.4B.
  - FACT #3 (PMTEC funding distribution) — rewritten to match the source's actual service-by-service breakdown: Army ($851M, range integration + JPMRC), Navy ($588M, includes PMTEC studies + live-fire target support + JFDD + JDECC), Air Force ($752M, includes named PMTEC Operations sub-category), Joint Staff separate $310M. The brief's prior wording ("Live Fire Target Support and Joint Force Development funded across Army, Air Force, Joint exercises") was structurally wrong; corrected.
- **Verifier results:** moved UNVERIFIABLE from 6 → 0. SUPPORTS: 2 → 3 (#5 intake URL, #9 world's largest range system, #13 Trojan EATS). PARTIAL: 6 → 10 (every CACI contract claim now has a primary source backing the numerics, with only minor wording-strictness gaps left).
- **Two verifier bugs fixed along the way:**
  - `_parse_ledger` simplified — any ledger line with `01_sources/...md` path counts as ingested, regardless of which §8 subsection. Fixes the auto-append-outside-§8.1/§8.2 invisibility bug.
  - `_FACT_RE` extended to capture multi-paragraph FACT bodies (so enumerated lists are visible to the verifier).
  - `_strip_citations` added — `[s.xxx]` tokens are removed from the claim before sending to the LLM so they're treated as bookkeeping, not claim content.
- **One fetcher bug fixed:** `web.py` no longer references `requests.HTTPError` which doesn't exist in `curl_cffi.requests`. Status checks moved to direct `r.status_code` inspection.
- **§2 open questions:** marked "Confirm FY26 PDI PMTEC line-item dollar amount" as resolved (the book does not carry a single consolidated line; the answer is "distributed across services").

**Net state:** vault now holds 17 ingested primary sources covering all FACT claims in the research file. Remaining PARTIAL verdicts are mostly real wording-precision findings (e.g., source says "Hawaii" not "Camp H.M. Smith"; source says "Industry Engagement Lead" not "Commercial Industry Engagement Lead") and are the operator's editorial-style call.

---

### 2026-05-14 — Cross-AI red-team via gemini-3.1-pro-preview

**By:** operator + `_scripts/red_team.py`
**Rationale:** SOP §2.1 rule 5 adversarial review before shipping. Drafting used Claude; red-team uses Gemini per prompt note.
**What changed:** Report written to `_red-team-2026-05-14-gemini-3.1-pro-preview.md`. Reviewed `capture-brief-v0.1-draft.docx` (14 substantive findings). Operator decides whether to address findings before next gate.

---

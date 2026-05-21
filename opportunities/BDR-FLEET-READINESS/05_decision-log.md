# BDR-FLEET-READINESS — Decision Log

Every decision: date, decision, by whom, rationale, what changed.

---

### 2026-05-21 — Research track scaffolded (no research started)

**By:** operator (instruction via `/remote-control`) + Claude Code (Opus 4.7) executing scaffold
**Rationale:** Open a new research track to examine whether NSWC Carderock Division's BDR / ship survivability modeling can be integrated into multidomain service training and what that modeling implies about current fleet training assumptions and PAE-IO repair-capacity planning. Scaffold only — no source ingestion or research performed.
**What changed:** Created folder `opportunities/BDR-FLEET-READINESS/` with standard structure (index.md, 00_research-file.md, 01_sources/, 02_quotes.md, 03_pocs.md, 04_artifacts/, 05_decision-log.md). Seeded 00_research-file.md with neutral working summary, falsifiable hypothesis labeled `Assessment:` in §7, open-questions list including explicit `[DISCONFIRMING]` items in §2, OSI-only research plan in §10, and a load-bearing classification-gradient flag in §9.1. `auto_find: false` set in index.md so the vault's automated source-finder will NOT run against this folder until operator confirms scaffold + makes three pending decisions (folder ID, customer field, PMTEC cross-link).

**Pending operator decisions before research begins:**
1. Confirm folder ID `BDR-FLEET-READINESS` (note: deviates from standard `[OPPORTUNITY]-[CUSTOMER]` pattern since no customer is specified yet).
2. Confirm customer field — candidates flagged in `index.md`: NSWC Carderock Division (modeling source), NAVSEA (parent command), or treat as a multi-customer research track.
3. Decide whether to cross-link to PMTEC given the multidomain-training overlap (e.g., backlinking from PMTEC's §3.1 priority #6 "Realistic training targets" or priority #4 "Multi-level secure information sharing" given training-injection adjacency).

---

### 2026-05-21 — Scaffold decisions A/B/C confirmed

**By:** operator (confirmation via `/remote-control` chat)
**Rationale:** Three scaffold decisions flagged in the 2026-05-21 scaffold report were answered: (A) keep folder ID `BDR-FLEET-READINESS` despite deviation from `[OPPORTUNITY]-[CUSTOMER]` pattern; (B) customer field = `multi-customer research track`; (C) cross-link to PMTEC = yes.
**What changed:**
- `index.md` — `customer:` field set to "multi-customer research track" with candidate downstream customers (NSWC Carderock, NAVSEA, OPNAV/N9, PAE-IO/Amentum) noted as an inline comment for when the track resolves.
- `index.md` — added "Related research tracks" section linking to `PMTEC-USINDOPACOM/index`.
- `00_research-file.md` — header `Customer:` field updated to reflect Decision B.
- `PMTEC-USINDOPACOM/00_research-file.md` §3.1 priority #6 ("Realistic training targets") — added inline cross-link to this track so the connection is discoverable from both directions.
- `auto_find:` remains `false` in `index.md` — pending operator's explicit "begin research" trigger before source ingestion starts.

**Next pending decision:** Operator says "begin research" to flip `auto_find:true`, configure `_search-config.yaml` (NAVSEA / Carderock / SASC / GAO / CRS / DoD comptroller queries), and start running disconfirming-evidence checks per §10.3 sequencing.

---

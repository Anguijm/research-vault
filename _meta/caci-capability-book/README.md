---
schema_version: 1
last_full_update_utc: '2026-05-31T05:00:00Z'
sessions_complete: 4
---

# CACI Capability Book

This directory holds a structured, source-cited description of CACI's corporate-level capabilities. The capability book is the **scoring layer** for the opportunity-discovery pipeline — it answers "does this notice match a CACI-corporate capability?" — distinct from the **query layer** (which slices SAM.gov by Pacific contracting offices) and the **filter layer** (which narrows to the operator-team's reach and contract vehicle).

## Why this exists

Without a capability book, the ranker only knows aggregate award statistics (`baseline_caci_footprint` and `directional_caci_footprint` in `_meta/caci-discovery-config.yaml`). It cannot reason about whether a specific notice's scope of work resembles a CACI capability area in narrative terms. The capability book closes that gap.

It enables the **three-way notice classification** the operator uses:

- **Direct-execute** — high CACI-capability match + high team-execution fit → bid lead
- **Relationship-lead** — high CACI-capability match + low team-execution fit + high customer-access fit → introduce CACI division
- **Customer-intel** — low CACI-capability match + high customer-access fit → relationship intelligence, not a bid

The relationship-lead category specifically requires the corporate capability book — without it, the operator cannot recognize "CACI can deliver this even though my team cannot."

## What's in this directory (after Sessions 1-4)

| File | Source | Purpose |
|---|---|---|
| `README.md` | this file | index and methodology |
| `capability-areas.md` | caci.com (7 capability pages) + FY25 10-K Business section | top-level 7-area taxonomy in CACI's own marketing AND investor language |
| `business-fy25-overview.md` | FY25 10-K Business section | corporate context not specific to one capability area: Expertise+Technology frame, scale ($8.6B / 25K employees), customer mix, contract instruments, acquisition pace, CRADLE facility |
| `growth-signals.md` | FY25 10-K MD&A + FY26 Q3 10-Q refresh | §0 has current-state (FY26 Q3): GFY26 DoD topline $838.7B, two shutdowns, ARKA closed, 78% DoD+IC concentration. §1-§7 preserved as FY25-baseline historical context. |
| `acquisitions.md` | press releases (2023-2025) | five of seven recent CACI acquisitions identified by name; ARKA Group ($2.6B, FY26) flagged forward; two FY24 acquisitions still unnamed |
| `vehicles.md` | caci.com/contracts | eight IDIQs + six GSA Schedules with contract numbers and PoP dates; **DTIC IAC MAC (FA807518D0006)** = operator-team's vehicle, recompetes 2027-09-29; vehicle-to-capability-area mapping |
| `source-ledger.md` | — | citation index; every claim in any other file references an entry here |
| `past-performance/top-25-by-amount.md` | USAspending top-25 CACI awards (FY19-FY26, sorted by amount) | concrete past-performance citations with PIIDs, parent IDVs, periods; cross-referenced to capability areas; **EH02 SHIP DESIGN SERVICES** confirms naval-architecture past performance for operator-team relevance |

## The capability taxonomy (one-line summary per area)

For full descriptions see `capability-areas.md`. CACI's seven capability areas as published at `caci.com`:

1. **C3I** — Command, Control, Communications, and Intelligence; multi-domain decision superiority
2. **Cyber** — Offensive/defensive operations, critical infrastructure defense, information dominance
3. **Digital Solutions** — Agile modernization of government enterprise apps and business processes
4. **Enterprise IT** — End-to-end IT infrastructure modernization for ~50 federal agencies
5. **Mission and Engineering Support** — Platform integration, naval architecture, M&S, training, logistics
6. **Space** — Space domain awareness, multi-source intelligence, decision support
7. **Spectrum Superiority** — Software-defined RF/EW/SIGINT technology for the electromagnetic spectrum

AI is positioned as a cross-cutting sub-capability of every area, not a standalone area.

## Highlights from Sessions 1-4 (what's most operationally useful)

> **The operator-team's contract is DTIC IAC MAC (Defense Technical Information Center Information Analysis Center Multiple Award Contract), FA807518D0006, recompete 2027-09-29.** This vehicle is in the candidate path for five of seven CACI capability areas — structurally a high-flexibility vehicle, corroborating the operator's intuition that there is more reach available than the team has historically used. See `vehicles.md` §1.

> **CACI's "Mission and Engineering Support" 10-K language explicitly includes "naval architecture, training and simulation services, logistics engineering"** — the team's Waterfront Operations and Workforce/Org Dev sub-team work is corporate-corroborated, not a stretch claim. See `capability-areas.md` §5.

> **CACI's named market trends include "near-peer competitors and other nation state threats" as a growth focus.** The operator-team's INDOPACOM region is the primary U.S. near-peer-competition AOR. The team's geography aligns with CACI's stated strategic direction. See `growth-signals.md` §3 trend #5.

> **GFY26 defense funding picture (refreshed from FY26 Q3 10-Q, March 2026):** GFY26 DoD topline came in at **$838.7 billion** — approximately $54B lower than GFY25's $893B CR level, but $8.4B above the President's PBR. The OBBBA's $156B defense supplemental remains available. The FY25 10-K's projected "+13% defense growth" did not materialize as projected; appropriations came in lower with the supplemental remaining intact. **Two government shutdowns occurred during GFY26** (Oct 1-Nov 12, 2025; Jan 30-Feb 3, 2026), and **DHS remains in partial shutdown as of the most recent reporting**. See `growth-signals.md` §0.

> **Azure Summit Technology acquisition ($1.275B, Oct 2024) substantially expanded the Spectrum Superiority area** with 300+ employees in RF/EW/SIGINT engineering. Recent capability addition. See `acquisitions.md`.

## Discipline reminders

- Every claim cites a source slug in `source-ledger.md`.
- FACT / Assessment / Speculation labels per the vault SOP.
- Named-entity discipline: contractor / product / person names appear here ONLY when the cited source surfaces them.
- All capability area names use CACI's own wording from the source, not paraphrased.

## Future refresh cadence

- **Annual**: refresh after each new CACI 10-K filing (typically August each year for fiscal year ending June 30).
- **Quarterly**: optional refresh from 10-Q filings for growth-signal drift.
- **Event-driven**: refresh acquisitions.md when CACI announces an M&A transaction.

## Known research gaps

- Two FY24 acquisitions remain unnamed; deeper press-release pass needed (acquisitions.md §4).
- The specific IAC under DTIC IAC MAC that the operator-team's task order falls under (vehicles.md §5).
- The sponsoring agency for the operator-team's specific task order vs. the administering AF contracting office.
- CRADLE facility location (CONUS or also Pacific).
- USAspending top-50 awards detail (deferred to future Session 4 follow-up — would benefit from the IDV-family pull Gemini recommended in the slice-plan red-team).

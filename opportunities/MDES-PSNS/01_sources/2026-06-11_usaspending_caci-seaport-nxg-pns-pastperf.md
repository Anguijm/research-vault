---
type: source
opportunity: MDES-PSNS
title: CACI SeaPort-NxG vehicle + Portsmouth Naval Shipyard engineering task orders (SHAPEC / DSSP) — federal award data
url: https://www.usaspending.gov/award/CONT_IDV_N0017819D7295_9700/
publisher: usaspending.gov (federal award data)
publication_date: 2026-06-11   # data current as of pull date
captured: 2026-06-11
captured_by: ingest.py          # pulled via _scripts/lib/usaspending.py
source_tier: 1                  # federal award data — primary
content_type: other             # structured award records
key_quotes_extracted: false
verified: 2026-06-11
content_sha256: 4af378067d8fad004ffc7b7ed31008cee839db71020e8ed4c60b3888a809913b
backfilled_hash: true
---

## Summary

Primary federal award data validating CACI's submarine-modernization engineering past
performance — previously sourced only to trade press [s.2026-06-11-caci-pns-task-order].
Confirms (a) the contracting **vehicle** is the Navy's **SeaPort-NxG** professional-
services IDIQ, held by CACI; (b) the **tasking** is a continuous line of engineering
support at **Portsmouth Naval Shipyard** for the **Ships Availability Planning and
Engineering Center (SHAPEC)** and the **Deep Submergence Systems Program (DSSP)**; and
(c) the work is **NAICS 541330 (Engineering Services)** — the exact code of the Puget
Sound Marine Design and Engineering IDIQ (Notice 3059-9900). This is directly relevant
past performance, not merely analogous.

## The vehicle (Indefinite-Delivery Contract / IDV)

| Field | Value |
|---|---|
| PIID | **N0017819D7295** |
| Name | SEAPORT-NXG |
| Holder | CACI, INC. - FEDERAL |
| Awarding office | Dept. of the Navy / **NSWC Dahlgren** |
| Period of performance | 2019-01-02 → 2029-01-01 |
| USAspending | https://www.usaspending.gov/award/CONT_IDV_N0017819D7295_9700/ |

## The tasking (Portsmouth Naval Shipyard engineering support task orders)

All: awarding office **Portsmouth Naval Shipyard** (Dept. of the Navy); **NAICS 541330
Engineering Services**; PSC **R425 (Support – Professional: Engineering/Technical)**.

| Task order | Holder | Obligated | Period | Parent vehicle | Scope (as stated in the award) |
|---|---|---|---|---|---|
| **N3904025F3001** | CACI, INC. - FEDERAL | $18,119,153 | 2025-08-28 → 2030-07-31 | N0017819D7295 (SeaPort-NxG) | "Portsmouth Naval Shipyard (PNS) Engineering Support Services" (current follow-on) |
| **N3904020F3000** | CACI, INC. - FEDERAL | $74,472,900 | 2020-03-20 → 2025-08-31 | N0017819D7295 (SeaPort-NxG) | "Engineering Support Services" |
| **N3904017F3000** | CACI TECHNOLOGIES, LLC | $16,325,464 | 2017-03-08 → 2020-03-31 | N0017804D4026 (SeaPort-e, predecessor vehicle) | "…the Contractor shall provide the necessary engineering, technical, administrative and managerial (support)… **in support of Ships Availability Planning and Engineering Center (SHAPEC) and the Deep Submergence Systems Program (DSSP)**" |

USAspending award pages:
- https://www.usaspending.gov/award/CONT_AWD_N3904025F3001_9700_N0017819D7295_9700/
- https://www.usaspending.gov/award/CONT_AWD_N3904020F3000_9700_N0017819D7295_9700/
- https://www.usaspending.gov/award/CONT_AWD_N3904017F3000_9700_N0017804D4026_9700/

## Notes

- **SHAPEC + DSSP scope is verbatim in the 2017 task order (N3904017F3000)**, on the
  predecessor vehicle SeaPort-e. The 2020 and 2025 task orders are the continuation of
  the same Portsmouth engineering-support line on **SeaPort-NxG** — same awarding office,
  same NAICS, same recipient lineage — but their public descriptions are abbreviated
  ("Engineering Support Services" / "PNS Engineering Support Services") and do not repeat
  the SHAPEC/DSSP language verbatim. So the SHAPEC/DSSP attribution is firmly sourced for
  the program line; treat the specific 2020/2025 scope as "same line, abbreviated public
  description" rather than independently re-confirmed.
- Combined CACI Portsmouth engineering-support obligations across the three task orders:
  ~$109M (2017–2030).
- The earlier trade-press figure of ">$83M, base + four options" aligns with the
  N3904020F3000 / N3904025F3001 task-order family on SeaPort-NxG.
- Pulled 2026-06-11 via `_scripts/lib/usaspending.py` (`fetch_award_by_id`).

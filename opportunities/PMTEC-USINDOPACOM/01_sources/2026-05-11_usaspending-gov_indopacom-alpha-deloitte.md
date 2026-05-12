---
type: source
opportunity: PMTEC-USINDOPACOM
title: "Deloitte INDOPACOM Alpha — GSA OASIS Delivery Order 47QFCA25F0010 (USAspending record)"
url: https://www.usaspending.gov/award/CONT_AWD_47QFCA25F0010_4732_GS00Q14OADU113_4732/
publisher: usaspending.gov
publication_date: 2025-03-01
captured: 2026-05-11
captured_by: operator
source_tier: 1
content_type: contract_record
key_quotes_extracted: false
verified: 2026-05-11
piid: 47QFCA25F0010
parent_idiq_piid: GS00Q14OADU113
recipient_uei: CKV2L9GZKJK3
---

## Summary

USAspending.gov authoritative contract record for the Deloitte-prime task order
supporting USINDOPACOM (commonly referred to industry-side as "INDOPACOM Alpha").
Captured via USAspending.gov public API on 2026-05-11. Verifies awardee, vehicle,
customer, place of performance, and start date. Ceiling and final option-period
end date are not present in USAspending's record for this task order (FPDS data
gap on `base_and_all_options_value`) — those remain industry-reported only.

## Extracted content

### Award

- **PIID:** `47QFCA25F0010`
- **Type:** DELIVERY ORDER (i.e., task order under an IDIQ)
- **Category:** contract
- **Description:** "THE PURPOSE OF THIS AWARD IS TO PROVIDE ENTERPRISE-WIDE
  PROFESSIONAL SERVICES TO SUPPORT UNITED STATES INDO-PACIFIC COMMAND."
- **Total obligation to date:** $58,923,548
- **`base_and_all_options_value`:** null (not reported by FPDS)
- **Place of performance:** Hawaii (state code HI; city code not reported)
- **Period start:** 2025-03-01
- **Period current end (Year 1):** 2026-07-31

### Recipient

- **Name:** DELOITTE CONSULTING LLP
- **UEI:** `CKV2L9GZKJK3`

### Awarding chain

- **Awarding agency:** General Services Administration
- **Awarding sub-agency:** Federal Acquisition Service
- **Funding agency:** Department of Defense
- **Funding sub-agency:** Department of the Navy
  - (USINDOPACOM unified-command funding generally flows through component
    service accounts; Navy is consistent with INDOPACOM HQ at Camp H.M. Smith.)

### Parent IDIQ (vehicle)

- **PIID:** `GS00Q14OADU113`
- **Description:** "ONE ACQUISITION SOLUTION FOR INTEGRATED SERVICES (OASIS)
  PROFESSIONAL SERVICES MULTIPLE AGENCY CONTRACT, IGF::OT::IGF"
- **Type:** INDEFINITE DELIVERY / REQUIREMENTS, MULTIPLE AWARD
- **Vehicle:** GSA OASIS (Unrestricted Pool)
- **Prime on parent IDIQ:** DELOITTE CONSULTING LLP

### Cross-reference to research-file claim

Original FACT in `00_research-file.md` §6.1:

> "Sub on Deloitte INDOPACOM Alpha — $467M GSA OASIS TO, period 1 Mar 2025 –
> 28 Feb 2030. Embedded staff at Camp H.M. Smith including PM/Exercise Planner
> SME [s.HigherGov-indopacom-alpha]."

**Verified from this USAspending record:**
- Deloitte is the prime ✓
- Vehicle is GSA OASIS ✓ (parent IDIQ `GS00Q14OADU113`)
- Customer is USINDOPACOM ✓
- Place of performance is Hawaii (consistent with Camp H.M. Smith) ✓
- Period starts 2025-03-01 ✓

**Not verified by this record (still single-sourced to HigherGov):**
- The $467M ceiling figure — USAspending shows only $58.9M obligated and the
  `base_and_all_options_value` field is null. The $467M may be the 5-year
  ceiling (base + 4 options); HigherGov typically derives ceilings from FPDS
  + IDIQ records that may be more complete than the API exposes.
- The 28 Feb 2030 final end date — USAspending shows current period ending
  2026-07-31 (Year 1). If $467M is a 5-year ceiling, 2030-02-28 is plausible
  as the all-options-exercised end date, but is not in the API record.
- CACI as a sub on this task order — USAspending does not report subcontractor
  rosters at the task-order level.

### Method

```python
# Search step (api.usaspending.gov)
POST /api/v2/search/spending_by_award/
{
  "filters": {
    "award_type_codes": ["A","B","C","D"],
    "recipient_search_text": ["Deloitte"],
    "time_period": [{"start_date": "2024-08-01", "end_date": "2026-05-11"}],
    "place_of_performance_locations": [{"country":"USA","state":"HI"}]
  },
  ...
}
# → 1 result: 47QFCA25F0010

# Detail step
GET /api/v2/awards/CONT_AWD_47QFCA25F0010_4732_GS00Q14OADU113_4732/
GET /api/v2/awards/CONT_IDV_GS00Q14OADU113_4732/   # parent
```

## Notes

- HigherGov record `[s.HigherGov-indopacom-alpha]` remains the only source for
  the ceiling value and the 28 Feb 2030 end date. Treat those two specifics as
  industry-reported, not USG-confirmed, until corroborated.
- Re-query USAspending quarterly to track obligation growth toward the alleged
  $467M ceiling and any reported period-of-performance extensions.
- SAM.gov retry pending — when the api.sam.gov key clears its 24-hour
  new-account throttle, search for the original award announcement and any
  modifications to this PIID; either may surface the ceiling.
- For future contract verifications, see backlog Phase 4d: add a `usaspending.py`
  lib alongside `sam_gov.py` to automate this pattern.

---
name: PSNS barges YR-85 / YR-95 deployed in Japan via PSNS detachment
description: PSNS-named barges in Japan are deployed at a Puget Sound Naval Shipyard detachment colocated in Japan; work on them is performed by SRF-JRMC or contracted by SRF-JRMC. Notices for these barges appear in SAM.gov under `organizationName=NAVSUP FLC YOKOSUKA` despite the "Puget Sound" naming.
type: project
originSessionId: 254eda7f-7db4-4f93-b460-1e14e2726754
---
The Yard Repair / utility barges **YR-85** and **YR-95** are named for Puget Sound Naval Shipyard (PSNS) administratively but are physically deployed in Japan at a PSNS detachment that's colocated there. Operator confirmed this on 2026-06-02 in response to the 8-slice batch run that surfaced two "6A1 Preventive Maintenance / Corrective Maintenance for PSNS Barge YR-85 and YR-95" notices through the `nav_yokosuka` slice (organizationName = NAVSUP FLC YOKOSUKA).

**Why:** The "Puget Sound" in the barge names is administrative, not geographic. The physical location is Japan. The work on those barges is performed by or contracted by SRF-JRMC, which makes them operator-team customer-access surface despite the PSNS name. This is structural — these barges are likely a long-running pattern, not a one-time arrangement.

**How to apply:**

- When a SAM.gov notice surfaces with "PSNS" in the title under organizationName NAVSUP FLC YOKOSUKA, treat it as SRF-JRMC-customer-access content, not as Puget Sound-CONUS work. The 2026-06-02 batch surfaced these as CUSTOMER-INTEL classification (high customer access, low CACI capability fit on barge trades-maintenance) — that classification was correct and should stand.
- The pattern may extend beyond YR-85 and YR-95. Other PSNS-named hulls at the Japan detachment likely route through the same NAVSUP FLC Yokosuka contracting path. Future surfacing should be read with this lens.
- Do NOT add an automatic out-of-scope rule that drops "Puget Sound" notices at NAVSUP FLC Yokosuka — that would suppress real customer-access intel. The CUSTOMER-INTEL classification is the right outcome.
- Capability-area-match is correctly weak for these (mission_engineering at 0.33) — they're barge trades work, not engineering-services work. Score should stay where it is.

---
type: demo
opportunity: BDR-FLEET-READINESS
phase: 1
created: 2026-06-01
audience: personal-portfolio / operator
status: draft
---

# BDR Level-1 flash drill demo

This is the Phase 1 deliverable for the operator's personal-portfolio demonstration of the Battle Damage Assessment and Repair (BDAR) Level-1 flash-drill game concept described in `00_research-file.md` §11.3.1.

This folder holds content and a teaching framework — not software. The medium is intentionally physical: the scenarios are designed to be printed on cards and run by a human moderator with a small group around a table. The Phase 1 goal is to prove the game concept works in its lowest-technology form so the operator can show a working demonstration without committing to a software build.

## What's in here

- `README.md` — this file
- `00_facilitators-guide.md` — how to run a Level-1 flash drill session. Moderator brief, timing, learning objectives, after-action discussion prompts.
- `scenarios/` — initial set of three scenario cards in markdown. Each card is designed to print to a single sheet (one-sided, business-card-stock or letter-paper format). The scenarios are:
  - `01_forward-team-mobilization.md` — RMC has to send people, gear, badges, and rules-of-engagement prep to where a damaged ship is sitting in a foreign port.
  - `02_bdat-to-bdar-handoff.md` — RMC receives a Battle Damage Assessment Team report and has to sequence the repair plan under time pressure.
  - `03_surge-triage-under-tempo.md` — Multiple damaged ships arrive in a compressed window; the RMC wardroom triages the work.
- `_decisions.md` — design-decision log for this demo (what was chosen, why, what was rejected).

## Who this is for

The portrayed audience inside the scenarios is the **wardroom and staff cell at a U.S. Navy Regional Maintenance Center (RMC)** — the commanding officer, executive officer, department heads, training officer, and visiting fleet liaisons at a CONUS-based RMC. The RMC is the receiving side: the team that gets approached with a problem and has to mobilize against it. (The companion fleet-commander-side scenarios — port selection in particular — would run from the same scenario base for a different audience and are not part of Phase 1.)

The audience for the **demo itself** is the operator's personal portfolio: someone reviewing the operator's BD analyst work who wants to see an actual playable artifact of the BDR concept, not just the capture brief. Anyone who can read the scenario cards and run a 15-minute session has the moderator's job covered — no special training is required to demonstrate the demo.

## What this demo does NOT try to do

- It is **not the product CACI would sell**. The Level-1 product as described in the BDR brief is also analog and printed, but the customer-facing sale would include a curated scenario library, NWDC-aligned scenario content review, classification handling, and a multi-session engagement plan. This demo is the smallest end of that, scoped to demonstrate that the game mechanic works.
- It does **not** include software, web delivery, or any AI-driven content generation. Levels 4 and 5 of the BDR product progression are software-driven. This is intentionally Level 1.
- It does **not** include a comprehensive scenario library. Three scenarios are enough to prove the game format. The customer-facing product would have 15-25 minimum.
- It does **not** cite real personnel, real ships by hull name, or real third-country contractors. The scenarios use plausibly-fictional ship designators (e.g., DDG-XX) and real public port names only.

## How to use this

1. Read `00_facilitators-guide.md` end to end. Five to ten minutes.
2. Pick one scenario from `scenarios/`. Print it or display it on a phone.
3. Gather two or more people who can play the wardroom role. Set a 15-minute timer.
4. Run the scenario per the facilitator's guide. The wardroom picks an answer in 5-10 minutes. The defender presents in 60 seconds. Discuss for 3-5 minutes using the after-action prompts.
5. Repeat with a different scenario in a future session. Pattern recognition builds across sessions, not within one.

## Provenance and audit

All content in this folder is operator-authored and operator-reviewed. Named-entity discipline from `_entity-allowlist.yaml` applies. No fact claim in any scenario is taken from a primary source not already in the BDR `_decisions/` or `01_sources/` track — the scenarios are illustrative game content, not analytical claims about real events. Any scenario that uses a real port name uses it only as a geographic setting; no operational claim about that port is made beyond what is publicly visible (the existence of US Navy facilities at Yokosuka, Sasebo, Pearl Harbor, Apra Harbor, San Diego, and Bahrain is publicly known).

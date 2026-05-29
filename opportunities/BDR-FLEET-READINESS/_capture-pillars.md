# BDR-FLEET-READINESS — Capture pillars and scope context

This file is the opportunity-specific scope that `_scripts/find_sources.py` feeds into the four-pillar capture-intelligence ranker (`_scripts/lib/ranker.py::rank_candidates_capture`). The ranker combines the content of this file with the general four-pillar rubric to produce per-candidate scores during search. The general rubric lives in the ranker; this file lives in the opportunity so that scope changes update the ranker automatically without editing shared code.

Update this file whenever the corrected-scope, the customer set, the work-type keywords, or the out-of-scope list changes. The decision-log should reference the change.

## Opportunity hypothesis

CACI proposes a five-level progression of contractor-supplied gamified decision-rehearsal scenarios for two specific Navy audiences. The product is scenario content, exercise injection, and decision-rehearsal training; the audience is the team that makes operational decisions about damaged ships, not individual Sailors learning hand-skills.

The five-level progression: Level 1 is 5-to-15-minute flash drills on printed cards; Level 2 is 30-to-45-minute linked-decision sequences; Level 3 is one-hour gamified wardroom sessions; Level 4 is 2-to-4-hour multi-session campaigns; Level 5 is AI-driven scenarios injected into live fleet exercises such as COMPTUEX, RIMPAC, LSE, and SWARMEX.

The procurement path is a task order against CACI's existing GSA OASIS, NITAAC CIO-SP3, or GSA MAS vehicles.

## Audiences

Audience (a) is the Battle Damage Assessment and Repair (BDAR) staff cell at a Navy repair activity. The staff cell makes repair-prioritization and resource-routing decisions for the activity's portfolio of in-progress and queued repair work. The repair activities are the four public naval shipyards (Norfolk, Puget Sound, Pearl Harbor, Portsmouth), the Regional Maintenance Centers (RMCs), and the forward-deployed Ship Repair Facility Japan (SRF-JRMC).

Audience (b) is the fleet commander making operational decisions about a damaged ship. Specific decision types include port selection under combat tempo, forward team mobilization, and foreign-port emergency contracting. The decision-making organizations are PACFLT N7, FLTFORCOM N7, and INDOPACOM J7.

## Pillar-3 customer hierarchy

Direct customer organizations score 8-9 under Pillar 3 when they state a specific intent toward decision-rehearsal training, scenario-injection, staff-cell readiness, or wartime-repair-team training. They have local Operations and Maintenance Navy (OMN) funding and an immediate pain point. The direct customer organizations are:

- The four public naval shipyards: Norfolk Naval Shipyard, Puget Sound Naval Shipyard, Pearl Harbor Naval Shipyard and Intermediate Maintenance Facility, Portsmouth Naval Shipyard.
- The Regional Maintenance Centers (RMCs), including their headquarters Commander, Navy Regional Maintenance Center (CNRMC).
- Ship Repair Facility Japan and Regional Maintenance Center (SRF-JRMC).
- Fleet Forces Command N7 (FLTFORCOM N7).
- Pacific Fleet N7 (PACFLT N7).
- Indo-Pacific Command J7 (INDOPACOM J7).

Headquarters and policy organizations score 6-7 under Pillar 3 for the same kind of statement. They validate the market but do not directly produce a near-term task order. The HQ/policy organizations are:

- Naval Sea Systems Command Headquarters, principally NAVSEA 04 (Logistics, Maintenance and Industrial Operations), NAVSEA 05 (Ship Design, Integration and Engineering), and NAVSEA 21 (Surface Warfare).
- Assistant Secretary of the Navy for Research, Development and Acquisition (ASN RDA).
- OPNAV and the staff of the Chief of Naval Operations (CNO).
- The Office of the Secretary of the Navy (SECNAV).

## Work-type keywords

These keywords identify candidates that may carry the work-type CACI is proposing. A keyword alone is not enough to score well — the candidate must place the work-type in context that the four-pillar rubric recognizes.

Scenario design. Scenario injection. Wargaming. Wargames. Modeling and simulation. M&S. Decision support. Decision rehearsal. Exercise design. Exercise injection. Staff augmentation (when at a named customer organization). C5ISR exercises (when at a named customer organization). Joint Exercise Division (JExD) funding lines. MAGTF Tactical Warfare Simulation (MTWS) funding lines. Joint National Training Capability (JNTC). Live-Virtual-Constructive (LVC) training. Distributed Maritime Operations (DMO) command-and-control wargaming.

## Out-of-scope categories (Rule D floor at 3/10)

Items in any of these categories score a maximum of 3 under the locked rubric, regardless of how many keywords they match. The 2026-05-26 corrected-scope hypothesis is binding.

- Damage-control hand-skills training or individual-Sailor casualty-control schoolhouse content. This includes Damage Controlman rating training, fire-fighting drills at the deck-plate level, and rescue and assistance party drills.
- Navy Education and Training Command (NETC) content. Sailor 2025 program content. Ready Relevant Learning (RRL) program content.
- General Navy shipbuilding programs (Golden Fleet plan, BBG-X, Constellation-class frigate, new ship classes, Future Surface Combatant family) when the article does not address training, exercises, or decision-rehearsal scenarios.
- Shipyard physical infrastructure investment (drydock construction, crane modifications, MILCON projects, Shipyard Infrastructure Optimization Program (SIOP) milestones) when the article does not address training, exercises, or decision-rehearsal scenarios.
- General Navy information-technology modernization, Department of Government Efficiency Navy IT reviews, IT helpdesk vehicles, Navy enterprise software contracts, and similar IT modernization news.
- Aircraft training systems (TC-12 trainer, F-35 training, helicopter pilot training simulators) unless the article serves as a procurement precedent for a CACI work-type.
- Recruiting news, ceremonial events, command-philosophy speeches without a wartime-repair, BDAR, or decision-rehearsal angle.

## Procurement-precedent recognition

The rubric explicitly recognizes contractor-discovery and work-type precedent items even when they fall outside the Navy customer set. AFRICOM exercise-design contracts, OSD-led exercise-design contracts, Missile Defense Agency test/exercise/wargames contracts, and Joint Staff JExD or MTWS funding lines are all 7-8 under Pillar 4 because they represent the procurement path for the same work-type CACI would propose at the Navy customer set. The ranker should not downgrade these on "not at a Navy customer" reasoning.

## Notes on the named-entity discipline

Pillar 4 (contractor discovery) specifies the customer organizations and the work-type keywords but never specific contractor identities. Contractor names appear in inbox items as outputs of the search and ranking process, not as inputs. The audit scripts at `_scripts/audit_named_entities.py` and `_scripts/audit_search_config.py` enforce this discipline; the four-pillar ranker preserves it by design.

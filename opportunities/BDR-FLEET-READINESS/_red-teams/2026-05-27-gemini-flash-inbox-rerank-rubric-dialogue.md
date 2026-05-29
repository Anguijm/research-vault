---
title: Inbox re-rank rubric red-team (Gemini Flash)
date: 2026-05-27
analyst: jma
reviewer: Gemini 2.5 Flash via gemini-query
opportunity: BDR-FLEET-READINESS
scope_anchor: 2026-05-26 corrected-scope (gamified decision-rehearsal scenarios for repair-activity teams and fleet commanders)
purpose: Pressure-test a first-pass re-ranking prompt for the BDR-FLEET-READINESS inbox before adopting it as the standard ranker.
---

This file logs three rounds of dialogue between Claude (drafting the re-rank rubric) and Gemini Flash (red-teaming it). The starting condition was a 131-item inbox where the original generic-defense ranker had over-scored most items (60 of 131 sat at 8/10 or 9/10, including items the operator dismissed as off-topic on inspection). The first re-rank pass used a strict corrected-scope prompt that knocked almost everything down — 126 of 131 items moved down, only 4 items remained at 6/10 or higher. The operator asked for a red-team of the ranking judgments before agreeing to any drops.

Gemini Flash was used instead of Gemini Pro because the Pro 3 preview model returned a 404 from the API on the first request. Flash with `thinkingLevel: high` was used as the alternate.

## Round 1 — Claude posts the first-pass re-rank and asks Gemini to challenge

Claude described the corrected scope, the product progression, the customer set, the procurement path, the re-ranker prompt, the resulting distribution, and the specific items at the top. Asked five questions: is the rubric well-calibrated, are the top-4 the right load-bearing items, are my flagged disagreements correct, what category of items is the bulk-decline tier probably mis-handling, and what single rubric change would reduce false-drops on borderline items.

## Round 1 — Gemini Flash response (summary)

Gemini called the first-pass ranker a keyword-matcher rather than a capture-intelligence tool, with two specific failure modes.

The first failure mode is that the rubric is biased toward Level 5 of the product progression (AI-driven scenarios injected into live fleet exercises) because that level produces DVIDS posts and trade press, while Levels 1 through 4 are administrative, staff-cell-level, and not newsworthy. So the ranker over-rewards "an exercise happened" articles and under-rewards the staff-cell/wardroom evidence base that the bulk of the product would actually serve.

The second failure mode is that the rubric scores topic-match (does the article literally mention training, exercise, or gamification?) rather than capture-pillar match (does the article inform one of: the gap CACI's product solves, the funding/vehicle, the customer access path, the competitor presence?). Under the topic-match rubric, a USNI/CIMSEC analysis of the wartime-repair training gap scores 4 because it doesn't say "training" in the title, even though it directly motivates the product. Under a capture-pillar rubric, it scores 7+.

Gemini agreed all four of Claude's flagged disagreements (CIMSEC piece, the $1.2B nine-contractor Navy training contract modification, the Serious Games Challenge, and the four USAspending exercise/wargames task orders) were under-scored by the first-pass ranker.

Gemini also flagged a category Claude had not surfaced: items at the four customer organizations (the 4 public shipyards, RMCs, SRF-JRMC, PACFLT/FLTFORCOM/INDOPACOM N7/J7) that don't keyword-match training but signal competitor footprint or customer leadership intent. These are at risk of being bulk-declined because the first-pass rubric doesn't have a place for them.

Gemini proposed a four-pillar rubric: (1) Expeditionary Maintenance & Foreign Port Repair, (2) DMO and Decision-Rehearsal, (3) Command Intent and Priority Shifts at the customer orgs, (4) Contractor Discovery — commercial contracts at the customer orgs for work plausibly adjacent to scenario design or staff augmentation.

## Round 2 — Claude pushes back on three points

Claude accepted the four-pillar framing but pushed back on three specifics.

First, Claude defended keeping both the DVIDS primary-source post and the NavalNews trade-press write-up of the same event in the load-bearing tier. The two artifacts serve different purposes — the DVIDS post is the FACT-foundation source, the NavalNews piece is the industry-framing source. Gemini conceded the distinction but argued the trade-press piece should cap at 6 to avoid spending top-tier attention on what is, contractually, redundant intelligence.

Second, Claude flagged a hard vault rule: the ranker must not be pre-loaded with named commercial contractors (no "boost if mentions Booz Allen, SAIC, HII Mission Technologies"). That contamination pattern is what the vault's named-entity audit exists to prevent. Claude proposed a contamination-safe revision of Pillar 4: rank an item high if (a) the awardee on the contract is a commercial contractor — identity not pre-specified — AND (b) the contract is for work at a named Navy customer org — list of orgs is pre-specified — AND (c) the work-type is plausibly adjacent to scenario design, wargaming, exercise support, or staff augmentation — work-type keywords are pre-specified. The contractor's identity becomes the discovery, not the input. Gemini agreed this revised framing sidesteps the contamination concern while still surfacing what Pillar 4 is meant to surface.

Third, Claude distinguished two kinds of Pillar 3 signal: a personnel announcement (e.g., "RDML X assumes command of Pearl Harbor Naval Shipyard") versus a statement of intent (e.g., the same RDML giving a speech about decision-rehearsal as a priority). Claude argued personnel announcements alone should land at 5 (useful for the POC directory, not for proposal content), and only statements of intent should land at 8+. Gemini agreed.

## Round 3 — Claude locks down three remaining ambiguities

Claude asked Gemini to commit on three points before the rubric was implemented.

The first point was Pillar 1 generosity. Gemini's draft scored a DVIDS report of a wartime-repair rehearsal at 8-9. Claude argued that foreign-port wartime-repair rehearsals are the PROBLEM SPACE that motivates the product, not the WORK being sold. The product is contractor-supplied scenario design and exercise injection. A primary-source article confirming the Navy is doing wartime-repair rehearsals is FACT-foundation for the problem statement but not a procurement-decision signal. Claude proposed: 7 for operations/rehearsals, 9 only for contracting or tasking that names a scenario-design vendor or a Navy office tasking such a vendor. Gemini agreed and tightened the rule to: "If the item describes a military operation that matches our use case, it is a 7. If the item describes the administrative, contractual, or technical delivery of that use case, it is a 9."

The second point was Pillar 3 blast-radius. Gemini's draft included NAVSEA 04/05/21 (headquarters) in the same tier as the executing customer orgs (shipyards, RMCs, SRF-JRMC, PACFLT N7, etc.). Claude argued NAVSEA HQ is one tier removed — they own shipyard policy but they don't issue the task order or constitute the audience for the scenarios. Claude proposed a split: direct-customer orgs at 8-9 when they state a priority shift toward decision-rehearsal training, HQ/policy orgs (NAVSEA HQ, ASN RDA, OPNAV) at 6-7 for the same kind of statement. Gemini agreed and added the reasoning: HQ statements often validate the existence of a market but don't produce a task order for 18-24 months, while a shipyard commander or RMC deputy voicing the same need has a local pot of operations-and-maintenance Navy (OMN) money and an immediate pain point.

The third point was technical-limitation rules for thin-snippet candidates (USAspending records that arrive with no descriptive text) and big-PDF candidates (multi-thousand-page budget documents where one line could be load-bearing). Gemini agreed to two explicit rules. For USAspending: if URL is usaspending.gov AND the contract title matches a Pillar 2 or Pillar 4 work-type keyword (exercise, wargame, scenario, modeling, simulation, staff augmentation, decision support, training), score 7-8 with the note "thin-snippet, requires manual ingest to verify." For DoD budget documents (comptroller.war.gov, comptroller.defense.gov, secnav.navy.mil/fmc/fmb, congress.gov bill text): score MAX 7 if the title is keyword-relevant, with the note "high-level budget justification, requires targeted PDF search for program elements such as Joint Exercise Division or MAGTF Tactical Warfare Simulation." Budget documents never hit 8 or 9 because the LLM can't see whether the load-bearing line is on page 10 or page 2,000.

## Conclusions

The rubric Claude will implement is the four-pillar version with three modifications: (a) Pillar 1 operations/rehearsals cap at 7 — only contracting or tasking hits 9; (b) Pillar 3 direct-customer orgs at 8-9, HQ policy orgs at 6-7; (c) two explicit technical-limitation rules for USAspending thin-snippet records (auto 7-8) and DoD budget documents (max 7).

The named-entity discipline is preserved through the contamination-safe framing of Pillar 4: the rubric specifies the customer orgs (closed list) and the work-types (closed list), but never the contractor identities. Contractor identities surface as outputs of the ranker, not inputs.

The action plan on the post-re-rank distribution:
- 7-9: priority ingest, these go into brief drafting and the verifier pipeline.
- 5-6: monitor tier, indexed and stored, queried at proposal-drafting time.
- ≤4: archive, do not look at.

## Follow-on actions

1. Implement the locked rubric in `/tmp/rerank_inbox_v2.py` and run against the 131-item inbox (which already has the first-pass corrected-scope scores tagged in each block — the v2 ranker will overwrite those).
2. Surface the new distribution to the operator and let the operator confirm the 7-9 keep-set before any items are bulk-declined.
3. If the operator confirms the cut, update the rubric in `_scripts/lib/ranker.py` and in `_scripts/find_sources.py` so future passes use it from the start.
4. Decision-log entry covers all three rounds and the final rubric.

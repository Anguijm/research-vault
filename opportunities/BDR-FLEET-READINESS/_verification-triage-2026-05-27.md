---
title: FACT-verification triage — BDR-FLEET-READINESS v0.4 capture brief / 2026-05-27 verifier sweep
date: 2026-05-27
analyst: Claude Code (Opus 4.7)
status: awaiting operator review
upstream_report: _verification-2026-05-27.md
purpose: For each PARTIAL or UNVERIFIABLE FACT in the 2026-05-27 verifier sweep, surface the verifier's missing-element note and propose a concrete resolution. The operator marks APPROVE / OVERRIDE per FACT, then Claude applies the resolutions in a single edit pass.
---

This document lists the 19 PARTIAL FACTs and 2 UNVERIFIABLE FACTs from the 2026-05-27 verifier sweep, in research-file FACT-number order. Each entry leads with the FACT identifier and a one-line description of why the verifier flagged it, then shows the verifier's missing-element note, then proposes a concrete resolution. The proposed resolutions cluster into a few patterns: PIID typos to correct, scope-note prose to split out into Assessment paragraphs, multi-source claims to tighten to the cited source only, and a small set of structural fixes (priority names, document attribution, fiscal-year alignment).

Two of the entries are UNVERIFIABLE because the FACT body contains no `[s.xxx]` citations at all (FACTs #45 and #46). Those require either source-ingestion or downgrade to Assessment — Claude cannot guess what the operator intended to cite.

The named-entity discipline is at issue in two PARTIALs (FACT #45 references contractor names and dollar amounts from inbox triage that were never tied to ingested sources, and FACT #6 / #34 / #38 conflate multiple Navy organizations' parallel releases under a single citation). These are flagged where they occur.

For each FACT, you can write your decision in the **Operator decision** line: `APPROVE` (apply the proposed resolution), `OVERRIDE: <your direction>` (apply this instead), or `DEFER` (leave as PARTIAL/UNVERIFIABLE for a later pass and accept the v1.0 standard does not require closure on this FACT).

---

## Bucket A — PIID typo fixes (mechanical)

### FACT #22 (§3) — PARTIAL — PIID typo: claim says 47QFCA20F0042; source says 47QFCA20F0002

The claim is otherwise correct. The verifier also flagged the description of `GS00Q14OADU121` as "OASIS-equivalent" — the source describes it only as IDC. The OASIS-equivalent characterization is a CACI-vehicle-portfolio interpretation that should not live inside the FACT.

**Proposed resolution:** Correct PIID typo `47QFCA20F0042` → `47QFCA20F0002`. Move the "OASIS-equivalent governmentwide vehicle" characterization out of the FACT and into the surrounding Assessment paragraph (the vehicle's role as an OASIS-equivalent is analytical interpretation, not a fact in this contract record).

**Operator decision:** _________________
Approve
### FACT #47 (§6) — PARTIAL — Same PIID typo (`47QFCA20F0042` → `47QFCA20F0002`) plus same OASIS-equivalent characterization

Same resolution as #22 — these are likely two instances of one upstream PIID typo that propagated.

**Proposed resolution:** Correct PIID and move OASIS-equivalent characterization out of FACT body.

**Operator decision:** approve _________________

---

## Bucket B — Multi-source attribution: claim names several Navy orgs but only one is cited

### FACT #6 (§3) — PARTIAL — Claim says Seventh Fleet, SRF-JRMC, USINDOPACOM, and COMPACFLT all published parallel releases; the single cited source is the DVIDS USS Ashland release

The verifier confirmed the Ashland exercise happened but found no mention of SRF-JRMC, USINDOPACOM, or COMPACFLT publishing parallel releases — the cited source is one DVIDS release, not the "all published parallel releases" claim.

**Proposed resolution:** Tighten the FACT to what the cited source actually says — Seventh Fleet released a DVIDS report on the USS Ashland Ship Wartime Repair and Maintenance Exercise in the Philippines. Move the "SRF-JRMC, USINDOPACOM, and COMPACFLT also published" portion into an Assessment paragraph noting the parallel-release pattern is the operator's observation across the customer-org landing pages, not a quoted source claim. (Alternative: ingest the SRF-JRMC, USINDOPACOM, and COMPACFLT pages and split FACT #6 into four citation-anchored FACTs. Heavier but more durable.)

**Operator decision:** approve_________________

### FACT #34 (§4) — PARTIAL — Same multi-source attribution issue plus "SWARMEX" name unattributed

Claim names SRF-JRMC, Seventh Fleet, USINDOPACOM, COMPACFLT as co-executors of "SWARMEX" at Cebu; source is a single Ashland release that does not use the SWARMEX name and does not list the other three orgs.

**Proposed resolution:** Combined fix with FACT #6 — tighten to what one cited source actually states (Seventh Fleet press release about Ashland's wartime-repair exercise at the Philippines). Drop "SWARMEX" terminology from the FACT body; if the SWARMEX name is needed for cross-reference, treat it in the surrounding Assessment as the operator's shorthand for the Ship Wartime Repair and Maintenance Exercise (SWaRMEx) program.

**Operator decision:** _________________
Approve 
### FACT #38 (§4) — PARTIAL — Claim attributes the press release to COMPACFLT specifically; source content doesn't self-identify the publisher (only the URL domain does)

The URL domain is `cpf.navy.mil`, which is COMPACFLT. But the source text itself does not say "COMPACFLT publishes this release."

**Proposed resolution:** Tighten claim to "A press release on the COMPACFLT website (cpf.navy.mil) reports..." rather than "COMPACFLT published a press release saying..." This is a minor language move that aligns FACT to source content while preserving the attribution that the URL domain provides.

**Operator decision:** approve_________________

### FACT #15 (§3) — PARTIAL — Same pattern: Pacific NAVFAC attribution comes from the URL, not the document text

Claim says "Pacific Naval Facilities Engineering Command (NAVFAC) published a SIOP brief..." Source content doesn't say "Pacific NAVFAC published this"; the URL `pacific.navfac.navy.mil` is the only attribution signal.

**Proposed resolution:** Tighten to "A SIOP brief on the Pacific NAVFAC site (pacific.navfac.navy.mil) documents PSNS-SBS infrastructure investments." Combine with the Bucket C fix on this FACT (split the Assessment scope note out of the FACT body).

**Operator decision:** _________________

### FACT #30 (§4) — PARTIAL — Same Pacific NAVFAC attribution and same Assessment-leak issue

Duplicate of FACT #15 in §4. The same Assessment paragraph wraps both. Same resolution applies.

**Proposed resolution:** Apply the same URL-attribution tightening as FACT #15. If FACT #15 and FACT #30 carry the same content, consider consolidating into one FACT and adjusting the cross-section reference.

**Operator decision:** _________________

---

## Bucket C — Scope-note / Assessment prose embedded inside the FACT body

### FACT #4 (§3) — PARTIAL — Claim has a `Scope note:` paragraph asserting what Contested Logistics funds (and does NOT fund) that the source doesn't explicitly enumerate

The source confirms the $0.6B Contested Logistics line item and the adversaries-targeting-supply-lines justification verbatim. It does not enumerate "spares, fuel distribution, lift capability, port-security assets" nor explicitly exclude "training scenarios" — that enumeration is operator interpretation of what physical-logistics-resilience funds typically buy.

**Proposed resolution:** Split into two paragraphs in the research file: the FACT now contains only the $0.6B Contested Logistics line item plus the verbatim "adversaries will target supply lines, ports, and communications" quote; the scope-note becomes an `**Assessment:**` paragraph immediately following, stating that physical-logistics-resilience line items typically fund spares/fuel/lift/port-security and not training scenarios. The Assessment doesn't need source-grounding because it is interpretive.

**Operator decision:** _________________

### FACT #9 (§3) — PARTIAL — Claim cites a DVIDS USS Iwo Jima damage-controlmen training piece but the FACT body refers to SWARMEX-Cebu, §1 decision moments, §11.3 BDAT pipeline, and the 2026-05-26 scope correction — none of which the source supports

The DVIDS source confirms the damage-control training event aboard USS Iwo Jima. Everything else in the FACT body is internal vault cross-reference, not source content.

**Proposed resolution:** Tighten the FACT to only what the DVIDS source supports — a DVIDS release covering USS Iwo Jima damage-control training in simulated casualty scenarios (flooding, fire, hull rupture). Move all cross-vault references (SWARMEX-Cebu comparison, §1 decision moments, §11.3 BDAT pipeline distinction, scope-correction commentary) into a surrounding Assessment paragraph or a separate `**Note:**` paragraph that explicitly says "this FACT is included to contrast with the corrected-scope direction; the source's deck-plate damage-control training is what §11.3 names explicitly out of scope."

**Operator decision:** _________________

### FACT #31 (§4) — PARTIAL — Claim says 6 SIOP projects are "across the four public shipyards" but source only says 6 SIOP projects without naming the shipyards

The DON Press Brief says "Invests in construction for 6 SIOP projects." It does not say where. The operator's interpretation (that they distribute across the four public shipyards) is reasonable but not stated.

**Proposed resolution:** Tighten the FACT to "The DON FY27 Press Brief funds six SIOP construction projects in FY27" with no shipyard distribution claim. Move the "across the four public shipyards" attribution into the Assessment paragraph that follows, noting that SIOP doctrine and historical SIOP project listings show the projects fall across the four public shipyards even when individual budget years don't enumerate them.

**Operator decision:** _________________

### FACT #44 (§5) — PARTIAL — Funder attribution detail (DoN vs DoD/DoN sub-tier) and obligation amount edge case

Source lists funding agency as "Department of Defense / Department of the Navy" — DoD as top-tier, DoN as sub-tier. Claim says "Department of the Navy funder" alone. Minor.

**Proposed resolution:** Correct the funder language to match the source's two-tier hierarchy: "Department of Defense (Department of the Navy sub-tier) funder." Verify the total obligation amount against the source's specific reported field.

**Operator decision:** _________________

---

## Bucket D — Tighten exercise / program naming

### FACT #35 (§4) — PARTIAL — Claim refers to "SWARMEX-Cebu"; NavalNews source describes it as a "wartime repairs rehearsal at Cebu South Port" without using SWARMEX terminology

The NavalNews piece confirms Philippine Naval Sea Systems Command participation. It does not call the exercise SWARMEX.

**Proposed resolution:** Tighten the FACT to: "NavalNews identified Philippine Naval Sea Systems Command participation in the USS Ashland wartime-repair rehearsal at Cebu South Port" with no SWARMEX terminology. Note in the surrounding Assessment that SWARMEX is the program-level name across these Ship Wartime Repair and Maintenance Exercise events; individual NavalNews coverage refers to specific events rather than the program name.

**Operator decision:** _________________

---

## Bucket E — Document / fiscal-year / priority-name corrections

### FACT #16 (§3) — PARTIAL — Claim says "FY27 Department of Defense budget justification book"; source is a "Department of War" document, and the cited language sits under USMC JNTC Project 774 with FY2025 funding (not FY27)

The source quote is correct verbatim. But the framing is wrong: the document is the Department of War FY27 PB Justification Book (the executive branch retitled DoD as DoW in 2025), and the specific quoted text is from FY2025 funding under Project 774, not FY27 new funding.

**Proposed resolution:** Two corrections. First, "Department of Defense" → "Department of War" (the source's actual organizational name). Second, clarify that the quoted text is the description of the existing tool capability funded under Project 774 USMC JNTC, not a new FY27 line item. Update the Assessment paragraph if it relies on the "newly funded in FY27" framing — that framing is wrong.

**Operator decision:** _________________

### FACT #17 (§3) — PARTIAL — Same DoD / DoW issue plus FY-alignment: the JNTC project's FY2025 / FY2026 / FY2027 line shows $0.268M FY2025, $0 FY2026, $0 FY2027

Same root cause as FACT #16. The "initiates design and development" language is the source's wording, but it sits under a FY2025-only funding line. The brief's framing ("the same FY27 justification book initiates...") implies FY27 funding when there isn't any.

**Proposed resolution:** Same DoD → DoW correction. Then either (a) drop the "initiates" framing entirely if the FY27 budget doesn't fund this line; or (b) reframe to "the FY27 PB Justification Book references the joint exercise design and control tool initiated under Project 774 (USMC JNTC) with FY2025 funding"; or (c) move FACT #17 entirely to Assessment because the cited language doesn't anchor a current-FY funded activity. This is the FACT most worth your direct call.

**Operator decision:** _________________

### FACT #27 (§4) — PARTIAL — Claim names four FY27 priorities ("Lethal & Effective Force," "Total Force Readiness," "Capable & Resilient Warfighter," "Industrial & Logistics Capacity") that the Caudle testimony source does not use

The actual four FY27 Caudle priorities are "Battle Ready Sailors – Quality of Service and Warfighter Competence," then three others the verifier didn't fully quote in the missing-element note.

**Proposed resolution:** Read the Caudle source directly, extract the four actual FY27 priority names verbatim, and replace the FACT's incorrect priority names with the verbatim names. The structural claim (that the testimony frames FY27 around four priorities, with one explicitly covering maintenance) is correct; only the priority names need correcting. The Assessment paragraph downstream may also need adjustment if it built reasoning on the wrong names.

**Operator decision:** _________________

---

## Bucket F — Tighten article framing

### FACT #11 (§3) — PARTIAL — Claim attributes a specific framing ("peacetime throughput is the floor and wartime throughput needs to be higher") to the CIMSEC article that the article doesn't use verbatim

The article does state that planned peacetime maintenance shortfalls exist and that the Navy lacks salvage capability for battle damage in major conflict. That's a related argument but not the exact framing the FACT claims.

**Proposed resolution:** Tighten the FACT's paraphrase. Change "current peacetime repair throughput is the floor and wartime repair throughput needs to be higher" to the source's actual framing — that planned peacetime maintenance is already short and that the Navy lacks salvage capability for battle damage in major conflict. Cite the specific source quote.

**Operator decision:** _________________

---

## Bucket G — Split FACT into two

### FACT #25 (§4) — PARTIAL — Claim packages two separate signing events (Press Brief + May 2026 Shipbuilding Plan); cited source only supports the Press Brief

The DON Press Brief is signed by Cao. The May 2026 Shipbuilding Plan signing is a separate claim with no citation.

**Proposed resolution:** Split into two FACTs. FACT #25a: Cao signed the cover of the DON FY27 Press Brief dated 28 April 2026 (cited source supports). FACT #25b: Cao signed the foreword of the Navy's May 2026 Shipbuilding Plan — this needs a separate citation (the May 2026 Shipbuilding Plan as a document). If we don't yet have it ingested, FACT #25b becomes a NEW UNVERIFIABLE pending ingestion, or it gets removed pending ingestion.

**Operator decision:** _________________

---

## Bucket H — Use full source-quoted scope

### FACT #39 (§5) — PARTIAL — Claim describes scope as "broad professional services" with "exercise, training, and operations support as named scope"; full source quote names "plans, operations, logistics, engagement, training, exercise, and assessment support"

The source quote is more specific than the FACT's paraphrase.

**Proposed resolution:** Replace the FACT's paraphrase with the full verbatim source-quoted scope: "Plans, Operations, Logistics, Engagement, Training, Exercise, and Assessment Support to AFRICOM."

**Operator decision:** _________________

---

## Bucket I — Minor language tightening

### FACT #37 (§4) — PARTIAL — Claim describes the instruction as "joint instruction" governing "peacetime" Optimized Fleet Response Plan; source citation is verbatim correct, language framing is minor

The verifier's missing-element note here is mostly hairsplitting. The instruction numbers match.

**Proposed resolution:** Minor language tighten — change "joint instruction governing the peacetime Optimized Fleet Response Plan" to "joint COMUSFLTFORCOM/COMPACFLT/COMUSNAVEUR/COMUSNAVAFINST instruction governing the Optimized Fleet Response Plan" — drops the "peacetime" qualifier (which isn't in the source) and keeps the instruction-number citation intact.

**Operator decision:** _________________

---

## Bucket J — UNVERIFIABLE (no citations in FACT body)

### FACT #45 (§5) — UNVERIFIABLE — Claim names specific contractors and dollar amounts at NSWC Carderock with no `[s.xxx]` citations

Claim names SAIC at $50.9M, ManTech at $45.6M, Leidos at $41.4M, Noblis MSD at $39M (truncated in the report). These came from the 2026-05-26 USAspending re-ranking but were never tied to ingested USAspending records. This is the named-entity contamination risk — contractor names and dollar figures in analytical content without source backing.

**Proposed resolution:** Two paths. (a) **Ingest the underlying USAspending records.** Run a USAspending deep-fetch for each named Carderock contract, ingest each as a source in `01_sources/`, add citations to the FACT body, re-run the verifier on FACT #45. This source-grounds the named entities properly. (b) **Remove the named-contractor list and dollar amounts from FACT #45 entirely.** Replace with "USAspending records for NSWC Carderock surface specific contractors at the tens-of-millions level pursuing acoustic-signature, signature-training, and Carderock-related work; specific contractor names and obligations require USAspending ingestion before they earn FACT status." Soft because no entity is named but compliant with discipline.

Path (a) is the cleaner v1.0 fix if you want these names in the brief. Path (b) is the cleaner fix if these names were aspirational rather than load-bearing.

**Operator decision:** _________________

### FACT #46 (§6) — UNVERIFIABLE — Claim asserts CACI NSS holds OASIS, CIO-SP3, and GSA MAS (GS-35F-349CA) with no `[s.xxx]` citations

The vehicle holdings claim is in v0.4 capture §5.4 as well, so this is load-bearing for the brief's "CACI NSS has the procurement path" argument.

**Proposed resolution:** Source-ground via USAspending or SAM.gov. The three vehicles can be confirmed by looking up each by contract number: GSA OASIS (governmentwide acquisition contract, multiple PIIDs per pool), NITAAC CIO-SP3 (`HHSN316201500006W` or similar), GSA MAS `GS-35F-349CA` (direct lookup). Either (a) ingest the three contract records from USAspending or SAM.gov and add the citations; or (b) reduce the FACT to whichever vehicle is actually visible in the existing CACI NSS AFRICOM record (parent IDV `GS00Q14OADU121` is part of OASIS — that confirms at least the OASIS holding).

**Operator decision:** _________________

---

## Operator workflow

1. Read each FACT entry and write `APPROVE` / `OVERRIDE: <text>` / `DEFER` on the **Operator decision** line.
2. Save the file.
3. Tell Claude "apply triage." Claude applies every APPROVE resolution, applies each OVERRIDE as specified, and leaves DEFER entries alone.
4. Claude re-runs `verify_facts.py` and surfaces the diff between the 2026-05-27 sweep and the post-triage sweep.

A v1.0 standard probably wants zero DEFER on FACTs that the briefs depend on, and explicit DEFER reasoning on any FACTs the briefs don't lean on. The §4 cluster (eight PARTIAL FACTs) is the most exposed because §4 is the brief's Competitive Landscape section.

# Monthly log — what was worked on each week

One entry per month. Update as you go. At month-end: note what was painful and what improved.

---

## 2026-05

**Focus opportunities:** PMTEC-USINDOPACOM (carried over from 2026-04); BDR-FLEET-READINESS (new)

**Week 1 (early May):**
- PMTEC carryover work — capture brief iterations toward v0.3.1 with cross-AI red-team passes
- Vault infrastructure: ingest pipeline maturation, named-entity audit script, grill-me skill
- BDR-FLEET-READINESS scaffolded — Navy ship-maintenance / fleet-readiness opportunity at SRF-JRMC

**Week 2-3 (mid May):**
- BDR-FLEET-READINESS source gathering and POC table
- BDR research file built through customer landscape, competitive landscape, and CACI fit assessment
- HM&E (Hull, Mechanical & Electrical) bridge-framing methodology developed for BDR

**Week 4 (late May):**
- BDR-FLEET-READINESS taken to v1.0 capture brief via verifier sweep, source-grounding, read-aloud pass, and Gemini-convergent red-team
- Final Gemini verdict on BDR: "Pass. Ready for BD-team review"
- Brief artifacts: capture-brief-v0.6 + executive-brief-v0.7

**Week 5 (end of May, into 2026-06):**
- Opportunity-seed-finder pipeline built — `_scripts/find_seeds.py`, `_scripts/approve_seeds.py`, three-source / four-pillar / three-layer architecture
- 12 rounds of out-of-scope closure-rule triage (88 seeds → 0 unmarked + 4 monitors)
- Discovered SAM.gov v2 search ignores most filter parameters; only `organizationName` works
- Pagination added to `lib/sam_gov.py`
- CACI capability book built — `_meta/caci-capability-book/` — five sessions plus FY26 Q3 refresh

**End-of-month notes:**
- **Painful:** SAM.gov v2 API documentation gaps caused weeks of wasted slice design — `ncode`/`ccode`/`q` are silently ignored. Empirical diagnostic was the only way to find this out.
- **Painful:** Cross-AI red-team (Gemini) compounded toward decisive pivots that nearly steered the capability-book project off-course. Feedback memory saved: treat red-team as input not directive.
- **Improved:** Section-by-section verifier discipline (small-ships workflow) shipped BDR-FLEET-READINESS at v1.0 quality in ~one week of focused work. The big-batch pattern from PMTEC v0.1→v0.3.1 was demonstrably more expensive.
- **Improved:** Auto-memory across sessions kept context coherent across multi-day work threads.
- **Infrastructure candidate:** None pressing. The slice-plan rewrite around `organizationName` is the active tactical work, not a new infrastructure need.

---

## 2026-06

**Focus opportunities:** TBD — pipeline-rebuild work (organizationName-anchored SAM.gov slices) is the active tactical thread carrying over from late May. Whether a new opportunity scaffolds this month depends on what the rebuilt pipeline surfaces.

**Week 1 (early June):**

**Week 2–3 (mid June):**

**Week 4 (late June):**

**End-of-month notes:**

---

## 2026-07

**Focus opportunity:** [TBD]

**Week 1 (triage):**

**Week 2–3 (research):**

**Week 4 (distill and ship):**

**End-of-month notes:**

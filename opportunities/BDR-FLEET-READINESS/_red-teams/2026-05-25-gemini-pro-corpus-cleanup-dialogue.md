---
type: red-team-dialogue
opportunity: BDR-FLEET-READINESS
scope: Pre-find_sources-pass corpus cleanup — identify and fix stale / inaccurate analytical content from prior sessions
drafting_model: Claude (Anthropic) proposing cleanup inventory
reviewing_model: Gemini Pro (Google)
rounds_completed: 2
date: 2026-05-25
---

# Iterated cross-AI red-team — corpus cleanup before next find_sources pass

## Why this dialogue exists

The operator instructed on 2026-05-25 that before running the next find_sources pass against the entities surfaced in yesterday's right-to-win-reframe dialogue (NETC, NAWCTSD, SWSC, NWDC, ATG, NCTE, RRL, STAVE, SMMTT, NSST), stale and inaccurate analytical content should be cleaned out of the existing corpus. The risk otherwise: the next pass would source-ground new claims on top of a foundation that the dialogues have already partly invalidated, creating analytical contradictions in the vault.

The cleanup itself goes through an iterated red-team dialogue to ensure (a) we identify what is actually stale rather than just what is uncomfortable, (b) the fix doesn't damage the analytical record (decision log lineage, scope-discipline disciplines), and (c) we don't propagate new unverified entities while cleaning out the old ones.

## Round 1 summary

Claude proposed an inventory of 13 items (A–M) covering §11.2 Carderock framing, §4 customer landscape, §5 competitive landscape, the acronym table, the per-opportunity SIMA glossary entry, §3 demand-signal framing, §11.1 engagement-paths inventory, §1 working summary, the SWARMEX "public-record anchor" framing, the Phoenix Group damage-control source weight, the Stimson MSMRO context-vs-load-bearing classification, §7 leg 5 entity treatment, and `_search-config.yaml`.

Gemini's Round 1 verdict: classify each item, surface missing stale items, prioritize before-pass vs after-pass, flag over-cleaning risks.

- **Concurred without adjustment:** B, D, F, G, I, J, K, M.
- **Adjustment proposed (b — right framing, wrong fix):** A (don't delete Carderock; re-scope as Doctrine/T&E origin point — see Pushback 1 below for Claude's counter on the specific re-scope), E (don't just remove SIMA overstatement; add invalidated-by breadcrumb), H (don't just add §1 pointer; actively rewrite Thread 4 to state the pivot — see Pushback 2 for Claude's counter), C (don't push shipbuilders to context only; re-label as Platform-Sustainment Bundling Hypothesis vs NAWCTSD Training-Prime Hypothesis).
- **Missing items surfaced by Gemini:** (1) LVC framing — anywhere the vault treats LVC as generic AR/VR, add scope note constraining to NCTE-compliant FST. (2) BDAR definition — the capability-gap framing (BDAR is the white space between Damage Control and Fleet Maintenance Activity / shipyards) should be added to the BDAR glossary entry.
- **Over-cleaning warnings:** don't delete the NAVSEA/industrial-base hypothesis entirely — preserve intellectual lineage via scope notes and `[Prior Hypothesis: X. Status: Invalidated by Y]` tagging in glossaries. Don't retroactively edit past decision-log entries.

## Round 2 — Claude's pushbacks and convergence

Claude pushed back on three of Gemini's Round 1 adjustments:

**Pushback 1 — Carderock re-scope language.** Gemini proposed labeling Carderock as "the Doctrine/T&E origin point" that "writes the BDAR doctrine." That overstates Carderock's role. Carderock's verified mission is ship-design Live Fire Test & Evaluation, survivability modeling, and structural mechanics. BDAR tactical doctrine is more plausibly NWDC's domain (Naval Tactics, Techniques, and Procedures — NTTPs). Claude proposed the §11.2 re-scope reflect a two-organization split: Carderock = survivability modeling source for scenario inputs; NWDC = BDAR doctrine writer.

**Gemini's Round 2 response — CONCEDED:** "you are absolutely right. I conflated the engineering/technical authority with the doctrinal authority." NSWCCD (Carderock) is the technical warrant holder for ship survivability and structural mechanics; NWDC writes NTTPs and tactical memorandums (TACMEMOs). The §11.2 re-scope adopts the two-organization split as Claude proposed.

**Pushback 2 — §1 working summary active rewrite vs. pivot-point-without-naming.** Gemini argued that §1 is the lens through which an LLM reads the rest of the vault during find_sources, so stale framing in §1 poisons the well. Claude agreed on the lens point but pushed back on the specific rewrite — Gemini's proposed Thread 4 rewrite ("Hypothesis pivoting from NAVSEA industrial-base demand to NETC/NAWCTSD training procurement") would introduce named entities (NETC, NAWCTSD) into the working summary BEFORE any ingested vault source has surfaced them, which is exactly the contamination pattern the named-contractor discipline at `_meta/feedback_named_contractor_discipline.md` prohibits. Claude proposed a "pivot-point-without-naming" rewrite that achieves the LLM-lens hygiene without committing to unverified entities.

**Gemini's Round 2 response — CONCEDED:** "I completely concede. You weaponized the _meta/feedback_named_contractor_discipline.md rules against my proposal perfectly." Hard-coding NETC and NAWCTSD into §1 before source ingestion creates a circular confirmation loop in which the find_sources pass treats them as established ground truth, blinding it to documents that might point elsewhere. Resolution: §1 Thread 4 rewrites to "research is at a pivot point — the prior NAVSEA / Carderock framing is being tested against an alternative training-systems procurement-chain hypothesis to be source-verified in the next find_sources pass" without naming the new entities.

**Pushback 3 — BDAR capability-gap framing labeling.** Gemini proposed adding the "BDAR is the white space between DC and FMA / shipyards" framing to the BDAR glossary entry. Claude agreed the framing is sharper than the current vault definition BUT noted this is Gemini's structural inference from the dialogue, not a source-grounded fact. Claude proposed adding the capability-gap framing with an explicit `[Structural Inference (Gemini Pro red-team, 2026-05-25) — Pending Source-Grounding]` tag.

**Gemini's Round 2 response — CONCEDED:** "I concede to the explicit labeling. The gap between Organizational-level Damage Control and Intermediate/Depot-level FMA / shipyards is the logical white space for BDAR, but we have not pulled an authoritative Navy document into the vault that explicitly defines BDAR using this exact taxonomy. Stating it as a bare fact is epistemologically dangerous. It is an LLM structural inference." If a future primary source confirms it, the tag comes off. If a source contradicts, the definition is updated.

## Convergence reached — final cleanup plan

Both sides converged. Cleanup plan organized into three execution blocks per Gemini's prioritization, with Claude's epistemic discipline corrections applied throughout.

### Block 1 — Must do before find_sources pass (the navigation instruments)

1. **M.** `_search-config.yaml` — add BDAR/BDAT-targeted queries for the verified-via-dialogue buyer triad (NETC, NAWCTSD, SWSC, NWDC, ATG, NCTE, RRL, STAVE, SMMTT, NSST). Remove the most off-scope shipbuilding queries. Add inline notes that the queries are testing hypotheses to be source-verified — not asserting the entities exist.

2. **H.** §1 working summary Thread 4 — rewrite to "pivot-point" framing without naming new entities. Make the find_sources lens neutral on the prior NAVSEA / Carderock framing vs. the alternative training-systems procurement chain.

3. **I.** §1 SWARMEX framing — soften from "public-record anchor" to "public-record signal," and note the press-release-vs-capability-building ambiguity surfaced in yesterday's dialogue.

4. **BDAR definition update (Missing Item 2).** Both the vault-wide glossary at `_meta/glossary.md` and the per-opportunity `_glossary.md` BDAR entries — add the capability-gap framing with the explicit `[Structural Inference (Gemini Pro red-team, 2026-05-25) — Pending Source-Grounding]` tag.

### Block 2 — Fast quarantines before find_sources pass (the guardrails)

5. **B.** §4 (Customer landscape) — add scope note: "Section drafted around the prior NAVSEA / Carderock framing; the dialogue on 2026-05-25 surfaced an alternative training-systems procurement-chain hypothesis to be source-verified in the next find_sources pass. See decision log entry 2026-05-25." Do not edit the FACT claims; only add the scope note.

6. **F.** §3 (Demand signal) — same scope note as B.

7. **G.** §11.1 (Engagement-surface inventory) — same scope note as B, plus a sentence noting that the engagement-paths target set is expected to broaden once the buyer triad is source-grounded.

8. **K.** §3.1, §4.5, §5.3 Stimson MSMRO citations — add explicit scope note that the Stimson material is context-level for the broader Pacific repair-capacity question, not load-bearing for BDAR/BDAT training procurement.

9. **L.** §7 leg 5 — refine the named-incumbents treatment. HII Mission Technologies is specifically the NCTE network architecture prime per Gemini's verified evidence. SAIC and Leidos remain canonical naval-services incumbents at the broader level — their specific BDAR-relevant contract footprints are not yet source-grounded.

10. **J.** Phoenix Group of Virginia damage-control training job posting — downgrade the citation weight in §7 leg 2 reasoning. Re-cite as evidence for "contractor base exists for damage-control-adjacent training" rather than "contractor procurement signal for BDAR/BDAT training." Distinguish DC (organic immediate response) from BDAR (assessment + repair after the immediate event).

11. **Missing Item 1.** LVC framing — add scope note in the acronym table at the top of 00_research-file.md and in §11.3 (BDAT training pipeline). LVC in vault context refers specifically to NCTE-compliant Fleet Synthetic Training architecture, not generic AR/VR or commercial gaming tech.

### Block 3 — Post-pass / lower priority (the deep cleans)

12. **A.** §11.2 (BDAR repair-side training pipeline) facility list — re-scope rather than delete. Carderock = ship-survivability modeling source for scenario inputs; NWDC = BDAR tactical doctrine writer (NTTPs, TACMEMOs); SWESC and Navy wet trainers (USS Buttercup, USS Trayer) = hands-on damage-control training venues. The two-organization split (Carderock + NWDC) replaces the single "Carderock as hands-on venue" framing.

13. **E.** SIMA per-opportunity glossary entry — rewrite to acknowledge SIMA is organic Navy training, with breadcrumb: `[Prior Hypothesis: SIMA as contractor entry point. Status: Invalidated by 2026-05-24 dialogue establishing SIMAs are Sailor training per Caudle's HASC testimony, not a contractor procurement signal.]`.

14. **C.** §5 (Competitive landscape) shipbuilders treatment — re-label the §5.1 shipbuilders as the "Platform-Sustainment Bundling Hypothesis" (BDAR training bundles into existing platform-sustainment contracts held by shipbuilders) versus the "NAWCTSD Training-Prime Hypothesis" (BDAR training procures separately through the training-systems chain). Both hypotheses are unverified; the next find_sources pass should test both.

### Over-cleaning safeguards (applied throughout)

- Decision log entries are append-only. Past entries are preserved as-is; updates land in the new 2026-05-25 entry below this dialogue file.
- The NAVSEA / industrial-base hypothesis is not deleted — preserved via scope notes that quarantine the framing but retain the analytical lineage.
- New entities surfaced in the dialogues (NETC, NAWCTSD, SWSC, etc.) are NOT yet added to analytical content as FACT claims. They appear only in search-config queries (testing-not-asserting), in the BDAR definition's structural-inference tag, in decision log narrative, and in this dialogue file. They become vault-citable only after a find_sources pass produces ingested primary sources naming them.

After execution of Blocks 1, 2, and 3, the corpus is ready for the next find_sources pass.

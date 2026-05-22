---
type: workflow
name: small-ships
purpose: Replace big-batch draft-then-red-team with verifier-first, section-by-section briefing
last_revised: 2026-05-22
---

# The small-ships workflow

This document describes how to draft a capture brief or executive brief one section at a time, verifying each section before writing the next one — instead of drafting the whole thing and then running verification and red-team at the end.

The technique is borrowed from test-driven development as applied to AI-assisted coding (Karpathy's "agentic engineering," Matt Pocock's "TDD skill," Anthropic's writer-reviewer pattern). The argument is that AI produces big batches of plausible-looking output that don't actually work, and the fix is small verified cycles instead. The Pragmatic Programmer's phrase is "outrunning your headlights" — feedback rate is your speed limit, and AI defaults to driving with the headlights off.

The pattern is documented separately from the SOP because it changes how briefs are built, not what the rules are. The verification rules at `_meta/verification-rules.md` are unchanged.

## The pattern in three sentences

For each section of a brief: first write the FACT claims that section needs to support, then run `verify_facts.py` against those claims and confirm the sources actually back them, then draft the prose, then red-team that one section. Move to the next section only when the current one is verified. The brief becomes a sequence of small verified ships rather than one big draft that gets attacked at the end.

## Why this replaces the current workflow

The PMTEC capture brief went through four revisions — v0.1 → red team → v0.2 → red team → v0.3 → red team → v0.3.1 — because each full-brief red-team pass surfaced problems that should have been caught earlier and instead required a full revision of the whole document. Each revision burned several hours of operator time and tens of thousands of tokens of AI quota.

The pattern that emerged from PMTEC is the big-batch pattern the Yanli Liu article warns against. The fix is to move verification and red-team **inside** the section loop, not outside the brief draft.

## The per-section loop

For each section of the brief, the loop is six steps. Each step is small and produces a checkable artifact.

**Step 1 — list the claims the section needs to make.** Before any prose, write out the specific factual claims the section will assert. Each claim gets the FACT, Assessment, or Speculation label up front. Each FACT gets a candidate citation tag pointing to a source already in `01_sources/`. The output of this step is a short markdown list, not a draft.

**Step 2 — run the verifier against the claim list.** Run `verify_facts.py` (or a targeted variant) against the claim list. The verifier reports which FACT claims are actually supported by the cited source, which are partially supported, which are unsupported, and which have no source ingested yet. If any FACT comes back unsupported or partially supported, fix it before drafting:
- Find a better source and ingest it, or
- Downgrade the claim from FACT to Assessment or Speculation with the correct label, or
- Cut the claim from the section entirely.

Do not draft prose around an unverified claim. The whole point of the small-ships pattern is to never write content the verifier has not blessed.

**Step 3 — draft the section prose.** Once the claim list has cleared the verifier, draft the prose for the section. The drafting model is whichever the SOP recommends for that section type — Claude for synthesis, Gemini for breadth (see SOP §5.1).

The prose must use only the claims from the verified list. New claims cannot be smuggled in during drafting. If during drafting it becomes clear a new claim is needed, stop drafting, go back to step 1, add the claim, and re-run the verifier.

**Step 4 — red-team the section.** Run the cross-AI red-team prompt at `_meta/prompts/cross-ai-red-team.md`, scoped to **this section only**, on the model the operator did not use for drafting. Three personas as usual — customer reviewer, competitor analyst, skeptical exec. The red-team output for a single section is small enough to address in minutes rather than hours.

**Step 5 — address findings or accept them.** For each red-team finding on this section, either fix it in the section, escalate it to the operator as a pending decision, or document why it is being accepted as-is. Findings the operator accepts get noted in the decision log so they do not resurface as "new" findings later.

**Step 6 — mark the section as a sealed ship and move on.** Add a brief sealed-state marker to the section header — a `<!-- ship: YYYY-MM-DD model-used -->` HTML comment is enough. Subsequent edits to a sealed section need to re-run the loop for that section. This prevents the operator from sleepwalking past previously-verified content during late-stage polish.

## How the brief gets assembled

After the last section is sealed, the brief draft already exists — it is the concatenation of the sealed sections. There is no separate "draft v0.1 of the full brief" step.

Two passes remain before the brief is shippable:

**Whole-brief consistency pass.** Read the assembled brief end-to-end. Check that section transitions are clean, that no claim is contradicted by another claim elsewhere, that the BLUF (Bottom Line Up Front) lines up with the body, and that the recommendation is supported by the FACTs that lead to it. Findings from this pass are usually small (transition wording, ordering tweaks, BLUF rewording) because the per-section verification has already caught the big problems.

**Distillation pass.** Derive the executive brief from the capture brief, per the SOP §5.5 prompt. The executive brief itself runs through the small-ships loop in miniature — each of its five sections (BLUF, why it matters, recommendation, risks, asks) gets its claim list, verifier check, and red-team before being assembled.

## What changes for the existing scripts

None of the existing scripts need to change to support this workflow. The relevant capabilities already exist:

- `verify_facts.py` can take a scoped claim list or a single-section path as input.
- `red_team.py` can take a single section or a paragraph block, not just a whole document.
- `refresh_brief_sources.py` works on the assembled brief at any time.

The change is **how the operator and Claude invoke these scripts**, not the scripts themselves. Per-section invocation is allowed today; we just have not been doing it.

That said — see the planned brief-builder consolidation in `_scripts/build_brief.py` (replacing the per-version scripts). The new module is being designed to support a `--section` flag from day one so the loop above can be driven from a single command.

## When NOT to use the small-ships pattern

The pattern adds overhead per section. For very short artifacts the overhead is bigger than the savings. Use straight drafting instead in these cases:

- One-page play cards. Treat the whole card as one "section" and run the loop once.
- Decision-log entries. They are not adversarial-review artifacts.
- Open-questions documents. Same.
- Source captures (`01_sources/*.md`). They are inputs to the loop, not outputs of it.

If a piece of work is shorter than three short paragraphs, do not run the small-ships loop on it — just draft and verify in place.

## How to know if this is working

After the first brief built this way (call it the pilot), look at three numbers:

- Total wall-clock time from "start drafting" to "shippable." Should drop versus PMTEC.
- Number of full-brief revisions (v0.1 → v0.2 → v0.3 → ...). Should drop to one or zero.
- AI quota burned by `verify_facts.py` and `red_team.py` over the full cycle. The article predicts this drops, because per-section verification is much smaller than per-brief verification.

If two of three numbers don't improve, the pattern is wrong for our scale and we revert. If all three improve, this becomes the default workflow and the SOP gets updated.

## First pilot

The next brief the operator drafts (whether for BDR-FLEET-READINESS once research resumes, or a return to PMTEC v0.4) is the pilot. Document the per-section loop timing and findings count in the relevant opportunity's decision log so we have data to compare against the PMTEC baseline.

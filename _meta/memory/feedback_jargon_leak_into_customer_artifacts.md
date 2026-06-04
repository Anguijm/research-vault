---
name: Synthesis-vault jargon must not leak into customer-facing artifacts
description: Internal compound nouns and self-referential phrasing built up across synthesis files must be translated to plain English before they reach exec summaries or briefs the customer reads
type: feedback
---

When working across daily-synthesis files, source files, and drafts, I tend to compress recurring themes into compound nouns and bureaucratic phrasings — "workforce-civilian-ratchet concern," "acquisition-sustainment feedback gap," "spec-track divergence," "structural fix," "operator-team-adjacent," "Pacific footprint." Inside the synthesis files this is a useful shorthand. Inside customer-facing artifacts (exec summaries, briefs the customer reads, anything that leaves the vault) this same vocabulary is unreadable jargon — the customer doesn't know the upstream context that gives the compound noun its meaning.

**Why:** The operator (J. Anguiano) called this out on 2026-06-04 reading the SRF-JRMC exec summary v0.1: "What the fuck are you trying to say with a sentence? It doesn't make sense. Fucking dumb it down." The specific sentence was "Lattner explicitly engaged the workforce-civilian-ratchet concern Andrew Sheets (Marine Corps) and Ian Shannon (Navy aviation) raised on Day 1 — the program is committed to maintaining sailor ownership of the ship alongside contractor support." The operator flagged it as "just one example of a bunch of things in this paper." The pattern is jargon-leak from synthesis into customer artifact.

**How to apply:**

1. **In synthesis files** (`02_daily-synthesis/`, source files, internal notes), compound nouns and shorthand are fine — they are working tools for me.

2. **In customer-facing drafts** (`03_drafts/` exec summaries, briefs marked for the customer or for leadership outside the project): every compound noun gets one of two treatments:
   - Replaced with a sentence that explains the thing in plain English.
   - If the compound noun must be used (it is a well-known program name or term), it must be defined on first use in the same paragraph.

3. **Bureaucratic verbs are a tell.** "Engaged the concern," "framed the response," "articulated the position," "surfaced the pattern," "positioned the construct" — these are signals I am hiding meaning behind structure. Replace with: "brought up," "said," "mentioned," "told the audience."

4. **Self-references break the cold-read.** "The concern X and Y raised on Day 1" — the customer doesn't have Day 1 in their head. Either name the concern in plain English, or cut the self-reference. Same rule for "per clip 7" / "[Source: mr26-clip7.]" — fine in synthesis, but exec summaries can route citations to the trip-report folder rather than into the prose.

5. **The cold-read test.** Before declaring a customer-facing draft done: read the first paragraph as if I had never seen the upstream synthesis. If any sentence requires the synthesis context to parse, rewrite it.

6. **Both directions on the gray box.** The operator owns the strategic decisions and the FACT calls. Tactical drafting is mine — and drafting includes making the prose actually readable for the audience. A first draft that is dense with synthesis-vocabulary is not a finished tactical product; it is half-done. Finish it.

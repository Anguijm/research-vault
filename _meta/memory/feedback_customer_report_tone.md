---
name: Customer-facing report tone — neutral, no self-congratulation, no contractor-government tension framing
description: Three anti-patterns to avoid in customer-facing trip reports and similar deliverables: framing contractor-government relationships as "tension," self-congratulatory language about having captured information, and punting analyst work to the customer as open follow-ups
type: feedback
---

When writing customer-facing trip reports, exec summaries, or similar deliverables, avoid three specific anti-patterns the operator flagged on 2026-06-05:

## 1. Don't frame contractor-government relationships as "tension"

I had written that the Day-1 Sheets/Shannon observation about "as contractors do more preservation work, sailors stop learning the trade" and Lattner's Day-2 response were an "honest tension" or "sailor-vs-contractor tension." Operator's correction: it isn't tension. Both sides made statements of operational reality.

- Sheets/Shannon: once contractors take on the work, it's hard to give it back to sailors because sailors stop learning.
- Lattner: the program structures SWARM Teams to work alongside sailors rather than take work over.

That's not tension or friction — it's two true statements about how the work actually flows. Calling it "tension" puts a negative cast on contractor relationships with the government, which is the wrong tone for a customer-facing report and especially wrong for a report on an industry event.

**Operator's exact words (2026-06-05):** *"I don't want to ever represent contractors as a point of tension with the government, especially at an industry event like this."*

Also drop emotionally charged phrasings like Ian Shannon's "we call it crack" line, even though it's a real on-tape quote. The principle: report neutral structural observations, not the moments that read as friction.

## 2. Don't be self-congratulatory about having information

I had written "I have direct names and emails:" before listing the Anti-Rust Program POCs. Operator's correction: that's self-congratulatory. Just present the contacts.

The pattern shows up in several flavors I should watch for:

- "I have direct names and emails: ..."
- "I was able to capture ..."
- "I came away with ..."
- "Notably, I noted ..."
- Any prose that brags about having the information rather than just presenting it.

Just present the facts. The reader doesn't need to know I'm proud of having captured them.

## 3. Don't punt analyst work to the customer as "open follow-ups"

I had left items in the "Still open from the trip" section that were essentially analyst tasks — e.g., "Whether NDAA §345 shows up explicitly in SURFMEPP, ST-1, Anti-Rust Program, or SIMA contract documentation — searchable via USASpending or contract-award text when records refresh." Operator's correction: *"Why don't you just go do that? Why are you telling me to go do that?"*

Customer-facing open-follow-up items should be things only the customer can resolve (internal SRF questions, decisions only the customer can make). Things the analyst can do should be either:

- **Actually done** before delivering the report (and the result reported), or
- **Listed as analyst action items** (clearly the analyst's responsibility, not punted to the customer), or
- **Dropped entirely** if they aren't actionable yet.

Don't leave "search USASpending for X" or "look up Y in Z database" as customer punchlist items. That's the analyst's job.

Also: don't leave low-value identification questions in the customer report. The operator's example: *"Nobody gives a fuck about Pat McDermott. Pat McDermott does not even need to be mentioned in this. I don't need to figure out who they are."* If a name comes up in a session but doesn't have customer-side relevance, drop it from the customer-facing artifact. Keep it in synthesis notes if it might matter later.

## 4. Don't telegraph that the event was recorded

I had phrasings like "Robinson said on tape," "Tenopir said on tape," "Cost data on tape:", "spoken, not on the slide," "name not on tape," "Ingle clarified this on tape," "Matt Chu cited X on tape" — all of which tell the reader that I have an audio recording of the conference.

Operator's correction (2026-06-05): *"Fucking nobody needs to know there's an audio recording of this event. If asked, I'll produce it. If asked face-to-face, I'll tell them, but I don't need to put it in my report that 'oh, they said it on tape.' My credibility is not enough. I have to say that 'oh, I have it on tape'? That's a silly way to represent yourself."*

The operator's credibility as an analyst stands on its own. Direct quotes don't need the qualifier — just attribute the quote to the speaker. Specifically:

- "Robinson said on tape:" → "Robinson said:" (or just "Robinson:")
- "Cost data on tape:" → "Cost data from his slides:" (slides are public materials; OK to reference)
- "spoken, not on the slide" → drop the qualifier; just present the content
- "name not on tape" → "name not captured" or rework to drop the medium reference
- "Ingle clarified this on tape" → "Ingle clarified this"
- "Speakers didn't cite §345 on tape" → "Speakers didn't invoke the statute by name" / "no speaker named §345 in their session"
- Audio timecode references like "around 52:39" → drop entirely; just reference the session

**Distinction:** referencing slides ("from his slides," "his slide listed...", "Foley's Composite Work Cell Concept slide") is fine — slides are public materials marked Distribution A: Approved for Public Release. Referencing the audio recording is the part that reads as self-congratulatory credibility-padding.

## 5. Don't make false negative claims based on incomplete sources

I had written "no speaker cited §345 by name in their sessions" / "I brought it into the trip as pre-trip policy context" in multiple reports. Operator correction (2026-06-05): false. Conlan Hsu (NSRP) cited §345 at the opening of the Day-1 NSRP SPC panel meeting — operator was there in person but did not record that opening portion of the meeting.

The lesson: don't claim "no one mentioned X" just because X isn't in my recorded sources. The operator was at the conference in person and heard things I didn't capture. My sources are recorded audio + slide photos; the operator's sources include everything they witnessed live.

**How to apply:**

- Avoid negative claims about what was said at the conference unless I can affirmatively verify them. Phrasings like "no speaker cited X," "no one mentioned Y," "X wasn't discussed" are all risky.
- If I want to say something about §345 (or any other policy context) being unattributed in my sources, frame it positively: "I had also brought §345 into the trip as pre-trip context." Don't claim no one else mentioned it.
- When I want to flag that something is operator-supplied context, just say that. Don't try to bound it by claiming no one at the conference touched on it.
- For unrecorded portions of the conference (Day-1 SPC panel opening, hallway conversations, etc.), the operator's first-person knowledge is the source. If they tell me Conlan Hsu cited §345, that's the FACT — not the absence of it in my audio.

This applies broadly to any conference, trip report, or interview-based work where I have a partial recording. Recorded sources are a subset of what happened.

## How to apply across the workflow

- **Synthesis files (`02_daily-synthesis/`):** all of these anti-patterns are OK in synthesis. Self-references, tension framing, every named person, "on tape" qualifiers — synthesis is internal notes, not customer-facing. False negative claims about what was said are NOT OK even in synthesis — those are FACT errors, not tone issues, and they propagate downstream.
- **Customer-facing drafts (`03_drafts/`):** strip all five. Neutral, no self-congratulation, no punted work, no irrelevant names, no recording-implication phrasings, no false negative claims about conference content.
- **Source files (`01_sources/`):** quote speakers verbatim including their tension/emotional language (it's FACT-of-speech), and recording-implication phrasings are fine since these are working transcripts. Don't carry those quotes or phrasings into customer artifacts unless they're useful.

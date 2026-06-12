---
type: trip-report-structured
event: # match the event README frontmatter `event`
event_dates: # YYYY-MM-DD to YYYY-MM-DD (omit if not discernible)
location: # city, venue (omit if not mentioned)
audience: agnostic-base
status: draft
created: # YYYY-MM-DD
sources: # e.g. "2 audio clips — see source-ledger.md"
---
<!-- STRUCTURED TRIP REPORT (audience-agnostic base).
     Lives in trip-reports/<EVENT>/02_synthesis/ (or 02_daily-synthesis/). The
     audience-specific 03_drafts/ artifacts (CACI exec/full, SRF exec/full) DERIVE from
     this by selection/re-emphasis; do not re-extract quotes for them.

     PROVENANCE (non-negotiable):
     - Every cite is [<ledger-slug> @ mm:ss]. <ledger-slug> is a tag in this event's
       source-ledger.md (e.g. s.clip1, mr26-clip5-...). mm:ss MUST match a real line
       in the matching transcript: `**[mm:ss] [Speaker]** text` in <clip>.transcript.named.md,
       or `**[mm:ss → mm:ss]** text` in <clip>.transcript.md when un-diarized. "Click
       every link" = the cite resolves in two hops (slug -> ledger row -> transcript line).
     - LABELS: Key claims = FACT-of-speech (someone said it on the recording) + a cite,
       NO analyst inference. TL;DR, Affect signals, Cross-cutting themes, the per-session
       Assessment line, and Confidence notes = Assessment (labeled). A speaker saying
       something is FACT-of-speech, not FACT-of-truth unless independently verified.
     - QUOTES: verbatim only, copied from the transcript (never re-typed from memory),
       ≤3 per session. If the transcript reads `[transcript uncertain]` or the audio is
       unclear, skip the quote — never guess.
     - SPEAKERS: carry the transcript's confidence exactly. Use the named transcript's
       legend: confirmed names as-is; blended/unconfirmed as e.g. "[S1 ≈ Fjeld,
       unconfirmed]" or "[S?]". NEVER upgrade a blended/unconfirmed S-id to a clean name.
     - Slide / corroboration fields are deferred to P2 (see _meta/trip-report-workflow.md);
       keep them as labeled stubs this phase. Omit any Date/Location field you cannot source.
     - Density over volume: cut anything a busy reader would skim. -->

# Trip report — <event title>

**Date:** <YYYY-MM-DD or range, omit if unknown> · **Location:** <venue, omit if unknown> · **Sources:** <N audio clip(s) — see `source-ledger.md`>

## TL;DR
<!-- Assessment. 3–5 bullets. Each = ONE non-obvious takeaway, NOT a topic header
     ("the panel discussed X" is banned). Each traces to >=1 session cite. -->
- <non-obvious takeaway> — _Assessment_ ([<slug> @ mm:ss])

## Sessions
<!-- One ### block per distinct talk/segment. One clip may split into several blocks;
     several clips covering one talk merge into one block. -->

### <session / talk title>
- **Speakers:** <confirmed names as-is; carry uncertainty, e.g. "[S1 ≈ Fjeld, unconfirmed]", "[S?]">
- **Coverage:** mm:ss–mm:ss in <slug>
- **Key claims:** <!-- FACT-of-speech. 3–7 bullets, each ends with a cite. No analyst inference here. -->
  - <claim> ([<slug> @ mm:ss])
- **Quotes:** <!-- verbatim, ≤3, copied from the transcript; pick emotional weight / quotable density -->
  > "<verbatim>" — <Speaker> ([<slug> @ mm:ss])
- **Slides referenced:** _deferred to P2 (Gemini-vision OCR of slide images, cross-checked vs transcript)_
- **Affect signals:** _Assessment:_ <where confident vs hedging vs deflecting, with cite; or "none notable">
- **Assessment:** <optional analyst read on this session, labeled; omit if nothing to add>

## Cross-cutting themes
<!-- Assessment. 2–4 patterns recurring across sessions. Each names the sessions it spans. -->
- **<theme>:** <synthesis> ([<slug> @ mm:ss], [<slug> @ mm:ss])

## Action items
<!-- Concrete next steps for the attendee. No vague "explore further". -->
- [ ] <action> — <provenance: [<slug> @ mm:ss] (slide # in P2)>

## Open questions
<!-- Carry from each 01_sources "Open questions"; include speaker-attribution and acronym uncertainty. One sentence each. -->
- <question the talks raised but did not answer>

## Confidence notes
<!-- Assessment paragraph(s). This phase is audio-only (no slide processing yet). -->
- **Corroboration:** audio-only this phase — claims rest on the local named transcript(s); slide cross-referencing deferred to P2.
- **ASR / attribution caveats:** <diarization confidence; blended/unconfirmed speakers from the named-transcript legend; notable ASR artifacts, e.g. mis-transcribed names/acronyms>.
- **Conflicts & resolution:** <claim-vs-claim disagreements and how resolved; or "none flagged">.

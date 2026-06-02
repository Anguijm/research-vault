---
type: trip-report-folder
event: MegaRust 2026
event_name_full: "MegaRust 2026 — sponsored by the American Society of Naval Engineers (ASNE)"
location: Marriott Mission Valley, San Diego, CA
operator: John Anguiano
attended_in_person: true
event_dates: 2026-06-02 to 2026-06-04
created: 2026-06-03
focus_panel: "NSRP SPC Panel Meeting — 8:00 AM-12:00 PM Tuesday June 2, Coastline Ballroom; led by Conlan Hsu and Angel Zepeda (NSRP)"
note_on_panel_acronym: "Operator initially said 'SCP'; the agenda labels it 'SPC' (Surface Preparation and Coatings). Aligned to SPC per the agenda. If NSRP uses a different official name, flag it."
audiences:
  - CACI internal leadership (BD bent)
  - SRF-JRMC customer leadership (intel + engagement bent)
deliverables:
  - CACI executive summary (2 pages)
  - CACI full trip report (5-15 pages, BD-flavored synthesis)
  - SRF-JRMC executive summary (2 pages)
  - SRF-JRMC full trip report (5-15 pages, raw-notes + recommendations)
---

# MegaRust 2026 — Trip Report Working Folder

This folder is the working set for the operator's MegaRust 2026 trip report. MegaRust is the annual industry-attended conference focused on ship corrosion / preservation; the operator is attending in person and capturing audio of the NSRP Surface Preparation & Coatings (SCP) panel sessions.

This is **not an opportunity folder.** No gate, no capture brief, no FAR 9.5 OCI processing. The folder structure is adapted from the opportunity-folder pattern but slimmed down because the artifact set is different (trip reports, not capture briefs) and the audience structure is different (two audiences, four artifacts).

## Layout

```
trip-reports/MEGARUST-2026/
  README.md                       — this file
  source-ledger.md                — citation index (every claim in any artifact references an entry here)
  _decisions.md                   — design/scope decisions for this trip
  audio/                          — raw M4A clips the operator dropped from the conference
  01_sources/                     — per-session transcripts, FACT/Assessment/Speculation labeled
  02_daily-synthesis/             — end-of-day rollups (Day 1, Day 2, Day 3)
  03_drafts/                      — working drafts of the four output artifacts:
                                      caci-exec-summary.md
                                      caci-full-report.md
                                      srf-exec-summary.md
                                      srf-full-report.md
```

## Workflow

1. **Audio comes in.** Operator drops M4A clips into `audio/`. Each clip is one session — typically 10 minutes to an hour.
2. **Transcribe per-session.** Each clip → a markdown source file in `01_sources/` named `<YYYY-MM-DD>_<session-slug>.md`. Format follows the per-session template (see below).
3. **Cross-reference inline during transcription.** As panelists name programs / NAICS / companies / customer orgs / CACI capability areas, the source file flags the cross-reference (e.g., "panelist mentioned NSRP SCP work on X — maps to capability area Y in `_meta/caci-capability-book/`"). This is what makes the trip report capture-relevant rather than just notes.
4. **Daily synthesis at end of day.** Pull the day's sources into a `02_daily-synthesis/day-N.md` file. Don't wait until Day 3 to start writing.
5. **Final artifacts after Day 3.** Use the daily syntheses to populate the four drafts in `03_drafts/`. The two CACI artifacts are BD-flavored (mostly intelligence-for-capture, some strategic synthesis). The two SRF artifacts are raw-notes-plus-recommendations.

## Source-file template (for `01_sources/`)

Every per-session source file should carry frontmatter with:

```yaml
---
type: trip-report-source
event: MegaRust 2026
day: 1 / 2 / 3
session_name: <verbatim title from the agenda>
session_type: panel / keynote / breakout / other
session_date_local: <YYYY-MM-DD>
session_time_local: <HH:MM-HH:MM>
panelists:
  - name: <Name, role, affiliation as introduced>
audio_clip: <filename in audio/>
transcribed: <YYYY-MM-DD>
transcription_method: <gemini-audio | whisper-local | manual | other>
---
```

Body sections:

- **Summary** — one-paragraph plain-English summary of the session (what was discussed, by whom, what stood out)
- **FACT — quoted material** — direct quotes from panelists, attributed by name, with timestamps if useful
- **FACT — paraphrased content** — what was said, paraphrased
- **Assessment — analyst observations** — operator's read on what was said
- **Cross-references** — explicit links to capability-book areas, opportunity-screening signals, prior vault content
- **Open questions** — what wasn't resolved or what to follow up on

The FACT/Assessment/Speculation labeling discipline applies. Speakers' claims are FACT-of-speech (they said it) but not FACT-of-truth unless independently verified.

## Audience-specific synthesis notes

**CACI internal version (mostly B with a little C):**
- Lead with the BD-relevant signals: customer programs mentioned, procurement vehicles named, competitor activity, capability adjacencies.
- Map each significant item back to the CACI capability book + the operator-team layer.
- Include a "what to watch / what to pursue" section for the BD team.

**SRF-JRMC customer version (mostly A with recommendations):**
- Lead with what was said. Less interpretation, more reporting.
- Treat the panel content as intel the SRF leadership may not have heard themselves.
- Include "how CACI can support continued engagement" — relationship-building recommendations, not capture-bid recommendations.

## Discipline

- OSI-only. If anything in the audio is FOUO / restricted / off-the-record, the operator flags it before transcription and we exclude it from the source ledger.
- Named-entity discipline applies; entities surface only via the ingested audio source, not extrapolation.
- All claims in any artifact cite a source-ledger entry.
- FACT/Assessment/Speculation labels are non-negotiable.

## Future codification

After this trip, if the workflow proves out, codify the pattern as a skill at `_meta/trip-report-workflow.md` so the next trip starts faster. Don't codify yet — wait to see what actually works.

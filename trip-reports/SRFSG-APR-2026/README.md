---
type: trip-report-folder
event: CACI SRFSG Annual Program Review 2026
event_name_full: "CACI SRFSG Annual Program Review 2026"
note_on_acronym: "SRFSG = the CACI program/group for SRF support work (the operator's SRF-JRMC support program). Full expansion not yet confirmed verbatim — flag if a source spells it out."
location: "PENDING — confirm"
operator: John Anguiano
attended_in_person: true
event_dates: 2026-06-08
created: 2026-06-08
sensitivity: osi                 # operator-confirmed 2026-06-08: non-sensitive / OSI, treat like MegaRust
audiences:
  - CACI internal leadership (BD bent)
deliverables:
  - CACI executive summary (2 pages)
  - CACI full trip report (5-15 pages, BD-flavored synthesis)
status: scaffold — capture-ready; event = CACI SRFSG Annual Program Review 2026; location still pending
---

# CACI SRFSG Annual Program Review 2026 — Trip Report Working Folder

Working set for the operator's trip report out of a CACI program review attended
2026-06-08. Capture mechanics mirror `trip-reports/MEGARUST-2026/` (audio clips →
per-session transcripts → synthesis → drafts), extended to take in **photos** as
well as audio. This is **not** an opportunity folder — no gate, no capture brief.

## Sensitivity

**Operator-confirmed 2026-06-08: this review is non-sensitive / OSI** — treat like
MegaRust. Audience for the artifacts is CACI internal leadership (BD bent).

Standing discipline still applies: this vault is OSI-only (no CUI, classified, or
proprietary-restricted content; see `CLAUDE.md`, `_handoff/HANDOFF.md` §11). If any
individual session turns out to be CUI / FOUO / restricted / off-the-record, flag it
before transcription and we exclude it from the source ledger and artifacts.

## Layout

```
trip-reports/CACI-PROGRAM-REVIEW-2026-06-08/
  README.md            — this file
  source-ledger.md     — citation index (every claim in any artifact cites an entry)
  _decisions.md        — open scope/sensitivity decisions for this trip
  audio/               — raw M4A clips the operator drops from the review
  photos/              — photos (slides, whiteboards, displays) — drop image files here
  01_sources/          — per-session transcripts + photo notes, FACT/Assessment labeled
  02_synthesis/        — rollup synthesis
  03_drafts/           — working draft(s) of the trip report
```

## Intake workflow

1. **Audio in.** Drop M4A clips into `audio/`. One clip ≈ one session/topic.
2. **Photos in.** Drop images into `photos/`. Name or note which session/slide each belongs to (a `photos/<session-slug>/` subfolder per session works, as MegaRust did with `slides/`).
3. **Transcribe per session.** Each clip → a markdown source file in `01_sources/` named `2026-06-08_<session-slug>.md`, using the per-session template below. Photos are referenced from the relevant source file (filename + one-line caption of what the slide showed).
4. **Synthesis.** Roll the day's sources into `02_synthesis/`.
5. **Draft.** Populate the trip report draft(s) in `03_drafts/` from the synthesis.

## Per-session source template (`01_sources/`)

```yaml
---
type: trip-report-source
event: CACI SRFSG Annual Program Review 2026
session_name: <session/topic title>
session_type: brief / discussion / demo / other
session_date_local: 2026-06-08
session_time_local: <HH:MM-HH:MM>
presenters:
  - name: <Name, role, org as introduced>
audio_clip: <filename in audio/>
photos:
  - <filename in photos/ + one-line caption>
transcribed: 2026-06-08
transcription_method: <whisper-local | gemini-audio | manual>
sensitivity: internal
---
```

Body: **Summary** · **FACT — quoted** · **FACT — paraphrased** · **Assessment** ·
**Cross-references** (capability book / opportunities / prior vault content) ·
**Open questions**.

## Discipline

- INTERNAL posture (above). No CUI/classified/proprietary-restricted content.
- Named-entity discipline: entities surface only via the captured audio/photos, not extrapolation.
- Every claim in any artifact cites a `source-ledger.md` entry.
- FACT (-of-speech) / Assessment / Speculation labels are non-negotiable; a speaker saying something is FACT-of-speech, not FACT-of-truth unless verified.

## Still pending (see `_decisions.md`)

Resolved 2026-06-08: sensitivity = non-sensitive/OSI; output = CACI exec summary + CACI full report.

Still open:
- **Location** — where the review is held (the only remaining identity field). Folder renamed to `SRFSG-APR-2026` (APR = Annual Program Review).

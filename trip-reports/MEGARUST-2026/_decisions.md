---
type: decision-log
event: MegaRust 2026
created: 2026-06-03
---

# Decision log — MegaRust 2026 trip report

## 2026-06-03 — Trip-report construct scaffolded

The operator is attending MegaRust 2026 in person and capturing audio of the NSRP Surface Preparation & Coatings (SCP) panel sessions. The trip report will be the output. This is a new construct in the vault; no prior trip reports have been done through this infrastructure.

**Decisions:**

- **Folder location:** `trip-reports/MEGARUST-2026/` at the vault root. Not under `opportunities/` (this is not an opportunity) and not under `_meta/` (this is content, not infrastructure). Future trips get sibling folders under `trip-reports/`.
- **Two audiences, four artifacts:**
  - CACI internal leadership — 2-page executive summary + 5-15 page full report. BD-flavored synthesis (mostly intelligence-for-capture, some strategic synthesis).
  - SRF-JRMC customer leadership — 2-page executive summary + 5-15 page full report. Mostly raw notes + recommendations for continued engagement.
- **Source structure:** per-session transcripts in `01_sources/`, with FACT/Assessment/Speculation labels and inline cross-references to the capability book + opportunity-screening signals during transcription, not after.
- **Daily synthesis cadence:** end of each conference day, pull sources into `02_daily-synthesis/day-N.md`. Don't wait until Day 3 to start writing.
- **Audio transcription approach:** undecided at scaffold time. Operator dropped responsibility on Claude. First clip will determine the approach — try Gemini's audio-capable analysis first; fall back to local Whisper or other tools if needed.
- **Codification deferred:** the workflow may become a vault skill at `_meta/trip-report-workflow.md` after this trip, if the pattern proves out. Not codifying yet.

**Open items at scaffold time:**

- Audio transcription mechanism — test with first clip
- Whether to wire any of this through the existing `build_brief.py` for .docx output if formal formatting is needed for distribution
- Whether to add an SRF-JRMC-specific entity allowlist for this trip if many SRF / NSRP / coatings-industry entities surface (named-entity discipline applies)

---

## 2026-06-12 — Trip-report workflow codified

The trip-report pattern (run ad-hoc for MegaRust and SRFSG) is now codified at
`_meta/trip-report-workflow.md`, with a reusable structured-report template at
`_templates/trip-report.md`. The template adopts the disciplined section structure
evaluated from an external proposal — TL;DR as non-obvious takeaways, per-session blocks
with cited claims + verbatim quotes + affect signals, cross-cutting themes, action items
with provenance, confidence notes — adapted to the vault's provenance: cites are
`[<ledger-slug> @ mm:ss]` resolving to the local `.transcript.named.md`; Key claims are
FACT-of-speech, interpretive sections are labeled Assessment; quotes are verbatim from the
local transcript. The structured report sits in `02_synthesis/` as the audience-agnostic
base from which the `03_drafts/` audience artifacts derive.

**Engine unchanged:** local faster-whisper + pyannote stays the default; no capture audio
goes to the cloud. Two future phases are decided but NOT built — P2 slide OCR via Gemini
vision (slide images only, never audio); P3 an optional sensitivity-gated Gemini audio
fast-path for public events only, with the local pipeline as the default.

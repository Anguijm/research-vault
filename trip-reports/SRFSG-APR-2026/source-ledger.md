# CACI SRFSG Annual Program Review 2026 — Source ledger

Citation index. Every claim in any synthesis or draft cites an entry here. One
entry per captured source (audio clip / photo set). Populated as sources are
transcribed into `01_sources/`.

| Tag | Source (audio clip / photos) | Session | Captured | Notes |
|---|---|---|---|---|
**Chronological order (operator-corrected 2026-06-08): clip 2 = MORNING (first); clip 1 = AFTERNOON (after lunch).** Filenames kept as-is for Drive provenance.

| s.clip2 | `audio/2026-06-08_srfsg_clip2.mp3` (Drive id 1ysuprMgVwgCyFmyFwFHCo9tZsu9PcxG3; 40.9MB; 2:50:06) — **MORNING / Part 1** | downtime → team-building → "glue"-leader brief → senior-officer contingency/operational-readiness brief → IDIQ-strategy discussion → `01_sources/2026-06-08_clip2-day1-teambuilding-and-big-rocks.md` | 2026-06-08 | The substantive core; source file needs full rebuild + speakers |
| s.clip1 | `audio/2026-06-08_srfsg_clip1.mp3` (Drive id 1ZcY-faepRMv82ZGhuSZd6Py51S8I5g4d; 27.4MB; 1:54:10) — **AFTERNOON / Part 2** | project-team-training program brief + team-building + Day-2 planning → `01_sources/2026-06-08_clip1-day1-program-brief-and-teambuilding.md` | 2026-06-08 | Speakers/acronyms flagged for operator review |

**Provenance:** pulled from the operator's Drive folder `1GHQoutXzvkurOlPnoNfir6yGfhSYxcLD`
via gdown (2026-06-08); no phantom/0-byte files this time. The Drive MP3s were "MPEG
ADTS" with non-standard framing that faster-whisper mis-read as ~10s, so they were
normalized to 16 kHz mono WAV via ffmpeg before transcribing (a few seconds of glitchy
frames dropped: ~6850s vs 6860s). WAVs are transient (removed after transcription);
MP3 originals retained.

---
type: source-ledger
event: MegaRust 2026
created: 2026-06-03
purpose: Citation index for every claim in any MegaRust 2026 trip-report artifact.
---

# Source ledger — MegaRust 2026

Every fact, quote, or assessment in any artifact under `trip-reports/MEGARUST-2026/` must reference an entry below. Add entries as audio clips are ingested.

## Citation format

```
### <citation-slug>

- Audio file: <filename in audio/>
- Session: <verbatim session title>
- Date / time (local): <YYYY-MM-DD HH:MM-HH:MM>
- Panelists / speakers: <names + affiliations>
- Transcription method: <gemini-audio | whisper-local | manual>
- Transcribed: <YYYY-MM-DD>
- Source file: <01_sources/...md>
- Notes: <caveats — audio quality, partial coverage, off-the-record exclusions>
```

## Sources

### mr26-clip1-laser-ablation-impl-2026-06-02

- Audio file: 80b4803b-Voice_260602_101029.m4a
- Session: NSRP SPC Panel Meeting — Laser Ablation Shipyard Implementation Presentation
- Date / time (local): 2026-06-02 10:10–10:21 (approximate)
- Panelists / speakers: NSRP SPC Panel led by Conlan Hsu and Angel Zepeda (NSRP). Presenter unidentified in this clip. Q&A participants: Conlan Hsu, John McRory (virtual).
- Transcription method: faster-whisper, medium.en model, local CPU
- Transcribed: 2026-06-03
- Source file: `01_sources/2026-06-02_clip1-laser-ablation-shipyard-implementation.md`
- Notes: 10:33 audio, 62 segments, clean transcription. Minor artifacts (e.g., "bare steel" → "Bear Steel", "MIL-PRF-23236" → "2-3-2-3-6", "disbondment" → "despondment") noted in the source file's FACT-quoted section.

### mr26-clip2-1k-polysiloxane-2026-06-02

- Audio file: 9fa50ed7-Voice_260602_102216.m4a
- Session: NSRP SPC Panel Meeting — 1K Polysiloxane Oxal-Free Coatings Viability Study Presentation
- Date / time (local): 2026-06-02 10:22–10:37 (approximate)
- Panelists / speakers: NSRP SPC Panel led by Conlan Hsu and Angel Zepeda (NSRP). Presenter: Eric (Elzly Technology, likely). Q&A participants: Glenn (NCP Coatings, likely); one questioner referenced as "Coach" — possible Whisper artifact for "Conlon" (Conlan Hsu).
- Transcription method: faster-whisper, medium.en model, local CPU
- Transcribed: 2026-06-03
- Source file: `01_sources/2026-06-02_clip2-1k-polysiloxane-oxal-free-viability-study.md`
- Notes: 14:20 audio, 189 segments. Several transcription artifacts on technical terms (Whisper rendered "MIL-PRF-24635F" as "PRF24635F" and "middle 2, 4, 6, 3, 5, F-type, 5-com1"; "Elzly Technology" as "LZ Technology"; "NCP Coatings" as "MCP Codings"; "Mark Ingle" as "Mark Ingalls"). Chemical identity of "Oxal/Oxyl" — central project topic — is unresolved on tape and the most important verification item for the operator.

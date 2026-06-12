# Trip-report workflow

Codified 2026-06-12. Pairs with `_templates/trip-report.md` and the non-negotiable
`_meta/verification-rules.md`. This formalizes the trip-report process that was run
ad-hoc for MEGARUST-2026 and SRFSG-APR-2026 (the codification deferred in MEGARUST
`_decisions.md`).

A trip report turns raw field captures (audio clips, and later slide photos) into a
verifiable, audience-ready report. The discipline is the same as the rest of the vault:
every claim traces to a source, FACT/Assessment/Speculation is labeled, and nothing is
invented.

---

## 0. Scope and layering

One folder per event: `trip-reports/<EVENT>/`, containing `README.md`, `source-ledger.md`,
`_decisions.md`, `audio/`, `photos/`, `01_sources/`, `02_synthesis/` (or
`02_daily-synthesis/`), and `03_drafts/`.

The pipeline is a layered stack — each layer is derived from and cites the one below it:

```
audio/<clip>.mp3
  → <clip>.transcript.md            (local transcription — §1)
  → <clip>.transcript.diarized.md   (local diarization — §1)
  → <clip>.transcript.named.md      (speaker names — §1)  ← citable source of quotes/timestamps
  → 01_sources/<session>.md         (per-session source files, labeled — §2)
  → 02_synthesis/structured-report.md  (the structured report, audience-agnostic — §4)
  → 03_drafts/<audience>.md         (audience-specific drafts, DERIVED — §5)
```

The default capture engine (§1) is **100% local**. No capture audio leaves the machine
in the default path (local-first, OSI-only). See Future phases for the gated exceptions.

## 1. Local audio pipeline (default — unchanged)

Run under `~/.local/whisper-venv/bin/python3`:

1. **Transcribe** — `_scripts/transcribe_audio.py <clip>.mp3` (faster-whisper, local GPU)
   → `<clip>.transcript.md`, lines `**[mm:ss → mm:ss]** text`.
2. **Diarize** — `_scripts/diarize_pyannote_unified.py` (or `_chunked.py` for a single clip;
   pyannote + ECAPA, local GPU) → `<clip>.transcript.diarized.md`, lines `**[mm:ss] [S#]** text`.
   Use the **unified** variant when several clips share one speaker set (one S-id = one
   person across clips).
3. **Name speakers** — voiceprint match / operator confirmation, then
   `_scripts/apply_speaker_names.py` → `<clip>.transcript.named.md`, lines
   `**[mm:ss] [Name or S#]** text`, with a header legend marking confirmed vs blended/
   unconfirmed speakers. **This named transcript is the citable source of every quote and
   timestamp.** Keep the `.diarized.md` (S-tagged) alongside as the raw record.

If diarization is skipped, the `.transcript.md` is the citable source and speakers are
"un-diarized — attributions unreliable."

## 2. Per-session source files (`01_sources/`)

One markdown file per session/clip, using the source-file template (see an event README's
"source-file template"): frontmatter (event, session, speakers, audio_clip,
transcription_method, …) + **Summary** + **FACT — quoted** + **FACT — paraphrased** +
**Assessment** + **Cross-references** (capability book / opportunities / prior vault content)
+ **Open questions**. Label FACT-of-speech vs FACT-of-truth vs Assessment vs Speculation.
These are the analytic workspace; they are inputs to the structured report, not outputs —
do not run the small-ships verification loop on them.

## 3. Source ledger (`source-ledger.md`)

One slug per captured source (e.g. `s.clip1`, `mr26-clip5-dod-corrosion-panel-2026-06-02`),
mapping the slug → audio file → session → `01_sources/` file. **Every cite anywhere in the
synthesis or drafts is `[<slug> @ mm:ss]`**, where `mm:ss` is a real line in the matching
transcript. This is what makes "click every link" a two-hop check.

## 4. Structured report (`02_synthesis/structured-report.md`) — the new layer

Consolidate the `01_sources/` files into one **audience-agnostic** structured report using
`_templates/trip-report.md`: TL;DR (non-obvious takeaways), per-session blocks (speakers,
coverage, key claims, ≤3 verbatim quotes, affect signals), cross-cutting themes, action
items, open questions, confidence notes. Quotes and timestamps are **copied from the
`.transcript.named.md`** — never re-typed. Key claims are FACT-of-speech + cite; everything
interpretive is labeled Assessment.

## 5. Audience drafts (`03_drafts/`) — derived

Derive the audience-specific artifacts (e.g. CACI exec / CACI full / SRF exec / SRF full)
from the structured report by **selection and re-emphasis**, not re-extraction. Cites are
inherited by reference to the structured report; do not re-pull quotes (that creates new
hallucination surfaces and duplicate verification burden). Build `.docx` via
`_scripts/build_brief.py` or pandoc only when a formatted deliverable is needed.

## 6. Verification gate

The six rules in `_meta/verification-rules.md` apply, especially **Rule 6 — click every
link**. Before any draft ships, confirm every `[<slug> @ mm:ss]` resolves to a real line in
the named transcript (grep the `mm:ss`), every quote substring-matches the transcript
verbatim, and no quote upgrades a blended/unconfirmed speaker to a clean name. Adversarial
review per Rule 5.

## 7. Standing discipline

OSI-only (flag and exclude any CUI/FOUO/off-the-record session before transcription);
never invent citations, POCs, or quotes; named-entity discipline (no contractor/product/
person introduced into analysis unless an ingested source surfaced it); boring, durable,
greppable tooling.

---

## Future phases (approach decided 2026-06-12, NOT built this phase)

- **P2 — Slide OCR + cross-referencing.** OCR slide *images* via Gemini **vision** (slide
  images only — never audio) and cross-reference against the local transcript: a slide claim
  corroborated by audio is high-confidence, either alone is medium, conflicts are flagged.
  This wires the template's "Slides referenced" field and the three-way corroboration in
  Confidence notes.
- **P3 — Optional Gemini single-call audio fast-path, GATED BY SENSITIVITY.** For **public /
  non-sensitive** events only (e.g. open conferences), a one-call Gemini audio→report path
  may be used for speed. The local pipeline (§1) stays the **default** and the only path for
  internal/shareable content. Any event's sensitivity must be classified (internal /
  shareable / public) before this path is even considered.

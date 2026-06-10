#!/usr/bin/env python3
"""Transcribe an audio file using faster-whisper. Output a markdown transcript
with segment-level timestamps.

Usage:
    ~/.local/whisper-venv/bin/python3 _scripts/transcribe_audio.py <audio_file>
    ~/.local/whisper-venv/bin/python3 _scripts/transcribe_audio.py <audio_file> --output <path>
    ~/.local/whisper-venv/bin/python3 _scripts/transcribe_audio.py <audio_file> --model small.en

Notes:
    - Runs locally on CPU. Models cached at ~/.cache/huggingface/hub/.
    - English-only models (e.g. medium.en) are smaller and faster than
      multilingual models of the same size, and more accurate on English audio.
    - Does NOT do speaker diarization. Speaker identification is operator's
      job from context.
    - Requires faster-whisper in a venv. This script must be invoked through
      the venv's Python interpreter (e.g. ~/.local/whisper-venv/bin/python3).
"""

import argparse
import sys
from datetime import timedelta
from pathlib import Path


def format_timestamp(seconds: float) -> str:
    """Format seconds as HH:MM:SS or MM:SS."""
    total = int(seconds)
    hours = total // 3600
    minutes = (total % 3600) // 60
    secs = total % 60
    if hours > 0:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    return f"{minutes:02d}:{secs:02d}"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("audio_file")
    ap.add_argument("--output", "-o",
                    help="Output markdown path (default: <audio>.transcript.md alongside the source)")
    ap.add_argument("--model", default="medium.en",
                    help="Whisper model size (tiny.en, base.en, small.en, medium.en, large-v3). Default: medium.en")
    ap.add_argument("--beam-size", type=int, default=5,
                    help="Beam size for decoding (higher = better quality, slower). Default: 5")
    ap.add_argument("--device", default="cpu", choices=["cpu", "cuda"],
                    help="Compute device. 'cuda' uses the GPU (much faster) if available. Default: cpu")
    args = ap.parse_args()

    audio_path = Path(args.audio_file).expanduser().resolve()
    if not audio_path.exists():
        print(f"ERROR: audio file not found: {audio_path}", file=sys.stderr)
        return 1

    output_path = Path(args.output).expanduser().resolve() if args.output else audio_path.with_suffix(".transcript.md")

    print(f"Audio file: {audio_path}", file=sys.stderr)
    print(f"Output:     {output_path}", file=sys.stderr)
    print(f"Model:      {args.model}", file=sys.stderr)
    print(f"Beam size:  {args.beam_size}", file=sys.stderr)
    print("", file=sys.stderr)
    print("Loading model (first run downloads it; subsequent runs use the cache)...", file=sys.stderr)

    from faster_whisper import WhisperModel
    compute_type = "float16" if args.device == "cuda" else "int8"
    model = WhisperModel(args.model, device=args.device, compute_type=compute_type)

    print(f"Transcribing...", file=sys.stderr)
    segments, info = model.transcribe(
        str(audio_path),
        beam_size=args.beam_size,
        vad_filter=True,
        vad_parameters=dict(min_silence_duration_ms=500),
    )

    print(f"Detected language: {info.language} (probability {info.language_probability:.2f})", file=sys.stderr)
    print(f"Duration: {format_timestamp(info.duration)} ({info.duration:.1f}s)", file=sys.stderr)
    print(f"Streaming segments to {output_path} ...", file=sys.stderr)

    header = [
        f"# Transcript: {audio_path.name}",
        "",
        f"- **Source audio:** `{audio_path.name}`",
        f"- **Audio duration:** {format_timestamp(info.duration)}",
        f"- **Detected language:** {info.language} (probability {info.language_probability:.2f})",
        f"- **Model:** {args.model}",
        f"- **Transcription tool:** faster-whisper (local, device={args.device}, compute={compute_type})",
        f"- **Speaker diarization:** NONE — operator must identify speakers from context.",
        "",
        "## Transcript",
        "",
    ]
    output_path.write_text("\n".join(header), encoding="utf-8")

    segment_count = 0
    with output_path.open("a", encoding="utf-8") as f:
        for segment in segments:
            start = format_timestamp(segment.start)
            end = format_timestamp(segment.end)
            text = segment.text.strip()
            f.write(f"**[{start} → {end}]** {text}\n\n")
            f.flush()
            segment_count += 1
            if segment_count % 20 == 0:
                print(f"  ...{segment_count} segments transcribed", file=sys.stderr)

    print(f"Done — {segment_count} segments written to {output_path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())

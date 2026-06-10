"""Speaker diarization with pyannote.audio, mapped onto an existing whisper transcript.

Needs a Hugging Face token (gated models). Provide it via:
  - env HF_TOKEN (or HUGGINGFACE_TOKEN), or
  - a line  HF_TOKEN=hf_xxx  in _scripts/.env
and accept the licenses for pyannote/speaker-diarization-3.1 and pyannote/segmentation-3.0.

Usage:
  ~/.local/whisper-venv/bin/python3 _scripts/diarize_pyannote.py <audio.(mp3|wav)> <transcript.md> [--num-speakers N | --min N --max M]

Writes <transcript>.diarized.md (transcript with [S#] speaker tags) and prints a turn summary.
"""
import argparse, os, re, subprocess, tempfile, sys
from pathlib import Path


def load_token() -> str:
    for k in ("HF_TOKEN", "HUGGINGFACE_TOKEN", "HUGGING_FACE_HUB_TOKEN"):
        if os.environ.get(k):
            return os.environ[k]
    env = Path(__file__).parent / ".env"
    if env.exists():
        for line in env.read_text().splitlines():
            m = re.match(r"\s*(HF_TOKEN|HUGGINGFACE_TOKEN)\s*=\s*(\S+)", line)
            if m:
                return m.group(2).strip().strip('"').strip("'")
    return ""


def to_sec(ts: str) -> float:
    p = [int(x) for x in ts.split(":")]
    return p[0] * 3600 + p[1] * 60 + p[2] if len(p) == 3 else p[0] * 60 + p[1]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("audio"); ap.add_argument("transcript")
    ap.add_argument("--num-speakers", type=int, default=None)
    ap.add_argument("--min", type=int, default=None); ap.add_argument("--max", type=int, default=None)
    a = ap.parse_args()

    token = load_token()
    if not token:
        print("ERROR: no HF token found (set HF_TOKEN in env or _scripts/.env).", file=sys.stderr)
        return 2

    import torch
    from pyannote.audio import Pipeline

    model = os.environ.get("PYANNOTE_MODEL", "pyannote/speaker-diarization-community-1")
    print(f"Loading {model} ...", file=sys.stderr)
    try:
        pipe = Pipeline.from_pretrained(model, token=token)
    except TypeError:  # older pyannote uses use_auth_token
        pipe = Pipeline.from_pretrained(model, use_auth_token=token)
    dev = "cuda" if torch.cuda.is_available() else "cpu"
    pipe.to(torch.device(dev))
    print(f"Device: {dev}", file=sys.stderr)

    # normalize to 16k mono wav
    audio = Path(a.audio)
    wav = audio if audio.suffix == ".wav" else Path(tempfile.mktemp(suffix=".wav"))
    if wav is not audio:
        subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", str(audio),
                        "-ar", "16000", "-ac", "1", str(wav)], check=True)

    kw = {}
    if a.num_speakers: kw["num_speakers"] = a.num_speakers
    if a.min: kw["min_speakers"] = a.min
    if a.max: kw["max_speakers"] = a.max
    print(f"Diarizing ({kw or 'auto speaker count'}) ...", file=sys.stderr)
    # load audio via soundfile (bypass torchaudio/torchcodec) and pass an in-memory waveform
    import soundfile as sf
    import numpy as np
    data, sr = sf.read(str(wav), dtype="float32")
    if data.ndim > 1:
        data = data.mean(axis=1)
    waveform = torch.from_numpy(np.ascontiguousarray(data)).unsqueeze(0)  # (1, time)
    diar = pipe({"waveform": waveform, "sample_rate": sr}, **kw)

    turns = [(t.start, t.end, spk) for t, _, spk in diar.itertracks(yield_label=True)]
    spk_ids = sorted({s for *_, s in turns})
    label = {s: f"S{i+1}" for i, s in enumerate(spk_ids)}
    print(f"{len(spk_ids)} speakers, {len(turns)} turns", file=sys.stderr)

    def spk_for(a0, b0):
        votes = {}
        for s, e, spk in turns:
            ov = max(0.0, min(b0, e) - max(a0, s))
            if ov > 0: votes[spk] = votes.get(spk, 0.0) + ov
        return label[max(votes, key=votes.get)] if votes else "S?"

    seg_re = re.compile(r"\*\*\[([0-9:]+) → ([0-9:]+)\]\*\*\s*(.*)")
    out = Path(a.transcript).with_suffix(".diarized.md")
    n = 0
    with out.open("w") as f:
        f.write(f"# Diarized transcript ({len(spk_ids)} speakers, device={dev})\n\n")
        for line in Path(a.transcript).read_text().splitlines():
            m = seg_re.match(line.strip())
            if not m:
                continue
            txt = m.group(3).strip()
            if not txt:
                continue
            tag = spk_for(to_sec(m.group(1)), to_sec(m.group(2)))
            f.write(f"**[{m.group(1)}] [{tag}]** {txt}\n\n")
            n += 1
    if wav is not audio:
        os.unlink(wav)
    print(f"Wrote {out} ({n} segments tagged across {len(spk_ids)} speakers).", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())

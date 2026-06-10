"""Unified speaker diarization across MULTIPLE clips (one shared speaker set).

Concatenates several audio clips (in the given chronological order) into a single
timeline and diarizes them as ONE job, so each speaker keeps one id across all
clips — "S5" is the same person in the morning and the afternoon. Writes a
per-clip `<transcript>.diarized.md` using each clip's ORIGINAL timestamps but the
unified ids, and prints the total voice count (directly comparable to a known
in-room headcount).

Same robustness as the single-clip version: chunked over the concatenation so VRAM
stays bounded, per-clip checkpoints rewritten after every chunk (crash-resilient),
audio decoded with soundfile to bypass the broken torchcodec FFmpeg backend.

Needs a Hugging Face token (gated model): env HF_TOKEN / a `HF_TOKEN=hf_xxx` line in
_scripts/.env, plus accepted model licenses.

Usage (chronological order — earliest clip first):
  ~/.local/whisper-venv/bin/python3 _scripts/diarize_pyannote_unified.py \
      AUDIO1 TRANSCRIPT1 AUDIO2 TRANSCRIPT2 [...] \
      [--chunk-min 25] [--num-speakers N | --min N --max M] [--seg-batch 16] [--match-thresh 0.65]
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


def fmt(sec: float) -> str:
    sec = int(sec)
    return f"{sec // 3600}:{(sec % 3600) // 60:02d}:{sec % 60:02d}"


SEG_RE = re.compile(r"\*\*\[([0-9:]+) → ([0-9:]+)\]\*\*\s*(.*)")


def write_clip(out: Path, transcript: Path, turns, offset, dur, n_spk, dev, covered_concat, total_dur, label):
    """Map global (concatenated-time) turns onto ONE clip's transcript.

    Transcript timestamps are clip-local; shift each segment by `offset` to vote
    against the global turns, but emit the original clip-local timestamp. Segments
    whose concatenated start is past `covered_concat` are marked [pending].
    """
    def spk_for(a_c, b_c):
        votes = {}
        for s, e, spk in turns:
            ov = max(0.0, min(b_c, e) - max(a_c, s))
            if ov > 0:
                votes[spk] = votes.get(spk, 0.0) + ov
        return f"S{max(votes, key=votes.get) + 1}" if votes else None

    pct = 100.0 * covered_concat / total_dur if total_dur else 0.0
    lines = [f"# Diarized transcript — {label} ({n_spk} unified speakers, device={dev})\n",
             f"> Unified diarization across all clips. Progress: {pct:.0f}% of the "
             f"combined {fmt(total_dur)} timeline. Speaker ids are shared across every clip.\n"]
    for line in transcript.read_text().splitlines():
        m = SEG_RE.match(line.strip())
        if not m:
            continue
        txt = m.group(3).strip()
        if not txt:
            continue
        a_local = to_sec(m.group(1))
        a_c = a_local + offset
        tag = spk_for(a_c, to_sec(m.group(2)) + offset)
        if tag is None:
            tag = "S?" if a_c < covered_concat else "pending"
        lines.append(f"**[{m.group(1)}] [{tag}]** {txt}\n")
    out.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("pairs", nargs="+", help="AUDIO1 TRANSCRIPT1 AUDIO2 TRANSCRIPT2 ... (chronological)")
    ap.add_argument("--chunk-min", type=float, default=25.0)
    ap.add_argument("--num-speakers", type=int, default=None)
    ap.add_argument("--min", type=int, default=None); ap.add_argument("--max", type=int, default=None)
    ap.add_argument("--seg-batch", type=int, default=16)
    ap.add_argument("--match-thresh", type=float, default=0.65)
    a = ap.parse_args()

    if len(a.pairs) % 2 != 0:
        print("ERROR: pairs must be AUDIO TRANSCRIPT AUDIO TRANSCRIPT ... (even count).", file=sys.stderr)
        return 2
    clips = [(Path(a.pairs[i]), Path(a.pairs[i + 1])) for i in range(0, len(a.pairs), 2)]

    token = load_token()
    if not token:
        print("ERROR: no HF token (set HF_TOKEN in env or _scripts/.env).", file=sys.stderr)
        return 2

    import torch, numpy as np, soundfile as sf
    from pyannote.audio import Pipeline

    model = os.environ.get("PYANNOTE_MODEL", "pyannote/speaker-diarization-community-1")
    print(f"Loading {model} ...", file=sys.stderr, flush=True)
    try:
        pipe = Pipeline.from_pretrained(model, token=token)
    except TypeError:
        pipe = Pipeline.from_pretrained(model, use_auth_token=token)
    dev = "cuda" if torch.cuda.is_available() else "cpu"
    pipe.to(torch.device(dev))
    for attr in ("segmentation_batch_size", "embedding_batch_size"):
        if hasattr(pipe, attr):
            try:
                setattr(pipe, attr, a.seg_batch)
            except Exception:
                pass
    print(f"Device: {dev}", file=sys.stderr, flush=True)

    # Decode every clip (soundfile, not torchcodec) and concatenate; record offsets.
    SR = 16000
    parts, offsets, durs = [], [], []
    cursor = 0.0
    for audio, transcript in clips:
        wav = audio if audio.suffix == ".wav" else Path(tempfile.mktemp(suffix=".wav"))
        if wav is not audio:
            subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", str(audio),
                            "-ar", str(SR), "-ac", "1", str(wav)], check=True)
        d, sr = sf.read(str(wav), dtype="float32")
        if d.ndim > 1:
            d = d.mean(axis=1)
        if sr != SR:  # safety; ffmpeg already forced SR
            print(f"WARN: {audio.name} sr={sr} != {SR}", file=sys.stderr, flush=True)
        parts.append(np.ascontiguousarray(d))
        offsets.append(cursor)
        durs.append(d.shape[0] / SR)
        cursor += d.shape[0] / SR
        if wav is not audio:
            os.unlink(wav)
        print(f"  + {audio.name}: {fmt(d.shape[0]/SR)} at offset {fmt(offsets[-1])}", file=sys.stderr, flush=True)

    data = np.concatenate(parts)
    del parts
    full = torch.from_numpy(np.ascontiguousarray(data)).unsqueeze(0)
    total_dur = data.shape[0] / SR
    print(f"Concatenated {len(clips)} clips -> {fmt(total_dur)} ({data.nbytes/1e6:.0f} MB resident)",
          file=sys.stderr, flush=True)

    kw = {}
    if a.num_speakers: kw["num_speakers"] = a.num_speakers
    if a.min: kw["min_speakers"] = a.min
    if a.max: kw["max_speakers"] = a.max

    def cos(u, v):
        nu, nv = np.linalg.norm(u), np.linalg.norm(v)
        return float(u @ v / (nu * nv)) if nu and nv else -1.0

    chunk_samp = int(a.chunk_min * 60 * SR)
    n_chunks = (data.shape[0] + chunk_samp - 1) // chunk_samp
    outs = [t.with_suffix(".diarized.md") for _, t in clips]
    labels = [a.name for a, _ in clips]

    global_turns = []
    centroids = []
    next_gid = 0

    def checkpoint(covered_concat):
        for ci, (audio, transcript) in enumerate(clips):
            write_clip(outs[ci], transcript, global_turns, offsets[ci], durs[ci],
                       next_gid, dev, covered_concat, total_dur, labels[ci])

    for ch in range(n_chunks):
        s0 = ch * chunk_samp
        s1 = min(s0 + chunk_samp, data.shape[0])
        off = s0 / SR
        seg = full[:, s0:s1].contiguous()
        print(f"[chunk {ch+1}/{n_chunks}] {fmt(off)}–{fmt(s1/SR)} diarizing ...", file=sys.stderr, flush=True)

        dout = pipe({"waveform": seg, "sample_rate": SR}, **kw)
        diar = dout.speaker_diarization
        embs = dout.speaker_embeddings
        if embs is not None and len(embs) == 0:
            embs = None

        local = list(diar.labels())
        lemb = {}
        for li, lab in enumerate(local):
            e = None
            if embs is not None and li < len(embs):
                ee = np.asarray(embs[li], dtype="float32")
                if ee.ndim == 1 and np.all(np.isfinite(ee)):
                    e = ee
            lemb[lab] = e

        # Stitch to global ids: match only against PRIOR-chunk centroids, one-to-one.
        prev_n = len(centroids)
        cands = []
        for lab in local:
            e = lemb[lab]
            if e is None:
                continue
            for g in range(prev_n):
                if centroids[g] is None:
                    continue
                s = cos(e, centroids[g])
                if s >= a.match_thresh:
                    cands.append((s, lab, g))
        cands.sort(key=lambda x: x[0], reverse=True)
        l2g, taken = {}, set()
        for s, lab, g in cands:
            if lab in l2g or g in taken:
                continue
            l2g[lab] = g
            taken.add(g)
            centroids[g] = 0.7 * centroids[g] + 0.3 * lemb[lab]
        for lab in local:
            if lab not in l2g:
                l2g[lab] = next_gid
                centroids.append(lemb[lab])
                next_gid += 1

        for t, _, spk in diar.itertracks(yield_label=True):
            global_turns.append((off + t.start, off + t.end, l2g[spk]))

        checkpoint(s1 / SR)
        if dev == "cuda":
            torch.cuda.empty_cache()
        print(f"  chunk done: {len(local)} local -> {next_gid} unified so far ({100.0*(s1/SR)/total_dur:.0f}%)",
              file=sys.stderr, flush=True)

    print(f"DONE. {next_gid} unified speakers, {len(global_turns)} turns across {len(clips)} clips:",
          file=sys.stderr, flush=True)
    for ci in range(len(clips)):
        print(f"  -> {outs[ci]}", file=sys.stderr, flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())

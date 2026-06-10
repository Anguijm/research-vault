"""Chunked, crash-resilient speaker diarization with pyannote.audio (GPU).

Why chunked: a single pass over a ~3 h file pushes the whole job through 8 GB of
laptop VRAM at once and, if it dies, loses everything. This slices the audio into
fixed-length windows, diarizes each on the GPU, frees VRAM between chunks, and
re-writes the partial `.diarized.md` after every chunk so a crash leaves usable
output. Speaker IDs are stitched across chunks via per-speaker embedding cosine
matching (falls back to fresh per-chunk IDs when the model returns no embeddings).

Audio is loaded with soundfile (libsndfile), NOT torchcodec — torchcodec's native
lib won't load against this box's FFmpeg ABI; pyannote accepts an in-memory
{"waveform", "sample_rate"} dict, so we sidestep it entirely.

Needs a Hugging Face token (gated models): env HF_TOKEN/HUGGINGFACE_TOKEN, or a
`HF_TOKEN=hf_xxx` line in _scripts/.env, plus accepted licenses for the model.

Usage:
  ~/.local/whisper-venv/bin/python3 _scripts/diarize_pyannote_chunked.py \
      <audio.(mp3|wav)> <transcript.md> \
      [--chunk-min 25] [--num-speakers N | --min N --max M] [--seg-batch 16]

Writes <transcript>.diarized.md (rewritten after each chunk) and prints progress.
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


def write_diarized(out: Path, transcript: Path, turns, n_spk, dev, covered_until, total_dur):
    """Map global speaker turns onto transcript segments; write a checkpoint.

    Segments past `covered_until` (not yet diarized) are emitted untagged with a
    [pending] marker so the partial file is honest about progress.
    """
    def spk_for(a0, b0):
        votes = {}
        for s, e, spk in turns:
            ov = max(0.0, min(b0, e) - max(a0, s))
            if ov > 0:
                votes[spk] = votes.get(spk, 0.0) + ov
        return f"S{max(votes, key=votes.get) + 1}" if votes else None

    pct = 100.0 * covered_until / total_dur if total_dur else 0.0
    lines = [f"# Diarized transcript ({n_spk} speakers so far, device={dev})\n",
             f"> Progress: diarized through {fmt(covered_until)} / {fmt(total_dur)} "
             f"({pct:.0f}%). Speaker IDs stitched across chunks by embedding match.\n"]
    for line in transcript.read_text().splitlines():
        m = SEG_RE.match(line.strip())
        if not m:
            continue
        txt = m.group(3).strip()
        if not txt:
            continue
        a0 = to_sec(m.group(1))
        tag = spk_for(a0, to_sec(m.group(2)))
        if tag is None:
            tag = "S?" if a0 < covered_until else "pending"
        lines.append(f"**[{m.group(1)}] [{tag}]** {txt}\n")
    out.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("audio"); ap.add_argument("transcript")
    ap.add_argument("--chunk-min", type=float, default=25.0, help="chunk length in minutes")
    ap.add_argument("--num-speakers", type=int, default=None)
    ap.add_argument("--min", type=int, default=None); ap.add_argument("--max", type=int, default=None)
    ap.add_argument("--seg-batch", type=int, default=16, help="segmentation/embedding batch size (VRAM cap)")
    ap.add_argument("--match-thresh", type=float, default=0.65, help="cosine sim to merge a speaker across chunks")
    a = ap.parse_args()

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
    # Cap VRAM per forward pass where the pipeline exposes batch knobs.
    for attr in ("segmentation_batch_size", "embedding_batch_size"):
        if hasattr(pipe, attr):
            try:
                setattr(pipe, attr, a.seg_batch)
                print(f"  set {attr}={a.seg_batch}", file=sys.stderr, flush=True)
            except Exception as e:
                print(f"  could not set {attr}: {e}", file=sys.stderr, flush=True)
    print(f"Device: {dev}", file=sys.stderr, flush=True)

    # Decode once via soundfile (not torchcodec); keep one resident copy.
    audio = Path(a.audio)
    wav = audio if audio.suffix == ".wav" else Path(tempfile.mktemp(suffix=".wav"))
    if wav is not audio:
        subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", str(audio),
                        "-ar", "16000", "-ac", "1", str(wav)], check=True)
    data, sr = sf.read(str(wav), dtype="float32")
    if data.ndim > 1:
        data = data.mean(axis=1)
    full = torch.from_numpy(np.ascontiguousarray(data)).unsqueeze(0)  # (1, T)
    total_dur = data.shape[0] / sr
    print(f"Loaded {fmt(total_dur)} @ {sr} Hz ({data.nbytes/1e6:.0f} MB resident)", file=sys.stderr, flush=True)

    kw = {}
    if a.num_speakers: kw["num_speakers"] = a.num_speakers
    if a.min: kw["min_speakers"] = a.min
    if a.max: kw["max_speakers"] = a.max

    chunk_samp = int(a.chunk_min * 60 * sr)
    n_chunks = (data.shape[0] + chunk_samp - 1) // chunk_samp
    out = Path(a.transcript).with_suffix(".diarized.md")

    global_turns = []          # (start_sec, end_sec, global_id)
    centroids = []             # list of np.ndarray, index == global_id
    next_gid = 0

    def cos(u, v):
        nu, nv = np.linalg.norm(u), np.linalg.norm(v)
        return float(u @ v / (nu * nv)) if nu and nv else -1.0

    for ci in range(n_chunks):
        s0 = ci * chunk_samp
        s1 = min(s0 + chunk_samp, data.shape[0])
        off = s0 / sr
        seg = full[:, s0:s1].contiguous()
        print(f"[chunk {ci+1}/{n_chunks}] {fmt(off)}–{fmt(s1/sr)} diarizing ...",
              file=sys.stderr, flush=True)

        # community-1 returns a DiarizeOutput dataclass: .speaker_diarization is
        # the Annotation; .speaker_embeddings is one centroid per speaker, already
        # ordered to match diar.labels(). Embeddings drive cross-chunk stitching.
        dout = pipe({"waveform": seg, "sample_rate": sr}, **kw)
        diar = dout.speaker_diarization
        embs = dout.speaker_embeddings
        if embs is not None and len(embs) == 0:
            embs = None

        local = list(diar.labels())  # row order matches embs
        # Per-local-speaker embedding (None if missing/degenerate).
        lemb = {}
        for li, lab in enumerate(local):
            e = None
            if embs is not None and li < len(embs):
                ee = np.asarray(embs[li], dtype="float32")
                if ee.ndim == 1 and np.all(np.isfinite(ee)):
                    e = ee
            lemb[lab] = e

        # Stitch to global ids: match ONLY against centroids from PRIOR chunks
        # (snapshot prev_n), one-to-one, greedy by descending similarity. Distinct
        # speakers within this chunk can never collapse, because their own fresh
        # centroids land at indices >= prev_n and are excluded from matching.
        prev_n = len(centroids)
        cands = []  # (similarity, local_label, prior_global_id)
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
            centroids[g] = 0.7 * centroids[g] + 0.3 * lemb[lab]  # running update
        for lab in local:  # unmatched speakers -> fresh global ids
            if lab not in l2g:
                l2g[lab] = next_gid
                centroids.append(lemb[lab])  # may be None; skipped in future matches
                next_gid += 1

        for t, _, spk in diar.itertracks(yield_label=True):
            global_turns.append((off + t.start, off + t.end, l2g[spk]))

        write_diarized(out, Path(a.transcript), global_turns, next_gid, dev, s1 / sr, total_dur)
        if dev == "cuda":
            torch.cuda.empty_cache()
        print(f"  chunk done: {len(local)} local spk -> {next_gid} global so far; "
              f"checkpoint written ({100.0*(s1/sr)/total_dur:.0f}%)", file=sys.stderr, flush=True)

    if wav is not audio:
        os.unlink(wav)
    print(f"DONE. {next_gid} speakers, {len(global_turns)} turns -> {out}", file=sys.stderr, flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())

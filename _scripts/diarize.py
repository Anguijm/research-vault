"""No-token speaker-diarization proof-of-concept.
ffmpeg-extract a segment -> 1.5s windows -> ECAPA embeddings (speechbrain) ->
agglomerative clustering -> map speaker labels onto the existing whisper transcript.

Usage: python diarize_demo.py <mp3> <transcript.md> <start_sec> <end_sec> [n_speakers]
"""
import sys, re, subprocess, tempfile, os, warnings
warnings.filterwarnings("ignore")
import numpy as np
import soundfile as sf
import torch
from sklearn.cluster import AgglomerativeClustering

mp3, tpath, start, end = sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4])
n_spk = int(sys.argv[5]) if len(sys.argv) > 5 else None
SR = 16000
WIN, HOP = 3.0, 1.0

# 1) extract segment to 16k mono wav
wav = tempfile.mktemp(suffix=".wav")
subprocess.run(["ffmpeg","-nostdin","-v","error","-y","-ss",str(start),"-to",str(end),
                "-i",mp3,"-ar",str(SR),"-ac","1",wav], check=True)
audio, _ = sf.read(wav); audio = audio.astype("float32")
os.unlink(wav)

# 2) ECAPA embedder (not gated, no token)
from speechbrain.inference.speaker import EncoderClassifier
enc = EncoderClassifier.from_hparams(source="speechbrain/spkrec-ecapa-voxceleb",
                                     run_opts={"device":"cpu"},
                                     savedir="/tmp/sb_ecapa")

# 3) window + embed (skip low-energy/silent windows)
wlen, hop = int(WIN*SR), int(HOP*SR)
embs, times = [], []
for s in range(0, max(1,len(audio)-wlen), hop):
    seg = audio[s:s+wlen]
    if np.sqrt(np.mean(seg**2)) < 0.005:   # skip near-silence
        continue
    with torch.no_grad():
        e = enc.encode_batch(torch.tensor(seg).unsqueeze(0)).squeeze().cpu().numpy()
    embs.append(e); times.append((start + s/SR, start + (s+wlen)/SR))
embs = np.vstack(embs)
print(f"[{len(embs)} voiced windows embedded]", file=sys.stderr)

# 4) cluster
if n_spk:
    cl = AgglomerativeClustering(n_clusters=n_spk, metric="cosine", linkage="average")
else:
    cl = AgglomerativeClustering(n_clusters=None, distance_threshold=0.65,
                                 metric="cosine", linkage="average")
labels = cl.fit_predict(embs)
print(f"[{len(set(labels))} speakers detected]", file=sys.stderr)

# helper: dominant speaker over a [a,b] time range
def spk_for(a, b):
    votes = {}
    for (ws, we), lab in zip(times, labels):
        ov = max(0, min(b, we) - max(a, ws))
        if ov > 0: votes[lab] = votes.get(lab, 0) + ov
    return max(votes, key=votes.get) if votes else None

# 5) parse transcript segments in [start,end], map speaker
def to_sec(ts):
    p = [int(x) for x in ts.split(":")]
    return p[0]*3600+p[1]*60+p[2] if len(p)==3 else p[0]*60+p[1]
seg_re = re.compile(r"\*\*\[([0-9:]+) → ([0-9:]+)\]\*\*\s*(.*)")
print(f"\n=== Diarized transcript  {start/60:.1f}–{end/60:.1f} min ===\n")
for line in open(tpath):
    m = seg_re.match(line.strip())
    if not m: continue
    a, b = to_sec(m.group(1)), to_sec(m.group(2))
    if b < start or a > end: continue
    txt = m.group(3).strip()
    if not txt: continue
    lab = spk_for(a, b)
    tag = f"S{lab+1}" if lab is not None else "S?"
    print(f"[{m.group(1)}] [{tag}] {txt}")

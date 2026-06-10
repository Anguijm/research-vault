"""Propose a split for the over-merged diarization ids (S1, S2, S7).

For each blended id, attribute every contiguous run to the nearest enrolled voice,
then summarize by clip (morning/afternoon) and as a coarse block timeline. If a
merge is time-localized (e.g. S1 = Fitzgerald in AM, Fjeld in PM) it shows up as a
clean per-clip split. Cosines are printed so confidence is visible; runs below the
floor are 'unclear'. Nothing is rewritten — this is a proposal to confirm.

Run: ~/.local/whisper-venv/bin/python3 _scripts/split_blended_ids.py
"""
import re, os, subprocess, tempfile, sys
from collections import defaultdict
from pathlib import Path
import numpy as np, soundfile as sf, torch

SR = 16000
BASE = "trip-reports/SRFSG-APR-2026/audio/"
CLIP_MP3 = {"AM": BASE + "2026-06-08_srfsg_clip2.mp3", "PM": BASE + "2026-06-08_srfsg_clip1.mp3"}
CLIP_DIA = {"AM": BASE + "2026-06-08_srfsg_clip2.transcript.diarized.md",
            "PM": BASE + "2026-06-08_srfsg_clip1.transcript.diarized.md"}
TARGETS = {"S1", "S2", "S7"}
FLOOR = 0.45

def mmss(m, s): return m * 60 + s
ENROLL = {
    "John Anguiano":   [("AM", mmss(41, 14), mmss(41, 50))],
    "Amanda Keech":    [("AM", mmss(41, 59), mmss(42, 16))],
    "Dasan Sparks":    [("AM", mmss(42, 21), mmss(42, 40))],
    "Matt Lyon":       [("AM", mmss(43, 25), mmss(44, 0))],
    "Paul Knight":     [("AM", mmss(44, 54), mmss(45, 47))],
    "Greg Hubert":     [("AM", mmss(45, 56), mmss(46, 55))],
    "Karen D.":        [("AM", mmss(49, 2), mmss(49, 20)), ("AM", mmss(50, 2), mmss(50, 14))],
    "Brooke Hawley":   [("AM", mmss(50, 24), mmss(50, 42))],
    "Shannon Bruce":   [("AM", mmss(50, 49), mmss(51, 44))],
    "John Fitzgerald": [("AM", mmss(62, 30), mmss(63, 45))],
    "Brian Fjeld":     [("PM", mmss(0, 0), mmss(0, 35))],
}


def to_s(t):
    p = [int(x) for x in t.split(":")]
    return p[0] * 3600 + p[1] * 60 + p[2] if len(p) == 3 else p[0] * 60 + p[1]


def hm(s):
    s = int(s); return f"{s//3600}:{(s%3600)//60:02d}:{s%60:02d}"


def main():
    audio = {}
    for k, mp in CLIP_MP3.items():
        wav = tempfile.mktemp(suffix=".wav")
        subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", mp,
                        "-ar", str(SR), "-ac", "1", wav], check=True)
        d, _ = sf.read(wav, dtype="float32")
        if d.ndim > 1:
            d = d.mean(axis=1)
        audio[k] = d
        os.unlink(wav)
    dev = "cuda" if torch.cuda.is_available() else "cpu"
    from speechbrain.inference.speaker import EncoderClassifier
    enc = EncoderClassifier.from_hparams(source="speechbrain/spkrec-ecapa-voxceleb",
                                         run_opts={"device": dev}, savedir="/tmp/sb_ecapa")

    def embed(clip, a, b, cap=30.0):
        seg = audio[clip][int(a * SR):int(min(b, a + cap) * SR)]
        if len(seg) < int(0.8 * SR):
            return None
        with torch.no_grad():
            return enc.encode_batch(torch.tensor(seg).unsqueeze(0)).squeeze().cpu().numpy()

    enrolled = {}
    for name, wins in ENROLL.items():
        es = [embed(c, a, b, cap=60.0) for (c, a, b) in wins]
        es = [e for e in es if e is not None]
        if es:
            enrolled[name] = np.mean(es, axis=0)
    nm = list(enrolled)

    def cos(u, v):
        return float(u @ v / (np.linalg.norm(u) * np.linalg.norm(v)))

    def nearest(e):
        sims = sorted(((cos(e, enrolled[n]), n) for n in nm), reverse=True)
        c0, n0 = sims[0]
        name = n0 if c0 >= FLOOR else "unclear"
        return name, c0, sims[1]

    seg_re = re.compile(r'\*\*\[([0-9:]+)\] \[(S\d+)\]\*\* (.*)')
    # collect runs for the target ids, tagged with clip + chronological order
    runs = defaultdict(list)  # S -> list of (clip, start, end)
    for clip, f in CLIP_DIA.items():
        segs = []
        for ln in Path(f).read_text().splitlines():
            m = seg_re.match(ln.strip())
            if m:
                segs.append((to_s(m.group(1)), m.group(2)))
        i = 0
        while i < len(segs):
            j = i
            while j + 1 < len(segs) and segs[j + 1][1] == segs[i][1]:
                j += 1
            start = segs[i][0]
            end = segs[j + 1][0] if j + 1 < len(segs) else segs[j][0] + 4
            if segs[i][1] in TARGETS and end - start >= 2.0:
                runs[segs[i][1]].append((clip, start, end))
            i = j + 1

    for S in sorted(runs, key=lambda s: int(s[1:])):
        # attribute each run
        attr = []  # (clip, start, end, name, cos)
        for clip, a, b in runs[S]:
            e = embed(clip, a, b)
            if e is None:
                continue
            name, c, _ = nearest(e)
            attr.append((clip, a, b, name, c))
        # per-clip name minutes
        by = defaultdict(lambda: defaultdict(float))
        for clip, a, b, name, c in attr:
            by[clip][name] += (b - a)
        print(f"\n========== {S} ==========")
        for clip in ("AM", "PM"):
            if not by[clip]:
                continue
            tot = sum(by[clip].values())
            parts = sorted(by[clip].items(), key=lambda kv: -kv[1])
            line = ", ".join(f"{n} {100*sec/tot:.0f}% ({sec/60:.0f}m)" for n, sec in parts if sec/tot >= 0.06)
            print(f"  {clip}: {line}")
        # coarse block timeline (merge adjacent same-name runs within a clip)
        print("  timeline:")
        last = None
        for clip, a, b, name, c in attr:
            key = (clip, name)
            if last and last[0] == clip and last[1] == name:
                last[3] = b; last[4].append(c)
            else:
                if last:
                    cs = np.mean(last[4])
                    print(f"    [{last[0]} {hm(last[2])}–{hm(last[3])}] {last[1]} (~{cs:.2f})")
                last = [clip, name, a, b, [c]]
        if last:
            cs = np.mean(last[4])
            print(f"    [{last[0]} {hm(last[2])}–{hm(last[3])}] {last[1]} (~{cs:.2f})")


if __name__ == "__main__":
    main()

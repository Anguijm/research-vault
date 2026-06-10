"""Diagnostic: re-attribute each diarization run to the nearest ENROLLED voice.

The unified diarization over-merged some distinct people into one speaker id (e.g.
S1 = John Fitzgerald in the morning + Brian Fjeld in the afternoon). This enrolls a
voiceprint per known person — from their clean self-introductions PLUS operator-
identified anchor utterances — then assigns every contiguous diarization run to the
nearest enrolled voice. Output is a merge map: for each old S-id, how its speech
time distributes across named people (revealing merges + mis-attributions). Runs
that match nobody above threshold are 'unknown' (late arrivals / no enrollment).

Run: ~/.local/whisper-venv/bin/python3 _scripts/reattribute_by_voiceprint.py
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
UNKNOWN_COS = 0.45  # below this to every enrolled voice => 'unknown'

def mmss(m, s): return m * 60 + s
# Enrolled voiceprints: clean self-intro windows (corrected names) + operator anchors.
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
    # operator-identified anchors for the two voices merged into S1:
    "John Fitzgerald": [("AM", mmss(62, 30), mmss(63, 45))],   # "my heavy programmers" / 1210 / power platform
    "Brian Fjeld":     [("PM", mmss(0, 0), mmss(0, 35))],      # "Military Sealift Command"
}


def to_s(t):
    p = [int(x) for x in t.split(":")]
    return p[0] * 3600 + p[1] * 60 + p[2] if len(p) == 3 else p[0] * 60 + p[1]


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
    print(f"ECAPA on {dev}", file=sys.stderr, flush=True)

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
    names = list(enrolled)

    def cos(u, v):
        return float(u @ v / (np.linalg.norm(u) * np.linalg.norm(v)))

    def nearest(e):
        sims = sorted(((cos(e, enrolled[n]), n) for n in names), reverse=True)
        return sims[0], (sims[1] if len(sims) > 1 else (0.0, "-"))

    # Build contiguous runs per old-S id, embed each, attribute to nearest enrolled voice.
    seg_re = re.compile(r'\*\*\[([0-9:]+)\] \[(S\d+)\]\*\* (.*)')
    attribution = defaultdict(lambda: defaultdict(float))  # old_S -> name -> seconds
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
            tag, dur = segs[i][1], end - start
            if dur >= 2.0:
                e = embed(clip, start, end, cap=30.0)
                if e is not None:
                    (c0, n0), _ = nearest(e)
                    who = n0 if c0 >= UNKNOWN_COS else f"unknown(~{n0} {c0:.2f})"
                    attribution[tag][who] += dur
            i = j + 1

    print("\n=== merge map: each diarization S-id -> share of speech by enrolled voice ===\n")
    for S in sorted(attribution, key=lambda s: int(s[1:])):
        total = sum(attribution[S].values())
        parts = sorted(attribution[S].items(), key=lambda kv: -kv[1])
        shown = ", ".join(f"{n} {100*sec/total:.0f}%" for n, sec in parts if sec / total >= 0.08)
        print(f"  {S:4s} ({total/60:.1f} min):  {shown}")


if __name__ == "__main__":
    main()

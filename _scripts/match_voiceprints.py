"""Match named people (from their morning self-introductions) to diarization
speaker ids, by voiceprint similarity.

Why: the intro round-robin diarizes badly (everyone collapses to a couple of ids),
but we DO know the time window when each named person spoke their intro. So embed
each named intro window directly (bypassing the bad intro tags), embed each S-id
from its long monologues in the substantive discussion (where diarization is
reliable), and match by cosine. Same model (ECAPA) on both sides => comparable.

S-ids with no confident name = people who skipped the intro (late arrivals) or whose
voiceprint didn't match — reported as unmatched rather than guessed.

Run: ~/.local/whisper-venv/bin/python3 _scripts/match_voiceprints.py
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
INTRO_ZONE = (40 * 60, 56 * 60)  # AM seconds to EXCLUDE from S references (bad diarization)

# Named intro windows in AM (clip2) local seconds, read from the transcript content.
def mmss(m, s): return m * 60 + s
NAMED = {
    "John Anguiano (you)": [("AM", mmss(41, 14), mmss(41, 50))],
    "Amanda Keech":        [("AM", mmss(41, 59), mmss(42, 16))],
    "Jason Sparks":        [("AM", mmss(42, 21), mmss(42, 40))],
    "Matt Lyon":           [("AM", mmss(43, 25), mmss(44, 0))],
    "Paul Knight":         [("AM", mmss(44, 54), mmss(45, 47))],
    "Greg Hubert":         [("AM", mmss(45, 56), mmss(46, 55))],
    "Karen D.":            [("AM", mmss(49, 2), mmss(49, 20)), ("AM", mmss(50, 2), mmss(50, 14))],
    "Brooke Hawley":       [("AM", mmss(50, 24), mmss(50, 42))],
    "Shannon Drews":       [("AM", mmss(50, 49), mmss(51, 44))],
}


def to_s(t):
    p = [int(x) for x in t.split(":")]
    return p[0] * 3600 + p[1] * 60 + p[2] if len(p) == 3 else p[0] * 60 + p[1]


def main():
    # Decode both clips once into memory.
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
        print(f"decoded {k}: {len(d)/SR/60:.1f} min", file=sys.stderr, flush=True)

    dev = "cuda" if torch.cuda.is_available() else "cpu"
    from speechbrain.inference.speaker import EncoderClassifier
    enc = EncoderClassifier.from_hparams(source="speechbrain/spkrec-ecapa-voxceleb",
                                         run_opts={"device": dev}, savedir="/tmp/sb_ecapa")
    print(f"ECAPA loaded on {dev}", file=sys.stderr, flush=True)

    def embed(clip, a, b):
        seg = audio[clip][int(a * SR):int(b * SR)]
        if len(seg) < int(0.8 * SR):
            return None, 0.0
        with torch.no_grad():
            e = enc.encode_batch(torch.tensor(seg).unsqueeze(0)).squeeze().cpu().numpy()
        return e, len(seg) / SR

    def embed_spans(spans, cap=30.0):
        es, secs = [], 0.0
        for clip, a, b in spans:
            e, dur = embed(clip, a, min(b, a + cap))
            if e is not None:
                es.append(e); secs += dur
        return (np.mean(es, axis=0) if es else None), secs

    # Named-person voiceprints from their intro windows.
    name_emb, name_secs = {}, {}
    for n, wins in NAMED.items():
        name_emb[n], name_secs[n] = embed_spans(wins, cap=60.0)

    # Build per-S references from longest monologue runs OUTSIDE the AM intro zone.
    seg_re = re.compile(r'\*\*\[([0-9:]+)\] \[(S\d+)\]\*\* (.*)')
    runs_by_S = defaultdict(list)
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
            end = segs[j + 1][0] if j + 1 < len(segs) else segs[j][0] + 5
            tag = segs[i][1]
            if not (clip == "AM" and INTRO_ZONE[0] <= start <= INTRO_ZONE[1]):
                runs_by_S[tag].append((end - start, clip, start, end))
            i = j + 1

    S_emb, S_secs = {}, {}
    for S, runs in runs_by_S.items():
        runs.sort(reverse=True)
        es, tot = [], 0.0
        for dur, clip, a, b in runs:
            if dur < 2:
                continue
            e, used = embed(clip, a, min(b, a + 30))
            if e is not None:
                es.append(e); tot += used
            if tot >= 90:
                break
        if es:
            S_emb[S] = np.mean(es, axis=0); S_secs[S] = tot

    def cos(u, v):
        return float(u @ v / (np.linalg.norm(u) * np.linalg.norm(v)))

    Ss = sorted(S_emb, key=lambda s: int(s[1:]))
    print(f"\nReference voiceprints built for: {', '.join(Ss)}\n")
    print(f"{'NAME':24s} {'intro_s':>7s}  best -> (cosine)   runners-up")
    best_for_S = defaultdict(list)
    for n in NAMED:
        ne = name_emb[n]
        if ne is None:
            print(f"{n:24s} {name_secs[n]:7.1f}  (no usable intro audio)")
            continue
        sims = sorted(((cos(ne, S_emb[S]), S) for S in Ss), reverse=True)
        c0, s0 = sims[0]
        runners = ", ".join(f"{S}={c:.2f}" for c, S in sims[1:4])
        print(f"{n:24s} {name_secs[n]:7.1f}  {s0} = {c0:.2f}      {runners}")
        best_for_S[s0].append((c0, n))

    print("\n--- per-S summary ---")
    for S in Ss:
        claimants = sorted(best_for_S.get(S, []), reverse=True)
        if not claimants:
            print(f"  {S}: (no name matched — likely a late arrival / no intro)   ref={S_secs[S]:.0f}s")
        else:
            who = ", ".join(f"{n} ({c:.2f})" for c, n in claimants)
            flag = "  <-- COLLISION" if len(claimants) > 1 else ""
            print(f"  {S}: {who}   ref={S_secs[S]:.0f}s{flag}")


if __name__ == "__main__":
    main()

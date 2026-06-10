"""Write named versions of the diarized transcripts.

Applies the confirmed speaker identifications (2026-06-10): four clean voiceprint
locks applied globally, three high-confidence blocks re-labeled by time range
inside the over-merged ids. Everything else keeps its S-tag and is flagged blended
in the header. Non-destructive: reads `<clip>.transcript.diarized.md`, writes
`<clip>.transcript.named.md`.
"""
import re
from pathlib import Path

BASE = "trip-reports/SRFSG-APR-2026/audio/"
GLOBAL = {"S3": "John Anguiano", "S4": "Greg Hubert", "S6": "Brooke Hawley", "S9": "Dasan Sparks"}

def hms(t):
    p = [int(x) for x in t.split(":")]
    return p[0] * 3600 + p[1] * 60 + p[2] if len(p) == 3 else p[0] * 60 + p[1]

CLIPS = [
    {"in": BASE + "2026-06-08_srfsg_clip2.transcript.diarized.md",
     "out": BASE + "2026-06-08_srfsg_clip2.transcript.named.md",
     "label": "clip 2 — morning, 2026-06-08",
     "blocks": [("S1", hms("1:01:44"), hms("1:15:06"), "John Fitzgerald"),
                ("S7", hms("2:18:13"), hms("2:49:17"), "Paul Knight")]},
    {"in": BASE + "2026-06-08_srfsg_clip1.transcript.diarized.md",
     "out": BASE + "2026-06-08_srfsg_clip1.transcript.named.md",
     "label": "clip 1 — afternoon, 2026-06-08",
     "blocks": [("S1", hms("0:00:06"), hms("0:11:01"), "Brian Fjeld")]},
]

LEGEND = """# Named transcript — {label}

> Speaker identification status (as of 2026-06-10). Names below replace the raw
> diarization S-ids; the S-tagged source is kept in the matching `.diarized.md`.
>
> **Confirmed** (voiceprint match + self-introduction): **John Anguiano** (was S3),
> **Greg Hubert** — outside team-building facilitator (S4), **Brooke Hawley** (S6),
> **Dasan Sparks** (S9).
>
> **High-confidence block re-labels** inside over-merged ids (time-ranged):
> **John Fitzgerald** = S1 @ 1:01:44–1:15:06 (morning); **Brian Fjeld** = S1 @
> 0:00:06–0:11:01 (afternoon); **Paul Knight** = S7 @ 2:18:13–2:49:17 (morning).
>
> **Still blended / approximate — confirm by ear:** remaining S1, S2, S5, S7, S8,
> S10, S11 are over-merged or unenrolled diarization clusters. S1 ≈ a Fitzgerald
> (morning) / Fjeld (afternoon) mix; S2 ≈ Amanda Keech + Shannon Bruce (inseparable
> by voiceprint); the early-morning S7 (~1:20–1:58) is an unresolved speaker; S5/S8/
> S11 are likely the quiet/late arrivals who skipped the introductions. [S?] = no
> speaker assigned (overlap/gap).
"""

seg_re = re.compile(r'^\*\*\[([0-9:]+)\] \[(S\d+|S\?|pending)\]\*\* (.*)$')

for c in CLIPS:
    out_lines = [LEGEND.format(label=c["label"])]
    relabels = 0
    for ln in Path(c["in"]).read_text().splitlines():
        m = seg_re.match(ln.strip())
        if not m:
            continue
        ts, tag, txt = m.groups()
        s = hms(ts)
        name = tag
        if tag in GLOBAL:
            name = GLOBAL[tag]; relabels += 1
        else:
            for bt, a, b, bn in c["blocks"]:
                if tag == bt and a <= s <= b:
                    name = bn; relabels += 1
                    break
        out_lines.append(f"**[{ts}] [{name}]** {txt}")
    Path(c["out"]).write_text("\n\n".join(out_lines) + "\n", encoding="utf-8")
    print(f"wrote {c['out']}  ({relabels} segments named)")

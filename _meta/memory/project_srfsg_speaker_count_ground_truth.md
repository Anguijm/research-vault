---
name: project_srfsg_speaker_count_ground_truth
description: SRFSG Apr 2026 review had ~13 distinct voices total across both Day-1 clips; a couple spoke very little
metadata:
  type: project
---

The operator was in the room for the CACI SRFSG Annual Program Review 2026 and
states there were **~13 distinct speakers total** across both Day-1 audio clips,
with **a couple who spoke very little**. Use this as ground truth when diarizing
and when mapping machine speaker ids (S1, S2, …) onto real names.

**Why:** it calibrates the diarization. Standalone per-clip counts are not
comparable to this 13 — each clip clusters speakers independently, so a person in
both clips is counted twice. The number comparable to ~13 comes from a **unified
cross-clip run** (both clips concatenated and diarized as one job, sharing one
speaker set) via `_scripts/diarize_pyannote_unified.py`.

**How to apply:** treat S-numbers as a labeling scaffold, not a verified
headcount. The very-quiet speakers are exactly the ones automated diarization
handles worst (too little voice signal to embed reliably — the `std() degrees of
freedom <= 0` warnings), so any machine count can be ±2 on them; the operator's
ear is the final arbiter. If the unified count lands materially below ~13,
re-run with `--max`/`--num-speakers` hints or a lower `--match-thresh` to recover
quiet speakers; if well above, raise the threshold. Relates to
[[project_operator_team_at_srf_jrmc]] for matching voices to named SRF people.

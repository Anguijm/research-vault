---
type: readme
study: world-class-planning
title: Build folder — what to run and in what order
classification: internal
created: 2026-07-28
---

# Build folder

Everything needed to build and run the early work-screening tool in Qlik. Read this first; the
folder used to be a flat pile of fifteen files with names like "Latest Script" and it was not
possible to tell which one to run.

## Run these, in this order

| File | State | What it does |
|------|-------|--------------|
| `phase-anatomy-diagnostic.md` | **run 2026-07-28, answered its question** | Fits nothing. Prints what a job's phases look like so we could decide which ones belong in a span. It established that `S01` and the rest of the S, P and M families are paperwork: near-zero labour, median duration around 350 days, opening at day zero. That was the cause of every earlier failure. Re-run it if the exclusion rule needs retuning. |
| `span-screen-v4.md` | **current, not yet run** | The screen. Excludes paperwork phases, works out which codes those are from the data rather than a hard-coded list, and reports how much of a job is idle waiting between steps. |
| `granularity-test.md` | **current, not yet run** | The first honest accuracy measurement. Learns on half the finished jobs, scores the other half, and reports how often the prediction lands in the right pile or a safely longer one, swept across work-type granularity. Also settles whether the regression beats a plain median. |

## Reference

| File | What it is |
|------|-----------|
| `qvd-field-inventory.md` | All 50 QVDs and 1,180 fields with source and definition, generated from the operator's data dictionary, plus a cross-reference of the 59 association keys showing which tables join to which. Use this instead of guessing field names. |
| `data-fields-and-tooling.md` | The earlier, narrower note on which fields the method needs and which tool to build in. Still current on method, superseded on field names by the inventory above. |
| `qlik-table-dump.txt` | Raw `LOAD` statements for the tables in the operator's Qlik app. Was `QLIK_Tables`. |
| `qlik-troubleshooting-handoff.md` | Self-contained context for a fresh assistant session, including the Qlik behaviours that have each cost a reload. Hand this over if a run fails and this session is not available. |

## `_runs/` — evidence from actual reloads

Kept because two of the three runs were wrong in instructive ways, and the reload logs are the only
ground truth in this project.

| File | What it shows |
|------|---------------|
| `2026-07-26_run1-output-all-must-do.xlsx` | First live output. All 2,699 candidates in one bin, predictions clustered at 366 days. The failure that started the diagnosis. |
| `2026-07-26_gemini-debug-session.md` | The debugging transcript, plus the schema dump that established the real field names and the phase-anatomy diagnostic output. Was `Recent Gemini`. |
| `2026-07-27_run2-script.qvs` | The script as the operator ran it on 27 July. Was `Latest Script`. |
| `2026-07-27_run2-reload-log.txt` | Its reload log. Was `latest output`. |
| `2026-07-28_run3-output-working-screen.xlsx` | First usable output: bins discriminate, 3,600 of 3,708 candidates score off their own SWBS fit. Also the evidence that the model is a lookup table, since estimated man-days correlate only 0.22 with predicted span. |

## `_lineage/` — superseded, kept on purpose

The vault keeps every version. These are here so the folder above stays readable, not because they
are disposable.

- `span-screen-v1.md` — the first-cut screen. Its `[CONFIRM]` list is still the best record of how
  the real field names were established.
- `span-screen-v3.md` — tested three span definitions at once. Superseded by v4 once the paperwork
  phases were identified, but its sum-of-phase-days and longest-phase variants are the controls v4
  refers to.
- `span-screen-test-harness.md` — the standalone diagnostic block, now folded into the scripts
  themselves. Its warning that `$(=Peek(...))` does not evaluate inside `TRACE` is the single most
  useful line in the folder.

## Open questions live elsewhere

Method decisions and their reasoning are in `../_decisions.md`, not here. This folder is only
artifacts.

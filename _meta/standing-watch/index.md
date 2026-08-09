---
type: standing-watch
id: standing-watch
title: Standing watch — pre-solicitation monitoring for the Navy maintenance enterprise
customer: none — this is not an opportunity
sensitivity: internal
opened: 2026-08-09
last_updated: 2026-08-09
auto_find: false          # run deliberately with --watch-dir, not on the opportunity sweep
cadence: monthly
last_find_run:
last_find_count_ai:
last_find_count_sam:
last_find_count_usa:
---

# Standing watch

News and press-release monitoring for the Navy maintenance enterprise, independent of any single
opportunity. **This is not an opportunity folder.** Nothing here goes through a gate, and there is
no capture brief. It exists to catch the events that happen *before* a solicitation exists.

## The reasoning

The opportunity scanner reads SAM.gov, which surfaces a requirement only once it is already a
solicitation. By then the scope is written and the incumbent usually knows the customer. The
operator's framing on 2026-08-09: the point of tracking customer activity is to anticipate
solicitations before they appear.

The evidence that this channel works is recent and specific. The two most valuable finds of the
last month — the SWRMC Pacific container programme and NAMPIE — came from a conference keynote and
a LinkedIn post. Neither was in SAM. Neither was in the newsletter beat matrix.

## What is watched, and why

Queries in `_search-config.yaml` are grouped by **trigger logic**, not by topic:

| Trigger | What it means |
|---|---|
| Organisation standing up | A new command has to decide how it buys; that window is when to be known to it |
| Unfunded programme finds money | Funding is the event that converts an intention into contracts |
| Statutory mandate | Mandates with deadlines reliably become programmes |
| Study recommendation uptake | A published recommendation the Navy acts on becomes a requirement |
| Recurring venue | Requirements get discussed at conferences before they are written |
| Industrial-base expansion | Pacific build-outs of existing programmes create new demand |

## How to run it

```bash
_scripts/.venv/bin/python _scripts/find_sources.py --watch-dir _meta/standing-watch
```

`auto_find` is `false` and this folder sits outside `opportunities/`, so the normal sweep will not
pick it up. That is deliberate: these triggers move on quarters, AI searches cost per query, and a
watch that fires weekly would mostly re-find the same material.

Results land in `_inbox.md` here, and ingested sources in `01_sources/`, exactly as they do for an
opportunity.

## Discipline

Every organisation and programme named in the config is already surfaced in a vault source. Nothing
is pre-loaded. One candidate, a recurring CNRMC mid-July leadership summit, was **excluded** because
it surfaced from a web search rather than an ingested source; if a source captures it, add it then.

## Review

A standing watch that only grows stops being read. When reviewing, go query by query and ask whether
the trigger is still plausible. Delete the ones that are not. If a watch item matures into a real
pursuit, it belongs in an opportunity folder and should come out of here.

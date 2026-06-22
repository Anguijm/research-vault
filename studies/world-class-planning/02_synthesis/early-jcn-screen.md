---
type: synthesis
study: world-class-planning
title: The early JCN screen — what's answerable when work first arrives
classification: internal
created: 2026-06-23
---

# The early JCN screen

The operator's decision is to screen **super early — as Job Control Numbers (JCNs) arrive in
AIM**, not later at the planning level. This note works through what that choice makes possible
and what it rules out. The short version: going early rules out AIM's good (planned) duration —
it doesn't exist yet — and makes a history-based estimate the only way to put a time on a
fresh JCN.

## What you have at induction, and what you don't
When a JCN is brokered in from the Type Commander's Validation, Screening, and Brokering (VSB)
system, it arrives with a **Class F ("ballpark," ±40%) estimate** of man-hours and material
(NAVSHIPREPFACINST 4700.1F ¶13.3). It does **not** yet have a CU-Phase (Component Unit Phase)
breakdown, a crew size, a sequence, or a duration in shifts — all of that is built later in
Technical and Execution Planning. So **AIM's native span estimate does not exist yet for a fresh
JCN.** Screening early is a deliberate choice to screen before the good number is born.

## What that makes the screen
Three consequences, which together define the screen:

1. **Lead with the drydock cut — it's the one clean answer at induction.** Whether a JCN needs the
   ship docked is structural, readable from the spec, and needs no duration estimate. It alone
   sorts a large share of "must-do in the CNO package" (docking work can't go in a CMAV or a WOO —
   no docking Key Events exist there). Cheapest, most reliable bin; do it first.

2. **For the time questions, a history model is the only option.** With no AIM span yet, the only
   way to put elapsed time on a fresh JCN is to look up what *similar* JCNs actually took —
   actual **Cycle Time** by work type, from AIM-NT / the HIT Kit. The Class F man-hours alone
   can't answer "96 hours?" or "6 weeks?" because man-hours are effort, not elapsed time, until
   you divide by a crew and lay them on a calendar. (Building that per-JCN history number is the
   subject of [estimate-attribution](estimate-attribution.md).)

3. **It lives in a gate you already have.** The Shop Screening Process (4700.1F §9) runs at
   induction, already weighs "work scope durations with respect to the availability duration," and
   already bands work by a 20-man-day line. So this is an enhancement to an existing early screen,
   not a new process.

## Design it as a three-bin sort, not a yes/no verdict
Two honest limits of going this early shape the design:

- **The split question (multiple windows of opportunity) mostly can't be answered yet.** SRF's own
  rule (¶10.1.2) gates a split on the *engineered steps* being technically separable, with Code 240
  Chief Engineer approval — and those steps don't exist until planning produces the CU-Phase
  breakdown. At induction you can only give a provisional, by-work-type split guess; the real call
  firms up later.
- **Class F is ±40%, so the early time estimate is coarse.** That's fine if the early screen
  *sorts* rather than decides: **clearly small → deferrable / "maybe" pile; clearly large or
  drydock-dependent → "must-do" CNO package; marginal → flag for a firmer look once the CU-Phase
  estimate exists.** A three-bin sort honors the data's precision; a hard yes/no over-claims it.

## A unit definition to settle first
Before testing anything against "96 hours," define what it means — 96 elapsed clock hours (four
days) or work-shifts? AIM measures span in 8-hour shifts on a one-shift / five-day calendar, so
the two don't line up until the definition is fixed. (And since "96 hours" isn't in 4700.1F at
all, SRF is defining it from scratch regardless.)

## The shape of the screen, end to end
1. **Drydock?** Yes → must-do (docking CNO availability). No → continue.
2. **Look up the JCN's history-based labor** (its work-type/SWLIN/size bin — see
   [estimate-attribution](estimate-attribution.md)).
3. **Convert labor → standalone span** (crew + calendar + work-type wait/cure/test drivers).
4. **Sort into three bins** against the window thresholds (96-hour [once defined] and 6-week CMAV).
5. **Provisional split flag** by work type; firm it at planning.

---
type: source-grounding
study: world-class-planning
title: What the AIM-NG manuals and 4700.1F actually say (distilled for the screen)
classification: internal
created: 2026-06-23
sources: 01A–11A AIM-NG + NAVSHIPREPFACINST 4700.1F + C200 Process Guide (all Distribution A)
---

# AIM-NG grounding — the facts that bear on the screen

What the manuals say, pulled together from a full read of all thirteen documents and organized
around the three-question screen. Citations are to the source paragraphs/pages so any claim can
be checked. Acronyms are expanded on first use.

## 1. Two of the three questions are already in SRF's own manual; one is not

SRF-JRMC's Availability Management Manual (NAVSHIPREPFACINST 4700.1F) already defines the windows
the screen asks about:

- **CMAV (Continuous Maintenance Availability)** = "normally **2 to 6 weeks** in duration…
  typically scheduled when the ship will be in port" (¶1.1.2). So "fits a 6-week CMAV?" is the
  upper bound of SRF's own CMAV definition.
- **WOO (Window of Opportunity)** — and the split rule, verbatim (glossary, p. 359): "**No length
  requirements exist for WOOs, so if a work item can be broken into multiple installation/repair
  phases it may be accomplished in multiple WOOs.**" The gate (¶10.1.2): a work item may be split
  across multiple WOOs if it is **not "at sea limiting," is approved by the Code 240 Waterfront
  Chief Engineer, and "the engineered steps can be technically broken up into several repair
  periods."** That is the third screen question, with its approval gate already specified.
- **"96 hours" has no basis in 4700.1F.** It appears once, as a **fire-safety** trigger (the
  8010-series requirements between concurrent availabilities, p. 152) — **not** a work-closeout
  category. If SRF adopts a 96-hour screen it must define it locally (or find it in the Joint
  Fleet Maintenance Manual or a Type Commander REDLINES instruction). Open gap.

There is already a **mandatory-vs-deferrable** regime, too: only the Code 240 Chief Engineer can
designate work "mandatory" (¶1.3); non-mandatory work "may be screened to a later availability,
continuous maintenance period, or window of opportunity" (C200 §3.9.5.2). This is the existing
analog of the screen's "must-do vs. maybe" split.

## 2. Drydock dependency is the cleanest, earliest discriminator
A CMAV and a WOO have **no docking/undocking Key Events** (DD00/UD00) — those exist only in a
Docking Selected Restricted Availability (DSRA). So **work that needs the ship docked (underwater
hull, sea valves, shafts, rudder, below-waterline preservation) structurally cannot fit a CMAV or
a WOO** and is forced into a docking CNO availability. This is readable from the spec/work type at
induction, needs no duration estimate, and decides a large share of the "must-do" list by itself
(4700.1F Figure 27 Key Event Requirement Matrix; C200 §4.2.4 "event-pure" rule).

## 3. How AIM estimates — and why a labor number is not a time number
- The schedulable atom is the **CU Phase (Component Unit Phase)**. Its **duration is in shifts**
  and is a **span** number — touch time **plus** wait/cure/test **plus** the Completion-of-Work
  Review — **not** a labor-hour sum (C200 §2.5; EXE Ch 8A; "duration includes required wait time
  such as 7-day NDT after welds or preservation cure," EPL Ch 4A).
- Duration is **built late**, in Technical/Execution Planning, from man-hours ÷ crew size ÷ 8 →
  shifts, then the longest path through the sequenced tasks. So the same labor with a different
  crew size or shift pattern (one-shift "15 calendar" vs. two-shift "25") yields a different span.
- **Estimate classes are the consistency yardstick** (C200 definitions): Class A ±10%, **Class C
  ±15%** (budget-quality, the planned estimate), Class D ±20%, **Class F ±40%** ("ballpark" —
  escalate prior cost + empirical similar-work cost + factors). At brokering, a **Class F estimate
  (man-hours + material) rides in with each JCN** (4700.1F ¶13.3; C200 §3.2.1.1).

## 4. The calibration data exists — but no one closes the loop on duration
AIM captures the actuals needed to calibrate estimates, but uses them to manage the current
availability, not to update a standard-duration library:
- **Cycle Time** = claimed actual start to claimed actual finish per CU Phase = the **actual span**
  (EXE Ch 8A).
- **QAC** (budget) vs **AQWP** (actual labor), both in **Resource-Days**, per CU Phase; **PfCw
  (Performance Factor for Closed Work)** = budget ÷ actual for completed work = the cleanest
  estimate-accuracy ratio (PMC Ch 10A).
- The **Reference Availability Model** uses a past like-availability's as-executed actuals as the
  next one's baseline (PMC Ch 10A) — the closest existing thing to "consistent estimates from
  history."
- History lives in **AIM-NT** and the **HIT Kit (Historical Information Tool Kit)**, which future
  planners are *required* to reuse for similar jobs (PCO Ch 11A).
- **Gap:** the C200 guide has **no quantitative estimate-to-actual variance metric and no
  calibration cadence**. Duration calibration is something SRF would build, not adopt.

## 5. The screen already has a home: the Shop Screening Process
The **Shop Screening Process** (4700.1F §9) runs at induction, already evaluates "work scope
durations with respect to the availability duration" (¶9.8.1), and already bands work by a
**20-man-day** line (Priority 0 < 20 MD, Priority 4 > 20 MD; ¶9.7.1). So a duration screen is an
enhancement to an existing early gate, with a man-day-band precedent already in the instruction.

## 6. The data model for attribution (the bundled-JCN problem)
- A **JCN (Job Control Number)** is the incoming work request; it becomes (part of) a **Job
  Summary (JS)**, "a logical grouping of like work at the SWLIN level or below" (C200 §3.2.2.12).
- The **CU Phase carries SWLIN (Ship's Work List Item Number) and component**, and rolls up to the
  Job Summary — so actual labor (AQWP) and Cycle Time are available **at CU-Phase level**.
- **When one JCN = one JS**, the CU-Phase actuals are cleanly that JCN's. **When several JCNs share
  a JS**, the CU-Phase-to-JCN link is ambiguous wherever JCNs share a SWLIN or share common
  service/test/tag-out phases — so per-JCN actuals are entangled. This is the attribution problem
  the estimation method (see [estimate-attribution](../02_synthesis/estimate-attribution.md))
  solves.

## 7. NMD vs AIM (why SRF's data is actually an advantage)
**NMD (Navy Maintenance Database)** develops the work-item specifications (its Master Specification
Catalog); **AIM (WebAIM at SRF)** executes and schedules them, in shifts at the CU-Phase level,
and captures actual Cycle Time (4700.1F §1.1.1). So SRF has a *richer* native substrate for the
duration questions than an NMD command — the work is to standardize and calibrate it, not invent
it.

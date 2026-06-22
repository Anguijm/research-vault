---
type: synthesis
study: world-class-planning
title: Getting a per-JCN actual out of bundled history
classification: internal
created: 2026-06-23
---

# Getting a per-JCN actual out of bundled history

The screen needs an estimate for **one** incoming Job Control Number (JCN). But history doesn't
always come one JCN at a time: when several JCNs were bundled into a single Job Summary, the
actual time and labor rolled up to the *summary*, and you can't cleanly say how much belonged to
each JCN. This note lays out the problem and two ways to get a per-JCN number anyway — a simple
one and a rigorous one (the rigorous one is written out in plain language).

## The problem, stated plainly
- One JCN per Job Summary → easy. The summary's CU Phases (Component Unit Phases), with their
  actual labor and Cycle Time, are that JCN's.
- Several JCNs per Job Summary → hard. The CU-Phase actuals are there, and they tie to SWLIN
  (Ship's Work List Item Number) and component, but where JCNs share a SWLIN or share common
  service/test/tag-out phases, you can't say which shifts were whose. The bundle's total is
  known; the per-JCN split is not.
- You only ever receive JCNs one at a time at induction, so you need a **per-JCN** number, built
  out of history that is partly bundled.

## The reframe that makes it solvable: attribute LABOR, not TIME
This is the most important move. Two of the things AIM records behave very differently when work
is bundled:

- **Labor** (Resource-Days / man-shifts) **adds up.** Three JCNs in one summary used, in total,
  about the sum of what the three would use apart (minus a little shared setup). You *can* split
  an additive total among its parts.
- **Cycle Time** (elapsed start-to-finish span) **does not add up.** Bundled JCNs are worked in
  parallel, share one tag-out and one access opening, so the bundle's span is closer to the
  longest single path through it — the max, not the sum. Splitting a span that was never the sum
  of its parts is a puzzle with no clean answer.

So: **do the attribution in labor** (well-posed), then **convert labor to span later** at
screening time (divide by crew, lay on the calendar, add the work-type wait/cure/test). Never try
to recover per-JCN span directly from a bundle.

## The simple way (do-first): job costing
Treat it exactly like costing a shop job:
1. **Directly attribute** the CU Phases you *can* map to a single JCN through their SWLIN/component
   — that's most of the production work.
2. **Allocate the shared phases** — services, staging, the tag-out, the test phases that cover
   several JCNs — across the JCNs they served, using each JCN's Class F (ballpark) man-hour
   estimate as the split key. Do the same wherever two JCNs collide on one SWLIN.
3. The pieces sum back to the bundle total by construction, and you now have a per-JCN labor figure
   even inside bundles.

This is enough to start. The rigorous way below uses all the data at once and also tells you how
much to trust each number.

## The rigorous way, in plain language

The goal: figure out how long **one kind of job** usually takes, even though your records often
lump several jobs together and you never saw them apart. Think of it like a stack of grocery
receipts where the price next to each item got torn off — but the **total** at the bottom is
still printed. With enough receipts, you can still work out the price of a banana.

**Step 1 — Sort every JCN into a handful of bins.** A bin is a *kind* of work — same trade, same
sort of SWLIN, same rough size (small / medium / large by its ballpark estimate). The idea is
that two JCNs in the same bin take about the same effort. Aim for a few dozen bins, not hundreds.

**Step 2 — Write each past Job Summary as one simple sentence.** Record only the mix of bins it
contained and the one number you actually know — the total labor:
> "This summary had two bin-A jobs and one bin-C job, and the whole thing took 300 man-days."

You are **not** guessing the split. You only write down the mix and the total.

**Step 3 — Do that for every past summary, easy and bundled alike.** A one-JCN summary is a
sentence with a single bin — "one bin-B job took 80 man-days" — which tells you a bin-B job is
about 80 right there. A bundled summary is a sentence with several bins and one total.

**Step 4 — Solve all the sentences together.** Each sentence is a little puzzle: *total = (how
many bin-A jobs × the cost of a bin-A job) + (how many bin-B × the cost of a bin-B) + …* You don't
know the per-bin costs yet — those are what you're after. One bundled sentence alone can't be
solved. But **hundreds of sentences, with the bins showing up in different combinations, can be
solved together**, because the same bin appears alongside many different partners, and only one
set of per-bin numbers makes all the sentences come out as close to true as possible. Finding
that best-fitting set of numbers is the whole trick — a computer does it instantly. (It's the
same idea as drawing the single best line through a cloud of dots. The formal name is
*regression*, or *least squares*; you don't need the name to use it.)

**Step 5 — Out comes a table.** Bin A ≈ X man-days, bin B ≈ Y, and so on — the typical actual
labor for one job of each kind, recovered even for jobs you only ever saw bundled. It also tells
you **how sure** it is about each bin: a bin that showed up in lots of summaries → trust it; a bin
that showed up only once or twice → treat it as a guess. That confidence is itself useful — it
tells you where the screen is solid and where it's shaky.

**Step 6 — Use it on a new JCN.** A JCN arrives at induction. Read its bin (trade, SWLIN kind,
size). Look up that bin's number. That's your approximate actual **labor** for the new JCN —
built from all your history, including the bundled history you could never split by hand. Then
convert it to elapsed time the usual way (crew, calendar, waits) to test it against the windows.

**A nice extra.** Instead of solving for "man-days per bin," you can solve for "**how the actual
compared to the ballpark estimate**, per bin" — a multiplier. (A bin that runs at 1.3 means jobs
of that kind take about 30% longer than their ballpark.) Then for a new JCN you just take the
ballpark estimate that already arrived with it and multiply. Same method, riding on a number you
already have at induction. In AIM's own language this multiplier is the **Performance Factor for
Closed Work (PfCw)** — recovered per bin, even from bundles.

## One caveat to design around: standalone vs. bundled
Jobs get bundled *for a reason* — related work, same system, same tag-out — and a JCN done inside
a bundle has a **shorter** span than it would alone, because it's sharing the access and the
setup. For the screen you almost always want the **standalone** span ("can this item, on its own,
fit a window?"), which is the conservative, defensible basis — bundling can only help from there.
So: lean on the clean one-JCN history for the **span** calibration, and use the bundled history
only for the additive thing it's good for — **labor**. If you ever quote a bundled-derived number
as a span, you'll understate it.

## What this gives you, and what's still owed
- **Gives:** a per-JCN labor estimate (with a confidence), built from all history; convertible to
  a standalone span for the screen.
- **Still owed:** the labor → span conversion (crew + calendar + work-type waits), calibrated
  against clean one-JCN actuals; and confirmation that Cycle Time and AQWP are actually queryable
  by SWLIN / work type out of AIM-NT (the whole approach rests on that data being reachable).

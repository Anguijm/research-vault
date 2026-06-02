---
type: scenario-card
opportunity: BDR-FLEET-READINESS
phase: 1
created: 2026-06-01
revised: 2026-06-02
decision_moment: bdat-to-bdar-handoff
audience: SRF-JRMC-Yokosuka-wardroom
duration_minutes: 15
---

# Scenario 2 — BDAT-to-BDAR handoff

## Setup

*0530, BDAT report lands in the SIPR inbox. DDG-XX took three hits in a brief engagement during a contested transit; BDAT embedded with the strike group spent eight hours on board assessing damage before she made it in. Ship is alongside at SRF-JRMC. Her CO is asking the wardroom for a repair sequence by 0700.*

*0545, CO's conference room. Around the table: CHENG, Waterfront Ops, Production Officer, Business and Strategic Planning Officer. CO presides. Seventy-five minutes to brief the ship's CO.*

## What the room knows

**The ship and the BDAT report:**

- DDG-XX, returning from a contested transit. Three hits in a brief engagement. Self-sustaining damage control complete; ship transited alongside under own power.
- BDAT spent eight hours aboard before the ship arrived. The BDAT report describes damage. It does not sequence the repair.
- The ship's CO is asking the SRF wardroom for the sequence by 0700. The CO's hand-off note (not on the BDAT report) says the strike group resumes operations in 11 days.

**The four damage items:**

- **A — CIWS mount.** Non-functional. Self-defense degraded. ~36-hour repair. X51 + X11. Parts on hand at the SRF.
- **B — Forward berthing compartment.** Structural cracking from a near-miss overpressure event. Cracks below the waterline but not flooding. ~5-day repair. X11 + X26. Parts in transit from Norfolk.
- **C — Main electrical bus.** Insulation damage from heat. Ship is operational but one electrical event away from a propulsion-affecting casualty. ~18-hour repair. X51. Parts on hand. Requires de-energizing half the ship during the work.
- **D — Sensor mast.** RF-emitter damage to a primary search radar. Ship can fight without it but with degraded long-range warning. ~4-day repair. X67 + supporting trades. Requires a KTR field service rep — KTR FSR is available in ~48 hours but a contract has to be in place through FLCY. Cash and FLCY bandwidth are both BSPO calls.

**Constraints on the sequence:**

- The room can start two items today. The other two start tomorrow.
- Item C de-energizes half the ship. Anything else worked on that side is disrupted during the de-energization window.
- Item B's parts from Norfolk are en route; ETA tomorrow morning. Starting B today means hours of idle hands until parts arrive.
- Item D's KTR FSR isn't on the deckplate until ~48 hours from now, and only if the contract closes through FLCY in time. Starting D today means idle hands or pre-positioning work while the FSR transits.

**SRF-JRMC current state:**

- Existing backlog: Blue Ridge (LCC-19) in Drydock 6 for a depot availability. A DDG in Drydock 5 for a docking reset. X11 and X26 are at capacity supporting those availabilities. X67 and X51 ~15% slack. X56 and X38 ~20% slack.
- MLA surge same-day in Yokosuka if shop demand exceeds standing capacity.

### What the room does NOT know

- Whether Norfolk's parts shipment for Item B actually arrives on its stated ETA.
- Whether FLCY can close the KTR contract for Item D's FSR inside 48 hours.
- Whether the electrical bus on Item C cascades before the wardroom can get to it.
- Whether the ship's CO has implicit priorities he hasn't stated (his hand-off note named the 11-day operational resume but not which item matters most to him).

## The decision

**Pick the two damage items to start today. Defend the sequence.**

[Restate Items A, B, C, D above as the choice set. The room picks any two.]

## What the room is weighing

1. **Cascade risk vs. work-now value.** Item C (main electrical bus) is the cascade item — one event away from a propulsion-affecting casualty. Starting C today buys insurance against the bus failing under load. Deferring C is a real risk bet.

2. **External dependencies (parts and KTR FSR) vs. start-now-to-feel-productive.** Item B's parts arrive tomorrow morning. Item D's FSR arrives in 48 hours and only if FLCY closes the contract. Starting either today pre-positions the work but accepts idle hours if the dependency slips. Starting them tomorrow is honest about the timeline but loses the staging-ahead window.

3. **Disruption from de-energization.** Item C de-energizes half the ship for ~18 hours. Anything else worked on that side during de-energization is disrupted. The sequence has to account for what de-energization makes impossible.

4. **Mission-readiness recovery curve.** CIWS restores self-defense. Berthing restores below-waterline structural integrity. Bus restores electrical reliability. Sensor restores long-range warning. The wardroom's sequence implicitly says which capability the ship gets back first. The 11-day operational resume means *all four* have to be done in time, but the *order* shapes what the ship can do during transit back to the strike group.

5. **What the sequence says to the ship's CO.** The BDAT report described damage; the sequence is the SRF's call. The sequence is also the CO's first impression of how the wardroom thinks under tempo. A sequence that names cascade risk and dependency bets reads professional; a sequence that just lists "items in order of repair time" reads thin.

## Defender's prompt

Stand. In 60 seconds, defend the two-item pick. Name the cascade risk you are accepting on the items you deferred. Name the dependency you are betting on. Moderator stops you at 60.

---

## After-action discussion prompts (for moderator)

1. **The BDAT report gave you four items but no priority. Who actually owns the priority call — BDAT, the ship's CO, or the SRF wardroom?** The pedagogical point of the BDAT-to-BDAR handoff: the report describes damage; the repair sequence is the SRF's call. A wardroom that waits for "more priority guidance" from the CO is failing the drill — the CO is asking the SRF for the sequence, not providing one.

2. **Item C is the cascade item. Did you start it today, or accept the cascade risk? Why?** Probes risk tolerance. There is no wrong answer; there is only a defended answer.

3. **Item D requires FLCY to close a KTR contract inside 48 hours. Did the BSPO get pressed on whether that's realistic, or did the room assume it?** Surfaces whether the contracting-timeline risk was named or wished away.

4. **What does the ship's CO see in your sequence?** Forces the wardroom to articulate the briefing, not just the repair plan.

## Learning objective (for moderator only)

**The BDAT-to-BDAR handoff is incomplete by design.** BDAT describes damage. The repair sequence is the SRF wardroom's call and cannot be offloaded to either the BDAT or the ship's CO. Wardrooms that wait for "more priority guidance" from the CO are failing the drill — the CO is asking the SRF for the sequence, not providing one. The drill teaches the room to take ownership of the sequencing call under incomplete information, which is the actual operational reality of a BDAR triage.

Secondary lesson: external dependencies (parts ETAs, KTR FSR contracts via FLCY) are real timeline risks. A wardroom that picks items B or D today is implicitly betting on Norfolk's parts ETA or FLCY's contracting bandwidth. Those bets should be named, not assumed.

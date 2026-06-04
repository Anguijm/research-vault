---
name: Navy shipyard terminology — docking/undocking, pierside, wet berth (not "haul-out")
description: Real Navy and shipyard people don't say "haul-out" or "pre-haul-out" — they say docking, undocking, pierside, wet berth. Customer-facing artifacts must use the right vocabulary or they sound fake.
type: feedback
---

The Navy / surface-ship shipyard vocabulary for what happens at an availability:

- **Docking** — the ship coming into a dry dock and getting set down on blocks once the dock is dewatered. NOT "haul-out."
- **Undocking** — the ship coming off blocks and out of the dry dock. NOT "haul-back" or "splash."
- **Pierside** — the ship is at a pier (not in a dry dock at all).
- **Wet berth** — the ship is sitting inside a dry dock that's still flooded (dock not yet dewatered, ship not yet on blocks).
- **Pre-docking** / **post-docking** — before and after the docking event. NOT "pre-haul-out" / "post-haul-out."

In practice for Edify-style hull inspection: NDI can be deployed pierside or in a wet berth — both pre-docking work, ship still floating. This is what Apt was pitching at MegaRust 2026.

**Why:** Operator (J. Anguiano) called this out on 2026-06-04: "Those are not words that we would use in our industry. ... You're either docking or undocking. ... Real Navy people don't fucking call it a haulout." Operator works at SRF-JRMC; he knows the trade vocabulary. Using "haul-out" in customer-facing artifacts makes the prose sound like a contractor who's never been on a Navy waterfront.

**How to apply:**

1. **In customer-facing artifacts** (`03_drafts/`, anything that goes to SRF leadership, CACI BD, or any Navy reader): use docking, undocking, pierside, wet berth, pre-docking, post-docking. Never haul-out, haul-back, splash, get-her-in-the-water.

2. **In synthesis and source files**: if I'm quoting a speaker who said "haul-out" verbatim, keep their words and mark them as the speaker's terminology. The fix is only needed when I'm summarizing or recommending in my own voice.

3. **"Wet dock" is not the same as "wet berth."** "Wet dock" historically means an enclosed dock that stays permanently flooded (a maritime term from European commercial shipping). A flooded U.S. Navy dry-dock with a ship in it is a wet berth, not a wet dock.

4. **Commercial industries (oil and gas, petrochemical, mining, nuclear) use "haul-out"** and similar terminology. Vendors crossing from those industries into Navy may use their home vocabulary in pitches — Apt at Edify is an example. When I summarize for a Navy reader, translate to Navy vocabulary.

5. **Other Navy / SRF terminology I should default to (incomplete list, grow over time):**
   - **Availability** — the maintenance period itself (CNO Availability for major work, SRA for selected restricted, RAV for restricted, EDSRA / DSRA for emergency or extended docking).
   - **Docking availability** — an availability that includes the ship going up on blocks.
   - **Non-docking availability** — an availability done entirely pierside or in a wet berth.
   - **Ship's force** — the crew. Distinct from contractors and from shipyard workers.
   - **Pre-availability planning** / **post-availability** — natural Navy phrasing.

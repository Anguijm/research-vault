---
type: decision-log
opportunity: BDR-FLEET-READINESS
phase: 1
scope: _demo subfolder
created: 2026-06-01
---

# Demo design decisions

## 2026-06-01 — Phase 1 demo scope and structure

Decisions made during the alignment session that produced this folder. Grill-me skill (`_meta/grill-me.md`) was invoked before scaffolding per CLAUDE.md mandate.

### What the demo is

A personal-portfolio proof of concept for the BDR Level-1 flash-drill game described in `00_research-file.md` §11.3.1. Audience for the demo is the operator's portfolio reviewer, not a Navy customer. The demo proves the game mechanic works in its lowest-technology form.

### What the demo is not

- Not software. Not a web app. Not a CLI. Operator confirmed this explicitly on 2026-06-01: "I'm not actually looking for code. I'm looking for content and medium. I'm happy to print scenario cards."
- Not the customer-facing product. The Level-1 product CACI would actually sell to the Navy includes content review with NWDC, classification handling, and a multi-session engagement plan — none of which apply to a portfolio piece.
- Not infrastructure shared with `harness-cli`. The operator confirmed: "harness is another infra repo. Since we are staying here maybe we don't need it." Decision: stand the demo up entirely within research-vault, no external dependencies.

### Branch and location

- **Branch:** `bdr-demo` off `main` in `research-vault`
- **Location:** `opportunities/BDR-FLEET-READINESS/_demo/`
- Parallels existing underscore-prefixed subfolders in the BDR opportunity folder (`_red-teams/`, `_plays/`, `_decisions/`).
- A branch — not a separate repo — was chosen because the operator confirmed the demo lives inside the vault, not as a sibling project.

### Audience inside the scenarios

The wardroom and staff cell at a **CONUS-based Regional Maintenance Center (RMC)**. Operator chose this audience explicitly: "I want to focus on scenarios that the RMC might be approached with."

The corresponding fleet-commander-side scenarios (port selection, in particular) are deferred. The brief notes both audiences play from the same scenario base, but Phase 1 holds to one audience for cognitive coherence.

### Number of scenarios — three

Three scenarios for Phase 1, covering three of the six operational-decision moments named in `00_research-file.md` §1:

1. **Forward team mobilization** — the RMC sends people, gear, and language coverage to a damaged ship in Sasebo.
2. **BDAT-to-BDAR handoff** — the RMC receives a Battle Damage Assessment Team report and sequences the repair under captain time-pressure.
3. **BDAR triage under combat tempo** — a three-ship surge arriving at the RMC over 60 hours forces a triage approach decision.

Three is enough to demonstrate that the game mechanic generalizes across decision types. Adding more scenarios is straightforward later; the marginal portfolio value of a fourth and fifth scenario is small for Phase 1. The two decision moments not represented (BDAT-side preparation and degraded-communications resource access) are deferred — they're realistic but Phase 1 covers the most operationally central three.

Port selection is explicitly NOT one of the three. Port selection is more of a fleet-commander decision than an RMC-receiving decision (see §1 of the BDR research file). Phase 1 holds to the RMC-receiving-side framing.

### Format — printable markdown cards

Each scenario is a single markdown file in `scenarios/` formatted to print to a single letter-sized sheet. The front of the card has the setup, decision, and five variables. The back (which is the lower half of the markdown file) has the after-action discussion prompts and the moderator-only learning objective.

Operator confirmed the print-card medium: "I'm happy to print scenario cards." No further format experimentation was attempted in Phase 1.

### Named-entity discipline

All three scenarios use:
- **Generic ship designators** (DDG-XX, FFG-XX) — no real USS hull names or numbers. Avoids creating fictional-but-mistakable specific ship claims.
- **Real public port names** (Sasebo, Yokosuka, Norfolk implied) — these are public Navy port locations and operator-blessed by `_entity-allowlist.yaml` and the BDR research file §1.
- **No invented host-nation contractors or named personnel.** Roles are described functionally (the captain, the BDAT, the Naval Surface Force commander).

This follows the named-entity discipline that's binding for analytical content in this vault. Scenario content is illustrative game material, not analytical claims about real events; the discipline still applies because the demo is a portfolio piece that gets read by people who can't always tell illustrative from factual.

### Decisions rejected

- **Code-based demo.** Rejected by operator on 2026-06-01.
- **Web app, CLI, or notebook delivery.** Same rejection.
- **A scenario library of 15+ scenarios.** Out of scope for Phase 1; would be appropriate at Phase 2 once the format is validated.
- **AI-generated scenario content.** Out of scope; introduces a software dependency the demo is explicitly avoiding.
- **Multiple audiences in Phase 1.** RMC-receiving-side only; fleet-commander-side deferred.
- **Pulling content patterns from `harness-cli`.** Deemed unnecessary once the operator confirmed the demo stays in research-vault.

### Open questions deferred to Phase 2 or later

- Whether the printed-card design needs visual polish (graphic design, layout, card-stock printing) before it's actually portfolio-ready. Phase 1 is content; Phase 2 could address visual presentation.
- Whether to add the three remaining decision moments (port selection, emergency contracting in a foreign port, degraded-communications information access) as additional scenarios.
- Whether to develop a moderator's training video or written facilitator certification.
- Whether to test the format with actual players and record an after-action note.

---
name: Don't explain a Navy customer's own world to them
description: When writing for a Navy activity (SRF-JRMC, any TYCOM, any RMC), don't gloss organizations, ranks, or terminology that are part of their everyday chain of command and trade vocabulary — they know
type: feedback
---

When writing customer-facing artifacts for a Navy activity (SRF-JRMC, any TYCOM, any RMC, any NAVSEA or NAVAIR shore command), the reader already knows the Navy chain of command, the Navy organizations, and the everyday Navy vocabulary. Don't explain those things. Explaining them reads as condescending and makes the prose feel like a contractor writing for an outsider.

**Specific examples — do not gloss these for a Navy reader:**

- **AIRPAC, SURFPAC, SUBPAC, AIRLANT, SURFLANT, SUBLANT** — type commanders. They know what a type commander is.
- **NAVSEA, NAVAIR, NAVSUP, SPAWAR / NAVWAR** — major systems commands.
- **SES, GS, O-#, E-#** — civilian and military ranks.
- **MARMC, SWRMC, NWRMC, SRF-JRMC, SRF-Japan, Pearl Harbor (PHNSY)** — Regional Maintenance Centers and shipyards.
- **FRC (Fleet Readiness Center) and its detachments** — they know.
- **CNO, COMNAVAIRFOR, COMNAVSURFOR** — leadership.
- **Availability types** — CNO Availability, DSRA, EDSRA, SRA, RAV, PSA, EOH. They know.
- **NSI** — NAVSEA Standard Items.
- **MIL-PRF, MIL-DTL, MIL-STD** — military specification prefixes.
- **ISEA** — In-Service Engineering Agent.
- **OPA, OMN, SCN** — appropriation categories.
- **ICW** — in conjunction with.
- **PAC, LANT** — Pacific, Atlantic.
- **CONUS, OCONUS, FDNF** — they know.

**Why:** Operator (J. Anguiano, SRF-JRMC) called this out on 2026-06-04 reading the SRF full report. His words: "I don't think we need to explain who AIRPAC is to SRF. Pretty sure the Navy activity understands who is in their chain of command and who is not. Completely unneeded explanation."

**How to apply:**

1. **For Navy-activity customer artifacts (SRF-JRMC and similar):** drop glosses on type commanders, systems commands, rank shorthand, and standard Navy vocabulary. Let the reader bring their own knowledge to the prose. Name the entity, attach a fact, move on.

2. **For CACI internal artifacts:** a light gloss may be appropriate the first time a less-common acronym appears (CACI BD leadership is Navy-fluent but not exclusively ex-Navy). For first-tier acronyms like AIRPAC, SES, NAVSEA, MARMC, no gloss needed even in CACI artifacts.

3. **Where to keep the gloss anyway:** when the gloss adds non-obvious information beyond expansion — e.g., naming the specific commander (CDR vs. RDML) or explaining a recent organizational change (AFLCMC now reporting to SAF/AQ rather than AFMC). That kind of "expansion-plus-context" earns its place. Pure-definition glosses do not.

4. **Test:** if removing the gloss leaves the sentence understandable to the intended customer, the gloss was unneeded. If removing it leaves a real gap, the gloss earns its place — but consider whether the gap is for the wrong audience.

5. **This rule does NOT relax the acronym-expansion rule for unusual or new acronyms.** OOT, KSS, OSRP, AEM/S — those still warrant first-use expansion because they're not universal Navy vocabulary. The line is "things in this customer's everyday world" vs. "things that might be new to even a Navy reader."

6. **"Navy chain of command" is not one uniform set — it splits by warfare community.** A customer's "everyday world" depends on which side they sit on. Operator (J. Anguiano, SRF-JRMC, surface side) confirmed on 2026-06-04 that **FRC (Fleet Readiness Center) should be expanded** for a surface-side reader, even though it's a perfectly normal aviation-side term — because FRCs are the NAVAIR analog to RMCs and SRF surface people don't have day-to-day exposure to them. The general principle: **crossover terms from the other warfare community need expansion.** Specifically:

   - **For surface-side customers (SRF, SURFMEPP, SURFPAC, NAVSEA shore commands)**: expand aviation-side terms (FRC, NAWCAD/NAWCWD, COMNAVAIRPAC's specific subordinate commands, FRC detachments, aviation-specific MIL-PRFs and MIL-STDs).
   - **For aviation-side customers**: expand surface-side terms (RMC names not in their region, NAVSEA codes, surface-ship MIL-PRFs they wouldn't see).
   - **For sub-side customers**: expand both surface and aviation terms; SUBMEPP and the submarine community has its own vocabulary subset.

   The test: would this term appear in a routine email or chat at the customer's command? If not, gloss it.

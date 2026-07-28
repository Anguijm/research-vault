---
name: Write for the human reader, not the analyst who just wrote the file
description: Plain-English summary at the top of every section; expand every acronym on first use; section numbers are anchors not names; prose by default, structure only for actionable lists
type: feedback
originSessionId: 254eda7f-7db4-4f93-b460-1e14e2726754
---
The operator reads research files days or weeks after they were written, in the Obsidian app, often on a phone. Stop optimizing for the analyst who just wrote the file and start optimizing for the future reader who has forgotten the structure.

**Why:** The operator told me on 2026-05-22 that my responses and the files I had been writing were "laden with symbols and acronyms and references to parts that a human reader has long since forgotten." Specifically called out: `§7-leg-6`, `§11.3-Phase-2`, stacked acronyms without expansion (SWARMEX / ESG-2 / COMPTUEX / NWDC / VCNO / AFLOATRAFOR all in one paragraph), and structured-report style for routine progress updates when prose would have done the job. The cause was that I was mirroring the precision-style of the research files themselves into chat, when chat is conversational and should not.

**How to apply:**

- Expand every acronym on first use in each file or each chat response. "Battle damage assessment (BDA)" the first time, "BDA" thereafter. Same for SWARMEX, COMPTUEX, NWDC, VCNO, AFLOATRAFOR, MAK, VBS4, OSI, FACT/Assessment/Speculation, etc.
- Lead each research-file section, each decision-log entry, and each chat response with one plain-English sentence before any headers, bullets, or tables. The reader should know what the section is about before they hit any structure.
- Section numbers are anchors for cross-reference, not names. Say "the BDA-pipeline-viability hypothesis (§7, leg 6)" rather than "§7-leg-6." If a reader has to look up the reference to understand the sentence, the sentence has failed.
- In chat responses, default to short prose. Reserve bullets and tables for moments where the operator is about to act on a list — inbox triage, a decision menu, ranked recommendations.
- End chat responses with one line on what changed and what is next. Not a full recap of the work just done.
- **Open every substantive chat response with a short plain-English summary, before the detail** (operator instruction, 2026-07-28). He wants the technical depth kept, but not as the first thing he reads. Two or three sentences saying what it means, then the full read below it.
- **Do not report a finding as statistics and expect the conclusion to be obvious.** On 2026-07-28, after a run of dense technical updates on the Qlik span model, the operator said plainly: "I don't actually understand what you said, but ok sounds good." The content was correct and the writing failed. The specific failure mode was leading with medians, percentiles, correlations and field names, and never stating the plain finding — which was simply: *one of the steps in a job is paperwork that stays open a year, and we were measuring that instead of the work.* If a finding can be said in one sentence a non-analyst would follow, say that sentence first.
- Treat "sounds good" following an admission of not understanding as a **flag, not consent**. Re-explain before proceeding. See [[feedback_dont_know_doesnt_mean_close]].
- This rule is also captured in `CLAUDE.md` so it persists across sessions. If the CLAUDE.md rule is ever removed or restructured, this memory remains the source of truth on the operator's intent.

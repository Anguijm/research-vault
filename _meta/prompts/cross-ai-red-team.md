---
type: prompt
name: cross-ai-red-team
recommended_model: whichever-you-did-not-use-for-drafting
last_revised: 2026-05-10
---

# Cross-AI red team

**When to use:** After producing a capture brief v0.1 draft. Run on the OTHER model from whichever you used for drafting — cross-model disagreement is the value. This is a substitute for a human adversarial review when no human is available; it is not a replacement (Rule 5).

**Recommended model:** Whichever you did NOT use for drafting. If you drafted with Claude, red-team with Gemini; if you drafted with Gemini, red-team with Claude.

**The prompt:**

```
You are reviewing this capture brief in three roles, in three separate passes.

Pass 1 — Customer reviewer: You are a J7 staffer at USINDOPACOM. What in this
brief is wrong, oversimplified, or sounds like marketing? What would you push
back on?

Pass 2 — Competitor analyst: You work at a competing prime. Where are the
weakest parts of the recommendation? What facts could be challenged? What
would you exploit if you saw this?

Pass 3 — Skeptical exec: You are a defense pure-play exec with 4 minutes to
read this. Is the recommendation clear? Is the ask actionable? What would
make you say "come back when you've done more homework"?

Be specific. Cite the section number for each critique.
```

**Notes:**
- Paste the full capture brief text into the prompt, or share the document if the model supports file upload.
- Run all three passes in the same session to keep context consistent.
- Log the model used, date, and key findings in `05_decision-log.md`.
- After red-team: if fewer than 2 findings, brief may be ready. If more than 2, it's not.
- This step happens in Week 4 (Day 2) of the monthly cadence, before human review.

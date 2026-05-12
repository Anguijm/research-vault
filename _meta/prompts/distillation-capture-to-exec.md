---
type: prompt
name: distillation-capture-to-exec
recommended_model: claude
last_revised: 2026-05-10
---

# Distillation — capture brief → executive brief

**When to use:** Week 4 (Day 4) of the monthly cadence, after the capture brief has passed adversarial review. Write the executive brief last — distill ruthlessly from the capture brief; do not draft independently.

**Recommended model:** Claude (stronger at ruthless compression and long-form analytical prose).

**The prompt:**

```
Here is a 12-page capture brief. Distill it into a 1-page executive brief
for a defense pure-play exec who reads on a phone.

Constraints:
  - BLUF first: 3–5 sentences. The opportunity, the recommendation, the ask.
  - "Why it matters" — 3–5 bullets.
  - Recommendation — 2–3 bullets.
  - Top risks — 2–3 bullets.
  - Asks — 2–3 bullets.
  - No methodology section. No bibliography. No hedging.
  - Prose with bullets, not all bullets. One chart maximum.
  - Cut anything not decision-relevant. If in doubt, cut it.

Maintain the fact / assessment / speculation labels from the source.
```

**Notes:**
- Paste the full capture brief text, or the `Internal` sensitivity sections specifically (the exec brief is internal by default).
- After generating the draft, populate the `executive-brief-template.docx` from `_templates/` — do not send a raw markdown output to the exec.
- The exec brief is always derived from the capture brief. Never write the exec brief first.
- Save the final file as `executive-brief-v1.0.docx` in `04_artifacts/`.

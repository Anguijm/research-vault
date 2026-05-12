# Prompt library

Six reusable prompts for the monthly capture brief cycle. One file per prompt.

## Model recommendations

| Prompt | Model | Why |
|---|---|---|
| `source-gathering.md` | Gemini | Broader/fresher web reach across DVIDS, .mil, trade press |
| `quote-extraction.md` | Claude | Better "verbatim with attribution" discipline |
| `cross-ai-red-team.md` | The OTHER one | Cross-model disagreement is the value — always use the model you didn't draft with |
| `distillation-capture-to-exec.md` | Claude | Stronger at ruthless compression |
| `poc-extraction.md` | Claude | Better at structured extraction from .mil pages |
| `weekly-scan.md` | Gemini | Broader web reach for opportunity discovery |

## When to use which prompt (monthly cadence)

**Week 1 — Triage:**
→ `weekly-scan.md` — surface new opportunity signals, pick focus for the month

**Weeks 2–3 — Research:**
→ `source-gathering.md` — broad gather across primary sources for the focus opportunity
→ `quote-extraction.md` — per source, after click-verifying the URL
→ `poc-extraction.md` — per source that contains named people

**Week 4 — Distill and ship:**
→ `cross-ai-red-team.md` — after producing capture brief v0.1, before human review
→ `distillation-capture-to-exec.md` — after capture brief passes adversarial review

## Important reminders

- Never use AI output without clicking every link (Rule 6 in `_meta/verification-rules.md`).
- The cross-AI red team is not a substitute for a human adversarial review — it's a fallback.
- `poc-extraction.md` and `weekly-scan.md` are stubs — add full prompt bodies from your own practice after 2–3 manual runs.

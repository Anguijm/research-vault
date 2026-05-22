---
type: skill
name: grill-me
purpose: Force shared understanding between operator and Claude before any non-trivial work begins
when_to_invoke: Before scaffolding a new opportunity, before drafting a new brief or a new brief version, before starting any work that will produce a durable artifact in the vault
last_revised: 2026-05-22
---

# Grill me — alignment skill

This is the alignment skill for the vault. Invoke it whenever Claude is about to commit to a piece of work that will produce a durable artifact — a folder, a brief, a play card, a long decision-log entry. The point is to surface every assumption Claude is about to make on the operator's behalf so the operator can correct or confirm them before any markdown gets written.

The skill exists because of a repeating pattern in this vault. The operator says "do X," Claude scaffolds X, and only later — sometimes in the next session — do we discover that X needed three decisions and a scope clarification that nobody made up front. The fix is to push the questions to the start of the work, not the end.

The skill is named after Matt Pocock's open-source Claude Code skill of the same name, which is the source of the technique.

## How Claude should behave

When this skill fires, do not start scaffolding, drafting, or editing yet. Interview the operator until a shared mental model exists.

Cadence: ask between three and ten questions at a time using `AskUserQuestion` for the multiple-choice ones and plain chat for the open-ended ones. Wait for answers. Ask the next batch. Keep going until you can recite the plan back in your own words and the operator agrees with the recitation.

The questions below are the **starter set**. They are the minimum, not the maximum. Add follow-up questions whenever an answer reveals an ambiguity, a constraint, or a downstream choice that has not been made. Stop only when you can answer "what am I about to build, why, for whom, and what would tell us it is wrong" without hedging.

If the operator's confirmation on a specific question is "sure," "I guess," "whatever," or any other hedge — that is not alignment. Re-ask the specific question whose answer was hedged, or break it into smaller sub-questions. Hedge answers are the source of after-the-fact decision logs.

Do not let the operator skip alignment. If they push you to start without it, push back once, briefly. If they insist, capture the unanswered questions in a `_open-questions.md` file in the folder you are about to build, so the questions survive into the work rather than getting lost.

## Starter questions for a new opportunity

These are the minimum questions before scaffolding a new opportunity folder. Use them as the first batch and add follow-ups based on the answers.

**Identity and scope:**
1. What is the folder identifier? Standard pattern is `OPPORTUNITY-CUSTOMER` per `HANDOFF.md` §3, but a deliberate deviation is allowed if the operator can explain why.
2. Who is the named customer? If multi-customer or unknown, what are the candidate customers and how will the field be resolved later?
3. What gate is this at — identify, pursue, bid, won, lost, or dropped?
4. What status — triaged, research, drafting, review, shipped, or stalled?

**Hypothesis and falsifiers:**
5. State the working hypothesis in one sentence. If the operator cannot, the opportunity is not ready to scaffold yet.
6. What evidence would falsify the hypothesis? Minimum two pieces, ideally from primary sources.
7. Which disconfirming sources should be pulled **first** to test the hypothesis early?

**Boundaries:**
8. What is explicitly out of scope? Reference `HANDOFF.md` §11 if applicable.
9. What sensitivity tier — internal, shareable, public — does the work need to respect?
10. Are there existing research tracks this should cross-link to? Are there any tracks this should explicitly **not** touch?

**Outputs and audience:**
11. What deliverable is this aiming at — capture brief, executive brief, play card, internal research only, or a customer-education paper?
12. Who is the audience for the deliverable?
13. When does the deliverable need to ship?

**Resource posture:**
14. How much operator time is available for this in the next 30, 60, and 90 days?
15. What is the budget for AI quota burn? `find_sources.py`, `verify_facts.py`, and `red_team.py` are not free.
16. Should `auto_find` be `true` or `false` at scaffold time?

## Starter questions for a new brief (or new brief version)

Use this list when the operator says "draft a brief" or "next version" of an existing brief, before drafting:

1. Which sections from the template are load-bearing for this audience, and which can be cut?
2. What FACT claims has the operator already verified for this version? Which still need verification?
3. What red-team passes have been run on prior versions? What were the top unresolved findings?
4. What is the target page count and the target audience reading level?
5. Are there explicit changes to the section structure since the last version?
6. What is the version-number convention for this opportunity?
7. Are there any decisions in `_decisions-pending-*.md` that block this version? If so, are they resolved or do we draft around them?

## When alignment is reached

Recite the plan back to the operator in your own words. Get explicit confirmation. Only then proceed to scaffold or draft. The recitation is what closes the alignment — it forces the operator to read what you heard, not what they meant.

Capture the final answers in the decision log of the resulting folder, so the alignment record is durable. The decision log entry should reference this skill by name so future sessions know the alignment was done deliberately.

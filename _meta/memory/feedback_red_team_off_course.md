---
name: Cross-AI red-team can pull operator brainstorms off-course
description: Iterative Gemini red-team often produces decisive, authoritative-sounding pivots that can override operator strategic intuition. Treat critique as input, not directive.
type: feedback
originSessionId: 254eda7f-7db4-4f93-b460-1e14e2726754
---
When running iterative red-team dialogue with Gemini (or any external LLM critique), Gemini's output is decisive and prescriptive — "stop doing X, do Y instead." Because the framing is confident, Claude tends to capitulate to the red-team conclusion even when the operator's original brainstorm had real strategic merit the red-team missed.

Concrete instance: 2026-05-31. Operator proposed building a CACI corporate capability book. Three rounds of Gemini red-team argued the corporate book was "strategic distraction" / "productivity theater" and pivoted to a narrower "Contract Vehicle Boundary Box" alternative. Claude synthesized the red-team conclusion and presented it back. Operator then pushed back: "it feels real wrong" — and was correct. The red-team had conflated query-layer with scoring-layer, and missed the operator's role as a relationship-lead between team-on-the-ground and CACI-corporate-capabilities. The corporate capability book had a real distinct job (scoring layer) that the red-team's framing dismissed.

**Why:** Gemini's training favors decisive recommendations. Three rounds of decisive recommendations compound — by Round 3, the red-team conclusion feels overdetermined. Claude's instinct to "synthesize what the red-team said" amplifies this rather than weighing it against the operator's original strategic intent.

**How to apply:** When running iterative red-team:
1. Before accepting a Gemini conclusion, explicitly check it against the operator's stated goal and intuition. If the conclusion contradicts the operator's instinct, the contradiction itself is a signal — investigate WHERE the red-team's framing diverged from the problem the operator was solving.
2. Surface red-team conclusions as "Gemini argues X" rather than "the correct answer is X." Preserve the operator's ability to push back.
3. Watch for the specific failure mode of conflating layers — query layer vs scoring layer, execution scope vs relationship scope, tactical vs strategic. Red-teams often collapse distinct layers in pursuit of a clean recommendation.
4. The operator's "it feels real wrong" is a high-signal phrase. Take it seriously and re-examine the synthesis, not just argue back.

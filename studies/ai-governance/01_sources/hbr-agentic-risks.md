---
type: source
study: ai-governance-landscape
title: Organizations Aren't Ready for the Risks of Agentic AI
author: Reid Blackman
publisher: Harvard Business Review (Digital Article, Risk Management)
publication_date: 2025-06-13
reprint: H08S2Z
url: https://hbr.org/2025/06/organizations-arent-ready-for-the-risks-of-agentic-ai
local_pdf: hbr/hbr-agentic-risks-2025-H08S2Z.pdf
captured: 2026-06-19
source_tier: 1
classification: internal
verified: 2026-06-19 (full text read from operator-provided PDF)
content_sha256: e72843e3231b9dc359bdf2a9f9f7f82e46dd6f9d1b751756cc2a7215304dccf6
backfilled_hash: true
---

# Organizations Aren't Ready for the Risks of Agentic AI (HBR, Blackman, 2025)

Full text, read from the operator's subscription PDF. This replaces the earlier
abstract-only capture. Quotes below are verbatim from the PDF.

## Summary

**Assessment.** Blackman's thesis: AI risk programs were built for "narrow AI" and
rest on four assumptions that progressively break as you move to generative AI and
then to agentic AI. He frames the work as "The Ethical Nightmare Challenge" and lays
out a five-stage complexity staircase from a single model to cross-organization
multi-agent systems, then names six things that get harder at each step up. The
practical message is to honestly locate yourself on the staircase and build the
infrastructure for your current stage before climbing to the next.

## FACT — quoted (verbatim)

- Definition of agents: AI chatbots and image generators "are becoming AI 'agents'—AI systems that can execute a series of tasks without being given specific instructions."
- The Ethical Nightmare Challenge asks leaders to: "Identify the ethical nightmares for their organizations that may result from wide-scale AI use"; "Create the internal resources that are necessary for nightmare avoidance"; "Upskill employees so they can use those resources, along with their updated professional judgment, to avoid those nightmares."
- "Agentic AI makes rising to this challenge more urgent: It introduces compounding risks that, if not managed, can create business and brand-defining disasters."
- On training: intervention requires "training that goes well beyond annual 30-minute compliance video watching… Specialized training is needed at least at the department level and in many cases at the role level."
- "Moving from Stage 1 to Stage 5 without the proper infrastructure isn't innovation—it's recklessness."

## FACT — paraphrased

**The four assumptions narrow-AI risk programs were built on** (and which break later):
1. The context of use is understood in advance.
2. Data-science expertise is on hand to perform risk assessments, monitor performance, and explain how the AI works.
3. There is usually an expert "human in the loop" checking outputs before they are acted on, at a pace a human can handle.
4. Monitoring and intervention are relatively straightforward — if the model performs poorly you stop using it, and the disruption is contained.

**What changes with generative AI:** contexts of deployment explode (testing "how will it perform in the intended context" becomes very hard); monitoring in the wild becomes immensely important; the human in the loop still works but needs more training (hallucinations); responsible prompting is needed (e.g., "not putting company sensitive data into an LLM that sends the data to a third party"); risk assessment happens in more places (models are procured from Microsoft, Google, Anthropic, OpenAI with generic mitigations; modifying a pre-trained model creates new assessment needs at multiple, unclear points).

**The five-stage complexity staircase:**
- Stage 1: an LLM connected to another generative AI → *multi-model AI*.
- Stage 2: an LLM connected to ~30 databases, ~50 narrow AIs, ~5 generative AIs, and the open internet.
- Stage 3: add the ability to take digital actions (e.g., perform financial transactions) → *multi-model agentic AI*.
- Stage 4: the ability to talk to other multi-model agents inside your organization → *internal multi-model multi-agentic AI*.
- Stage 5: the ability to talk to AI agents outside your organization → "a head-spinning quagmire of incalculable risk."

**The six things that get harder as you climb** (why the challenge intensifies):
1. Deciding who performs what risk assessment, and when — a risk assessment at every node is "pragmatically impossible," so cost/benefit analysis against risk appetite is required.
2. The human in the loop's ability to "wisely stand between system outputs and impacts decreases drastically" — too much data to process in real time.
3. Enormous weight falls on go/no-go (pre-green-light) decisions, which presuppose people know how to test and evaluate systems before approval; "most organizations lack these critical pre-deployment evaluation frameworks."
4. Real-time monitoring becomes of tremendous importance ("without real-time monitoring, the pace at which things can unravel is diabolical").
5. Intervention methods must be designed for when "the light starts blinking red," ideally minimally disruptive (shut off the offending model node rather than the whole system, though some risks force a full shutdown).
6. Upskilling employees, continuously and at department/role level, is essential; "the most successful companies… invested and continue to invest heavily in employee training before deploying the technology, not after problems emerge."

## Assessment (relevance to this study / SRF-JRMC context)

- The staircase reframes "agentic" as a spectrum, not a binary. **Assessment:** an askSage deployment that only retrieves and drafts sits low on the staircase; one wired to take actions or talk to other agents climbs fast, and the governance must climb with it. This matches the OWASP/CSA "raise governance to match the most advanced agent you run, or lower the deployment tier" idea in `[owasp-state-agentic-gov]`.
- Point 3 (most orgs lack pre-deployment evaluation frameworks) and the training argument both reinforce the independent-evaluation/validation gap flagged elsewhere in this study.

## Cross-references

- Pairs with `[hbr-rai-checklist]` (same lead author; the "what to build" companion).
- Reinforces agentic controls in `01_sources/stream-3-agentic.md` (HITL breakdown at scale; intervention/kill design; monitoring).

## Source note

Author Reid Blackman is founder/CEO of Virtue (an AI-governance advisory firm) and
author of *Ethical Machines*. Single-author opinion/practitioner piece, not empirical
research — weight accordingly.

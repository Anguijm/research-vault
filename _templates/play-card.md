---
type: play_card
opportunity: OPPORTUNITY-ID
play_number: N
play_name: Short headline name
posture: prime | sub | partner
status: ideation | scoping | capture-authorized | bidding | won | lost | dropped
tam_range_usd: low-high   # e.g. 10000000-50000000
capture_probability: low | medium | high
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
linked_brief: capture-brief-vX.Y-draft.docx §N.N
linked_decisions: _decisions-pending-YYYY-MM-DD.md (decision letters)
---

# Play N — [Short headline name]

Single-page operator reference for one prime/sub/partner play within an
opportunity. Lives next to the capture brief in the opportunity folder.
Update on every brief revision or decision-memo change. Re-cite the linked
sections so the play card stays consistent with the brief.

## What the customer wants

[Quote the specific customer-stated demand signal — verbatim where possible —
with a `[s.xxx]` citation to the ingested source.]

> *…verbatim or near-verbatim customer language…*
> — [citation tag]

[1-2 sentence translation of what the demand actually requires from industry.]

## What we actually bring (per ingested primary sources)

| | |
|---|---|
| **Product / capability** | [Specific product name(s), not generic categories] |
| **Software** | [Specific software, with vendor's actual marketing language quoted] |
| **Customers / track record** | [Reference customers; flag if names are TBC] |
| **Financials (acquisition / contract value)** | [Cite primary source] |
| **What we do NOT bring** | [Be explicit about scope limits — what the red-team would catch if we overclaimed] |

## The play

**Headline:** [One-sentence positioning. What we propose to deliver, to whom, via what mechanism.]

**Constraining principles:**

1. [Principle that bounds the pitch — e.g., "No integration claims for X months"]
2. [Scope principle — "Stay in lane Y, don't bridge to Z"]
3. [Process principle — "X reviews and signs off before external use"]

## Vehicle / pathway

```
[Procurement vehicle name]
        ↓
   [What it does / who issues it]
        ↓
   [Our role in the flow]
        ↓
   [What it leads to long-tail]
```

## 30-day move

| | |
|---|---|
| **Primary contact** | [Named person, role, warm-intro path if any] |
| **Goal of the meeting** | [Concrete outcome — not "build relationship"] |
| **Parallel contact(s)** | [Other people to touch in same window] |
| **Prerequisite** | [What MUST happen before the meeting] |
| **Deliverable** | [Specific artifact — pitch deck / white paper / etc.] |

## 90-day move

1. [Concrete deliverable #1]
2. [Concrete deliverable #2]
3. [Concrete deliverable #3]

## TAM (cite §10 of brief if exists)

| | Range | Confidence |
|---|---|---|
| Floor — [scenario] | $XM | low/medium/high |
| Ceiling — [scenario] | $X–$YM | low/medium/high |

## Constraints to enforce (red-team-grounded)

| Don't say | Why |
|---|---|
| ["Overclaim 1"] | [Red-team finding that proved this is exploitable] |
| ["Overclaim 2"] | [Customer-credibility risk] |
| ["Buzzword"] | [Customer flagged as marketing] |

## Risks + mitigations

| Risk | Mitigation |
|---|---|
| [Competitor exploit angle] | [Specific defense] |
| [Internal execution risk] | [What/who blocks it] |
| [Customer-side risk] | [What we can control vs. what we accept] |

## What success looks like

- **30 days:** [Concrete milestone]
- **90 days:** [Concrete milestone]
- **180 days:** [Decision point — proceed / pivot / kill]
- **12 months:** [Revenue / capture metric]

## Open questions (gating answers)

- [Question 1 — what answer unblocks what part of the play]
- [Question 2 — gating decision elsewhere in the vault]

## Linked artifacts

- Brief: [[04_artifacts/...|capture brief]] §N.N Play X
- Decisions: [[_decisions-pending-...|decision letters]]
- Source citations: [[00_research-file#§X.Y|research file section]]

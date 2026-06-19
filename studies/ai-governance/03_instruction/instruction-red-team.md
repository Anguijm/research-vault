---
type: red-team
study: ai-governance-landscape
title: Red-team (logic pass) — instruction rewrite v0.1
classification: internal
created: 2026-06-19
red_team: Gemini (flash, high reasoning) via gemini MCP
focus: logic, internal consistency, enforceability, structure, military form — NOT gap-hunting
discipline: per _meta/memory — input not directive; date-of-knowledge fenced (Gemini told not to relitigate 2026 facts); named-entity/code claims not asserted without command confirmation
---

# Red-team logic pass on instruction v0.1

Gemini was pointed at logic/consistency/enforceability/structure/military-form, with an
explicit date-of-knowledge fence (do not relitigate GenAI.mil, DoDI 5400.19, the CDAO
2024 guidance, OMB M-25-21). It returned nine findings; all nine accepted, several with
terminology corrections applied here. Results folded into **instruction-v0.2.md**.

| # | Finding | Disposition / fix in v0.2 |
|---|---------|---------------------------|
| 1 | **LN/ITAR cross-caveat loophole.** A centrally-indexed knowledge base could hold NOFORN/ITAR data; an agent acting for a Local National user could synthesize an "unclassified" output derived from caveated data the user can't hold. The "agent inherits user access" control doesn't cover the shared index. | **ACCEPT in v0.2, then LIGHTENED in v0.2.1 by operator context.** v0.2 built an access-segmented index. **Operator update 2026-06-19:** NOFORN is already barred from the SRF-JRMC share and all technical direction is screened by a derivative classifier before reaching the share, so the AI corpus is already releasability-screened. v0.2.1 §5.c/§7.c now INHERIT that existing control rather than rebuild it; the only residual is "index only the screened corpus; no un-screened uploads" (don't let the AI bypass the screener). Good example of finding-was-valid-in-the-abstract but already-mitigated-upstream. |
| 2 | **CHENG vs. Department Head authority collision.** A Dept Head could approve a "productivity" use case that is actually technical, bypassing the CHENG. | **ACCEPT.** v0.2: Dept Heads **propose**; CHENG **concurs** on any use case touching technical specs, tag-outs, work-authorization, or quality; CIO validates platform/security. *(Gemini's "Code 900/Code 200" not asserted.)* |
| 3 | **Verification loophole.** "Verify against the controlling doc" can be satisfied by reading the AI's own retrieved snippet — circular, defeats hallucination control. | **ACCEPT.** v0.2: verification must be **out-of-band** — the human opens the controlling document through a non-AI authoritative source; the AI's own snippet is not sufficient. *(Gemini's "ATIS" generalized to "official technical library/authoritative source.")* |
| 4 | **PII/PHI prohibition is a "pinky-swear" without architecture.** "Don't enter PII" fails an audit. | **ACCEPT.** v0.2: CIO implements **Data Loss Prevention / sensitive-pattern interception at the prompt-ingress layer** (to the extent the platform supports it), aligned with enterprise guardrails — prevention, not only ConMon detection. |
| 5 | **Records vs. spillage deadlock (internal contradiction).** Records says retain all prompts as Federal Records; Incidents says "don't delete" a spill. Combined, a classified spill becomes a permanent classified record inside the IL5 store, which is a worse spill and hard to purge. | **ACCEPT — sharpest find.** v0.2: "don't delete" is the immediate forensic step; the spilled record is then **isolated and routed to the formal spillage-cleanup / emergency records-destruction process after Security Manager + Legal adjudication**. *(Gemini cited 36 CFR 1229 — included as [verify citation], not asserted.)* |
| 6 | **DDIL fallback is aspirational without a check.** | **ACCEPT.** v0.2: add a **quarterly manual-reversion certification** by Department Heads. *(Gemini's "Condition Zebra" is afloat damage-control, not a shipyard connectivity state — generalized to "loss of connectivity / contingency.")* |
| 7 | **Knowledge Base is misplaced at the end.** It is central to technical authority and hallucination control. | **ACCEPT.** v0.2 reorders: Authorized/Prohibited Data → **Knowledge Base** → Technical Authority. Flow: what data → where the official data comes from → who has authority. |
| 8 | **"Combination of people, not one owner" is corporate-speak; Navy assigns a single point of accountability.** | **ACCEPT, reconciled with operator.** The operator said management is "a combination of folks"; Gemini says assign single accountability. Both hold: v0.2 frames the **Commanding Officer as the accountable authority** (Navy form) while **responsibilities are distributed** across CIO (platform/security), CHENG (technical accuracy), Legal (records/labor), Dept Heads. Honors the operator's intent in proper instruction form. *(ED noted as a delegation option, not asserted.)* |
| 9 | **Token caps could deny mission work** during emergent/surge repair. | **ACCEPT.** v0.2 Annex A: caps are **fiscal planning, not operational denial**; CIO may reallocate/override for high-priority (Level I / emergent) work. |

## Discipline notes (what was filtered)
- No specific command code numbers asserted (Gemini guessed Code 200 / Code 900).
- 36 CFR 1229 (emergency records destruction) included as a citation to verify, not asserted as controlling.
- "ATIS" and "Condition Zebra" generalized (out-of-context for this use).
- Finding 8 reconciled toward the operator's stated "combination of people" rather than overriding it.
- Gemini did not raise any stale-fact objection to the 2026 issuances; the date fence held.

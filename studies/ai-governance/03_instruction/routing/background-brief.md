# Background Brief — How this askSage governance package was built

*Context for the working group. One read so reviewers understand what they're looking at and why
the major calls were made. The full landscape report and the analysis records are included in /
available with this package.*

## Why this exists
SRF-JRMC is adopting **askSage**, an agentic AI platform (it reasons over multiple steps,
retrieves data across command processes, and can take actions), used alongside the DoD enterprise
platform **GenAI.mil**. Agentic AI in a safety-of-life, OCONUS industrial command needs
governance that protects information security, the technical authority chain, seaworthiness, and
compliance — without smothering the productivity gain. This package is that governance, plus the
pilot, the per-department plan, and the training to stand it up.

## The standard we measured against (the landscape)
An open-source review of how the military, large corporations, federal civilian agencies, and
regulated industries govern AI found a consistent backbone — **seven primitives** (a named
accountable owner + a standing governance body; an AI use-case inventory bound to a risk tier;
risk-proportional controls; human review before consequential action; strict data-handling
boundaries; lifecycle monitoring; independent challenge/audit) and, for agentic tools, **five
added controls** (autonomy tiered to oversight; least-privilege write-gating; runaway/cost
control; per-agent identity + observability; a kill switch). The instruction implements all of
these through *existing* Navy structures rather than new ones. (Full detail: the landscape
report, included.)

## How the draft was built (iterative, adversarial)
The instruction went through eleven drafts. The path: an initial AI-generated draft → a gap
analysis against the landscape standard → a multi-round adversarial red-team (a logic/consistency
pass that caught real contradictions) → reconciliation of a second AI advisory (whose facts were
verified against primary sources and USASpending, and whose two risky recommendations were
rejected) → a final whole-package red-team. References were verified against the issuances; the
acquisition/authority basis was confirmed against federal award data.

## Decisions already made (please don't relitigate without a substantive reason)
- **Two platforms:** GenAI.mil for general questions, **askSage for agentic work**.
- **Data:** CUI up to IL5 **yes**; classified, NNPI, PII, PHI **no** (firm command decisions).
- **AI is decision support, not authority:** evaluated by the cognizant authority along existing
  lines of responsibility; the AI changes no existing process.
- **Governance through existing command structures** — no new boards; the Department Heads are
  the governance forum.
- **Federated knowledge base:** each code owns/feeds its repository; Code 200 owns the technical
  library and screening; CIO/ISSM is the platform custodian.
- **Per-department evaluator and information-governance plan** before access; **pilot first**
  (read-only) to validate before promulgation.

## What's left for the working group
The draft carries visible **"Working group to resolve"** / **[CONFIRM]** markers for the
command-specific items: the instruction's SSIC and number (Code 1100 assigns — 5239 vs 5230);
the command's local references (its SORM, its spillage SOP); the cognizant Security
Classification Guide(s); the source-of-record system for verification; the Foreign Disclosure /
export-control authority; the specific billet delegations; and adoption of the departmental-plan
template. The cover/comment sheet lists these for resolution.

## What's in this package
The cover/comment sheet, this background brief, the landscape report (reference), the draft
instruction, the pilot authorization memo, the departmental information-governance plan template,
and the training plan.

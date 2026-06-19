---
type: synthesis
study: ai-governance-landscape
title: AI Governance Landscape — what military and corporate organizations actually do
status: draft v0.1
classification: internal
created: 2026-06-19
sources: ../source-ledger.md
---

# AI Governance Landscape

This report documents how other organizations govern artificial intelligence (AI):
the U.S. military, large corporations, cross-industry standards bodies, regulated
industries, and the civilian federal government. It is a landscape, not a
recommendation. It deliberately does not grade or rewrite any draft instruction;
mapping these findings onto a specific SRF-JRMC policy is a separate later pass.
The aim is narrow and useful: before you write your own AI governance policy, see
the shape of the ones already in the field.

**Labeling.** A statement that "Organization X does Y" is a **FACT** when a cited
source says so; the citation slug (for example `[nist-ai-rmf]`) resolves in
`../source-ledger.md`, and the full quote lives in the matching `01_sources/`
file. Anything that is my reading of the pattern is marked **Assessment**.
Unconfirmed leads are marked **Speculation / unverified** and must not be treated
as fact. Two honesty notes carried from the research: McKinsey article bodies could
not be retrieved (their claims here are from McKinsey's own search abstracts, not
full text, and are flagged for you to pull behind your subscription), and several
primary `.mil`/`.gov` pages hard-blocked the fetcher, so a few items rest on
reputable secondary sources that quote the primary. See the reliability section.

---

## TL;DR — the seven things everybody does

**Assessment.** Across military, corporate, federal, banking, and healthcare
sources, the same seven governance primitives recur. The vocabulary differs by
sector, but the machine underneath is strikingly consistent. If there is one
takeaway, it is that mature AI governance is not a document, it is these seven
standing functions:

1. **A named accountable owner plus a standing governance body.** A single
   senior person who owns the policy (Chief AI Officer, Authorizing Official,
   model-risk head), sitting over a cross-functional committee that meets on a
   set cadence. `[dod-caio-statement]` `[omb-m-25-21]` `[diligent-ai-gov]`
   `[nist-ai-rmf]` `[sr-11-7]`
2. **An inventory of AI use cases, bound to a risk tier.** You cannot govern what
   you have not catalogued. Every regime keeps a register and classifies each
   entry by risk so controls scale to consequence. `[omb-m-25-21]`
   `[diligent-ai-gov]` `[sr-11-7]` `[eu-ai-act]`
3. **Risk tiering that drives proportional controls.** Light touch for low-risk
   uses, hard gates and extra review for high-risk ones. The EU writes this into
   law; enterprises and agencies mirror it internally. `[eu-ai-act]`
   `[omb-m-25-21]` `[sg-model-ai-gov]`
4. **Human review before consequential action.** A person validates or approves
   before a high-stakes output is used or released. `[omb-m-25-21]`
   `[dodi-5400.19]` `[anthropic-agent-framework]` `[sg-model-ai-gov]`
5. **Strict data-handling boundaries.** What data may enter which system, set by
   sensitivity, with a bright line against pouring protected data into tools that
   are not authorized for it. `[dodi-5400.19]` `[navy-genai-mil]`
6. **Lifecycle monitoring, not one-time sign-off.** Approval is a gate, then
   continuous monitoring watches for drift, degradation, and new failure modes.
   `[gao-21-519sp]` `[fda-ai-device]` `[sr-11-7]` `[nist-ai-rmf]`
7. **Independent challenge and audit.** Someone separate from the builder can
   question, validate, and if needed halt the system, with audit trails to make
   that possible. This is the function that most distinguishes a mature regime
   from a checklist. `[gao-21-519sp]` `[sr-11-7]`

**Assessment.** The agentic layer (Section 4) adds a further set of controls that
ordinary chatbot governance does not need: per-agent identity, write-action
gating, runaway-loop and cost brakes, and agent-speed kill switches. Those are the
controls most specific to an askSage-class platform.

---

## 1. The military: one authority, five principles, a hard data line

**The U.S. Department of Defense (DoD) runs AI governance as hub-and-spoke: a
single office sets policy, the components execute.** The Chief Digital and
Artificial Intelligence Office (CDAO) is the DoD lead for AI policy and oversight,
and the CDAO is explicitly named as the Department's Chief AI Officer (CAIO); the
CDAO Council is described as "the DoD's AI governance body." `[dod-caio-statement]`
`[dod-rai-strategy]` The stated operating model is "centralized coordination of
RAI policies and guidance with decentralized execution." `[dod-rai-strategy]`

**FACT.** The normative spine is the five DoD AI Ethical Principles, adopted
February 2020: Responsible, Equitable, Traceable, Reliable, and Governable.
`[dod-ai-ethical-principles]` Two of these do governance work directly.
"Responsible" hard-codes human accountability ("DoD personnel will exercise
appropriate levels of judgment and care, while remaining responsible for the
development, deployment, and use of AI capabilities"). "Governable" requires a
built-in off-switch ("the ability to disengage or deactivate deployed systems that
demonstrate unintended behavior"). `[dod-ai-ethical-principles]` The Responsible AI
(RAI) Strategy and Implementation Pathway (2022) turns the principles into six
Foundational Tenets, each broken into Lines of Effort with an assigned Office of
Primary Responsibility. `[dod-rai-strategy]`

**On generative AI specifically, the pattern has been pilot-then-codify.** The DoD
stood up Task Force Lima (August 2023) to study generative AI and large language
models, then sunset it (December 2024) and federated the work to standing offices,
launching an AI Rapid Capabilities Cell to scale adoption. `[tf-lima-charter]`
`[tf-lima-execsum]` `[ai-rcc]` The current acceptable-use rule set with real teeth
is DoD Instruction 5400.19 (effective July 2025), which governs public-affairs use
of AI and states the bright line plainly: "Commercial AI solutions outside of the
DoD's control are not authorized for any non-public information." `[dodi-5400.19]`
It also requires pre-use assessment, continuous monitoring, human oversight and
approval of generative outputs before public release, provenance labeling, and
reporting of anomalous outputs to the Component Chief Information Officer.
`[dodi-5400.19]` Authorization runs through the DoD Risk Management Framework, with
the Authorizing Official as the accountable decision-maker and AI-specific threats
(data poisoning, inference attacks, model drift) named for monitoring.
`[dod-ai-cyber-rmf]`

**The most concrete recent development is platform consolidation.** The DoD is
collapsing service-specific tools onto a single CDAO-governed platform,
GenAI.mil, with all tools certified for Controlled Unclassified Information (CUI)
and Impact Level 5 (IL5), under enterprise contracts with four frontier vendors
(Anthropic, OpenAI, xAI, Google). `[dod-genai-mil-rollout]` The Department of the
Navy mandated transition to GenAI.mil by April 30, 2026, and the platform prohibits
protected health information and personally identifiable information even at IL5.
`[navy-genai-mil]` The Air Force's NIPRGPT and the Army's CamoGPT are being folded
in. `[niprgpt-sunset]`

**Assessment, and directly relevant to your situation.** The Army provides the
closest public analog to what SRF-JRMC is doing. In 2025 the Army CIO blocked the
Air Force's NIPRGPT from Army networks over data-governance concerns, then stood up
its own Enterprise LLM Workspace powered by **Ask Sage**, accredited for CUI with
an IL5 / FedRAMP-High Authority to Operate, and governed partly through
**token-based billing controlled by the CIO**, where releasing tokens is the
access-control lever. `[army-camogpt-asksage]` That is the same platform family and
the same token-budget control vector your draft contemplates, already running
inside a DoD component. The Army CIO's framing of accountability is worth keeping:
"If you're using an AI tool, it doesn't absolve you from meeting those
requirements." `[army-camogpt-asksage]` (A caveat against over-reading this: the
DoD-wide direction is toward GenAI.mil as the single platform; a command standing
up a separate askSage instance should understand how that squares with the
consolidation push. That is a strategic question for you, flagged not answered.)

**Reliability note for this section.** The Department of the Navy CIO's own
generative-AI memos could not be fetched (the doncio.navy.mil site hard-blocks
automated retrieval); the Navy specifics above rest on the Naval Postgraduate
School library guide and defense trade press that quote those memos. Verify exact
wording against the memos before quoting them as primary. `[don-genai-guidance]`

---

## 2. Corporations: a board-backed committee, an inventory, federated execution

**Large enterprises converge on a standing governance body plus a named executive
owner, increasingly at the very top.** The recurring corporate structure is a
board-approved AI policy and risk appetite, a cross-functional committee (risk,
legal, compliance, data, security, business) meeting monthly, and a single
accountable executive per high-risk system. `[diligent-ai-gov]` McKinsey's survey
data (from its abstract, pending your full-text pull) reports that 28 percent of
respondents say the CEO oversees AI governance and that CEO oversight is the single
governance element most correlated with earnings impact from generative AI.
`[mck-state-of-ai]` The Chief AI Officer role is institutionalizing this ownership.
`[caio-role-pattern]`

**The dominant operating model is "centralized governance, federated execution."**
A central risk or compliance function sets enterprise policy and provides
challenge, while business, legal, IT, and data teams own implementation across the
AI life cycle. `[mck-trust-maturity]` Microsoft is a documented worked example: a
central Office of Responsible AI owns the standard and the mandatory impact
assessment, a Responsible AI Council acts as the governance body, and "Responsible
AI Champions" are embedded in each division as reviewers. `[microsoft-rai-standard]`
Microsoft also requires an impact assessment completed early, at product vision,
and review gates for sensitive uses. `[microsoft-rai-standard]`

**The frameworks everyone maps to are NIST, ISO, and the EU AI Act.** The U.S.
National Institute of Standards and Technology AI Risk Management Framework (AI RMF
1.0, 2023, plus a Generative AI Profile in 2024) organizes the work into four
functions, Govern, Map, Measure, and Manage, with Govern as the cross-cutting
function "infused throughout" and senior leadership setting "the tone for risk
management." `[nist-ai-rmf]` ISO/IEC 42001 (2023) is the certifiable management-
system standard: top-management commitment, a documented AI policy, AI risk and
impact assessments before deployment, lifecycle controls, third-party management,
and certification by independent third-party audit. `[iso-42001]` The EU AI Act
supplies the risk-tiering template in law: unacceptable-risk uses prohibited,
high-risk uses carrying the bulk of obligations (lifecycle risk management, data
governance, logging, human oversight, conformity assessment), limited-risk uses
needing only transparency, and minimal-risk uses unregulated. `[eu-ai-act]`

**Two HBR pieces frame the corporate posture.** A responsible-AI program is
described as enterprise-wide governance, not per-project guardrails: it "defines
the enterprise-wide policy, governance structures, roles and responsibilities,
processes, and more that enable wide-scale deployment of AI." `[hbr-rai-checklist]`
And a 2025 HBR piece argues bluntly that "organizations aren't ready for the risks
of agentic AI," because instruction-light, multi-step agents outrun existing risk
programs. `[hbr-agentic-risks]` Both are paywalled; abstracts captured, full text
is on your pull list.

---

## 3. The agentic layer: the controls a chatbot policy does not have

**This is the part most specific to askSage, because askSage is agentic.** An
agent that can plan, chain steps, retrieve data, and take actions needs governance
beyond "don't paste CUI into the chatbot." The research surfaces a coherent and
fast-maturing set of agent-specific controls, grouped below. **Assessment:** these
five clusters are the substance of agentic governance as the field currently
understands it.

**Autonomy tied to human oversight, matched to risk.** The cleanest model is a
tiered one: fully supervised agents whose every action needs human approval,
constrained-autonomy agents that execute pre-approved action types within scope and
escalate outside it, and fully autonomous agents for low-risk work.
`[csa-nist-rmf-agentic]` Crucially, the oversight level "is a property of the
decision, determined dynamically by risk," not a fixed setting for the whole
system. `[strata-hitl]` The three modes have standard names: human-in-the-loop
(approve before the action), human-on-the-loop (monitor and intervene), and
human-out-of-the-loop (autonomous). `[strata-hitl]` Good practice replaces a bare
"Approve?" prompt with a structured one ("intent, data lineage, permissions chain,
expected blast radius, rollback plan") and matches the approval time window to risk.
`[strata-hitl]` Anthropic's own agent framework states the principle: humans should
retain control "particularly before high-stakes decisions," with read-only
defaults and approval before an agent modifies systems. `[anthropic-agent-framework]`

**Least-privilege permissions and write-action gating.** Agents get only the
goals, tools, and data they actually need; high-impact or irreversible actions are
gated behind explicit human confirmation. `[teleport-agentic-mitigations]` An agent
acting for a user inherits that user's permissions and no more, with data-loss-
prevention so it cannot return data it should not. `[msft-agent-governance]` A
strong specific control: separate code generation from code execution, with an
approval gate between them, and run tools in sandboxes with egress control.
`[teleport-agentic-mitigations]`

**Runaway-loop and cost control.** This is the "token budget" problem stated
concretely. The engineering consensus is multi-layer brakes: a hard cap on
reasoning steps per task, a cumulative token or dollar budget that kills the run
when exhausted, no-progress detection (compare consecutive outputs; if too similar,
the agent is stuck), and an absolute wall-clock timeout. `[bswen-loop-control]`
"Single guards fail. Multi-layer defense works." `[bswen-loop-control]` On the
governance side, Microsoft's guidance is to track token and compute use per agent
and fire real-time alerts as spend approaches budget thresholds "to prevent
overruns." `[msft-agent-governance]` (Gartner reportedly now names "FinOps for
agentic AI" as a category; that is an unverified search lead, not confirmed.)

**Identity, observability, and a kill switch.** Give every agent a unique,
verifiable identity ("identity as the new control plane"), maintain a registry so
shadow agents can be found ("you can't govern agents you don't know exist"),
keep tamper-evident audit logs that attribute every action to a specific agent,
and watch runtime behavior for drift. `[owasp-state-agentic-gov]`
`[msft-agent-governance]` `[csa-nist-rmf-agentic]` Containment is increasingly
automated: the severe-incident pattern is "automated agent suspension or kill-
switch activation rather than relying on human-in-the-loop containment decisions,"
because at agent speed a human cannot react fast enough. `[csa-nist-rmf-agentic]`
`[owasp-state-agentic-gov]`

**Standards and threat catalogs.** The reference list for agentic risk is the
OWASP Top 10 for Agentic Applications 2026 (ten named risk classes including Agent
Goal Hijack, Tool Misuse, Identity and Privilege Abuse, and Rogue Agents) and its
companion governance report. `[owasp-agentic-top10]` `[owasp-state-agentic-gov]`
The emerging federal anchor is the NIST AI Agent Standards Initiative (announced
February 2026), covering agent identity, least-privilege tool access, and audit
attribution, with an interoperability profile targeted for late 2026.
`[csa-nist-agent-standards]` For ordinary (non-agentic) LLM apps, the OWASP Top 10
for LLM Applications 2025 is the controls reference, and two of its entries,
"Excessive Agency" and "Unbounded Consumption," are exactly the agentic autonomy
and cost problems. `[owasp-llm-top10]`

---

## 4. Regulated industries and federal civilian: the model-risk analog

**The most useful insight from this stream is that AI governance is not new, it is
an extension of model risk management.** Banking has governed quantitative models
for over a decade under Supervisory Letter SR 11-7 (2011), and that structure is
now being applied to machine learning and large language models. Its center of
gravity is "effective challenge": "the critical analysis of a model against its
objectives by informed, technically competent parties who can identify model
limitations and assumptions." `[sr-11-7]` It mandates independent validation by
people separate from the developers, with authority to force changes, plus a model
inventory, documentation, and a three-lines-of-defense structure (developers,
independent validation, internal audit). `[sr-11-7]`

**FACT.** That same lifecycle logic shows up in healthcare and federal civilian
governance. The U.S. Food and Drug Administration's draft guidance on AI-enabled
devices (January 2025) uses a Total Product Lifecycle approach, a nine-area
documentation set, bias mitigation through subpopulation testing, and a
Predetermined Change Control Plan that pre-authorizes a bounded set of post-market
model changes. `[fda-ai-device]` The Government Accountability Office's AI
Accountability Framework (2021) is built around four principles, Governance, Data,
Performance, and Monitoring, and is explicitly designed for auditors and third-party
assessors, not self-certification. `[gao-21-519sp]`

**The federal civilian rulebook is OMB Memorandum M-25-21 (April 2025), which
replaced M-24-10.** It requires each agency to name a Chief AI Officer, stand up an
AI governance board, maintain a public AI use-case inventory, and apply minimum
risk-management practices to "high-impact" AI, including human review before
deployment: "Agencies shall ensure that all high-impact AI systems receive
appropriate human review before deployment." `[omb-m-25-21]` The Federal Reserve
Board's published compliance plan (October 2025) is a concrete worked example of
turning that memo into an operating model: a CAIO with approval authority over
high-impact deployments, layered committees, the inventory used as the intake gate,
and impact assessments per high-impact case. `[fed-m25-21-compliance]` (DoD is
statutorily exempt from the federal use-case inventory mandate but has stated it
complies voluntarily and that its CAIO "will not, at present, be issuing any
waivers." `[dod-caio-statement]`)

**Assessment.** The recurring lesson here is that the function which separates a
mature regime from a paper policy is **independent validation and audit**. Banking
has it; the GAO framework is built around it; the FDA inserts an external regulator.
Where it is weakest, governance is judged weakest: a former FDA Commissioner is
quoted that "no health system in the United States is currently capable of
validating an AI algorithm once it's in use." `[hospital-ai-gov]` Any new policy
that names an owner and an inventory but has no independent-challenge function is,
by this standard, incomplete.

---

## 5. Where approaches diverge

**Assessment.** Two genuine forks are worth seeing, because they are choices a
policy author makes, not settled questions:

- **Prescriptive rules versus principles-led flexibility.** The U.S. federal,
  banking, and FDA regimes are prescriptive and enforceable within their sectors.
  The United Kingdom (five cross-sector principles applied by existing regulators,
  no new AI law) and Singapore (a voluntary, operational framework) are
  deliberately principles-based and pro-innovation. `[uk-pro-innovation]`
  `[sg-model-ai-gov]` Both converge on the same primitives; they differ on whether
  the controls are mandates or guidance.
- **Centralized control versus federated execution, and when to shift.** McKinsey's
  guidance to financial institutions is to start with a centralized oversight
  committee in early adoption and shift control to subcommittees as governance
  matures. `[mck-fi-genai-gov]` The maturity-model idea recurs in the agentic
  governance work too: score your governance capability against the complexity of
  the agents you are actually running, and either raise the governance or lower the
  deployment tier. `[owasp-state-agentic-gov]`

---

## 6. Reliability notes and unverified leads

**FACT about the research itself, kept visible per the vault's verification rules.**

- **McKinsey bodies were not retrieved.** The mckinsey.com origin blocked every
  fetch. All McKinsey claims here come from McKinsey's own search-result abstracts,
  not full article text. They read as consistent with the rest of the landscape,
  but treat them as leads until you pull the full text. The exact URLs are on the
  operator pull list. `[mck-state-of-ai]` `[mck-fi-genai-gov]` `[mck-trust-maturity]`
- **Several primary government pages hard-blocked the fetcher.** SR 11-7, the FDA
  device guidance, and the DON CIO memos were reached through reputable secondary
  sources that quote them (ModelOp, CenterWatch, the NPS library guide). Verify
  exact wording against the primaries before quoting as primary.
- **One fabricated citation was caught and discarded.** A research agent's first
  fetch of the GAO generative-AI report returned a wrong report number and invented
  quotes; it was re-verified against the real PDF and the bad version dropped. The
  GAO content here is from the verified document. `[gao-25-genai]`

**Speculation / unverified leads (do not cite as fact):**

- A 2026 revision of bank model-risk guidance, SR 26-02 with OCC Bulletin 2026-13,
  possibly superseding SR 11-7. This surfaced in two independent research streams,
  which raises its plausibility, but neither fetched the primary. `[sr-26-02]`
- An EU "Digital Omnibus" deferring the high-risk AI Act deadline from August 2026
  to December 2027. `[eu-digital-omnibus]`
- A later federal memo, M-26-04 on "unbiased AI principles" (December 2025).
- The figure that 26 percent of organizations now have a Chief AI Officer (an IBM
  study cited only in a snippet). `[caio-role-pattern]`

---

## 7. Operator pull list (your subscriptions)

These are the paywalled or un-fetchable items worth pulling with your McKinsey and
HBR subscriptions. URLs are exact in `../source-ledger.md`.

- McKinsey, "Managing the risks around generative AI" — the four-bucket risk model
  and the monthly responsible-gen-AI steering group. `[mck-managing-risks-genai]`
- McKinsey, "Implementing generative AI with speed and safety" — the control
  scorecard across business, procedural, manual, and automated controls.
  `[mck-speed-safety]`
- McKinsey, "How financial institutions can improve their governance of gen AI" —
  centralized-then-federated committee evolution; model inventory and identity-
  binding. `[mck-fi-genai-gov]`
- McKinsey, "Deploying agentic AI with safety and security: a playbook for
  technology leaders" — the agentic-specific playbook. `[mck-agentic-playbook]`
- McKinsey, "State of AI" / AI Trust Maturity waves — the five-dimension maturity
  model including agentic governance and controls. `[mck-state-of-ai]`
  `[mck-trust-maturity]`
- HBR, "Designing a Responsible AI Program? Start with this Checklist." The
  checklist is behind the paywall. `[hbr-rai-checklist]`
- HBR, "Organizations Aren't Ready for the Risks of Agentic AI." `[hbr-agentic-risks]`

---

## What this is not, and what comes next

**Assessment.** This pass answers "what does everyone else do." It does not grade
your Gemini draft, and it does not propose a Department of the Navy instruction.
When you are ready, the natural next pass is the gap analysis: lay the seven
primitives and the five agentic controls beside the draft and see what is strong,
what is missing (an independent-challenge function and an AI use-case inventory are
the two most likely gaps, on this evidence), and what is over-built. Until then,
read this as the map, and pull the McKinsey and HBR full texts so the corporate
claims rest on full sources rather than abstracts.

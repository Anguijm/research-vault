---
type: source-pack
study: ai-governance-landscape
stream: Agentic-AI-specific governance
captured: 2026-06-19
method: web-research subagent (WebSearch + WebFetch), raw output preserved
classification: internal
content_sha256: f8685f3c024529b499247fc0075dff7ac0a8362d5e55d85d8ebe097fb69c7bda
backfilled_hash: true
---

# Stream 3 — Agentic-AI-specific governance (raw research pack)

Raw research pack. Every URL is as fetched. Every source below was actually
retrieved and read; un-retrievable sources are listed honestly at the end and
their content is NOT reported. Input to the synthesis report.

---

## 1. OWASP Top 10 for Agentic Applications 2026 — OWASP Gen AI Security Project. Released Dec 9, 2025.
URLs: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ ; https://genai.owasp.org/2025/12/09/owasp-genai-security-project-releases-top-10-risks-and-mitigations-for-agentic-ai-security/
Fetched pages confirm the framework, date, publisher, and three highlighted threats (Agent Behavior Hijacking, Tool Misuse, Identity and Privilege Abuse); goal is "real-time intent controls and adaptive guardrails." Full 10 IDs (from search snippets + the fetched Teleport source in §2): ASI01 Agent Goal Hijack, ASI02 Tool Misuse & Exploitation, ASI03 Identity & Privilege Abuse, ASI04 Agentic Supply Chain, ASI05 Unexpected Code Execution (RCE), ASI06 Memory & Context Poisoning, ASI07 Insecure Inter-Agent Communication, ASI08 Cascading Failures, ASI09 Human-Agent Trust Exploitation, ASI10 Rogue Agents.

## 2. Teleport — OWASP Top 10 for Agentic Applications 2026: mitigations breakdown — Jack Pitts, Dec 15, 2025. Fetched.
URL: https://goteleport.com/blog/owasp-top-10-agentic-applications/
Richest fetched source for concrete per-risk controls:
- "Enforce least privilege so agents only get the goals, tools, and data they actually need."
- "Require human approval for high-impact or goal-changing actions"; "Require explicit confirmation for destructive actions."
- "Apply strict least privilege controls for each tool (scope, rate limits, allowed data)."
- "Run tools in sandboxed environments with egress controls"; "Run code in hardened, non-root, sandboxed containers with strict limits."
- "Give each agent a unique, bounded identity with short-lived credentials"; "Require re-authorization for privilege escalation"; wipe cached context between tasks.
- "Separate code generation from code execution with approval and validation gates."
- "Add rate limiting, blast-radius caps, and circuit breakers."
- "Implement kill switches that can revoke access across deployments on compromise"; "rapid containment like kill switches and credential revocation."
- "Use behavioral monitoring and watchdog agents to detect collusion or abnormal patterns"; "Maintain comprehensive signed audit logs of agent actions and communication."
- "Use mutual TLS authentication (mTLS) and encryption for agent channels"; sign messages with nonces/timestamps to prevent replay.

## 3. OWASP — State of Agentic AI Security and Governance 2.01 — OWASP Gen AI Security Project; June 1, 2026 (analysis by Capsule Security, June 3, 2026, Bar Kaduri). Both fetched.
URLs: https://genai.owasp.org/resource/state-of-agentic-ai-security-and-governance/ ; https://www.capsulesecurity.io/blog-post/owasp-state-of-agentic-ai-security-and-governance-2026-what-changed-and-what-it-means
- "Identity as the new control plane"; a full chapter on Agent Identity / Non-Human Identity.
- Governance "measured in hours," requiring "live monitoring, drift detection, automated incident routing, and agent-speed kill mechanisms."
- An "Enterprise Adoption Maturity Model" scoring governance capability against deployment complexity: "identify the most advanced agents you are running today, then either raise governance maturity to match or reduce the deployment tier."
- "Safety and security converge at the deployment layer."
- "Shadow AI… is present in nearly every organization contributors examined and must be discovered before it can be governed."

## 4. CSA — NIST AI Agent Standards Initiative (federal framework note) — Cloud Security Alliance; March 30, 2026. Fetched.
URL: https://labs.cloudsecurityalliance.org/research/csa-research-note-nist-ai-agent-standards-federal-framework/
NIST Center for AI Standards and Innovation AI Agent Standards Initiative (announced Feb 17, 2026). Four domains: interoperability/security standards; identity and authorization for non-human principals; agent action containment and least-privilege tool access; operational audit trails with attribution to specific agents. NCCoE focus: distinguishing agents from human users; extending OAuth 2.0 to agent principals; bounded access delegation; logging for "attribution to specific non-human entities for audit and forensic purposes." An "AI Agent Interoperability Profile" + SP 800-53 control overlays (COSAiS) in development; interoperability profile targeted Q4 2026. Gap: no standalone federal agentic AI security standard yet.

## 5. CSA — Agentic profile of the NIST AI RMF (v1 draft) — CSA AI Safety Initiative; ~March 27, 2026. Fetched.
URL: https://labs.cloudsecurityalliance.org/agentic/agentic-nist-ai-rmf-profile-v1/
Strongest fetched source for autonomy tiers tied to oversight + kill-switch detail:
- "Tier 1 agents operate in fully supervised mode, generating outputs that require human approval before any action is taken." "Tier 2 agents operate with constrained autonomy, executing pre-approved action types within a predefined scope but requiring human escalation for actions outside that scope."
- "produce and maintain a tool risk inventory for each agentic deployment that documents every tool available to the agent," defining "the scope of actions the agent is authorized to take without human approval; the conditions under which the agent must pause and escalate."
- "an agent accountability register" naming "the business owner accountable for the agent's behavior"; identity via Decentralized Identifiers (DIDs) and SPIFFE credentials.
- "automated agent suspension or kill-switch activation — for the highest-severity incident patterns rather than relying on human-in-the-loop containment decisions."
- Preserve "audit logs capturing the agent's complete action history"; Tier 2+ agents "collect and analyze a defined set of runtime behavioral metrics" against "dynamic baselines"; "Behavioral drift… is a risk category."

## 6. Strata Identity — Human-in-the-Loop: A 2026 Guide to AI Oversight — Eric Olden; May 11, 2026. Fetched.
URL: https://www.strata.io/blog/agentic-identity/practicing-the-human-in-the-loop/
- HITL: "A human to approve or authorize an action before the AI system executes it." HOTL: "The AI to act autonomously while a human monitors outputs and can intervene." Human-out-of-the-loop: fully autonomous (low-risk default).
- "The oversight level is a property of the decision, determined dynamically by risk, context, and policy."
- "Match SLA to risk: 15-second lane for low-risk actions, 2-minute lane for PII access, 15-minute lane for financial disbursements."
- "Replace 'Approve?' with a checklist: intent, data lineage, permissions chain, expected blast radius, rollback plan."
- "Identity governance is the enforcement layer… ensuring HITL checkpoints are technically enforced."

## 7. Microsoft — Governance and security for AI agents across the organization (Cloud Adoption Framework) — Stephen Sumner; updated 2026-06-02. Fetched.
URL: https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/governance-security-across-organization
Most operationally detailed vendor source. Four layers (data governance/compliance; agent observability; agent security; agent development) + single control plane:
- "Every agent must be observable, governed, and secure." Leaders must "identify what agents exist… limit what they can access… observe what they do… stop what they should not do."
- Agent registry / anti-shadow-AI inventory: "You can't govern agents you don't know exist."
- One identity per agent (Microsoft Entra Agent ID); actions "must be attributable and enforceable to a unique identity."
- Least privilege + permission inheritance: "Grant agents access only to the specific data sources required"; agent "inherits that user's permissions"; DLP so it can't "return credit card numbers."
- Cost/compute control: track "token consumption and compute usage," tag costs per agent, "Set up real-time alerts… when spending approaches budget thresholds… to prevent overruns."
- "Decide in advance how to quickly disable an agent if it malfunctions or causes harm," preserving logs.
- Sandboxing: "Public-facing agents must not access internal business data."
- MCP "enforces boundaries around what agents can access"; restrict to "trusted MCP servers." Adversarial testing + I/O filtering + managed identities before production; route AI alerts into the SOC.

## 8. Anthropic — Our framework for developing safe and trustworthy agents — Aug 4, 2025. Fetched.
URL: https://www.anthropic.com/news/our-framework-for-developing-safe-and-trustworthy-agents
Five principles: keep humans in control while enabling autonomy; transparency; align with human values; protect privacy; secure interactions.
- "Humans should retain control over how their goals are pursued, particularly before high-stakes decisions." In Claude Code, "humans can stop Claude whenever they want and redirect its approach," read-only default, approval before modifying systems.
- "Humans need visibility into agents' problem-solving processes" (real-time to-do checklist).
- MCP enables "controls to allow or prevent Claude from accessing specific tools."
- Agents must avoid "inappropriately carry[ing] sensitive information from one context to another."
- (Search-surfaced, not fetched: Anthropic "Plan Mode" — review/modify a whole execution plan upfront vs approving each action.)

## 9. Google DeepMind Frontier Safety Framework v3 (via SiliconANGLE) — Sept 22, 2025. Fetched (secondary).
URL: https://siliconangle.com/2025/09/22/google-deepmind-expands-frontier-ai-safety-framework-counter-manipulation-shutdown-risks/
- "expands safety reviews to cover scenarios where models may resist human shutdown or control"; greater scrutiny to misalignment and "the idea that highly capable systems could… resist modification or shutdown."
- New "Critical Capability Level for harmful manipulation."
- "mitigations must be applied proactively before systems cross dangerous boundaries"; safety-case reviews required before external deployment AND large-scale internal rollouts once a model hits CCL thresholds.

## 10. AWS — Updated GRC user guide for responsible AI adoption — AWS Security Blog; May 13, 2026. Fetched (announcement).
URL: https://aws.amazon.com/blogs/security/introducing-the-updated-aws-user-guide-to-governance-risk-and-compliance-for-responsible-ai-adoption/
Names an "AI agent management" dimension covering Amazon Bedrock AgentCore, Bedrock Guardrails, Bedrock Agents, SageMaker Model Monitor. The post is an announcement; detailed agent-autonomy mechanics sit in the linked guide (not retrieved). Treat as: confirmed existence of agent-specific GRC guidance + the Bedrock Guardrails/AgentCore control surface.

## 11. Loop / cost / runaway-spend control — engineering sources
(a) BSWEN — "How Do You Stop AI Agents From Infinite Loops?" Cowrie; Mar 11, 2026. Fetched. URL: https://docs.bswen.com/blog/2026-03-11-prevent-ai-agent-infinite-loops/
- Iteration cap: "Set a maximum number of reasoning steps per task. No exceptions." (default max_iterations = 50).
- Token/cost budget kill: "Track cumulative token usage. Kill the agent when the budget is exhausted." (default max_tokens = 500_000, ≈ $50).
- No-progress detection: "Compare consecutive reasoning outputs. If similarity exceeds threshold, the agent is stuck."
- Semantic completion check: "Ask the LLM: 'Is the task done?' Require explicit confirmation."
- Time-based circuit breaker: "Absolute timeout regardless of progress" (default 30 min).
- "Single guards fail. Multi-layer defense works."
(b) Dev|Journal — "How an Unchecked AI Agent Loop Cost $437 Overnight" — earezki, 2026-04-29, URL https://earezki.com/ai-news/2026-04-29-i-let-my-ai-agent-run-overnight-it-cost-437/ — returned HTTP 403; content NOT reported. Listed as a real dated artifact only.

## 12. Curation index — Oliver Patel, "The Ultimate Agentic AI Governance Resource Guide" — Substack. Fetched.
URL: https://oliverpatel.substack.com/p/updated-the-ultimate-agentic-ai-governance
Corroborates existence/URLs of follow-up artifacts: NIST "Strengthening AI Agent Hijacking Evaluations" (2025); OWASP's four agentic docs; OECD "agentic AI landscape" (2026); Singapore IMDA "Model AI Governance Framework for Agentic AI" (2026) + CSA Singapore "Securing Agentic AI"; UK AISI control-measures work; WEF "AI Agents in Action" (2025); Google "Secure AI Framework (SAIF) 2.0: Focus on Agents" (2025, https://www.saif.google/focus-on-agents); Meta "Agents Rule of Two" (2025); OpenAI "Practices for Governing Agentic AI Systems"; McKinsey agentic playbook. The catalog itself "does not provide explicit verbatim quotations."

## Sources NOT retrieved (content not reported)
- McKinsey "State of AI trust in 2026: Shifting to the agentic era" and "Deploying agentic AI with safety and security" — WebFetch timed out.
- Gartner 2026 Hype Cycle for Agentic AI + Aug 26, 2025 press release — HTTP 403. (Search snippets: new "agentic AI governance," "agentic AI security," "FinOps for agentic AI" profiles; prediction that 40%+ of agentic projects scrapped by end-2027 partly from "inadequate risk controls" — unverified.)
- OWASP agentic PDFs (landing pages thin; per-risk controls in §2 from Teleport, not the OWASP PDF directly).
- DeepMind FSF primary PDF and Anthropic "Plan Mode" detail — search-known, not fetched.

---

## Top takeaways (agentic-specific controls)

**Autonomy / HITL, matched to risk**
1. Tier autonomy and bind each tier to an oversight mode (fully supervised → constrained autonomy → autonomous). Sources: CSA RMF Agentic Profile; Strata; Anthropic.
2. Gate high-impact and irreversible actions behind explicit human approval, with structured (not yes/no) approvals and time-boxed SLAs. Sources: Teleport; Strata; Anthropic.

**Permissions / write-gating**
3. Least privilege scoped to the goals, tools, and data an agent needs, with permission inheritance from the invoking user and short-lived credentials. Sources: Teleport; Microsoft CAF; CSA NIST initiative; OWASP State-of-Governance.
4. Separate code generation from execution and run tools/code in sandboxes with egress control. Sources: Teleport; Microsoft CAF.

**Cost / loop control**
5. Multi-layer runaway brakes: hard iteration/max-step caps, token/cost budgets that kill the run, no-progress detection, absolute wall-clock timeout. Sources: BSWEN; Teleport; Microsoft CAF. ("FinOps for agentic AI" is the named market category — Gartner, unverified.)

**Observability / audit / halt**
6. Comprehensive, tamper-evident/signed audit logs attributing every action to a specific agent, plus continuous behavioral monitoring with drift detection. Sources: CSA NIST initiative; CSA RMF profile; Microsoft CAF; Teleport.
7. Kill switch / rapid containment, increasingly automated for the most severe patterns. Sources: Teleport; CSA RMF profile; OWASP State-of-Governance; Microsoft CAF; Anthropic.

**Identity / guardrails / standards**
8. Give every agent a unique, verifiable identity (non-human identity / Entra Agent ID / DIDs+SPIFFE) and an accountability owner; maintain a registry to kill shadow AI. Sources: Microsoft CAF; CSA initiative + RMF profile; OWASP State-of-Governance.
9. Secure inter-agent communication; treat multi-agent systems as a cascading-failure surface (mTLS, signed messages, blast-radius caps). Sources: Teleport; CSA initiative.
10. Frontier-lab guardrails address misalignment/goal-drift, shutdown resistance, harmful manipulation — gated by capability thresholds. Sources: DeepMind FSF v3; Anthropic; OWASP Top 10.

**Standards to watch:** NIST AI Agent Standards Initiative (Feb 17, 2026; interoperability profile Q4 2026; SP 800-53 agentic overlays in development); OWASP Top 10 for Agentic Applications 2026 + State of Agentic AI Security and Governance 2.01.

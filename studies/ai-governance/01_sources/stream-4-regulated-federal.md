---
type: source-pack
study: ai-governance-landscape
stream: Regulated-industry + federal-government + standards
captured: 2026-06-19
method: web-research subagent (WebSearch + WebFetch), raw output preserved
classification: internal
content_sha256: 88daba48a8305ca5946da0ac7c296d0f70eb295cf221930c08bed624137ff5cd
backfilled_hash: true
---

# Stream 4 — Regulated-industry + federal-government AI governance (raw research pack)

Raw research pack. Every URL is as fetched. Where a primary `.gov`/`.mil` page
hard-blocked the fetcher, that is noted and a fetched alternative is used. No URLs,
titles, dates, or quotes invented. Input to the synthesis report.

---

## 1. OMB Memorandum M-25-21 (successor to M-24-10) — federal civilian AI governance
- **Title:** "Accelerating Federal Use of AI through Innovation, Governance, and Public Trust." **Publisher:** OMB. **Date:** April 3, 2025. Rescinds and replaces M-24-10 (March 28, 2024).
- **URL (public mirror of OMB PDF):** https://static.carahsoft.com/concrete/files/9717/4412/5797/Guidance_M-25-21_Accelerating_Federal_Use_of_AI_through_Innovation_Governance_and_Public_Trust.pdf
- Corroboration: https://digitalgovernmenthub.org/examples/omb-m-25-21-accelerating-federal-use-of-ai-through-innovation-governance-and-public-trust/ ; https://www.hunton.com/privacy-and-cybersecurity-law-blog/omb-issues-revised-policies-on-ai-use-and-procurement-by-federal-agencies

Mechanisms: each agency designates a CAIO (agency-wide governance policy, oversight, compliance); establish governance bodies that review/approve AI initiatives with documented decisions; maintain an enterprise AI strategy; maintain a documented, publicly reported AI use-case inventory with deployment context + risk classification; **"high-impact AI"** tier (replaces M-24-10's twin rights-impacting / safety-impacting categories with a single high-impact tier); minimum risk-management practices for high-impact AI — pre-deployment testing/validation, AI impact assessment (incl. civil rights), ongoing monitoring, human review/oversight, documentation + auditability.
Verbatim (fetched PDF): "Agencies shall ensure that all high-impact AI systems receive appropriate human review before deployment."
Lineage: supports Executive Order 14179 ("Removing Barriers to American Leadership in Artificial Intelligence," Jan 23, 2025). **Unverified later lead:** M-26-04, "Increasing Public Trust in AI Through Unbiased AI Principles" (whitehouse.gov, Dec 2025 per URL path) — NOT fetched/verified.

## 2. Federal Reserve Board — Compliance Plan for OMB M-25-21 (worked example)
- **Publisher:** Federal Reserve Board of Governors. **Date:** October 1, 2025.
- **URL:** https://www.federalreserve.gov/publications/compliance-plan-for-OMB-memorandum-m-25-21.htm

The abstract M-25-21 mechanisms instantiated: a CAIO with explicit approval authority over all high-impact AI deployments; layered bodies (AI Program Team; AI Enablement Working Group; Technology Oversight Committee chaired by the COO); inventory as intake gate (all AI users submit use cases; the AI Program Team assesses permissibility); high-impact screening workflow; impact assessment per high-impact case with recorded determinations + annual waiver recertifications; human oversight + automated guardrails ("supervisor agents" detecting inaccuracies; technical controls that terminate noncompliant AI on Board systems).
Verbatim: "Those use cases flagged as possible high-impact AI uses are referred to the AI Program team for confirmation of the high-impact determination." / "Human review protocols ensure that AI use cases undergo expert evaluation before use."

## 3. GAO AI Accountability Framework (GAO-21-519SP)
- **Title:** "Artificial Intelligence: An Accountability Framework for Federal Agencies and Other Entities." **Publisher:** GAO. **Date:** June 30, 2021.
- **URL:** https://www.gao.gov/products/gao-21-519sp (PDF https://www.gao.gov/assets/gao-21-519sp.pdf)

Four principles, each with key practices + questions + audit procedures for entities, auditors, and third-party assessors: **Governance** (objectives, oversight structures, accountability roles, multi-perspective stakeholders); **Data** (quality, reliability, representativeness); **Performance** (effective, intended results); **Monitoring** (continuous reassessment so systems "remain reliable and relevant over time"). Built to be independently assessed, not self-certified; third-party assessments/audits explicitly endorsed; references IG-office consultation.
Verbatim: "AI systems pose unique challenges to such oversight because their inputs and operations are not always visible."
Companion (fetched): GAO-23-106811, "Key Practices to Help Ensure Accountability in Federal Use," May 16, 2023, https://www.gao.gov/products/gao-23-106811 — restates the four principles; "third-party assessments and audits are important to achieving these goals"; workforce/expertise gaps are a binding constraint.

## 4. Financial services — SR 11-7 model risk management, extended to AI/ML
- **Title:** "Supervisory Guidance on Model Risk Management" (SR 11-7; OCC Bulletin 2011-12). **Publisher:** Federal Reserve + OCC. **Date:** April 4, 2011.
- **Primary URL (confirmed live but hard-blocked the fetcher, HTTP 404 to the agent):** https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm
- **Fetched for substance:** ModelOp, "SR 11-7 Model Risk Management," https://www.modelop.com/ai-governance/ai-regulations-standards/sr-11-7 (quotes SR 11-7's own language). Corroboration: https://www.the-algo.com/insights/ai-governance-financial-services-sr1107 ; https://www.glacis.io/guide-sr-11-7

This is the mature "model risk management" analog the brief asked to flag. Mechanisms: model defined broadly enough to capture AI/ML/LLMs; **effective challenge** as the central control; three core elements (robust development/implementation/use; sound validation; governance/policies/controls); **independent validation** by parties separate from development with authority to mandate changes (conceptual soundness + ongoing monitoring + outcomes analysis/back-testing); governance infrastructure (roles, model inventory, policies, documentation; board + senior management own the framework); **three lines of defense** (developers; independent validation; internal audit). SR 21-8 (2021) supplements for ML/alt-data/cloud (search context).
Verbatim (ModelOp mirror, quoting SR 11-7): "the critical analysis of a model against its objectives by informed, technically competent parties who can identify model limitations and assumptions" (effective challenge); "a quantitative method, system, or approach that applies statistical, economic, financial, or mathematical theories... to process input data into quantitative estimates" (model definition).
**Unverified lead (search, NOT fetched):** a 2026 revision — SR 26-02 (PDF path https://www.federalreserve.gov/supervisionreg/srletters/SR2602.pdf) + OCC Bulletin 2026-13 (https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-13.html). Treat as unverified.

## 5. Healthcare — FDA guidance on AI-enabled medical devices
- **Title:** "Artificial Intelligence-Enabled Device Software Functions: Lifecycle Management and Marketing Submission Recommendations" (Draft). **Publisher:** FDA. **Date:** Draft Jan 7, 2025 (docket FDA-2024-D-4488).
- **Primary URLs (both hard-blocked the fetcher):** Federal Register https://www.federalregister.gov/documents/2025/01/07/2024-31543/ ; FDA SaMD page https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-software-medical-device
- **Fetched for substance:** CenterWatch, https://www.centerwatch.com/insights/fda-guidance-on-ai-enabled-devices-transparency-bias-lifecycle-oversight/

Mechanisms (track SR 11-7's lifecycle logic): Total Product Lifecycle (TPLC) governance; nine-area marketing-submission documentation set (device description/UI, labeling, risk assessment, data management, model description/development, validation, performance monitoring, cybersecurity); bias mitigation (data representativeness + subpopulation testing); transparency/labeling; **Predetermined Change Control Plan (PCCP)** — pre-authorize a bounded set of post-market model changes without a new submission; post-market performance monitoring.
Verbatim (CenterWatch, quoting standards): validation = confirming "the particular requirements for a specific intended use can be consistently fulfilled" (21 CFR 820.3(z)); bias "can produce erroneous results in a systemic but unpredictable way."
FDA program context (search; FDA pages blocked): 2021 AI/ML SaMD Action Plan; Good Machine Learning Practice (GMLP) 10 principles (Oct 2021, with Health Canada + UK MHRA); PCCP guiding principles (Oct 2023); Transparency principles (June 2024); Final Marketing Submission guidance (Dec 2024).

### 5b. Hospital / health-system AI governance committees
- npj Digital Medicine (Nature Portfolio), "Advancing healthcare AI governance through a comprehensive maturity model": https://www.nature.com/articles/s41746-026-02418-7 ; PMC https://pmc.ncbi.nlm.nih.gov/articles/PMC13004926/ (abstract read, not full body).
- Executive committee over functional subpanels; a five-level maturity model (HAIRA) across seven domains; CAOS framework (Comprehensive Algorithmic Oversight and Stewardship; Springer https://link.springer.com/article/10.1007/s10728-025-00537-y).
- **Local-validation gap:** former FDA Commissioner Robert Califf (JAMA Summit, via Stanford Medicine https://med.stanford.edu/medicine/news/current-news/standard-news/ai-in-medicine-jama2025.html): "no health system in the United States is currently capable of validating an AI algorithm once it's in use." The independent-validation function that exists in banking is largely absent in hospitals.

## 6. Other governments — comparative color
### 6a. United Kingdom — principles-based, regulator-led
- "A pro-innovation approach to AI regulation" (White Paper). DSIT / Office for AI. Presented 29 March 2023; updated 3 August 2023.
- **URL:** https://www.gov.uk/government/publications/ai-regulation-a-pro-innovation-approach/white-paper
- Five cross-sector principles: safety/security/robustness; appropriate transparency & explainability; fairness; accountability & governance; contestability & redress. No new AI regulator and no single AI law — existing sector regulators apply the principles; non-statutory first, statutory "due regard" duty anticipated later.
- Verbatim: "Governance measures should be in place to ensure effective oversight of the supply and use of AI systems, with clear lines of accountability established across the AI life cycle."

### 6b. Singapore — operational, voluntary framework
- IMDA / PDPC "Model AI Governance Framework" (1st ed. 2019; 2nd ed. 2020; GenAI ed. 2024).
- **URL (landing; full PDF separate):** https://www.pdpc.gov.sg/help-and-resources/2020/01/model-ai-governance-framework ; corroboration https://blogs.duanemorris.com/duanemorrisandselvam/2026/03/03/singapores-digital-ai-governance-a-pro-innovation-framework-driven-model/
- Internal governance structures and measures; human oversight calibrated to risk (human-in / over / out-of-the-loop by use-case risk); operations management (dataset management, robustness, monitoring); stakeholder communication/transparency; GenAI extension (2024) adds hallucination, IP, provenance, cybersecurity, systemic risk. (Mechanism detail from search summaries; landing page returned metadata only.)

## 7. Security controls reference — OWASP Top 10 for LLM Applications 2025
- OWASP Foundation (GenAI Security Project). Version released Nov 17, 2024 (the "2025" edition).
- **URLs:** https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/ ; https://genai.owasp.org/llm-top-10/
- Full list: LLM01 Prompt Injection; LLM02 Sensitive Information Disclosure; LLM03 Supply Chain; LLM04 Data and Model Poisoning; LLM05 Improper Output Handling; LLM06 Excessive Agency; LLM07 System Prompt Leakage; LLM08 Vector and Embedding Weaknesses; LLM09 Misinformation; LLM10 Unbounded Consumption.
- Governance-relevant themes: governance frameworks; rigorous output validation; supply-chain monitoring; control system agency through access restrictions + human-oversight. LLM06 Excessive Agency + LLM10 Unbounded Consumption map directly onto agentic autonomy and cost control.

---

## Top takeaways (regulated-industry + federal)

1. **A "model risk management / independent validation" function is the mature analog**, converging into AI governance. SR 11-7's structure (independent validation, "effective challenge," model inventory, three lines of defense) is echoed in FDA's TPLC/PCCP, GAO's four-principle framework, and hospital committee models. Sharpest contrast: banking has a working independent-validation function; healthcare largely does not (Califf).
2. **A named, accountable officer + standing governance body is standard** (CAIO with approval authority over the AI Governance Board; instantiated concretely in the Fed Board compliance plan).
3. **Inventories + risk tiering are the universal intake gate** (federal public use-case inventories + "high-impact" tier; bank model inventories; UK/Singapore risk-calibrated controls).
4. **Lifecycle / continuous monitoring beats point-in-time approval** (GAO Monitoring; FDA TPLC + PCCP + post-market; SR 11-7 ongoing monitoring; OWASP lifecycle).
5. **Human oversight before/over consequential decisions is near-universal** (M-25-21 human review before deploying high-impact AI; Singapore calibrated HITL; OWASP Excessive Agency).
6. **Documentation, transparency, bias/fairness assessment are recurring mandatory artifacts.**
7. **Independent / third-party assessment is the trust mechanism that distinguishes mature regimes** (GAO built for auditors; SR 11-7 independent validation; FDA premarket review). Where weakest (hospitals buying models), it is flagged as the central gap.
8. **Two philosophies coexist:** prescriptive sectoral rules (US federal, banking, FDA) vs principles-led flexibility (UK, Singapore) — converging on the same primitives (accountable owner, inventory, risk tiering, human oversight, monitoring, documentation).

---
type: source-pack
study: ai-governance-landscape
stream: DoD / U.S. military AI governance
captured: 2026-06-19
method: web-research subagent (WebSearch + WebFetch), raw output preserved
classification: internal
---

# Stream 1 — DoD / U.S. military AI governance (raw research pack)

This is the verbatim research pack from the web-research subagent. Every URL is
as fetched. Reliability caveats are preserved. This is an INPUT to the synthesis
report, not the deliverable.

**Retrieval caveat (from the agent):** All `.mil` domains (ai.mil, esd.whs.mil,
dodcio.defense.gov, media.defense.gov, doncio.navy.mil) hard-block direct fetching
from this environment. The agent recovered core primary PDFs through the Internet
Archive `id_` snapshot endpoint and extracted text locally. DON CIO primary memos
remained unreachable even via archive; DON content rests on the Naval Postgraduate
School library guide and trade press. The agent caught and discarded one fabricated
WebFetch result (wrong GAO report number + invented quotes).

---

## 1. DoD AI Ethical Principles (Feb 2020)

- **Source:** text reproduced inside the RAI Strategy; original SecDef memo Feb 24, 2020.
- **Publisher:** DoD / CDAO (RAI Working Council).
- **URL:** https://web.archive.org/web/2025id_/https://media.defense.gov/2024/Oct/26/2003571790/-1/-1/0/2024-06-RAI-STRATEGY-IMPLEMENTATION-PATHWAY.PDF

The five principles, verbatim, "apply to all DoD AI capabilities, encompassing both combat and non-combat applications":
- **Responsible:** "DoD personnel will exercise appropriate levels of judgment and care, while remaining responsible for the development, deployment, and use of AI capabilities."
- **Equitable:** "The Department will take deliberate steps to minimize unintended bias in AI capabilities."
- **Traceable:** "relevant personnel possess an appropriate understanding of the technology... including with transparent and auditable methodologies, data sources, and design procedures and documentation."
- **Reliable:** capabilities "will have explicit, well-defined uses, and the safety, security, and effectiveness of such capabilities will be subject to testing and assurance within those defined uses across their entire life-cycles."
- **Governable:** "possessing the ability to detect and avoid unintended consequences, and the ability to disengage or deactivate deployed systems that demonstrate unintended behavior."

## 2. DoD Responsible AI (RAI) Strategy and Implementation Pathway

- **Publisher:** DoD Responsible AI Working Council. **Date:** June 2022.
- **URL:** https://web.archive.org/web/2025id_/https://media.defense.gov/2024/Oct/26/2003571790/-1/-1/0/2024-06-RAI-STRATEGY-IMPLEMENTATION-PATHWAY.PDF

- Operationalizes the five Ethical Principles through **six Foundational Tenets**: (1) RAI Governance, (2) Warfighter Trust, (3) AI Product and Acquisition Lifecycle, (4) Requirements Validation, (5) Responsible AI Ecosystem, (6) AI Workforce. Each tenet has Lines of Effort (LOEs) with a designated Office of Primary Responsibility (OPR).
- **CDAO is the DoD lead** "for coordinating the implementation and oversight of guidance and policy on AI, including RAI and the DoD AI Ethical Principles."
- Named bodies: the **RAI Working Council**; the **CDAO governing council** ("a 4-star level governance body run by the CDAO to oversee all aspects of data, analytics, and AI for the Department"); and **DoD Component RAI Leads**.
- Operating model: "CONDUCT CENTRALIZED COORDINATION OF RAI POLICIES AND GUIDANCE WITH DECENTRALIZED EXECUTION."
- Quote: "All DoD Components must ensure that their AI capabilities are in alignment with the DoD Ethical Principles, and that their policies and practices enable RAI implementation."

## 3. CDAO Task Force Lima (Generative AI / LLM task force)

- **Publisher:** Deputy Secretary of Defense. **Date:** August 10, 2023.
- **URL:** https://web.archive.org/web/2023id_/https://media.defense.gov/2023/Aug/10/2003279040/-1/-1/1/ESTABLISHMENT_OF_CDAO_GENERATIVE_AI_AND_LARGE_LANGUAGE_MODELS_TASK_FORCE_TASK_FORCE_LIMA_OSD006491-23_RES_FINAL.PDF

- "The CDAO will lead Task Force Lima," chaired through the Algorithmic Warfare Directorate; lessons feed the RAI Working Council and rise through the CDAO Council to the Deputy's Management Action Group.
- Quote: "Task Force Lima will develop, evaluate, recommend, and monitor the implementation of generative AI technologies across DoD to ensure the Department is able to design, deploy, and use generative AI technologies responsibly and securely."

## 4. Task Force Lima Executive Summary (final report)

- **Publisher:** DoD CDAO. **Date:** December 2024. Distribution A (public release).
- **URL:** https://web.archive.org/web/2025id_/https://www.ai.mil/Portals/137/Documents/Resources%20Page/2024-12-TF%20Lima-ExecSum-TAB-A.pdf

- Recommends CDAO sunset Task Force Lima and federate GenAI adoption to standing OPRs.
- Pushes **provisional authorizations for LLM services** and an **LLM Authority-to-Operate (ATO) dashboard** so "commands have the relevant information about LLM platforms with Interim Authorization to Test (IATT) or ATOs on DoD enclaves."
- Directs scaling of **DoD-secured GenAI platforms (NIPRGPT and CamoGPT)** to avoid "inadvertent spills through employee queries to commercial and unsecured GenAI services."
- Flags **classification-by-aggregation** as a DoD-unique concern.
- Quote: "While the technology will never be perfect, it is imperative that leaders only deploy GenAI in situations for which it is well suited and that users understand the capabilities and limitations before deploying GenAI in safety or security critical applications."

## 5. CDAO AI Rapid Capabilities Cell (AI RCC) — Task Force Lima successor

- **Publisher:** DefenseScoop (trade press). **Date:** December 11, 2024.
- **URL:** https://defensescoop.com/2024/12/11/cdao-pentagon-generative-ai-rapid-capabilities-cell-sunset-task-force-lima/

- AI RCC run by CDAO with the Defense Innovation Unit (DIU); risk management built on ATO processes and identity, credential, and access management (ICAM).
- CDAO head Radha Plumb governance philosophy: "better brakes make faster trains."

## 6. DoD Instruction 5400.19 — Public Affairs Use of Artificial Intelligence

- **Publisher:** ATSD(PA). **Date:** Effective July 28, 2025.
- **URL:** https://web.archive.org/web/2025id_/https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodi/540019p.PDF

Most concrete current acceptable-use rule set found:
- Hard data rule: "DoD personnel may only enter classified information, controlled unclassified information (including PII or protected health information)... into AI systems authorized for that level of classification or control... **Commercial AI solutions outside of the DoD's control are not authorized for any non-public information.**"
- CIO gatekeeping; pre-use assessment + continuous monitoring; licensing must "contractually address vendor use and retention of DoD user data."
- Human-in-the-loop for generative output before public release; transparency/labeling (photorealistic GenAI imagery "labeled as a photo illustration"; provenance metadata); anomaly reporting of "new, repetitive, and unexpected AI tool outputs (and the prompts used)" to the Component CIO.
- Two binding decision matrices; Component matrices "may be more restrictive, but not less restrictive."
- Ties to the July 12, 2024 CDAO Memorandum and the August 23, 2023 DoD CIO Memorandum.

## 7. DoD AI Cybersecurity Risk Management Tailoring Guide (v2)

- **Publisher:** DoD CIO. **Date:** 14 July 2025 (cleared Aug 7, 2025).
- **URL:** https://web.archive.org/web/2025id_/https://dodcio.defense.gov/Portals/0/Documents/Library/AI-CybersecurityRMTailoringGuide.pdf

- Integrates AI into the DoD Risk Management Framework (RMF) under DoDI 8510.01 / 8500.01; the **Authorizing Official (AO)** is the named accountable decision-maker.
- Requires continuous monitoring for AI-specific threats: "data poisoning, inference attacks, model discovery, reverse [engineering]," bias, degrade, drift.
- Cites the CDAO memo "Guidelines and Guardrails to Inform Governance of Generative AI."

## 8. CDAO Statement on DoD Compliance with OMB M-24-10 (CAIO designation)

- **Publisher:** Office of the CDAO. **Date:** compliance plan published Sept 24, 2024.
- **URL:** https://web.archive.org/web/2025id_/https://www.ai.mil/Portals/137/Documents/Resources%20Page/Statement_on_DoD_2024.pdf

- "The Chief Digital and AI Officer (CDAO), the Department's Chief AI Officer (CAIO)."
- The **CDAO Council** is "the DoD's AI governance body."
- DoD is statutorily exempt (Advancing American AI Act) from the federal AI use-case inventory requirement but voluntarily complies; the CAIO "will not, at present, be issuing any waivers."

## 9. GAO — Generative AI Use and Management at Federal Agencies (GAO-25-107653)

- **Publisher:** GAO. **Date:** July 2025.
- **URL:** https://web.archive.org/web/2025id_/https://www.gao.gov/assets/gao-25-107653.pdf
- (An earlier WebFetch returned a fabricated report number "GAO-24-287SP" with invented quotes; that was discarded. Below is from the verified PDF.)

- Names the primary DoD GenAI governance memo: "DoD CDAO, **Guidelines and Guardrails to Inform Governance of Generative Artificial Intelligence**, (July 12, 2024)."
- DoD concern: "generative AI models could aggregate various unclassified information... and unintentionally output classified information."
- Government-wide control under M-24-10: agency CAIOs centrally track high-impact use cases; an AI Impact Assessment is required before deploying any high-impact use case; waivers must be written, system-specific, and reported to OMB within 30 days.

## 10. Department of the Navy (DON) Generative AI / LLM guidance

- **Publisher:** DON CIO. **Dates:** interim memo Sept 6, 2023; GenAI.mil designation memo Jan 28, 2026.
- **Primary URLs BLOCKED** (F5 BIG-IP "Request Rejected"): https://www.doncio.navy.mil/ContentView.aspx?id=16442 and ...ID=16448
- **Sourced instead from:** NPS Dudley Knox Library guide https://libguides.nps.edu/gen-ai/guidance (retrieved).

- 2023 memo framed as interim guardrails: "The purpose of this memorandum is to offer interim guardrail guidance when considering the use of Generative Artificial Intelligence (AI) or Large Language Models (LLM)."
- Per trade-press summary (not verified against primary): rules of engagement and access through **Jupiter** (DON enterprise data/analytics platform); accountability "ultimately resides with each individual organization's respective leadership."

## 11. Navy mandates GenAI.mil as enterprise CUI/IL5 platform

- **Publisher:** CDO Magazine. **Date:** March 30, 2026.
- **URL:** https://www.cdomagazine.tech/us-federal-news-bureau/us-navy-mandates-genai-mil-for-enterprise-cui-il5-ai-use

- DON CIO memo Jan 28, 2026 directs all DON commands to transition to GenAI.mil by **April 30, 2026.**
- GenAI.mil is the mandated **IL5 / CUI** platform; "The platform prohibits the use of protected health and personally identifiable information."
- Integrated tools: Google Gemini for Government, xAI for Government, OpenAI ChatGPT.

## 12. DoD enterprise GenAI.mil rollout (CDAO-governed)

- **Publisher:** DefenseScoop. **Date:** December 9, 2025.
- **URL:** https://defensescoop.com/2025/12/09/genai-mil-platform-dod-commercial-ai-models-agentic-tools-google-gemini/

- CDAO operates GenAI.mil as the single DoD-wide platform; "All of the tools that will be available on GenAI.mil are certified for Controlled Unclassified Information (CUI) and Impact Level 5 (IL5)."
- CDAO holds enterprise contracts with four frontier vendors: Anthropic, xAI, OpenAI, Google.
- Supporting: Air & Space Forces Magazine, "Pentagon Brings ChatGPT into Its Official AI Tool Set," Feb 13, 2026, https://www.airandspaceforces.com/pentagon-adds-chatgpt-official-ai-tool-set/ — GenAI.mil "consolidates AI tool adoption under uniform governance, replacing earlier service-specific systems like NIPRGPT and CamoGPT."

## 13. Air Force NIPRGPT — governance and sunset

- DefenseScoop, Dec 18, 2025: https://defensescoop.com/2025/12/18/air-force-sunsetting-niprgpt-generative-ai-platform/
- Air & Space Forces Magazine, Dec 22, 2025: https://www.airandspaceforces.com/air-force-shutting-down-ai-chatbot-niprgpt/

- NIPRGPT (Air Force Research Laboratory, 2024, NIPRNet) operated under unclassified-only guardrails; data governance followed CNSSI 1253 and NIST SP 800-53; ~700,000 users.
- Decommissioned Dec 31, 2025, folded into GenAI.mil. "The insights gathered from NIPRGPT were foundational in shaping future requirements, establishing effective guardrails, and defining governance."

## 14. Army CamoGPT / Enterprise LLM Workspace — governance and inter-service block

- Air & Space Forces Magazine, June 25, 2025: https://www.airandspaceforces.com/fearing-data-leaks-army-blocks-air-force-ai-program-from-its-networks/
- Breaking Defense, July 23, 2025: https://breakingdefense.com/2025/07/army-upgrades-policy-technology-to-secure-genai/
- TechTarget, Oct 9, 2024: https://www.techtarget.com/searchenterpriseai/news/366613198/Government-use-of-AI-by-key-US-military-branches

- Army CIO Leonel Garciga blocked NIPRGPT from Army networks April 2025 over data-governance/cyber concerns; "The block was focused on getting us to a governance framework for AI used in a production state." No service is required to honor another's ATO — authorization is fragmented per command.
- Army stood up the **Enterprise LLM Workspace (May 2025)**, powered by **Ask Sage**, with CUI accreditation, IL5/FedRAMP-High ATO, and **token-based billing** controlled by the Army CIO (token release is the access-control lever).
- Quote (Garciga): "If you're using an AI tool, it doesn't absolve you from meeting those requirements."
- Quote (Army CTO Gabriel Chiulli): "Soldiers will soldier: They'll go and use stuff that's useful whether or not they're supposed to use it."

## 15. DoD Directive 3000.09 — Autonomy in Weapon Systems (adjacent context only)

- **Date:** Reissued January 25, 2023.
- **URL:** https://static.carahsoft.com/concrete/files/4917/1101/9112/Guidance_DoD_Directive_3000.09_-_Autonomy_in_Weapon_Systems.pdf (summary card reproducing core policy text)

- Core control: "Autonomous and semi-autonomous weapon systems will be designed to allow commanders and operators to exercise appropriate levels of human judgment over the use of force." Senior-review/approval gate before development and fielding. Treat as adjacent — governs lethal autonomy, not enterprise-LLM use.

---

## Top takeaways (DoD/military)

1. **Single hub-and-spoke authority:** CDAO is DoD's Chief AI Officer; the CDAO Council is the named "AI governance body"; centralized coordination + decentralized execution.
2. **Five Ethical Principles** (Responsible, Equitable, Traceable, Reliable, Governable) operationalized through six Foundational Tenets with assigned OPRs. "Responsible" hard-codes human accountability; "Governable" requires disengage/deactivate.
3. **Strict CUI/non-public-data handling with a bright line against commercial tools.** Classification-by-aggregation is a recurring DoD-unique worry.
4. **Authorization gating via the RMF** (ATO/IATT, IL5, FedRAMP), Authorizing Official accountable, mandatory continuous monitoring.
5. **Consolidation onto a single CDAO-governed platform (GenAI.mil)** certified for CUI/IL5, superseding NIPRGPT and CamoGPT; PII/PHI prohibited even at IL5.
6. **Human review for generative output, plus transparency/provenance labeling.**
7. **Persistent human accountability** — using an AI tool never waives legal obligations.
8. **Governance is still maturing and iterative** — pilot-then-codify (Task Force Lima → AI RCC); inter-service ATO fragmentation (Army's NIPRGPT block) shows gaps closing in real time.

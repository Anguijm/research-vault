---
type: source
study: ai-governance-landscape
title: Designing a Responsible AI Program? Start with this Checklist
author: Reid Blackman; Ingrid Vasiliu-Feltes
publisher: Harvard Business Review (Digital Article, AI and Machine Learning)
publication_date: 2024-12-05
reprint: H08HKF
url: https://hbr.org/2024/12/designing-a-responsible-ai-program-start-with-this-checklist
local_pdf: hbr/hbr-rai-checklist-2024-H08HKF.pdf
captured: 2026-06-19
source_tier: 1
classification: internal
verified: 2026-06-19 (full text read from operator-provided PDF)
content_sha256: fdf595c7171df257133f1d99f5a553265d38e2d3dc758aea6005dedeaa92a4d2
backfilled_hash: true
---

# Designing a Responsible AI Program? Start with this Checklist (HBR, Blackman & Vasiliu-Feltes, 2024)

Full text, read from the operator's subscription PDF. This replaces the earlier
abstract-only capture. Quotes below are verbatim.

## Summary

**Assessment.** This is the "what to build" companion to the agentic-risks piece. Its
central, transferable argument: **fully design the responsible-AI (RAI) program before
implementing it, then implement in phases** — do not take "baby steps" in the design.
The authors give an eight-question readiness checklist; if you cannot answer "yes" to
all eight, slow the rollout and finish the design first. The audience is large
enterprises, but the discipline (design fully, phase the build) maps cleanly onto a
command writing an instruction.

## FACT — quoted (verbatim)

- "A responsible AI program (or 'RAI' program for short) not only builds guardrails for particular AI solutions and the teams that manage them, but it also defines the enterprise-wide policy, governance structures, roles and responsibilities, processes, and more that enable wide-scale deployment of AI."
- The observed failure pattern: "Companies are rushing to implement their RAI programs before they've finished designing them. The results are predictable: inefficient and difficult-to-scale efforts… wasted resources; and slowed innovation."
- On abstract values: "Many organizations have an RAI values statement. Almost every one of these includes a commitment to high-level concepts like fairness, privacy, transparency, safety, and accountability. The problem is that, articulated this abstractly, the values are impossible to implement." The fix is to "connect those values to procedures."
- Design vs implement: "a phased rollout of the RAI program is highly recommended… However, this must be distinguished from taking baby steps in the *design* of the program. The program should be designed as fully as possible prior to implementation."
- Building analogy: better to "complete the design of the four-wing building and then build in phases than… build a single wing and figure out later how to make additions." And: "completing design of an RAI program requires far fewer resources than implementation."

## FACT — paraphrased: the eight readiness questions

1. **Have you determined the strategic objectives of your RAI program?** Best-in-class, skate by current regulation, or be ready for pending regulation? This drives how you design risk assessments, augment workflows, run audits, and set thresholds for escalation and go/no-go decisions, and which stakeholders (vendors, suppliers, partners) are held to the same standards.
2. **Are your RAI values clearly connected to procedures?** Abstract values are unimplementable; tie each value to concrete procedures (e.g., "fairness" → identify which stakeholders might be discriminated against at each lifecycle stage, and confer with them when risk is high).
3. **Have you designed RAI metrics (KPIs and OKRs)?** Distinguish metrics for the *program* from metrics for individual models. Measure employee awareness, employee compliance (including when overseeing others' AI use), whether the program produces desired impacts, and whether improvement efforts succeed. Decide what to measure, who collects, frequency, targets/benchmarks/thresholds, and deployment rate.
4. **Have you trained the people overseeing the program?** The RAI committee is cross-functional; its weaknesses are that members over-focus on their own expertise, some risks sit outside everyone's expertise, and members are not experts at *running* an RAI program. Alignment training/workshops address this.
5. **Do you have the personnel you need?** Often no one has the skills; existing quality-assurance/quality-improvement (QA/QI) and audit teams "are not up to the task if they are not trained for responsible AI in particular." Two paths: hire new, or train existing (training existing is preferred to start; expect to hire as the program matures).
6. **How will the RAI program harmonize with other enterprise priorities?** It interacts with cybersecurity, privacy, and IT-optimization programs. Ask whether it interferes (don't stifle innovation), whether it augments (e.g., the cyber program), and what needs tweaking (HR, workflow, financial resources).
7. **Have you developed an RAI strategic roadmap?** Execution steps from design through implementation, monitoring, QA, and audit; plus budgeting, financing, oversight personnel, and management style. Decide cadence: enterprise-wide-simultaneous vs sequential-by-department/role.
8. **Have you designed an implementation playbook?** How the roadmap is executed per department, role, workflow, and AI-interaction type, with guidelines, checklists, and tutorials to ensure adherence.

## Assessment (relevance to this study / SRF-JRMC context)

- **Assessment.** The design-fully-then-phase principle is the single most transferable
  idea for the operator's task: write the complete governance design (not just the
  acceptable-use rules already drafted), then roll it out in phases. It argues against
  shipping a thin instruction and bolting on the missing pieces (inventory, metrics,
  validation function) later.
- Q2 (values → procedures) is a concrete test to run against any draft instruction: do
  its stated principles each resolve to a procedure, or are they abstract?
- Q5 reinforces the independent-evaluation/personnel gap flagged across this study:
  existing QA/audit staff are not RAI-capable without training.

## Cross-references

- Pairs with `[hbr-agentic-risks]` (same lead author; the "why it's urgent" companion).
- Q-checklist overlaps the seven primitives in `02_synthesis/landscape-report.md`
  (owner + body, metrics, training, harmonization, roadmap) and the corporate
  operating-model material in `01_sources/stream-2-corporate-enterprise.md`.

## Source note

Co-authors: Reid Blackman (Virtue) and Ingrid Vasiliu-Feltes, MD (former Chief
Compliance / Quality / Safety Officer in regulated industries; Senior Advisor at
Virtue). Practitioner checklist, not empirical research.

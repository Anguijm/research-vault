# Operator decisions — AI governance study

Operator (strategic-layer) decisions on the SRF-JRMC askSage governance work. These
resolve or refine items raised in `02_synthesis/gap-analysis.md`. Captured here so
they survive past the chat. The draft instruction is still not edited.

## 2026-06-19 — first decision batch

1. **CUI stays in; PII and PHI are carved out.** Controlled Unclassified Information
   (CUI) remains authorized on askSage up to Impact Level 5 — that is the point of the
   instance and it is unchanged. The carve-out is narrow: the **Privacy (PII)** and
   **Health (PHI)** categories of CUI are *not* valid candidates for askSage, even
   though they are technically CUI. This resolves the discrepancy flagged at
   gap-analysis F.5 Q2 by matching the DoD GenAI.mil line, which authorizes CUI but
   prohibits PII/PHI even at IL5. Rationale: PII and PHI carry independent legal
   regimes (Privacy Act, HIPAA) on top of CUI handling, and they are the worst case for
   the mosaic/aggregation risk. *(Data-classification call — operator's to make.)*

2. **Technical adjudication belongs to the CHENG (Chief Engineer) and the CHENG's
   chain.** Adjudicating a technical question — a weld spec, a torque value, the kind
   of thing the human-in-the-loop exists for — is done by a qualified person in the
   CHENG's chain, not by the general end user and not by the CIO. This confirms the
   "Technical Authority supremacy" finding (gap-analysis priority #1) and confirms the
   **CHENG** billet, which the red team raised and the study had deliberately declined
   to assert until the operator confirmed it. *(Refinement: the technical
   human-in-the-loop is the right qualified person, which also blunts the
   confirmation-fatigue risk.)*

3. **IT and information security aspects are CIO-level responsibility** (including the
   ISSM). So ownership is a deliberate split: the **CHENG chain** owns technical /
   functional adjudication; the **CIO** owns the information-technology and
   information-security side. It will likely be a **combination of people** managing
   the program, not a single owner. *(This is the realized, command-native form of the
   "bifurcated ownership" finding at gap-analysis F.2.)*

4. **Record retention and legal hold need a Legal chop.** The records/legal-hold
   provisions (gap-analysis F.1 item 2 / priority #4) should be reviewed and approved
   by Legal (Staff Judge Advocate / Office of Counsel) before they are set.

5. **Digital supervision is OUT OF SCOPE for the AI implementation.** The AI will not
   be a digital supervisor of anyone — this is broader and cleaner than the earlier
   "prohibit AI supervisor over Local National staff" control. Excluding digital
   supervision from scope entirely removes most of the Master Labor Agreement (MLA) /
   Status of Forces Agreement labor exposure at its root. *(Scope boundary — operator's
   to set. The residual MLA/ITAR concern is now only about a Local National user's
   agent inheriting that user's data access, not about AI-as-supervisor.)*

## 2026-06-19 — command context (refines, supersedes a red-team control)

6. **NOFORN is already barred from the SRF-JRMC network share, and all technical
   direction (drawings, policy, manuals) is screened by a derivative classifier who
   redacts or denies any unreleasable information before it reaches the share.** The
   command is mature at source-document handling. **Implication:** the cross-caveat
   "access-segmented index" control the logic red-team proposed (instruction finding #1)
   is largely redundant with this upstream process. The AI knowledge base **inherits**
   the already-screened corpus; it is not a new releasability authority. The remaining,
   narrower control is to keep askSage indexing *only* the screened authoritative corpus
   and to **prohibit ad hoc ingestion of un-screened source documents**, so the AI never
   becomes a bypass of the derivative-classifier screening. Folded into instruction
   v0.2.1 (§5.c, §7.c). *(General posture this reinforces: the instruction should inherit
   and reference existing command processes — screening, Quality Assurance, security —
   not rebuild them.)*

7. **Aggregation / classification-by-compilation is not a new AI risk — inherit the SCG,
   don't build an AI-specific control.** The operator's point: the aggregation risk does
   not change from the non-AI state. A human with the same share access can already
   compile a classified readiness picture by hand, and the Security Classification Guide
   (SCG) and spillage procedures already govern it for everyone, tool-agnostic. The only
   thing askSage changes is **likelihood/inadvertence** — it compiles fast across many
   sources, so a user may cross the compilation line without realizing it. **Resolution
   (instruction v0.2.1 §4.e):** inherit the SCG + spillage procedure; address the delta
   via training and user recognition; the earlier "compartment the agent / scope
   horizontal access" engineering control is demoted to an **optional defense-in-depth
   COMMAND DECISION** (it lowers inadvertent one-prompt compilation but does not reduce
   the underlying risk, since the user could compile manually anyway). Same posture as
   item 6: inherit existing command processes, don't rebuild them in the AI layer.

## 2026-06-19 — Section A strategic decisions (operator, via `_open-items.md`)

Folded into instruction **v0.3**.

8. **Instance basis: askSage, not GenAI.mil.** Rationale (operator): GenAI.mil is **not
   mature enough to merit convergence yet** ("maybe someday"); askSage already provides
   **ATO'd IL5** functionality and **connects to the Navy's Flank Speed shares**, so it is
   an accredited, integrated capability now. **Any process built in askSage is intended to
   be transferable to GenAI.mil when warranted** — convergence stays a future option, not a
   dead end. Framing correction: the command operates **under askSage's IL5 ATO** (askSage
   provides the accredited platform) and owns the governance layer; it does not own/build
   an ATO. Data residency is tied to the Flank Speed environment + askSage's ATO boundary
   (both accredited), which strengthens item 11's working assumption (working group still
   confirms the specific ATO reference + Flank Speed connection authority).
9. **Impact Level: IL5.**
10. **Maturity target: best-in-class.** Instruction now maps to the DoD AI Ethical
    Principles + NIST AI RMF functions and adds an annual (and on-significant-change)
    review cadence.
11. **Data residency: working assumption that existing accreditation/processes cover it**
    ("I'd think" — treated as a working assumption, NOT closed; working group confirms with
    the cognizant authority). Per [[feedback_dont_know_doesnt_mean_close]], left as a
    [CONFIRM], not resolved.
12. **Governance forum: Department Heads, quarterly** continuance-of-approval review of the
    use-case inventory. No new committee.
13. **Manual fallback (DDIL): immediate.** Every AI-enabled workflow must have an
    immediately-available manual fallback.
14. **Aggregation agent-scoping: DROPPED.** The optional defense-in-depth scoping measure
    is not adopted (friction without reducing the underlying risk).

## 2026-06-19 — per-department authoritative AI evaluator (instruction v0.4)

15. **Authoritative evaluation of AI output is generalized to the cognizant domain
    authority, and each department designates an evaluator.** Operator's refinement: rather
    than only "technical → CHENG," AI-produced content is authoritatively evaluated by
    whoever owns that subject matter — **technical → CHENG chain, IT/security → CIO,
    business/strategic → BSPO (Business Strategic Planning Office), other functional content
    → the cognizant department head/authority.** **Every department designates, in writing,
    an authoritative AI content evaluator** who evaluates their own domain's content and
    routes anything technical to the CHENG chain (the safety-of-life backstop). Folded into
    instruction **v0.4** (§6 generalized + new §6.b; §8.e adds the designation duty; §7.b
    cross-reference updated). The full domain-to-authority map is a working-group item.

## 2026-06-19 — real department structure + "AI changes no process" (instruction v0.5)

16. **Embedded the real SRF-JRMC department structure and removed the overbearing routing.**
    Operator provided the command's departments (Codes 100–1200; no 400/800/1000 — see
    `_glossary.md`). Governing principle, stated by the operator: **the AI does not change
    existing processes; responsibility falls along established command lines.** So:
    - **Deleted** the "for technical content the bar is highest / route everything to CHENG"
      language. A cost estimate doesn't go to the CHENG; 200 doesn't validate 300's schedule;
      nobody from 1200 runs apprentice training. Each department is the authoritative
      evaluator for AI content in its own area of responsibility (the §6.a table). No
      special safety-of-life routing sentence — existing QA and technical authority already
      enforce that.
    - **Federated knowledge base** (§5): each department owns, feeds, and controls access to
      its own repository; Code 200 owns the technical library + derivative classifier; the
      CIO/ISSM is custodian of the platform (connection registry, access, monitoring), not
      the content. Operator endorsed the "CIO would want to know which repos are connected"
      reasoning → light registry, not central content ownership.
    - **Records/directives generalized** to "in accordance with the command SORM" (operator:
      "I don't think we need to break everything out this granularly"), not granular
      Code-1100 mechanics. Added §3.e capstone: this instruction changes no existing
      authority or line of responsibility.
    Folded into **instruction v0.5**; routing package rebuilt; `_glossary.md` created.

## 2026-06-19 — dual-platform (askSage + GenAI.mil); trim §2 scope (instruction v0.6)

17. **The command uses BOTH askSage and GenAI.mil — supersedes the standalone framing of
    item 8.** Recommended split: **GenAI.mil for general questions; askSage for agentic work.**
    GenAI.mil may also be used to develop/refine agents and agentic-workflow prompts before
    spending askSage tokens (a token-economy practice; added to Annex A). GenAI.mil is not yet
    mature enough to host the command's agentic work, so askSage carries it for now, with
    transfer to GenAI.mil intended when it can. **The instruction stays askSage-specific**
    (GenAI.mil runs under its DoD enterprise governance); §2 acknowledges both and the split.
18. **Removed the entire §2 "Explicitly out of scope" block** (operator: the prohibited items
    are wordy and "no one thinks an AI would be used to supervise someone"). No substantive
    loss: prohibited data stays fully in §4; "AI output is always a draft / not an authority"
    stays in §3.a and §6.a. **Digital supervision (item 5) is therefore no longer stated in the
    instruction** — deemed unnecessary; the residual Master Labor Agreement / SOFA concern is
    still covered by least-privilege / permission-inheritance (§7.c). Item 5 stays as the
    historical record; this is the supersession note.

## 2026-06-19 — research context (NOT a decision): askSage authority basis + BigBear.ai ownership

Web research (`01_sources/asksage-genai-mil-adoption.md`) on two operator questions, with
implications for the §2 authority-basis `[CONFIRM]`:

- **The GenAI.mil mandate is an enterprise DEFAULT, not an exclusive ban.** Marine Corps:
  "prioritization of GenAI.mil does not limit the use of other LLMs"; Air Force: move to
  GenAI.mil "or other approved systems." So the v0.6 dual-platform framing is well-founded; a
  command runs askSage as a **separately authorized** capability + an acquisition vehicle (the
  Army's IL5/cArmy workspace on a $49M IDIQ is the public model).
- **But the DON mandate is the strongest of the services, and NO Navy command is a public
  askSage adopter** — the Navy bet on GenAI.mil. SRF-JRMC is early/unusual for the Navy, which
  raises the bar on **documenting its askSage authority basis** (the §2 `[CONFIRM]` marker).
- **Vendor change is material:** askSage is now owned by **BigBear.ai** (acquired $250M, closed
  Dec 31, 2025) and its founder-CTO Nicolas Chaillan departed Feb 28, 2026. Worth a vendor-
  continuity line in the platform-governance posture and the working-group authority confirm.

*(Surfaced for the operator; no instruction change made without direction.)*

## Still open — Section B/C, deferred to the working group

Per operator: the remaining items (Section B confirmations + Section C command-specific
code/role mappings in `_open-items.md`) are handled once the working group starts
reviewing the draft. They remain as `[CONFIRM]` / `[MAP TO COMMAND]` markers in
instruction v0.3.

> Full worksheet: [[_open-items]] (`_open-items.md`).

- **GenAI.mil vs. a standalone askSage instance**, and whether the command can inherit
  a higher-echelon Authority to Operate rather than standing up its own.
- **Maturity target** — compliance-minimum vs. best-in-class — which sets how heavy the
  eventual instruction should be.
- **Data residency / sovereignty** — where the IL5 data physically lives, host-nation
  admin-access and cryptographic questions.
- **Mapping the study's generic roles to the command's actual billets and codes**
  (the CHENG chain is now confirmed; the rest still to be mapped).

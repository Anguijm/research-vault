---
type: reference
purpose: Vault-wide primer on Organizational Conflict of Interest (OCI) in federal contracting
last_revised: 2026-05-24
---

# Organizational Conflict of Interest — primer

This is a vault-wide reference for the operator's use across opportunities. It is not legal advice. The authoritative source is the Federal Acquisition Regulation Part 9.5 (Subpart 9.5 — Organizational and Consultant Conflicts of Interest), and any specific OCI situation should be cleared with the contractor's contracts and legal teams before action is taken on it.

## What OCI is

Organizational Conflict of Interest, usually abbreviated OCI, is the federal-contracting rule that prevents a company providing services to the government from simultaneously being in a position to (a) give itself an unfair advantage in competing for related work, or (b) have its judgment on government matters compromised by other work the company is doing. The rule lives in FAR Part 9.5. Contracting officers are required to identify and mitigate OCI situations before contract award, and the consequences of an unmitigated OCI range from disqualification from a competition to cancellation of an existing award.

## The three flavors of OCI

Every OCI situation falls into one of three categories. The category matters because the mitigation pattern is different for each.

**Unequal access to information.** The contractor has access to non-public information from current work that would give them an unfair advantage in competing for follow-on or adjacent work. This includes operational data, internal processes, customer preferences, personnel knowledge, work products, and forward-looking signals about what the customer is planning to buy next. This is the most common flavor for defense services incumbents because being on contract at all gives the contractor access to material that outside bidders do not have.

**Biased ground rules.** The contractor wrote or helped write the requirements, specifications, or statement of work that they are now bidding on. This includes situations where the contractor was paid to do market research, requirements definition, or feasibility studies that produced the bid documents. Mitigation is harder because the contractor has shaped the playing field, not just gained information about it.

**Impaired objectivity.** The contractor's other work or relationships could compromise their judgment on the matter at hand. This is most relevant for advisory work, assessments, evaluations, source selection support, and similar tasks where the contractor's analytical conclusions are the deliverable. Less relevant for product or service procurement directly.

## Standard mitigation pattern

When an incumbent contractor wants to bid on follow-on or adjacent work, the standard remediation pattern has four components.

**Documented organizational firewall.** The proposal team is segregated from the operational team. No shared people, no shared work products, no shared physical workspace if practical. The firewall is captured in a written plan that names the personnel on each side and the procedures for any cross-side communication. Personnel can be moved back and forth only with documented re-clearance.

**Public-information-only proposal content.** Every claim in the proposal is based on publicly-available information plus general operator knowledge. Contract-specific data, customer-internal documents, and operational artifacts produced under the existing contract do not enter the proposal artifact. This is the discipline that the vault's named-entity audit, source-supported FACT labeling, and contact-protection rule were designed to support.

**Formal disclosure to the contracting officer.** The contractor formally discloses the existing contract and the OCI mitigation plan to the contracting officer on the new competition, usually in writing. The contracting officer either approves the mitigation plan, requires changes to it, or determines that the OCI is unmitigable and disqualifies the contractor.

**Written letter authorizing the bid.** The contracting officer issues a letter or other instrument formally acknowledging that the bid is allowed and what restrictions apply. Without that letter, the bid is at risk of being rejected at any point in the competition.

In some cases — usually when the OCI is large and difficult to mitigate — the contracting officer can require the incumbent to choose: keep the existing contract and forgo the bid, or pursue the bid and divest the existing work to a different contractor. This is the most severe outcome and appears only when the OCI is structural rather than mitigable.

## How this discipline maps to the vault

The vault was designed with OCI hygiene as one of several backstops, even though the OCI label was not used explicitly until this primer was written.

The named-entity audit at `_scripts/audit_named_entities.py` forces analytical content to be source-supported and flags any commercial entity name in vault content that is not in any ingested source. This catches the case where an analyst inadvertently writes operator-knowledge about a contractor into the analytical research file.

The FACT / Assessment / Speculation labeling discipline in the SOP at `_meta/sop.md` makes the basis for every claim explicit. A claim labeled FACT must have a citation tag pointing to an ingested public source. A claim labeled Assessment is the analyst's reasoned judgment from public material. A claim labeled Speculation is forward-looking guesswork. None of these labels can rest on operational data from a contract relationship.

The contact-protection note in section 9.3 of each opportunity's research file explicitly carves operator working-level knowledge out of the file. The contact's framing scopes the research; it does not enter the FACT chain.

The named-entity-discipline memory at `feedback_named_contractor_discipline.md` records the operator's rule that named contractors, products, and people do not enter analytical content unless ingested sources surface them organically.

Together, these disciplines mean that the vault's analytical content should be reviewable by a contracting officer evaluating OCI risk without exposing the contractor to disqualification. The vault is the proposal-content side of the firewall. Operational data, personnel details, and customer-internal context from any existing contract stay outside the vault.

## What to do before a bid

Before any proposal work begins on a vault opportunity, the operator should clear three things with the relevant contractor's contracts or legal team.

First, whether the existing contractor relationship at the candidate customer permits a bid on the new work. The answer for most defense services incumbents is "yes with restrictions," but the specifics matter — particularly whether any subset of the new work overlaps with the existing scope of work, and whether any personnel involved in the new bid have had access to non-public information.

Second, what the contractor's standard firewall procedure is for incumbent-pursues-follow-on situations. Most major defense services contractors live in this situation constantly and have a well-established procedure. The procedure should be documented and the proposal team should be staffed in accordance with it.

Third, what formal disclosure the contractor needs to make to the contracting officer on the new competition. The disclosure usually includes a statement of the existing contract, the personnel involved, the information accessed, and the mitigation plan being applied. The contracting officer's written response is the gating event before any final proposal is submitted.

## When OCI does not apply

Not every situation where a contractor is in a position to know something useful about a customer creates an OCI. The rule applies specifically to non-public information acquired through a contract relationship that gives the contractor an unfair competitive advantage. It does NOT apply to:

Publicly-available information about the customer, including the customer's published budget, public solicitations, congressional testimony, GAO reports, DoD press releases, and any other primary source the analyst would ingest into the vault.

General industry knowledge about how the customer's organization works, what its mission is, what its typical procurement patterns are. This is the kind of knowledge any defense services professional has and that doesn't depend on holding a specific contract.

Knowledge gained at industry days, formal SBIR/STTR engagements, BAA white-paper exchanges, or other engagement on-ramps that are open to the broader industry. Information shared through these formal channels is not OCI-tainted because every competing bidder has equal access.

The line between OCI-relevant non-public information and non-OCI general knowledge is sometimes blurry. When in doubt, the contractor's contracts or legal team is the authoritative interpreter. The vault should err on the side of source-supported public material and treat any operator-side knowledge about specific contractor positions, personnel, or operational details as OCI-relevant and therefore out-of-scope for analytical content.

## Cross-references

- The vault SOP at `_meta/sop.md` — verification rules and FACT/Assessment/Speculation labeling.
- The named-entity discipline memory at `feedback_named_contractor_discipline.md` — do not introduce named entities into vault content unless sources surface them.
- The contact-protection discipline in section 9.3 of any opportunity research file — operator working-level knowledge stays out of the file.
- The entity-provenance-check skill at `_meta/entity-provenance-check.md` — pre-execution audit for OCI-relevant entity contamination.

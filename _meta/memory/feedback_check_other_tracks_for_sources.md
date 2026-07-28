---
name: check-other-tracks-before-declaring-a-source-gap
description: "the operator's other vault tracks routinely already hold the source an opportunity needs; search them before concluding the evidence does not exist"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 47b5ca29-ff88-45d9-8fa4-924c4cd2c690
---

Before writing "public sources do not show X" into a brief, **search the operator's other tracks and
the second-brain vault.** Twice on 2026-07-28 the decisive source for BDR-FLEET-READINESS was already
in the operator's own material and had simply never crossed into the opportunity.

**Why.** The BDR capture brief carried a source-grounding caveat for two months stating there was no
confirmed Navy demand signal. Both halves of the refutation already existed:

1. `trip-reports/MEGARUST-2026/` held the SWRMC executive director's 4 June 2026 keynote describing a
   Pacific battle-damage-repair program, with SRF-JRMC named as the coordinating command. The trip
   report even contained a line saying the BDR research file should incorporate it. Nobody did.
2. The second-brain vault at `/home/johnanguiano/brain` (`20_curated/projects/waterfront-brief/`)
   held a RAND study on battle damage repair, carried second-hand through Defense News. Retrieving
   the primary source (RAND RR-A470-9) produced the strongest evidence in the opportunity.

The vault's tracks are siloed by design, which is correct for provenance but means evidence does not
migrate on its own. The operator collects broadly across trip reports, newsletters and the brain
vault; the opportunity folders only see what was deliberately ingested into them.

**How to apply.**

- When an opportunity says a source gap exists, grep `trip-reports/`, `studies/`, other
  `opportunities/`, and `/home/johnanguiano/brain` for the topic before accepting the gap.
- Trip reports are primary sources. Conference keynotes by named government executives are citable
  and are often stronger demand evidence than budget documents or journal articles.
- When another track carries a claim second-hand, **go get the primary source.** The brain vault's
  own colophon says FACT there means the named source says it, not that it was independently
  verified, so a news article about a study is not the study. See
  [[reference_fetching_403_blocked_domains]] for reaching publishers that block the normal tooling.
- Cross-vault material still has to clear the ordinary classification and citation rules. Moving
  content from a trip report into a business-development artifact is a different use than the trip
  report itself, so surface it to the operator rather than assuming. Relates to
  [[project_private_non_osi_area]].

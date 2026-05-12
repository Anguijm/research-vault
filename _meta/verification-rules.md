# The six verification rules
**Printable reference. These are non-negotiable.**
Last extracted from SOP: 2026-05-11

---

## Rule 1 — Primary source over secondary

If Breaking Defense quotes a general, find the speech transcript on the .mil site or DVIDS and cite **that**. If a press release cites a contract value, find the SAM.gov / USAspending.gov / HigherGov record and cite **that**. Trade press is fine for color and analysis. It is not fine as the only citation for a factual claim.

**Primary sources hierarchy (best to worst):**

1. .mil sites, DVIDS, SAM.gov, USAspending.gov, comptroller PB books, GAO reports, congressional testimony, CRS reports
2. Company SEC filings (10-K, 10-Q, 8-K), investor day decks, official press releases
3. HigherGov, OrangeSlices.ai, GovTribe (these aggregate primaries)
4. Trade press: Breaking Defense, Defense News, DefenseScoop, Inside Defense, ExecutiveBiz, GovConWire
5. Think tank analysis: CSIS, RAND, CNAS, Hudson, AEI
6. Blogs, social media, single-author commentary

---

## Rule 2 — Two-source rule for non-trivial claims

Anything about money, timelines, named people, or organizational reporting needs two independent sources. If you can only find it once, mark it **"single-sourced"** in the brief.

Common single-source traps: contract ceiling values cited only by the awarded contractor; org charts derived from LinkedIn alone; dates pulled from secondary press without checking the primary release.

---

## Rule 3 — Date-stamp everything

Every fact in the research file gets a `[verified YYYY-MM-DD]` tag. POCs, contract ceilings, budget figures, org reporting lines — all of it rots fast. A fact verified six months ago is a hypothesis today. Re-verify all POCs and contract data **every 90 days** for active opportunities.

---

## Rule 4 — Label fact / assessment / speculation explicitly

Use the words. Every claim in your research file and your brief carries one of three labels:

- **FACT:** traceable to a primary source (cite inline).
- **ASSESSMENT:** your reasoned judgment based on multiple facts. Prefix with "Assessment:".
- **SPECULATION:** forward-looking inference not yet supported by evidence. Prefix with "Speculation:" and flag for review.

Reviewers should challenge any claim that does not carry one of the three labels. This is the single biggest defense against AI-induced overconfidence.

---

## Rule 5 — Adversarial review before any artifact ships

Before the capture brief or exec brief leaves your machine, someone else (the on-call analyst, ideally) tries to break it. Specifically: "find one claim you think is wrong or weakly sourced." If they find one, you fix it. If they find more than two, the brief isn't ready.

If no human is available, run the cross-AI red team described in `_meta/prompts/cross-ai-red-team.md`. It's not a substitute, but it's better than nothing.

---

## Rule 6 — Click every link

When AI gives you a citation, **open the link**. AIs hallucinate citations, including credible-looking ones. The 30-second click is the difference between professional intel and a blog post. This is non-negotiable.

> Note: an AI made one error in prior research — incorrectly attributing Alion's acquisition to CACI rather than HII. A 30-second click on the source would have caught it. Bake "click every link" into your habit; do not assume AI's confidence equals accuracy.

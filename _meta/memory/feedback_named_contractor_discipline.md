---
name: Do not introduce named entities unless ingested sources surface them
description: Specific commercial contractors, agencies, products, and people should appear in vault analytical content only when an ingested source surfaces them — not pre-emptively assumed from inferred context
type: feedback
originSessionId: 254eda7f-7db4-4f93-b460-1e14e2726754
---
When writing analytical content into a research file, glossary, decision log, points-of-contact directory, or derived deliverable, do not introduce a specific named entity (commercial contractor, product, named person, named program) unless that entity has been surfaced organically by an ingested source. Inferred context, plausible-sounding industry knowledge, and "I think I remember reading this" do not count as sources.

**Why:** the operator caught two recurring instances on 2026-05-23. First, the vault glossary's PAE-IO entry described it as an Amentum-owned subsidiary based on inferred context — that was wrong (PAE-IO is a Navy organizational consolidation). Second, even after the first correction, the vault's analytical content still named Amentum as the industrial-supply-side actor across §1 of the research file, the customer frontmatter, the points-of-contact scope note, and the source-file analytical notes. A grep of the 13 ingested source files confirmed Amentum appeared in zero of them. Every Amentum reference was analyst-introduced, not source-supported. That is a SOP rule 4 violation pattern: Assessment-level claims about specific entities written as if they were FACTs, with no citation backing.

**How to apply:**

- Before naming any specific commercial entity (contractor, vendor, named product, named person) in vault analytical content, grep the ingested sources in that opportunity's `01_sources/` for the name. If zero hits, do not write the name into analytical prose.
- **The same rule applies to search-config queries.** Do not pre-load a named entity into `_search-config.yaml` ai_searches or USAspending recipient queries unless the entity has already surfaced in an ingested source. Doing so pollutes the inbox with downstream matches that are then easy to mistake for organic surfacing. They are not organic; they are downstream of the analyst-seeded query.
- Inbox candidates that come from queries naming specific entities should be treated as suspect, not as "operator triage decisions." The honest path on cleanup is to remove the contaminated queries from the search config and move the affected inbox entries to `_rejected.md` so they don't get re-queued.
- Decision-log entries that record prior errors involving named entities are preserved as the historical record; this rule applies to forward-looking work, not to the append-only log.
- When the operator asks "are we tracking X?" and X has not appeared in a source, the honest answer is "X has not appeared in any ingested source; we have not verified X's role in this research."
- This rule pairs with the SOP's FACT / Assessment / Speculation labeling: pre-emptive entity-naming is almost always an unlabeled Assessment, which should be either labeled explicitly or excised.

**Specific operator correction (2026-05-23):** the operator caught a self-validating loop where I (a) wrote Amentum into the vault glossary as an assumption, (b) added Amentum-named queries to `_search-config.yaml`, (c) ran find_sources which returned Amentum content, and then (d) called the resulting inbox hits "organic find_sources surfacing." The operator's correction: those hits are not organic, they are downstream of (a) and (b). Watch for this loop pattern across opportunities — it is easy to fall into when an entity feels obvious in context.

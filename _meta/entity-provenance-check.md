---
type: skill
name: entity-provenance-check
purpose: Catch inferred-fact-as-known-fact pollution between scaffolding and execution
when_to_invoke: Between scaffolding a new opportunity and the first find_sources pass; after every major scope expansion; before drafting any brief from the research file
last_revised: 2026-05-23
---

# Entity provenance check

This is a short alignment skill — about two minutes per run — focused on one question: for every specific named entity that has been written into the vault for this opportunity (research file, glossary, search config, points-of-contact directory), can the operator point at the source that introduced that entity, or should the entity be marked provisional?

The skill is named *entity-provenance-check* because the pollution pattern it catches is one of provenance: an analyst-introduced name that later looks like it came from a source.

The skill exists because of a specific incident on 2026-05-23 (see the BDR-FLEET-READINESS decision log). Claude had introduced the name "Amentum" into the vault glossary based on inferred context, then added Amentum-named queries to the search config based on the same assumption, and then characterized the downstream find_sources hits as "organic surfacing." Three layers of contamination, all from one inferred fact at the top. The operator caught it. This skill is the prevention pattern for the next time the same hazard appears.

## How Claude should behave

When this skill fires, do not start drafting, querying, or briefing yet. Run the two audits, then interview the operator on every flagged entity.

**Step 1.** Run `_scripts/audit_named_entities.py --opportunity <ID>`. This scans the analytical content for the opportunity and flags any named entity from the watchlist that appears in the research file, glossary, points-of-contact directory, or decision log but does NOT appear in any ingested source. Note the contaminated entries.

**Step 2.** Run `_scripts/audit_search_config.py --opportunity <ID>`. This scans `_search-config.yaml` for the same opportunity and flags any query that names a watchlist entity which is not in any ingested source. Note the contaminated queries.

**Step 3.** If either audit reports zero contaminated entries, the skill is complete. Move on with the work.

**Step 4.** If contaminated entries exist, ask the operator about each one specifically. For each flagged entity, the question is one of these three, in order:

1. *"This research file (or glossary, or search config) names `<entity>`, but the entity does not appear in any ingested source. Did you mean to introduce this name? If so, what source surfaced it?"*

2. *If the operator confirms they introduced it from a known external source:* "Should we ingest that source so the FACT chain has the citation?"

3. *If the operator does NOT recognize the entity, or says they did not introduce it:* the name should be removed from analytical content immediately. If it lives in a search query, the query should also be removed and any inbox candidates downstream of that query should be moved to `_rejected.md`.

**Step 5.** After cleanup, re-run both audits. The skill is complete only when both report zero contaminated entries.

## When this skill fires

The skill fires at four moments:

- Between scaffolding a new opportunity and the first `find_sources` pass against it. This catches any entity names that landed in the scaffold from inferred context.
- After any major scope expansion that adds new sections to the research file (e.g., the §11.3 BDA pipeline addition or the §11 engagement strategy addition on BDR). Scope expansion is the moment when new assumptions are most likely to creep in.
- After any source-recovery event where the operator manually pastes content. Manual paste is good for getting around fetch failures, but it also bypasses the normal ingest review path and is a moment when associated assumptions can leak.
- Before drafting any brief from the research file. The brief is operator-facing and is the wrong place for contamination to first be caught.

The skill is fast (the audits run in seconds), so the cost of running it more often than strictly necessary is low.

## Watchlist maintenance

The audits are only as good as the watchlist at `_meta/named-entities-watchlist.yaml`. If an opportunity introduces a new contractor, product, or program name that the watchlist does not cover, add it. The watchlist grows over time as the vault matures. Adding an entity to the watchlist does NOT mean the entity is contaminated — it just means the audits will track it going forward.

## Per-opportunity allowlist

Each opportunity can have a `_entity-allowlist.yaml` file at the opportunity-folder root. The allowlist excuses specific entities from the audit's "contaminated" bucket, on the operator's say-so. Use it when an entity is legitimately part of the research's analytical context but has not yet surfaced in an ingested source.

Format:

```yaml
allowlist:
  CACI: The operator's company. Baseline reference for any opportunity in this vault.
  ARKA: CACI subsidiary acquired March 2026. Operator-blessed cross-opportunity reference.
```

The key is the entity name (case-sensitive, matching the watchlist). The value is the operator's one-line reason — for future-self documentation, not for the audit logic.

Allowlisting an entity does NOT mean every claim about it is FACT. The verify-facts workflow still checks specific claims against specific sources. The allowlist resolves only the entity-presence audit, not the FACT-claim audit.

When the audit finds an allowlisted entity in analytical content with zero source backing, it reports it in an ALLOWLISTED bucket rather than a CONTAMINATED bucket, and does NOT fail. The allowlisted bucket is informational — the operator can see at a glance which entities are riding on operator-knowledge alone, in case any of them eventually warrant a source.

## What this skill does NOT do

This skill does not check FACT claims line-by-line against their cited sources. That is the job of `verify_facts.py`. This skill checks the *existence* of named entities in analytical content, not whether the specific claims about them are accurate. The two complement each other: this skill catches pollution at the entity level; the verifier catches it at the claim level.

This skill also does not flag non-entity assumptions (e.g., "the Navy is planning a 50% increase in distributed shipbuilding"). Those are caught by the verifier when they make it into a FACT claim. The skill's scope is entity provenance only.

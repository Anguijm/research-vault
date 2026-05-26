---
type: red-team-dialogue
opportunity: BDR-FLEET-READINESS
scope: Plan the AI-only diagnostic for the 0-candidate find_sources pass executed 2026-05-25
drafting_model: Claude (Anthropic) drafting the v1 / v2 / v3 plans
reviewing_model: Gemini Pro (Google) red-teaming each plan revision
rounds_completed: 2
date: 2026-05-25
---

# Iterated cross-AI red-team — diagnostic plan for 0-candidate find_sources pass

## Why this dialogue exists

The 2026-05-25 find_sources pass against the refreshed `_search-config.yaml` (60 queries — 50 AI, 11 SAM, 7 USAspending) returned `0 AI + 0 SAM + 0 USA = 0 new candidates queued`. The cause for SAM (429 rate-limit) and USAspending (HTTP 500 outage matching the 2026-05-21 pattern) is visible in the truncated tail of the run. The cause for 0 AI candidates is not — the per-query stdout for the 50 AI queries was hidden behind a `tail -80` truncation in the original bash invocation, and the re-run hung in TCP SYN-SENT to an AWS endpoint for 45+ minutes before being killed.

Before running a diagnostic, the operator required the diagnostic plan itself to go through iterated cross-AI red-team — the same pattern used in the 2026-05-25 right-to-win-reframe and corpus-cleanup dialogues. The goal of the red-team: ensure the diagnostic is bounded, reversible, and hypothesis-distinguishing in a single fault-isolation round.

## Round 1 summary — Claude's v1 plan, Gemini's six challenges

Claude's v1 plan proposed: build a diagnostic config (10 buyer-triad queries + 2-3 baseline queries), add a single print statement after `searcher.search()` returns, run with `--dry-run` plus `tee` to a log file, bucket the output by hypothesis.

Gemini surfaced six challenges:
1. **TCP SYN-SENT mitigation weak.** The `timeout 600` wrapper bounds blast radius but diagnoses nothing if the hang occurs *inside* the AI service call — the post-call print never executes.
2. **Missing H6: URL Validation network block.** URL validation makes HTTP GETs against candidate URLs; a WAF-blackholed `.mil` URL hangs in SYN-SENT exactly the way the re-run did.
3. **Missing H7: OpenAI Ranker Failure.** If OpenAI degraded, the script could silently produce 0 candidates.
4. **`--dry-run` gamble unacceptable.** The v1 plan said "need to confirm" whether `--dry-run` skips network calls — not acceptable to present to operator with unresolved core mechanism.
5. **Single-round assumption unrealistic.** The plan should be reframed as fault isolation, not root cause + fix.
6. **Print statement brittle.** `results[0].get('url')` crashes if results isn't a list of dicts.

## Round 2 — Claude's responses

Claude accepted challenges 1, 2, 5, 6 and partially-accepted 3.

**Pushback on Challenge 4 (Claude's pushback).** Claude read `find_sources.py` and `_scripts/lib/inbox.py` to ground the `--dry-run` semantics. Result: `--dry-run` does NOT skip network calls; it only suppresses the `inbox.append_candidates` file write (the function prints the candidate block to stdout instead). Every AI search, every URL validation HTTP GET, every OpenAI ranker call still runs unchanged. So `--dry-run` is exactly the right mechanism — full diagnostic network visibility with zero inbox pollution. Gemini's alternatives (`--out` flag, opportunity rename) don't exist in this codebase and would be more invasive than the already-safe native mechanism. Gemini's worry was valid but the mechanism stands.

**Gemini's Round 2 response — CONCEDED:** "You absolutely nailed the pushback on Challenge 4. This is exactly why reading the code beats assuming standard conventions. If `--dry-run` retains all network calls and only suppresses the disk write, it is the perfect native mechanism. I concede the point entirely."

Claude then asked two challenges back to Gemini:

**C1 (Claude → Gemini) — Is three-stage bracketing sufficient?** v2 brackets three network stages with BEFORE-and-AFTER prints: A=`searcher.search()`, B=`ranker.resolve_and_validate()`, C=`ranker.rank_candidates()`. Each "BEFORE" print states the stage; each "AFTER" print states the result or error. If the script hangs, the last BEFORE without a matching AFTER tells us which stage hung. Is three stages enough, or should the diagnostic also bracket inside `searcher.search()` for intra-search visibility?

**Gemini's response — three stages sufficient.** "You correctly reframed the goal of this pass as fault isolation, not root-cause analysis. If `searcher.search()` hangs, we don't need to know yet whether it was Claude, Gemini, or a SERP API that caused it. We just need to definitively point the finger at `searcher.py` and rule out the URL validator and ranker. Adding intra-search prints right now violates the 'isolate the domain first' principle." Convergence on three stages.

**C2 (Claude → Gemini) — Is H7 actually load-bearing?** Looking at `rank_candidates`, the ranker uses per-candidate try/except inside a ThreadPoolExecutor. A partial ranker failure yields candidates with `_score = '?'`, not an empty list. For H7 to produce literally 0 candidates queued, the ranker would have to either (a) fail *before* the thread pool (which would throw an unhandled exception and produce a stack trace, not a silent "0 candidates queued" success), or (b) `find_sources.py` would have to apply a post-ranking drop filter that hits every candidate. Neither matches the observed exit-0 + 0-queued result. So H7 looks subsumed by H1/H3 unless there's a strict post-rank filter Claude missed.

**Gemini's response — CONCEDED H7 is a phantom.** "You are exactly right—H7 as currently stated is a phantom hypothesis. Because of the per-candidate try/except inside the thread pool, a partial ranker failure results in degraded data, not an empty list. ... Unless there is a strict post-ranking drop filter in `find_sources.py` that you haven't mentioned, H7 is subsumed. I recommend dropping H7 entirely to keep the diagnostic matrix tight." Convergence: H7 dropped.

## Gemini's one minor improvement on top of v2

The v2 plan used a multi-line shell command for config swap-and-run with reversion at the end. Gemini noted that `&&` chains don't revert on timeout/crash, and `;` is brittle to `Ctrl+C`. **Tweak:** use a subshell with an `EXIT` trap so config reverts no matter how the command terminates (timeout, crash, signal). Claude accepted.

## Final converged plan (v3) — approved by both models

### Goal

Localize the failure domain that produced 0 candidates queued in the 2026-05-25 find_sources pass. This is a **fault isolation round** — it identifies which stage failed, not the fix. A second round may be needed to root-cause within the identified stage.

### Hypotheses (final set, H7 dropped per Round 2)

- **H1.** `searcher.search()` returns 0 results for every query (AI service returning empty — buyer-triad queries too narrow, or AI service degraded for this topic space).
- **H1'.** AI search hangs (TCP SYN-SENT) against the AI service endpoint — observable as `[A-pre]` print without matching `[A-post]`.
- **H2.** Results return but get fully deduplicated against `01_sources/` + `_inbox.md` existing URLs.
- **H3.** Results return, aren't dedup'd, but all get dropped at URL validation as invalid (404/403/index pages).
- **H5.** AI search service rate-limit / transient 429s.
- **H6.** URL validation hangs (TCP SYN-SENT) against a WAF-blocked candidate URL — observable as `[B-pre]` print without matching `[B-post]`.

### Approach

**Step 1 — Build diagnostic config** at `opportunities/BDR-FLEET-READINESS/_search-config-diagnostic.yaml` (NOT in `_scripts/` — kept with the opportunity for traceability) with two buckets:
- Bucket A: all 10 new buyer-triad queries
- Bucket B: 3 baseline queries from the existing config that have known recent matches in `01_sources/` (verified by checking source ledger entries dated 2026-05-23)

**Step 2 — Add three bracketed print pairs** to `_run_ai_search` in `find_sources.py`, each marked with `# DIAGNOSTIC 2026-05-25 — REVERT AFTER`:

```python
# Stage A: AI search call (around line 185)
print(f"  [DX][A-pre]  searcher.search('{query[:60]}...') starting...", flush=True)
results = searcher.search(query, date_window, max_candidates, use_claude, use_gemini)
print(f"  [DX][A-post] results type={type(results).__name__} len={len(results) if isinstance(results, (list, tuple)) else 'N/A'}", flush=True)

# Stage B: URL validation (around line 202)
print(f"  [DX][B-pre]  resolve_and_validate({len(new_candidates)} candidates) starting...", flush=True)
validated = ranker.resolve_and_validate(new_candidates)
print(f"  [DX][B-post] validated={len(validated)}", flush=True)

# Stage C: OpenAI ranker (around line 213)
print(f"  [DX][C-pre]  rank_candidates({len(validated)} candidates) starting...", flush=True)
validated = ranker.rank_candidates(validated, opp_context, openai_key)
print(f"  [DX][C-post] ranked={len(validated)} scores={[c.get('_score', '?') for c in validated]}", flush=True)
```

Each line uses `flush=True` (belt-and-suspenders with `-u`). Print statements are type-safe per Gemini's Challenge 6 fix.

**Step 3 — Execute** with subshell + EXIT trap (Gemini's Round 2 improvement) so config swap reverts on any termination:

```bash
(
  trap 'mv opportunities/BDR-FLEET-READINESS/_search-config.yaml.bak opportunities/BDR-FLEET-READINESS/_search-config.yaml 2>/dev/null && echo "[DX] Config reverted."' EXIT
  mv opportunities/BDR-FLEET-READINESS/_search-config.yaml opportunities/BDR-FLEET-READINESS/_search-config.yaml.bak
  cp opportunities/BDR-FLEET-READINESS/_search-config-diagnostic.yaml opportunities/BDR-FLEET-READINESS/_search-config.yaml

  timeout 600 python3 -u _scripts/find_sources.py \
    --opportunity BDR-FLEET-READINESS \
    --dry-run 2>&1 | tee /tmp/find_sources_diagnostic.log
)
```

- `timeout 600`: bounded blast radius for any TCP SYN-SENT hang.
- `-u`: unbuffered Python I/O.
- `--dry-run`: zero inbox pollution (confirmed by code read).
- `tee`: captures log even if stdout pipe closes.
- `2>&1`: stderr captured (catches diagnostic-print tracebacks).
- `trap ... EXIT`: config reverts on timeout, crash, or `Ctrl+C`.

**Step 4 — Bucket the log output by stage:**
- For each query: identify the last `[DX]` line printed. If `[A-post]` appears with len=0 → H1. If `[A-post]` never appears → H1'.
- After all queries: if `[B-pre]` appears but `[B-post]` doesn't → H6. If `[B-post]` shows validated << raw_total → H3.
- If `[C-pre]` appears but `[C-post]` doesn't → ranker hang (not in final hypothesis set but observable). If `[C-post]` shows scores all '?' → ranker degraded but not the 0-cause.
- Cross-reference Bucket A vs. Bucket B: if A produces 0 raw but B produces normal raw → H1 specific to buyer-triad queries. If both produce 0 raw → systemic.

**Step 5 — Write findings** to `opportunities/BDR-FLEET-READINESS/_red-teams/2026-05-25-find_sources-diagnostic-output.md`. Revert print statements via `grep -n "DIAGNOSTIC 2026-05-25 — REVERT AFTER"` to find every modification site, then remove. Confirm `_search-config.yaml.bak` no longer exists (the EXIT trap should have reverted). Surface findings to operator for next-action decision.

### Risks

- **R1** — Code modification. Mitigation: single sentinel comment string for grep-based reversion.
- **R2** — Resolved. `--dry-run` confirmed to skip only inbox writes (Gemini Challenge 4 conceded).
- **R3** — TCP hang. Mitigation: `timeout 600` + bracketed prints + `flush=True` + `-u`.
- **R4** — Baseline-query drift. Mitigation: pick baseline queries with known recent successes traceable to `01_sources/`.
- **R5** — Config swap not reverted. Mitigation: subshell + EXIT trap guarantees reversion regardless of termination cause (Gemini Round 2 improvement).

### Expected outcomes

- One of H1, H1', H2, H3, H5, H6 should be cleanly identified after the run.
- If buyer-triad queries (Bucket A) produce 0 raw but baseline (Bucket B) produces normal raw → operator's next move is to rewrite the buyer-triad queries.
- If both produce 0 raw → AI service issue, retry-later is the move.
- If validation drops everything → H3, investigate which URLs are getting dropped.
- If validation hangs → H6, identify the WAF-blocking URL.

## Convergence statement

Both models converged on v3. The plan is bounded (600s timeout), reversible (EXIT trap + sentinel grep), hypothesis-distinguishing (six hypotheses each map to a specific log signature), and observable (per-stage bracketed prints with `flush=True`). Ready for operator approval before execution.

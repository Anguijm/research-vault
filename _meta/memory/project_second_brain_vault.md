---
name: project_second_brain_vault
description: "Personal \"second brain\" Obsidian vault at /home/johnanguiano/brain, separate from the defense research vault, with an AI topic-expansion engine and a staging-to-promote gate."
metadata: 
  node_type: memory
  type: project
  originSessionId: 52291d96-1006-48e2-ba61-eaa04c19659d
---

Built 2026-06-15. A personal knowledge vault at `/home/johnanguiano/brain`, fully separate
from the defense research vault at `/home/johnanguiano/research`. Three locked architecture
decisions (settled via cross-AI red-team):

1. **Library model.** New separate vault. The research vault is mounted read-only at
   `brain/_library/research` (symlink); personal automation never writes into it. Verified:
   the expand engine left the research vault's mtime unchanged.
2. **Staging to Curated.** AI output lands in messy `10_staging/<topic>/`; the operator
   promotes keepers into PARA-light `20_curated/{projects,areas,resources,archive}/`.
   Promotion is operator-only, the gate where understanding is built. Do NOT promote on the
   operator's behalf; that undercuts the whole design.
3. **Full loop, staged + unverified.** Everything AI-produced is labeled Assessment or
   Speculation, never FACT, with `source_tier` and `ai_generated` flags. FACT is reserved
   for operator-verified, primary-sourced claims at promotion.

Governing risk to keep visible: **epistemic decoupling** (breadth of storage outrunning
depth of understanding). The promotion gate is the defense.

**The engine:** `brain/_scripts/expand.py "<topic>"` generates queries (Claude), web-searches
(`lib/searcher.py`, Claude web_search + optional `--use-gemini`), dedups/ranks by tier,
ingests via `ingest.py` into `10_staging/<topic>/sources/`, then drafts `synthesis.md`
(labeled, with a source ledger + open questions). Run with the vault's own venv:
`brain/_scripts/.venv/bin/python3` (has anthropic, google-genai, trafilatura, curl_cffi).
Front page is `brain/Home.md` (Dataview, narrative-first, staging-to-promote queue on top).

Reuse note: fetchers (`lib/fetchers/*`) were copied verbatim from the research vault;
`routing.py`/`frontmatter.py`/`ingest.py`/`searcher.py` were re-cut brain-native (open-web
tiering, no defense bias). `verify_facts.py`/`red_team.py` were intentionally NOT ported:
the manual promotion gate is the brain's verification model. Plan file:
`~/.claude/plans/ok-i-want-to-iridescent-rocket.md`.

**Headed Playwright (2026-06-16):** `lib/fetchers/playwright_headed.py` launches visible
Chromium on `DISPLAY=:1` with `playwright_stealth.stealth_sync`, detects captcha/bot-check
interstitials, and (interactive mode) pauses for the operator to solve them in the window.
`ingest.py --render auto|fast|headed` (auto escalates to headed when the curl fetch looks
walled/empty). Confirmed: it bypasses the NCBI/PubMed reCAPTCHA wall that gave curl_cffi a
525-byte page, pulling the full 71KB article. Browsers are shared from `~/.cache/ms-playwright`.

**Git + web access (2026-06-16):** brain is git repo "B2 Electric Bugaloo" (README +
`.git/description`), branch `main`. NOT local-only (operator explicitly wants it web
accessible; the local-first rule binds only the defense research vault). Two GitHub repos
under account Anguijm:
- `github.com/Anguijm/brain` — PRIVATE source repo (whole vault). `.gitignore` excludes
  `_library/`, `_scripts/.venv/`, `_scripts/.env`, workspace json, pycache.
- `github.com/Anguijm/brain-garden` — PUBLIC Quartz 5 digital garden, deployed to GitHub
  Pages at **https://anguijm.github.io/brain-garden/** via `.github/workflows/deploy.yml`.
  Lives at `/home/johnanguiano/brain-garden/` (separate dir from the vault).

Publishing: `brain/_scripts/publish_garden.sh` rsyncs ONLY `20_curated/*.md` into the
garden's `content/`, commits, pushes (triggers Pages rebuild). Privacy by construction:
staging/inbox/_meta/_library can never reach the public site. `draft: true` on a curated
note keeps it off the garden. The site starts empty (curated is empty until promotion).

**Phone-first control (2026-06-16):** operator works the brain from a phone, away from the
laptop. Chosen mechanism is NOT Obsidian/git-plugin file sync but **Claude Code Remote
Control** (official, shipped Feb 2026; local CLI is v2.1.168 which supports it). The engine
(venv, Playwright, `:1` display, `.env` secrets) only exists on the laptop, so the phone is
a thin client into a local session. `brain/_scripts/remote.sh` launches
`claude --remote-control brain` inside a persistent tmux session (named `brain`) in the
vault with `DISPLAY=:1` set; attach from the phone Claude app or browser via QR. CONFIRMED
WORKING: this entire build (headed Chromium on :1, API calls with local .env secrets, two
GitHub repos created + pushed, live Pages deploy) was driven via Remote Control from the
operator's phone on 2026-06-15, so the plan/OAuth requirement is satisfied in practice. The
operator works phone-first; do not assume they are at a desktop. `brain/CLAUDE.md` gives
those remote sessions the vault's operating rules.

**Captcha handling (2026-06-16, settled = stealth + quarantine, free):** headed+stealth
auto-clears passive walls; genuinely interactive captchas are quarantined + flagged by
`ingest.py` (not ingested as captcha text). `expand.py` passes `--no-interactive` so
unattended/remote runs never block. No paid solver service.

Relates to [[feedback_avoid_em_dash_tell]], [[feedback_keep_draft_versions]], and
[[project_sync_architecture_decision]].

**Keep them separate (operator, 2026-07-29).** The two vaults are separate and should generally
remain so. Practical rules:

- **Read across, do not write across.** Searching the brain vault to find a source the research
  vault needs is correct and has paid off (see [[feedback_check_other_tracks_for_sources]]). Copying
  material between them, or unifying them, is not.
- **Do not push the brain repo from a research-vault session.** Committing locally when work
  genuinely belongs there is fine; pushing is the operator's call, and the vault feeds a public
  site. Asked and declined on 2026-07-29.
- **Route by subject, not by convenience.** NAMPIE 2026 (advanced manufacturing, CNRMC) was first
  filed into BDR-FLEET-READINESS and the operator corrected it to the brain vault. When something
  does not obviously belong to an existing opportunity, ask rather than parking it in the nearest
  active track.

**Discrepancy to be aware of (2026-07-29):** this memory says promotion to `20_curated/` is
operator-only, but `brain/CLAUDE.md` rule 2 currently instructs the assistant to promote keepers
itself. They conflict. The in-repo CLAUDE.md is the authority for work done inside that vault, but
given `20_curated/` publishes publicly, default to staging and flag anything questionable rather
than promoting it.

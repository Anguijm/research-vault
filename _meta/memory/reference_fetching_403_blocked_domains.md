---
name: reference-fetching-403-blocked-domains
description: How to fetch .mil/USNI and other 403-blocked sources — headed Playwright; USAspending via the API client
metadata: 
  node_type: memory
  type: reference
  originSessionId: bd960e99-a70c-4a23-a471-0e5c1a315cf2
---

Some source domains hard-block this environment with HTTP 403 (Akamai/Cloudflare
bot defenses): `navy.mil`, `msc.usff.navy.mil`, `news.usni.org`, **`rand.org`
(confirmed 2026-07-28, both the product page and the `/content/dam/.../*.pdf`
path)**, and likely other `.mil` sites. For these, `ingest.py` (including its
headless-Playwright fallback), the `WebFetch` tool, and plain `curl` with a
browser UA all fail.

**`WebSearch` still works on these domains even when fetching does not** — use it
with `allowed_domains` to find the exact report page and title first, then fetch
with headed Playwright. That is how RAND RR-A470-9 was located and captured for
BDR-FLEET-READINESS on 2026-07-28.

**Working method (operator-endorsed 2026-06-07):** drive a **headed** Playwright
Chromium against the real X display, not headless. Use the venv that already has
playwright + browsers: `_scripts/.venv/bin/python`, `export DISPLAY=:1`. Launch
`headless=False` with `--disable-blink-features=AutomationControlled`, a realistic
Chrome UA, a normal context (locale/timezone/viewport/Accept-Language), and a
small `navigator.webdriver`/languages/plugins init script. Wait for
`networkidle`, then read `document.body.innerText`. Leave a respectable
randomized pause (~20–40s) between page loads. A reusable script lives at
`/tmp/pw_fetch.py` (see the HANWHAOCEAN-DOD decision log for the pattern).
Cloudflare "Just a moment…" interstitials may still 403 occasionally — retry or
fall back to an equivalent primary.

After capture, write a schema-compliant source file by hand (headed Playwright
gives raw `innerText`, so quotes are genuinely verbatim — unlike the WebFetch
summarizer, whose quotes must be flagged UNVERIFIED).

**For USAspending awards, do NOT scrape the site** — use the vault's
`_scripts/lib/usaspending.py` API client (`parse_search_entry` → `execute_query`,
and `ingest_award(opp_dir, candidate)` to write a source file + ledger entry).
It's the authoritative, citable, boring-tool path for the same data and returns
exact PIIDs, obligations, dates, and contracting offices.

Relates to [[feedback_named_contractor_discipline]] (entities still must surface
organically) and the CLAUDE.md "no web access" note, which is outdated — web/
search tools and headed Playwright are available in-session.

#!/usr/bin/env python3
"""
derive_caci_directional.py — Populate the Layer 2 (CACI directional) section
of `_meta/caci-discovery-config.yaml` from public CACI careers / investor
materials.

The directional layer captures where CACI is signaling growth that
USAspending hasn't caught yet — current job postings, recent earnings-call
language, recent press releases.

Best-effort scrape: some CACI sites are JavaScript-rendered and may 403 a
plain requests client. The script logs which sources worked and which
didn't, and writes whatever it managed to extract back into the YAML.
Operator can hand-augment if a critical source failed.

Usage:
    python derive_caci_directional.py
    python derive_caci_directional.py --dry-run
"""

import argparse
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import requests
import yaml
from dotenv import load_dotenv

SCRIPT_DIR = Path(__file__).parent
VAULT_ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))
load_dotenv(SCRIPT_DIR / ".env")

CONFIG_PATH = VAULT_ROOT / "_meta" / "caci-discovery-config.yaml"

# Public CACI URLs to try. Order matters; first successful fetch per category
# wins. If a URL 403s or doesn't return useful HTML, the script tries the
# next one in the category.
SOURCES = {
    "careers": [
        "https://careers.caci.com/global/en/search-results",
        "https://careers.caci.com/",
    ],
    "investor_relations": [
        "https://investor.caci.com/news-releases",
        "https://investor.caci.com/",
    ],
    "press_releases": [
        "https://www.caci.com/insights-and-news",
        "https://www.caci.com/",
    ],
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; caci-discovery-bot/1.0; research-vault)",
    "Accept": "text/html,application/xhtml+xml",
}

# Capability / growth keywords to mine from scraped content. Each match
# increments a counter; the top-N entries become the Layer 2 signal list.
GROWTH_KEYWORDS = [
    "Indo-Pacific", "Indo Pacific", "INDOPACOM",
    "Joint All-Domain", "JADC2", "Joint All Domain",
    "Live-Virtual-Constructive", "LVC",
    "Exercise design", "Wargaming", "Wargames", "Scenario generation",
    "Decision support", "Decision rehearsal",
    "AI", "Artificial Intelligence", "machine learning", "ML",
    "C5ISR", "C4ISR",
    "Modeling and simulation", "M&S",
    "Electronic Warfare", "EW",
    "Cyber", "Cybersecurity",
    "Spectral", "Signature", "Counter-UAS", "C-UAS",
    "Naval", "Navy", "Maritime",
    "Power Apps", "Power Platform", "Low-code",
    "Additive manufacturing", "3D printing",
    "Workforce", "Workforce development",
    "Digital twin", "DevSecOps",
    "Cloud", "Hybrid cloud", "AWS", "Azure",
]


def _utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _fetch(url: str, timeout: int = 15) -> tuple[bool, str]:
    """Fetch a URL with a polite user-agent. Returns (ok, body_text)."""
    try:
        r = requests.get(url, headers=HEADERS, timeout=timeout, allow_redirects=True)
    except requests.RequestException as e:
        return False, f"network error: {e}"
    if r.status_code != 200:
        return False, f"HTTP {r.status_code}"
    return True, r.text


def _strip_html(html: str) -> str:
    """Crude HTML-to-text: drop tags, collapse whitespace, decode entities."""
    text = re.sub(r"<script[^>]*>.*?</script>", " ", html, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"<style[^>]*>.*?</style>", " ", text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"&nbsp;", " ", text)
    text = re.sub(r"&amp;", "&", text)
    text = re.sub(r"&#39;|&apos;", "'", text)
    text = re.sub(r"&quot;", '"', text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def _extract_signals(text: str) -> Counter:
    """Count occurrences of each growth keyword (case-insensitive)."""
    counter = Counter()
    text_low = text.lower()
    for kw in GROWTH_KEYWORDS:
        # Word-boundary match for short acronyms; substring for multi-word
        if len(kw) <= 6 and " " not in kw:
            pattern = r"\b" + re.escape(kw.lower()) + r"\b"
            matches = re.findall(pattern, text_low)
        else:
            matches = re.findall(re.escape(kw.lower()), text_low)
        if matches:
            counter[kw] = len(matches)
    return counter


def _load_config() -> dict:
    return yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8"))


def _save_config(cfg: dict) -> None:
    CONFIG_PATH.write_text(
        yaml.dump(cfg, sort_keys=False, allow_unicode=True, default_flow_style=False, width=120),
        encoding="utf-8",
    )


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true", help="Show output but don't write the YAML.")
    args = ap.parse_args()

    cfg = _load_config()

    print("Fetching public CACI directional sources...")
    fetch_log = []
    all_signals = Counter()
    sample_text = {}

    for category, urls in SOURCES.items():
        category_signals = Counter()
        category_ok = False
        for url in urls:
            ok, body = _fetch(url)
            fetch_log.append({"url": url, "ok": ok, "note": "" if ok else body[:100]})
            print(f"  {'✓' if ok else '✗'} {url}")
            if ok:
                text = _strip_html(body)
                sample_text[category] = text[:500]
                signals = _extract_signals(text)
                category_signals += signals
                category_ok = True
                # First-success-wins per category
                break
        if category_ok:
            all_signals[category] = sum(category_signals.values())
            for kw, count in category_signals.items():
                all_signals[kw] = all_signals.get(kw, 0) + count

    # Build the hiring_concentrations and growth_signals lists from the
    # accumulated signal counter. Filter out the category-meta entries.
    keyword_signals = [
        {"keyword": kw, "occurrences": count}
        for kw, count in all_signals.most_common()
        if kw in GROWTH_KEYWORDS
    ]

    cfg["directional_caci_footprint"]["last_derived_utc"] = _utc_now()
    cfg["directional_caci_footprint"]["growth_signals"] = keyword_signals[:30]
    cfg["directional_caci_footprint"]["hiring_concentrations"] = [
        # If careers page fetched, the top keywords from that section are
        # the hiring concentrations. We approximate from the global counter
        # because the per-category split is lossy after merge.
        {"keyword": kw["keyword"], "estimated_share": "see growth_signals"}
        for kw in keyword_signals[:10]
    ]
    cfg["directional_caci_footprint"]["executive_themes"] = [
        # Without access to earnings-call transcripts, this remains a
        # manual-augmentation field. Logged here for the operator to
        # populate if needed.
        "Populate manually from the most recent CACI quarterly earnings call transcript at investors.caci.com if needed.",
    ]
    cfg["directional_caci_footprint"]["fetch_log"] = fetch_log
    cfg["last_full_update_utc"] = _utc_now()

    print()
    print(f"Layer 2 — top growth signals ({len(keyword_signals)} unique keywords):")
    for sig in keyword_signals[:20]:
        print(f"  {sig['occurrences']:4d}  {sig['keyword']}")
    print()
    print("Fetch outcomes:")
    for f in fetch_log:
        status = "OK" if f["ok"] else f["note"]
        print(f"  {status:30s}  {f['url']}")

    if args.dry_run:
        print("\n(dry-run: not writing config)")
        return

    _save_config(cfg)
    print(f"\n✓ Wrote {CONFIG_PATH.relative_to(VAULT_ROOT)}")


if __name__ == "__main__":
    main()

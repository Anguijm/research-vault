#!/usr/bin/env python3
"""
ingest.py — Source ingestion for the defense research vault.

Usage:
    python ingest.py <URL> --opportunity <ID> [--type auto|article|pdf|youtube] [--title "Override"]

Examples:
    python ingest.py https://www.pacom.mil/.../article/... --opportunity PMTEC-USINDOPACOM
    python ingest.py https://example.com/report.pdf --opportunity PMTEC-USINDOPACOM --type pdf
    python ingest.py https://www.youtube.com/watch?v=... --opportunity PMTEC-USINDOPACOM --type youtube
"""

import argparse
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

from dotenv import load_dotenv
from slugify import slugify

# Load .env from the same directory as this script
load_dotenv(Path(__file__).parent / ".env")

# Vault root is one level up from _scripts/
VAULT_ROOT = Path(__file__).parent.parent

# Add _scripts/ to path so lib/ imports work
sys.path.insert(0, str(Path(__file__).parent))

from lib.routing import route, get_source_tier, sanitize_domain
from lib.frontmatter import build_frontmatter
from lib.ledger import update_ledger


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Ingest a URL into the defense research vault.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    p.add_argument("url", help="URL to ingest")
    p.add_argument("--opportunity", required=True, metavar="ID",
                   help="Opportunity folder ID (e.g., PMTEC-USINDOPACOM)")
    p.add_argument("--type", choices=["auto", "article", "pdf", "youtube"],
                   default="auto", dest="content_type",
                   help="Content type (default: auto-detect from URL)")
    p.add_argument("--title", metavar="TITLE",
                   help="Override the extracted title")
    p.add_argument("--debug", action="store_true",
                   help="Print request/response details to diagnose fetch failures")
    return p.parse_args()


def validate_url(url: str) -> bool:
    try:
        parts = urlparse(url)
        return parts.scheme in ("http", "https") and bool(parts.netloc)
    except Exception:
        return False


def build_slug(title: str, max_len: int = 60) -> str:
    return slugify(title, max_length=max_len, separator="-")


def resolve_write_path(sources_dir: Path, filename: str) -> Path:
    """Handle idempotency: if filename exists, prompt operator."""
    target = sources_dir / filename
    if not target.exists():
        return target

    print(f"\nWARN: File already exists: {target.relative_to(VAULT_ROOT)}")
    print("  (r) replace   (s) skip   (n) write with timestamp suffix")
    choice = input("Choice [r/s/n]: ").strip().lower()

    if choice == "s":
        print("Skipping — no file written.")
        sys.exit(0)
    elif choice == "n":
        import time
        new_name = target.stem + f"_{int(time.time())}.md"
        print(f"Writing as: {new_name}")
        return sources_dir / new_name
    elif choice == "r":
        return target
    else:
        print("Unrecognised choice — skipping.")
        sys.exit(1)


def main() -> None:
    args = parse_args()
    url = args.url.strip()

    # --- Validate inputs ---
    if not validate_url(url):
        print(f"ERROR: Not a valid http/https URL: {url}")
        sys.exit(1)

    opp_dir = VAULT_ROOT / "opportunities" / args.opportunity
    if not opp_dir.exists():
        print(f"ERROR: Opportunity folder not found: {opp_dir}")
        print(f"  Create it first — see _templates/new-opportunity-instructions.md")
        sys.exit(1)

    sources_dir = opp_dir / "01_sources"
    sources_dir.mkdir(exist_ok=True)
    quarantine_dir = sources_dir / "_quarantine"

    # --- Route and fetch ---
    fetcher_class = route(url, args.content_type)
    print(f"\nFetcher : {fetcher_class.__name__}")
    print(f"URL     : {url}")

    try:
        result = fetcher_class(debug=args.debug).fetch(url)
    except RuntimeError as e:
        print(f"\nERROR: {e}")
        sys.exit(1)

    if args.title:
        result["title"] = args.title

    if not result.get("title"):
        result["title"] = urlparse(url).netloc + " — untitled"
        result.setdefault("warnings", []).append(
            "Title could not be extracted — using domain as fallback. Edit manually."
        )

    # --- Build file metadata ---
    captured_date = date.today().isoformat()
    domain = urlparse(url).netloc
    tier = get_source_tier(domain)
    publisher = sanitize_domain(domain)
    slug = build_slug(result["title"])
    filename = f"{captured_date}_{publisher}_{slug}.md"
    citation_slug = f"{captured_date}-{slug[:30]}"

    # --- Determine write path ---
    warnings = result.get("warnings", [])
    content = result.get("content", "").strip()

    if not content:
        # Quarantine files with no extracted content
        quarantine_dir.mkdir(exist_ok=True)
        write_dir = quarantine_dir
        warnings.append(
            "No content extracted — file written to 01_sources/_quarantine/ "
            "for operator review."
        )
    else:
        write_dir = sources_dir

    target = resolve_write_path(write_dir, filename)

    # --- Build and write source file ---
    frontmatter = build_frontmatter(
        opportunity=args.opportunity,
        title=result["title"],
        url=url,
        publisher=publisher,
        publication_date=result.get("publication_date", ""),
        captured=captured_date,
        source_tier=tier,
        content_type=result.get("content_type", "article"),
    )

    body = (
        "\n## Summary\n\n"
        "\n\n"
        "## Extracted content\n\n"
        f"{content}\n\n"
        "## Notes\n\n"
    )

    target.write_text(frontmatter + body, encoding="utf-8")

    # --- Update source ledger ---
    research_file = opp_dir / "00_research-file.md"
    if research_file.exists():
        update_ledger(research_file, citation_slug, url, filename)
    else:
        warnings.append(
            "00_research-file.md not found — source ledger not updated. "
            "Add the citation manually."
        )

    # --- Print summary ---
    rel_path = target.relative_to(VAULT_ROOT)
    print(f"\n{'─' * 60}")
    print(f"  File      : {rel_path}")
    print(f"  Tier      : {tier}  ({fetcher_class.__name__})")
    print(f"  Title     : {result['title']}")
    print(f"  Citation  : [s.{citation_slug}]")
    if result.get("publication_date"):
        print(f"  Pub date  : {result['publication_date']}")
    for w in warnings:
        print(f"  WARN      : {w}")
    print(f"{'─' * 60}\n")


if __name__ == "__main__":
    main()

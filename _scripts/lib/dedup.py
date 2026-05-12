"""URL deduplication across sources/, _inbox.md, and _rejected.md."""

import re
from pathlib import Path


def load_known_urls(opp_dir: Path) -> set[str]:
    """Return all URLs already seen: ingested sources, inbox, and rejected log."""
    urls: set[str] = set()

    # 01_sources/ — read url: frontmatter field from each .md file
    sources_dir = opp_dir / "01_sources"
    if sources_dir.exists():
        for f in sources_dir.glob("*.md"):
            if f.is_file():
                m = re.search(r'^url:\s*(.+)$', f.read_text(encoding="utf-8"), re.MULTILINE)
                if m:
                    urls.add(m.group(1).strip())

    # _rejected.md — URLs appear in the first column of the markdown table
    rejected = opp_dir / "_rejected.md"
    if rejected.exists():
        for m in re.finditer(r'\|\s*(https?://\S+?)\s*\|', rejected.read_text(encoding="utf-8")):
            urls.add(m.group(1))

    # _inbox.md — URLs appear on "  - URL: ..." lines
    inbox = opp_dir / "_inbox.md"
    if inbox.exists():
        for m in re.finditer(r'^\s+- URL:\s*(https?://\S+)', inbox.read_text(encoding="utf-8"), re.MULTILINE):
            urls.add(m.group(1))

    return urls


def load_known_notice_ids(opp_dir: Path) -> set[str]:
    """Return all SAM.gov notice IDs already seen across sources/, inbox, rejected."""
    ids: set[str] = set()

    # 01_sources/ — sam_notice_id: in source frontmatter
    sources_dir = opp_dir / "01_sources"
    if sources_dir.exists():
        for f in sources_dir.glob("*.md"):
            if f.is_file():
                m = re.search(r'^sam_notice_id:\s*(\S+)', f.read_text(encoding="utf-8"), re.MULTILINE)
                if m:
                    ids.add(m.group(1).strip())

    # _inbox.md — "  - Notice ID: ..." lines
    inbox = opp_dir / "_inbox.md"
    if inbox.exists():
        for m in re.finditer(r'^\s+- Notice ID:\s*(\S+)', inbox.read_text(encoding="utf-8"), re.MULTILINE):
            ids.add(m.group(1))

    # _rejected.md — optional 6th column "notice_id=..." appended to reason
    rejected = opp_dir / "_rejected.md"
    if rejected.exists():
        for m in re.finditer(r'notice_id=(\S+?)(?:\s*\||\s*$)', rejected.read_text(encoding="utf-8"), re.MULTILINE):
            ids.add(m.group(1))

    return ids


def load_known_award_ids(opp_dir: Path) -> set[str]:
    """Return all USAspending PIIDs + generated_internal_ids already seen."""
    ids: set[str] = set()

    sources_dir = opp_dir / "01_sources"
    if sources_dir.exists():
        for f in sources_dir.glob("*.md"):
            if f.is_file():
                text = f.read_text(encoding="utf-8")
                for key in ("piid", "award_id", "generated_id"):
                    m = re.search(rf'^{key}:\s*(\S+)', text, re.MULTILINE)
                    if m:
                        ids.add(m.group(1).strip())

    inbox = opp_dir / "_inbox.md"
    if inbox.exists():
        text = inbox.read_text(encoding="utf-8")
        for pat in (r'^\s+- Award ID:\s*(\S+)', r'^\s+- Generated ID:\s*(\S+)'):
            for m in re.finditer(pat, text, re.MULTILINE):
                ids.add(m.group(1))

    return ids

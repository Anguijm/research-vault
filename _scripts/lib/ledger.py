"""Source ledger update for 00_research-file.md."""

import re
from pathlib import Path

LEDGER_HEADER = "## 8. Source ledger"


def update_ledger(research_file: Path, citation_slug: str, url: str, filename: str) -> None:
    """Append a citation entry to the §8 Source ledger section.

    Creates the section if it doesn't exist. Inserts before §9 if present,
    otherwise appends to end of file.
    """
    text = research_file.read_text(encoding="utf-8")
    entry = f"- [s.{citation_slug}] {url}  →  `01_sources/{filename}`"

    if LEDGER_HEADER in text:
        # Find the header position, then locate the next ## section after it
        header_pos = text.index(LEDGER_HEADER)
        after_header = text[header_pos + len(LEDGER_HEADER):]
        next_section = re.search(r'\n(?=## )', after_header)
        if next_section:
            insert_pos = header_pos + len(LEDGER_HEADER) + next_section.start()
            text = text[:insert_pos].rstrip() + "\n" + entry + "\n" + text[insert_pos:]
        else:
            text = text.rstrip() + "\n" + entry + "\n"
    else:
        text = text.rstrip() + f"\n\n---\n\n{LEDGER_HEADER}\n\n{entry}\n"

    research_file.write_text(text, encoding="utf-8")

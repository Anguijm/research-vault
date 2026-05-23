"""Inbox read/write/parse/expire operations for _inbox.md."""

import re
from datetime import datetime, timedelta
from pathlib import Path
from urllib.parse import urlparse

EXPIRY_DAYS = 30

_URL_LINE_RE = re.compile(r'^\s+- URL:\s*(https?://\S+)', re.MULTILINE)
_ADDED_RE = re.compile(r'^\s+- Added:\s*(\S+)', re.MULTILINE)
_FOUND_BY_RE = re.compile(r'^\s+- Found by:\s*(.+)', re.MULTILINE)
_REASON_RE = re.compile(r'^\s+- Reason:\s*(.+)', re.MULTILINE)
_SOURCE_TYPE_RE = re.compile(r'^\s+- Source type:\s*(\S+)', re.MULTILINE)
_NOTICE_ID_RE = re.compile(r'^\s+- Notice ID:\s*(\S+)', re.MULTILINE)
_AWARD_ID_RE = re.compile(r'^\s+- Award ID:\s*(\S+)', re.MULTILINE)
_GENERATED_ID_RE = re.compile(r'^\s+- Generated ID:\s*(\S+)', re.MULTILINE)
_ITEM_RE = re.compile(
    r'^(- \[\s*(?P<state>[x\-]?)\s*\] \*\*(?P<title>[^*]+)\*\*[^\n]*\n(?:[ \t]+- [^\n]*\n)*\n?)',
    re.MULTILINE,
)


def _inbox_path(opp_dir: Path) -> Path:
    return opp_dir / "_inbox.md"


def _rejected_path(opp_dir: Path) -> Path:
    return opp_dir / "_rejected.md"


def load_inbox_urls(opp_dir: Path) -> set[str]:
    inbox = _inbox_path(opp_dir)
    if not inbox.exists():
        return set()
    return {m.group(1) for m in _URL_LINE_RE.finditer(inbox.read_text(encoding="utf-8"))}


def parse_items(opp_dir: Path) -> list[dict]:
    inbox = _inbox_path(opp_dir)
    if not inbox.exists():
        return []
    text = inbox.read_text(encoding="utf-8")
    items = []
    for m in _ITEM_RE.finditer(text):
        block = m.group(0)
        state = m.group("state").strip() or " "  # normalize: empty → pending
        raw_title = m.group("title").strip()
        # Strip markdown link syntax: [display](url) → display
        link_m = re.match(r'\[([^\]]+)\]', raw_title)
        title = link_m.group(1) if link_m else raw_title
        url_m = _URL_LINE_RE.search(block)
        added_m = _ADDED_RE.search(block)
        found_by_m = _FOUND_BY_RE.search(block)
        reason_m = _REASON_RE.search(block)
        source_type_m = _SOURCE_TYPE_RE.search(block)
        notice_id_m = _NOTICE_ID_RE.search(block)
        award_id_m = _AWARD_ID_RE.search(block)
        gen_id_m = _GENERATED_ID_RE.search(block)
        items.append({
            "state": state,  # ' '=pending, 'x'=approved, '-'=rejected
            "title": title,
            "url": url_m.group(1) if url_m else "",
            "added": added_m.group(1) if added_m else "",
            "found_by": found_by_m.group(1).strip() if found_by_m else "",
            "reason": reason_m.group(1).strip() if reason_m else "",
            "source_type": source_type_m.group(1) if source_type_m else "",
            "notice_id": notice_id_m.group(1) if notice_id_m else "",
            "award_id": award_id_m.group(1) if award_id_m else "",
            "generated_id": gen_id_m.group(1) if gen_id_m else "",
            "block": block,
        })
    return items


def load_inbox_notice_ids(opp_dir: Path) -> set[str]:
    """Notice IDs currently in _inbox.md (any state)."""
    inbox = _inbox_path(opp_dir)
    if not inbox.exists():
        return set()
    return {m.group(1) for m in _NOTICE_ID_RE.finditer(inbox.read_text(encoding="utf-8"))}


def load_inbox_award_ids(opp_dir: Path) -> set[str]:
    """USAspending PIIDs + generated IDs currently in _inbox.md (any state)."""
    inbox = _inbox_path(opp_dir)
    if not inbox.exists():
        return set()
    text = inbox.read_text(encoding="utf-8")
    ids: set[str] = set()
    ids.update(m.group(1) for m in _AWARD_ID_RE.finditer(text))
    ids.update(m.group(1) for m in _GENERATED_ID_RE.finditer(text))
    return ids


def append_candidates(opp_dir: Path, candidates: list[dict], dry_run: bool = False) -> int:
    """Append candidates to _inbox.md. Returns count written."""
    if not candidates:
        return 0

    inbox = _inbox_path(opp_dir)
    ts = datetime.now().strftime("%Y-%m-%d %H:%M")
    ts_iso = datetime.now().isoformat(timespec="seconds")
    opp_id = opp_dir.name

    lines = [f"\n## Candidates added {ts}\n\n"]
    for c in candidates:
        domain = urlparse(c["url"]).netloc or c["url"]
        score = c.get("_score")
        score_tag = f" `{score}/10`" if score is not None else ""
        lines.append(f"- [ ] **[{c['title']}]({c['url']})**{score_tag} — {domain}\n")
        lines.append(f"  - URL: {c['url']}\n")
        lines.append(f"  - Found by: {c['model']} (query: \"{c['query']}\")\n")
        if c.get("_rank_note"):
            lines.append(f"  - Note: {c['_rank_note']}\n")
        lines.append(f"  - Reason: {c.get('reason', '')}\n")
        lines.append(f"  - Added: {ts_iso}\n")
        lines.append("\n")

    block = "".join(lines)

    if dry_run:
        print(block)
        return len(candidates)

    if not inbox.exists():
        _init_inbox(inbox, opp_id, ts_iso)

    text = inbox.read_text(encoding="utf-8")
    text = re.sub(r'^last_updated:.*$', f'last_updated: {ts_iso}', text, flags=re.MULTILINE)
    inbox.write_text(text + block, encoding="utf-8")
    return len(candidates)


def append_sam_candidates(opp_dir: Path, candidates: list[dict], dry_run: bool = False) -> int:
    """Append SAM.gov candidates to _inbox.md with extended metadata."""
    if not candidates:
        return 0

    inbox = _inbox_path(opp_dir)
    ts = datetime.now().strftime("%Y-%m-%d %H:%M")
    ts_iso = datetime.now().isoformat(timespec="seconds")
    opp_id = opp_dir.name

    lines = [f"\n## SAM.gov candidates added {ts}\n\n"]
    for c in candidates:
        title = c.get("title", "(untitled notice)")
        flags = c.get("flags") or []
        prefix = "".join(f"[{f}] " for f in flags)
        url = c.get("url", "")
        score = c.get("_score")
        score_tag = f" `{score}/10`" if score is not None else ""

        lines.append(f"- [ ] **[{prefix}{title}]({url})**{score_tag} — sam.gov\n")
        lines.append(f"  - URL: {url}\n")
        lines.append(f"  - Notice ID: {c.get('notice_id', '')}\n")
        lines.append(f"  - Source type: sam_gov\n")
        query = c.get("query") or "(structured)"
        lines.append(f"  - Found by: sam.gov (query: \"{query}\")\n")
        if c.get("_rank_note"):
            lines.append(f"  - Note: {c['_rank_note']}\n")
        lines.append(f"  - Notice type: {c.get('notice_type', '')}\n")
        lines.append(f"  - Posted: {c.get('posted_date', '')}\n")
        lines.append(f"  - Response deadline: {c.get('response_deadline', '')}\n")
        lines.append(f"  - Set-aside: {c.get('set_aside') or 'None'}\n")
        naics = c.get("naics") or []
        lines.append(f"  - NAICS: {', '.join(naics) if naics else 'none'}\n")
        dept = c.get("department", "")
        sub = c.get("subtier", "")
        dept_line = " / ".join(p for p in (dept, sub) if p) or "(unknown)"
        lines.append(f"  - Department: {dept_line}\n")

        attachments = c.get("attachments") or []
        if attachments:
            lines.append(f"  - Attachments: {len(attachments)} (not yet downloaded)\n")
            for a in attachments:
                lines.append(f"    - {a.get('name','attachment')} — {a.get('url','')}\n")
        else:
            lines.append(f"  - Attachments: 0\n")

        lines.append(f"  - Reason: {c.get('reason', '')}\n")
        lines.append(f"  - Added: {ts_iso}\n")
        lines.append("\n")

    block = "".join(lines)

    if dry_run:
        print(block)
        return len(candidates)

    if not inbox.exists():
        _init_inbox(inbox, opp_id, ts_iso)

    text = inbox.read_text(encoding="utf-8")
    text = re.sub(r'^last_updated:.*$', f'last_updated: {ts_iso}', text, flags=re.MULTILINE)
    inbox.write_text(text + block, encoding="utf-8")
    return len(candidates)


def append_usaspending_candidates(opp_dir: Path, candidates: list[dict], dry_run: bool = False) -> int:
    """Append USAspending award candidates to _inbox.md with contract metadata."""
    if not candidates:
        return 0

    inbox = _inbox_path(opp_dir)
    ts = datetime.now().strftime("%Y-%m-%d %H:%M")
    ts_iso = datetime.now().isoformat(timespec="seconds")
    opp_id = opp_dir.name

    lines = [f"\n## USAspending candidates added {ts}\n\n"]
    for c in candidates:
        title = c.get("title", "(no description)")
        url = c.get("url", "")
        amount = c.get("amount_obligated") or 0
        amount_label = f"${amount:,.0f}" if amount else "no amount"

        lines.append(f"- [ ] **[{title[:120]}]({url})** `{amount_label}` — usaspending.gov\n")
        lines.append(f"  - URL: {url}\n")
        lines.append(f"  - Award ID: {c.get('award_id', '')}\n")
        lines.append(f"  - Generated ID: {c.get('generated_id', '')}\n")
        lines.append(f"  - Source type: usa_spending\n")
        query = c.get("query") or "(structured)"
        lines.append(f"  - Found by: usaspending.gov (query: \"{query}\")\n")
        lines.append(f"  - Recipient: {c.get('recipient', '')}\n")
        lines.append(f"  - Amount obligated: {amount_label}\n")
        lines.append(f"  - Period: {c.get('start_date','')} → {c.get('end_date','')}\n")
        lines.append(f"  - Place: {c.get('state', '')}\n")
        lines.append(f"  - Awarder: {c.get('awarder', '')}\n")
        if c.get('funder'):
            lines.append(f"  - Funder: {c.get('funder', '')}\n")
        lines.append(f"  - Reason: {c.get('reason', '')}\n")
        lines.append(f"  - Added: {ts_iso}\n")
        lines.append("\n")

    block = "".join(lines)

    if dry_run:
        print(block)
        return len(candidates)

    if not inbox.exists():
        _init_inbox(inbox, opp_id, ts_iso)

    text = inbox.read_text(encoding="utf-8")
    text = re.sub(r'^last_updated:.*$', f'last_updated: {ts_iso}', text, flags=re.MULTILINE)
    inbox.write_text(text + block, encoding="utf-8")
    return len(candidates)


def _init_inbox(inbox: Path, opp_id: str, ts: str) -> None:
    inbox.write_text(
        f"---\ntype: inbox\nopportunity: {opp_id}\nlast_updated: {ts}\n---\n\n"
        f"# Inbox — pending review\n\n"
        f"**Tap/click a checkbox to approve.** That's all you need to do here.\n"
        f"Then run `python _scripts/approve_inbox.py {opp_id}` to ingest approved items\n"
        f"and interactively review the rest.\n",
        encoding="utf-8",
    )


def expire_old_items(opp_dir: Path) -> int:
    """Move pending items older than EXPIRY_DAYS to _rejected.md. Returns count expired."""
    cutoff = datetime.now() - timedelta(days=EXPIRY_DAYS)
    expired = []
    for item in parse_items(opp_dir):
        if item["state"] != " ":
            continue
        try:
            if datetime.fromisoformat(item["added"]) < cutoff:
                expired.append(item)
        except (ValueError, TypeError):
            pass
    for item in expired:
        _write_rejected(opp_dir, item["url"], item["title"],
                        "inbox_expiry", f"{EXPIRY_DAYS}-day expiry")
        _remove_block(opp_dir, item["block"])
    return len(expired)


def write_rejected(opp_dir: Path, url: str, title: str,
                   rejected_by: str, reason: str) -> None:
    _write_rejected(opp_dir, url, title, rejected_by, reason)


def _write_rejected(opp_dir: Path, url: str, title: str,
                    rejected_by: str, reason: str) -> None:
    rejected = _rejected_path(opp_dir)
    date = datetime.now().strftime("%Y-%m-%d")
    if not rejected.exists():
        opp_id = opp_dir.name
        rejected.write_text(
            f"---\ntype: rejected_log\nopportunity: {opp_id}\n---\n\n"
            f"# Rejected sources — sticky, never re-queue\n\n"
            f"| URL | Title | Rejected by | Date | Reason |\n"
            f"|---|---|---|---|---|\n",
            encoding="utf-8",
        )
    safe_url = url.replace("|", "\\|")
    safe_title = title.replace("|", "\\|")
    with open(rejected, "a", encoding="utf-8") as f:
        f.write(f"| {safe_url} | {safe_title} | {rejected_by} | {date} | {reason} |\n")


def _remove_block(opp_dir: Path, block: str) -> None:
    inbox = _inbox_path(opp_dir)
    if not inbox.exists():
        return
    text = inbox.read_text(encoding="utf-8")
    inbox.write_text(text.replace(block, "", 1), encoding="utf-8")


def remove_block(opp_dir: Path, block: str) -> None:
    _remove_block(opp_dir, block)

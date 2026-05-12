#!/usr/bin/env python3
"""
verify_facts.py — LLM-verified FACT claims against ingested sources.

For each FACT claim in <opportunity>/00_research-file.md:
  1. Extract claim text and all [s.xxx] citations.
  2. Resolve each citation to either an ingested file in 01_sources/ or a
     §8.2 "cited but not ingested" entry.
  3. For each ingested source on the claim, ask Claude to verify whether the
     source supports the claim, returning a structured verdict + quote.
  4. Combine per-source verdicts into a single FACT-level status.
  5. Write a markdown verification report and (optionally) update the
     verification markers in 00_research-file.md.

Usage:
    python verify_facts.py --opportunity PMTEC-USINDOPACOM
    python verify_facts.py --opportunity PMTEC-USINDOPACOM --update-markers
    python verify_facts.py --opportunity PMTEC-USINDOPACOM --model claude-sonnet-4-6
"""

import argparse
import json
import os
import re
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

SCRIPT_DIR = Path(__file__).parent
VAULT_ROOT = SCRIPT_DIR.parent
OPP_ROOT = VAULT_ROOT / "opportunities"

sys.path.insert(0, str(SCRIPT_DIR))
load_dotenv(SCRIPT_DIR / ".env")

DEFAULT_MODEL = "claude-sonnet-4-6"

# Per-source content truncation (LLM input budget guard).
# Sonnet handles ~200K tokens of context; ~120K chars leaves headroom for the
# prompt + a long source. Bumped from 24K (which truncated the FY26 PDI book
# before its PMTEC tables on p.19 were visible).
_MAX_SOURCE_CHARS = 120000


# ── Research-file parsing ───────────────────────────────────────────────

_FACT_RE = re.compile(
    r'^\*\*FACT:\*\*\s*(?:`\[[^`]+\]`\s*)?'             # FACT marker + optional status badge
    r'(?P<body>.+?)'                                    # body (greedy until terminator)
    r'(?=\n{2,}\*\*(?:FACT|Assessment|Speculation):\*\*'  # next labeled paragraph
    r'|\n{2,}#{1,3}\s'                                  # next heading
    r'|\n{2,}---\s*\n'                                  # horizontal rule on its own line
    r'|\Z)',
    re.MULTILINE | re.DOTALL,
)
_CITATION_RE = re.compile(r'\[s\.([A-Za-z0-9._\-]+)\]')


def _strip_citations(claim: str) -> str:
    """Remove [s.xxx] citation tags from claim text before sending to the model.
    Citations are bookkeeping, not claim content."""
    return re.sub(r'\s*\[s\.[A-Za-z0-9._\-]+\]', '', claim).strip()
_SECTION_RE = re.compile(r'^## (?P<num>\d+)\.', re.MULTILINE)
_LEDGER_LINE_RE = re.compile(
    r'^- \[s\.(?P<tag>[A-Za-z0-9._\-]+)\]\s*(?P<rest>.+)$',
    re.MULTILINE,
)


def parse_research_file(path: Path) -> tuple[list[dict], dict[str, dict]]:
    """Return (facts, ledger).

    facts: list of {claim, citations, section, raw_block}
    ledger: tag → {url, path, ingested: bool, note}
    """
    text = path.read_text(encoding="utf-8")

    # Build section index so we can label each FACT by section number
    section_positions = [(m.start(), int(m.group("num"))) for m in _SECTION_RE.finditer(text)]

    def section_for(offset: int) -> int:
        last = 0
        for pos, num in section_positions:
            if pos > offset:
                break
            last = num
        return last

    facts: list[dict] = []
    for m in _FACT_RE.finditer(text):
        body = m.group("body").strip()
        citations = list(dict.fromkeys(_CITATION_RE.findall(body)))  # preserve order, dedupe
        if not body:
            continue
        facts.append({
            "claim": body,
            "citations": citations,
            "section": section_for(m.start()),
            "offset": m.start(),
            "raw": m.group(0),
        })

    ledger = _parse_ledger(text)
    return facts, ledger


def _parse_ledger(text: str) -> dict[str, dict]:
    """Return tag → metadata for every ledger line in §8.

    Simpler rule: any `- [s.TAG] ...` line within §8 is a ledger entry.
    Ingested is determined by presence of an `01_sources/...md` path — independent
    of which subsection (§8.1, §8.2, or auto-appended) the line lives in.
    """
    ledger: dict[str, dict] = {}

    # Capture all of §8 (from "## 8. Source ledger" to the next "## " heading)
    sec8 = re.search(r'^## 8\. Source ledger(.+?)(?=^## \d|\Z)', text, re.DOTALL | re.MULTILINE)
    body = sec8.group(1) if sec8 else text

    for m in _LEDGER_LINE_RE.finditer(body):
        tag = m.group("tag")
        rest = m.group("rest")
        path_m = re.search(r'`?(01_sources/[^`\s]+\.md)`?', rest)
        url_m = re.search(r'(https?://\S+)', rest)
        path = path_m.group(1) if path_m else ""
        ingested = bool(path)

        # If the same tag appears more than once, prefer the entry with the path
        existing = ledger.get(tag)
        if existing and existing["ingested"] and not ingested:
            continue
        ledger[tag] = {
            "url": url_m.group(1) if url_m else "",
            "path": path,
            "ingested": ingested,
            "note": rest.strip(),
        }
    return ledger


def _load_source_content(opp_dir: Path, ledger_entry: dict) -> str:
    rel = ledger_entry.get("path")
    if not rel:
        return ""
    src = opp_dir / rel.replace("01_sources/", "01_sources/", 1)
    # The relative path stored in the ledger is from the opportunity folder
    candidate_paths = [opp_dir / rel, VAULT_ROOT / rel]
    for p in candidate_paths:
        if p.exists():
            return p.read_text(encoding="utf-8")[:_MAX_SOURCE_CHARS]
    return ""


# ── LLM verification ────────────────────────────────────────────────────

_VERIFY_PROMPT = """\
You are a fact-verification assistant for a defense business-development research vault.

Determine whether the CLAIM below is supported by the SOURCE content provided.

CLAIM:
{claim}

SOURCE (URL: {source_url}):
{source_content}

Rules:
- Judge ONLY whether the source explicitly contains evidence for the claim.
- A close paraphrase is acceptable evidence (e.g. "the largest coalition range system in the world" supports a claim about "world's largest coalition range system").
- Numbers must match within reasonable rounding; dates must match within the same calendar quarter.
- Do NOT speculate. Do NOT use general knowledge. Use only what the source text contains.
- If the source supports part of the claim but not all of it, report PARTIAL and specify the missing elements.
- If the source does not mention the claim's subject at all, report DOES_NOT_SUPPORT.

Respond in JSON only, no other text:
{{"status": "SUPPORTS" | "PARTIAL" | "DOES_NOT_SUPPORT",
  "supporting_quote": "<exact verbatim quote from source, or empty>",
  "missing_elements": "<elements of claim NOT supported, or empty>",
  "notes": "<one sentence reasoning>"}}"""


def verify_against_source(claim: str, source_url: str, source_content: str, model: str) -> dict:
    """Call Claude to verify claim against source content. Returns the parsed JSON."""
    import anthropic
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    prompt = _VERIFY_PROMPT.format(
        claim=_strip_citations(claim),
        source_url=source_url or "(no url)",
        source_content=source_content or "(source content empty)",
    )
    msg = client.messages.create(
        model=model,
        max_tokens=1500,
        messages=[{"role": "user", "content": prompt}],
    )
    text = next((b.text for b in msg.content if hasattr(b, "text")), "")
    return _parse_verdict(text)


def _parse_verdict(text: str) -> dict:
    """Extract the JSON verdict from the model response."""
    if not text:
        return _fallback_verdict("empty model response")
    m = re.search(r'```(?:json)?\s*(\{[\s\S]*?\})\s*```', text)
    if m:
        text = m.group(1)
    else:
        start = text.find("{")
        end = text.rfind("}")
        if start != -1 and end != -1:
            text = text[start:end + 1]
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return _fallback_verdict("malformed JSON from model")
    status = data.get("status", "DOES_NOT_SUPPORT").upper()
    if status not in ("SUPPORTS", "PARTIAL", "DOES_NOT_SUPPORT"):
        status = "DOES_NOT_SUPPORT"
    return {
        "status": status,
        "supporting_quote": str(data.get("supporting_quote") or "").strip(),
        "missing_elements": str(data.get("missing_elements") or "").strip(),
        "notes": str(data.get("notes") or "").strip(),
    }


def _fallback_verdict(reason: str) -> dict:
    return {"status": "DOES_NOT_SUPPORT", "supporting_quote": "",
            "missing_elements": "", "notes": f"verify error: {reason}"}


# ── Combining per-source verdicts → FACT-level status ──────────────────

def combine_status(per_source: list[dict], has_unresolved: bool) -> str:
    """Aggregate per-source verdicts into a single FACT status."""
    if not per_source:
        return "UNVERIFIABLE"   # No ingested source available
    statuses = [r["status"] for r in per_source]
    if "SUPPORTS" in statuses:
        # Any source fully supports → SUPPORTS (corroborated by ingested evidence)
        return "SUPPORTS"
    if "PARTIAL" in statuses:
        return "PARTIAL"
    # All verdicts are DOES_NOT_SUPPORT
    if has_unresolved:
        return "UNVERIFIABLE"   # Cited source not ingested; we couldn't prove either way
    return "DOES_NOT_SUPPORT"


# ── Report rendering ────────────────────────────────────────────────────

_STATUS_ICON = {
    "SUPPORTS": "✓",
    "PARTIAL": "⚑",
    "DOES_NOT_SUPPORT": "✗",
    "UNVERIFIABLE": "?",
}


def render_report(opp_id: str, model: str, results: list[dict]) -> str:
    counts: dict[str, int] = {}
    for r in results:
        counts[r["status"]] = counts.get(r["status"], 0) + 1

    lines = [
        f"# FACT Verification Report — {opp_id}",
        f"",
        f"*Generated {datetime.now().isoformat(timespec='seconds')} by `verify_facts.py` (model: `{model}`)*",
        f"",
        f"## Summary",
        f"",
        f"- **{len(results)}** FACT claims scanned",
        f"- **{counts.get('SUPPORTS', 0)}** SUPPORTS — claim is corroborated by an ingested source",
        f"- **{counts.get('PARTIAL', 0)}** PARTIAL — some elements supported by an ingested source",
        f"- **{counts.get('DOES_NOT_SUPPORT', 0)}** DOES_NOT_SUPPORT — ingested source contradicts or omits the claim",
        f"- **{counts.get('UNVERIFIABLE', 0)}** UNVERIFIABLE — cited source(s) not yet in 01_sources/",
        f"",
        f"## Verifications",
        f"",
    ]

    for i, r in enumerate(results, 1):
        icon = _STATUS_ICON.get(r["status"], "?")
        section = f"§{r['section']}" if r["section"] else ""
        lines.append(f"### {icon} FACT #{i} {section}  —  **{r['status']}**")
        lines.append(f"")
        lines.append(f"**Claim:**")
        lines.append(f"> {r['claim_short']}")
        lines.append(f"")
        if r["citations"]:
            lines.append(f"**Citations:** {' '.join(f'[s.{c}]' for c in r['citations'])}")
            lines.append(f"")
        lines.append(f"**Sources checked:**")
        for s in r["sources_checked"]:
            line = f"- `[s.{s['tag']}]` "
            if s.get("ingested"):
                line += f"→ `{s['path']}` — verdict: **{s['verdict']['status']}**"
                if s.get("url"):
                    line += f" ([source]({s['url']}))"
            else:
                line += f"→ ⚠ not in `01_sources/` (cited only in §8.2)"
            lines.append(line)
        for s in r["sources_checked"]:
            v = s.get("verdict")
            if not v or not s.get("ingested"):
                continue
            if v.get("supporting_quote"):
                quote = v['supporting_quote'].replace("\n", " ").strip()
                lines.append(f"  > _\"{quote[:400]}{'…' if len(quote) > 400 else ''}\"_")
            if v.get("missing_elements"):
                lines.append(f"  - Missing in this source: {v['missing_elements']}")
            if v.get("notes"):
                lines.append(f"  - Model note: {v['notes']}")
        lines.append(f"")

    return "\n".join(lines) + "\n"


# ── Marker updater (optional) ───────────────────────────────────────────

_STATUS_TO_MARKER = {
    "SUPPORTS": "`[✓ INGESTED]`",
    "PARTIAL": "`[⚑ PARTIAL]`",
    "DOES_NOT_SUPPORT": "`[✗ UNSUPPORTED]`",
    "UNVERIFIABLE": "`[⚠ PENDING-INGEST]`",
}


def update_markers_in_research_file(research_file: Path, results: list[dict]) -> int:
    """Replace each FACT's status marker with the verifier's verdict. Returns count updated."""
    text = research_file.read_text(encoding="utf-8")
    updated = 0
    for r in results:
        old_block = r["raw"]
        new_marker = _STATUS_TO_MARKER[r["status"]]
        # Remove any existing marker, then add the new one right after **FACT:**
        cleaned = re.sub(r'`\[[^`]+\]`\s*', "", old_block, count=1)
        new_block = re.sub(r'\*\*FACT:\*\*\s*', f"**FACT:** {new_marker} ", cleaned, count=1)
        if new_block != old_block and old_block in text:
            text = text.replace(old_block, new_block, 1)
            updated += 1
    research_file.write_text(text, encoding="utf-8")
    return updated


# ── Main ────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--opportunity", required=True, metavar="ID",
                        help="Opportunity folder ID (e.g., PMTEC-USINDOPACOM)")
    parser.add_argument("--model", default=DEFAULT_MODEL,
                        help=f"Anthropic model ID (default: {DEFAULT_MODEL})")
    parser.add_argument("--update-markers", action="store_true",
                        help="Update FACT status markers in 00_research-file.md per the verdict")
    parser.add_argument("--max-workers", type=int, default=4,
                        help="Parallel verification calls (default: 4)")
    args = parser.parse_args()

    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("ERROR: ANTHROPIC_API_KEY not set in .env")
        sys.exit(1)

    opp_dir = OPP_ROOT / args.opportunity
    if not opp_dir.is_dir():
        print(f"ERROR: Opportunity folder not found: {opp_dir}")
        sys.exit(1)

    research_file = opp_dir / "00_research-file.md"
    if not research_file.exists():
        print(f"ERROR: 00_research-file.md not found in {opp_dir}")
        sys.exit(1)

    print(f"Parsing {research_file.relative_to(VAULT_ROOT)}...")
    facts, ledger = parse_research_file(research_file)
    print(f"  Found {len(facts)} FACT claims, {len(ledger)} ledger entries")

    # Build verification work list: (fact_idx, tag, source_url, source_content)
    work_items: list[tuple[int, str, str, str]] = []
    for idx, fact in enumerate(facts):
        for tag in fact["citations"]:
            entry = ledger.get(tag, {})
            if entry.get("ingested") and entry.get("path"):
                content = _load_source_content(opp_dir, entry)
                if content:
                    work_items.append((idx, tag, entry.get("url", ""), content))

    print(f"  Queued {len(work_items)} (FACT × ingested-source) verifications")

    # Run verifications in parallel
    verdicts: dict[tuple[int, str], dict] = {}
    print(f"Running verifications with {args.model}...")
    with ThreadPoolExecutor(max_workers=args.max_workers) as ex:
        futures = {
            ex.submit(verify_against_source, facts[idx]["claim"], url, content, args.model):
            (idx, tag)
            for idx, tag, url, content in work_items
        }
        for fut in as_completed(futures):
            idx, tag = futures[fut]
            try:
                verdicts[(idx, tag)] = fut.result()
                print(f"  ✓ FACT #{idx + 1} × [s.{tag}] → {verdicts[(idx, tag)]['status']}")
            except Exception as e:
                verdicts[(idx, tag)] = _fallback_verdict(str(e))
                print(f"  ✗ FACT #{idx + 1} × [s.{tag}] → ERROR: {e}")

    # Build per-FACT result rows
    results: list[dict] = []
    for idx, fact in enumerate(facts):
        sources_checked = []
        per_source_verdicts = []
        has_unresolved = False
        for tag in fact["citations"]:
            entry = ledger.get(tag, {})
            if entry.get("ingested") and entry.get("path"):
                v = verdicts.get((idx, tag), _fallback_verdict("not run"))
                sources_checked.append({
                    "tag": tag, "ingested": True,
                    "path": entry["path"], "url": entry.get("url", ""),
                    "verdict": v,
                })
                per_source_verdicts.append(v)
            else:
                sources_checked.append({
                    "tag": tag, "ingested": False,
                    "path": "", "url": entry.get("url", ""),
                    "verdict": None,
                })
                has_unresolved = True
        status = combine_status(per_source_verdicts, has_unresolved)
        claim_short = re.sub(r'\s+', ' ', fact["claim"]).strip()
        if len(claim_short) > 400:
            claim_short = claim_short[:400] + "…"
        results.append({
            "status": status,
            "claim_short": claim_short,
            "raw": fact["raw"],
            "citations": fact["citations"],
            "section": fact["section"],
            "sources_checked": sources_checked,
        })

    # Render and write report
    report = render_report(args.opportunity, args.model, results)
    out = opp_dir / f"_verification-{datetime.now().strftime('%Y-%m-%d')}.md"
    out.write_text(report, encoding="utf-8")
    print(f"\nReport written: {out.relative_to(VAULT_ROOT)}")

    if args.update_markers:
        n = update_markers_in_research_file(research_file, results)
        print(f"Updated {n} status markers in {research_file.relative_to(VAULT_ROOT)}")

    counts = {s: sum(1 for r in results if r["status"] == s)
              for s in ("SUPPORTS", "PARTIAL", "DOES_NOT_SUPPORT", "UNVERIFIABLE")}
    print(f"\nSummary: SUPPORTS={counts['SUPPORTS']}  PARTIAL={counts['PARTIAL']}  "
          f"DOES_NOT_SUPPORT={counts['DOES_NOT_SUPPORT']}  UNVERIFIABLE={counts['UNVERIFIABLE']}")


if __name__ == "__main__":
    main()

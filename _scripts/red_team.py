#!/usr/bin/env python3
"""
red_team.py — Cross-AI red-team review of a capture or exec brief.

Pulls the operator's `_meta/prompts/cross-ai-red-team.md` prompt body, extracts
the brief text from the .docx, attaches FACT-level supporting quotes from the
latest verification report, sends to Gemini, and writes a red-team report into
the opportunity folder. Per SOP §2.1 rule 5 (adversarial review before
shipping) and the prompt note: red-team with the OTHER model from drafting.

Usage:
    python red_team.py --opportunity PMTEC-USINDOPACOM
    python red_team.py --opportunity PMTEC-USINDOPACOM --brief executive
    python red_team.py --opportunity PMTEC-USINDOPACOM --model gemini-2.5-pro
    python red_team.py --opportunity PMTEC-USINDOPACOM --no-quotes
"""

import argparse
import os
import re
import sys
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

SCRIPT_DIR = Path(__file__).parent
VAULT_ROOT = SCRIPT_DIR.parent
OPP_ROOT = VAULT_ROOT / "opportunities"
PROMPT_FILE = VAULT_ROOT / "_meta" / "prompts" / "cross-ai-red-team.md"

sys.path.insert(0, str(SCRIPT_DIR))
load_dotenv(SCRIPT_DIR / ".env")

DEFAULT_MODEL = "gemini-3.1-pro-preview"
MAX_OUTPUT_TOKENS = 8000   # red-team responses are long — 3 passes × specific critiques


# ── Brief extraction ────────────────────────────────────────────────────

def _read_brief(path: Path) -> str:
    """Extract all paragraph text from a .docx, stopping at the auto-generated
    Sources sentinel so the red-team isn't graded on our own Sources appendix."""
    from docx import Document
    doc = Document(path)
    SENTINEL = "── Sources (auto-generated"
    lines = []
    for p in doc.paragraphs:
        if SENTINEL in p.text:
            break
        if p.text.strip():
            lines.append(p.text)
    # Tables too
    for t in doc.tables:
        for row in t.rows:
            cells = [c.text.strip() for c in row.cells]
            if any(cells):
                lines.append(" | ".join(cells))
    return "\n".join(lines)


def _find_brief(opp_dir: Path, kind: str) -> Path:
    artifacts = opp_dir / "04_artifacts"
    pattern = f"{kind}-brief-*.docx"
    matches = sorted(artifacts.glob(pattern))
    if not matches:
        raise FileNotFoundError(f"No {kind} brief found in {artifacts}")
    # Latest version if multiple
    return matches[-1]


# ── Source-quote extraction (from latest verification report) ───────────

def _collect_supporting_quotes(opp_dir: Path) -> str:
    """Pull FACT-level supporting quotes from the latest _verification-*.md.

    Returns a markdown block with one FACT per entry: claim → supporting quote.
    Used to ground the red-team in what the brief's evidence actually says,
    so Gemini can flag cases where the brief overclaims relative to sources.
    """
    reports = sorted(opp_dir.glob("_verification-*.md"))
    if not reports:
        return "(No verification report found — red-team has no per-FACT quote ground truth.)"
    latest = reports[-1]
    text = latest.read_text(encoding="utf-8")

    out = [f"## FACT-level supporting quotes (from {latest.name})", ""]
    # Each FACT block: claim line + supporting_quote lines (markdown blockquotes)
    blocks = re.split(r'^### ', text, flags=re.MULTILINE)
    for b in blocks[1:]:
        header_m = re.match(r'(?P<icon>\S+)\s+FACT #(?P<n>\d+)\s+§\d+\s+—\s+\*\*(?P<status>\w+)\*\*', b)
        if not header_m:
            continue
        n = header_m.group("n")
        status = header_m.group("status")
        claim_m = re.search(r'\*\*Claim:\*\*\s*\n>\s*(.+?)(?:\n\n|\n\*\*)', b, re.DOTALL)
        claim = claim_m.group(1).strip().replace("\n> ", " ") if claim_m else "(no claim extracted)"
        # All supporting quotes in this FACT block
        quote_matches = re.findall(r'^\s*>\s*_"(.+?)"_\s*$', b, re.MULTILINE)
        out.append(f"### FACT #{n} ({status})")
        out.append(f"**Claim:** {claim[:400]}{'…' if len(claim) > 400 else ''}")
        if quote_matches:
            for q in quote_matches[:2]:   # cap at 2 quotes per FACT to control prompt size
                out.append(f"> {q[:600]}{'…' if len(q) > 600 else ''}")
        else:
            out.append("> _(no supporting quote in report — verifier could not anchor)_")
        out.append("")
    return "\n".join(out)


# ── Prompt assembly ─────────────────────────────────────────────────────

def _load_red_team_prompt() -> str:
    """Extract the prompt body from inside the ``` fence in the SOP prompt file."""
    text = PROMPT_FILE.read_text(encoding="utf-8")
    m = re.search(r'```\n(.+?)\n```', text, re.DOTALL)
    if not m:
        raise RuntimeError(f"Could not find fenced prompt body in {PROMPT_FILE}")
    return m.group(1).strip()


def _assemble_prompt(brief_text: str, source_quotes: str, include_quotes: bool) -> str:
    prompt_body = _load_red_team_prompt()
    parts = [
        prompt_body,
        "",
        "---",
        "",
        "## CAPTURE BRIEF (full text)",
        "",
        brief_text,
    ]
    if include_quotes:
        parts.extend(["", "---", "", source_quotes])
    parts.extend([
        "",
        "---",
        "",
        "Begin your three-pass red-team now. For each pass, prefix critiques "
        "with the brief section number when possible (e.g., '§5.1', '§7'). "
        "Be specific and adversarial. If a claim in the brief looks supportable "
        "from the FACT-level supporting quotes above, do not flag it — focus your "
        "ammunition on places where the brief reaches beyond what the source actually says.",
    ])
    return "\n".join(parts)


# ── Gemini call ─────────────────────────────────────────────────────────

def _call_gemini(prompt: str, model: str) -> str:
    from google import genai
    from google.genai import types
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config=types.GenerateContentConfig(
            max_output_tokens=MAX_OUTPUT_TOKENS,
            temperature=0.4,   # some creativity for adversarial framing
        ),
    )
    return response.text or "(empty response from Gemini)"


# ── Report writing ──────────────────────────────────────────────────────

def _write_report(opp_dir: Path, model: str, brief_path: Path, response: str) -> Path:
    date = datetime.now().strftime("%Y-%m-%d")
    safe_model = model.replace("/", "_").replace(":", "_")
    out = opp_dir / f"_red-team-{date}-{safe_model}.md"
    frontmatter = (
        f"---\n"
        f"type: red_team_report\n"
        f"opportunity: {opp_dir.name}\n"
        f"reviewed: {brief_path.name}\n"
        f"model: {model}\n"
        f"date: {date}\n"
        f"prompt_source: _meta/prompts/cross-ai-red-team.md\n"
        f"---\n\n"
    )
    body = (
        f"# Cross-AI Red Team — {opp_dir.name}\n\n"
        f"*Reviewer: `{model}`  ·  Subject: `{brief_path.name}`  ·  Generated: {datetime.now().isoformat(timespec='seconds')}*\n\n"
        f"Run via `_scripts/red_team.py` using the prompt at "
        f"`_meta/prompts/cross-ai-red-team.md`. Three passes per SOP §2.1 rule 5: "
        f"Customer / Competitor / Skeptical Exec.\n\n"
        f"---\n\n"
        f"{response.strip()}\n"
    )
    out.write_text(frontmatter + body, encoding="utf-8")
    return out


def _append_decision_log(opp_dir: Path, model: str, brief_path: Path,
                        report_path: Path, finding_count: int | None) -> None:
    log = opp_dir / "05_decision-log.md"
    if not log.exists():
        return
    date = datetime.now().strftime("%Y-%m-%d")
    finding_str = f"{finding_count} substantive findings" if finding_count is not None else "findings TBD by operator"
    entry = (
        f"\n### {date} — Cross-AI red-team via {model}\n\n"
        f"**By:** operator + `_scripts/red_team.py`\n"
        f"**Rationale:** SOP §2.1 rule 5 adversarial review before shipping. "
        f"Drafting used Claude; red-team uses Gemini per prompt note.\n"
        f"**What changed:** Report written to `{report_path.name}`. "
        f"Reviewed `{brief_path.name}` ({finding_str}). "
        f"Operator decides whether to address findings before next gate.\n\n"
        f"---\n"
    )
    with open(log, "a", encoding="utf-8") as f:
        f.write(entry)


def _count_findings(response: str) -> int | None:
    """Heuristic — count numbered/bulleted items in the response. Returns None if unsure."""
    bullets = len(re.findall(r'^\s*[\d]+\.\s|\n\s*[-*]\s', response))
    return bullets if bullets > 0 else None


# ── Main ────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--opportunity", required=True, metavar="ID")
    parser.add_argument("--brief", default="capture",
        choices=["capture", "executive"],
        help="Which brief to red-team (default: capture)")
    parser.add_argument("--model", default=DEFAULT_MODEL,
        help=f"Gemini model ID (default: {DEFAULT_MODEL})")
    parser.add_argument("--no-quotes", action="store_true",
        help="Skip the FACT-level supporting quotes context (smaller prompt)")
    args = parser.parse_args()

    if not os.environ.get("GEMINI_API_KEY"):
        print("ERROR: GEMINI_API_KEY not set in .env")
        sys.exit(1)

    opp_dir = OPP_ROOT / args.opportunity
    if not opp_dir.is_dir():
        print(f"ERROR: Opportunity folder not found: {opp_dir}")
        sys.exit(1)

    brief_path = _find_brief(opp_dir, args.brief)
    print(f"Brief: {brief_path.relative_to(VAULT_ROOT)}")

    print(f"Extracting brief text...")
    brief_text = _read_brief(brief_path)
    print(f"  {len(brief_text):,} chars")

    include_quotes = not args.no_quotes
    quotes = _collect_supporting_quotes(opp_dir) if include_quotes else ""
    if include_quotes:
        print(f"Collected FACT-level supporting quotes: {len(quotes):,} chars")

    prompt = _assemble_prompt(brief_text, quotes, include_quotes)
    print(f"Total prompt: {len(prompt):,} chars  ·  model: {args.model}")
    print(f"Calling Gemini (this can take 30-60s for a 3-pass red-team)...")

    response = _call_gemini(prompt, args.model)
    print(f"  ↩ {len(response):,} chars of red-team output\n")

    report = _write_report(opp_dir, args.model, brief_path, response)
    rel = report.relative_to(VAULT_ROOT)

    findings = _count_findings(response)
    _append_decision_log(opp_dir, args.model, brief_path, report, findings)

    print(f"✓ Report written: {rel}")
    if findings is not None:
        print(f"  Approximate finding count: {findings}")
    print(f"  Decision log updated: {(opp_dir / '05_decision-log.md').relative_to(VAULT_ROOT)}")


if __name__ == "__main__":
    main()

"""Claude and Gemini parallel search dispatcher."""

import json
import os
import re
from concurrent.futures import ThreadPoolExecutor, as_completed

PROMPT_TEMPLATE = """\
You are a defense market intelligence research assistant. Find publicly available
news articles, press releases, and primary documents from the past {date_window_days}
days matching this search:

QUERY: {query}

Return up to {max_candidates_per_run} of the most relevant results.

For each result, provide:
  - URL (direct link, not a search result page)
  - Title (as published)
  - Publisher/domain
  - Publication date (YYYY-MM-DD if known, else "unknown")
  - Brief reason for relevance to the query (1 sentence)

Rules:
  - Only include sources from the past {date_window_days} days.
  - Prefer primary sources: .mil sites, DVIDS, SAM.gov, USAspending.gov, GAO,
    congressional records, SEC filings, company press releases.
  - Trade press (Breaking Defense, Defense News, etc.) is acceptable as context.
  - Do NOT include search result pages, social media posts, or aggregator landing pages.
  - Do NOT invent URLs. If you are not confident a URL exists, omit it.
  - If no results match, return an empty list.

Respond in JSON format only:
{{
  "query": "...",
  "results": [
    {{
      "url": "...",
      "title": "...",
      "publisher": "...",
      "publication_date": "...",
      "reason": "..."
    }}
  ]
}}"""


def _call_claude(prompt: str, query: str) -> list[dict]:
    import anthropic
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    msg = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2048,
        tools=[{"type": "web_search_20250305", "name": "web_search"}],
        messages=[{"role": "user", "content": prompt}],
    )
    text = next((b.text for b in msg.content if hasattr(b, "text")), None)
    return _parse_response(text, query, "claude")


def _call_gemini(prompt: str, query: str) -> list[dict]:
    from google import genai
    from google.genai import types
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            tools=[types.Tool(google_search=types.GoogleSearch())],
        ),
    )
    return _parse_response(response.text, query, "gemini")


def _parse_response(text: str | None, query: str, model: str) -> list[dict]:
    if not text:
        return []
    # Extract JSON from a fenced code block if present
    m = re.search(r'```(?:json)?\s*([\[{][\s\S]*?[\]}])\s*```', text)
    if m:
        text = m.group(1)
    else:
        # Fall back: find first { or [ and take from there
        start = re.search(r'[{\[]', text)
        if start:
            text = text[start.start():]
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return []
    # Accept both {"results": [...]} and bare [...]
    if isinstance(data, list):
        raw = data
    elif isinstance(data, dict):
        raw = data.get("results", [])
    else:
        return []
    results = []
    for r in raw:
        url = r.get("url", "").strip()
        if not url or not url.startswith("http"):
            continue
        results.append({
            "url": url,
            "title": r.get("title", "").strip() or url,
            "publisher": r.get("publisher", ""),
            "publication_date": r.get("publication_date", "unknown"),
            "reason": r.get("reason", ""),
            "query": query,
            "model": model,
        })
    return results


def search(
    query: str,
    date_window_days: int,
    max_candidates: int,
    use_claude: bool,
    use_gemini: bool,
) -> list[dict]:
    """Run query against available models in parallel. Returns combined candidate list."""
    prompt = PROMPT_TEMPLATE.format(
        query=query,
        date_window_days=date_window_days,
        max_candidates_per_run=max_candidates,
    )

    tasks = []
    if use_claude:
        tasks.append(("claude", _call_claude))
    if use_gemini:
        tasks.append(("gemini", _call_gemini))

    if not tasks:
        return []

    results = []
    with ThreadPoolExecutor(max_workers=len(tasks)) as executor:
        futures = {executor.submit(fn, prompt, query): name for name, fn in tasks}
        for future in as_completed(futures):
            name = futures[future]
            try:
                results.extend(future.result())
            except Exception as e:
                print(f"  WARN: {name} search error for '{query}': {e}")
    return results

"""
playwright_browser.py — Headless-browser fallback fetcher.

When the curl_cffi-based WebFetcher gets a 403 from Akamai- or
Cloudflare-class bot detection that browser-TLS impersonation alone cannot
defeat, this fetcher launches a real headless Chromium via Playwright and
extracts content the same way.

Tradeoffs: slower (1-3s per fetch), heavier (Chromium binary is ~300MB), but
defeats more bot-detection layers than curl_cffi alone. Used as a fallback,
not as the default fetcher.

Returns the same dict shape as the WebFetcher in web.py so the calling code
does not need to know which fetcher produced the result.
"""

import re
from datetime import datetime
from urllib.parse import urlparse

import trafilatura

from lib.fetchers.base import BaseFetcher


class PlaywrightFetcher(BaseFetcher):
    """Headless-Chromium fallback fetcher with Playwright.

    Used by web.py's fallback path when curl_cffi exhausts its retries on
    403 or 429. Not invoked directly from ingest.py routing — it is a
    fallback inside the WebFetcher path.
    """

    TIMEOUT_MS = 30_000
    WAIT_AFTER_LOAD_MS = 1_500

    def fetch(self, url: str) -> dict:
        warnings = []
        try:
            html, final_url = self._render(url)
        except Exception as e:
            raise RuntimeError(f"Playwright fetch failed for {url}: {e}")

        content = trafilatura.extract(
            html,
            url=final_url,
            include_links=False,
            include_images=False,
            include_tables=True,
            output_format="markdown",
        )

        if not content:
            warnings.append(
                "Playwright fetch succeeded but trafilatura extracted no content. "
                "Page may be SPA-rendered with non-standard markup."
            )
            content = ""

        title = self._extract_title(html, final_url)
        pub_date = self._extract_date(html)
        if not pub_date:
            warnings.append("Publication date not found in page metadata — fill in manually.")

        return {
            "title": title,
            "content": content,
            "content_type": self._detect_content_type(final_url),
            "publication_date": pub_date,
            "warnings": warnings,
        }

    def _render(self, url: str) -> tuple[str, str]:
        from playwright.sync_api import sync_playwright

        with sync_playwright() as p:
            browser = p.chromium.launch(
                headless=True,
                args=[
                    "--disable-blink-features=AutomationControlled",
                    "--no-sandbox",
                ],
            )
            try:
                context = browser.new_context(
                    user_agent=(
                        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                        "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
                    ),
                    viewport={"width": 1366, "height": 900},
                    locale="en-US",
                )
                page = context.new_page()
                response = page.goto(url, wait_until="domcontentloaded", timeout=self.TIMEOUT_MS)
                if response is None:
                    raise RuntimeError(f"No response from {url}")
                if response.status >= 400:
                    raise RuntimeError(
                        f"HTTP {response.status} fetching {url} via Playwright"
                    )
                page.wait_for_timeout(self.WAIT_AFTER_LOAD_MS)
                html = page.content()
                final_url = page.url
            finally:
                browser.close()

        return html, final_url

    def _extract_title(self, html: str, url: str) -> str:
        import html as html_module

        def clean(s: str) -> str:
            s = html_module.unescape(s)
            s = re.split(r'\s+[|>]\s+', s)[0]
            return re.sub(r'\s+', ' ', s).strip()

        m = re.search(r'<title[^>]*>(.*?)</title>', html, re.I | re.S)
        if m:
            t = clean(m.group(1))
            if len(t) > 15:
                return t

        for pat in [
            r'<meta[^>]+property=["\']og:title["\'][^>]+content=["\'](.*?)["\']',
            r'<meta[^>]+content=["\'](.*?)["\'][^>]+property=["\']og:title["\']',
        ]:
            m = re.search(pat, html, re.I | re.S)
            if m:
                t = clean(m.group(1))
                if t:
                    return t

        path = urlparse(url).path.rstrip("/")
        return path.split("/")[-1].replace("-", " ").replace("_", " ") or urlparse(url).netloc

    def _extract_date(self, html: str) -> str:
        patterns = [
            r'<meta[^>]+property=["\']article:published_time["\'][^>]+content=["\']([\d\-T:Z+]+)["\']',
            r'<meta[^>]+content=["\']([\d\-T:Z+]+)["\'][^>]+property=["\']article:published_time["\']',
            r'<meta[^>]+name=["\']DC\.date["\'][^>]+content=["\']([\d\-T:Z+]+)["\']',
            r'<meta[^>]+name=["\']pubdate["\'][^>]+content=["\']([\d\-T:Z+]+)["\']',
            r'<time[^>]+datetime=["\']([\d\-T:Z+]+)["\']',
        ]
        for pat in patterns:
            m = re.search(pat, html, re.I)
            if m:
                raw = m.group(1)
                try:
                    dt = datetime.fromisoformat(raw.replace("Z", "+00:00"))
                    return dt.date().isoformat()
                except ValueError:
                    if re.match(r'\d{4}-\d{2}-\d{2}', raw):
                        return raw[:10]
        return ""

    def _detect_content_type(self, url: str) -> str:
        u = url.lower()
        if any(k in u for k in ("press-release", "pressrelease", "press_release")):
            return "press_release"
        if any(k in u for k in ("speech", "remarks", "statement", "testimony")):
            return "speech"
        if "transcript" in u:
            return "transcript"
        return "article"

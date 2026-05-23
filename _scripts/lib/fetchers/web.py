"""Web fetcher: curl_cffi (browser TLS impersonation) + trafilatura."""

import re
import time
from datetime import datetime
from urllib.parse import urlparse

import trafilatura

try:
    from curl_cffi import requests
    _IMPERSONATE = "firefox"
except ImportError:
    import requests
    _IMPERSONATE = None

from lib.fetchers.base import BaseFetcher


class WebFetcher(BaseFetcher):

    HEADERS = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
    }
    TIMEOUT = 30
    _RETRY_DELAY = 3  # seconds before one retry on 403/429

    def fetch(self, url: str) -> dict:
        warnings = []

        html = self._download(url)

        content = trafilatura.extract(
            html,
            url=url,
            include_links=False,
            include_images=False,
            include_tables=True,
            output_format="markdown",
        )

        if not content:
            warnings.append(
                "trafilatura extracted no content — page may be JavaScript-rendered, "
                "paywalled, or require authentication."
            )
            content = ""

        title = self._extract_title(html, url)
        pub_date = self._extract_date(html)

        if not pub_date:
            warnings.append("Publication date not found in page metadata — fill in manually.")

        return {
            "title": title,
            "content": content,
            "content_type": self._detect_content_type(url),
            "publication_date": pub_date,
            "warnings": warnings,
        }

    def _download(self, url: str) -> str:
        return self._attempt(url, retry=True)

    def _attempt(self, url: str, retry: bool) -> str:
        kwargs = {"headers": self.HEADERS, "timeout": self.TIMEOUT}
        if _IMPERSONATE:
            kwargs["impersonate"] = _IMPERSONATE
        try:
            r = requests.get(url, **kwargs)
        except Exception as e:
            raise RuntimeError(f"Network error fetching {url}: {e}")

        if self.debug:
            print(f"\n[DEBUG] Request headers:")
            for k, v in self.HEADERS.items():
                print(f"  {k}: {v}")
            print(f"[DEBUG] Response status : {r.status_code}")
            print(f"[DEBUG] Response headers:")
            for k, v in r.headers.items():
                print(f"  {k}: {v}")
            print(f"[DEBUG] Response body (first 500 bytes):")
            print(f"  {r.text[:500]!r}\n")

        if r.status_code in (403, 429) and retry:
            time.sleep(self._RETRY_DELAY)
            return self._attempt(url, retry=False)

        # Status check (curl_cffi uses different exception classes than requests,
        # so check status directly rather than via raise_for_status())
        if r.status_code >= 400:
            if r.status_code in (403, 429):
                # Last-resort fallback: try a real headless browser. Akamai
                # and Cloudflare bot detection often inspects TLS fingerprints
                # in ways curl_cffi cannot fully imitate, but a real Chromium
                # via Playwright defeats most of those layers.
                playwright_html = self._try_playwright_fallback(url)
                if playwright_html is not None:
                    return playwright_html
                raise RuntimeError(
                    f"HTTP {r.status_code} fetching {url} — fetch failed after retry "
                    f"and Playwright fallback; try --debug to diagnose, or fall back "
                    f"to manual download as last resort."
                )
            raise RuntimeError(f"HTTP {r.status_code} fetching {url}")

        return r.text

    def _try_playwright_fallback(self, url: str) -> str | None:
        """Last-resort fetch through a real headless browser.

        Returns the rendered HTML on success, or None if Playwright is not
        installed or the fallback itself fails. Caller decides what to do
        with None (raise the original 403 error message).
        """
        try:
            from playwright.sync_api import sync_playwright
        except ImportError:
            if self.debug:
                print("[DEBUG] Playwright not installed — fallback skipped.")
            return None

        if self.debug:
            print(f"[DEBUG] Falling back to Playwright for {url}")

        try:
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
                    response = page.goto(url, wait_until="domcontentloaded", timeout=30_000)
                    if response is None or response.status >= 400:
                        if self.debug:
                            status = response.status if response else "no-response"
                            print(f"[DEBUG] Playwright fallback got status {status}")
                        return None
                    page.wait_for_timeout(1_500)
                    html = page.content()
                finally:
                    browser.close()
        except Exception as e:
            if self.debug:
                print(f"[DEBUG] Playwright fallback errored: {e}")
            return None

        if self.debug:
            print(f"[DEBUG] Playwright fallback succeeded — {len(html)} chars")
        return html

    def _extract_title(self, html: str, url: str) -> str:
        import html as html_module

        def clean(s: str) -> str:
            s = html_module.unescape(s)
            # Strip " > Site Name > Section" suffixes common on .mil sites
            s = re.split(r'\s+[|>]\s+', s)[0]
            return re.sub(r'\s+', ' ', s).strip()

        # Prefer <title> tag — .mil sites often have full article title there
        m = re.search(r'<title[^>]*>(.*?)</title>', html, re.I | re.S)
        if m:
            t = clean(m.group(1))
            if len(t) > 15:   # skip section-name stubs like "News" or "Home"
                return t

        # Fall back to og:title (may be truncated or entity-encoded)
        for pat in [
            r'<meta[^>]+property=["\']og:title["\'][^>]+content=["\'](.*?)["\']',
            r'<meta[^>]+content=["\'](.*?)["\'][^>]+property=["\']og:title["\']',
        ]:
            m = re.search(pat, html, re.I | re.S)
            if m:
                t = clean(m.group(1))
                if t:
                    return t

        # Last resort: last path segment
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

"""PDF fetcher: pypdf."""

import io
import re
from urllib.parse import urlparse

import requests
from pypdf import PdfReader

from lib.fetchers.base import BaseFetcher


class PDFFetcher(BaseFetcher):

    HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; defense-research-vault/1.0)"}
    TIMEOUT = 60

    def fetch(self, url: str) -> dict:
        warnings = []

        pdf_bytes = self._download(url, warnings)
        reader = self._parse(pdf_bytes)

        meta = reader.metadata or {}
        title = self._extract_title(meta, url)
        pub_date = self._extract_date(meta)

        if not title:
            warnings.append("PDF metadata missing title — using filename as fallback.")
        if not pub_date:
            warnings.append("PDF metadata missing publication date — fill in manually.")

        pages_text, image_only = self._extract_text(reader)

        if image_only:
            warnings.append(
                "No extractable text — PDF appears to be image-based. "
                "OCR required before content is usable. File quarantined."
            )
            content = ""
        else:
            content = "\n\n".join(pages_text)

        return {
            "title": title,
            "content": content,
            "content_type": "pdf",
            "publication_date": pub_date,
            "warnings": warnings,
        }

    def _download(self, url: str, warnings: list) -> io.BytesIO:
        try:
            r = requests.get(url, headers=self.HEADERS, timeout=self.TIMEOUT, stream=True)
            r.raise_for_status()
        except requests.HTTPError as e:
            code = e.response.status_code
            if code == 403:
                raise RuntimeError(
                    f"HTTP 403 — this PDF may require authentication. "
                    f"Download manually and ingest from a local path. ({url})"
                )
            raise RuntimeError(f"HTTP {code} fetching PDF {url}: {e}")
        except requests.RequestException as e:
            raise RuntimeError(f"Network error fetching PDF {url}: {e}")

        ct = r.headers.get("content-type", "")
        if "pdf" not in ct and not url.lower().endswith(".pdf"):
            warnings.append(f"Content-Type is '{ct}' — may not be a PDF.")

        return io.BytesIO(r.content)

    def _parse(self, pdf_bytes: io.BytesIO) -> PdfReader:
        try:
            return PdfReader(pdf_bytes)
        except Exception as e:
            raise RuntimeError(f"Could not parse PDF: {e}")

    def _extract_title(self, meta: dict, url: str) -> str:
        title = (meta.get("/Title") or "").strip()
        if not title:
            title = urlparse(url).path.split("/")[-1]
            title = re.sub(r'\.pdf$', '', title, flags=re.I)
            title = title.replace("-", " ").replace("_", " ").strip()
        return title

    def _extract_date(self, meta: dict) -> str:
        raw = str(meta.get("/CreationDate") or meta.get("/ModDate") or "")
        m = re.match(r"D:(\d{4})(\d{2})(\d{2})", raw)
        if m:
            return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
        return ""

    def _extract_text(self, reader: PdfReader) -> tuple[list[str], bool]:
        pages = []
        for i, page in enumerate(reader.pages, start=1):
            text = (page.extract_text() or "").strip()
            if text:
                pages.append(f"### Page {i}\n\n{text}")
        image_only = len(pages) == 0 and len(reader.pages) > 0
        return pages, image_only

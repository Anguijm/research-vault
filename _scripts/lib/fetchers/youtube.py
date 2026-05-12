"""YouTube fetcher: Supadata API."""

import os
from urllib.parse import urlparse, parse_qs

import requests

from lib.fetchers.base import BaseFetcher

SUPADATA_TRANSCRIPT_URL = "https://api.supadata.ai/v1/youtube/transcript"


class YouTubeFetcher(BaseFetcher):

    def fetch(self, url: str) -> dict:
        api_key = os.environ.get("SUPADATA_API_KEY", "").strip()
        if not api_key:
            raise RuntimeError(
                "SUPADATA_API_KEY is not set. Add it to _scripts/.env and retry.\n"
                "  Get a key at https://supadata.ai"
            )

        video_id = self._extract_video_id(url)
        if not video_id:
            raise RuntimeError(f"Could not extract YouTube video ID from: {url}")

        data = self._call_supadata(api_key, video_id)

        title = data.get("title") or f"YouTube — {video_id}"
        pub_date = (data.get("publishedAt") or "")[:10]

        warnings = []
        if not pub_date:
            warnings.append("Upload date not returned by Supadata — fill in manually.")

        content = self._format_transcript(data)

        return {
            "title": title,
            "content": content,
            "content_type": "youtube",
            "publication_date": pub_date,
            "warnings": warnings,
        }

    def _extract_video_id(self, url: str) -> str:
        parsed = urlparse(url)
        if "youtu.be" in parsed.netloc:
            return parsed.path.lstrip("/").split("?")[0]
        ids = parse_qs(parsed.query).get("v", [])
        return ids[0] if ids else ""

    def _call_supadata(self, api_key: str, video_id: str) -> dict:
        try:
            r = requests.get(
                SUPADATA_TRANSCRIPT_URL,
                headers={"x-api-key": api_key},
                params={"videoId": video_id, "lang": "en"},
                timeout=30,
            )
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            code = e.response.status_code
            if code == 401:
                raise RuntimeError("SUPADATA_API_KEY is invalid or expired.")
            if code == 404:
                raise RuntimeError(
                    f"No transcript found for video '{video_id}'. "
                    "The video may have no captions, or captions may be disabled."
                )
            raise RuntimeError(f"Supadata API error {code}: {e}")
        except requests.RequestException as e:
            raise RuntimeError(f"Network error calling Supadata API: {e}")

    def _format_transcript(self, data: dict) -> str:
        segments = data.get("content", [])

        if isinstance(segments, str):
            return segments

        if not segments:
            return ""

        lines = []
        for seg in segments:
            if not isinstance(seg, dict):
                lines.append(str(seg))
                continue
            text = seg.get("text", "").strip()
            if not text:
                continue
            offset = seg.get("offset") or seg.get("start")
            speaker = seg.get("speaker", "")
            parts = []
            if offset is not None:
                parts.append(f"[{self._ms_to_timestamp(offset)}]")
            if speaker:
                parts.append(f"**{speaker}:**")
            parts.append(text)
            lines.append(" ".join(parts))

        return "\n\n".join(lines)

    def _ms_to_timestamp(self, ms) -> str:
        try:
            total = int(ms) // 1000
            return f"{total // 60:02d}:{total % 60:02d}"
        except (TypeError, ValueError):
            return str(ms)

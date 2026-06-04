---
name: Operator's MegaRust 2026 Google Drive — phantom 0-byte file collision
description: The Drive folder has duplicate-named files (one real, one 0-byte) that gdown's folder-walk downloads in order, overwriting the good file. Workaround is to pull the real file by ID directly.
type: reference
originSessionId: 254eda7f-7db4-4f93-b460-1e14e2726754
---
# Operator's MegaRust 2026 Google Drive — phantom 0-byte file collision

## What happened

The operator's MegaRust 2026 audio Drive folder (`https://drive.google.com/drive/folders/1ezx8DV3SsSDS6KHgr5lyIFAo0ffgvsnP`) has at least one case where two files share the same name — the real recording (e.g., 91 MB) and an empty 0-byte phantom. Specifically observed 2026-06-04: `Voice 260603_105026.m4a` had both:

- File ID `1YlKTL2CKugYB19DuJnrA86TJ5OdUUvpU` — 91.3 MB real audio
- File ID `1XP5q56PE1RTGPL2h_bCy80iWxnLUVDXC` — 0 bytes empty

gdown's `--folder` mode downloads both in sequence and the empty one **overwrites** the real one. Result: a 0-byte file in the destination, useless for transcription.

## Operator status (2026-06-04)

Operator confirmed the Drive won't let them delete the phantom from the source. So the collision persists on the Drive side. The workaround has to live on the download side.

## Workaround

When pulling from this Drive folder, if a file lands as 0 bytes:

1. Re-run gdown's folder-walk to confirm both file IDs.
2. Identify the real file by size (gdown prints the URL with the file ID before the download progress bar).
3. Pull the real file directly by its ID using the URL form (not the `--id` flag, which gdown no longer supports):

```bash
~/.local/whisper-venv/bin/gdown "https://drive.google.com/uc?id=<FILE_ID>" --output /home/johnanguiano/research/trip-reports/MEGARUST-2026/audio/<filename>.m4a
```

4. Verify with `ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 <file>` before kicking off transcription. A real file returns a duration in seconds; a corrupted file returns "moov atom not found."

## Why this matters

This is a recoverable error if caught early, but a 0-byte file silently fails transcription with a misleading error (faster-whisper exits without a useful message). Always size-check audio after download before kicking off transcription.

## When this rule expires

When the operator deletes the phantom files from the Drive, or when this specific MegaRust 2026 Drive folder is no longer being pulled from. Until then, the workaround is the only safe download path.

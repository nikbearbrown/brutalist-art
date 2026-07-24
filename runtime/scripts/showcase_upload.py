#!/usr/bin/env python3
"""
showcase_upload.py — upload finished showcase-series episode cuts to YouTube.

Reads episodes.json for titles/descriptions, uploads each final mp4 as
UNLISTED (Bear flips public in Studio), and adds to the correct playlist.

Usage (run from brutalist-art/):
  python3 runtime/scripts/showcase_upload.py <mark> \\
      --channel nikbearbrown \\
      --playlist-16x9 "Brutalist — Claude for Video Production" \\
      --playlist-916  "Shorts" \\
      [--dry-run]

Auth: uses youtube/credentials/<channel>/{client_secret.json,youtube_token.json}
Ledger: youtube/credentials/<channel>/showcase_upload_ledger.json (written on success)
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ART = Path(__file__).resolve().parents[2]
SERIES = ART / "youtube" / "showcase-series"
CREDS = ART / "youtube" / "credentials"
SCOPES = [
    "https://www.googleapis.com/auth/youtube.upload",
    "https://www.googleapis.com/auth/youtube",
    "https://www.googleapis.com/auth/youtube.force-ssl",
]


def get_service(channel: str):
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build

    d = CREDS / channel
    client = d / "client_secret.json"
    token = d / "youtube_token.json"
    creds = None
    if token.exists():
        creds = Credentials.from_authorized_user_file(str(token), SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(str(client), SCOPES)
            creds = flow.run_local_server(port=0)
        token.write_text(creds.to_json())
    return build("youtube", "v3", credentials=creds)


def ensure_playlist(youtube, title: str, cache: dict) -> str:
    if title in cache:
        return cache[title]
    pid, token = None, None
    while True:
        resp = youtube.playlists().list(
            part="id,snippet", mine=True, maxResults=50, pageToken=token
        ).execute()
        for it in resp.get("items", []):
            if it["snippet"]["title"] == title:
                pid = it["id"]
                break
        token = resp.get("nextPageToken")
        if pid or not token:
            break
    if pid is None:
        resp = youtube.playlists().insert(
            part="snippet,status",
            body={"snippet": {"title": title},
                  "status": {"privacyStatus": "public"}},
        ).execute()
        pid = resp["id"]
        print(f"  + created playlist '{title}'")
    cache[title] = pid
    return pid


def add_to_playlist(youtube, playlist_id: str, video_id: str):
    youtube.playlistItems().insert(
        part="snippet",
        body={"snippet": {
            "playlistId": playlist_id,
            "resourceId": {"kind": "youtube#video", "videoId": video_id},
        }},
    ).execute()


def upload_video(youtube, mp4: Path, title: str, description: str, tags: list[str]) -> str:
    from googleapiclient.http import MediaFileUpload

    body = {
        "snippet": {
            "title": title[:100],
            "description": description[:5000],
            "tags": tags[:30],
            "categoryId": "27",  # Education
        },
        "status": {
            "privacyStatus": "unlisted",
            "selfDeclaredMadeForKids": False,
        },
    }
    media = MediaFileUpload(str(mp4), chunksize=-1, resumable=True, mimetype="video/mp4")
    req = youtube.videos().insert(part="snippet,status", body=body, media_body=media)
    resp = None
    while resp is None:
        status, resp = req.next_chunk()
        if status:
            pct = int(status.progress() * 100)
            print(f"    {pct}%", end="\r", flush=True)
    print()
    return resp["id"]


def make_description(ep: dict, cfg: dict, aspect: str) -> str:
    handle = cfg.get("handle", "@NikBearBrown")
    series = cfg.get("series_title", cfg["mark"])
    n = ep["n"]
    title_str = ep["title_out"]["title"]
    your_turn_prompt = ep["your_turn"]["prompt"]
    recap_lines = ep.get("recap", {}).get("artifactLines", []) if aspect == "16x9" else []

    lines = [
        title_str,
        "",
        f"Part {n} of 5 from '{series}' — twenty logo motion techniques across five episodes, "
        "built entirely in Remotion. No keyframes: every move is a pure function of the frame.",
        "",
    ]
    if aspect == "16x9":
        lines += [
            f"Techniques in this episode: {ep['title']}",
            "",
        ]
        if recap_lines:
            lines += ["Recap:", *[f"  · {l}" for l in recap_lines], ""]
    lines += [
        "Your turn prompt:",
        f"  {your_turn_prompt}",
        "",
        f"{handle}",
        "#Remotion #LogoAnimation #MotionDesign #BrutalistVideo #ClaudeAI",
    ]
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mark")
    ap.add_argument("--channel", default="nikbearbrown")
    ap.add_argument("--playlist-16x9", default="Brutalist — Claude for Video Production")
    ap.add_argument("--playlist-916", default="Shorts")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    cfg_path = SERIES / args.mark / "episodes.json"
    if not cfg_path.exists():
        sys.exit(f"[showcase_upload] no episodes.json at {cfg_path}")
    cfg = json.loads(cfg_path.read_text())

    ledger_path = CREDS / args.channel / "showcase_upload_ledger.json"
    ledger = json.loads(ledger_path.read_text()) if ledger_path.exists() else {}

    yt = None if args.dry_run else get_service(args.channel)
    pl_cache: dict[str, str] = {}

    for ep in cfg["episodes"]:
        n = ep["n"]
        for aspect in ("16x9", "916"):
            cut = f"ep{n:02d}" + ("-16x9" if aspect == "16x9" else "")
            mp4 = SERIES / args.mark / cut / f"{args.mark}-{cut}.mp4"
            if not mp4.exists():
                print(f"  [skip] {cut}: final mp4 missing at {mp4.relative_to(ART)}")
                continue

            ledger_key = f"{args.mark}::{cut}"
            if ledger_key in ledger:
                print(f"  [skip] {cut}: already uploaded → {ledger[ledger_key]['videoId']}")
                continue

            title = ep["title_out"]["title"]
            description = make_description(ep, cfg, aspect)
            playlist_name = args.playlist_16x9 if aspect == "16x9" else args.playlist_916
            tags = ["Remotion", "LogoAnimation", "MotionDesign", "ClaudeAI", "BrutalistVideo",
                    "SVGAnimation", ep["title"]]

            mb = mp4.stat().st_size // (1024 * 1024)
            print(f"  {'[DRY-RUN] ' if args.dry_run else ''}uploading {cut} ({mb}MB) → '{title}' → {playlist_name}")

            if args.dry_run:
                continue

            vid_id = upload_video(yt, mp4, title, description, tags)
            print(f"    videoId: {vid_id}")

            pl_id = ensure_playlist(yt, playlist_name, pl_cache)
            add_to_playlist(yt, pl_id, vid_id)
            print(f"    added to '{playlist_name}'")

            ledger[ledger_key] = {
                "videoId": vid_id,
                "title": title,
                "playlist": playlist_name,
                "file": str(mp4),
            }
            ledger_path.write_text(json.dumps(ledger, indent=2, ensure_ascii=False))
            print(f"    ledger saved → https://youtu.be/{vid_id}")

    print("[showcase_upload] done")


if __name__ == "__main__":
    main()

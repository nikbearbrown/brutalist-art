#!/usr/bin/env python3
"""
publish_playlist.py — upload finished Medhavy videos to @MedhavyAI and add them to a
named playlist IN CHAPTER ORDER.

For each video folder (one per NotebookLM video, each with beat_sheet.json,
mp4/<slug>.mp4, and description.txt), this:
  1. authenticates to the YouTube Data API (OAuth desktop flow, cached token),
  2. finds — or creates — the target playlist by title,
  3. uploads any folder not already in the ledger, then
  4. inserts each into the playlist at the position given by its chapter_number,
     so the playlist reads in chapter order regardless of upload order.

Videos upload as `unlisted` by default: a brand-new YouTube API project cannot make
uploads public until Google approves an API audit, and forcing `public` before that
just fails. Flip to --privacy public once audited (or publish each from the Studio UI).

One-time setup (see references/youtube-setup.md): a Google Cloud project with the
YouTube Data API enabled, an OAuth "Desktop app" client saved as client_secret.json,
and the @MedhavyAI account added as a test user on the consent screen.

Install:  pip install google-api-python-client google-auth-oauthlib google-auth-httplib2

Usage:
    # preview only — no upload, no quota:
    python publish_playlist.py --root path/to/notebooklm-videos --dry-run

    # upload everything not yet posted, add to the playlist in chapter order:
    python publish_playlist.py --root path/to/notebooklm-videos \
        --playlist "Quantum Mechanics Volume 1 (NotebookLM)"

    # specific folders:
    python publish_playlist.py FOLDER_A FOLDER_B --privacy public
"""
from __future__ import annotations

import argparse
import os, json
import sys
import time
from pathlib import Path

SCOPES = [
    "https://www.googleapis.com/auth/youtube.upload",
    "https://www.googleapis.com/auth/youtube",
]
EDU_CATEGORY = "27"

# ── Series anchors ───────────────────────────────────────────────────────────
# The whole series funnels to one intro video and one master playlist. By DEFAULT
# every SHORT's description points to the intro VIDEO ("What is Brutalist?"), and
# every LONG's description points to the series PLAYLIST ("Brutalist"). Override
# either in .env (blank disables that anchor); pass --no-anchor to skip entirely.
ANCHOR_VIDEO_URL    = os.environ.get("ART_ANCHOR_VIDEO_URL",
                                     "https://youtu.be/xXKgCXc1nm4")                       # What is Brutalist?
ANCHOR_PLAYLIST_URL = os.environ.get("ART_ANCHOR_PLAYLIST_URL",
                                     "https://www.youtube.com/playlist?list=PLG9H-C6rp5RU")  # Brutalist

def anchor_block(kind: str) -> str:
    if kind == "short":
        return f"\n\n▶ Start the series — What is Brutalist?\n{ANCHOR_VIDEO_URL}" if ANCHOR_VIDEO_URL else ""
    return f"\n\n▶ The full series playlist — Brutalist\n{ANCHOR_PLAYLIST_URL}" if ANCHOR_PLAYLIST_URL else ""

def folder_kind(folder: Path, default: str) -> str:
    """A short if it lives in a short/ subfolder or its metadata says so; else the CLI default."""
    if folder.name == "short":
        return "short"
    try:
        m = json.loads((folder / "beat_sheet.json").read_text()).get("metadata", {})
    except Exception:
        m = {}
    if str(m.get("kind", "")).lower() == "short" or str(m.get("format", "")).lower() in ("short", "9:16", "vertical"):
        return "short"
    return default


def get_service(client_secret: Path, token_path: Path):
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build

    creds = None
    if token_path.exists():
        creds = Credentials.from_authorized_user_file(str(token_path), SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not client_secret.exists():
                sys.exit(f"[yt] missing OAuth client secret: {client_secret}\n"
                         f"    See references/youtube-setup.md.")
            flow = InstalledAppFlow.from_client_secrets_file(str(client_secret), SCOPES)
            creds = flow.run_local_server(port=0)
        token_path.write_text(creds.to_json())
    return build("youtube", "v3", credentials=creds)


def find_or_create_playlist(youtube, title: str, privacy: str, dry: bool) -> str | None:
    req = youtube.playlists().list(part="id,snippet", mine=True, maxResults=50)
    while req is not None:
        resp = req.execute()
        for it in resp.get("items", []):
            if it["snippet"]["title"].strip().lower() == title.strip().lower():
                print(f"[yt] found playlist '{title}' → {it['id']}")
                return it["id"]
        req = youtube.playlists().list_next(req, resp)
    if dry:
        print(f"[yt] (dry-run) would CREATE playlist '{title}'")
        return None
    resp = youtube.playlists().insert(
        part="snippet,status",
        body={"snippet": {"title": title,
                          "description": "NotebookLM deep dives, chapter by chapter. By Medhavy."},
              "status": {"privacyStatus": "public" if privacy == "public" else "unlisted"}},
    ).execute()
    print(f"[yt] created playlist '{title}' → {resp['id']}")
    return resp["id"]


def already_in_playlist(youtube, playlist_id: str) -> dict:
    """videoId -> playlistItemId, so re-runs don't double-add."""
    import time
    from googleapiclient.errors import HttpError
    out = {}
    req = youtube.playlistItems().list(part="id,contentDetails", playlistId=playlist_id, maxResults=50)
    while req is not None:
        try:
            resp = req.execute()
        except HttpError as e:
            if e.resp.status == 404:
                # Newly created playlist not yet propagated — treat as empty
                time.sleep(3)
                return {}
            raise
        for it in resp.get("items", []):
            out[it["contentDetails"]["videoId"]] = it["id"]
        req = youtube.playlistItems().list_next(req, resp)
    return out


def upload_video(youtube, folder: Path, privacy: str, kind: str = "long", add_anchor: bool = True):
    from googleapiclient.http import MediaFileUpload
    sheet = json.loads((folder / "beat_sheet.json").read_text())
    md = sheet["metadata"]
    slug = md["slug"]
    mp4 = folder / "mp4" / f"{slug}.mp4"
    if not mp4.exists():
        raise SystemExit(f"[yt] no master mp4: {mp4} (run sandwich.py first)")
    desc = (folder / "description.txt")
    description = desc.read_text() if desc.exists() else md.get("title", "")
    if add_anchor:
        link = ANCHOR_VIDEO_URL if kind == "short" else ANCHOR_PLAYLIST_URL
        if link and link not in description:            # idempotent: don't double-append
            description = description.rstrip() + anchor_block(kind)

    body = {
        "snippet": {
            "title": md["title"][:100],
            "description": description,
            "categoryId": EDU_CATEGORY,
            "tags": (md.get("tags") or ["Quantum Mechanics", "Physics", "NotebookLM", "Medhavy",
                     md.get("chapter_title", "")])[:15],
        },
        "status": {"privacyStatus": "public" if privacy == "public" else "unlisted",
                   "selfDeclaredMadeForKids": False},
    }
    media = MediaFileUpload(str(mp4), chunksize=-1, resumable=True, mimetype="video/mp4")
    req = youtube.videos().insert(part="snippet,status", body=body, media_body=media)
    print(f"[yt] uploading {mp4.name} …")
    resp = None
    while resp is None:
        status, resp = req.next_chunk()
        if status:
            print(f"    {int(status.progress()*100)}%")
    vid = resp["id"]
    print(f"[yt] uploaded → https://youtu.be/{vid}")
    return vid


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("folders", nargs="*", help="explicit video folders")
    ap.add_argument("--root", help="scan this dir for video folders (each has beat_sheet.json)")
    ap.add_argument("--playlist", default="Quantum Mechanics Volume 1 (NotebookLM)")
    ap.add_argument("--privacy", choices=["unlisted", "public"], default="unlisted")
    ap.add_argument("--channel", default=os.getenv("ART_YOUTUBE_CHANNEL", "nikbearbrown"),
                    help="channel key → youtube/credentials/<channel>/ (default: $ART_YOUTUBE_CHANNEL or nikbearbrown)")
    ap.add_argument("--client", default=None)
    ap.add_argument("--token", default=None)
    ap.add_argument("--ledger", default=None)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--kind", choices=["long", "short"], default="long",
                    help="long → description points to the series PLAYLIST; short → to the intro VIDEO "
                         "(auto-detected for short/ subfolders regardless)")
    ap.add_argument("--no-anchor", action="store_true",
                    help="do not append the default series cross-link to the description")
    args = ap.parse_args()

    folders = [Path(f).expanduser().resolve() for f in args.folders]
    if args.root:
        root = Path(args.root).expanduser().resolve()
        folders += [p.parent for p in root.glob("*/beat_sheet.json")]
    folders = sorted(set(folders),
                     key=lambda f: json.loads((f / "beat_sheet.json").read_text())
                     ["metadata"].get("chapter_number") or 999)
    if not folders:
        sys.exit("[yt] no video folders found (need --root or explicit folders)")

    print("[yt] publish order (by chapter):")
    for f in folders:
        m = json.loads((f / "beat_sheet.json").read_text())["metadata"]
        print(f"   ch{m.get('chapter_number')}  {m['title']}")

    if args.dry_run:
        print("[yt] dry-run — authenticating read-only preview")

    _repo = Path(os.environ.get("ART_HOME") or Path(__file__).resolve().parents[4])  # repo root
    _cred = _repo / "youtube" / "credentials" / args.channel
    client_p = Path(args.client).resolve() if args.client else _cred / "client_secret.json"
    token_p  = Path(args.token).resolve()  if args.token  else _cred / "youtube_token.json"
    if not client_p.exists():
        sys.exit(f"[yt] no client_secret at {client_p} — put OAuth creds in "
                 f"youtube/credentials/{args.channel}/ (see .env.example)")
    youtube = get_service(client_p, token_p)
    playlist_id = find_or_create_playlist(youtube, args.playlist, args.privacy, args.dry_run)
    in_pl = already_in_playlist(youtube, playlist_id) if (playlist_id and not args.dry_run) else {}

    ledger_path = (Path(args.ledger).resolve() if args.ledger else _cred / "youtube_publish_ledger.json")
    ledger = json.loads(ledger_path.read_text()) if ledger_path.exists() else {}

    for pos, folder in enumerate(folders):
        slug = json.loads((folder / "beat_sheet.json").read_text())["metadata"]["slug"]
        if slug in ledger:
            vid = ledger[slug]
            print(f"[yt] {slug} already uploaded → {vid}")
        elif args.dry_run:
            print(f"[yt] (dry-run) would upload {slug}")
            continue
        else:
            kind = folder_kind(folder, args.kind)
            vid = upload_video(youtube, folder, args.privacy, kind=kind, add_anchor=not args.no_anchor)
            ledger[slug] = vid
            ledger_path.write_text(json.dumps(ledger, indent=1))

        if playlist_id and not args.dry_run and vid not in in_pl:
            youtube.playlistItems().insert(
                part="snippet",
                body={"snippet": {"playlistId": playlist_id,
                                  "resourceId": {"kind": "youtube#video", "videoId": vid}}},
            ).execute()
            print(f"[yt] added {slug} to playlist at position {pos}")
            time.sleep(1)

    print("[yt] done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Upload The Prompting Playbook to @NikBearBrown / Claude prompting playlist."""
import argparse, json, sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

REEL          = Path(__file__).parent
VIDEO         = REEL / "claude-liam-prompting-playbook.mp4"
SRT           = REEL / "claude-liam-prompting-playbook.srt"
CREDS_DIR     = Path("/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/youtube/credentials/nikbearbrown")
CLIENT_SECRET = CREDS_DIR / "client_secret.json"
TOKEN_FILE    = CREDS_DIR / "youtube_token.json"

TITLE = "The Prompting Playbook — Debug the Prompt Like Code"
TAGS  = ["Claude", "Anthropic", "Prompt Engineering", "LLM", "AI Engineering",
         "Prompting", "Evals", "Claude Code", "Teardown", "NikBearBrown",
         "Liam in for Bear", "Production AI", "AI Best Practices"]
DESCRIPTION = """\
Anthropic engineer Margot Vanlar runs the real prompting playbook on a real production prompt. Two scenarios, one discipline: a prompt in production that broke on migration, and a new agentic system built from zero. Liam, in for Bear.

The playbook in four moves: evals first, hygiene second, patch debt third, capability gap fourth. A prompt that works is debugged like code — reproducible test cases, one failure mode at a time.

0:00 The playbook in four moves (verdict)
0:34 Two scenarios, one discipline
0:54 Two scenarios unpacked — production vs. zero
1:17 Eval suite: control, edge, boundary
1:44 Hygiene: XML structure + output contract
2:17 Patch debt — old defensive instructions backfire
2:52 Instructions don't add capability — tools do
3:25 Both sides of the trade-off (billing escalation)
3:57 New agent: model × prompt × harness
4:26 Generate-evaluate-repair loop
5:00 Your turn — build your eval suite

Source: Anthropic "Code with Claude" — The Prompting Playbook (Margot Vanlar, Applied AI Engineer)

Built with Kokoro am_onyx voice · Claude fidelity skin · Manim + Remotion visuals.
Liam, in for Bear.

youtube.com/@NikBearBrown

#Claude #AnthropicAI #PromptEngineering #LLM #AIEngineering #NikBearBrown
"""
PLAYLIST_NAME = "Claude prompting"
CATEGORY      = "28"   # Science & Technology

SCOPES = ["https://www.googleapis.com/auth/youtube.upload",
          "https://www.googleapis.com/auth/youtube",
          "https://www.googleapis.com/auth/youtube.force-ssl"]


def get_service():
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
    creds = None
    if TOKEN_FILE.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(str(CLIENT_SECRET), SCOPES)
            creds = flow.run_local_server(port=0)
        TOKEN_FILE.write_text(creds.to_json())
    return build("youtube", "v3", credentials=creds)


def ensure_playlist(yt, title):
    cache, page = {}, None
    while True:
        resp = yt.playlists().list(part="id,snippet", mine=True, maxResults=50, pageToken=page).execute()
        for item in resp.get("items", []):
            cache[item["snippet"]["title"]] = item["id"]
        page = resp.get("nextPageToken")
        if not page:
            break
    if title in cache:
        print(f"  playlist '{title}' → {cache[title]}")
        return cache[title]
    resp = yt.playlists().insert(
        part="id,snippet,status",
        body={"snippet": {"title": title}, "status": {"privacyStatus": "public"}},
    ).execute()
    pid = resp["id"]
    print(f"  created playlist '{title}' → {pid}")
    return pid


def upload_video(yt, path, publish_at):
    from googleapiclient.http import MediaFileUpload
    body = {
        "snippet": {
            "title": TITLE,
            "description": DESCRIPTION,
            "tags": TAGS,
            "categoryId": CATEGORY,
        },
        "status": {
            "privacyStatus": "private",
            "publishAt": publish_at.strftime("%Y-%m-%dT%H:%M:%S.000Z"),
            "selfDeclaredMadeForKids": False,
        },
    }
    media = MediaFileUpload(str(path), chunksize=-1, resumable=True, mimetype="video/mp4")
    req = yt.videos().insert(part="snippet,status", body=body, media_body=media)
    vid_id = None
    while vid_id is None:
        status, resp = req.next_chunk()
        if resp:
            vid_id = resp["id"]
        elif status:
            print(f"  upload {int(status.progress() * 100)}%", end="\r")
    print(f"  uploaded → https://www.youtube.com/watch?v={vid_id}")
    return vid_id


def upload_captions(yt, video_id, srt_path):
    from googleapiclient.http import MediaFileUpload
    media = MediaFileUpload(str(srt_path), mimetype="application/octet-stream")
    resp = yt.captions().insert(
        part="snippet",
        body={"snippet": {"videoId": video_id, "language": "en", "name": "English", "isDraft": False}},
        media_body=media,
    ).execute()
    print(f"  captions uploaded → {resp.get('id')}")


def add_to_playlist(yt, playlist_id, video_id):
    yt.playlistItems().insert(
        part="snippet",
        body={"snippet": {"playlistId": playlist_id,
                          "resourceId": {"kind": "youtube#video", "videoId": video_id}}},
    ).execute()
    print(f"  added to playlist {playlist_id}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not VIDEO.exists():
        sys.exit(f"Video not found: {VIDEO}")

    size_mb = VIDEO.stat().st_size // 1024 // 1024
    print(f"Video   : {VIDEO.name} ({size_mb} MB)")
    print(f"Title   : {TITLE}")
    print(f"Channel : @NikBearBrown")
    print(f"Playlist: {PLAYLIST_NAME}")
    print(f"Captions: {SRT.name if SRT.exists() else 'MISSING — upload without'}")

    if args.dry_run:
        print("[dry-run] would upload now")
        return

    publish_at = datetime.now(timezone.utc) + timedelta(minutes=15)
    print(f"Publish at (private until flipped): {publish_at.isoformat()}")

    yt = get_service()
    vid_id = upload_video(yt, VIDEO, publish_at)
    if SRT.exists():
        upload_captions(yt, vid_id, SRT)
    playlist_id = ensure_playlist(yt, PLAYLIST_NAME)
    add_to_playlist(yt, playlist_id, vid_id)

    ledger = CREDS_DIR / "youtube_publish_ledger.json"
    log = json.loads(ledger.read_text()) if ledger.exists() else []
    log.append({"video_id": vid_id, "title": TITLE, "playlist": PLAYLIST_NAME,
                "uploaded_at": datetime.now(timezone.utc).isoformat()})
    ledger.write_text(json.dumps(log, indent=2))

    print(f"\nDone.")
    print(f"  Video ID : {vid_id}")
    print(f"  Watch    : https://www.youtube.com/watch?v={vid_id}")
    print(f"  Studio   : https://studio.youtube.com/video/{vid_id}/edit")
    print(f"  Flip public in Studio when ready.")


if __name__ == "__main__":
    main()

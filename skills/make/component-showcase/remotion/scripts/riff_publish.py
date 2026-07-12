#!/usr/bin/env python3
"""riff_publish.py — the riff publish step. Reuses the existing bears-doodles YouTube
uploader (youtube_publish.py) instead of a connector or the browser.

It reads the conformed beat sheet, generates the YouTube title + description (auto chapters
from segment timings + the library credit + the channel), and assembles the publish-folder
contract youtube_publish.py expects:

  publish/<slug>/beat_sheet.json          metadata: slug, title, hashtags, playlist
  publish/<slug>/mp4/<slug>.mp4           the rendered master (copied from --video)
  publish/<slug>/<slug>-youtube.md        the full description (verbatim)

Then it prints the exact youtube_publish.py command (runs on your Mac with your OAuth —
see the bears-doodles reference/youtube-publishing.md; uploads land in the named playlist,
created if missing). Nothing is uploaded from here.

Usage:
  python3 scripts/riff_publish.py --video out/brutalist-onda.mp4 --playlist Brutalist
"""
import argparse, json, shutil, sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]  # brutalist/remotion/
# Mirror src/riff/channel.ts (the riff default channel identity).
CHANNEL = {"name": "Nik Bear Brown", "handle": "@NikBearBrown", "url": "https://www.nikbearbrown.com/"}
UPLOADER = "../../unreal-reels/aspects/explainer/bears-doodles/scripts/youtube_publish.py"


def ts(frame: int, fps: int) -> str:
    s = int(frame / fps)
    return f"{s // 60}:{s % 60:02d}"


def chapter_label(seg: dict) -> str:
    lab = seg.get("label")
    if lab and " · " in lab:  # "01 / 59 · Onda BarChart" -> "01 · Onda BarChart"
        num, rest = lab.split(" · ", 1)
        return f"{num.split('/')[0].strip()} · {rest}"
    c = seg.get("card") or {}
    return c.get("title", seg["id"])


def build_description(sheet: dict) -> str:
    # If the sheet carries its own YouTube description (non-catalog riffs — Soul ID, Manim,
    # etc.), trust it verbatim and just guarantee the channel footer. Only the template-library
    # catalog uses the auto-generated "AI makes writing Remotion trivial…/Chapters" body below.
    own = sheet.get("youtube_description") or sheet.get("description")
    if own:
        foot = f"—\n{CHANNEL['name']}\n{CHANNEL['url']}\n{CHANNEL['handle']}"
        return own if CHANNEL["handle"] in own else f"{own.rstrip()}\n\n{foot}"
    fps = sheet.get("fps", 30)
    lib = sheet.get("library", {})
    name, link = lib.get("name", "the library"), lib.get("link", "")
    total = lib.get("count", "")
    lines = []
    lines.append("AI makes writing Remotion trivial. The scarce thing now isn't the code — it's "
                 "knowing what already exists, so you can ask for the right one. This series walks the "
                 "Brutalist template library a few at a time: 367 open-source Remotion templates, "
                 "adapted and catalogued so you know what's in the tool belt.\n")
    n_tpl = sum(1 for s in sheet["segments"] if s.get("template"))
    lines.append(f"This video: {n_tpl} of {name}'s {total} components — what each one is, and when to reach for it.\n")
    if link:
        lines.append(f"Thank you, {name}. {name} is MIT-licensed and installed as source you own "
                     f"(not a black-box dependency), with one signature motion language across the whole "
                     f"catalog. Find the rest, and full credit, here:\n→ {name}: https://{link}\n")
    lines.append("Chapters")
    for s in sheet["segments"]:
        lines.append(f"{ts(s['start_frame'], fps)}  {chapter_label(s)}")
    lines.append("")
    lines.append(f"—\n{CHANNEL['name']}\n{CHANNEL['url']}\n{CHANNEL['handle']}")
    if link:
        lines.append(f"\nCredits: {name} — https://{link}")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--video", required=True, type=Path)
    ap.add_argument("--sheet", type=Path, default=HERE / "beats" / "templates-onda.conformed.json")
    ap.add_argument("--playlist", default="Brutalist")
    ap.add_argument("--slug", default=None)
    ap.add_argument("--privacy", default="unlisted", choices=["unlisted", "private"])
    ap.add_argument("--run", action="store_true", help="actually upload now (no dry-run)")
    ap.add_argument("--dry-run", action="store_true", help="preview the schedule, upload nothing")
    ap.add_argument("--workspace", type=Path,
                    default=Path("${ART_PUBLISH_WORKSPACE:-./publish-workspace}"),
                    help="holds client_secret.json + youtube_token.json + youtube_publish_ledger.json (SECRETS — never commit)")
    a = ap.parse_args()
    if not a.video.exists():
        sys.exit(f"[publish] video not found: {a.video}")
    sheet = json.loads(a.sheet.read_text())
    slug = a.slug or a.video.stem
    title = sheet.get("title", slug.replace("-", " "))
    hashtags = sheet.get("hashtags") or ["Remotion", "Onda", "MotionGraphics", "ReactVideo", "TemplateLibrary", "Brutalist", "NikBearBrown"]

    folder = HERE / "publish" / slug
    (folder / "mp4").mkdir(parents=True, exist_ok=True)
    shutil.copy(a.video, folder / "mp4" / f"{slug}.mp4")
    (folder / "beat_sheet.json").write_text(json.dumps(
        {"metadata": {"slug": slug, "title": title, "hashtags": hashtags, "playlist": a.playlist}},
        indent=1))
    (folder / f"{slug}-youtube.md").write_text(build_description(sheet))

    uploader = (HERE / UPLOADER).resolve()
    ws = a.workspace
    argv = ["python3", str(uploader), str(folder), "--no-pairs", "--allow-partial",
            "--schedule-scope", "playlist",
            "--which", "landscape", "--interval-hours", "2", "--privacy", a.privacy,
            "--client", str(ws / "client_secret.json"), "--token", str(ws / "youtube_token.json"),
            "--ledger", str(ws / "youtube_publish_ledger.json")]
    print(f"[publish] assembled {folder.relative_to(HERE)}  (title, description, chapters, playlist='{a.playlist}')")
    if a.run:
        import subprocess
        print("[publish] UPLOADING for real (no dry-run) — running your OAuth uploader...\n")
        return subprocess.run(argv).returncode
    if a.dry_run:
        import subprocess
        print("[publish] dry-run (no upload, no quota)...\n")
        return subprocess.run(argv + ["--dry-run"]).returncode
    # default: just print the ready-to-paste commands
    q = " ".join(f'"{x}"' if " " in x or "/" in x else x for x in argv)
    print("[publish] preview (no upload):\n\n  " + q + " --dry-run\n")
    print("[publish] real upload (adds to the playlist):\n\n  " + q + "\n")
    print("[publish] or just run it directly:  python3 scripts/riff_publish.py --video <mp4> --run")
    print(f"\n[note] added to the '{a.playlist}' playlist (created if missing). "
          "publish-workspace creds are SECRETS — never commit.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

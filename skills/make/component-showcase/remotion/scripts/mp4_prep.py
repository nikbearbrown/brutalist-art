#!/usr/bin/env python3
"""mp4_prep.py — stage an mp4 riff's clips into public/clips/ so Remotion's staticFile can
serve them, and sanity-check that every clip a beat sheet references actually exists.

A RiffMp4 segment references a clip by bare filename (`"clip": "braocmkcpvg.mp4"`). Remotion
only serves files under public/, so this copies each referenced clip from the sheet's
`clips_dir` (default ../higgsfield/character-tuzi) into public/clips/. Run it once before
riff_audio -> riff_conform -> render.

Usage:
  python3 scripts/mp4_prep.py beats/soul-tuzi.beats.json
  python3 scripts/mp4_prep.py beats/soul-tuzi.beats.json --clips-dir /abs/path/to/clips
"""
import argparse, json, shutil, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]  # brutalist/remotion/


def probe_duration(p: Path) -> float:
    try:
        out = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "default=nw=1:nk=1", str(p)],
            capture_output=True, text=True, check=True).stdout.strip()
        return round(float(out), 2)
    except Exception:
        return 0.0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("beatsheet", type=Path)
    ap.add_argument("--clips-dir", type=Path, default=None,
                    help="source folder of the mp4 clips (default: the sheet's clips_dir)")
    a = ap.parse_args()
    sheet = json.loads(a.beatsheet.read_text())

    src = a.clips_dir or (HERE / sheet.get("clips_dir", "../higgsfield/character-tuzi"))
    src = Path(src).resolve()
    dst = HERE / "public" / "clips"
    dst.mkdir(parents=True, exist_ok=True)

    clips = [s["clip"] for s in sheet["segments"] if s.get("clip")]
    missing, staged = [], []
    for c in clips:
        s = src / c
        if not s.exists():
            missing.append(c); continue
        d = dst / c
        if not d.exists() or d.stat().st_size != s.stat().st_size:
            shutil.copy2(s, d)
        staged.append((c, probe_duration(d)))

    for c, dur in staged:
        print(f"[clip] public/clips/{c}  ({dur:.2f}s)")
    if missing:
        print(f"\n[err] {len(missing)} clip(s) not found in {src}:", file=sys.stderr)
        for c in missing:
            print(f"      - {c}", file=sys.stderr)
        return 1
    print(f"\n[ok] {len(staged)} clips → public/clips/  (source: {src})")
    print("[next] riff_audio.py beats/soul-tuzi.beats.json → riff_conform.py → render riff-soul-tuzi")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""
suno_slice.py — slice a Suno vocal-only stem from the pantry into per-beat
mp3s, filling the SAME slots generate_audio.py would have filled.

THE CONTRACT: the human generated each <slug>.suno.N.txt (from
suno_export.py) in Suno, downloaded the VOCAL-ONLY stem, and saved it as
pantry/<slug>-vocals-N.wav (mp3/m4a/flac also accepted; a single-chunk reel
may drop the -N). This script:

  1. recomputes the export's chunking, so it knows exactly which beats each
     stem contains, in order;
  2. finds the spoken segments in each stem by silence detection
     (ffmpeg silencedetect — no extra deps);
  3. REFUSES to write anything unless segments == beats for every stem
     (tune --silence-db / --min-gap and re-run on a mismatch);
  4. slices each segment (with padding) to mp3/beat-<BID>.mp3, measures the
     real duration, and writes actual_duration_s + audio_file back into
     beat_sheet.json, plus mp3/timings.json — byte-for-byte the same
     interface generate_audio.py produces.

From here the pipeline neither knows nor cares which engine spoke:
./art run, captions, shorts, publish — all identical.

Usage:
    python3 suno_slice.py path/to/<slug>                 # slice + write back
    python3 suno_slice.py path/to/<slug> --dry-run       # report segmentation only
    python3 suno_slice.py path/to/<slug> --silence-db -35 --min-gap 0.5
"""
import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from suno_export import chunk_beats, DEFAULT_LIMIT, DEFAULT_TAG

FFMPEG = shutil.which("ffmpeg") or "ffmpeg"
FFPROBE = shutil.which("ffprobe") or "ffprobe"
STEM_EXTS = (".wav", ".mp3", ".m4a", ".flac")


def media_duration(path: Path) -> float:
    out = subprocess.run([FFPROBE, "-v", "error", "-show_entries",
                          "format=duration", "-of", "csv=p=0", str(path)],
                         capture_output=True, text=True, check=True)
    return float(out.stdout.strip())


def find_stem(folder: Path, slug: str, n: int, single: bool):
    names = [f"{slug}-vocals-{n}"] + ([f"{slug}-vocals"] if single and n == 1 else [])
    for name in names:
        for ext in STEM_EXTS:
            p = folder / "pantry" / f"{name}{ext}"
            if p.exists():
                return p
    return None


def speech_segments(stem: Path, silence_db: float, min_gap: float):
    """Spoken [start, end] windows via ffmpeg silencedetect."""
    r = subprocess.run([FFMPEG, "-i", str(stem), "-af",
                        f"silencedetect=noise={silence_db}dB:d={min_gap}",
                        "-f", "null", "-"], capture_output=True, text=True)
    starts = [float(m) for m in re.findall(r"silence_start:\s*([\d.]+)", r.stderr)]
    ends = [float(m) for m in re.findall(r"silence_end:\s*([\d.]+)", r.stderr)]
    total = media_duration(stem)
    # build speech windows between silences
    segs, cursor = [], 0.0
    for s, e in zip(starts, ends if len(ends) == len(starts) else ends + [total]):
        if s - cursor > 0.25:                      # a real spoken stretch
            segs.append([cursor, s])
        cursor = e
    if total - cursor > 0.25:
        segs.append([cursor, total])
    # a trailing silence_start with no end means the file ends silent — the
    # zip above already handled it via the padded ends list
    return segs, total


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder", type=Path)
    ap.add_argument("--limit", type=int, default=DEFAULT_LIMIT,
                    help="chunk size used at export time (must match)")
    ap.add_argument("--tag", default=DEFAULT_TAG,
                    help="meta tag used at export time (must match)")
    ap.add_argument("--silence-db", type=float, default=-38.0,
                    help="silence threshold dB (raise toward -30 if segments merge)")
    ap.add_argument("--min-gap", type=float, default=0.4,
                    help="min silence seconds between beats (Suno pauses at blank lines)")
    ap.add_argument("--pad-in", type=float, default=0.10)
    ap.add_argument("--pad-out", type=float, default=0.15)
    ap.add_argument("--dry-run", action="store_true",
                    help="report segmentation per stem; write nothing")
    a = ap.parse_args()
    folder = a.folder.resolve()
    sheet_path = folder / "beat_sheet.json"
    sheet = json.loads(sheet_path.read_text())
    slug = sheet["metadata"].get("slug", folder.name)

    chunks = chunk_beats(sheet, a.limit, a.tag)
    single = len(chunks) == 1

    # pass 1 — every stem present and cleanly segmented, or nothing happens
    plan, problems = [], []
    for n, (_, beats) in enumerate(chunks, 1):
        stem = find_stem(folder, slug, n, single)
        if stem is None:
            problems.append(f"stem {n}: missing pantry/{slug}-vocals-{n}.wav "
                            f"(covers {beats[0]['beat_id']}–{beats[-1]['beat_id']})")
            continue
        segs, total = speech_segments(stem, a.silence_db, a.min_gap)
        mark = "✓" if len(segs) == len(beats) else "✗"
        print(f"[suno] stem {n}: {stem.name}  {total:.1f}s · "
              f"{len(segs)} spoken segments for {len(beats)} beats {mark}")
        if len(segs) != len(beats):
            for i, (s, e) in enumerate(segs, 1):
                print(f"        seg {i}: {s:7.2f} → {e:7.2f}  ({e - s:.2f}s)")
            problems.append(f"stem {n}: {len(segs)} segments ≠ {len(beats)} beats — "
                            f"tune --silence-db/--min-gap, or re-generate the stem")
            continue
        plan.append((stem, total, segs, beats))
    if problems:
        print("[suno] NOT SLICING:")
        for p in problems:
            print(f"[suno]   ✗ {p}")
        return 1
    if a.dry_run:
        print("[suno] dry-run — segmentation clean, nothing written")
        return 0

    # pass 2 — slice, measure, write back
    (folder / "mp3").mkdir(exist_ok=True)
    timings_path = folder / "mp3" / "timings.json"
    timings = json.loads(timings_path.read_text()) if timings_path.exists() else {}
    by_id = {b["beat_id"]: b for b in sheet["beats"]}
    for stem, total, segs, beats in plan:
        for (s, e), b in zip(segs, beats):
            bid = b["beat_id"]
            lo = max(0.0, s - a.pad_in)
            hi = min(total, e + a.pad_out)
            out = folder / "mp3" / f"beat-{bid}.mp3"
            subprocess.run([FFMPEG, "-y", "-v", "error", "-ss", f"{lo:.3f}",
                            "-to", f"{hi:.3f}", "-i", str(stem), "-vn",
                            "-c:a", "libmp3lame", "-q:a", "2", str(out)],
                           check=True)
            dur = media_duration(out)
            beat = by_id[bid]
            beat["audio_file"] = f"mp3/beat-{bid}.mp3"
            beat["actual_duration_s"] = round(dur, 2)
            timings[bid] = round(dur, 2)
            print(f"[suno] beat-{bid}.mp3  {dur:.2f}s  (stem {stem.name} "
                  f"{lo:.2f}→{hi:.2f})")
    sheet_path.write_text(json.dumps(sheet, indent=1, ensure_ascii=False))
    timings_path.write_text(json.dumps(timings, indent=1))
    print(f"[suno] beat_sheet.json + mp3/timings.json updated — durations are "
          f"GROUND TRUTH, same as generate_audio.py")
    print(f"[suno] next: ./art run {folder.name}  (the rest of the pipeline is "
          f"identical either voice engine)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

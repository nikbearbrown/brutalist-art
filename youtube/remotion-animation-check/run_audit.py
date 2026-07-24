#!/usr/bin/env python3
"""
run_audit.py — Walk all books/ beat_sheet.json files (sorted, deterministic),
find missing media beats in vox-format sheets, classify each, and build one
audit deck per 15 missing beats in this directory.

Resumable: skips any deck folder that already has deck.html.

Usage:
  python3 brutalist-art/youtube/remotion-animation-check/run_audit.py
"""

import json
import os
import re
import shutil
import struct
import subprocess
import sys
import wave
from datetime import datetime
from pathlib import Path

# ── Paths ─────────────────────────────────────────────────────────────────────
OUT_DIR = Path(__file__).resolve().parent         # remotion-animation-check/
BOOKS   = OUT_DIR.parents[2]                      # books/
BUILD_DECK = BOOKS / "brutalist-art/runtime/scripts/build_deck.py"
DECK_SIZE  = 15

# ── Pattern inference ─────────────────────────────────────────────────────────
PATTERN_KEYWORDS = {
    "scaleComparison": [
        "larger", "smaller", "size", "scale", "magnitude", "bigger",
        "times larger", "compare", "nanometer", "micron", "μm", "nm",
        "percent", "ten times", "hundred times", "order of magnitude",
    ],
    "attritionChain": [
        "reduces", "shrinks", "stage", "filter", "loss", "cascade",
        "pipeline", "fewer", "drops", "clinical trial", "survival",
        "mortality", "patients who", "from.*to.*patients",
        "end up", "remain", "only.*percent",
    ],
    "threshold": [
        "exceed", "crosses", "above", "below the limit", "trigger",
        "threshold", "critical", "enough to", "reaches the level",
        "concentration", "toxic", "lethal", "effective dose",
        "cut.?off", "passes the",
    ],
    "binaryBranch": [
        "either", " or ", "two options", "choice", "decide",
        "resolves", "determines whether", "success or failure",
        "yes or no", "measured or not", "known or unknown",
        "pass or fail",
    ],
    "divergentFates": [
        "same.*but", "identical.*different", "split into", "diverge",
        "two paths", "one group.*other group", "treatment.*control",
        "healthy.*disease", "both start", "then diverge",
    ],
    "calloutTour": [
        "this diagram", "this figure", "this image", "annotate",
        "points to", "label", "indicate", "here we see", "look at",
        "each part", "the components", "broken down into",
        "wheel", "boxes", "verdict", "fact.?check", "map", "chart",
        "table", "the real", "filed as", "shows", "architecture",
        "overview", "layout", "structure", "breakdown",
    ],
}


def infer_pattern(narration: str) -> str:
    n = narration.lower()
    scores = {}
    for pattern, keywords in PATTERN_KEYWORDS.items():
        score = sum(1 for kw in keywords if re.search(kw, n))
        if score > 0:
            scores[pattern] = score
    if not scores:
        return "static - no pattern fits"
    return max(scores, key=scores.get)


def pattern_what_it_shows(pattern: str) -> str:
    return {
        "calloutTour":     "a labeled diagram walking through key components",
        "binaryBranch":    "two diverging paths from a single decision point",
        "divergentFates":  "the same starting state splitting into different outcomes",
        "scaleComparison": "objects or quantities compared on a shared scale axis",
        "attritionChain":  "a population or quantity shrinking through sequential stages",
        "threshold":       "a value approaching and crossing a critical numeric limit",
        "static - no pattern fits": "a static title card or plain text slide",
    }.get(pattern, "an appropriate visualization")


# ── Missing-beat detection ────────────────────────────────────────────────────

def beat_missing_path(beat: dict, folder: Path):
    """Return the expected media path if the beat is missing, else None."""
    if not isinstance(beat, dict):
        return None
    shot = beat.get("shot")
    if not isinstance(shot, dict):
        return None

    # remotion rendered.out
    rem = shot.get("remotion")
    if isinstance(rem, dict):
        ren = rem.get("rendered")
        if isinstance(ren, dict):
            out = ren.get("out", "")
            if out and not (folder / out).exists():
                return folder / out

    # slot (own / archive / ai)
    slot = shot.get("slot", "")
    if slot and not (folder / slot).exists():
        return folder / slot

    return None


def classify(beat: dict) -> tuple:
    """Returns (verdict, pattern_or_source, asset_note)."""
    shot   = beat.get("shot", {}) if isinstance(beat.get("shot"), dict) else {}
    source = shot.get("source", "unknown")
    narr   = (beat.get("narration_text") or "").strip()
    note   = shot.get("note", "")

    if source == "remotion":
        pattern = infer_pattern(narr)
        desc    = f"{pattern} — {narr[:100].rstrip()}{'...' if len(narr) > 100 else ''}"
        return "NEEDS-VISUAL", pattern, desc
    else:
        if note:
            asset = note.split("—")[-1].strip()[:120]
        elif source in ("own", "archive"):
            asset = f"{source} media slot — {narr[:80].rstrip()}..."
        else:
            asset = f"real-world asset ({source}) — {narr[:80].rstrip()}..."
        return "LEGIT-SKIP", source, asset


# ── Segment builder ───────────────────────────────────────────────────────────

def make_segment(idx: int, total: int, rec: dict) -> dict:
    reel_slug = rec["reel_slug"]
    beat_id   = rec["beat_id"]
    verdict   = rec["verdict"]
    pattern   = rec["pattern"]
    narr      = rec["narration"]
    asset     = rec.get("asset", "")

    sid = f"S{idx:02d}"

    title = [[f"{reel_slug} — ", False], [beat_id, True]]

    if verdict == "NEEDS-VISUAL":
        wire_label = f"NEEDS-VISUAL → {pattern}"
        wire_body  = f"Should show: {pattern_what_it_shows(pattern)}"
        narration  = (
            f"Beat {beat_id} in reel {reel_slug} is missing its Remotion animation. "
            f"The concept — {narr[:180].rstrip()}. "
            f"Rhetorical shape points to {pattern}: this slot should show "
            f"{pattern_what_it_shows(pattern)}."
        )
    else:
        wire_label = f"LEGIT-SKIP → {pattern}"
        wire_body  = f"Waiting on: {asset[:120]}"
        narration  = (
            f"Beat {beat_id} in reel {reel_slug} is a legitimate skip. "
            f"The pipeline cannot generate this — it needs {asset[:160].rstrip()}. "
            f"The narration concept is: {narr[:120].rstrip()}."
        )

    body_html = (
        f'<div class="stack">'
        f'<div class="wire"><b>{wire_label}</b><span>{wire_body}</span></div>'
        f'<p class="lead">{narr[:180].rstrip()}{"..." if len(narr) > 180 else ""}</p>'
        f'</div>'
    )

    return {
        "id": sid,
        "num": idx,
        "total": total,
        "section": verdict,
        "label": f"{idx:02d} / {total:02d} · {verdict}",
        "dark": False,
        "title": title,
        "body_html": body_html,
        "beats": [{"type": "analytic", "text": narration}],
    }


# ── Kokoro audio (inline — same logic as make_audio_kokoro.py) ─────────────────

FFMPEG  = shutil.which("ffmpeg")  or "ffmpeg"
FFPROBE = shutil.which("ffprobe") or "ffprobe"
VOICE   = "am_onyx"


def _model_paths():
    env_m = os.environ.get("KOKORO_MODEL")
    env_v = os.environ.get("KOKORO_VOICES")
    if env_m and env_v:
        return Path(env_m), Path(env_v)
    art_home = os.environ.get("ART_HOME")
    roots = ([Path(art_home)] if art_home else []) + list(Path(__file__).resolve().parents)
    for root in roots:
        cand = root / "brutalist-art" / "runtime" / "models" / "kokoro"
        m = cand / "kokoro-v1.0.onnx"
        v = cand / "voices-v1.0.bin"
        if m.exists() and v.exists():
            return m, v
    return None, None


def _write_mp3(samples, sr, out: Path):
    tmp = out.with_suffix(".tmp.wav")
    ints = [max(-32768, min(32767, int(s * 32767))) for s in samples]
    with wave.open(str(tmp), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes(struct.pack(f"<{len(ints)}h", *ints))
    subprocess.run([FFMPEG, "-y", "-v", "error", "-i", str(tmp),
                    "-c:a", "libmp3lame", "-q:a", "2", str(out)], check=True)
    tmp.unlink()


def generate_audio(deck_dir: Path, segs: list) -> bool:
    """Generate audio/Snn.mp3 for each segment. Returns True on success."""
    m, v = _model_paths()
    if not (m and v):
        print("[audio] kokoro model files not found — skipping audio (deck will be silent)")
        return False
    try:
        from kokoro_onnx import Kokoro
    except ImportError:
        print("[audio] pip install kokoro-onnx — skipping audio")
        return False

    k = Kokoro(str(m), str(v))
    adir = deck_dir / "audio"
    adir.mkdir(exist_ok=True)

    for seg in segs:
        sid  = seg["id"]
        text = seg["beats"][0]["text"]
        out  = adir / f"{sid}.mp3"
        if out.exists():
            continue
        try:
            samples, sr = k.create(text, voice=VOICE, speed=1.0, lang="en-us")
            _write_mp3(samples, sr, out)
            print(f"  [audio] {out.name}")
        except Exception as e:
            print(f"  [audio] {sid} failed: {e}")
    return True


# ── Deck builder ──────────────────────────────────────────────────────────────

def build_deck(deck_dir: Path, segs: list, batch_num: int) -> bool:
    """Write beat_sheet.json, generate audio, run build_deck.py."""
    n    = len(segs)
    slug = f"audit-{batch_num:04d}"

    sheet = {
        "slug":   slug,
        "title":  f"Remotion Animation Audit — {batch_num:04d}",
        "series": "Media Audit",
        "source": f"audit/{batch_num:02d}",
        "metadata": {
            "chapter":        batch_num,
            "total_chapters": 999,
            "playlist":       "Media Audit",
            "palette":        "medhavy",
            "engine":         "kokoro",
            "voice_kokoro":   VOICE,
        },
        "segments": segs,
    }

    bs_path = deck_dir / "beat_sheet.json"
    bs_path.write_text(json.dumps(sheet, indent=2, ensure_ascii=False))
    print(f"[deck] beat_sheet.json written — {n} segments")

    generate_audio(deck_dir, segs)

    result = subprocess.run(
        [sys.executable, str(BUILD_DECK), str(deck_dir)],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        print(f"[deck] build_deck.py FAILED:\n{result.stdout}\n{result.stderr}")
        return False
    print(f"[deck] {result.stdout.strip()}")
    return True


# ── CHECK-LOG writer ──────────────────────────────────────────────────────────

def append_log(batch_num: int, records: list, deck_dir: Path, ok: bool):
    log = OUT_DIR / "CHECK-LOG.md"
    nv  = sum(1 for r in records if r["verdict"] == "NEEDS-VISUAL")
    nl  = sum(1 for r in records if r["verdict"] == "LEGIT-SKIP")
    ids = ", ".join(f"{r['reel_slug']}:{r['beat_id']}" for r in records)
    tag = "OK" if ok else "BUILD-FAILED"
    line = (f"- {batch_num:04d} [{tag}] — {len(records)} beats "
            f"(NEEDS-VISUAL {nv}, LEGIT-SKIP {nl}) — {ids} — "
            f"`open {deck_dir}/deck.html`\n")
    with log.open("a") as f:
        f.write(line)


# ── Main walk ─────────────────────────────────────────────────────────────────

def walk_missing():
    """Yield missing-beat records in sorted path order."""
    for bs in sorted(BOOKS.rglob("beat_sheet.json")):
        # Skip decks inside the audit output itself
        if OUT_DIR in bs.parents:
            continue
        try:
            d = json.loads(bs.read_text())
        except Exception:
            continue

        beats = d.get("beats")
        if not beats or not isinstance(beats, list):
            continue  # segments-format lecture — no media slots

        folder    = bs.parent
        reel_slug = d.get("metadata", {}).get("slug") or d.get("slug") or folder.name

        for beat in beats:
            if not isinstance(beat, dict):
                continue
            if beat_missing_path(beat, folder) is None:
                continue

            bid   = beat.get("beat_id", "?")
            narr  = (beat.get("narration_text") or "").strip()
            shot  = beat.get("shot", {}) if isinstance(beat.get("shot"), dict) else {}
            anim  = {}
            if isinstance(shot.get("remotion"), dict):
                anim = shot["remotion"]

            verdict, pattern, asset = classify(beat)

            yield {
                "reel_path":  str(bs.parent),
                "reel_slug":  reel_slug,
                "beat_id":    bid,
                "narration":  narr,
                "verdict":    verdict,
                "pattern":    pattern,
                "asset":      asset,
                "intended_pattern": anim.get("pattern", ""),
                "shot_source": shot.get("source", ""),
            }


def main():
    print(f"[audit] BOOKS = {BOOKS}")
    print(f"[audit] OUT   = {OUT_DIR}")
    print(f"[audit] started {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Initialise log header once
    log_path = OUT_DIR / "CHECK-LOG.md"
    if not log_path.exists():
        log_path.write_text(
            f"# Remotion Animation Audit — CHECK-LOG\n"
            f"Generated {datetime.now().strftime('%Y-%m-%d')}\n\n"
        )

    all_records = []   # global ordered list of all missing beats

    batch     = []     # current 15-beat window
    batch_num = 0      # 0015, 0030, …

    def flush_batch(records: list, num: int):
        tag  = f"{num * DECK_SIZE:04d}"
        ddir = OUT_DIR / tag

        if (ddir / "deck.html").exists():
            print(f"[audit] {tag}/ already has deck.html — skip")
            return

        ddir.mkdir(exist_ok=True)
        segs = [make_segment(i + 1, len(records), r) for i, r in enumerate(records)]
        ok   = build_deck(ddir, segs, num * DECK_SIZE)
        append_log(num * DECK_SIZE, records, ddir, ok)
        print(f"[audit] deck {tag} {'DONE' if ok else 'FAILED (logged)'}")

    for rec in walk_missing():
        all_records.append(rec)
        batch.append(rec)

        if len(batch) == DECK_SIZE:
            batch_num += 1
            flush_batch(batch, batch_num)
            batch = []

    # flush remaining < 15
    if batch:
        batch_num += 1
        flush_batch(batch, batch_num)

    total     = len(all_records)
    n_decks   = batch_num
    n_vis     = sum(1 for r in all_records if r["verdict"] == "NEEDS-VISUAL")
    n_skip    = sum(1 for r in all_records if r["verdict"] == "LEGIT-SKIP")

    # pattern histogram
    hist = {}
    for r in all_records:
        if r["verdict"] == "NEEDS-VISUAL":
            hist[r["pattern"]] = hist.get(r["pattern"], 0) + 1

    # top reels by missing count
    reel_counts = {}
    for r in all_records:
        reel_counts[r["reel_slug"]] = reel_counts.get(r["reel_slug"], 0) + 1
    top_reels = sorted(reel_counts.items(), key=lambda x: -x[1])[:20]

    # deck builder success rate
    log_lines = log_path.read_text().splitlines()
    failed = sum(1 for l in log_lines if "BUILD-FAILED" in l)
    ok_cnt = n_decks - failed

    report = f"""# Remotion Animation Audit — CHECK-REPORT
Generated {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Summary
- **Total missing beats**: {total}
- **Decks built**: {n_decks}  (every {DECK_SIZE} beats)
- **NEEDS-VISUAL**: {n_vis}
- **LEGIT-SKIP**: {n_skip}

## Deck builder health
- OK: {ok_cnt} / {n_decks}
- FAILED: {failed} (see CHECK-LOG.md for details)

## Top reels by missing-beat count (top 20)
| Reel slug | Missing beats |
|---|---|
""" + "".join(f"| {slug} | {cnt} |\n" for slug, cnt in top_reels) + """
## Pattern-need histogram (NEEDS-VISUAL only)
| Pattern | Count |
|---|---|
""" + "".join(f"| {p} | {c} |\n" for p, c in sorted(hist.items(), key=lambda x: -x[1])) + f"""
## Notes on deck builder
The deck builder (`build_deck.py`) produced {ok_cnt}/{n_decks} successful decks.
{"All decks built cleanly." if failed == 0 else f"{failed} deck(s) failed — check CHECK-LOG.md for per-deck errors."}
Audio was generated via Kokoro (am_onyx, free/local).
"""

    (OUT_DIR / "CHECK-REPORT.md").write_text(report)
    print(f"\n[audit] DONE — {total} missing beats · {n_decks} decks · "
          f"NEEDS-VISUAL {n_vis} · LEGIT-SKIP {n_skip}")
    print(f"[audit] Report: {OUT_DIR}/CHECK-REPORT.md")


if __name__ == "__main__":
    main()

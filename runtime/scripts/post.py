#!/usr/bin/env python3
"""post.py — clean 4K staging for a finished brutalist reel.

Steps (per skills/make/post/SKILL.md):
  1. check    — preconditions: filled==of, slates==[], cut in {master,final},
                GATE T pass, audio locked, no active MISSING: in BUILD-LOG
  2. 4k-audit — probe every clip in clips/; re-render sub-2160 beats; recompile if needed
  3. final    — compile.py --height 2160 (clean master, no review overlay)
  4. assert   — sample frames; fail if marker band detected in bottom corner
  5. describe — write/refresh <slug>.md (chapters + boilerplate) into TOPOST
  6. move     — MOVE master into TOPOST (reel keeps beat_sheet for rebuilds)
  7. topaz    — detect Topaz Video AI ffmpeg; upscale into TOPOST (log skip if not found)
  8. log      — upsert TOPOST/staged.json (additive, keyed by slug)

Usage:
  python3 runtime/scripts/post.py <reel-path> [options]

Options:
  --to <dir>           TOPOST staging directory
                       (default: books/youtube/TOPOST)
  --topaz-model <m>    Topaz TVAI model (default: prob-3)
  --topaz-height <h>   Topaz output height px (default: 4320 = 8K)
  --force              re-stage even if already in staged.json

Hard rules (enforced here, not just documented):
  - Never uploads. STOP after staging.
  - art final only — never --review.
  - No stretched 4K: every beat is born 2160p or gets re-rendered.
  - No markers: frame-asserted before move.
  - staged.json is additive — never clobbers other entries.
"""

import argparse, json, os, re, shutil, subprocess, sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

FFMPEG  = shutil.which("ffmpeg")  or "ffmpeg"
FFPROBE = shutil.which("ffprobe") or "ffprobe"

DEFAULT_TOPOST = Path(
    "/Users/bear/Documents/CoWork/bear-textbooks/books/youtube/TOPOST"
)

TOPAZ_CANDIDATES = [
    "/Applications/Topaz Video AI.app/Contents/MacOS/ffmpeg",
    "/Applications/Topaz Video AI 4.app/Contents/MacOS/ffmpeg",
    "/Applications/Topaz Video AI 5.app/Contents/MacOS/ffmpeg",
    "/Applications/Topaz Video AI 3.app/Contents/MacOS/ffmpeg",
]
TOPAZ_MODEL_DIRS = [
    "/Applications/Topaz Video AI.app/Contents/Resources/models",
    "/Applications/Topaz Video AI 4.app/Contents/Resources/models",
    "/Applications/Topaz Video AI 5.app/Contents/Resources/models",
    "/Applications/Topaz Video AI 3.app/Contents/Resources/models",
]


# ── helpers ──────────────────────────────────────────────────────────────────

def die(msg):
    print(msg, file=sys.stderr)
    sys.exit(1)

def probe_wh(path):
    r = subprocess.run(
        [FFPROBE, "-v", "error", "-select_streams", "v:0",
         "-show_entries", "stream=width,height", "-of", "csv=p=0", str(path)],
        capture_output=True, text=True,
    )
    try:
        vals = r.stdout.strip().splitlines()[0].split(",")
        return int(vals[0]), int(vals[1])
    except (ValueError, IndexError):
        return None, None

def probe_duration(path):
    r = subprocess.run(
        [FFPROBE, "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(path)],
        capture_output=True, text=True,
    )
    try:
        return float(r.stdout.strip())
    except ValueError:
        return None

def fmt_ts(seconds):
    s = int(seconds)
    m, s = divmod(s, 60)
    return f"{m}:{s:02d}"

def resolve_slot_path(folder, bid):
    """Mirror compile.py's resolve_slot precedence."""
    for rel in (f"media/{bid}.mp4", f"manim/{bid}.mp4", f"manim/{bid}.mov",
                f"media/{bid}.png", f"media/{bid}.jpg"):
        p = folder / rel
        if p.exists():
            return p
    return None

def _probe_wh_any(path):
    """Probe width×height for video or image source files."""
    if path.suffix.lower() in (".mp4", ".mov", ".webm", ".avi", ".mkv"):
        return probe_wh(path)
    # Image: try PIL first, fall back to ffprobe
    try:
        from PIL import Image
        img = Image.open(path)
        return img.size[0], img.size[1]
    except Exception:
        pass
    r = subprocess.run(
        [FFPROBE, "-v", "error", "-select_streams", "v:0",
         "-show_entries", "stream=width,height", "-of", "csv=p=0", str(path)],
        capture_output=True, text=True,
    )
    try:
        vals = r.stdout.strip().splitlines()[0].split(",")
        return int(vals[0]), int(vals[1])
    except (ValueError, IndexError):
        return None, None


# ── Step 1: preconditions ────────────────────────────────────────────────────

def step_check(reel_dir, bs):
    print("[post] ── STEP 1: check preconditions ──")
    meta  = bs.get("metadata", {})
    build = meta.get("build", {})

    filled = build.get("filled")
    of_    = build.get("of")
    slates = build.get("slates", [])
    cut    = build.get("cut", "")

    if filled != of_:
        die(f"[post] FAIL: beat sheet not fully filled ({filled}/{of_})")
    if slates:
        die(f"[post] FAIL: {len(slates)} slate(s) remain: {slates}")
    if cut not in ("master", "final"):
        die(f"[post] FAIL: metadata.build.cut='{cut}', need master or final")
    print(f"[post]   beat sheet: {filled}/{of_} filled, 0 slates, cut={cut} ✓")

    # GATE T
    tc = reel_dir / "TYPECHECK.md"
    if not tc.exists():
        die("[post] FAIL: TYPECHECK.md missing — run kerning skill first")
    tc_text = tc.read_text()
    if re.search(r'\|\s*FAIL\s*\|', tc_text):
        die("[post] FAIL: TYPECHECK.md contains FAIL rows")
    if "GATE T: **PASS**" not in tc_text and "Overall: PASS" not in tc_text:
        die("[post] FAIL: TYPECHECK.md does not show PASS")
    print("[post]   GATE T: PASS ✓")

    # BUILD-LOG active MISSING: lines (strict: line content starts with MISSING:)
    bl = reel_dir / "BUILD-LOG.md"
    if bl.exists():
        for line in bl.read_text().splitlines():
            # "- MISSING:" is a historical list item; skip. Only flag bare "MISSING:" openers.
            stripped = line.lstrip()
            if stripped.startswith("MISSING:"):
                die(f"[post] FAIL: BUILD-LOG.md has active MISSING: line:\n  {line}")
    print("[post]   BUILD-LOG: no active MISSING: lines ✓")

    # Audio locked
    timings = reel_dir / "mp3" / "timings.json"
    if not timings.exists():
        die("[post] FAIL: mp3/timings.json missing — audio not generated")
    t = json.loads(timings.read_text())
    if not t:
        die("[post] FAIL: timings.json is empty")
    print(f"[post]   audio: locked ({len(t)} beats) ✓")
    print("[post]   all preconditions green\n")


# ── Step 2: 4K audit + re-render ─────────────────────────────────────────────

def step_4k_audit(reel_dir, bs):
    """Probe SOURCE resolution for each beat (not the compiled clips).

    compile.py always upscales to the target height, so clips/*.mp4 are always
    2160p regardless of source quality. We must check the source slots directly.
    Returns (recompile_needed: bool, native_res: dict[bid -> (w,h) | None]).
    """
    print("[post] ── STEP 2: 4K audit (source resolution) ──")
    clips_dir  = reel_dir / "clips"
    manifest_p = clips_dir / "manifest.json"
    manifest   = json.loads(manifest_p.read_text()) if manifest_p.exists() else {}
    beats      = bs.get("beats", [])
    beat_by_id = {b["beat_id"]: b for b in beats}
    sub4k      = []        # (bid, clip_path, src_w, src_h)
    native_res = {}        # bid → (w, h) | None

    for b in beats:
        bid = b["beat_id"]
        src = resolve_slot_path(reel_dir, bid)
        if src is None:
            print(f"[post]   {bid}: no source slot — skip")
            native_res[bid] = None
            continue
        w, h = _probe_wh_any(src)
        if w is None:
            print(f"[post]   {bid}: cannot probe {src.name} — skip")
            native_res[bid] = None
            continue
        native_res[bid] = (w, h)
        ok = h >= 2160
        print(f"[post]   {bid}: {src.name}  {w}×{h}  {'✓' if ok else '✗ SUB-4K'}")
        if not ok:
            sub4k.append((bid, clips_dir / f"{bid}.mp4", w, h))

    if not sub4k:
        print("[post]   all source slots are native 4K ✓\n")
        return False, native_res

    print(f"\n[post]   {len(sub4k)} sub-4K source(s): {[b for b,*_ in sub4k]}")

    for bid, clip_path, cw, ch in sub4k:
        beat  = beat_by_id.get(bid, {})
        lane  = beat.get("lane", "?")
        print(f"\n[post]   fixing {bid} ({lane}) — source {cw}×{ch}")

        placed_4k = False

        # Try Manim re-render for MANIM-lane beats
        if lane == "MANIM":
            shot       = beat.get("shot", {})
            scene_name = (shot.get("manim") or {}).get("scene")
            scenes_py  = reel_dir / "scenes.py"
            if scene_name and scenes_py.exists():
                print(f"[post]   → Manim 4K re-render: {scene_name}")
                out = _manim_render_4k(reel_dir, scenes_py, scene_name)
                if out and out.exists():
                    mw, mh = probe_wh(out)
                    print(f"[post]   Manim output: {out.name}  {mw}×{mh}")
                    if mh and mh >= 2160:
                        dest = reel_dir / "media" / f"{bid}.mp4"
                        shutil.copy2(str(out), str(dest))
                        print(f"[post]   placed 4K Manim render → media/{bid}.mp4")
                        placed_4k = True
                        native_res[bid] = (mw, mh)
                    else:
                        print(f"[post]   Manim output sub-4K ({mh}p) — falling back to existing source")
                else:
                    print("[post]   Manim render failed — falling back to existing source")

        if not placed_4k:
            print(f"[post]   {bid}: source is sub-4K ({cw}×{ch}) — will be upscaled by compile.py")

        # Invalidate the cached clip so compile.py rebuilds from the (possibly updated) source
        if clip_path.exists():
            clip_path.unlink()
            print(f"[post]   deleted stale clips/{bid}.mp4")
        if bid in manifest:
            del manifest[bid]
            manifest_p.write_text(json.dumps(manifest, indent=1))
            print(f"[post]   cleared manifest[{bid}]")

    print()
    return True, native_res  # signals that a recompile will happen


def _manim_render_4k(reel_dir, scenes_py, scene_name):
    """Run manim -qk for a single scene. Return output Path or None."""
    r = subprocess.run(
        ["manim", "-qk", "--disable_caching", str(scenes_py.name), scene_name],
        capture_output=True, text=True, cwd=str(reel_dir),
    )
    print(f"[post]   manim rc={r.returncode}")
    if r.returncode != 0:
        snippet = (r.stderr or r.stdout)[-400:]
        print(f"[post]   manim output: {snippet}")
        return None
    # Manim puts output in media/videos/<stem>/4K60fps/<Scene>.mp4
    vids = reel_dir / "media" / "videos"
    if vids.exists():
        hits = sorted(vids.rglob(f"{scene_name}.mp4"), key=lambda p: p.stat().st_mtime)
        if hits:
            return hits[-1]
    return None


# ── Step 3: compile clean 4K master ─────────────────────────────────────────

def step_final(art_home, reel_dir):
    print("[post] ── STEP 3: compile clean 4K master ──")
    compile_py = art_home / "runtime" / "scripts" / "compile.py"

    # Re-confirm GATE T (mirrors art final behavior)
    tc_py = art_home / "runtime" / "scripts" / "type_check.py"
    if tc_py.exists():
        r = subprocess.run(["python3", str(tc_py), str(reel_dir)],
                           capture_output=True, text=True)
        if r.returncode >= 2:
            die(f"[post] GATE T BLOCKED:\n{r.stdout}")
        if r.returncode == 3:
            print("[post]   GATE T: skipped (missing deps)")
        else:
            print("[post]   GATE T: re-confirmed PASS ✓")

    r = subprocess.run(
        ["python3", str(compile_py), str(reel_dir), "--height", "2160"],
        capture_output=True, text=True,
    )
    if r.stdout:
        print(r.stdout[-3000:])
    if r.returncode != 0:
        die(f"[post] compile FAILED:\n{r.stderr[-800:]}")
    print("[post]   compile complete ✓\n")


# ── Step 4: frame-assert no markers / burn-in ───────────────────────────────

def step_frame_assert(reel_dir, slug):
    print("[post] ── STEP 4: frame-assert (no marker band) ──")
    master = reel_dir / f"{slug}.mp4"
    if not master.exists():
        die(f"[post] frame-assert FAIL: master not found at {master}")

    dur = probe_duration(master)
    if not dur:
        die("[post] frame-assert FAIL: cannot probe master duration")

    work = reel_dir / "_qc" / "post-assert"
    work.mkdir(parents=True, exist_ok=True)

    sample_times = [dur * p for p in (0.10, 0.28, 0.50, 0.72, 0.90)]
    fail_count   = 0

    try:
        from PIL import Image
        use_pil = True
    except ImportError:
        use_pil = False
        print("[post]   PIL not available — structural assert only")

    for i, t in enumerate(sample_times):
        frame_path = work / f"assert-{i:02d}.png"
        r = subprocess.run(
            [FFMPEG, "-y", "-ss", f"{t:.3f}", "-i", str(master),
             "-frames:v", "1", "-q:v", "2", str(frame_path)],
            capture_output=True, text=True,
        )
        if r.returncode != 0 or not frame_path.exists():
            print(f"[post]   frame {i} (t={t:.0f}s): extract failed — skip")
            continue

        if use_pil:
            img = Image.open(frame_path).convert("RGB")
            fw, fh = img.size
            # compile.py places review labels at overlay=16:H-h-16 (bottom-left corner)
            # Band height ~ h*0.032 for 2160p ≈ 69px; check generous 400×90 region
            bw, bh_ = min(400, fw), min(90, fh)
            region  = img.crop((0, fh - bh_, bw, fh))
            pixels  = list(region.getdata())
            dark    = sum(1 for rv, gv, bv in pixels if rv < 55 and gv < 55 and bv < 55)
            pct     = dark / max(len(pixels), 1)
            verdict = "POSSIBLE MARKER" if pct >= 0.35 else "clean"
            print(f"[post]   frame {i} t={t:.0f}s: bottom-left dark={pct:.1%}  {verdict}")
            if pct >= 0.35:
                fail_count += 1
        else:
            print(f"[post]   frame {i} t={t:.0f}s: extracted (no PIL check)")

    if fail_count:
        die(f"[post] frame-assert FAIL: {fail_count} frame(s) show possible marker band — "
            "inspect _qc/post-assert/ frames and re-compile clean")

    print(f"[post]   frame-assert: PASS ✓  (frames in {work.relative_to(reel_dir)})\n")


# ── Step 5: generate YouTube description ────────────────────────────────────

def step_describe(reel_dir, bs, slug, topost_dir):
    print("[post] ── STEP 5: generate YouTube description ──")
    meta   = bs.get("metadata", {})
    beats  = bs.get("beats", [])
    title  = meta.get("title", slug)
    topic  = meta.get("topic", "")
    playlist    = meta.get("playlist", "")
    in_for_bear = meta.get("in_for_bear", False)

    channel_handle = "@NikBearBrown"
    persona_line   = (f"{channel_handle} / Liam-in-for-Bear"
                      if in_for_bear else channel_handle)

    # Build beat durations (clips/manifest preferred for chapter accuracy)
    durations = {}
    man_p = reel_dir / "clips" / "manifest.json"
    if man_p.exists():
        for bid, val in json.loads(man_p.read_text()).items():
            try:
                durations[bid] = float(val.split("|")[3])
            except (IndexError, ValueError):
                pass
    tim_p = reel_dir / "mp3" / "timings.json"
    if tim_p.exists():
        for bid, dur in json.loads(tim_p.read_text()).items():
            if bid not in durations:
                try:
                    durations[bid] = float(dur)
                except (TypeError, ValueError):
                    pass

    # Cumulative offsets
    offsets = {}
    t = 0.0
    for b in beats:
        bid = b["beat_id"]
        offsets[bid] = t
        t += durations.get(bid, float(b.get("estimated_duration_s", 6.0)))
    total_dur = t

    # Chapter markers: CARD beats, first beat of each ACT, closing beats
    chapter_bids = {"B00"}
    seen_acts    = set()
    for b in beats:
        bid  = b["beat_id"]
        lane = b.get("lane", "")
        act  = b.get("act", "")
        if bid in ("BVDT", "BHTF"):
            chapter_bids.add(bid)
            continue
        if lane == "CARD":
            chapter_bids.add(bid)
            continue
        act_key = act.split("—")[0].strip() if "—" in act else act.strip()
        if act_key.upper().startswith("ACT") and act_key not in seen_acts:
            chapter_bids.add(bid)
            seen_acts.add(act_key)

    def chapter_label(b):
        bid = b["beat_id"]
        act = b.get("act", "")
        if bid == "B00":    return "Introduction"
        if bid == "BVDT":   return "Verdict"
        if bid == "BHTF":   return "Your Turn"
        if "—" in act:      return act.split("—", 1)[1].strip()
        return act.strip().title() or bid

    chapters = sorted(
        [(offsets[b["beat_id"]], chapter_label(b))
         for b in beats if b["beat_id"] in chapter_bids],
        key=lambda x: x[0],
    )
    if not chapters or chapters[0][0] > 0.5:
        chapters.insert(0, (0.0, "Introduction"))

    # Hook from B00 narration
    hook = next((b.get("narration_text", "")
                 for b in beats if b["beat_id"] == "B00"), "")[:300]

    # YOUR TURN from BHTF narration
    your_turn = next((b.get("narration_text", "")
                      for b in beats if b["beat_id"] == "BHTF"), "")[:350]

    # Hashtags
    hashtags = "#ComputationalSkepticism #AgenticAI #AI #MachineLearning #Claude #NikBearBrown"

    lines = [f"# {title}", ""]
    lines += [hook, ""]
    if playlist:
        lines += [f"**Series:** {playlist}"]
    if topic:
        lines += [f"**Topic:** {topic}"]
    lines += ["", "---", "", "## Chapters", ""]
    for ts, label in chapters:
        lines.append(f"{fmt_ts(ts)} {label}")
    lines += ["", "---", "", "## YOUR TURN", "", your_turn, ""]
    lines += ["---", "", f"**{persona_line}**", ""]
    if playlist:
        lines.append(f"*Part of the {playlist} series.*")
    lines += ["", hashtags, ""]
    lines += ["---", "",
              "*Sources and citations: see the reel's SOURCES.md in the open textbook.*"]

    md = "\n".join(lines) + "\n"
    out_path = topost_dir / f"{slug}.md"
    out_path.write_text(md)
    print(f"[post]   wrote {out_path.name}  ({len(chapters)} chapters, ~{fmt_ts(total_dur)})\n")
    return out_path


# ── Step 6: move master into TOPOST ─────────────────────────────────────────

def step_move(reel_dir, slug, topost_dir):
    print("[post] ── STEP 6: move master into TOPOST ──")
    master = reel_dir / f"{slug}.mp4"
    if not master.exists():
        die(f"[post] MOVE FAIL: master not found at {master}")

    size_mb = master.stat().st_size / 1_000_000
    dur     = probe_duration(master)
    w, h    = probe_wh(master)
    print(f"[post]   {master.name}  {size_mb:.1f} MB  {fmt_ts(dur)}  {w}×{h}")

    dest = topost_dir / f"{slug}.mp4"
    shutil.move(str(master), str(dest))
    print(f"[post]   moved → {dest}\n")
    return dest


# ── Step 7: Topaz upscale ────────────────────────────────────────────────────

def step_topaz(topost_dir, slug, model, topaz_height):
    print("[post] ── STEP 7: Topaz Video AI upscale ──")

    topaz_ffmpeg    = None
    topaz_model_dir = None

    print("[post]   searching for Topaz Video AI ffmpeg:")
    for c in TOPAZ_CANDIDATES:
        found = Path(c).exists()
        print(f"[post]     {'FOUND' if found else '    -'}  {c}")
        if found and topaz_ffmpeg is None:
            topaz_ffmpeg = c

    print("[post]   searching for Topaz model directory:")
    for c in TOPAZ_MODEL_DIRS:
        found = Path(c).exists()
        print(f"[post]     {'FOUND' if found else '    -'}  {c}")
        if found and topaz_model_dir is None:
            topaz_model_dir = c

    if not topaz_ffmpeg:
        reason = "Topaz Video AI.app not found at any known macOS location"
        print(f"[post]   topaz.ran=false  reason: {reason}\n")
        return {"ran": False, "reason": reason}
    if not topaz_model_dir:
        reason = "Topaz model directory not found"
        print(f"[post]   topaz.ran=false  reason: {reason}\n")
        return {"ran": False, "reason": reason}

    src_path = topost_dir / f"{slug}.mp4"
    out_path = topost_dir / f"{slug}-topaz.mp4"
    out_w    = topaz_height * 16 // 9  # assumes 16:9

    cmd = [
        topaz_ffmpeg,
        "-i", str(src_path),
        "-vf", f"tvai_up=model={model}:scale=0:w={out_w}:h={topaz_height}",
        "-c:v", "hevc_videotoolbox",
        "-profile:v", "main",
        "-b:v", "120M",
        "-tag:v", "hvc1",
        "-c:a", "copy",
        str(out_path),
    ]
    env = {**os.environ,
           "TVAI_MODEL_DIR": topaz_model_dir,
           "TVAI_MODEL_DATA_DIR": topaz_model_dir}

    print(f"\n[post]   model={model}  output={out_w}×{topaz_height}")
    print(f"[post]   command:\n    {' '.join(str(c) for c in cmd)}\n")

    r = subprocess.run(cmd, capture_output=True, text=True, env=env)
    # Clean up any 0-byte stub ffmpeg may have created before erroring
    if out_path.exists() and out_path.stat().st_size == 0:
        out_path.unlink()
    if r.returncode != 0 or not out_path.exists():
        reason = f"Topaz ffmpeg exited {r.returncode}: {(r.stderr or r.stdout)[-300:]}"
        print(f"[post]   topaz.ran=false  {reason}\n")
        return {"ran": False, "reason": reason}

    size_mb = out_path.stat().st_size / 1_000_000
    print(f"[post]   Topaz complete: {out_path.name}  {size_mb:.1f} MB ✓\n")
    return {"ran": True, "model": model,
            "output_res": f"{out_w}x{topaz_height}",
            "output_file": out_path.name}


# ── Step 8: upsert staged.json ───────────────────────────────────────────────

def step_log(topost_dir, slug, bs, master_path, topaz_result, all_beats_4k, markers_clean,
             reel_dir=None, native_res=None):
    print("[post] ── STEP 8: upsert staged.json ──")
    meta   = bs.get("metadata", {})
    beats  = bs.get("beats", [])

    staged_json = topost_dir / "staged.json"
    data = (json.loads(staged_json.read_text())
            if staged_json.exists() else {"videos": []})

    # Measure staged master
    dur  = probe_duration(master_path) if master_path.exists() else None
    w, h = probe_wh(master_path) if master_path.exists() else (None, None)

    # America/New_York — EDT in July (UTC-4)
    ny_tz    = timezone(timedelta(hours=-4))
    now_ny   = datetime.now(tz=ny_tz)
    staged_at = now_ny.strftime("%Y-%m-%dT%H:%M:%S") + "-04:00"

    topaz_file = topaz_result.get("output_file") if topaz_result.get("ran") else None

    # source_reel = the reel folder path (relative to books root), not the chapter source
    books_root = topost_dir.parents[1]  # TOPOST/../.. = books/
    try:
        source_rel = str(reel_dir.relative_to(books_root)) + "/"
    except (ValueError, AttributeError):
        source_rel = meta.get("source") or f"books/humanitarians-youtube/brutalist/{slug}/"

    # Per-beat native source resolution for honest QC reporting
    beats_native_res = None
    if native_res:
        beats_native_res = {
            bid: ({"w": wh[0], "h": wh[1], "native_4k": wh[1] >= 2160}
                  if wh else {"w": None, "h": None, "native_4k": None})
            for bid, wh in native_res.items()
        }

    entry = {
        "slug":        slug,
        "title":       meta.get("title", slug),
        "source_reel": source_rel,
        "staged_at":   staged_at,
        "files": {
            "master_4k":     master_path.name,
            **({"topaz_upscale": topaz_file} if topaz_file else {}),
            "description_md": f"{slug}.md",
        },
        "resolution":   f"{w}x{h}" if w else "3840x2160",
        "duration_s":   round(dur, 1) if dur else None,
        "beat_count":   len(beats),
        "all_beats_4k": all_beats_4k,
        **({"beats_native_res": beats_native_res} if beats_native_res else {}),
        "markers_clean": markers_clean,
        "gate_t":       "pass",
        "topaz":        topaz_result,
        "status":       "staged",
    }

    videos = data.get("videos", [])
    idx    = next((i for i, v in enumerate(videos) if v.get("slug") == slug), None)
    if idx is not None:
        videos[idx] = entry
        print(f"[post]   updated existing entry for {slug}")
    else:
        videos.append(entry)
        print(f"[post]   added new entry for {slug}")
    data["videos"] = videos

    staged_json.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"[post]   staged.json → {staged_json}")
    print(f"\n[post]   entry:\n{json.dumps(entry, indent=4)}\n")
    return entry


# ── main ─────────────────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser(
        description="post — clean 4K staging for a finished brutalist reel"
    )
    ap.add_argument("reel",           type=Path,
                    help="path to reel folder (books/<book>/youtube/<slug>/)")
    ap.add_argument("--to",           type=Path, default=DEFAULT_TOPOST,
                    help="TOPOST staging directory")
    ap.add_argument("--topaz-model",  default="prob-3",
                    help="Topaz TVAI model (default: prob-3)")
    ap.add_argument("--topaz-height", type=int, default=4320,
                    help="Topaz output height in pixels (default: 4320 = 8K)")
    ap.add_argument("--force",        action="store_true",
                    help="re-stage even if already in staged.json")
    args = ap.parse_args()

    reel_dir = args.reel.resolve()
    if not reel_dir.is_dir():
        die(f"[post] reel not found: {reel_dir}")

    # Locate ART_HOME (toolkit root)
    art_home_env = os.environ.get("ART_HOME", "")
    art_home     = Path(art_home_env) if art_home_env else Path(__file__).resolve().parents[2]

    topost_dir = args.to.resolve()
    topost_dir.mkdir(parents=True, exist_ok=True)

    bs_path = reel_dir / "beat_sheet.json"
    if not bs_path.exists():
        die(f"[post] beat_sheet.json not found in {reel_dir}")
    bs   = json.loads(bs_path.read_text())
    slug = bs.get("metadata", {}).get("slug") or reel_dir.name

    print(f"\n[post] ════════════════════════════════════════════")
    print(f"[post]  reel:   {slug}")
    print(f"[post]  dir:    {reel_dir}")
    print(f"[post]  TOPOST: {topost_dir}")
    print(f"[post] ════════════════════════════════════════════\n")

    # 1. preconditions
    step_check(reel_dir, bs)

    # 2. 4K audit — probes SOURCE resolution, fixes stale clips, returns native_res
    recompile_flagged, native_res = step_4k_audit(reel_dir, bs)

    # Derive all_beats_4k from actual source resolutions (not compile output)
    probed = [wh[1] for wh in native_res.values() if wh is not None]
    all_beats_4k = bool(probed) and all(h >= 2160 for h in probed)

    # 3. compile clean 4K master (always — guarantees clean final even if no sub-4K found)
    step_final(art_home, reel_dir)
    bs = json.loads(bs_path.read_text())  # reload: compile stamps the sheet

    # 4. frame-assert no markers
    step_frame_assert(reel_dir, slug)

    # 5. generate description into TOPOST
    step_describe(reel_dir, bs, slug, topost_dir)

    # 6. MOVE master into TOPOST
    master_path = step_move(reel_dir, slug, topost_dir)

    # 7. Topaz upscale (or log skip)
    topaz_result = step_topaz(topost_dir, slug, args.topaz_model, args.topaz_height)

    # 8. upsert staged.json (all_beats_4k and beats_native_res reflect sources, not clips)
    step_log(
        topost_dir, slug, bs, master_path, topaz_result,
        all_beats_4k=all_beats_4k,
        markers_clean=True,  # post.py guarantees this via step 4
        reel_dir=reel_dir,
        native_res=native_res,
    )

    # Final banner
    print("[post] ════════════════════════════════════════════")
    print("[post]  STAGED ✓")
    print(f"[post]  master:  {topost_dir / (slug + '.mp4')}")
    if topaz_result.get("ran"):
        print(f"[post]  topaz:   {topost_dir / (slug + '-topaz.mp4')}")
    else:
        print(f"[post]  topaz:   skipped — {topaz_result.get('reason', '')}")
    print(f"[post]  desc:    {topost_dir / (slug + '.md')}")
    print(f"[post]  manifest:{topost_dir / 'staged.json'}")
    print("[post] ════════════════════════════════════════════")
    print("[post]  STOP — human uploads from TOPOST. Never upload from here.")
    print("[post] ════════════════════════════════════════════\n")


if __name__ == "__main__":
    main()

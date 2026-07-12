#!/usr/bin/env python3
"""teardown_rerender.py — Re-render all 22 nbb/ Manim beats in teardown palette.

Usage (from books/):
    python3 runtime/scripts/teardown_rerender.py <books_dir> <toolkit_dir>
    # or via the wrapper:
    bash runtime/scripts/teardown_rerender.sh

What it does for each nbb/ directory:
  1. Reads beat_sheet.json to find all manim-source beats
  2. Removes the symlink (or stale file) in nbb/manim/
  3. Renders from the parent reel's scenes.py with ART_PALETTE=teardown
  4. Recompiles with compile.py → nbb/<slug>-review.mp4 and nbb/mp4/
"""
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path


def log(msg: str) -> None:
    print(f"[nbb-rerender] {msg}", flush=True)


def find_manim_output(parent_dir: Path, scene_class: str) -> Path | None:
    """Find the assembled mp4 manim produces under media/videos/."""
    # manim -qh --fps 24 -r 1920,1080 scenes.py SceneClass
    # → media/videos/scenes/1080p24/SceneClass.mp4
    for candidate in parent_dir.rglob(f"{scene_class}.mp4"):
        if "partial_movie" not in str(candidate):
            return candidate
    # fallback: any mp4 matching the name
    for candidate in parent_dir.rglob(f"{scene_class}.mp4"):
        return candidate
    return None


def render_beat(parent_dir: Path, scene_class: str, dest: Path, toolkit_root: Path) -> bool:
    """Render one scene from parent's scenes.py with teardown palette."""
    scenes_py = parent_dir / "scenes.py"
    if not scenes_py.exists():
        log(f"  ERROR: no scenes.py in {parent_dir}")
        return False

    gfx_lib = toolkit_root / "manim"
    env = os.environ.copy()
    env["ART_PALETTE"] = "teardown"          # overrides setdefault("medhavy") in scenes.py
    env["PYTHONPATH"] = str(gfx_lib)

    log(f"  rendering {scene_class} → {dest.name}")
    result = subprocess.run(
        ["manim", "-qh", "--fps", "24", "-r", "1920,1080", "scenes.py", scene_class],
        cwd=parent_dir,
        env=env,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        log(f"  manim FAILED for {scene_class}:\n{result.stderr[-800:]}")
        return False

    out = find_manim_output(parent_dir, scene_class)
    if out is None:
        log(f"  ERROR: no output mp4 found for {scene_class} in {parent_dir}")
        return False

    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(out, dest)
    log(f"  slotted → {dest.relative_to(dest.parents[3])}")
    return True


def recompile_nbb(nbb_dir: Path, toolkit_root: Path) -> bool:
    """Run compile.py on the nbb/ directory."""
    compile_script = toolkit_root / "scripts/compile.py"
    log(f"  recompiling {nbb_dir.name}")
    result = subprocess.run(
        [sys.executable, str(compile_script), str(nbb_dir), "--review"],
        capture_output=False,   # stream compile output
    )
    if result.returncode != 0:
        log(f"  compile.py FAILED for {nbb_dir}")
        return False

    # copy review mp4 to mp4/ (mirrors what run.sh does)
    mp4_dir = nbb_dir / "mp4"
    mp4_dir.mkdir(exist_ok=True)
    for f in nbb_dir.glob("*.mp4"):
        shutil.copy2(f, mp4_dir / f.name)

    return True


def process_nbb(nbb_dir: Path, toolkit_root: Path) -> bool:
    parent_dir = nbb_dir.parent  # the medhavy reel dir

    bs_path = nbb_dir / "beat_sheet.json"
    if not bs_path.exists():
        log(f"  SKIP: no beat_sheet.json in {nbb_dir}")
        return True

    bs = json.loads(bs_path.read_text())
    manim_beats = [
        (b["beat_id"], b["shot"]["manim"]["scene_class"])
        for b in bs["beats"]
        if b["shot"].get("source") == "manim"
    ]

    if not manim_beats:
        log(f"  SKIP: no manim beats in {nbb_dir}")
        return True

    log(f"=== {parent_dir.name}/nbb — beats: {[bid for bid, _ in manim_beats]} ===")

    # Step 1: remove symlinks / stale files
    for bid, _ in manim_beats:
        dest = nbb_dir / "manim" / f"{bid}.mp4"
        if dest.is_symlink() or dest.exists():
            dest.unlink()
            log(f"  unlinked {bid}.mp4")

    # Step 2: render each beat
    for bid, scene_class in manim_beats:
        dest = nbb_dir / "manim" / f"{bid}.mp4"
        if not render_beat(parent_dir, scene_class, dest, toolkit_root):
            log(f"  ABORT: render failed for {bid} ({scene_class})")
            return False

    # Step 3: recompile
    return recompile_nbb(nbb_dir, toolkit_root)


def main() -> None:
    if len(sys.argv) < 3:
        sys.exit("Usage: teardown_rerender.py <books_dir> <toolkit_dir>")

    books_dir = Path(sys.argv[1]).resolve()
    toolkit_root = Path(sys.argv[2]).resolve()

    nbb_dirs = sorted(
        p for p in books_dir.rglob("nbb")
        if p.is_dir() and (p / "beat_sheet.json").exists()
        and "youtube" in str(p)
    )

    if not nbb_dirs:
        sys.exit(f"No nbb/ directories found under {books_dir}")

    log(f"Found {len(nbb_dirs)} nbb/ directories")

    failed = []
    for nbb_dir in nbb_dirs:
        try:
            ok = process_nbb(nbb_dir, toolkit_root)
        except Exception as exc:
            log(f"  EXCEPTION in {nbb_dir}: {exc}")
            ok = False
        if not ok:
            failed.append(nbb_dir)

    print()
    if not failed:
        log(f"All {len(nbb_dirs)} nbb reels re-rendered in teardown palette and recompiled.")
    else:
        log(f"Completed with {len(failed)} failure(s):")
        for f in failed:
            log(f"  {f}")
        sys.exit(1)


if __name__ == "__main__":
    main()

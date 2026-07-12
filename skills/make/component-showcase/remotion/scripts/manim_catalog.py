#!/usr/bin/env python3
"""manim_catalog.py — build a Brutalist riff that catalogs ONE Manim library.

Discovers Scene subclasses in a ManimCE repo, renders a sample to mp4 (low quality), stages
the clips into public/clips/manim/, and writes a clip beat sheet (same schema as the mp4 riff)
so RiffManim plays them under NBB narration + the brutalist outro. One library per video:
"Scene N of M — the <SceneName>."

ManimGL repos (`from manimlib import ...`) are NOT rendered by ManimCE. This skips GL-only
files and, if a library is entirely GL, refuses with a clear message (port it, or run a
separate ManimGL pass). Scenes that fail to render are skipped and logged — never faked.

Usage:
  python3 scripts/manim_catalog.py --lib ../manim/manim-fourier-series \
      --name "manim-fourier-series" --link github.com/taibeled/manim-fourier-series \
      --license MIT --max 8
  python3 scripts/manim_catalog.py --lib ../manim/manim-physics --discover-only   # list, no render
"""
import argparse, ast, json, re, shutil, subprocess, sys, tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]  # brutalist/remotion/
SKIP_DIRS = {"build", "dist", ".git", "__pycache__", "media", "node_modules", "tests", "test"}


def find_scenes(lib: Path):
    """[(pyfile, ClassName, base, docstring_first_line)] for ManimCE Scene subclasses only."""
    out = []
    for py in sorted(lib.rglob("*.py")):
        if any(p in SKIP_DIRS for p in py.parts):
            continue
        try:
            src = py.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        is_gl = bool(re.search(r"from\s+manimlib|import\s+manimlib", src))
        is_ce = bool(re.search(r"from\s+manim\b|import\s+manim\b", src))
        if is_gl and not is_ce:
            continue  # ManimGL-only file — not renderable by ManimCE
        try:
            tree = ast.parse(src)
        except Exception:
            continue
        for node in ast.walk(tree):
            if not isinstance(node, ast.ClassDef):
                continue
            # Must have construct() defined directly (not just inherited) — base classes render blank.
            has_construct = any(
                isinstance(item, ast.FunctionDef) and item.name == "construct"
                for item in node.body
            )
            if not has_construct:
                continue
            # Accept if any base contains "Scene", OR if the file imports manim and the class has
            # construct() — covers demo classes that inherit from library builder classes.
            base_names = [ast.unparse(b) if hasattr(ast, "unparse") else "" for b in node.bases]
            scene_by_base = any("Scene" in b for b in base_names)
            scene_by_file  = is_ce  # file imports from manim — any construct() class is renderable
            if not (scene_by_base or scene_by_file):
                continue
            base = ast.unparse(node.bases[0]) if node.bases else "Scene"
            doc = (ast.get_docstring(node) or "").strip().splitlines()
            out.append((py, node.name, base, doc[0] if doc else ""))
    return out


def _pkg_root_for(py: Path) -> Path | None:
    """Walk up from py until we find the top-most directory with __init__.py — that's the src root."""
    d = py.parent
    pkg_root = None
    while (d / "__init__.py").exists():
        pkg_root = d.parent
        d = d.parent
    return pkg_root  # None if file is not inside a package


def _has_relative_imports(py: Path) -> bool:
    src = py.read_text(encoding="utf-8", errors="ignore")
    return bool(re.search(r"^\s*from\s+\.+", src, re.MULTILINE))


def _make_wrapper(py: Path, cls: str, tmp_dir: Path) -> Path:
    """Create a flat wrapper file that exposes cls as a local subclass.

    Manim filters scenes by __module__, so a simple import isn't enough — we must define
    the class in the wrapper's own module via type(). Also handles sys.path so the package
    root is importable even when the package isn't installed."""
    pkg_root = _pkg_root_for(py)
    try:
        rel = py.relative_to(pkg_root)
        module = ".".join(rel.with_suffix("").parts)
    except (TypeError, ValueError):
        return py  # can't compute — fall back to original file
    wrapper = tmp_dir / f"_wrap_{cls}.py"
    sys_path_line = f"import sys; sys.path.insert(0, {str(pkg_root)!r})\n" if pkg_root else ""
    wrapper.write_text(
        f"{sys_path_line}"
        f"from {module} import {cls} as _Base\n"
        f"{cls} = type({cls!r}, (_Base,), {{}})\n"
    )
    return wrapper


def render_scene(py: Path, cls: str, media_dir: Path, timeout: int, wrap_dir: Path | None = None):
    """Render one scene with ManimCE at low quality. Returns (mp4_path | None, err | None)."""
    render_py = py
    if _has_relative_imports(py) and wrap_dir is not None:
        render_py = _make_wrapper(py, cls, wrap_dir)
    try:
        r = subprocess.run(
            ["manim", "-ql", "--media_dir", str(media_dir), str(render_py), cls],
            capture_output=True, text=True, timeout=timeout,
            cwd=str(render_py.parent))
    except subprocess.TimeoutExpired:
        return None, f"timeout after {timeout}s"
    except FileNotFoundError:
        sys.exit("[err] `manim` not on PATH — install ManimCE (pip install manim).")
    if r.returncode != 0:
        tail = (r.stderr or r.stdout or "").strip().splitlines()[-3:]
        return None, " | ".join(tail)[:300]
    hits = sorted(media_dir.rglob(f"{cls}.mp4"), key=lambda p: p.stat().st_mtime)
    if hits:
        return hits[-1], None
    # Static scene (0 animations) — manim writes a PNG instead. Convert to a 3-second mp4.
    imgs = sorted(media_dir.rglob(f"{cls}_*.png"), key=lambda p: p.stat().st_mtime)
    if not imgs:
        imgs = sorted(media_dir.rglob(f"*{cls}*.png"), key=lambda p: p.stat().st_mtime)
    if imgs:
        mp4_out = media_dir / f"{cls}.mp4"
        subprocess.run(
            ["ffmpeg", "-y", "-loop", "1", "-i", str(imgs[-1]),
             "-t", "3", "-vf", "scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2",
             "-c:v", "libx264", "-pix_fmt", "yuv420p", str(mp4_out)],
            capture_output=True, check=True)
        return mp4_out, None
    return None, "rendered but no mp4 found"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lib", required=True, type=Path, help="path to the Manim library repo")
    ap.add_argument("--name", default=None, help="display name (default: folder name)")
    ap.add_argument("--link", default="", help="repo URL for the credit")
    ap.add_argument("--license", default="", help="license for the credit")
    ap.add_argument("--max", type=int, default=8, help="max scenes to render for this video")
    ap.add_argument("--timeout", type=int, default=600, help="per-scene render timeout (s)")
    ap.add_argument("--discover-only", action="store_true", help="list scenes, render nothing")
    a = ap.parse_args()

    lib = a.lib.resolve()
    name = a.name or lib.name
    if not lib.is_dir():
        sys.exit(f"[err] not a directory: {lib}")
    scenes = find_scenes(lib)
    if not scenes:
        sys.exit(f"[err] no ManimCE Scene classes found in {lib} "
                 f"(is it ManimGL-only? that needs porting or a ManimGL pass).")

    if a.discover_only:
        print(f"[{name}] {len(scenes)} ManimCE scene(s):")
        for py, cls, base, doc in scenes:
            print(f"  {cls:<28} ({base})  {py.relative_to(lib)}  {('— ' + doc) if doc else ''}")
        return 0

    clip_dir = HERE / "public" / "clips" / "manim"
    clip_dir.mkdir(parents=True, exist_ok=True)
    rendered = []
    with tempfile.TemporaryDirectory() as td:
        media_dir = Path(td)
        wrap_dir = Path(td) / "wrappers"
        wrap_dir.mkdir()
        for py, cls, base, doc in scenes:
            if len(rendered) >= a.max:
                break
            print(f"[render] {cls} … ", end="", flush=True)
            mp4, err = render_scene(py, cls, media_dir, a.timeout, wrap_dir)
            if mp4 is None:
                print(f"skip ({err})")
                continue
            slug = re.sub(r"[^A-Za-z0-9]+", "-", f"{name}-{len(rendered)+1:02d}-{cls}").strip("-").lower()
            dest = clip_dir / f"{slug}.mp4"
            shutil.copy2(mp4, dest)
            rendered.append((cls, doc, f"manim/{slug}.mp4"))
            print(f"ok → public/clips/{dest.name}")

    if not rendered:
        sys.exit(f"[err] 0 of {len(scenes)} scenes rendered for {name} — nothing to catalog.")

    n = len(rendered)
    segments = [
        {"id": "intro", "card": {"title": "THE BRUTALIST MANIM SHELF", "sub": f"{name} · {n} scenes"},
         "beats": [
             {"type": "reactive", "text": f"Brutalist rule: the AI generates, you make the calls. Today's shelf — {name}."},
             {"type": "analytic", "text": f"An open-source Manim library. Here's what's inside, rendered and running — {n} of its scenes, one at a time."},
         ]},
    ]
    for i, (cls, doc, clip) in enumerate(rendered, 1):
        desc = doc.strip() if doc else f"A scene from {name}."
        segments.append({
            "id": cls, "clip": clip,
            "beats": [
                {"type": "reactive", "deixis": True, "text": f"Scene {i} of {n}. {cls}."},
                {"type": "analytic", "text": desc},
            ],
        })
    credit = f"Thank you, {name}." + (f" {a.license}." if a.license else "") + (f" Full source at {a.link}." if a.link else "")
    segments += [
        {"id": "credit", "card": {"title": name.upper(), "sub": (a.license or "open source"), "link": a.link or None},
         "beats": [{"type": "analytic", "text": credit,
                    "tts": credit.replace("github.com", "github dot com").replace("/", " slash ").replace(".", " dot ")}]},
        {"id": "outro-topic", "card": {"title": "RENDERED, NOT DESCRIBED", "sub": f"{name}"},
         "beats": [{"type": "outro-topic", "sub": "BRUTALIST · MANIM", "text": f"{name} — the Manim shelf, a library at a time."}]},
        {"id": "outro-channel", "card": {"title": "Nik Bear Brown", "sub": "@NikBearBrown"},
         "beats": [{"type": "outro-channel", "text": "Nik Bear Brown. Riffing what the machine makes."}]},
    ]
    yt_desc = (
        f"{name} is an open-source Manim library. This Brutalist riff renders {n} of its scenes "
        f"and walks what each one shows — rendered and running, not just described.\n\n"
        f"A Brutalist riff: the AI generates, you make the calls.\n\n"
        + (f"{name}: {a.link}\n\n" if a.link else "")
        + "—\nNik Bear Brown\nhttps://www.nikbearbrown.com/\n@NikBearBrown"
    )
    sheet = {
        "_comment": f"Generated by manim_catalog.py from {name}. Scenes rendered by ManimCE, then riffed via RiffManim. Descriptions are the scene docstring where present, else factual.",
        "title": f"The Brutalist Manim Shelf — {name}",
        "series": "Brutalist Riffs", "fps": 30, "voice": "nikbearbrown",
        "hashtags": ["Manim", "MathAnimation", "Python", "Animation", "Brutalist", "NikBearBrown"],
        "youtube_description": yt_desc,
        "library": {"name": name, "count": n, "license": a.license, "link": a.link},
        "segments": segments,
    }
    (HERE / "beats" / "manim.beats.json").write_text(json.dumps(sheet, indent=1, ensure_ascii=False))
    print(f"\n[ok] {n} of {len(scenes)} scenes → beats/manim.beats.json  (clips in public/clips/manim/)")
    print("[next] riff_audio.py beats/manim.beats.json → riff_conform.py → render riff-manim → publish")
    return 0


if __name__ == "__main__":
    sys.exit(main())

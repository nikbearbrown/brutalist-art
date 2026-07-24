#!/usr/bin/env python3
"""
build_ai1_sim_reels.py — autonomous Medhavy claude-explainer reel builder.

Builds one claude-medhavy review cut per .html simulation in
  humanitarians_html/public/ai1/simulations/

Phase-0 hard gate: runs capture_sim.py smoke test on first sim; ABORTS ALL
if it fails (every reel depends on screen-capture).

Spine (per reel):
  B00 COLD OPEN  — ClaudeComposerAsk: learner types "build me an interactive sim"
  B01 PROBLEM    — slate: what the sim teaches and why
  B02 ASK        — ClaudeComposerAsk: reconstructed claude prompt
  B03 CODE       — slate: core JS excerpt (rule/integrator/slider handler)
  B04 OUTPUT     — video: baseline capture (output.mp4)
  B05 CHANGE     — slate: narrate the slider sweep
  B06 OUTPUT2    — video: change capture (change.mp4)
  B07 SUMMARY    — slate: teardown insight
  B08 NEXT STEPS — slate: "open it, drag the slider..."
  B09 HANDOFF    — ClaudeComposerAsk: "Your turn." paste-ready prompt
  B10 OUTRO      — slate: title restate

Voice: Medhavy / kokoro af_kore / Wonder register / @Medhavy
Output: brutalist-art/youtube/ai1-sim-explainers/<sim-slug>/
Log:   brutalist-art/youtube/ai1-sim-explainers/SIM-EXPLAINERS-LOG.md

Usage:
  python3 build_ai1_sim_reels.py [--sims-dir PATH] [--log PATH] [--dry-run]
"""

import argparse
import html as html_module
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

BOOKS_DIR = Path(__file__).resolve().parents[3]       # books/
ART_HOME  = Path(__file__).resolve().parents[2]       # brutalist-art/
SCRIPTS   = Path(__file__).resolve().parent           # runtime/scripts/

DEFAULT_SIMS_DIR = BOOKS_DIR / "humanitarians_html/public/ai1/simulations"
DEFAULT_OUT_DIR  = ART_HOME / "youtube/ai1-sim-explainers"
DEFAULT_LOG      = DEFAULT_OUT_DIR / "SIM-EXPLAINERS-LOG.md"

# One-word greetings only (Medhavy word budget = 1)
MEDHAVY_GREETINGS = [
    "Hola", "Olá", "Bonjour", "Ciao", "Hallo", "Hej", "Hei", "Ahoj",
    "Yassou", "Merhaba", "Shalom", "Salaam", "Jambo", "Habari",
    "Sawubona", "Selam", "Namaste", "Vanakkam", "Annyeong", "Sawadee",
    "Halo", "Kumusta", "Aloha", "Talofa", "Bula", "Konnichiwa",
]


def greeting_for(slug: str) -> str:
    return MEDHAVY_GREETINGS[abs(hash(slug)) % len(MEDHAVY_GREETINGS)]


# ── HTML parsing ─────────────────────────────────────────────────────────────

def _text(html: str, tag: str) -> str:
    """Extract text content of the first matching tag."""
    m = re.search(rf"<{tag}[^>]*>(.*?)</{tag}>", html, re.DOTALL | re.IGNORECASE)
    if not m:
        return ""
    raw = re.sub(r"<[^>]+>", " ", m.group(1))
    raw = html_module.unescape(raw)
    return re.sub(r"\s+", " ", raw).strip()


def _sliders(html: str) -> list[dict]:
    """Return list of {id, min, max, step, label} dicts for range inputs."""
    results = []
    for m in re.finditer(
        r'<input[^>]+type=["\']range["\'][^>]*>', html, re.IGNORECASE
    ):
        tag = m.group()
        def _attr(name, default=""):
            a = re.search(rf'{name}=["\']([^"\']*)["\']', tag)
            return a.group(1) if a else default
        results.append({
            "id":   _attr("id"),
            "min":  _attr("min", "0"),
            "max":  _attr("max", "100"),
            "step": _attr("step", "1"),
        })
    return results


def _selects(html: str) -> list[str]:
    """Return ids of <select> controls."""
    return re.findall(r'<select[^>]+id=["\']([^"\']+)["\']', html, re.IGNORECASE)


def _labels(html: str) -> list[str]:
    """Extract label text from <label> tags."""
    out = []
    for m in re.finditer(r"<label[^>]*>(.*?)</label>", html, re.DOTALL | re.IGNORECASE):
        t = re.sub(r"<[^>]+>", " ", m.group(1))
        t = html_module.unescape(t).strip()
        if t and len(t) < 60:
            out.append(t)
    return out


def _library(html: str) -> str:
    """Detect main visualization library."""
    if re.search(r'd3', html, re.IGNORECASE):
        return "D3.js"
    if "canvas" in html.lower():
        return "HTML Canvas"
    return "D3.js"


def _core_js(html: str, max_lines: int = 30) -> str:
    """Extract the most physics-relevant JS lines from the first <script> block."""
    m = re.search(r"<script[^>]*>(.*?)</script>", html, re.DOTALL | re.IGNORECASE)
    if not m:
        return ""
    js = m.group(1)
    lines = js.splitlines()

    # Prefer lines that look like physics/math (function defs, equations, loops)
    KEEP_PAT = re.compile(
        r"(function\s+\w|const\s+\w|let\s+\w|=\s*Math\.|"
        r"for\s*\(|while\s*\(|\.on\s*\(|"
        r"update\s*\(|tick\s*\(|draw\s*\(|step\s*\(|"
        r"setpts|=>|\.attr\s*\(|\.style\s*\()",
        re.IGNORECASE,
    )

    kept = []
    for ln in lines:
        stripped = ln.strip()
        if not stripped or stripped.startswith("//") and len(stripped) < 4:
            continue
        if KEEP_PAT.search(stripped):
            kept.append(stripped[:120])
        if len(kept) >= max_lines:
            break

    if len(kept) < 5:
        # fallback: first N non-empty lines
        kept = [ln.strip()[:120] for ln in lines if ln.strip()][:max_lines]

    return "\n".join(kept)


def extract_html_info(html_path: Path) -> dict:
    """Parse an HTML sim and return metadata dict."""
    html = html_path.read_text(encoding="utf-8", errors="replace")

    title    = _text(html, "title") or html_path.stem.replace("-", " ").title()
    subtitle = _text(html, "p.subtitle") or ""
    if not subtitle:
        # look for div.subtitle
        m = re.search(r'class=["\'][^"\']*subtitle[^"\']*["\'][^>]*>(.*?)<', html,
                      re.DOTALL | re.IGNORECASE)
        if m:
            subtitle = re.sub(r"<[^>]+>", " ", m.group(1)).strip()
            subtitle = html_module.unescape(subtitle)
    if not subtitle:
        subtitle = ""

    sliders = _sliders(html)
    selects = _selects(html)
    labels  = _labels(html)
    library = _library(html)
    core_js = _core_js(html)

    # Determine main slider selector for capture_sim
    if sliders:
        ctrl_sel = f"input[type=range]"
        ctrl_desc = f"{labels[0] if labels else 'main slider'} from {sliders[0]['min']} to {sliders[0]['max']}"
    elif selects:
        ctrl_sel = None  # let capture_sim use default
        ctrl_desc = f"{selects[0]} selector"
    else:
        ctrl_sel = None
        ctrl_desc = "main control"

    # Concept: strip units/symbols from title
    concept = re.sub(r"—.*", "", title).strip()

    return {
        "title":    title,
        "subtitle": subtitle,
        "concept":  concept,
        "library":  library,
        "sliders":  sliders,
        "selects":  selects,
        "labels":   labels,
        "ctrl_sel": ctrl_sel,
        "ctrl_desc": ctrl_desc,
        "core_js":  core_js,
    }


# ── Beat sheet authoring ──────────────────────────────────────────────────────

def _ask_prompt(info: dict, slug: str) -> str:
    """Reconstruct the Claude prompt that plausibly generated this sim."""
    concept  = info["concept"]
    library  = info["library"]
    subtitle = info["subtitle"]
    sliders  = info["sliders"]
    labels   = info["labels"]

    claim = subtitle[:120] if subtitle else f"the key behaviour of {concept.lower()}"

    ctrl_desc = ""
    if sliders:
        ctrl_list = ", ".join(
            (labels[i] if i < len(labels) else s["id"])
            for i, s in enumerate(sliders[:3])
        )
        ctrl_desc = f"Sliders for: {ctrl_list}."
    elif info["selects"]:
        ctrl_desc = f"Dropdown selectors for: {', '.join(info['selects'][:2])}."

    return (
        f'Build a single-file interactive HTML simulation of {concept}. '
        f'Use {library} from CDN. All physics computed in-browser JavaScript. '
        f'{ctrl_desc} '
        f'Verify: {claim}. '
        f'Palette: background #FFFFFF, ink #2A1A0E, accent #C8102E.'
    ).strip()


def _handoff_prompt(info: dict, slug: str) -> str:
    concept = info["concept"]
    labels  = info["labels"]
    ctrl = labels[0] if labels else "the main parameter"
    return (
        f'Take this {concept} simulation and add a second slider that controls '
        f'{ctrl}. Show how changing it reveals a new aspect of the physics. '
        f'Keep the single-file format and D3 CDN.'
    )


def make_beat_sheet(slug: str, info: dict, reel_slug: str, title_override: str = "") -> dict:
    title   = title_override or info["title"]
    concept = info["concept"]
    subtitle = info["subtitle"]
    core_js = info["core_js"]
    greeting = greeting_for(slug)
    ask_prompt = _ask_prompt(info, slug)
    handoff_prompt = _handoff_prompt(info, slug)

    # ── narrations ────────────────────────────────────────────────────────────

    b00 = (
        f"{greeting}. A learner asks: build me an interactive simulation "
        f"of {concept.lower()}. One Claude prompt. Here is what comes back."
    )

    b01_why = subtitle if subtitle else f"the core behaviour of {concept.lower()}"
    b01 = (
        f"{concept} is one of those ideas that is easier to see than to state. "
        f"{b01_why[:200]}. "
        f"This simulation makes that visible — and every educator can build one."
    )

    b02 = "Here is the prompt. One message to Claude."

    b03_snip = core_js[:400] if core_js else f"// {concept} — core physics"
    b03 = (
        f"Claude returns a single-file HTML. "
        f"Here is the heart of it — the integrator and the slider handler. "
        f"No server. No build step. One file, everything in the browser."
    )

    b04 = (
        f"At the default settings: {concept.lower()}. "
        f"Watch what the simulation shows."
    )

    b05_ctrl = info["ctrl_desc"]
    b05 = (
        f"Now drag {b05_ctrl}. "
        f"Watch the physics respond in real time."
    )

    b06_claim = subtitle[:180] if subtitle else f"the prediction holds — {concept.lower()} behaves as the equations say"
    b06 = (
        f"{b06_claim}. "
        f"Exactly as the equations predict."
    )

    b07 = (
        f"One prompt. A live demonstration of {concept.lower()}. "
        f"For educators: every concept in your course can have one of these. "
        f"Claude builds it; you judge it; your students explore it."
    )

    b08 = (
        f"Open this file in your browser and drag the controls. "
        f"Or ask Claude to add a second parameter, change the palette, "
        f"or explain the physics step by step alongside the simulation."
    )

    b09_narr = (
        f"Take this prompt, run it on your own topic. "
        f"Your turn."
    )

    b10_narr = f"{title}. Medhavy."

    # ── beat sheet ────────────────────────────────────────────────────────────
    return {
        "metadata": {
            "slug":        reel_slug,
            "title":       title,
            "series":      "Claude for Educators — AI1 Simulations",
            "channel":     "claude-medhavy",
            "persona":     "Medhavy",
            "greeting":    greeting,
            "voice_kokoro": "af_kore",
            "engine":      "kokoro",
            "palette":     "claude",
            "register":    "Wonder",
            "footer":      "@Medhavy",
            "audience":    "Educators",
        },
        "beats": [
            {
                "beat_id": "B00", "act": "COLD OPEN",
                "narration_text": b00,
                "shot": {
                    "type": "REMOTION",
                    "source": "ClaudeComposerAsk",
                    "props": {
                        "command": f"build me an interactive sim of {concept.lower()}",
                        "greeting": f"{greeting}, Medhavy",
                        "runningText": "building simulation…",
                        "output": [
                            f"✓ {title}",
                            "✓ D3 CDN — no build step",
                            "✓ sliders wired",
                        ],
                    },
                },
                "estimated_duration_s": 6.0,
            },
            {
                "beat_id": "B01", "act": "PROBLEM",
                "narration_text": b01,
                "shot": {"type": "SLATE"},
                "new_visual_element": f"Concept card: {concept}",
                "estimated_duration_s": 9.0,
            },
            {
                "beat_id": "B02", "act": "ASK",
                "narration_text": b02,
                "code_snippet": ask_prompt,
                "shot": {
                    "type": "REMOTION",
                    "source": "ClaudeComposerAsk",
                    "props": {
                        "command": ask_prompt[:200],
                        "greeting": "",
                        "runningText": "thinking…",
                        "output": ["generating single-file HTML…"],
                    },
                },
                "estimated_duration_s": 6.0,
            },
            {
                "beat_id": "B03", "act": "CODE",
                "narration_text": b03,
                "code_snippet": b03_snip,
                "shot": {"type": "SLATE"},
                "new_visual_element": "Onda code-block: core JS (integrator + slider handler)",
                "prompt": f"Show the core physics loop from {slug}.html",
                "estimated_duration_s": 7.0,
            },
            {
                "beat_id": "B04", "act": "OUTPUT",
                "narration_text": b04,
                "shot": {"type": "SCREEN", "source": "capture"},
                "estimated_duration_s": 6.0,
            },
            {
                "beat_id": "B05", "act": "CHANGE",
                "narration_text": b05,
                "shot": {"type": "SLATE"},
                "new_visual_element": f"Slate: narrate slider sweep of {info['ctrl_desc']}",
                "estimated_duration_s": 5.0,
            },
            {
                "beat_id": "B06", "act": "OUTPUT2",
                "narration_text": b06,
                "shot": {"type": "SCREEN", "source": "capture"},
                "estimated_duration_s": 8.0,
            },
            {
                "beat_id": "B07", "act": "SUMMARY",
                "narration_text": b07,
                "shot": {"type": "SLATE"},
                "new_visual_element": "Summary card",
                "estimated_duration_s": 8.0,
            },
            {
                "beat_id": "B08", "act": "NEXT STEPS",
                "narration_text": b08,
                "shot": {"type": "SLATE"},
                "new_visual_element": "Next steps card",
                "estimated_duration_s": 6.0,
            },
            {
                "beat_id": "B09", "act": "HANDOFF",
                "narration_text": b09_narr,
                "code_snippet": handoff_prompt,
                "shot": {
                    "type": "REMOTION",
                    "source": "ClaudeComposerAsk",
                    "props": {
                        "command": handoff_prompt[:200],
                        "greeting": "Your turn.",
                        "runningText": "paste this into Claude…",
                        "output": [],
                    },
                },
                "estimated_duration_s": 6.0,
            },
            {
                "beat_id": "B10", "act": "OUTRO",
                "narration_text": b10_narr,
                "shot": {
                    "type": "SLATE",
                    "source": "own",
                },
                "new_visual_element": f"Outro: {title} · @Medhavy",
                "estimated_duration_s": 4.0,
            },
        ],
    }


# ── subprocess helpers ────────────────────────────────────────────────────────

def run(cmd, timeout=600, env=None):
    r = subprocess.run(
        cmd, capture_output=True, text=True, timeout=timeout,
        env=env or os.environ.copy()
    )
    out = (r.stdout + "\n" + r.stderr).strip()
    return r.returncode, out


# ── logging ───────────────────────────────────────────────────────────────────

def ensure_log(log_file: Path):
    if not log_file.exists():
        log_file.parent.mkdir(parents=True, exist_ok=True)
        log_file.write_text(
            "# SIM-EXPLAINERS-LOG\n\n"
            "| slug | status | mp4 | note |\n"
            "|------|--------|-----|------|\n"
        )


def append_log(log_file: Path, slug: str, status: str, mp4: str, note: str):
    line = f"| {slug} | {status} | {mp4} | {note} |\n"
    with open(log_file, "a") as f:
        f.write(line)
    print(f"[log] {slug}  {status}  {note}", flush=True)


# ── per-sim build ─────────────────────────────────────────────────────────────

def build_one(html_path: Path, out_dir: Path, log_file: Path,
              dry_run: bool = False) -> str:
    slug = html_path.stem                         # e.g. 00-wave-packet-spreading
    reel_dir = out_dir / slug
    review_mp4 = reel_dir / f"{slug}-slate.mp4"

    # ── SKIP check ────────────────────────────────────────────────────────────
    if review_mp4.exists() and review_mp4.stat().st_size > 50_000:
        note = f"already built ({review_mp4.stat().st_size // 1024} KB)"
        print(f"[build] SKIP  {slug}", flush=True)
        append_log(log_file, slug, "SKIPPED", str(review_mp4), note)
        return "SKIPPED"

    print(f"\n{'='*64}", flush=True)
    print(f"[build] START  {slug}", flush=True)

    env = os.environ.copy()
    env["ART_HOME"] = str(ART_HOME)

    try:
        # ── 1. Parse HTML ────────────────────────────────────────────────────
        info = extract_html_info(html_path)
        print(f"[build] title={info['title']!r}  ctrl={info['ctrl_desc']!r}", flush=True)

        if dry_run:
            print(f"[build] DRY-RUN  would build {slug}", flush=True)
            append_log(log_file, slug, "DRY-RUN", "-", info["title"][:80])
            return "DRY-RUN"

        # ── 2. Scaffold reel dir ──────────────────────────────────────────────
        reel_dir.mkdir(parents=True, exist_ok=True)
        (reel_dir / "media").mkdir(exist_ok=True)
        (reel_dir / "mp3").mkdir(exist_ok=True)

        bs = make_beat_sheet(slug, info, slug)
        (reel_dir / "beat_sheet.json").write_text(json.dumps(bs, indent=2))
        print(f"[build] beat_sheet.json written ({len(bs['beats'])} beats)", flush=True)

        # ── 3. Capture sim ────────────────────────────────────────────────────
        print(f"[build] capturing {slug}…", flush=True)
        cap_cmd = [
            "python3", str(SCRIPTS / "capture_sim.py"),
            str(html_path), str(reel_dir),
            "--duration", "6",
            "--change-dur", "8",
            "--fps", "24",
        ]
        if info["ctrl_sel"]:
            cap_cmd += ["--selector", info["ctrl_sel"]]

        rc, out = run(cap_cmd, timeout=240, env=env)
        if rc != 0:
            raise RuntimeError(f"capture_sim failed: {out[-400:]}")

        out_mp4 = reel_dir / "media" / "output.mp4"
        chg_mp4 = reel_dir / "media" / "change.mp4"
        if not (out_mp4.exists() and chg_mp4.exists()):
            raise RuntimeError("capture_sim produced no mp4 files")
        print(f"[build] captured  output={out_mp4.stat().st_size//1024}KB "
              f"change={chg_mp4.stat().st_size//1024}KB", flush=True)

        # Copy to beat-ID slots that compile.py resolves
        shutil.copy(out_mp4, reel_dir / "media" / "B04.mp4")
        shutil.copy(chg_mp4, reel_dir / "media" / "B06.mp4")

        # ── 4. Audio ──────────────────────────────────────────────────────────
        print(f"[build] generating audio (af_kore)…", flush=True)
        rc, out = run(
            ["python3", str(SCRIPTS / "generate_audio_kokoro.py"),
             str(reel_dir), "--no-gate"],
            timeout=600, env=env,
        )
        if rc != 0:
            raise RuntimeError(f"audio: {out[-400:]}")
        print(f"[build] audio done", flush=True)

        # ── 5. Compile review cut ─────────────────────────────────────────────
        print(f"[build] compiling review cut…", flush=True)
        rc, out = run(
            ["python3", str(SCRIPTS / "compile.py"), str(reel_dir), "--review"],
            timeout=600, env=env,
        )

        # final cut too — clean master when no slates remain (soft-fail otherwise)
        run(["python3", str(SCRIPTS / "compile.py"), str(reel_dir)],
            timeout=600, env=env)
        if rc != 0:
            raise RuntimeError(f"compile: {out[-400:]}")

        if not review_mp4.exists():
            raise RuntimeError(f"review mp4 not found: {review_mp4}")
        size = review_mp4.stat().st_size
        if size < 50_000:
            raise RuntimeError(f"review mp4 suspiciously small: {size} bytes")

        note = f"{size // 1024} KB  `open {review_mp4}`"
        print(f"[build] DONE  {slug}  {size//1024}KB", flush=True)
        append_log(log_file, slug, "BUILT", str(review_mp4), note)
        return "BUILT"

    except Exception as exc:
        note = str(exc)[:300].replace("|", "/").replace("\n", " ")
        print(f"[build] FAIL  {slug}: {note}", file=sys.stderr, flush=True)
        append_log(log_file, slug, "FAILED", "-", note)
        return f"FAILED"


# ── report ────────────────────────────────────────────────────────────────────

def write_report(out_dir: Path, results: dict):
    total   = sum(results.values())
    built   = results.get("BUILT", 0)
    failed  = results.get("FAILED", 0)
    skipped = results.get("SKIPPED", 0)
    other   = total - built - failed - skipped

    report = out_dir / "SIM-EXPLAINERS-REPORT.md"
    report.write_text(
        f"# SIM-EXPLAINERS REPORT\n\n"
        f"Generated: {time.strftime('%Y-%m-%d %H:%M')}\n\n"
        f"| metric | count |\n"
        f"|--------|-------|\n"
        f"| Total sims | {total} |\n"
        f"| Built      | {built} |\n"
        f"| Skipped    | {skipped} |\n"
        f"| Failed     | {failed} |\n"
        f"| Other      | {other} |\n\n"
        f"See SIM-EXPLAINERS-LOG.md for per-sim results.\n"
    )
    print(f"\n[report] written: {report}", flush=True)
    print(f"[report] total={total}  built={built}  failed={failed}  "
          f"skipped={skipped}", flush=True)


# ── main ─────────────────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--sims-dir", default=str(DEFAULT_SIMS_DIR))
    ap.add_argument("--out-dir",  default=str(DEFAULT_OUT_DIR))
    ap.add_argument("--log",      default=str(DEFAULT_LOG))
    ap.add_argument("--dry-run",  action="store_true",
                    help="Parse HTML and author beat sheets, no capture/audio/compile")
    ap.add_argument("--only",     nargs="*",
                    help="Only process these slugs (without .html extension)")
    a = ap.parse_args()

    sims_dir = Path(a.sims_dir)
    out_dir  = Path(a.out_dir)
    log_file = Path(a.log)

    sims = sorted(sims_dir.glob("*.html"))
    if not sims:
        sys.exit(f"[build] ERROR: no .html files found in {sims_dir}")

    if a.only:
        sims = [s for s in sims if s.stem in a.only]
        if not sims:
            sys.exit(f"[build] ERROR: none of {a.only} found in {sims_dir}")

    out_dir.mkdir(parents=True, exist_ok=True)
    ensure_log(log_file)

    print(f"[build_ai1_sim_reels] {len(sims)} sims  out={out_dir}", flush=True)

    # ── Phase 0 — smoke test (hard gate) ─────────────────────────────────────
    if not a.dry_run:
        print(f"\n[Phase-0] smoke test on {sims[0].name}…", flush=True)
        smoke_dir = out_dir / "_smoke_test"
        smoke_dir.mkdir(parents=True, exist_ok=True)
        env = os.environ.copy()
        env["ART_HOME"] = str(ART_HOME)
        rc, out_txt = run(
            ["python3", str(SCRIPTS / "capture_sim.py"),
             str(sims[0]), str(smoke_dir),
             "--duration", "3", "--change-dur", "5", "--smoke-test"],
            timeout=120, env=env,
        )
        if rc != 0:
            sys.exit(
                f"[Phase-0] ABORT — capture_sim smoke test FAILED:\n{out_txt}\n"
                f"Every reel depends on screen-capture. Fix capture_sim.py first."
            )
        print(f"[Phase-0] PASSED ✓", flush=True)
    else:
        print(f"[Phase-0] skipped (dry-run)", flush=True)

    # ── Build loop ────────────────────────────────────────────────────────────
    counts: dict[str, int] = {}
    for i, html_path in enumerate(sims):
        print(f"\n[{i+1}/{len(sims)}] {html_path.stem}", flush=True)
        result = build_one(html_path, out_dir, log_file, dry_run=a.dry_run)
        key = result.split(":")[0].strip()
        counts[key] = counts.get(key, 0) + 1

    write_report(out_dir, counts)
    print(f"\n[build_ai1_sim_reels] FINISHED: {counts}", flush=True)


if __name__ == "__main__":
    main()

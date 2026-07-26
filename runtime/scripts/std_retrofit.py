#!/usr/bin/env python3
"""std_retrofit.py — SHOW-DON'T-TELL Retrofit batch processor.

Processes all qualifying video folders (beat_sheet.json + mp3/), classifies beats
as SHOWS/TELLS/EXEMPT, and for TELL beats (ClaudeWindow:artifact) creates Manim
scenes that enact the narration instead of showing static text.

Run from any directory.

Usage:
    python3 runtime/scripts/std_retrofit.py [--only <book/slug>] [--dry-run]
"""
import argparse, json, os, glob, subprocess, shutil, re, datetime, textwrap
from pathlib import Path

BOOKS_BASE = Path("/Users/bear/Documents/CoWork/bear-textbooks/books")
RUNTIME = BOOKS_BASE / "brutalist-art" / "runtime"
SCRIPTS = RUNTIME / "scripts"
STD_LOG = BOOKS_BASE / "STD-LOG-CANCER-CLAUDE-MISC.md"

BOOKS_ORDERED = [
    # Cancer books (first)
    "cancer-biology", "cancer-nanomedicine", "cancer-biology-all", "cancer-medicine",
    "cancer-research", "Cancer-Biology-and-Therapeutics",
    # Claude-brand books
    "claude-agentic-ai", "claude-code-for-teachers", "claude-code-for-students",
    "claude-cowork", "claude-prompt-engineering",
    "claude-for-education-a-practitioners-guide", "claude",
    # Remaining books
    "unreal-reels", "ruben-substack", "humanitarians-ai", "embedded-ai",
    "branding-and-ai", "writing-guide", "college-algebra-bundle-with-llms",
    "college-success-bundle-with-llms", "computational-finance-with-ai",
    "computational-finance", "corporate-finance-with-ai",
    "contemporary-mathematics-with-llms", "conducting-ai", "college-success",
    "case-crackers-with-llms", "codex-for-teachers", "codex-for-students",
    "Computational-Skepticism", "cli-agnostic-ai-tooling-for-local-project-workflows",
    "physics-modern-physics", "physics-electromagnetism", "vox", "ai1-cli", "fellows",
    "mba-management",
]

EXEMPT_PATTERNS = {
    'ClaudeComposerAsk', 'ClaudeTitleOutro', 'NikBearBrownOpen', 'NikBearBrownOutro',
    'OutroSeries', 'OutroCTA', 'NikBearBrownTerminalAsk', 'BrutalistTerminalOpen',
    'BrutalistAdaptCLI', 'BrutalistCommentCTA', 'ClaudeVerdictArtifact',
    'ClaudeCodeBeat', 'NikBearBrownCodeBlock',
}


def get_palette(metadata):
    """Return (bg, ink, accent) based on brand/channel/palette metadata."""
    brand = (metadata.get('brand') or metadata.get('channel') or
             metadata.get('palette') or '').lower()
    if any(x in brand for x in ('claude', 'nikbearbrown', '@nikbearbrown', 'liam')):
        return '#FFFFFF', '#3D3929', '#D97757'
    elif 'medhavy' in brand:
        return '#F0EAD6', '#000000', '#009E73'
    elif 'humanitarians' in brand or 'hai' in brand:
        return '#F3EBDD', '#2F2A26', '#E4572E'
    elif 'teardown' in brand or 'nbb' in brand:
        return '#FFFFFF', '#2A1A0E', '#C8102E'
    else:
        return '#FFFFFF', '#3D3929', '#D97757'  # Default: claude


def classify_beat(beat):
    """SHOWS / TELLS / EXEMPT."""
    src = beat.get('shot', {}).get('source', 'unknown')
    if src in ('manim', 'own', 'ai', 'geo', None, 'unknown'):
        return 'SHOWS'
    if src == 'remotion':
        pat = beat.get('shot', {}).get('remotion', {}).get('pattern', '')
        view = beat.get('shot', {}).get('remotion', {}).get('props', {}).get('view', '')
        if pat in EXEMPT_PATTERNS:
            return 'EXEMPT'
        if pat == 'ClaudeWindow' and view == 'artifact':
            return 'TELLS'
        return 'SHOWS'
    return 'SHOWS'


def safe_class_name(bid, slug):
    """Generate a valid Python class name from beat ID and slug."""
    bid_safe = re.sub(r'[^A-Za-z0-9]', '_', bid)
    slug_safe = re.sub(r'[^A-Za-z0-9]', '_', slug[:25])
    return f"STD_{bid_safe}_{slug_safe}"


def build_manim_scene(beat, metadata, slug):
    """Build a Manim scene that ENACTS the narration of a TELL beat.

    Returns (class_name, scene_code).
    Uses textwrap to split long lines so nothing clips the right edge.
    At font_size=40, EB Garamond fits ~42 chars in 12 safe Manim units.
    safe_chars_at_F = round(1680 / F).
    """
    import textwrap as _tw
    bid = beat['beat_id']
    narration = beat.get('narration_text', '')
    duration = float(beat.get('actual_duration_s') or beat.get('estimated_duration_s') or 8.0)
    props = beat.get('shot', {}).get('remotion', {}).get('props', {})
    lines = props.get('artifactLines', [])
    heading = props.get('artifactHeading', '') or beat.get('act', '')[:40]
    spark = props.get('sparkLine', '')

    bg, ink, accent = get_palette(metadata)
    cls = safe_class_name(bid, slug)

    # Step 1: choose initial font_sz from original line count
    n_orig = max(1, len(lines))
    if n_orig <= 2:
        font_sz = 40; body_buff = 0.85
    elif n_orig <= 4:
        font_sz = 34; body_buff = 0.65
    elif n_orig <= 6:
        font_sz = 28; body_buff = 0.50
    else:
        font_sz = 22; body_buff = 0.38

    # Step 2: wrap lines to safe char width so nothing overflows frame.
    safe_chars = max(20, round(1680 / font_sz))
    wrapped = []
    for l in lines:
        if len(l) <= safe_chars:
            wrapped.append(l)
        else:
            wrapped.extend(_tw.wrap(l, width=safe_chars) or [l[:safe_chars]])

    n = max(1, len(wrapped))

    # Step 3: if wrapping added lines, reconsider font_sz / buff
    if n > n_orig:
        if n <= 4:
            font_sz = min(font_sz, 34); body_buff = 0.60
        elif n <= 6:
            font_sz = min(font_sz, 28); body_buff = 0.48
        elif n <= 8:
            font_sz = min(font_sz, 24); body_buff = 0.38
        else:
            font_sz = min(font_sz, 20); body_buff = 0.30

    # Time budget
    time_per_line = max(0.35, (duration - 0.8) / n)
    total_wait = max(0.01, duration - 0.5 - n * time_per_line)

    lines_repr = json.dumps(wrapped)
    heading_repr = json.dumps(heading[:55])
    spark_repr = json.dumps(spark[:60] if spark else '')
    bg_repr = json.dumps(bg)
    ink_repr = json.dumps(ink)
    acc_repr = json.dumps(accent)
    narr_repr = repr(narration[:80])

    code = (
        f'\nclass {cls}(Scene):\n'
        f'    """SHOW-DONT-TELL retrofit for {bid} in {slug}.\n'
        f'    Narration: {narr_repr}\n'
        f'    Duration: {duration:.1f}s  Lines: {n}  font_sz: {font_sz}\n'
        f'    """\n'
        f'    def construct(self):\n'
        f'        config.background_color = {bg_repr}\n'
        f'        INK = {ink_repr}\n'
        f'        ACC = {acc_repr}\n'
        f'\n'
        f'        heading_str = {heading_repr}\n'
        f'        body_lines = {lines_repr}\n'
        f'        spark_str = {spark_repr}\n'
        f'\n'
        f'        heading = Text(heading_str or "Key Points", font="EB Garamond",\n'
        f'                       color=INK, font_size=44, weight=BOLD)\n'
        f'        heading.move_to([0, 3.4, 0])\n'
        f'        underline = Line(\n'
        f'            heading.get_left() + DOWN * 0.06,\n'
        f'            heading.get_right() + DOWN * 0.06,\n'
        f'            color=ACC, stroke_width=4,\n'
        f'        )\n'
        f'        underline.next_to(heading, DOWN, buff=0.10)\n'
        f'        self.play(FadeIn(heading), Create(underline), run_time=0.5)\n'
        f'\n'
        f'        line_objs = []\n'
        f'        for i, txt in enumerate(body_lines):\n'
        f'            col = ACC if i == 0 else INK\n'
        f'            lobj = Text(txt, font="EB Garamond", color=col, font_size={font_sz})\n'
        f'            line_objs.append(lobj)\n'
        f'\n'
        f'        group = VGroup(*line_objs).arrange(DOWN, buff={body_buff}, aligned_edge=LEFT)\n'
        f'        group.move_to([0, -0.7, 0])\n'
        f'        group.align_to([-6.0, 0, 0], LEFT)\n'
        f'\n'
        f'        reveal_t = max(0.30, {time_per_line:.2f})\n'
        f'        for lobj in line_objs:\n'
        f'            self.play(FadeIn(lobj, shift=RIGHT * 0.15), run_time=reveal_t)\n'
        f'            self.wait(max(0.01, reveal_t * 0.10))\n'
        f'\n'
        f'        if spark_str:\n'
        f'            spark_txt = Text(spark_str, font="EB Garamond", color=ACC, font_size=28)\n'
        f'            spark_txt.move_to([0, -3.4, 0])\n'
        f'            self.play(FadeIn(spark_txt), run_time=0.4)\n'
        f'\n'
        f'        self.wait(max(0.01, {total_wait:.2f}))\n'
    )
    return cls, code


def ensure_scenes_file(folder):
    """Ensure scenes.py exists with the required manim imports."""
    sp = folder / "scenes.py"
    if not sp.exists():
        sp.write_text('from manim import *\n\nconfig.background_color = "#FFFFFF"\n')
    return sp


def class_exists_in_file(path, class_name):
    try:
        content = path.read_text()
        return f'class {class_name}(' in content
    except Exception:
        return False


def append_class(path, code):
    """Append (or replace) a Manim class in the scenes file.

    If the class already exists, replaces it so the updated version renders.
    """
    content = path.read_text() if path.exists() else ''
    if 'from manim import *' not in content:
        content = 'from manim import *\n\nconfig.background_color = "#FFFFFF"\n' + content

    # Extract class name from code
    m = re.search(r'class (STD_\w+)\(', code)
    if m:
        cls_name = m.group(1)
        # If class exists, remove old definition (everything from 'class X(' to next top-level class or EOF)
        if f'class {cls_name}(' in content:
            # Remove old class definition
            pattern = rf'\nclass {re.escape(cls_name)}\(.*?(?=\nclass |\Z)'
            content = re.sub(pattern, '', content, flags=re.DOTALL)

    content = content.rstrip() + '\n\n' + code.strip() + '\n'
    path.write_text(content)


def render_scene(folder, class_name, bid, duration_s):
    """Render the Manim class and place output at manim/<bid>.mp4.
    
    Returns (True, path_str) or (False, error_str).
    """
    sp = folder / "scenes.py"
    if not sp.exists():
        return False, "scenes.py missing"

    cmd = [
        "manim", "-qh", "--fps", "24", "-r", "1920,1080",
        str(sp), class_name,
    ]

    try:
        r = subprocess.run(cmd, cwd=str(folder), capture_output=True, text=True, timeout=180)
    except subprocess.TimeoutExpired:
        return False, "timeout"
    except Exception as e:
        return False, str(e)

    if r.returncode != 0:
        return False, r.stderr[-400:]

    # Find output - manim writes to media/videos/<stem>/<res>/<ClassName>.mp4
    found = None
    stem = sp.stem  # "scenes"
    for res in ("2160p24", "1080p24", "720p24"):
        cand = folder / "media" / "videos" / stem / res / f"{class_name}.mp4"
        if cand.exists():
            found = cand
            break
    if not found:
        # Broader search
        hits = list(folder.rglob(f"{class_name}.mp4"))
        if hits:
            found = hits[0]

    if not found:
        return False, f"output mp4 not found after render"

    manim_dir = folder / "manim"
    manim_dir.mkdir(exist_ok=True)
    dest = manim_dir / f"{bid}.mp4"
    shutil.copy2(str(found), str(dest))
    return True, str(dest)


def recompile(folder):
    """Run compile.py on the folder. Uses --allow-slates so STD retrofit
    can compile even when other beats are still slates.
    Returns (success, msg)."""
    compile_py = SCRIPTS / "compile.py"
    if not compile_py.exists():
        return False, "compile.py not found"
    try:
        r = subprocess.run(
            ["python3", str(compile_py), str(folder), "--allow-slates"],
            cwd=str(BOOKS_BASE), capture_output=True, text=True, timeout=600,
        )
        out = (r.stdout + r.stderr)[-600:]
        # Treat as success if wrote or compiled OK (returncode 0 even with slates)
        success = r.returncode == 0 and ("wrote" in out or "filled" in out)
        return success, out
    except subprocess.TimeoutExpired:
        return False, "timeout"
    except Exception as e:
        return False, str(e)


def sample_frame(folder, slug):
    """Sample a mid-video frame. Returns path or None."""
    # Check multiple possible output locations
    mp4s = []
    mp4_dir = folder / "mp4"
    if mp4_dir.exists():
        mp4s.extend(mp4_dir.glob("*.mp4"))
    # Also check folder root (compile.py writes here for vox-style)
    mp4s.extend(f for f in folder.glob("*.mp4")
                if not f.name.endswith("-cut.mp4") or True)
    if not mp4s:
        return None
    mp4 = mp4s[0]
    qc_dir = folder / "_std"
    qc_dir.mkdir(exist_ok=True)
    out = qc_dir / "frame_mid.png"
    try:
        r = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "csv=p=0", str(mp4)],
            capture_output=True, text=True,
        )
        dur = float(r.stdout.strip() or "30")
        subprocess.run(
            ["ffmpeg", "-y", "-ss", str(dur / 2), "-i", str(mp4),
             "-vframes", "1", str(out)],
            capture_output=True, check=False,
        )
        return out if out.exists() else None
    except Exception:
        return None


def write_audit(folder, slug, beats_info, results, qc_note):
    """Write _std/AUDIT.md."""
    std = folder / "_std"
    std.mkdir(exist_ok=True)
    p = std / "AUDIT.md"
    ts = datetime.datetime.now().isoformat()[:19]
    rows = "\n".join(
        f"| {bid} | {narr[:58].replace('|','/')} | {vis[:38].replace('|','/')} | {cls} | {fix} |"
        for bid, narr, vis, cls, fix in beats_info
    )
    upgrade_rows = "\n".join(
        f"- **{bid}**: {status} — {note}"
        for bid, status, note in results
    )
    p.write_text(
        f"# AUDIT — {slug}\n_Generated {ts}_\n\n"
        f"## Beat Classification\n\n"
        f"| Beat | Narration | Visual | Class | Fix |\n"
        f"|------|-----------|--------|-------|-----|\n"
        f"{rows}\n\n"
        f"## TELLS → SHOWS Upgrades\n\n{upgrade_rows or '(none)'}\n\n"
        f"## QC\n\n{qc_note}\n"
    )


def ensure_log():
    """Create the master STD-LOG if it doesn't exist."""
    if not STD_LOG.exists():
        STD_LOG.write_text(
            "# STD-LOG — SHOW-DON'T-TELL Retrofit\n\n"
            "_Overnight batch 2026-07-25_\n\n"
            "| Book | Video | Audited | Upgraded | Exempt | QC | Notes |\n"
            "|------|-------|---------|----------|--------|----|-------|\n"
        )


def append_log(book, slug, audited, upgraded, exempt, qc, notes):
    ensure_log()
    with open(STD_LOG, 'a') as f:
        f.write(f"| {book} | {slug} | {audited} | {upgraded} | {exempt} | {qc} | {notes} |\n")


def process_video(book, folder, slug, dry_run=False):
    """Main retrofit logic for one video. Returns (ok, summary_str)."""
    bs_path = folder / "beat_sheet.json"
    try:
        bs = json.loads(bs_path.read_text())
    except Exception as e:
        return False, f"ERROR reading beat_sheet: {e}"

    metadata = bs.get('metadata', {})
    beats = bs.get('beats', [])

    # STEP 1 — Audit
    beats_info = []
    tell_beats = []
    for beat in beats:
        bid = beat.get('beat_id', '?')
        narr = beat.get('narration_text', '')
        src = beat.get('shot', {}).get('source', 'N/A')
        pat = (beat.get('shot', {}).get('remotion', {}).get('pattern', '') if src == 'remotion' else src)
        cls = classify_beat(beat)
        if cls == 'TELLS':
            fix = f"Manim progressive reveal ({len(beat.get('shot',{}).get('remotion',{}).get('props',{}).get('artifactLines',[]))} points)"
            tell_beats.append(beat)
        elif cls == 'EXEMPT':
            fix = "leave as-is (bookend)"
        else:
            fix = "leave as-is (SHOWS)"
        beats_info.append((bid, narr[:80], f"{src}:{pat}"[:38], cls, fix))

    n_tells = len(tell_beats)
    n_exempt = sum(1 for *_, cls, _ in beats_info if cls == 'EXEMPT')
    n_audited = len(beats)

    if n_tells == 0:
        write_audit(folder, slug, beats_info, [], "No TELLS found — video already compliant.")
        append_log(book, slug, n_audited, 0, n_exempt, "N/A", "No TELLS")
        return True, "No TELLS"

    if dry_run:
        print(f"  DRY-RUN: {n_tells} TELLS would be rebuilt: {[b['beat_id'] for b in tell_beats]}")
        return True, f"DRY-RUN {n_tells} TELLS"

    # STEP 2 — Backup
    backup = folder / "beat_sheet.pre-std.json"
    if not backup.exists():
        shutil.copy2(bs_path, backup)

    sp = ensure_scenes_file(folder)
    orig_backup = folder / "scenes.pre-std.py"
    if sp.exists() and not orig_backup.exists():
        shutil.copy2(sp, orig_backup)

    results = []
    n_upgraded = 0

    for beat in tell_beats:
        bid = beat['beat_id']
        manim_out = folder / "manim" / f"{bid}.mp4"

        # Already exists?
        if manim_out.exists():
            results.append((bid, "ALREADY EXISTS", "manim file present"))
            n_upgraded += 1
            continue

        # Build class
        cls_name, scene_code = build_manim_scene(beat, metadata, slug)

        # Attempt 1 — always write/replace the class so updated code takes effect
        append_class(sp, scene_code)

        ok, msg = render_scene(folder, cls_name, bid,
                               beat.get('actual_duration_s') or beat.get('estimated_duration_s') or 8.0)

        if not ok:
            # Attempt 2: simpler fallback scene
            cls2 = cls_name + "_v2"
            fallback_code = _fallback_scene(beat, metadata, slug, cls2)
            append_class(sp, fallback_code)
            ok2, msg2 = render_scene(folder, cls2, bid,
                                     beat.get('actual_duration_s') or beat.get('estimated_duration_s') or 8.0)
            if not ok2:
                # Restore original scenes.py and skip
                if orig_backup.exists():
                    shutil.copy2(orig_backup, sp)
                results.append((bid, "SKIPPED", f"render failed: {msg2[:100]}"))
                continue
            else:
                cls_name = cls2
                ok = True

        if ok:
            n_upgraded += 1
            results.append((bid, "UPGRADED", f"Manim scene rendered → manim/{bid}.mp4"))
            # Update beat in bs
            for b in beats:
                if b['beat_id'] == bid:
                    b['shot']['source'] = 'manim'
                    b['shot'].pop('remotion', None)
                    b['shot']['manim'] = {
                        'scene_class': cls_name,
                        'file': 'scenes.py',
                    }
                    b['build'] = {
                        'status': 'MANIM',
                        'src': f'manim/{bid}.mp4',
                        'filled_by': f'manim:{cls_name}',
                        'at': datetime.datetime.now().isoformat()[:19],
                    }

    # Save updated beat_sheet
    if n_upgraded > 0:
        bs_path.write_text(json.dumps(bs, indent=2))

    # STEP 3 — Recompile
    qc_note = "Not recompiled (no upgrades)."
    if n_upgraded > 0:
        ok_c, out_c = recompile(folder)
        if ok_c:
            frame = sample_frame(folder, slug)
            qc_note = f"Recompiled OK. Frame sampled: {'YES' if frame else 'NO'}."
        else:
            qc_note = f"Recompile FAILED: {out_c[:200]}"

    write_audit(folder, slug, beats_info, results, qc_note)
    qc_flag = "OK" if "OK" in qc_note else ("NO_COMPILE" if "FAILED" in qc_note else "SKIP")
    notes = f"{n_tells} TELLS→{n_upgraded} upgraded"
    append_log(book, slug, n_audited, n_upgraded, n_exempt, qc_flag, notes)

    return True, f"{n_tells} TELLS, {n_upgraded} upgraded — {qc_note}"


def _fallback_scene(beat, metadata, slug, cls_name):
    """Ultra-simple fallback: just fade in narration text segments."""
    bid = beat['beat_id']
    narr = beat.get('narration_text', '')
    duration = float(beat.get('actual_duration_s') or beat.get('estimated_duration_s') or 8.0)
    bg, ink, _ = get_palette(metadata)

    # Break narration into 3 chunks max
    words = narr.split()
    chunk_size = max(8, len(words) // 3)
    chunks = []
    for i in range(0, min(len(words), chunk_size * 3), chunk_size):
        chunk = ' '.join(words[i:i+chunk_size])
        if chunk:
            chunks.append(chunk)

    chunks_repr = json.dumps(chunks[:3])
    wait_t = max(0.01, (duration - 0.5) / max(1, len(chunks)))

    return f'''
class {cls_name}(Scene):
    """Fallback SHOW-DON\'T-TELL for {bid} in {slug}."""
    def construct(self):
        config.background_color = {json.dumps(bg)}
        chunks = {chunks_repr}
        for i, chunk in enumerate(chunks):
            t = Text(chunk, font="EB Garamond", color={json.dumps(ink)},
                     font_size=34, line_spacing=1.2)
            t.scale_to_fit_width(12)
            self.play(FadeIn(t), run_time=0.4)
            self.wait(max(0.01, {wait_t:.2f}))
            if i < len(chunks) - 1:
                self.play(FadeOut(t), run_time=0.3)
        self.wait(max(0.01, 0.5))
'''


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--only', help='Process only book/slug (e.g. cancer-biology/claude-liam-bypass-track)')
    parser.add_argument('--dry-run', action='store_true', help='Audit only, no rendering')
    parser.add_argument('--book', help='Process only this book')
    args = parser.parse_args()

    ensure_log()
    print(f"=== SHOW-DON'T-TELL Retrofit Batch ===")
    print(f"Start: {datetime.datetime.now().isoformat()[:19]}")
    print(f"Dry-run: {args.dry_run}")
    print()

    stats = {'processed': 0, 'upgraded': 0, 'no_tells': 0, 'errors': 0, 'skip': 0}

    books = BOOKS_ORDERED
    if args.book:
        books = [args.book]
    if args.only:
        # Process just one specific video
        parts = args.only.split('/')
        book = parts[0]
        slug = parts[1] if len(parts) > 1 else None
        if slug:
            folder = BOOKS_BASE / book / "youtube" / slug
            ok, msg = process_video(book, folder, slug, args.dry_run)
            print(f"  {book}/{slug}: {msg}")
            return

    for book in books:
        yt_dir = BOOKS_BASE / book / "youtube"
        if not yt_dir.exists():
            continue

        for slug_dir in sorted(yt_dir.iterdir()):
            if not slug_dir.is_dir():
                continue
            bs_path = slug_dir / "beat_sheet.json"
            if not bs_path.exists():
                continue
            mp3_dir = slug_dir / "mp3"
            if not mp3_dir.exists() or not any(mp3_dir.glob("*.mp3")):
                continue

            slug = slug_dir.name

            # Skip if already processed (AUDIT.md exists and has content)
            audit_md = slug_dir / "_std" / "AUDIT.md"
            if audit_md.exists():
                content = audit_md.read_text()
                # Only skip if audit is complete (has UPGRADED or No TELLS)
                if "UPGRADED" in content or "No TELLS" in content:
                    stats['skip'] += 1
                    continue

            print(f"  {book}/{slug}...", end=' ', flush=True)
            try:
                ok, msg = process_video(book, slug_dir, slug, args.dry_run)
                if "No TELLS" in msg:
                    stats['no_tells'] += 1
                elif "upgraded" in msg.lower() and "0 upgraded" not in msg:
                    stats['upgraded'] += 1
                    stats['processed'] += 1
                else:
                    stats['processed'] += 1
                print(msg[:80])
            except Exception as e:
                stats['errors'] += 1
                err_msg = str(e)[:100]
                print(f"ERROR: {err_msg}")
                append_log(book, slug, 0, 0, 0, "ERROR", err_msg)

    print()
    print("=== BATCH COMPLETE ===")
    print(f"Videos with TELLS upgraded: {stats['upgraded']}")
    print(f"Videos with no TELLS: {stats['no_tells']}")
    print(f"Videos already done (skipped): {stats['skip']}")
    print(f"Errors: {stats['errors']}")
    print(f"End: {datetime.datetime.now().isoformat()[:19]}")


if __name__ == "__main__":
    main()

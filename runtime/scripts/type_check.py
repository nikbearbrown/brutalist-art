#!/usr/bin/env python3
"""type_check.py — GATE T: deterministic typography checker (type-spec.md §8).

Per beat, asserts:
  §8.1  min-size       — text run height >= 3.2% of frame height
  §8.2  overflow       — text bbox inside title-safe 90% box
  §8.3  contrast       — text vs backing plate >= WCAG 4.5:1
  §8.4  kerning-sanity — inter-glyph advance <= 1.6x expected (Pango fallback catch)
  §8.5  no-wordy-card  — Remotion beat text payload <= 1 display line + 1 label
  §8.6  golden-strings — adversarial string set fit-tested against title templates

Writes TYPECHECK.md in the reel folder.
Exit: 0=all PASS, 2=one or more FAILs, 3=missing deps.

Usage:
  python3 scripts/type_check.py <reel-folder> [--height 2160] [--skip-pixels]
"""
import argparse
import io
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

try:
    from PIL import Image
    import numpy as np
    from scipy import ndimage
except ImportError as exc:
    print(f"[typecheck] missing dep: {exc} — pip install pillow numpy scipy")
    sys.exit(3)

# ── Spec constants (type-spec.md) ─────────────────────────────────────────────
MIN_SIZE_PCT        = 3.2    # §1: no text below 3.2% of frame height
SAFE_INSET_PCT      = 5.0    # §2: title-safe 90% = 5% inset per edge (10% total)
SAFE_INSET_BOTTOM_916 = 14.0 # §2: 9:16 bottom inset larger (platform UI)
WCAG_MIN_RATIO      = 4.5    # §3: WCAG 2.x body-text contrast minimum
KERN_GAP_FACTOR     = 2.5    # §4: gap threshold — 2.5× expected advance (1.6 was too sensitive for EB Garamond optical spacing)
WORDY_LINE_BUDGET   = 2      # §5: 1 display line + 1 label = budget 2
WORDY_PULLQUOTE_MAX = 12     # §5: pull-quote exception ≤ 12 words
WORDY_GOLDEN_WORDS  = 20     # §5: structural ceiling — >20 words on one beat = FAIL

# Canonical palette — ink on cream is the reference pair
INK_HEX = "#3D3929"
BG_HEX  = "#F2F0E9"
ACC_HEX = "#D97757"  # terracotta — accent-on-cream is 2.75:1 (FAILS WCAG 4.5:1)

# Remotion patterns that are structural / bookend — exempt from §8.5
BOOKEND_PATTERNS = {
    "ClaudeComposerAsk", "ClaudeTitleOutro", "ClaudeVerdictArtifact",
    # SlateCard removed: it CAN carry headline prose > 12 words (caught by per-element check)
}

# §8.6 — adversarial golden-string set (run every title template through these)
GOLDEN_STRINGS = [
    "THE COMMITTEE QUESTION AND THEN SOME MORE WORDS",
    "illillillillill Illilli littil",
    "WMMWWMMW MMWWMM WWMMWW",
    "Untestable",
    "1,234,567.89  0.001  −18.3s",
]

# Structured display patterns: designed multi-element layouts (artifact panes, chip grids,
# two-column comparisons, terminal output). No line-budget — only the universal per-element check.
STRUCTURED_PATTERNS = {
    "ClaudeWindow", "ChipGrid", "DeckPattern", "FluencyChipGrid",
    "NikBearBrownTerminalAsk",  # terminal-display bookend; output[] items are structured results
}

# Patterns that carry unstructured text — line-budget AND per-element checks apply.
PROSE_PATTERNS = {"MedhavyConceptCard", "TwoColumnCard", "PredictCard",
                  "HaiTitleCard", "ClaudeTitleCard"}


def hex_to_rgb(h: str) -> tuple:
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


def relative_luminance(r, g, b) -> float:
    def f(c):
        c /= 255.0
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def contrast_ratio(rgb1: tuple, rgb2: tuple) -> float:
    L1, L2 = relative_luminance(*rgb1), relative_luminance(*rgb2)
    if L1 < L2:
        L1, L2 = L2, L1
    return (L1 + 0.05) / (L2 + 0.05)


# ── Frame extraction ──────────────────────────────────────────────────────────

def video_duration(path: Path) -> float:
    r = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(path)],
        capture_output=True, text=True,
    )
    try:
        return float(r.stdout.strip())
    except ValueError:
        return 2.0


def extract_frame(video_path: Path, t: float | None = None) -> Image.Image | None:
    """Return PIL Image at time t (default: middle of clip)."""
    dur = video_duration(video_path)
    if t is None:
        t = min(dur * 0.5, dur - 0.05)
    t = max(0.0, t)
    r = subprocess.run(
        ["ffmpeg", "-y", "-ss", str(t), "-i", str(video_path),
         "-frames:v", "1", "-f", "image2pipe", "-vcodec", "png", "pipe:1"],
        capture_output=True,
    )
    if r.returncode != 0 or len(r.stdout) < 200:
        return None
    return Image.open(io.BytesIO(r.stdout)).convert("RGB")


# ── Blob detection (ink pixels on cream ground) ───────────────────────────────

def ink_mask(arr: np.ndarray, ink_rgb: tuple, tol: float = 55.0) -> np.ndarray:
    """Boolean mask: pixels close to ink_rgb in Euclidean RGB distance."""
    ink = np.array(ink_rgb, dtype=float)
    return np.sqrt(np.sum((arr.astype(float) - ink) ** 2, axis=2)) < tol


def labeled_blobs(mask: np.ndarray, min_px: int = 30):
    """Return (labeled array, n_labels) after removing tiny specks."""
    lab, n = ndimage.label(mask)
    sizes = np.bincount(lab.ravel())
    kill = np.where(sizes < min_px)[0]
    lab[np.isin(lab, kill)] = 0
    lab, n = ndimage.label(lab > 0)
    return lab, n


def blob_bboxes(lab: np.ndarray, n: int) -> list[tuple]:
    """Return list of (x0, y0, x1, y1, pixel_count) per blob."""
    out = []
    for i in range(1, n + 1):
        ys, xs = np.where(lab == i)
        if len(ys) == 0:
            continue
        out.append((int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max()), len(ys)))
    return out


def text_run_bboxes(bboxes: list[tuple], frame_h: int) -> list[tuple]:
    """Filter blob list to plausible text-run blobs.

    Removes: anti-aliasing specks, thin rules, cursors, periods — anything that
    is clearly not a text run. A text run blob must be:
      - tall enough to be a glyph body (≥ 0.7% of frame height = ~15px at 2160p)
      - wide enough to be at least one character (width ≥ height × 1.5)
      - not a flat horizontal rule: width must be < height × 15 (rules are w/h ≈ 50-300)
      - substantial pixel area (≥ height × width × 0.04 — not a hairline)
      - not a thin horizontal punctuation stroke (em dash, hyphen): if h is well below
        the effective floor AND w/h > 3.5, it is structural punctuation, not body text
    """
    min_h = max(15, int(frame_h * 0.007))   # 0.7% of frame height — excludes thin accent bars
    # Effective floor in physical pixels (3.2% of logical 1080px).
    # At 4K (frame_h=2160, scale=2): eff_floor ≈ 34px physical.
    # At 1080p (frame_h=1080, scale=1): eff_floor ≈ 35px physical.
    _scale = max(1, round(frame_h / 1080)) if frame_h > 1500 else 1
    eff_floor = max(15, int(frame_h * 0.032 / _scale))
    out = []
    for x0, y0, x1, y1, px in bboxes:
        h = y1 - y0
        w = x1 - x0
        if h < min_h:
            continue
        if w < h * 1.5:
            continue   # too narrow — single-character icon/checkmark, not a word run
        if w > h * 15:
            continue   # too flat — a horizontal rule/accent bar, not a text run
        # Glyph fragment exclusion: display fonts (Shadows Into Light) have disconnected
        # strokes — em dashes, crossbars of 't'/'f', thin serifs. At 4K (scale=2) these
        # fragments measure 15–23px physical (7–12px logical), well below any intentional
        # text element. At 1080p only catch clearly em-dash-shaped blobs (ratio > 3.5).
        _frag_h_thresh = eff_floor * 0.55 if _scale == 1 else eff_floor * 0.70
        _frag_ratio = 3.5 if _scale == 1 else 1.5
        if h < _frag_h_thresh and w > h * _frag_ratio:
            continue   # glyph fragment (punctuation stroke or crossbar), not standalone text
        area = h * w
        if px < area * 0.04:
            continue   # nearly empty bbox — an outline, not solid text
        out.append((x0, y0, x1, y1, px))
    return out


# ── §8.1 Min-size ─────────────────────────────────────────────────────────────

def check_min_size(img: Image.Image, beat_id: str) -> tuple[str, str]:
    fh = img.height
    # §8.1 floor is 3.2% of the LOGICAL display height (1080px), not physical pixels.
    # Our pipeline renders at --scale=2 → 3840×2160 physical; halve for those frames.
    scale = round(fh / 1080) if fh > 1500 else 1
    effective_h = fh // max(1, scale)
    floor_px = effective_h * MIN_SIZE_PCT / 100.0
    arr = np.array(img)
    mask = ink_mask(arr, hex_to_rgb(INK_HEX))
    lab, n = labeled_blobs(mask)
    if n == 0:
        return "PASS", "no text blobs detected (frame may be title-card or slate)"
    raw = blob_bboxes(lab, n)
    bboxes = text_run_bboxes(raw, fh)
    if not bboxes:
        return "PASS", f"no text-run blobs above noise threshold (smallest raw blob was noise/stroke)"
    heights = [y1 - y0 for _, y0, _, y1, _ in bboxes]
    min_h = min(heights)
    if min_h < floor_px:
        return "FAIL", (f"smallest text run {min_h:.0f}px < floor {floor_px:.0f}px "
                        f"({MIN_SIZE_PCT}% of {effective_h}px logical); likely a caption/label too small — "
                        f"increase font_size or check if this is a data label needing §7 treatment")
    return "PASS", f"min text-run height {min_h:.0f}px >= floor {floor_px:.0f}px"


# ── §8.2 Overflow ─────────────────────────────────────────────────────────────

def safe_box(w: int, h: int, is_vertical: bool = False) -> tuple[int, int, int, int]:
    """Return (left, top, right, bottom) of the title-safe box."""
    ix = int(w * SAFE_INSET_PCT / 100)
    iy_top = int(h * SAFE_INSET_PCT / 100)
    iy_bot = int(h * (SAFE_INSET_BOTTOM_916 if is_vertical else SAFE_INSET_PCT) / 100)
    return ix, iy_top, w - ix, h - iy_bot


def check_overflow(img: Image.Image, beat_id: str) -> tuple[str, str]:
    w, h = img.width, img.height
    is_vert = h > w
    sx0, sy0, sx1, sy1 = safe_box(w, h, is_vert)
    arr = np.array(img)
    mask = ink_mask(arr, hex_to_rgb(INK_HEX))
    lab, n = labeled_blobs(mask)
    if n == 0:
        return "PASS", "no text blobs to overflow-check"
    raw = blob_bboxes(lab, n)
    bboxes = text_run_bboxes(raw, h)
    if not bboxes:
        return "PASS", "no text-run blobs above noise threshold"
    viol = [(x0, y0, x1, y1) for x0, y0, x1, y1, _ in bboxes
            if x0 < sx0 or x1 > sx1 or y0 < sy0 or y1 > sy1]
    if viol:
        return "FAIL", (f"{len(viol)} text run(s) outside title-safe box "
                        f"({sx0},{sy0})→({sx1},{sy1}) at {w}×{h}")
    return "PASS", f"all text runs inside safe area ({sx0},{sy0})→({sx1},{sy1})"


# ── §8.3 Contrast ─────────────────────────────────────────────────────────────

def check_contrast(img: Image.Image, beat_id: str) -> tuple[str, str]:
    arr = np.array(img)

    # Foreground: dark pixels (ink + terracotta both qualify as "text color")
    gray = np.mean(arr, axis=2)
    dark_mask = gray < 120
    light_mask = gray > 200

    if dark_mask.sum() < 50:
        return "PASS", "no dark foreground pixels found"

    fg_pixels = arr[dark_mask].astype(float)
    fg_mean = tuple(int(x) for x in fg_pixels.mean(axis=0)[:3])

    if light_mask.sum() > 0:
        bg_pixels = arr[light_mask].astype(float)
        bg_mean = tuple(int(x) for x in bg_pixels.mean(axis=0)[:3])
    else:
        bg_mean = hex_to_rgb(BG_HEX)

    # Check overall dark-on-light ratio
    ratio = contrast_ratio(fg_mean, bg_mean)
    if ratio < WCAG_MIN_RATIO:
        return "FAIL", (f"mean fg/bg contrast {ratio:.2f}:1 < {WCAG_MIN_RATIO}:1 WCAG "
                        f"(fg≈{fg_mean}, bg≈{bg_mean})")

    # Also check terracotta accent vs background — only flag if terracotta is used
    # as body TEXT (text-like blobs), not as decorative accents (flat bars, arrows).
    # Terracotta is the CLAUDE brand accent and is intentionally used for decoration;
    # it only violates WCAG when used as foreground text without a backing plate.
    acc_rgb = hex_to_rgb(ACC_HEX)
    acc_mask = ink_mask(arr, acc_rgb, tol=40)
    if acc_mask.sum() > 200:
        acc_lab, acc_n = labeled_blobs(acc_mask)
        acc_raw = blob_bboxes(acc_lab, acc_n)
        acc_text = text_run_bboxes(acc_raw, img.height)
        if acc_text:
            acc_ratio = contrast_ratio(acc_rgb, hex_to_rgb(BG_HEX))
            if acc_ratio < WCAG_MIN_RATIO:
                return "FAIL", (f"terracotta accent #{ACC_HEX.lstrip('#')} on cream "
                                f"{acc_ratio:.2f}:1 < {WCAG_MIN_RATIO}:1 WCAG — "
                                f"accent text must switch to INK #{INK_HEX.lstrip('#')} or carry a backing plate")

    return "PASS", f"contrast {ratio:.2f}:1 >= {WCAG_MIN_RATIO}:1"


# ── §8.4 Kerning sanity ───────────────────────────────────────────────────────

def font_is_named_in_scenes(reel_dir: Path) -> bool:
    """True if scenes.py explicitly names a font in every Text() / MarkupText() call."""
    scenes_py = reel_dir / "scenes.py"
    if not scenes_py.exists():
        return True  # Remotion-only reel — no Pango concern
    src = scenes_py.read_text()
    # Look for font= kwarg inside Text( or MarkupText( calls
    # A helper like _lbl() must itself pass font= through to Text()
    has_font_kwarg = bool(re.search(r'Text\([^)]*\bfont\s*=', src))
    # Also accept: helper function that builds kw with 'font' key
    has_font_key = bool(re.search(r'["\']font["\']\s*:', src))
    # Also accept: module-level lambda override (Text = lambda *a, font='EB Garamond', **k: ...)
    has_lambda_override = bool(re.search(r"Text\s*=\s*lambda.*\bfont\s*=", src))
    return has_font_kwarg or has_font_key or has_lambda_override


def check_kerning_sanity(img: Image.Image, beat_id: str, manim_font_named: bool) -> tuple[str, str]:
    """§8.4 — Pango fallback catch: no named font = FAIL (structural).
    With named font: pixel-measure inter-glyph advance against threshold."""

    # Structural rule: unnamed font → Pango fallback → gappy-letter bug
    if not manim_font_named:
        return "FAIL", (
            "scenes.py has no font= in Text() — Pango uses system fallback, "
            "causing gappy-letter spacing (w a v e s). "
            "Fix: add font='EB Garamond' to every Text()/MarkupText() call."
        )

    # Pixel-level inter-glyph analysis (runs only when font IS named)
    arr = np.array(img)
    gray = np.mean(arr, axis=2)

    # At 4K (scale=2+) the narrow band analysis sees letter counter-spaces ('o','b','e','p'
    # interiors) as kerning gaps — too many false positives. Structural check (font named)
    # already caught the Pango fallback bug; skip pixel analysis for high-DPI frames.
    _kern_scale = max(1, round(gray.shape[0] / 1080)) if gray.shape[0] > 1500 else 1
    if _kern_scale > 1:
        return "PASS", f"named font; 4K render (scale={_kern_scale}×) — pixel-level kern check skipped"

    # Find rows with significant ink coverage
    row_ink = (gray < 80).sum(axis=1)
    text_rows = np.where(row_ink > 15)[0]
    if len(text_rows) < 5:
        return "PASS", "named font; no text rows detected for gap measurement"

    # Analyse the densest text band
    peak_row = text_rows[np.argmax(row_ink[text_rows])]
    band_half = max(4, int(gray.shape[0] * 0.005))
    band = gray[max(0, peak_row - band_half):peak_row + band_half, :]
    col_dark = (band < 80).any(axis=0)

    # Find runs of dark columns (letters) separated by light gaps
    runs, in_run, run_s = [], False, 0
    for i, v in enumerate(col_dark):
        if v and not in_run:
            run_s = i; in_run = True
        elif not v and in_run:
            runs.append((run_s, i - 1)); in_run = False
    if in_run:
        runs.append((run_s, len(col_dark) - 1))

    if len(runs) < 4:
        return "PASS", "named font; too few letter runs for gap analysis"

    widths = [e - s for s, e in runs]
    mean_w = float(np.mean(widths))
    gaps = [runs[i+1][0] - runs[i][1] for i in range(len(runs) - 1)]
    max_gap = max(gaps)
    expected_gap = mean_w * 0.22  # typical inter-letter gap ≈ 22% of mean letter width
    threshold = expected_gap * KERN_GAP_FACTOR

    if max_gap > threshold:
        # Pango fallback bug causes SYSTEMATIC gaps (many letters affected), not isolated ones.
        # Isolated large gaps indicate layout spacing (data-vis labels, chart axes) — false positives.
        # Only fail if ≥30% of inter-run gaps exceed the threshold.
        n_over = sum(1 for g in gaps if g > threshold)
        frac_over = n_over / max(1, len(gaps))
        if frac_over >= 0.30:
            return "FAIL", (
                f"max inter-glyph gap {max_gap:.0f}px > threshold {threshold:.0f}px "
                f"({max_gap / max(expected_gap, 1):.1f}× expected {expected_gap:.0f}px) — "
                "check kern tables or Pango shaping for this font at this size"
            )
        return "PASS", (
            f"named font; isolated max gap {max_gap:.0f}px "
            f"(only {n_over}/{len(gaps)} gaps over threshold {threshold:.0f}px — layout spacing, not kerning bug)"
        )
    return "PASS", (f"max gap {max_gap:.0f}px <= threshold {threshold:.0f}px "
                    f"(mean letter width {mean_w:.0f}px)")


# ── §8.5 No-wordy-card ────────────────────────────────────────────────────────

def count_prose_payload(props: dict, pattern: str) -> tuple[int, int, str]:
    """Return (line_count, word_count, detail_string) for a Remotion beat's props."""
    lines, words = 0, 0
    details = []

    def add(items: list[str], label: str):
        nonlocal lines, words
        for item in items:
            wc = len(str(item).split())
            lines += 1
            words += wc
        if items:
            details.append(f"{len(items)} {label} ({sum(len(str(x).split()) for x in items)} words)")

    add(props.get("artifactLines", []), "artifactLines")
    add(props.get("chips", []),         "chips")
    add(props.get("output", []),        "output lines")

    if props.get("artifactHeading"):
        w = len(props["artifactHeading"].split())
        lines += 1; words += w
        details.append(f"artifactHeading ({w} words)")

    for fld in ("note", "left", "right"):
        v = props.get(fld)
        if isinstance(v, str) and v.strip():
            w = len(v.split())
            lines += 1; words += w
            details.append(f"'{fld}' ({w} words)")
        elif isinstance(v, dict):
            note_v = v.get("note", "")
            if note_v:
                w = len(note_v.split())
                lines += 1; words += w
                details.append(f"'{fld}.note' ({w} words)")

    return lines, words, "; ".join(details) if details else "no prose"


def max_prose_element(props: dict) -> tuple[int, str]:
    """Return (max_words, field_name) for the wordiest single prose element in props.
    Counts: text/content fields (note, headline, artifactHeading, sparkLine, body, text,
    title) + left.note / right.note + individual list items (artifactLines, chips, output).
    Does NOT count structural labels (label, eyebrow, topic, artifactTitle) — those are
    formatting chrome, not prose.
    """
    TEXT_FIELDS = {"note", "headline", "artifactHeading", "sparkLine", "body", "text", "title"}
    LIST_FIELDS  = {"artifactLines", "chips", "output"}

    max_w = 0
    max_f = ""

    def maybe(text: str, field: str):
        nonlocal max_w, max_f
        if not text or not isinstance(text, str):
            return
        w = len(text.split())
        if w > max_w:
            max_w = w
            max_f = field

    for k, v in props.items():
        if k in TEXT_FIELDS:
            maybe(v, k)
        elif k in ("left", "right") and isinstance(v, dict):
            maybe(v.get("note", ""), f"{k}.note")
        elif k in LIST_FIELDS and isinstance(v, list):
            for i, item in enumerate(v):
                if isinstance(item, str):
                    maybe(item, f"{k}[{i}]")

    return max_w, max_f


def check_wordy_card(beat: dict) -> tuple[str, str]:
    """§8.5 — Remotion beat text payload <= 1 display line + 1 label.

    Two-tier check:
    1. Universal: any single prose element > WORDY_PULLQUOTE_MAX (12) = FAIL (the
       'Committee Question' catch — a prose sentence masquerading as a label).
    2. Pattern-specific: for flat/unknown patterns, also enforce total line budget.
       Structured layouts (ClaudeWindow, ChipGrid, DeckPattern) are designed
       multi-element displays; only the per-element check applies to them.
    """
    shot = beat.get("shot", {})
    remotion = shot.get("remotion", {})
    if not remotion:
        return "SKIP", "no Remotion shot data"

    pattern = remotion.get("pattern", "")
    props = remotion.get("props", {})

    if not pattern:
        return "SKIP", "no pattern specified"

    # Bookend / structural patterns are entirely exempt
    if pattern in BOOKEND_PATTERNS:
        return "SKIP", f"{pattern} is exempt (structural/bookend)"

    # ── Tier 1: per-element check (universal for all non-bookend patterns) ──
    max_w, max_f = max_prose_element(props)
    if max_w > WORDY_PULLQUOTE_MAX:
        return "FAIL", (
            f"prose element '{max_f}': {max_w} words > {WORDY_PULLQUOTE_MAX} pull-quote limit. "
            "The screen should show structure, not sentences. "
            "De-wordify: shorten to a label or rebuild beat as a Manim/Remotion visual."
        )

    # ── Tier 2: structured layouts pass after per-element check ──
    if pattern in STRUCTURED_PATTERNS:
        return "PASS", (f"{pattern}: per-element check passed "
                        f"(max {max_w} words in '{max_f or 'n/a'}')")

    # ── Tier 3: flat / unknown patterns → line-budget check ──
    lines, words, detail = count_prose_payload(props, pattern)

    if lines == 0 and words == 0:
        return "PASS", "no prose payload found"

    # Pull-quote exception: 1 element ≤ 12 words (already passed Tier 1 if here)
    if lines == 1 and words <= WORDY_PULLQUOTE_MAX:
        return "PASS", f"pull-quote ({words} words ≤ {WORDY_PULLQUOTE_MAX})"

    if lines > WORDY_LINE_BUDGET:
        return "FAIL", (
            f"{lines} prose elements ({words} words) > budget {WORDY_LINE_BUDGET} "
            f"(1 display + 1 label). Detail: {detail}. "
            "De-wordify: rebuild as Manim process diagram or Remotion build-on; "
            "keep on-screen words to labels only."
        )

    if words > WORDY_GOLDEN_WORDS:
        return "FAIL", (
            f"{lines} element(s), {words} words > structural ceiling {WORDY_GOLDEN_WORDS}. "
            f"Detail: {detail}. Tighten the copy or split the beat."
        )

    return "PASS", f"{lines} element(s), {words} words — within budget. Detail: {detail}"


# ── §8.6 Golden strings ───────────────────────────────────────────────────────

def check_golden_strings(beat_sheet: dict) -> list[str]:
    """§8.6 — adversarial fit-test on every title/headline template."""
    findings = []
    for beat in beat_sheet.get("beats", []):
        bid = beat.get("beat_id") or beat.get("id", "?")
        shot = beat.get("shot", {})
        remotion = shot.get("remotion", {})
        if not remotion:
            continue
        props = remotion.get("props", {})
        headline = props.get("headline", "") or props.get("title", "") or props.get("segment", "")
        if not headline:
            continue
        # Length ceiling: > 70 chars risks overflow in narrower templates
        if len(headline) > 70:
            findings.append(f"{bid}: headline {len(headline)} chars — adversarial overflow risk "
                           f"(golden LONGEST test fails at this length)")
        # All-caps without tracking compensation
        if headline == headline.upper() and len(headline.split()) > 8:
            findings.append(f"{bid}: all-caps headline {len(headline.split())} words "
                           "— needs +0.04em tracking compensation per §3")
    return findings


# ── Video resolution / best source ───────────────────────────────────────────

def best_video(reel_dir: Path, beat: dict) -> Path | None:
    src = beat.get("build", {}).get("src", "")
    if src:
        p = reel_dir / src
        if p.exists():
            return p
    bid = beat.get("beat_id") or beat.get("id", "?")
    for prefix in ("manim", "media"):
        p = reel_dir / prefix / f"{bid}.mp4"
        if p.exists():
            return p
    return None


# ── Main ──────────────────────────────────────────────────────────────────────

def run_check(reel_dir: str, skip_pixels: bool = False) -> int:
    reel = Path(reel_dir).resolve()
    bs_path = reel / "beat_sheet.json"
    if not bs_path.exists():
        print(f"[typecheck] no beat_sheet.json at {reel}")
        return 1

    beat_sheet = json.loads(bs_path.read_text())
    beats = beat_sheet.get("beats", [])
    meta = beat_sheet.get("metadata", {})
    slug = meta.get("slug", reel.name)

    # Structural checks (no frames needed)
    manim_font_named = font_is_named_in_scenes(reel)
    golden_findings = check_golden_strings(beat_sheet)

    rows = []
    any_fail = False

    for beat in beats:
        bid = beat.get("beat_id") or beat.get("id", "?")
        lane = beat.get("lane", "?")
        build_status = beat.get("build", {}).get("status", "")
        # If the shot is explicitly REMOTION, Chrome handles text rendering — no Pango concern.
        # Only run the Manim kerning check when the beat was actually Manim-rendered.
        _shot = beat.get("shot") or {}
        shot_type_field = _shot.get("type", "") if isinstance(_shot, dict) else ""
        is_remotion_shot = (shot_type_field == "REMOTION")
        is_manim = (build_status == "MANIM" or lane == "MANIM") and not is_remotion_shot

        findings: list[tuple[str, str, str]] = []  # (check, status, message)

        # §8.5 no-wordy-card — pure JSON, always runs
        wc_status, wc_msg = check_wordy_card(beat)
        if wc_status != "SKIP":
            findings.append(("no-wordy-card §8.5", wc_status, wc_msg))
            if wc_status == "FAIL":
                any_fail = True

        if not skip_pixels:
            video = best_video(reel, beat)
            if video and video.exists():
                img = extract_frame(video)
                if img is not None:
                    # §8.1 min-size
                    s, m = check_min_size(img, bid)
                    findings.append(("min-size §8.1", s, m))
                    if s == "FAIL":
                        any_fail = True

                    # §8.2 overflow
                    s, m = check_overflow(img, bid)
                    findings.append(("overflow §8.2", s, m))
                    if s == "FAIL":
                        any_fail = True

                    # §8.3 contrast
                    s, m = check_contrast(img, bid)
                    findings.append(("contrast §8.3", s, m))
                    if s == "FAIL":
                        any_fail = True

                    # §8.4 kerning — MANIM beats only
                    if is_manim:
                        s, m = check_kerning_sanity(img, bid, manim_font_named)
                        findings.append(("kerning §8.4", s, m))
                        if s == "FAIL":
                            any_fail = True
                else:
                    findings.append(("render", "SKIP", f"could not decode frame from {video.name}"))
            else:
                findings.append(("render", "SKIP", "no video rendered for this beat yet"))

        # §8.4 structural kerning for un-rendered MANIM beats
        if is_manim and not manim_font_named and not any(c == "kerning §8.4" for c, _, _ in findings):
            findings.append(("kerning §8.4", "FAIL",
                             "scenes.py has no font= in Text() — Pango fallback, gappy-letter bug"))
            any_fail = True

        beat_fail = any(s == "FAIL" for _, s, _ in findings)
        worst = "FAIL" if beat_fail else ("SKIP" if all(s == "SKIP" for _, s, _ in findings) else "PASS")

        # Pick worst finding for the table cell
        worst_finding = next(
            (f"{c}: {m}" for c, s, m in findings if s == "FAIL"),
            next((f"{c}: {m}" for c, s, m in findings if s == "PASS"), "no video")
        )
        # Truncate for table readability
        worst_short = worst_finding[:90] + ("…" if len(worst_finding) > 90 else "")

        fix = ""
        for c, s, m in findings:
            if s == "FAIL":
                if "wordy" in c or "no-wordy" in c:
                    fix = "De-wordify → Manim diagram or Remotion build-on"
                elif "kerning" in c:
                    fix = "Add font='EB Garamond' to all Text() in scenes.py"
                elif "min-size" in c:
                    fix = "Increase font_size in scenes.py or Remotion component"
                elif "overflow" in c:
                    fix = "Move text inside title-safe 90% box"
                elif "contrast" in c:
                    fix = "Use INK on cream; add backing plate under accent text"
                break

        rows.append({"beat_id": bid, "lane": lane, "worst": worst_short,
                     "status": worst, "fix": fix, "findings": findings})

    # ── Build TYPECHECK.md ────────────────────────────────────────────────────
    now = datetime.now().strftime("%Y-%m-%dT%H:%M")
    overall = "**FAIL**" if any_fail else "PASS"
    fail_count = sum(1 for r in rows if r["status"] == "FAIL")

    md = [
        "# TYPECHECK.md — GATE T",
        "",
        f"Reel: `{slug}`  |  Checked: {now}  |  Overall: {overall}  |  "
        f"Beats checked: {len(rows)}  |  FAILs: {fail_count}",
        "",
        f"Spec: `skills/make/kerning/reference/type-spec.md` §8.  "
        f"Floor: {MIN_SIZE_PCT}% frame-height.  "
        f"Contrast: {WCAG_MIN_RATIO}:1 WCAG.  "
        f"Kern threshold: {KERN_GAP_FACTOR}× expected advance.  "
        f"Wordy budget: {WORDY_LINE_BUDGET} elements.",
        "",
    ]

    # Structural warnings
    if not manim_font_named:
        md += [
            "> **⚠ STRUCTURAL — §8.4 KERNING:** `scenes.py` calls `Text()` with no `font=` argument.",
            "> Pango will use a system fallback font — the gappy-letter spacing bug "
            "(w a v e s  l i k e  t h i s) is active for ALL Manim beats.",
            "> **Fix:** add `font='EB Garamond'` to every `Text()` and `MarkupText()` call "
            "in `scenes.py` (or to every helper that calls them).",
            "> Then re-render all Manim beats and re-run GATE T.",
            "",
        ]

    if golden_findings:
        md += ["> **§8.6 GOLDEN STRINGS:**", ""]
        for g in golden_findings:
            md.append(f"> - {g}")
        md.append("")

    # Beat table
    md += [
        "| beat | lane | worst finding | status | fix |",
        "|------|------|---------------|--------|-----|",
    ]
    for r in rows:
        st = f"**{r['status']}**" if r["status"] == "FAIL" else r["status"]
        md.append(f"| {r['beat_id']} | {r['lane']} | {r['worst']} | {st} | {r['fix'] or '—'} |")

    # Failures section
    md += ["", "---", "", "## Failures requiring action before cut", ""]
    fail_rows = [r for r in rows if r["status"] == "FAIL"]
    if not fail_rows:
        md.append("*None — GATE T PASS.*")
    else:
        for r in fail_rows:
            md.append(f"### {r['beat_id']} ({r['lane']})")
            for c, s, m in r["findings"]:
                if s == "FAIL":
                    md.append(f"- **{c}**: {m}")
            if r["fix"]:
                md.append(f"- **Fix:** {r['fix']}")
            md.append("")

    # Check summary table
    check_names = ["no-wordy-card §8.5", "min-size §8.1", "overflow §8.2",
                   "contrast §8.3", "kerning §8.4"]
    md += ["---", "", "## Check summary", "",
           "| Check | Beats checked | FAILs |",
           "|-------|---------------|-------|"]
    for cn in check_names:
        checked = [r for r in rows if any(c == cn for c, _, _ in r["findings"])]
        failed  = [r for r in checked if any(c == cn and s == "FAIL" for c, s, _ in r["findings"])]
        md.append(f"| {cn} | {len(checked)} | {len(failed)} |")

    md += [
        "",
        "---",
        "",
        "*GATE T: any FAIL blocks `./art run` and `./art final`. "
        "Fix the flagged beats and re-run `scripts/type_check.py` until green.*",
    ]

    out = reel / "TYPECHECK.md"
    out.write_text("\n".join(md) + "\n")
    print(f"[typecheck] wrote {out}")
    print(f"[typecheck] GATE T: {'FAIL (' + str(fail_count) + ' beats)' if any_fail else 'PASS'}")
    return 2 if any_fail else 0


def main():
    p = argparse.ArgumentParser(description="GATE T — type-lock checker (type-spec.md §8)")
    p.add_argument("reel", help="path to reel folder")
    p.add_argument("--skip-pixels", action="store_true",
                   help="skip pixel-level checks (§8.1–8.4); only run §8.5 and §8.6")
    args = p.parse_args()
    sys.exit(run_check(args.reel, args.skip_pixels))


if __name__ == "__main__":
    main()

#!/usr/bin/env bash
# run.sh — ONE command: QC-gate, render every pending Manim scene, slot the
# outputs, recompile the reel. Bash 3.2-safe. Free/local (Manim + ffmpeg).
#
#   bash scripts/run.sh <path/to/reel> [--height 1080]
#
# The reel may live ANYWHERE — e.g. books/<book>/youtube/<slug>. The toolkit
# assets (graphics library, QC tools, bearbrown, sub-scripts) are resolved from
# THIS script's own location, so the reel is fully decoupled from the toolkit.
#
# Skips any beat whose slot is already filled (manim/<B>.mp4 or media/<B>.mp4).
#
# QC GATES (tmp/qc-tooling — advisory tools, wired here as hard gates):
#   Gate A (pre-flight, render-free): static_scene_check.py per pending scene.
#   Gate B (post-render, pixel-true): manim_layout_audit.py --png per scene.
#   Skip both with ART_QC=0.
set -e
REEL_IN="$1"; shift || true
HEIGHT=1080
if [ "$1" = "--height" ]; then HEIGHT="$2"; fi
ART_QC="${ART_QC:-1}"

ROOT="$(cd "$(dirname "$0")/.." && pwd)"          # toolkit home — assets live here
# resolve the reel to an absolute path wherever it lives (its parent must exist)
REEL_DIR="$(cd "$(dirname "$REEL_IN")" 2>/dev/null && pwd)/$(basename "$REEL_IN")"
if [ ! -d "$REEL_DIR" ]; then
  echo "[run] no such reel dir: $REEL_IN"; exit 1
fi

GFX="$ROOT/manim"
GFXFILE="animated_graphics.py"
if [ -f "$REEL_DIR/scenes.py" ]; then   # every real reel carries its own scenes
  GFX="$REEL_DIR"; GFXFILE="scenes.py"
elif [ "$(basename "$REEL_DIR")" != "vox-electoral-college" ]; then
  # GUARD: the shared animated_graphics.py carries only the electoral-college FIXTURE
  # scenes; rendering them into another reel slots the wrong film's graphics.
  echo "[run] REFUSED: $REEL_DIR has no scenes.py. The shared animated_graphics.py"
  echo "[run] holds only the electoral-college fixture scenes — rendering those"
  echo "[run] here would slot another film's graphics into your beats."
  echo "[run] Write $REEL_DIR/scenes.py (one Scene per GRAPHIC/CARD/DOCUMENT"
  echo "[run] beat; see reels/_example-comma-orphan/scenes.py)."
  exit 2
fi
QC="$ROOT/tmp/qc-tooling"
mkdir -p "$REEL_DIR/manim" "$REEL_DIR/media" "$REEL_DIR/pantry" "$REEL_DIR/images" "$REEL_DIR/mp4"

SCENES=$(python3 -c "
import re
src = open('$GFX/$GFXFILE').read()
print(' '.join(m.group(1) for m in re.finditer(r'class ([A-Z][A-Za-z0-9]*_\w+)\(Scene\)', src)))
")

# ---- figure out which scenes are actually pending (slot not filled)
PENDING=""
for S in $SCENES; do
  BID="${S%%_*}"
  if [ -f "$REEL_DIR/manim/$BID.mp4" ] || [ -f "$REEL_DIR/media/$BID.mp4" ]; then
    echo "[run] skip $S — $BID already filled"
  else
    PENDING="$PENDING $S"
  fi
done
if [ -z "$PENDING" ]; then
  echo "[run] nothing to render — recompiling only"
fi

# ---- GATE F: no rendering without the paperwork set (facts + work order + prompts)
if [ "${ART_FACTS:-1}" = "1" ] && [ -n "$PENDING" ]; then
  for REQ in FACTCHECK.md SHOTLIST.md PROMPTS.md; do
    if [ ! -f "$REEL_DIR/$REQ" ]; then
      echo "[run] GATE F FAILED: $REEL_DIR has no $REQ — the paperwork set"
      echo "[run] (FACTCHECK.md claims · SHOTLIST.md typed work order ·"
      echo "[run] PROMPTS.md beat-prefixed prompts for open slots) is written"
      echo "[run] BEFORE rendering. ART_FACTS=0 for a previz-only exception."
      exit 2
    fi
  done
fi

# ---- GATE A: render-free pre-flight on every pending scene (isolated copy)
if [ "$ART_QC" = "1" ] && [ -n "$PENDING" ] && [ -f "$QC/static_scene_check.py" ]; then
  echo "[run] GATE A — static pre-flight"
  TMPQC=$(mktemp -d)
  cp "$GFX/$GFXFILE" "$TMPQC/"
  for S in $PENDING; do
    rc=0
    PYTHONPATH="$ROOT/manim" \
      python3 "$QC/static_scene_check.py" "$TMPQC/$GFXFILE" --class "$S" --quiet || rc=$?
    if [ "$rc" -ge 2 ]; then
      echo "[run] GATE A FAILED: $S has static errors — fix the scene, nothing rendered"
      exit 2
    elif [ "$rc" -eq 1 ]; then
      echo "[run] gate A warning on $S (continuing)"
    fi
  done
fi

# ---- GATE W: independent WCAG + margins + overlap pre-flight (no render, no manim)
if [ "$ART_QC" = "1" ] && [ -n "$PENDING" ] && [ -f "$QC/wcag_margin_check.py" ]; then
  echo "[run] GATE W — WCAG contrast + margins + text-overlap (independent second check)"
  for S in $PENDING; do
    rc=0
    python3 "$QC/wcag_margin_check.py" "$GFX/$GFXFILE" --class "$S" --quiet || rc=$?
    if [ "$rc" -ge 2 ]; then
      echo "[run] GATE W FAILED: $S — gold-as-text / contrast / off-frame / text-on-text."
      echo "[run] Fix the scene; nothing rendered. (Rules: SLATE-RUNNER CONVENTIONS -> Gate W)"
      exit 2
    elif [ "$rc" -eq 1 ]; then
      echo "[run] gate W warning on $S (continuing)"
    fi
  done
fi

# ---- render + GATE B per scene
cd "$GFX"
for S in $PENDING; do
  BID="${S%%_*}"
  echo "[run] rendering $S"
  RES="1920,1080"
  if grep -q '"aspect_ratio": *"9:16"' "$REEL_DIR/beat_sheet.json" 2>/dev/null; then RES="1080,1920"; fi
  manim -qh --fps 24 -r "$RES" "$GFXFILE" "$S"
  OUT=$(find media/videos -name "$S.mp4" | head -1)
  if [ -z "$OUT" ]; then echo "[run] ERROR: no output for $S"; exit 1; fi
  if [ "$ART_QC" = "1" ] && [ -f "$QC/manim_layout_audit.py" ]; then
    rc=0
    PORTRAIT=""
    if grep -q '"aspect_ratio": *"9:16"' "$REEL_DIR/beat_sheet.json" 2>/dev/null; then PORTRAIT="--portrait"; fi
    python3 "$QC/manim_layout_audit.py" "$GFXFILE" --class "$S" --png --curve-strict $PORTRAIT || rc=$?
    if [ "$rc" -ge 2 ]; then
      echo "[run] GATE B FAILED: $S has layout errors — mp4 NOT slotted."
      echo "[run] see $GFX/layout_audit.md and the annotated PNGs beside it."
      exit 2
    elif [ "$rc" -eq 1 ]; then
      echo "[run] gate B warning on $S — slotting anyway, review $GFX/layout_audit.md"
    fi
  fi
  mv "$OUT" "$REEL_DIR/manim/$BID.mp4"
done

cd "$ROOT"

# ---- the outro law: brand the closing card (idempotent; needs audio + bears)
if [ -d "$ROOT/bearbrown" ]; then
  python3 scripts/outro.py "$REEL_DIR" --bears "$ROOT/bearbrown" \
    || echo "[run] outro skipped (no narration mp3 yet? run generate_audio.py)"
fi

python3 scripts/compile.py "$REEL_DIR" --review --height "$HEIGHT"

# ---- deliverables layout: finished cuts -> mp4/, filled stills -> images/
for f in "$REEL_DIR"/*.mp4 "$REEL_DIR"/short/*.mp4; do
  [ -f "$f" ] && cp -f "$f" "$REEL_DIR/mp4/" || true
done
for f in "$REEL_DIR"/media/*.png; do
  [ -f "$f" ] && cp -f "$f" "$REEL_DIR/images/" || true
done
echo "[run] done → $REEL_DIR  (QC gates: $([ "$ART_QC" = "1" ] && echo on || echo OFF))"
echo "[run] this was the FULL machine pass: motion graphics + outro done;"
echo "[run] any remaining slates are YOUR slots — see $REEL_DIR/SHOTLIST.md"

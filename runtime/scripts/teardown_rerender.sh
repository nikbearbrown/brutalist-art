#!/usr/bin/env bash
# teardown_rerender.sh — Re-render all 22 nbb/ Manim beats in teardown palette.
#
# Problem: nbb/manim/B03.mp4 (and B07, B11 in ch1) were symlinks to the Medhavy
# parent's renders — cream bg, green curves. This script:
#   1. Deletes each symlink in nbb/manim/
#   2. Re-renders from the parent reel's scenes.py with ART_PALETTE=teardown
#   3. Recompiles each nbb/ reel with compile.py → nbb/mp4/
#
# Run from books/:
#   bash runtime/scripts/teardown_rerender.sh
#
# Per-beat mp3/ audio is already rendered — do NOT re-run generate_audio.py.
set -e
BOOKS="$(cd "$(dirname "$0")/../.." && pwd)"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
python3 "$ROOT/scripts/teardown_rerender.py" "$BOOKS" "$ROOT" "$@"

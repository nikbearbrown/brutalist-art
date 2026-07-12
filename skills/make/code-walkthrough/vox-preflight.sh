#!/usr/bin/env bash
# vox-preflight.sh — verify a machine can build vox simulation videos.
# Run it from the folder that holds vox/ (your books/ parent), or pass that path:
#   bash vox-preflight.sh                 # uses the current folder
#   bash vox-preflight.sh /path/to/books  # explicit
# It only READS and runs a no-network Gate A. It installs nothing and spends nothing.

set -u
BOOKS="${1:-$PWD}"
VOX="$BOOKS/vox"
pass=0; fail=0
ok()   { printf "  \033[32mOK\033[0m   %s\n" "$1"; pass=$((pass+1)); }
bad()  { printf "  \033[31mFAIL\033[0m %s\n" "$1"; fail=$((fail+1)); }
info() { printf "\n\033[1m%s\033[0m\n" "$1"; }

info "0. Layout — vox/ must sit beside your book folders"
if [ -d "$VOX" ]; then ok "found $VOX"; else bad "no vox/ under $BOOKS — clone it here (see the guide)"; fi

info "1. Python 3 + render libraries"
if command -v python3 >/dev/null; then ok "python3: $(python3 --version 2>&1)"; else bad "python3 not on PATH"; fi
for m in manim PIL numpy requests mutagen; do
  if python3 -c "import $m" 2>/dev/null; then ok "python import: $m"; else bad "python import: $m  (pip install)"; fi
done

info "2. ffmpeg (the compositor)"
if command -v ffmpeg >/dev/null; then ok "ffmpeg: $(ffmpeg -version 2>/dev/null | head -1)"; else bad "ffmpeg not found  (brew install ffmpeg)"; fi

info "3. House fonts (all four must register, or renders silently use the wrong font)"
for f in garamond inter montserrat "pt mono"; do
  if fc-list 2>/dev/null | grep -iq "$f"; then ok "font: $f"; else bad "font missing: $f  (copy vox/fonts into ~/Library/Fonts)"; fi
done

info "4. ElevenLabs key (narration)"
if [ -f "$VOX/.env" ]; then
  if grep -q '^ELEVENLABS_API_KEY=' "$VOX/.env" && ! grep -q '^ELEVENLABS_API_KEY=your-elevenlabs-api-key' "$VOX/.env"; then
    ok "vox/.env has ELEVENLABS_API_KEY set"
  else
    bad "vox/.env exists but ELEVENLABS_API_KEY is still the placeholder"
  fi
else
  bad "no vox/.env  (cp vox/.env.example vox/.env, then add your key)"
fi

info "5. Node lane (the Onda terminal + code-block beats that a sim reel uses)"
if command -v node >/dev/null; then ok "node: $(node -v)"; else bad "node not found  (brew install node)"; fi
if [ -d "$VOX/aspects/remotion-pass/remotion/node_modules" ]; then
  ok "remotion node_modules present"
else
  bad "remotion deps not installed  (cd vox/aspects/remotion-pass/remotion && npm install)"
fi

info "6. Gate A smoke test on the bundled example (no network, no render)"
EX="$VOX/reels/_example-comma-orphan/vox_scenes.py"
if [ -f "$EX" ]; then
  T=$(mktemp -d); cp "$EX" "$T/"
  if PYTHONPATH="$VOX/aspects/explainer/vox-explainer/manim" \
       python3 "$VOX/tmp/qc-tooling/static_scene_check.py" "$T/vox_scenes.py" --class B04_TwoTables >/dev/null 2>&1; then
    ok "Gate A passed on the example scene"
  else
    bad "Gate A errored — the QC toolchain isn't wired up (check PYTHONPATH / deps above)"
  fi
  rm -rf "$T"
else
  bad "bundled example not found at $EX"
fi

info "Summary"
printf "  %s checks passed, %s failed\n" "$pass" "$fail"
if [ "$fail" -eq 0 ]; then
  printf "  \033[32mReady.\033[0m You can build simulation reels.\n"; exit 0
else
  printf "  \033[31mNot ready.\033[0m Fix the FAIL lines above, then re-run.\n"; exit 1
fi

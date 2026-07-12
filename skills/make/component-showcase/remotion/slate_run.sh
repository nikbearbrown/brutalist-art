#!/usr/bin/env bash
# slate_run.sh — run Claude Code over AUTORUN.md, looping until BOTH masters exist.
# Each pass is a fresh autonomous Claude Code turn that reads AUTORUN.md, runs the pipeline,
# fixes any error, and continues. The loop re-launches until the 16:9 and 9:16 outputs are on
# disk, so a mid-render crash or an exhausted turn just triggers another pass instead of stopping.
set -u
P="$ART_HOME/skills/make/component-showcase/remotion"
L="$P/out/brutalist-onda-41-59.mp4"
S="$P/out/brutalist-onda-41-59-short.mp4"
cd "$P" || { echo "cannot cd to $P"; exit 1; }

pass=0
while :; do
  if [ -s "$L" ] && [ -s "$S" ]; then
    echo "✅ slate run complete — both masters exist:"
    echo "   $L"
    echo "   $S"
    break
  fi
  pass=$((pass + 1))
  echo "──────── slate run · pass $pass · $(date '+%Y-%m-%d %H:%M:%S') ────────"
  claude --dangerously-skip-permissions \
    -p "Read AUTORUN.md in $P and execute it to completion. Do not stop until both '$L' and '$S' exist, are non-empty, and rendered with zero errors, and the 16:9 is published to the Brutalist playlist. Diagnose and fix any error yourself. Absolute paths only."
  echo "──────── pass $pass returned; re-checking outputs ────────"
  sleep 2
done

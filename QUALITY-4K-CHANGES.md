# Brutalist pipeline: 4K-native + encoder-quality pass

Goal: renders that stay crisp **after** YouTube's VP9/AV1 re-compression — driven by (1) uploading at 4K so YouTube gives the video its richer bitrate ladder, and (2) not baking in generation loss before the file ever leaves the toolkit.

Seven files changed. All parse on your toolchain. Nothing else preserved — you said recompiles are fine.

## What changed and why

**`runtime/scripts/run.sh`** — the render driver
- `HEIGHT=1080` → **`HEIGHT=2160`** (masters compile at 4K).
- Manim now renders true 4K: `RES` `1920,1080`→`3840,2160` (and `1080,1920`→`2160,3840` for 9:16), and `manim -qh` → **`-qk`**.

**`runtime/scripts/remotion_scenes.py`** — the Remotion scene renderer
- Added **`--scale=2`** (the 1920×1080 comps now render at true 3840×2160, supersampled).
- Added **`--image-format=png`** — this kills Remotion's default **JPEG-q80 frame step**, the hidden quality ceiling that was softening flat brand color and text *before* any encode. This is the single biggest text-crispness win and it helps at any resolution.
- Added **`--crf=16`**.

**`runtime/scripts/compile.py`** — the assembler (this is where the triple-generation loss lived)
- Per-clip normalize: `veryfast`/`crf 20` → **`medium`/`crf 12`**. Near-visually-lossless, so this pass stops being a real generation of loss.
- Final concat/encode: `veryfast`/`crf 20` → **`slow`/`crf 16`**. This is now the *only* meaningful lossy step. `veryfast` was the biggest avoidable loss in the whole chain.

**`runtime/scripts/shorts.py`** and **`runtime/scripts/outro.py`** — `veryfast`/`crf 20` → **`slow`/`crf 16`** at their encode points.

**`runtime/scripts/capture_sim.py`** — screen-capture input encode `fast`/`crf 22` → **`slow`/`crf 18`**.

**`art`** — `art final` default `--height 1080` → **`2160`**.

## Two honest caveats

1. **I could not test-render this.** My sandbox has no GPU, Remotion, or Manim. The edits are surgical and parse cleanly, but 4K Manim (`-qk`) is much slower and more memory-hungry than 1080, and Remotion at `--scale=2` is 4× the pixels. **Test on one or two videos before recompiling all 70** — watch for Manim OOM on the heaviest scenes.

2. **Brand cards are not native 4K yet.** The outro card and the shorts title cards are drawn with PIL at 1080/1080×1920 and get upscaled to 2160 by compile. On bold logo/title graphics that's nearly invisible, so I left them — making them native 4K means rescaling absolute PIL font/line sizes, which is its own tested pass. The *content* scenes (Manim + Remotion, where text crispness actually matters) are true 4K. `render.py` (the deck/lecture tool) is a separate subsystem and was left alone — flag it if you want decks at 4K too.

## Test one video, then batch

Because `run.sh` skips any beat whose clip already exists, the cached 1080 renders must be cleared so they re-render at 4K.

1. Review the diff:
   `cd brutalist-art && git diff -- runtime/scripts/ art`
2. Pick one reel, clear its cached renders, recompile:
   `rm -f <book>/youtube/<slug>/manim/*.mp4 <book>/youtube/<slug>/media/*.mp4`
   `./brutalist-art/art run <book>/youtube/<slug>`
3. Verify it's actually 4K and crisp:
   `ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0 <book>/youtube/<slug>/<slug>.mp4`  → should read `3840,2160`
4. If it looks right, do the rest. Recompiling visuals is **free and local** (Manim + Remotion + ffmpeg) — narration audio is cached, so no ElevenLabs spend. It's just slow at 4K.

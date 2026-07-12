# AUTORUN — render the full Onda series (16:9 + 9:16) and publish

You are Claude Code on Bear's Mac, working directory
`$ART_HOME/skills/make/component-showcase/remotion` (= `$PROJECT` below).

**Goal:** produce **six finished masters** — the three Onda videos, each in **16:9 and 9:16** —
so Bear can watch all of them, and publish each 16:9 to the **Brutalist** playlist. Run fully
autonomously: run each step; on any error, read it, fix the code/config, and re-run that step.
**Do not stop until the DONE criteria hold. Do not ask questions. Absolute paths only.**

## Paths
- `$PROJECT` = `$ART_HOME/skills/make/component-showcase/remotion`
- remotion bin = `$PROJECT/node_modules/.bin/remotion`
- outputs go in `$PROJECT/out/`

## The three videos
| # | --start-num | slugs (comma-separated, in order) | 16:9 output | 9:16 output |
|---|---|---|---|---|
| 1 | 1  | `bar-chart,count-up,line-chart,pie-reveal,progress-bar,timeline,title-card,lower-third,stat-card,quote-card,chapter-card,end-card,underline,highlight,callout,draw-on,icon-pop,shimmer-sweep,text-fade-replace,mesh-gradient` | `out/brutalist-onda-01-20.mp4` | `out/brutalist-onda-01-20-short.mp4` |
| 2 | 21 | `fade-in,fade-out,slide-in,slide-out,scale-in,rotate-in,blur-reveal,mask-reveal,image-reveal,tracking-in,typewriter,word-rotate,word-stagger,slot-machine-roll,marquee,ken-burns,parallax,spotlight,spotlight-card,stagger-group` | `out/brutalist-onda-21-40.mp4` | `out/brutalist-onda-21-40-short.mp4` |
| 3 | 41 | `terminal,code-block,code-diff,matrix-decode,node-graph,dynamic-grid,progress-steps,split-screen,video-clip,audio-clip,audio-visualizer,captions,pulsing-indicator,confetti,rgb-glitch-text,gradient-shift,grain-overlay,vignette,camera-shake` | `out/brutalist-onda-41-59.mp4` | `out/brutalist-onda-41-59-short.mp4` |

## One-time setup (do this first)
Add a portrait composition to `src/Root.tsx` if it isn't already there:
```tsx
<Composition id="tour-data-9x16" component={RiffTour} width={1080} height={1920} fps={TOUR_FPS} durationInFrames={TOUR_FRAMES} />
```
`RiffTour` reads `beats/templates-onda.conformed.json` — the same sheet `tour-data` uses — so the
portrait composition automatically renders whichever video is current. `RiffTour` is mostly
`AbsoluteFill` with a top label band and a bottom caption band; it should read in portrait. Only
touch paddings in `src/riff/RiffTour.tsx` / `src/riff/BeatCaption.tsx` if the label or captions
clip. Keep the teardown palette and the top-label / bottom-caption structure. After the first
portrait render, check a frame (`remotion still ... tour-data-9x16 ... --frame 1600`) and fix
clipping before moving on.

## Per-video procedure
The beat sheet and audio are **shared/transient** (one filename, overwritten per video), so
**finish one video's two renders before starting the next.** For each video with start-num `N`
and slug list `S`:
1. `python3 $PROJECT/scripts/onda_catalog.py --start-num N --slugs S`
2. `python3 $PROJECT/scripts/riff_audio.py $PROJECT/beats/templates-onda.beats.json`  (re-voices this video — required because step 1 regenerated the sheet)
3. `python3 $PROJECT/scripts/riff_conform.py $PROJECT/beats/templates-onda.beats.json`
4. `python3 $PROJECT/scripts/riff_gate.py $PROJECT/beats/templates-onda.conformed.json`
5. render 16:9: `$PROJECT/node_modules/.bin/remotion render $PROJECT/src/index.ts tour-data $PROJECT/out/<this video's 16:9 name>.mp4`
6. render 9:16: `$PROJECT/node_modules/.bin/remotion render $PROJECT/src/index.ts tour-data-9x16 $PROJECT/out/<this video's 9:16 name>.mp4`
7. publish the 16:9: `python3 $PROJECT/scripts/riff_publish.py --video $PROJECT/out/<this video's 16:9 name>.mp4 --run`  (the ledger dedups, so an already-published video is skipped safely)

## Known-good facts — do NOT re-litigate
- `remotion.config.ts` pins the project root as an **absolute** path — keep it. `process.cwd()` / `__dirname` both resolve wrong and cause `Field 'browser' doesn't contain a valid alias configuration`.
- The zod **"installed 3.25.76 vs required 4.3.6" banner is NON-FATAL.** Ignore it.
- React error #130 = a component resolved to `undefined`. `onda_catalog.py` resolves each component export by PascalCase(slug); fix `export_names()` / the registry, do not guess props.
- `publish-workspace/client_secret.json`, `youtube_token.json`, `youtube_publish_ledger.json` are real OAuth **secrets** — never print, commit, or move them.

## DONE when ALL of these hold
All six files exist in `$PROJECT/out/`, each non-empty and rendered with **zero frame errors**:
`brutalist-onda-01-20.mp4`, `brutalist-onda-01-20-short.mp4`,
`brutalist-onda-21-40.mp4`, `brutalist-onda-21-40-short.mp4`,
`brutalist-onda-41-59.mp4`, `brutalist-onda-41-59-short.mp4`,
and each 16:9 published (a `https://youtu.be/...` URL printed for each, or skipped as already in the ledger).

Then print the six output paths and the YouTube URLs so Bear can look at them.

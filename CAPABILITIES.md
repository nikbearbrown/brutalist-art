# CAPABILITIES — what each video type needs

One row per video type: what it makes, the keys it needs, the installs beyond the
core, the rough cost per run, the example that teaches it, and the **one thing the
human must supply that the CLI cannot generate**. `./setup` checks all of this live;
this table is the at-a-glance version. Cost legend: **free** · **$** ElevenLabs
narration · **$$** AI image/video (higgsfield CLI).

| Video type (skill) | Makes | Keys | Installs beyond core | Cost | Example | Human must supply |
|---|---|---|---|---|---|---|
| **previz** | A watchable timing pass: every beat a slate/request card | none | ffmpeg, Pillow | free | *(any beat sheet)* | the beat sheet (script) |
| **slate-cut** | The zero-key first cut; ungeneratable beats become request cards with prompts | none | ffmpeg, Pillow | free | `slate-cut--base-rate` | the beat sheet |
| **sketch-explainer** | MinutePhysics sketch explainer; silent, or narrated | ELEVENLABS* | Manim (+LaTeX for math) | free→$ | *(to add, Phase 5)* | the concept + narration approval |
| **math-explainer** | 3Blue1Brown-style pure-Manim explainer | ELEVENLABS | Manim, LaTeX | $ | *(to add)* | the concept + which derivations to show |
| **explainer** | Flagship: each beat's mp4 from the best tool (Manim / Remotion / AI video / stills), composited | ELEVENLABS (+higgsfield for AI beats) | Manim, Node/Remotion | $→$$ | `explainer--size-paradox` | the script; real footage/AI clips for capture beats |
| **bio** | Narrated biography (`--length`, default 3:00) | ELEVENLABS (+higgsfield for photoreal) | Manim | $→$$ | *(to add)* | the subject write-up; real photos if wanted |
| **code-walkthrough** | "Build it with Claude Code + Manim" reel | ELEVENLABS | Manim, Node/Remotion | $ | *(to add)* | the code/story to walk through |
| **recitation-film** | Film of a spoken-word literary recitation | ELEVENLABS | Manim, Node/Remotion, faster-whisper | $ | *(to add)* | the recitation audio (the performance is the clock) |
| **kids-video** | Ages 1–5 concept film, dev-psych gated | ELEVENLABS | Manim | $ | *(to add)* | the concept + age target |
| **music-video** | Beat-synced music video from your WAV + lyrics | none | librosa, Node/Remotion | free | `music-video--c-is-for-cookie` | **the song (WAV) + lyrics** |
| **lyric-overlay** | Karaoke lyrics + audiogram over a finished video | none | faster-whisper, Node/Remotion | free | *(to add)* | the finished video + lyrics |
| **lyric-resync** | Re-cut a video so each beat matches its lyric (image-to-video) | higgsfield | jq | $$ | *(to add)* | the source video + lyrics |
| **dance-video** | A character dancing on the beat | higgsfield | jq | $$ | *(to add)* | the song + a character reference |
| **story-film** | Story → narrated AI film, one beat per scene | ELEVENLABS + higgsfield | jq | $$ | `00-story-film-demos` | the story/script |
| **terminal-screencast** | CLI video: terminal in, animated output out | ELEVENLABS | Node/Remotion | $ | `terminal-screencast--compression-journey` | the terminal session to feature |
| **ai-asset-gen** | Images/video/3D/audio via the higgsfield CLI | higgsfield | jq | $$ | — | the prompt/brief |
| **line-art-vectorizer** | Clean SVGs from B/W line art | none | vtracer | free | — | the line-art image |
| **figure-planner** | Figure plans + SVG→PNG rendering | none | Node (sharp) | free | — | the chapter/prose to plan figures for |
| **youtube-publisher** | Publishes to YouTube: transcript, timestamped description, bookends | YouTube OAuth (free quota) | faster-whisper, Node/Remotion | free | — | the finished mp4(s) + channel authorization |

\* `sketch-explainer` runs **silent with no key**; narration adds `ELEVENLABS_API_KEY`.

## The human/AI division (every skill)

The CLI does the technical build — it generates every piece of media it can (Manim,
Remotion, or another tool) and composites per beat. For media it **cannot** fake — a
real capture, archival footage, a performance, a gen-AI clip — it emits a **request
card** naming the beat and (for AI/historical beats) a suggested prompt or search
terms. You drop the real media into `pantry/`; the tool checks it, strips sound if
needed, cuts or extends it to the beat, renames it, and slots it into the composite.

Query what a given reel still needs, and how, with the beat ledger:

```bash
./art todo <reel> --open                       # every unfilled beat, with prompts
./art todo <reel> --method animated_graphics   # beats the pipeline should animate
```

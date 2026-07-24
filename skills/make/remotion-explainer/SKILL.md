---
name: remotion-explainer
description: >
  Turn textbook material — a chapter, a section, or a single concept — into
  a short Remotion explainer video. Cajal's scope-before-spectacle
  discipline applied to motion: scan for concepts worth a video, storyboard
  a blueprint, generate per-beat Remotion scenes, and hand off the audio +
  render commands. Silent/captioned by default; ElevenLabs narration is an
  opt-in upgrade. Use when asked to make a tutorial video, an explainer, a
  "little video for this concept," or to turn a chapter into video.
metadata:
  tags: remotion, education, textbook, tutorial, cajal, explainer, voiceover, elevenlabs, video
---

# Muybridge

The cajal figure skill scans chapters and renders the *static* figures a concept needs. This skill does the same for **motion**: it turns one textbook concept into a short (60–120s) Remotion explainer — the moving-picture sibling of a cajal figure. (The name is for Eadweard Muybridge, who first broke motion into frames.) Same discipline: **scope before spectacle, one idea per artifact, every visual answers the narration.**

Always load `remotion-best-practices` before writing any Remotion code.

## What this skill produces — and what it does not

It produces, in order: a **blueprint** (the script), the **Remotion scene files**, a **reel** that sequences them, the **Root.tsx registration**, and the exact **commands** to generate audio and render.

It does **not** itself render the MP4 or call ElevenLabs. A skill is a prompt; rendering needs headless Chromium and minutes of compute, and narration needs an API key and quota. So this skill stops at "a runnable reel project + two commands." The human (or CI) runs `generate-audio.ts` and `remotion render` in the `remotion/` project. Say this plainly when handing off — never imply a finished video appeared.

## Default: silent and captioned. Voice is opt-in.

The default reel needs **no API key**: each scene carries its key phrase as on-screen text (animated, like the chinese-room demo), so it teaches with captions alone. Narration is a separate, opt-in upgrade — only run `generate-audio.ts` when the user asks for voice **and** `ELEVENLABS_API_KEY` + `ELEVENLABS_VOICE_ID` are set (see `KEYS.md`). Build scenes silent-first; the `[Audio]` line is added only after the MP3s exist.

## Inputs

- **Source material** — a chapter file, section, excerpt, notes, or a named concept. Ground everything in it.
- **Audience** — what the learner already knows and what they're trying to understand.
- **Brand** (optional) — read `brand/[BRAND]/[BRAND].md` if named; else default to `brand/NBB`.
- **Voice** (optional) — only if narration is explicitly requested and keys are present.

## The pipeline

```
scan → storyboard → scenes → (captions  |  voice)  → render commands
 │        │           │          silent      opt-in     handoff
 │        │           └─ Scene-NN-*.tsx + Reel + Root.tsx
 │        └─ blueprint.md  (### Slide NN / Speaker notes — also drives audio)
 └─ propose which concepts deserve a video (like cajal's figure scan)
```

### 1. Scan (optional, cajal-style)
Given a chapter, propose the 1–3 concepts that would most reward a 60–120s video: name each, the single idea it teaches, the misconception it repairs, and a suggested shape. Recommend *one* to build first. Don't storyboard everything.

### 2. Storyboard → `blueprint.md`
- Pick a tutorial **shape**: mechanism · timeline · comparison · process · misconception-repair · worked example · story-of-an-idea.
- Draft from `references/blueprint-template.md` — the 7-beat arc (hook → name → first mechanism → make-the-relationship-visible → misconception-repair → transfer → durable model). 5–8 scenes; one idea-move per scene.
- Each slide: `### Slide NN`, then `**Purpose** / **Visual intent** / **On-screen text** / **Speaker notes:**`. Only the text under `**Speaker notes:**` is read by the audio script, so keep the other fields above it.
- Target **20–45 spoken words per slide**. Label any invented analogy as an *instructional analogy*. No paragraphs on screen.
- Stop here and get the blueprint accepted before writing scenes or audio.

### 3. Scenes → Remotion code
Scaffold the project, then generate one scene per beat from `references/scene-template.tsx`.
- **Paths:** code/reference under `demos/[slug]/` (or `clients/[CLIENT]/[slug]/`); runtime assets under `public/[slug]/`. Blueprint at `[project]/blueprint.md`; scenes at `[project]/src/scenes/Scene-NN-kebab.tsx`; sequencer at `[project]/src/[PascalName]Reel.tsx`.
- **One file per scene**, named export `SceneNNName`, exporting `durationInFrames`.
- **Reel:** a `[Series]` of `[Series.Sequence durationInFrames={N}]` — one per scene, in order.
- **Register** every scene and the reel in the applicable `Root.tsx` (`[Composition]` each; `fps={30}`, `width={1920}`, `height={1080}`), following the **Studio organization** default below. See `references/registration-and-render.md`.
- **Silent-first:** do **not** add `[Audio]` yet. The on-screen text from the blueprint carries the meaning.
- **Frame budget** (30 fps): size each scene to its content. Silent caption beat ≈ 4–7s (120–210 frames). When voiced, a scene must be **at least** the narration length: `frames ≈ ceil(words ÷ 2.5 × 30) + 60` (a ~1s lead-in + ~1s tail; audio starts at `from={30}`).

### Studio organization (default — one active video at a time)

Teachers are not video editors. They work on the newest video, one at a time, and
do not want a wall of old compositions. So when you register a video, do it this way
**by default, without asking**:

1. Wrap the new video's compositions in a top-level `[Folder name="[slug]"]` (its reel
   first, then its scenes) and place that folder **first** in `RemotionRoot`.
2. Move every other top-level project into a single `[Folder name="archive"]` — create
   it if absent, and nest each older project as its own subfolder inside it.

Result: the new video sits alone at the top of the Studio sidebar; everything older is
collapsed under `archive`. Nothing is deleted — folders only organize the sidebar. This
is the default. Only deviate (keep several visible, delete an old project, custom
grouping) when the user explicitly **asks to reorganize**.

### Generate cinematic assets with Higgsfield (optional)

When a beat wants a real photo or video clip instead of CSS shapes, generate it with the
**higgsfield-generate** skill and drop the file into the project's `public/[slug]/`, then
reference it in the scene. This runs on the user's machine through their authenticated
`higgsfield` CLI (their account + credits) — hand over the command; do not assume you can
run it here.

Higgsfield prints a **result URL**, not a local file (there is no `--output` flag). So
generate, then download into the video's assets:

```bash
# 1) generate — prints the asset URL on stdout
higgsfield generate create gpt_image_2 --prompt "…" --aspect_ratio 16:9 --resolution 2k --wait
# 2) download that URL into the video's public assets
curl -o public/[slug]/name.png "[printed-url]"
# (one-shot: add --json and pipe through jq to grab the url, then curl)
```

Then use it in the scene: `[Img src={staticFile('[slug]/name.png')} /]`, or
`[OffthreadVideo src={staticFile('[slug]/clip.mp4')} /]` for a Seedance/Kling clip
(`seedance_2_0`, `kling3_0`).

- **On-brand only.** A minimalist diagram reel usually should not carry a photoreal
  background. Reach for Higgsfield when the concept *wants* cinematic or photographic
  imagery — a historical scene, a physical mechanism, a character — not as decoration.
- Generated media are assets like any other: they live under `public/[slug]/`, the human
  approves the look before it ships, and you never fabricate provenance.

### 4a. Captions (silent path, default)
The animated on-screen text *is* the caption. If you later have MP3s, you can run Whisper for word-level timing (`docs/voice-generation.md` → Whisper section) to sync captions to speech.

### 4b. Voice (opt-in upgrade)
Only when requested and keys are present:
```bash
npx tsx scripts/generate-audio.ts [project]/blueprint.md public/[slug]
```
MP3s land at `public/[slug]/audio/slide-NN.mp3` (+ meta sidecars). Then add to each scene, near the top of its `AbsoluteFill`:
```tsx
[Sequence from={30}][Audio src={staticFile('[slug]/audio/slide-NN.mp3')} /][/Sequence]
```
If speaker notes change, delete that slide's MP3 + `.meta.json` and rerun (skip-if-exists resumes).

### 5. Render (handoff — commands only)
Don't render here. Hand the user these — and tell them to run from the `remotion/` project root (the folder with `package.json`):
```bash
npx remotion studio                                   # preview live
npx remotion still [ReelId] --scale=0.25 --frame=30   # one-frame sanity check
npx remotion render [ReelId] out/[slug].mp4           # full reel
```

## Core rules

- **One concept per video.** Several in the source → propose the best single one, or a short series.
- **Small working memory.** 5–8 scenes, one idea-move each. No decorative complexity.
- **Every visual answers the narration / caption.** If a shape doesn't carry meaning, cut it.
- **Source-grounded.** No invented facts; tie claims to the chapter (and the book's `facts/` store where one exists). Label instructional analogies as such.
- **Diagrams over text.** Prefer mechanisms, timelines, comparisons, worked micro-examples; key phrases only, never paragraphs.
- **Reuse cajal figures.** If a cajal SVG/PNG already exists for the concept, drop it into `public/[slug]/` and `[Img src={staticFile(...)}]` it rather than re-drawing.
- **Brand tokens** come from `brand/[BRAND]/[BRAND].md`; don't hardcode ad-hoc colors when a brand is named.

## Output contract

When you stop, report: the **concept sentence**; the **files created/changed**; whether it's **silent or voiced**; the **exact render command** for the reel; and any **unresolved source, accuracy, or asset gaps**. Be explicit that rendering and (if voiced) audio generation are commands the user runs — the skill did not produce the MP4 itself.

# Installs, `.env`, and credentials — set up once, then make videos

This is the companion doc to **video 2** in the *Brutalist — Claude for Video Production*
playlist. It is not the full install checklist — that's the terse [`INSTALL.md`](../INSTALL.md) at
the repo root, and the doctor (`./setup`) checks every piece for you. This doc explains the parts
people actually get stuck on: where keys live, what `npx` and `pip` and a virtual environment
*are* and why the toolkit uses them, which paid services do what — and the one 30-minute setup step
that saves more time than everything else combined.

The rule for the whole thing: **you only install what the features you want need.** With nothing but
`ffmpeg` and Pillow — zero keys — `previz` and the `slate-cut` first pass already run. Everything
else layers on top, and a blank key just greys out the feature that needs it. Nothing breaks.

---

## `.env` — one file for everything

Every key, every path, every toggle lives in one file: `.env` at the repo root. You make it by
copying the template:

```bash
cp .env.example .env
```

`.env` is gitignored, so your keys never get committed. Open it, fill in only the lines for
features you want, and leave the rest blank. A blank `ELEVENLABS_API_KEY` doesn't error — it just
means narration is off until you add one. The dispatcher (`./art`) loads `.env` automatically before
running any skill, so once a key is in the file, every part of the toolkit can see it.

That's the whole model: **one file, blank = off, the tool loads it for you.**

## Credentials — the one thing that isn't just a key

Most services are a single key on a line. YouTube is the exception: it uses Google's Desktop OAuth,
which is a pair of JSON files, not an API key. Those live in a per-channel folder:

```
youtube/credentials/<channel>/
  client_secret.json           # you download this from the Google Cloud console
  youtube_token.json           # created automatically the first time you authorize
  youtube_publish_ledger.json  # the record of what this channel has already uploaded
```

The whole `youtube/credentials/` folder is gitignored — those are secrets and local state, never
committed. You pick which channel is active with one line in `.env`:

```
ART_YOUTUBE_CHANNEL=nikbearbrown
```

Most people have exactly one channel and never think about this again. If you run more than one, add
another folder (`youtube/credentials/medhavy/`, `youtube/credentials/hai/`, …) and switch channels
by changing that one line.

## What is `npx`, and why we use it

`npx` ships with Node (`npm`'s sibling). It **runs a Node package's command-line tool without
installing that tool permanently or globally.** It finds the version the project already pins, runs
it, and leaves nothing behind to rot.

In this toolkit `npx` is how every Remotion render happens:

```bash
npx remotion render src/index.ts BarChart out/barchart.mp4
npx remotion studio            # live preview while you scrub the timing
```

Why not just install Remotion globally once? Because Remotion is version-sensitive — the components
are written against a specific Remotion 4.x + React 18.3.1, and a mismatched global copy renders
subtly wrong or fails outright. `npx` guarantees you get **the exact version pinned in that
project's `node_modules`**, not whatever happens to be on your machine. Same command on every
computer, nothing to clean up afterward. You install the project's Node deps once per Remotion
folder (`npm install` inside it); `npx` handles the rest.

## What is `pip`, and why we use it

`pip` is Python's package installer. It pulls the libraries the toolkit's scripts import — Manim
(animation), librosa and soundfile (audio timing), faster-whisper (caption alignment), Pillow
(slates and request cards), vtracer (line-art), and the Google API clients (YouTube). One command
installs the pinned set:

```bash
pip install --break-system-packages -r requirements.txt
```

Two things worth knowing. First, `--break-system-packages`: recent macOS and Linux Python builds
refuse to install into the *system* Python by default, to stop you from clobbering packages the OS
depends on. The flag says "yes, I mean it" — **but the cleaner answer is a virtual environment**
(next section), and inside one you don't need the flag at all. Second, `requirements.txt` holds
`numpy < 2` on purpose: librosa, numba, and some Manim builds still break on numpy 2.x. That pin is
exactly why an isolated environment matters.

## Virtual environments — and how Claude Code uses them

A **virtual environment** (a "venv") is an isolated Python: its own copy of the interpreter and its
own set of installed packages, living in a folder inside the project. Activate it and `python3`
means *this* project's Python — with *this* project's exact library versions — instead of the
system one. Deactivate and you're back to normal. Nothing leaks between projects.

That isolation is why the `numpy < 2` pin can hold here without you having to downgrade numpy
everywhere else on your machine. Create and enter one like this:

```bash
python3 -m venv .venv          # make it (once)
. .venv/bin/activate           # enter it (each new shell)
pip install -r requirements.txt
```

The toolkit expects the venv at `./.venv` — that's the default value of `ART_VENV` in `.env`. **Here
is the part that matters for Claude Code:** when Claude Code builds a video for you, it runs the
render scripts (Manim, the audio pipeline, the compositor) as `python3 …`. Those calls resolve to
whichever Python is active in its shell. So Claude Code should be working **inside the venv** — with
`./.venv` activated — so that `python3` is the one that has Manim and librosa installed at the
pinned versions. When it is, `./setup` shows a green readiness table and the renders just work; when
it isn't, you'll see "module not found" for exactly the libraries you `pip install`ed elsewhere.
The fix is always the same: activate the venv, then run. Run `./setup` any time to see which side of
that line you're on.

## The paid services, and what each one does

Four services cost money. None is required to start, and each unlocks a specific capability:

- **ElevenLabs** *(paid — the important one)* — voice cloning and narration. This is what turns a
  beat sheet's text into spoken audio in *your* voice. Set `ELEVENLABS_API_KEY`; get it at
  elevenlabs.io. Unlocks every narrated video: explainer, sketch-explainer, math-explainer, bio,
  kids-video, story-film, recitation-film, code-walkthrough, and the narrated lecture pipeline.
- **higgsfield** *(paid)* — AI image and video generation, driven through the `higgsfield` CLI
  (`higgsfield auth login` once). This is the tool for beats a machine has to *generate* rather than
  animate: lyric-resync, dance-video, photoreal bio footage, AI-video explainer beats, ai-asset-gen.
- **fal.ai** *(paid, optional)* — an alternate image path with style LoRAs. Set `FAL_KEY` only if
  you want it; the pipeline runs fine without it.
- **YouTube Data API** *(free, but quota'd)* — publishing. Not a paid key — it's the OAuth
  credentials above, and Google grants a free daily quota (about six uploads a day at the default,
  raisable through their review). This is what `youtube-publisher` uses to post the finished
  playlist.

The through-line: **ElevenLabs is the one to set up first**, because narration is the spine of most
videos — and because of the next section.

## The 30 minutes that saves you the most: clone your voice

> **Strong recommendation: record about 30 minutes of your own voice, once, and make an ElevenLabs
> voice clone of it.** It is the single biggest time-saver in this whole toolkit.

Here's the math. If you narrate every video live, you pay a fixed tax *every session* just to get
usable audio — finding the mic, killing the room noise, setting levels, re-recording the line you
flubbed. Thirty minutes gone before you've kept a single good take, and you pay it again next time,
and the time after that.

A voice clone moves that cost to **once.** You spend one focused 30-minute session recording clean
audio, ElevenLabs learns your voice, and from then on every video narrates itself directly from the
beat sheet's text — instantly, in your voice, no mic, no room, no retakes. The beat sheet is the
script; the clone reads it.

Yes, the clone will mispronounce some words. So will you. That's not a reason to skip it — it's a
review note like any other: catch the wrong pronunciation the same way you'd catch a wrong note in a
live take, fix that one beat's text (spell it phonetically), and move on. The occasional
mispronunciation is a rounding error against never fighting a microphone again.

Set the clone up, put its voice ID in `.env` (`ELEVENLABS_VOICE_ID`, or a named one like
`ELEVENLABS_VOICE_NIKBEARBROWN`), and you're done. This is the highest-leverage 30 minutes you'll
spend on the whole setup.

## Verify

Two commands tell you exactly where you stand:

```bash
./setup            # dependency + no-key-feature readiness table
./art keys         # validate every key you've set — live and free, no spend
```

`./setup` shows which system binaries, Python libs, and Node deps are present and what each missing
one unlocks. `./art keys` probes each key against a free account-status endpoint (it never spends
characters, credits, or renders) and tells you whether ElevenLabs, higgsfield, and your YouTube
OAuth are actually valid. Green on both means you're ready to build.

---

*Full checklist: [`INSTALL.md`](../INSTALL.md). Every variable, annotated:
[`.env.example`](../.env.example). This doc is the basis of video 2 —
[`youtube/installs/`](../youtube/installs/).*

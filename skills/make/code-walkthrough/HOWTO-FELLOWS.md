# How to Create Simulation Videos

*A fellow's guide to the vox `simulation` aspect — build a "make your own physics/math simulation with Claude Code + Manim" reel, in the Medhavy register.*

A **simulation video** is not a physics explainer. It teaches the **workflow**: the `prompt → read the script → run → check → change` loop, using a physics or math concept only as the running example. You'll build one the same way we built the worked example — `quantum-mechanics-vol1/youtube/medhavy-ch1-classical-sims` — which you can open and copy beat-for-beat.

Work in two passes. **Part 1** gets your machine ready and proves it with one check. **Part 2** builds your own reel. Don't skip Part 1 — the most common failure (wrong fonts) renders every video in a substitute typeface and *no gate warns you*.

---

## What you download

vox is a **toolkit**, not a book. It builds videos from book content that sits **beside** it as a sibling folder. So you need a parent folder (call it `books/`) holding **at least two** repos side by side: the toolkit, and one book.

```
books/                          ← any parent folder you make
├── vox/                        ← the toolkit          (github.com/nikbearbrown/vox)
└── quantum-mechanics-vol1/     ← a book, sibling of vox (github.com/nikbearbrown/quantum-mechanics-vol1)
    ├── chapters/               ← the source markdown the scout reads
    └── youtube/                ← your reels build in here
        └── medhavy-ch1-classical-sims/   ← the worked example to copy
```

Clone both into the **same** parent folder:

**Step 1 — make the parent folder and clone the toolkit + one book side by side:**

```bash
mkdir -p ~/books && cd ~/books
git clone https://github.com/nikbearbrown/vox.git
git clone https://github.com/nikbearbrown/quantum-mechanics-vol1.git
```

Any book works — clone whichever ones you're assigned as more siblings of `vox/`. They are deliberately separate repos: `vox/` is the shared engine everyone updates; the books are the content, each kept and backed up on its own.

You also need the **Claude Code CLI** installed (that's what drives the build). If `claude` isn't on your PATH yet, install it first — the guide at the end of this doc assumes `claude` runs.

---

## What you install

macOS-oriented (the font step and `open` commands assume a Mac). Four things: Python render libraries, ffmpeg, the house fonts, an ElevenLabs key — plus Node for the terminal/code-block beats a sim reel uses.

**Step 2 — Python libraries (Manim + the vox pipeline deps):**

```bash
cd ~/books
pip install -r vox/requirements.txt
pip install manim Pillow
```

**Step 3 — ffmpeg (the compositor), via Homebrew:**

```bash
brew install ffmpeg
```

**Step 4 — register the four house fonts so Manim can find them by name:**

```bash
cp vox/fonts/*/static/*.ttf vox/fonts/PT_Mono/*.ttf ~/Library/Fonts/
```

**Step 5 — your ElevenLabs key (this is the only thing that ever spends money — narration audio):**

```bash
cp vox/.env.example vox/.env
```

Then open `vox/.env` and replace `your-elevenlabs-api-key` with your real key. The three voice IDs (NikBearBrown, Medhavy, Humanitarians) are already filled in — leave them. `.env` is gitignored, so **your key stays on your machine; never commit it or paste it to anyone.**

**Step 6 — Node lane.** A simulation reel opens with an Onda **terminal** beat and shows the generated code in an Onda **code-block** beat. Those are rendered by the Remotion project, which is the *only* part of vox that needs Node. Install Node, then the project's deps:

```bash
brew install node
cd ~/books/vox/aspects/remotion-pass/remotion && npm install
```

---

## Part 1 — Build the install check (do this first)

Before building anything, prove the whole toolchain end-to-end. Save the preflight script (delivered alongside this guide as `vox-preflight.sh`) into your `books/` folder and run it there:

**Step 7 — run the preflight from your `books/` parent folder:**

```bash
cd ~/books
bash vox-preflight.sh
```

It checks, in order: vox sits beside your books · Python 3 + `manim, PIL, numpy, requests, mutagen` all import · `ffmpeg` present · **all four fonts** registered · `vox/.env` has a real key (not the placeholder) · Node + the Remotion `node_modules` installed · and finally it runs **Gate A** (a no-network layout check) on vox's bundled example scene.

Every line prints `OK` or `FAIL`. If it ends with **`Ready.`**, your machine can build reels. If anything says `FAIL`, fix that one line — the message names the install step — and re-run. Don't move to Part 2 until it's green.

> If you'd rather not use the script, the same checks by hand:
> ```bash
> cd ~/books
> python3 -c "import manim, PIL, numpy, requests, mutagen; print('py deps ok')"
> which ffmpeg
> fc-list | grep -iE 'garamond|inter|montserrat|pt mono'   # must list all four
> node -v && test -d vox/aspects/remotion-pass/remotion/node_modules && echo "node lane ok"
> ```

---

## Part 2 — Create your own simulation video

### First, look at the worked example

Open the reel we built and watch it, then read its files — your reel copies this shape:

**Step 8 — open the example video and list its files:**

```bash
open ~/books/quantum-mechanics-vol1/youtube/medhavy-ch1-classical-sims/medhavy-ch1-classical-sims-review.mp4
ls ~/books/quantum-mechanics-vol1/youtube/medhavy-ch1-classical-sims/
```

The files that define a reel (copy these as your template):

| File | What it is |
|---|---|
| `beat_sheet.json` | the single source of truth — every beat, its duration, its `tts` (spoken) and `text` (on-screen), and props |
| `vox_scenes.py` | the Manim scenes — one class per rendered beat, named `B{N}_<ConceptRun>` |
| `FACTCHECK.md` | every formula and number verified against a source (gates the audio spend) |
| `PEDAGOGY.md` | the teaching audit — must end `VERDICT: PASS` or `generate_audio.py` refuses to run |
| `SHOTLIST.md` / `PROMPTS.md` | per-beat shot notes and the generation prompts |

### How a simulation reel is shaped

**Medhavy bookends, always:** first beat is the Medhavy intro (Onda terminal), last beat is the Medhavy outro. Between them, each simulation segment is **four acts**:

1. **PROMPT** — an Onda *terminal* beat showing the real `claude "..."` command that generates the scene. The narration is about *prompting* (the three things every generation prompt must state: the rule, the numbers, what to render) — not about the physics.
2. **SCRIPT** — an Onda *code-block* beat showing the actual generated Python that runs in Act 3. The narration is about *reading generated code* — finding the one line that encodes the physics.
3. **RUN** — the Manim simulation running for real. The narration names **two concrete things to verify** (a boundary case, a published value) — not "it looks right."
4. **CHANGE** — a follow-up `claude "update X.py ..."` command that tweaks one parameter. The narration's point: *closing the loop is the skill.*

The physics still has to be **correct** (there's a fact gate), but it is the vehicle, never the lesson.

### The standing rules your reel must follow

These live in the toolkit — read them before you build; the gates enforce them:

- `vox/MEDHAVY.md` — the Medhavy intro/outro text, and the pronunciation split (screen shows `Medhavy`, voice says `med dahvy`).
- `vox/VISUAL-RULES.md` — **less text** (labels are short tags, the voice carries the words), **natural colors override the palette** (light renders as its real spectral color — 700nm red, 546nm green, UV violet), and **safe-area margins** (16:9 protects left/right, 9:16 protects top/bottom; 9:16 is a reflow, never a crop).
- `vox/REGISTERS.md` — which outro closes the video.
- `vox/PRONUNCIATION.md` — the ElevenLabs pronunciation dictionary.

### Build it with Claude Code

Launch Claude Code from the `books/` parent (so it sees vox and every book at once), permissions skipped so it runs hands-off:

**Step 9 — launch Claude Code from `books/`:**

```bash
cd ~/books
claude --dangerously-skip-permissions
```

**Step 10 — scout a chapter and get a plan (paste this into Claude Code; swap the book folder for yours):**

```
Read vox/CLAUDE.md, vox/aspects/simulation/SKILL.md, vox/MEDHAVY.md, and vox/VISUAL-RULES.md. Run the simulation scout on quantum-mechanics-vol1: scan its chapters for simulatable concepts (a rule that produces a visible curve/trajectory/spectrum, with at least two testable predictions, and a surprising result). Propose either ONE deep sim or a reel of 3-4, name the concepts and why, and wait for my approval before writing anything.
```

Review what it proposes, then approve the build:

**Step 11 — build the approved reel (paste into Claude Code; set your slug):**

```
simulation build <slug> — write FACTCHECK.md, SHOTLIST.md, and PEDAGOGY.md (ending VERDICT: PASS), then beat_sheet.json (B00 Medhavy intro -> the four-act segments -> Medhavy outro) and vox_scenes.py. Run Gate A + W pre-flight, fix any failures (cap 3 attempts), generate the audio, then run the full build. Follow every rule in MEDHAVY.md and VISUAL-RULES.md, keep the physics correct against FACTCHECK.md, and give me the open command for the review mp4 when it's done.
```

Under the hood that runs the two pipeline commands (you can also run them yourself for one reel):

```bash
python3 vox/scripts/generate_audio.py quantum-mechanics-vol1/youtube/<slug>   # narration — spends credits
bash    vox/scripts/vox_run.sh        quantum-mechanics-vol1/youtube/<slug>   # render + QC gates + compile
```

The deliverable is `quantum-mechanics-vol1/youtube/<slug>/<slug>-review.mp4`.

**Step 12 — make the 9:16 Short (one example only, strictly under 3:00 — a YouTube Shorts hard rule):**

```
Build the 9:16 Short for quantum-mechanics-vol1/youtube/<slug>: run vox_short.py on ONE segment only, keep the Medhavy intro + outro, reflow to portrait (never crop), and confirm the whole Short runs under 3:00. Re-run the gates on the short/ folder and give me the open command.
```

### If something fails

- **Audio refuses to run** → that's the pedagogy gate. The reel folder needs a `PEDAGOGY.md` ending `VERDICT: PASS`. Rewrite the beat sheet until the audit passes; don't annotate around it.
- **A scene fails its layout gate** → read `<reel>/layout_audit.md`, fix the scene, re-run. After ~3–5 attempts, hand the finding back to Claude Code (or to Cowork) to clear by hand.
- **Wrong fonts** → re-run Part 1; if the four-font check wasn't all green, every frame used a substitute. Fix fonts, re-render.

---

## The whole thing in one breath

Clone `vox` + a book as siblings → install Python/ffmpeg/fonts/key + Node → run `vox-preflight.sh` until it says **Ready** → open the `medhavy-ch1-classical-sims` example → launch Claude Code from `books/` → scout, approve, `simulation build <slug>`, then the 9:16 Short. The loop the video teaches — prompt, read, run, check, change — is the same loop you'll be running to build it.

# INSTALL

Everything here is checked by `./setup` (the doctor). You do **not** have to install
all of it — install only what the features you want need. Run `./setup` any time to
see the per-feature readiness table and exactly what each missing piece unlocks.

The fastest path:

```bash
git clone <this repo> && cd brutalist-art
cp .env.example .env          # fill in only the keys you need (all optional to start)
./setup --install             # installs core Python deps, then prints readiness
```

With **zero keys and zero extra installs beyond ffmpeg + Pillow**, `previz` and the
`slate-cut` first pass already run. Everything else layers on top.

---

## 1. System binaries

| Tool | Needed for | macOS | Debian/Ubuntu |
|---|---|---|---|
| **ffmpeg** (+ ffprobe) | almost everything (compositing, captions, cuts) | `brew install ffmpeg` | `sudo apt install ffmpeg` |
| **Python ≥ 3.10** | all scripts | `brew install python@3.12` | `sudo apt install python3 python3-pip` |
| **Node ≥ 20** | Remotion features (explainer, music-video, lyric-overlay, code-walkthrough, youtube-publisher, figure-planner) | `brew install node` | `nvm install 20` (nodejs.org / nvm) |
| **LaTeX + dvisvgm** | Manim math (`MathTex`) — math-explainer, some explainer beats | `brew install --cask mactex-no-gui` | `sudo apt install texlive texlive-latex-extra dvisvgm` |
| **jq** | parsing the higgsfield CLI's JSON responses | `brew install jq` | `sudo apt install jq` |
| **higgsfield CLI** | all AI image/video (lyric-resync, dance-video, ai-asset-gen, photoreal bio, explainer AI beats) | see the tool's own docs, then `higgsfield auth login` | same |

ffmpeg must be built with `libx264` and `aac` (the Homebrew/apt builds are). Manim
math also needs the LaTeX pieces above; without them, non-math scenes still render.

## 2. Python dependencies

```bash
pip install --break-system-packages -r requirements.txt
```

Pins are in `requirements.txt`. Two things worth knowing:

- **numpy is held `< 2`** on purpose — librosa/numba and some Manim builds still break
  on numpy 2.x. If you already have numpy 2 in the environment, use a venv (below).
- **Manim has its own system deps** (Cairo, Pango, ffmpeg). On Linux:
  `sudo apt install libcairo2-dev libpango1.0-dev pkg-config`. On macOS Homebrew's
  `manim` bottle or `brew install cairo pango pkg-config` covers it.

Recommended: an isolated venv (the scripts default to `./.venv`, override with
`ART_VENV` in `.env`):

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
```

## 3. Node dependencies (per Remotion project)

Node deps live with each Remotion project, not at the repo root. Install where you
render. All projects use **Remotion 4.x + React 18.3.1 + TypeScript ~5.4**:

```bash
(cd runtime/remotion && npm install)                          # Medhavy bookends (youtube-publisher, slate-filler)
(cd skills/make/component-showcase/remotion && npm install)   # component-showcase bench
(cd skills/make/lyric-overlay/templates && npm install)       # lyric-overlay
```

Remotion renders through headless Chromium; it downloads its own on first render, or
point `ART_CHROME` at an existing Chrome/Chromium in `.env`.

## 4. Keys

All keys live in `.env` (copy from `.env.example`; `.env` is gitignored). A blank key
just disables the features that need it — nothing else breaks.

- **`ELEVENLABS_API_KEY`** (paid) unlocks all narration. Get it at elevenlabs.io.
- **AI image/video** goes through the `higgsfield` CLI login (`higgsfield auth login`).
  `HIGGSFIELD_API_KEY` / `MINIMAX_API_KEY` are present as blank placeholders in
  `.env.example` if your setup prefers passing them via the environment.
- **YouTube** uses Google Desktop OAuth, not a key: download `client_secret.json`
  from the GCP console (YouTube Data API v3 → OAuth client → Desktop) and point
  `ART_YOUTUBE_CLIENT_SECRET` at it. First publish opens a browser to authorize.
- **`FAL_KEY`** (paid, optional) enables the fal.ai style path.

## 5. Verify

```bash
./setup            # readiness table; exit 0 if all no-key features are ready
./art --list       # every skill (and its former name)
./art todo examples/slate-cut--base-rate   # the beat ledger on the no-key example
```

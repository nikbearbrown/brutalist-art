# showcase-series BUILD-LOG (append-only)

## 2026-07-22 — musinique-logo-2 pilot

### Status entering session
- ep01–ep05 (9:16 Short cuts): beat_sheet.json + mp3/ + props.json present; video-silent.mp4 missing.
- ep01–ep05-16x9: beat_sheet.json only; no audio, no props, no render.
- full-16x9: props.json + video-silent.mp4 present (from earlier run).
- BUILD-LOG did not exist; creating now.

### Step 1 — generate Kokoro audio for five ep0N-16x9 folders
- ep01-16x9: E90=16.87s E91=9.51s E92=3.63s ✓
- ep02-16x9: E00=13.46s E90=14.57s E91=9.86s E92=3.65s ✓
- ep03-16x9: E00=13.03s E90=15.70s E91=9.39s E92=3.71s ✓
- ep04-16x9: E00=13.42s E90=15.17s E91=9.69s E92=3.73s ✓
- ep05-16x9: E00=13.40s E90=17.07s E91=13.08s E92=4.78s ✓

### Step 2 — props (all 10 cuts)
ep01=53.5s ep01-16x9=79.2s ep02=58.1s ep02-16x9=84.1s ep03=58.5s ep03-16x9=83.9s ep04=59.9s ep04-16x9=85.7s ep05=64.4s ep05-16x9=91.2s

### Step 3 — renders (foreground, one at a time)
All 10 via npx remotion render --concurrency=1, foreground, one at a time:
ep01(○ 3.4MB) ep01-16x9(+ 4.7MB) ep02(○ 5.9MB) ep02-16x9(+ 6.7MB) ep03(○ 5.7MB) ep03-16x9(+ 6.3MB) ep04(○ 4.7MB) ep04-16x9(+ 6.7MB) ep05(○ 5.5MB) ep05-16x9(+ 5.7MB)

### Step 4 — mux
All 10 cuts muxed. showcase_episodes.py mux musinique-logo-2 → 10 FINAL mp4s.

### Step 5 — Visual QC
Frames sampled: 0.5fps for ep02/ep02-16x9; 0.25fps for all others. All rubric points checked.
RESULT: PASS — 0 defects across all 10 cuts. Details in _qc/REPORT.md.

**STOPPED here per BUILD-PROMPT. Awaiting Bear approval before batch.**

### Step 6 — YouTube upload (Bear approved 2026-07-22)
Channel: @NikBearBrown · Privacy: unlisted (flip public in Studio)
Script: runtime/scripts/showcase_upload.py (written this session)
Ledger: youtube/credentials/nikbearbrown/showcase_upload_ledger.json

| Cut | Title | Playlist | Video ID |
|---|---|---|---|
| ep01-16x9 | Musinique, In Motion — Part One. | Brutalist | uPs40QlCO24 |
| ep01 | Musinique, In Motion — Part One. | Shorts | 11_9uG0hdZY |
| ep02-16x9 | Musinique, In Motion — Part Two. | Brutalist | 6ku1brE91io |
| ep02 | Musinique, In Motion — Part Two. | Shorts | BfQAx10yR4Y |
| ep03-16x9 | Musinique, In Motion — Part Three. | Brutalist | B-uTWzPyHYc |
| ep03 | Musinique, In Motion — Part Three. | Shorts | cIgHIn9qozk |
| ep04-16x9 | Musinique, In Motion — Part Four. | Brutalist | BM7Rx5cQvzU |
| ep04 | Musinique, In Motion — Part Four. | Shorts | G7qhuN8qfm4 |
| ep05-16x9 | Musinique, In Motion — Part Five. | Brutalist | phiSJI0ssfU |
| ep05 | Musinique, In Motion — Part Five. | Shorts | D0BO3dSSHsc |

Note: "Brutalist — Claude for Video Production" playlist was created fresh on the channel (did not already exist — created by the script). Verify in Studio that it's set to public.

---
## 2026-07-22 — musinique-logo-2 pilot

**Session**: scaffold already done; Kokoro audio generated for all 6 original cuts
(full-16x9, ep01–ep05) with --no-gate.

**Script update discovered mid-session**: showcase_episodes.py was updated between
first `props` run and `mux`. New `cuts_of()` generates ep0N (9:16) + ep0N-16x9 (landscape)
per episode; full-16x9 long cut is now `build_full_16x9`-gated (set false in episodes.json).
Episodes.json also gained per-episode `recap` fields (verdict cards for 16x9 cuts).

**Builds**:
- `props musinique-logo-2` → 10 props.json (ep01–ep05 × 2 aspects)
- Renders (foreground, one at a time):
  - ShowcaseWrap16x9: ep01-16x9, ep02-16x9, ep03-16x9, ep04-16x9, ep05-16x9
  - ShowcaseWrap916: ep01, ep02, ep03, ep04, ep05
  - Also rendered old-arch full-16x9 (7711f = 257s) — no longer tracked, file retained at full-16x9/video-silent.mp4
- `mux musinique-logo-2` → 10 FINAL mp4s (ep05-16x9 required manual ffmpeg re-run after subprocess 183 fluke)

**QC**: PASS — all 9 rubric points checked for ep01-16x9 and ep01. See _qc/REPORT.md.

**Stopped here per BUILD-PROMPT**: awaiting Bear approval before batch.

# Claude Code Prompt — Accurate 16:9 → 9:16 Converter (Shorts pipeline hardening)

## The rules (existing + new, consolidated)

Already law in the repo (`runtime/scripts/shorts.py` docstring — "THE SHORTS
LAW", plus `skills/make/sketch-explainer/reference/reframing-16x9-to-9x16.md`):

- A Short is a DERIVATIVE CUT, never a re-edit. **3:00 is a HARD cap** —
  at/under the cap the whole reel reformats; over it, beats are CUT (longest
  middle beats first; hook, hero, outro protected), never re-authored. When
  beats are cut, the outro is rewritten to send viewers to the 16:9 long —
  that outro is the only regenerated audio.
- Shorts ALWAYS post to the **"Shorts" playlist**; the description funnels to
  the parent long (the native Related-Video chip is a manual Studio step —
  the API can't set it).
- Reformat is REFLOW, not crop: authored vector/Remotion graphics are NEVER
  center-cut. Scale to the constrained width, redistribute down the height,
  serialize side-by-side panels, split what can't fit. Only captured/user
  footage is center-cut (biased by shot.focus), and `pantry/<beat>-916.*`
  always wins.
- REMOTION beats rewire to a portrait `<pattern>916` composition when one
  exists in Root.tsx; when it doesn't, the beat is FLAGGED and a human must
  intervene. **This flag path is the thing that keeps failing** — text in
  custom components overflows or clips in portrait.

New standing rules (this prompt bakes them in):

1. **TEXT LAW (the known failure).** Every portrait composition must reflow
   text with `maxWidth` + wrap/auto-fit against a 9:16 safe area — never
   reuse landscape coordinates or fixed widths. No 916 variant ships until
   its text survives frame-level QC.
2. **SHORTS PLAYLIST LAW.** 9:16 videos are posted ONLY to the "Shorts"
   playlist, on every channel (created if missing). Never to a topic or
   series playlist.
3. **SCHEDULE LAW.** A Short's publish time = the channel's last *scheduled*
   post + 1 hour; if the channel has nothing scheduled, publish immediately.
   Computed per channel at publish time.
4. **HARD CAP LAW.** 3:00 is enforced, not advised: a 9:16 over 3:00 is
   refused by the pipeline until beats are cut to bring it under (target
   ≤2:55 for muxing headroom). YouTube classifies vertical ≤3 min as Shorts
   by aspect + duration alone — over the cap the video silently stops being
   a Short.

Run Claude Code from:

`/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art`

Paste the complete prompt below. Nothing to replace.

```text
Build the accurate 16:9 → 9:16 converter for the explainer pipeline —
hardening shorts.py's existing SHORTS-LAW flow so the Remotion-text failure
mode is gone and the new Shorts publishing rules are encoded. No publishing
during this build, no git commit or push, free pipeline only. Run without
approval pauses.

READ COMPLETELY BEFORE ACTING
- runtime/scripts/shorts.py            (the SHORTS LAW docstring — the base)
- skills/make/sketch-explainer/reference/reframing-16x9-to-9x16.md
                                       (the reflow ruleset: scale to width,
                                        distribute down height, serialize,
                                        split — never shrink-and-float)
- skills/make/sketch-explainer/reference/shorts-vs-longform-strategy.md
- skills/make/ai-explainer/SKILL.md (House laws — LOGO, VISUAL QC,
                                        SHOW-DON'T-TELL all apply in 9:16)
- runtime/remotion/src/tokens/layout.ts and claude.ts
- runtime/remotion/src/Root.tsx        (which 916 compositions exist today)
- runtime/scripts/remotion_scenes.py, compile.py, stage_publish.py
- skills/upload/youtube-publisher/SKILL.md

PART 1 — 9:16 SAFE AREA (the missing constant)
layout.ts currently defines CANVAS/SAFE for 16:9 only. Add the portrait set:
CANVAS916 = {w:1080, h:1920} and SAFE916 = {x:54, y:96, w:972, h:1728,
r:1026, b:1824} (5% inset), with the same safeX/safeY/safeCenter helper
pattern parameterized by canvas. Every 916 composition positions essential
text, logos, and chips from SAFE916 — never from landscape coordinates.

PART 2 — PORTRAIT COMPOSITIONS FOR EVERY HOUSE SCENE (kill the flag path)
Inventory every Remotion composition the explainer beats actually use
(Root.tsx + the scenes remotion_scenes.py wires). For each one that lacks a
<name>916 twin, build it as a REFLOW, not a scale:
- Scale content to the portrait WIDTH, then redistribute down the HEIGHT:
  side-by-side panels serialize into a vertical stack (stacking order =
  reading order); a layout that can't stack splits into sequential
  sub-beats. Never shrink the landscape layout into the middle of the
  portrait frame.
- TEXT LAW: every text element gets maxWidth + wrap or auto-fit inside
  SAFE916. No fixed pixel widths, no reused landscape x-coordinates. Long
  labels wrap or shrink; boxes size to content or clip by intent.
- The logo bug relocates inside SAFE916 (still lower-right, still
  low-opacity, still never covering content); spark lines and segment
  titles re-anchor to the portrait grid.
- Props must keep the SAME zod schema as the landscape composition, so
  shorts.py's rewiring works unchanged (standing rule in its docstring).
Render a test still of each new 916 composition with deliberately LONG prop
text (a 2x-length title, a long label) and Read the PNG — text intact inside
SAFE916 before the composition counts as done.

PART 3 — SHORTS.PY HARDENING
- HARD CAP LAW: after the plan/compile, probe the output duration. If the
  final 9:16 exceeds 3:00, FAIL LOUDLY with the beat-cut plan that would
  bring it under (target ≤2:55) — never emit an over-cap file as done.
- The ONDA/Remotion check should now find a 916 composition for every house
  scene; keep the flag path for genuinely custom one-off scenes, but the
  standard library must produce zero flags on a normal explainer.
- After compile, run the frame-level VISUAL QC pass on the 9:16 output
  (sample frames ≥2 fps + per-beat 15/50/85%, Read the PNGs, 8-point rubric
  against SAFE916, log to short/_qc/REPORT.md, zero BLOCKER/MAJOR before
  done). The mp4 probe alone never counts.

PART 4 — PUBLISH RULES (encode, don't execute)
In the publisher path (stage_publish.py / the youtube-publisher scripts),
encode for any 9:16 upload:
- SHORTS PLAYLIST LAW: add the video ONLY to the channel's "Shorts"
  playlist (create it if missing). Never to topic/series playlists; the
  series funnel stays in the description link to the parent long.
- SCHEDULE LAW: query the channel's scheduled uploads (private with a
  future publishAt); set this Short's publishAt = latest scheduled + 1
  hour. If nothing is scheduled, publish immediately (no publishAt).
- Log the computed decision (playlist id, publishAt or "immediate") in the
  publish ledger. All of this remains behind the existing human publish
  gate — this build NEVER uploads anything.

PART 5 — PROVE IT END TO END
Pick one finished 16:9 explainer under youtube/ that is UNDER 3:00 and one
OVER 3:00 (check durations first):
- Under-cap: run the converter; expect zero Remotion flags, full reflow,
  QC-clean short/<slug>-916.mp4.
- Over-cap: expect the loud cap failure with a sane auto cut plan; apply
  the plan, rebuild, confirm the rewritten outro points to the long, and
  QC the result.
Do not publish either. Report: compositions added (and which reflow move
each used — stack / split / rescale), shorts.py changes, publisher changes,
QC results for both test videos, and any scene that still needs a human
pantry override.

REAL TEST MATRIX (from the @NikBearBrown channel, UCg0cw2ouRhQ8dr114yGp0mA —
map these titles to their youtube/<slug>/ folders; they exercise every path):
- UNDER-CAP, reformat whole (no beats cut): "When Safety Training Fails"
  (1:51), "The Sycophancy Gradient" (2:00), "Persisting Progress Across
  Context Windows" (2:12), "Caching Pixels You've Already Seen" (2:13),
  "The Hard Case" (2:31), "Same Text, Better Scaffold" (2:45).
- AT THE CAP, must trim for headroom (3:00 is the hard ceiling; target
  ≤2:55): "The Fluency Ceiling" (3:00). Confirm the pipeline does NOT pass a
  3:00 file through untrimmed.
- OVER-CAP, must cut beats + rewrite outro: "The Photoelectric Effect"
  (3:24, has chapter markers — use them for beat boundaries), "An Off Switch
  for Dangerous Knowledge" (3:25), "What 81,000 People Want from AI" (3:21),
  "Claude, Peer-Reviewed." (4:08), "Claude on the Clock." (4:58), "The Cost
  of the Pivot" (4:42).
- SCHEDULE LAW live check: the channel currently has TWO scheduled posts
  (both Jul 18, 2026 — "The Cost of the Pivot" and "The Engineer Who
  Stayed"). A new Short's computed publishAt MUST be the LATER of those two
  scheduled times + 1 hour. Print the computed publishAt and the scheduled
  post it keyed off — do NOT actually schedule or upload.
Run at least the two required end-to-end cases (one under, one over) live;
the rest are the acceptance checklist the converter must satisfy.

PART 6 — WRITE THE LAW DOWN
Append a "SHORTS / 9:16 LAW" bullet to the House laws section of
skills/make/ai-explainer/SKILL.md summarizing: derivative cut; reflow
never crop for authored graphics; TEXT LAW (maxWidth + wrap inside SAFE916);
3:00 hard cap enforced by the pipeline; Shorts playlist only; schedule =
last scheduled + 1h else immediate; visual QC mandatory on every 9:16
build. Two or three tight sentences per clause — pointer to shorts.py and
the reframing reference for the full doctrine.
```

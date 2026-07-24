# Claude Code Prompt — Unattended 9:16 Batch (all checked 16:9 finals → Shorts)

Runs the 16:9 → 9:16 converter across a whole list of already-finished,
already-checked 16:9 videos with NO approval pauses. Each 16:9 is treated as
the final master: under the 3:00 cap it just reflows to portrait (no beat
audit, no cutting, audio untouched); only videos OVER the cap get the
SHORTS-LAW beat cut. Produces the 9:16 final cuts and a staggered schedule
PLAN — it does not upload (publishing stays a separate human-gated step).

Run Claude Code from:

`/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art`

Paste the complete prompt below. Nothing to replace — the work list is embedded.

```text
Produce a 9:16 final cut for EVERY video in the WORK LIST below. This is an
unattended batch: run without approval pauses, process rows independently,
and never let one video's failure stop the batch. Free pipeline only: no
ElevenLabs, no higgsfield, NO publishing, NO uploading, NO git commit or
push. You WILL write a schedule plan, but you will not act on it.

CORE PRINCIPLE — THE 16:9 IS THE CHECKED FINAL MASTER
Every input is already rendered, fact-checked, and visually QC'd. Do NOT
re-audit it, re-mark or re-plan its beats, rewrite its script, or touch its
audio/timing. The job is to REFLOW the frame from landscape to portrait and
output the 9:16. Beat-cutting happens ONLY when an input runs over the 3:00
Shorts cap (see the DURATION RULE) — never otherwise.

READ ONCE BEFORE THE BATCH
- CLAUDE-CODE-916-CONVERTER.md            (the full ruleset)
- runtime/scripts/shorts.py               (THE SHORTS LAW)
- skills/make/sketch-explainer/reference/reframing-16x9-to-9x16.md
- skills/make/ai-explainer/SKILL.md   (House laws — LOGO, VISUAL QC,
                                           FILL-THE-CANVAS bind in 9:16 too)
- runtime/remotion/src/tokens/layout.ts   (SAFE916 already exists)
- runtime/remotion/src/Root.tsx
- skills/upload/youtube-publisher/SKILL.md (channel resolution, Shorts rules)

ONE-TIME SETUP (before looping)
Confirm SAFE916/CANVAS916 exist in layout.ts (they do). Inventory which
Remotion compositions across the whole work list still lack a <name>916
portrait twin, and build each twin ONCE as a REFLOW so every video that uses
it benefits:
- Content scaled to the portrait WIDTH, redistributed down the HEIGHT;
  side-by-side panels serialize top-to-bottom in reading order; anything
  that can't stack splits into sequential sub-beats. Never shrink-and-float.
- TEXT LAW: every text element uses maxWidth + wrap/auto-fit inside SAFE916 —
  no reused landscape coordinates, no fixed pixel widths.
- FILL-THE-CANVAS: use the taller portrait frame — scale type and content up
  to occupy SAFE916; don't leave the bottom empty.
- Logo bug relocates inside SAFE916 (lower-right, low-opacity).
- Keep the SAME zod prop schema as the landscape composition so shorts.py
  rewires unchanged. Render a test still per twin with deliberately LONG prop
  text and Read the PNG — text intact inside SAFE916 before it counts done.

PER-VIDEO LOOP (for each WORK LIST row)
1. RESOLVE: map the video id (and title) to its youtube/<slug>/ folder via
   the publish ledger (youtube/credentials/<channel>/youtube_publish_ledger.json
   maps id → folder) or by title match. If unresolvable, log SKIPPED(no-folder)
   and continue. If a 9:16 final already exists in the folder's short/, log
   SKIPPED(exists) and continue (idempotent) unless it's clearly stale.
2. DURATION RULE (probe the real mp4 duration):
   - <= 3:00  → straight reflow: the whole reel reformats 16:9 → 9:16, every
     beat carries 1:1, audio and timing untouched, NO beat marks/cutting. If
     the muxed 9:16 ends up over 3:00 only from container overhead, trim
     trailing silence/endcard to land <= 2:58 — never cut a content beat.
   - > 3:00   → SHORTS-LAW beat cut is required (3:00 is a hard ceiling):
     auto-plan via shorts.py (drop longest middle beats first; protect the
     hook, the hero, and the outro) to bring it to <= 2:55, rewrite ONLY the
     outro to say what was cut and point to the long, regenerate ONLY that
     outro's audio, then reflow to portrait.
3. BUILD: run shorts.py + compile the short at 1080x1920 into the folder's
   short/. Expect zero Remotion flags now that the twins exist; if a beat
   still flags, fix its composition rather than ship a center-cut of authored
   text. If a needed pantry override is truly required, log it and continue.
4. VISUAL QC (mandatory, per video): sample frames (>=2 fps + per-beat
   15/50/85%), Read the PNGs, run the rubric against SAFE916 (edge bleed,
   title-safe, overflow, collision, legibility, brand bug, aspect, canvas
   fill). Log to short/_qc/REPORT.md. Fix root causes and re-render until
   zero BLOCKER/MAJOR. The mp4 probe alone never counts.
5. LOG: append one line to youtube/_916-batch/BUILD-LOG.md — id | title |
   slug | in-duration | out-duration | reflow-only or beat-cut | QC verdict |
   done/failed/skipped. On failure after two attempts, write FAILED.md in the
   folder explaining why and CONTINUE — never block the batch.

SCHEDULE PLAN (compute only — do NOT upload or schedule)
Group finished Shorts BY CHANNEL (resolve each from its folder's beat-sheet
folderLabel / brand). For each channel, order its Shorts (oldest source date
first), then assign publishAt: the FIRST = that channel's latest scheduled
upload + 1 hour (or "immediate" if the channel has nothing scheduled); each
subsequent Short = previous + 1 hour (stagger, never co-post at one clock
time). Record channel, Shorts playlist target ("Shorts", created on publish
if missing), and computed publishAt per video in
youtube/_916-batch/SCHEDULE-PLAN.md. This is a plan the human executes later;
this run performs no uploads and adds nothing to any playlist.

FINISH
Write youtube/_916-batch/SUMMARY.md: counts (built / skipped-exists /
skipped-no-folder / failed), total Shorts runtime, the list of portrait twins
created, any videos that needed a beat cut (with in→out durations), any that
still need a human pantry override, and the path to SCHEDULE-PLAN.md. End the
run with those counts. Nothing is published.

WORK LIST (id — title — 16:9 duration)
iUXC69MZl8E — Persisting Progress Across Context Windows — 2:12
oPI3c6pf1N4 — The Hard Case — 2:31
mvCN15H91Ko — The Engineer Who Stayed — 3:24
m4tv4cL1l7Y — The Fluency Ceiling — 3:00
kes_0sIS-k8 — Same Text, Better Scaffold — 2:45
c0jDRjBpnQI — The CRA Ladder — 2:56
HcQlKBkA9tM — Caching Pixels You've Already Seen — 2:13
F-3csy0YmMs — Claude, Seeded (Algorithmic-Art Skill) — 5:05
_NBPIIa4fVQ — Claude, Peer-Reviewed — 4:08
P1RfhJJ6hS0 — Claude on the Clock — 4:58
QENWK9l8J9s — When Safety Training Fails — 1:51
Dm8-lZ-Y0ZE — The Sycophancy Gradient — 2:00
1yCYkISIMDQ — An Off Switch for Dangerous Knowledge — 3:25
okgNY7sHYmE — What 81,000 People Want from AI — 3:21
fR9GCsYtjYs — Claude's Values Across Models and Languages — 3:03
YuKL035BUuQ — Every Remotion Move, One Logo — Musinique Mark 2 (16:9) — 3:46
3dSlg4LGV60 — Every Remotion Move, One Logo — Musinique Mark (16:9) — 3:43
gD-MhJlFHtA — Every Remotion Move — Bear Brown Initials (16:9) — 4:06
9_YRDjgYJgE — Every Remotion Move, One Logo — Bear Brown Mark (16:9) — 3:17
8VVGo70TMlQ — Every Remotion Move — Bear Brown Initials — 3:41
G7GtXjuUhoA — Every Remotion Move, One Logo — Musinique Mark — 3:43
JmkNlXL38sM — Why a Broken Oxygen Sensor... (ccRCC/VHL) — 5:42
WDmrjHrtnlI — One Wordmark, Every Move — HAI Typography (16:9) — 3:01
dFvpoQZdiN4 — Every Remotion Move — H Mark (16:9) — 2:50
wNjxSDwtJgk — Why a Metabolic Enzyme Mutation... (IDH1) — 5:36
uJ4-cBbz4Yg — The pH-Triggered Lock (siRNA/LNP) — 4:25
PK8o4CU_2m8 — The Photoelectric Effect — 3:24
-WCwbxmraIA — Claude, For Teachers — 2:11
4HoBA5otwMU — Claude, On Average — 2:29
eX_jbpfwmI0 — Claude, Taught — 2:13
```

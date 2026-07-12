---
name: audit
description: Audit the state of every vox video across all books and write vox/YOUTUBE.MD. Use when the user types `audit`, `youtube status`, `video status`, asks what's built/finalized, which reels need 16:9 or 9:16, or for a state-of-everything report. Deterministic and idempotent — safe to re-run anytime.
---

# audit — state of every vox video → vox/YOUTUBE.MD

Scans **every book** (`books/<book>/youtube/`), finds each built reel, checks its
state, and writes a single report to **`vox/YOUTUBE.MD`**. It is a **pure function of
the filesystem** — no partial state, no credits, no network.

## Command
```bash
python3 scripts/vox_audit.py            # writes vox/YOUTUBE.MD
```
That's the whole audit. It runs in ~1s over ~180 reels.

## Why it can't "hit a limit"
The audit is a deterministic script, not an LLM pass — it finishes in one shot and
cannot run out of context. **If Claude Code stalls, waits on a rate limit, or restarts,
just run the command again**: it regenerates the full, current report from what's on
disk. There is nothing to resume and no state to corrupt. (The long, limit-prone work
is *finishing* the reels the report flags — that resumes the normal vox way, via the
report + `QUEUE.md`. The audit itself is instant.)

## State model (per reel, by file presence)
- **planned** — `beat_sheet.json` exists, no review cut yet.
- **slate-cut** — `<slug>-review.mp4` exists (preview, may still have open slates).
- **16:9** — a landscape final cut is in `mp4/` (the master; slates filled).
- **9:16** — a portrait final cut is in `mp4/` (the short).
- **complete** — both 16:9 and 9:16 present.
- **[BLOCKED]** — a `layout_audit.md` is present (a gate failed on that reel).

Aspect (16:9 vs 9:16) is decided by `ffprobe` on the cut's dimensions, with a
filename fallback (`short`/`916`/`vert` → 9:16) if `ffprobe` is absent. "Open slates"
counts beats with no filled `media/<BID>.(mp4|png|jpg)` or `manim/<BID>.(mp4|mov)`.

## What the report contains
1. **Summary** — totals: reels, books, complete, 16:9, 9:16, slate-cut only, planned,
   blocked, and books with an empty `youtube/`.
2. **Needs attention** — blocked reels and slate-cuts not yet finalized, each with the
   next action (fill slates / run `final cut`).
3. **Full inventory** — every reel: beats, duration, review/16:9/9:16 ✓, open slates, state.
4. **Empty books** — youtube/ folders scaffolded but with no reels built yet.

## Options
```bash
python3 scripts/vox_audit.py <BOOKS_ROOT>     # audit a different books/ dir
python3 scripts/vox_audit.py --out <PATH>     # write the report elsewhere
```
Defaults: `BOOKS_ROOT` = the `books/` dir above `vox/`; out = `vox/YOUTUBE.MD`.

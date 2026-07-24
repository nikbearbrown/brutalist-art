# SERIES-BUILD-PROMPT — claude-explainer E5–E9

Paste into Claude Code from `books/` (typically `claude --dangerously-skip-permissions`):

```
Build the claude-explainer series one episode at a time, waiting for my feedback between episodes. Never build two episodes in one turn.

Ground truth, read all of it before episode one:
1. brutalist-art/youtube/SERIES-ROADMAP-claude-explainer.md — the slate: E5 claude-taught ("Wagwan, Bear" — the Wagwan check fires), E6 claude-scripted ("Habari, Bear"), E7 claude-on-average ("Annyeong, Bear"), E8 claude-steered ("Bula, Bear"), E9 claude-judged ("Vanakkam, Bear"). Each entry has the premise, thesis line, cold-open command, beat sketch, and spark lines — treat them as the approved creative brief.
2. brutalist-art/skills/make/ai-explainer/SKILL.md and brutalist-art/CLAUDE-BRAND.md — the laws: cold open on ClaudeComposerAsk, spark line on every inner beat (never a lonely asterisk; typing is B00-only), Onda code-block for anything code (never re-skinned), ASK→RESULT pairs for any generated graphic (composer micro-beat showing the real generation prompt, then the Manim/Remotion result in the channel palette; unfilled media renders as a PIPELINE slate), verdict as a one-page artifact view, HANDOFF beat second-to-last (composer, greeting 'Your turn.', a paste-ready prompt directly relevant to the episode, runningText 'paste this into Claude…', type-on — typing appears only in cold open and handoff), title-restate outro, Title Case segments, one terracotta accent, GATE P before audio spend.
3. brutalist-art/youtube/claude-on-empty/ and brutalist-art/youtube/claude-unsupervised/ — the two exemplar reels. Their beat_sheet.json is the schema to copy; their remotion-src/ (Empty.tsx, Unsupervised.tsx) is the composition pattern to adapt per episode.

Per episode, in order E5 → E6 → E7 → E8 → E9:
1. Create brutalist-art/youtube/<slug>/ with beat_sheet.json (9–10 beats from the roadmap's sketch; write full Teardown narration; compute and record the Wagwan check; per-beat sparkLine props; verdict artifactLines; a HANDOFF beat before the outro with the episode's paste-ready prompt).
2. Write PEDAGOGY.md — an honest audit against the SLATE-RUNNER checklist in the style of the exemplars (act structure, cold open, gap formula, utility lint, vocabulary law, length law, narration spot-check). If the script fails a check, REWRITE the narration until it passes; only then end the file with "VERDICT: PASS". For E7 (claude-on-average) add a fact-check section — keep every LLM claim mechanistic and verifiable, no benchmark claims.
3. Write NARRATION-GATE-P.md (the sign-off table) and BUILD-PROMPT.md (this episode's standalone rebuild prompt, patterned on the exemplars').
4. Generate audio: python3 runtime/scripts/generate_audio.py youtube/<slug>/ from brutalist-art/. ffprobe each mp3 → actual_duration_s into the beat sheet.
5. Build the composition in brutalist-art/skills/make/component-showcase/remotion, adapting the exemplar pattern (new callout items aimed at the right window elements, new spark lines, episode's verdict page, title-restate outro). No Caption bar — that was previz-only. Conform: frames = ceil((mp3 duration + 0.4) * 30) per beat; mp3s in public/mp3/.
6. Render at --scale=1.5 (1280x720 authored → 1920x1080) to youtube/<slug>/media/final-cut.mp4.
7. QC: ffprobe (audio present, duration = frames/30 ±0.2s); extract stills of B00, one mid beat, the verdict, and the outro, and LOOK at them against the laws.
8. Report: per-beat durations, total runtime, QC findings, file path, and the narration table.

Then STOP. Do not start the next episode. Wait for my reply:
- If I type "next" — proceed to the next episode in order.
- If I give feedback or changes — apply them to the CURRENT episode only (edit the beat sheet, regenerate only the affected beats' audio with --only, re-conform, re-render), re-run QC, report, and wait again. A changed beat means its mp3 AND its timing regenerate; untouched beats keep their audio.
- If I type "skip" — leave the current episode as-is and move to the next.
- If I type "stop" — end the run and summarize what's built and what's pending.

Never publish or upload anything at any point. GATE P is per-episode and never bypassed.
```

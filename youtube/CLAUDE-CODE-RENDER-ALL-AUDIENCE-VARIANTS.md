# Claude Code Prompt — Render All Medhavy and HAI Variants Unattended

Run Claude Code from:

`/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art`

Then paste this entire prompt:

```text
Run the complete audience-variant production pipeline for all four jobs below. This is an unattended batch. Do not pause for approval or ask questions. Make reasonable in-scope implementation decisions, continue through audio generation, visual rendering, compilation, QC, and final verification. Do not publish, upload, push, commit, or modify either canonical source reel.

JOBS

1. Medhavy — Claude, Judged
Authoritative sheet:
/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/youtube/medhavy-claude-judged/beat_sheet.medhavy.json
Required output:
/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/youtube/medhavy-claude-judged/claude-judged-medhavy.mp4

2. HAI — Claude, Judged
Authoritative sheet:
/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/youtube/hai-claude-judged/beat_sheet.hai.json
Required output:
/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/youtube/hai-claude-judged/claude-judged-hai.mp4

3. Medhavy — Claude, On Average
Authoritative sheet:
/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/youtube/medhavy-claude-on-average/beat_sheet.medhavy.json
Required output:
/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/youtube/medhavy-claude-on-average/claude-on-average-medhavy.mp4

4. HAI — Claude, On Average
Authoritative sheet:
/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/youtube/hai-claude-on-average/beat_sheet.hai.json
Required output:
/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/youtube/hai-claude-on-average/claude-on-average-hai.mp4

CANONICAL SOURCES — READ-ONLY REFERENCES

/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/youtube/claude-judged/
/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/youtube/claude-on-average/

Never modify, rename, overwrite, or regenerate files inside those two canonical directories. They are factual and visual references only.

READ THESE RULES COMPLETELY BEFORE ACTING

- AGENTS.md
- skills/make/medhavy/SKILL.md
- skills/make/hai/SKILL.md
- runtime/voices/wonder/VOICE.md
- runtime/voices/pragmatist/VOICE.md
- skills/make/audience-preset/brands/medhavy.md
- skills/make/audience-preset/brands/hai.md
- docs/remotion-best-practices/SKILL.md

UNATTENDED EXECUTION RULES

- Do not pause at GATE P. Perform the pedagogy audit yourself and continue only when its written verdict is PASS. If it fails, repair the audience-namespaced variant, rerun the audit, and continue after it passes.
- Kokoro is authorized for every narration beat. Generate all audio without requesting approval.
- Do not switch to ElevenLabs. Use the configured Kokoro voices.
- Local Remotion, ffmpeg, ffprobe, and repository render scripts are authorized. Run the complete local pipeline without approval pauses.
- Never spend money, call paid media-generation services, publish, upload, push, commit, or contact anyone.
- Process jobs sequentially so logs and failures are attributable to one variant.
- A failure in one job must not stop later jobs. Record it, continue, then retry failed jobs once after the first pass.
- Do not produce double-prefixed slugs.
- Do not rename or overwrite the authoritative variant sheets. If a runtime tool requires beat_sheet.json, create a documented build-only copy or symlink inside that variant directory.

AUDIENCE REQUIREMENTS

Medhavy jobs:
- Register: Wonder.
- Voice: Kokoro af_kore.
- Palette: Medhavy Okabe-Ito.
- Typography: EB Garamond and Montserrat.
- Outro: Medhavy.com OutroCTA.
- No exercise beat.
- B08 must state both when to use AI and when not to use AI without turning into a drill.

HAI jobs:
- Register: Pragmatist.
- Voice: Kokoro am_onyx.
- Palette: Humanitarians.
- Typography: EB Garamond and Montserrat.
- Outro: Humanitarians AI OutroCTA.
- Preserve B08's runnable cli_exercise, including ASK, OUTPUT, CHANGE, OUTPUT 2, and concrete next step.
- B08 must state both when to use AI and when not to use AI as an operational decision rule.

PIPELINE FOR EACH JOB

1. Parse and validate the authoritative JSON.
2. Confirm exactly ten beats and closing order B07 VERDICT → B08 AI-USE-BOUNDARY → B09 OUTRO.
3. Confirm the metadata voice, register, palette, slug, and output filename match the job.
4. Write PEDAGOGY.md in the variant directory. Audit factual preservation, learning sequence, audience register, the B08 use/do-not-use boundary, and the outro. End with VERDICT: PASS. If not PASS, repair only the variant and rerun.
5. Preserve the source facts and visual argument. Do not fabricate claims.
6. Generate fresh per-beat Kokoro narration from the variant narration. Never reuse canonical Bear audio. Measure every MP3 and write actual_duration_s only into the build copy used by the renderer.
7. Re-render every Remotion beat in the target audience palette. Do not copy stale Claude-colored frames where doing so violates the target palette.
8. Render B08 and B09 from their specified Remotion components. Ensure no stale @NikBearBrown outro, canonical voice, or canonical palette remains.
9. Compile a clean 1920×1080 MP4 using narration as the master clock. No missing-media slates, silent voiced beats, clipped text, broken fonts, or placeholder cards.
10. Generate a QC contact sheet. Inspect every beat for clipping, legibility, wrong palette, stale branding, incorrect beat order, and unintended blank frames. Repair and rerender failures automatically.
11. Verify the final with ffprobe: 1920×1080 video stream, audio stream present, non-trivial file size, and duration consistent with summed measured beats.
12. Confirm the exact required output filename exists.

CONTENT-SPECIFIC CHECKS

Claude, Judged:
- Preserve the distinction between determinable checks and judgeable decisions.
- Preserve the claim that agents can inspect schema, timing, paths, resolution, and QC artifacts.
- Preserve human authority over interest, fairness, worth, and publication.
- B08 must distinguish evidence-based reversible checks from human accountability.

Claude, On Average:
- Preserve that generation proceeds token by token from context-conditioned probabilities.
- Preserve that responses are samples from a distribution.
- Preserve that temperature zero narrows selection but does not guarantee a context-independent fixed answer.
- B08 must distinguish useful variation for exploration from unsafe reliance on one unverified draw for exact or high-consequence decisions.

FINAL BATCH REPORT

Write:
/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art/youtube/AUDIENCE-VARIANTS-RENDER-REPORT.md

For each of the four jobs report:
- status: BUILT or FAILED
- authoritative beat sheet
- final MP4 path
- voice and palette
- beat count
- measured duration
- file size
- resolution
- audio stream present
- PEDAGOGY verdict
- QC contact-sheet path
- repairs made
- remaining concerns
- ready-to-paste command: open /absolute/path/to/final.mp4

At the end report totals: attempted, built, failed. Do not claim success unless the final file exists and passes ffprobe. Do not publish or push anything.
```

# Claude Code Prompt — Convert One Video to Medhavy and HAI

Run Claude Code from:

`/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art`

Replace `SOURCE_REEL` with the absolute path to the reel folder, then paste the complete prompt below.

```text
SOURCE_REEL=/absolute/path/to/the/source/reel

Convert SOURCE_REEL into two fully rendered audience variants: Medhavy and HAI. Run the complete local pipeline without approval pauses. Do not publish, upload, push, commit, use ElevenLabs, or call paid media-generation services.

READ COMPLETELY BEFORE ACTING

- AGENTS.md
- skills/make/medhavy/SKILL.md
- skills/make/hai/SKILL.md
- skills/make/explainer/SKILL.md
- runtime/voices/wonder/VOICE.md
- runtime/voices/pragmatist/VOICE.md
- skills/make/audience-preset/brands/medhavy.md
- skills/make/audience-preset/brands/hai.md
- docs/remotion-best-practices/SKILL.md

The source reel and every source asset are read-only. Never modify, rename, overwrite, crop, recolor, annotate, enhance, regenerate, or delete anything inside SOURCE_REEL.

OUTPUTS

If SOURCE_REEL is <book>/youtube/<slug>/, create:

- <book>/youtube/medhavy-<slug>/
  - beat_sheet.medhavy.json
  - <slug>-medhavy.mp4
- <book>/youtube/hai-<slug>/
  - beat_sheet.hai.json
  - <slug>-hai.mp4

Do not create double-prefixed slugs. Never overwrite an existing variant without first preserving its authoritative beat sheet and reporting what already exists.

THE MEDIA-OWNERSHIP RULE

Before rewriting anything, classify every source beat in MEDIA-LEDGER.md:

1. HUMAN-PROVIDED MEDIA
   - Any existing source `media/<beat>.mp4|mov|png|jpg|jpeg|webp`, screen recording, archive clip, photograph, illustration, or other supplied asset.
   - Treat an ambiguous existing asset as human-provided.
   - Record its absolute source path, byte size, SHA-256, dimensions, duration if video, and beat ID.

2. CLAUDE-GENERATED VISUAL
   - A beat whose visual is generated from code or structured props: Remotion, Manim, D3, cards, diagrams, charts, Claude UI components, slates, or an explicitly marked generated asset.
   - Record the generating scene/component/script and beat ID.

Human-provided media always wins when both classifications appear possible. Do not replace supplied media with a generated approximation.

HUMAN-PROVIDED MEDIA MUST NOT VISUALLY CHANGE

- Copy or symlink the exact supplied asset into each audience variant. Verify the copied source asset has the same SHA-256 as the original.
- Do not crop, reframe, color-grade, desaturate, recolor, retouch, sharpen, denoise, upscale, add text, add borders, add overlays, remove objects, regenerate frames, or change aspect ratio.
- Do not alter the source file itself.
- The only permitted adaptation is temporal conformance in a derived `clips/` file so the media matches the newly measured narration MP3.
- If the media is longer than the narration window: shorten it by trimming time only. Preserve the opening and the key action; trim the tail unless the beat sheet explicitly identifies a better in/out point.
- If the media is shorter than the narration window: lengthen it by uniform retiming only. Never freeze the last frame and never synthesize new frames. Preserve pitch by stripping the source audio and using narration as the only soundtrack.
- Keep aspect ratio exactly. If canvas fitting is required, pad/letterbox; never crop or stretch.
- Do not exceed 3× slowdown. If a clip would require more than 3× slowdown, keep the narration for that beat closer to the source duration instead of damaging the media.
- Stills remain the same pixels. They may be held for the MP3 duration. Do not add a new Ken Burns move unless the source beat already used one.
- All retiming is derived and reversible. MEDIA-LEDGER.md must show source path → derived clip path → original duration → MP3 duration → trim/retime factor.

NARRATION RULE FOR HUMAN-PROVIDED MEDIA BEATS

Keep the narration on human-provided-media beats the same or extremely close to the source:

- Preserve the same factual claims, referents, order of ideas, proper nouns, numbers, and relationship between spoken words and what appears on screen.
- Prefer a register edit, not a rewrite.
- Target the original word count and sentence timing within approximately ±10%.
- Do not introduce a new example, visual referent, claim, list item, or action that the supplied media does not show.
- If the original narration names an on-screen object or action, keep that reference at approximately the same relative point in the beat.
- If Kokoro voice timing differs, conform the media duration to the measured MP3. Do not rewrite away the meaning merely to hit an estimated duration.

CLAUDE-GENERATED VISUAL BEATS MAY CHANGE

For Remotion, Manim, D3, cards, diagrams, charts, Claude UI beats, slates, and other generated visuals:

- Rewrite narration fully into the target audience register while preserving facts.
- Regenerate the visual to fit the rewritten narration, measured MP3 duration, audience palette, and typography.
- Update on-screen copy so it agrees with the new narration.
- Re-time reveals to the new voice.
- Preserve the beat's pedagogical job and act unless the audience skill explicitly requires an added ending beat.
- Do not copy stale source-brand frames when the target palette or outro differs.

MEDHAVY VARIANT

- Scaffold with `python3 runtime/scripts/brand_variant.py "$SOURCE_REEL" medhavy` or the equivalent safe command after resolving SOURCE_REEL.
- Authoritative sheet: `beat_sheet.medhavy.json`.
- Register: Wonder—first principles, genuine curiosity, intellectual honesty.
- Voice: Kokoro `af_kore`.
- Palette: Medhavy Okabe-Ito.
- Typography: EB Garamond and Montserrat.
- Preserve human-media narration closely under the rule above.
- Generated-visual narration may vary more substantially to become a coherent Wonder explanation.
- No CLI exercise or drill beat.
- Optional experiment tangent only when naturally earned.
- Final beat: Medhavy.com OutroCTA.

HAI VARIANT

- Scaffold with `python3 runtime/scripts/brand_variant.py "$SOURCE_REEL" hai` or the equivalent safe command after resolving SOURCE_REEL.
- Authoritative sheet: `beat_sheet.hai.json`.
- Register: Pragmatist—method, when to use it, when not to use it, failure conditions.
- Voice: Kokoro `am_onyx`.
- Palette: Humanitarians.
- Typography: EB Garamond and Montserrat.
- Preserve human-media narration closely under the rule above.
- Generated-visual narration may vary more substantially to become an operational Pragmatist explanation.
- Add the required runnable HAI CLI worked exercise as the second-to-last beat. It is a newly generated beat and may use a freshly rendered Claude/terminal visual.
- Final beat: Humanitarians AI OutroCTA.

UNATTENDED PIPELINE FOR EACH VARIANT

1. Inspect and validate the source beat sheet, all media, generated scenes, audio, and existing final cut.
2. Write MEDIA-LEDGER.md before copying or rendering anything.
3. Scaffold the audience-namespaced variant. Never modify the canonical source.
4. Rewrite the beat sheet following the human-media versus generated-visual rules above.
5. Preserve beat IDs for all inherited beats. New required ending beats get unique IDs without renumbering or reassigning supplied media.
6. Write PEDAGOGY.md and FACTCHECK.md. Repair the variant until both end with VERDICT: PASS. Do not pause for approval.
7. Generate fresh Kokoro MP3s for every voiced beat. Never reuse the original narrator's audio. Measure every MP3 and write real `actual_duration_s` values only into the audience variant/build copy.
8. Copy or symlink every human-provided media source without changing its bytes. Verify SHA-256 equality.
9. Conform human-provided video into derived beat clips by trim or uniform retime only. Strip source audio. Preserve aspect ratio and pixels. Do not apply the audience palette to supplied media.
10. Render generated visual beats anew in the target palette, synchronized to the new MP3s.
11. Compile a complete clean 1920×1080 video. Narration is the master clock. No missing-media slates, silent voiced beats, placeholders, clipped copy, or stale source-brand outro.
12. Generate a QC contact sheet and inspect every beat.
13. For human-provided beats, compare source and variant frames to confirm the image content is unchanged apart from temporal position and padding. Confirm source-file SHA-256 remains identical.
14. Verify the final with ffprobe: 1920×1080, audio stream present, non-trivial file size, and duration consistent with measured beats.
15. Open both final MP4s for human review.

FAILURE HANDLING

- Do not stop the batch because one variant fails. Record the failure, continue with the other variant, then retry the failed variant once.
- Repair local code, paths, fonts, timing, or rendering problems automatically.
- Never solve a timing problem by altering human-provided imagery beyond trimming or uniform retiming.
- Never substitute generated media for missing or difficult human-provided media.
- If the source lacks an asset required by its own beat sheet, leave a clearly reported blocker rather than fabricating it.

FINAL REPORT

Write `<source-parent>/<slug>-MEDHAVY-HAI-RENDER-REPORT.md` containing:

- source reel path and source final-video path
- Medhavy and HAI authoritative beat-sheet paths
- final MP4 paths
- status: BUILT or FAILED
- voice, register, palette, beat count, duration, resolution, audio-stream status, and file size
- PEDAGOGY and FACTCHECK verdicts
- QC contact-sheet paths
- all human-provided beat IDs
- SHA-256 verification results for supplied media
- all media duration changes: source duration, MP3 duration, trim/retime factor
- all generated beats that were redesigned for the new voice
- repairs made and remaining concerns
- ready-to-paste commands:
  `open /absolute/path/to/<slug>-medhavy.mp4`
  `open /absolute/path/to/<slug>-hai.mp4`

Do not claim success unless both final files actually exist and pass ffprobe. Do not publish or push.
```

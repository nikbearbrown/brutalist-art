# NARRATION — GATE P sign-off · The Ad That Answered Itself (SHOW-first rebuild)

> **STOP.** No audio generated, nothing rendered. Reply with edits, or "go" to spend
> audio (Kokoro `am_onyx`, free/local). `generate_audio.py` runs only after sign-off.

Reel: `brutalist-art/youtube/claude-liam-can-ai-be-trusted-ad/`
Channel: claude-liam (@NikBearBrown) · Liam, in for Bear · Teardown · ~2:23 est.

**Rebuilt under the strengthened SHOW-DON'T-TELL LAW**: every body beat now carries a
`show` block (ordered visual events); evidence lands ON SCREEN (verbatim comment cards,
the ad's own questions, the strike-through edit, the waveform); narration cut to 41–58
words per body beat — the voice reacts to the screen. The slate previz ANIMATES the
show events at estimated timing — review it by watching, not reading.

| Beat | Act | Est. | Sign | What the viewer WATCHES · what the voice says |
|---|---|---|---|---|
| B00 | ASK | 14s | ☐ | Command types on, send arms, RESULT lines land ("99 comments read — three camps found"). VO: ad setup + "This is Liam, in for Bear. The internet answered for them. Watch." (36 w) |
| B01 | BODY | 16s | ☐ | The ad's OWN questions land as grain polaroids, one per phrase; a ghost "?" forms behind. VO: what the ad is; "asking is not answering." (46 w) |
| B02 | BODY | 15s | ☐ | Verbatim comment cards drop in — praise left-tilt, attacks right-tilt; counter climbs to 99+. VO: it worked; credit given; "what did the conversation conclude?" (43 w) |
| B03 | BODY | 16s | ☐ | Six frame-cards SORT themselves on the spoken cue — warm → "NO AI IN IT", ominous → "THE AI"; @bong-garcia's "Bravo, Anthropic!" stamps. VO: 41 w. |
| B04 | BODY | 18s | ☐ | "Can ~~AI~~ be trusted?" — the strike draws ON the spoken word; "the companies building it" types in; @BenGrimm977's card slides up. VO: 58 w. |
| B05 | BODY | 15s | ☐ | Live piano waveform plays; track-ID comments ping in; card flips: Duval Timothy — "Ball" (2017); stamp: "recorded 9 years before the ad". VO: 50 w. |
| B06 | VERDICT | 22s | ☐ | Artifact page writes itself — each line reveals on its spoken phrase; final line holds alone. VO: 70 w (spoken artifact lines — exempt bookend). |
| B07 | HANDOFF | 22s | ☐ | Composer, "Your turn.", prompt types on: watch it silent, then sound-only — which cut wins? VO ends "Liam, in for Bear." (61 w) |
| B08 | OUTRO | 5s | ☐ | Title restates, terracotta period, handle, "Liam, in for Bear." |

## Law audit

- **SHOW-DON'T-TELL**: every body beat has a `show` block; evidence on screen, voice reacts; no beat passes as a static slide. PPT test: pass. ✓
- **Narration budget**: body beats 41–58 words (bookends exempt). ✓
- **Cold open**: B00 = ClaudeComposerAsk WITH result lines (the ask lands answered). ✓
- **Handoff / typing**: typing in exactly B00 + B07; handoff greeting "Your turn." ✓
- **In-for-Bear**: spoken in B00 and B07/B08. ✓ · **Wagwan check**: "Yassou, Liam" (Greek). ✓
- **Illustrate law**: B01–B05 five distinct schemes (question-stack, comment-rain, sort-split, strike-swap, waveform); no two consecutive beats share a scheme. ✓
- **Evenhanded**: praise cards land on screen alongside attacks (B02); verdict credits craft first. ✓

## What happens on "go"

1. `python3 runtime/scripts/generate_audio.py youtube/claude-liam-can-ai-be-trusted-ad/` (Kokoro am_onyx).
2. ffprobe each mp3 → `actual_duration_s`; map `show[].at` fractions onto real durations (sub_beats for mid-sentence hits).
3. Build the five concept scenes + ClaudeComposerAsk/Verdict/TitleOutro per the show blocks; conform to audio.
4. Render `[slug].mp4` + `[slug]-slate.mp4`; VISUAL QC (frame sampling, 9-point rubric). **Never publish.**

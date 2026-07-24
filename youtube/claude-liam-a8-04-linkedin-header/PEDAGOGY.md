# PEDAGOGY audit — claude-liam-a8-04-linkedin-header ("Design a LinkedIn Header That Actually Works (1584 × 396)")

ai-explainer (pragmatist register — how-to). claude-liam, Kokoro am_onyx.
Episode 4 of the "Ship It" series (INFO 7375 Assignment 8). Audited against ai-explainer house + frame laws.

## Act structure
- B00 cold open → B01 exact dimensions and why → B02 set up the canvas with AI → B03 apply brand colors, type, and value prop → B04 safe zone and mobile crop check → B05 export PNG and assemble PDF → B06 beginner traps → BVDT verdict → BHTF your turn handoff → BOUT outro. 10 beats. PASS

## Cold open (COLD OPEN LAW)
- B00 is ClaudeComposerAsk. Liam self-introduces ("Hola — this is Liam"). Output line names the deliverable: 1584 × 396 px, safe zone right 75%, brand + tagline, export PNG then PDF. PASS

## Gap formula / hook
- Episode 4 opens with two concrete failure modes: wrong dimensions compress the header into a blurry stripe, and text placed in the wrong zone is hidden behind the profile photo on mobile. The grader uses a phone. Resolution: exact pixel dimensions, a precisely defined safe zone (right 75%, left 25% is danger), a four-element brand application checklist, a mobile crop check before export, and a PNG-not-JPEG export that preserves crisp edges before LinkedIn's own compression. PASS

## Utility lint
- BHTF prompt produces the full header generation prompt (1584 × 396, PRIMARY_HEX, ACCENT_HEX, FONT_DESCRIPTION, BRAND_ADJECTIVE, NAME, ROLE, TAGLINE with 8-word cap, no text in left 250 pixels) — directly usable as the Canva AI / Adobe Firefly / DALL·E generation prompt for the 15-point LinkedIn header deliverable. The prompt is read aloud and discussed: pull brand sheet first (primary hex, accent hex, brand font, role), fill every bracket before pasting, add name and tagline in the right half of the canvas after generation, check the safe zone, export as PNG, assemble the PDF (HANDOFF LAW). PASS

## Vocabulary / register (Pragmatist)
- Steps-first throughout: dimensions and safe zone explained with specific pixel values in B01 (1584 × 396, left ~400 px danger zone, desktop photo overlap ≈ 152 px wide), the four brand elements listed in order in B03 (name, tagline ≤8 words, one brand visual element, accent color present), the five export steps numbered in B05 (File → Download → PNG, then PDF assembly). Every term defined on first use: "safe zone" in B01, "subdomain / URL slug" referenced in B05 context. No "just." Brand continuity reminders thread through B02 (specify brand hex codes in the generation prompt), B03 (all four elements come from the A6/A7 brand sheet), B04 (right 50% bulletproof, right 75% comfortable minimum), and B06 (trap 4: without hex codes the AI picks a generic blue-to-purple gradient). PASS

## Honesty (DOUBLE-CHECK LAW)
- B04 explicitly names the "text behind profile photo" trap: anything placed in the left 25% is hidden by the profile photo on mobile, and "the grader uses a phone." B06 names trap 4 directly: when a generation prompt omits hex codes, "it picks a generic gradient — usually blue-to-purple — that has nothing to do with your brand." B05 explains why PNG is required over JPEG: LinkedIn compresses on upload, so starting with the cleanest source (PNG, which preserves sharp edges) reduces the compound quality loss. B04 adds the mobile crop note that the danger zone can widen toward the center on some phone screens, reinforcing conservative safe-zone placement. PASS

## Length law
- 10 beats, est. ~379s (~6:19) at Kokoro pace (B00 26s + B01 52s + B02 26s + B03 50s + B04 48s + B05 46s + B06 52s + BVDT 38s + BHTF 36s + BOUT 5s). Appropriate for a how-to episode covering LinkedIn's technical spec, a two-stage AI-assisted design workflow (background generation + Canva composition), a safe-zone visual check, PNG export rationale, and four graded traps. PASS

## Visual law spot-check
- ILLUSTRATE LAW: ClaudeComposerAsk for prompt beats (B00, B02, BHTF); ClaudeWindow for informational/checklist beats (B01, B03, B05, B06); custom Remotion A8HeaderSafeZone for the illustrated safe zone / danger zone diagram with mobile crop annotation (B04); ClaudeVerdictArtifact for the verdict (BVDT); ClaudeTitleOutro for outro (BOUT). ASK→RESULT: B02 shows the background generation prompt in ClaudeComposerAsk with two output lines confirming canvas size and next step; B04 shows the safe zone diagram as the result of the "picture a vertical line" instruction. SparkLine on all body beats ("1584 × 396. Right 75% is your canvas." / "Name. Tagline. Brand element. Accent. That's four." / "Right 75% is safe. Right 50% is bulletproof." / "PNG out of Canva. PDF for submission." / "Dimensions. Safe zone. 8-word max. Your hex codes."). No fabricated screenshots (REBUILD LAW). PASS

VERDICT: PASS

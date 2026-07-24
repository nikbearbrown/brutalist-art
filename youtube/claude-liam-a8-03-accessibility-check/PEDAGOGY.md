# PEDAGOGY audit — claude-liam-a8-03-accessibility-check ("The Color Accessibility Check (WebAIM), Step by Step")

ai-explainer (pragmatist register — how-to). claude-liam, Kokoro am_onyx.
Episode 3 of the "Ship It" series (INFO 7375 Assignment 8). Audited against ai-explainer house + frame laws.

## Act structure
- B00 cold open → B01 what WCAG contrast is → B02 open WebAIM and enter hex codes → B03 read the pass/fail result → B04 when it fails — how to fix with Claude → B05 repeat for all combos and export PDF → BVDT verdict → BHTF your turn handoff → BOUT outro. 9 beats. PASS

## Cold open (COLD OPEN LAW)
- B00 is ClaudeComposerAsk. Liam self-introduces ("Hola — this is Liam"). Output lines name the deliverable: WCAG AA thresholds (4.5:1 normal / 3:1 large), the tool (webaim.org, free, no login), and the submission artifact (one PDF with every passing combination). PASS

## Gap formula / hook
- Episode 3 opens with the tension that a brand palette that looks beautiful on screen may fail a purely mathematical accessibility standard — and the failure is invisible to the designer's eye until it is measured. A secondary tension: when the palette fails, students guess at replacement hex codes slowly and often land on something that passes but looks wrong. Resolution: a free one-URL tool that gives an instant ratio, plus a Claude prompt that produces three pre-verified compliant alternatives when the ratio fails. PASS

## Utility lint
- BHTF prompt produces the compliant-alternatives prompt (text hex, background hex, failing ratio, three alternative text colors with predicted ratios) — directly usable as the Claude session prompt when the WebAIM result fails, and as the path to the PDF deliverable worth 5 points. The prompt is read aloud and discussed: open WebAIM first, enter primary text and background hex codes, read the ratio, screenshot if it passes (4.5:1 or higher), paste the fix prompt into Claude only if it fails, then run all remaining text-on-background combinations (heading, body, button, link) and assemble the single PDF (HANDOFF LAW). PASS

## Vocabulary / register (Pragmatist)
- Steps-first throughout: WCAG vocabulary defined once and concisely in B01 (WCAG, AA, 4.5:1, 3:1, contrast ratio as mathematical luminance comparison), the WebAIM input flow stated as numbered steps in B02, the result reading explained precisely in B03 (four rows, two AA targets, green = PASS, screenshot requirements). Every term defined on first use: "contrast ratio" and "relative luminance" in B01, "foreground color" and "background color" in B02. No "just." Brand continuity reminder: B04 opens by telling students not to guess hex codes when a ratio fails — specificity about the failure context is what makes the Claude prompt produce usable alternatives. PASS

## Honesty (DOUBLE-CHECK LAW)
- B04 explicitly instructs students not to guess at hex codes when the ratio fails ("Guessing is slow and you will probably land on something that passes but looks wrong"). The Claude fix prompt includes predicted ratios for each alternative, and students are told to verify each alternative on WebAIM before accepting it — the predicted ratio from Claude is a starting point, not a certified result. The BVDT verdict repeats the skip-the-guessing rule. Screenshot requirements in B03 require the hex inputs, ratio number, and PASS badge all in one frame — preventing a screenshot of only the badge without proof of the measured values. PASS

## Length law
- 9 beats, est. ~305s (~5:05) at Kokoro pace (B00 18s + B01 50s + B02 38s + B03 42s + B04 28s + B05 48s + BVDT 38s + BHTF 38s + BOUT 5s). Appropriate for a how-to episode covering the WCAG standard, a one-URL tool walkthrough, pass/fail reading, a Claude-assisted fix path, and a multi-combo PDF assembly workflow. PASS

## Visual law spot-check
- ILLUSTRATE LAW: ClaudeComposerAsk for prompt beats (B00, B04, BHTF); ClaudeWindow for informational/checklist beats (B01, B03, B05); custom Remotion A8WebAIMStep for the illustrated WebAIM hex-entry and result-reading flow (B02); ClaudeVerdictArtifact for the verdict (BVDT); ClaudeTitleOutro for outro (BOUT). ASK→RESULT: B04 shows the compliant-alternatives prompt in ClaudeComposerAsk with three example output alternatives (hex + predicted ratio + PASS label); B05 shows the full combo checklist as the result artifact. SparkLine on all body beats ("4.5:1 for normal text. 3:1 for large. AA is the floor." / "Free. Instant. No login." / "Normal Text AA: 4.5:1+. Screenshot the PASS." / "Every combo. One PDF."). No fabricated screenshots (REBUILD LAW). PASS

VERDICT: PASS

# PEDAGOGY audit — claude-liam-a8-02-website-responsive ("Build Your Website, Part 2: Make It Not Break on Mobile")

ai-explainer (pragmatist register — how-to). claude-liam, Kokoro am_onyx.
Episode 2 of the "Ship It" series (INFO 7375 Assignment 8). Audited against ai-explainer house + frame laws.

## Act structure
- B00 cold open → B01 what responsive means → B02 mobile preview toggle → B03 the three things that break first → B04 how to ask the AI to fix each → B05 publish and get the live link → BVDT verdict → BHTF your turn handoff → BOUT outro. 9 beats. PASS

## Cold open (COLD OPEN LAW)
- B00 is ClaudeComposerAsk. Liam self-introduces ("Hola — this is Liam"). Output lines name the deliverable: check mobile view (most visitors land here first), fix the three common break points before publishing, the live URL is the deliverable — not the editor preview. PASS

## Gap formula / hook
- Episode 2 opens with the tension that a site which looks correct in the desktop editor can be broken on mobile — and most visitors land on mobile first. A second tension: students mistake the editor URL or preview URL for the assignment deliverable when the live URL is a different address. Resolution: a structured mobile QC pass using the in-editor preview toggle, a single combined fix prompt for all three break points, and a five-step publish workflow that ends with verifying on the actual phone. PASS

## Utility lint
- BHTF prompt produces the three-break-point mobile fix prompt (hero text overflow, fixed-width images, broken hamburger menu) — directly usable as the revision message for the website's mobile layer and as the path to the live URL deliverable. The prompt is read aloud and discussed: use the mobile preview toggle first (not the actual phone), screenshot the Hero section, identify which of the three breaks apply, paste the fix prompt removing only inapplicable lines, then run the five publish steps and paste the live URL somewhere safe before submitting (HANDOFF LAW). PASS

## Vocabulary / register (Pragmatist)
- Steps-first throughout: responsive design defined concisely in B01 (one codebase, multiple layouts; explicit pixel widths for desktop/tablet/phone), the preview toggle located precisely per platform in B02, the three break points named and described before the fix prompt in B03, and the five publish steps numbered in B05. Every term defined on first use: "responsive design" in B01, "hamburger menu" in B03, "URL slug" in B05. No "just." Brand continuity reminder: in B04 students are told to remove only the inapplicable lines from the fix prompt, not to rewrite it, preserving the specificity the tool needs. PASS

## Honesty (DOUBLE-CHECK LAW)
- B01 explicitly states that AI platforms generate responsive code by default "but it does not guarantee it works correctly — it gets the desktop right first and the mobile second, and the mobile often has errors you need to catch and fix." B05 distinguishes three distinct URLs (editor URL, preview URL, live URL) and instructs students to open the live URL on their actual phone after publishing — not in a desktop browser tab — because "the live build can differ from the preview." The BVDT verdict repeats this distinction. PASS

## Length law
- 9 beats, est. ~349s (~5:49) at Kokoro pace (B00 30s + B01 42s + B02 50s + B03 55s + B04 30s + B05 55s + BVDT 36s + BHTF 46s + BOUT 5s). Appropriate for a how-to episode covering responsive QC, platform-specific toggle navigation, three break-point categories, a combined fix prompt, and a five-step publish workflow. PASS

## Visual law spot-check
- ILLUSTRATE LAW: ClaudeComposerAsk for prompt beats (B00, B04, BHTF); ClaudeWindow for informational/checklist beats (B01, B03, B05); custom Remotion A8MobilePreviewStep for the illustrated platform-by-platform toggle guide (B02); ClaudeVerdictArtifact for the verdict (BVDT); ClaudeTitleOutro for outro (BOUT). ASK→RESULT: B04 shows the combined mobile fix prompt in ClaudeComposerAsk; B05 shows the five publish steps as the result checklist. SparkLine on all body beats ("One codebase. Multiple layouts. Test all of them." / "Look for a phone icon or a breakpoint toggle in the preview toolbar — every platform has one." / "Identify which ones your site has before writing the fix prompt." / "The live URL is the deliverable — not the preview."). No fabricated screenshots (REBUILD LAW). PASS

VERDICT: PASS

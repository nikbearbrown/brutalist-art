# NARRATION — claude-liam-claude-science

**GATE P: pending — human sign-off required before audio generation**

Source: Anthropic "The Briefing: AI for Science" (YouTube ID: cd3PsBoGYkc, ~90s)
Transcript: `books/anthropics/youtube-transcripts/claude/transcripts/cd3PsBoGYkc.txt`
Channel: claude-liam | Voice: Kokoro am_onyx | Register: Teardown
Title: **Ten Years Every Year.**
Subline: *The pitch, and the comment section.*

---

## Beat narrations

### YTV01 — Verdict (pre-roll summary)

> Anthropic's pitch for Claude Science comes down to one number: ten years every year. The CEO's 2023 forecast was fifty to a hundred years of biological progress compressed into five to ten — a factor of ten. The pitch video is the case that compression has started. Here's what it shows, what it omits, and what the comment section caught. The toil part is real. The rate-limiting-step question isn't answered. The token architecture isn't addressed. The ×10 only applies where cognition is the bottleneck — and in wet-lab science, often it isn't.

*~35 s | ClaudeVerdictArtifact*

---

### B00 — Cold Open

> Anthropic launched Claude Science. And this is Liam, in for Bear. The pitch video is ninety seconds — music, montage, and one number: fifty to a hundred years of scientific progress compressed to five to ten. Bear had notes. Let's actually look at what the pitch claims, what it demonstrates, what the comment section is asking, and where the number is solid versus where it's doing a lot of work.

*~23 s | ClaudeComposerAsk — greeting: "Yassou, Liam"*

---

### B01 — Scale (50–100 → 5–10)

> The claim is a scale comparison. Dario's 2023 essay: AI could compress fifty to a hundred years of scientific progress into five to ten. That's a factor of ten compression on the timeline. The pitch video is the evidence that compression has started — not fifty years from now, but now. Scale the numbers: fifty years becomes five. A hundred becomes ten. Ten years every year.

*~22 s | ScaleComparison (C2, deckPatterns) — PIPELINE slate until registered in Root.tsx*

---

### B02 — Attrition (3 days vs 3+ weeks)

> The first concrete evidence. An experiment takes three days to run — then three or more weeks to analyze. Those weeks aren't science. They're the toil you endure to get to the science. That toil is collapsing. Three days of experiment. Three-plus weeks of analysis: reading, pattern-matching, report generation. Claude Science targets that middle. If analysis goes from weeks to hours, you've compressed the research cycle by a real factor — not a promised one.

*~27 s | AttritionChain (C2, deckPatterns) — PIPELINE slate until registered in Root.tsx*

---

### B03 — Human + AI

> The scientist in the video says it plainly: no human would have thought of that hypothesis. We needed the kind of experimental science and thinking AI cannot help you with. You put these two things together, you get your answer. The architecture: AI supplies hypotheses from literature synthesis. Human designs and runs the experiment. Human checks the reasoning. AI doesn't design a novel experiment from unknown physics — but it can read everything published on protein folding faster than any human lab. The loop is the product.

*~27 s | SourceFlow (C3, structural.tsx)*

---

### B04 — ×10 Meter

> What ×10 actually looks like. Not ten times as many papers. Not ten times as many labs. The meter: a researcher who spent three weeks on analysis now spends three days. An understaffed team can interrogate a literature base they couldn't afford to hire someone to read. A single investigator can develop hypotheses across five subfields instead of one. That's the compressible version of ×10. The meter moves where cognition is the constraint — not where the constraint is the bench, the reagents, or the instrument queue.

*~28 s | LayerStack (C3, structural.tsx) — three rows of compression*

---

### B05 — Hype (ChipGrid)

> The pitch's aspirational layer. More diseases treated. Undruggable targets drugged. Entire underexplored fields opened up. Faster diagnoses. Bigger public health impact. These are real outcomes if the timeline compresses at scale. The question is the causal chain: how long between "Claude reads the literature" and "the drug passes Phase 3"? The wet-lab steps, regulatory pathways, and manufacturing don't compress with the analysis. The comment section noticed this gap between the pitch and the proof.

*~25 s | ChipGrid (C3, structural.tsx) — 5 aspiration chips + 1 warn chip*

---

### B06 — Token Meter

> The constraint the video doesn't mention. A serious research project — a protein structure, a clinical trial dataset, a corpus of papers on a single target — routinely exceeds what fits in a single context window. Claude Science has to handle document chunking, retrieval augmentation, and memory across multi-session work. The token budget is a real ceiling. The launch doesn't say what the architecture is. That matters for whether ×10 applies to deep single-target work or only to literature synthesis at the breadth level.

*~27 s | LayerStack (C3, structural.tsx) — three context tiers*

---

### B07 — Divergence

> Here's where the comment section splits. Optimists: the toil-collapsing claim is already demonstrated — literature synthesis, data analysis, report generation — and the compounding starts immediately. Skeptics: the bottleneck for most science isn't reading time, it's running the experiment. Three days of wet lab doesn't compress with an LLM. If your constraint is bench time, reagents, or instrument access, ten years every year doesn't apply to you. Both sides are reading the same pitch. They're disagreeing about which step is actually the bottleneck.

*~30 s | DivergentFates (C2, deckPatterns) — PIPELINE slate until registered. REBUILD LAW: source 1 optimist + 1 skeptic comment verbatim from cd3PsBoGYkc.*

---

### B08 — Locked Door

> What Claude Science cannot do. Design the experiment when the physics is genuinely unknown — that's still the human's job. Verify the physical result — someone still runs the gel, reads the flow cytometer, interprets the micrograph. Detect when the hypothesis is unfalsifiable. The scientist in the video says it explicitly: the moment we stop bringing intelligence and creativity and discipline to science — that's a big problem. That's not a caveat. That's the architecture of the product.

*~28 s | LayerStack (C3, structural.tsx) — three locked layers, no accent on locks*

---

### B09 — Branch

> Two branches. If your rate-limiting step is cognitive — literature synthesis, data interpretation, hypothesis generation, writing — the case is strong. Claude Science is your accelerant now. If your rate-limiting step is physical — experiment runtime, instrument time, reagent cost, patient recruitment — Claude Science is a downstream tool that improves analysis of results you still have to generate. The ×10 claim is accurate at the analysis bottleneck. It doesn't compress the bench.

*~25 s | BinaryBranch (C2, deckPatterns) — PIPELINE slate until registered*

---

### B10 — Scorecard

> The scorecard. Pitch claim: ten years of progress every year. Column one — what it demonstrates: analysis time collapsing, literature synthesis at scale, hypothesis suggestion from pattern-matching, faster iteration on experiment design. Column two — what it asserts without demonstrating: the causal chain from faster analysis to faster drug approval, ×10 applying to experiment-bottlenecked science, the token architecture for deep single-target work. The pitch is strong on the real claim — and quiet on the hard constraints.

*~30 s | ClaudeWindow — two-column artifact table*

---

### B11 — Handoff ("Your turn.")

> Your turn. Pick a research project you're running or know well. Identify the rate-limiting step — not the experiment, the analysis. Load the relevant data, literature, or lab notes. Ask Claude for the three hypotheses you haven't considered. Then check: does the analysis actually compress? That's the experiment the pitch video didn't show.

*~23 s | ClaudeComposerAsk — greeting: "Your turn."*

---

### B12 — Title Outro

> Ten Years Every Year. Liam, in for Bear.

*~8 s | ClaudeTitleOutro — title: "Ten Years Every Year.", @NikBearBrown, subline: "The pitch, and the comment section."*

---

## Open items before audio

1. **Verbatim comments** (B07, REBUILD LAW): Source 1 optimist + 1 skeptic comment from YouTube video `cd3PsBoGYkc`. Handles in mono, text in serif. No screenshots — native cream-stage rebuild cards only.
2. **C2 pattern components** (B01, B02, B07, B09): `ScaleComparison`, `AttritionChain`, `DivergentFates`, `BinaryBranch` need to be imported from `skills/make/component-showcase/remotion/src/deckPatterns.tsx` into the main runtime and registered in `Root.tsx`. Until then, these beats render as PIPELINE slates.
3. **ClaudeWindow table** (B10): Confirm `ClaudeWindow` supports a two-column table artifact view — or adapt to `ClaudeVerdictArtifact` with column A / column B layout.

---

## Timing estimate

| Beat | Scene | Est. duration |
|---|---|---|
| YTV01 | ClaudeVerdictArtifact | 35 s |
| B00 | ClaudeComposerAsk (cold open) | 23 s |
| B01 | ScaleComparison (PIPELINE) | 22 s |
| B02 | AttritionChain (PIPELINE) | 27 s |
| B03 | SourceFlow | 27 s |
| B04 | LayerStack (×10 meter) | 28 s |
| B05 | ChipGrid | 25 s |
| B06 | LayerStack (token meter) | 27 s |
| B07 | DivergentFates (PIPELINE) | 30 s |
| B08 | LayerStack (locked door) | 28 s |
| B09 | BinaryBranch (PIPELINE) | 25 s |
| B10 | ClaudeWindow (scorecard) | 30 s |
| B11 | ClaudeComposerAsk (handoff) | 23 s |
| B12 | ClaudeTitleOutro | 8 s |
| B_LOGO | LogoOutro (NBB, via logo.py) | ~12 s |
| **Total** | | **~5:30** |

---

## GATE P sign-off

Read the narrations above. If the script is approved for audio generation, sign below and set `metadata.gate_p` to `"approved"` in `beat_sheet.json`.

**Signed:** ___________________________  **Date:** ___________

**Notes / changes requested:**

# PEDAGOGY audit — claude-liam-a2-05-agent-design ("Design Your 3 Madison Agents (15 of 30 pts)")

INFO 7375 Assignment 2 Episode 5 — architecture section of the Madison PRD, worth 15 points. claude-liam, Kokoro am_onyx.
Episode 5 of the "Plan It Like a PM — Your Madison PRD" series on @NikBearBrown; Liam in for Bear. Audited against ai-explainer house + frame laws.

## Act structure
- B00 (ClaudeComposerAsk open), B01 (A2MadisonLayers Remotion), B02 (ClaudeComposerAsk — agent design prompt), B03 (A2AgentCommDiagram Remotion), B04 (ClaudeComposerAsk — schema prompt), B05 (ClaudeWindow artifact — four traps), BVDT (ClaudeVerdictArtifact), BHTF (ClaudeComposerAsk handoff), BOUT (ClaudeTitleOutro). 9 beats. PASS

## Cold open (COLD OPEN LAW)
- B00 is ClaudeComposerAsk. Liam self-introduces as Episode 5. Output lines enumerate the three deliverables: 3 named agents with specific jobs, a communication diagram showing who sends what to whom, and grounding in real Madison layers and components. PASS

## Gap formula / hook
- Tension: the architecture section is where students either nail the Madison framework or invent features that do not exist in it. Resolution: the episode teaches what Madison layers and components actually exist before any agent is named, closing the credibility gap that invented features create. PASS

## Utility lint
- BHTF prompt produces a concrete artifact: three named agents each with a specific job, a Madison layer, a named component, a data output, and a simple communication flow — plus flags for any component not verifiable in the Madison README. Read aloud in narration and the prompt command is displayed on screen; Liam adds two concrete refinement steps: tighten each agent's job to a buildable sentence, then verify every component name in the README before committing to the board (HANDOFF LAW). PASS

## Vocabulary / register (Pragmatist)
- Steps-first throughout: the episode moves from layers → agents → diagram → schema → traps in a linear, building sequence. Every term defined on first use: "orchestration layer" introduced with its function ("coordination envelope above the five layers, not one of them"), "schema annotation" explained before the prompt that generates it, "Thompson sampling" named in context of Multi-Armed Bandit optimization in the Performance layer. PASS

## Honesty (DOUBLE-CHECK LAW)
- B01 explicitly names the real Madison components (MarketMind Research, Brand Voice Personalization, AI Concierge Systems, Multi-Armed Bandit / Thompson sampling, Bellman, Popper) and closes with "Before you name an agent, confirm the component you plan to cite actually exists in the Madison README — the link is in the assignment brief. Do not invent features." B05 (traps) repeats the verification imperative: "If you name a component that does not exist in the Madison README, the instructor will notice." BVDT closes with "AI drafted the suggestions; you own the truth." No Madison component is presented as invention or guess. PASS

## Length law
- 9 beats, est. ~215s (~3:35) at Kokoro pace (B00 20s + B01 35s + B02 35s + B03 35s + B04 30s + B05 25s + BVDT 25s + BHTF 40s + BOUT 5s). Appropriate for a mid-series instructional episode covering a 15-point rubric section with two custom Remotion diagrams and a traps beat. PASS

## Visual law spot-check
- ILLUSTRATE LAW: every conceptual beat has a matched visual — B01 uses A2MadisonLayers Remotion (the five-layer diagram with real component labels and footnote), B03 uses A2AgentCommDiagram Remotion (three boxes, labeled arrows, orchestration envelope, schema annotation on one arrow), B02/B04/BHTF use ClaudeComposerAsk, B05/BVDT use ClaudeWindow/ClaudeVerdictArtifact. ASK→RESULT: B02 displays the design prompt and outputs, B04 displays the schema prompt and outputs, BHTF displays the handoff prompt and outputs — all three show realistic Claude prompts before the result. SparkLine on body beats: B05 ("distinct jobs → labeled arrows → PRD-relevant → README-verified"), BVDT artifact lines serve the same condensing function. No fabricated screenshots. PASS

VERDICT: PASS

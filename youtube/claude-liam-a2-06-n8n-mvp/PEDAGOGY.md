# PEDAGOGY audit — claude-liam-a2-06-n8n-mvp ("Scope the MVP: ONE n8n Workflow (15 of 30 pts)")

INFO 7375 Assignment 2 Episode 6 — MVP scope section of the Madison PRD, worth 15 points. claude-liam, Kokoro am_onyx.
Episode 6 of the "Plan It Like a PM — Your Madison PRD" series on @NikBearBrown; Liam in for Bear. Audited against ai-explainer house + frame laws.

## Act structure
- B00 (ClaudeComposerAsk open), B01 (ClaudeWindow artifact — n8n vs Madison), B02 (ClaudeComposerAsk — scope-selection prompt), B03 (ClaudeComposerAsk — node-sequence prompt), B04 (ClaudeWindow artifact — out-of-scope list), B05 (ClaudeWindow artifact — excellence moves), B06 (ClaudeWindow artifact — four traps), BVDT (ClaudeVerdictArtifact), BHTF (ClaudeComposerAsk handoff), BOUT (ClaudeTitleOutro). 10 beats. PASS

## Cold open (COLD OPEN LAW)
- B00 is ClaudeComposerAsk. Liam self-introduces as Episode 6. Output lines enumerate the three deliverables: one n8n workflow (not all three agents), 3–5 verified node names in an input → process → output sequence, and an explicit out-of-scope list. PASS

## Gap formula / hook
- Tension: the most common failure mode is designing something unrealistically large and then being unable to demo it in Week 3 — scope is where the grade is lost, not on content. Resolution: the episode provides three concrete feasibility criteria for picking the one agent and a required template for declaring what is not being built, converting an infinite design space into a demoable one-week artifact. PASS

## Utility lint
- BHTF prompt produces a concrete artifact: a trigger node, 3–5 real n8n nodes each with type, job, input, and output, a two-sentence input → process → output description, and an out-of-scope list with the two unbuilt agents, any unavailable data source, and any deferred user-story feature. Read aloud in narration: Liam instructs students to verify every node name at docs.n8n.io before committing to the board and to write the out-of-scope list before finalizing the diagram (HANDOFF LAW). PASS

## Vocabulary / register (Pragmatist)
- Steps-first throughout: the episode moves from terminology clarification → agent selection criteria → node sequence design → out-of-scope list → excellence moves → traps in strict build order. Every term defined on first use: "n8n" introduced as "a separate visual workflow-automation platform — not part of Madison" (B01), "node" defined as "one step — trigger, action, or transformation" (B01), "MVP ceiling" explained as 3–5 nodes in B03 and repeated in B06. PASS

## Honesty (DOUBLE-CHECK LAW)
- B01 draws an explicit conceptual boundary: "Madison and n8n are two different things" — stated in narration and rendered as a ClaudeWindow artifact so the distinction is visible on screen. B03 warns directly: "The AI sometimes invents node names that sound plausible but do not exist in n8n. If you put a node name on your diagram that does not exist, the instructor will check and you will lose credibility on the whole section. Verify first, then commit." B06 (traps) names the specific pattern: "'AI Marketing Optimizer node' does not exist in n8n — the instructor will check docs.n8n.io." B05 (excellence) tells students to open docs.n8n.io and find the specific node before using its name. No node names are presented as authoritative without the verification instruction. PASS

## Length law
- 10 beats, est. ~280s (~4:40) at Kokoro pace (B00 20s + B01 30s + B02 30s + B03 40s + B04 30s + B05 30s + B06 25s + BVDT 25s + BHTF 40s + BOUT 5s). Appropriate for the most mechanically dense section of the assignment: one agent selection decision, a node sequence design, and an out-of-scope list, each with its own traps beat and excellence moves. PASS

## Visual law spot-check
- ILLUSTRATE LAW: every conceptual beat has a matched visual — B01 renders the n8n vs Madison distinction as a ClaudeWindow artifact with sparkLine, B04 displays the out-of-scope template as a ClaudeWindow artifact, B05 and B06 each use ClaudeWindow artifacts with sparkLines that distill the rule to one line. ASK→RESULT: B02 displays the scope-selection prompt and three output lines, B03 displays the node-sequence prompt and four output lines, BHTF displays the full handoff prompt and four output lines — all show realistic Claude prompts before results. SparkLine on body beats: B01 ("Madison designs it — n8n builds it — one agent — one workflow"), B04 ("name what you will not build → show you understand the constraint"), B05 ("verified node names → data schema → named trigger → demo-ready"), B06 ("3–5 nodes → one agent → out-of-scope listed → all node names verified"). No fabricated screenshots. PASS

VERDICT: PASS

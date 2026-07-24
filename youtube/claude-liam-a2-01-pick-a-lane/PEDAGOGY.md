# PEDAGOGY audit — claude-liam-a2-01-pick-a-lane ("Pick a Lane: Find the ONE Real Job (10 pts)")

Episode 1 of the "Plan It Like a PM — Your Madison PRD" series for INFO 7375 Assignment 2. Covers the Dream-Job card (10 pts): one real job posting, verbatim technical requirements, and a one-sentence "why this role" anchor. claude-liam, Kokoro am_onyx.
Series of 4 episodes building a Madison PRD from job search through user stories and success metrics. Audited against ai-explainer house + frame laws.

## Act structure
- B00 cold open → B01 what goes in the Dream-Job card → B02 how to find the right posting → B03 extracting the top 3 requirements → B04 the excellence move (hiring manager context) → B05 traps → BVDT verdict → BHTF your turn handoff → BOUT outro. 9 beats. PASS

## Cold open (COLD OPEN LAW)
- B00 is ClaudeComposerAsk. Liam self-introduces ("Hola — this is Liam. Episode 1."). Output lines enumerate the three deliverables: job posting with link, top 3 technical requirements in the company's words, and one-sentence why-this-role. PASS

## Gap formula / hook
- Opening tension: "You cannot plan a project that gets you hired if you haven't named the job" — a concrete failure mode, not a general statement. Resolves immediately: by the end of the episode the viewer has the three items on the Dream-Job card. The excellence move (B04) and traps (B05) give a clear gradient between an eight and a ten. PASS

## Utility lint
- BHTF prompt produces a concrete extraction artifact — exact job title, company, top 3 verbatim requirements, team/reporting structure, suggested why-sentence — directly usable as the Dream-Job card. Read aloud by Liam with full instructions including the hallucination-check step ("do not trust the requirements list without checking it against the actual posting text"). HANDOFF LAW: the prompt is read, the check step is discussed. PASS

## Vocabulary / register (Pragmatist)
- Steps-first throughout: each beat opens with what to do before explaining why. Terms defined on first use: "Dream-Job card" introduced with its four required elements in B01; "hiring manager context" introduced with the LinkedIn search method in B04. Register matches how-to series doctrine — no throat-clearing, no rhetorical questions, concrete nouns throughout. PASS

## Honesty (DOUBLE-CHECK LAW)
- Hallucination risk flagged explicitly in both B02 ("AI summaries of job requirements are sometimes wrong — not because Claude is guessing, but because training data for recent postings can lag") and BHTF ("do not trust the requirements list without checking it against the actual posting text — read the posting and confirm that those exact phrases appear"). BVDT also flags the date conflict in the assignment brief (May 22 vs. Jan 23) and directs the student to confirm the real deadline with their instructor. PASS

## Length law
- 9 beats, est. ~279s (~4:39) at Kokoro pace (B00: 21s, B01: 45s, B02: 40s, B03: 37s, B04: 42s, B05: 46s, BVDT: 42s, BHTF: 44s, BOUT: 5s, total narration 322s — task described as ~5.4 min). Appropriate for a one-deliverable how-to episode with a specificity-intensive task. PASS

## Visual law spot-check
- ILLUSTRATE LAW: B00 ClaudeComposerAsk for the cold open prompt beat; B01 ClaudeWindow artifact for the four required card elements; B02 ClaudeComposerAsk for the search strategy prompt; B03 ClaudeComposerAsk for the extraction prompt; B04 ClaudeWindow artifact for the excellence move steps; B05 ClaudeWindow artifact for the four traps; BVDT ClaudeVerdictArtifact for the rules summary; BHTF ClaudeComposerAsk for the handoff prompt; BOUT ClaudeTitleOutro. ASK→RESULT: B02 and B03 show the prompt (ask) and enumerate the expected output (result) inline within the ClaudeComposerAsk pattern; B04 and B05 show informational reference cards in ClaudeWindow. SparkLine present on B01 ("All four. Not three."), B02 (output list), B04 ("Calibrate to their vocabulary, not a template."), B05 ("One real posting. All four elements."). No fabricated screenshots. PASS

VERDICT: PASS

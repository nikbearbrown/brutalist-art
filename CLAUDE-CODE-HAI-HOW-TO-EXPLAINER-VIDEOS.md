# Claude Code Prompt — "How to Make Explainer Videos for Your Research" (Humanitarians AI, 16:9, claude-liam)

A single onboarding explainer for Humanitarians AI Fellows: how to turn a
week of their research work into a Brutalist claude-explainer video, then
publish it to the channel. Liam voice, Humanitarians AI branding.

Run Claude Code from:

`/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art`

Paste the complete prompt below. Nothing to replace. This is a toolkit how-to
(the Brutalist meta-series exception to the ownership rule), so it builds into
`brutalist-art/youtube/`. Free pipeline only — Kokoro voice, no ElevenLabs, no
higgsfield, no publishing, no git commit or push.

```text
Build one 16:9 claude-explainer video: "How to Make Explainer Videos for Your
Research" — an onboarding video for Humanitarians AI Fellows that teaches them
the exact Brutalist workflow for turning a week of their own research into a
published explainer. claude-liam VOICE, but Humanitarians AI BRANDING (folder
chip @HumanitariansAI). Free pipeline only: Kokoro voice, no ElevenLabs, no
higgsfield, no publishing, no git commit or push. Run without approval pauses
(no paid spend is possible under these constraints).

READ COMPLETELY BEFORE ACTING

- AGENTS.md
- CLAUDE-BRAND.md
- skills/make/ai-explainer/SKILL.md  (note the claude-hai audience =
  STUDENTS/learners; this video's audience is Fellows learning the pipeline)
- skills/make/explainer/SKILL.md (and the MOTION.md / REMOTION.md it points to)
- skills/make/your-turn/SKILL.md (closing block contract)
- skills/make/cli-explainer/SKILL.md (for the command/terminal beats)
- docs/remotion-best-practices/SKILL.md
- runtime/remotion/src/tokens/claude.ts

FORMAT

- 1920x1080 (16:9), 30 fps.
- Voice/persona: Liam (Kokoro am_onyx), register Teardown-but-warm — this is a
  welcome to Fellows, not a takedown. Folder chip: @HumanitariansAI. Do not
  use ElevenLabs.
- Audio-first: narration generated and measured per beat FIRST; every beat
  conforms to its audio. Length derives from the beats — expect 3–5 minutes.
- Title: "How to Make Explainer Videos for Your Research".
- SIGN-IN LINE: on the cold open and again on the outro, Liam says
  "Liam, for Humanitarians AI." (This video is the template; it also TEACHES
  Fellows that when THEY build with the Liam voice, Liam should say
  "Liam, for [their name] and Humanitarians AI" — show that line as an
  on-screen example in the relevant step.)

THE STORY (warm, practical, Fellow-to-Fellow)

Hook: You did the research this week. Here's how to turn it into a two-minute
explainer the world can actually watch — using Claude and the Brutalist
system — in one sitting.
Then walk the SIX steps as the spine of the video, each its own segment:

STEP 1 — Put your week in a folder.
  Everything you did this week — notes, code, figures, data, the paper draft,
  screenshots — goes into one folder. That folder is the raw material; Claude
  reads it to find the stories worth animating.

STEP 2 — Get the Brutalist system.
  The video toolkit (skills, Manim + Remotion, the Claude look) is what turns
  your work into a finished reel. Download it and get set-up help by emailing
  hr@humanitarians.ai. Put the Brutalist skills alongside your week's folder.

STEP 3 — Open Claude Code in that folder.
  Run this exact command in the folder that has your work AND the Brutalist
  skills:  caffeinate claude --dangerously-skip-permissions
  ("caffeinate" keeps your Mac awake for the long render; the flag lets Claude
  run the pipeline end to end without stopping to ask for each permission.)

STEP 4 — Give Claude the prompt — with YOUR specifics.
  Start from the generic prompt and STEER IT with what you actually did this
  week. The generic seed:
    "claude code prompt to create claude explainer liam voice for every one
     of these video ideas — it should create animation visualizations and
     infographics"
  Then make it yours: name your project, your result, the figure or number
  worth showing, the one idea you want a viewer to leave with. The more
  specific you are about YOUR week, the better the video. And if you use the
  Liam voice, tell Claude to have Liam say "Liam, for [your name] and
  Humanitarians AI" — show that instruction on screen.

STEP 5 — Watch, then ask for changes.
  Claude builds the video(s). Watch them. Anything off — a wrong number, a
  pace that drags, a chart that should be a different chart — just tell Claude
  in plain language and it revises. Iterate until it's right.

STEP 6 — Publish to the channel.
  When it's ready, use Gaurav's publishing script (get it from
  hr@humanitarians.ai) to post it to youtube.com/@humanitariansai, in the
  "Fellows Research" playlist. That's where your research explainer lives.

Landing: your research deserves an audience. The work is already done — this
just gives it a face. Welcome aboard.

STRUCTURE (claude-explainer skeleton + your-turn closing)

- Beat 0 — ClaudeComposerAsk cold open. Liam: "You did the research. Let's
  turn it into a video the world can watch — in one sitting. Liam, for
  Humanitarians AI."
- Middle — the six steps as the segments, carried by the figures below.
- Closing per your-turn: VERDICT recap card (the 6 steps as a numbered
  checklist) → Your Turn composer beat → title re-read + "Liam, for
  Humanitarians AI" on the @HumanitariansAI brand card.
- Your Turn suggested prompt (Liam reads it in full): "Here's my folder of
  this week's research — [one line on what you did]. Create a claude-explainer
  in the Liam voice for every video idea in it, with animated visualizations
  and infographics, and have Liam say 'Liam, for [my name] and Humanitarians
  AI.'"

FIGURES (build these natively; this is a workflow how-to so the terminal and
the pipeline ARE the subject — the ILLUSTRATE LAW allows UI where the UI is
the subject; still, prefer clean house-style mocks over real screenshots)

FIGURE 1 — THE ONE-SITTING PIPELINE (opening map)
  A left-to-right flow the whole video hangs on: YOUR WEEK'S FOLDER →
  BRUTALIST SKILLS → CLAUDE CODE → WATCH & REVISE → PUBLISH (Fellows
  Research). Each node lights terracotta as its step comes up; the map
  reappears as a progress rail between segments.

FIGURE 2 — THE FOLDER (Step 1)
  A folder icon filling with labeled cards — notes, code.py, figure.png,
  data.csv, draft.md, screenshots — dropping in one by one. Caption: "one
  folder = the raw material."

FIGURE 3 — THE COMMAND (Steps 2–3)
  An Onda terminal beat. First the email chip: hr@humanitarians.ai (get the
  Brutalist system + setup help). Then the command typed live, monospace,
  with per-token callouts:
    caffeinate claude --dangerously-skip-permissions
  Annotation rings: "caffeinate = keep the Mac awake for the render",
  "--dangerously-skip-permissions = run the whole pipeline without pausing".

FIGURE 4 — GENERIC → SPECIFIC (Step 4; the key teaching beat)
  Split panel. Left, the generic prompt (greyed). Right, the SAME prompt with
  terracotta insertions where the Fellow adds their specifics — project name,
  the result, the figure to show, the one takeaway, and the
  "Liam, for [your name] and Humanitarians AI" line. Narration: the specifics
  are what make it yours. Show the sign-in line as its own callout card.

FIGURE 5 — WATCH & REVISE (Step 5)
  A little player card with a revise loop beneath it: a plain-language note
  ("this number's wrong" / "slow this part down") arcs back into the pipeline
  and the card updates. Caption: "plain language in, better video out."

FIGURE 6 — PUBLISH (Step 6)
  The publish step: Gaurav's script (chip: hr@humanitarians.ai) → the
  @HumanitariansAI channel → the "Fellows Research" playlist, the new video
  sliding into the playlist row. Terracotta on "Fellows Research".

FIGURE RULES

- Claude fidelity palette: cream #FAF9F5 page, warm ink #3D3929, terracotta
  #D97757 as the ONE accent per beat. EB Garamond segment titles, Title Case.
  Onda code-block for the terminal/command. Accent reserved for each beat's
  single focal element.
- The email hr@humanitarians.ai, the exact command
  (caffeinate claude --dangerously-skip-permissions), the channel
  youtube.com/@humanitariansai, and the playlist name "Fellows Research" must
  appear on screen EXACTLY as written.
- Transform-don't-cut within figure beats.

OUTPUTS

- youtube/claude-liam-hai-how-to-explainer-videos/
  - beat_sheet.json  (persona Liam, folderLabel @HumanitariansAI)
  - claude-liam-hai-how-to-explainer-videos.mp4 (1920x1080)
  - SOURCES.md — the six steps, the exact command, the email, the channel,
    and the playlist, each written out verbatim for QC.
- Verify the mp4 exists and plays (probe duration and frame count) before
  reporting done, and end with the beat → timestamp table.
- If a figure animation fails to render after two attempts, replace that beat
  with a slate card naming it and log the failure — never silently drop it.
```

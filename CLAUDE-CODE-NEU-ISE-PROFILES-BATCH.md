# Claude Code Prompt — NortheasternISE People Profiles → claude-explainer (batch, profile mode, claude-liam)

Turns the NortheasternISE Substack export into a fleet of claude-explainer
PROFILE-mode reels — one per story ABOUT A PERSON — Liam voice, @HumanitariansAI
branding, published-ready (not published). Every reel uses the `profile`
modifier: greeting `Profile, <Name>`, the subject named throughout, a PERSON
CREDIT card with verbatim links.

Source zip (already on disk):
`/Users/bear/Documents/CoWork/bear-textbooks/books/TMP/5UJLKT7uS5qEBkJNU3hMSg.zip`

Run Claude Code from:

`/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art`

TWO PHASES. Paste PHASE 1 now, review the manifest it writes, then tell Claude
Code to run PHASE 2 on the approved rows. Free pipeline only — Kokoro voice, no
ElevenLabs, no higgsfield, no publishing, no git commit or push, throughout.

Shared rules (whole job):
- `profile` MODIFIER on claude-explainer — read the "The `profile` modifier"
  section of `skills/make/ai-explainer/SKILL.md` first; it governs the
  greeting (`Profile, <Subject Name>`), the name-throughout rule, the required
  PERSON CREDIT card, and the honesty (DOUBLE-CHECK-for-people) law.
- Channel: claude-liam voice (Kokoro am_onyx, IN-FOR-BEAR — Liam signs "Liam,
  in for Bear"), folder chip @HumanitariansAI, HAI logo bug. Register
  Teardown-warm. Format 1920x1080 (16:9), 30fps.
- Build into `../humanitarians_html/youtube/claude-liam-profile-<name-slug>/`
  (match the two existing profiles' location and naming — kaustubha-eluri,
  aditi-deodhar).
- Publish target (for later, human-run): @humanitariansai YouTube "Profiles"
  playlist. This batch does NOT publish.

============================================================================
PHASE 1 — CLASSIFY & MANIFEST  (run now; build nothing)
============================================================================

```text
PHASE 1 of the NortheasternISE profiles batch. Do NOT build any video, generate
audio, or render anything. Produce a review manifest only. No git commit/push.

1. Unzip ../TMP/5UJLKT7uS5qEBkJNU3hMSg.zip into a scratch dir you control (e.g.
   ../humanitarians_html/youtube/_neu-ise-source/). Treat it as READ-ONLY input.

2. Enumerate posts/*.html. For each, read the title + subtitle + body and
   classify into exactly one bucket:
   - PROFILE — a feature story whose SUBJECT is a specific named individual
     (a student, fellow, researcher, founder, or professor) and their work,
     journey, or philosophy. These are the builds. Signal: the subtitle names a
     person ("<Name> and the Discipline of…", "How <Name> Learned to…",
     "<Name> at Northeastern"), or the body is a portrait of one person.
   - SKIP — everything else, with a one-line reason: technical/analysis essays,
     how-to / career-advice articles, book reviews, job postings, the weekly
     job "harvest"/dataset digests, the Substack-editor how-to, interview case
     studies, and any *.opens.csv / *.delivers.csv / email_list.csv / posts.csv
     (analytics, not articles) and near-empty stubs (e.g. 188842210.389.html).
   Never silently drop — every post lands in PROFILE or SKIP with a reason.

3. HIGH-CONFIDENCE PROFILE SEEDS (verify each by reading; add any you find that
   I missed; correct me if a seed is actually not a personal profile):
   - 189421959 The Architect Who Didn't Wait to Be Asked — Anshika Khandelwal
   - 189519823 The Precision of Honest Work — Aravind Balaji
   - 188185792 The Honest Gambit — Aravind Balaji's first paper
   - 188183890 QEMA-G and the Education of Ambition — Aravind Balaji (companion
     to 188185792/189519823 — if all three are the same subject, CONSOLIDATE
     into ONE Aravind Balaji profile drawing on all three, and log the merge)
   - 189674952 The Lab That Builds by Doing — Nik Bear Brown
   - 189796667 The Builder Who Said No — Advaith Krishna Vasisht
   - 189797002 The Engineer Who Fixes What Nobody Asked… — Sayam Khatri
   - 190129779 The Weight of What You Build — the grad student building AI for
     emergency responders (get the name from the body)
   - 190788782 The Builder's Grammar — Ayushi Walia
   - 191511989 The Engineer Nobody Photographed — (confirm the named subject in
     the body; if it's an anonymized composite, SKIP with that reason)
   - 192231340 The Difference Between Performing Your Career… — Yadeesh K R
     ("A profile of Yadeesh K R")
   - 193221055 My Tech Journey — first-person self-profile (get the author's
     name; build only if a real named person's story, else SKIP)
   - 199127494 The Startup Founder Who Isn't Allowed to Be in Charge — (name the
     founder from the body; if it's an ecosystem essay with no single subject,
     SKIP with that reason)
   ALREADY BUILT — SKIP (do not rebuild): 189414412 The Cost of the Pivot
   (Aditi Deodhar) and 192785994 Why Most AI Projects Fail… (Kaustubha Eluri).

4. For each PROFILE, extract and record in the manifest:
   - post id + source html path
   - SUBJECT name (the person the video is about) + a name-slug
     (firstname-lastname) → folder claude-liam-profile-<name-slug>
   - the article AUTHOR/byline (credit on the SOURCES card)
   - the ONE-SENTENCE THESIS the reel will land (the article's core claim)
   - 2–4 evidence beats (the subject's projects/work) a builder could start from
   - the subject's public links IF the article states them (LinkedIn/GitHub);
     mark "none in source" when absent — never invent a link
   - a proposed episode title (reuse the article's title where it works)

5. Write the manifest to
   ../humanitarians_html/youtube/PROFILES-BATCH-MANIFEST.md — a table of PROFILE
   rows (build list) followed by the SKIP list with reasons. Also print a
   one-line summary: N profiles to build, M skipped. STOP. Build nothing.
```

============================================================================
PHASE 2 — BUILD  (run after the manifest is reviewed)
============================================================================

```text
PHASE 2 of the NortheasternISE profiles batch. Build a claude-explainer in
PROFILE MODE for every PROFILE row in
../humanitarians_html/youtube/PROFILES-BATCH-MANIFEST.md, and keep going until
all are built. Resumable LOOP. Free pipeline only: Kokoro voice, no ElevenLabs,
no higgsfield, no publishing, no git commit or push. Run without approval pauses
— the human reviews finished mp4s at the end.

READ FIRST: AGENTS.md · CLAUDE-BRAND.md · skills/make/ai-explainer/SKILL.md
(esp. "The `profile` modifier" section) · skills/make/explainer/SKILL.md (+
MOTION.md / REMOTION.md) · skills/make/your-turn/SKILL.md ·
docs/remotion-best-practices/SKILL.md · runtime/remotion/src/tokens/claude.ts.
For visual reference, the two shipped profiles:
../humanitarians_html/youtube/claude-liam-profile-{kaustubha-eluri,aditi-deodhar}/.

PER PROFILE (the profile-mode contract):
- Voice claude-liam (Kokoro am_onyx); folder chip @HumanitariansAI; HAI logo
  bug; register Teardown-warm. 1920x1080, 30fps. Audio-first.
- GREETING (the modifier's signature): B00 ClaudeComposerAsk greeting reads
  `Profile, <Subject Name>` (not "Hello, Liam"); Liam still says "Liam, in for
  Bear" aloud in B00 and the outro. The subject's NAME appears on segment cards
  and spark lines throughout, and on the outro title card.
- Build the reel to land the manifest's ONE thesis for that person. Cold open =
  the article's hook as a mystery. Body = the subject's arc + evidence beats,
  each rebuilt as a native concept illustration / infographic (REBUILD LAW —
  never a headshot or a lifted article image; create animation visualizations
  and infographics wherever the story has a mechanism, a before/after, or a
  set of projects).
- Closing per your-turn: VERDICT recap card → PERSON CREDIT card (subject name,
  program/role, public links VERBATIM from the manifest — none invented; the
  article's call-to-action if any) → Your Turn composer beat (a prompt in the
  subject's spirit) read in full by Liam → title re-read on the @HumanitariansAI
  card.
- HONESTY (DOUBLE-CHECK LAW for people): only claims the article makes — no
  invented metric, quote, credential, or link; keep soft attributions soft. Log
  the article title/author/date + every on-screen name and link in SOURCES.md.

OUTPUT per profile → ../humanitarians_html/youtube/claude-liam-profile-<name-slug>/:
- beat_sheet.json (persona Liam, folderLabel @HumanitariansAI, greeting
  `Profile, <Name>`)
- mp4/claude-liam-profile-<name-slug>.mp4 (1920x1080)  [and the -slate previz]
- <name-slug>.srt caption track
- description.txt (for the later publish step)
- SOURCES.md

THE LOOP:
1. Ledger at ../humanitarians_html/youtube/PROFILES-BATCH-BUILD-LOG.md: subject |
   slug | status (pending/built/failed/merged) | mp4 path | notes.
2. For each PROFILE, SKIP if its mp4 already exists and probes valid
   (idempotent/resumable). Else build end to end.
3. Verify each mp4 plays (probe duration + frame count), run the VISUAL QC LAW
   frame pass, mark built, update the ledger, MOVE ON.
4. A beat that won't render after two tries → slate card + log; never drop a
   beat silently.
5. A whole profile that fails after a genuine attempt → mark failed with reason,
   CONTINUE — one failure never halts the batch.
6. Stop when every PROFILE row is built/failed/merged. Print the final ledger
   and, per built reel, its beat → timestamp table.

Begin with the first PROFILE row and work down. Do not ask for confirmation
between reels. When done, remind the human: publish to @humanitariansai
"Profiles" playlist with the youtube-publisher script (dry-run + lock channel ID
first).
```

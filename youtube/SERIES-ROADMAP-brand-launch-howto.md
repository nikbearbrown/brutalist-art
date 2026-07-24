# SERIES ROADMAP — "Ship It: Build Your Brand's Live Presence"

A how-to ai-explainer series for **INFO 7375 Assignment 8** (Building Your Live
Website, Resumes & LinkedIn Header — due July 24, 2026). Audience: **students who
have never done any of this before.** Register: **pragmatic, step-by-step** (Liam
voice, `claude-liam`, Kokoro am_onyx). The whole series exists to walk a beginner
from "brand strategy locked" to "six deliverables submitted," one screen-share-style
episode per graded piece.

> Voice/channel note: built on `claude-liam` per request (Liam, @NikBearBrown).
> Because the audience is students, the natural alternative is `claude-hai`
> (@HumanitariansAI — the students channel, Pragmatist register). One-variable
> swap in each beat sheet if you'd rather brand it that way.

## Series doctrine (applies to every episode)

- **Ship-it mindset, stated out loud.** First version, not final. "Functional over
  flawless." Every episode ends by producing the actual deliverable, not a theory of it.
- **Assume zero prior knowledge.** Name every button. Define every acronym the first
  time (ATS, WCAG, hero section, responsive). Never say "just" — if a step is easy,
  show it; if it's fiddly, warn them.
- **The AI does the heavy lift, the student makes the judgment.** Every episode shows
  the exact prompt to paste into the tool, then what to CHECK in the result. The lesson
  is *how to steer the tool*, not "the tool does it for you."
- **One deliverable per episode = one Your Turn.** The HANDOFF beat is literally the
  assignment task, with the paste-ready prompt that starts it.
- **Brand continuity is the through-line.** Every episode reminds them: pull the logo,
  palette, type, and voice from Assignments 6 & 7. "No blank placeholder boxes."
- **ai-explainer bookends stay:** composer cold open → step-by-step body → verdict recap
  → Your Turn (the deliverable) → title-restate outro. 16:9. Free pipeline (Kokoro).
- **Honesty:** platform UIs and dimensions change — each SOURCES.md notes "re-verify the
  tool's current UI before recording." No fabricated screenshots (REBUILD LAW): tool
  steps are rebuilt as clean illustrated flows, not lifted screen-grabs.

---

## The episodes (build in this order)

### E0 — "Before You Build: The Map" (~3 min) — optional cold-open episode
- **slug:** `claude-liam-a8-00-the-map`
- **premise:** Six deliverables sound like six weekends. It's really one brand, applied
  six times. Show the whole board so nobody freezes at the start.
- **teach:** the six pieces (website, accessibility check, LinkedIn header, 3 visuals,
  ATS resume, visual resume) as one asset system fed by A6/A7; what "first version" means
  for the grade; the ship-it rule.
- **deliverable produced:** none — this is the orientation episode. Your Turn = "open your
  A7 brand sheet and paste your palette hexes, fonts, and logo file into one scratch doc
  you'll reuse in every step."
- **note:** cuttable if you want to start straight at the website.

### E1 — "Build Your Website with AI, Part 1: Pick a Platform & Get a First Draft" (~6 min)
- **slug:** `claude-liam-a8-01-website-draft`
- **premise:** The scariest deliverable is the fastest with v0/Framer/Wix — if you
  prompt it with your brand instead of a blank "make me a site."
- **teach (the steps):**
  1. Choose one platform (v0.dev / Framer AI / Wix AI / Squarespace AI) — a 20-second
     decision matrix (v0 = most control/code; Framer = designer-friendly; Wix/Squarespace
     = most guardrails). Pick one, don't shop.
  2. Write the FIRST prompt with brand baked in: name, role/value-prop, palette hexes,
     font names, the 4 required sections. Show the exact prompt.
  3. Generate → read the result against the brand, not just "does it look nice."
  4. One revision pass (change a color the tool got wrong; fix a section it merged).
- **required-sections callout:** Hero (name + role/value-prop + CTA), Projects (≥3, title
  + image + description), About, Contact (real info + a clear action).
- **beginner traps:** blank placeholder boxes; letting the tool pick random colors; forgetting
  the CTA; 3 projects with no images.
- **deliverable produced:** the live site draft (Part 1, 35 pts). Your Turn = the paste-ready
  "build my brand site" prompt with their tokens filled in.

### E2 — "Build Your Website, Part 2: Make It Not Break on Mobile" (~4 min)
- **slug:** `claude-liam-a8-02-website-responsive`
- **premise:** "Test it on your phone. If it's broken on mobile, it's not done." Half the
  grade-killers here are mobile layout, not desktop.
- **teach:** what "responsive" means (define it); the platform's mobile-preview toggle;
  the three things that break first (hero text overflow, images not scaling, nav collapsing);
  how to ask the AI to fix each; then publish and get the LIVE LINK (the actual deliverable).
- **deliverable produced:** the published live link. Your Turn = "open your site on your
  actual phone, screenshot the hero, and fix the first thing that's wrong."
- **note:** E1+E2 can merge into one longer episode if you prefer a single website video.

### E3 — "The Color Accessibility Check (WebAIM), Step by Step" (~4 min)
- **slug:** `claude-liam-a8-03-accessibility-check`
- **premise:** 5 points, one tool, ten minutes — and the one piece of required
  documentation. Also the thing that makes your site readable to everyone.
- **teach:** what WCAG contrast is and why it matters (define AA/AAA, the 4.5:1 floor for
  normal text, 3:1 for large); open webaim.org/resources/contrastchecker; enter your text
  hex + background hex; read the pass/fail; **what to do when it FAILS** (darken the text,
  don't just hope); repeat for every text-on-color combo in the brand; screenshot each;
  assemble the screenshots into one PDF.
- **tie-in:** this is the real-world version of the contrast beat in "Claude, Restrained" —
  reuse that WCAG-meter visual language.
- **deliverable produced:** the accessibility-check PDF (Part 1, 5 pts). Your Turn = "run
  every text/background pair in your palette; if any fails, here's the prompt to get 3
  compliant alternatives that stay on-brand."

### E4 — "Design a LinkedIn Header That Actually Works (1584 × 396)" (~5 min)
- **slug:** `claude-liam-a8-04-linkedin-header`
- **premise:** The header is a billboard with your face punched out of the corner. Most
  people cram text into the exact spot the profile photo covers.
- **teach:** the exact dimensions (1584 × 396 px) and WHY (the safe zone — profile pic
  bottom-left, cropping on mobile); set the canvas in Canva AI / Firefly / DALL·E; apply
  brand colors + type + one visual element; add the value prop / tagline (short — "headers
  with too much text get ignored"); position text clear of the photo and the mobile crop;
  export PNG/JPG; drop into a PDF.
- **beginner traps:** wrong dimensions → stretched/blurry; text behind the profile photo;
  paragraph of text nobody reads; off-brand stock gradient.
- **deliverable produced:** the header PNG/JPG in a PDF (Part 2, 15 pts). Your Turn = the
  paste-ready header-generation prompt with their brand tokens + tagline.

### E5 — "3 On-Brand AI Images That Look Like a Set" (~5 min)
- **slug:** `claude-liam-a8-05-brand-visuals`
- **premise:** Anyone can generate one good image. The grade is in three that look like
  siblings — same family, not three random stock photos.
- **teach:** what "visual consistency" means and how to engineer it — a reusable prompt
  SKELETON (same style tag, same palette words, same lighting/medium) with only the SUBJECT
  changing across the three; pick a tool (Midjourney / DALL·E / Firefly / Canva / SD);
  generate 3 representing expertise/industry/values/offering; the consistency check ("put
  them side by side — do they belong together?"); assemble into a PDF.
- **beginner traps:** three different art styles; ignoring brand palette; images that don't
  say anything about the person/startup.
- **deliverable produced:** 3 images in a PDF (Part 2, 15 pts). Your Turn = the reusable
  prompt skeleton with instructions to swap only the subject line three times.

### E6 — "The ATS-Friendly Resume (why the robot rejects you)" (~6 min)
- **slug:** `claude-liam-a8-06-ats-resume`
- **premise:** Before a human ever reads your resume, a parser does — and it throws away
  anything it can't read. ATS-friendly isn't boring; it's smart.
- **teach:** what an ATS is (Applicant Tracking System — define it) and what breaks it
  (columns, tables, text-in-images, fancy headers); the single-column rule; strategic
  keywords (pull them from the target job description — show how); where subtle brand lives
  without breaking parsing (accent color on headings, brand font for the name, tiny logo);
  export BOTH PDF and Word/text and WHY both.
- **beginner traps:** two-column template; skills in a graphic; keyword stuffing; only a PDF.
- **deliverable produced:** ATS resume, PDF + Word (Part 3, 15 pts). Your Turn = a prompt
  that takes their experience + a target job post and drafts a single-column, keyword-aligned
  resume they then fact-check.

### E7 — "The Visually Designed Resume (the 6-second scan)" (~5 min)
- **slug:** `claude-liam-a8-07-visual-resume`
- **premise:** The other resume is for the robot. This one is for the human who spends six
  seconds on it. Different job, different rules.
- **teach:** research first (Pinterest for layout inspiration — how to search it well);
  visual hierarchy so the eye lands on name → role → proof in order; where the headshot /
  brand image goes; full brand system applied (color, type, layout); the 6-second test
  (glance away, look back — what did you remember?).
- **beginner traps:** decoration over hierarchy; unreadable font pairings; burying the
  value prop; nothing scannable.
- **deliverable produced:** visual resume PDF (Part 3, 15 pts). Your Turn = "screenshot your
  draft, look at it for six seconds, and list the three things you remember — if your name
  and role aren't two of them, here's the prompt to fix the hierarchy."

### E8 (BONUS) — "One More Touchpoint (+5): Newsletter, Social Set, or Pitch Template" (~4 min)
- **slug:** `claude-liam-a8-08-bonus-touchpoint`
- **premise:** Five free points for proving your system stretches to a fourth surface.
- **teach:** pick ONE (email/blog template, 3+ social posts, or a deck template); apply the
  exact same tokens; the consistency test against the website + resumes.
- **deliverable produced:** the bonus artifact. Your Turn = the template-generation prompt
  for whichever surface they chose.

---

## Suggested cut for a shorter series

If eight is too many, the tight six-episode cut (one per graded deliverable) merges
E0 into E1 and E1+E2 into one website episode:
1. Website (E1+E2) · 2. Accessibility check (E3) · 3. LinkedIn header (E4) ·
4. Brand visuals (E5) · 5. ATS resume (E6) · 6. Visual resume (E7). Bonus E8 optional.

## Build order & mechanics

- Each episode is a standalone ai-explainer reel built into `<course-book>/youtube/`
  (or `brutalist-art/youtube/` if you want it as a channel series — tell me the owning
  book slug and I'll point the builds there).
- Same pipeline as the connector series: author beat_sheet.json → PEDAGOGY (GATE P) →
  Kokoro am_onyx audio (free) → visuals → QC → BUILD-PROMPT.md.
- Register override in metadata: `"register": "Pragmatist"` (how-to), not Teardown.
- I can build them one at a time for your review, or hand you a single resumable batch
  prompt that builds all eight on your Mac (like the anthropics/meta-series batches).

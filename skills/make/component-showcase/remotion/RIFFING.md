# RIFFING.md — the riff referent (how narration couples to the scene)

*v3.* Operational doctrine for riff. Riffing is narration whose content, timing, and
emphasis are **contingent on the scene as it plays** — not a script read near the right
timestamps. This file is the *referent* (fixed structure); the generator improvises only
the surface against it. Synthesized from jazz-improvisation cognition, deixis / joint-
attention research, sports-broadcast craft, expert-anticipation studies, and multimedia
cognitive-load theory (sources at the end).

---

## Purpose — surveying the tool belt (the AI+Human argument)

Riff exists so a **human can see the tool belt**. AI makes *writing* Remotion (or Manim)
trivial — so the scarce thing is no longer the code, it's the human's **awareness of what
exists**. You can't ask for a template you don't know is there, and there are hundreds. Riff
walks the belt past you so you learn what to *summon*.

This is self-demonstrating: a human watching AI-generated templates to learn what to ask for
**is** the Brutalist AI+Human split in the flesh — the AI generates, the human recognizes and
selects (labor separation, principles 4 + 5). The medium is the argument.

Two consequences run through every riff:
- **The payload is summoning-knowledge, not description.** Each riff ends on *when you'd reach
  for this — and when you wouldn't*. "Dies past ~8 bars" only matters as "so don't summon it
  for twelve categories; ask for a ranking instead."
- **The AI+Human split is the spine motif** (RIFFING's motif mechanic — established early,
  varied across the series, never verbatim): *"you didn't write this. You recognized you
  needed it. That's the job now."* It's the connective tissue between templates.

**Scope.** Riff narrates three input forms — Remotion, Manim, and mp4 (the perception
front-ends differ; see below). **This first series is Remotion** — the template-belt tour.
Manim and mp4 riffing are the same doctrine pointed at other inputs, in later series.

---

## Clock: sacred events, flexible holds

**Not "visual is master," not "audio is master."** Three things, in order of authority:

1. **The event *sequence* is sacred** — order and meaning come from the scene (the bar
   finishes, then the outlier lands). Never distorted to fit the voice.
2. **The audio *durations* set the pacing** — measured once from the generated TTS.
3. **The visual *holds* are the free variable** — the dead air *between* events stretches so
   each event seats under its beat. Events don't move; only the gaps flex.

So the ordering is a **bounded two-pass — measure once, conform once — not a loop:**

- **Remotion / Manim (re-renderable):** provisional render (gives the event sequence + a
  draft schedule) → beat sheet → generate audio + **measure** real clip durations → **re-
  render** with inter-event holds set to the measured audio.
- **mp4 (fixed):** phase-sample + scene-detect → beat sheet → generate audio → **conform by
  cutting** (trim / pad / freeze-frame *between* events). Same move, coarser tool.

This is the greybox → audio → conform pattern the pipeline already runs, with beat-sheet
discipline on top. The doc's fear ("animation chasing the voice") is a fear of distorting
*events*; stretching *holds* doesn't touch them, so the fear doesn't apply here.

---

## Perception must yield a *schedule*, not just a description

The two channels exist to produce the **event timeline** — every visual event with a frame
stamp.

- **Declared-truth (Manim/Remotion):** compute the schedule from the props. onda bar-chart
  `delay=0, stagger=4, duration=slow`: bar *i* finishes at `delay + i·stagger + duration`.
  Frame-accurate, no inference.
- **Sampled-frames (mp4):** scene-change detection for event frames; **phase** frames
  (start / mid / end — never random) for the look; timing from frame timestamps. Inference-
  only — hedge confidence.

---

## Cadence: the ~2-second micro-unit

Two independent literatures converge: jazz midlevel idea-units average **2.25s** (Frieler
et al., 140-solo corpus), and mean shared attention *before* a deictic word is **2.149s**
(Todisco et al.). Treat **~2s as the reactive micro-unit** — a reactive beat that runs
longer has already missed the next visual change. Coherence comes from **motivic
recurrence** (Frieler: ~25% of units relate to a prior one, mean chain ~2.8), not lexical
variety: return to the same thread and vary it, don't reinvent framing each beat.

---

## The beat sheet (the referent schema)

```jsonc
{
  "target": "onda:bar-chart",
  "clock": "sacred-events",          // events fixed; holds conform to measured audio
  "fps": 30, "duration_frames": 180,
  "events": [                        // the schedule — declared truth or scene-detect
    { "id": "E1", "frame": 0,  "desc": "bars empty, labels set" },
    { "id": "E2", "frame": 48, "desc": "Code bar tops out — the tall one" },
    { "id": "E3", "frame": 72, "desc": "Citations lands short — the outlier" }
  ],
  "motifs": ["confidence isn't accuracy", "the eye finds the outlier"],
  "beats": [
    { "type": "reactive", "pin": {"event": "E2", "lead_ms": -300},
      "max_words": 5, "deixis": true, "priority": 1, "text": "watch this one" },
    { "type": "predict",  "pin": {"event": "E3", "lead_ms": -600},
      "priority": 1, "text": "the next one should worry you" },
    { "type": "event",    "pin": {"event": "E3"} },            // observational silence
    { "type": "resolve",  "pin": {"event": "E3", "lag_ms": 300},
      "text": "there it is — a third of citations, wrong" },
    { "type": "analytic", "pin": {"range": ["E3+30", "end"]},
      "tier": "reset", "text": "..." },
    { "type": "outro-topic",   "render": "remotion", "source": "ABOUT.MD",
      "text": "one line placing this in its playlist / topic" },
    { "type": "outro-channel", "render": "remotion", "source": "AUTHOR.MD",
      "text": "the channel beat — who made this, where to go next" }
  ]
}
```

### Per-beat fields
- **type** — `reactive` · `predict` · `event` · `resolve` · `analytic`.
- **pin** — an event + `lead_ms` (negative = word/pointer arrive *before* the event) or a
  `range` (for soft-timed analytic beats).
- **priority** — the triage rank: **what to say first if the scene accelerates and the gap
  closes** (from the play-by-play duty hierarchy — down/distance before formation before
  run-pass). If time is lost, drop low-priority beats, not high.
- **max_words / tier** — the load cap (see chunking).
- *DEFERRED fields* (build only when we riff a high-event stream — see right-sizing):
  `abort_condition` (what renewed action cancels this beat mid-sentence), `return_point`
  (what narration snaps back to after an interrupt), `knowledge_source`
  (`visible` / `prepared` / `anticipation`).

### Beat types
- **reactive** — hard-pinned, ≤5 words, ~2s, deictic. Does exactly one of: direct attention,
  name the visible event, or mark a shift.
- **predict / event / resolve** — the atomic unit (POE, White & Gunstone 1992). `predict`
  states what an expert flags before it happens (short, falsifiable, audibly *ahead*);
  `event` is silence while it lands; `resolve` confirms **or** repairs, referencing the
  prediction ("there it is" / "except—"). A repaired wrong prediction is credible public
  model-updating — it demonstrates model quality, not failure. Resolve fires for confirmed
  predictions too.
- **analytic** — soft-pinned to a gap, prepared-knowledge-driven. Surface order: recap →
  mechanism → relevance; **if the gap is short, drop the recap first** (the image is still
  salient), keep mechanism + relevance. **Land on the summon-cue** — end on *when you'd reach
  for this template and when you wouldn't*; the tool-belt payload lives here.

### Deixis rule
Any visual pointer (highlight, zoom, the accent landing) **leads** the spoken deictic word;
the word must never arrive before the pointer, or the viewer searches retrospectively
("narration lag"). Demonstratives are **attention tools, not labels** (Jara-Ettinger &
Rubio-Fernández): if the field is crowded or attention has drifted, **restore attention
first** (an imperative — "look here") *then* attach the deictic. Tune the lead empirically;
don't hard-code a ms constant.

### The outro — mandatory, always Remotion
Every riff ends with a **two-beat outro**, and it is **always rendered in Remotion** — no
matter whether the body was Remotion, Manim, or mp4. The outro is the channel's branded tail
(teardown palette), not part of the riffed unit, so its renderer never changes with the input:
- **topic / playlist beat** — places the piece in its series/topic; content from the book's
  `ABOUT.MD`. (vox `OutroSeries`.)
- **channel beat** — the channel CTA / author; content from `AUTHOR.MD`. (vox `OutroCTA`.)

Riff **reuses** the existing vox `OutroSeries` / `OutroCTA` compositions + tokens and only
*fills* them — it never re-authors the outro. A Manim or mp4 riff is muxed, then the two
Remotion outro beats are appended as the tail.

### Silence — three typed devices
- **pre-complexity** — before a dense sequence: let the layout be read before motion.
- **observational** — during the event (`event` beat): zero verbal load while the viewer
  verifies the prediction.
- **post-complexity** — after resolution: consolidation before interpretation.

### Chunking — fit one chunk to one gap (three tiers)
- **micro-gap (~2s):** one deictic clause only — anchor + event. More risks missing the next
  change.
- **short reset:** one new analytic proposition + one consequence link (what happened + why
  it matters). Drop the recap if the image still carries it.
- **extended stoppage / replay:** event → mechanism → likely-next. The home for color /
  telestration / docent depth. (Segmentation + transient-information theory: Spanjers et al.,
  Mayer; working-memory ≈ 2–4 interacting elements.)

---

## Right-sizing (adopt now vs. defer)

**Adopt now** (calm showcase clips): sacred-events/flexible-holds clock · the event schedule
· the ~2s cadence · predict→event→resolve · reactive/analytic split · deixis-leads-pointer +
restore-attention · the three silences · the three chunk tiers · priority triage · motif
variation.

**Defer** until a high-event stream (a Manim simulation, a screen recording): the
preemptible-interrupt FSM and its `abort_condition` / `return_point` fields. A 6-second onda
chart has 2–4 scheduled events and no surprises to interrupt for — building the dispatcher
now is paying for preemption a slideshow can't use.

---

## Why this is the educational engine (not style)
The **predict** beat is the friction moment — the seconds where the viewer must evaluate a
claim before the scene resolves it. That evaluation is the learning. A riff that only reacts
("here's a bar chart") removes the friction and becomes the bypass the Irreducibly-Human
taxonomy names. predict→event→resolve is *why* riff claims to teach.

---

## What this means for the pilot
The current pilot (static RiffCard → silent scene) is the over-scripted failure this
doctrine rejects. Rebuild: shrink or drop the card; compute each scene's schedule; generate
a beat sheet; play narration **over** the scene; generate + measure the NBB audio; re-render
the scene's holds to the measured audio (conform); append the two Remotion outro beats
(topic + channel). Card-first becomes voice-over-scene.

---

*Grounded / load-bearing:* deixis-leads-pointer and demonstratives-as-attention-tools
(Diessel & Coventry; Todisco et al.; Jara-Ettinger & Rubio-Fernández); prepared-spontaneity
and midlevel-unit cadence (Berliner; Norgaard; Frieler et al.); reactive/analytic split and
yield discipline (sports-broadcast craft — Ferguson; RTNDF); anticipation as audible
expertise (Williams et al.; Gredin et al.); POE (White & Gunstone 1992); segmentation /
transient-information / chunk caps (Spanjers et al.; Mayer; Sweller). *Soft heuristics only:*
exact ms lead figures — treat as tunables, not constants.

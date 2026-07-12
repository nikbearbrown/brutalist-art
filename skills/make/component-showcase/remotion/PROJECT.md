# PROJECT.md — riff (Brutalist project state)

Home for the riff Remotion project and its output reels. Riff is a **Brutalist-level**
tool (it critiques any renderer — mp4, Remotion, Manim), which is why it lives here under
`brutalist/`, not inside vox. Vox's `_bench` is its first input.

**Phase: Schema populated → awaiting Verify before Generate.** Both layers below are filled
from the onda audit + the three gated decisions. No harness code is written yet.

---

## Designer / intent layer

**What riff is.** `riff <target>` renders a visual unit with a made-up example and *riffs*
on it in the **NikBearBrown / Teardown** voice, so a human can **see the tool belt** — learn
which of the hundreds of templates exist and *when to summon each*. AI makes writing Remotion
trivial; the scarce thing is the human's awareness of the inventory, and riff supplies it.
Output: short showcase-with-critique clips, batched into a series. Doctrine: `RIFFING.md`.

**Its Brutalist role.** Riff is self-demonstrating: a human watching AI-generated templates
to learn what to ask for **is** the AI+Human split — AI generates, the human recognizes and
selects (principles 4 + 5). It is also the *inform* step of bench promotion (367 keepers, 1
promoted): riff lets you *see* and *hear the trade-offs* so **you** decide what to promote
into the live pipeline (the 4th vector lane). Riff surfaces pros/cons and the summon-cue; it
never makes the keep call.

**Scope.** Riff narrates Remotion, Manim, and mp4. **This first series is Remotion** — the
template-belt tour; Manim and mp4 are the same doctrine on other inputs, later series.

**What each reel means.** One reel per **functional category** (DATA, TEXT, SHAPE, TITLE,
TRANSITION, BACKGROUND, EFFECT, AUDIO). A viewer sees every data-viz option together, every
text option together — a comparative catalog they can pause on, not a random showreel.

**Register.** NikBearBrown / Teardown (Feynman × MKBHD): take the scene apart, explain how it
works, judge the design choice, name where it earns its place in *teaching* and where it
doesn't. Honest about limits. Not a promo — a teardown.

**Examples are themed-educational.** Each fixture teaches a real concept (an AI / stats /
physics idea), so a reel reviewing a bar chart also teaches something. The showcase carries a
payload; it is never lorem-ipsum.

**Open creative questions.** (1) reel length target per scene (~20–30s?); (2) does each reel
open with a category cold-open (what this lane is *for* in teaching) — recommend yes;
(3) which concept theme per category for the fixtures (pick during Generate).

---

## Technical layer

**Stack.** Remotion (assembly + Remotion-scene rendering) · Manim (Manim-scene rendering) ·
ffmpeg (mp4 frame-grab) · ElevenLabs NBB voice + faster-whisper captions (reused from vox).
Constitution: `brutalist/CLAUDE.md` + the Remotion §; this project's specifics below.

**Pilot = onda** (cleanest tokens → highest render success). Audited contract:

- **59 components**, each `vox/remotion/_bench/onda/registry/components/<slug>/`:
  `<Component>.tsx` + `schema.ts` (Zod, **every prop `.default()`ed**, `kind` literal =
  slug) + `<slug>.meta.json` (`title`, `description`, `pickWhen`, `category`, `tags`,
  `dependencies`) + `README.md`.
- **Auto-instantiation:** `schema.parse({})` yields full valid props for any component. The
  harness renders any onda scene with zero config; fixtures override only **content** props
  (`data`, `text`, …) to make the example themed-educational.
- **meta.json is riff-script source:** `description` + `pickWhen` seed the NBB riff (what it
  does · when to use it), which the register then sharpens into pros/cons + educational read.
- **Tokens:** onda components read `var(--onda-*, fallback)`. Retint to teardown by setting
  12 CSS vars on the harness wrapper — onda is dark-canvas by default; this flips it to the
  teardown white/ink/red light look. onda's "accent is earned, one focal moment" == teardown's
  one-red rule, so the mapping is native:

  | `--onda-*` | onda (dark) | → teardown |
  |---|---|---|
  | `--onda-bg` | `#08080A` | `#FFFFFF` |
  | `--onda-surface` | `#0E0E12` | `#FFFFFF` |
  | `--onda-surface-2` | `#121217` | `#F0EEE9` |
  | `--onda-border` | `#1C1C22` | `#D4D4D4` |
  | `--onda-border-lit` | `#26262E` | `#545454` |
  | `--onda-text` | `#F2F2F4` | `#2A1A0E` |
  | `--onda-dim` | `#8E8E98` | `#545454` |
  | `--onda-faint` | `#56565F` | `#545454` |
  | `--onda-accent` | `#D96B82` | `#C8102E` |
  | `--onda-accent-soft` | `#E89AAB` | `#F6D8DC` |
  | `--onda-font-display` | Clash Display | Montserrat |
  | `--onda-font-body` | Space Grotesk | EB Garamond |

**Harness design (to Generate, unit by unit — not yet built):**
1. `src/harness/OndaScene.tsx` — a Remotion composition parametrized by `slug`: sets the 12
   teardown vars on a wrapper, imports the onda component by slug, renders
   `schema.parse(fixtureFor(slug))`. Wrapped in an error boundary — **renders what renders,
   logs what fails** (slug + reason) to `render-log.json`; never silent-drops.
2. `src/fixtures/<category>.ts` — themed-educational content overrides keyed by content prop.
   One theme per category (DATA first for the pilot).
3. `src/Root.tsx` — registers one composition per onda slug (from the meta.json list).
4. Driver (`riff.py` or `riff.sh`) — enumerate onda slugs → render each short clip (Mac) →
   author NBB riff per slug from meta.json → ElevenLabs NBB audio → faster-whisper captions →
   assemble `[clip + VO + caption]` per category into a reel.

**What runs where.** Harness/fixtures/Root/driver: authored here. **Rendering + ElevenLabs +
assembly: your Mac** (Remotion render, GPU, voice spend). Riff never renders or spends here.

**Phase gates.** (a) verify this schema before any code; (b) verify the harness on the first
onda render before scaling past the pilot; (c) verify riff scripts before ElevenLabs spend.

**Failure expectation.** Even onda (cleanest) will have some non-rendering components (unknown
props beyond defaults, primitive deps). The pilot's job is to *measure* that rate on the
cleanest collection before committing the other six.

---

## Generation log
_(empty — Generate has not begun; awaiting schema verify.)_

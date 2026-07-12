# Characters — Bear's Cubs (the closed pose library)

The consistency law made concrete: ONE host, drawn ONE way, with a CLOSED set
of named poses. Beats reference a pose by name (`host_pose`); nobody draws a
new gesture mid-episode. The same bear, the same wave, the same celebration,
every episode — recognition is the mechanism (video-deficit research: the
parasocial relationship builds across sessions; rewatchability is a feature).

## The host: BEAR
Kid-form of the Bear Brown mascot. Flat primitives only, no gradients, no
outlines. Design tokens (fixed — never restyle mid-series):
- fur `#7A4E2D` · paw pads/details `#5C3A20` · muzzle + inner ears `#E8D9C0`
- features INK `#2F2A26` · ground CREAM `#F3EBDD`
- props use the vox accents (CRIMSON/TEAL/GOLD) — the PROP carries the
  concept color, the bear never changes color.
- geometry: circles and capsules; head ≈ ⅓ of standing height; big round
  ears; small smile default.

## Pose library — one pose per beat role
Source of truth: `host/character-sheet.svg`. Finals: `host/<pose>.png`.

| pose | beat role | gesture | face |
|---|---|---|---|
| `wave` | hello | one paw raised open | smile |
| `present` | teach | paw extended toward the exemplar prop | smile |
| `point` | question | paw points straight at the viewer | smile |
| `listen` | pause | paw cupped to ear, head tilt | eyes closed, smile |
| `celebrate` | confirm | both paws up | open mouth (joy) |
| `not` | contrast | paws crossed in an X | flat mouth |
| `sing` | song | paws out, swaying; note marks | open mouth |
| `bye` | coview | both paws waving | smile |

Rules:
- **Closed set.** A beat's `host_pose` must be one of the eight. Adding a
  pose is a series-level decision recorded in this file first.
- **Role↔pose defaults** follow the table; Gate K warns on mismatches.
- **The dance clips** in `../../bearbrown/` are the motion form of `sing` —
  use a clip for the song beat when motion is wanted; the still for teasers.
- **Static-background law still applies:** the bear holds a pose per beat;
  pose-to-pose change happens AT the cut, never as within-beat animation
  during teaching (motion budget belongs to the concept, not the host).

## Upgrading the art (optional, later)
The SVG sheet is the frozen intent (Clockwork Part 1). To upgrade a pose to
finished art, run Illustrator Concept-to-Vector with the sheet cell as the
reference sketch — draft on the 10-credit model, commit at 40 — then export
`host/<pose>.png` (transparent). Prompts, one per pose, paste as-is:

```
HOST-WAVE, flat vector children's illustration of a round friendly brown bear standing, one paw raised in an open wave, small smile, cream muzzle, big round ears, solid flat fills, no gradients, no outlines, plain background
```
```
HOST-PRESENT, flat vector children's illustration of a round friendly brown bear standing, one paw extended to the side as if presenting an object, small smile, cream muzzle, big round ears, solid flat fills, no gradients, no outlines, plain background
```
```
HOST-POINT, flat vector children's illustration of a round friendly brown bear standing, one paw pointing straight forward at the viewer, small smile, cream muzzle, big round ears, solid flat fills, no gradients, no outlines, plain background
```
```
HOST-LISTEN, flat vector children's illustration of a round friendly brown bear standing, one paw cupped to its ear, eyes closed, gentle smile, head tilted, cream muzzle, big round ears, solid flat fills, no gradients, no outlines, plain background
```
```
HOST-CELEBRATE, flat vector children's illustration of a round friendly brown bear standing, both paws raised high, mouth open in joy, cream muzzle, big round ears, solid flat fills, no gradients, no outlines, plain background
```
```
HOST-NOT, flat vector children's illustration of a round friendly brown bear standing, paws crossed in an X in front of its chest, flat neutral mouth, cream muzzle, big round ears, solid flat fills, no gradients, no outlines, plain background
```
```
HOST-SING, flat vector children's illustration of a round friendly brown bear standing, paws out to both sides mid-sway, mouth open singing, three small music notes above, cream muzzle, big round ears, solid flat fills, no gradients, no outlines, plain background
```
```
HOST-BYE, flat vector children's illustration of a round friendly brown bear standing, both paws raised waving goodbye, warm smile, cream muzzle, big round ears, solid flat fills, no gradients, no outlines, plain background
```

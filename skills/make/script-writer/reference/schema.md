# The style-agnostic beat_sheet (what `script` emits)

Same envelope as every vox `beat_sheet.json`, with two disciplines added: every
beat carries a Brown Blue **role**, and `shot.source` is left **null** so the
sheet commits to *content*, not *renderer*. Downstream (`slate cut`,
`remotion pass`, doodle, pure Manim) fills the shot; nothing here has to change.

## metadata
| key | value | notes |
|---|---|---|
| `title` | the video's on-screen title | the answer, not the topic |
| `slug` | kebab-case id | folder name |
| `register` | `"Teardown"` | the gate expects this |
| `voice` | `"NikBearBrown"` | audience/charter |
| `voice_id` | `"${ELEVENLABS_VOICE_NIKBEARBROWN}"` | resolved from `vox/.env` at audio time |
| `palette` | `"teardown"` | **default**, overridable per style |
| `style_preset` | `"nikbearbrown"` | **default**, overridable per style |
| `pedagogy` | `"brownblue"` | marks the arc it was built against |
| `key_case` | one line | §1.1 — the puzzle that motivates everything; never spoken as preamble |
| `tier` | `single-insight` / `standard` / `multi-act` | derived (§5) |
| `source` | where the text came from | path, URL, or `"pasted"` |
| `total_estimated_duration_seconds` | float | sum of beats |
| `deferred` | `[ "…", … ]` | scope cuts, surfaced in the BOUNDARY beat |

## beats[]
| key | value | who reads it |
|---|---|---|
| `beat_id` | `B01`, `B02`, … | |
| `role` | one of `HOOK INSTANCE TRANSFORM ABSTRACTION TANGENT PAYOFF BOUNDARY` | gate (arc) |
| `narration_text` | the spoken line, Teardown voice | gate (forbidden scan), audio |
| `visual_intent` | what the viewer SEES — renderer-free prose | the style builder |
| `on_screen_text` | key label(s), optional | style builder |
| `estimated_duration_s` | ~5–9 s/beat | gate (length) |
| `lands_equation` | `true` on an ABSTRACTION that puts up an equation | gate → forces next beat = TANGENT |
| `references_hook` | `true` on the PAYOFF that returns the HOOK object | gate (warn) |
| `viewer_exercise` | one concrete task, on the BOUNDARY beat | gate (hard) |
| `shot` | `{ "type":"GRAPHIC", "source":null, "motion":"fade" }` | **left open** for any style |

## The role arc (partial order the gate audits)
```
HOOK        key case, unsolved — opens the video, zero vocabulary
INSTANCE    a concrete parametrized example, shown moving   (≥2 before any ABSTRACTION)
TRANSFORM   the same object morphing — the intuition carrier
ABSTRACTION the general statement / definition — arrives as an ENDPOINT
TANGENT     unpacks a landed equation (only after an equation-landing ABSTRACTION)
PAYOFF      the HOOK resolved by the abstraction (same object back on screen)
BOUNDARY    what this video did NOT teach + one viewer exercise (fused with the outro)
```

## Dressing it in a style later
`shot.source:null` is the whole point. To render:
- **House / Manim** → `slate cut <dir>`: writes `vox_scenes.py`, sets each content
  beat `source:"manim"`, wraps with the nbb Remotion open/outro.
- **Remotion** → `remotion pass <dir>`: fills beats carrying a `shot.remotion.pattern`.
- **Pure 3b1b** → set every beat `source:"manim"`, no bookends.
- **Doodle / other** → hand `role`+`narration_text`+`visual_intent` to that builder.
The script and its arc never change; only the shot layer does.

# 9:16 Shorts — Schedule Plan

Computed 2026-07-19. **This is a plan only — no uploads have been made.**
Human authorizes each upload; run youtube-publisher skill with `--allow-partial` per row.

## Channel routing

| Channel | Shorts playlist | Videos |
|---|---|---|
| @NikBearBrown | PLJs-MuR0Up1M (Shorts) | 12 videos |
| @HumanitariansAI | PLERO8fp8W7gE (Shorts) | 1 video |

## @NikBearBrown — 12 shorts

Anchor: last @NikBearBrown scheduled upload was 2026-07-18T10:39:32Z (claude-liam-profile-aditi-deodhar 16:9).
Short slots start 2026-07-19T10:00:00Z, staggered 1h apart.

| # | Schedule (UTC) | slug | short mp4 | dur |
|---|---|---|---|---|
| 1 | 2026-07-19T10:00:00Z | claude-liam-off-switch-gram | `short/claude-liam-off-switch-gram-short.mp4` | 2:47 |
| 2 | 2026-07-19T11:00:00Z | claude-liam-81k-interviews | `short/claude-liam-81k-interviews-short.mp4` | 2:56 |
| 3 | 2026-07-19T12:00:00Z | claude-liam-claude-values-axes | `short/claude-liam-claude-values-axes-short.mp4` | 2:36 |
| 4 | 2026-07-19T13:00:00Z | sycophancy-to-subterfuge | `short/sycophancy-to-subterfuge-short.mp4` | 2:20 |
| 5 | 2026-07-19T14:00:00Z | claude-for-teachers | `short/claude-for-teachers-short.mp4` | 2:06 |
| 6 | 2026-07-19T15:00:00Z | claude-liam-algorithmic-art | `short/claude-liam-algorithmic-art-short.mp4` | 2:35 |
| 7 | 2026-07-19T16:00:00Z | claude-liam-coding-agents-social-sciences | `short/claude-liam-coding-agents-social-sciences-short.mp4` | 2:32 |
| 8 | 2026-07-19T17:00:00Z | claude-liam-economic-index-cadences | `short/claude-liam-economic-index-cadences-short.mp4` | 2:43 |
| 9 | 2026-07-19T18:00:00Z | access-scaffolding-text-substitution | `short/access-scaffolding-text-substitution-short.mp4` | 2:49 |
| 10 | 2026-07-19T19:00:00Z | cra-progression-scaffold | `short/cra-progression-scaffold-short.mp4` | 2:26 |
| 11 | 2026-07-19T20:00:00Z | fluency-prerequisite-comprehension | `short/fluency-prerequisite-comprehension-short.mp4` | 2:38 |
| 12 | 2026-07-19T21:00:00Z | preserve-cognitive-demand-differentiation | `short/preserve-cognitive-demand-differentiation-short.mp4` | 2:35 |

### Reel locations for @NikBearBrown uploads

```
brutalist-art/youtube/claude-liam-off-switch-gram/
brutalist-art/youtube/claude-liam-81k-interviews/
brutalist-art/youtube/claude-liam-claude-values-axes/
anthropics/youtube/sycophancy-to-subterfuge/
brutalist-art/youtube/claude-for-teachers/
brutalist-art/youtube/claude-liam-algorithmic-art/
brutalist-art/youtube/claude-liam-coding-agents-social-sciences/
brutalist-art/youtube/claude-liam-economic-index-cadences/
anthropics/k12-teacher-skills/youtube/access-scaffolding-text-substitution/
anthropics/k12-teacher-skills/youtube/cra-progression-scaffold/
anthropics/k12-teacher-skills/youtube/fluency-prerequisite-comprehension/
anthropics/k12-teacher-skills/youtube/preserve-cognitive-demand-differentiation/
```

## @HumanitariansAI — 1 short

| # | Schedule (UTC) | slug | short mp4 | dur |
|---|---|---|---|---|
| 1 | 2026-07-19T10:00:00Z | claude-liam-profile-kaustubha-eluri | `short/claude-liam-profile-kaustubha-eluri-short.mp4` | 2:39 |

```
humanitarians_html/youtube/claude/claude-liam-profile-kaustubha-eluri/
```

## Publisher command (per video, from books/)

```bash
./brutalist-art/art run <reel-path>/short   # verify short looks good first
python3 brutalist-art/skills/upload/youtube-publisher/youtube_publish.py \
  <reel-path>/short \
  --channel humanitarians  # or nikbearbrown \
  --playlist "Shorts" \
  --allow-partial --no-pairs \
  --scheduled 2026-07-19T10:00:00Z
```

## Quality notes

- All 13 shorts are under the 3:00 Shorts cap (longest: 2:56).
- Non-916 Remotion compositions center-cropped 16:9→9:16; edge text may clip.
  Affected: sycophancy B01–B03, claude-for-teachers B01–B05 (STILL), K12 B01/B02a/B02b.
- kaustubha-eluri audio regenerated from narration text (source mp3s were absent);
  timing matches original (Kokoro am_onyx).
- off-switch-gram middle beats (B01–B10 ex. B12) are Manim/GRAPHIC slates;
  only bookend Remotion cards are 916-native.

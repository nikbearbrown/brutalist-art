# 9:16 Batch Build Log — 2026-07-18/19

| id | title | slug | in-dur | out-dur | method | qc | status |
|---|---|---|---|---|---|---|---|
| iUXC69MZl8E | Persisting Progress | feature-list-checkpoint-persistence | 2:12 | — | — | — | SKIPPED(exists) |
| HcQlKBkA9tM | Caching Pixels | screenshot-prompt-caching | 2:13 | — | — | — | SKIPPED(exists) |
| QENWK9l8J9s | When Safety Training Fails | sleeper-agents-safety-training-fails | 2:07 | — | — | — | SKIPPED(exists) |
| YuKL035BUuQ | Musinique Mark 2 (16:9) | claude-liam-musinique-logo-2-remotion-showcase-16x9 | 3:46 | — | — | — | FAILED(no-master-mp4) |
| 3dSlg4LGV60 | Musinique Mark (16:9) | claude-liam-musinique-logo-remotion-showcase-16x9 | 3:43 | — | — | — | FAILED(no-master-mp4) |
| gD-MhJlFHtA | Bear Brown Initials (16:9) | claude-liam-bear-brown-initials-remotion-showcase-16x9 | 4:06 | — | — | — | FAILED(no-master-mp4) |
| 9_YRDjgYJgE | Bear Brown Mark (16:9) | claude-liam-bear-brown-logo-remotion-showcase-16x9 | 3:17 | — | — | — | FAILED(no-master-mp4) |
| 8VVGo70TMlQ | Bear Brown Initials (portrait) | claude-liam-bear-brown-initials-remotion-showcase | 3:41 | — | — | — | FAILED(no-master-mp4) |
| G7GtXjuUhoA | Musinique Mark (portrait) | claude-liam-musinique-logo-remotion-showcase | 3:43 | — | — | — | FAILED(no-master-mp4) |
| WDmrjHrtnlI | HAI Wordmark (16:9) | claude-liam-hai-wordmark-remotion-showcase-16x9 | 3:01 | — | — | — | FAILED(no-master-mp4) |
| dFvpoQZdiN4 | H Mark (16:9) | claude-liam-h-logo-remotion-showcase-16x9 | 2:50 | — | — | — | FAILED(no-master-mp4) |
| JmkNlXL38sM | VHL/ccRCC | nbb-vox-vhl-hif | 5:42 | — | — | — | FAILED(broken-mp4-symlink) |
| wNjxSDwtJgk | IDH1 | hai-vox-idh-2hg | 5:36 | — | — | — | FAILED(no-master-mp4) |
| uJ4-cBbz4Yg | pH-Triggered Lock | vox-endosomal-escape | 4:25 | — | — | — | FAILED(no-master-mp4) |
| 4HoBA5otwMU | Claude On Average | medhavy-claude-on-average | 2:29 | — | — | — | FAILED(no-master-mp4) |
| eX_jbpfwmI0 | Claude Taught | claude-liam-claude-taught | 2:13 | — | — | — | FAILED(no-master-mp4) |
| PK8o4CU_2m8 | Photoelectric Effect | vox-photoelectric-effect | 3:24 | — | — | — | FAILED(broken-mp4-symlink) |
| 1yCYkISIMDQ | An Off Switch for Dangerous Knowledge | claude-liam-off-switch-gram | 2:47 | 2:47 | reformat+drop(B09,YTV01,B11,B02) | PASS | DONE |
| okgNY7sHYmE | 81,000 Interviews | claude-liam-81k-interviews | 2:56 | 2:56 | reformat+drop(B13,YTV01,B08) | PASS | DONE |
| fR9GCsYtjYs | Values Axes | claude-liam-claude-values-axes | 3:24 | 2:36 | drop(B05,B02,B04,YTV01)+reformat | PASS | DONE |
| — | Sycophancy to Subterfuge | sycophancy-to-subterfuge | 2:20 | 2:20 | reformat(under cap) | PASS | DONE |
| — | Claude for Teachers | claude-for-teachers | 2:06 | 2:06 | reformat(under cap); B01–B05 STILL(16:9 center-crop) | PASS | DONE |
| — | Algorithmic Art | claude-liam-algorithmic-art | 2:35 | 2:35 | drop(BVDT,B03,B08,B04,B02)+reformat | PASS | DONE |
| — | Coding Agents Social Sciences | claude-liam-coding-agents-social-sciences | 2:32 | 2:32 | drop(B05,B03,B06)+reformat | PASS | DONE |
| — | Economic Index Cadences | claude-liam-economic-index-cadences | 2:43 | 2:43 | drop(B06,B05,B04,B01,B08)+reformat | PASS | DONE |
| — | Access Scaffolding | access-scaffolding-text-substitution | 2:49 | 2:49 | reformat(under cap) | PASS | DONE |
| — | CRA Progression | cra-progression-scaffold | 2:26 | 2:26 | reformat(under cap) | PASS | DONE |
| — | Fluency Prerequisite | fluency-prerequisite-comprehension | 2:38 | 2:38 | reformat(under cap) | PASS | DONE |
| — | Preserve Cognitive Demand | preserve-cognitive-demand-differentiation | 2:35 | 2:35 | reformat(under cap) | PASS | DONE |
| — | The Engineer Who Stayed | claude-liam-profile-kaustubha-eluri | 2:39 | 2:39 | drop(B03,B06)+reformat; audio regenerated(source mp3s absent) | PASS | DONE |

## Notes

- **SKIPPED(exists)**: Short already existed at the time of the batch — not overwritten.
- **FAILED(no-master-mp4)**: Folder has beat_sheet.json and media sources but no compiled master mp4. Likely a planning-only or Remotion-monolithic folder. Needs full render pipeline, not just reformat.
- **FAILED(broken-mp4-symlink)**: Master mp4 symlink resolves to a non-existent file. Needs source video recovery.
- **center-crop note**: Beats with 16:9 Remotion compositions (no 916 twin) are rendered at 1920×1080 then center-cropped to 1080×1920. Edge content may be clipped.
- **audio regenerated**: kaustubha-eluri's source mp3 files were absent from the video folder (likely embedded during original compile). Kokoro am_onyx re-generated from beat_sheet narration text.

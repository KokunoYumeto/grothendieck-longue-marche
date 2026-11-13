# Re-cut of the waiting archive packages, and the notes packet (13 Nov 2026)

Claude Opus 5.5 at effort high, 0 sub-agents, 13 Nov 2026 (build 17:30-18:20 UTC, notes packet 18:20-18:40 UTC).

## Counts

| | Packages | Scans kept | GB (scans + context zips) | under 30 | 30-39 | 40-50 | over 50 | mean |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| before (36-178 of 12 Nov) | 143 | 9,362 | 14.10 | 0 | 2 | 18 | 123 | 65.5 |
| after (36-250) | 215 | 9,362 | 14.22 (+ RESULTS_STATE, about 0.01) | 5 | 34 | 176 | 0 | 43.5 |

The same 9,765 planned scans (9,362 kept, 403 blank) are covered exactly once before and after (checked by script).
Under 30 kept scans: 57_MPL_49+50 (21), 59_MPL_21 (27), 108_MPL_161-6 (28), 123_MPL_161-4 (28),
250_MPL_119_144-161+119_276-281 (22): each is a cote of at most 50 scans that the rule may not split and that does not
fit beside its neighbour in the same group (21 + 22 = 57; 49+50+51+52 = 58 split at the cote boundary; 129 + the 119
leaves = 59). C: free 39 GB at the end (lowest during the build: 26 GB).

## Mapping

`MAPPING.tsv`: every old package (folder, kept, cotes and scans) with its new packages (folders, kept, cotes and scans).
Order W is kept: ranks 4 and 5, the ten probes, then the groups of 12 Nov in their order. Numbers 36-250.
Old 36-44 (ranks 4-5) became 36-47; the probes 45-54 became 48-58 (the probe 49-52, 58 scans, is now 57 and 58);
old 55-178 became 59-250. Rank 4 is now one stream (144 rest, 148, 143, 141, 145).
Packages 36 and 37 were sent by the coordinator at about 18:34 UTC; they are in `SENT_PACKAGES.txt` and the notes tool
never changes them.

## Script changes (backups next to each script, suffix `_before_recut_20261113`)

- `full_archive_20261112/plan.py`: one cap of 50 (`RECUT_CAP`) for every group; the caps of 12 Nov stay in PLAN.json as
  `cap_20261112`; numbering from 36 (`FIRST_NUM`); the groups of the old 36-54 prepended as `EARLY_GROUPS` with their
  segments as built then (from PDF page 1 where they started there); **the cap counts kept scans**: blank scans are
  left out of the zip by the build tool, so `pack_kept` runs pack_dp unchanged on the kept scans (blank lists of every
  waiting scan from the 12 Nov manifests, `BLANKS_20261112.json`, made by `make_blanks.py`) and maps each cut back to
  scan numbers. Effect: 215 packages instead of 221 counted on planned scans, and no package splits a 51-scan pair
  such as 89+132 (47 kept). **141 moved before 145** inside rank 4 (145 + 141 = 54, over the cap; 143 + 141 = 50):
  without it 141 would be a package of 16 scans. Old PLAN.json kept as `PLAN_20261112_before_recut.json`.
- `full_archive_20261112/build_full.py`: own progress file and log (`RECUT_PROGRESS_20261113.txt`,
  `BUILD_LOG_RECUT_20261113.json`); disk floor 15 GB (was 40 GB); the old 36-54 get their 12 Nov context folders
  (`context_ranks4_5_probes_20261112`) and their questions paragraphs verbatim (`QUESTIONS_36_54.json`, taken from
  their prompts; rank 5's item on 153/155 only in the package holding them; the 49-52 question on 51/52 only in the
  package holding them); for the split probe 49-52 a copy of its README names the package's cotes and where the
  others went; one more check `kept_as_expected`; the as-built prompt is saved as `PROMPT_as_built_20261113.md`.
  Edited by `edit_build_full.py`.
- `full_archive_20261112/contexts.py`: package numbers in the READMEs (probe packages, 156-8) are taken from PLAN.json
  instead of being written in (they were 45-53 and 97-99).
- `pack_dp.py` and `build_package_multi.py`: unchanged.
- `ARCHIVE_PROMPT_TEMPLATE.md` (backup `ARCHIVE_PROMPT_TEMPLATE_before_results_state_20261113.md`): one paragraph in
  the notes part ("Our own results on these subjects: `notes/RESULTS_STATE.md`": transcription first; read it before
  the notes; connect notes by id; do not re-derive what an entry settles; record under its id how the manuscript
  bears on an open item). Every waiting prompt was built from it.

The old 36-178 folders were moved to `packages_superseded_20261113\` before the build and deleted after all new
packages passed (14 GB).

## The notes packet: `tools_20261113/build_results_state.py`

- Writes `notes/RESULTS_STATE.md` (at most 40,000 bytes) into the package's context zip; the zips carry no MANIFEST
  file, so their README.md (the zip's list of contents) gains a section naming it; the zip is rebuilt through a
  temporary file and tested. `--refresh <folder>` rebuilds one package (run it just before sending), `--all` every
  waiting package, `--dry` writes the file only.
- Sources: the main `*_results.csv` of the newest version of each run (20 registers, 2,119 rows: LM1, LM2, LM4, LM7,
  LM7_PUSH, LM8, FLAGGED_149, EXIT_ONE_TYPE, CYCLOTOMIC_KERNEL, PRETOT, TOTEX, TOTEX2 and the eight Dérivateurs returns);
  intake verdicts per row from INTAKE_TOTEX2 and INTAKE_LM8; PUSH_ITEMS*, IMPLICATIONS*, INTAKE_* results and notes,
  COMPANION_COMPLETION_*; MATHS_PROMPTS_TALLY.md (state of each run); the notes of every returned archive package
  (3,264 notes); the war game round 2 and the hunches H1-H9 (261 items).
- Selection: each package's context key and question key name subjects (keyword sets); score = distinct keyword hits
  + 3 per mention of the package's cotes + 2 for a run that belongs to the subject. Five sections, filled in order with
  byte budgets and the rest passed on: open items (open rows of the registers, push items, candidate prompt items,
  companion questions), settled rows, intake readings, archive notes, war-game items; then the state of the runs and
  the source paths (relative to Documents, no user name). Each entry: id (e.g. **LM4 C.12**), status (the return's own,
  marked as its claim unless an intake verdict follows), source file.
- Same-cote rule (coordinator, 13 Nov): the notes of every returned package of the same cote go in under
  `same_cote_<cote>/` (final `<PKG>_notes.md`; a checkpoint's `working_notes.jsonl` only when no final exists), with
  a README section "Same cote, earlier packages" and a clause at the end of the prompt's context sentence. Today only
  cote 144 has such returns, and 36 and 37 (sent) already carry them by hand; no waiting package matches yet. The rule
  applies at every `--refresh`, so the probes' returns (136, 93, 79, 83, 154, 138, 43) reach the rest of their cotes.
- Sizes: 215 packets, median 38.6 KB, 118 of 35 KB or more, 49 under 10 KB (minimum 2.0 KB): the small ones are
  subjects our runs have not touched (EGA plans, SGA drafts 31-42, SGA 3 and reeditions, functional analysis, the
  popular texts, cote 93). Per package in the table below (bytes; entries per section).

## Checks

Every package: both zips pass `testzip`; 3 images per kept scan; kept + blank = the planned ranges; kept = the
expected count from the 12 Nov blank lists (all 215 equal); context zip with README.md and `notes/RESULTS_STATE.md`
(at most 40 KB) named in the README; folder flat (PROMPT.md and two zips); prompt counts and no placeholder; the
RESULTS_STATE paragraph in the prompt; the lint (`push_rule_pro_prompts.py --lint`) passes on all 215 prompts and on
the template. Results in `BUILD_LOG_RECUT_20261113.json` and `VERIFY.json` (215 of 215 pass).

## Packages
| 36 | 36_MPL_144_122-167 | rank 4: the rest of 144, then 148, 143, 141,  | 43 | 144: 125, 128, 133 | 58.5 | rank4 | yes |  | 39985 (25 / 49 / 1 / 13 / 9) |
| 37 | 37_MPL_144_168-184+148_001-028 | rank 4: the rest of 144, then 148, 143, 141,  | 43 | 144: 172, 179 | 61.7 | rank4 | yes |  | 39990 (25 / 49 / 1 / 13 / 9) |
| 38 | 38_MPL_148_029-072 | rank 4: the rest of 144, then 148, 143, 141,  | 44 | none | 83.4 | rank4 | yes |  | 39978 (25 / 48 / 1 / 13 / 9) |
| 39 | 39_MPL_143+141 | rank 4: the rest of 144, then 148, 143, 141,  | 50 | none | 57.7 | rank4 | yes |  | 39885 (25 / 48 / 1 / 13 / 9) |
| 40 | 40_MPL_145 | rank 4: the rest of 144, then 148, 143, 141,  | 38 | none | 34.5 | rank4 | yes |  | 39880 (25 / 48 / 1 / 13 / 9) |
| 41 | 41_MPL_150_001-043 | rank 5 with 153 and 155 | 41 | 150: 6, 11 | 66.0 | rank5 | yes |  | 39813 (30 / 39 / 2 / 10 / 8) |
| 42 | 42_MPL_150_044-084 | rank 5 with 153 and 155 | 41 | none | 54.3 | rank5 | yes |  | 39813 (30 / 39 / 2 / 10 / 8) |
| 43 | 43_MPL_150_085-099+151_001-031 | rank 5 with 153 and 155 | 43 | 151: 10, 16, 26 | 50.6 | rank5 | yes |  | 39818 (30 / 39 / 2 / 10 / 8) |
| 44 | 44_MPL_151_032-075 | rank 5 with 153 and 155 | 44 | none | 57.3 | rank5 | yes |  | 39813 (30 / 39 / 2 / 10 / 8) |
| 45 | 45_MPL_152+120 | rank 5 with 153 and 155 | 38 | none | 65.9 | rank5 | yes |  | 39818 (30 / 39 / 2 / 10 / 8) |
| 46 | 46_MPL_121_001-048 | rank 5 with 153 and 155 | 43 | 121: 3, 25, 29, 38, 40 | 57.8 | rank5 | yes |  | 39813 (30 / 39 / 2 / 10 / 8) |
| 47 | 47_MPL_121_049-073+153+155 | rank 5 with 153 and 155 | 44 | 121: 53, 64, 69 | 83.5 | rank5 | yes |  | 39823 (30 / 39 / 2 / 10 / 8) |
| 48 | 48_MPL_156-1+156-2 | probe: 156-1 and 156-2 | 46 | none | 64.9 | probe_156 | yes |  | 17815 (8 / 31 / 0 / 4 / 2) |
| 49 | 49_MPL_136_002-046 | probe: 136 | 44 | 136: 19 | 53.7 | probe_136 | yes |  | 38710 (32 / 62 / 2 / 0 / 3) |
| 50 | 50_MPL_93_002-046 | probe: 93 | 42 | 93: 2, 26, 35 | 56.6 | probe_93 | yes | yes | 3454 (0 / 0 / 0 / 3 / 0) |
| 51 | 51_MPL_79_001-045 | probe: 79 | 45 | none | 53.5 | probe_79 | yes |  | 38632 (11 / 79 / 0 / 1 / 0) |
| 52 | 52_MPL_83_001-045 | probe: 83 | 43 | 83: 2, 18 | 59.0 | probe_83 | yes |  | 38632 (11 / 79 / 0 / 1 / 0) |
| 53 | 53_MPL_154_001-045 | probe: 154 | 44 | 154: 11 | 158.7 | probe_154 | yes |  | 17794 (8 / 31 / 0 / 4 / 2) |
| 54 | 54_MPL_138_001-045 | probe: 138 | 44 | 138: 24 | 48.4 | probe_138 | yes |  | 39753 (26 / 50 / 2 / 8 / 2) |
| 55 | 55_MPL_159 | probe: 159 | 32 | 159: 14, 24 | 39.9 | probe_159 | yes |  | 39018 (12 / 68 / 0 / 8 / 0) |
| 56 | 56_MPL_43_001-045 | probe: 43 | 42 | 43: 14, 39, 44 | 53.5 | probe_43 | yes |  | 39623 (21 / 62 / 0 / 2 / 7) |
| 57 | 57_MPL_49+50 | probe: 49, 50, 51, 52 | 21 | none | 26.7 | probe_49-52 | yes |  | 39639 (21 / 62 / 0 / 2 / 7) |
| 58 | 58_MPL_51+52 | probe: 49, 50, 51, 52 | 37 | none | 45.9 | probe_49-52 | yes |  | 39639 (21 / 62 / 0 / 2 / 7) |
| 59 | 59_MPL_21 | rank 3: the EGA plans, with 127 and 128 | 27 | 21: 3 | 46.0 | rank3 | yes | yes | 4501 (0 / 0 / 0 / 4 / 1) |
| 60 | 60_MPL_22+23_002-016 | rank 3: the EGA plans, with 127 and 128 | 44 | none | 65.6 | rank3 | yes | yes | 4505 (0 / 0 / 0 / 4 / 1) |
| 61 | 61_MPL_23_017-062 | rank 3: the EGA plans, with 127 and 128 | 43 | 23: 42, 43, 48 | 59.7 | rank3 | yes | yes | 4501 (0 / 0 / 0 / 4 / 1) |
| 62 | 62_MPL_23_063-099+26 | rank 3: the EGA plans, with 127 and 128 | 43 | 23: 69, 72, 86, 95 | 67.6 | rank3 | yes | yes | 4505 (0 / 0 / 0 / 4 / 1) |
| 63 | 63_MPL_35+48+102+127 | rank 3: the EGA plans, with 127 and 128 | 45 | 102: 8 | 61.1 | rank3 | yes |  | 4515 (0 / 0 / 0 / 4 / 1) |
| 64 | 64_MPL_128 | rank 3: the EGA plans, with 127 and 128 | 30 | 128: 31 | 35.9 | rank3 | yes |  | 4502 (0 / 0 / 0 / 4 / 1) |
| 65 | 65_MPL_134-1+134-2_146-185 | rank 9: the handwritten leaves of Pursuing St | 45 | 134-1: 3 | 67.2 | dossier | yes |  | 39517 (27 / 40 / 4 / 13 / 9) |
| 66 | 66_MPL_134-8_043-087 | rank 9: the handwritten leaves of Pursuing St | 44 | 134-8: 60 | 113.9 | dossier | yes |  | 39651 (27 / 40 / 4 / 13 / 9) |
| 67 | 67_MPL_158_002-044 | rank 9: the handwritten leaves of Pursuing St | 40 | 158: 6, 17, 44 | 46.8 | dossier | yes |  | 39649 (27 / 40 / 4 / 13 / 9) |
| 68 | 68_MPL_158_045-086 | rank 9: the handwritten leaves of Pursuing St | 40 | 158: 55, 60 | 43.6 | dossier | yes |  | 39649 (27 / 40 / 4 / 13 / 9) |
| 69 | 69_MPL_108+112+113+114+115 | rank 9: the handwritten leaves of Pursuing St | 40 | none | 126.1 | dossier | yes |  | 39643 (27 / 40 / 4 / 13 / 9) |
| 70 | 70_MPL_116+117 | rank 9: the handwritten leaves of Pursuing St | 34 | 116: 9 | 40.6 | dossier | yes |  | 39513 (27 / 40 / 4 / 13 / 9) |
| 71 | 71_MPL_118 | rank 9: the handwritten leaves of Pursuing St | 38 | 118: 13, 38 | 72.3 | dossier | yes |  | 39649 (27 / 40 / 4 / 13 / 9) |
| 72 | 72_MPL_103+104 | rank 9: the handwritten leaves of Pursuing St | 32 | 103: 8 | 40.9 | dossier | yes |  | 39513 (27 / 40 / 4 / 13 / 9) |
| 73 | 73_MPL_105 | rank 9: the handwritten leaves of Pursuing St | 48 | 105: 9, 24, 29, 42 | 162.6 | dossier | yes |  | 39649 (27 / 40 / 4 / 13 / 9) |
| 74 | 74_MPL_106+107 | rank 9: the handwritten leaves of Pursuing St | 41 | none | 158.1 | dossier | yes |  | 39513 (27 / 40 / 4 / 13 / 9) |
| 75 | 75_MPL_109 | rank 9: the handwritten leaves of Pursuing St | 34 | 109: 12, 16, 20 | 56.7 | dossier | yes |  | 39649 (27 / 40 / 4 / 13 / 9) |
| 76 | 76_MPL_111+162-5_019-032+135_002-018 | rank 9: the handwritten leaves of Pursuing St | 42 | 162-5: 19, 21, 32; 135: 2, 7 | 65.8 | dossier | yes | yes | 39520 (27 / 40 / 4 / 13 / 9) |
| 77 | 77_MPL_135_019-059 | rank 9: the handwritten leaves of Pursuing St | 36 | 135: 25, 31, 35, 39, 46 | 59.4 | dossier | yes |  | 39649 (27 / 40 / 4 / 13 / 9) |
| 78 | 78_MPL_137_002-044 | rank 9 continued: 137 and 133 (II.9) | 42 | 137: 6 | 52.2 | ii9 | yes |  | 38550 (32 / 61 / 2 / 0 / 3) |
| 79 | 79_MPL_137_045-086 | rank 9 continued: 137 and 133 (II.9) | 42 | none | 51.7 | ii9 | yes |  | 38550 (32 / 61 / 2 / 0 / 3) |
| 80 | 80_MPL_133 | rank 9 continued: 137 and 133 (II.9) | 50 | 133: 5, 10, 41 | 64.4 | ii9 | yes |  | 38550 (32 / 61 / 2 / 0 / 3) |
| 81 | 81_MPL_14_002-044 | rank 6: motives | 40 | 14: 18, 23, 43 | 58.2 | motives | yes |  | 14190 (2 / 4 / 0 / 4 / 16) |
| 82 | 82_MPL_14_045-086 | rank 6: motives | 41 | 14: 72 | 58.6 | motives | yes |  | 14190 (2 / 4 / 0 / 4 / 16) |
| 83 | 83_MPL_14_087-132 | rank 6: motives | 41 | 14: 105, 110, 119, 125, 130 | 59.6 | motives | yes |  | 14190 (2 / 4 / 0 / 4 / 16) |
| 84 | 84_MPL_13 | rank 6: motives | 44 | 13: 3, 13, 22, 26, 33, 36, 45 | 58.1 | motives | yes |  | 14190 (2 / 4 / 0 / 4 / 16) |
| 85 | 85_MPL_12_002-050 | rank 6: motives | 48 | 12: 20 | 70.5 | motives | yes | yes | 14646 (2 / 4 / 0 / 4 / 17) |
| 86 | 86_MPL_12_051-098 | rank 6: motives | 48 | none | 79.6 | motives | yes | yes | 14646 (2 / 4 / 0 / 4 / 17) |
| 87 | 87_MPL_12_099-149 | rank 6: motives | 48 | 12: 103, 110, 124 | 74.4 | motives | yes | yes | 14646 (2 / 4 / 0 / 4 / 17) |
| 88 | 88_MPL_12_150-168+15_002-033 | rank 6: motives | 49 | 15: 15, 25 | 62.4 | motives | yes | yes | 14650 (2 / 4 / 0 / 4 / 17) |
| 89 | 89_MPL_15_034-086 | rank 6: motives | 49 | 15: 58, 65, 80, 83 | 77.0 | motives | yes | yes | 14190 (2 / 4 / 0 / 4 / 16) |
| 90 | 90_MPL_15_087-138 | rank 6: motives | 49 | 15: 116, 127, 134 | 66.0 | motives | yes | yes | 14190 (2 / 4 / 0 / 4 / 16) |
| 91 | 91_MPL_15_139-194 | rank 6: motives | 49 | 15: 140, 146, 153, 156, 158, 167, 169 | 70.5 | motives | yes | yes | 14190 (2 / 4 / 0 / 4 / 16) |
| 92 | 92_MPL_15_195-228+18_002-017 | rank 6: motives | 49 | 18: 8 | 73.2 | motives | yes | yes | 14194 (2 / 4 / 0 / 4 / 16) |
| 93 | 93_MPL_18_018-062 | rank 6: motives | 45 | none | 64.7 | motives | yes |  | 14190 (2 / 4 / 0 / 4 / 16) |
| 94 | 94_MPL_136_047-094 | the rest of 136 (II.9) | 46 | 136: 47, 79 | 63.9 | ii9 | yes |  | 38536 (32 / 61 / 2 / 0 / 3) |
| 95 | 95_MPL_136_095-141 | the rest of 136 (II.9) | 46 | 136: 122 | 69.3 | ii9 | yes |  | 38536 (32 / 61 / 2 / 0 / 3) |
| 96 | 96_MPL_136_142-188 | the rest of 136 (II.9) | 46 | 136: 161 | 70.2 | ii9 | yes |  | 38536 (32 / 61 / 2 / 0 / 3) |
| 97 | 97_MPL_136_189-234 | the rest of 136 (II.9) | 45 | 136: 214 | 66.4 | ii9 | yes |  | 38536 (32 / 61 / 2 / 0 / 3) |
| 98 | 98_MPL_136_235-281 | the rest of 136 (II.9) | 46 | 136: 243 | 64.9 | ii9 | yes |  | 38536 (32 / 61 / 2 / 0 / 3) |
| 99 | 99_MPL_136_282-327 | the rest of 136 (II.9) | 45 | 136: 319 | 76.2 | ii9 | yes |  | 38536 (32 / 61 / 2 / 0 / 3) |
| 100 | 100_MPL_136_328-376 | the rest of 136 (II.9) | 45 | 136: 344, 347, 354, 356 | 75.0 | ii9 | yes |  | 38537 (32 / 61 / 2 / 0 / 3) |
| 101 | 101_MPL_138_046-089 | rank 10: the rest of 138 (III.7) | 42 | 138: 79, 88 | 48.4 | maps | yes |  | 39860 (27 / 39 / 4 / 13 / 9) |
| 102 | 102_MPL_138_090-133 | rank 10: the rest of 138 (III.7) | 43 | 138: 92 | 48.0 | maps | yes |  | 39860 (27 / 39 / 4 / 13 / 9) |
| 103 | 103_MPL_76_002-047 | rank 10: maps on surfaces and the icosahedron | 40 | 76: 2, 11, 15, 35, 45, 47 | 53.4 | maps | yes |  | 39872 (27 / 39 / 4 / 13 / 9) |
| 104 | 104_MPL_76_048-063+88+70_002-016 | rank 10: maps on surfaces and the icosahedron | 44 | 76: 49; 88: 10 | 59.4 | maps | yes |  | 39880 (27 / 39 / 4 / 13 / 9) |
| 105 | 105_MPL_70_017-064 | rank 10: maps on surfaces and the icosahedron | 43 | 70: 28, 38, 49, 61, 64 | 54.1 | maps | yes |  | 39872 (27 / 39 / 4 / 13 / 9) |
| 106 | 106_MPL_70_065-109 | rank 10: maps on surfaces and the icosahedron | 44 | 70: 73 | 54.2 | maps | yes |  | 39872 (27 / 39 / 4 / 13 / 9) |
| 107 | 107_MPL_70_110-126+75 | rank 10: maps on surfaces and the icosahedron | 46 | 70: 113, 126; 75: 29 | 59.0 | maps | yes |  | 39876 (27 / 39 / 4 / 13 / 9) |
| 108 | 108_MPL_161-6 | rank 10: maps on surfaces and the icosahedron | 28 | 161-6: 3, 12, 21, 24, 32 | 41.5 | maps | yes |  | 39875 (27 / 39 / 4 / 13 / 9) |
| 109 | 109_MPL_79_046-094 | rank 10 with 79: the rest of 79 | 49 | none | 60.0 | maps | yes |  | 39858 (27 / 39 / 4 / 13 / 9) |
| 110 | 110_MPL_79_095-144 | rank 10 with 79: the rest of 79 | 50 | none | 61.1 | maps | yes |  | 39858 (27 / 39 / 4 / 13 / 9) |
| 111 | 111_MPL_79_145-194 | rank 10 with 79: the rest of 79 | 50 | none | 63.6 | maps | yes |  | 39858 (27 / 39 / 4 / 13 / 9) |
| 112 | 112_MPL_79_195-244 | rank 10 with 79: the rest of 79 | 50 | none | 67.0 | maps | yes |  | 39858 (27 / 39 / 4 / 13 / 9) |
| 113 | 113_MPL_79_245-297 | rank 10 with 79: the rest of 79 | 50 | 79: 272, 275, 282 | 56.8 | maps | yes |  | 39858 (27 / 39 / 4 / 13 / 9) |
| 114 | 114_MPL_83_046-089 | rank 10 with 83: the rest of 83 | 42 | 83: 47, 80 | 60.7 | maps | yes |  | 39858 (27 / 39 / 4 / 13 / 9) |
| 115 | 115_MPL_83_090-133 | rank 10 with 83: the rest of 83 | 43 | 83: 101 | 61.9 | maps | yes |  | 39858 (27 / 39 / 4 / 13 / 9) |
| 116 | 116_MPL_83_134-177 | rank 10 with 83: the rest of 83 | 43 | 83: 149 | 60.2 | maps | yes |  | 39858 (27 / 39 / 4 / 13 / 9) |
| 117 | 117_MPL_83_178-222 | rank 10 with 83: the rest of 83 | 43 | 83: 182, 206 | 64.4 | maps | yes |  | 39858 (27 / 39 / 4 / 13 / 9) |
| 118 | 118_MPL_64_002-039 | rank 10 with 64 | 38 | none | 49.8 | book3 | yes |  | 39664 (27 / 38 / 4 / 13 / 9) |
| 119 | 119_MPL_64_040-077 | rank 10 with 64 | 38 | none | 43.5 | book3 | yes |  | 39664 (27 / 38 / 4 / 13 / 9) |
| 120 | 120_MPL_64_078-115 | rank 10 with 64 | 38 | none | 44.0 | book3 | yes |  | 39664 (27 / 38 / 4 / 13 / 9) |
| 121 | 121_MPL_64_116-157 | rank 10 with 64 | 39 | 64: 122, 130, 142 | 45.8 | book3 | yes |  | 39664 (27 / 38 / 4 / 13 / 9) |
| 122 | 122_MPL_161-3 | rank 10: the two popular texts | 46 | 161-3: 2, 3, 14, 17, 23, 28, 30, 34 | 68.0 | popular | none |  | 2046 (0 / 0 / 0 / 0 / 0) |
| 123 | 123_MPL_161-4 | rank 10: the two popular texts | 28 | 161-4: 2, 14, 19 | 43.4 | popular | none |  | 2046 (0 / 0 / 0 / 0 / 0) |
| 124 | 124_MPL_156-8_002-043 | rank 11: the final state of the Geometrie des | 42 | none | 58.8 | forms | yes |  | 17839 (8 / 31 / 0 / 4 / 2) |
| 125 | 125_MPL_156-8_044-085 | rank 11: the final state of the Geometrie des | 42 | none | 51.4 | forms | yes |  | 17839 (8 / 31 / 0 / 4 / 2) |
| 126 | 126_MPL_156-8_086-127 | rank 11: the final state of the Geometrie des | 42 | none | 52.8 | forms | yes |  | 17839 (8 / 31 / 0 / 4 / 2) |
| 127 | 127_MPL_156-5 | rank 11: the final state of the Geometrie des | 48 | none | 67.5 | forms | yes |  | 17839 (8 / 31 / 0 / 4 / 2) |
| 128 | 128_MPL_156-3 | rank 11: the final state of the Geometrie des | 40 | none | 58.0 | forms | yes |  | 17839 (8 / 31 / 0 / 4 / 2) |
| 129 | 129_MPL_156-9_002-047 | rank 11: the final state of the Geometrie des | 46 | none | 61.2 | forms | yes |  | 17839 (8 / 31 / 0 / 4 / 2) |
| 130 | 130_MPL_156-9_048-093 | rank 11: the final state of the Geometrie des | 46 | none | 58.4 | forms | yes |  | 17839 (8 / 31 / 0 / 4 / 2) |
| 131 | 131_MPL_156-9_094-140 | rank 11: the final state of the Geometrie des | 46 | 156-9: 129 | 58.9 | forms | yes |  | 17839 (8 / 31 / 0 / 4 / 2) |
| 132 | 132_MPL_67_002-052 | rank 12: 67 | 46 | 67: 15, 22, 23, 47, 52 | 101.5 | book3 | none |  | 39838 (27 / 39 / 4 / 13 / 9) |
| 133 | 133_MPL_67_053-101 | rank 12: 67 | 47 | 67: 83, 90 | 93.4 | book3 | none |  | 39838 (27 / 39 / 4 / 13 / 9) |
| 134 | 134_MPL_10_002-049 | rank 13: tensor categories, cycles, L-functio | 46 | 10: 18, 32 | 71.0 | book2rest | yes | yes | 6855 (0 / 0 / 0 / 3 / 7) |
| 135 | 135_MPL_10_050-098 | rank 13: tensor categories, cycles, L-functio | 47 | 10: 59, 85 | 68.7 | book2rest | yes | yes | 6855 (0 / 0 / 0 / 3 / 7) |
| 136 | 136_MPL_10_099-150 | rank 13: tensor categories, cycles, L-functio | 47 | 10: 101, 110, 114, 138, 142 | 78.5 | book2rest | yes | yes | 6855 (0 / 0 / 0 / 3 / 7) |
| 137 | 137_MPL_10_151-198 | rank 13: tensor categories, cycles, L-functio | 47 | 10: 156 | 80.5 | book2rest | yes | yes | 6855 (0 / 0 / 0 / 3 / 7) |
| 138 | 138_MPL_11_002-042 | rank 13: tensor categories, cycles, L-functio | 39 | 11: 2, 33 | 43.1 | book2rest | yes |  | 6855 (0 / 0 / 0 / 3 / 7) |
| 139 | 139_MPL_11_043-058+56 | rank 13: tensor categories, cycles, L-functio | 50 | 11: 50; 56: 10, 19, 34 | 67.2 | book2rest | yes |  | 6859 (0 / 0 / 0 / 3 / 7) |
| 140 | 140_MPL_60_002-035 | rank 13: tensor categories, cycles, L-functio | 34 | none | 54.8 | book2rest | none |  | 6855 (0 / 0 / 0 / 3 / 7) |
| 141 | 141_MPL_60_036-070 | rank 13: tensor categories, cycles, L-functio | 35 | none | 56.0 | book2rest | none |  | 6855 (0 / 0 / 0 / 3 / 7) |
| 142 | 142_MPL_69_002-049 | rank 14: regular polyhedra, graphs (calculati | 46 | 69: 2, 41 | 57.9 | calc | yes |  | 38680 (11 / 79 / 0 / 1 / 0) |
| 143 | 143_MPL_69_050-103 | rank 14: regular polyhedra, graphs (calculati | 46 | 69: 65, 66, 73, 77, 89, 94, 95, 100 | 63.3 | calc | yes |  | 38680 (11 / 79 / 0 / 1 / 0) |
| 144 | 144_MPL_69_104-120+72_002-034 | rank 14: regular polyhedra, graphs (calculati | 47 | 69: 105, 107; 72: 22 | 53.2 | calc | yes |  | 38684 (11 / 79 / 0 / 1 / 0) |
| 145 | 145_MPL_72_035-081 | rank 14: regular polyhedra, graphs (calculati | 47 | none | 50.2 | calc | yes |  | 38680 (11 / 79 / 0 / 1 / 0) |
| 146 | 146_MPL_72_082-113+74_002-018 | rank 14: regular polyhedra, graphs (calculati | 47 | 74: 8, 18 | 57.1 | calc | yes |  | 38684 (11 / 79 / 0 / 1 / 0) |
| 147 | 147_MPL_74_019-070 | rank 14: regular polyhedra, graphs (calculati | 47 | 74: 20, 25, 32, 41, 46 | 64.4 | calc | yes |  | 38680 (11 / 79 / 0 / 1 / 0) |
| 148 | 148_MPL_74_071-120 | rank 14: regular polyhedra, graphs (calculati | 48 | 74: 72, 92 | 65.6 | calc | yes |  | 38680 (11 / 79 / 0 / 1 / 0) |
| 149 | 149_MPL_74_121-136+85_002-034 | rank 14: regular polyhedra, graphs (calculati | 48 | 74: 127 | 59.4 | calc | yes |  | 38684 (11 / 79 / 0 / 1 / 0) |
| 150 | 150_MPL_85_035-082 | rank 14: regular polyhedra, graphs (calculati | 48 | none | 55.1 | calc | yes |  | 38680 (11 / 79 / 0 / 1 / 0) |
| 151 | 151_MPL_85_083-098+86 | rank 14: regular polyhedra, graphs (calculati | 48 | none | 62.4 | calc | yes |  | 38684 (11 / 79 / 0 / 1 / 0) |
| 152 | 152_MPL_93_047-091 | rank 15: the rest of 93; 161-5 | 42 | 93: 71, 79, 85 | 62.5 | 93rest | yes | yes | 3476 (0 / 0 / 0 / 3 / 0) |
| 153 | 153_MPL_93_092-134 | rank 15: the rest of 93; 161-5 | 42 | 93: 125 | 59.6 | 93rest | yes | yes | 3476 (0 / 0 / 0 / 3 / 0) |
| 154 | 154_MPL_93_135-177 | rank 15: the rest of 93; 161-5 | 42 | 93: 141 | 55.7 | 93rest | yes | yes | 3476 (0 / 0 / 0 / 3 / 0) |
| 155 | 155_MPL_93_178-220 | rank 15: the rest of 93; 161-5 | 43 | none | 50.3 | 93rest | yes | yes | 3476 (0 / 0 / 0 / 3 / 0) |
| 156 | 156_MPL_93_221-236+161-5 | rank 15: the rest of 93; 161-5 | 43 | 161-5: 2 | 45.2 | 93rest | yes | yes | 3483 (0 / 0 / 0 / 3 / 0) |
| 157 | 157_MPL_19_002-048 | rank 16: categories, universal algebra, topos | 43 | 19: 3, 13, 30, 35 | 60.2 | rank16 | none |  | 39155 (45 / 38 / 4 / 5 / 3) |
| 158 | 158_MPL_19_049-096 | rank 16: categories, universal algebra, topos | 43 | 19: 56, 70, 72, 86, 94 | 50.1 | rank16 | none |  | 39155 (45 / 38 / 4 / 5 / 3) |
| 159 | 159_MPL_161-1+161-2_002-028 | rank 16: categories, universal algebra, topos | 38 | 161-1: 2, 3, 9, 15; 161-2: 2, 3, 17, 26 | 57.5 | rank16 | none |  | 39165 (45 / 38 / 4 / 5 / 3) |
| 160 | 160_MPL_161-2_029-069 | rank 16: categories, universal algebra, topos | 38 | 161-2: 33, 36, 54 | 58.9 | rank16 | none |  | 39158 (45 / 38 / 4 / 5 / 3) |
| 161 | 161_MPL_161-2_070-112 | rank 16: categories, universal algebra, topos | 38 | 161-2: 80, 89, 97, 108, 111 | 59.9 | rank16 | none |  | 39158 (45 / 38 / 4 / 5 / 3) |
| 162 | 162_MPL_156-4_002-045 | rank 17: the three earlier versions of Analys | 44 | none | 63.5 | forms | yes |  | 17840 (8 / 31 / 0 / 4 / 2) |
| 163 | 163_MPL_156-4_046-089 | rank 17: the three earlier versions of Analys | 44 | none | 63.5 | forms | yes |  | 17840 (8 / 31 / 0 / 4 / 2) |
| 164 | 164_MPL_156-6_002-040 | rank 17: the three earlier versions of Analys | 39 | none | 45.5 | forms | yes |  | 17840 (8 / 31 / 0 / 4 / 2) |
| 165 | 165_MPL_156-6_041-079 | rank 17: the three earlier versions of Analys | 39 | none | 43.5 | forms | yes |  | 17840 (8 / 31 / 0 / 4 / 2) |
| 166 | 166_MPL_156-6_080-094+156-7_002-028 | rank 17: the three earlier versions of Analys | 42 | none | 53.4 | forms | yes |  | 17847 (8 / 31 / 0 / 4 / 2) |
| 167 | 167_MPL_156-7_029-071 | rank 17: the three earlier versions of Analys | 43 | none | 54.6 | forms | yes |  | 17840 (8 / 31 / 0 / 4 / 2) |
| 168 | 168_MPL_156-7_072-114 | rank 17: the three earlier versions of Analys | 43 | none | 53.6 | forms | yes |  | 17840 (8 / 31 / 0 / 4 / 2) |
| 169 | 169_MPL_71 | rank 18, Book V: Jordan, immersions, pseudoli | 41 | 71: 2, 5, 16, 18, 20, 35 | 51.6 | bookv18 | none |  | 17832 (8 / 31 / 0 / 4 / 2) |
| 170 | 170_MPL_80_002-056 | rank 18, Book V: Jordan, immersions, pseudoli | 49 | 80: 2, 9, 16, 20, 31, 56 | 62.1 | bookv18 | none |  | 17832 (8 / 31 / 0 / 4 / 2) |
| 171 | 171_MPL_80_057-073+81_002-037 | rank 18, Book V: Jordan, immersions, pseudoli | 49 | 80: 60, 72; 81: 9, 31 | 48.4 | bookv18 | none |  | 17836 (8 / 31 / 0 / 4 / 2) |
| 172 | 172_MPL_81_038-055+154_046-076 | rank 18, Book V: Jordan, immersions, pseudoli | 49 | none | 130.7 | bookv18 | yes |  | 17837 (8 / 31 / 0 / 4 / 2) |
| 173 | 173_MPL_154_077-126 | rank 18, Book V: Jordan, immersions, pseudoli | 49 | 154: 99 | 187.1 | bookv18 | yes |  | 17833 (8 / 31 / 0 / 4 / 2) |
| 174 | 174_MPL_154_127-176 | rank 18, Book V: Jordan, immersions, pseudoli | 50 | none | 195.6 | bookv18 | yes |  | 17833 (8 / 31 / 0 / 4 / 2) |
| 175 | 175_MPL_73+77_002-026 | rank 18, Book IV: polygons, quadrics, graphs | 49 | 73: 3, 8, 12, 14 | 58.2 | calc | yes |  | 39604 (15 / 66 / 0 / 3 / 5) |
| 176 | 176_MPL_77_027-075 | rank 18, Book IV: polygons, quadrics, graphs | 49 | none | 58.6 | calc | yes |  | 39600 (15 / 66 / 0 / 3 / 5) |
| 177 | 177_MPL_77_076-124 | rank 18, Book IV: polygons, quadrics, graphs | 49 | none | 58.4 | calc | yes |  | 39600 (15 / 66 / 0 / 3 / 5) |
| 178 | 178_MPL_77_125-158+78_002-016 | rank 18, Book IV: polygons, quadrics, graphs | 49 | none | 56.5 | calc | yes |  | 39604 (15 / 66 / 0 / 3 / 5) |
| 179 | 179_MPL_78_017-063 | rank 18, Book IV: polygons, quadrics, graphs | 47 | none | 58.3 | calc | yes |  | 39600 (15 / 66 / 0 / 3 / 5) |
| 180 | 180_MPL_78_064-110 | rank 18, Book IV: polygons, quadrics, graphs | 47 | none | 56.8 | calc | yes |  | 39600 (15 / 66 / 0 / 3 / 5) |
| 181 | 181_MPL_78_111-130+82_002-028 | rank 18, Book IV: polygons, quadrics, graphs | 47 | none | 56.0 | calc | yes |  | 39604 (15 / 66 / 0 / 3 / 5) |
| 182 | 182_MPL_82_029-079 | rank 18, Book IV: polygons, quadrics, graphs | 48 | 82: 33, 36, 46 | 53.8 | calc | yes |  | 39600 (15 / 66 / 0 / 3 / 5) |
| 183 | 183_MPL_84_002-049 | rank 18, Book IV: polygons, quadrics, graphs | 47 | 84: 8 | 78.8 | calc | yes |  | 39600 (15 / 66 / 0 / 3 / 5) |
| 184 | 184_MPL_84_050-096 | rank 18, Book IV: polygons, quadrics, graphs | 47 | none | 70.6 | calc | yes |  | 39600 (15 / 66 / 0 / 3 / 5) |
| 185 | 185_MPL_84_097-145 | rank 18, Book IV: polygons, quadrics, graphs | 48 | 84: 123 | 75.7 | calc | yes |  | 39600 (15 / 66 / 0 / 3 / 5) |
| 186 | 186_MPL_84_146-193 | rank 18, Book IV: polygons, quadrics, graphs | 48 | none | 70.7 | calc | yes |  | 39600 (15 / 66 / 0 / 3 / 5) |
| 187 | 187_MPL_87 | rank 18, Book IV: polygons, quadrics, graphs | 36 | 87: 2, 17, 21, 32 | 49.2 | calc | yes |  | 39600 (15 / 66 / 0 / 3 / 5) |
| 188 | 188_MPL_89+132 | rank 18, Book IV: polygons, quadrics, graphs | 47 | 132: 5, 10, 13, 25 | 62.6 | calc | yes |  | 39605 (15 / 66 / 0 / 3 / 5) |
| 189 | 189_MPL_43_046-093 | rank 19: duality of groups, Picard, abelian v | 46 | 43: 83, 88 | 58.8 | abelian | yes |  | 39668 (21 / 62 / 0 / 2 / 7) |
| 190 | 190_MPL_43_094-142 | rank 19: duality of groups, Picard, abelian v | 46 | 43: 99, 111, 127 | 70.6 | abelian | yes |  | 39668 (21 / 62 / 0 / 2 / 7) |
| 191 | 191_MPL_43_143-192 | rank 19: duality of groups, Picard, abelian v | 46 | 43: 157, 166, 175, 179 | 69.4 | abelian | yes |  | 39668 (21 / 62 / 0 / 2 / 7) |
| 192 | 192_MPL_43_193-208+45_002-032 | rank 19: duality of groups, Picard, abelian v | 46 | 43: 194 | 72.2 | abelian | yes |  | 39672 (21 / 62 / 0 / 2 / 7) |
| 193 | 193_MPL_45_033-080 | rank 19: duality of groups, Picard, abelian v | 47 | 45: 44 | 77.4 | abelian | yes |  | 39668 (21 / 62 / 0 / 2 / 7) |
| 194 | 194_MPL_46_002-048 | rank 19: duality of groups, Picard, abelian v | 47 | none | 68.7 | abelian | yes |  | 39668 (21 / 62 / 0 / 2 / 7) |
| 195 | 195_MPL_46_049-095 | rank 19: duality of groups, Picard, abelian v | 47 | none | 71.3 | abelian | yes |  | 39668 (21 / 62 / 0 / 2 / 7) |
| 196 | 196_MPL_53+55 | rank 19: duality of groups, Picard, abelian v | 49 | 55: 16 | 80.6 | abelian | yes |  | 39672 (21 / 62 / 0 / 2 / 7) |
| 197 | 197_MPL_59+58_002-019 | rank 19: duality of groups, Picard, abelian v | 44 | 59: 22 | 64.0 | abelian | yes |  | 39672 (21 / 62 / 0 / 2 / 7) |
| 198 | 198_MPL_58_020-067 | rank 19: duality of groups, Picard, abelian v | 44 | 58: 29, 45, 55, 64 | 66.6 | abelian | yes |  | 39668 (21 / 62 / 0 / 2 / 7) |
| 199 | 199_MPL_90+91_002-018 | rank 20: K-theory, Neron, residues, intersect | 39 | 91: 4, 15 | 55.6 | rank20 | none |  | 16147 (4 / 13 / 0 / 4 / 10) |
| 200 | 200_MPL_91_019-058 | rank 20: K-theory, Neron, residues, intersect | 38 | 91: 30, 33 | 53.5 | rank20 | none |  | 16143 (4 / 13 / 0 / 4 / 10) |
| 201 | 201_MPL_91_059-098 | rank 20: K-theory, Neron, residues, intersect | 38 | 91: 60, 86 | 45.2 | rank20 | none |  | 16143 (4 / 13 / 0 / 4 / 10) |
| 202 | 202_MPL_91_099-143 | rank 20: K-theory, Neron, residues, intersect | 38 | 91: 103, 112, 117, 125, 130, 133, 137 | 58.5 | rank20 | none |  | 16143 (4 / 13 / 0 / 4 / 10) |
| 203 | 203_MPL_94+97 | rank 20: K-theory, Neron, residues, intersect | 39 | 97: 6, 15 | 51.7 | rank20 | none |  | 16147 (4 / 13 / 0 / 4 / 10) |
| 204 | 204_MPL_98 | rank 20: K-theory, Neron, residues, intersect | 43 | none | 61.4 | rank20 | none |  | 16143 (4 / 13 / 0 / 4 / 10) |
| 205 | 205_MPL_101 | rank 20: K-theory, Neron, residues, intersect | 42 | none | 57.0 | rank20 | none |  | 16144 (4 / 13 / 0 / 4 / 10) |
| 206 | 206_MPL_31_002-051 | rank 21: SGA 4, 5 and 7 drafts | 46 | 31: 34, 40, 41, 46 | 69.5 | rank21 | none |  | 4833 (1 / 1 / 0 / 1 / 2) |
| 207 | 207_MPL_31_052-102 | rank 21: SGA 4, 5 and 7 drafts | 47 | 31: 53, 64, 73, 89 | 77.3 | rank21 | none |  | 4833 (1 / 1 / 0 / 1 / 2) |
| 208 | 208_MPL_32 | rank 21: SGA 4, 5 and 7 drafts | 46 | 32: 2 | 49.4 | rank21 | none |  | 4833 (1 / 1 / 0 / 1 / 2) |
| 209 | 209_MPL_33_002-049 | rank 21: SGA 4, 5 and 7 drafts | 48 | none | 73.5 | rank21 | none |  | 4833 (1 / 1 / 0 / 1 / 2) |
| 210 | 210_MPL_33_050-097 | rank 21: SGA 4, 5 and 7 drafts | 48 | none | 61.7 | rank21 | none |  | 4833 (1 / 1 / 0 / 1 / 2) |
| 211 | 211_MPL_33_098-146 | rank 21: SGA 4, 5 and 7 drafts | 49 | none | 66.2 | rank21 | none |  | 4833 (1 / 1 / 0 / 1 / 2) |
| 212 | 212_MPL_33_147-181+34_002-017 | rank 21: SGA 4, 5 and 7 drafts | 49 | 33: 169; 34: 2 | 72.6 | rank21 | none |  | 4837 (1 / 1 / 0 / 1 / 2) |
| 213 | 213_MPL_34_018-065 | rank 21: SGA 4, 5 and 7 drafts | 47 | 34: 52 | 73.0 | rank21 | none |  | 4833 (1 / 1 / 0 / 1 / 2) |
| 214 | 214_MPL_34_066-113 | rank 21: SGA 4, 5 and 7 drafts | 47 | 34: 83 | 66.9 | rank21 | none |  | 4833 (1 / 1 / 0 / 1 / 2) |
| 215 | 215_MPL_34_114-161 | rank 21: SGA 4, 5 and 7 drafts | 47 | 34: 129 | 69.2 | rank21 | none |  | 4833 (1 / 1 / 0 / 1 / 2) |
| 216 | 216_MPL_34_162-210 | rank 21: SGA 4, 5 and 7 drafts | 47 | 34: 163, 182 | 65.6 | rank21 | none |  | 4833 (1 / 1 / 0 / 1 / 2) |
| 217 | 217_MPL_36_002-052 | rank 21: SGA 4, 5 and 7 drafts | 49 | 36: 2, 9 | 72.0 | rank21 | none |  | 4833 (1 / 1 / 0 / 1 / 2) |
| 218 | 218_MPL_36_053-085+39 | rank 21: SGA 4, 5 and 7 drafts | 49 | 39: 2, 9, 18 | 62.9 | rank21 | none |  | 4837 (1 / 1 / 0 / 1 / 2) |
| 219 | 219_MPL_40+41+42 | rank 21: SGA 4, 5 and 7 drafts | 46 | none | 55.3 | rank21 | none |  | 4841 (1 / 1 / 0 / 1 / 2) |
| 220 | 220_MPL_122 | rank 22: descent, heights, etale cohomology | 32 | 122: 2, 19 | 45.6 | rank22 | none |  | 16138 (4 / 13 / 0 / 4 / 10) |
| 221 | 221_MPL_123 | rank 22: descent, heights, etale cohomology | 44 | 123: 21, 25, 33 | 65.9 | rank22 | none |  | 16138 (4 / 13 / 0 / 4 / 10) |
| 222 | 222_MPL_125+126 | rank 22: descent, heights, etale cohomology | 39 | 126: 17, 26, 31 | 50.2 | rank22 | none |  | 16143 (4 / 13 / 0 / 4 / 10) |
| 223 | 223_MPL_131 | rank 22: descent, heights, etale cohomology | 38 | 131: 11, 19, 22 | 60.0 | rank22 | none |  | 16138 (4 / 13 / 0 / 4 / 10) |
| 224 | 224_MPL_130 | rank 22: descent, heights, etale cohomology | 44 | 130: 3, 9, 16, 21, 34 | 70.5 | rank22 | none |  | 16138 (4 / 13 / 0 / 4 / 10) |
| 225 | 225_MPL_57_002-045 | rank 23: Picard schemes | 43 | 57: 2 | 67.4 | abelian | yes |  | 39638 (21 / 62 / 0 / 2 / 7) |
| 226 | 226_MPL_57_046-088 | rank 23: Picard schemes | 43 | none | 66.3 | abelian | yes |  | 39638 (21 / 62 / 0 / 2 / 7) |
| 227 | 227_MPL_57_089-132 | rank 23: Picard schemes | 43 | 57: 98 | 65.5 | abelian | yes |  | 39638 (21 / 62 / 0 / 2 / 7) |
| 228 | 228_MPL_57_133-179 | rank 23: Picard schemes | 43 | 57: 137, 146, 168, 172 | 66.1 | abelian | yes |  | 39638 (21 / 62 / 0 / 2 / 7) |
| 229 | 229_MPL_57_180-225 | rank 23: Picard schemes | 43 | 57: 200, 207, 213 | 54.6 | abelian | yes |  | 39638 (21 / 62 / 0 / 2 / 7) |
| 230 | 230_MPL_57_226-270 | rank 23: Picard schemes | 43 | 57: 232, 247 | 73.5 | abelian | yes |  | 39638 (21 / 62 / 0 / 2 / 7) |
| 231 | 231_MPL_57_271-315 | rank 23: Picard schemes | 43 | 57: 278, 293 | 67.8 | abelian | yes |  | 39638 (21 / 62 / 0 / 2 / 7) |
| 232 | 232_MPL_62_002-050 | rank 23: Picard schemes | 46 | 62: 3, 18, 27 | 70.9 | abelian | yes |  | 39638 (21 / 62 / 0 / 2 / 7) |
| 233 | 233_MPL_62_051-097 | rank 23: Picard schemes | 46 | 62: 56 | 88.7 | abelian | yes |  | 39638 (21 / 62 / 0 / 2 / 7) |
| 234 | 234_MPL_63_002-049 | rank 23: Picard schemes | 45 | 63: 2, 15, 35 | 79.1 | abelian | yes | yes | 39638 (21 / 62 / 0 / 2 / 7) |
| 235 | 235_MPL_63_050-101 | rank 23: Picard schemes | 46 | 63: 56, 65, 79, 82, 86, 95 | 68.5 | abelian | yes | yes | 39638 (21 / 62 / 0 / 2 / 7) |
| 236 | 236_MPL_27+28 | rank 24: SGA 3 and the reeditions | 44 | 27: 8, 17 | 62.7 | rank24 | none |  | 2624 (1 / 1 / 0 / 0 / 0) |
| 237 | 237_MPL_29_002-048 | rank 24: SGA 3 and the reeditions | 46 | 29: 7 | 69.1 | rank24 | none | yes | 2620 (1 / 1 / 0 / 0 / 0) |
| 238 | 238_MPL_29_049-094 | rank 24: SGA 3 and the reeditions | 46 | none | 66.0 | rank24 | none | yes | 2620 (1 / 1 / 0 / 0 / 0) |
| 239 | 239_MPL_29_095-140 | rank 24: SGA 3 and the reeditions | 46 | none | 71.7 | rank24 | none | yes | 2620 (1 / 1 / 0 / 0 / 0) |
| 240 | 240_MPL_29_141-187 | rank 24: SGA 3 and the reeditions | 47 | none | 67.1 | rank24 | none | yes | 2620 (1 / 1 / 0 / 0 / 0) |
| 241 | 241_MPL_29_188-217+37_002-022 | rank 24: SGA 3 and the reeditions | 47 | 29: 190, 208; 37: 2, 6 | 54.1 | rank24 | none | yes | 2624 (1 / 1 / 0 / 0 / 0) |
| 242 | 242_MPL_37_023-074 | rank 24: SGA 3 and the reeditions | 47 | 37: 29, 32, 46, 56, 65 | 52.1 | rank24 | none | yes | 2620 (1 / 1 / 0 / 0 / 0) |
| 243 | 243_MPL_37_075-100+160 | rank 24: SGA 3 and the reeditions | 47 | 160: 18 | 54.8 | rank24 | none | yes | 2625 (1 / 1 / 0 / 0 / 0) |
| 244 | 244_MPL_1_051-098 | rank 25: functional analysis (rest), early no | 48 | none | 121.7 | rank25 | none |  | 2069 (0 / 0 / 0 / 0 / 0) |
| 245 | 245_MPL_1_099-150 | rank 25: functional analysis (rest), early no | 49 | 1: 106, 123, 141 | 114.7 | rank25 | none |  | 2069 (0 / 0 / 0 / 0 / 0) |
| 246 | 246_MPL_2 | rank 25: functional analysis (rest), early no | 41 | 2: 6, 27, 31 | 76.0 | rank25 | none |  | 2069 (0 / 0 / 0 / 0 / 0) |
| 247 | 247_MPL_66+68_002-032 | rank 25: functional analysis (rest), early no | 34 | 68: 23 | 37.2 | rank25 | none |  | 2074 (0 / 0 / 0 / 0 / 0) |
| 248 | 248_MPL_68_033-056+162-1+162-6 | rank 25: functional analysis (rest), early no | 35 | 68: 35, 47, 49 | 37.8 | rank25 | none |  | 2084 (0 / 0 / 0 / 0 / 0) |
| 249 | 249_MPL_129_077-115 | API-route cotes: their handwritten leaves (12 | 37 | 129: 79, 89 | 53.6 | apileaves | none | yes | 39805 (25 / 39 / 3 / 13 / 8) |
| 250 | 250_MPL_119_144-161+119_276-281 | API-route cotes: their handwritten leaves (12 | 22 | 119: 147, 154 | 32.3 | apileaves | none | yes | 39704 (25 / 38 / 3 / 13 / 9) |

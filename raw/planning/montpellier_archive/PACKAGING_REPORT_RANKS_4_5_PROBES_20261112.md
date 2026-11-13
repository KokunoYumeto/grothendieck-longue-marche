# Packaging report: ranks 4 and 5 and the ten probes (packages 34-54)

Claude Opus 5.5 (effort high), 12 Nov 2026, finished 21:12 UTC (clock checked). Order as in the war game (round 1
§2.3 stages 2-4; round 2 "Next, in order" item 2 and §1.4): rank 4, then rank 5 with 153 and 155, then the ten
probes. 21 packages, 1070 scans kept, 1553.9 MB in all. Nothing was sent; packages 31-33, packages_done\ and
returns\ were not touched; PRO_QUEUE.md and the RUNBOOK were not edited.

## Packages

All checks pass for all 21 (build log with the per-package check fields:
`packages_work\BUILD_LOG_RANKS_4_5_PROBES_20261112.json`): both zips pass `testzip`; the scans zip holds 3 images
per kept scan; kept = planned range minus the blank scans the tool lists in the prompt (ranges verified contiguous,
no overlap); the context zip is not empty and has its README.md; the folder holds exactly PROMPT.md, the scans zip
and the context zip. The tool's manifest and the prompt as built (before the questions paragraph) are in
`packages_work\<package name without number>\` (MANIFEST.json, PROMPT_as_built_20261112.md).

| Package | Cotes and scans | Kept | Blank (left out) | Scans MB | Context MB | Context contents | Questions added | Checks |
|---|---|---:|---|---:|---:|---|---|---|
| 34_MPL_144_001-061 | 144 scans 1-61 (59 kept) | 59 | 144:12, 144:41 | 78.3 | 1.97 | Longue Marche context (build_lm_context.py: our text of 140-1 to 140-4, all 1,588 scans second-passed, its notes, table of contents, global pass, overview, SECTIONS_STATE) + final research notes of the 9 returned packages of 147 (3), 149 (2), 146 (2), 142 (2) | rank 4: H1 (M(0,5) as an equation, date); which Γ(g,ν) (F13); filling map and (f) of §32; continuation of 149 §4 after ms. p. 67 (D_J, tubulure, maquette); inertia computation of 149 scan 78 | all pass |
| 35_MPL_144_062-121 | 144 scans 62-121 (59 kept) | 59 | 144:102 | 71.3 | 1.97 | Longue Marche context (build_lm_context.py: our text of 140-1 to 140-4, all 1,588 scans second-passed, its notes, table of contents, global pass, overview, SECTIONS_STATE) + final research notes of the 9 returned packages of 147 (3), 149 (2), 146 (2), 142 (2) | rank 4: H1 (M(0,5) as an equation, date); which Γ(g,ν) (F13); filling map and (f) of §32; continuation of 149 §4 after ms. p. 67 (D_J, tubulure, maquette); inertia computation of 149 scan 78 | all pass |
| 36_MPL_144_122-184 | 144 scans 122-184 (58 kept) | 58 | 144:125, 144:128, 144:133, 144:172, 144:179 | 77.4 | 1.97 | Longue Marche context (build_lm_context.py: our text of 140-1 to 140-4, all 1,588 scans second-passed, its notes, table of contents, global pass, overview, SECTIONS_STATE) + final research notes of the 9 returned packages of 147 (3), 149 (2), 146 (2), 142 (2) | rank 4: H1 (M(0,5) as an equation, date); which Γ(g,ν) (F13); filling map and (f) of §32; continuation of 149 §4 after ms. p. 67 (D_J, tubulure, maquette); inertia computation of 149 scan 78 | all pass |
| 37_MPL_148_001-053 | 148 scans 1-53 (53 kept) | 53 | none | 99.4 | 1.97 | Longue Marche context (build_lm_context.py: our text of 140-1 to 140-4, all 1,588 scans second-passed, its notes, table of contents, global pass, overview, SECTIONS_STATE) + final research notes of the 9 returned packages of 147 (3), 149 (2), 146 (2), 142 (2) | rank 4: H1 (M(0,5) as an equation, date); which Γ(g,ν) (F13); filling map and (f) of §32; continuation of 149 §4 after ms. p. 67 (D_J, tubulure, maquette); inertia computation of 149 scan 78 | all pass |
| 38_MPL_148_054-072+143 | 148 scans 54-72 (19 kept); 143 scans 1-34 (34 kept) | 53 | none | 66.1 | 1.97 | Longue Marche context (build_lm_context.py: our text of 140-1 to 140-4, all 1,588 scans second-passed, its notes, table of contents, global pass, overview, SECTIONS_STATE) + final research notes of the 9 returned packages of 147 (3), 149 (2), 146 (2), 142 (2) | rank 4: H1 (M(0,5) as an equation, date); which Γ(g,ν) (F13); filling map and (f) of §32; continuation of 149 §4 after ms. p. 67 (D_J, tubulure, maquette); inertia computation of 149 scan 78 | all pass |
| 39_MPL_145+141 | 145 scans 1-38 (38 kept); 141 scans 1-16 (16 kept) | 54 | none | 52.8 | 1.97 | Longue Marche context (build_lm_context.py: our text of 140-1 to 140-4, all 1,588 scans second-passed, its notes, table of contents, global pass, overview, SECTIONS_STATE) + final research notes of the 9 returned packages of 147 (3), 149 (2), 146 (2), 142 (2) | rank 4: H1 (M(0,5) as an equation, date); which Γ(g,ν) (F13); filling map and (f) of §32; continuation of 149 §4 after ms. p. 67 (D_J, tubulure, maquette); inertia computation of 149 scan 78 | all pass |
| 40_MPL_150_001-061 | 150 scans 1-61 (59 kept) | 59 | 150:6, 150:11 | 91.4 | 0.15 | returns MPL_147_138-190 and MPL_149_091-136 (transcription + notes; README points to 149 scans 128-136) + STATEMENTS_WITH_STATUS.md (STRATA C.1-C.8, F.1-F.13; BISITE D.1-D.13; RESIDUE G.1-G.5, H.1-H.8; all labelled as the returns' claims) | rank 5: tubulure/ombre; Remords resolved in Dec. 1981?; 120-121 axioms vs o-minimal; comparison vs Shiota | all pass |
| 41_MPL_150_062-099+151_001-023 | 150 scans 62-99 (38 kept); 151 scans 1-23 (21 kept) | 59 | 151:10, 151:16 | 69.9 | 0.15 | returns MPL_147_138-190 and MPL_149_091-136 (transcription + notes; README points to 149 scans 128-136) + STATEMENTS_WITH_STATUS.md (STRATA C.1-C.8, F.1-F.13; BISITE D.1-D.13; RESIDUE G.1-G.5, H.1-H.8; all labelled as the returns' claims) | rank 5: tubulure/ombre; Remords resolved in Dec. 1981?; 120-121 axioms vs o-minimal; comparison vs Shiota | all pass |
| 42_MPL_151_024-075+152 | 151 scans 24-75 (51 kept); 152 scans 1-13 (13 kept) | 64 | 151:26 | 104.2 | 0.15 | returns MPL_147_138-190 and MPL_149_091-136 (transcription + notes; README points to 149 scans 128-136) + STATEMENTS_WITH_STATUS.md (STRATA C.1-C.8, F.1-F.13; BISITE D.1-D.13; RESIDUE G.1-G.5, H.1-H.8; all labelled as the returns' claims) | rank 5: tubulure/ombre; Remords resolved in Dec. 1981?; 120-121 axioms vs o-minimal; comparison vs Shiota | all pass |
| 43_MPL_120+121_001-034 | 120 scans 1-25 (25 kept); 121 scans 1-34 (31 kept) | 56 | 121:3, 121:25, 121:29 | 68.2 | 0.15 | returns MPL_147_138-190 and MPL_149_091-136 (transcription + notes; README points to 149 scans 128-136) + STATEMENTS_WITH_STATUS.md (STRATA C.1-C.8, F.1-F.13; BISITE D.1-D.13; RESIDUE G.1-G.5, H.1-H.8; all labelled as the returns' claims) | rank 5: tubulure/ombre; Remords resolved in Dec. 1981?; 120-121 axioms vs o-minimal; comparison vs Shiota | all pass |
| 44_MPL_121_035-073+153+155 | 121 scans 35-73 (34 kept); 153 scans 1-11 (11 kept); 155 scans 1-11 (11 kept) | 56 | 121:38, 121:40, 121:53, 121:64, 121:69 | 101.5 | 0.15 | returns MPL_147_138-190 and MPL_149_091-136 (transcription + notes; README points to 149 scans 128-136) + STATEMENTS_WITH_STATUS.md (STRATA C.1-C.8, F.1-F.13; BISITE D.1-D.13; RESIDUE G.1-G.5, H.1-H.8; all labelled as the returns' claims) | rank 5: tubulure/ombre; Remords resolved in Dec. 1981?; 120-121 axioms vs o-minimal; comparison vs Shiota; separate headings for 153 and 155 | all pass |
| 45_MPL_156-1+156-2 | 156-1 scans 1-27 (27 kept); 156-2 scans 1-19 (19 kept) | 46 | none | 64.9 | 0.0 | README with the war game's guess for this cote | probe: the war game's guess (cote 156) | all pass |
| 46_MPL_136_002-046 | 136 scans 2-46 (44 kept) | 44 | 136:19 | 53.7 | 0.0 | README with the war game's guess for this cote | probe: the war game's guess (cote 136) | all pass |
| 47_MPL_93_002-046 | 93 scans 2-46 (42 kept) | 42 | 93:2, 93:26, 93:35 | 56.6 | 0.0 | README with the war game's guess for this cote | probe: the war game's guess (cote 93); typed sheets marked in sheet_kind (`reused_typed` / `typed`) | all pass |
| 48_MPL_79_001-045 | 79 scans 1-45 (45 kept) | 45 | none | 53.5 | 0.0 | README with the war game's guess for this cote + B5 / S10 and bi-icosahedron-through-M(0,5) paragraphs | probe: the war game's guess (cote 79) | all pass |
| 49_MPL_83_001-045 | 83 scans 1-45 (43 kept) | 43 | 83:2, 83:18 | 59.0 | 0.0 | README with the war game's guess for this cote + B5 / S10 and bi-icosahedron-through-M(0,5) paragraphs | probe: the war game's guess (cote 83) | all pass |
| 50_MPL_154_001-045 | 154 scans 1-45 (44 kept) | 44 | 154:11 | 158.7 | 0.0 | README with the war game's guess for this cote | probe: the war game's guess (cote 154) | all pass |
| 51_MPL_138_001-045 | 138 scans 1-45 (44 kept) | 44 | 138:24 | 48.4 | 0.0 | README with the war game's guess for this cote | probe: the war game's guess (cote 138) | all pass |
| 52_MPL_159 | 159 scans 1-34 (32 kept) | 32 | 159:14, 159:24 | 39.9 | 0.0 | README with the war game's guess for this cote | probe: the war game's guess (cote 159) | all pass |
| 53_MPL_43_001-045 | 43 scans 1-45 (42 kept) | 42 | 43:14, 43:39, 43:44 | 53.5 | 0.0 | README with the war game's guess for this cote | probe: the war game's guess (cote 43) | all pass |
| 54_MPL_49+50+51+52 | 49 scans 1-10 (10 kept); 50 scans 1-11 (11 kept); 51 scans 1-23 (23 kept); 52 scans 1-14 (14 kept) | 58 | none | 72.6 | 0.0 | README with the war game's guess for this cote | probe: the war game's guess (cote 49-52) | all pass |

Sizes: rank 4 and rank 5 packages are 53-64 scans (45-70 asked). The probes are the first 45 scans planned, fewer
kept where scans were blank; 159 whole is 32 kept; 156-1 + 156-2 whole is 46 (the war game's 44 counts from
MANIFEST.csv: every PDF has one page more than its MANIFEST count, here and in all 26 cotes checked).

How the long groups were split (near-equal, one stream each, order kept):
- 144 (184 scans, 8 blank): 1-61, 62-121, 122-184 = 59, 59, 58 kept.
- 148 + 143 + 145 + 141 (72 + 34 + 38 + 16 = 160, no blanks): 148 alone would be 72 (over 70), and 143 + 145 + 141
  together 88. Split as one stream into 53, 53, 54: 148 scans 1-53; 148 scans 54-72 with 143; 145 with 141.
- Rank 5 (294 kept) as one stream in five packages of 56-64: 150 1-61; 150 62-99 + 151 1-23; 151 24-75 + 152;
  120 + 121 1-34; 121 35-73 + 153 + 155.

## Context zips (opened only after the freeze, as the template says)

Sources: `packages_work\context_ranks4_5_probes_20261112\` (rank4, rank5, probe_*), each with README.md and
SUMMARY.txt (the first line goes into the prompt).
- **Rank 4 (1.97 MB zipped):** `build_lm_context.py` output (our text of 140-1 to 140-4, 1,588 scans, all
  second-passed; its notes; table of contents; global pass; overview; SECTIONS_STATE.md) plus the final research
  notes of the nine returned packages of 147 (003-047, 048-137, 138-190), 149 (001-090, 091-136), 146 (001-099,
  100-134) and 142 (001-093, 094-122), from `returns\*_unzipped\`; no checkpoint folders.
- **Rank 5 (0.15 MB):** the returns MPL_147_138-190 and MPL_149_091-136 (transcription and notes each; the README
  points to 149 scans 128-136) and `STATEMENTS_WITH_STATUS.md`: STRATA C.1-C.8 and F.1-F.13, BISITE D.1-D.13,
  RESIDUE G.1-G.5 and H.1-H.8, statements in full from the returns' results registers
  (`derivateurs_companion_20261109\pro_returns_20261110\...\*_results.csv`). Status: every row is labelled "claim
  (return: Proved / Known / Refuted / Open)". The verdict of the 10 Nov effort-medium reviews
  (`pro_reviews_20261110\5_STRATA\REVIEW_author.md`, `7_BISITE\REVIEW_author.md`) is given beside it, marked as a
  lower-effort reading that does not make a row proved.
- **Probes (2-4 KB):** a README per cote with the war game's guess (round 1 stage 4, S11, S14, S20, the reader
  carry-questions; round 2 §1.1 and §1.4 row 4 for 43 and 49-52). For 79 and 83 also bridge B5, S10 and the
  bi-icosahedron through M(0,5) (round 1 Book IV prediction, lookup 13).

## Questions for the notes

One paragraph per package, after the attachments paragraph; it says the questions are for the notes, after the
freeze, and never change the transcription.
- Rank 4: H1 (M(0,5) condition as an equation, and its date); which Γ(g,ν) each page means (F13); the filling map
  (LM3b B.4-B.6, described in words) and (f) of §32 of the Longue Marche (present in the context, 140-2 notes); does
  148 or 144 continue 149 §4 after ms. p. 67 (D_J, "tubulure", "maquette"); the inertia computation of 149 scan 78.
- Rank 5: "tubulure" and "ombre"; the Remords resolved by him in December 1981; 120-121 axioms against o-minimal
  structures; his comparison against Shiota's theorem; in package 44 only (the one holding them), notes on 153 and
  155 under headings of their own.
- Probes: the guess for the cote. Package 47 (cote 93) also has a paragraph asking for every typed sheet to be marked
  in the inventory's `sheet_kind`: `reused_typed` for another text, `typed` for a typescript of the folder's own text
  (a value the template does not have). Package 54 carries one question marked as ours, not the war game's: whether
  51 and 52 hold the proof for abelian varieties that 149 scan 103 recalls ("il y a belle lurette").

## The template change

`ARCHIVE_PROMPT_TEMPLATE.md`, backed up first as `ARCHIVE_PROMPT_TEMPLATE_before_standing_questions_20261112.md`.
Added in item 4 (notes) only: the two standing questions of round 2 §1.8 (which steps the manuscript marks as
unverified; which title sheets and page counts it carries), and the note kinds "self-flagged" and "withdrawn in the
same text" in the list of kinds. Nothing else changed (checked by diff). All 21 prompts carry it.

## Not found, and problems met

- **No review at effort max** exists for STRATA, BISITE or RESIDUE (`pro_reviews_max_20261112\5_STRATA`,
  `7_BISITE`, `8_RESIDUE` are empty). RESIDUE G and H have no review of any kind (the 10 Nov RESIDUE folder holds only
  check scripts for part E). So no row is "proved per the reviews"; all are claims.
- **`build_package_multi.py` no longer matches the template**: it expects the inventory string ``(columns `scan,element,kind,``,
  which the sheet-kind repair of 12 Nov changed to ``scan,sheet_kind,element,kind,``. The first build attempt of 34
  stopped there (its partial scans zip was removed). The builds ran the tool unchanged through a wrapper that maps
  that one substitution to the new string (scratchpad `multi_wrap.py`); the tools folder was outside my write scope,
  so the tool itself still needs the fix.
- The single-file packages (34-37, 40, 46-53) were built with the multi-cote tool so that the scan ranges stay exact;
  its wording for one file ("from 1 files ..., in this order", "cotes 144") was corrected in the prompt by script.
- Package 50 (cote 154, listing paper) is 158.7 MB for 44 scans, the largest so far (package 33 was 127 MB).
- The first scan of cote 93 and the second of 83 are blank; the probes of 93 and 43 keep 42 scans.

## Ready-made PRO_QUEUE rows (for the main session to paste; renumber the # column to follow the queue)

| # | Prompt folder | Series | What it is | Upload |
|---|---|---|---|---|
| 34 | 34_MPL_144_001-061 | archive | 59 scans (144 scans 1-61 (59 kept)); Book III, rank 4; context zip opened after the freeze | PROMPT.md + 2 zips |
| 35 | 35_MPL_144_062-121 | archive | 59 scans (144 scans 62-121 (59 kept)); Book III, rank 4; context zip opened after the freeze | PROMPT.md + 2 zips |
| 36 | 36_MPL_144_122-184 | archive | 58 scans (144 scans 122-184 (58 kept)); Book III, rank 4; context zip opened after the freeze | PROMPT.md + 2 zips |
| 37 | 37_MPL_148_001-053 | archive | 53 scans (148 scans 1-53 (53 kept)); Book III, rank 4; context zip opened after the freeze | PROMPT.md + 2 zips |
| 38 | 38_MPL_148_054-072+143 | archive | 53 scans (148 scans 54-72 (19 kept); 143 scans 1-34 (34 kept)); Book III, rank 4; context zip opened after the freeze | PROMPT.md + 2 zips |
| 39 | 39_MPL_145+141 | archive | 54 scans (145 scans 1-38 (38 kept); 141 scans 1-16 (16 kept)); Book III, rank 4; context zip opened after the freeze | PROMPT.md + 2 zips |
| 40 | 40_MPL_150_001-061 | archive | 59 scans (150 scans 1-61 (59 kept)); Book V, rank 5; context zip opened after the freeze | PROMPT.md + 2 zips |
| 41 | 41_MPL_150_062-099+151_001-023 | archive | 59 scans (150 scans 62-99 (38 kept); 151 scans 1-23 (21 kept)); Book V, rank 5; context zip opened after the freeze | PROMPT.md + 2 zips |
| 42 | 42_MPL_151_024-075+152 | archive | 64 scans (151 scans 24-75 (51 kept); 152 scans 1-13 (13 kept)); Book V, rank 5; context zip opened after the freeze | PROMPT.md + 2 zips |
| 43 | 43_MPL_120+121_001-034 | archive | 56 scans (120 scans 1-25 (25 kept); 121 scans 1-34 (31 kept)); Book V, rank 5; context zip opened after the freeze | PROMPT.md + 2 zips |
| 44 | 44_MPL_121_035-073+153+155 | archive | 56 scans (121 scans 35-73 (34 kept); 153 scans 1-11 (11 kept); 155 scans 1-11 (11 kept)); Book V, rank 5; context zip opened after the freeze | PROMPT.md + 2 zips |
| 45 | 45_MPL_156-1+156-2 | archive | 46 scans (156-1 scans 1-27 (27 kept); 156-2 scans 1-19 (19 kept)); probe; context zip opened after the freeze | PROMPT.md + 2 zips |
| 46 | 46_MPL_136_002-046 | archive | 44 scans (136 scans 2-46 (44 kept)); probe; context zip opened after the freeze | PROMPT.md + 2 zips |
| 47 | 47_MPL_93_002-046 | archive | 42 scans (93 scans 2-46 (42 kept)); probe; context zip opened after the freeze | PROMPT.md + 2 zips |
| 48 | 48_MPL_79_001-045 | archive | 45 scans (79 scans 1-45 (45 kept)); probe; context zip opened after the freeze | PROMPT.md + 2 zips |
| 49 | 49_MPL_83_001-045 | archive | 43 scans (83 scans 1-45 (43 kept)); probe; context zip opened after the freeze | PROMPT.md + 2 zips |
| 50 | 50_MPL_154_001-045 | archive | 44 scans (154 scans 1-45 (44 kept)); probe; context zip opened after the freeze | PROMPT.md + 2 zips |
| 51 | 51_MPL_138_001-045 | archive | 44 scans (138 scans 1-45 (44 kept)); probe; context zip opened after the freeze | PROMPT.md + 2 zips |
| 52 | 52_MPL_159 | archive | 32 scans (159 scans 1-34 (32 kept)); probe; context zip opened after the freeze | PROMPT.md + 2 zips |
| 53 | 53_MPL_43_001-045 | archive | 42 scans (43 scans 1-45 (42 kept)); probe; context zip opened after the freeze | PROMPT.md + 2 zips |
| 54 | 54_MPL_49+50+51+52 | archive | 58 scans (49 scans 1-10 (10 kept); 50 scans 1-11 (11 kept); 51 scans 1-23 (23 kept); 52 scans 1-14 (14 kept)); probe; context zip opened after the freeze | PROMPT.md + 2 zips |

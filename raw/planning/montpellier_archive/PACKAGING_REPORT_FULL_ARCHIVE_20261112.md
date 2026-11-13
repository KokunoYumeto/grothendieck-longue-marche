# Packaging report: the full archive (packages 55-178)

Claude Opus 5.5 (effort high), 12 Nov 2026, report written 22:26 UTC (clock checked). Every cote of the Montpellier archive still to transcribe that does not go over the API, packaged for GPT-6 Astra (ChatGPT Pro mode) in order W after the probes. **Preliminary packages**: the transcription part is final, the context zips may be upgraded before sending (each README says so). Nothing was sent; packages 31-54, packages_done\ and returns\ were not touched; PRO_QUEUE.md and the RUNBOOK were not edited; no git.

**124 packages, 8410 scans kept, 12.70 GB** (scans and context zips). All checks pass: yes.
 C: free after the build: 58.0 GB.

## Method

- Plan: `packages_work\full_archive_20261112\plan.py` → `PLAN.json` (groups in order W, packing by dynamic programming in `pack_dp.py`: fewest packages under the cap, then as even as possible; a cote no longer than the cap is never split; no piece of a long cote under 15 scans). Caps: 70 for keystone chapters (Books III and V, the dossier, II.9), 90 for calculation folders and drafts of printed texts. Coverage was checked by script: every Pro-route cote, minus what is packaged or returned, is covered exactly once.
- Build: `build_full.py` (one package at a time, resumable; progress in `FULL_ARCHIVE_PROGRESS.txt`, entries with every check field in `BUILD_LOG_FULL_ARCHIVE_20261112.json`), calling `build_package_multi.py` through `run_multi.py` (which only lets one package hold two parts of one file: 119). Contexts: `contexts.py` → `packages_work\context_full_archive_20261112\<package>\` (README.md, SUMMARY.txt, files).
- **The tool fix.** `build_package_multi.py` now substitutes the template's current inventory line (``scan,sheet_kind,element,kind,`` → ``cote,scan,sheet_kind,element,kind,``); one line changed, backup `build_package_multi_before_sheetkind_fix_20261112.py`. The earlier wrapper is no longer needed. The template was used as it stands.
- **PDF page 1 left out.** PDF page 1 of every file is the IMAG cover sheet of the digitization (the returned package of 16, 47, 54, 44 transcribed it as a drawing of the institute's logo); site page n is PDF page n+1. Whole cotes are packaged from PDF page 2, as the pilot (MPL_1_002-050) and the probes of 136 and 93 were. Packages 31-54 include it where they start at scan 1.
- Prompts: the template as built by the tool; for one-file packages the wording was corrected by script as in 34-54 ("cote", "from 1 file"); a questions paragraph (the war game's questions, in the form of 34-54) where the war game has one; a "Typed sheets in the inventory" paragraph (as in package 47) for packages holding cotes with typescripts or offprints (10, 12, 15, 21, 23, 29, 37, 63, 93, 119, 129, 161-5, 162-5). The prompt as built is kept in `packages_work\<package name>\PROMPT_as_built_20261112.md` with the tool's MANIFEST.json.
- Checks per package: both zips pass `testzip`; the scans zip holds 3 images per kept scan; kept + blanks = the planned range exactly; the context zip is not empty and has README.md; the folder holds exactly PROMPT.md, the scans zip and the context zip; the prompt's counts equal the kept scans; no placeholder left.

## Packages

| # | Package | Scans planned | Kept | Blank (left out) | Scans MB | Context MB | Context | Questions | Checks |
|---|---|---|---:|---|---:|---:|---|---|---|
| 55 | 55_MPL_21+22+23_002-026 | 21 scans 2-29; 22 scans 2-30; 23 scans 2-26 (82) | 81 | 21: 3 | 126.7 | 0.22 | README + our French EGA: plan of the treatise (EGA I intro), chapter 0, contents of EGA II and IV | yes; typed-sheets paragraph | all pass |
| 56 | 56_MPL_23_027-099+26 | 23 scans 27-99; 26 scans 2-11 (83) | 76 | 23: 42, 43, 48, 69, 72, 86, 95 | 112.2 | 0.22 | README + our French EGA: plan of the treatise (EGA I intro), chapter 0, contents of EGA II and IV | yes; typed-sheets paragraph | all pass |
| 57 | 57_MPL_35+48+102+127+128 | 35 scans 2-6; 48 scans 2-6; 102 scans 2-14; 127 scans 2-24; 128 scans 2-32 (77) | 75 | 102: 8; 128: 31 | 97.0 | 0.22 | README + our French EGA: plan of the treatise (EGA I intro), chapter 0, contents of EGA II and IV | yes | all pass |
| 58 | 58_MPL_134-1+134-2_146-185 | 134-1 scans 2-7; 134-2 scans 146-185 (46) | 45 | 134-1: 3 | 67.2 | 2.55 | README + NEW_RESULTS.md + DOSSIER_STATEMENTS_WITH_STATUS.md (STRATA D, G.2; PATHS; BISITE A-C, E-G; RESIDUE B-D, F, I, J; all claims) + our Dérivateurs companion + Pursuing Stacks contents and ch. VI-VII (arXiv, CC0) | yes | all pass |
| 59 | 59_MPL_134-8_043-087+158_002-023 | 134-8 scans 43-87; 158 scans 2-23 (67) | 64 | 134-8: 60; 158: 6, 17 | 137.7 | 2.55 | README + NEW_RESULTS.md + DOSSIER_STATEMENTS_WITH_STATUS.md (STRATA D, G.2; PATHS; BISITE A-C, E-G; RESIDUE B-D, F, I, J; all claims) + our Dérivateurs companion + Pursuing Stacks contents and ch. VI-VII (arXiv, CC0) | yes | all pass |
| 60 | 60_MPL_158_024-086+108 | 158 scans 24-86; 108 scans 2-6 (68) | 65 | 158: 44, 55, 60 | 75.4 | 2.55 | README + NEW_RESULTS.md + DOSSIER_STATEMENTS_WITH_STATUS.md (STRATA D, G.2; PATHS; BISITE A-C, E-G; RESIDUE B-D, F, I, J; all claims) + our Dérivateurs companion + Pursuing Stacks contents and ch. VI-VII (arXiv, CC0) | yes | all pass |
| 61 | 61_MPL_112+113+114+115+116+117 | 112 scans 2-5; 113 scans 2-13; 114 scans 2-6; 115 scans 2-15; 116 scans 2-11; 117 scans 2-26 (70) | 69 | 116: 9 | 158.0 | 2.55 | README + NEW_RESULTS.md + DOSSIER_STATEMENTS_WITH_STATUS.md (STRATA D, G.2; PATHS; BISITE A-C, E-G; RESIDUE B-D, F, I, J; all claims) + our Dérivateurs companion + Pursuing Stacks contents and ch. VI-VII (arXiv, CC0) | yes | all pass |
| 62 | 62_MPL_118+103 | 118 scans 2-41; 103 scans 2-18 (57) | 54 | 118: 13, 38; 103: 8 | 94.4 | 2.55 | README + NEW_RESULTS.md + DOSSIER_STATEMENTS_WITH_STATUS.md (STRATA D, G.2; PATHS; BISITE A-C, E-G; RESIDUE B-D, F, I, J; all claims) + our Dérivateurs companion + Pursuing Stacks contents and ch. VI-VII (arXiv, CC0) | yes | all pass |
| 63 | 63_MPL_104+105 | 104 scans 2-17; 105 scans 2-53 (68) | 64 | 105: 9, 24, 29, 42 | 181.4 | 2.55 | README + NEW_RESULTS.md + DOSSIER_STATEMENTS_WITH_STATUS.md (STRATA D, G.2; PATHS; BISITE A-C, E-G; RESIDUE B-D, F, I, J; all claims) + our Dérivateurs companion + Pursuing Stacks contents and ch. VI-VII (arXiv, CC0) | yes | all pass |
| 64 | 64_MPL_106+107 | 106 scans 2-17; 107 scans 2-26 (41) | 41 | none | 158.1 | 2.55 | README + NEW_RESULTS.md + DOSSIER_STATEMENTS_WITH_STATUS.md (STRATA D, G.2; PATHS; BISITE A-C, E-G; RESIDUE B-D, F, I, J; all claims) + our Dérivateurs companion + Pursuing Stacks contents and ch. VI-VII (arXiv, CC0) | yes | all pass |
| 65 | 65_MPL_109+111+162-5_019-032 | 109 scans 2-38; 111 scans 2-17; 162-5 scans 19-32 (67) | 61 | 109: 12, 16, 20; 162-5: 19, 21, 32 | 103.4 | 2.55 | README + NEW_RESULTS.md + DOSSIER_STATEMENTS_WITH_STATUS.md (STRATA D, G.2; PATHS; BISITE A-C, E-G; RESIDUE B-D, F, I, J; all claims) + our Dérivateurs companion + Pursuing Stacks contents and ch. VI-VII (arXiv, CC0) | yes; typed-sheets paragraph | all pass |
| 66 | 66_MPL_135 | 135 scans 2-59 (58) | 51 | 135: 2, 7, 25, 31, 35, 39, 46 | 78.4 | 2.55 | README + NEW_RESULTS.md + DOSSIER_STATEMENTS_WITH_STATUS.md (STRATA D, G.2; PATHS; BISITE A-C, E-G; RESIDUE B-D, F, I, J; all claims) + our Dérivateurs companion + Pursuing Stacks contents and ch. VI-VII (arXiv, CC0) | yes | all pass |
| 67 | 67_MPL_137_002-070 | 137 scans 2-70 (69) | 68 | 137: 6 | 84.5 | 0.14 | README (S11, B7) + Pursuing Stacks contents and ch. VI-VII (arXiv, CC0) | yes | all pass |
| 68 | 68_MPL_137_071-086+133 | 137 scans 71-86; 133 scans 2-54 (69) | 66 | 133: 5, 10, 41 | 83.8 | 0.14 | README (S11, B7) + Pursuing Stacks contents and ch. VI-VII (arXiv, CC0) | yes | all pass |
| 69 | 69_MPL_14_002-066 | 14 scans 2-66 (65) | 62 | 14: 18, 23, 43 | 91.6 | 6.03 | README (stage 7 table, round 2 §2.4) + first Book II return 16+47+54+44 (claims) + Oda 1969 | yes | all pass |
| 70 | 70_MPL_14_067-132 | 14 scans 67-132 (66) | 60 | 14: 72, 105, 110, 119, 125, 130 | 84.7 | 6.03 | README (stage 7 table, round 2 §2.4) + first Book II return 16+47+54+44 (claims) + Oda 1969 | yes | all pass |
| 71 | 71_MPL_13+12_002-034 | 13 scans 2-52; 12 scans 2-34 (84) | 76 | 13: 3, 13, 22, 26, 33, 36, 45; 12: 20 | 103.5 | 6.03 | README (stage 7 table, round 2 §2.4) + first Book II return 16+47+54+44 (claims) + Oda 1969 | yes; typed-sheets paragraph | all pass |
| 72 | 72_MPL_12_035-118 | 12 scans 35-118 (84) | 82 | 12: 103, 110 | 132.0 | 6.03 | README (stage 7 table, round 2 §2.4) + first Book II return 16+47+54+44 (claims) + Oda 1969 | yes; typed-sheets paragraph | all pass |
| 73 | 73_MPL_12_119-168+15_002-035 | 12 scans 119-168; 15 scans 2-35 (84) | 81 | 12: 124; 15: 15, 25 | 112.7 | 6.03 | README (stage 7 table, round 2 §2.4) + first Book II return 16+47+54+44 (claims) + Oda 1969 | yes; typed-sheets paragraph | all pass |
| 74 | 74_MPL_15_036-119 | 15 scans 36-119 (84) | 79 | 15: 58, 65, 80, 83, 116 | 117.7 | 6.03 | README (stage 7 table, round 2 §2.4) + first Book II return 16+47+54+44 (claims) + Oda 1969 | yes; typed-sheets paragraph | all pass |
| 75 | 75_MPL_15_120-204 | 15 scans 120-204 (85) | 76 | 15: 127, 134, 140, 146, 153, 156, 158, 167, 169 | 107.4 | 6.03 | README (stage 7 table, round 2 §2.4) + first Book II return 16+47+54+44 (claims) + Oda 1969 | yes; typed-sheets paragraph | all pass |
| 76 | 76_MPL_15_205-228+18 | 15 scans 205-228; 18 scans 2-62 (85) | 84 | 18: 8 | 123.3 | 6.03 | README (stage 7 table, round 2 §2.4) + first Book II return 16+47+54+44 (claims) + Oda 1969 | yes; typed-sheets paragraph | all pass |
| 77 | 77_MPL_136_047-112 | 136 scans 47-112 (66) | 64 | 136: 47, 79 | 91.1 | 0.14 | README (S11, B7) + Pursuing Stacks contents and ch. VI-VII (arXiv, CC0) | yes | all pass |
| 78 | 78_MPL_136_113-178 | 136 scans 113-178 (66) | 64 | 136: 122, 161 | 96.3 | 0.14 | README (S11, B7) + Pursuing Stacks contents and ch. VI-VII (arXiv, CC0) | yes | all pass |
| 79 | 79_MPL_136_179-244 | 136 scans 179-244 (66) | 64 | 136: 214, 243 | 95.8 | 0.14 | README (S11, B7) + Pursuing Stacks contents and ch. VI-VII (arXiv, CC0) | yes | all pass |
| 80 | 80_MPL_136_245-310 | 136 scans 245-310 (66) | 66 | none | 98.5 | 0.14 | README (S11, B7) + Pursuing Stacks contents and ch. VI-VII (arXiv, CC0) | yes | all pass |
| 81 | 81_MPL_136_311-376 | 136 scans 311-376 (66) | 61 | 136: 319, 344, 347, 354, 356 | 104.1 | 0.14 | README (S11, B7) + Pursuing Stacks contents and ch. VI-VII (arXiv, CC0) | yes | all pass |
| 82 | 82_MPL_138_046-089 | 138 scans 46-89 (44) | 42 | 138: 79, 88 | 48.4 | 2.03 | README (B5, B6, Book IV literature) + Longue Marche text/notes, returned notes of 147/149/146/142 + LM2 congruence rows (claims) + Esquisse (API transcription) | yes | all pass |
| 83 | 83_MPL_138_090-133 | 138 scans 90-133 (44) | 43 | 138: 92 | 48.0 | 2.03 | README (B5, B6, Book IV literature) + Longue Marche text/notes, returned notes of 147/149/146/142 + LM2 congruence rows (claims) + Esquisse (API transcription) | yes | all pass |
| 84 | 84_MPL_76 | 76 scans 2-63 (62) | 55 | 76: 2, 11, 15, 35, 45, 47, 49 | 73.4 | 2.03 | README (B5, B6, Book IV literature) + Longue Marche text/notes, returned notes of 147/149/146/142 + LM2 congruence rows (claims) + Esquisse (API transcription) | yes | all pass |
| 85 | 85_MPL_88+70_002-056 | 88 scans 2-16; 70 scans 2-56 (70) | 66 | 88: 10; 70: 28, 38, 49 | 87.6 | 2.03 | README (B5, B6, Book IV literature) + Longue Marche text/notes, returned notes of 147/149/146/142 + LM2 congruence rows (claims) + Esquisse (API transcription) | yes | all pass |
| 86 | 86_MPL_70_057-126 | 70 scans 57-126 (70) | 65 | 70: 61, 64, 73, 113, 126 | 81.9 | 2.03 | README (B5, B6, Book IV literature) + Longue Marche text/notes, returned notes of 147/149/146/142 + LM2 congruence rows (claims) + Esquisse (API transcription) | yes | all pass |
| 87 | 87_MPL_75+161-6 | 75 scans 2-33; 161-6 scans 2-34 (65) | 59 | 75: 29; 161-6: 3, 12, 21, 24, 32 | 78.7 | 2.03 | README (B5, B6, Book IV literature) + Longue Marche text/notes, returned notes of 147/149/146/142 + LM2 congruence rows (claims) + Esquisse (API transcription) | yes | all pass |
| 88 | 88_MPL_79_046-129 | 79 scans 46-129 (84) | 84 | none | 102.4 | 2.03 | README (B5, B6, Book IV literature) + Longue Marche text/notes, returned notes of 147/149/146/142 + LM2 congruence rows (claims) + Esquisse (API transcription) | yes | all pass |
| 89 | 89_MPL_79_130-213 | 79 scans 130-213 (84) | 84 | none | 107.5 | 2.03 | README (B5, B6, Book IV literature) + Longue Marche text/notes, returned notes of 147/149/146/142 + LM2 congruence rows (claims) + Esquisse (API transcription) | yes | all pass |
| 90 | 90_MPL_79_214-297 | 79 scans 214-297 (84) | 81 | 79: 272, 275, 282 | 98.5 | 2.03 | README (B5, B6, Book IV literature) + Longue Marche text/notes, returned notes of 147/149/146/142 + LM2 congruence rows (claims) + Esquisse (API transcription) | yes | all pass |
| 91 | 91_MPL_83_046-133 | 83 scans 46-133 (88) | 85 | 83: 47, 80, 101 | 122.6 | 2.03 | README (B5, B6, Book IV literature) + Longue Marche text/notes, returned notes of 147/149/146/142 + LM2 congruence rows (claims) + Esquisse (API transcription) | yes | all pass |
| 92 | 92_MPL_83_134-222 | 83 scans 134-222 (89) | 86 | 83: 149, 182, 206 | 124.5 | 2.03 | README (B5, B6, Book IV literature) + Longue Marche text/notes, returned notes of 147/149/146/142 + LM2 congruence rows (claims) + Esquisse (API transcription) | yes | all pass |
| 93 | 93_MPL_64_002-053 | 64 scans 2-53 (52) | 52 | none | 66.3 | 1.97 | README + Longue Marche text/notes, returned notes of 147/149/146/142 + LM2 congruence rows (claims) | yes | all pass |
| 94 | 94_MPL_64_054-105 | 64 scans 54-105 (52) | 52 | none | 59.1 | 1.97 | README + Longue Marche text/notes, returned notes of 147/149/146/142 + LM2 congruence rows (claims) | yes | all pass |
| 95 | 95_MPL_64_106-157 | 64 scans 106-157 (52) | 49 | 64: 122, 130, 142 | 57.7 | 1.97 | README + Longue Marche text/notes, returned notes of 147/149/146/142 + LM2 congruence rows (claims) | yes | all pass |
| 96 | 96_MPL_161-3+161-4 | 161-3 scans 2-55; 161-4 scans 2-32 (85) | 74 | 161-3: 2, 3, 14, 17, 23, 28, 30, 34; 161-4: 2, 14, 19 | 111.4 | 0.0 | README | none (no war-game question) | all pass |
| 97 | 97_MPL_156-8_002-056 | 156-8 scans 2-56 (55) | 55 | none | 76.1 | 0.05 | README (S14, B10) + Esquisse (API transcription) | yes | all pass |
| 98 | 98_MPL_156-8_057-112 | 156-8 scans 57-112 (56) | 56 | none | 68.6 | 0.05 | README (S14, B10) + Esquisse (API transcription) | yes | all pass |
| 99 | 99_MPL_156-8_113-127+156-5 | 156-8 scans 113-127; 156-5 scans 2-49 (63) | 63 | none | 85.8 | 0.05 | README (S14, B10) + Esquisse (API transcription) | yes | all pass |
| 100 | 100_MPL_156-3+156-9_002-020 | 156-3 scans 2-41; 156-9 scans 2-20 (59) | 59 | none | 86.9 | 0.05 | README (S14, B10) + Esquisse (API transcription) | yes | all pass |
| 101 | 101_MPL_156-9_021-080 | 156-9 scans 21-80 (60) | 60 | none | 73.7 | 0.05 | README (S14, B10) + Esquisse (API transcription) | yes | all pass |
| 102 | 102_MPL_156-9_081-140 | 156-9 scans 81-140 (60) | 59 | 156-9: 129 | 76.0 | 0.05 | README (S14, B10) + Esquisse (API transcription) | yes | all pass |
| 103 | 103_MPL_67_002-051 | 67 scans 2-51 (50) | 46 | 67: 15, 22, 23, 47 | 101.5 | 1.97 | README + Longue Marche text/notes, returned notes of 147/149/146/142 + LM2 congruence rows (claims) | none (no war-game question) | all pass |
| 104 | 104_MPL_67_052-101 | 67 scans 52-101 (50) | 47 | 67: 52, 83, 90 | 93.4 | 1.97 | README + Longue Marche text/notes, returned notes of 147/149/146/142 + LM2 congruence rows (claims) | none (no war-game question) | all pass |
| 105 | 105_MPL_10_002-085 | 10 scans 2-85 (84) | 80 | 10: 18, 32, 59, 85 | 125.1 | 6.03 | README + first Book II return (claims) + Oda 1969 | yes; typed-sheets paragraph | all pass |
| 106 | 106_MPL_10_086-170 | 10 scans 86-170 (85) | 79 | 10: 101, 110, 114, 138, 142, 156 | 126.3 | 6.03 | README + first Book II return (claims) + Oda 1969 | yes; typed-sheets paragraph | all pass |
| 107 | 107_MPL_10_171-198+11 | 10 scans 171-198; 11 scans 2-58 (85) | 82 | 11: 2, 33, 50 | 106.4 | 6.03 | README + first Book II return (claims) + Oda 1969 | yes; typed-sheets paragraph | all pass |
| 108 | 108_MPL_56 | 56 scans 2-39 (38) | 35 | 56: 10, 19, 34 | 51.2 | 6.03 | README + first Book II return (claims) + Oda 1969 | yes | all pass |
| 109 | 109_MPL_60 | 60 scans 2-70 (69) | 69 | none | 110.8 | 6.03 | README + first Book II return (claims) + Oda 1969 | none (no war-game question) | all pass |
| 110 | 110_MPL_69_002-083 | 69 scans 2-83 (82) | 76 | 69: 2, 41, 65, 66, 73, 77 | 98.0 | 0.0 | README (recompute tables; B5, B12) + LM2 congruence rows (claims) | yes | all pass |
| 111 | 111_MPL_69_084-120+72_002-046 | 69 scans 84-120; 72 scans 2-46 (82) | 75 | 69: 89, 94, 95, 100, 105, 107; 72: 22 | 88.0 | 0.0 | README (recompute tables; B5, B12) + LM2 congruence rows (claims) | yes | all pass |
| 112 | 112_MPL_72_047-113+74_002-016 | 72 scans 47-113; 74 scans 2-16 (82) | 81 | 74: 8 | 93.4 | 0.0 | README (recompute tables; B5, B12) + LM2 congruence rows (claims) | yes | all pass |
| 113 | 113_MPL_74_017-099 | 74 scans 17-99 (83) | 75 | 74: 18, 20, 25, 32, 41, 46, 72, 92 | 99.4 | 0.0 | README (recompute tables; B5, B12) + LM2 congruence rows (claims) | yes | all pass |
| 114 | 114_MPL_74_100-136+85_002-047 | 74 scans 100-136; 85 scans 2-47 (83) | 82 | 74: 127 | 107.3 | 0.0 | README (recompute tables; B5, B12) + LM2 congruence rows (claims) | yes | all pass |
| 115 | 115_MPL_85_048-098+86 | 85 scans 48-98; 86 scans 2-33 (83) | 83 | none | 102.6 | 0.0 | README (recompute tables; B5, B12) + LM2 congruence rows (claims) | yes | all pass |
| 116 | 116_MPL_93_047-118 | 93 scans 47-118 (72) | 69 | 93: 71, 79, 85 | 98.7 | 0.0 | README (S20; typed sheets) | yes; typed-sheets paragraph | all pass |
| 117 | 117_MPL_93_119-191 | 93 scans 119-191 (73) | 71 | 93: 125, 141 | 95.7 | 0.0 | README (S20; typed sheets) | yes; typed-sheets paragraph | all pass |
| 118 | 118_MPL_93_192-236+161-5 | 93 scans 192-236; 161-5 scans 2-29 (73) | 72 | 161-5: 2 | 79.0 | 0.0 | README (S20; typed sheets) | yes; typed-sheets paragraph | all pass |
| 119 | 119_MPL_19_002-076 | 19 scans 2-76 (75) | 68 | 19: 3, 13, 30, 35, 56, 70, 72 | 88.8 | 0.0 | README | none (no war-game question) | all pass |
| 120 | 120_MPL_19_077-096+161-1+161-2_002-037 | 19 scans 77-96; 161-1 scans 2-20; 161-2 scans 2-37 (75) | 63 | 19: 86, 94; 161-1: 2, 3, 9, 15; 161-2: 2, 3, 17, 26, 33, 36 | 91.4 | 0.0 | README | none (no war-game question) | all pass |
| 121 | 121_MPL_161-2_038-112 | 161-2 scans 38-112 (75) | 69 | 161-2: 54, 80, 89, 97, 108, 111 | 106.4 | 0.0 | README | none (no war-game question) | all pass |
| 122 | 122_MPL_156-4_002-061 | 156-4 scans 2-61 (60) | 60 | none | 87.5 | 0.05 | README (S14, B10) + Esquisse (API transcription) | yes | all pass |
| 123 | 123_MPL_156-4_062-089+156-6_002-033 | 156-4 scans 62-89; 156-6 scans 2-33 (60) | 60 | none | 75.8 | 0.05 | README (S14, B10) + Esquisse (API transcription) | yes | all pass |
| 124 | 124_MPL_156-6_034-094 | 156-6 scans 34-94 (61) | 61 | none | 69.2 | 0.05 | README (S14, B10) + Esquisse (API transcription) | yes | all pass |
| 125 | 125_MPL_156-7_002-057 | 156-7 scans 2-57 (56) | 56 | none | 73.0 | 0.05 | README (S14, B10) + Esquisse (API transcription) | yes | all pass |
| 126 | 126_MPL_156-7_058-114 | 156-7 scans 58-114 (57) | 57 | none | 72.1 | 0.05 | README (S14, B10) + Esquisse (API transcription) | yes | all pass |
| 127 | 127_MPL_71+80_002-016 | 71 scans 2-48; 80 scans 2-16 (62) | 53 | 71: 2, 5, 16, 18, 20, 35; 80: 2, 9, 16 | 67.2 | 0.06 | README + Book V statements with status (claims) + Esquisse (API transcription) | none (no war-game question) | all pass |
| 128 | 128_MPL_80_017-073 | 80 scans 17-73 (57) | 52 | 80: 20, 31, 56, 60, 72 | 56.5 | 0.06 | README + Book V statements with status (claims) + Esquisse (API transcription) | none (no war-game question) | all pass |
| 129 | 129_MPL_81+154_046-060 | 81 scans 2-55; 154 scans 46-60 (69) | 67 | 81: 9, 31 | 114.7 | 0.06 | README + Book V statements with status (claims) + Esquisse (API transcription) | yes | all pass |
| 130 | 130_MPL_154_061-118 | 154 scans 61-118 (58) | 57 | 154: 99 | 209.1 | 0.06 | README + Book V statements with status (claims) + Esquisse (API transcription) | yes | all pass |
| 131 | 131_MPL_154_119-176 | 154 scans 119-176 (58) | 58 | none | 228.0 | 0.06 | README + Book V statements with status (claims) + Esquisse (API transcription) | yes | all pass |
| 132 | 132_MPL_73+77_002-051 | 73 scans 2-29; 77 scans 2-51 (78) | 74 | 73: 3, 8, 12, 14 | 86.9 | 0.0 | README (recompute tables; B5, B12) + LM2 congruence rows (claims) | yes | all pass |
| 133 | 133_MPL_77_052-129 | 77 scans 52-129 (78) | 78 | none | 93.5 | 0.0 | README (recompute tables; B5, B12) + LM2 congruence rows (claims) | yes | all pass |
| 134 | 134_MPL_77_130-158+78_002-051 | 77 scans 130-158; 78 scans 2-51 (79) | 79 | none | 94.7 | 0.0 | README (recompute tables; B5, B12) + LM2 congruence rows (claims) | yes | all pass |
| 135 | 135_MPL_78_052-130 | 78 scans 52-130 (79) | 79 | none | 95.0 | 0.0 | README (recompute tables; B5, B12) + LM2 congruence rows (claims) | yes | all pass |
| 136 | 136_MPL_82 | 82 scans 2-79 (78) | 75 | 82: 33, 36, 46 | 86.4 | 0.0 | README (recompute tables; B5, B12) + LM2 congruence rows (claims) | yes | all pass |
| 137 | 137_MPL_84_002-078 | 84 scans 2-78 (77) | 76 | 84: 8 | 121.0 | 0.0 | README (recompute tables; B5, B12) + LM2 congruence rows (claims) | yes | all pass |
| 138 | 138_MPL_84_079-155 | 84 scans 79-155 (77) | 76 | 84: 123 | 118.0 | 0.0 | README (recompute tables; B5, B12) + LM2 congruence rows (claims) | yes | all pass |
| 139 | 139_MPL_84_156-193+87 | 84 scans 156-193; 87 scans 2-41 (78) | 74 | 87: 2, 17, 21, 32 | 106.0 | 0.0 | README (recompute tables; B5, B12) + LM2 congruence rows (claims) | yes | all pass |
| 140 | 140_MPL_89+132 | 89 scans 2-21; 132 scans 2-32 (51) | 47 | 132: 5, 10, 13, 25 | 62.6 | 0.0 | README (recompute tables; B5, B12) + LM2 congruence rows (claims) | yes | all pass |
| 141 | 141_MPL_43_046-126 | 43 scans 46-126 (81) | 77 | 43: 83, 88, 99, 111 | 107.7 | 6.03 | README (round 2 §2.4; 43 and bridge B11) + first Book II return (claims) + Oda 1969 | yes | all pass |
| 142 | 142_MPL_43_127-208 | 43 scans 127-208 (82) | 76 | 43: 127, 157, 166, 175, 179, 194 | 111.0 | 6.03 | README (round 2 §2.4; 43 and bridge B11) + first Book II return (claims) + Oda 1969 | yes | all pass |
| 143 | 143_MPL_45 | 45 scans 2-80 (79) | 78 | 45: 44 | 129.7 | 6.03 | README (round 2 §2.4; 43 and bridge B11) + first Book II return (claims) + Oda 1969 | yes | all pass |
| 144 | 144_MPL_46_002-064 | 46 scans 2-64 (63) | 63 | none | 92.4 | 6.03 | README (round 2 §2.4; 43 and bridge B11) + first Book II return (claims) + Oda 1969 | yes | all pass |
| 145 | 145_MPL_46_065-095+53 | 46 scans 65-95; 53 scans 2-34 (64) | 64 | none | 101.6 | 6.03 | README (round 2 §2.4; 43 and bridge B11) + first Book II return (claims) + Oda 1969 | yes | all pass |
| 146 | 146_MPL_55+59 | 55 scans 2-18; 59 scans 2-28 (44) | 42 | 55: 16; 59: 22 | 61.1 | 6.03 | README (round 2 §2.4; 43 and bridge B11) + first Book II return (claims) + Oda 1969 | yes | all pass |
| 147 | 147_MPL_58 | 58 scans 2-67 (66) | 62 | 58: 29, 45, 55, 64 | 96.1 | 6.03 | README (round 2 §2.4; 43 and bridge B11) + first Book II return (claims) + Oda 1969 | yes | all pass |
| 148 | 148_MPL_90+91_002-046 | 90 scans 2-25; 91 scans 2-46 (69) | 65 | 91: 4, 15, 30, 33 | 90.9 | 0.0 | README (S19) | none (no war-game question) | all pass |
| 149 | 149_MPL_91_047-115 | 91 scans 47-115 (69) | 65 | 91: 60, 86, 103, 112 | 87.0 | 0.0 | README (S19) | none (no war-game question) | all pass |
| 150 | 150_MPL_91_116-143+94+97 | 91 scans 116-143; 94 scans 2-24; 97 scans 2-19 (69) | 62 | 91: 117, 125, 130, 133, 137; 97: 6, 15 | 86.7 | 0.0 | README (S19) | none (no war-game question) | all pass |
| 151 | 151_MPL_98+101 | 98 scans 2-44; 101 scans 2-43 (85) | 85 | none | 118.4 | 0.0 | README (S19) | none (no war-game question) | all pass |
| 152 | 152_MPL_31_002-075 | 31 scans 2-75 (74) | 67 | 31: 34, 40, 41, 46, 53, 64, 73 | 104.2 | 0.0 | README | none (no war-game question) | all pass |
| 153 | 153_MPL_31_076-102+32 | 31 scans 76-102; 32 scans 2-48 (74) | 72 | 31: 89; 32: 2 | 92.1 | 0.0 | README | none (no war-game question) | all pass |
| 154 | 154_MPL_33_002-079 | 33 scans 2-79 (78) | 78 | none | 112.9 | 0.0 | README | none (no war-game question) | all pass |
| 155 | 155_MPL_33_080-156 | 33 scans 80-156 (77) | 77 | none | 105.0 | 0.0 | README | none (no war-game question) | all pass |
| 156 | 156_MPL_33_157-181+34_002-054 | 33 scans 157-181; 34 scans 2-54 (78) | 75 | 33: 169; 34: 2, 52 | 110.9 | 0.0 | README | none (no war-game question) | all pass |
| 157 | 157_MPL_34_055-132 | 34 scans 55-132 (78) | 76 | 34: 83, 129 | 111.7 | 0.0 | README | none (no war-game question) | all pass |
| 158 | 158_MPL_34_133-210 | 34 scans 133-210 (78) | 76 | 34: 163, 182 | 108.1 | 0.0 | README | none (no war-game question) | all pass |
| 159 | 159_MPL_36 | 36 scans 2-85 (84) | 82 | 36: 2, 9 | 114.7 | 0.0 | README | none (no war-game question) | all pass |
| 160 | 160_MPL_39+40+41+42 | 39 scans 2-20; 40 scans 2-28; 41 scans 2-14; 42 scans 2-7 (65) | 62 | 39: 2, 9, 18 | 75.5 | 0.0 | README | none (no war-game question) | all pass |
| 161 | 161_MPL_122+123 | 122 scans 2-35; 123 scans 2-48 (81) | 76 | 122: 2, 19; 123: 21, 25, 33 | 111.5 | 0.0 | README | none (no war-game question) | all pass |
| 162 | 162_MPL_125+126+131 | 125 scans 2-9; 126 scans 2-35; 131 scans 2-42 (83) | 77 | 126: 17, 26, 31; 131: 11, 19, 22 | 110.2 | 0.0 | README | none (no war-game question) | all pass |
| 163 | 163_MPL_130 | 130 scans 2-50 (49) | 44 | 130: 3, 9, 16, 21, 34 | 70.5 | 0.0 | README | none (no war-game question) | all pass |
| 164 | 164_MPL_57_002-086 | 57 scans 2-86 (85) | 84 | 57: 2 | 131.1 | 6.03 | README (round 2 §2.4; 43 and bridge B11) + first Book II return (claims) + Oda 1969 | yes | all pass |
| 165 | 165_MPL_57_087-171 | 57 scans 87-171 (85) | 81 | 57: 98, 137, 146, 168 | 125.8 | 6.03 | README (round 2 §2.4; 43 and bridge B11) + first Book II return (claims) + Oda 1969 | yes | all pass |
| 166 | 166_MPL_57_172-256 | 57 scans 172-256 (85) | 79 | 57: 172, 200, 207, 213, 232, 247 | 114.2 | 6.03 | README (round 2 §2.4; 43 and bridge B11) + first Book II return (claims) + Oda 1969 | yes | all pass |
| 167 | 167_MPL_57_257-315+62_002-027 | 57 scans 257-315; 62 scans 2-27 (85) | 80 | 57: 278, 293; 62: 3, 18, 27 | 123.5 | 6.03 | README (round 2 §2.4; 43 and bridge B11) + first Book II return (claims) + Oda 1969 | yes | all pass |
| 168 | 168_MPL_62_028-097+63_002-016 | 62 scans 28-97; 63 scans 2-16 (85) | 82 | 62: 56; 63: 2, 15 | 149.1 | 6.03 | README (round 2 §2.4; 43 and bridge B11) + first Book II return (claims) + Oda 1969 | yes; typed-sheets paragraph | all pass |
| 169 | 169_MPL_63_017-101 | 63 scans 17-101 (85) | 78 | 63: 35, 56, 65, 79, 82, 86, 95 | 124.9 | 6.03 | README (round 2 §2.4; 43 and bridge B11) + first Book II return (claims) + Oda 1969 | yes; typed-sheets paragraph | all pass |
| 170 | 170_MPL_27+28+29_002-031 | 27 scans 2-37; 28 scans 2-11; 29 scans 2-31 (76) | 73 | 27: 8, 17; 29: 7 | 104.6 | 0.0 | README | none (no war-game question); typed-sheets paragraph | all pass |
| 171 | 171_MPL_29_032-108 | 29 scans 32-108 (77) | 77 | none | 114.9 | 0.0 | README | none (no war-game question); typed-sheets paragraph | all pass |
| 172 | 172_MPL_29_109-184 | 29 scans 109-184 (76) | 76 | none | 113.2 | 0.0 | README | none (no war-game question); typed-sheets paragraph | all pass |
| 173 | 173_MPL_29_185-217+37_002-045 | 29 scans 185-217; 37 scans 2-45 (77) | 71 | 29: 190, 208; 37: 2, 6, 29, 32 | 83.3 | 0.0 | README | none (no war-game question); typed-sheets paragraph | all pass |
| 174 | 174_MPL_37_046-100+160 | 37 scans 46-100; 160 scans 2-23 (77) | 73 | 37: 46, 56, 65; 160: 18 | 81.6 | 0.0 | README | none (no war-game question); typed-sheets paragraph | all pass |
| 175 | 175_MPL_1_051-122 | 1 scans 51-122 (72) | 71 | 1: 106 | 172.8 | 0.08 | README (+ return MPL_1_002-050 where cote 1 is in the package) | none (no war-game question) | all pass |
| 176 | 176_MPL_1_123-150+2 | 1 scans 123-150; 2 scans 2-45 (72) | 67 | 1: 123, 141; 2: 6, 27, 31 | 139.5 | 0.08 | README (+ return MPL_1_002-050 where cote 1 is in the package) | none (no war-game question) | all pass |
| 177 | 177_MPL_66+68+162-1+162-6 | 66 scans 2-5; 68 scans 2-56; 162-1 scans 2-10; 162-6 scans 2-6 (73) | 69 | 68: 23, 35, 47, 49 | 75.0 | 0.0 | README (+ return MPL_1_002-050 where cote 1 is in the package) | none (no war-game question) | all pass |
| 178 | 178_MPL_129_077-115+119_144-161+119_276-281 | 129 scans 77-115; 119 scans 144-161; 119 scans 276-281 (63) | 59 | 129: 79, 89; 119: 147, 154 | 85.9 | 0.0 | README | none (no war-game question); typed-sheets paragraph | all pass |

Groups in order: rank 3: the EGA plans, with 127 and 128 (55…); rank 3: the EGA plans, with 127 and 128 (56…); rank 3: the EGA plans, with 127 and 128 (57…); rank 9: the handwritten leaves of Pursuing Stacks, 158 and the dossier (58…); rank 9: the handwritten leaves of Pursuing Stacks, 158 and the dossier (59…); rank 9: the handwritten leaves of Pursuing Stacks, 158 and the dossier (60…); rank 9: the handwritten leaves of Pursuing Stacks, 158 and the dossier (61…); rank 9: the handwritten leaves of Pursuing Stacks, 158 and the dossier (62…); rank 9: the handwritten leaves of Pursuing Stacks, 158 and the dossier (63…); rank 9: the handwritten leaves of Pursuing Stacks, 158 and the dossier (64…); rank 9: the handwritten leaves of Pursuing Stacks, 158 and the dossier (65…); rank 9: the handwritten leaves of Pursuing Stacks, 158 and the dossier (66…); rank 9 continued: 137 and 133 (II.9) (67…); rank 9 continued: 137 and 133 (II.9) (68…); rank 6: motives (69…); rank 6: motives (70…); rank 6: motives (71…); rank 6: motives (72…); rank 6: motives (73…); rank 6: motives (74…); rank 6: motives (75…); rank 6: motives (76…); the rest of 136 (II.9) (77…); the rest of 136 (II.9) (78…); the rest of 136 (II.9) (79…); the rest of 136 (II.9) (80…); the rest of 136 (II.9) (81…); rank 10: the rest of 138 (III.7) (82…); rank 10: the rest of 138 (III.7) (83…); rank 10: maps on surfaces and the icosahedron (84…); rank 10: maps on surfaces and the icosahedron (85…); rank 10: maps on surfaces and the icosahedron (86…); rank 10: maps on surfaces and the icosahedron (87…); rank 10 with 79: the rest of 79 (88…); rank 10 with 79: the rest of 79 (89…); rank 10 with 79: the rest of 79 (90…); rank 10 with 83: the rest of 83 (91…); rank 10 with 83: the rest of 83 (92…); rank 10 with 64 (93…); rank 10 with 64 (94…); rank 10 with 64 (95…); rank 10: the two popular texts (96…); rank 11: the final state of the Geometrie des formes (97…); rank 11: the final state of the Geometrie des formes (98…); rank 11: the final state of the Geometrie des formes (99…); rank 11: the final state of the Geometrie des formes (100…); rank 11: the final state of the Geometrie des formes (101…); rank 11: the final state of the Geometrie des formes (102…); rank 12: 67 (103…); rank 12: 67 (104…); rank 13: tensor categories, cycles, L-functions (105…); rank 13: tensor categories, cycles, L-functions (106…); rank 13: tensor categories, cycles, L-functions (107…); rank 13: tensor categories, cycles, L-functions (108…); rank 13: tensor categories, cycles, L-functions (109…); rank 14: regular polyhedra, graphs (calculation folders) (110…); rank 14: regular polyhedra, graphs (calculation folders) (111…); rank 14: regular polyhedra, graphs (calculation folders) (112…); rank 14: regular polyhedra, graphs (calculation folders) (113…); rank 14: regular polyhedra, graphs (calculation folders) (114…); rank 14: regular polyhedra, graphs (calculation folders) (115…); rank 15: the rest of 93; 161-5 (116…); rank 15: the rest of 93; 161-5 (117…); rank 15: the rest of 93; 161-5 (118…); rank 16: categories, universal algebra, topos (119…); rank 16: categories, universal algebra, topos (120…); rank 16: categories, universal algebra, topos (121…); rank 17: the three earlier versions of Analysis situs (122…); rank 17: the three earlier versions of Analysis situs (123…); rank 17: the three earlier versions of Analysis situs (124…); rank 17: the three earlier versions of Analysis situs (125…); rank 17: the three earlier versions of Analysis situs (126…); rank 18, Book V: Jordan, immersions, pseudolines (127…); rank 18, Book V: Jordan, immersions, pseudolines (128…); rank 18, Book V: Jordan, immersions, pseudolines (129…); rank 18, Book V: Jordan, immersions, pseudolines (130…); rank 18, Book V: Jordan, immersions, pseudolines (131…); rank 18, Book IV: polygons, quadrics, graphs (132…); rank 18, Book IV: polygons, quadrics, graphs (133…); rank 18, Book IV: polygons, quadrics, graphs (134…); rank 18, Book IV: polygons, quadrics, graphs (135…); rank 18, Book IV: polygons, quadrics, graphs (136…); rank 18, Book IV: polygons, quadrics, graphs (137…); rank 18, Book IV: polygons, quadrics, graphs (138…); rank 18, Book IV: polygons, quadrics, graphs (139…); rank 18, Book IV: polygons, quadrics, graphs (140…); rank 19: duality of groups, Picard, abelian varieties (141…); rank 19: duality of groups, Picard, abelian varieties (142…); rank 19: duality of groups, Picard, abelian varieties (143…); rank 19: duality of groups, Picard, abelian varieties (144…); rank 19: duality of groups, Picard, abelian varieties (145…); rank 19: duality of groups, Picard, abelian varieties (146…); rank 19: duality of groups, Picard, abelian varieties (147…); rank 20: K-theory, Neron, residues, intersections (148…); rank 20: K-theory, Neron, residues, intersections (149…); rank 20: K-theory, Neron, residues, intersections (150…); rank 20: K-theory, Neron, residues, intersections (151…); rank 21: SGA 4, 5 and 7 drafts (152…); rank 21: SGA 4, 5 and 7 drafts (153…); rank 21: SGA 4, 5 and 7 drafts (154…); rank 21: SGA 4, 5 and 7 drafts (155…); rank 21: SGA 4, 5 and 7 drafts (156…); rank 21: SGA 4, 5 and 7 drafts (157…); rank 21: SGA 4, 5 and 7 drafts (158…); rank 21: SGA 4, 5 and 7 drafts (159…); rank 21: SGA 4, 5 and 7 drafts (160…); rank 22: descent, heights, etale cohomology (161…); rank 22: descent, heights, etale cohomology (162…); rank 22: descent, heights, etale cohomology (163…); rank 23: Picard schemes (164…); rank 23: Picard schemes (165…); rank 23: Picard schemes (166…); rank 23: Picard schemes (167…); rank 23: Picard schemes (168…); rank 23: Picard schemes (169…); rank 24: SGA 3 and the reeditions (170…); rank 24: SGA 3 and the reeditions (171…); rank 24: SGA 3 and the reeditions (172…); rank 24: SGA 3 and the reeditions (173…); rank 24: SGA 3 and the reeditions (174…); rank 25: functional analysis (rest), early notes, documents (175…); rank 25: functional analysis (rest), early notes, documents (176…); rank 25: functional analysis (rest), early notes, documents (177…); API-route cotes: their handwritten leaves (129, 119) (178…).

## Exclusions, with their reasons

| What | Why it has no package here | Source |
|---|---|---|
| 147 (all), 149, 146, 142; 1 scans 2-50; 16, 47, 54, 44 | packaged and returned (`packages_done\`: MPL_1_002-050, MPL_147_*, 04-11) | packages_done\ |
| 5, 6, 7, 8, 9, 4, 100 (crystals) | packages 30-33 (30 in packages_done\); 100 complete in 33 (scans 1-53, 47 blank) | build manifests |
| 144, 148, 143, 145, 141; 150, 151, 152, 120, 121, 153, 155; 156-1, 156-2; 159; 49-52 | packages 34-45, 52, 54 | PACKAGING_REPORT_RANKS_4_5_PROBES |
| 136 scans 2-46, 93 2-46, 79 1-45, 83 1-45, 154 1-45, 138 1-45, 43 1-45 | the probes (46-51, 53); the rest of each cote is packaged here from scan 47 (136, 93) or 46 | same |
| *La Longue Marche*, 140-1 to 140-4 (1,584 pp.) | done by our pilot: PLAN_EVERYTHING ("Already ours: transcription done, second pass running"); PLACEMENT route "done (second pass finishing)". Verified | PLAN_EVERYTHING.md, PLACEMENT_EVERYTHING.csv |
| *Les Dérivateurs*, manuscript 157-1 to 157-5 (2,135 pp.) | "the Künzer-Malgoire-Maltsiniotis edition is complete; our companion covers 28 of its 32 chunks"; route "done through the printed edition; concordance only". 158, 159 and 160 are not part of it (158: around the derivators, rank 9; 159: projective connections, probe 52; 160: SGA 3, rank 24) and are packaged | PLAN_EVERYTHING.md, Scope |
| *Pursuing Stacks* typescript, 134-1 to 134-8 | API (round 2 §4.4: "*Pursuing Stacks*, the Esquisse and cotes 24-25 leave the Pro queue for the API (their handwritten leaves stay in it)"); 680 pages done over the API. Its handwritten leaves, not sent there, are packaged (58, 59): 134-1 whole, 134-2 scans 146-185 (letter copies), 134-8 scans 43-87 (notes on listing paper, with typed versos) | API_TYPESCRIPTS_REPORT.md, "Pages for the in-app route or Pro" |
| 134-2 scans 116-144 (R. Brown's translation, cover note, comments), duplicates and *Récoltes et Semailles* versos of 134-2 | typed: the API report sends Brown's pages over the API; the duplicates and versos were left out there | same, "Not done" |
| *Esquisse*, cote 119: copy 1 (done over the API), copy 2 (typescript with annotations), offprints of 1971, typed reports and course texts | API (clean-scan route). Its handwritten pages (scans 144-161 and 276-281, found by a text-recognition score and checked on thumbnails) are packaged (178) | PLACEMENT; EXISTING_EDITIONS_CHECK §2 |
| Cotes 24 and 25 (EGA V) | API (round 2 §1.4 row 5, §4.4); typed throughout (text-recognition score of every page), not yet done over the API (credit ran out) | API_TYPESCRIPTS_REPORT.md |
| 129 (Montréal seminar 1970), 162-5 (Tapis de Quillen): typed parts | API as clean typescripts (PLAN_EVERYTHING; PLACEMENT). Their handwritten pages are packaged: 129 scans 77-115 (handwritten notes interleaved with some faint typed sheets; 178), 162-5 scans 19-32 (notes of 1968; 65) | PLACEMENT; text recognition made for this build |
| 139 (Prix Émile Picard medal, 2 pp.) | "concordance only" | PLACEMENT |
| 110 | "not in the open archive (slot reserved)"; not in MANIFEST | PLACEMENT; PLAN_EVERYTHING |
| PDF page 1 of every file | the IMAG cover sheet of the digitization, not archive material | returned package 11 (16 scan 1) |

## Not found, and problems met

- **Paris-years printed witnesses (round 2 §1.8).** Only Oda 1969 is local (`context_sources_20261112\oda1969`); it
  is in the motives, rank-13 and abelian/Picard contexts. Not found locally: Kleiman's text in *Dix exposés*,
  "Standard conjectures", Mukai 1981, the CSG transcriptions of the letters (L10d, L11d, L23d), the letter to Tate.
  "Motifs" (the 24 typed pages from cote 12), which the war game names as the motives' witness, is not local either.
  These are the first upgrades for those contexts.
- **Contents of our SGA 3, 4, 5, 7 editions** (PLACEMENT's context for ranks 21 and 24) were not assembled; those
  packages carry a README only.
- **Returns not yet in.** The contexts of the rests of the probes (136, 93, 79, 83, 154, 138, 43), of 156 (after 45),
  of 64 and 67 (rank-4 returns) and of rank 17 (rank-11 returns) name the returns they lack; adding them is the main
  upgrade before sending.
- **No review at effort max** for STRATA, PATHS, BISITE or RESIDUE: every row in the dossier and Book V statements is
  labelled "claim (return: ...)".
- **Typed sheets not yet inventoried.** The plan sends the typed sheets of 10, 12, 15 (and 37) over the API "after an
  inventory"; no inventory exists, so these packages hold the whole cotes and ask for every typed sheet to be marked in
  `sheet_kind`. If the inventory is made first, those scans can be dropped before sending.
- **161-5** is printed Barsotti-Tate offprints; PLACEMENT says "only the annotations and the notes are transcribed",
  but the template transcribes everything. The package (118) follows the template; decide before sending.
- **The 18 cotes to inventory for versos** (PLACEMENT_EVERYTHING.md) were not inventoried; the template's
  `sheet_kind` column covers reused sheets inside the run.
- **The page choice for 129 and 119** rests on a Tesseract (English) word score and a look at thumbnails, not on a
  full reading: a few typed pages of 129 are inside the range, and a handwritten page outside it would be missed.
- **134-2 front matter** (scans 9, 11, 14: contents pages and the dedication, entirely handwritten) went over the API
  and is not repackaged.
- **Scan counts.** Every PDF has one page more than its MANIFEST count (all 178 checked with pdfinfo).

## Ready-made PRO_QUEUE rows (for the main session to paste; renumber the # column to follow the queue)

| # | Prompt folder | Series | What it is | Upload |
|---|---|---|---|---|
| 55 | 55_MPL_21+22+23_002-026 | archive | 81 scans (21 scans 2-29; 22 scans 2-30; 23 scans 2-26); Book I, order W: rank 3; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 56 | 56_MPL_23_027-099+26 | archive | 76 scans (23 scans 27-99; 26 scans 2-11); Book I, order W: rank 3; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 57 | 57_MPL_35+48+102+127+128 | archive | 75 scans (35 scans 2-6; 48 scans 2-6; 102 scans 2-14; 127 scans 2-24; 128 scans 2-32); Book I, order W: rank 3; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 58 | 58_MPL_134-1+134-2_146-185 | archive | 45 scans (134-1 scans 2-7; 134-2 scans 146-185); Book VI, order W: rank 9 with 137 and 133; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 59 | 59_MPL_134-8_043-087+158_002-023 | archive | 64 scans (134-8 scans 43-87; 158 scans 2-23); Book VI, order W: rank 9 with 137 and 133; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 60 | 60_MPL_158_024-086+108 | archive | 65 scans (158 scans 24-86; 108 scans 2-6); Book VI, order W: rank 9 with 137 and 133; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 61 | 61_MPL_112+113+114+115+116+117 | archive | 69 scans (112 scans 2-5; 113 scans 2-13; 114 scans 2-6; 115 scans 2-15; 116 scans 2-11; 117 scans 2-26); Book VI, order W: rank 9 with 137 and 133; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 62 | 62_MPL_118+103 | archive | 54 scans (118 scans 2-41; 103 scans 2-18); Book VI, order W: rank 9 with 137 and 133; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 63 | 63_MPL_104+105 | archive | 64 scans (104 scans 2-17; 105 scans 2-53); Book VI, order W: rank 9 with 137 and 133; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 64 | 64_MPL_106+107 | archive | 41 scans (106 scans 2-17; 107 scans 2-26); Book VI, order W: rank 9 with 137 and 133; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 65 | 65_MPL_109+111+162-5_019-032 | archive | 61 scans (109 scans 2-38; 111 scans 2-17; 162-5 scans 19-32); Book VI, order W: rank 9 with 137 and 133; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 66 | 66_MPL_135 | archive | 51 scans (135 scans 2-59); Book VI, order W: rank 9 with 137 and 133; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 67 | 67_MPL_137_002-070 | archive | 68 scans (137 scans 2-70); Book II, order W: rank 9 with 137 and 133; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 68 | 68_MPL_137_071-086+133 | archive | 66 scans (137 scans 71-86; 133 scans 2-54); Book II, order W: rank 9 with 137 and 133; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 69 | 69_MPL_14_002-066 | archive | 62 scans (14 scans 2-66); Book II, order W: rank 6; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 70 | 70_MPL_14_067-132 | archive | 60 scans (14 scans 67-132); Book II, order W: rank 6; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 71 | 71_MPL_13+12_002-034 | archive | 76 scans (13 scans 2-52; 12 scans 2-34); Book II, order W: rank 6; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 72 | 72_MPL_12_035-118 | archive | 82 scans (12 scans 35-118); Book II, order W: rank 6; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 73 | 73_MPL_12_119-168+15_002-035 | archive | 81 scans (12 scans 119-168; 15 scans 2-35); Book II, order W: rank 6; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 74 | 74_MPL_15_036-119 | archive | 79 scans (15 scans 36-119); Book II, order W: rank 6; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 75 | 75_MPL_15_120-204 | archive | 76 scans (15 scans 120-204); Book II, order W: rank 6; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 76 | 76_MPL_15_205-228+18 | archive | 84 scans (15 scans 205-228; 18 scans 2-62); Book II, order W: rank 6; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 77 | 77_MPL_136_047-112 | archive | 64 scans (136 scans 47-112); Book II, order W: the rest of 136; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 78 | 78_MPL_136_113-178 | archive | 64 scans (136 scans 113-178); Book II, order W: the rest of 136; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 79 | 79_MPL_136_179-244 | archive | 64 scans (136 scans 179-244); Book II, order W: the rest of 136; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 80 | 80_MPL_136_245-310 | archive | 66 scans (136 scans 245-310); Book II, order W: the rest of 136; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 81 | 81_MPL_136_311-376 | archive | 61 scans (136 scans 311-376); Book II, order W: the rest of 136; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 82 | 82_MPL_138_046-089 | archive | 42 scans (138 scans 46-89); Book III, order W: rank 10 with 79, 83, 64; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 83 | 83_MPL_138_090-133 | archive | 43 scans (138 scans 90-133); Book III, order W: rank 10 with 79, 83, 64; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 84 | 84_MPL_76 | archive | 55 scans (76 scans 2-63); Book IV, order W: rank 10 with 79, 83, 64; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 85 | 85_MPL_88+70_002-056 | archive | 66 scans (88 scans 2-16; 70 scans 2-56); Book IV, order W: rank 10 with 79, 83, 64; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 86 | 86_MPL_70_057-126 | archive | 65 scans (70 scans 57-126); Book IV, order W: rank 10 with 79, 83, 64; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 87 | 87_MPL_75+161-6 | archive | 59 scans (75 scans 2-33; 161-6 scans 2-34); Book IV, order W: rank 10 with 79, 83, 64; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 88 | 88_MPL_79_046-129 | archive | 84 scans (79 scans 46-129); Book IV, order W: rank 10 with 79, 83, 64; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 89 | 89_MPL_79_130-213 | archive | 84 scans (79 scans 130-213); Book IV, order W: rank 10 with 79, 83, 64; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 90 | 90_MPL_79_214-297 | archive | 81 scans (79 scans 214-297); Book IV, order W: rank 10 with 79, 83, 64; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 91 | 91_MPL_83_046-133 | archive | 85 scans (83 scans 46-133); Book IV, order W: rank 10 with 79, 83, 64; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 92 | 92_MPL_83_134-222 | archive | 86 scans (83 scans 134-222); Book IV, order W: rank 10 with 79, 83, 64; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 93 | 93_MPL_64_002-053 | archive | 52 scans (64 scans 2-53); Book III, order W: rank 10 with 79, 83, 64; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 94 | 94_MPL_64_054-105 | archive | 52 scans (64 scans 54-105); Book III, order W: rank 10 with 79, 83, 64; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 95 | 95_MPL_64_106-157 | archive | 49 scans (64 scans 106-157); Book III, order W: rank 10 with 79, 83, 64; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 96 | 96_MPL_161-3+161-4 | archive | 74 scans (161-3 scans 2-55; 161-4 scans 2-32); Book front door, order W: rank 10 with the two popular texts; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 97 | 97_MPL_156-8_002-056 | archive | 55 scans (156-8 scans 2-56); Book V, order W: rank 11; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 98 | 98_MPL_156-8_057-112 | archive | 56 scans (156-8 scans 57-112); Book V, order W: rank 11; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 99 | 99_MPL_156-8_113-127+156-5 | archive | 63 scans (156-8 scans 113-127; 156-5 scans 2-49); Book V, order W: rank 11; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 100 | 100_MPL_156-3+156-9_002-020 | archive | 59 scans (156-3 scans 2-41; 156-9 scans 2-20); Book V, order W: rank 11; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 101 | 101_MPL_156-9_021-080 | archive | 60 scans (156-9 scans 21-80); Book V, order W: rank 11; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 102 | 102_MPL_156-9_081-140 | archive | 59 scans (156-9 scans 81-140); Book V, order W: rank 11; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 103 | 103_MPL_67_002-051 | archive | 46 scans (67 scans 2-51); Book III, rank 12; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 104 | 104_MPL_67_052-101 | archive | 47 scans (67 scans 52-101); Book III, rank 12; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 105 | 105_MPL_10_002-085 | archive | 80 scans (10 scans 2-85); Book II, rank 13; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 106 | 106_MPL_10_086-170 | archive | 79 scans (10 scans 86-170); Book II, rank 13; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 107 | 107_MPL_10_171-198+11 | archive | 82 scans (10 scans 171-198; 11 scans 2-58); Book II, rank 13; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 108 | 108_MPL_56 | archive | 35 scans (56 scans 2-39); Book II, rank 13; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 109 | 109_MPL_60 | archive | 69 scans (60 scans 2-70); Book II, rank 13; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 110 | 110_MPL_69_002-083 | archive | 76 scans (69 scans 2-83); Book IV, rank 14; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 111 | 111_MPL_69_084-120+72_002-046 | archive | 75 scans (69 scans 84-120; 72 scans 2-46); Book IV, rank 14; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 112 | 112_MPL_72_047-113+74_002-016 | archive | 81 scans (72 scans 47-113; 74 scans 2-16); Book IV, rank 14; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 113 | 113_MPL_74_017-099 | archive | 75 scans (74 scans 17-99); Book IV, rank 14; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 114 | 114_MPL_74_100-136+85_002-047 | archive | 82 scans (74 scans 100-136; 85 scans 2-47); Book IV, rank 14; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 115 | 115_MPL_85_048-098+86 | archive | 83 scans (85 scans 48-98; 86 scans 2-33); Book IV, rank 14; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 116 | 116_MPL_93_047-118 | archive | 69 scans (93 scans 47-118); Book II, rank 15; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 117 | 117_MPL_93_119-191 | archive | 71 scans (93 scans 119-191); Book II, rank 15; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 118 | 118_MPL_93_192-236+161-5 | archive | 72 scans (93 scans 192-236; 161-5 scans 2-29); Book II, rank 15; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 119 | 119_MPL_19_002-076 | archive | 68 scans (19 scans 2-76); Book VI, rank 16; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 120 | 120_MPL_19_077-096+161-1+161-2_002-037 | archive | 63 scans (19 scans 77-96; 161-1 scans 2-20; 161-2 scans 2-37); Book VI, rank 16; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 121 | 121_MPL_161-2_038-112 | archive | 69 scans (161-2 scans 38-112); Book VI, rank 16; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 122 | 122_MPL_156-4_002-061 | archive | 60 scans (156-4 scans 2-61); Book V, rank 17; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 123 | 123_MPL_156-4_062-089+156-6_002-033 | archive | 60 scans (156-4 scans 62-89; 156-6 scans 2-33); Book V, rank 17; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 124 | 124_MPL_156-6_034-094 | archive | 61 scans (156-6 scans 34-94); Book V, rank 17; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 125 | 125_MPL_156-7_002-057 | archive | 56 scans (156-7 scans 2-57); Book V, rank 17; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 126 | 126_MPL_156-7_058-114 | archive | 57 scans (156-7 scans 58-114); Book V, rank 17; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 127 | 127_MPL_71+80_002-016 | archive | 53 scans (71 scans 2-48; 80 scans 2-16); Book V, rank 18; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 128 | 128_MPL_80_017-073 | archive | 52 scans (80 scans 17-73); Book V, rank 18; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 129 | 129_MPL_81+154_046-060 | archive | 67 scans (81 scans 2-55; 154 scans 46-60); Book V, rank 18; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 130 | 130_MPL_154_061-118 | archive | 57 scans (154 scans 61-118); Book V, rank 18; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 131 | 131_MPL_154_119-176 | archive | 58 scans (154 scans 119-176); Book V, rank 18; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 132 | 132_MPL_73+77_002-051 | archive | 74 scans (73 scans 2-29; 77 scans 2-51); Book IV, rank 18; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 133 | 133_MPL_77_052-129 | archive | 78 scans (77 scans 52-129); Book IV, rank 18; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 134 | 134_MPL_77_130-158+78_002-051 | archive | 79 scans (77 scans 130-158; 78 scans 2-51); Book IV, rank 18; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 135 | 135_MPL_78_052-130 | archive | 79 scans (78 scans 52-130); Book IV, rank 18; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 136 | 136_MPL_82 | archive | 75 scans (82 scans 2-79); Book IV, rank 18; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 137 | 137_MPL_84_002-078 | archive | 76 scans (84 scans 2-78); Book IV, rank 18; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 138 | 138_MPL_84_079-155 | archive | 76 scans (84 scans 79-155); Book IV, rank 18; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 139 | 139_MPL_84_156-193+87 | archive | 74 scans (84 scans 156-193; 87 scans 2-41); Book IV, rank 18; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 140 | 140_MPL_89+132 | archive | 47 scans (89 scans 2-21; 132 scans 2-32); Book IV, rank 18; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 141 | 141_MPL_43_046-126 | archive | 77 scans (43 scans 46-126); Book I, rank 19; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 142 | 142_MPL_43_127-208 | archive | 76 scans (43 scans 127-208); Book I, rank 19; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 143 | 143_MPL_45 | archive | 78 scans (45 scans 2-80); Book I, rank 19; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 144 | 144_MPL_46_002-064 | archive | 63 scans (46 scans 2-64); Book I, rank 19; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 145 | 145_MPL_46_065-095+53 | archive | 64 scans (46 scans 65-95; 53 scans 2-34); Book I, rank 19; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 146 | 146_MPL_55+59 | archive | 42 scans (55 scans 2-18; 59 scans 2-28); Book I, rank 19; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 147 | 147_MPL_58 | archive | 62 scans (58 scans 2-67); Book I, rank 19; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 148 | 148_MPL_90+91_002-046 | archive | 65 scans (90 scans 2-25; 91 scans 2-46); Book I, rank 20; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 149 | 149_MPL_91_047-115 | archive | 65 scans (91 scans 47-115); Book I, rank 20; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 150 | 150_MPL_91_116-143+94+97 | archive | 62 scans (91 scans 116-143; 94 scans 2-24; 97 scans 2-19); Book I, rank 20; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 151 | 151_MPL_98+101 | archive | 85 scans (98 scans 2-44; 101 scans 2-43); Book I, rank 20; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 152 | 152_MPL_31_002-075 | archive | 67 scans (31 scans 2-75); Book I, rank 21; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 153 | 153_MPL_31_076-102+32 | archive | 72 scans (31 scans 76-102; 32 scans 2-48); Book I, rank 21; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 154 | 154_MPL_33_002-079 | archive | 78 scans (33 scans 2-79); Book I, rank 21; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 155 | 155_MPL_33_080-156 | archive | 77 scans (33 scans 80-156); Book I, rank 21; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 156 | 156_MPL_33_157-181+34_002-054 | archive | 75 scans (33 scans 157-181; 34 scans 2-54); Book I, rank 21; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 157 | 157_MPL_34_055-132 | archive | 76 scans (34 scans 55-132); Book I, rank 21; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 158 | 158_MPL_34_133-210 | archive | 76 scans (34 scans 133-210); Book I, rank 21; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 159 | 159_MPL_36 | archive | 82 scans (36 scans 2-85); Book I, rank 21; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 160 | 160_MPL_39+40+41+42 | archive | 62 scans (39 scans 2-20; 40 scans 2-28; 41 scans 2-14; 42 scans 2-7); Book I, rank 21; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 161 | 161_MPL_122+123 | archive | 76 scans (122 scans 2-35; 123 scans 2-48); Book I, rank 22; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 162 | 162_MPL_125+126+131 | archive | 77 scans (125 scans 2-9; 126 scans 2-35; 131 scans 2-42); Book I, rank 22; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 163 | 163_MPL_130 | archive | 44 scans (130 scans 2-50); Book I, rank 22; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 164 | 164_MPL_57_002-086 | archive | 84 scans (57 scans 2-86); Book I, rank 23; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 165 | 165_MPL_57_087-171 | archive | 81 scans (57 scans 87-171); Book I, rank 23; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 166 | 166_MPL_57_172-256 | archive | 79 scans (57 scans 172-256); Book I, rank 23; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 167 | 167_MPL_57_257-315+62_002-027 | archive | 80 scans (57 scans 257-315; 62 scans 2-27); Book I, rank 23; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 168 | 168_MPL_62_028-097+63_002-016 | archive | 82 scans (62 scans 28-97; 63 scans 2-16); Book I, rank 23; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 169 | 169_MPL_63_017-101 | archive | 78 scans (63 scans 17-101); Book I, rank 23; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 170 | 170_MPL_27+28+29_002-031 | archive | 73 scans (27 scans 2-37; 28 scans 2-11; 29 scans 2-31); Book I, rank 24; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 171 | 171_MPL_29_032-108 | archive | 77 scans (29 scans 32-108); Book I, rank 24; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 172 | 172_MPL_29_109-184 | archive | 76 scans (29 scans 109-184); Book I, rank 24; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 173 | 173_MPL_29_185-217+37_002-045 | archive | 71 scans (29 scans 185-217; 37 scans 2-45); Book I, rank 24; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 174 | 174_MPL_37_046-100+160 | archive | 73 scans (37 scans 46-100; 160 scans 2-23); Book I, rank 24; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 175 | 175_MPL_1_051-122 | archive | 71 scans (1 scans 51-122); Book workshop, rank 25; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 176 | 176_MPL_1_123-150+2 | archive | 67 scans (1 scans 123-150; 2 scans 2-45); Book workshop, rank 25; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 177 | 177_MPL_66+68+162-1+162-6 | archive | 69 scans (66 scans 2-5; 68 scans 2-56; 162-1 scans 2-10; 162-6 scans 2-6); Book workshop, rank 25; preliminary context, opened after the freeze | PROMPT.md + 2 zips |
| 178 | 178_MPL_129_077-115+119_144-161+119_276-281 | archive | 59 scans (129 scans 77-115; 119 scans 144-161; 119 scans 276-281); Book II, workshop, after rank 25; preliminary context, opened after the freeze | PROMPT.md + 2 zips |

## Send next, in order W

After the probes (45-54): rank 3, then rank 9 with 137 and 133, then rank 6, then the rest of 136, then rank 10 with 79, 83, 64, then rank 11; after that the plan's rank, then the cote number.

1. 55_MPL_21+22+23_002-026 (81 scans; rank 3: the EGA plans, with 127 and 128)
2. 56_MPL_23_027-099+26 (76 scans; rank 3: the EGA plans, with 127 and 128)
3. 57_MPL_35+48+102+127+128 (75 scans; rank 3: the EGA plans, with 127 and 128)
4. 58_MPL_134-1+134-2_146-185 (45 scans; rank 9: the handwritten leaves of Pursuing Stacks, 158 and the dossier)
5. 59_MPL_134-8_043-087+158_002-023 (64 scans; rank 9: the handwritten leaves of Pursuing Stacks, 158 and the dossier)
6. 60_MPL_158_024-086+108 (65 scans; rank 9: the handwritten leaves of Pursuing Stacks, 158 and the dossier)
7. 61_MPL_112+113+114+115+116+117 (69 scans; rank 9: the handwritten leaves of Pursuing Stacks, 158 and the dossier)
8. 62_MPL_118+103 (54 scans; rank 9: the handwritten leaves of Pursuing Stacks, 158 and the dossier)
9. 63_MPL_104+105 (64 scans; rank 9: the handwritten leaves of Pursuing Stacks, 158 and the dossier)
10. 64_MPL_106+107 (41 scans; rank 9: the handwritten leaves of Pursuing Stacks, 158 and the dossier)

Then 65-68 (the rest of the dossier, 137 and 133), 69-76 (motives), 77-81 (the rest of 136), 82-96 (rank 10 with 79, 83, 64 and the popular texts), 97-102 (156 final), and onward by number.


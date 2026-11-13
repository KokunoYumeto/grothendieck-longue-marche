# Packaging report, 12 November 2026: LM4, LM5, LM6

Packaged by Claude Opus 5.5. This was packaging only. No PROMPT.md, BACKGROUND.md or mathematics was edited. Each upload folder holds exactly `PROMPT.md` (a byte-identical copy of the work folder's `PROMPT.md`) and `<NAME>_background.zip`. Each folder is flat, has 2 files and has one zip under 500 MB, so no zip was split.

- **Builder:** `package_20261112.py` in this folder. It writes the zips in the same layout as `LM3b_TEICHMULLER_PUSH/build_zip_20261111.py` and `lm12_push_20261111.py`:
  - `MANIFEST.tsv` sits at the root of each zip, with columns `path_in_zip`, `source_path_or_url`, `sha256`, `bytes` and `note`.
  - The transcriptions are in `longue_marche/LM_<KEY>/` with their `_notes_checked.md`.
  - The scans are in `scans/<cote>/scanNNN.jpg`.
  - The table of contents and the notes are in `context/`.
  - Answers go in `<X>_return/` and reviews in `<X>_review/`. The `code/` and `audit/` folders of the LM2, LM3 and LM3b answers are left out, as in the earlier builds.
  - Zip names are ASCII-sanitized; none needed changing.
- **Copy of the manifest:** `<NAME>/MANIFEST_20261112.tsv` in each work folder. It lists every file in the zip with its source path and SHA-256.
- **Rule for the current text of a package:** the first file that exists among `second_pass\LM_<KEY>_checked_fixed.tex`, `second_pass\LM_<KEY>_checked.tex`, `answers\fixed\…` and `answers\unzipped\…`. The notes come from `second_pass\CURRENT_TEXT_INDEX.tsv`. Where a ZIP_LIST row named an older file, the current one was used. Those cases are listed under each prompt.
- **Checks run on every zip:**
  - `testzip` passed.
  - No names are non-ASCII.
  - No e-mail addresses or key/token patterns appear in any text member (md, tex, csv, txt, bib, py, json, tsv).
  - No file comes from the Obsidian notes folder.
  - Nothing was written to any `outbox/` or writers' `outputs/` folder.

## LM4_FINITE_GROUP_ACTIONS: ready

- **Upload folder:** `..\pro_prompts_draft_20261111\LM4_FINITE_GROUP_ACTIONS\`
- **Zip:** `LM4_FINITE_GROUP_ACTIONS_background.zip`, 171,489,608 bytes (171.5 MB), 548 files (MANIFEST.tsv included).

**Rows included (109 of 110):**
- `PROMPT.md` at the root.
- `BACKGROUND.md` and `BACKGROUND_ADD.md` in `context/`.
- `OVERVIEW.md` as `context/OVERVIEW.md`.
- Packages P01–P058 (cote 140-2): the current text and checked notes of each, in `longue_marche/` (116 files).
- The Dérivateurs returns, named sections only, as listed in BACKGROUND.md and BACKGROUND_ADD.md and as cited in the "After …" blocks:
  - `CATHOT_return/sections/BC.tex`
  - `GALOIS_return/`: `sections/C.tex`, `sections/conventions.tex`, `GALOIS_paper.tex`, `GALOIS_results.csv`
  - `STRATA_return/`: `sections/00_conventions.tex`, `B.tex`, `F.tex`, `STRATA_paper.tex`, `STRATA_results.csv`, `STRATA_report.md`
  - `PATHS_return/`: `sections/00_conventions.tex`, `D.tex`, `PATHS_paper.tex`, `PATHS_results.csv`, `PATHS_report.md`
- `LM2_return/`, `LM3_return/` and `LM3b_return/`, taken from the answer zips without `code/` or `audit/`.
- `LM3_review/REVIEW.md` and `LM3b_review/REVIEW.md` (Opus 5.5, effort max).
- `LM_EXPERT_notes/`: FINDINGS, HUNCHES, LIT_LM6_anabelian and LIT_LM4_surfaces.
- 34 papers in `literature/<slug>/`.

**Added under WHAT IS ATTACHED:**
- The scans named in the prompt, cote 140-2: 53–54, 62, 69, 82, 84, 86, 91–92, 97–102, 115–118, 130, 137–160, 179–205, 222–230, 264–471 and 498–501. That is 292 images, which also cover the Part-heading ranges 264–294, 294–317 and 318–436.
- In `context/`: the table of contents, `GLOBAL_PASS.md`, `merge_fixes_open.md` and `DEVELOPMENT_CANDIDATES_draft_20261108.md`.
- `papers/`: two background papers of BACKGROUND.md that were downloaded to `_downloads` and are not already in `literature/`. They are Boggi–Zalesskii arXiv:2406.08639v2 and Nakamura, Sugaku Expositions 1997.

**Current text used where the row named an older file:** P04 and P05 now have `second_pass\LM_P0x_checked.tex`; the row named `answers\unzipped`. P046 now has `_checked_fixed.tex`.

**Left out:**
- `STRUCTURE.txt`, which is marked NOT FOR THE ZIP.

**Mismatch with the prompt:**
- The blocks "After STRATA" and "After PATHS" say that `STRATA_review/REVIEW_author.md` and `PATHS_review/REVIEW_author.md` are attached. They are not in the zip. The ZIP_LIST holds them back because those reviews are being redone at effort max, and `derivateurs_companion_20261109\pro_reviews_max_20261112\5_STRATA` and `6_PATHS` are still empty. Pro will look for these two files. They can be added when the redone reviews exist, or the user can choose to send the zip as it is.
- `OVERVIEW.md` and the table of contents are in `context/` rather than at the root, as in the earlier LM zips.

## LM5_MULTI_GALOIS_TOPOI: ready

- **Upload folder:** `..\pro_prompts_draft_20261111\LM5_MULTI_GALOIS_TOPOI\`
- **Zip:** `LM5_MULTI_GALOIS_TOPOI_background.zip`, 185,779,102 bytes (185.8 MB), 661 files.

**Rows included (86 of 87):**
- `PROMPT.md`.
- `context/BACKGROUND.md`, `context/BACKGROUND_ADD.md` and `context/OVERVIEW.md`.
- Packages P01–P058 in `longue_marche/`.
- The Dérivateurs returns, per BACKGROUND.md and BACKGROUND_ADD.md:
  - `CATHOT_return/`: `sections/BC.tex`, `D.tex`, `E.tex`, `E_ind.tex`, `E_local_union.tex`, `research/BC_report.md`
  - `GALOIS_return/`: the report, register, paper (pdf and tex), bib, and `sections/conventions, A, B, B_general, B_KT, C, E, F`
  - `STRATA_return/`: the report, register, paper (pdf and tex), bib, and `sections/00_conventions, A, B, C, F`
  - `PATHS_return/`: the report, register, paper (pdf and tex), bib, and `sections/00_conventions, A_colimits, C_paths, D, D_kt, E`
- `LM3_return/` and `LM3b_return/`, without code or audit.
- `LM3_review/REVIEW.md` and `LM3b_review/REVIEW.md`.
- The four MPL transcriptions and their four notes files, at the root under the names the prompt uses.
- `RGLUE_DICTIONARY_20261112.md` at the root.

**Scans:**
- Cote 140-2: 6–18, 103–109, 119–137, 160–179, 233–250 and 259 (78 images).
- Cote 147: scans 106–190 (85 pages).
- Cote 149: scans 1–22, 51–53 and 128–136 (34 pages). This is the WHAT IS ATTACHED list, which is wider than the ZIP_LIST's 3–4 and 18–22.
- The 147 and 149 images come with their halves `_a` and `_b`, under `scans/147/` and `scans/149/`.
- The ZIP_LIST said to extract the 147 and 149 pages from `147.pdf` and `149.pdf`. They were taken instead from the packages' scans zips (`packages_done\…_scans.zip`). These hold the same pages, since scan n is PDF page n (`DROPPED_SCANS_CHECK_20261112.md`), and they are the images the transcriptions were made from.

**Added:**
- `context/` files, as for LM4.
- `papers/`: two background papers named in BACKGROUND.md that are available locally:
  - Ørsnes Jansen arXiv:2308.09551v2 (the PDF from the LM3 zip)
  - Deligne 1989 (from the literature store)
- The Douteau–Waas paper (arXiv:2112.02394) exists locally only as LaTeX source inside the 5_STRATA zip. That source contains the authors' e-mail addresses, so it was not included.

**Current text used where the row named an older file:** P04, P05 and P046, as for LM4.

**Left out:**
- `STRUCTURE.txt` (NOT FOR THE ZIP).
- The other papers of BACKGROUND.md are not local and are not in the ZIP_LIST: SGA 1 V, SGA 4, Moerdijk, Bunge, Bunge–Moerdijk, Leroy, Dubuc, Stix 2006, Illusie, Talpo–Vistoli, CSST, Artin–Mazur, Hoyois, Lurie, Breen, Kneser, Smale, Morel–Voevodsky.

**Mismatch with the prompt:**
- `STRATA_review/REVIEW_author.md` and `PATHS_review/REVIEW_author.md` are named in the blocks "After STRATA" and "After PATHS" but are not attached, for the same reason as in LM4.

## LM6_POINTS_AS_SECTIONS: ready (two attachments the prompt makes conditional are not yet available)

- **Upload folder:** `..\pro_prompts_draft_20261111\LM6_POINTS_AS_SECTIONS\`
- **Zip:** `LM6_POINTS_AS_SECTIONS_background.zip`, 181,631,957 bytes (181.6 MB), 647 files.

**Rows included (136 of 143):**
- `PROMPT.md`, `context/BACKGROUND.md` and `context/OVERVIEW.md`.
- In `longue_marche/`: packages P01–P058 (cote 140-2) and LM_C4-001-019 to LM_C4-267-280 (cote 140-4), each with its current text and notes (146 files).
- `LM3_return/` and `LM3b_return/`, without code or audit.
- `LM3_review/REVIEW.md` and `LM3b_review/REVIEW.md`.
- `LM_EXPERT_notes/`: FINDINGS, HUNCHES, LIT_LM6_anabelian and LIT_LM6_sections.
- `literature/`: 41 papers from the literature store in `literature/<slug>/`, plus the three OpenAI 2026 papers (019 ×2, 031) at `literature/`.
- At the root:
  - the two cote 149 transcriptions and their notes
  - `R149_WARGAME_EXCERPTS_20261112.md` and `R149_NOTES_20261112.md`

**Scans:**
- Cote 140-2: 19–67, 69–88, 109–115, 132–151, 348, 377–378, 395–471 and 480–490 (187 images).
- Cote 140-4: 166–178 (13 images). BACKGROUND.md asks for 166–178; the prompt cites 172–178.
- Cote 149: 44–103 and 125–127, with halves (63 pages).
  - This covers the WHAT IS ATTACHED list and the ZIP_LIST members.
  - It also covers every scan of cote 149 that the block on cote 149 and Part F cite, including the ranges 64–99 and 85–95.

**Current text used where the row named an older file:**
- P04, P05 and P046.
- LM_C4-134-152 to LM_C4-267-280 now have `second_pass\…_checked.tex`; the rows named `answers\unzipped`.

**Left out:**
- `STRUCTURE.txt` and `CHANGES_R149_20261112.md`, both marked NOT FOR THE ZIP.
- Three rows marked NOT LOCAL that are still not local:
  - Bresciani arXiv:2108.13397 and Bresciani, Invent. Math. 235 (2024)
  - Schmidt–Stix, Ann. of Math. 184 (2016)
  - Ribet's appendix to Katz–Lang (1981)
- `CYCLOTOMIC_KERNEL_return/` and `FLAGGED_149_return/` (PENDING): neither prompt has been answered. The prompt makes these two conditional ("if they have been answered").

**Mismatch with the prompt:** none beyond the conditional returns.

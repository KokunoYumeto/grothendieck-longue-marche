# Packaging report, 12 November 2026: EXIT_ONE_TYPE, EXIT_TOWER, CYCLOTOMIC_KERNEL, FLAGGED_149

Packaged by Claude Opus 5.5. This was packaging only. No PROMPT.md, BACKGROUND.md or mathematics was edited. The upload folders were created under `..\pro_prompts_archive_20261112\<NAME>\`. Each holds exactly `PROMPT.md` (a byte-identical copy of the work folder's) and `<NAME>_background.zip`. Each folder is flat, has 2 files and has one zip under 500 MB, so no zip was split.

- **Builder:** `C:\Users\user\Documents\longue_marche_pro_pilot_20261104\pro_prompts_draft_20261111_work\package_20261112.py`. Its layout follows the earlier Longue Marche zips:
  - `MANIFEST.tsv` sits at the root, with columns `path_in_zip`, `source_path_or_url`, `sha256`, `bytes` and `note`.
  - Returns go in `<X>_return/` and reviews in `<X>_review/`, exactly as the prompts name them.
  - Literature goes in `literature/<slug>/`.
  - The files the prompts name by bare filename are at the root: `PROMPT.md`, `BACKGROUND.md`, `RGLUE_DICTIONARY_20261112.md`, the `MPL_…_transcription.tex` and `_notes.md` files, and the R149 files.
- **Copy of the manifest:** `<NAME>/MANIFEST_20261112.tsv` in each work folder.
- **Scans:**
  - The Montpellier scans are under `scans/` with their package names, `MPL_<cote>_<range>_scanNNN.jpg`, plus the halves `_a` and `_b`. They were taken from the packages' scans zips in `grothendieck_archive_transcription_20261110\packages_done\`.
  - Where a ZIP_LIST row said to extract pages from `147.pdf` or `146.pdf`, the package scans zips were used instead. These are the same pages, since scan n is PDF page n (`DROPPED_SCANS_CHECK_20261112.md`), and they are the images the transcriptions were made from.
  - Longue Marche scans are under `scans/140-2/scanNNN.jpg`.
- **Checks run on every zip:**
  - `testzip` passed.
  - All names are ASCII.
  - No e-mail addresses or key/token patterns appear in any text member.
  - No file comes from the Obsidian notes folder.
  - Nothing was written to any `outbox/` or writers' `outputs/` folder.
- **Returns that do not exist yet:** none of EXIT_ONE_TYPE, CYCLOTOMIC_KERNEL or FLAGGED_149 has been answered. Neither `longue_marche_pro_pilot_20261104\answers\` nor `grothendieck_archive_transcription_20261110\returns\` holds a return for any of them.

## EXIT_ONE_TYPE: ready

- **Upload folder:** `..\pro_prompts_archive_20261112\EXIT_ONE_TYPE\`
- **Zip:** `EXIT_ONE_TYPE_background.zip`, 119,465,545 bytes (119.5 MB), 304 files.

**Rows included (all 20):**
- At the root:
  - `PROMPT.md` and `BACKGROUND.md`
  - `RGLUE_DICTIONARY_20261112.md`
  - `MPL_147_048-137_transcription.tex`, `MPL_147_138-190_transcription.tex` and `MPL_149_091-136_transcription.tex`, with their three notes files
- `STRATA_return/`: `sections/A.tex`, `B.tex`, `C.tex`, `F.tex`, `00_conventions.tex`, `STRATA_results.csv` and `STRATA_paper.pdf`.
- `RESIDUE_return/sections/H.tex`.
- `BISITE_return/sections/F.tex`.

**Scans:**
- Cote 147: 60 and 106–190 (86 pages).
- Cote 149: 128–136 (9 pages).
- With halves, 285 images. These cover WHAT IS ATTACHED and every scan the prompt cites.

**Left out:** nothing.

**Mismatch with WHAT IS ATTACHED:** none.

**The EXIT_ONE_TYPE return** is not a row of this prompt. It is the missing row of EXIT_TOWER (below).

## EXIT_TOWER: ready to send without the EXIT_ONE_TYPE return, which the prompt attaches only "if [it] exists"

- **Upload folder:** `..\pro_prompts_archive_20261112\EXIT_TOWER\`
- **Zip:** `EXIT_TOWER_background.zip`, 109,842,235 bytes (109.8 MB), 387 files.

**Rows included (27 of 28):**
- At the root:
  - `PROMPT.md` and `BACKGROUND.md`
  - `RGLUE_DICTIONARY_20261112.md`
  - the transcriptions of 147 (048-137, 138-190) and of 146 (001-099, 100-134), with their four notes files
- `STRATA_return/`: `sections/C.tex`, `F.tex`, `00_conventions.tex`, the register and the paper.
- `RESIDUE_return/`: `sections/H.tex`, `RESIDUE_results.csv` and `code/` (77 files, including `GHIJ/marked_curve_lifts.py`).
- `BISITE_return/sections/F.tex`.
- `LM3_return/` and `LM3b_return/`, from the answer zips without `code/` or `audit/`.
- `LM3_review/REVIEW.md` and `LM3b_review/REVIEW.md`.

**The row "the Longue Marche packages containing scans 348 and 399" was resolved to cote 140-2, not 140-3:**
- LM3b cites "§30; folio 176; scan 348; §33 bis; folio 202; scan 399" in its results register.
- Those folios are in the cote 140-2 packages:
  - LM_P035 (scans 341–350) carries `\mspage{176}`.
  - LM_P040 (scans 391–400) carries scan 399 as `\mspage{202}`, with the "??" that B.5 is about.
- No cote 140-3 package has those folios.
- Attached:
  - `longue_marche/LM_P035/LM_P035_checked_fixed.tex` and `LM_P035_notes_checked.md`
  - `longue_marche/LM_P040/LM_P040_checked_fixed.tex` and `LM_P040_notes_checked.md`
  - `scans/140-2/scan348.jpg` and `scan399.jpg`

**Scans:**
- Cote 147: 56–105, 135, 150–152 and 176–180 (59 pages).
- Cote 146: 90–110 (21 pages asked for, 19 attached).
- With halves, 236 images, including the two 140-2 scans.
- Cote 146 scans 102 and 105 are blank sheets: show-through and an archive folio only. The 146 package left them out (`DROPPED_SCANS_CHECK_20261112.md`), so they are not in the zip.

**Left out:**
- "TO BE ADDED WHEN IT EXISTS: the return of EXIT_ONE_TYPE" (`EXIT_ONE_TYPE_return/`). EXIT_ONE_TYPE has not been answered. There are two options:
  - send EXIT_TOWER now without it, which the prompt allows ("If the return of EXIT_ONE_TYPE exists when this is sent, it is attached")
  - wait for EXIT_ONE_TYPE to return and rebuild with `package_20261112.py EXIT_TOWER` after adding the row

**Mismatch with WHAT IS ATTACHED:** none except the conditional `EXIT_ONE_TYPE_return/`.

## CYCLOTOMIC_KERNEL: ready

- **Upload folder:** `..\pro_prompts_archive_20261112\CYCLOTOMIC_KERNEL\`
- **Zip:** `CYCLOTOMIC_KERNEL_background.zip`, 34,808,659 bytes (34.8 MB), 134 files.

**Rows included (23 of 27):**
- At the root:
  - `PROMPT.md`
  - the two cote 149 transcriptions and their two notes files
  - `R149_WARGAME_EXCERPTS_20261112.md` and `R149_NOTES_20261112.md`
- `literature/`: 9 papers (Stix cuspidal, Nakamura 1994, the letter to Faltings, Esnault–Hai, Mochizuki 2004, Mochizuki 1999, Tamagawa 1997, Hoshi–Mochizuki, Belyi).
- `LM_EXPERT_notes/FINDINGS.md`.
- `LM3_return/`: the report, the register and `sections/D.tex`, as the row says.
- `LM3b_return/`: the report, the register and section D, which is `sections/DG.md` with its `DG_report.md`, `DG_results.csv`, `DG_readings.csv` and `DG_refs.bib`.
- `LM3_review/REVIEW.md` and `LM3b_review/REVIEW.md`.

**Scans:**
- Cote 149: 13–15, 22, 32, 44–66 and 126–131 (34 pages, with halves). The ZIP_LIST members, plus the scans the prompt cites that the ZIP_LIST lacked: 13–15, 22, 32, 46–47, 50–52, 58, 64–65.
- Cote 140-2: 433 and 483. The prompt cites these Longue Marche scans by number (the "peut-être même" of scan 433; the conjecture of §34, scan 483).
- 104 images in all.

**Left out:**
- `BACKGROUND.md` (NOT FOR THE ZIP).
- Three rows marked NOT LOCAL that are still not local:
  - Ribet's appendix to Katz–Lang (1981)
  - Tsujimura, Adv. Math. 435 (2023) and arXiv:2501.11277
  - Zarhin, Duke Math. J. 54 (1987)

**Mismatch with WHAT IS ATTACHED:** none.

## FLAGGED_149: ready (the CYCLOTOMIC_KERNEL return, which the prompt attaches only if answered, is not yet available)

- **Upload folder:** `..\pro_prompts_archive_20261112\FLAGGED_149\`
- **Zip:** `FLAGGED_149_background.zip`, 70,993,574 bytes (71.0 MB), 237 files.

**Rows included (23 of 26):**
- At the root:
  - `PROMPT.md`
  - the two cote 149 transcriptions and their notes
  - `MPL_142_001-093_transcription.tex` and its notes
  - the two R149 files
- `literature/`: 10 PDFs. These are 6 named files plus the PDF of each of the four named folders (Earle–Eells, Yagasaki, Kerckhoff, Constantin–Kolev). The `.txt` extractions beside them were not taken.
- `LM_EXPERT_notes/FINDINGS.md`.

**Scans:**
- Cote 149: 13–15, 21, 24–40, 45, 52, 54, 65, 70–72, 74–83, 85, 90, 93–95, 100–103, 116, 119–120, 122–124, 126–127, 130–131 and 133–135 (60 pages). The ZIP_LIST members, plus the scans the prompt cites in rows F1–F26 and Parts A–E that the ZIP_LIST lacked.
- Cote 142: 3–14 (12 pages).
- With halves, 216 images.

**Left out:**
- `BACKGROUND.md` (NOT FOR THE ZIP).
- One row marked NOT LOCAL that is still not local: Carlson–Haine–Wolf arXiv:2407.19920 and Carlson–Stix arXiv:2410.22474.
- `CYCLOTOMIC_KERNEL_return/` (PENDING): CYCLOTOMIC_KERNEL has not been answered.

**Mismatch with WHAT IS ATTACHED:** none. The prompt makes the CYCLOTOMIC_KERNEL return conditional.

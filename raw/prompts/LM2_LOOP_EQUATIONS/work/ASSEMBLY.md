# ASSEMBLY of LM2_LOOP_EQUATIONS_background.zip

155 files, 34,934,413 bytes zipped (hash and per-file SHA-256 in `MANIFEST.tsv`). Built 11 Nov 2026 from BACKGROUND.md (10 Nov 20:35), `BACKGROUND_ADD.md` and `CHANGES_20261110.md` (both 11 Nov 00:17).

## In the zip
- `longue_marche/`: 28 packages, text and notes: LM_P050-P056, LM_P057api, LM_P058, LM_P059-P067, LM_P068-069, LM_P070-071, LM_C3-131-149 to LM_C3-264-282 (eight packages). Text and notes: `longue_marche/<KEY>/`, current text by the rule (`checked_fixed` > `checked` > `answers\fixed` > `answers\unzipped`), notes = `_notes_checked.md`. Every returned text is a second-pass `_checked.tex` or `_checked_fixed.tex`; no first-pass-only package occurs. LM_P060: the checked text `LM_P060_checked.tex` (no `_fixed` exists) with `LM_P060_notes_checked.md`. (BACKGROUND.md says "LM_P050-P058"; the manuscript package for scans 561-570 is keyed `LM_P057api`.)
- `longue_marche/LM_P060_first_pass_returns/`: both first-pass returns (transcription and notes of each): `return_1_earlier/` = `answers\LM_P060.zip` (identical to `answers\unzipped\LM_P060`; zip time 6 Nov 15:51) and `return_2_later/` = `answers\LM_P060(1).zip` (zip time 6 Nov 16:14).
- `context/source_of_record_audit_longue_marche.md`: `SOURCE_OF_RECORD_AUDIT_20261110\sections\longue_marche.md` (the open LM_P060 question is finding (1) of its OPEN list; BACKGROUND.md calls it "item 2"), `context/GLOBAL_PASS.md` (T7, T8), the table of contents, `context/OVERVIEW.md`, `context/second_pass_corrections.md` (4 card lines: C3-207-225, C3-226-244, C3-245-263, C3-264-282).
- `scans/140-3/` (scans 9-10, 11-20 (LM_P060), 54-57, 85, 120, 155, 170, 178, 185, 204-205, 209-217, 226-245) and `scans/140-2/` (505, 511-524). Scans: the main `scanNNN.jpg` of each listed scan only (the `_a`/`_b` half-page crops in the `img*` folders are not included); named `scans/<cote>/scanNNN.jpg`. No zip passed 150 MB, so no image was re-saved; all are the original JPEGs.
- `proof_packs/008_The-Deligne-Drinfeld-conjecture-/`: the manuscript PDF and `PACK.md`, and `lean/008.md` and `lean/DeligneDrinfeld.lean` fetched from raw.githubusercontent.com/openai/math (BACKGROUND_ADD.md). The Lean file was only read as text, never run.
- `papers/` (18 files): Drinfeld (Russian original, mathnet.ru); Ihara ICM 1990 (pp. 99-120 cut from the volume); Schneps GT^ survey; Lochak-Schneps Invent. 127; Nakamura-Schneps Invent. 141; Belyi (Russian original and English translation); Conrad SL(2,Z); Raghunathan, *The congruence subgroup problem* (arXiv math/0503088, PDF and source); Guillot (PDF and source); Bleher-Chinburg-Lubotzky (PDF and source); Hain-Matsumoto (PDF and source); Brown (PDF and source).

## Identifiers resolved for "(m)" entries
- Guillot, *The Grothendieck-Teichmuller group of a finite group and G-dessins d'enfants*: arXiv:1407.3112 (v3) is correct.
- Bleher-Chinburg-Lubotzky (optional entry): arXiv:2004.08860 *On representations of Gal(Qbar/Q), GT^ and Aut(F^_2)*, found by author search.
- From BACKGROUND_ADD.md: Hain-Matsumoto (Compositio 139 (2003)) = arXiv:math/0006158v2 (the free version); Brown, *Mixed Tate motives over Z* = arXiv:1102.1312.

## Left out, and why
- Cote 140-1 packages LM_C1-001-019, LM_C1-020-037: no second pass exists ("when their second pass exists").
- Papers not fetched (at the end of `MANIFEST.tsv`): Drinfeld's English translation; Ihara, *On the embedding* (1994); Nakamura, *Limits of Galois representations ... I* (Project MUSE); Nakamura, *On Galois rigidity* (CUP); Serre, *Arbres, amalgames, SL_2* (Conrad and Raghunathan included instead).

## Mismatches between BACKGROUND.md and the disk
- BACKGROUND.md "LM_P050-P058" vs. key `LM_P057api` (above). Otherwise every listed text, note and scan exists.

Downloads were made with a generic User-Agent, each into its own subfolder of `_downloads\` in this prompt folder; nothing from them was run; the arXiv `*_source.gz` files are the gzip files exactly as served (not unpacked). Shadow libraries were not used.

# ASSEMBLY of LM1_GROUP_SCHEMES_background.zip

153 files, 67,125,807 bytes zipped (hash and per-file SHA-256 in `MANIFEST.tsv`). Built 11 Nov 2026 from the BACKGROUND.md of 10 Nov 20:35 (unchanged since) and `CHANGES_20261110.md` (it says no BACKGROUND_ADD.md is needed).

## In the zip
- `longue_marche/`: 28 packages, text and notes: LM_C3-131-149, LM_C3-150-168, the 23 packages LM_C3-264-282 to LM_C3-682-696, LM_C4-001-019, LM_C4-020-038, LM_C4-039-057 (56 files). Text and notes: `longue_marche/<KEY>/`, current text by the rule (`checked_fixed` > `checked` > `answers\fixed` > `answers\unzipped`), notes = `_notes_checked.md`. Every returned text is a second-pass `_checked.tex` or `_checked_fixed.tex`; no first-pass-only package occurs.
- `scans/140-3/` (50 scans: 151, 259, 264-271, 321-324, 336, 358, 370, 393, 399, 441, 479-480, 489, 546, 596-611, 626-634, 652) and `scans/140-4/` (27 scans: 3-16, 29-41). Scans: the main `scanNNN.jpg` of each listed scan only (the `_a`/`_b` half-page crops in the `img*` folders are not included); named `scans/<cote>/scanNNN.jpg`. No zip passed 150 MB, so no image was re-saved; all are the original JPEGs.
- `context/second_pass_corrections.md`: the 26 board-card lines (23 C3 packages from 264 and C4-001, C4-020, C4-039), verbatim; `context/GLOBAL_PASS.md` (T9, T10 are the topics named; the whole file is included), `context/table_of_contents_Grothendieck_Circle_tableLM.txt`, `context/OVERVIEW.md`.
- `papers/` (16 files): SGA 3 Exposes VIII, IX, X, XI, XII, XXII, XXIII (Polo's re-edition PDFs); Lazard, Deligne (Extensions centrales), Brylinski-Deligne (Numdam); Milne, Algebraic Groups and Class Field Theory (author's notes); K. Conrad's SL(2,Z) notes; Hain-Matsumoto (PDF and arXiv source); Bhargava, P-orderings (JAMS 2009).

## Left out, and why
- The output of LM2_LOOP_EQUATIONS (Part A dictionary): does not exist yet ("if available").
- Card lines for LM_C3-131-149 and LM_C3-150-168: the BACKGROUND asks for them only for C3 from 264 and C4-001 to C4-057.
- Papers not fetched (links and reasons at the end of `MANIFEST.tsv`): Serre, *Arbres, amalgames, SL_2* (book); Hochschild-Mostow (JSTOR); Kostant, *Groups over Z* (AMS login wall); Deligne 1989 section 9 (Springer); Cahen-Chabert Monthly survey. Substitutes included: Conrad (the amalgam), Hain-Matsumoto (pro-algebraic hull and Malcev completion), Bhargava (integer-valued polynomials).
- No "(m)" entries occur in this BACKGROUND.md.

## Mismatches between BACKGROUND.md and the disk
- None in the manuscript part: every listed package, text, notes and scan exists. BACKGROUND.md says "as in LM4_FINITE_GROUP_ACTIONS\BACKGROUND.md" for the root and the text rule; that file was used.
- The choice of Hain-Matsumoto over Deligne section 9 and of Bhargava over "Cahen-Chabert's surveys" is mine (BACKGROUND.md says "record which").

Downloads were made with a generic User-Agent, each into its own subfolder of `_downloads\` in this prompt folder; nothing from them was run; the arXiv `*_source.gz` files are the gzip files exactly as served (not unpacked). Shadow libraries were not used.

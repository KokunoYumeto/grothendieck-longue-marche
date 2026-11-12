# Scans dropped as "blank" by the packager: check of 12 Nov 2026

All 31 scans that the packager left out as blank (`skipped_blank` in the manifests) were rendered from the archive PDFs and checked by eye on high-contrast grayscale images.

**Result: 3 carry Grothendieck's writing, 28 are blank, none is another document.** All three with writing are in packages that have already been returned. None of the scans in the packages still waiting to be sent needs to go back in.

## Method

- **Scan numbering.** Scan n is PDF page n. This was checked against `packages_work/MPL_142_001-093/MANIFEST.json` and the zip of that package: the package's `scan022` and `scan024` match PDF pages 22 and 24. Scan 23 is the page missing between them. The page counts of all nine PDFs match the manifests: 1: 150, 5: 53, 6: 67, 7: 72, 8: 81, 16: 56, 100: 53, 142: 122, 146: 134.
- **Rendering.** Each scan was rendered with PyMuPDF at 110 dpi in grayscale, with a histogram stretch: the 0.5th percentile goes to black, the 60th percentile (the paper) to white, then gamma 2.2. The images are in `DROPPED_SCANS_CHECK_work\<cote>_<scan>.png`. Unclear areas were looked at in crops of up to 500 dpi.
- **Show-through.** Faint text on a scan was compared with the neighbouring scans, both as it is and mirrored (`neighbours.py`). On every scan below where this was checked, the faint text matches a neighbouring page. Usually the match is unmirrored, with the next scan: the archive photographed each sheet from above, and the writing on the sheet underneath shows through. On three scans it matches the scan before; on 8/33 it is the mirrored back of the typed page on scan 32.
- **Archive folio numbers.** Every sheet has a pencil number at the bottom left. This number is the archive's own running count of the sheets, not Grothendieck's page number. On cotes 142, 146, 5, 7, 8, 16 and 100 it equals the number the archive prints under the image on the PDF page (scan n carries n−1). On cotes 1 and 6 it runs ahead of that number in places (for example 6/58 carries "68"), but it is in the same hand and the same position. Grothendieck's own page numbers are a circled number at the top: for example, 142 scan 24 carries his "(5)" at the top and the archive's "23" at the bottom left. A scan whose only mark is this folio number was therefore classed as blank, under the rule that an archive mark alone counts as blank.

## Table

| Cote | Scan | Class | What is on it | Reading | Package (status) |
|---|---|---|---|---|---|
| 1 | 2 | blank | archive folio "1"; a hair or fibre on the scanner glass (the same curl is on scans 43 and 47) | — | MPL_1_002-050 (returned) |
| 1 | 37 | blank | archive folio "38" only | — | MPL_1_002-050 (returned) |
| 1 | 43 | blank | faint show-through of a manuscript page, too faint to read; folio "44"; scanner hair | — | MPL_1_002-050 (returned) |
| 1 | 47 | blank | faint show-through of a manuscript page, too faint to read; folio "48"; scanner hair | — | MPL_1_002-050 (returned) |
| 142 | 23 | **writing** | his note on the number of pages, top left, in pencil; archive folio "22" | "pages 5 à 23 (= 19 pages)" | MPL_142_001-093 (returned) |
| 142 | 43 | **writing** | his page-count note, top left, in pencil; archive folio "42" | "22 pages" | MPL_142_001-093 (returned) |
| 142 | 65 | blank | archive folio "64" only; nothing else at 150 dpi, top half and bottom half each checked | — | MPL_142_001-093 (returned) |
| 146 | 26 | blank | show-through of scan 27 (the table of "≃ R" relations); folio "25" | — | MPL_146_001-099 (returned) |
| 146 | 35 | blank | show-through of scan 36 ("Lemme 1 …"); folio "34" | — | MPL_146_001-099 (returned) |
| 146 | 42 | blank | show-through of scan 43 ("Soit n un entier ≥ 3 …"); folio "41" | — | MPL_146_001-099 (returned) |
| 146 | 57 | blank | archive folio "56" only | — | MPL_146_001-099 (returned) |
| 146 | 70 | blank | show-through of scan 71 ("⊗L_i = L_K" and a table); folio "69" | — | MPL_146_001-099 (returned) |
| 146 | 76 | blank | show-through of scan 75 (formulas (41), triangle, polygon); folio "75" | — | MPL_146_001-099 (returned) |
| 146 | 79 | **writing** | his cover-sheet note: a page count top left in pencil, a title top right in ink; archive folio "78" | "(19 p)" … "Groupoïdes" | MPL_146_001-099 (returned) |
| 146 | 80 | blank | archive folio "79" only | — | MPL_146_001-099 (returned) |
| 146 | 88 | blank | archive folio "87" only | — | MPL_146_001-099 (returned) |
| 146 | 102 | blank | show-through of scan 103 ("Le fibré SP_G …"); folio "101" | — | MPL_146_100-134 (returned) |
| 146 | 105 | blank | show-through of scan 104 (the SP_G diagrams); folio "104" | — | MPL_146_100-134 (returned) |
| 16 | 2 | blank | show-through of scan 3; folio "1" | — | MPL_16+47+54+44 (waiting, packages\11) |
| 16 | 24 | blank | show-through of the typed page on scan 23; folio "23" | — | MPL_16+47+54+44 (waiting, packages\11) |
| 5 | 2 | blank | show-through of scan 3 (the X_zar … diagram); folio "1" | — | MPL_5+6_001-037 (waiting, packages\30) |
| 6 | 39 | blank | show-through of a manuscript page ("Lemme", "H¹(G, R_L)"), not of the grey cover sheets on scans 38 and 40, so the source page is not identified; folio "38" | — | MPL_6_038-067+7_001-060 (waiting, packages\31) |
| 6 | 58 | blank | show-through of scan 59 ("Compléments sur les groupes de W_n"); folio "68" | — | MPL_6_038-067+7_001-060 (waiting, packages\31) |
| 6 | 64 | blank | show-through of scan 65; folio "74" | — | MPL_6_038-067+7_001-060 (waiting, packages\31) |
| 7 | 2 | blank | show-through of scan 3 ("Anneaux … stratifiés …"); folio "1" | — | MPL_6_038-067+7_001-060 (waiting, packages\31) |
| 7 | 20 | blank | faint show-through of scan 21; a paper-clip mark at top right; folio "19" | — | MPL_6_038-067+7_001-060 (waiting, packages\31) |
| 8 | 24 | blank | show-through of scan 25 ("Groupe de Barsotti-Tate …"); folio "23" | — | MPL_7_061-072+8_001-078 (waiting, packages\32) |
| 8 | 28 | blank | show-through of scan 29; folio "27" | — | MPL_7_061-072+8_001-078 (waiting, packages\32) |
| 8 | 33 | blank | the back of the typed page on scan 32, whose text shows through mirrored; folio "32" | — | MPL_7_061-072+8_001-078 (waiting, packages\32) |
| 8 | 77 | blank | show-through of scan 78; folio "76" | — | MPL_7_061-072+8_001-078 (waiting, packages\32) |
| 100 | 47 | blank | faint show-through of typed lines at the top; folio "46" | — | MPL_8_079-081+9+4+100 (waiting, packages\33); also listed as skipped in packages_work\MPL_100_047-053 |

## Counts

| Class | Count |
|---|---|
| writing | 3 (142/23, 142/43, 146/79) |
| blank | 28: 7 carry the archive folio only (one of them, 1/2, also a scanner hair); 21 carry show-through |
| other document | 0 |
| **total** | **31** |

On 142/65: the scan shows no writing other than the archive folio "64", although 65 was listed as "known to carry writing". The page was checked at 150 dpi in two halves.

## Scans to restore

**Packages already returned: a small top-up package later**

- 142, scan 23: "pages 5 à 23 (= 19 pages)" (from MPL_142_001-093)
- 142, scan 43: "22 pages" (from MPL_142_001-093)
- 146, scan 79: "(19 p)" … "Groupoïdes", a cover sheet (from MPL_146_001-099)

**Packages waiting to be sent: back into their package**

- None. All 13 dropped scans in cotes 5, 6, 7, 8, 16 and 100 are blank or show-through.

Nothing in the packages, manifests or packager was changed.

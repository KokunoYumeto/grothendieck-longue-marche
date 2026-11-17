# Typesetting audit

Checkpoint02 PDF: 99 pages; 26 rendered pages visually inspected. SHA-256: `007d81bee43f882da0327d3ebad9b5d73b081ac158229b840f2d8b1474085f8a`.

The first complete source pass had 6 overfull boxes above 2 pt, maximum 16.97998 pt: part_a_lifting A.L6; part_a_cm A.C11; part_a_harmonic A.J2; part_b_arrows subgroup definitions and B5.5; and the long eight-root list in part_c_results. Each was repaired in the source by splitting a display or allowing the numerical list to break.

Later additions exposed 2 further displays above 2 pt: the integral localization diagram (12.09682 pt) and the class-three Hall coordinate tuple (42.64426 pt). Both were split in the source. These were separate later source passes, not eight simultaneous errors in one final build.

Final LuaLaTeX pass: **0 overfull boxes**, **0 above 2 pt**, no undefined references, no missing citations and no multiply-defined labels. There are three underfull paragraph diagnostics; the affected pages remain legible and within margins. BibTeX and all three LuaLaTeX passes exit successfully. Full logs are in notes/build/ and the root .log file.

Poppler rendered the following pages at 105 dpi, and root opened and visually inspected every listed full page: 1, 11, 14, 21, 29, 30, 32, 33, 34, 40, 50, 60, 64, 65, 67, 70, 73, 74, 75, 79, 86, 87, 89, 90, 95, 99.

These include every formerly overflowing region (including the root list on page 75), all new table and tuple regions selected by the script, and an eleven-page sample spread across the document. No clipping, overlapping equation labels, missing glyphs, or unreadable displays was observed. The twelve-row finite cubic certificate on page 40 and the 24-element section fibre on page 95 were also explicitly checked. The manifest records the exact PDF hash and observations; rendering alone was not counted as visual inspection.

The earlier source-only checkpoint contained no unchecked PDF. It is retained unchanged.


## Checkpoint03, third-hour audit

The integrated PDF has 139 pages and 1101480 bytes. Its SHA-256 is `a89000c9b466bc32b636a0927afc8669cdb35d9f62a3346e0fa6f1f6fd7d2b53`.

Three subsequent third-hour source additions exposed overfull boxes of 59.3618 pt (the two B.M1 quotient maps), 89.49585 pt (the six simultaneous core conditions in B.C22), and 72.74455 pt (the long normalization-program filename). The maps and core conditions were split into aligned lines; the filename now permits line breaks through the path macro. The missing display closer in B.N6 and an extra alignment separator in the elliptic condition were also repaired before the clean build. These diagnostics arose in different intermediate passes, not simultaneously in the final pass.

The final LuaLaTeX log has zero overfull boxes, zero above 2 pt, no unresolved references, no missing citations and no duplicate labels. BibTeX and all three final LuaLaTeX passes completed successfully. Seven underfull diagnostics remain; the affected content is legible and within the page margins.

Poppler rendered 63 selected pages at 105 dpi. Every selected full PNG was actually opened and visually inspected. Root inspected 22 pages, the centralizer auditor 22 pages and the ghost auditor 19 pages. This includes every repaired region and an eleven-page spread sample. There is no clipping, overlapping equation tag, damaged glyph or unreadable display. The exact page lists, individual observations and the PDF hash are in the completed manifest.

Pages: 1, 14, 15, 29, 32, 33, 34, 41, 42, 43, 44, 45, 46, 47, 48, 49, 56, 62, 63, 64, 65, 66, 70, 74, 75, 76, 77, 78, 79, 80, 81, 82, 84, 85, 86, 87, 89, 95, 96, 97, 98, 108, 109, 111, 112, 117, 118, 119, 120, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 139.


## Checkpoint04, fourth-hour audit

The integrated PDF has 185 pages and 1401560 bytes. SHA-256: `de627f7e907b923dfa2b9d70994a66561d0fc6a01514dccd17263b87b899769b`. It contains 103 numbered statements: 88 Proved, 2 Known and 13 Open.

The first fourth-hour pass exposed a 3.60463 pt overflow in a long theorem-heading paragraph; the paragraph was rephrased. An illegal tag placement in an aligned display and a missing display closer in B.R12 were repaired. B.Q10 and B.R19 were split into separate lines before final review. These intermediate failures are recorded as repairs; their partial PDFs are not deliverables.

The final BibTeX run and all three LuaLaTeX passes succeeded. The final log has zero overfull boxes, zero above 2 pt, no unresolved references, no missing citations and no duplicate labels. There are 10 underfull diagnostics; visual inspection found the content legible and within margins.

All 87 selected full PNGs were actually opened and visually inspected: root 22 pages, tower auditor 22, centralizer auditor 22, and ghost auditor 21. New proof regions, all formerly repaired display regions and an eleven-page spread sample are included. A provisional concern about FD.9 was resolved by reopening page 178 singly: the equation tag is at the right margin with clear separation. Root also independently opened that page and confirmed the placement. No clipping, overlapping text, damaged glyphs or unreadable display was found.

Pages: 1, 14, 15, 19, 29, 30, 33, 34, 35, 38, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 56, 73, 75, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 104, 105, 106, 107, 108, 109, 110, 111, 112, 119, 120, 121, 130, 132, 133, 135, 136, 141, 148, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 185.


## Checkpoint05, fifth-hour audit

The frozen integrated PDF has235 pages and1730437bytes. SHA-256: `ede3897e5dd2a50d941b4cf5eaf2c4e73f849330a7b1ad833f47b063c37e41e7`. It contains128 numbered statements:113Proved,2Known,13Open.

Fifth-hour intermediate additions exposed two overfull tables:91.36694pt in B.S36 and62.89728pt in B.S42. Both were repaired by splitting the column headings into stacked lines in the proof source. An improper paragraph-depth error in the surface-realization proof was repaired by replacing the heading command with an ordinary spaced bold paragraph. QD.2 was put in a correctly nested aligned environment. These changes affect layout, with the mathematical displays retained.

The final BibTeX run and all three LuaLaTeX passes succeeded. The final log has zero overfull boxes, zero above2pt, no unresolved references, no missing citations and no duplicate labels. It has11 underfull diagnostics. The completed visual-inspection record follows below.

All99 selected full-page PNGs were actually opened and visually inspected at105dpi: root26, tower auditor25, centralizer auditor24, ghost auditor24. Every selected fifth-hour proof region, every repaired display and an eleven-page spread sample are included. Root additionally inspected the actual covering square ASR.19 on page60. There is no clipping, overlapping equation tag, damaged glyph or unreadable display.

Pages: 1, 15, 24, 30, 33, 34, 35, 42, 43, 44, 45, 46, 47, 48, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 95, 96, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 118, 119, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 145, 148, 149, 151, 158, 159, 160, 165, 171, 172, 174, 175, 180, 188, 212, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 235.


## Checkpoint06

Checkpoint06 has 271 pages, zero overfull boxes and no unresolved references or citations. All 95 selected full-page PNGs were opened and visually inspected. No clipping, overlap, damaged glyphs or unreadable displays were found. The PDF SHA256 is 6dafe83fa80ffec05042c68f9cb9a13e4223961ccf563b27e561f723f3311a92. The exact source/build hashes, individual page observations and PNG hashes are retained in the build and visual-audit manifests.

Inspector counts: {'root': 24, 'tower': 24, 'centralizer': 24, 'ghost': 23}.


## Checkpoint07

The seventh-hour first complete build had two overflows greater than2pt, of10.81139pt and129.59485pt, and one smaller1.3854pt paragraph overflow. The source display, breakable filenames and paragraph map were repaired. A later newly integrated proof had a missing math delimiter; that failed build and every subsequent build log are retained. The final three-pass build has zero overfull boxes. Checkpoint07 has 310 pages, zero overfull boxes and no unresolved references or citations. All 101 selected full-page PNGs were opened and visually inspected. No clipping, overlap, damaged glyphs or unreadable displays were found. The PDF SHA256 is ddc2b4623e3565442139392d1154ac179c5e080cac683701db14fbc125c893f2. The exact source/build hashes, individual page observations and PNG hashes are retained in the build and visual-audit manifests.

Inspector counts: {'root': 26, 'tower': 25, 'centralizer': 25, 'ghost': 25}.


## Checkpoint08

The first eighth-hour build stopped at an Improper prevdepth error caused by paragraph commands inside a proof; all three such headers in the harmonic fragment were repaired and the actual failed log was retained. Subsequent eighth-hour full builds reported zero overfull boxes, including zero greater than2pt. The new proof headers use explicit paragraph spacing. The finite CM marking was corrected by the actual free-group swap before the final freeze. Checkpoint08 has 345 pages, zero overfull boxes and no unresolved references or citations. All 91 selected full-page PNGs were opened and visually inspected. No clipping, overlap, damaged glyphs or unreadable displays were found. The PDF SHA256 is ff86c6ffbccf3e23134ad2d878795e90a81b5557020365c5d12daab705672839. The exact source/build hashes, page observations and PNG hashes are retained in the build and visual-audit manifests.

Inspector counts: {'root': 23, 'tower': 23, 'centralizer': 23, 'ghost': 22}.


## Checkpoint09

The initial ninth-hour build had one5.168pt overfull SVM display and one unresolved Fresse citation. Both were repaired in authoritative sources, with the failed build and bibliography gate retained. The next full build had zero overfull boxes; full-page inspection identified a crowded SVM.6 rank row and bibliography spacing. The final same-height spacing repair retained all mathematical content. Checkpoint09 has 372 pages, zero overfull boxes and no unresolved references or citations. All 85 selected full-page PNGs were opened and visually inspected. The observed crowded SVM.6 display was repaired without changing its two-line height; exact bibliography locations received ordinary spacing. The repaired render changed only pages171,370,371; each was reopened and inspected. The other82 selected images were byte-identical, verified by SHA256. The final inspected pages have no clipping, overlap, damaged glyphs or unreadable displays. The PDF SHA256 is 294008c6a29dfb9132c1da9e7111d194e7baa053334592a3f0624c5bcba553f1. Exact source/build hashes, before-repair files and all page observations are retained.

Inspector counts: {'root': 22, 'tower': 21, 'centralizer': 21, 'ghost': 21}.


## Checkpoint 10

Checkpoint 10 has 408 pages, zero overfull boxes and no unresolved references or citations. All 101 selected full-page PNGs were opened and visually inspected. The first tenth-hour build exposed one 74.68729pt overflow at CMC.1; its authoritative source was split into two gathered lines. The failed source and build logs remain retained. A later wording repair made the assertion 2*kappa_s=0 explicit; the sole changed full-page image, page 222, was reopened and inspected. The other 100 selected PNGs were byte-identical, checked by SHA256. The final three-pass build has no overflow. The PDF SHA256 is 7f233e449e7e1187ce60eb1de7988a840a440b7703862440ed9ef0a0f7eb9b15. Exact source/build hashes, page observations and image hashes are retained.

Inspector counts: {'root': 26, 'tower': 25, 'centralizer': 25, 'ghost': 25}.

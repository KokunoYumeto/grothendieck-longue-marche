# PDF verification method

## All-page painted bounds

`scripts/page_bounds_20261113.py` is an adaptation of the supplied `typeset/scripts/page_bounds_20261113.py`. The supplied version invokes `mutool draw -F bbox`; the adaptation calls **MuPDF’s native `fz_new_bbox_device`** through PyMuPDF. It does not substitute text-extraction rectangles for painted ink and does not infer absence of off-sheet content from a clipped raster image. The native device takes the union of the painted-object bounding boxes, including text, strokes, fills and images.

The execution backend is PyMuPDF 1.26.6 with MuPDF 1.26.11. Each verification JSON records the actual backend versions used. The all-page table records the ink rectangle, sheet rectangle, main text block, permitted area, and every exceeded edge in PDF points (1/72 inch).

The default permitted area is the supplied check’s area: A4 with 25 mm margins; 20 mm right marginal-note column and 10 pt separation; 12 pt head allowance; and the page number at 30 pt below the text block, with 3 pt of ink allowance. The original tolerances are retained: 1.5 pt at the permitted-area edges and 0.5 pt at the sheet edges. Every page is measured. Blank pages are explicitly represented. Pages outside the sheet are also included among outside-area pages; the two failure classes are not made mutually exclusive.

For standard `pdflscape` pages, PDF rotation is removed before the test. The rotated body occupies the original article’s block and its article page number retains its ordinary underlying-sheet position. Display orientation and rotated ink coordinates are also recorded. A three-page portrait/landscape/portrait calibration, using the actual 25 mm geometry and a rule spanning the full landscape line, yielded no sheet or permitted-area overflow. This prevents a landscape article’s deliberately unrotated footer from being mistaken for escaped text.

When a page exceeds an edge, the script also lists offending painted objects from `get_bboxlog`, and the nearby glyph metrics from `get_texttrace`. These secondary data are diagnostic. A possible single-letter overhang is flagged for visual review and is not silently accepted. An optional exception record must identify the current PDF hash, page, one alphabetic character, reviewer and reason. No exception can waive ink outside the sheet or an offending non-text object.

## Log verification

`scripts/verify_pdf.py` reads the adjacent LuaLaTeX log. It records every overfull horizontal or vertical box, the largest excess, all excesses above 2 pt, missing-character diagnostics, LaTeX errors, warnings, undefined-reference warnings, and underfull-box counts. It joins wrapping within individual diagnostics; it does not raise `hfuzz` or suppress an overfull report.

The parser was checked against the supplied English pre-repair log and `typeset/OVERFULL_BEFORE.tsv`: **all 382 rows, all widths, and all source line locations agree exactly**. The greatest excess in that source log is **331.94247 pt**. A reader’s own “before” figures are recorded only when its actual baseline log is supplied. Figures from the old English draft are not substituted for a French or newly constructed form’s baseline.

## Independent link verification

Every PDF external URI annotation is read independently. A scan link must match exactly:

`https://grothendieck.umontpellier.fr/web/viewer.html?file=../<cote>.pdf#page=<scan>`

Distinct scan coverage is checked separately for cotes 140-1, 140-2, 140-3 and 140-4 against 37, 575, 696 and 280 scans. Missing, extra and malformed targets are listed. Total external links, archive links, pages containing links and distinct scan pages are separate counts.

The PDF annotations have `/NM` identifiers containing the marked-source IDs actually covered by the annotation. These are matched against the adjacent `.lm-links.tsv` file. For each annotation, the verifier reconstructs direct marker coverage and recursive parent coverage, checks the scan target, and reconstructs the marker’s physical-page set. These independently reconstructed counts and page sets must equal the trace.

One annotation may cover nested marks. Its descendants can each credit a common ancestor; consequently the sum of all marker-run counts is intentionally greater than the number of PDF annotations. The verifier reproduces that recursion rather than comparing unlike totals. It separately checks the Lua `LM-AUDIT` annotation total against the actual PDF annotation total, as well as its marker, unlinked-marker, distinct-scan and physical-page totals against independently counted results.

Stable `source_id` values allow a source occurrence that is expanded repeatedly by a mathematical measurement or `mathchoice` to retain one identity. The selected painted branch must be linked. It is not valid simply to discard all unlinked expansions, because that could conceal an actual missing link. Per-form source-projection checks remain a separate part of the master-generation audit.

The verifier also reads every literal `LMsourceMark` call in that PDF's own adjacent TeX source. Every expanded runtime source ID must exist there exactly once and agree in marker kind, cote and scan. A shared language instrumentation JSON is a fallback only: an old pilot can coexist with a later full-body JSON, so the adjacent TeX source is the authoritative inventory for that PDF. Intentionally unexecuted alternate-form branches are not counted as missing shipped marks.

The two initial package pilots independently reproduced every marker’s PDF run count, page set and target with zero trace mismatches. Their initial excess unlinked expansions were diagnosed as three discarded branches each for two `text` choices and two discarded measurements each for two relation-class checks. This diagnosis motivated stable source IDs; it was not used to declare the uncorrected pilots finished.

The later two-package pilots using stable IDs cover all 37 scans of cote 140-1. Their diplomatic/corrected PDFs have 26/37 physical pages and 590/610 scan annotations, respectively. Each has zero unlinked marked occurrences, zero independent coverage/target mismatches, and complete agreement between expanded source IDs and its own TeX inventory. Their unrepaired baseline layout violations remain failures; this regression check is not final-reader certification.

## Required page selection and rendering

The verifier maps each original overflow site and each previous scaling/rotation site from `data/layout_before_sites.json` and `data/layout_pass_sites.json` back to its cote and scan. Nontrivial current local repairs in `data/layout_repairs_applied.json` are included for the relevant language; empty-cell placeholders do not independently enlarge the selection. All physical pages linked from that scan are selected, and the range extends to the next scan’s first page, including across a cote boundary, so that an unmarked continuation cannot escape inspection. The final scan extends through the end of the document. All landscape pages and all new ink-boundary failures are added. Forty pages, including the first and last, are then spread evenly across each PDF.

With `--render`, full-page PNGs are rendered at 900 pixels in width, and contact sheets contain four pages in a two-by-two arrangement. Additional overview sheets contain 16 pages in a four-by-four arrangement, with each page 550 pixels wide and individually labelled. The full-page images remain available for closer inspection. `SELECTED_PAGES.tsv` records every selection reason. `CLOSE_REVIEW_PAGES.tsv` flags prior mathematical/large overflows, previous scaling/rotation, current local layout repairs, landscapes and ink anomalies. `VISUAL_REVIEW.tsv` records each page, the PDF SHA-256, image dimensions, its individual image and both sheet names, decoded RGB-pixel SHA-256, PNG-file SHA-256, review status, reviewer and observations.

Rendering alone does not count as visual inspection. New rows are **pending**. A page counts as reviewed only when its row records `reviewed`, a reviewer and observations, its PDF hash agrees, and the actual image still matches both recorded image hashes. A review can carry forward across a rebuilt PDF only if the page had an attributed completed review and its freshly rendered RGB pixels **and** PNG file are exactly unchanged. Changed pixels or absent old image hashes reset the page to pending. Carry-forwards and resets are recorded in `REVIEW_HISTORY.jsonl`, with the preceding review and both PDF hashes; no inspection is invented for a new image.

`scripts/compare_pdf_pixels.py` renders and compares every corresponding page of an apparatus reader and its annotated master, including pages outside the selected visual-review set. With `--transfer-reviewed`, a selected master page can inherit a review only if its corresponding apparatus page was already reviewed, both review rows belong to the current PDF hashes, both saved image files match their stored hashes and fresh renders, and the two images have identical RGB-pixel and PNG-file hashes. The transferred row records the source PDF, source page, source image, hashes, actual reviewer and original observations. Different title pages require their own inspection. This is explicit reuse of existing visual evidence, not automatic inspection.

The carry-forward/transfer workflow was exercised on an actually inspected pilot page. A metadata-only PDF change preserved all 26 page rasters and transferred exactly the one reviewed page; a pending second page stayed pending. A further metadata-only change carried that same review forward. Introducing visible pixels on the reviewed page then reset it to pending. The regression artifact is separate from final edition review records.

After a final rebuild, `scripts/render_pending_review.py` can arrange only the still-unreviewed images into separate review sheets. It validates each existing PNG and decoded-pixel hash before copying a thumbnail, writes a page/hash index, and leaves the selection, full-size images and review TSV unchanged. Its default sheets contain sixteen pages at 550 pixels each; `--columns 2 --rows 2 --width 900` produces four-page sheets. These arrangements carry no inspection claim. Actual observations must still be supplied after viewing the pages.

The final report must summarize the completed review records and every remaining failure honestly.

## Typical invocation

```bash
python scripts/verify_pdf.py build/LM_FR_diplomatique.pdf --output-dir verification --render
```

Optional `--before-log` supplies the reader’s own baseline log; `--geometry` supplies documented per-page geometry overrides when needed; `--exceptions` supplies reviewed single-letter overhangs. These options preserve the actual measured rectangles and diagnostics in the record.

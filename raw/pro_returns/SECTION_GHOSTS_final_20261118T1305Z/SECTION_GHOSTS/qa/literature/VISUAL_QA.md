# Final PDF visual QA: literature pages

- Reviewer: `/root/literature`.
- Completed: `2026-11-18T13:02:32.622195+00:00`.
- Frozen PDF: `SECTION_GHOSTS_paper.pdf` (2,671,609 bytes; 378 pages).
- SHA-256 before and after inspection: `fed1f30941dbbe05d50da29e95bc9d236b571e0ef449912bbcc4805fabcd3563`.
- Actually viewed physical PDF pages: **18–21 and 364–378**, 19 pages total.
- Method: 125 dpi page renders, assembled into the five listed montages; **each montage was opened separately with `view_image` and visually inspected**. Individual page PNGs are retained but are not separately claimed as viewed.

## Findings

| Viewed pages | Opened montage | Findings |
|---|---|---|
| 18–21 | `P16_pages_018_021.png` | P16 theorem heading, all displayed formulas P.16.1–P.16.16, equation numbers, prose, citations, proof ending, and transition into Part A are legible. No clipping, overlap, missing glyphs, or header/footer collision observed. |
| 364–367 | `Bibliography_pages_364_367.png` | Pages 364–366 contain the historical audit register, not the bibliography; table columns, continuation headers, row boundaries and closing prose fit cleanly. References begin on page 367 after one continuation line. Hanging indents and long URL wraps are legible. |
| 368–371 | `Bibliography_pages_368_371.png` | Bibliography entries, accented names, mathematical symbols, hanging indents, page continuations and wrapped URLs are legible. No clipping, overlap or missing glyphs observed. |
| 372–375 | `Bibliography_pages_372_375.png` | Bibliography remains readable and consistently aligned. Long source URLs, including the multiline Nakamura–Tsunogai–Yasuda URL, wrap within the text block. No clipping, overlap or missing glyphs observed. |
| 376–378 | `Bibliography_pages_376_378.png` | Final bibliography pages, including Pál–Schlank, Stix and Wickelgren entries, are legible. Natural entry continuations across pages are intact. The last page ends cleanly with expected unused space below the final entry. |

## Outcome

**PASS.** No clipped text, equation/tag collision, overlapping bibliography entries, missing glyphs, header/footer collision, or broken table boundary was observed in the inspected pages. Page numbers and running headers are consistent. Blue source URLs wrap within the text block; their line breaks do not constitute clipping.

The requested range 364–378 includes three pages of the historical audit register; the References heading actually begins on page 367. All these pages were inspected.

No mathematical source, bibliography source, master metadata, or PDF content was changed for this review. The frozen PDF hash was rechecked and is unchanged. This record certifies visual layout only: it adds no claim of a new proof check, primary-source verification, live hyperlink test, or inspection of pages outside the listed range.

Rendered review images are QA artifacts, not manuscript source deliverables.

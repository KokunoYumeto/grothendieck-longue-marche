# SR02_63–71 — completed second reading

All **30 selected pages** are finished. The run contains **677 boxes**, each with a first reading prepared before its isolated blind reading. MAIN compared the readings by script and adjudicated the genuine differences on enlarged crops, also reading every manuscript page in full against the scan.

## Final contents

| File or directory | Contents |
| --- | --- |
| `edited_pages/` | The 30 finished diplomatic LaTeX page files, under their supplied filenames. |
| `placements.tsv` | 467 decision rows: 178 exact source replacements (`a`) and 289 retained readings (`b`). The replacement count includes representation conformance, including 18 removals of inherited editorial comments. |
| `second/` | Every page's coordinate boxes, first readings, isolated blind readings, token comparison and adjudication review; supplementary blind records are preserved. |
| `crops/` | Saved blind and MAIN crops, upright views of slanted writing, detail crops and review sheets. Coordinates refer to the supplied JPGs. |
| `SR02_63-71_notes.md` | The 39-row notation table, eleven codicological checks, page-order findings and page decisions, including unresolved readings and written slips. |
| `SR02_63-71_hand_log.md` | The 43-row handwriting/notation log with local scope and explicit witness-attribution limits. |
| `CHECK_EVENTS.tsv` | 701 events covering 696 statement IDs: the 677 boxes and 19 additional exact-placement loci. Five revisited IDs have distinct earlier and final-conformance events. |
| `progress.log` | UTC start, page completion records and explicitly identified addenda. Earlier completion events remain; the latest entry for a page gives its final counts. |
| `scripts/` | The preparation, comparison, decision, conformance and lossless packaging scripts used in this run. |
| `analysis/` | Supporting review records, checkpoint receipts, compression evidence and the final structural QA reports. Earlier proposals and snapshots are documentary history; final reports and the principal logs state the completed result. |

The selection comprises 15 pages of cote 63, 11 pages of cote 156-5 and four pages of cote 71. It is not an edition of the complete three cotes. Unselected pages and unavailable witnesses are not reconstructed.

## Replacement semantics

Read TSVs with a tab-delimited CSV parser: quoted fields can contain actual newlines. For every `a` row, `find` is an exact, unique span of the corresponding **original supplied page**, and `replace` is its adjudicated replacement. All source spans on one page are nonoverlapping. Apply them against the original text in descending source-position order; do not search the evolving edited text for subsequent finds. A `b` row has empty replacement fields.

The final conformance addendum is explicit in `scripts/final_conformance.py` and `analysis/final_conformance.json`. It preserves the earlier reading decisions while moving running text outside drawing nodes, repairing the command boundary before the already decided J, and removing reader comments from page files. The older per-page decision scripts record their original completion stage; the final placement table includes the later addendum.

## Verification and limits

The final read-only QA checks all 30 edited pages by exact replay from the original sources, unique/nonoverlapping source spans, all 677 first/blind pairs, complete comparison reviews, crop references, UTC progress records and TeX grouping. It also verifies that the supplied 30 TeX pages, 30 JPG scans and preamble retained their original bytes. Those attachments are excluded from this delivery.

The audit uses no OCR, text-recognition library, PDF text layer or TeX compilation. Remaining reading uncertainty stays in the page files. The CHECK events record the actual transcription/representation work and explicitly make no claim to mathematical proof checking or formal certification.

Four supplemental MAIN crops extend one or two source pixels below their scan; the generated padding and exact coordinates are documented in `analysis/documentation_cleanup_qa.md`. No ink is inferred from that padding.

The archive uses standard ZIP compression methods, including BZIP2 and LZMA where useful. Documented image optimizations and archive-only PNG encodings preserve the exact decoded image pixels. The archive's encoding manifest records those changes; no crop is discarded to reduce archive size.

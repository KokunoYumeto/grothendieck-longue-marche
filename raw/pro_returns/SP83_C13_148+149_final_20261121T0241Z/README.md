# SP83_C13_148+149: consolidated diplomatic transcription

The complete deliverable covers the 23 supplied scan pages, in `page_order.txt` order. Each page received a full reading against witnesses C and H, main-reader crop adjudication, and a frozen independent reading by a different one of the three readers. The transcription preserves unresolved ink as uncertainty; it does not claim human verification.

## Completion record

| Measure | Total |
|---|---:|
| Accepted pages and completed independent audits | 23 |
| Independently read prescribed boxes | 339 |
| Boxes with unequal first/second token sequences | 288 |
| Boxes whose adjudicated reading changed | 126 |
| Material discrepancy places | 715 |
| Places differing from C | 276 |
| Places differing from H | 640 |
| High / medium / low confidence places | 474 / 116 / 125 |
| Supplied doubt marks decided, in original order | 261 |
| Inventoried elements | 520 |
| Remaining doubt-table entries | 275 |
| Mathematical check events | 63 |
| Frozen transcription files | 24 |

A place can differ from both witnesses. Material discrepancy counts exclude changes of macro syntax or certainty alone. Audit box counts are a separate measure and include such token differences. A doubt-table row can cover several local in-place uncertainty marks; the table is organized by reading place, not by macro occurrence. Check-event types state what was actually checked; carrying a source assertion as background does not verify it.

## Files to read

| File or directory | Content |
|---|---|
| `pages/` | The 23 accepted diplomatic page fragments. |
| `SP83_C13_148+149_transcription.tex` | All accepted pages in order, one fragment without a preamble. Use the supplied original PREAMBLE and its conventions. |
| `SP83_C13_148+149_changes.md` | Counts, consequential corrections, page-by-page C/H/final comparisons, visual evidence and unresolved places. |
| `SP83_C13_148+149_collation.tsv` | Only the material places where H differs from the final reading. |
| `decisions.tsv` | All 261 supplied MARKS decisions in their original order. Additional cancelled-text decisions are documented in the changes report and records. |
| `SP83_C13_148+149_doubts.md` | Consolidated notation table, remaining doubts, abbreviations and legibility assessment. |
| `SP83_C13_148+149_inventory.csv` | Every inventoried text block, display, drawing, margin, deletion and insertion, in page order. |
| `SP83_C13_148+149_notes.md` and `CHECK_EVENTS.tsv` | Page content and mathematical reading notes, with explicitly classified check events. |
| `SP83_C13_148+149_hand_log.md` and `SP83_C13_148+149_sheet_feedback.md` | Observed hand habits, local exceptions, witness errors and error-sheet feedback. |
| `second/` | Prescribed original-pixel boxes, frozen first and independent readings, exact token comparisons and main-reader adjudications. |
| `crops/` | Retained evidence images; restore the original PNG paths as described below. |
| `records/`, `scripts/`, `qa/`, `work/proposed/` | Accepted structured evidence, reproducible processing, dated QA snapshots and original reader proposals. Proposals are historical working documents; `pages/` is authoritative. |
| `progress.log`, `transcription_hashes.tsv`, `checkpoint_receipts.json` | Reading/audit chronology, the 24 frozen SHA-256 values, verification and durable checkpoint records. Earlier checkpoint ZIPs are not nested here. |

## Exact evidence-image restoration

The archive uses the lossless transport documented in `CROPS_README_V2.md`, `CROP_COMPRESSION_MANIFEST_V2.json` and `image_transport_note.md`. Most retained PNGs are stored as lossless JPEG XL; some additional helper views are represented by byte-exact recipes from an included parent crop. No manuscript scan is required for restoration, no crop is discarded, and no delivered image is reduced in resolution.

After extracting the ZIP, run:

```sh
python scripts/restore_crops.py
```

This restores the original `.png` names used throughout the evidence records. Python, Pillow, NumPy and an FFmpeg build supporting JPEG XL are required; exact verified versions are recorded in the transport manifest. To restore images and verify every original file against its SHA-256:

```sh
python scripts/compact_archive_v2.py --verify-all
```

The complete checkpoint06 transport test restored all 856 retained PNGs exactly, independently verified all 1449 original entries, and compared those restored PNGs with the final retained evidence files. The final archive's manifest supplies the exact hashes for its own text, metadata and image contents. The archive retains the full test report. Attached source scans, witness files, prepared halves and previous ZIPs are intentionally excluded.

## Scope of the checks

No OCR, outside research or TeX compilation was used. Structural validation checks the page set, conventions, balanced structures, required records, independent-reading integrity and evidence references. Drawing geometry is expressed in TikZ and checked visually; it remains a transcription of the drawn structure and marks, not a photographic facsimile. The least secure letters, revision layers, labels and edge-clipped words are identified in the doubts and notes. Earlier QA reports remain as dated snapshots; the reports named `final` describe the completed review.

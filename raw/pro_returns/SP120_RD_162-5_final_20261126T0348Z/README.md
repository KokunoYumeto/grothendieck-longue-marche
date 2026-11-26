# SP120 RD 162-5 — diplomatic transcription


## Authoritative text and page order

The final diplomatic readings are in `pages/162-5_scanNNN.tex`. `SP120_RD_162-5_transcription.tex` combines those same 21 page fragments in this order:

```text
002, 003, 004, 005, 006, 007, 008, 009, 010, 011, 012,
013, 014, 015, 016, 017, 018, 020, 022, 023, 024
```

The combined file is a LaTeX fragment without a preamble. Its readings preserve source spellings, abbreviations, errors, cancellations, additions, and localized uncertainty. Mathematical expectations do not authorize repairing the source text.

`second/*_first.tsv` and `second/*_second.tsv` preserve historical readings frozen before comparison. They are evidence of the reading process and can differ from the adjudicated final pages. Partial files, `drafts/`, and working metadata in `reports/` and `state/` are retained for provenance; use the final page fragments and combined file for the completed transcription. Historical notes describe the scope and state at the time they were written.

## The two archives

`SP120_RD_162-5_final.zip` contains the transcription, evidence tables, notes, audit records, and reproducibility scripts. Its `crops/` directory contains only `CROPS.tsv`, with canonical crop filenames, source-scan pixel boxes, and the places examined.

`SP120_RD_162-5_crops.zip` contains all `1,761` registered canonical crop images under `crops/`, including the evidence for changed and unresolved places. These are grayscale JPEGs at quality 85, copied without further recompression. The archive is `164,696,509` bytes, below 200 MB. Supplemental rotated or resized display derivatives are excluded; their parent crops, coordinates, dimensions, hashes, and known or qualified derivations are documented separately in `state/derived_crop_views.tsv`.

### Main deliverables

| File or directory | Contents |
|---|---|
| `pages/`; `SP120_RD_162-5_transcription.tex` | Final page readings and their ordered combination. |
| `SP120_RD_162-5_changes.md` | Per-page and aggregate changes against C and H, confidence counts, consequential corrections, source evidence, remaining unresolved places, and changed audit places with both historical readings. |
| `SP120_RD_162-5_collation.tsv` | Differences between witness H and the final reading, with witness C, evidence, category, and confidence. H has no text for scans 002 and 020, so those pages have no H-collation rows. |
| `decisions.tsv` | One decision per supplied MARKS entry, in its original order, with the adopted or unresolved reading, evidence, crop, and confidence. |
| `SP120_RD_162-5_doubts.md` | Notation table, remaining localized doubts, abbreviation interpretations, and an assessment of legibility and the witnesses. |
| `SP120_RD_162-5_inventory.csv` | Page elements, their positions and hands, and transcription coverage. |
| `SP120_RD_162-5_notes.md`; `CHECK_EVENTS.tsv` | Reading notes and explicitly scoped mathematical checks, including outcome and available model/effort/run metadata. |
| `SP120_RD_162-5_sheet_feedback.md`; `SP120_RD_162-5_hand_log.md` | Error-category feedback and recurring features of the handwriting and typing. |
| `second/`; `progress.log` | Box coordinates, frozen first and blind second readings, token comparisons and adjudications, completion/audit events, and final freeze verification. |
| `scripts/`; `state/`; `reports/`; `drafts/` | Reproducibility tools, receipt and review records, working metadata, and historical working material. |

## Blind reading and adjudication

All 21 first-stage page readings were completed before the blind second-reading phase began. Each page's blind reader had not performed its first-stage reading and received only the page image and neutral box list, without either witness, the first-box readings, final page text, notes, or private mappings. Each second reading was saved before comparison.

The blind phase covered 930 selected boxes, focusing on the specified difficult material; it was not a second transcription of every ordinary line. Scripted token comparison found `571` differing boxes, and adjudication changed `234` boxes. Token differences include differences of TeX representation, graphic encoding, and uncertainty notation. They are not interchangeable with counts of corrections against C or H. Root visually adjudicated each differing box against the crop, recorded the evidence, and retained or changed the reading, with localized doubt where the ink does not settle it.

**Two first-box format exceptions:** `162-5_scan005_first.tsv`, B013, and `162-5_scan009_first.tsv`, B054, preserve English graphic glosses instead of TeX graphic readings. Their corresponding first-stage page fragments already contained TikZ for those graphics. These are exceptions to the requirement that every first-box record use the transcription's TeX conventions. The historical records remain unchanged; their representation differences must be understood in that light. Neither gloss was supplied to the blind reader.

## Sources, checks, and recovery

No OCR, external research, or TeX compilation was used. TeX checks were structural. Mathematical check claims are limited to the statements and outcomes recorded in `CHECK_EVENTS.tsv`; they do not certify all mathematics on the pages.

Original scans, attached witness files, the supplied preamble, and raw scan halves are deliberately omitted. Restore the original supplied bundle separately if rerunning source-dependent tools; scripts expect sibling paths including `../source/SP120_RD_162-5_scans/` and `../source/SP120_RD_162-5_texts/`. Comparison excerpts remain in the requested evidence records.

The final 21 page hashes and combined-transcription hash are recorded in `state/frozen_hashes.tsv` and `progress.log`, followed by an unchanged-hash verification. `scripts/final_archive_check.py` checks the final archives against that freeze and the canonical crop registry. `state/checkpoint_receipts.json` preserves durable-save receipts and archive checksums; earlier checkpoint ZIPs are immutable and are not nested inside the final archives.

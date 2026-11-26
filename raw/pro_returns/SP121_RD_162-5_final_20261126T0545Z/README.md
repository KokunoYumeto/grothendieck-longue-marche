# SP121_RD_162-5 diplomatic collation

This package records the scan-based consolidation of witnesses C and H for scans 025–031 and 033–046 of cote 162-5. The transcription is a LaTeX fragment; use the supplied source PREAMBLE separately. No OCR, external research or TeX compilation is part of this run.

## Reading records

`pages/` contains only pages accepted by the main reader, each with its matching done line in `progress.log`. All 21 pages have completed the first pass and the independent image-only audit. The audit covers 470 boxes; 367 token-different boxes were adjudicated on narrow crops and 51 box readings were amended. Those audit counts are separate from the counts against witnesses C and H. Per-page evidence in `data/` produces the changes, H collation, MARKS decisions, inventory, notes, doubts and hand log. `verification/` records the main reader’s visual adjudications. The final image-only audit reads every required difficult box with a different reader; `second/` retains both readings and the token comparison.

The source scans, witnesses, preamble, input archive and native halves are deliberately omitted. `verification/source_manifest.json` identifies the supplied archive and prompt by checksum. Crop coordinates are in `crops/CROPS.tsv`; checkpoints and the main final archive carry this register only. The separate final crop archive carries the images.

The final crop archive contains 1,571 evidence crops as grayscale JPEGs at quality 85, without reducing their dimensions. Its size is 172,370,377 bytes, below the requested 200 MB ceiling. Every referenced change, remaining-doubt and adjudication crop is included; conservative page-wide inclusion covers doubts without a separate crop link. The crop archive's JSON/CSV manifests record the selection, encoding and checksums; `verification/crop_package_result.json` gives its final SHA-256.

## Scripts

- `scripts/crop.py`: create and register an enlarged, sharpened grayscale evidence crop from a source scan. Deciding crops are limited to 40% of scan width. Broad image-only audit boxes preserve complete required formulas through overlapping narrow components, all of which were inspected for each differing box.
- `scripts/assemble.py`: rebuild reports from accepted page evidence; accept a reviewed draft with `--finalize PAGE`; prepare and seal the second-reading TSV files with `--second-files`; package current deliverables with `--package PATH`.
- `scripts/audit.py`: compare sealed first and blind second readings token by token, and log a completed root adjudication. It never applies text changes automatically.
- `scripts/verify.py`: check structural completeness and, after all audits, freeze and verify SHA-256 hashes without compiling TeX.
- `scripts/check_quotes.py`: verify the exact witness-C/H excerpts in all change rows.
- `scripts/package_crops.py`: select every crop required by changes, retained doubts and audit decisions, then create the single grayscale JPEG evidence archive below 200,000,000 bytes. Its manifests record every included image and encoding profile.
- `scripts/normalize_final_syntax.py`: the recorded, one-time correction of three unsupported insertion options and three diagram separator encodings after the image audits. This changed syntax only; witness quotations, historical readings, audit counts and source readings were preserved.

Scripts locate the edition root from their own path and the source attachment tree beside it, under `source/`. `procedures/reader_instructions.md` documents the reading schema and restrictions. The task’s attached prompt remains the controlling source of requirements.

Mathematical statements in the notes are reported source claims unless CHECK_EVENTS identifies an actual, scoped check. Doubts and surprising source readings remain in the transcription; a mathematically expected correction belongs only in the notes.

The sealed pre-audit readings are historical evidence and intentionally differ from the final pages at the recorded amended boxes. `verification/frozen_sha256.json` and the final lines of `progress.log` establish the final transcription state. Do not rerun page acceptance, second-file sealing, or transcript assembly over a frozen edition. The nine events in `CHECK_EVENTS.tsv` identify the limited mathematical checks actually performed; transcription and visual comparison alone are not counted as proof checks.

All 570 change rows received an explicit error-sheet classification review. The changes report counts 289 differences against C and 526 against H, with overlap between the two; 95 rows are marked mathematically consequential. The 167 original MARKS have one decision each, in source order. The doubts report retains 205 unresolved records. Exact-text verification checked all 1,140 quoted C/H excerpts without discrepancies. These are editorial record counts, not estimates of the transcription's residual error rate.

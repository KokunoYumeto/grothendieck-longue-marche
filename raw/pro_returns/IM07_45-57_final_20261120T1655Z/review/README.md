# Review and reproducibility record

The authoritative deliverables are `placements.tsv`, `edited_pages/`, `notes.md`, `crops/`, `CHECK_EVENTS.tsv`, and `progress.log` at the archive root. The `review/` and `scripts/` folders document how those deliverables were produced.

## Coverage

All 69 input rows, including both occurrences of L1310, have a final decision. All 58 page files are present. Five rows cause five exact replacements on five pages; the other 53 pages retain their original bytes, including line endings. The decision totals are a: 5, b: 55, c: 5, d: 4.

- L195, 56/005: identify the surviving insertion as varphi_nu after comparison with the explicit form at 56/026; preserve the uncertain cancelled predecessor.
- Qsow045, 57/077: remove the doubt-marked paper/ink speck after u.
- L636, 57/092: add an explicit X/A doubt, with X first, rather than asserting a certain A.
- L634, 57/100: encode the destination Y written over X as a cancellation and insertion.
- L644, 57/155: mark the overwritten coefficient 3/2 and reproduce the three dots below the cancelled c_0.

Mathematical corrections in the supplied table are identified as supplied editorial material. The work checks facsimile readings and file integrity; it does not claim independent proofs of that mathematics. Model identity is recorded as declared in the session; a runtime effort value was not exposed.

## Record precedence

`PAGE.json` and `PAGE.proposed.tex` are the page reader's original return. `PAGE.final.json`, when present, contains the main reader's adjudication. `PAGE.accepted.json` is the authoritative per-page record used to construct the aggregate files. `PAGE.main_revised.tex` is present for a later amendment. Earlier accepted records are retained under `before_amendment` names; they are historical records, not additional final decisions.

The final row disposition can be resolved while a literal reading remains uncertain. Such cases have `unresolved: false` and `ink_unsettled: true`; their in-place doubt marks and a concise uncertainty table remain in the deliverables. The older crossed-out predecessor at L195 is also still uncertain, even though its surviving replacement was identified.

The amendment at 56/005 preserves the initial page-only judgment and the later comparison-based decision. The amendment to 47/007 adds the actually viewed cross-reference to the Kummer passage at 57/144. External reading notes FW01, FW02 and SF07 were not supplied and were not checked. `provenance_adjustments.json` documents a clerical correction that restored one reader event to its original wording while retaining the main judgment in its separate event.

## Reproduction

The input ZIP was unpacked once into a sibling `source/` directory. It is not copied into this archive. To reproduce the integrity audit elsewhere, place this archive's contents in a work directory with a sibling `source/` containing the original extracted input files and a sibling `upload/IM07_45-57.zip` containing the original attachment. Then run:

```sh
python3 scripts/verify_final.py
```

The audit checks input identity against ZIP member bytes, all 69 row identities and their order, all 58 pages, uniqueness of each original find span, reconstruction of each final page using only approved replacements, per-page hashes, crop and metadata references, note coverage, check-event coverage, and one completion record per page. Its report is `review/verification.json`. It reads the input ZIP without extracting it again.

`make_crop.py` uses Pillow only for geometric cropping, resizing and contrast adjustment. No OCR or recognition software is used. Each crop has a JSON sidecar recording its source image, box coordinates, output dimensions, contrast and resampling. Some additional orientation/preview images document the actual visual review.

`accept_page.py` and `amend_page.py` preserve page bytes outside the approved original spans. The acceptance script requires the per-page assignment folder used during work; a fresh session can rebuild those assignments from the input table and `review/page_order.json`. `package_work.py` creates a new ZIP and an internal path/size/SHA-256 manifest, excluding inputs, caches and prior ZIPs. Its final CRC test checks the archive container. The manifest excludes itself to avoid a circular hash.

## Timing

Work began at 2026-11-20T16:15:31Z. All page decisions were written by 2026-11-20T16:51:50Z. The first scheduled checkpoint falls at 2026-11-20T17:00:31Z; no checkpoint was due when page review ended. Any checkpoint actually created is recorded in the run metadata. No checkpoint is created at a page or section boundary.

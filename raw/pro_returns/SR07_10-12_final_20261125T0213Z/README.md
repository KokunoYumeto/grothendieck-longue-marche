# SR07_10-12 — completed second reading

## Deliverables

`SR07_10-12_final.zip` contains the completed diplomatic transcription and its
audit records. `SR07_10-12_crops.zip` contains the image evidence selected for
changed or undecided places. Extract both archives to the same directory to
place the exported JPEGs beside `crops/CROPS.tsv`.

| Item | Final count |
|---|---:|
| Finished pages | 30 |
| Prepared boxes with first and blind second readings | 1,002 |
| Token comparisons marked different | 779 |
| Placement decisions | 617 |
| Exact replacements, decision a | 494 |
| Text-stands decisions, decision b | 123 |
| Surviving uncertainty-macro occurrences | 359 |
| Crop locations recorded | 1,863 |
| Crop images exported | 1,255 |
| Crop archive size in bytes | 186,164,209 |

The replacement count includes documentary changes required by the page-file
conventions; it is not a count of corrected manuscript words. Thirty-three
placements solely remove editorial `%` comments and have no source-ink locus.
They are identified individually in `audit/editorial_crop_exemptions.tsv`.

## File guide

- `edited_pages/`: the 30 finished page files, using the supplied preamble.
- `placements.tsv`: exact original find spans and replacements, first and blind
  readings, ink adjudications, confidence, and crop references. This ledger and
  `edited_pages/` are the authoritative final transcription.
- `second/`: prepared boxes, sealed first readings, blind second readings,
  per-page token comparisons and crop manifests. The six supplemental boxes are
  integrated in the main per-page tables; their separate records preserve the
  supplemental reading procedure.
- `second/comparison_scope.tsv`: all 779 differing comparisons; 510 are attached
  to placement decisions and 269 have individual representation or crop-context
  explanations.
- `SR07_10-12_notes.md`: notation table, page-specific reading notes, retained
  doubts, source limitations, and all eleven codicological checks, including the
  30-face collation and cited archive inventory.
- `SR07_10-12_hand_log.md`: observed writing and notation habits, their scope,
  and the readings they affected.
- `CHECK_EVENTS.tsv`: 1,002 documentary box events. These record reading and
  comparison; they make no claim to have proved the mathematics.
- `progress.log`: page completion, amendments and immutable checkpoint history.
- `crops/CROPS.tsv`: all 1,863 crop locations, source-pixel coordinates,
  rotations, scales and purposes. Crops of unchanged, settled readings that are
  not in the image archive can be recut from the attached scans.
- `audit/crop_export.tsv`: every exported image, its hash and source coordinates,
  and why it was selected. The crop ZIP also contains this manifest.
- `audit/remaining_doubts.tsv`: the 359 surviving `\unsure` or `\illegible`
  macro occurrences, with locations in the final TeX files. Its literal box
  matching column is only an aid; altered alternatives can differ from both
  earlier readings. See the separate uncertainty/crop coverage audit.
- `audit/uncertainty_crop_coverage.tsv`: a verified mapping from every one of
  those 359 final-text occurrences to its existing exported image evidence.
- `audit/`: independent coverage, format, codicology and integrity reviews;
  metadata corrections; exact-replay results; export and final-release records.
- `scripts/`: the run's preparation, comparison, crop, adjudication, amendment
  and packaging programs. Historical mutation scripts must not be rerun against
  the completed output. `document_state.py` checks exact original-to-final
  replacement replay using the supplied source tree.
- `drafts/`: retained adjudication and working records for audit history. No
  unfinished page is included in `edited_pages/`.

## Evidence and verification

All 30 edited pages were reconstructed exactly from the attached starting page
and the ledger's a decisions. All 1,002 box IDs match the first readings, blind
readings, comparisons and documentary events. The 23 stale per-page image-scale
values found in the final metadata review were corrected without changing image
pixels or readings; the old/new values are preserved in the audit.

The exported crops are grayscale JPEG at quality 85. Every generated detail in
each selected evidence family is retained, and the archive is below the decimal
200 MB limit. Source-ink changes have exported evidence; documentary comment
removals are explicitly distinguished. The full crop-location inventory also
records crops not exported.

The eleven codicological checks were recorded before the final page was
committed. Distinctions between observation, inference and unresolved dating or
publication correspondence are preserved in the notes. Retained uncertainty
marks are part of the completed reading, not uncompleted work.

No OCR or TeX compilation was used. No attached source files, fetched source
copies, previous checkpoint archives or crop images are included in this main
archive; the crop directory here contains only its location manifest. The
supplied `PREAMBLE.tex` and source scans remain external to both deliverables.

For script reuse, place the supplied unpacked source tree in a sibling directory
named `source`, as expected by `scripts/audit_tools.py`. The sources are not
distributed again here.

Final packaging timestamp: 2026-11-25T02:13:36Z.

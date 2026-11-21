# Processing integrity and final technical review

The first reader assigned to scan103 independently reviewed only the processing scripts after finishing that page. No additional page texts, reports, images or blind readings were supplied for this technical task. The main reader applied the resulting changes before any actual blind comparison.

Four concrete issues were identified and addressed:

1. A blind submission could have changed after comparison without detection. The exact submitted bytes are now committed once, and approval/final validation reconstruct the comparison from those committed inputs.
2. A truncated first-reading manifest could have verified only its remaining rows. Verification now requires the exact 48 distinct expected paths, and manifest publication is atomic.
3. A truncated final freeze could have verified fewer than25 files, and packaging did not enforce the freeze. Verification now requires all24 pages plus the combined transcription; final validation checks them, and final packaging checks the frozen hashes against its own snapshot bytes.
4. An interrupted ZIP write could have left an incomplete official filename. ZIPs are now built under a temporary name, every entry is checked against the snapshot, and the completed archive is published atomically. Start and completion events are distinguished in the log.

Focused checks performed by the main reader passed: complete exact manifest accepted; header-only, incomplete and duplicate-path manifests rejected; changed committed bytes rejected; committed-file replacement refused; and a token substitution reconstructed correctly from the exact supplied byte buffers. All Python scripts were parsed successfully. These checks concern processing integrity, not handwriting recognition or the mathematical claims in the manuscripts. No OCR or TeX compilation was used.

Before the last two page reports arrived, a further screening check compared the22 approved pages with their proposed first-box readings. Every distinct source numerical token was represented; the only unmatched numerical values were TikZ coordinates. Every insertion, cancellation, marginal note and manuscript-page macro was represented, with one long cancellation on082 deliberately split across three consecutive boxes. These are limited consistency screens: they do not establish spatial coverage of every repeated numeral or replace the visual box review.

Scan 087 audit approval passed integrity/operation checks and wrote its approved record, but report generation stopped on a newly added abbreviation field named abbreviation instead of form. Corrected the apparatus schema, rebuilt all reports and appended the pending audit log once. No committed readings were changed.

The scan 092 blind view log also records its original image, in addition to every prescribed crop. View validation now accepts the optional exact NNN-ORIGINAL ID only when its path resolves to that assigned source image. All prescribed box IDs remain mandatory, unexpected IDs still fail, and reader identity is checked across every row. The original log was preserved unchanged.

## Final review

All24 scans have first-reader approval and completed blind adjudication: 197 boxes, 160 differing boxes, 1458 scripted token operations, and 78 boxes whose final reading changed. Every differing operation has one explicit main-reader decision and a crop reference. These counts describe the audit, not error rates or independent human validation.

A final independent metadata review found and corrected stale apparatus excerpts: the cancelled comma doubt in082, the clipped normalisat quotation in099, singular chgt in101, the short-only transf and automatiq-with-raised-t forms in102, the S/G uncertainty description in104, and the updated upper drawing excerpt in098. Source witness quotations, committed first/second readings and the page texts were not altered by those metadata synchronizations.

The101 feedback category was corrected from an unrecognized variant to insertion placement. Validation now rejects unrecognized substantive categories, preventing the category sum from silently losing a row. Historical blind-view logs keep their original absolute paths; integrity.resolve_view_image maps their work/source suffixes to the current restored workspace. All approved logs verified, and a focused relocated-root fixture check confirmed the path mapping without asserting that its synthetic path fixtures were image readings.

All processing Python files passed syntax parsing. Final structural validation checks braces, environment nesting, allowed source conventions, exact page order, generated combined-text equality, all90 supplied mark decisions in order, inventory completeness, crop existence, distinct first/blind readers, exact48 pre-blind commitments, immutable second submissions, reconstructed token comparisons, operation coverage, and the exact25-file freeze. ZIP publication additionally compares every archived entry against its snapshotted bytes. No OCR, external manuscript research, or TeX compilation was performed.

A final literal-substring screen compared every adjudicated box-final fragment to its page. Ten flags were manually reconciled as cross-box underline/deletion scopes, display-tag syntax, a term embedded in its connected-note TikZ drawing, or intervening separately inventoried margin notes. All approved readings were applied; this screen required no page edits. FINAL_CONSISTENCY.json records the ten local explanations.

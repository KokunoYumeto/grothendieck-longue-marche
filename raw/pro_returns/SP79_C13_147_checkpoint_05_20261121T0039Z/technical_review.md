# Technical review before blind reading

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

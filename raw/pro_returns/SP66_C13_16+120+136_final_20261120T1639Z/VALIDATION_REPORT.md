# Validation record

The primary reader alone made all image-based reading decisions, including the second audit. A separate helper performed mechanical validation of the files and tables. It did not inspect images or decide any manuscript reading. No OCR, external research or TeX compilation was used.

## Completed checks

- The 25 page files occur in the supplied order; the combined fragment is their exact concatenation with inter-page blank lines.
- All 187 entries from the supplied live-text mark register are represented in `decisions.tsv`, in order, with matching cote and scan metadata.
- The 446 rows of the H collation exactly match the H-difference rows and generated fields in `CHANGE_LEDGER.tsv`. H's page number is the scan number minus one. There are no H rows for the cover without H text.
- The ledger contains 484 recorded places: 141 differ from C, 446 from H, and 103 from both. Confidence is high at 317, medium at 107 and low at 60. Pure macro differences and certainty-only changes are not counted as textual differences.
- All 506 inventory rows are marked transcribed, cover the 25 pages and have unique element identifiers within each page.
- The 83 check events have the requested five-column schema, permitted event types and no exact duplicate rows. They distinguish targeted checks from statements only carried as background.
- All 25 completion entries and all 25 audit entries occur in the required order in `progress.log`.
- The LaTeX fragments pass mechanical checks for brace and environment balance, the supplied/standard macro vocabulary, and apparent control-word joins. These are source checks, not a claim of compilation or rendered-page verification.
- The 127 uncertainty/illegibility wrapper occurrences have located coverage in the 124-row doubts table; adjacent wrappers can share a row. Equivalent double-prime notation in the scan009 doubt record has been aligned with the page text without changing the reading.
- The ten-category feedback and final legibility assessment are included. Their counts are generated from the final ledgers.

## Freeze and archive verification

`progress.log` records the SHA-256 of all 25 page files and the combined transcription at the freeze, followed by a verification that those 26 hashes remain unchanged. `PACKAGE_MANIFEST.tsv` inside the ZIP records the byte length and SHA-256 of every included work file.

The final archive check verifies that its member list and member bytes match the current deliverables and manifest, that all required files are present, and that it contains no attached sources, scan images, crop images, page halves or nested ZIPs. The immutable earlier checkpoints are separate archives and are not embedded.

## Reading limits

Mechanical checks do not certify palaeographic accuracy. The local uncertainty wrappers, decisions, doubts, hand log and pixel-box evidence remain authoritative about what could and could not be read. Mathematical checks are limited to the claims and checks actually recorded in the notes and `CHECK_EVENTS.tsv`.

# SP123_RD_36 — audited diplomatic edition

This package records an image-based consolidation of the 22 supplied scan pages, in the requested order:

003, 004, 005, 006, 007, 008, 028, 029, 030, 031, 032, 033, 034, 035, 036, 037, 038, 039, 040, 041, 042, 043.

## Status and authority

`progress.log` records two distinct stages. A `scan NNN done` entry certifies the main-reviewed first reading. A `scan NNN audited` entry certifies the independent image-only second reading, manual adjudication and audit-integrity checks. A final frozen edition requires the audited stage for all 22 supplied pages, followed by a transcription freeze and unchanged-hash verification. Files under `drafts/` are unfinished; `pages/` contains completed first readings amended only through recorded audit decisions.

All 22 supplied pages have completed the main-reviewed first reading and the independent image-only audit of their assigned boxes. Every scripted token difference has a recorded main-reader adjudication. The apparatus totals derive from the final canonical records after metadata reconciliation, and `AUDIT_SUMMARY.tsv` gives the completed per-page audit counts. The released transcription comprises 22 page fragments and the combined fragment; `FROZEN_SHA256.tsv`, `VALIDATION.json`, and `progress.log` record its freeze and final integrity checks.

The scans are the reading authority. C and H are unverified comparison witnesses. No OCR, text-recognition library, external edition, internet research, or TeX compilation is used. Source errors and uncertain ink are retained in the transcription. Mathematics and notation guide where to inspect and how to rank genuinely ambiguous forms; they do not authorize replacement of a clear written form.

## Files

| File or directory | Function |
| --- | --- |
| `pages/` | One consolidated TeX fragment per completed scan. |
| `SP123_RD_36_transcription.tex` | All 22 fragments in scan order, created only at the final freeze. |
| `SP123_RD_36_changes.md` | Per-locus C/H readings, final readings, physical evidence, confidence, remaining doubts, and audit changes. |
| `SP123_RD_36_collation.tsv` | Substantive departures from H's source readings; editorial synopses are excluded. |
| `decisions.tsv` | Disposition of every supplied MARKS identifier, in its original order. |
| `SP123_RD_36_doubts.md` | Notation table, unresolved readings, abbreviations, and final legibility assessment. |
| `notation.md` | Current notation table and cross-page comparison used by the apparatus and subsequent page assignments. |
| `SP123_RD_36_inventory.csv` | All transcribed text blocks, formulas, diagrams, margins, insertions, deletions, and other source elements. |
| `SP123_RD_36_notes.md` | Page content, source slips, limits of mathematical checking, and codicological observations. |
| `CHECK_EVENTS.tsv` | Only checks actually performed, with their actual strength. Transcription alone is not a proof check. |
| `SP123_RD_36_hand_log.md` | Habits observed on these pages, their verified scope, and their effect on readings. |
| `SP123_RD_36_sheet_feedback.md` | Error-sheet categories and locally observed recurring difficulties. |
| `second/` | Box lists, first readings, independently written second readings, scripted token comparisons, and adjudications. |
| `AUDIT_SUMMARY.tsv` | Per-page sealed-audit box, difference, token-hunk, revision and unresolved-box counts, with completion status. |
| `crops/CROPS.tsv` | Every crop's source coordinates, rotation, enlargement width, phase, and intended locus. |
| `reports/` | Original structured reports from the first page readers. These are proposals, not the final authority. |
| `review/` | Main-reader records and observation notes; these generate the final apparatus. |
| `notation_snapshots/` | The current notation table supplied with each successive page assignment. |
| `scripts/` | Cropping, apparatus assembly, audit comparison, finalization, hashing, verification, and packaging programs. |
| `run_state.json` | Coordinator state for resumption; it never substitutes for the page and audit completion entries. |
| `source_manifest.tsv` | Identifiers and hashes of the attached sources, without copying their contents into this package. |
| `FROZEN_SHA256.tsv` | Hashes of the frozen page fragments and combined transcription; created at the final freeze. |
| `VALIDATION.json` | Delivery-integrity verification, including the absence of TeX compilation; created at final validation. |

The original attached scans, witness files, and preamble are deliberately absent. The finished TeX uses the supplied preamble conventions; the combined file is a fragment and has no preamble. The separate final crop archive contains the evidence images for changed or unresolved loci. Checkpoint packages and the main final archive contain only the crop manifest, so crop images are not repeatedly stored.

## Reading and audit record

Three page readers work on different pages. A reader receives the next page only after the main reader has inspected the prior return's divergent or unresolved loci and completed that page. The whole-page and native-half readings precede tight detail crops. Details are cropped from native images at no more than 40% of source width and enlarged, using the supplied script.

Only after all 22 first readings are complete does a different page reader receive the page's images and a neutral box list. The reader writes `second.tsv` before seeing any first reading or comparison. The main reader then runs the token comparison and inspects every differing crop. Formatting-only differences are identified as such, but are not silently discarded from the comparison record.

### Historical records and count meanings

Original reports and locked first readings preserve the first-pass record. The plain `counts` objects in working review JSON files are legacy summary fields; some describe an earlier or partially updated state. They are retained for provenance and are not authoritative final totals. Exact first-pass statistics should be read in the original reports, not inferred from a mixed working summary.

For scan 043 boxes B05, B06 and B19, the locked first TSV uses the shorthand `[drawing]`. The full geometric first reading had already been written in the page file. `second/first_page_snapshots/` preserves its exact pre-blind checkpoint 04 copy and provenance; its README explains the limited meaning of the token comparison at those three rows. The original locked inputs and comparison counts remain unchanged.

Current change, inventory and doubt totals are rebuilt from the current canonical lists. Mark-disposition totals come from `decisions.tsv`. Audit box, differing-box, token-hunk, changed-box and unresolved-box totals come from the sealed audit records and `AUDIT_SUMMARY.tsv`. These measures have different units and must not be added together.

A changed audit box may reflect a substantive reading, a changed uncertainty, or a graphic refinement. An unresolved audit box is not the same unit as a doubt entry or a retained MARKS identifier. Formatting-only token differences remain in the comparison record without becoming source-reading corrections. A confirmed first C candidate is not evidence that C had the wrong word or symbol.

## Resumption from a checkpoint

Restore the attached ZIP once alongside this working directory. The source manifest and page order identify the required files. Recreate native halves and per-page kits from those attachments where needed; do not include them in deliverable archives. Recreate a missing crop from its recorded native coordinates, rotation, and enlargement parameters. Consult the latest progress entries and main-review records before continuing; never infer completion from the existence of a draft or a reader report alone. Earlier checkpoint ZIPs remain immutable and are not nested inside later packages.

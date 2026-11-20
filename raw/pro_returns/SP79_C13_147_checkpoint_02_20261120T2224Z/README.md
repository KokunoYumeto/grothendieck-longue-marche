# SP79_C13_147: consolidated diplomatic transcription

The supplied scans are the sole textual authority. Witnesses C and H are comparison drafts, not independent evidence for a reading. No OCR, outside research, or TeX compilation is used.

## Deliverables

The `pages/` fragments and the combined transcription contain the source text in the supplied conventions. The changes log, H collation, decisions table, doubts, inventory, notes, check events, error-sheet feedback, and hand log form the apparatus. Crop references give coordinates in the original scan, before rotation or enlargement. Light foliation whose authorship cannot be established is identified as such in the inventory and notes.

`reviews/` preserves the first reader's returns. `adjudicated/` contains the structured records approved by the main reader and, when completed, blind-reading adjudications. These JSON records are supporting evidence; the checkpoint itself is the ZIP containing the complete work to date. The main reader's direct image inspections are listed in `root_visual_review.tsv`.

`second/` holds each page's box coordinates, the first reading committed before comparison, the independent blind reading, and the scripted token comparison. A second reader is assigned only to pages that reader did not read in the first round. Blind box descriptions state categories of material, without proposed words or digit values.

The comparison preserves exact TeX tokens apart from whitespace. Consequently, its differences include equivalent typesetting syntax as well as competing readings. Every differing box receives a visual adjudication; the comparison JSON retains all token operations within that box. In the audit log, `D differences` counts boxes with one or more token differences and `K changed` counts boxes whose consolidated reading changed. These are not counts of individual tokens. The first-reading files and neutral box lists are committed with SHA-256 before the blind phase and are not edited afterward.

For each differing box, the main reader also assigns every scripted token operation to an explicit decision and ink explanation. The per-page `_token_adjudication.tsv` expands those decisions to one row per operation, including equivalent macro choices and words clipped by a box boundary. The audit approval script checks that no operation is omitted or assigned twice.

Physical line counts follow each reader's explicitly recorded convention (for example, prose baselines or baselines including marginal additions). They document coverage and are not a standardized measure of page density. The changes tables count substantive places against C and H; added uncertainty alone is excluded from those totals.

`progress.log` records page completion, blind audits, checkpoint creation, and the final transcription freeze. `TRANSCRIPTION_SHA256.tsv`, once present, contains the frozen hashes of all page fragments and the combined transcription. `PACKAGE_MANIFEST.tsv` records the contents of this ZIP; it does not include itself in its own hash list.

## Scripts and continuation

The scripts assemble reports from adjudicated records, validate their structural completeness without compiling TeX, prepare blind comparison tables, compare tokens, freeze the transcription, and package the work. The input ZIP must be available separately; source scans, source texts, and regenerable image halves are deliberately excluded from the deliverable. `source/` is expected two directory levels above this work folder, matching the session layout. The source C/H differences TSV contains unescaped quote characters, so it is read with `csv.QUOTE_NONE`.

The chronological progress log and per-page reports establish what has been completed. An in-progress checkpoint may contain drafts that are not yet main-reader approved and does not imply completion of all 24 pages. The final validation requires all pages, all supplied doubt-mark decisions in order, all inventories, and the completed independent second readings.

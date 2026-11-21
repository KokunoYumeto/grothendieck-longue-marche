# SP92_C13_150+151 — working edition and audit record

This package documents a direct visual collation of the 25 supplied scans against witnesses C and H. The controlling instructions are the attached `PROMPT(20261121-153212).md`; the older attached prompt versions are not substituted for it.

## Files and status

`pages/` contains the pages already finalized by the main reader. The combined transcription is assembled in the order in `page_order.txt`, with one cote marker at each cote boundary. It is a LaTeX fragment using the supplied preamble's conventions, standard LaTeX, TikZ and tikz-cd. No TeX compilation, OCR, text-recognition library, or external research is used.

The changes log, H collation, mark decisions, inventory, doubts, notes, hand log and error-sheet feedback are assembled from the page records. A shared place can differ from both witnesses. Counts describe places, not tokens. Added doubt alone and equivalent macro syntax are excluded from change rows; resolving a C doubt is recorded with its crop even when its first proposed reading is confirmed.

`progress.log` is the authoritative record of completed first readings, completed blind audits, checkpoint timing and eventual hash freeze. A working checkpoint is not a claim that all 25 pages or the blind audits are complete. Candidate files under `records/` may still be in preparation; only records marked `root_reviewed` with corresponding files in `pages/` enter the cumulative outputs.

`records/` retains page-level reading evidence, deletion and insertion checks, crop coordinates, notation observations and coverage of every supplied C/H difference row. `records/root_views.json` records crops actually inspected by the main reader. `diff_coverage.tsv` distinguishes substantive reading decisions from alignment, editorial and macro-only differences. The literal-tab parsing repair is documented in `records/input_parsing_note.md`.

`crops/` holds the enlarged, contrast-adjusted reading crops, with original-image coordinates in the records and changes log. These are evidence images, not substitutes for the transcription. The native source scans, supplied witness texts and generated overlapping halves are deliberately excluded from this package because they can be restored from the input attachment. Temporary display-size copies are also excluded.

`second/` contains each page's fixed box list and first reading before the independent audit, followed by the blind second reading, scripted token comparison and main-reader adjudication when those stages have occurred. A second reader receives only that page's images and the box list, using the transcription conventions already supplied, without either witness or the first reading. Box labels are reduced to neutral element types, so they do not disclose a proposed word, symbol, or decision. All 25 first readings and box lists are sealed by hash before any blind reading starts. Reader assignments are recorded in `reader_assignments.tsv`.

Audit comparisons preserve all token differences, including differences of equivalent TeX syntax. Every differing box receives an image adjudication. The audit progress line counts token-difference runs as differences and counts changed adjudicated boxes separately; it also reports the number of differing boxes. Changes following the blind reading retain both written readings in the changes log. Changes of certainty alone are documented there without inflating the counts of readings differing from the source witnesses.

## Reproducible bookkeeping

The scripts in `scripts/` create crops, assemble the cumulative files, finalize reviewed pages, compare the two written readings, validate coverage, package scheduled checkpoints and freeze or verify the final transcription. They never decide a reading from text or perform OCR. Source attachments are expected in the sibling `source/` directory after unpacking the supplied ZIP once. Reading packets and overlapping halves can be regenerated from those sources, but an existing half or decided crop should not be regenerated during an uninterrupted reading.

Checkpoint ZIP names are immutable and sequential; `CHECKPOINTS.tsv` records their timestamps and persistent file identifiers. No previous checkpoint ZIP is included inside another ZIP. At completion, `TRANSCRIPTION_SHA256.tsv` records the hashes of all 25 page files and the combined fragment, and a final verification entry in `progress.log` confirms whether they remained unchanged.

`CHECK_EVENTS.tsv` describes only mathematical checks or uses that actually occurred. A page summary or visual rereading is not represented as a proof check. Unsettled manuscript readings and authorial slips remain visible in the text and notes.

## Witness identifiers

The H collation follows the explicit mapping in the controlling prompt: H page n corresponds to our scan n + 1. Thus `their_page` is `our_scan` minus one; `folder` is the cote. The supplied witness filename is `hua_<cote>_scanNNN.tex`, indexed by our scan rather than H’s page.

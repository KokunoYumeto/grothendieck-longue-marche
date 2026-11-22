# SP92_C13_150+151 — consolidated edition and audit record

This package documents a direct visual collation of the 25 supplied scans against witnesses C and H. The controlling instructions are the attached `PROMPT(20261121-153212).md`; the older attached prompt versions are not substituted for it.

## Files and status

`pages/` contains all 25 pages, finalized by the main reader after the unfamiliar-reader audit. The combined transcription is assembled in the order in `page_order.txt`, with one cote marker at each cote boundary. It is a LaTeX fragment using the supplied preamble's conventions, standard LaTeX, TikZ and tikz-cd. No TeX compilation, OCR, text-recognition library, or external research is used.

The changes log, H collation, mark decisions, inventory, doubts, notes, hand log and error-sheet feedback are assembled from the page records. A shared place can differ from both witnesses. Counts describe places, not tokens. Added doubt alone and equivalent macro syntax are excluded from change rows; resolving a C doubt is recorded with its crop even when its first proposed reading is confirmed.

`progress.log` is the authoritative record of completed first readings, completed blind audits, checkpoint timing and the final hash freeze. All 25 current page records are marked `root_reviewed` and `audited`; their TEX mirrors match `pages/`. Historical first-pass readings and explicitly superseded metadata are retained as evidence, not as competing current readings. Earlier working checkpoints record the state reached at their own timestamps.

`records/` retains page-level reading evidence, deletion and insertion checks, crop coordinates, notation observations and coverage of every supplied C/H difference row. `records/root_views.json` records crops actually inspected by the main reader. `diff_coverage.tsv` distinguishes substantive reading decisions from alignment, editorial and macro-only differences. The literal-tab parsing repair is documented in `records/input_parsing_note.md`.

`crops/` holds the enlarged, contrast-adjusted reading crops, with original-image coordinates in the records and changes log. These are evidence images, not substitutes for the transcription. The native source scans, supplied witness texts and generated overlapping halves are deliberately excluded from this package because they can be restored from the input attachment. Temporary display-size copies are also excluded.

`second/` contains each page's fixed box list and first reading before the independent audit, followed by the blind second reading, scripted token comparison and completed main-reader adjudication. A second reader receives only that page's images and the box list, using the transcription conventions already supplied, without either witness or the first reading. Box labels are reduced to neutral element types, so they do not disclose a proposed word, symbol, or decision. All 25 first readings and box lists are sealed by hash before any blind reading starts. Reader assignments are recorded in `reader_assignments.tsv`.

Audit comparisons preserve all token differences, including differences of equivalent TeX syntax. Every differing box receives an image adjudication. The audit progress line counts token-difference runs as differences and counts changed adjudicated boxes separately; it also reports the number of differing boxes. Changes following the blind reading retain both written readings in the changes log. Changes of certainty alone are documented there without inflating the counts of readings differing from the source witnesses.

## Reproducible bookkeeping

The scripts in `scripts/` create crops, assemble the cumulative files, finalize reviewed pages, compare the two written readings, validate coverage, package scheduled checkpoints and freeze or verify the final transcription. They never decide a reading from text or perform OCR. Source attachments are expected in the sibling `source/` directory after unpacking the supplied ZIP once. Reading packets and overlapping halves can be regenerated from those sources, but an existing half or decided crop should not be regenerated during an uninterrupted reading.

Checkpoint ZIP names are immutable and sequential; `CHECKPOINTS.tsv` records their timestamps and persistent file identifiers. No previous checkpoint ZIP is included inside another ZIP. `TRANSCRIPTION_SHA256.tsv` records the hashes of all 25 page files and the combined fragment, and a final verification entry in `progress.log` confirms whether they remained unchanged.

`CHECK_EVENTS.tsv` describes only mathematical checks or uses that actually occurred. A page summary or visual rereading is not represented as a proof check. Unsettled manuscript readings and authorial slips remain visible in the text and notes.

## Witness identifiers

The H collation follows the explicit mapping in the controlling prompt: H page n corresponds to our scan n + 1. Thus `their_page` is `our_scan` minus one; `folder` is the cote. The supplied witness filename is `hua_<cote>_scanNNN.tex`, indexed by our scan rather than H’s page.

## Completed audit and limits

The fixed box lists contain **389 boxes**. Scripted comparisons identified **326 differing boxes**, comprising **2,164 token-difference runs**; the main reader viewed every differing box. **138 boxes changed** after that review, including localized uncertainty, cancellation scope and graphic details as well as words and mathematical signs. These box counts are not word-error rates. All **1,032 supplied C/H difference entries** are covered, and `decisions.tsv` contains all **101 supplied doubt marks** in their original order. The comparison input hashes preserve all **75 box-list, first-reading and second-reading TSVs**.

The final collation records **790 places**: **383 against C** and **714 against H**, with overlap where both witnesses differ. Confidence is high at 628, medium at 105 and low at 57 logged places. The inventory has 579 elements, and the doubts table has 210 entries, some covering more than one uncertain symbol. The 54 mathematical check events distinguish limited coordinate computations, targeted arguments and counterexamples; no abstract result is certified merely by transcribing it. See the per-page notes for the scope of each check.

Static TeX checks covered brace/environment balance, preamble-defined commands, cancellation wrappers, uncertainty grouping and TikZ matrix separators. They do not certify page layout or replace a TeX compilation; compilation was prohibited and was not performed. Remaining uncertain ink is marked in the transcription, including heavily canceled formulae, tiny retraced indices, clipped typed fragments and the last page's crowded small-compartment caption.

The delivered archive uses pixel-verified lossless crop encodings to retain every crop at its original cropped dimensions. `CROP_ENCODING.md`, `CROP_ENCODING.tsv` and `scripts/restore_png_crops.py` document the stored formats, their checksums and restoration to PNG. Crop filenames in current evidence links are synchronized with those encodings; historical display paths and sealed reading TSVs remain unchanged. Original-PNG container hashes in the historical evidence are distinguished from stored-file and decoded-pixel hashes.

`records/final_audit_verification.json` records the final coverage checks. The 26 transcription hashes are frozen only after the reading and encoding work, then verified unchanged before packaging. The final archive contains the complete deliverables and work evidence, with no input scans, supplied witness files, generated halves or earlier checkpoint ZIPs.

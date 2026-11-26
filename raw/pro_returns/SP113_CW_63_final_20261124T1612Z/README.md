# SP113_CW_63 diplomatic transcription

This edition covers archive scans 004–014 and 016–020, in that order. Scan 015 is outside the supplied task. The controlling instructions are the attached `PROMPT(20261124-134306).md`. The attached source ZIP was extracted once, and its existing internal folders were used directly.

## Final edition

All sixteen pages completed the first reading, main-reader review and independent blind audit. The final changes log records 143 places against witness C: 47 high-confidence, 93 medium-confidence and 3 low-confidence readings. Adding a doubt, or removing a doubt introduced only during this run while restoring supplied C, does not increase that count. Witness H supplies no transcribed text for these pages, so the H collation contains zero data rows.

The blind audit covers 602 boxes. Token comparison produced 482 differing boxes, each with an explicit root decision or a documented formatting-equivalence explanation. The historical first and second readings remain hash-locked. The 52 remaining-doubt entries cover 48 uncertainty marks and four unreadable cancellations. The inventory records 383 transcribed elements. A single 36-entry cross-page notation table heads the final doubts file; the older rolling table is retained only as historical documentation.

The final page fragments and combined transcription are the authoritative readings. Earlier drafts, raw reports, replacement proposals and review findings preserve the sequence of work; their provisional readings are superseded by the final files and the applied-correction receipts.

## Reading and evidence

Three first-pass readers each received one page at a time. Each read the whole page for layout and both supplied halves against witness C, then inspected enlarged crops of uncertain or changed places. The main reader inspected the returned decision crops and decided each departure or unresolved reading. A reader who had not read a page then read its audit boxes from images and coordinates alone, before seeing any comparison. The main reader adjudicated the resulting differences on saved crops.

The final transcription follows the visible ink, including mathematical slips, unusual spelling, cancellations and incomplete punctuation. The prose notes distinguish statements reported from the manuscript from checks actually performed. `CHECK_EVENTS.tsv` records the latter with their scope and outcome. No OCR, external source lookup, or TeX compilation is used.

## Files and state

- `pages/` contains pages accepted by the main reader, each with a corresponding `scan NNN done` entry in `progress.log`.
- `drafts/` preserves the generated working readings, including earlier versions of accepted pages. These are documentation, not the final text.
- `SP113_CW_63_transcription.tex` combines the accepted page files in scan order and has no preamble. It uses the supplied edition macros.
- The changes, doubts, inventory, notes, hand log and error-sheet feedback are assembled from the reviewed page reports.
- `crops/` contains the enlarged evidence images. Their original-image pixel boxes are recorded in the page reports and logs.
- `reports/raw/` preserves each page reader's report before the main reader's acceptance record. `reports/` holds the reviewed reports and calculation results.
- `second/` holds the completed independent audit box lists, first readings, second readings, token comparisons and adjudications. First readings were locked by hash before blind assignments began. The second readers received only image paths, box coordinates and the generic transcription conventions.
- `scripts/` and `documentation/reader_work/` preserve the programs and generated working records used for this edition.

The progress log is the authority for how far a checkpoint has reached. An accepted page is not yet independently audited unless its `scan NNN audited` line is present. A final edition additionally has a `transcription frozen` entry, SHA-256 hashes for all sixteen page files and the combined fragment, and a final unchanged-hash verification.

## Checkpoints

Every checkpoint contains the generated deliverables and documentation accumulated at that time, including all saved crops. Checkpoints have unique sequential names and do not contain earlier checkpoint ZIPs. Unchanged attached source files, scans, witnesses and prompt extracts are excluded. The final ZIP retains all the generated material preserved in the checkpoints.


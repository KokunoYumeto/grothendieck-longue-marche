# Blind second reading protocol

Begin only after all 25 first-pass page files and box lists have been sealed. The assigned reader must not have read this page or its witnesses. Root enforces the recorded eligibility exclusions.

The reader is given only the assigned original scan, its neutral `_boxes.tsv`, and these procedural instructions. Do not open reading packets, witness texts, page candidates, final pages, first-reading TSVs, comparison files, root notes, notation tables, other readers’ files, or global logs. The existing transcription conventions remain the same. No OCR, text recognition, external research, or TeX compilation.

For every box, crop the original image once at its exact recorded coordinates. Save an enlarged, legible copy as `crops/<page>_blind_<box>.png`, using Pillow LANCZOS and optional autocontrast/sharpening. A slanted region may be rotated for reading; retain the original coordinates in a small reader record. Inspect every crop with the image tool yourself. Read all ink belonging to the region, distinguishing cancellation, additions, margin text, underlining, numbers, punctuation and every mathematical decoration. Preserve uncertainty locally rather than supplying expected mathematics.

Write one row for every box in `second/<page>_second.tsv`, columns `box`, `reading`. Use a CSV writer with a literal tab delimiter, preserving real TeX backslashes and any internal newlines. The reading must be your complete independent text for that box, not a comment about it. Preserve overlapping text when it belongs to overlapping regions. Describe any unavoidable boundary ambiguity separately in `second/<page>_reader_record.json`; never inspect the first reading to resolve it. That record should identify the reader, actual viewed crop files and coordinates, and any unresolved visual issues.

When all readings are written, report that the file is complete and stop editing it. Root then runs the scripted token comparison, views every differing box, and records the decision. Never revise the blind reading after learning the first reading or comparison.

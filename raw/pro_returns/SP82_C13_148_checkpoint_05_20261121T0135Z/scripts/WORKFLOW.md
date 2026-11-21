# Processing notes

The supplied archive was unpacked once. `prepare.py packet N` constructs a page-only reader packet and the two native-resolution overlapping halves, reusing existing halves rather than recreating them. The first readers receive one page at a time; the next assignment follows main-reader approval, cumulative record rebuild and the page-done log entry.

The source differences list is a literal TSV, not quoted CSV. Its quotation marks are text tokens. It contains 1,113 data rows. `prepare.py` therefore uses `csv.QUOTE_NONE`; ordinary CSV quote parsing would join lines in scans 031 and 041–046. This was corrected before scan 031 was assigned. No earlier assigned page had a changed row count. The source marks TSV contains 515 marks, M0181 through M0695.

Evidence crops are made once per first-pass place from original pixel rectangles, with Pillow autocontrast, optional rotation, LANCZOS enlargement and sharpening. The headerless crop manifests record filename, x0, y0, x1, y1 and rotation. Native halves and JPEG display copies are reproducible intermediates and are excluded from deliverables. When an image-output size limit prevents a PNG from reaching the reader, a JPEG display copy of the same saved pixels and dimensions is used; a failed transport is not counted as a view. The evidence PNG remains in crops/.

`assemble.py` formats adjudicated review records. It does not read manuscript images, choose readings, perform OCR, or compile TeX. It checks mark coverage at acceptance, writes the literal token comparisons in the second pass, packages the output tree, and records/verifies final SHA-256 hashes. The input scans, source transcriptions and original attachments are not copied into output packages.

Blind second readers are assigned only after all 24 first-pass pages are done. Their box lists and first readings are written before they are given images and box lists. They receive no witness, first reading, approved page or notes.

## Blind comparison records

All first box readings were written and SHA-256 hashed before the fresh image-only readers were assigned. First readings are retained unchanged after adjudication. Comparison uses literal LaTeX, word, digit and punctuation tokens without normalization; the per-box comparison and each non-equal token span are saved separately. In the audit progress lines, B counts boxes, D counts boxes containing at least one literal token difference, and K counts boxes whose adjudicated reading changes the first reading. Every differing box has a main-reader crop decision, including differences caused only by equivalent drawing code, wrapper syntax or visible context. Such equivalent renderings do not inflate the witness changes counts. The changes log separately records actual blind-reading changes with both readings.

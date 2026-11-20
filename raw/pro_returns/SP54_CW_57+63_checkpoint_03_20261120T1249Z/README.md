# SP54_CW_57+63 — consolidated diplomatic second pass

The requested page order is cote 57 scans 022, 023, 073–079, then cote 63 scans 003–014 and 016–020. There are 26 pages.

The page fragments and assembled transcription use the supplied PREAMBLE.tex. The changes, collation, doubts, inventory and reading notes document the final editorial decisions. CHECK_EVENTS.tsv distinguishes the mathematical work actually performed from statements merely carried as the page's assertions. progress.log records completion times and frozen hashes.

The readers/ directory preserves three independent, fresh-context readings per page, observations and crop metadata. adjudication/ preserves the main reader's additional crop evidence. briefs/ preserves every brief version and each page's initial notation snapshot. records/ contains the structured decisions from which the tables were assembled. scripts/ contains the image-cropping and record-assembly code. These are documentation of this run, not additional transcriptions offered in place of the consolidated pages.

Inputs were the user's PROMPT(20261120-103328).md and SP54_CW_57+63.zip. The input archive was unpacked once. Witness C and H are the supplied drafts; the supplied scan pixels are the authority. The input scans, witnesses and original attached files are excluded from this output archive. No OCR, text-recognition library or external mathematical source is used.

The current second-pass brief supersedes first-pass workflow instructions in the witness folders. Their transcription conventions and macro definitions remain in force. H's descriptions of the cote 63 pages are not a text witness and produce no H collation rows.

Inventory scan identifiers include cote and scan (for example 57/022), avoiding ambiguity between the two source PDFs. Source image references identify the input archive's filenames; all decision crops are included in this archive. A retained uncertainty is explicitly marked in the transcription and doubts table.

## Continuation from a checkpoint

Extract a checkpoint into an `out/` directory beside `source/` containing the supplied input archive’s two folders. The scripts derive their base path from their own location. `scripts/prepare_inputs.py` recreates the disposable page bundles from those inputs without changing the completed work. `records/page_order.json` gives the order; a page is complete when its page file, structured record and progress entry are present. Preserve the existing completed records and raw reader returns.

`records/reader_runs.tsv` identifies the brief version assigned to each page, and `briefs/<page>_notation.md` preserves its starting notation table. For an interrupted page, finish and compare all three independent returns before adjudicating it. New pages always receive three new readers with no inherited image context. Root adjudication specifications and included crops document the final choices; record-assembly scripts only format those decisions.

The checkpoint schedule state is kept in `records/checkpoint_schedule.json` after the first scheduled save. It records the last checkpoint creation time and every checkpoint filename. `scripts/checkpoint_watch.py` restores that state when the disposable work state is absent. Its transfer step uses the official Library prepared-upload helper obtained through the current Library skill; the helper modules are environment utilities and can be fetched again. Continue the 45-minute cadence, do not overwrite earlier archives, and do not put checkpoint ZIPs into later archives.

Absolute paths in the original reader reports identify this run’s environment. Resolve an `out/` suffix inside this archive, and a `source/` suffix against the supplied input archive. The human-facing changes table and collation list use archive-relative decision-evidence paths. No source attachment is needed for the included crops; the full scans remain in the original input archive.

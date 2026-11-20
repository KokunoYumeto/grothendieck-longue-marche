# SP49_CW_109 — second diplomatic pass

Status at this build: 21 of 27 supplied scan pages adjudicated. Completed scans: 009, 010, 011, 013, 014, 015, 017, 018, 019, 021, 022, 023, 024, 025, 026, 027, 028, 029, 030, 031, 032.

## Deliverables

- pages/: one final LaTeX fragment per completed scan, using the supplied filenames.
- SP49_CW_109_transcription.tex: concatenated fragments with one cote marker and no preamble.
- PREAMBLE.tex: the unchanged supplied macro definitions.
- SP49_CW_109_changes.md: decisions, C/H comparisons, reader alternatives, crop evidence and confidence counts.
- SP49_CW_109_collation.tsv: only substantive differences from H where H has actual transcribed text (scans 009–011).
- SP49_CW_109_doubts.md: the cumulative notation table, unresolved readings, abbreviation interpretations and legibility assessment.
- SP49_CW_109_inventory.csv: complete element inventory for adjudicated pages.
- SP49_CW_109_notes.md and CHECK_EVENTS.tsv: page content and actual mathematical checks, with limits and provenance.
- progress.log: start, sequential page completion, checkpoint receipts, and eventual freeze/recheck hashes.
- SP49_CW_109_workflow.md and briefs/: reader instructions, revisions and crop accounting.
- readers/, crops/, records/, scripts/: original independent returns, visual evidence, structured main-reader decisions and reproducible assembly/checking scripts.

## Reading method and limits

Three fresh independent readers examine each page, in supplied scan order. Each sees the whole and both supplied halves once, then a tight crop for each place still open. The main reader compares the full returns and adjudicates disagreements on crops. Models: GPT-6 Astra Pro for the main reader and subagents; reasoning effort is not exposed and is not inferred. No OCR, PDF text recognition, outside transcription or web research is used. No human verification is claimed.

Current counts: 366 changed C loci, 57 H collation loci, 223 unresolved readings, 1089 inventoried elements, 26 mathematical check events. These are diplomatic comparison counts, not error-rate estimates: they include literal quote shapes and revised uncertainty marks. H has only descriptions for the other 24 scans.

## Restoring a checkpoint

The archive contains all work documentation written at its creation, but excludes the original attachments, scans, witnesses, derived convenience input copies and older checkpoint ZIPs. Restore its contents under a work/ directory and make the supplied source folders available in the sibling source/ directory. scripts/setup.py can recreate the excluded inputs from those attached sources without replacing existing progress, notation or mathematical events. It finishes with the corrected header-aware context extractor and restores each archived notation snapshot. Retain the supplied same-page clarification/addendum documents; their rationale is recorded in the workflow. Use state.json and progress.log to identify the next scan and the brief actually in force; archived notation snapshots preserve what each completed reader received. A checkpoint may include unfinished reader work for the current page. Do not mark that page complete until all three returns and main adjudication are finished.

scripts/build.py assembles apparatus from records/scanNNN.json. scripts/validate.py performs static LaTeX balance and completeness checks, without compilation. scripts/commit_page.py enforces page order. scripts/freeze.py requires all 27 pages and a documented notation audit before hashing; its check mode verifies the frozen files. Checkpoints are prepared only when the 45-minute interval is due, and a save receipt is acknowledged only after persistence succeeds. Older checkpoint ZIPs are never overwritten or nested.

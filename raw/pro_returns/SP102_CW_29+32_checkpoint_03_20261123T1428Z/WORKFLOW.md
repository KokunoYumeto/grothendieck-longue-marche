# SP102 working edition

The governing instructions are the attached latest prompt dated 2026-11-23. Twenty selected source leaves are read visually, without OCR or external research. Original source images and witnesses are intentionally absent from this archive.

`pages/` contains only leaves whose main image review and done entry are complete. `drafts/` contains unfinished first-reader candidates. Per-page reports in `reports/` preserve the witness readings, visible evidence, uncertainty decisions, inventories, notation observations, and proposed independent-reading boxes. The main reader records its decision in each report before moving the leaf.

The three first readers receive one page at a time in source order. The next page is assigned when a first reader is free after returning its previous page; main adjudication continues in parallel. After every leaf is done, another reader receives only that leaf’s images and neutral box list. The first and second readings are saved separately before token comparison; all disagreements are adjudicated on the saved second crops.

`crops/` contains the enlarged visual evidence, with original whole-image pixel coordinates recorded in the reports. Running text is encoded as text; true diagrams and drawings are typeset. The scripts assemble the deliverables from the reviewed reports, compare independent readings, and verify structural consistency and final hashes. They perform no text recognition and no TeX compilation.

The first work timestamp is in `progress.log`. Checkpoints are complete snapshots at 45-minute intervals. Existing checkpoint ZIPs, attached sources, and unchanged source extractions are never embedded in a snapshot.

## Rebuilding the current deliverables

Run `python scripts/assemble.py` from this directory to rebuild the combined fragment and logs from finished pages. Run `python scripts/audit.py` for structural checks. Only after all pages are finished, `python scripts/assemble.py --boxes` writes the first-reading box tables for the blind stage. Do not rerun `--boxes` after blind readings begin; those first tables are the pre-comparison record.

The reports and progress log are the record of completed work. The working notation file is carried forward to each newly assigned first reader.

The per-page writer scripts preserve first-reader construction history. Do not rerun them over a completed page: the final page files and reviewed JSON reports also contain main-reader and blind-audit decisions. The assembler is the supported way to regenerate combined deliverables.

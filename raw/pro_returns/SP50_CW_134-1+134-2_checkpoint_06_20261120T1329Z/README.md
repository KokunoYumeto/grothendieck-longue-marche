# SP50_CW_134-1+134-2 — second-pass diplomatic transcription

This return records the supplied 29 scans, in their page-map order: cote 134-1 scans 002, 004–007; cote 134-2 scans 146–169. It uses only the supplied scan images and the two supplied draft witnesses. No OCR, external text, other reproduction or internet research is used.

## Main files

- `pages/`: the consolidated page fragments, with the same filenames as witness C.
- `SP50_CW_134-1+134-2_transcription.tex`: page fragments concatenated in order, without a preamble.
- `PREAMBLE.tex`: the supplied macro definitions, unchanged.
- `SP50_CW_134-1+134-2_changes.md`: counts, consequential changes, decisions against either witness, and remaining doubts by page.
- `SP50_CW_134-1+134-2_collation.tsv`: actual reading differences against H; no rows for scan 002, where H has no text.
- `SP50_CW_134-1+134-2_doubts.md`: running notation, unresolved places, abbreviations, retained slips and legibility assessment.
- `SP50_CW_134-1+134-2_inventory.csv`: all page elements and states.
- `SP50_CW_134-1+134-2_notes.md`: short page notes; no research beyond these pages.
- `CHECK_EVENTS.tsv`: the actual mathematical or documentary uses/checks behind the notes, with checking distinguished from reading.
- `SP50_CW_134-1+134-2_workflow.md`: briefs, revisions, crop counts and observations.
- `progress.log`: UTC progress, checkpoint history, freeze hashes and final hash verification.

## Supporting audit record

`readers/` preserves every independent full reading and structured report. `decisions/` preserves the main reader’s consolidated decisions. `evidence/` contains newly generated tight crops, each with its source-pixel box and image processing in `crops.jsonl`; it does not contain the supplied whole-page or half-page scans. A path beginning `out/` in a reader report is relative to the session workspace; inside this archive, remove that leading component. `briefs/` preserves each used brief and each page’s notation snapshot. The images named under `source/` remain in the original attachment.

`scripts/` holds the actual preparation, crop, collation, inventory, validation and packaging programs. These programs do not recognize handwriting. They read existing witness text, process pixels for human-style visual inspection, and format the recorded decisions. `state.json` and `page_order.json` document execution order. Checkpoint ZIPs contain all work written so far and never contain earlier checkpoint ZIPs or the original attachments.

The supplied witness descriptions identify C as the Codex first pass and H as the Commutator project snapshot at commit `aef7db2`. Those descriptions are provenance supplied with the task, not an independent assessment of either witness. Both witnesses remain drafts; scan ink governs every reading.

This is a diplomatic transcription, not a corrected mathematical edition. A retained doubt is a statement about what this scan can establish. A mathematical expectation or an agreement between readers does not supply missing ink.

Completion is recorded in `progress.log` and `summary_counts.json`. In a checkpoint, files and counts describe the completed pages to that time; work in progress remains in its reader directories. The final archive contains all 29 completed pages and the frozen-hash verification.

## Resuming a checkpoint

The upload receipt for a checkpoint is necessarily written after that ZIP has been sealed. It is therefore present in the next checkpoint, not inside the ZIP whose upload it records. When restoring checkpoint NN, take its number and its `checkpoint archive created` line as authoritative for the checkpoint schedule: set the next checkpoint to NN+1 and the previous checkpoint time to that creation time. Do not overwrite or rebuild the restored checkpoint. Its successful durable upload is established by the conversation or the later receipt, not by a receipt presumed to be inside it.

Restore the archive into `out/`, restore the original supplied package separately into `source/`, and rebase `page_order.json` paths to the new workspace if necessary. The source package remains the authority for scan and witness inputs; they are not duplicated here. Preserve the completed-page order in `state.json`. An unfinished page must still receive all required independent readings and main adjudication before its `done` event; do not promote partial reader files to a completed page. The scripts, reader briefs, notation snapshots, recorded decisions and generated crops preserve the work already performed.

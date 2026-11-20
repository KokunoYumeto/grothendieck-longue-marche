# SP40_CW_81 — second-pass diplomatic transcription

This package contains the consolidated transcription and its reading record for cote 81, scans 2–8 and 10–26 (24 scans). Scan 9 is outside the supplied task.

During the work, checkpoint copies contain the completed prefix recorded by the `scan NNN done` lines in progress.log, together with any current-page reader work. Only the final archive has all 24 completed page records and the transcription freeze/recheck entries. The preparation script can rebuild a page packet from the original attachments after restoration.

The supplied scan images govern every reading. Witness C is the prior Codex transcription; witness H is the supplied Commutator transcription at commit aef7db2. Witness S is the supplied sweep correction table. The original attachments, whole scans, and witness directories are excluded from this deliverable; their SHA-256 identities are in source_identity.json.

The numbered scan files are in pages/. SP40_CW_81_transcription.tex concatenates those files in scan order and is a LaTeX fragment. PREAMBLE.tex is the supplied macro definition file. The changes, H collation, doubts, inventory, notes, check events, progress and workflow documents accompany it.

Independent proposals and visual-reading records are in readers/<scan>/<A|B|C>/. C in that directory name denotes the third current reader, distinct from witness C. Main-reader decisions are in records/; newly made adjudication crops are in crops/. Crop paths in the logs are relative to this package. Brief versions and notation snapshots are in briefs/. Scripts preserve the generation and structural checking procedures.

The approved `records/scanNNN.json` files govern the consolidated tables. Intermediate `checks/*record_draft.json` files and their assembly scripts preserve the mechanical preparation before root approval; their pending flags and earlier wording remain part of the work history. Root's later approved decisions are in the numbered records. Mathematical-check certificates and the root's crop-decision notes are also retained in checks/.

A checkpoint is a complete snapshot of all work written at its creation time. Earlier checkpoint ZIPs and source attachments are never nested inside it. Final completion and the transcription SHA-256 freeze and recheck are recorded in progress.log.

## Restoring the full crop record

Beginning with checkpoint 12, the complete archive uses reversible storage for the crop PNGs to fit the destination's file-size limit. The original checkpoint snapshot is retained locally, and the saved transport ZIP represents every original entry. TeX, tables, reports and scripts remain ordinary files at their original paths. The archive also contains `RESTORE_CHECKPOINT.py`, `CHECKPOINT_TRANSPORT_README.txt` and a manifest recording every original path, file size and SHA-256.

Extract `RESTORE_CHECKPOINT.py` and run it with `--archive ARCHIVE.zip --destination restored_work` to reconstruct the complete original file tree in an empty destination. The transport README gives the validated Python, Pillow, libwebp and zlib versions and the exact PNG serialization settings. Each restored file must pass its recorded size and SHA-256 checks. The packaging audit records the direct original-byte comparisons actually performed for that snapshot; checkpoint 12 passed all 1,317 original entries. Later audits are retained separately. Storage verification does not adjudicate manuscript ink or validate a mathematical assertion.

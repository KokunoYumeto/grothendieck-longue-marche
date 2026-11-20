# SP40_CW_81 — second-pass diplomatic transcription

This package contains the consolidated transcription and its reading record for cote 81, scans 2–8 and 10–26 (24 scans). Scan 9 is outside the supplied task.

During the work, checkpoint copies contain the completed prefix recorded by the `scan NNN done` lines in progress.log, together with any current-page reader work. Only the final archive has all 24 completed page records and the transcription freeze/recheck entries. The preparation script can rebuild a page packet from the original attachments after restoration.

The supplied scan images govern every reading. Witness C is the prior Codex transcription; witness H is the supplied Commutator transcription at commit aef7db2. Witness S is the supplied sweep correction table. The original attachments, whole scans, and witness directories are excluded from this deliverable; their SHA-256 identities are in source_identity.json.

The numbered scan files are in pages/. SP40_CW_81_transcription.tex concatenates those files in scan order and is a LaTeX fragment. PREAMBLE.tex is the supplied macro definition file. The changes, H collation, doubts, inventory, notes, check events, progress and workflow documents accompany it.

Independent proposals and visual-reading records are in readers/<scan>/<A|B|C>/. C in that directory name denotes the third current reader, distinct from witness C. Main-reader decisions are in records/; newly made adjudication crops are in crops/. Crop paths in the logs are relative to this package. Brief versions and notation snapshots are in briefs/. Scripts preserve the generation and structural checking procedures.

The approved `records/scanNNN.json` files govern the consolidated tables. Intermediate `checks/*record_draft.json` files and their assembly scripts preserve the mechanical preparation before root approval; their pending flags and earlier wording remain part of the work history. Root's later approved decisions are in the numbered records. Mathematical-check certificates and the root's crop-decision notes are also retained in checks/.

A checkpoint is a complete snapshot of all work written at its creation time. Earlier checkpoint ZIPs and source attachments are never nested inside it. Final completion and the transcription SHA-256 freeze and recheck are recorded in progress.log.

# SP48_CW_104 — second-pass diplomatic transcription

Before the final freeze, `progress.log` identifies the pages actually completed; checkpoints may contain a partial run.

The authoritative consolidated text is in `pages/`, one file for each archive scan 002–017, and in their ordered concatenation `SP48_CW_104_transcription.tex`. The latter is a LaTeX fragment with no preamble. `PREAMBLE.tex` is the supplied macro set; `SP48_CW_104_standalone.tex` is a convenience wrapper.

The changes log identifies differences against both supplied AI witnesses and records the image evidence, independent readers' alternatives, and the main reader's decision. The collation TSV includes differences against witness H only; differences of equivalent macro syntax are excluded. The doubts file begins with the running notation table. The inventory, notes, check-event register, progress log, and workflow record accompany them.

`records/scanNNN/reader_A`, `reader_B`, and `reader_C` retain the three independent page readings and their observation records. These are documentary alternatives, not three additional consolidated texts. `records/scanNNN/decision.json` is the structured source of the final page's records. The recorded evidence is limited to observations and conclusions, not hidden deliberation. `briefs/` preserves the briefs and notation snapshots used on each page. Decision crops and their coordinate manifests remain with the work; the original scan images, original witness files, and input archive are deliberately excluded.

Only the attached archive and prompt were used. No OCR, text recognition, PDF text layer, external edition, or web research was used. Mathematical source assertions remain as written; actual mathematical checks, when performed, are separately identified in `CHECK_EVENTS.tsv`. A reading agreement is not a proof.

Source: Montpellier archive of Alexander Grothendieck, cote 104, scans 2–17. Witness C consists of the supplied H104-01 and H104-02 first-pass files. Witness H is the supplied Commutator project transcription and drawing files at commit aef7db2. The source manifest records input identity without redistributing the inputs.

Structural validation checks LaTeX delimiters and environment balance, marker order, and exact concatenation. It is not a compilation or a substitute for reading the scans. Page and combined-text hashes are frozen only after all page decisions and the notation reconciliation; the final hash verification is recorded in progress.log.

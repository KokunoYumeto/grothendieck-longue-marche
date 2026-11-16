# Work records and authority of the delivered files

The authoritative diplomatic witness is `../MPL_36_002-052_transcription.tex` together with the 31 files in `../pages/`. The inventory and doubts file describe that frozen witness. The research notes are separate and were written after the freeze and context opening recorded in `../progress.log`.

`frozen_hashes.json` records the pre-context SHA-256 values. `final_verification.json` records the final comparison with those values and the other structural checks. The final hash check does not remove the uncertainty marked in the diplomatic text.

Historical page-writing, audit, geometry and assembly scripts are retained to document the work and checkpoints. Their intermediate readings and provisional inventories are superseded by the delivered page files, final doubts and final inventory. **Do not rerun a script that writes a page file, assembles the transcription or freezes it again after context access.** The main script names include `assemble.py`, `reconcile.py`, `final_geometry.py`, `final_table_geometry.py`, `normalize_tikzcd.py` and `freeze.py`; earlier page-specific scripts can also write text.

`notes_data.py` and `register_data.py` contain the final research-note and register data. `build_notes.py` and `build_register.py` render those notes and perform actual searches against the separately supplied context. Their query records identify all three searched files and locations, while preserving only brief matched excerpts. `notes_standing.md`, `notes_register.md`, `notes_bibliography.md` and `notes_final_verification.md` supply the corresponding sections of the final notes. The algebraic checks in `own_calculation_checks.md` explain the main restricted tests without changing the manuscript.

`validation_wrapper.tex`, `run_validation.sh`, `validation_report.md` and `validation/` document compilation and selected diagram-layout checks. The wrapper uses deliberately large pages and simplified display definitions for the prescribed markup; it is a QA fixture, not a finished critical edition. Generated QA PDFs, image crops, temporary TeX caches, the attached scans, the attached context and complete external sources are omitted from the ZIP.

All image reading, transcription and audit work was performed in one stream, without OCR or helper agents. The delivered order is the supplied scan order, including reused sheets and the cancelled draft; it is not a conjectured chronological order of composition.

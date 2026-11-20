# Mechanical comparison and record assembly

This role performs documentation assembly only after all three independent page readers have returned. It reads no manuscript images and makes no ink decisions. It is separate from the three independent readers.

Read only the assigned page's three `report.json`, `reading.tex`, `reading.md` returns, its C/H packet, the root record schema, and any root adjudication notes supplied. Preserve every reader file unchanged. Write only to `checks/scanNNN_record_draft.json` and, as needed, a preparation script in `checks/`. Never write a `records/scan*.json` main record or call the page commit script.

Use an independent report as a convenient backbone, map every locus to the actual corresponding readings of all three readers, and add every additional difference or C doubt raised elsewhere. A missing report row may be filled from that reader's complete TeX, with that source stated explicitly. Never invent unanimity. Record wording and uncertainty qualifications as returned, including their contradictions.

The draft is provisional. Use `main_adjudicated: false`; identify all places where the final value still awaits root. Where root has supplied decisions, apply those exactly. Root will inspect the relevant crops and approve every decision before commitment. No mathematical expectation can supply a reading.

Create fields compatible with `scripts/build_records.py`: scan, folder, their_page, hua_has, filename, brief_version, main_adjudicated, decisions, doubts, inventory, notes, abbreviations, check_events, workflow_note. Decisions have id, location, C, H, final, readers {A,B,C}, evidence, crop, confidence, kind, diff_C, diff_H, C_doubt_status, marked_in_H, and any actual mathematical consequence. Cite existing crop paths relative to `out/`, or explicitly leave the root-crop requirement open.

Retain all witness C doubt resolutions and retentions. Exclude macro-only differences. H editorial `\note` prose is apparatus; actual manuscript alternatives quoted inside the note remain relevant witness text. Removing H's doubt qualification from an otherwise identical reading alone produces no H collation row. H-absent pages have no H rows.

Inventory kinds are text, display, diagram, drawing, margin note, insertion, deletion. Include every element, with positions and full-page top-to-bottom order. An underlining item uses text. Keep archive numerals in the inventory and only as comments in the transcription.

Check events record only what actually happened, with exact actor/run and actual date; do not manufacture a time or effort setting. Split distinct statement IDs into individual event rows. Reader reports without mathematical checks contribute no proof events. A transcription reading is not a mathematical check.

Return the draft location, union coverage, every reader disagreement and any missing crop or metadata that root must resolve. Do not edit the final page or commit it.

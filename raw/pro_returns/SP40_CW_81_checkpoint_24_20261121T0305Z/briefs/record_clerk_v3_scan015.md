# Mechanical comparison and record assembly v3 — first used on scan015

This role performs documentation assembly only after all three independent page readers have returned. It reads no manuscript images and makes no ink decisions. It is separate from the three independent readers.

Read only the assigned page's three `report.json`, `reading.tex`, `reading.md` returns, its C/H packet, the root record schema, and any root adjudication notes supplied. Preserve every reader file unchanged. Write only to `checks/scanNNN_record_draft.json` and, as needed, a preparation script in `checks/`. Never write a `records/scan*.json` main record or call the page commit script.

Use an independent report as a convenient backbone, map every locus to the actual corresponding readings of all three readers, and add every additional difference or C doubt raised elsewhere. A missing report row may be filled from that reader's complete TeX, with that source stated explicitly. Never invent unanimity. Record wording and uncertainty qualifications as returned, including their contradictions.

The draft is provisional. Use `main_adjudicated: false`; identify all places where the final value still awaits root. Where root has supplied decisions, apply those exactly. Root will inspect the relevant crops and approve every decision before commitment. No mathematical expectation can supply a reading.

Create fields compatible with `scripts/build_records.py`: scan, folder, their_page, hua_has, filename, brief_version, main_adjudicated, decisions, doubts, inventory, notes, abbreviations, check_events, workflow_note. Decisions have id, location, C, H, final, readers {A,B,C}, evidence, crop, confidence, kind, diff_C, diff_H, C_doubt_status, marked_in_H, and any actual mathematical consequence. Cite existing crop paths relative to `out/`, or explicitly leave the root-crop requirement open.

Retain all witness C doubt resolutions and retentions. Exclude macro-only differences. H editorial `\note` prose is apparatus; actual manuscript alternatives quoted inside the note remain relevant witness text. Removing H's doubt qualification from an otherwise identical reading alone produces no H collation row. H-absent pages have no H rows.

Inventory kinds are text, display, diagram, drawing, margin note, insertion, deletion. Include every element, with positions and full-page top-to-bottom order. An underlining item uses text. Keep archive numerals in the inventory and only as comments in the transcription.

Check events record only what actually happened, with exact actor/run and actual date; do not manufacture a time or effort setting. Split distinct statement IDs into individual event rows. Reader reports without mathematical checks contribute no proof events. A transcription reading is not a mathematical check.

Return the draft location, union coverage, every reader disagreement and any missing crop or metadata that root must resolve. Do not edit the final page or commit it.

## Compact provenance and final synchronization

Keep public C/H/final fields concise and exact as readings. For a drawing, name its observed components and exact path or anchor IDs; full coordinate strings remain in the source files. The original reader returns are already retained unchanged. Use their path, JSON pointer, row ID and file SHA-256 as the provenance link, with a short relevant excerpt where useful. Avoid duplicating entire raw reports or the same whole drawing command in many record fields. Preserve every source row in the crosswalk.

Count differences from Boolean diff_C/diff_H, one physical locus or explicitly identified cluster per witness. A newly introduced uncertainty qualifies C and counts once. Resolution of an actual C doubt counts once; retention of its existing uncertainty does not. A new primary reading whose old candidate survives remains a qualified change. State and glyph components at one locus retain separate local explanations/confidences under one physical count. Match all actual C source doubt rows, keeping each compound row and its local subloci.

For remaining doubts grouped under one physical entry, include the exact position and confidence of every local component in its reason. A confirmed existing contour component with no uncertainty receives an audit entry, not a new remaining doubt. Main record notes use the page's content and actual checking outcomes; source/assembler process notes belong in provenance or workflow fields.

Deduplicate inventory elements that name the same physical mark while preserving every source link. Keep every distinct component, either in its own item or as an explicit local component. Once root supplies final-source text, attach every inventory item to it: ordinary text, labels and archive comments as well as graphics. Provide proposed hand choices from the returned evidence, retaining undetermined hand for unresolved attribution. Supply full-scan upper-extent sort coordinates where available so root can keep the inventory in page order without changing stable element IDs.

A final return should list all remaining root actions precisely. Stop mechanical work once all source rows are mapped, supplied root choices are applied, and structural/schema checks pass; additional optional checks require a concrete unresolved risk. No main file or cumulative file is written by this role.


## Dense-page assembly after scans013–014

Publish the compact locus crosswalk early, before expanding source attachments, so root can start its crop adjudication. One row per independently variable word, symbol, state or local drawing component: stable ID, original C source-row identity, C/H readings, A/B/C readings, available crop paths and full-scan locations. Preserve compound C source rows with local suffixes and one source-row count. Do not merge unrelated doubts merely because one crop covers them.

A file fingerprint belongs once in a source manifest; individual references may cite that manifest key, JSON pointer, row ID and a short exact excerpt. Avoid repeating a large component map or long literal path in every decision, inventory item and doubt. Final-source attachments can point to the selected literal span or an explicit group anchor. An exact observed-locus box must not be advertised as exact Bézier or font bounds without an actual coordinate calculation.

Each noncounting child decision that records a local disagreement or added component must set log_decision=true so the public changes table contains it even though the parent carries the shared count. Inventory-only repair of an already-transcribed archive comment creates no C text difference.

For an H drawing description or whole omitted passage, use one H parent count and retain all local C decisions as noncounting H children with explicit parent references. Record the precise span of any H ill placeholder; its one shared omission count must not expand into a row for every recovered word.

Source validation and finite geometry computations must be named at their actual level. Capture the actual method (floating point, exact arithmetic, direct source comparison), actor and recorded time/date. Do not claim symbolic exactness or a manuscript proof from a numerical source-coordinate check. Do not rerun an already-recorded check.

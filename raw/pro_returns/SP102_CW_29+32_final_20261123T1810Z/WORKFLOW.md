# SP102 completed diplomatic edition

The governing instructions are the attached latest prompt dated 2026-11-23. Twenty selected source leaves are read visually, without OCR or external research. Original source images and witnesses are intentionally absent from this archive.

`pages/` contains only leaves whose main image review and done entry are complete. `drafts/` contains unfinished first-reader candidates. Per-page reports in `reports/` preserve the witness readings, visible evidence, uncertainty decisions, inventories, notation observations, and proposed independent-reading boxes. The main reader records its decision in each report before moving the leaf.

The three first readers receive one page at a time in source order. The next page is assigned when a first reader is free after returning its previous page; main adjudication continues in parallel. After every leaf is done, another reader receives only that leaf’s images and neutral box list. The first and second readings are saved separately before token comparison; all disagreements are adjudicated on the saved second crops.

`crops/` contains the enlarged visual evidence, with original whole-image pixel coordinates recorded in the reports. Running text is encoded as text; true diagrams and drawings are typeset. The scripts assemble the deliverables from the reviewed reports, compare independent readings, and verify structural consistency and final hashes. They perform no text recognition and no TeX compilation.

The first work timestamp is in `progress.log`. Checkpoints are complete snapshots at 45-minute intervals. Existing checkpoint ZIPs, attached sources, and unchanged source extractions are never embedded in a snapshot.


## Completed coverage

All twenty selected leaves have finished main image reviews and independent second-reader adjudications. The primary sealed audit contains **380 boxes**, **304 differing boxes**, and **46 changed boxes**. The two separately sealed coverage supplements add **2 boxes**, **1 differing box**, and **0 changed boxes**: **382 boxes in all**. A changed box can contain multiple changed places, and two overlapping boxes can cover the same place; these box counts are therefore distinct from the C/H change counts.

The C/H comparison records 174 changed places against C and 372 against H; 150 affect both, for 396 distinct changed places. Their confidence counts are 222 high, 83 medium and 91 low. There are 796 inventory entries, 229 remaining doubt entries and 21 check events. Certainty qualifications and pure macro differences are excluded from these change counts.

The last primary audit finished on 2026-11-23 at 17:55:25 UTC. No image-reading decision remains pending. Remaining ink ambiguities are explicitly retained in the transcription and doubts table. The final transcription hash record and its verification are in `frozen_sha256.json` and `progress.log`.

The reports retain historical first-stage observations and sealed pre-comparison readings. Later root decisions and final page files govern the accepted transcription; historical first readings are not rewritten to conceal the changes. No per-page construction or adjudication writer should be rerun over the finished edition.

## Rebuilding the current deliverables

Run `python scripts/assemble.py` from this directory to rebuild the combined fragment and logs from finished pages. Run `python scripts/audit.py` for structural checks. Only after all pages are finished, `python scripts/assemble.py --boxes` writes the first-reading box tables for the blind stage. Do not rerun `--boxes` after blind readings begin; those first tables are the pre-comparison record.

The reports and progress log are the record of completed work. The working notation file is carried forward to each newly assigned first reader.

The per-page writer scripts preserve first-reader construction history. Do not rerun them over a completed page: the final page files and reviewed JSON reports also contain main-reader and blind-audit decisions. The assembler is the supported way to regenerate combined deliverables.

## Blind reading records and final verification

After the one-time box-table generation, seal all twenty manifests and first tables with `python scripts/audit.py --seal PAGE` before dispatch. Never regenerate or edit sealed tables. Different readers write independent tables before comparison; all exact TeX tokens, paragraph boundaries, and quote/dash ligatures are compared. Each differing box receives a visible-evidence decision in its comparison record. The audit counts boxes: a changed box contains at least one changed reading, while individual changed places are separately recorded in the changes log. A documentary `% no foreground ink` sentinel represents an empty source rectangle only in the reading table.

Run `python scripts/audit.py --compare PAGE --reader /root/READER`, then adjudicate and run `--finish-audit PAGE`. After all audits, rebuild with `assemble.py`, run `audit.py --freeze`, and finally `audit.py --verify-frozen`. These validate the exact twenty page files, the combined fragment, and the hashes of all sealed and independent reading tables.

### Certainty qualifications

A completed comparison may mark a decision with the Boolean `certainty_only_edit: true` when the edit only qualifies uncertainty. An absent flag means false. The flag must be Boolean; a decision cannot have both `changed: true` and `certainty_only_edit: true`. Mixed boxes remain substantive and document their qualifications in their decision evidence. Only `changed: false` qualifications enter the separate certainty section. On the next rebuild, `assemble.py` places these decisions in a separate **Certainty qualifications after independent image reading** section under the relevant page in the notes. Each entry retains the first reading, independent second reading, decision, visible evidence, and saved crop reference, and identifies whether it came from the primary audit or a coverage supplement.

These qualifications are excluded from substantive C/H change totals and recurring-error counts. The section is derived from completed comparisons without modifying reports or appending `changes` or `audit_changes` entries. If an existing `audit_changes` entry repeats the same box and first/second pair, that entry is displayed once in the certainty section. Other entries within the same box remain separate, since one box can contain several substantive changed places. Primary box-audit counts retain their existing meaning and calculation.

### Supplemental coverage

Two separately sealed coverage supplements preserve the original blind-stage records while supplying additional independent coverage:

| Page | Supplemental box |
| --- | --- |
| C29-06_29_scan122 | S001 |
| C29-06_29_scan123 | S001 |

Their box manifests, first readings, independent second readings, seals, and comparisons are in `second/supplemental/`. Each seal records the page, reason, timestamp, and byte hashes of the supplemental box and first-reading tables. The original primary manifests, first and second tables, seals, and comparisons remain unchanged. The required independent crops are `crops/second/PAGE_S001.jpg`.

After the supplemental reader has published the second table, run `python scripts/supplemental_audit.py --compare PAGE --reader /root/READER`. Adjudicate every differing supplemental box with a nonempty decision, evidence, and crop reference, plus a Boolean `changed` value; then run `python scripts/supplemental_audit.py --finish PAGE`. Identical readings still require the saved independent crop. Completion is recorded separately as `supplemental_audit` in the report, with `total_independent_boxes` equal to the unchanged primary box count plus the supplemental count. A matching retry preserves completed records and can restore an interrupted completion marker or log entry.

Both `audit.py --freeze` and `audit.py --verify-frozen` now require these two completed S001 audits in addition to all twenty primary audits. They recheck supplemental seal identity and the box/first byte hashes, the second-table hash stored in the comparison, strict TSV structure and exact coverage, recomputed comparison readings and token differences, adjudications, reader independence, crop files, completion counts and timestamps, and the matching report completion records. Existing supplemental comparisons without a tokenizer-version field are supported by recomputing their differences with the same primary tokenizer; newly created comparisons record the version explicitly.

The frozen transcription manifest still contains exactly the twenty page files and the combined fragment. Supplemental validation is an additional gate and does not change primary audit counts or the original primary validation rules. Rebuild and run the final freeze commands only after page editing and adjudication are complete.

Final freeze and verification also require every report to be marked done, explicitly main-reviewed, and carry a valid completion timestamp.

## Final witness-count reconciliation

The final accounting review excludes a witness-change score whenever that complete witness reading remains an admitted alternative with the same source state, scope and placement, and no mandatory additional ink. A preference change alone is excluded. Genuine resolution of a witness doubt or mandatory extra ink remains a reading change. Seventeen additional rows were reclassified under this rule; `reports/final_counting_adjustments.json` preserves their original flags, final flags, readings and reasons. No page, first/second table, comparison decision, seal or recorded audit K count was changed. The K values record the completed first-to-final box adjudications; they are distinct from this final comparison against C and H.

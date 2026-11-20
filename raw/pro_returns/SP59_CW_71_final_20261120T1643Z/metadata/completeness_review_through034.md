# Mechanical deliverable-completeness review through scan 034

> Historical snapshot: scan-008 unknown-status statements below are superseded by the dated exact-replay update at the end of this review.

Snapshot: 2026-11-20 16:18:44 UTC. Text records and filenames only; no image was opened or processed, and no mathematical or reading decision was made. Root is continuing the second image readings, so audit completion, the freeze, final hashes and the final ZIP remain finalization work rather than findings of this review.

## Findings requiring final text

1. `LEGIBILITY.md` is absent. Consequently `SP59_CW_71_doubts.md` still says “The reader's final assessment has not yet been entered.” An unapplied proposal is in `metadata/legibility_summary_proposal.md`.
2. `FEEDBACK_EXTRA.md` is absent. The generated error-sheet feedback still ends “No additional recurring category has yet been recorded.” The ten-category counts are complete, but this provisional sentence needs the reader's final confirmation or replacement. An unapplied proposal is in `metadata/feedback_summary_proposal.md`.
3. `HAND_LOG_EXTRA.md` is absent. The required hand log itself is populated; this is not a missing deliverable. No separate final cross-page reconciliation statement is present yet. Only the sole reader can confirm completion of the requested cross-page notation reconciliation.
4. The previously documented crop-metadata exception remains: `008_slanted.jpg` has no recovered exact source box or rotation. The complete crop appendix says so explicitly and excludes rejected numerical candidates. No substitute coordinates were inferred.

## Routing defect fixed with explicit root authorization

`records.resolved_status()` previously treated statuses beginning “C doubt resolved…” / “C doubts resolved…” as unresolved because it recognized only bare resolved prefixes. Exactly 16 already-resolved rows were routed to the wrong generated section: eight on scan 007 and eight on scan 008. The function now recognizes that precise explicit prefix. The records and readings were not changed.

Before: 201 remaining / 144 resolved. After: 185 remaining / 160 resolved. Exact row locators and unchanged statuses are listed in `metadata/resolved_status_routing_fix.tsv`. Current snapshot: 185 remaining / 160 resolved.

## Requirements verified

- All 25 expected page filenames match `page_map.tsv`; there are no extra or missing page files.
- The combined TeX is a fragment, has one `\cotefile{71}`, and contains all 25 `\scanpage` markers in the requested order, with no document preamble.
- All ten required top-level deliverable files are present: transcription, changes, collation, doubts, inventory, notes, sheet feedback, hand log, CHECK_EVENTS and progress.log.
- Exact requested collation and inventory column names are present. CHECK_EVENTS has its six required semantic fields. The bundled validator reports no schema or structural errors.
- H has zero collation rows for scans 009, 015, 024, 026 and 028, as required. Every H page number equals our scan minus one; all rows use valid kinds and yes/no doubt flags. H collation currently has 499 rows.
- Inventory has 549 rows, all `transcribed=yes`, with no empty required fields. Every `kind` and `sheet_kind` is in the prompt's allowed sets.
- The doubts notation table contains 77 entries covering all 25 scans, with no empty required notation fields. There are 102 abbreviation entries. Empty abbreviation tables on 024, 026 and 028 are not by themselves evidence of missing content.
- The hand log contains 50 entries with all four required metadata fields filled. Only scan 009 has no hand-habit entry; its recorded content is printed material, so that absence is not a mechanical defect.
- All ten error-sheet categories are generated. Their reference lists contain exactly 516 distinct changed-place IDs, with no dangling or duplicate IDs. Their counts agree with the active change records.
- The changes log has all 25 page sections, per-page unresolved sections, counts, consequential corrections and both relevant witness-S IDs: SA01-K71-05 on 010 and SA01-K71-02 on 033.
- Notes have one section for each of the 25 scans. Check events identify their notes or manuscript places and include date, model/run metadata, event type and outcome; no required event cell is empty. Event labels were not evaluated as mathematical claims in this mechanical review.
- The complete crop appendix contains all 234 known source boxes, including the five early boxes added to its table. The three scan-033 margin aliases are derivatives of one source crop and are excluded from the source-box count.
- No image, JSON, nested checkpoint ZIP or final ZIP is present inside the output tree. Python bytecode caches are intermediate files to be excluded by the packaging script.

## Finalization status

Second-reading warnings from `validate --complete` reflect the audits root is actively performing; this review does not add audit events or mark any page audited. The freeze/hash lines and final package should be produced after that work. `WORK_IN_PROGRESS.md` should be brought to its final state before delivery. Missing optional helper files such as NOTES_EXTRA.md or DOUBTS_EXTRA.md do not alone indicate missing required content.


## Supplemental update — 2026-11-20 16:28:26 UTC

This dated supplement supersedes the earlier pending-summary and audit-status observations without rewriting the historical review. It is based on text records and filenames only; no image was opened, and no reading or mathematical decision was made.

- `LEGIBILITY.md` and `FEEDBACK_EXTRA.md` are now populated with the exact proposed sections reviewed and approved by root. Their approval/application metadata is in `metadata/summary_approvals.tsv`, and the generated doubts/feedback files include the approved prose.
- All 25 required nonempty second-reading records now exist, and progress.log contains an audited event for each expected scan. These are the sole reader's records; this mechanical update adds no audit events.
- Root is writing the final hand/notation reconciliation. This supplement does not preempt or certify that reader judgment.
- Crop metadata now contains 235 distinct documented source boxes and 236 tight-crop rows, with the single explicit unrecovered exception `008_slanted.jpg`. There are three derivative aliases of the same scan-033 margin crop and six supplied-half transformations.
- The new `029_audit_montre.jpg` entry has original box (615,1615,1185,1695), rotation 0. The filename is a working label; root reports that the one view confirmed the already transcribed reading and caused no transcription change. The metadata update itself makes no ink judgment.
- The crop table in CHANGES_EXTRA.md has been refreshed. `records.build` was deliberately not run while comparison metadata repairs are in progress; root should rebuild after those repairs to incorporate this refreshed appendix in the generated changes log.

## Supplemental update — 2026-11-20 16:42:18 UTC: crop-coordinate documentation complete

The former sole coordinate exception, `008_slanted.jpg`, is resolved. SIFT/RANSAC registration led to a unique byte-identical replay of the saved crop from source box **(980,950,1240,1155)** at **−34 degrees**, without mirroring. All 200 nearby geometry-compatible integer candidates were tested; one matched the entire JPEG byte sequence, SHA-256 `20147642b901c8f08f8981f39469d965a2cdbebf06378bc1e77469a42f0f7b98`, with decoded-pixel RMSE **0.0**. Root reviewed and accepted this result.

The consolidated metadata now contains **236 distinct documented source boxes**, **236 tight-crop rows**, **zero unrecovered boxes**, three existing-crop derivative aliases, and six supplied-half transformations. The two earlier failed correlation reports are retained as historical, superseded evidence; their candidate coordinates remain rejected. The current unknown list is empty. See `crop008_recovery_history.md` and `crop008_exact_replay.md` for provenance and bounded-search limitations.

This work used numerical geometry only. It added no image reading, audit event, crop image, transcription change, or mathematical adjudication. The complete register and `CHANGES_EXTRA.md` were updated; final `records.py build` is intentionally left to root after metadata coordination.

# Final completion and reconciliation report

The consolidated diplomatic transcription covers every supplied leaf: **079–098 and 100–102**, 23 leaves of cote 149. Scan 099 was absent from the source set and has not been reconstructed. The authoritative page files are in `pages/`; the combined fragment is `SP87_C13_149_transcription.tex`.

## Completed reading record

Three first readers worked from each assigned leaf's scan, full-resolution overlapping halves, the two local witnesses, the supplied local difference/mark records and the current notation table. The main reader inspected the whole leaves and the disputed saved crops. All 23 first readings were committed before the blind stage. Each blind reader was different from that leaf's first reader and received the source images and anonymous boxes, without either witness or the first reading. The second TSV was saved before script comparison. Every token-different box was explicitly adjudicated on its image, with both original readings preserved.

| Final measure | Count |
|---|---:|
| Supplied leaves, page files and completed blind audits |23|
| Anonymous boxes independently reread |466|
| Token-different boxes explicitly adjudicated |328|
| Boxes changing a reading or its doubt state |122|
| Original C/H difference IDs covered exactly once |590|
| Original C marks in source order |85|
| Logged places differing from C or H |517|
| Places against C |144|
| Places against H |471|
| High / medium / low confidence rows |349 /113 /55|
| Inventoried elements, all transcribed |318|
| Remaining grouped doubt entries |166|
| Separately recorded mathematical check/use/background events |31|
| Saved crop images |906|

A place or box can contain several tokens; one place can differ from both witnesses. These counts are not token error rates. The 85 supplied marks finish as 37 first readings, 1 listed alternative, 8 other readings and 39 undecided. An undecided mark remains transcribed with its uncertainty; it is not omitted or silently regularized.

## Final metadata reconciliation

The unexecuted proposal and findings files remain in this archive as historical review records. Their status is superseded as follows:

- The 178 guarded corrections in `scripts/propose_documentation_cleanup.py` were reviewed by root and independently checked by a second agent, then applied to notes, hand observations, notation and inventory on 079–095. They changed no page or frozen reading.
- Static findings F01 and F03 were reconciled by `scripts/finalize_metadata.py`: D0027 and D0282 now point to the retained certainty/convention decisions, and the three 090 doubt-table Reading values are literal canonical TeX. All 590 coverage IDs remain.
- The README cote label now agrees with cote 149. The requested filename prefix remains unchanged.
- The 19 exact late metadata clarifications on 096/097/098/100 were applied by `scripts/apply_late_documentation_cleanup.py`. The old first-pass empty-check-list statement on 097 is explicitly historical; the existing main-reader event remains. One existing 096 event description now says initial prefix rather than initial E, without changing its claim, outcome, type or attribution.
- `review/feedback.md` and `review/legibility.md` contain the completed assessment. The earlier proposed versions are historical drafts. `review/notation_final.md` records the final cross-leaf dispositions; the earlier comparison register preserves the hypotheses that led to them.

All final tables were regenerated from the canonical `review/*_reviewed.json` records. Earlier reader reports and frozen first TSVs deliberately retain rejected readings, so they should not be mistaken for the authoritative transcription. Uncertain numeral-hand attribution has not been guessed from a page wrapper.

## Validation and freeze

The final structural gate, `python3 scripts/validate_work.py --final`, passed with 23 pages, 85 marks and no errors. This checks supplied-page/mark/difference coverage, required second readings and adjudications, inventory vocabulary, crop existence and bounds, brace structure and the combined-fragment identity. It is not TeX compilation or a proof of the manuscript's mathematical assertions.

The 23 page files and combined transcription were frozen as 24 SHA-256 records in `review/frozen_hashes.tsv` and `progress.log`. The final unchanged-hash check is recorded below and in the progress log. The separate final evidence-integrity report checks the preserved blind records and comparison/adjudication coverage.

No OCR, outside research or TeX compilation was used. Mathematical checks are typed and attributed in `CHECK_EVENTS.tsv`; source assertions reported in notes are not automatically checked theorems. Unbalanced source punctuation, source wording and explicit doubts remain literal.

## Archive contents and preservation

Four 45-minute checkpoints were saved during the work before the final archive. They are cumulative work snapshots, not page-only exports. The final ZIP includes all required deliverables, retained crops, first and second readings, adjudications, scripts and review documentation. Source attachments, original scans and witness texts, temporary halves, generated witness packets, bytecode and older ZIPs are excluded. The final archive manifest records each included file's byte count and SHA-256; packaging also verifies ZIP CRCs.

Final evidence-integrity gate: reader_b verified all 23 first-stage baseline hashes, all 23 first/second comparison hashes, exact reconstruction of all 23 comparisons, 328 complete explicit adjudications, 590 original difference IDs and 85 original marks, with zero errors. All 164 evidence files remained byte-identical during that gate. The separate final notation traceability review corrected several box citations and narrowed the h-like-k statement to the documented 102 occurrences; these were documentation-only changes.

Final unchanged-hash check passed 2026-11-21 15:40:07 UTC: all24 frozen transcription files match their recorded SHA-256.

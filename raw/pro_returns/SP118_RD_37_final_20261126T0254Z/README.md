# SP118_RD_37 — diplomatic transcription and audit

This edition concerns the nineteen supplied scans of Montpellier archive cote 37, in the supplied order: 008, 014, 017, 019, 020, 021, 022, 026, 028, 033, 036, 037, 038, 047, 048, 049, 050, 051, 057.

## Reading files

- `pages/` contains one consolidated LaTeX fragment for each completed page. `SP118_RD_37_transcription.tex` joins them in scan order. The supplied source `PREAMBLE.tex` is required to use these fragments; it is not duplicated here. No TeX compilation was performed.
- `SP118_RD_37_changes.md` records physical loci differing from either available witness and the explicit resolutions of witness C's doubt marks. Its counts are loci, not tokens or independent-model error rates. Added uncertainty alone is listed in the doubts file.
- `SP118_RD_37_collation.tsv` contains substantive departures from H's source transcription. H's editorial synopses, page labels and explanatory headings are not manuscript text; pages for which H supplies only a synopsis have no collation rows.
- `decisions.tsv` follows the actual source `MARKS.tsv` IDs and order. Those IDs begin with `R`, although the prompt's illustrative ID format begins with `M`.
- `SP118_RD_37_inventory.csv` records the text, formulas, diagrams, drawings, insertions, deletions and marginal material represented in each finished page.
- `SP118_RD_37_doubts.md` begins with the notation table, followed by remaining uncertainty, proposed abbreviation expansions, and a legibility assessment. Expansions are editorial aids and are not substituted into the transcription.
- `SP118_RD_37_notes.md`, `CHECK_EVENTS.tsv`, `SP118_RD_37_hand_log.md` and `SP118_RD_37_sheet_feedback.md` distinguish source statements, actual checks, local handwriting observations, and feedback for later readings.

## Independent reading and evidence

The first readers, blind second readers and main adjudicator were AI agents. References to visual inspection describe those agents' inspection of the supplied images; no human visual verification is claimed. The three first readers worked on separate pages, and the main adjudicator inspected the evidence for unresolved places and departures from either witness before committing each page. Only after all nineteen first passes were complete did a different reader receive each page's selected boxes, without either witness, the consolidated page, or its first box readings. The box lists and first readings were sealed before this stage. All nineteen independent readings and all differing boxes have now been adjudicated. Their inputs, scripted token comparisons and decisions are retained in `second/` and `records/`; dated progress entries distinguish completed stages from historical checkpoint states.

The three audit measures have different meanings. **568 boxes** received blind readings. **418 differing boxes** contained a difference between the first and second token sequences, including differences in macro choice, equivalent drawing geometry or uncertainty notation; this is neither a count of changed tokens nor a count of manuscript errors. **76 changed boxes** were revised by adjudication, including added uncertainty and drawing refinements. The witness apparatus separately counts **349 physical loci**, of which **163 differ from C** and **268 differ from H**; a locus can differ from both. Added uncertainty alone and purely syntactic differences do not add witness-change rows. All **137 source doubt marks** are accounted for in their original order.

The main archive contains `crops/CROPS.tsv`, with original-scan coordinates and rotation. The JPEG evidence is delivered once in the separate `SP118_RD_37_crops.zip`. A box is recorded in original pixels as `(x0, y0, x1, y1)`, with the right and lower edges excluded by the image crop operation. Source scans, source witness files, full-resolution halves and earlier checkpoint ZIPs are not duplicated in this archive.

## Diplomatic policies

Ink decides the reading. Original wording, abbreviations, unbalanced punctuation, inconsistent references and mathematical slips are preserved. Uncertainty remains in place as `\unsure{...}`; its first alternative is the preferred reading. Illegible material is retained with the supplied conventions. Typed overstrikes are represented as a deleted underlying character followed by the surviving character when their sequence can be read. Running text and numerals remain text; drawing strokes and genuine diagram labels may use TikZ. Archival foliation is preserved in the conventional archive-number comments and distinguished from authorial page numbers in the notes.

The work used AI-agent visual transcription, image crops and structural scripts. It used no OCR, text-recognition system, external research, or TeX compilation. Mathematical reading checks do not authorize silent correction of the source.

## Reproducibility and status

`progress.log` records page completion, independent audits, timed checkpoints and the transcription freeze. The SHA-256 values cover all nineteen page fragments and the combined transcription; the final check records whether they remain unchanged. `records/` preserves reader returns, main-reader adjudication records and supporting documentation. `scripts/` contains the crop, apparatus, comparison, validation, packaging and hash utilities. Only completed pages belong in `pages/`. Earlier proposed readings, one-time editing scripts and dated review snapshots are retained as process evidence; the consolidated pages and adjudicated records govern the final edition. The files historically named `apparatus_pending.md` and `root_math_pending.md` document completed consistency work and limited checks, not outstanding tasks.

The source package and prompt remain the authority for reproducing the input. These files document this reading of the supplied scans and do not certify the correctness of every mathematical claim appearing in them.

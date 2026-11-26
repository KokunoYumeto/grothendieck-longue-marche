# SP119_RD_37: transcription and collation

This package contains the consolidated reading of the 18 supplied scans of cote 37 of the Montpellier Alexander Grothendieck papers, in the supplied order: 58–64, 73, 78–84, 95, 99, 100.

## Reading the edition

- `pages/` contains one finished LaTeX fragment per scan. `SP119_RD_37_transcription.tex` combines them in order and has no preamble. Use the `PREAMBLE.tex` already supplied with the source archive.
- `SP119_RD_37_changes.md` records departures from either witness, certainty decisions, the remaining unresolved readings, and the adjudicated blind comparisons. Counts distinguish the C and H witnesses; a locus may differ from both and must not be counted twice by adding those columns.
- `SP119_RD_37_collation.tsv` contains the substantive H disagreements. Its `their_page` is the H page number, one less than our scan number. There is no H text for scans 73, 84 or 99.
- `decisions.tsv` follows the exact identifier order of the supplied `MARKS.tsv`. `SP119_RD_37_doubts.md` contains the notation table, explicit uncertainties, abbreviation expansions and legibility assessment.
- The inventory, notes, handwriting log, error-sheet feedback and `CHECK_EVENTS.tsv` document coverage, source observations and the limits of mathematical checking. A transcription observation is not represented as an independent proof.
- `second/` preserves the box lists, primary readings written before comparison, independent second readings, literal token comparisons and reader assignments. The first-reading and box-list hashes are recorded at assignment; the independent second reading and its crops are hashed before comparison. Formatting-token disagreements are adjudicated explicitly as such; they are not automatically treated as new readings. Audit totals count boxes, and overlapping boxes can cover the same physical mark.
- `SHA256SUMS.txt` and `progress.log` record the final frozen transcription and its verification. `VALIDATION.json` summarizes structural completeness checks.

The transcription preserves the source's spelling, accents, abbreviations, punctuation, mathematical notation, cancellations and insertions. Alternative readings remain inside `\unsure{...}`. No uncertainty is resolved by an expected mathematical formula or by the sequence of reference numbers. Printed letterhead is transcribed; the separate archival pencil foliation is recorded in the designated page comment.

## Image evidence

`crops/CROPS.tsv` records every crop's name, source page, original pixel box, rotation and reading phase. The separate `SP119_RD_37_crops.zip` supplies the grayscale JPEG images of changed or explicitly uncertain loci, resolved source marks and blind disagreements. Routine confirming crops not included in the image dump can be cut again from the supplied scans and this manifest. The source scans and full-resolution halves are not copied into either deliverable ZIP.

## Method and reproducibility

Three assigned readers worked on separate pages, each with only that page's source witnesses, image, overlapping halves and the current notation table. The primary reader checked every differing or open place against its crop. After all first readings, each page's marked boxes were read by a different reader without access to its witnesses, primary readings or notes. Token comparisons were made only after the blind readings were written; their differences were then decided from the crops.

No OCR, external research or TeX compilation was used. The scripts assemble and validate records; they do not recognize handwriting or infer the source text. `records/` holds the primary adjudicated data, and `reading_returns/` preserves the original reader reports. The derived logs are rebuilt from the primary records.

To regenerate derived logs, use `python3 scripts/build_records.py` with this directory placed under the working root and the supplied source archive extracted once under `sources/`. The crop helper uses that same source layout. No attached source file is bundled in this package.

## Completion totals

All 18 pages have completed primary and blind audits. All 68 supplied marks have an adjudication entry: 25 are resolved and 43 remain undecided. The remaining-doubts table contains 60 recorded loci across the edition, including doubts beyond the supplied marks. The independent pass covers 227 boxes: 106 have literal first/second token differences, including formatting differences, and 20 boxes changed after crop adjudication. These are box counts, not counts of distinct textual errors.

The final changes tables contain 128 substantive loci: 28 differ from witness C and 115 from witness H; 15 loci differ from both. Confidence across those loci is 87 high, 26 medium and 15 low. A further 21 certainty-only entries are excluded from those substantive counts. The inventory contains 154 elements. The crop manifest records 446 inspected crop boxes; the separate image archive includes 240 selected evidence images, as described above.

The retained doubts are substantive limits of the reading. This is an AI collation with independent assigned readings and primary crop adjudication, not a claim of human palaeographic verification. Mathematical content is described and used cautiously for reading; no external literature search, independent theorem proof or TeX rendering was performed.

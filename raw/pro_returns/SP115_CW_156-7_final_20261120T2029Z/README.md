# SP115_CW_156-7 — consolidated diplomatic transcription

This package covers all eight supplied scans 002–009, corresponding to manuscript pages 1–8 of Alexander Grothendieck’s Montpellier archive cote156-7. The source heading on 002 is **Analysis Situs (troisième mouture)** and its written date is **23 juin**. The year 1986 and catalogue date range 23–26 June are supplied archival metadata, not additions to the handwritten date.

## Edition

- `pages/` contains one consolidated LaTeX fragment per scan, with the original C filenames.
- `SP115_CW_156-7_transcription.tex` concatenates those eight fragments in scan order, without a preamble.
- `SP115_CW_156-7_changes.md` records the adjudicated C/H differences, evidence, confidence, unresolved readings and changes arising from the blind rereading.
- `SP115_CW_156-7_collation.tsv` lists differences from H with the required scan/page mapping. H’s manuscript page n corresponds to our scan n+1.
- `SP115_CW_156-7_inventory.csv` lists every text block, formula group, drawing, margin, insertion and deletion inventoried in the edition.
- `SP115_CW_156-7_doubts.md` contains the shared notation table, remaining uncertainties and attested abbreviations with proposed expansions.
- `SP115_CW_156-7_notes.md` follows the mathematics page by page, distinguishing the source’s assertions and slips from checks actually performed.
- `CHECK_EVENTS.tsv` records those mathematical checks and their explicit premises.
- `SP115_CW_156-7_hand_log.md` and `SP115_CW_156-7_sheet_feedback.md` record handwriting habits and error categories.

## Reading and audit evidence

The image is the authority throughout. C and H are the two supplied AI draft witnesses; the supplied sweep correction SA21-K7-01 was separately checked on the ink. Uncertainty is marked in place and listed in the apparatus. Clear authorial slips, source abbreviations, incomplete sentences, correction layers and graphic details are retained.

The first reading was divided among three readers, one page at a time, followed by direct root inspection of every returned disagreement or open place. Each page’s difficult passages were subsequently assigned to a different reader. Those readers received only the page images and neutral box coordinates. The initial box and reading TSVs were frozen before that stage, and the second readings were written before scripted token comparison.

`second/` preserves the neutral box lists, immutable first readings, independent second readings, comparisons, root decisions, coordinate manifests and initial page snapshots. `crops/` contains the inspected crops, including the independently generated blind crops. `review/` and `scripts/` preserve working records and reproducible processing; files labelled proposed, pending or draft are historical reading records. The consolidated fragments in `pages/` are the edition.

The blind audit covered 290 boxes. Script comparison identified 240 differing box readings, all directly adjudicated on crops by root. Those decisions changed 73 distinct physical places, counting uncertainty changes and deduplicating overlapping boxes. The frozen first-excerpt tables contain two empty cells: scan002 B008 (an incidental marginal mark, judged not text) and scan006 B047 (a formula already present in the frozen initial page). These limitations are explicitly recorded in `review/first_excerpt_coverage_review.md`; neither was silently treated as a missing passage in the page. A registered extension of scan004 B029 was needed because its first blind crop clipped the word ending; its coordinates and reason are preserved.

No OCR, text-recognition library, PDF text layer, external research or TeX compilation was used. Validation checks syntax structure, file/schema coverage, exact concatenation, audit completeness and recorded hashes; it does not claim that a compiled layout was inspected. Archive manifests record the packaged bytes and their SHA-256 values. Final frozen transcription hashes and their end-of-run recheck are recorded in `progress.log`.

The supplied scans, witness files, context material and previous checkpoint ZIPs are excluded from this archive, as requested.

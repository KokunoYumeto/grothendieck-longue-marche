# SP70_C13_142 — consolidated diplomatic transcription

The final transcription comprises the 24 per-scan fragments in `pages/` and
their ordered concatenation, `SP70_C13_142_transcription.tex`. The scan order is:
026, 027, 028, 029, 030, 031, 033, 034, 035, 036, 037, 038, 039, 040, 041, 042,
044, 045, 046, 047, 048, 049, 050, 051. Gaps in the supplied sequence have not
been reconstructed.

The combined file is a fragment without a preamble. It uses the conventions
and macros of the supplied `PREAMBLE.tex`, together with standard LaTeX,
TikZ and tikz-cd. The supplied preamble and witnesses are not repeated here.
No compilation was performed.

## Reading record

- `SP70_C13_142_changes.md`: per-page comparisons, confidence, consequential
  corrections, inspected crop coordinates and remaining uncertainties.
- `SP70_C13_142_collation.tsv`: differences from the supplied H text, with H's
  page numbers one below the scan numbers and its own doubt flags.
- `decisions.tsv`: all 162 supplied doubt marks, in their original order.
- `SP70_C13_142_doubts.md`: final notation table, all remaining in-text doubt
  marks, certainty decisions, abbreviation expansions and legibility assessment.
- `SP70_C13_142_inventory.csv`: 573 transcribed page elements.
- `SP70_C13_142_notes.md` and `CHECK_EVENTS.tsv`: manuscript content and the
  limited mathematical checks actually performed.
- `SP70_C13_142_hand_log.md` and `SP70_C13_142_sheet_feedback.md`: observed
  handwriting habits and feedback on the recurring-error categories.
- `AUDIT.md`, `AUDIT_CHANGES.tsv` and `progress.log`: the ordered second reading,
  subsequent notation reconciliation, timestamps and frozen SHA-256 values.

The same primary reader inspected every page in order and then performed the
ordered second reading. Mechanical assistance was restricted to packaging,
syntax, metadata and numerical crop provenance. The readings were not divided
among manuscript readers. No OCR or external research was used.

## Supporting files

The remaining TSV and Markdown files are the underlying registers and
supplementary documentation from which the main reports were assembled.
`CROPS.tsv` records 144 crop rectangles. `CROP_PIXEL_RECOVERY.tsv` and
`CROP_COORDINATE_RECOVERY.md` distinguish exact numerical image provenance from
the eight documented, non-certified filename associations on scan 026.
The crop images, full scans and page halves are deliberately absent.

The scripts document the actual work and include mechanical validators.
The `pageNNN.py` and manual audit/final-notation scripts record successive
decisions, not an idempotent build system: do not rerun them against the final
registers, because they append historical rows. `record.py` regenerates the
combined fragment and reports from the current page files and registers.
The final frozen hashes, rather than an attempted replay of the draft scripts,
identify the delivered transcription.

`CHECKPOINTS.tsv` lists the two earlier immutable checkpoint archives. The final
ZIP contains the current versions of all their deliverable and documentation
paths, together with the completed later work; it contains no earlier ZIP.

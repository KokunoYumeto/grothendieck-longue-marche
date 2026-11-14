# Validation before freeze

All 46 second visual audits and the final notation review preceded context access. The inventory has 955 rows, all marked `yes`; balanced-brace extraction indexes 472 `\unsure` occurrences and one `\illegible` occurrence, including the 88 faint paper legends.

The complete combined fragment passed a pdfTeX/LaTeX **draft-mode syntax check** (exit status 0) with `amsmath`, `amssymb`, `graphicx`, `xcolor`, and `tikz-cd`, plus TikZ libraries `calc` and `arrows.meta`. The exact checking preamble is retained at `scripts/validation_preamble.tex`; it supplies simple diagnostic definitions of the required state macros, not a proposed edition layout. The environment lacked prebuilt LaTeX formats, so a local pdfLaTeX format was generated; a full PDF attempt reached the end of all source pages but font embedding failed for the unavailable TS1 font `tcrm0700`. No finished PDF or claim of publication-layout verification is supplied.

The syntax fixes affected only TikZ cell separators inside macro arguments, display math around an array, accented upright labels, and TeX grouping of a subscript. They did not add, remove, or reinterpret manuscript content. The actual manuscript drawings and diagrams had already been checked visually during the audits; no OCR was used.

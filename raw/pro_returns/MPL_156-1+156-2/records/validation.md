# Validation before freeze

All 46 second visual audits and the final notation review preceded context access. The inventory has 955 rows, all marked `yes`; balanced-brace extraction indexes 472 `\unsure` occurrences and one `\illegible` occurrence, including the 88 faint paper legends.

The complete combined fragment passed a pdfTeX/LaTeX **draft-mode syntax check** (exit status 0) with `amsmath`, `amssymb`, `graphicx`, `xcolor`, and `tikz-cd`, plus TikZ libraries `calc` and `arrows.meta`. The exact checking preamble is retained at `scripts/validation_preamble.tex`; it supplies simple diagnostic definitions of the required state macros, not a proposed edition layout. The environment lacked prebuilt LaTeX formats, so a local pdfLaTeX format was generated; a full PDF attempt reached the end of all source pages but font embedding failed for the unavailable TS1 font `tcrm0700`. No finished PDF or claim of publication-layout verification is supplied.

The syntax fixes affected only TikZ cell separators inside macro arguments, display math around an array, accented upright labels, and TeX grouping of a subscript. They did not add, remove, or reinterpret manuscript content. The actual manuscript drawings and diagrams had already been checked visually during the audits; no OCR was used.

## Final package validation

Final structural verification is recorded in final_validation.json: all 47 frozen hashes unchanged, all 46 page files in prescribed order, 955 inventory rows all yes, all 473 uncertainty macros represented in the index, and all 125 research entries with source/kind/quotation/context metadata. Actual searches cover those 125 entries plus 26 standing audit rows and nine open-register comparisons. The complete notes contain approximately 21,400 words, including context metadata, tables and bibliography. No supplied images, PDFs or archives are included.

Independent post-freeze research reviews checked the explicit counterexamples, context identifiers and statuses, quoted uncertainty, and primary-source theorem scope. The final archive is checked for integrity and for inclusion of the frozen bytes; no new image reading or source alteration occurred during this phase.

# MPL_81_038-055+154_046-076

The completed retained selection is cote154, PDF scans046–076:31 pages with handwritten numbering45–75. All cote81 scans named in the package title were expressly omitted from the supplied image archive as already transcribed elsewhere.

## Main files

- `MPL_81_038-055+154_046-076_transcription.tex`: the combined diplomatic fragment, with no preamble; exact concatenation of the31 files in `pages/`.
- `MPL_81_038-055+154_046-076_doubts.md`: notation concordance, all507 marked uncertainty occurrences with confidence, abbreviation glossary, and legibility assessment.
- `MPL_81_038-055+154_046-076_inventory.csv`:693 elements, all marked transcribed.
- `MPL_81_038-055+154_046-076_notes.md`:110 individually anchored research items, authorial-reservation register, documentary inventory, current-results comparisons, post-freeze reading questions, and APA references.
- `progress.log`: sequential page-completion and audit records, freeze hashes, context opening, and final verification.

`records/` contains the frozen hashes, final checks, method record, uncertainty data, and item-level context-search records. `support/` preserves the scripts, comparison reports, and textual validation history; historical partial or failed checks there are superseded by the final validation record.

## Optional compilation

The source fragments require definitions of the editorial macros and the usual TikZ/tikz-cd packages. A separate portable review wrapper is supplied as `records/compile_validation.tex`; from the extracted archive root, with a normal XeLaTeX installation and the required packages, run:

```bash
xelatex -output-directory=records records/compile_validation.tex
```

This review wrapper distinguishes uncertainty, deletion, insertion, and marginal material by color. It is a validation aid, not a replacement for the source’s editorial markup or a claim that the handwritten pages had this typeset layout.

The transcription was frozen before context was opened. The final verification confirms that all31 page hashes and the combined-fragment hash remain unchanged. The notes preserve the distinction between the manuscript’s own claims, the supplied research runs’ statuses, and the present reader’s conditional ideas.

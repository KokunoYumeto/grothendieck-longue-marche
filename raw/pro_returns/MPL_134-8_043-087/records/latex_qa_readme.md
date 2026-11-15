# LaTeX syntax QA — final technical state

## Governing final result

`records/latex_qa_combined_final.json` governs the final syntax result. The actual combined fragment compiled successfully at SHA-256 `3f85b51570feeb779ae2fd3d9e338ea8f90078fbce6e6e406722a402d6bc8c79`, with return code 0, no structural errors, and no missing-character diagnostic. `records/final_source_hashes.json` records all 44 page hashes and the combined hash; all 45 remained unchanged after the final compilation, and the combined bytes equal the ordered concatenation of the pages.

The principal reader froze the transcription at 2026-11-15 11:49:57 UTC. The technical helper made no transcription-source edits, inspected no scan images, and read no context for this technical work. Later, separately authorized research-note work is outside this QA scope.

## Paragraph-ending correction and remaining warnings

The final correction changes only `scripts/latex_qa_preamble.tex`. Its `diagram` wrapper now schedules a paragraph ending when the supplied brace group closes, while allowing TeX to read the body directly so that TikZ can establish its matrix-separator catcodes. The previous wrapper left the following printed job table in the same paragraph as its preceding banner inside the minipage. That joined layout caused the substantial overfull boxes at combined line 2304 (scan 072, 38.90453 pt) and line 2580 (scan 074, 297.74498 pt).

The corrected installed harness removes both large overflows at the unchanged combined hash. No resizebox source patch was needed or applied. The single remaining layout warning is a 0.19052 pt overfull box at combined lines 620–629 (scan 050), which the principal reader judged immaterial. `latex_qa_combined_before_block_end.json` and `latex_qa_block_end_trial.json` retain the historical comparison; the final report supersedes them.

The raw log also reports that the installation lacks the default `pdftex.map`. The harness explicitly loads the installed `lm.map`, `symbols.map`, and `latxfont.map`; the final run succeeds without missing-character diagnostics. This environment warning is recorded separately in the final JSON because the original warning collector matched capitalized LaTeX warnings. Generated format files, wrappers, logs, snapshots, and PDFs remain in the sibling `texqa-cache` directory, outside this package. No system-wide TeX configuration was changed.

## Reviewed source proposals — applied by the principal reader

The technical helper prepared patches and compiled scratch copies. The principal reader reviewed and applied the source proposals. Historical proposal reports describe those earlier stages and do not imply the patches remain outstanding.

- `applied_syntax_fixes.patch` preserves the reviewed nine-page delimiter, matrix-separator, arrow-label, and text/math-wrapper repairs. The current `suggested_syntax_fixes.patch` is empty because those repairs are present.
- `proposed_diagram_arrays.patch` preserves the five reviewed table-to-array conversions on scans 043, 047, 050, and 056. Their exact inverses preserve original text and spacing tokens, column specifications, and row breaks. The four scratch-copy compile results are in `latex_qa_banner_proposal.json`.
- `proposed_remaining_diagrams.patch` preserves the reviewed TikZ conversions for scans 051, 052, and 062, including the long chain's brace extents. The source-body and token checks are in its JSON manifest; scratch-copy results are in `latex_qa_remaining_diagram_proposal.json`.
- `proposed_scan075_label_borders.patch` preserves the reviewed upper ellipse and lower rounded rectangle around existing arrow labels. Only label-node border options were added; the exact inverse retains every original word and arrow option. The scratch-copy result is in `latex_qa_scan075_label_borders.json`.

The compiler's missing-target reports on scans 072 and 074 were referred to the principal reader, who checked the ink and changed the direction keys to `drr` and `u`, respectively. All reading and later visual/notation corrections belong to the principal reader. The technical helper did not inspect images or select readings.

## Structural validation and assembly — executed

`scripts/check_package_structure.py` checks the expected 44 pages (043–087, excluding 060), scan/cote headers, permitted control words, required diagram environments, inventory schema and kind labels, unique element IDs, per-scan records, and completion/audit coverage. The inventory conversion was reviewed and applied by the principal reader, with the original retained. Its proposal, exact inverse provenance, mapping, and review record remain under `records/`.

The principal reader reviewed and executed `scripts/assemble_and_validate.py` after all 44 visual audits and reviewed corrections. `assembly_validation.json` and `assembly_verification.json` record the completed assembly/verification. The script concatenates exact page bytes in scan order, beginning with the existing `\cotefile{134-8}` in scan 043, and adds no content or newline normalization. It never writes to `progress.log` or freezes files. Its write mode refuses operation after a freeze/context-open marker. `assembly_validation_usage.md` documents the commands and their current status.

## Doubt extraction — executed and independently checked

After explicit authorization, `scripts/extract_doubts.py` read all 44 live page files and was refreshed after the final scan 073 notation change. `doubts_extracted.json` contains 457 complete raw `\unsure` occurrences, with no malformed calls or extraction errors. `doubts_extraction_integrity.json` reports an independent pass: all 44 source hashes, all 457 character and UTF-8-byte slices, and the location fields match. No nested doubt-target occurrence appears in the current corpus; nested arguments are retained, and synthetic cases exercise nested targets.

The extractor assigns no reading, alternative split, confidence, or word-count interpretation. It changes no page source, notation table, or doubt-register Markdown. The principal reader used the refreshed raw output for the final register. The 19 checks in `doubts_extractor_synthetic_validation.json` remain historical preparation evidence, while the live integrity report governs the extracted current corpus. See `doubts_extractor_usage.md` for exact span conventions and limitations.

## Read-only compilation command

From the package's parent directory:

```sh
python MPL_134-8_043-087/scripts/check_latex.py --fragment MPL_134-8_043-087/MPL_134-8_043-087_transcription.tex --report MPL_134-8_043-087/records/latex_qa_combined_report.json
```

The wrapper supplies the task macros and ordinary mathematical/TikZ packages. It colour-codes deletions, insertions, and uncertain readings for syntax inspection. The auxiliary PDF is a QA rendering; the deliverable remains the frozen source fragment. Earlier per-page, continuous, and proposed-copy reports are historical evidence and are superseded by `latex_qa_combined_final.json` for the final combined source. All watchers have stopped. No input scans, context files, compiler PDFs, or compiler caches are included in this package.

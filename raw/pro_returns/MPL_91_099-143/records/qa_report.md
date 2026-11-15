# Final checks before the context archive was opened

All 38 whole scans and their supplied halves were read visually in the sequential first pass, then compared again during the second audit recorded in `progress.log` and `audit.md`. Enlarged or rotated views were used for cancellations, small indices, inserted words, and ambiguous alphabet choices. No OCR was used.

The cross-page notation comparison is recorded in `notation.md` and at the top of the doubt register. It covered the partition capital, schématique wording, antifique/antifinie wording, limit signs, prime counts, category circles, bars, typed Lie-algebra alphabets, continuation strokes, determinant signs, and quotation marks. The extra comparison of scans 099 and 115 retained the same P-alphabet alternatives. The inventory was reconciled with the audited readings; the separator under scan 099's opening formula was added.

A temporary XeLaTeX harness compiled the complete fragment to 38 pages. The runtime's TeX format was initially absent; it was generated locally from the installed LaTeX sources, and both installed TeX/font trees were made available to the process. No sources were fetched to repair the mathematics or handwriting.

Syntax corrections made before freezing: explicit TikZ matrix separators in all 19 `tikzcd` environments; math delimiters around one deleted formula in scan 108; a valid matrix-node name for the border in scan 128; text mode for the cancelled word “idéal” in that page; separate placement of the inclusion symbols and labels in scan 136; anchors for the three grouping brackets in scan 142; left-aligned filtration labels in scan 138 to prevent a bracket crossing the final expression. These changes alter TeX mechanics/placement, not readings.

Rendered diagrams were inspected on scans 101, 105–107, 114, 118, 120, 123, 128, 136 and 138, and the compound bracket drawing on 142 was enlarged and compared with the scan. The final complete compile has no errors or missing-character warnings. One 20.65-point overfull line on typed scan 119 is caused by the intentionally simple unbreakable-underlining macro in the temporary harness; its text remains within the wide QA page. The harness displays deletions/insertions in colour and only the first doubt reading for checking; it is not a substitute for the full diplomatic fragment, which retains every state macro and alternative.

`verify_package.py` checks all 38 page names, combined order and exact concatenation, the single cote marker, inventory schema and all-yes status, sequential completion and audit records, balanced groups/environments, and (after freezing) every stored transcription hash. The main fragment has no preamble. The temporary QA PDF is not part of the requested deliverable.

There are 448 explicit doubt occurrences, including nine `illegible` occurrences totalling an estimated 25 words. Fourteen of those estimated words are in the layered cancelled proof on scan 122. Approximate manuscript locations in the doubt register are visual line bands/positions; the separate source-line number is exact.

The sheet-kind classification records visible reuse: several handwritten sheets show the typescript on their reverse through the paper. Scan 109 is marked `cancelled_draft` for its large cancelled opening draft; the subsequent live proposition and corollaries on the same scan remain live in the transcription. Scan 116's main text is cancelled throughout. Folio numbers and printed pagination are separately retained.

## Research-note verification after the freeze

The final notes contain 56 individually identified items and the two standing-question sections, planning response and five-row open-item disposition. There are 59 saved context-search records: one per note plus three summary-section searches. All seven own-idea notes carry a confidence and reason. The five exact symbolic checks in exact_calculations.py passed. Inline mathematics delimiters and control characters were checked in the Markdown. The transcription files were not modified during this research stage.

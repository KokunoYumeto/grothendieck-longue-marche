# Final review record

## Reading protocol and boundary

One primary reader transcribed the pages sequentially and performed the second
visual reading of every supplied scan, using the whole-page and overlapping
half-page images. No OCR was used. Auxiliary agents performed infrastructure
checks, external bibliography retrieval, and two self-contained mathematical
checks; they did not read, transcribe, or audit manuscript images or determine
manuscript readings.

The individual audit lines, SHA-256 values, freeze at 2026-11-15 01:39:54 UTC,
and context opening at 01:39:55 UTC are in `progress.log`. The inadvertent
earlier listing of the contextual ZIP's member names and sizes is recorded
there and in the notes; the file contents were not opened before freezing.

## Structural checks

The structural validator checks 49 page files, 626 inventory rows, and all 50
frozen SHA-256 values. The combined fragment is the exact ordered byte
concatenation of the individual fragments. The source contains neither a
document preamble nor an embedded source image. All inventory rows have
`transcribed=yes`, and their sheet classifications are consistent within each
scan.

Four advisory warnings arise because the validator looks lexically for
display-math delimiters. These were inspected in the frozen text and do not
identify an absent expression:

| Scan | Inventoried expression | Why the lexical display check warns |
|---|---|---|
| 093 | Expression beginning with the arc/complement notation | It is present as inline mathematics within the marginal passage. |
| 094 | Antipodal transport comparison, involving tau and the crossing exponent | It is present in inline math. |
| 105 | Doubt-marked marginal inequality beginning with the lower-bound sign | It is present in the marginal inline math. |
| 115 | `N′=N−1` | It is a mathematical label inside a TikZ node. |

Inventory kinds describe the manuscript element, not the choice of LaTeX math
delimiter. The warnings are retained rather than hidden by altering the
frozen transcription or the validator.

## Compilation and visual diagnostic checks

The full 49-scan diagnostic compilation completed successfully at the run
beginning 2026-11-15 01:37:20 UTC and produced 85 diagnostic PDF pages. Its
result, scan-to-PDF-page map, and warnings are in
`qa-build/full_compile_after119_summary.json`. Representative diagnostic PDF
pages 1, 37, 45, 60, and 84 were visually inspected for text, diagrams, reused
printing, and drawing layout. This diagnostic sampling is distinct from the
complete second reading of all 49 manuscript scans.

Before freezing, the text-circle nodes on scan 105 were moved to their proper
outer text mode, retaining their inner mathematical prime and equality
labels. The subsequent scan-105 compilation, beginning 01:39:02 UTC, passed
with the invalid-math-mode warnings removed. Its result is recorded in
`qa-build/scan105_fontcheck_summary.json`. General unicode-math notices and one
legacy OMS font fallback remain properties of the diagnostic harness; no
missing-character or overfull/underfull-box errors were reported in those
checks. No post-context change was made to any frozen fragment.

The compilation logs and failed preliminary attempt are kept as work records.
Generated PDFs, image previews, formats, and auxiliary caches are excluded
from the final archive and can be regenerated with the harness.

## Research-note checks

The notes contain 75 distinct item IDs: C01–C03, R01–R60 with the separate
R38a/R38b and R50a/R50b/R50c locations, O01–O06, and T01–T03. Each item has
an anchor, a kind, and a recorded contextual query; own ideas state their
confidence and reasoning. The 75 IDs agree with `context_queries.json` and
`context_search_summary.json`. The search script scanned every supplied
contextual file for each query, and its output records exact filenames,
line numbers, and nearby source markers.

The final editorial pass removed accidental leading patch characters from the
notes and supplied Markdown math delimiters for the mathematical commentary.
These corrections affected the notes alone. The classification distinguishes
the direct Esquisse section 8 construction from the broader tame-topology
motivation and from the unestablished connection with the 1986 geometry of
forms. No supplied research-register status was upgraded.

External primary sources were consulted only after freezing. The Esquisse and
Brown-letter passages and the Montpellier catalogue were directly retrieved;
publisher metadata and abstracts were checked for Folkman–Lawrence and
Goodman–Pollack. The two combinatorics papers' full proofs were not independently
audited. Source URLs, bibliographic details, and these limits are in the notes.

The two auxiliary mathematical checks are documented separately in
`auxiliary_math_checks.md`. They verify deductions conditionally on stated
mathematical hypotheses, not readings or the applicability of an omitted
manuscript convention.

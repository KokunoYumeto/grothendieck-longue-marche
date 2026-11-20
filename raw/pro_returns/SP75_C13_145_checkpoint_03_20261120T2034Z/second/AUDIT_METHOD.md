# Independent reading and adjudication

The first-page reports identify the first reader. Each audit assignment records a different reader, its UTC assignment time, and the supplied evidence: the target scan image and a box list containing only structural descriptions. The exact source coordinates are retained in each `*_boxes.tsv`. The image itself is not included in this edition, because it is among the supplied attachments.

`FIRST_READINGS_SHA256.tsv` seals all24 first box-reading files before an independent second reading is submitted. An independent reader writes `*_second.tsv` and a crop manifest before the main reader runs the comparison. The first and second reading files are then kept unchanged. Each comparison receipt records their SHA-256 hashes and the box-list hash before token comparison.

The comparison tokenizes LaTeX commands, words, numbers, and every non-space character. It does not discard macro or layout differences. `*_token_differences.json` records each differing token span. The corresponding `*_comparison.tsv` groups the spans by source box, preserving the first reading, independent reading, final adjudication and ink evidence. A grouped row can contain several lexical, symbolic, punctuation or markup differences. Every differing box is checked on its saved second-reading crop by the main reader, including boxes whose ultimate difference is only typesetting.

In the required `scan NNN audited ...` log entries, B is the number of independently read boxes, D is the number of boxes with one or more token differences, and K is the number of those boxes whose adjudication changes the first consolidated reading. The per-box token-span counts remain available separately. These are not counts of incorrect words and are not an error-rate estimate.

The main changes table counts substantive loci against witnesses C and H. Its independent-reading subsection additionally records all differing boxes, including retained first readings and typography-only comparisons. A changed source reading is reconciled with the page and its applicable decisions, doubts, inventory or witness-difference rows; immutable first readings are never rewritten to match the later result.

## Documented reader exclusion

During first-page packet preparation, a quoting problem in the supplied literal TSV caused reader_b to see difference-list text for scans025–027 while working on024. The incident and correction are documented in `../packet_boundary_incident.json`. Reader_b is excluded from independent readings of all three affected pages, regardless of first-reader assignment. The preparation, audit-completion and final-verification scripts enforce that exclusion. The target packets for025–027 were regenerated with the literal TSV parser before their first reading.

No OCR, external research, or TeX compilation is part of either reading. The enlarged crops are visual evidence, not recognition output.

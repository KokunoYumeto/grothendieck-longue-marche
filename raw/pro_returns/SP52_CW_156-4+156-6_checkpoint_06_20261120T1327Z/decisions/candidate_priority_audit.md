# Candidate-priority count audit — completed scans 065–071

Text-only audit of the completed decision JSONs. **No candidate found:** none of the 242 difference rows with `change_c: false` has the same `\unsure` candidate multiset in its C quotation and final `reading` with a changed order.

| Scan | Rows with `change_c: false` inspected |
|---|---:|
| 065 | 33 |
| 066 | 39 |
| 067 | 55 |
| 068 | 31 |
| 069 | 26 |
| 070 | 22 |
| 071 | 36 |

Method: started with `rg`; read each difference's exact `c` and `reading` fields; parsed balanced `\unsure{...}` groups and split alternatives only on unescaped pipes at that group's top brace level. Compared exact candidate multisets and ordered lists. Escaped braces and pipes were not treated as delimiters; nested formula groups were preserved. No equivalence of different macro spellings was treated as a new candidate. Also inspected the false-flag rows whose source and final strings differ; their uncertainty differences are not same-candidate priority reversals.

As a check that the parser detects actual order changes, it found eight reordered same-candidate groups elsewhere, all already marked `change_c: true`: scan067 D029, D050, D053 and D059; scan068 R1-D006; scan069 R1-D09 and R1-D27; scan071 071-D45. For example, scan067 D050 has C `\unsure{bien|vu|la|là}` and final `\unsure{vu|bien|la|là}`, correctly flagged as a C change.

No records, flags, counts, source quotations, final readings, page files or historical briefs changed. No images, compilation or broader validation was performed. This report concerns the recorded final `reading` fields; it is not a new manuscript judgment.

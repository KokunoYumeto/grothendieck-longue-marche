# Mechanical doubts locator coverage review

Snapshot: 2026-11-17 23:05:24 UTC

The page files contain 335 uncertainty macros: 332 unsure and 3 illegible. The current authored Reading doubts table has 175 rows. 32 macro occurrences have an exact same-page reading-cell candidate after whitespace/backslash normalization and removal of outer math/code delimiters. This is a candidate text match, not confirmation that the occurrence is covered.

The authored rows use approximate manuscript positions, frequently grouping several symbols or occurrences. Those positions cannot be safely equated with TeX source line numbers. Consequently the current table cannot be mechanically certified as an exhaustive occurrence locator, nor can a nonmatching row be declared an omitted doubt merely from this comparison. No confidence was inferred or changed.

| Scan | unsure | illegible | Authored rows | Exact reading-cell candidates |
|---|---:|---:|---:|---:|
| 90 | 12 | 1 | 9 | 2 |
| 91 | 1 | 0 | 1 | 0 |
| 93 | 10 | 0 | 5 | 0 |
| 94 | 8 | 0 | 6 | 0 |
| 95 | 8 | 0 | 4 | 1 |
| 96 | 8 | 0 | 4 | 1 |
| 97 | 4 | 0 | 1 | 0 |
| 98 | 21 | 0 | 9 | 0 |
| 99 | 9 | 0 | 5 | 1 |
| 100 | 15 | 1 | 6 | 0 |
| 101 | 8 | 0 | 4 | 0 |
| 102 | 6 | 0 | 4 | 1 |
| 103 | 4 | 0 | 2 | 1 |
| 104 | 22 | 0 | 5 | 0 |
| 105 | 2 | 0 | 2 | 0 |
| 106 | 7 | 0 | 6 | 4 |
| 107 | 8 | 1 | 5 | 2 |
| 108 | 9 | 0 | 6 | 0 |
| 109 | 4 | 0 | 4 | 1 |
| 110 | 3 | 0 | 3 | 3 |
| 111 | 7 | 0 | 5 | 0 |
| 112 | 7 | 0 | 4 | 0 |
| 113 | 0 | 0 | 0 | 0 |
| 114 | 7 | 0 | 4 | 2 |
| 115 | 4 | 0 | 3 | 0 |
| 116 | 1 | 0 | 1 | 0 |
| 117 | 22 | 0 | 5 | 0 |
| 118 | 2 | 0 | 2 | 0 |
| 119 | 6 | 0 | 4 | 0 |
| 120 | 6 | 0 | 4 | 1 |
| 121 | 0 | 0 | 0 | 0 |
| 122 | 8 | 0 | 5 | 1 |
| 123 | 12 | 0 | 5 | 2 |
| 124 | 13 | 0 | 5 | 0 |
| 125 | 18 | 0 | 7 | 2 |
| 126 | 7 | 0 | 5 | 1 |
| 127 | 19 | 0 | 6 | 0 |
| 128 | 3 | 0 | 3 | 1 |
| 129 | 2 | 0 | 2 | 1 |
| 130 | 6 | 0 | 4 | 1 |
| 131 | 1 | 0 | 3 | 1 |
| 132 | 12 | 0 | 7 | 2 |
| 133 | 0 | 0 | 0 | 0 |

## Current exhaustive supplement

The primary reader has run the supplementary-table script. The current read-only verification is:

```json
{
  "recorded_entries": 335,
  "missing_keys": [],
  "extra_keys": [],
  "body_or_line_mismatches": [],
  "current_occurrence_coverage_exact": true
}
```

## Supplementary-table method

After the transcription is frozen, append a separate exhaustive macro locator table while preserving the existing notation table, authored readings, alternatives, confidence judgments, and abbreviations. Use one row per source macro occurrence, including nested or deleted uncertainties and unbraced single-token arguments. Columns should identify cote, scan, TeX line, macro kind, ordinal, and exact macro body; manuscript line positions must not be invented. Keep alternatives in the same order as the source body and retain illegible word counts as counts rather than proposed readings.

The supplement should state that it is a mechanical locator index, not an additional reading or independent check. Do not assign new confidence ratings from the presence of unsure; link to authored confidence rows only when a unique exact relationship is established. Preserve exact raw strings in a TSV or JSON record alongside any Markdown escaping needed for pipes, backticks, and line breaks. Hash the frozen source files used, count every occurrence, and assert that the supplement has exactly the same occurrence keys.

This read-only review does not append the supplementary table or change the doubts file; any existing supplement is checked separately above.

# DSS comparison coverage review

Reviewed 2026-11-17 18:45:06 UTC.

## Result

PASS: no mechanical coverage or field-format errors found.

- **255 comparison records** match **255 catalogue IDs** exactly; no missing, extra or duplicate IDs.
- Record order matches the source catalogue order.
- Every record has exactly **five fields** separated by the literal delimiter ` || `. The comment header on line 1 is excluded from the record count.
- All fields are nonempty; the literal evidence value `none` is preserved as a value rather than interpreted as a missing field.
- All note kinds belong to the task’s allowed vocabulary: unpursued implication (236), unproved claim (7), reading question (8), conjecture (2), self-flagged (2).
- Approximate sentence counts, with identifier dots and common abbreviations protected: 1 sentence(s): 255 records.
- No note exceeds the requested one-to-four-sentence range in this mechanical estimate.

## Exact source statuses and locators

- All 255 `status_exact` values and all 255 manuscript locator strings in the catalogue match the current DSS source cells exactly; the catalogue source-line values also match.
- Status totals: `claim (return: Known)`: 33, `claim (return: Proved)`: 146, `claim (return: Refuted)`: 57, `claim (return: Open)`: 19.
- The comparison file contains no replacement status field. A renderer joining each comparison to `context_catalog.json` by its exact ID can use `status_exact` verbatim and preserve the source’s `claim (return: ...)` qualification.
- No combined-note renderer was found in the scripts directory at this review time; this confirms the catalogue inputs and join keys, rather than claiming to certify future rendering code.

## Delimiter and Markdown checks

- Internal pipe characters in comparison fields: 0; literal tabs: 0; control characters: 0; fields with odd backtick counts: 0; fields with leading/trailing whitespace: 0.
- Skip the `#` comment header when parsing. Split records on ` || `, not on a single pipe.
- The supplied context statements may contain mathematical pipes (for example BISITE A.28); their source parser uses ` | ` and preserves the internal pipe. If full context text is embedded in a Markdown table, escape table pipes at rendering time without mutating the exact catalogue source string.
- The comparison fields themselves have no internal pipes or tabs and therefore present no detected table-column collision. CSV output should still use a CSV writer because prose contains commas and quotes.

## Topic check and scope

- The short topics were compared with the corresponding same-ID contextual statement openings. No obvious topic/ID mismatch was found.
- This review makes no judgment about manuscript readings, scan evidence, quoted wording, or whether a proposed mathematical relationship is correct. No images or frozen transcription were read.
- The comparison content was not edited.

## Reviewed input hashes

- `working/comparisons_dss.txt`: `3d55949f0e2df1da0711a3d22805b952dffeee50e78aed8859303438b0bc2b25`
- `working/context_catalog.json`: `e509e748ffea4789fb552ac4719e367faeefdfe0a06b79b5999c3eb7948f8ec4`
- `context/DOSSIER_STATEMENTS_WITH_STATUS.md`: `f6de029f0eae002860692e675986f32dc274f98c9d09cd32de30c421c0c1ebf3`

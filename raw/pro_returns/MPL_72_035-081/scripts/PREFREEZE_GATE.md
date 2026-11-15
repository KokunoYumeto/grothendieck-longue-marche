# Mechanical gate before transcription freeze

Checked at **2026-11-15 00:36:40 UTC**. This report reads saved text, records, and the progress log only. It supplies no manuscript reading and does not execute or record a freeze.

## Passing checks

- All 47 page fragments, scans 035–081, are present with matching markers.
- The combined transcription equals the direct byte concatenation of those page files.
- The inventory contains 1,052 rows, all with valid kinds, sheet kinds, and `transcribed=yes`; element identifiers are consecutive within every scan.
- Structural validation reports no brace, environment, file-order, marker, or completion-log error.
- The static TeX review reports zero diagnostics across 18 TikZ-CD environments: no remaining literal-cell-separator warning, empty-anchor warning, nested-diagram error, out-of-range relative arrow target, or unmatched explicit delimiter.
- All 64 source segments listed by the deletion proposal CSV are represented by their rebuilt deletion rows. This checks source-argument correspondence; it does not replace the primary reader's element-boundary decisions.
- The log contains exactly 47 correctly formatted audit entries, with valid UTC timestamps and one entry for each requested scan. At the check, neither a freeze record nor a context-open record was present.
- The previously stale scan 049 bottom-note wording has been updated. Its new inventory ID is **049.47**, with content `Attention, n-1 et non n!`.

The validator's remaining unclassified command names, `\x` and `\s`, are the previously checked TikZ `\foreach` variables. The absent research-notes file is expected before context is opened.

## Residual macro/count differences: existing coverage

| Scan | Count difference | Existing element | Explanation |
|---|---|---|---|
| 039 | 1 margin macro / 0 margin-note rows | Drawing **039.14** | The margin wrapper contains the already inventoried vertical emphasis stroke. |
| 059 | 3 margin macros / 2 margin-note rows | Diagram **059.07** | One wrapper contains the already inventoried upper-right diagram; the position preserves its marginal location. |
| 080 | 4 margin macros / 3 margin-note rows | Deletion **080.02** | One wrapper contains only the already inventoried cancelled `a_i` in the top-right margin. |

These residuals identify location wrappers around elements whose content kinds are already recorded. They supply no missing element for an additional inventory row.

## One inventory prefix to align

At the checked snapshot, **040.16** records `-\sigma\Pi\prime`, while the inserted argument in the source at TeX line 27 is `-\sigma\Pi'`. Align the inventory prefix with that exact existing source string during the primary reader's final record rebuild. No transcription change is proposed by this comparison.

## Integrity verification after the primary reader freezes

Use the read-only helper:

```sh
python scripts/freeze_verify.py --json
```

At final delivery, after context work:

```sh
python scripts/freeze_verify.py --require-context --json
```

It requires exactly 48 unique transcription hashes and 47 unique audit entries, compares current source bytes, verifies direct concatenation, and checks recorded audit/freeze/context ordering. Keep the original 48 manifest entries; the final comparison is documented with a separate summary statement.

No TeX compilation succeeded because the installation lacks the required format and package files. Static checks are the available syntax evidence. This limitation is documented in `MECHANICAL_REVIEW.md`; no distribution was installed.

No page, record, inventory, progress entry, or audit entry was edited while producing this gate report. Only supporting reports were refreshed or written.

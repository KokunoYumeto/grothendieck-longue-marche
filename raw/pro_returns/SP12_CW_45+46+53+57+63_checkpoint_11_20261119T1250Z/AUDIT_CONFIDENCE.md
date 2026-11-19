# Explicit audit confidence

`audit_confidence.json` is an optional, additive record of confidence supplied personally by the primary reader during the visual audit. The installed file contains no occurrences:

```json
{
  "version": 1,
  "pages": {}
}
```

No entries or confidence values are generated automatically. Missing entries retain existing first-pass behavior, including explicit `not assessed` placeholders.

## Schema

The top-level fields are exactly `version` (integer 1) and `pages` (object). Each key in `pages` is the mapped committed output path, such as `pages/EXAMPLE.tex`. Its value has exactly two fields:

| Field | Required value |
|---|---|
| `page_sha256` | SHA-256 of the exact current page bytes, as 64 lowercase hexadecimal characters |
| `occurrences` | Array of primary-supplied occurrence objects |

Every occurrence has exactly these fields:

| Field | Required value |
|---|---|
| `line` | Positive, one-based physical source line |
| `column` | Positive, one-based Python Unicode-code-point column at the backslash of the active unsure macro; a tab counts as one character |
| `macro` | The entire literal macro string returned by `_unsure_entries`, including its braces and all original whitespace; universal-newline text reading is used |
| `confidence` | Exactly `high`, `medium`, or `low`, supplied by the primary |
| `decision_ref` | Object with exactly `file` and `number`: the same page's mapped decision JSON path and its positive one-based decision number |

The occurrence key is `(page path, line, column, exact macro text)`. References are traceability; their existing confidence values are not substituted for the supplied occurrence value. Keep referenced decision ordinals stable during the audit; appending records preserves existing ordinals. The schema does not infer whether a reference is semantically appropriate.

## Validation and resolution

The shared validator checks the page hash, active parsed occurrence, exact coordinates and macro text, enum, same-page reference and reference bounds. Duplicate JSON keys, duplicate locations, unknown/missing schema fields, booleans used as integers, malformed data, parser warnings on an audited page, and stale mappings are rejected. There is no whitespace normalization, nearest-position search, macro expansion, reference guessing, or automatic relocation.

Every supplied entry must validate before the doubts output is overwritten. Invalid entries do not fall through to heuristic matching. A valid entry takes precedence only at its exact occurrence and reports `basis=primary_occurrence` plus its decision reference. Other identical macros receive no automatic propagation. The required five-column doubts table is retained.

If a page changes after an entry was supplied, the primary must revalidate the occurrence and supply its current coordinates, exact text, and page hash. The helper does not rebase or invent audit values.

## Mechanical interface

The pure functions are in `scripts/review.py`: `_audit_source_text`, `_audit_json_loads`, `_validate_audit_confidence`, and the extended `_unsure_confidence_detail`. `rebuild_doubts()` loads the optional file and completes validation before its single write. Existing callers with no audit index retain the first-pass resolver behavior.

The diagnostic captures exact page bytes and calls the same validator and resolver. It reports `audit_confidence_entries`, `audit_confidence_pages`, `primary_confidence_rows`, and a `primary_occurrence` count. Mechanical tooling can use the saved filename-map metadata; it need not read original sources. When loading review helpers without the module's initialization, include the three new pure functions and supply `json`, `re`, and `hashlib` in the namespace.

Run the synthetic tests with `python3 scripts/test_audit_confidence.py`. To validate committed output, run `scripts/diagnose_committed.py` with its explicit `--root` and `--page-map` options, using a saved metadata TSV. Tests use temporary synthetic strings and records only; they do not supply confidence to actual pages.

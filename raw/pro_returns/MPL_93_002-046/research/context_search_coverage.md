# Context-search and note-metadata coverage

Generated: 2026-11-15T11:47:56+00:00. Status: **PASS**.

Notes snapshot: `MPL_93_002-046_notes.md`; SHA-256 `456a268f724f1072ecd3ad32de893bb6a31172f7061b5b551813a4ae3e1a9ac2`.

82 note occurrences; 82 unique IDs. Groups: A: 4, C: 35, E: 27, O: 7, P: 9.

453 query occurrences: 143 have literal matches; 310 have explicit empty match lists.

| Check | Applicable | Passed | Failed IDs (heading line) |
|---|---:|---:|---|
| Unique ID | 82 | 82 | None |
| Nonempty File/location | 82 | 82 | None |
| Allowed Kind | 82 | 82 | None |
| Own-idea Confidence (low/medium/high) | 29 | 29 | None |
| Nonempty Context queries | 82 | 82 | None |
| Nonempty Context comparison text | 82 | 82 | None |

Allowed Kinds: self-flagged; unproved claim; conjecture; unpursued implication; withdrawn in the same text; reading question; own idea.

## Search method and scope

Literal substring within each physical source line after Unicode casefold, NFD normalization, and removal of combining marks (case- and accent-insensitive). Punctuation and whitespace are retained; no stemming, regular-expression, semantic, or cross-line matching.

Semicolon-separated Context queries values; surrounding whitespace and one final sentence full stop are removed. Query order and duplicates are retained. Empty matches are explicit [] lists.

Mechanical presence/uniqueness and enum checks only; location accuracy, mathematical content, attribution, and the adequacy of context comparisons are not assessed.

Exactly two supplied context files were searched:

- `context_sources/README.md` — SHA-256 `2f6607e0928bd941834fc2cf265f44a9415792762e29c856d9ceb41aacab9112`.
- `context_sources/notes/RESULTS_STATE.md` — SHA-256 `ef501ab156bc82217f3d7d3c830a5c18f1d1e8275a48bf6cb366aa58e0df03d8`.

Per-note fields, query terms, and matching file/line/text records are in `context_search_by_note.json`. This is a snapshot; rerun after any notes change.

Invocation from the work directory:

```sh
python tools/build_research_records.py
```

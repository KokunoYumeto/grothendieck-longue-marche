# Mechanical documentation tooling

`records.py` formats reader-supplied decisions. It performs no image reading,
OCR, textual recognition, mathematical verification, or TeX compilation.
All reading evidence, crop coordinates, inventories, notes, and confidence
judgments are entered by the sole page reader.

## Recording a page

Import `record_page` from `records.py`. Root must first initialize
`output/progress.log` with the actual starting UTC timestamp. The function is:

```python
record_page(
    scan, tex, changes, inventory, notes,
    doubts=None, hand=None, notation=None, abbreviations=None,
    checks=None, unresolved=None, audit=None,
)
```

`tex` is the full literal page fragment, including its `\scanpage{N}` marker.
`notes` is Markdown prose. `unresolved` is either Markdown prose or a list of
strings. All other collections are lists of dictionaries. Re-recording a page
replaces its records, so preserve any earlier rows that remain applicable.

| Collection | Dictionary keys |
| --- | --- |
| changes | `id, place, C, H, final, scan_shows, confidence, diff_C, diff_H, kind, error_kind, marked_H, consequential, S_id` |
| inventory | `element, kind, position, first_words_or_objects, sheet_kind, hand, transcribed` |
| doubts | `place, reading, alternatives, confidence, status` |
| hand | `habit, occurrences, scope, misreadings` |
| notation | `sign, form, scans, remarks` |
| abbreviations | `abbreviation, expansion, scans, remarks` |
| checks | `statement_id, date, who, type, outcome` |

Missing change flags default to false. IDs default to `71-NNN-NNN`, confidence
to `medium`, collation kind to `other`, and the error-sheet category to `Other`.
Missing inventory metadata defaults to `sheet_kind=text`, `hand=his hand`, and
`transcribed=yes`. The reader must override these when the page requires it.
Dates of check events default to the current UTC date. The reader should supply
an accurate `who` field; its fallback states that the effort is not exposed.

Use `consequential` for a short explanation, not merely `yes`, when a correction
changes the mathematics. Put every crop's scan and original-pixel box directly
in `scan_shows`. Witness-S confirmations can be recorded with both difference
flags false and their row identifier in `S_id`.

`record_page` writes the page and its records, rebuilds the aggregate files,
then appends the actual `scan NNN done ... UTC` event. It never records future
pages. For the actual second reading, call `record_audit(scan, narrative)`;
this saves the audit narrative and appends an `audited` event. Correct readings
and records before recording the completed audit.

## Rebuilding and validating

```bash
python output/scripts/records.py build
python output/scripts/records.py validate
python output/scripts/records.py validate --complete
```

The rebuild reads only already-written page records. It does not assert that a
page has been visually read. Validation checks file presence, table headers,
page order, H coverage constraints, inventory completion flags, unique change
IDs, confidence values, and coarse LaTeX brace balance. It does not compile TeX
or certify the accuracy of any transcription.

The `records/scanNNN/` files are the authoritative documentation inputs.
Aggregate files are regenerated. Put supplementary reader prose in any of
these optional files, which rebuilds preserve and incorporate:

- `LEGIBILITY.md`
- `FEEDBACK_EXTRA.md`
- `HAND_LOG_EXTRA.md`
- `NOTES_EXTRA.md`
- `DOUBTS_EXTRA.md`
- `CHANGES_EXTRA.md`

No source image, crop, attached witness, or JSON record belongs in this output
tree. Packaging and persistent checkpoint saving are handled separately by the
primary reader at the required times.

# Mechanical comparison-record review through scan 032

Scope: the 23 saved pages through scan 032. Only existing consolidated TeX and
documentation records were used. No image, OCR, witness transcription, or
mathematical reasoning was used. No page or authoritative record was changed.

## Existing proposal remains unapplied

All 23 rows in `exact_fragment_replacements_proposed.tsv` still match their
original complete-row hashes and original final cells. The proposal file is
unchanged. The incomplete blocks previously identified on scans 025, 027, 029,
and 031 remain pending primary-reader review.

## Scan 032 comparison-cell completeness

There are no new truncated main-text omission cells on scan 032. Its omission
rows 71-032-023 and 71-032-030 already describe complete individual marks. No
additional exact-fragment replacement is proposed for this scan.

## One witness-description/scope inconsistency

The same inserted set-name glyph is described differently in C's two records:

| Row | C description |
| --- | --- |
| 71-032-001 | doubtful calligraphic L/script L/L |
| 71-032-020 | deleted doubtful ens; raised Phi des |

The glyph reading belongs to 71-032-001. Row020 concerns the old `ens` deletion
and raised replacement/placement, but repeats the glyph as though C already
read Phi. Proposed scope-only repair for review:

- Keep 71-032-001 unchanged.
- In 71-032-020's C, H, and final cells, replace only the set-name glyph with
  `[set-name glyph separately collated: 71-032-001]`.
- Retain row020's old-ens cancellation, raised placement, `des`, evidence,
  confidence, category, and witness flags.

This would remove the inconsistent C description and make the two scopes
explicit. It requires no new glyph reading and need not change counts. It has
not been applied.

## Structural and overlap checks

The package validator reported 23 saved pages, zero errors, and zero warnings.
No new omission cell containing a long summary/ellipsis was found outside the
existing 23-row proposal. A text-only check found no H-omission final cell
containing another separately counted H-final string longer than 45 characters.
That narrow check does not establish that all shorter marks or semantic scopes
are disjoint; the concrete scan032 issue above remains for review.

## Prepared application script — not executed

`scripts/apply_exact_fragment_replacements.py` is ready for the reviewed
23-cell proposal. Its exact allowed ID set is fixed. It guards each complete
original change row and each source-page hash, protects place/flags/categories/
confidence, and changes only `final` cells. It recognizes the original and
already-applied states, so rerunning after a successful application makes no
additional changes or log entries. Independent reader edits cause it to stop.

On an authorized application it rebuilds the aggregates, verifies that counts,
page bytes, and combined-transcription bytes are unchanged, and writes a
mechanical application history. It adds no reading, audit, or mathematical
check event.

Commands for the primary reader after review:

```bash
# Read-only preview
python output/scripts/apply_exact_fragment_replacements.py

# Apply only after authorization
python output/scripts/apply_exact_fragment_replacements.py --apply
```

Neither command was run by the preparing agent. Only syntax parsing of the
script was performed.

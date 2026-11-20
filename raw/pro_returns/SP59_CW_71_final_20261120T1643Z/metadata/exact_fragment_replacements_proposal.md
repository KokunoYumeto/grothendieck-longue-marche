# Exact-fragment replacement proposal — approved and applied

The primary reader approved all 23 cells unchanged. They were applied on
2026-11-20 at 16:12:06 UTC using the guarded apply script. All original-row and
source-page hashes passed; witness flags, categories, count scopes, counts,
page bytes, and consolidated-transcription bytes were unchanged. Application
hashes are recorded in `exact_fragment_applications.tsv`. The retained TSV is
the reviewed proposal and its original-state evidence.

`exact_fragment_replacements_proposed.tsv` contains 23 proposed `final`-cell
replacements drawn from the existing consolidated pages:

| Scan | Rows |
| --- | --- |
| 025 | 71-025-027 |
| 027 | 71-027-018 through 71-027-025 |
| 029 | 71-029-018 through 71-029-022 |
| 031 | 71-031-011 through 71-031-019 |

The review covered all saved pages through scan 031. Eighteen proposed rows
replace truncated or descriptive main-text blocks. Five additionally replace
short prose/math summaries with their exact existing TeX: 71-027-019 and
71-031-011, 016, 017, 019. Already complete single-symbol or state descriptions
are not treated as truncated main-text blocks.

No page, comparison record, count scope, witness flag, confidence level, or
category has been changed by preparing this proposal. There was no image
reading, OCR, consultation of witness transcriptions, or mathematical analysis.
The parent reader separately authorized the scan017 command-spacing correction;
that syntax-only correction and its regeneration safeguard are applied and
documented in MECHANICAL_REPAIRS.md/.tsv.

## Exact text and exclusions

The proposed cells retain the consolidated spellings, accents, punctuation,
letters, indices, uncertainty, deletions, and included insertions. Existing row
boundaries and explicit exclusions are preserved.

Excluded material with an existing change ID appears as
`[separately collated: ID]`. Explicitly quoted material without a change ID uses
`[excluded quotation in H: locator; no change ID]`; no ID is invented. These are
editorial scope markers in comparison cells, never additions to a transcription
page. Where only an underline property is excluded, its wrapper is removed from
the comparison cell and its words remain. The actual page markup is unchanged.

Every proposal includes the old final field, exact new field, exclusion notes,
source anchors, a hash of the complete original change row, and a source-page
hash. Original flags and categories are copied into extra columns to make their
preservation reviewable. All referenced change IDs were checked against the
current records. Applying only these final-cell replacements would leave the
number and classification of change rows unchanged.

## Scope details reviewed and approved by the primary reader

- **71-027-023 and 71-027-024:** the generic exclusion wording does not name the
  `tel` underline or the `ensemble convexe` underline in these particular
  occurrences. The proposal retains those source macros rather than infer an
  additional exclusion. The primary reader checked H027 and confirmed that H
  quotes neither this `tel` underline nor the Lemme-IV `ensemble convexe`.
- **71-031-015:** the in-paragraph stippled group is marked as 71-031-005;
  the standalone marginal bullet following the blank lemma reference is marked
  as 71-031-006. This mapping follows the existing record labels and macro
  placement, without a new visual decision.
- **71-031-016:** the proof-ending sentence explicitly included by this row is
  retained. The generic exclusion of H's quoted final sentence refers here to
  the page-foot sentence beginning `On veut étudier`, which lies outside all
  proposed source spans.
- **71-027-020:** the whole uniqueness phrase is masked according to the old
  cell's explicit exclusion, with both existing IDs 71-027-005 and 71-027-006.
  The circled cap and `ens. des` insertion receive clearly identified no-ID
  quotation markers.

All 23 replacements above have been applied unchanged. The separate scan033
proposal was also approved and applied at 16:17:39 UTC; its own application
history documents the comparison and H-flag changes.

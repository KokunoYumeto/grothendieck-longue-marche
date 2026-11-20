# Scan 033 C-fragment and count-scope proposal — approved and applied

The primary reader approved these exact comparison cells and exclusions. They
were applied at 2026-11-20 16:17:39 UTC. The immutable proposal TSV retains its
original source hashes and review-state evidence; the application record is
`scan033_comparison_applications.tsv`. The final evidence omits the proposed-
clarification label and replaces its obsolete C-only wording.

The reader also authorized H omission comparisons for 71-033-001, 002, and 003:
each now has `diff_C=yes`, `diff_H=yes`, `kind=omission`, and the retained
`error_kind=Symbols and indices`. H therefore increases by three while C and
distinct-place totals are unchanged. No page text changes.

The eight H main-text omission rows, 71-033-012 through 71-033-019, were checked
against the supplied witness-C page text and the current consolidated page.
This was mechanical textual extraction only: no image, OCR, or mathematical
argument was examined. Six rows required comparison-cell updates; 012 and 017
were included as comparison-text controls. All eight rows received the approved
evidence clarification on application.

`scan033_comparison_replacements_proposed.tsv` contains exact proposed C and
final fragments, old cells, source-file hashes, complete original-row hashes,
and the review-state flags/categories. The TSV itself is retained unchanged as
the approved proposal; application history records the final row hashes.

## Three individually counted signs excluded from broader omissions

| Broader omission row | Sign owned by separate row |
| --- | --- |
| 71-033-013 | 71-033-001 |
| 71-033-014 | 71-033-002 |
| 71-033-016 | 71-033-003 |

The actual C fragments contain `\varnothing`; the consolidated fragments
contain `\phi`. Each is replaced, in both proposed comparison cells, by the
same `[separately collated: ID]` marker. The local glyph row retains the C
comparison and now records the individual H omission; the broader H-omission
block explicitly excludes it. The approved evidence text states that scope
exclusion. No row or confidence changes; only the three reader-authorized H
flags and kinds change alongside these comparison cells.

## Other restored witness-C details

- **71-033-018:** C's `\unsure{A.|A}` and `\unsure{réfait|réfoit}` are restored
  in the proposed C column. The final column retains the consolidated choices.
  The authorized `\in A.` command-spacing correction is reflected in the
  proposed final fragment, without treating it as a reading difference.
- **71-033-019:** C's opening and closing delimiter doubts
  `\unsure{[|(}` and `\unsure{]|)}` are restored in its column. The final
  column retains the consolidated square brackets.
- **71-033-015:** the existing exclusion of H's quoted parentheses around
  `J-` is retained. The proposal marks the opening and closing insertion
  positions separately, using explicit no-ID quotation markers. The slanted
  annotation remains outside the main-text block.
- **71-033-017:** the crossed margin note remains outside the extracted block,
  as it is already compared in 71-033-006 through 71-033-011.

## Applied work kept separate

The primary reader separately authorized and received two repairs:

- 71-032-020 now masks its set-name glyph in C/H/final with
  `[set-name glyph separately collated: 71-032-001]`. All flags and classifications
  are unchanged, and its regeneration metadata is updated.
- The scan033 page's `\inA.` token is now `\in A.`, with a read033.py safeguard
  before block extraction. No reading-change row was added.

Those applied repairs are documented in MECHANICAL_REPAIRS.md/.tsv. The scan033
comparison-cell proposal above is now applied. The earlier 23-cell proposal
was approved and applied unchanged at 16:12:06 UTC, with its
original-row and source-page hash guards satisfied. The separately authorized
scan010 scope narrowing and scan013 relation split are also applied. Structural
validation covers all 25 saved pages with zero errors and zero warnings. The
scan033 application left all page and consolidated-transcription bytes
unchanged. A guarded in-memory step in read033.py preserves the approved
comparisons and flags on regeneration, refusing changed source-page text.

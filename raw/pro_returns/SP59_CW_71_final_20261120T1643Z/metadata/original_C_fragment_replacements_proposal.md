# Original C fragment replacements — approved and applied

The primary reader requested exact source-C comparison fragments for the
remaining broad main-text omission rows whose C cells say `Present in C` or
`Main paragraph transcribed in C`. The accompanying
`original_C_fragment_replacements_proposed.tsv` contains **48 C-cell-only
proposals**: all 47 broad placeholders, plus the adjacent inserted-sentence
placeholder `71-023-011` (`full parenthetical assumption`). All 48 C replacements were approved unchanged by the primary reader and
applied at 2026-11-20 16:34:54 UTC. Approval and applied-row hashes are recorded in
`original_C_fragment_applications.tsv`. The proposal TSV itself is unchanged.

This work copied the supplied original C TeX mechanically and matched it to
existing comparison scopes. No image, OCR, source-H reading, ink decision, or
mathematical interpretation was used.

## Coverage

| Scan | Proposed IDs | Cells |
| --- | --- | ---: |
| 023 | 71-023-011 and 71-023-018 through 027 | 11 |
| 025 | 71-025-020 through 028 | 9 |
| 027 | 71-027-017 through 026 | 10 |
| 029 | 71-029-017 through 025 | 9 |
| 031 | 71-031-011 through 019 | 9 |
| **Total** | **47 broad omissions and one inserted sentence** | **48** |

The existing C cells for the broad omissions on scans021, 033, and 034 already
contain fragments. Their rows are outside this proposal.

## What changes, and what is preserved

Only the C field was replaced. H, final, place, evidence,
confidence, categories, witness flags, IDs, and count scopes remain unchanged.
Application left C/H/distinct-place counts unchanged: C 72, H 499, distinct places 516.

Original C uncertainty expressions, candidate order, spelling, punctuation,
indices, and included revision markup are retained. The proposals do not
substitute the reader's resolved final forms into C. Examples include the
interieur/intérieur and exterieur/extérieur alternatives in 023-011, the
comma/3/semicolon order in 025-023, source alternatives in the chain argument,
the QED alternatives in 027-026, the cancelled-n doubt in 029-024, and
considĕre/considère in 031-017.

The H cells identify absence of a transcription or an editorial synopsis.
These descriptions are appropriate to their existing omission scopes: there
is no omitted main-text H fragment to invent or copy into those cells. No H
replacement is proposed.

Existing explicit masks are repeated with identical wording and order.
Where an existing final cell omits an excluded annotation without a displayed
mask, the C proposal omits that same annotation and documents the operation
in the `exclusions` column. No new scope is introduced.

## Scope details reviewed and approved by the primary reader

- **023-011:** the additional C proposal copies the complete original inserted
  sentence, including C's two accent alternatives. The final cell was separately
  approved and applied at 2026-11-20 16:24:09 UTC, with both underlines and the
  final `.)` / `).` uncertainty. Its source reading and flags did not change.
- **023-022 and 023-023:** the existing excluded interlinear explanation and
  three Remarque insertions remain outside these base-text cells. Their original
  C wording is not allowed to expand the established omission scopes.
- **023-025 and 023-026:** the existing exclusions of marginal marks, the
  inserted assumption, quoted underline property, inserted endpoint condition,
  and crossed endpoint clause are preserved. The assumption is represented
  separately in 023-011.
- **025-020:** the excluded x-ne-y, beta, and ouverts insertions, cancelled beta,
  marginal mark, and separately compared existence-phrase underline remain
  excluded. Original C alternatives in the retained base text remain literal.
- **027-021:** follows the documented removal of three quoted underline
  properties (`pour nous` and two `ensemble convexe` occurrences), retaining
  the words and original C uncertainty expressions.
- **029-023:** follows its current base-text scope by removing inserted `dit`
  and the parenthetical insertion, then unwrapping the `Definition`, `le`,
  and `co` underline properties. The local parenthesis readings and le/co
  underline are already compared separately.
- **031-015:** repeats the two existing exclusion markers as editorial scope
  boundaries even though C has neither excluded ink mark. It supplies no
  mark as source-C text.
- **025-022, 027-017, and 029-025:** retain literal original-C heading underline
  markup. The current final comparison cells use shorter heading representations;
  these C-only proposals do not change those final cells or count markup as a
  new reading difference.

## Integrity guards

Each TSV row includes the complete original-source file SHA256, the complete
current change-row SHA256 (NUL-joined values in `records.CHANGE_FIELDS` order),
and the existing final-cell SHA256. Source anchors in the consolidated TSV
are **inclusive prefixes and inclusive suffixes of the original source span**,
before scope exclusions. No source file is attached to the deliverable.

All 48 IDs, old placeholders, source hashes, row hashes, final-cell hashes, and
carried flags/categories were checked against the current files. The proposed
IDs exhaust the three identified generic C placeholders in the saved records.
Every unmasked source character in the extracted fragments was checked as
retained source material; the only added text is an explicitly identified
editorial exclusion marker.

The proposal TSV SHA256 at preparation is
`4b928bf81cbd0cea2562b37dc07f86d6764ce3b964dfd1519e670dbb32c40caf`.

The approved 023-011 final-cell repair is documented in
MECHANICAL_REPAIRS.md/.tsv. All 48 C-cell replacements above were subsequently
applied at 2026-11-20 16:34:54 UTC, with every source/row/final guard satisfied. Exactly one
aggregate rebuild followed. All 26 frozen transcription hashes remained
unchanged, and complete/audit structural validation reported zero errors and
zero warnings. No first-reading script was rerun and no page-done or audit
event was added.

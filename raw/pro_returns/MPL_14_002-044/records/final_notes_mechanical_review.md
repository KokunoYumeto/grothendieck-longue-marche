# Final notes and doubts mechanical review

**Current-file snapshot:** 2026-11-15 01:24:56 UTC. Only this report was written.

## Result

**The final assembly passes the requested mechanical checks.** The notes contain 97 unique note IDs and 97 matching unique anchors: **B 5; M 34; A 38; RT 8; R 8; H 4**.

All 97 notes have a frozen-page filename or the edition's explicitly defined `scanNNN` filename alias, a location, context filename/alias with cote and scan or an explicit bounded negative/unavailable-context statement, and register/status metadata. The globally declared WG2/Hua status keys apply as stated. B05's previously missing labelled Register field is now present; its body retains the claim-level status qualifications.

The review found no evidence-record header, search-ledger appendix, handoff section, or patch text accidentally appended inside a note. RT3's lettering dictionary is an intentional accompanying table.

## Math and Markdown

The delimiter/brace scan found no unmatched or nested math delimiter and no unbalanced TeX brace. The final independent Pandoc Markdown parse succeeds without warnings and recognizes **689 math spans** and **7 tables**, with column counts **3, 4, 3, 3, 3, 3, 3**. No unintended table columns or unbalanced inline-code span was found in the notes.

A separate earlier MathML export check gave converter-specific fallbacks for 14 expressions using the old-style `\rm` declaration and one using `\varprojlim`. These are macro-compatibility warnings from that converter, not delimiter/brace errors. They do not block the Markdown deliverable; no browser-render certification is claimed.

## B01/B04 and bibliography

- B01 retains the full profinite formulation and full profinite geometric abelianization, together with the Tate restriction on the prime.
- B04 retains hyperbolicity, the smooth proper completion, `g\in D_I`, the containment-in-inertia conclusion of Theorem 30, and maximality/Corollary 31 for full inertia.
- The Milne citation key has been changed to `Milne01`, avoiding the overlap with note M01.

## Doubts-file repairs verified

All four formatting repairs are present: the closing backtick on `$=$s`; removal of the blank line before the Torus-character row; `\unsure{k-groupe\|s-groupe}`; and `\unsure{\operatorname{Tr}\|\operatorname{tr}}`.

The final GFM parse succeeds and gives:

| Table | Columns | Data rows |
|---|---:|---:|
| Notation | 3 | 39 |
| Reading doubts | 6 | 283 |
| Abbreviations | 3 | 48 |

The reading-row count agrees with the stated 282 `\unsure` occurrences and one `\illegible` occurrence. The inspected table cells have no remaining unescaped alternative pipe or unmatched backtick. The repairs preserve the displayed reading text.

## Audited files

- `MPL_14_002-044_notes.md`: 139665 bytes; SHA256 `1d893e050ea398c31adda0ff63f874b55e8e9ed16067387d79c38532b8c1aa04`.
- `MPL_14_002-044_doubts.md`: 41561 bytes; SHA256 `5b9f80400f4c6489de0fa75f7283bb67fe29a31044487f742f4b0fdfbfb17a01`.

No notes, note-source record, doubts file, frozen page, combined transcription, inventory, or progress log was edited by this review. This report covers assembly, metadata, and rendering syntax; it is not another manuscript-image audit or a new review of all mathematical arguments.

# Mechanical review after scan 030

Recorded 2026-11-20 15:52:56 UTC. Scope: the 21 saved pages 007–015, 017, 019, and 021–030. This is a review of TeX source and documentation records, not an ink reading or second-reading audit. No image, OCR, source witness page transcription, or external mathematical source was consulted; the supplied PREAMBLE was read only for macro and package definitions. No authoritative page, record table, or check-event classification was changed.

## Definite lexical issue

- **Scan 017, page-file line 71:** `U\subsetC` contains the undefined fused command `\subsetC`. Syntax-only fix: `U\subset C`. Add the corresponding normalization before the save in `read017.py`. No reading-difference row is appropriate for this command separator.

No other definite undefined command or environment-nesting defect was found through scan 030. The prior `\partialX`, `\cupV`, and `\subsetD` faults are absent. Local foreach variables such as `\dx`, `\dy`, `\ink`, `\point`, `\p`, `\x`, `\y`, and `\v` were not treated as undefined commands. TeX was not compiled.

## Every illegible macro occurrence

There are **3** source occurrences of `\illegible`, all with argument `1`, all inside `\deleted`, and all in prose contexts. None is syntactically inside math mode, a diagram, or a figure. The occurrences are scan 012 line 70, scan 023 line 19, and scan 029 line 25. This is a syntactic result only; the primary reader remains responsible for the ink and whether the words are recoverable. Full source context and flags are in `mechanical_review_after_scan030_illegible.tsv`.

## Incomplete final-reading comparison cells

Thirteen H-omission rows use ellipses, English summaries, or placeholders such as `[complete ...]` in the `final` field, rather than recording the full compared fragment:

- 71-025-027.
- 71-027-018, 71-027-020, 71-027-021, 71-027-022, 71-027-023, 71-027-024, 71-027-025.
- 71-029-018, 71-029-019, 71-029-020, 71-029-021, 71-029-022.

These rows flow unchanged into the public collation's `final_reading` column. The actual consolidated page text is present; the defect concerns the comparison record. Copy the corresponding exact consolidated fragments into these cells, retaining the existing deliberate exclusions for words/marks compared in separate rows. If an exclusion divides a passage, use distinct, explicitly scoped fragments or rows instead of an unmarked summary. The accompanying TSV preserves each affected cell for review. This finding does not assert that the page transcription omits anything.

## Scope and compound-row notes

- The repaired scan 021 omission cells now exclude their separately counted margin drawings and the specific `aussi`/`couple` underline decorations. No recurrence of the previously identified exact annotation duplication was found in those repaired cells.
- **71-010-033** mixes the initial `de/sur` reading difference with an unchanged final `B/B-prime` doubt. Its H difference is supported by the initial unreadable group; narrow the counted change's scope to that group and keep the final B uncertainty in the doubts record. This does not require another C/H correction count or a new ink decision.
- **71-013-007** explicitly names a vertical equality beneath `X_i` and a separate oblique link beneath the boundary term. If counting independent relation placements, split into `71-013-007a` (vertical equality) and `71-013-007b` (oblique link), inheriting the existing evidence, confidence, and witness flags. The current record may instead be retained as one reconstructed diagram unit if that is the primary reader's stated inventory/counting convention; no forced split is asserted mechanically.
- **71-007-013** remains the approved single cancelled arrow-and-Sigma diagram fragment, not a new grouping defect.

## Structural validation

The current package validator reported **21 pages, zero errors, zero warnings**. It checked table schemas, allowed H collation kinds, page ordering, inventory completion flags, coarse brace balance, and exact agreement between the combined transcription and page fragments. Independent spot checks found no difference flag whose final string exactly duplicates the flagged witness string. This validation does not prove linguistic or mathematical correctness.

The snapshot TSV records hashes of the page and per-page record files reviewed. No proof-check event, scan-done event, or scan-audited event was added for this mechanical review.

# Text-only inventory audit: C123-01_123_scan018

Scope: compared only the completed R1/R2/R3 `report.json` and `reading.tex`, packet `C.tex`, `H.tex`, `C_questions.md`, and assembly code `out/scripts/finalize_page.py`. No image was opened, no OCR or external source used, and no reading decision made. Statements about marks below are quotations or summaries of reader reports, not independent observations of ink.

## Additional loci absent from R1 differences

1. **Leader attached to the first raised class c.** R2 D07 calls this a “two-armed bent stroke”; R3 D07 describes a “left curve” descending and rising to the right. R2 inventory item 6 includes “c and bent insertion marker”; R3 items 6–7 explicitly separate c and its leader. R1 inventory item 5 records c but does not explicitly record the leader, and R1 reading has only `\inserted{\handwritten{$c$}}`. Thus this is both a difference-list gap and a graphic-detail gap in the R1 base reading/inventory. Reported whole-image boxes: R2 `[1533,223,1614,291]`; R3 `[1535,227,1599,286]`. Both reader difference entries have `crop: null`; assembly requires the main reader's evidence crop.

2. **First cancelled homomorphisme, before élément.** R2 D13 and R3 D13 both report the first `un \deleted{homomorphisme} élément`, omitted by H. R1 already retains this in its reading and inventory item 9 but has no difference entry. Keep this distinct from R1 D17, the later deleted `homomorphisme G_m -> T`. Reported whole-image boxes: R2 `[409,448,677,494]`; R3 `[413,454,684,490]`. These entries also have `crop: null`.

No further substantive R2/R3 locus absent from R1's difference coverage was identified. The above are coverage findings only; final readings and graphics remain for the main reader.

## Deduplication and comparison cautions

- Counts differ because the readers split composite loci differently: R1 has 49 differences/46 inventory entries; R2 54/49; R3 48/55. R1 difference IDs skip D36; do not treat the maximum ID as the count or reuse that gap without deliberate mapping.
- R2 D08/D09 split the conjugacy curve and typed medium already combined by R1 D07. R2 D28/D31 split orbit-note medium/curve already combined by R1 D26.
- R2 D21/D22 and R3 D19/D20 split the Weyl product glyph from the underlined Z/R alphabets; R1 D18 already includes both. If retaining one composite row, preserve both subclaims.
- R2 D32–D35 split ou-encore attachment, glyph, medium, and enclosure; R1 D27–D29 already cover that group. R3 D05 combines typed-addition medium across several regions; it does not identify a new text locus beyond R1's local medium entries.
- R2/R3 separately inventory the crossed cell after the l/o overlay, whereas R1 inventory item 7 and D08 combine it with the overlay. This is already a represented locus, but the reported readings differ: R1 draws an uncertain crossed impression, R2 uses one cancelled illegible character, R3 a tentative cancelled n. Do not lose the cancellation component when consolidating.
- R2 D37's discussion of the full stop after Cent(i) and closing parenthesis extends its audit around the small preceding mark; those following signs are already present in all three readings and C/H. It is not an additional difference.
- All three report the live baseline comma at non vide, but R1 serializes it after the insertion and R2/R3 before. This is an attachment/serialization issue within R1 D41, not a new locus.
- R2/R3's a/e or da/de treatment before foncteurs is an alternate reading of R1 D37, not an extra locus. The plural foncteurs is separately covered by R1 D38.
- R2/R3 combine both Z indices in one difference; R1 D46/D47 separate them. R1 additionally marks uncertainty on the first handwritten Z index. Keep the two occurrences identifiable when consolidating.

## C-doubt coverage

Every report contains 19 `c_doubts` rows: the 18 question-table rows plus the first-tensor doubt from C.tex that is not separately listed in C_questions.md. No uncovered C question or C.tex `\unsure` locus was found.

The article before foncteurs recurs in C-question rows 8, 16, and 18, and in the corresponding three report rows. These are one physical article locus; row 16 additionally checks plural foncteurs and unaccented fibres. Preserve the question coverage references without triple-counting the article as three differences.

The three prior C notes are also covered: the characteristic-zero hesitation is retained in every reading; the stabilizer structure/dimension/semi-simplicité question is retained and inventoried; the opening cancelled “sur la catégorie” is retained and separately inventoried. The archive number 17 is recorded only as a comment in all three readings.

## Complete inventory coverage

Across the reported inventories, all body blocks, both displayed morphisms, the deletions, handwritten fills, principal inserted clauses, large cancelled torsor explanation, and final unfinished Un_c sentence are covered. R1 uses broader body-block entries where R2/R3 use smaller entries; that accounts for much of the count difference.

The only graphic object explicitly inventoried by another reader but absent as an explicit detail from R1's reading/inventory is the initial c leader noted above. R2's separate article-overlay inventory entry is already covered by R1's map-explanation body entry and D37. R3's separate curves and body blocks correspond to R1 composite entries. No other complete-inventory coverage gap was found by textual comparison.

Assembly note: `finalize_page.py` copies differences and inventory from the chosen base unless the specification supplies overrides/additions. The first deleted homomorphisme therefore needs an added difference even though its text is already in R1; the c leader needs whatever text/inventory treatment the main reader determines after viewing its own evidence. This audit does not edit that specification or determine either reading.

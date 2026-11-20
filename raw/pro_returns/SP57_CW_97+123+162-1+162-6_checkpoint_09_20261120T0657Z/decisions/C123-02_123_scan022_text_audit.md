# C123-02_123_scan022 — text-only union audit

## Scope and completion

Complete comparison of `packets/C123-02_123_scan022/{C.tex,H.tex,C_questions.md}` and all three readers' `reading.tex` and `report.json` under `out/readers/C123-02_123_scan022/`. R2 was complete and its JSON parsed successfully when audited. Counts: R1 has 26 differences / 30 inventory entries; R2 has 29 / 40; R3 has 30 / 40. Each has 12 `c_doubts` entries.

The initial reader comparison inspected no images, crops, previous pages, or root decision files. Root subsequently authorized a text-only crosscheck of the named final spec and preview; that check is recorded at the end. This audit establishes textual agreement, divergence, and reporting coverage only. It does not decide the ink or validate any drawing coordinates.

## Conflicts and distinct additional loci

1. **First superscript 2: medium.** C, R1 and R3 encode `^{2}`; R2 encodes `^{\handwritten{2}}`. R1 inventory 12–13 leaves the medium less secure; R3 D11, inventory 16, `remaining_doubts`, and its final comment explicitly leave it unresolved. R2 inventory 16 calls it handwritten. R2 has **no dedicated differences entry for this handwriting attribution**. Under root's confirmed reporting convention, C's absent wrapper does not assert typed medium, so R2's wrapper is not by itself a substantive C change. H's editorial note explicitly calls both exponents handwritten. The glyph 2 itself is unanimous.
2. **`appeared`: stroke representation and alternative.** All three replace C's asserted deleted predecessor / handwritten replacement with a doubtful graphic overlap. R1 draws two traces, with a curved lower trace; R3 draws two straight obliques; R2 draws one continuous curved trace and alone puts an explicit `|k` alternative after the graphic inside `\unsure`. All three reports leave chronology unresolved. This is a drawing difference, not three competing completed words.
3. **Bottom `extension`: two separate uncertain cells.** R1 has `extension`; R2 has `exten\unsure{s}ion` (R2-D25); R3 has `ext\unsure{e|a}nsion` (D25). The R2 uncertainty is the **s**, while R3's is the **second e**. Neither subsumes the other.
4. **Bottom second quotient denominator.** R1 and R3 have `\mathbb{Z}/h\unsure{Z|\mathbb{Z}}`; R2 has `\mathbb{Z}/h\mathbb{Z}` without doubt. R2's notation entry explicitly claims paired diagonals in both groups. First quotient and second numerator agree as `\mathbb{Z}`; the final standalone central `Z` agrees as plain `Z`.
5. **Bottom `hence`.** R1: `hence`; R2: `hen\unsure{ce}`; R3: `\unsure{hence}`. These differ in the extent of doubt, not the proposed word.
6. **Bottom `order`.** R1/R2: `order`; R3: `\unsure{order}`. This is an additional R3 locus, separate from `hence`.
7. **Interrupted vertical trace at bottom multiplication sign.** R2 alone draws and inventories it (R2-D27; inventory 37). It is absent from C, H, R1 and R3. R2 calls it a separate interrupted upright trace without assigning a mathematical function; its inventory calls the hand only “handwritten-looking.” Presence and ink status remain for the scan reviewer.
8. **Bottom right-hand slant.** R3 alone uses `rotate=-3` for the right prose and order formula and explicitly reports their downward slant. All three place the order formula on a lower row. This is an additional placement feature, not a different formula.
9. **Upper-right heading.** R1 alone adds `\hfill`. All three inventories locate the heading at the upper right, but R2/R3 retain C's unaligned heading code. No inference about actual rendering is made without the macro/layout context.

## Missing or incompletely reported drawing / placement elements

- **R1 body insertion cues:** inventory 15 says “Of G-tilde insertion and cue” is transcribed, and inventory 18 says “Raised generating and insertion cue” is transcribed. Its actual reading retains only `center\inserted{\handwritten{of $\widetilde{G}$}},` and `a\deleted{n} \inserted{generating} element`; it contains no explicit curve or above-line TikZ placement at either locus. R1-16's evidence also mentions the handwritten insertion curve without drawing it. R2-D13/D17 and R3 D14/D18 supply both curves and positions. The live comma after `center` is preserved by all three, but R2/R3 explicitly anchor it to the baseline.
- **Bottom annotation and lower formula:** all three retain the annotation text, oblique leader, and separate lower-right formula. R1 uses two small local diagrams; R2 lays out the full footer in fixed centimetre coordinates and `\scriptsize`; R3 uses linked em-based nodes. The different geometry must not be counted as omitted words. Only R3 explicitly encodes the right-hand slant.
- **R2-only vertical trace:** absent from R1/R3 inventories as well as their readings. It is not an inventory-only claim by R2: the four interrupted segments are actually in its reading.
- **Underlines beneath the two body Zs:** all readings retain `\underline{\mathrm{Z}}/\mathrm{h}\underline{\mathrm{Z}}`. R3 inventory 23 inventories the rules separately and leaves their medium unassigned. R1 groups them in inventory 16; R2 records them in its differences/notation but has no separate inventory item. This is inventory granularity, not a missing underline in R2's reading. R1's grouping phrase “handwritten phi, underline rules and star” is less precise about the rules' medium than R3's explicit statement.
- **Archive 21:** present as a comment in all readings and mentioned in all reports' notes. Only R2 gives it its own inventory entry (40). It is not missing from R1/R3 and is not an authorial page number.

## Union of difference loci

IDs below are the actual report IDs: R1 entries use `R1-`, R2 entries use `R2-D`, and R3 uses bare `D`. A dash means no dedicated difference entry; other coverage is stated. Split rows expose distinct letters or graphic elements bundled into one reader entry.

| Locus | R1 | R2 | R3 | Union result / coverage |
|---|---|---|---|---|
| Doubtful handwritten place | R1-01 | R2-D01 | D01 | All `\unsure{Massy}`. |
| Journal abbreviation | R1-02 | R2-D02 | D02 | All `\unsure{Maer.\|Amer.}` in C order. |
| First title initial t/T | R1-03 | R2-D04 | D03 | All deleted typed t and handwritten T. |
| First title quotation strokes / ellipsis | R1-04 | R2-D03 | D04 | Same reading; R2/R3 explicitly discuss the three separate stops. |
| Second title quotation strokes | R1-05 | R2-D05 | D06 | Same reading. |
| Typed ai and transposition curve in polynomail | R1-06 | R2-D06 | D05 | Same C graphic, no supplied replacement letters. |
| appeared mixed cell | R1-07 | R2-D07 | D07 | Shared rejection of asserted chronology; drawings differ. |
| Alg. initial | R1-08 | R2-D08 | D08 | Same deleted a/A doubt and pen A. |
| First quadruples extra cell | R1-09 | R2-D09 | D09 | Same deleted a/u doubt. |
| in apposition quotation marks | R1-10 | R2-D10 | D10 | Same typed opening and handwritten closing marks. |
| First superscript 2 medium | —; inventory 12–13 | —; inventory 16 | D11 | R2 handwritten; R1/R3 unresolved. |
| First body phi | R1-11 | R2-D11 | D12 | Same `\handwritten{\phi}`. |
| where W predecessor | R1-12 | R2-D12 | D13 | Same H/W doubt under pen W; confidence differs only. |
| of G-tilde insertion and curve | —; inventory 15 | R2-D13 | D14 | Text in all; explicit curve/layout only R2/R3. |
| Indicatrix phi | R1-13 | R2-D14 | D15 | Same `\handwritten{\phi}`. |
| Two underlined body Zs | R1-14 | R2-D15 | D16 | Same underlined ordinary typed letters. |
| Cancelled n of an | R1-15 | R2-D16 | D17 | Same cancelled n. |
| generating position and curve | —; inventory 18 | R2-D17 | D18 | Explicit curve/layout only R2/R3. |
| generating typed medium | R1-16 | R2-D18 | D18 | All typed; differs from H's explicit handwritten attribution. |
| stablity | R1-17 | R2-D19 | D19 | All change C's stability to H's stablity. |
| rigid quotation marks | R1-18 | R2-D20 | D20 | Same paired strokes. |
| in general position quotation marks | R1-19 | R2-D21 | D21 | Same paired strokes. |
| opposite quotation marks | R1-20 | R2-D22 | D22 | Same paired strokes. |
| automorphisms k/i overlap | R1-21 | R2-D23 | D23 | Same overlapping glyphs without chronology; offsets vary. |
| Final quadruples cancelled a | R1-22 | R2-D24 | D24 | All definite deleted a. |
| Bottom extension, second e | — | — | D25 | R3 `e\|a` doubt only. |
| Bottom extension, s | — | R2-D25 | — | R2 doubtful s only. |
| Bottom second denominator Z | R1-23 | —; notation | D26 | R1/R3 plain/double-struck doubt; R2 definite double-struck. |
| Bottom cancelled parenthetic group | R1-24 | R2-D26 | D27 | Same `(G)` / `(\widetilde{G})` doubt. |
| Bottom interrupted vertical trace at × | — | R2-D27 | — | R2-only extra drawing. |
| Bottom center annotation, leader and placement | R1-25 | R2-D28 | D29/D30 | All retain text and leader below-left; different layouts. |
| Bottom lower-right order formula and placement | R1-26 | R2-D28 | D29 | All lower the same `hz\varphi(h)`; R3 additionally slants it. |
| Bottom hence doubt | — | R2-D29 | D28 | ce-only versus whole-word doubt. |
| Bottom order doubt | — | — | D28 | R3-only whole-word doubt. |

Additional shared elements covered by the inventories/readings, without a separate conflict entry: salutation and continuous paragraph ending `(they`; date; second handwritten exponent 2; handwritten indicatrix star; all three body intersection signs; handwritten footnote call after the comma following e; underline under `distinguished`; full handwritten bottom note and its opening asterisk. No body continuation or replacement title has been supplied.

## C-doubt coverage and packet inconsistencies

All three reports cover the same **12 distinct C doubt/question loci**: place; abbreviation; Alg.; first quadruples; last quadruples; appeared; where W; automorphisms; bottom cancelled group; polynomail; suggests number; an/generating. Repeated abbreviation and grouped quadruples rows in `C_questions.md` do not create unexamined loci.

- **Last quadruples:** the question file groups first and last as deleted a/u, but actual C has `quadr\deleted{a}uples` at the last occurrence. Each reader explicitly considers that occurrence and retains definite a. This is a reported resolution, not a silently missed alternative.
- **suggests number:** actual C and H both have `suggests number`; all readings agree. `C_questions.md` offers `suggests a number` as a contrast but does not label its table columns. The readers' claims that the question file says *H* has the article overstate what that headerless row expressly identifies. The factual point that supplied H has no article is correct.
- **Questions and page identity:** every report's notes preserve the interrogative status of the general-position, distinguished-class and automorphism passages, the break at `(they`, and the distinction between quoted article references and a page title. They also cover date/place and absence of an authorial page count. These narrative question notes need no added glyph-doubt entry.
- **Additional uncertainties outside the original C doubt list:** first 2 medium; footer second denominator; footer e/a, s, hence, order; and the extra vertical trace must remain in the union. The two body insertion curves and footer placement/slant also require independent disposition.

## Report-to-reading consistency

A whitespace-insensitive literal check of every `differences[].reading` against its own complete `reading.tex` found only these two nonliteral snippets:

1. **R2-D18** says `\inserted{generating} (typed)`. The parenthetic `(typed)` is explanatory report prose, absent from the reading; the macro itself is present and is not wrapped as handwritten.
2. **R3 D11** says `\operatorname{card}(\mathrm{W})^{2} % medium unresolved: typed or handwritten`. The reading contains the same formula and puts the medium qualification in a final comment instead of immediately after it.

Neither is a substantive transcription mismatch. All other `differences[].reading` strings occur literally after whitespace normalization, including each full footer fragment. C and H excerpts likewise match their packet witnesses after whitespace normalization, except R2-D27's intentional placeholders “not transcribed.”

Reporting gaps / qualifications:

- **R1** labels both body insertion cues transcribed although its reading has no explicit cue drawings. Its first-exponent medium uncertainty is present in inventory 12–13, but absent from both `differences` and `remaining_doubts`. Its added `\hfill` and omitted `\cotefile{123}` are not listed in `differences`.
- **R2** has no dedicated first-exponent difference entry; the inventory and reading consistently call it handwritten. The confirmed nonassertive-wrapper convention means this is not a substantive unreported C correction. The root union records the medium disagreement against H's explicit assertion. R2-D23 gives high confidence to the k/i overlay while `remaining_doubts` gives medium confidence to its unresolved chronology; these can describe different aspects and are not a contradictory glyph reading.
- **R3** consistently encodes its new footer e/a, denominator, hence and order doubts and both insertion curves. D11's comment location is the harmless exception above.
- **H-marking metadata — confirmed convention:** `marked_in_H` specifically tracks H's `\ill` / `\uncertain` marking, not `sic` or editorial comments. Therefore all three `stablity` entries correctly have `marked_in_H:false` despite H's `\note{sic}`; `h_changed:false` is also correct. The explicit H comments on both exponents, `of G-tilde`, `generating`, `distinguished`, and the lower center annotation do not require this flag to be true.

## Macro-only / implementation differences to separate from ink judgments

- R1 omits C's `\cotefile{123}`; R2/R3 retain it. All have `\scanpage{22}` and the archive-21 comment. The missing cote macro is metadata, not a missing source word.
- Different TikZ node names (`appeared` / `r` / `letters`, `automorph` / `k` / `letters`) are implementation only. Changed strokes, offsets, rotations, sizes and anchors are **not automatically** macro-only: they encode geometry that the root reviewer must assess.
- `\margin` versus H's `\marginal`, `\deleted` versus H's `\struck`, `\widetilde` versus `\tilde`, and ordinary roman math wrappers do not by themselves establish a new lexical reading. `\uline{distinguished}` and H's `\emph{distinguished}` with an explicit underline note carry the same underlying word; all readers retain C's underline convention.
- Do **not** collapse `\phi`/`\varphi`, underlined Z / `\mathbb{Z}`, the first 2's `\handwritten` wrapper, or local `\unsure` scopes as merely stylistic macros: those encode the reported shape, medium, or uncertainty distinctions.

## Authorized final spec / preview crosscheck

After the reader audit, root authorized inspection of `out/decisions/C123-02_123_scan022_spec.json` and `out/decisions/C123-02_123_scan022_preview.tex` only. No new image inspection occurred.

- **Union coverage passes:** the 32 final difference loci account for every locus in the split union table. Grouping the two extension cells, the hence/order uncertainties, and the medium/placement aspects of generating is explicit. Replacing R3 D29/D30 with separate annotation and lower-formula geometry entries preserves both their content and placement; the extra vertical trace and upper-right heading each receive their own entry.
- **Inventory coverage passes:** all 40 R3 inventory elements remain, with the separate vertical trace and archive foliation added, giving 42. Both body insertion leaders are actually drawn. The first 2 inventory leaves medium unresolved. The footer has its annotation/leader, lower-right formula, and two explicit `rotate=-3` nodes.
- **Doubt coverage passes:** all 12 C-question loci remain covered; the 13 final remaining-doubt entries retain the two distinct extension-cell doubts together, the narrowed `hen\unsure{ce} of ord\unsure{er}`, the second-denominator doubt, and the trace's ink/surface and function uncertainty. Narrowing the whole-word R3 doubts is an explicit root ink decision, not an accidental omission.
- **Text consistency passes:** the spec's replacement text exactly equals the preview, and its old-text match equals the complete R3 reading. The selected appeared and automorphisms graphics are R3's; both body insertion graphics remain intact. No mathematical normalization was introduced by this text merge.
- **Metadata/prose observations resolved by root:** the omitted `\cotefile{123}` is intentional normalized assembly metadata. After the checked snapshot, root confirmed that the regenerated spec notes now describe the C_questions contrast without attributing the article to H and state that this is not an actual C/H difference. Both supplied witnesses omit the article. No further audit action is needed at either item.

No reader, report, spec, or preview files were changed by this audit; only this audit file was written.

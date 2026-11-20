# Independent reader audit — scan 008, R2

**Status: complete. Actual enhanced crops: 15.** All 12 distinct C doubt loci have individual entries. S.json is empty. The complete page, including the two marginal notes, overwrites, insertion, brace, underlining and unfinished final sentence, is transcribed. Eight uncertainties remain explicitly represented; no text or mathematical symbol is left blank.

## Independence and authorized inputs

I read only this packet’s brief.md, inputs.json, C.tex, H.tex, C_context.md, S.json and notation.md, and the two directly referenced preambles. I used no OCR, text-recognition library, PDF extraction, web research, other page image, other reader output or consolidated decision. All written files are in this assigned R2 directory. No further reader was spawned.

## Image-view sequence

The clock was first registered at 09:40:58 UTC, immediately after reading the packet and preambles. The following images were actually emitted through the image tool, once each:

| Order | Image | UTC | Role |
|---:|---|---|---|
| 1 | J156-6-01_156-6_scan008.jpg | 2026-11-20T09:41:04Z | whole |
| 2 | J156-6-01_156-6_scan008_a.jpg | 2026-11-20T09:41:09Z | half_a |
| 3 | J156-6-01_156-6_scan008_b.jpg | 2026-11-20T09:41:29Z | half_b |
| 4 | 01_order_descriptor.jpg | 2026-11-20T09:43:03Z | crop |
| 5 | 02_upper_margin.jpg | 2026-11-20T09:43:03Z | crop |
| 6 | 03_lower_margin.jpg | 2026-11-20T09:43:04Z | crop |
| 7 | 04_first_relation.jpg | 2026-11-20T09:43:31Z | crop |
| 8 | 05_first_definition_subject.jpg | 2026-11-20T09:43:31Z | crop |
| 9 | 06_first_definition_endings.jpg | 2026-11-20T09:43:31Z | crop |
| 10 | 07_first_parenthesis_insertion.jpg | 2026-11-20T09:43:31Z | crop |
| 11 | 08_refinement_X.jpg | 2026-11-20T09:43:57Z | crop |
| 12 | 09_refinement_element.jpg | 2026-11-20T09:43:57Z | crop |
| 13 | 10_ombre_retracing.jpg | 2026-11-20T09:43:57Z | crop |
| 14 | 11_deux_revision.jpg | 2026-11-20T09:43:57Z | crop |
| 15 | 12_deleted_dans.jpg | 2026-11-20T09:44:39Z | crop |
| 16 | 13_meme_abbreviation.jpg | 2026-11-20T09:44:39Z | crop |
| 17 | 14_ie_punctuation.jpg | 2026-11-20T09:44:39Z | crop |
| 18 | 15_bottom_disjoint.jpg | 2026-11-20T09:44:39Z | crop |

The whole image was used for layout. Half A and then half B were read line by line against both drafts. Neither half was reopened or enlarged in its entirety. The crop phase began only after both halves had been read. Some narrow rectangular crops contain incidental fragments of adjacent lines; these were not used to reopen a settled locus.

## Loci still open after the halves

1. The word de/dans and the typographic alphabet of the family F in (1.10).
2. Full precise reading, initial case and punctuation of the upper oblique NB.
3. Full precise reading of the lower oblique NB, its initial G/C, and punctuation.
4. The underlying letters and old comparison in the heavily overwritten first relation.
5. The underlying letter in the first definition’s subject.
6. The two vertically adjacent overwritten F endpoints in the first definition and parenthesis.
7. The corrected operand and anchor/content of the =X insertion in the first parenthesis.
8. The small x/X in the refinement parenthesis.
9. élément versus élt.
10. Whether the dark internal stroke of ombre is retracing or a canceled/overwritten letter.
11. The canceled final glyph and live/deleted extent of deux.
12. The canceled word before entre.
13. The barred m versus an equality sign after d’une.
14. The dot pattern before {F,G}.
15. The presence or absence of final s in the bottom disjoint.

The curved lower rule of preccurlyeq, lowercase nb, spécifique, and the final dans of the bracket were already readable from half A. The body phrase sous figures without a hyphen was settled from half B. Their original-source coordinates are supplied in the report even though no crop was made for them.

## Crop record and pixel transforms

All crops use the original whole JPEG, 1682 × 2361 pixels. Boxes are (left, top, right, bottom) in that original source. Every crop received Pillow autocontrast, UnsharpMask(radius=1.3, percent=140, threshold=2), LANCZOS enlargement to 3000 pixels wide, and JPEG output at quality 95 with subsampling 0. Rotations used BICUBIC with expansion and white fill. No crop was remade, recompressed, or emitted twice.

| Crop | Original box | Rotation | Output pixels | Why needed and result |
|---|---|---:|---|---|
| 01_order_descriptor.jpg | (1060, 145, 1555, 285) | 0° | 3000 × 848 | de/dans remains unresolved: closed d and low compressed tail; F is clear, alphabet not uniquely determined. |
| 02_upper_margin.jpg | (18, 475, 265, 1020) | -50° | 3000 × 2813 | Entire note read upright. Terminal period is present; initial l/L case remains uncertain. |
| 03_lower_margin.jpg | (18, 805, 450, 1515) | -50° | 3000 × 2876 | Entire note read upright. The flat lower return/downward terminal supports G; a colon follows the last F of the implication. |
| 04_first_relation.jpg | (485, 755, 715, 880) | 0° | 3000 × 1630 | Old F inside G and old G behind F are visible. The old comparison remains < or ≪ under the final ≤. |
| 05_first_definition_subject.jpg | (815, 750, 1050, 862) | 0° | 3000 × 1430 | Older F’s upright and arms are distinct inside the later G. |
| 06_first_definition_endings.jpg | (1435, 825, 1670, 995) | 0° | 3000 × 2170 | Both endpoints preserve old G curves under live F. These adjacent endpoint edits form one narrow vertical locus. |
| 07_first_parenthesis_insertion.jpg | (790, 845, 1130, 993) | 0° | 3000 × 1306 | Old F is inside live G. Only =X is above the line, anchored immediately after G. Capital Si is clear. |
| 08_refinement_X.jpg | (805, 1070, 1140, 1160) | 0° | 3000 × 806 | Small crossed diagonals favour x, but X remains possible. |
| 09_refinement_element.jpg | (1315, 1060, 1640, 1160) | 0° | 3000 × 923 | Two accents and a medial run establish full élément. |
| 10_ombre_retracing.jpg | (1300, 1145, 1535, 1230) | 0° | 3000 × 1085 | A dark m-shaped run contains a small oval, without a separate canceling slash. Retracing is first candidate; overwritten o/m remains possible. |
| 11_deux_revision.jpg | (755, 1525, 1000, 1645) | 0° | 3000 × 1469 | Separate live x follows a crossed loop-and-descender glyph. q is visually favoured over x; deu is retained live. |
| 12_deleted_dans.jpg | (710, 1640, 1125, 1760) | 0° | 3000 × 867 | Initial d, medial remnants and terminal s support deleted dans. |
| 13_meme_abbreviation.jpg | (470, 2190, 810, 2280) | 0° | 3000 × 794 | Curved lower letter beneath a straight upper bar establishes the barred verbal m. |
| 14_ie_punctuation.jpg | (835, 2180, 1010, 2265) | 0° | 3000 × 1457 | Two low intervening marks are visible, the second elongated; retain i..e/i.e, without final point. |
| 15_bottom_disjoint.jpg | (485, 2250, 835, 2345) | 0° | 3000 × 814 | Terminal t is followed by blank space and colon; no s is present. |

Complete crop source paths, original and rotated sizes, output sizes and output paths are also recorded in crop_manifest.json.

## Line-by-line comparison

| Page position / line group | Reading and comparison with C and H |
|---|---|
| Top page number | 7, in his hand; both witnesses agree. No archive pencil number is visible. |
| (1.10), signs and label | Label (1.10)., then ≤, ≪, preccurlyeq. The curved lower rule resolves C’s preceq alternative; H’s descriptive note is credited. |
| (1.10), descriptor | relations d’ordre followed on a second line by de/dans and family F. C reads de; H reads dans. The crop leaves the word ambiguous, with de first. The calligraphic/fraktur font difference is kept as actual alphabet uncertainty, not disguised as macro equivalence. |
| et les relations … and (1.11) | Both drafts’ words, M and the two signs are confirmed. The exact (1.11) label has no following period. |
| First slanted NB | The full orders-on-L statement is present. C’s lower-case les and H’s Les cannot be distinguished securely; terminal period agrees with H and is missing from C. |
| Square bracket, first line | nb la relation d’ordre preccurlyeq induite dans M. C’s lowercase nb is resolved; H’s local et is replaced by nb. |
| Square bracket, second and third lines | est moins importante, comme structure spécifique dans M]. Both words that H doubts or leaves ill are readable. C’s text is confirmed. |
| Second slanted NB | NB G ≤ F ⇒ G ≪ F : une sous-figure de F raffine F. G/C is resolved to G from the lower-terminal shape. H’s colon is present; C omits it. |
| First relation at left | Live G ≤ F agrees with both; C’s overwritten F and G states are visible and omitted by H. The former comparison remains uncertain. |
| First definition, first two body lines | G est dit une sous-figure de F. The underlines beneath sous and figure are real. Both operands have the old opposite letters underneath, agreeing with C’s physical-state account and absent from H. |
| First parenthesis | Capital Si; corrected G from F; only =X inserted above after G; ∈ M, c’est donc une strate de F. Strate is underlined. Final F is over G. H’s intervention is not ignored, but its old G and whole G=X insertion are incorrect. |
| Refinement relation and definition | G ≪ F; G est dit un raffinement de F. Raffinement is underlined. Both drafts agree on the live text. |
| Refinement parenthesis, first line | si G = x/X ∈ M, c’est donc un élément. Small x/X remains uncertain as C marks it; H’s certainty is not followed. Full élément is established by the two accent marks. |
| Refinement parenthesis, second line | de la grande ombre de F). The dark internal letter is preserved with physical-state alternatives. C’s definite deleted o/m is not established; H’s plain unqualified word omits the doubt. |
| Subdivision relation and definition | G preccurlyeq F; G est dit une subdivision de F, on dit que la figure G subdivise la figure F. The underlining and final period are present. Both drafts’ live text is confirmed. |
| Je note enfin … | deu plus canceled q/x plus separate live x; autres relations importantes. C correctly retains the live word but its old x is not secure. H’s whole-word strike loses the live x and overstates the deletion. |
| … entre figures | deleted dans, then live entre figures:. The crop resolves C’s canceled-word doubt; H’s reading is confirmed. |
| (1.12) | Left brace, F et G compatibles and F et G disjoints, both predicate words underlined, trailing comma. Both drafts represent the words and signs correctly. |
| qui l’une et l’autre … | Both following prose lines agree: peuvent s’exprimer en termes de la relation d’ordre ≤:. No missing word, exponent, or sign detected. |
| Compatibility characterization, first line | F et G compatibles: ce sont des sous figures … . The space between sous and figures is present; H supplies an uninked hyphen. |
| Compatibility characterization, second line | d’une barred-m figure, i..e/i.e {F,G} majoré pour ≤;. C’s barred-m alternative is resolved, while H expands it to même. The dot pattern remains ambiguous and no final point follows e. Set braces, comma and semicolon are present. |
| Bottom fragment | F et G disjoint: F et G compatibles, et leur. The t ends before the colon with no s. C’s doubt is resolved to singular; H’s plural is not inked. No continuation is supplied. |

## Content and mathematical-check limits

The page names the three orders and their induced relations, adds the two marginal observations, defines subfigure/refinement/subdivision, and introduces compatibility and disjointness via ≤. It characterizes compatibility by a common majorant and stops mid-sentence in the disjointness characterization. The bracketed assessment that the third relation is “moins importante, comme structure spécifique dans M” is preserved. There is no explicit authorial request to check a proof or resolve a doubt.

I followed the formulas and the relation between the prose and symbols to locate transcription risks. I did not verify the underlying order-theoretic claims, reconstruct earlier definitions, prove the implication, or complete the interrupted sentence. Check events are therefore recorded only as authorial assertions carried as background, with an explicit statement that no mathematical verification was performed. Pure visual choices are not counted as proof checks.

## Remaining limitations

Exactly one enhanced view was made for each of the 15 open loci above. At that depth, eight uncertainties remain: de/dans; family F alphabet; les/Les; old comparison; x/X; internal ombre state; old q/x in deux; and the i..e/i.e dot pattern. They are retained in reading.tex and report.json. No further crop or repeat view was used to force a resolution.

Final file validation checked JSON parsing, mandatory report fields, all 12 C-doubt entries, the empty S array, 15 crop view-log entries, all required confidence values and the presence of the complete transcription. The inventory and unresolved list were complete before status was set to complete.

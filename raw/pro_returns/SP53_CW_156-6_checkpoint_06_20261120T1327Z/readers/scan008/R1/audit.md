# Scan 008 — independent reader R1 audit

## Scope and actual image use

I read the full brief first, then the assigned inputs, both complete witness pages, C's doubt context, the empty S list, the notation table, and the two supplied preambles. I did not read another reader's output, any other scan, or a main adjudication. No OCR, recognition library, text extraction, external research, or published transcription was used.

The whole image was emitted once at 09:40:57 UTC for layout. Half a was emitted once at 09:41:00 UTC and half b once at 09:41:20 UTC. They were read in that order against C and H. Every later image emission was one of the 15 new enhanced crops below. None was emitted twice. The view timestamps in report.json are clock readings immediately after the relevant image or batch; all images in a subsecond batch share that recorded second.

The page is a manuscript text sheet in the author's hand, numbered 7. It contains three numbered displays, a three-row aligned set of definitions, two oblique left marginal NB notes, overwritten variables, one above-line insertion, local word corrections, and prose ending with an unfinished sentence. There is no pictorial drawing or arrow diagram. The definitions are typeset as a tabular alignment, not as an invented diagram. C's use of a diagram wrapper for that table is a layout choice and is not counted as a witness discrepancy.

## Open loci after the two halves

The halves left the following loci for a single deeper crop: the third comparison; de/dans and the family F alphabet; the complete upper oblique note; the complete lower oblique note including its first G/C and punctuation; the first formula's overwritten operands and comparison; the first definition's corrected prose variables; the first parenthesis's old variables and inserted =X; x/X in the second parenthesis; élément/élt; the dark writing within ombre; the correction in deux; the canceled preposition before entre; the barred m/equality candidate; the dots in i..e; and the final singular/plural disjoint(s).

The low nb at the bracket opening, spécifique, the following dans, the punctuation of label (1.10)., the large initial S in the second parenthesis, and the absence of a hyphen in the bottom sous figures were settled from the halves. Their original-image coordinates are supplied in report.json, with crop=null. They were not cropped again merely to manufacture evidence.

## Crop transforms and purposes

All crop boxes are from the original whole image, 1682 × 2361 pixels, `/workspace/scratch/42e661864e98/source/SP53_CW_156-6_scans/J156-6-01_156-6_scan008.jpg`. Each box was extracted once with Pillow. Oblique notes alone were rotated clockwise (negative Pillow rotation), with BICUBIC resampling and a white expanded canvas. Each crop received autocontrast, LANCZOS enlargement to 3000 pixels across, and UnsharpMask(radius=1.2, percent=145, threshold=3). Each was saved once as JPEG quality 95 with no chroma subsampling. No already-made evidence was recompressed.

| Crop | Original box (left, top, right, bottom) | Rotation | Output pixels | Purpose |
| --- | --- | --- | --- | --- |
| 01_third_relation.jpg | (840, 145, 990, 240) | 0° | 3000 × 1900 | Curvature and stroke count of the third relation in (1.10). |
| 02_top_dans_family_F.jpg | (1070, 150, 1580, 285) | 0° | 3000 × 794 | Reading de/dans and the alphabet of the family F. |
| 03_upper_margin.jpg | (22, 480, 278, 1010) | -53° | 3000 × 2720 | Read the oblique upper NB note including its punctuation and relation symbols. |
| 04_lower_margin.jpg | (24, 835, 430, 1525) | -55° | 3000 × 2738 | Read the oblique lower NB note, first G/C, arrow, hyphen, and line order. |
| 05_first_relation_overwriting.jpg | (485, 765, 710, 875) | 0° | 3000 × 1467 | Identify underlying operands and comparison below the live G <= F. |
| 06_subfigure_row_corrections.jpg | (825, 760, 1660, 915) | 0° | 3000 × 557 | Identify overwritten G/F states in the first definition and exact underlines. |
| 07_strate_parenthesis.jpg | (790, 855, 1665, 990) | 0° | 3000 × 463 | Identify operand corrections, inserted =X and terminal F in the first parenthesis. |
| 08_refinement_X.jpg | (875, 1080, 1125, 1167) | 0° | 3000 × 1044 | Distinguish lowercase x from uppercase X after G=. |
| 09_element_word.jpg | (1320, 1070, 1655, 1168) | 0° | 3000 × 878 | Distinguish fully written element from abbreviated elt. |
| 10_ombre_correction.jpg | (1305, 1155, 1530, 1240) | 0° | 3000 × 1133 | Identify the physically dark corrected portion within ombre. |
| 11_deux_correction.jpg | (770, 1535, 980, 1635) | 0° | 3000 × 1429 | Separate live and crossed strokes in deux. |
| 12_deleted_dans.jpg | (705, 1660, 905, 1760) | 0° | 3000 × 1500 | Read the crossed word before entre figures. |
| 13_barred_m.jpg | (480, 2195, 660, 2280) | 0° | 3000 × 1417 | Distinguish barred m from an equality sign after d une. |
| 14_ie_points.jpg | (835, 2185, 990, 2270) | 0° | 3000 × 1645 | Read the number and position of dots in the i.e. abbreviation. |
| 15_bottom_disjoint.jpg | (510, 2255, 790, 2345) | 0° | 3000 × 964 | Check whether the bottom occurrence has a final s. |

The emitted crop sequence was 01–03 at 09:42:32, 04–06 at 09:42:59, 07–10 at 09:43:23, and 11–15 at 09:44:01 UTC. This is **15 actual crops**, plus one whole and two half views, for **18 actual image emissions**.

## Decisive strokes and remaining limits

1. The third sign has both a curved cusp and a distinctly curved lower rule. This resolves C's straight/curly lower-rule doubt to `\preccurlyeq`.
2. The top word has d followed by compressed low strokes and a final hook. I favor dans but retain de as an alternative. The F letter is secure; the calligraphic/fraktur distinction is not. Its long top arm and returned foot are recorded rather than silently assigning H's or C's font.
3. The upper note reads “NB les relations d'ordre induites par <=, << sur L sont discrètes”. The NB has one underline. The initial l is read as lowercase. There is no terminal period visible after the last word.
4. The lower note reads “NB G<=F => G<<F. une sous-figure de F raffine F”. The G's angular terminal agrees with other G forms on this page, resolving the first-operand doubt. A single point, not a colon, follows the displayed implication. The arrow is double-shafted and directed right. The note's line order and hyphen are preserved.
5. The first formula has a clear earlier F under G and an earlier G under F. An additional angle is visible behind the live <=, but the older comparison remains `<`/`<<` uncertain.
6. The first definition's prose also has F changed to G and G changed to F. The two separate underlines under sous and figure and the intervening hyphen are visible. H's plain live variables omit the old ink.
7. The first parenthesis has old F beneath G, above-line `=X` alone with an insertion stroke leading after G, and old G beneath the terminal F. H records a correction but misidentifies its old letter and treats G=X as the insertion span. Its initial Si is capitalized.
8. The next crossed variable is small, with a curved/looped left stroke, favoring x. X remains a real visual alternative and is retained.
9. The word after un has the initial accented e, a high l, a second small accent, and additional low strokes before the terminal t. I resolve it to élément, with medium confidence; no abbreviated élt is silently expanded.
10. The m-region of ombre is dark and contains a small oval, but no independent cancellation stroke establishes the sequence asserted by C. The first reading is a retraced live m; old o overwritten by m remains the alternative. Both the letter and its deletion state are thus represented as uncertain in place.
11. The separate final x of deux is clear. The preceding crowded corrected character remains tentatively x. The d/e/u connections are read as live; H's deletion of the entire word and omission of the separate terminal x are not followed. The extent and old terminal letter are documented cautiously, not treated as a certain full-word strike.
12. The crossed preposition retains the initial d and terminal hook, with middle remnants. It supports dans, while the horizontal cancellation is clear.
13. The abbreviation after d'une has a curved lower trough/hump below a separate straight overbar. It is a barred verbal m, not an equality sign. The probable expansion même is confined to the abbreviation list.
14. The i has its own high dot, then two distinct low marks occur before the e. There is no final dot. I preserve literal i..e, rather than H's standardized i.e.
15. The bottom adjective ends at t immediately before the colon. No s is present. Literal disjoint is retained even though the earlier display has disjoints.

## Line-by-line comparison coverage

- **Header and (1.10):** author number 7, comparison list, commas, “relations d'ordre”, the next-line preposition/family letter, label, and the label's final point were read. C's sign doubt is resolved; H misses the point; the preposition and alphabet remain explicitly uncertain.
- **Connecting prose and (1.11):** “et les relations induites dans M” and the <=, << display with its M and label agree in substance with both witnesses. All tokens were read; no mathematical inference was needed.
- **Bracket paragraph:** nb differs from H's et; C's case doubt is resolved to nb. The remaining full sentence was compared word by word. H's uncertain spécifique and illegible word before M are readable. The brackets, comma and terminal point are included.
- **Both marginal notes:** each complete oblique inscription was read after rotation. Upper/lower case, underlined NB, relation signs, the implication's direction, the lower note's period, and hyphenated sous-figure were compared with both witnesses. H's upper-note period and lower-note colon are not supported.
- **First definition and parenthesis:** every live and old variable, comparison, insertion, explanatory word, parenthesis, underline and hyphen was compared. H's omissions/misidentifications of old ink are reported individually; C's unresolved old-comparison candidate remains open. There is no arrow diagram in this block.
- **Second definition and parenthesis:** the live G<<F row and underlined raffinement agree. The initial Si, x/X, élément, ombre correction, and final F/closing parenthesis were inspected. Both witnesses use lowercase si; the manuscript's larger S is preserved. The x/X and ombre state are not normalized.
- **Third definition:** G preccurlyeq F, underlined subdivision, comma, and “on dit que la figure G subdivise la figure F.” were read across the half boundary. Both witnesses agree substantially. The period is present.
- **“Je note enfin” paragraph:** the live introductory wording, the local correction in deux, importantes, canceled dans, entre figures and colon were compared. H's entire-word strike is not adopted; the old end-character remains uncertain. C's doubt on dans is resolved.
- **(1.12):** left brace, both F et G rows, the separate underlines of compatibles/disjoints, display label and final comma were verified. Both witnesses agree substantially.
- **Following prose:** the two lines “qui l'une et l'autre peuvent s'exprimer en termes de la relation d'ordre <=:” were read without a substantive discrepancy.
- **Compatibility definition:** “F et G compatibles: ce sont des sous figures d'une ... figure, ... {F,G} majoré pour <=;” was read in full. The absence of the hyphen, literal barred abbreviation, exact i..e punctuation, braces, set comma, acute accent of majoré, and semicolon are retained.
- **Final line:** “F et G disjoint: F et G compatibles, et leur” is complete for the page. The singular adjective is visually resolved; no continuation from another page was consulted or supplied.

## Mathematical reading and checking

The page names orders, introduces the vocabulary sous-figure/raffinement/subdivision, states the two marginal observations, and begins the compatibility/disjointness definitions. There is no computation, proof, authorial question, or explicit instruction to verify a claim on this page. The NB passages are remarks, not claimed proof checks. The bracketed phrase says the third induced relation is “moins importante, comme structure spécifique dans M”; it is preserved as prose, not recast as a mathematical defect.

I performed visual transcription and local parsing. I did not prove the marginal implication or discreteness assertion, reconstruct prior definitions, or infer the missing end of the disjointness sentence. The check_events therefore use only “carried as background without fault found”, with outcomes explicitly saying no mathematical verification was performed.

## Completeness and limitations

All 12 unique C doubt loci are individually accounted for. The supplied S.json is empty, so the S audit has zero rows. The complete inventory contains 32 entries covering the whole sheet, both margins, each display/text block, the physical corrections and the insertion. Every entry is included in reading.tex; six unresolved loci remain explicitly represented and explained in report.json. No physically unreadable word was replaced with an invented reading or with an unnecessary illegible marker.

The main limits are the deliberately one-view/one-crop protocol and the heavy overlap of old and new ink. Enlargement cannot recover strokes under an overwrite. The uncertainty retained in the top preposition, F alphabet, earlier comparison, x/X, ombre state and earlier end-character of deux reflects those limits. This is a complete independent page return, not a sample and not an adjudication of the other readers.

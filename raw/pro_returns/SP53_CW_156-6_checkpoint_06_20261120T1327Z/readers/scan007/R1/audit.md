# Scan 007 — independent reader R1 audit

## Scope and method

Read only the assigned scan 007 packet: brief.md, inputs.json, C.tex, H.tex, C_context.md, S.json, notation.md, the referenced exact PREAMBLE.tex, and the referenced H preamble for witness-macro interpretation. No other page, other reader, consolidated decision, OCR, recognition library, PDF text extraction, external source, or proof source was consulted. S.json is empty, hence there are no S rows to adjudicate.

The complete whole image was emitted once for layout. The supplied first half and then second half were each emitted once and read in order against both witnesses. Neither half was re-viewed or enlarged wholesale. Twelve tight crops were subsequently made, each emitted once. All 15 images in the view log were actually emitted through `image((await tools.view_image({path: ...})).image_url)`.

The page has the manuscript number 6, a main paragraph running over 20 body lines, and a two-line unfinished paragraph beginning with a live section sign. There are no displays, diagrams, drawings, independent marginal notes, or separately visible archive pencil numbering. The term lieux “de la figure” has one underline, continuing on its next written line. The manuscript is entirely handwritten.

## Actual image-view sequence

| Sequence | Role | Image | UTC |
|---|---|---|---|
| 1 | whole | J156-6-01_156-6_scan007.jpg | 2026-11-20T09:22:28Z |
| 2 | half_a | J156-6-01_156-6_scan007_a.jpg | 2026-11-20T09:22:32Z |
| 3 | half_b | J156-6-01_156-6_scan007_b.jpg | 2026-11-20T09:22:51Z |
| 4 | crop | 01_multiombre_start.jpg | 2026-11-20T09:24:07Z |
| 5 | crop | 02_forme_ending.jpg | 2026-11-20T09:24:07Z |
| 6 | crop | 03_inclusion_overwrite.jpg | 2026-11-20T09:24:07Z |
| 7 | crop | 04_incidences_ending.jpg | 2026-11-20T09:24:44Z |
| 8 | crop | 05_relation_de_F.jpg | 2026-11-20T09:24:44Z |
| 9 | crop | 06_leq_de_M.jpg | 2026-11-20T09:24:44Z |
| 10 | crop | 07_ca_revient.jpg | 2026-11-20T09:25:21Z |
| 11 | crop | 08_au_barred_m.jpg | 2026-11-20T09:25:21Z |
| 12 | crop | 09_souvent_start.jpg | 2026-11-20T09:25:21Z |
| 13 | crop | 10_ateliers_start.jpg | 2026-11-20T09:26:10Z |
| 14 | crop | 11_a_partir_overwrite.jpg | 2026-11-20T09:26:10Z |
| 15 | crop | 12_section_mark.jpg | 2026-11-20T09:26:10Z |

## Loci left open after the two half views

The following were still open when the half views ended; they account for all twelve crops, in page order. The two doubts in the overwritten inclusion cluster share one physical locus and one crop. C’s doubt about pourtant was already settled by half b and was not cropped.

1. The darkened opening of multiombre: earlier om versus retracing the live beginning; deletion state also uncertain.
2. The final letters of formé/formée.
3. The overwritten relation wording: canceled d’ordre/d’inclu and the beginning of the replacement inclusion.
4. The terminal number of incidence(s).
5. The short preposition before the second tilde F: de/dans.
6. The short preposition between ≤ and M: de/dans; the adjacent small order sign and M were included as context.
7. The first word of ça revient, including its cedilla and H’s rival phrase se réduisant.
8. The barred mark after au: barred m/equality sign.
9. The overwritten initial of souvent and H’s competing reading of its live continuation.
10. The doubled initial A of Ateliers and possible underlying a.
11. The overwritten preposition before partir: old de versus H’s old à.
12. The initial section sign/S and H’s assertion that it is struck out.

The parenthetical warning, déployement, the two reflexive réconstitue clauses, the abbreviation ie., the word pourtant, and both pairs of literal double quotation marks were settled from the halves. Their report entries give original-source crop coordinates even where no new crop was necessary. H’s note about the page number correctly records the manuscript number and is credited, not treated as manuscript prose. H’s emphasis versus C’s underline is a representation difference and has no separate collation row. The literal quotation-mark glyphs are recorded separately because paired short strokes differ from guillemets.

## Crop production and evidence

All crops came from `/workspace/scratch/42e661864e98/source/SP53_CW_156-6_scans/J156-6-01_156-6_scan007.jpg` (1682 × 2360 pixels). Boxes below use that original image’s coordinates `[left, top, right, bottom]`. No crop was remade, recompressed, or re-viewed. There were **12 actual crops**.

The same transform was used on each: tight Pillow crop; rotation 0°; RGB autocontrast with cutoff 0; enlargement by LANCZOS to the dimensions below; UnsharpMask radius 1.2, percent 120, threshold 3; JPEG quality 95 with subsampling 0. This reveals source strokes without attempting recognition or reconstructing lost pixels.

| Crop | Original box | Output pixels | Reason and decisive strokes |
|---|---|---|---|
| 01_multiombre_start.jpg | [420, 585, 820, 690] | 3000 × 788 | Two low superposed runs precede clean l/t. They permit old om but do not establish cancellation over retracing; both states retained. |
| 02_forme_ending.jpg | [1115, 565, 1355, 666] | 2880 × 1212 | Accent above a flattened final run; no independently separated extra e. formé first, formée retained. |
| 03_inclusion_overwrite.jpg | [1080, 876, 1438, 956] | 3000 × 670 | Second d/apostrophe and heavy underlying run remain, with a legible live sion suffix. Both canceled wording and live initial letters remain doubtful. |
| 04_incidences_ending.jpg | [655, 1104, 1100, 1200] | 3000 × 647 | Detached terminal run and downward return favour a plural s, but compressed ce/ces remain unresolved. |
| 05_relation_de_F.jpg | [1015, 1172, 1282, 1288] | 3000 × 1303 | Looped d followed by one low e-like tail. Resolved de; separate wave above F confirms tilde. |
| 06_leq_de_M.jpg | [433, 1328, 759, 1426] | 3000 × 902 | Separate d plus shallow e-like cup/return. Resolved de; ≤ has a distinct lower stroke, and M is two-peaked. |
| 07_ca_revient.jpg | [265, 1449, 612, 1545] | 3000 × 830 | Open c with a descending returning cedilla and low a; verb ends in a clear crossed t. Resolved ça revient. |
| 08_au_barred_m.jpg | [639, 1439, 952, 1526] | 3000 × 834 | Straight upper bar above a lower bowl, internal rise and long tail. Resolved barred verbal m, not equality. |
| 09_souvent_start.jpg | [1099, 1738, 1399, 1834] | 3000 × 960 | Live ouvent is readable, but the initial has multiple crossed strokes, a rounded base and upright. souvent is secure; old à/d remains open. |
| 10_ateliers_start.jpg | [449, 1861, 735, 1966] | 3000 × 1101 | Small lower loop and doubled uprights beneath the capital A. Possible old a versus retraced A remains open. |
| 11_a_partir_overwrite.jpg | [1220, 1836, 1490, 1941] | 3000 × 1167 | Old tall d-like stem and small right-hand e-loop remain beside the new rounded a and grave. Resolved de→à. |
| 12_section_mark.jpg | [325, 2167, 479, 2258] | 2772 × 1638 | Two linked returns and long lower exit; no independent strike-through. Resolved live section sign. |

The complete pixel-transform manifest is in crop_manifest.json. Evidence paths in report.json are relative to out/ and point to `readers/scan007/R1/crops/`.

## Line-by-line comparison ledger

Line numbers below count written body lines, not the manuscript header. The comparisons were made during the ordered half views; the crop conclusions above then refine only the listed open loci.

| Written line(s) | Literal content or objects checked | Comparison and decision |
|---|---|---|
| Header | 6 | Clear, in the author’s hand. Both witnesses agree, and H’s descriptive page-number note is correct. |
| 1–2 | Ainsi, l’ombre d’une figure est formée / des lieux qui la raffinent -- on dit | Both witnesses agree on the live words. Initial formée, accents, comma after Ainsi, and dash were read. |
| 3 | aussi que ce sont les lieux “de la | Live words agree. Single underline and paired upper quotation strokes read; H’s guillemet shape differs. |
| 4–5 | figure” (à ne pas confondre, avec les / strates de la figure qui sont des lieux). | C agrees with the ink. H’s ill/un peu/abusivement/ou are locally replaced by à/ne pas/confondre/avec. Underline, closing quote, comma, parentheses and final stop checked. |
| 6 | La multiombre est donc formé/formée des | Live multiombre, est donc and des agree. Earlier om versus retracing remains open; final e of formée remains open. |
| 7 | ombres de ses strates, elle est indexée | Both witnesses agree. Comma and indexée accent checked; the line-end division of indexée is joined in the prose transcription. |
| 8 | par le déployement tilde F, ensemble des | C’s y spelling is supported by the descender; H’s déploiement modernizes it. Wave over F and comma checked. |
| 9 | strates de F, la relation d’[overwritten wording] de la | The canceled wording and replacement inclusion require crop 03. All surrounding words, apostrophe, F and comma agree. |
| 10 | figure ensembliste n’étant autre que | Both witnesses agree. No extra word or note is present. |
| 11 | la relation d’incidence(s) entre strates | C’s plural/singular doubt survives crop 04; H is certain singular. Other words agree. |
| 12 | de F, ie. la relation de tilde F induite | ie. has one final stop, unlike H’s i.e. The short preposition was resolved de by crop 05; both ordinary and tilde F checked. |
| 13 | par ≤ de M (ou par ≪ au choix, | Signs ≤ and ≪, cursive M, parenthesis and comma read. Crop 06 resolves de against H’s dans and removes C’s doubt. |
| 14 | ça revient au barred m). Alors qu’une | Crops 07–08 resolve ça revient and barred m. H’s se réduisant and = differ. Closing parenthesis and period checked. |
| 15 | figure ne se réconstitue pratiquement | C agrees. H’s n’est reconstituable is contradicted by the separate reflexive se and short tue ending. |
| 16 | jamais à partir de son ombre, elle | Both witnesses agree; à accent, comma and elle checked. |
| 17 | se réconstitue pourtant [overwritten s]ouvent (cas | C’s reflexive verb agrees, unlike H’s est reconstituable. pourtant is readable in the half and C’s doubt is removed. Crop 09 establishes souvent and preserves low-confidence old à/d; H’s canceled donc/live dans is not supported. |
| 18 | des “Ateliers ensemblistes”) [de→à] partir | Name and continuation agree. Crop 10 retains uncertainty about old a versus retraced A. Crop 11 resolves the earlier preposition as de, with live à; H’s canceled à differs. Literal double quotation strokes checked. |
| 19–20 | de sa multiombre. Nous y / reviendrons. | Both witnesses agree. Capital N, full word reviendrons and both periods checked. No appended mark or margin note. |
| 21–22 | § Il y a lieu de parler des / relations d’ordre canoniques | Final words agree and there is no terminal full stop. Crop 12 resolves a live section sign, against C’s S alternative and H’s deletion state. |

## Mathematical reading and actual check scope

The page identifies the shadow with the refining places, and the multi-shadow with the family of shadows of strata indexed by tilde F. It identifies the inclusion relation with the strata-incidence relation induced from ≤ on M, and asserts equivalence with the relation induced from ≪. It contrasts reconstruction from an ordinary shadow with reconstruction from a multi-shadow in “Ateliers ensemblistes”, then introduces canonical order relations.

The two order signs were read literally; the sign after au was not silently replaced by a mathematical equals sign. The spelling déployement and the incidence(s) uncertainty are preserved. The de readings describe the written words, without an editorial conversion to dans. “ça revient au barred m” is an assertion of equivalence, not an authorial doubt. “Nous y reviendrons.” promises later discussion. There is no explicit doubt/check instruction such as “à vérifier”.

No mathematical proof check, independent re-proof, formal certificate, or computation was performed. The four check_events are explicitly categorized as background carried without fault found, each with outcome “read as the author’s assertion; no mathematical verification performed”. The isolated page supplies insufficient definitions for an independent proof of the asserted induced-relation equivalence or reconstruction property.

## Completion and limits

reading.tex contains the complete page, including every live text block, the underline, all recognized correction loci, and all seven retained uncertainties. report.json has 21 substantive collation entries, all 14 C doubt loci, an empty S array, 20 inventory entries, notation and abbreviation notes, and a complete unresolved array. Two collation rows solely concern literal quotation-mark shape, not underline/emphasis macro choice. All marked_in_H values refer only to actual ill/uncertain doubt markers at that local locus; neither struck nor add alone is counted as a doubt.

The main remaining limitation is the physical superposition of older letters and live writing. In multiombre and Ateliers even the existence of a separate canceled character remains uncertain, so the alternatives in reading.tex explicitly preserve cancellation-versus-retracing. No extra older word was inferred from semantics, and no ambiguity was resolved by the mathematical context alone. Nothing outside this one page has been read.

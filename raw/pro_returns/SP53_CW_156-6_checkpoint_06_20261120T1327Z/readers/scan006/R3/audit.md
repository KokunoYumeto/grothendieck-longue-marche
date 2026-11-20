# Scan 006 — independent reader R3 audit

## Scope and method

I read only the assigned scan 006 packet (`brief.md`, `inputs.json`, `C.tex`, `H.tex`, `C_context.md`, `S.json`, `notation.md`) and the exact referenced preamble, `/workspace/scratch/42e661864e98/out/PREAMBLE.tex`. I did not consult another reader, any other page image, any consolidated decision, OCR, a text-recognition library, PDF text extraction, external research, or a published transcription. S.json is an empty array. The notation table contains no adjudicated glyphs.

The whole image was emitted once for layout, followed by half A once and half B once for the line-by-line reading. The whole is 1683 × 2361 pixels; half A is 1683 × 1260; half B is 1683 × 1261 and corresponds to whole-image y = 1100 onward. All report boxes use the original whole-image coordinates. Metadata inspection did not perform text recognition.

**Actual targeted crops: 15. Actual image emissions: 18 (one whole, two supplied halves, fifteen crops).** No source image, supplied half, or saved crop was emitted twice. Each open focal area received one crop. Crops can contain adjoining lines as context; for example, crop 05 incidentally includes part of the replacement word below its target, while crop 06 supplies that word’s sole focused enlargement.

All files written by this reader are confined to `/workspace/scratch/42e661864e98/out/readers/scan006/R3/`.

## Image-view sequence

The UTC times below are recorded at the corresponding image-emission calls; crops emitted within one call share its timestamp. The first recorded start time follows the preliminary packet reads.

| UTC | Role | Image |
|---|---|---|
| 2026-11-20T08:58:48Z | whole | `/workspace/scratch/42e661864e98/source/SP53_CW_156-6_scans/J156-6-01_156-6_scan006.jpg` |
| 2026-11-20T08:58:57Z | half_a | `/workspace/scratch/42e661864e98/source/SP53_CW_156-6_scans/J156-6-01_156-6_scan006_a.jpg` |
| 2026-11-20T09:00:53Z | half_b | `/workspace/scratch/42e661864e98/source/SP53_CW_156-6_scans/J156-6-01_156-6_scan006_b.jpg` |
| 2026-11-20T09:04:55Z | crop | `/workspace/scratch/42e661864e98/out/readers/scan006/R3/crops/01_opening_deletion.png` |
| 2026-11-20T09:04:55Z | crop | `/workspace/scratch/42e661864e98/out/readers/scan006/R3/crops/02_multomb_edit.png` |
| 2026-11-20T09:04:55Z | crop | `/workspace/scratch/42e661864e98/out/readers/scan006/R3/crops/03_figure_F_glyph.png` |
| 2026-11-20T09:04:55Z | crop | `/workspace/scratch/42e661864e98/out/readers/scan006/R3/crops/04_fidelement_accent.png` |
| 2026-11-20T09:05:56Z | crop | `/workspace/scratch/42e661864e98/out/readers/scan006/R3/crops/05_jusqua_present.png` |
| 2026-11-20T09:05:56Z | crop | `/workspace/scratch/42e661864e98/out/readers/scan006/R3/crops/06_now_abbreviation.png` |
| 2026-11-20T09:05:56Z | crop | `/workspace/scratch/42e661864e98/out/readers/scan006/R3/crops/07_power_alphabet.png` |
| 2026-11-20T09:05:56Z | crop | `/workspace/scratch/42e661864e98/out/readers/scan006/R3/crops/08_fig_arrow.png` |
| 2026-11-20T09:07:12Z | crop | `/workspace/scratch/42e661864e98/out/readers/scan006/R3/crops/09_trouve_ending.png` |
| 2026-11-20T09:07:12Z | crop | `/workspace/scratch/42e661864e98/out/readers/scan006/R3/crops/10_first_mapping_arrow.png` |
| 2026-11-20T09:07:12Z | crop | `/workspace/scratch/42e661864e98/out/readers/scan006/R3/crops/11_multomb_retracing.png` |
| 2026-11-20T09:07:12Z | crop | `/workspace/scratch/42e661864e98/out/readers/scan006/R3/crops/12_after_etre_mark.png` |
| 2026-11-20T09:08:50Z | crop | `/workspace/scratch/42e661864e98/out/readers/scan006/R3/crops/13_cancelled_phrase.png` |
| 2026-11-20T09:08:50Z | crop | `/workspace/scratch/42e661864e98/out/readers/scan006/R3/crops/14_de_barred_m.png` |
| 2026-11-20T09:11:50Z | crop | `/workspace/scratch/42e661864e98/out/readers/scan006/R3/crops/15_insertion_comma_anchor.png` |

## Loci left open after the halves

The initial focused-crop set covered fourteen areas: (1) the last word of the opening cancellation; (2) the canceled word after Multomb(F); (3) the doubled-looking F in the upper definition; (4) the accent in fidèlement; (5) the wording and enclosure of the historical insertion; (6) the contracted replacement above d’autre part; (7) the P alphabet; (8) the Fig arrowhead; (9) trouve/trouvera; (10) the class-domain F and canceled a) arrow end; (11) the crowded t in multomb; (12) the mark after l’être; (13) the canceled phrase below inserted On; and (14) de plus the barred abbreviation and pour at the foot.

The comma attachment beside the indexée insertion was not secure when I assembled the C/H punctuation comparison. It was explicitly retained as an open placement issue and received crop 15. That single crop showed the insertion connector to the left of the separate comma, confirming C’s order. I did not re-open a whole half to answer it.

The halves themselves were sufficient for the cancellation of toute, canceled On before C’est, the y spelling in déployement, the absence of commas after the inverse-image maps, the lower canceled hook, and la seconde. Tight original-source boxes for these non-cropped decisions are supplied in report.json.

## Crop construction and stroke decisions

All fifteen crops were made from `/workspace/scratch/42e661864e98/source/SP53_CW_156-6_scans/J156-6-01_156-6_scan006.jpg`.

Each was cropped with Pillow, autocontrasted, sharpened with `UnsharpMask(radius=1.0, percent=130, threshold=3)`, and enlarged to **3000 pixels across using LANCZOS**. Crop 05 was additionally rotated **−2.5°** (clockwise) with BICUBIC resampling, expansion, and a white fill before sharpening/enlargement. Every other rotation was 0°. No further transformations, re-crops, or second image views were made. The exact manifest is also in `crop_manifest.json`.

| Crop file | Original box [left, top, right, bottom] | Rotation; output size | Reason and decisive strokes |
|---|---|---|---|
| `crops/01_opening_deletion.png` | [266, 55, 750, 172] | 0°; 3000 × 725 | Opening a/de: a single low a loop remains, without a separate d ascender and e; read a. |
| `crops/02_multomb_edit.png` | [1368, 72, 1666, 220] | 0°; 3000 × 1490 | Canceled word: an ascending loop and small terminal trace favor de, but the joins remain masked; retain de|la. The interlinear est appelé is visible above. |
| `crops/03_figure_F_glyph.png` | [851, 337, 1084, 431] | 0°; 3000 × 1210 | F glyph: two separated parallel stems and a doubled top bar; retain the locally doubled F. |
| `crops/04_fidelement_accent.png` | [573, 502, 867, 583] | 0°; 3000 × 827 | Adverb accent: a short down-right stroke is distinct from the main-line descender; read fidèlement. |
| `crops/05_jusqua_present.png` | [392, 656, 1611, 780] | -2.5°; 3000 × 436 | Inserted clause: the accented e and ending of présent are visible; read Jusqu’à présent. The long surrounding line is an insertion enclosure. |
| `crops/06_now_abbreviation.png` | [877, 726, 1175, 811] | 0°; 3000 × 856 | Replacement: mai-, a low n, a tall t, compressed continuation and final raised stroke; retain maintent|maintnt|maintenant. |
| `crops/07_power_alphabet.png` | [562, 1141, 1185, 1256] | 0°; 3000 × 554 | P alphabet: stem, angular bowl and lower-left curl establish P but do not isolate one TeX font family. |
| `crops/08_fig_arrow.png` | [807, 1271, 1035, 1355] | 0°; 3000 × 1105 | Fig arrow: only an upper barb appears at the right end; read rightharpoonup. |
| `crops/09_trouve_ending.png` | [439, 1388, 724, 1477] | 0°; 3000 × 937 | Verbal ending: a short ve group ends before the comma; read trouve. |
| `crops/10_first_mapping_arrow.png` | [538, 1474, 1002, 1573] | 0°; 3000 × 640 | First row: the class F has a top flourish/loop; its font remains uncertain. A rounded return survives under oblique cancellations at the arrow’s left end; read a canceled hook. |
| `crops/11_multomb_retracing.png` | [1289, 1534, 1596, 1631] | 0°; 3000 × 948 | Operator letter: live t is readable, with dense upper diagonal/looped ink. Prior-state reconstruction remains uncertain; do not invent an underlying deleted character. |
| `crops/12_after_etre_mark.png` | [944, 1851, 1176, 1938] | 0°; 3000 × 1125 | End mark: two intersecting oblique strokes form four principal arms; retain a cross, with function unspecified. |
| `crops/13_cancelled_phrase.png` | [1214, 1819, 1591, 1912] | 0°; 3000 × 740 | Canceled phrase: three groups; the last has the r beginning, i dot and e-n continuation of rien. The earlier low groups support on ne. Capital On is inserted above. |
| `crops/14_de_barred_m.png` | [266, 2212, 674, 2300] | 0°; 3000 × 647 | Foot: looped d and small e remain live; lower cursive hump under a distinct bar supports barred m; p descender and following low strokes confirm pour. |
| `crops/15_insertion_comma_anchor.png` | [266, 565, 611, 674] | 0°; 3000 × 948 | Insertion anchor: the thin connector descends immediately left of the separate comma after M; insert indexée… before that comma. |

## Line-by-line comparison with C and H

The following groups cover every line in reading order, including interlinear material. Ordinary differences of LaTeX syntax (`\operatorname`/`\mathrm`, `\uline`/`\emph`, or page-number macros) are not treated as reading differences.

| Manuscript line or element | Comparison and reading decision |
|---|---|
| Top centered number | Read 5; encode with `\mspage{5}`. No independent archive pencil number is visible. |
| Opening cancellation | Read `une figure a`, as C, with the whole fragment canceled. H’s final `de` is rejected by crop 01. |
| `Pour … figure F, Multomb(F) … la` | Preserve canceled `toute`, omitted as a deletion by H. Preserve inserted `est appelé` and the following canceled word; that word remains `de|la`. The live `la` follows it. Preserve the masculine `appelé` as inked. |
| `grande multiombre de F, ou la` | Read the full line, including comma and both separate single underlines. |
| `M-multiombre de F. … C’est en` | The F is visibly doubled and is retained as `\mathbb{F}`. Read canceled `On` before `C’est`. |
| `fait une figure ensembliste dans` | Read the full line against both witnesses; no substantive lexical difference remains. |
| Interlinear `indexée … par F tilde (le … de F)` | Read `fidèlement` and `déployement`. Retain the tilde, literal parentheses, and historical y spelling. The long connector is an insertion mark. |
| `M, et dont la connaissance implique celle de` and following `F.` | Read both lines. Crop 15 places the preceding insertion before the comma after M. Preserve the final stop after F. |
| Inserted historical clause | Read `Jusqu’à présent il n’était pas question de L.`. H’s `Jusqu’ici puisque` and added grammatical parentheses are unsupported. |
| `Utilisant … l’application` and replacement above | Preserve canceled `d’autre part`; the insertion remains `maintent|maintnt|maintenant`, without expanding it. |
| Inclusion display | Read `L` hooked into `M`, followed by a comma. Both witnesses convey the relation. |
| `et les applications images inverses` / `correspondantes` | Read both lines with spelling and plural endings as supplied by the ink. |
| First inverse-image line | Read P(M) to P(L), without a final comma. The token P is clear; the exact font family remains uncertain at its first occurrence. |
| Second inverse-image line | Read Fig(M) with a one-sided upper-barbed arrow to Fig(L), without a final comma. |
| `on trouve, en composant avec 1.6 a)b)` | Resolve C’s verbal-ending doubt as `trouve`. Preserve the comma and literal reference numbering. |
| `(1.9)`, brace, a) row | Preserve the exact label, brace, a), uncertain class-domain F, canceled left hook, P(L), plain variable F and mapsto omb(F). The manuscript label is at the left; a TeX comment records that physical placement alongside `\tag*{(1.9)}`. |
| b) row | Preserve b), the same first-candidate class F, canceled hook, Fig(L), plain variable F, mapsto multomb(F), and final comma. Flag the crowded t; the earlier pen state cannot be separated securely. |
| `dont la première n’a aucune raison` | Read the full first line of the qualification. |
| `d’être injective, la seconde par contre` | Read the feminine `la seconde`; H’s `le second` differs from the ink. |
| `a une tendance à l’être` and cross | Retain the cross after l’être. Its meaning is left unassigned. |
| Canceled phrase and inserted On | Read canceled `on ne rien` and inserted `On`, preceding the next line’s appelle. H omits the visible rien and changes the earlier words. |
| `appelle omb(F) la petite ombre de F,` | Read the line and its comma, with one underline beneath `petite ombre`. |
| `ou simplement son ombre quand une` | Read the full continuation. |
| `confusion semble exclue, et` | Read the phrase and comma; no authorial wording is modernized. |
| `de [barred abbreviation] pour multomb, la (petite)` | Read live `de`, literal barred m, and `pour`. H’s deletion/expansion and missing pour are not followed. Preserve the comma, parentheses and underline on petite. |
| `multiombre de la figure F.` | Preserve the single underline spanning `multiombre de la` and the final F and stop. |

## Doubt accounting and mathematical reading

All **12 unique C doubt marks** have individual `c_doubts` entries. The duplicated contextual notes are treated as repetitions of the same physical loci. **Nine are resolved and three retained**: the canceled de/la word, the contracted replacement above d’autre part, and the P alphabet. Two additional issues remain explicit in this reader’s TeX: the domain-F font choice and the crowded t’s physical state. The latter is marked with `\unsure{t}` and an explanatory comment; no speculative deleted symbol is manufactured.

The page defines grande and petite shadows/multi-shadows, then obtains the small assignments by restriction along L into M and composition with 1.6 a)b). I checked the visible map directions and source/target pattern only. The earlier reference was not inspected, and no proof of recovery or injectivity was attempted. The doubled F and one-sided arrowhead are retained despite conventional mathematical expectations.

The author’s qualifications are recorded literally: “dont la première n’a aucune raison d’être injective, la seconde par contre a une tendance à l’être” and “quand une confusion semble exclue”. There is no explicit proof-check request on this page. The cross is reproduced without interpreting its purpose.

## Coverage and limitations

The inventory contains 30 entries covering the entire sheet and embedded alterations. The reading contains **eight confirmed deletion loci, five insertion loci, five single-underlined spans, three display blocks, and five displayed map relations**. There are no diagrams, drawings, independent margin notes, dates, or titles on the page. No double underline was identified.

The output preserves prose paragraphs and display structure without reproducing every physical line break. Exact handwritten font families and inseparable overwritten layers remain the principal limits. The report records these limits rather than resolving them from witness agreement or mathematical expectation. `marked_in_H` denotes an explicit H markup or relevant note at the locus; the H quotation and evidence explain what H actually marks.

The complete transcription is `reading.tex`; the structured evidence, twelve C doubts, empty S-row list, inventory, notation proposals and check events are in `report.json`. All source coordinates and crop transformations are also retained in `crop_manifest.json`.

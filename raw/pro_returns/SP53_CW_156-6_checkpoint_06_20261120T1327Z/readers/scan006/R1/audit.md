# Scan 006 — Independent reader R1 audit

## Scope and inputs

Read only the assigned packet (`brief.md`, `inputs.json`, `C.tex`, `H.tex`, `C_context.md`, `S.json`, `notation.md`) and the exact `/workspace/scratch/42e661864e98/out/PREAMBLE.tex`. The supplied notation table has no adjudicated glyphs. `S.json` is empty, so there are no S rows to confirm or overturn. No other reader, other page, final decision, OCR, PDF text extraction, text-recognition library, external source, or published transcription was consulted. No further reader was spawned. All outputs are inside the assigned R1 directory.

The initial recorded UTC time is 08:58:36 on 2026-11-20. This is a complete page reading, not a sample. There are three mathematical display blocks and no independent drawing or diagram requiring TikZ. The arrows belong to displayed maps. There is no archive pencil number visible.

## Image-view sequence

Every entry below was actually emitted with the image tool. The whole page and each supplied half were emitted exactly once; no entire half was enlarged. Each of the 16 crops was emitted once and was neither re-cropped nor re-viewed. The repeated upper display visible in the natural overlap of the two supplied halves is not an extra image view.

| Order | Role | UTC | Image |
|---:|---|---|---|
| 1 | whole | 2026-11-20T08:58:40Z | /workspace/scratch/42e661864e98/source/SP53_CW_156-6_scans/J156-6-01_156-6_scan006.jpg |
| 2 | half_a | 2026-11-20T08:58:50Z | /workspace/scratch/42e661864e98/source/SP53_CW_156-6_scans/J156-6-01_156-6_scan006_a.jpg |
| 3 | half_b | 2026-11-20T08:59:06Z | /workspace/scratch/42e661864e98/source/SP53_CW_156-6_scans/J156-6-01_156-6_scan006_b.jpg |
| 4 | crop | 2026-11-20T09:03:35Z | /workspace/scratch/42e661864e98/out/readers/scan006/R1/crops/01_cancelled_opening.png |
| 5 | crop | 2026-11-20T09:03:35Z | /workspace/scratch/42e661864e98/out/readers/scan006/R1/crops/02_toute_state.png |
| 6 | crop | 2026-11-20T09:03:35Z | /workspace/scratch/42e661864e98/out/readers/scan006/R1/crops/03_called_cancelled_word.png |
| 7 | crop | 2026-11-20T09:03:35Z | /workspace/scratch/42e661864e98/out/readers/scan006/R1/crops/04_double_F.png |
| 8 | crop | 2026-11-20T09:04:09Z | /workspace/scratch/42e661864e98/out/readers/scan006/R1/crops/05_fidelement.png |
| 9 | crop | 2026-11-20T09:04:09Z | /workspace/scratch/42e661864e98/out/readers/scan006/R1/crops/06_maintenant.png |
| 10 | crop | 2026-11-20T09:04:09Z | /workspace/scratch/42e661864e98/out/readers/scan006/R1/crops/07_script_P.png |
| 11 | crop | 2026-11-20T09:04:09Z | /workspace/scratch/42e661864e98/out/readers/scan006/R1/crops/08_fig_arrow_and_F.png |
| 12 | crop | 2026-11-20T09:05:10Z | /workspace/scratch/42e661864e98/out/readers/scan006/R1/crops/09_trouve.png |
| 13 | crop | 2026-11-20T09:05:10Z | /workspace/scratch/42e661864e98/out/readers/scan006/R1/crops/10_equation_a_arrow.png |
| 14 | crop | 2026-11-20T09:05:10Z | /workspace/scratch/42e661864e98/out/readers/scan006/R1/crops/11_equation_b_arrow.png |
| 15 | crop | 2026-11-20T09:05:10Z | /workspace/scratch/42e661864e98/out/readers/scan006/R1/crops/12_multomb_overwrite.png |
| 16 | crop | 2026-11-20T09:06:22Z | /workspace/scratch/42e661864e98/out/readers/scan006/R1/crops/13_la_seconde.png |
| 17 | crop | 2026-11-20T09:06:22Z | /workspace/scratch/42e661864e98/out/readers/scan006/R1/crops/14_etre_cross.png |
| 18 | crop | 2026-11-20T09:06:22Z | /workspace/scratch/42e661864e98/out/readers/scan006/R1/crops/15_cancelled_rien_and_On.png |
| 19 | crop | 2026-11-20T09:06:22Z | /workspace/scratch/42e661864e98/out/readers/scan006/R1/crops/16_de_abbreviation.png |

## Loci left open after the two halves

The 16 crop loci below were listed after the half-page pass. They are the only enlarged loci. C's cancelled On before C'est, the spelling déployement, insertion entry before the comma after M, and the complete Jusqu'à présent sentence were already settled on half_a; their uncropped source boxes are nevertheless supplied in report.json. The ordinary prose, single underlines, page number, inclusion hook, reference 1.6 a)b), formula label (1.9), element-map directions and closing comma of (1.9) were likewise settled on the halves.

Each crop used its named supplied half as the original source. Pixel boxes are `[left, top, right, bottom]`, with right and bottom exclusive. Every transform was: crop; **0° rotation**; RGB autocontrast with cutoff 0; resize by **LANCZOS to width 3000 px**; save PNG. No sharpening, binarization, OCR or stroke reconstruction was used. Output heights preserve aspect ratio, rounded to the nearest pixel.

| Crop | Source | Original box | Output size | Why needed | Decisive strokes / remaining limit |
|---|---|---|---|---|---|
| crops/01_cancelled_opening.png | half_a | [271, 59, 740, 160] | 3000 × 646 | Distinguish the cancelled final a from H's de. | A single closed a; no d ascender or separate e. |
| crops/02_toute_state.png | half_a | [465, 145, 635, 222] | 3000 × 1359 | Decide whether toute is live, as H prints, or cancelled. | A separate straight strike crosses the low letter bodies. |
| crops/03_called_cancelled_word.png | half_a | [1371, 78, 1666, 222] | 3000 × 1464 | Read the dense crossed short word and its relation to est appelé. | Insertion is clear; la\|de remains uncertain; dans not supported. |
| crops/04_double_F.png | half_a | [863, 335, 1083, 443] | 3000 × 1473 | Distinguish doubled F from ordinary F. | Two separate full-height stems and reinforced arms; preserve mathbb F. |
| crops/05_fidelement.png | half_a | [566, 498, 848, 589] | 3000 × 968 | Separate the accent from crossing strokes of figure above. | Detached down-right accent supports grave è: fidèlement. |
| crops/06_maintenant.png | half_a | [708, 725, 1178, 843] | 3000 × 753 | Read the contracted replacement above d'autre part. | mai and t-like peaks clear; intervening run remains maintent\|maintnt\|maintenant. |
| crops/07_script_P.png | half_a | [567, 1139, 1190, 1259] | 3000 × 578 | Inspect P glyph family against C and H. | Script P is secure; mathcal\|mathscr remains uncertain. |
| crops/08_fig_arrow_and_F.png | half_b | [825, 149, 1224, 271] | 3000 × 917 | Inspect the single-barb candidate and the apparently detached target-F top stroke. | One upper barb only. The detached mark is the top arm of F, not an additional overbar. |
| crops/09_trouve.png | half_b | [442, 281, 729, 375] | 3000 × 983 | Distinguish trouve from trouvera. | Compact ve ending followed by comma; no ra. |
| crops/10_equation_a_arrow.png | half_b | [539, 382, 785, 470] | 3000 × 1073 | Read the first cancelled attachment and script domain F. | Rounded hook beneath slashes; script F has a flourished top and single stem. |
| crops/11_equation_b_arrow.png | half_b | [553, 488, 785, 575] | 3000 × 1125 | Read the second cancelled attachment independently and compare domain F. | Same cancelled hook; same script domain F. |
| crops/12_multomb_overwrite.png | half_b | [1290, 443, 1590, 526] | 3000 × 830 | Inspect a dense t overwrite unrecorded by both witnesses. | t stem/cross-stroke survives, but live retracing versus cancellation remains uncertain. |
| crops/13_la_seconde.png | half_b | [928, 663, 1303, 737] | 3000 × 592 | Decide between C's la seconde and H's le second without repairing grammar. | Final e-like tail favours seconde; article vowel remains indistinct. |
| crops/14_etre_cross.png | half_b | [945, 756, 1187, 832] | 3000 × 942 | Distinguish cross, asterisk and period. | Two crossing strokes; cross retained, no corresponding note seen. |
| crops/15_cancelled_rien_and_On.png | half_b | [1219, 715, 1592, 817] | 3000 × 820 | Read the first cancelled groups, final rien and replacement On. | rien and inserted On clear; on ne\|a priori remains uncertain. |
| crops/16_de_abbreviation.png | half_b | [271, 1085, 703, 1190] | 3000 × 729 | Resolve the possible deletion, barred abbreviation and word before multomb. | Live de, barred m with articulated lower stroke, and looped-p pour. |

**Actual crop count: 16.** These are 16 original crops and 16 emitted crop views, not additional iterations. Each source file is named absolutely in report.json. The report also supplies source boxes for all differences settled without a crop.

## Line-by-line comparison

Line identifiers below describe manuscript lines, not retained TeX line wrapping. Consecutive uncontested words are grouped, but every line, insertion and cancellation was compared with both drafts. Macro-only differences such as H's `emph` versus our `uline`, `mathrm` versus `operatorname`, page-number macro spelling, and H's explicit explanatory hook note were not treated as independent substantive misreadings.

| Manuscript line(s) | Comparison and decision |
|---|---|
| A0: header and abandoned first line | Manuscript 5 is clear and is represented by mspage{5}. The cancelled opening ends in a, not H's de (crop 01). No title or date. |
| A1: Pour ... figure F, Multomb(F) ... la | toute is cancelled (crop 02). est appelé is a real insertion above the following crossed short word. That crossed word remains la\|de, against H's definite dans (crop 03). Main-line comma after F and the parentheses of Multomb(F) are retained. |
| A2: grande multiombre de F, ou la | Both words grande and multiombre have separate single underlines. de F, comma, ou la agree and are read on the half. |
| A3: M-multiombre de F. On C'est en | Genuine hyphen after M; visibly doubled F retained (crop 04). Full stop follows. Cancelled On is readable on half_a, removing C's doubt. C'est en continues into the next main line. |
| A4: fait une figure ensembliste dans | All words agree with both drafts and were read on half_a. The descenders of this line cross the later indexing insertion but are not themselves corrections. |
| A5 main: M, et dont la connaissance implique celle de | Both drafts' ordinary words agree. The insertion leader enters just after M and before the original comma, so the comma follows the inserted clause in reading order. |
| A5 inserted: indexée ... (le déployement de F) | indexée, par, tilde F and the parentheses are clear on the half. fidèlement is resolved with grave accent in crop 05. The descender after déplo establishes déployement, preserving C against H's déploiement. |
| A6: F. | The final F and stop complete the upper paragraph and are included. |
| A7 inserted: Jusqu'à présent ... L. | The half resolves Jusqu'à présent il n'était pas question de L. H's Jusqu'ici puisque and textual parentheses are rejected: the large curved enclosure is an insertion carrier. The period is retained. |
| A7 main: Utilisant ... l'application | d'autre part is struck through. The replacement above it remains maintent\|maintnt\|maintenant (crop 06), without silently expanding it. Utilisant and l'application agree. |
| A8: inclusion display | L hookrightarrow M, with the left hook and terminal comma, is clear on the half and agrees with both drafts. |
| A9–A10: et les applications images inverses / correspondantes | Read word by word; both drafts agree. No extra punctuation supplied. |
| A11 / top of B: P inverse-image row | The P alphabet remains mathcal\|mathscr at the first occurrence (crop 07). The second P repeats it; later occurrences use the first candidate. The arrow has two clear barbs. H's final comma is absent. |
| B1: Fig inverse-image row | Names, parentheses and arguments agree. The arrow has only an upper barb (crop 08). The detached target-F top stroke is an F arm, not an added overbar. H's comma is absent. |
| B2: on trouve, en composant avec 1.6 a)b) | trouve is resolved in crop 09. The comma, remaining prose and numbered reference are read from the half. The referenced earlier material is not consulted. |
| B3: (1.9)a | The left label (1.9), brace and a) are present. Script domain F and cancelled left hook checked in crop 10. Target P(L) repeats the preceding P. The plain F maps to lowercase omb(F). |
| B4: (1.9)b | Script F and cancelled left hook checked independently in crop 11. Target Fig(L), input F, right mapsto and terminal comma are clear. The t of multomb(F) is densely overwritten (crop 12), requiring the additional live/retraced-versus-deleted-t uncertainty that both drafts omit. |
| B5: dont la première n'a aucune raison | The words and accent of première agree and are included. |
| B6: d'être injective, ... par contre | The comma and flanking words agree. The la seconde\|le second locus remains open after crop 13; grammar is not used to force a reading. |
| B7: a une tendance à l'être; cancellation and On | The phrase is read as written. The following mark is a cross (crop 14), not H's full stop. Crop 15 confirms cancelled final rien and inserted On; the preceding crossed groups remain on ne\|a priori. H's On va fails to include the visible rien. |
| B8: appelle omb(F) la petite ombre de F, | All live words, function name, argument and comma agree. petite ombre has one continuous underline. |
| B9–B10: ou simplement son ombre quand une / confusion semble exclue, et | Read in full on half_b. Ordinary wording and punctuation agree; no expansion or correction introduced. |
| B11: de [barred m] pour multomb, la (petite) | Crop 16 resolves live de, a barred m abbreviation, and pour. H incorrectly strikes and expands the first two tokens and reads the following word as uncertain de. multomb is unexpanded; comma and parentheses retained; petite alone is underlined. |
| B12: multiombre de la figure F. | multiombre de la has one continuous underline, then live figure F and final stop. Nothing follows at the page foot. |

## Completeness and remaining limits

The full page is in reading.tex. The inventory has 26 entries, including the page number, all prose/display blocks, five insertions, eight definite deletions, the additional uncertain t overwrite, the cross and the final abbreviated definition. All have been checked against the completed transcription and marked transcribed=yes. There are no independent margin notes, drawings, diagrams, dates or hidden continuation blocks in this image. The large curved insertion carriers are represented by insertion placement rather than treated as drawn mathematical objects.

All 12 distinct C doubtful loci are present in c_doubts; duplicate mentions of the same physical doubt in C_context.md are not counted twice. **Eight are resolved and four retained.** Six loci in all remain explicitly uncertain in reading.tex: the cancelled la\|de; maintent\|maintnt\|maintenant; the first P alphabet; the t overwrite; la seconde\|le second; and cancelled on ne\|a priori. The 27 difference records include literal punctuation, every differing physical state, uncertainty removals and all substantive alphabet differences. S contributes no rows.

The mathematical notes distinguish a local parsing check from proof. I followed the inclusion, inverse-image directions, the two outputs in (1.9), the grande/petite names, and the injectivity qualification. I did not prove recovery of F, faithful indexing, or injectivity, and did not inspect the cited 1.6. The exact cautious phrases are quoted in report.json. No explicit authorial instruction to verify a theorem was found.

The main physical limits are the opacity of cancelled strokes, the contracted replacement for d'autre part, the arbitrary correspondence between handwritten script P and two LaTeX alphabets, and the strongly overwritten t. No extra image iteration was used to manufacture certainty. The final decisions belong to the adjudicator; this independent reading has not been revised from another reader's findings.

Schema note: marked_in_H is treated as true for an explicit uncertainty or relevant physical-intervention mark/note in H. A surrounding add is counted only when placement itself is at issue. This interpretation is also stated in brief_feedback.


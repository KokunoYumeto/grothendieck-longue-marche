# Scan 007 — independent reader R2 audit

Only the assigned scan 007 packet and its referenced PREAMBLE were read. No other page, other reader, consolidated decision, OCR, text recognition, PDF text extraction, external research, or published transcription was used. S.json is empty. The supplied notation table was treated as provisional, not authoritative.

## Image-view sequence

C, H, C_context, S, notation and PREAMBLE were read before the image pass. The first recorded timestamp (09:22:45 UTC) is the start of that image pass; packet reading preceded it.

1. Whole scan — 2026-11-20 09:22:45 UTC, once, for layout.
2. Supplied half a — 09:22:53 UTC, once, read line by line against both witnesses.
3. Supplied half b — 09:23:25 UTC, once, read line by line against both witnesses.
4. Crops 01–03 — 09:24:52 UTC; crops 04–06 — 09:25:47 UTC; crops 07–09 — 09:26:22 UTC; crops 10–13 — 09:27:10 UTC. Every crop was emitted once through the image tool.

**Actual crops: 13. Total emitted images: 16.** No whole image or half was revisited, no whole half was enlarged, and no crop was recropped or re-emitted.

## Loci left open after the halves

The thirteen crop loci were: initial multiombre correction; formé(e); the combined old/replacement inclusion collision; incidence(s); each of the two compressed prepositions; ça and revient; the barred-m/equality-shaped sign; the dense prefix in the second réconstitue; the overwritten initial and live word souvent; initial A of Ateliers; the correction beneath à partir; and the final section-like sign. The inclusion collision carries two C doubts in one physical locus. The dense ré prefix was an additional observation beyond the C doubt list.

The halves already settled the parenthetical warning, déployement with y, ie. punctuation, the two finite-verb reconstruction clauses and pourtant. No crop was made for these settled loci. Their tight source coordinates are supplied in report.json. All 14 C doubt-table entries have individual dispositions; 4 are resolved and 10 retained.

## Crop transforms and decisions

All crops use the original whole JPEG, with pixel boxes in that source (1682 × 2360). Rotation is 0°. Each was cropped in Pillow, autocontrasted with 0.5% cutoff, sharpened with UnsharpMask(radius=1.2, percent=130, threshold=2), and enlarged by LANCZOS to 3000 pixels wide. The enlarged output was saved as JPEG quality 95, chroma subsampling 0. No OCR or text-image interpretation library was used.

| Crop | Original box [left, top, right, bottom] | Output pixels | Needed for / result |
|---|---|---|---|
| `crops/01_multiombre_correction.jpg` | [428, 580, 816, 680] | 3000 × 773 | Double initial undulations: test older om against retracing; unresolved. |
| `crops/02_forme_ending.jpg` | [1120, 554, 1373, 669] | 3000 × 1364 | Terminal formé(e): test whether a separate last e survives; unresolved. |
| `crops/03_inclusion_correction.jpg` | [1084, 868, 1455, 982] | 3000 × 922 | Collision after relation d’: recover old word and live replacement; old word open, inclusion resolved. |
| `crops/04_incidences_ending.jpg` | [658, 1095, 1113, 1207] | 3000 × 738 | Detached incidence(s) ending: distinguish final s from a separated e; unresolved. |
| `crops/05_relation_preposition.jpg` | [1008, 1176, 1290, 1300] | 3000 × 1319 | Compressed preposition before tilde F: de/dans remains open. |
| `crops/06_preposition_M.jpg` | [526, 1310, 760, 1435] | 3000 × 1603 | Compressed preposition before M: de/dans remains open. |
| `crops/07_ca_revient.jpg` | [260, 1425, 601, 1540] | 3000 × 1012 | Cedilla and the following word: resolves ça revient; no new deleted word isolated. |
| `crops/08_barred_m.jpg` | [633, 1421, 970, 1524] | 3000 × 917 | Two-stroke sign: resolves curved letter plus upper bar, barred m. |
| `crops/09_reconstitue_onset.jpg` | [340, 1758, 741, 1865] | 3000 × 800 | Unnoticed dense prefix at second réconstitue: retains uncertainty in physical state, without invented earlier letters. |
| `crops/10_souvent_correction.jpg` | [1100, 1725, 1420, 1844] | 3000 × 1116 | Overwritten initial and live adverb: d/à remains open; souvent is secure. |
| `crops/11_ateliers_initial.jpg` | [467, 1849, 742, 1970] | 3000 × 1320 | Capital A collision: old a versus retracing remains open. |
| `crops/12_a_partir_correction.jpg` | [1326, 1825, 1644, 1959] | 3000 × 1264 | Overwritten à: earlier de versus à remains open. |
| `crops/13_paragraph_sign.jpg` | [328, 2140, 679, 2252] | 3000 × 957 | Final section-like mark: §/S remains open; no secure independent cancellation stroke. |

Each output path is under /workspace/scratch/42e661864e98/out/readers/scan007/R2/. The exact source, box, rotation, filter settings, size and absolute output path are also recorded in report.json crop_transforms. Detailed decisive-stroke evidence is in differences and c_doubts.

## Line-by-line comparison record

- Header: his number 6 is visible; neither a separate archive number nor a date is present.
- Lines 1–3, “Ainsi” through “de la”: both witnesses preserve the lexical sequence. The opening word is capitalized; the comma after Ainsi and the dash before on dit are present. The underline starts at lieux. C’s TeX underline and H’s emphasis were treated as equivalent notation for that visible underline, not a separate textual discrepancy.
- Lines 4–5, “figure” through “lieux).”: underline continues under figure; the raised paired quotation marks are transcribed with the required TeX quote convention. C’s “à ne pas confondre, avec les” matches the ink. H’s illegible/un peu/abusivement/ou sequence does not. The final parenthesis and full stop are present.
- Line 6: “La … est donc … des” is complete. Initial multiombre and the formé(e) ending required crops 01–02. The live noun is secure; its earlier-letter state and the final e count remain marked.
- Lines 7–8: “ombres de ses strates, elle est indexée par le déployement” agrees lexically except H’s modernized déploiement. The y descender, tilde over F, comma and “ensemble des” are visible.
- Line 9: “strates de F, la relation d’ … de la” is complete. There is a canceled older start plus the replacement inclusion; crop 03 was used once for both. C’s uncertainty in live inclusion is removed; the older d’ordre/d’inclu remains unresolved.
- Lines 10–11: “figure ensembliste n’étant autre que la relation d’… entre strates” agrees apart from the uncertain incidence(s) ending. The n’ and apostrophes are retained. Crop 04 does not decide the final s/e question.
- Line 12: “de F, ie. la relation … tilde F induite” is complete. C’s ie. punctuation matches the half; H’s i.e. supplies an unobserved intervening stop. Crop 05 retains the first de/dans doubt. The wave above F is clear.
- Line 13: “par ≤ … M (ou par ≪ au choix,” is complete. Both signs are visually secure, with one lower bar on ≤ and none on ≪. Crop 06 retains the second de/dans doubt and confirms the tall curved M.
- Line 14: the clause is “ça revient au barred m). Alors qu’une”. Crops 07–08 resolve C’s ça/sa and barred-m/equality doubts. H’s se réduisant and equals sign disagree. The closing parenthesis and period are secure.
- Lines 15–16: “figure ne se réconstitue pratiquement jamais à partir de son ombre, elle” is visible and agrees with C. H’s n’est reconstituable misaligns the actual finite-verb phrase. No new crop was needed.
- Line 17: “se réconstitue pourtant … souvent (cas” is complete. H’s est reconstituable is rejected. Crop 09 records the dense ré prefix without inventing a canceled old word. Pourtant was already resolved from the half. Crop 10 keeps d/à under the initial open and resolves the live word souvent; H’s uncertain dans is this live token, while its canceled donc is a separate proposed underlying reading.
- Line 18: “des [quotes]Ateliers ensemblistes[quotes]) à partir” is complete. Crops 11–12 preserve the unresolved earlier a/retraced-A and de/à correction states. There is one physically overwritten position before partir. Quote typography is rendered by the stipulated TeX convention; no macro-only discrepancy was counted.
- Lines 19–20: “de sa multiombre. Nous y reviendrons.” agrees in both witnesses, including the full stops and the forward reference.
- Lines 21–22: final sign plus “Il y a lieu de parler des relations d’ordre canoniques”. Crop 13 preserves §/S uncertainty and supplies no secure evidence for H’s asserted cancellation. The sentence is unfinished at the page edge, with no invented punctuation or continuation.

## Mathematical reading and limitations

The content was followed as a definition/explanation of shadow and multiombre, an assertion identifying inclusion with induced incidence, and a reconstruction claim. The phrase “au choix, ça revient au barred m” was read as the author’s equivalence assertion. “Nous y reviendrons.” is a forward reference, not a request for verification. There is no explicit authorial doubt or check phrase on this sheet.

No proof check, independent re-proof or computation was performed. The three mathematical statements are recorded only as background, with the explicit outcome that they were read as the author’s assertions without mathematical verification. In particular, expected mathematics was not used to choose incidence/incidences or de/dans.

The final reading has 11 explicit unresolved loci. Ambiguous physical state is preserved at multiombre and Ateliers; a heavily retraced prefix is not automatically declared a deletion. No older character is supplied under réconstitue. No formula symbol is replaced by an illegibility placeholder. The complete text, all interventions (including uncertain ones), underline, header and unfinished final paragraph are inventoried and transcribed. There are no diagrams, drawings, displays or independent margin notes to typeset.

Status: complete.

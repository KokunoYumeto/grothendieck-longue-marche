# Scan 007 — reader R3 audit

## Scope and inputs

Read only this page’s brief, inputs, C.tex, H.tex, C_context.md, S.json, notation table and the referenced PREAMBLE. No other reader output, other page, external source, OCR, text-recognition library or PDF text extraction was used. S.json is empty. No further reader was spawned. All writes are confined to this assigned R3 directory.

## Image-view sequence

Every image listed below was emitted through `image((await tools.view_image({path: ...})).image_url)`. The whole and each supplied half were viewed once, in the required order. No full half was enlarged or viewed again. Each new crop was emitted once.

| Order | Role / file | UTC |
|---|---|---|
| 1 | whole — J156-6-01_156-6_scan007.jpg | 2026-11-20T09:22:39Z |
| 2 | half_a — J156-6-01_156-6_scan007_a.jpg | 2026-11-20T09:22:43Z |
| 3 | half_b — J156-6-01_156-6_scan007_b.jpg | 2026-11-20T09:23:04Z |
| 4 | crop — 01_multiombre_start.jpg | 2026-11-20T09:24:46Z |
| 5 | crop — 02_forme_ending.jpg | 2026-11-20T09:24:58Z |
| 6 | crop — 03_inclusion_overwrite.jpg | 2026-11-20T09:24:58Z |
| 7 | crop — 04_incidences_ending.jpg | 2026-11-20T09:25:44Z |
| 8 | crop — 05_relation_preposition.jpg | 2026-11-20T09:25:44Z |
| 9 | crop — 06_order_preposition.jpg | 2026-11-20T09:25:44Z |
| 10 | crop — 07_ca_revient.jpg | 2026-11-20T09:26:21Z |
| 11 | crop — 08_barred_m.jpg | 2026-11-20T09:26:21Z |
| 12 | crop — 09_souvent_start.jpg | 2026-11-20T09:26:42Z |
| 13 | crop — 10_ateliers_start.jpg | 2026-11-20T09:26:42Z |
| 14 | crop — 11_a_partir_overwrite.jpg | 2026-11-20T09:26:42Z |
| 15 | crop — 12_paragraph_sign.jpg | 2026-11-20T09:27:26Z |
| 16 | crop — 13_reconstitue_start.jpg | 2026-11-20T09:27:26Z |
| 17 | crop — 14_F_after_strates.jpg | 2026-11-20T09:27:26Z |

## Whole-page inventory and half-page pass

The whole-page view established one handwritten page number 6 at the top, a long prose paragraph, a second paragraph beginning with a section-like sign, an underlined phrase, and several crowded correction regions. No marginal note, display, diagram, drawing, title, date or separate archive number was observed.

### Line-by-line comparison

- Lines 1–3: read Ainsi through lieux de la against C and H. Both lexical openings agree. The quotation is made of high paired ticks, and the underline is single; H’s guillemets are not literal ink.
- Lines 4–5: read figure and the complete parenthesis. C’s à ne pas confondre, avec les strates de la figure qui sont des lieux is supported. H’s ill/un peu/abusivement/ou sequence is a phrase-level misreading, not omitted ink.
- Line 6: La and the live multiombre are clear; the dark initial and formé(e) ending remained open. Both received separate tight crops.
- Lines 7–8: ombres de ses strates, elle est indexée par le déployement tilde F, ensemble des is present. The descending y settles déployement against H’s modernized déploiement. The tilde is a separate wave.
- Lines 9–10: strates de F, la relation d’… de la figure ensembliste n’étant autre que agrees in its unaffected stretches. The crossed word and live replacement remained open as one correction locus and received crop 03.
- Line 11: la relation d’incidence(s) entre strates is present. The last e/s sequence remained open for crop 04.
- Line 12: de F, ie. la relation de/dans tilde F induite is present. The preposition remained open for crop 05. Ordinary F’s apparent upper mark was added to the open list and checked in crop 14; it is its retraced upper arm, not an additional accent. The abbreviation has no interletter point, against H’s i.e.
- Line 13: par ≤ de/dans M (ou par ≪ au choix, is present. Signs ≤ and ≪ are clear; the second compressed preposition needed crop 06.
- Line 14: ça revient au barred m). Alors qu’une: the first word and barred sign remained on the crop list. Crops 07 and 08 settle them. H’s se réduisant and = do not fit the visible strokes.
- Lines 15–16: figure ne se réconstitue pratiquement jamais à partir de son ombre, elle is legible from the half. H’s n’est reconstituable substitutes a different verbal construction.
- Line 17: se réconstitue pourtant …souvent (cas is present. Pourtant is settled from the half and does not need a crop. A crowded initial ré in réconstitue was checked in crop 13; no former canceled word was established. Crop 09 addresses the overwritten initial and live souvent. H’s est reconstituable and uncertain dans are not the live words.
- Line 18: des opening quotation Ateliers ensemblistes closing quotation) …à partir is present. The possible old a and the correction under à required crops 10 and 11. The first remains a physical-state uncertainty; the second shows old de.
- Lines 19–21: de sa multiombre. Nous y reviendrons. is present without additional text or marginal matter.
- Final two lines: Il y a lieu de parler des relations d’ordre canoniques is clear and unfinished at the page boundary. Crop 12 settles the leading mark as a live §, against H’s struck § and C’s symbol uncertainty.

## Loci left open after the halves

The open list comprised: initial multiombre/possible om; formé/formée; the canceled and replacement word after relation d’; incidence(s); both de/dans prepositions; ça/sa and the adjacent verb phrase as aligned to H; barred m/=; the old start and live word at souvent; possible former a beneath Ateliers; old matter beneath à partir; §/S and cancellation state; possible retracing at the second réconstitue; and the form of ordinary F in de F, ie. All were addressed by the fourteen local crops below. Pourtant, the two reconstruction constructions, déployement and the parenthetic caution were already settled by the halves; their coordinates are supplied in the report without redundant crops.

## Crop construction and decisions

All crops come from the original 1682 × 2360 whole-page JPEG. Boxes use original-source coordinates `[left, top, right, bottom]`. Rotation is 0° for every crop. Pillow processing was: crop → grayscale → autocontrast with 0.5% cutoff → UnsharpMask(radius=1, percent=140, threshold=3) → LANCZOS resize to 3000 pixels wide, preserving aspect ratio → JPEG quality 95, subsampling 0. No crop was re-cropped or re-viewed. The separate crop_manifest.json records all transforms.

| Crop | Original box | Output pixels | Purpose and result |
|---|---|---|---|
| 01_multiombre_start.jpg | [275, 572, 815, 690] | 3000 × 656 | Distinguish a possible old om from normal or retraced mu; the former fragment and its cancellation state remain uncertain. |
| 02_forme_ending.jpg | [975, 570, 1500, 680] | 3000 × 629 | Inspect the accented final stroke for one versus two e letters; formé/formée remains open. |
| 03_inclusion_overwrite.jpg | [1065, 870, 1545, 985] | 3000 × 719 | Separate the canceled d’ordre/d’inclu and the overwritten live inclusion; both are retained with uncertainty. |
| 04_incidences_ending.jpg | [650, 1087, 1320, 1210] | 3000 × 551 | Inspect the detached terminal for plural s; incidence(s) remains uncertain. |
| 05_relation_preposition.jpg | [755, 1190, 1285, 1310] | 3000 × 679 | Read the compressed preposition before tilde F; de/dans remains open. |
| 06_order_preposition.jpg | [425, 1325, 780, 1425] | 3000 × 845 | Read the compressed preposition before M and verify nearby ≤/M strokes; only the preposition remains open. |
| 07_ca_revient.jpg | [250, 1432, 770, 1545] | 3000 × 652 | Distinguish ç from s and align H’s reduisant reading; ça revient is settled. |
| 08_barred_m.jpg | [645, 1434, 975, 1530] | 3000 × 873 | Distinguish barred cursive m from =; the visible trough and kink settle barred m. |
| 09_souvent_start.jpg | [1085, 1720, 1430, 1835] | 3000 × 1000 | Separate the old initial from the live word often; souvent is secure, old à/d remains uncertain. |
| 10_ateliers_start.jpg | [445, 1844, 745, 1970] | 3000 × 1260 | Inspect the extra low loop under A; possible deleted a versus retraced A remains open. |
| 11_a_partir_overwrite.jpg | [1315, 1835, 1635, 1958] | 3000 × 1153 | Identify the old group beneath à; a distinct d and low e settle deleted de. |
| 12_paragraph_sign.jpg | [315, 2150, 490, 2250] | 3000 × 1714 | Decide § versus S and whether struck; live § is settled. |
| 13_reconstitue_start.jpg | [325, 1754, 750, 1865] | 3000 × 784 | Inspect a crowded initial in the second réconstitue for a correction or old word; no independent predecessor is identified. |
| 14_F_after_strates.jpg | [270, 1218, 640, 1320] | 3000 × 827 | Check whether ordinary F has an added bar/tilde; it has two arms only, with a retraced top arm. The adjacent ie. also confirms its literal punctuation. |

Actual crop count: **14**. Total emitted image count: **17** (one whole, two halves, fourteen crops).

## Mathematical reading and limitations

The page gives a shadow definition, a multiombre/indexing description, an identification with incidence and induced orders, and a reconstruction contrast. These were read as the author’s assertions; no proof, independent re-proof or computation was performed. The equivalence remark “ou par ≪ au choix, ça revient au [barred m]” and “Nous y reviendrons” are preserved. Neither is treated as a completed mathematical verification.

Five C doubts are resolved and nine are retained. Remaining uncertainty is local ink uncertainty, particularly flattened letter endings and overwritten initials. No grammatical expectation supplies a final e or singular ending; no expected mathematical formulation chooses de/dans. The possible old om and a remain uncertain in physical state, as opposed to asserting deletion merely from dark retracing. The old fragment beneath souvent has only local traces, so it is not expanded to H’s donc.

No reading from another page or reader was used to resolve an uncertainty. There is no missing text gap and no formula symbol was replaced by an illegibility placeholder. All observed page elements are represented in reading.tex and the inventory; no diagram/drawing markup is required because no such element is present.

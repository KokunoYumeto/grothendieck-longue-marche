# Scan 012 — independent reader R2 audit

Scope: only the assigned scan 012 packet, its authorized current-page conventions, the supplied current-page whole/halves, and R2’s own crops. No other page, reader result, consolidated decision, OCR, external research, PDF extraction, or LaTeX compilation was used.

The first logged UTC time is the whole-image session start; packet reads preceded that clock event. Whole and half images were emitted exactly once each. The page has been transcribed completely, including its ending continuation.

## Actual image-view sequence

1. 2026-11-20 11:20:03 UTC — whole: `J156-6-02_156-6_scan012.jpg` (emitted through tools.view_image).
2. 2026-11-20 11:20:09 UTC — half_a: `J156-6-02_156-6_scan012_a.jpg` (emitted through tools.view_image).
3. 2026-11-20 11:20:33 UTC — half_b: `J156-6-02_156-6_scan012_b.jpg` (emitted through tools.view_image).
4. 2026-11-20 11:22:23 UTC — crop: `01_diagram_118.jpg` (emitted through tools.view_image).
5. 2026-11-20 11:23:02 UTC — crop: `02_slanted_margin.jpg` (emitted through tools.view_image).
6. 2026-11-20 11:24:01 UTC — crop: `03_de_plus_insertion.jpg` (emitted through tools.view_image).
7. 2026-11-20 11:24:10 UTC — crop: `04_sole_element.jpg` (emitted through tools.view_image).
8. 2026-11-20 11:24:21 UTC — crop: `05_les_relations.jpg` (emitted through tools.view_image).
9. 2026-11-20 11:24:26 UTC — crop: `06_display_120.jpg` (emitted through tools.view_image).
10. 2026-11-20 11:24:48 UTC — crop: `07_deleted_et.jpg` (emitted through tools.view_image).
11. 2026-11-20 11:25:00 UTC — crop: `08_deployement.jpg` (emitted through tools.view_image).
12. 2026-11-20 11:25:19 UTC — crop: `09_final_family_f.jpg` (emitted through tools.view_image).
13. 2026-11-20 11:25:26 UTC — crop: `10_label_123.jpg` (emitted through tools.view_image).
14. 2026-11-20 11:25:29 UTC — crop: `11_bottom_replacement.jpg` (emitted through tools.view_image).
15. 2026-11-20 11:26:01 UTC — crop: `12_final_dy.jpg` (emitted through tools.view_image).

## Open loci after the two half views

The following twelve locus groups remained open. The margin was treated as one connected slanting locus because its prose, two formulas, cancellation and nearby body-line start interlock. The bottom replacement was likewise one physical correction locus. Each received one crop only; no crop was remade or re-viewed.
- 01_diagram_118: Dark lower-right sign and the small gaps in the oblique enclosure.
- 02_slanted_margin: All slanted prose, the first equivalence, cancellation, proposed underbar sign and terminal punctuation; overlapping start of the body paragraph and first family F.
- 03_de_plus_insertion: Insertion anchor and possible comma following de plus.
- 04_sole_element: Shortened element word and right-hand empty-family sign.
- 05_les_relations: Upper versus lower case initial after a).
- 06_display_120: Abbreviation, Sup lettering and each i, plus crowded final inequality.
- 07_deleted_et: Canceled group immediately above the live D of D’autre.
- 08_deployement: Medial descender and exact spelling.
- 09_final_family_f: Last object of (1.22), including its looped foot.
- 10_label_123: Punctuation after 1 in the final label.
- 11_bottom_replacement: Both uncertain words in the replacement: deleted equivalent and inserted minima/minimes.
- 12_final_dy: Last words and the d’y/de s’y disagreement.

## Crop transforms and decisions

All original-source coordinates below refer to the full 1681 × 2361 scan. All crops received autocontrast, UnsharpMask(radius=1.2, percent=120, threshold=3), LANCZOS resizing and JPEG quality 95. Only crop 02 was rotated, using bicubic resampling and white fill before enlargement.
- `01_diagram_118.jpg`: source `J156-6-02_156-6_scan012.jpg`; box [408, 205, 1100, 725]; rotation 0°; output 3200 × 2405 pixels. Both left corners of the frame have gaps. The lower-right sign includes a heavy extra upright; no specific deleted predecessor was invented.
- `02_slanted_margin.jpg`: source `J156-6-02_156-6_scan012.jpg`; box [12, 730, 625, 1342]; rotation -32°; output 3600 × 3596 pixels. Read the slanting note in its own direction; retained car, avoir, full relation, il faudrait écrire, the canceled F plus wedge, double-underlined ou and terminal point. Resolved the apparent membership prime as neighboring-line punctuation. The alleged extra standalone formula and struck Les were not found. Alphabet choices remain explicitly uncertain.
- `03_de_plus_insertion.jpg`: source `J156-6-02_156-6_scan012.jpg`; box [760, 932, 1110, 1092]; rotation 0°; output 2800 × 1280 pixels. The insertion ends with a separate comma and enters between est and réflexive.
- `04_sole_element.jpg`: source `J156-6-02_156-6_scan012.jpg`; box [1260, 1038, 1648, 1169]; rotation 0°; output 3000 × 1013 pixels. Retained élémt|élément because the middle collapses to a line; confirmed the slashed empty sign and its collection subscript.
- `05_les_relations.jpg`: source `J156-6-02_156-6_scan012.jpg`; box [525, 1367, 715, 1474]; rotation 0°; output 2600 × 1464 pixels. Resolved the tall straight initial with its foot as capital L in Les.
- `06_display_120.jpg`: source `J156-6-02_156-6_scan012.jpg`; box [535, 1570, 1665, 1707]; rotation 0°; output 3600 × 436 pixels. Read str with raised t and a point, capital Sup, all dotted i indices, and the reinforced terminal leq. No old character can be isolated under that reinforcement.
- `07_deleted_et.jpg`: source `J156-6-02_156-6_scan012.jpg`; box [254, 1794, 480, 1881]; rotation 0°; output 2800 × 1078 pixels. Retained Et|En under cancellation; rejected a full canceled D’autre.
- `08_deployement.jpg`: source `J156-6-02_156-6_scan012.jpg`; box [793, 1915, 1160, 2007]; rotation 0°; output 3000 × 752 pixels. Read a long descending y; no separate acute appears above the reduced e of initial de. Transcribed deployement.
- `09_final_family_f.jpg`: source `J156-6-02_156-6_scan012.jpg`; box [913, 1971, 1138, 2070]; rotation 0°; output 2800 × 1232 pixels. Resolved the last object as the collection F by its closed foot and curved top; H’s observational note is credited while its body correction is rejected.
- `10_label_123.jpg`: source `J156-6-02_156-6_scan012.jpg`; box [255, 2127, 414, 2211]; rotation 0°; output 2500 × 1321 pixels. Resolved the separator as a comma: (1,23).
- `11_bottom_replacement.jpg`: source `J156-6-02_156-6_scan012.jpg`; box [878, 2136, 1670, 2266]; rotation 0°; output 3600 × 591 pixels. Kept the bottom équivalent and minima|minimes doubts. The longer minimales is unsupported by a tall l. The deletion and its replacement were both transcribed.
- `12_final_dy.jpg`: source `J156-6-02_156-6_scan012.jpg`; box [1470, 2245, 1665, 2333]; rotation 0°; output 2600 × 1173 pixels. Resolved d’y; no separate s is present.

## Line-by-line comparison record

- Header and diagram: read author number 11; compared every G/F object, six relations and five double arrows against both witnesses. All arrow directions agree. Recorded the frame gaps and the additional upright in the dark lower-right sign. The body’s two clean compatibility signs were compared separately and are not normalized to H’s between glyph.
- First three body lines: compared Parmi les six relations, il y a quatre relations d’ordre, the four listed signs, and et les deux autres relations ... sont symétriques, including commas and final point. The marginal criticism was read at crop 02 rather than silently harmonized with this assertion.
- Slanted margin, top to bottom: compared Non ... n’est pas rel. d’ordre; elle est transitive mais non réflexive, car; the self-incidence equivalence; Pour avoir une relation d’ordre il faudrait écrire; the canceled F/wedge; the underlined-triangle definition, déf, doubly underlined ou, F=F and its terminal point. Kept the literal repeated F operands. No second standalone left-hand formula is supplied.
- Next body paragraph: compared La relation, compatibility sign, est, inserted de plus with its comma, réflexive, mais parallel ne l’est que si, first family F, est réduit à son seul, the uncertain element word, empty-family sign, comma, and car. No struck Les was identifiable. Family F’s alphabet is marked once.
- (1.19): compared the two plain F operands, parallel, two-headed implication, equality, slashed oval and subscript, figure vide and point. Only the family alphabet differs substantively from H; emptyset/varnothing macro choice is not independently counted.
- Remarques a): compared underline, capital Les, relations, triangle, et leq, se déterminent mutuellement, point, Connaissant leq, on définit M subset F comme. The open inclusion is retained. M and family F follow their explicitly uncertain first occurrences.
- (1.20): compared both braces, every X, membership, family F, vertical separator, abbreviated str with raised t and point, irréductible and comma, the lower pour leq gloss, i.e., leq, capital Sup with lower i, both ordinary F_i, rightward implication, exists i, avec and final leq. The last leq is retraced; no deleted predecessor is added. H’s inline gloss layout is not counted as a textual discrepancy by itself.
- Following line: compared puis triangleleft par (1.17). The short canceled group was inspected separately from the live D’autre part, connaissant triangleleft on définit M par.
- (1.21): compared M, equality, braces, X membership family F, separator and X triangleleft X. Introductory line of (1.22): puis, pour ordinary F in family F, son deployement; the y descender and absent separate acute were checked at crop 08.
- (1.22): compared tilde F, equality, braces, X membership M, separator, X triangleleft and final collection F. Kept this literal terminal family symbol despite the tempting mathematical replacement.
- Final transition and display: read et enfin; compared F leq G, equivalence, both tildes and the open subset sign. Checked the label’s comma at crop 10.
- Bottom revision: compared Donc, pour déterminer, the complete canceled la structure, il est équivalent phrase, its above-line replacement les données minima|minimes qui, then fixent la structure d’atelier, il est indifférent d’y. Kept the page continuation open. No footer, date or archive pencil number was found.

## Doubts, mathematical check limits, and counts

- C has 10 distinct unsure loci on this page. All are individually accounted for in report.json; duplicate context-table references were not counted again.
- Actual images: 1 whole, 2 halves, 12 newly made crops, 12 crop views; 15 view events total.
- The report has 40 difference loci, 23 inventory elements and 6 remaining doubt loci. S.json is an empty array, so there are no S adjudications to confirm or overturn.
- Mathematical statements were followed and summarized, but not proved. The seven check events explicitly say that the author’s assertions were read as background without mathematical verification. Pure visual decisions are in the collation and above, not inflated into proof checks.
- The remaining limits are reduced cursive endings, a short heavily canceled group, and the typographic alphabet of recurring collection letters. The marginal crop was rotated approximately upright once; no additional rotation/crop search was performed.
- Structural checks are recorded below after output generation. No compilation or format-building attempt occurred.

## Structural verification result

- JSON parsed successfully; mandatory difference fields, controlled vocabularies, 10 C doubt rows, and all 23 inventory statuses passed.
- Braces balanced; 6 paired display delimiters; dollar delimiters even; environments properly paired and nested; commands restricted to the supplied/allowed set.
- Actual transcription marks: 6 unsure, 0 illegible, 3 deleted, 2 inserted, 1 diagram.
- No LaTeX compilation was attempted.
- reading.tex SHA-256: `6bc896026eb3315966ea05539f8c74ec06cffea8d0aa095c77727a0cda2a9a2d`.
- Completed 2026-11-20 11:35:09 UTC.

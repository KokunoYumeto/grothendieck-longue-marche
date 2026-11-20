# Scan 012 — independent reader R1 audit

## Scope and inputs

Read only the scan012 packet, the supplied current-page whole and two half images, PREAMBLE.tex, the authorized C PROMPT.md conventions, and the permitted crop helper. No other reader, other page image, consolidated decisions, external research, OCR, PDF text extraction, or LaTeX engine was used. S.json contains an empty list. The exact C PROMPT path was supplied during this run and read before making crops.

## Actual image-view sequence

Every image below was emitted through `tools.view_image`. The whole and each half were viewed once; none was enlarged or emitted again. Each new crop was emitted once. Times are UTC tool observations.

| # | Role | Image | Viewed UTC |
|---:|---|---|---|
| 1 | whole | `/workspace/scratch/42e661864e98/source/SP53_CW_156-6_scans/J156-6-02_156-6_scan012.jpg` | 2026-11-20 11:20:00 UTC |
| 2 | half_a | `/workspace/scratch/42e661864e98/source/SP53_CW_156-6_scans/J156-6-02_156-6_scan012_a.jpg` | 2026-11-20 11:20:06 UTC |
| 3 | half_b | `/workspace/scratch/42e661864e98/source/SP53_CW_156-6_scans/J156-6-02_156-6_scan012_b.jpg` | 2026-11-20 11:20:32 UTC |
| 4 | crop | `/workspace/scratch/42e661864e98/out/readers/scan012/R1/crops/01_diagram_frame.jpg` | 2026-11-20 11:22:28 UTC |
| 5 | crop | `/workspace/scratch/42e661864e98/out/readers/scan012/R1/crops/02_diagram_compatibility.jpg` | 2026-11-20 11:22:44 UTC |
| 6 | crop | `/workspace/scratch/42e661864e98/out/readers/scan012/R1/crops/03_slanted_correction.jpg` | 2026-11-20 11:23:25 UTC |
| 7 | crop | `/workspace/scratch/42e661864e98/out/readers/scan012/R1/crops/04_relation_start.jpg` | 2026-11-20 11:24:25 UTC |
| 8 | crop | `/workspace/scratch/42e661864e98/out/readers/scan012/R1/crops/05_family_f.jpg` | 2026-11-20 11:24:34 UTC |
| 9 | crop | `/workspace/scratch/42e661864e98/out/readers/scan012/R1/crops/06_element_word.jpg` | 2026-11-20 11:24:46 UTC |
| 10 | crop | `/workspace/scratch/42e661864e98/out/readers/scan012/R1/crops/07_remarques_initial.jpg` | 2026-11-20 11:25:00 UTC |
| 11 | crop | `/workspace/scratch/42e661864e98/out/readers/scan012/R1/crops/08_final_inequality_120.jpg` | 2026-11-20 11:25:05 UTC |
| 12 | crop | `/workspace/scratch/42e661864e98/out/readers/scan012/R1/crops/09_deleted_before_dautre.jpg` | 2026-11-20 11:25:19 UTC |
| 13 | crop | `/workspace/scratch/42e661864e98/out/readers/scan012/R1/crops/10_bottom_revision.jpg` | 2026-11-20 11:25:36 UTC |
| 14 | crop | `/workspace/scratch/42e661864e98/out/readers/scan012/R1/crops/11_de_plus_punctuation.jpg` | 2026-11-20 11:27:26 UTC |

The whole view established page number 11, the six-vertex implication diagram, its oblique frame, two main prose paragraphs, a long left slanted correction, (1.19), the underlined Remarques a), four further displayed formulas, and the revised concluding sentence. No independent drawing, date, archive pencil number, header/footer wording, or additional margin note was found.

## Open loci after the two halves

The halves settled the ordinary body text, most displayed signs and indices, the medial y in déployement, the family identity of the final F in (1.22), and the comma in (1,23). Their tight original-source boxes are recorded in report.json without creating crops for those settled loci.

The following remained open: the precise gaps in the diagram frame; the dense lower-right relation sign and adjacent retraced F; the coherent slanted correction (including membership, canceled start, missing words and punctuation); H’s alleged canceled Les before La relation; the affiliation of the curve after inserted de plus; the first family F’s alphabet; the compressed element word; capital versus lower-case Les after a); the state of the final inequality of (1.20); the short canceled group before D’autre; and the overlapping bottom deletion/insertion. These became eleven crops. The slanted correction was kept as one connected locus so that its line order and the affiliation of punctuation could be decided in the same rotated view. The neighboring bottom deletion and insertion similarly share one adequate crop.

## Crops and pixel transforms

All crop boxes refer to the original whole image, 1681 × 2361 pixels. Each image was cropped once, optionally rotated with BICUBIC resampling and white fill, autocontrasted, sharpened with UnsharpMask(radius=1.2, percent=120, threshold=3), then enlarged by LANCZOS and saved as JPEG quality 95. No evidence crop was recompressed, re-cropped or re-viewed.

| Crop | Original box (left, top, right, bottom) | Rotation | Output pixels | Purpose and decisive strokes |
|---|---|---:|---|---|
| `01_diagram_frame.jpg` | `[531, 340, 886, 724]` | 0.0° | 2800 × 3029 | Two white gaps at the left corners; top edge overruns the right edge. C’s closed cycle is changed; H is credited for observing the enclosure. |
| `02_diagram_compatibility.jpg` | `[809, 562, 965, 647]` | 0.0° | 2800 × 1526 | Four diagonal free ends plus an extra upright. Upright’s live/canceled history remains uncertain. Adjacent F has two upright tracks joining below; ordinary/retraced versus doubled alphabet remains open. |
| `03_slanted_correction.jpg` | `[18, 746, 620, 1320]` | -38.0° | 3400 × 3384 | Rotated coherent marginal note. Reads car, avoir, full relation, il faudrait écrire; resolves canceled F plus triangle; double underline beneath ou; no duplicate standalone lower formula. Membership’s upper mark remains open. |
| `04_relation_start.jpg` | `[235, 986, 579, 1084]` | 0.0° | 2800 × 798 | Live La relation and crossing strokes from the marginal note; no canceled Les. |
| `05_family_f.jpg` | `[519, 1067, 613, 1158]` | 0.0° | 2400 × 2323 | Swept cap, crossing middle arm, curled foot. Family identity clear; calligraphic/Gothic alphabet remains open. |
| `06_element_word.jpg` | `[1312, 1064, 1597, 1158]` | 0.0° | 2800 × 924 | Two acute marks and l are clear; reduced horizontal middle and terminal upright allow élémt/élément. Adjacent slashed oval and family subscript retained. |
| `07_remarques_initial.jpg` | `[526, 1379, 668, 1474]` | 0.0° | 2400 × 1606 | Tall straight capital L after a), followed by reduced es; reads Les. |
| `08_final_inequality_120.jpg` | `[1423, 1625, 1670, 1706]` | 0.0° | 2800 × 918 | Retraced live leftward inequality has an upper diagonal and two lower arms; no distinct canceled operand can be recovered. Reads X≤F_i. H’s descriptive surcharge note is credited. |
| `09_deleted_before_dautre.jpg` | `[255, 1783, 468, 1878]` | 0.0° | 2800 × 1249 | Very short canceled group above the live D; E and crossed upright favour Et, with En retained. Too short to be D’autre. |
| `10_bottom_revision.jpg` | `[877, 2138, 1673, 2264]` | 0.0° | 3400 × 538 | Minima/minimes reduced ending remains open; no tall l supports minimales. Canceled équivalent skeleton readable, possible acute overlaps inserted qui. |
| `11_de_plus_punctuation.jpg` | `[789, 941, 992, 1004]` | 0° | 2800 × 869 | Detached final small curve is s; next curve runs down into the insertion guide. No independent comma. |

The exact source paths, output paths, creation times and transforms are also in report.json/crop_log and the individual crop JSON sidecars. Crop 11 was made after resolving the neighboring crop set; it was the sole crop of the still-open insertion-punctuation locus.

## Line-by-line comparison against both witnesses

Consecutive uncontested manuscript lines are grouped below. Reading decisions were made from the emitted halves and, only for the open regions above, their single enlarged crops.

| Manuscript region | Comparison and decision |
|---|---|
| Top page number | 11, matching C and H. No other numbering at the head. |
| Diagram (1.18), upper vertex and middle row | G triangleleft F above G leq F; left G preccurlyeq F; right G parallel F. All letters, triangle, curved lower rule of preccurlyeq and arrow directions checked. |
| Diagram lower row and decorations | G ll F at lower left, G compatibility F at lower right. Five double implication arrows all descend. Frame gaps differ from C (D01). Dense sign and retraced final F carry local uncertainties (D02–D03). |
| Parmi les six relations … il y a quatre | Words and comma agree; no omitted qualification found. |
| relations d’ordre … et les | Four literal signs in order: triangleleft, leq, preccurlyeq, ll. Commas retained; the text’s claim is not corrected from the marginal objection. |
| deux autres relations … sont symétriques. | Parallel and the clean open zigzag sign are read. H’s between glyph does not preserve its geometry (D04). Terminal point retained. |
| Margin: Non … elle est transitive mais non réflexive, car | Rel. is abbreviated in the first sentence. Car is physically present and absent from H (D05). No expansion of rel. in the transcription. |
| Margin: first equivalence | Literal F triangleleft F iff F membership M. Upper mark near membership remains doubtful (D06); M font is first marked here (D07). No following point before Pour (D08). |
| Margin: Pour avoir une relation d’ordre | Avoir is readable where H has ill; relation is full here (D09–D10). |
| Margin: il faudrait écrire | Reads il faudrait écrire, replacing H’s locally aligned ill avoir écrit (D11). The phrase is an authorial qualification and is quoted in the notes. |
| Margin: crossed start and proposed definition | Canceled F triangleleft is resolved (D12). Live F trianglelefteq F has a single lower bar under the first triangle; déf over the double equivalence. Right side is F triangleleft F ou F=F, with F repeated literally throughout. Ou has two underlines (D13); terminal point recorded (D14). There is no second standalone copy beyond this definition (D15). |
| La relation … est | No canceled Les before the live La (D16). Clean compatibility zigzags retained (D17). |
| Inserted de plus and réflexive, mais | Insertion belongs after est. The following long curved stroke is its guide, not a comma (D18). Réflexive and the comma after it agree. |
| parallel ne l’est que si … est réduit à son seul | Apostrophes and reduced à checked. Family F gets its first local alphabet alternatives (D19). |
| element word, empty figure, car | Élémt/élément remains marked (D20). Empty figure is a slashed oval with a family F below (D21). Car sits on the next body line but is continuous prose. |
| (1.19) | F parallel F iff F = empty figure with family F below; figure vide. and its point are retained. Both outer Fs plain; subscript font follows first occurrence (D22). |
| Remarques a) Les relations … se déterminent mutuellement. | Heading has one underline. Capital Les is settled (D23); triangleleft and leq, reflexive se, and final point agree. No separate paragraph or item is omitted. |
| Connaissant leq, on définit M subset family F comme | Open subset sign has no lower rule; local M and F forms recorded (D24). |
| (1.20), left and middle | M={X in family F vertical bar X …}; family letters inspected locally (D25). Baseline str with raised t and point, not expanded strict. (D26). Irreductible word and the below-baseline pour leq remain in their layout. |
| (1.20), implication and final line | Comma and i.e. retained. X leq capital Sup_i F_i implies exists i avec X leq F_i. Capital S differs from H sup (D27). Three indices (one below Sup and two F subscripts) are i; quantified i is also dotted. Closing brace present at right edge. Crop 08 finds retracing, not a readable canceled operand. |
| puis triangleleft par (1.17). | All tokens, parentheses and point agree. |
| canceled opening; D’autre part, connaissant triangleleft on définit M par | Short canceled Et/En retained, not H D’autre (D28). Live D’autre part follows. Local M alphabet recorded (D29). No extra comma after connaissant clause is supplied. |
| (1.21) | M={X in family F vertical bar X triangleleft X}; all Xs, vertical separator and braces checked. Recurring alphabet choices recorded (D30). |
| puis, pour F in family F, son déployement | Two distinct F forms (D31). The long descending y settles déployement against modernized déploiement (D32); commas kept. |
| (1.22) | Separate wave over ordinary F; equality and set braces. X in M vertical bar X triangleleft family F. M choice recorded (D33). Last glyph’s turned foot resolves family identity (D34); H’s explicit literal-reading note is credited, so this alone is not marked against its physical reading. |
| et enfin; (1,23) | F leq G iff tilde F subset tilde G. Both overmarks are waves, open inclusion has no lower rule. Low separator after 1 is a comma (D35), not normalized to the other labels. |
| Donc, pour déterminer … | Opening wording and comma agree. The crossed phrase remains deleted. |
| bottom deletion and replacement | Deleted la structure, il est équivalent/equivalent; word identity legible, accent unresolved (D36). Inserted les données minima/minimes qui; no tall l for H minimales (D37). Placement is before the live fixent. |
| fixent la structure d’atelier, il est indifférent d’y | Ordinary concluding wording and apostrophes retained. Last word group is d’y, not H de s’y (D38). The sentence is unfinished at the page edge; nothing is supplied from a following page. |

## Doubts, inventory and mathematical limits

All ten distinct C doubt loci are individually covered in report.json: four resolved (canceled F plus triangle; déployement; family identity of final F in (1.22); comma label) and six retained (membership mark; first family alphabet; élémt/élément; Et/En; accent in equivalent; minima/minimes). Duplicate C-context rows were not counted twice.

The final transcription has nine unsure macros, zero illegible macros, four deleted macros and two inserted macros. One deleted macro occurs only in the explicitly uncertain alternative for the extra diagram upright; it is not an assertion of four certain cancellations. There are nine unresolved loci in the report, and all 24 inventory elements have transcribed=yes.

The mathematics was followed for parsing and for distinguishing literal symbols from tempting repairs. In particular, no G was substituted for F in the marginal definition, no ordinary F was substituted for the final family F in (1.22), and the initial order-relation claim was retained alongside its authorial correction. No proof, re-proof, computation or formal certificate was performed. The four check_events record assertions carried as background and explicitly say no mathematical verification was performed.

No additional crop or repeated view was used to force resolution of the remaining doubts. The main limitations are the finite scan resolution, black cancellation, and interleaving of slanted note strokes with the main text. The exact typographic alphabets are underdetermined by handwritten forms, so first-occurrence alternatives remain explicit.

## Structural validation

Passed: UTF-8 JSON parse; all required report collections present; unique difference IDs; allowed difference kinds, confidence values, H doubt marks and check-event categories; all evidence paths exist; all inventory entries are complete; eleven JPEG crops and fourteen logged image emissions.

Passed: balanced unescaped braces, six display-math delimiter pairs, even inline dollar count, correctly paired tikzcd and aligned environments, and macro allowlist. No new notation macro is defined. No LaTeX compilation or engine-format creation was attempted.

Actual totals: 1 whole view + 2 half views + 11 crop views = 14 image emissions; 11 new crops; 38 substantive difference rows; 10 C doubt loci; 0 S rows; 24 inventory elements; 9 unresolved loci.

Finished: 2026-11-20 11:35:56 UTC.

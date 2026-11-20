# Scan 009 — independent reader R1 audit

## Scope and sequence

I read only the assigned scan 009 brief, inputs.json, C.tex, H.tex, C_context.md, S.json, notation.md, the two named preambles, and the three named scan images. C and H were treated as unverified drafts. No other page or reader material, OCR, text extraction, external research, or proof source was consulted. No subagent was spawned.

The whole image was emitted once for layout, then half a and half b were each emitted once for line-by-line reading. The supplied whole image measures 1682 × 2361 px; half a measures 1682 × 1260 px; half b measures 1682 × 1261 px. Half b begins at whole-image y = 1100. All crop boxes below refer to the whole-image source, not to a scaled display or half-image coordinate system.

| UTC | Emitted image(s) | Purpose |
|---|---|---|
| 10:01:58 | whole scan 009 | Layout: page number 8, opening prose, one implication, a tall right-hand column for (1.13), corrections, final unfinished paragraph. No independent marginal note, drawing, or diagram. |
| 10:02:05 | half a | First line through the opening of the middle correction, compared against C and H. |
| 10:02:41 | half b | Overlapping middle paragraph through the last word relation, compared against C and H. |
| 10:04:35 | crops 01–03 | Family alphabet; right-column prose/edge; abbreviation punctuation. |
| 10:05:12 | crops 04–06 | om/omb; élément/élt; lieu commun(s). |
| 10:05:51 | crops 07–10 | tout; layered correction; article/theory correction; live tout and lieu. |
| 10:06:44 | crops 11–15 | Lower canceled fragments, ateliers ending, final punctuation, barred m. |

Every listed view was actually emitted through the image tool. There were **15 actual crops**, each generated and emitted once. No whole image or half was emitted a second time, and no crop was re-cropped or re-viewed.

## Open loci after the halves

The halves settled the manuscript number, main opening wording, the single underline, ordinary G in the first implication, its final point, the attribution “On a, par les axiomes:”, the absence of =∅ from the crossed expression, the final literal om(G), the added sous-, the omitted tjrs in H, and the overall sequence of the paragraph. Coordinates are supplied in report.json for discrepancies settled without crops.

Remaining local issues were: printed alphabet for the family F; the short word before sens; terminal disjoint(s) at the right paper edge; points in i.e.; the b question in the live equality; full élément against abbreviated élt; lieu and commun(s) endings; tout against a quantifier-like glyph; com/co inside the upper correction; the exact la/l’ correction; whether the later tout is crossed and whether its following noun has x; dis/disj; en de/en des; cancellation versus retracing in ateliers; an apparent final point after ensembliste; and barred m against equality. Adjacent issues within a single short region were handled in one crop (02, 05, 06 and 10), without making duplicate crops of a locus.

## Crop transforms and decisions

All crops use Pillow only: crop the specified original-pixel box, rotate 0°, autocontrast with 0.2% cutoff, UnsharpMask radius 1 / percent 130 / threshold 2, and LANCZOS enlargement to 3000 px across. They are saved as JPEG quality 95 with no chroma subsampling. No existing crop was recompressed. The complete machine-readable transform and decisive-stroke records are in crop_manifest.json.

| Crop | Original box (left, top, right, bottom) | Output px | Decision / remaining limit |
|---|---|---|---|
| 01_family_F | [566, 57, 950, 180] | 3000 × 961 | F identity clear; calligraphic/fraktur alphabet remains uncertain. |
| 02_rhs_sens_plural | [1010, 555, 1682, 669] | 3000 × 509 | One short au before sens; no en un. Final disjoint(s) remains edge-limited. |
| 03_ie | [1497, 655, 1647, 710] | 3000 × 1100 | Separate medial and final points support i.e. |
| 04_live_ombre | [988, 707, 1649, 785] | 3000 × 354 | No b between m and opening parenthesis: om(G). |
| 05_element_elt | [987, 774, 1672, 896] | 3000 × 534 | Full upper élément; short later élt. No raised t in the upper word. |
| 06_lieu_communs | [942, 1081, 1525, 1180] | 3000 × 509 | Singular lieu; communs/commun retained as uncertain. |
| 07_tout_left | [234, 1220, 693, 1320] | 3000 × 654 | Letter components and local crossbar pattern support tout, not a single quantifier. |
| 08_disjoint_com | [1155, 1158, 1440, 1315] | 3000 × 1653 | Canceled com beneath live inserted disjoint; lower disjoint also canceled. |
| 09_la_theorie | [528, 1300, 1188, 1408] | 3000 × 491 | Retained l, canceled a, added apostrophe, canceled théorie, live atelier. |
| 10_tout_lieu | [1200, 1300, 1665, 1415] | 3000 × 742 | Tout crossbar is live; noun has no x. |
| 11_dis_compat | [236, 1624, 744, 1745] | 3000 × 715 | Canceled disj/dis remains ambiguous at the live-word boundary. |
| 12_sous_ensembles | [1045, 1716, 1620, 1840] | 3000 × 647 | Readable en des/en de under the strike; sous- clearly inserted. |
| 13_ateliers | [552, 1923, 840, 2037] | 3000 × 1188 | Live ateliers clear; older er/ers deletion versus retracing unresolved. |
| 14_ensembliste_punctuation | [523, 2259, 1010, 2355] | 3000 × 591 | Apparent dot is final e; no separate punctuation before et. |
| 15_bar_m | [971, 2256, 1397, 2355] | 3000 × 697 | Curved lower m and separate bar; not equality, no quotes around modéré. |

## Line-by-line comparison

| Manuscript region | Comparison and result |
|---|---|
| Opening two prose lines | All words, empty-figure subscript, punctuation and the single underline on figure vide read. C/H differ in alphabet; first family F is explicitly uncertain. No doubled family F is inferred. |
| First implication | F/G pair, disjoints, double-line rightward implication, compatibles and terminal point read. C’s G/C doubt is resolved to G; C’s missing point is restored. |
| Attribution line | “On a, par les axiomes:” is read directly, including comma and colon. This is the local evidence for S; no extra crop made for a settled line. |
| (1.13), top intervention | Canceled tout; replacement omb(F) et omb(G) above the canceled intersection. H’s supplied =∅ is absent from the canceled line. The label and two-headed equivalence were read. |
| (1.13), next two prose lines | “sont ''disjoints'' au sens suivant: ils sont …” read; H’s en un has too many words. The final disjoint(s) is explicitly unresolved because of the edge. Quotation marks and colon are included. |
| (1.13), ensemblistement/equality | i.e. punctuation checked; live omb(F) ∩ om(G)=∅, et read literally, retaining the b asymmetry. |
| (1.13), last three lines | tout élément de omb(F) est / compatible avec tout élt / de om(G). C’s two word-form doubts resolved. H’s b and extra terminal parenthesis on the last line are not supported. |
| Explanation, first two lines | — i.e. deux figures sont disjointes ssi elles n’ont pas de lieu commun(s), et. Singular lieu is clear; terminal commun(s) is marked uncertain. |
| Explanation, next line and correction | tout lieu de l’une est; original disjoint canceled, aborted com canceled above it, live replacement disjoint. C’s tout/quantifier and com doubts are resolved; H’s co is too short. |
| Explanation, parenthesis and ending | (au sens de l[deleted a][added apostrophe][deleted théorie]atelier) de tout lieu de l’autre;. The initial l is shared, without a second l. Later tout is live and later lieu lacks x. Semicolon is included. |
| Cela paragraph, first two lines | Cela montre que les relations de [deleted disj/dis]compatibilité et de disjonction sont. Canceled prefix remains uncertain. |
| Cela paragraph, following two lines | importantes aussi dans les [deleted en des/en de][inserted sous-]ensembles M,L de F. Dans le. H omits sous- and leaves the canceled word group wholly illegible; readable candidates are supplied with uncertainty. |
| Set-theoretic case | cas des ateliers ensemblistes, ces relations sont “triviales” sur L: deux lieux sont tjrs [deleted disjoints][inserted compatibles], et disjoints ssi ils sont distincts. Ateliers intervention is explicitly uncertain; tjrs, omitted by H, is included. The comma, quotes, colon, and full stop were read. |
| Final lines | Par contre, même dans le cas ensembliste et barred-m modéré, la relation. The seeming point after ensembliste is its final e; barred m is not equality. H’s quotes around modéré are absent. The sentence remains unfinished without an invented final point. |

All 13 C doubt loci, including repeated listings of the same locus in the packet, are accounted for once in c_doubts: 9 resolved, 4 retained. The final reading has 6 unresolved loci: the 4 retained ones plus the family alphabet and commun(s). No unrecorded gap or formula-symbol illegibility is used.

## Mathematics, S, and limits

S row SA21-K6-07 is **partly confirmed** only in the precise sense that the page really attributes (1.13) to the axioms and states the displayed condition. Its countermodel and proposed restriction to At 9 are claims about material outside this page. They were not checked, and no correction from S was inserted into the reading. The uncropped attribution-line coordinates are [258, 401, 1121, 479] in the whole-image source; the numbered display is [230, 475, 1680, 980].

The page was followed mathematically as a definition, implication, asserted equivalence, verbal paraphrase, and set-theoretic example. This was **not a proof check**. The four check_events are only background carriage, each explicitly stating that no mathematical verification was performed. The sole authorial justification phrase is “On a, par les axiomes:”; there is no explicit authorial doubt/check request.

The most material limits are the right-edge disjoint(s), highly compressed terminal commun(s), and heavily crossed lower fragments. They remain marked in reading.tex. Ateliers is not forced into a definite deletion history merely because its end is darkly retraced. No external image or expected mathematics was used to remove these uncertainties.

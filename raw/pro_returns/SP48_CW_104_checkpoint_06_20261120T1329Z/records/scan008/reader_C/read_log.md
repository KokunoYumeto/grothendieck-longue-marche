# Scan 008 — independent Reader C register

## Inputs and view discipline

Read `briefs/brief_v07_scan008.md`, `PREAMBLE.tex`, and `briefs/notation_before_scan008.md` before opening an image. Read only the authorized scan008 packet (`C.tex`, `H.tex`, `C_context.md`, `page.json`). No H drawing packet was supplied. No other page or reader output was consulted. The initial attempts to prefix the packet/image paths with `SP48_CW_104` failed; those failures occurred before any image delivery.

The whole image was viewed once for page layout and all handwritten blocks. Half a was then viewed once and half b once. Their dimensions were read as 1691 × 2373, 1691 × 1266 and 1691 × 1267 respectively. Sixteen unresolved loci were cropped from the whole image, each saved and viewed once. There were no image-delivery failures or redeliveries. All crop boxes, actual output sizes and processing are in `crop_metadata.json`. All rotations are 0°. Processing was Pillow crop, autocontrast with cutoff 0, and LANCZOS enlargement to 2600 pixels wide; no sharpening was applied.

## Line and element register

| Source order | Checked observation and result |
|---|---|
| Opening | `De plus, se rappelant la definition de`. C has the correct wording; H adds an absent `on`, a cancellation and a different inflection. Crop 01 resolves the first e as unaccented. |
| First display | `J_n = D-tilde_n = ens des sous-objet de D_n`. J’s low hook, the separate tilde, both equals signs, D indices and every word were checked. H’s I and abbreviation stop disagree. Crop 02 resolves no final s on sous-objet. |
| Application introduction | `on a, pour forall n in N, une application canonique, strictement croissante`. C agrees with the visible words and comma after canonique. H has a different opening and repeats croissante. No comma follows the final croissante. The N returning stems and quantifier were examined. |
| Type map and caption | Right-directed arrow from J_n to doubled N, tau_n above it. The side caption repeats tau_n and has two opening ticks before type; no closing pair or enclosing parentheses is visible. C is retained. |
| Image sentence | `dont l’image est formée`, crossed `des`, `de l’ens`. Crop 03 resolves the separate final e in formée. H’s fournie/dans differ. No stop follows ens. |
| Set-description line | The old `I_{≤n} des` is crossed together. The live doubled `N_{≤n}={n’ in N | n’≤n}` has both braces, both lower indices, a high prime and a terminal point. C agrees with the formula. H misclassifies des as an insertion. Crop 14 confirms a detached point between the deleted phrase and the live N; it is traced without assigning function. |
| Largest object paragraph | `Notons que chaque J_n a un plus grand élément, qui est` was checked word by word. The q descender supports chaque, against H’s doubtful déjà. The quoted D_n has opening ticks only. |
| Parenthetical description | Crop 04 resolves `en tant`, and confirms raised `le` with its caret before sous-objet. The remainder `sous-objet maximal de D_n` and closing parenthesis agree with C. H’s wording and un differ. |
| Naming phrase | Crop 05 leaves the live/canceled history unresolved. The visible descender favors `que je note`, while the C old est/il and on/on y alternatives remain explicitly available in the combined in-place uncertainty. Both earlier C doubts are retained rather than silently discarded. |
| Reference and equality | Raised `(par (ii))` has a leader to the end of `On a donc`. The next display is `tau_n^{-1}(n)={d_n}`; minus, 1, parentheses, braces and lower-case d were all checked and agree with both witnesses. H does not mark the raised reference as an insertion. |
| Canceled Si line | The full sentence `Si n’≤n, alors pour tout x in J_n` is struck. J is hooked. No final period can be isolated; C’s period is removed. H has I. |
| Soient line | `Soient n,n’ in N,` is live. The following main x/J/tau equation and terminal on are canceled. Crop 06 leaves the smaller upper canceled `x in J / x in` unresolved. |
| Raised condition | `avec n’≤n` is written above the discarded material and has no following comma. The placement is preserved as an insertion. |
| Considérons and next deletions | Crop 07 resolves live considérons, with one occurrence only. It resolves the next deleted group’s start as via, but leaves the opening-parenthesis question in via x/via (x). The following `on a alors une/un application` is all canceled; une/un remains uncertain. |
| First Hom map | Crop 08 preserves the old O/D overlap at the first argument, resolves the second D as plain, and confirms the two-row layout. The hook arrow points right to `D-tilde_n=J_n`. The lower `u mapsto u(d_{n’})` is beneath the arrow/target; d is lower-case and the index prime is high. No comma follows the upper J. |
| Bijection sentence | `qui est une bijection des Hom sur l’ens tau_n^{-1}(n’), et considérons` was checked in full. Both witnesses otherwise agree here; H adds a stop after ens. |
| Second Hom map | Crop 09 retains underlying D/O uncertainty and reads the tiny elevated mark as 4/asterisk, independently of the clear lower n-prime. The target Hom has two tilded D arguments with square-ended low brackets and J labels beneath; every label/index was checked in half b. H’s actual formula omits these annotations, although its prose note partly describes them with I. |
| Detached lower-right marks | Crop 15 confirms two discrete dark points, the upper farther right. They are preserved as a literal small trace without semantic attribution. |
| Deduced application | `on en déduit une ... application` agrees outside the deletion. Crop 10 favors the incomplete crossed bijec, with bi ce/bi se retained because the middle strokes overlap. The entire descending curve and cancellation contour are included. |
| Definition line | `tau_n^{-1}(n’) =def J_{n’,n}` was checked for every index, prime and bar. def has no acute. Crop 11 confirms both low indices are live and leaves the adjacent canceled `(n’)/(n)` unresolved. H instead cancels the second index. |
| Left lower annotation | Crop 12 shows a wavy left vertical strand and straight right strand, represented by a 90° rotated simeq. The tall square brackets enclose both that relation and Hom below. The annotation sits under the left inverse-image term. C’s straight equality and small brackets are amended; H’s note describes the wrong side and does not draw the structure. |
| Lower type annotation | The square-ended bracket, `ens des / éléments / de J_n de / type n’`, and their attachment were checked. C agrees; H’s prose has une and I. |
| Rho arrow and element map | The label is rho_{n,n’}, not H’s varphi. The target is `Hom(J_{n’},J_n)`. The word before the element map is unaccented ou, resolving C’s doubt. Crop 16 confirms xi at left and as the compressed index of u, with separate superscript n. The mapping formula otherwise agrees with both. |
| Injectivity sentence | `qui est injective, plus précisément on a la ...` was checked. There is no added ou before plus and no de after the final noun. Crop 13 leaves commutativité/commutativite unresolved because the last elevated trace is faint. |
| Final diagram | C’s entire existing TikZ was checked: J_{n,n’} at left; rho_{n,n’}; Hom(J_{n’},J_n); right arrow with u mapsto u(d_{n’}); J_n at right; and the low open curve labeled inclusion. The first J index pair is n,n-prime, distinct from the definition’s n-prime,n. The lower connector has a left inward curl, detached ends, a label interruption and no arrowhead. H’s lower arrowhead is unsupported. |
| Number and sheet | Bottom-left 7 is recorded as archive numbering. There is no title/date or own folio at the top. The sheet is handwritten text; faint background traces do not establish typed reuse or additional recoverable words. |

## Crop results

| Crop | Target | Result |
|---|---|---|
| 01_definition | First e accent | Resolved: definition, no accent. |
| 02_sous_objet | Terminal plural | Resolved: sous-objet, no separate s. |
| 03_formee | Final e | Resolved: formée. |
| 04_en_tant | Crowded parenthesis and raised le | Resolved en tant; insertion confirmed. |
| 05_quon | Phrase before note | Unresolved history; que je favored, C rewritten alternatives retained. |
| 06_old_x | Upper canceled group | x in J / x in retained. |
| 07_considerons | Live ending, via group, lower cancellation | Considérons resolved; via start resolved; parentheses and une/un retained. |
| 08_first_Hom | Overlap, D alphabet, map placement | Old O/D retained; second D plain; two-row layout confirmed. |
| 09_second_Hom | Old D/O and high mark | Old D/O retained; high mark 4/asterisk, prime excluded. |
| 10_old_bi | Full canceled fragment including descender | Bijec favored; bi ce/bi se retained. |
| 11_lower_J | Indices and canceled parentheses | Both indices live; canceled n-prime/n unresolved. |
| 12_vertical_relation | Curved relation and enclosing brackets | Resolved literal wavy-left/straight-right relation; brackets enclose both levels. |
| 13_commutativite | Final e/accent region | C accent alternatives retained. |
| 14_point_after_des | Isolated point | One point confirmed; unassigned role. |
| 15_points_after_map | Right-side pair | Two detached points confirmed; unassigned role. |
| 16_xi_subscript | Small index of u | Xi reading confirmed. |

## Consistency and limits

`reading.tex` was compared once against C as text after the images. All amendments in that diff are covered in `report.json`, including uncertainty resolutions, the deleted Si period, the revised vertical relation/enclosure and detached-point traces. Retained C doubts are separately recorded. Every substantive H difference is recorded, including those where C remains the better reading. Equivalent macro syntax was not counted as a difference.

No OCR, web research, external parallel text, compilation, rendering or mathematical proof/computation check was performed. `checks` is therefore empty. The reported mathematical claims are observations of the manuscript, not verified theorems. No image was reopened for the final consistency pass.

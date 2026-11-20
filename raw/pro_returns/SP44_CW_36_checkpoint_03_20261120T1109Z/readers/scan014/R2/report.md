# Scan 014 — independent reader R2

## Scope and time

- UTC start (first recorded clock reading): **2026-11-20T10:12:14Z**.
- UTC end: **2026-11-20T10:28:35Z**.
- Page read: scan 014 only, manuscript page **5**, archive sheet **13**.
- Inputs read in full: `briefs/brief_v05_scan014.md`, the exact `PREAMBLE.tex` named there, and `packets/scan014/packet.md` (C, H, C doubts/notes and frozen notation). I did not inspect another page, another reader's files or another reader's return.
- No OCR, text recognition, web source, published transcription, LaTeX compilation or mathematical restoration was used. Source-image dimensions and my own crop metadata were read without reopening their pixels.

## Actual visual sequence

1. `A36-01_36_scan014.jpg`, viewed once with `view_image`, for layout. It established a typescript with three main prose units, two separate displayed formulas, typed interlinear insertions, several extensive machine cancellations, pen underlines/signs, manuscript page 5 at upper right and archive 13 at lower left. There is no independent diagram or drawing.
2. `A36-01_36_scan014_a.jpg`, viewed once at supplied resolution. I read the entire half against both witnesses.
3. `A36-01_36_scan014_b.jpg`, viewed once at supplied resolution. I read the entire half, including the overlap, against both witnesses. Its whole-image vertical offset is 995 pixels.
4. Sixteen distinct crops, all created by the supplied helper with `--scan 14 --reader R2`, then actually inspected once each with `view_image`. They were viewed in the order listed below. No crop was recreated or reopened. No whole half was enlarged or reopened. No viewer delivery was truncated.

The whole page is 1679 × 2150 pixels; each half is 1679 × 1155 pixels. All boxes below and in the JSON use **whole-image coordinates**. The helper metadata records autocontrast, LANCZOS resizing and `UnsharpMask(1,110,3)`, saved as JPEG90. All crops have width 2500 except `top_close`, width 2300. Only `k_note` was rotated, by +2° to reduce the slant.

| Crop, relative to the work directory | Whole-image box | Rotation |
|---|---|---:|
| `crops/scan014/R2/cancelled_upper.jpg` | `[205, 270, 1605, 397]` | 0° |
| `crops/scan014/R2/da_classe.jpg` | `[923, 479, 1250, 548]` | 0° |
| `crops/scan014/R2/first_class.jpg` | `[575, 545, 1154, 626]` | 0° |
| `crops/scan014/R2/inline_class_cancelled.jpg` | `[365, 674, 1320, 815]` | 0° |
| `crops/scan014/R2/proof_define.jpg` | `[380, 971, 915, 1045]` | 0° |
| `crops/scan014/R2/proof_curve.jpg` | `[1018, 1110, 1250, 1200]` | 0° |
| `crops/scan014/R2/product_one.jpg` | `[1190, 1182, 1515, 1269]` | 0° |
| `crops/scan014/R2/product_two.jpg` | `[1030, 1260, 1235, 1342]` | 0° |
| `crops/scan014/R2/construction.jpg` | `[380, 1464, 737, 1538]` | 0° |
| `crops/scan014/R2/k_note.jpg` | `[1296, 1603, 1558, 1704]` | 2.0° |
| `crops/scan014/R2/last_display.jpg` | `[560, 1826, 867, 1923]` | 0° |
| `crops/scan014/R2/fibres_mark.jpg` | `[342, 1897, 507, 1981]` | 0° |
| `crops/scan014/R2/hyperplanes.jpg` | `[855, 1912, 1125, 1984]` | 0° |
| `crops/scan014/R2/base_S.jpg` | `[1340, 1912, 1577, 1995]` | 0° |
| `crops/scan014/R2/final_map.jpg` | `[1270, 1995, 1678, 2092]` | 0° |
| `crops/scan014/R2/top_close.jpg` | `[1526, 196, 1667, 271]` | 0° |

## Compact line-by-line coverage

Source lines are identified by their approximate whole-image y positions. Each entry includes ordinary prose, punctuation and the inline symbols on that line, not only the disputed words. A source line break was not promoted into a new paragraph. The proof's indented opening and the separated numbered section 4 are preserved as paragraphs; both separately positioned formulas remain displays. The final restriction formula remains in its prose line.

| Source locus | Coverage and result |
|---|---|
| Top insertion, y 78–145 | Read `a) et b) vérifiés pour le morphisme`, i with barred-s subscript, colon, **X** with barred-s subscript, right arrow, second **X** with barred-s subscript, and `induit`. Typed letters and pen placement guide are distinguished. Both X readings were settled on half a. |
| Main line, y 135–187 | Read literal `Onnsuppose`, the cancelled `que le morphisme induit`, `pour lesfibres en`, barred s, and opening geometric-point parenthesis. The extra n and joined lesfibres remain. |
| Main line, y 204–266 | Read cancelled `fixé`, `de S`, cancelled comma and `qu'on a intérêt à prendre`, `au dessus da point`, fully underlined `générique`, `de S)`. The separate terminal stop was settled by `top_close`. |
| Cancelled line, y 276–329 | Read `si S est irréductible pour avoir le maximum de chances de ... que` through x-outs. The `pouvoir/pourvoir` locus remains uncertain after its single crop. |
| Cancelled/live line, y 339–396 | Read `l'hypothèse sérieuse b). Soit z un cycle a` beneath cancellation, raised typed `Soit`, then live z, pen membership, Z raised n, `(Y)`, and `tel que le cycle`. |
| Main line, y 415–473 | Read `induit sur Y` with barred-s subscript, `soit algébriquement équivalent à zéro, et à fortiori`, including the accent and source `à`. |
| Main line, y 485–538 | Read `cohomologiquement équivalent à zéro. Donc ...a classe`. The first letter of the article has a d/l overprint; its possible orders remain explicitly uncertain. |
| First display, y 544–626 | Read u(z), pen membership, H raised 1, S, R raised 2n−1, f with lower pen star, underlined Z, crossed coefficient subscript, `(n))`. Two actual terminal closings are retained. |
| Main line, y 632–697 | Read `est définie. Ceci posé, je dis que`, underlined `cette classe est`, and cancelled `une classe de torsion` within the ruled span. H's note recording the cancelled words is credited. |
| Main line, y 674–752 | Read underlined `contenue dans`, i with pen star, H with cancelled old round degree and live 1, S, R raised 2n−1, overwritten direct-image g, lower star, overwritten/uncertain coefficient and crossed subscript, then underlined `modulo une classe de torsion`, comma and `du`. The inline group ends in three closings. |
| Interline, y 721–789 | Read typed and cancelled `On applique 2) à i` with a barred-s subscript. Crop settled the presence of that subscript. |
| Condition line/interline, y 751–812 | Read `moins si on`, cancelled `suppose S japonais de dimension 1, ou même`, separate cancelled raised `si,`, and live `se permet de`. |
| Main line, y 815–881 | Read `remplacer S par un ouvert non vide(restriction`, cancelled `sans doute`, raised typed `probablement`, `inutile, mais`. No extra paragraph is inserted. |
| Main line, y 870–910 | Read `cet énoncé nous suffira pour ce qu'on veut en faire).` |
| Proof opening, y 916–975 | Read `Pour le voir, on applique 2) au morphisme i` with barred-s subscript, period, `La courbe C et`. |
| Proof line, y 983–1045 | Read `le cycle Z'' peuvent`, overlapping d/s plus e, literal `définit`, `déjà sur une extension finie K de k(s),`. The two prime strokes, terminal t and capital K are retained. |
| Proof line, y 1058–1119 | Read capital `Un argument de trace permet de supposer que K=k(s), et`, then cancelled `quitte à prendre`. |
| Proof line, y 1127–1189 | Read cancelled `l'adhérence du cycle`, `on peut supposer que`, the overlapping curve capital, cancelled `et Z`, and `est une courbe propre`. |
| Proof line, y 1197–1267 | Read `et lisse relative sur S lui-même, et Z'' un cycle sur`, first overprinted product capital, literal baseline x with lowered S, C, comma, cancelled `Alors`, and `et que`. |
| Proof line, y 1267–1337 | Read `la formule z=i*(z')+z'' est valable sur`, the second overprinted product and its baseline x, period, `Elle implique une`. The star is pen. |
| Proof line, y 1340–1403 | Read `décomposition analogue de u(z), qui est la somme de i*(u(z')) et de`, with all nested brackets and the pen star. |
| Proof line, y 1410–1475 | Read `u(z''), de sorte qu'il suffit de prouver que u(z'') est nul. Or u(z'')`. |
| Proof line, y 1480–1554 | Read `induit par`, the overwritten initial of `construction 2)`, `l'homomorphisme nul`, H raised 1 on C with barred-s, right arrow, H raised 2n−1 on Y with barred-s, period, and literal `Im`. |
| Proof line, y 1552–1605 | Read `résulte donc bien de 1) que u(z'') est nul, cqfd.` |
| Section 4 addition, y 1603–1704 | Read pen `sur k Alg. clos,`; terminal pen comma survives, as does the original typed comma after m. No cancellation of that typed comma is invented. |
| Section 4 line, y 1642–1706 | Read `4. Soient X un schéma projectif et lisse de dimension m, prenons`. The plural `Soient` is visible and is not grammaticalised. |
| Section 4 line, y 1710–1768 | Read `un pinceau de Lefschetz, de façon à obtenir une variété éclatée non`. |
| Section 4 line, y 1781–1827 | Read `moins projective et lisse X` with separate pen tilde, `et un morphisme`. |
| Last display, y 1826–1923 | Read typed f and X with separate pen tildes, colon and right arrow, cancelled S plus an additional visible x-out cell, then ordinary P raised 1 and lowered k. |
| Bottom line, y 1903–1989 | Read `dont les fibres sont les sections hyp[extra cancelled é]erplanes du pinceau. Soit [base] un`. The b has a retouched/extended ascender; the cancelled extra letter has a detached acute. The base capital remains B/S/U/doubled-S uncertain. |
| Bottom line, y 1995–2086 | Read `ouvert non vide de P^1_k au dessus duquel X` with pen tilde, `soit lisse, et soit`, final j/f, colon, `Y=`, X with tilde, restriction stroke, repeated base glyph, right arrow, clipped pen S-like target and final stop. The formula stays inline. |
| Page furniture | Manuscript 5 is in `\handwritten{\mspage{5}}`; archive 13 appears only in a comment. No omitted independent margin annotation or diagram was found. |

## Complete comparison and inventory

The complete comparison is in `result.json`: **45 separate locus rows**, each with C, H, final reading, separate against flags, specific ink observations, evidence path, whole-coordinate box and mathematical consequence. Its full inventory contains **73 items**, covering every prose block, separate display, substantial inline formula, individual cancellation, insertion, pen sign, underline and page number. The report does not substitute an amendment list for the page: `reading.tex` contains the complete diplomatic reading.

Counts are **23 against C** and **38 against H**. These include C-doubt resolutions as required by v05; a confirmation that resolves C's alternative can therefore be against C even where its first textual candidate is retained. There are **24 C-doubt rows**, and **15 unresolved items**, matched one for one to in-place doubt markers. No mathematical check event was claimed.

H's remarks about cancelled text, the overwritten open-base letter and the partly retraced final line are treated as witness evidence. H's global chi-shaped-ell convention and its emphasis convention are credited: differences of macro vocabulary, bold versus ordinary underlined coefficient house type, and absent handwriting wrappers alone are not counted as H errors. The two baseline product x signs are separate actual glyph differences, as required by the brief.

### C doubts and earlier notes: disposition

| C item | Disposition / comparison row |
|---|---|
| `Onnsuppose`; `lesfibres`; `da point` | Settled from half a in favour of the literal forms: 01, 04, 07. |
| Top `X_sbar -> X_sbar` | Both X capitals confirmed on half a: 02. H's note already acknowledges them. |
| Cancelled `pouvoir que / pourvoir que` | Both candidates remain after `cancelled_upper`: 09. The rest of the two cancelled lines is transcribed, rather than wholly unreadable: 09–10. |
| `da classe / la classe` | The extra round component and ascender favour an actual d/l overlap. Both temporal orders are retained: 11. |
| First coefficient / missing display parenthesis | Underlined ordinary Z confirmed; crossed subscript retained with chi/ell doubt and changed source-layer assessment: 12. Two closing curves confirmed, no completion: 13. |
| Inline old H degree | Uncertain old 0 retained: 14. |
| Inline old direct-image f/g | Uncertain old f/g retained with live pen g: 15. |
| Inline Z/Q | Possible Q-over-Z structure added as preferred candidate, with Z and Q alternatives retained: 16. |
| Cancelled insertion `i_sbar / i` | Barred-s subscript resolved as present: 20. |
| Overlaid curve capital | Outer C curve and diagonal justify uncertain C/Z overprint orders; doubled C remains an alternative: 26. |
| First product capital | C's doubled-X/X/Y uncertainty remains: 28. |
| Second product capital | Y-like fork/stem plus lower X strokes; uncertain overprint orders retained: 31. |
| `construction` old d | Old d remains uncertain: 33. |
| `peuvent de définit / se définir` | d/s overlap is marked structurally: 23. Final t in `définit` is confirmed: 24. |
| `Im / Il résulte` | Two m shoulders confirmed on half b: 34. |
| `Soient / Soit X` | Complete `Soient` confirmed on half b: 35. |
| Last display cancelled S/Sx | S plus a separate visible x cancellation cell retained: 38. The x is not asserted as an old lexical symbol. |
| Cancelled letter in hyperplanes | Acute and e body resolve the extra cancelled letter as **é**, rather than k or x: 40. |
| Bottom base letter | Literal two-bowl B shape preferred, with S/U/doubled-S alternatives; order of any overprinting remains unknown: 41. The repeated glyph uses the first candidate in accordance with the recurring-glyph convention: 43. |
| Final map j/f and target | j/f remains unresolved, j preferred from dot and low hook: 42. Clipped S-like target remains uncertain: 44. |
| Tildes / ordinary P / bars and stars | The listed tildes are pen strokes over X/f only; P is a single ordinary typed capital; barred s and all listed stars are separately accounted for in inventory and notation. No reading was changed merely to match earlier notation. |
| `restriction probablement inutile` | The author's reservation is preserved, together with the cancelled `sans doute` and typed replacement `probablement`; 22 and inventory items 36–37. |

### Further points material to adjudication

The stop after the first `S)` is clearly separate in `top_close`; it is present in H but missing in C. The last line also has a separate final stop, omitted by H. The pen insertion in section 4 ends in its own comma, while the original typed comma remains after m. The LaTeX therefore preserves both, even though that is awkward punctuation. The capital in `Alg.` is retained rather than lowered to H's `alg.`.

The uncertainty in the bottom base is deliberate. The crop presents a near-upright left side and two right bowls, which makes B the closest literal outline. S/U/doubled-S remain possible because of the superposed forms. The reading does **not** claim that B is the intended mathematical base. The same ambiguous form appears after the final restriction stroke, and its first candidate is carried there without repeating the doubt marker. In contrast, the final target is a tall pen S-like shape clipped by the scan edge. Mathematical consistency has not been used to collapse these different pieces of evidence.

The long stroke over the b in `fibres` is treated as retouching/extension of that letter, with uncertain full-pen versus surviving-type provenance. It has not been invented as a new letter, marginal annotation or diagram. The overprint alternatives in the article before `classe`, in `...e définit`, the curve name and the second product are likewise alternatives of structure/order, not confident reconstructions of revision chronology.

## Mathematical reading and diagnostic limits

The page assumes conditions a) and b) for the written map on geometric fibres and considers a cycle z in Z^n(Y) whose fibre is algebraically equivalent to zero and consequently cohomologically zero. It says the associated u(z) is defined in the displayed first-cohomology group. The asserted conclusion places it in an i-star image modulo a torsion class, at least after replacing S by a nonempty open. The author explicitly weakens the earlier `sans doute` to `probablement` when calling that restriction unnecessary.

The proof invokes statement 2), spreads a curve and a double-prime cycle over a finite extension K of k(s), appeals to a trace argument, and supposes the curve/cycle defined relatively over S. It then uses a decomposition z=i-star(z-prime)+z-double-prime and says the remaining class induces the zero map from H^1 of the curve fibre to H^(2n−1) of the Y fibre; it invokes statement 1) to conclude vanishing. Statements 1) and 2) themselves are outside this permitted page packet, so this was a reading of the proof, not a verification of those propositions.

The ink-sensitive mathematical diagnostics were the opening X-to-X morphism, the ambient capitals of the two products, the inline coefficient correction, and the final base/name/target. Each relevant unsettled locus received its permitted crop. Expected domains, the usual shape of a trace argument and the familiar name of a Lefschetz-pencil morphism were not used as substitute evidence.

A purely structural count confirms that the first class display visibly lacks one closing parenthesis relative to its nesting; the inline i-star group also lacks one. These omissions were deliberately preserved. This parenthesis count is a transcription/syntax check, not a mathematical proof event. Section 4 begins a Lefschetz-pencil construction from a smooth projective X of dimension m over the added algebraically closed field k, with a blown-up X and a morphism to the projective line, and ends in the uncertain restriction map.

**Actual mathematical check events: none.** No targeted proof check, independent re-proof, computation/formal certificate, use-and-recheck, background-carrying event or refutation was claimed. The JSON `check_events` list is empty.

## Structural validation

The written LaTeX was checked for balanced braces, balanced inline-math delimiters, two matched display pairs, use only of the attached diplomatic macros and ordinary allowed LaTeX commands, correct scan-page marker and absence of a new `cotefile` marker or newly defined macros. The source's missing ordinary parentheses are intentional and are not confused with unbalanced LaTeX delimiters.

The JSON was parsed and its required fields checked. All 45 difference IDs are unique; each has an in-bounds whole-image box and an existing crop path or the actual half used as evidence. All 73 inventory items use an allowed kind and are marked transcribed. All 16 crop metadata entries correspond to one actual inspection. The 15 in-place `unsure` occurrences correspond to the 15 unresolved records. **No compilation was run.**

## Brief feedback

The v05 distinctions between letter shape, source layer and temporal correction order are necessary on this page. A future explicit neutral overprint convention could represent inseparable C/Z or d/s components without choosing an old/live order even as the first alternative. Under the current macros, both structural alternatives have been retained in place. The whole-coordinate requirement is useful: all half-settled differences have boxes without generating redundant crops.

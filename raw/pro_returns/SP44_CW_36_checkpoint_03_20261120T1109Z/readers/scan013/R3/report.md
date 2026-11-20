# Scan 013 — independent reader R3

Recorded UTC start: **2026-11-20T09:52:41Z**. UTC end is recorded below after the structural check.

## Scope and authority

I read `briefs/brief_v04_scan013.md` completely, then the exact `PREAMBLE.tex` it names, and the complete page-local `packets/scan013/packet.md`. These supplied the two fallible witnesses, C's doubts, and the frozen notation comparison. I did not open another page, another reader's return, published text, or any external source. No OCR, text-recognition facility, web search, or compilation was used. I did not alter the shared transcription, notation, or progress files.

The return consists of the complete `reading.tex`, this report, and `result.json`. The JSON contains **40 comparison rows**, **63 inventory entries**, **10 unresolved entries**, the notation observations, and the two actual conditional mathematical checks. The comparison list and inventory in that file are complete; this report supplies the coverage and interpretive context without duplicating every row.

## Actual image-view record

The whole image is **1682 × 2151** pixels. The halves are **1682 × 1155** and **1682 × 1156**. Half a starts at whole-image y = 0; half b starts at y = 995. All reported boxes use whole-image coordinates.

The actual viewing sequence was:

1. `A36-01_36_scan013.jpg`, once, for layout only.
2. `A36-01_36_scan013_a.jpg`, once, for every line and symbol.
3. `A36-01_36_scan013_b.jpg`, once, for every line and symbol.
4. The fifteen crops listed below, each generated once and actually inspected once with the image viewer. No crop or full half was reopened. None of the viewer outputs was truncated before inspection.

The whole-page inspection located the pen-looking page number 4, the opening b) condition, its cohomology display, the four-line motif continuation, the underlined three-line statement, the a') equation, the three-line b') clause, the eight-line proof, section 3 with its interlinear insertion and final display, and the pencil-looking archive number 12. There are no diagrams, drawings, independent marginal prose notes, or footnotes. The manuscript/page number and archive number are separately represented.

Every crop used the supplied helper with `--scan 13 --reader R3`. The helper performed autocontrast, LANCZOS enlargement to width 2400, and modest unsharp masking. Rotation was 0° for these saved crops; the interlinear additions were legible at their original baseline angle. Crop sidecar JSON files preserve the operations, coordinates, and creation times.

| Crop under `crops/scan013/R3/` | Whole-image box | Open question inspected |
|---|---|---|
| `curve_letter.jpg` | [1410, 135, 1540, 228] | Double impression/alphabet of the first curve name |
| `first_display.jpg` | [425, 340, 1158, 438] | Closing parenthesis after C, old Z/new Q, crossed subscripts, arrow and degrees |
| `cette_cancel.jpg` | [1168, 498, 1420, 582] | Accent in cetté and cancelled following cells |
| `morceau_du.jpg` | [490, 548, 736, 637] | Plus grand placement guide and cancelled dx/du/de |
| `b_cancel_indices.jpg` | [550, 991, 1118, 1078] | Cancelled opening, added primes, and o/0 index |
| `q_prefix.jpg` | [1188, 977, 1520, 1082] | Q- prefix alphabet, underline, source layer, and placement guide |
| `e_courbe.jpg` | [534, 1060, 819, 1150] | Cancelled e after surviving un, old courbe, underline boundary |
| `product_correction.jpg` | [978, 1060, 1153, 1159] | Old Cx, separately cancelled X, new Y, live xC |
| `nul_coefficients.jpg` | [261, 1138, 1046, 1222] | Double underline, cancelled de, old Z under left Q, coefficients, map |
| `hypthese.jpg` | [1042, 1383, 1384, 1470] | Missing o and weak è in hypthèse |
| `final_z.jpg` | [183, 1725, 580, 1820] | Final overprinted z'/Z' and recurring o-shaped index |
| `regulier.jpg` | [1166, 1887, 1394, 1983] | Word accent and whether right hook is punctuation or placement guide |
| `et_un_underline.jpg` | [712, 865, 1064, 941] | Rule beginning below t of et; ununderlined following formula |
| `pullback_prime.jpg` | [180, 1590, 605, 1682] | Star, id subscript, and pen prime on the inner Z |
| `algebri_underline.jpg` | [1395, 790, 1623, 881] | Whether the line-end algébri- is underlined; it is |

The last crop resolved a remaining emphasis-scope question during transcription. It is a distinct locus from the et/un crop and does not duplicate any previously cropped word.

## Line-by-line coverage

Coordinates below are approximate text-line regions, not inferred paragraph boundaries. Line-end hyphenation is joined in the LaTeX; visible paragraph indentation and larger spacing are preserved.

| Region | Explicit coverage |
|---|---|
| Top margin, y 59–99 | Pen-looking 4, represented by handwritten `mspage`, not the archive number. |
| Opening line 1, y 164–211 | b), Pour toute courbe algébrique, parenthetic propre/lisse/connexe, uncertain double C, sur k and comma. The accents and parentheses were checked. |
| Opening line 2, y 237–278 | et tout cycle algébrique Z sur YxC de codimension n, l'homomorphisme. Product is baseline typed x; the capital Z is ordinary type. |
| Opening line 3, y 308–340 | correspondant, alone at the left text margin; no new paragraph inferred. |
| First display, y 363–432 | Z:, H^1, literal `(C)`, overwritten left coefficient, recurring crossed subscript, `(1))`, handwritten right arrow, H raised 2n-1, Y and comma, clean underlined right Q, crossed subscript, `(n))`. |
| Continuation line 1, y 443–490 | a son image dans celle de i*, reference (***), period, opening `(NB Si on admet le yoga des`. Both stars and parentheses are retained. |
| Continuation line 2, y 518–564 | motifs, justifiable par les plus source quote marks, conjectures standard, comma, literal cetté, cancelled following cells, condition. |
| Interline/continuation line 3, y 556–638 | Handwritten plus grand and guide before morceau; cancelled dx/du/de; source upright quote strokes around de niveau 1; du motif; cancelled Coker; ayant comme. |
| Continuation line 4, y 652–705 | réalisation, mechanical crossed glyph in adique, Coker i with pen star, est nul). No alphabet normalization from the intended meaning. |
| Statement line 1, y 727–803 | Sous ces conditions, pour tout cycle algébrique, z with pen membership and ordinary Z^n(Y), qui est. Three separate emphasis rules; formula itself has no underline. |
| Statement line 2, y 800–873 | algébriquement équivalent à zéro, il existe un cycle, z' with pen membership and Z^n(X), line-end algébri-. The line-end word has its own pen underline; no rule runs under the formula. |
| Statement line 3, y 874–939 | quement équivalent à zéro, et un with uncertain whole-word underline scope, z'' with pen membership and Z^n(Y), tels que. The final formula and tels que are not underlined. |
| a') line, y 942–989 | Left label a'), z = i*(z') + z''; raised pen star and all primes checked. It is retained as the labelled display. |
| b') line 1, y 1000–1080 | Cancelled l'hom(x), live z'', two separately added pairs of primes on Z, t_1 and o/0-shaped second index, où, typed Z'', est un, inserted underlined Q- with source-layer alternative, cycle. |
| b') line 2, y 1082–1160 | de codimension n sur un; cancelled e courbe; produit; cancelled Cx, separately slashed X and pen Y, live xC; induisant un homomorphis-. Separate underlines stop before n and the product formula. |
| b') line 3, y 1152–1220 | -me, doubly underlined nul, cancelled de, H^1(C, left overwritten coefficient and crossed subscript (1)), pen right arrow, H raised 2n-1 with Y and clean right coefficient (n)). Wrapped homomorphisme is joined. |
| Proof line 1, y 1264–1325 | Indented Démonstration immédiate : on écrit z = Z(t_1)-Z(t_o) avec. Both parameter indices and difference sign checked. |
| Proof line 2, y 1334–1388 | Z with pen membership in ordinary Z^n(YxC), ce Z définit un homomorphisme Z:H^1(C)→H raised 2n-1(Y), cancelled dont le. |
| Proof line 3, y 1404–1470 | qui par hypothèse b) tombe dans Im i with pen star; donc par literal hypthèse a) est égal au. The second spelling lacks o. |
| Proof line 4, y 1479–1524 | composé (iv)Z=i(vZ), or vZ:H^1(C)→H raised 2n-1(X) est algébrique puisque. The printed i, without star, remains. The irregular arrowhead is still a right arrow. |
| Proof line 5, y 1549–1592 | v l'est, donc donné par un cycle algébrique Z' sur XxC, et si on pose. Prime and ordinary letters individually checked. |
| Proof line 6, y 1603–1664 | Z''=Z-(ixid_C) with raised pen star (Z with pen prime), on aura par construction que Z'' induit l'homomor-. No closing parenthesis is deleted or restored. |
| Proof line 7, y 1681–1736 | -phisme nul H^1(C)→H raised 2n-1(Y). Cancelled D'autre part; Il suffit alors de poser. Joined homomorphisme retains its ordinary prose form. |
| Proof line 8, y 1752–1818 | Overprinted first z'/Z'/double-struck-looking Z', equality of two Z' evaluations, comma, z'' and equality of two Z'' evaluations, period. This remains a continuation at the text margin, not a newly centered display. |
| Section 3 line 1, y 1851–1899 | 3. Mettant ensemble les réflexions de 1) et 2), on trouve ceci. On. Typed capitalization and full stops retained. |
| Section 3 line 2, y 1895–1970 | se donne des schémas propres et lisses X et Y sur S; inserted regularity word before connexe, et un S-. The right hook is part of the guide; accent remains unresolved. |
| Section 3 line 3, y 1993–2029 | morphisme. The line-end S-morphisme hyphen is lexical and is retained after joining. |
| Bottom display, y 2061–2098 | i:Y, pen right arrow, X and period. No diagram structure beyond this one-map display. |
| Bottom-left margin, y 2082–2125 | Pencil-looking 12, represented only as the archive sheet comment. |

## Comparison decisions and C's doubts

The JSON comparison rows give C's reading, H's reading, my reading, separate against-C/against-H flags, ink observations, evidence path, confidence, and a box for every locus. An uncertainty-resolution row may agree with one of C's already supplied candidates and therefore have `against_C: false`. A flag against a witness in a still-uncertain row records the preferred literal reading or added uncertainty, not a categorical claim that the witness's candidate is impossible.

### Important independent findings

- The closing parenthesis immediately after C in the first display is unmistakably tall. H silently makes this a comma. The malformed expression is retained, with no attempted mathematical repair.
- The left coefficient in b') contains another recoverable old Z under the Q. Both witnesses omit that cancelled layer there. The right coefficient is a clean Q without this internal diagonal.
- The repeated crossed letter in coefficients and in the adic adjective looks mechanical. It is recorded as chi/ell at first occurrence, chi thereafter; C's pen-ell source layer is changed. H's global statement that the machine ell is chi-shaped is expressly credited, so this alone is **not** counted as an H error.
- Literal **cetté** and **hypthèse** are retained. Their acute/grave marks and missing letter were individually checked.
- The old product begins with cancelled **Cx**, followed by a separately cancelled X and its pen Y replacement. H records only the X-to-Y change. C already permits the Cx alternative.
- The hook after the inserted regularity word continues into the placement guide. It does not supply C's comma. The short accent over the first e looks grave, but I keep the acute alternative because the cursive execution is not decisive.
- The underlined Q- prefix appears typed, with a pen placement guide. Since source-layer inference remains less secure than the letter reading, the handwritten alternative is retained in place. H's explicit ink claim is consequently flagged as a preferred-source-layer disagreement, not disproved categorically.
- H's emphasis wrappers include several formulas and tail phrases beneath which no pen rule exists. The comparison records actual scope and the two rules under nul, while treating mere `emph`/`uline` equivalence as no error.

### Complete C-doubt disposition

| C doubt or notation concern | Disposition and evidence |
|---|---|
| Doubled first C | Unresolved alphabet: displaced impressions are visible; `mathbb C` / C retained. Row 01, `curve_letter`. |
| cetté/cette | Resolved to literal cetté, clear acute. Row 07, `cette_cancel`. |
| Cancelled même/xxxxé | Unresolved; visible cancellation-cell reading xxxxé is first, lexical même remains possible. Row 08. |
| Cancelled du/de/dx | Unresolved; first d is clear, second cell crossed. dx is a visible-cell reading, not a restored word. Row 09, `morceau_du`. |
| Cancelled opening of b') | l'hom survives; final x-out cell is visible, with no recoverable underlying last letter. l'homx/l'hom retained. Row 19. |
| e courbe/courbe | Resolved to cancelled e courbe. The extra e is a separate cell after live un. Row 23. |
| Old C or Cx; X-to-Y | Resolved to old Cx plus separately slashed X and added Y. Row 24. |
| Cancelled de/dx after nul | Preferred de, medium confidence from remaining e middle/lower strokes. Row 27. |
| hypthèse/hypothèse | Resolved to hypthèse; no o cell. Row 33. |
| Final z'/Z'/double impression | Unresolved; overlap and order remain uncertain. No old/live decomposition is invented. Row 35. |
| First-display closing parenthesis | Confirmed exactly as C had noted, despite malformed mathematics. Row 02. |
| Q prefixes/coefficient underlines | Separate underline and ordinary Q confirmed; first left overwrite confirmed, b') left old Z newly observed; source layer of interlinear prefix is explicitly uncertain. Rows 03, 21, 28. |
| Prime marks and i stars | Checked at every occurrence; the cropped pullback has a real pen prime and star. Two pen prime pairs in b') are retained. The final variable's overprint remains unresolved. Inventory and notation list give provenance. |
| Ordinary Z^n, H, Coker, Im, id_C, baseline x | Checked on both halves, with the pullback and product crops as local confirmation. No global capital normalization; ordinary forms are retained where their strokes warrant them. |
| Handwritten page 4 and section 3 | Both confirmed; archive 12 is kept separate. |
| Explicit motivic qualification | Preserved in the transcription and mathematical notes; no unconditional theorem is substituted. |

## Mathematics: reading, diagnostics, and actual checks

The page states a condition on the action of correspondences from a proper smooth connected curve: their images must lie in the image of i*. It then states that an algebraically trivial cycle z decomposes as i*(z') + z'', with z' algebraically trivial and z'' represented as a difference of fibres of a rational cycle whose correspondence action is zero. The proof names a map v, uses the two preceding conditions, chooses a realizing cycle Z', and subtracts its pullback. Section 3 begins a relative setup with proper smooth X and Y over a regular/connected base S and a morphism i:Y→X.

The author's qualification is explicit: **“Si on admet le yoga des motifs, justifiable par les``conjectures standard''”**. Its conditional status is retained. I did not verify the motivic parenthesis, the existence of an algebraic realizing cycle, any standard conjecture, or the earlier hypotheses a) and b) beyond what is actually written on this page.

Two mathematical diagnostics affected reinspection but not emendation:

1. The first displayed expression does not parse with the literal closing parenthesis after C. The crop confirms the closing curve, and the transcription retains it.
2. In `(iv)Z=i(vZ)`, the symbol is printed i without a star, although nearby image statements use i*. This is not silently changed; H's note accurately identifies the same source feature. A conditional map calculation may name the map A, but that explanatory notation is not inserted into the page.

The two `check_events` record checks actually performed:

- **Targeted proof check, `36-013-proof-zero-action`.** Let A be the map denoted i in the local composite, V the map v, and T the action of Z. Assume that AV is the identity on Im A, as the local argument invokes, and that T takes values in Im A. For every h, AVT(h)=T(h); therefore `(T-AVT)(h)=0`. This checks the stated subtraction step under those assumptions and compatible realization. It is not a proof of the earlier condition a) or of algebraicity/existence.
- **Computation or formal certificate, `36-013-cycle-decomposition` — computation only, no formal certificate.** Assuming evaluation at the two parameters commutes with pullback, substitute `Z''=Z-P(Z')`, where P is the displayed pullback. The difference `Z''(t_1)-Z''(t_o)` equals `Z(t_1)-Z(t_o) - i*[Z'(t_1)-Z'(t_o)]`; rearranging yields a'). This verifies the additive identity conditionally. It does not establish the family's existence or the characterization of algebraic equivalence.

No numerical or degree check was claimed merely because exponents were transcribed. The cohomological degrees, targets, indices, and prime/star distinctions were read individually. The mathematical role of a second parameter was not used to decide whether its typed glyph is o or zero.

## Inventory and provenance

The 63 JSON inventory entries include every body text block, the three separate displays, both page/archival numerals, every readable cancellation, each pen membership sign, each added arrow and star, the two separate prime-pair additions in b'), the pullback prime, both Q-over-Z layers, each underline segment including wrapped continuations, the old Cx and separately slashed X, the added Y, and all three interlinear insertions with their placement guides. No unsupported attribution to a particular person's hand is made.

Pen rules beneath typed words use `uline`/`uuline` without falsely turning the words into handwriting. Ordinary heavy type is not made bold. The final z/Z overprint is left as a structural alphabet uncertainty rather than assigning an unsupported temporal old/live sequence. Visible x-out characters are explicitly distinguished from recovered cancelled lexical letters.

## Structural validation and brief feedback

Only structural validation is performed: balanced braces and TeX delimiters, allowed command vocabulary, JSON schema fields and enumerated kinds, valid whole-image boxes, and presence of all fifteen crop files. The authorial unmatched mathematical punctuation is not a TeX-structure error and remains. No LaTeX was compiled.

The v04 clarifications were useful, particularly the distinction between a recoverable old letter and a visible x-out cell, and the instruction to credit H's global typography notes. One further convention would help: how to encode an underline that begins inside a word, as below the t in et. Here the whole-word scope remains an explicit in-place alternative. The typed-versus-pen source layer of a clean interlinear coefficient likewise receives an in-place alternative instead of an unqualified attribution.


**UTC end: 2026-11-20T10:03:33Z.** Structural validation passed: brace and delimiter balance, allowed macros, all 40 complete comparison records, all 63 inventory records, valid coordinates, both enumerated check-event types, and 15 crop/sidecar pairs. No compilation was performed.

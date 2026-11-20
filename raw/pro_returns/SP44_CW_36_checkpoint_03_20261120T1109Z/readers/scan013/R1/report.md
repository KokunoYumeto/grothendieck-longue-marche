# Scan 013 — independent reader R1

## Scope and timing

- Logged start of visual examination (UTC): 2026-11-20T09:52:31.799483Z.
- End of reading/output preparation (UTC): 2026-11-20T10:03:59.986223Z.
- Inputs read in full: `briefs/brief_v04_scan013.md`, the exact `PREAMBLE.tex` named there, and `packets/scan013/packet.md` only.
- No other page image, other reader return, OCR, text-recognition output, web source, published transcription, or LaTeX compilation was used. I did not delegate further.

## Actual image-view sequence

The whole image was opened once with `view_image` for layout. Its dimensions are 1682 × 2151. The supplied half **a** (1682 × 1155) was then opened once and read line by line; half **b** (1682 × 1156) was then opened once and read line by line. Half b begins at whole-image y = 995. Overlap is part of the supplied images; neither full half was reopened or enlarged.

After those three views, the thirteen remaining-locus crops below were created once each with the supplied helper, `--scan 13 --reader R1`, and actually inspected with `view_image` in the table order. Crops were output two per viewer call or one for the last call; no image output was truncated. The helper applied autocontrast, LANCZOS resize to 2400 pixels wide, and UnsharpMask(1,110,3), saving JPEG90. No second crop of a locus was made. All bounding boxes below and in the JSON refer to whole-image coordinates. All rotations were 0°; the insertion words remain at their mild original baseline slope and were legible at this size.

| Actually viewed crop | Whole-image bounding box | Rotation |
|---|---|---|
| `crops/scan013/R1/curve_letter.jpg` | `[1240, 143, 1633, 288]` | 0° |
| `crops/scan013/R1/first_coefficient.jpg` | `[430, 345, 1160, 495]` | 0° |
| `crops/scan013/R1/cette_cancelled.jpg` | `[1120, 500, 1610, 630]` | 0° |
| `crops/scan013/R1/motif_insertion_du.jpg` | `[475, 543, 760, 645]` | 0° |
| `crops/scan013/R1/b_cancelled_opening.jpg` | `[545, 991, 730, 1080]` | 0° |
| `crops/scan013/R1/b_before_produit.jpg` | `[530, 1055, 835, 1145]` | 0° |
| `crops/scan013/R1/b_product.jpg` | `[965, 1055, 1160, 1145]` | 0° |
| `crops/scan013/R1/b_after_nul.jpg` | `[258, 1128, 445, 1212]` | 0° |
| `crops/scan013/R1/b_coefficients.jpg` | `[445, 1120, 1055, 1225]` | 0° |
| `crops/scan013/R1/b_evaluation_indices.jpg` | `[728, 991, 1135, 1080]` | 0° |
| `crops/scan013/R1/proof_hypthese.jpg` | `[1050, 1340, 1410, 1453]` | 0° |
| `crops/scan013/R1/proof_final_z.jpg` | `[176, 1730, 580, 1818]` | 0° |
| `crops/scan013/R1/regulier_insertion.jpg` | `[1115, 1877, 1425, 1985]` | 0° |

The crops were created after the half reads and before inspection. Their metadata JSON files retain the actual creation UTC times and transformation parameters.

## Compact line-by-line coverage

The labels below are local report labels, not additions to the transcription. Physical source line breaks are joined in `reading.tex`, except that source paragraphs, displays, enumeration, insertions and lexical hyphens are retained.

| Line or element | Whole-image y, approximately | Coverage and decision |
|---|---:|---|
| Handwritten number | 65–95 | Read as 4; represented through handwritten `mspage`, not the archive number. |
| L01 | 166–210 | b), Pour toute courbe algébrique, parenthetic propre/lisse/connexe, doubled/overprinted curve name, sur k, all read. Curve alphabet uncertainty retained after crop. |
| L02 | 239–282 | et tout cycle algébrique Z sur YxC de codimension n, l’homomorphisme; all letters, accents and typed lowercase product x read. |
| L03 | 307–342 | correspondant read in full, continuous with preceding sentence. |
| D01 | 356–431 | Entire Z-labelled map checked symbol by symbol: H, raised 1, literal C), old Z/pen Q, lower rule, crossed subscript, (1)), pen arrow, 2n−1, Y comma, right underlined Q/subscript/(n)). No punctuation repair. |
| L04 | 443–490 | a son image dans celle de i with added star, de (***). (NB Si on admet le yoga des; punctuation and three asterisks read. |
| L05 | 519–566 | motifs, justifiable par les followed immediately by typed double quotes, conjectures standard, live cetté, cancelled cells and condition read. Live acute is secure; old word is not restored as même. |
| Insertion | 554–608 | plus grand, with continuous placement guide targeting before morceau; no invented terminal punctuation. |
| L06 | 592–637 | signifie que le morceau, cancelled d[u/e/x], quoted de niveau 1, du motif, cancelled Coker, ayant comme; all read. |
| L07 | 657–703 | réalisation, mechanical crossed glyph-adique, Coker i with pen star, est nul). Mechanical-versus-pen distinction rechecked against the coefficient crop. |
| L08 | 731–801 | Sous ces conditions, pour tout cycle algébrique, z membership Z^n(Y), qui est; all words and exact lexical underline intervals recorded. |
| L09 | 804–871 | algébriquement équivalent à zéro, il existe un cycle, z prime membership Z^n(X), algébri-; membership signs and separated rules recorded; source line-end hyphen joined. |
| L10 | 877–935 | -quement équivalent à zéro, et un, z double prime membership Z^n(Y), tels que; un alone underlined and unruled formulas/connectives retained. |
| D02 | 940–989 | a-prime label; z = i with pen star (z prime) + z double prime; all symbols read. |
| L11 | 1013–1079 | b-prime label; cancelled l’hom plus terminal x-out; z double prime evaluation; two pen double primes; 1 and round o/0 indices; où Z double prime est un cycle. |
| Q-prefix insertion | 992–1040 | Handwritten underlined Q-hyphen and placement guide attach the prefix to cycle. |
| L12 | 1084–1150 | de codimension n sur un, cancelled e courbe, produit, cancelled Cx, pen-struck X/pen Y, live xC, induisant un homomorphis-; underlines, correction layers and every live/cancelled factor recorded. |
| L13 | 1153–1210 | -me, double-underlined nul, cancelled de, complete coefficient-bearing cohomology map, final period. Both left coefficient old Z and pen Q are visible; recurring glyphs mechanical. |
| L14 | 1266–1321 | Démonstration immédiate : on écrit z = Z(t1) − Z(to), avec; accents and point indices read. |
| L15 | 1330–1393 | Z membership Z^n(YxC), ce Z définit un homomorphisme, complete Z map and cancelled dont le; all read. |
| L16 | 1404–1458 | qui par hypothèse b) tombe dans Im i with pen star donc par hypthèse a) est égal au; missing o in the second word is confirmed, not repaired. |
| L17 | 1474–1534 | composé (iv)Z = i(vZ), or vZ: H^1(C) rightward pen arrow H^{2n−1}(X) est algébrique puisque; i is left unstarred as typed. |
| L18 | 1543–1600 | v l’est, donc donné par un cycle algébrique Z prime sur XxC, et si on pose; all read. |
| L19 | 1608–1673 | Z double prime = Z − (ixid_C) with pen star, argument Z with added prime, on aura par construction que Z double prime induit l’homomor-; exact parentheses and index C retained. |
| L20 | 1682–1743 | -phisme nul, full H^1(C) to H^{2n−1}(Y) map, period; cancelled D’autre part; Il suffit alors de poser. |
| L21 | 1754–1814 | Both final fibre-difference equalities read. Initial overlapping z/Z impressions retained as an in-place uncertainty without a claimed old/live order; round indices use the first occurrence’s o/0 convention. |
| L22 | 1849–1897 | 3. Mettant ensemble les réflexions de 1) et 2), on trouve ceci. On; numbering, accents and punctuation read. |
| L23 | 1920–1978 | se donne des schémas propres et lisses X et Y sur S [régulier] connexe, et un S-; full line read. |
| Insertion | 1894–1975 | régulier targets the gap after S. Curved right hook continues into the placement guide; no comma follows the insertion. |
| L24 | 1990–2033 | morphisme, completing the lexical S-morphisme without introducing a new paragraph. |
| D03 | 2058–2108 | i: Y, pen arrow to X, separated terminal period. This is a one-map display, not an omitted diagram. |
| Archive number | 2080–2127 | Pencil-like 12 at lower left, recorded only in an archive comment. |

## Complete comparison and doubt accounting

The authoritative exhaustive per-locus lists are in `result.json`: **42 comparison rows**, **60 inventory entries**, and **6 unresolved entries**. Each comparison row supplies both witnesses’ readings, the returned reading, per-witness flags, specific ink evidence, and a whole-image bounding box. Rows also record C-doubt confirmations when the preferred C reading survives.

All C doubts were addressed:

| C doubt | Result |
|---|---|
| Doubled curve C | Doubled/overprinted contours confirmed, but deliberate alphabet unresolved. In-place C alternatives retained. |
| cetté/cette | The acute over the live final e is clear: cetté. |
| Cancelled même/xxxxé | Five crossed cells are visible; final accented/e-like remnant uncertain. `xxxxé|xxxxx` records visible cancellation marks, not a recovered word; même cannot be read letter by letter. |
| Cancelled du/de/dx after morceau | First d readable; second remains u/e/x. |
| Cancelled l’hom/l’homx/Xhomx | l, apostrophe and hom contours recoverable; a separate final x-out cell survives. Returned l’homx, with the terminal x explicitly documented as cancellation material. |
| Extra e before courbe | Confirmed: the cancelled material includes the e that would follow un, plus courbe. |
| Cancelled C/Cx and X before Y | A separate Cx prefix is present before the pen-struck X and added Y. Both cancelled layers retained. |
| Cancelled de/dx after nul | Read as de at moderate confidence after the crop; e bowl/middle stroke remain visible. |
| hypthèse/hypothèse, repeated twice in C’s notes | One source locus; confirmed hypthèse without o. |
| Final z-prime/overprinted Z-prime | Remains unresolved, with C’s three alphabet/overprint candidates retained. No temporal order invented. |
| H^1(C) versus H^1(C, | The source has a full live closing parenthesis; kept despite malformed standard notation. |

The following substantive decisions are especially consequential for collation. Both left underlined coefficient letters preserve an old typed Z under a pen Q; C recorded only the first. The recurring hooked crossed coefficient and adic glyphs have mechanical structure and are therefore not wrapped as handwritten ell. H’s supplied global machine-ell note is credited, so these source-layer corrections are not charged as H letter errors. The live cetté and hypthèse are retained despite normal French expectations. The section-3 insertion ends without a comma: the apparent comma is visibly continuous with the placement guide.

C’s scattered pen-underlining scopes are largely supported. H’s continuous emphasis includes several formulas and connecting words with no source underline and misses the first Sous ces conditions rule; those distinct loci are recorded. The two lines under nul are preserved as double underlining. H’s explanatory notes themselves are not source text, and its explicit X-to-Y correction note is credited; the additionally omitted old Cx prefix is separately reported. Mere absent handwriting wrappers, equivalent arrow/operator macros, and H’s display packaging of the last two proof equalities are not counted as textual errors. By contrast, the serifed literal x product glyphs are recorded separately from H’s rendered multiplication crosses.

## Full page inventory and source layers

`result.json` inventories every text block and all three displays, the handwritten manuscript number, archive number, every cancellation, overwritten coefficient, inserted word/prefix, added prime/star/member/arrow, every separate lexical underline interval, and the ambiguous final typewriter overprint. Pen provenance applies to the rules beneath typed words, not to the words themselves. Writer identity is not established from this page alone. No independent drawing, multi-object diagram, margin argument, footnote, or untranscribed prose block remains.

Paragraph cues are the indented conclusion beginning Sous ces conditions, the separated condition/display lines, the enlarged gap and indent before Démonstration immédiate, and the new numbered section 3. The final proof equations have no new paragraph cue and are kept in the proof paragraph. Ordinary source line wraps do not introduce paragraphs. Lexical S-morphisme and glyph-adique retain their hyphens; algébri-/quement and homomor-/phisme line-break hyphens are joined.

The notation list includes the doubled curve-name doubt, the mechanical chi/ell-shaped glyph, the round o/0 index, both overwritten Q coefficients, pen Q-cycle prefix, typed products, ordinary H and cycle-group Z capitals, final overlapping variable, visible x-out convention, quotation marks, and pen prime/star forms. No global blackboard alphabet or handwriting normalization was imposed.

## Mathematical reading and actual check

The page gives condition b on images of curve correspondences, then a decomposition of an algebraically trivial cycle into a pullback plus a fibre difference with zero cohomology action. Its motif explanation expressly depends on the yoga of motifs and “conjectures standard”; this is the author’s conditional reservation, not a proposition verified here. The proof uses a map v asserted to be algebraic, constructs a cycle Z prime and subtracts its pullback. Section 3 begins the relative setup over regular connected S.

The first display’s C) is a mathematical parsing problem but a visually clear reading, so it remains. The composition `(iv)Z=i(vZ)` has unstarred i, as H also explicitly notes; no star is supplied. The page itself omits coefficient and twist arguments in the proof’s shorter formulas; they are not reconstructed. The o/0 alphabet, doubled C, and overlapping final z/Z remain visual uncertainties independently of the expected mathematics.

**One actual conditional targeted proof check was carried out.** Let A denote the cohomology operator written i in the composition, assume the identity from a) used in the text says that Av acts as the identity on Im A, and use b) in the form Im Z contained in Im A. For any u, Z(u) lies in Im A, hence Av(Z(u)) = Z(u), so `(Z−AvZ)(u)=0`. This checks exactly the local zero-action step under that assumed identity. It does not verify a), the standard conjectures, algebraicity of v, representability by Z prime, cycle pullback compatibility, or the whole theorem. This event alone appears in `check_events`; no formal certificate was produced.

## Structural verification and brief feedback

Only structural checks were applied: JSON parses, difference IDs are unique, each comparison has a whole-image box and required fields, crop files and metadata exist, inventory coverage is populated, and `reading.tex` has balanced braces/math delimiters/environments with only supplied macros and ordinary allowed LaTeX commands. The page was not compiled.

The brief was usable without substantive amendment. Its warnings about overlapping old/live type, machine glyphs, x-out cells, H’s global notes and continuous placement hooks directly affected the readings. Crop metadata records the mild original slant honestly; no repeated crop was used to force uncertain readings.

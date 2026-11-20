# Independent reading R2 — scan 013

- UTC start: **2026-11-20 09:52:32 UTC** (first recorded clock reading, after loading the brief and packet).
- UTC end: **2026-11-20 10:04:57 UTC**.
- Scope: scan 013 only, manuscript page 4, archive pencil sheet number 12.
- Inputs read in full: `briefs/brief_v04_scan013.md`, the exact `PREAMBLE.tex` it names, and `packets/scan013/packet.md` (both witnesses, all earlier C doubts/notes, frozen notation, and crop instructions).
- Sources actually inspected: the assigned whole, both assigned halves, and 13 saved tight crops from that same whole. No other page, reader return, OCR, web, published text, or compilation was used. No shared deliverable was altered.

## Visual sequence and operations

1. `source/SP44_CW_36_scans/A36-01_36_scan013.jpg` was opened **once** for layout. It is 1682 × 2151 pixels. Layout inventory: handwritten 4 above; the continuation b), its first cohomology display and motivic parenthesis; a three-line underlined conclusion; the a′) equality; b′) in three lines with corrections; one eight-line proof paragraph; paragraph 3 and its final morphism display; the pencil 12 below. No diagram or drawing was observed.
2. `A36-01_36_scan013_a.jpg` was opened **once**, then read in order from the handwritten 4 through the visible portion of b′). Dimensions: 1682 × 1155. Every prose line, raised/lowered glyph, cancellation, insertion, rule and punctuation mark was compared with C and H.
3. `A36-01_36_scan013_b.jpg` was opened **once**, then read in order from the overlap at b′) through the pencil 12. Dimensions: 1682 × 1156; its local y coordinates correspond to whole-image y + 995.
4. Open loci were recorded before making the first twelve crops. Each was made once with the prescribed helper, `--scan 13 --reader R2`. The saved crops were opened in the order tabulated below, two per viewer output. One additional remaining source-layer question, the proof's raised n, received one separate crop after the initial crop sequence. No crop was regenerated and no whole or half was reopened. Image delivery was complete; no resend was required.

The helper applied autocontrast, LANCZOS enlargement to 2400 pixels wide, and UnsharpMask(radius 1.0, percent 110, threshold 3), saving JPEG at quality 90. All rotations were 0°: the target letter shapes were readable without an additional rotated view. Every bbox below and every bbox in `result.json` is in **whole-image coordinates**. Half-settled bboxes are approximate localization boxes, not claims of pixel segmentation.

| View order | Saved crop | Whole bbox [x0,y0,x1,y1] | Remaining locus examined |
|---|---|---|---|
| 4 | `crops/scan013/R2/first_curve_C.jpg` | [1385, 145, 1618, 218] | First curve capital and displaced impressions |
| 5 | `crops/scan013/R2/first_display.jpg` | [430, 350, 1165, 435] | Literal parenthesis, old Z/Q, repeated subscript alphabet/source layer |
| 6 | `crops/scan013/R2/cette_cancelled.jpg` | [1175, 505, 1585, 571] | Acute on cetté and following cancelled cells |
| 7 | `crops/scan013/R2/plus_grand_du.jpg` | [425, 550, 995, 641] | Insertion target; cancelled pair after morceau |
| 8 | `crops/scan013/R2/statement_underlines.jpg` | [192, 720, 1610, 940] | Exact rule distribution and et un left endpoint |
| 9 | `crops/scan013/R2/bprime_opening.jpg` | [550, 995, 1125, 1080] | Opening x-outs, paired primes, short round section index |
| 10 | `crops/scan013/R2/Q_cycle_prefix.jpg` | [1190, 973, 1540, 1073] | Prefix source layer and curved placement guide |
| 11 | `crops/scan013/R2/bprime_product_corrections.jpg` | [480, 1065, 1158, 1153] | Cancelled e courbe; cancelled Cx; X/Y correction |
| 12 | `crops/scan013/R2/bprime_nul_coefficients.jpg` | [258, 1137, 1055, 1218] | Double rule, de/dx, old Z under left Q, coefficient subscripts |
| 13 | `crops/scan013/R2/hypthese.jpg` | [958, 1390, 1455, 1460] | Missing o in hypthèse |
| 14 | `crops/scan013/R2/final_zprime.jpg` | [178, 1737, 972, 1824] | Overprinted initial z/Z, parallel formulas and round indices |
| 15 | `crops/scan013/R2/regulier_insertion.jpg` | [1150, 1892, 1385, 1974] | Word and hook as part of placement guide |
| 16 | `crops/scan013/R2/proof_cycle_group.jpg` | [186, 1310, 425, 1389] | Raised n source layer and ordinary cycle-group alphabet |

## Explicit line-by-line coverage

Line numbers here are this report's labels, following the visible typewriter baselines; they do not insert numbering into the transcription. Hyphenated end-of-line fragments were joined only where a word is continued. The lexical S-morphisme remains hyphenated.

| Unit; approximate whole y | First / last words or objects | Reading coverage and disposition |
|---|---|---|
| Top; 65–95 | 4 | Pen number; `handwritten{mspage{4}}`. |
| L1; 170–204 | b) Pour toute courbe … sur k, | All accents and commas read; curve capital remains double-impression/C uncertain. |
| L2; 239–275 | et tout cycle … l'homomorphisme | Z, typed x, C, codimension n and apostrophe read. |
| L3; 310–337 | correspondant | Complete short continuation line. |
| D1; 365–429 | Z:H¹(C) … H^(2n−1)(Y,Qχ(n)) | Every degree, coefficient, lower rule, subscript, parenthesis and arrow read. Closing parenthesis after C retained; old Z/Q correction preserved. |
| L4; 447–486 | a son image … yoga des | i star and (***) read; NB parenthesis continues. |
| L5; 519–562 | motifs, justifiable … condition | Straight quote pairs; cetté; five cancelled cells, final accented-cell uncertainty preserved. |
| L6; 590–629 | signifie que … ayant comme | plus grand placed before morceau; cancelled dx/du/de and Coker retained; level 1 quotes read. |
| L7; 654–698 | réalisation … est nul). | Mechanical crossed adic glyph and pen i star; parenthesis and final stop retained. |
| L8; 732–800 | Sous ces conditions … qui est | Single rules and gaps checked; z∈Zⁿ(Y) is outside the rules. |
| L9; 808–868 | algébriquement … algébri- | Comma after zéro; first-cycle existence; z′∈Zⁿ(X); underlines and the word continuation checked. |
| L10; 878–935 | quement … tels que | Second algebraically-trivial phrase; et un underline endpoint uncertain; third cycle formula and tels que have no rule. |
| D2; 944–983 | a′) z=i*(z′)+z″ | All primes, pen star, plus sign and label; no added punctuation. |
| L11; 1001–1074 | b′) [x-outs] z″=… où Z″ est un cycle | Opening cancellation, paired Z prime strokes, t₁/t_o, comma, où, and Q- insertion read. |
| L12; 1070–1151 | de codimension … homomorphis- | n, live un plus cancelled e courbe, produit, cancelled Cx and X/pen Y, live xC; all pen rules. |
| L13; 1148–1213 | -me nul [x-outs] H¹(C,…)→… | Continuation joined; nul doubly underlined; de/dx retained; newly noticed old Z under left Q preserved; all coefficients/degrees/parentheses and period. |
| L14; 1269–1324 | Démonstration immédiate : … avec | Accents, colon, z=Z(t₁)−Z(t_o) and final avec. |
| L15; 1328–1382 | Z∈Zⁿ(YxC), … [dont le cancelled] | Raised n confirmed typed by the final crop; ordinary Z/H; arrow and degrees; readable deletion retained. |
| L16; 1410–1457 | qui par hypothèse b) … égal au | First hypothèse complete; Im i pen star; second word literally hypthèse; a) retained. |
| L17; 1475–1520 | composé (iv)Z=i(vZ), … puisque | i printed without star in both occurrences; all v/Z/parentheses and right arrow read; H^(2n−1)(X). |
| L18; 1549–1592 | v l'est, donc … si on pose | Ordinary typed Z′ and XxC; accents and comma retained. |
| L19; 1603–1661 | Z″=Z−(ixid_C)*(Z′), … homomor- | id subscript C, pen star and added prime on Z; typed product; continuation. |
| L20; 1683–1737 | phisme nul H¹(C)→… [D'autre part] Il suffit … | Joined word, full cohomology expression, period; deleted D'autre part retained. |
| L21; 1757–1818 | [z′/Z′ overprint]=Z′(t₁)−Z′(t_o), z″=… | Overlap retained as an uncertainty without inferred temporal old/live order. Both complete fibre differences read, including round indices, comma and period. This is a paragraph continuation, not a separate display. |
| L22; 1849–1892 | 3. Mettant ensemble … On | Paragraph onset, number and both 1)/2) references read. |
| L23; 1894–1977 | se donne des schémas … un S- | X/Y/S read; régulier inserted after S; apparent final hook belongs to guide, so no comma supplied after régulier. |
| L24; 1999–2027 | morphisme | Joined to preceding S- as lexical S-morphisme. |
| D3; 2067–2109 | i:Y→X. | Ordinary type letters, colon, pen arrow and final period. |
| Bottom left; 2078–2127 | 12 | Pencil archive number; comment only. |

## Complete comparison and C-doubt accounting

The complete, individually localized list is `result.json` → `differences`: **35 rows**, including **14 C-doubt/earlier-reading rows**. Thirteen rows have `against_C=true`; 27 have `against_H=true`; a row may concern both. Confirmations or choices already admitted among C's alternatives are included even where neither or only H is opposed. The flags record an adopted source-reading difference, not a claim that a fallible witness's entire alternative list is false. Source-layer differences are separated from intended mathematical identification.

H's global statement that the machine ell is chi-shaped is credited. Consequently the recurring chi/ell alphabet choice alone is not counted against H. Likewise H's emph is accepted as equivalent to uline where the extent agrees, and bold Q versus ordinary underlined Q is not by itself an error. H's expressly editorial comments are not transcribed or counted as extraneous source text. Its factual notes concerning old X, inserted Y, the source layer of Q-, and régulier were actually checked.

The comparison index below points to the full exact C/H readings, ink observations, evidence names and boxes in JSON:

| Row | Locus | Against C | Against H | Disposition |
|---|---|---:|---:|---|
| R2-013-01 | L1: curve letter after connexe) | no | yes | Keep double-impression/C doubt. |
| R2-013-02 | D1: punctuation immediately after C | no | yes | Keep literal closing parenthesis after C. |
| R2-013-03 | D1: old integer coefficient under the left Q | no | yes | Preserve typed old Z under pen Q. |
| R2-013-04 | D1: left coefficient subscript | yes | no | Mechanical crossed subscript; no pen ell. |
| R2-013-05 | D1: right coefficient subscript | yes | no | Same mechanical source layer at right. |
| R2-013-06 | L5: quotation marks around conjectures standard | no | yes | Use actual straight quote pairs. |
| R2-013-07 | L5: cetté | no | yes | Resolve to accented cetté. |
| R2-013-08 | L5: cancelled cells after cetté | yes | yes | Visible x-outs; do not reconstruct a whole même. |
| R2-013-09 | L6: cancelled pair after morceau | no | yes | Keep dx/du/de; visible x dominates second cell. |
| R2-013-10 | L6: quotation marks around de niveau 1 | no | yes | Use actual straight quote pairs. |
| R2-013-11 | L6: cancelled Coker before ayant | no | yes | Preserve readable cancelled Coker. |
| R2-013-12 | L7: letter in adic adjective | yes | no | Adic glyph is mechanical, not separate pen ell. |
| R2-013-13 | L8–L10: main conclusion underline distribution | no | yes | Restore distinct underline bands and their gaps. |
| R2-013-14 | L10: underline at et un | yes | no | Keep uncertainty about et in et un rule. |
| R2-013-15 | L11: cancelled opening of b') | no | yes | Keep l'homx/l'hom/Xhomx cancellation doubt. |
| R2-013-16 | L11: second section index in b') | yes | yes | Mark first o/0 subscript doubt. |
| R2-013-17 | L11: source layer of inserted Q- prefix | no | yes | Keep typed/handwritten Q- source-layer alternative. |
| R2-013-18 | L12: cancelled text following live un | no | yes | Cancelled old ending e and courbe are readable. |
| R2-013-19 | L12: cancelled Cx cells before X/Y | no | yes | Preserve both visible cancelled Cx cells. |
| R2-013-20 | L12: X replaced by pen Y | no | no | Confirm typed X cancellation and pen Y replacement. |
| R2-013-21 | L12: underline distribution around codimension and product | no | yes | Keep n and the product outside prose rules. |
| R2-013-22 | L13: double underline under nul | no | yes | Preserve two separate rules beneath nul. |
| R2-013-23 | L13: cancelled word after nul | no | yes | Keep de/dx cancellation doubt. |
| R2-013-24 | L13: old Z beneath left Q coefficient | yes | yes | Preserve the additional old Z under left Q. |
| R2-013-25 | L13: left coefficient subscript source layer | yes | no | Mechanical crossed left subscript. |
| R2-013-26 | L13: right coefficient subscript source layer | yes | no | Mechanical crossed right subscript. |
| R2-013-27 | L14: second section index in opening proof formula | yes | yes | Carry first o/0 doubt to proof index. |
| R2-013-28 | L15: cancelled dont le | no | yes | Preserve readable cancelled dont le. |
| R2-013-29 | L16: spelling of second hypothesis reference | no | yes | Resolve literal hypthèse; no missing o supplied. |
| R2-013-30 | L20: cancelled D'autre part | no | yes | Preserve readable cancelled D'autre part. |
| R2-013-31 | L21: initial overprinted z' / Z' | no | yes | Keep z/Z overlap; do not assert old/live order. |
| R2-013-32 | L21: second section index in Z' difference | yes | yes | Carry o/0 notation in first final difference. |
| R2-013-33 | L21: second section index in Z'' difference | yes | yes | Carry o/0 notation in second final difference. |
| R2-013-34 | L20–L21: proof final equalities remain paragraph continuation | no | yes | Keep proof formulas within their paragraph. |
| R2-013-35 | L23: inserted régulier and adjacent hook | yes | no | Guide hook is not a comma after régulier. |

### All packet C doubts and notation entries

| Packet item | Outcome and evidence |
|---|---|
| Doubled first C | Still uncertain; two displaced contours are visible (`first_curve_C`); row 01. |
| cetté/cette; deleted même/xxxxé | Acute on cetté resolved; old full même not recovered. Five visible cancellation cells, possible final accented e; rows 07–08. |
| Beginning b′), deleted l'hom/l'homx/Xhomx | Alternatives retained with l'homx first; terminal visible x-out documented; row 15. |
| Cancelled e courbe/courbe | A residual e after live un is visible; old e courbe retained; row 18. |
| Product cancelled C/Cx; X/pen Y | Both Cx cells visible; x-out versus old product role remains interpretive. X crossed and pen Y confirmed; rows 19–20. |
| Cancelled de/dx after nul | Both retained, de first; row 23. |
| hypthèse/hypothèse (listed twice in packet) | The sequence lacks o and reads hypthèse; row 29 covers both duplicate entries. |
| Final z′/double Z′/Z′ | Overlapping small and larger impressions; candidates retained, no temporal layer imposed; row 31. |
| Cancelled du/de/dx after morceau | Visible dx first; old vowel not recoverable; row 09. |
| H¹(C)Q… versus H¹(C,Q…) | Parenthesis after C is clear; literal malformed expression retained; row 02. |
| Zⁿ cycle-group alphabet | Ordinary single Z and raised serifed n confirmed, including the proof (`proof_cycle_group`). No new alphabet or pen n supplied. |
| Underlined Q prefix and coefficients | Single Q plus independent rule confirmed. Left first coefficient retains old Z as C recorded; left b′) coefficient also retains an old Z not preserved by C/H. Prefix source layer remains typed/pen uncertain; rows 03, 17, 24. |
| Z double primes; i stars | Paired upper pen strokes in both b′) terms and individual pen stars inventoried. Remaining typewritten primes are retained; final initial z/Z uncertainty remains. C's general prime note is credited, so merely missing a handwriting wrapper in one inline occurrence is not treated as a new H error. |
| H, Z, Coker, Im, id_C and typed x products | All checked individually on the page. Ordinary letters/function names retained. Source typed x is encoded literally; H's product macro alone is not treated as a semantic error. |
| Explicit conditional motif note | The author's conditional admission is retained, not strengthened into an unconditional assertion. |
| Handwritten 4; section 3 | Both confirmed and included; archive 12 is kept only as a comment. |

## Full inventory and source layers

The canonical full inventory is `result.json` → `inventory`: **63 individually identified entries**. It contains every text block and all three displays; both page numbers; each deleted word/cell group; the two Z→Q overwrites; the X→Y correction; every separate prime, star, membership or arrow insertion; all individual prose rules, including each physical continuation across a typewriter line break and both rules under nul; both verbal insertions and their guides; the Q- prefix; and the final z/Z overprint with no assigned temporal direction. Hand attribution remains “pen; personal attribution not established from this page” unless the evidence supports typewriter or pencil-like source layers.

The inventory does not treat normal typewriter accents, typed mathematical exponents, or recurring coefficient underscores as new pen interventions. They remain part of the complete text/display entries and notation table. The raised n in the proof was specifically checked and has the ordinary serifed typed shape. No extra authorial mark was inferred from isolated pale scan traces.

Observable paragraph cues are retained: an indented opening b); a separate indented conclusion after the motivic parenthesis; the a′)/b′) structure; an indented proof after a blank gap; and paragraph 3 after the proof. The last line of the proof begins at the normal body margin and follows its preceding line without an independent display gap. No extra paragraph is inferred from an ordinary line break.

## Mathematical reading and actual check

The page states a cohomological image condition for every codimension-n correspondence on Y x C, with C proper, smooth and connected. It then interprets that condition motivically **under the author's explicit admission**: “Si on admet le yoga des motifs, justifiable par les” followed by the source-quoted conjectures standard. The inserted plus grand qualifies morceau. This is the author's conditional explanatory gloss, not a theorem checked here.

Under the cited conditions, an algebraically trivial z on Y is claimed to equal i*(z′)+z″, with z′ algebraically trivial on X and z″ a difference of fibres of a Q-cycle inducing the zero map on the indicated cohomology groups. The proof builds Z′ from vZ and sets Z″=Z−(i x id_C)*(Z′). The text writes (iv)Z=i(vZ) using i without a star. H's note about that abuse agrees with the ink; I do not insert a star into those two occurrences.

**Actual check performed — targeted proof check, statement `36-013-proof-kernel-identity`:** Write J for the map printed as i or i*, and A for the map printed as Z. Assume exactly the properties invoked in this proof: the image of A lies in Im J, and Jv is the identity on Im J. For every u, Jv(Au)=Au. Therefore (A−JvA)(u)=0. Conditional on the asserted realization of vA by Z′ and the action of the pullback being J, the constructed Z″ induces zero. This checks the local linear-map step. It does not establish the earlier hypothesis a), algebraicity of v, the representation of algebraically trivial cycles as fibre differences, or the motivational standard-conjecture claim. No formal certificate and no independent re-proof of those claims was attempted.

Mathematical diagnostics prompted no silent repairs. The source's H¹(C)Q… punctuation is malformed, but the closing curve after C is visible and retained. The final z/Z overlap is not resolved from the role expected for an algebraically trivial cycle. The spelling hypthèse is not filled out from context. The o/0 distinction is treated as a literal alphabet question and marked at its first occurrence, not settled from the meaning of a section index.

Paragraph 3 begins the relative setup: X and Y proper and smooth over regular connected S, with i:Y→X. The comma-like hook after the inserted régulier is physically continuous with the placement guide, so it is not added as punctuation.

## Remaining uncertainties

`result.json` → `unresolved` gives **11 entries**: the first curve capital; chi/ell alphabet; the cancelled cells after cetté; dx/du/de; the et un underline extent; the opening l'homx/l'hom/Xhomx cancellation; o/0; Q- source layer; de/dx after nul; final z′/Z′/double-impression interpretation; and whether the visible cancelled x next to C belonged to the old product or is itself a cancellation cell. Each is represented in place or, for the visible Cx cell whose glyph is certain but cancellation role is not, explicitly documented without asserting an old product.

## Structural verification and brief feedback

Structural checks passed: balanced LaTeX braces; paired inline-math delimiters; exactly three balanced display pairs; no undeclared or disallowed macros; valid JSON; 35 unique difference IDs; complete required fields; valid difference and inventory kinds; whole-image bounding boxes in range; and all 13 saved crop files plus their helper metadata present. This was a structural verification only; LaTeX was **not compiled**.

No substantive change to brief v04 is proposed. Its visible-x-out distinction was especially useful here. Uneven handwritten rule endpoints can leave word-level scope uncertain even after a tight view; preserving a local alternative is preferable to assigning emphasis from sentence meaning.


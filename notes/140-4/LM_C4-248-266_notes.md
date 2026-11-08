# LM_C4-248-266 — Editorial and research notes

## 1. Source, pagination, and transcription conventions

This package contains a diplomatic French reading of all 19 supplied images, in filename order, with a LaTeX transcription and a separate element inventory. All manuscript references below are to the attached excerpt of Grothendieck (1981); the source identification and date follow the attached task brief. No published transcription, external edition, or secondary literature was used to supply readings.

The filename scan number is one greater than the small archival page number and printed footer. The transcription uses the filename number in `\scanpage`; `\mspage` records only the large authorial folio number actually visible at the top. The small archival pagination and printed institutional footer are not included as manuscript text.

| Filename scan | Archival footer | Visible author folio |
|---|---:|---:|
| 248 | 247 | — |
| 249 | 248 | 772 |
| 250 | 249 | — |
| 251 | 250 | 773 |
| 252 | 251 | — |
| 253 | 252 | 774 |
| 254 | 253 | — |
| 255 | 254 | 775 |
| 256 | 255 | — |
| 257 | 256 | 776 |
| 258 | 257 | — |
| 259 | 258 | 777 |
| 260 | 259 | — |
| 261 | 260 | 778 |
| 262 | 261 | — |
| 263 | 262 | 779 |
| 264 | 263 | — |
| 265 | 264 | 780 |
| 266 | 265 | — |

The fragment preserves source abbreviations, surviving cancelled wording, insertions, marginal notes, formula labels, and visible inconsistencies. Paragraphs are reflowed; manuscript line endings within a paragraph are not reproduced. The differing placements of stars, tildes, singleton braces, underlines, and abbreviations have not been made mathematically uniform. An apparently redundant or incomplete expression remains in the fragment when supported by the ink.

`\unsure{reading|alternative}` records competing readings; the first is preferred but is not asserted as certain. A single-argument uncertainty records an insecure reading for which no equally plausible alternative is available. `\illegible{n}` is limited to obliterated prose and gives an estimated word count; no formula or diagram symbol is replaced by such a placeholder. Repeated doubts may share one explanatory row where the same palaeographical issue recurs. Approximate positions in the tables refer to the handwritten images, not to source-code line numbers.

The LaTeX is intentionally a fragment without a preamble or macro definitions. Its editorial macros must be defined by the receiving document, with support for their occurrences in both prose and mathematics; the mathematical and diagram content uses standard LaTeX/AMS notation and TikZ-CD, with TikZ for the visible emphasis strokes. No scan images are embedded. The final word on scan 266 remains unfinished as written: “s'expri-”.

## 2. Table of doubts

The fragment contains 174 explicit uncertainty marks and 6 prose illegibility marks, the latter covering an estimated 7 words. The records below include the cancelled and overwritten material.

### Scans 248–252

There is one entry below for each of the 56 uncertainty or illegibility marks in this section. Positions follow the handwritten page, not the reflowed LaTeX. A repeated symbol receives a separate entry at each occurrence; the broad upper and lower serifs on the interval letter make `I` versus `\overline I` uncertain in scan 252.

| Scan | Approximate line or position | Reading in the transcription | Alternatives / qualification | Confidence |
|---|---|---|---|---|
| 248 | top cancellation above first line | `Bref.` | No secure alternative; entire word heavily cancelled | low |
| 248 | line 4, cancelled after catégorie | `rev.` | rev (abbreviation punctuation uncertain) | medium |
| 248 | line 7, after s’identifie | `canoniquement` | canonique (ending highly abbreviated) | medium |
| 248 | line 11, cancelled after D_x^* | `est` | et | low |
| 248 | line 11, cancelled after est | `\illegible{1}` | One obliterated word; no recoverable reading | low |
| 248 | line 12, cancelled after D_{x,i}^* | `isomorphes à` | isomorphe à | medium |
| 248 | above cancelled isomorphes à | `provenant` | No secure alternative; inserted word is tightly compressed | low |
| 248 | line 14, after disques | `forment` | forme (final stroke ambiguous) | medium |
| 248 | line 18, de … fondamental | `groupoïde` | groupe | low |
| 248 | line 18, cancelled mathematical token before T_x | `\mathbb{Z}` | No secure alternative; overwritten letter | low |
| 249 | middle, after Rev(U) est | `multigaloisienne` | multigaloisien (compressed final strokes) | medium |
| 249 | middle, condition following U and inserted loc | `0` | 1 (digit overlapped by insertion stroke) | low |
| 249 | equation (60), label | `k_x` | \kappa_x (Latin/Greek letter uncertain) | medium |
| 250 | upper paragraph after encore | `par` | pour (cancelled) | low |
| 250 | upper paragraph en termes d’… | `autom.` | automorph. (abbreviation compressed) | medium |
| 250 | upper paragraph between l’ and opération | `hom` | hom. (cancelled word and punctuation) | low |
| 250 | fiber-product subscript, cancelled token | `D` | U overwritten by U | low |
| 250 | middle right cancellation before NB | `\illegible{1}` | One obliterated word or letter | low |
| 250 | middle right cancellation after NB | `Chaque fois` | chaque fois (capital uncertain) | medium |
| 250 | middle paragraph ou, plus … | `généralement` | généralemt (ending compressed) | medium |
| 250 | pi_1 after Pour le comparer, cancelled token | `S` | No secure alternative; scribble | low |
| 250 | quoted phrase chem. de … | `domin.` | domination (abbreviation/ending uncertain) | low |
| 250 | between D_x^{*~}/U and U tilde/U | `à` | : (two isolated strokes) | medium |
| 250 | parenthesis after (62), cancelled token before U | `\widetilde U` | No secure alternative; overlaid writing | low |
| 250 | bottom beneath fibre, upward curved arrow | `U` | u (may belong to the overlapping NB) | low |
| 250 | bottom NB after si | `\illegible{1}` | One heavily cancelled word before D_x^{*~} | low |
| 250 | bottom NB d’un disque … | `épointé` | pointé (initial stroke uncertain) | medium |
| 250 | bottom NB beginning of first Revuni formula, cancelled token | `D` | R (overwritten beginning) | low |
| 250 | bottom NB connection after le choix de (62) | `équivaut à` | équivaut au choix de (crowded line at bottom border) | low |
| 250 | bottom-right NB celui d’un … | `chemin` | chemins (ending uncertain) | medium |
| 250 | bottom-right NB opening of final parenthesis | `U` | si U (possible extra short word) | low |
| 250 | bottom-right NB final parenthesis | `loc.` | les rev. (compressed strokes) | low |
| 250 | bottom-right NB end | `1-connexe` | 1-connexes (final stroke uncertain) | medium |
| 251 | top, line 1, after est | `mod` | mot?; abbreviated modulo? | low |
| 251 | top, canceled word beneath élément | `autom.` | autre abréviation sous la rature | low |
| 251 | top, line 2 left, canceled abbreviation | `int.` | intérieur abrégé | medium |
| 251 | equation (63), first symbol | `\pi_s\|\pi` | small mark may be subscript s or overwritten punctuation | low |
| 251 | below (63), second prose line | `change\|compose` | overwritten joining strokes; cancellation status uncertain | low |
| 251 | lower-left marginal C heading, parenthesis | `jouant` | faisant? | medium |
| 251 | lower-left marginal C heading, canceled word | `origine` | origines? | low |
| 251 | lower-left marginal C heading, quoted abbreviation | `pts\|pt` | plural stroke unclear | medium |
| 252 | line 1, interval definition I=[0,1] | `I\|\overline I` | capital I with broad serifs or separately barred I | medium |
| 252 | line 2 left, bracketed interval germ | `I\|\overline I` | same serif/bar ambiguity | medium |
| 252 | line 2, after germe | `résiduel` | voisiné initially considered; terminal l favors résiduel | medium |
| 252 | line 2, after de before en 0 | `I\|\overline I` | same serif/bar ambiguity | medium |
| 252 | upper-left diagonal marginal note, second line | `paramétrer` | paramétrés? | medium |
| 252 | upper-left diagonal marginal note, fourth line | `voisinages` | voisinage | medium |
| 252 | upper-left diagonal marginal note, near end | `sous-ensemble` | sous-ensembles | medium |
| 252 | upper-left diagonal marginal note, penultimate line | `certaines` | terminal letters compressed | medium |
| 252 | equation (66), source bracketed germ | `I\|\overline I` | same serif/bar ambiguity | medium |
| 252 | equation (66), operator before subscript x | `\mathrm{germ\,rés}` | germes; accent/word-spacing uncertain | low |
| 252 | first prose line after (66), bracketed germ | `I\|\overline I` | same serif/bar ambiguity | medium |
| 252 | first prose line after (66), after germe | `résiduel` | voisiné initially considered | medium |
| 252 | equation (67), canceled symbol beside φ | `\gamma` | possibly overwritten φ or another letter; ink dense | low |
| 252 | lower paragraph, canceled word above abélienne | `galoisienne` | galoisien; replacement repeats word | medium |
| 252 | equation (69), bracketed interval germ | `I\|\overline I` | same serif/bar ambiguity | medium |

### Scan 253

| Scan | Approximate line / position | Reading | Alternatives | Confidence |
|---|---|---|---|---|
| 253 | Below factorisation diagram | iso can. | Abbreviation ending and final stop faint; “iso can” also possible | medium |
| 253 | Bottom paragraph, after “si” | le | l’; residual apostrophe and corrected article are superposed | low |
| 253 | Bottom right, struck-through words | Prenons | Pour cela; final letters heavily intersected by cancellation | low |

### Scan 253 — interval glyph

| Scan | Approximate line / position | Reading | Alternatives | Confidence |
|---|---|---|---|---|
| 253 | Equation (70), bracketed interval-germ argument | I | overline I; a single detached top stroke could be an ordinary serif | medium |
| 253 | First factorisation diagram, left object | I | overline I; same single-top-stroke ambiguity | medium |
| 253 | Equation (71), right-hand universal-cover argument | I | overline I; same glyph | medium |
| 253 | Composite diagram immediately above (72), left object | I | overline I; same glyph | medium |
| 253 | Equation (72), right-hand fundamental-group argument | I | overline I; same glyph | medium |

The first pass treated the detached upper stroke as an overbar. A fresh crop comparison with the definition on scan252 and the ordinary interval I gave no separate second top stroke; the fragment now explicitly flags the alternatives and prefers plain I. This is a visual reassessment, not a mathematical normalisation.

### Scan 254

| Scan | Approximate line / position | Reading | Alternatives | Confidence |
|---|---|---|---|---|
| 254 | Top line, struck-through segment after “l’origine” | illegible{2} | A trial reading “en un” cannot be supported through the cancellation; estimated two words | low |
| 254 | Second line, struck-through first word | conduit | Cancellation obscures the middle; “considéré” is possible | low |
| 254 | Second line, struck-through last word | hom. | Final stop uncertain; “hom” | medium |
| 254 | Middle paragraph, name of the set of germs | Germarc | Courarc; the capital and compressed medial letters are ambiguous | low |
| 254 | After gamma′, immediately before “les isomorphismes” | cancelled un | cancelled les | low |
| 254 | Equation (75), underlined category label | Germarc | Courarc; same compressed label as in the prose | low |

### Scan 255

| Scan | Approximate line / position | Reading | Alternatives | Confidence |
|---|---|---|---|---|
| 255 | Upper, cancelled word after “en x” | Germ | Only the capital and compressed horizontal remainder survive clearly | low |
| 255 | Equation (76) | Germarc diff | Courarc diff; spacing before diff is not fully determinate | low |
| 255 | After “pleine de”, cancelled symbol | C_x (calligraphic) | G_x (calligraphic); overstriking obscures the letter and subscript | low |
| 255 | Upper paragraph, underlined category | Germarc | Courarc; same reading problem as scan254 | low |
| 255 | Equation (79), source category | Germarc diff | Courarc diff; same compressed lettering | low |
| 255 | Bottom paragraph, “l’application … à” | associant | Final strokes do not independently distinguish associant from a compressed ending | medium |

### Scan 256

| Scan | Approximate line / position | Reading | Alternatives | Confidence |
|---|---|---|---|---|
| 256 | Equation (80), lower right, after “dans” | 𝕊_x^* | 𝕊_x; a star-shaped superscript is visible and is retained rather than mathematically corrected | medium |
| 256 | Immediately above “Au lieu”, cancelled word | illegible{1} | Trial reading “Je” cannot be substantiated under the dense overwriting | low |
| 256 | Equation (81), tiny cancelled mark at lower left of parenthesised approximation label | right arrow | tilde; compact overwritten mark below the retained double tilde | low |
| 256 | Equation (82), before “être réduits” | pouvant | Initial letter has heavy additional strokes; remainder supports the reading | medium |
| 256 | Equation (82), before “des pts” | à | Vowel is overwritten but its accent is visible | medium |
| 256 | After “c’est un ensemble ordonné,” | et on | donc; heavily joined and overwritten opening letters | medium |

### Scan 257

| Scan | Approximate line / position | Reading | Alternatives | Confidence |
|---|---|---|---|---|
| 257 | Top, cancelled symbol after “soit” | underlined A_{0x} | underlined A_x; deletion intersects the subscript and no comma is securely visible | low |
| 257 | Middle, cancelled symbol between “arc” and A | double-stroked S | xi; dense overwriting leaves a vertical stem and several loops | low |
| 257 | Middle, after “isom d’inclusion” | ds | dans; highly contracted form, without a confidently visible abbreviation point | medium |

### Scans 258–262

| Scan | Approximate line or position | Reading retained | Alternatives or uncertainty | Confidence |
|---|---|---|---|---|
| 258 | l. 3, cancelled word after est | connexe | The overwritten word may have a different opening; no secure alternative. | low |
| 258 | l. 3, cancelled short word before son | le | The compact cancellation may conceal a different short word. | low |
| 258 | l. 3, fundamental-group symbol after son | \pi_1 | \Pi_1; the handwritten letter has a capital-shaped outline, whereas surrounding groupoid symbols also use a capital Pi. The exact alphabet is not secure here. | medium |
| 258 | l. 4, cancellation replaced above the line | un x de | The first and last words are heavily crossed; x is visible. | low |
| 258 | l. 5, sphere symbol S_x | \mathbb S_x | A vertical/double-stroked S is visible; the precise intended typographic alphabet is uncertain. | medium |
| 258 | (88), second line of target | au | en | medium |
| 259 | (89), source second line | au | en | medium |
| 259 | paragraph after (89), l. 1 | va associer | on associe; the short first word and the final inflection of associer are compressed. | medium |
| 259 | paragraph after (89), l. 1, cancellation after membership sign | \mathcal E | Another calligraphic capital may underlie the dense overwriting. | low |
| 259 | paragraph after (89), cancelled l. 2 | sous-espace | The cancellation crosses the joining strokes and possible hyphen. | medium |
| 259 | paragraph after (89), last word | résiduel | Letters are largely readable; whether its horizontal stroke is a cancellation or an underline remains uncertain (encoded as cancellation). | medium |
| 259 | start of paragraph above cones, cancelled text | Les demi-droites | La demi-droite; the number/endings are obscured by the cancellation. | low |
| 259 | after cônes, cancelled adjective | ouverts | Only portions of loops survive the dense crossing. | low |
| 259 | right of Tang_x(X), cancelled false start | disti | Possibly disti. with terminal abbreviation point. | low |
| 259 | above l'espace ... entier, insertion | tang^t | tangent; abbreviated ending and attachment are unclear. | low |
| 259 | cancelled clause before Considérons | Soit C un | The terminal short word may differ. | low |
| 259 | insertion above cancelled Soit C | C A_x | C ∈ C A_x; no separate membership sign is securely distinguishable in the compressed cluster. | low |
| 259 | left of (90), cancelled short word | un | A short crossing contains no secure alternative. | low |
| 259 | (90), cancelled mark between source and arrow | & | Possibly a cancelled arrow/connection sign; retained as a doubted ampersand. | low |
| 259 | lower paragraph after Mais considérons la, cancellation | famille | ensemble des; heavily struck through. | low |
| 259 | lower paragraph before cônes, cancelled text below inserted des | arcs | Possibly des; the upper word des is taken as an insertion. | low |
| 259 | lower paragraph before C strictement, cancelled sign | ∈ | The overwritten sign may be an inclusion sign. | low |
| 260 | top overlapping correction, cancelled two words | de cette | du filtre; the middle layer lies between the original deletion and the uppermost insertion. | medium |
| 260 | l. 2, after V∩(C'\{0}) | comma + où | :; the small ink marks can also be punctuation. | low |
| 260 | l. 7, cancelled symbol before D_x* | X_x | X; subscript-like strokes are indistinct. | low |
| 260 | l. 8, cancellation before isom. | est é | et il; the last small accented character may be a false start of évidemment. | low |
| 260 | l. 11–12, adjective broken across lines | simétriques | symétriques; the apparent i-dot may be an accent or a joining stroke. | medium |
| 260 | l. 14, between variable and pour | i.e. | The abbreviated cluster could be another connective. | low |
| 260 | right-side inclusion insertion, cancelled capital | A | Only the capital-shaped overwritten mark is secure. | low |
| 260 | penultimate line, after via la | vérification | vérific^t (abbreviated form); final strokes are compressed. | medium |
| 260 | last line, initial cancelled short word | par | The small scribble is not secure. | low |
| 260 | last line, before plus haut | explicitée | explicité; final ending is faint and overwritten. | medium |
| 261 | l. 5, insertion before deux | les | des | medium |
| 261 | unnumbered Isom diagram, upper-left object's first cover | star in superscript | The small mark is tick-like; interpreted as the same star appearing clearly on the second cover. | medium |
| 261 | unnumbered Isom diagram, before comma after first cover | right brace } | A double curved stroke is visible; it may be an overwritten parenthesis rather than a brace. | low |
| 261 | line after unnumbered diagram, cancelled word | bonne | Word fairly legible, but the horizontal line could instead be an underline. | medium |
| 262 | first body word below diagram (93), overlapping the margin note | Le | The L-shaped curve and short terminal stroke are partly crowded by the diagonal note; no independent alternative is securely readable. | medium |
| 262 | lower paragraph after repeated (90), between de and Theta | ce | The word is reduced to a straight short stroke and may instead be a dash. | low |

### Scan 263

| Scan | Approximate line / position | Reading | Alternatives | Confidence |
|---|---|---|---|---|
| 263 | 1, parenthesis | diff. | diff, without abbreviation stop | medium |
| 263 | 10, end of first paragraph | standard | Capital initial possible; last strokes compressed | medium |
| 263 | 10, terminal marks | ... followed by a stop | One extended terminal stroke and one stop | low |
| 263 | 11, above-line insertion | u | φ | medium |
| 263 | 11, after inserted letter | un un | First group may be a shortened overwritten word rather than a repeated un | low |
| 263 | 12, insertion over deletion | automorphisme | Initial and abbreviated internal strokes compressed | medium |
| 263 | 14, deletion before autom. | des | les | low |
| 263 | 14 | autom. | autom, with no separate stop | medium |
| 263 | display, equation number | 95 | 94; final numeral is overwritten | medium |
| 263 | display, both left superscripts | u | φ | medium |

### Scan 264

| Scan | Approximate line / position | Reading | Alternatives | Confidence |
|---|---|---|---|---|
| 264 | upper-left marginal note, last line | p. 783 | Last digit could be a closing flourish rather than 3 | medium |
| 264 | diagonal section heading after colon | la structure | structure; introductory strokes compressed | low |
| 264 | displayed tangent-space equality, middle symbol | deleted V | double-stroked V; the crossbar could belong to the letter | low |
| 264 | left margin beside 1) | sous-entend | Last strokes of sous and first strokes of entend compressed | medium |
| 264 | cancelled sentence after D* equality | resp. | resp without an abbreviation stop | medium |
| 264 | cancelled sentence, right edge | universels | Ending partly lost beneath cancellation and at page edge | low |
| 264 | before A_(X,x) | cancelled script A | membership sign; heavily overwritten | low |
| 264 | between A_(X,x) and A_x | ou | overwritten connective | medium |
| 264 | cancelled line below cone-set definition | secteurs angulaires | Both word endings obscured by the cancellation stroke | low |
| 264 | same line | propres, then replacement propres | Final plural stroke is compressed | medium |
| 264 | after “on désigne par”, cancelled symbols | tilde A, tilde C | f(A), f(C); both overwritten | low |
| 264 | connective between those symbols | ou | overwritten | low |
| 264 | superscribed replacements | Ep(A), Ep(C) | E_p(A), E_p(C); relative baseline of p ambiguous | medium |
| 264 | lower-left marginal note | épaississement | Beginning touches the scan border | medium |
| 264 | same marginal note, cancelled word | image | germe; dense ink | low |

### Scan 265

| Scan | Approximate line / position | Reading | Alternatives | Confidence |
|---|---|---|---|---|
| 265 | (97), first Γ argument, cancelled glyph | tilde A | S; overwritten compact symbol | low |
| 265 | (97), second Γ argument, cancelled glyph | tilde A | Only parts of the old mark remain | low |
| 265 | (97), second Γ argument and last equality | Ep(A) | E_p(A); p baseline ambiguous | medium |
| 265 | (98), Isom subscript | T_x | barred T_x; separate upper bar not secure at this size | medium |
| 265 | (98), cancelled second argument | D_x^(star tilde)(tilde A) | The parentheses and interior argument are heavily crossed out | low |
| 265 | (98), parenthesis immediately after cancellation | ) | May belong within the cancelled span | low |
| 265 | (98), replacement second argument | Ep(A) | E_p(A) | medium |
| 265 | just before “une inclusion” | one cancelled unreadable word | Possibly Si or Soit; neither is securely supported | low |
| 265 | (99), both right-hand arguments | Ep(A′), Ep(A) | E_p(A′), E_p(A) | medium |
| 265 | (99), connector between D expressions | short dash | Right arrow; no arrowhead is secure in the scan | low |
| 265 | cancelled text before (101) | A maps to H(A) définit | Left-pointing connector; last word compressed | low |
| 265 | prose before (102) | du | de | medium |
| 265 | (102), left descending arrow | ρ | γ | medium |

### Scan 266

| Scan | Approximate manuscript position | Reading in the fragment | Alternatives or qualification | Confidence |
|---|---|---|---|---|
| 266 | First line, cancelled word after « est » | `isomorphe` | The overlaid cancellation obscures most internal letters; this is a tentative reading of the retained contours. | low |
| 266 | (103), superscript above S at the right | `*` inside a deletion | The crossed superscript could be a different abandoned symbol; the following tilde is clear. | low |
| 266 | (103), before the lower Revuni | `\mathbb S` inside a deletion | Heavily overwritten abandoned symbol. | low |
| 266 | (105), overwritten subscript of the right-hand Hom | deleted `\underline{\operatorname{Revuni}}`, with inserted `\mathbb S_x` above | Several strokes are superposed; neither the exact extent of the old category label nor the final subscript is secure. A second reading supports the final uni strokes in the deleted label. | low |
| 266 | Diagonal left note beside (105), opening | `i.e. on a pour` | Compressed diagonal script; the last word is especially abbreviated in its strokes. | medium |
| 266 | Same note, after A,A′∈A_x | `l'iso. can` | The compressed letters could be `l'isom. can`; no expansion has been made. | medium |
| 266 | Paragraph beginning « Ceci », crossed word | `fait` | `étant`; the cancellation leaves very little usable ink. | low |
| 266 | Same paragraph, after « essentiellement » | `constant` | The ending is retraced; no different word is confidently readable. | medium |
| 266 | Near the bottom, words replaced by « Cet ens » | `On a donc` | The long deletion crosses the middle and last word. | low |
| 266 | Line immediately before (106), overwritten word | `torseurs` | `foncteurs`; the final form is retraced, with an exceptionally tall initial stroke. | low |
| 266 | (106), label on the left | `i_A` | `\widetilde{\imath}_A`; the small stroke over the initial may be a dot or an accent. | medium |


## 3. Abbreviations and notation met

Expansions are suggestions for the notes only. Repeated forms are retained where their punctuation, local meaning, or confidence differs. No expansion is inserted into the transcription.

### Scans 248–252

These proposed expansions belong only to the notes; the transcription keeps the source forms.

| Form as written | Proposed expansion | Location / qualification |
|---|---|---|
| rev. | revêtement, revêtements | Scans 248–252; number follows the context. |
| Rev | revêtements | Underlined category name on these pages. |
| Revuni | revêtement universel / revêtements universels | Scan 250; exact interpretation depends on whether the notation denotes an object or a category. |
| pt | point | Scans 249–250. |
| pts | points | Scan 251 margin; the plural stroke is uncertain. |
| p. ex. | par exemple | Scan 249. |
| syst. | système | Scan 248. |
| def | définition | Formula annotations, including (56), (57), (66). |
| NB | nota bene | Scan 250, including a canceled occurrence. |
| hom | homomorphisme | Scans 249, 251–252; several occurrences have no written full stop. |
| loc | localement | Inserted condition on scan 249, without a securely visible full stop. |
| loc. | localement | Tentative reading at the end of the dense NB on scan 250. |
| autom. | automorphisme | Scan 250 and scan 251; some occurrences are canceled or tightly compressed. |
| int. | intérieur | Canceled abbreviation at the top of scan 251. |
| chem. | chemin | Scan 250, quoted expression. |
| domin. | domination | Tentative reading on scan 250; whether the source writes a full word remains uncertain. |
| i.e. | id est | Scan 250. |
| isom | isomorphisme | Scan 251; no unambiguous full stop after this occurrence. |
| mod | modulo | Tentative reading at the top of scan 251. |
| ext. | extérieur | Scan 251. |
| top. | topologique | Scan 252. |
| sort. | sortant | Scan 252 marginal note. |
| germ rés | germe résiduel | Tentative operator in (66); spacing and accent are uncertain. |
| Ens | ensembles | Final object in (69). |

### Scan 253

| Written form | Proposed expansion (notes only) |
|---|---|
| rev. | revêtement |
| iso can. | isomorphisme canonique |
| déf | définition |
| Rev uni | revêtement universel |

### Scan 254

| Written form | Proposed expansion (notes only) |
|---|---|
| hom. | homomorphisme (cancelled) |
| ens | ensemble |
| Tang | espace tangent |
| Isom | ensemble des isomorphismes |
| Germarc | germes d’arcs, if this is the correct reading of the label |

### Scan 255

| Written form | Proposed expansion / identification (notes only) |
|---|---|
| diff. | différentiable |
| diff (in category name) | différentiables |
| ∀ (within prose) | tout |
| 𝕊_x, 𝕊¹ | Sphere / circle notation rendered with a double-stroked S; the hand sometimes resembles an ordinary S crossed by one vertical stroke |

### Scan 256

| Written form | Proposed expansion (notes only) |
|---|---|
| i.e. | id est |
| pts | points |
| Gr | groupoïde enveloppant |

### Scan 257

| Written form | Proposed expansion / identification (notes only) |
|---|---|
| ens | ensemble |
| isom | isomorphismes |
| ds | dans, if the abbreviated reading is correct |
| & | et |
| Gr_0 | full subgroupoid on point arcs, as defined in this page |

### Scans 258–262

| Form as written | Proposed expansion or meaning, in these notes only |
|---|---|
| cat. | catégories / catégorie (context-dependent) |
| ssi | si et seulement si |
| pts | points |
| l'autom | l'automorphisme |
| i.e. | id est / c'est-à-dire |
| Revuni | revêtements universels |
| Gr | groupoïde (associated groupoid construction) |
| Aut | automorphismes |
| 1-conn. | 1-connexes |
| isom | isomorphisme |
| isom. | isomorphisme |
| l'iso. | l'isomorphisme |
| l'appl. | l'application |
| tang^t | tangent (doubtful reading of superscript abbreviation) |
| 1-connexe | 1-connexe (connected and simply connected in the local usage) |
| vérific^t | vérification (possible, uncertain abbreviated reading) |
| diff. | différentiable |
| déf | définition |
| ess. | essentiellement |
| comm. | commutatif |
| can. | canonique |
| can | canonique (diagram label) |
| iso | isomorphisme |
| hom. | homogène |
| Rev.uni. | revêtements universels (category label; punctuation varies visibly) |
| Revuni. | revêtements universels (category label) |

### Scan 263

Abbreviations: `diff.` = différentiable; `rev.` = revêtement; `autom.` = automorphisme(s); `équiv.` = équivalence; the barred-m sign = même.

### Scan 264

Abbreviations: `ens` = ensemble; `autom` = automorphisme; `rev.` = revêtement; `resp.` = respectivement; `corr.` = correspondance; `uni.` = universel; `p.` = page. `Ep` is apparently associated with the marginal word “épaississement”; its exact typography remains uncertain.

### Scan 265

Abbreviations: `ens` = ensemble; `isom.` = isomorphisme; `déf` = définition; barred-m = même; `Gr` is the label attached to the groupoïde enveloppant; `Tors` denotes the category of torsors in the page's notation.

### Scan 266

| As written | Tentative expansion |
|---|---|
| déf | définition |
| cat. | catégories / catégorie |
| i.e. | id est |
| iso. can | isomorphisme canonique |
| hom. | homomorphisme |
| isom | isomorphismes |
| ens | ensemble |
| barred m | même |
| Revuni / Rev.uni. | revêtements universels |
| Gr | groupoïde enveloppant |


## 4. Legibility and editorial limits

The running prose and most large displays are substantially clearer than the cancellations and marginal additions. The dense NB on scan 250, layered revisions on scans 259–260 and 264, and overwritten symbols on scans 265–266 deserve the greatest caution. Doubt marks indicate editorial limitations, not omissions from the reading.

### Scans 248–252

The main displayed formulae and the broad paragraph structure are substantially more legible than the cancellations. The least secure passage is the NB spread across the bottom and right margin of scan 250: its lines intersect the explanation of (62), and several words are compressed against the frame. I inspected the full pages and magnified or rotated separate crops of the difficult passages; no external transcription or mathematical reconstruction supplied the wording. Three one-word illegibility marks remain, all in canceled prose on scans 248 and 250, and none replaces a mathematical symbol.

In scan 250, the letters read as `y,z` above the right part of (62) belong to the continuation of the marginal NB, “les images dans U”; they are not transcribed as a superscript on `Revuni`. The small curved arrow and `U` below the fiber-functor caption are much less secure and are marked accordingly. The parenthesis begun in the explanation after (62) is not completed editorially. Scan 251 (63) has a small dark subscript-like stroke beside the first pi; the alternatives are retained instead of dropping the mark. Scan 252 (69) has a visibly left-pointing second arrow, from `(Ens)` to the interval-cover category. The upper-left marginal proposal on scan 252 is transcribed in full after inspection in a rotated crop; its compressed word endings retain explicit doubts.

### Scan 253

Scan 253: the main formulas and factorisation are substantially legible. The corrected article before “germe” and the final crossed-out phrase are the least secure readings on this page; the interval-germ I glyph is flagged at each bracketed occurrence because the long detached top stroke may be a serif rather than a distinct overbar. The unbracketed interval in prose remains plain I.

### Scan 254

The crossed-out wording in the top two lines is substantially obstructed by cancellation strokes. The repeated category label is readable only tentatively; it is not silently expanded or replaced. In (74), the first source-cover subscript is written without a visibly separate comma between x and gamma, whereas the second comma is clear; this difference is retained.

### Scan 255

The body and the labels of the three principal equivalences are comparatively clear. The overwritten symbol after “pleine de” is not recoverable with confidence. The two downward equivalence decorations in (79) are drawn as rotated double tildes, and have been reproduced as rotated approximation signs rather than silently replaced by equality signs. The two long marginal emphasis strokes are reproduced in TikZ.

### Scan 256

The two numbered diagrams and the arc-set definition are mostly legible. A cancelled word above “Au lieu” is physically obscured after enlargement; the estimated word count is one. In the final parenthesis, the visible text is “les objets sont les ∈ A_x”; no separately visible A before the membership sign has been supplied. In (80), the unusual apparent star on the circle notation is left as a flagged reading, not silently removed. The tiny overwritten symbol in the equivalence label (81) is separately recorded as a cancellation.

### Scan 257

The main construction, its two-row diagram (84), and the final functor are legible. The two heavily cancelled mathematical symbols are recorded with tentative readings rather than a word-count illegibility placeholder. The objects of (84) are written a and b without singleton braces, whereas the preceding object map explicitly has {a}; that difference is retained. The calligraphic A is visibly underlined in the top definition and in (83), while the later occurrences do not carry equally distinct underlines and are not normalised.

### Scans 258–262

This is a source-only diplomatic reading of the five supplied images. Scan numbers follow filenames: the archive footers read 257–261, one less than the scan labels used here. The large manuscript folios visible in this section are 777 on scan 259 and 778 on scan 261. Archive URLs, institutional footers, and the small archive pagination are excluded.

The main prose and diagrams on scans 258, 261, and 262 are substantially readable, but several short words, endings, and cancelled starts remain uncertain. Scans 259–260 contain the least secure material: several layers of correction overlap, and the distinction between an underline and a cancellation is not always certain. The compressed cone-set notation on scan 259, the topmost correction on scan 260, and the small stray-looking curved mark in the first Isom argument on scan 261 deserve checking against a better original. A visible dot in the right-hand object map of (93) is retained as a dot; no variable has been supplied there. The abbreviated ending “hom.” at the bottom of scan 262 is retained.

The recurring S glyph has a distinct vertical/double stroke; it is represented by \mathbb S. The first occurrence is marked as a typographic doubt and the same representation is used thereafter. No unreadable stretch has been silently replaced by mathematical reconstruction. The doubtful readings listed below include deleted material; their presence does not imply that the cancelled wording can be recovered with confidence.

### Scan 263

The filename scan263 corresponds to the printed archive page 262; the original author folio 779 is retained in the transcription. The large main text is substantially legible. The altered sentence beginning “Soit maintenant” is the least secure passage: an above-line letter, a curved insertion stroke, and two short baseline groups are preserved without silently removing the possible repetition.

### Scan 264

This page contains several layers of revision. The main correspondence (96) is legible, but its abbreviated prose and the lines through the definitions of arcs and cones require caution. The marginal heading and the cancelled symbols replaced by Ep(A), Ep(C) are particularly insecure. The tilde on the final base `\widetilde D_x^*` has been retained even though it may be an inadvertent authorial repetition; no mathematical correction is made.

### Scan 265

Author folio 780 is visible. Most prose and the restrictions/factorization displays can be read securely. The strongest uncertainties are the overwritten first arguments of the two Γ expressions, the cancelled second argument of (98), the exact typography Ep versus E_p, and a short stroke in (99) that does not show a secure arrowhead. The fragment retains the apparently surviving closing parenthesis beside the deletion in (98) with a doubt mark; it does not silently rebalance the manuscript formula.

### Scan 266

The main argument and the arrows in (103)–(106) are reasonably clear. The cancelled word in the opening line, the right-hand Hom subscript in (105), and the overwritten word before (106) are the least secure readings. The definition involving S with indices x,A has been left on the upper row of (103), where it is written, rather than moved to the object row. The final word is physically unfinished at the page boundary and is retained as « s'expri- ».


## 5. Research notes — separate from the transcription

These observations are in English and do not amend the French transcription. “Unproved claim” identifies a proof obligation or an assertion whose full verification is not given at the cited location; it does not claim that Grothendieck never proves it elsewhere. Later construction within this excerpt may address an earlier announcement. Own ideas are proposed checks, not established results or claims of novelty. Brief quotations and scan/equation references refer throughout to Grothendieck (1981).

### Scans 248–252

These notes distinguish the source's assertions and expectations from proposed checks of my own. They are observations about these five pages only, not claims of priority or claims that the matters are unresolved elsewhere in the manuscript or literature. Citations refer to the supplied manuscript scans.

1. **Scan 248, equation (56) and the following paragraph — unproved claim.** The identification with the orientation module is supported by the sketch that the punctured disks' fundamental groups “forment un syst. projectif constant”. A full proof should specify a cofinal system of representative disks, verify the transition isomorphisms, and show that the identification with the orientation module is independent of the disk and respects reversal of orientation. The word transcribed as “canoniquement” remains a paleographical doubt.

2. **Scan 248, final complete paragraph — unproved claim.** The universal covers are said to “forment un groupoïde connexe”. To make this precise in the setting of germs, one would need existence of these covers, comparison isomorphisms after restriction, and the identification of the automorphism groups with the local orientation module; the source's phrase immediately before “fondamental” is itself uncertain between “groupoïde” and “groupe”.

3. **Scans 249–250, (60)–(61) and the section-functor formula — unproved claim.** Grothendieck announces “je vais définir un hom canonique”, then describes an action on sections of the pullback of a cover. A detailed verification should check naturality in the cover, compatibility with restriction of representatives of the germ, and the left/right action conventions that determine the direction of the induced homomorphism.

4. **Scans 250–251, (62)–(65) — unproved claim.** The chosen comparison of universal covers gives a homomorphism, while the source asserts that its choice-free result is “un hom ext. bien déterminé”. A proof should explicitly calculate how changing the comparison (62) changes the induced isomorphism (63) by conjugation, and then identify the resulting outer homomorphism with that induced by the inclusion of the punctured local germ into `U`.

5. **Scan 252, upper-left marginal note — conjecture (methodological expectation, not an asserted theorem).** The phrase “il serait plus commode pour la suite” proposes replacing the parameterized interval description by a germ of a subset of `X`, “satisfaisant à certaines propriétés”. The properties are not supplied in this note; recovering the intended restrictions and comparing the two descriptions is a concrete task left open here.

6. **Scan 252, (66)–(69), especially the final paragraph — unproved claim.** The text proposes to use the arc-germ morphism “pour définir un foncteur fibre”. A full argument should identify the interval-germ covering category with sets, prove that truncating the interval does not change the functor, and check that the passage from a continuous representative to its germ preserves the stated construction. The arrow in (69) from sets toward interval covers is part of the source and should be retained in such an account.

7. **Scan 251, (65) — own idea; confidence: high.** A useful check would compare `X = R², U = R² \ {0}` with `X = S², U = S² \ {x}`: the same cyclic local group should map very differently into the two global groups. This tests the important distinction between a canonical outer homomorphism and an asserted embedded peripheral subgroup; these pages assert the former and do not establish injectivity. The reason for high confidence is that the proposed examples reduce to elementary contractions of the corresponding punctured surfaces.

8. **Scan 252, marginal proposal and conditions (68) — own idea; confidence: medium.** Before replacing parameterized germs by subset germs, I would test continuous arcs with self-intersections or repeated excursions accumulating at the initial point, and compare them with embedded regular arcs. The displayed conditions require departure from `x` but do not visibly impose injectivity, so the image germ may omit order or multiplicity information carried by a parameterization. This is a proposed obstruction to investigate, not a claim that the constructions fail or that Grothendieck intended to include all such examples.

### Scan 253

- **Scan 253, equations (70)–(72) — unproved claim.** The words “on aura une factorisation” and “un iso can.” assert that an outgoing interval germ factors through its associated universal cover and that the two resulting based universal-cover constructions agree canonically. A proof would have to specify the category of germs and verify the universal properties, including independence from shortening the interval.
- **Scan 253, final paragraph — unpursued implication.** The definition beginning “un germe de courbe … est différentiable” introduces differentiability of the germ rather than a globally fixed representative. A check of invariance under changing representatives is needed before the construction can be used as a categorical source; the subsequent page supplies an additional tangency condition.

### Scan 254

- **Scan 254, equation (73) and following paragraph — unpursued implication.** The condition that the tangent map “est injective” assigns a nonzero tangent ray to the differentiable outgoing arc germ. The text does not here discuss invariance under orientation-preserving reparametrisation, which would be necessary if one later treats such germs as unparametrised arcs.
- **Scan 254, equations (74)–(75) — unproved claim.** After defining morphisms by isomorphisms of associated universal covers, the manuscript says “On trouve donc … une équivalence de … groupoïdes connexes.” Full faithfulness is built into (74), but essential surjectivity still requires every relevant universal cover to be represented by an outgoing arc germ, together with the local hypotheses guaranteeing connectedness.
- **Scan 254, equation (74) — own idea (confidence: medium).** Check separately the role of parametrisation by comparing two germs with identical images but different rates of approach to x. The definition through universal covers may identify more objects than a geometric equivalence of parametrised germs would; this is a proposed diagnostic, not an established defect or a novelty claim.

### Scan 255

- **Scan 255, equations (77)–(79) — unproved claim.** “Je vais définir une équivalence de catégories” promises a functor from differentiable arc germs to the fundamental groupoid of tangent directions, whose object map assigns the “demi-tangente.” Beyond the stated object map, a proof requires canonical compatible bijections on morphisms and the essential surjectivity of the tangent-ray assignment.
- **Scan 255, final paragraph — unpursued implication.** The required “bijection canonique” between arc-germ morphisms and tangent-direction morphisms makes the passage from a surface germ to its tangent circle stronger than an abstract isomorphism of local fundamental groups. Its dependence on the differentiable structure, and the precise naturality required under differentiable maps, remain to be specified on this page.
- **Scan 255, equation (79) — own idea (confidence: medium).** Test the claimed functor against curves sharing the same nonzero tangent ray but approaching it with different higher-order terms. The object map makes them identical in the tangent groupoid, so the construction should provide a coherent comparison of their universal-cover objects; this is a useful check of canonicity, not a claim of a new result.

### Scan 256

- **Scan 256, equations (80)–(81) — unproved claim.** “Je vais définir plutôt un foncteur” replaces a proposed family of morphism bijections by a functor from the direction-circle groupoid to universal covers of the punctured germ. The parenthesis “qui sera une équivalence de catégories” still requires functoriality, full faithfulness and essential surjectivity; defining the displayed object correspondence alone would not establish them.
- **Scan 256, equation (82) and final paragraph — unproved claim.** The assertion “on sait que le groupoïde enveloppant … est canoniquement équivalent” to the circle’s fundamental groupoid depends on localising the inclusion category of closed simply connected arcs. A proof can be sought by subdivision of paths and comparison of subdivisions, with special attention to degenerate arcs and exclusion of the whole circle, both written into (82).
- **Scan 256, equation (82) — own idea (confidence: medium).** Compare the localisation of the closed-arc poset with that of a small collection of overlapping arcs that still covers the circle. This could provide a concrete test of which relations recover the fundamental loop; the proposal is motivated by the explicit inclusion-category presentation and is not a claim that the reduction has already been proved.

### Scan 257

- **Scan 257, equations (83)–(84) — unproved claim.** The “équivalence canonique” is now described on point objects and on the zigzag a → A ← b. Establishing it requires showing that these arc zigzags generate all morphisms and that their relations match homotopy classes of paths, including the circle’s nontrivial winding relation.
- **Scan 257, final paragraph and equation (85) — unpursued implication.** “La donnée d’un foncteur … équivaut à la donnée d’un foncteur” starts a universal-property reformulation, whose target is supplied on the next page. The text as shown leaves open whether the equivalence is meant as a bijection of functor data, an equivalence of functor categories, or an equivalence up to specified natural isomorphism.
- **Scan 257, equation (84) — own idea (confidence: medium).** Track a concatenated sequence of small arcs that winds once around the circle and verify its image under the proposed functor. This tests whether the localisation sends the elementary zigzags to the expected fundamental-group generator and whether changing the subdivision introduces unwanted relations; it follows directly from the displayed description but is not carried out here.

### Scans 258–262

These notes are separate from the transcription. They identify tasks suggested by the local excerpt and do not certify novelty or claim that a proof is absent from the rest of the manuscript. No explicit conjecture or question has been securely identified in these five scans. References below are to the supplied scan numbers and the author’s equation numbers.

#### 1. Scan 258, after (86), condition involving (86bis)

**Kind:** unproved claim.

The criterion that (85) be an equivalence is stated in terms of connectedness, a fundamental group isomorphic to Z, and the image of the two-arc circuit being a ‘générateur’. A proof needs to show that this circuit generates the source vertex group and that sending it to a generator gives full faithfulness; the excerpt does not supply those checks here.

#### 2. Scan 258, (87)–(88)

**Kind:** unproved claim.

‘il suffit de définir un foncteur’ into 1-connected germs over D_x^* asserts a passage from such germs to universal covers. A proof must state the relevant category of germs and show that its universal-cover assignment is functorial with the required equivalence criterion.

#### 3. Scan 259, after (89)

**Kind:** unproved claim.

The revised text proposes a ‘filtre sur X-x tendant vers x’ in place of a germ of a subspace. The construction needs a precise germ-of-filter equivalence relation and a proof that the associated 1-connected germ is independent of representatives.

#### 4. Scan 259, cone paragraph and (90)

**Kind:** unproved claim.

The assertion that the elements of A_x ‘s'identifient évidemment’ with the specified closed cones is not proved here. Its verification must handle singleton arcs, excluded zero and whole-space cones, and the relation between arc inclusion and cone inclusion.

#### 5. Scan 259, last paragraph, strict containing cones

**Kind:** unpursued implication.

Replacing a single chart-image of a cone by a filter of strictly containing cones is designed to remove chart dependence, which the text explicitly notes as ‘dépend du choix de l'iso. local’. A systematic comparison with neighbourhood filters on the circle of directions would clarify which parts depend only on first-order data; the independence claim continues on the following scan.

#### 6. Scan 260, upper paragraph, image-filter construction

**Kind:** unproved claim.

The filter is said to be one ‘qui ne dépend pas du choix de f’. Proving this needs a uniform comparison of a chart change tangent to the identity with strictly enlarged cones near the origin; pointwise convergence of directions alone does not state the needed filter inclusion.

#### 7. Scan 260, middle paragraph, contractibility

**Kind:** unproved claim.

The text takes V ‘convexes fermés’ and the intersections V∩(C'−{0}) as ‘contractibles’, then concludes that the germ is 1-connected. A proof must verify the contractibility for all admitted directional arcs and justify the passage from this neighbourhood basis to covering theory of the germ.

#### 8. Scan 260, last paragraph, (88), (87), (81)

**Kind:** unproved claim.

‘on vérifie que ce dernier est bien une équivalence’ refers back to the two-arc criterion ((86bis)) without carrying out the verification on this page. The missing check is that the constructed local covers send the circuit to a generator of the relevant automorphism group.

#### 9. Scan 260, middle contractibility argument

**Kind:** own idea.

A direct polar-coordinate proof could contract an admitted sector intersection by moving its direction inside the proper arc and adjusting its positive radius inside a convex neighbourhood. Confidence: medium, because the surrounding argument is two-dimensional and the arcs are proper, but the exact class of allowed closed neighbourhoods and the treatment of endpoints must be checked; this is a proposed verification, not a claim of novelty.

#### 10. Scan 261, (91)

**Kind:** unproved claim.

The ‘morphismes d'inclusion canoniques’ from the differentiable arc germ to the germ attached to its half-tangent are asserted directly. Their construction needs the first-order control of the arc and the strict-cone filter used on the preceding pages; it is not a literal inclusion of the curved arc into a straight ray.

#### 11. Scan 261, (92) and the following Isom diagram

**Kind:** unpursued implication.

For two differentiable arcs with the same half-tangent, both displayed covers are compared with the same object Θ(Δ). This suggests a canonical comparison between their corresponding fibre functors, but the naturality and compatibility of that comparison must be checked rather than inferred from the equality of the direction alone.

#### 12. Scan 261, end of page, essentially commutative diagram

**Kind:** own idea.

One could formulate the naturality requirement as a specified natural isomorphism between the two routes around (93), rather than merely the existence of equivalent categories. Confidence: high as a bookkeeping proposal, since the text explicitly says ‘ess. comm.’ and the displayed cover comparisons supply candidate components; the coherence conditions still require verification.

#### 13. Scan 262, left marginal note beside (93)

**Kind:** unpursued implication.

The note identifies the earlier difficulty as the lack of a ‘morphisme direct entre le germe D_x^*, et l'espace S_x’. This distinguishes the equivalence of covering groupoids from an explicitly given map of the underlying germ to the circle; a direct realization would require an additional construction and its invariance properties.

#### 14. Scan 262, (94) and its following line

**Kind:** unproved claim.

The equivalence is ‘défini comme composé de Θ^{-1} avec le foncteur can.’. Interpreting the inverse as a quasi-inverse of an equivalence requires recording its dependence on choices, or the canonical natural-isomorphism class of the resulting functor; that coherence is not detailed in this paragraph.

#### 15. Scan 262, final paragraph around repeated (90)

**Kind:** unpursued implication.

The passage says the construction can be made explicit as ‘une construction canonique dans un espace vectoriel V’. Comparing that explicit local model across changes of coordinates with the same differential is a concrete way to test the earlier assertion that the strict-cone filter is independent of the chosen local isomorphism; the paragraph begins that model but continues beyond this page.

### Scan 263

- **Scan 263, lines 5–10; unproved claim.** “Il faut voir comment … dépend ‘continûment’ de Δ” is followed by “tout à fait standard”. A proof would need to specify the parameter space of rays, the category in which the universal coverings vary, and the precise meaning of continuity; the adjective does not itself provide these definitions.
- **Scan 263, lines 11–end; unpursued implication.** An automorphism fixing x and differentiable there induces automorphisms of the punctured germ and of the circle of tangent rays. The following comparison must track both actions on lift torsors, rather than merely compare abstract fundamental groups.
- **Scan 263, first paragraph; own idea; medium confidence.** A useful model to test is a real oriented two-dimensional vector space with the covering of its nonzero vectors parameterized by a real angular coordinate. This may make the dependence on Δ explicit, but an angular coordinate requires an auxiliary choice, so it would not alone establish the claimed invariant construction.

### Scan 264

- **Scan 264, (96) and adjacent upper-left margin; unproved claim.** The “bijection canonique” between the two sets of lifts is asserted to be an isomorphism of orientation-module torsors. The marginal note says the construction “sera faite dans les pages qui suivent” and points to (122), p. 783; those later pages are outside the present attachment range.
- **Scan 264, paragraph before 1); question / expectation.** “J'ai envie de donner une description axiomatique de (94) et (96)” announces an intended axiomatization. The following pages should be read as specifying the data and compatibility conditions of this comparison, not as a completed proof of every assertion in (96).
- **Scan 264, 1), cone and arc definitions; unpursued implication.** The correspondence between arcs of the tangent circle and proper closed cones permits a local construction indexed by an ordered family of subsets. A rigorous treatment must specify exactly which degenerate arcs are included and how the germ associated with a cone is defined independently of a chart.
- **Scan 264, (96); own idea; medium confidence.** Test the asserted torsor isomorphism separately on a linear orientation-preserving map and a reflection. The reflection is especially useful because its action changes the sign on the orientation module, so it can expose a hidden equivariance convention that a positive rotation would not reveal.

### Scan 265

- **Scan 265, (97)–(98); unproved claim.** The two sets of sections are said to be “l'un et l'autre Torseurs” over the same orientation module, and H(A) is said to be a torsor as well. This requires nonemptiness of the section sets and simple transitivity of the stated actions, including at singleton arcs and for the germ Ep(A).
- **Scan 265, (99)–(101); unproved claim.** Restriction along A⊂A′ is asserted to give “des isom. de … torseurs”, hence a canonical map H(A)→H(A′). A proof should establish that the restriction maps are bijections and verify the identity and composition laws, with the variance in (99) distinguished from that in (100).
- **Scan 265, (102); unpursued implication.** Because the target is a groupoid, a functor from the ordered category extends through its groupoid completion. The diagram isolates a useful universal-property step, but the subsequent claim that the resulting torsor-valued functor has trivial transport requires additional geometric input on the next page.
- **Scan 265, (98)–(102); own idea; medium confidence.** H can be viewed as a system of comparison torsors for two systems of local sections. This suggests checking whether its monodromy is the difference of the two section monodromies, but the signs and left/right action conventions must be fixed before this becomes a proof.

### Scan 266

- **Scan 266, opening and (103)–(105) — unproved claim.** « On sait que » introduces the assertion that the enveloping groupoid is a T_x-groupoid and that the functor to universal coverings is an equivalence. A full verification would identify its objects and all morphism torsors, including how the diagonal marginal reformulation of (105) compares with the overwritten main formula.
- **Scan 266, middle paragraph — unproved claim.** « je dis que le foncteur … est essentiellement constant » is followed by the explicit zero homomorphism on fundamental groups. The argument on this page does not prove that zero-monodromy assertion; a proof must compute the transport of the comparison torsor around a generator, rather than infer constancy merely from the existence of isomorphisms between its values.
- **Scan 266, final paragraph and (106) — unpursued implication.** The stated « système transitif d'isomorphismes » is used to define a common value H of the two chosen universal coverings. The compatibility required of the maps i_A is therefore part of the construction's content; the sentence stating that compatibility continues beyond the supplied excerpt.
- **Scan 266, essential constancy — own idea.** Compare the monodromy of the two section torsors around a pair of complementary arcs in the direction circle, then compute the induced monodromy on their Isom torsor. Confidence: medium; cancellation is suggested by the common orientation module, but the sign conventions and the actual naturality of the identifications must be checked before this gives a proof.

## 6. Inventory and source validation

The CSV has 339 inventoried elements over all 19 scans, each marked `yes`, using the requested seven element kinds. The inventory records text blocks, displays, diagrams, drawings, marginal notes, insertions, and deletions separately, and follows each page from top to bottom. Its identifiers are local editorial identifiers, not additional manuscript numbering.

The combined fragment was checked for scan order, visible folio order, balanced TeX groups and environments, math delimiters, allowed editorial commands, and agreement with the inventory page coverage. Two TikZ-CD cells received syntactic grouping so that a leading bracket is not parsed as an environment option and a nested array is kept within its cell; neither change alters visible manuscript content. A full TeX compilation could not be performed because the available installation lacks the LaTeX format and package files. The ZIP contains exactly the three requested files.

## Reference

Grothendieck, A. (1981). *La Longue Marche à travers la théorie de Galois* [Handwritten manuscript, cote 140-4; archive file covering pp. 650bis–787, supplied scans 248–266]. Université de Montpellier.

The bibliographic identification is supplied by the task brief; the page readings and research observations are based on the attached images.

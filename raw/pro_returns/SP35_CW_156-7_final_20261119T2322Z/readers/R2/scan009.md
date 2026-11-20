# R2 — scan009 / manuscript page8

Independent reading: 2026-11-19 22:54:12 UTC – 2026-11-19 23:09:21 UTC.

**86 rows; 28 differences from C; 85 from H. All 34 C doubts audited; 23 crops.**

## Principal findings

- The upper abandoned draft and its slanted NB are marked cancelled. The note’s own smaller erased words are preserved separately.
- Cancelled Cor1 literally has **F≪F** and **C′≪G**. The initial second figure is **C**; its later disjointness operand remains **C|G**. No mathematical correction is inserted.
- The upper NB resolves **immédiat**, parenthetic **d’où**, and crossed **absurde**. The common-refinement line gains explicit low-confidence prime alternatives.
- AtDC2 has literal **tt**, a local underline through the middle hypotheses, and a separate shallow enclosing contour. The apparent point on the underline is the written comma crossing it.
- The live title is **Propriété1** after **On voudra la**. The reference and On a assertion are live; the next proof-start line is cancelled.
- The reference resolves **cf**, cancelled **p.**, and underlined **73**. Its final sign is two shafts and a separate curved right cap, without a pointed head.
- The diagram is fully drawn: slightly open diamond and oval, full diagonal, two filled points, small inner x-cross and two larger outer X-crosses. No additional semantic labels are invented.
- The lower note has a literal **two-upright/two-crossbar sign**, not an overline above parallel. **C’est un**, the colon before **At∥**, and crossed **ex** resolve. The example-word abbreviation and small first-variable case remain doubtful.
- The live label reads **At DD1**, and the oblique word reads **ancien**. Its attachment remains uncertain. The written **K** followed by **L** indices is retained.
- The last labels are **Corollaire1** and **Corollaire2**, without Main. Corollaire1 refers to the property; Corollaire2 labels the disjoint-refinement implication. The next line begins **Plus gén.**.

## Remaining uncertainties

- M alphabet: `\unsure{M|\mathcal M}` (medium).
- old first relation: `\deleted{\unsure{\parallel}}` (low).
- old first statement end mark: `\unsure{\text{\S}|?|.}` (low).
- old beginning before Soient: `\deleted{\unsure{Alors}}` (low).
- upper margin old impossible: `\deleted{\unsure{impossible}}` (low).
- upper margin common-refinement line: `Z\ll\unsure{X′|X},\ \unsure{Z′|Z}\ll Y` (low).
- figure-family alphabet: `\unsure{\mathscr F|\mathcal F}` (medium).
- Cor1 disjointness second operand: `\unsure{C|G}` (low).
- Cor2 old equation initial: `\unsure{L}` (low).
- AtDC2 old word: `\unsure{Soit|Soient}` (low).
- AtDC2 old letter: `\deleted{\unsure{L}}` (low).
- cancelled proof-start verb: `\unsure{Montrons}` (low).
- cancelled proof-start short group: `\unsure{en}` (low).
- lower note first variable case: `\unsure{x′|X′}, twice` (low).
- lower note example word: `\unsure{contre-exple|contre-exemple|contre exemple}` (low).
- live axiom separator: `\unsure{o|,}` (low).
- live NB noun: `\unsure{l’énoncé|l’inverse}` (low).
- live NB old word: `\deleted{\unsure{est}}` (low).
- ancien attachment: `ancien above/right of Soient; intended attachment uncertain` (low).

## Mathematics and limits

**summary, not proof check**. The page abandons two disjointness/compatibility drafts and their corollaries, then proposes a locality criterion for compatibility under refinement. A marginal note explicitly says the criterion is false in the simplicial case and gives a drawing. The final named axiom and corollaries reuse the restriction indices L after introducing K.

**targeted proof check** (R2-009-M1). The final contradiction in the upper NB is valid under the stated local assumptions that Z is a nonempty stratum, Z≪L and Z is disjoint from L. Disjointness gives compatibility and Z∩L=empty. By At4, applied to the stratum Z itself, Z≪L yields a stratum U≤L with Z≪U. Compatibility of Z with L descends to U, so At5 for compatible strata gives Z≤U≤L. Hence Z∩L=Z, contradicting that a stratum is nonempty. This checks the final contradiction only; it does not prove the preceding Z≪X,Y⇒Z≪X∩Y step or resolve the possible primes.

**conditional targeted proof check** (R2-009-M2). The globally compatible ⇒ locally compatible direction follows if the subscript-L objects are subfigures of their parents. Indeed, if A≤F′ and B≤G′ and H is a common upper figure for compatible F′ and G′, then H is also an upper figure for A and B. This proves hereditary compatibility for those subfigures. A definition of F′_L is not established on this page, so the check is explicitly conditional on that subfigure property and does not prove the displayed equivalence or the final axiom.

**targeted counterexample to literal cancelled formula** (R2-009-M3). The literal cancelled Cor1 formula, with F≪F and C′≪G but conclusion F′∥G′, cannot be a universal theorem as written. In the two-element Boolean figure poset {empty,{a}}, take refinement=inclusion and all figures compatible. Set F=C=G=C′=empty and F′=G′={a}. The disjointness premise and the two written refinement premises hold, while F′∩G′={a}, so the conclusion fails. This diagnoses the missing/mismatched primed operands in an abandoned draft; no correction is inserted into its text.

**unverified author claim**. The simplicial counterexample is transcribed and drawn, but the restriction notation and identities of the parts of the drawing are insufficiently specified within the pages read to certify it independently. No external GFVI pages cited by H were consulted. The final hash-like relation is a contour reading, not an independently proved negation interpretation.

**literal mismatches retained**. The cancelled F≪F and C′≪G, the initial C and later C/G uncertainty, and live K with subsequent L indices are preserved. The oblique ancien is readable but its verbal attachment remains uncertain. No missing conclusion is supplied after the abandoned Alors.

## Full collation

| ID | Place | C | H | R2 | Evidence / confidence |
|---|---|---|---|---|---|
| R2-009-01 | opening final words | d’autres | \ill{} | d’autres | A d, apostrophe and the connected autres group end the opening paragraph; no next word is supplied. [high] From supplied half. |
| R2-009-02 | whole upper At DC1 / Cor1 / Cor2 draft | all cancelled | only first line cancelled, later clauses and corollaries live; prose note says crossed | all cancelled, with local earlier changes separately represented | Long oblique strokes run through the whole upper draft. The local horizontal deletions do not exhaust that global cancellation. [high] From supplied half. |
| R2-009-03 | old At DC1 label underline | At underlined | plain At DC1 | At alone underlined | A short baseline rule sits directly beneath At and ends before DC. [high] From supplied half. |
| R2-009-04 | first and recurring M alphabet | \unsure{M\|\mathcal M} | \mathcal M | \unsure{M\|\mathcal M} | Two tall stems and a bowed joining trough survive the horizontal cancellation. They do not settle a named font; the uncertainty itself is preserved. [medium] Crop: readers/R2/crops/scan009_M.png |
| R2-009-05 | old relation inside first compatibility sign | \deleted{\unsure{\parallel}} | no old sign | \deleted{\unsure{\parallel}} | Two near-upright strokes survive inside the crossed angular replacement. They plausibly form old parallel bars, but the overlapping paths prevent certainty. [low] Crop: readers/R2/crops/scan009_oldsign.png |
| R2-009-06 | mark after first old Y | \unsure{\text{\S}\|?\|.} | omitted | \unsure{\text{\S}\|?\|.} | Two small stacked bent loops are cut at their waist by the horizontal cancellation; a section-like mark is preferred, but the original remains unclear. [low] Crop: readers/R2/crops/scan009_oldsign.png |
| R2-009-07 | old beginning before added Soient | \deleted{\unsure{Alors}} | \struck{At} | \deleted{\unsure{Alors}} | A tall A and following upright l are visible above a dense horizontal strike; the following low letters are largely covered. The group is longer than the two-letter At. [low] Crop: readers/R2/crops/scan009_oldAlors.png |
| R2-009-08 | Soient above the old beginning | inserted Soient | Soient presented on main baseline | inserted Soient | The small Soient sits above the local horizontal cancellation. [high] Crop: readers/R2/crops/scan009_oldAlors.png |
| R2-009-09 | avec X′ parallel X cap Y insertion anchor | after X′≪X, inside cancelled statement | detached after the first statement line | raised clause attached after X′≪X, within the globally cancelled draft | The added avec begins above the cancelled Y′≪Y segment and the following formula continues along that same raised writing level. [high] From supplied half. |
| R2-009-10 | intersection name in added clause | \unsure{L\|\mathcal L} | L | L | A plain rising stem turns into one horizontal foot; there is no extra loop or upper flourish. [medium] Crop: readers/R2/crops/scan009_L.png |
| R2-009-11 | i.e. gloss in the raised insertion | (i.e. X′∥Z pour Z≤X,Y) | i.e. gloss without parentheses | parenthesized i.e. gloss | Opening and closing curves enclose the gloss independently of the added formula. [high] From supplied half. |
| R2-009-12 | upper slanted NB cancellation state | live | live | cancelled with the abandoned upper draft | After rotation a long straight stroke crosses the La / importante / relation lines and continues into the upper draft below. R2 reads this as a global cancellation through the note, distinct from its two shorter erased words. [medium] Crop: readers/R2/crops/scan009_upperNB.png |
| R2-009-13 | upper marginal NB underline | underlined NB | plain NB | underlined NB | A separate short rule lies beneath the two heading letters. [high] Crop: readers/R2/crops/scan009_upperNB.png |
| R2-009-14 | upper margin opening | La chose importante est | Il [ill.] choisi [ill.] | La chose importante est | The rotated lines show La, chose, importante and est in sequence; the visible last word is not choisi. [high] Crop: readers/R2/crops/scan009_upperNB.png |
| R2-009-15 | upper margin after empty intersection | \unsure{immédiat} | \uncertain{immédiat} | immédiat | The initial i, double m run, accented middle, and final crossed t are readable upright; no final e is added. [medium] Crop: readers/R2/crops/scan009_upperNB.png |
| R2-009-16 | upper margin proof connector | Car | opening parenthesis / unread | Car | The word begins with a capital open C and ends with the joined ar strokes. [high] Crop: readers/R2/crops/scan009_upperNB.png |
| R2-009-17 | upper margin overwritten relation after first Z | Z\deleted{\ll}\leq X′ | Z≤X′ | Z\deleted{\ll}\leq X′ | An extra angular layer remains under the reinforced live less-or-equal sign. [medium] Crop: readers/R2/crops/scan009_upperNB.png |
| R2-009-18 | upper margin common-refinement line: small raised marks | Z≪X, Z≪Y | Z≪X, Z≪Y | Z\ll\unsure{X′\|X},\ \unsure{Z′\|Z}\ll Y | Small raised strokes beside the first X and second Z can be read as primes; they are close to the neighbouring line and comma. They are recorded as uncertain rather than discarded to regularize the inference. [low] Crop: readers/R2/crops/scan009_upperNB.png |
| R2-009-19 | upper margin first or | or | semicolon | or | A small rounded o and rising r follow L and the comma. [high] Crop: readers/R2/crops/scan009_upperNB.png |
| R2-009-20 | upper margin second or | or | et | or | The leftmost group before Z≪L has an o-like loop and short r, with no tall t. [medium] Crop: readers/R2/crops/scan009_upperNB.png |
| R2-009-21 | upper margin first erased word | \deleted{\unsure{impossible}} | \ill{} | \deleted{\unsure{impossible}} | A p-like descent and later tall strokes survive below the heavy horizontal line; impossible remains plausible but not fully separable. [low] Crop: readers/R2/crops/scan009_upperNB.png |
| R2-009-22 | upper margin parenthetic connective | \unsure{d’où\|comme} | \ill{} | d’où | After the opening curve, the first letter has a tall d stroke and a separate apostrophe-like mark; the remaining low group fits où rather than the longer comme. [medium] Crop: readers/R2/crops/scan009_upperNB.png |
| R2-009-23 | upper margin parenthetic compatibility | Z [compat] L | unread / omitted | Z [compat] L in parentheses | Z and L flank the angular compatibility mark inside a closing parenthesis. The macro used for the base compatibility sign is not itself counted as a difference. [high] Crop: readers/R2/crops/scan009_upperNB.png |
| R2-009-24 | upper margin final implication | ⇒ Z≤L | ⇒ Z overlined-parallel L = empty | ⇒ Z≤L | The implication is followed by Z, a less-or-equal angle and L; the intersection-equals-empty formula comes later on its own line. [high] Crop: readers/R2/crops/scan009_upperNB.png |
| R2-009-25 | upper margin second erased word | \deleted{\unsure{absurde}} | \ill{} | \deleted{absurde} | The initial a loop, tall b, joined sur and final de strokes remain visible under a local horizontal strike. [medium] Crop: readers/R2/crops/scan009_upperNB.png |
| R2-009-26 | upper margin before final contradiction | car | omitted | car | A small c/a/r group follows the crossed absurde. [medium] Crop: readers/R2/crops/scan009_upperNB.png |
| R2-009-27 | upper margin final underlined formula | Z∩L=∅ !, underlined | Z overlined-parallel L=∅ ! | Z∩L=∅ !, underlined | The thick middle mark has an arched upper join and two descending sides. A separate long rule underlines the full final equation and exclamation mark. [high] Crop: readers/R2/crops/scan009_upperNB.png |
| R2-009-28 | cancelled Cor1 second initial figure | \unsure{C\|G} | G | C | The capital is an open C with a long lower arm and no inward crossbar or return. The nearby later G has a distinctly developed inward lower return. [medium] Crop: readers/R2/crops/scan009_cor1_initial.png |
| R2-009-29 | Cor1 and recurring figure-family alphabet | \unsure{\mathscr F\|\mathcal F} | \mathfrak F | \unsure{\mathscr F\|\mathcal F} | A looped/curving main stem and separate crossing arm recur. The handwriting is cursive, while exact mathscr versus mathcal representation remains uncertain. [medium] Crop: readers/R2/crops/scan009_cor1_initial.png |
| R2-009-30 | cancelled Cor1 disjointness premise | F∥G | F∥G | F\parallel\unsure{C\|G} | The right letter is a C-shaped outline with a tiny detached lower-right dash. That dash may supply an incomplete G return, but it is not decisive. [low] Crop: readers/R2/crops/scan009_cor1_right.png |
| R2-009-31 | cancelled Cor1 first refinement premise | F≪F | F′≪F | F≪F | There is no detached prime after the first F; the following strokes belong to the double-angle relation. [high] Crop: readers/R2/crops/scan009_cor1_right.png |
| R2-009-32 | cancelled Cor1 second refinement premise | C′≪G | G′≪G | C′≪G | The primed first letter is an open C; the following unprimed G has a returning lower stroke. [high] Crop: readers/R2/crops/scan009_cor1_second.png |
| R2-009-33 | cancelled Cor1 final punctuation | period | period | no terminal period | After the final primed G the crop and supplied half show no separate baseline point. [medium] Crop: readers/R2/crops/scan009_cor1_second.png |
| R2-009-34 | cancelled Cor2 old equation initial | \deleted{\unsure{L}=Sup…} | \struck{\ill{}} | \deleted{\unsure{L}=Sup_{Z∈Ftilde∩Gtilde} Z} | The leading group is almost buried by zigzag cancellation; L remains uncertain. The Sup trace, lower Z/membership and two deployed-set indices survive in parts below the heavy line. The replacement L=F∩G is clearly above. [low] Crop: readers/R2/crops/scan009_cor2_old.png |
| R2-009-35 | At DC2 title adjective | spacieux | spécieux | spacieux | The title has a rounded a after sp and no acute accent. [high] From supplied half. |
| R2-009-36 | At DC2 old word at end of title | \deleted{\unsure{Soit\|Soient}} | live Soient | \deleted{\unsure{Soit\|Soient}} | So and a tall crossed terminal-like stem survive, but the long cancellation return obscures whether further low letters belonged to the original word. [low] Crop: readers/R2/crops/scan009_DC2_Soit.png |
| R2-009-37 | At DC2 old letter behind K | \deleted{\unsure{L}}K | K | \deleted{\unsure{L}}K | An extra short horizontal arm and lower stem curl remain with the K arms. An earlier L is possible but not independently secure. [low] Crop: readers/R2/crops/scan009_DC2_K.png |
| R2-009-38 | At DC2 after pour | \unsure{tt} | tous | tt | Two tall strokes share a crossbar and each has a curled lower exit. They spell the two-letter abbreviation tt, without ous. [high] Crop: readers/R2/crops/scan009_tt.png |
| R2-009-39 | At DC2 underline beneath middle hypotheses | underline Y′≪Y, X′∥K | no underline | underline Y′≪Y, X′∥K | A continuous low rule begins below Y′ and ends beneath K. The apparent central pointed bend is the written comma crossing that rule, not an additional implication sign. [high] Crop: readers/R2/crops/scan009_DC2_rule.png |
| R2-009-40 | At DC2 enclosing lower contour | not drawn | described as encadré | shallow lower contour with rising ends, drawn | The entire unfinished draft has a long low border below its last line and rising oblique/curved ends. It is distinct from the long cancellation strokes. [high] From supplied half. |
| R2-009-41 | introduction to live property | On voudra la | On voudrait la | On voudra la | The word ends in the low a stroke, with no terminal t. [high] From supplied half. |
| R2-009-42 | live property title | Propriété 1 | Proposition 1 | Propriété 1, underlined | The title contains the short été ending after propri; it is not the longer position sequence. The underline runs through the numeral. [high] From supplied half. |
| R2-009-43 | reference and On a line state | live | whole reference and assertion struck | reference and On a assertion live; only next proof-start line cancelled | The long strike follows the lower proof-start baseline. It passes below the reference letters and does not cross the upper assertion text. [high] Crop: readers/R2/crops/scan009_citation.png |
| R2-009-44 | reference initial abbreviation | \unsure{cf\|Cf} | cf. | cf | The first c is distinctly lower than the adjacent GF capitals; the f descends. There is no dot after the abbreviation. [medium] Crop: readers/R2/crops/scan009_citation.png |
| R2-009-45 | reference small cancelled token | \deleted{\unsure{p.}} | omitted | \deleted{p.} | A descender, crossed loop and separate small dot can be followed between cf and GF. [medium] Crop: readers/R2/crops/scan009_citation.png |
| R2-009-46 | reference roman numeral decoration | VI with upper and lower rule | plain VI | VI with upper and lower rule | One line lies above VI and another below it. [high] Crop: readers/R2/crops/scan009_citation.png |
| R2-009-47 | reference page number | \uline{\unsure{73\|13}} | 73, not underlined | underlined 73 | The first digit has an angled top return before its descending stroke; the second has two curved lobes. A separate line underlines both digits. [medium] Crop: readers/R2/crops/scan009_citation.png |
| R2-009-48 | On a assertion abbreviation | tjrs | omitted | tjrs | The tall t and descending j with short rs continuation occur before the final relation-shaped mark. [high] From supplied half. |
| R2-009-49 | On a assertion terminal mark | uncertain rounded-return drawing or Rightarrow | Longrightarrow | two shafts plus a separate rounded right return, drawn literally | Two horizontal shafts end before a separate larger curved cap. The cap descends and returns left at the bottom; it does not form a pointed arrowhead. [high] Crop: readers/R2/crops/scan009_assertedarrow.png |
| R2-009-50 | cancelled proof start first word | \unsure{Montrons} | omitted | \unsure{Montrons} | A large M and portions of the low n/t/r/o/n/s run survive, but the upper strike and marginal writing overlap the word. [low] Crop: readers/R2/crops/scan009_crossedline.png |
| R2-009-51 | cancelled proof start middle prose | qu’on a bien | omitted | qu’on a bien | The descending q and later a/bien groups can be followed along the struck baseline. [medium] Crop: readers/R2/crops/scan009_crossedline.png |
| R2-009-52 | cancelled proof start before arrow | \unsure{en} | omitted | \unsure{en} | Two short low joined strokes are partly effaced by the long cancellation; en remains tentative. [low] Crop: readers/R2/crops/scan009_crossedline.png |
| R2-009-53 | Ceci est équivalent parenthetical qualification | (si on le voit de façon générale) | unread groups plus incomplete parentheses | (si on le voit de façon générale) | The whole parenthetical is readable across the lower line, including the tall f and cedilla-bearing façon. No extra editorial words are supplied. [high] From supplied half. |
| R2-009-54 | H supposed independent additions after cancelled proof start | no such extra added prose | add ill ill | no extra independent prose addition | The slanted writing intersecting the proof-start area belongs to the long marginal criterion note, not to an additional standalone body phrase. [medium] From supplied half. |
| R2-009-55 | lower margin criterion wording | Critère de compatibilité pour les raffinements de sous-figures | Critère de compatibilité followed by unread struck/added fragments | Critère de compatibilité pour les raffinements de sous-figures | Rotation separates the words pour les raffinements de sous-figures from the body text crossing them. [high] Crop: readers/R2/crops/scan009_criterion.png |
| R2-009-56 | lower criterion underlines | Critère, compatibilité, sous-figures underlined | no comparable complete underline spans | Critère, compatibilité, sous-figures underlined | Each of those three groups has its own long baseline rule. The low rule overlaps the following Mais at an oblique angle; it is not taken as a separate deletion of Mais. [high] Crop: readers/R2/crops/scan009_criterion.png |
| R2-009-57 | thin vertical line beside live axiom | line embedded with criterion margin note | described as a border beside At CD1 | thin vertical border beside the live At DD1 block | The straight line stands just left of the live axiom/Posons/implique lines, separate from the slanted criterion. The fragment places it with that block. [high] Crop: readers/R2/crops/scan009_criterion.png |
| R2-009-58 | simplicial example drawing | TikZ drawing | description only | complete diamond, open oval, diameter, two filled vertices and three cross marks drawn | The rotated crop shows a slightly open lower diamond corner, a nearly closed inner oval with a lower-right gap, a top-to-bottom diagonal through two filled oval intersections, one small inner cross and two larger outer crosses. [high] Crop: readers/R2/crops/scan009_diagram.png |
| R2-009-59 | drawing inner small cross | \unsure{x\|+} | small internal mark | x-shaped crossing | Once rotated to the writing direction, both short strokes are diagonal; their crossing is x-shaped rather than horizontal/vertical. [high] Crop: readers/R2/crops/scan009_diagram.png |
| R2-009-60 | drawing external lower-left cross | \unsure{X\|x} | a cross below the unrotated figure | larger X-shaped cross | Two long diagonal strokes cross, substantially larger than the internal mark. [medium] Crop: readers/R2/crops/scan009_diagram.png |
| R2-009-61 | drawing external lower-right cross | \unsure{X\|Y} | a cross to the right of the unrotated figure | reinforced X-shaped cross | Four diagonal arms can be followed; the lower-left diagonal is reinforced. The thin lower-right arm remains, so the mark is not reduced to a three-armed Y. [medium] Crop: readers/R2/crops/scan009_diagram.png |
| R2-009-62 | lower margin first variable case in premise and consequent | X′ in both places | X′ in both places | \unsure{x′\|X′} in both places | Both first crosses are noticeably small and low beside the tall Y′. The cramped slanted hand may account for the size, so lowercase x is preferred with uppercase retained. [low] Crop: readers/R2/crops/scan009_lowernote.png |
| R2-009-63 | lower margin consequent relation | drawn hash-like sign \| # \| notparallel \| parallel | overlined parallel | literal two uprights with two transverse bars, drawn | Two strong near-vertical strokes are crossed by two short oblique bars at distinct heights. This is not one bar drawn above parallel. Its logical interpretation is left open. [high] Crop: readers/R2/crops/scan009_lowernote.png |
| R2-009-64 | lower margin article after C’est | \unsure{C’est un\|C’est une} | c’est un | C’est un | The short group ends at n before the separate contre group. There is no extra e loop; the initial C is capital. [medium] Crop: readers/R2/crops/scan009_lowernote.png |
| R2-009-65 | lower margin example word | \unsure{contre-exemple\|contre-exple\|contre exemple} | contre-ex. | \unsure{contre-exple\|contre-exemple\|contre exemple} | The middle is crossed by writing in the main direction. A short exple-like sequence is preferred, but neither the full em group nor the exact hyphen/space can be certified. No abbreviation point is visible. [low] Crop: readers/R2/crops/scan009_lowernote.png |
| R2-009-66 | lower margin before At | \unsure{:} | omitted | : | Two separate small points occur vertically before the At group. [medium] Crop: readers/R2/crops/scan009_lowernote.png |
| R2-009-67 | lower margin first axiom name | At parallel | At 11 | At parallel | The first pair consists of two plain parallel bars. The later numeral 11 has distinctly numeral-like top/foot strokes. [high] Crop: readers/R2/crops/scan009_lowernote.png |
| R2-009-68 | lower margin strengthening phrase | et a fortiori à | et ill | et a fortiori à | The long f descender and connected ortiori run are legible across the oblique line. [high] Crop: readers/R2/crops/scan009_lowernote.png |
| R2-009-69 | lower margin locally erased group | \deleted{\unsure{ex}} | omitted | \deleted{ex} | A short e-like loop is followed by crossing x strokes beneath an additional local cancellation. [medium] Crop: readers/R2/crops/scan009_lowernote.png |
| R2-009-70 | lower marginal reference | (cf GF VI with rules, p.67,68) | reference partly supplied in editorial notes | (cf GF VI with upper/lower rules, p.67,68) as marginal text | The reference is physically part of the slanted note. Its letters, ruled VI, page numbers and closing parenthesis are present. [high] Crop: readers/R2/crops/scan009_lowernote.png |
| R2-009-71 | lower note punctuation after consequent | comma before C’est | opening parenthesis before c’est | line break with no added comma or parenthesis | After the primed Y the line has no detached comma; the next line starts with the large C itself, without a separate opening parenthesis. [medium] Crop: readers/R2/crops/scan009_lowernote.png |
| R2-009-72 | live axiom letters | \unsure{DD\|DC} | CD (with editorial old DD/DC alternatives) | DD | Both current letters have a stem and closed right bowl. The retracing does not reveal an independently readable older CD or DC layer. [medium] Crop: readers/R2/crops/scan009_heading.png |
| R2-009-73 | live axiom label underline extent | At DD underlined, 1 outside | At CD1 emphasized as one span | At DD underlined; 1 outside | The rule ends beneath the second D before the separated numeral. [high] Crop: readers/R2/crops/scan009_heading.png |
| R2-009-74 | oblique interlinear word | \unsure{ancien\|ou bien\|ou bien,} | ou uncertain ancien | ancien | The word has an initial rounded a/n run, then c and a dotted i followed by en. There is no tall b required by bien and no second word ou. [medium] Crop: readers/R2/crops/scan009_addedword.png |
| R2-009-75 | oblique ancien position | inserted after Soient | addition after X,Y | above/right of Soient; verbal attachment uncertain | The word rises obliquely above the right edge of Soient, between that line and the preceding ancien At12 line. No secure arrow fixes its intended grammatical attachment. [medium] Crop: readers/R2/crops/scan009_addedword.png |
| R2-009-76 | small separator between Y and X′ | \unsure{o\|,} | et | \unsure{o\|,} | A narrow closed oval with a downward extension is visible. It is unlike a full written et; the shorter comma alternative remains only a possibility. [low] Crop: readers/R2/crops/scan009_separator.png |
| R2-009-77 | live Posons meet operation | K=X cap Y | K=X wedge Y | K=X cap Y | The operation has a rounded arch with two descending sides, matching intersection; it has no pointed wedge apex. [high] From supplied half. |
| R2-009-78 | live axiom NB noun | \unsure{l’énoncé\|l’inverse} | l’inverse | \unsure{l’énoncé\|l’inverse} | The compressed run has possible accent-like marks above its beginning and ending. Those permit énoncé, while the lower joins can be read inverse. The apparent final points are not independently promoted to a colon. [low] Crop: readers/R2/crops/scan009_NBbottom.png |
| R2-009-79 | live axiom NB old word | \deleted{\unsure{est}} | \ill{} | \deleted{\unsure{est}} | An old tall/looped short group is crossed before the clean live est. Its individual e/s/t strokes cannot be securely separated. [low] Crop: readers/R2/crops/scan009_NBbottom.png |
| R2-009-80 | live axiom NB abbreviation | tjrs | toujours | tjrs | The tall t and long j descent are followed by only the short rs run. [high] Crop: readers/R2/crops/scan009_NBbottom.png |
| R2-009-81 | live axiom NB placement | after the implication/conclusion | before implique | aside beside the final implication/conclusion | The parenthetical occupies the right side of the final axiom lines, after the displayed compatibility condition rather than interrupting before implique. [high] Crop: readers/R2/crops/scan009_NBbottom.png |
| R2-009-82 | H inline reference after implique | no body reference here | (cf. GF VI) | no independent body reference | The slanted GF VI reference belongs to the adjacent counterexample note; it is not an added parenthesis in the axiom sentence. [high] Crop: readers/R2/crops/scan009_lowernote.png |
| R2-009-83 | first final corollary label | Corollaire 1 | Cor. Main 1 | Corollaire 1 | The full Corollaire is written and underlined, followed by numeral1; no Main word is present. [high] From supplied half. |
| R2-009-84 | first final corollary content | la ``propriété’’ ci dessus | (cf. la « propriété » ci-dessus) | la ``propriété’’ ci dessus | The line starts directly with la, has paired high quotation strokes, and separates ci and dessus with blank space. It contains neither cf nor outer parentheses nor a hyphen. [high] From supplied half. |
| R2-009-85 | second final corollary label and scope | Corollaire2 beside F∥G refinement implication | that implication placed under Cor.Main1; next Si given Cor.Main2 | Corollaire2 labels the F∥G refinement implication | The underlined Corollaire2 stands at the left of the same line as F∥G, F′≪F, G′≪G ⇒ F′∥G′. [high] From supplied half. |
| R2-009-86 | final generalization introduction | Plus gén. Si … | Si … under Cor.Main2; editorial uncertain pour que | Plus gén. Si … | The distinct P/l/u/s run is followed by gén. and the Si clause. It is not pour que, and the generalization is not assigned an additional numbered corollary. [high] From supplied half. |

## C doubt audit

| C reading | Place | Outcome | Row |
|---|---|---|---|
| M\|mathcal M | old At DC1 membership | retained | R2-009-04 |
| old parallel | old At DC1 sign | retained | R2-009-05 |
| section sign\|?\|. | old At DC1 after Y | retained | R2-009-06 |
| old Alors | before inserted Soient | retained | R2-009-07 |
| L\|mathcal L | inserted intersection name | resolved | R2-009-10 |
| immédiat | upper NB | resolved | R2-009-15 |
| deleted impossible | upper NB | retained | R2-009-21 |
| d’où\|comme | upper NB parenthesis | resolved | R2-009-22 |
| deleted absurde | upper NB | resolved | R2-009-25 |
| C\|G | Cor1 initial second figure | resolved | R2-009-28 |
| mathscr F\|mathcal F | Cor1 set alphabet | retained | R2-009-29 |
| old L | Cor2 Sup equation | retained | R2-009-34 |
| Soit\|Soient | At DC2 old word | retained | R2-009-36 |
| old L | At DC2 before K | retained | R2-009-37 |
| tt | At DC2 quantifier abbreviation | resolved | R2-009-38 |
| cf\|Cf | reference | resolved | R2-009-44 |
| deleted p. | reference | resolved | R2-009-45 |
| 73\|13 | reference number | resolved | R2-009-47 |
| rounded-return drawing\|Rightarrow | On a assertion | resolved | R2-009-49 |
| Montrons | cancelled proof start | retained | R2-009-50 |
| en | cancelled proof start | retained | R2-009-52 |
| x\|+ | drawing inner mark | resolved | R2-009-59 |
| X\|x | drawing outer left | resolved | R2-009-60 |
| X\|Y | drawing outer right | resolved | R2-009-61 |
| drawn sign\|#\|notparallel\|parallel | lower note consequent | resolved | R2-009-63 |
| C’est un\|C’est une | lower note | resolved | R2-009-64 |
| contre-exemple\|contre-exple\|contre exemple | lower note | changed | R2-009-65 |
| : | lower note before At | resolved | R2-009-66 |
| deleted ex | lower note before At11 | resolved | R2-009-69 |
| DD\|DC | live axiom label | resolved | R2-009-72 |
| ancien\|ou bien\|ou bien, | oblique insertion | resolved | R2-009-74 |
| o\|, | live variable list | retained | R2-009-76 |
| l’énoncé\|l’inverse | live NB | retained | R2-009-78 |
| deleted est | live NB | retained | R2-009-79 |

## Inspection and protocol record

Whole image once, then supplied a and b halves once, followed by 23 once-only unresolved-locus crops. Slanted notes, oblique insertion and example drawing were rotated within their single crops. All images were actually viewed with view_image. C scan009, H page8 stopping before page9, all C scan009 doubts and relevant C notes were read. No other/main009 report was opened. No OCR, external research or compilation was performed for scan009. The separate macro audit contains an explicit disclosure of three earlier prohibited synthetic diagnostic compiler attempts; no blanket no-compilation claim is made for the run.

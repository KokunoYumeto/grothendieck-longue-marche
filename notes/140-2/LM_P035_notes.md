# LM_P035 — Editorial apparatus and research notes

## 1. Scope, source, and conventions

This apparatus accompanies the diplomatic French LaTeX transcription of the ten supplied images `LM_P035_scan341.jpg`–`LM_P035_scan350.jpg`. The attribution, title, year, and shelfmark follow the supplied task brief. Readings are based on these images; no published transcription, later manuscript passage, or reconstructed mathematical argument has been used to fill missing ink.

The scan numbers follow the filenames. The visible handwritten numbers are also retained in position with `\mspage`; their different hands or numbering functions have not been independently established. The printed archive footer, its repeated page number, web address, and institutional address are not manuscript text and are omitted.

| Scan | Upper handwritten number | Lower handwritten number |
|---|---|---|
| 341 | — | 340 |
| 342 | 173 | 341 |
| 343 | — | 342 |
| 344 | 174 | 343 |
| 345 | — | 344 |
| 346 | 175 | 345 |
| 347 | — | 346 |
| 348 | 176 | 347 |
| 349 | — | 348 |
| 350 | 177 | 349 |

The transcription is a UTF-8 LaTeX fragment, without a preamble or macro definitions. Editorial interventions use only the macros specified in the brief. `\unsure{a|b}` exposes alternative readings; it does not claim that the alternatives are exhaustive. `\illegible{n}` counts estimated words or, within formulae, unreadable symbol groups. Recoverable cancellations remain inside `\deleted`, even when a replacement is also legible. In the heavily revised passages, an uncertainty may concern the state of a stroke (underline versus deletion) as well as its reading.

The ordinary serifed capital `I` is not given an extra overbar. The quotient-group glyph with doubled left stem is represented by `\Gamma`; the distinct capital `\Pi` is retained where its right stem is visible. The recurring swash group letters are represented by `\mathcal G` and `\mathcal T`, normalizers by `\mathcal N`, and the related full-group symbol by `\mathcal M`; these are typographical approximations of the hand, with ambiguous individual occurrences marked. The ornate symmetric-group symbol is represented by `\mathfrak S`, with its alphabetic appearance noted as uncertain at its first occurrence. Single hats, double hats, primes, `!`, and `+` are not identified with one another or silently made consistent. No interpretation of the double hat as a second completion is assumed.

Clear diagrams are encoded with `tikz-cd`. The large diagram on scan 344 preserves its unfilled bracketed quotient descriptions; detached arrows and the small unlabelled arrow sketch are described separately. Scan 348 uses a bracketed description because several vertical arrowheads do not resolve securely. These are transcriptions of objects and connections, not facsimiles of the page geometry. The large diagram requires a wide typesetting area; page layout and the editorial macro definitions are left to the parent document. A temporary wrapper verified LaTeX syntax and accented-label rendering; that wrapper is not part of the deliverable.

## 2. Table of doubts

Locations refer to the handwritten area, approximately from top to bottom; diagram positions and marginal locations are more dependable than line counts. Confidence concerns the ink reading, not the truth of a mathematical statement. Several related marks may be grouped in one row; all local uncertainty remains visible in the LaTeX.

| Scan | Approximate line / location | Reading retained | Alternatives / difficulty | Confidence |
|---|---|---|---|---|
| 341 | 1 | s'appellera | The compressed ending might be a present-tense form; not all letters are separable. | medium |
| 341 | 2, deletion before « Si » | Il | Overwritten and crossed; another short word is possible. | low |
| 341 | 4 and throughout | Γ with doubled left stem | The ink has a doubled left vertical and a top bar; no separate right stem supports Π. Alphabetic styling remains approximate. | high |
| 341 | 6, canonical map | fraktur S_I | Script S_I is an alternative typographical representation of the ornate glyph. | medium |
| 341 | 7 | cancelled word after « n'est » | No recoverable reading. | low |
| 341 | 8, codomain | cancelled superscript above S_I | Small dark crossed mark; do not supply an exponent. | low |
| 341 | left margin by Σ/Σ! | moralement | Very compressed word; initial and ending are uncertain. | medium |
| 341 | left margin by Σ/Σ! | one hat on T^{!+} | A second hat is not visible here, unlike the ambient group in the body. | medium |
| 341 | after « dans N_Σ » | three cancelled words | Heavy horizontal cancellation; word count is estimated. | low |
| 341 | below injective map | dont / quand | Initial letter and compressed ending are not securely distinguishable. | low |
| 341 | lower-left marginal equation | car; Σ/Σ! | The first word and numerator are overwritten or cramped. | low |
| 341 | penultimate displayed equation | N! / Σ! → N/Σ | Both marked letters are heavily retraced; no earlier underlying glyph can be recovered. | medium |
| 341 | final sentence | arithmétiquement | The extended ending and final tall stroke favour -ment; compressed intervening letters remain doubtful. | medium |
| 342 | 2, before « donc » | implication arrow | Very short heavy arrow, direction/type uncertain. | low |
| 342 | 4, insertion after N! | isomorphism arrow to Γ_Σ | The arrow is heavily rewritten. | medium |
| 342 | between paragraphs | two deleted words | Too heavily cancelled to recover. | low |
| 342 | « Soit maintenant » | I / I′ | No clear prime beside the first I, although the added cardinality uses I′. Kept explicitly unresolved. | low |
| 342 | « trous en » | I minus I′ | The left set symbol and difference stroke are retraced. | low |
| 342 | first displayed arrow | superscript * on π | A dark superscript is visible; possibly a cancelled glyph instead of an asterisk. | low |
| 342 | cancelled opening before « Considérons » | Pour une application | Last word looks like application, but cancellation crosses all three. | low |
| 342 | insertion and deleted generator list | b_i; b_{ν−ν′+1} … b_ν | Letters b and parts of the overwritten index are uncertain. | medium |
| 342 | above « groupes » | deleted bases | Overwritten word and attachment are not certain. | low |
| 342 | « groupes à lacets » | à; deleted dans | Small linking word and cancelled word are difficult. | medium |
| 342 | torsor subgroup | double-hatted G with subscript g;(ν,ν′) | Letter is overwritten; a semicolon appears here, whereas commas occur elsewhere. The tail of ν′ has a cancellation. | medium |
| 342 | right-hand addition « Aut » | lac subscript | Crowded below a cancellation; no expansion of an unseen qualifier is supplied. | low |
| 342 | action on S_ν | invarie | Compressed verb; « laisse invariant » is not visibly written out. | medium |
| 342 | right insertion | deleted aussi; l'ens | First word is overwritten; placement belongs after the action verb. | low |
| 342 | parenthetical complement | ou; ν−ν′; son/leur ens complémentaire | Overwriting in the index and a long insertion line obscure exact wording and attachment. | low |
| 342 | large left margin, opening | Disons aussi / Disons ainsi; ∀ base, ∀ discrétification | Very small diagonal writing; both quantifier-like marks are retained with doubt. The clause en définit une is clearer. | low |
| 342 | large left margin, middle | classes de conjugaison; par / pour; év. orientées | Connecting words after d’où and a later noun remain unreadable; the inserted π,π′ lies above the conjugaison line. | low |
| 342 | large left margin, ending | Il n'y a que; préarithmétisations / arithmétisations; demanderait; une analyse plus précise | The note is cramped and partly intersects the main body; the added verb ending is uncertain. | low |
| 342 | final sentence | one-hatted G_{g,ν′} | Letter is heavily retraced; one hat is visible. | medium |
| 343 | upper-left insertion and repeated shorthand | m-bar | A short horizontal sign abbreviates même; it is not silently expanded in the fragment. | medium |
| 343 | addition after « bases extérieures » | adapted to I′; deleted « (i.e.) pour lesquelles » | The retained quoted words are clearer than the cancelled explanatory tail. | low |
| 343 | interlinear addition before « si deux » | (p.ex.) | Small compressed abbreviation; another short parenthesis is possible. | low |
| 343 | after « compatibles i.e. » | deleted définissent | Initial letters visible; middle crossed by a long stroke. | medium |
| 343 | after second T(π) | comma | Small dark mark below the baseline might instead be a letter-shaped remnant. | low |
| 343 | cancelled bracketed block | revient; qui envoie | Multiple diagonal cancellation strokes obscure these connecting words. | low |
| 343 | cancelled lower equality | Σ | Overwritten central glyph; no attempt is made to recover an underlying earlier letter. | medium |
| 343 | lower paragraph, after « les ens. » | canoniques; one illegible item | Compressed long word and following item remain unresolved. | low |
| 343 | « sans utiliser de … sur I » | structure particulière / structures particulières | The terminal strokes do not securely distinguish number. | medium |
| 343 | before final Isom! | one deleted symbol | Dark retraced loop does not permit recovery. | low |
| 344 | Top, diagram title | `Bases de (π)` | The short word `de` is cramped against the opening parenthesis. | medium |
| 344 | Upper-left quotient, first and second denominators | `G⁺`, `G!⁺` | Calligraphic G rather than a script S; the alphabet is visually best supported by the repeated G shapes. | medium |
| 344 | Upper-left brace note | `pas séparé` | Two small slanting words; the second is not fully secure. | low |
| 344 | Centre-left brace note | `pas séparé` | Repeated annotation, equally compressed; no independent expansion supplied. | low |
| 344 | Central strict prediscretification, first numerator | `widehat Pi` | Initial letter is overwritten; hat and subscript survive. | medium |
| 344 | Central strict prediscretification, last numerator | `Isom ext_lac` (no `!`) | No secure exclamation is visible in this line, although one occurs in surrounding lines. No `!` has been supplied. | medium |
| 344 | Orientée labels above three node titles | Inserted `orientées` | Curved attachment strokes could resemble underlining; treated as insertion guides. | medium |
| 344 | Left secondary vertical arrow | A second, cancelled downward arrow | Its association with the first left vertical arrow is spatially clear, but its original endpoint is obscured. | low |
| 344 | Right long detached arrow | `widehat T_{g,nu}` | The label is legible; the arrow's endpoints are not attached to written objects. Described without supplying endpoints. | medium |
| 344 | Lower-right miniature diagram | Two offset lozenge-like arrow motifs and descending arrows | No objects are written; some small arrow connections remain uncertain. Kept as a bracketed diagram description. | low |
| 344 | Bottom-right note | `TSVP` | Closely joined capitals; no securely readable punctuation. | medium |
| 345 | Line 1, after `On pose` | One illegible cancelled item | Dense overwritten character or symbol. | low |
| 345 | Lines 5–6, insertion before `profini` | `ext` | Small superscript word with attachment stroke; no secure final point. | medium |
| 345 | Line 8 | `d'où` | Final letter and accent are compressed. | medium |
| 345 | Line 16, end of canonical-isomorphism paragraph | `u` | Could be another short handwritten variable; no named variable has been silently supplied elsewhere. | low |
| 345 | Line 17, following inserted `couples (π,Σ) d'un` | `groupe` / `groupes`, `profini` / `profinis` | Terminal s strokes cannot be settled after the insertion changed the sentence. | low |
| 345 | Line 18, above cancellation | `muni d'une` | Revised singular/plural ending is obscured; the older `munis d'une` remains cancelled below. | low |
| 345 | Line 19 | `isomorphismes`; `arithmétiquement` | Opening syllables of the first word are overwritten. The second word has a long ending with a final tall stroke, favouring -ment over -ques; it remains marked doubtful. | medium |
| 345 | Line 23 | `ou au choix` | Three compressed short words; the long word ends like `choix`. | low |
| 345 | Final line | `des autom` | The connecting word and absence/presence of a final point are not secure. | low |
| 346 | Line 2 | `pas`; `même` / barred-m abbreviation | `pas` is reduced to two strokes and the following darkened word may be the shorthand m-bar rather than full `même`. | medium |
| 346 | Line 6, insertion before `torseur` | Double-hatted `G!_{g,nu}` / single-hatted `G!_{g,nu}` | The tiny added hat marks are faint; both readings are shown. | low |
| 346 | Line 11, before `I'` | `si` / `à` | Very short connective, hard to separate from the preceding punctuation. | low |
| 346 | Line 11, before `hom.` | `un` / `des` | The short word is heavily retraced. | low |
| 346 | Lines 12–13, cancelled phrase | A group glyph and `dans widehat Pi` | One extra cancelled word/symbol cannot be recovered; the two group letters are marked doubtful. | low |
| 346 | Lines 14–15, displayed `hat G! = Σ!` | Single-hatted G retained | The glyph resembles G, although the preceding sheet defines Σ through a T-shaped glyph. No mathematical correction has been made. | medium |
| 346 | Line 16, after `de` | Underlined / cancelled `widehat G!_{g,nu}` | A line at the base of the group glyph may be an underline or a cancellation; both states are exposed in `\unsure`. | low |
| 346 | Lines 18–19, normalizer insertion | `je dis que ce` | The insertion rewrites cancelled `qui`; placement follows its bent guide. | medium |
| 346 | Lemma, after first normalizer term | One cancelled item | The surviving short crossed stroke is not safely recoverable. | low |
| 346 | Lower-left margin | `pas prouvé`; cancelled `de Norm(Σ!)/Σ!` | The remaining cancelled line is nearly wholly covered by diagonal loops. Four missing words/symbol groups are estimated. | low |
| 346 | Penultimate line | `Σ!` | Sigma is overwritten by another stroke; retained with doubt. | medium |
| 346 | Last line, after `qu'il` | `est` | Low contrast, compressed short word before membership sign. | low |
| 347 | l. 1, after “envie de” | `proposer` | `prononcer`; medial strokes do not resolve the word securely. | low |
| 347 | l. 1, before “la” | deleted illegible word | A small cancellation, perhaps a short grammatical word; no restoration attempted. | low |
| 347 | first display; 348 lower display | `Prédiscrét` | `Prédiscrit`; the abbreviated label and its vowel/diacritic are not secure. | medium |
| 347 | ll. 4–5 | `orientées`, `aient`, `autom.` | Endings, overwriting in `aient`, and abbreviation punctuation are not fully clear. | medium |
| 347 | l. 6 | `il faut et s.` | The final `s.` may abbreviate “suffit”; cancellation begins in this area. | low |
| 347 | l. 6, cancellation | `pour leurs im.` | Text is struck through and superseded by the insertion `qu'il en soit ainsi.`; the cancelled abbreviation is uncertain. | low |
| 347 | central paragraph, right edge | deleted `qui induit` | A second cancelled short clause precedes the insertion `a fortiori`; exact wording partly obscured. | low |
| 347 | central paragraph, after “implique” | `qu'il en induit` | `qu'il les induit`; merged short words do not support a confident grammatical reconstruction. | low |
| 347 | near normalizer map | deleted illegible marks after each normalizer | Old indices or arguments were heavily overwritten; count is estimated in the LaTeX. | low |
| 347 | following normalizer map | deleted `qui est de m̄` | The cancellation is long, and several strokes are merged with its horizontal line. | low |
| 347 | before quotient display | `correspondant` | Word outline is plausible but intermediate letters are indistinct. | medium |
| 347 | quotient display | deleted group symbols | Dense overwriting before both displayed quotient expressions is not reconstructed. | low |
| 347 | lower interlinear insertion | deleted `π = Π̂_(g,ν)` | The cancellation is legible only as a proposed group identification. | medium |
| 347 | lower parenthetical insertion | `choisissant`; un-hatted / hatted Π; `I'` or `i`; `élémt` / `élément` | The new identification has no separately secure hat. Wording and index variable are cramped; a hat remains visible in the cancelled earlier identification. | low |
| 347 | “le cas où” | `I' = {i'}` | The apparent prime within braces may be only the dot/stroke of `i`; the following map visibly uses `i`. | low |
| 347 | bottom parenthetical line | `autom.` | Presence of abbreviation stops is uncertain; last clause `pas seulement extérieurs` is substantially clearer. | medium |
| 348 | first line | `π̂` | The mark above the pi is overwritten; whether it is a surviving hat is uncertain. | medium |
| 348 | second line, rightmost argument | `(π,i)` | This is what is visible; no prime has been inserted to reconcile it with the preceding `(π')`. | medium |
| 348 | left margin beside “J'admets” | `rappelons qu'on suppose π nonabélien` | The first phrase and the word after pi are slanted and tightly written; the condition `(2g+ν≥3)` is clearer. | low |
| 348 | first two exact sequences | double-hatted `G` groups | Several group glyphs are overwritten and may preserve a corrected `T`; hats are recorded as visible. | medium |
| 348 | discrete sequence, kernel | `Π*_(g,ν−1)` | `Π+_(g,ν−1)`; the tiny superscript is not secure. | low |
| 348 | discrete sequence, remaining groups | `G` | Swash glyphs have been repeatedly overwritten; not enough ink separation to rule out a corrected `T`. | medium |
| 348 | prose immediately after discrete sequence | `connue` / `comme`; `sous` / `sans`; deleted `particulière` / `partie dense` | This short, partly cancelled clause remains very uncertain; it has not been made grammatical by conjectural emendation. | low |
| 348 | three-row diagram, top central object | `G!+_(g,ν)` | `T!+_(g,ν)`; heavily overwritten glyph. | low |
| 348 | three-row diagram, vertical links | descending or ascending | Four vertical strokes have rounded hooks without a securely resolved tip; the lower right arrow is more clearly descending. A bracketed diagram description preserves the uncertainty. | low |
| 348 | three-row diagram, below middle central object | deleted illegible material | One short crossed-out item, possibly an old label/index; not reconstructed. | low |
| 348 | quotient after “on lit sur le diagramme” | double-hatted `G` with `!` | Superscript is overwritten; an additional cancelled character is recorded as illegible. | low |
| 348 | final parenthesis | `=` | A leftward arrow is also possible; the sign before the hatted group is scribbled. | low |
| 349 | 1, deleted words and interlinear replacement | deleted `donnant par`; inserted `donnant` | The struck second word is particularly weak; the corrected word above it is much clearer. | low |
| 349 | 1, right insertion | `\widehat{\mathcal G}^{!+}_{g,\nu-1}` | The top decoration and `!` are cramped by the top edge; single hat appears likelier than double. | medium |
| 349 | 2, initial group symbol | `\mathcal T'` | A small superscribed trace could be part of a correction or a hat; the prime is visible. | medium |
| 349 | 3, cancellation after “et” | `N(\Sigma)` | Crossed strokes prevent a secure reading; the last symbol resembles Sigma. | low |
| 349 | 8, corollary opening | `is.` | Possibly `iso.`; no full word supplied. | medium |
| 349 | 9, corollary display | right-directed isomorphism arrows, continuation, deleted `\Gamma_{g,0}` | The continuation is a single horizontal mark rather than three distinct dots; the canceled last term remains doubtful. | medium |
| 349 | left margin beside corollary | “On voit aussi que … invariant dans … équivaut à … invariant dans …” | The repeated word invariant is favoured by the ink; Sigma decorations, the first ambient group, and the connective remain uncertain. | low |
| 349 | 10, abbreviated adverb | `canoniqt` | Compressed ending may have a superscript `t`; no expansion is put in the transcription. | medium |
| 349 | 13, overwritten word before “admis” | deleted illegible word | Dark overwritten strokes could be a cancellation rather than an additional word. | low |
| 349 | 14, first source and target | `\widehat{\widehat{\mathcal T}}^{!}_{g,(\nu,\nu-1)}` to double-hatted `\mathcal M_{g,\nu-1}` | Source superscript is faint; target is M-like and differs visibly from the G in the following line. | low |
| 349 | 17, “foncteur … sens inverse” | `en` | Small following dots may belong to the word ending or punctuation. | medium |
| 349 | 17, quoted operation | `forage` | Independent rereading resolves the initial f and descending g; an earlier candidate bouchage is rejected. | high |
| 349 | 18, final line | `quid\|qui en des étal. de courbes reste incompris` | Several initial short words remain unresolved; reste is probable and incompris is clearer. No grammatical repair is supplied. | low |
| 350 | heading | `(suite)`; `passage` | The parenthetical word and the compressed strokes in `passage` are not fully distinct. | medium |
| 350 | 1, end | `considérons\|considéré` | The ending is compressed; grammatical plausibility has not been used to choose silently. | low |
| 350 | 3, parenthesis | `on en\|on le vérifie` | The short word between `on` and `vérifie` is uncertain. | low |
| 350 | 4, deleted phrase | illegible word + `discrétifié` | The interlinear replacement “muni des” is clearer than the canceled text. | low |
| 350 | 4 | `traces sur π` | `traces` is a probable reading; the displayed group appears **unprimed** and no prime has been restored from mathematical expectation. | medium |
| 350 | 4 | `lacets` | The final `s` is compressed. | medium |
| 350 | canceled block, lines 6–7 | `n conjugués`; `int(g)` | `n` is overwritten, and the conjugation abbreviation is cramped. | medium |
| 350 | canceled block, index parenthesis | `n=[π:π′]` followed by a brace-like mark, then `1≤α≤n` | A possible right brace is preserved as uncertain; the condition is interlinear over an unreadable canceled word. | low |
| 350 | canceled block, crossed lines 8 and 10 | `comptés\|compter le nb de fois qu'une classe de conjugaison…` | Ending of first word and a few crossed small strokes are weak; the interlinear replacement is kept separate. | low |
| 350 | canceled block, interlinear formula | `d_α\|d_{iα}` and `L′_{iα}\|N′_{iα}` | The `i` may be absent in the first subscript; the denominator's letter is crossed/overwritten. | low |
| 350 | canceled block, before `L′_{iα}=…` | `pour` | Possibly `où`; overwritten initial letters remain unclear. | low |
| 350 | canceled block, final row | `conjugaison` | Final `s` cannot be excluded. | medium |
| 350 | 15, deletion before second “sous-groupes” | `les` | Heavily canceled short word. | low |
| 350 | condition b) | relation `=\|:`; singular `lacet` | The relation is two tiny strokes; no final `s` is distinctly visible in `lacet`. | medium |
| 350 | beside formula (1) | `où\|ici` | The initial word of the parenthesis is compressed; the index formula itself is clear. | medium |
| 350 | formula (2), deleted beginning | `2g\|2α` | The canceled variable is overwritten. | low |

## 3. Abbreviations met

Expansions below are tentative explanations in the apparatus only. Dots, singular/plural endings, and uncertain readings remain as transcribed in the LaTeX. Mathematical operator names are included alongside prose abbreviations.

| Form as written / tentatively read | Proposed expansion or interpretation | Qualification |
|---|---|---|
| `hom`, `hom.` | homomorphisme | Singular or plural depends on the uncertain surrounding wording. |
| `i.e.` | id est | Not expanded in the transcription. |
| `ss-groupe`, `ss-groupes` | sous-groupe, sous-groupes | Hyphenated shorthand. |
| `autom`, `autom.`, `automs.` | automorphisme(s) | Final stops and the written s are preserved where visible. |
| `ext`, `ext.` | extérieur(s) | Also appears in operator names; the insertion before profini on scan 345 is uncertain. |
| `ab` | abélianisé / abélianisation | Subscript in the opening formula. |
| `card` | cardinal | In set cardinalities and the Hurwitz annotation. |
| `lac` | lacets / respectant les lacets | Operator subscript; its exact definitional scope requires earlier pages. |
| `Aut`, `Aut ext` | automorphismes, automorphismes extérieurs | Mathematical operator names. |
| `Isom`, `Isom ext` | isomorphismes, isomorphismes extérieurs | Mathematical operator names. |
| `ens`, `ens.` | ensemble(s) | Written without a secure stop in some insertions. |
| `chgt` | changement | In the torsor comparison. |
| `év.` | éventuellement | Doubtful diagonal insertion on scan 342. |
| $\overline{\mathrm m}$ | même | The barred-m sign is preserved, not expanded. |
| `p.ex.` | par exemple | Doubtful small insertion on scan 343. |
| `NB` | nota bene | Underlined where visible. |
| `isom`, `isom.` | isomorphisme | Both forms occur. |
| `can.` | canonique | Underlined on scan 345. |
| `tt` | tout | In tt comme. |
| `Norm` | normalisateur | Mathematical operator. |
| `TSVP` | tournez s'il vous plaît | The letters themselves are doubtful. |
| `s.` | suffit | Tentative reading in il faut et s. |
| `im.` | images | Tentative reading in cancelled text. |
| `iso` | isomorphisme | Underlined on scan 348. |
| `Prédiscrét` / `Prédiscrit` | prédiscrétifications | Abbreviated set label; the vowel/diacritic is uncertain. |
| `Préarithm.` | préarithmétisations | Abbreviated set label. |
| `is.` | isomorphismes | Could read iso.; scan 349. |
| `canoniqt` | canoniquement | Compressed ending, possibly superscript t. |
| `étal.` | étale(s) | Highly uncertain final line of scan 349. |
| `rev.` | revêtement | Section heading on scan 350. |
| `tjrs` | toujours | Scan 350. |
| `int` | automorphisme intérieur / conjugaison intérieure | Uncertain in the cancelled coset discussion. |
| `mod` | modulo | In the cancelled coset discussion. |
| `nb` | nombre | In cancelled text. |
| `Centr` | centralisateur | In conditions a)–b) on scan 350. |
| `élémt` | élément | Possible abbreviation in the cramped insertion on scan 347. |

The uncertain reading `quid` on the last line of scan 349 would be a Latin interrogative word, not an abbreviation; `qui` remains an alternative.

## 4. Legibility assessment

The large formulae and most uninterrupted prose are substantially more legible than the interlinear revisions. The least secure text is the diagonal left margin of scan 342, the small inserted parenthesis on scan 347, the clause following the discrete exact sequence on scan 348, and the final line of scan 349. These passages retain alternative readings and estimated gaps; they have not been made grammatical or mathematically coherent by restoration. The quotation **forage des trous** on scan 349 is clearer after independent rereading, but the words following it remain partly doubtful.

The two small brace annotations and detached arrows on scan 344, overwritten group letters and lower marginal calculation on scan 346, and several vertical connectors on scan 348 warrant particular caution. The cancelled block on scan 350 is less reliable than its intact lower half. In particular, the summation restriction **sur i**, the prime in **2g′−2**, and the centralizer subscripts were checked individually. The explicit admission **J'admets**, the marginal **pas prouvé**, and the subsequent warning **est peut-être tout à fait faux !** are preserved and are essential to the research notes' conditional reading of the argument.

## 5. Research notes — English, separate from the transcription

These notes concern only what is written, asserted, questioned, or left unfinished in the supplied excerpt. Each item cites its scan and approximate location, supplies its kind, and quotes the relevant wording when the reading permits. “Unproved claim” means that the necessary proof is not provided in these pages; it makes no claim about other parts of the manuscript or the literature. Items labelled “own idea” are suggestions with stated confidence and reasons, not claims of novelty or established results. In particular, the consequences following the admitted step on scan 348 remain conditional in view of the warning on scan 349.

1. **Scan 341, opening; conjecture.** The identification of the abelianized normalizer quotient with profinite units is explicitly conditional: « Si notre conjecture fondamentale est vraie ». The pages supplied here do not state that conjecture in full, so its precise hypotheses and the character's asserted kernel must be recovered from earlier pages before evaluating the conclusion.

2. **Scan 341, middle and lower half; unproved claim.** The product map from N/Σ! to N/N! × N/Σ is called injective and then « bijectif ». A proof should isolate the asserted surjectivity Σ → S_I and the intersection Σ! = Σ ∩ N!; these supply the group-theoretic conditions behind the displayed decomposition.

3. **Scan 341, end; unpursued implication.** The isomorphism N!/Σ! → N/Σ suggests that the normalizer quotient can be recovered using automorphisms fixing the peripheral index set pointwise; the next page continues « extérieurs induisant l'identité sur I ». This should be checked with the exact ambient groups and hat conventions, without assigning a meaning to the different hat conventions from notation alone.

4. **Scan 342, first paragraph; unproved claim.** In type (0,3), the manuscript asserts Σ! = (1), identifies Σ with S_3, and says the normalizer « s'identifie au produit direct des deux », referring to the centralizer and S_3. This is presented as the special case of the preceding product argument; verifying the triviality of Σ! requires its definition on earlier pages.

5. **Scan 342, middle; unproved claim.** The bases adapted to the retained peripheral set « forment un torseur » under a specified subgroup of the double-hatted automorphism group. A proof should check existence, freeness, and transitivity of the action, keeping track of the revised choice of the first ν′ peripheral generators and the distinction between automorphisms and outer automorphisms.

6. **Scan 342, end; unpursued implication.** Filling holes is described by « le chgt de groupe d'opérateurs » between the displayed double-hatted groups. This suggests comparing filling several holes at once with successive fillings at the level of torsors; compatibility of those maps, including their markings, would need proof and should not be assumed from a drawing.

7. **Scan 342, left margin; conjecture (question; reading uncertain).** The marginal note appears to reserve the arithmetic structures for further examination (the closing words are tentatively read « une analyse plus précise »). The wording and its precise referent are not fully legible, so this is only a flag to re-examine the manuscript, not a securely transcribed mathematical assertion.

8. **Scan 343, upper-middle; conjecture (question).** The manuscript asks « en déduit-on une préarithmétisation de π′ » from one of π. Its reformulation asks whether two prediscretifications having the same exterior automorphism subgroup still have compatible images after filling holes; the question mark and interrogative inversion must not be converted into a theorem.

9. **Scan 343, opening; unproved claim.** The statement « toute prédiscrétification de π en définit une de π′ » extends the filling construction to several kinds of structure. A proof needs well-definedness under the equivalence relations defining each kind and careful placement of the added condition « adaptées à I′ ».

10. **Scan 343, crossed-out block; conjecture (question; cancelled formulation).** A proposed reformulation in terms of a map between double-hatted outer automorphism groups is crossed out as a whole and stops after « dans ». It may reveal an attempted route toward the preceding question, but it is not an additional asserted lemma or a completed statement.

11. **Scan 343, lower paragraph; unproved claim.** Choosing « un ordre total » on the peripheral set is said to define a sub-torsor under the group marked with !. The argument should explicitly identify the fibre over the chosen order and the pointwise stabilizer; without the preceding definitions one should not infer a canonical choice of that order.

12. **Scan 343, middle; own idea.** A useful test is to compare stabilizers before and after quotienting by the normal closure of the filled peripheral subgroups, rather than to assume that a stabilizer always descends faithfully. **Confidence: medium as a research strategy, not as a result; reason:** the explicit compatibility question singles out precisely a possible loss of information under filling.

13. **Scan 344, large diagram — unproved claim.** The diagram identifies spaces labelled “discrétifications,” “prédiscrétifications strictes,” “prédiscrétifications,” and “préarithmétisations” with successive quotients of isomorphism torsors. A proof should verify the action and stabilizer at each stage, including the `!` variants and the three arrows labelled `{±1}`; the sheet itself supplies identifications rather than an accompanying argument.

14. **Scan 344, two left braces — own idea. Confidence: low; reason: the repeated marginal reading is uncertain.** If the annotations do read “pas séparé,” investigate whether these mark the topological failure of separation of the quotients by discrete groups. One should first settle the word from the image and then check the topology intended on the relevant isomorphism torsor; no separation assertion is being added to the transcription.

15. **Scan 345, middle paragraph — unproved claim.** The isomorphism `Γ_Σ → Γ_Σ'` is asserted to be canonical: “ne dépend évidemment pas du choix de u” (the variable is uncertain). A proof would compare two isomorphisms transporting the chosen data and show that their discrepancy induces the identity on the normalizer quotient; this requires identifying that discrepancy with the appropriate subgroup rather than simply invoking isomorphism of the underlying groups.

16. **Scan 345, lower paragraph — unproved claim.** The manuscript says the specified pairs with their indicated isomorphisms “forment un groupoïde connexe,” with an “objet ‘origine’.” Establishing this description requires existence of morphisms between any two permitted pairs, compatibility of composition with the arithmetic condition, and the claimed identification of the origin's automorphism group with `Γ_{g,ν}`.

17. **Scan 345, final paragraph — own idea. Confidence: medium; reason: the two phrases are readable, but the exact surrounding definitions are outside this sheet.** Compare “à isom unique près” with the simultaneous identification of an automorphism group `Γ_{g,ν}`. It may be necessary to distinguish uniqueness of the *construction of the chosen origin* in an additionally marked setting from uniqueness of every isomorphism between objects in the groupoid; this is a question about the intended categorical scope, not a correction of the manuscript.

18. **Scan 346, opening paragraph — unproved claim.** The four spaces other than “Bases (π)” and “Bases ext (π)” are said to be homogeneous under the indicated `!` automorphism group and to be quotients of an `Isom!` torsor. A proof would need the transitivity of that restricted action and a careful check that each of the four written subgroups is the relevant stabilizer; the exception for the two base spaces is part of the claim and must remain visible.

19. **Scan 346, middle paragraph — unproved claim.** For the selected `I'`, a homomorphism between the doubly hatted automorphism groups is stated to send the unhatted groups, single-hatted groups, and the indicated `Σ!` and product subgroups into their counterparts. The construction and the precise role of the chosen indices should be checked before using it to define maps on the four quotient spaces.

20. **Scan 346, final lemma and margin — unproved claim.** The displayed lemma identifies `N_Σ!` with the normalizer of `Σ!` inside the indicated `!` group; the margin says “pas prouvé.” The proposed argument reaches “montrons qu'il normalise Σ,” so the essential missing implication is that normalizing the smaller subgroup `Σ!` forces normalization of the larger `Σ` in the stated ambient group; the note records the status on this sheet, without assuming what happens on later pages.

21. **Scan 346, paragraph preceding the lemma — own idea. Confidence: high for the general algebraic issue, medium for its relevance here because preceding definitions may supply the needed property.** The phrase “comme Σ! s'envoie dans Σ! … [N!] s'envoie dans le normalisateur” deserves a separate functoriality check: inclusion of a subgroup image alone does not in general imply the corresponding inclusion of normalizer images. Surjectivity onto the target subgroup, or a suitable characterization of that subgroup invariant under the image action, would be a sufficient additional ingredient to seek; this is not offered as a counterexample to the manuscript's specific groups.

22. **Scan 347, opening paragraph — conjecture.** The manuscript introduces a “conjecture” that the canonical map between the oriented prediscretification sets is “bijective.” A proof must establish both existence and uniqueness of a lift through the indicated filling/forgetting operation; the uncertainty in the abbreviated set name does not affect the explicit status of this statement as a conjecture.

23. **Scan 347, after the first display — unproved claim.** The argument asserts that equality `Σ_α = Σ_β` is equivalent to equality for their images, and hence that “la bijection précédente induit une bijection” of prearithmetizations. The point requiring justification is reflection of equality of the embedded automorphism subgroups by the group map, rather than merely preservation of equality in the forward direction.

24. **Scan 347, central paragraph and normalizer quotient display — unproved claim.** The inserted assertion that “les bijections précédentes sont compatibles avec” a homomorphism of operator groups is followed by a map of normalizers and an assertion that its quotient map “est un isomorphisme.” A full argument needs a precise statement of the operator action and a check that every relevant target normalizer class has a lift, with the quotient kernel identified; the cancelled formulas do not supply such a proof here.

25. **Scan 347, lower paragraph — unproved claim.** “Pour s'en convaincre il suffit de regarder … le cas où” introduces singleton notation for `I'`, while the following page uses type `(g,ν−1)`. The role of this index set must first be reconciled with the earlier filling prescription, whose complement notation is also revised and partly uncertain. An iterative reduction would then need compatible compositions and control of dependence on the order of filling; those details are not supplied here.

26. **Scan 347, final parenthesis — unproved claim.** The parenthesis says that outer automorphisms preserving the relevant lacet define automorphisms of the filled group that are “pas seulement extérieurs.” The passage from outer to actual automorphisms should be constructed explicitly and proved independent of representatives; the short explanatory parenthesis does not itself verify that independence.

27. **Scan 348, opening assumption — unproved claim.** “J'admets ... par analogie avec le cas discret” explicitly qualifies the assertion that the displayed homomorphism is an “iso.” This assumption carries the subsequent exact sequences and the conclusion about bijectivity; the surrounding argument should not be presented as an unconditional proof.

28. **Scan 348, exact sequences and three-row diagram — unpursued implication.** The diagram distinguishes a discrete row, a row with single hats, and a row with double hats, while reusing a hatted surface-group kernel in the lower two rows. Establishing the vertical comparisons would clarify the relation between the kernels in the single-hat and double-hat groups; the definitions of those groups must be recovered from preceding pages before interpreting the comparison.

29. **Scan 348, paragraph beginning “L'application” — unproved claim.** “on lit sur le diagramme” is the stated basis for identifying the quotient sets and deriving “la bijectivité.” A rigorous quotient argument needs compatible surjections and exact kernel identifications, and must check the superscript `!` versus `!+` conventions; the transcription retains the visible difference rather than repairing it.

30. **Scan 348, exactness assumption — own idea (confidence: medium).** Test the proposed sequence of profinite groups in finite characteristic quotients of the punctured group, tracking the indicated kernel and the kernel after filling a puncture. This could locate an obstruction to kernel equality or to surjectivity, because exactness of the discrete sequence alone does not establish either property for the single-hat and double-hat groups with definitions not supplied in these scans; it is a suggested diagnostic, not a theorem or a claim of novelty.

31. **Scan 349, lines 1–7 — unproved claim.** The text says the normalizer of `Σ` “est l'image inverse” of the normalizer of `Σ′`, and deduces `N/Σ ≃ N′/Σ′`. A proof should state the quotient homomorphism and the precise inverse-image relation for `Σ` and `Σ′`; the normalizer assertion is only justified under those hypotheses. The immediate argument may supply those hypotheses on the preceding page, but they must be checked rather than inferred from the conclusion.

32. **Scan 349, corollary, lines 8–12 — unpursued implication.** The displayed identifications, described as “canoniques,” assert independence of the normalizer quotient from the number of punctures down to the listed stable cases: `(g,0)` for `g≥2`, `(1,1)` for genus one, and `(0,3)` for genus zero. The subsequent NB explicitly questions an admitted fact, so this is recorded as a conditional consequence, not an established invariance theorem. Compatibility of the identifications with successive choices of filled punctures would be a further issue to investigate.

33. **Scan 349, NB, lines 13–16 — conjecture (expressed doubt).** Grothendieck writes that the admitted fact is “loin d'être évident” and “est peut-être tout à fait faux !”. The doubt expressly includes surjectivity of one displayed map and injectivity of a second; because the first target glyph is uncertain, its group identification should be settled from the manuscript before these become precise research statements.

34. **Scan 349, final paragraph, lines 17–18 — unproved claim.** The admitted fact is recast as an “énoncé d'existence d'un foncteur” in the inverse direction, with the operation quoted as “forage des trous” (the quoted operation is clear after rereading). Establishing this formulation would require specifying the source and target categories and their morphisms, constructing the functor, and checking how its induced maps recover the disputed group-theoretic properties. The closing handwritten line remains too uncertain to supply additional hypotheses safely.

35. **Scan 349, corollary and NB — own idea.** Test the proposed invariance first at the smallest displayed stable cases, while separating failure of injectivity, failure of surjectivity, and failure of functorial compatibility under successive fillings. **Confidence: medium** as a research strategy, because the NB explicitly isolates injectivity and surjectivity, while compatibility is an additional question suggested here by the canonical identifications; no claim is made that these tests will settle the problem or are new.

36. **Scan 350, first paragraph, lines 1–5 — unproved claim.** The statement that a finite-index subgroup inherits a group-with-peripheral-loops structure is introduced with “On sait” and a reduction “par passage au cas discret.” A proof would need to specify the discrete realization, justify passage to its profinite completion, and verify that the peripheral subgroups obtained by intersection are precisely those intended. The apparent unprimed `π` in the phrase transcribed “traces sur π” has not been corrected in the text.

37. **Scan 350, conditions a)–b), lines 16–17 — unproved claim.** The words “sont ainsi les sous-groupes” introduce a characterization through `L′=Centr_π(L′)∩π′` and the condition that its centralizer is a peripheral subgroup of `π`. Proving both directions requires a precise centralizer statement under the manuscript's hypotheses; it should not be extended to arbitrary profinite groups without checking those hypotheses.

38. **Scan 350, formula (1), lines 18–21 — unproved claim.** The degree function is followed by the fiberwise identity `∑d(i′)=n`, with the summation restricted by “sur i.” A proof must identify the fiber over each peripheral class and relate the index `d(L′)=[L:L′]` to its contribution, while controlling the representative choices. This restriction of the sum is essential and is retained explicitly in the transcription.

39. **Scan 350, formula (2), final lines — unproved claim.** “On aura la formule de Hurwitz” announces the displayed genus relation rather than proving it on this page. The overbrace also identifies the ramification sum with `n card I−card I′`; its verification should first use the fiberwise identity (1), then establish the genus identity under the chosen interpretation of the peripheral data. Nothing here determines whether a proof is given on a subsequent page.

40. **Scan 350, canceled coset discussion and formula (1) — own idea.** A natural proof strategy is to study the action of a peripheral subgroup on the finite coset set of `π′` in `π`, using its orbits to organize the fibers and their lengths. **Confidence: high** as a candidate explanation of the displayed finite sum, because both coset representatives and subgroup indices are visibly present in the canceled discussion; the required identification of the manuscript's peripheral classes still needs proof, and no novelty is asserted.

41. **Scans 349–350, transition — own idea.** Keep two distinct questions separate in a later comparison: recovering peripheral and degree data for an actual finite-index subgroup, and constructing the inverse-direction “forage des trous” functor questioned on scan 349. **Confidence: medium**, because the first is addressed by explicit subgroup/centralizer conditions here, whereas the second is expressly doubted on the preceding page; neither should be used as evidence for the other without an additional argument.

## Source reference

Grothendieck, A. (1981). *La Longue Marche à travers la théorie de Galois* [Handwritten manuscript, cote 140-2; supplied scans 341–350 of the archive file designated “pages 1–292”]. Université de Montpellier.

Bibliographic details follow the accompanying task brief. The scan/location references throughout this apparatus refer to the supplied images, not to an externally consulted edition. No claim is made here about the later resolution or originality of the research questions.

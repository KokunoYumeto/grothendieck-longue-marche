# LM_P060 — Notes to the diplomatic transcription

## 1. Source, scope, and conventions

The accompanying `LM_P060_transcription.tex` transcribes the ten supplied JPEG images, scans 11–20, in their supplied order. Bibliographic information follows the accompanying task prompt: Alexander Grothendieck, *La Longue Marche à travers la théorie de Galois* (1981), Montpellier archive cote 140-3, file described as pages 293–650. The images themselves are the evidence for every reading. No published transcription or external mathematical source was used to complete the text.

The LaTeX file is a fragment and begins with `\scanpage{11}`. It has no preamble or macro definitions. It uses the requested editorial macros and ordinary mathematical LaTeX. The deliberately visible uncertainty alternatives are parts of the transcription. Counts in `\illegible{n}` are estimates; an unreadable mathematical factor or subscript is counted as one unit where a word count is inapplicable. Paragraph order is retained, with interlinear additions attached at the visible or explicitly doubtful attachment point. Broad cancellations and readable material beneath them are preserved.

Upper folio numerals and lower handwritten image-sequence numerals are distinguished. The lower numerals agree with the printed archive counters, but their authorship cannot be established from these images; they are retained as `\margin{…}`, without attributing them to Grothendieck. The printed institutional footers outside the manuscript frame are excluded.

| Scan | Supplied image | Visible upper folio (`\mspage`) | Lower handwritten numeral (`\margin`) |
|---|---|---|---|
| 11 | `LM_P060_scan011.jpg` | — | 10 |
| 12 | `LM_P060_scan012.jpg` | 294 | 11 |
| 13 | `LM_P060_scan013.jpg` | — | 12 |
| 14 | `LM_P060_scan014.jpg` | 295 | 13 |
| 15 | `LM_P060_scan015.jpg` | — | 14 |
| 16 | `LM_P060_scan016.jpg` | 296 | 15 |
| 17 | `LM_P060_scan017.jpg` | — | 16 |
| 18 | `LM_P060_scan018.jpg` | 297 | 17 |
| 19 | `LM_P060_scan019.jpg` | — | 18 |
| 20 | `LM_P060_scan020.jpg` | 298 | 19 |

The visible distinction between the marked subset `X^{!}` and the covering surface `X'` is preserved. Looped Latin path letters are encoded as `\ell`, while Greek lambda remains `\lambda`. Clearly doubled number-field and projective-space letters are encoded with `\mathbb`; uncertain alphabet choices are marked. The arched endpoint arrows on scan 16 are represented by `\overset{\curvearrowright}{x,z_i}`. Equation number (21) occurs on both scans 13 and 16 and has been retained in both places.

Two page-state issues deserve explicit mention. On scan 13, **provient** has a horizontal cancelling stroke and approximately six sublinear dots, which may restore the cancelled word; the fragment marks the deletion status as uncertain. On scans 16–17, a cancelled sentence continues across the boundary as **l'excep- / tion**; each visible portion remains in its own page. The drawings on scan 17 are recorded in a `\figure` description, with doubtful tiny labels identified individually.

## 2. Table of doubts

Locations refer approximately to physical manuscript lines, formulas, or marginal positions. The anchors are more reliable than a continuous line count where revisions overlap. **High** means the visible feature is strongly supported, including a few initially doubtful readings resolved by rereading; **medium** means a preferred reading remains uncertain; **low** means the wording, symbol, or editorial state is substantially unresolved. Confidence concerns the reading of the ink. A mathematical expectation has not been used to settle an ambiguous character.

| Scan | Approximate line / location | Reading retained | Alternatives or qualification | Confidence |
|---|---|---|---|---|
| 11 | 4, right edge, following « de sorte que » | `\deleted{$\forall x\in X$}` | The quantifier is visible but the cancellation status and the crowded following symbols are uncertain. | low |
| 11 | 5, before « les stabilisateurs » | `\deleted{\illegible{1}}` | A compact overwritten/cancelled group cannot be resolved. | low |
| 11 | 5, after `(x∈X)` | « opèrent » | Final strokes are overwritten; « opère » is possible. | medium |
| 11 | 8, parenthesis after `Y=X/G` | « surface topologique » | Singular/plural terminal strokes are faint. | medium |
| 11 | 11, small mapping below « signature » | `a↦d_X(a)` | Small argument could be `u` or `b`; no mathematical normalization has been made. | low |
| 11 | 15–16, both local-degree factors | `ν_a` | `ν_x`; the tiny subscript is looped and a-like, but a cursive `x` cannot be excluded. The surrounding argument `x` has not been used to settle it. | low |
| 11 | 19, description of the second covering category | `H-rev` with superscript `ts` | The shortened ending is uncertain; it may be written on the baseline. | medium |
| 12 | 2, item b) | « trouve » | Interior letters are abbreviated to strokes; « définit » would fit the construction but is not adopted from context. | medium |
| 12 | 8, after « Remarques. » | `OPS` | `OFS`; the middle letter is poorly separated from the first. | medium |
| 12 | 9, after definition of `S` | « remplaçons » | « remplacer » or « remplaçant » is less likely; ending faint. | medium |
| 12 | 10, after `X\setminus S` | Closing parenthesis | A closing parenthesis appears before the comma and is retained, even though the continuation is syntactically awkward. | high |
| 12 | 10–11, inserted condition | `OPS` | `OFS`; same compact abbreviation as above. | medium |
| 12 | 10–11, inserted replacement | « par » | Compressed link between the two marked-set expressions; independent rereading did not resolve every stroke. | low |
| 12 | 11, right interlinear set definition | `S={x∈X! \| d_X(x)=1,[G_x]=1` | Crowded over the following prose; terminal brace/parenthesis is not securely visible and is not supplied. Exact separator before `[G_x]` uncertain. | low |
| 12 | 11, main line beneath insertion | « pour nous est » | Overlapped by the smaller set definition; « pour nous » more secure than final word. | low |
| 12 | last line | « donnée » | Final letters and accents are faint; plural not securely excluded. | medium |
| 13 | Formula (21), both groups, and group in the following paragraph | Comma before each basepoint | Semicolon; inner parentheses are clearly visible, but these very small separators are not fully distinct. | medium |
| 13 | 5, « en termes de ... » | « calculs » | Final plural stroke faint; singular « calcul » possible. | medium |
| 13 | 6, after the fundamental group | `\deleted{provient}` within an uncertainty mark | Clear word crossed through, with approximately six dots underneath; these may indicate restoration. Confidence is high for the word and visible marks, lower for its editorial status. | medium |
| 13 | 10–11, equivalence of pairs | `sss` | `ssi`; the visible sequence has three s-shaped strokes and no secure dot over a final `i`. | medium |
| 13 | 14, between « les » and `λ_a^{d_X(a)}` | Underlined « le » / underlined `ℓ` | Tiny looped and possibly overwritten glyph with a separate short lower stroke. Independent rereading did not confirm the earlier candidate `k`; no mathematical interpretation is imposed. | low |
| 13 | 15, definition of `λ_a` | « classe » | Very compressed strokes. | medium |
| 13 | 17, « l'image de ... dans H » | script `G` | Initial doubt resolved in favour of the large script group letter by independent comparison with repeated forms on the page; the unexpected wording is retained. | high |
| 13 | 18, beginning of last line | « Et » | « et » or overwritten initial word. | low |
| 13 | 18, both labels over equals signs | `dfn` | `déf`; independent reading favours an initial looped `d`, tall `f`, short final `n`, though the letters remain tiny. | medium |
| 14 | 1, after `(γ,ℓ)` | Deleted `\illegible{1}` | A short heavily cancelled item; it may have been “est,” but too little survives to transcribe it as a word. | low |
| 14 | 10, above “dans” before `λ_b^{ν(a)}` | Inserted `\rightsquigarrow` | The raised wavy stroke and descending mark may be a correction/attachment sign rather than another mathematical arrow. | low |
| 14 | 12, between the powered meridians | `\rightsquigarrow` | `\sim`; the right end is too faint to settle whether it has an arrowhead. | low |
| 14 | 13, opening of the example | “Revenons” | No secure alternative; final minims are compressed. | medium |
| 14 | 14, group equalities, twice | `\mathfrak S_3` | `\mathcal S_3`; the letter is a stylized S, but the intended mathematical alphabet is not fully secure. | medium |
| 14 | Addition above the right end of line 14 | Deleted `\illegible{1}` at the beginning of `X^{!}` | An overwritten initial item of the set cannot be recovered. | low |
| 14 | 16, before “au quotient” | “passage” | No secure alternative; several interior letters are faint. | medium |
| 15 | 1, `d_Y` in the opening fundamental group | `\underline d_Y` | Plain `d_Y`; the short heavy lower stroke may be an underline or a pen retracing. | low |
| 15 | 1–2, group description | “cartographique” | No secure alternative; the word straddles the line boundary and its first portion is faint. | medium |
| 15 | 6, cancelled words before “un choix” | “six places” | “six points”; the second word is crossed through. | low |
| 15 | 6, “dans un …” | “ens” | Possibly “ens.”; no clear terminal period is visible. | medium |
| 15 | 10, after “Ils se trouvent” | “respectivement” | No secure alternative; a compressed cursive middle and final stroke. | medium |
| 15 | 13, after `(0,1,∞)` | “supérieur” | A plural ending cannot be excluded from the final stroke. | medium |
| 15 | Interlinear gloss after “supérieur” | “hémisphère” | “hémisph”; the ending may be abbreviated and is partly crossed by a descender from the line above. | low |
| 15 | 17, after the chosen `(0,1/2)` | “correspondant” | No secure alternative; the word ending is a rapid stroke. | medium |
| 15 | 18, before the three `τ'_i` | Deleted `\illegible{1}` | A cancelled earlier symbol or short item, not securely recoverable. | low |
| 15 | 19, small added phrase above `s'obtiennent` | “au dessus” | “en dessus” is not excluded; the first pair of letters is very small. The phrase is treated as interlinear addition. | medium |
| 15 | 22, final line | “grand cercle” | “grands cercles”; singular/plural endings are not distinct. | medium |
| 16 | 3, before “triangle” | “du double” | “des doubles”; the article and endings are slight strokes. | medium |
| 16 | 4, before `(0,1,∞)` | “triangle sphérique” | “triangles sphériques”; the terminal strokes do not securely settle number. | medium |
| 16 | 5, after “situé” | “respectivement” | No secure alternative; abbreviated-looking interior strokes. | medium |
| 16 | 5, before the first side | “le côté” | “les côtés”; the plural marks are not clearly separable. | medium |
| 16 | Left diagonal margin, second line | “caractérisés” | No secure alternative; the ending and internal accents are faint. | medium |
| 16 | Left diagonal margin, tiny insertion | “resp.” | The mark could be a shorter qualification; the placement before “comme” is clear, the exact letters less so. | low |
| 16 | Left diagonal margin, before “dans les triangles” | “se trouvant” | No secure alternative; the first word and verb ending are compressed. | medium |
| 16 | 7, after “Les points” | Deleted `\illegible{1}` | A cancelled short word, perhaps “les,” remains unclear. | low |
| 16 | 8, after `τy sont` | “respectivement” | No secure alternative; a rapid connected stroke. | medium |
| 16 | 9, third endpoint expression | Deleted `\dot\sigma_\infty` | A dotted sigma and infinity-like subscript appear beneath cancellation, but the whole item is overwritten. | low |
| 16 | 11, deleted pair after “éléments” | `(\dot\sigma_0\dot\tau,\lambda_0)` | Both components are overwritten; the sigma subscript and the second lambda's subscript are insecure. | low |
| 16 | 15, between “de” and `−j̄=P` | Deleted “x à” | The second mark could be a relation symbol; the cancellation obscures it. | low |
| 16 | 17, last basepoint in the displayed identification | `P` | Lowercase `p`; letter size/descender makes case uncertain. | low |
| 16 | 18, after “On peut alors prendre” | Deleted `\illegible{1}` | A long cancellation leaves no secure word. | low |
| 16 | 20, overlapping text before “arcs de grand cercle” | Deleted `\illegible{2}` | Two estimated words in a heavily overwritten interlinear revision; segmentation is insecure. | low |
| 16 | 20–21, cancelled parenthesis | “avec les bouts en P” | “les deux bouts en P”; the first two words are crossed through. | low |
| 16 | 20, surviving interlinear revision | “chemins de” | The final “de” is doubtful. Together with the surviving “de P” on the next line this yields a duplicated “de”; no grammatical correction has been made. | low |
| 16 | 21, overwritten material before `g_iP` | Deleted `\illegible{1}` | The cancelled item is not recoverable. | low |
| 16 | 21, immediately after `g_iP` | Deleted `\illegible{1}` | A short overdrawn mark may be an abandoned arrow or word. | low |
| 16 | 21, cancelled bottom line | “respectivement” | No secure alternative; a strike crosses most letters. The line ends “l'excep-” and continues on the next scan. | low |
| 17 | 1, deleted continuation | `tion du dernier` | `tion des derniers`; the initial `tion` continues the cancelled `l'excep-` on scan 16 and is not the beginning of `l'un` | medium |
| 17 | 1, deleted continuation | `ne rencontrent` | The final verbal stroke could be read as `-ant`; `rencontrant` is possible from this line alone | medium |
| 17 | 1, deleted continuation | `graphe` | Letter sequence is compressed and partly intersected by the large cancelling stroke | medium |
| 17 | 2, deleted prose | `du double triangle sphérique` | `des doubles triangles sphériques`; the article and plural endings are not secure | medium |
| 17 | 3, deleted prose | `le dernier le rencontrant` | Final verbal ending is less clear than the stem | medium |
| 17 | Above line 3, within deleted prose | `seult` | `seuls` or a more compressed form of `seulement`; the word is visibly added above the line | low |
| 17 | 7, deleted equation | `f(z)=-j` | `f(z)=-\bar j`; the potential bar is not securely distinct from nearby ink | medium |
| 17 | 9, first triangle in deleted list | `(1/2,-\bar j,1)` | First two entries are overwritten; their exact earlier state is unrecoverable | medium |
| 17 | Upper sphere, path labels | `\lambda_0,\lambda_1,\lambda_\infty` | Some subscripts cannot be isolated confidently from crossing arcs | low |
| 17 | Upper sphere, pole-to-interior path | `\ell` | The small label could be a neighbouring stroke rather than an independent letter | low |
| 17 | Upper sphere, small upper labels | `\lambda'_1,\lambda'_\infty` and two unread labels | Exact primes/subscripts and two additional labels remain unresolved | low |
| 17 | 10, immediately above general path formula | `donnés` | The ending is faint and the antecedent lies across earlier corrections | medium |
| 17 | 11, general path formula | `g_i` after an overwritten/deleted group of ink | Original symbol and precise nature of its overwritten accent cannot be recovered | low |
| 17 | 11, argument in general path formula | `\ell^{-1}` | `\ell'`; the tiny upper marks cannot securely be separated | low |
| 17 | Below first lower formula | `symétrie p.r. à l'équateur` | `l'équateur` is split over two written lines; the heavy horizontal stroke has been represented as doubtful underlining, but cancellation is also possible | low |
| 17 | Above first homotopy statement | One deleted word | No secure reading of the small isolated cancelled word | low |
| 17 | Below second lower formula | `p.r. à` | The abbreviation's second letter and the small following preposition are compressed | medium |
| 17 | Third homotopy statement | Deleted two-word passage replaced by `arc de` | The underlying wording is unreadable; deletion count estimated | low |
| 18 | 1, reference following `[C]` | Deleted `(13)` | Deleted `(43)` is also possible; cancellation obscures the first digit | low |
| 18 | 2, `p. 7` reference | `ff` | A handwritten capital `H`; no terminal full stop is securely visible | low |
| 18 | About 13, before the reference to formula (13) | `or on a` | Three very faint word traces; wording not fully recoverable letter by letter | low |
| 18 | Preliminary calculation of `\ell'_1` | `\sigma_\infty` | The initial Greek symbol is heavily retouched, with a descending stroke unlike the clearer repetition in (24) | low |
| 18 | (25), middle relation | Subscript `1` in `\ell'_1` | Overwritten index could visually be `\infty`; the reading is explicitly doubtful even though the surrounding equations suggest `1` | low |
| 18 | Diagonal margin, ambient group | `U_{0,3}^{an}` | Small raised qualifier is not fully resolved | medium |
| 18 | Diagonal margin, ambient group | `\mathfrak S_3` | Precise alphabet of the large stylized group letter is uncertain | medium |
| 18 | Diagonal margin, ambient group | `\mathbf Z/2` | `\mathbb Z/2`; handwritten double strokes do not distinguish the intended typeface securely | medium |
| 18 | Diagonal margin, expansion of `\sigma_0` | Final factors `\tau'_1\tau'_0` | Factors lie at the sloping paper edge; the last subscript is partly clipped | low |
| 18 | Diagonal margin, expansion of `\ell_1` | Final factor `\tau'_0` | Partly clipped at the sloping edge | low |
| 18 | Bottom of diagonal margin, `\varepsilon_0` line | Deleted three mathematical units; replacement `\tau'_\infty\tau'_1` | Multiple layers of overwriting; the reading and replacement/deletion boundary are uncertain | low |
| 18 | Bottom of diagonal margin, `\varepsilon_\infty` line | Last factor `\tau'` with unreadable subscript | Subscript is lost at the scan edge; no value supplied from the algebra | low |
| 19 | Opening, l. 1 | `encore` | A severely abbreviated or compressed adverb; no second reading sufficiently secure | medium |
| 19 | Opening, l. 1 | `les relations` | `la relation`; the plural endings are weak | medium |
| 19 | First formula, l. 2 | `\mathfrak{G}_{0,3}` | The letter is strongly inked and ornamented; its exact alphabet is not fully secure | medium |
| 19 | Annotation beneath first formula | `groupe` | The fast stroke may be an abbreviation; the parenthesis opening is faint | medium |
| 19 | Same annotation, second line | `graphique`, after `carto-` | Faint word ending; line-end hyphen is retained in the fragment | medium |
| 19 | Annotation under group symbol | `\mathrm{Aut}_{\mathrm{loc}}` | `\mathrm{Aut}_{\mathrm{ext}}`; `loc` fits the visible first long stroke better | medium |
| 19 | First `Gl(…,Z)'` on l. 2 | `2` | `1`; the digit is overwritten and is not regularized from the mathematics | low |
| 19 | After the first display, ca. l. 5 | `Rappelons` | Final letters are compressed | medium |
| 19 | Right end of (26), deletion | `agit` | One crossed-out word; a reliable alternative is unavailable | low |
| 19 | Just left of “sur le demi-plan” | `f` | Small isolated sloping glyph, possibly a reference/insertion mark rather than a letter; encoded as a marginal doubt | low |
| 19 | “demi-plan de …”, ca. l. 8 | `Poincaré` | Final accent and ending are faint | medium |
| 19 | Diagonal left NB, twice | `comp.` | Abbreviation likely, but full ending/period indistinct | medium |
| 19 | Diagonal left NB, before “l'image” | `est` | Very compressed connector; could be omitted in the author's syntax | low |
| 19 | Diagonal left NB, parenthesis | `ou` | First small word in the parenthesis is crowded | medium |
| 19 | Lower-left note near elliptic-curve paragraph | `équivalence` | `équivalences`; singular/plural ending unclear | medium |
| 19 | End of the same lower-left note | `\illegible{1}` | One short word or abbreviation after “de catégories”; not expanded | low |
| 19 | Penultimate main paragraph | `correspond` | Final strokes are weak | medium |
| 19 | Above “un générateur … de”, near bottom | `\eta` | Greek letter uncertain; its elevation and leading stroke suggest insertion above a caret | medium |
| 19 | Last word “rigidification” | No underline encoded | A long descending loop from the `g` resembles an underline, but does not clearly form independent emphasis | medium |
| 20 | Opening l. 1; repeated ca. l. 6 | `type` | Compressed word; earlier candidate readings included `fonct.` or a short noun, but none is secure | low |
| 20 | Opening, two occurrences of lattice symbol | `\pi` | `\Pi`; these small handwritten forms do not reliably distinguish case | medium |
| 20 | Equation `e_1\wedge e_2=…`, ca. l. 3 | `\eta` | Greek letter difficult, as at the end of scan 19 | medium |
| 20 | Insertion “comme base de V sur C” | `comme base`, attached to `L'élément e_1` | Wording is fairly clear; the exact attachment is less clear. It lies above the next-line `e_1`, rather than being silently made a property of the pair `(e_1,e_2)` | medium |
| 20 | End of normalization sentence, ca. l. 4 | `Ainsi,` | `Ainsi;`; punctuation indistinct | medium |
| 20 | “un élément e₂=τ de …”, ca. l. 7 | `\mathbb C` | `E`; the curved doubled letter is not silently corrected from the mathematical context | medium |
| 20 | Item 1°, first line | `engendrent` | `engendre`; the final stroke may be a `t` | medium |
| 20 | Item 1°, second line | `rg` | Ending resembles the familiar abbreviation, but may be a compressed full word | medium |
| 20 | Item 1°, following `rg` | `1` | The visible digit looks like `1`; mathematical expectation of rank two is kept out of the transcription | high |
| 20 | Item 2°, quoted adjective | `directe` | Final `e` not fully distinct | medium |
| 20 | Insertion before “des classes”, lower half | `l'ens` | Final letters/period unclear; no period silently added | medium |
| 20 | After “rigidifiées” | `ens.` | Small abbreviated word; possible different short connector | medium |
| 20 | Before final matrix | `que` | `pour`; the initial descending letter is ambiguous | medium |
| 20 | Final 2×2 matrix | Commas retained in both rows: `a,b` / `c,d` | Unlike the matrix in scan 19, small comma-like marks are visibly present | high |
| 20 | Last visible word | `corres-` | The word continues beyond the supplied page; final visible strokes and hyphen are faint. It has not been completed | medium |

## 3. Abbreviations and compact signs met

Expansions in this table are explanatory proposals confined to these notes. Uncertain source readings remain uncertain.

| As written | Scan(s) | Tentative expansion or meaning |
|---|---|---|
| `inv.` | 11 | invariant(e) |
| `Ob` | 11–12 | objets |
| `Rev` | 11–12 | revêtements, in the category notation |
| `rev` with raised `ts` (uncertain placement) | 11 | revêtements |
| `OPS` / `OFS` (uncertain) | 12 | Probably *on peut supposer* if the reading is `OPS`; no secure expansion is assigned to `OFS`. Independent rereading favours `OPS`. |
| `iso.` | 13 | isomorphisme |
| `sss` / `ssi` (uncertain) | 13 | Probably *si et seulement si*; the final letter is not securely dotted. |
| `ss-groupe` | 13 | sous-groupe |
| `m` with a bar (`\overline{\mathrm m}`) | 13–16 | même |
| `dfn` / `déf` above an equality (uncertain) | 13 | définition / par définition; the visible letters favour `dfn`. |
| `déf` above an equality | 19 | définition |
| `i.e`, `i.e.` | 12–20 | *id est*, c'est-à-dire; terminal punctuation follows the individual reading. |
| `NB`, `NB.` | 14, 16, 18–19 | *nota bene*; punctuation and underlining vary in the source. |
| `ens` (uncertain) | 15 | ensemble; a final period is not securely visible. |
| `l'ens`, `ens.` (uncertain) | 20 | l'ensemble, ensemble |
| `sup` | 15 | supérieur |
| `hémisph` (alternative reading) | 15 | hémisphère |
| `resp.` | 15–16 | respectivement; the margin occurrence on scan 16 is less secure. |
| Superscript `an` | 14–16, 18 | analytique / analytification; the tiny occurrence in scan 18's margin is doubtful. |
| `seult` (uncertain) | 17 | seulement; the alternative `seuls` would be a complete word. |
| `p.r.` (uncertain) | 17 | par rapport |
| `p.` | 18 | page |
| `ff` (uncertain) | 18 | following pages / et les pages suivantes; the mark could instead be a capital `H`. |
| `[C]` | 18 | Internal reference; the exact preceding text or section is not established from these scans. |
| `OK` | 18 | okay; retained in « Tout est OK ! » |
| `Aut` | 19 | automorphismes |
| `loc` (uncertain subscript) | 19 | Perhaps locaux / local; the convention is not defined here, and `ext` remains an alternative reading. |
| `GP` | 19–20 | groupe projectif; the page gives a quotient by scalar matrices. |
| `Gl` | 19 | groupe linéaire général |
| `Sl` | 19–20 | groupe spécial linéaire |
| `comp.` (uncertain) | 19 | composante(s) |
| `dim` | 19 | dimension |
| `rg` | 19–20 | rang; the occurrence on scan 20 is faint. |
| `ell.` | 20 | elliptique(s) |

The line-broken `carto-` / `graphique` on scan 19 is not an abbreviation. No expansion is assigned to the illegible final word of that page's small categorical note.

## 4. Legibility and limitations

The main statements, many displayed formulas, and the rational function are substantially more legible than the compressed prose, tiny subscripts, and later additions. The clearer formulas should still be read together with their local doubt marks. Independent rereading was used for difficult passages, including the initial stabilizer hypothesis, the inserted reduction on scan 12, the path description on scan 13, and the final elliptic-curve discussion.

The least secure passages are the overwritten stabilizer sentence on scan 11; the overlapping reduction on scan 12; the stray underlined glyph before the powered meridian on scan 13; the small arrows and hemispherical gloss on scans 14–15; and the multiply revised final lines of scan 16. Scan 17's cancelled paragraph and small labels in the spherical drawings remain difficult. Rotating scan 18's diagonal margin makes most of its calculation readable, but its lowest identities contain overwriting and clipping that enlargement cannot recover. On scans 19–20, the ornamented group symbol, the `Aut` subscript, the small categorical note, and the repeated word provisionally read *type* deserve particular caution.

Several apparently surprising features have been retained: the large script group letter in scan 13's « l'image de … »; the mismatch between scan 16's inserted endpoint formulas and the subsequent indexed pairs; the doubtful duplicated *de* in its final revision; and the visible rank **1** on scan 20. None of these observations establishes whether the manuscript contains a slip, a changed convention, or an unresolved reading. The final word on scan 20 remains unfinished. The table records uncertainty about readings and page state; it is not a claim that every unmarked stroke is beyond possible rereading.

## 5. Research notes — English, separate from the transcription

These notes refer to the supplied manuscript (Grothendieck, 1981). Their scan-and-location labels provide the pinpoint references for quotations. They identify claims, possible implications, and proposed checks; they do not supply missing words to the transcription. Quotations inherit the uncertainty attached to their source readings. Ideas attributed to the transcriber are labelled **own idea**, with confidence and reasons.

No explicit new conjecture or open-ended research question was securely identified in the legible passages of these ten scans. The author's stated programme includes « Je voudrais … expliciter … relations », the proposed normalized inverse-image construction, and several instructions to verify calculations. Unreadable and clipped marginal material limits any claim about absence.

1. **Scan 11, stabilizer hypothesis — own idea.** The requirement that stabilizers act « fidèlement au voisinage de x, en conservant l'orientation locale en x » invites a local-model check before using the quotient construction. A possible test is to analyze a disk with a finite cyclic rotation group and compare local degrees upstairs and downstairs; confidence: high that this is a useful test, because the next formula explicitly multiplies the signature by the stabilizer order, not that every needed local hypothesis has already been proved here.

2. **Scan 11, signature formula — unpursued implication.** The displayed rule multiplying `d_X(x)` by the local factor `[G_x]` suggests that one must establish independence of the chosen lift `x`; the written subscript on `ν` is uncertain. A proof would need compatibility of the signature with the group action and conjugacy of the relevant stabilizers.

3. **Scan 12, items (a)–(c), formula (19) — unproved claim.** « Ce foncteur est une équivalence de catégories. » The pages here state the quotient construction and its equivalence without supplying a complete argument for descent of objects and morphisms; a proof would need to check the local ramification bounds as well as the equivariant structure.

4. **Scan 12, item (d) — unproved claim.** « Description d'un foncteur quasi-inverse par image inverse “normalisée”. » This specifies the proposed inverse construction but gives no construction or unit/counit verification on this page. A proof would need a precise meaning of normalization in the category being used and a local calculation after pullback.

5. **Scan 12, reduction remark — unproved claim.** The suggestion to replace `X` by `X\setminus S` when `d_X=0`, and the interlinear simplification of points with signature one and trivial stabilizer, are asserted without detail. One would need to make explicit the convention encoded by zero and one in the covering category before proving that these replacements preserve it; the cramped insertion is an uncertain transcription.

6. **Scan 12, formula (20) — unpursued implication.** In the indicated special case the ramified quotient category is represented by an ordinary equivariant covering category upstairs: the author writes « sans donnée de ramification ». It would be useful to determine exactly which information remains in the group action and which disappears from the explicit signature; this note does not extend the asserted equivalence beyond its written hypotheses.

7. **Scan 13, corollary (21) — unproved claim.** « on a un iso. canonique » is stated as the consequence of the preceding equivalence. A proof would need to show compatibility of that equivalence with the fibre functors at `x` and its image `y`, since equivalence of categories alone does not specify the displayed based isomorphism.

8. **Scan 13, description of `(γ,ℓ)` — unproved claim.** The description of a group element by `γ∈G` and a path from `x` to `γ⁻¹x` is followed by an equivalence relation using the kernel of the punctured-surface map. A complete verification would require the product convention and a proof that the path relation is respected by it; no product formula is supplied on this page.

9. **Scan 13, kernel paragraph — unproved claim.** The kernel is described as the invariant subgroup « engendré par les » powers `λ_a^{d_X(a)}`. A proof would require the local monodromy relation and a global gluing argument; the extra tiny glyph before the power is not confidently read and must not be treated as a new mathematical factor.

10. **Scan 13, final map `f_U` — own idea.** The based comparison could be checked first on a punctured disk quotient, following a path and its image and measuring how often the image winds around the puncture. Confidence: high that this is a useful diagnostic, because it directly tests the exponent and inverse conventions used on the next page; no general theorem is claimed by this observation.

11. **Scan 14, lines 5–12 — unproved claim.** “On voit tout de suite” introduces the assertion that equivalent pairs `(γ,ℓ)` induce the same element on the quotient side. The stated mechanism is the image of a small meridian under the ramified quotient, followed by the exponent identity `d_X(a)ν(a)=d_Y(b)`. A careful proof should track the normal subgroups generated by these powered meridians and specify basepath/conjugacy choices, since a small meridian based at a distant point is not uniquely chosen.

12. **Scan 14, lines 10–12 — unpursued implication.** The formula “degré de ramification” together with the displayed multiplication of exponents suggests an explicit local compatibility condition for descent of ramified covering data. It would be useful to formulate precisely which divisibility conditions on local ramification indices this argument uses, and whether the same local calculation proves both existence and uniqueness in the inverse construction. This is an implication to investigate, not an asserted extension of the manuscript.

13. **Scan 14, bottom formula — own idea.** **Confidence: high as a verification strategy.** The rational map written here can be checked directly by differentiating it and factoring the numerators of `f`, `f−1`, and the denominator, then comparing the resulting multiplicities with the marked sets on the page. This would provide a concrete check on the ramification bookkeeping without relying on the later group identifications; no result of that calculation has been used to alter a symbol in the transcription.

14. **Scan 15, lines 6–13 — unproved claim.** The page says that the six inverse images include “trois dans l'hémisphère nord,” that these are permuted transitively by `ρ`, and that the stated spherical triangles map “homéomorphiquement.” A proof would need the precise spherical realization, the action of `ρ`, and control of the rational map on the edges and interiors of these triangles. The three assertions are related but logically distinct.

15. **Scan 15, lines 14–17 — unpursued implication.** “j'ai envie de prendre” selects the segment `(0,1/2)` and its associated triangle. The other two choices are not analysed on this page; tracking the induced changes of basepoint and generators would clarify which subsequent formulas are literal equalities for this selection and which are determined only up to conjugation.

16. **Scan 15, lines 18–22 — unproved claim.** The generators “s'obtiennent en prenant des chemins” joining the two poles through three specified equatorial points. To justify that these paths yield the intended involutory generators, one should compute their products with the conjugate/reflected paths and identify the resulting homotopy classes. Their involutivity is stated in the added adjective, not proved in this paragraph.

17. **Scan 16, lines 1–6 and left margin — unproved claim.** The lifts are said to cross the barycentric subdivision “en exactement un point,” with the endpoints characterized by membership in specified triangles. A proof requires a precise lifting argument and a check that no additional subdivision edges are crossed. The diagonal margin appears to refine the endpoint characterization and should be considered with the main argument rather than treated as decorative annotation.

18. **Scan 16, lines 7–13 — own idea.** **Confidence: medium, because several dotted symbols and corrections are difficult.** Compare the endpoint identities for `g_i` with the later pair representations of `τ'_i` before attempting to deduce a presentation. A small table recording each source path, its endpoint, the acting element, and the corresponding quotient generator could distinguish a deliberate relabelling from an unfinished correction; the apparent mismatch itself is not enough to establish an error.

19. **Scan 16, lines 14–21 — unproved claim.** “Nous allons utiliser l'arc de grand cercle” proposes a change of basepoint, followed by “On peut alors prendre.” An explicit verification should state the convention for composing paths and derive the transformed path for each acting group element. The corrected direction of the basepath and the rewritten description of `λ'_i` are important evidence for that calculation; the badly cancelled final wording should not be used as a secure formula.

20. **Scan 16, final cancelled sentence — own idea.** **Confidence: low as an interpretation, high as an editorial caution.** The abandoned description by great-circle arcs may have been replaced because the transported paths are better specified by their homotopy classes. Compare the continuation on the next scan before drawing that conclusion: the revisions could instead be changing only endpoints or the treatment of the final path. This is a possible explanation of the revision, not a claim about Grothendieck's intent.

21. **Scan 17, three lower path statements — unproved claim.** The first two changed-basepoint paths are each said to be “homotope au lacet trivial,” while the third is represented by an arc of the indicated great circle. The drawings suggest the geometric argument, but an explicit proof would need homotopies that avoid every deleted point of the surface and respect both endpoints. The cancelled upper description should be treated as a discarded working argument, rather than silently used as part of the surviving proof.

22. **Scan 18, (23) and the sentence immediately following — unproved claim.** Grothendieck writes “les quatre premières sont claires” for the involution and commuting-product relations. Their verification requires tracking the precise lifted reflections and the earlier definitions; the remaining relation is reduced on this page to a formula cited from `[C]`, formula (13). The page therefore supplies a reduction of the verification, not an independently complete proof of all the inputs.

23. **Scan 18, (24)–(25) — unproved claim.** If “les relations caractéristiques” is intended as a full presentation, the claim is stronger than the assertion that the displayed elements satisfy these relations. That interpretation would require generation and the absence of additional relations, in addition to checking the three identities in (25). The page closes with “Tout est OK !” without explicitly separating these possible senses of the phrase.

24. **Scan 18, diagonal margin — unpursued implication.** The statement “On exprime les éléments remarquables” is followed by explicit words in the primed involutions. These formulas permit a systematic comparison of the two generator systems and of the corresponding peripheral elements. Such a comparison depends on the precise order of factors; it should not use the mathematically expected order to repair the clipped or overwritten source.

25. **Scan 18, (23)–(25) — own idea; confidence: medium.** Compare the involution presentation with the presentation obtained for its subgroup of even words, using a direct rewriting argument. This may separate the verification of individual relations from the completeness of the claimed peripheral presentation and clarify which earlier geometric facts are indispensable. The confidence concerns the usefulness of this check, not a claim that it yields a new result or that every needed hypothesis is already present here.

26. **Scan 17, lower formulas, and scan 18, lowest marginal identities — own idea; confidence: medium.** A subsequent critical edition could independently verify the readable word identities algebraically while retaining the diplomatic text unchanged. Agreement would help prioritize rereading of individual glyphs, but it would not license replacing an unreadable index: an apparent algebraic disagreement could equally represent a genuine manuscript error or a different convention. This is a proposed verification workflow, not evidence for any particular disputed reading.

27. **Scan 19, opening and first formula — unproved claim.** The proposed comparison is introduced by “Je voudrais … expliciter … relations” with `GP(1,Z)`. These two pages begin an explanation, but do not complete a generator-and-relation identification of the ornamented group in the first formula with the projective integral group; a full account would first need the exact group notation and automorphism subscript to be established from the surrounding manuscript.

28. **Scan 19, (26)–(28) and following sentence — unproved claim.** The assertion “est isomorphe au groupe des automorphismes conformes de D” is given after the determinant-dependent formula. A proof should check preservation of the upper half-plane, composition in both determinant signs, the scalar kernel, and surjectivity onto the intended automorphism group. The conjugate branch makes the precise scope of “conformes” worth checking: the formula suggests that orientation reversal is included here.

29. **Scan 19, diagonal NB — unproved claim.** The note says that `GP(1,R)` “a deux comp. connexes” and identifies the neutral component with a quotient of `Sl(2,R)`. A proof would need to show that the determinant-sign map descends through the scalar quotient, that its two fibers are connected, and that the stated special-linear image is the positive component.

30. **Scan 19, final paragraph and lower-left note — unproved claim.** The claim that an elliptic curve over the complex numbers “équivaut à celle d'un espace V” with a lattice requires the analytic uniformization step and, for the marginal “équivalence de catégories”, a specification of morphisms. The final word of that marginal note is illegible, so no claim about a further qualifier such as canonicity is attributed to the author.

31. **Scan 19, (28), together with scan 20's positive orientation — own idea.** Compare the negative-determinant branch with changing a marking after conjugating the complex line and its lattice, and test whether this gives the intended extension from the positive projective group to the full group. **Confidence: medium**; the two branches and the orientation condition are explicit, but the exact moduli interpretation and allowed isomorphisms are not fixed on these pages.

32. **Scan 20, normalization to `e_1=1` and the two conditions — unpursued implication.** The text passes from a rigidification to a parameter with “τ∈D”. Beyond the coordinate calculation, a precise moduli statement would need to explain whether this parametrizes actual marked objects, isomorphism classes of marked objects, or an equivalence of categories, and to keep track of any automorphisms of the data.

33. **Scan 20, item 1°, “de rg 1” — own idea.** Check the visible rank-one wording against the simultaneous condition that the imaginary part of τ is nonzero: then 1 and τ are linearly independent over the real numbers, so their integer span has rank two. **Confidence: high for this algebraic check**; it follows directly from separating real and imaginary parts of an integer relation. The transcription preserves the apparent `1`, and this observation does not establish whether the source contains a slip or a difficult digit.

34. **Scan 20, final fractional-linear action — unproved claim.** After “on trouve”, the action of the displayed matrix is stated as τ↦(aτ+b)/(cτ+d). A proof should explicitly specify how the matrix changes the ordered basis and whether the action is on markings or on their inverses; otherwise a transpose or inverse can enter while leaving an apparently familiar formula. The visible commas inside the matrix and the author's chosen formula have not been normalized.

35. **Scan 20, last two lines — unproved claim.** “Ce groupe opère proprement” and “exactement deux trajectoires critiques” are asserted before the sentence continues off the supplied page. A proof would require a properness argument and a classification of the nontrivial stabilizers up to orbit, for example from a fundamental domain. The two trajectories are not named in the provided continuation, and no names are supplied in the transcription.

36. **Scan 20, quotient `Sl(2,Z)' ≃ GP(1,Z)^+` — own idea.** Track the central sign separately when comparing the effective action on D with the preceding geometric data. **Confidence: medium**; the prime quotient and the positive projective group are visible, but the exact rigidification convention is partly uncertain. This check could clarify whether an effective orbit space and a quotient retaining automorphisms are being distinguished later in the manuscript.

## Source reference

Grothendieck, A. (1981). *La Longue Marche à travers la théorie de Galois* [Unpublished manuscript; supplied scans 11–20 of the Montpellier archive file, cote 140-3, described as pages 293–650]. Université de Montpellier.

The attribution, date, title, and archival file description above are supplied by `LM_P060_prompt.md`. The visible folio and image numbers are recorded separately in Section 1. No bibliographic claim about an external edition is made.

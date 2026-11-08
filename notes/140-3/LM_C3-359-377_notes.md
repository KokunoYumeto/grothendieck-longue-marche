# LM_C3-359-377 — Editorial and research notes

## 1. Source, scope, and transcription conventions

This edition transcribes the 19 supplied image files `LM_C3-359-377_scan359.jpg` through `LM_C3-359-377_scan377.jpg`. The identification and date follow the supplied task description: Alexander Grothendieck, *La Longue Marche à travers la théorie de Galois* (1981), Montpellier archive cote 140-3. The images are the sole source of the transcription. No published transcription or external reconstruction was used.

The scan numbers follow the filenames, not the lower number printed or handwritten on each sheet. Both visible handwritten numberings are preserved with `\mspage`, including the isolated upper **4** on scan 363. Equation labels, repeated labels, abbreviated words, changing superscripts, unfinished formulas, and incomplete sentences have not been regularized. The printed institutional imprint outside the black manuscript frame is copied into TeX comments at the end of each scan, and appears as a separate inventory element; it is not attributed to the manuscript's author.

| Scan / filename suffix | Visible handwritten number(s), in reading order |
|---:|---|
| 359 | 358 |
| 360 | 481, 359 |
| 361 | 360 |
| 362 | 482, 361 |
| 363 | 4, 362 |
| 364 | 483, 363 |
| 365 | 364 |
| 366 | 484, 365 |
| 367 | 366 |
| 368 | 485, 367 |
| 369 | 368 |
| 370 | 486, 369 |
| 371 | 370 |
| 372 | 487, 371 |
| 373 | 372 |
| 374 | 488, 373 |
| 375 | 374 |
| 376 | 489, 375 |
| 377 | 376 |

The LaTeX deliverable is a fragment, beginning with `\scanpage{359}`, with no preamble or macro definitions. It uses the requested editorial macros plus ordinary LaTeX/AMS mathematical commands and `tikz-cd`. The receiving document must define the editorial macros and load its preferred mathematical, underline, and diagram packages. Mathematical underlines are encoded with `\underline`; underlined prose uses `\uline` or `\uuline`. These are transcription choices for the visible marks, not corrections of the notation.

## 2. Table of doubts

The entries below locate the explicit doubt marks in the fragment. Approximate line counts are local to the handwritten page, not the line numbers in the `.tex` file; displayed equation numbers and physical positions disambiguate them. A proposed reading is not established by its mathematical plausibility. Where no second reading is supported, none is invented. Some tables group repeated instances of an identical doubtful glyph within a single formula, explicitly identifying those occurrences.

### Scans 359–363

Line numbers count approximate handwritten lines within the manuscript image, excluding the institutional footer. Repeated instances are listed separately. Proposed mathematical readings use the same LaTeX spelling as the fragment. A dash in the alternatives column means that the image did not support a second definite reading, not that the proposed reading is certain.

| ID | Scan | Approximate manuscript line / position | Proposed reading | Alternatives | Confidence |
|---|---:|---|---|---|---|
| 359-U01 | 359 | l. 4, cancelled symbol after «pour que» | `$\lambda$` | No alternative established from the image | low |
| 359-U02 | 359 | l. 5, insertion above unipotence adjective | `str\textsuperscript{t}` | No alternative established from the image | medium |
| 359-U03 | 359 | l. 5, abbreviated adjective after «encore» | `unip.\textsuperscript{t}` | No alternative established from the image | medium |
| 359-U04 | 359 | ll. 7–8, cancelled phrase below insertion | `c'est évident` | No alternative established from the image | low |
| 359-U05 | 359 | ll. 9–10, cancelled phrase before «de cette hypothèse» | `dans le cas` | No alternative established from the image | low |
| 359-U06 | 359 | l. 11, cancelled word after «car. 2» | `quitte` | No alternative established from the image | low |
| 359-U07 | 359 | l. 16, displayed equation number | `45` | `46` | medium |
| 359-U08 | 359 | l. 18, noun/adjective after «soit» | `injection` | `injective` | medium |
| 359-U09 | 359 | l. 23, cancelled word before ring presentation | `sur` | No alternative established from the image | low |
| 359-U10 | 359 | l. 24, last generator of displayed ideal | `S` | No alternative established from the image | medium |
| 359-U11 | 359 | l. 27, cancelled beginning of spectrum formula | `$\mu'_2\simeq$` | No alternative established from the image | low |
| 359-U12 | 359 | l. 28, overwritten symbol in direct sum | `\varepsilon` | No alternative established from the image | low |
| 360-U01 | 360 | l. 2, small parenthetical insertion above «de G» | `(ou non)` | No alternative established from the image | low |
| 360-U02 | 360 | l. 5, word before «des Borels» | `suite` | No alternative established from the image | medium |
| 360-U03 | 360 | diagram (48), far-left black mark | `1` | No alternative established from the image | medium |
| 360-U04 | 360 | diagram (48), left vertical arrow decoration | `\wr` | `?` | low |
| 360-U05 | 360 | diagram (48), right vertical arrow decoration | `\wr` | `?` | low |
| 360-U06 | 360 | diagram (48), cancelled character before B tilde | `B` | No alternative established from the image | low |
| 360-U07 | 360 | diagram (48), overwritten beginning of unipotent label | `\mathrm U` | No alternative established from the image | low |
| 360-U08 | 360 | diagram (48), small label below lower-left object | `c.à.d.` | No alternative established from the image | low |
| 360-U09 | 360 | l. 14, abbreviation after «car» | `rés.` | No alternative established from the image | medium |
| 360-U10 | 360 | l. 18, punctuation after B_u tilde | `,` | `»` | medium |
| 360-U11 | 360 | l. 18, cancelled word after «j’ai» | `fait` | No alternative established from the image | low |
| 360-U12 | 360 | l. 19, underlined word before «vérifié» | `déjà` | No alternative established from the image | medium |
| 360-U13 | 360 | l. 23, abbreviated word before «en droites» | `ssfibrés` | No alternative established from the image | medium |
| 361-U01 | 361 | l. 1, phrase before «point dans PG» | `ce même` | No alternative established from the image | medium |
| 361-U02 | 361 | l. 5, overwritten quantifier after «du fait» | `qu'une` | `qu'aucune` | low |
| 361-U03 | 361 | ll. 5–6, unipotence adjective and ending | `unipotente régulière` | No alternative established from the image | medium |
| 361-U04 | 361 | ll. 9–10, adjective after «section epsilon de» | `unipotents réguliers` | `unipotente régulière` | medium |
| 361-U05 | 361 | l. 13, verb after «On» | `notera` | No alternative established from the image | medium |
| 361-U06 | 361 | l. 17, coefficient in formula for N prime | `1+\nu` | No alternative established from the image | medium |
| 361-U07 | 361 | l. 20, cancelled phrase before «les hom.» | `on a alors` | No alternative established from the image | low |
| 361-U08 | 361 | l. 22, source subscript in composite diagram | `a` | `0` | medium |
| 361-U09 | 361 | l. 23, cancelled word before «associés» | `seront` | No alternative established from the image | low |
| 361-U10 | 361 | l. 23, verb before «distincts» | `seront` | `sont` | medium |
| 361-U11 | 361 | l. 24, two horizontal strokes before «valeur» | `=` | `\overline{\mathrm m}` | medium |
| 361-U12 | 361 | l. 25, cancelled phrase after «En effet» | `on aura` | No alternative established from the image | low |
| 361-U13 | 361 | l. 27, overtraced relation before quotient designation | `=` | `\simeq` | medium |
| 361-U14 | 361 | l. 27, final quotient designation: descending g-shaped letter | `\mathfrak g` | No alternative established from the image | medium |
| 362-U01 | 362 | l. 5, bundle designation after «section de»: descending g-shaped letter | `\mathfrak g` | No alternative established from the image | medium |
| 362-U02 | 362 | l. 13, source of cancelled diagram | `a` | `0` | low |
| 362-U03 | 362 | l. 13, label of cancelled diagram | `\widetilde{\underline\varepsilon}_0` | No alternative established from the image | low |
| 362-U04 | 362 | l. 14, first source subscript in (49) | `a` | `0` | medium |
| 362-U05 | 362 | l. 15, second source subscript in (49) | `a` | `0` | medium |
| 362-U06 | 362 | l. 18, first argument in second line of (50) | `t` | `u` | medium |
| 362-U07 | 362 | l. 18, middle argument in second line of (50) | `t` | `u` | medium |
| 362-U08 | 362 | l. 18, final argument in second line of (50) | `t` | `u` | medium |
| 362-U09 | 362 | l. 20, overwritten article before «relèvement» | `un` | No alternative established from the image | low |
| 362-U10 | 362 | l. 20, right-hand insertion | `unip.\textsuperscript{t}` | No alternative established from the image | medium |
| 362-U11 | 362 | l. 21, cancelled word before «le choix» | `qui` | `que` | low |
| 362-U12 | 362 | l. 21, before «priori» | `à` | No alternative established from the image | medium |
| 362-U13 | 362 | l. 23, false start before final epsilon_1 formula | `\rho` | No alternative established from the image | low |
| 362-U14 | 362 | lower-left diagonal margin, cancelled expression beginning int / i.e. | `\operatorname{int}(\varepsilon_0)` | `\mathrm{i.e.}\,\sigma(\varepsilon_0)` | low |
| 362-U15 | 362 | lower-left diagonal margin, final cancelled glyphs | `\varepsilon_0` | No alternative established from the image | low |
| 362-U16 | 362 | lower-left diagonal margin, last formula | `\sigma(\varepsilon_0)` | `\sigma^{-1}(\varepsilon_0)` | low |
| 362-U17 | 362 | lower-left diagonal margin, two terminal strokes (possibly emphasis) | `=` | No alternative established from the image | low |
| 363-U01 | 363 | l. 1, cancelled opening | `Et` | No alternative established from the image | low |
| 363-U02 | 363 | l. 1, cancelled word below «description» | `précision` | `position` | low |
| 363-U03 | 363 | l. 2, cancelled word after «pour» | `ensuite` | No alternative established from the image | low |
| 363-U04 | 363 | l. 5, sign/word before «1-paramètre» | `à` | No alternative established from the image | medium |
| 363-U05 | 363 | l. 7, source subscript in homomorphism display | `a` | `0` | medium |
| 363-U06 | 363 | l. 7, terminal decoration of horizontal line | `\longrightarrow` | `\text{---}` | low |
| 363-U07 | 363 | l. 8, small mark after «ait» | `$\times$` | `$*$` | low |
| 363-U08 | 363 | l. 14, parenthetical phrase in item 1 | ```Pour mémoire''` | No alternative established from the image | low |
| 363-U09 | 363 | l. 15, cancelled word before inserted «unipotentes» | `str\textsuperscript{t}` | No alternative established from the image | low |
| 363-U10 | 363 | l. 16, overwritten term before 1+N_i | `\mathrm{Id}+` | No alternative established from the image | low |
| 363-U11 | 363 | l. 20, dot above initial epsilon_1 in (54) | `\dot{\varepsilon}_1` | `\varepsilon_1` | medium |
| 363-U12 | 363 | l. 21, initial overwritten symbol in cancelled (55) | `\rho` | No alternative established from the image | low |
| 363-U13 | 363 | l. 24, introductory word of replacement item 3 | `Étant` | No alternative established from the image | medium |
| 363-U14 | 363 | l. 25, false start above second (55) | `\rho\sigma^{-1}\rho` | No alternative established from the image | low |
| 363-U15 | 363 | l. 30, cancelled word before «termes» | `fonction` | No alternative established from the image | low |
| 363-U16 | 363 | l. 30, possible connective before «inversement» | `et` | No alternative established from the image | medium |

### Scans 364–368

The approximate line numbers below count manuscript writing from the first body line, with each displayed formula counted as one line; interlinear writing is referred to the line to which it belongs. They do not count the archive's printed footer.

| Scan | Approx. line / position | Reading | Alternatives / reason for doubt | Confidence |
|---|---|---|---|---|
| 364 | 1 | `4)` | The numeral is dark and appears to be 4, but duplicates the following paragraph's numeral and may be an overwritten numeral. | medium |
| 364 | 2, (56) | `\sigma` | The symbol has an overwritten lower stroke; σ is the principal visible reading. | medium |
| 364 | 6 | `tte` | Abbreviated form before “fibre”; the small ending is not fully distinguishable. | low |
| 364 | 11, insertion | `fppf` | Lower-case `fppf` appears intended, but middle letters are very compressed. | medium |
| 364 | 18 | `et` | Dark, overwritten conjunction before “la normalisation”; it may have been partly cancelled. | low |
| 364 | 18 | `u` | `v_1`; the initial normalization parameter is not distinct enough to settle alphabet or a possible subscript. | low |
| 364 | 21, deletion | `l'échange se fait` | Cancelled line; “l'échange” is a tentative reading of a partly obliterated word. | low |
| 364 | 22, (58), first underbrace | `=` | A short upper stroke over the first minus may form an equality sign; the annotation may instead begin directly with `-\rho^{-1}\sigma`. | low |
| 364 | last line | `posant` | `prenant`; word is clipped at the right edge and the middle strokes are compressed. | low |
| 365 | 3, (61) | `\varepsilon_1^{-1}` | `\varepsilon_0^{-1}`; the index in the first relation is overwritten. | medium |
| 365 | 5 | `\sigma''` | Overwritten second summand in the inline trace formula. | medium |
| 365 | 7, (62) | `v` | `\nu`; the handwritten denominator does not determine the alphabet. | low |
| 365 | 8 | `v_1` | `u_1`; rounded initial stroke before the subscript 1. | low |
| 365 | 11 | `(A1)_2` | `(41)_2`; reference has overwritten first character and compressed final subscript. | low |
| 365 | 13 | `v_1` | `u_1`; the repeated normalization parameter. | low |
| 365 | 14 | `épinglage` | Middle letters of the underlined technical noun are contracted. | medium |
| 365 | 15 | `i.e.` | Abbreviation between the ordinary and projective pairs is dark and compressed. | low |
| 365 | 19, second matrix | `v_1/v` | `u_1/v`; the numerator's initial letter is rounded. | low |
| 365 | 22 | `épinglage` | Fast cursive middle letters. | medium |
| 365 | 22 | index `1` in `\varepsilon_1` | The index is darkened by overwriting. | medium |
| 365 | 23 | `offrait` | Ending is compressed; `offre` is a possible alternative. | medium |
| 365 | 24 | `épinglages` | Compressed technical noun, plural ending visible but slight. | medium |
| 365 | 24 | `naturels` | The letters under the quotation marks are faint; this is the best reading. | medium |
| 366 | 1, insertion | `correspondant` | Last strokes could include a final s; present-participle reading retained. | medium |
| 366 | 2, deletion | `ou` | Short cancelled connective is mostly covered by the deletion stroke. | low |
| 366 | 6 | `pérégrinations` | Inner letters are compressed; the word is not restored from its context. | medium |
| 366 | 10, deletion | `\varepsilon` | Small black overwritten symbol before `-\rho\sigma^{-1}`; any subscript is not separable. | low |
| 366 | 18 | `méritait` | Final cursive strokes are compressed. | medium |
| 366 | 23, inline product | index `0` in `\widetilde\varepsilon_0` | Index is merged with the lower body of ε. | medium |
| 366 | 23, inline product | `=` | The equality sign is overwritten; extra strokes may be cancellation remnants. | low |
| 366 | 24 | `\mathfrak S'_3` | `\mathcal G'_3`; the large handwritten group letter is not unambiguously distinguishable. | low |
| 366 | 25–26 | `qui` | Could appear as `quitte`; compressed connection before “à son tour.” | low |
| 367 | 3, deletion | `en appliquer à` | `en appliquant à`; deletion crosses the ending of the second word. | low |
| 367 | 6, arrow label | `\varphi` | `\psi`; upper curves and central stem are not wholly distinct. | medium |
| 367 | 11 | `\varphi` | Repetition of the homomorphism symbol; same alphabetic uncertainty as the arrow label. | medium |
| 367 | 19, deletion | `qui opère` | `qu'on a`; the cancellation stroke covers the connective almost throughout. | low |
| 367 | 21, deletion | `comme` | Baseline word is almost covered; above it, cancelled `par` and replacement `comme` remain visible. | low |
| 367 | 22 | subscript `lac` in `Aut` | `ext`; the subscript resembles “lac” but is very contracted. | medium |
| 367 | 22 | `\mathcal G_{0,3}` | `\mathbb G_{0,3}`; handwritten outline-like capital G does not settle the intended alphabet. | low |
| 367 | 24 | `le` | `ce`; small connective before “troisième facteur.” | medium |
| 367 | 24 | index `0` in `\ell'_0` | Index is filled in with dark ink. | medium |
| 367 | 25, deletion | `).` | Closing parenthesis appears cancelled or overwritten before the continuation; state of the punctuation is uncertain. | low |
| 367 | 26, deletion | `le` | `la`; small cancelled pronoun before “conserver.” | low |
| 368 | subtitle, deletion | `\mathcal G_{\rho,\sigma}^{*0}` | The superscript star and small circle are visible, but cancellation obscures most of the group letter and subscripts. | low |
| 368 | 8 | `pré-Borel` | `pri-Borel`; the short vowel and its mark are not distinct. | low |
| 368 | 10 | `centralisateurs` | `stabilisateurs`; the initial letters have been heavily retraced. | medium |
| 368 | (2), last coordinate | `\nu` | `\delta`; overwritten symbol, different in appearance from the later plain ν. | low |
| 368 | diagonal margin, line 1 | `maintenant` | Several inner letters are reduced to connecting strokes. | medium |
| 368 | diagonal margin, line 2 | `d'où` | `lié à`; the compressed letters immediately before `L_1` are uncertain. | medium |
| 368 | diagonal margin, final line | `(2)` | The numeral has very little visible upper contour. | medium |
| 368 | 17 | `du premier` | `des premiers`; the short connective and the final word ending are compressed. The apparent wording has not been made grammatically smoother. | low |
| 368 | 17 | `ds` | The short word after “premier” resembles this abbreviation; `dans` is another possible reading. | low |
| 368 | 19, insertion over deletion | `signifie` | Retraced letters partly overlap the cancelled “il faut et il suffit”; attachment and reading are tentative. | low |
| 368 | 22 | `\underline u` | `=`; the object after “simplifiant par” consists of two nearly horizontal strokes. | medium |
| 368 | penultimate line | `donnera` | `donnerait`; the last letter is reduced to a small pointed stroke. | medium |

### Scans 369–373

| Scan | Approximate line or location | Reading retained | Alternative or qualification | Confidence |
|---|---|---|---|---|
| 369 | 2, first deletion | `que` | First deleted word is compressed and overtraced. | medium |
| 369 | 2, after ρ | `aient`, deleted | Reading and exact extent of the strike are uncertain. | low |
| 369 | 2 | `act.` | Abbreviation for action; the final mark may be a superscript abbreviation stroke. | medium |
| 369 | 3 | `g.` | The abbreviation after « à » appears to be *gauche*. | medium |
| 369 | 3, deleted symbol after « par » | `L_1` | Subscript is obscured by the strike. | low |
| 369 | 4, deleted symbol after « sous-groupe » | `L_1` | Subscript and surviving lower strokes are overtraced. | low |
| 369 | Above 4 | `unip` with superscript `t` | Could be an abbreviated or very compressed *unipotent*; not expanded in the transcription. | medium |
| 369 | 11, deletion | `alors pour tout` | The middle letters are obscured by a horizontal strike. | low |
| 369 | 11, deleted formula at the inserted σ⁻¹ | `ρ(-)` | Parenthesis-like traces may belong to a superseded argument; the correction is crowded. | low |
| 369 | 15, after « déterminant » | `donc ablt` with superscript `n` | The abbreviation after *donc* is unresolved; possibly an abbreviation concerning abelianization. | low |
| 369 | Lower-left marginal note, opening | `(si` | The opening punctuation is intermingled with the main text. | low |
| 369 | Lower-left margin, after « régulier » | `i.e.` | Short letters touch the nearby main equation label. | medium |
| 369 | Lower-left margin, after ρ et σ | `ne sont homoth.` | Several internal letters are compressed; a homothety abbreviation is the best reading, not an established expansion. | low |
| 369 | Lower-left margin, next line | `en aucune fibre)` | The final parenthesis and some of the first word overlap main-text strokes. | low |
| 369 | Lower-left margin, apparent deletion | `détermine` | The word is heavily crossed and close to the main paragraph; its deletion extent is uncertain. | low |
| 369 | Lower-left margin, next phrase | `sur un corps, il y a une` | The short words after *corps* are the least secure part of this phrase. | low |
| 369 | Lower-left margin | `ambiguïté`, tentatively underlined | Main letters are recognizable. The apparent emphasis stroke could instead include the descending stroke of g; the underline remains uncertain. | low |
| 369 | Lower-left margin | `possible` | Final strokes are compressed. | low |
| 369 | Lower-left margin, before « deux » | `entre` | Alternative `d'ordre`; an independent rotated reading favors entre, but the connecting strokes remain faint. | medium |
| 369 | Lower-left margin, parenthesis | `deux`, underlined | The word after *les* is overtraced; the lower emphasis stroke is separately visible. | medium |
| 369 | Lower-left margin, last line | `l'élément en q.` | Ending and abbreviation at the foot are uncertain. | low |
| 369 | Right margin beside (5) | `𝔾_m` (`\mathbb G_m`) | The equality's right member is close to the edge; the multiplicative-group reading is most likely. | medium |
| 369 | Bottom deletion | `qu'on ait` | The words lie between the deletion line and the abandoned display. | low |
| 369 | Deleted (6), before B′₀ | `\rho` | A distinct loop and descending stroke support rho; the insertion is crowded against B. No parentheses are supplied. | medium |
| 369 | Deleted (6) | `=` after `T_σ ∩ ρ B'_0` | Only a terminal horizontal trace remains; the abandoned formula has no recoverable right member. | low |
| 370 | 6, deleted word before « l'on » | `il` | Heavily struck short word. | low |
| 370 | 11, deleted variable before ζ | `ν` with underline, followed by comma | It may be an initial ordering of the unknowns; the strike and underline cannot be completely separated. | low |
| 370 | 11 and (7), four occurrences | `ζ` | Alternative `ξ`; the hand uses an elongated descending form. | medium |
| 370 | 16, page reference | `435',436` | The middle digits could be read as 5 rather than 3 at normal scale; enlarged reading favors 3. | medium |
| 370 | 17, deleted word after « conditions » | `que` | Alternative `pour`. | low |
| 370 | (8b), overwritten symbol | Deleted `ρ`, replaced by `σ` | Lower traces resemble ρ, but the original letter is partly covered. | low |
| 370 | 24 | `des` | Alternative `de`; no grammatical normalization has been imposed. | medium |
| 371 | Above 1 | `assez` | Short added word is faint; the caret attaches it to « naturel ». | medium |
| 371 | 2, ε₀ definition | `σ^{-1}ρ` | Alternative `-σ^{-1}ρ`; no separate minus is secure in this overtraced opening. | low |
| 371 | 2 | `quasi-unipotent` | Final word might contain an abbreviation stroke rather than fully written letters. | medium |
| 371 | 3, deletion | `un par` | Both very short deleted words remain low-confidence. | low |
| 371 | (9), underlabel of first commutator | `ζ` | Alternative `ξ`; its long descending stroke extends toward the following prose. | medium |
| 371 | (9), underlabel of second commutator | `η` | Overtraced loop; η is supported by the subsequent condition on η. | medium |
| 371 | Right of (9), dark deletion | `ε` | The small cancelled glyph is almost entirely inked over. | low |
| 371 | 10, before « nous avons » | `on` | Alternative `où`; a short word is present, despite the awkward retained syntax. | low |
| 371 | (11), cancelled symbol after ε(b) | `σ` | The original symbol is largely obscured by cancellation. | low |
| 372 | 4 | `loc` with superscript `t` | The superscript abbreviation ending is faint. | medium |
| 372 | 10, after « transport de » | `structure` | Initial tall cursive stroke is unusual, but remaining letters support this reading. | medium |
| 372 | (12), and both appearances in (15) | Superscript `\flat` | Alternative literal `b`; the sign is repeatedly overtraced. Its order relative to `*` is preserved. | medium |
| 372 | 16, before deleted « notre » | `pour` | Extent of the cancellation through these two words is not fully clear. | medium |
| 372 | (14), right matrix delimiter | `}` | Alternative `)`; the handwritten right delimiter appears brace-like, unlike the left parenthesis. | low |
| 373 | (16), both appearances | Superscript `\flat` | Alternative literal `b`; same uncertain mark as in scan 372. | medium |
| 373 | (17), both exponents and parameter clause | `n` | Alternative `u`; all three related glyphs are retained with doubt. | medium |
| 373 | (18), after det α ∈ | `Γμ₂` | Dark overlapping strokes obscure the transition between Γ and μ₂. | medium |
| 373 | Right of (18), superscript on SG | `*` | Alternative `\flat`; the isolated dark mark differs from the clearly drawn star in the following line. | low |
| 373 | Added word below deleted « Soit donc » | `Rem.` | Abbreviation's interior letters are compressed. | medium |
| 373 | Deleted expression before SG | `ε' ← (α,β),` | Alternative `ε'(α,β),`; deletion obscures whether the intervening horizontal strokes were an arrow. | low |
| 373 | 19, « dont le … est automatique » | `premier` | Alternative `première`; the final stroke is too short to resolve confidently. | medium |

### Scans 374–377

Each occurrence of `\unsure` or `\illegible` in this four-scan fragment has its own row below, in transcription order. Locations refer to the handwritten page, using its displayed equation numbers where possible; scan numbers refer to the supplied filenames. The repeated b-shaped superscript is deliberately not normalized, and changes between it, a circle, a star, and their ordering remain in the transcription.

| Scan / occurrence | Approximate line or position | Reading | Alternative | Confidence | Basis of doubt |
|---|---|---|---|---|---|
| 374.1 | top, line 1, after qui | `montrent` | `No second reading proposed.` | medium | Verb ending is a light stroke. |
| 374.2 | top, line 3, parenthesis | `correspondant` | `No second reading proposed.` | medium | Compressed word and terminal strokes. |
| 374.3 | top, line 3, identity factors | `\{1\}\times\{1\}` | `\{(1,1)\}` | low | Overtraced braces and identity factors; the two written arrangements are difficult to separate. |
| 374.4 | top, line 4, deletion after où | `l'on a` | `No second reading proposed.` | low | Only parts of the crossed words survive. |
| 374.5 | after (21), produit ... direct | `\frac12` | `No second reading proposed.` | medium | The small fraction is read as the author’s shorthand for semi-. |
| 374.6 | (22), superscript on second group | `\flat` | `b` | low | Dark b-shaped superscript; flat-sign versus letter b unresolved. |
| 374.7 | (23), superscript on last group | `\flat` | `b` | low | Same unresolved b-shaped superscript. |
| 374.8 | below (23), crossed factor before T0 | `B'_0` | `No second reading proposed.` | low | Overwritten factor resembles B0 prime. |
| 374.9 | below (23), replacement first factor | `T_0` | `T'_0` | medium | A small prime cannot be separated securely from the preceding alteration. |
| 374.10 | (24), second group superscript | `\flat` | `b` | low | Same unresolved b-shaped superscript. |
| 374.11 | line after (24), second starred group | `\flat` | `b` | low | Same unresolved b-shaped superscript; order relative to the star retained. |
| 374.12 | after (24), déduit des descriptions | `déduit` | `déduits` | medium | Singular/plural terminal stroke is unresolved. |
| 374.13 | next line, parenthesized pair of factors | `T_0` | `T'_0` | medium | Prime on T0 remains unresolved. |
| 374.14 | (25), source group superscript | `\flat` | `b` | low | Same unresolved b-shaped superscript. |
| 374.15 | (25), first target factor | `T_0` | `T'_0` | medium | Prime on T0 remains unresolved. |
| 375.1 | first projection diagram, source group | `\flat` | `b` | low | Unresolved b-shaped superscript. |
| 375.2 | first projection diagram, vertical comparison of tuples | `\wr` | `\Vert` | medium | Wavy isomorphism sign versus parallel strokes. |
| 375.3 | after first projection, sur le ... | `ssgroupe` | `s/groupe` | medium | Written shorthand could be ssgroupe or s/groupe. |
| 375.4 | next line, before (21) | `défini` | `définis` | medium | Terminal s, if present, is not secure. |
| 375.5 | paragraph after (21), parenthesis | `déterminants` | `No second reading proposed.` | medium | Word broken over the physical line; strokes support déterminants. |
| 375.6 | determinant-character diagram, second arrow label | `\delta_\sigma` | `No second reading proposed.` | medium | Sigma subscript is overwritten; delta remains visible. |
| 375.7 | (22), source group superscript | `\flat` | `b` | low | Unresolved b-shaped superscript. |
| 376.1 | (23), kernel group superscript | `\flat` | `b` | low | Unresolved b-shaped superscript after star and circle. |
| 376.2 | (23), middle group superscript | `\flat` | `b` | low | Unresolved b-shaped superscript after star. |
| 376.3 | line immediately after (23), group superscript | `\circ\flat` | `\circ` | low | The small circle is visible; a second overtraced mark may also be present. |
| 376.4 | (25), first kernel factor superscript | `\flat` | `b` | low | Unresolved b-shaped superscript. |
| 376.4a | (25), separator between the two kernel factors | `\times` | No second reading established. | low | The small cross is crowded against the retraced initial S of the next factor; the multiplication sign is not independently clear. |
| 376.5 | (25), second kernel factor superscript | `\flat` | `b` | low | Unresolved b-shaped superscript. |
| 376.6 | (25), middle group superscript | `\flat` | `b` | low | Unresolved b-shaped superscript after circle. |
| 376.7 | (25), deleted beginning of parameter tuple | `(\underline{u},` | `\underline{u}` | low | Deleted u is visible; initial parenthesis and comma less secure. |
| 376.8 | (26), first definition, superscript | `\flat` | `b` | low | Unresolved b-shaped superscript. |
| 376.9 | (26), second definition, superscript | `\flat` | `b` | low | Unresolved b-shaped superscript. |
| 376.10 | paragraph after (26), insertion above rho | `non-s` | `non-g` | low | Short parenthesis reads approximately non-s or non-g; no expansion supplied in the transcription. |
| 376.11 | same paragraph, ST_rho superscript | `\flat` | `b` | low | Unresolved b-shaped superscript. |
| 376.12 | same paragraph, inserted dimension parenthesis | `dim 1` | `No second reading proposed.` | medium | Small letters and numeral are light. |
| 376.13 | next line, before pour sigma | `itou` | `No second reading proposed.` | medium | Compact word read as itou. |
| 376.14 | same line, deletion after Ainsi | `\illegible{1}` | `No reading recovered; one deleted word estimated.` | low | One crossed word/glyph remains physically unreadable after enlarged inspection. |
| 376.15 | after matrix display, ST_rho superscript | `\flat` | `b` | low | Unresolved b-shaped superscript. |
| 376.16 | next line, ST_sigma superscript | `\flat` | `b` | low | Unresolved b-shaped superscript. |
| 376.17 | next line, group before est un tore | `\flat` | `b` | low | Unresolved b-shaped superscript after circle. |
| 376.18 | last paragraph, group after en termes de | `\circ` | `No second reading proposed.` | medium | Tiny open superscript is read as circle; no flat-like mark supplied here. |
| 377.1 | top line, after en | `interprétant` | `No second reading proposed.` | medium | Interprétant fits the visible letter sequence; ending is compressed. |
| 377.2 | top third line, additive-group subscript | `a` | `0` | medium | Tiny a resembles a small circle/zero. |
| 377.3 | crossed formula above conjugation relation | `\varepsilon_0(\lambda)` | `No second reading proposed.` | low | Central epsilon/subscript/argument are heavily crossed; outer u and u inverse remain legible. |
| 377.4 | (27), source group superscript | `\circ` | `\flat` | low | Heavily overtraced circle/flat-like mark next to the star and argument (0). |
| 377.5 | (28), horizontal arrow label | `\theta` | `\Theta` | medium | Theta is overtraced; uppercase versus lowercase is uncertain. |
| 377.6 | (28), deleted first tuple entry | `\alpha` | `No second reading proposed.` | low | Crossing obscures part of alpha. |
| 377.7 | (28), deleted final tuple entry | `\varepsilon` | `No second reading proposed.` | low | Crossing obscures epsilon and adjacent closing punctuation. |
| 377.8 | (28), deleted vertical comparison below alpha | `\Vert` | `=` | low | Two small strokes could be vertical equality or an equality sign. |
| 377.9 | (28), deleted vertical comparison below beta | `\Vert` | `=` | low | Two small strokes could be vertical equality or an equality sign. |
| 377.10 | (28), final factor of bottom object | `N'_\sigma` | `T'_\sigma` | low | N is written over an earlier shape resembling T; prime and sigma are visible. |
| 377.11 | below projection map, du produit ... comme | `considérée` | `considéré` | medium | Final e after the accented ending is not secure. |
| 377.12 | inclusion diagram near bottom | `\hookrightarrow` | `\subset` | medium | Left hook is visible; the right terminal could be a stylized arrowhead or the end of a subset stroke. |
| 377.13 | near bottom, On posera aussi ... | `souvent` | `No second reading proposed.` | medium | Compressed final word read as souvent. |
| 377.14 | left of final displayed formula | `(` | `No second reading proposed.` | medium | Isolated curved mark read as an opening parenthesis; no closing counterpart appears on this scan. |
| 377.15 | final displayed formula, map symbol | `\theta` | `\Theta` | medium | Same overtraced theta/Theta as in (28). |
| 377.16 | last line, before crossed si det | `donc` | `d'où` | medium | Word could read donc or d’où. |

## 3. Abbreviations and shorthand

Possible expansions are confined to these notes. The same abbreviated form can have a different grammatical expansion in another sentence; low-confidence expansions are not substitutes for the written form. The tables retain the local qualifications from each portion of the manuscript.

### Scans 359–363

| As written | Tentative expansion, for the notes only |
|---|---|
| néc. | nécessaire(s), nécessairement according to the context |
| néc.ᵗ | nécessairement |
| suff. | suffisante(s) |
| unipot. | unipotent(e)(s) |
| unip. | unipotent(e)(s) |
| unip.ᵗ | unipotent |
| strᵗ | strict, possibly strictement; the reading itself is doubtful |
| inv. | inversible |
| plus gén. | plus généralement |
| p.ex. | par exemple |
| car. | caractéristique |
| il f. et s. | il faut et suffit |
| isom. | isomorphe |
| nbs | nombres |
| rég | régulier(s) |
| can.ᑫ | canonique |
| s-groupes | sous-groupes |
| par. | paramètre |
| hyp. | hypothèse |
| i.e. | id est / c'est-à-dire |
| rés. | résiduelle(s), uncertain reading |
| alg. lin. | algèbre linéaire |
| ssfibrés | sous-fibrés, uncertain exact abbreviated spelling |
| ss | sans |
| hom. | homomorphismes |
| $\overline{\mathrm m}$ | même(s) |
| resp. | respectivement |
| cqfd. | ce qu'il fallait démontrer |
| dfn | définition; written above an equality sign |
| mono | monomorphisme |
| rég. | régulier(s), régulière(s) |

### Scans 364–368

| Written form | Probable expansion (not expanded in the transcription) |
|---|---|
| `i.e.` | id est / c'est-à-dire |
| `f. et s.` | faut et suffit |
| `tte` | toute (uncertain reading of the abbreviation) |
| `inv.` | inversible |
| `cf.` | confer / voir |
| `prop.` | proposition |
| `p.` | page |
| `loc.` | localement |
| `fppf` | fidèlement plat et de présentation finie |
| `proj. élém.` | projecteur élémentaire |
| `ssi` | si et seulement si |
| `$\overline{\mathrm m}$` / `$\overline{\mathrm m}$s` | même / mêmes |
| `hom.` | homomorphismes |
| `autom.` | automorphisme |
| `ens.` | ensemble |
| `lac` (uncertain subscript of `Aut`) | Possibly “lacets”; identification remains uncertain. |
| `ds` (uncertain) | dans |
| `dfn` | définition / par définition |

### Scans 369–373

| Written form | Proposed expansion or meaning |
|---|---|
| `act.` | action; the precise abbreviation ending is uncertain. |
| `g.` | gauche, in the phrase concerning multiplication. |
| `unip` with superscript `t` | unipotent; uncertain abbreviation reading. |
| `df` above an equality | définition / « par définition ». |
| `i.e.` | id est, c'est-à-dire. |
| `ablt` with superscript `n` | Unresolved; possibly an abbreviation concerning abelianization. It should not be expanded without rechecking the image. |
| `NB` | nota bene. |
| `homoth.` | homothétiques; low-confidence reading in scan 369's diagonal note. |
| `en q.` | en question; low-confidence reading at the end of the same note. |
| `p. ex` | par exemple. |
| `s.` | suffit, in « il faut … et il s. ». |
| `p.` | page. |
| `loc` with superscript `t` | localement. |
| `inv.` | inversible. |
| `Rem.` | Remarque; reading uncertain. |
| `\overline{\mathrm m}` | même. |
| `Tr` | trace. |
| `det` | déterminant. |

### Scans 374–377

These possible expansions are editorial aids confined to these notes; they are not substituted into the transcription.

| As written | Possible meaning | Location / qualification |
|---|---|---|
| `\overline{\mathrm m}` | même | Scan 376, “lui-m̄”. |
| `\overline{\mathrm m}s` | mêmes | Scan 374, before “équations (20)”. |
| `1/2` before “direct” | semi- | Scan 374; the small fraction itself remains doubtful. |
| `1/2` before “simple” | semi- | Scan 376. |
| `ssgroupe` or `s/groupe` | sous-groupe | Scan 375; written form is uncertain. |
| `mono` | monomorphisme / monomorphism | Scan 375, “est mono”. |
| `iso.` | isomorphisme | Scan 375. |
| `isom.` | isomorphe | Scan 376, “est isom. au sous-schéma”. |
| `hom` / `hom.` | homomorphisme | Scans 375 and 377. |
| `épi` | épimorphisme / épimorphique | Scan 375. |
| `i.e.` | id est | Scan 375, third row of diagram (22). |
| `car.` | caractéristique | Scan 376, characteristics 2 and 3. |
| `dim` | dimension | Scan 376, inserted parenthesis and underlined conclusion. |
| `non-s` / `non-g` | possibly non-scalaire | Scan 376, inserted parenthesis after rho; the reading and expansion are low confidence. |
| `Ker` | noyau / kernel | Scan 376, (26). |
| `det` | déterminant | Scans 374–377. |
| `OK.` | acknowledgment of the calculation | Scan 377, after (27). |

## 4. Legibility and editorial limits

The main prose and large formulas are substantially more legible than the cancellations, diagonal marginal notes, compressed endings, and tiny superscripts. The least secure passages are the revised clauses on scans 359–363, the normalization letters and overwritten reference on scans 364–365, the amended paragraph after (2) on scan 368, the diagonal note on scan 369, and the group superscripts and crossed coordinate expressions on scans 372–377. The recurring b-shaped superscript remains explicitly uncertain between a flat sign and a literal b; the distinct small circles and changing order relative to stars have been retained. One deleted word on scan 376 remains `\illegible{1}` after enlarged inspection. No mathematical glyph is replaced by an illegibility count.

Several incomplete or apparently inconsistent forms are deliberate retentions. The prime on T₀ varies in scans 372–374; the opening question on scan 367 visibly lacks an inverse exponent on its final unipotent; the set description on scan 368 reaches the edge without visible closing punctuation; and scan 376's (25) ends its parameter image with “det a = det”. The last sentence on scan 377 is unfinished. These have not been completed from context.

Every page was compared with its transcription and inventoried; difficult areas were examined in enlarged or rotated crops, with independent rereadings of selected passages. The files have also been checked for scan coverage, balanced LaTeX braces and environments, diagram alignment tokens, and CSV completeness. A compiled rendering could not be verified: the local TeX installation has binaries but lacks the required formats and packages. This is a source-level transcription with explicit residual uncertainty, not a claim of a definitive critical edition.

## 5. Research notes — English, separate from the transcription

These items identify questions, unproved or deferred claims, implications worth pursuing, and explicitly labelled editorial ideas. They are grounded in the supplied pages; earlier hypotheses and later proofs are not presumed. A statement listed here may be established elsewhere in the manuscript. No idea is asserted to be new, and no uncertain reading is silently promoted into a mathematical premise. Author-date citations refer to the primary-source entry at the end; references to scan numbers provide precise locations within this supplied excerpt.

### Scans 359–363

#### R359.1 — Scan 359, middle — unpursued implication

The equations “$2\nu=0$, $\nu^2=0$” isolate the scalar ambiguity as a simultaneous square-zero and 2-torsion phenomenon. The claim that the earlier map (43) is injective precisely when these sections vanish suggests separating the question about sections over the chosen base from the stronger question about a monomorphism after arbitrary base change. Equation (43) itself is outside the supplied extract, so its full source and target must be recovered before asserting the stronger formulation. (Grothendieck, 1981, scan 359).

#### R359.2 — Scan 359, bottom — own idea

**Confidence: high for the algebraic example; limited for its application to the absent map (43).** Test the displayed equations over $R=\mathbf F_2[\eta]/(\eta^2)$ with $\nu=\eta$ and $\lambda=1+\eta$. The equations hold although $\lambda\ne1$; this gives a direct test object for the nontrivial infinitesimal scalar ambiguity described here, without relying on a classification theorem. (Grothendieck, 1981, scan 359).

#### R359.3 — Scan 359, bottom — unpursued implication

The phrase “fini sur $\mathbf Z$, pas plat sur $\mathbf Z$” accompanies a presentation with a square-zero $\mathbf Z/2\mathbf Z$ summand. A useful continuation would compute the fibers and the group law in the $\nu$ coordinate separately; the coordinate-ring presentation alone does not identify its Hopf structure with an additive square-zero construction. That distinction matters when applying the translation quotient on the next sheet. (Grothendieck, 1981, scan 359).

#### R360.1 — Scan 360, upper half — unproved claim

“Il se trouve que $\mu'_{2S}$ opère librement par translations” precedes the isomorphism (47). No proof of the quotient assertion is supplied on this sheet. A proof would have to specify the represented unipotent functors, check the scalar action, and show that the asserted quotient has the displayed projective target over the relevant bases, including bases with nilpotents and 2-torsion. (Grothendieck, 1981, scan 360).

#### R360.2 — Scan 360, middle — conjecture / question

Grothendieck asks, “La difficulté proviendrait-elle du fait que les flèches verticales … ne seraient pas injectives,” outside the hypothesis that 2 is invertible. The question concerns the compatibility of the two Borel correspondences with the proposed correspondences for one-parameter unipotent subgroups. The next scan proposes a different explanation involving the failure of an individual projective unipotent section to determine a parametrization, so the initial question should not be reported as his final conclusion. (Grothendieck, 1981, scan 360).

#### R360.3 — Scan 360, lower half — unproved claim

“J'ai envie de dire que” introduces $B=\operatorname{Norm}(B_u)$ and $\widetilde B=\operatorname{Norm}(\widetilde B_u)$. He says that he has checked the first formula by linear algebra, but gives no calculation here and does not supply the projective version. A verification should be scheme-theoretic over the bases under discussion, since checking geometric points would miss the infinitesimal phenomenon already isolated on scan 359. (Grothendieck, 1981, scan 360).

#### R361.1 — Scan 361, upper half — conjecture / proposed explanation

“La difficulté doit plutôt provenir du fait” introduces the problem of associating a parametrized one-parameter subgroup to a projective unipotent section. The word immediately after “fait” has a doubtful reading and must not be used to strengthen the quantifier in the claim. The subsequent formulas give the concrete ambiguity through $\varepsilon'=\lambda\varepsilon$. (Grothendieck, 1981, scan 361).

#### R361.2 — Scans 361–362, lower and upper portions — unpursued implication

The two parametrizations are asserted to be “distincts”; the following phrase states that they share the value at $t=1$, using a sign that looks like two horizontal strokes. Their derivatives are then compared in $M/\mathcal O_S$. This suggests studying the fibers of evaluation at 1 on the relevant scheme of homomorphisms, rather than treating evaluation as a complete invariant. The differential calculation is continued on scan 362, so this is a consequence to investigate, not a claim that the manuscript leaves the displayed distinction wholly unproved. (Grothendieck, 1981, scans 361–362).

#### R361.3 — Scan 361, lower half — own idea

**Confidence: high for the suggested calculation; no general classification claimed.** Over $R=\mathbf F_2[\eta]/(\eta^2)$, use the visibly displayed family with a nonzero square-zero $2\times2$ matrix $N$ and $\lambda=1+\eta$. Comparing $1+tN$ with $1+t((1+\eta)N+\eta I)$ in the projective quotient gives an explicit test of how equality at $t=1$ can coexist with different derivatives. The calculation should retain the entire polynomial family over $R[t]$, rather than checking only $R$-valued values of $t$. (Grothendieck, 1981, scan 361).

#### R362.1 — Scan 362, upper third — own idea

**Confidence: high for the local algebra check, conditional on the intended bundle hypotheses.** The step from “partout non nulle” to $\nu\widetilde N=0\Rightarrow\nu=0$ can be checked by making a coordinate of $\widetilde N$ a unit locally. A complete account should explicitly distinguish a section nonzero in every residue-field fiber from a section merely nonzero as a global section; only the former directly supplies this local argument. This is a proposed verification of the manuscript's step, not an emendation of its wording. (Grothendieck, 1981, scan 362).

#### R362.2 — Scan 362, middle and lower portions — unpursued implication

The conclusion requires “aussi des ‘sous-groupes à 1 paramètre’ (paramétrés)” in addition to the projective elements. This suggests that a suitable parameter space should retain the homomorphisms themselves and their compatibility under conjugation, rather than only their values at 1. The proposition on the next scan provides a concrete formulation to test, with a strictness condition on the homomorphism. (Grothendieck, 1981, scan 362).

#### R363.1 — Scan 363, proposition, item 1 — unproved claim

The assertion “$\exists$ uniques $\varepsilon_0,\varepsilon_1$ sections” gives unique regular-unipotent lifts associated with the parametrized projective subgroups. No proof is included on this sheet. A proof would need to establish existence locally, show uniqueness with the entire parametrization fixed, and verify compatibility on overlaps; the scalar ambiguity from scan 359 should not be discarded merely by checking the value at 1. (Grothendieck, 1981, scan 363).

#### R363.2 — Scan 363, item 3 and bottom — unproved claim

“Pour un choix convenable de $\rho$” introduces the normalization $\lambda_0=1$, followed by the statement that it determines $\rho$ uniquely in terms of $\sigma$ and conversely. The page states the scalar relations for lifts but does not show the descent or invertibility checks behind the normalization. Those checks should be made before treating the statement as a global choice over an arbitrary base. (Grothendieck, 1981, scan 363).

### Scans 364–368

- **Scan 364, items 4–5, equations (57)–(57′); kind: unproved claim.** The criterion “`\operatorname{Tr}(\rho+\sigma)` inv.” is asserted to characterize fibrewise independence, and the normalization `\operatorname{Tr}(\rho+\sigma)=1` is said to determine the lifts “de façon unique.” A proof would have to establish the trace criterion over the stated base and then check existence, uniqueness, and descent of the locally chosen lifts, especially where 2 is not invertible; the referenced proposition on manuscript p. 478′ may already supply part of the argument. (Grothendieck, 1981, scan 364).
- **Scan 364, “Remarques” 1 and equations (58)–(59); kind: unpursued implication.** The statement that the conditions are “symétriques” in `(\rho,\sigma)` is accompanied by inversion of both associated unipotents after exchanging the pair. This gives a concrete symmetry to follow through the subsequent choice of preferred unipotent and its normalization; no independent claim about its eventual scope is made here. (Grothendieck, 1981, scan 364).
- **Scan 365, equation (62); kind: unproved claim.** The identity for the trace of the inverted pair is attributed to “un calcul matriciel immédiat,” without the calculation being supplied on this page. A verification should begin with the rank-two identity for the trace of an inverse and explicitly recover the sign and denominator from the earlier normalization conventions, whose parameter letters remain palaeographically uncertain here. (Grothendieck, 1981, scan 365).
- **Scan 365, final paragraph; kind: own idea. Confidence: medium.** The proposed four “épinglages ‘naturels’” should be checked after specialization to characteristic 2: inversion of a square-zero unipotent matrix then coincides with the original matrix, so distinctions visible in the displayed formulas may collapse. This is a suggestion for checking the precise moduli data, not a claim that the manuscript's four choices are globally identical; the reason is the elementary calculation `(1+N)^{-1}=1-N` when `N^2=0`. (Grothendieck, 1981, scan 365).
- **Scan 366, paragraph beginning “On a préféré normaliser”; kind: unpursued implication.** The author explicitly ties the normalization to the “forme la plus commode de l'équation des lacets,” with references to §§44–45. This identifies an order-dependent convention rather than an invariantly selected one; comparing those earlier sections would clarify which displayed signs and matrix entries arise from that convention. (Grothendieck, 1981, scan 366).
- **Scan 366, item 2, equation (64); kind: unproved claim.** A group, whose handwritten letter is uncertain here, is said to act “par permutations circulaires” and by reversal with inversion of the triple. The verification to supply is that these operations preserve the product relation and induce exactly the stated exchange of the pair after a cyclic permutation; the next page continues this interpretation. (Grothendieck, 1981, scan 366).
- **Scan 367, opening question; kind: conjecture (explicit question).** “Comment … interpréter la transformation” asks for a group-theoretic interpretation of simultaneous inversion of the pair. The following lines propose precomposition with a specified automorphism of `\Pi_{0,3}`, so the question is pursued on this very page rather than left wholly unanswered. (Grothendieck, 1981, scan 367).
- **Scan 367, automorphism displays and final paragraph; kind: unproved claim.** The four transformations are identified with a subgroup isomorphic to `\mathbb Z/2\mathbb Z\times\mathbb Z/2\mathbb Z`, generated by the two written τ-automorphisms, and said to stabilize `L_0`. A proof should check the relations and the precise automorphism category denoted by the uncertain subscript on `Aut`, then distinguish stabilizing the subgroup itself from stabilizing its conjugacy class if the latter is relevant. (Grothendieck, 1981, scan 367).
- **Scan 367, opening question compared with scan 365, (61); kind: own idea. Confidence: high about the need for comparison, low about the resolution.** The question's final triple visibly ends in `\widetilde\varepsilon_1` without an inverse, whereas (61) earlier relates the transformed first unipotent to an inverse of an indexed unipotent. A notation audit should check whether a different triple convention explains the apparent mismatch before treating it as an error; the transcription deliberately preserves both readings. (Grothendieck, 1981, scan 367).
- **Scan 368, opening paragraph and (2); kind: unproved claim.** The “possibilité de paramétriser les solutions” is recalled as the essential result reached in III. The page writes an explicit morphism from `B'_0\times T_\rho\times T_\sigma`, but the recap alone does not establish bijectivity or a scheme-theoretic isomorphism; those properties require the earlier hypotheses and proof, which are only referenced here. (Grothendieck, 1981, scan 368).
- **Scan 368, diagonal marginal note; kind: conjecture (explicit question).** The note asks “à quelles conditions on peut avoir une paramétrisation” of the indicated form. The distinction between starting with `\rho,\sigma,B'_0,\varepsilon_1` and assuming the already normalized situation is worth tracking in the following pages, where the sufficient and necessary conditions may be separated. (Grothendieck, 1981, scan 368).
- **Scan 368, sentence between (2) and (3); kind: unproved claim.** Membership in the solution scheme is reduced to the displayed identity `\rho(u)=\varepsilon_1(-\nu(u))\sigma(u)`. A detailed verification must state how `\rho(u)` and `\sigma(u)` denote conjugation, use the defining commutation of the two centralizer factors, and check that the map to the additive group is a morphism of schemes; the page gives the algebraic rearrangement but not those functorial details. (Grothendieck, 1981, scan 368).
- **Scan 368, remark following (2); kind: unpursued implication.** The author says that `\nu(u)=\det(u)-1` has no “importance capitale” for the moment. This points to a potentially more general parametrization problem with an initially unspecified scalar-valued morphism, although the page does not assert such a generalization as a theorem. (Grothendieck, 1981, scan 368).

### Scans 369–373

The following items concern what is written or suggested on these particular leaves. They do not assert novelty, and a point flagged here may be proved or reconsidered elsewhere in the manuscript. The sole source used is the supplied manuscript (Grothendieck, 1981); no published transcription has been consulted.

1. **Scan 369, approximately lines 8–9; kind: unproved claim.** The parenthesis « et par un argument connu » passes from an inclusion involving the image of `B'_0` to equality with `B'_1`. The underlying argument should be reconstructed at the level of subgroup schemes over the intended base, including which hypotheses ensure that a fibrewise inclusion yields the asserted equality (Grothendieck, 1981, scan 369).

2. **Scan 369, formula (4); kind: unpursued implication.** The phrase « la propriété essentielle » identifies normalization of `B'_0` by `σ^{-1}ρ` as the compatibility needed for the proposed construction of solutions. This should be kept distinct from the surjectivity question raised on the next leaf: a comparison of the construction's domain with the full solution functor would clarify the exact scope of the criterion (Grothendieck, 1981, scans 369–370, eqs. 4 and 6).

3. **Scan 369, formula (5) and right margin; kind: unproved claim.** The marginal « Il suffit p. ex » gives a sufficient intersection condition for uniqueness of the parameters. Its verification should use intersections of group functors or subgroup schemes, not merely intersections of geometric-point sets, since nonreduced intersections could affect uniqueness (Grothendieck, 1981, scan 369, eq. 5). The reading of the right member as the multiplicative group remains marked in the transcription.

4. **Scan 369, lower-left marginal note; kind: unpursued implication.** The low-confidence note mentions « Borels contenant » and appears to discuss the ambiguity in choosing `B_0` from a regular relative element. Before using its mathematical content, the uncertain wording must be checked; once established, it suggests comparing the possible Borels in the semisimple and unipotent cases and the behavior of this choice over a nonfield base (Grothendieck, 1981, scan 369, lower-left margin).

5. **Scan 370, approximately lines 3–7 and formula (6); kind: conjecture / question.** The explicit question « toute solution de (1) s'écrit-elle bien » asks whether the displayed parametrization exhausts the solutions. A proof needs to establish surjectivity of the map from `B'_0` to the simultaneous-solution scheme `𝓧_{ρ,σ}`, with the stated interpretation of regularity and with local lifting over the relevant base (Grothendieck, 1981, scan 370, eqs. 6–7).

6. **Scan 370, last paragraph and formula (8); kind: conjecture / doubt.** « Il n'est pas clair si ces conditions » explicitly questions the necessity of the two strong hypotheses used earlier, including the general-position condition. Testing necessity would require examples satisfying the parametrization with weaker conditions, or a counterexample after one hypothesis is removed; their role in the preliminary calculations alone does not settle that issue (Grothendieck, 1981, scan 370, eq. 8).

7. **Scan 371, first paragraph; kind: conjecture / expectation.** « La suite montrera si cette restriction est judicieuse » leaves the choice of hypotheses open for later examination. The text regards unipotence, or at least quasi-unipotence, of the relative element as natural while describing condition (8b) as less imperative; these are the author's provisional judgments on this leaf (Grothendieck, 1981, scan 371).

8. **Scan 371, trace-zero discussion after (9); kind: own idea.** One can test the stability claim by comparing the trace condition before and after multiplication of `η` by a general section of `μ₂`, without immediately specializing that section to `−1`. **Confidence: medium**, because trace linearity and the determinant relation explain the proposed calculation, but the distinction between all scheme-valued `μ₂` points and one visible sign becomes material over bases with 2-torsion (Grothendieck, 1981, scan 371, eq. 9 and following paragraph).

9. **Scan 371, formula (10); kind: unproved claim.** The recapitulation identifies « le résultat crucial » as the displayed isomorphism from `B'_0 × T_ρ × N'_σ`. A self-contained proof on these leaves would need an inverse construction, uniqueness of its parameters, and compatibility with base change; those ingredients are not supplied in this recapitulating paragraph (Grothendieck, 1981, scan 371, eq. 10).

10. **Scan 372, approximately lines 1–7; kind: unproved claim.** The first assertion is called « trivial par définition », while the subsequent assertion says that local realization of arbitrary signs « exige justement » trace zero. The precise local topology and the equivalence between the normalizer condition and realization of the sign should be made explicit, especially when 2 is not invertible (Grothendieck, 1981, scan 372).

11. **Scan 372, approximately lines 8–12; kind: own idea.** Because the group structure on `𝓖*` is introduced by transport from the product, it is useful to write its multiplication explicitly in the displayed commutator coordinates and check each later subgroup against that law. **Confidence: high** that this is a well-defined check, since an isomorphism is explicitly invoked; no claim is made here that the coordinatewise product in the ambient factors already gives the transported law (Grothendieck, 1981, scans 371–372, eq. 10).

12. **Scan 373, formulas (16)–(17); kind: unproved claim.** « Des structures de produit semi-direct » records a decomposition with the subgroup `Λ_0`, whose diagonal embedding is then displayed. A full verification should establish the unique factorization, normality of the appropriate factor, and the conjugation action with the factor order exactly as written (Grothendieck, 1981, scan 373, eqs. 16–17).

13. **Scan 373, marginal note beside (19); kind: unproved claim.** The note « ε²=1 résulte déjà de la première relation » records a redundancy among the equations. Taking determinants is the indicated route to a verification, with the rank and the determinant of the one-parameter unipotent term stated explicitly (Grothendieck, 1981, scan 373, eq. 19 and margin).

14. **Scan 373, formula (20); kind: own idea.** Eliminating `ε'` from the final determinant conditions suggests a description using equality of the squares of two determinant characters. **Confidence: high at the level of the displayed equations**, since `ε'=det(b)/det(a)` and `ε'^2=1` give precisely that algebraic test; the corresponding subgroup-scheme description and action still require verification, and may be developed on subsequent leaves (Grothendieck, 1981, scan 373, eq. 20).

### Scans 374–377

The following notes are based only on the supplied manuscript images. They distinguish the author’s statements from possible work suggested by those statements; no implication is claimed to be new, and no hypothesis missing from preceding pages has been supplied.

#### R374.1 — Scan 374, (22) — Unproved claim

The phrase “une structure de produit 1/2 direct” asserts the semidirect decomposition displayed in (22). A full proof needs an identified normal factor, a splitting, and the conjugation action, all as group-scheme constructions over the intended base. The calculation of the action is taken up explicitly on scan 377, so this is a deferred step within the supplied extract (Grothendieck, 1981, scans 374, 377).

#### R374.2 — Scan 374, after (24) — Unpursued implication

The instruction “en remplaçant N′σ par Tσ” relates the starred and unstarred subgroup descriptions. It suggests comparing the resulting inclusions and quotients functorially, with particular care over the superscripts and base hypotheses that distinguish the groups. These pages state the replacement but do not spell out that comparison as a separate result (Grothendieck, 1981, scan 374).

#### R375.1 — Scan 375, first projection and (21) — Unproved claim

The projection “est mono, et induit un iso.” onto the determinant-constrained subgroup. The preceding isomorphism from T0 to the multiplicative group should provide the reconstruction of the omitted u-coordinate, but the inverse morphism and its compatibility with base change are not written out here. Checking that construction would make precise which determinant relation is used at each step (Grothendieck, 1981, scan 375).

#### R375.2 — Scan 375, (22) — Unproved claim

The sentence beginning “On voit tout de suite” asserts that the displayed map to μ2 × μ2 is an epimorphism, using the epimorphism of the determinant characters. A proof should specify the sheaf topology and construct local lifts satisfying the coupled determinant conditions, rather than infer surjectivity merely on points over a field. This matters especially for bases with residue characteristic 2, where the displayed μ2 factors require scheme-theoretic treatment (Grothendieck, 1981, scan 375).

#### R376.1 — Scan 376, (25)–(26) — Unproved claim

The phrase “se dévisse donc à son tour” introduces a second exact sequence with the determinant kernels as its first nontrivial term. Its exactness requires checking both the kernel identification and local surjectivity of the common determinant map, with the preceding equal-determinant relation imposed. The incomplete written endpoint of the parameter-image formula in (25) should not be silently repaired while reconstructing this proof (Grothendieck, 1981, scan 376).

#### R376.2 — Scan 376, modular matrices and conclusion — Unproved claim

For the two displayed matrices, the manuscript says one determinant-kernel group is a “tore ... sauf en car. 3” and the other a torus except in characteristic 2, concluding “tore de dim 3” away from those characteristics. A proof should compute the relevant centralizer algebras and their determinant kernels, then justify the dimension and torus property of the extension in (25). The exceptional fibers deserve an explicit calculation rather than only the exclusion stated here (Grothendieck, 1981, scan 376).

#### R376.3 — Scan 376, displayed modular matrices — Own idea

Compute the characteristic polynomials of the written matrices, x² − x + 1 and x² + 1, and examine their repeated-root fibers in characteristics 3 and 2. These elementary calculations suggest a direct route to describing the exceptional determinant-kernel group schemes, including possible nonreduced or unipotent structure, without assuming that the torus description extends to those fibers. Confidence is high for the polynomial calculations and medium for the proposed structural route, because the definitions and base conditions preceding this excerpt are still needed (source matrices: Grothendieck, 1981, scan 376).

#### R377.1 — Scan 377, conjugation relation and (27) — Unpursued implication

The manuscript concludes that “l’opération se fait via le caractère composé” through the displayed determinant character. Consequently the kernel of that character is the natural subgroup to test for trivial action on the additive factor in the semidirect product. Establishing the exact kernel and its behavior over the base would sharpen the decomposition beyond the factorization written on this page (Grothendieck, 1981, scan 377).

#### R377.2 — Scan 377, (28) and first projection — Own idea

Construct the “hom. canonique” directly from the original coordinates, then compare that construction with its description as the first projection on B′0 × Tρ × N′σ. This would test the asserted canonicity against the chosen product parametrization and identify its kernel and image under the transported group law. Confidence is medium: the projection description gives a concrete route, but the full earlier definition of the solution group and its multiplication is required (Grothendieck, 1981, scan 377).

## Reference

Grothendieck, A. (1981). *La Longue Marche à travers la théorie de Galois* [Handwritten manuscript, cote 140-3; supplied scans 359–377, lower folios 358–376]. Université de Montpellier archive. https://grothendieck.umontpellier.fr

The bibliographic identification and date are supplied with the images; the archive URL is reproduced from their printed imprint. This transcription and these research notes do not rely on the contents of an externally retrieved archive page.

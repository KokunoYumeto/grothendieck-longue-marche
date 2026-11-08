# LM_P036 — Notes to the diplomatic transcription

## Source and locating conventions

All manuscript quotations and source claims below refer to the ten supplied images of Grothendieck's *La Longue Marche à travers la théorie de Galois* (1981). The transcription follows the **file/scan numbers 351–360**, as required by the attached task. The archive numbers visible at the foot of the images are one lower. Only the authorial folios visible at the top are entered with `\mspage`.

| Scan / file number | Archive footer | Visible authorial folio |
|---|---|---|
| 351 | 350 | — |
| 352 | 351 | 178 |
| 353 | 352 | — |
| 354 | 353 | 179 |
| 355 | 354 | — |
| 356 | 355 | 180 |
| 357 | 356 | — |
| 358 | 357 | 181 |
| 359 | 358 | — |
| 360 | 359 | 182 |

The `.tex` file is a fragment, with no preamble or macro definitions. It uses the requested editorial macros, conventional LaTeX mathematical notation, and `tikz-cd`. No missing continuation has been supplied at either boundary. Diagram descriptions in square brackets describe visible marks when the arrowheads or an overwritten object prevent a secure diagram encoding; they are editorial descriptions, not additional manuscript prose.

**Repeated letterform uncertainty.** The principal two-upright group glyph sometimes has a long curved right foot, and its case cannot be settled consistently from these scans. It is explicitly rendered `\unsure{\Pi|\pi}` at every occurrence, including within decorated expressions, instead of silently standardizing to either case. This does not express uncertainty about the separately visible primes, indices, or hats. The ornate C/G-like symbol is likewise marked where uncertain; the leaner T-like symbol has not been replaced by it. Single and double hats, broad accent scopes, plus signs, and argument hats have not been regularized to a presumed mathematical convention.

**Limits of the notes.** These are source-based research notes, not a survey of subsequent literature or a claim about novelty. No published transcription or secondary source was used to supply a manuscript reading. Suggested proof obligations and examples are kept outside the transcription; they are not asserted to be missing from the manuscript as a whole. A development or change of confidence later within these ten scans is cross-referenced where relevant. In particular, scan 360 questions conditions attached to the comparison on `P`; it does not prove that the original `Discret` injectivity statement is false.

## 2. Table of doubts

Locations refer approximately to handwritten main-text baselines, counting displays as rows and excluding the folio and archive footer. Interlinear additions and margins are named separately. The locations are aids to finding the ink, not an imposed line numbering. Confidence is confidence in a proposed reading, not confidence in a mathematical assertion. Repeated instances of the same uncertainty are grouped in a row where practical; the transcription marks each affected instance.

| Scan | Approximate line / location | Reading | Alternatives or unresolved feature | Confidence |
|---|---|---|---|---|
| 351–360 | Every occurrence of the principal two-upright group letter | `\unsure{\Pi\|\pi}` | Uppercase Π versus lowercase π. The curved right foot and variable size do not settle the case; no group-theoretic distinction is inferred. | low |
| 351 | 3, before parenthesis | deleted `n` | The small cancellation may conceal a different one-letter start. | low |
| 351 | 3 | `car.` | `car` without the abbreviation point; the first letter is faint. | medium |
| 351 | left margin, lines 1–3 | `est`, `anabélien` | Very compressed oblique writing; ending of the second word uncertain. | medium |
| 351 | left margin, lines 5–8 | `condition`, `donc conservée`, `aux revêtements` | Several letters merge with the main text. | low |
| 351 | left margin, final four lines | `mesure`, `positivité stricte`, one illegible item, `degré d'anabélianité`, `en qq sorte` | Wording and order are especially uncertain. Two short parallel strokes follow `stricte`; they might be closing quotation marks or the same-sign. No article has been supplied before `positivité`. | low |
| 351 | 6 | `tte` | Contracted word for “toute”; the exact abbreviation is indistinct. | medium |
| 351 | insertion above cohomology formula | `dans le cas discret` followed by one deleted illegible word | The letters of `discret` are compressed; the cancellation is unreadable. | low |
| 351 | cohomology formula | `U`, `U′` | Possibly calligraphic `𝒰`, `𝒰′`; the strokes do not settle the alphabet. | low |
| 351 | cohomology formula, coefficient symbol | blackboard `ℤ` | Bold `Z`; double strokes are visible but their intended alphabet is uncertain. | medium |
| 351 | after `(l'isom. trace)` | `θ` | An isolated overwritten mark precedes `T′`; it could be a correction rather than a retained θ. | low |
| 351 | inserted parenthesis around the restriction condition | `tt π′` | Exact abbreviation and extent of the spanning parenthesis are uncertain. The condition is visibly `d'indice fini de π`. | medium |
| 351 | penultimate main line | `soit` | `soient`; ending is a short dark stroke. | medium |
| 351 | deleted last line | `qu'il le soit` | `qu'il en soit`; the crossing line obscures the short words. | low |
| 352 | formula after `telles que`, lines 5–7 | `Aut ext` / `Autext`, subscript `lac`; doubly hatted `𝒯` | The spacing of the compound operator and exact script alphabet are less secure than the arrows, hats, and prime/subscript positions. | medium |
| 352 | right-side note, product formula | `Π′·Π₀ = Π` | `Π′₀·Π₀ = Π`; an overwritten mark under the first prime could be a cancelled subscript. | low |
| 352 | immediately before `Π′₀ soit dans` | one deleted illegible word / symbol | The dark mark is intertwined with the margin note and may be a rewritten group symbol. | low |
| 352 | 11, `le Π₀… donnant` | superscript `*` | The mark could be a cancelled prime or an overwritten correction; it is retained under a doubt mark. | low |
| 352 | 12 | `naissance` | Initial letters are overwritten. | medium |
| 352 | 17, article before the cancellation | `le` | `l′`; an added small loop and the former apostrophe overlap. | low |
| 352 | 17, cancellation before `profini` | `adhérence dans` | `extension de`; the tall stem favours `adhérence`, but the entire phrase is struck through. | low |
| 352 | 21, cancelled short word before `groupe` | `gr` | `un`; dense deletion obscures it. | low |
| 353 | 4, after `Faisons` | `itou` | Compressed short word; only its initial `it` is particularly clear. | medium |
| 353 | 5, between the two group symbols | `⊃` | `>`; the short right-pointing stroke does not settle inclusion versus inequality notation. | low |
| 353 | 7, after `aux m̄` | `dᵢ` | `δᵢ`; the stem and index are not securely distinguished. | low |
| 353 | 9 | `connu` | The middle letters are only a wavy stroke. | medium |
| 353 | 9 | `tte` | Exact contraction for “toute” is uncertain. | medium |
| 353 | 16, after `y avoir` | `une action` | `des actions`; the determiner is overwritten and the noun ending is faint. | low |
| 353 | 16, above-line insertion | `extérieure` | `extérieures`; the final stroke is uncertain. | medium |
| 353 | 18 | `factorise` | `factorisent`; manuscript ending is indistinct. | low |
| 353 | 20–21 | `bonne`, `celle` | `bonnes`, `celles`; final strokes could be plural endings. | medium |
| 353 | 21, final abbreviation | `ss-groupe` | `s-groupe`; the two initial short strokes and hyphen merge. | low |
| 354 | 2 | `\Pi_0\supset\Pi'_0` | The relation is angular and could literally be `>`; both are retained in a doubt mark. | medium |
| 354 | 3, following `Autext` | One deleted mathematical item | The overstruck blob cannot be read securely. | low |
| 354 | 3, last group | A single hat over `\mathcal T`, with a separate hat over `\Pi'_0` | There may instead be two hats over the calligraphic letter. | low |
| 354 | 5, `de façon` | Underlined `de façon` | The heavy squiggle beneath may be a cancelled earlier two-word expression, with `de façon` inserted above it. The transcription exposes both possible states. | low |
| 354 | 6 | `factorise` | The final letters are attenuated; no independent alternative is secure. | medium |
| 354 | 6, `\mathcal T(\Pi_0^{\prime})` | A prime on the group argument | The prime is overwritten and could conceal another short mark. | medium |
| 354 | 7, insertion after `extension` | Possibly hatted `\Pi` with superscript `\natural` | The upper small mark may be a hat or an adjacent ink mark; the superscript is a zigzag resembling a natural sign, with sharp as an alternative. | low |
| 354 | 10, `sur` | `\Pi^{\natural}` | The repeated superscript is clearer but may be a highly cursive sharp. | medium |
| 354 | 14, inserted criterion | Deleted `fini` | Short crossed word after the group containing `\gamma`; the first and final strokes fit this reading. | medium |
| 354 | 14, inserted criterion | `\operatorname{int}(\gamma).G\not\subset\mathcal T` | The barred relation may be `\notin`; the final calligraphic letter has no visible argument. | low |
| 354 | 14–15, cancelled original criterion | `u`, `d'ordre`, then one illegible word, `provenant pas de, dans` | Several words are crossed through more than once; neither the sequence nor the word endings are secure. | low |
| 354 | 15, cancelled block | `ou se relevant` | First two words and the participial ending are doubtful; they have not been normalized to a smoother construction. | low |
| 354 | 16, cancelled block | `\mathcal G(\Pi'_0)^+=\operatorname{Aut}_{\mathrm{lac}}(\Pi'_0)^+` | The highly looped first letter may be calligraphic C rather than G. | low |
| 354 | 17, cancelled clause | `dont la conjugaison dans … un` | The wording is crossed out; `conjugaison` and the final `un` are only proposals. | low |
| 354 | 18–20, successive revisions | Deleted `i.e. tel que u ne fixe`; later `i.e. tel que G ne stabilise pas …` | The revisions overlap a larger cancelled passage. The later right-hand wording appears uncancelled, but the exact chronological boundary of that cancellation is not certain. | low |
| 354 | 20, right-hand addition | `ne stabilise pas` | Letter endings are indistinct; `pas` is close to the page edge. | medium |
| 354 | Last line, preceding `Un tel` | One deleted word | Readable traces are insufficient for a proposal. | low |
| 354 | Last line | `tjrs....` | The abbreviation could be a slightly different contracted form of *toujours*; four terminal dots are visible. | medium |
| 355 | 2 | `des` | `deux` remains possible at this compressed ending. | medium |
| 355 | 2, first group | `\Pi'_0` | A small prime is visible. It is retained despite the subsequent unprimed `\Pi_0`; no correction has been made from the mathematical context. | high |
| 355 | 4 | `prédiscrt.` | `prédiscrét.` is a possible spelling of the abbreviation; the terminal t-stroke is distinct. | medium |
| 355 | 4 | `strictes` | `stricte` is possible; the original `des` is cancelled and replaced by `la` plus the same-sign, so agreement has not been silently corrected. | medium |
| 355 | 9, at right edge | `discrétifications` | The ending may instead be an abbreviated `discrétific.`; the writing reaches the dark page boundary. | low |
| 355 | Display (4) | `Prédiscrt` | The t is taller and clearer than the compressed middle letters. This local spelling is kept instead of harmonizing it with `Prédiscr` in scan 356. | medium |
| 355 | Display (4), both superscripts | `+` | The thickly retraced cross is slightly star-like; `\ast` is retained as an alternative. | medium |
| 355 | Display (5), both labels | `Préarithm` | The compressed middle letters are not individually certain. | medium |
| 355 | Display (6), both groups | `\mathbb{\Gamma}` | There are doubled vertical strokes, but plain `\Gamma` is an alternative alphabetic rendering. It does not resemble the two separated uprights of the fundamental-group letter. | medium |
| 355 | Last word | `comp.` with raised `t`, then `ble` | Exact placement and final abbreviation letters are uncertain; it is not expanded in the transcription. | low |
| 356 | 2–3 | `compatibles` | There is a dot-like short stroke after `comp`; `comp.tibles` could be the actual abbreviation. | medium |
| 356 | 5, both groups | `\mathbb{\Gamma}_{\Sigma}`, `\mathbb{\Gamma}_{\Sigma'}` | Plain Gamma remains possible as the alphabetic rendering of the doubled vertical glyph. | medium |
| 356 | 6–7, twice | `unique` | Each occurrence visibly has an i-like mark before a descending q. Other compressed initial letters cannot be excluded. | medium |
| 356 | 6, `pour` | `pour` | The p is overwritten or heavily looped; the available strokes do not justify marking the whole word as deleted. | medium |
| 356 | 10 | `interprète` | The central strokes and accent are faint. | medium |
| 356 | 10, conjecture formula | Doubled Gamma with indices `g,\nu`, then doubled Gamma with index 0 | Plain Gamma is possible; the second index may be Latin v rather than Greek nu. | medium |
| 356 | 11 | `aurait` | `aura` is possible if the final stroke is merely terminal flourish. The conditional has not been upgraded to a categorical assertion. | medium |
| 356 | 12, inline `Discr` comparison | Plain dash | A weak right arrowhead may have been intended, but no full head is clear; both readings are marked. | low |
| 356 | Diagram, upper horizontal connector | Horizontal line without an arrowhead | A small downward tick appears at the right end; it may be an incomplete right arrowhead. The other two horizontal arrows and all four downward arrows are clear. | low |
| 356 | Diagram, middle-row names | `P`, `P'` | The first letters could be lowercase p; the primes are visible. | medium |
| 356 | Diagram, middle-left operator | `Prédiscr` | The initial `d` or former capital D is overwritten; an independent earlier word cannot be recovered. | medium |
| 356 | First line after diagram | Deleted `diagr` | A final abbreviation point is not certain. | medium |
| 356 | Penultimate line | `injectivité`, `bijectivité` | Some interior and final letters are reduced to strokes; no other reading is secure. | medium |
| 356 | Last line | `Donc` | The middle letters are highly compressed. | medium |
| 357 | 1, deletion after « que » | `\deleted{\unsure{déjà}}` | Crossed letters could be a different short word; no secure alternative. | medium |
| 357 | 1–2, interlinear insertion | `(orientées)` | Ending and attachment after « discrétifications » are not completely secure. | medium |
| 357 | 3 | `orientée` | Last stroke could conceal a plural ending. | medium |
| 357 | 3–4, insertion | `leurs traces sur Π'` | « traces » is plausible from the ink but compressed. | medium |
| 357 | 4, between Π′₀ and Π′₁ | `et` | Overwriting makes the connecting word or possible earlier symbol difficult to distinguish. | low |
| 357 | 6 | `orientée`, underlined `stricte` | Singular/plural endings are reduced to short strokes. | medium |
| 357 | 7, deletion after « clair » | `\deleted{\illegible{3}}` | About three words; a precise expansion is not warranted. | low |
| 357 | 13, group containing u | Wide accent over C/G(Π₀), exponent + | Ornamental C/G alphabet and exact reach of the broad accent. | low |
| 357 | 14, group containing u′ | Wide accent over C/G(Π₀, Π′₀), exponent + | There is a dark accent/overwriting near + whose independent status is unresolved. | low |
| 357 | 15–17, repeated group symbols | C/G(Π₀)⁺; C/G(Π₀, Π′₀)⁺; accented C/G(Π₀, Π′₀)⁺ | C versus G and calligraphic versus Gothic letterform. | low |
| 357 | 15–16, interlinear word under « définit » | `\inserted{\unsure{directs\|discrets}}` | One added word above the gap before « de Π₀ »; a curved leader attaches it after the qualified automorphism abbreviation. The reading is uncertain. | low |
| 357 | 16 | `i-automs` | `l-automs`; prefix and abbreviated ending are faint; not expanded in the transcription. | low |
| 357 | 18 | `compactifié` | Letter string appears to be « compactifié »; « complété » is a less likely alternative. | medium |
| 357 | 19, deletion after « où » | `\deleted{\illegible{1}}` | One short word. | low |
| 357 | 20, group receiving the image of u′ | Accented script T/C(Π′₀) | This leaner letter differs visibly from the ornamental C/G above; identification remains uncertain. | medium |
| 357 | 22, struck word after « ss-groupe » | `fermé` | Mostly crossed out; not secure. | low |
| 358 | 1–2, first two homomorphisms | C/G, then accented C/G with accented Π arguments | Ornamental letter identification and the single/double hat count of the very dark caret clusters remain uncertain; accents have not been normalized. | low |
| 358 | 1, after « définissant » | `l'` | Could be « le » written very briefly. | low |
| 358 | 3 | `ouverts` | Word is compressed and faint; only its outline is clear. | medium |
| 358 | 6, first application | P(Π) → P(Π′) | Initial P is overwritten; an earlier D may be underneath. | medium |
| 358 | 8 | `bien` | Could be « vu ». | low |
| 358 | 8, interlinear addition | `alors` | Letter sequence is compressed. | medium |
| 358 | 9, interlinear addition and following verb | `nous voulons` / `montrer` | May instead read « montrons »; the relation between the addition and original verb is uncertain. | low |
| 358 | 10, after « injective » | `...` | Several short strokes may be punctuation or a crossed fragment. | low |
| 358 | 10, right-hand correction | Added « Cela » and deleted « cela signifie » | Order and exact extent of the crossing-out are difficult; two forms of « Cela » occur. | low |
| 358 | 11–12, condition (a) | Double-accented C/G with accented Π₀; single-accented positive groups with accented arguments | Number/attachment of accents and letter family; each visible accent was retained without mathematical correction. | low |
| 358 | 13–15, condition (b) | Double-accented C/G with accented Π′₀; broad accent over positive group; double-accented source group | Accent scope varies visibly across the line. | low |
| 358 | 17, condition (c) | Double-accented C/G(Π₀) hook-arrow double-accented C/G(Π′₀) | Letter family remains uncertain; the arrow has a visible hook-like beginning. | medium |
| 358 | 18, parenthesis | `c'est injectif` | Short word before « injectif » is not completely secure. | medium |
| 358 | 18, deletion after parenthesis | `est` | Crossing obscures the word. | medium |
| 358 | 19, normalizer subscript | Double-accented C (alternative single-accented C) | Tiny accent is not secure; C/G ambiguity also applies here. | low |
| 358 | 19, normalizer argument | Accented C/G with + before (Π₀) | Ornamental letter family; placement of + before the argument is visible and retained. | low |
| 359 | 1, between “même” and `M(π)` | `que` | Very elevated, compressed strokes; not treated as a definite later insertion. | medium |
| 359 | 1, after “est” | `exactement` | `ex.` with a raised `t`; the end is compressed or overwritten, so expansion is not asserted. | low |
| 359 | 2 | `surjectivité` | The first letters are overwritten. | medium |
| 359 | 3, map between the two `A` terms | Double-headed right arrow | A single right arrow with an arched extra stroke above its shaft. | low |
| 359 | 3, 5, 7–8, diagram (7), cancelled final lines | Calligraphic `C` | Calligraphic `G`; the looped glyph is not identified from the mathematics. The single and double hats visible in each occurrence are preserved separately. | low |
| 359 | 6 | `réunies` | The ending is compressed. | medium |
| 359 | 7, left gamma subscript | Deleted illegible symbol before `π₀` | The overwritten subscript cannot be recovered reliably. | low |
| 359 | 8, right quotient numerator | `M` with superscript `♯` | Superscript `*`; a small mark is visible and has not been dropped. | low |
| 359 | 9, first letter reference after “d'avoir” | `(c)` | `(e)`; the letter is overwritten. | low |
| 359 | 12, letter reference after “de” | `(c)` | `(e)`; the small inner stroke could belong to either letter. | low |
| 359 | 13 | `tout` | Faint, abbreviated-looking strokes. | medium |
| 359 | Diagram (7), outer vertical links | Hooked vertical shafts, described physically | Their arrowheads and therefore a fully certain directional encoding are not visible; the middle arrow points down and is bracketed with a question mark. | low |
| 359 | 17 | `concernent` | Final letters are compressed. | medium |
| 359 | 18, final letter reference | `c)` | `e)`; heavily retraced. | low |
| 359 | 19, cancelled passage | `sera` | Initial and final strokes are crossed. | medium |
| 359 | Above line 19, cancelled passage | Inserted `immédiate` | The last letters are unclear; the insertion belongs before “de a)”. | medium |
| 359 | 20, cancelled passage | `assurera` | `implique`; cancellation strokes obscure the letter sequence. | low |
| 359 | 20, cancelled passage, letter reference | `c)` | `e)`; overtracing obscures the letter. | low |
| 359 | 21, very bottom, cancelled passage | Unfinished `C`/`G` glyph after “mod” | No missing argument, hat, or continuation has been supplied. | low |
| 360 | 1 | `Peut-être` | `Peut. être`; the short separating mark resembles a dot. | medium |
| 360 | 4 | `assez` | The ending is only a short stroke. | medium |
| 360 | 7–8 | Double-hatted calligraphic `C` | Double-hatted calligraphic `G`; the same unresolved looped glyph as on scan 359. | low |
| 360 | 9 | `passant` | Several middle letters are reduced to strokes. | medium |
| 360 | 14, 16, diagram (8) | Calligraphic `N` | Ordinary italic `N`; its manuscript form is ornate, and the first occurrence is retraced. | low |
| 360 | 14, before the first `N` | Deleted illegible glyph | Its outer loop survives, but its internal strokes have been cancelled. | low |
| 360 | 15 | `corresp.dants` | Fully written `correspondants`; possible abbreviation points cannot be distinguished from reduced letters with confidence. | low |
| 360 | 17, cancelled line | `soient` | `soit`; the ending is crossed through. | low |
| 360 | 17, first cancelled mathematical symbol | Tilde over single-hatted script `T` with `+` | Tilde over script `T` with `+`; the accent region is overwritten. | low |
| 360 | 17, active continuation | `notées` | `notés`; the ending and agreement are not normalized. | low |
| 360 | 18, immediately before diagram (8) | Full stop | Short dash; a single heavy horizontal mark is visible. | low |
| 360 | Diagram (8), first upper node after `G` | Tilde over single-hatted script `T` with `+` | The base glyph is overwritten and also resembles the earlier `C`; two small points after the plus are described without interpreting them as primes or punctuation. | low |
| 360 | Diagram (8), left vertical link | Hooked shaft, described physically | No clear arrowhead; the diagonal arrow from `G`, middle bracketed arrow, and right vertical arrow point downward. | low |

## 3. Abbreviations and contracted labels met

Expansions in this table are proposals for the notes only. A doubtful abbreviated form remains doubtful in the transcription. The set labels are included for reference, without asserting definitions absent from the supplied pages.

| As written or provisionally read | Proposed expansion / function | Qualification |
|---|---|---|
| `i.e.` | *id est* | Repeated throughout. |
| `NB`, `NB.` | *nota bene* | Punctuation varies. |
| `card` | cardinal / cardinality | Formula (3). |
| `car.` | caractéristique | Doubtful reading on scan 351. |
| `EP`, `EP!` | Euler–Poincaré; the exclamation mark may specify compact supports | Expansion and interpretation only. |
| `tt`, `tte` | tout / toute | Several contracted forms are doubtful. |
| `\overline{\mathrm m}` | même / mêmes | The wavy same-sign; no word substituted in the transcription. |
| `iso`, `iso.`, `isom`, `isom.` | isomorphisme | Local punctuation retained. |
| `qq` | quelque(s) | In the uncertain marginal phrase `en qq sorte`. |
| `Aut ext`, `Autext` | automorphismes extérieurs | Operator spacing retained locally. |
| `Aut` | automorphismes | In the cancelled construction on scan 354. |
| Subscript `lac` | lacets / à lacets | Probable function of the operator qualifier. |
| `ext.` | extérieure | Added on scan 352. |
| `int` | automorphisme intérieur / conjugaison intérieure | Mathematical function label. |
| `Discret`, `Discr` | Labels for sets of discrétifications | Distinct local written forms retained. |
| `discrét.` | discrétification | Scan 357. |
| `tjs`, `tjrs` | toujours | Exact second contraction doubtful. |
| `hom` | homomorphisme(s) | Usually no definite final period. |
| `pt` | point | `du pt de vue`, scan 353. |
| `ss-groupe` | sous-groupe | Exact initial strokes doubtful on scan 353. |
| `prédiscrt.`, possible `prédiscrét.` | prédiscrétification | Spelling of the contraction is doubtful. |
| `Prédiscrt`, `Prédiscr` | Labels for sets of prédiscrétifications | The tall terminal t in (4) is not harmonized with scan 356. |
| `Préarithm` | A label for the next arithmetic quotient, possibly préarithmétifications | Earlier definition not present; operator reading is doubtful. |
| `Arithm` | Label for arithmetic structures or arithmétifications | Earlier terminology would need checking. |
| `comp.` with raised `t`, followed by `ble` | compatible | Exact layout of the contraction is uncertain. |
| Possible `comp.tibles` | compatibles | Alternative to a compressed full word. |
| `l'ens` | l'ensemble | No final period clearly visible. |
| `resp.` | respectivement | Scan 356. |
| `à g.` | à gauche | Describes the torsors. |
| `ssi` | si et seulement si | Scan 356. |
| `Gal` | groupe de Galois | Mathematical operator. |
| `comm.` | commutatif | After `diagramme`, scan 356. |
| Deleted `diagr` or `diagr.` | diagramme | Exact final point uncertain. |
| `i-automs` or `l-automs` | a qualified class of automorphismes | Prefix remains unresolved and is not expanded. |
| `Pb` | problème | Scan 357. |
| `caract.` | caractéristiques | Scan 358. |
| `mod` | modulo | Distinct from conjugation; scan 358 reads `congru mod`. |
| `Norm` | normalisateur | In the displayed definition of M. |
| Possible `ex.` with raised `t` | exactement | Alternative to a compressed full word, scan 359. |
| Possible `corresp.dants` | correspondants | Exact abbreviation points doubtful, scan 360. |

## 4. Legibility and reliability

The ordinary French prose is generally more readable than the mathematical decorations and revisions. The clearer portions include formula (3), much of the normal-subgroup discussion, the elementary conjugation calculation, and the broad three-row structure of the diagram on scan 356. Each page has been read as a whole, transcribed against the ink, and reread; enlarged crops and independent comparisons were used for disputed passages.

The least reliable passages are the diagonal marginal note on scan 351, the interwoven cancellations in the lower half of scan 354, the short interlinear qualifier after the automorphism abbreviation on scan 357, the correction surrounding the injectivity discussion on scan 358, and the cancelled bottom paragraph of scan 359. The case of the principal group letter, the ornamental C/G alphabet, several hat counts, small c/e references, and some diagram arrowheads remain unresolved. Short word endings are marked rather than supplied from agreement or syntax.

This should be treated as a cautious diplomatic working transcription. The explicit doubts and physical descriptions are part of the result; they are not invitations to choose the mathematically expected reading without returning to the scans. The unexpected quotient at the beginning of scan 352 and the prime in the first group listed on scan 355 have been preserved. The final sentence of scan 360 stops where the supplied page stops.

## 5. Research notes — English, separate from the transcription

The sole documentary source for these items is Grothendieck (1981), located by the scan and approximate line specified in each item. Statements of what a proof would need are proposed checks, not findings that earlier or later parts of the manuscript lack such a proof. Authorial questions, asserted claims, conditional consequences, and the transcriber's own ideas are distinguished. An own idea is a suggestion for investigation or a formal example, not a claim of novelty.


### Scan 351

- **351, formula (3); unpursued implication.** The visible relation `2g′ − 2 + card I′ = n(2g − 2 + card I)` suggests checking which discrete invariants are forced by passage to the subgroup under discussion. The preceding hypotheses are outside this excerpt; no assertion about ramification or the class of coverings is supplied here (Grothendieck, 1981, scan 351).
- **351, cohomology paragraph; unproved claim.** “De façon évidente” introduces restriction of discrétifications, and the oriented case is referred to “un peu de cohomologie.” A proof would need to identify the two displayed cohomology groups and the trace isomorphism, and justify the factor `nθ⁻¹` with the manuscript's conventions (Grothendieck, 1981, scan 351).
- **351, final paragraph; conjecture / question.** “Il n'est pas clair pour moi à première vue” asks about both surjectivity and injectivity of `Discret(π) → Discret(π′)`. The final, revised sentence relates injectivity to equality of commensurable discrétifications; its cancelled wording should not be treated as a completed proof. Scans 352–353 subsequently announce injectivity and discuss a proposed obstruction to surjectivity, whose construction is attempted in scan 354 (Grothendieck, 1981, scan 351).

### Scan 352

- **352, lines 3–8; conjecture.** Under the heading “Conjecture,” the restriction map is asserted to be injective, with image characterized by factorization of the finite quotient's outer action through the discrete group written `𝒯(Π′₀)` and, “en fait,” its positive subgroup. The two assertions—injectivity and the image condition—should be assessed separately (Grothendieck, 1981, scan 352).
- **352, inserted right-side note; unproved claim.** “En d'autres termes” proposes an equivalent description involving `int(hg)(Π′₀) ⊂ Π′₀` and a normalizer product. Proving the equivalence requires checking exactly how outer representatives change under multiplication by an element of Π′; the first factor in the written product remains palaeographically uncertain (Grothendieck, 1981, scan 352).
- **352, middle and end; unproved claim.** “Montrons qu'elle est suffisante” reconstructs an extension from the outer action using the displayed centre condition. The final sentence explicitly leaves compatibility with the “structure à lacets” to be checked, so reconstruction as a profinite group is not the whole claimed result (Grothendieck, 1981, scan 352).
- **352, lines 13–22; own idea.** Separate the proposed descent into an extension problem, a completion problem, and a compatibility problem for the designated lacets, and test whether the same uniqueness statement holds at all three stages. **Confidence: medium**, because the manuscript itself distinguishes the group structure from the lacet structure, but the definitions before this excerpt are unavailable (Grothendieck, 1981, scan 352).

### Scan 353

- **353, lines 1–7; unproved claim.** The proposed lacet structure is to be recovered by taking the lacet subgroups and “leurs Centralisateurs,” first in Π and then in Π₀. The words “on devrait trouver” leave a verification: whether these centralizers give exactly the designated local subgroups and respect restriction to Π′₀ (Grothendieck, 1981, scan 353).
- **353, lines 7–12; conjecture / expectation.** “J'ai l'impression que ça ne doit pas être très vache à prouver” is followed by a proposed sufficient general statement: a “sans torsion” extension of a finite group by a group with lacets should again carry a canonical lacet structure. The scope of “groupe à lacets” and the canonicity claim need to be recovered from earlier definitions before testing this statement (Grothendieck, 1981, scan 353).
- **353, corollary; unproved claim.** “En tous cas” announces injectivity of `Discret(Π) → Discret(Π′)`. Its dependence on the uniqueness/normalizer argument should be checked separately from the existence of a compatible lifted lacet structure. The unfinished compatibility step does not, by itself, show that the injectivity argument is incomplete (Grothendieck, 1981, scan 353).
- **353, NB; conjecture / expectation.** “Elle ne doit pas tjs être bijective” proposes failure of surjectivity through finite outer actions which do not factor through the discrete `𝒯(Π′₀)`. The following scan begins an attempted construction, so this paragraph is a proposed obstruction and not yet a worked example (Grothendieck, 1981, scan 353).
- **353, final paragraph; own idea.** Test whether failure to preserve an embedded discrete subgroup can distinguish two outer actions whose associated profinite extensions are isomorphic. **Confidence: medium**, because this is suggested by the explicit factorization condition, but an example still needs the lacet and torsion conditions checked (Grothendieck, 1981, scan 353).

### Scans 354–356

#### R354.1 — Scan 354, approximately lines 4–12 — unproved claim

Grothendieck writes that after conjugating the finite action one obtains an extension “isomorphe à” the original profinite group, whose chosen discretification is nevertheless not induced from the larger group. A proof needs an explicit identification of the two extensions, verification that the lacet structures correspond under that identification, and a precise argument for the final noninducibility assertion. The cancelled construction below should not be treated as a completed proof of all three steps (Grothendieck, 1981, scan 354).

#### R354.2 — Scan 354, final construction and last line — unproved claim

The surviving ending reads, with uncertainty in the abbreviation, “Un tel γ existe tjrs....” The rewritten criterion appears to ask for conjugation taking the finite group outside the discrete Teichmüller subgroup, and a later addition refers to failure to stabilize a conjugated discrete subgroup. Establishing the existence claim therefore requires both the exact ambient group and all restrictions on the finite action to be recovered; the visibly cancelled attempts do not settle that issue on this leaf (Grothendieck, 1981, scan 354).

#### R354.3 — Scan 354, inserted noncontainment criterion — own idea

**Confidence: high for the formal check; uncertain as an objection in context.** Test the criterion with the trivial finite group: conjugation still sends it to the trivial subgroup, so it cannot leave a subgroup containing the identity. This suggests checking whether nontriviality or another restriction on the action was imposed earlier; it is not offered as a counterexample to hypotheses outside these supplied leaves.

#### R355.1 — Scan 355, approximately lines 8–12 — conjecture

The words “je présume” introduce the expectation that two discretifications “adhérents” to one another continue to define the same prediscretification after restriction. The relevant topology and the precise equivalence relation on discretifications need to be identified before proving that restriction respects this relation. A continuity statement alone would need to be matched to the manuscript's intended meaning of mutual adherence (Grothendieck, 1981, scan 355).

#### R355.2 — Scan 355, display (4) and following line — conjecture

Within the same presumptive passage, Grothendieck expects the induced comparison of oriented prediscretification sets to be “encore bijective.” Injectivity and surjectivity are distinct requirements: the former rules out distinct upper-level classes merging on restriction, while the latter asks for extension of every class at the lower level. The displayed superscript is thickly retraced and is separately marked as a palaeographical doubt. Scan 360 later questions the group conditions required for this comparison, especially the surjectivity condition, without proving their failure (Grothendieck, 1981, scans 355, 360).

#### R355.3 — Scan 355, display (5) — conjecture

The further phrase “passe à son tour au quotient” proposes a bijection on the next, arithmetical quotient. This requires compatibility with an additional equivalence relation, beyond the well-definedness required for (4). The earlier definition of the label read as *Préarithm* should be checked before identifying this quotient with any familiar arithmetic moduli construction. Scan 360 subsequently casts doubt on the required comparison properties, especially surjectivity (Grothendieck, 1981, scans 355, 360).

#### R355.4 — Scan 355, display (6), continuing at the top of scan 356 — conjecture

For corresponding Σ and Σ′ he expects “un isom canonique” between the attached groups, compatible with their actions on the respective sets. The continuation calls these sets left torsors, so a proof would need to construct the group comparison without auxiliary choices and verify equivariance of the torsor comparison. The group glyph is read as a doubled Gamma and its exact alphabet is recorded as uncertain. The required conditions are analysed further in scans 358–359 and questioned in scan 360 (Grothendieck, 1981, scans 355–356, 358–360).

#### R355.5 — Scan 355, first paragraph — own idea

**Confidence: high for the elementary group manipulation; applicability requires the stated factorization.** Test whether a factorization Π = Π′Π₀ converts a Π-conjugating element into a Π′-conjugating element, since the Π₀ factor preserves Π₀ itself. This is a way to examine the opening concern about changing the conjugating group, not a new result; scan 357 carries out this elementary manipulation, conditional on the displayed factorization (Grothendieck, 1981, scans 355, 357).

#### R356.1 — Scan 356, approximately lines 1–5 — unproved claim

The parenthesis “qui sont resp. des torseurs à g.” treats the two compatible-prediscretification sets as torsors. The action must be specified, with freeness and transitivity established or cited from earlier manuscript pages. For the comparison proposed on the preceding leaf, these actions also need to be related by the claimed canonical group isomorphism (Grothendieck, 1981, scan 356).

#### R356.2 — Scan 356, approximately lines 5–8 — conjecture

“En même temps, on trouvera” introduces an expected equivalence for a property whose word is tentatively read as “unique,” immediately described in terms of invariance under the indicated doubly hatted Teichmüller group. A proof should compare the stabilizers or fixed-point conditions of Σ and Σ′ under the two indicated actions. Because the property word is doubtful, this note deliberately does not replace it with a more conventional mathematical term (Grothendieck, 1981, scan 356).

#### R356.3 — Scan 356, approximately lines 9–14 and diagram — conjecture

The “conjecture fondamentale” is invoked to support descent of the discretification comparison through two quotients and a commutative diagram. Its exact earlier formulation is needed: this page refers to a group identification involving the Γ with indices g and ν and the displayed Galois group, but does not restate the full conjecture or prove the implication. The tentative verb is retained as *aurait* rather than being turned into an unconditional assertion (Grothendieck, 1981, scan 356).

#### R356.4 — Scan 356, lower square and final paragraph — unpursued implication

The assertion “le carré inférieur est cartésien” would identify P with the fibre product A ×₍A′₎ P′ for the indicated maps, and hence identify the fibre over a chosen element of A with the corresponding fibre in P′. This describes the precise compatible-lifting statement to prove. Grothendieck explicitly separates it from “l'injectivité ou … la bijectivité” of A → A′, so those stronger claims should not be read into the square (Grothendieck, 1981, scan 356).

#### R356.5 — Scan 356, qualification after the diagram — own idea

**Confidence: high; elementary set-theoretic example.** To keep the final qualification explicit, take a two-element set A mapping to a singleton A′, any nonempty P′ over A′, and P = A × P′. The resulting lower square is cartesian while A → A′ is not injective, illustrating why cartesianness by itself does not settle the stronger question left open here; this is only a formal toy model, not an example of the manuscript's arithmetic structures.

### Scans 357–358

1. **Scan 357, approximately lines 8–11 — unproved claim (subsidiary equality).** The assertion « on aura Π = Π′ · Π₀ » supports the displayed conjugacy calculation. These lines give the ensuing calculation but do not supply a justification of this equality; a proof would need the precise earlier hypotheses on Π₀ and Π′, for example whether density and finite index are available. This is a note about the missing local justification, not a claim that the equality is false (Grothendieck, 1981, scan 357).

2. **Scan 357, approximately lines 12–18 — conjecture / expectation.** « Tâchons de procéder de [m̄] » and « en écrivant si possible u = u′u₀ » propose extending the elementary conjugacy argument by a factorization involving the completion of a subgroup stabilizing Π′₀. The displayed factorization is explicitly tentative. A proof would need to identify the precise action and prove the needed product or orbit statement; the uncertain ornamental letters should be resolved before formulating it as a theorem (Grothendieck, 1981, scan 357).

3. **Scan 357, approximately lines 21–23, continuing on scan 358 — unproved claim.** « il n'y a aucun Pb si Π′ est un ss-groupe caractéristique » introduces a restriction homomorphism and its completed version. The local text does not prove all of the compatibility assertions implicit in passing to the completion. A careful proof should distinguish existence of restriction, preservation of the additional structure, and continuity or extension to the indicated completion (Grothendieck, 1981, scans 357–358).

4. **Scan 358, approximately lines 2–7 — unproved claim.** « les sous groupes [ouverts] caract. de Π sont cofinaux » is used to reduce to the characteristic case. The word « ouverts » is a doubtful reading, and the cofinality assertion depends on hypotheses not restated here. A proof would have to establish the appropriate invariant neighbourhood basis and show that the desired assertions are preserved through this reduction (Grothendieck, 1981, scan 358).

5. **Scan 358, approximately lines 11–17 — unpursued implication.** The circled (a), (b), and (c) separate inverse-image control of a positive subgroup, representation, modulo the indicated positive subgroup, by an element of the source image, and preservation of a normalizer. Their formulation suggests that injectivity, surjectivity, and descent to the next quotient require distinct group-theoretic statements. Scan 359 develops the corresponding quotient criteria, and scan 360 questions whether properties (a), (b), and (c) hold: (a) remains “plausible”, whereas (b) is “voire douteuse”; the validity of a criterion and the assertion that its hypotheses hold here are distinct (Grothendieck, 1981, scan 358).

6. **Scan 358, approximately lines 17–18 — unproved claim.** The parenthetical « NB il est immédiat que [c'est] injectif » asserts injectivity of the preceding homomorphism. A proof would need the exact definition of the groups and to show that an element whose restriction is trivial was already trivial; the page does not establish that step. The short phrase before « injectif » is itself marked doubtful in the transcription (Grothendieck, 1981, scan 358).

7. **Scans 357–358 — own idea; confidence: medium.** A useful first test is to separate the proposed factorization u = u′u₀ from the cofinality reduction and examine finite quotients in which the stabilizer action and orbit map can be written explicitly. Failure of the finite orbit statement in a model satisfying the necessary hypotheses could locate the obstruction, while success would only motivate further work and would not prove the completed assertion. The reason for this suggestion is the explicit factorization and inverse-image/congruence criteria on these pages; no claim of novelty or established validity is made.

### Scans 359–360

1. **Scan 359, lines 1–5; kind: unproved claim.** The conditions labelled (d) and (e) use an “image inverse” statement for the `M` groups and congruence “mod” the target `M` group. A proof of the claimed injectivity/surjectivity interpretations would need to specify the ambient homomorphism and its coset action carefully, since several of the letter references and one superscript in the adjacent quotient display remain palaeographically uncertain.

2. **Scan 359, lines 6–12; kind: unproved claim.** The manuscript says the canonical homomorphism “est iso” under the listed conditions and then separates conditions used to define the map, establish injectivity, and obtain bijectivity. The proof obligation is to check all three stages, including the relevant normal subgroups and the kernels of the induced quotient maps; the unclosed parenthesis and uncertain `(c)/(e)` reference are left as written in the transcription.

3. **Scan 359, diagram (7) and lines 17–18; kind: conjecture.** The middle vertical arrow is surrounded by brackets with a question mark, and the text concludes “à charge de prouver”. Thus compatibility of the intermediate `M` groups, together with the additional labelled properties, is still a task at this point rather than an established consequence of the displayed outer maps.

4. **Scan 359, cancelled lines 18–21; kind: unproved claim.** The cancelled passage begins “D'ailleurs d)” and attempts to derive this condition from another labelled condition and a congruence statement about elements of the distinguished plus subgroup. Because the passage is crossed through and unfinished, it should be studied as an abandoned proof attempt; its dependency on the element-congruence assertion needs independent verification.

5. **Scan 360, lines 1–6; kind: conjecture.** Grothendieck asks whether the properties might be “tout à fait fausses”, while regarding the injectivity condition as “plausible” and the surjectivity condition as “voire douteuse”. This sharply limits the status of the preceding expectations: a later check should distinguish the two directions and should not report the displayed maps as bijections on the strength of these pages.

6. **Scan 360, lines 7–12; kind: unproved claim.** The concern is that one of the double-hatted groups can be “beaucoup plus petit” than its primed counterpart; the proposed diagnostic is quotienting by `\widehat{\pi}'_0=\pi'`. The assertion that this subgroup lies in the smallest displayed group and is invariant in the largest requires verification for the actual actions and inclusions, before the quotient diagram can be used to infer an obstruction.

7. **Scan 360, lines 13–17 and diagram (8); kind: unproved claim.** The quotients in the lower row are identified with the three displayed `T`/`N` groups, while those in the upper row are described as “des extensions” by the finite group `G=\pi_0/\pi'_0\simeq\pi/\pi'`. A proof would need to produce the exact sequences, justify this finite-group identification, and verify that the inclusions and the diagonal map from `G` respect those sequences.

8. **Scans 359–360, diagrams (7)–(8); kind: unpursued implication.** The appearance of a second bracketed question mark after quotienting suggests that the compatibility problem for the intermediate groups survives passage to the quotient. The present excerpt ends before the consequence introduced by “qui montre que” is stated, so the intended conclusion cannot be recovered from this unit alone.

9. **Scan 359, canonical quotient display and diagram (7); kind: own idea.** Formulate a purely group-theoretic lemma separating existence, injectivity, and surjectivity of the induced quotient map, with explicit preimage and image conditions, and then match each manuscript letter to that lemma only after the uncertain readings are resolved. **Confidence: high as a method,** because the manuscript already separates these three tasks; this is a proposed way to check the argument, not an assertion that its hypotheses hold here.

10. **Scan 360, diagram (8); kind: own idea.** Look for a conjugacy or quotient invariant of an element in a lower-row group that could obstruct its being represented by the image of the upper-row extension; begin with the visible finite subgroup `G` and its normalizers. **Confidence: medium,** because the manuscript identifies a possible disparity between the groups and explicitly introduces `G`, but supplies no example establishing failure of surjectivity in this excerpt.

## Reference

Grothendieck, A. (1981). *La Longue Marche à travers la théorie de Galois* [Handwritten manuscript; Montpellier archive, cote 140-2; supplied scans 351–360, with visible authorial folios 178–182]. Université de Montpellier.

The source identification and date are taken from the supplied task and images. All quotations in these notes are from those images; doubtful readings are identified in the transcription and doubt table.

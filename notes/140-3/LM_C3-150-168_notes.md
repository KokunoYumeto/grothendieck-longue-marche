# LM_C3-150-168 — transcription apparatus and research notes

## 1. Source, pagination, and editorial conventions

This apparatus accompanies the diplomatic French transcription of all nineteen supplied scans, numbered **150–168 by filename**. The source attribution and date are those supplied with the assignment: Alexander Grothendieck, *La Longue Marche à travers la théorie de Galois* (1981), Montpellier archive, cote 140-3, archive file “pages 293–650.” All readings and quotations derive from the supplied images. No published transcription or external text has been used to complete a reading.

The filename number differs by one from the small number at the lower left of each manuscript image and from the printed archive footer. The transcription uses the filename number in `\scanpage`. Central handwritten manuscript pagination is recorded in `\mspage` only where visible; the lower-left numerals are preserved in `\margin`, without assigning their hand or provenance. The printed institutional footer outside the manuscript's black frame is excluded. The visible jump from manuscript page 370 to 380 is preserved.

| Filename scan | Central manuscript numeral | Lower-left numeral |
|---|---|---|
| 150 | — | 149 |
| 151 | 365 | 150 |
| 152 | — | 151 |
| 153 | 366 | 152 |
| 154 | — | 153 |
| 155 | 367 | 154 |
| 156 | — | 155 |
| 157 | 368 | 156 |
| 158 | — | 157 |
| 159 | 369 | 158 |
| 160 | — | 159 |
| 161 | 370 | 160 |
| 162 | — | 161 |
| 163 | 380 | 162 |
| 164 | — | 163 |
| 165 | 381 | 164 |
| 166 | — | 165 |
| 167 | 382 | 166 |
| 168 | — | 167 |

Uncertain readings remain inside `\unsure{…}`; alternatives are separated by `|`. `\illegible{n}` records an estimated number of unreadable words or, within formulae, compact groups of symbols. Those estimates do not assert that the obliterated material can be segmented precisely. Cancellations, insertions, underlining, and marginal material are retained; nested deletions represent revisions inside an already cancelled passage. Placement within a formula or paragraph follows visible attachment marks where they are recoverable, and uncertainty about a difficult attachment is noted below.

Original equation numbers, including repetitions, are retained. Apparent algebraic errors, changes of sign, overwritten indices, and unfinished sentences have not been silently corrected. Slash fractions remain in that form where the scope of the handwritten division is ambiguous. Typographical line wrapping is editorial; the source's paragraph sequence is retained. The LaTeX file is a fragment with no preamble or macro definitions, as requested.

## 2. Table of doubts

Locations refer to approximate physical lines, nearby wording, or the manuscript's equation numbers, rather than LaTeX source lines. Confidence concerns the reading of the ink, not the truth of a mathematical statement. Repeated ambiguous glyphs are sometimes grouped in one row while remaining marked at their occurrences in the transcription. A few high-confidence rows retain the outcome of a second reading of a previously doubtful or mathematically surprising passage.

### Scans 150–154

Locations use approximate physical lines or, where more reliable, the manuscript's own equation numbers. “No recoverable alternative” means that no competing reading could responsibly be proposed. Repeated occurrences of the same ambiguous glyph are listed together; the uncertainty remains marked at each occurrence in the transcription.

| Scan | Approximate line or location | Reading in transcription | Alternatives or issue | Confidence |
|---|---|---|---|---|
| 150 | (57), first row, twice | `\nu` | The overwritten strokes can resemble a gamma; the surviving letter is uncertain. | medium |
| 150 | (58), cancelled material to right of box | `\deleted{\illegible{3}}` | Several symbols obliterated by heavy cancellation. | low |
| 150 | Unnumbered matrix below (58), left prefactor | `\varepsilon` | Apparent scalar before the left matrix is retained; whether it is cancelled is unclear. | low |
| 150 | Same matrix, right prefactor | `\varepsilon` | Small overwritten letter at equality. | medium |
| 151 | Opening sentence, after “comme” | `\deleted{\illegible{1}}` | A short horizontal cancellation with no reliably recoverable word. | low |
| 151 | (61), cancelled first-row note | `\deleted{\illegible{2}}` | Overwritten symbols cannot be separated. | low |
| 151 | (61), cancelled note before `\mu U=\varepsilon` | `D=1/\mu` | `D` and the fraction are crossed through. | low |
| 151 | (61), between minus sign and `(\mu-1)` | `\deleted{\illegible{1}}` | A densely cancelled symbol. | low |
| 151 | (62), second line, first letter | `c` | Resembles `s`; a conjectural identification is explicitly marked. | medium |
| 151 | (62), fourth line, sign before `ab` | `-` | `+` is also possible; no mathematical correction has been made. | low |
| 151 | Paragraph after (62), “solutions … équations” | `aux` | Final stroke does not clearly resolve the complete word. | medium |
| 151 | Theorem, matrix-name glyph | `\xi` | `\zeta`; this tall cursive Greek glyph recurs in scans 152 and 153. | medium |
| 151 | Small mark between theorem's two formulae | `(+)` | Could be a reference/caret mark rather than the literal plus sign. | low |
| 152 | (56), left matrix-name glyph | `\xi` | `\zeta`. | medium |
| 152 | Upper left marginal note, opening verb | `démontre` | The medial strokes are compressed; no secure competing verb. | medium |
| 152 | Upper left marginal note, after “d'inclure” | `aussi la` | Faint/oblique words at the edge of the note. | low |
| 152 | Paragraph after `U=t^2+u^2`, before `1/\mu` | Deleted `\mu` | Densely overdrawn symbol. | low |
| 152 | Same paragraph, `\varepsilon(…+u^2)` | `t^2` | First term indistinct. | medium |
| 152 | Transition after the mod-4 proof, between “On voit” and “de façon” | `en` | `un`; a short uncancelled cluster is visible and retained without regularizing the sentence. | low |
| 152 | Paragraph below `D=\delta(…)`, after “On” | Deleted `pourrait donc` | Crossed-out phrase; endings are doubtful. | low |
| 152 | Following line, before “premiers p” | `les nb` | The initial short cluster could include a quantifier or different abbreviated wording. | low |
| 152 | Character notation in prose | `\varepsilon_p` | `\beta_p`; the handwritten letter is overwritten. | low |
| 152 | (63), first character-value notation | `\varepsilon_3(\mu)` | `\beta_3(\mu)`. | low |
| 152 | (63), second character-value notation | `\varepsilon_2(\mu)` | `\beta_2(\mu)`. | low |
| 152 | Last line, “µ mod …” | `3` | `2`; overdrawn numeral. | low |
| 152 | Lower left marginal product, first sign set | `\{\pm1\}` | Overwriting partly obscures the first set. | medium |
| 153 | Opening line before “cf” | `\deleted{\illegible{1}}` | A small scratched-out word or symbol. | low |
| 153 | Initial formula for `g`, after `(l_0^\nu f)^{-1}` | `\xi` | `\zeta`. | medium |
| 153 | Left marginal note, matrix-name glyph | `\xi` | `\zeta`. | medium |
| 153 | Left marginal note, after `\alpha` | `\deleted{\illegible{1}}` | Overwritten cancelled material. | low |
| 153 | Left marginal note, last two lines | `au choix`, then `\illegible{2}` | Several oblique words remain unresolved; do not use this passage as an exact quotation. | low |
| 153 | Unnumbered product for `g`, middle underbrace label | `l_1^\nu` | `l_0^\nu`; the subscript is minute. | medium |
| 153 | Same product, lower-left entry of `\rho(f)` | `t+u-r-s` | Heavy overwriting; individual signs/letters are uncertain. | medium |
| 153 | Same product, lower-right entry of `\rho(f)` | `r-t` | Overwriting on the first letter. | medium |
| 153 | Next matrix, lower-left entry | `\mu(t+u)-r-s` | The minus sign and following letters are partly overdrawn. | medium |
| 153 | Paragraph after (65), “α₀ ou …” | `\xi` | `\zeta`. | medium |
| 153 | Final paragraph, after “une matrice” | `\deleted{\illegible{1}}` | A scratched-out letter or symbol. | low |
| 153 | Last paragraph, second profinite group | `\widehat{\mathcal G}_{0,3}` | Exact alphabet/shape of the capital group symbol remains uncertain. | medium |
| 154 | First prose line, deleted word | `satisf` | The ending is not visible enough to expand or normalize. | low |
| 154 | Insertion after “que u” | `le initial` | `l'initial`; the apparent two-word spelling is retained as an alternative. | low |
| 154 | After (68), deleted phrase | `on devrait avoir` | The cancellation obscures the middle letters. | low |
| 154 | Immediately before (69) | Deleted `d'où` | The horizontal stroke may be cancellation or emphasis. | low |
| 154 | Final paragraph, verb before `(69)` | `dégagé` | `dégoté`; neither reading is certain enough to print without a doubt mark. | low |
| 154 | (70), factor between `p` and `+q\rho` | `\mathrm{id}` | Strongly overwritten identity symbol; no secure alphabet can be assigned. | low |

### Scans 155–159

| Scan | Approximate line or location | Reading in the transcription | Alternatives or unresolved feature | Confidence |
|---|---|---|---|---|
| 155 | After (71), parenthesis | “où” | The short connective is lightly formed. | medium |
| 155 | After (71), determinant | $\alpha$ | The letter has a dark correction at its lower right; an additional mark or index cannot be excluded. | medium |
| 155 | Second numbered display | (72) | The number is overwritten, though the later reference to 72 is legible. | medium |
| 155 | Display with reference “(52 et 58)” | $cd$ | The first part of this product is overwritten. | medium |
| 155 | First proposed expressions for p and q | Deleted, illegible token before $\mu c$ | One compact cancelled mathematical token; no dependable reading. | low |
| 155 | Parenthesis before (73) | “s'opposant” | The end of the word and its compressed internal strokes are uncertain. | medium |
| 155 | Same parenthesis | “à” | May be a colon; the mark looks like two separated short strokes. | low |
| 155 | Immediately after that parenthesis | “je trouvais” | The opening letters have been retraced; “trouvais” is clearer than the pronoun. | medium |
| 155 | Before (73), “bien …” | “sûr” | End of the word overlaps a hooked mark, possibly punctuation. | medium |
| 155 | Last sentence, after (74) | $\varepsilon'_2$ | $\varepsilon'$; an apparent subscript has been heavily touched up. | low |
| 155 | Lower-left marginal note | “désignant un scalaire” | The note is diagonal, cramped, and overlaps the main text; the final clause is the least secure part of the note. | low |
| 156 | Opening sentence after the first display | Deleted “donc” | The crossed word may be another short connective. | low |
| 156 | First commutator product, second factor | Lower-right entry $1$ | The digit is thickly retraced. | medium |
| 156 | First underbraced product | Lower-right entry $u-t$ | $-u-t$; a dark leading stroke may belong to the letter u. | low |
| 156 | Second expanded matrix, upper-left entry | $t(u+t)$ after $1/\mu+$ | Several strokes are overwritten; an additional cancelled letter may be present. | low |
| 156 | Last expanded matrix, lower-left entry | Cancelled t after u | The mark is dark and its status as cancellation rather than retracing is uncertain. | low |
| 156 | Same entry | Cancelled exponent 2 on the final t | A thick mark appears at exponent height; its cancellation status is uncertain. | low |
| 156 | Left marginal reference | “appliquer” | The connected letters are faint; the reading is more secure at the beginning than at the ending. | medium |
| 156 | End of the identity below $[u,\rho]=g$ | “−!” | An exclamation mark alone; there is a small preceding dash or pen stroke. | low |
| 156 | “dans le … où” | Deleted “cas” | The word is crossed through and overdrawn. | medium |
| 156 | Before the similarity identity | “similitude” after underlined “anti” | The final part is overwritten, with approximately one unreadable word or token following. | low |
| 156 | “Mais … la matrice” | Deleted “et” | The small cancelled word could be a different connective. | low |
| 156 | Right marginal comment beside τ∞ | “orthog.” | The abbreviation's ending is compressed. | medium |
| 156 | Below τ∞ | “cas-type” | The first syllable and the connection to “type” are not fully distinct. | medium |
| 156 | Last display, diagonal factor | Upper-left entry $1$ | $-1$; a hooked leading stroke resembles a minus. | low |
| 156 | Last display, final matrix | Upper-left entry u | $-u$; a leading stroke may be a minus rather than part of u. | low |
| 156 | Same matrix | Upper-right entry t | $-t$; the sign has been thickly retraced. | low |
| 157 | First commutator display, bracketed matrix | Upper-left entry u | A small overdrawn mark below or beside it might be an index or a correction. | medium |
| 157 | Same display, before the inverse matrix | $1/\mu$ | $\mu$; the small mark above μ is visible but its role is not secure. The later factors have not been used to regularize it. | low |
| 157 | Second underbraced product | Upper-right entry u | $-u$; the leading stroke could be a sign. | low |
| 157 | Expanded matrix, lower-left entry | $-(u^2+t^2)$ | The minus and opening parenthesis are crowded into the matrix delimiter. | medium |
| 157 | Before “a-t-on bien” | Deleted “d'où” | “donc”; the cancellation prevents a confident distinction. | low |
| 157 | Beside/below the tentative equality $[u,\rho]=-g$ | “i.e.” | A small dark handwritten insertion; possibly another short word. | low |
| 157 | Before “équivaut à” | “prévue” | “précise”; the middle letters are compressed. | medium |
| 157 | Last paragraph | “tjs” | The middle abbreviation stroke is not distinct. | medium |
| 158 | (75), superscript on the diagonal factor | $\alpha_2$ | The diagonal entries are rewritten and the exponent may belong to an earlier state of the expression; it remains visible. | low |
| 158 | Opening of corollary | “du” | The connective is overwritten. | medium |
| 158 | After the group of loops | “commutant” | The ending is compressed into a long stroke. | medium |
| 158 | Corollary, both occurrences of the group with subscript 3 | $\mathfrak S_3$ | $\mathcal S_3$; the handwritten alphabet cannot be determined securely from this page alone. | low |
| 158 | Corollary, both occurrences of the extended group | $\widehat{\mathcal G}_{0,3}^{+}$ | $\widehat{\Gamma}_{0,3}^{+}$; the large ornate letter is ambiguous. Hat, indices, and plus are retained. | low |
| 158 | Bottom, adjective after “autom.” | Deleted “intérieur” | The cancelled form could have a plural ending. | low |
| 158 | Same place, replacement above the cancelled form | “intérieur” | “intérieurs”; replacement and deletion overlap. The nearby word “matrice” has been treated as an insertion into “une matrice u”. | low |
| 159 | Upper-left marginal note | “corollaire” | The middle letters are joined and pale. | medium |
| 159 | End of upper marginal note | “de”, followed by one illegible token | The text runs into the main paragraph; the last token might be a symbol rather than a word. | low |
| 159 | After “définis ainsi” | Deleted “On a” | A compact overwritten opening; exact letters remain uncertain. | low |
| 159 | Before “L'observation analogue” | One illegible deleted word | No reliable lexical reading. | low |
| 159 | Before “vecteur (c,d)” | One illegible deleted word | A descending initial stroke is visible, but the word is not recoverable. | low |
| 159 | Last prose line | “l'élément” | The article has been overdrawn; a discarded “le” may remain underneath. | medium |

### Scans 160–164

Locations refer to manuscript baselines approximately; equation numbers and positional descriptions are more reliable than a continuous line count in the heavily revised passages. The scan identifier is the filename identifier, not the printed archive footer. “No secure alternative” means that no additional lexical or mathematical restoration is proposed. Estimates in `\illegible{n}` count short mathematical units as well as words when necessary.

| Scan | Approximate line / location | Reading in the transcription | Alternatives / unresolved issue | Confidence |
|---|---|---|---|---|
| 160 | l. 1, after “et” | One deleted unit and one surviving illegible word | The visible word-ending does not securely identify the word; no contextual completion | low |
| 160 | ll. 6–8, deleted sentence | “envie” | No secure alternative beneath the strike | medium |
| 160 | ll. 6–8, deleted sentence | “mes / mon”, “calculs / calcul” | Possessive and final plural stroke are unclear | low |
| 160 | Upper-left marginal NB | “valable” | Could not establish every letter | medium |
| 160 | Upper-left marginal NB | “moyennant” | No secure alternative; connected strokes crowded | medium |
| 160 | First long matrix product after (80) | Exponent `-\nu / -1` on `\ell_0` | The final stroke can look like the numeral 1 | medium |
| 160 | Same product, upper-right entry of the rightmost matrix | Deleted `+d` after `c` | Black cancellation conceals most of the old entry | low |
| 160 | Final display, first expanded term | `\mu urt / \mu turt` | Extra dark stroke immediately after `\mu` may be a redundant or deleted `t` | low |
| 160 | Final display, note above equality | “si `\varepsilon_2=+1`” | Last sign/numeral and exact attachment are compressed | medium |
| 160 | Final display, inside `s(...)` | `\varepsilon_2u^2 / \varepsilon_2\mu u^2` | Presence of a separate `\mu` cannot be established; none supplied silently | low |
| 160 | Final display, overbraced factor | `-st+ur / st+ur` | First sign is overwritten; algebra was not used to choose it | low |
| 161 | Top line, note above first equality | “si `\varepsilon_2=1`” | Tiny note; arrow attachment is visible but letters are compressed | medium |
| 161 | Matrix before (82), upper-right entry | `\varepsilon_2t` | `t` has been overwritten | medium |
| 161 | Above equality to `\delta\uline{u}` | Deleted “si `\varepsilon_2=1`” | Cancellation and initial word are crowded | medium |
| 161 | (82), first scalar | `\delta` | Overwritten symbol, whereas the repeated scalar later in the line is clearer | medium |
| 161 | To the right of (82) | Deleted “si `\varepsilon_2=1` (i.e. `\mu\equiv1 (4)`)” | Cross-hatching obscures the lower clause; exact extent of cancellation is not completely certain | low |
| 161 | Before (83) | “compte” and one deleted illegible unit | Multiple strokes overlap the phrase “compte tenu de (75)” | low |
| 161 | (83), before `(t\sigma_\infty+u)` | One deleted illegible mathematical unit | Could be an earlier scalar or symbol; no reconstruction retained | low |
| 161 | (83), appended condition | Deleted “si `\varepsilon_2=1`” | Heavy cancellation, no secure alternative | medium |
| 161 | (83), after formula defining `\alpha` | One deleted illegible unit | Black isolated overwritten mark | low |
| 161 | Expanded right-hand product under (84) | Lower-right `d` in `\alpha_0` | The letter has an additional overwritten stroke | medium |
| 161 | Left-hand computation below (84) | Two deleted illegible clusters, estimated four and seven units | Scribbling hides intermediate matrices; the surviving first expansion and last matrix have been retained | low |
| 161 | Text below (84) | “était” | The word was overwritten; no confident alternative | medium |
| 161 | Following line | “contenu / condition” | “contenu” fits the visible strokes better; the long central stroke is obscured by the preceding descender | medium |
| 161 | Final Remarque | “par / pr” | Whether an abbreviated form or compressed full word was written is uncertain | medium |
| 161 | Final Remarque | “biais” | Short, faint connected letters | medium |
| 161 | Final Remarque | “valables” | Final plural stroke uncertain | medium |
| 162 | l. 1 | “formulable / formulables” | Final plural stroke uncertain | medium |
| 162 | l. 3 | “compréhensives” | Internal compressed letters; the word has not been replaced by “compréhensibles” | medium |
| 162 | First displayed commutator | Subscript `0 / 3` on `\alpha` | The handwritten subscript looks different from some later zeros | low |
| 162 | Following line, first matrix group | `\mathrm{Gl}` | Initial `G` is overwritten; case of the handwritten `l` is not completely secure | medium |
| 162 | After “est donné” | Deleted “et” plus one illegible unit, replaced by “ainsi que” | The rest of the old wording lies under the insertion | low |
| 162 | (*), parameter-group sentence and following display | `\mathcal{E}_0 / \varepsilon_0` (three occurrences) | Calligraphic capital and Greek-letter forms cannot be securely distinguished; later lighter occurrences look like `\varepsilon_0` | low |
| 162 | Final paragraph, “ajustements …” | “cogitables / copiables” | Descender and dot are visible; neither reading is secure. Independent review did not resolve this word | low |
| 162 | Final paragraph, added parenthesis | “(ainsi que des compléments substantiels)” | Wording is clear, but no unambiguous insertion caret fixes its exact place; placed after “général” and before the following parenthesis | medium |
| 163 | l. 1 | “gammes” | Connected medial strokes | medium |
| 163 | l. 1 | “délectables” | First half is compressed; no contextual substitution adopted | medium |
| 163 | End of first paragraph | “qui etc.” | Very abbreviated ending; no closing parenthesis supplied from the preceding page | medium |
| 163 | “contexte présent adélique” paragraph | “trop” | First letters overwritten | medium |
| 163 | Proposition, first line | Deleted `a,b` and deleted `r,s` | Most of the canceled letters are covered | low |
| 163 | Next line | “correspondent” | Final inflection only partly resolved | medium |
| 163 | Underbrace below `ad-bc` | “déf” | Tiny abbreviation above the equality | medium |
| 163 | Last matrix relation before (85) | `f` in `\sigma_\infty(f)^{-1}` | Compact parenthesis and letter overlap | medium |
| 163 | Following line | `\nu` | Overwritten Greek letter, repeated in the canceled uniqueness sentence | low |
| 163 | Following line | “convenable / convenables” | Final stroke does not settle singular/plural | medium |
| 163 | Immediately before (85) | “f / faut” | Only a clear initial `f` and connected stroke are recoverable; abbreviation has not been silently expanded | low |
| 163 | Same line | One deleted illegible unit after “et” | Small black cancellation | low |
| 163 | (85) | `cd` | Product overwritten | medium |
| 163 | Deleted sentence after (85) | “signes”; `\nu` | First word and scalar are partially covered by the replacement sentence | low |
| 163 | Before the first canceled formula near (86) | Deleted “définit” plus one illegible unit | Final erased symbol cannot be identified | low |
| 163 | Canceled formula before (86) | `\varepsilon_3`, relation `\equiv / =`, possible `(c^2+cd+d^2)` and `\in\widehat{\mathbb Z}^*` | All terms after the first sign are heavily struck through | low |
| 163 | Beside (86) | Small marginal “par” | Its intended attachment is not identifiable | low |
| 163 | Canceled formula below (86) | `\mu / 1/\mu`, `\varepsilon_3`, and the norm expression | Several successive revisions overlap | low |
| 163 | Beneath that canceled formula | Three illegible deleted units | Only fragments remain | low |
| 163 | Revised paragraph between (85) and (86) | New tuple, “par `a,b,c,d`, par la … relation,” and `(\mu=2\nu+1)` are marked as insertions | Their positions relative to the canceled version are recoverable only approximately; the old version is also retained | medium |
| 164 | First line of parameters | `\mu / \mu_2` | A small low stroke follows `\mu`; it may be an index or residue of a revision | low |
| 164 | Existence parenthesis | “Il” | The initial pen shape might contain an opening parenthesis | medium |
| 164 | (87), three addition signs | `+ / -` | The signs are thickly overwritten | low |
| 164 | (87), vector direction | `t / u`, `u / t` | Both entries have been overwritten; no choice made from the determinant equation | low |
| 164 | Canceled block, definition of `R` | First `r` | Dark overwritten initial letter | medium |
| 164 | (88), canceled subcalculation in the line for `D` | `U`, possible `t^2`, and one illegible unit | A newer equality was written above an older one before the whole block was crossed out | low |
| 164 | Just below that subcalculation | “`t^2+`” | Tiny isolated mathematical fragment; attachment unclear | low |
| 164 | Final line | “à” | Small stroke between “ici” and “la” | medium |

### Scan 165

| Scan | Approximate line or locus | Reading | Alternative / issue | Confidence |
|---|---|---|---|---|
| 165 | Opening parenthetical reference | `cf.` | Ink before (61) is overwritten; an additional `i.e.` is placed beneath the equation. | medium |
| 165 | (88), second equation | `c` in `(c+d)` | Letter is overwritten; no secure alternative. | medium |
| 165 | Determinant following (88) | `c²` | First letter retraced/overwritten. | medium |
| 165 | After congruences | Deleted `puis` | Struck beginning, partly obscured. | low |
| 165 | Before `représenter` | Deleted `déf.` | Possibly a longer abandoned word; final stroke is obscured. | low |
| 165 | Parenthesis near foot | `dépendent` | Ending faint; `dépendant` cannot be excluded. | medium |
| 165 | Before `paramètres` | Deleted `un grand choix` | Very heavily crossed out; reading tentative. | low |
| 165 | Before `σ,τ` | One illegible deleted item | May be symbols rather than a word. | low |
| 165 | Last line, after `c,d` | `t,u` | Two symbols retraced; no secure alternative. | medium |
| 165 | Last line, second variable after `r` | `s` | Alternative `t`; the variable is retraced and s/t-shaped on independent review. Mathematical consistency has not been used to choose it. | medium |

### Scan 166

| Scan | Approximate line or locus | Reading | Alternative / issue | Confidence |
|---|---|---|---|---|
| 166 | First line | `λ` after `paramètre` | Very small stroke at the closing curve; may be only a parenthesis. | low |
| 166 | Before (89) | `linéaires-affines` | Separator and ending crowded; possibly `linéaires. Affines`. | medium |
| 166 | Below `rang 3` | Deleted `det` | Short crossed abbreviation; location in the revision sequence is uncertain. | low |
| 166 | Second matrix congruence | Modulus `2` | Written in a rounded form; no secure alternative. | medium |
| 166 | Group symbols in Remarque | `\widehat{\widetilde{\Pi}}_{0,3}` | Two accent strokes; order/identity of tilde and hat is not certain. | low |
| 166 | Following `(c,d)` | Deleted `fixées` | Beginning overwritten; possibly `fixés`. | low |
| 166 | Repeated congruence at bottom | One deleted item between `1+c` and `(4)` | Earlier modulus or coefficient is overwritten. | low |
| 166 | Deleted continuation of repeated congruence | `⇔` and `cd ≡ 0 (4)` | Arrow partly cancelled; intervening item illegible. | low |
| 166 | Deleted second continuation | `⇔ c ≡ 0 (4)` | Oblique cancellation strokes obscure both arrow and letter. | low |

### Scan 167

| Scan | Approximate line or locus | Reading | Alternative / issue | Confidence |
|---|---|---|---|---|
| 167 | Opening, following `c` | One illegible deleted item | Replaced by above-line `mod 4`. | low |
| 167 | Before cancelled formula above (90) | Deleted `par` | Short crossed word. | medium |
| 167 | Cancelled formula above (90) | `ε₂ ≡ ε₃ c`, then `ε₂ ≡ ε₃(1+c) (4)` | First subscript and symbol after `ε₃` are obscured. | low |
| 167 | (91), mixed term | `cd` | Letters have been retraced/overwritten. | medium |
| 167 | (91), relation after quadratic form | `≡` | Could be `=`; a short upper stroke and two darker lower strokes are superimposed. | low |
| 167 | (91), immediately before `ε(t²+u²)` | One illegible deleted item | Several letters or symbols may be present. | low |
| 167 | `où ε ... est le signe` | One illegible deleted item | Above-line `∈{±1}` is an insertion. | low |
| 167 | (92), first two variables | `b`, `s` | Both are overwritten, with `s` especially resembling `b`. | medium |
| 167 | Three occurrences of `signe` | No separate underline | The long lower strokes are continuous descenders of g, as also seen in `congruence`; independent review supports treating them as letter shapes. | high |
| 167 | `torseur ... des solutions` | `\mathcal T` | Calligraphic capital T; a large τ-like glyph is also visually possible. | medium |

### Scan 168

| Scan | Approximate line or locus | Reading | Alternative / issue | Confidence |
|---|---|---|---|---|
| 168 | Number of action formula | `(93)` | Final digit has a curved lower hook resembling 3 but is overwritten; `(94)` remains an alternative. | medium |
| 168 | Abandoned start to matrix expansion | Illegible deleted opening followed by `-2nc, b-` | The leading character and opening delimiter are obscured; the tail is recoverable. | low |
| 168 | `dans ... l'ensemble` | One illegible deleted item | Small crossed character or word. | low |
| 168 | Parenthesis after `(87)` | `qui se` followed by an illegible word | Ending of the reference cannot be read securely. | low |
| 168 | Dense insertion under reference | `assuré`, `seulement quand` | Overlapping ascenders and descenders obscure the phrase. | medium |
| 168 | Same insertion | `on considère des` | Alternative `en considérant des`; syntax is not used to decide. | low |
| 168 | Same insertion, congruence | `α′₀`, `f′₀` | An independent rereading supports both primes and both zero subscripts; not silently normalized to unprimed f. | high |
| 168 | Before `dire que` | Deleted `donc` | Cancellation and retracing overlap. | medium |
| 168 | Inserted group notation | `GL(2,Ẑ)^{±1′}` | Final apostrophe may be separate from the superscript, or absent. | low |
| 168 | Addition before underlined u | `à lacets` | Confirmed by independent rereading. | high |
| 168 | Deleted words before (95) | `les valeurs` | Second word largely crossed through. | low |
| 168 | Deleted continuation of (95a) | `qui donne` | Beginning under strike; no secure alternative. | low |
| 168 | Inserted parenthesis after (95a), opening | `donc` | Alternative `d'où`; no apostrophe is visible, but overlapping strokes warrant a doubt mark. | medium |
| 168 | Sign functions in (95a), deleted and inserted versions | `ε₂(μ)`, `ε₃(μ)` | The function glyphs can resemble `ξ₂`, `ξ₃`; both alternatives are marked. | low |
| 168 | Inserted sign formula after (95a) | First `ε₂` | Subscript retraced and resembles another letter. | medium |
| 168 | Deleted line after (95b) | Illegible symbol followed by `= ε₃, μ, c,d,t,u ∈ Ẑ`, `satisfaisant` | Several superimposed versions; segmentation is tentative. | low |
| 168 | Before `(86)` | `sempiternelle` | Individual letter shapes support this reading on independent review. | high |
| 168 | Last paragraph | `ambiguité` | Alternative `ambiguïté`; exact diacritic placement is unclear. | medium |
| 168 | Last visible word | `rationnel` | Low-contrast ending at the right edge; sentence continues outside supplied pages. | medium |

## 3. Abbreviations met

Expansions in this section are interpretive aids only. They are not inserted into the transcription. Variant spellings and punctuation remain as they occur in each scan group; repetition between groups records their local occurrence rather than a proposed standardization.

### Scans 150–154

These expansions belong to the apparatus only.

| As written | Probable expansion | Locations |
|---|---|---|
| `i.e.` | id est; c'est-à-dire | 150–154 |
| `NB` | nota bene | 151, 153 |
| `cf` | confer; voir/comparer | 152–153 |
| `dim.` / `dim` | dimension | 151 |
| `rel` | relative | 151, marginal correction |
| `resp` / `resp.` | respectivement | 151–152 |
| `pt` | point | 151 |
| `sss` | si et seulement si | 152 |
| `mod` | modulo | 152 |
| `cqfd.` | ce qu'il fallait démontrer | 152 |
| `nb` (uncertain reading) / `nbs` | nombre / nombres | 152, 154 |
| `hom` | homomorphisme | 153 |
| `etc` / `etc…` | et cetera | 153 |
| `autom.` | automorphisme | 154 |
| `l'ens` | l'ensemble | 154 |
| `\overline{\mathrm m}` in `lui-…` | même | 153 |
| `\mathrm{id}` (uncertain) | identité | 154, (70) |
| `\operatorname{Spec}` | spectre | 151 |
| `Gl`, `Sl` | groupe linéaire général; groupe spécial linéaire | 151, 153–154 |

### Scans 155–159

| As written | Probable expansion or meaning, confined to these notes |
|---|---|
| i.e. | *id est*, “that is”. |
| ssi | *si et seulement si*. |
| etc | *et cetera*. |
| O.K. | A short acknowledgement that the displayed check works; “okay”. |
| orthog. (uncertain reading) | *orthogonale*, in “réflexion orthog.” |
| tjs (uncertain reading) | *toujours*. |
| autom / autom. | *automorphisme*, or the plural where the syntax requires it; the transcription preserves the original forms. |
| mod | *modulo*. |
| NB | *nota bene*. |
| Id / id | Identity map or identity matrix in the displayed formulas. |
| §43 | A reference to section 43; the section sign is retained as written. |

### Scans 160–164

| As written | Proposed meaning, for this list only |
|---|---|
| `mod` | modulo |
| `cf` | comparez / confer |
| `i.e.` | id est, “c'est-à-dire” |
| `NB` | nota bene |
| `p.ex.` | par exemple |
| `dim` | dimension |
| `déf` (uncertain) | définition / par définition |
| `etc.` | et cetera |
| `sup.` | supérieur, in “coin sup. gauche” |
| `pr` (alternative reading only) | par |
| `f` (uncertain compressed form) | possibly “faut” in “il f et il suffit”; not silently expanded |
| `\S` | section / paragraphe |
| `Gl`, `Sl` | Groupe linéaire général and groupe spécial linéaire; exact handwritten case is not fully secure |

### Scan 165

- `cf.` (doubtful here): confer / compare.
- `i.e.`: id est.
- Deleted `déf.` (doubtful): possibly définir; no expansion is inserted in the transcription.

### Scan 166

- `équa.`: équations.
- `l'ens.`: l'ensemble.
- `dim`: dimension.
- `mod`: modulo.
- `NB`: nota bene.
- `inv.`: inversible.
- Deleted `det` (doubtful): déterminant.

### Scan 167

- `mod`: modulo.
- `i.e.`: id est.
- `l'ens.`: l'ensemble.

### Scan 168

- `l'ens.`: l'ensemble.
- `cf`: confer / compare.
- `autom`: automorphisme.
- `Id`: identité.
- `§`: section / paragraphe.
- `bis`: repeated or supplementary numbering; retained in `(24bis)`.

## 4. Legibility and limits

The uncancelled central prose and most large matrix displays are substantially more legible than the oblique margins, compact insertions, and overwritten calculations. The principal limits are the marginal notes on scans 152–153, 155, and 159–161; reworked coefficients and signs in the long calculations; the cancellations on scans 163–164 and 166; and the dense insertion and revised list on scan 168. These are explicit uncertainties, not claims that the missing wording can be recovered from mathematical context.

Each assigned scan received a full-page reading, a transcription pass, and a comparison against the image; selected difficult loci received an additional independent reading. The audit does not make the transcription error-free. In particular, minor diacritics, compressed endings, cancellation boundaries, and the placement of very small additions remain less secure than the main text. The final scan has been checked through its last visible word; its unfinished closing sentence has not been completed.

## 5. Research notes — English, separate from the transcription

These notes concern the supplied extract of Grothendieck (1981). Each scan and equation reference below is a locator in that primary source. Quotations are brief readings of the supplied handwriting; an unresolved reading is not promoted to established evidence. “Conjecture / expectation” includes working hopes and doubts that may be resolved elsewhere, including on a later supplied scan. “Unproved claim” means that a proof is not supplied at the cited location; it does not assert that the claim is unproved in the rest of the manuscript or the literature. Items labelled **own idea** are proposed checks or directions, with confidence and reasons, not claims of novelty or established results. No literature review is claimed.

### Scans 150–154

1. **Scan 151, paragraph following (62); kind: unproved claim / expectation.** Grothendieck writes “on doit pouvoir vérifier” that the scheme of solutions has relative dimension 3 and relative dimension 1 over either displayed factor; the margin says “non, il est de dim. rel totale 4.” A proof would need an exact independent equation set, a statement of the base and the projection under consideration, and an analysis of fibres, rather than merely subtracting the number of displayed equations from the number of variables. The marginal correction should be checked against subsequent discussion, without deleting the earlier claim from the diplomatic text.

2. **Scan 151, margin beside (61)–(62); kind: unproved claim.** The note says that the last relation is “conséquence des autres,” taking account of `C+D-B=1` and `AD-BC=1`; the last polynomial relation is likewise marked as a consequence. To validate the implication over the intended coefficient ring, one should make explicit where the invertibility derived from `\mu D=1` enters the elimination. This is especially relevant to the dimension count in the following paragraph.

3. **Scan 152, upper left margin; kind: conjecture / expectation.** “Ce serait le moment d'inclure … la relation `\mu\equiv\delta\ (3)`” records a proposed expository addition, not a new conjectural equality. Its suggested demonstration is only partly legible in the margin; the central text supplies the analogous calculation later on the same scan. The relation and the location of the proposed insertion are worth checking against the manuscript's later revisions.

4. **Scan 152, paragraph introducing the quadratic characters and (63); kind: own idea. Confidence: high for the elementary diagnostic, limited for the author's intended convention.** The literal square criterion at the prime 2 should be compared carefully with the mod-4 sign characterized in the preceding paragraph: `5` is `1` modulo 4 but cannot be a square modulo 8. Thus a direct identification of the sign in (63) with the indicator of membership in `(\mathbb Z_2^*)^2` requires clarification of the intended character or additional hypotheses. This is a research/checking note only; the transcription retains the written criterion.

5. **Scan 152, last paragraph and (63); kind: unpursued implication.** The words “la connaissance de … équivaut à celle de `\mu` mod …” connect the two signs with small-modulus data, while the adjacent margin displays the product of unit groups modulo 4 and 3. A useful later check is whether the combined mod-12 datum is used merely to determine the two signs or to impose stronger conditions on the admissible multipliers. The first modulus in the final prose line is visually uncertain and should not be treated as settled evidence until the image is re-examined.

6. **Scan 153, (65) and the paragraph below it; kind: unpursued implication.** Grothendieck remarks that “`g` s'exprime simplement en termes de `f`,” whereas expressing `\alpha` requires both sets of variables. The displayed matrix (65) appears to depend only on `t,u,\mu`, so the effect of changing the top row of `f` is worth making explicit. Any proposed invariance must be checked using the manuscript's precise change-of-choice convention and admissibility equations.

7. **Scan 153, left marginal note; kind: unproved claim.** The clearly readable part asserts that the relevant quantity is “déterminé sans ambiguïté (au signe près)” by an automorphism, while contrasting it with the choices entering `f`. A proof would have to specify the equivalence relations on the lifts and verify which quantities survive the change `f\mapsto l_0^n f`. Because several words in the final portion of this margin remain illegible, this note deliberately does not reconstruct a complete formal statement from it.

8. **Scan 154, (68 bis)–(69); kind: unpursued implication.** Applying `x\mapsto x\rho(x)\rho^2(x)` to the twisted commutator fixes the second sign, and the remaining equation is rewritten as `u=\alpha u_0` with `[u_0,\rho]=1`. This suggests organizing the remaining choices as a coset of a centralizer and then imposing the other conjugacy and determinant equations. The note concerns the structure made visible by the displayed calculations, not a claim that all remaining compatibility conditions have been solved here.

9. **Scan 154, paragraph below (69); kind: unproved claim recalled from earlier work.** “Nous avons déjà remarqué” introduces the assertion that the two conjugacy equations determine `u` up to an invertible scalar, with the determinant reducing the residual ambiguity to `\lambda^2=1`. The local proof is not repeated on this scan; it would require determining the simultaneous centralizer of the relevant matrices over `\widehat{\mathbb Z}` and checking possible exceptional components. The statement may have been justified on earlier pages outside this assignment.

10. **Scan 154, same paragraph; kind: conjecture / expectation.** The phrase “on espère néanmoins tomber sur un choix canonique” explicitly leaves open a preferred representative despite the prime-by-prime sign ambiguity. Subsequent formulae should be checked for what exactly canonically determines the representative, and whether the construction remains invariant under the choices in the preceding scans. This expectation is recorded even if a later page resolves it.

11. **Scan 154, (70); kind: own idea. Confidence: high as a direct algebraic check, conditional on the uncertain identity glyph.** The matrix family in (70) can be tested directly as the commutant of the displayed `\rho` by writing a general 2×2 matrix and comparing the four entries of the products. After resolving the overwritten identity symbol, its determinant also provides a concrete quadratic expression with which to check the subsequent norm-like formulae. This is a proposed verification of the written calculation, not an emendation of (70).

### Scans 155–159

All manuscript observations and quotations below refer to the supplied images of Grothendieck (1981), using filename scan numbers. A “conjecture” label includes the author's working expectations and doubts, including ones reconsidered within the next page; it does not assert that a question remains open elsewhere in the manuscript.

1. **Scan 155, paragraph after (73); kind: conjecture / working expectation.** Grothendieck recalls “de subodorer que l'on devrait avoir ε′ = +1 ssi p ≡ 1 (4)” after finding that an earlier universal positive-sign conclusion was not compatible “avec le corps des classes”. A careful study would have to identify the role of p and the relevant class-field-theoretic condition from the preceding context rather than assume that the symbol denotes an arbitrary prime.

2. **Scan 155, right annotation to (74); kind: conjecture / working expectation.** The brief note “sans doute, ε₂ = 1” connects the commuting case to the sign determined by μ. The following scans develop this distinction, so this is a record of the author's intermediate expectation rather than an independently unresolved claim.

3. **Scan 155, (71)–(73); kind: own idea. Confidence: medium.** The repeated expressions $p^2+pq+q^2$ and $c^2+cd+d^2$, with reciprocal μ factors, invite a norm-based organization of these calculations. One could test this by working directly in the two-dimensional algebra generated by the displayed ρ and computing the determinant of $c\rho+d$; the reason for the suggestion is the explicit recurrence of the same quadratic polynomial, not an appeal to an external identification.

4. **Scan 156, left margin beside the commutator calculation; kind: unpursued implication.** The note “On pourrait aussi appliquer les formules §43 (78)” points to an alternative calculation. Comparing that cited formula with the present expansion would require the actual earlier section, which is not supplied in this five-scan segment.

5. **Scan 156, final paragraph; kind: conjecture / working expectation.** Grothendieck wants to “trouver ‘au pif’ une expression” when ε₂ = −1 and says “je prévois que la matrice” involving τ∞ will work. Scan 157 tests this expectation, encounters a sign problem, and changes the placement of τ∞; both the failed trial and the repair should be kept when studying the argument.

6. **Scan 157, from the tentative commutator to t replaced by −t; kind: unpursued implication.** The trial equality leads to “2μut = 0”, followed by “décidément, ça déconne !”, and the next step replaces t by −t. This passage is suitable for a separate reconstruction of the sequence of sign conventions, with each intermediate matrix checked independently, because collapsing the calculation to its eventual answer would conceal why the left and right placements of the reflection matter.

7. **Scan 158, (75)–(78); kind: own idea. Confidence: high that a check is needed, not that a particular correction is established.** Recompute (77) in both ε₂ cases directly from (75), keeping the group commutator and the conjugation notation distinct. The reason is visible on the page: the left formula has $-\varepsilon_2\mathrm{id}$, whereas its adjacent “i.e.” statement has $+\varepsilon_2\sigma_\infty$; the diplomatic transcription deliberately leaves this discrepancy intact.

8. **Scan 158, corollary; kind: unproved claim in the local text.** The corollary says that the action “passe en une action dans le quotient” and is induced by an automorphism of $\mathrm{GL}(2,\widehat{\mathbb Z})$ defined by a matrix of determinant μ. A full proof of descent needs to establish preservation of the kernel of the relevant quotient map and the agreement of the induced action with the displayed conjugation; the preceding two-by-two computations alone do not explicitly state those steps on this page.

9. **Scan 159, upper-left margin; kind: unproved claim.** The margin says one is “ramené au cas où u commute à σ∞”, “quitte à conjuguer” by an inner automorphism; the end of the note is not fully legible. The corresponding reduction would need an explicit normalizing conjugation and a check that the hypotheses and multiplier used in the corollary survive it.

10. **Scan 159, second left marginal note; kind: unpursued implication.** “On a fait ceci, pour le moment, pour u commutant à σ∞” limits the scope of the calculation performed. This should be compared with the preceding corollary's exterior-commutation hypothesis before treating the passage as a proof for every representative.

11. **Scan 159, inserted “modulo signe” and (79); kind: unpursued implication.** The promised construction “canoniquement”, qualified by inserted “modulo signe”, rests on the fact that left multiplication by $\ell_0^n$ leaves the lower row (t,u) unchanged. To formalize the claim one should specify the quotient of choices for f, the remaining simultaneous sign ambiguity, and why no other ambiguity from the original automorphism remains.

12. **Scan 159, last paragraph; kind: own idea. Confidence: medium.** The analogous invariance of (c,d) suggests comparing the two lower-row expressions $t\sigma_\infty+u$ and $c\rho+d$ as parallel descriptions of the same action. The reason is the explicit transition from the f calculation to α₀ and then to $c\rho+d$; this is a proposed organization for further reading, not a claim of a new relation or a relation proved on this page.

### Scans 160–164

These are source-based working questions, not claims of established results or novelty. Formula readings carrying doubt marks remain provisional; the quoted words below are brief and only support the particular note. References identify the supplied scans, independently of the footer numbering.

1. **Scan160, (80) and following two lines — conjecture / question.** The question mark over the equality in (80) and “peut-être de corriger par un facteur” record a provisional comparison of the conjugating matrix with `\mu\alpha(c\rho+d)`. The marginal correction points to the factor `\delta=\varepsilon_3`, and scan161 subsequently writes it in (82), so the question is locally pursued rather than simply abandoned. A study of the derivation should keep the original question and the later scalar correction as distinct stages (Grothendieck, 1981, scans160–161, eqs. 80–82).

2. **Scan161, (83)–(84) — unpursued implication.** The reformulation culminates in `\varepsilon_2U=D` and `\varepsilon_2T=C`, called the “contenu essentiel” in the provisional reading of the accompanying sentence. This invites a precise comparison between the conjugating-matrix expression and the two scalar compatibility conditions, including an account of why the other matrix entries are redundant under the determinant relations. The dependence on the legibility of “contenu” is editorial, whereas the two displayed scalar identities are clear (Grothendieck, 1981, scan161, eqs. 83–84).

3. **Scans161–162, Remarque and opening continuation — conjecture / expectation.** “Sans doute sous des conditions beaucoup plus générales” expresses the expectation that the calculation is valid in a broader setting of matrix groups over arbitrary rings. The text then introduces fixed `\rho,\sigma`, a scalar, and a one-parameter subgroup rather than restricting itself to the original profinite situation. A proof must specify the base ring, determinant constraints, and invertibility assumptions instead of assuming that every displayed division remains valid (Grothendieck, 1981, scans161–162).

4. **Scan162, final paragraph — conjecture / expectation.** “Devraient pouvoir se développer” and the inserted “compléments substantiels” explicitly leave a more general treatment for possible later work. The closing admission “je ne sais si je vais expliciter” should be tracked against the continuation of the manuscript rather than treated as a promise of a completed argument. This note records both the expectation and the author's hesitation (Grothendieck, 1981, scan162, final paragraph).

5. **Scan162, (*) — own idea; confidence: medium.** A useful first reconstruction would define the solution functor of (*) with the determinant conditions stated explicitly, then ask on which open subsets a commutator equation is equivalent to a conjugacy equation. This is a proposed organizational step, not an asserted description of the manuscript's intended scheme. The reason for medium confidence is that the displayed matrix equation is explicit, but the base and fixed-versus-variable data are not all settled in this remark (Grothendieck, 1981, scan162, eq. *).

6. **Scan163, first paragraph — unproved claim.** The phrase “schéma relatif lisse de dim relative 4” proposes smoothness and a dimension for the scheme of solutions of (*), with `f,\alpha_0,\mu` variable. No proof is supplied at that point in these pages, and the base of the relative statement and the determinant restrictions must be identified before a Jacobian or deformation calculation can check it. The claim should therefore be examined in the general-ring framework of the preceding remark, not merely by counting displayed variables (Grothendieck, 1981, scans162–163).

7. **Scan163, first paragraph and (85) — own idea; confidence: medium.** A targeted test of the proposed smoothness would examine the relevant Jacobian in residue characteristics 2 and 3 before extrapolating from characteristic zero. The reason is that differentiating the visible quadratic expressions `t^2+u^2` and `c^2+cd+d^2` changes their behavior in these characteristics. This is a suggested check only; it does not assert that the stated solution scheme fails to be smooth (Grothendieck, 1981, scan163).

8. **Scan163, Proposition and (85) — unproved claim / proof obligation.** The proposition asserts a necessary and sufficient condition on the two lower rows through the equality, up to sign, of their quadratic expressions as units. A proof has to complete both lower rows to matrices satisfying the stated determinants and the compatibility relation, and then identify the freedom left in the upper rows. Scan164 begins this reconstruction, but its first detailed construction of the auxiliary matrix is crossed out, so canceled calculations should not be counted automatically as the final proof (Grothendieck, 1981, scans163–164, eqs. 85–88).

9. **Scan163, revised paragraph between (85) and (86) — own idea; confidence: medium.** Audit the intended sign involution before formalizing the parameter space: the inserted tuple contains `2\nu+1`, whereas the surviving displayed negation ends in `-\nu`. If the sign reversal is meant to send `\mu=2\nu+1` to `-\mu`, elementary algebra instead sends `\nu` to `-\nu-1`. This is an editorial hypothesis to be checked against later pages; the multiple revision layers prevent a confident statement of the intended correction, and the transcription preserves the ink (Grothendieck, 1981, scan163).

10. **Scan163, (86) — own idea; confidence: medium.** Compare the surviving `c^2+cd+u^2` in (86) with the preceding `c^2+cd+d^2` in (85) before deriving consequences from the proposition. The visible mismatch may be an unrevised intermediate slip, but the reason for checking it is the different last variable on the same page, not an assumption that the formulas must already be consistent. No correction has been made in the transcription (Grothendieck, 1981, scan163, eqs. 85–86).

11. **Scan164, existence assertion preceding (87) — unproved claim.** “Il y en a toujours” asserts existence of `r,s` with `ur-ts=1`, but the written parenthetical explanation invokes `r^2+s^2` and the components `r_p,s_p`. The variable scope therefore needs verification in any reconstructed proof: the available data of the proposition are the fixed lower-row entries. The statement and its written explanation should be distinguished (Grothendieck, 1981, scan164, upper half).

12. **Scan164, (87) — own idea; confidence: high, conditional on the unit hypothesis.** For fixed `t,u` with `q=t^2+u^2` invertible, the concrete choices `r_0=u/q` and `s_0=-t/q` satisfy `ur_0-ts_0=1`. One can then check directly the proposed affine family in the direction `(t,u)` and determine whether it gives every completion over the stated ring. This construction is elementary and motivated by the page, not claimed as new; it is kept in the notes and has not been used to choose the overwritten signs in (87) (Grothendieck, 1981, scans163–164).

13. **Scan164, canceled block containing (88) — unpursued implication.** The deleted calculation defines `A` using `(1+BC)/D` and reduces the remaining compatibility to the upper-left corner relation, described as the “coin sup. gauche.” It is worth determining why this route was abandoned and whether its reduction remains valid after the hypotheses are made explicit. The page itself does not state a reason for the cancellation, so the crossed-out argument is evidence of an attempted approach rather than an accepted conclusion (Grothendieck, 1981, scan164, canceled eq. 88 and following lines).

### Scan 165

- **Scan 165, after (88); unproved claim.** The determinant is said to be a unit, « ce qui assure une solution unique ! ». A verification should calculate the determinant of the displayed coefficient matrix with its written signs and recover the stated quadratic form, then use invertibility over the profinite coefficient ring.
- **Scan 165, middle; unpursued implication.** The preference to « partir du multiplicateur μ » suggests organizing the solutions by the multiplier and the two bottom rows. The isolated congruence `μ ≡ ε₂ (2)` needs comparison with the earlier and later congruences; modulo 2 alone cannot distinguish the two integer signs, and the transcription deliberately preserves the written modulus.
- **Scan 165, lower paragraph; conjecture / expectation.** Grothendieck says the pairs « dépendent de 1 paramètre » in a sense one could « préciser si on y tenait », with explicit parameters `σ,τ`. Making this precise would require specifying the parameter spaces and whether the parametrizations are global, local, or torsor descriptions, particularly at primes where the quadratic forms behave differently.

### Scan 166

- **Scan 166, (89) and following paragraph; unproved claim.** The system is said to have « rang 3 », and its solutions form an « espace affine de dim 1 » over `Ẑ`. A complete formulation over this ring should exhibit a split surjective coefficient map, identify its rank-one kernel, and establish that the affine fibre is nonempty.
- **Scan 166, Remarque; unpursued implication.** « On n'a pas pour le moment tenu compte des conditions de congruence » introduces restrictions on which algebraic solutions arise from the indicated group elements. The ensuing congruence computation is only part of the task: one should distinguish necessity, sufficiency for matrix lifting, and lifting to the original profinite groups.
- **Scan 166, (89); own idea — high confidence, algebraic reason.** Write the coefficient map in the variable order `(a,b,r,s)` and seek an explicit kernel generator once the unit quadratic form has been fixed. This would make the claimed affine parameter and its reduction modulo 2 directly comparable with the additive action on scan 168; this is a proposed verification, not a claim that the manuscript has already supplied all steps.

### Scan 167

- **Scan 167, (90); unpursued implication.** The statement that `c mod 4` and the determinant sign determine the other sign is an explicit compression of the sign data: « permet de trouver le signe ε₂ ». It would be useful to track how this condition interacts with all the earlier independent sign choices, rather than assuming that the two signs remain free after congruences are imposed.
- **Scan 167, paragraph after (92); unproved claim.** The lifting problem is interpreted through a quotient torsor, and the set of lifts is asserted to be a torsor under `2Ẑ ≃ Ẑ`, ending « Aucun mystère ! ». A complete argument should give the torsor action, verify compatibility with reduction, and identify the fibre above the prescribed mod-2 solution.
- **Scan 167, final paragraph; own idea — high confidence, elementary group-theoretic reason.** Once the claimed additive `Ẑ`-torsor structure is established, the appearance of `2Ẑ` can be checked directly as the kernel of reduction modulo 2. This isolates which part is formal from which part still depends on the matrix equations and their nonempty solution set.

### Scan 168

- **Scan 168, action formula labelled uncertain (93)/(94), and its following paragraph; unproved claim.** The displayed additive action is identified, up to the factor 2, with the ambiguity of solutions when the four bottom-row entries are fixed: « c'est justement l'indétermination ». A proof should verify preservation of (93) and compare its orbits with the full affine solution fibres, including the added mod-2 conditions.
- **Scan 168, (95)–(97); unpursued implication.** The text characterizes what is « déterminé intrinsèquement » by the automorphism in terms of the multiplier and bottom rows. The precise equivalence relation on these quantities, particularly the surviving signs and the prime in the group notation, deserves an explicit invariant formulation before treating them as canonical coordinates.
- **Scan 168, (96); own idea — high confidence about the need for checking, no claim of correction.** Compare the two visible `ε₂` coefficients with (86), (90), and the signs used in reconstructing the matrices. This might be an uncorrected slip or might depend on a specialization not visible here; the original subscript remains unchanged in the transcription.
- **Scan 168, last paragraph; unproved claim / deferred question.** Grothendieck recalls a « moyen naturel » to normalize the choice of f, cites §41 and the inserted `(24bis)`, and writes « j'y reviendrai encore par la suite ». The proposed normalization and its compatibility with the intrinsic data should be checked at that earlier reference and in the continuation; the current extract ends before the reservation beginning « mais il me semble peu rationnel » is completed.
- **Scan 168, additive action; own idea — medium confidence, explicit-formula reason.** One can test the stabilizer and orbit claims first in finite coefficient quotients, retaining the factor 2 rather than cancelling it there. Such tests may locate a failed lifting or sign condition, but finite computations alone would not establish the inverse-limit statement.

## 6. Primary-source reference

Grothendieck, A. (1981). *La Longue Marche à travers la théorie de Galois* [Handwritten manuscript, cote 140-3, archive file “pages 293–650”; supplied scans 150–168]. Université de Montpellier.

Bibliographic identification follows the supplied task metadata; it has not been independently verified against an external catalogue. All scan locators in this apparatus use the supplied filenames, as mapped in Section 1.

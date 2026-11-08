# LM_C3-226–244 — Diplomatic transcription notes

## 1. Source, scope, and editorial conventions

This file accompanies `LM_C3-226-244_transcription.tex`, a diplomatic French transcription of all 19 supplied images. The attribution, title, date, and archival description are those supplied with the task: Alexander Grothendieck, *La Longue Marche à travers la théorie de Galois* (1981), Montpellier archive, cote 140-3, pages 293–650. No published transcription or external source was used to supply readings or complete the mathematics.

**Scan numbers follow the image filenames.** Each printed footer is one lower than its filename scan number. Visible main manuscript page numbers are transcribed with `\mspage`; the small handwritten lower-left numerals are retained with `\margin`, without attributing their hand. Printed archive addresses and institutional footers are metadata, not manuscript text, and are not included in the LaTeX fragment. A dash below means that no main manuscript page number was securely read; none has been interpolated.

| Filename scan | Printed footer / small lower numeral | Main manuscript page number retained |
|---|---|---|
| 226 | 225 | — |
| 227 | 226 | 413 |
| 228 | 227 | — |
| 229 | 228 | 415 |
| 230 | 229 | — |
| 231 | 230 | 416 |
| 232 | 231 | — |
| 233 | 232 | 417 |
| 234 | 233 | — |
| 235 | 234 | 418 |
| 236 | 235 | — |
| 237 | 236 | 419 |
| 238 | 237 | — |
| 239 | 238 | 420 |
| 240 | 239 | — |
| 241 | 240 | 421 |
| 242 | 241 | — |
| 243 | 242 | 422 |
| 244 | 243 | — |

The fragment has no preamble and begins with `\scanpage{226}`. Its editorial commands are confined to those requested. The host document must define those commands and provide the usual mathematical and `tikz-cd` support. The two diagrams use `ampersand replacement=\&` so that they can occur inside the permitted `\diagram{…}` wrapper.

Cancellation, insertion, and marginal text are retained separately where their states can be distinguished. `\unsure{reading}` records a tentative reading; `\unsure{reading|alternative}` keeps a graphical alternative visible. `\illegible{n}` estimates the number of unreadable words; in a cancelled formula it estimates mathematical units rather than ordinary words. The fragment preserves visible mismatches, repeated equation numbers, unmatched prose punctuation, and changes of notation instead of completing them from mathematical expectations. The single-wave and double-wave superscripts are distinguished as `\sim` and `\approx`; hats, plus signs, exclamation marks, primes, and underlining have not been globally normalized. The double-stroked integer letter is represented by `\mathbb Z`; the broad curled group letter is rendered provisionally as `\mathcal G`, with local doubts where its alphabet or identity remains insecure.

## 2. Table of doubts

These tables group repeated occurrences of the same difficulty within a passage. Equation numbers, paragraph descriptions, and marginal positions supplement approximate line counts. Confidence is confidence in the reading or revision state, not in the truth of a mathematical claim: **high** means relatively secure visible evidence with a residual issue, **medium** a plausible but incomplete reading, and **low** a materially unresolved reading or revision sequence.

### Scans 226–230

Locations below refer to the manuscript's visible paragraphs or numbered displays; line counts restart after a paragraph reference where needed. The bottom pencil numerals 225–229 are retained as marginal annotations, without an attribution of their hand. Only the main top numbers 413 and 415 are entered with `\mspage`.

| Scan page | Approximate line/location | Reading retained | Alternatives / reason for doubt | Confidence |
|---|---|---|---|---|
| 226 | Opening line, before and after underlined u | A possible opening brace; `u ∈ B`; a possible closing brace after `(2)` | Dense overwriting around the brace and membership/group glyph; the status of some strokes as deletion or letter is not certain. | low |
| 226 | Opening line, congruence for M | `M ≡ 0 (2)` | The final modulus is faint and partly clipped at the right; the numeral is not completely resolved. | medium |
| 226 | Before “tore maximal” | Inserted `le` | The short addition above the line could be a different article; a stroke below it may be a superseded article. | medium |
| 226 | Display (178), left group symbol | Underlined `B₁` | The lower flourish could belong to the handwritten capital rather than be an underline. | medium |
| 226 | Paragraph after (178), opening | `au quotient` | `aux quotients`; the final strokes do not securely establish singular or plural. | medium |
| 226 | Same paragraph, group before `/L₀` | `M^{!~}(0)` | `[0]`; the left delimiter resembles a parenthesis, but the stabilizer notation elsewhere uses square brackets. This is not corrected from context. | medium |
| 226 | Same paragraph, after “mieux” | Superscript cross `×` | Could be an asterisk or another annotation sign. | medium |
| 226 | Same paragraph, before “à la décomposition” | `grâce` | Final letters are very compressed; no replacement is supplied from the sentence's grammar. | medium |
| 226 | Proposition, representative's notation | `u = u_{u̇}` | `u = u_ξ`; the subscript is overwritten and not securely separable. | low |
| 226 | Inserted matrix explanation, last matrix, upper left entry | Illegible entry | The entry is overwritten; neither `1` nor `A` is sufficiently supported for an unqualified transcription. | low |
| 227 | Top left deleted formula | Deleted `M_{0,3}^{!~}(0)` | Superscript and the exact symbol under the strokes remain uncertain. | low |
| 227 | Display (179), set membership | `u ∈ M^{!~}(0)` | `[0]`; the round-looking delimiter is retained with an explicit alternative. | medium |
| 227 | End of first paragraph, before the final extension | `ou` | The two short strokes could represent a different connective. | medium |
| 227 | Proof paragraph, first word | `Ceci` | `Cela`; the last two letters are compressed. | medium |
| 227 | Paragraph beginning “Si”, between ξ and η | Deleted illegible sign | A dark correction precedes η; it cannot safely be identified. | low |
| 227 | Formula after “sous la forme” | Subscript ξ in `f⁻¹u_ξ` | The subscript is heavily reinforced. | medium |
| 227 | Insertion after “cette représentation” | `entachée de l'indétermination (136)` | The first word is compressed; `entachée` is a tentative reading, not an expansion of an abbreviation. | medium |
| 227 | Bracket after “est normalisé” | `si`, with inserted `pour` | The attachment of the added `pour` and whether `si` was intended to be canceled are uncertain; both visible states are retained. | low |
| 227 | Same bracket, between ξ and its matrix | `≃` | The relation sign is overwritten; it may be an equality or a notation sign. | low |
| 227 | Bottom display number | `(179)` | The number appears to repeat the upper display's `(179)`; a clipped or obscured distinguishing mark cannot be excluded. It is not renumbered. | medium |
| 228 | Opening phrase | `avec f normalisé` | `avec ξ normalisé`; the tall glyph resembles f, although this is not used to infer the intended mathematical normalization. | medium |
| 228 | Rmq, first line | `essayer` | The initial letters and ending are very compressed. | medium |
| 228 | Rmq, after “se pose aussi” | `sur` | `pour`; the initial stroke is not secure. | low |
| 228 | Formula (183), action on q | `ρ̇(q)` | `ρ(q)`; there is a small mark above the letter, but its status as a dot is uncertain. | medium |
| 229 | Formula (3), after the expression for g | Deleted illegible sign | A small crossed/overwritten fragment is visible before the line giving α₀. | low |
| 229 | Before display (4) | Deleted `λ ∈` | A crossed letter and membership sign are visible, but the letter is not fully recoverable. | low |
| 229 | Case 1, above “d'où” | Deleted `=(σ∞ρ)²` | The contents of the parentheses are partly crossed through. | low |
| 229 | Case 1, canceled calculation after `u(x)=` | First two terms illegible; tentative tail `=hσ∞gρ=h(σ∞gσ∞⁻¹)σ∞ρ` | The cancellation crosses nearly every term; the readable tail is explicitly marked uncertain. | low |
| 229 | Bottom conjugation formula | Deleted prefix; λ in `φ̂(f)λf⁻¹` | The prefix is obscured and the thin λ overlaps adjacent factors. | low |
| 230 | First formula, initial crossed factor | Illegible deleted factor | The deletion is too dense to recover its letters. | low |
| 230 | First formula, centralizer subscript | `Π̂_{0,3}` | The ambient-group glyph is not secure; no replacement with the mathematically expected ambient group is made. | low |
| 230 | Upper left marginal note | `pas non plus`, followed by one illegible word | The slanting lines crowd the main text; the end of the note is clearer in its formula than in its prose. | low |
| 230 | Formula immediately before (6), initial crossed factor | Illegible deleted factor | Dense diagonal cancellation. | low |
| 230 | After (6) | `∃λ` in “d'éliminer …” | The sign preceding λ resembles an existential quantifier but is not completely clear. | medium |
| 230 | Case 2, expression for `f₁⁻¹` | Two illegible canceled terms before `gρ(f⁻¹)` | The old expression has been heavily overwritten. | low |
| 230 | Canceled line before `uφ̂(x)=u(σ∞)` | Tentative `uφ̂(x)=int(φ̂(f₁))` | Only parts of the canceled line are securely recognizable. | low |
| 230 | Conjugation condition and following two formulas | Exponents `+1` or `−1` on φ̂-expressions | Several exponents are rewritten in darker ink; the sign is not resolved. All three occurrences are marked. | low |
| 230 | Sentence introducing the parity parameter | `i` | `α`; the variable appears reinforced. Later the last formula visibly uses α, which is preserved rather than standardized. | medium |
| 230 | Before “on trouve la condition” | Deleted `f` | A crossed descending glyph follows `gρ(f⁻¹)`; its reading as f is tentative. | low |
| 230 | Canceled condition at bottom | Tentative full crossed equality | The order of the first two factors, inverse placements, and `ℓ₀ʳ` in the crossed right side are not fully secure. | low |
| 230 | Penultimate condition, exponent on σ∞ | Inserted α | An arrow and overwritten character occupy this position; α is read with doubt from the visible correction. | low |

#### Additional transcription cautions

The two equal conjugation expressions in scan 230's line for `φ̂(u(x))` visibly do not have identical inverse notation: the first has an inverse and the second has none visible. The second expression has therefore been transcribed without an added inverse. This is a record of the page, not a mathematical endorsement. Similarly, the use of `(0)` and `[0]`, and the final use of α after an apparent i in the parity calculation, have not been silently unified.

### Scans 231–235

Line numbers are approximate counts from the first body line of the scan, excluding the manuscript page number. Equation numbers and marginal positions are more reliable locators. Repeated instances of one uncertain notation within a passage are grouped in a single row. The printed archive footer is one below the scan filename; the small handwritten lower-left numerals are retained separately as marginal marks, without attributing their hand to Grothendieck.

| Scan | Approximate line / locator | Reading in the transcription | Alternatives / issue | Confidence |
|---|---|---|---|---|
| 231 | L3, target of the comparison map | `\mathcal G` | Exact calligraphic versus Gothic alphabet uncertain; no mathematical identification used to resolve it. | medium |
| 231 | L8, (7) | Exponent `i`; membership condition on the right reads `α ∈ Z/2Z` | The exponent is overwritten; `α` is an alternative reading. The apparent difference between the exponent and the right-hand membership condition has been preserved. | low |
| 231 | Margin beside (7) | “ou encore” | The compressed word after “ou” may differ. | medium |
| 231 | L13, cancelled transformation before (8) | `(α,β,f)`, tentative mapsto, then three illegible units | The cancelled right-hand symbols are not recoverable with confidence. The estimated illegible count represents mathematical groups rather than ordinary words. | low |
| 231 | L16–17, (*) and following membership condition | `i′` | `α′`; overwritten lettering does not consistently distinguish them. | low |
| 231 | L19, long calculation after “Or on aura” | `ξ′`, `ξ` | The compressed forms resemble a looped `f` in places. The reading `ξ` is retained with doubt, without deriving it from the expected identity. | medium |
| 231 | Beneath the L19 calculation | Two separate cancelled, illegible units | The first lies under the intermediate factor involving `φ̂(ℓ₀ⁿ)`; the second under the coefficient near the right end. | low |
| 231 | L21, first exponent after “la relation (*) s’écrit” | `r′−n` | `r′−2n`; the subtraction term has been overwritten. | low |
| 231 | L21–25, exponents and (9) | `i′−n`, later `α′−n`, and `i′=i+n` | `i` versus `α` remains uncertain, and the variation in the visible forms is not silently standardized. | low |
| 232 | L5, “décrire … par un triple” | `u` | `φ`; the letter has an unusual descending stroke. | low |
| 232 | L6–7, parenthesis beginning “a priori” | Opening parenthesis before “a priori”; only the visible parenthesis around `(8)` is supplied at the end | A separate closing parenthesis for the prose parenthesis is not securely visible. No balancing parenthesis was added merely for grammar. | medium |
| 232 | L9, before “relation” | “une” | The word is overwritten. | medium |
| 232 | Margin beside (10) | “celle de la p. 410′, 413” | Article may be different; the first reference has an uncertain prime; the second may read `417`. | low |
| 232 | L11, description of the choice | “sera” | The linking word is compressed; `est` is a possible alternative. | medium |
| 232 | L16, domain of `α` | Tilde and hat on `Π₀,₃` | Both marks are visible, but their exact typographical stacking is uncertain. | medium |
| 233 | L2 onward, finite target with subscript `3` | `\mathcal G_3` | `\mathfrak S_3`; the source glyph is not replaced merely because a standard finite-group interpretation would be plausible. | medium |
| 233 | (12), (13), and prose references to the quotient map | A small filled dot after `φ̂` | An open circle is possible. The alternatives are explicitly marked. | medium |
| 233 | Composite arrow labelled “can” | Two-headed rightward arrow | A single rightward arrow retraced by the pen is possible. Its rightward direction is clear. | medium |
| 233 | L15, kernel sentence | “inv.” | Final abbreviation strokes are small; likely “invariant”. | high |
| 234 | L1, opening of Corollaire 2 | “Les” | The word is heavily inked. The ensuing singular “est” has not been corrected to agree with it. | medium |
| 234 | L1, subgroup abbreviation | Raised `s/` followed by “groupe” | Exact form of the abbreviation is uncertain; possibly a shorthand for “ss-groupe”. | medium |
| 234 | L3, between “est” and “en corr.” | One deleted illegible unit | A tall struck symbol/word cannot be safely identified. | low |
| 234 | L5, after `(ξ,f)` | Deleted `∈` | The small cancellation may contain another symbol. | low |
| 234 | L6, parenthesis before (14)–(15) | “ne faisant intervenir que ξ” | “en faisant intervenir que ξ”. | medium |
| 234 | Margin beside (14)–(15) | “il faut de plus la ‘condition’ ‘liminaire’…” | Final quoted adjective is difficult; no omitted condition has been supplied. | medium |
| 234 | (16), domain of `α` | Left: `α∈Π̂₀,₃`; right: “l’unique élément de” a tilde-and-hat `Π₀,₃` | The differing domains are visible and retained, rather than reconciled. | high |
| 234 | (17), first line | `β` in two conjugating factors | The letter is overwritten. | medium |
| 234 | (17), final right-hand factor | `ξρ` | The `ξ` is heavily retraced. | medium |
| 235 | Upper-left margin | “Cette notation … les considérations générales …” | “notation” and “considérations” are compressed and only tentatively resolved. | medium |
| 235 | Upper-left margin, lower lines | `u_{ξ,η}`; “de toute façon” | The subscript is heavily inked; “toute” is compressed. | medium |
| 235 | (18), cancelled expression on first line | Two illegible mathematical units | Parts resemble an inner-conjugation expression, but the letters are not recoverable reliably. | low |
| 235 | (18), overbrace label | `η` | `ν`; the handwritten label is small. | medium |
| 235 | L12, “dans le premier …” | `mbr` | `mb`; final abbreviated letter uncertain. | medium |
| 235 | Corollaire 3, group symbol | `\mathcal G` with hat and plus | The group letter is retraced and could belong to another calligraphic/Gothic alphabet. | medium |
| 235 | Corollaire 3, insertion after `u_ξ` | `(ξ normalisé*)` | Singular/plural ending of “normalisé” uncertain. The curved leader attaches the insertion after `u_ξ`, not after “à bouts”. | medium |
| 235 | Corollaire 3, before “commutent” | One deleted illegible word/symbol | A small cancellation cannot be read confidently. | low |

### Scans 236–240

Locations below count manuscript lines approximately from the top of the writing area, excluding archive foliation and printed metadata; display numbers are added when more precise than a line count.

| Scan | Approx. line / location | Reading retained | Alternatives / reason for doubt | Confidence |
|---|---|---|---|---|
| 236 | 3, insertion over deletion | `simples` | The last stroke could be an abbreviation stop; the deleted `que l'on ait` is clearer than the inserted ending. | medium |
| 236 | 5, before `r=0` | `car` | `cas`; the final letter is open and the word is underlined or overwritten. | low |
| 236 | 12, before `=l_0^n=1` | `f` | `f_0`; a low stroke near the foot of the letter may be a subscript. | medium |
| 236 | Corollaire 4, after `dont l'` | deleted `image`, inserted `intersection` | Layering of the correction is partly opaque. | medium |
| 236 | Corollaire 4, `ext. à …` | `la carte` | `la cat.`; a raised terminal stroke or insertion cannot confidently be assigned. | low |
| 236 | Corollaire 4, parenthetical group | `\mathcal M_{0,3}^{+\widehat{\ }}` | The order and placement of the raised plus and hat are uncertain. | low |
| 236 | (23), parenthesis after `\mathcal M` | `(0)` | The zero is overwritten and resembles an omega-shaped loop. | medium |
| 236 | Final display label | `(23)` | Overwriting affects the units digit. | medium |
| 237 | 8–9, two deleted prose fragments | `pour`; `donne` | Strikethrough hides parts of the letters. | low |
| 237 | Even case, deleted factor before `\varepsilon_1^{3n}` | `\sigma_\infty` | The short overwritten factor is not securely identifiable. | low |
| 237 | Odd case, deleted factor after `=` | `\varepsilon_0` | A hat-like cancellation covers the symbol and any exponent. | low |
| 237 | Diagonal lower-left NB | Group `\mathcal M_{0,3}^{!\approx}(0)`; `une`; `au moins il`; `l'autre`; isolated `tout entier`, `reste à voir si` | Several words remain illegible and the overlapping note interferes with the paragraph heading; no full assertion is reconstructed. An independent second reading supports the isolated phrases but does not resolve the initial group expression. | low |
| 237 | Last paragraph heading | `Scholie` | The diagonal marginal writing crosses the underlined word. | low |
| 238 | 7, before `point 0` | `sur le` | `en le`; the connecting strokes of the preposition are weak. | medium |
| 238 | 8, deletion preceding insertion `dont l'image dans` | `et qui sera déterminé` | The first conjunction and the ending of `déterminé` are partly covered by the cancellation line. | low |
| 238 | 9 and subsequent quotient notation | `\mathfrak m_0/\mathfrak m_0^2` | The intended typeface of the small handwritten m is not secure; first occurrence marked in the transcription. | medium |
| 238 | 11, after `\mathbb P^1_{\mathbb Q}` | `)` | A corrected or overwritten closing sign, with no securely visible matching opening parenthesis. | low |
| 238 | 16, correction before `qui détermine` | deleted `ce`, inserted `condition` | The deleted two-letter form is uncertain. | medium |
| 238 | 18, after `signe près` | `ce ser.` | Possibly a rapidly written full form `ce sera` or `ce serait`; it is not expanded. | low |
| 239 | Below (25), canceled set notation | `\{\xi\mid\xi\in\widehat\Pi_{0,3}\text{ sol. de }(14)(15)\}` and two illegible units | Dense oblique cancellation leaves some readable symbols but obscures the continuation and the relation to the overwritten group notation. | low |
| 239 | (26), subgroup argument | `(0)` | The shape again resembles an omega-like loop. | medium |
| 239 | (27), deleted initial expression | `u_{\xi,f}` | The crossed subscript may contain different letters. | low |
| 239 | (27), final factor and beginning of the right-hand parenthesis | `u_0` | `u_\xi`; a long retouched descender beneath the subscript makes the corrected reading uncertain. The later explicit `u_0=u_\xi` is retained. | low |
| 239 | (29), after comma | One illegible canceled unit | Small black overwritten mark, possibly a letter. | low |
| 240 | 2 | `triples` | The beginning of the word is retouched; an underlying earlier reading cannot be separated confidently. | medium |
| 240 | Underlined heading | `Rescholie` | The first syllable and spelling of this heading are uncertain; not silently regularized to `Scholie`. | low |
| 240 | 4 and after (30) | `l'ens.` | The abbreviation for ensemble is legible, but the final point is not clear. | medium |
| 240 | Twice after (30), group containing `\alpha` | `\widehat{\widetilde\Pi}_{0,3}` | Both a tilde-like mark and a hat are visible; their exact ordering/stacking is uncertain. This is not reduced to plain `\widehat\Pi`. | medium |
| 240 | Before canceled calculation | `p. 395' (52)` | The final page digit and prime mark are close together; `395'` is the favored reading. | medium |
| 240 | Canceled first line, last factor | `f''=1` | The tall letter might be `l`; cancellation crosses it. | low |
| 240 | Canceled second line, additional erased initial factor | `\alpha''\rho` | Several strokes of a separately canceled attempt remain before the expansion; exact letters are low confidence. | low |

### Scans 241–244

Approximate line locations count the main handwritten lines from the top, treating a display as one or several lines as its layout requires. Equation numbers are the more reliable locators. “Low” means the proposed reading or the order of a heavily revised passage remains insecure.

| Scan | Approximate line / locator | Reading retained | Alternative / unresolved feature | Confidence |
|---|---|---|---|---|
| 241 | 1, before (33) | Cancelled numeral or mark, `\deleted{\illegible{1}}` | Earlier equation number cannot be recovered | low |
| 241 | 3–6, (34) | Calligraphic `\mathcal G`, `\mathcal M`, `\mathcal N` | The broad curled G-like glyph is not silently replaced by a conventional symmetric-group symbol | medium |
| 241 | 6, after inclusion | Cancelled one-symbol group fragment | Underlying group letter cannot be recovered | low |
| 241 | 9, (35) | `\widehat\Pi_{0,3}` after cancellation | Overwritten predecessor is illegible | low |
| 241 | 9, (35), arrow before N | `\twoheadrightarrow` | `\longrightarrow` redrawn or thickened rather than deliberately surjective | low |
| 241 | 10, revised prose | “sous-extension” inserted over cancelled “extension” | Inserted prefix/word is not completely secure | low |
| 241 | 11–12, below (35) | Cancelled “la” and about seven illegible words | The struck-through abandoned sentence cannot be reliably reconstructed | low |
| 241 | 12–14, before (36) | Cancelled old “(36)”; inserted “On a”; cancelled “aussi”; “une autre str. d’ext. sur” | Revision order and attachment of “On a” are uncertain; “aussi” may have been retained rather than cancelled; “autre” is faint | low |
| 241 | 20, (37) | `\mathcal N_{0,3}^{!\approx}(0)` | The capital visually favors N, but alternative `\mathcal M` remains explicit | medium |
| 242 | 3–4, lower left of (38) | `\mathcal M_{0,3}^{!\approx}(0)` | Initial capital is overwritten | medium |
| 242 | 5, before (39) | “donnée” | “donné”; final e is not distinct | medium |
| 242 | 9–10, revision before “du fait” | Cancelled “i.e.”; inserted “plus particulièrement” | The cancelled abbreviation is faint; only “particulièrement” has a reasonably clear underline | medium |
| 242 | 17, insertion near §41 | `\mathcal E_{0,3}` | Initial capital resembles an epsilon/E-like script character; alphabet is insecure | low |
| 242 | 9–13 | Opening parenthesis before “du fait” | Closing partner is not clearly visible; it has not been supplied | medium |
| 243 | 7–8, after tautological calculation | “veut … revienne” | “voit … revient”; neither ending should be resolved by grammatical preference | medium |
| 243 | 11–12, before “délicate” | “du”; cancelled “la variable”; inserted “paramètre” | “de” is possible; the corrected noun and its predecessor remain tentative. The following feminine “délicate” is not corrected to match the proposed insertion | low |
| 243 | 12–13 | “au priori” | “a priori”; joined strokes are ambiguous | medium |
| 243 | Bottom calculation after (40) | Cancelled `(\sigma_\infty\ell_1^{-1}\sigma_\infty^{-1})`, cancelled underbrace label `\ell_0^{-1}`, and inserted `\ell_0^{-1}` | The replacement overlaps the closing parenthesis; its upper stroke could instead be read as an outer inverse on that parenthesis. The tentative transcription follows the visible subscript 0, without repairing the algebra | low |
| 244 | 2, (41) | `\mu` in exponent and residue class | `j`; both occurrences show overwriting | low |
| 244 | 3–7, (42) and nearby prose | `j` | `\mu`; earlier correction may not have been propagated, but this is not assumed | medium |
| 244 | 4, cancelled line | “α est … (j)=α₃ est l’entier …” | Initial words and one symbol/word at each ellipsis are insecure | low |
| 244 | 13–14, cancelled computation | `(\xi\rho)^{-1}` and `(\rho^{-1}\xi^{-1}\rho)\rho^{-1}` | First and last products are crossed through; the middle `\rho^{-1}\xi^{-1}` is clearer | low |
| 244 | 18–20, before final condition | Cancelled “ceci équiv.” and formula; inserted “on a”; cancelled “que” | Attachment and exact words in this small revision are uncertain | low |
| 244 | 20, equality annotation | `df` | `déf`; tiny letters above equals are hard to separate | low |
| 244 | 22, final numbered display | `(44)` | Numeral is very small/overwritten | medium |
| 244 | Last line | `\{1,\tau_\infty\}` | No prime is clearly visible here, although several preceding occurrences have a prime; no prime is supplied | medium |
| 241–244 | Lower left | `240`, `241`, `242`, `243` retained with `\margin` | These appear to be secondary foliation; the annotator cannot be established from these images | medium |

### Further points preserved without correction

- Scan 227 appears to repeat display number (179); the lower occurrence remains marked uncertain rather than renumbered.
- Scan 230, formula (6), has `\varepsilon_0^r`, whereas its later reprise on scan 231 appears to use `\ell_0^r`; the two readings are retained.
- Scan 234, (16), visibly gives different decorations on the two displayed domains for `\alpha`. The common frame enclosing (14)–(15) is represented by a single mathematical box with the two labels inside it.
- Scan 237 retains the unexpected visible reading `\varepsilon_1^{2n}=0`. The right-hand side has not been changed to an identity element.
- Scan 240, (30), says only “pour ν∈Ẑ conv.” at that point; no additional unit condition is imported from an earlier page.
- Scan 243 has a tentative correction from cancelled “la variable” to inserted “paramètre”, followed by the unchanged feminine word “délicate”. In the calculation below (40), the cancelled conjugator and the proposed replacement `\ell_0^{-1}` overlap and remain low-confidence readings.
- Scan 244, (41), has an overwritten μ-like parameter, whereas the following prose and (42) more closely resemble `j`. They have not been silently unified. No prime is supplied on the final `\tau_\infty` where none is securely visible.

## 3. Abbreviations and abbreviated notation met

The proposed expansions below are editorial explanations confined to these notes. They are not inserted into the transcription. Distinct visible forms, including stops and missing stops, are listed together only to avoid repeating their explanations.

| Form as written | Tentative expansion or meaning |
|---|---|
| `ss-groupe`, `ss-groupes` | sous-groupe, sous-groupes |
| raised `s/` followed by `groupe` (uncertain) | sous-groupe |
| `i.e.` | *id est*, c'est-à-dire |
| `df` over an equality; `df` / `déf` (uncertain) | définition / défini par |
| `cf` | *confer*, comparer / voir |
| `Th.` | théorème |
| `p.` | page |
| `m̄`, represented as `\overline{\mathrm m}` | même |
| `Rmq` | remarque |
| `chgt` | changement |
| `hom.` | homomorphisme |
| `autom.`, `autom` | automorphisme |
| `extᵗ` | extérieurement |
| `ext.` | extérieur(s) |
| `int` | automorphisme intérieur / conjugaison intérieure |
| `int.` | intérieur |
| `Centr` | centralisateur |
| `NB` | *nota bene* |
| `GL` | groupe linéaire général; mathematical notation |
| `§` | section / paragraphe |
| `f. et s.` | faut et suffit |
| `mod`, `mod 2` | modulo, modulo 2 |
| `conv.` | convenable |
| `inv.` (tentative) | invariant |
| `Ker` | noyau |
| `can` | canonique |
| `corr.` | correspondance |
| `l'ens`, `l'ens.` | l'ensemble |
| `mbr` / `mb` (uncertain) | membre |
| `ssi` | si et seulement si |
| `prop.` | proposition |
| `cqfd.` | ce qu'il fallait démontrer |
| `sol.` | solution(s) |
| `½ direct`, represented with `\frac12` | semi-direct |
| `cor.` | corollaire |
| `iso. can.` | isomorphisme canonique |
| `str. d'ext.` (uncertain) | structure d'extension |
| `loc. cit.` | *loco citato*, à l'endroit cité |
| `conj.` | conjugaison |
| `Norm` | normalisateur |
| `équiv.` (uncertain, cancelled) | équivaut / équivalent |

## 4. Legibility assessment

The paragraph order and most uncancelled displays are more secure than short connecting words, pale word endings, and overwritten subscripts. Enlargement makes much of the running prose readable, but it does not reliably separate every letter from a cancellation or a later correction. The exact alphabet of some group symbols and the stacking of their decorations remain less certain than the broad formula layout. The fragment records these limits; it should not be treated as a fully resolved critical edition.

The least trustworthy regions are the opening and bottom corrections on scans 226–227; the cancelled computations and inverse exponents on scans 229–231; the marginal references on scan 232; the additional-condition note on scan 234; the cancelled first formula and marginal prose on scan 235; the diagonal lower-left NB on scan 237; the cancelled material below (25) and at the foot of scan 240; the revision between (35) and (36) on scan 241; the overlapping factor below (40) on scan 243; and the overwritten parameter and cancellations on scan 244. These have explicit uncertainty or illegibility marks. A successful syntax check confirms that the assembled fragment can be processed with definitions for the requested editorial commands; it does not certify disputed readings or the mathematics.

## 5. Research notes — English, separate from the transcription

The following items concern only what is stated, proposed, or left unresolved within the supplied images. Source quotations and locators refer to the manuscript (Grothendieck, 1981); the scans are numbered by filename. “Unproved claim” includes local dependencies and assertions whose proof may occur elsewhere, not a claim that Grothendieck never proved them. Proposed implications and original suggestions have not been checked against the rest of the manuscript or the literature, and no novelty is asserted. They do not supply or alter any transcription reading.

### R01 — Scan 226, paragraph after (178) — Unproved claim / scope requiring clarification

Grothendieck calls μ “le seul invariant abélien qu'on sache lui associer dans le contexte présent.” The qualification about the present context matters: the displayed triangular-matrix decomposition alone should not be read as a universal assertion about every abelian quotient of the full group. A precise formulation would need to specify the allowed invariants and explain how the relevant kernel is being excluded or controlled (Grothendieck, 1981, scan 226).

### R02 — Scan 228, Rmq after (181) — Conjecture / author's proposed investigation

The author asks to “mettre ces scindages canoniques en relation avec le choix d'une uniformisante” at 0. This is an explicit task left open here, with the same question also raised at 1 and ∞. The proposed comparison would have to identify which choice of local parameter realizes the specified canonical section and how changing that choice changes the representative (Grothendieck, 1981, scan 228).

### R03 — Scan 228, (182)–(183) — Unproved claim

The statements “s'applique évidemment sans chgt” and “On aura d'ailleurs” accompany the analogous sections at 1 and ∞ and their transport by ρ. A proof would track the local cyclic subgroups, their normalizers, and the normalization condition under this action, rather than merely rename the punctures. The claim may have supporting material elsewhere in the manuscript; no such support is imported into this transcription (Grothendieck, 1981, scan 228).

### R04 — Scan 228, Rmq — Own idea

Try to formulate the uniformizer question in terms of tangential data at a puncture, then calculate the effect of scaling that datum on the chosen lift and on μ. **Confidence: medium.** The suggested comparison is motivated by the author's local-parameter question and the visible normalizer calculations, but these pages neither identify the necessary datum nor prove such an interpretation; no novelty or established equivalence is claimed (Grothendieck, 1981, scan 228).

### R05 — Scan 230, opening centralizer equality and (6) — Unproved claim

The passage identifies a centralizer of `ε₀^μ` with the indicated procyclic group and uses this to introduce `r ∈ Ẑ`. The subscript specifying the centralizer's ambient group is itself doubtful, and the marginal “on n'a pas nécessairement” explicitly raises an ambient-membership issue. A proof must first fix the ambient group, then justify the centralizer identification and the resulting parametrization of λ (Grothendieck, 1981, scan 230).

### R06 — Scan 230, after the case `x=ℓ₁` — Unproved claim

The phrase “ce qui signifie aussi qu'il existe” introduces a parameter in `Z/2Z` from the conjugation condition on `σ∞`. This uses a centralizer assertion for the involution that is not proved in this passage. Its verification would have to be made in the same ambient group used in the preceding calculation, with the displayed inverse conventions checked independently of the uncertain overwriting (Grothendieck, 1981, scan 230).

### R07 — Scan 230, the two generator calculations — Own idea

A finite-quotient audit could compare the two conjugation conditions for admissible triples and the extracted procyclic and parity parameters. **Confidence: medium.** The displayed equations descend to compatible finite quotients and could reveal convention or factor-order problems, but a finite check would not establish the profinite statement or resolve a palaeographic uncertainty, and it must never be used to silently change the transcription (Grothendieck, 1981, scan 230).

### R08 — Scan 231, (8)–(9) — own idea

The visible transformation laws `r′=r−n` and the tentatively read `i′=i+n mod 2` suggest examining `i+r mod 2` as a quantity independent of the chosen triple. **Confidence: medium**, because the observation follows formally from those laws, but `i`/`α` is overwritten in the source and should be settled before using the formulation. This is a proposed check, not a novelty claim (Grothendieck, 1981, scan 231).

### R09 — Scan 232, margin beside (10) — conjecture (author's explicit question)

Grothendieck asks, “Il faudrait examiner si cette définition coïncide…” with an earlier definition “formulée sans faire intervenir” `φ̂`. The earlier page references are read tentatively as 410′ and 413, and should be verified before comparing the two normalization procedures; the margin does not assert that their equality has been proved (Grothendieck, 1981, scan 232).

### R10 — Scan 232, final paragraph and (10)–(11) — unpursued implication

The author emphasizes that the two relations “ne faisant d'ailleurs pas intervenir f” constrain the other parameters independently of `f`. It is worth tracking precisely how this separation behaves under composition and changes of representatives; the later formula (19) in this span explains the role of `f` through inner conjugation, but does not by itself establish every such compatibility (Grothendieck, 1981, scan 232).

### R11 — Scan 233, kernel sentence following (13) — unproved claim

“En fait, le noyau …” is identified with the invariant subgroup generated by `ℓ₀², ℓ₁², ℓ∞³`. A proof should establish equality with the kernel, not only containment, and specify the intended closure in the profinite setting; the claim is stated without that verification on this page (Grothendieck, 1981, scan 233).

### R12 — Scan 234, Corollaire 2 and margin beside (14)–(15) — unproved claim

The proposed parametrization is qualified in the margin: “il faut de plus la ‘condition’ ‘liminaire’…” (the final adjective remains uncertain). Any proof of the stated correspondence needs the exact additional condition and must show that the displayed generator images determine an admissible automorphism, including the relevant invertibility and end conditions, rather than merely satisfying formal equalities (Grothendieck, 1981, scan 234).

### R13 — Scan 234, (16) — unproved claim

The phrase “l'unique élément” asserts a unique reconstruction of `α` from `ξ=αρ(α)⁻¹`. The displayed domains for `α` differ between the left and right parts of the same line; after establishing the intended domain from the manuscript, a proof would need to determine the image and fibres of that map. No domain correction has been made in the transcription (Grothendieck, 1981, scan 234).

### R14 — Scan 234, margin beside (16) — own idea

The observation “on n'a pas vraiment besoin de α,β” suggests testing the construction directly in `ξ`-coordinates, using the explicit generator images rather than repeatedly choosing auxiliary lifts. **Confidence: medium**, because (17)–(19) support this as a working approach, while the preceding existence and uniqueness statements still need their exact hypotheses. This is a proposed method for checking the argument, not an established new construction (Grothendieck, 1981, scan 234).

### R15 — Scan 235, Corollaire 3 — unproved claim

The normalized `u_ξ` are characterized as exactly those automorphisms satisfying (20) and “qui de plus normalisent L₀”. The corollary is stated here without its converse proof on this page; the continuation must be checked for the elimination of any remaining inner-conjugation ambiguity (Grothendieck, 1981, scan 235).

### R16 — Scan 235, (20) — own idea

The exact identity `φ̂∘u_ξ=u_ξ∘φ̂` suggests checking whether composition preserves both this commutation relation and the chosen normalization, so that the preferred representatives form a subgroup. **Confidence: high for this being a concrete verification to attempt**, because (20) and the explicit normalizer condition provide testable hypotheses; it is not presented as an established or novel result here (Grothendieck, 1981, scan 235).

### R17 — Scan 236, Corollaire 4 — Unproved claim on this page, continued on scan 237

The assertion that the normalized elements “forment un sous-groupe” and that the intersection with the inner subgroup “est réduit à {1}” yields the displayed isomorphism (23). The subgroup assertion needs compatibility of normalization with composition and inverses; the next scan explicitly supplies an argument for triviality of the intersection, so this is a local proof dependency rather than an assertion that the manuscript omits all justification (Grothendieck, 1981, scan 236).

### R18 — Scan 237, proof of Corollaire 4 — Unproved claim / prior dependency

The reduction to `\alpha=\beta=l_0^n` explicitly invokes “prop. de la page 404”; that proposition is outside this assigned scan range. The subsequent even/odd calculation also uses that the displayed equality between powers forces `n=0`, so a full verification must identify the relevant intersections and orders in the ambient profinite group; the visible `\varepsilon_1^{2n}=0` is a transcription issue to compare with the surrounding argument, not a correction made here (Grothendieck, 1981, scan 237).

### R19 — Scan 237, lower-left NB — Conjecture / question, only partially legible

The note includes “tout entier” and “reste à voir si”, apparently qualifying the scope of the section discussed in the main paragraph. Because several intervening words and group decorations are obscured, it would be unsafe to formulate a precise mathematical conjecture from this note without a better image or an independent reading (Grothendieck, 1981, scan 237).

### R20 — Scan 238, lines 5–11 — Conjecture / expected identification

“Il faudrait vérifier que cette section canonique est associée au choix d'une uniformisante” asks for a geometric identification of the section at the point 0. A proof would have to compare the group-theoretic normalization with the section associated to a local parameter and explain precisely which class in `\mathfrak m_0/\mathfrak m_0^2` determines it (Grothendieck, 1981, scan 238).

### R21 — Scan 238, lines 11–19 — Question left for later

The author writes “il faudrait déterminer cet élément”, proposes a basis over `\mathbb Z` as well as over `\mathbb Q`, and ends “Mais est-ce bien le bon ? Il faudrait y revenir !” after the alternatives `z` and `-z`. The integral condition is expected on this page to leave a sign ambiguity; neither the correct sign nor the asserted compatibility with the previously constructed section is settled here (Grothendieck, 1981, scan 238).

### R22 — Scan 238, final question — Own idea (confidence: medium)

A concrete way to investigate the sign question would be to compute the actions associated to `z` and `-z` on a small common finite quotient of the relevant fundamental group and compare them with the normalized section's action. This is a proposed diagnostic, not a claim of sufficiency or novelty: agreement on such a quotient could fail to distinguish sections that differ at deeper levels (Grothendieck, 1981, scan 238).

### R23 — Scan 239, (26)–(29) — Unpursued implication

The statement “de façon unique” gives coordinates consisting of a normalized representative and an inner-conjugating element `f`. One can therefore ask for an explicit multiplication rule on these two coordinates, with special care over the order of composition and the inverse in `int(f^{-1})`; the next scan begins to address the normalized component rather than spelling out the entire two-coordinate product here (Grothendieck, 1981, scan 239).

### R24 — Scan 240, recap and (30) — Unproved claim / dependence on the preceding construction

The recap asserts an “en corr. 1-1” parametrization by solutions of the two equations and then an equivalent description in terms of `\alpha`. A stand-alone proof would need both directions of the passage `\xi=\alpha\rho(\alpha)^{-1}` in the specified decorated subgroup, together with verification that the constructed `u_\xi` is an automorphism satisfying the required normalization; the recap refers back to the construction rather than proving these points anew (Grothendieck, 1981, scan 240).

### R25 — Scan 240, (31)–(32) — Own idea (confidence: high as an algebraic check, not a novelty claim)

The action on `\rho` in (31) gives a direct check of the order of multiplication: applying `u_{\xi'}` to `u_\xi(\rho)` yields the parameter `u_{\xi'}(\xi)\xi'`. This can be compared with the continuation on scan 241 and with the canceled `\alpha''` calculation, and would be a useful check before deriving a full multiplication rule in the coordinates of (27) (Grothendieck, 1981, scan 240).

### R26 — Scan 241, (35)–(37); unproved claim

The passage says that the subgroup which is a “section de (24)” is also a “section de (36), d’où un iso. can.” A proof checked in isolation would need the exact inclusion of the two extensions, the induced map of quotients, and the statement that the proposed subgroup meets the larger kernel trivially and projects onto the required quotient. The badly revised prose immediately before (36) should be resolved before using it as a definitive formulation (Grothendieck, 1981, scan 241).

### R27 — Scan 242, (38)–(39); unproved claim

The assertion “Φ est un homomorphisme de groupes” is justified by actual commutation with the comparison map. To check it independently one must fix the author's multiplication convention for the two semidirect products and verify the corresponding equivariance identity; outer commutation alone would leave conjugation data to track (Grothendieck, 1981, scan 242, eqs. 38–39).

### R28 — Scan 242, closing paragraph; conjecture / expectation

Grothendieck writes “on devrait pouvoir vérifier l’égalité de ces homomorphismes” and specifies “de façon effective.” This explicitly leaves a comparison with the homomorphism in §41, p. 316′, for further work; the earlier construction and its indicated restrictions would need to be retrieved before assessing the equality (Grothendieck, 1981, scan 242).

### R29 — Scan 243, middle paragraph; unproved claim / acknowledged gap

The existence of the quantity β, described as “délicate” after a revised noun, is said to rest on “des fondements qui n’ont pas encore été établis.” The immediate research task is to identify those foundations from the preceding definitions and determine exactly which existence or uniqueness assertion is being used; the calculation itself should not be treated as repairing the acknowledged gap (Grothendieck, 1981, scan 243).

### R30 — Scan 243, first paragraph and (40); unpursued implication

The text compares imposing the commutation condition at `x=\ell_1` with imposing it at `x=\ell_\infty`, after the condition at `x=\ell_0` becomes tautological. The final scan begins the latter calculation, but this packet does not supply a separate complete comparison of the two resulting tests with every normalization and inner conjugation convention displayed (Grothendieck, 1981, scans 243–244).

### R31 — Scan 244, (41)–(43); unproved claim

The text says “alors on a nécessairement” and then gives the two nonzero residue possibilities modulo 3. A self-contained check should identify the order of `\rho`, the precise automorphism hypothesis on `u`, and the conversion from that residue to `\alpha_3`; it should also resolve the visible change between `j` and `\mu` before treating the formulas as a single definition (Grothendieck, 1981, scan 244, eqs. 41–43).

### R32 — Scan 244, final display and sentence; unpursued implication

The calculation ends with a particular element of the extended group that “commute à ρ.” No description of that centralizer follows within the supplied packet; determining it would be needed before converting this last condition into a more explicit parametrization (Grothendieck, 1981, scan 244).

### R33 — Scans 242–244; own idea — confidence: medium

After uncertain symbols have been resolved, one could check the two proposed commutation tests in finite quotients, explicitly retaining the order of factors and the normalization data. This would be a way to locate convention errors or failures in particular quotients; it would not by itself establish the profinite statement. The reason for the suggestion is the packet’s explicit generator formulas and the unresolved comparison, rather than any claim that the method is new (Grothendieck, 1981, scans 242–244).

### R34 — Scan 242, (39); own idea — confidence: high for the formal check, conditional on the conventions

Write out both semidirect-product multiplication laws and calculate the image of a product under `\Phi(u\cdot a)=u\widehat\varphi(a)`. The resulting equality isolates the exact equivariance assertion used in the manuscript and gives a compact criterion against which the earlier §41 construction can be compared; this is a proposed verification, not a claim that the earlier construction has already been checked (Grothendieck, 1981, scan 242).

## Primary-source reference

Grothendieck, A. (1981). *La Longue Marche à travers la théorie de Galois* [Unpublished manuscript; supplied scans 226–244 from cote 140-3, pages 293–650]. Université de Montpellier.

The year, archival title, and cote are reproduced from the supplied task description; they have not been independently verified. All page-specific citations above refer to the supplied image filenames, not to a published edition or to the printed archive footer numbering.

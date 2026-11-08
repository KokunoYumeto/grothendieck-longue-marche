# LM_C3-321-339 — Editorial and research notes

## 1. Scope, source, and foliation

This edition covers all **19 supplied files, scans 321–339**, in filename order. The LaTeX file is a fragment: it has no preamble or document environment and uses the editorial macros specified in the supplied prompt, together with standard mathematical LaTeX and `tikz-cd`. It begins and ends with the manuscript's supplied continuation; no missing preceding or following text has been supplied.

The scan numbers are not the lower numbers visible on the sheets. Both handwritten numerical series are recorded with `\mspage` where visible. This preserves their physical presence without claiming that the lower series is in Grothendieck's hand. The printed archive captions, border, URL, and institutional footer are not manuscript text and have not been transcribed.

| File scan | Upper handwritten number | Lower handwritten number |
|---|---|---|
| 321 | — | 320 |
| 322 | 461 | 321 |
| 323 | 462 | 322 |
| 324 | — | 323 |
| 325 | 463 | 324 |
| 326 | — | 325 |
| 327 | 464 | 326 |
| 328 | — | 327 |
| 329 | 465 | 328 |
| 330 | — | 329 |
| 331 | 466 | 330 |
| 332 | — | 331 |
| 333 | 467 | 332 |
| 334 | — | 333 |
| 335 | 468 | 334 |
| 336 | — | 335 |
| 337 | 469 | 336 |
| 338 | — | 337 |
| 339 | 470 | 338 |

**Reading conventions.** `\unsure` marks a provisional reading; alternatives separated by `|` are genuinely unresolved. `\illegible{n}` estimates the number of unreadable words or, in a mathematical passage, unreadable symbols. A cancelled passage remains inside `\deleted` even when it contains an earlier local cancellation. The slanting marginalia are linearized in reading order; uncertain attachment is noted below. Arithmetic cancellation strokes are retained as deletions rather than silently evaluating or simplifying the calculation.

The scalar glyphs adopted as Latin *v* and *w* may be Greek ν and ω. Their ambiguous alphabet is marked explicitly throughout the mathematical text, including repeated matrix entries; this records an uncertainty in identification, not a claim that the manuscript switches alphabets. A larger already-marked doubtful expression is not given nested marks solely for these letters. The small equality annotation read as `dfn` is retained as that abbreviation.

## 2. Table of doubts

Locations refer to the manuscript's approximate prose or display rows, or to its equation numbers and marginal positions. They are not LaTeX source-line numbers. Repeated scalar-alphabet doubts are grouped in the table; the inline markers retain their individual locations. Confidence concerns the reading of the ink, not the mathematical truth of the passage. A blank alternative means that no defensible second reading was found.

### 2.1. Scans 321–326

| Scan | Approximate line / location | Reading | Alternatives / limitation | Confidence |
|---|---|---|---|---|
| 321 | 2, (38) | `\delta v` | `\delta_0`; a following short curved character is not secure | low |
| 321 | 4–5, (39), first denominator | `-vd^2+cd+d^2` | `-vc^2+cd+d^2`; the first squared letter resembles a cursive d | low |
| 321 | 4–5, (39), second denominator | `-va^2+cd+d^2` | `-vc^2+cd+d^2`; the denominator has not been harmonized to the first | low |
| 321 | 4–5, (39), first matrix upper right | Inserted `B/D` over a deleted expression | Deleted symbol not recoverable | low |
| 321 | 9, pair after “la donnée de” | `\varepsilon` | Heavily overwritten Greek character | medium |
| 321 | 11, display number | `(40)` | Number deformed at left; sequence alone is not grounds for certainty | medium |
| 321 | 19, after “on aura” | Deleted word marked illegible | One word or symbol | low |
| 321 | 22, after the sentence ending with epsilon | Deleted isolated symbol | Could be a pen trial rather than a deleted mathematical letter | low |
| 322 | 1 | `\mathcal G^{*}_{\rho,\sigma}` | Script form and superscript are not secure | medium |
| 322 | 5–6, above `A_\sigma` | `ss-schéma` | Initial abbreviation may differ; written above the line | medium |
| 322 | 6, after `A_\sigma` | Deleted word marked illegible | One short word | low |
| 322 | 9, struck-through phrase before mu | “compléter prenant” | Two words; exact second ending uncertain | low |
| 322 | 9, after `\varepsilon/U_0` | Deleted phrase marked illegible | Approximately two words | low |
| 322 | 17, before “peut prendre” | “en” | “ne”; a short horizontal stroke is the only substantial visible form | low |
| 322 | 19, final matrix upper right | `S_0` | `C_0`; the glyph differs from clearer S on the preceding sheet | medium |
| 323 | 2, enumeration | `1^\circ)` | Overwritten numeral | medium |
| 323 | 7, rank of M | `4` | `1`; the digit has a long sloping stroke but no clear closed junction | medium |
| 323 | 8, between sections and the displayed pair | Inserted word marked illegible | Short slanting interlinear addition, approximately one word | low |
| 323 | 9, before first formula | `a)` | Could be an altered enumeration mark | low |
| 323 | 13, deletion before “en chaque fibre” | Two illegible words | Strikes overlap inserted text | low |
| 323 | 14, “inéquivalente à” | `\widetilde\varepsilon_0` | `\widetilde\varepsilon_1`; the apparent zero has not been corrected on mathematical grounds | medium |
| 323 | 16, before “distinctes” | One deleted illegible word | Possibly a form of “partout,” but not adopted | low |
| 323 | First slanting marginal NB | “réguliers”; “de façon”; underlined “unique”; `G` | Overlapping additions; the group letter can be `P`. “unique” follows the phrase before the lifted pair; its attachment was revised on reinspection. | low |
| 323 | First marginal NB, interline | “avec” followed by `\widetilde\sigma(\varepsilon_0)=\widetilde\rho(\varepsilon_0)=\varepsilon_1` | The three epsilon terms may also carry tildes; the equality sequence is cramped and overlaps the prose. | low |
| 323 | First marginal NB, near “canoniques” | `\illegible{1}` for entangled residual ink | Approximately zero to one additional word: these marks may instead belong to “avec” or its overlapping formula. The insertion attachment is uncertain. | low |
| 323 | (3), before `\mathrm{Gl}(2)_S` | Deleted symbol marked illegible | Could be an earlier group label | low |
| 323 | Second slanting marginal NB | Deleted “n'est pas vraie” | Strike and insertion attachment are not fully secure | low |
| 323 | Second marginal NB | “tte section” | Could be plural “ttes sections” | low |
| 323 | Second marginal NB, last two lines | `\tau`, `2\tau=0,\ \tau^2=0` | Letter and the first coefficient need reinspection; conditions are read conservatively | low |
| 324 | 2 | “tout système” | First word has a stroke across it; deletion status uncertain | low |
| 324 | 2, deleted list | Four illegible entries | Replaced above the line by `v,w,v',w'` | low |
| 324 | (6), first subscript | `1` | `0`; overwritten black subscript | medium |
| 324 | (9), after N | Deleted isolated symbol | One short mark; may be an abandoned subscript | low |
| 324 | (11), last value | `v'` | `-v'`; a leading stroke could be a minus | medium |
| 325 | After (15), before (16) | Deleted word marked illegible | Approximately one word | low |
| 325 | Between (17) and (18) | “en car. rés. est ≠2” | The connective and abbreviation sequence are difficult; no grammatical normalization made | low |
| 326 | 5, after “précédentes” | Deleted word marked illegible | One overwritten short word | low |
| 326 | 6, after “qui” | “reviennent” | “mènent” | medium |
| 326 | 8 | “se tourner vers” | Middle word's compressed strokes remain doubtful | medium |
| 326 | (21), first matrix label | Deleted rho, inserted sigma | Overwriting rather than a clean caret insertion | medium |

### 2.2. Scans 327–332

| Scan | Approximate line / location | Reading | Alternatives / limitation | Confidence |
|---|---|---|---|---|
| 327 | Top equivalence scheme, (22) | `v,w` and their primes | The rounded handwriting can resemble Greek nu/omega. Every ambiguous occurrence is explicitly marked in the transcription with `\unsure` and both the Latin and Greek alternatives; the notation has not been silently normalized. | medium |
| 327 | Upper-right addition to (22) | Deleted `rho^3=-1`; replacement `rho^2-rho+1=` | Last symbol and right border are clipped; direction of the diagonal double arrow is less secure than the visible endpoints. | low |
| 327 | Proof, approximately line 3 | `chacune` | Compressed letter sequence; no reliable distinct alternative. | medium |
| 327 | Proof, after `du fait que` | Unreadable deletion, one word | Overwriting obscures the former reading. | low |
| 327 | Proof, after `sigma^2=v id` | Unreadable deletion, approximately two words | No secure reconstruction. | low |
| 327 | Before matrix preceding (23) | Deleted `rho=` | The cancelled mark is short and may include one additional stroke/symbol. | low |
| 328 | Heading after the opening paragraph | `Remarques` | Singular `Remarque`; the ending is compressed. | medium |
| 328 | Paragraph after (27) | `mbs` | Abbreviation appears to denote the two members; middle/final strokes indistinct. | medium |
| 328 | Unnumbered product after `On a d’ailleurs`, resulting matrix lower right | `w` with an apparent prime | A short separate stroke could be a prime or a pen mark; the entry is explicitly doubtful rather than corrected by multiplication. | medium |
| 328 | After `OK. Composant (25)` | Insertion `(sous la forme rho epsilon_1=rho^2 sigma)` | The hook appears to attach this parenthesis after (25); attachment is less secure than its text. | medium |
| 328 | Before final matrix | Deleted `l'`, inserted `Essayons de prouver`, deleted `résulte`, inserted `par`, deleted `d'` | Several overwritings overlap; exact deleted initial article and verb are uncertain. | low |
| 328 | Final matrix, lower-right entry | `-w(w^2+2v)+v-w^2` | Plus before the final square is also possible; the coefficient within the first parentheses is overwritten; retain doubt rather than calculate it into existence. | low |
| 328 | Final inverse-unipotent matrix, upper-right entry | `-1/v` | Right edge clipped and fraction overwritten. | low |
| 328 | Last two lines | `rho^2 sigma=-epsilon_0^{-1}` | A short stroke may instead belong to the epsilon, yielding no minus sign. | low |
| 328 | Last line | `cela implique` / `ce qui implique`; deleted `d'où` | Former phrase compressed; latter overwritten by the insertion `i.e. v=-w^2`. | low |
| 329 | Initial matrix, lower-right entry | Inserted `w^3` | Underlying deleted formula unreadable. | low |
| 329 | Top amended sentence and right margin | Deleted equivalence ending `ssi w=1 OK.`; partial marginal reading | Several superposed attempts and some clipped writing; the complete sequence cannot be recovered reliably. | low |
| 329 | Before `rho^3 sigma` | Deleted two-word phrase; deleted `u` before `rho epsilon_0^{-1}` | Overwritten and unresolved. | low |
| 329 | After `(7)` | `epsilon_0=-sigma^{-1}rho`; final `sigma` in the inverse relation | First product is overwritten; a cancelled glyph, perhaps sigma, lies between the minus and inverse rho in the second formula; the final sigma may have a small subscript 0 or merely a pen mark. | low |
| 329 | After (28) | Deleted `cette` | Could be a short superseded connector rather than this word. | low |
| 329 | (31) | Minus sign in `rho^3=-w^3 . 1` | The sign is retraced/overwritten. | medium |
| 329 | (32) | Deleted `v=-w^2` | End of the cancelled term is overwritten; the same condition is reinserted below. | medium |
| 330 | (34), trace condition | `Tr` written over a deleted `det` | The earlier glyph is partly obscured and marked doubtful. | medium |
| 330 | After (35) | `impliquent` | Singular `implique` is also possible; the inserted subject was not used to regularize the verb. | medium |
| 330 | First equation in the cancelled lower block | Equation number `36` | The overwritten number could be `30`. | low |
| 330 | Last equation | Equality sign; deleted `det` | Sign is heavily retraced and could visually be a not-equal sign; the cancelled short term is obscure. | low |
| 331 | (36), first letter | Sigma over an earlier rho | Earlier descender remains visible; exact state of the overwritten letter is uncertain. | medium |
| 331 | Paragraph after (37) | `lin` with superscript-like `t` | Abbreviation for linear independence; suffix only a short raised stroke. | low |
| 331 | Same line, matrix algebra | `en M_2(underlined O_S)` | `de` possible for the preposition; exact alphabet of M and O is not secure. | medium |
| 331 | Before (38) | `De` followed by the same-sign / barred-m abbreviation | The mark resembles two short horizontal strokes; preserved with a doubt rather than expanded. | medium |
| 332 | Cancelled initial heading | `fondateur` | `fondamental`; the fast final strokes do not securely resolve the adjective. | low |
| 332 | Cancelled theorem, insertions above the line | `(sur schéma S)` and `une algèbre` | The short phrase before `S` and the first word above `associées` are compressed. The stroke through `une algèbre` has been treated as a cancellation; the curves enclosing `associées` are doubtful parentheses and may instead be an insertion callout. | low |
| 332 | (41), after first `régulier` | Deleted `i.e.` | Retraced short abbreviation may contain a different final stroke. | low |
| 332 | Before (42) and before (44) | `M` | Script/calligraphic M is also possible. | medium |
| 332 | Left margin beside (42) | `nilp.` with superscript-like `ts` | The raised ending is compressed; the rest reads `i.e. leur det et leur tr sont nuls`. | medium |
| 332 | (44), deleted attempted second condition | `2°)(rho+sigma)` | The start is heavily crossed out and might include further symbols. | low |
| 332 | (44), right-hand scratch calculation | Deleted double implication and `rho+sigma=`; overwritten scalar `u` | Last scalar is heavily retraced; the following membership line reads `u in Gamma G_m`. | low |
| 332 | Before (45) | Deleted `iso` | Only a few blacked-over strokes remain; retain doubt. | low |
| 332 | Label before the images of rho-zero and sigma-zero | `46` | The last digit is overwritten and may read `48`; its anticipated place in the sequence has not been used to decide. | low |

### 2.3. Scans 333–335

| Scan | Approximate line / location | Reading | Alternatives / limitation | Confidence |
|---|---|---|---|---|
| 333 | Opening, before (48) | `où` followed by one cancelled word | Cancelled word unreadable | low |
| 333 | (48), first member | `(ε₀)₀` | Parenthesis and second zero are overwritten | medium |
| 333 | (48), second member | Cancelled `(ε₁)₀`, replaced above by `(ε₁)₀ = −ρ₀σ₀⁻¹` | Precise cancelled subscript is difficult to separate | medium |
| 333 | Theorem, line 3 | `associées` | Ending could be `associés`; no normalization made | medium |
| 333 | Theorem, line 3 | `alg.` | Abbreviation after `une` is compressed | medium |
| 333 | Definition 1, first line | Inserted `triplet` | Underlying deleted word is unreadable | low |
| 333 | Cancelled display before (49) | Original number `49`; `régulier` | Number overwritten; word ending covered by cancellation | medium |
| 333 | (51) | Deleted `partout` | Cancellation obscures ending | medium |
| 333 | (51), right margin | Deleted `sur les`, inserted `en chaque` | Overlap makes deleted wording uncertain | medium |
| 333 | Beside nilpotent display | `N₀ et N₁` | Connector is a small raised and overwritten mark | low |
| 333 | Last line | `de G` | `dans G` possible | medium |
| 334 | Opening line 2 | Deleted `cinq` | Letters partly overwritten | medium |
| 334 | (54), cancelled line | Final `sont` | Last word lies under long cancellation stroke | medium |
| 334 | (54), before `nilpotent` | Deleted `unip.` | Short abbreviation severely crossed out | low |
| 334 | (54), following parenthesis | One deleted mark before `ε₁` | No defensible reading | low |
| 334 | (55), initial mark | One cancelled mark | It may be a redundant Greek letter rather than a word | low |
| 334 | (56), boxed polynomial | `ρ² + ρ + 1 = 0` | The first sign has been marked `+\|-`; the visible extra stroke supports plus, notwithstanding the surrounding mathematics | medium |
| 334 | Definition 3, numeral | Cancelled `3` followed by `3)` | Several overlapping numeral strokes | low |
| 334 | Definition 3, designation | `standard` | Fast underlined word; retain uncertainty | medium |
| 334 | After (57), projected triple | `ε̃₀` | Subscript after this tilde letter is very faint | medium |
| 334 | Last paragraph, insertion | `le diagramme comm. d'` | Ending of abbreviation `comm.` uncertain | medium |
| 335 | (58), left vertical connector | Vertical isomorphism sign, represented by `\wr` | There is no confidently visible full arrow shaft; transcription uses a phantom diagram edge | medium |
| 335 | After theorem, cancelled word | `réflexions` | Cancellation and abbreviated ending obscure full word | low |
| 335 | Same paragraph | `du présent` | `des présent` possible from ink; not grammar-corrected | medium |
| 335 | Before displayed domain `Gl(2)` | Deleted `isom.` | Crossed-out initial letters are faint | low |
| 335 | Projective parenthetical map, right edge | Target `G` | `PG` possible; leftmost letter may be covered / abbreviated | low |
| 335 | After `(donc aussi sur ε₀)` | Left-facing arrow-like sign | Could be a relocation mark rather than a mathematical symbol | low |
| 335 | `la … chose` | Barred m sign | The mark also resembles `=`; both retained | medium |
| 335 | (59), before `Gₘ` | One cancelled symbol | Possibly `μ₂`, but insufficient ink remains; left illegible | low |
| 335 | Explanation of (59) | `réduite` | `réduit` possible; terminal stroke unclear | medium |
| 335 | Before (60) | `resp.` | Abbreviation is very compressed | medium |

### 2.4. Scans 336–339

| Scan | Approximate line / location | Reading | Alternatives / limitation | Confidence |
|---|---|---|---|---|
| 336 | Opening line | ss-schémas | Abbreviated prefix before “schémas”; possibly gr.-schémas. | low |
| 336 | Opening, above “par” | respᵗ | Small inserted abbreviation with a raised terminal stroke. | medium |
| 336 | Opening, third line | Gl(2)_S | Alphabet / numeral in the group notation is faint. | low |
| 336 | Right margin beside (61) | aura; nécᵗ | Verb favours “aura” on independent rereading; the contraction and final superscript remain uncertain. | low |
| 336 | First line of Rmq | Vu ces résultats, | Overwritten phrase; five words beneath are not recoverable. | low |
| 336 | Before (62) | la / les; R | Article and parenthetic label unclear. “seule” is an insertion. | low |
| 336 | Right of (62) | (?) | Heavily crossed small parenthesized annotation. | low |
| 336 | Final prose, before (63) | se remplacer | Verb ending and preceding short word faint. | medium |
| 337 | Opening, third line | l'ens. / l'une | The compressed letters do not securely distinguish an abbreviation for “ensemble” from “l'une”; punctuation likewise unclear. | low |
| 337 | After (64) | n'implique | Compressed verb and ending. | medium |
| 337 | Parenthetic insertion after (64) | (51) / (52) | Final digit in the cross-reference; independent rereading favours 51. | low |
| 337 | Between (65) and (66) | idempotent | Beginning overwritten. | medium |
| 337 | Left oblique NB margin | peut-être; que dans; premières; (64); doit exiger que; non homothéties | Several superposed strands; word order and links not secure. Unrecoverable words are separately marked in the transcription. | low |
| 337 | NB margin, trace of ρ | 0 / 1 | Ink looks like zero; mathematical expectation was not used to resolve it. | low |
| 337 | Between (67) and (68) | strictᵗ unipotent, replaced by unipotent régulier | Cancellation and overwritten replacement overlap. | low |
| 338 | Opening line, cancelled formula | ρ − 1 | Dense cancellation. | low |
| 338 | Rank-one paragraph | [one illegible word]; dit (cancelled) | Reworked transition after “donc” and before “que N est”. | low |
| 338 | Tensor description | calligraphic M | Exact script alphabet not secure. The dual is written as a check over F, not modernized to F∨. | medium |
| 338 | Below Tr σN = 0 | σ² + σρ = σρ − 1 | A small linking stroke attaches this below σN; recorded as an insertion after the displayed relation. | high (content), medium (placement) |
| 338 | Prose after (69) | pour | Beginning heavily overwritten; possible cancelled antecedent. | low |
| 338 | (70), first entry of conjugating matrix | a | Appears as a very short stroke; doubtful even though the later repeated matrix is clearer. | medium |
| 338 | (70), group of u | ΓSl(2) | Γ and the group lettering are compressed. | medium |
| 339 | Right of matrix N − 1 | inv. | Abbreviated qualification beside the inverse formula. | medium |
| 339 | (72), after N² = N | cancelled equivalence arrow | Small overwritten mark; arrow reading uncertain. | low |
| 339 | First line of determinant expansion | plus in (bd + ac)²; cancelled +1 | Plus is faint and cancelled addition heavily overwritten. | low |
| 339 | Second line of determinant expansion | − / = | Overwritten horizontal sign; both possibilities retained. | low |
| 339 | Expanded determinant, far right | b²d² (cancelled) | Term reaches the black image border; terminal exponent partly clipped. | low |
| 339 | Matrix before (74) | ρσ | Both letters overwritten. | medium |
| 339 | (74), first trace | σρ | Product letters superposed / corrected. | medium |

| Scan | Approximate line / location | Reading | Alternatives / limitation | Confidence |
|---|---|---|---|---|
| 321–333 | Repeated scalar parameters in the formulas | Latin `v`, `w` | Greek ν, ω; uncertainty is marked throughout the final fragment. | medium |
| 323 | Lower NB*, insertion after “L'unicité” | `de v,w (i.e. de ρ₀,σ₀)` | Two separate coefficient signs and a comma favour this reading over φ; the alphabet of v,w remains doubtful. | medium |
| 333–334 | Small annotations above defining equalities | `dfn` | Scan 333 is clearer; scan 334 has superposed/cancelled writing. No expansion to “définition” is made in the transcription. | medium |

## 3. Abbreviations encountered

Expansions here are editorial aids only. They are not substituted into the transcription. Distinct graphic forms are retained as distinct entries.

| As written / represented | Possible expansion or meaning |
|---|---|
| i.e. | id est |
| cf | confer / compare |
| p. | page |
| dfn (above an equals sign) | définition / equality by definition |
| tt | tout |
| tte / ttes | toute / toutes |
| loc.t | localement |
| ss-schéma (uncertain) | sous-schéma |
| inv | inversible |
| car. rés. | caractéristique résiduelle |
| NB | nota bene |
| Tr | trace |
| det | déterminant |
| Centr | centralisateur |
| Norm | normalisateur |
| id. | identité |
| Gl, Sl, GP | General linear, special linear, and the manuscript's projective linear notation; retained as written rather than standardized to a different notation |
| `Dém.` | Démonstration |
| `diff` | différence |
| `id` | identité |
| `p.ex.` | par exemple |
| `mbs` (uncertain) | membres |
| `inv.` | inversible |
| `int` | automorphisme intérieur |
| `ssi` | si et seulement si |
| `OK` | accord / vérification concluante |
| `lin` with uncertain superscript `t` | linéairement |
| barred-m sign (uncertain on scan 331) | même |
| `nilp.` with uncertain raised `ts` | nilpotents |
| `iso.` | isomorphisme |
| `alg.` (uncertain) | algèbre |
| `rg.` | rang |
| `dfn` over an equality | par définition |
| `tte` | toute |
| `unipot.` | unipotent |
| `rég.` | régulier |
| `homoth.` | homothétiques |
| `resp.` | respectivement |
| `comm.` (uncertain) | commutatif |
| `isom.` (cancelled, uncertain) | isomorphisme |
| barred m / equals-like sign (uncertain) | même |
| Rmq | remarque |
| respᵗ (uncertain) | respectivement |
| nécᵗ (uncertain) | nécessairement |
| ss-schémas (uncertain) | sous-schémas |
| hom. | homomorphismes |
| fppf | fidèlement plat et de présentation finie |
| l'ens. (uncertain alternative) | l'ensemble |
| locᵗ | localement |
| bis | suffix for a repeated equation number |

## 4. Legibility and editorial limits

The continuous prose and large matrices are usually more legible than the annotations, word endings, and overwritten signs. Each scan was read as a whole and checked against enlarged regions where necessary; independent rereading was concentrated on the dense margins and the revised algebra. The transcript covers every supplied page, but it does **not** recover every word: unresolved spans remain visibly marked.

The least secure areas are the denominators in scan 321, both slanting NB notes on scan 323, the clipped right edge of the equivalence scheme on scan 327, the amended matrix and final prose on scan 328, the upper-right working notes on scan 329, the cancellations around the definitions on scans 333–334, and the long oblique NB on scan 337. The rank-one paragraph on scan 338 contains a genuinely unreadable reworked transition. Scan 339 is relatively clear in its principal matrices but has an overwritten continuation sign and a clipped term in the determinant expansion.

The lower argument on scan 330 is globally crossed out; its marginal “faux” is retained. The plus sign in scan 331, equation (40), is preserved despite the minus signs nearby. The boxed sign on scan 334, equation (56), remains doubtful. These discrepancies have not been repaired by algebra. Fine distinctions in accents, final plural strokes, scalar alphabets, and the boundaries of overlapped insertions remain less secure than the main structural reading.

## 5. Research notes — English, separate from the transcription

These notes describe questions, claims, and possible investigations prompted by **these supplied pages only**. “Unproved” or “unpursued” means that the indicated passage does not supply the relevant argument or development; it does not assert that the matter is unresolved elsewhere in the manuscript or in the literature. No published transcription was used to settle the ink, and no novelty is claimed. All manuscript citations refer to Grothendieck (1981) as identified in the source reference below; doubtful quotations must be read with the corresponding transcription markers.

### 5.1. Scans 321–326

All source references below are to the supplied scans of Grothendieck's manuscript, not to a published transcription. The suggestions are working questions, not novelty claims or established conclusions. The quoted passages themselves should be read with the uncertainty markers in the transcription when applicable.

1. **Scan 321, remark after (39) — unpursued implication.** The sentence “la donnée de β seule … ne permet pas de récupérer μ” is followed by `μ = ε/U₀` in (42). It is worth describing precisely the residual sign information lost on retaining β alone and the locus on which `U₀` is invertible; this is the immediate parameter-recovery issue raised by the text (Grothendieck, 1981, scan 321, remark and (42)).

2. **Scan 322, middle paragraph — unproved claim.** The assertion that “ζ pourra bel et bien s'écrire loc.t sous la forme αρ(α)⁻¹” refers to the theory in (II) and a lemma on p. 455. A verification would need the intended local topology and the hypotheses ensuring local conjugacy, together with the stated `Tρ` indeterminacy; this passage does not provide that proof (Grothendieck, 1981, scan 322, middle paragraph).

3. **Scan 322, last paragraph — own idea.** Study the parameter set `ε ∈ μ₂` over nonreduced bases and in residue characteristic 2 before interpreting the final formula as a choice of two ordinary signs. **Confidence: medium**, because the manuscript explicitly uses the group scheme notation μ₂ and does not restrict the base to a field in this passage; the interpretation would need verification against the preceding definitions (Grothendieck, 1981, scan 322, first and last paragraphs).

4. **Scan 323, (1)–(5) — unproved claim.** The claim “il existe un épinglage unique” identifies a normal form from two regular unipotent sections whose associated projective points are fibrewise distinct. A proof should establish the actual descent of that normal form and determine the centralizer of the marked data, while distinguishing that claim from the marginal qualification of uniqueness of the coefficients v,w (Grothendieck, 1981, scan 323, (1)–(5)).

5. **Scan 323, first marginal NB — unproved claim.** The marginal note asserts the existence of lifts satisfying `−σ⁻¹ρ = ε₀` and `(ρ+σ)² = ρ+σ`. To check this separately from the displayed normal form, one would need to analyze the scalar ambiguity in the lifts and show that the two normalization requirements can be imposed simultaneously over the stated base (Grothendieck, 1981, scan 323, first marginal NB; reading of the overlapping interline remains uncertain).

6. **Scan 323, second marginal NB — unproved claim.** The note qualifies uniqueness of the coefficients v,w (and thus of the displayed matrices rho0,sigma0), with “demande quelques restrictions sur S” and a condition provisionally read as the absence of nonzero sections τ satisfying `2τ = 0` and `τ² = 0`. The first task is a better reading of that margin; after that, a proof would have to identify the possible infinitesimal ambiguities in those coefficients and show why precisely those equations exclude them (Grothendieck, 1981, scan 323, second marginal NB; low confidence in parts of the literal reading).

7. **Scan 323, second marginal NB — own idea.** Test the uniqueness of the scalar coefficients over a characteristic-2 dual-number ring by determining which normalized pairs of lifted matrices can have the same projective images. This should distinguish coefficient ambiguity from uniqueness of an épinglage. **Confidence: medium**, because the uncertain marginal condition explicitly appears to involve both 2-torsion and square-zero sections; an actual counterexample or proof is not supplied here and should not be presumed.

8. **Scan 324, (9)–(10) — unpursued implication.** The equations `σ+ρ = N = diag(0,1)` and `Tr(ζN) = D` single out a rank-one projector and one matrix coefficient. It would be useful to formulate the coefficient-recovery argument intrinsically in the associated rank-four Azumaya algebra and determine exactly which parts of the chosen splitting are encoded by the two projective sections (Grothendieck, 1981, scan 324, (9)–(10)).

9. **Scan 325, (13)–(16) — unproved claim.** The morphism `N′σ → μ₂` is said to be an “épimorphisme,” giving the displayed exact sequence. A verification must distinguish surjectivity as a morphism of sheaves from surjectivity on global points and determine what happens when 2 is not invertible; the text here states the equivalence but does not display that proof (Grothendieck, 1981, scan 325, (13)–(16)).

10. **Scan 325, (17)–(18) — unproved claim.** The passage beginning “Si 2 est section régulière de O_S” compares the projective stabilizer `N′σ` with the normalizer `Nσ`. The proof should keep separate the regular-element hypothesis and the stronger invertibility condition invoked before (18), particularly over bases with 2-torsion; the connective wording between these conditions is itself uncertain in the scan (Grothendieck, 1981, scan 325, (17)–(18)).

11. **Scan 326, prose before 3° — conjecture / stated expectation.** “On va … [se tourner vers] des conditions qui vont servir à fixer v” announces the next stage after fixing w. This is a stated programme rather than an independent conjecture; the following subsections should be checked for the exact hypotheses that eliminate the remaining scalar parameter (Grothendieck, 1981, scan 326, paragraph before 3°).

12. **Scan 326, (20) — unproved claim.** The determinant and ε₀ conditions are said to “résulte[r] aussitôt de (6) et (11).” The suggested verification is a direct matrix calculation using those formulas over the base ring, preserving the invertibility hypothesis on v and without treating fibrewise identities as sufficient on their own (Grothendieck, 1981, scan 326, (20)).

### 5.2. Scans 327–332

- **Scan 327, proof and lower paragraph — Unpursued implication.** The proof uses the phrase “ne peut être un scalaire” to compare the diagonal entries of a matrix cube. A useful further check is which of the equivalences remain valid over arbitrary, possibly nonreduced base rings, where coefficient comparison can require more than fibrewise non-scalarity; this is a question for verification, not a change to the manuscript text.
- **Scan 327, left margin — Unproved claim / deferred argument.** The marginal instruction “cf lemme ci-dessous” explicitly defers an alternative demonstration of the equivalence involving the projective order conditions. The lemma on the following pages should be checked against every condition referenced here, especially the distinction between a scalar cube and the specific value `-1`.
- **Scan 328, after (27) and final paragraph — Conjecture / exploratory proof attempt.** The initial claim that each displayed formula implies the preceding conditions is qualified by the insertion “sauf la dernière (27).” The later insertion “Essayons de prouver” marks a fresh attempt at the converse for (27), so the unqualified earlier sentence should not be treated as the author's final position.
- **Scan 328, final matrix — Own idea (confidence: medium).** An independent symbolic calculation over a universal commutative ring could isolate the exact locus on which (27) holds and compare it with the loci from (24)–(26). The reason for proposing this check is the visible sequence of corrections and the author's separation of (27) from the other formulas; it is a verification task, not a claim of a new result.
- **Scan 329, (27bis), (28), and lemma (30)–(32) — Unpursued implication.** The passage distinguishes the projective condition that the cube be scalar from the lifted condition “`rho^3=-1`,” and records a remaining parameter in `mu_3`. It would be useful to track this parameter as a group-scheme condition over the base, rather than treating it merely as three distinct complex numbers; the manuscript does not develop that distinction on this page.
- **Scan 329, lower lemma — Own idea (confidence: medium).** One can compare the parameter locus `v=-w^2`, with `w` invertible, against the normalized locus `w=1`, including in characteristic 3. The displayed `mu_3` condition motivates checking whether infinitesimal root-of-unity parameters survive before the additional determinant or trace normalization is imposed; no novelty is asserted.
- **Scan 330, cancelled lower argument, beside “faux” — Own idea (confidence: high).** The cancelled inference from fibrewise non-scalarity to “`rho+1 est inversible`” can be tested using the displayed standard matrix `rho=[[0,1],[-1,1]]` over the field with three elements. Its off-diagonal entry makes it nonscalar, whereas `det(rho+1)=3=0`, so the asserted invertibility fails there; this direct calculation explains a possible reason for the author's “faux,” without claiming to identify his own intended counterexample.
- **Scan 330, corollary (33)–(35) — Unproved claim.** The statement “deux de celles-ci … la troisième” asserts that two of the three relations imply the third and is tied to the preceding normal-form hypotheses. A proof should explicitly retain those hypotheses and derive the implication from the earlier parameter formulas; for arbitrary matrices the scalar matrix `-I` already shows why the surrounding restrictions cannot be silently dropped.
- **Scan 331, paragraph after (37) — Unproved claim.** The reverse coefficient comparison is justified by “compte tenu que” the identity and sigma are linearly independent sections. A proof over a general base can read an off-diagonal entry of the normal-form matrix, whose unit coefficient forces the coefficient of sigma to vanish, and then read a diagonal entry; this would supply the missing base-ring detail without using the rejected invertibility argument of scan 330.
- **Scan 331, (38)–(40) — Own idea (confidence: high).** The visible plus in (40) should be checked against the minus in (38) and (39) and against the standard matrix displayed earlier. For that matrix over the integers, `rho^2+rho+I=2rho`, so the plus-sign relation does not follow under the same normalization; this is an internal consistency check, not an emendation of the transcription or an assertion about revisions elsewhere in the manuscript.

- **Scan 332, (41)–(44) — Unproved claim.** The assertion “de façon canonique” claims a choice of lifts of the two projective sections satisfying the stated normalization and idempotent condition. A proof should establish both existence and uniqueness over the base and compatibility with restriction; the scratch calculation allowing a unit multiple of the sum suggests that fixing this scalar is part of the normalization.
- **Scan 332, before (45) through (47) — Unproved claim.** The text states that there is a “unique triplet” consisting of an épinglage and the two displayed normal-form sections. Verification should include the precise meaning of the isomorphism and the functorial dependence on the original regular unipotent data, as well as the asserted images of their lifts in (47).
- **Scan 332, opposite unipotent data and idempotent sum — Own idea (confidence: medium).** It may be useful to construct the claimed normal form directly from the kernels and images of the two regular nilpotent operators and the idempotent `rho+sigma`. The reason is that the fibrewise inequivalence condition and the two rank-one directions are visible ingredients in this page; checking their gluing would test the global content of the asserted canonical épinglage, without assuming that this construction is new or already proved here.

### 5.3. Scans 333–335

These observations refer only to the supplied pages (Grothendieck, 1981, scans 333–335). They are separate from the diplomatic transcription and do not assert that a question remains open elsewhere in the manuscript or in the literature.

1. **Scan 333, theorem heading and definition 1 — unpursued implication.** The expression “Théorème d'épinglage modulaire” and the definition of projective modular triples suggest studying the precise relation between this rigidifying datum and a conventional pinning of a reductive group. A comparison would need to identify the extra information contained in the two regular unipotents and to verify compatibility with base change; the pages here do not provide that comparison.

2. **Scan 333, conditions (49)–(51) — own idea.** One could investigate whether the sheaf of triples satisfying the displayed projective relations represents the sheaf of trivializations of the associated rank-four Azumaya algebra. **Confidence: medium.** The bijection stated in scan 335 points toward this interpretation, but a scheme-theoretic or sheaf-theoretic assertion, rather than a pointwise classification, would require separate verification.

3. **Scan 334, condition (56) — unproved claim.** The manuscript says “quatre conditions équivalentes” without repeating a proof on this page. Establishing the statement requires the preceding normalization hypotheses and a careful check of Cayley–Hamilton over an arbitrary base; the ambiguous polynomial sign must first be resolved from the manuscript rather than corrected by that argument.

4. **Scan 334, standard triple (57) — unproved claim.** The assertion that the displayed triple “est bel et bien un triplet modulaire” is not proved here. Direct matrix multiplication checks the explicit relations, while the regularity and fibrewise inequivalence conditions must also be checked, including fibres of small characteristic.

5. **Scan 335, theorem immediately after (58) — unproved claim.** “Toutes les flèches de (58) sont bijections” packages existence, uniqueness, and compatibility between linear and projective triples. The following paragraph refers back to the results of §VI rather than giving a new proof; an independent proof would have to reconstruct the isomorphism from the triple and establish that the reconstruction descends over the base.

6. **Scan 335, explanation of injectivity and (59) — unpursued implication.** The equality “\(T_\rho\cap T_\sigma=G_m\)” identifies the residual simultaneous centralizer with scalar automorphisms. It is worth separating this group-valued statement from its corresponding infinitesimal statement, since pointwise uniqueness alone does not exclude nonreduced stabilizers over arbitrary bases.

7. **Scan 335, stronger relation (60) — unproved claim.** The text adds “la relation plus forte” followed by \(N'_\rho\cap N'_\sigma=G_m\). A proof must deal with simultaneous projective stabilizers, not merely exact centralizers, and the definition of the primed groups is continued on the following scan.

8. **Scan 335, (59)–(60) — own idea.** Test the asserted scalar intersection functorially on dual-number extensions in characteristics 2 and 3, allowing nilpotent infinitesimal coefficients. **Confidence: high as a useful verification strategy, not as a predicted counterexample.** Those characteristics are natural stress tests for the projective order-two and order-three relations, and a functorial calculation could distinguish genuine rigidity from a statement only about geometric points.

### 5.4. Scans 336–339

#### R336.1

- **Scan / location:** 336, Rmq and (62)–(63).
- **Kind:** conjecture / question.
- **Note:** “Il est plausible” introduces an expectation that the indicated group sheaf over Spec Z is generated by two finite cyclic group maps and an additive group map, subject to the displayed relation; “cela vaudrait bien la peine de tirer cette question au clair” explicitly calls for clarification. The analogous assertion for Gl(2) is also proposed, with cyclic orders four and six and the altered relation (63). A proof would have to specify and establish the claimed presentation in the category of fppf sheaves, not merely verify its displayed matrices (Grothendieck, 1981, supplied scan 336, lower folio 335).

#### R336.2

- **Scan / location:** 336, (61) and right margin.
- **Kind:** unproved claim.
- **Note:** The marginal observation asserts, with an uncertain abbreviation, that the scalar in the projective stabilizer condition necessarily satisfies “ε² = 1.” A proof should identify exactly which determinant or trace hypotheses from the preceding construction are being used and check the assertion over arbitrary base rings, including characteristic two (Grothendieck, 1981, supplied scan 336, lower folio 335).

#### R336.3

- **Scan / location:** 336, proposed generators and relation.
- **Kind:** own idea.
- **Note:** Check the proposed presentation first on field-valued points and then on rings with nilpotents; a sheaf presentation may require descent data invisible in a presentation of integral points. **Confidence: medium** as a useful test strategy, because the explicit reference to fppf sheaves makes passage between sections and sheafification a material issue; no result or novelty is asserted.

#### R337.1

- **Scan / location:** 337, opening Rmq and (64).
- **Kind:** conjecture / question.
- **Note:** “J'ai la nette impression” and “est surabondant” introduce a suspected redundancy among conditions (51)–(56). He asks whether the displayed simpler algebraic conditions entail the others, but the compressed wording before “des trois conditions” is uncertain; the transcription does not decide whether he wrote an abbreviation for the ensemble or “l'une” (Grothendieck, 1981, supplied scan 337, upper folio 469 / lower folio 336).

#### R337.2

- **Scan / location:** 337, (65)–(68) and final paragraphs.
- **Kind:** unpursued implication.
- **Note:** The page begins a reduction using the idempotent N = ρ + σ and proves by contradiction the condition “N non nul en tte fibre”; it also begins the analogous exclusion of N = 1, continued on scan 338. A systematic treatment should distinguish these fibrewise assertions from global splitting and from the separate trace condition in (68) (Grothendieck, 1981, supplied scans 337–338).

#### R337.3

- **Scan / location:** 337, oblique NB margin and (64).
- **Kind:** own idea.
- **Note:** Test any proposed redundancy statement on scalar matrices as well as non-scalar matrices before removing the regularity hypotheses. **Confidence: high** that this is a necessary diagnostic, because polynomial equations alone may admit scalar solutions while regularity explicitly excludes a different geometric behaviour; the exact marginal wording is too uncertain to attribute a full formulation to Grothendieck.

#### R338.1

- **Scan / location:** 338, rank-one paragraph.
- **Kind:** unproved claim / expressed doubt.
- **Note:** After excluding the two scalar idempotents, Grothendieck writes “(sauf erreur)” while passing to a rank-one description, local decomposability, and Tr N = 1, det N = 0. The precise reworked transition is partly illegible; a proof should use the image/kernel decomposition of an idempotent and explain why it yields the asserted local tensor description over the base scheme (Grothendieck, 1981, supplied scan 338, lower folio 337).

#### R338.2

- **Scan / location:** 338, (69) and subsequent question.
- **Kind:** conjecture / question.
- **Note:** “il faudrait voir si oui ou non elle résulte des autres relations” identifies the trace equation as the remaining issue in the attempted reduction. The following choice of explicit conjugate matrices (70) starts that verification, which continues through the final supplied scan (Grothendieck, 1981, supplied scans 338–339).

#### R338.3

- **Scan / location:** 338, reduction preceding (69).
- **Kind:** own idea.
- **Note:** A basis-free reformulation of the last trace calculation may clarify the exact hypotheses and avoid a conjugacy assumption that is only locally available. **Confidence: medium**, because the page passes from an Azumaya-algebra setting to a chosen matrix model; the proposed reformulation is a research direction, not an established reading or claimed new theorem.

#### R339.1

- **Scan / location:** 339, (70bis)–(74).
- **Kind:** unpursued implication.
- **Note:** The explicit calculation reaches “Tr ρσ … = 2” in (74) and therefore addresses the remaining trace question formulated on scan 338 within the chosen matrix parametrization. These pages do not separately spell out all descent or regularity hypotheses required to turn that computation into a global equivalence for forms associated to an Azumaya algebra (Grothendieck, 1981, supplied scan 339, upper folio 470 / lower folio 338).

#### R339.2

- **Scan / location:** 339, (71)–(74).
- **Kind:** own idea.
- **Note:** Seek a direct derivation of the final trace identity from the quadratic identities and idempotency using the degree-two characteristic identity, with the exact non-scalar hypotheses made explicit. **Confidence: medium**, because the matrix expansion suggests an invariant identity, but its extension over arbitrary rings and its dependence on the marginal regularity qualification require proof; no novelty or completed proof is claimed.

## 6. Primary source

Grothendieck, A. (1981). *La Longue Marche à travers la théorie de Galois* [Unpublished handwritten manuscript, cote 140-3, archive file “pages 293–650”; supplied scan images 321–339]. Université de Montpellier. [Archive address printed on the scans](https://grothendieck.umontpellier.fr).

The title, date, archive designation, and scan identifiers follow the supplied task prompt and image captions. This is the sole source used for the diplomatic reading. The research notes are a manuscript-based working inventory, not an external literature review.

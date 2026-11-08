# LM_P041 — Transcription notes and research notes

## Scope, source, and locators

This accompanies `LM_P041_transcription.tex`, a diplomatic LaTeX fragment of the ten supplied manuscript images. The fragment contains no preamble or macro definitions. It uses the requested editorial macros, standard LaTeX/AMS mathematical notation, and `tikz-cd` for the final clearly directed two-object diagram; the less secure diagram is described explicitly. Its syntax was checked in a temporary LaTeX wrapper providing definitions for the editorial macros; that wrapper is not part of the deliverable.

Readings were made from the supplied images, page by page, with enlarged crops and a rereading of each page. Particularly uncertain passages received an independent second reading. No published transcription, external mathematical exposition, or later part of the manuscript was used to supply text. The attribution, title, date, and archival designation follow the attached task prompt.

The filename identifiers determine `\scanpage`. They are one higher than the printed archive footer labels. The separate upper manuscript numbers are recorded with `\mspage`; the small handwritten numerals at the foot of each sheet are preserved with `\margin`, without asserting that they are in the same hand as the upper pagination. The printed institutional footer, URL, and duplicated printed page number are archive paratext and are not transcribed as manuscript text.

| Scan / filename identifier | Printed archive label and lower handwritten numeral | Visible upper manuscript number |
|---|---:|---:|
| 401 | 400 | 203 |
| 402 | 401 | — |
| 403 | 402 | 204 |
| 404 | 403 | — |
| 405 | 404 | 205 |
| 406 | 405 | — |
| 407 | 406 | 206 |
| 408 | 407 | — |
| 409 | 408 | 207 |
| 410 | 409 | — |

Approximate line numbers below count handwritten main-body baselines, including displayed mathematical rows but excluding pagination. A note identifies its host line when it concerns an insertion. Physical line breaks were usually retained for convenience, but they are not a formal line-by-line facsimile; the source's paragraph divisions and reading order take precedence.

`\unsure{reading|alternative}` preserves alternatives in the transcription. A single candidate inside `\unsure` is still doubtful. `\illegible{n}` estimates the number of unrecovered words; an isolated overwritten mathematical glyph or short mark is counted as one unit. Nested `\inserted{\deleted{…}}` records an addition that was itself subsequently cancelled, without claiming an exact chronology beyond the visible layers. French bracketed descriptions inside `\diagram` and `\figure` are editorial descriptions of visible graphics, not words attributed to the author.

The looped script letter is provisionally encoded as `\mathcal T`; single and double hats are distinguished locally. Cursive N and M forms are represented with the indicated ordinary or calligraphic alphabets, with local doubts where the distinction is insecure. Repeated double-stem Greek capitals, tiny a/dot subscripts, and angular superscripts remain a material limitation; neither the conventional name of a group nor the mathematics it is expected to satisfy was used to settle them. Repeated equation labels, absent plus signs, incomplete punctuation, and apparent grammatical irregularities have not been repaired.

## 1. Table of doubts

Confidence concerns the proposed **reading**, not the truth of the mathematical assertion. “High” entries usually document a visible feature that is easy to omit, rather than a disputed word. Closely related occurrences of the same uncertain glyph may share a row.


### Scans 401–403


| Scan | Approx. line | Reading in transcription | Alternatives / difficulty | Confidence |
|---|---:|---|---|---|
| 401 | 1–5 | `\widehat{\widehat{\mathcal T}}`, `\mathcal N` | Looped handwritten mathematical letters are encoded as script T and N; the first numerator after the arrow is overwritten. A modern naming convention has not been used to resolve the alphabet. | medium |
| 401 | 3 | `M_{a'}^{\sharp}` / `M_{a'}^{\natural}` | Small superscript is particularly difficult; enlargement shows more strokes than a simple hat. The main letter looks like M, but an overwritten N cannot be excluded; the double-hatted numerator is also retraced. | low |
| 401 | 4 | inserted `n'aurait` | Word rises above the baseline; the scope of the addition includes at least the upper portion of the word. | medium |
| 401 | 5 | `\widehat{\widehat{\mathcal T}}(\pi'_i)` | The target script letter is heavily retraced; retain the local doubt mark. | medium |
| 401 | 9 | deleted `courbes alg.` | The crossing passes through most of the letters; final abbreviation is doubtful. | low |
| 401 | 10–11 | inserted `de type (g,\nu),` | Insertion connector appears to lead after the first `arithmétisés,`; the connector is faint. | medium |
| 401 | 15 | deleted `par` | A short crossed word beginning with a descending stroke; possibly a false start rather than a complete word. | low |
| 401 | 17 | deleted `Je pense qu'il` | Several strokes merge with the cancellation, particularly `pense`. | low |
| 401 | 17 | inserted and deleted `On aura`; surviving insertion `ou encore` | Independent rereading distinguishes two interlinear layers above the cancelled main line. The two phrases remain doubtful, but they are not treated as alternative readings of the same layer. | low |
| 401 | 17 | `\Gamma_{g,\nu}` / `\Pi_{g,\nu}` | Double-stroked upright is visible; no clear separate far-right upright. Gamma is the preferred reading. | medium |
| 401 | 18 | deleted `pour`, one illegible word, `\Gamma'` | Crossed mathematical letter/word between `pour` and the final gamma cannot be reliably recovered. | low |
| 401 | 18 | `dans` | A short intact word with detached final s after the cancellations; retained with doubt. | medium |
| 402 | 1–2 | (15), two maps from `\Gamma'_{g,\nu}` | Source upright is retraced. One hat is read on each target T; the second target has `+!`, the first only `+`. A long grouping stroke is represented by a left vertical delimiter. | medium |
| 402 | 3 | `que` / `qu'`, followed by deleted `il s'agit` | The cancellation leaves the exact vowel/elision of the connective uncertain. | low |
| 402 | 4 | `l'image inverse` | Highly compressed word `image`; the phrase is a tentative visual reading, not supplied from the proposed construction. | medium |
| 402 | 6 | `deux` | The central letters are flattened; `seuls` was considered but does not fit the visible ending as well. | low |
| 402 | 6 | `mbs` | Short form after `deux`, perhaps for membres; do not expand in the transcription. | low |
| 402 | 11 | `ss-groupes` | Two small initial strokes are overwritten. | medium |
| 402 | 11 | `inscrits` / `associés` | Neither reading accounts securely for every stroke; the former better fits the beginning and final tall stroke. | low |
| 402 | 12 | deleted `\mathcal T'_i` | Script symbol and lower index are crossed. | low |
| 402 | 12 | `\mathcal T_{g,\nu}^{+!}` | No separate hat is clearly visible at this occurrence; none has been supplied. | medium |
| 402 | 15 | `passages` / `passage` | Final s is not securely distinguishable. | low |
| 402 | 15 | inserted `successifs.` | Final letters and apparent terminal dot are uncertain; the insertion is placed with `passages`. | medium |
| 402 | 16 | second lower index `\nu-2` | Final digit is dark and retraced; 2 is preferred but 1 cannot be completely excluded. | medium |
| 402 | 16–17 | deleted `pour lesquelles`, inserted `qui soient` | Replacement is above the cancellation. | high |
| 403 | 1 | `suffise` | Final consonant stroke could instead support `suffire`; continuation from the preceding page does not settle the ink. | medium |
| 403 | 1 | deleted `\mathcal N_{g,\nu}` | Most of the mathematical symbol is overwritten. | low |
| 403 | 3 | deleted `\nu=0` | The final part of the expression is obscured; the uncancelled condition later on the line is clear. | low |
| 403 | 7 | `M_{g,\nu\,\overline{\mathbb Q}_a}` | Subscripted barred Q and a are visible; spacing/attachment and the precise alphabet of M/Q remain uncertain. | medium |
| 403 | 9–10 | `s'attendre`; `des tas !` / `du tout !` | This is one of the least secure phrases. Its grammar has not been repaired or an à supplied; rereadings favor `des tas !`, but the terminal stroke remains ambiguous. | low |
| 403 | 11 | `courbe algébrique potentielle` / plural alternative | Noun/adjective endings are not secure; the transcription preserves the singular/plural uncertainty. | low |
| 403 | 12 | `sous-entendu` | Compressed opening of the parenthesis. | medium |
| 403 | 12 | `pas` / `non` | Tiny word before `précisée`; rereading favors `pas`, without supplying an unobserved field hypothesis. | low |
| 403 | 13 | `d'une` / `d'un` | Final small mark is ambiguous; the addition has not been used to regularize agreement. | low |
| 403 | 13 | inserted `groupe extprofini` / `groupe catprofini` | Small insertion above π; first letters of the underlined second word are insecure. | low |
| 403 | 13 | `lacets` / `lacet` | Terminal s not clearly distinguishable. | low |
| 403 | 13 | deleted `profini`, inserted and deleted `ext` | Two successive revisions are preserved separately; precise lettering of the lower cancelled word is weak. | low |
| 403 | 16–17 | deleted marginal mark near (16) | An overwritten letter/false start; one illegible unit is recorded. | low |
| 403 | 17 | subscript `a` / `\bullet`; superscript `\natural` | Both small signs are uncertain. The upper sign is angular and zigzag-like; natural is an encoding of a candidate reading, not an established notational identification. | low |
| 403 | 21 | inserted `trivialmt` / `trivialemt` | Tiny abbreviated interlinear word; it has not been expanded to trivialement. The connecting curve starts just before `revient`, where the insertion is placed, but the attachment is insecure. | low |


### Scans 404–406


| Scan | Approximate line/location | Reading in transcription | Alternatives / precise issue | Confidence |
|---|---|---|---|---|
| 404 | 3 | `constant` | Parenthetic word beginning `cons…`, ending in a tall `t`; not read letter by letter. | low |
| 404 | 3 | `correspondant` | `correspondent`; unstressed vowels and ending are compressed. | medium |
| 404 | 4 | `munies` | Final letters very weak; the inserted `alors` is clearer. | medium |
| 404 | 5 | `isom.` | May be a shorter abbreviation, `iso`; the final minim is uncertain. | medium |
| 404 | (17) | `P_a` / `\mathbb P_a` | Doubled left stroke could signify a different alphabet; subscript resembles `a`. | medium |
| 404 | (18) | `Γ_a` | The subscript is a compressed stroke; compare `Γ_•` later on this page. | medium |
| 404 | (18), Aut subscript | `Γ_{g,ν}` / `Π_{g,ν}` | Both uprights cluster at the left, favoring Γ with a doubled stem; the alphabet remains locally marked. | medium |
| 404 | left margin, opening | `Le cas où` | Independent rereading favors this over the initial tentative reading `Ici bien sûr`; compressed opening is retained with doubt. | medium |
| 404 | left margin, 3rd line | `trivial, est celui` / `trivial, et celui` | Connecting verb/word and comma remain insecure. | low |
| 404 | left margin, 4th line | deleted word | Approx. one word under heavy horizontal cancellation, not recoverable. | low |
| 404 | left margin, after `ext` | one illegible unit | A compact parenthesis-like suffix or symbol follows `ext`; it is not silently reduced to a full stop. | low |
| 404 | left margin, 5th line | `munis` | Ending and first strokes compressed. | low |
| 404 | left margin, underlined phrase | `prédiscrétification` | Highly tentative full reading: `pré` and a possible `…ification` ending are more secure than the intervening letters. Earlier `pré-descript.` reading was not retained; this is not a settled technical term. | low |
| 404 | left margin, following line | `arbitraire` | Independent rereadings favor the full word over the earlier, rejected abbreviation reading `arith. a`; it remains marked. | medium |
| 404 | left margin, parenthesis | `d'où`, `exacte` / `ayant` | Several cancellations obscure the words; `exacte` is now preferred, but not supplied as an unmarked consequence of the sequence. | low |
| 404 | left margin, sequence | `1 → T̂_a → N_a → Γ_a → 1` | Single hat is visible; Γ/Π at the end and the other alphabets and tiny subscripts remain insecure. | medium |
| 404 | 9 | `fois-ci` | Hyphen and final letters weak. | medium |
| 404 | 10 | `ens` | Probably abbreviation for ensembles; no certain final stop visible. | medium |
| 404 | 13 | one illegible verb before `les Points` | `définira`, `considère/considérera`, and an opening `dénom…` were considered, but none survives letter-by-letter verification. No full-word candidate is imposed in the transcription. | low |
| 404 | 13 | cancelled mark before `Points` | A heavily overwritten attempted initial or word; counted as one illegible word. | low |
| 404 | 15 | `relèvts` | Abbreviation versus longer compressed spelling cannot be distinguished. | low |
| 404 | 16 | `ou` | Could be `en`; very short isolated stroke preceding (19). | low |
| 404 | (19) and (20) | `Γ_•^♮` | Superscript is a zigzag; natural-sign encoding provisional. | low |
| 404 | (19) | `M_a` in calligraphic alphabet | Letter is visually M-like; calligraphic versus ordinary mathematical alphabet unresolved. | medium |
| 404 | foot of body | deleted word after `(ceci pour` | Aborted word near bottom border is crossed out and incomplete. | low |


| Scan | Approximate line/location | Reading in transcription | Alternatives / precise issue | Confidence |
|---|---|---|---|---|
| 405 | 3 | `d'un` | The short word is overwritten; not all strokes distinct. | medium |
| 405 | insertion over line 4 | `tel que` | First short word could be abbreviated; no expansion imposed. | medium |
| 405 | insertion over line 4 | `Γ′ ∩ Σ_a = (1)` | The subscript of Σ resembles a dot; `Σ_•` is possible. The parentheses around 1 are present. | medium |
| 405 | 4 | `permettrait-il` | Final `-il` seems visible even though the preceding subject is feminine; not corrected to `-elle`. | medium |
| 405 | 5, 13 | `arithmatisation(s)` / `arithmétisation(s)` | The vowel and accent before t are not secure; no spelling has been normalized silently. | low |
| 405 | 7 | `N_a` | Calligraphic N is heavy and retraced; rendered with `\mathcal`. | medium |
| 405 | 8 | `suffirait` | `suffira`; ending before comma compressed. | medium |
| 405 | 10 | `isom.` | Middle/final letter compressed; may be the shorter `iso.`. | medium |
| 405 | 11, after insertion | `le` | Word retraced heavily, can look like a letter-symbol. | medium |
| 405 | 14 | one illegible word after `Or ceci revient` | Possibly `exactement` or an abbreviation of it; exact written form not secure. | low |
| 405 | beside circled g | `quand même` | Independent rereading favors this two-word reading; the initial q-like descender and final tall stroke are clearer than the middle letters. `probablement` was considered and rejected as unsupported. | low |
| 405 | beside circled g | deleted `tout` | Capitalization and full reading under cancellation uncertain. | low |
| 405 | 16, 18 | `N′` | The alphabet may be calligraphic, `\mathcal N′`; not silently harmonized with other N-symbols. | medium |
| 405 | 18 | `sont` | Heavily retraced; it may conceal a correction, but a distinct cancellation of the full word is not certain. | medium |
| 405 | 18 | `a fortiori` | Initial a is very compressed. | medium |
| 405 | opening and final paragraphs | Σ without subscript; single-hatted T in the insertion and final normalizer | These forms are retained despite possible expectations of a subscript or plus sign; none is securely visible at those occurrences. | high |
| 405 | closing parenthesis | no closing textual parenthesis added | The final `)` belongs to the normalizer's mathematical argument; an additional textual close is not visible. | medium |


| Scan | Approximate line/location | Reading in transcription | Alternatives / precise issue | Confidence |
|---|---|---|---|---|
| 406 | 1 | `classes` | Final word on line, strongly compressed. | medium |
| 406 | 2 | `relèvts` | Could be a longer compressed spelling or abbreviation; retained as uncertain. | low |
| 406 | 4 | `groupoïde` | Internal vowels and final letter run together; singular inferred only tentatively from the ink. | medium |
| 406 | 6 | `Γ^♮` | Superscript may instead be a sharp sign, or a retraced correction; no unmarked identification. | low |
| 406 | 7 | `reposer` | `repérer`; accent not securely visible and middle letters compressed. | medium |
| 406 | 8 | `Γ^♮` | A faint tick at upper right might be part of the retraced Γ; plain Γ remains possible. | low |
| 406 | 8 | `seulement` | Initial part darkened/overwritten; not enough evidence to mark a separate deleted word. | medium |
| 406 | 9 | `moralmt` / `moralement` | Middle letters look like `moral…`; an abbreviated ending is possible and is not expanded silently. | low |
| 406 | 11 | closing delimiter after the ellipsis | Resembles a curly `}` rather than a `)`, despite the earlier opening parenthesis. | low |
| 406 | 16 | `Γ′` | Two small dots below/near the letter could indicate a bullet subscript, `Γ′_•`, rather than stray ink. | low |


### Scans 407–408


| Scan | Approx. line / location | Reading retained | Alternatives / unresolved detail | Confidence |
|---|---|---|---|---|
| 407 | 1, enclosure | `I' ⊂ I = I(π)` | The enclosure is open along most of its lower edge; its three-sided shape is recorded in a `\figure` description, without closing it typographically. | high |
| 407 | 2 | `trouve` | The compressed ending is a short stroke; `trouver` cannot be excluded from the letter forms alone. | medium |
| 407 | 3 | `bouchage` | The middle letters are very cursive; this reading is marked rather than supplied from the geometry. | medium |
| 407 | 4, deletion | `qui` | The word is crossed horizontally. Its descending initial is clear, but the ending is partly hidden. | medium |
| 407 | 6, (20) | superscript `\natural` on `π` | `\sharp`; the tiny angular sign is not confidently identifiable. | low |
| 407 | 7, right end | inserted `a'` | The small raised label is linked to the end of `arithmétisation`; placement as an insertion is more secure than its exact letter. | medium |
| 407 | 8 | `on a` | Very compressed connective after `et`; the reading is marked. | medium |
| 407 | 9–12, (21) and following sentence | `Γ_a`, `Γ_{a'}` | The left upright of Γ is doubled/retraced. The very small subscript `a` resembles a dot in some occurrences. | medium |
| 407 | 10–12 | `P`, including `P_a`, `P_{a'}` | `\mathbb P`: the upright is explicitly doubled in (21), while the later standalone P is less strongly retraced. No semantic normalization of this alphabet is intended. | low |
| 407 | 9–10, (21) | first row rightward isomorphism arrow; second row `\simeq` | The first horizontal stroke ends in a dark point; whether the second also has a tiny arrowhead is uncertain. | medium |
| 407 | 11, (21) | vertical `\wr`-like mark over `P` | It could be a vertical equivalence sign or an isomorphism arrow; the two visible strokes are not unambiguously directed. | low |
| 407 | right of (21) | `\leadsto` | A loose rightward squiggle, not securely identified as a formal arrow. | low |
| 407 | 12, after `que` | `Γ_a` | `π_a`; this glyph is not silently changed to the mathematically more expected unindexed `π`. | low |
| 407 | 14 | `trouver` | The middle letters and the final stroke are very compressed. | medium |
| 407 | 17 and 20, script letter | doubly hatted `\mathcal T` in the homomorphism; singly hatted `\mathcal T` in (22) | The looped script letter can resemble a C; the top cross-stroke favors T. The distinction between two hats in the first display and one in (22) is clearer than the alphabet itself. | medium |
| 407 | 19–20, (22) | `\mathcal N_a`, `\mathcal N_{a'}` | Ordinary N with a flourished pen stroke is also possible; the two occurrences differ in how heavily they are retraced. | medium |
| 407 | 19–20, (22), vertical connectors | open-up cup-shaped inclusion signs | Very short downward arrows are a possible reading. The transcription describes the visible arrangement instead of supplying full vertical arrows. | low |
| 408 | 1 | `donnant` | `déduisant`; only the first tall ascender is clear, so the shorter reading is provisionally preferred. | low |
| 408 | 1 | `justement` | The final strokes are retraced; the word is recognizable but its exact ending is less clear. | medium |
| 408 | 4, composition | `Γ ⊂ N_a → N_{a'}` | The first connector could be an incomplete `\hookrightarrow`. It has a C-shaped left end and a long baseline but no distinct arrowhead at the right. | low |
| 408 | 5 | `égalmt` | `également`; a compressed abbreviated ending is more consistent with the visible strokes. | low |
| 408 | 7 | `quasi-section` | `quasi section`; a separating short stroke could be either a hyphen or part of the following word. | medium |
| 408 | 8 | `Donc` | `On`; the initial rounded capital and flattened tail do not resolve the word securely. | low |
| 408 | 8 | deleted `par`, inserted `sous` | `sous` is directly above the cancelled `par`; the attachment is clear. | high |
| 408 | 9, cancelled glyph | `\deleted{\illegible{1}}` | A single overwritten/cancelled mathematical symbol, possibly U, before the surviving `π`. | low |
| 408 | 9 | `π` without a prime | Its right leg rises in a long stroke, but no detached prime is visible. It is not changed to `π'` for consistency with nearby formulas. | medium |
| 408 | 10 | `relatif` | The final f is visible; no following e is seen. The masculine form is retained despite the preceding nouns. | high |
| 408 | 11 | `P` | `\mathbb P`, as on the preceding scan. | medium |
| 408 | 12, within the cancelled block | `peut-être par` | The cancellation stroke passes through the upper portions; an unreadable two- or three-word phrase remains possible. | low |
| 408 | 15, within the cancelled block | `tte` | The glyph could be the quantifier `∀`; both are retained as alternatives. | low |
| 408 | 17, before surviving `Je` | `\deleted{\illegible{1}}` | One heavily overwritten short word or symbol, possibly a rejected beginning of the sentence. | low |


### Scans 409–410


| Scan | Approximate line / location | Reading retained | Alternative / source of doubt | Confidence |
|---|---|---|---|---|
| 409 | 3, crossed-out clause | `du fait que Γ opérait tr.` | The final abbreviation is only a tall cross-stroke and short ink trace; `opérait` is partly obscured by the deletion line. | low |
| 409 | 3, insertion | `si I′ ≠ ∅,` | The empty-set sign is drawn with a long diagonal; it is not an ordinary zero. The inequality and the prime are clear. | high |
| 409 | 5, insertion | `vrai` before `groupoïde` | The insertion is above the first portion of `groupoïde`; its curved placement stroke should not be read as part of the word. | high |
| 409 | 7 | `pure` | Final ending compressed; `pur` cannot be excluded from the visible trace alone. | medium |
| 409 | 9 | `trivialt` | Possible abbreviation for *trivialement*; the ending is a short raised-looking stroke, not a clearly written full `-ement`. No expansion has been made in the transcription. | medium |
| 409 | 10 | `tt` | Could be a compact universal-quantifier sign rather than two letters. | low |
| 409 | 11 | `i′ ∈ I′,` | Initial `i′` and following comma are compact and can resemble parentheses at whole-page scale; no extra parentheses have been supplied. | medium |
| 409 | 11, deletion | `relèvement de` | The long horizontal deletion obscures several middle letters. | low |
| 409 | 12 | `hom.` | `hom` is probable; the abbreviation point is not secure. | medium |
| 409 | 15, before `classe` | `uq` | A compact u/q-like form; possibly shorthand for *unique*, or a very compressed writing of that word. The glyph has not been silently expanded. | low |
| 409 | 15, insertion | `π′-` before `conj.` | Written above the line, with a placement stroke to the start of `conj.`. | high |
| 409 | 18 | `qu'elle satisfait` | `qu'elles satisfont` is also possible at normal scale; singular readings fit the visible final strokes slightly better, but both words remain marked. | medium |
| 409 | (25), middle argument | `α′` / `a′` | The cursive letter could be Greek alpha or Latin a; both alphabets are made explicit rather than inferred from the arithmetization terminology. | low |
| 410 | 1 | Underline from `dis` to `injective` | The line begins after the large initial `Je`; a terminal dark point may be the end of the underline rather than punctuation. No terminal full stop has been supplied. | medium |
| 410 | 3 | `réalisable` | The final stroke is compressed; singular versus plural ending is not entirely secure. | medium |
| 410 | 5 | `admissibles`, `réalisables` | Plural endings are partly reduced to short terminal strokes. | medium |
| 410 | 6 | `K⁺` | Alternative `K`: the upper-right arm ends in a distinct plus-shaped thickening, which could be a superscript or a pen correction. No prime is clearly isolated. | low |
| 410 | 7 | `fixes` | The word is heavily contracted into an initial descending stroke and a horizontal continuation. | medium |
| 410 | 9, right margin of main line | `)` | A small isolated curved mark follows `et des`; it might be punctuation or a stray correction mark. It is retained with doubt. | low |
| 410 | 9 | `N_{g,ν}` | The capital is cursive; comparison with the rest of the bundle is needed to settle ordinary versus calligraphic `N`. | medium |
| 410 | 10, deletion | `Et` | Several overdrawn strokes obscure the short abandoned word. | low |
| 410 | Left marginal note opposite lines 5–8 | `On va revenir au cas card I′ = 2 …` | The initial letter of `card` could be a capital `C`; the number 2 is clear. | medium |
| 410 | 13 | `éventuelles` | Initial accent and the compressed opening syllables are faint. | medium |
| 410 | Bottom functor, source second line | `relatives`, probably struck through | The heavy line may instead be overwriting/underlining. Both states are explicitly offered in the transcription rather than silently deciding. | low |
| 410 | Bottom functor, source crossed phrase | `d'un ens` | The deletion line passes through almost all the phrase. | low |
| 410 | Bottom functor, source group with subscript P | `Γ_P` / `Π_P` | Uprights cluster at the left while the top bar extends rightward; Γ is visually preferred, but the alphabet remains marked. | medium |
| 410 | Bottom functor, source final line | `ens I′ de pts à l’∞` | The `à l’∞` ending is compact but the infinity sign is visible; it should not be normalized into `i′ …`. | medium |
| 410 | Bottom functor, target final line | `pts ratls / Γ` | Alternative `pts réels / Γ`; the middle letters and any superscript arrangement are not secure. The spelling has not been expanded to *rationnels*. | low |
| 410 | Bottom-left marginal note | `fonctorialités` | Alternative `constructions`; the long word is compressed and partly against the edge. | low |
| 410 | Bottom-left marginal note | `anabéliennes habituelles` | Both words are plausible readings of the slanted ink, but several letters and endings are indistinct. | low |


## 2. Abbreviations met

Expansions belong to this list only. They are interpretations, not text inserted into the transcription. Doubtful abbreviation readings are identified explicitly; a compressed word is not treated as an established abbreviation merely because an expansion is plausible.

| As written or tentatively read | Tentative expansion / role | Scans |
|---|---|---|
| `alg.` | algébrique(s) | 401, 403–404, 407, 410 |
| `Autext`; `Aut ext` | automorphismes extérieurs; operator spacing retained locally | 402 |
| `Aut` | automorphismes, in a mathematical operator | 404 |
| `Norm` | normalisateur, in a mathematical operator | 401, 405 |
| `hom.`; `hom` | homomorphisme(s); the point is uncertain in some occurrences | 401, 407–409 |
| `i.e.` | id est | 402, 404, 406–407 |
| `mbs` (doubtful) | possibly membres | 402 |
| `ss-groupes` (initial strokes doubtful) | sous-groupes | 402 |
| `ss-groupe` | sous-groupe | 405–406, 410 |
| `etc` | et cetera | 402 |
| `iso`; `iso.` | isomorphisme(s) | 403–404 |
| `isom.` (doubtful; possibly `iso`) | isomorphisme | 404–405 |
| `ext`; `ext.` | extérieur(s) / extérieure(s), according to occurrence; the suffix in the diagonal note on 404 is not recovered | 403–404, 407, 409 |
| `relèvts` (doubtful) | relèvements | 404, 406 |
| `ens`; `ens.` | ensemble(s) | 404, 409–410 |
| `tt` (sometimes doubtful) | tout; a compact universal-quantifier sign is an alternative at one occurrence | 405, 409 |
| `tte` (doubtful) | toute; alternatively a universal-quantifier sign | 408 |
| `NB` | nota bene | 406 |
| `\overline{\mathrm m}` | même | 406–408 |
| `lui-` followed by `\overline{\mathrm m}` | lui-même; the sign is retained literally | 406 |
| `sous-ext.` | sous-extension | 406 |
| `pts`; `pt` | points; point | 406, 410 |
| `rat` | rationnels | 406, 410 |
| `ratls` (doubtful; alternative `réels`) | possibly rationnels | 410 |
| `égalmt` (doubtful) | également | 408 |
| `tr.` (cancelled, doubtful) | possibly trivialement | 409 |
| `trivialt` (doubtful) | trivialement | 409 |
| `trivialmt` / `trivialemt` (doubtful) | trivialement | 403 |
| `moralmt` (doubtful; alternative full word) | moralement | 406 |
| `uq` (doubtful) | possibly unique; the compact glyph is not expanded | 409 |
| `conj.` | conjugaison | 409 |
| `can.` | canonique | 409 |
| `Pts` | points, as part of the mathematical notation in (25) | 409 |
| `card` (capitalization doubtful) | cardinal | 410 |
| `pot.` | potentielles | 410 |

## 3. Legibility and limits

These pages are unevenly legible. Much of the uncancelled prose and the larger displays can be read after enlargement, but compressed endings, small abbreviations, retraced capitals, and the distinction between single and double hats require caution. The text is a checked provisional transcription, not a claim that all remaining doubtful passages have been deciphered.

The least trustworthy areas are the middle denominator in the first quotient and the layered revisions at the foot of scan 401; the subgroup adjective on scan 402; the short “s'attendre …” phrase and definition insertions on scan 403; the entire diagonal marginal note on scan 404; and the revised source inscription and marginalia of the final functor on scan 410. The qualifier beside (g), the angular superscripts, and the compact `uq`-like glyph also remain insecure. The underlined technical expression tentatively read as `prédiscrétification` is particularly weak and must not be used as a securely attested term.

The diagram on scan 407 is described rather than completed with conjectured vertical arrows. The three-sided frames on scans 404 and 407 are described as open at the bottom. The cancelled admissibility block on scan 408, including its equation (24), remains cancelled in the transcription; the later uncancelled equation carrying the same number is preserved as a separate occurrence. Original spelling and agreement have not been regularized where the image suggests an irregularity; doubtful readings stay marked even when one alternative would make smoother French or more familiar mathematics.

## 4. Research notes — English, separate from the transcription

These are observations and proposed proof obligations arising from the supplied primary source (Grothendieck, 1981). Each entry gives its scan and, where practicable, an approximate line or equation locator. An author's question, expectation, or cancelled proposal is not promoted to a theorem. An “unproved claim” means that its proof is not supplied at the cited location in these ten scans; it does not mean that the claim is false or that a proof is absent elsewhere. Own ideas include a confidence level and reason and make no claim of novelty. No literature-status or later-manuscript check has been performed, and none of these notes changes a transcription reading.


### R401.1 — Scan 401, approximately lines 1–6 — conjecture / explicit doubt

The author links a quotient-map bijectivity to an isomorphism between the displayed decorated groups and calls the latter “bien problématique” (Grothendieck, 1981, scan 401). This is a reservation about the proposed reconstruction, not a theorem affirming the displayed isomorphism. The middle denominator is textually insecure, so a precise modern statement must wait for that reading and the preceding definitions.

### R401.2 — Scan 401, approximately lines 7–13 — unproved claim

The “bouchage des trous” functor is said to give “une équivalence” between the two categories described, with types (g, ν) and (g, ν−1) and a change from exterior to non-exterior lacets (Grothendieck, 1981, scan 401). A proof would need the exact objects and morphisms, an explicit construction of the functor, and full faithfulness and essential surjectivity compatible with the stated arithmetizations. None of those proofs is given on this page.

### R401.3 — Scan 401, approximately lines 14–18 — conjecture / programme

“On peut se proposer d'essayer” introduces the attempt to characterize the smaller N-group inside the displayed normalizer N′ (Grothendieck, 1981, scan 401). The page poses the characterization problem rather than stating sufficient intrinsic conditions. Its subsequent quotient notation is revised in the manuscript and should not be silently standardized before that problem is formulated.

### R402.1 — Scan 402, approximately lines 3–9 — conjecture

“Je présume” introduces a proposed description through one of the two outer-automorphism maps in (15), apparently by inverse image of a suitable closed subgroup (Grothendieck, 1981, scan 402). The words read as “l'image inverse” remain doubtful. If confirmed, the missing work is to specify that subgroup and prove that the resulting inverse image is exactly the intended Γ-group.

### R402.2 — Scan 402, approximately lines 9–17 — unproved claim / proposed criterion

The author says the conditions labelled (e) are “bien de ce type” and considers conditions stable under successive passages to groups with fewer punctures (Grothendieck, 1981, scan 402). The definition of (e) is outside these ten scans, and the adjective describing the relevant subgroups is insecure. Verification therefore requires the earlier definition, the exact passage maps, and a proof that each proposed normalization condition is preserved.

### R402.3 — Scans 402–403, end of 402 and opening of 403 — conjecture / explicit doubt

The warning “il n'est pas dit du tout” carries across the page break into doubt about whether these conditions suffice; the opening of 403 says the condition becomes “vide” in the stated limiting cases (Grothendieck, 1981, scans 402–403). The visible cases include ν=0 with g≥2, and the pairs (1,1) and (0,3). A sufficiency argument must address those cases explicitly instead of using the existence of a forgetful operation that has ceased to impose information.

### R403.1 — Scan 403, approximately lines 5–7 — conjecture

“Il est possible qu'il faille faire intervenir” introduces properties of the displayed moduli fundamental groups “liés à la compactification” (Grothendieck, 1981, scan 403). The page does not identify the extra properties or show they characterize the desired arithmetic subgroup. A useful next step is to make the relevant compactification data explicit before testing which parts are determined by the abstract profinite groups.

### R403.2 — Scan 403, approximately lines 11–21 — unproved claim / provisional definition

The proposed potential algebraic curves include an arithmetization and a germ of “admissible” lift, and “Elles forment une catégorie” is qualified by “pour le moment” restricting attention to isomorphisms (Grothendieck, 1981, scan 403). The excerpt subsequently gives conditions and then reopens the problem of a satisfactory definition of admissibility; this page alone does not settle it. One must specify equivalence of lift germs and the isomorphism compatibility before the categorical assertion can be checked.

### R403.3 — Scans 401–403 — own idea

Compare the proposed criteria before and after each puncture-filling map in the explicitly mentioned limiting types, recording exactly which conditions become tautological. **Confidence: medium** that this is a useful diagnostic, because the manuscript itself identifies vacuity as the obstruction; no claim is made that the test proves or disproves the intended characterization. This is a suggested programme, not an established result or a novelty claim.

### R403.4 — Scan 401, approximately lines 7–13 — own idea

Try to state the claimed equivalence as a comparison of groupoids that keeps both conjugacy classes and chosen representatives of peripheral data visible. **Confidence: medium**, because the contrast “pas extérieurs !” suggests that the distinction between outer data and chosen data is structurally relevant. This suggestion must not be used to fill the manuscript's undeciphered symbols or to assert that the equivalence has been proved.


### Scan 404

- **Scan 404, lines 9–12 — kind: conjecture / expectation.** The phrase “on s'attend à trouver” introduces an expectation of finite sets of isomorphisms after a torsor has been fixed, in contrast to the preceding profinite torsor situation. A proof would need the precise category of objects and morphisms and a justification that fixing the extra torsor data leaves only finitely many isomorphisms; the statement on this page is an expectation, not a displayed proof.
- **Scan 404, lines 13–20 — kind: unpursued implication.** The definition through “classes de … conjugaison” of “admissibles” lifts is paired with a genuine action and the displayed trivial-fixed-subgroup condition. It is worth separating whether this condition is necessary, sufficient, or only one component of admissibility: scan 406 explicitly identifies admissibility here with satisfying (20), while any later qualifications must be checked separately. The box itself is not a proof of a geometric classification.
- **Scan 404, (17)–(18) — kind: own idea.** One could test the expected finiteness first for the automorphism group of a single potential curve equipped with the displayed torsor identification, before addressing all isomorphism sets. **Confidence: medium** as a research strategy, because automorphisms are the self-isomorphism special case; no finiteness conclusion or novelty is asserted.


### Scan 405

- **Scan 405, lines 2–8 — kind: conjecture / question.** Under “Question liminaire,” Grothendieck asks whether the specified group data permit recovery of the arithmetization, beginning with recovery of `N_a`. The question should be studied with the subgroup, its normalizing group, and the trivial-intersection condition all retained; the page does not justify dropping any of that input.
- **Scan 405, lines 8–14 — kind: unproved claim.** “Il suffirait” (ending uncertain) proposes an outer-isomorphism compatibility condition as a route to an affirmative answer. To establish the reduction one would need to show how preservation of the indicated subgroup and the finite-index product recovers the arithmetic structure, and specify whether compatibility is canonical or only up to the stated exterior equivalence.
- **Scan 405, circled g — kind: conjecture / expectation.** The condition marked “facultatif” asserts that elements in the indicated larger group which normalize the single-hatted subgroup and transport an open subgroup `N′` into `N_{g,ν}` already belong to `N_{g,ν}`. Its force is greater than the displayed self-normalizer consequence; no proof appears on this page, and the doubtful qualification is not treated as evidence that the statement is established.
- **Scan 405, final two lines — kind: unproved claim.** “serait son propre normalisateur” is presented as an “a fortiori” consequence of g. Under the literal quantified reading of g, the group-theoretic step would take `N′ = N_{g,ν}` and an element normalizing it; the substantive issue remains the validity and exact hypotheses of g itself.
- **Scan 405, circled g — kind: own idea.** Test whether the proposed transporter condition can be restated as a commensurator rigidity assertion inside the normalizer of the specified single-hatted subgroup. **Confidence: medium** as a possible reformulation, because a commensurating element transports a suitable finite-index intersection into the original group; conversely, one-sided transport may need additional index hypotheses, so equivalence is not asserted.


### Scan 406

- **Scan 406, lines 1–6 — kind: unproved claim.** “on fait un groupoïde” asserts a groupoid construction from the quoted “points de U,” with exterior fundamental group π and a strict action of the displayed Γ-group. A proof would need an explicit definition of the morphism torsors, composition, and strict action, together with independence from representatives of the conjugacy classes used for the objects.
- **Scan 406, lines 1–3 — kind: unproved claim / definitional issue.** At this point the manuscript writes “‘admissibles’ i.e. satisfaisant (20),” so the fixed-subgroup condition is being used as the criterion within this discussion. This should be checked against the author's later qualifications about admissibility, rather than silently assimilated to a modern definition or treated as a proven geometric classification.
- **Scan 406, lines 7–11 — kind: unpursued implication.** The NB distinguishes giving the group itself from giving only “son germe,” and interprets the stronger choice as a curve defined over a finite subextension K. The effect of changing that choice on the resulting strict action and field of definition is not worked out on this page.
- **Scan 406, lines 12–16 — kind: unproved claim.** “Les pts fixes de Γ correspondent” introduces an identification with points rational over K, followed by the analogous statement for a closed subgroup Γ′ and its associated field K′. Establishing this interpretation for the potential objects in question would require a justified link between the groupoid construction, admissible lifts, and geometric descent; the page gives the correspondence without that proof.
- **Scan 406, lines 1–6 — kind: own idea.** Construct the proposed groupoid initially from chosen representatives of the lift classes and explicit conjugating elements, then test how passage to a quotient changes isotropy groups and strictness of the Γ-action. **Confidence: medium** as a diagnostic construction, since it directly exposes the choices hidden by passing to conjugacy classes; it is not asserted to yield the groupoid intended by Grothendieck without further work.


### Scans 407–408

1. **Scan 407, approximately lines 1–6 — unproved claim.** The operation described as “bouchage des trous en I′” produces a new exterior group with lacets and the map (20). A proof would need to specify exactly which closed normal subgroup is killed and show that the construction does not depend on representatives of the exterior group or of its lacets. The relation between the Γ-stability of I′ and descent of the action is one of the visible hypotheses to check.

2. **Scan 407, approximately lines 7–12, (21) — unproved claim.** The statement “π′ hérite d'une arithmétisation” is followed by identifications of the arithmetic groups and of the objects written P. A proof should explain why the operation preserves this arithmetic datum and the indicated identifications; the last symbol in the following “même P” comparison is too uncertain to strengthen the statement beyond the display. This is a local proof obligation, not a claim that such preservation is false.

3. **Scan 407, approximately lines 16–20, (22) — unproved claim.** “On aura un hom canonique” introduces a map between the doubly hatted script groups, followed by a square involving the N-groups and the singly hatted script groups. Establishing the claim would require checking that the relevant automorphisms descend through (20), that they carry the designated subgroups to the designated subgroups, and that the normalizer-related maps are compatible. The uncertain vertical signs in the square should be resolved before choosing a precise categorical formulation.

4. **Scan 407, lines 1–20 — own idea; confidence: medium.** Test whether filling successively along nested Γ-stable subsets gives the same homomorphism as a single filling operation, with compatible identifications of the objects P. This is suggested by the words “canonique” and “hérite” and by (21)–(22), but composition and admissibility are not established in this local passage. A small diagram of three nested subsets would isolate the required compatibility without assuming a general functor already exists.

5. **Scan 408, approximately lines 3–7, (23) — unproved claim.** The composed homomorphism is called “injectif” and a “quasi-section.” To prove injectivity, one would at least need to show that the kernel of the map from N_a to N_{a′} meets the chosen copy of Γ trivially; the quasi-section condition also needs to be checked after passage to the displayed quotient. The ambiguous first connector in the preceding composition should not itself be used as a proof of injectivity.

6. **Scan 408, approximately lines 8–11 — unproved claim with an explicit proviso.** “Sous réserve d'admissibilité” precedes the assertion of a potential algebraic-curve structure relative to the same P. The phrase makes preservation of admissibility a separate missing step in the proposed construction, rather than a consequence already proved here. The surviving text at this point appears to say π without a prime, a reading left uncorrected in the transcription.

7. **Scan 408, approximately lines 11–16, cancelled (24) — conjecture / cancelled definitional proposal.** Inside a cancelled block, Grothendieck writes the fixed-point condition `(π′)^Γ = (1)` and proposes, “et s'il le faut,” to put the indicated family of conditions into the definition of admissibility. The cancellation is essential: these lines should be studied as a rejected or suspended formulation, not quoted as his settled definition. Determining which part was unsatisfactory would require comparing this proposal with the subsequent definition and with the geometric examples motivating it.

8. **Scan 408, approximately lines 17–19 — conjecture / open definitional question.** The surviving sentence explicitly says he is “gêné aux entournures” for lack of a “définition en forme” of “admissible.” This identifies a foundational gap on which the preceding construction depends. A study of these pages should therefore distinguish statements about arbitrary group actions from statements conditional on the intended admissibility notion.

9. **Scan 408, cancelled (24) — own idea; confidence: medium.** Test the proposed fixed-point requirement on small punctured examples and on actions satisfying the same elementary group-theoretic constraints but lacking an identified geometric origin. The purpose would be to examine whether the candidate condition is merely necessary, potentially sufficient after extra hypotheses, or too restrictive; no counterexample or sufficiency theorem is asserted here. The reason for the test is the visible gap between the concrete fixed-point equation and the still-unformulated admissibility condition.


### Scans 409–410

1. **Scan 409, line 1 — unproved claim / deferred clarification.** “je vais y revenir très vite” explicitly postpones a return to the preceding discussion. Any use of the admissibility terminology in this passage should be checked against the promised subsequent clarification, rather than treating the current fragment as a completed definition.

2. **Scan 409, lines 3–9 — unproved claim.** With the inserted hypothesis “si `I′ ≠ ∅`,” the exterior group is said to be describable by a “vrai groupoïde” with object set `I′` and a strict `Γ`-action, an assertion called “de l'algèbre pure.” A proof needs to construct the groupoid and its action and show in what sense they recover the given exterior-group data; the chosen nonempty object set and the distinction between strict and outer actions cannot be suppressed.

3. **Scan 409, lines 9–17 and (24) — unproved claim.** “Le fait que `Γ` opère” trivially on the objects is used to obtain the displayed canonical homomorphism and a conjugacy class of liftings. The object denoted `π′(i′)` and the comparison between different choices of `i′` must be specified before canonicity and independence up to `π′`-conjugacy have been proved.

4. **Scan 409, line 18 — conjecture / expectation.** “on espère” accompanies the condition `${π′}^{Γ} = 1`; the precise singular/plural wording around the hope is not secure. One should identify the hypotheses under which the proposed lifted action could have trivial fixed subgroup and whether admissibility is intended to provide those hypotheses.

5. **Scan 410, line 1 — unproved claim.** “Je dis que cette application est injective” refers to (25), the map from `I′` to the set denoted `Pts(π′, α′, Γ)`. A proof has to show that two distinct chosen objects cannot give the same relevant conjugacy class of admissible liftings, not merely that each object gives a class.

6. **Scan 410, lines 2–10 — unproved claim / requested internal proof.** The injectivity is termed “évident” under realization by a true algebraic curve and true rational points, but Grothendieck immediately asks for “des raisons internes.” The proposed internal inputs are the family `(N_{g,ν})` and properties of these groups; a proof would have to isolate a separation or conjugacy property that replaces the geometric realization argument.

7. **Scan 410, left marginal note — conjecture / deferred test case.** “On va revenir au cas card `I′ = 2` …” singles out a two-object case for later treatment. This is a useful explicit locator for checking whether the manuscript subsequently supplies the missing injectivity argument in a minimal nontrivial case.

8. **Scan 410, lines 11–15 and bottom arrow — unproved claim / conditional construction.** “Ce pt étant admis” precedes the functor called “bouchage de trous,” while the two possible admissibility definitions are put “entre parenthèses.” The construction needs to be checked on morphisms, not only on objects, and its dependency on the unresolved point-separation and admissibility issues should remain explicit.

9. **Scan 410, final functor — unpursued implication.** The source retains a chosen set `I′` of points at infinity, while the target retains a subset of a set of points. The arrow suggests that marking the points produced by filling holes is essential information for comparing the source and target; the page does not establish whether the resulting functor is faithful, full, or reversible.

10. **Scans 409–410, groupoid construction and injectivity — own idea. Confidence: medium.** Test the assertion on a connected two-object groupoid possessing a `Γ`-fixed isomorphism between its objects. If the resulting point classes coincide, the admissibility hypotheses must exclude that model; the reason for the confidence level is that the groupoid mechanism is elementary, but its identification with this manuscript's `Pts` construction still needs a proof.

11. **Scan 410, final functor — own idea. Confidence: medium.** Check whether filling two disjoint selected sets of holes in either order gives canonically isomorphic results, and whether retaining the resulting marked points permits a reverse puncturing operation. The reason is that the source and target inscriptions appear to retain the relevant marking data, but the page has not fixed admissibility or proved functoriality; this is a proposed test, not an established result or a claim of novelty.


### R409.12 — Scans 407 and 409 — own idea

Keep separate the setwise Γ-stability of I′ stated at the beginning of scan 407 and the pointwise trivial action used on scan 409. **Confidence: high** in the logical distinction, since an action can preserve a set while permuting its elements; whether a further hypothesis or restriction of Γ is intended here requires the surrounding definitions. This is a proposed consistency check of the hypotheses, not an assertion that the manuscript contains an error.

## Reference

Grothendieck, A. (1981). *La Longue Marche à travers la théorie de Galois* [Handwritten manuscript, cote 140-2, archive file “pages 1–292”; supplied scans 401–410, printed archive labels 400–409, visible upper manuscript pagination 203–207]. Université de Montpellier. Attribution, year, and archival identification are supplied by `LM_P041_prompt.md`; textual evidence is the ten attached image files.

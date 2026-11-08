# LM_C4-172-190 — Editorial and research notes

## Scope, provenance, and reading conventions

This package transcribes all 19 supplied scan images, using their filename numbers 172–190. It is a diplomatic reading of the attached rasters: uncertainty marks are substantive editorial information, and a completed inventory entry means that the element is represented, not that every character is certain. No external transcription, published edition, or later mathematical result was used to repair the manuscript.

The printed archive counters are one less than the filename numbers. Original large manuscript foliation is retained with `\mspage`. The institutional footer, its printed counter, and the matching pale pencilled archive foliation are archival apparatus and are excluded from the manuscript body. No manuscript page in this set is blank. The first and last images both contain text continuing across the supplied boundary.

| Scan | Printed archive counter | Original manuscript number visible |
|---:|---:|---:|
| 172 | 171 | — |
| 173 | 172 | 734 |
| 174 | 173 | — |
| 175 | 174 | 735 |
| 176 | 175 | — |
| 177 | 176 | 736 |
| 178 | 177 | — |
| 179 | 178 | 737 |
| 180 | 179 | — |
| 181 | 180 | 738 |
| 182 | 181 | — |
| 183 | 182 | 739 |
| 184 | 183 | — |
| 185 | 184 | 740 |
| 186 | 185 | — |
| 187 | 186 | 741 |
| 188 | 187 | — |
| 189 | 188 | 742 |
| 190 | 189 | — |

The LaTeX is a fragment with no preamble. Its host document must define the state/doubt macros requested in the task and provide standard mathematical commands, TikZ, and `tikz-cd`. Manuscript abbreviations, repeated numbering, unfinished sentences, and visibly nonstandard formulas are retained. Paragraph-internal line wraps are not reproduced mechanically. Ordinary handwriting is mapped to LaTeX alphabets; particularly uncertain alphabet choices are marked locally and discussed below. Small insertion guides are represented by placing `\inserted{…}` at the indicated point; separate drawings and diagrams are encoded in TikZ.

## 1. Table of doubts

Locations refer approximately to handwritten lines, displays, or relative page positions. Confidence describes the reading of the ink, not the truth of the mathematical claim. Some rows cover a repeated doubtful symbol or several closely related occurrences.

| Scan | Approximate line / location | Reading retained | Alternatives / issue | Confidence |
|---|---|---|---|---|
| 172 | (371) and following prose | `Π₁` / `π₁` | Cross-page image comparison finds the same handwritten glyph throughout; uppercase/lowercase is not securely distinguishable. | medium |
| 173 | Middle paragraph, fundamental group | `Π₁` / `π₁` | Same recurring glyph ambiguity as scan 172; no intentional case change is inferred. | medium |
| 174 | (372), its annotation, and final paragraph | `Π₁` / `π₁` | Same recurring glyph ambiguity; every occurrence carries the alternative. | medium |
| 175 | Opening prose and both diagrams | `Π₁` / `π₁` | Same recurring glyph ambiguity; the subscript remains visibly 1. | medium |
| 176 | Quotient annotation above (376) | `Π₁` / `π₁` | Same recurring glyph ambiguity as the neighbouring pages. | medium |
| 172 | Top continuation | `donc` | The final strokes are compressed. | medium |
| 172 | Cancelled expression above first display | `g_n≥3` | The cancellation obscures the relation and final character. | low |
| 172 | First display, right inner underbrace | `Û₁` | The U is heavily overwritten. | low |
| 172 | Cancelled intermediate equality | `2−2g_n=−n²` | The first sign and terms are crossed through. | low |
| 172 | (369), cancelled term | `2+` | Compact obliteration; the first digit is particularly doubtful. | low |
| 172 | (370), final bound | Overwritten `3`, replaced by `4` | Independent review distinguishes the surviving 4 from a lower remnant tentatively read as 3; the former numeral remains doubtful. | medium |
| 172 | Paragraph beginning “Si le yoga” | Deleted `existence` | Ending obscured by the strike; possibly plural. | low |
| 172 | Same paragraph, before “correspondent” | Deleted `s'expliquent par` / `s'expriment par` | Several letter bodies disappear beneath the strike; the q-descender is not securely visible. | low |
| 172 | (371), annotation beneath arithmetic group | `∩`, `U₁`, `M_{0,3}^{!}` | The arch is reproduced as a symbol, without resolving its intended inclusion direction; U is small; the final superscript resembles an exclamation mark. | low |
| 172 | After (371), insertion above “pts” | `3n` | The first stroke can also be read as a small letter. | medium |
| 173 | Line 2 | `refléter` / `réfléter` | Position of the first accent is uncertain; the manuscript has not been standardized to dictionary spelling. | medium |
| 173 | Line 3 | `arrivions` | `arrivons`; the short medial stroke is not sharply resolved. | medium |
| 174 | Line 2 | `celles` / `celle` | Independent review favours the plural, but the final stroke remains compressed. | medium |
| 174 | Line 6, cancellation after “Fermat” | `où` | The strike hides most of the two-letter word. | low |
| 174 | Line 8, ornate group letter | `𝔖₃` | Typeface/letter interpretation of the ornate handwritten glyph; reproduced consistently as Fraktur S. | medium |
| 174 | Last paragraph, extension reference | `372` | Final handwritten digit is compressed and can resemble 1. | medium |
| 175 | (373), deleted upper middle object | `G̃_{ρ,σ}[n]` | The underlying label is mostly obliterated; this is a tentative reading of the residual strokes only. | low |
| 175 | (373), labels at top and identity-like arrows | `𝓔_n`, `1` | The calligraphic extension letter resembles epsilon; short parallel strokes at arrows may instead mark a doubled arrow. | medium |
| 175 | (373), upper central vertical arrow | `ép.` | `ip.`; first letter and accent are weak. | low |
| 175 | (373), second/third central group objects | Fraktur `G̃` | The thick repeated tracing makes its typographic alphabet uncertain; (374) has a visibly simpler G. | medium |
| 175 | Above “une façon” | One cancelled word | The ink is fully blacked out at the supplied resolution; represented by `\deleted{\illegible{1}}`. | low |
| 175 | (374), between central object and quotient | Ditto-like pair of strokes `''` | Could be a compressed vertical equality. | low |
| 175 | Lower paragraph, cancelled word before “scindage” | `qui` | Only the first descending stroke and short i-like strokes remain visible. | low |
| 175 | Lower paragraph, before “tels scindages” | `(deux` | A second independent image reading resolved this as main text, not a marginal “choix”; the diagonal cancellation overlaps it. | high |
| 175 | Bottom, deleted phrase | `Cela est d'ailleurs` | Several letters are crossed through; possible alternative introductory wording. | low |
| 175 | Bottom insertion after “pt” | `fixe` | The abbreviated ending is cramped. | medium |
| 175 | Bottom, curve subscript | `U_∞` / `U_n` | Small loop-shaped subscript; not resolved by mathematical context. | low |
| 175 | Diagonal marginal note | `corresp.` / `correspondent`, deleted `étant` | The replacement and cancelled word overlap; wording remains tentative. | low |
| 175 | Marginal extension symbol | `G^{+∧}/μ` | A + followed by a small ∧ is visible at the upper right; the letter's flourish is compressed into the adjacent main line. | medium |
| 175 | End of marginal note | Deleted `dans`; reference `12°)` | Independent reading confirms the reference; the cancellation remains doubtful and no opening parenthesis is supplied. | medium |
| 176 | Annotation below E_n, before (376) | Rotated `≃`; `S_n` / `S_3` | Independent review finds two strokes in the connector and favours the n-shaped subscript; a doubtful rotated equivalence mark is retained. | medium |
| 176 | Parenthesis after (376), first word | `les` | Resolved on independent rereading; earlier alternative `Ces` was not retained. | high |
| 176 | Same line | `du niveau` | Resolved on independent rereading of the compressed connecting strokes. | high |
| 176 | End of parenthesis | `scholie` / `scolie` | The possible h is not separable from adjacent strokes. | medium |
| 176 | Last paragraph | `pts` / `pt`; `rationnels` / `rationnel` | Independent review favours the plural endings, despite the visibly singular article and verb; doubt is retained. | low |
| 176 | Below E_n in (377) | `\varphi` | A tiny curled mark is retained rather than omitted; it could be a linking mark instead of a letter. | low |
| 177 | 1, obliteration between “modulo” and the completed module notation | deleted n | The surviving blot does not establish the cancelled symbol. | low |
| 177 | 4, obliteration after U₁(Q) | deleted x₁ | Could be a different short cancelled symbol; x₁ is also inserted earlier on this line. | low |
| 177 | 5–7, group before and in (378) | γₙ | A differently formed Greek letter cannot be excluded. | medium |
| 177 | 11, after the abbreviation for “même” | “seulement” | Several middle letters are compressed. | medium |
| 177 | (379), label below underbrace | (Q*)^ | The final delimiter may be a square bracket rather than a rounded parenthesis. | medium |
| 177 | (379), third cohomology term | opening parenthesis after H¹ | It may be absent in the handwriting. | low |
| 178 | top displayed formula | blackboard G for the multiplicative group | Plain G is also possible from the handwriting; both occurrences are marked. | medium |
| 178 | lower half, “pratiquement nous … dans le” | “restons” | The middle letters are very compressed. | medium |
| 179 | title | “de” | “des” | medium |
| 179 | first paragraph, parenthesis | “caractère” | A few middle strokes are very light. | medium |
| 179 | second paragraph, after “des” | “s-gr.” | The first abbreviated letter is shaped like an x. | medium |
| 179 | third line of bracketed NB | deleted “avec” | Only crossed remnants survive; another short word is possible. | low |
| 179 | penultimate line | “s-groupes” | Possibly “sc-groupes” or a compressed “sous-groupes”. | medium |
| 179 | last line, deletion before the cyclic-group parenthesis | “discr.” | The cancellation crosses most of the final letters. | low |
| 180 | 4, after “celle de” | Π₀ with an extra star-like subscript stroke | Π₀ alone; the added or retraced stroke is not securely identifiable. | low |
| 180 | end of 4 | “les” | “des” | medium |
| 180 | 5–6 | “s-groupes”, “s-groupes-lacets” | A compact “sous-groupes” cannot be ruled out. | medium |
| 180 | condition following “de type (g,ν)” | inserted “anabélien i.e. ≠”; first pair (0,0) | First pair may have a retraced 1; independent review leaves deleted `avec` / `≠` unresolved. | medium |
| 180 | same condition, lower crossed-out pairs | (0,2), (1,0) | The first old pair is especially obscured; the corrected pairs above look like (0,1), (1,0). | low |
| 180 | cancellation between “système inductif” and “d'ensembles” | “avec une application” | “avec des applications”; the joining strokes and number are obscured. | low |
| 180 | cancelled unnumbered display | L(Π), L(Πᵢ) | Second object may be L₀(Πᵢ); the crossing line obscures any connecting mark, so no relation is supplied. | low |
| 180 | words before the cancelled numbered display | deleted “peut”, then “pose” | “prend” for the surviving word | low |
| 180 | surviving (1), superscript on L₀ | ♮ | ♯; comparison with the germ notation on scans 188–189 supersedes the initial conjectural reading G/Gᵢ. | medium |
| 180 | crossed-out paragraph below (1) | “On suppose que Π admet un ensemble générateur fini, donc un syst.” | The word “que” and final four-word fragment are only tentative. | low |
| 180 | live nonemptiness condition near bottom | L(Πᵢ) ≠ ∅ | The argument may be Πᵢ₀; no subscript 0 is securely visible on L itself. | medium |
| 181 | (2), (3), margin, and inline terms | superscript ♮ on L₀ | ♯; the same lightning-shaped superscript appears on the germ notation of scans 188–189. | medium |
| 181 | oblique margin, conjugation notation | int(g), with one larger initial read Int(g) | Initial capitalization is not secure; both alternatives are retained locally. | medium |
| 181 | deletion above “les morphismes canoniques” | “On doit prouver” | The last word is partly crossed and its ending is compressed. | medium |
| 181 | after underlined “L-structure” | a dot | The isolated point may be stray ink rather than punctuation. | low |
| 181 | subgroup in the last paragraph | Π′₀ | Π₀ with an upturned terminal stroke on the top bar; the small 0 is visible. | low |
| 181 | (4), left object | L(Π) | L₀(Π); the lower-right loop on L could be a closely attached subscript. | medium |
| 182 | Equations (5)–(6) and lower annotation | `Π₁` / `π₁` | Independent comparison with scans 172, 174, 176, and 185 shows the same glyph, whose uppercase/lowercase form is not securely distinguishable. | medium |
| 183 | Surface fundamental-group expressions | `Π₁` / `π₁` | Same recurring handwriting ambiguity; no case distinction is supplied from mathematical convention. | medium |
| 185 | Equation (4), fundamental-group term | `Π₁` / `π₁` | Same handwritten glyph as in the earlier exact sequences; every occurrence is marked. | medium |
| 182 | 6, overwritten expression after `Π/Π₀` | deleted `≃ G` | The lower strokes are heavily overwritten; the former relation and letter remain tentative. | low |
| 182 | 6, replacement above the same expression | `→ Autext(Π₀)` | The letters of `Autext` overlap the cancelled version. | medium |
| 182 | 7, after “sur l’” | `ens` | A contracted “ensemble” is likely, but the final stroke is indistinct; no abbreviation point is confidently visible. | medium |
| 182 | 13, addition above “anabélienne” | `0-conn.` | The ending of the abbreviated qualification is compressed. | medium |
| 182 | 15, former equation number | deleted `4`, replaced by `5` | The former numeral is almost covered by the correction. | low |
| 182 | 15, final argument of `Π₁(X,G;…)` | solid dot `•` | The mark is much smaller than the `a` in the following prose and in the lower annotation. It is retained as a dot without reconciling the discrepancy. | high |
| 182 | 18, exact sequence | headless first and last strokes; middle arrows rightward | The terminal strokes do not show the distinct arrowheads visible on the middle arrows. | medium |
| 183 | 6, before inserted “l’existence” | `de` | `des`; an overlapping ending is unclear. | medium |
| 183 | 10, inserted verb before “un bon énoncé” | `dégager` | `disposer`; the long opening stroke and final letters are difficult. | low |
| 183 | 12, deleted words after inserted “X de caractère fini,” | `par des` | The cancellation traverses most letter bodies. | low |
| 183 | 12, article before “signature” | `d’une` | `d’un`; the ending is only a short joining stroke. | medium |
| 183 | 12, quoted noun | `signature` | The middle and ending of the word are compressed; the reading is not supplied solely from the mathematical context. | medium |
| 183 | 13, small cancelled ending after “fini” | deleted `e` | It may be only a corrected final stroke rather than a full letter. | low |
| 183 | 18, after `Π₁(X;G,a)` | comma | semicolon; the mark is thickened. | medium |
| 184 | 4, first word | `Celà` | `Cela`; a small mark above the final vowel may be an accent or a stray stroke. | medium |
| 184 | 8, after “un travail de” | `raccordage` | Some internal vowels are reduced to short strokes. | medium |
| 184 | 11, after “pour” | `traiter` | `trouver`; the middle of the word is crowded. | medium |
| 185 | 6, cancelled isolated symbol after “le groupe” | `𝔐` | `𝔊`; dense cancellation prevents confident identification. | low |
| 185 | 7, cancelled beginning of equation (4) | `𝔐₀,₃⁺` | `𝔊₀,₃⁺`; the subscript and superscript are also partly covered. | low |
| 185 | 7, matrix-group name | `Sl` | `SL`; the second letter has a loop like a handwritten lower-case l. No capitalisation correction has been made. | medium |
| 185 | 15, end of interlinear parenthesis | `orientation` | The final letters are squeezed against the right side. | medium |
| 186 | 4, after inserted `L-` | `autom` | `aut`; the terminal abbreviated strokes are on the baseline, not a clear superscript. | medium |
| 186 | 5, heavily ornamented group letter | `𝔊₀,₃⁺` | `𝔐₀,₃⁺`; an M-like stroke overlaps the main letter. | low |
| 186 | 9, middle object of exact sequence | `𝔊₀,₃⁺` | `𝔐₀,₃⁺`; the same crowded letter form recurs. | low |
| 186 | 12, parenthetical `L-…` | `autom` | `aut`; the abbreviated ending is compressed and no point is clearly visible. | medium |
| 186 | 18, deleted symbol before the map arrow | `Π` | The remaining strokes do not support a more confident reading. | low |
| 187 | 1, 19: ornate group symbol | `\mathfrak G_{0,3}^{+}` | Handwritten ornate alphabet; the main body resembles G, but comparison with the symmetric-group S is difficult. No extra tilde is inferred from its upper flourish. | medium |
| 187 | 6, 8 | `SPG` | `SPS`; the final capital has a descending stroke. | low |
| 187 | 8: deletion before `\dot\sigma_0` | `\dot\sigma` | The small symbol is heavily struck through; an initial sigma is the best visual reading. | low |
| 187 | 9 | `c'est` | The initial letters are highly contracted; the proposed reading is retained only with a doubt mark. | medium |
| 188 | 1, 3–4, 6: ornate group symbol | `\mathfrak G_{0,3}` and its `+` form | The alphabet remains a visual uncertainty, as on scan 187. | medium |
| 188 | 12: replacement above `famille` | `ensemble fini` | The first strokes overlap the deleted f, so the beginning is less clear than the rest. The surviving `d'une` is not silently changed to `d'un`. | medium |
| 188 | 13, display (5): superscript on k | `\natural` | Possibly `\sharp`; retained as a doubtful natural sign, without normalizing to an exterior-morphism convention. | low |
| 188 | display (5): overwritten source object | deleted `\mathbb Z`, inserted `T` | Z-like lower strokes remain visible under the darker T. | low |
| 188 | final inserted words | `Pour` | The capital is overwritten and has additional bars; the rest of the phrase is clear. | medium |
| 189 | 1: small overwritten mark before `\Pi_0` | deleted `à` | A compact loop is overwritten; whether it was a word or an aborted symbol cannot be established from the ink. | low |
| 189 | 4: deletion between `hom.` and `effectifs` | `ext.` | Almost completely inked over; the central crossing and terminal trace give only weak support. | low |
| 189 | 5: superscript on k | `\natural` | Alternative `\sharp`, as on scan 188. | low |
| 190 | 3: before T in the germ's source | deleted `n` | The dark mark is visibly cancelled; n is the best reading, but its strokes are congested. | low |
| 190 | 4: superscript on k | `\natural` | Alternative `\sharp`, as on scans 188–189. | low |
| 190 | 9: after `sur \Pi_0,` | `\xi` or `&` | A separate curled sign precedes « évidemment »; its shape could be a Greek xi or the author's ampersand. Both alternatives are retained locally. | low |

## 2. Abbreviations met

Expansions are proposed only here and have not been substituted into the transcription. A repeated abbreviation can have different functions in different passages.

| As written | Proposed expansion or function | Scan group |
|---|---|---|
| `EP`, `EP!` | caractéristique d'Euler–Poincaré; exclamation convention possibly compact support | 172–176 |
| `i.e.` | id est | 172–176 |
| `rat/ℚ` | rationnels sur ℚ | 172–176 |
| `pt`, `pts` | point, points | 172–176 |
| `th.` | théorème | 172–176 |
| `m̄` | même | 172–176 |
| `Ker` | noyau | 172–176 |
| `dt` | dont | 172–176 |
| `ét` | étale | 172–176 |
| `ép.` | épimorphisme (tentative reading of a diagram label) | 172–176 |
| `ext.` | extension, in the marginal note on scan 175 | 172–176 |
| `corresp.` | correspondent (tentative reading) | 172–176 |
| `géom.` | géométrique | 172–176 |
| `pr.` | produit | 172–176 |
| `½ direct` | semi-direct | 172–176 |
| `dfn` | définition | 172–176 |
| `prop.` | proposition | 172–176 |
| `p.` | page | 172–176 |
| `ff` | et suivantes | 172–176 |
| pt | point | 177–181 |
| mod | modulo | 177–181 |
| dfn over an equality | définition; “equal by definition” | 177–181 |
| $\overline{\mathrm m}$ | même | 177–181 |
| dim | dimension | 177–181 |
| pts | points | 177–181 |
| i.e. | id est | 177–181 |
| hom. | homéomorphe(s), in the description of the surfaces | 177–181 |
| s-gr. | sous-groupes | 177–181 |
| s-groupes | sous-groupes | 177–181 |
| NB. | nota bene | 177–181 |
| discr. (cancelled, uncertain) | discrets | 177–181 |
| pb | problème | 177–181 |
| ens | ensemble | 177–181 |
| ens. | ensemble | 177–181 |
| syst. (cancelled, uncertain) | système | 177–181 |
| sous-ens. | sous-ensemble | 177–181 |
| dist. | distingué | 177–181 |
| fi. | fini | 177–181 |
| int(g), Int(g) | inner automorphism induced by g; initial capitalization uncertain | 177–181 |
| Im | image | 177–181 |
| `NB` | nota bene | 182–186 |
| `ens` | ensemble | 182–186 |
| `0-conn.` | 0-connexe | 182–186 |
| `pt` | point | 182–186 |
| `pts` | points | 182–186 |
| `op. ext.` | opérations extérieures | 182–186 |
| `essᵗ.` | essentiellement | 182–186 |
| `supp` | support | 182–186 |
| `etc` | et cetera | 182–186 |
| `p.ex.` | par exemple | 182–186 |
| `autom` / `aut` | automorphisme | 182–186 |
| `hom` | homomorphisme | 182–186 |
| `Dém.` | démonstration | 182–186 |
| `Autext` | automorphismes extérieurs | 182–186 |
| `hom.` | homomorphisme | 187–190 |
| `i.e.` | id est | 187–190 |
| `resp.` | respectivement | 187–190 |
| `SPG` / `SPS` | Uncertain: possibly an abbreviation of « supposons » or « sans perte de généralité »; the letters themselves remain doubtful. | 187–190 |
| `autos` | automorphismes | 187–190 |
| `autom.` | automorphisme | 187–190 |
| `int` | intérieur | 187–190 |
| `rg` | rang | 187–190 |
| `ext.` | extérieur | 187–190 |
| `ens` | ensemble | 187–190 |
| `nb` | nombre | 187–190 |
| `p. ex` | par exemple | 187–190 |
| `NB` | nota bene | 187–190 |
| `ens.` | ensemble | 187–190 |

## 3. Legibility and editorial limitations

The continuous prose and main surviving formulas are generally more legible than the cancellations and interlinear work. Scans 173–174, 178, and 184 are comparatively clear. The weakest readings are the overwritten computation and small annotation on scan 172; the replaced diagram object and crossing diagonal note on scan 175; the repeatedly revised definitions and excluded types on scan 180; and the crowded surface/signature additions on scan 183. Several small cancelled symbols and rapid word endings elsewhere remain doubtful. One completely blacked-out word on scan 175 is represented by `\deleted{\illegible{1}}`; doubtful mathematical symbols have tentative readings rather than `\illegible` substitutes.

Every assigned page was read as a whole, transcribed, and reread with enlarged strips or selected close crops, followed by an element inventory. The dense crossings on scans 175 and 180–181 and selected early-page readings received additional independent checks. Those checks resolved some readings, including the main-text “deux tels scindages” on scan 175, while leaving other alternatives marked. They do not establish an error-free or authoritative critical text. The last page is treated through its actual cutoff, “d’une telle”.

The transcription was checked for ordered page coverage, macro arguments, balanced braces/environments, correspondence of the inventory to the page ranges, and the required archive contents. A full typographical proof is not part of this deliverable; the fragment deliberately leaves macro design and page layout to its host document.

## 4. Research notes — English, separate from the transcription

These entries concern what is stated, suggested, or left unproved **within the supplied excerpt**. They do not claim that a question remains open in the rest of the manuscript or in present-day literature. References to earlier manuscript pages are reported as references to be checked, not as pages inspected in this task. Own ideas are expressly labelled and are neither assertions of established results nor claims of novelty. The common primary-source citation is Grothendieck (1981), with the scan and local position given for each entry.

### Scans 172–176

### Scan 172, lower half — conjecture / expectation

“Si le yoga … est valable” makes the proposed correspondence between rational points and suitable splittings conditional. The page also singles out splittings at infinity and a centralizer condition involving the kernel of the cyclotomic character; a proof would have to specify precisely how that group condition selects the geometric sections.

### Scan 172, upper half — unpursued implication

The displayed genus formula and the assertion that the open curves are anabelian distinguish the punctured curves from their compactifications at small n. A comparison of the section statements must retain that distinction, particularly at n=3, where the displayed compactified genus is one.

### Scan 173, lines 3–8 — conjecture / expectation

“Si nous arrivions à prouver l'inexistence de scindages … autres que ceux … à l'infini” proposes proving the needed nonexistence directly, without first proving the full “yoga anabélien.” The implication requires the point-to-section construction and a proof that a section arising from an interior rational point cannot be one of the excluded sections at infinity.

### Scan 173, lines 9–16 — conjecture / expectation

“Il n'est nullement exclu qu'une analyse assez poussée” of M₀,₃ and N₁,₁ could rule out nontrivial splittings for every n≥3. The page proposes increasingly fine approximations of both the fundamental group and its extension structure but does not provide the obstruction that would establish that nonexistence.

### Scan 173, final lines — unpursued implication

“Chaque nouvel affinement” of the Lie approximations is to prompt a renewed study of the splitting question. One issue worth separating is whether failure to split is detectable at a finite stage or only in the compatibility of sections across all stages; this distinction is not resolved on this page.

### Scan 174, first paragraph — unproved claim

The current approximation is called the “approximation ‘minima’” in which the Fermat tower can be expressed algebraically. A precise minimality assertion would need a category of allowed approximations and a demonstration that every coarser quotient loses the relevant covering data; the page refers back to 13° rather than giving such a universal property here.

### Scan 174, middle — conjecture / expectation

The calculations “semblent suggérer” that the extension enriched by the three-letter permutation group “jouera un rôle important.” The potentially useful additional datum is the symmetry action together with the arithmetic extension; the page does not yet show that it adds an obstruction to splitting.

### Scan 174, last paragraph — unpursued implication

The move to a quotient extension keeps the group action while discarding a normal subgroup of the geometric fundamental group. It is worth checking exactly which information about conjugacy classes of sections survives the quotient, since the proposed application concerns those classes and not merely the quotient group itself.

### Scan 175, (373)–(374) — unproved claim

The displayed comparison is offered as a way to “construire ‘algébriquement’ les diagrammes (373),” with the image of M̂[n]→M̂ specified as nM̂. Verifying the construction requires checking that the normal subgroup defining the quotient is preserved by the arithmetic and symmetry actions and that every displayed row remains exact.

### Scan 175, lower paragraph — unproved claim

The manuscript says the relevant splittings are “conjugués par un unique élément de M̂.” Conjugacy existence and uniqueness are distinct assertions; their proof must account for both the obstruction to conjugating two sections and the centralizer of a fixed section.

### Scan 175, lower paragraph — own idea

**Confidence: high as a formal reformulation, without asserting the required vanishings.** Once the displayed abelian-kernel semidirect-product description and its action are fixed, transitivity of kernel conjugation on sections can be tested through continuous H¹, while uniqueness is controlled by H⁰. This separates two requirements hidden in “un unique élément” and gives a concrete way to audit the assertion.

### Scan 176, (375)–(376) — unproved claim

The compatible quotient extensions are identified with the displayed semidirect products, with the subgroup nM̂ identified by definition with M̂[n]. A verification should distinguish the chosen splitting from canonical data and check its compatibility with the geometric basepoints and the arithmetic action throughout the tower.

### Scan 176, parenthesis after (376) — conjecture / expectation

The author says these interpretations “mériteraient de figurer” in the earlier scholie-proposition and refers to p. 712′ ff. That backward reference should be checked for the exact hypotheses; those earlier manuscript pages are not among the supplied images.

### Scan 176, last paragraph — unpursued implication

“Un pt … définit un scindage” introduces the passage from a rational point to a section of the quotient extension (377). The subsequent analysis must distinguish existence of such a quotient section from lifting it to the full extension and from its coming from a rational point; this page alone supplies no converse.

### Scans 177–181

- **Scan 177, upper half — unproved claim.** The passage says that knowing the splitting “implique la connaissance du pt correspondant” and obtains uniqueness of the lifted rational point when the quotient in (378) is trivial for odd n. A proof of the stated dependence on the splitting would need the precise comparison map of extensions and the equivalence relation on splittings from the preceding pages; the elementary roots-of-unity calculation alone does not supply that comparison.
- **Scan 177, lower half — conjecture/question.** “Afin d'examiner (si faire se peut) lesquels peuvent raisonnablement correspondre” explicitly leaves open which splitting classes are geometric. The task is to distinguish classes coming from rational points inside the cohomology group displayed in (379).
- **Scan 177, (379) — unproved claim.** The chain of identifications ends in G(Q)^ without a proof on this page. Its justification needs the module action, the manuscript's Tate-twist convention (the visible sign is −1), the meaning of the completion, and the relevant Kummer comparison.
- **Scan 177, (378)–(379) — own idea; confidence: medium.** Compare the ambiguity in lifting rational points for even and odd n before imposing a geometricity condition on cohomology classes. This is a useful test because the displayed quotient is trivial for odd n, whereas the same elementary argument permits a nontrivial sign ambiguity for even n; the manuscript definitions and any excluded boundary points must be checked before treating this as a result.
- **Scan 178, central and lower paragraph — conjecture/question.** The present approximation is judged “beaucoup trop grossière”, and the page concludes that it is “nécessaire de passer à des approximations plus fines”. The proposed next step is to find invariants that see the equation of Uₙ rather than only the ambient torus.
- **Scan 178, equation and surrounding prose — unpursued implication.** The author observes that the current cohomological description proceeds “sans nous préoccuper de l'équation”. This isolates a failure of this approximation to distinguish the curve from its torus embedding; the exact additional relation needed in a finer quotient is not developed on this page.
- **Scan 178, displayed torus and equation — own idea; confidence: medium.** Before using the displayed equation as a test for geometric splitting classes, check how its three coordinates and the right-hand side 1 are interpreted after taking the diagonal quotient. This is an editorial and mathematical consistency check motivated by the simultaneous quotient notation and equation on the page, not a proposed correction to either.
- **Scan 179, first paragraph — unpursued implication.** The reason for introducing L-groups is to “englober des groupes fondamentaux mixtes” of surfaces with finite automorphism groups. This points toward a formulation that keeps peripheral data under finite extensions, but the equivalence with a geometric or orbifold formulation is not established on this page.
- **Scan 179, second paragraph — unproved claim.** “Tout sous-groupe d'indice fini … hérite une structure à lacets” is recalled as something already seen. A verification would have to track intersections with peripheral subgroups, duplicate conjugacy classes, and the exceptional low-complexity surfaces expressly excluded in the bracketed note.
- **Scan 179, bracketed note — unpursued implication.** The exception says that in certain small types the structure is not determined “par la seule donnée” of conjugacy classes of cyclic subgroups. A useful comparison with the later germ-based definition would identify exactly which orientation or multiplicity information those subgroup classes lose.
- **Scan 180, first paragraph — unproved claim.** The structure “se récupère” from a finite-index subgroup by taking centralizers of its peripheral subgroups. A proof needs the appropriate centralizer statements and control of the exceptional types; the qualification “quand elle existe!” also separates uniqueness of recovery from existence.
- **Scan 180, revised definition — unproved claim.** The sets of structures “forment un système inductif”, but transition maps and their compatibility are not proved here. The revisions make invariance under the quotient group explicit, so compatibility must include that equivariance condition.
- **Scan 180, last paragraph — unproved claim.** Nonemptiness is used to obtain a finite generating set and then a cofinality statement for normal finite-index subgroups. A proof should separate the finite-generation assertion from the normal-core construction, and should use the exact nonemptiness object intended by the partly ambiguous subscript.
- **Scan 180, surviving (1) — own idea; confidence: medium.** Check whether passing to a common normal finite-index subgroup provides a direct construction of the transition maps between invariant peripheral structures. This is suggested by the quotient invariance in (1) and would make the independence of a chosen finite-index subgroup easier to test, but the injectivity and geometric admissibility conditions still need proof.
- **Scan 181, oblique marginal note — unproved claim.** When the subgroup is not normal, the author says “on peut définir” invariant structures by agreement with conjugates on the intersections of the relevant subgroups. A proof must show that this agreement condition is compatible with restriction to further finite-index subgroups and with the invariant-structure set already defined for normal subgroups.
- **Scan 181, (3) — unproved claim.** The canonical maps into the limit “sont injectifs”, and this is immediately used to attach a unique lacet structure to a subgroup of definition. The missing step is a uniqueness-of-recovery argument showing that distinct structures cannot become equal after restriction to a smaller finite-index subgroup.
- **Scan 181, (4) and following sentence — unproved claim.** The induced map of L-structures is said to be “injectif”, with its image to be characterized by the sentence continuing on the next scan. Establishing that characterization would require descent of the peripheral structure as well as injectivity; the uncertain handwritten source notation should be settled before giving a precise statement.
- **Scan 181, margin and definition paragraph — own idea; confidence: medium.** Compare the marginal intersection condition with descent data on the finite-index subgroup and its conjugates. The explicit agreement on intersections suggests this comparison, but compatibility for all conjugating elements and the distinction between actual structures and limit classes must be checked before claiming an equivalence.

### Scans 182–186

The following notes concern only the supplied manuscript pages. They do not assert that the proposed questions remain open elsewhere in the manuscript or in the literature. Source: Grothendieck (1981), scans cited individually below.

### Scan 182, upper half — unproved claim

For an extension by a finite group, the text says that the L-structures on the full group “correspondent aux L-structures” on the subgroup that are invariant under the outer action. A proof would need to show that invariance of the subgroup structure is sufficient for descent and that the result is independent of the representatives used for the outer action. The displayed replacement map itself is partly overwritten, so the exact notation should be checked before formalising this statement.

### Scan 182, bracketed NB — unpursued implication

The assignment `Π ↦ L(Π)` is said to be “un foncteur en les groupes extérieurs”, with outer isomorphisms as arrows. This suggests that any subsequent classification should preserve the distinction between a structure on a particular group and a structure transported through an outer isomorphism. The page does not develop this distinction further.

### Scan 183, lines 2–9 — conjecture

“Il semble que ∀ L-groupe soit isomorphe à un groupe obtenu ainsi” proposes a geometric presentation by a finite group acting on a surface. The phrasing remains tentative, and the author describes the asserted result as deep and “pas compris totalement”. A classification would have to specify the admissible surfaces, finite actions, and exceptional cases.

### Scan 183, lines 6–8 — unproved claim

The proposed geometric realisation is described as essentially equivalent to the existence of fixed points for finite subgroups of Teichmüller groups. This equivalence is asserted rather than established on the page. A proof would need both the passage from a finite outer action to a geometric action and the converse construction, with the relevant Teichmüller object and action specified.

### Scan 183, lines 9–15 — conjecture

The author asks for a “bon énoncé” relating the 2-category of L-groups to surfaces with the indicated signature data. The statement has several additions and deletions, so it is a proposed formulation rather than a settled definition here. The meaning of its morphisms and 2-morphisms is particularly worth checking against subsequent manuscript pages.

### Scans 183–184, connecting paragraph — conjecture

The author expects, outside certain “triviaux” cases, a faithful finite-group presentation, followed by a criterion involving trivial centralizers of every subgroup of finite index. “Cela devrait donner une description” expresses the hoped-for intrinsic description. Both the exceptional cases and the exact implication between faithful presentation and the centralizer condition require further scrutiny.

### Scan 184, middle — unpursued implication

“Un travail de raccordage à faire” is proposed to treat the general case through finite-group extensions of L-groups. The page does not give that construction. One would need to determine which extension data preserve the peripheral structure and how different extensions are identified.

### Scan 184, lower half — unpursued implication

The text says that “il faudrait faire le lien” with associated L-Galois topoi, by adapting the corresponding developments for groups with loops. This points to a reconstruction or comparison problem, but no equivalence of categories or topoi is stated here. The relevant notion of L-Galois topos should be recovered from the surrounding manuscript before formulating a precise theorem.

### Scan 184, centralizer discussion — own idea

One possible checking strategy is to compare the proposed centralizer condition with the kernel of the finite group action in explicit finite extensions of surface groups. **Confidence: medium**, because the text itself ties faithful actions to centralizers, but the necessary hypotheses and exceptional cases are not fixed on these pages. This is a suggested test of the formulation, not an asserted result or a claim of novelty.

### Scan 185, opening paragraph — conjecture

“Il se pourrait” that L-groups provide the right general context for defining and studying Teichmüller groups, rather than only groups with loops. This is an expectation about the scope of the definitions. It leaves open what extra constructions or invariance properties the broader context should support.

### Scan 185, lower half — unproved claim

For the displayed group, every direct L-automorphism is said to be inner, where direct means inducing the identity on the orientation module. The claim is not proved at that point; scan 186 begins an argument through preservation of the subgroup `Π₀,₃`. Establishing the preservation statement alone still leaves the relation between the restricted automorphism, its peripheral data, and innerness to be checked.

### Scans 185–186, connecting paragraph — conjecture

“Il se pourrait que cette propriété” together with trivial centre, or the stronger finite-index centralizer condition, characterises the displayed group up to “isomorphisme (non unique)”. The text explicitly distinguishes these two possible additional assumptions. Testing the weaker condition separately from the stronger one could reveal which part of the proposed characterisation is intended to exclude exceptional or ineffective examples.

### Scan 186, middle and lemma — unproved claim

The author strengthens the preservation claim to “tout automorphisme de la structure de groupe”, not merely L-automorphisms. The lemma states that a normal subgroup with quotient `𝔖₃` must be `Π₀,₃`, and more precisely that every surjection to `𝔖₃` is conjugate to the canonical one. A proof starts at the bottom with the presentation `ρ³ = σ² = 1` and continues on the next scan; the claim is therefore not being labelled permanently unproved.

### Scan 186, lemma — unpursued implication

Uniqueness of the kernel among normal subgroups with the stated quotient would make `Π₀,₃` characteristic, directly explaining the preceding preservation assertion. The stronger assertion about conjugacy of surjections controls more than the kernel alone. Keeping those two levels distinct is useful when tracing how the later automorphism argument uses the lemma.

### Scans 187–190

- **Scan 187, lines 1–10 — unpursued implication.** The argument ending « et on gagne » classifies the relevant surjections by conjugating the images of the order-three and order-two generators. One can ask how far the same image-normalization argument extends when the target is a different finite quotient; this would require keeping track of conjugacy classes and of whether the chosen generator images still generate the whole target.
- **Scan 187, lines 11–20 — conjecture.** The proposed definition « groupe de Teichmüller » is revised in the same paragraph to use exterior L-automorphisms of the orientation subgroup. The property singled out is that the “direct” group for the displayed genus-zero, three-marked group « est réduit à 1 »; its status and hypotheses should be checked against the immediately preceding pages rather than inferred from the definition alone.
- **Scan 188, lines 1–6 — conjecture.** « Cette propriété est peut être caractéristique » proposes that uniqueness of the inducing element could characterize the displayed discrete L-group. A proof would need to specify the class of L-groups being compared and rule out nonisomorphic groups having the same exterior-automorphism property.
- **Scan 188, lines 7–17 — unpursued implication.** The reformulation by a rank-one orientation module and « germes d'hom. extérieurs » suggests separating the orientation datum from the peripheral maps. The equivalence of this reformulation with the earlier definition requires checking that restriction to finite-index subgroups does not lose either peripheral multiplicity or the intended conjugacy information.
- **Scan 189, lines 1–8 — unproved claim.** The text states « on trouve un nb fini de germes » after passage to a finite-index subgroup. A proof should describe the conjugacy classes of representatives that land in the subgroup and explain why restriction to smaller subgroups of the rank-one source produces only finitely many relevant exterior germs.
- **Scan 189, lines 9–13 — unpursued implication.** The asserted « unique axiome » is existence of a finite-index subgroup whose induced structure comes from a lacet structure. The independence of this condition from the particular witnessing subgroup is a natural compatibility question for further finite-index passage.
- **Scan 189, final paragraph — unpursued implication.** « On peut généraliser » introduces the removal of the finite-index requirement. The next page must be read together with this proposal, because the present page stops at « mais en » and does not yet state the replacement condition.
- **Scan 190, left marginal NB — conjecture (explicit doubt).** « il n'est pas clair a priori que cet ens. de germes d'hom. ext. soit fini » flags an unresolved finiteness issue in the generalization. This is separate from the finite-index statement on scan 189: either a proof or an admissible counterexample is needed once the witnessing normal subgroup is allowed to have infinite index.
- **Scan 190, lines 7–11 — unproved claim.** A lacet structure is said to be « uniquement déterminée, une fois Π₀ choisi ». A proof would have to show that the supplied exterior germs and orientation module recover the whole lacet structure, including any normalization or multiplicity data that passage to germs might suppress.
- **Scan 190, lines 11–15 — unproved claim.** The witnessing subgroup is asserted to be determined « à commensurabilité près », and the visible inserted intersection is claimed to have finite index in each of two witnesses and to satisfy the same requirement. No proof is supplied on this page; one should check both finite-index assertions and preservation of the induced lacet structure under intersection.
- **Scans 188–190 — own idea; confidence: medium.** One possible way to organize a test of the definition is to compare a chosen peripheral homomorphism with its restrictions to the finite-index subgroups of the rank-one orientation module, recording exactly which generator and multiplicity information survives as a germ. The reason for this suggestion is the manuscript's explicit move from homomorphisms to germs and its simultaneous uniqueness claim; it is a proposed check, not a claim of equivalence, validity, or novelty.

## Reference

Grothendieck, A. (1981). *La Longue Marche à travers la théorie de Galois* [Handwritten manuscript, cote 140-4, supplied scans 172–190 of the archive file covering pages 650bis–787]. Université de Montpellier archive. Bibliographic identification follows the attached task prompt; readings are based on the attached scan images.

# LM_P052 — Editorial and research notes

## 1. Source and coverage

The transcription covers the ten supplied images, `LM_P052_scan511.jpg` through `LM_P052_scan520.jpg`, in filename order. All readings, quotations, and manuscript-specific observations refer to Grothendieck (1981), as supplied with the task; the scan and equation locators in the tables and research headings specify the cited passage. No published transcription, later manuscript passage, or external mathematical source was used to fill gaps in the handwriting.

The three numbering systems are kept separate:

| Scan used by `\scanpage` | Archive number visible in the image | Author's number visible at the top |
|---|---|---|
| 511 | 510 | 261 |
| 512 | 511 | — |
| 513 | 512 | 262 |
| 514 | 513 | — |
| 515 | 514 | 263 |
| 516 | 515 | — |
| 517 | 516 | 264 |
| 518 | 517 | — |
| 519 | 518 | 265 |
| 520 | 519 | — |

The archive's website/address footer and its duplicate page labels have not been treated as manuscript text. No author page number has been interpolated on the intervening images. The initial and final sentences of the extract remain open where the supplied pages begin or end.

### Reading conventions

The `.tex` file is a fragment, with no preamble or macro definitions. It uses the editorial macros requested in the task; a host document must define those macros and load the usual mathematical LaTeX facilities and `tikz-cd`. Its syntax was checked by compiling it inside a temporary wrapper; the wrapper and generated PDF are not part of the deliverable. Diagram matrices use `ampersand replacement=\&` so that they remain valid when passed as arguments to `\diagram`.

An `\unsure` is a positive warning about a proposed reading, even when the mathematics makes that reading attractive. An `\illegible{n}` counts an estimated number of unreadable units; in cramped mathematical deletions a unit can be a symbol rather than a word. Insertions and deletions do not imply a fully recoverable chronology of the revisions. Marginal paragraphs are placed beside the relevant passage in reading order; this is not a facsimile of their diagonal placement.

In particular, visible variation between `03` and `0,3`, between `11` and `1,1`, and between hatted and unhatted symbols has not been globally regularized. The lower-case-looking `l` of `Sl` and `Gl`, the author's abbreviations, uneven parentheses, and the surprising marginal formula on scan 519 are retained. The research notes do not authorize any change to the transcription.

## 2. Table of doubts

Locations are approximate handwritten lines or identifiable displays, not line numbers in the reflowed LaTeX. **High** means that the visible feature is clear, even if unusual; **medium** means a supported but incomplete reading; **low** means substantial ambiguity or an unreadable passage. A few rows document an important visible feature or revision rather than a choice between two words. Repeated instances of the same uncertain glyph can share a table row; their doubt marks remain at the individual occurrences in the transcription.

| Scan | Approximate line / position | Reading retained | Alternative or unresolved detail | Confidence |
|---|---|---|---|---|
| 511 | 2, after « des » | `rev\textsuperscript{ts}` | Contracted *revêtements* is likely; the raised letters and possible circumflex are not fully separable. | medium |
| 511 | 3, after « maximum » | `imposé` | `imposée`; final small stroke does not decide the ending. | medium |
| 511 | Display below « galoisiens » | `B` / `D` as left object of the classifying-topos map | The baseline glyph is unclear; a B-like retraced glyph is written immediately above it. | low |
| 511 | Same display, above left object | Inserted uncertain `B` | Independent inspection found no unequivocal cancellation stroke; the upper glyph is retained as an uncertain insertion belonging to the source object. | low |
| 511 | Parenthesis below topoi map | `commute aux` | The compressed initial word is read by its visible outline; not every medial letter is resolved. | medium |
| 511 | Same parenthesis, after directed `lim` | `quelc.` | Possible longer abbreviation of *quelconques*; ending is compressed. | medium |
| 511 | Biset notation | Deleted illegible mark above first `Π` | Might be a cancelled prime or another superscript; no mathematical correction has been made. | low |
| 511 | « ce torseur définit … » | `lui aussi` | Two short words remain difficult; no reliable second reading. | low |
| 511 | Left margin, second line | `l'ens` | `l'un` visually possible, but the abbreviation is the preferred reading. | medium |
| 511 | Left margin, parenthesis and following word | Deleted illegible material, then `isom` | Heavily overwritten; neither original parenthetical expression nor its exact relationship to `isom` is secure. | low |
| 511 | Left margin, quoted cover phrase | `universel`, `ramification` | The letter groups are compressed and overlap the main text. Singular/plural endings are not secure. | low |
| 511 | Left margin, after « de cet » | `objet` | Final strokes partly coincide with a nearby correction. | medium |
| 511 | Left margin, before « ordinaire » | `sur` / `avec`, `rev. universel`; deleted `ramification` and one illegible word | Successive cancellations and line placement are hard to disentangle. | low |
| 511 | (8), weak horizontal arrowheads | `\unsure{\longrightarrow}` at the first link of the upper row and the lower row links | The horizontal strokes are clear; their arrowheads are weak or indistinct. They are marked doubtful instead of being inferred silently from exactness. | low |
| 511 | (8), over both `E` symbols | Deleted illegible superscript | May be cancelled hats; do not treat this as a resolved reading. | low |
| 511 | (8), subscript of first `Γ` | Deleted `Q` | Retraced and crossed through. | low |
| 511 | Last two lines, `U` symbols | `U`; first index `0,3` / `03` | Script versus plain capital, the first index comma, and a blackened following subscript are unclear. The second index appears to be `03`. | low |
| 512 | Left margin (9 bis), introductory verb | `s'insère` | Several medial letters are very compressed. | medium |
| 512 | Left margin (9 bis) | `idem` | The short abbreviation-like word is not fully resolved. | medium |
| 512 | Both marginal exact sequences and main quotient | `\mathfrak S_3` | The handwritten ornate S could also be represented as calligraphic S; the font/alphabet is uncertain. | medium |
| 512 | « modulo conjugaison… », and definition of `K` | Bare `Π'` retained | No hat has been silently supplied at these occurrences, although hats occur nearby. This is a notation observation, not an emendation. | high |
| 512 | Above « n'est pas triviale » | `(ni m̄ sur (Π'_{0,3})_{ab}^{*} …)` | Subscript `ab`, asterisk attachment, cancellation and closing punctuation are cramped; only the opening words are reasonably clear. | low |
| 512 | Same insertion, far right | Two deleted illegible units | Overwriting prevents recovery of the original expression. | low |
| 512 | Lower left asterisk note | `Z/2Z + Z/3Z` | Slash/subscript layout is compressed; retain doubt on the literal fraction-like notation. | medium |
| 512 | Final line, cancelled beginning | `Ce qui` | Possibly a different abbreviated start; crossed out. | low |
| 513 | First occurrence of `Π` | Prime | Prime is retraced into a dark vertical blot. | medium |
| 513 | Parenthetical identification of centre | `à` | The small mark could be read as punctuation. | medium |
| 513 | End of small parenthetical annotation after centre | `),` | Possibly only a comma; only one small curved mark is clearly resolved before « et ». | low |
| 513 | « et … pour » | `idem` | Compressed abbreviation-like writing. | medium |
| 513 | After second displayed-in-prose isomorphism | `isomorphisme` | `isomorphismes`; the ending is not securely legible. | medium |
| 513 | Before « deux générateurs » | `dans` | Short word is reduced to connected strokes. | medium |
| 513 | Inline names before (14) | `λ₃, λ₂` | Retraced letters and subscripts; the clear displayed relations are not used to suppress this local uncertainty. | medium |
| 513 | « ces … proviennent d'… » | `élts` | `élmts`; abbreviated middle letters are hard to distinguish. | medium |
| 514 | l. 3, after “En fait” | `tout` | Highly compressed final word; not reconstructed from the claim. | medium |
| 514 | l. 6 | `ss/groupes` | Possibly `s/groupes`; the numerator above the oblique stroke is cramped. | low |
| 514 | l. 6 | `engendrés` | The termination is compressed. | medium |
| 514 | l. 8 | `autom.` | The abbreviation's final strokes and punctuation are faint. | medium |
| 514 | l. 10, quotation | `anharmoniques` | Some medial letters are joined into a single stroke. | medium |
| 514 | l. 12, after “placer” | deleted unreadable item | Possibly a first attempt at a generator symbol; not securely recoverable. | low |
| 514 | l. 14, following the linear group | deleted `/±1` | The quotient suffix is heavily overwritten. | low |
| 514 | l. 14 | `mod` | The word is very cursive. | medium |
| 514 | l. 14 onward | opening parenthesis before `ce qui implique` | No definite corresponding closing parenthesis is visible before the following parenthetical sentence; none has been supplied. | medium |
| 514 | l. 16 | `au fait` | `enfin` remains possible. | low |
| 514 | ll. 17–18, struck out | `J'ajoute à (15) des relations fondamentales` | First word and the word beneath the inserted `(15)` are partly obscured; `(15)` is above the cancelled line. | low |
| 514 | equation (16), right-hand isolated mark | `\varepsilon` | Possibly a correction mark or an abandoned character; no missing equals sign has been supplied. | low |
| 514 | l. 20, after “c'est” | two deleted unreadable words | The deletion obscures the preceding phrase. | low |
| 514 | l. 20 | `justement` | The remaining adverb has a compressed ending. | medium |
| 514 | last line | `définira` | `définit` is possible. | low |
| 515 | after the bracket following (18), l. 5 | `où` | Only a very compressed initial trace survives; the reading is probable. | medium |
| 515 | l. 17, before the unnumbered arrow | `avec` | Short final word is reduced to joined strokes. | medium |
| 515 | unnumbered arrow in l. 18 | `\widehat{\Pi}_{0,3}` | Possibly no hat: the putative hat partly coincides with the descender of “définir” above. | low |
| 515 | cancelled number beside the penultimate display | `(21)` | Digit strokes are overwritten; the formula itself is not cancelled. | medium |
| 515 | penultimate text line | `relever` | Medial and final letters are highly cursive. | medium |
| 516 | l. 8 | `sous-groupe` | The hyphen is not secure; `sous groupe` may be the literal spacing. | medium |
| 516 | l. 8 | `engendré` | Terminal accent and ending are cursive. | medium |
| 516 | diagonal left margin, parenthetical condition | `Π_{g,ν−1} non ab.` | The group symbol/index overlaps writing above; the qualification's short strokes are compressed. | medium |
| 516 | diagonal left margin | `idem` | `item` is also compatible with the tall medial stroke. | low |
| 516 | equation-number deletion before (23) | unreadable cancelled item | Presumably an earlier numbering attempt, but digits cannot be recovered safely. | low |
| 516 | under the domain of (24) | `τ` | The character resembles a small `z`; its precise form is uncertain. | medium |
| 516 | annotation under (24) | `triangulé pointé` | `triangulaire` and `ponctué` remain alternatives respectively. | low |
| 516 | lower left margin | `pas encore défini` | The first two words are very cursive; no definite insertion pointer is visible. | medium |
| 516 | penultimate main-text line | `mb` | Likely the abbreviated word “membre”, but no expansion is made in the transcription and punctuation is unclear. | medium |
| 516 | last main-text word | `modulaire` | The final stroke could conceal a plural ending; syntax was not used to supply one. | medium |
| 517 | 3 | `mb` | `md`; the abbreviation after “deuxième” has a final upright hook. | low |
| 517 | Display (25), target superscript | `\illegible{1}` in superscript | A dark reworked small sign above the target `M`; it cannot be identified. No cancellation is asserted, because a similar sign may recur as notation on other scans. | low |
| 517 | Immediately after (25), canceled words | “Cela signifie aussi” | “Cela” is clear; the following canceled two words are tentatively “signifie aussi.” | medium |
| 517 | Before (26) | “bon cas” | First word has a tall initial and a long final stroke; “bon” is probable. | medium |
| 517 | After (26), “la donnée … une famille” | `de` | `d'`; an added apostrophe-like stroke overlaps the end of the preceding word. | low |
| 517 | Final paragraph, first line | `si` | The short word resembles an accented `à`; the reading “si” is tentative. | medium |
| 517 | Final paragraph, quotation marks | `“variable” ∈ U_{0,3}”` | Opening and closing quote strokes are uneven; the transcription retains the visible extra closing pair rather than silently balancing it. | low |
| 517 | Last line, between “de” and `P^1` | `\deleted{\illegible{1}}` | A canceled/reworked short mathematical or textual token is present; no safe letter reading. | low |
| 518 | 2, after “marqués” | `resp.` | Dense strokes overlap the initial letters; no separate cancellation is certain. | medium |
| 518 | 8, “quelconque S” | `\inserted{S}` | The `S` is visibly above the baseline and has been treated as an insertion at the preceding noun phrase. | high |
| 518 | 9, parenthetical characteristic condition | `ttes` | Probable abbreviation for “toutes”; exact arrangement/number of t-strokes is unclear. | low |
| 518 | Inserted category description, tuple | Deleted `,γ` | The third symbol after `β` is crossed out heavily; gamma is probable. | low |
| 518 | 10–11, after inserted “d'une” | `courbes` | `courbe`; the final short stroke does not settle number. | low |
| 518 | 10–11 | `elliptiques` | `elliptique`; the original plural context and added singular article were not reconciled. | low |
| 518 | 11, parentheses | `homogène` | `homogènes`; final stroke uncertain. | medium |
| 518 | 11 | `relative` | `relatives`; final stroke uncertain. | low |
| 518 | 11, canceled text before “sur S” | “avec” and one illegible word | Several diagonal cancellation strokes conceal the remainder. | low |
| 518 | 12, canceled word after “et” | `dont` | Letter outlines are compatible with “dont,” but cancellation obscures them. | low |
| 518 | 12, after `α,β` | Deleted `,γ` | Same difficult canceled third-symbol reading as in the inserted tuple. | low |
| 518 | 13–14, after `{}_2E` | `en tant` | Compressed words at the end of the line; followed by the readable “que schéma” on the next. | medium |
| 518 | 14, added property of the scheme | `loc. constant` | Insertion placed after “schéma” according to its curved leader. | high |
| 518 | 15, bracketed aside | `donnant` | The final letter is compressed into a crossing stroke. | medium |
| 518 | 17, punctuation after `(β,γ)` | comma | Full stop; the stroke is very small. | low |
| 518 | 17, canceled ordered pair | `(γ,α)` | Both letters are crossed through; their order is uncertain. | low |
| 518 | 20, before “distinctes” | `marquées` | The initial and ending strokes are compressed; all letters are not independently distinct. | medium |
| 518 | 22, after `E/±1` | `muni` | The first letter is heavily retraced; capitalization is uncertain. | medium |
| 518 | Left margin, first line | `=` | Possibly the author's “same” abbreviation `m̄`; the two strokes look straight. | low |
| 518 | Left margin, after `α,β,γ` | `sont` | Highly compressed linking word. | low |
| 518 | Left margin, after “trois” | `sections` | Some internal letters cannot be separated. | low |
| 518 | Left margin, after “qui” | `sont` | Short ending at the edge of the note overlaps main-body lettering. | low |
| 518 | Left margin, canceled word | `partout` | Heavy horizontal deletion hides the middle of this tentative word. | low |
| 518 | Left margin, final line | `partout` | Compressed word; the ending is not distinct. | low |
| 518 | Left margin, final symbol | `≠1` | The terminal character has the visible form of `1`; it has not been changed to `0` to suit additive notation. | medium |
| 519 | Upper left margin, after “compliquées” | `avec` | The short connector is compressed; no secure alternative. | medium |
| 519 | Upper left margin, after the two primed objects | `etc.` | Exact punctuation and letters are faint. | medium |
| 519 | Left margin, after “aller” | `bonnement` | `hardiment`; neither candidate is sufficiently secure. | low |
| 519 | Left margin, displayed family equation | `y^2=\sqrt{x(x-1)(x-\lambda)}` | The visible superscript resembles 2 and a separate radical is visible. The simultaneous square and radical have deliberately not been mathematically repaired. | high |
| 519 | Lower part of left margin, after `U_{0,3}` | `pour … avoir` | One short word is unreadable; the remaining two readings are themselves uncertain. The map to `M_{1,1}` is clearer than the connecting prose. | low |
| 519 | Main l. 5, after “opère” | `trivialement` | The ending is compressed and may be abbreviated. | medium |
| 519 | Main l. 6, “Donc il … prendre” | `faut` | The long horizontal stroke may be part of the letter formation; it has not been classified as a deletion. | medium |
| 519 | Main l. 7, before the cancelled phrase | `la` | `le`; the following “catégorie fibrée” is crossed out and replaced above the line by “champ”. | low |
| 519 | Main l. 8, after “elliptiques en” | `convenant` | Several interior letters are compressed. | medium |
| 519 | Main l. 9, both `Isom` symbols | `\mathrm{Isom}` | The initial letter is heavily retraced; its exact alphabet or possible underlining is not securely recoverable. | medium |
| 519 | Main l. 13, beginning of “champ est représentable” | `Cet` | `Ce`; the apparent final stroke may be a t. | low |
| 519 | Main l. 15, cancelled words before “ayant” | `déduit de …` | Last short item illegible; the first two words are also marked uncertain. | low |
| 519 | Moduli symbols, especially (27) | `M` / `\mathbb M` | Doubled or looped left stems and retracing prevent a secure alphabet choice. The uncertainty is retained at each moduli-symbol occurrence on this page. | medium |
| 519 | Main ll. 19–24 and (27), repeated level variable | `m` | `n`; handwritten wave alone does not securely distinguish them. | medium |
| 519 | Main l. 22, immediately after (27) | `note` | `voit`. | low |
| 519 | Main l. 22, inserted central subgroup | `(\pm1)` | `\{\pm1\}`; the enclosing signs are uncertain. | medium |
| 519 | Main l. 22, after “opère” | `trivialement` | The terminal strokes do not securely distinguish the full word from an abbreviation. | medium |
| 519 | Main l. 24, after the primed `Sl` quotient symbol | `\illegible{1}` | Small looped or overwritten glyph before the equality; not silently discarded or classified as a deletion. | low |
| 520 | Moduli symbols, especially (28)–(30) | `M` / `\mathbb M` | Pronounced feet and additional stem traces may be deliberate blackboard lettering or pen retracing; no confident normalization is made. | medium |
| 520 | (28) and first two prose lines, level variable | `m` | `n`; repeated at the level bracket, residue ring, “choix de”, and inequality. | medium |
| 520 | First prose line | `(ce` | `Ce`; the closing parenthesis is visible on the next line, but the opening stroke is ambiguous. | low |
| 520 | First prose line, after “qui” | `manifest` with a raised `t` | Full `manifestement`; compressed ending may be an abbreviation. | low |
| 520 | After (29), and label below (30) | `\mathfrak{S}_3` | Highly cursive initial; letter/alphabet identified tentatively. | medium |
| 520 | (30), after the first prime and before `[2]` | `\illegible{1}` in the raised position | Dark short sign; cannot establish whether intentional notation or pen correction. | low |
| 520 | (30), immediately after target `M'_{11}` | `\illegible{1}` | Looped sign, similar to a mark near the earlier moduli target; no confident identification. | low |
| 520 | Prose after (30), first word of next row | `étant` | Compressed ending and accent. | medium |
| 520 | Canonical map following (30), at the lower right of `Sl(2,Z)` | `\illegible{1}` in a lower position | Small looped glyph under the completion sign; not treated as a cancellation. | low |
| 520 | Last prose line before (31) | `hom` | `homom.`; exact abbreviation and punctuation are not secure. | low |
| 520 | Above and left of (31), cancelled label | `(\illegible{1})` | Apparently an earlier equation label; its digits cannot be confidently recovered. | low |
| 520 | (31), annotation above `\widehat\Pi_{0,3}` | `\mathcal{T}_{0,4}^{!+}` | A hat may be present, but nearby strokes from the preceding prose interfere. | low |
| 520 | (31), annotation above `\mathcal E_{0,3}` | `N_{0,4}` | `\mathcal N_{0,4}`; letter is legible but its alphabet is uncertain. | medium |
| 520 | (31), annotation below the lower geometric group | `\{\pm1\}` | `(\pm1)`; enclosing signs uncertain. The vertical isomorphism mark is typeset as the corresponding `\simeq` relation. | medium |

## 3. Abbreviations met

The expansions in this table are editorial hypotheses only. They have not replaced the abbreviated forms in the transcription. Alternative spellings or punctuation in the first column reflect different occurrences or an explicitly uncertain reading.

| Form as written | Probable expansion or function | Scan(s) / qualification |
|---|---|---|
| `rev` with raised `ts` | revêtements | 511; raised letters uncertain |
| `pts`, `pt` | points, point | 511, 518 |
| `Ens` | ensembles | 511 |
| `quelc.` | quelconques | 511; exact ending/punctuation uncertain |
| `g.` | gauche | 511, in « exact à g. » |
| `ens.`, `ens` | ensemble | 511; marginal `l'ens` uncertain |
| `hom`, `homom.` | homomorphisme | 511, 515–516, 520; punctuation and longer form sometimes uncertain |
| `isom`, `isom.` | isomorphisme(s) | 511, 513 |
| `iso` | isomorphisme | 513, labels of arrows |
| `rev.` | revêtement | 511, 517, 519–520 |
| `géom.` | géométrique(s) | 511, 519–520 |
| `resp.` | respectivement | 511, 514, 518 |
| `autom.` | automorphisme(s) | 512, 514, 519 |
| `int.` | intérieur | 512 |
| `ext.` | extérieure; extension | 512 (opération); 516 (group extensions) |
| `th.` | théorème | 512 |
| `§` | paragraphe / section | 512 |
| `m̄` | même | 512–513, 515; possible instance in the margin of 518 |
| `op. ex.` | opération extérieure | 512 |
| `ab` | abélianisé / abélianisation | 512; the subscript is unresolved |
| `Autext` | automorphismes extérieurs | 513 |
| `Cent` | centre | 513 |
| `ss-groupe`, `ss/groupes` | sous-groupe, sous-groupes | 513–514, 519; slash/numerator uncertain on 514 |
| `élts` / `élmts` | éléments | 513; exact contracted spelling uncertain |
| `car.` | caractéristique(s) | 514, 518 |
| `mod` | modulo | 514; reading uncertain |
| `non ab.` | non abélien | 516; qualification uncertain |
| `mb` / `md` | membre | 516–517; final letter and punctuation uncertain |
| `inv` | inversible | 518 |
| `résid.` | résiduelle(s) | 518 |
| `ttes` | toutes | 518; contracted letters uncertain |
| `cat` | catégorie | 518 |
| `syst` | systèmes | 518 |
| `loc.` | localement | 518 |
| `etc`, `etc.` | et cetera | 518–519; the marginal occurrence on 519 is uncertain |
| `p.ex.` | par exemple | 519 |
| `cf` | confer / compare | 519, margin |
| `manifest` with raised `t` | manifestement | 520; abbreviated ending uncertain |
| `Sl`, `Gl` | groupe spécial linéaire, groupe général linéaire | 513–516, 519–520; letter case preserved |
| `Sch` | schémas | 519; notation for the base category |
| `Isom` | isomorphismes | 519; precise alphabet and possible sheaf notation unresolved |

## 4. Legibility assessment

The main prose and the larger numbered formulas are generally much more legible than the small annotations. The weakest continuous passages are the diagonal notes on scans 511, 518, and 519. The retraced source glyph in the first topos map, the blackened superscripts in (8), the final insertion on scan 512, the revisions around (16), and the annotations below (24) require particular caution. On scans 517 and 520, several small recurring signs beside moduli symbols remain unidentified; they have not automatically been classified as cancellations.

Abbreviations, singular/plural endings, index commas, hats, primes, and tiny punctuation are the main sources of residual uncertainty. Independent readings were reconciled for the first three scans, including occurrence-by-occurrence checks of the index commas. The compressed level letter on scans 519–520 remains `m` or `n`. The fragment preserves the apparent combination of a square on the left and a radical on the right in scan 519's marginal equation; that is a reading of the page, not validation of the equation.

The uncertainty marks are part of the transcription and should remain attached to quotations taken from it. Illegible deletion counts are estimates, and the most heavily overwritten passages cannot be claimed as completely recovered. The clear parts of a displayed formula should not be used to promote its doubtful marks to certainty.

## 5. Research notes — English

These items record the author's expressed expectations, assertions whose proofs are not supplied here, consequences worth checking, and explicitly labelled proposals by the transcriber. They are not a literature review or a claim that an issue remained unresolved later. Each heading is a locator for the primary-source citation, Grothendieck (1981); a brief quotation identifies the relevant wording. An **own idea** is a proposed investigation with its confidence and reason, not an asserted result or a claim of novelty.

### R01 — Scan 511, (7 bis) and following paragraph — unproved claim

« a les propriétés d'exactitude » and « est donc défini par un … ens. » assert the passage from a functor between categories of group actions to a right torsor with a second group action. A proof should specify the precise ramification-bounded covering categories, verify the exactness conditions, and establish the claimed torsor property; these details are not supplied on this page.

### R02 — Scan 511, middle paragraph — unpursued implication

« Le choix d'une origine pour ce torseur » points to a dependence on an auxiliary choice when the homomorphism is extracted. It is worth tracking explicitly how changing that origin changes the homomorphism and how this relates to the inner-conjugacy ambiguity stated on scan 512; this is a question about the manuscript's construction, not a correction to its text.

### R03 — Scan 512, (9) — unproved claim

« Les raisonnements précédents s'étendent à ce cadre » (beginning on scan 511) asserts an arithmetic version yielding a morphism of extensions. A proof would need to construct the functor over the base field and check both the maps on geometric kernels and the identity on the arithmetic quotient, including the stated ambiguity « modulo conjugaison ».

### R04 — Scan 512, definition of `K` through « lui-m̄ est fini » — unproved claim

« On voit alors que … se fait par un groupe fini » is the key reduction before invoking « le th. 1 du § précédent ». To assess the argument, one needs the preceding theorem's actual hypotheses and a proof that the restricted outer action factors through the displayed finite quotient; the present extract does not include that theorem.

### R05 — Scan 512, last paragraph — unproved claim

« Donc par Artin » and « comme χ(τ) = −1 » condense two external ingredients in the proof of triviality of the kernel. A reconstruction should identify the precise Artin result being invoked, explain its applicability to `K`, and verify the induced action on the indicated quotient or abelianization without relying on the uncertain final insertion.

### R06 — Scan 513, opening paragraph — conjecture / expectation

« J'ai envie maintenant d'interpréter » announces the intended identification with a central quotient and asks that it be « compatible à l'action extérieure de Γ ». The discrete identifications below it do not themselves supply this arithmetic compatibility; scans 515–520 should be read as attempts to construct the comparison geometrically.

### R07 — Scan 513, (10)–(13) — unproved claim

« pour mémoire » introduces isomorphisms obtained by « bouchage du trou » and the action on the fundamental group, followed by the description of the centre. A proof must fix the exact marking and orientation conventions of the Teichmüller groups, since those conventions determine the filling map and the distinction between the two linear groups.

### R08 — Scan 513, (14)–(15) — unproved claim

« Il est connu » states a presentation by elements of orders three and two, while « Sauf erreur » expressly qualifies their lifting to elements of orders six and four. One should verify the lifts, their exact orders, and the common central element; the next page discusses the additional relation rather than giving explicit matrices here.

### R09 — Scan 514, ll. 3–7 — unproved claim

An “élément d'ordre fini” is said to be conjugate to a power of one of the two displayed generators. A proof would have to classify finite-order elements of the written integral linear group and state precisely the roles of conjugacy and inversion; those qualifications occur just above the claim.

### R10 — Scan 514, ll. 8–10 — unproved claim

The cyclic subgroups of orders 4 and 6 are identified with the automorphism groups of the “deux courbes elliptiques exceptionnelles” in characteristic zero (the abbreviation read as `autom.` is uncertain). A verification would require identifying the curves and explaining which point or origin their automorphisms preserve; neither identification is supplied on this page.

### R11 — Scan 514, ll. 11–17 — conjecture / expressed doubt

The author says that he has no formula to “placer” the generators and adds “sans doute” about generation of the full group from generation modulo its centre. He immediately warns about “la relation supplémentaire”, so the uncertainty and subsequent relation should be studied together rather than treating the tentative implication as an unqualified assertion.

### R12 — Scan 514, equation (16) — own idea (high confidence as a verification plan, not as a historical or novelty claim)

Check the tentative lifting argument directly from the displayed relation `u_4^2=u_6^3` and the next line's identification with the central element `-1`. The reason for confidence in this plan is that the manuscript itself singles out precisely the central element that the argument would need to recover.

### R13 — Scan 515, ll. 12–16 / equation (20) — conjecture / expectation

“Je veux maintenant me convaincre” introduces the desired compatibility of the completed homomorphism with the outer action of `Γ=Π_Q`. This is stated as a goal here; a verification would have to specify how the two outer actions are compared, including their indeterminacy by inner automorphisms.

### R14 — Scan 515, ll. 17–21 / equation (21) — conjecture / expectation

“J'ai envie de définir directement” and “et m̄ de le relever” describe a proposed direct construction and a lift from the quotient by `±1` to the full completed group. The page does not yet establish that this stronger construction respects the indicated arithmetic action.

### R15 — Scan 515, equations (19)–(21) — own idea (medium confidence as a research plan)

Separate the existence of a lift across the central quotient by `±1` from compatibility of that lift with the outer arithmetic action. The reason to try this separation is the author's explicit move from the quotient in (20) to the larger target in (21); it may expose an obstruction that would be hidden by checking the displayed generator relations alone.

### R16 — Scan 516, equation (22) and following relators — unproved claim

The target “s'identifie au quotient” by the invariant subgroup generated by the three displayed relators. A proof would have to show that these relators give the whole kernel, not merely that their images are trivial; the page records the assertion without a separate proof.

### R17 — Scan 516, ll. 11–13 and diagonal margin — unproved claim

“Peut s'interpréter comme un groupe de Teichmüller” is supported by a short extension statement in the margin and the equality `T^{!+}_{0,3}=(1)`. Checking the assertion requires fixing exactly what the `!` and `+` decorations mean and verifying the exceptional cases covered by the partly uncertain “non ab.” condition.

### R18 — Scan 516, between (23) and (24) — conjecture

“Dont je soupçonne qu'il se prolonge en un hom” explicitly proposes an extension from the groups decorated by `+` to the groups displayed in (24). A proof would need to specify the image of the extra coset and verify the relations connecting it to the subgroup in (23).

### R19 — Scan 516, annotation below (24) — unproved claim

The domain is described as an “ext. de {1,τ} par Π_{0,3}” and identified with a “groupe cartographique” bearing two uncertain adjectives. The extension structure and the cartographic interpretation merit independent verification; the adjacent marginal “pas encore défini” has an uncertain attachment and should not be assigned a more precise referent without further manuscript evidence.

### R20 — Scan 516, final two lines — unpursued implication

“J'interprète le premier mb de (23)” as the “Π_1 ‘géométrique transcendant’ du topos modulaire” shifts the proposed group map toward a moduli-theoretic construction. The sentence continues on the following scan, so its interpretation should be checked together with that continuation before concluding which moduli object is intended.

### R21 — Scan 516, equation (24) — own idea (medium confidence as a verification plan)

Given a candidate image for the nontrivial element of the displayed two-element quotient, calculate its conjugation action on the two chosen generators and compare it with the domain extension. This is a concrete test of the stated expectation; confidence is only medium because the page does not completely spell out the extension action or fix the generator matrices.

### R22 — Scan 517, lines 6–10 and (25) — kind: conjecture (expressed expectation)

Grothendieck writes “On devrait donc pouvoir définir …” a morphism of modular multiplicities over `Q` that “donnerait naissance à (23).” The open task at this point is to give a geometric construction and then verify that its induced map is the previously written homomorphism, including the treatment of stabilizers. The heavily overwritten superscript of the target in (25) prevents a confident statement here about the precise version of the target.

### R23 — Scan 517, (26) and following paragraph — kind: unproved claim

The asserted identification `M_{0,4}^{!} ≃ U_{0,3}` turns the requested datum into “une famille de courbes elliptiques sur U_{0,3}.” A proof at the stated moduli level would need to track the ordering of all four marked points and the descent of the normalization of three of them; identifying point sets alone would not settle the assertion for families.

### R24 — Scan 518, lines 1–6, continuing scan 517 — kind: unproved claim

The branched quadratic covering is said to give “une courbe elliptique,” with the point over `0` chosen as origin and the other points becoming “les trois points d'ordre 2.” A verification would need to establish smoothness and genus one for the covering and identify its covering involution with inversion relative to that origin. The choice of origin and the order of the branch labels should be checked explicitly against the notation used later.

### R25 — Scan 518, lines 7–15 — kind: unproved claim

The construction is extended to a base scheme with `2` invertible and to systems `(E,α,β)` in which the sections form a basis of `{}_2E`. One should verify that the construction and basis condition are preserved by base change, and explain the local constancy property inserted into the text. The manuscript's many revisions in this sentence make the intended source category a point requiring special care in any reconstruction.

### R26 — Scan 518, lines 15–18 — kind: unpursued implication

The third section `γ=α+β` appears “comme un troisième larron,” with other ordered pairs asserted to be bases as well. This suggests comparing the permutations of the three nonzero sections with permutations of the corresponding three nonzero branch labels, keeping the origin separate. The damaged canceled ordered pair should not be used as evidence for a particular permutation formula.

### R27 — Scan 518, lines 19–23 — kind: unproved claim

The functor is described by “en associant à E le quotient E/±1,” equipped with the four image sections. A proof would need to show that this quotient is a relative projective line in the intended sense and that the four image sections remain pairwise disjoint over every base point. It would also have to specify the behavior on isomorphisms, which is not worked out in these lines.

### R28 — Scan 518, quotient construction — kind: own idea. Confidence: medium; reason: the displayed quotient forgets a visible involution, but the precise categorical conventions are not settled by this page alone

Test the construction on an elliptic curve with a chosen basis of its 2-torsion and compare its automorphisms with those of the marked quotient projective line. This is a concrete way to locate any loss of faithfulness before trying to prove that the construction is an equivalence; it is a proposed check, not a claim of novelty or an established result in these notes.

### R29 — Scan 519, left margin — Unproved claim / proposed simplification

“Les pages qui suivent sont inutilement compliquées” introduces a proposed simplification using a directly specified elliptic family over `U_{0,3}` and a map to `M_{1,1}`. The readable phrase “il suffit d'y aller” and the final “cf plus bas” leave the construction and its comparison with the primed moduli objects to be checked elsewhere. A proof would have to identify the resulting morphism and compare its induced geometric and arithmetic fundamental-group maps; the marginal equation itself first requires independent confirmation of its transcription.

### R30 — Scan 519, main ll. 1–13 — Unproved claim

The functor is described as “presque une équivalence”, with the elliptic involution acting trivially on the quotient object, and the proposed repair replaces isomorphisms by their quotient under `±1` before passing to an associated champ. A proof would need full faithfulness after that quotient, local essential surjectivity, and effective descent for the resulting objects. The manuscript's passage from the crossed-out “catégorie fibrée” to the inserted “champ” makes the descent step a substantive part of the construction.

### R31 — Scan 519, main ll. 13–21, (27) — Unproved claim

The resulting champ is said to be “représentable par une multiplicité modulaire”, with the displayed completed modular group modulo `±1` as geometric fundamental group. The finite-level presentation in (27) points toward a proof but does not supply compatibility between the level presentations or the fundamental-group calculation on this page. Those comparisons would need to preserve the distinction between a quotient presentation and an ordinary quotient space.

### R32 — Scan 519, main ll. 22–25 — Unproved claim

The insertion “le ss-groupe central” modifies the assertion that `±1` “opère” trivially on the level-moduli object. Verification requires the exact moduli functor and the meaning of the group action, including whether equality means equality of marked objects or equality of their isomorphism classes. This is the step used to replace the finite linear group by its primed quotient.

### R33 — Scan 520, immediately after (28) — Unproved claim

The presentation is said to “ne dépend pas du choix” of the level, in the written range with lower bound 2. A proof would require compatible comparison morphisms between presentations at different levels and a check of the endpoint of that range. The compressed adverb preceding this assertion is uncertain in the transcription; the independence assertion itself is legible.

### R34 — Scan 520, (29)–(30) — Unproved claim

The morphism from the four-pointed genus-zero moduli object is asserted to be “un rev. galoisien” with the indicated three-letter permutation group, more precisely the level-2 object over `M'_{11}`. A proof would need to recover the relevant level-2 data from the labelled branch points, account for automorphisms, and identify the full deck group with the displayed finite linear group. The additional small signs attached to the moduli notation remain palaeographically unresolved.

### R35 — Scan 520, paragraph following (30) — Unproved claim

The geometric fundamental group of the level-2 object is described as “isomorphe au noyau” of the displayed reduction map. A proof would need the connectedness of the finite cover and the compatibility of its geometric fundamental group with the profinite topology on the corresponding finite-index subgroup. Keeping the central quotient and completion operations explicit is necessary to justify the stated factorization.

### R36 — Scan 520, (31) — Unpursued implication

The “suites exactes” diagram supplies a possible route to the compatibility of the geometric map with the outer Galois actions. These pages end with the diagram, without an explicit base-point comparison or a statement of the ambiguity under inner conjugation. Recording those choices would be needed before using the diagram to identify a particular earlier group homomorphism.

### R37 — Scans 519–520, central quotient and (29)–(30) — Own idea

Compare the inertia groups before and after quotienting the elliptic involution, especially at elliptic objects with additional automorphisms, before interpreting the morphism as a cover of ordinary spaces. **Confidence: medium**, because the manuscript explicitly removes a central involution and then presents a nontrivial finite Galois cover; the proposed local check is motivated by those two operations, but its outcome is not asserted here. This is a suggested verification, not an established conclusion or a claim of novelty.

### R38 — Scan 520, (29)–(31), compared with (17), (22), and (23) in the supplied earlier scans — Own idea

Compute the index of the image of the geometric fundamental-group map associated with the asserted finite cover and compare it with the earlier generator-defined map. **Confidence: medium**, because the cover and finite group in (30) make an index test concrete, while identifying the two maps requires choices and comparisons not made on this page. A mismatch would be evidence to distinguish the constructions, not grounds to alter the manuscript or declare a contradiction without further investigation.

## Reference

Grothendieck, A. (1981). *La Longue Marche à travers la théorie de Galois* [Handwritten manuscript, cote 140-2, supplied scans 511–520; visible author numbers 261–265]. Université de Montpellier.

The title, date, and archive designation above are taken from `LM_P052_prompt.md`; the text itself was read from the ten supplied contrast-enhanced JPGs. The archive footer numbers correspond to 510–519, as shown in the coverage table. No bibliographic reconstruction has been inserted into the LaTeX fragment.

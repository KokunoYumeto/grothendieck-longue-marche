# LM_P029 — Editorial apparatus and research notes

## 1. Scope, sources, and notation

The accompanying `LM_P029_transcription.tex` is a diplomatic LaTeX fragment for the ten supplied image files. It contains no preamble, document class, macro definitions, translation, or reconstructed continuation. Readings come from the supplied scans and enlarged inspection crops, with a second comparison against the images; no published transcription or external reconstruction was used. The source title, date, and archive identifier follow the attached task brief (Grothendieck, 1981).

The scan filenames and the printed archive footers differ by one. `\scanpage{…}` follows the filenames, as requested. `\mspage{…}` records only the distinct authorial foliation visible at the top; the archival page figures and institutional imprint are not treated as part of the manuscript prose.

| Scan / filename suffix | Archive footer | Authorial page number visible at top |
|---|---:|---:|
| 281 | 280 | — |
| 282 | 281 | 142 |
| 283 | 282 | — |
| 284 | 283 | 143 |
| 285 | 284 | — |
| 286 | 285 | 144 |
| 287 | 286 | — |
| 288 | 287 | 145 |
| 289 | 288 | — |
| 290 | 289 | 146 |

Approximate line references below identify the main handwritten rows, with headings, insertions, displays, and marginalia identified separately. They are finding aids rather than a claim to exact lineation. A high/medium/low confidence label concerns the reading of the ink, never the mathematical validity of the statement. The number in `\illegible{n}` estimates the unread words; an unread mathematical item is counted as one item where word counting is inapplicable.

Short terminal strokes, alphabets, prime placement, punctuation, and the scope of corrections remain doubtful at the places indicated. The symbols `S^!`, `S^{\prime!}`, and `I^{\prime!}` follow visible detached dots rather than being normalized to double primes. Apparent discrepancies such as unprimed `V`, `I'` in place of `I^{\prime!}`, and the unrepaired wording “Elle n'est … prouvée” are preserved. The underlined mathematical group notation is retained with `\underline`; underlined prose uses the requested `\uline` or `\uuline`.

Line endings within paragraphs are not reproduced mechanically. Words divided only by a line break have been joined, including `indépendamment` and `centralisateur`; no abbreviation is expanded in the transcription. The fragment uses the requested editorial macros and ordinary LaTeX mathematical notation, plus `tikz-cd` for clear diagrams. The diagrams use `ampersand replacement=\&` to remain usable inside `\diagram{…}`, and a rotated comparison sign uses the standard `graphicx` command `\rotatebox`. Macro definitions and a temporary compilation wrapper are intentionally not included in the deliverable.

## 2. Table of doubts

The tables are grouped by scan. Several repeated occurrences of the same unresolved symbol are grouped in one row; the doubt marks remain at the individual occurrences in the transcription.


### scans 281–283

| Scan | Approximate line / location | Reading retained | Alternative or unresolved point | Confidence |
|---|---|---|---|---|
| 281 | 1 | Je présume | Opening overlaps the diagonal marginal note; the first two words remain uncertain. | medium |
| 281 | 2 | où on ne | Short strokes partly overlap the margin; one or more words may differ. | low |
| 281 | 3–4, 16–17 | Superscript u after 0 in A | n; the ink is not transcribed as Γ merely because the marginal revision uses Γ. All four occurrences are marked. | low |
| 281 | Upper-left margin, formula | Subscript 1 on the second Π | A heavy retracing obscures the subscript; the right-hand expression appears to be Π₁(A⁰)^Γ. | medium |
| 281 | Upper-left margin | reprendre | The compressed middle letters are uncertain. | medium |
| 281 | Upper-left margin, ending | feuille intercalée | Both words are partly crowded against the main text. | medium |
| 281 | 6 | homotopisme | The middle consonants are compressed; no substitution of a more familiar mathematical term is intended. | medium |
| 281 | 6 | cela | Possibly a shorter word; the final letters are a stroke. | low |
| 281 | 7–8 | ∞-équivalence | The word is divided between lines and the last part is very compressed. | medium |
| 281 | 10–11 | en me limitant au besoin au cas | The word limitant is divided across the line boundary; its last letters remain doubtful. The surrounding short words became readable on an independent enlarged-image check. | medium |
| 281 | 11 | inserted combinatoire; (cas | The insertion connector is not transcribed as textual parentheses; the apparent opening parenthesis before the repeated cas is uncertain. | low |
| 281 | 12 | Closing brace-like sign after fait ! | It could be a parenthesis or a revision mark; it has not been silently discarded. | low |
| 281 | 12 | Deleted plus; inserted reste; touffu | Alternatives restes and touffus; the overwritten word and singular/plural endings are uncertain. | low |
| 282 | Heading, preposition | de | des; the terminal stroke does not clearly distinguish them. The section number 24 appears double-underlined. | medium |
| 282 | Heading, formula | ν+n−1 | ν+u−1; the short ascending stroke does not settle the letter. | medium |
| 282 | 1, after fidèle | si on y tient | The middle words and final consonant are compressed. | medium |
| 282 | 2–3 | U in U⊂X=Û and Aut(U) | Both U glyphs are heavily retraced or overwritten; no precise recoverable original is asserted. | medium |
| 282 | 4 | A^u=A^Γ | A^n=A^Γ; the first exponent remains uncertain. | low |
| 282 | 6, cancelled line | transforme U en lui m̄ | The old object is overwritten, but may be U; the verb and object remain tentative. | low |
| 282 | 6, inserted line | autom.; X/Γ≡X′ | The abbreviation ending and the relation sign (≡ or ≃) are uncertain. | medium |
| 282 | 7, cancellation | étant | Short heavily crossed word before X. | low |
| 282 | 13, cancellation | tel que | Could be another two-word connective; retained with doubt. | low |
| 282 | 14–15, revision | sur lequel (deleted); L'image / inverse (inserted) | Two additional crossed words cannot be recovered; insertion ordering follows the nearby replacement words. | low |
| 282 | 15 and 17, below V′ | A solid dot below each of the two V′ labels | Dots are visibly present; whether they belong to the notation, to punctuation or to another annotation is unclear. Their approximate position is retained with `\underset`. | low |
| 282 | 18 | V^Γ | V with a corrected or retraced upper stroke; the extra mark is not silently removed. | low |
| 282 | 20 | One unread cancelled word before Γ-rev. | Cancellation is too dense for a reading. | low |
| 282 | 20 | au dess. d'un | Possibly a less abbreviated phrase; final words join scan283's “isom de V′”. | low |
| 283 | 5 | avec la | The beginning of this line is obscured by the diagonal note. | low |
| 283 | 8 | à lacets | de lacets; the preposition is overwritten. | low |
| 283 | 10, 13–14 | Fraktur g for the exterior automorphism | Barred g; the transverse stroke and the alphabet cannot be securely distinguished. | low |
| 283 | Left margin, end | Two unread words after pour expliciter | The text overlaps the main line; no completion has been supplied. | low |
| 283 | 14, deletion | f comme g | The last crossed symbol is uncertain. | medium |
| 283 | 15, deletion | soit | et; the overwritten first strokes do not settle the word. | low |
| 283 | 16, deletion | Two unread words after dégénérés | No secure reading through the strike. | low |


### scans 284–286

| Scan | Approx. line / location | Reading in transcription | Alternatives / difficulty | Confidence |
|---|---|---|---|---|
| 284 | 2, cancelled adjective | `orientable`, replaced by `admissible` | Original word is crossed through; its middle letters are obscured. | medium |
| 284 | 4 | `sous-ens.` | The first abbreviated component is a compressed horizontal trace. | medium |
| 284 | 5, fundamental-group formula | `\Pi_1(X',x')` | `V'` remains an alternative. The visible letter looks like `X'`; no correction to a punctured-surface formula has been made. | medium |
| 284 | 6, insertion | `nommé V` | First word is heavily contracted. | medium |
| 284 | 7 | `ponctué` | `pointé` cannot be excluded from the short middle strokes. | medium |
| 284 | 10 | `V' ramifié` | `V` if the apparent prime is incidental. | medium |
| 284 | 11 | `groupe lacet` | Singular/plural ending and possible hyphen are not fully resolved. | medium |
| 284 | 11, before `L_{s'}` | Cancelled illegible item, one estimated word/symbol | Overwriting prevents a secure reading. | low |
| 284 | 13 | `l'ens` | `l'espace`; the compressed noun is unresolved. | low |
| 284 | 13, cancelled item | `par` | Could be another short false start. | low |
| 284 | 15 | `de V` | Possible faint prime, hence `de V'`. | medium |
| 284 | 17, pullback formula | `g^*(V'/V) ≃ V'` | Prime placement and the numerator/denominator order remain uncertain. The expression has not been replaced by what the mathematics might suggest. | low |
| 284 | 17, insertion over isomorphism | `V-isom` | Possible `V'-isom`; terminal punctuation is unclear. | medium |
| 284 | left margin alongside 16–19 | `Sps que` | Abbreviation for a supposition appears contracted; initial letters uncertain. | low |
| 284 | 20, insertion | `élément de` | Possible final `du`. | medium |
| 284 | 20, centre notation | `z (= Centre Γ)` | `ζ`; a capital `Z` was also considered, but is less secure visually. Relation could be `∈`. | low |
| 284 | 21 | `rev. ramifié` | First abbreviation is overwritten. | low |
| 284 | 22, insertion and cancellation | `On veut` plus one cancelled illegible word | `On voudrait` possible; the cancelled original is not recoverable. | low |
| 284 | 22, cancelled phrase | `g provient par un` | Middle wording lies under a long cancellation stroke. | low |
| 284 | 23 | `néc.` | `nécess.`; the abbreviation is short and contracted. | medium |
| 284 | 24 | `isot.` | Final abbreviation point unclear. | medium |


### scan 285

| Scan | Approx. line / location | Reading in transcription | Alternatives / difficulty | Confidence |
|---|---|---|---|---|
| 285 | 2, before inserted `sont` | One cancelled illegible word | Possibly a verb such as `induisent`, but no secure reading. | low |
| 285 | 4, `Aut(V)` and associated insertion | `V` | An underlying letter is overwritten; original may have been `U`. | medium |
| 285 | 4, cancelled phrase | `ou Aut(U)` | Cancellation crosses the abbreviation and relation to the preceding group. | low |
| 285 | 4, inserted group | `Aut(V)^0_Γ` | The lower Γ-like mark may instead belong to a correction mark or another positioning of Γ. | low |
| 285 | insertion below l. 4 / above l. 5 | `lorsque Aut(V')^0 est 1-connexe` | Words are legible; attachment to the following lifting assertion is inferred from the large insertion brace and may be misplaced. | medium |
| 285 | 6 | `principes généraux` | Last adjective is contracted, with a long stroke before its final x. | medium |
| 285 | 7, before lifting display | Two cancelled `Aut` fragments | Both are overwritten false starts; the first could be another A-shaped expression. | low |
| 285 | 11, first displayed factor | Cancelled `0` before Γ in `Aut(U)^Γ` | A black blob occupies the position of a superscript 0; its cancellation state is uncertain. | low |
| 285 | 12 | `S^! (=U^! avec une notation antérieure)` | `avec` is contracted; exclamation marks are supported by detached dots. | medium |
| 285 | 13, cancelled formula after B | `⊂ Aut(U)^0` | Relation and the beginning of the formula are overwritten. | low |
| 285 | 13, inserted formula | `⊂ Aut(U)^0 ∩ Aut(U,S^!)_=` | Overwritten argument may be `V`; terminal subscript looks like `=` but might be `ε`. | low |
| 285 | 14 | `qui` | Only a short trace follows q; `que` cannot be entirely excluded. | medium |
| 285 | 19, inserted end of sentence | `on` | A small dot plus short terminal stroke; could be an unfinished transition. | low |
| 285 | 20–22, cancelled argument | `B^{0Γ} ⊂ Aut(U)^{0Γ} = B^Γ`; vertical `≃` to `Aut(V')^0`; `donc`; `connexe`; two illegible words | Final relation may be inclusion rather than equality; vertical sign may be equality; two cancelled words after `et` cannot be secured. The diagram description preserves the surviving spatial evidence. | low |
| 285 | bottom exact-sequence diagram | `B^{0Γ^0}` | An extra small circle is visibly present above/right of Γ; its grouping is uncertain. It is retained rather than omitted. The two lower comparison signs are drawn vertically (wavy left stroke, straighter right stroke), so the diagram rotates the comparison symbol. The relation below H¹ is vertical equality with a question mark at its right. | low |
| 285 | right margin | `déduit donc de` | First two words are compressed. | medium |


### scan 286

| Scan | Approx. line / location | Reading in transcription | Alternatives / difficulty | Confidence |
|---|---|---|---|---|
| 286 | 2, parenthesis | `donc` | Contracted initial word; rest reads `est ∞-connexe`. | medium |
| 286 | 3 | `anabélien` | Accents and the middle vowel are faint; `anobélien` is a possible literal reading. | medium |
| 286 | 5, insertion before Π₁ | `de` with inserted `ce` | The lower word looks partly like `du`; no grammatical repair is silently imposed. | medium |
| 286 | left margin at 6 | `?` | Isolated dark mark could be a question mark or a cancellation mark. | low |
| 286 | 7–8, cancellation / underlining | `et mieux que simultanément`; `H⁰(Γ,Π₁(Mon(S^!,U)))`; cancelled `=H¹(Γ,Π₁( ))=1` | Underlines are dashed in the source and rendered with `\uline`. A solid strike crosses only the right-hand formula; it is uncertain whether the whole display was intended to be cancelled. The first inner opening delimiter is overwritten and could be a brace. Empty parentheses in the H¹ term have been preserved. | medium |
| 286 | 12 | `des` | Overwritten short word at the end of the line. | medium |
| 286 | 15 | `d'indices` | Singular `d'indice` cannot be excluded from the terminal stroke. | medium |
| 286 | 18 | `d'ens` | `d'un`; the abbreviated phrase is unclear and has not been grammatically completed. | low |
| 286 | 18–19 | `opération` | `action`; a descending initial stroke supports the longer reading, but the middle is contracted. | medium |


### Scans 287–288

| Scan | Approximate line or position | Reading retained | Alternatives or unresolved feature | Confidence |
|---|---|---|---|---|
| 287 | 1 | `I^{\prime!}` | The second raised stroke has a lower dot: read as exclamation mark, not a second prime; retained consistently where this is visible. | high |
| 287 | 6 | `élém\textsuperscript{t}` | A contracted `élément` is likely; the exact abbreviation and whether the final stroke is a raised `t` are uncertain. | medium |
| 287 | 12, crossed first heading | `Commentaire.` | Possibly a different aborted heading; the cancellation obscures several middle letters. The later underlined `Commentaire.` is clear. | medium |
| 287 | 17, before the Autext display | `\deleted{\illegible{1}}` | Crossed mathematical expression, perhaps a morphism between two Pi symbols; primes and arrow direction cannot safely be read. The count denotes one mathematical item. | low |
| 287 | 18, after `groupe Π_1 de` | `tortils` | No secure alternative. The word is retained with doubt and has not been normalized to other braid terminology. | medium |
| 287 | lower left margin | `\mathfrak{S}_{I'}` | The large letter is a stylized S; its precise alphabet (Gothic or script) is uncertain. Only one prime is clearly visible in the index; `I^{\prime!}` remains possible. | low |
| 287 | lower left margin | `ce Π_1` | `ce` versus `un`; the short word before Pi is compressed. | medium |
| 287 | final main line, before inserted `couples` | `\deleted{\illegible{1}}` | Overwritten/crossed mathematical or textual item at the left edge; no secure reading. | low |
| 287 | insertion above the final main line | `couples (Π',I^{\prime!}) d'un` | `couples` has compressed middle letters. The insertion is attached before `Γ-groupe`; the exact relationship to the adjacent crossed item is not completely clear. | medium |
| 287 | final main line | `ext.` | `cat.` is a possible visual reading. The abbreviation is marked in the transcription rather than inferred from the subject matter. | medium |
| 287 | final main line, after `Π',` | `\deleted{\illegible{1}}` | One short crossed word or notation; no secure reading. | low |
| 288 | 5 | `non` in `(non seulement …)` | The word is heavily retraced. A deliberate cancellation is not certain; it is retained with doubt rather than treated as securely deleted. | medium |
| 288 | 9 | `forte` | `fort`; the ending is a short stroke. | medium |
| 288 | 10, before Autext display | `trivial` | Initial letters are overwritten. Reading and deletion status both remain uncertain; no clear cancellation line crosses the entire word, so it is retained as `\unsure{trivial}`. | medium |
| 288 | 12–13, above `serait` | `surjectivité` | The word is clear; its interlinear placement is treated as an insertion after `cette`. A compressed continuation line is also possible. | medium |
| 288 | 14 | `classe` | Possibly an abbreviated form such as `cl.`; most of the middle/end is a compressed stroke. | medium |
| 288 | 16 | `toute` | `tout`; the apparent final e is not secure. | medium |
| 288 | 17 | `op.` | `gr.`; the first letter is a small loop and the second a descending stroke. | medium |
| 288 | 18, expression added below Autext | `Autext_lac(Π',I)` | `I` appears without prime or exclamation mark in this added expression; no correction to other I notations has been made. | high |
| 288 | 18, vertical relation to added expression | Vertical `=` | A vertical isomorphism sign, such as a rotated `≃`, is also possible. The transcription therefore describes the arrangement instead of inventing an arrow. | low |
| 288 | 18–19, crossed phrase and raised replacement | `\deleted{telle que}` followed by `\inserted{ayant la}` | The crossed phrase's ending and the exact boundary between the deleted wording and the raised `la` are uncertain. | medium |
| 288 | 19, before underlined `action` | `=` | A barred-m abbreviation for “même” is an alternative, but the two short strokes look like a literal equality sign in the independent review. | medium |
| 288 | 19, after `conjugué` | `par` | `à`; the short word has a descending stroke resembling p. The manuscript sentence continues on the next scan, and grammar has not been used to suppress the doubtful reading. | medium |


### scans 289–290

| Scan | Approximate line / location | Reading used | Alternatives / source of doubt | Confidence |
|---|---|---|---|---|
| 289 | 1 | `précédente` | `précédent`; pale final stroke does not establish the last vowel independently. | medium |
| 289 | 1 | `noyau` | No secure alternative; the middle and final strokes are very faint. | medium |
| 289 | 2, both subscripts | `Autext_lac` | `Autext_loc`; the condensed subscript is not fully resolved. | low |
| 289 | 2, last factor | `\mathfrak S_{I^{\prime!}}` | A cursive permutation-group symbol is visible; the exact alphabet of the large symbol is uncertain. | low |
| 289 | 3 | `réénoncer` | No secure alternative; the two vowels and accents are compressed. | medium |
| 289 | 6 | `extérieurement` | No secure alternative; several internal letters are reduced to a continuous stroke. | medium |
| 289 | 7, insertion above `Π` | `anabélien` | The insertion is legible in outline; vowel details and its exact comma attachment are less secure. It is placed before the existing comma following `Π`. | medium |
| 289 | 8 and 13 | `\mathcal E` | Plain `E`, or an epsilon-like hand; the extension symbol has a curly form not securely attributable to a particular alphabet. | low |
| 289 | 9 | `va désigner` | The first short word and the ending of `désigner` are uncertain; no confident competing whole phrase. | medium |
| 289 | 9, parenthesis | `pts` | The abbreviation is compressed; it may have a raised final letter. | medium |
| 289 | 10 | `l'ens` | A dot after the abbreviation is not securely visible; none has been supplied. | medium |
| 289 | 12 | `notion` | No secure alternative; first letters are compressed. | medium |
| 289 | 14 | `noté` | `notée`; final vowel not distinguishable. | medium |
| 289 | 16 | `maintenant` | No secure alternative; several letters form a long wavy stroke. | medium |
| 289 | 16–17, left insertion | `ext` | The final dot, if any, is not distinguishable from the insertion stroke. | medium |
| 289 | 17, long insertion | `avec` | No secure alternative; very short opening strokes. | low |
| 289 | 17, long insertion | `fidèle (pour simplifier)` | Final vowel of `fidèle` and letters in `simplifier` are compressed. | medium |
| 289 | 17 | `fixons-nous` | The second word has heavy overwriting. No separate deleted word can be securely isolated. | medium |
| 289 | 18, insertion | `on ait` | Initial `on` may have been written with a capital `O`; retained with a doubt mark. | medium |
| 289 | 20, deletion after `Π` | `\Pi'_{I^{\prime!}}` | The deletion could instead represent a quotient `\Pi'/I^{\prime!}`; the arrangement and possible bar are obscured. | low |
| 290 | 1 | `\amalg` | `\sqcup`; the disjoint-union-like sign has joined upright strokes. | medium |
| 290 | upper-right margin | `Π,Γ` | `Π_Γ`; separation and relative size do not determine whether the second letter is a subscript. | low |
| 290 | upper-right margin | `anabélien` | Ending not fully clear; the singular form is the best reading. | medium |
| 290 | 3 | `classe` | No secure alternative; middle letters compressed. | medium |
| 290 | 4, 6–7, 13–14 | `\mathcal E`, `\mathcal E'` | The same alphabet ambiguity as on scan 289; all instances are marked. | low |
| 290 | 5 | `L_{i'}` | `Z_{i'}`; the ink strongly resembles the earlier `L`, despite the preceding definition of `Z_{i'}` as a centralizer. No mathematical correction is made. | medium |
| 290 | 6 | `projection` | No secure alternative; several letters are highly compressed. | medium |
| 290 | 9, beginning | `maximale` | Overlapped by the left marginal note. | medium |
| 290 | 8–9, interlinear parenthesis | `elle-=` | `elle-` followed by the abbreviated *même* sign; the two horizontal strokes look more like `=` than a clearly formed barred `m`. | low |
| 290 | 8–9, interlinear parenthesis | `(sans doute elle est déjà maximale elle-= ?...)` | The curved stroke below the end may be an insertion connector rather than underlining; placement immediately after `maximale` is the best local reading. | medium |
| 290 | left margin beside 8–10 | `Oui, car pour … Γ cyclique … réalisable... ! ?` | Two words before the possible `Γ cyclique` and roughly five following words remain illegible. The two fragments and final punctuation are separately doubtful. | low |
| 290 | 17 | `en se ramenant` | `on se ramène`; the initial short word and the verb ending are uncertain. | medium |
| 290 | left margin beside 15–17 | `l'hyp.` | The abbreviated ending and dot are unclear; no expansion is inserted in the transcription. | medium |
| 290 | same margin | `risque` | `risquent`; final strokes indistinct. | medium |
| 290 | same margin | `réalisée` | `réalisé`; final vowel indistinct. | medium |
| 290 | 19, deleted line | `ramené` | No secure alternative; the strike passes through the word. | low |
| 290 | 19, replacement above deleted line | `prouvée` | No secure alternative; overwritten initial-middle strokes and final vowel not entirely resolved. | medium |
| 290 | 19, replacement | `sauf` | No secure alternative; initial stroke and parenthesis are close together. | medium |


## 3. Abbreviations met

The expansions in this table are suggestions for the apparatus only. The transcription preserves the actual forms and their punctuation. Alternative readings such as `cat.` or `gr.` are included as alternatives, not represented as secure occurrences.

| Form as written or tentatively read | Suggested expansion / meaning | Location or qualification |
|---|---|---|
| `Cf` | confer / voir | 281, marginal note |
| `1°`, `2°`, `3°` | numbered assertions or premièrement, deuxièmement, troisièmement | 281 refers back to assertions outside this excerpt; 287 has numbered conditions |
| `Pb` | problème | 284, opening |
| `Aut` | automorphismes | Mathematical notation; underlined in 284–286 |
| `Autext` | automorphismes extérieurs | 287–290 |
| subscript `lac` | lacets | 287–290; `loc` remains a possible visual reading in 289 |
| `Mon` | monomorphismes | 285–286; the precise geometric space is not silently defined in the transcription |
| `ens`, `l'ens`, `sous-ens.` | ensemble, l'ensemble, sous-ensemble | Several pages; some endings and the first component of `sous-ens.` are uncertain |
| `d'ens` | d'ensemble | 286; doubtful reading, with `d'un` an alternative |
| `pt`, `pts` | point, points | Several pages; a raised terminal stroke is sometimes hard to resolve |
| `élts` | éléments | 283 |
| `élém` with raised `t` | élément | 287; exact contracted form uncertain |
| `rev.` | revêtement | 282, 284; includes `Γ-rev.` |
| `fond.` | fondamental | 283 |
| `hom` | homomorphisme | 283–284, 286 |
| `autom.`, `autom` | automorphisme | Several pages; punctuation retained occurrence by occurrence |
| `ext.`, `ext` | extérieur / extérieure | Several pages; a 287 occurrence admits `cat.` as an alternative |
| `cat.` | catégorie / catégoriel, depending on syntax | An uncertain alternative reading only; no expansion is inserted in the text |
| `isom` | isomorphisme | 283, 287 |
| `V-isom` | isomorphisme au-dessus de V | 284; prime placement remains uncertain |
| `ss-groupes` | sous-groupes | 283 |
| `sous-gr.` | sous-groupe | 285, cancelled occurrence |
| `resp` | respectivement | 284; final stop not securely visible |
| `Sps` | supposons | 284, uncertain marginal abbreviation |
| `mod` | modulo | 284 |
| `néc.` / `nécess.` | nécessairement | 284, uncertain abbreviation |
| `isot.` | isotope | 284; final stop uncertain |
| `homéo.`, `homéo` | homéomorphisme(s) | 288; the abbreviation alone does not settle number |
| `ess.` | essentiellement | 288 |
| `op.` | opération | 288; `gr.` remains a visual alternative |
| `gr.` | groupe | Alternative reading in 288, not a secure separate occurrence |
| `NB` | nota bene | 282 |
| `i.e.` | id est / c'est-à-dire | Several pages |
| `dess.` | dessus | 282; tentative reading |
| `l'hyp.` | l'hypothèse | 290, marginal note; ending and stop uncertain |
| barred-m sign, `\overline{\mathrm m}` | même | 282–283; the two-stroke signs on 288 and 290 are also recorded as possible literal `=` signs |
| `elle-=` | apparently elle-même | 290; sign remains doubtful and is not expanded |

## 4. Short legibility assessment

The main prose is often recoverable, but these are working pages with rapid contractions and substantial revision. Confidence is lowest in scan281's opening overlap and closing parenthesis, scan282's corrected covering notation, the bottom of scan284, the abandoned argument and added symbols on scan285, the bottom lines and marginal extension note on287, and the overlapping left marginalia on290. The tiny superscripts and the alphabet of the extension symbol also remain uncertain.

Clearer passages include the numbered conditions on287, much of the conjecture on286, and the main paragraphs on289. Several apparent inconsistencies remain even where the ink is readable. They have been retained, and no percentage accuracy is claimed. Reading a marked passage as a mathematical theorem without returning to the image would be unwarranted; the research notes below do not resolve its textual uncertainties.

## 5. Research notes — English, separate from the transcription

Each item identifies a source location and one of the requested kinds: **conjecture**, **unproved claim**, **unpursued implication**, or **own idea**. “Conjecture” includes explicit questions and expectations, including discarded formulations where stated. “Unproved claim” means that the proof is not supplied on these pages; it does not assert that the claim is false, novel, or still open. The author may settle a point elsewhere. These are local research prompts grounded in the supplied manuscript, not a review of the subsequent literature. Suggestions labelled “own idea” include a confidence level and a reason, and carry no claim of novelty.


1. **Scan 281, lines1–4 and upper-left margin — conjecture.** The marginal objection “Trop brutal !” changes the proposed fundamental-group comparison to one with the Γ-invariants on the right. The relevant main-text superscript is uncertain, so the exact original assertion must first be recovered; after that, one could ask which hypotheses make the comparison with invariant classes injective or surjective (Grothendieck, 1981, scan 281).


2. **Scan 281, lines5–8 — conjecture.** “Le plus agréable serait” introduces an expectation of a homotopical strengthening, followed by a reference to an “∞-équivalence” whose ending is not fully secure. A study should separate an isomorphism on the displayed fundamental groups from a statement about all homotopy groups or an actual homotopy equivalence; this page does not give the additional assumptions (Grothendieck, 1981, scan 281).


3. **Scan 281, lines9–18 — conjecture.** The author wants to establish the earlier assertions “1°, 2°, 3°” for A=A_{g,ν} with finite Γ and then “essayer de prouver” that the displayed subgroup or subspace is contractile. Those numbered assertions are outside this excerpt, and the superscript u/n is unresolved; both are prerequisites to formulating a precise theorem (Grothendieck, 1981, scan 281).


4. **Scan 282, lines5–20; scan 283, lines1–3 — unproved claim.** Beginning with “Evidemment”, the manuscript passes from a centralizing automorphism to a quotient automorphism, preservation of branch data, and an isomorphism of the pulled-back Γ-cover. A proof would need to state the category of surface automorphisms, show extension over the omitted points, and distinguish an unpointed covering isomorphism from a chosen equivariant lift; the visible V/V′ expressions should not be silently repaired (Grothendieck, 1981, scans 282–283).


5. **Scan 283, lines4–13 — unproved claim.** The condition that the composite with φ be “conjugué à φ”, together with preservation of S^{prime!}, is presented as the group-theoretic lifting criterion. It calls for an explicit verification using basepoint changes and the Γ-action; the margin's choice of a∈V and a′∈V′ makes that bookkeeping particularly relevant (Grothendieck, 1981, scan 283).


6. **Scan 283, lines14–17 — unproved claim.** “g est défini … à isotopie près” is qualified by the degenerate cases (0,ν′), ν′=0,1,2, which “il faudra examiner à part”. A proof needs a faithful passage from the relevant isotopy classes to peripheral-preserving exterior automorphisms, and the listed exceptional cases require direct treatment; no additional exception is inserted into the transcription (Grothendieck, 1981, scan 283).


7. **Scan 283, lines18–22 — unproved claim.** The lift f is said to be determined modulo the centre of Γ, and “on sait déjà” that A⁰∩Γ=(1) is then used for uniqueness in the displayed subgroup. A proof should verify both the central ambiguity of Γ-equivariant lifts and the cited intersection statement; the latter is referred to earlier work, not proved on this page (Grothendieck, 1981, scan 283).


8. **Scans 281–283 — own idea.** A useful test is to compare the manuscript's proposed fixed-point homotopy statements with the corresponding statements for families of equivariant lifts, starting with a small cyclic action and recording every lift ambiguity. **Confidence: medium as a diagnostic, low as a theorem:** the excerpt provides concrete lifting data and identifies a central ambiguity, but the missing hypotheses and uncertain exponent prevent an unconditional conclusion. This is a proposed check, with no claim of novelty (Grothendieck, 1981, scans 281–283).


9. **Scan 284, ll. 16–20 — unproved claim.** “Ce qui exprime que g provient par passage au quotient” connects a conjugacy condition on monodromy with lifting an automorphism through the covering. A proof needs to specify whether the lift is required to commute with the prescribed Γ-action and to justify precisely the stated ambiguity involving the centre; the pullback expression and centre notation have uncertain readings (Grothendieck, 1981, scan 284).


10. **Scan 284, ll. 22–25 — conjecture.** “On veut exprimer” (opening wording uncertain) seeks a criterion for the existence of a lift isotopic to the identity in `Aut(U)`, followed by “On aimerait”. The parenthetical “unique!” is an additional assertion to check: it requires ruling out a nonidentity central deck transformation isotopic to the identity after filling the indicated punctures (Grothendieck, 1981, scan 284).


11. **Scan 284, ll. 24–25 — unproved claim.** The manuscript identifies being isotopic to the identity with inducing the trivial outer automorphism of `Π₁(U)` through “i.e.”. A proof should state the exact surface class, treatment of ends and punctures, and isotopy conventions; this note does not assert that the equivalence holds without those qualifications (Grothendieck, 1981, scan 284).


12. **Scan 284, ll. 10–12 — own idea.** Test the lifting and uniqueness assertions first for a connected finite cyclic cover with one specified branch orbit, comparing peripheral monodromy before and after filling. **Confidence: medium as a useful test, not as a theorem**, because the nontriviality condition on `L_{s'} → Γ` is explicit while several later identifications depend on it (Grothendieck, 1981, scan 284).


13. **Scan 285, ll. 1–5 — conjecture.** “prouver que ce sont exactement ceux qui” continues the preceding page's expectation and proposes an exact characterization by isotopy to 1 in `Aut(V')`. The alternative formulation says a suitable lift is already isotopic to 1 on the unfilled surface; identifying precisely which Γ-equivariance requirement belongs to the inserted group notation is part of the problem (Grothendieck, 1981, scan 285).


14. **Scan 285, ll. 5–7 — unproved claim.** “se relève (en vertu de principes généraux)” asserts a group-level lifting of the identity component, with an inserted condition that `Aut(V')^0` is `1-connexe`. A proof should construct the lift by lifting isotopies, then show independence of paths and compatibility with composition; the insertion's exact attachment is uncertain but its words are legible (Grothendieck, 1981, scan 285).


15. **Scan 285, ll. 8–9 — unproved claim.** The condition on g is stated to be “certainement suffisante”. This establishes only one direction of the proposed characterization on these pages; the converse still requires control of lifts that are isotopic after filling punctures (Grothendieck, 1981, scan 285).


16. **Scan 285, ll. 10–12 — unproved claim.** “les résultats déjà obtenus impliquent que” introduces the claim that the indicated Γ-centralizing subgroup of the identity component fixes the branch set pointwise. The earlier results and their surface hypotheses are not supplied here and need to be located before treating the pointwise-fixing conclusion as unconditional (Grothendieck, 1981, scan 285).


17. **Scan 285, ll. 13–17 — unproved claim.** The quotient `Aut(U)^0/B ≃ Mon(S^!,U)` and the identity-component statement `B^0 = Aut(V)^0` are asserted with little explanation. A proof needs an evaluation map, its image and stabilizer, and an isotopy extension or local-triviality argument appropriate to the precise topology on the automorphism groups (Grothendieck, 1981, scan 285).


18. **Scan 285, ll. 16–18 — unproved claim.** “un argument connu nous montre” precedes `B/B^0 ≃ Π₁(Mon(S^!,U))`. The exact sequence of the evaluation fibration should be written explicitly, including the contribution of `Π₁(Aut(U)^0)`; the page's formula should not be treated as proved until the hypothesis that eliminates that contribution is established (Grothendieck, 1981, scan 285).


19. **Scan 285, bottom diagram — conjecture.** The endpoint `H¹(Γ,B⁰)` is accompanied by `=?1`. This is an explicit unresolved vanishing question, distinct from identifying the groups earlier in the sequence; one must specify the Γ-action and the intended nonabelian or topological cohomology convention (Grothendieck, 1981, scan 285).


20. **Scan 285, cancelled argument and final diagram — unpursued implication.** The surviving exact-sequence calculation separates a component/invariant issue from a possible `H¹` obstruction. The cancelled passage immediately above it should be read as an abandoned step, not cited as a completed proof of connectedness or surjectivity (Grothendieck, 1981, scan 285).


21. **Scan 285, ll. 13–18 and bottom diagram — own idea.** Compare the fixed subgroup of the configuration-space fundamental group with the fundamental group of the fixed-configuration locus, keeping track of the chosen Γ-invariant base configuration. **Confidence: medium as a diagnostic**, because these are distinct constructions and the displayed argument moves between invariants, components and lifting; their equality must be proved in the particular geometric setting (Grothendieck, 1981, scan 285).


22. **Scan 286, ll. 1–4 — unproved claim.** “Donc on trouve que la composante neutre” identifies the neutral component of `Aut(U)^{0Γ}` with `Aut(V)^0` and states an infinite-connectivity conclusion under a surface condition read as “V anabélien”. A proof should separate the identity component of a fixed subgroup from the fixed subgroup of an identity component and track the assumptions used in the preceding lifting calculation (Grothendieck, 1981, scan 286).


23. **Scan 286, ll. 4–6 — conjecture.** “On voudrait prouver que” explicitly asks for triviality of the Γ-invariant subgroup of the configuration-space fundamental group. Its precise action and base configuration need to be specified; the nearby inclusion of component groups does not by itself establish the requested vanishing (Grothendieck, 1981, scan 286).


24. **Scan 286, ll. 6–8 — conjecture (deleted stronger formulation).** The words “et mieux que simultanément” and the H¹ equality are crossed out. The attempted simultaneous H⁰/H¹ vanishing formulation is therefore recorded as a discarded or revised expectation, not a settled claim; whether the uncrossed H⁰ expression was also intended to be abandoned is paleographically uncertain (Grothendieck, 1981, scan 286).


25. **Scan 286, ll. 9–13 — conjecture.** “On aimerait que ceci soit vrai même indépendamment d'hypothèses de réalisabilité” asks for a statement based on an abstract homomorphism into a Teichmüller group. The phrase “hypothèses adéquates” leaves the necessary additional restrictions unspecified, making their formulation a separate research problem (Grothendieck, 1981, scan 286).


26. **Scan 286, ll. 14–23 — conjecture.** Under the heading “Conjecture”, a finite outer action on a group with peripheral-loop data is to be lifted to a more punctured group `Π'`, with a Γ-stable subset `I^{\prime!}` and a compatible “bouchage des trous” map `Π' → Π`. The numbered requirements occur on the next scan; the existence assertion here should be assessed together with those requirements rather than interpreted as an arbitrary quotient presentation (Grothendieck, 1981, scan 286).


27. **Scan 286, conjecture — own idea.** When a geometric realization is available, try deleting precisely the points with nontrivial stabilizers and compare the resulting peripheral classes with the proposed `I^{\prime!}`. **Confidence: medium as a construction to test**, because the manuscript itself contrasts realizable and abstract cases, and the stabilizer data can explain why the punctures are distinguished (Grothendieck, 1981, scan 286).


28. **Scan 286, conjecture — own idea.** Audit trivial and nonfaithful outer actions before assuming the conjecture includes a faithfulness restriction. **Confidence: medium as an edge-case check**, because the visible sentence says only “un groupe fini opérant extérieurement”; any missing restriction may instead be contained in the ambient terminology or in the continuation and must be checked there (Grothendieck, 1981, scan 286).


29. **Scan 287, lines 1–8 — conjecture (continuation of the preceding page).** The two numbered requirements combine “le stabilisateur … soit non réduit à 1” with an extension that “n'a pas d'éléments d'ordre fini ≠ 1.” A proof of the proposed construction must therefore verify both the condition on stabilizers of the added peripheral indices and the absence of nonidentity torsion in the extension; neither verification is supplied on this page (Grothendieck, 1981, scan 287).


30. **Scan 287, lines 9–11 — conjecture.** The structure “muni du morphisme Π' → Π” is asserted to be “déterminé à isom unique près.” The following commentary expressly says that this uniqueness is “ni même prouvée,” so the assertion should be tracked as part of the proposed statement, not as a result proved here (Grothendieck, 1981, scan 287).


31. **Scan 287, lines 12–16 — unproved claim.** “L'existence … est évidente dans le cas ‘réalisable’” is not accompanied here by a construction. A proof would need to specify the realization, the added peripheral data, and the map to Π, and then verify that these objects satisfy both numbered requirements rather than merely producing some punctured surface (Grothendieck, 1981, scan 287).


32. **Scan 287, Autext display and lower left margin — unproved claim.** The discussion identifies a kernel with a group denoted Π_1, then qualifies that identification in the margin: “plutôt, une extension … par ce Π_1.” The stylized S and its index are uncertain, so the exact quotient must first be established from the ink before a precise extension statement can be tested (Grothendieck, 1981, scan 287).


33. **Scan 287, lower left margin — own idea.** A useful test is to compare the kernels obtained by remembering individual added peripheral labels and by remembering only their underlying set; the latter may introduce a permutation quotient. **Confidence: medium**, because the marginal extension by a stylized S suggests this distinction, but its alphabet and index are not secure and this page supplies no proof (Grothendieck, 1981, scan 287).


34. **Scans 287–288, final paragraph of 287 through line 8 of 288 — conjecture.** The desired functor is described as “pleinement fidèle,” while achieving this is called “déjà problématique.” The comment distinguishes the already-mentioned essential-surjectivity requirement from full faithfulness; a proof must therefore control morphisms as well as construct objects (Grothendieck, 1981, scans 287–288).


35. **Scan 288, lines 7–8 — unproved claim.** “La fidélité signifie justement que Π_1^Γ = 1” reduces faithfulness to a fixed-subgroup assertion. To justify the reduction, one must identify the relevant automorphism kernel and its Γ-action precisely, including the peripheral labels and the marginal correction to the kernel on scan 287 (Grothendieck, 1981, scan 288).


36. **Scan 288, lines 9–15 — conjecture.** The author says that surjectivity of the displayed map between Γ-invariant Autext groups “serait conséquence du fait” that a suitable “classe d'homéo.” contains a representative “commutant à Γ.” This calls for a representative-selection argument in the realizable case; the page does not prove that a class with the required equivariance has an actually commuting representative (Grothendieck, 1981, scan 288).


37. **Scan 288, lines 16–19 — conjecture.** “Il faut ajouter à ceci” introduces a condition comparing another lift of Γ with the preceding one, subject to having the same action on `I^{\prime!}`. The statement continues on the next scan and the word immediately before the final “la” is doubtful, so its conjugacy condition should be completed and checked there before it is used as a formal hypothesis (Grothendieck, 1981, scan 288).


38. **Scan 288, lines 16–19 — own idea.** Once the automorphism kernel and a reference lift are fixed, one could try to encode differences between lifts by nonabelian 1-cocycles and test whether the desired conjugacy conclusion amounts to a vanishing statement for their equivalence classes. **Confidence: medium**, because the text explicitly compares lifts up to conjugacy, but the exact kernel, peripheral action, and allowed class of lifts must be settled first; this is a proposed route, not an established or claimed new result (Grothendieck, 1981, scan 288).


39. **Scan 289, lines 3–4 — conjecture.** The announced intention to “réénoncer la conjecture précédente” in a “forme un peu plus générale” makes the following construction a proposed strengthening or reformulation, not a proved theorem on this sheet. A comparison with the earlier conjecture should determine exactly which realizability assumptions are being relaxed; the uncertain word reading does not justify supplying those assumptions in the transcription (Grothendieck, 1981, scan 289).


40. **Scan 289, lines 9–15 — unproved claim.** The definition of `Φ(Π,Γ)` uses conjugacy classes of nontrivial maximal partial sections, after which the text says “Il est clair que Φ est un Γ-ensemble” and “on sait aussi qu'il est fini.” A local proof would need both a well-defined action on the conjugacy classes and a finiteness argument for those maximal partial sections; neither argument is written out here (Grothendieck, 1981, scan 289).


41. **Scan 289, lines 12–14 — unproved claim.** The parenthesis says that the intrinsic character of `Φ(Π,Γ)`, independently of the chosen extension, was “déjà noté” (ending uncertain). A verification should identify the equivalences of extensions under which maximality and conjugacy classes of partial sections are preserved, rather than treating the choice of extension as immaterial without specifying that equivalence (Grothendieck, 1981, scan 289).


42. **Scan 289, lines 16–22; scan 290, line 1 — conjecture.** After imposing a `Γ`-stable subset `I^{\prime!}` with nontrivial stabilizers, the manuscript proposes to “définir une bijection,” displayed on the following scan as a map from the disjoint union to `Φ(Π,Γ)`. A proof would have to show that filling the selected peripheral classes produces exactly the new classes represented by that marked subset, with neither identifications nor additional classes (Grothendieck, 1981, scans 289–290).


43. **Scan 290, upper-right margin — conjecture.** The qualification “également anabélien, pour être plus sûr !” indicates hesitation about the hypotheses for the proposed bijection. Because its mathematical subject is itself unclear (`Π,Γ` versus `Π_Γ`), the note should be checked against other pages before any precise additional assumption is attributed to Grothendieck (Grothendieck, 1981, scan 290).


44. **Scan 290, a), lines 5–9 — unproved claim.** The local centralizer construction is followed by the assertion that the resulting partial section is “contenue dans une unique section partielle” with `maximale` at the next line. This requires more than merely extending a finite subgroup to some maximal one: uniqueness, and its independence of the chosen peripheral representative, must also be justified. The possibly written `L_{i'}` where `Z_{i'}` might be expected is a textual uncertainty, not a license to repair the argument (Grothendieck, 1981, scan 290).


45. **Scan 290, a), interlinear note beside lines 8–9 — conjecture.** “sans doute elle est déjà maximale” asks whether taking a maximal enlargement is unnecessary. The statement should be distinguished from the preceding uniqueness assertion, and the partly illegible marginal response should not be counted as a recovered proof (Grothendieck, 1981, scan 290).


46. **Scan 290, a), lines 10–11 — unproved claim.** The claimed application is “évidemment compatible avec les actions de Γ.” A verification would track the conjugation of a peripheral subgroup, its centralizer in the extension, and the resulting partial-section class through the quotient map; the heading's `I'` should not be silently replaced by `I^{\prime!}` in formulating that check (Grothendieck, 1981, scan 290).


47. **Scan 290, b), lines 13–17 and left margin — unproved claim.** The main text says that a “section maximale donne une section maximale,” apparently by reduction to cyclic `Γ`, but the margin begins “pas clair” and questions the hypothesis on the nontrivial stabilizers. A proof must show that the reduction preserves the hypotheses needed for maximality and that no larger partial section appears after passing to the quotient; the margin records a live objection, not assent (Grothendieck, 1981, scan 290).


48. **Scan 290, c), lines 18–21 — unproved claim.** The revised paragraph restricts the claimed proof of bijectivity to realizable situations or a selected set reduced to one element, adding “mais alors Γ cyclique.” Checking the latter implication requires identifying the result that forces the full stabilizer of that one element to be cyclic and explaining why this makes the situation realizable; neither argument is developed on this scan (Grothendieck, 1981, scan 290).


49. **Scan 290, a)–c) — own idea; confidence: medium.** Subject to checking the relevant kernels are torsion-free, reformulate partial sections as finite subgroups of the extensions that inject into `Γ`, then study their images under `\mathcal E'\to\mathcal E`. This may isolate the two separate obstructions to the proposed decomposition: distinct maximal classes merging and new maximal classes not arising from the designated peripheral centralizers. The reason for the suggestion is that both displayed constructions already proceed through extension groups and quotient maps; no validity or novelty of this reformulation is asserted (Grothendieck, 1981, scan 290).


50. **Scan 289, final paragraph; scan 290, b)–c) — own idea; confidence: medium.** Test the construction with explicit presentations for small cyclic actions on punctured surfaces, tracking a chosen invariant subset of punctures through filling. Compare cases where all marked stabilizers remain nontrivial with cases where that condition changes under restriction to a subgroup. This is a diagnostic proposal motivated by the marginal objection about stabilizers, not a proposed counterexample or a proof (Grothendieck, 1981, scans 289–290).


## Reference

Grothendieck, A. (1981). *La Longue Marche à travers la théorie de Galois* [Unpublished manuscript, cote 140-2, archive file “La Longue Marche, pages 1–292”; supplied scans 281–290, archive footers 280–289]. Université de Montpellier.

Bibliographic metadata above follows the attached brief. The primary evidence used for the transcription and the source-based research notes is the supplied set of ten images.

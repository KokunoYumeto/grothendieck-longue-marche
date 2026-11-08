# LM_C4-229-247 — Editorial and research notes

## 1. Scope, pagination, and conventions

This is a diplomatic transcription of the nineteen supplied scans, in filename order, of Alexander Grothendieck’s *La Longue Marche à travers la théorie de Galois* (1981). The archive description supplied with the task is Montpellier, cote 140-4, pages 650bis–787. Readings were made from the supplied images; published transcriptions were not used to supply or correct manuscript text.

Scan references throughout these notes refer to the filename numbers, 229–247. The lower-left handwritten folios run from 228 to 246; they are retained as marginal content. The visible upper manuscript numbers run from 762 to 771, occurring on alternate scans. The mechanically printed folio, URL, institutional address, and postal address below each manuscript frame are also transcribed, as a separate centered block at the end of that scan. They are provenance text printed on the supplied image, distinct from the handwriting.

The transcription preserves cancellations, additions, unfinished sentences, visible anomalies, and the author’s abbreviations. A vertical bar inside an uncertainty macro separates alternative readings; it is editorial rather than an asserted source character. Literal dotted continuations already present in the manuscript are retained, particularly in equation (33); they do not stand for omitted content. Doubts attach to the ink, while mathematical checks belong exclusively to section 5 below.

The TeX file is a fragment with no preamble. It uses the requested editorial macros, ordinary LaTeX mathematics, TikZ, and tikz-cd. A host document needs definitions for those editorial macros, mathematical support such as amsmath/amssymb, and TikZ/tikz-cd; its definitions must accept both text and mathematics, including editorial marks inside exponents, diagram nodes, and labels. No macro definitions or diagnostic wrapper are included in the fragment.

## 2. Table of doubts

Approximate line references count the main handwritten body, excluding the printed footer; equation numbers and marginal positions give more precise locations. High, medium, and low denote confidence in the proposed reading, not in the mathematical correctness of the manuscript. Several occurrences of the same ambiguous glyph may share one localized row.

| Scan | Approximate line or position | Reading | Alternatives or issue | Confidence |
|---|---|---|---|---|
| 229 | 2; (11) | \mathbb S_0 | \mathfrak S_0; distinctive handwritten S-like glyph | medium |
| 229 | 3, before exponentiel | revêtement | Ending compressed into the terminal stroke | medium |
| 229 | (11), second row right | terminal point within parenthesis | point outside an unfinished parenthesis | low |
| 229 | 6, after « relèvement de » | u_{\mathbb S^1} | the S-like subscript and superscript 1 are compressed | low |
| 229 | (12), crossed-out fragment on right | s'écr. | possibly another abbreviated fragment | low |
| 229 | before « qui induit » | deleted Propo | unfinished Propos | medium |
| 229 | proposition, last line | deleted contra | unfinished beginning of a longer word | low |
| 230 | 4, deletion before s'identifie | qui | overwritten short word | medium |
| 230 | 6, deletion replaced by l'image inverse | au dessus de | original phrase strongly crossed through | low |
| 230 | 8, cancelled symbol before R | R | overwritten double-line letter | low |
| 230 | 10, deleted word after le | dernier | second half is partly covered by stroke | medium |
| 230 | Cor. 1, first line | inv. | inverse abbreviated by abbreviated ending stroke | medium |
| 230 | Cor. 1, opening | Le sous-g. inv. | Le sous-groupe inverse; compressed abbreviation, independently reread against an initial L'image reading | medium |
| 230 | Cor. 1, first occurrence of Sl | 2 | loop resembles 0/parenthesis | medium |
| 230 | Cor. 1, deleted word after gén. | can. | canon.; degen. | low |
| 230 | lower-left marginal note | subset sign after {±1} | de | low |
| 230 | Cor. 2, cancelled mark before omega-prime | overlined omega | an erased overbar or arrow | low |
| 231 | (16), deleted map below exact sequence | n maps to omega-prime_0 | severely crossed mapping; exponent could have been present | low |
| 231 | (16), replacement mapping | omega_0^n | (omega-prime_0)^n; prime may be obscured by preceding cancellation | low |
| 231 | Corollaire and its proof | Gothic capital Z | Gothic lower-case z; the ink is a three-like group symbol | medium |
| 231 | last paragraph after conjugaison | SPS | abbreviation for a form of supposer; literal letters uncertain | low |
| 231 | last paragraph, subgroup/circle relation | subset | membership sign | medium |
| 232 | upper-left marginal note | sympathique | compressed middle letters | medium |
| 232 | middle paragraph, deleted formula | = −id | omega = −id; initial mark could be part of an overwritten letter | low |
| 232 | above the cancelled parenthesis | l'unique | heavily struck word | low |
| 232 | deleted parenthetical clause | distinct de +1 | ≠ +1; the connecting word/symbol is crossed by the deletion line | low |
| 232 | deletion below unique générateur | d'un relèvement | soit un relèvement | low |
| 232 | lower-left marginal note, first line | vaut | est; abbreviation/stroke | medium |
| 232 | lower-left marginal note | inverse image L-tilde_rho | L_rho without visible tilde | medium |
| 233 | top line, main deletion | d'une façon | ending obscured by cancellation | low |
| 233 | top line, deletion above the line | de la | separate very short phrase, overwritten | low |
| 233 | after Gl(2,Z)-tilde | un gr. | un groupe; au gr. | low |
| 233 | upper-left margin, before x+iy on right | minus | overwritten short sign | medium |
| 233 | action paragraph | S_0 with doubled/stylized S | fraktur S_0 | medium |
| 233 | deleted symbol before S-tilde_0 | R | heavily overwritten letter | low |
| 233 | (22), first exponent inside parentheses | πit | πi without t | medium |
| 233 | (22), hooked mark after exp on second line | opening brace | cancelled character; no secure closing brace visible | low |
| 233 | after “symétrie” | p.r. | par | medium |
| 233 | fixed-point exponential, denominator | 4 | 8; numeral overwritten | medium |
| 233 | after fixed-point expression | extra closing parenthesis | retraced parenthesis rather than a separate one | low |
| 233 | (23), denominator of 1 | 8 | 4; numeral overwritten | low |
| 233 | final line, deletion after que | tau-prime with tilde | tau-prime without tilde | low |
| 234 | 4 | aussi | ainsi; the final word is highly compressed | medium |
| 234 | 6, deletion before “dans” | et | The stroke through this short word hides its body; “sont” is another possible reading | low |
| 234 | 6, group name | Sl | First letter is overwritten; possibly correction from Gl | medium |
| 234 | 9 | mbs | Abbreviation of “membres”; the final superscript-like stroke is compressed | medium |
| 234 | 9 | caractéristiques | Final letters approach the right frame | medium |
| 234 | unnumbered display after (20), first underbrace | deleted exponent −1 after omega_0 | The dark overstrike may cover a different abandoned exponent; omega_0 itself is clear | low |
| 234 | proof opening and diagram (26) | Pi (capital) | pi (lowercase); symbol is reinforced/overwritten | medium |
| 234 | proof opening, deletion | engendré | Several interior letters obscured by a horizontal cancellation | medium |
| 235 | 2, abstract quotient group; equation (27); proof conclusion | pi / Pi | Uppercase or lowercase is not consistent in the handwriting; diagram glyph is reinforced | medium |
| 235 | 4 | central | Interior strokes compressed; final “l” has a large flourish | medium |
| 235 | comparison argument, line after “facteurs extrêmes” | des | de; the small final stroke is unclear, so the name of the lemma is not normalized | medium |
| 235 | second exact sequence, cancelled label | (28) | (27); label is heavily crossed out | low |
| 235 | equation (28), deletion after first equals | 1, | omega_0; the cancelled symbol is densely overwritten | low |
| 235 | final paragraph, line 1 | essayer | Ending compressed | medium |
| 235 | final paragraph, deleted word replaced by groupe | élément | Word body partly removed by horizontal strike | low |
| 235 | final paragraph, line 2 | avec | en; connected strokes are abbreviated | medium |
| 235 | final paragraph, cancelled beginning before r_0 tilde | au de | Possibly an abandoned “au dessus”; only these letters are proposed in the transcription | low |
| 235 | final paragraph, second unlifted element | r_1 | sigma_0; the written symbol differs from the clearly written lifted r_1 on the preceding line | low |
| 235 | final paragraph, penultimate line | m’inspirant | Ending written as a short stroke | medium |
| 236 | first prose line | engendrent | Final compressed stroke; plural ending not fully separated | medium |
| 236 | third prose line, after the sigma–tau pair | engendre | engendrent; the end of the verb is flattened | medium |
| 236 | fourth–fifth prose lines, after the omega–tau pair | engendrent | Word crosses the line end; terminal stroke is indistinct | medium |
| 236 | diagram (31), lower right vertex | D indexed by sigma tilde | rho tilde; the subscript is overwritten and its left loop resembles rho | medium |
| 236 | map j, second formula, argument | tau prime tilde | Subscript-like overstrike makes the letter unclear; no extra index has been silently supplied | medium |
| 236 | comment after (32) | somme | Initial letter has an open loop | medium |
| 236 | (33), cancelled product in second row | sigma tilde r_0 tilde | Both factors are heavily overwritten; order is suggested by the surviving sigma contour and final subscript 0 | low |
| 237 | (34), superscript after r_0 in first product | deleted −1 | Dense patch resembles a cancelled inverse exponent; no unmarked exponent is supplied | low |
| 237 | (34), between cubed and squared factors | deleted = above multiplication dot | The original operator is overwritten; the replacement dot is separately visible | medium |
| 237 | (34), superscript after r_0 in second product | deleted −1 | Dense patch resembles a cancelled inverse exponent | low |
| 237 | below the factors, crossing bottom of box | deleted “amalgamée” | A cancelled broad underbrace labelled omega_0; word-versus-symbol distinction is itself uncertain under the large overstrike | low |
| 238 | upper-left beside “Posons” | check mark | Faint pencil-like hook; possibly an incidental mark | low |
| 238 | (35), cancellation before X_1 | X_1 | Subscript heavily overwritten | low |
| 238 | (37), argument of the second T | U indexed 1,1 | U and final index are heavily retraced; the nearby uncancelled gloss is clear | medium |
| 238 | lower paragraph, verb describing the action | différentiablement | différentiellement; word divided across lines and internal letters compressed | medium |
| 238 | lower paragraph, cancelled symbol before X_1 | calligraphic T | tau; dense overstrike | low |
| 239 | 1, opening reference | `1°)` | Overwritten numeral, possibly an earlier `4` beneath `1` | low |
| 239 | 1, isolated mark immediately after reference | `e` | Unresolved retraced or cancelled letter | low |
| 239 | 4, after covering-group notation | `du` | `de` | medium |
| 239 | 5, deletion below inserted reference | `le Théorème` | Final letters obscured by rule and insertion | medium |
| 239 | 7, overwritten mark between S and Teichmüller glyph | `*` | Cancelled letter/symbol, no secure identity | low |
| 239 | 10, before `3°` | `du` | `de` | medium |
| 239 | a), cancelled symbols beneath first factors | `\omega\widetilde\sigma` | The looping strokes may be a different cancelled subscript or expression | low |
| 239 | a), cancellation beneath `=1` | `\omega_0` | Prior right-hand side unrecoverable with confidence | low |
| 239 | a), first action symbol | `\widetilde\tau'` | Overwritten original symbol resembles rho | medium |
| 239 | b), cancelled exponent on first r in product | `-1` | Retraced exponent not fully recoverable | low |
| 239 | b), cancellation below product | `\omega_0` | Additional cancelled strokes over and before omega | low |
| 239 | 15, after `que nous` | `calculerons` | Middle and final letter sequence abbreviated by continuous strokes | medium |
| 239 | (39), subscript on Aut ext | `loc` | `lac` | medium |
| 240 | Upper-left diagonal margin, first word | `j'utilise` | Final strokes are hurried | medium |
| 240 | Upper-left margin, after `la` | `not.` | The final abbreviation stroke could be longer than a t | medium |
| 240 | Insertion above line 3 | `-lacets` | Middle vowels unclear; final t and s favour this reading over `-local` | medium |
| 240 | Deletion before the action display | `de S` | Dense obliterating strokes between the two discernible ends | low |
| 240 | 10, after `doit` | `normaliser` | Final r is only a short stroke | medium |
| 240 | 16, final parenthesis | `!` | Two small marks alongside the closing parenthesis | low |
| 240 | 17, superscript near U′ at right edge | `a` | A partly clipped overwritten mark; possibly cancelled rather than a retained exponent | low |
| 240 | 19, before `principal` | `rev.` | Terminal dot not distinct | medium |
| 240 | Last line, deletion after `base` | `a` | Heavily retraced cancelled letter | low |
| 241 | Top-left cancelled equation number | `(44)` | `(42)`; several overstrikes | low |
| 241 | 2, opening word | `au` | `en`; the first letter is retraced | medium |
| 241 | (44), description of l | `classe` | A compressed abbreviation beginning `cl` cannot be excluded | medium |
| 241 | (44), deleted symbol before `a+gamma` | `gamma` | `tau` | low |
| 241 | 10, inside quotation | `compose` | Middle strokes are very compressed | medium |
| 241 | Drawing, top-left vertex label | `a-e_1` | Minus sign thickly retraced; subscript 1 is retained | medium |
| 241 | Drawing, lower-left vertex label | `a-e_0-e_1` | Second minus thickly retraced | medium |
| 241 | Drawing, lower-right vertex label | `a-e_0` | Minus sign thickly retraced; subscript 0 is retained | medium |
| 241 | 19, adjective in quotation marks | `radiologique` | Central vowel and consonant sequence uncertain | medium |
| 242 | Heading, above `germes d'espaces` | `revêtements de`, underlined insertion | The lower curved stroke belongs to the insertion connector; the insertion is not treated as doubly underlined. | high |
| 242 | Upper-left diagonal marginal note | deleted `le`, inserted `pas le` | The underlying article is traversed by a strong cancellation; `les` is a weaker possible reading. | low |
| 242 | Main definition, line 2 | `une` followed by deleted `base de`, then `filtre` | The feminine article remains visibly after deletion; it has deliberately not been changed to `un`. | high |
| 242 | Equation (46), first Hom subscript | `Phi_{S_i},Phi'` | The small raised tick near `S_i` could be read as a prime, but close comparison with the same subscript in the explanatory sentence favours the comma belonging to the pair of filters. | medium |
| 242 | After equation (46) | deleted `Phi_{S_i} est` | The cancellation passes through the subscript and the short word `est`; both remain readable. | medium |
| 242 | Compatibility condition, before `on ait` | deleted `f` | The ink is retraced and looped. The underlying letter is f-like; whether it is a cancellation or an abandoned overwritten f cannot be settled. | low |
| 242 | Below-right of equation (47) | `*`, doubt marked | The isolated dense ink mark may be an asterisk, a tiny deletion, or an incidental pen mark. It is retained without assigning an explanatory function. | low |
| 242 | Final paragraph, first word | `ces\|les` | The initial open stroke favours `ces`; the short first syllable remains ambiguous. | medium |
| 243 | upper-left margin | `aller` | unresolved cursive word | low |
| 243 | upper-left margin | `loin` | `long` | low |
| 243 | main line 4, deleted word after `germe` | `est` | blackened letters; no secure alternative | medium |
| 243 | (48), image of `E` | `{}^1 E_{(S,Φ)}` | `\widetilde E_{(S,Φ)}`; the initial slanted stroke is not secure | low |
| 243 | second numbered condition | `ess!` | `ess` with superscript `t` | medium |
| 244 | main line 2, deleted word above/between `top.` and `peut` | `\illegible{1}` | a word such as `doit` was considered but no letters are secure after magnification | low |
| 244 | main line 4 | `associant` | ending compressed; no equally likely complete alternative | medium |
| 244 | main line 5, after `espace` | `S` | an overwritten `X` may underlie the letter | medium |
| 244 | main line 8 | `induit` | `induite` | medium |
| 244 | first word after `Soit` | deleted script `S` | a first attempt at script `X` | low |
| 244 | (50), first argument | script `X` over a deleted script `S` | overlapping retracing rather than a distinct deleted symbol is possible | low |
| 245 | beginning of definition paragraph | `Soient` | `Soit` | medium |
| 245 | `voisinages de Y ... X` | `dans` | abbreviation `ds` | medium |
| 245 | residual-germ parenthesis | `ssi` | final abbreviated stroke is not fully distinct | medium |
| 245 | marginal note before (52) | `diagramme` | compressed ending; no confident alternative | medium |
| 245 | marginal note before (52) | `canoniques` | abbreviated/compressed middle letters | medium |
| 245 | (52), upper-left node | `Germ_Y(X)` | overtraced abbreviation; the final letters are less secure | medium |
| 245 | (52), upper-right node | `Gerres_Y(X)` | `Geres_Y(X)` | low |
| 245 | cancellation after `cette notion` | `surtout` | only the principal strokes remain visible | medium |
| 245 | cancellation before `1-connexe` | `simp` | an incomplete beginning of `simplement`; no visible period | low |
| 245 | cancelled tuple after `espace` | `(S,Φ)` | symbols are overstruck, but match the inserted tuple above | medium |
| 245 | last line, left-hand variable | `X` | overtraced script `X` | medium |
| 246 | left of first line | isolated `.` | stray pen point rather than intended punctuation | low |
| 246 | transition after universal-cover notation | `quoi` | `qui`; the sequence visibly continues `il me`, and has not been repaired grammatically | low |
| 246 | lower paragraph, overwritten subscript of `Φ` | deleted `S′_i` | a deleted `S` or differently indexed `S` | low |
| 247 | (54), target-category abbreviation | `Germesp` | middle and final abbreviation strokes are compressed | medium |
| 247 | main line 4, cancellation before `un` | deleted `le` | a very short abandoned word or quotation mark; the blackened strokes do not yield secure letters | low |
| 247 | main line 8, cancellation before `cat.` | deleted `g` | an abandoned initial, perhaps of `germes`; no further letters can be recovered | low |
| 247 | start of second paragraph, following deleted `que` | `toujours` | `tjrs` | medium |
| 247 | second paragraph, cancellation before `multigaloisienne` | deleted `g` | blackened beginning of a longer word; the loop resembles `g` | low |
| 247 | lower paragraph, `Les ... universels` | `rev!` | `rev.`; the punctuation has a visible tall stroke above the dot | medium |
| 247 | penultimate prose line | `1-connexe` | `1. connexe`; separator looks short and point-like | medium |
| 247 | bottom equation number | `55` | `53`; the second digit is compressed at the bottom frame | medium |

## 3. Abbreviations met

Expansions are proposed only in this list. Variants, doubtful forms, and cancelled beginnings are retained separately where their readings or proposed expansions differ.

| Written form | Proposed expansion | Scan(s) |
|---|---|---|
| `rev.` | revêtement; revêtements (plural in this occurrence) | 229; 230; 243; 244 |
| `i.e.` | id est | 229; 230; 231; 233; 234; 242; 246 |
| `\overline{\mathrm m}` | même | 229; 236 |
| `Propo (deleted; doubtful)` | beginning of Proposition | 229 |
| `Dém.` | démonstration | 230; 234 |
| `O.K.` | okay / confirmation | 230 |
| `Cor.` | corollaire | 230 |
| `inv.` | inverse | 230 |
| `sous-g. (doubtful)` | sous-groupe | 230 |
| `gén.` | générateur; générateurs | 230; 232; 234 |
| `can. (deleted; doubtful)` | canonique | 230 |
| `él.` | élément | 230 |
| `resp.` | respectivement | 230; 232; 241 |
| `Ker` | noyau (kernel) | 230 |
| `prop.` | proposition | 231; 233; 239 |
| `p.` | page | 231; 239 |
| `tt` | tout | 231; 244 |
| `SPS (doubtful)` | probably supposons or a shorthand involving supposer | 231 |
| `ens` | ensemble | 231; 232 |
| `cqfd.` | ce qu'il fallait démontrer | 232; 235 |
| `can.` | canonique | 232; 247 |
| `id` | identité | 232 |
| `gr. (deleted; doubtful)` | groupe | 233 |
| `NB` | nota bene | 233; 240; 245 |
| `p.r.` | par rapport | 233 |
| `autom.` | automorphisme | 233 |
| `pt` | point | 233; 239; 240; 245 |
| `cf` | confer / compare | 234 |
| `§` | section / paragraph | 234 |
| `mbs` | membres | 234 |
| `OK.` | agreement / “okay” | 234 |
| `l’hom` | l’homomorphisme | 234 |
| `mod` | modulo | 234 |
| `dfn` | définition | 235 |
| `iso` | isomorphismes / isomorphisme | 235 |
| `cor.` | corollaire | 236 |
| `hom` | homomorphisme | 238 |
| `NB.` | nota bene | 239 |
| `cf.` | confer / compare | 239 |
| `isom.` | isomorphisme | 239 |
| `dfn over an equality` | définition / by definition | 239 |
| `Aut ext` | automorphismes extérieurs | 239 |
| `loc (doubtful)` | local / locaux; `lac` remains an alternative paleographic reading | 239 |
| `not. (doubtful)` | notation | 240 |
| `Norm` | normalisateur | 240 |
| `Aut` | automorphismes | 240 |
| `lac` | lacets; this is visibly a subscript in the normalizer and action expressions | 240 |
| `rev. (doubtful final dot)` | revêtement | 240 |
| `iso. can.` | isomorphisme canonique | 241 |
| `ab` | abélianisé / abélianisation | 241 |
| `appl.` | applications | 242 |
| `top.` | topologiques | 242; 244 |
| `Hom` | homomorphismes/morphismes, here the maps compatible with the displayed filters | 242 |
| `Rev` | revêtements, in the underlined category notation | 242 |
| `Ens` | ensembles | 243 |
| `underlined Rev` | revêtements | 243 |
| `const.` | constant | 243 |
| `pl.` | pleinement | 243 |
| `loc.` | localement | 243 |
| `ess! / ess with superscript t` | essentiellement (reading of the ending uncertain) | 243 |
| `tte` | toute | 243 |
| `hom.` | homomorphisme | 243 |
| `ext.` | extérieur | 243 |
| `cat.` | catégorie | 244 |
| `i.e` | id est | 245 |
| `ssi` | si et seulement si | 245 |
| `tjrs` | toujours | 245 |
| `deleted simp` | beginning or abbreviation of simplement | 245 |
| `Germ` | germe | 245 |
| `Gerres (uncertain)` | germe résiduel | 245 |
| `rev (without a visible period in some occurrences)` | revêtement | 246 |
| `isom` | isomorphisme | 246 |
| `Germesp (uncertain)` | germes d'espaces | 247 |
| `rev! (uncertain)` | revêtements, perhaps the same abbreviation `rev.` with an incidental stroke | 247 |
| `iso.` | isomorphisme | 247 |


## 4. Legibility and limits

The principal prose, most matrices, and the live portions of the displayed presentations are reasonably legible. Compressed word endings and abbreviated strokes are less secure than the overall sentences. The doubt table records these distinctions rather than assigning a uniform confidence to a page. One blackened word on scan 244, immediately after “top.”, remained unreadable after enlargement and is represented by the sole word-count illegibility marker.

The least trustworthy material is the cancelled map beneath (16), the successive revisions and diagonal notes on scan 232, the overwritten constants and exponents on scan 233, the small cancellations in (28) and (34), and the overstruck presentations on scan 239. The clipped mark by the covering-space symbol on scan 240, the object abbreviations in the marginal square on scan 245, and the short blackened words on scan 247 also remain uncertain. These marks have been represented, with alternatives where possible.

The lattice sketch is reconstructed in TikZ, retaining the visible arrow directions and the apparent interchange of coordinate indices in its labels. The diagrams likewise retain their written directions and uncertain objects. The final page was inspected at the same level as the opening pages, including the full rotated vertical note and its terminal symbol. Compilation and structural checks establish that the fragment can be processed and that all scans and inventoried elements are represented; they cannot resolve paleographic uncertainty. The transcript is therefore an explicitly qualified reading, not a claim that every doubtful stroke has been settled.

## 5. Research notes — English

These notes are separate from the diplomatic text. Each scan reference cites the supplied manuscript (Grothendieck, 1981); short quotations anchor comments to the visible wording. “Unproved claim” means that the indicated step is not proved at that location in the supplied passage, even when it may follow from earlier work or be addressed later. Proposed investigations and conditional calculations are not assertions of novelty or corrections to the transcription.

1. **Scan 229, proposition — unpursued implication.** The assertion « homéomorphe à R³ » would imply contractibility, and hence vanishing of all positive-dimensional homotopy groups, of the displayed covering group. This is a consequence to check against the precise covering construction, not an alteration of the proposition.

2. **Scan 229, (13) — own idea.** The extension over the group with determinant ±1 should be examined as an extension with a possibly nontrivial action on its infinite cyclic kernel. Confidence: high as a question to investigate, because the disconnected group and the later reflection formulas make the coefficient action consequential; this note does not assert centrality.

3. **Scan 230, proof of the proposition — unproved claim.** « s'identifie topologiquement à l'inclusion » of the unit circle into its product with R² is used without a construction on this page. One would want an explicit parametrization of Sl(2,R), a check of the embedded circle, and then an application of the lifting classification.

4. **Scan 230, Cor. 1 — unproved claim.** The assertion “est ≃ Z” for the inverse image of a finite cyclic subgroup includes a uniquely normalized generator. The next scan develops a closely related claim, but on this page the conjugacy-to-rotations and normalization steps have not yet been written out.

5. **Scan 230, Cor. 2 — unproved claim.** « L'action d'un g » of determinant −1 is asserted to invert the kernel generator and the central generator. A proof needs a lift of a reflection and a computation of its action on a full turn; extending from one reflection to every determinant −1 element also requires an argument.

6. **Scan 230, last exponential condition — own idea.** Compare the written membership sign with the intended typing of u as a point of the unit circle, while keeping the original sign in the transcription. Confidence: high that a typographical/handwriting issue warrants review, because the immediately preceding display identifies u with the complex number u(1); no correction is asserted.

7. **Scan 231, “Je voudrais décrire” — conjecture / question.** « Je voudrais décrire ... par générateurs et relations » states the aim of obtaining a presentation of the lifted integral matrix group. Later pages in this packet address that aim; its occurrence here is retained as a research item.

8. **Scan 231, last paragraph — unproved claim.** « par conjugaison SPS » suppresses the justification that a finite cyclic subgroup of Sl(2,R) can be placed in the displayed rotation subgroup. A proof would need a conjugating real basis, with attention to the determinant of the change of basis and the chosen orientation.

9. **Scan 231, proposition — unpursued implication.** The assertion “est isomorphe à Z” about the inverse images of the order-six and order-four subgroups supplies candidates for an amalgamated presentation. The actual amalgamation and compatibility of central generators need the subsequent relations; they do not follow solely from the cyclicity assertion.

10. **Scan 232, (17)–(18) — own idea.** The displayed operation uses exponents +2n and +3n, whereas (17) equates rho-tilde cubed with sigma-tilde to the power −2. Under a central infinite-order omega-prime, the two sides acquire factors omega-prime to +6n and −6n respectively; a sign check is therefore necessary before using this as a torsor action. Confidence: high in the conditional calculation; the transcript retains both positive exponents as written.

11. **Scan 232, lower-right margin — conjecture / question.** « Faire la vérification » explicitly leaves a verification to be performed near the normalization formulas (20). A verification should establish existence and uniqueness of the indicated lifts and compatibility with the chosen omega_0, rather than infer them from a preferred presentation.

12. **Scan 232, “il vaut mieux dire” margin — unproved claim.** The note asserts a unique generator of each cyclic inverse image lying above the selected rho or sigma, followed by relations (20). Proving this requires knowing how each integral matrix sits in its finite cyclic subgroup and which sign of the infinite cyclic generator projects to it.

13. **Scan 232, (19)–(20) — own idea.** Track omega_0, which lies over the central order-two subgroup, separately from omega-prime_0, the kernel generator, throughout the later group presentations. Confidence: high as a useful consistency check, because (19) explicitly makes the former a square root of the latter and changing their roles changes the extension.

14. **Scan 233, “cette extension est scindée” — unpursued implication.** The order-two lift constructed in (21) gives a splitting over the chosen reflection subgroup. Together with the inversion action from the preceding corollary, this invites an explicit semidirect-product description of that preimage; the extension's multiplication should be checked before carrying the description to the full integral group.

15. **Scan 233, (22)–(23) — own idea.** Verify the formulas against the stated parametrization z = exp(2iπt), keeping the manuscript's written expressions separate from the check. For a reflection z ↦ i times the conjugate of z, this parametrization gives the candidate lift t ↦ 1/4 − t modulo integers; the fixed parameter is 1/8, which may help explain—but does not resolve—the overwritten fraction and the extra 2iπ in (23). Confidence: high in this conditional calculation, low in any claim about the author's intended correction.

16. **Scan 233, beginning “Ceci résulte” — unproved claim.** « Ceci résulte ... aussitôt de la prop. précédente » leaves the passage from cyclic inverse images to the unique normalized rho- and sigma-lifts implicit. A proof should separate uniqueness of a generator with specified projection from compatibility of its powers with the selected central generator.

17. **Scan 234, theorem (25); kind: unpursued implication.** The displayed relation “$\widetilde\rho^3\cdot\widetilde\sigma^2=1$” gives a natural route to comparison with a two-generator one-relator group of type $(3,2)$. Any such identification must track the inverse on one generator and distinguish the kernel of the map to $\mathrm{Sl}(2,\mathbb Z)$ from the larger kernel of the map to its quotient by $\{\pm1\}$. This is a question for a separate algebraic comparison; no normalization has been made in the transcription.

18. **Scan 234, proof after (24); kind: unproved claim.** “il suffit de montrer que les premiers mbs satisfont les relations caractéristiques (20)” invokes uniqueness of lifts characterized by their powers. A full verification would identify the discrete central kernel and show that the relevant power constraints determine the lift uniquely.

19. **Scan 235, proof between (27) and Corollaire 1; kind: unproved claim.** “en induisant des iso identiques sur les facteurs extrêmes” is the decisive step of the comparison of exact sequences. Because the first displayed sequence does not explicitly begin with an injection, a detailed proof should verify infinite order of the abstract central element, or derive injectivity from its image in the second sequence, before invoking the comparison argument.

20. **Scan 235, final paragraph; kind: unproved claim.** “Je vais essayer de présenter le … groupe … avec trois générateurs involutifs” announces a second presentation to be constructed on the following pages. The algebraic task is to verify that the proposed involutions generate and that substituting them into (28) introduces neither extra relations nor an unintended quotient.

21. **Scan 236, opening paragraph; kind: unproved claim.** “engendrent un groupe isomorphe à $D_\infty$” is asserted for three pairs of elements. A verification must show that the rotation-like generator in each pair has infinite order and that conjugation by the indicated involution reverses it; the second property follows from the preceding formulas, whereas the first depends on the covering-group construction.

22. **Scan 236, (31)–(32); kind: unpursued implication.** The displayed “somme amalgamée de groupes” gives a route to normal forms and to an action on the tree associated with an amalgam. One could use that action to compare finite subgroups and involutions of the extended covering group; this is a research direction, not a classification established in these pages.

23. **Scan 236, (33); kind: unproved claim.** “Or on peut prendre … les générateurs involutifs” introduces the substitutions needed for the next corollary. A complete derivation should check that each proposed product squares to the identity and express the former generators back in terms of the new ones before transforming the defining relation.

24. **Scan 237, Corollaire 2 and (34); kind: unproved claim.** “admet une présentation (à trois générateurs involutifs …)” states the final presentation without a new proof on this sheet. Its proof is the elimination/substitution argument suggested by (33); an independent check should confirm the order of the factors in both products, since switching either pair replaces the associated element by its inverse.

25. **Scan 237, (34); kind: own idea. Confidence: medium.** Treat the product relation as a relation among three reflections and compare it with quotients obtained by separately setting the cubic and square factors equal to the identity. The reason to explore this is that the manuscript retains only their product as a relation, so those quotients may clarify precisely which central information the covering group keeps; no novelty or established identification is claimed.

26. **Scan 238, (37) and the sentence immediately following; kind: unproved claim.** “dont on sait que c’est un isomorphisme” invokes the identification of the mapping-class group of the once-punctured torus with the integral linear group. A complete argument should separate surjectivity, obtained from explicit mapping classes, from injectivity of the homology representation and should state whether orientation-reversing homeomorphisms are included.

27. **Scan 238, final paragraph; kind: unproved claim.** “l’action sur l’espace tangent s’identifie à l’action tautologique” is used to compare two extension constructions. The required verification is that the tangent action at the fixed origin, with its chosen orientation convention, induces the same action on the covering of directions as the linear representation; the announced conclusion continues on the next scan.

28. **Scan 238, notation between (36) and (37); kind: own idea. Confidence: high.** Audit the occurrence U_{1,0} against the surrounding definition U_{1,1}=X_1 minus {0} before using the argument in a later proof. The reason is the explicit mismatch on this page, not an assumption about which expression the author intended; the transcription deliberately leaves U_{1,0} unchanged.

29. **Scan 239, lines 6–10 — unproved claim.** The theorem states that the inverse image of the extension “s'identifie canoniquement” with `Gl(2,Z)^~`, referring back to the proposition on manuscript page 761. On this page the identification is asserted through that earlier reference; checking it would require tracking the extension kernel, its chosen generator, and the orientation convention in the preceding paragraph.

30. **Scan 239, lines 15–17 — conjecture / author question.** The parenthetical “(judicieusement ?)” explicitly questions the choice of a base point for computing the fundamental group. The subsequent lattice construction should be checked to see which choices make the actions of the displayed generators easiest to express.

31. **Scan 239, (39) — unproved claim.** The displayed identification involving “Aut ext” is stated without an argument on this page. A verification would need a precise interpretation of the handwritten `loc` subscript and a proof that the relevant peripheral structure is exactly the one preserved by the indicated automorphisms.

32. **Scan 239, presentations a), b) — own idea.** **Confidence: medium.** Once the cancellations have been resolved paleographically, compare the two presentations by substituting the involution products into the first presentation and checking each relation directly. This would detect a sign or inverse mismatch without allowing the algebra to dictate what the manuscript says; the reason for the suggestion is the dense overstriking in both displayed relations.

33. **Scan 240, (41) — unproved claim.** The statement “on aura” identifies `S T_{1,1}` with a normalizer of the cyclic subgroup generated by the boundary loop. A proof must specify whether the subgroup itself or its conjugacy class is fixed, and check the corresponding change from outer automorphisms to actual automorphisms.

34. **Scan 240, lines 6–16 — unproved claim / deferred calculation.** “Donc il faudrait expliciter l'action” announces a calculation of the displayed generators on `x` and `y`; no such formulas are supplied on this page. The required check is that the resulting automorphisms satisfy the presentations and carry the peripheral generator to itself or its inverse according to the stated cases.

35. **Scan 240, lines 10–13 — unproved claim.** The requirement “transformer” the peripheral generator into itself or its inverse is stated for the indicated generators: preserve `l′_0` for `rho~` and `sigma~`, and invert it for the involutions. Establishing this requires following the orientation of the peripheral loop through each geometric representative, including the paths used to return the base point.

36. **Scan 240, last paragraph — unpursued implication.** The “revêtement principal” with group `Z^2` offers a way to represent noncommutativity of the punctured-torus group as winding around deleted lattice points. The next page begins the relative-path description, but a full generator-action calculation remains to be extracted from that model.

37. **Scan 241, (42)–(44) — unproved claim.** The “iso. can.” and the exact sequence are stated through a mixed fundamental-group construction, and the path-pair calculation is credited to Jean Malgoire. A detailed verification should define the equivalence relation on pairs, the group multiplication and the injection of the fundamental group of the lattice complement.

38. **Scan 241, after (44) — unpursued implication.** The convention “compose comme les fonctions” fixes the order of multiplication for the path-pair model. This matters for every subsequent commutator and generator-action formula; a derivation must translate the geometric concatenation order into that convention explicitly.

39. **Scan 241, final paragraph and drawing — unproved claim.** The commutator loop is called “visiblement opposé” to the displayed peripheral loop. Its sign is argued pictorially here; a proof would compare the orientation of the square boundary with that of the radial loop while retaining the chosen multiplication convention.

40. **Scan 241, drawing — own idea.** **Confidence: high.** Independently compute the four endpoint displacements using `a=(1/2,1/2)` and compare them with every vertex label in the sketch. The visible `a-e_1` at the upper left and `a-e_0` at the lower right may reflect a local index interchange, because the nearby e_1 and e_0 lattice labels and the x/y arrows indicate the opposite coordinate displacements; this is an editorial check, not a correction to the transcription.

41. **Scan 241, (43) — own idea.** **Confidence: medium.** Use the plane with lattice points removed to construct generators for the kernel of the map to `Z^2`, then examine how deck translations move those generators. The reason is that (43) identifies the quotient with the abelianization and the sketch supplies a loop around one deleted point; extending the construction to every lattice point could make the kernel action explicit.

42. **Scan 242, after (46), unproved claim.** Grothendieck writes, “La composition des morphismes de germes est évidente.” A proof should show that representatives can be restricted so that they compose, and that the resulting germ is independent of those representatives and restrictions; the filter-compatibility condition is the relevant ingredient.

43. **Scan 242, (47) and final paragraph, conjecture / expectation.** The phrases “sans doute” and “au moins dans les ‘bons cas’” qualify the proposed interpretation of these coverings as coverings of a suitable limiting topos. The sentence continues on the next page; at this point the precise choice of topos and the hypotheses making the interpretation valid remain open.

44. **Scan 242, (47), own idea — medium confidence.** Clarify whether the displayed limit of categories is intended as a filtered 2-colimit and identify its objects and morphisms by eventual restriction. This is suggested by the analogous explicit limit of sets of morphisms in (46), but the categorical coherence data are not spelled out here.

45. **Scan 242, upper-left margin, own idea — medium confidence.** Work out the categorical role of the germ associated with the improper filter, which the note explicitly allows and calls “germe d’espace vide”. Domains can be shrunk to the empty set in that case; checking the resulting Hom sets would test the conventions against the proposed topos interpretation.

46. **Scan 243, upper-left margin; kind: conjecture/question.** The marginal question is tentatively read as “cela ne fait pas aller loin ?”; both substantive words remain doubtful. The point of the question cannot safely be identified more specifically than its position beside the proposed projective-limit description, and its wording should be settled before using it as evidence of a mathematical reservation.

47. **Scan 243, first paragraph; kind: unproved claim/expectation.** The category “dans les bons cas” “a tendance à être multigaloisienne, voire galoisienne.” A precise investigation would need to specify those good cases and establish the categorical axioms for the filtered category of coverings; the phrase itself supplies no hypotheses or proof.

48. **Scan 243, conditions 1° and 2°; kind: unproved claim.** The asserted reformulation beginning “Ce foncteur est pl. fidèle” uses eventual constancy on components and eventual triviality of induced exterior fundamental-group maps. A proof should state the local hypotheses under which coverings are classified by these groups and track the quantifier order; the inserted nonemptiness and containment conditions are part of the claim.

49. **Scan 243, condition 2°; kind: own idea.** Compare the condition with pro-triviality of a system of fundamental groups without interchanging the quantifiers over neighborhoods and coverings. **Confidence: medium**: the written condition requires one smaller neighborhood to kill the whole induced group map, whereas an individual covering might trivialize only after a smaller neighborhood depending on that covering; whether the two formulations agree needs checking in the intended category.

50. **Scan 244, first paragraph; kind: unproved claim.** The category of topological spaces “peut être considérée comme sous-catégorie pleine” of the category of germs by using the trivial filter. The associated assertion that the category of coverings restricts correctly to ordinary topological coverings needs an explicit comparison of the morphisms and pullback functors.

51. **Scan 244, (49)–(50); kind: unproved claim.** A morphism from a `1`-connected germ is used to produce a “foncteur fibre” and then `π_1` relative to it. The categorical construction should specify the needed exactness and detection properties of this functor in the multigaloisienne case, and the additional connectedness condition used for the subsequent equivalence of categories.

52. **Scan 244, bottom paragraph; kind: unpursued implication.** The explicit condition “Si X est 0-connexe” distinguishes recovery of the whole covering category from a base germ that selects a component. One can investigate how the construction varies between components without treating the single associated group as a description of the whole disconnected case.

53. **Scan 245, first paragraph; kind: unproved claim.** The assertion that the fundamental group “dépend fonctoriellement du triple” involves the morphism from the `1`-connected germ, not only its source and target objects. A proof should formulate morphisms between such triples and verify that the resulting homomorphisms are compatible with composition and with the chosen equivalence for constant coverings.

54. **Scan 245, residual-germ definition; kind: unproved claim.** “Il est vide ssi Y est ouvert” identifies when the residual filter becomes empty. The proof can be sought directly in the neighborhood-filter definition; it should keep the convention for an empty or improper filter explicit.

55. **Scan 245, NB sentence; kind: unpursued implication.** The assertion that the germ at a point is “tjrs 1-connexe” whereas the residual germ need not be isolates local punctured-neighborhood monodromy as the information retained by the latter. This suggests comparing local covering categories of ordinary and residual germs in concrete spaces, without inferring that the residual germ is always nontrivial.

56. **Scan 245, last assertion; kind: unproved claim.** “Tout germe d'espaces (S,Φ) peut s'interpréter” as a residual germ in `X=S∪{ω}` is stated without constructing the topology. A proof should specify neighborhoods of the added point and verify that their traces on `S` recover exactly the original filter up to germ equivalence.

57. **Scan 245, last assertion; kind: own idea.** Try adjoining `ω` with neighborhoods generated by `{ω}∪U`, where `U` runs through an open cofinal basis of `Φ`, while retaining the original open sets of `S`. **Confidence: high as a construction to check**, because it directly encodes the written filter; separation properties of the resulting space and any requirement of a proper filter must still be examined.

58. **Scan 246, middle paragraph; kind: unpursued implication.** “Je m'intéresse au choix d'un rev. universel” of the residual germ of a surface point identifies the local object motivating the digression. The role of a *choice* of universal covering, and the transformations between such choices, deserves comparison with the earlier lifted-group constructions without inserting that comparison into the transcription.

59. **Scan 246, lower paragraph; kind: unproved claim.** A covering represented over some `S_i∈Φ` defines a germ over the original germ that “ne dépend pas du choix” of representatives. A proof should pass to common refinements, construct the comparison morphisms, and establish their compatibility before obtaining the stated canonical functor.

60. **Scan 246, isomorphism parenthesis; kind: own idea.** Test the scope of “à isom unique près”: the intended uniqueness may concern the comparison induced by a *fixed* covering object and its refinements, rather than every isomorphism of the resulting germs. **Confidence: medium**, because coverings can have automorphisms, so an unqualified reading of uniqueness would need further structure; the inserted “au dessus de” may be relevant but by itself should not be treated as a proof.

61. **Scan 247, (54) and first paragraph; kind: unproved claim.** The canonical functor from coverings to germs over the base “est pleinement fidèle,” and its essential image defines an étale covering of the germ. A proof should check that every morphism of the resulting germs over the base descends to a morphism between covering representatives after a common refinement, not merely that covering morphisms induce germ morphisms.

62. **Scan 247, second paragraph; kind: unproved claim.** The `1`-connected objects are called universal coverings, and “ils forment un groupoïde, connexe ssi” the covering category is galoisienne. Establishing this requires both that morphisms between such objects are invertible and that the asserted connectedness criterion follows from the stated multigaloisienne hypothesis.

63. **Scan 247, bottom paragraph and formula; kind: unproved claim.** A universal covering “est bel et bien un germe d'espaces” that is `1`-connected, and the written formula identifies its associated fundamental group with its covering automorphism group. The comparison should be derived from the fiber functor and the full-faithfulness assertion, including the dependence on the chosen universal covering.

64. **Scan 247, vertical marginal note; kind: unpursued implication.** The note interprets the displayed group as the fundamental group of the “cat. multigaloisienne ‘abstraite’,” “calculé” at a `1`-connected object. This explicitly invites comparison of the geometric base-germ construction with the purely categorical one and of their behavior when several connected components are present.

65. **Scan 247, bottom formula; kind: own idea.** Audit the action and composition conventions in the comparison with the automorphism group of a universal covering; a representation by `Hom` can introduce an opposite-group convention. **Confidence: high that the convention must be checked, not that the written formula is wrong**, because the variance of the representing functor and the chosen left/right action determine the precise comparison.

### Literature checkpoints

66. **Scans 230–231, covering arguments; 243, conditions 1°–2° — own idea, literature checkpoint.** Compare the uses of covering classification with the hypotheses of Hatcher’s Theorem 1.38, which assumes path connectedness, local path connectedness, and semilocal simple connectedness (Hatcher, 2002, p. 67). **Confidence: high in the need for this check**, because a passage to germs or a filtered system does not by itself supply those hypotheses for every representative; this comparison is proposed only for the research argument.

67. **Scans 234–240, lifted presentations and peripheral automorphisms — own idea, literature checkpoint.** Use the braid-group and Dehn–Nielsen–Baer treatments in Farb and Margalit (2012) as comparison points for the presentation and for the distinction between outer automorphisms and automorphisms preserving a specified peripheral subgroup. **Confidence: medium**, because these pages also include orientation-reversing elements and a chosen lift, so any identification requires explicit choices of generators, action conventions, and central element.

68. **Scans 243–247, categorical reconstruction and final automorphism formula — own idea, literature checkpoint.** Compare the reconstruction discussion with SGA 1, Exposé V, §§4–5 and §9, while keeping its finite-set/profinite framework distinct from the category of coverings under consideration here (Grothendieck & Raynaud, 1971/2004). Section 5.1 explicitly discusses the opposite-group relationship between automorphisms of a fiber functor and of its representing pro-object. **Confidence: high that a variance check is required**, because the last formula on scan 247 identifies a fundamental group with a covering automorphism group; the citation supplies a convention to compare, not a correction of that formula.

### References

Farb, B., & Margalit, D. (2012). *A primer on mapping class groups*. Princeton University Press. https://press.princeton.edu/books/hardcover/9780691147949/a-primer-on-mapping-class-groups

Grothendieck, A. (1981). *La Longue Marche à travers la théorie de Galois* [Handwritten manuscript; supplied scans 229–247, Montpellier archive cote 140-4, file described as pages 650bis–787]. Université de Montpellier. The transcription’s primary source is the image packet supplied with the task.

Grothendieck, A., & Raynaud, M. (2004). *Revêtements étales et groupe fondamental (SGA 1)* (arXiv:math/0206203v2). arXiv. https://doi.org/10.48550/arXiv.math/0206203 (Original work published 1971)

Hatcher, A. (2002). *Algebraic topology*. Cambridge University Press. https://pi.math.cornell.edu/~hatcher/AT/ATchapters.html

The external references above were consulted only for these separate research checkpoints and bibliographic identification, not to determine or emend the manuscript readings. They do not amount to an exhaustive literature or novelty review.

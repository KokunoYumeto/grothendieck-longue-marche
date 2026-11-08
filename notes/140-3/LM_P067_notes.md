# LM_P067 — Transcription notes

## 1. Source, pagination, and conventions

This companion accompanies the diplomatic French transcription of the ten supplied images, `LM_P067_scan081.jpg` through `LM_P067_scan090.jpg`. The manuscript identification, year, and archive designation follow the supplied task sheet (Grothendieck, 1981); no published transcription, later manuscript pages, or external mathematical source was used to supply readings.

| Scan number | Visible upper author number | Secondary handwritten lower-left number | Printed archive page below the image |
| --- | --- | --- | --- |
| 81 | 329 | 80 | 80 |
| 82 | — | 81 | 81 |
| 83 | 330 | 82 | 82 |
| 84 | 331 | 83 | 83 |
| 85 | — | 84 | 84 |
| 86 | 332 | 85 | 85 |
| 87 | — | 86 | 86 |
| 88 | 333 | 87 | 87 |
| 89 | — | 88 | 88 |
| 90 | 334 | 89 | 89 |

The fragment starts with `\scanpage{81}`. Upper author numbers use `\mspage`; the smaller handwritten lower-left numbers use `\margin`, because their authorship cannot be established here. Printed archive footers, URLs, and institutional addresses are outside the manuscript transcription. No author page number has been supplied where none is visible.

The prescribed uncertainty, deletion, insertion, margin, emphasis, diagram, and figure macros are used without definitions: the deliverable is intentionally a fragment with no preamble. Standard mathematical LaTeX and `tikz-cd` encode the formulas and the clear extension diagram. The recurrent looped Latin letter is consistently encoded as `\ell`; this does not change its indices, powers, or multiplication order. The broad group glyphs, some Greek letters, and overwritten decorations remain explicitly uncertain. `|` inside `\unsure{...}` separates alternatives; it is not a manuscript mathematical bar. Counts in `\illegible{n}` are estimates of words or short mathematical items.

Source paragraph order is retained; display arrangement and line wrapping are typographic, not a facsimile of the sheet. Marginal-note placement follows the visible attachment where recoverable. Where an insertion's attachment itself is doubtful, that uncertainty is recorded below. A horizontal separator on scan 83 is encoded as a rule. Apparent grammatical and mathematical anomalies have not been corrected.

## 2. Table of doubts

**Confidence concerns paleographic reading.** High means the recorded marks are well supported, including when their mathematical content is surprising; medium means a plausible reading remains uncertain; low means substantial ambiguity or damaged/overwritten text. Repeated doubts are grouped in these tables, while the corresponding occurrences remain marked in the fragment. Approximate line positions refer to the handwritten source, not to lines in the LaTeX file.

### Scans 81–83

| Scan | Approximate line / location | Reading used | Alternatives / unresolved issue | Confidence |
| --- | --- | --- | --- | --- |
| 81 | 1 | `les` after “On construit” | The short final word is compressed; `le` is also possible. | medium |
| 81–83 | Recurrent cocycle symbol, starting scan 81, line 2 | `ζ` | `ξ`; the long descending stroke is clear, but its small upper strokes are not consistently separable. | medium |
| 81–83 | Recurrent exponent / parameter, starting scan 81, line 2 | `γ` | `δ`; the writer's looped form makes the letter identification uncertain. | medium |
| 81 | Diagonal NB, first half | `en détermine` | Verb ending and the following short item are uncertain; the following item is left illegible. | low |
| 81 | Diagonal NB, middle | Formula `ζ = ℓ₀^γ h₀⁻¹`, followed by `satisfasse (A)` | Parameter letters share the global ambiguities; the verb's ending is insecure. | low |
| 81 | Diagonal NB, last substantive line | `est unique` | The preceding three words and the full construction cannot be read securely. | low |
| 81 | Diagonal NB | Cancelled words | Approximately two cancelled words are illegible. | low |
| 81 | 9, after the definition of g | Cancelled `définit` | Middle and ending are obscured by the cancellation stroke. | medium |
| 81 | 13, “la seule équation délicate” paragraph | Possibly cancelled `pour`; `laquelle` | It is unclear whether “pour” is cancelled or retraced; the next word could be plural `lesquelles`. Neither grammar nor mathematical sense has been used to repair it. | low |
| 81 | 17, correction before “sur λ” | Cancelled `question`, replaced by underlined `condition` | The lower cancelled word and the exact correction layer are uncertain. | medium |
| 82 | 9, before u ∈ Γ | `sera` | The compressed verb has no secure alternative. | medium |
| 82–83 | Recurrent matrix-group name | `Sl` | `SL`; capitalization of the looped second letter is uncertain. | medium |
| 82 | 11, “réduisons le …” | Inserted `groupe` above a cancelled item | The cancelled item is not securely readable. | low |
| 82 | 11 onward, large extended-group symbol | `𝒢` | A separate tilde may be present, or the upper wave may belong to the calligraphic letter. | low |
| 82 | 12 | `équations` | Final plural stroke is uncertain; a singular reading is possible. | medium |
| 82 | 13, cancelled display | `ℓ₀³ = ℓ₁³ = ℓ∞³ = 1` | A further cancelled item at the right is unreadable. | low |
| 82 | 14 | `remplacé` | Interior and ending are compressed; no secure alternative. | medium |
| 82 | 15, permutation-group symbol | `𝔖₃` | `𝒮₃`; the calligraphic / Gothic font distinction cannot be resolved from this hand. | low |
| 82 | 18, first factor of the surviving cubic-relations display | `ℓ₀` | Retracing partly obscures the initial letter. | medium |
| 83 | 3, matrix-group coefficient ring | `Ẑ` | `ℤ`; the mark above the Z is retraced and might be a cancelled rather than surviving hat. | low |
| 83 | Before (61), substitution in (24 bis) | `h₀`, `ℓ₀` | `h∞`, `ℓ∞`; the compressed subscripts have two-lobed forms. These alternatives are marked independently of the clearer subscripts elsewhere. | low |
| 83 | (61)–(63), hatted map | `φ̂` (varphi rendering) | `ρ̂`; the loop and descending stem are not fully distinguishable. | medium |
| 83 | Between the parameter tuple and “satisfaisant” | One small illegible marginal item | The isolated mark's text and attachment are unclear. It is retained separately. | low |
| 83 | (62), underbrace label | `h` | `h₀`; no subscript can be recovered confidently. | low |
| 83 | (62), before g₀ in the third row | Cancelled illegible term | Approximately one mathematical item, obscured by crosshatching. | low |
| 83 | Tuple immediately before (63) | `(ζ, r, s)` | The second and third entries could be overwritten `γ, β`; alternatives remain explicit. | low |
| 83 | Right-side note beside (63) | `donc` | `avec`; initial strokes are compressed. The opening parenthesis is retained without supplying an unseen closing parenthesis. | low |
| 83 | Last paragraph | `λ` | The first occurrence is heavily retraced. | medium |
| 83 | Last paragraph, after λ′ = | Cancelled illegible term | Approximately one mathematical item before the surviving product. | low |

### Scans 84–86

| Scan | Approximate location | Reading retained | Alternatives or nature of doubt | Confidence |
|---|---|---|---|---|
| 84 | Heading and (1) | Large group glyph as calligraphic G, with an explicit alternative adding a tilde | The upper wave may be part of the letter rather than a separate diacritic; alphabet unresolved | low |
| 84–86 | Heading; finite permutation group throughout | Fraktur S, alternatively calligraphic S | Handwritten alphabet not securely distinguishable | medium |
| 84 | Heading and identification under (1) | Capital Pi with subscript 1, alternatively lowercase pi | The fundamental-group letter has straight, tall legs; case uncertain | medium |
| 84 | Heading, equivariant fundamental-group expression | `{1, τ}` | The two elements and comma are heavily overwritten | low |
| 84 | Left marginal note, beside heading and §I | “défini comme Aut” with subscript “lac” or “loc” | Subscript, “on en donne cinq,” “définitions,” and the concluding parenthesis are insecure; about three words are left illegible, as is one deleted word | low |
| 84 | §I, about l. 7 | “présenté” | Final letters and accent are cursive strokes | medium |
| 84 | Below definition of the punctured sphere, about ll. 12–13 | Deleted “par autom. holomorphes” | Middle abbreviation may be a longer form of “autom.” | medium |
| 84 | Beside the overwritten subgroup notation, about l. 16 | `(2)` and deleted S-subscript-3 glyph | The small parenthesized mark may be an abandoned number; deleted group glyph only partly recoverable | low |
| 84 | “est le sous-groupe des … conformes,” about ll. 16–17 | “automorphismes” or “éléments” | Several superimposed strokes prevent separation of the underlying versions | low |
| 84 | Enumeration before (2), about l. 19 | Identity entry as “id” or “1” | Short dark entry before the three transpositions is overwritten | low |
| 84 | Enumeration before (2), after dotted rho | One deleted symbol left illegible | Cannot distinguish the crossed symbol from pen correction | low |
| 84 | Insertion above the first formula in (2) | `=1+1/(1−z)`, alternatively `=1+1/(z−1)` | Denominator order must not be chosen from the algebraic identity | low |
| 85 | Above number (6) | One deleted item left illegible | It may be an abandoned equation number | low |
| 85 | (6) | Dotted taus without primes; rho without a visible dot | Later lines use other decorations; the transcription does not supply the missing marks | high |
| 85 | About ll. 5–6 | “antiinvolutions” or “anti-involutions”; “données” | Possible hyphen and faint final strokes | medium |
| 85 | (7), first two left sides | Dotted, primed tau-subscript-0 and tau-subscript-1, evaluated at z | Symbols have been overwritten, particularly the prime and first argument | medium |
| 85 | Sentence introducing fixed points, about l. 8 | Deleted “dans U-subscript-0,3”; one small insertion and two deleted items left illegible | Carets and dense cancellation overlap “des autom. conformes de” | low |
| 85 | Right of (8) | Ordinal suffix “ième,” alternatively “ème,” for 3 and 6 | Very compressed superscript handwriting | medium |
| 85 | Insertion above the first circle in (9) | `={z : z+z̄=zz̄}`, followed tentatively by `=1/z` or `=1/2`, and then `=1/2−U` | The terminal upper fraction may be `1/z` or `1/2`; the fraction structure and relation of the stacked insertions remain insecure. No algebraic correction has been made | low |
| 85 | Sphere interpretation, about l. 18 | Deleted “symétries,” inserted underlined “réflexions” | Cancelled word is obscured; number of emphatic underlining strokes is difficult to distinguish from the cancellation | medium |
| 85 | Same line | Inserted “gr” with raised “ds,” alternatively “grands,” before “cercles” | Abbreviated versus fully written form uncertain | medium |
| 85 | Sphere drawing | Pole labels and six equatorial labels supported; three primed-tau labels tentative | Curves, arrowheads, letters, and shading overlap; about two interior labels remain illegible | low |
| 86 | About l. 5, cancellation | “Prenant” or “Prenons un de” | Final syllable of the first deleted word crossed out | low |
| 86 | Above the same cancellation | “(C'est aussi” or “(C'est ainsi” | Short inserted adverb consists largely of strokes | medium |
| 86 | About l. 8 | “déterminés” | Ending is compressed | medium |
| 86 | (11), first underbraced product | Initial tau, then dotted primed tau-infinity, then tau | The initial tau is overwritten and may have been cancelled; all visible factors are retained, with doubt attached | low |
| 86 | (11), final underbraced product | Tau followed tentatively by dotted primed tau-0, then an illegible cancellation | Subscript and cancellation are densely overwritten | low |
| 86 | Generator list between (11) and (12) | Exponent `−1`, alternatively `1`, on dotted rho | Small dark superscript cannot be separated reliably | low |
| 86 | (12) | Unsubscripted dotted sigma squared | No subscript can be seen; it has not been supplied | high |
| 86 | Subgroup identification after (13), about l. 20 | Final calligraphic T-subscript-0,3 | Letter/decorations of the final group designation remain uncertain | low |
| 86 | Signature condition, about l. 22 | `sg(g)` or epsilon evaluated at g | Signature notation is overwritten and has a long descending stroke | medium |
| 86 | Bottom-left marginal note | “étant les” or “étaient,” followed by “notés précédemment” | First words do not resolve securely | low |
| 86 | Same marginal note | Sigma-0, sigma-1, sigma-infinity, alternatively with bars | Long upper strokes may be part of the sigmas rather than separate bars | low |

### Scans 87–88

| Scan | Approximate line / position | Reading in the transcription | Alternatives / qualification | Confidence |
|---|---|---|---|---|
| 87–88 | Throughout | `\unsure{\mathcal G\|\widetilde{\mathcal G}}` | The broad upper wave may belong to the handwritten calligraphic capital rather than be a separate tilde. Both the letter's exact alphabet and the accent remain uncertain. | medium |
| 87 | Top, before l. 1 | Deleted `(14)` | An overwritten earlier label; its digits are uncertain. | low |
| 87 | L. 1, deletion above `identifie` / `ces` | Deleted `plonge` | It may be a different cancelled verb. The exact attachment of this cancelled reading is uncertain. | low |
| 87 | Ll. 1–2 | `au`, replaced by inserted `à des éléments du` | The insertion's connector points before `groupe`; the clause is a revision, not a supplied grammatical repair. | high |
| 87 | L. 2, long struck clause | Several illegible words around the large group symbol | No lexical reconstruction attempted. The number of deleted words is an estimate. | low |
| 87 | L. 2, group membership | `\mathfrak S'_3` or `\mathcal S'_3` | Ornate capital; the precise typographic alphabet is not securely distinguishable. | medium |
| 87 | L. 3, before `g(x)` | `pose` | `par` is the other plausible reading. | medium |
| 87 | Eq. (14), second row | Dotted or undotted `\tau'_0` in its three occurrences | The small marks above these three symbols look like dots; the other rows are undotted. This unevenness has not been normalized. | medium |
| 87 | Eq. (14), final entry | `\tau'_\infty(\ell_0\|\ell_\infty)=\ell_1^{-1}` | The input subscript is a dark loop/blob. The right-hand subscript looks like 1. No replacement with a mathematically expected entry has been made. | low |
| 87 | Eq. (15), parenthesis | `({\tau'_\infty})^2` | The prime on the last tau in the involution chain may be absent; the alternatives are marked. | medium |
| 87 | Eq. (15), above the parenthesis | Inserted `on a` after `et bien sûr` | These tiny words are written above the power identities and have been retained. | high |
| 87 | Between (15) and following paragraph | Inserted `Dans` before `Le groupe` | The word is circled, with a curved connector to the paragraph below. A colon remains beside (15). | high |
| 87 | Ll. 9–10 | `définit` | The verb is clear in outline; its accent is not securely separable from the quick strokes. | medium |
| 87 | Eq. (16), final row | The overwritten `\ell_1` entries | The subscripts have been heavily rewritten; 1 is the proposed reading. | medium |
| 87 | Eq. (18), first chain | `\rho\ell_0 = [deleted mark] \ell_1\rho` | The segment after the second equality is overwritten. The surviving `\ell_1\rho` remains tentative. | low |
| 87 | Eq. (18), last chain | `\ell_0\rho^{-1}` | The exponent −1 is visible; it has been preserved even though a nearby pattern could tempt a different reading. | high |
| 87 | L. 21, definition of `\tau_i` | Inserted `=\tau'_i\sigma_i` | The formula is written above and to the right of the main definition, with a curved placement mark. | high |
| 87 | L. 18, end | `de` | `des` is possible at the end of `au dessus de[s]`. | medium |
| 87 | Ll. 21–22 | Deleted `donc`; inserted `de carré 1` before `et de commuter` | The words lie below the parenthetical phrase after the definition, but a curved placement line appears to point to `et` in the characterization below. Attachment to the earlier parenthesis remains possible; the word-reading is substantially firmer than the placement and punctuation. The earlier opening parenthesis is retained without supplying an editorial closing parenthesis. | low |
| 87 | L. 22, above and below underlined characterization | Illegible deleted material, including a group-membership expression | Scribbles and horizontal strokes overlap. The transcription does not attempt to recover the entire earlier formulation. | low |
| 87 | Ll. 22–23 | `\tau_i est caractérisé` | `caractérisé` and the extent of the underline are partly obscured by revisions. | medium |
| 87 | Lower left marginal note beside ll. 22–24 | `rappeler pourquoi on a cette caractérisation` | The first three short words are faint and oblique; the final word is underlined and clearer. | medium |
| 87 | Final two lines | `topologique` | The word is split across the line and its opening is very compressed. It remains marked rather than accepted from context. | medium |
| 87 | Final line, parenthetical reference | `[C]` | `[TC]` is also possible; the initial bracket/stroke is indistinct. No identification of the referenced item is asserted. | low |
| 88 | Eq. (22), first definition | Tiny `dfn` over the equality | `déf` is possible. Its exact horizontal attachment is also imprecise. | low |
| 88 | Eq. (22), first row, after `\rho\sigma_1` | Illegible struck symbol | The erased material is too dark to decipher. | low |
| 88 | Eq. (22), second row, definition | `\sigma_0` | This symbol is rewritten; the surviving subscript looks like 0. | medium |
| 88 | Eq. (22), third row, second squared product | `(\rho\sigma_\infty)^2` | The overwritten subscript may instead be 0; the literal ∞-like shape and the alternative are both recorded. | low |
| 88 | L. 8 | `\mathcal T_{0,3}` | The script-like capital might be an ordinary handwritten T. | medium |
| 88 | L. 9 | `involutifs` | The final strokes are compressed. | medium |
| 88 | L. 9, cancelled count | Deleted `et quatre`, replaced by inserted `deux` | `quatre` is partly crossed through; `deux` is clear. | medium |
| 88 | Between ll. 9–10 | Inserted `et deux d'ordre 6` | The placement mark leads between the two order-three elements and the two following products. | high |
| 88 | Above l. 12 | Inserted exception beginning `Sauf les deux derniers` | The black interline note qualifies the sentence about lifting every element. Its natural attachment is before that sentence; no separate insertion caret is fully visible. | medium |
| 88 | L. 12 | `Nous avons relevé` | `avons` is almost reduced to a few low strokes; the ending and accent of `relevé` are also faint. | medium |
| 88 | L. 14, after conjugation phrase | `de` | `des` remains possible. | medium |
| 88 | L. 16, before `U=U_{0,3}^{an}` | `dans` | `de` is also possible. | medium |
| 88 | L. 17 | `topologiques` | Compressed middle letters and final ending, although the general outline supports this reading. | medium |
| 88 | L. 19, chosen lifts in the parenthesis | `\tau_0,\tau_1,\tau_\infty` without primes | No primes are visible. They have not been supplied to match the preceding list of dotted primed taus. | high |
| 88 | L. 20 | `le plus commode` | The article reads `le`; it has not been changed to agree with the preceding `façon`. | high |
| 88 | L. 23 | `correspondants` | `correspondantes` is possible because the ending is compressed. | medium |
| 88 | Ll. 23–25, poles | `-\bar j,-j`; chosen pole `-\bar j` | The minus before the chosen pole is present; it must not be dropped. | high |
| 88 | Final two lines | `peuvent`, `conjuguant` | The verb endings are cursive strokes rather than separately visible letters. | medium |

### Scans 89–90

| Scan | Approximate line / location | Reading used | Alternatives / unresolved issue | Confidence |
| --- | --- | --- | --- | --- |
| 89 | 1, insertion above (23) | `ρ l₁⁻¹` | Heavily overwritten final factor; a residual stroke after the exponent is not securely interpretable. | medium |
| 89 | 1, third conjugate in (23) | `τ∞⁻¹` | The exponent on the final factor is extremely faint. | medium |
| 89 | 4 | `corollaires` | The middle and ending are fluent strokes; no secure alternative. | medium |
| 89 | 10 | `relatifs` | Plural ending indistinct. | medium |
| 89 | 11, deletion before inserted “deux orbites” | `pts` plus one illegible item | The crossed original wording cannot be reconstructed securely. | low |
| 89 | 16 | `𝒢` / `G̃` with subscript 0,3 | Upper wave may belong to the calligraphic letter rather than be a distinct tilde. | low |
| 89 | 17 and 23 | `𝔖₃′` / `𝒮₃′` | Letter family of the looped symmetric-group symbol is uncertain. | low |
| 89 | 17, “De …” | `m̄` | `=`; the upper stroke is straight, the lower slightly wavy. It may be the manuscript's abbreviation for “même.” | medium |
| 89 | 24, last line | `trouve` | `trouvera`; final strokes are overwritten. | low |
| 90 | 3, heading at right edge | `triangul-` | May be an abbreviated or compressed ending of “triangulé”; no expansion made. | low |
| 90 | 4, header formula | `ℙ_C^{1∘}` | The small upper mark could instead be a filled dot; the transcription offers both. | low |
| 90 | 5, far right | `avec` | Word partly compressed by page edge. | medium |
| 90 | 6, before “générateurs” | deleted illegible item | A short overwritten start cannot be read securely. | low |
| 90 | 7–8, corrected description of `σ_i` | deleted `fait échange`, inserted `change`, inserted `de dim i` | This correction has several overlapping layers. The inserted “de” is visible, but the short next item is only tentatively `dim`; no terminal point is secure. Cancelled intervening wording is left illegible. | low |
| 90 | 9, deleted word before inserted “chgts d'orientation” | `passages` | Ending and following cancelled strokes uncertain. | low |
| 90 | 9 | `tangentielle` | `tangentielles`; final stroke could be an s. | medium |
| 90 | 12–13, (25), and 15, products of generators | primed `σ₀`, `σ₁`, `σ₂` | The strong overtracing and small marks may contain a different accent or no prime. Whole affected expressions remain marked. | low |
| 90 | left margin beside (25) | `σ∞′`, `σ₂′` | Same prime/overtrace uncertainty. | medium |
| 90 | left margin, last two lines | `carrément`; `r₀,r₁,r∞` | Alternative letter reading `σ₀,σ₁,σ∞`; the letter family cannot be established visually. | low |
| 90 | 14, inserted parenthesis after “d'indice 2” | `triangul'` | The abbreviation ending is unclear. A crossed prior subgroup label is left illegible. | low |
| 90 | 15, underneath generator definitions | `= l∞′`, `= l₀′`, `= l₁′` | Short doubled strokes connect the main symbols to the labels below; interpretation as equalities is marked. | medium |
| 90 | 15, third product | `σ′` | `σ`; a dark mark to the right may not be a prime. | low |
| 90 | 17, (26) | deleted illegible factor after `ρ_s` | Crosshatching prevents reading the cancelled term. | low |
| 90 | 19–22, formula label | `(27)` | `(17)`; first digit compressed/overwritten. | medium |
| 90 | 23, before “cet homomorphisme” | deleted illegible word | Possibly an abandoned start, but no secure reading retained. | low |
| 90 | bottom cancelled formula label | `(28)` | `(27)` also possible. | low |

## 3. Abbreviations and compressed forms encountered

Expansions are editorial interpretations supplied **only in this list**. An uncertain form is not expanded in the transcription. A few mathematical labels and unresolved cross-references are included for clarity.

| Form as written / tentatively read | Proposed expansion or function | Location / qualification |
| --- | --- | --- |
| `i.e.` | *id est*; c'est-à-dire | Scans 81–82, 86 |
| `NB`, `NB.` | *Nota bene* | Repeated, including margins |
| `mod` | modulo; in prose, a qualification of equivalence | Scans 82–83, 88 |
| `bis` | Supplementary or repeated numbering | “24 bis,” scan 83 |
| `Sl` / `SL` | Special linear group | Scans 82–83; capitalization uncertain |
| `Gl` | Groupe linéaire | Scan 84 heading |
| `GP` | Probably groupe projectif | Scan 84 reads `GP(1, Z)`; this expansion is interpretive |
| `an` in superscript | analytique | Repeated mathematical notation |
| `autom.` | automorphismes | Scans 84–85, 88; less secure in cancelled text |
| `Aut` with subscript `lac` / `loc` | Probably automorphismes de lacets | Scans 84, 87; the scan 84 subscript remains uncertain |
| `cf.` | *confer*; voir | Scan 84 marginal note |
| `p.r.` | par rapport | Scans 85–86 |
| `pt`, `pts` | point, points | Scans 85–86, 88–89 |
| `syst.` | système | Scan 86 |
| `gr` with raised `ds` | grands | Scan 85; the full word is an alternative reading |
| `id` | identité | Scan 84; `1` is an alternative reading |
| `sg` | signe / signature | Scan 86; the symbol may instead be epsilon |
| `dfn` / `déf` | Définition / a mark meaning “defined as” | Scan 88, (22); exact form uncertain |
| `m̄`, encoded `\overline{\mathrm m}` | même | Scan 88 |
| `De m̄` / `De =` | Probably de même | Scan 89; equality-like mark remains ambiguous |
| `[C]` / `[TC]` | Unresolved cross-reference | Scan 87; not identified with an external source |
| `conn.` | connexes | Scan 89 |
| `ens.` | ensembles | Scan 89 |
| `resp.` | respectivement | Scans 89–90 |
| `chgts` | changements | Scan 90 |
| `dim` | Probably dimension | Scan 90; short inserted item is uncertain; no terminal point is secure |
| `cart.` | cartographique | Scan 90 |
| `triangul-`, `triangul'` | Possibly compressed forms of triangulé | Scan 90; endings uncertain and not expanded |

## 4. Legibility and limits

The main prose and uncorrected formula rows are often readable after enlargement. The weakest material is scan 81's diagonal NB, scan 84's diagonal note beside the heading, scan 85's stacked additions over (9), scan 86's overwritten products in (11) and bottom note, scan 87's revised characterization and introduction, and scan 90's corrected account of a map frame. These passages contain intersecting strokes, retracing, or nearly vanished word endings; they should be treated as provisional readings.

Dots, primes, small subscripts, the broad calligraphic group letters, the long cocycle symbol, and the exponent letter on the opening pages need particular caution. The sphere drawing is described rather than reconstructed; interior operator labels that overlap the curves remain doubtful. The insertion “de carré 1,” on scan 87 is placed in the characterization using its curved leader, but the alternative attachment is documented. The source's missing or surprising decorations have not been filled in to make adjacent formulas agree.

Each page received a full reading followed by comparison of its transcription with the image; selected difficult passages received a second independent reading. This process cannot make the remaining low-confidence passages authoritative. Formula references (B), C, and (24 bis), and the continuation at the end of scan 90, are not reconstructed from absent pages. A temporary LaTeX harness was used to check syntax; its macro definitions and compiled output are not part of the deliverable.

## 5. Research notes — English, separate from the transcription

These notes distinguish the author's questions, expectations, assertions without a proof on the supplied page, and deferred work from editorial implications and proposed investigations. **“Unproved claim” means that a proof is not supplied in this passage; it does not mean that the claim is unproved elsewhere.** No suggestion is presented as a new result or as established mathematics. All scan, formula, and approximate-line locators below are pinpoint references to the supplied primary source, Grothendieck (1981). Brief quotations preserve the source wording where it is secure; uncertain quotations are identified as such.

### Scans 81–83

1. **Scan 81, diagonal NB — conjecture / question.** The note opens “Il faudrait s'assurer” and ends “À éclaircir!”; it appears to ask about recovering a parameter from g₀, but several intervening words are not secure. The exact uniqueness or determination question should be re-established from the source and the preceding definition before any proof is attempted.

2. **Scan 81, lower paragraph — unproved claim / stated difficulty.** Grothendieck identifies the existence of a solution as “problématique” and singles out “l'équation C,” together with a unit condition on the exponent. A proof or counterexample would require the exact earlier equations (B) and C; these pages do not supply enough information to reconstruct them safely.

3. **Scan 81, final line, continuing scan 82, first paragraph — conjecture / expectation.** “Je prévois” introduces an expected choice between the two cases of (B) according to whether p modulo 3 is 1 or −1. The congruence calculations on scan 82 state the restriction, but these pages do not complete a proof that it selects the asserted branch of (B).

4. **Scan 82, “Pour le tester” paragraph; scan 83, opening — unproved claim / deferred calculation.** The proposed test is a reduction involving cubic relations and then reduction modulo 6; the next page postpones the required identification of σ∞ and ρ with the words “explicitation que nous ferons tantôt.” To carry out the test, one would need those exact matrix representatives, the meaning of the prime on the matrix-group notation, and compatibility of the proposed operator with the quotient.

5. **Scan 83, (61)–(63) — unproved claim / proposed parametrization.** “On pense donc que u correspond à” introduces a parameter tuple, after which g₀ is eliminated. A complete treatment would separate the algebraic elimination from the existence, sufficiency, and possible uniqueness of the proposed correspondence; the preceding definition of the hatted map is required and is not supplied here.

6. **Scan 83, final paragraph — unpursued implication.** The text records how a change of λ affects the long cocycle symbol by left and right multiplication with powers of the peripheral generators. This suggests checking which parts of the displayed parameter system are invariant under that change, while retaining the manuscript's order of multiplication.

7. **Scan 82, reduction modulo 6 — own idea.** Once the matrix representatives and quotient conventions are recovered, enumerate the finite quotient and test the two congruence classes separately. **Confidence: high as a finite verification strategy, not as a proof of the full profinite statement.** The page proposes this reduction explicitly, but a successful finite check would still need a separate argument to control the original group.

8. **Scan 83, (62)–(63) — own idea.** Perform the elimination in both directions in a formal noncommutative calculation, keeping every exponent and inverse in its written order. **Confidence: medium.** The displayed expressions make the forward substitution testable, while equivalence and reconstruction may require hypotheses from earlier pages and a secure reading of the hatted map.

### Scans 84–86

1. **Scan 84, heading — unproved claim.** Under “Récapitulation sur le groupe,” Grothendieck displays identifications among the extended group, equivariant fundamental-group constructions, the quotient of `Gl(2, Z)` by `{±1}`, and `GP(1, Z)` (Grothendieck, 1981, scan 84, heading). Their construction is not given on this page. A proof would need compatible definitions of the orbifold action, basepoint, and central quotient; the uncertain action-group entry in the heading should be resolved before using the complete chain.

2. **Scan 84, (1) — unproved claim.** The group is given “comme une extension” of the finite symmetry group by the punctured-sphere fundamental group (Grothendieck, 1981, scan 84, (1)). A proof would need an explicit projection, identification of its kernel, and verification of the asserted quotient action. This is stated in a recapitulation, so earlier pages may contain the construction.

3. **Scan 84, (2)–(4) — unproved claim.** The listed transformations are “donnés par les formules explicites,” and their composition and conjugation identities are then recorded (Grothendieck, 1981, scan 84, (2)–(4)). Direct composition, with a fixed convention for order of composition, could check the relations independently. The crowded insertion above the first formula in (2) should be treated as a separate textual uncertainty rather than a reason to alter the displayed transformation.

4. **Scan 85, margin beside (9) — unproved claim.** The marginal “NB” asserts that the fixed-point sets of the two conjugation-twisted rotations are empty (Grothendieck, 1981, scan 85, marginal note beside (9)). A proof could solve the corresponding conjugate equations on the projective line, explicitly considering infinity. This would also clarify how these two anticonformal symmetries differ from the three displayed reflection involutions.

5. **Scan 85, paragraph after (9) — unpursued implication.** “L'image la plus suggestive” is the Riemann-sphere picture, with the four involutions interpreted as reflections in an equator and meridians (Grothendieck, 1981, scan 85, paragraph after (9)). The phrase “sans doute” here expresses a preference for a geometric picture rather than a formal conjecture. A precise reconstruction would need to specify the sphere model in which the stated fixed circles become great circles and match the six labeled equatorial points.

6. **Scan 85, (7)–(9) — own idea. Confidence: high as a checking method, not as a claim about the obscured reading.** One could make a separate symbolic consistency ledger: derive each fixed locus directly from its displayed anticonformal map and compare the result with the uncorrected and inserted versions of (9). The reason is that (7) supplies explicit maps while the final stacked insertion in (9) is too uncertain to identify confidently. Such a ledger should remain outside the transcription and should record discrepancies rather than repair them.

7. **Scan 86, opening paragraph — unproved claim.** The four circles are said to yield “12 triangles sphériques,” fundamental domains permuted “de façon simplement transitive” (Grothendieck, 1981, scan 86, opening paragraph). A proof would require identifying the intersections and chambers, checking their stabilizers, and distinguishing the action on chamber interiors from the action on their boundary points. The barycentric-subdivision description offers a possible route to that verification.

8. **Scan 86, (11)–(12) — own idea. Confidence: medium.** The asserted “syst. de générateurs” suggests comparing the reflection presentation with a finite triangle-group or Coxeter presentation, then deriving the orientation-preserving subgroup presentation (Grothendieck, 1981, scan 86, (11)–(12)). The reason for medium confidence is that the first and last products in (11) are overwritten, and (12) visibly contains an unsubscripted sigma. The comparison is a proposed check of the author's intended algebra; it cannot license reconstructing the ink.

9. **Scan 86, §II and (13) — unproved claim.** The three loops are “liés par la relation génératrice” in the displayed order `l∞ l1 l0 = 1` (Grothendieck, 1981, scan 86, (13)). A proof should use explicit based loops and orientation conventions, since those choices determine the order of the product. The current page does not draw those loops.

10. **Scan 86, paragraph after (13) — unproved claim.** The subgroup described as the “stabilisateur de” the chosen nonreal basepoint is said to act on the fundamental group, with its six operations named (Grothendieck, 1981, scan 86, paragraph after (13)). A proof would need to check that the stated parity condition indeed fixes the basepoint and produces based automorphisms, then compare the geometric symmetries with the listed operations. The signature symbol and final group designation remain transcription doubts.

11. **Scan 86, the two finite subgroups — own idea. Confidence: medium.** The conformal subgroup discussed before §II and the basepoint stabilizer discussed after (13) may provide a useful way to organize the two families of involutions appearing in the notation. Comparing their generators as explicit transformations could separate geometric fixed-point data from choices of lifts to based automorphisms. The reason for medium confidence is that the distinction is supported by the two descriptions on the page, but the decorations and the concluding marginal reminder are not fully legible; no general equivalence or novelty is asserted.

### Scans 87–88

1. **Scan 87, equations (17)–(18); kind: unproved claim.** Under “On a,” the text lists conjugation and product identities without a derivation on this page. A verification would evaluate both sides on loop generators while retaining the manuscript's multiplication convention. The overwritten first chain in (18) and its visibly surprising final exponent should be settled paleographically before using the formulas in a proof.

2. **Scan 87, characterization beside equations (19)–(20); kind: unproved claim.** The text characterizes the chosen lift by being over `\tau` and by “de commuter à `\sigma_i`”; the marginal reminder is provisionally read as “rappeler pourquoi …”. A proof must establish uniqueness within the specified coset, not merely check that the displayed product has the stated commutation and order properties. The marginal wording remains a paleographic uncertainty, while the mathematical characterization is plainly present.

3. **Scan 87, final two lines; kind: unproved claim / deferred work.** “Pour bien faire, il faudrait expliciter” introduces a request for a description of the listed `\sigma_i,\rho,\tau'_i,\tau_i`; the adjective is provisionally read as *topologique* and the cross-reference as `[C]`. A reconstruction should specify representative paths and basepoint choices, and then compare the induced actions with (14)–(21). The uncertain adjective and reference should not be used to identify an external source without further manuscript evidence.

4. **Scan 88, immediately after equation (22); kind: unproved claim.** The underlined “caractérisé” asserts that the element over `\dot\sigma_i` is characterized by `\varepsilon_i^2=\ell_i`. A proof must separate the existence supplied by the explicit product from uniqueness among elements of the designated coset. This may require a centralizer or root-uniqueness argument in the precise group used here; no such proof appears on this page.

5. **Scan 88, interline exception and starred marginal note; kind: unproved claim.** “Ce n'est pas possible” excludes the final two elements from the statement about lifting elements with the same order, and the marginal formula records empty fixed-point loci for the two order-six transformations. Checking this requires both the fixed-point calculation for the two antiholomorphic actions and the connection between fixed points and order-preserving lifts. The order of composition must be taken from the manuscript, not assumed.

6. **Scan 88, paragraph beginning “On sait que”; kind: unproved claim.** The text identifies conjugacy classes of same-order lifts with “composantes connexes des pts fixes” of the corresponding topological automorphisms. A proof would construct the path-based extension, track the change under conjugation by `\Pi_{0,3}`, and verify the order condition. This is the structural assertion behind the subsequent counts of possible lifts.

7. **Scan 88, lower half and final line; kind: unproved claim.** The text says “il y en a trois” for the lifts over `\tau` and gives two choices for the two order-three elements, corresponding to the two displayed poles. It then says that the lifts attached to the other pole can be obtained by conjugating with a `\tau_i`. A verification should identify the relevant connected fixed components on the punctured sphere and check the pole-interchanging action of that conjugation.

8. **Scans 87–88, action tables and lift classification; kind: own idea.** After the doubtful indices have been resolved from the images, a symbolic calculation on reduced free-group words could audit the displayed automorphism identities and expose convention-sensitive discrepancies. **Confidence: high as a checking method**, because such an audit can compare images of generators without replacing the manuscript's formulas by expected ones. It would be a separate verification layer and must never silently change the diplomatic transcription.

9. **Scan 88, conjugacy-class classification; kind: own idea.** One could try to express the order-preserving lift problem as a cocycle problem for the relevant finite cyclic action, then compare that algebraic description with the fixed-component description stated here. **Confidence: medium**, because the discussion of lifts modulo `\Pi_{0,3}`-conjugation suggests this formulation, but the precise extension, action conventions, and geometric hypotheses still have to be specified. This is a proposed route for examination, not a claimed new result.

### Scans 89–90

1. **Scan 89, lines 1–3, (23) — unproved claim.** The three displayed elements are said to be “d'ordre 3,” mutually “Π₀,₃-conjugués,” but “non Π₀,₃-conjugués à ρ.” A verification would need to distinguish conjugation by the ambient extension from conjugation by its normal subgroup, and then verify the nonconjugacy assertion; checking the displayed conjugation identities alone would not establish the last point.

2. **Scan 89, lines 4–8, (24) — unproved claim.** Grothendieck invokes “la théorie générale” and the claim that the connected components of the fixed-point sets here are “1-connexes,” then displays trivial fixed subgroups of Π₀,₃ for the listed operators. A full justification would need the precise fixed-point/lift correspondence being invoked and a topological verification of the connected components in each listed case.

3. **Scan 89, lines 9–18 — unproved claim.** The stabilizers of the two exceptional orbits are stated to have orders “4 resp. 6,” and a stabilizer is described as “bel et bien relevé multiplicativement.” One could verify both the stabilizer action and the relations of its chosen lifts; preserving the distinction between dotted quotient operators and undotted lifts is essential, especially where the ink is ambiguous.

4. **Scan 89, lines 19–24, continuing scan 90, lines 1–2 — unproved claim.** The passage says that the conjugacy classes of a lifting “correspondent aux pts fixes,” then distinguishes one fixed point for one stabilizer from two for the other. The stated transition to the other class by conjugating with any τᵢ should be checked against that correspondence, including why the result is independent of the chosen i at the level of Π₀,₃-conjugacy classes.

5. **Scan 90, lines 12–22, (25)–(27) — unpursued implication.** The involution presentation, its subgroup “d'indice 2,” and “le quotient de Π₀,₃ par l₁²,l∞³” are placed next to each other. An explicit derivation of the subgroup presentation and of the stated generator images would make the relationship precise; because the primes are heavily retraced, this should begin with renewed examination of the source, not a correction of the displayed relations by mathematical expectation.

6. **Scan 90, line 23 — unproved claim / deferred continuation.** The final words, “cet homomorphisme se prolonge en,” announce an extension whose target is not present on this supplied page. This is a continuation to consult later in the manuscript; no target or extension property has been supplied editorially.

7. **Scan 89, (23)–(24) — own idea.** Construct the relevant lift action on a universal cover and compare the two proposed order-three conjugacy classes through their fixed-point data. **Confidence: medium.** The page itself explicitly organizes the discussion around fixed points and lifting classes, but the required hypotheses and the exact general theorem are outside these two pages; this is a proposed check, not a claim of novelty or an established result.

8. **Scan 90, (25)–(27) — own idea.** After resolving the overwritten prime marks, derive the index-two subgroup presentation mechanically from the three-involution presentation, keeping the manuscript’s multiplication order throughout. **Confidence: high as a verification strategy, not as a reading of the damaged symbols.** The page supplies generators, relators, and the proposed images, so this finite algebraic check can expose unresolved transcription alternatives without deciding them in advance.

## Primary-source reference

Grothendieck, A. (1981). *La Longue Marche à travers la théorie de Galois* [Handwritten manuscript; supplied scans 81–90 from archive cote 140-3, file designated “pages 293–650”]. Université de Montpellier archive.

Bibliographic identification follows `LM_P067_prompt.md` and the supplied scan metadata; it has not been independently verified against an external catalogue. This reference supports the source observations above, not the truth or novelty of the separately labeled editorial proposals.

# LM_P030 — Transcription notes

## Scope, source, and location conventions

This file accompanies `LM_P030_transcription.tex`. The transcription is a diplomatic LaTeX fragment of the ten supplied images, in their filename order. It is not a translation, a corrected mathematical edition, or a reconstruction from another transcription. Readable cancellations and additions are retained; doubtful words, signs, alphabet choices, and revision states are marked explicitly.

The scan identifiers and visible paginations differ:

| Scan identifier | Image filename | Secondary lower/printed page number | Upper handwritten folio encoded with `\mspage` |
|---|---|---|---|
| 291 | `LM_P030_scan291.jpg` | 290 | None visible |
| 292 | `LM_P030_scan292.jpg` | 291 | 147 |
| 293 | `LM_P030_scan293.jpg` | 292 | None visible |
| 294 | `LM_P030_scan294.jpg` | 293 | 148 |
| 295 | `LM_P030_scan295.jpg` | 294 | None visible |
| 296 | `LM_P030_scan296.jpg` | 295 | 149 |
| 297 | `LM_P030_scan297.jpg` | 296 | None visible |
| 298 | `LM_P030_scan298.jpg` | 297 | 150 |
| 299 | `LM_P030_scan299.jpg` | 298 | None visible |
| 300 | `LM_P030_scan300.jpg` | 299 | 151 |

Only the upper manuscript foliation is encoded as `\mspage`. The secondary lower pagination is recorded in this table; the archive's repeated printed institutional footer is excluded from the manuscript text. No scan in this set is blank.

Approximate line references count the principal handwritten baselines, including displayed formulas and diagram rows, from the top of each scan. Folio numbers are not counted. Interlinear and marginal material is located relative to the nearest baseline. These are manuscript locations, not line numbers in the LaTeX file; the accompanying descriptions are more reliable than the counts.

The fragment has no preamble and intentionally does not define the editorial macros. It uses the requested macro vocabulary and standard LaTeX mathematical notation, with `tikz-cd` for sufficiently clear diagrams. Where diagram strokes or directions cannot be established, a bracketed description records the visible terms and the uncertainty. An apparent unmatched parenthesis, changing operator name, anomalous subscript order, or incomplete cancelled formula has not been repaired for mathematical or grammatical consistency.

### Confidence convention

- **High:** the local reading is clear; a table entry may still record a nonlexical issue such as the presence of a revision or an omitted arrowhead.
- **Medium:** a preferred reading is supported by the ink, but some letters, strokes, endings, or attachment points remain unresolved.
- **Low:** competing readings, dense overwriting, or an illegible portion prevents a secure reconstruction.

The confidence column gives a conservative overall assessment for the stated locus. It is not a probability estimate. Repeated doubtful glyphs are grouped in the table, and uncertainty about a cancelled passage is not evidence that the author retained it.

## 1. Table of doubts

| Scan | Approximate line / location | Reading retained | Alternatives / unresolved point | Confidence |
|---|---|---|---|---|
| 291 | 1, cancelled word | `posé` | The cancelling stroke obscures the word ending. | medium |
| 291 | 1, addition above the cancelled word | `admis` | Initial and terminal letters are compressed; not securely `admet`. | medium |
| 291 | 4–5, interline addition | `s' ∈ I' ⇒ Γ_{s'} ≠ (1)` | Initial variable is heavily inked; placement between “stable” and “par Γ” is preserved spatially, but its intended syntactic attachment is not certain. The subset in this condition appears to be `I'`, without the exclamation mark of `I^{\prime !}`. | medium |
| 291 | 7, set symbol | `Φ(π,Γ)` | Glyph resembles a loop on a stem with a baseline; exact mathematical alphabet remains uncertain. | medium |
| 291 | 8, parenthesis after “foncteur” | `lui-m̄ un pur engueulard` | The surprising last word remains tentative: the descending `g` and ending are more distinct than the compressed middle. Two readings from the image suggested this form; it is not replaced by a more plausible mathematical noun. | low |
| 291 | 13 | `ess. surjectif` | Abbreviation before “surjectif” is compressed. | medium |
| 291 | 17–20, reworked passage | Cancelled “Il se peut que”; inserted “Je pense”; cancelled “les propriétés … sur le … fidélité” | Several overlapping revision stages; positions and readable remnants retained without reconstructing a polished sentence. | low |
| 291 | 21, cancelled display | `Autext(π',I^{\prime !}) → Autext(π)Γ,I^{\prime !}` / target with `π,Γ` | A closing-parenthesis-like arc immediately after `π` precedes a heavily retraced Γ-like glyph. The final superscript might be prime-plus-exclamation or double prime; no secure closing delimiter at the end is supplied. This is not normalized into a well-formed three-argument operator. | low |
| 292 | 1 and 7 | `α_s` / `α` | Compact map name; final low hook might be a subscript `s` or merely the tail of `α`. Both repeated occurrences were compared. | medium |
| 292 | 2 | `th.` | Abbreviation is compressed; initial letter is not fully distinct. | medium |
| 292 | 9 | `Établir` | Initial capital is clear, but an acute accent is uncertain. | medium |
| 292 | 10 | `ramenant` | Final syllable reduces to a short trailing stroke. | medium |
| 292 | 13–17 | `Φ` and calligraphic `E` | Exact alphabet of the set and extension symbols not completely resolved. | medium |
| 292 | 9–12 | Opening parenthesis after “précédent” | No secure closing parenthesis appears before the final full stop; none supplied. | high |
| 293 | 1–2 | `opérant de façon [illegible]` | The word after “cycliques” is compressed; the adjective on the next line could not be established. No prime-order hypothesis is supplied from context. | low |
| 293 | 4 | `désinfection` / `description` | The tall descending middle letter may be `f` or `p`; neither reading is established. “Description” is not substituted merely because it sounds like a familiar theorem label. | low |
| 293 | 6 | `homologiques` | The initial tall cluster, medial ascender and later descending `g` support this reading; the retraced beginning still prevents full confidence. | medium |
| 293 | 8 | `devraient` | Ending not sufficiently differentiated to rule out `devrait`; plural is tentative. | medium |
| 293 | 12, interline replacement | `du moins pour des` | Final two short words are especially compressed. | medium |
| 293 | 14, above “action de” | `ext.` | Interlinear abbreviation has a weak final stroke and point. | medium |
| 293 | 17 | `si`, cancelled `bonne` | First is overwritten; second is heavily cancelled. | low |
| 293 | 20 | `I^{\prime !} → Φ(π,Γ)` | Connecting stroke could be a rightward arrow or a dash without a securely visible arrowhead. | low |
| 294 | 1 | `néc.`, `réalisabilité` | Abbreviation is compressed; the end of the long word approaches the right edge. | medium |
| 294 | 2–3, insertion over `se remonte` | `(par “forage de trous” … pour I^{\prime !}=Φ(π,Γ))` | `forage` is probable, but the tall initial letter and interior joins are not completely separable; a following cancelled item is unreadable. Internal insertion attachment is uncertain. | medium |
| 294 | 3 | `remonte` | Last strokes do not establish every letter independently. | medium |
| 294 | 4–6 | `remontement`, `ess.` | Word endings and abbreviation are compressed. | medium |
| 294 | 5, cancelled line | `que l'ex. corr. de Γ par des π'` | `par des` and the placement of `de Γ` under overlapping strokes are weak readings. | low |
| 294 | 7 | `\mathcal E'` / `\mathcal E^{!}` | Curly E/epsilon-like extension symbol; its superscript appears prime-like here, unlike later clear exclamation marks. | low |
| 294 | 10 | `n° 19` | Possibly `n° 9`; first numeral is a short bent stroke. | low |
| 294 | 11, 13 | `SA_{g,ν}^{!}` | Dense superscript resembles a cancelled/overwritten `!`, a sharp, or a ξ-like mark; no silent resolution. | low |
| 294 | 13, before equals | `\{` | An isolated left-brace-like mark occurs immediately after the subgroup label; its function is unclear. | low |
| 294 | 14–16, insertion | `(ens. des autom. de U_{g,ν} qui)` | `autom.` is compressed and may include a superscript; insertion is placed after the set definition, preserving its physical vicinity rather than asserting a corrected reading. | low |
| 294 | 15 | `induisent` / `induit`; `ds` / `dans` | Ending revised/overwritten; short form before `le` is uncertain. | low |
| 295 | 2 | `trouées` / `troués` | Word is in quotation marks at least at the opening; the ending and a possible closing quote are not secure. No closing quotation mark has been supplied. | medium |
| 295 | 3 | `induisent` | Compressed ending. | medium |
| 295 | 5 | `invariant` | Several interior letters are reduced to joins. | medium |
| 295 | 6–7 | `quot`, `isom.`, `autom.` | Abbreviation lengths and stops are not all secure. `quot` has not been expanded. | medium |
| 295 | 8 | `S_{g,ν}` / `SA_{g,ν}` | Extra ink beside S resembles an A or a corrected/calligraphic stroke. | low |
| 295 | 9 | `U_{ν,g}` / `U_{g,ν}` | Visible subscript appears ν,g, in this order; the conventional ordering is not imposed. | low |
| 295 | 10 | `ds` / `dans` | Compressed first token in the parenthesis. | medium |
| 295 | 14 | `posons` | Initial stroke is overwritten; it may incorporate an abandoned word. | medium |
| 295 | 19 | `Γ_{g,ν}^{!+} = Γ^{!}` | The equality is darker and above the main baseline and is treated as inserted. Superscript ! is secure; the extra + is small but visible. | medium |
| 296 | 2 | `induisant` | Ending is faint and compressed. | medium |
| 296 | 3–4, cancelled opening | `Pour tt [one unreadable word]`, `Soit`, cancelled `ℓ` | The final word of the first abandoned start is not securely legible; `ℓ` before `L_i` is overwritten. | low |
| 296 | 5–6, insertion | `(≃ un rev. universel D̃_i^*)` | Attached to the point of `B_{D_i^*}`; the initial equivalence mark and abbreviated `rev.` are small. | medium |
| 296 | 6–8 | `du` / `de`; cancelled `sur`; `entre`; `dans`; cancelled `l'élément` | Short words occur beside faint/cancelled strokes. | low |
| 296 | 9, Aut formula | cancelled subscript `g,ν` on `s` | The subscript is crossed over and may contain additional ink; it is not silently removed. | low |
| 296 | 11, parenthesis | `strict.` | Possibly `strictement` or `stricte`; ending and stop are not resolved. The following qualification ending in a closing parenthesis is visibly added above. | low |
| 296 | 13 | `g_i∈π`, `tels` | Membership target is overwritten, though π is the likely reading; the adjective is compressed. | medium |
| 296 | 14, first display | deleted factor before `ℓ`; exponent `χ(u)` replaced by `α` | Dense cancellation hides the factor. The exponent's revision is probable, not certain. | low |
| 296 | 15 | `lesquels` / `les quels` | There is a noticeable pen break/space. A word after `u` is struck through and unreadable. | medium |
| 296 | 18 | `on a` | Almost reduced to short strokes after `ℓ∈L_i`; not supplied confidently. | low |
| 296 | 19, composition calculation | `int(h_i^{-1})` | Factor is written over and partly blackened. The remaining product order is retained as seen. | medium |
| 296 | 21–22 | `Posons` | Final word at bottom edge has faint interior strokes; an earlier term before `h_i v(g_i)` is crossed out. | medium |
| 296–300 | Repeated B-objects in prose and diagrams | `B` | The looped or doubled upright does not securely distinguish ordinary B from a calligraphic alphabet. Every occurrence is marked in the fragment. | medium |
| 297 | 1, end of product formula | `(vu,h_i v(g_i)\deleted{\illegible{1}})` | A compact black cancelled factor follows `v(g_i)`; it may contain a subscript `i`, but no factor has been reconstructed. The final grouping is also compressed. | low |
| 297 | between lines 1–2, upper right | `\margin{$S$}` | The letter is clear, but no attachment stroke identifies its purpose; it is treated as an unanchored note. | low |
| 297 | 3–7 and 14–15, repeated extension symbol | `\mathcal E^{!}` / `S\mathcal E^{!}` | The E-like glyph varies from a cursive epsilon shape to an outlined capital E; exact alphabet is uncertain. The superscript has a separate lower dot and is read as `!`, not a prime. | medium |
| 297 | 4, annotation above `(π,I)` | inserted `id. sur I` | A bracket points toward the `I` in the operator's argument; the transcription records the words after the formula rather than inventing an operator superscript. | medium |
| 297 | 10–13, cancelled passage | `hom canonique`; `les hom des Γ!` | Abbreviation endings and possible periods are faint or intersected by cancellation strokes. | medium |
| 297 | 14, after `d'extension` | deleted `(centrale)` | Dense overwriting crosses the word; both the opening parenthesis and exact letter sequence are less secure than the surviving ending. | medium |
| 297 | 14, right margin | `où [ℰ?] opère sur T^I via son action sur T` | Whether the E-like symbol has a tiny superscript is unclear; no superscript has been supplied in the marginal note. | medium |
| 297 | 15, end of new exact-sequence row | `ℰ! - 1` | The final connector is a short horizontal stroke without a discernible arrowhead. No right-pointing head has been supplied. | high |
| 297 | 16, cancelled old exact-sequence row | `1 → T_g^{S_{g,ν}} → SΓ_{g,ν}^{!} → Γ_{g,ν}^{!} - 1` | Several arrowheads and portions of the superscript are hidden by the horizontal deletion line. | low |
| 297 | 17, cancelled orientation-module comparison | `T_g (\unsure{\simeq} Z)` | The comparison sign is repeatedly written/overwritten, with small extra strokes above it; these could be an annotation or part of the overwritten sign. Exact typography of `Z` is uncertain. | low |
| 297 | 17–20, lower cancelled block | `sur ... Il faut donc définir ... Notons que ... et` | Large diagonal strokes cancel the block, and the last two lines are also separately struck horizontally; the nesting/chronology of cancellations cannot be recovered with confidence. | medium |
| 297 | 20, superscript twice on `SA_{g,ν}` | `\unsure{!\|\sharp}` | A dense vertical zigzag could also be a ξ-like sign or an overwritten/cancelled exclamation mark. No uniform notation has been inferred from adjacent pages. | low |
| 297–298 | 297 line 12; 298 line 1 | `S^{\prime}Γ^{!}` as target | Enlargement clearly separates the short prime after `S` from the dotted exclamation sign after `Γ`. This differs from the unprimed `S` in the live `Sℰ!` formulas. | high |
| 297–300 | Repeated orientation-module symbol, including subscripts | `T` / `\mathbb T` | The top bar is sometimes doubled or retraced. Blackboard typography cannot be established from the ink; the alternative is recorded at every occurrence rather than inferred from the expected module. | medium |
| 298 | 2, `pour ... i` | `\unsure{\forall\|\mathrm{tt}}` | The handwritten mark resembles either a cursive universal quantifier or the two-letter abbreviation `tt`. The membership condition is an above-line insertion attached to `i`. | medium |
| 298 | 3, parenthesis after `s_i` | `qu'on` | The compressed end of the line does not show all letters distinctly. | medium |
| 298 | 5, abbreviation before `entre` | `iso` | An abbreviation for an isomorphism seems intended, but the letters are faint and there is no securely visible final period. | medium |
| 298 | 5, universal-cover symbol | `\widetilde U(i)` / `U(i)` | The apparent tilde overlaps the descending/returning stroke of `p` in `épointé` on the line above; a separately intended accent cannot be established. | low |
| 298 | 6, abbreviated second cover | `univ.` | The word ending and abbreviation point are compressed. | medium |
| 298 | 7–8, end of cancelled passage | `Cet autom` | `Cet` is clear, but the next truncated/cancelled word might have another ending; no completion has been supplied. | low |
| 298 | 8 | `interpréter` | The final letters are cursive strokes; the reading is probable but not independently secure letter by letter. | medium |
| 298 | 11 | `bon sens` | The word after `bon` is reduced to a short loop and stroke. `sens` is only a tentative reading, not a contextual restoration. | low |
| 298 | 12, first automorphism symbol | `\ddot u` / `\dot u` | Two separate dots are visible above/beside the first `u`; later occurrences have one dot. The two-dot form has not been normalized to the later notation. | medium |
| 298 | 12 | `autoéquivalence` / `autoéquiv.` | The word's end is highly compressed; it may be abbreviated. | low |
| 298 | 13 | deleted `dans` | A heavily written/crossed word precedes `de la situation`; both the reading and exact cancellation state are uncertain. | medium |
| 298 | 13, 21, 23, diagram letters | `B` | These B-like glyphs have looped/doubled stems; ordinary versus calligraphic alphabet cannot be established. | medium |
| 298 | 14, between principal baselines | inserted `induisant l'identité sur I` | The smaller interline clause is treated as an insertion; its textual content is much clearer than the chronology of its addition. | medium |
| 298 | 17 | `tt` / `tout` | The final shorthand is a pair of tall strokes; it is not silently expanded. | medium |
| 298 | 18–19, bracket after `γ_i` | `déterminé par élémt de T` | Singular/plural ending is uncertain; an extra `un` may be compressed after `par`; `élémt` may instead be a compressed full `élément`. | low |
| 298 | 19, before `Le groupe` | deleted `L'ens des` | The horizontal strike crosses the abbreviation; the replacement starts on the same line. | medium |
| 298 | 20 and 22 | `automs` / `autom.` | The last hook and any abbreviation period are uncertain. | low |
| 298 | 21 and 23 | right-pointing connectors in the tuples of `B`-objects | Some connectors have clear arrowheads, others only a faint end-hook or a plain stroke; the doubtful ones are marked rather than regularized. | medium |
| 298 | 22 | `d'isom.` / `d'équiv.` | The beginning of the abbreviated word is ambiguous; the final strokes resemble `som.` more than a securely spelled longer word. | low |
| 299 | 2, 4–8, 12; throughout | `\mathcal E` | The ink is an E/epsilon-shaped glyph; `\varepsilon` or another calligraphic E form remains possible. Its alphabet is not securely identified. | low |
| 299 | 2, 4–8, 12; superscripts | `!` after Γ and the E-like letter | The enlargement shows a separate lower dot: this is not transcribed as a lone prime. No separate prime immediately after S is evident here. | high |
| 299 | 4–5; first diagram | Two rows with the displayed terms and downward arrows | The initial material of the lower row is overwritten or possibly cancelled and cannot safely be completed to `1`. The upper connector from `T^I` to the S–E-like term lacks a distinct arrowhead; the next two connectors have bent right ends whose status as arrowheads is unclear. A bracketed diagram description records these observations. | low |
| 299 | 7; before “l'extension” | `\deleted{\illegible{1}}` | A short word is crossed through; “une” is possible but not secure. | low |
| 299 | 7; above “de Γ!” | Inserted `S\Gamma^{!}` | Attachment to “l'extension” is supported by the placement of the added group symbol. | high |
| 299 | 9 | `d'autoéqui.` / `de autoéqui.` | The mark after d/e is not sufficiently clear to choose the contraction. | medium |
| 299 | 10–11, 14–16, 19; B-diagrams | `B` | The verticals are doubled or looped. Ordinary B versus a calligraphic form is unresolved, hence the doubt mark. | low |
| 299 | 13; before “autoéqui.” | `\deleted{\illegible{1}}` | The crossed word may begin “auto…”, but the remaining letters are not secure. | low |
| 299 | 15; curved interior arrow | `isom. de comm.`; direction explicitly doubtful | The expansions would probably be “isomorphisme de commutation/commutativité”; the abbreviation letters and the final dots are not wholly secure. Both ends of the curve have extra strokes, so down-right versus up-left is unresolved. | low |
| 299 | 19 | `du 2-diagramme` | The short article and the initial numeral are uncertain; “des” and the precise singular/plural ending cannot be excluded. | medium |
| 300 | folio | `151` | The middle digit is round in this hand but is read as 5, not 0. | high |
| 300 | 2; cancellation and superscription | Deleted `extérieurs`, inserted `autom.` | The original ending and the replacement abbreviation are both partly compressed. | medium |
| 300 | 5–6; abbreviations | `hom` without a final dot | A possible very faint dot cannot be resolved. Scan 299 has a more evident `hom.`. | medium |
| 300 | 5 onward; all E-like symbols | `\mathcal E` | `\varepsilon` or another calligraphic E form remains possible. | low |
| 300 | 6–9; upper part of the large diagram | `1↓π`, `1↓π`, and an isomorphism-like label on `π→π` | The small mark above the horizontal arrow is read as `\sim` with doubt. There is a visible arrow from the left π to S–E, but no distinct corresponding stroke from the right π to E; none has been supplied. | medium |
| 300 | 9; lower right of large diagram | A connector from Γ to 1 with no distinct head | This may be an abbreviated arrow; the no-head connector preserves the visible stroke. | medium |
| 300 | 13; insertion before E | `l'ext` | Probably an abbreviation for “l'extension”; a final dot is not securely visible. | medium |
| 300 | 14; quotient sentence | `T^{I}` / `T^{S}` | The exponent has an angular, S-like stroke, although I is the stronger candidate. It is not silently harmonized with preceding displays. | medium |
| 300 | 15; paragraph opening | `Revenant`, possibly deleted | The long line through the word might be a cancellation or part of the ductus. “Revenons” is a less secure lexical alternative. | low |
| 300 | 15 | `topologique` | The middle and final letters are densely joined and partly retraced. | medium |
| 300 | 16; surface notation | `U_{g,ν}` | Ordinary U versus a more cursive/calligraphic form is uncertain. | medium |
| 300 | 16 | `prendra` / `prend`; `les` / `des` | The endings and the small article are strokes rather than separately legible letters. | medium |
| 300 | 17; left of first definition | Cancelled `S\mathcal E_{g,ν}` | An abandoned marginal group symbol is heavily overwritten; its initial S is only tentative. | low |
| 300 | 17; first definition | Deleted `ext` after Aut | The crossed suffix is plausible as “ext” but is not fully separable from the cancellation strokes. | medium |
| 300 | 17, 19; fundamental-group symbol | `π` / `Π` with subscript g,ν | The capital/lowercase distinction is not secure in these two parenthesized occurrences. | medium |
| 300 | 17–18; right-hand parenthesis | `Γ_{g,ν+1}`, `(g,ν)≠(0,0),(0,1)` | The displayed exclusions are clear enough to retain. The cancelled following criterion is tentatively `π_{g,ν}≠0`; the letter, cancellation boundary, and final extraneous mark are uncertain. | low |
| 300 | 21–23; last comparison | `SΓ'_{g,ν+1}` | The small slash appears after Γ and has no distinct lower dot. It is retained as a prime, independently of the exclamation marks on scan 299. The same prime-looking stroke occurs in the inserted explanation and the following group symbol; no harmonization was made. | medium |
| 300 | 21; denominator after slash | `\unsure{T}_{\illegible{1}}` | T is probable; the heavily retraced subscript cannot responsibly be resolved. It may contain s and/or g,ν, but those letters have not been supplied. | low |
| 300 | 21–22; circled insertion | Cancelled illegible word, then `où SΓ'_{g,ν+1} désigne le` | The first word is unreadable; “où” is probable. The circled addition is attached before “sous-groupe”, following the descending placement line. | low |
| 300 | 22 | `élé-ts` | Probably a contracted “éléments”; the contraction is retained rather than expanded. | medium |
| 300 | 22–23 | `le`; final `s` | The article is retraced, and the last symbol before a closing parenthesis is only tentatively s. The overlapping parentheses and ellipsis are retained without grammatical repair. | low |

## 2. Abbreviations met

Expansions in this table are editorial and tentative. They are not substituted into the transcription. Distinct visible punctuation or shortened forms are retained as separate entries where useful.

| As written | Tentative expansion or function |
|---|---|
| `ext.` | extérieur / extérieure; extérieure (action); extension (elsewhere) |
| `i.e.` | id est |
| `pl.` | pleinement |
| `ess.` (uncertain reading) | essentiellement |
| `m̄` (`\overline{\mathrm m}`) | même |
| `Autext` | automorphismes extérieurs; automorphismes extérieurs; interpretation is tentative, and the lettering is retained as one operator; automorphismes extérieurs / groupe des automorphismes extérieurs |
| `th.` (uncertain reading) | théorème |
| `Pb` | problème |
| `ens.` | ensemble / ensembles |
| `pts` | points |
| `néc.` | nécessairement / nécessaire, according to syntax |
| `tte` | toute |
| `cond.` | condition |
| `suff.` | suffisante |
| `ex.` | extension, probably, in the cancelled passage |
| `corr.` | correspondante |
| `ess.` | essentiellement, probable |
| `$\overline{\mathrm m}$` | même |
| `n°` | numéro |
| `autom.` | automorphismes; automorphismes; inserted reading uncertain |
| `i.e` | id est |
| `ds` | dans, if the abbreviated reading is correct |
| `ss-groupes`, `ss-groupe` | sous-groupes, sous-groupe |
| `NB` | nota bene |
| `quot` | quotient, if the abbreviated reading is correct |
| `isom.` | isomorphe; isomorphisme |
| `tt` | tout / toute / tous, unresolved in a cancelled start |
| `pt` | point |
| `rev.` | revêtement |
| `isom` | isomorphisme; isomorphe |
| `str.` | structure |
| `élts` | éléments |
| `int` (in formulae) | automorphisme intérieur / conjugaison intérieure |
| `strict.` | strictement, if the abbreviated reading is correct |
| `ens` | ensemble |
| `loc` | local / locaux |
| `id.` | identité |
| `hom` | homomorphisme(s), without silently supplying a missing period |
| `can.` | canoniquement / canonique |
| `univ.` | universel |
| `iso` | isomorphisme |
| `autom` / `automs` / `autom.` | automorphisme / automorphismes; individual readings remain uncertain |
| inserted `can` | canonique |
| `autoéquiv.` (alternative reading) | autoéquivalence |
| `syst.` | systèmes |
| `tt` (tentative) | tout |
| `élémt` (tentative) | élément |
| `isom.` / `équiv.` (alternative readings) | isomorphie / équivalence |
| `hom.` (299), `hom` (300) | homomorphisme |
| `d'isom.`, `d'isom`, `d'iso.` | d'isomorphisme, with the variable punctuation retained |
| `autoéqui.` | autoéquivalence(s) |
| `pt.` | point |
| `comm.` | commutation or commutativité; reading and expansion uncertain |
| `ext.` in “ext. ou totaux” | extérieurs |
| `ext.` in “comme ext. de Γ” | extension |
| `l'ext` | l'extension; inserted reading uncertain |
| `resp.` | respectivement |
| `can` above ≃ | canonique / canoniquement |
| `Aut` | automorphismes / groupe des automorphismes |
| `lac` in the subscript | lacets; the exact convention must be obtained from the manuscript, not supplied in the transcription |
| `élé-ts` | éléments; contracted reading uncertain |
| `Aut ext` | automorphismes extérieurs; the space in this operator is retained where visible |

The prefixed `S`, superscript `!`, prime positions, and the letters naming groups or modules are mathematical notation; no expansion of them is imposed.

## 3. Legibility and limits

The broad prose and several principal formulas are substantially more readable than the corrections. The weakest parts are the lower cancellation block on scan 291, the opening parenthesis and theorem-name word on scan 293, the overlapping first paragraph and subgroup superscripts on scan 294, the first conjugation formula on scan 296, the cancelled passages on scans 297–298, and the lower-right comparison on scan 300. No uncertain reading should be promoted to an established mathematical premise solely because it fits the surrounding argument.

### Scans 291–293

Scan 291 has fairly legible main prose but very compressed interline corrections. Its lower cancellation block, the arguments of the deleted automorphism display, and the noun following “un pur” are substantially less secure than the surrounding text. Superscripts containing both a prime and an exclamation mark are retained as such, rather than regularized to a double prime.

### Scans 294–296

Scan 294 has clear broad paragraph structure and a reasonably secure section heading, but the opening paragraph contains overlapping cancellations and interlinear additions. The compact superscript on `SA` and the annotation under its definition remain weak readings. The short symbols have not been regularized by their mathematical roles.

Scan 295 is more legible overall. The quotient and displayed inclusions can be followed, but the author has not made the two superficially similar zero-superscript expressions identical: `(SA)^{0}` and `SA^{0}` are kept distinct. The order of the subscript on `U` is not silently corrected.

Scan 296 is low contrast in its prose and heavily revised near the first conjugation formula. The composition calculation is more legible than the surrounding cancellations. Its factor order is reproduced rather than recomputed; the interpretation of the overwritten exponent and the factor `int(h_i^{-1})` deserves independent checking.

### Scans 297–298

On scan 297, the upper group-law discussion is substantially more legible than the lower revisions. The large cancellations, the E-like extension symbol, the dense superscripts on `SA`, and the exact limits of replacement passages are the least secure features. A crossed-out passage has been retained as crossed-out text even where its mathematical development is later resumed.

Scan 298's main construction can be followed, but several abbreviated endings, the apparent double-dot on the first `u`, the notation for the classifying objects, and the clause about determination by an element of `T` remain insecure. The first paragraph is crossed by several long diagonal cancellation strokes. A visible prime on `S` has been retained even where omitting it would produce a more familiar notation.

### Scans 299–300

The running prose of scan 299 is considerably clearer than its overwritten initial exact-sequence diagram. The E-like group letter and the B-like diagram symbols do not admit a confident typographical-alphabet decision from these pages alone. On scan 300, the main extension construction is readable, including the small vertical additions to the large diagram; the final two definitions and especially the cramped, circled explanation at the lower right are the least trustworthy passages. The output deliberately retains uncertainty about the final quotient denominator, the exceptional-case cancellation, prime placement, and the disposition of the last parentheses rather than using the expected mathematics to finish them.

## 4. Research notes — English, separate from the transcription

These are questions and proposed verification tasks arising from this excerpt. They do not revise the transcription, assert originality, or claim that an argument is absent from the remainder of the manuscript or the literature. Brief quoted phrases refer only to these supplied images; bracketed question marks in quotations identify doubtful readings. No external transcription or secondary literature was used to complete a reading.

Authorial conjectures and expectations, unproved claims, and implications not pursued here are distinguished from items explicitly labelled **own idea**. Each own idea states its confidence and reason. Source locations in each item refer to Grothendieck (1981), as described below.

1. **Scan 291, approximately lines 7–13 — conjecture.** The author writes, “La conjecture est que le foncteur … est une équivalence de catégories,” and separates full faithfulness from essential surjectivity. The exact categories and the marked subset condition should be recovered from the preceding pages before formalizing this assertion; the uncertain noun in the parenthesis should not be used as mathematical evidence.

2. **Scan 291, approximately lines 14–17 — unproved claim.** “Le point 2°) est clair” is restricted to situations realizable on both sides, while “le point 1°) n'est pas prouvé” explicitly leaves full faithfulness open even there. A proof would need to establish the claimed correspondence of morphisms, rather than merely produce geometric representatives of objects.

3. **Scan 291, approximately lines 18–24 — conjecture / expectation.** In the revised passage, “Je pense” introduces a reduction to a singleton marked set and the expectation that properties of the “forage d'un trou” functor will establish the result. Because the superscript on the underlined singleton condition reads `I'`, whereas nearby subsets are `I^{\prime !}`, that distinction should be checked against the preceding definitions rather than silently equated.

4. **Scan 292, approximately lines 1–12 — conjecture / proposed programme.** “Le Programme d'attaque du Pb de réalisabilité” separates bijectivity of the maps tentatively read as `α_s` from full faithfulness of the preceding functor. The author proposes reducing the latter assertion to one “orbite (singulière)”; a rigorous reduction would have to specify how morphisms and their compatibilities descend or reassemble across orbits.

5. **Scan 292, approximately lines 13–17 — conjecture / proposed programme.** Under `Φ(π,Γ)=∅`, paraphrased on the page by the absence of nonidentity finite-order elements in the extension, the task is to “prouver que” the extension equipped with conjugacy classes of centralizers of the `L_i` is a “groupe à lacets.” Establishing this requires the actual definition of that class of groups and verification of its peripheral data; absence of torsion alone is not presented as a proof here.

6. **Scan 292, approximately lines 18–21, continuing on scan 293 — conjecture / proposed programme.** The author says “il faudrait commencer par réaliser ce programme” to obtain the preliminary properties of the sets tentatively read as `Φ(π,Γ)`. The continuation proposes cyclic groups and proceeding “par dévissage”; the condition in the intervening parenthesis is not securely readable, so no stronger hypothesis such as prime order should be attributed to this passage.

7. **Scan 293, approximately lines 4–9 — conjecture / conditional expectation.** “Si le th. de [désinfection / description?] complet … était vrai,” the three programme items “devraient l'être aussi.” The parenthesis speaks of an equivalence of 2-categories, but the exact adjective naming the second category is doubtful; a proof needs to identify the functor and justify passage from the higher categorical statement to each individual programme item.

8. **Scan 293, approximately lines 9–13 — conjecture / conditional expectation.** The author expects items I and II to hold when the relevant 2-functor “serait 2-fidèle (pas néc. … 3-fidèle),” with the revised restriction to realizable situations. The erased additional “pas” and replaced “condition néc.” are retained as revision evidence, not treated as the author's final proposition.

9. **Scan 293, approximately lines 13–20 — unpursued implication.** The definition introduced by “On dirait donc” combines an automorphism-group isomorphism with a conjugacy condition for other actions giving the same downstairs action and marked-set map. These are logically distinct requirements; determining exactly which is supplied by the proposed 2-faithfulness requires definitions from the preceding manuscript, especially since the displayed target reads `Aut`, whereas the source reads `Aut ext`.

10. **Scan 293, approximately lines 13–20 — own idea.** Test the two admissibility requirements separately on a fully specified small cyclic action and its marked peripheral data, keeping the lifting problem separate from the automorphism comparison. **Confidence: medium as a research strategy, not as a mathematical result.** The reason is that the page itself distinguishes an automorphism isomorphism from uniqueness up to conjugacy, so examples may reveal different obstructions without assuming an equivalence theorem.

11. **Scan 294, lines 1–8 — conjecture / expectation.** The conditional wording “la cond. néc. et suff. … serait” proposes a realizability criterion using an admissible lift of an exterior action and a corresponding extension that is “un groupe à lacets.” The paragraph should be compared with the preceding definition of admissibility and the precise hypotheses on faithful actions; the claim is conditional here, not a proved equivalence.

12. **Scan 294, lines 4–6 — unproved claim.** In the parenthesis beginning “par définition”, the lift is said to be “ess. unique” (abbreviation uncertain). A proof would need to specify the equivalence relation on lifts and separate existence from the automorphisms that remain after the peripheral data are fixed.

13. **Scan 294, lines 17–19 — unproved claim.** “celui-ci n'est pas un ss-groupe fermé” is asserted for the subgroup defined by inducing the identity near the marked set. The topology on the ambient automorphism group and an explicit convergent family whose support approaches a puncture would be needed to verify the stated nonclosedness.

14. **Scan 294, lines 13–19 — own idea.** Test the nonclosedness assertion using finite partial products of homeomorphisms supported on disjoint annuli accumulating at a puncture, with displacements tending to zero. Each partial product could be trivial on some neighbourhood of the puncture while the limit remains nontrivial arbitrarily close to it. **Confidence: medium as a possible construction, not as an established example**, because convergence and membership in the intended automorphism group still depend on the topology and regularity assumptions; individual maps with shrinking supports could instead converge to the identity and would not establish nonclosedness.

15. **Scan 295, lines 1–4 — unpursued implication.** The author says that for compact surfaces with boundary “il y aurait lieu de prendre” automorphisms inducing the identity on the boundary. Comparing this boundary condition with identity on an entire neighbourhood of each puncture would require a precise collar or end construction and attention to the topology used on automorphism groups.

16. **Scan 295, lines 5–10 — unproved claim.** The subgroup is described as “invariant” and the quotient as a group of “germes” of automorphisms, equivalently germs “à l'infini.” A proof would need to define equality of germs, check that the kernel is exactly the neighbourhoodwise-identity subgroup, and determine which germs extend to global automorphisms.

17. **Scan 295, lines 11–19 — unproved claim.** “On aura évidemment” introduces the inclusions and the canonical homomorphism from the newly named special group to the indicated Teichmüller group. The distinction between `(SA)^{0}` and `SA^{0}` is left visible; a careful proof must establish precisely which identity component or intersection is meant in the denominator before forming the quotient.

18. **Scan 295, lines 15–19 — conjecture / expectation.** “qu'on va interpréter de façon algébrique” announces a subsequent interpretation of the canonical map. It is a stated programme at this point, and the next scan's peripheral choices must be checked for their dependence on representatives.

19. **Scan 296, lines 4–9 — unproved claim.** The choice of a subgroup representative `L_i` is described as equivalent to giving a “pt” of the indicated `B` object and an isomorphism to the reference point. A careful account would need the category of points and its equivalences, together with an explanation of how changes in the chosen universal covering alter the resulting subgroup representative.

20. **Scan 296, lines 10–16 — unproved claim.** Preservation of “la str. à lacets” is expressed by the existence of elements `g_i`, followed by the assertion that they are determined “modulo multiplication à droite” by elements of `L_i`. The uniqueness assertion would require control of the centralizer of `L_i` in `π`; the printed formulas alone do not supply that argument.

21. **Scan 296, lines 18–22 — unpursued implication.** The displayed composition computation leads to the ordered system `h_i v(g_i)` and the next construction. To turn this into a group law one should check closure and inverses for pairs consisting of an automorphism and chosen conjugators, then state how changing representatives in the `L_i`-ambiguity affects the construction.

22. **Scan 296, lines 14–22 — own idea.** Compare two choices of the family `L_i` and their conjugating elements to determine whether the resulting enriched automorphism groups are isomorphic canonically or only after additional choices. **Confidence: medium** that this isolates a useful invariance problem, because the page makes choices explicitly and its multiplication formula retains those choices; no canonical isomorphism is asserted here.

23. **Scan 297, lines 1–5 — unproved claim.** The sentence “On trouve alors une structure de groupe” asserts that the admissible pairs form a subgroup of the indicated semidirect product. The displayed multiplication alone does not verify closure of the admissibility condition or closure under inversion; those checks must use the preceding definition of the pairs.

24. **Scan 297, lines 7–10 — unproved claim.** The projection is said to be “surjectif” with kernel “can. isom” to the product of the peripheral groups, compared in turn with the orientation module to the power `I`. A proof needs both the existence of permitted choices above each automorphism and an exact account of the freedom in those choices.

25. **Scan 297, lines 14–15 and right margin — unpursued implication.** The deletion of “centrale” beside an explicit annotation about the action on the orientation module should be checked carefully against any later central-extension statement. One useful question is whether restriction to automorphisms acting trivially on that module makes the extension central; this is not a claim that it splits.

26. **Scan 297, lines 1–15 — own idea.** Choose lifts of the projected automorphisms and use the displayed product to compute their composition defect as a candidate cocycle with values in the indicated kernel. **Confidence: medium**, because the displayed multiplication supports this route, but the exact coefficient action and the choices hidden in the preceding definitions still have to be checked; no novelty or established result is claimed.

27. **Scan 298, lines 8–11 — conjecture / expectation.** “Je voudrais interpréter cette extension comme l'image inverse” explicitly states the intended interpretation as the pullback of an extension of `Γ!` by `T^I`. The author adds a canonicity qualification and a choice of the covers `\widetilde D_i^*`; comparing the algebraic pair construction with the following categorical construction is still a proof obligation on this page.

28. **Scan 298, lines 15–19 — unproved claim.** The lifts are described as systems `(\dot u,γ_i)` with `γ_i:\widetilde D_i^*→\dot u(\widetilde D_i^*)`, followed by a partly uncertain bracket about determination by an element of `T`. One should verify existence of each isomorphism, the precise dependence on choices, and whether the possible choices form a torsor rather than a canonically identified group; the uncertain bracket must not be quoted as a settled assertion.

29. **Scan 298, lines 19–23 — unproved claim.** The phrase “ou si on préfère” introduces a second description through automorphisms of the longer diagram beginning with `B_I`. A proof would need an explicit comparison of the two kinds of automorphism data, including their isomorphisms, and compatibility of that comparison with composition.

30. **Scan 298, lines 10–23 — own idea.** Compare two choices of the covers and the comparison isomorphisms directly, recording whether the resulting extensions are isomorphic canonically, noncanonically, or only up to an inner ambiguity. **Confidence: medium**, because the visible qualification “une fois choisis” makes choice-dependence explicit, but the required coherence data are not established on this page; this is a proposed check, not a novelty claim.

31. **Scan 299, lines 6–11 — unproved claim / proof sketch.** The statement “est bien l'image inverse de … l'extension” claims a pullback identification for the extension with kernel `T^I`. The page begins an explanation in terms of classes of autoequivalences; a complete proof would need explicit comparison maps, verification of the induced group laws, and identification of the kernel map with the displayed identity on `T^I`. The initial exact-sequence notation contains cancellations, so the claim should first be checked against the preceding page's definitions.

32. **Scan 299, lines 12–19 — unproved claim.** The group represented by the square with an “isom. de comm.” is said to map naturally to the group of isomorphism classes for the chain `B_I → B_{D*} → B_U`: “qui s'envoie de façon naturelle”. One would need to specify which coherence data are retained or forgotten, show the construction is invariant under isomorphism, and verify compatibility with composition. The handwritten B-alphabet and the curved-arrow label remain doubtful; this is a research question about the displayed construction, not an asserted reconstruction of its conventions.

33. **Scan 300, lines 1–9 — unproved claim.** Grothendieck says there was no need “de se borner” to automorphisms “induisant l'identité sur I”, and extends the construction to the unmarked groups. A proof must keep track of the action on the indexing set I and the resulting action on `T^I`; the two columns of added π-terms suggest the compatibility that has to be checked. The absent or indistinct stroke from the right upper π to the E-like group should not be supplied as evidence for a completed diagram.

34. **Scan 300, lines 10–12 — unproved claim.** The page states that one can regard the S–E-like group “comme ext. de Γ par `T^I × π`”. The explicit direct product is a substantive claim: a verification should produce the two subgroup maps, show their intersection is trivial, and show that they commute, rather than merely establish an extension of π by `T^I`. These requirements are proposed proof obligations; no correction to the written product is intended.

35. **Scan 300, lines 13–14 — unpursued implication.** The sentence “se déduit en divisant” presents the E-like and SΓ extensions as quotients by the two indicated factors. An immediate point to check is whether the two quotient descriptions recover a common comparison diagram with the expected normal subgroups and the same action of Γ. The doubtful exponent in the second sentence should be resolved before using it to identify a specific quotient.

36. **Scan 300, lines 17–18 — unproved claim.** The first geometric definition is accompanied by a “can” isomorphism-like comparison with `Γ_{g,ν+1}` and the explicit exclusions `(0,0),(0,1)`. A proof would require a precise convention for the extra marked point, the subgroup of the automorphism group denoted by the `lac` condition, and the treatment of low-complexity cases. The subsequently cancelled “i.e.” criterion is not secure evidence for any further equivalence.

37. **Scan 300, lines 21–23 — unproved claim.** The last, heavily revised comparison uses a quotient and an added explanation containing “désigne le … sous-groupe” and “qui fixent … dernier élément”. The objects requiring verification are the distinguished-element stabilizer, the precise factor removed in the quotient, and compatibility with the extension defined above. The denominator and several symbols are unresolved in the transcription, so the exact mathematical assertion cannot yet be stated with confidence.

38. **Scan 300, lines 10–14 and 21–23 — own idea (confidence: medium).** Work out a single explicitly punctured surface with chosen local loops and chosen lifts, and compute both quotient maps from the S–E-like extension before attempting the general case. This could test the direct-product kernel assertion and distinguish the role of a framing/local-loop factor from the role of a moving distinguished point. Confidence is medium because the two quotient operations are explicit on the page, while the final geometric comparison still contains unresolved notation; no claim of novelty or established validity is made.

39. **Scan 299, square diagram; scan 300, diagram and final comparison — own idea (confidence: low).** Treat the chosen interior isomorphism in the square as additional data and ask whether forgetting that datum accounts precisely for the displayed `T^I` kernel, then compare the result with the extra-point construction at the bottom of scan 300. The diagrams motivate this test, but the necessary definitions and coherence conventions are not supplied on these two pages, so this is only a possible route of investigation.

## Source reference

Grothendieck, A. (1981). *La Longue Marche à travers la théorie de Galois* (Cote 140-2, archive file described in the supplied prompt as “pages 1–292”; supplied scan files 291–300) [Unpublished handwritten manuscript, digitized images]. Université de Montpellier.

Bibliographic identification follows the supplied task prompt and the image footers. The source citation is not a claim to have checked another edition, the archive catalogue, or later developments.

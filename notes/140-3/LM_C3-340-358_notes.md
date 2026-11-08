# LM_C3-340-358 — Editorial and research notes

## 1. Scope and conventions

This package transcribes the **19 supplied scans, 340–358**, in filename order. It is a diplomatic transcription of the manuscript supplied with the task (Grothendieck, 1981), with cancellations, insertions, marginal writing, unfinished expressions, and visible inconsistencies retained. No external transcription, published edition, or later manuscript passage was used to supply missing readings.

The lower-left handwritten foliation runs from **339 to 357**; an additional upper manuscript number is visible on several sheets. Both systems are retained with `\mspage` at their respective positions. `\scanpage` always denotes the supplied filename number. The printed archive page number, URL, institutional address, and black facsimile border are not manuscript text and are excluded. The supplied source identification is recorded in the reference below.

The LaTeX file is a fragment without a preamble or macro definitions, as requested. It retains the manuscript's physical sequence, including corollaries on scan 346 before the proof continuation on scan 347, duplicate equation numbers, open parentheses, and unfinished calculations. Cancellation strokes are encoded by deletion macros; grouping marks and placement arrows are represented separately. Standard mathematical typesetting is used to encode the visible notation, not to correct it.

There are **514 inventory entries**. `transcribed=yes` means that the element has been represented, including any doubtful reading; it does not assert that every letter is certain. Confidence labels refer to the proposed reading, not to the truth of the mathematics. A single tentative reading indicates that no second reading was sufficiently supported to offer one. The explicit-marker concordance in §6 records every occurrence of `\unsure` or `\illegible`, including repetitions and nested cancellations.

## 2. Table of doubts

Locations refer to approximate handwritten lines within the manuscript frame, excluding foliation unless stated. Formula numbers, quoted words, and margin positions are often more reliable than line counts. The complete source-line concordance in §6 supplies an additional exact locator in the delivered LaTeX file.

### Scans 340–344

| Scan | Approximate line or position | Reading | Alternative(s) | Confidence |
|---|---|---|---|---|
| 340 | top, lines 1--12 | `par` | `en` | medium |
| 340 | top, lines 1--12 | `\overline{\mathrm m}` | No secure alternative | medium |
| 340 | top, lines 1--12 | `tte` | No secure alternative | medium |
| 340 | upper middle, line 13 | `\deleted{\text{et}}` | No secure alternative | low |
| 340 | upper middle, line 13 | `N_1` | `N_0` | low |
| 340 | upper middle, line 13 | `\widetilde\sigma(N_1)` | No secure alternative | low |
| 340 | upper middle, line 13 | `:` | No secure alternative | low |
| 340 | middle, line 15 | `(\deleted{74})` | No secure alternative | low |
| 340 | middle, lines 16--18 | `appliquant` | No secure alternative | low |
| 340 | lower middle, lines 19--20 | `(**)` | No secure alternative | low |
| 340 | lower middle, lines 19--20 | `\deleted{=\lambda^2}` | No secure alternative | low |
| 340 | lower middle, line 22 | `.` | No secure alternative | low |
| 341 | upper, lines 4--5 | `(**)` | No secure alternative | low |
| 341 | upper middle, lines 6--14 | `(**)` | No secure alternative | low |
| 341 | upper middle, lines 6--14 | `det` | No secure alternative | low |
| 341 | middle, line 15 | `2` | No secure alternative | low |
| 341 | middle, lines 16--17 | `le` | No secure alternative | low |
| 341 | middle, lines 16--17 | `ve.` | No secure alternative | low |
| 341 | lower, lines 21--25 | `serais` | `sera` | low |
| 341 | bottom, line 26 | `3` | `2` | low |
| 341 | bottom, line 26 | `-` | `+` | low |
| 342 | upper, line 7 | `(75)` | `(76)` | medium |
| 342 | middle, lines 10--13 | `c'était` | No secure alternative | low |
| 342 | middle, lines 14--15 | `''` | No secure alternative | low |
| 342 | middle, beneath second epsilon identity | `Prenant` | No secure alternative | low |
| 342 | middle, beneath second epsilon identity | `\varepsilon_0=\det\rho` | No secure alternative | low |
| 342 | lower, line 20 | `=` | No secure alternative | low |
| 342 | bottom, line 25 | `4` | No secure alternative | low |
| 343 | top, line 1 | `par` | No secure alternative | low |
| 343 | middle, lines 6--9 | `''` | No secure alternative | low |
| 343 | middle, lines 6--9 | `(` | No secure alternative | low |
| 343 | middle, lines 6--9 | `\deleted{\rho}\inserted{\sigma}` | No secure alternative | low |
| 343 | diagonal left margin, beside lines 7--11 | `--` | No secure alternative | low |
| 343 | middle, line 10 | `-` | No secure alternative | low |
| 343 | lower, lines 13--17 | `la` | No secure alternative | low |
| 343 | lower, lines 13--17 | `versions` | `voisines` | low |
| 343 | lower, lines 13--17 | `testées` | `telles` | low |
| 343 | lower, lines 13--17 | `excepté que je` | No secure alternative | low |
| 343 | lower, lines 13--17 | `suis` | No secure alternative | low |
| 344 | upper, lines 2--4 | `1)` | No secure alternative | low |
| 344 | upper, lines 2--4 | `\mathrm{GP}(1)` | No secure alternative | medium |
| 344 | upper, lines 2--4 | `associées` | No secure alternative | medium |
| 344 | upper, lines 2--4 | `\mathbb P` | `\mathcal P` | medium |
| 344 | upper middle, line 6 | `\mathcal M` | No secure alternative | medium |
| 344 | upper middle, line 7 | `v` | `\nu` | medium |
| 344 | upper middle, line 8 | `aura` | `a` | medium |
| 344 | upper middle, line 9 | `v` | `\nu` | medium |
| 344 | upper middle, line 9 | `v` | `\nu` | medium |
| 344 | middle, lines 12--13 | `a')` | No secure alternative | medium |
| 344 | middle, lines 12--13 | `localmt` | `localt` | medium |
| 344 | middle, lines 14--16 | `e_0` | `E_0` | medium |
| 344 | middle, lines 14--16 | `\rho.` | No secure alternative | low |
| 344 | lower, lines 20--22 | `b'')` | No secure alternative | medium |
| 344 | lower, lines 20--22 | `:` | No secure alternative | medium |
| 344 | lower, lines 20--22 | `est` | `étant` | medium |
| 344 | lower, lines 20--22 | `isomorphe` | No secure alternative | low |
| 344 | lower, lines 20--22 | `loc$^{\mathrm t}$` | No secure alternative | low |
| 344 | lower, lines 23--24 | `est` | `$\to$` | medium |
| 344 | lower, line 24 | `v` | `\nu` | medium |
| 344 | bottom, lines 25--26 | `loc$^{\mathrm t}$` | `local$^{\mathrm t}$` | medium |
| 344 | bottom, lines 25--26 | `p.r.` | `p.v.` | medium |

### Scans 345–349

| Scan | Approximate line or location | Reading in transcription | Alternative(s) | Confidence |
|---|---|---|---|---|
| 345 | Opening display (3), upper right entry | Latin `v` | Greek `ν` | Medium |
| 345 | Upper-right margin, line following “d'où” | `ρ e₁ = −v ρ e₀ − w e₀` | The overwritten right-hand side is not secure; no replacement from the companion matrix has been made | Low |
| 345 | Proof of a⇒b, deleted word before inserted “fibre” | `corps` | No alternative secure | Low |
| 345 | Deleted clause immediately after c⇔c′ | `car les` | Possibly an abbreviated connective followed by an article | Low |
| 345 | Following the companion matrix in the proof, before “précisément” | `st.` | Possibly a contracted “sont” with no visible full ending | Medium |
| 345 | Parenthesis in the transpose argument, deleted word | `d'ailleurs` | Possibly “donc”; cancellation obscures the middle | Low |
| 345 | Transpose argument, after `ρ = ᵗ(ᵗρ)` | Deleted right brace | Possibly a cancelled closing punctuation stroke | Low |
| 345 | Last inserted clause before “par chgt de base” | `stable` | A contracted spelling or abbreviation of the same word | Medium |
| 346 | NB, opening words | `En` in “En fait” | The first word is overwritten | Medium |
| 346 | NB parenthesis, after “et” | Barred `m` sign | An equality-like sign | Medium |
| 346 | Immediately below (6) | `OPs` | An abbreviated “On peut supposer”; the exact capital/lowercase sequence is uncertain | Medium |
| 346 | Immediately below (6), after `α ∈ Γ` | `SG` | `SL(2)` | Low |
| 346 | Cancelled heading preceding corollary 2 | `ε` following “Soit” | No alternative secure | Low |
| 346 | Corollary 2, second section named after `ρ` | `ζ` | `ξ` | Medium |
| 346 | Corollary 2(a), cancelled sign after `ζ` | `≠` | No alternative secure | Low |
| 346 | Paragraph following (a), (b) | `Ce n'est` | `Ce ne sont` | Medium |
| 346 | Same paragraph, deleted short word after “cor. 1” | `de` | No alternative secure | Low |
| 346 | Boxed determinant expression (8) near bottom | Latin `v` in `c²v` | Greek `ν` | Medium |
| 347 | First paragraph, before “donc” | `OPs` | An abbreviated “On peut supposer”; precise casing uncertain | Medium |
| 347 | First paragraph, cancelled connective before “On aura” | `et` | No alternative secure | Low |
| 347 | After the long cancelled calculation, “et si u…” | `commute` | Letters are crossed by other ink | Medium |
| 347 | Last equality line of centralizer proof | `≠` between the two evaluations at the first basis vector | `=` | Low |
| 347 | Same line, right-hand evaluation after the doubtful sign | `u(e′₀)` | `u′(e₀)` | Low |
| 347 | Definition, after the first sentence | `Itm` | `Item` | Medium |
| 348 | Condition d′, cancelled prefix before the existence sign | `Si` | No alternative secure | Low |
| 348 | Before “De plus”, cancelled word | `Dém` | No alternative secure | Low |
| 348 | Final definition, after cancelled “dit” | `que` | The cramped word may be part of a further revision | Medium |
| 348 | Final definition, before `det N = tr N = 0` | `ssi` | `si` | Low |
| 349 | Condition d, label above the left-pointing isomorphism | `φ` | `ψ` | Medium |
| 349 | Remark heading next to “Rmq”, cancelled word | `Corol` | Possibly a longer contraction of “Corollaire” | Medium |
| 349 | Equation (12), discriminant expression | Latin `v` | Greek `ν` | Medium |
| 349 | Deleted short word after “Les P” near bottom | `en` | Possibly the beginning of a different cancelled construction | Low |
| 349 | Isolated short word after “dans M.” in the projector definition | `Dém.` | `leur.` | Low |


### Scans 350–354

| Scan | Approximate line/position | Reading | Alternatives | Confidence |
|---|---|---|---|---|
| 350 | Top manuscript numeral | 476 | Final digit not fully distinct | medium |
| 350 | Line 1, deleted before P | N | Overwritten letter not recoverable with certainty | low |
| 350 | Line 1, deletion before “tore” | sous | Short cancelled word | low |
| 350 | Line 2, after “des” | α | Letter overwritten | low |
| 350 | Line 3, deleted before D₀ | la droite | les droites | medium |
| 350 | Line 3, deleted after D₀ | induisent | infinitive/ending unclear | medium |
| 350 | Above line 3, cancelled insertion | le couple des | Several letters obscured by a cancellation line | low |
| 350 | Upper right insertion | p.r. | p.v. | low |
| 350 | Line 6, cancelled phrase | commutant | comparant | low |
| 350 | Below (14), cancelled word | aura | donc | low |
| 350 | Remark, ε subscript | ε₁ | ε without an index, or ε≠1 | low |
| 350 | Inserted qualification of N | nilp. régul. | nilp. régulier | medium |
| 350 | Remark, “cela revient au” | m with overbar | =; lower stroke very compressed | medium |

| Scan | Approximate line/position | Reading | Alternatives | Confidence |
|---|---|---|---|---|
| 351 | First line, group before PG | GP(1) | First occurrence compressed; repeated clearer below | medium |
| 351 | Lines 2–3, three Aut subscripts | S-gr | S-gp | medium |
| 351 | Overwritten letter before P | N | Earlier letter substantially overwritten | low |
| 351 | “le … Borel” | m with overbar | =; lower stroke very compressed | medium |
| 351 | Cancelled word below “proviennent” | prov. | Exact earlier word not recoverable | low |
| 351 | Right margin beside (16) | vraiment joli | “vraiment” and final ending faint | medium |
| 351 | After “question de” | l'équi. | équi. without initial article | medium |
| 351 | Cancelled word after “ρ régulière” | Une | Ute / La | low |
| 351 | Next line, cancelled before “la conjugaison” | une | un | low |
| 351 | Cancelled invariant name at (19) | δ(ρ) | Δ(ρ) | low |

| Scan | Approximate line/position | Reading | Alternatives | Confidence |
|---|---|---|---|---|
| 352 | First line, end | qu'on | que | medium |
| 352 | Second line, first word | trouve | trouver | medium |
| 352 | Below (20) | soit | reste; overwritten form | low |
| 352 | Proposition, cancelled before conjuguées | équi | équi- | medium |
| 352 | Proposition, far-right cancellation after “il f.” | et s. | Abbreviation partly obscured and at edge | low |
| 352 | Normalization paragraph | OPS | O.P.S.; “on peut supposer” shorthand | medium |

| Scan | Approximate line/position | Reading | Alternatives | Confidence |
|---|---|---|---|---|
| 353 | Parenthesis below square-zero algebra | nbs duaux | nbres duaux | medium |
| 353 | Cancelled phrase after first condition's ε̃₀ | ε̃₁, tous deux | Precise cancelled phrase obscured | low |
| 353 | First condition, verb | soit | soient; overwritten ending | medium |
| 353 | Slanted right margin above (25) | relèvement plus conv. | relèvement plus commode; middle words uncertain | low |
| 353 | Cancelled scalar, both marginal equations | λ₀ | λ with a different overwritten subscript | medium |

| Scan | Approximate location | Reading | Alternative / issue | Confidence |
|---|---|---|---|---|
| 354 | First line | non-homothétiques | non homothétiques; a short intervening stroke may or may not be a hyphen | Medium |
| 354 | Upper block, cancelled word beneath insertion épinglage | scindage | Cancellation crosses the middle of the word; no secure alternative | Low |
| 354 | Parameter conditions below (26), tiny cancelled mark under w′ | ρ | Possibly an abandoned prose initial p; the remainder is crossed through | Low |
| 354 | (27), upper right entry of final ε₀ matrix | ? | A visible question-mark-like form is written heavily over an earlier vertical character, possibly 1 | Medium |
| 354 | (27), upper left entry of the second product matrix, denominator | w′ | u′; the ink has the multi-stroke form of w but remains ambiguous | Low |
| 354 | (27), lower left numerator of the second product matrix | vw′−wv′ | vw′+wv′; the sign is overwritten | Low |
| 354 | (27), lower left denominator of the second product matrix | w′v′ | u′v′; the first letter has two low humps, resembling the doubtful w′ in the upper left denominator | Low |
| 354 | (27), above the equality before the final ε₁ matrix | déf. | A densely retraced abbreviation, likely indicating definition | Low |
| 354 | (27), lower left entry of final ε₁ matrix | 1 | Overdrawn previous form is not securely separable | Medium |
| 354 | Cancelled fraction following (28) | (vw′+wv)/(uv) | (vw′−wv)/(uv); the cancellation obscures the sign | Low |
| 354 | Line between (29) and (30) | croisant | The middle and ending of this word are compressed; no alternative is secure | Low |
| 354 | Left note below (30) | coeff. | Possibly coef.; the f strokes are compressed | Medium |
| 354 | (31), lower right entry of N₀ | 0 | 1; a dark overwritten loop obscures the prior and final stroke sequence | Low |


### Scans 355–358

| Scan | Approximate line or position | Reading in transcription | Alternative or issue | Confidence |
|---|---|---|---|---|
| 355 | 4, addition above right | `régulières` (deleted) | Overstruck, but the word is probable. | medium |
| 355 | 5, insertion | `Posons` | Compressed ending above the canceled heading. | medium |
| 355 | 6, left of first display | `\varepsilon` | Possibly an abandoned “et”; isolated mark. | low |
| 355 | 10, overwritten verb | `sont` (deleted), `est` (inserted) | The original plural verb is largely overwritten. | low |
| 355 | 10 | `unipotents` | `unipotent`; the final stroke may be a canceled or retained plural ending. | medium |
| 355 | 10 | `réguliers` | `régulier`; same uncertainty about the retained ending. | medium |
| 355 | 10, far right, deleted | `partout` | Heavily overlaid by the parenthetical equivalence. | low |
| 355 | between 11 and 12, deleted | `non équivalents, i.e.` | The canceled phrase is crossed by subsequent insertions. | low |
| 355 | left of display (32), successive old labels | `(32)`, `(33)`, `(34)` | All three former labels are densely overstruck; the second is especially uncertain. | low |
| 356 | display (35), second matrix, upper-right entry | deleted `1`, followed by `?` | The entry is blackened and overwritten; the surviving hook and dot may be a question mark or remnants of another coefficient. Its later value is deliberately not substituted. | low |
| 356 | left diagonal margin, final lines | `u,w,v` | The last two letters are compressed; the ordering `u,v,w` cannot be excluded from the ink alone. | low |
| 356 | left, between (36) and the next paragraph | deleted `(37)` | The old tag is heavily overstruck. | low |
| 356 | display following “On aura dans (35)” | `(38)` | The overwritten final digit is probable but not secure. | medium |
| 356 | proof, approximate line 14 | `vu` | `vue`; the final stroke does not resolve the ending. | medium |
| 356 | first operator in the determinant expansion | `det` | Retraced ink obscures the first operator; no earlier reading can be recovered securely. | medium |
| 356 | approximate line 22 | `on aura` | Very faint short strokes. | medium |
| 356 | final equation tag | `(*)` | `(6)` or another altered tag; the ink is not a clear numeral. | low |
| 356 | final sentence | `mb` | `membre`; the terminal strokes may abbreviate or continue the word. | medium |
| 357 | approximate line 9, deletion | `c’est en` | `c’est un`; the final small group is crossed out. | low |
| 357 | diagonal corollary, first deleted symbol after “de” | `N₀` | The subscript is obscured by cancellation. | low |
| 357 | diagonal corollary, middle | `évidemment` | `évidente`; the ending is compressed and crossed by adjacent strokes. | low |
| 357 | diagonal corollary, middle | `sous-Module` | `sous-module`; capitalization is unclear. | medium |
| 357 | diagonal corollary, lowest compressed line | `remplacer` | The word is interrupted by the neighboring body text. | medium |
| 357 | approximate line 12, after the first σ with tilde | subscript `1` | May instead be an abandoned stroke adjacent to the comma; both the numeral reading and its attachment remain doubtful. | low |
| 357 | approximate line 13 | `est` | Overwritten verb before “en fait”; no secure earlier layer. | medium |
| 357 | approximate line 20 | `simplifier` | `normaliser`; the upper strokes and ending are difficult to distinguish. | low |
| 358 | canceled line under the inserted question | `notera` | `note`; the continuation after the t is crossed out. | medium |
| 358 | same canceled line | `entièrement déterminé` | Most letters remain visible, but the deletion traverses both words and obscures their endings. | medium |
| 358 | beginning of next line, deletion | `par` | Small, densely crossed-out group before the retained “par”. | low |
| 358 | left object of diagram (43) | deleted `stri.` | Probably an abbreviation of “stricts” or “strictement”; its exact ending and punctuation are not clear. | low |
| 358 | parenthesis below (43), overlapping layers | deleted `fppf`, inserted `fppf`, deleted `Zar.` | Both an fppf-like cluster and a Zar-like cluster are present, but their stratification and punctuation are especially insecure. The transcription attempts the visible layers instead of silently choosing a topology. | low |
| 358 | lower-left marginal note | `rég` | Abbreviated regularity qualifier; a final abbreviation point may be absent or obscured. | medium |

### Particular reading decisions

The exponent and sign in (75) on scan 341, its following (75)/(76) label on scan 342, and the heavily canceled early calculations remain doubtful. The additional equality on scan 340 preferentially reads `\widetilde\rho(N_1)` from the ink. The final insertion on scan 343 was independently read but remains insecure. The compressed *localement* abbreviations, the verb after T in scan 344, and the hooked mark before “isomorphe” are explicitly flagged.

The determinant parameter's open, upward-ending glyph may be Latin v or Greek ν. The transcription flags its definition-linked occurrences and uses the preferred reading for repetitions; it does not alternate alphabets merely to fit mathematical expectations. The parameter w is not silently changed to Greek omega. The general and special linear group names retain the visible script ell, while the projective name read as GP(1) is not replaced by a modern convention.

On scan 353, the last argument in (23) visibly reads ε̃₁, while (24) has ε₀. The four dashes in (25) are manuscript ditto marks. On scan 354, the repeated label (26), the two denominator ambiguities in (27), and the sequence “w′+w=u … w′=w−u” are retained. The blackened upper-right matrix coefficient on scan 356 is not supplied from a later calculation. Scan 357 retains ε₁=−σ⁻¹ρ, its reference b⇔c, and both occurrences of label (40). Scan 358 retains the ink-based parenthetical ε₀=−σρ⁻¹. These are readings of the supplied pages, not proposed corrections.

## 3. Abbreviations met

Expansions are explanatory and appear only in these notes. Grouped variants preserve differences encountered on the pages. An uncertain abbreviation is not expanded in the transcription.

| As written | Probable expansion or function |
|---|---|
| i.e. | id est; c'est-à-dire |
| $\overline{\mathrm m}$ | même |
| tte | toute (reading uncertain on scan 340) |
| Tr | trace |
| det | déterminant |
| mbs | membres |
| dfn | définition; equality by definition |
| inv. | inversible |
| hyp. | hypothèse |
| V. p. | voir page |
| cf | confer; comparer / voir |
| NB | nota bene |
| néc. | nécessairement |
| loc. | localement |
| localmt / localt | localement; exact abbreviation uncertain |
| locᵗ / localᵗ | localement; superscript t retained in the transcription |
| Zar | Zariski |
| End | endomorphismes; the underline is retained where visible |
| p.r. / p.v. | probably « par rapport »; r/v remains uncertain |
| OK | assent to the immediately preceding calculation |
| `loc.`, `loc` | localement |
| `p.r.` | par rapport |
| `chgt` | changement |
| `Dém`, `Dém.` | démonstration |
| `op.` | opérateur |
| `st.` | sont, probably abbreviated |
| `p.ex.` | par exemple |
| `autom.` | automorphismes |
| `fppf` | fidèlement plat et de présentation finie |
| `top.` | topologie |
| `ét` | étale |
| `ds` | dans |
| `OPs` | probably “On peut supposer” |
| `f. et s.` | faut et suffit |
| `cor.` | corollaire |
| Barred `m` | même |
| `cqfd.` | ce qu'il fallait démontrer |
| `prop.` | proposition |
| `Itm` / `Item` | item, functioning as “de même” |
| `ssi` | si et seulement si |
| `pt` | point |
| `mod` | modulo |
| `resp.` | respectivement |
| `Rmq` | remarque |
| `Corol` | corollaire |
| `condit.` | conditions |
| `corr.` | correspondance |
| “p.r.” (reading uncertain, possibly “p.v.”) | probably *par rapport*. |
| “proj.” | *projecteur*. |
| “él.” | *élémentaire*. |
| “nilp.” | *nilpotent*. |
| “régul.” | *régulier*. |
| “dim” | *dimension*. |
| “isom.” | *isomorphe*. |
| “iso” | *isomorphismes*. |
| “Aut” | *automorphismes*. |
| “gr” (subscript reading uncertain) | probably *groupes*. |
| “équi.” (deleted) | probably *équi-* in *équiconjugaison*, but the intended completed word is uncertain. |
| “pt” (deleted) | *point*. |
| “prov.” (deleted, reading uncertain) | probably an abandoned beginning of *proviennent*. |
| “autos” | *automorphismes*. |
| “int.” | *intérieurs*. |
| “il f.” | probably *il faut*. |
| “et s.” (deleted and uncertain) | probably *et suffit*. |
| “OPS” (reading uncertain) | probably *on peut supposer*. |
| “OK.” | affirmative conclusion. |
| “nbs” / “nbres” (uncertain) | *nombres*. |
| “rg” | *rang*. |
| “conv.” (uncertain) | probably *convenable*. |
| élém. | probably *élémentaire*. |
| coeff. | probably *coefficient*; spelling itself is doubtful. |
| déf. | probably *définition*; reading itself is doubtful. |
| Γ | mathematical notation for sections; not expanded in the transcription. |
| `p.` | page |
| `loc. cit.` | loco citato; à l’endroit cité |
| `isom` / `isom.` | isomorphisme |
| `hyp` | hypothèse |
| `mb` / `mbs` | membre / membres |
| `qfd.` | ce qu’il fallait démontrer |
| `nᵒ` | numéro |
| `combin. lin.` | combinaisons linéaires |
| `stri.` (deleted, doubtful) | stricts / strictement; exact intended expansion uncertain |
| `unipot.` / `unip.` | unipotent, with inflection determined by the surrounding sentence |
| `Zar.` (deleted, doubtful) | Zariski |
| `rég` | régulière, in the final-page marginal note |

## 4. Legibility and verification limits

The uncancelled prose and large displays are generally more legible than the rapid revisions. The weakest regions are the overwritten calculations on scans 340–342, the final insertion on scan 343, the small marginal formula on scan 345, the crowded wording and primes on scans 347–348, the canceled upper passage and overlapping additions on scan 350, the matrix entries on scans 354 and 356, the lower lines of the long diagonal corollary on scan 357, and the overlapping fppf/Zar revisions below (43) on scan 358. Several marks permit only a tentative attempt. The doubt table is part of the transcription's evidential limits and should remain with it.

Every supplied scan was read as a whole and then in enlarged regions, and its text was compared against the draft. Independent passes concentrated on the first five pages, the final matrix calculations, and the last page's notation. The final page received the same transcription and inventory treatment as the earlier pages; its question about uniqueness is not completed from a later source.

The inventory and marker concordance are checked mechanically against the assembled files, along with page order, brace balance, and environment pairing. These checks establish structural coverage, not certainty of the handwriting. The temporary TeX verification environment lacks its document classes and package tree, including tikz-cd, so no successful full typesetting compilation is claimed. No rendered PDF is part of the requested deliverable.

## 5. Research notes — separate from the transcription

All manuscript citations in the entries below refer to **Grothendieck (1981), supplied scan and location as indicated**. They are reading notes based on these pages, not a survey of the later manuscript or of published literature. A claim flagged here may be proved or qualified elsewhere. Own ideas are labeled, with a confidence assessment and reason, and are not presented as established or new results. Nothing in this section changes the diplomatic text.

### Research note 1

**Scan 340, opening paragraph — conjecture / expectation**

The statement « Ce calcul suggère fortement » introduces the expectation that the relations numbered (64) already imply (68), followed by a proposed reduction to fibrewise independence of the two epsilon sections. The preceding definitions and numbered relations lie outside this packet, so the logical dependency should be reconstructed from the adjacent manuscript before treating this as a proved equivalence. The cancelled parts of the ensuing argument must be distinguished from the surviving argument when doing so.

### Research note 2

**Scan 340, cancelled middle calculation — unproved claim**

The cancelled sentence « un calcul immédiat donne aussi » promises an additional computation, but its accompanying expression stops after a partly written term involving N₁. A verification would need to identify the precise conjugation actions and the scalar by which they act on the assumed common line. This is an abandoned proof step, not an assertion endorsed by the finished text.

### Research note 3

**Scan 340, surviving λ² and λ³ line — own idea**

The pair of scalar relations λ² = λ³ = 1 suggests isolating a short algebraic lemma before revisiting the manuscript's conjugation calculation: in any commutative ring these two equalities force λ = 1. The open work is to justify both equalities from the particular actions, with all nonvanishing and fibre restrictions stated. Confidence: high for the scalar implication, conditional for its application here; the reason is the direct identity λ = λ·λ² = λ³ = 1.

### Research note 4

**Scans 341–342, remark and continuation — conjecture / expectation**

« Je ne serais pas étonné » proposes an alternative set of conditions equivalent to (51)–(56), using the polynomial identities and regular unipotence in (75), with additional regularity of σ and ρ if needed. The visible exponent and one sign in (75) remain doubtful in the transcription, so the research problem should first be fixed from the ink and the adjoining manuscript. The desired consequence is explicitly described on scan 342 as the idempotence of N = ρ + σ.

### Research note 5

**Scan 342, (75)/(76)–(77) and question mark — unpursued implication**

The parenthesis « ce qui équivaut, si N régulier » is followed by the trace and determinant conditions and an explicit question mark. A proof audit should separate the direction supplied by the characteristic identity from the direction that uses regularity to exclude the two scalar idempotents on fibres. In particular, the argument should record whether “regular” is being used as an everywhere fibrewise condition and how the assertion behaves on a nonreduced base.

### Research note 6

**Scan 343, final paragraph — conjecture / unresolved question**

The closing « Ce n'est pas entièrement élucidé -- à revenir à la charge! » explicitly leaves the proposed equivalence unresolved at this point. The displayed reduction identifies det N = 0 with the trace identity numbered (69), under the normalizations used in the calculation. The suggested return to an argument based on (68), rather than (75), supplies a concrete proof route to compare with the later recap.

### Research note 7

**Scan 344, regularity proposition — unpursued implication**

The proposition places fibrewise nonscalarity, the rank-two subalgebra generated by ρ, cyclic vectors, and companion forms in one equivalence list. Some conditions are explicitly restricted to M = End(F), and their locality qualifiers differ on the page. Tracking those qualifiers through the proofs on the following scans is necessary before using the result over a nonsplit Azumaya algebra.

### Research note 8

**Scan 344, condition c — own idea**

Test whether the isomorphism in condition c is intended only locally: take F = L ⊕ L for a nontrivial invertible sheaf L, with ρ acting by 0 and 1 on the two summands. Fibrewise ρ is nonscalar, whereas the module over O[T]/(T(T−1)) corresponds to the pair (L,L), so a global identification with the algebra itself would force trivializations of both copies of L. Confidence: high as a proposed test of a global reading, because the two idempotent summands recover the two line bundles; this does not alter the transcription and does not claim a new result.

### Research note 9

**Scan 345, proof after condition d′ — unproved claim.** The equivalences `a⇔a′` and `b⇔b′⇔b″` are called “trivial,” with the first justified only by “algèbre linéaire.” A detailed proof should specify how fibrewise non-scalarity implies that the span of 1 and ρ is a locally free direct summand, and how a cyclic vector on one fibre lifts to a cyclic local section. Over a general base, these steps require local freeness and the invertibility of an appropriate determinant, not merely a calculation over a field.

### Research note 10

**Scans 345 and 347, condition d and its continuation — unproved claim.** The centralizer is asserted to remain `O_S + O_Sρ` “après chaque chgt de base.” The calculation on scan 347 explains why a commuting endomorphism is determined by its value on a cyclic vector; the remaining structural point worth spelling out is the descent of this presentation from a local splitting of the Azumaya algebra and its compatibility with arbitrary base change. The visible cancellation at the end of the calculation should not be used to infer a different algebraic claim.

### Research note 11

**Scan 346, NB and the parenthesis after corollary 2 — unproved claim.** The statement “On peut alors prendre α ds SG…” deserves an explicit locality qualification. The preceding NB refers to the fppf quotient and to the étale topology when 2 is invertible, whereas the corollary itself first asks for a solution “loc. Zar.” A proof should track which base changes are used when a conjugator is lifted or adjusted to determinant one, rather than treating all these localities as interchangeable.

### Research note 12

**Scan 346, corollary 3 — unpursued implication.** “L'indétermination de α” is described by right multiplication by a unit of `A_ρ`. This suggests viewing the local solution space of the displayed commutator equation as a torsor under the unit group of the quadratic centralizer algebra. The distinction between local solvability and a global section could then be expressed as a gluing problem; the manuscript's corollary provides the stabilizer calculation but does not pursue that formulation here.

### Research note 13

**Scan 347, corollary 1 — own idea.** Investigate the global obstruction left after regular sections have the same trace and determinant, since the stated conjugacy criterion is local. One possible approach is to use the isomorphism torsor of the associated cyclic modules over the common quadratic algebra. **Confidence: medium** that this is a useful formulation: the local companion matrices and the centralizer formula directly suggest it, but a complete global statement needs careful hypotheses on the base and the Azumaya algebra.

### Research note 14

**Scan 348, proposition and “De plus” paragraph — unproved claim.** The equivalent descriptions in terms of a regular unipotent section, a nilpotent endomorphism, a line subbundle, and a Borel are stated without a separate proof on this page. A proof should establish that image and kernel give the indicated line bundle, construct the local Jordan basis used in c′, and verify the uniqueness and descent of the corresponding Borel. The assertion that D determines N “mod homothétie” also needs its precise local or sheaf-theoretic meaning specified.

### Research note 15

**Scan 348, final definition — own idea.** Test why the adjective “strictement” is attached to the trace-and-determinant definition of nilpotence over nonreduced bases. For example, over `k[η]/(η²)` with characteristic not 2, the scalar matrix `N = η I₂` satisfies `N² = 0` but has nonzero trace `2η`, so square-zero alone does not imply the displayed strict condition. **Confidence: high** in this example, because both assertions follow directly by multiplication and trace; it is a proposed explanatory test, not an emendation of the definition.

### Research note 16

**Scan 349, remark and equation (12) — unpursued implication.** The sentence “cet argument montre, plus généralement” gives invertibility of the discriminant as a sufficient condition for regularity. It would be useful to separate this open locus from the full regular locus: the regular nilpotent forms of scan 348 suggest that zero discriminant need not obstruct regularity. This comparison could organize the semisimple and unipotent cases within the same centralizer-algebra picture.

### Research note 17

**Scan 349, final corollary — unproved claim.** The page announces “une corr. biunivoque” between elementary projectors and Killing pairs `(B,T)`, and the sentence continues on the next scan. A complete verification should recover an ordered decomposition into two line subbundles from the projector, identify the associated torus and Borel, and check the inverse construction. This is flagged for comparison with that continuation, not treated as an unfinished argument in the manuscript as a whole.

### Research note 18

**Scan 350, remark; unproved claim.** “Le schéma des … est un fibré en droites épointées” identifies the scheme of regular unipotents (alternatively regular nilpotents) over the Borel scheme with a punctured line bundle. The precise assertion would require checking the associated line bundle and its transition functions, as well as the conventions used for the three forms \(G\), \(SG\), and \(PG\).

### Research note 19

**Scan 350, remark; unproved claim.** The statements “lisse de dim relative 2” and “fibré-lisse de dim relative 1” give smoothness and relative dimensions without an argument on this page. A proof should distinguish the dimension over the base from the dimension over the Borel scheme and verify that these assertions survive the relevant descent.

### Research note 20

**Scan 350, final paragraph; unproved claim.** The asserted identification of a fibre product with “le schéma des épinglages” is presented without construction here. A verification would have to specify both maps to the Borel scheme and construct mutually inverse maps between the fibre product and pinning data.

### Research note 21

**Scan 350, (13)–(14); unpursued implication.** The passage to the opposite pair replaces the displayed projector by “1-N,” preserving the author’s notation. This suggests studying the involution on the projector parameter space and its compatibility with the two Borel projections; the notation should be checked against adjacent pages before formulating a formal statement.

### Research note 22

**Scan 351, opening continuation; unproved claim.** The pinning scheme is described as “un torseur” under a sequence involving \(GP(1)_S\) and automorphism schemes of the three displayed groups. The exact scope of the handwritten automorphism subscripts should be settled before assessing the claimed identifications; in particular, one must distinguish all automorphisms from any restricted automorphism functor intended here.

### Research note 23

**Scan 351, (15)–(16); unproved claim.** “On vérifie que ceci revient aux relations suivantes” presents the association of a projector and a regular unipotent through \(PN=0\) and \(NP=N\). A proof should identify the kernel/image lines and check both directions of the equivalence with the preceding pinning description.

### Research note 24

**Scan 351, (17)–(19); unpursued implication.** The trace-square divided by determinant is invariant under scalar rescaling and conjugacy by the displayed calculation. This naturally raises the separate question of when it is a complete invariant of local projective conjugacy; the following page begins that question.

### Research note 25

**Scan 352, proposition and (21); unpursued implication.** The qualification “Ces conditions sont suffisantes quand … Trρ inv.” singles out the unit-trace locus for completeness of the invariant under local fppf conjugacy. This is stronger than mere nonzero trace on a general base, and the distinction is essential to the displayed division by the trace at the end.

### Research note 26

**Scan 352, normalization paragraph; unproved claim.** “loc. fppf, existe λ” invokes a square root of a unit to normalize determinants, without spelling out the cover. The relevant construction to check is the finite locally free cover obtained by adjoining a root of \(X^2-\det(\rho')/\det(\rho)\), including its faithful flatness in residue characteristic two.

### Research note 27

**Scan 352, final paragraph; unpursued implication.** The equation \(\tau'^2=\tau^2\) yields the displayed \(\mu_2\)-valued ratio when \(\tau\) is invertible. The proof therefore does not require replacing \(\mu_2\) by the two constant signs; the group-scheme formulation retains information when two is not invertible.

### Research note 28

**Scan 352, (20)–(22); own idea — confidence: medium.** One could study the conjugacy quotient on the complementary trace-zero locus using infinitesimal test bases. The reason is that the proof breaks precisely at division by \(\tau\), and the next scan supplies square-zero examples that may detect information lost by squaring the trace; this is a proposed line of analysis, not a claim of novelty or a completed result.

### Research note 29

**Scan 353, opening remark; unproved claim.** “il y a des contre-exemples évidents” is followed by two companion matrices over \(A_0[w,w']/(w^2,ww',w'^2)\). A complete proof should explicitly show that their traces cannot become unit multiples under the relevant faithfully flat extensions, rather than checking only that their squared traces and determinants agree.

### Research note 30

**Scan 353, square-zero example; own idea — confidence: high as a proposed test, not as a completed theorem.** The example can be read as a test of whether the invariant loses first-order directions at trace zero. The reason is visible in the algebra: the two independent square-zero parameters have equal squares, whereas the matrices retain those parameters as their respective traces.

### Research note 31

**Scan 353, between (23) and (25); unproved claim.** “proviennent canoniquement” asserts canonical lifts of the two regular projective unipotents to \(SG\). This merits a proof of existence, uniqueness, and compatibility with the displayed conjugation actions over general bases, including nonreduced bases and residue characteristic two.

### Research note 32

**Scan 353, margin beside (25); unproved claim.** The marginal replacement of scalar coefficients by a minus sign depends on a suitable choice of lifts of the projective sections; the explanatory words in that margin remain uncertain. A precise argument would identify the permitted scalar changes and show that both formulas can be normalized simultaneously.

### Research note 33

**Scan 353, condition 2; unpursued implication.** “en chaque fibre ‘non équivalents’” strengthens a global inequality to a fibrewise condition. The ensuing normal-form discussion should be checked for exactly where this condition supplies an invertible coefficient and a global or local splitting.

### Research note 34

**Scan 354, upper block — unproved claim.** “définissent un … épinglage canonique” asserts a canonical pinning from the two unipotent data after the fibrewise nonhomothety condition. A proof should identify the two corresponding root subgroups, justify the choice of the root-group section, and check the stated canonicity under change of trivialization and base change.

### Research note 35

**Scan 354, (27)–(29) — unpursued implication.** The displayed normalization makes one unipotent matrix have lower off-diagonal entry 1 and relates the parameters of ρ and σ. The line “w′+w=u … w′=w−u” contains a visible sign discrepancy; studying the claimed normal form requires distinguishing that written discrepancy from the intended identities rather than silently replacing it.

### Research note 36

**Scan 354, (30) and adjoining text — unproved claim.** “ce qui détermine σ en termes de ρ … et de P” follows the claimed relation ρ+σ=uP. To turn this into an intrinsic reconstruction, one should specify how u and the elementary projector are recovered from the original pair and verify that the reconstruction has the required determinant and unipotence properties.

### Research note 37

**Scan 354, final display — own idea, medium confidence.** The ratio u/v in ε₀ and the normalization of ε₁ suggest that the remaining pair can be organized by a small number of scalar invariants after the pinning is fixed. This is suggested by the actual displayed matrices, but a classification would still require checking residual conjugation and descent over the base; it is not asserted here as established or new.

### Research note 38

**Scan 355, opening lines; kind: conjecture (expectation / stated aim, not a formal conjecture).** “On aimerait donner des ‘critères numériques’ intrinsèques” states the aim of replacing coordinate-dependent conditions on the pair by intrinsic conditions. The proposition that follows pursues that aim on these same pages; the wording should not be treated as an unresolved conjecture independently of the subsequent proof.

### Research note 39

**Scan 355, condition (b) and its right margin; kind: unproved claim.** The marginal assertion “ceci exprime que ε₀ est régulier et indépendant de ε₁” attaches regularity and independence to invertibility of `Tr(σ+ρ)`. A full proof requires the earlier cited proposition (p. 449′) or a direct fiberwise analysis followed by a scheme-theoretic argument over the base; that proof is not supplied in this margin.

### Research note 40

**Scan 355, bottom marginal note; kind: unpursued implication.** “P et u sont uniquement déterminés” identifies the scalar and projector through the trace of the sum. This suggests that the decomposition can be constructed compatibly with base change wherever that trace is invertible; the note itself gives formulas, not a separate base-change statement.

### Research note 41

**Scan 356, conditions (e), (f), and their margins; kind: unproved claim.** “cet isom est unique” and “cet φ est encore unique” assert uniqueness of the coordinate identification fixed by the stated data. The proof is introduced as “Démonstration facile,” but the detailed argument printed on this page concerns the determinant identity; an independent verification of uniqueness would have to show that the remaining simultaneous centralizer acts trivially under the intended notion of isomorphism.

### Research note 42

**Scan 357, upper paragraph; kind: unproved claim.** The equivalence between `det Q=0`, invertibility of `Tr Q`, and `Q=uP` is said to follow from the previous results, followed by “que j’ai oublié d’expliciter.” The direct proof suggested by the displayed conditions is to take `u=Tr Q` and use the rank-two characteristic equation to check that `P=u⁻¹Q` is idempotent; verifying that it is an elementary projector requires the relevant regularity or fiber-rank criterion from the preceding pages.

### Research note 43

**Scan 357, diagonal corollary; kind: unproved claim.** “1,N₀,N₁,P forment une base” and the later replacements by ρ and σ are stated in the margin without a proof there. The two accompanying linear formulas suggest checking the determinants of the corresponding changes of basis, using precisely the units required by the proposition, rather than reasoning only over geometric points.

### Research note 44

**Scan 357, main body; kind: unpursued implication.** “il reste la question de normaliser les relèvements” introduces the common rescaling that enforces `Tr(ρ+σ)=1`. This gives a candidate preferred lift of the projective pair when the required trace is invertible, but the subsequent page explicitly asks about its uniqueness; existence of the displayed normalization should therefore be kept distinct from uniqueness.

### Research note 45

**Scan 358, inserted question; kind: conjecture / explicit question.** “Y. a-t-il unicité de ρ,σ en termes de” the projective pair asks whether the preceding conditions and normalization determine the lifts. The page turns to a prerequisite concerning unipotent lifts, so this question is recorded as a question on this page, without assuming that it remains open later in the manuscript.

### Research note 46

**Scan 358, paragraph before (43); kind: unproved claim under examination.** “Je voudrais d’abord vérifier avec soin une assertion faite par la bande un certain nb de fois” introduces the proposed bijection between regular unipotents in G and PG. The text treats local surjectivity as a possible definition and explicitly isolates injectivity for proof, reaching only `λ²=1` by the end of the supplied page.

### Research note 47

**Scan 358, final display; kind: own idea. Confidence: high for the conditional example, with the base hypotheses still to be checked against the wider manuscript.** If the base permits characteristic two and nilpotents, test injectivity over `R=k[t]/(t²)` with `char k=2`, `ε=I+E₁₂`, and `ε′=(1+t)ε`. Both matrices have trace zero, determinant one, and regular square-zero differences from the identity, yet they have the same projective class and are distinct; this follows by direct matrix multiplication and the unit off-diagonal entry. This is a candidate obstruction to a scheme-level uniqueness statement under the usual trace/determinant definition, not a claim about the author’s ultimate assumptions or about novelty.

## 6. Complete explicit-marker concordance

This register has one row for every explicit uncertainty marker in the LaTeX fragment, including repeated readings. “Source line” is the line in the delivered `.tex`, not a new manuscript line number. Context is a condensed source extract used only as a locator; the detailed manuscript positions, alternative interpretations, and confidence assessments appear in §2. Parent editorial macros identify whether a mark occurs inside a cancellation, insertion, margin, or foliation. Where a token carries no second proposed reading, no alternative has been silently supplied.

| No. | Scan | Source line | Marker and literal reading | Editorial context | Nearby source |
|---|---|---|---|---|---|
| 1 | 340 | 3 | `\unsure{par\|en}` | main text / formula | `e calcul suggère fortement que les relations \unsure{par\|en} (64) impliquent déjà (68)\ldots{} c'est $\un` |
| 2 | 340 | 3 | `\unsure{\overline{\mathrm m}}` | main text / formula | `en} (64) impliquent déjà (68)\ldots{} c'est $\unsure{\overline{\mathrm m}}$ à peu de choses près une démonstration\ldot` |
| 3 | 340 | 3 | `\unsure{tte}` | main text / formula | `i.e. que $N_0,N_1$ sont non-homothétiques en \unsure{tte} fibre. Or (67)` |
| 4 | 340 | 6 | `\unsure{\deleted{\text{et}}}` | main text / formula | `(*) N_1=\widetilde\sigma(N_0),\ \unsure{\deleted{\text{et}}}\ \inserted{=\widetilde\rho(\unsure{N_1\|N_0})` |
| 5 | 340 | 6 | `\unsure{N_1\|N_0}` | inserted | `leted{\text{et}}}\ \inserted{=\widetilde\rho(\unsure{N_1\|N_0})}\ \deleted{N_0=\unsure{\widetilde\sigma(N_1` |
| 6 | 340 | 6 | `\unsure{\widetilde\sigma(N_1)}` | deleted | `detilde\rho(\unsure{N_1\|N_0})}\ \deleted{N_0=\unsure{\widetilde\sigma(N_1)}}\,\unsure{:}` |
| 7 | 340 | 6 | `\unsure{:}` | main text / formula | `deleted{N_0=\unsure{\widetilde\sigma(N_1)}}\,\unsure{:}` |
| 8 | 340 | 12 | `\unsure{(\deleted{74})}` | main text / formula | `\unsure{(\deleted{74})} N_1=\lambda N_0` |
| 9 | 340 | 15 | `\unsure{appliquant}` | main text / formula | `on en conclurait, en \unsure{appliquant} \deleted{$\widetilde\sigma$ et} utilisant $\` |
| 10 | 340 | 18 | `\unsure{(**)}` | deleted | `\deleted{\unsure{(**)}` |
| 11 | 340 | 20 | `\unsure{\deleted{=\lambda^2}}` | deleted | `N_0&=\lambda N_1\unsure{\deleted{=\lambda^2}},` |
| 12 | 340 | 29 | `\unsure{.}` | deleted | `\deleted{(**) N_0=\rho^{-1}N, N_1\unsure{.}}` |
| 13 | 341 | 54 | `\unsure{(**)}` | deleted | `\deleted{\unsure{(**)}}` |
| 14 | 341 | 60 | `\unsure{(**)}` | deleted, inserted | `t les déterminants \inserted{des deux mbs de \unsure{(**)},} on trouve (\deleted{\unsure{det}} admettan` |
| 15 | 341 | 60 | `\unsure{det}` | deleted, deleted | `x mbs de \unsure{(**)},} on trouve (\deleted{\unsure{det}} admettant que $\det\sigma=\det\rho=1$, ce q` |
| 16 | 341 | 65 | `\unsure{2}` | deleted | `ame{Tr}\sigma}_{0}+\underbrace{(\det\sigma)^{\unsure{2}}}_{1} \text{i.e.} 1=0}` |
| 17 | 341 | 70 | `\unsure{le}` | deleted | `\deleted{Je \unsure{le} \unsure{ve.}}` |
| 18 | 341 | 70 | `\unsure{ve.}` | deleted | `\deleted{Je \unsure{le} \unsure{ve.}}` |
| 19 | 341 | 82 | `\unsure{serais\|sera}` | deleted | `\deleted{Je ne \unsure{serais\|sera}}` |
| 20 | 341 | 87 | `\unsure{3\|2}` | main text / formula | `(75) \sigma^2+1=\rho^{\unsure{3\|2}}\unsure{-\|+}\rho+1=0,` |
| 21 | 341 | 87 | `\unsure{-\|+}` | main text / formula | `(75) \sigma^2+1=\rho^{\unsure{3\|2}}\unsure{-\|+}\rho+1=0,` |
| 22 | 342 | 104 | `\unsure{(75)\|(76)}` | main text / formula | `\unsure{(75)\|(76)} N^2-N=0` |
| 23 | 342 | 113 | `\unsure{c'était}` | main text / formula | `Mais $N$ est régulier, car si sur une fibre \unsure{c'était} un scalaire on aurait que (en se restreignan` |
| 24 | 342 | 118 | `\unsure{''}` | inserted | `-\inserted{\unsure{''}}\rho\sigma^{-1}&=\rho\sigma=\varepsilon_1=1+` |
| 25 | 342 | 122 | `\unsure{Prenant}` | deleted | `\deleted{\unsure{Prenant} $\unsure{\varepsilon_0=\det\rho}$}` |
| 26 | 342 | 122 | `\unsure{\varepsilon_0=\det\rho}` | deleted | `\deleted{\unsure{Prenant} $\unsure{\varepsilon_0=\det\rho}$}` |
| 27 | 342 | 137 | `\unsure{=}` | main text / formula | `2\sigma\unsure{=}\rho\sigma+2\underbrace{\sigma^2}_{-1}\rho` |
| 28 | 342 | 147 | `\unsure{4}` | deleted | `i.e. $\deleted{\unsure{4}}\ 2$ inv. et $\lambda=\dfrac{\varepsilon}{2}` |
| 29 | 343 | 162 | `\unsure{par}` | deleted | `\deleted{Mais $\operatorname{Tr}N=0$ \unsure{par}}` |
| 30 | 343 | 177 | `\unsure{''}` | main text / formula | `\unsure{''}` |
| 31 | 343 | 178 | `\unsure{(}` | main text / formula | `\det\unsure{(}\unsure{\deleted{\rho}\inserted{\sigma}}(1+\s` |
| 32 | 343 | 178 | `\unsure{\deleted{\rho}\inserted{\sigma}}` | main text / formula | `\det\unsure{(}\unsure{\deleted{\rho}\inserted{\sigma}}(1+\sigma^{-1}\rho)` |
| 33 | 343 | 184 | `\unsure{--}` | margin | `\margin{calcul déjà fait V. p. \unsure{--} ? (cf formule (69))}` |
| 34 | 343 | 187 | `\unsure{-}` | main text / formula | `+\rho)=2+\operatorname{Tr}(\sigma^{-1}\rho)=2\unsure{-}\operatorname{Tr}\sigma\rho, \text{donc}` |
| 35 | 343 | 196 | `\unsure{la}` | deleted | `Pour \deleted{\unsure{la}} prouver cette relation \inserted{(ou des \u` |
| 36 | 343 | 196 | `\unsure{versions\|voisines}` | inserted | `a}} prouver cette relation \inserted{(ou des \unsure{versions\|voisines} \unsure{testées\|telles})}, on peut songer à` |
| 37 | 343 | 196 | `\unsure{testées\|telles}` | inserted | `\inserted{(ou des \unsure{versions\|voisines} \unsure{testées\|telles})}, on peut songer à \deleted{partir}\inserte` |
| 38 | 343 | 196 | `\unsure{excepté que je}` | main text / formula | `ted{partir}\inserted{procéder} comme tantôt, \unsure{excepté que je} \unsure{suis} parti de (68) au lieu de (75).` |
| 39 | 343 | 196 | `\unsure{suis}` | main text / formula | `céder} comme tantôt, \unsure{excepté que je} \unsure{suis} parti de (68) au lieu de (75). Ce n'est pas` |
| 40 | 344 | 206 | `\unsure{1)}` | deleted | `\deleted{\unsure{1)}} On désigne par $G,SG,PG$ des formes de $\ma` |
| 41 | 344 | 206 | `\unsure{\mathrm{GP}(1)}` | main text / formula | `$\mathrm G\ell(2)_S$, $\mathrm S\ell(2)_S$, $\unsure{\mathrm{GP}(1)}_S$ \unsure{associées} à une $\overline{\math` |
| 42 | 344 | 206 | `\unsure{associées}` | main text / formula | `hrm S\ell(2)_S$, $\unsure{\mathrm{GP}(1)}_S$ \unsure{associées} à une $\overline{\mathrm m}$ Algèbre d'Azuma` |
| 43 | 344 | 206 | `\unsure{\mathbb P\|\mathcal P}` | main text / formula | `M$, i.e. à un fibré en droites projectives $\unsure{\mathbb P\|\mathcal P}$, sur $S$.` |
| 44 | 344 | 210 | `\unsure{\mathcal M}` | main text / formula | `Soit $\rho$ une section de $\unsure{\mathcal M}$ \inserted{(pas néc. inv.)}, posons` |
| 45 | 344 | 213 | `\unsure{v\|\nu}` | main text / formula | `(1) \unsure{v\|\nu}=\det\rho, w=\operatorname{Tr}\rho` |
| 46 | 344 | 216 | `\unsure{aura\|a}` | main text / formula | `de sorte qu'on \unsure{aura\|a} l'équation d'Hamilton-Cayley` |
| 47 | 344 | 219 | `\unsure{v\|\nu}` | main text / formula | `(2) \rho^2-w\rho+\unsure{v\|\nu}=0 \text{i.e.} \rho^2=w\rho-\unsure{` |
| 48 | 344 | 219 | `\unsure{v\|\nu}` | main text / formula | `e{v\|\nu}=0 \text{i.e.} \rho^2=w\rho-\unsure{v\|\nu}` |
| 49 | 344 | 226 | `\unsure{a')}` | main text / formula | `\unsure{a')} $\mathcal A_\rho=\underline{\mathcal O}_S+\u` |
| 50 | 344 | 226 | `\unsure{localmt\|localt}` | main text / formula | `erline{\mathcal O}_S\rho$ est un sous-module \unsure{localmt\|localt} facteur direct libre de rang $2$ de $\mathca` |
| 51 | 344 | 230 | `\unsure{e_0\|E_0}` | main text / formula | `O_S}(F)$) Il existe loc. (Zar) une section $\unsure{e_0\|E_0}$ de $F$ telle que $(e_0,\deleted{\unsure{\rh` |
| 52 | 344 | 230 | `\unsure{\rho.}` | deleted | `re{e_0\|E_0}$ de $F$ telle que $(e_0,\deleted{\unsure{\rho.}}e_1\mathrel{\overset{\mathrm{dfn}}{=}}\rho(e` |
| 53 | 344 | 238 | `\unsure{b'')}` | main text / formula | `\unsure{b'')} (Si $\mathcal M=\underline{\operatorname{End` |
| 54 | 344 | 238 | `\unsure{:}` | main text / formula | `F)$.) Le $\mathcal O_S[T]$-module $F_\rho$ ($\unsure{:}$ $T$ \unsure{est\|étant} une indéterminée, qu` |
| 55 | 344 | 238 | `\unsure{est\|étant}` | main text / formula | `al O_S[T]$-module $F_\rho$ ($\unsure{:}$ $T$ \unsure{est\|étant} une indéterminée, qui opère sur $F$ par $\rh` |
| 56 | 344 | 238 | `\unsure{isomorphe}` | deleted | `, qui opère sur $F$ par $\rho$) est \deleted{\unsure{isomorphe} à $\underline{\mathcal O}_S$} \inserted{\del` |
| 57 | 344 | 238 | `\unsure{loc$^{\mathrm t}$}` | inserted, deleted | `underline{\mathcal O}_S$} \inserted{\deleted{\unsure{loc$^{\mathrm t}$}} monogène} loc$^{\mathrm t}$ (Zar).` |
| 58 | 344 | 240 | `\unsure{est\|$\to$}` | main text / formula | `\underline{\mathcal O}_S[T]$-module $F_\rho$ \unsure{est\|$\to$} isomorphe à` |
| 59 | 344 | 243 | `\unsure{v\|\nu}` | main text / formula | `\underline{\mathcal O}_S[T]/(T^2-wT+\unsure{v\|\nu})` |
| 60 | 344 | 246 | `\unsure{loc$^{\mathrm t}$\|local$^{\mathrm t}$}` | main text / formula | `nderline{\operatorname{End}}(F)$)} $\exists$ \unsure{loc$^{\mathrm t}$\|local$^{\mathrm t}$} Zar une base $e_0,e_1$ de $F$, telle que la` |
| 61 | 344 | 246 | `\unsure{p.r.\|p.v.}` | main text / formula | `,e_1$ de $F$, telle que la matrice de $\rho$ \unsure{p.r.\|p.v.} à cette base` |
| 62 | 345 | 254 | `\unsure{v\|\nu}` | main text / formula | `(3) \rho_{e_0,e_1}=0&-\unsure{v\|\nu}\\1&w` |
| 63 | 345 | 257 | `\unsure{-v\rho e_0-w e_0}` | margin | `$\rho e_1=\unsure{-v\rho e_0-w e_0}$}` |
| 64 | 345 | 274 | `\unsure{corps}` | deleted | `0$ \deleted{dans}\inserted{sur} une \deleted{\unsure{corps}}\inserted{fibre} de façon à ne pas être vect` |
| 65 | 345 | 276 | `\unsure{car les}` | deleted | `ial ; \deleted{$c')\Longleftrightarrow c'')$ \unsure{car les}}\inserted{les bases pour lesquelles}` |
| 66 | 345 | 277 | `\unsure{st.}` | main text / formula | `orme $0&-v\\1&w$ \unsure{st.} précisément les bases de la forme $(e_0,e_1=` |
| 67 | 345 | 279 | `\unsure{d'ailleurs}` | deleted | `ions envisagées, ${}^t\rho$ aussi. (\deleted{\unsure{d'ailleurs}} et inversement il en résulte que la conditi` |
| 68 | 345 | 279 | `\unsure{$\}$}` | deleted | `'implique pour $\rho={}^t({}^t\rho)$\deleted{\unsure{$\}$}}, i.e. $c'')\longrightarrow c')$) --- mais c` |
| 69 | 345 | 282 | `\unsure{stable}` | inserted | `\deleted{Si $u$ commute}\inserted{Comme $b$ \unsure{stable}} par chgt de base, il suffit de voir que` |
| 70 | 346 | 291 | `\unsure{En}` | main text / formula | `\uline{NB} \unsure{En} fait, $G=\underline{\mathcal M}^{*}$ opère s` |
| 71 | 346 | 291 | `\unsure{\overline{\mathrm m}\|=}` | main text / formula | `G_m$, et $PG$ est quotient fppf de $SG$ (et $\unsure{\overline{\mathrm m}\|=}$ pour la top. (ét), si 2 inv.).` |
| 72 | 346 | 297 | `\unsure{OPs}` | main text / formula | `\unsure{OPs} $\alpha\in\Gamma\unsure{SG\|\mathrm{SL}(2)}$.` |
| 73 | 346 | 297 | `\unsure{SG\|\mathrm{SL}(2)}` | main text / formula | `\unsure{OPs} $\alpha\in\Gamma\unsure{SG\|\mathrm{SL}(2)}$.` |
| 74 | 346 | 299 | `\unsure{\varepsilon}` | deleted | `\deleted{\uline{Proposition} Soit $\unsure{\varepsilon}$}\inserted{\uline{Corollaire 2} Soient} $\rh` |
| 75 | 346 | 299 | `\unsure{\zeta\|\xi}` | main text / formula | `\inserted{\uline{Corollaire 2} Soient} $\rho,\unsure{\zeta\|\xi}$ deux sections de $G$, $\rho$ étant régulier` |
| 76 | 346 | 305 | `\unsure{\neq}` | deleted | `ta\rho$ est régulier, i.e. $\zeta$ \deleted{$\unsure{\neq}$} non-homothétique à $\rho^{-1}$ sur aucune` |
| 77 | 346 | 311 | `\unsure{Ce n'est\|Ce ne sont}` | main text / formula | `\unsure{Ce n'est\|Ce ne sont} que les conditions du cor. 1 \deleted{\unsur` |
| 78 | 346 | 311 | `\unsure{de}` | deleted | `sont} que les conditions du cor. 1 \deleted{\unsure{de}} de conjugaison de $\zeta\rho$ à $\rho$, la` |
| 79 | 346 | 314 | `\unsure{v\|\nu}` | inserted | `{i.e. $\boxed{\text{\textcircled{8}} c^2\unsure{v\|\nu}+wcd\deleted{\text{inv.}}+d^2 \text{inv.}` |
| 80 | 347 | 321 | `\unsure{OPs}` | main text / formula | `cela montre que la question est locale fppf. \unsure{OPs} donc $\mathcal M=\underline{\operatorname{En` |
| 81 | 347 | 321 | `\unsure{et}` | deleted | `i d'une base $(e_0,e_1=\rho(e_0))$. \deleted{\unsure{et}} On aura, si` |
| 82 | 347 | 332 | `\unsure{commute}` | main text / formula | `et si $u$ \unsure{commute} \deleted{$=ae_1+$} à $\rho$, on aura` |
| 83 | 347 | 342 | `\unsure{\neq\|=}` | main text / formula | `u(e_0)\unsure{\neq\|=}\unsure{u(e'_0)\|u'(e_0)}, u(e_1)=u'(e_1)` |
| 84 | 347 | 342 | `\unsure{u(e'_0)\|u'(e_0)}` | main text / formula | `u(e_0)\unsure{\neq\|=}\unsure{u(e'_0)\|u'(e_0)}, u(e_1)=u'(e_1) \text{donc }u=u',` |
| 85 | 347 | 346 | `\unsure{Itm\|Item}` | main text / formula | `ntes de la prop. est dite \uline{régulière}. \unsure{Itm\|Item} pour sections de $G$, $SG$, interprétées com` |
| 86 | 348 | 390 | `\unsure{Si}` | deleted | `d') \deleted{\unsure{Si}}$\exists$ Borel $SB\subset SG$, tel que $\va` |
| 87 | 348 | 392 | `\unsure{Dém}` | deleted | `\deleted{\unsure{Dém}} De plus, $D,B,SB$ sont bien déterminés par` |
| 88 | 348 | 394 | `\unsure{que}` | main text / formula | `\uline{Définition :} on \deleted{dit} \unsure{que} $\varepsilon$ est (strictement) unipotent ss` |
| 89 | 348 | 394 | `\unsure{ssi\|si}` | main text / formula | `$, que $N$ est \uline{strictement nilpotent} \unsure{ssi\|si} $\det N=\operatorname{tr}N=0$ (d'où $N^2=0$` |
| 90 | 349 | 416 | `\unsure{\varphi\|\psi}` | diagram | `loc. Zar)} isom $\mathcal M\xleftarrow[\sim]{\unsure{\varphi\|\psi}}\mathrm M_2(\underline{\mathcal O}_S)$, tran` |
| 91 | 349 | 420 | `\unsure{Corol}` | deleted | `\uline{Rmq} \deleted{\unsure{Corol}} Pour la démonstration, on notera que la con` |
| 92 | 349 | 426 | `\unsure{v\|\nu}` | main text / formula | `ho)=(\operatorname{Tr}\rho)^2-4\det\rho=w^2-4\unsure{v\|\nu}` |
| 93 | 349 | 431 | `\unsure{en}` | deleted | `deleted{\uline{Corollaire}} Les $P$ \deleted{\unsure{en}} satisfaisant les condit. de la proposition` |
| 94 | 349 | 431 | `\unsure{Dém.\|leur.}` | main text / formula | `projecteurs élémentaires} dans $\mathcal M$. \unsure{Dém.\|leur.}` |
| 95 | 350 | 438 | `\unsure{476}` | mspage | `\mspage{\unsure{476}}` |
| 96 | 350 | 440 | `\unsure{N}` | deleted | `associant à \deleted{$\unsure{N}$} $P$ le \deleted{\unsure{sous}} tore` |
| 97 | 350 | 440 | `\unsure{sous}` | deleted | `ant à \deleted{$\unsure{N}$} $P$ le \deleted{\unsure{sous}} tore` |
| 98 | 350 | 445 | `\unsure{\alpha}` | main text / formula | `formé des $\unsure{\alpha}$ qui stabilisent` |
| 99 | 350 | 446 | `\unsure{la droite}` | deleted | `\deleted{\unsure{la droite}} $D_0$` |
| 100 | 350 | 447 | `\unsure{induisent}` | deleted | `\deleted{et \unsure{induisent}}` |
| 101 | 350 | 448 | `\unsure{le couple des}` | deleted, inserted | `\deleted{\inserted{\unsure{le couple des}}}` |
| 102 | 350 | 450 | `\unsure{p.r.\|p.v.}` | inserted | `\inserted{donc \unsure{p.r.\|p.v.}}` |
| 103 | 350 | 452 | `\unsure{commutant}` | deleted | `\deleted{\unsure{commutant} à $N$.}` |
| 104 | 350 | 474 | `\unsure{aura}` | deleted | `\deleted{\unsure{aura}} est le stabilisateur de $D_1$.` |
| 105 | 350 | 478 | `\unsure{1}` | main text / formula | `uline{Remarque}. Le schéma des $\varepsilon_{\unsure{1}}$` |
| 106 | 350 | 479 | `\unsure{nilp.}` | inserted | `rted{unipotents réguliers, ou encore des $N$ \unsure{nilp.} \unsure{régul.}}` |
| 107 | 350 | 479 | `\unsure{régul.}` | inserted | `réguliers, ou encore des $N$ \unsure{nilp.} \unsure{régul.}}` |
| 108 | 350 | 482 | `\unsure{\overline{\mathrm m}\|=}` | main text / formula | `de $G$, de $SG$ ou de $PG$, cela revient au $\unsure{\overline{\mathrm m}\|=}$),` |
| 109 | 351 | 497 | `\unsure{\mathrm{GP}(1)}` | main text / formula | `resp. $\unsure{\mathrm{GP}(1)}_S\xrightarrow{\sim}PG$),` |
| 110 | 351 | 500 | `\unsure{\mathrm{gr}}` | main text / formula | `\underline{\mathrm{Aut}}_{S-\unsure{\mathrm{gr}}}\mathrm{G}\ell(2)_S` |
| 111 | 351 | 501 | `\unsure{\mathrm{gr}}` | main text / formula | `\simeq\underline{\mathrm{Aut}}_{S-\unsure{\mathrm{gr}}}\mathrm{S}\ell(2)_S` |
| 112 | 351 | 502 | `\unsure{\mathrm{gr}}` | main text / formula | `\simeq\underline{\mathrm{Aut}}_{S-\unsure{\mathrm{gr}}}` |
| 113 | 351 | 504 | `\unsure{N}` | deleted | `On dit que $\varepsilon$ et \deleted{$\unsure{N}$}$P$ sont` |
| 114 | 351 | 507 | `\unsure{\overline{\mathrm m}\|=}` | main text / formula | `s'ils définissent le $\unsure{\overline{\mathrm m}\|=}$ Borel,` |
| 115 | 351 | 509 | `\unsure{prov.}` | deleted | `\deleted{\unsure{prov.}}\inserted{proviennent} d'un épinglage.` |
| 116 | 351 | 519 | `\unsure{vraiment}` | margin | `\margin{C'est \unsure{vraiment} \unsure{joli} !}` |
| 117 | 351 | 519 | `\unsure{joli}` | margin | `\margin{C'est \unsure{vraiment} \unsure{joli} !}` |
| 118 | 351 | 522 | `\unsure{l'équi.}` | deleted | `\deleted{\unsure{l'équi.}}\inserted{la} conjugaison des sections` |
| 119 | 351 | 527 | `\unsure{Une}` | deleted | `\deleted{\unsure{Une}}` |
| 120 | 351 | 528 | `\unsure{une}` | deleted | `\deleted{\unsure{une}} la conjugaison` |
| 121 | 351 | 549 | `\unsure{\delta\|\Delta}` | deleted | `\deleted{\unsure{\delta\|\Delta}(\rho)=}` |
| 122 | 352 | 558 | `\unsure{qu'on}` | main text / formula | `on a fait ce qu'il fallait pour \unsure{qu'on}` |
| 123 | 352 | 559 | `\unsure{trouve}` | main text / formula | `\unsure{trouve} un $G\longrightarrow E^1$ qui passe au` |
| 124 | 352 | 569 | `\unsure{soit\|reste}` | main text / formula | `et qui \unsure{soit\|reste} invariant par autos int.` |
| 125 | 352 | 573 | `\unsure{équi}` | deleted | `\deleted{\unsure{équi}} conjuguées loc. fppf,` |
| 126 | 352 | 575 | `\unsure{et s.}` | deleted | `il f. \deleted{\unsure{et s.}}` |
| 127 | 352 | 593 | `\unsure{OPS}` | main text / formula | `Donc \unsure{OPS} (quitte à remplacer $\rho$ par $\lambda\rho$` |
| 128 | 353 | 637 | `\unsure{nbs\|nbres}` | main text / formula | `(\unsure{nbs\|nbres} duaux sur le module libre de rg $2$` |
| 129 | 353 | 658 | `\unsure{$\widetilde\varepsilon_1$, tous deux}` | deleted | `\deleted{\unsure{$\widetilde\varepsilon_1$, tous deux}}` |
| 130 | 353 | 660 | `\unsure{soit\|soient}` | main text / formula | `\unsure{soit\|soient} unipotent régulier —` |
| 131 | 353 | 679 | `\unsure{relèvement}` | margin | `\margin{pour un \unsure{relèvement} \unsure{plus}` |
| 132 | 353 | 679 | `\unsure{plus}` | margin | `\margin{pour un \unsure{relèvement} \unsure{plus}` |
| 133 | 353 | 680 | `\unsure{conv.\|commode}` | margin | `\unsure{conv.\|commode} de $\sigma$ et $\rho$}` |
| 134 | 353 | 682 | `\unsure{\lambda_0}` | margin, deleted | `$\varepsilon_0=-\deleted{\unsure{\lambda_0}}\sigma^{-1}\rho$,` |
| 135 | 353 | 683 | `\unsure{\lambda_0}` | margin, deleted | `$\varepsilon_1=-\deleted{\unsure{\lambda_0}}\rho\sigma^{-1}$}` |
| 136 | 354 | 701 | `\unsure{non-homothétiques\|non homothétiques}` | main text / formula | `\unsure{non-homothétiques\|non homothétiques}.` |
| 137 | 354 | 707 | `\unsure{scindage}` | deleted | `un \deleted{\unsure{scindage}}` |
| 138 | 354 | 719 | `\unsure{\rho}` | deleted | `\deleted{$\unsure{\rho}$}` |
| 139 | 354 | 733 | `\unsure{?}` | main text / formula | `=1&\unsure{?}\\0&1\\[1ex]` |
| 140 | 354 | 736 | `\unsure{w'\|u'}` | main text / formula | `-\dfrac{u}{\unsure{w'\|u'}}&0\\` |
| 141 | 354 | 737 | `\unsure{-\|+}` | main text / formula | `\dfrac{vw'\unsure{-\|+}wv'}{\unsure{w'\|u'}v'}&-\dfrac{v}{v'}` |
| 142 | 354 | 737 | `\unsure{w'\|u'}` | main text / formula | `\dfrac{vw'\unsure{-\|+}wv'}{\unsure{w'\|u'}v'}&-\dfrac{v}{v'}` |
| 143 | 354 | 740 | `\unsure{\mathrm{déf.}}` | inserted | `\overset{\inserted{\unsure{\mathrm{déf.}}}}{=}` |
| 144 | 354 | 741 | `\unsure{1}` | main text / formula | `1&0\\\unsure{1}&1` |
| 145 | 354 | 753 | `\unsure{+\|-}` | deleted | `\deleted{$(29) \dfrac{vw'\unsure{+\|-}wv}{uv}$}` |
| 146 | 354 | 764 | `\unsure{croisant}` | main text / formula | `en d'autres termes \unsure{croisant} $(26)(27)$` |
| 147 | 354 | 772 | `\unsure{coeff.}` | margin | `\deleted{et} du \unsure{coeff.} $u$ de $\rho$, et de $P$}` |
| 148 | 354 | 780 | `\unsure{0\|1}` | main text / formula | `N_0=0&u/v\\0&\unsure{0\|1}` |
| 149 | 355 | 789 | `\unsure{régulières}` | inserted, deleted | `rho,\sigma$ deux sections \inserted{\deleted{\unsure{régulières}}} de $G$,` |
| 150 | 355 | 791 | `\unsure{Posons}` | inserted | `\deleted{Conditions équivalentes} \inserted{\unsure{Posons}}` |
| 151 | 355 | 793 | `\unsure{\varepsilon}` | main text / formula | `\unsure{\varepsilon} \varepsilon_0=-\sigma^{-1}\rho,` |
| 152 | 355 | 802 | `\unsure{sont}` | deleted | `lon_0$ \deleted{et $\varepsilon_1$} \deleted{\unsure{sont}} \inserted{est} \unsure{unipotents\|unipotent` |
| 153 | 355 | 802 | `\unsure{unipotents\|unipotent}` | main text / formula | `n_1$} \deleted{\unsure{sont}} \inserted{est} \unsure{unipotents\|unipotent} \unsure{réguliers\|régulier} \deleted{\unsure` |
| 154 | 355 | 802 | `\unsure{réguliers\|régulier}` | main text / formula | `\inserted{est} \unsure{unipotents\|unipotent} \unsure{réguliers\|régulier} \deleted{\unsure{partout}} \inserted{$(\Left` |
| 155 | 355 | 802 | `\unsure{partout}` | deleted | `potent} \unsure{réguliers\|régulier} \deleted{\unsure{partout}} \inserted{$(\Leftrightarrow\varepsilon_1$}` |
| 156 | 355 | 802 | `\unsure{non équivalents, i.e.}` | deleted | `t $\varepsilon_1$ \deleted{partout} \deleted{\unsure{non équivalents, i.e.}} indépendants \inserted{en chaque fibre}, --` |
| 157 | 355 | 811 | `\unsure{(32)}` | deleted | `\deleted{\unsure{(32)}}&\\[-1.2em]` |
| 158 | 355 | 821 | `\unsure{(33)}` | deleted | `\deleted{$\unsure{(33)}$} \deleted{$\unsure{(34)}$}` |
| 159 | 355 | 821 | `\unsure{(34)}` | deleted | `\deleted{$\unsure{(33)}$} \deleted{$\unsure{(34)}$}` |
| 160 | 356 | 852 | `\unsure{1}` | deleted | `1}(\varepsilon_0)&=1&\deleted{\unsure{1}}\unsure{?}\\0&1` |
| 161 | 356 | 852 | `\unsure{?}` | main text / formula | `lon_0)&=1&\deleted{\unsure{1}}\unsure{?}\\0&1` |
| 162 | 356 | 874 | `\unsure{w}` | margin | `ce qui décrit $u,\unsure{w},\unsure{v}$ en termes de $\rho$, donc aussi` |
| 163 | 356 | 874 | `\unsure{v}` | margin | `ce qui décrit $u,\unsure{w},\unsure{v}$ en termes de $\rho$, donc aussi $u',v',w'\l` |
| 164 | 356 | 876 | `\unsure{(37)}` | deleted | `\deleted{$\unsure{(37)}$}` |
| 165 | 356 | 880 | `\unsure{(38)}` | main text / formula | `\unsure{(38)} \varphi^{-1}(\varepsilon_0)=\begin{pmat` |
| 166 | 356 | 887 | `\unsure{vu\|vue}` | main text / formula | `facile. L'équivalence $a)\Leftrightarrow b)$ \unsure{vu\|vue} dans prop. p. $449'$. Pour $b)\Leftrightarro` |
| 167 | 356 | 890 | `\unsure{\det}` | main text / formula | `\unsure{\det}(\sigma+\rho)` |
| 168 | 356 | 901 | `\unsure{on aura}` | main text / formula | `commune à $b)$ et $c)$, \unsure{on aura}` |
| 169 | 356 | 903 | `\unsure{*\|6}` | main text / formula | `(\unsure{*\|6}) \det(\sigma+\rho)=\det\sigma\,(2+\oper` |
| 170 | 356 | 905 | `\unsure{mb\|membre}` | main text / formula | `donc le premier \unsure{mb\|membre} est nul ssi $\operatorname{Tr}\sigma^{-1}\rh` |
| 171 | 357 | 919 | `\unsure{c'est en\|c'est un}` | deleted | `vec $e)$, $f)$ est aussi immédiate, \deleted{\unsure{c'est en\|c'est un}} et ne fait que résumer certains calculs pré` |
| 172 | 357 | 921 | `\unsure{N_0}` | margin, deleted | `sont combin. lin. indépendantes de \deleted{$\unsure{N_0}$} $N_0,N_1,P$` |
| 173 | 357 | 928 | `\unsure{évidemment\|évidente}` | margin | `$\rho,\sigma$ forment une base \unsure{évidemment\|évidente} du \unsure{sous-Module\|sous-module} de $M$ e` |
| 174 | 357 | 928 | `\unsure{sous-Module\|sous-module}` | margin | `ent une base \unsure{évidemment\|évidente} du \unsure{sous-Module\|sous-module} de $M$ engendré par $(N_0+N_1)$ et $P$, donc` |
| 175 | 357 | 932 | `\unsure{remplacer}` | margin | `ma$ par $P$; i.e. dans $N_0,N_1,P,1$ on peut \unsure{remplacer} $N_0$, ou $N_1$ par $\rho$ ou $\sigma$.}` |
| 176 | 357 | 938 | `\unsure{1}` | main text / formula | `partons de $\widetilde\rho,\widetilde\sigma_{\unsure{1}}$, que nous voulons décrire --- l'épinglage` |
| 177 | 357 | 938 | `\unsure{est}` | main text / formula | `}$, que nous voulons décrire --- l'épinglage \unsure{est} en fait défini déjà en termes de $\widetilde` |
| 178 | 357 | 942 | `\unsure{simplifier\|normaliser}` | main text / formula | `e{facteur}} scalaire $\lambda_0$ --- on peut \unsure{simplifier\|normaliser} plus en multipliant $\rho,\sigma$ par le fac` |
| 179 | 358 | 967 | `\unsure{notera}` | deleted | `\deleted{On \unsure{notera} que $\varepsilon_1$ est \unsure{entièrement` |
| 180 | 358 | 967 | `\unsure{entièrement déterminé}` | deleted | `d{On \unsure{notera} que $\varepsilon_1$ est \unsure{entièrement déterminé}}` |
| 181 | 358 | 969 | `\unsure{par}` | deleted | `\deleted{\unsure{par}} par les conditions $\varepsilon_1=-\rho\sig` |
| 182 | 358 | 978 | `\unsure{stri.}` | diagram, deleted | `{c}\text{unipotents }\deleted{\unsure{stri.}}\\\text{réguliers de}\\G` |
| 183 | 358 | 983 | `\unsure{fppf}` | deleted | `(au moins localement \deleted{\unsure{fppf}} \inserted{\unsure{fppf}} \deleted{\unsure{Z` |
| 184 | 358 | 983 | `\unsure{fppf}` | inserted | `localement \deleted{\unsure{fppf}} \inserted{\unsure{fppf}} \deleted{\unsure{Zar.}})` |
| 185 | 358 | 983 | `\unsure{Zar.}` | deleted | `ure{fppf}} \inserted{\unsure{fppf}} \deleted{\unsure{Zar.}})` |
| 186 | 358 | 989 | `\unsure{rég}` | margin | `n dira qu'une section de $PG$ est unipotente \unsure{rég} si elle est loc. fppf l'image d'une section` |

## Source reference

Grothendieck, A. (1981). *La Longue Marche à travers la théorie de Galois* (cote 140-3, archive file described as pages 293–650; supplied scans 340–358) [Unpublished manuscript]. Université de Montpellier. Source identification supplied in the task; archive address printed on the scans: <https://grothendieck.umontpellier.fr>.

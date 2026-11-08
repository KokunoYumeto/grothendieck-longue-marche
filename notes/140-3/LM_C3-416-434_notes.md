# LM_C3-416-434: transcription notes

## Scope and source identification

This package transcribes all 19 supplied images, from `LM_C3-416-434_scan416.jpg` through `LM_C3-416-434_scan434.jpg`, in filename order. The French transcription is diplomatic: authorial corrections, inconsistent notation, abbreviated words, and uncertain readings remain in place. It is not a critical reconstruction of an intended final text.

Three numbering systems must be distinguished. `\scanpage` follows the supplied filenames; `\mspage` records the original upper folio where visible; the handwritten number at the lower left is retained separately in the transcription. The typeset Montpellier footer outside the black manuscript frame is archival metadata, not manuscript writing, and is not included as manuscript text.

| Scan filename number | Lower-left archival number | Original upper folio | Inventory elements |
|---|---|---|---|
| 416 | 415 | Not visible | 23 |
| 417 | 416 | 510 | 20 |
| 418 | 417 | Not visible | 14 |
| 419 | 418 | 511 | 19 |
| 420 | 419 | Not visible | 22 |
| 421 | 420 | 512 | 19 |
| 422 | 421 | Not visible | 24 |
| 423 | 422 | 513 | 24 |
| 424 | 423 | Not visible | 17 |
| 425 | 424 | 514 | 17 |
| 426 | 425 | Not visible | 18 |
| 427 | 426 | 515 | 17 |
| 428 | 427 | Not visible | 16 |
| 429 | 428 | 516 | 23 |
| 430 | 429 | Not visible | 16 |
| 431 | 430 | 517 | 28 |
| 432 | 431 | Not visible | 15 |
| 433 | 432 | 518 | 33 |
| 434 | 433 | 519 (preceded by an uncertain cancelled mark) | 28 |

The inventory has **393 rows**. `transcribed = yes` means that the element is represented in the LaTeX, including explicit uncertainty or deletion where necessary; it does not certify every letter as certain. Nested additions and deletions have their own rows where they form distinct elements.

### Editorial and typesetting conventions

- The requested state macros distinguish surviving text, cancellations, insertions, marginal material, and doubt. The first reading inside `\unsure{reading|alternative}` is the preferred visual reading, not a mathematical emendation.
- Cursive manuscript glyphs are represented by `\mathcal M`, `\mathcal T`, and `\mathcal R`; the straight `T_\rho` and `T_\sigma` remain distinct. The repeated elaborated `G_m` glyph is represented consistently as `\mathbb G_m`. Translating pen forms into a named font is less secure than identifying most letters; the general doubts below record that limitation.
- Page 416's long rotated addition is placed with (30), before (31), following its callout. Other marginal blocks retain their relative textual attachment; their physical locations are recorded in the inventory. The drawings reproduce the visible callout and bracket shapes in TikZ.
- Rotated equivalence and inclusion signs are retained as signs. They are not replaced by inferred morphisms. Headless, hooked, dashed, and dotted connections in diagrams retain their observed distinctions.
- Source numbering is retained, including both occurrences of (96), on scans 432 and 433. The final comma after “un autre, scindage,” on scan 434 is retained without inventing a continuation.
- The fragment deliberately has no preamble or macro definitions. It was successfully compiled in a separate validation wrapper with the requested macros, AMS mathematics, `graphicx`, TikZ, and `tikz-cd`; that wrapper and its proof PDF are not deliverables. `ampersand replacement=\&` and grouped arrow labels make the diagrams usable inside the requested `\diagram` macro. These are syntax choices, not additions to the manuscript.

## Table of doubts

Confidence describes the visual reading, not the truth of the mathematical statement. A high-confidence row may document a conspicuous feature retained despite contextual pressure to change it. Closely repeated occurrences are grouped in one row where they share the same issue.

| Scan | Approximate line or location | Reading | Alternatives or source of doubt | Confidence |
|---|---|---|---|---|
| 416–434 | Recurring elaborated multiplicative-group glyph | `\mathbb G_m` | Plain `G_m`; the ink has an extra inner stroke or loop, with no supported page-dependent change of alphabet. | medium |
| 416–434 | Recurring constructed-group initials | `\mathcal M`, `\mathcal R` | Ordinary handwritten `M`, `R`; the calligraphic mapping is typographic rather than a claim that a modern font is uniquely determined. | medium |
| 416–434 | Curled group initial versus straight torus initials | `\mathcal T_{\rho,\sigma}`, distinct from `T_\rho`, `T_\sigma` | The curled initial is consistently distinct; this alphabet distinction is stronger than the `M`/`R` distinction. | high |
| 416 | Upper-left slanting marginal note beside (24) | `aura` | `a` with a following stroke; `a un` | medium |
| 416 | (24), vertical identification; (26) and (31), subsidiary vertical marks | `\simeq` or containment, rotated to follow the page | The small handwritten equivalence sign is not typographically determinate | medium |
| 416 | Left rotated paragraph, (30) | `\varepsilon_0` | cursive `e_0` | medium |
| 417 | Text above (33) | `can.` | `can` without a visible final point | medium |
| 417 | NB, immediately after (36) | `\mathcal M_{ρ,σ}[0)` | `\mathcal M_{ρ,σ}(0)`; the left delimiter is angular and the right one rounded | low |
| 417 | Final parenthesis, initial `M` before `ρ,σ(0)` | overwritten/cancelled `M`, then `M` | A single heavily corrected glyph; cancellation and replacement are not separately legible | low |
| 418 | After the first displayed inclusion | `est` | possibly an overstruck `est`; the extra stroke may be the letter formation | medium |
| 418 | Cross-reference after `l'écriture` | `(19)` | `(49)` | low |
| 418 | Cancelled number beside normalizer assertion | `(39)` | the digits are crossed over | medium |
| 418 | Normalizer assertion | `=` | `\simeq` | medium |
| 418 | Deleted words after `Par construction` | `on a ⊂, pour ⊃` | The last relation is particularly obscured | low |
| 418 | Following `du tout` | `bien` | overwritten beginning; `bien` is the best letter-based reading | medium |
| 418 | First profinite group in final paragraph | `\widetilde{\mathcal G}_{0,3}^{\widehat{+}}` | `\widetilde{\mathcal G}_{0,\widehat3}^{+}` | low |
| 418 | Generator in final paragraph | `\varepsilon_0` | cursive `e_0` | medium |
| 418 | Last parenthesis | `moyennant` | The medial letters are reduced to strokes | medium |
| 418 | Last word | `fait` | `faite` | low |
| 419 | Slanting upper-left marginal note | `calculs de pts entiers` | the abbreviated middle word may be `pt` with a flourish | medium |
| 419 | Opening list, third group | `\mathcal M(0)^\circ` | the left delimiter resembles `[`, giving `[0)` | low |
| 419 | Opening list, third group, initial glyph | cancelled `M` plus replacement `M` | one superposed corrected initial | low |
| 419 | Three vertical annotations in (43) | a cup-shaped inclusion mark | downward arrow with a reduced head | low |
| 420 | Formula (46), right after closing parenthesis | Deleted `\simeq` | Small overwritten mark; its exact original sign is obscured. | low |
| 420 | Upper left margin, first line | Toute la fin du n° | Toute la fin du [section sign]; first and last strokes indistinct. | low |
| 420 | Upper left margin, third line | après (ou avant) le n° 6° | Parenthetical word and article are compressed; `avant` is a tentative ink reading. | low |
| 420 | Upper left margin, last line | à propos des « radicalités » | Beginning is partly crowded into the margin; quoted word is not wholly resolved. | low |
| 420 | Left margin beside (49) and (52) | id. | Could be an abbreviated repetition mark; both are retained. | low |
| 420 | Paragraph after (53) | caractérisations | Central abbreviated strokes and ending are faint. | medium |
| 420 | Last line | centr. | centre; a small dark mark may be an abbreviation point. | medium |
| 421 | First line, deletion after sigma | en tant | Striking-out is concentrated on the second word; its extent is uncertain. | low |
| 421 | Text before (55), deleted word | quatre | Overwritten by the inserted `trois`; original descender is visible. | medium |
| 421 | Deleted line before (55) | i_B | Possible prime on i; the subscript is overwritten. | low |
| 421 | Formula (55), source of i_sigma | SN'_sigma | N and its index/prime are overwritten; ST'_sigma is less likely. | low |
| 421 | Two lines after (55) | contient contient | The word occurs at the end of the first line and again at the beginning of the next; the repetition is preserved. | medium |
| 421 | Addition below (56), group at start | script B_rho,sigma | script T_rho,sigma; this is retained as an explicit alternative. | low |
| 421 | Right edge of added action character | {1,tau_infinity} | Opening delimiter resembles a parenthesis; final characters run into the black border. | low |
| 422 | Deleted left-hand part of (59), lower sign | script R | SG; heavy zigzag deletion obscures the middle strokes. | low |
| 422 | Formula (60), cancelled words at right | on a | qu'on; one or two words are compressed under the deletion stroke. | low |
| 423 | First line, replaced word | invariant | The replacement `distingué` is clear; strokes of the discarded word are crossed. | medium |
| 423 | Repeated quotient superscript, (63)–(67) and prose | natural sign | sharp sign; the manuscript repeatedly uses an angular lightning-like glyph, with its shape clearer than its typographical identity. | medium |
| 423 | Immediately after (65) | dont | The initial descending stroke is doubled or overwritten. | medium |
| 423 | Reference preceding (66) | 64 | 69; the last digit has a closed-looking upper curve. | medium |
| 424 | paragraph before (68) | `intouché` | `intact` | medium |
| 424 | top unnumbered diagram, arrow tail | simple right arrow with `épi` above | retraced or overwritten tail mark | medium |
| 424 | cancelled paragraph after (68) | `n'est autre que` | `n'est ... que` | medium |
| 424 | cancelled paragraph, last group | superscript circle before `(0)`, another after `(0)` | first small mark may be a correction rather than a circle | low |
| 424 | diagonal left margin beside (69) | `Il y aurait intérêt à commencer tt de suite avec l'introduction` | middle words/abbreviation faint | medium |
| 424 | same margin | `reconstitution / réalisation (102)` | connected middle letters unclear | low |
| 424 | same margin, end | `en termes de sommes amalg. des prod...` | several connected words remain insecure | low |
| 425 | Top, (71), first condition | `μ ∈ Γ G_m` | The parameter is heavily retraced; an earlier λ may lie under it. | medium |
| 425 | Top right, (71), after `det b` | Deleted `=λ²` | The old value is overwritten almost completely; `=μ²` is also possible. No old value is secure. | low |
| 425 | Above (72), left | Added `j_G` | The small added function label may be a different subscript or a reworked `j`; its attachment is not explicit. | low |
| 425 | (72), first argument of `j` | `μ` | λ may survive underneath the heavier strokes. | medium |
| 425 | (72), upper right matrix entry | `1` | `0` cannot be ruled out at this resolution, but the visible stroke is upright. The entry is not changed to make the formula a torus homomorphism. | low |
| 425 | (72), after membership sign | `Γ S G` | The `S` is visible but conflicts with the determinant of the displayed matrix. It is retained, with doubt, rather than removed. | medium |
| 425 | (72), after `j_{T_0}` | Deleted `(μ)` | The crossed argument may contain a different parameter. | low |
| 425 | (72), target of `j_G` | Deleted `S` before `G` | The heavy stroke may be an overwritten letter rather than a distinct cancellation. | low |
| 425 | (73), verbal line | `revêtement algébrique` | The initial letters of the adjective are congested; `algébrique` is the best reading, but is not secure. | medium |
| 426 | First line, quotient superscript | `♮` or `♯` | The mark is a small lightning-shaped glyph. Both printed approximations remain tentative. | low |
| 426 | Crossed tuple above `engendré par` | Closing `)` | The cancellation makes the closing parenthesis difficult to distinguish from the final stroke of `b`. | low |
| 426 | Middle, product expressing a section | `λ j_{T_0}(μ⁻²)` | The scalar resembles λ, while the subscript resembles `T_0`; earlier formulas use different symbols. Those earlier formulas were not used to repair this line. | medium |
| 426 | Before first `int j_G` display | Detached `i.` | This may be an abandoned start of a word or an isolated pen mark. It remains represented in place. | low |
| 426 | Second `int j_G` display | Exponent `−2` | The final numeral has only a short hooked stroke; `−1` is a possible visual alternative. | medium |
| 426 | Above final display | Deleted `Notons en` | The second word is heavily crossed and could instead be `que`. | low |
| 426 | Final display number | `(76)` | The last numeral resembles an open 6, but is close to the author's 5 in this scan. | medium |
| 427 | Between (77) and (78) | `amalgamée` | The middle syllables and final accent are faint. | medium |
| 427 | Abandoned display above (78) | Deleted `M°_{ρ,σ}` | Most of the group letter and the superscript are crossed through; the indices are clearer. | low |
| 427 | Second factor in (78) | Deleted `M`, replaced by `G̃` | The two group letters overlap; the cancellation/replacement segmentation is tentative. | medium |
| 427 | Above (79), overwritten prose | Deleted `bien con.`, inserted `description` | The replaced wording is not secure; only the inserted `description` is clear. | low |
| 428 | Large cancellation, beginning | `est gr.` | The abbreviated beginning is tangled with cancellation strokes; `est` is clearer than `gr.`. | low |
| 428 | Large cancellation, after `engendré par` | `points interposés` / `produits interposés` | The two-word reading is highly tentative. Its initial and medial tall strokes are visible, but the crossing lines obscure several letters. | low |
| 428 | Small deletion before large cancellation | `et T° ≃` | The final sign may instead be an unfinished equality or word beginning. | low |
| 428 | Insertion above `scindage de l'extension` | Quoted `de travers` | Independent rereading supports the initial `t` and the longer cursive run. The remaining letters are faint, so the reading is still marked uncertain. | medium |
| 429 | Upper paragraph, final word at right | `factorise` | The ending approaches the page edge and is faint. | medium |
| 429 | Remark, `de façon …` | `analogue` | Read from the a/n/l/g-like strokes; the central letters are faint. | medium |
| 429 | First scalar factor in the preimage | `G_m` | The `G` is heavily retraced; no deleted alternative is asserted. | medium |
| 429 | Four added superscripts on the new `R` | `∞` / `∼` | A dark ω/∞-like added mark. Its intended notation is unresolved; the same uncertainty is retained at every occurrence. | low |
| 429 | Margin, crossed old sequence label | Deleted `(86)` | The old number is nearly obliterated; this is only an estimated reading. | low |
| 429 | Margin, replacement sequence label | `(87)` / `(81)` | The final digit lacks a clear upper bar. The visible reading is not resolved using the later numbering. | low |
| 430 | Lower paragraph before (84) | parlante | Very fluent ending; could be `parlante` with the final letters run together | medium |
| 430 | (84), under the inclusion sign beneath the first factor | `1` before `\mathcal M^\circ(0)` | Isolated upright stroke may be a residual stroke rather than a numeral | low |
| 430 | (84), crossed-out annotation under `\mu_2` | `G_m` | Dense cancellation; a mark above the G is not securely separable | low |
| 431 | Cancelled first heading | Le sous-groupe | The word before `groupe` is substantially obscured by the cancellation | medium |
| 431 | Cancelled first heading, group argument | `\tfrac12` | Possible additional stroke/letter after the fraction; the cancellation prevents a secure reading | low |
| 431 | Slanted left marginal heading, first line | Groupes mixtes | The first line is very cursive; only the following `du radical` and the group list are secure | low |
| 431 | Before (89) | Dailleurs | An apostrophe after the D is not securely visible | medium |
| 431 | Annotation below `S\mathcal R` in (90) | cancelled `\kappa` | `\Theta`; densely overwritten symbol between `Ker` and the opening parenthesis | low |
| 431 | Bottom triangle following (93) | cancelled `G_m` at bottom right | The final ink is overwritten and very close to the page border | low |
| 432 | (94), below the lower `PG` arrow | `1` | Small dark isolated stroke may be a residual mark | low |
| 432 | Left marginal NB, second line | se réduit à voir | The connecting words are highly compressed | medium |
| 432 | Left marginal NB, after `est épi` | `(?)` | The sign inside the parentheses is not secure | low |
| 432 | Left marginal NB, final words | est triviale | Highly compressed ligatures | medium |
| 432 | Text before (95) | poliment | `joliment` is a possible reading of the initial letter | medium |
| 432 | (95), lower middle vertex | `S\mathcal R_{\rho,\sigma}` | Ink resembles `SR`, with no securely visible circle; a mathematical expectation of `\mathcal R^\circ` has not been substituted | low |
| 432 | (95), upper direct horizontal edge | cancelled `G` | Overwritten mark adjacent to the surviving `G` label | low |
| 433 | (96), upper left diagonal | cancelled `\mu_2`, surviving `\simeq` | Both label and source-end stroke are heavily overwritten; a residual stroke resembles an additional arrowhead | low |
| 433 | (96), left of upper front vertex | cancelled `S` before `\mathcal T^+` | Dense isolated overwritten glyph | low |
| 433 | (96), lower left diagonal | hooked tail; cancelled `\mu_2`, surviving `\sim` | `\simeq`; the surviving mark resembles a rotated tilde. A residual 2-shaped stroke and blackened label remain; their layering is not secure | low |
| 433 | (96), bottom dotted edge T^circ–G_m | headless dotted edge | No terminal arrowhead is visible in the enlargement; none is added from context | high |
| 433 | Parenthesis after `soit à 1` | cancelled `marqués par` | Multiple crossing strokes obscure the two words | low |
| 433 | Insertion over the preceding parenthesis | cancelled `autrefois`, then `on en fait` | The layering and the first cancelled word are insecure | low |
| 433 | Same parenthesis, after `flèches` | cancelled `d'inclusion` | `d'isomorphisme`; the overdrawn arrow crosses the word | low |
| 433 | Before (97), long struck line | qui implique les relations | Number/ending of the verb and initial connective are not secure | low |
| 433 | (97), first row, two heavily cancelled groups | `S\mathcal R^\circ\cap SG` | Repeated group fragments overlap with cancellation; exact superscripts least secure | low |
| 433 | (97), first row, far right cancelled glyph | `\mu_2` | Blackened terminal glyph | low |
| 433 | (97), second row, cancelled ending | `\ne\mu_2 (centre SG)` | Sign and first word of the parenthesis uncertain | low |
| 433 | Cancelled bottom paragraph, first line | il suffit de voir que les | il faut voir que les | low |
| 433 | Cancelled bottom paragraph, third line | évidemment | Ending partially obscured by a diagonal cancellation | medium |
| 433 | Cancelled bottom display, underbrace label | `\operatorname{Ker}\Theta` | Close to the lower frame, partly crossed out | low |
| 434 | Original folio, top centre | deleted uncertain `8`, then `519` | The three final digits are readable; a dark overwritten curl precedes them. It could be a cancelled digit other than 8. It is retained separately rather than silently discarded. | low |
| 434 | First displayed R in opening line | `R_{rho,sigma}^{circ}` | A dark circle-like superscript is visible. The annotation beneath this same R reads `Ker tildeTheta` without a circle. The superscript is not silently removed to reconcile the two. | medium |
| 434 | Below the first two R's | `Ker tildeTheta`, `Ker Theta^circ` | The short curved strokes are reproduced as underbraces. A tilde on the second Theta is not distinctly visible, unlike in the adjacent main formula; tilde presence is marked uncertain. | high |
| 434 | After “résulte” | deleted `de` | A very short word is struck through. Its visible strokes are compatible with “de”; it is not needed to make the surviving sentence grammatical. | medium |
| 434 | Following “Le fait que”, lower half | deleted `S R_rho` | The cancelled mathematical false start is only partly formed. R and a rho-shaped subscript are clear; initial S is overwritten, and no separate sigma can be read securely. | low |
| 434 | Annotation beneath M^+ | `Ker` | `Ker'`; a short slanted stroke near the end of “Ker” is not securely assignable. The vertical equality marker and “dfn” are separate and preserved. | low |
| 434 | M^+(0) in final displayed product | M^+(0) | The M has been heavily retraced, without an unambiguous cancellation; no discarded alternative letter is supplied. | high |
| 434 | End of page | “un autre, scindage,” | The page ends on the comma. No continuation has been invented. | high |

## Abbreviations met

Expansions below are tentative explanations confined to the notes. They are never substituted for the written forms in the transcription. Repetitions across ranges retain local punctuation and usage.

### Scans 416–419

| As written | Tentative expansion, only in these notes |
|---|---|
| can. | canonique |
| mono | monomorphisme |
| i.e. | id est |
| gr | groupes / de groupes, as subscript to `Aut` |
| Aut | automorphismes |
| Ker | noyau (kernel) |
| det | déterminant |
| NB. | nota bene |
| hom | homomorphisme |
| cf | confer / compare |
| $\frac12$ direct | semi-direct (the fractional shorthand is retained in the transcription) |
| isom. | isomorphe |
| ss-groupe | sous-groupe |
| tjrs | toujours |
| p.ex | par exemple |
| pts | points (uncertain abbreviated reading in margin) |
| dfn | définition (above an equality sign) |

### Abbreviations met — scans 420–424

| As written | Tentative expansion (here only) |
|---|---|
| dfn | définition |
| Ker | noyau (kernel) |
| Centr | centre |
| centr. | centre |
| n° | numéro |
| cf | confer / voir |
| id. | idem, if the marginal reading is correct |
| i.e. | id est / c'est-à-dire |
| inv. | inversible |
| hom | homomorphisme |
| mono | monomorphisme |
| car. | caractéristique |
| autom. | automorphisme |
| cart. | cartésien / cartésienne |
| Rad | radical |

Additional marginal forms on scan 424: `tt` — probably *tout*; `amalg.` — probably *amalgamées*. Both readings remain marked uncertain in the diplomatic transcription.

### Abbreviations met: scans 425–429

Explanations occur only here, not as expansions in the transcription.

| As written | Probable meaning | Location / qualification |
|---|---|---|
| `NB.` / underlined `NB` | Nota bene | Scan 425, annotation under (71); scan 429, margin. |
| `det` | Déterminant | Scan 425. |
| `incl` | Inclusion | Scan 425, (73). |
| `can.` / `can` | Canonique | Scan 425, arrows; scans 427–429. |
| `hom.` / `hom` | Homomorphisme | Scans 425, 427, 429. |
| `cart` | Cartésien | Scan 425, centre of (74). |
| `épi` | Épimorphisme | Scan 426; scan 429, factorization. |
| `i.e.` | Id est | Scan 426. |
| `int` | Automorphisme intérieur / conjugaison intérieure | Scan 426, the two opposing conjugation formulas. |
| `cqfd` | Ce qu'il fallait démontrer | Scan 426. |
| `cf` | Confer / se reporter à | Scan 426, (76). |
| Underlined `Rmq` | Remarque | Scan 427. |
| `morph. can.` | Morphisme canonique | Scan 427. |
| `\overline{\mathrm m}` | Même | Scan 427 (`de m̄`); scan 428 (`lui-m̄`, `utiliser m̄`); scan 429, deleted paragraph. |
| `dfn` | Définition | Scan 428, above the defining equality. |
| `ss-groupe` | Sous-groupe | Scan 428. |
| `gr.` | Groupe | Scan 428, deleted text; the abbreviation itself is uncertain. |
| `mono` | Monomorphisme | Scan 429, factorization. |
| `etc` | Et cetera | Scan 429, final paragraph. |

### Scan 430 — abbreviations met

- `mb.`: membre.
- `hom`: homomorphismes (no terminal stop is securely visible here).
- `Centr`: centre.

### Scan 431 — abbreviations met

- `dfn`: définition.
- `comp. neutre`: composante neutre.
- `Centr`: centre.
- `hom`: homomorphisme.
- `p-`: par (the dash-like abbreviation is retained).
- `i.e.`: id est.

### Scan 432 — abbreviations met

- `NB`: nota bene.
- `cart`, `cocart`: cartésien, cocartésien.
- `épi`: épimorphisme.
- `déf`: définition.
- `p.ex.`: par exemple.

### Scan 433 — abbreviations met

- `post`: postérieure (cancelled incomplete/abbreviated word).
- `iso`: isomorphismes.
- `isom.`: isomorphes.

### Abbreviations and graphical conventions

- `can.`: canonique; retained in “morphisme can.” and “inclusion can.”
- `iso`: isomorphismes; retained and underlined in the transcription.
- `dfn`: définition; retained beside the vertical equality in the lower annotation.
- `cf`: confer; the cross-reference to (44).
- “produit ½ direct”: produit semi-direct; kept with the written fraction in the transcription.
- The order of the superscripts `+circ` in (98) and in its quotient is preserved.
- Plain 433 at the lower left is the handwritten archival page number. The printed institutional footer outside the frame is not manuscript text.

## Legibility and limits

The main uncancelled prose and most formulas are readable after enlargement, but the manuscript remains a working draft with faint strokes, tightly compressed abbreviations, superposed corrections, and several dense cancellations. All 19 pages were reread against the transcription, with enlarged inspection of difficult passages and independent checks of selected readings and the large diagrams. Such checking reduces error; it cannot turn ambiguous ink into a certain reading.

The least secure passages are the revised normalizer discussion and profinite indices on scan 418; the diagonal notes on scans 420 and 424; the overwritten parameters and matrix on scan 425; the large cancelled block and quoted insertion on scan 428; the added superscript on the new `R` on scan 429; and the layers of cancellation before and within (97) on scan 433. Their uncertainty remains visible in the LaTeX and is itemized above. The mark before folio 519 and the unfinished cancelled mathematical start on the final page also remain uncertain.

Context has not been used to repair literal surprises: the reversed-looking determinant ratios, the mixed delimiter after (36), the repeated `contient`, uncertain or apparently inconsistent superscripts, the matrix and target in (72), the source's “Hamilton–Cayley”, and the repeated equation number (96) are retained. No published transcription was consulted. A better image or examination of the original could resolve some marked readings; the package makes no claim of a zero-error transcription.

## Research notes — English, separate from the transcription

These are source-based working observations and proposed checks, not additions to the manuscript. The four kinds are **conjecture**, **unproved claim**, **unpursued implication**, and **own idea**. “Unproved claim” may mean asserted without a full proof at the cited location; subsequent uptake in this supplied packet is identified where apparent. Authorial expectations and retracted assertions are distinguished in the prose. Own ideas state confidence and its reason, and are not presented as established or new. No external literature search or priority assessment has been undertaken.

1. **Scan 416, (24), unproved claim.** The words “donne un mono” accompany the inclusion in `T_ρ × N′_σ` and the condition `(det a/det b)² = 1`. A verification would need the preceding definitions of `\mathcal T_{ρ,σ}` and the morphisms being projected, together with the relevant meaning of monomorphism over the base; the displayed condition is transcribed without supplying that verification.

2. **Scan 416, (27)–(28), unproved claim.** “une suite exacte canonique” introduces the determinant sequence with kernel `ST_ρ × ST_σ`. Checking exactness requires the precise topology or category in which the quotient is meant and the surjectivity of the determinant maps; surjectivity on all rings of points should not be inferred just from the written sequence.

3. **Scan 416, marginal (30) and (31), unpursued implication.** The action on `L_0` is written as `g(ε_0(λ)) = ε_0(μλ)`, with `μ = χ(g)`, while the action on `SG` factors through `T_0 → PG`. These formulas suggest a compatibility condition needed for the subsequent semidirect construction; that compatibility is explicitly asserted in scan 417, (38), and reformulated at the opening of scan 418.

4. **Scan 417, (37)–(38), unproved claim.** “On définit un plongement canonique” and “ce qui est bien compatible avec les opérations” assert that the inclusion of the common subgroup and the map `i(λ)=j(λ)` on `L_0` extend to an embedding. A proof would check the action relation for the semidirect product used to define `\mathcal M[0]` and then compute the kernel; the faint delimiter in the preceding NB must be checked independently of that proof.

5. **Scan 418, revised normalizer paragraph, conjecture.** This is a rejected assertion undergoing authorial revision: the heading “Proposition” is cancelled and replaced by “Remarque”; the displayed normalizer equality remains, but the following text says the required self-normalizing property “n'est pas vrai du tout”. It must not be silently repaired into a theorem; establishing its final intended status requires following subsequent manuscript discussion.

6. **Scan 418, final paragraph, conjecture.** The analogous profinite statement is an expectation pending verification, followed by “moyennant vérification !” and “que je n'ai tjrs pas fait” (the final inflection is uncertain). A proof would require exact identification of the profinite groups and generators, followed by a normalizer calculation for the indicated closed cyclic subgroups; both the handwritten indexing and the mathematical verification remain open here.

7. **Scan 418, normalizer paragraph, own idea. Confidence: medium.** Test the rejected assertion in a split matrix model by computing the conjugation of the subgroup corresponding to `L_0` by upper triangular matrices, then compare the resulting normalizer with the proposed product `\mathcal M(0)·L_0`. The reason for this test is the manuscript's explicit warning about self-normalization in `SG`; the precise identification of `L_0` must be recovered before the example can settle anything about the manuscript's groups.

8. **Scan 419, (39)–(41), unproved claim.** The connected-component notation is introduced with “composantes neutres”, and (39) identifies the quotient by the neutral component with `μ₂ × μ₂`. A proof needs the base scheme and connectedness or smoothness hypotheses for the groups involved; behavior at residue characteristic two cannot be read off solely from a diagram of these group schemes.

9. **Scan 419, (45), unproved claim.** The norm-one product is asserted to be “central” in `\mathcal M^\circ`, followed immediately by “pas dans \mathcal M”. The semidirect action should be computed on both factors to show why the neutral component acts trivially while components outside it need not do so; the continuation begins on scan 420 and gives the component action explicitly in scans 423–424, especially (68).

10. **Scan 420, margin beside (47); kind: unproved claim.** The annotation says, “cette inclusion n'est pas une égalité, cf plus bas”. The explicit subgroup in (47) therefore must not be substituted for the entire centre; a proof of strictness would need an additional central element or a structural computation of that centre. The centre is subsequently computed in scans 425–427, beginning with (75).

11. **Scan 420, formulas (48)–(52); kind: unproved claim.** The text says the displayed finite subgroup “est en fait contenu dans le Centre de … tout entier”. Verification must check conjugation by components outside the neutral component, since centrality within the latter alone is insufficient.

12. **Scan 420, formula (53) and following sentence; kind: unpursued implication.** The “cas modulaire” is characterized by the displayed determinant and matrix conditions, with an explicit reference to “VI” for other characterizations. The relationship between these concrete order relations and the central embeddings merits tracking into the following page, rather than treating the several conditions as proved equivalent here.

13. **Scan 421, paragraph after (55); kind: unproved claim.** “Pour 2 inv. sur S, l'hom (53) est un mono (mais pas en car. 2, bien sûr)” states injectivity with an explicit characteristic-two failure. The parenthetical reference is transcribed as written; establishing the assertion requires distinguishing the relevant group schemes and their sections and then computing the kernel after reduction in characteristic two.

14. **Scan 421, formula (56) and action annotation; kind: unproved claim.** The displayed description of integral points as a semidirect product is accompanied by an action through a character of the dihedral factor and conjugation by the displayed diagonal matrix. A proof would require computing the integral points of both tori and the normalizer and checking that the proposed section realizes exactly that action.

15. **Scan 421, formula (56); kind: own idea.** One could test the stated semidirect-product presentation by explicit integer matrices and compare its reductions modulo 2 and modulo odd primes. **Confidence: medium**, because the matrices and character are concrete enough for a direct computation, while the overwritten normalizer notation must first be settled from the manuscript context; this is a proposed verification, not a claimed new result.

16. **Scan 422, formulas (57)–(58); kind: unproved claim.** “On définit un hom.” gives the map by its restrictions to the displayed factors, including the identity on the subgroup identified with SG. To justify that these assignments extend to a homomorphism, one must check their compatibility with the action defining the semidirect product.

17. **Scan 422, formulas (59)–(62); kind: unproved claim.** “on trouve” introduces the exact sequence of kernels and identifies the neutral kernel with the product of two determinant-one subgroups. A complete proof should establish both the kernel calculation and surjectivity of the two sign characters in the category and topology intended for these group schemes.

18. **Scan 422, discarded identifications below (61); kind: own idea.** The cancelled identifications with `Rad` and the neutral centre could be checked against the later calculation of the full centre, rather than reinstated on structural grounds. **Confidence: high** that this is a useful verification step, because the cancellation is unambiguous; no mathematical equality is asserted here on the basis of the deleted text.

19. **Scan 423, formulas (64)–(66); kind: unproved claim.** The restriction of the quotient map to G is said to be “l'identité”, followed by “donc on trouve” the direct-product decomposition. A detailed group-scheme argument should construct the complementary kernel of that retraction and verify that it commutes with the embedded G and maps isomorphically onto the two-sign quotient.

20. **Scan 423, final paragraph; kind: unpursued implication.** “donc G y opère trivialement” reduces the remaining conjugation action on the two determinant-one factors to the finite quotient. Scan 424, (68), identifies the second sign as acting, fixes the first factor, and gives the action on the second generator. A remaining question is how that description behaves over bases where the sign group schemes are not étale.

21. **Scan 423, text before (65) and final clause; kind: own idea.** A formal consistency check should compare the literal `R` in “étant trivial sur …” and the centre assertion without circle superscripts with the kernel and neutral-component formulas immediately above. **Confidence: high** that these need editorial tracking, because the visible notation differs; no correction or counterclaim is inferred from that discrepancy alone.

22. **Scan 424, paragraph and formula (68); kind: unproved claim.** The quotient action is said to operate “via son deuxième facteur”, to leave the first determinant-one factor untouched, and to send the second generator to its sign multiple. Verification requires checking this on the full group functor, including the source's stated compatibility with the quadratic relation, rather than only on geometric points.

23. **Scan 424, definition (69), sequence (70), and final formula; kind: unpursued implication.** Defining the displayed subgroup as the inverse image of the scalar subgroup gives an extension by the neutral kernel, followed by the formula `f = λ u⁻¹` and `λ² = det u`. This square-root condition is formulated as the Cartesian square on scan 425, (74), and developed into the central amalgamated-product description on scan 427, (77)–(79). Its behavior on sections over different base rings remains a useful comparison problem.

24. **Scan 424, diagonal margin beside (69); kind: conjecture.** The partly uncertain editorial expectation begins “Il y aurait intérêt” and refers ahead to “(102)” and “6°”. This signals that the proposed placement or presentation of the subgroup is deferred; the unclear connecting words are not evidence for a specific additional theorem.

25. **Scan 424, final formula; kind: own idea.** The scalar parameter could be retained explicitly when comparing rational points over different base rings, so that failure to choose a square root is distinguished from failure of the associated sheaf morphism to be an epimorphism. **Confidence: medium**, because the displayed relation makes the obstruction concrete, but the precise ambient topology and definitions must be recovered from the preceding manuscript context.

26. **Scan 425, (73)–(74) — unproved claim.** The sentence “on a un diagramme cartésien” asserts that the map from `R°` to `T_ρ ×_{G_m} T_σ` is obtained from the squaring map on `G_m`. A full verification would compare the functors of sections of the two corners using (71), with particular care over the overwritten parameters and the determinant condition. The adjective transcribed as “algébrique” in (73) remains uncertain, so no stronger covering property is inferred from that word.

27. **Scan 425, (74) — own idea.** Compare this pullback under squaring over bases where 2 is invertible and where it is not, and determine precisely which topology makes the displayed epimorphisms exact. **Confidence: medium**, because the square supplies a concrete construction to examine, but these pages do not state the relevant base assumptions at this point. This is a proposed check, not a claim that the manuscript's “revêtement” is everywhere étale.

28. **Scan 426, proof following (75) — own idea.** Formalize the cancellation between `int j_G(μ²)` and `int j_G(μ⁻²)` as a statement about the action on `SG` without choosing pointwise square roots. **Confidence: medium**, because the two opposing inner automorphisms are explicitly written, while the formula for the section itself contains unresolved scalar and subscript readings. The argument should be checked sheafwise before using it to justify a central-product description over an arbitrary base.

29. **Scan 427, (77)–(79) — unpursued implication.** The phrase “somme amalgamée centrale” and (78) suggest comparing the central product defined by `R°` and `SG` with the analogous presentation of `G` in (79). One can ask which isomorphisms of the central extension (77) induce isomorphisms of the resulting groups, and what information about the two embeddings of `μ₂` must be retained. The page constructs the homomorphism between the two presentations but does not pursue such a comparison problem here.

30. **Scan 428, middle paragraph — unpursued implication.** The author emphasizes reconstruction “sans avoir à utiliser m̄ des plongements” of `T_ρ` and `T_σ` in `G`, and even less the sections `ρ, σ`. This separates the group reconstructed from the abstract groups, their characters, and the form `G` from the additional data selecting a splitting. Comparing different embeddings with the same character data would clarify exactly where the lost choice re-enters.

31. **Scan 428, final paragraph — conjecture.** The chosen splitting “jouera un rôle essentiel.” This is an explicit statement of expected use, not a theorem left unproved: the next scan already composes that section with the map to `G` and identifies its image as `T_0`. Further checking should track how that choice, as opposed to the intrinsic central-product construction, is used later in the manuscript.

32. **Scan 429, remark and final paragraph — conjecture.** “On peut songer à construire” the full group by introducing the scalar preimage, but the author then says, “Je ne vais pas expliciter ici la construction,” being unsure it will be needed. This deferred construction is substantially resumed in scans 431–434 through the projective kernel, its quotient characters, and the isomorphisms (98). A full reconstruction would still require explicit multiplication and component actions in terms of the stated data, while the temporary superscript on the new `R` remains textually unresolved.

33. **Scan 429, diagonal margin — unproved claim.** The marginal note calls `R` “le noyau de l'hom composé” `M → G → PG` and writes a corresponding exact sequence. One should verify equality of this kernel with the scalar-preimage definition in the main text and check the asserted surjectivity onto `PG` over the intended base. The rewritten sequence number is uncertain, independently of the mathematical content.

34. **Scan 429, scalar preimage and identity component — own idea.** Investigate how the disconnected components act on the connected centre identified earlier as `R°`; the full scalar preimage need not be assessed solely from the centrality statement inside `M°`. **Confidence: medium**, because the manuscript distinguishes the full group from its identity component and considers, but cancels, a renaming; these five pages do not compute that component action. This is an investigation to undertake, not an assertion that any particular centre formula here is false.

35. **Scan 430, (81)–(82); unproved claim.** The words “on aura” introduce the descriptions of the integral points and the use of (74) to obtain the extra factor `\{\pm1\}`. A proof should verify the two integral-point identities `T_\rho(\mathbb Z)=ST_\rho(\mathbb Z)` and `T_\sigma(\mathbb Z)=ST_\sigma(\mathbb Z)` from the preceding definitions, and then check that the pullback description really gives the stated integral points.

36. **Scan 430, (84)–(85); unpursued implication.** The “inclusion canonique” is asserted to induce “un isomorphisme” on integral points. This makes the distinction between the underlying group morphism and its evaluation on one base ring worth checking over other rings, without reading the integral-point isomorphism as a group-scheme isomorphism.

37. **Scan 430, (84)–(85); own idea. Confidence: medium.** Test the same map on rings with units whose squares differ from 1, and on nonreduced rings in characteristic 2. These tests may isolate why its integral-point behaviour is unusually simple; the suggestion is motivated by the `\mu_2` factor and the square map in the cited (74), and is not an assertion of a new result.

38. **Scan 431, (88); unproved claim.** “On aura” identifies the intersection `\mathcal R\cap\mathcal M^\circ` with the “comp. neutre” of `\mathcal R`. This identification needs a connectedness argument for that kernel/preimage; an intersection with an ambient identity component does not by itself establish that it is the subgroup’s identity component.

39. **Scan 431, (89)–(90); unproved claim.** “D'ailleurs on a aussi” identifies the projective kernel with `\Theta^{-1}(G_m)` and then gives an exact sequence ending in `G_m`. To verify it one needs the kernel of `G\to PG`, the restriction defining `\kappa`, and the appropriate sense of surjectivity over the base.

40. **Scan 431, (92)–(93); unpursued implication.** The equality “`\chi(g)=\kappa(g)^2`” links the two scalar characters. Its scheme-theoretic kernel involves the square map on `G_m`; checking it over bases where 2 is not invertible is a natural continuation, without replacing it by a statement only about geometric points.

41. **Scan 432, left marginal NB; unproved claim.** Grothendieck explicitly notes “une vérification à faire,” reducing it to whether `S\mathcal R_{\rho,\sigma}\to\mu_2\times\mu_2` “est épi,” and concludes that “la vérification est triviale” (last words not completely secure). A proof should construct or locally lift the required pairs of characters, retaining the relevant scheme/sheaf sense of epimorphism rather than merely checking a few rational points.

42. **Scan 432, (94)–(95); unproved claim.** The three lateral squares are said to be “à la fois cartésiens et cocartésiens.” Each assertion should be checked in the category being used: the pullback statements concern preimages/intersections, while the pushout statements require the claimed quotient identifications.

43. **Scan 432, (96); unpursued implication.** The displayed exact sequence specifies the three quotient characters simultaneously, with kernel `ST_\rho\times ST_\sigma`. This gives a concrete test for which conclusions depend only on the norm-one factors and which also depend on the two component characters.

44. **Scan 432, (95)–(96); own idea. Confidence: medium.** Reconstruct the asserted exact sequence by an explicit fibre-product calculation from `\kappa`, `\varepsilon_3`, and `\varepsilon_2`, and compare it with the prism’s lateral squares. This would test the commutative-diagram argument while avoiding reliance on the uncertain lower middle label; the note is a proposed verification, not a correction of that label.

45. **Scan 433, opening sentence; unpursued implication.** The description “en termes des groupes très simples” stresses the reduction to the two `ST` factors, `G_m`, and `\mu_2`. The resulting presentation suggests comparing different pairs `(\rho,\sigma)` with isomorphic norm-one factors and character data, while keeping track of any embedding information still used in the construction.

46. **Scan 433, (96) and following paragraph; unproved claim.** The two opposite vertical faces of the cube are said to be “cartésiennes et cocartésiennes,” and the four horizontal projections have kernels isomorphic either to `\mu_2` or to 1. Verifying these assertions requires checking all four intersections with `SG`, not reading their values solely from the labels in the heavily revised diagram.

47. **Scan 433, (97); unproved claim.** The surviving relation gives `\mathcal R\cap SG=\mathcal R^\circ\cap SG=\mu_2`, whereas `S\mathcal R\cap SG=S\mathcal R^\circ\cap SG=\{1\}`. The proof attempted beneath it is cancelled; scan 434 supplies the replacement kernel argument. The cancellations must not be treated as surviving mathematical claims.

48. **Scan 433, dashed right-hand square of (96); own idea. Confidence: medium.** Check the compatibility of the two square maps `\lambda\mapsto\lambda^2` with the integral-point calculation on scan 430 and with base change in characteristic 2. This may clarify the role of the central `\mu_2` without identifying it prematurely with a constant two-element group; the note is a proposed consistency check, not a claim of novelty.

49. **Scan 434, opening unnumbered displays — unpursued implication.** The manuscript compares restrictions of `tildeTheta` to SG and calls their common kernel “bien μ₂”. It then uses the inclusion SG ⊂ G to give `SR ∩ SG = {1}` and consequently the corresponding assertion for SR°. The visible circle-like superscript on the first R remains a textual uncertainty, rather than being resolved from these claims.

50. **Scan 434, (98) — own idea. Confidence: medium.** Check the exactness and comparison hypotheses in the proof outline introduced by “Le fait que l'on a des isomorphismes”: the second isomorphism follows by comparing (62) and (28), and the first uses “le lemme des cinq” on the displayed μ₂ × μ₂ quotients. This is a proposed formal verification because the relevant category and topology must be recovered from earlier definitions; the page already supplies the proof strategy and is not being classified as lacking an argument.

51. **Scan 434, final paragraph — unpursued implication.** In the semidirect-product presentation cited as (44), the manuscript contrasts the splitting induced by M(0) with “un autre, scindage,”. The new splitting is only announced on this page; its definition is not included in the supplied final line.

52. **Scan 434, final paragraph — own idea. Confidence: medium.** The trivial intersection with SG and the isomorphism SR → T^+ suggest that the announced second splitting is intended to use the subgroup SR. This inference is motivated by the immediate order of the argument, but the final sentence does not yet state the map and must not be completed in the transcription.


## Source reference

Grothendieck, A. (1981). *La Longue Marche à travers la théorie de Galois* (Cote 140-3; supplied scan files 416–434 from the archive file described as pages 293–650) [Handwritten manuscript]. Université de Montpellier.

The title, date, and cote are supplied by the accompanying task brief; the repository attribution also appears in the image footers. References within these notes use scan filename numbers, not the offset archival numbers. This citation identifies the supplied primary source and does not imply verification against a separate edition.

# LM_P054 — Transcription apparatus and research notes

## 1. Source, pagination, and editorial conventions

This apparatus accompanies `LM_P054_transcription.tex`, a diplomatic transcription of the ten supplied images of Alexander Grothendieck's *La Longue Marche à travers la théorie de Galois*. The attribution, date (1981), and archival identification (Montpellier, cote 140-2) follow the supplied task brief. Readings were made from the supplied scans; no published transcription was used. The external literature listed in section 6 is used only for the separate research comparisons, not to determine or repair manuscript readings.

The scan numbers follow the filenames and the requested sequence. The printed archive footer is one number lower; it is not substituted for the requested `\scanpage` number. Only the visible authorial page numbers are encoded as `\mspage`.

| Scan / filename number | Printed archive footer | Visible authorial page number |
|---|---|---|
| 531 | 530 | 271 |
| 532 | 531 | — |
| 533 | 532 | 272 |
| 534 | 533 | — |
| 535 | 534 | 273 |
| 536 | 535 | — |
| 537 | 536 | 274 |
| 538 | 537 | — |
| 539 | 538 | 275 |
| 540 | 539 | — |

The LaTeX file is a fragment without a preamble or macro definitions. It uses the requested editorial macros and standard mathematical LaTeX, with `tikz-cd` for the readable core of diagram (8). A bracketed description within `\diagram` records the placement of its small, less secure annotations. Marginal material remains in `\margin`; cancelled and interlinear readings are distinguished with `\deleted` and `\inserted`. Paragraph order and page boundaries are retained, while ordinary handwritten line breaks are not mechanically reproduced. Accents, abbreviations, punctuation, unbalanced authorial parentheses, and changes of notation have not been regularized.

In the table below, approximate lines refer to physical handwritten lines, counting displayed formula rows when needed and excluding the authorial header and printed footer. “M” identifies the diagonal margin on scan 533. More specific regional descriptions take precedence over an approximate line count. Confidence concerns the reading of the marks, not the mathematical truth of the passage. Where no alternative is offered, the uncertainty remains; the absence of an alternative does not make the retained reading certain. Counts in `\illegible{n}` estimate words or, in formulas, short symbolic items.

## 2. Table of doubts

| Scan | Approximate line / region | Reading retained | Alternatives / difficulty | Confidence |
|---|---|---|---|---|
| 531 | 1, first connector | A horizontal dash | `\longrightarrow`; no distinct arrowhead is recoverable. | low |
| 531 | 1 (twice), 12 | `\mathcal T` | Greek `\tau`; the manuscript's highly cursive letter cannot confidently be assigned a typeface. Hats and the `+`/prime marks are separately visible. | medium |
| 531 | 3, end | `cqfd.` | Compressed abbreviation with long terminal stroke; no fully supported alternative. | medium |
| 531 | 6 | `baptisé` | Central letters are compressed. | medium |
| 531 | 11 | `bien` | Initial letter is overwritten. | medium |
| 531 | 12, before target group | Deleted illegible item (1) | A cancelled mathematical symbol, not a recoverable word. | low |
| 531 | 14, source group | `\widehat{\Pi}_{0,3}` | First subscript is partly joined to the descending main stroke. | medium |
| 531 | 15 | `reste` | Short strokes could support another verbal form; none securely read. | medium |
| 531 | 16 | `commutant` | Last letters are reduced to a long joined stroke. | medium |
| 531 | 17 | `proposait` | Ending is compressed. | medium |
| 532 | 1 | `essayant` | Initial and final strokes are compressed. | medium |
| 532 | 1, cancellation | Deleted `prouver` | Strike-through obscures the middle and ending. | low |
| 532 | 1, interlineation | Inserted `trouver` | Reading of the replacement is provisional; its exact relation to the cancelled word is crowded. | low |
| 532 | 1, 3, 5, group letter | `\mathcal T` | Greek `\tau`; same paleographical uncertainty as on scan 531. | medium |
| 532 | 2 | `dans` | `de`; several connected strokes follow the initial d. | low |
| 532 | 3, first arrow label, lower line | `surj` | The visible label is very compressed; it must not be silently changed to an expected property of this map. | low |
| 532 | 4 | `fourvoyé` | Interior letters and ending are abbreviated by the pen. | medium |
| 532 | 5, sign before source group | `\varphi` | `\rho`; a narrow looped vertical character, without a securely visible colon. | low |
| 533 | 5 | `remords`, after `D'abord un` | Independently read this way in two image inspections; the unusual wording has not been replaced by the contextually tempting `rappel`, whose p-descenders are unsupported. | medium |
| 533 | 7 | `Soient` | `Soit`; ending is overwritten, followed by a small cancelled or corrective mark. | low |
| 533 | 7, after `Soient` | Deleted illegible item (1) | Small slashed loop, perhaps a cancelled symbol rather than a word. | low |
| 533 | 7, after `topologique` | Superscript `*` | Small star/callout-like mark; attachment uncertain. | low |
| 533 | 14 | `locale` | End of word is compressed. | medium |
| 533 | 16, end | `ens` | Abbreviation's final stroke indistinct; no expansion inserted in the transcription. | medium |
| 533 | 19 | `\subset` | `\in`; inclusion/membership sign is overwritten. | low |
| 533 | 21, right edge | `ramification` | Final letters compressed near the edge. | medium |
| 533 | 24 | `espace` | Middle and ending weakly differentiated. | medium |
| 533 | M1–M10, repeatedly | `\mathcal G`, `\mathcal H` | `\mathfrak G`, `\mathfrak H`; ornamental capitals do not determine the intended typographic alphabet securely. Ordinary `G` is kept separate. | low |
| 533 | M2 | Deleted `X`, two illegible items, ornamental `G` | Dense crossing-out prevents recovery of the intervening words; estimate is approximate. | low |
| 533 | M3, before `X` | Deleted illegible item (1), inserted `sur` | Two writing layers overlap. | low |
| 533 | M3, after `X` | `avec` | `son`; the short connective is compressed. | low |
| 533 | M4 | Underlined `invariant` | Some internal strokes are merged. | medium |
| 533 | M5 | `satisfaisant` | End of line overlaps adjacent writing. | low |
| 533 | M7, before `Y=X/G` | Deleted illegible item (1) | Overwritten or cancelled mark. | low |
| 533 | M7 | `prenant` | `posant`; the interior strokes are not individually distinct. | medium |
| 533 | M7–M8, between the quotient formulas | `avec` | Small interlinear connective, close to the body text. | low |
| 533 | M8 | `dessus` | `les isos`; very compressed running script. | low |
| 533 | M9, before `Rev` | Deleted illegible item (1) | Dark overwritten mark. | low |
| 533 | M9–M10, equivalence sign | `\simeq` | `\cong`; number and shape of the short horizontal strokes are uncertain. | low |
| 533 | M11, first fundamental-group basepoint | `x` | Written over a preceding or retraced stroke. | low |
| 533 | M13, first group | `\mathcal G_{0,3}` | `\mathfrak G_{0,3}`; ornamental letter, also faintly separated from its subscript. | low |
| 533 | M13–M14, T-like letters | `\mathcal T` | Greek `\tau`. | medium |
| 533 | M13, linear group | `Gl` | `Sl`; first letter heavily retraced. | low |
| 533 | M13, after the linear-group parenthesis | Illegible item (1) | A short cluster of additional strokes is interleaved with the adjoining body text. Its content and exact attachment cannot be securely established. | low |
| 533 | M14, symmetric-group letter | `\mathfrak S_3` | `\mathcal S_3`; ornate capital. | medium |
| 534 | 1, `rev. ... de Y` | `ramifié` | Final ending is faint; `ramifiée` is not securely supported. | medium |
| 534 | 1–2 | `subordonné` | Word crosses a line break; the final ending is abbreviated to a stroke. | medium |
| 534 | 2, signature | `\underline d\,\illegible{1}=\underline d(X/Y)` | One dark ξ/brace-like, possibly cancelled symbol follows the first underlined d; its identity and cancellation status cannot be established. | low |
| 534 | 8, `rev. ... Y'` | `ramifié` | Final accent/ending compressed. | medium |
| 534 | 8, after `Y` | `compatible` | Initial letters are overwritten; no independent earlier reading recovered. | medium |
| 534 | 9, before `(X,G)-revêtement` | `\deleted{\illegible{2}}` | Two cancelled words; the first may be `le`, but the strike and overwritten loops obscure it. The replacement `le` is beneath them. | low |
| 534 | 13 | `réguliers` | Initial and terminal letters are run together. | medium |
| 534 | 18 | `transitivement` | Middle/terminal strokes are compressed. | medium |
| 534 | 21, equation (2) | `a` / `x` | Left basepoint is a looped a-like letter, unlike the x in the opening condition; do not regularize solely from the mathematics. | low |
| 535 | 3, equation (3), first nontrivial term | `\deleted{\Pi_1((X,G),x)}\inserted{\Pi_1(X,x)}` | The original inner `(X,G)` is circled and overwritten; G is uncertain and may have been altered to 1. A line from the left margin supplies `\Pi_1(X,x)`, interpreted as the replacement; cancellation applies to a circled correction rather than an ordinary horizontal strike. | low |
| 535 | 4, NB, between `On a` and `un` | `?` | Isolated hook resembling a question mark, with no separate lower dot securely visible; it could be a stray/corrective stroke. | low |
| 535 | 7, after `dim 1` and before dash | `.` | A very small pale dot is present, but it may be image noise rather than a full stop. | low |
| 535 | 11, NB end | `l'énoncé` / `les énoncés` | The article and singular/plural ending are compressed and partly overwritten. | medium |
| 535 | 12, NB end | `raisonnable` | Final n/a/b/l strokes run together. | medium |
| 535 | 14, symmetric group | `\mathfrak S_3` / `\mathcal S_3` | The ornate capital is reproduced as a Gothic S; a script S remains possible. Subsequent occurrences on these pages carry the same explicit alphabet uncertainty. | medium |
| 535 | 15, cancelled word after `avec les` | `notations` | Strong horizontal deletion obscures the middle letters. | medium |
| 535 | 15, insertion above cancelled word | `conventions` | Small interlinear writing; initial letters are uncertain. | medium |
| 535 | 16, cancelled formula | `Y=\illegible{1}\,\mathbb P^1(\mathbb C)` | The centre is heavily overwritten. The first symbol resembles Y and the final `\mathbb P^1(\mathbb C)` is much clearer; no missing quotient or equality has been supplied. | low |
| 535 | Bottom, equation (5) | right basepoint `y` | At the right border, y and the nested closing parentheses overlap. Parentheses are transcribed as the visible double nesting, but the exact comma placement is insecure. | medium |
| 536 | 1, first word | `ou` / `or` | No accent is securely visible above the short opening word. It might represent `où`, but that accent has not been silently supplied. | low |
| 536 | 3 | `sera` | The middle letters are reduced to connected short strokes. | medium |
| 536 | 4, directly after `y=f(x)` | `\in` / `\leftarrow` | Dark two-bar, left-pointing sign; it might also be a crossed correction, but its cancellation status cannot be determined. It has not been silently omitted. | low |
| 536 | 10, insertion above `point-base` | `orbital` | Initial letters are overwritten; the ending is fairly clear. | medium |
| 536 | 10, before `=U_{0,3}(C)` | `X_0` / `X` | A heavy overwritten X-like letter with a loop at its lower right; whether the loop is a zero or part of the correction is uncertain. | low |
| 536 | 11, after `premier` | `mb` | Final b-like loop is highly compressed; probable abbreviation for membre. | medium |
| 536 | 12, after `(5bis)` | `\deleted{\illegible{1}}` | One vertically looped cancelled word or symbol, possibly `et`; no reading retained. | low |
| 537 | Lines 1, 5; diagram twice; paragraph after diagram, line 2 | `\mathfrak{S}_3` | Large ornate S-like symbol; the choice of Fraktur rather than another script alphabet is uncertain. All five occurrences carry `\unsure`. | medium |
| 537 | Line 3 | `arithméticogéométrique` | The adjective appears to run together; an indistinct hyphen or an accent in the first component cannot be excluded. | medium |
| 537 | Line 4 | `travaillant` | Final strokes are compressed; `travaillons` is less likely. | medium |
| 537 | Line 4 | `schém.` | Possibly the full word `schéma` with a small final stroke; a distinct dot follows the visible word. | medium |
| 537 | Line 6, signature | `3` in `2\{1\}+3\{\infty\}` | The digit is overwritten and dark; an underlying 2 may be present, but the layers cannot be separated confidently. | medium |
| 537 | Diagram, middle row, first two nontrivial groups; side-note reference | `\mathcal{E}_{0,3}`, `\mathcal{E}'_{0,3}` | Tall epsilon-shaped script capital; the alphabet is not certain. Both nodes and the side-note reference carry `\unsure`. | medium |
| 537 | Diagram, annotation left and below `\widehat{\Pi}_{0,3}` | `\widehat{\mathcal{T}}^{+}_{0,4}` | The script T/tau-like letter is uncertain; hat, plus, and indices are visible. Its adjoining pair of diagonal strokes is described without imposing an equality sign. | low |
| 537 | Diagram, annotation left and below `\mathcal{E}_{0,3}` | `N^{!}_{0,4}` | Initial N-like letter and elevated exclamation-like sign are uncertain. The adjoining pair of diagonal strokes is described rather than interpreted. | low |
| 537 | Paragraph after diagram, line 5 | `ci-dessus` | Only `ci-d…` is distinct; the end is compressed, and `ci-devant` cannot be excluded. | low |
| 537 | Paragraph after diagram, line 5 | `sous-entendu` | `sous-entendus`; last stroke may be a final s. | medium |
| 537 | Last line | `tj.` | Possibly `tjs.`; the crossed t and the following descender are dark and crowded. | low |
| 538 | Line 2 | `oiseusement` | The two s-like forms are visible, but the medial and final run of strokes is compressed; no secure alternative is offered. | medium |
| 538 | Line 2, after each of the two moduli expressions | `,` (twice) | Both marks are dark, cross-like, and could be asterisks or cancellations rather than ordinary commas. The marks have not been suppressed. | low |
| 538 | Line 3, cancelled phrase | `devrait être` | `devait être`; the r is not securely distinguishable under the deletion. | low |
| 538 | Line 3, after cancelled `devrait être` | `\illegible{1}` | About one additional cancelled word or short group lies beneath the insertion and strike; it cannot be read securely. | low |
| 538 | Line 13 | `sous-schém.` | Possibly full `sous-schéma`; the compressed end looks abbreviated and is followed by a dot. | medium |
| 538 | Line 15, after `où` | `u` | The variable is a single shallow stroke; n is not entirely excluded by the shape. | medium |
| 538 | Line 15 | `au` | Dense small word after the emphasized `identité` and below the added `id_E`; it may contain an overwritten or cancelled form. | low |
| 538 | Line 15, added `id_E` | `\inserted{id_E}` after `l'identité` | The symbol itself is clear. Its curved linking stroke is interpreted as an insertion connector; an opening parenthesis cannot be excluded. | medium |
| 538 | Line 19, first occurrence with round brackets | `M_{1,1}(n)` | `M_{1,1}(2n)`; the left of the dark n-like letter is overwritten, and may contain a separate numeral. The later occurrence on line 20 is a plain `(n)`. | low |
| 538 | Penultimate line, after `Spec Z` | `sera` | `ser.`; the short compressed word ends in a dark point. An initial reading `est` was rejected on closer inspection, but the retained reading remains uncertain. | low |
| 538 | Last line, cancelled word | `schém.` | `schéma`; much of the word is crossed out and covered by the added `topos modulaire`. | low |
| 539 | 1, after “se” | `récupère` | The last part is highly compressed; no second complete reading is secure. | medium |
| 539 | 2, (9), relation after the first M | `\simeq` | `\cong`; the thick overtraced strokes make the number of lower bars uncertain. | low |
| 539 | 4, end | `représente` | The final syllable is a rapid continuous stroke. | medium |
| 539 | 5, subscript to `(Sch)` | `\mathbb Z` | `S`, or another overtraced subscript; it is small and unusually dense. | low |
| 539 | left margin beside lines 6–9 | `est` | The two strokes could be a right-pointing reference arrow rather than a word. The alternative `\to` is retained inside the doubt mark. | low |
| 539 | 16, after the inserted base | `peut` | Overwritten lower strokes; no other whole-word reading is secure. | medium |
| 539 | 19, “classes d'…” | `isom.` | `Isom.`; the initial stroke is unusually tall. | medium |
| 539 | 21, after the dash | `idem` | A more contracted abbreviation such as `idᵐ` cannot be excluded; the medial letters are not separable. | medium |
| 539 | 21, before Q | `(p.ex` | `p.ex`: the initial open curve may be a parenthesis or part of the p. No closing parenthesis can be confidently identified in the remaining line. | low |
| 540 | 3, “fibre …” | `gén` | `gén.`; no separate terminal point can be confidently distinguished. | medium |
| 540 | 4 | `relativement` | Final letter sequence compressed into a stroke; a contracted spelling is possible. | medium |
| 540 | 5, before “effet” | `En` | Overtraced first letter; no earlier separate word can be recovered. | medium |
| 540 | 9, superscript after 2 | `ième` | `ème`; the short initial stroke and dot favour ième but remain small. | medium |
| 540 | 13, opening parenthesis | `prenant` | Several medial letters are reduced to short marks. | medium |
| 540 | 14, cancelled material before “l'image” | `\deleted{\illegible{1}}` | Approximately one cancelled word; no reliable reading. | low |
| 540 | 14, between 1 and n | `mod` | Compressed three-stroke word; `est` is graphically conceivable but less convincing. | medium |
| 540 | 17, after “primitives” | `nièmes` | `n-ièmes`; no independent joining hyphen is securely distinguishable. | medium |
| 540 | insertion at line 21, doubly underlined | `en car.0` | Initial en is crossed by the descender of the preceding line. The qualification's placement is read as applying to “géom. connexes”. | medium |

## 3. Abbreviations and compressed forms met

Expansions in this table are apparatus only. They have not been substituted into the transcription. Where an abbreviation or its punctuation is uncertain, the corresponding doubt remains in section 2. The meanings of `gén`, `ext`, and similar forms depend on their immediate context.

| Form as written / transcribed | Proposed expansion or interpretation | Location |
|---|---|---|
| `Aut ext` | Automorphismes extérieurs. | 531, initial display |
| `Aut` | Automorphismes. | 539, action group |
| `cqfd.` (uncertain) | Ce qu'il fallait démontrer. | 531, opening conclusion |
| `hom` / `hom.` | Homomorphisme; final point is not consistently visible. | 531–532 |
| `iso.` | Isomorphisme. | 531; 535–536; 540 |
| `isom` | Isomorphisme; no separate final point securely visible. | 534, corollary; 540 |
| `isom.` / `Isom.` | Isomorphisme(s); capitalization uncertain at the lower occurrence. | 539 |
| `isos` (uncertain alternative) | Isomorphismes. | 533, diagonal margin |
| `can.` | Canonique. | 532, arrow label; 535–536 |
| `iso.can` | Isomorphisme canonique. | 540, annotation above (12) |
| `i.e.` | *Id est*. | 531; 534; 537; 539–540 |
| `cf` | Confer / se reporter à. | 531 |
| Barred wavy m, `\overline{\mathrm m}` | Même. | 531; 537 |
| `surj` (uncertain) | Surjectif; proposed expansion of the doubtful arrow label only. | 532, composite map |
| `§` | Paragraphe / section. | 533; 535–536; 538 |
| `ens` | Ensemble. | 533; 534; 539 |
| `coeff` | Coefficient. | 533, signature |
| `ord` | Ordre. | 533, stabilizer |
| `Rev` | Revêtements; mathematical category name. | 533–534 |
| `ext` | Extension. | 533, diagonal margin |
| `ext.` | Extérieure. | 540, exterior power |
| `top.` | Topologique. | 534, insertion at top |
| `rev.` | Revêtement. | 534, (a) and NB |
| `NB` | *Nota bene*. | 534–535; 539 |
| `loc.` | Localement. | 534, NB |
| `noeth.` | Noethériens. | 534, NB |
| `dim` | Dimension; no final stop securely visible. | 534–535; 538 |
| `comp.` | Composantes. | 534, corollary |
| `rel.` | Relative. | 535, `dim rel. 1` |
| `pᵗ-base` | Point-base; the superscript t is retained in LaTeX. | 536, opening paragraph |
| `mb` (uncertain) | Membre. | 536, after (5bis) |
| `autom.` / `autom` | Automorphisme; punctuation varies. | 536; 538 |
| `int.` | Intérieur. | 536, after (6) |
| `bis` | Supplementary/repeated numbering designation. | 536, equation and cross-reference |
| `schém.` | Schéma; some occurrences remain doubtful. | 537–538 |
| `car.` | Caractéristique. | 537, last line |
| `tj.` (uncertain) | Toujours. | 537, last line |
| `gén` | Général / généralement. | 538, `plus gén` |
| `gén` / `gén.` | Générique. | 540, `fibre gén` |
| `sous-schém.` (uncertain) | Sous-schéma. | 538 |
| `dev.` | Devient. | 538 |
| `t.f.` | Type fini. | 538 |
| `Spec` | Spectre. | 538–540 |
| `id` | Identité. | 538, automorphisms |
| `Sch` | Schémas; category of schemes, with an unresolved subscript. | 539 |
| `Gl` | Groupe linéaire général. | 533, doubtful margin; 539 |
| `Sl` | Groupe spécial linéaire. | 533, alternative reading; 539, margin |
| `ssi` | Si et seulement si. | 539, margin |
| `p.ex` | Par exemple; punctuation and initial parenthesis are uncertain. | 539, final line |
| `idem` (uncertain compressed form) | Same assertion in the indicated other base situation. | 539, final line |
| `géom.` | Géométriquement, qualifying connected fibres. | 540 |
| `mod` (uncertain) | Modulo. | 540 |
| `car.0` | Caractéristique zéro. | 540, doubly underlined insertion |

## 4. Legibility and limits

The main prose and most central displays are readable, but the small corrections are appreciably less secure. Scan 533's long diagonal marginal note is the weakest passage: deletions, ornamental group letters, and writing close to the body text overlap. The first homomorphisms on 531–532 also leave the alphabet of the T/tau-like letter unresolved. On 534–536, particular caution is needed at the extra mark following the signature d, the circled correction in (3), the cancelled quotient formula, and the added basepoint terminology. Diagram (8)'s principal rows and columns are legible; its small side labels and adjoining oblique strokes are less certain.

On 538, the opening cancellation, the attachment of the added `id_E`, and the compressed final lines remain doubtful. On 539–540, the `(Sch)` subscript and the beginning of the qualification above “géom. connexes” are insecure. Several visible differences have deliberately been retained: the superscript 1 on the left of (5), `X^{!}` versus `X'`, the uncommaed subscript `11`, square versus round level brackets, `Spec[1/n]` without a supplied Z on 538, `Z/nZ` versus `Z[1/n]` around (10), and the successive torsion expressions on 540. None is treated as an editorial correction. The explicit doubt marks describe local limits of confidence; they should not be read as a guarantee that every other letter is beyond reconsideration.

## 5. Research notes — English, separate from the transcription

“Unproved claim” means that the required argument is not supplied in these ten scans; it does not mean that the assertion is false, novel, or unproved elsewhere. Each location below cites the supplied manuscript directly (Grothendieck, 1981). Own ideas are proposed checks or comparisons, with their confidence and reasons stated. They do not alter the transcription. No explicit conjecture has been inferred merely from a doubtful punctuation mark.

### 5.1. Questions, assertions, implications, and proposed checks

1. **Scan 531, approximately lines 9–17 — unproved claim / authorial question.** Grothendieck writes “de s'assurer qu'il en est bien ainsi” before requiring the homomorphism just used to agree, through a suitable isomorphism, with the other displayed homomorphism and its exterior actions. A proof would have to construct the comparison, specify its dependence on basepoints or paths, and verify compatibility with the exterior actions; a match between abstract group presentations would not by itself establish the intended compatibility. This records a comparison problem, not a claim that it has already been solved here.

2. **Scan 532, approximately lines 5–9 — authorial doubt / correction.** The “naturel” homomorphism is said to be “pas du tout celui qu'on avait en vue,” followed by “il me faut revenir à la charge.” This explicitly reopens the construction at the preceding page boundary. The statement should be checked against the eventual replacement construction before attributing a completed comparison proof to this passage.

3. **Scan 533, approximately lines 10–15 — unproved claim.** The parenthesis says that the two faithfulness conditions are “équivalentes” and concludes that each stabilizer is “un groupe cyclique.” A proof needs to use the actual hypotheses on the properly acting discrete group and the local surface action, including orientation preservation, and to clarify whether the global/local faithfulness comparison needs connectedness or an effectiveness assumption on each component.

4. **Scan 533, approximately lines 15–22 — unproved claim.** The quotient is asserted to be a paracompact surface, while the locus of nontrivial stabilizers and its image are called “partie discrète.” One should supply local quotient charts, a justification for discreteness under the stated action hypotheses, and the relation between the ramification index and the stabilizer order. These are proof obligations suggested by the written proposition, rather than silent additions to its hypotheses.

5. **Scan 533, diagonal margin — unproved claim.** The “Variante” asserts equivalences for equivariant covering categories and their fundamental groups after passage through a normal subgroup. Its exact ornamental group symbols and some wording remain uncertain, so a proof should only be formulated after checking the marginal transcription; it would need to define the quotient action and track the residual group in the covering-category construction.

6. **Scan 533, diagonal margin, `Application` — unpursued implication.** The marginal application links a group with subscript `(0,3)` to the primed T-like group with subscript `(1,1)` and writes a further extension by `\Pi_{0,3}`. This invites an explicit comparison of the extension and the displayed linear group, but the first linear-group letter is uncertain between `Gl` and `Sl`, so the transcription cannot settle which comparison is intended.

7. **Scans 531–533 — own idea (confidence: medium).** Compare the failed and proposed homomorphisms through their induced actions on a chosen covering category, with basepoint-change paths recorded explicitly. This may expose whether the discrepancy is in the abstract homomorphism, the identification of source/target, or the exterior-action compatibility; the reason for trying it is Grothendieck's own transition from a failed “natural” map to the covering-category formulation. This is a proposed investigation, not an established or claimed new result.

8. **Scan 534, (a)–(b), equation (1) — unproved claim.** The page asserts an “équivalence de catégories” between equivariant covers and covers subordinate to a ramification signature. A proof would need the local ramification model at nonfree orbits, reconstruction of the equivariant cover, and verification that morphisms descend and lift; those details are not supplied here.

9. **Scan 534, NB, approximately lines 6–15 — unproved claim.** “On peut expliciter un foncteur quasi-inverse” is followed by the prescription of a “normalisé” fibre product, with “un sens topologique facile à expliciter.” The missing construction should define that topological normalization at the branch locus and establish the two inverse equivalences; the scheme version likewise requires checking the hypotheses under which normalization gives the claimed cover.

10. **Scan 534, corollary, equation (2) — unproved claim.** The text gives an “isom canonique” of fundamental groups from the categorical comparison. Establishing its canonicity requires matching the fibre functors at the selected points, in addition to the categorical equivalence; the doubtful left basepoint in the manuscript remains a transcription issue.

11. **Scan 535, equation (3) — unproved claim.** For connected X, the page writes a “suite exacte canonique.” A proof must identify the kernel with the ordinary fundamental group of X and obtain the surjection to G from equivariant-cover monodromy; the circled correction makes the distinction between ordinary and equivariant fundamental groups especially worth checking.

12. **Scan 535, NB, approximately lines 4–12 — unproved claim / authorial expectation.** After claiming an analogous scheme-theoretic corollary, Grothendieck writes “il faudrait (si j'en ai besoin) faire un peu attention” when passing to relative smooth curves. His statement is explicitly left to be formulated more carefully; a proof would first need precise base, ramification, and connectedness hypotheses. The isolated mark after “On a” may itself be a question mark, but that reading is uncertain.

13. **Scan 535, example, equation (4) — unproved claim.** The quotient is specified by the three orbit rows and ramification indices “d₀=2”, “d₁=2”, and “d∞=3.” Verifying the example requires the actual action and quotient map, checking every exceptional stabilizer and confirming the stated image of each orbit; the deleted quotient identification should not be reconstructed from those expectations in the transcription.

14. **Scan 535, (4)–(5) — own idea.** A useful independent check would be to construct an explicit rational invariant of the six transformations of the thrice-punctured sphere and normalize its three exceptional values to the manuscript's 0, 1, and ∞. **Confidence: medium** that this is a productive calculation, because the displayed orbit data determine a concrete test; no explicit invariant or claim of novelty is supplied here.

15. **Scan 536, first paragraph and (5bis) — unproved claim.** Grothendieck observes that one “ne peut prendre x=P=j” for the preceding comparison and instead selects x outside the listed exceptional orbits, preferably with “Q=j” as the image basepoint. A proof should make explicit how the selected ordinary basepoint avoids the ramification locus and identify the resulting ramified-cover fundamental group with the named `\Pi'_{0,3}`.

16. **Scan 536, (5bis)–(6), approximately lines 9–16 — unproved claim.** The proposed passage from a generic x to the “point-base” P uses a “classe de chemins,” with the group prefix inserted above the line, and the resulting isomorphism “change par autom. int.” Checking this requires defining the relevant orbit/path class and calculating how a changed choice conjugates the identification.

17. **Scan 536, (6)–(7) — unpursued implication.** The page links the quotient-surface construction to the previously written sequence, saying it “n'est autre que (9bis) du § précédent,” with a more transparent interpretation continued on the next page. The compatibility of this geometric realization with the earlier construction is a concrete comparison problem, not an additional identity proved on this page.

18. **Scan 536, (6)–(7) — own idea.** One could test the path-choice ambiguity by writing generators represented by small loops around the two surviving branch values and tracking a change of path from P to x. **Confidence: medium** that this will clarify the inner-automorphism qualification, because conjugation by a connecting loop is directly visible in the construction; this is a proposed check rather than a new or established claim.

19. **Scan 537, lines 2–7 and diagram (8) — unproved claim.** The words “le diagramme de suites exactes” announce an arithmetic version of the preceding topological construction, without a proof on this page. A proof would need to specify the ramification conditions, identify the arithmetic and geometric groups, and verify exactness and compatibility of the horizontal and vertical sequences; the uncertain small annotations should be deciphered before interpreting the claimed identifications.

20. **Scan 537, paragraph after diagram (8), lines 1–4 — unpursued implication.** “Nous voulons maintenant mettre en relation” announces a comparison between the three-punctured parameter space with its permutation action and the elliptic modular multiplicity. One question for the following pages is exactly which stabilizers survive that comparison and whether the comparison concerns the moduli object itself, its quotient, or both.

21. **Scan 537, final three lines — own idea.** The decision “je vais travailler plutôt, sur” the base with 2 inverted suggests checking the comparison separately at odd residue characteristics, including characteristic 3. **Confidence: medium:** the change of base is explicit, but the necessary hypotheses of the comparison are not yet stated on this page, so no validity claim is made here.

22. **Scan 538, lines 1–4 and inserted correction — unproved claim.** The replacement phrase “est une gerbe liée par” `Z/2` changes the status of the preceding identification. A proof would need to describe the relevant moduli groupoids and descent, establish the asserted band, and distinguish the primed object from the unprimed level-2 object; the deleted sentence is too obscured to support a precise account of the earlier formulation.

23. **Scan 538, lines 6–14 — unproved claim.** The sentence beginning “si n est un entier ≥ 3” asserts that the indicated Jacobi rigidification really eliminates automorphisms, and explicitly extends the discussion to abelian varieties of arbitrary dimension. A proof would need to state the base and level hypotheses and show that an automorphism trivial on the indicated torsion subgroup is trivial; those hypotheses should be checked rather than supplied to the transcription.

24. **Scan 538, lines 14–17 — unproved claim.** For level 2, the text instead describes the automorphism as `id_E` over a “partie ouverte fermée de S” and `-id_E` over its complement. Verifying this statement over a general base would require both a classification on geometric fibres and a justification that the sign varies on open-and-closed pieces, including the passage through families and nonreduced bases.

25. **Scan 538, lines 17–23 — unpursued implication.** “Ceci suggère … de coiffer” the level-2 moduli object by one with higher even level proposes a presentation by an ordinary scheme of finite type. The assertion about its image in `Spec Z` calls for checking the exact definition of full level structure, representability, the permitted values of the level, and the role of inverting that level.

26. **Scan 538, lines 1–4 and 17–23 — own idea.** One can test the proposed higher-level presentation by tracing how the residual sign automorphism acts on the presentation and how it reappears in descent to level 2. **Confidence: medium:** both the `Z/2` gerbe language and the proposal to cover by higher level are explicit on this page, but this is a suggested verification strategy, not an established conclusion or a claim of novelty.

27. **Scan 539, lines 1–3, (9); unproved claim.** The phrase “se récupère comme” introduces a description of the modular multiplicity by a level-moduli scheme together with its `Gl` action. A proof would need to make precise the category represented by this pair and verify descent of both elliptic curves and their isomorphisms, including the stabilisers. The word “récupère” is marked uncertain in the transcription.

28. **Scan 539, second left-margin note; unproved claim.** The marginal assertion “représentable ssi n ≥ 3” includes the explicit contrast “ne l'est pas pour n = 1, 2”. Its proof would require both a representability construction at the indicated higher levels and a precise obstruction at the two lower levels, with the base hypotheses of the surrounding discussion retained. The small verb/reference glyph does not affect the legibility of the inequality or the two exceptional values.

29. **Scan 539, (10) and NB; unproved claim.** The text calls the coarse modular scheme “l'enveloppe représentable” of a nonrepresentable functor of isomorphism classes. What remains to specify is the universal property meant by this phrase, including its behaviour after a change of base; this is distinct from merely writing the orbit quotient in (10). No such proof is supplied on these two scans.

30. **Scan 539, first margin, and scan 540, (11); unpursued implication.** The insistence “Gl … et non Sl” can be compared with the later morphism to the torsor of primitive roots. The exterior-square construction suggests that the difference between changing an unrestricted level basis and imposing an additional determinant condition is relevant to the connected-component discussion. This is a connection to investigate, not a replacement for either displayed formula.

31. **Scan 539, line 13 and the parenthesis below (10); own idea.** The base immediately before (10) is written `Z/nZ`, whereas the line below it explicitly gives `Z[1/n]`. Before formalising the quotient assertion, check surrounding manuscript pages for the intended base and whether one occurrence is a slip, because the two literal expressions lead to different questions. **Confidence: high** that the two expressions differ visibly; no confidence claim is made about the author's intended correction.

32. **Scan 540, exterior-square display and the next display, approximately lines 10–12; own idea.** The written expressions include both `μ_n^{⊗−1}(S)` and then `μ_n(S)`. A useful check is to trace the author's conventions for torsion, duality, and exterior powers, and to distinguish group objects from their S-valued sections before comparing this computation with a pairing construction. **Confidence: medium:** the need for a convention check follows from the visible notation, while the explanation cannot be settled from these two pages.

33. **Scan 540, after (11), lines 20–21; unproved claim.** The morphism is asserted to have “fibres géom. connexes”, with an insertion read as “en car.0”. Establishing this would require a connectedness argument after fixing the primitive-root datum; a characteristic-zero uniformisation argument is one possible route to examine. The inserted qualification remains a palaeographic uncertainty and should be checked before treating it as a firm restriction.

34. **Scan 540, (12); unproved claim.** Passing “à la limite” produces the tower morphism and an identification with `Spec Σ` annotated “iso.can”. A complete argument needs compatible transition maps for the primitive-root torsors, a specification of the inverse-limit object, and the definition of Σ, which is not given on these two scans. The claimed canonicity should be checked against all those choices.

35. **Scan 540, (11)–(12), in conjunction with the `Gl` margin on 539; own idea.** One could track the change-of-basis action through the exterior-square construction at every finite level and then ask for compatibility with the limit. This may clarify which part of the arithmetic action is detected by the primitive-root datum and which acts within a geometric fibre. **Confidence: medium:** the finite-level maps in the manuscript motivate the construction, but compatibility and the precise action would still need proof; no novelty is asserted.

### 5.2. Literature comparisons proposed for further study

These comparisons were added after the readings were made. Their terminology does not replace the manuscript's own terminology or settle a doubtful symbol.

1. **Scans 533–537, covering-category comparison and exact sequences — own idea (literature comparison; confidence: medium).** Recast the proposed equivariant covering category through the quotient stack `[X/G]`, then compare its fibre functor and inertia with Noohi's covering-space Galois theory (2005, §§18.2–18.3, especially Theorem 18.19). The reason for this comparison is the close match between the manuscript's categorical and fundamental-group assertions and the modern covering-stack formulation, but the local path-connectedness and semilocal simple-connectedness hypotheses must be checked before applying that theorem. This offers a proof-organizing framework, not a claim that the two formulations have already been identified.

2. **Scans 539–540, the `Gl` margin, level structures, and (11) — own idea (literature comparison; confidence: medium).** Compare the unrestricted level-basis problem written here with Hain's pairing-normalized level structures and congruence-subgroup description (2014, §4.2). The reason is that the choice of a pairing value can affect which change-of-basis group and which geometric component are being considered, so the conventions must be aligned before comparing connectedness statements. The comparison does not authorize replacing the manuscript's `Gl` by `Sl`, or changing either torsion display.

3. **Scans 535 and 537–539, relative curves, representability, and the base with the level inverted — own idea (literature comparison; confidence: medium).** Use Deligne and Rapoport's *Les schémas de modules de courbes elliptiques* (1973) as a primary comparison source for the proposed relative and integral formulations. The reason is that the manuscript changes base and level conventions while leaving several representability assertions unproved here; a useful next step is to build a statement-by-statement comparison specifying the level functor, base, stabilizers, and quotient universal property. This is a research lead, not an assertion that an unspecified theorem there proves all the statements on these pages.

## 6. References

Deligne, P., & Rapoport, M. (1973). Les schémas de modules de courbes elliptiques. In *Modular functions of one variable II* (Lecture Notes in Mathematics, Vol. 349, pp. 143–316). Springer-Verlag. [Author's institutional publication record and scan](https://publications.ias.edu/deligne/paper/367).

Grothendieck, A. (1981). *La Longue Marche à travers la théorie de Galois* (cote 140-2; supplied scans 531–540) [Unpublished manuscript]. Université de Montpellier. Attribution, date, and shelfmark follow the supplied task brief; the transcription's immediate sources are the ten supplied image files.

Hain, R. (2014). *Lectures on moduli spaces of elliptic curves* (Version 3) [Preprint]. arXiv. https://doi.org/10.48550/arXiv.0812.1803

Noohi, B. (2005). *Foundations of topological stacks I* [Preprint]. arXiv. https://doi.org/10.48550/arXiv.math/0503247

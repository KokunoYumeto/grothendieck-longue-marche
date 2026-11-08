# LM_P047 — Reading notes

## 1. Source, scope, and pagination

This file accompanies `LM_P047_transcription.tex`, a diplomatic LaTeX fragment based solely on the ten supplied images. The fragment preserves the French, abbreviations, mathematical notation, cancellations, interlinear additions, marginal material, and two drawings; doubtful readings are marked rather than repaired from the mathematics. No external transcription, later manuscript pages, or mathematical literature was used to establish a reading.

The scan identifiers follow the filenames, as required by the task. The reproduced printed archive footer is consistently one number lower. The small lower-left handwritten numbers are retained with `\margin{…}` without assigning their authorship; only the top manuscript foliation is encoded with `\mspage{…}`. The printed institutional footer is not manuscript text and has not been transcribed.

| Supplied scan | Top manuscript number visible | Lower-left handwritten number / printed archive footer |
|---|---|---|
| 461 | 233 | 460 |
| 462 | — | 461 |
| 463 | 234 | 462 |
| 464 | — | 463 |
| 465 | 235 | 464 |
| 466 | — | 465 |
| 467 | 236 | 466 |
| 468 | — | 467 |
| 469 | 237 | 468 |
| 470 | — | 469 |

The `(29)` at the upper right of scan 462 is treated as an added reference near “on a,” not as manuscript pagination. The text begins and ends in continuation of material outside this batch; neither boundary has been completed. The LaTeX file deliberately has no preamble or macro definitions.

## 2. Table of doubts

Line numbers are approximate manuscript lines, counting formula rows where useful; equation numbers and named regions are more reliable locators. “High” means the reading or placement is strongly supported but a specific residual issue is recorded; “medium” means a plausible reading remains uncertain; “low” means cancellation, compression, or ambiguous attachment prevents a reliable choice. These are reading-confidence labels, not judgments about mathematical validity. Repeated instances of the same local glyph ambiguity may share one row. Counts in `\illegible{n}` estimate obscured words or, in mathematical material, short written units; they are not measurements of lost text.

### Scans 461–463

| Scan | Approximate line / region | Reading retained | Alternative / qualification | Confidence |
|---|---|---|---|---|
| 461 | l. 2, group before “l'élément” | `\mathcal H^{-}` | `\mathcal G^{-}`; this glyph looks different from the clearer G below | low |
| 461 | (40), parenthesis | `ss pts fixes` | `s pts fixes`; number of s strokes unclear | medium |
| 461 | above l. 4 | inserted `par (32)` | Attachment to “on trouve alors” inferred from the short insertion stroke; numeral 32 is clear | high |
| 461 | end of (41) | deleted, one unreadable unit | An overwritten mathematical glyph or short formula; no recovery asserted | low |
| 461 | slanted left margin, opening | `du reste` | `de suite` | medium |
| 461 | slanted left margin, connective | `donc` | Ending compressed into a stroke | medium |
| 461 | slanted left margin, ending | `ce qui est (42)` | `ce qui ⇒ (42)`; a word or an arrow cannot be securely distinguished | low |
| 461 | above unnumbered display | inserted `j∈I` | `i∈I`; the first letter is overwritten and a directing/correcting stroke is present | medium |
| 461 | unnumbered display before (42), first ρ | index `i` | `j` | low |
| 461 | same display, first braced subscript | `{j}` | `{i}` | medium |
| 461 | same display, second τ inside parentheses | subscript `{∅}` | `∅`; the apparent extra braces are retained as a doubtful literal reading | low |
| 461 | same display, τ immediately after parentheses | subscript `{0}` | `{∅}`; does not silently become the expected `∅` | low |
| 461 | (42), both ρ indices | `i` | `j`; same short hooked form as the earlier ρ index | medium |
| 461 | after `et de`, semidirect-product paragraph | deleted, approximately two unreadable units | Heavy horizontal overwriting; no expansion supplied | low |
| 461 | before `(τρ)^2=1` | doubtful deleted `τρ`, followed by `on a` | Exact letters and whether the first two glyphs are a canceled mathematical start remain uncertain | low |
| 461 | after `i.e. pour` | `tt` | Universal-quantifier glyph `∀` is another possibility; if alphabetic, probably “tout” | low |
| 461 | next line, `σ∈…` | `\mathcal H^{-1}` | `\mathcal G^{-1}`; the literal exponent −1 is much clearer than the group letter | low |
| 461 | between σ and underlined assertion | deleted, one unreadable glyph | A τ-like overwritten character, not securely recoverable | low |
| 461 | definition of V₀, union index | `j∈I` | `i∈I`; lower stroke reinforced | medium |
| 461 | definition of V₀, cylinder | `\overline T_j` | `T_j`; separation of the upper bar from the T's crossbar is weak | medium |
| 461 | final line, component symbol | `π₀` | Handwritten capital Π₀ cannot be fully excluded; ordinary component notation has not been used as proof of the reading | medium |
| 462 | l. 1, both cylinders | `\overline T_j` | `T_j`; bar/crossbar distinction weak | medium |
| 462 | l. 1, `(29)` | added reference following “on a” | Placement is above the line; no autograph folio 29 is inferred | high |
| 462 | l. 5, before `(z,t)` | deleted, one unreadable unit | Overwritten symbol, possibly an abandoned variable | low |
| 462 | l. 5, interlinear membership after `(z,t)` | `\overline T_j` | `T_j`; the insertion shows the same uncertain bar/crossbar distinction as the other occurrences | medium |
| 462 | l. 5, transformation after “pt fixe de” | `tau` | `z`; the local sign is unusually z-shaped, and has not been identified solely from the calculation | medium |
| 462 | l. 5, after `τρ_j^{n_j}` | `ssi` | `ss`; final short stroke indistinct | medium |
| 462 | l. 6, between `t=0,` and `et` | deleted `si` | deleted `et` | low |
| 462 | (45), cylinder base | `\overline T_j` | `T_j`; same bar issue | medium |
| 462 | (46), subset | `I'_u` | Plain `I_u` is less likely: an upper-right prime appears visible | high |
| 462 | (46), final line, verb | `sont` | `est`; short initial strokes are compressed | medium |
| 462 | (46), final line, adjective | `impair` | `impairs`; the final stroke does not securely establish the number | medium |
| 462 | l. 14, group before Aut | `\mathcal A_g` | `\widetilde{\mathcal A}_g`; a possible tilde is entangled with the slanted margin's `τρ″`; ordinary/script A also uncertain | low |
| 462 | parenthetical insertion above group line | `par un élément de A_g^+` | `comme élément de …`; the first two short words are cramped; a possible tilde over A is entangled with `est` from the main line | medium |
| 462 | transition to canceled lower block | `ou aussi` | Reading and precise boundary of the large cancellation need inspection | medium |
| 462 | canceled block, first prose fragments | `mais … dans le groupe G (trop petit)` | Several intervening words irrecoverable; retained words separately marked where doubtful | low |
| 462 | canceled interline addition | `on a l'égalité … H` | Two units between “égalité” and the script letter unreadable; attachment and the letter H are uncertain | low |
| 462 | canceled middle, surrounding `ρ∈H` | four unreadable units, `ρ∈H`, two unreadable units | No sentence reconstructed from the algebra | low |
| 462 | canceled middle, before “d'une part” | `les questions` | First word and ending of the second interfered with by cancellation | low |
| 462 | canceled display near lower third | `(τρ)^{-1}·ρ_{I'}(τρ)=τρρ_{I'}` | First factor/exponent and entire right-hand expression uncertain; cancellation crosses these symbols | low |
| 462 | canceled final lines | `l'agrandissant, en` | Nested earlier deletion appears to precede a revision; word ending and exact deletion extent uncertain | low |
| 462 | canceled final lines | `complétant` | Terminal strokes partly merge with cancellation | medium |
| 462 | last canceled line | `chaque \overline T_j par une configuration plus` | Bar on T and “configuration” uncertain; the sentence is not completed | medium |
| 462 | slanted canceled margin, first displayed product | `(τρ)(τρ')(τρ)^{-1}` | Several initial factors overwritten; marked as a whole uncertain reading | low |
| 462 | same margin, underbrace labels | `ρ^{-1}` and `ρρ'^{-1}` | Both are compact and crossed; no missing τ inserted from calculation | low |
| 462 | same margin, middle power | `ρ^2` | Superscript looks like 2 but is cramped | medium |
| 462 | same margin, prose after `ρ²=ρ′ρ″` | `c.à.d.` | `càd.`; abbreviation and stops unclear | low |
| 462 | same margin, concluding prose | `τρ' est conjugué … τρ'' dans G, dès que ρ′ρ″∈H²` | Several initial/linking words unreadable; “conjugué” and second involution doubtful | low |
| 463 | l. 7, conjugacy criterion | `ssi` | `ss`; last short stroke unclear | medium |
| 463 | l. 11, holes | `D'_j` | `D_j`; small upper-right stroke may be a prime | medium |
| 463 | l. 11, after “On” | deleted, one unreadable unit | A short p-like start has been crossed out | low |
| 463 | l. 12, before “action” | `l'` | The l-like stroke may itself have been corrected/canceled; surrounding words are clearer | low |
| 463 | l. 13 and l. 22, dihedral letter | double-struck `\mathbb D` | bold `\mathbf D`; the D is doubled in the ink, but its intended typographic alphabet is uncertain | medium |
| 463 | l. 22, orthogonal group | deleted `3`, replaced by `2` | First numeral heavily corrected; 2 is clear | medium |
| 463 | l. 23, group replaced above line | deleted `Z/2Z`, inserted `{±1}` | Old expression heavily struck; retained as doubtful rather than silently omitted | medium |
| 463 | l. 24, range of α | unreadable deleted group, inserted `{±1}` | Old group notation cannot be recovered with comparable confidence | low |

### Scan 464

Approximate line numbers count the main handwritten lines from the top; formula rows count as lines. Marginal locations are described separately. A dash in the alternatives column means that no alternative was sufficiently legible to propose.

| Scan | Approximate line / region | Reading | Alternative(s) | Confidence |
|---|---|---|---|---|
| 464 | 11, immediately before first equals sign | Deleted illegible symbol | A short overwritten symbol; no safe reading | low |
| 464 | 11, immediately after first equals sign | ζ before u_{\zeta,\alpha}\tau^\beta | Unidentified ζ-like stroke; it has not been removed on mathematical grounds | low |
| 464 | 14 | rappellera | Ending is compressed; no secure alternative | medium |
| 464 | 15, first deletion after donc | One illegible word | — | low |
| 464 | 15, first interlinear addition | est à | à | low |
| 464 | 15, second deletion | plus | — | low |
| 464 | 15, second interlinear addition | priori | — | medium |
| 464 | 18, overwritten subscript after D | 2g | n | medium |
| 464 | 20, trajectory/index-set glyph | Calligraphic J | Blackboard J | low |
| 464 | 20, after p.ex. | les | ici | low |
| 464 | 20, following word | justement | — | medium |
| 464 | 22, deleted word before parenthesis | les | — | low |
| 464 | 21–22, insertion above μ_{2g} lui-m̄ | l'ens | — | low |
| 464 | 21–22, same insertion | 2g ièmes | Exponent/ending after the number is compressed | low |
| 464 | 21–22, insertion attachment | After μ_{2g} in the transcription | The bent long stroke might attach the insertion nearer lui-m̄; not taken as an emphasis underline | low |
| 464 | 22, after lui-m̄ | vu | — | low |
| 464 | 22, following deletion | One illegible word | — | low |
| 464 | 22, before sous-ens. | pour | — | low |
| 464 | 25, before P_0 | point | pt | medium |
| 464 | 27 | transformés | transformées | medium |
| 464 | lower-left margin, first line | simplemt | simplement with a compressed ending | medium |
| 464 | lower-left margin, third line | rencontre | — | low |
| 464 | lower-left margin, product before D'_0 | ζ_0 | ζ | low |
| 464 | lower-left margin, before exponential | où | — | low |

### Scan 465

| Scan | Approximate line / region | Reading | Alternative(s) | Confidence |
|---|---|---|---|---|
| 465 | 2, spelling/diacritic | ambiguité | ambiguïté; diaeresis not securely visible | low |
| 465 | 5, before aux éléments | correspond.ts | correspondants; possibly correspondant | low |
| 465 | 5, inserted quotient numerator and existing quotient numerator | Calligraphic J | Blackboard J | low |
| 465 | 7, initial standalone set glyph | S | Calligraphic J | low |
| 465 | 8, polygon size | 2g | 2μ as the handwritten shape appears | medium |
| 465 | 8, deletion under déterminent | forment | — | medium |
| 465 | 9, deletion after normalise | One illegible word | — | low |
| 465 | 12, quotient defining I | Calligraphic J | Blackboard J | low |
| 465 | 16, symbol before restriction to V_0 | τ | The lower stroke is heavily retraced | medium |
| 465 | 20, cancelled formula number | (51) | The final digit is obscured by cancellation | low |
| 465 | 20, subscript of the right-hand ρ | Opening parenthesis in u(j) | The closing curve is visible; the opening curve after u is less secure | medium |
| 465 | last line | tout entier | Endings compressed | medium |
| 465 | lower-left insertion sur X_0 | Attached after l'action, with a visible comma retained | The leader overlaps the following de; attachment is very likely but punctuation is less certain | medium |

### Scan 466

| Scan | Approximate line / region | Reading | Alternative(s) | Confidence |
|---|---|---|---|---|
| 466 | 6, parenthesis within transport de structure | envers | Several letters are joined into a low stroke | medium |
| 466 | 7–8, insertion beneath τ_I | donné | donnée | medium |
| 466 | 8, before à τ'_j | égal | égale | medium |
| 466 | 10, raised glyph on τ_I | 2 | A retraced or cancelled superscript; no confident alternative | low |
| 466 | 11, circles | médians | Ending is compressed | medium |
| 466 | 13, after commute | également | Possibly an abbreviated ending | medium |
| 466 | 15, after il | ne | me | medium |
| 466 | 15, after pas | important | Retraced final strokes | medium |
| 466 | 16, before closing bracket | adoptons | Ending is compressed | medium |
| 466 | 19, small cancellation above the line after τ_g | par | — | low |
| 466 | 22, cancelled first factor after G = | H in the script alphabet | The crossed strokes do not allow all details of the former factor to be recovered | low |

### Scans 467–470

| Scan | Approximate line / region | Reading in transcription | Alternatives or issue | Confidence |
|---|---|---|---|---|
| 467 | 5; insertion over 12 | `\pi_g` | `\Pi_g`; the handwritten pi does not unambiguously specify case | medium |
| 467 | 6, first word | `avec` | Final letters overwritten; no secure different reading | medium |
| 467 | 10 | `chgts` | Abbreviated word has compressed middle strokes | medium |
| 467 | 11, before `syst.` | `au` | `un`; no article supplied from grammar | low |
| 467 | 17, after “lanière” | inserted `L` | The raised L is clear; the curved baseline mark is treated as an insertion leader, though it initially resembles a cursive letter | medium |
| 467 | 20 | `s'introduisent` | Plural ending is compressed; singular `s'introduit` cannot be wholly excluded | medium |
| 467 | 21 | `voire` | `voir`; final stroke ambiguous | medium |
| 467 | left margin, second line when rotated | `remarquable` | Middle strokes compressed; no secure alternative | medium |
| 467 | left margin, third line when rotated | `rappelle` | Compressed verb; no secure alternative | medium |
| 468 | 1, last word | `des` | `les`; initial letter not securely separated | medium |
| 468 | 2 | `pris` | `pas`; `a` appears without a distinct accent | medium |
| 468 | 6 | `\pi_g` | `\Pi_g`; same handwritten case ambiguity | medium |
| 468 | 9 | `panachée` | Distinctive but highly compressed middle strokes; no secure alternative | medium |
| 468 | 11, deleted line | `apparaître` | Crossed-through letters | medium |
| 468 | 20, before `rho_0 tau` | `\illegible{1}` in deletion | One overwritten/erased symbol, possibly an earlier tau | low |
| 468 | 23, crossed commutators | `[epsilon_1,tau]` | `[tau,epsilon_1]`; ordering obscured by strikeout | low |
| 468 | 24, crossed relation | `(tau' epsilon_0)^2=(tau' epsilon_1)^2` | Primes, order and indices partly obscured; last `=1` clearer | low |
| 468 | lower-left margin, line 2 | `l'élément de repère` | Dense overlapping strokes; no secure alternative | low |
| 468 | lower-left margin, line 3 | `le fixe` | Compressed and partly overwritten | low |
| 468 | lower-left margin, line 3, after `et` | `\illegible{1}` | Roughly one word or abbreviation | low |
| 468 | lower-left margin, line 4 | `en somme` | Could involve `sommet`; reading not established | low |
| 468 | bottom-right margin, line 1 | `expriment` | `exprimant`; ending compressed | medium |
| 468 | bottom-right margin, lines 2–3 | `commutativité` | `commutation`; split word partly overwritten | low |
| 468 | bottom-right margin, after `tau` | `\illegible{1}` in deletion | Approximately one crossed word, perhaps a preposition | low |
| 469 | middle paragraph, 4th line | `involutions` | Rightmost ending close to the image border | medium |
| 469 | middle paragraph, 5th line, end of substitution | `epsilon_1` | Final subscript partly at the image border | medium |
| 469 | third line of final paragraph | `amusette` | Compressed medial letters; no secure alternative | medium |
| 470 | 4, after `ou dans` | `\mathcal G_g` | `\mathcal C_g`; large looped capital is not settled from this page | low |
| 470 | 5, after `puisque` | `\illegible{1}` in deletion | One densely cancelled symbol or word | low |
| 470 | 7, first word | `effectives` | `effectif`; ending compressed | medium |
| 470 | 9, after `pts` | `bases` | `base`; final stroke compressed | medium |
| 470 | 11, first word | `fondamental` | `fondamentale`; last letters do not visibly give the expected plural `fondamentaux`; no grammatical correction made | medium |
| 470 | 12 | `abéliens` | `abélien`; final s uncertain | medium |
| 470 | 16, below Z in SL(2,Z) | `\illegible{1}`, placed below Z | Small dense mark, possibly a cancelled g or j; neither its reading nor cancellation status is secure, and the placement does not assert that it is a meaningful mathematical subscript | low |
| 470 | 17, after “à travers les” | `tubes` | `trous`; compressed middle strokes are not securely recoverable | medium |
| 470 | 18, second displayed group name | `GP(1,k)` | `GL(1,k)`; P favored, opening parenthesis compressed, final argument may be k or h; not normalized to a familiar group | low |
| 470 | final line, after `Jean` | `\illegible{1}` | Possible `y`, `en`, or an m-shaped abbreviation; none securely read | low |
| 470 | final line, quoted verb | `mord` | Final quotation is visible; verb remains provisional | medium |

## 3. Abbreviations met

Expansions in this table are explanatory proposals only. They are never substituted into the transcription. Doubtful abbreviated forms remain explicitly doubtful in the fragment.

| As written | Proposed expansion or function |
|---|---|
| `ss` / `s` in “ss pts fixes” | sans; the number of s strokes is uncertain |
| `pts` | points |
| `pt` | point |
| `ens` / `ens.` | ensemble |
| `i.e.` | id est / c'est-à-dire |
| `tt` | tout; the first occurrence could instead be a quantifier glyph |
| `ssi` / `ss` in conditions | si et seulement si; the final stroke is sometimes uncertain |
| `c.à.d.` / `càd.` in the cancelled margin | c'est-à-dire; form and stops uncertain |
| `$\overline{\mathrm m}$` | même |
| `p.r.` | par rapport |
| `p.ex.` | par exemple |
| `sous-ens.` | sous-ensemble |
| `simplemt` (uncertain) | simplement |
| `correspond.ts` (uncertain) | correspondants; exact ending uncertain |
| `dim` | dimension |
| `chgts` (uncertain) | changements |
| `syst.` | système |
| `rev.` | revêtement / revêtements, according to the occurrence |
| `NB` | nota bene |
| `autom` | automorphismes |
| `Int` | intérieur, as a mathematical operator |
| `card` | cardinal |
| `Aut` | automorphismes, as a group notation |
| `exp` | fonction exponentielle |
| `½ direct`, `1/2 direct`, `1/2-direct` | semi-direct; the fractional form and local hyphenation are retained |
| `½ simple` | semi-simple; the fractional form is retained |

## 4. Legibility and limits

Most uncancelled main text and the larger numbered displays are readable after enlargement. This remains a provisional diplomatic reading: a word that fits the argument is not necessarily the word written, and a recognizable mathematical glyph may still leave its alphabet, subscript, or revision state uncertain.

| Scans | Least secure material |
|---|---|
| 461–463 | The script G/H distinction, i/j indices, and possible T overbars; the braced subscripts before (42); especially the extensively cancelled lower third and slanted margin of scan 462. |
| 464–466 | The extra ζ-like stroke in the first formula on 464, the revised orientation reservation, the orbit-choice insertion and diagonal marginal condition; the S/J distinction and cancelled numbering on 465; the raised 2-like mark on τ_I on 466. |
| 467–470 | The narrow rotated margin on 467 and small margins/cancelled algebra on 468; the few right-edge endings on 469; the larger-group glyph, overwritten mark under Z, group notation near the end, and final incomplete sentence on 470. |

The drawings are described from their visible contours, line styles, and labels; missing gluing data have not been supplied. Insertion attachment and the extent of some cancellations remain uncertain even where individual letters can be read. The doubt tables record these limitations explicitly, and the research notes below do not alter the transcription.

## 5. Research notes — English, separate from the transcription

All manuscript quotations and attributions below refer to Grothendieck (1981), with the supplied scan identifiers and local equation or line anchors. “Conjecture” also covers the author's questions, expectations, and proposed programme; a question may be answered on the very next supplied page, which is stated where relevant. An “unproved claim” means that proof details are not given at the cited location, not that the assertion is false or unproved elsewhere. The proposed implications and own ideas are research leads scoped to these pages; they have not been checked for priority, later treatment in the manuscript, or resolution in the literature.

### 461-R1 — Unproved claim — semidirect-product normal form (approximately ll. 9–11)

“Ainsi G apparaît comme le produit semi-direct” uses both the inversion relation and the identification `H≃Z^I`. The displayed calculation establishes the conjugation action locally, but this excerpt does not itself prove independence of the generators of H or uniqueness of the asserted normal form. A complete proof would have to import those previously established facts or verify them for the supported cylinder transformations.

### 461-R2 — Unpursued implication — the negative coset consists of involutions (approximately ll. 12–14)

The assertion “est une anti-involution !” following `(τρ)^2=1` suggests studying the full family indexed by H before imposing geometric equivalence. The inversion action makes the distinction between enumerating involutions and classifying their conjugacy classes particularly important; the latter is taken up explicitly in scan 463. This observation is a consequence to check within the stated group structure, not a claim of novelty.

### 461-R3 — Unproved claim — additivity of the fixed-set index (approximately ll. 15–20)

“il suffit de prendre la somme des” reduces the global index to the cylinder contributions continued on scan 462. To make the reduction fully explicit, one should verify that the fixed set avoids V₀, that cylinder boundary identifications do not join distinct fixed components, and that all fixed components are accounted for by the local models. The present lines indicate the argument but leave these topological details implicit.

### 462-R1 — Unpursued implication — parity patterns versus the numerical index ((45)–(46))

The condition “n_j est impair” makes the numerical index depend on the cardinality of the odd-exponent set. Equal cardinalities need not record which cylinders carry the odd exponents; the numerical index therefore supplies less information than the entire parity pattern before further conjugacies are considered. A useful next comparison is between these patterns and the actions of the larger symmetry groups introduced later in the supplied sequence.

### 462-R2 — Unproved claim — geometric conjugacy of the involutions (after (46))

“Il est visible” is supplemented by “par des raisons générales” before a conjugacy assertion involving `u` and `τ_{I'}`. An explicit conjugator and a precise statement of its orientation behavior would clarify the assertion, particularly because the inserted parenthesis concerning `A_g^+` and the extensively canceled continuation are not fully legible. The canceled argument is not treated here as a valid theorem or as the author's final formulation.

### 463-R1 — Unpursued implication — a square-quotient parametrization (approximately ll. 1–8)

The criterion “ρ′ρ″^{-1}∈H²” identifies H-conjugacy of the displayed involutions with equality in the quotient H/H². Under the asserted finite-rank identification `H≃Z^I`, this gives a parity-vector indexing set with `2^{|I|}` elements. The passage does not at this point determine how many such classes become identified by additional surface symmetries.

### 463-R2 — Conjecture (expectation) — the richest simple symmetry arrangement (approximately ll. 9–13)

“La façon la plus riche en symétries simples … me semble la suivante” expresses a tentative geometric preference for the dihedral arrangement of the antipodal holes. It is not accompanied here by a defined extremal invariant or a maximality proof. Any attempt to formulate it as a theorem would first need to specify what counts as a simple symmetry and which competing configurations are admitted.

### 463-R3 — Unproved claim — passing from the spherical action to the punctured and attached surface (approximately ll. 9–25)

The instruction “on prend l'action type du groupe dihédral” gives formulas for the sphere action, while the choice of antipodal holes is described as part of the construction. To justify the later induced surface action, one needs equivariant choices of disks and compatibility of their attaching maps with the cylinder models. This is a construction problem suggested by the page, rather than an assertion that the supplied segment contains no later treatment of it.

### 463-R4 — Own idea — classify the parity vectors under the explicit finite symmetries (after (48))

Compute the action of the transformations `u_{ζ,α}` on the cylinder labels, then study its orbits on the quotient H/H² from the preceding criterion. **Confidence: high as a feasible research step**, because both the local transformation formulas and the square criterion are explicitly present; a full orbit computation and the comparison with geometric conjugacy still require work. This is a proposed calculation, not an established result or a claim of novelty.

### 463-R5 — Own idea — examine the smallest genera separately (following the dihedral construction)

Work out the configurations with one and two antipodal pairs, recording separately the action on the sphere, on the holes, and on the set of paired cylinders. **Confidence: medium**, because the explicit formulas make the examples accessible, but possible kernels or coincidences in these small cases have not been computed here. This check could expose qualifications needed in a general presentation without altering any manuscript reading.

### Scan 464

- **Scan 464, approximately lines 1–13 — unproved claim.** Grothendieck writes “On peut d'ailleurs l'élargir en un groupe” and gives the enlargement by the antipodism, including commutation and coordinate formulas. A proof would verify the commuting involution, its independence from the first factor, and the displayed actions directly from the earlier coordinate conventions; the extra ζ-like glyph in the transcription must be checked as handwriting before interpreting that formula.
- **Scan 464, approximately lines 14–17 — unpursued implication.** The phrase “τ renverse l'orientation” is followed by a visibly revised reservation concerning “transport de structure.” These pages therefore call for a distinction between equivariance as a topological action and equivariance respecting orientation; the exact wording of the reservation is uncertain, so no sharper assertion is attributed to him.
- **Scan 464, approximately lines 18–27 and lower-left margin — unproved claim.** The construction says “On choisit un disque” and then takes its translates, with a marginal condition apparently requiring disjointness from a neighboring translate. A complete construction would state the size and disjointness requirements and verify that the chosen disks and their boundary identifications support the subsequent group action.
- **Scan 464, lower-left margin — own idea.** One could try to make the geometric smallness condition explicit by giving the initial disk a radius bounded in terms of the adjacent orbit-point spacing. **Confidence: medium:** the visible note appears to impose disjointness from a neighboring rotation, but the coordinate metric and the full earlier disk conventions are not supplied on this page.

### Scan 465

- **Scan 465, approximately lines 1–12, equation (49) — unproved claim.** The assertion “la surface X_g est déterminée” continues by saying it is unambiguous, and the dihedral group acts “par transport de structure”; the text then asserts that it normalizes G. A proof would verify compatibility of the disk identifications and cylinder maps with the action, then check the displayed conjugation of each τ indexed by a subset.
- **Scan 465, approximately lines 13–20, equation (50) and following display — unproved claim.** The antipodism τ_g is asserted to “commute à l'action” of the dihedral group, and the next display gives a permutation rule for the ρ_j. The required verification would track the extension from V_0 through the cylinders and distinguish an identity of actual transformations from any weaker isotopy statement.
- **Scan 465, approximately lines 21–23 — unpursued implication.** From “d'où un produit 1/2-direct” the page constructs an action of the indicated product on X_g. The existence of that action does not by itself determine its kernel, which is not calculated here.
- **Scan 465, last two lines — conjecture.** The phrase “Quant à la question de prolonger” introduces the question of extending the enlarged dihedral action from X_0 to X_g. The immediate continuation on scan 466 addresses it; this entry records the question locally rather than presenting it as an unresolved conjecture.
- **Scan 465, equations (49)–(50) — own idea.** Test the action on a single cylinder in coordinates to check exactly which transformations permute the twist generators and which invert them. **Confidence: medium:** the formulas specify the desired behavior, while the preceding page explicitly warns about orientation reversal; the missing earlier coordinate/gluing conventions have to be recovered before drawing a conclusion.

### Scan 466

- **Scan 466, approximately lines 1–4 — unproved claim.** The extension question is answered by “ça a été fait sans crier gare,” followed by the correspondence from the antipodism of X_0 to τ_g and its commutation with the dihedral action. To justify the resulting enlarged action one would check the defining relations of the extra involution on all of X_g, including the cylinders.
- **Scan 466, approximately lines 4–12 — conjecture.** “Il pourrait sembler plus naturel” introduces an alternative convention that would associate τ_I with the initial antipodism. He then compares the coordinate expression and the fixed circles; the raised 2-like glyph in the fixed-point sentence remains a transcription uncertainty and must be resolved before using that particular statement literally.
- **Scan 466, approximately lines 12–14 — unproved claim.** The statement “τ_I commute également à D_n” is accompanied by a short argument from (41) and the product of the ρ_i. A complete check still requires the earlier definitions of those generators and the dihedral permutation of their indices, rather than assuming that invariance merely follows from the notation.
- **Scan 466, approximately lines 15–16 — conjecture.** The passage treats the choice of convention as apparently unimportant “pour le moment,” expressing an expectation about its practical irrelevance at this stage; the small ne/me reading and some endings remain uncertain. It does not establish equivalence of all geometric or quotient constructions that could use the two involutions.
- **Scan 466, approximately lines 17–22, equation (51) — unproved claim.** “On peut donc dire aussi que le groupe” introduces an action of the enlarged dihedral group on H and the containing product in (51). Its verification requires compatibility of that action with the already specified action of τ_g and with the inclusion of G; the factor order and the cancellation in (51) have been preserved rather than standardized.
- **Scan 466, alternative convention — own idea.** Compare the quotients produced by the two extension conventions, starting with the explicit local map (z,t) ↦ (z,−t). **Confidence: medium:** this local model suggests a fixed middle circle, but the global conclusion is conditional on resolving the raised glyph in the fixed-set sentence and checking the earlier gluing.
- **Scan 466, relation τ_I = ρ_I τ_g — own idea.** Try to formulate the change of convention as a change of splitting by ρ_I, and determine whether conjugation within H realizes it. **Confidence: medium:** the written relation directly motivates the test, but the page neither proves such a conjugacy nor specifies its consequences for the full surface action.

### Scan 467

1. **Conjecture — lines 2–7.** The programme “Il faudrait maintenant” begins with “Expliciter l'action extérieure” on the surface fundamental group. These pages leave the explicit automorphisms and the treatment of basepoint changes to be worked out.
2. **Unproved claim — lines 7–11.** The subgroup written `(Z/2Z)^3` is said to stabilize a cylinder and to be interpreted as coordinate sign changes in three-dimensional Euclidean space. A verification would require writing the three involutions in the given geometric model and checking their independence, commutation, and preservation of the attaching circles.
3. **Conjecture — item 2, lines 12–20.** “Étudier l'action” concerns the “spécial” Teichmüller group of a cylinder or of a larger region made by adding a “lanière.” The precise boundary conditions defining this special group, and its homomorphism into the ambient group, are not specified here.
4. **Unproved claim — item 2, lower half.** The larger regions are described as “un tore à 1 trou” and “un tore à deux trous.” A proof would need an explicit gluing description, with Euler characteristic and boundary components checked against the drawings; the pictures alone do not encode every gluing convention.
5. **Unproved claim — left margin.** The local group is called “essentiellement un SL(2,Z),” then more precisely a central extension by `Z`, recalling the universal covering group of `SL(2,R)`. Identifying the extension would require specifying the group, the central element, and the comparison map; the adjective before `de SL(2,Z)` is uncertain in the transcription.
6. **Own idea — item 1; confidence: medium.** An explicit choice of based loops through each cylinder could turn the coordinate sign changes into substitutions on a surface-group presentation, with changes of connecting paths tracked as inner automorphisms. This is a plausible computational route because the passage supplies concrete geometric symmetries, but the resulting formulas have not been derived or checked here.
7. **Own idea — item 2 and margin; confidence: medium.** Compare the actions obtained when the boundary circles of the one-hole and two-hole regions are fixed pointwise versus merely preserved as sets. This may clarify which central extension is intended, because the text itself singles out a “spécial” subgroup without stating its boundary convention; this is a question to test, not an identification asserted as established.

### Scan 468

1. **Conjecture — lines 1–4.** “Il est possible qu'il faudra considérer” introduces pairwise combinations to study relations among the elements arising from the previously described regions; the exact reading `pas/pris a deux` is uncertain. What kinds of pairs suffice, and whether larger overlaps contribute additional relations, are left open.
2. **Conjecture — lines 4–10.** The proposed task is to write fundamental-group generators and “la fameuse relation” for a “panachée” arrangement of handles. The passage does not supply the loops, their ordering, or the connecting paths needed to determine the resulting word.
3. **Unproved claim — lower third.** The chosen involutions are asserted to satisfy the displayed order and commutation relations, including `(epsilon_1 tau')^2=1`. Checking these relations requires the geometric actions on the marked cylinder and the marked index; the left-margin discussion of that index is not fully legible.
4. **Unpursued implication — lines 17–25.** The relation `(epsilon_1 tau')^2=1` encodes a stabilizer symmetry at the chosen marked index, while the dihedral generators move the index. A systematic comparison of its conjugates is a possible way to test what relations among the transported twists are actually forced by the proposed generating set; no such derivation appears on this page.

### Scan 469

1. **Unproved claim — (52).** The words “sauf erreur” qualify the assertion that the listed relations present the semidirect product. A proof would need both that the geometric generators satisfy the relations and that the abstract presented group maps injectively into the intended product; in particular the commutation of the transported generators of the abelian subgroup needs examination.
2. **Unproved claim — (52 bis) and the sentence following it.** After changing the two dihedral generators to anti-involutions, the relations are said to be “essentiellement ‘les mêmes’,” apart from the last relation on the second line. The substitutions and their inverses should be checked algebraically, retaining the inner parentheses in the third term of that line.
3. **Unpursued implication — final paragraph continuing on scan 470.** The subgroup `H ≃ Z^g` is compared with a maximal torus, a comparison the next page develops as a question of intrinsic characterization. The finite group action and its normalizer offer concrete data with which to assess the scope and limits of that analogy.
4. **Own idea — (52); confidence: high for the conditional algebraic test, not for any claim of a previously unnoticed error.** For `g=2`, test the displayed presentation by imposing `tau=epsilon_1=1`: the remaining displayed relations permit `epsilon_0` and `tau'` to be arbitrary involutions and hence permit the quotient `C_2*C_2`. If the intended product has finite dihedral factor and `tau` inverts every generator of `H ≃ Z^2`, imposing `tau=1` instead forces the image of `H` to have exponent two, making that intended quotient finite. This discrepancy would require rechecking the exact presentation and any implicit hypotheses or omitted relations; it is not a license to alter the transcription.

### Scan 470

1. **Conjecture — lines 1–5, continuing scan 469.** The maximal-torus comparison motivates the wish for “une caractérisation intrinsèque” in the Teichmüller group or a larger group whose handwritten capital is uncertain. No intrinsic group-theoretic criterion is supplied here.
2. **Unproved claim — lines 5–11.** The subgroup viewed as actual topological transformations is said to fix the points of `V_0`, with the poles offered as basepoints for universal covers and fundamental groups. A full verification should distinguish the actual transformation action from an action only up to isotopy, and check the restrictions of all the generators to `V_0`.
3. **Conjecture — lines 11–12.** “Ce sont peut-être les sous-groupes abéliens-libres maximaux” proposes a possible intrinsic characterization. The intended meaning of maximality and the ambient group need to be specified before this can be tested; the printed transcription does not strengthen this tentative sentence.
4. **Conjecture — lines 13–15.** “On aimerait étudier le normalisateur” is followed by the question whether it is exactly what comes from automorphisms of the complement of the cylinder interiors. A proof or counterexample would have to specify the boundary data needed for such complement automorphisms to extend across the cylinders, and compare their images with the whole normalizer.
5. **Conjecture — final paragraph.** The local groups associated to the “lanières” are asked to play “un rôle analogue” to rank-one groups in reductive algebraic-group theory. The analogy is explicitly posed as a question, and the second named comparison group is not securely readable, so no modern notation or specific theorem has been substituted.
6. **Own idea — maximality sentence; confidence: medium.** Look for an essential simple closed curve in `V_0`, outside the displayed cylinders and not parallel to their meridians, whose supported twist commutes with all `rho_j` and is independent of `H`. If such a curve and independence proof exist in the intended genus and ambient group, they would test the proposed maximality by extending `H`; neither existence nor independence has been established here. The distinction between actual homeomorphisms and isotopy classes is material to this test.
7. **Own idea — fixed basepoints; confidence: medium.** Use a common fixed pole to attempt based, rather than merely outer, automorphism formulas for the subgroup that fixes it. The reason this is promising is the explicit fixed-point statement, but compatibility of the choices with the larger symmetry group and with the universal covering transformations remains to be checked.
8. **Own idea — final rank-one analogy; confidence: medium.** Compute the homological actions of the groups supported on one “lanière” and on the larger two-hole region, then compare relations when two such regions overlap. This could expose which parts of the proposed analogy concern generation and which concern relations, without assuming that the analogy is exact or that any resulting structure is new.

## Source reference

Grothendieck, A. (1981). *La Longue Marche à travers la théorie de Galois* [Handwritten manuscript, cote 140-2, “La Longue Marche, pages 1–292”; supplied scans 461–470]. Université de Montpellier.

The date, title, and archival identification above are supplied by the task prompt; the university identification and archive footer are visible in the images.

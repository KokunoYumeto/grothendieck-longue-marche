# LM_P058 — Editorial notes and research notes

## Source, numbering, and scope

**Source reference (APA):** Grothendieck, A. (1981). *La Longue Marche à travers la théorie de Galois* [Handwritten manuscript, cote 140-2, supplied task scans 571–575]. Université de Montpellier.

All manuscript citations below refer to this supplied primary source. No published transcription, later manuscript passage, or external literature was used to settle the handwriting. The research notes identify work to investigate; they do not establish what the rest of the manuscript or subsequent literature proves.

The task's scan numbers, taken from the attachment filenames, differ by one from the numbers printed beneath the facsimiles:

| Task scan / filename suffix | Printed archive label | Upper manuscript number reproduced with `\mspage` |
| --- | --- | --- |
| 571 | 570 | 290 |
| 572 | 571 | None visible |
| 573 | 572 | 291 |
| 574 | 573 | None visible |
| 575 | 574 | 292 |

The matching lower-left foliation and printed institutional footer were treated as archive apparatus, not as additional authorial page numbers. The LaTeX fragment begins with `\scanpage{571}` and contains no preamble or macro definitions. The drawing descriptions are editorial descriptions inside `\figure`; they are not manuscript prose. The last triangular diagram is encoded in `tikz-cd`, with ordinary arrows in the directions visible on the page.

## 2. Table of doubts

Line locations are approximate visual baselines, counted from the first manuscript text or table heading, excluding the upper page number. Displays, interlinear additions, and marginal notes make exact line counts impractical; the equation numbers and quoted anchors identify the intended locations. Confidence concerns the preferred reading or interpretation of a mark, not the mathematical truth of the resulting statement. “No secure alternative” means that no competing word can responsibly be supplied.

### Scan 571

| Approximate line / location | Reading retained | Alternatives or unresolved issue | Confidence |
| --- | --- | --- | --- |
| ≈4, left of upper row of (74) | Opening-parenthesis-shaped mark `(` | Could be a nontextual stroke; marked `\unsure` rather than silently omitted. | low |
| ≈4 and ≈8, both linear groups | `Sl` | `SL`; the second letter looks like a cursive lowercase l. The alternatives are marked at both occurrences. | medium |
| ≈4–5, below “d'ordre 12” | A tiny overwritten or cancelled item | An infinity-like trace survives, but neither its reading nor its cancellation state is secure; both are qualified. | low |
| ≈7, “en fait, on doit avoir…” | Interlinear correction, encoded as an uncertain insertion | The text is between the two principal rows; no unequivocal caret establishes that it was added later. | medium |
| ≈7, correction's group subscript | `4` | `1`; the visible shape favors 4. No mathematically inferred 3 has been substituted. | medium |
| ≈11, “ces groupes … resp.” | `sont` | The heavy strokes may cancel the word or merely retrace it. The transcription exposes both states. | low |
| ≈14, replacement before “modulaires” | Deleted `variétés`, replaced by inserted `courbes` | The deleted word is partly obscured; no secure alternative. | medium |
| ≈17, first polyhedron sentence | `à faces` | The small à-like mark and compressed following word remain uncertain; the unusual “à faces des triangles” is retained. | medium |
| Margin beside ≈18–21 | `arêtes repliées` | Final letters are compressed; no secure alternative. The note is placed beside the first “triangles” passage. | medium |
| ≈18, insertion after “clair” | `a priori` | `a-priori`; the small leading mark could be a reduced a or part of a hyphenated form. | medium |
| ≈18, “par l'…” | `isom.` | `isom` without a stop; the abbreviation point is indistinct. | medium |
| ≈19–20, cartographic-group description | `triangulaire` | The visible ending can also be read as `triangula-`; no completion is supplied without a doubt mark. | low |
| ≈20, cartographic-group symbol | `\pi'_{0,3}` | `\Pi'_{0,3}`; the short curved legs do not securely distinguish case. | medium |
| ≈21, second polyhedron sentence | `à faces` | The first cluster is heavily overworked. A distinct cancelled word cannot be separated confidently from the à itself. | low |
| ≈23, “sous-groupes de…” | `congruence` | `congruences`; the final stroke does not securely establish singular or plural. | medium |
| ≈24, “très…” | `exactement` | Interior letters following ex are compressed and disconnected; no secure alternative word. | medium |

### Scan 572

| Approximate line / location | Reading retained | Alternatives or unresolved issue | Confidence |
| --- | --- | --- | --- |
| ≈6, parenthesis before “congruentielles” | `v.s` | Possibly a form resembling `v°s`; the abbreviation and its expansion are unresolved. | low |
| ≈12, b), first symmetric-group subscript | `2` | `4`; the ink looks more like 2, although the formula invites a different mathematical reading. | low |
| ≈18, crossed line before “Les courbes” | Deleted `Les variétés` | The first word and parts of the second remain visible, but the cancellation obscures the full sequence. | low |
| ≈19, end of “obtenues…” | `se` | The compressed end can resemble `sont`; only the tentative reading se is retained. | medium |
| ≈21, “qui sont…” | `retrouvés` | `retrouvées`; the ending is too compressed to distinguish securely. | medium |
| ≈25, left of the surviving radical formula | One illegible cancelled expression | A radical and fragments of an argument survive; the argument has not been reconstructed. Here `\illegible{1}` counts one expression. | low |
| ≈28, after the drawing | `formé` | `formée`; the final stroke does not resolve the ending. | medium |
| ≈28, after “d'un sommet,” | `sur` | No secure alternative. There are two visible words before “arête”; the first has not been omitted. | medium |

The curved guide under the inserted “quadratique” belongs to that insertion. It has not been transcribed as a parenthesis before “de Y” or as a tilde on Y. The first quotient is written `±1`, whereas the quotient in c) has braces `{±1}`.

### Scan 573

| Approximate line / location | Reading retained | Alternatives or unresolved issue | Confidence |
| --- | --- | --- | --- |
| ≈2, beneath inserted “repliées” | One illegible deleted word | `triplées` is visually tempting but insufficiently supported; it is not supplied in the transcription. | low |
| ≈4–5, “une face…” | `triangulaires` | `triangulaire`; a plural-like final stroke is visible despite the singular noun. | medium |
| ≈6–7, parenthesis after “d'autom” | `quotts` | `quotient`; this may be an abbreviation, but it has not been expanded. | low |
| ≈6–7, linear-group name | `Sl` | `SL`; lowercase l is favored, with explicit doubt. | medium |
| ≈6–7, integer-ring letter | Plain `Z` | Blackboard-bold `\mathbb Z`; unlike some earlier F's, doubling is not clear here. | medium |
| ≈9–10, insertion after 12 | `?!` after “mult. de 4 et de 6” | Exact punctuation is uncertain; the words, numerals, and attachment after 12 are substantially clearer. | medium |
| ≈10–11, after “pour que” | One short illegible deleted element | No secure reading; it is not silently suppressed. | low |
| ≈24–25, arithmetic-uniformity sentence | `toutes caractéristiques` | `toute caractéristique`; the final strokes do not settle number. | medium |
| ≈25–26, “de base…” | `quiconque` | `quelconque`; the ink favors the former, without a clearly visible tall l. No plural or dictionary spelling has been imposed. | low |
| Final line, arithmetic-group glyph | `\Gamma_{\mathbb Q}` | `\Pi_{\mathbb Q}`; two close left strokes and a curved upper stroke make the capital uncertain. | low |

The opening square bracket before “Ces variétés” and the parenthesis before “il faudrait” have no securely visible closing counterparts on this page; none has been supplied. The long curves below “triangulaires” and “rigidifiante” are read as letter descenders, not independent emphasis lines.

### Scan 574

| Approximate line / location | Reading retained | Alternatives or unresolved issue | Confidence |
| --- | --- | --- | --- |
| ≈3, personal name | `Malgoire` | No secure alternative; the internal cursive sequence is qualified rather than resolved from biographical knowledge. | medium |
| ≈7, deleted text after “variables” | `en` followed by infinity | Alternatively `\ne\infty`; both the reading and the deleted state are preserved. | low |
| ≈7, second-level insertion | `partout` | No secure alternative; the small word is inserted between “sections” and “distinctes”. | medium |
| ≈8, “la section…” | `correspondante` | The interior is compressed; no secure competing word. | medium |
| ≈9, symbol with subscript 0,3 | `U` | Possibly blackboard-bold U. The letter reads as U rather than M; the exact alphabet remains uncertain. | medium |
| ≈10, determinant insertion | One deleted word before `ad-bc` | Possibly `det`, perhaps `dont`; neither is secure enough to enter as a reading. | low |
| ≈14, formula (78), terminal mark | Comma | Period; the small mark has a possible tail. | low |
| ≈15, before `(a,b,c,d)` | A ξ-like glyph | Could instead be an illegible cancelled or overwritten element. Both reading and state are exposed in `\unsure`. | low |
| ≈20, “peut supposer … inversible” | `c` | The letter is heavily retraced; no secure alternative is supplied. | medium |
| ≈24, far right of final fraction | No definite terminal punctuation transcribed | Several dots or smudges may include punctuation, but no particular mark can be identified reliably. | low |

The long stroke beneath the determinant condition is treated as its insertion guide. The surviving algebraic factors, equations, and signs were checked individually; they are clearer than the surrounding cancellations.

### Scan 575

| Approximate line / location | Reading retained | Alternatives or unresolved issue | Confidence |
| --- | --- | --- | --- |
| ≈4, “elle est…” | `caractérisée` | `caractérisé`; the last vowel stroke is compressed. | medium |
| ≈5, invariance abbreviation | `p.r.` | The short second letter is indistinct; no secure alternative abbreviation. | medium |
| ≈6, below inserted variable list | Deleted `et` | The same glyph may be an uncancelled or overwritten et; both states are retained. | low |
| ≈9–10, “au premier…” | `mb.` | Possibly a more compressed form of the abbreviation for membre; no separate closing parenthesis is securely visible. | medium |
| ≈12, after “qu'on” | One illegible deleted glyph or word | A tall crossed cluster survives; no secure reading. | low |
| ≈14, before `GP(1)` | `moralement` | `normalement`; the visible tall l favors the first reading, but the sequence remains uncertain. | medium |
| Beside the diagram | One cancelled label or character | Possibly a repeated `c)`; insufficiently clear to transcribe confidently. | low |
| Diagram, left of descending arrow | `se factorisant` | The final letters are compressed; “par” below is clear. | medium |

The ornate symmetric-group letter is consistently represented by `\mathfrak S`. This is a typographic rendering of the visible hand, not a replacement of the groups by modern notation. The ordinary arrows, the label “épi”, the assignment `σ ↦ φ_σ`, and the inverse-permutation indices in (80) were individually checked. In particular, no hook or additional application parentheses have been introduced.

## 3. Abbreviations met

Expansions belong only to this list. An uncertain written form remains uncertain even when its likely expansion is familiar.

| Form as written or tentatively read | Scan(s) | Proposed expansion or interpretation |
| --- | --- | --- |
| `resp.` | 571 | respectivement |
| `isom.` / `isom` | 571 | isomorphisme; the stop is uncertain |
| `cf` | 571 | confer / comparez; no secure stop |
| `rég.` | 572, table heading | régulier / régulière |
| `or.` | 572, table heading | orienté / orientée |
| `v.s` [uncertain] | 572 | Unresolved; no expansion proposed confidently |
| `rev.` | 572–573 | revêtement |
| `autom` in `d'autom` | 573 | automorphismes; no secure terminal stop |
| `quotts` [uncertain] | 573 | Probably quotients, if the abbreviated reading is correct |
| `mult.` | 573 | multiple |
| `i.e.` | 573 | id est |
| `p. ex.` | 574 | par exemple |
| `etc` | 574 | et cetera; the transcription retains the absence of a secure stop |
| `coeff.` | 575 | coefficients |
| `p.r.` [uncertain] | 575 | par rapport |
| `mb.` [uncertain] | 575 | membre, in “premier membre” |
| `hom` | 575 | homomorphisme; no secure stop |
| `épi` | 575, diagram | épimorphisme / épimorphique |
| `Sl` / `SL` [case uncertain] | 571, 573 | Linear-group notation, probably groupe spécial linéaire |
| `GP` | 571, 575 | Group notation, probably groupe projectif; not redefined on these leaves |

The possible deleted `det` on scan 574 has not been counted as an established abbreviation because its reading remains unresolved.

## 4. Legibility and editorial limits

These pages are moderately legible overall, with substantially clearer displayed algebra than fast prose or overwritten material. The main risks are the anomalous subscripts in (74) and the quotient list, the exact alphabet of a few group symbols, compressed singular/plural endings, and the distinction between cancellation and retracing. The weakest readings are the qualifier before “congruentielles”, the short glyph before `(a,b,c,d)`, the final arithmetic-group capital on scan 573, and the parenthetical wording around `GP(1)`.

Each page was read as a whole, transcribed in sequence, and compared again with enlarged views; independent readings were then reconciled against the images. Disagreement was retained where the ink did not resolve it. Insertion guides were distinguished from underlining and from parentheses, and the complete displays were checked symbol by symbol. The LaTeX fragment also passed a compilation check with temporary definitions of the requested editorial macros; those definitions and the check output are not included in the deliverable.

This is a conservative working transcription, not a claim that every unmarked stroke is beyond dispute. In particular, the doubtful French forms, the apparent nonstandard subscripts, and the open punctuation have not been repaired for grammatical or mathematical consistency.

## 5. Research notes — separate from the transcription

These notes are in English and concern only what the supplied leaves state or leave open. “Conjecture” below includes an author's question, expectation, or proposed work program; it does not imply that he formulated a precise theorem. Own ideas are proposed investigations, not established results and not claims of novelty. Their confidence labels refer to the plausibility or usefulness of the proposed investigation.

### R1. Finite groups and the polyhedral table

**Location:** scans 571–572, (74)–(75). **Kind:** unproved claim.

The qualified “Sauf erreur” accompanies the tetrahedral and icosahedral identifications, followed by the four-row modular-curve/polyhedron table. A proof would have to recover the precise meanings of `SΓ′`, `GP`, and the prime on the level-2 curve, then verify the groups, covering actions, and orientation conventions; these leaves supply no such verification. The doubtful correction subscript in (74) remains a textual uncertainty and is not repaired by this proposed mathematical check (Grothendieck, 1981, scans 571–572).

### R2. Exhaustion of the rational congruence cases

**Location:** scan 571, approximately lines 13–15. **Kind:** unproved claim.

“Si je me rappelle bien” qualifies the assertion that the cases `n = 2, 3, 4, 5` exhaust the rational curves under discussion. Verification would need the exact moduli convention and a genus calculation, distinguishing the open curve from its compactification and checking what range of levels the surrounding discussion presupposes (Grothendieck, 1981, scan 571).

### R3. Why the realizations are congruence realizations

**Location:** scan 571, approximately lines 16–25. **Kind:** unproved claim.

The passage contrasts what was “clair” from the displayed group isomorphism with the further observation that the relevant subgroups are congruence subgroups. A proof would need to transport the combinatorial or covering objects through the stated isomorphism and separately identify their congruence kernels; the relation between these two steps is not worked out here (Grothendieck, 1981, scan 571).

### R4. The scope of the folded-edge exception

**Location:** scan 571, margin; scan 573, figure (76). **Kind:** unpursued implication.

The marginal “sauf un” directs the reader to the example with the tentatively read “arêtes repliées”. This makes it important to determine whether the asserted exhaustion concerns polyhedra in a restricted geometric sense or regular maps admitting the pictured edge behavior. The definitions and the exact status of this exception require comparison with the surrounding manuscript (Grothendieck, 1981, scans 571, 573).

### R5. Exhaustion by the listed proper quotients

**Location:** scan 572, quotient list a)–c) and the remark on d). **Kind:** unproved claim.

“On trouve comme quotients possibles” introduces an asserted complete list, with the exclusion of d) attributed to simplicity. A proof would enumerate the normal subgroups of the four displayed groups and then show why the resulting rational covers reduce to the two cases subsequently described. The uncertain source subscript in b) must be resolved textually before treating that particular written map as a reliable statement (Grothendieck, 1981, scan 572).

### R6. The quadratic cover and its drawn map

**Location:** scan 572, approximately lines 22–29. **Kind:** unproved claim.

The argument that the ramification index must “diviser 2 et 3” is followed by the equation `y = √(x(x−1))` and the one-vertex equatorial picture. A complete verification should specify the branch-point conventions, justify the unramified point, and recover the stated face and vertex indices from the cover. This would also clarify how the square-root expression is being used as a description of the covering curve (Grothendieck, 1981, scan 572).

### R7. The cubic quotient and figure (76)

**Location:** scan 572, final paragraph; scan 573, opening and (76). **Kind:** unproved claim.

The “rev. cyclique d'ordre 3” is described as ramified only at 0 and infinity and then associated with type `(3,3)`, folded edges, and a single triangular face. Reconstructing its monodromy and the corresponding cyclic ordering at the vertex would test the precise combinatorial interpretation of the picture. The unusual wording “une face triangulaires” remains a diplomatic reading, not a mathematical conclusion about the number of faces (Grothendieck, 1981, scans 572–573).

### R8. The proposed divisibility condition for rigidification

**Location:** scan 573, first paragraph, especially the insertion after 12. **Kind:** conjecture — expectation of a necessary condition.

“Il faudrait que le groupe de Galois-Poincaré du rev. soit multiple de 12” is strengthened or explained by the inserted “mult. de 4 et de 6 ?!”. Before attempting a proof, one must recover the definition of “rigidifiante” and determine which group-theoretic quantity the phrase “soit multiple” denotes in the preceding setup. The excerpt presents a proposed obstruction, not a demonstrated sufficient criterion (Grothendieck, 1981, scan 573).

### R9. Explicit interpretation of the three remaining modular curves

**Location:** scan 573, paragraph beginning “Il y aurait lieu”. **Kind:** conjecture — explicit research question.

“D'expliciter la relation” asks for a correspondence between points of the three remaining rational curves and elliptic curves with Jacobi rigidifications at echelons 3, 4, and 5. A satisfactory answer would specify the moduli objects and give the actual correspondence, rather than stop with the finite-group identifications. The inserted “courbes elliptiques à” is important to the object being requested (Grothendieck, 1981, scan 573).

### R10. What is expected to be in Klein

**Location:** scan 573, approximately lines 21–23. **Kind:** conjecture — expectation about existing work.

The author expects “des choses précises dans Klein”, but supplies no title, passage, or formula on these leaves. Locating what he had in mind would require a separate literature investigation and comparison of its normalizations with (75). No particular work of Klein has been identified or credited on the strength of this phrase alone (Grothendieck, 1981, scan 573).

### R11. Uniformity in characteristic and over a base

**Location:** scan 573, approximately lines 23–26. **Kind:** conjecture — desired extension.

The wish for constructions “valables simultanément” in the tentatively read “toutes caractéristiques” asks for more than formulas at complex points. It would require a precise formulation over a base scheme, with a treatment of the characteristics where the level or automorphism behavior changes. The wording after “de base” remains uncertain, so this note does not use a normalized spelling to strengthen the source's quantifiers (Grothendieck, 1981, scan 573).

### R12. The proposed connection with arithmetic actions on maps

**Location:** scan 573, final lines, continued on scan 574. **Kind:** conjecture — suggested connection.

“Ce souci semble intimement lié” connects the preceding moduli aim to the action of the arithmetic-group symbol with subscript Q on isomorphism classes of maps, especially regular spherical maps. The relation is asserted as an expectation, without a construction or a statement of equivalence on these leaves. The following assessment, “Dieu sait qu'elle est juteuse !”, emphasizes the perceived promise of the question but adds no precise mathematical conjecture (Grothendieck, 1981, scans 573–574).

### R13. From local homographies to a section over S

**Location:** scan 574, construction preceding (77) through the final formula. **Kind:** unproved claim.

The text proposes “la section correspondante” and then works with local coefficients whose determinant is invertible. The affine calculation is displayed, but independence of coefficient representatives, the handling of sections at infinity, and gluing over the base are not explained on these leaves. A proof should make those steps explicit while respecting the inserted requirement that the sections be everywhere distinct (Grothendieck, 1981, scan 574).

### R14. Characterization by invariance and normalization

**Location:** scan 575, after (79), conditions a) and b). **Kind:** unproved claim.

“Elle est caractérisée par les deux propriétés” claims uniqueness from homographic invariance and the normalization at `(0,1,∞,x₄)`. A proof would normalize the first three arguments and specify the rational-function domain and the meaning of the specialization involving infinity. The author's “avec un grain de sel” expressly flags that the expression on the left needs interpretation (Grothendieck, 1981, scan 575).

### R15. The permutation homomorphism and its factorization

**Location:** scan 575, symmetry paragraph, diagram, and (80). **Kind:** unproved claim.

The “propriété remarquable de symétrie” is encoded by a homomorphism from the four-letter symmetric group through the three-letter symmetric group to `GP(1)`. A direct proof would compute the fractional-linear transformations for generating permutations, verify the composition convention using the inverse indices in (80), and identify the kernel. Those computations are not supplied on this page (Grothendieck, 1981, scan 575).

### R16. Homogeneous-coordinate verification

**Location:** scans 574–575, cross-ratio calculation. **Kind:** own idea. **Confidence:** high as a verification strategy; the reason is that the affine expression already consists of paired differences.

I suggest replacing each difference by the determinant of two homogeneous coordinate columns and tracking how rescaling the four columns affects the full ratio. Checking cancellation of these factors could provide a coordinate-independent formulation and a gluing argument, including sections meeting the infinity chart. This is a proposed verification of the construction, not a result claimed by the transcription or a claim of novelty.

### R17. Generators, exceptional values, and small characteristic

**Location:** scan 575, diagram and (80), read alongside scan 573's arithmetic aim. **Kind:** own idea. **Confidence:** medium; direct substitutions are straightforward, but their geometric interpretation depends on the base and the moduli problem.

I suggest first calculating the transformations attached to adjacent transpositions, then studying where different transformations take the same parameter value. Repeating that calculation in characteristics 2 and 3 may help identify which stabilizer or branching phenomena must be addressed in an arithmetic formulation. This is a proposed investigation, not an assertion that any particular exceptional-value classification has been established here.

### R18. Formulate the level correspondences as moduli problems

**Location:** scan 573, the request at echelons 3, 4, and 5. **Kind:** own idea. **Confidence:** medium; the usefulness of the approach is clear, but the needed moduli definitions are outside this excerpt.

I suggest writing each sought correspondence as a comparison of explicit moduli functors, allowing a stack formulation if automorphisms persist. The comparison could then be tested over bases where the relevant level is invertible and over the remaining characteristics. This would separate questions about pointwise formulas from questions about representability, automorphisms, and base change without presupposing that the desired comparison exists.

### R19. Test the rigidification obstruction on the small quotients

**Location:** scan 573's divisibility remark, with the covers on scan 572. **Kind:** own idea. **Confidence:** medium; the examples are explicit, but “rigidifiante” must first be recovered from the manuscript's definitions.

I suggest reconstructing the local stabilizer or ramification conditions behind the numbers 4 and 6, then testing them on the quadratic and cubic quotient examples. This could distinguish a necessary divisibility condition from a sufficient rigidification criterion or reveal an overly strong formulation. No counterexample is asserted here.

### R20. Reordering four points and the preceding modular discussion

**Location:** scans 574–575, especially the factorization diagram. **Kind:** unpursued implication.

The explicit action on the cross-ratio suggests comparing the parameter for an ordered quadruple with the quotient obtained by forgetting its order. It would be useful to determine whether, and with which normalizations and base restrictions, that quotient connects to the modular objects discussed immediately before the “Complément”. This is an inferred direction of study; the identification is not supplied on these leaves (Grothendieck, 1981, scans 574–575).

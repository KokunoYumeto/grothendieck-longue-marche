# LM_P063 — Editorial and research notes

## Source and page identification

The transcription was made from the ten supplied JPEGs, `LM_P063_scan041.jpg`–`LM_P063_scan050.jpg`. The supplied prompt identifies them as scans 41–50 of Montpellier archive cote 140-3, *La Longue Marche*, pages 293–650. No published transcription, external reconstruction, or later mathematical account was used to supply readings.

**Primary-source reference (APA style):** Grothendieck, A. (1981). *La Longue Marche à travers la théorie de Galois* [Handwritten manuscript, cote 140-3, file described as pages 293–650; supplied scans 41–50]. Université de Montpellier.

The scan sequence, the printed archive pagination, and the larger handwritten numbers at the top are distinct:

| Scan marker | Printed archive footer; matching small lower-left number | Larger manuscript number visible at top |
|---|---|---|
| 41 | 40 | None visible |
| 42 | 41 | 309 |
| 43 | 42 | None visible |
| 44 | 43 | 310 |
| 45 | 44 | None visible |
| 46 | 45 | 311 |
| 47 | 46 | None visible |
| 48 | 47 | 312 |
| 49 | 48 | None visible |
| 50 | 49 | 313 |

Only the top manuscript numbers are assigned `\mspage` markers. The authorship of the small lower-left numbers cannot be established from these images; their agreement with the archive footers is recorded here without treating them as a second confidently authorial pagination. No absent manuscript page number has been inferred. The printed archive URL and institutional footer are not included in the manuscript text.

## Editorial conventions and confidence

The `.tex` file is a fragment, starts with `\scanpage{41}`, and has no preamble or macro definitions. The requested macros distinguish uncertainty, unreadability, deletion, insertion, marginal writing, underlining, and diagrams. Ordinary line wrapping has not been reproduced mechanically. Words divided by the scan boundary remain at that boundary; an incomplete sentence at the end of scan 50 remains incomplete.

An alternative inside `\unsure{reading|alternative}` records a genuine competing visual reading. An isolated `\unsure{reading}` retains a tentative reading without pretending that a second one has been identified. `\illegible{n}` counts an estimated number of words or, in a crossed formula, an estimated unrecoverable written unit. A tentative abbreviation is not expanded in the transcription. The first member of an alternative is not a correction of the second.

The small unattached `3`-like mark near the beginning of scan 48 is retained as doubtful marginal material. No exponent, footnote function, or insertion point is assigned to it. The empty section/page references on scan 50 remain empty rather than being supplied or treated as recovered numerals.

Horizontal strokes have been distinguished from securely headed arrows. Diagram (56), whose horizontal directions are not secure, is given as a bracketed description with its objects, labels, vertical directions, and uncertain horizontal heads. In (60), the visible unheaded strokes are represented with dash connectors. No direction has been inferred solely from an expected functor or exact sequence. An apparently surprising formula, including (65), is retained without adding a quotient, relation, or missing condition.

The confidence column concerns the **visual reading**, not the mathematical truth of a statement:

| Confidence | Meaning |
|---|---|
| high | The relevant strokes support the recorded reading strongly; the row may document a previously doubtful feature or a consequential detail retained as written. |
| medium | The reading is plausible from the ink, but an ending, abbreviation, symbol, or attachment remains insecure. |
| low | The strokes do not discriminate reliably between alternatives, or substantial text is unreadable. |

Locations below refer approximately to the **handwritten lines**, counting from the top main-text line, not to line numbers in the `.tex` file. Equations and marginal positions are used where they identify a passage more reliably. Repeated occurrences of one uncertain glyph may be grouped in a single row.

## Table of doubtful readings

Locations use the scan numbers 41–50. Line references are approximate handwritten positions; equation numbers, insertion points, and margins provide the more precise anchors. Confidence assesses the reading of the ink, not the truth of a mathematical assertion. Repeated doubtful glyphs are grouped where the same issue recurs.

| Scan | Approximate handwritten location | Selected reading | Alternative or reason for doubt | Confidence |
|---|---|---|---|---|
| 41 | Opening, first category symbol | `C_{1,1}^{\mathrm{ext}\,\prime}` | `C_{1,1}^{\mathrm{cat}\,\prime}`; the raised letters are faint and compressed. | medium |
| 41 | Opening, after the second category symbol | `passant au` | `prenant un`; the reduced internal strokes do not securely distinguish the two phrases. | low |
| 41 | Opening, before `universel` | `autom` | The shortened word and its termination are indistinct; no expansion or final full stop is supplied. | medium |
| 41 | Opening, after the inserted `\{\pm1\}` | `du groupe` | `des groupes`; the article and final plural stroke are uncertain. | low |
| 41 | Following handwritten line | `fondamental` | `fondamentaux`; the ending is reduced, so singular agreement is not imposed from context. | low |
| 41 | After `de ce groupoïde` | `.` | The faint punctuation before the following dash may not be a full stop. | low |
| 41, 43 | 41: after `équivalent`; 43: insertion after `muni` | `can.\textsuperscript{t}` | The raised terminal letter and punctuation are not fully distinct. The abbreviated form is retained. | medium |
| 41 | Before `on tire maintenant une` | `dt` | `d'où`; the opening marks may be an abbreviation rather than the fully written phrase. | low |
| 41 | (56), upper-left object | `C_{1,1}^{\mathrm{ext}\,\prime}` | The second subscript can resemble `0`; it is not resolved solely from the repeated notation. | medium |
| 41 | (56), both horizontal connectors | `dirigées vers la gauche` | `non discernables`; the left-pointing appearance is stronger on the lower connector, but neither head is fully secure. | low |
| 41 | (56), following sentence, and (57) | `\mathrm{GP}` | `\mathrm{Gp}`; the height and loop of the second letter do not decisively establish its case. | medium |
| 41, 48, 50 | Matrix-group notation throughout | `\mathrm{Gl}`, `\mathrm{Sl}` | `\mathrm{GL}`, `\mathrm{SL}`; the second letter is looped, and the distinction between cursive lowercase `l` and uppercase `L` remains typographically uncertain. | medium |
| 42 | Opening paragraph, after `topologique` | `isotopique` | Several internal strokes are compressed. The word is not replaced by a mathematically more expected term. | medium |
| 42 | Opening paragraph, after `Legendre` | `relations` | The final `s` is reduced to a short stroke; singular `relation` remains possible. | medium |
| 42 | End of the first paragraph, before the two fundamental-group symbols | `de types` | `des types`; the small stroke after the preposition is not decisive. | medium |
| 42 | Between `\Pi_{0,3}` and `\Pi_{1,1}` | `ou` | `et`; the conjunction consists of short, faint strokes. | low |
| 42 | Second paragraph, after `de type` | `1.1` | `1,1`; the separator is too small to identify confidently. | medium |
| 42 | Lower-left marginal note, initial formula | `(-1)_{\pi'}` | `\operatorname{Aut}_{\pi'}`; the tightly joined initial strokes obscure the symbol. | medium |
| 42 | Lower-left marginal note, before `+1` | `multiplicateur` | `multiplicité`; the ending is not secure. | low |
| 43 | Struck-through word after `d'une` | `action` | `autre`; the deletion crosses most of the word. | low |
| 43–46 | (58); scan 44 before and in (60), including the deletion; scan 45 before and in (62); scan 46 opening insertion | `\mathcal E`, `\widetilde{\mathcal E}` | The curly extension glyph is not unambiguously distinguished from similarly formed Greek or script letters. The overwritten occurrence is especially weak. | medium |
| 43 | (58), connector from `\pi'` to the extension symbol | `\mathrel{\text{---}}` | No arrowhead is securely visible; a rightward arrow is not supplied. | medium |
| 43 | (58), final connector to `1` | `\longrightarrow` | An unheaded horizontal stroke is also possible. | low |
| 43 | Topological model, after `groupe topologique` | `E\simeq\mathbf U\times\mathbf U` | The second heavy letter can resemble `H`, and the precise alphabet of the repeated glyph is uncertain. | medium |
| 43 | Quoted phrase after `La théorie des` | `forages` | The final plural stroke is insecure; `forage` remains possible. | medium |
| 43 | Same quoted phrase | `simultanés` | The ending, accent, and plural are compressed; singular `simultané` is possible. | medium |
| 43 | Immediately after the quoted phrase | `relatif` | `relative`; the final inflection is not securely visible. | low |
| 43 | After `à une` | `situation` | The letter group is indistinct; `action` is a possible competing reading, not an adopted correction. | low |
| 43 | Before `groupe à lacets` | `d'un` | `de un`; the join after the preposition is uncertain. | low |
| 43 | Parenthesis, before `dans le cas discret` | `même` | Overlap with the diagonal marginal writing obscures the initial word. | low |
| 43 | Parenthesis, after `été` | `écrit` | The ending is faint. Grammatical agreement is not restored by adding a letter. | low |
| 43 | Parenthesis, before `conjecturaux` | `énoncés` | The beginning is crossed or obscured by the marginal writing. | medium |
| 43 | Diagonal margin, after `dans un cas` | `\illegible{2}` | Approximately two words cannot be recovered reliably. | low |
| 43 | Same margin, after `des forages` | `\illegible{1}` | Approximately one word cannot be recovered reliably. | low |
| 43 | Same margin, before `successivement` | `répétés` | Several letters intersect the main writing; no competing full reading is secure. | low |
| 43 | End of the diagonal marginal note | `...` | The terminal small marks may not constitute an ellipsis. | low |
| 44 | Opening paragraph, interlinear clause after `J` | `i_0 fixe par G` | The clause is inserted between baselines; the word `fixe` is particularly compressed. | medium |
| 44 | Opening paragraph, before `groupe \widetilde{\pi}'(J)` | `du` | `de`; the short final stroke is ambiguous. | medium |
| 44 | After (59), before the inserted `l'espace` | `cat.` | `ext.`; the initial letters of this abbreviation are not secure. | low |
| 44 | Left marginal note | `trivialement` | The middle and ending are reduced to extended strokes. | medium |
| 44 | Before (60), after `de G par \widetilde{\pi}'` | `correspondant` | The final inflection is compressed; it is not corrected to agree with another word. | medium |
| 44 | (60), all horizontal connectors | Unheaded connectors | Clear arrowheads are absent; the diagram retains dash-only connectors. | medium |
| 44 | After (60), first `s'identifie` | `donc` | The ending is very short and faint. | medium |
| 44 | Final handwritten line, continuing on scan 45 | `aussi` | The word is squeezed against the right edge; the following continuation stroke is retained. | medium |
| 45 | Paragraph after (61), after `structure à lacets` | `facile` | The internal letter sequence is compressed. | medium |
| 45 | Immediately before (63), deleted formula after `soit` | `\pi=` | The strokes are heavily crossed; the formula cannot be regarded as fully secure. | medium |
| 45 | Final handwritten line | `(0,3)` | The last digit is retraced or overwritten; an earlier reading cannot safely be recovered. | medium |
| 46 | Opening insertion after `extérieur` | `=\widetilde{\mathcal E}` | `\in\widetilde{\mathcal E}`; the first sign can resemble membership. The letter itself shares the extension-symbol doubt recorded above. | medium |
| 46 | Opening paragraph, deletion after `tel que` | `\deleted{\illegible{1}}` | The overwritten formula cannot be reliably recovered; the extent is estimated as one item. | low |
| 46 | (66), domain | `\widetilde{\pi}` | The letter is retraced or overwritten; no additional index is supplied. | medium |
| 46 | After (66), before `d'être` | `condition` | The internal strokes are weak, although this reading is favoured. | medium |
| 46 | Same sentence, inside quotation marks | `ramifié` | The ending and accent are faint. | medium |
| 46 | Final paragraph, after `ce n'est pas` | `tout` | The crossing stroke may be a retraced `t`, rather than a deletion. | medium |
| 46 | Final paragraph, after `défini` | `mod.` | `aux`; the initial abbreviation or word is unclear, including its punctuation. | low |
| 46 | Same quoted expression | `autom.` | The abbreviation and final full stop are uncertain; the following `int` is left unexpanded. | medium |
| 46 | Last handwritten line | `symétrie` | A plural ending is possible; the last stroke is inconclusive. | medium |
| 47 | First handwritten line | `choisit` | `décrit` is possible; the faint interior marks favour the selected reading without settling it. | medium |
| 47 | (68), connector from `\widetilde{\pi}` to `\mathbb Z/2\mathbb Z` | `\mathrel{\text{---}}` | No head is discernible on this horizontal link; a direction is not supplied. | high |
| 47 | Prose immediately after (69), between the two puncture-index sets | `\simeq` | `=`; the upper stroke may be curved or merely irregular. | medium |
| 47 | Insertion after `dessus` | `autre` | The word is reduced to a short stroke within `qui n'est autre que l'op. canonique`. | medium |
| 47 | Lower half, after `un tel` | `élément` | The second half of the word is run together or overwritten. | medium |
| 47–49 | 47: near the foot; 48: before the unnumbered map; 49: question after (73) | `l'hom.`, `hom.` | The final full stop is not secure at these occurrences. | medium |
| 47 | Inline map near the foot, after `l'hom. extérieur` | `\longrightarrow` | `\mathrel{\text{---}}`; the apparent right arrowhead may instead be an irregular endpoint of an unheaded stroke. | low |
| 48 | Opening interlinear insertion, before `un groupoïde` | `ds` | A very reduced `dans` is possible; the short form is retained as read. | medium |
| 48 | Upper middle of the page, between the first two handwritten lines | `3` | Detached small mark, possibly a digit or unassigned ink. No exponent, footnote reference, or attachment to nearby words is inferred. | low |
| 48 | Opening of the second paragraph | `Modulo` | The interior letters are compressed, although the selected reading is favoured. | medium |
| 48 | Same sentence, after `rédaction plus` | `soignée` | The final feminine ending is faint. | medium |
| 48 | Same sentence, after `sans` | `bavure` | `bavures`; the presence of a plural ending is not secure. | medium |
| 48 | Parenthesis immediately before (70), after `au moins` | `mod` | The short form is compressed; a final full stop is not securely visible and is not supplied. | medium |
| 48 | End of that parenthesis | `intérieurs` | `intérieur`; the beginning overlaps a descender from the preceding line, and the final plural stroke is insecure. | medium |
| 48–50 | (70), its right margin and subsequent prose; (71), the scan 49 margin and (73); (76) and the final paragraph | `\mathfrak S` | `\mathcal G`; the repeated swirled group letter leaves both letter identity and alphabet uncertain. Its mathematical role is not used to decide the glyph. | low |
| 48 | Right margin beside (70), after `on peut` | `le` | `la`; the second letter is very small. | medium |
| 48 | Same margin, after `préciser` | `mod. autom. int.` | The abbreviations and their punctuation are compressed into short strokes. | medium |
| 48 | Same margin, after `provenant` | `de` | `des`; the final stroke is ambiguous. | medium |
| 48 | Same margin, superscript on the group symbol | `1+` | `i,+`; the initial upright mark, possible comma, and spacing are cramped. | low |
| 48 | First main-text line after (70) | `mod. autom. intérieurs` | The abbreviations and the word ending are very compressed. This main-text phrase is separate from the marginal comment above it. | medium |
| 48 | Next handwritten line, before `sûr` | `bien` | The beginning is overwritten. | medium |
| 48 | Unnumbered map to `\mathrm{Gl}(2,\mathbb Z)` | `\sim` above the arrow | The small upper mark is thickened or overwritten. | medium |
| 48 | After `à l'occasion` | `,` | `;`; no upper dot can be identified securely. | medium |
| 48 | Final handwritten line, before `\mathrm{Gl}(2,\mathbb Z)'` | `ou à` | Only short connecting strokes remain visible. | medium |
| 49 | Immediately before (71) | `morphisme` | The initial letters are crossed by the diagonal marginal writing. | medium |
| 49 | (71), first target, principal letter | `\mathbb U` | `\mathbb M`; light and heavy overlapping letter-forms coexist. Their order of correction is not reconstructed. | low |
| 49 | (71), first target, final subscript | `3` | The digit is heavily retraced; no competing digit can be recovered safely. | low |
| 49 | Insertion beneath the first target of (71), after `courbe analytique` | `complexe` | `complète`; the internal strokes and ending are compressed. | medium |
| 49 | Diagonal left margin, after `dans les` | `réflexions` | The ending intersects the main text; the plural cannot be certified from every stroke. | medium |
| 49 | Same margin, after `complexe` | `de façon` | `afin`; overlapping main-text strokes support more than one segmentation. | low |
| 49 | Same margin, between `pas` and `(73)` | `ds` | `dans`; the abbreviation status is uncertain. The main display number (71) crosses this region but is not part of the marginal sentence. | medium |
| 49 | End of the same marginal note | `en qu.` | The terminal abbreviation is weak; its exact letters and punctuation are insecure. | low |
| 49 | After the deleted `dont l'effet sur` | `induit` | The initial letters are overwritten; no separate deletion is inferred. | medium |
| 49 | Immediately before (73), after `l'hom` | `ext.` | `cat.`; the two compressed letter groups cannot be securely distinguished. | low |
| 49 | Final paragraph, before `universel canonique` | `revêt.` | `revêtement`; the termination may be abbreviated or obscured by overwriting. | low |
| 49 | Final handwritten word | `de` | `des`; the last stroke may be the tail of `e` rather than an `s`. | medium |
| 50 | Opening line, name before `D` | `Poincaré` | The end of the name is extremely reduced. | medium |
| 50 | (74) and the parenthesis in (75) | `M` | `\mathbb M`; these occurrences are less clearly doubled than the earlier moduli symbols, and the alphabet remains doubtful. | medium |
| 50 | Left margin beside (75), after `en` | `forme` | `termes`; the middle letters are faint. | low |
| 50 | Same margin, after `de` | `ce morphisme` | Both words are poorly resolved and partly compressed into strokes. | low |
| 50 | Insertion beneath (76), first word | `cet` | The word is overwritten. | medium |
| 50 | Same insertion, after `iso.` | `qui` | The short word is faint and compressed. | medium |
| 50 | Margin beside (75) and insertion beneath (76), references | `cf \S\quad`; `\S\quad, p.\quad` | The reference numbers appear unfilled. Blank spaces are preserved rather than supplied with inferred section or page numbers. | high |
| 50 | First `U` in the paragraph after (76) | `0,3` | `3`; a small loop may be a `0`, but its following comma is not secure. Later repetitions do not decide this occurrence. | low |
| 50 | Final-line insertion between `Pour` and `l'identifier` | `pouvoir` | The fine letter endings are uncertain, although the insertion point is clear. | medium |
| 50 | Final basepoint formula, after `P=` | `-\bar{\jmath}` | `-j`; the short upper stroke may be an overbar or an elongated dot. | low |

## Abbreviations encountered

Expansions are given here only. Dots, the raised terminal letter, and doubtful forms follow the transcription; a proposed expansion does not settle an uncertain reading.

| Form encountered | Location | Proposed expansion or interpretation |
|---|---|---|
| `ext` | Category superscripts, scan 41 onward | *extérieur* or *extérieure*, according to the qualified object. |
| `autom` | Scan 41; parenthesis before (70), scan 48 | *automorphisme* or *automorphismes*; the written forms have no secure final full stop. |
| `can.\textsuperscript{t}` | Scan 41; insertion on scan 43 | Probably *canoniquement*; the raised terminal `t` is retained. |
| `dt` | Scan 41, before `on tire` | Probably *dont*, if the selected reading is correct; `d'où` remains an alternative reading rather than an expansion. |
| `Tors` | Scan 41, (56) and following sentence | *torseurs*. |
| `Gl` | Scans 41, 48 | Probably *groupe linéaire*; the second letter's case is not completely secure. |
| `GP` / `Gp` | Scan 41, (56)–(57) | Probably *groupe projectif*; the capitalization is unresolved. |
| `iso` | Scan 41, before (57) | *isomorphisme*; no final full stop is transcribed here. |
| `iso.` | Scans 44–45, 50 | *isomorphisme*. |
| `Autext` | Scan 42 | *automorphismes extérieurs*. |
| `lac` | Subscript of `Autext`, scan 42 | *lacets*, referring to the preserved lacet structure. |
| `NB` | Scan 42, marginal note | *nota bene*. |
| `i.e.` | Scan 42 margin; scan 44 insertion; scans 46–48 | *id est*, “c'est-à-dire.” |
| `cat.` | Scan 44, after `groupe fondamental`; alternative reading before (73), scan 49 | Expansion unresolved because the abbreviation itself competes with `ext.`; the latter would mean *extérieur*. |
| `top.` | Scan 45, after `surface` | *topologique*. |
| `hom` | Scans 46, 49–50 | *homomorphisme*; no clear final full stop is present at these occurrences. |
| `ext.` | Scan 46, in `(ext.)`; scan 49 before (73); alternative reading on scan 44 | *extérieur*. |
| `ab` | Group subscripts, scan 46 | *abélianisé* or *abélianisation*. |
| `mod.` | Scans 46, 48 | *modulo*; the reading on scan 46 competes with `aux`, and punctuation is uncertain. |
| `autom.` | Scans 46, 48–49 | *automorphismes*; punctuation is uncertain at the doubtful occurrences. |
| `int` | Scan 46 | *intérieurs*; no final full stop is supplied. |
| `op.` | Scan 47, insertion | *opération*. |
| `hom.` | Scans 47–50 | *homomorphisme*; the final full stop is explicitly doubtful in several occurrences. |
| `ds` | Scan 48, opening insertion; scan 49, diagonal margin | *dans*, if the abbreviated reading is correct; the full word remains a competing reading. |
| `mod` | Scan 48, parenthesis before (70) | *modulo*; no final full stop is securely visible here. |
| `int.` | Scan 48 margin; scan 49 opening | *intérieurs*; punctuation in the scan 48 marginal cluster is uncertain. |
| `an` | Superscripts, scans 49–50 | *analytique* or *analytiques*, according to the object. |
| `en qu.` | Scan 49, end of diagonal margin | Probably *en question*; the abbreviated reading remains doubtful. |
| `revêt.` | Scan 49, final paragraph | *revêtement*; the ink may instead contain the full word. |
| `can.` | Scan 50, in `iso. can.` | *canonique*. |
| `Sl` | Scan 50 | Probably *groupe spécial linéaire*; the second letter's case remains uncertain. |
| `cf` | Scan 50, left margin | *confer*, “voir” or “comparer”; no final full stop is supplied. |
| `rev.` | Scan 50, final paragraph | *revêtement*. |
| `p.` | Scan 50, insertion beneath (76) | *page*; the page number is left blank. |

## Legibility assessment

The main text is recoverable in substantial part, but these pages do not support an unqualified claim of exact transcription. Faint strokes often leave singular/plural endings, accents, abbreviation stops, and small primes unresolved. Darker revisions can obscure earlier writing, and diagonal marginal notes overlap both the main prose and display numbers. Enlargement and rotation made some strokes easier to inspect; they did not create evidence missing from the photographs.

The least secure areas are the opening of scan 41 and the horizontal connectors in (56); the note below scan 42; the diagonal note and closing grammatical endings on scan 43; the abbreviation after “groupe fondamental” on scan 44; the quotation near the end of scan 46; the recurring curled group glyph and its small marginal superscript on scan 48; the overwritten target of (71) and the diagonal note on scan 49; and the marginal definition note, first late occurrence of the index on `U`, and final basepoint on scan 50. The large page numbers and equation sequence (55)–(76) are more secure than these details. The doubt marks should remain in place until further image evidence resolves them.

## Research notes — English

These notes are separate from the diplomatic transcription. They concern what the **supplied excerpt** states, questions, or leaves implicit. “Unproved claim” means that a complete proof is not supplied on these ten scans; it is not a claim that the assertion is unproved in the literature. A point may be settled elsewhere in the manuscript. Mathematical suggestions below are proposals for checking, not corrections of the ink or assertions of novelty. All manuscript references below are to Grothendieck (1981), identified in the source reference above.

### R01 — Scan 41, (55)–(57)

**Kind: unproved claim.** The stated “équivalence de catégories” is accompanied by a square involving torsor categories and the quotient by the inserted central `{±1}`. A complete account would specify the functors and their compatibility with the indicated group isomorphism, while resolving the square’s uncertain horizontal directions from better evidence (Grothendieck, 1981, scan 41).

### R02 — Scan 42, approximately lines 6–13

**Kind: conjecture / authorial intention.** “J’aimerais expliciter maintenant l’équivalence de Legendre (55)” announces a direct construction in terms of groups with lacet data, following an argument using Teichmüller groups and an “isomorphisme ad-hoc.” The ensuing construction should be assessed for its definition on morphisms and its claimed canonicity, not merely for agreement on chosen topological models (Grothendieck, 1981, scan 42).

### R03 — Scan 42, final paragraph

**Kind: unproved claim.** The element `(-1)_{π′}` is described as “l’unique élément non trivial du centre” of the displayed outer-automorphism group. Verification requires the precise meaning of the subscript `lac`, followed by both existence and uniqueness under that convention; the separate marginal statement concerning orientation has its own reading uncertainties (Grothendieck, 1981, scan 42).

### R04 — Scan 43, opening and (58)

**Kind: unproved claim.** The passage from the exterior operation to “une extension canonique” is asserted directly. A proof would need to explain the extension construction, its dependence on the outer action, and the hypotheses under which its asserted canonicity holds (Grothendieck, 1981, scan 43).

### R05 — Scan 43, after (58)

**Kind: unproved claim.** “Exactement trois classes de π′-conjugaison de scindages” is justified by appeal to the topological model and its three nonzero fixed points. The missing comparison should identify sections with the stated fixed-point data and verify that the resulting correspondence is independent of the auxiliary realization (Grothendieck, 1981, scan 43).

### R06 — Scan 43, closing main paragraph

**Kind: conjecture / authorial qualification.** The author writes that there are, “pour le moment,” “énoncés conjecturaux” in the theory invoked for simultaneous drilling of holes. The exact scope of this qualification needs to be checked against the doubtful nearby wording and the continuation on scan 44; the construction should not be assigned a stronger status than the excerpt gives it (Grothendieck, 1981, scan 43).

### R07 — Scan 43, diagonal margin

**Kind: unpursued implication.** The marginal remark is tentatively read as mentioning “d’un trou à la fois” and “successivement.” If correct, it suggests checking whether iterated one-hole constructions suffice here, and whether different orders yield canonically comparable results; the difficult marginal reading prevents treating either conclusion as established (Grothendieck, 1981, scan 43).

### R08 — Scan 43, the section-conjugacy assertion

**Kind: own idea.** After choosing one section of (58), try an explicit nonabelian cocycle calculation of the other section-conjugacy classes, recording where the choice enters. **Confidence: medium**, because the extension formulation makes the test concrete, but the allowed lacet structure and the required notion of canonicity still have to be fixed from the manuscript.

### R09 — Scan 44, opening and (59)

**Kind: unproved claim.** “Construire canoniquement” introduces the new punctured group and an isomorphism compatible with the `G`-operations. A proof should distinguish construction up to inner automorphism from construction of an actual group with specified peripheral data, and should verify compatibility for morphisms as well as for one object (Grothendieck, 1981, scan 44).

### R10 — Scan 44, left margin

**Kind: unproved claim.** The note appears to say that `G` “opère trivialement” on the puncture-index set. A proof would identify all the relevant puncture classes and show that each is fixed individually; this observation remains conditional on the marked uncertainty in the marginal word (Grothendieck, 1981, scan 44).

### R11 — Scan 44, lower half and (60)

**Kind: unproved claim.** The extension is identified with the “groupe fondamental mixte” of the displayed space and action. Establishing this requires comparing the extension from the outer operation with the extension arising from the free topological action, including the precise equivalence relation under which that comparison is canonical (Grothendieck, 1981, scan 44).

### R12 — Scan 45, (61)–(62)

**Kind: unproved claim.** The lacet structure is called “facile à décrire,” and the puncture-index identifications are called canonical. The detailed argument would need to construct the peripheral subgroups through the covering and quotient, then justify both relations in (62), rather than infer them from cardinalities alone (Grothendieck, 1981, scan 45).

### R13 — Scan 45, (63)

**Kind: unproved claim.** “Boucher le trou en i₀” is said to produce the group written as `π = L(π′)`. A proof should specify exactly which subgroup or conjugacy data are killed, recover the remaining lacet structure, and account for the distinction between “effectif” and “extérieur,” which the author’s revisions emphasize (Grothendieck, 1981, scan 45).

### R14 — Scan 45, last paragraph; scan 46, opening

**Kind: unpursued implication.** “Reprenant en sens inverse” introduces the reversal using the “foncteur ‘forage de trous’.” It remains to determine at what categorical level this is an inverse, which additional choices it requires, and whether the two composites come with canonical comparison maps (Grothendieck, 1981, scans 45–46).

### R15 — Scan 46, (64) and the invoked functor

**Kind: unproved claim.** The drilling functor is used to add a distinguished puncture and obtain the displayed decomposition of the index set. A full construction would specify its independence of presentations or coordinates and its action on exterior morphisms (Grothendieck, 1981, scan 46).

### R16 — Scan 46, (65)–(67)

**Kind: own idea.** Check the earlier convention for `T^{I(\widetilde π)}` before interpreting the displayed abelianization and coefficient-sum map; one can test the notation against an explicit peripheral presentation of the four-punctured sphere. **Confidence: high that the convention needs checking, low about any proposed correction**, because the full index set is visibly written, while the algebraic meaning of that superscript may have been fixed elsewhere. No augmentation relation, quotient, or reduced index set has been added to the transcription.

### R17 — Scan 46, (66)–(67) and following prose

**Kind: unproved claim.** The homomorphism is characterized by being “‘ramifié’ en tous les i,” and its kernel is assigned type `(1,4)`. Verification should show that the prescribed peripheral values respect all defining relations and should calculate the topological type of the associated two-sheeted cover (Grothendieck, 1981, scan 46).

### R18 — Scan 46, closing paragraph; scan 47, (68)–(69)

**Kind: unpursued implication.** “Ce n’est pas tout à fait un groupe extérieur” flags an ambiguity beyond inner automorphisms, attributed to the extra involution. The exact sequence and puncture-index comparison on scan 47 provide a place to track how this extra symmetry acts on representatives and on morphisms (Grothendieck, 1981, scans 46–47).

### R19 — Scan 47, closing paragraph; scan 48, opening

**Kind: unproved claim.** The requirement to have “‘choisi un noyau’” is described through a `(Z/2Z)`-gerbe and a connected groupoid with that fundamental group. A proof would construct this groupoid of choices explicitly and identify its automorphisms, then show how choosing an object supplies the stronger exterior-group datum sought in the preceding sentence (Grothendieck, 1981, scans 47–48).

### R20 — Scan 48, paragraph surrounding (70)

**Kind: conjecture / authorial expectation.** The qualification “il me semble” accompanies the assertion that the conceptual reflections prove a canonical isomorphism, with the parenthetical restriction read as “au moins mod autom intérieurs.” A fuller redaction should establish functoriality and state the residual inner ambiguity precisely; the right marginal qualification also needs its uncertain superscript resolved (Grothendieck, 1981, scan 48).

### R21 — Scan 48, after (70)

**Kind: unproved claim.** “Tout à fait indépendant, me semble-t-il” distinguishes the conceptual assertion from the claim that the displayed natural homomorphism to `Gl(2,Z)` is an isomorphism. To verify independence, one would audit the construction for hidden use of that identification or of a chosen identification of the two fundamental groups (Grothendieck, 1981, scan 48).

### R22 — Scan 48, closing paragraph; scan 49, opening

**Kind: unpursued implication.** The warning “plus sujet à caution” concerns identifying the target of (70) with the central quotient, while the next page permits that only “comme groupe extérieur.” This distinction suggests tracking the information lost when an actual homomorphism is replaced by its class up to inner automorphism, especially when composing such identifications (Grothendieck, 1981, scans 48–49).

### R23 — Scan 49, diagonal marginal note

**Kind: conjecture / authorial proposal.** “On pourrait inclure” introduces the suggested inclusion of complex conjugation so that (73) need not be restricted to the positive subgroups. To carry out the proposal, one would extend both the analytic construction and its group actions, then check compatibility with the involutions; several connecting words and the final abbreviation remain doubtful (Grothendieck, 1981, scan 49).

### R24 — Scan 49, (71)–(72)

**Kind: unproved claim.** A “morphisme canonique” of analytic modular objects is said to induce an isomorphism. Its construction, the significance of the primes, and its effect on the indicated fundamental groups require verification; the overwritten first target of (71) must be settled from the manuscript rather than silently reconciled with (72) (Grothendieck, 1981, scan 49).

### R25 — Scan 49, (73) and the following question

**Kind: conjecture / authorial question.** “Est-il possible de le préciser de façon utile, en un hom effectif, non seulement extérieur?” explicitly asks for a stronger version of the induced homomorphism. The proposed use of a canonical universal covering on the next lines should be checked for which choices it removes and which choices remain (Grothendieck, 1981, scan 49).

### R26 — Scan 50, (74)

**Kind: unproved claim.** The isomorphism is described as “pas seulement extérieur” and compared with (50) after restriction to an index-two subgroup. The proof obligations are to explain what the chosen universal-cover description fixes and to check the comparison with the earlier formula, which is outside the supplied excerpt (Grothendieck, 1981, scan 50).

### R27 — Scan 50, (75)–(76)

**Kind: unproved claim.** The “hom canonique” from `D` is asserted to be compatible with the displayed operator-group homomorphism. A verification would construct the map, prove the stated equivariance, and then establish the following universal-cover and mixed-fundamental-group identifications; the target group glyph is left explicitly doubtful in the transcription (Grothendieck, 1981, scan 50).

### R28 — Scan 50, annotation under (76)

**Kind: unproved claim / deferred reference.** The note says the isomorphism “est explicité dans” and leaves section/page references unfilled. The missing reference is an editorial task for comparison with the rest of the manuscript, not a number to be guessed or inserted here (Grothendieck, 1981, scan 50).

### R29 — Scan 50, final sentence

**Kind: unpursued implication.** “Pour pouvoir l’identifier” introduces an identification with a fundamental group at a written basepoint, but the excerpt stops at “il.” The next leaf should be checked for the required lift, path, or other datum and for how it interacts with the preceding canonicity claim; even the bar on the basepoint letter remains a marked reading issue (Grothendieck, 1981, scan 50).

### R30 — Scans 47–50, choice groupoid versus effective homomorphism

**Kind: own idea.** Formulate the groupoid of kernel choices and the groupoid of choices giving an effective version of (73), then test whether the construction supplies a functor between them or leaves an additional obstruction. **Confidence: medium**, because the manuscript explicitly juxtaposes a gerbe of kernel choices with the later effective-homomorphism question, but it does not identify those two choice problems on these pages.

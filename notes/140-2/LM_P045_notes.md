# LM_P045 — Transcription apparatus and research notes

## 1. Source, numbering, and editorial conventions

The transcription follows the ten supplied image files, `LM_P045_scan441.jpg` through `LM_P045_scan450.jpg`, in filename order. The filenames and task instruction determine the `\scanpage` values. The lower page labels, also repeated in the printed archive footers, run from 440 to 449: they are one less than the filename scan numbers. The upper handwritten manuscript numbers are recorded separately with `\mspage` only where visible. No absent manuscript page number has been supplied.

| Transcription scan / filename suffix | Visible lower label and archive footer | Visible upper manuscript page |
| --- | --- | --- |
| 441 | 440 | 223 |
| 442 | 441 | — |
| 443 | 442 | 224 |
| 444 | 443 | — |
| 445 | 444 | 225 |
| 446 | 445 | — |
| 447 | 446 | 226 |
| 448 | 447 | — |
| 449 | 448 | 227 |
| 450 | 449 | — |

The fragment begins and ends in continuation. Printed institutional footers and the repeated lower archive labels are not incorporated into the manuscript prose. Readable cancellations, interlinear replacements, marginal text, and the canceled duplicate diagram are retained. The diagonal correction on scan 444 is treated as an insertion continuing the main proof; the nonorientability note on scan 445 has no secure insertion anchor and remains a margin note.

All decipherment is based on the supplied images. External works cited in Section 5 are comparison resources for the research notes only; no published transcription or later mathematical formulation was used to supply manuscript words. Apparent mathematical inconsistencies remain in the transcription, including the repeated number (14), the superscript in the definition of Y on scan 446, the index statement on scan 447 without an inserted image operation, and the j/i mismatch in (20).

The `.tex` is a fragment without a preamble or macro definitions, as requested. It uses the specified editorial macros, ordinary LaTeX/AMS mathematical commands, and `tikz-cd`. A host document must define the editorial macros and load the relevant mathematical and diagram packages. Diagram (16) carries an overall doubt marker because of localized arrow and cancellation issues; its individual uncertainties are specified below.

## 2. Table of doubts

Line numbers are approximate handwritten lines counted from the top of the manuscript text, excluding page numbers. Displays, additions, and diagonal writing make an exact linear count inappropriate in some places; those entries give a region or equation number instead. Repeated instances of the same doubtful symbol are sometimes grouped. Counts in `\illegible{n}` estimate words or short symbol clusters, not securely counted lexical units.

**Confidence:** **high** means the proposed reading is strongly supported but a stated detail remains doubtful; **medium** means a material alternative or incomplete letter pattern remains; **low** means the reading or its placement is weak, or the text is unrecoverable. These are qualitative editorial assessments, not measured error probabilities.

### Scan 441

| Approximate line / region | Reading in the transcription | Alternatives or reason for doubt | Confidence |
| --- | --- | --- | --- |
| 1 | `compatibles` | Ending is lightly traced. | high |
| 2 | `définie` | Middle and ending are compressed. | medium |
| 2 | `\widetilde U\longrightarrow U` | The connecting stroke may be an unheaded dash. | low |
| 3 | `autom.` | The abbreviated word after l’ is faint. | medium |
| 4, deleted word | `Pour` | Puis | low |
| 5 | `fermée` | Final letters are compressed. | high |
| 8, deletion | `éléments` | Strike-through crosses the middle and final letters. | medium |
| 8, above-line replacement | `scindages` | Several medial letters merge; the earlier provisional reading sous-groupes was rejected on visual rereading. | medium |
| 11, overwritten label | `4 or 5` | The earlier equation number is obscured; the separate retained (5) is readable. | low |
| 11 and 18, equations (5) and (6) | `Sc` | Se; the second letter lacks a securely distinguishable cross-stroke. | medium |
| 12, definition after (5) | `scindages` | Medial letters are lightly written. | medium |
| 13, definition after (5) | `sur` | The short word before Z/2 is reduced to connected strokes. | medium |
| 20, deleted noun | `scindage` | Partially obscured by the horizontal strike-through. | medium |
| 20, deleted words replaced by d’ | `tel q’` | The final character may be an unfinished word rather than an apostrophe. | low |
| 21, after Alors | `\illegible{2}` | Two short canceled clusters; they may be symbols rather than lexical words. | low |
| 22, equation (7) | `sss` | ssi; the final stroke is not unambiguously dotted. | medium |
| 22, after equation (7) | `\illegible{1}` | Canceled short word or symbol after the comma. | low |
| 23, deletion above the circular case | `\illegible{4} Z_i` | Heavy hatching obscures approximately four words/symbols, but the final Z_i remains readable and is retained. | low |
| 23 | `S^1` | Blackboard-bold S^1; a second stroke may belong to the letter or to the correction above. | medium |

### Scan 442

| Approximate line / region | Reading in the transcription | Alternatives or reason for doubt | Confidence |
| --- | --- | --- | --- |
| 2 | `défini` | The compressed ending is not fully resolved. | medium |
| 6 | `remplacer` | Several middle letters run together. | medium |
| 7–8, display | `(9)` | Overwritten number; underlying form may be (8). | medium |
| 10, deleted word | `prenant` | Could not resolve the heavily retraced middle letters. | low |
| 10, above-line insertion | `can.` | can without a visible full stop | medium |
| 11, argument of the universal-cover symbol | `x` | The argument has been retraced or overwritten. | medium |
| 11 | `ponctué` | pointé is a possible misleading reading; the longer form seems supported by the ink. | medium |
| 13 | `correspondantes` | The ending is compressed. | medium |
| 13 | `déduites` | The first letters are weak; do not use the mathematical construction to resolve them. | medium |
| 15, deleted word | `seules` | Struck-through letters remain only partly legible. | low |
| 15, below σ′ | `illegible deleted notation` | One overwritten item, apparently a former subscript or annotation. | low |
| 15 | `obtenues` | The ending is a short joined stroke. | medium |
| 16, before the fixed-locus expression | `illegible deleted item` | One short overwritten item. | low |
| 19 | `élts` | élémts; abbreviation and its exact ending remain uncertain. | low |

### Scan 443

| Approximate line / region | Reading in the transcription | Alternatives or reason for doubt | Confidence |
| --- | --- | --- | --- |
| 3 | `prouvera` | The last syllable is compressed. | medium |
| 4, before π₀(U^σ) | `le, deleted` | The canceled short word is unclear. | low |
| 5, parenthesis | `avec` | The opening token is not securely legible. | low |
| 5, parenthesis | `triviale` | The word is not secure; no correction to trivialité has been made. | low |
| 5, parenthesis | `ses` | ttes; the token has two tall initial strokes. | low |
| 7 | `revêtᵗ` | revêtement; possible raised final t. | medium |
| 8 | `correspondant` | The final letters are very compressed. | medium |
| 10–11, diagram number | `(8)` | Number overwritten or retraced. | low |
| 13 | `trivialᵗ` | The final t appears raised; abbreviation for trivialement is likely. | medium |
| 18, canceled paragraph | `simpleᵗ` | simplement; exact abbreviation uncertain. | medium |
| 20, canceled paragraph | `une` | The opening is traversed by the cancellation stroke. | low |
| 18–19, interlinear rewrite | `l’image, deleted and rewritten` | The lower canceled word is thickly overwritten; the upper l’image is clearer. | low |
| 18–19, interlinear rewrite | `induit, deleted` | The beginning is partly obscured. | medium |
| 20, interlinear rewrite | `Ũ_i` | Ũ; the subscript is weak. | low |
| 21, interlinear rewrite | `revêtᵗˢ` | revêtements; possible raised abbreviated ending. | medium |

### Scan 444

| Approximate line / region | Reading in the transcription | Alternatives or reason for doubt | Confidence |
| --- | --- | --- | --- |
| 1 | `fortiori` | A preceding a may be obscured by the marginal addition; it has not been supplied in the text. | medium |
| 3 | `égal` | The accent and first letter are weak. | medium |
| 2–3, inserted map | `Ũ_i^{σ_i}` | Ũ^{σ_i}; the subscript i below U is not clearly distinguishable. | medium |
| 2–3, end of insertion before the diagonal margin continuation | `fait de` | The thick terminal strokes can resemble cancellation; reading remains uncertain. | medium |
| diagonal marginal insertion | `simpleᵗ` | simplement | medium |
| diagonal marginal insertion | `finalᵗ` | finalement | medium |
| 5, main text | `simpleᵗ` | simplement | medium |
| 8 | `homéom.` | The abbreviated ending and accent are weak. | medium |
| 10, deleted phrase | `les élts` | The last letters are obscured by the cancellation. | low |
| 11, deleted item | `illegible deleted word` | One word before the inserted les élém. | low |
| 11, insertion | `les élém.` | les élts; exact abbreviation and punctuation uncertain. | low |
| 17, canceled wording | `désignant` | The beginning and ending cross the deletion stroke. | medium |
| 17, insertion | `simpleᵗ` | simplement | medium |
| 18, formula (12), under the isomorphism sign | `f` | A small f-like mark is explicit but its identity is insecure; it has not been omitted. | low |
| 19 | `can.` | The final letters are compressed. | medium |

### Scan 445

| Approximate line / region | Reading in the transcription | Alternatives or reason for doubt | Confidence |
| --- | --- | --- | --- |
| 1, 3 | `g_i with exponent 0` | small letter o or circle; tiny round character does not distinguish these securely | medium |
| 3–4, 7, 10, 12, 14 | `π_i; π_1(U)` | Π_i; Π_1(U); handwritten capital/lowercase pi forms are not securely differentiated | medium |
| 5 | `indices` | word ending not secure; no distinct alternative retained | medium |
| 5 | `n'y parle` | tense and final letter of parle are not fully distinct | medium |
| 7 | `opérant` | ending compressed; opérant is probable | medium |
| 7 | `trivial with raised t` | a compressed full form trivialement is possible; abbreviation retained as tentative | medium |
| 8 | `transport` | some medial letters are reduced to strokes | medium |
| 16 | `deleted donc` | one canceled word; only initial d and remaining low strokes are distinguishable | low |
| 18 | `calligraphic T_g` | Γ_g; script alphabet uncertain | medium |
| margin beside Corollaire 1 | `et X_g/σ non orientable....` | the words non orientable are probable; no caret securely places this as an insertion into a specific sentence | medium |

### Scan 446

| Approximate line / region | Reading in the transcription | Alternatives or reason for doubt | Confidence |
| --- | --- | --- | --- |
| 4 | `calligraphic T_g` | Γ_g | medium |
| 4 | `one illegible deleted word before ellipsis` | heavy diagonal cancellation obscures the letters | low |
| 5 | `Aut subscript loc` | subscript letters compressed; loc is tentative | medium |
| 6 | `deleted Π_g` | symbol heavily overwritten after alors | low |
| 7, display (14) | `u_i as exponent of Π_g` | overwriting obscures the preceding state of the exponent | medium |
| 8, deleted text | `satisfont tous deux anti-` | first word especially uncertain; all three initial words are partly covered by the cancellation | low |
| 9 | `h in the existential statement` | overwritten letter; later h supports but does not remove the local doubt | medium |
| 11 | `Nécessairement` | ending reduced to a stroke; no alternative retained | medium |
| 11–12 | `calligraphic T_g and its plus form` | Γ_g; the same alphabet ambiguity affects the fixed subgroup and Centr subscript | medium |
| 16 | `Y subscript g,i` | first subscript is overwritten; g,i is the visible probable reading | medium |

### Scan 447

| Approximate line / region | Reading in the transcription | Alternatives or reason for doubt | Confidence |
| --- | --- | --- | --- |
| 1 | `de l' followed by a deleted Y` | d' followed by the deletion; boundaries of the correction are unclear | low |
| 2 | `π_0(∂Y)` | Π_0(∂Y); handwritten case uncertain | medium |
| 2 | `remontant` | medial strokes are compressed | medium |
| 4 | `two illegible canceled words` | the cancellation between the fixed-component set and qu'on peut interpréter obscures the text | low |
| 5 | `ainsi` | aussi | low |
| 5 | `l'ens` | abbreviation and final s uncertain; not expanded in the transcription | medium |
| 7 | `calligraphic T_g^+` | calligraphic G_g^+; this particular group letter is overwritten | low |
| 8 | `relevant` | relèvement | medium |
| 9 | `Π-conjugué` | π-conjugué; no g subscript is visible here | medium |
| 13 | `posant` | ending compressed; no distinct alternative retained | medium |
| diagram (16) | `two rows 1→T→G→script-T; T vertical equality; the other vertical arrows descend` | main topology is relatively clear; exact arrowhead form on the short horizontal arrows and the apparent hook at the top of the right vertical arrow remain less secure | medium |
| diagram (16), upper third entry | `deleted Centr with calligraphic G_g subscript` | dense cancellation obscures parts of this superseded notation | low |
| diagram (16), lower third and fourth entries | `deleted plus signs before u_i and σ_i` | the blackened marks could be read as stars; their status as canceled plus signs is probable but not certain | medium |
| diagram (16), right of both rows | `one illegible canceled tail per row` | possibly arrows and terminal 1s, but not restored in the transcription | low |
| diagram (16), line 17, line 21 | `calligraphic T_g / calligraphic T` | Γ_g / Γ | medium |
| 20 | `l [deleted es] 'assertion` | overwriting may concern the whole article les; singular ending of assertion is not fully distinct | low |
| 21, deleted ending and canceled interlinear text | `qui followed by estimated three illegible words and one illegible interlinear word` | word counts approximate; the final canceled clause cannot be reconstructed reliably | low |

### Scan 448

| Approximate line / region | Reading in the transcription | Alternatives or reason for doubt | Confidence |
| --- | --- | --- | --- |
| ~2, cancelled first proof | `\dot\gamma; u_i\prime` | The overwritten first symbol and placement of the prime/subscript are not fully resolved. | low |
| ~3, cancelled first proof | `\mathcal{G}_g^{+u_i}` | \mathcal{G}_g^{+}; the extra superscript is crossed or overwritten. | low |
| ~4, start of cancelled equation | `\deleted{\illegible{1}}` | One cancelled word or operator before u_i′ cannot be read. | low |
| ~4–5, cancelled first proof | `h\gamma (twice)` | The factors are uncertain; no inverse or changed order has been supplied from the argument. | low |
| ~5, cancelled fragment after membership sign | `\illegible{1}` | The object after the membership sign is not recoverable. | low |
| ~7, live paragraph | `d’autre part` | Final t of part is uncertain; d’autre par is possible. | medium |
| ~9, live paragraph, small cancellation | `il existe` | The cancelled phrase is partly covered by its ruling. | medium |
| between ~13 and 14, right side | `comme` | A small isolated cancelled word; reading and attachment are uncertain. | low |
| ~15, interlinear addition in cancelled Corollaire 3 | `\deleted{\illegible{1}}` | One word preceding 0-conn. has been overwritten. | low |
| ~15, same addition | `0-conn.; homéom.` | The initial numeral and the abbreviation endings are not entirely secure. | medium |
| ~16, cancelled Corollaire 3 | `\deleted{\illegible{1}} before \Pi` | One overwritten symbol or word after Pour que is undeciphered. | low |
| ~17, cancelled Corollaire 3 | `f et s.` | Possibly f. et s.; the exact abbreviation and punctuation are uncertain. | medium |
| ~18–19, inserted condition in cancelled Corollaire 3 | `comp. \illegible{2} \unsure{compacte}` | The words between comp. and the possible compacte are obscured; no topological condition has been reconstructed. | low |
| ~20, before Les éléments | `\deleted{\illegible{1}}` | A short cancelled word is unreadable. | low |
| ~20, separate cancellation below/right of Les éléments de torsion de | `quand U \illegible{2} orientable` | U and the ending orientable are partly visible; quand and the two intervening words remain doubtful. | low |
| ~21, after Pi in cancelled Corollaire 3 | `comme` | The cancelled word might be another short connective. | low |
| ~23, last line of cancelled Corollaire 3 | `qui correspondent à des comp. non compactes` | The handwritten expansion or abbreviation of correspondent and the final condition are partly obscured; the whole phrase remains doubtful. | low |

### Scan 449

| Approximate line / region | Reading in the transcription | Alternatives or reason for doubt | Confidence |
| --- | --- | --- | --- |
| ~5 | `\mathcal{T}_g^{\prime\prime}` | \mathcal{T}_g^\sharp; the small superscript is not resolved. | low |
| ~5, after près | `..` | Possibly an ellipsis of three points; punctuation is faint. | low |
| ~7 | `recette` | The word has the visible shape of recette, but the middle letters are rapid. | medium |
| ~9 | `doublement` | Possibly dédoublement; the opening strokes are not completely resolved. | medium |
| ~10, first surface subscript | `deleted 2 in g−2i,i` | A cancelled numeral before i is visible but not certainly 2. | low |
| ~10 | `donc en partant` | The short words and ending of partant are compressed. | medium |
| ~11, before plan | `\deleted{\illegible{1}}` | One cancelled symbol or word is unreadable. | low |
| ~11, subscript of Y_0 | `\deleted{\illegible{1}}` | An earlier subscript is heavily overwritten underneath the visible 0. | low |
| ~11, tiny cancellation below projectif | `D_0` | Possibly Y_0 or another symbol; no insertion pointer is visible, so the attachment is uncertain. | low |
| ~12, above rebouche | `\inserted{\deleted{\illegible{1}}}` | An abandoned interlinear word is unreadable; its relation to rebouche is inferred from position only. | low |
| ~13 | `g-i` | The small minus is weak; the expression is retained as a doubtful reading. | medium |
| ~16 | `correspondants` | The final letters are a short stroke; correspondantes or an uninflected ending is not excluded. | medium |
| ~17, immediately before equation (17) | `Alors` | Heavily overwritten or cancelled short word. | low |
| ~17, equation (17) | `V_{0,g}` | V_{0,j}; the second subscript has a dotted/looped shape. | medium |
| ~20, before the boundary formula | `en les points` | The first short words could be read differently. | medium |
| ~20, lower bound of union | `g-i+1\le j\le g` | The 1 after + is a narrow stroke, and the first inequality is less clear than the second. | medium |
| ~21, final line | `revêt` | The accent and compressed middle strokes are not fully distinct. | medium |

### Scan 450

| Approximate line / region | Reading in the transcription | Alternatives or reason for doubt | Confidence |
| --- | --- | --- | --- |
| ~1, after U_0 | `\deleted{\illegible{1}}` | One crossed-out provisional name cannot be read. | low |
| ~1, restriction target | `\bigcup D_j` | The apparent target differs from the preceding V_0; it has not been corrected to make the construction consistent. | low |
| ~3, equation (18), before U_0 | `\deleted{\illegible{1}}` | A separate cancelled name or short word lies to the left of the surviving expression. | low |
| ~3, equation (18), after U_0 | `\deleted{\illegible{1}}` | A second overwritten provisional name is unreadable. | low |
| ~4, after the numeral 2 | `deleted g` | The small crossed character below/right of 2 may be g. | low |
| ~5–6, two-element set, repeated | `\varepsilon_j` | \mathcal{E}_j; the handwritten alphabet is uncertain. | medium |
| ~8, after D_j | `...` | The number of points is not entirely secure. | low |
| ~8, cancelled clause | `On construit` | The verb is partly covered by a cancellation line. | medium |
| ~8, cancelled clause after construit | `\illegible{1}` | The object or name before de sorte que is overwritten. | low |
| ~8, above the cancelled clause, after Soit | `\deleted{\illegible{1}}` | A cancelled interlinear name is unreadable; its precise relation to the following M_j is uncertain. | low |
| ~9, before surviving M_j | `\deleted{\illegible{1}}` | Another heavily overwritten name is visible before M_j. | low |
| ~10 | `est recollé` | Possibly se recolle; first word and final accent are not completely resolved. | medium |
| ~12, before equation (20) | `soit` | Possibly sur; the short word is very cursive. | low |
| ~13, equation (20) | `M_i under a coproduct indexed by j` | The visible short dotted suffix looks i, unlike the long j elsewhere; it is preserved and not emended to M_j. | high |
| ~15, equation (21) | `g-i` | Possibly g+i; the operator is thickened or blotted. | low |
| ~17, target of the first cancelled map | `X_{g-i,i}` | Y_{g-i,i}; the initial letter and part of the subscript are overwritten. | low |
| ~22, resumed live paragraph | `doublement` | Possibly dédoublement; the beginning of the word is overwritten. | medium |
| ~23 | `défini` | The ending is a short stroke; défini / défini(e) cannot be resolved solely from the ink. | medium |
| ~24, cancellation after dedans | `X_g, followed by \illegible{4}` | A crossed symbol may be X_g; the adjacent cancelled words are not securely readable. | low |
| ~25, cancellation after the inserted revêtement phrase | `\deleted{\illegible{3}}` | Approximately three cancelled words are covered by a strong horizontal stroke. | low |
| ~26, last equation number | `22` | Possibly 21; the second digit is ambiguous. | medium |
| ~26, before surviving X_{g,i} | `\deleted{\illegible{1}}` | One earlier notation has been completely crossed out. | low |

## 3. Abbreviations and compact notations met

Expansions below are editorial proposals only. The transcription does not expand them. Differences in punctuation are retained, and uncertain abbreviated endings are identified. `int` and `Int` have different apparent uses here.

| Form as read | Proposed expansion or use |
| --- | --- |
| `autom.` | automorphisme(s) |
| `top.` | topologique(s) |
| `dim` | dimension |
| `ens.` | ensemble |
| `conj.` | conjugaison; conjugaison (in « à conj. près ») |
| `comp. conn.` | composante connexe |
| `sss [or ssi]` | si et seulement si; the last handwritten letter is uncertain |
| `i.e.` | id est |
| `Sc [or Se]` | Probably the set of scindages modulo the stated conjugacy relation; this is a notation gloss, not an expansion inserted into the text. |
| `hom` | homomorphisme |
| `Dém` | Démonstration |
| `can.` | canonique |
| `rev.` | revêtement |
| `op.` | opération(s) |
| `iso` | isomorphismes |
| `l’ens` | l’ensemble |
| `élts / élémts / élém.` | éléments; the exact abbreviated forms are uncertain |
| `comp.` | composante; composante, tentatively in the cancelled boundary condition |
| `ttes` | toutes, if that reading of the disputed parenthesis is correct |
| `revêtᵗ / revêtᵗˢ` | revêtement / revêtements; uncertain abbreviated endings |
| `trivialᵗ` | trivialement |
| `simpleᵗ` | simplement; abbreviation versus full word uncertain |
| `finalᵗ` | finalement; abbreviation versus full word uncertain |
| `homéom.` | homéomorphisme; homéomorphe or homéomorphisme, according to context |
| `$\overline{\mathrm m}$` | même |
| `Im` | image |
| `Aut` | automorphismes |
| `trivial with raised t (tentative)` | trivialement |
| `cqfd.` | ce qu'il fallait démontrer; ce qu’il fallait démontrer |
| `card` | cardinal |
| `loc (tentative subscript)` | possibly local / locaux; expansion is not secure |
| `int` | automorphisme intérieur, or conjugation by the indicated element; automorphisme intérieur / conjugaison, in int(γ)u_i |
| `NB` | nota bene |
| `Centr` | centralisateur |
| `autom` | automorphismes |
| `ens (tentative)` | ensemble |
| `ens` | ensemble (no full stop is evident in these occurrences) |
| `Int` | intérieur, in the surface formulas; distinct from the preceding group-theoretic int |
| `0-conn.` | 0-connexe; reading occurs in a cancelled interlinear condition and is uncertain |
| `f et s.` | faut et suffit, tentatively; abbreviation is doubtful and belongs to the cancelled Corollaire 3 |
| `corr.` | correspondance |
| `appl.` | application |

## 4. Legibility and limits of the transcription

The continuous prose and most large formulas are moderately legible after enlargement. Compressed endings and abbreviations still account for many doubt markers. The weakest material is the parenthesis on scan 443, the interleaved cancellation and replacement at its foot, the diagonal correction on scan 444, the overwritten group symbols and diagram tails on scan 447, the wholly canceled Corollaire 3 on scan 448, and the provisional definitions and indices on scan 450. The early canceled clusters around (7) are also poorly recoverable.

Greater confidence attaches to the visible paragraph order, the principal displayed maps, and the distinction between retained and wholesale canceled passages than to every individual word or symbol in those difficult areas. The circular generator exponent, some π/Π and script-letter distinctions, several equation numbers, and the sign in the surface subscript in (21) remain unresolved. Canceled material has not been promoted to an accepted assertion. The fragment preserves the readable content of deletions, including a final Z_i inside the heavily hatched clause on scan 441; unreadable stretches are explicit estimates.

## 5. Research notes — separate from the transcription

These notes concern only what is stated, invoked, or suggested in the supplied extract. “Unproved claim” includes a step invoked without a proof here; it does not mean that the full manuscript or the literature lacks a proof. Several arguments are completed later within these same ten images, and the notes identify that where relevant. A wholly canceled claim is discussed as a discarded formulation. Brief quotations are finding aids; uncertain details remain governed by the diplomatic transcription and the doubt table.

No securely readable explicit mathematical conjecture is identified in the surviving text of this extract. The author’s wish to construct a simultaneous geometric figure on scan 449 is recorded under the requested conjecture/expectation category, with its status as a construction aim stated explicitly. “Own idea” marks an editorial proposal for further investigation; none is asserted to be established or new. Manuscript locations below refer to Grothendieck (1981), using the filename-based scan numbers in Section 1.

### R01. Scan 441 — 5–6, a)

**Kind:** unproved claim.

**Manuscript cue:** « (Pour mémoire) ... sous-variété fermée ... de dim 1 ».

The fixed-locus assertion is recalled without a proof on this page. Checking it requires the hypotheses on U and its involution from the preceding pages, plus the appropriate local fixed-point model; these ten supplied images do not contain the beginning of the theorem.

### R02. Scan 441 — 8–18, b), equations (5)–(6)

**Kind:** own idea.

**Manuscript cue:** « Cette application se factorise en une bijection ».

Compare the component-to-splitting map with the cocycle description of splittings of a group extension by Z/2. This comparison would require a fixed choice of one splitting and careful tracking of the conjugation convention; it is an interpretive direction, not an additional formula attributed to the manuscript. The subsequent supplied pages contain the manuscript's geometric argument for the displayed bijection.

**Confidence:** medium. **Reason:** The page visibly identifies conjugacy classes of splittings with order-two elements outside the kernel, but does not introduce cocycles or choose a reference splitting here.

### R03. Scan 441 — 19–24, c)–d)

**Kind:** unpursued implication.

**Manuscript cue:** « π^{σ_i}={1} ... Z_i≃R ».

The asserted contrast between the line and circle cases suggests that fixed subgroups can detect the compactness of individual fixed components. Before using this as a reconstruction statement, one must verify the ambient hypotheses, the converse in (7), and the conjugacy choices in d), whose statement continues onto scan442.

### R04. Scan 442 — 6–8

**Kind:** unpursued implication.

**Manuscript cue:** « quitte à remplacer g_i par un conjugué ».

The conjugacy qualification suggests isolating a formulation independent of the selected representative and basepoint. The comparison between the geometric component and the fixed subgroup should keep track of which lift of the involution is being used.

### R05. Scan 442 — 21–22

**Kind:** unproved claim.

**Manuscript cue:** « Comme par le lemme … est non vide et connexe ».

This is a dependency on an invoked lemma, not a claim that the full manuscript lacks a proof. Before transferring the classification to another surface or involution, one should check exactly which hypotheses guarantee nonemptiness and connectedness of the fixed locus in the universal cover.

### R06. Scan 443 — 1–17

**Kind:** unpursued implication.

**Manuscript cue:** « l’application déduite (6) est bijective ».

The argument separates a connected-image statement from the stronger assertion that the image fills a fixed component. The latter uses the universal-cover construction on this page; any generalization should identify a replacement for that step rather than rely only on connectedness.

### R07. Scan 444 — top and diagonal marginal insertion, (10)

**Kind:** unproved claim.

**Manuscript cue:** « un rev. étale de son image ».

The marginal revision strengthens the canceled equality of images to an isomorphism from the universal cover of the component to the lifted fixed locus. The local covering assertion is compressed: a detailed verification should specify the local homeomorphism and explain the one-sheeted conclusion from simple connectedness of the target.

### R08. Scan 444 — (11)–(12)

**Kind:** own idea.

test the covering argument explicitly for a line component and for a circular component, retaining the chosen lifted involution throughout. This is a verification exercise that may clarify which step changes when the component ceases to be simply connected; it is not a claim of novelty.

**Confidence:** medium. **Reason:** The two cases are suggested by the manuscript’s contrast between the trivial fixed subgroup and the subsequent deck-transformation group T_i, but an explicit model has not been worked out here.

### R09. Scan 445 — 6–10

**Kind:** unproved claim.

**Manuscript cue:** « Il est clair ... commute à l'hom injectif ».

The equivariance needed to induce T_i→π_i^{σ_i} is asserted by appeal to transport of structure. A full check should specify the lifted involution on the chosen universal cover and verify that the map on deck groups is equivariant for exactly that choice; the subsequent surjectivity argument is present on this page.

### R10. Scan 445 — margin beside Corollaire 1

**Kind:** unpursued implication.

**Manuscript cue:** « et X_g/σ non orientable.... ».

This marginal qualification may restrict the scope of Corollaire 1, but no caret securely locates its insertion in the statement. Any later use of the corollary should check whether nonorientability of the quotient is an explicit standing hypothesis; the note has not been silently incorporated into the theorem text.

### R11. Scan 446 — 1–4, together with scan 445 margin

**Kind:** own idea.

Compare involutions with the same number of fixed components but different orientability of the quotient, asking whether the conjugacy classes of lifts or the embedded cyclic fixed subgroups distinguish them. This is a proposed comparison, not a claim that such examples occur under all the present hypotheses.

**Confidence:** medium. **Reason:** Part (a) singles out the component count, whereas the margin records an additional topological qualification that the count alone may not encode.

### R12. Scan 446 — 16

**Kind:** own idea.

**Manuscript cue:** « Soit Y_{g,i}=X_g^{σ_i} ».

Check the literal superscript notation against the surrounding definitions before using this as an identification of spaces. The same paragraph calls Y a connected nonorientable surface with boundary, while the earlier superscript notation refers to a fixed locus; the transcription preserves the visible formula without deciding whether this is a slip or a local notational convention.

**Confidence:** high. **Reason:** The sigma is visibly superscripted and no quotient slash is visible, but the intended mathematical interpretation is not settled by this local reading.

### R13. Scan 446 — 18–19; continuing scan 447, lines 1–3

**Kind:** unproved claim.

**Manuscript cue:** « il est bien connu, et immédiat ».

Transitivity on boundary components is invoked for the automorphism group of the connected nonorientable surface, and then lifted to the pair (X_g,σ_i). A proof should construct homeomorphisms exchanging the required boundary circles and verify the permitted category and compatibility of their lifts with the involution.

### R14. Scan 447 — 7–11

**Kind:** unproved claim.

**Manuscript cue:** « quitte à modifier h ».

The passage from Π-conjugacy to equality in (15) is condensed into a modification of h. An explicit verification should write the inner conjugating element and check that multiplying the chosen lift by it preserves the required positive subgroup and the projected class commuting with σ_i.

### R15. Scan 447 — 17

**Kind:** own idea.

**Manuscript cue:** « l'indice de ... dans ... ».

The text literally describes an index of the automorphism centralizer in the outer centralizer, without the words 'image de'. Before formalizing Corollaire 2, distinguish that homomorphism from its image: the displayed kernel T suggests that the intended finite index concerns the image subgroup, but no such repair is inserted into the transcription.

**Confidence:** high. **Reason:** The diagram includes T as a kernel term, while the prose omits an explicit image operation; the note concerns interpretation rather than a correction to the ink.

### R16. Scan 447 — 18–20

**Kind:** unproved claim.

**Manuscript cue:** « inclusions de sous-groupes d'indice 2 ».

The reduction from the full groups to the positive subgroups uses an index-two assertion for both centralizers. A proof should identify the relevant orientation characters and exhibit elements in the nonpositive cosets; the involutions themselves are natural candidates once their orientation behavior is fixed.

### R17. Scan 447 — Corollaire 2, together with scan 445's range 0≤i≤g

**Kind:** own idea.

Audit the i=0 boundary case before treating the index formula as an unconditional statement. Corollaire 1(a) would provide no order-two lift in that case, so the parts that choose u_i, and hence the cyclic group T, should be read conditionally rather than as assigning a subgroup of index zero.

**Confidence:** high. **Reason:** The displayed range includes zero, whereas the later construction explicitly starts with a chosen lift u_i.

### R18. Scan 447 — diagram (16)

**Kind:** own idea.

For the image subgroup in the outer centralizer, determine its action on the cyclic kernel T and ask whether the resulting extension splits, beginning with i=1. This is a possible computation; the present pages do not exhibit a section or establish a splitting criterion.

**Confidence:** medium. **Reason:** Cyclicity of T and the proposed finite-index image give concrete extension data, but do not by themselves imply a splitting.

### R19. Scan 448 — ~5–13, live middle proof

**Kind:** own idea.

**Manuscript cue:** « le stabilisateur … est formé des … ».

isolate the elementwise calculation ending in α⁻¹γ belonging to the centralizer as a general lifting criterion for an extension of groups. A separate proof could clarify exactly which quotient action is used and which stabilizer classes lift to actual commuting automorphisms. This is a proposed reformulation for study, not a claim of novelty or a correction of the manuscript.

**Confidence:** high. **Reason:** The visible proof explicitly passes from equality modulo inner conjugacy to membership in an actual centralizer.

### R20. Scan 448 — ~14–23, wholly cancelled Corollaire 3

**Kind:** unproved claim.

**Manuscript cue:** « Les éléments de torsion … sont d’ordre 2 ».

This assertion belongs to a wholly cancelled and locally revised passage, not to an accepted corollary on these pages. Its intended hypotheses and even part of the boundary condition remain illegible. Assessing or proving the discarded formulation would require recovering the relevant meaning of Π and the earlier conventions; ordinary surface fundamental groups must not simply be substituted for that missing context.

### R21. Scan 449 — ~1–7

**Kind:** conjecture / authorial expectation (construction aim).

**Manuscript cue:** « J’ai envie de construire une figure ».

Construction aim or expectation, not a mathematical conjecture: Grothendieck wants one geometric figure to exhibit the topological anti-involutions giving the σ_i and the various associated u_i. He begins such a construction on this and the following page. The supplied pages do not by themselves complete the promised simultaneous description of all the associated automorphisms.

### R22. Scan 449 — ~7–14

**Kind:** unproved claim.

**Manuscript cue:** « Nous savons que … s’obtient en regardant … ».

The realization of σ_i through an oriented double of the indicated quotient surface is invoked as known, rather than proved here. A proof would need the precise meaning of the doubling construction, the admissible range of g and i, and the classification or existence statement being invoked. The overwritten surface subscript is a transcription issue and has not been repaired to support that interpretation.

### R23. Scan 449 — ~17–20

**Kind:** unpursued implication.

**Manuscript cue:** « contenue à la fois dans ».

The punctured projective-plane piece is described as lying in both Y_0 and the modified surface and as agreeing with the latter near the remaining boundary. This supplies a potential common domain for comparing the associated covers as the number of Möbius attachments varies. Such a comparison would still require explicit choices of embeddings and collar identifications; none is supplied in detail on this page.

### R24. Scan 450 — ~4–8

**Kind:** unproved claim.

**Manuscript cue:** « un rev. trivial à 2 feuillets ».

The trivial two-sheeted cover over each disk and the interpretation of its sheets as the two orientations of that disk are stated without a separate proof. A verification would check the restriction of the chosen cover to each disk and the compatibility of the sheet labels with the ambient orientation double. This is a local verification suggested by the text, not an assumption used to resolve the uncertain set symbol.

### R25. Scan 450 — ~13–15 and ~22–26

**Kind:** own idea.

test the displayed gluing construction for a few small admissible pairs (g,i), recording Euler characteristics and boundary-component counts before and after taking the double. Such checks could help locate the intended role of the blotted sign in equation (21) and the summation-index mismatch in equation (20), while leaving both diplomatic readings unchanged. The precise interpretation of “doublement orienté” must be fixed first.

**Confidence:** medium. **Reason:** The disk and Möbius-band pieces make a finite topological consistency check feasible, but some conventions and index readings are unresolved.

### R26. Scan 450 — ~16–21, cancelled block

**Kind:** unproved claim.

**Manuscript cue:** « On voit qu’on a une appl. continue ».

The proposed map from U_0 and the claimed induced homeomorphism on its interior are wholly cancelled. They should be treated as an abandoned formulation whose target notation is also partly overwritten. A proof or counterexample would require deciding which spaces were intended and how the boundary was to be identified; no such decision belongs in the transcription.

### R27. Scan 450 — ~22–26

**Kind:** own idea.

study whether deleting the interiors of the lifted Möbius-band pieces provides a common invariant subsurface on which the various involutions and their centralizers can be compared. The preimage description of the lifted pieces suggests this route, but the eventual comparison maps are not constructed in the supplied pages. This is only a possible continuation of the construction, not an established consequence asserted here.

**Confidence:** medium. **Reason:** The final surviving formula defines the complementary surface, whereas the promised simultaneous description of the automorphisms is still incomplete in this extract.

### R28. Scan 441–445 — component-to-splitting correspondence and the lifted fixed locus

**Kind:** own idea.

Compare the discrete covering-space argument with the hypotheses needed for a profinite analogue. Pál (2011) proves a topological section result for profinite fundamental groups of finite CW complexes under a finite-cover cohomology condition, with applications to real points and fixed points on complex curves. The correspondence in these manuscript pages motivates that comparison, but the discrete and profinite statements must not be identified without checking their separate assumptions.

**Confidence:** medium. **Reason:** The shared ingredients are fixed components, group actions, and classes of sections; completion introduces additional hypotheses that are not supplied by this local manuscript passage.

### R29. Scan 443–445 — universal-cover square, insertion (10), and the deck-group argument

**Kind:** own idea.

Organize a detailed verification of the covering steps around the lifting criterion, uniqueness of lifts, and the action of deck transformations on a fiber. Hatcher (2002, Section 1.3, especially Propositions 1.33–1.34 and the discussion on pp. 70–71) provides precise formulations for those ingredients. These tools can clarify the compressed steps, but they do not independently establish the manuscript’s invoked fixed-locus lemma.

**Confidence:** high. **Reason:** The proof visibly uses lifted maps and deck transformations; the remaining fixed-locus statement is a separate geometric input.

## 6. References

Grothendieck, A. (1981). *La Longue Marche à travers la théorie de Galois* (Cote 140-2; supplied files `LM_P045_scan441.jpg`–`LM_P045_scan450.jpg`; visible archive labels 440–449; upper manuscript numbers 223–227) [Unpublished handwritten manuscript, supplied digital facsimiles]. Université de Montpellier.

Hatcher, A. (2002). *Algebraic topology*. Cambridge University Press. [Author-hosted text](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf).

Pál, A. (2011). The real section conjecture and Smith’s fixed-point theorem for pro-spaces. *Journal of the London Mathematical Society, 83*(2), 353–367. [https://doi.org/10.1112/jlms/jdq075](https://doi.org/10.1112/jlms/jdq075). [Author’s preprint](https://arxiv.org/abs/0905.1205).

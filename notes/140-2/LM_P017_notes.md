# LM_P017 — editorial and research notes

## Scope and numbering

This delivery concerns the ten supplied JPEGs, `LM_P017_scan161.jpg` through `LM_P017_scan170.jpg`. The transcription is a LaTeX fragment, not an edited reconstruction or a translation. Identification of the manuscript and its date follows the accompanying task description; no published transcription or external literature was used to supply readings.

The images contain more than one numbering system. Both visible handwritten number series are recorded with `\mspage`, in their approximate positions; their hands and dates have not been authenticated. The printed archive footer and its institutional address are not treated as manuscript text.

| Scan | Handwritten number at top | Handwritten number at lower left / printed archive page |
|---|---:|---:|
| 161 | 80 | 160 |
| 162 | — | 161 |
| 163 | 81 | 162 |
| 164 | — | 163 |
| 165 | 82 | 164 |
| 166 | — | 165 |
| 167 | 83 | 166 |
| 168 | — | 167 |
| 169 | 84 | 168 |
| 170 | — | 169 |

Comments beginning `%` in the LaTeX file are editorial locators. Bracketed prose inside `\diagram{...}` describes visible diagrams where a clean TikZ rendering would conceal ambiguity; this prose is not attributed to Grothendieck. The transcription retains the unfinished opening and ending, unmatched textual brackets where visible, and uncertain or surprising notation rather than completing it from context.

## 1. Table of doubts

Confidence concerns the reading of the ink, not the truth of the mathematics. **High** means that the visible feature is relatively clear despite a possible interpretive issue; **medium** means a plausible but unconfirmed reading; **low** means that the reading or its attachment is particularly insecure. A dash in the alternatives column means that no sufficiently supported alternative was identified, not that the reading is certain. An illegible-word count is an estimate.

Line ranges are approximate locators for manuscript prose, not a new diplomatic line numbering. Within each range, the entries follow transcription order; the state labels identify deleted text, insertions, margins, or diagrams. Repeated entries are retained when the same uncertain notation appears at different places. TeX is shown literally in the reading column so that each entry can be located in the fragment.

| ID | Scan | Approximate line / location | Reading | Alternatives | Confidence |
|---|---:|---|---|---|---|
| D01 | 161 | ca. ll. 1–5 | [illegible: 2 estimated words] | — | low |
| D02 | 161 | ca. ll. 1–5 | `au` | — | low |
| D03 | 161 | ca. ll. 1–5; deleted | `le` | — | low |
| D04 | 161 | ca. ll. 1–5 | `intuition` | `intention` | medium |
| D05 | 161 | ca. ll. 1–5 | `calculatoire` | — | low |
| D06 | 161 | ca. ll. 1–5 | `plutôt` | — | low |
| D07 | 161 | ca. ll. 5–16; deleted, insertion | `néc$^t$.` | — | low |
| D08 | 161 | ca. ll. 5–16; deleted | `ouvert` | — | medium |
| D09 | 161 | ca. ll. 5–16; deleted, insertion | `déf.` | — | low |
| D10 | 161 | ca. ll. 5–16; deleted | `$B_U'$` | — | low |
| D11 | 161 | ca. ll. 5–16; deleted | `$B_U$` | — | low |
| D12 | 161 | ca. ll. 5–16; deleted, diagram | `\sim` | — | medium |
| D13 | 161 | ca. ll. 17–24; deleted | [illegible: 1 estimated word] | — | low |
| D14 | 161 | ca. ll. 17–24 | [illegible: 1 estimated word] | — | low |
| D15 | 161 | ca. ll. 17–24; deleted | [illegible: 2 estimated words] | — | low |
| D16 | 161 | ca. ll. 17–24 | `$S_{\text{ét}}$` | — | medium |
| D17 | 161 | ca. ll. 17–24 | `se reconstituer` | — | medium |
| D18 | 161 | ca. ll. 17–24 | `$B_{\pi_0 B_{D^*}}$` | — | low |
| D19 | 162 | ca. ll. 15–23; deleted | `D` | — | medium |
| D20 | 162 | ca. ll. 15–23 | `\rho_!` | `\rho_{i!}` | medium |
| D21 | 162 | ca. ll. 15–23; deleted | `et` | — | medium |
| D22 | 162 | ca. ll. 15–23; insertion | `$\Xi_i$ (ou` | — | low |
| D23 | 162 | ca. ll. 15–23; deleted | [illegible: 2 estimated words] | — | low |
| D24 | 163 | ca. ll. 1–3; diagram | `\Xi_i` | `\Pi_i` | medium |
| D25 | 163 | ca. ll. 1–3; diagram | `\Pi` | — | medium |
| D26 | 163 | ca. ll. 1–3; deleted | `et` | — | medium |
| D27 | 163 | ca. ll. 3–10 | `toposienne` | — | medium |
| D28 | 163 | ca. ll. 3–10; insertion | `posant` | — | medium |
| D29 | 163 | ca. ll. 3–10; insertion | `fét` | — | low |
| D30 | 163 | ca. ll. 3–10 | `\ldots\ comme envisagé` | — | low |
| D31 | 163 | ca. ll. 11–18 | `D_{X,U}` | `B_{X,U}` | medium |
| D32 | 163 | ca. ll. 11–18; deleted | [illegible: 2 estimated words] | — | low |
| D33 | 163 | ca. ll. 11–18; deleted | [illegible: 1 estimated word] | — | low |
| D34 | 164 | ca. ll. 1–5; deleted | `foncteurs` | — | medium |
| D35 | 164 | ca. ll. 1–5; deleted | [illegible: 1 estimated word] | — | low |
| D36 | 164 | ca. ll. 6–11 | `D_{X;S}` | `B_{X;S}` | medium |
| D37 | 164 | ca. ll. 6–11; deleted | `présent` | — | low |
| D38 | 164 | ca. ll. 12–18 | `ens.` | `en.` | low |
| D39 | 164 | ca. ll. 19–25 | `$(\simeq D_{\text{ét}})$` | — | medium |
| D40 | 165 | ca. ll. 1–2; margin, deleted | [illegible: 1 estimated word] | — | low |
| D41 | 165 | ca. ll. 1–2; margin | `trois` | — | medium |
| D42 | 165 | ca. ll. 1–2; margin | `des` | — | medium |
| D43 | 165 | ca. ll. 5–14; deleted | `to.` | — | low |
| D44 | 165 | ca. ll. 5–14 | `D^*=D-S` | `D^*\longrightarrow D-S` | medium |
| D45 | 165 | ca. ll. 15–16; deleted, diagram | `\rho_X` | — | medium |
| D46 | 165 | ca. ll. 15–16; deleted, diagram | [illegible: 2 estimated words] | — | low |
| D47 | 166 | upper diagram; diagram | `U` | — | medium |
| D48 | 166 | upper diagram; margin | `on a` | — | medium |
| D49 | 166 | ca. ll. 1–5; insertion | `ess$^t$.` | `strict.` | low |
| D50 | 166 | ca. ll. 6–12 | `\Pi_1` | — | medium |
| D51 | 166 | ca. ll. 6–12; insertion | `B_{\Pi_1 B_{X,S}}` | `B_{\Pi_1 B_{X;S}}` | medium |
| D52 | 166 | ca. ll. 6–12; diagram | `\Pi_1` | — | medium |
| D53 | 166 | ca. ll. 13–19 | `\Pi_1` | — | medium |
| D54 | 166 | ca. ll. 13–19 | `cependant` | `équivalent` | low |
| D55 | 166 | ca. ll. 13–19 | `\Pi_1` | — | medium |
| D56 | 166 | ca. ll. 13–19; insertion | `équiv.` | `égaux` | low |
| D57 | 167 | upper diagram; diagram | `\Pi_1` | — | medium |
| D58 | 167 | upper diagram; diagram | `\Pi_1` | — | medium |
| D59 | 167 | ca. ll. 1–4 | `le triangle` | `la diagonale` | low |
| D60 | 167 | ca. ll. 5–12; deleted | `est` | — | medium |
| D61 | 167 | ca. ll. 5–12 | `n'sont` | `sont` | low |
| D62 | 167 | ca. ll. 5–12; insertion | `(semi-` | — | low |
| D63 | 167 | ca. ll. 5–12 | `\Pi_1` | — | medium |
| D64 | 167 | ca. ll. 5–12 | `\Pi_1` | — | medium |
| D65 | 167 | ca. ll. 5–12 | [illegible: 1 estimated word] | — | low |
| D66 | 167 | ca. ll. 13–15; deleted | [illegible: 1 estimated word] | — | low |
| D67 | 168 | ca. ll. 1–2 | `induites` | `traduites` | low |
| D68 | 168 | ca. ll. 1–2 | `topos` | — | low |
| D69 | 168 | ca. ll. 3–11; deleted | `cependant` | — | medium |
| D70 | 168 | ca. ll. 12–15 | `tte` | — | medium |
| D71 | 168 | ca. ll. 16–22 | `\Pi_1` | — | medium |
| D72 | 168 | ca. ll. 16–22 | `calculatoire` | — | low |
| D73 | 169 | ca. l. 1; diagram | `\Xi_i` | `\mathcal E_i` | medium |
| D74 | 169 | ca. l. 1; diagram | `\Pi` | `\pi` | medium |
| D75 | 169 | ca. ll. 2–8 | `\Pi_1` | — | medium |
| D76 | 169 | ca. ll. 2–8 | `\Xi_i` | `\mathcal E_i` | medium |
| D77 | 169 | ca. ll. 9–16 | `sous-monde` | `sous-ensemble` | low |
| D78 | 169 | ca. ll. 9–16; deleted | `B_{\Pi_1(U\cup S_0)}` | — | medium |
| D79 | 169 | ca. ll. 9–16; insertion | `B_{U\cup S_1}` | `B_{U\cup S_0}` | medium |
| D80 | 170 | ca. ll. 1–2 | `S_1` | — | medium |
| D81 | 170 | ca. ll. 3–6; deleted | `de dessous` | — | low |
| D82 | 170 | ca. ll. 3–6; deleted | `la situation` | — | low |
| D83 | 170 | ca. ll. 3–6; deleted | `B_{S_0}` | — | medium |
| D84 | 170 | large central diagram; diagram | `B_{\Pi_1(U\cup S_0)}` | — | medium |
| D85 | 170 | large central diagram; diagram | `B_{\Pi_1(U\cup S)}` | — | medium |
| D86 | 170 | large central diagram; diagram, deleted | `B_{\Pi_1 X}` | — | medium |
| D87 | 170 | large central diagram; diagram | `'` | — | low |
| D88 | 170 | ca. ll. 7–9 | `B_{\Pi_1 U_1}` | — | medium |
| D89 | 170 | ca. ll. 7–9 | `B_{D_1^*}` | — | medium |
| D90 | 170 | ca. ll. 7–9; diagram | `\Pi_1` | — | medium |
| D91 | 170 | ca. ll. 10–15; deleted | `donc` | `dans` | medium |
| D92 | 170 | ca. ll. 10–15 | `\Pi_1` | — | medium |
| D93 | 170 | ca. ll. 10–15 | `corres-` | — | low |


### Additional layout and notation reservations

| Scan | Location | Visible feature / adopted treatment | Alternative or limitation | Confidence |
|---:|---|---|---|---|
| 161 | Middle cancelled passage | The block beginning “Donnons-nous” and ending with the amalgamation diagram is enclosed in `\deleted`. | The long cancellation strokes do not delimit every word unambiguously; the earlier short cancellation is retained inside the larger one. | medium |
| 161 | Lower cancelled diagram | The horizontal relation between `B_D` and `B_S` is rendered as a bidirectional relation, with its apparent equivalence mark doubtful. | The overlying cancellation stroke obscures the exact relation and the extent of the lower bracket. | low |
| 162 | “multigaloisiens” | Double underlining is retained. | One of the lower strokes may partly belong to the descender of the handwritten letter. | medium |
| 162 | Final paragraph | The opening square bracket and later closing parenthesis are retained as seen. | Their scope has not been repaired to produce balanced prose punctuation. | medium |
| 163 | First group diagram | The left oblique stroke is described rather than supplied with a definite arrowhead. | Its intended direction may be recoverable from context, but that is not a visual reading. | low |
| 163 | Interlinear bracket about sheaves on `X` | The explanation is attached to the newly written `B_{X;S}`. | Dense cancellation makes the exact order of the bracket and overwritten continuation insecure. | medium |
| 165 | Rotated marginal note | The margin was read after rotation of a crop; no new text was inferred from the main paragraph. | Its first overwritten words and the article before “inclusions” remain doubtful. | medium |
| 166 | Interlinear “Sauf erreur…” remark | “2-cartésiens” and the reference to the “2-cat. des topos” are legible. | The intervening qualification about commutativity is less secure. | medium |
| 166–169 | Repeated subscript before `X` or `D` | `\unsure{\Pi_1}` records heavily rewritten notation. | The strokes sometimes distinguish neither the original subscript nor the final chosen form. They have not been silently regularized throughout. | low |
| 167 | Bottom of the lower étale diagram | The visible horizontal arrow points from `X_{\text{ét}}` to `U_{\text{ét}}`; it is retained that way. | A mathematically expected opposite direction has not been substituted. This is a clear arrow-reading, not a claim that the diagram is correct. | high |
| 168 | First paragraph | The target of `X_{\text{ét}}\longrightarrow X` is transcribed simply as `X`. | No `B` or subscript is supplied to reconcile it with nearby constructions. | high |
| 169–170 | Component labels | The inserted `U\cup S_1` / `U\cup S_0` reading on scan 169 is left doubtful; scan 170 visibly uses `U\cup S_0` under an annotation `U_1`. | The indices should not be normalized across the two pages without rechecking the overwritten ink. | medium |
| 170 | Large central diagram | Faint or interrupted comparison strokes and overwritten object labels are described in brackets. | No clean arrowhead or isomorphism is supplied where the ink does not establish one. | low |
| 170 | Final line | The last word is retained as a doubtful fragment, `corres-`. | The supplied batch ends here; no completion or continuation has been supplied. | low |
| All | Letterforms | Plain `B`, `D`, and the marked alternatives for the group letters reproduce the readable forms without imposing a new notational system. | Long lower strokes of handwritten capital letters are not automatically treated as emphasis. The explicit underlining on scan 166 is distinguished from such strokes. | medium |

## 2. Abbreviations met

Expansions below are editorial interpretations only. They are not substitutions made in the transcription. Operators and subscript labels are included where an expansion may aid later checking.

| Form as transcribed | Probable expansion / function | Reservation |
|---|---|---|
| `p^t` | point | In “point de vue”; superscript form retained. |
| `appr.` | approche; possibly appréhension | The surrounding opening phrase on scan 161 is insecure. |
| `néc^t.` | nécessairement | Both the letters and the intended expansion are low-confidence. |
| `déf.` | définition / défini | The small note in the cancelled block is doubtful. |
| `n°` | numéro | The following reference number is not legible. |
| `dim` | dimension | Not expanded in the fragment. |
| `i.e.` | id est | Appears in explanatory clauses. |
| `Gal` | groupe de Galois | Operator, not a prose replacement. |
| `Aut` | automorphismes | Operator applied to chosen covering objects. |
| `Hom` | morphismes / homomorphismes | Meaning depends on the category in question. |
| `Ker` | noyau | Operator in the definition of `L_i`. |
| `Spec` | spectre | Operator on a field or a local ring. |
| `iso`, `iso.` | isomorphisme; isomorphismes; isomorphe | Grammatical function varies. |
| `rev.`, `rev` | revêtement; revêtements | Full stop is not imposed where absent. |
| `comp. conn.` | composantes connexes | In the paragraph about the chosen coverings. |
| `fét` | fini étale / étale fini | Provisional reading of a small insertion on scan 163. |
| `ét` | étale | Primarily a subscript label. |
| `loc.`, `loc` | localement | Full-stop variation retained. |
| `ens.` | ensembles | The reading on scan 164 is itself uncertain. |
| `Π-ens` | ensembles munis d'une action de `Π` | Occurs in cancelled text on scan 169. |
| `hyp.` | hypothèse | In the dimension qualification. |
| `pts` | points | In the two-point description of `D_i`. |
| `NB` | nota bene | Marginal note on scan 165. |
| `homom.` | homomorphisme | Used of the commutation morphism. |
| `hom` | homomorphisme | In “hom de diagrammes” on scan 170. |
| `ess.` | essentiellement | Do not replace it with strict equality or commutativity. |
| `ess^t.` / `strict.` | essentiellement / strictement | Competing readings of the interlinear qualification on scan 166. |
| `comm`, `comm.` | commutatif; commutativité | Several diagram annotations. |
| `2-cat.` | 2-catégorie | In the interlinear remark on scan 166. |
| `sup.` | supérieur; supérieure | Referent on scan 167 is doubtful. |
| `équiv.` | équivalent; équivalence | One possible reading of the correction on scan 166. |
| `tte` | toute | Provisional reading on scan 168. |
| `s-groupe` | sous-groupe | In the quotient formula. |
| `géom` | géométrique | The visible form is not expanded. |
| `can.` | canoniquement; canonique | In the final claim of equivalence. |
| `\overline{\mathrm m}` | même | Retained as a manuscript abbreviation, not as an equality sign. |

The doubtful cancelled `to.` and the incomplete final `corres-` have not been assigned confident expansions. They may be unfinished words rather than stable abbreviations.

## 3. Legibility and reliability

The main prose is substantially more legible than the opening continuation, interlinear revisions, and overwritten diagram labels. I trust the plainly written distinctions between gluing and commutative amalgamation, the explicit acyclicity reservation, and the main normal-generation wording more than the exact form of several subscripts. The first scan's cancelled passage, the lower part of scan 162, the bracketed insertion on scan 163, the margin of scan 165, and the large diagram on scan 170 require the most caution.

The fragment is not a certified reading. In particular, proposed words inside `\unsure` must not be quoted as settled text, and the bracketed diagram descriptions must not be mistaken for manuscript prose. No illegible passage was completed from a mathematical expectation. A syntax-only LaTeX check was performed with temporary definitions of the editorial macros; those definitions and the test output are not included, because the requested deliverable is a fragment without a preamble.

## 4. Research notes — separate from the transcription

These notes concern only what is present, qualified, cancelled, or left unexplained in the supplied scans. Quoted wording is kept short; uncertain readings are identified. “Unproved claim” means that a proof is not supplied in this batch, not that the claim is false or absent elsewhere in the manuscript. The items labelled **own idea** are proposals for investigation, not assertions of novelty or established results.

### R01 — Scan 161, middle cancelled passage | Unproved claim, cancelled

The words “On a une décomposition analogue” accompany the decompositions involving `B_{D^*}` and `B_D`, before a proposed amalgamation diagram; the whole passage is cancelled (Grothendieck, 1981, scan 161). A reconstruction of this abandoned attempt would have to identify the component-indexed decompositions and their compatibility with the relevant morphisms. Cancellation matters: this is evidence of a discarded stage of the argument, not an endorsed theorem to be incorporated into the later construction.

### R02 — Scan 162, opening paragraph | Unpursued implication

The instruction to “tenir compte des corps résiduels” follows the attempt to recover the closed-part datum from the component set (Grothendieck, 1981, scan 162). The excerpt therefore invites a comparison between keeping only `I` and keeping the residue-field Galois groups at its elements. Such a comparison should determine precisely which information the earlier set-indexed description loses, without assuming that the subsequent notation has already resolved every arithmetic issue.

### R03 — Scans 162–163, chosen coverings and group diagram | Unproved claim

The description “s'explicite par la donnée d'un groupe” and the condition “les σ_i surjectifs” assert a group-theoretic presentation after choices of covering objects and identifications (Grothendieck, 1981, scans 162–163). A proof needs to specify the status of the “rev. universels,” the category of groups involved, and how changing these choices changes the homomorphisms and their comparison data. The overwritten name of the middle group should not be settled by this mathematical reconstruction.

### R04 — Scan 163, base-field paragraph and first square | Unpursued implication

The paragraph beginning “Quand il y a un corps de base K” adds `B_e` and a “donnée de commutativité” to the diagram (Grothendieck, 1981, scan 163). A further question is whether each subsequent construction and comparison is meant to be made over this base topos, with its specified commutation datum retained. Checking that issue would separate the arithmetic compatibility from the underlying unbased construction; the excerpt does not carry out that check.

### R05 — Scans 163–164, recollement paragraph | Unproved claim

The construction via `σ_*ρ^*` is said to produce “un topos mixte” which is not generally multigaloisien (Grothendieck, 1981, scans 163–164). A proof should give the objects and morphisms of the glued category, establish the topos structure, and identify the four morphisms and the comparison transformation in the displayed square. It should also specify exactly what extra property would make this mixed topos multigaloisien; no criterion is supplied here.

### R06 — Scan 164, opening formula | Unpursued implication

The comparison is explicitly “pas un iso” but “un morphisme de foncteurs sans plus,” with the visible orientation `σ^*ψ^* → ρ^*φ^*` (Grothendieck, 1981, scan 164). Consequently, a proposed universal property has to retain a potentially noninvertible comparison transformation rather than replace the square by a commuting one. Identifying the corresponding category of cones and its permitted 2-cells is a separate mathematical task left implicit on these pages.

### R07 — Scan 164, dimension-one geometric model | Unproved claim

The identification `B_{D;S} ≃ D_ét` is asserted under the stated dimension hypothesis and followed by “D_i n'a que 2 pts” (Grothendieck, 1981, scan 164). A proof needs to relate the indicated henselian local schemes and their punctured parts to the particular sheaf categories used in the gluing. The two-point observation should be connected to that étale argument explicitly, and the statement should not be extended to higher dimension or to a different henselization convention without further work.

### R08 — Scan 165, middle paragraph and marginal note | Unproved claim

The text insists that the canonical morphism is `φ_D`, “et non de ψ_Dσ,” and relates `φ_D` to an inclusion of schemes (Grothendieck, 1981, scan 165). It also says that the other indicated composites do not generally correspond to scheme morphisms. The needed verification is an explicit comparison of these distinct topos morphisms and the geometric inclusions, preserving the noninvertible comparison rather than identifying the arrows because they share source and target.

### R09 — Scan 166, interlinear remark | Conjecture / qualified assertion

“Sauf erreur” qualifies the statement that the two squares are “2-cartésiens” in the “2-cat. des topos”; the intervening commutativity qualification is less legible (Grothendieck, 1981, scan 166). This is a particularly direct item to check: formulate the appropriate 2-pullback problem for each square and verify its universal property with the intended 2-cells. The nearby warning about the upper triangle must be retained in that formulation rather than removed to make the verification easier.

### R10 — Scan 166, passage to locally constant objects | Unproved claim

Passing to the objects described as “loc. constants” is said to yield a “somme amalgamée de topos,” with the lower object provisionally read as `B_{Π_1 X}` (Grothendieck, 1981, scan 166). A proof needs to identify the precise category of locally constant objects intended here and show the asserted universal property of this new square. In particular, the excerpt should not be silently restricted to finite locally constant objects merely to make a familiar formulation available.

### R11 — Scan 166, final paragraph | Unproved claim

Replacing `B_U` by `B_{D^*}` is said to give a classifying topos related to `B_S` by the displayed arrow, with “isom.” followed by a hard-to-read correction (Grothendieck, 1981, scan 166). The point to establish is whether restriction to the closed-part datum is an equivalence for the locally constant objects under consideration and how this equivalence is realized by that arrow. Exact isomorphism, equivalence, and a chosen identification should remain distinct until the correction and the construction have been checked.

### R12 — Scan 167, middle paragraph | Conjecture / explicit expectation

The two comparison maps have “une nette tendance d'être ‘acycliques’,” explained as inducing cohomological isomorphisms, followed by “il faudrait voir … ce point” (Grothendieck, 1981, scan 167). This is an expectation accompanied by a request for verification, not a theorem proved in the excerpt. A precise version must specify the coefficient objects, the degrees, and the sense of acyclicity, then prove it or exhibit the needed restrictions.

### R13 — Scan 168, first paragraph | Unproved claim with an external-to-the-batch reference

The geometric comparison morphisms have “moins de chances d'être acycliques,” but the text still invokes “des cas importants” recalled in an earlier section (Grothendieck, 1981, scan 168). The earlier section is not supplied, so these pages alone do not identify those cases or their hypotheses. The next research step is to locate that reference and compare its actual assumptions with the two maps written here, without supplying guessed examples as though they were Grothendieck's.

### R14 — Scan 168, formal-construction paragraph | Unproved claim

The constructions are described as “purement formelles” and independent of a further hypothesis, in a phrase containing the doubtful abbreviation `tte` (Grothendieck, 1981, scan 168). Their formal scope should be checked against the earlier standing conditions on `σ` and on the multigaloisien topoi, rather than interpreting this sentence as cancellation of those conditions. One must also distinguish formal existence of the glued or amalgamated object from the separate geometric and cohomological identifications.

### R15 — Scan 169, quotient paragraph | Unproved claim

The fundamental-group expression is said to be the quotient by the “s-groupe invariant engendré” by the `ρ_i(L_i)`, with `L_i = Ker σ_i` (Grothendieck, 1981, scan 169). A proof can be organized around the universal property of compatible homomorphisms out of the displayed group span, using the surjectivity conditions actually stated earlier. It also needs to determine the relevant group category and the meaning of generation there; the transcription does not add the word “fermé.”

### R16 — Scans 169–170, partial filling | Unpursued implication

The phrase “bouchage partiel de trous” accompanies the choice of `I_0`, the decomposition into `I_0` and `I_1`, and the geometric interpretation involving `U_1` (Grothendieck, 1981, scans 169–170). This suggests studying the entire family of constructions indexed by subsets of components, together with its transition maps, rather than a single filling. The overwritten `S_0` / `S_1` labels must be checked before attributing a precise indexing convention to the manuscript.

### R17 — Scan 170, final paragraph | Unproved claim

“Il est évident” introduces the assertion that the iterated amalgamation is “can. équivalente” to the previously obtained object (Grothendieck, 1981, scan 170). A proof should establish equivalence through the relevant universal properties and explain the claimed canonicity, not merely compare the abstract groups after making choices. Since the final sentence continues beyond the batch, its next clause or any following qualification is unavailable here.

### R18 — Scans 163–165 | Own idea: an elementary noninvertible-comparison test

Take the candidate input in which the three initial topoi are categories of sets and both initial morphisms are identities, then write out the proposed gluing data as two objects with a connecting map. A nonbijective connecting map offers a concrete test of the author's distinction between a comparison morphism and an isomorphism, once the variance conventions have been fixed. **Confidence: medium; reason:** the candidate is elementary, but identifying its exact relation to the manuscript's chosen gluing conventions is part of the test, not something assumed here.

### R19 — Scan 169 | Own idea: isolate the closure operation in the quotient

Investigate whether “invariant engendré” denotes algebraic normal generation, closed normal generation, or a closure operation belonging to a more specific category of groups. If a Hausdorff or profinite quotient is intended, the kernel must satisfy the appropriate closedness requirement, whereas the visible wording does not state it. **Confidence: high that this is a necessary clarification; reason:** the relevant group topology affects the quotient, and no choice of closure should be inserted into a diplomatic transcription.

### R20 — Scans 169–170 | Own idea: component-indexed quotient filtration

After fixing the group category, attach to a subset `J ⊂ I` the normal-generation datum formed from the `ρ_i(L_i)` with `i ∈ J`, and compare the resulting quotient maps as `J` grows. Test whether this algebraic family realizes the manuscript's partial fillings and whether its universal comparison maps agree with those in the large diagram. **Confidence: medium; reason:** monotonicity of generated relations supplies a plausible algebraic model, but the topological closure and the topos-level identification remain to be checked.

### R21 — Scan 170 | Own idea: a two-component discrete-group test

As a deliberately discrete toy model, take `Π = F(a,b)`, two groups `Ξ_i = Z`, trivial `Γ_i`, and maps sending the two chosen generators to `a` and `b`. Filling one component imposes one of the relations `a = 1` or `b = 1`, and filling both imposes both relations, providing an explicit order-of-filling test. This is not a proof for the manuscript's full category of topoi or any profinite interpretation. **Confidence: high for the discrete presentation calculation; reason:** the two stages can be compared directly by the same final pair of relations.

### R22 — Scans 167–168 | Own idea: separate cohomological tests from group calculations

For an explicitly constructed small input diagram, compare the glued topos with its locally-constant-object counterpart using a declared coefficient system and a declared cohomological degree. Repeat the calculation with more than just constant coefficients before concluding anything from an agreement of fundamental groups. **Confidence: medium; reason:** this tests the exact gap highlighted by the author's acyclicity reservation, but no computation or general counterexample is supplied in this note.

### R23 — Scans 167–168 | Own idea: an independent variance ledger

Make a ledger distinguishing scheme morphisms, geometric morphisms of topoi, and inverse-image functors for the lower étale diagram and its comparison with the earlier diagrams. Use it to diagnose the visibly leftward `X_ét → U_ét` arrow and the written target `X` on the next scan, without changing either transcription. **Confidence: high that this check is warranted; reason:** the visible direction is clear, while the intended typing and any possible authorial slip are separate questions.

## Reference

Grothendieck, A. (1981). *La Longue Marche à travers la théorie de Galois* [Handwritten manuscript, cote 140-2, “pages 1–292”; supplied scans 161–170]. Université de Montpellier.

The bibliographic identification and date above are supplied by the task description. All research items are anchored to the supplied scans, and none is presented as a literature-verified novelty claim.

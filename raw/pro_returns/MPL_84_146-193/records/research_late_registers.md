# Supplementary registers for mathematical scans 172–192

These registers were prepared analytically from the frozen transcription, without opening original scans or changing any reading. “Count” below counts displayed cases, coordinates, rows, or rules; it is not an inferred count of isomorphism classes. The files are `pages/MPL_84_146-193_84_scanNNN.tex` for the stated NNN. Individual drawings and diagrams are already enumerated in the complete page inventory; the present register records the tables and explicit or implicit finite enumerations needed for the calculation-folder question.

## Tables and enumerations

| ID | Scan / approximate TeX lines | What is enumerated | Parameters and ordering | Displayed count / total | Recomputability and qualifications |
|---|---|---|---|---|---|
| T172a | 172 / 9–15 | Product coefficients and discriminant | `b1,b2,c1,c2`; then `b,c,δ` | 3 defining identities | Universal polynomial check in `recompute_quadratic_algebras.py`; all pass in the stated monic local model. |
| T172b | 172 / 18–19 | Exceptional conditions for the indicated injection | Characteristic and the two linear coefficients | One exception described by `char.2` and `b1=b2=0` | Exact over fields; over general rings use `Ann(2,b1,b2)`. Script gives full finite coefficient grids and ring counterexamples. |
| T172c | 172 / 53–56 | Two input extension sequences | Inputs 1 and 2 | 2 rows | Structural pair, not a numeric classification; the frozen subscript `L_{1|2}` in the second row stays unresolved. |
| T174a | 174 / 14–18 | Conditions on `f:E→E` | Restriction to `L`, induced quotient action | 2 numbered conditions, second rewritten | Can be checked by a triangular 2×2 matrix once domains are fixed; do not implement the cancelled version as another condition. |
| T174b | 174 / 28–33 | Relations between `π` and `f` | Stabilizing `L`; values in `L`; restriction to `L` | 3 displayed implication/equivalence statements | Third statement has the `L'` domain issue in note L174.1; no all-true assertion is made. |
| T174c | 174 / 35–50 | Paired extensions and one cancelled tensor extension | Dual/original pair; two inputs; repeated input pair | Three pairs of 2 sequences; 1 separate cancelled sequence | This is structural bookkeeping, not a count of objects; repeated rows remain repeated. |
| T176a | 176 / 3–7 | Factor/product basis notation | `Ai,Ei` and `A,E`; generator and unit/module basis | 3-row, 6-column layout with many blank cells | Labels include unresolved indices; the layout is not a completed multiplication table. |
| T176b | 176 / 9–12 | Dual-basis evaluations | Factor pair `(Ai,Ei)` and product pair `(A,E)` | 2×2 array of 4 chained equalities, representing 8 written generic pairing values (12 after expanding `i=1,2`) | In basis order `(1,u)` versus `(x,e)`, each set is the identity matrix; generic `i` refers to either input and is not a third independent factor. |
| T176c | 176 / 19–23, 40–50 | Two coefficients of the product generator | Here `λ` is constant coefficient, `μ` multiplies `u` | 2 coefficients; `λ=b1b2`, live `μ=1` | Cancellation history includes an abandoned factor two; compare the reversed naming on scan 190. |
| T178a | 178 / 15–34 | Compatibility requirements for descent | Numbering 1°, 2°, 3° | 4 announced, 3 numbered items written | The fourth item is absent from this page; the script does not invent it or certify the doubtful second identity. |
| T180a | 180 / 33–36 | Symmetrizers on dual tensor modules | `f∈A1⊗A2`, `x∈E1⊗E2` | 2 definitions plus 2 domain entries, in a 2×2 array | Universal adjoint-matrix check supplied; the arrow glyph itself remains doubtful in the transcription. |
| T180b | 180 / 26–26, 39–64 | Four blocks of a candidate product pairing | Tensor/scalar presentation for `A`, tensor/line presentation for `E` | 1 essential block plus 3 other displayed rules = 4 | The doubtful words “deux-autres” do not match a count of three other rules; quotient compatibility must still be checked. |
| T182a | 182 / 4–7 | Boundary pairing identities | `f,x,σ,φ,ψ` | 2 displayed identities | Conditional descent identities; uncertain ambient restrictions prevent treating the two lines alone as a full proof. |
| T182b | 182 / 24–37 | Parallel notation for the two inputs | Unit; algebra element; cancelled trial; quotient `φ`; module pair `x,T`; `ψ`; `π` | 7 rows, 2 principal factor columns: 14 slots, 13 nonblank entries including 1 cancelled trial; plus the side label `E1` | This is a correspondence table, not an enumeration of finite groups or polyhedra. Row 3 has a cancelled entry only in the first factor column. |
| T184a | 184 / 5–15 | Quotient presentations | Product algebra `A` and product module `E` | 2 presentations | Universal-pushout formulas, with uncertain denominator and subscript readings retained. |
| T184b | 184 / 19–22 | Candidate dual extension sequences | `A` with scalar subobject; `E` with line subobject | 2 rows | Ranks `1,2,1` are conditional on locally free input lines and the intended quotient construction. |
| T184c | 184 / 33–34 | Pairings involving the scalar component | Scalar against tensor element; scalar against line element | 2 rules | First is `λψ(x)`, second zero; part of the four-block prescription, not a separate nondegeneracy proof. |
| T184d | 184 / 43–46 | Requested boundary values | `f∈A1 or A2`; `x∈E1⊗L2+L1⊗E2` | 2 conditions | These are desiderata signalled by “on veut”; no missing proof is filled in. |
| T186a | 186 / 3–9 | Images under tensor symmetrization | Ordered basis `(1,u1,u2,u1u2)`; nearby specialization `ui²=-ci` | 4 image entries `(2,0,0,2u1u2)` on the consistent `b1=b2=0` interpretation | Script verifies the specialization and records the general matrix; uncertain original indices remain unchanged. |
| T186b | 186 / 9 | Special quadratic products | `u1²`, `u2²`, and `u1²u2²` | 3 value relations, preceded by an isolated `1` | Checked conditionally with `b1=b2=0`; not valid for arbitrary nonzero linear coefficients. |
| T186c | 186 / 25–27 | Terms under a change of lifts | Original product; first mixed term; second mixed term; line–line term | 4 displayed terms | Coordinate-change script verifies the related scalar generator identity; doubtful variable repeats in the manuscript are not silently fixed. |
| T188a | 188 / 20–26 | Data describing an element of the dual | Trial `(f,g1,g2)` replaced by `(f,λ)` | 3 trial data items reduced to 2 live data items | `f` is a bilinear form, not one scalar coordinate; these counts are components, not dimensions. |
| T188b | 188 / 31–40 | Cancelled consistency restrictions | Labels a), b), then 2 restrictions on factor inputs | 2 cancelled labelled conditions; 2 cancelled displayed evaluations | All remain cancelled; they are not additional axioms of the live description. |
| T188c | 188 / 43–44 | Live trace restrictions | First-factor and second-factor restrictions | 2 equalities | Recoverable from the universal property of the displayed pushout; does not alone identify `E` with the dual. |
| T190a | 190 / 10–12 | Trace and norm of an affine-linear generator | Here `λ` multiplies `u`, `μ` is constant | 2 formulas | Script checks `Tr=-λβ+2μ`, `N=λ²c+μ²−λμβ`; the frozen minus/plus uncertainty is not changed. |
| T190b | 190 / 21–24 | Dual-basis pairing values | `(1,u)` against `(x,e)` | 4 entries in a 2×2 array | Conditional perfect pairing; one source entry is `u|e`, retained. |
| T190c | 190 / 26–27 | Coefficient extraction | `λ` from pairing with `e`; `μ` from pairing with `x` | 2 formulas | Same method as scan 176 with swapped scalar names. |
| T190d | 190 / 45–49 | Characterization of `u` | Pairing with `e1⊗e2`; pairing with `x1*x2` | 2 defining values, 1 and 0 | Determines `u` under the stated dual-basis hypothesis; uncertain `e_{1|2}` is retained. |
| T192a | 192 / 3–6 | Two input quadratic equations | Inputs 1 and 2, coefficients `bi,ci` | 2 rows | Inputs of the universal polynomial script; doubtful plus signs remain source doubts. |
| T192b | 192 / 14–15 | Splittings of algebras and dual modules | `A1,A2,E1,E2` | 4 displayed presentations | Local choices, not assumed globally trivial line bundles. |
| T192c | 192 / 24–27 | Choices of line bases | `e1∈L1`, `e2∈L2` | 2 choices, with 2 explanatory labels | A structural 2×2 array; a doubtful second label is retained. |
| T192d | 192 / 30–33 | Line-valued coefficients in scalar bases | `b1,c1,b2,c2` versus `β1,γ1,β2,γ2` | 4 formulas in a 2×2 array | Script tracks affine generator changes; tensor-square/ordinary-square typography remains uncertain. |
| T192e | 192 / 41–42 | Live scalar input quadratic equations | `u1,u2`, scalar `βi,γi` | 2 formulas | Second sign and β-subscript remain doubtful; the script’s consistent model is explicitly editorial. |
| T192f | 192 / 49–53 | Basis correspondence conditions | `e1=φ(u1)`; zero pairing; `ψ(x1)=1` | 3 conditions | Locally determines the indicated correspondence under perfect pairing. |
| T192g | 192 / 45–60 | Input and product basis correspondences | First input; second input; product | 3 displayed correspondences | These are object correspondences, not three independent scalar equations. |

## Numerical recomputation report

The manuscript itself does not enumerate finite-field parameter cases on these scans; the following is an explicitly editorial recomputation of its local formula. The script exhausts all `p^4` ordered coefficient tuples `(b1,b2,c1,c2)` for `p=2,3,5`, including degenerate inputs, and counts the rank of the map whose columns are `(1,0,0,0)` and `(0,b2,b1,2)`.

| Base field | Coefficient tuples | Rank-one images | Rank-two images | Product polynomials with 0 / 1 / 2 roots | Both inputs have nonzero discriminant |
|---|---:|---:|---:|---|---:|
| F₂ | 16 | 4 | 12 | 2 / 12 / 2 | 4 |
| F₃ | 81 | 0 | 81 | 18 / 45 / 18 | 36 |
| F₅ | 625 | 0 | 625 | 200 / 225 / 200 | 400 |
| Total | 722 | 4 | 718 | 220 / 282 / 220 | 440 |

For F₂ with `b1=b2=1`, the four ordered pairs `(c1,c2)` give the Artin–Schreier coefficients `c1+c2`: two split products and two nonsplit products. Thus the four rank-one failures among all 16 tuples occur exactly at `b1=b2=0`, and are different from the four étale-input cases. These finite counts illustrate the universally derived criterion and do not replace its proof.

The script also enumerates kernels over `Z/4Z` for `(b1,b2)=(0,0),(2,0),(1,0)` and `Z/6Z` for `(0,0),(3,0)`, always with `c1=c2=0`. The kernel sizes are respectively `2,2,1,2,1`, exactly as predicted by `Ann(2,b1,b2)`.

## Authorial checks, qualifications, questions, revisions, and unfinished computations

| Scan | His marker or brief words | Status on the page / linked note |
|---|---|---|
| 172 | Doubtful “injectif sauf si car. 2 et b1=b2=0” | Explicit qualification; L172.3 and the conditional general-ring analysis L172.4. |
| 172 | Cancelled “dégénéré / dégénère en car. 2” | Cancelled broad-looking warning, compared with live qualified wording on 192; L172.6. |
| 174 | `f(x)−χx∈L` replaced by `χx−f(x)∈L`; “l’identité” replaced by `χid` | Local sign and scalar corrections; retained in L174.1. |
| 176 | `!` beneath `b1u2` | Emphasis/check target, not an explicit question; L176.3. |
| 176 | `=2` cancelled in the μ computation and in final formulas | Coefficient correction to one; L176.2. |
| 176 | Final `=2·` | Unfinished reformulation; L176.4. |
| 178 | “Il y a à écrire quatre compatibilités” | Four required, only three numbered items visible in the frozen text; L178.1. |
| 178 | `OK` at the foot | Local approval marker; it does not supply the missing fourth numbered check; L178.3. |
| 180 | Question-mark alternative under `x1⊗x2` | The frozen reading also allows a parallel/equality-like mark; uncertain punctuation, not securely an authorial mathematical doubt. |
| 182 | Cancelled `½Tr`; final equality and half-expression unfinished | A normalization route is discarded or not completed; L182.1–L182.2. |
| 184 | Twice “on veut que ce soit” | Requirements on a descended pairing, not completed verifications; L184.1. |
| 186 | `?` on `E1∧E2→E1⊗E2` | Explicitly questioned comparison map; L186.1. |
| 186 | `O K` after the boundary calculation | One displayed boundary computation accepted; L186.1. |
| 188 | `(g1,g2)` replaced by `λ`; cancelled conditions a), b) | Revision of dual data and restrictions; L188.1. |
| 188 | Cancelled `E→A∨?`; cancelled `λ=ψ(x)` | Tentative comparison withdrawn on this page; the question mark itself is a transcription doubt, not a securely identified authorial doubt; L188.3. |
| 190 | “u décrit / déduit en termes de u1,u2 ?” | Explicit generator question; L190.1. |
| 190 | First coefficient pairing cancelled and replaced | The whole-product element replaces a bare `u` in the evaluation; preserved in L190.3. |
| 192 | “ça croule si 2=0, b1=b2=0” (the two French words remain doubtful) | Explicit failure warning; L192.1. |
| 192 | `u=2uu′+` | Unfinished coefficient computation; L192.4. |

## Titles and page counts in this assigned subset

The even mathematical leaves 172–192 have no identified title sheet or explicit total page count in the frozen transcription. “compatibilités pour” (178), “Considérons” (188), and the generator question (190) are working headings or prompts; they are not titles of a separately counted work. Pencil margin numbers 171,173,…,191 identify positions but do not state the extent of a text. The reused typed pages, handled separately, contain the package’s explicit textual titles and page-count remarks.

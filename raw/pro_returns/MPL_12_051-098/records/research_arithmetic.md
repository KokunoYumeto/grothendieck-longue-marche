# Arithmetic cohomology: post-freeze research record

Prepared by `/root/transfer_support`, 2026-11-17, after the transcription freeze at 19:50:51 UTC and the parent's authorization to consult context. The full context README, full 512-line RESULTS_STATE register, relevant Hua sections, and frozen scans 073–084 were read; original manuscript images were not opened, and no OCR or changes to frozen transcription, doubts, or inventory were made. The 40 files in `records/frozen_transcription_hashes.json` were checked at 20:04:38 UTC with no mismatches.

Each item below has one to four explanatory sentences; location and source metadata are separate. `Hua` means **Hua, modernised reading of cote 12**, `context/hua_project/12.modern.tex`, and is interpretative context, never an independent transcription. `RS` means `context/notes/RESULTS_STATE.md`; its returned-package statuses remain claims requiring review. All weights and Frobenius eigenvalues below use geometric Frobenius and the convention that Qℓ(1) has weight −2, with ℓ different from the finite-field characteristic.

## AR01 — The coefficient hypothesis behind the upper weight bound

**Kind:** hypothesis / reading question; **confidence:** high for the scope distinction, unresolved for the author's intended category.

**Current:** `pages/MPL_12_051-098_12_scan051.tex`, scan051, display at line31; `pages/MPL_12_051-098_12_scan073.tex`, scan073, lines5–11; **quote:** “M motif … ct tordu … de poids ρ”, upper endpoint `ρ+Inf(2i,2n)`.

**Context match:** Hua, “Motifs constants tordus, et leurs anneaux (pages 35 à 40)”, lines993–1000, and “Sur un corps fini : la suite de Hochschild–Serre et les poids (pages 70 et 72)”; also its later “Poids de la cohomologie ℓ-adique d'une variété singulière ou non propre (pages 104 à 108)”, outside the current packet. **RS connection:** MPL_15_087-138 §3 and MPL_14_002-044 B04 are comparison leads, not proofs of this coefficient bound. **Primary:** [D], [L].

Hua explicitly interprets “constant tordu” as a lisse realization, and scan074 applies the term to an abelian scheme, so finite geometric monodromy cannot be supplied silently. Deligne's ordinary-cohomology lower bound is weight ≥ρ+i for a pure lisse coefficient on a smooth separated base, while the stated upper bound is not valid for every such coefficient. A coefficient that becomes geometrically constant after a finite étale cover does satisfy the constant-coefficient bound after taking a direct summand and tensoring with its pure arithmetic representation. The Legendre calculation in AR02 is therefore a test of the broad lisse interpretation, not a change of the manuscript's words.

## AR02 — A finite-field test of both the bound and its vanishing consequence

**Kind:** own deduction from a published example; **confidence:** high, by the explicit trace formula and Poincaré duality.

**Current:** scan051, line31, and scan073, lines11–26; **quote:** `−2≤ρ≤1 (si i=1)`.

**Context match:** Hua's two subsections named in AR01; no Legendre counterexample to this assertion was located in the supplied context. **RS connection:** none settles this coefficient-scope issue. **Primary:** [L], [D]; independent confirmation from `/root/research_foundations`.

Over F5 let U=P¹−{0,1,∞} and let V=R¹f_*Qℓ for the Legendre elliptic family y²=x(x−1)(x−λ); V is pure of weight 1, while Stacks Tag 03VA computes H¹_c(Ū,V) of dimension 2 with both Frobenius eigenvalues 1. The fibre cup pairing gives V∨≅V(1), so curve duality gives H¹(Ū,V)≅H¹_c(Ū,V)∨(−2), whose eigenvalues are 25 and whose weight is 4, larger than ρ+2=3. For M=V(2), of weight −3, H¹(Ū,M) has eigenvalue 1 and hence a nonzero invariant, so Hochschild–Serre gives H¹(U,M)≠0 outside scan073's proposed range. This is an editorial deduction from a standard published example, with no claim of historical or mathematical novelty.

## AR03 — The small endpoint error is separate from the coefficient problem

**Kind:** algebraic check of a conditional argument; **confidence:** high.

**Current:** `pages/MPL_12_051-098_12_scan073.tex`, scan073, lines15–26; **quote:** `−2≤ρ≤1 (si i=1)`.

**Context match:** Hua, “Sur un corps fini : la suite de Hochschild–Serre et les poids (pages 70 et 72)”, already corrects this endpoint. **RS connection:** no additional resolution needed. **Primary:** elementary manipulation of the displayed inequalities.

Even assuming the displayed weight bounds, substituting i=1 into the two preceding intervals gives {0}∪[−2,−1]=[−2,0] for integral ρ, not [−2,1]. This is already an explicit Hua observation and must not be credited as a new finding. Fixing the endpoint alone would not resolve AR01–AR02's coefficient-scope obstruction.

## AR04 — Weight +1 on scan074 versus 1−1 on scan076

**Kind:** convention / reading question; **confidence:** high conditional on the Tate-module interpretation, no new palaeographic conclusion.

**Current:** `pages/MPL_12_051-098_12_scan074.tex`, scan074, lines16–19; `pages/MPL_12_051-098_12_scan076.tex`, scan076, line12; **quotes:** “pur de poids 1”; “poids 1−1=0”.

**Context match:** Hua, “16) Points rationnels et cohomologie des variétés abéliennes (pages 73 à 79)”, explicitly discusses and normalizes the sign. **RS connection:** LM7 C.1 and MPL_14_002-044 M24a concern related realization conventions. **Primary:** [T], [D].

If the realization intended in scan074 is R¹f_*Qℓ(1) for the dual abelian scheme, it has weight −1 and identifies with the rational Tate module of A. This is the normalization used by scan076's subsequent weight calculation, whereas an untwisted R¹f_*Qℓ has weight +1. The frozen alternatives `f^*|f_*` and `1|0` remain alternatives: the mathematical comparison explains the tension but does not decide the ink, and Hua already identifies the issue.

## AR05 — Kummer's exact sequence does not itself prove the finiteness claim

**Kind:** unproved implication / scope qualification; **confidence:** high.

**Current:** `pages/MPL_12_051-098_12_scan075.tex`, scan075, lines19–26; **quote:** “H¹(S,A)(ℓ) fini”.

**Context match:** Hua, §16; `context/MPL_16+47+54+44_transcription.tex`, cote16 scan21, equation(8.7), explicitly separates a Tate module from finite torsion in the Gm case. **RS connection:** FERMAT_SUCCESSOR A.53 and SECTIONS_OVER_Q A.186–A.188 are specific returned-package Sha claims, not general finiteness inputs. **Primary:** [ADT, II.5], [KT].

The rational Kummer sequence has cokernel VℓH¹(S,A), so the proposed equality of Mordell–Weil and cohomological spaces asks for this Tate module to vanish. Replacing that condition by finiteness of H¹(S,A)(ℓ) uses the requisite finite-cotype hypothesis and must not be inferred merely because the group is torsion. For an abelian scheme on a smooth proper curve C over a finite field, H¹(C,A) identifies with Sha(A_K/K), but an arbitrary finite-type S over Z or an open curve requires a different statement with local conditions. Thus neither the Kummer sequence nor the specific RS examples proves the general expectation written here.

## AR06 — The lattice quotient missing from scan076's last display

**Kind:** formula qualification; **confidence:** high, with an immediate test case.

**Current:** `pages/MPL_12_051-098_12_scan076.tex`, scan076, final diagram; **quote:** `H¹(Fp,M) = (M⊗Q/Z)^π`.

**Context match:** Hua, §16, already supplies the quotient by rational invariants. **RS connection:** no new standing claim. **Primary:** continuous cohomology of the displayed lattice exact sequence.

For a torsion-free finitely generated discrete G=Gal(F̄q/Fq)-module M, the exact sequence 0→M→M⊗Q→M⊗Q/Z→0 gives H¹(G,M)=(M⊗Q/Z)^G/im((M⊗Q)^G). The trivial lattice M=Z makes the distinction decisive: H¹(G,Z)=0 but (Q/Z)^G=Q/Z. Finite torsion in M requires its own finite correction, and the quotient correction is already present in Hua.

## AR07 — The finite-kernel qualification on scans077–079 matters

**Kind:** qualification already written in the manuscript; **confidence:** high.

**Current:** `pages/MPL_12_051-098_12_scan077.tex`, scan077, line15; `pages/MPL_12_051-098_12_scan079.tex`, scan079, lines3–8; **quote:** “surj. à noyau fini”.

**Context match:** Hua, §16, distinguishes the finite fixed-part contribution and the surjection. **RS connection:** none. **Primary:** the Leray sequence written on scan076, together with AR06.

The displayed isomorphism on scan079 is expressly qualified by its margin as a surjection with finite kernel. Likewise, A(S)→M^π retains the finite group of rational points of the fixed abelian variety, so passing to a rational realization can justify a comparison that is not a literal integral isomorphism. This is a qualification already supplied by the source and Hua, rather than an editorial replacement of the display.

## AR08 — Scan078's constant-Jacobian nonvanishing survives a precise normalization

**Kind:** verified calculation / normalization question; **confidence:** high.

**Current:** `pages/MPL_12_051-098_12_scan078.tex`, scan078, lines4–13; **quotes:** “n'est pas néc nul”; “End(J) … Qℓ”; “qui est non nul”.

**Context match:** Hua, §16, already emphasizes the counterexample to a later blanket vanishing; its tensor shorthand also needs dual/twist conventions. **RS connection:** MPL_15_087-138 §3, Tate's linear Hom comparison. **Primary:** [T]; constant Sha comparison [MC].

For C/Fq smooth proper geometrically connected of positive genus and A=J_C×C, the precise geometric term is H¹(C̄,Qℓ)⊗VℓJ≅End(VℓJ), while H²(C̄,VℓJ) has weight 1 and no Frobenius invariants. Hochschild–Serre, semisimplicity of finite-field abelian Frobenius, and Tate's Hom theorem therefore give H²(C,VℓJ)≅End_Fq(J)⊗Qℓ≠0. Kummer identifies this with VℓH²(C,A) after the standard rationalization, in particular in the constant case where Sha is finite. This confirms the mathematical mechanism without resolving the frozen `check J|bar J` or scalar-ring alternatives; an unqualified product VℓJ⊗VℓJ would miss the needed dual/twist.

## AR09 — Scan082 has a conflicting assertion, not an established vanishing theorem

**Kind:** unproved claim contradicted in its literal generality; **confidence:** high.

**Current:** `pages/MPL_12_051-098_12_scan082.tex`, scan082, opening; **quotes:** “H^i(C,A)=0 si i≥2”; “sans doute … H¹(C,A)=0”.

**Context match:** Hua, “Une courbe sur un corps fini (page 81)”, already flags both assertions and their conflict with scan078. **RS connection:** specific Sha claims listed in AR05 do not imply universal vanishing. **Primary:** [ADT, II.5], [KT], and AR08.

Taking the positive-genus constant Jacobian of AR08 disproves the first assertion as written, even for a smooth proper curve and an abelian scheme. The degree-one group in that setting is a Sha group, for which finiteness is already weaker than zero; neither Weil weights nor Tate's finite-field Hom theorem supplies the claimed vanishing. The text presents a later speculative leaf, not an explicit resolution of the earlier nonvanishing, and Hua already recognizes this conflict.

## AR10 — The BSD comparison needs its global-function-field setting

**Kind:** modern theorem delimiting a heuristic; **confidence:** high.

**Current:** `pages/MPL_12_051-098_12_scan080.tex`, scan080, final sentence; **quote:** “essentiellement équivalente à la conjecture de Birch--Swinnerton Dyer”.

**Context match:** Hua, §16, discusses the curve/function-field case and Brauer comparison; scan079 asks about the corresponding map of H²(Gm). **RS connection:** FERMAT_SUCCESSOR A.53 and SECTIONS_OVER_Q A.186–A.188 are separately scoped arithmetic claims. **Primary:** [KT], [MA].

For an abelian variety over a function field in one variable over a finite field, Kato–Trihan proves that finiteness of one ℓ-primary Sha component, including ℓ=p, implies the full BSD conjecture. This is an appropriate modern comparison for the rank/Kummer question after restricting the base and supplying the local conditions. It is not a statement that arbitrary higher-dimensional bases in scans074–080 satisfy the classical global-field BSD equivalence, and numerical rank comparisons must distinguish Frobenius invariants from generalized eigenspaces.

## AR11 — The local p-primary observation is compatible with duality, but Oda has a different scope

**Kind:** established local comparison / limitation; **confidence:** high.

**Current:** `pages/MPL_12_051-098_12_scan082.tex`, scan082, local-duality paragraph; **quote:** “essentiellement un p-groupe, modulo groupe fini”.

**Context match:** Hua, “Une courbe sur un corps fini”; `context/MPL_16+47+54+44_transcription.tex`, cote54 scan7, final question about recovering an extension from p^A; `context/MPL_16+47+54+44_notes.md`, D05, already cites Oda. **RS connection:** LM7 C.1 concerns realizations, not a p-primary Sha-finiteness result. **Primary:** [ML], [O].

Over a characteristic-p local field, local duality identifies H¹(K,A) with the Pontryagin dual of A∨(K), whose open formal subgroup is pro-p and whose quotient is finite, explaining the stated prime-to-p finiteness qualification. Oda's Corollary 5.11 identifies the Dieudonné module of A[p] with H¹_dR(A), including the Hodge subspace, for an abelian variety over a perfect field. Thus the finite group scheme and its F,V structure retain information that geometric p-torsion points alone lose, exactly the limitation already identified by context D05. This does not prove local or global Sha finiteness, and Oda's perfect-field theorem cannot simply be applied to the imperfect local field Fq((t)).

## AR12 — The literal high-degree question on scan084 has a singular counterexample

**Kind:** own explicit hypothesis test using standard cohomology; **confidence:** high, with incidence ranks independently checked by code.

**Current:** `pages/MPL_12_051-098_12_scan084.tex`, scan084, lines5 and32–38; **quotes:** “X de type fini sur Z”; “H^i(X,Qℓ(1))=0 … si i≥4 ??”.

**Context match:** Hua, “Calculs sur Qℓ(1) et Gm (page83)”, repeats the question without settling it; its later singular-weight subsection gives general background but not this construction. **RS connection:** no located result settles this literal singular case. **Support:** calculation below and `records/arithmetic_snc_check.py`, with exact output in `records/arithmetic_snc_check.json`.

Let D={x0x1x2x3=0}⊂P³_Fq and X=D×P¹_Fq, a proper singular scheme of finite type over Z, with ℓ≠p. The four planes have six pairwise lines, four triple points, and no fourfold intersection, so the component complex is the boundary of a tetrahedron and contributes a Frobenius-fixed weight-zero line to H²(D̄,Qℓ). Tensoring this line with H²(P¹,Qℓ)(1) gives a fixed line in H⁴(X̄,Qℓ(1)), and Hochschild–Serre consequently forces H⁴(X,Qℓ(1))≠0. This answers the unrestricted question negatively while preserving its question marks and makes no novelty claim beyond providing an explicit editorial test absent from the checked context.

## AR13 — Exact size of the example, and why the smooth case differs

**Kind:** own calculation; **confidence:** high, because every stratum and differential is explicit.

**Current / context / RS:** as AR12. **Primary comparison for the smooth case:** [D, Corollary 3.3.5].

The augmented component resolution is exact on geometric stalks, and its hypercohomology has E1 rows Qℓ⁴→Qℓ⁶→Qℓ⁴ in b=0, Qℓ(−1)⁴→Qℓ(−1)⁶ in b=2, and Qℓ(−2)⁴ in b=4, with nonzero differential ranks 3,3,3. Parity and the three-column range force degeneration after these differentials, giving H²(D̄)=Qℓ⊕Qℓ(−1), H³(D̄)=Qℓ(−1)³, and H⁴(D̄)=Qℓ(−2)⁴ as Frobenius modules. Künneth then gives invariant dimension 1 in H⁴(X̄,Qℓ(1)) and coinvariant dimension 3 in H³(X̄,Qℓ(1)), so the arithmetic H⁴ of X has dimension 4, while the same calculation already gives H⁴(D,Qℓ(1))≅Qℓ³. For smooth separated finite-type X/Fq, in contrast, the lower weight bounds for H^{i−1}(X̄,Qℓ(1)) and H^i(X̄,Qℓ(1)) are i−3 and i−2, both positive when i≥4, and Hochschild–Serre does give vanishing.

## AR14 — Removing one point from a curve does not make its Brauer group infinite

**Kind:** own quantitative qualification of an existing context claim; **confidence:** high, by the residue sequence.

**Current:** `pages/MPL_12_051-098_12_scan084.tex`, scan084, lines41–48; **quote:** “faux quand on lui enlève des pts”; ambiguous degrees `2|3` and `3|2`.

**Context match:** Hua, “Calculs sur Qℓ(1) et Gm (page83)”, repeats the broad assertion; `context/MPL_16+47+54+44_transcription.tex`, cote16 scans21 and23, Kummer and Brauer exact sequences, distinguish torsion and rational parts. **RS connection:** LM7 C.1 is a useful puncture/1-motive comparison, not a resolution of the ambiguous degree. **Primary:** [ADT, II.2.1].

For a smooth proper geometrically connected C/Fq and U=C−D with r≥1 removed closed points, the global residue sequence gives Br(U)=ker((Q/Z)^r→Q/Z)≅(Q/Z)^{r−1}. Consequently a single puncture still gives Br(U)=0, whereas two give Q/Z, and the relevant prime-to-p corank is r−1 rather than the number of removed points. Rational Kummer and localization yield the comparison below, which also explains why the two cohomological degrees behave differently. This is a mathematical qualification of the wording, not permission to resolve either frozen numeral alternative from expected theory.

| Curve | dim H²(−,Qℓ(1)) | dim H³(−,Qℓ(1)) | Br(−) |
|---|---:|---:|---|
| Proper C | 1 | 1 | 0 |
| C minus one closed point | 0 | 0 | 0 |
| C minus r≥1 closed points | r−1 | 0 | (Q/Z)^{r−1} |

## AR15 — Rational Tate modules suppress precisely some information needed by the questions

**Kind:** context match / limitation; **confidence:** high.

**Current:** scan075 Kummer sequence; scan078 H²(A); scan084 “coBrauer” and `Tℓ(Gm)=Qℓ(1)`.

**Context match:** `context/MPL_16+47+54+44_transcription.tex`, cote16 scan21, equations(8.3)–(8.7), and scan23, equations(8.8)–(8.9); `context/MPL_16+47+54+44_notes.md`, 16:21:1–4 and R8. **RS connection:** LM7 C.1's integral realizations and SECTIONS_OVER_Q A.186–A.188's finite primary groups. **Primary:** the supplied exact sequences; [O] for the distinct characteristic-p realization.

The earlier cote16 pages explicitly retain finite torsion before identifying rational Tate modules and distinguish Br′ from its divisible part. That distinction explains why a zero rational Tate module, a finite torsion group, and a zero torsion group cannot be interchanged in scans075–084. The scalar notation on scan084 mixes a Qℓ-valued heading with a possible Zℓ example, so a modern comparison should specify the rationalization while leaving the diplomatic notation unchanged.

## AR16 — What these checks do and do not contribute to the standing register

**Kind:** standing-problem match and non-implication; **confidence:** high about the scope of the present calculations.

**Current:** scans074–084, rational points, abelian realizations, Kummer, weights, and local terms.

**Context / RS:** `context/notes/RESULTS_STATE.md`, FLAGGED_149 B9; LM7 E.23; LM6 A.22; LM7 C.1 and C.8; FERMAT_SUCCESSOR A.53; SECTIONS_OVER_Q A.182 and A.186–A.188; MPL_15_087-138 §3; WG2 §1.1 #2/#3 and §2.3 #12.

These pages provide explicit linear comparisons and failure tests for abelian realizations, so they connect naturally with the registered Picard 1-motive and Jacobian calculations. They do not prove the still-labelled-open prime-to-p point question FLAGGED_149 B9, the metabelian/depth-two section-map problem LM7 E.23, or the CM procyclic-normalizer problem LM6 A.22, because none of the present calculations supplies the requisite nonabelian reconstruction or local compatibility. Likewise, the specific returned-package Sha and rank results remain separately scoped claims rather than inputs for a general finiteness theorem here. RS's overview sentence “No Hua findings fall in these scans” is inaccurate for this packet: Hua's §§V–VI directly discuss the current arithmetic leaves, and their prior observations are credited throughout this record.

## Optional support — A symmetric-square version of AR02

**Kind:** independent check, not needed for the shorter main example; **confidence:** high.

**Primary:** [K, Chapter 15, pp. 73–74], [D, Theorem 1.8.4]; independent deduction checked by `/root/hua_comparison`.

For F=Sym²V on the Legendre U over an odd finite field, Katz gives purity of weight 2, geometric monodromy SO3, and tame local monodromy consisting of one Unip(3) block at each cusp. The three inertia-invariant lines have weight 0; χ_c(Ū,F)=−3 and vanishing of H⁰,H²_c imply that their boundary injection exhausts the three-dimensional H¹_c. Since F∨=F(2), duality makes H¹(Ū,F) pure of weight 6, exceeding the claimed upper bound 4. The rank-two F5 example in AR02 is preferable for the main note because it has an explicit published trace calculation and fewer ingredients.

## Primary sources and retrieval provenance

The URLs below identify the sources; retrieval references are supplied for the parent to reopen before using live citations in a final response. No secondary search snippets are used as evidence.

| Key | Primary source and exact point used | URL | Retrieved reference IDs |
|---|---|---|---|
| D | P. Deligne, *La conjecture de Weil II*, Publ. Math. IHÉS52(1980),137–252; Theorem 1.8.4, Corollaries 3.3.4–3.3.8; introduction p. 138 explicitly equates lisse and “constant tordu” | https://publications.ias.edu/sites/default/files/Number40.pdf | turn403751952view0; turn490511336view0; turn821460587view1 |
| L | The Stacks Project, §64.24, Tag 03VA, *The Legendre family*, explicit compact-support trace computation | https://stacks.math.columbia.edu/tag/03VA | turn512974160view0; independent parent-agent refs turn196551735view0 and turn610018403view2 |
| T | J. Tate, *Endomorphisms of Abelian Varieties over Finite Fields*, Invent. Math.2(1966),134–144; §1 main theorem and §2 Frobenius semisimplicity, p. 138 | https://pazuki.perso.math.cnrs.fr/index_fichiers/Tate66.pdf | turn961214263view1 |
| ADT | J. S. Milne, *Arithmetic Duality Theorems*, second edition(2006); II.2.1 residue sequence, II.5.1–5.2 finiteness/duality qualifications, II.5.5 Sha identification | https://www.jmilne.org/math/Books/ADTnot.pdf | turn223045030view0; turn775252917view0; turn775252917view1 |
| KT | K. Kato and F. Trihan, *On the conjectures of Birch and Swinnerton-Dyer in characteristic p>0*, Invent. Math.153(2003),537–592; introduction theorem p. 537; author-uploaded full text | https://doi.org/10.1007/s00222-003-0299-2 ; https://www.researchgate.net/publication/227273997_On_the_conjectures_of_Birch_and_Swinnerton-Dyer_in_characteristic_p0 | turn348528139view0; turn618209735view1 |
| MA | J. S. Milne, author comments on *On a conjecture of Artin and Tate* (1975), distinguishing the ℓ-primary and p-primary comparisons and the later Kato–Trihan result | https://jmilne.org/math/articles/1975a.html | turn918421462view1 |
| MC | J. S. Milne, *The Tate–Shafarevich group of a constant abelian variety*, Invent. Math.6(1968),91–105; author's statement of the full BSD result for constant abelian varieties | https://www.jmilne.org/math/articles/1968b.html ; https://www.jmilne.org/math/articles/abstracts.html | turn895722189view0; turn895722189view2 |
| ML | J. S. Milne, *Weil–Châtelet groups over local fields*, Ann. Sci. ENS3(1970),273–284, addendum5(1972),261–264; author's statement of characteristic-p local duality | https://www.jmilne.org/math/articles/1970c.pdf ; https://www.jmilne.org/math/articles/abstracts.html | turn895722189view1; turn895722189view2 |
| O | T. Oda, *The first de Rham cohomology group and Dieudonné modules*, Ann. Sci. ENS4e série2(1969),63–135; Corollary 5.11, printed p. 131 / PDF page 70 | https://www.numdam.org/item/ASENS_1969_4_2_1_63_0.pdf | turn741419338view1; supplied PDF independently inspected at Corollary 5.11 |
| K | N. M. Katz, *Convolution and Equidistribution*, author PDF, Chapter 15, pp. 73–74, Legendre and symmetric-square local/geometric monodromy | https://web.math.princeton.edu/~nmk/mellin398.pdf | turn918421462view0; turn348528139view1; turn348528139view2; turn821460587view0 |

## Reproducibility and file boundary

Run `python records/arithmetic_snc_check.py` from `MPL_12_051-098_work` to reproduce the exact incidence ranks and dimension 4 calculation; the script reads no user source files. Its output is retained as `records/arithmetic_snc_check.json`. The report, script, and JSON are the only new written deliverables from this arithmetic task; Oda extraction/rendering intermediates are outside the work directory and are not checkpoint deliverables. No upload or checkpoint was performed by this agent.

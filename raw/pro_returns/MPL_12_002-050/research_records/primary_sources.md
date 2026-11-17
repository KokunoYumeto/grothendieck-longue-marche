# Primary-source checks for the research notes

**Intermediate research record.** The reconciled theorem scopes, final source locators, and all 17 bibliography entries are in `../MPL_12_002-050_notes.md`. This report preserves the initial checks; the final notes include the subsequent Nori/Ayoub, period-connectedness, and birational-counterexample qualifications.

Research phase, 17 November 2026. `context/README.md` and `context/notes/RESULTS_STATE.md` were read first. No source scan was read for this subtask and no frozen transcription file was changed. These are bounded literature checks, not a review of every proof in the cited papers. The parent reader must align the external statements with the frozen manuscript wording and scans.

## Register connections and scope

The directly relevant existing leads are **WG2 §2.4 #3** (correspondence rings, lettering, and the proposed SL₂/weight identification), **WG2 §2.3 #7** (numerical semisimplicity), **MPL_14_087-132 M04 and M23**, **MPL_15_087-138 L07 and §111**, **MPL_15_195-228+18_002-017 M07 and S15**, **MPL_18_018-062 MB10 and §2**, and **MPL_15_087-138 T26**. The Hom comparison also bears on **MPL_18_018-062 §3** and **MPL_15_087-138 §3**. Their register status remains that of first-pass leads; this file verifies specified published comparison statements rather than re-deriving those runs' claims. The register's open **LM6 A.22** is not resolved by any comparison below.

## SC69 — Grothendieck's original printed conventions

**A. Grothendieck, “Standard conjectures on algebraic cycles,” 1969, pp. 193–199, especially §§2–4.** [Researcher-hosted text](https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/StandardConjs.pdf).

The checked text uses **A(X)** for the Lefschetz assertion, including its restriction to algebraic classes; **B(X)** for algebraicity of the Λ-operator; **C(X)** for algebraic Künneth projectors, with a stronger independence-of-ℓ formulation; and **Hdg(X)** for positivity. It states B(X)⇒A(X) and A(X×X)⇒B(X), so the global formulations are equivalent. This paper does not provide the later full A/B/C/D/I list under those exact letters. In particular, do not call the manuscript's lettering identical to “Grothendieck 1969” merely because some letters recur. genui{"citation":{"refs":["turn717828400view0","turn310834320view3","turn310834320view4","turn709572008view5"]}}

## SC94 — The conventional comparison table

**S. L. Kleiman, “The standard conjectures,” Motives, Proc. Sympos. Pure Math. 55(1), 1994, pp. 3–20.** [University-hosted paper](https://download.uni-mainz.de/mathematik/Algebraische%20Geometrie/Lehre/WS23.Padische1994.Kleiman.Standard.Conjectures.pdf). Checked §4, especially printed p. 14, and §5, printed pp. 16–17.

| Printed convention | Content to match against the manuscript's actual statement |
|---|---|
| A(X,L) | Lefschetz isomorphism on rational algebraic cycle classes. |
| B(X) | Algebraicity of the Lefschetz inverse/Λ operator. |
| C(X) | Algebraicity of the cohomological Künneth projectors. |
| D(X) | Equality of homological and numerical equivalence. |
| Hdg(X) | Positivity of the signed intersection pairing on primitive algebraic classes. |

**Lettering caveat:** the checked original papers use **Hdg**, not the letter I. The table identifies mathematical content; it is not a claim that every printed source uses the same labels. Kleiman's Proposition 5-1 says D⇒A, with the converse under Hdg. genui{"citation":{"refs":["turn511174439view5","turn511174439view3","turn862254603view3"]}}

An exact modern source for **I** is **J. S. Milne, *Tannakian Categories*, penultimate version, 16 February 2025**, Chapter VI §8, printed pp. 241, 247, 251–252: [author's text](https://www.jmilne.org/math/Books/tcdraft.pdf). It gives A(X,L) and B(X), then **Iᶦ(X,L)** for positive definiteness on primitive codimension-i algebraic classes and **I(X,L)** for all these assertions together; Conjecture 8.32 is D(X). Conjecture 8.1 uses C(X) for algebraic Künneth projectors. Thus I is a verified modern label for the same positivity content, without attributing that letter to Grothendieck's 1969 paper. genui{"citation":{"ref":"turn977945775view3"}}

## J92 — Numerical semisimplicity does not automatically supply realization

**U. Jannsen, “Motives, numerical equivalence, and semi-simplicity,” Invent. Math. 107 (1992), 447–452.** [Institutional PDF](https://epub.uni-regensburg.de/26642/1/jannsen10.pdf). Checked Theorem 1 and Corollary 2.

For a base field k and characteristic-zero coefficient field F, Theorem 1 identifies numerical equivalence as precisely the adequate equivalence relation whose correspondence-motive category is semisimple abelian. Standard conjectures are not needed for numerical semisimplicity. Corollary 2 adds algebraicity of Künneth components and changes the commutativity signs to obtain a Tannakian category. This is not a statement that an arbitrary Weil cohomology already factors through numerical equivalence. **Inference:** such factorization requires numerically trivial correspondences to act trivially in the chosen cohomology; equality of numerical and homological equivalence supplies this missing condition. Keep numerical motives, homological motives, and a chosen realization separate. genui{"citation":{"ref":"turn717828400view1"}}

## NA17 — What the Nori/Ayoub comparison proves

**U. Choudhury and M. Gallauer Alves de Souza, “An isomorphism of motivic Galois groups,” Adv. Math. 313 (2017), 470–536.** [Accepted manuscript](https://ora.ox.ac.uk/objects/uuid%3Ab86c4da7-d7ad-4b63-abc2-c78853bf050a/files/md8343c1db0d1a4927ecb71bb3205cbc0); [arXiv record](https://arxiv.org/abs/1410.6104). Checked introduction and Theorem 9.1.

The setting includes a field embedded in C, hence characteristic zero, with the chosen Betti realization. Theorem 9.1 identifies the Nori and Ayoub Hopf algebras, and therefore their affine pro-group schemes, for coefficients in a principal ideal domain. This supports an actual comparison of the constructed motivic Galois groups. It does **not** by itself identify every motivic correspondence with an algebraic cycle modulo homological or numerical equivalence, prove the standard conjectures, establish general fullness of Hodge/ℓ-adic realizations, or make the entire mixed category semisimple. Those would be additional conclusions requiring separate input. genui{"citation":{"refs":["turn205789477view1","turn310834320view8","turn709572008view3","turn533611484view3"]}}

## A13 — The pure Nori comparison uses motivated cycles

**D. Arapura, “An abelian category of motivic sheaves,” Adv. Math. 233 (2013), 135–195.** [Working author preprint, arXiv:0801.0261v4](https://arxiv.org/pdf/0801.0261); [institutional author text](https://pure.mpg.de/pubman/item/item_3121497_1/component/file_3121498/Arapura_an%2Babelian_oa_2013.pdf). Checked §6.4, Theorem 6.4.1. The institutional URL returned 403 to the parent reader; the arXiv text was opened successfully and the theorem independently checked there. genui{"citation":{"refs":["turn941228787view2","turn833958865view2"]}}

Arapura identifies his rational pure category with André's category of motives; over a point this is the pure Nori/André comparison relevant here. André's category is semisimple Tannakian and has a faithful Betti realization. Its morphisms are **motivated** correspondences. The paper explicitly distinguishes these from algebraic cycles and states their coincidence under standard-conjecture assumptions. Thus this theorem does not erase the algebraicity issue in Grothendieck's original correspondence construction. genui{"citation":{"ref":"turn709572008view1"}}

## P — A precise period-conjecture formulation

**A. Huber, “Galois theory of periods,” especially §5.3, Conjecture 5.10 and Proposition 5.11.** [Author/institutional paper](https://home.mathematik.uni-freiburg.de/arithgeom/preprints/huber-galois.pdf).

For a rational Nori motive over Q̄, the tensor category it generates has Tannaka group G(M) and formal-period torsor X(M). The stated conjecture requires connectedness of X(M) and equality between dim G(M) and the transcendence degree of its periods. Proposition 5.11 gives the equivalent formulation using genericity of the evaluation/comparison point together with connectedness. **Scope inference:** construction of comparison isomorphisms or of the period torsor alone is not this transcendence assertion. A manuscript passage should be called a period conjecture only if it asserts the relevant genericity, algebraic-independence, or dimension statement, with its hypotheses. genui{"citation":{"ref":"turn205789477view2"}}

## TH — The linear Hom theorem, with fields kept explicit

**J. Tate, “Endomorphisms of abelian varieties over finite fields,” Invent. Math. 2 (1966), 134–144.** [Researcher-hosted original](https://pazuki.perso.math.cnrs.fr/index_fichiers/Tate66.pdf), opening Main Theorem.

For abelian varieties A,B over a finite field k and ℓ≠char(k), the canonical map

\[
\mathbf Z_\ell\otimes\operatorname{Hom}_k(A,B)
\longrightarrow\operatorname{Hom}_{G_k}(T_\ell A,T_\ell B)
\]

is an isomorphism. This is a theorem about homomorphisms of abelian varieties, not arbitrary maps of varieties. genui{"citation":{"ref":"turn310834320view1"}}

**G. Faltings, “Endlichkeitssätze für abelsche Varietäten über Zahlkörpern,” Invent. Math. 73 (1983), 349–366.** [Researcher-hosted original](https://pazuki.perso.math.cnrs.fr/index_fichiers/Faltings83.pdf). Checked §5, Satz 3, Satz 4, and Korollar 1, printed pp. 360–361.

For number fields, Satz 3 gives semisimplicity of the rational Tate-module representation, and Satz 4 and Korollar 1 give the corresponding integral ℓ-adic End/Hom isomorphisms. Thus a number-field comparison with anabelian Hom can use Faltings, instead of silently transferring Tate's finite-field theorem to a different base. genui{"citation":{"ref":"turn862254603view1"}}

## AH — The nonlinear Hom theorem requires openness and outer equivalence

**S. Mochizuki, “The local pro-p anabelian geometry of curves,” Invent. Math. 138 (1999), 319–423.** [Author's paper](https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Local%20Pro-p%20Anabelian%20Geometry%20of%20Curves.pdf). Checked introduction Theorem A and its identification with Theorem 16.5.

For a sub-p-adic field K, smooth source and hyperbolic curve target, the theorem identifies dominant K-morphisms with open continuous arithmetic fundamental-group homomorphisms over G_K, modulo inner automorphisms from the geometric target group. The theorem covers the profinite and geometric pro-p versions stated there; number fields are within its base-field scope. This is not a bijection between all variety maps and all abstract group homomorphisms. **Inference for the requested table:** passing to abelianization/Jacobians gives a linear shadow and forgets information retained by the full arithmetic fundamental group. genui{"citation":{"refs":["turn310834320view9","turn205789477view3"]}}

## W — Central tensor grading versus a Lefschetz SL₂

**P. Deligne and J. S. Milne, “Tannakian Categories,” LNM 900 (1982), checked in the authors' corrected 2018 text, Definition 5.1, p. 49.** [Author-hosted text](https://www.jmilne.org/math/xnotes/tc2018.pdf); [version information](https://www.jmilne.org/math/xnotes/tc.html).

A functorial tensor-compatible Z-grading of the **category itself** corresponds to a central cocharacter G_m→G. This differs from merely choosing a grading on the vector spaces of one fibre functor. genui{"citation":{"ref":"turn793736073view3"}}

**Formal inference, high confidence; not a new result and not a re-proof of the register's manuscript claims.** If an SL₂→G had its diagonal cocharacter equal to this central weight cocharacter, its Lie-algebra Cartan element H would be central. The relations [H,E]=2E and [H,F]=−2F would force E=F=0 in characteristic zero, and then H=[E,F]=0: the SL₂ action would be trivial. Therefore a nontrivial Lefschetz SL₂ cannot be embedded with that identification of Cartan and central weight. This does not exclude other SL₂ subgroups of a motivic Galois group.

The categorical typing matters as well: an algebraic Lefschetz map is naturally h^i(X)→h^{i+2}(X)(1), preserving weight after its Tate twist; the untwisted raising operator on total cohomology changes degree. An action through the algebra of correspondences is consequently not automatically a subgroup of tensor automorphisms of the realization. These distinctions bear on **WG2 §2.4 #3**, **MPL_14_087-132 M04**, and **MPL_15_087-138 L07/§111**; preserve their existing status rather than announcing their conclusion as new.

Similarly, semisimplicity and trivial centre should not be equated: representations of G_m in characteristic zero are semisimple although its centre is all of G_m. This is an elementary counterexample to an unrestricted dictionary between those two properties.

## E — Hua's proposed Enriques test: supported, with coefficient/equivalence caveats

**Credit:** the proposal to test the statements at cote 12 scans 049–050 against complex Enriques surfaces comes from **Hua's modernised reading**, as communicated by the parent reader. The following verifies the external mathematics; it does not verify the reading or meaning of γ on those manuscript pages.

**I. Dolgachev, “A brief introduction to Enriques surfaces,” arXiv:1412.7744v2 (11 April 2016), §3, pp. 6–8.** [Author's research article](https://arxiv.org/pdf/1412.7744).

For a complex Enriques surface S the checked passages give q=p_g=0, b₁=0, b₂=10, 2K_S=0 and Kodaira dimension zero. They explicitly identify Pic(S) with H²(S,Z), so degree-two cohomology is algebraic; rationally the odd cohomology vanishes. These statements concern the surface, not the unirationality of its moduli space. genui{"citation":{"refs":["turn793736073view2","turn355122679view1","turn765603169view3"]}}

**Inferences, high confidence.** The nonzero section of 2K_S rules out ruledness, because a ruled surface has no positive pluricanonical sections. It also rules out unirationality in characteristic zero: resolving a generically finite dominant rational map from P² gives a rational smooth surface mapping separably to S, and pullback injects pluricanonical sections, contradicting their vanishing on that rational surface. Thus “H² algebraic implies ruled” fails for complex surfaces.

With **rational homological equivalence**, a point, a divisor basis and its intersection-dual basis supply projectors and give

\[
h(S)\simeq\mathbf1\oplus\mathbf Q(-1)^{\oplus10}\oplus\mathbf Q(-2).
\]

This calculation concerns the underlying motive, not every additional structure, and does not by itself prove the same decomposition for **Chow** motives. Its use against “all positive γ vanish ⇒ unirational” depends on verifying that the manuscript's γ really vanishes on these Tate summands.

**S. Bloch, A. Kas and D. Lieberman, “Zero cycles on surfaces with p_g=0,” Compositio Math. 33 (1976), 135–145.** [Journal archive original](https://www.numdam.org/item/CM_1976__33_2_135_0.pdf), opening discussion, pp. 135–136.

This paper independently proves that any two points of a complex Enriques surface are rationally equivalent, hence CH₀(S)≅Z. It is an additional Chow-theoretic input, not a consequence of H² being algebraic. No complete Chow-motive decomposition is claimed on the basis of the short checks in this record. genui{"citation":{"ref":"turn793736073view1"}}

## H05 — A primary genus-two witness stronger than an isogeny

**Credit:** Hua's modernised reading proposed the isogenous-Jacobian test for cote 12 scan 049; the particular published witness below was located in this literature check.

**E. W. Howe, “Infinite families of pairs of curves over Q with isomorphic Jacobians,” J. London Math. Soc. 72 (2005), 327–350.** [Author's publication page](https://ewhowe.com/papers/paper20.html); [author's preprint](https://arxiv.org/pdf/math/0304471).

The paper gives geometrically nonisomorphic genus-two curves over Q whose Jacobians are isomorphic as **unpolarized** abelian varieties, including examples with absolutely simple Jacobians. This is stronger than the isogeny witness requested. The introduction expressly separates the result from polarized Torelli. **Inference:** their unpolarized H¹ realizations cannot reconstruct the curves, and Riemann–Hurwitz excludes nonconstant maps between the distinct genus-two curves, despite the Jacobian isomorphism. This does not refute reconstruction from the canonically principally polarized Jacobian, nor the anabelian Hom theorem with its full group and openness conditions. genui{"citation":{"refs":["turn793736073view0","turn765603169view0"]}}

## SS — Supersingular E × E: geometric H² algebraic, but not ruled

**E. Z. Goren and K. E. Lauter, “Evil Primes and Superspecial Moduli,” IMRN (2006), Article ID 53864, §4, printed pp. 14–16.** [Author-hosted published paper](https://www.math.mcgill.ca/goren/PAPERSpublic/evilprimes.pdf).

For A=E×E over an algebraic closure of F_p, with E supersingular, the paper identifies NS(A) with the symmetric endomorphism lattice for a principal polarization, and explicitly states that this lattice has rank 6. In the product-polarization presentation it consists of quaternionic Hermitian two-by-two matrices, with two integral diagonal coordinates and one quaternionic off-diagonal coordinate. genui{"citation":{"refs":["turn833958865view0","turn717209793view1"]}}

**J. S. Milne, *Abelian Varieties*, version 2.00 (2008), Chapter I, Propositions 3.9–3.10 and Theorem 12.1.** [Author's text](https://www.jmilne.org/math/CourseNotes/AV.pdf). The theorem gives b₂(A)=6 and b₁(A)=4. The propositions say that rational maps from P¹, and more generally from a unirational variety, to an abelian variety are constant. genui{"citation":{"refs":["turn833958865view3","turn224298932view1","turn977945775view4"]}}

**Inferences, high confidence.** For ℓ≠p, the Kummer sequence injects NS(A)⊗Q_ℓ into H²_et(A,Q_ℓ(1)); both spaces have dimension 6, so the divisor cycle map is an isomorphism. This is **geometric** cohomology and geometric NS: over a particular finite field, not every divisor need already be defined over that field. No assertion for de Rham cohomology in characteristic p is being substituted for this ℓ-adic statement.

The absence of rational curves rules out ruledness: a birational parametrization by a ruled surface would give nonconstant rational maps from its general P¹ fibres into A. Proposition 3.10 also excludes unirationality. Thus this independently supports the H²-algebraic/nonruled counterexample communicated by the parent reader. Since b₁(A)=4, the example alone does **not** give a motive consisting only of Tate summands or establish the separate “all positive γ vanish” premise.

## Retrieval and use limits

All substantive external claims above were checked in papers by their authors, author-hosted texts, institutional manuscripts, or journal archives. The bibliography is deliberately bounded. No inference here establishes the archive's precise lettering or supplies missing manuscript hypotheses; those remain the parent reader's task using the frozen transcription. The supplied register's earlier results remain claims except where its own status explicitly records review. Before citing these web references in the final response, the parent should open the linked sources in its own research session.

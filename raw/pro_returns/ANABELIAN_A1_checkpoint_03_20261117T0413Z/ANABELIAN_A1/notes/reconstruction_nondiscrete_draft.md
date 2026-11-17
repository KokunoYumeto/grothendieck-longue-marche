# Rank-one nondiscrete residue-characteristic-zero extension

Literature auditor, 17 November 2026. This draft was independently reviewed by the parent, configuration auditor and criterion auditor and promoted as B.LIT5–6 in `sections/B_reconstruction_nondiscrete.tex`. All three reviews found no blocker. The primary-source hypotheses below have been checked. The new argument is the passage to the valuative logarithmic limit, not a statement quoted verbatim from one source.

## Proposed conclusion

Let K carry a nontrivial henselian **rank-one** valuation of residue characteristic zero, without a discreteness or completeness assumption. Then the supported scaling from B.CF6 produces a nonalgebraic pinned self-equivalence of the small étale topos of A1_K over BG_K. Consequently étale-topos reconstruction fails over K.

This suffices for every nontrivially henselian valued field of finite transcendence degree over Q whose specified valuation has residue characteristic zero: such a valuation has finite rational rank and hence finite rank, so it admits a nontrivial rank-one coarsening, which remains henselian and of residue characteristic zero. Mixed characteristic is not included.

## Primary sources opened

1. P. Achinger, K. Hübner, M. Lara, J. Stix, *Logarithmic geometry beyond fs*, arXiv:2411.13662v1, 22 November 2024, https://arxiv.org/pdf/2411.13662. Opened `turn108view0`, independently reopened `turn116view0`; exact Proposition 4.2.6 located in `turn116view1`. Downloaded PDF/text: `sources/AchingerHubnerLaraStix2024_beyondfs.*`.
2. E. Lepage, *Covers in p-adic analytic geometry and log covers I*, AIF 63 (2013), 1427–1467, https://www.numdam.org/article/AIF_2013__63_4_1427_0.pdf, independently opened `turn87view0`. Theorems 1.6 and 1.8, pp.1437–1439, are the fs input.
3. B. Hassett, *Moduli spaces of weighted pointed stable curves*, Adv. Math. 173 (2003), no.2, 316–352, DOI 10.1016/S0001-8708(02)00058-0. Author PDF https://www.math.brown.edu/bhassett/papers/weights/weights10.pdf, `turn123view0`; journal metadata `turn118search2`. Theorem 2.1, author PDF p.4: the stable weighted moduli stack is smooth proper over Z and its coarse moduli scheme is projective; all weights one recovers ordinary stable pointed curves. For genus zero with at least three labelled marks every automorphism is trivial, so the stack is the fine projective scheme. The finite-presentation moduli problem extends from the paper's initially noetherian bases to arbitrary bases by the usual limit descent of finitely presented families. Only properness and the universal stable family are used here.

### Exact AHLS input

* Definition 3.4.4: an affine charted system has compatible strict étale chart covers by direct systems of **saturated prelog rings**. Transition maps are affine. Its limit is saturated, with the expected colimit log structure.
* Proposition 4.2.6: the category of finite Kummer étale covers of such a qcqs saturated limit is the filtered colimit of the corresponding covering categories. In this non-fs theory a finite Kummer étale morphism has **integral**, not necessarily finite, underlying scheme map. This convention is essential for nondiscrete valuation rings.
* Lemma 5.3.2: a microbial valuation ring R of residue characteristic zero with a fixed pseudouniformizer pi is a filtered colimit of local excellent regular subalgebras Lambda_i, containing pi, such that V(pi)_red is snc and Lambda_i -> R is local. When R is henselian, the Lambda_i can be chosen henselian. A rank-one valuation is microbial: R[1/pi]=K for any nonzero pi in its maximal ideal.
* The paragraph immediately following Lemma 5.3.2 identifies (R\{0} -> R) with colim (M_i -> Lambda_i), where M_i=Lambda_i intersect Lambda_i[1/pi]^times. These induce fs log-regular structures on Spec Lambda_i.
* Example 2.4.5: for **any** saturated monoid P and any a in P, the monoid P[e_1,...,e_n]/(sum e_j=a) is saturated; P -> P_n(a) is smooth, vertical and saturated. Thus nodal charts commute with ordinary base change as well as saturated logarithmic base change.
* Corollary 4.4.9: for any henselian valued field, the canonical valuative log scheme Spec(R\{0} -> R) has Kummer étale fundamental group equal to the maximal tame quotient of G_K. In residue characteristic zero all finite extensions are tame, so this quotient is all G_K. No discrete valuation assumption is present.

## 1. The stable model and its finite chart data

Fix a finite split marked set S in P1(L), containing 0,1,infinity, over a finite extension L/K. Write R for the henselian rank-one valuation ring of L in this paragraph. Properness of the fine scheme Mbar_0,n gives a stable marked genus-zero family X over R extending (P1_L,S), with its generic identification. Stability and this identification make it unique and compatible with every extension of valued fields.

There is also a direct finite cluster construction, which specifies all charts required below. Starting with P1_R, each cluster is separated at its next **branching** radius by blowing up an ideal (x-a,d), where d is a nonzero difference realizing that radius. The two charts have equations x-a=d z and (x-a)w=d. At a subsequent cluster, use the normalized coordinate on the current smooth component and a parameter whose valuation is the difference between the child and parent depths. Only finitely many branching depths occur in a finite marked set. Components with fewer than three special points are omitted or contracted. The result is the stable family above. At every node it has an étale chart xy=a for a nonzero a in the maximal ideal; at every mark it has a smooth chart with a horizontal coordinate z. The nodes and their branches are split because all the marks are split and the dual graph is a labelled tree.

Let M=R\{0}. The base log structure is the canonical one defined by M -> R. Equip X with its vertical boundary and the marked sections. Locally its charts over M are M itself on an unmarked smooth open, M plus N at a mark, and M[e_1,e_2]/(e_1+e_2=a) at a node. These are saturated charts; the resulting log structure is the natural compactifying log structure of the punctured generic curve. This last identification follows from AHLS Proposition 5.3.1 on the vertical part, with the disjoint smooth horizontal divisor then adjoined. The generic log-trivial locus is exactly U=P1_L\S.

## 2. Noetherian approximation with proper models

Choose a nonzero pi in the maximal ideal. Apply AHLS Lemma 5.3.2 and retain a cofinal system of henselian local excellent regular Lambda_i containing the finitely many coefficients needed to define the marked family and its finite chart cover, all gluings, and the displayed chart parameters. Ordinary finite-presentation descent gives a proper stable marked family X_i over Lambda_i whose ordinary base change is X. Properness, stability, and the finite étale chart data descend after increasing i. These conditions can alternatively be obtained by descending the R-point of the fine projective moduli scheme and its universal family.

For each finitely many nonzero node parameters a, rank one gives N with pi^N/a in R. Put both a and pi^N/a into Lambda_i. Then a belongs to M_i=Lambda_i intersect Lambda_i[1/pi]^times. On the regular snc base it is a unit times a monomial in the irreducible local equations of V(pi)_red. Include all inverses of normalized coefficient differences which are units, so sections and chart overlaps remain separated at these stages. The resulting nodal and marked charts are exactly M_i[e_1,e_2]/(e_1+e_2=a) and M_i plus N.

Consequently X_i is fs log smooth over the fs log-regular base Spec(Lambda_i,M_i), and hence is log regular (Kato's theorem cited explicitly in AHLS immediately after Lemma 5.3.2). The underlying map X_i -> Spec Lambda_i is proper. All integers are invertible, since Lambda_i may and will be chosen as Q-algebras. Its log-trivial open U_i has limit U.

For j >= i, all these charts are base changes. The nodal and marked monoid maps are saturated, so saturated and ordinary base change agree on their underlying schemes. Thus {X_i} is an **affine charted** system of qcqs saturated log schemes in the exact sense of AHLS Definition 3.4.4, with limit X. The same is true of their log closed fibres X_i,s_i: because Lambda_i -> R and all transition maps are local inclusions, the residue fields form a direct system with colimit the residue field of R. The limit of the log closed fibres is X_s with the pulled-back full valuative log structure.

Lepage Theorems 1.6 and 1.8, with all primes, give canonical restriction equivalences

    FEt(U_i) <- KCov(X_i) -> KCov(X_i,s_i).

Ordinary finite étale continuity on the left and AHLS Proposition 4.2.6 on the other two categories therefore give canonical restriction equivalences

    FEt(U) <- KCov(X) -> KCov(X_s).                       (N1)

This is the required all-prime comparison for a noncomplete nondiscrete rank-one valuation ring. No replacement of the full valuative log structure by one finite chart is made.

The construction is functorial: (N1) consists of actual restriction functors, not chosen identifications depending on the approximation. For any finite diagram of morphisms of marked models, choose common finite chart data and a common cofinal approximation; the finite-stage restriction squares commute. Taking limits gives their commutativity. Equivalently, the groupoid of extensions with a specified generic restriction is contractible by full faithfulness, so all comparison cocycles are forced.

## 3. The arithmetic base is exactly BG_L

Apply the same limit proof to the log base itself, proper over itself. It identifies KCov(S_R) and KCov(s_R) with FEt(L). This is independently confirmed for S_R by AHLS Corollary 4.4.9. Every functor in (N1) commutes with pullback of these constant covers. Therefore (N1) is over the **entire BG_L**, not a quotient and not an unspecified automorphism of it.

For a finite extension L'/L, the canonical valuative log map Spec R_L' -> Spec R_L is a finite Kummer étale map in AHLS's sense (Proposition 4.4.3); its underlying integral map need not be finite. Stable families base change as schemes, their saturated log structures base change by the displayed saturated monoids, and the comparison commutes with the actual extension L'/L. This is enough for ordinary finite Galois descent of the generic étale covers.

## 4. The supported scaling and logarithmic coherence

Choose nonzero t in the maximal ideal of the original field K, set lambda=1+t, and let F(a)=lambda a if v(a)>0, F(a)=a otherwise, and F(infinity)=infinity. The unique henselian extension of the valuation to Kbar makes F G_K-equivariant. The same case check as B.CF6 gives

    (F(a)-F(b))/(a-b) in 1+m_Kbar

for every distinct finite a,b. Thus all differences have the same valuations and initial forms; no discrete value group is needed.

Use a scalar d in L whose valuation is the radius of a cluster, chosen as a difference of marks. Use the **same scalar d** to normalize the corresponding transformed cluster, centered at F(a). The component coordinates are z=(x-a)/d, and under a contraction or refinement another coordinate w=(x-b)/e satisfies

    z=(b-a)/d+(e/d)w.                                   (N2)

Extracting a coefficient of minimal valuation produces a reduced factor which is a nonzero constant, w, or c+w. F preserves the first nonzero normalized form of each coefficient. The value-group exponent and reduced unit function in every log pullback therefore agree. Here the ghost monoids are the full valuative monoids, not integer exponents. The node smoothing parameter e/d can be taken literally the same on the two sides; any alternative choice differs by the already controlled initial-form unit. Products, quotients and reciprocal coordinates account for all charts, including a target generator vanishing identically on a contracted component.

It follows that the labelled stable special fibres have isomorphic saturated log structures over the same canonical log base and that these isomorphisms commute with every mark-forgetting contraction. The uniqueness check at a reduced node is unchanged: a possible lift difference satisfies u_1u_2=1, u_1x=x and u_2y=y, whence u_1-1 lies in (x) intersect (y)=0. On smooth opens the vertical part is fixed by the base; the horizontal divisor is a non-zero-divisor. Hence no further lift ambiguity remains.

The argument is compatible with finite valued extensions because initial forms commute with the inclusions of associated graded valued fields. Galois compatibility follows from equivariance of F and the uniquely labelled component and logarithmic maps. At a marked point a the horizontal parameter is changed by lambda or one, a principal unit of the fixed field K. The actual field K(F(a))=K(a) is unchanged, the arithmetic cusp quotient G_K(a) is identified by the identity, and horizontal inertia is preserved. Hensel's lemma provides all roots of principal units, because every integer is invertible.

## 5. The entire small étale site

Using (N1), transport finite covers of every P1_K\S and use the just-proved compatibility for nested marked sets and finite splitting extensions. The construction over BG_K follows from section 3, including all actual cusp residue extensions. The normalization-and-retained-points proof of B.CF7 then applies word for word: each quasi-compact separated étale object of A1_K is an open of the normal finite compactification of its generic finite algebra; the retained unramified points and their actual residue extensions are carried along; generic algebra maps extend uniquely; and geometric point surjectivity detects covering families. These objects form a basis of the small étale site.

The induced point bijection is F. It fixes every nonzero rational number because residue characteristic zero makes v(Q^times)=0, but moves t. It is consequently not induced by any K-morphism A1_K -> A1_K: a polynomial fixing infinitely many rational points is the identity. This is a reconstruction counterexample.

## 6. Why finite transcendence degree suffices for the coarsening

Let d=trdeg_Q K be finite and the original residue characteristic be zero. The valuation is trivial on Q. If v(a_1),...,v(a_r) are rationally independent, distinct monomials in the a_j have distinct valuations, so no nonzero Q-polynomial can vanish at them. Hence r <= d: the rational rank of the value group Gamma is finite. A strict chain of convex subgroups of an ordered abelian group gives rationally independent nonzero elements in successive quotients, so its length is at most the rational rank. There is therefore a maximal proper convex subgroup H. The ordered quotient Gamma/H is nonzero of rank one. The coarsened valuation is henselian (every coarsening of a henselian valuation is henselian), and its residue characteristic is still zero because Q^times consists of units. The rank-one result applies to the same field K.

## Review items before promotion

The substantive proof points are the use of saturated nodal charts to identify ordinary and log base change, the affine-charted hypothesis on the closed-fibre limit, and the coordinate check (N2) for every contraction. The draft makes those points explicit. The original DVR argument alone did not prove this statement; AHLS continuity and approximation are essential additions. The conclusion remains restricted to residue characteristic zero and does not settle arbitrary mixed-characteristic henselian fields.

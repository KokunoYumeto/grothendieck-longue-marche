# Independent audit of the fixed-prime cuspidal proof

Reviewer: finite_field_criteria. Date: 16 November 2026, 11:50–12:10 UTC.
This is an audit record, not a change to the aggregate outcome register.

## Outcome and files read

The following complete arguments passed this independent mathematical review:

- `agent_F/F_fixed_r_configuration_draft.tex`, the finite-cover proof of fixed-prime relative configuration exactness, formerly FF.50 and now integrated by the geometric agent as AG.41.
- `agent_F/F_fixed_r_boundary_draft.tex`, the diagonal boundary construction and transport, now AG.42.
- `agent_geometric/cuspidal_conditional_separation_draft.tex`, the conditional separation theorem AG.40.

Together they give the proposed proof of A1. The conclusion uses the relative cuspidally pro-r quotients for a single prime r different from p. It does not assume or imply injectivity of the full prime-to-p configuration fiber. The latter assertion was separately disproved in AG.39. There is no conflict between these two statements: they concern different kernels and different completions.

The review concentrated on exactness after completion, the normal-core construction, the arithmetic field of definition, the preservation of actual boundary decomposition groups, and the distinction between recognizing a point up to conjugacy and comparing its Kummer evaluation in one extension. No remaining mathematical gap was found in the stated proof chain.

## 1. Finite-cover configuration repair

### 1.1. The pro-r monodromy lemma

Let 1 -> L -> H -> B -> 1 be the discrete fiber sequence, with L a finitely generated nonabelian free group. If the image on L/[L,L]L^r is an r-group, conjugation gives a homomorphism from H to a pro-r subgroup of Aut(L^(r)). The argument does not need a splitting of H -> B and does not confuse an outer action with an action: conjugation on the actual normal subgroup L is canonical.

The proof that the automorphism kernel is pro-r is correct. For a finite r-group P, the tuples lifting a fixed ordered basis of P/Phi(P) all generate P and form a set of r-power cardinality. The automorphism kernel acts freely on that set. Thus it is an r-group. Iterated Frattini subgroups are characteristic, open and cofinal in the finitely generated free pro-r group, so the finite assertion passes to the inverse limit.

The resulting homomorphism H^(r) -> Aut(L^(r)) restricts on L^(r) to the faithful inner-automorphism map. Center-freeness of a nonabelian free pro-r group is exactly the input needed here. Hence L^(r) embeds in H^(r).

The further use of compactness is valid: a continuous injective map of profinite groups is a topological embedding. Therefore a finite quotient prescribed on the fiber is dominated by a finite quotient of the total group. The total quotient need not restrict to exactly that prescribed quotient; containment of kernels is sufficient and is what the proof uses.

### 1.2. The proper product cover

For a proper Galois étale cover a:C' -> C with group A, the complement Y of the pullback diagonal in C' x C' is an A x A cover of the configuration space. The removed components are the disjoint graphs of the deck transformations. Their disjointness follows from freeness of the deck action. The fiber is C' with the complete fiber a^(-1)(x) removed.

The exact sequence of discrete topological fundamental groups follows from the locally trivial surface fibration and the vanishing of pi_2 of the proper base curve of genus at least two. Its fiber is free of rank 2g(C')+|A|-1.

The monodromy on punctured-fiber homology is the identity on the boundary subspace because every puncture is individually labeled and complex orientation is preserved. It is the identity on compact homology because the compactified family is a product. Its action on the extension is therefore a shear in an additive F_r-vector space, an r-group. This verifies the hypothesis of the preceding lemma without asserting that the complete monodromy is trivial.

### 1.3. Normal cores and the relative quotient

Given a finite quotient Q of the relative fiber group, its cusp image R is a normal r-group and A=Q/R is a finite proper prime-to-p quotient. On the proper cover associated to A, the fiber quotient has image in R, so it is visible in the pro-r fiber completion.

Choose a finite r-index kernel J in the total group of Y dominating this fiber quotient. Taking the normal core over the finite A x A quotient preserves the property that the kernel upstairs is an r-group: the relevant quotient embeds in a finite product of r-groups. The resulting total finite quotient is an r-by-(A x A) group and consequently has prime-to-p order.

The containment J* intersect Lambda subset ker(q) is sufficient to dominate q on the original fiber. It survives completion because it is a statement in a joint finite image. Finally, the image of the total cusp kernel lies in the normal r-subgroup, so the quotient factors through the cuspidally pro-r total group. This is the key additional factorization; a quotient of the full total group alone would not suffice.

Every finite quotient of the relative fiber is therefore detected, proving injectivity. Right exactness follows from the universal property of completion and the fact that the killed relative cusp kernel lies in the second-projection fiber. Closedness of the image follows from compactness.

### 1.4. Specialization and arithmetic descent

The specialization input is for smooth proper pairs, respectively (C,x) and (C x C, diagonal), with relative normal-crossing boundary. It identifies geometric prime-to-p groups and the fiber maps functorially. Thus the characteristic relative quotients are identified as well. This is the scope supplied by SGA 1 XIII, Corollary 2.9 and section 2.10; no assertion about wild completion is imported.

For a finite-field point P, the actual arithmetic point section supplies the pullback of the second projection. The proposed map from the punctured-curve arithmetic group is an isomorphism on geometric kernels by the just-proved theorem and is the identity on G_k. The extension comparison therefore proves the arithmetic identification. There is no assumed global section of the configuration fibration.

## 2. Boundary comparison and transport

The root-stack construction is used only to produce a boundary homomorphism to the tame group, and then to the geometrically prime-to-p quotient. This is the correct target. It does not assert an extension of arbitrary wild covers.

SGA 1 XIII, Proposition 5.2 supplies extension across the complete Kummer chart after killing tame inertia; its proof already includes the necessary purity argument. The primary attached TeX was checked by the root and geometric agents. The extensions glue by uniqueness of normalization and respect increasing root orders and transverse pullback.

For the root gerbe, the assertion needed is only that inertia maps to the kernel and that quotienting by its image gives the proper base group. No premature injectivity of finite gerbe inertia is assumed. Passing to compatible root orders and then to geometric prime-to-p completion preserves this right exactness. In particular, no additional kernel from the discarded geometric base group is silently carried into the boundary image.

The image of the boundary group in the total relative group projects onto the diagonal proper group. Because the diagonal map of that proper group is injective, its remaining kernel is exactly the image of inertia. This is initially only a quotient of Z_r(1).

The quotient is the full Z_r(1): punctured-curve inertia is detected with infinite r-adic order by sending the first two free surface generators to the two standard generators of the pro-r Heisenberg group. Their commutator is 1+e_13. The proved fiber injection preserves it in the total group. Transverse intersection multiplicity one identifies this generator with the diagonal Kummer generator. This argument avoids circular use of a full boundary-injectivity theorem.

The local transverse chart maps the actual puncture decomposition group into the global boundary group. It is an isomorphism on inertia and on the arithmetic proper-point subgroup. It is therefore the complete inverse image of that subgroup in the boundary extension, rather than merely a subgroup with the same projection.

For conjugate proper sections, choose a geometric diagonal-boundary lift d of the proper geometric conjugator gamma. Conjugation by d carries the two actual arithmetic punctured groups and their cusp subgroups to one another; its first proper-coordinate action is Inn(gamma). A geometric element e in the target punctured group lifting gamma^(-1) exists because its proper geometric projection is onto. The composite Inn(e) Inn(d) is over the identity of the proper arithmetic group and takes the cusp subgroup to a target conjugate. These are precisely AG.40's hypotheses. Both elements are geometric, so no unintended change of constants or Frobenius is introduced.

## 3. Conditional separation theorem

### 3.1. Same-prime retention on every visible open subgroup

For the cusp kernel K and N=ker(K -> K^(r)), the retention argument applies to every open I containing N, not only normal or r-core intermediate covers. Take I_0=core_F(I), and then take the F-core of a finite r-quotient kernel on I intersected with I_0. The image of K downstairs is an r-group because N is already killed, and the further kernel upstairs is an r-group because it embeds in a product of conjugate r-quotients. Thus the total image of K is an r-group and kills N. This proves that all finite r-quotients of I survive.

Killing the visible cusp inertia therefore recovers the entire proper pro-r fundamental group of the smooth compactification of every such cover. Its Frobenius action is retained. The resulting integral Weil polynomial and proper point counts are exact. Cuspidal double cosets and arithmetic projections recover the missing-point counts, so the corresponding open point counts also agree.

### 3.2. Point recognition by finite sets

After extending constants to make a chosen source point rational, every open neighborhood of its transported section has full arithmetic projection and corresponds to an open target cover with a rational point. The finite sets of such rational points have the finite-intersection property because one may pass to the cover defined by the intersection of finitely many open subgroups. Compactness supplies a point on the inverse system.

A geometric lift then has an actual point decomposition subgroup contained in the transported section. Both project isomorphically to the same Galois group, so containment is equality. Surjectivity of the individual transition maps on rational points is not assumed. This distinction is necessary.

For the full proper prime-to-p group, the exceptional set used here is finite. I rechecked the attached primary Saidi–Tamagawa text, Proposition 1.8(vi), including its cofinite-prime-set hypothesis. The set of all primes other than p is cofinite, so the hypothesis applies. The point-label statement is used only outside this finite set and the two chosen cusps.

### 3.3. Central extensions, gauges, and Kummer evaluation

The cuspidally central one-point kernel is Z_r(1). Its geometric extension class is the degree-one cycle class. The Kummer construction from O(P), with its canonical trivialization away from P and its local residue, gives the extension without a configuration exactness assumption. The cusp kernel is normally generated by inertia, so geometric centralization introduces no further generators.

An extension isomorphism over the identity has multiplier one on Z_r(1), because both geometric extension classes are the same generator. The difference cocycle on the fiber product of the two extensions has residues +1 and -1. Subtracting p^e times this cocycle from the Kummer class of the rational function with divisor p^e(P-Q) kills both residues and descends to proper H^1.

Proper H^1 with coefficient Z_r(1) consists of constant Kummer classes: the geometric invariant term vanishes by Frobenius weights. A single a in k* accounts for the full remaining gauge. The proof does not assume that an arbitrary common-open cocycle is constant before its residues have been removed.

The conjugator between two point subgroups can be reduced to the cusp kernel. For a point rational over the current constant field, Saidi–Tamagawa Lemma 1.7 makes the proper normalizer equal to the point subgroup: it injects into G_k and already contains a subgroup mapping onto G_k. Dividing the conjugator by the corresponding element of the target point subgroup removes its proper projection. Conjugation by the remaining element in the central kernel changes only a coboundary. Thus the difference cocycle has zero evaluation class at every nonexceptional point.

Finally, full r-adic Kummer theory over a finite residue field detects each nontrivial r-primary root of unity. Choosing f(R)/a to be such a root avoids the finite excluded image set and contradicts the evaluations if f is nonconstant. This uses the inverse-limit Kummer class, not one finite-level Kummer class that could become divisible after residue extension.

## 4. Independent alternative proof and its scope

`agent_criteria/cuspidal_fiber_repair_draft.tex` contains a different proof of the same fixed-r configuration repair. It identifies the cusp Frattini module with F_r[[Delta]], proves a finite relative IA automorphism lemma, and applies the joint image in Aut(F_cr) x Delta x Delta. The joint image is necessary to retain the universal quotient factorization. It was read in full and approved independently by both the geometric and F agents.

The alternative remains unintegrated. The finite-cover proof above is preferable as the primary proof because it avoids the infinite cusp-module inverse limit and starts directly from discrete finite-rank fiber groups. The alternative is corroboration, not an extra hypothesis or a replacement for the boundary argument.

A simplification suggested by the F agent is valid: if a central element of F_cr acts trivially on the regular cusp module, its proper image acts trivially by left translation on F_r[[Delta]], so that image is one. The element then lies in the center of the free pro-r cusp kernel, which is trivial. This avoids an additional appeal to center-freeness of Delta.

## 5. Source-scope caution retained

The proof does not import a full prime-to-p fiber injection from the Mochizuki author versions. The apparent source-scope conflict with that statement and the conditional nature of Saidi–Tamagawa's outside-exceptional cuspidally abelian comparison are recorded separately. Stix's cited relative-completion theorem retains the full base and cannot by itself justify simultaneous completion of the base. The direct fixed-r proof is what removes that obstacle here.

The final outcome register remains the root agent's responsibility. This audit approves the displayed proof chain and keeps its quotient conventions explicit.

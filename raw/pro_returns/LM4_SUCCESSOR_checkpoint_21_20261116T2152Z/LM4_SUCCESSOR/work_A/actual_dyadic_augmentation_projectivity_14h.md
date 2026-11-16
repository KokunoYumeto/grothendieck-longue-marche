# Actual dyadic augmentation freeness from prescribed involution classes

Research proof proposed after the checkpoint14 formal freeze, 2026-11-16. This is not included in the frozen formal paper. It concerns the actual augmentation module of the negative pants extension; no finite tree or peripheral conjugator is inferred.

## Statement

Let E=F semidirect C2 be the actual full negative pants extension, with F a free profinite group of rank two. Let c1,c2,c3 represent its three involution classes, put Ci=<ci>, and assume the already proved centralizer identities C_E(ci)=Ci. Write epsilon for the orientation character. For every prime p, define

    Lambda_G = Z_p[[G]],
    P_p = direct_sum_(i=1)^3 Z_p[[E/C_i]],
    R_p = kernel(P_p -> Z_p).

Then:

1. For EVERY finite discrete E-module A, restriction H1(E,A) -> direct_sum_i H1(Ci,A) is onto, and restriction in degree two is injective.
2. R_p is a finitely generated projective compact Lambda_E-module for every p, including p=2.
3. For every p there is an actual compact module isomorphism R_p direct_sum (R_p tensor epsilon) = Lambda_E^4.
4. At p=2, R_2 is free of rank two over Z_2[[E]].

The first assertion uses Haran's prescribed-involution-class embedding theorem, rather than only high-degree torsion localization. The odd-p orientation ambiguity and the full finite-tree/marked-generation gate are not removed.

## 1. A finite head retaining the relevant centralizers

Fix a finite E-module A. Choose a finite quotient q0:E->Q0 through which its action factors. There is a finer finite quotient q:E->Q, with map Q->Q0, satisfying all of the following:

- the three ci have nonidentity, pairwise nonconjugate images in Q;
- for each i, the image of C_Q(q(ci)) in Q0 is contained in q0(Ci).

Nonidentity can be imposed with the orientation quotient. Pairwise nonconjugacy follows from profinite conjugacy separation: the conjugacy class of each ci is compact, and two disjoint compact conjugacy classes have disjoint images in a sufficiently fine finite quotient.

For the centralizer assertion, let N range over open normal subgroups contained in ker(q0). The closed sets

    X_(i,N) = {g in E : [g,ci] lies in N}

decrease to C_E(ci)=Ci. If q0(X_(i,N)) were not contained in q0(Ci) for every N, the closed sets X_(i,N) intersect q0^(-1)(Q0 minus q0(Ci)) would all be nonempty and would have the finite intersection property. Compactness would give an actual centralizer element with forbidden q0-image, a contradiction. A common finite refinement works for the three ci and for the conjugacy conditions.

This argument does not assume that centralizers in arbitrary finite quotients are already cyclic. Only their projections to the selected action head have been controlled.

## 2. Prescribed local cocycles become one global cocycle

Choose arbitrary classes xi_i in H1(Ci,A), represented by a_i in A with

    a_i + ci a_i = 0.

Form the finite split extension B=A semidirect Q. Each

    v_i=(a_i,q(ci))

is an involution. Let C be the union of their full B-conjugacy classes. Every involution of E is conjugate to one ci, so (q:B->Q,C) is a finite Inv(E)-embedding problem in the precise sense of Haran (1990), Definition1.1(4).

The actual E is real projective by the index-two free subgroup and the established self-centralizers. Haran's Proposition2.3, implication (a)->(b), supplies a homomorphism psi:E->B lifting q and sending all involutions into C. Write psi(g)=(d(g),q(g)); then d is a continuous 1-cocycle.

The image psi(ci) must lie in the B-conjugacy class of v_i, since q(ci) is not conjugate to q(cj) for j unequal i. A conjugator (a,k) between these two elements has k in C_Q(q(ci)). Its action on A is therefore either the identity or the action of ci. The usual semidirect-product conjugation formula gives

    d(ci) = k a_i + (1-ci)a.

Modulo (ci-1)A this equals a_i: if k acts as ci, its difference from a_i is itself (ci-1)a_i. Thus res_(Ci)[d]=xi_i simultaneously for all i. This proves the required surjectivity for arbitrary finite coefficients, including nontrivial actions and arbitrary primary exponents.

The finite centralizer-head refinement is the step that converts a prescribed allowed CONJUGACY CLASS into the desired local COHOMOLOGY CLASS. Omitting it would not justify the conclusion.

## 3. Degree-two injection and actual projectivity

Let eta in H2(E,A) restrict to zero on every Ci. A continuous cocycle representing eta factors through a finite quotient Q through which the A-action factors; refine Q to keep every ci nonidentity. It defines a finite extension B->Q with kernel A. Vanishing of its Ci restriction means that each q(ci) has an involution lift in B. The resulting finite real embedding problem for E has a solution by real projectivity. Its pullback extension over E splits, so eta=0.

Apply continuous Ext to

    0 -> R_p -> P_p -> Z_p -> 0.

Shapiro gives the segment

    H1(E,A) -> direct_sum_i H1(Ci,A) -> Ext1_E(R_p,A)
      -> H2(E,A) -> direct_sum_i H2(Ci,A).

The preceding surjectivity and injectivity force Ext1_E(R_p,A)=0 for every finite p-primary coefficient module A.

Here this is the compact-module projectivity criterion, not a claim about only trivial coefficients. To spell out its use: every map from R_p to a finite quotient of a finite module extension lifts because the corresponding pullback Ext class vanishes. The module R_p is finitely generated, since its restriction to F is free of rank four, as shown below. Consequently these finite lifting sets are finite. For an arbitrary epimorphism of compact modules, apply the finite lifting property to its finite quotient epimorphisms and take the compact inverse limit of the compatible finite lifting sets. Thus R_p is projective in the category of compact Z_p[[E]]-modules.

## 4. The induction sequence and the dyadic conclusion

As F-sets, all E/Ci are the regular F-set. Therefore

    Res_F R_p = kernel(Lambda_F^3 -> Z_p)
              = Lambda_F^2 direct_sum I_F
              = Lambda_F^4.

The augmentation ideal I_F is free of rank two because F is the full free profinite group of rank two. Induction gives

    Ind_F^E Res_F R_p = Lambda_E^4.

The standard tensor-induction identity identifies this module with
R_p tensor_Zp Z_p[E/F], with diagonal E-action. The augmentation exact sequence of the order-two permutation module gives the exact sequence

    0 -> R_p tensor epsilon -> Ind_F^E Res_F R_p -> R_p -> 0.

Its final map is the induction counit. It splits because R_p has just been proved projective. This proves

    R_p direct_sum (R_p tensor epsilon) = Lambda_E^4

for every p. At p=2 we do NOT split Z_2[C2] into sign eigenspaces; that would be invalid. The splitting is instead obtained from projectivity of the particular quotient module R_2.

Modulo two the orientation twist disappears. Put Rbar=R_2/2R_2 and Lambdabar=F2[[E]]. Then

    Rbar direct_sum Rbar = Lambdabar^4.

For every finite quotient E/U, reduction by its augmentation kernel yields finite modules over the finite group algebra F2[E/U]. Krull--Schmidt cancellation makes the reduction of Rbar free of rank two. The finite sets of such isomorphisms are nonempty and have the inverse-limit finite intersection property: a basis at a common finer quotient induces compatible bases at any finite collection of levels. No arbitrary prechosen bases are being retained. Compactness therefore gives Rbar=Lambdabar^2.

Lift the two resulting generators to R_2 and let f:Lambda_E^2->R_2 be the resulting map. Its compact cokernel C satisfies C/2C=0. Every finite abelian quotient of C is a finite two-group on which multiplication by two is onto; it is therefore zero. Hence C=0. Since R_2 is projective, f splits. Its kernel K is a compact direct summand; reduction modulo two is zero because f modulo two is an isomorphism. The same compact Nakayama argument gives K=0. Thus R_2=Lambda_E^2, as claimed.

## 5. Source check and scope

Primary source opened directly:

Haran, D. (1990). Closed subgroups of G(Q) with involutions. Journal of Algebra,129,393--411. https://www.tau.ac.il/~haran/Papers/closed_subgp_invs.pdf .

Definition1.1(4), printed394, defines the allowed involution-class set. Remark1.2(b), printed395, identifies this with projectivity relative to the family of order-two subgroups. Proposition2.3 and its proof, printed397--398, state and prove equivalence of real projectivity and solvability of every finite Inv(G)-embedding problem. The (a)->(b) implication uses the auxiliary finite cover of Haran--Jarden (1985), Corollary6.2; the parent independently opened that construction and its proof, printed466--467, at the primary Numdam PDF (turn760view1). CE independently read the full Haran statement and this proof (turn762view0). Retrieval references in this session: turn755view0 and turn756view0/1; independent parent reading turn757view0.

This proof closes the previously isolated actual dyadic degree-one/module-projectivity question. It supplies no finite quotient graph for the profinite tree, no free integral augmentation module at all odd primes, and no generating marked reflection triangle. The earlier odd-prime orientation-complement ambiguity therefore remains an actual recognition issue. Even successful unmarked recognition would need the separately recorded peripheral transfer.


## Addendum: the finite allowed-class cover is self-contained here

For clarity, the allowed-class embedding input can also be obtained directly from the already audited full-profinite free-product torsion theorem. Let B->A be a finite embedding problem, and let C be the prescribed conjugacy-closed union of involution classes in B. Form a finite-rank free profinite product D of one C2 for each class represented in C and a free profinite group, mapping onto B by the named involutions and sufficiently many additional generators. Every involution of D maps into C by the torsion theorem.

Let S be the preimage in D of B minus (C union {1}). It is compact. Its square-image {s^2:s in S} is compact and does not contain1: an element with square1 would be identity or an involution, both excluded by the chosen B-image. Choose an open normal U contained in ker(D->B) and disjoint from this square-image. The finite quotient D/U maps onto B, contains involution lifts of every element of C, and has no involution lying above a forbidden B-element.

Now apply real projectivity to the composite finite problem D/U->A. Every involution of E has a lift because its A-image lies under C. The resulting solution, followed by D/U->B, sends each involution into C union {1}; the nonidentity head condition excludes1. This proves exactly the allowed-class assertion needed in Section2. It does not assert a proper solution and does not identify E with D or a free product.

The parent and CE independently passed the complete actual-module proof. The new conclusion is the actual full-head dyadic freeness R_2=Z_2[[E]]^2, not merely a claim about the maximal pro-two quotient. The remaining odd-prime orientation isomorphism and finite-tree/marked-generation questions remain unproved.

Final complete parent and CE reviews: PASS. CE detailed record: work_CE/review_actual_dyadic_augmentation_14h.txt. The parent independently checked the cited primary auxiliary-cover construction as well as the complete compact-module proof. Formal integration is reserved until after checkpoint14 capture.

# Fourteenth-hour recognition audit: the odd augmentation module

Research note, 2026-11-16. This does not assert a full recognition theorem or a peripheral conjugacy theorem. The accepted A81 statement and the formal paper are unchanged.

## Exact setting

Let E=F semidirect C2 be the actual extension of a full free profinite group F of rank two by a negative peripheral involution. Let C1,C2,C3 be representatives of its three involution classes, as supplied by R1/C28. The orientation character epsilon is trivial on F and negative on each Ci. Fix an odd prime p and write Lambda_G=Z_p[[G]]. Set

    P_p = direct_sum_(i=1)^3 Z_p[[E/C_i]],
    R_p = kernel(P_p -> Z_p),

where the map is the sum of the augmentations.

## 1. Projectivity at odd primes is proved

Each permutation module Lambda_E tensor_(Z_p[C_i]) Z_p is projective: it is the direct summand Lambda_E (1+c_i)/2 of Lambda_E. The actual free augmentation resolution over F is

    0 -> Lambda_F^2 -> Lambda_F -> Z_p -> 0.

Induction to E is exact because F is open, and produces a length-one projective resolution of Z_p[E/F]. Since p is odd, this last module splits as Z_p direct_sum Z_p(epsilon). Consequently Z_p has projective dimension at most one as a compact Lambda_E-module. In the exact sequence

    0 -> R_p -> P_p -> Z_p -> 0,

with P_p projective, Schanuel's lemma therefore makes R_p projective. This argument avoids assuming a profinite tree realization or a full-category subgroup Kurosh decomposition.

The same proof cannot be copied at p=2: averaging over the Ci is unavailable, and the permutation modules need not be projective.

## 2. The exact stable orientation relation

Restriction to F identifies every E/C_i with the regular F-set. Thus

    R_p restricted to F = kernel(Lambda_F^3 -> Z_p)
                        is isomorphic to Lambda_F^2 direct_sum I_F
                        is isomorphic to Lambda_F^4.

The first isomorphism uses differences of the first two coordinates and their sum; the second uses the full free rank-two augmentation ideal. The finite-index induction identity now gives

    Ind_F^E Res_F R_p = R_p tensor_Zp Z_p[E/F]
                     = R_p direct_sum (R_p tensor epsilon)
                     is isomorphic to Lambda_E^4.

This is stronger than a numerical rank calculation. It does not imply R_p is free of rank two: the two orientation-twisted projective summands have only been shown to be complements.

For trivial coefficients and the orientation coefficient, the dimensions of Hom(R_p,F_p) are both two in our actual negative rank-two case. The first follows from E_ab=C2^3; the second follows from H1(F,F_p) carrying the negative action and the index-two Hochschild--Serre comparison. Thus these two easiest simple modules do not detect a discrepancy. They do not control other finite simple coefficient modules.

If one could prove the additional isomorphism R_p = R_p tensor epsilon, then finite quotient cancellation would give R_p = Lambda_E^2: every finite quotient has 2 R_p isomorphic to four regular modules, and Krull--Schmidt cancellation gives the half-sized isomorphism there; compactness of the finite isomorphism sets recovers the continuous isomorphism. We have not proved the additional symmetry. A duality statement, even if available, would need its exact source and target: replacing a module by its dual can exchange nonisomorphic finite simple constituents, and is not the displayed orientation isomorphism.

## 3. What low-degree cohomology still needs at p=2

For a finite discrete p-primary E-module A, the long Ext sequence of the augmentation sequence contains

    H1(E,A) -> direct_sum_i H1(C_i,A) -> Ext1_E(R_p,A)
      -> H2(E,A) -> direct_sum_i H2(C_i,A).

In particular, even injectivity of the degree-two torsion restriction only identifies Ext1 with the cokernel of the degree-one restriction. It does not make that cokernel zero. High-degree localization, the number of involution classes, and self-centralizers therefore do not by themselves supply the degree-one surjectivity required by this module route. No use of a high-degree restriction theorem at degree one is made here.

## 4. Relation to full recognition

Haran's closed-subgroup embedding into a real-free group gives an action on a profinite tree, without the required finite quotient graph. A finite quotient tree would yield the elementary graph-of-finite-groups recognition recorded in real_projectivity_recognition_recheck_12h.md. The projectivity and complement identity above do not construct such a tree or an actual generating triple of reflections. Even an abstract orientation-preserving E isomorphism with C2 amalg C2 amalg C2 would leave the separate problem of preserving the three specified peripheral subgroups.

A new bounded primary-source search reconfirmed the previously audited category distinctions. Herfort--Zalesskii's finite-order automorphism and finite graph realization conclusions are pro-p; the full closed-subgroup result of Haran is an embedding. No applicable full-category theorem upgrading the present sharp hypotheses was located. This is a record of the search outcome, not a theorem that no stronger result exists.

Primary references rechecked in this session:

- Haran, D. (1990). Closed subgroups of G(Q) with involutions. Journal of Algebra,129,393--411. https://www.tau.ac.il/~haran/Papers/closed_subgp_invs.pdf . Proposition1.4 is the embedding statement; the later real-free decomposition is pro-two.
- Herfort, W., and Zalesskii, P. (2013). Virtually free pro-p groups. Publications Mathematiques de l'IHES,118,193--211. https://www.numdam.org/item/10.1007/s10240-013-0051-4.pdf . Theorem1.1 and its automorphism consequence remain explicitly pro-p.
- Pál, A., and Quick, G. (2025). Real projective groups are formal. Mathematische Annalen,392,1833--1876. https://doi.org/10.1007/s00208-025-03145-2 . Theorem2.1 recognizes real projectivity, without the full free-product conclusion.

These sources were already audited in the project's prior recognition note. The new argument in Sections1--3 is elementary homological algebra and does not import a new external recognition theorem.

## Brief algebraic caution: even twisted duality is not orientation symmetry

This paragraph is only a finite module example, not the actual R_p of a reflection extension. Over F7 take the split group C3 times C2, with C3 characters 1,zeta,zeta^2 for zeta=2 and the two orientation signs. Give a module R the multiplicities

    C3 character       orientation +       orientation -
    1                         2                     2
    zeta                      3                     1
    zeta^2                    1                     3.

Then R plus its orientation twist is four regular modules; its restriction to C3 is four regular modules; and R dual is isomorphic to its orientation twist. Both easiest simple multiplicities are two, and its character at the nontrivial involution is zero. Nevertheless R is not two regular modules, since the four indicated nontrivial-character multiplicities differ from two. The example only explains the algebraic distinction between twisted duality and orientation invariance. C3 times C2 is not being claimed to be a permissible quotient with all the actual source hypotheses, and no actual augmentation module or full-group counterexample is produced.

The parent and CE independently reviewed the odd projectivity and complement calculation above. This module illustration does not change the unresolved actual-module or tree-realization gate. No additional finite-group census was undertaken for it.


## Subsequent actual dyadic resolution (same hour)

The low-degree obstruction isolated in Section3 has now been resolved using additional primary input, not high-degree localization alone. Haran's prescribed-involution-class embedding theorem plus the actual centralizer-head refinement gives degree-one restriction surjectivity for every finite coefficient module. The full proof in actual_dyadic_augmentation_projectivity_14h.md establishes projectivity at every prime and actual dyadic freeness. Thus Section3 remains the explanation of what the initial localization argument omitted, not a claim that this degree-one map is still unproved. The odd-prime orientation-twist and full tree/marking gates remain open. Parent and CE reviews pass.

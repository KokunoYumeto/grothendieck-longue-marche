# Canonical-image section test: an exact limitation

Research, checkpoint21 cycle, 2026-11-16. This note evaluates the proposed strategy that a nonunit canonical Fox element might force extra full section classes. It proves no new unit, generation, or peripheral-conjugacy assertion.

## 1. Actual setting

Retain the actual pure negative involution alpha and its full canonical word u from `actual_marked_Fox_unit_gate_15h.md`. Put w=u^{-1}yu and H=closure<x,w> in F. The actual identities alpha(x)=x^{-1} and alpha(w)=w^{-1} make H stable. Write E=F semidirect <alpha> and E_H=H semidirect <alpha>.

The three actual involutions

    alpha, x alpha, w^{-1} alpha

generate E_H. They lie in the three distinct ambient section classes: the last two are the local endpoints for the actual x and y cusps, transported by the actual canonical u. This is the same pure-pants section incidence used in A11/C28. No statement about the third product xw is introduced.

## 2. The canonical image already has exactly three section classes

The closed subgroup H of the full free profinite group F is projective: its p-cohomological dimension is at most one for every p. Every involution of E_H is self-centralizing, because this holds in E. The same real-projectivity criterion used in A82 therefore applies to E_H, without assuming H is a full free profinite group of rank two.

For clarity the relevant consequence of real projectivity can be proved directly with the already audited allowed-class formulation. Given finitely many pairwise nonconjugate involutions a_1,...,a_m of E_H, choose a finite quotient in which their heads are nonidentity and pairwise nonconjugate. For arbitrary bits epsilon_i use the finite extension F_2×Q→Q and allow only the conjugacy class with first coordinate epsilon_i over each selected head class. Above every other actual involution head allow either sign. The prescribed-class lifting property gives a continuous homomorphism E_H→F_2 with the selected values. Thus the evaluations on these m classes are independent, and

    m <= dim_F2 H^1(E_H,F_2) <= 3.

The final inequality follows from the three displayed generators; it does not assume their generation of E. Since all three distinct ambient classes are already represented, E_H has exactly three involution classes, and their map to the ambient three classes is bijective. Conjugacy of sections by E_H is the same as conjugacy by H: multiplying an odd conjugator by the involution being conjugated changes its orientation without changing the conjugacy.

Consequently the actual map of nonabelian pointed sets

    H^1(C2,H) -> H^1(C2,F)

is bijective. This conclusion is consistent with H being proper. It does not assert that an arbitrary weak real embedding-problem solution is proper.

## 3. The actual coset space has only the selected fixed point

Let X=F/H, with the alpha action induced by its action on F. If gH is fixed, then g^{-1}alpha g is a section in E_H in the ambient class of alpha. By the preceding bijection it is H-conjugate to alpha. Hence a suitable product of g and an element of H centralizes alpha in F. The latter centralizer is trivial, so g belongs to H. Thus

    X^alpha = {H}.

The same argument applies to each actual section class after translating its unique fixed coset. In particular a proposed obstruction based only on an additional full fixed coset or an additional full section class cannot detect failure of H=F: these additional objects do not occur in the actual canonical image.

## 4. Dyadic permutation-module formulation

Let C=ker(Z_2[[X]]→Z_2), the actual reduced coset module. The selected point H splits the augmentation equivariantly. Choose cofinal alpha-stable open normal N of F. Then X_N=F/HN is finite. For each N_0, there is a finer N for which every alpha-fixed point of X_N maps to the selected point of X_{N_0}. Otherwise compactness of the finite coset systems would supply an alpha-fixed point of X outside H.

Over Z/2^a, the reduced permutation module on X_N decomposes into free two-point orbits and the trivial summands indexed by its other fixed points. The former have zero Tate cohomology. The maps from sufficiently fine N kill all the latter classes at any prescribed finite level. The inverse system of Tate cohomology is therefore pro-zero. Passing to the compact inverse limit is legitimate: the periodic kernel/image equations have finite compact solution sets, and compatible finite-level solutions lift by the finite-intersection property. It follows that

    Tate H^j(C2,C)=0 for every integer j.

This is not a vanishing statement for C itself. The Fox criterion identifies C with the cokernel of the particular triangular incidence map, so proving Tate acyclicity does not prove the Fox element is a unit. In particular A82 projectivity/freeness and A84 twisted duality cannot turn this computation alone into generation.

## 5. Assessment of the focused attempt

The exact involution identity B=theta(B)A, the actual full two-cycle in the GT0 case, and the section-class test above yield no full-head invertibility argument. The finite-cover boundary proof still needs the actual third cusp; its inclusion cannot be obtained by treating xw as that cusp. No new primary recognition theorem was imported, no group census was run, and no formal statement or register was changed.

The resulting negative assessment is precise: extra full section classes and the associated dyadic permutation Tate groups are unavailable as obstructions to a proper canonical image. The full Fox unit and marked peripheral-conjugacy questions remain Open.

Dependencies are the already audited actual source statements C28/A11, the real-projectivity criterion and prescribed-class theorem as used with full proofs in A82, and elementary compact finite-level Tate calculations. This research note does not require a full-category free-product recognition theorem.

Primary recheck in this cycle: Pál, A., and Quick, G. (2025), *Real projective groups are formal*, *Mathematische Annalen, 392*, 1833–1876, https://doi.org/10.1007/s00208-025-03145-2. The complete publisher page was reopened (`turn924view0`); Theorem2.1 and its following sentence explicitly state the criterion and inheritance by every closed subgroup. The separate counting argument above uses the already proof-audited allowed-class construction of A82, rather than importing Scheiderer's later cohomology theorem without its dependencies.

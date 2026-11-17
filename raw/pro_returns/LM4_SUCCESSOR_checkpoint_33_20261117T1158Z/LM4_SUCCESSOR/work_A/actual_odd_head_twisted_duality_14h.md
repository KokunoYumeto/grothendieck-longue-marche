# Actual odd finite-head twisted duality: proposed recognition refinement

Research note, 2026-11-16, after checkpoint14 formal freeze. This is a calculation for the actual augmentation module, not the abstract module illustration. Its compact-module and tree consequences are deliberately limited below.

## Actual finite head and exact homology sequence

Retain the actual negative pants extension E=F semidirect C2 and its three involution classes Ci from the dyadic augmentation note. Choose an open normal K of E contained in F, and set Q=E/K. Write epsilon for its orientation character and k=F_p for an odd prime. Put

    Rbar = k tensor_(Z_p) (R_p)_K,
    A = direct_sum_i k[Q/q(C_i)],
    M = H1(K,k).

The actual compact R_p is projective by the preceding reviewed note, so Rbar is a projective k[Q]-module. Restriction of each permutation summand to K is free, because K intersects each torsion Ci trivially. The homology sequence of the augmentation exact sequence therefore gives

    0 -> M -> Rbar -> A -> k -> 0.

Thus [Rbar]=[M]+[A]-[k] in the ordinary Grothendieck group G0(k[Q]) of finite modules.

## Boundary and compact-surface modules

For each of the three base cusps, let D_j be its actual dihedral normalizer in E, and let Dbar_j be its finite image in Q. The cusp permutation module is

    C = direct_sum_(j=1)^3 k[Q/Dbar_j].

The number of these cosets is exactly the number of positive oriented boundary circles in the K-cover. Boundary homology is their permutation module tensored with epsilon, modulo its one total-sum relation. If H is the compact-surface homology quotient, then

    [M] = [H] + epsilon([C]-[k]).

This holds even when p divides the number of cusps: it is a quotient by the one diagonal total-sum vector, not an assertion that the augmentation kernel splits off.

The actual intersection form on H is nondegenerate and transforms by epsilon, so H dual is H tensor epsilon. The sign follows from the map on the surface pair, without a geometric Nielsen realization: the negative automorphism takes every oriented peripheral generator to a conjugate of its inverse. The boundary of the relative degree-two orientation class is the total sum of the oriented boundary classes; its coefficient is therefore negative. Naturality of the relative cup pairing induces the stated sign on compact homology. Positive deck transformations preserve the orientation. No unmarked group-recognition statement enters here.

## Exact finite dihedral identity and the actual incidence cycle

Let D=Dbar_j be a finite dihedral group, with the two endpoint reflection subgroups C_+,C_- and orientation epsilon. A barycentrically subdivided polygon gives the exact finite cellular sequence

    0 -> k(epsilon) -> k[D]
      -> k[D/C_+] direct_sum k[D/C_-] -> k -> 0.

The two reflection types are permitted to become conjugate, or even equal when the rotation image is trivial. The formula still holds (in the last case use the two-edge polygon). Consequently

    (1-epsilon)([k[D/C_+]]+[k[D/C_-]]) = 2(1-epsilon)[k]

in G0(k[D]): the regular module is unchanged by the orientation twist, and (1-epsilon)^2=2(1-epsilon).

Induce this identity from each Dbar_j to Q. In the actual full group the three-cusp incidence graph is the C28 triangle: each of the three global involution classes occurs exactly twice among the six local cusp endpoints. Passing to Q and summing therefore gives

    2(1-epsilon)[A] = 2(1-epsilon)[C].

G0(k[Q]) is a free abelian group on its simple modules, so cancellation of the integer2 is valid. We obtain

    (1-epsilon)([A]-[C])=0.

This is an identity for the actual marked cusp and reflection permutation modules. It is not inferred from an arbitrary module having the same dimension.

## Result and its exact limit

The modules A and C are permutation modules and hence self-dual. Combining the preceding identities gives

    [Rbar dual] - [Rbar tensor epsilon]
      = (1-epsilon)([A]-[C])
      = 0.

Thus the two actual modules have identical composition multiplicities for every odd p. If p does not divide |Q|, semisimplicity makes this an actual isomorphism

    Rbar dual = Rbar tensor epsilon.

In that semisimple case the already proved complement isomorphism

    Rbar direct_sum (Rbar tensor epsilon) = k[Q]^4

now determines every self-dual simple multiplicity. If S is self-dual, its multiplicity in Rbar equals that of S tensor epsilon, and is exactly twice its multiplicity in the regular module. Over a nonsplitting field this is 2 dim_(End_Q(S)) S, not automatically 2 dim_k S. In particular, if all simple k[Q]-modules are self-dual, Rbar is free of rank two.

Nonselfdual pairs can still carry the compensating orientation imbalance exhibited by the abstract module example. No such imbalance in an actual Rbar has been constructed. At primes dividing |Q|, the composition-factor equality has been proved, but this note does not invoke a Cartan-map theorem to identify the projective modules or assert an inverse-limit duality. In all cases this calculation stops before a finite tree, a generating reflection triangle, or marked peripheral conjugacy.

## Dependencies and preservation

The argument uses the actual surface pair and intersection form already audited in C6/C28 and A81, the C28 three-cycle incidence theorem, and the newly reviewed actual R_p projectivity. The finite dihedral identity is proved directly by its polygon chain complex. The assertion is preserved as research pending independent review; the formal checkpoint14 paper is unchanged.

Independent CE audit of the exact sequence, duality sign, dihedral identity (including rotation order one), and self-dual multiplicity conclusion: PASS. Complete independent parent review: PASS, including the actual permutation counts, signed boundary quotient, compact orientation sign, the collapsed-rotation polygon case, G0 cancellation and the precise semisimple limit.

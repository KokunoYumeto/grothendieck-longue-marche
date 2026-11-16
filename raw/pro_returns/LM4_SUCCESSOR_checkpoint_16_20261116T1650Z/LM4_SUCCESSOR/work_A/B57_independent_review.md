# Independent mathematical review of B.57

Reviewed by the Part A agent on 2026-11-16. Scope: the complete proof in `work_CE/B_common_kernel_counterexample.tex`, its precise quotient types, its actual central refinement, and its consequence for the three resolvent kernels. Verdict: the proof is sound, subject to the stated R2/central-quotient input and the cited primary Schur-multiplier fact. This review does not resolve the centralizer problem for K or the main involution questions.

## Exact retained quotient and joint image

The fifteen kernels are closed normal subgroups of the icosahedral subgroup K, stable under its conjugation, and their full five-coset collection is permuted by B. Their intersection V is therefore closed and normal in B. The cone-three filling images of K are the whole target B, because either order-three subgroup normally generates A4. The cone-two filling image is the index-three torsion-free subgroup of C3 amalg C3. Its three cusp classes receive the twelve source cusp classes in blocks of four, with exponent one. These distinctions are essential and are correctly present in the proof.

The A9 quotient retains only three cusps. Each of the fifteen filling kernels has full image A9: factorization through a cone-three filling would kill the unique target cusp, and factorization through a cone-two filling would kill all three target cusps since every block of four contains one of the nine killed source cusps. The iterated commutator of the fifteen kernels consequently maps onto A9 and is contained in V. No invalid image/intersection interchange occurs.

The sixty induced coordinate kernels are distinct because their nonzero cusp supports are the sixty distinct translates of the chosen tripod. For any chosen coordinate, iterated commutators of all other coordinate kernels isolate a surjective copy of A9 in that coordinate. Thus the induced image of K is the entire product A9^60. Normality then gives q(V)=A9^60, and this proves the exact infinite joint image C times over A5 the full wreath product, isomorphic to A9^60 semidirect C. In particular the section C used subsequently is a genuine subgroup of this actual quotient.

## The actual central refinement

For N=V intersection ker(q), the proof works in B/[N,B], not in a substitute convenient cover. The preimage of the finite perfect subgroup M=A9^60 is M# times the central kernel, where M# is the canonical image of the finite universal central cover (2.A9)^60. This universal property is valid for a central extension with an infinite profinite central kernel. The image M# is finite and perfect. Its intersection with the preimage C# of the specified section is central.

The diagonal odd-conjugation automorphism fixes the entire universal central kernel C2^60 and therefore descends through every possible coupled central quotient defining M#. It fixes M# intersection C# and commutes with C# conjugation, since that conjugation is the unique lift of the coordinate-permutation action on the perfect base. Consequently the formula eta# on M# and identity on C# defines a continuous automorphism of the actual central refinement.

The primary ATLAS A9 page and J. N. Bray's primary A9 presentation page were independently opened; both record multiplier 2 and outer automorphism group 2. The proof uses only the multiplier assertion from this finite-group input.

## Preservation of all three actual marked classes

For s and r, the regular permutation actions have only cycles of lengths two and three, respectively. Their actual defining order relations force all base cycle products to be one. Hence each is conjugate by M into the specified C section; lifting such conjugators to M# puts the actual source element into C#, where the constructed automorphism fixes it. This verifies the needed conjugacy in the actual central refinement.

For the actual cusp tau, the twelve regular five-cycles correspond to the twelve source cusp classes. Every base cycle product is either a seven-cycle of A9 or the identity. An odd transposition preserves each such A9 conjugacy class: a seven-cycle has an odd centralizer on its two fixed letters. In 2.A9, the unique order-seven lift of any seven-cycle makes conjugacy preservation true for each lift separately; multiplying by the fixed central involution handles the other lift. Both elements over the identity are fixed. The coordinate twisted-conjugacy equations are therefore solvable in the full product (2.A9)^60 before passing to M#. This is valid even when the central quotient couples coordinates. It proves conjugacy of the actual tau, with a literal conjugator in the actual refinement.

The A.3/A.34 closed-normal central criterion now applies to all three marked conjugacy classes simultaneously. It gives full peripheral automorphisms, not merely automorphisms of a finite quotient, and their action on C is exactly the identity.

## Consequences

Exact identity on C implies exact identity on all three corrected resolvent targets. The resulting multiplier-one action preserves every individual source cusp and hence the selected tripod quotient. Its action on the tripod A9 quotient is the specified odd transposition. If its tripod outer class were trivial, that A9 automorphism would be inner, a contradiction. B.10 then excludes it from K.

The finite outer A9 character is well-defined on the closed cyclic subgroup of the resulting outer automorphism: changes of a representative acting identically on A5 are inner by an element of K because A5 is centerless. R1 makes this closed procyclic subgroup torsion-free. Its nontrivial quotient C2 therefore forces a closed Z2 factor. This justifies the infinite-common-kernel assertion as well as strict containment. No conclusion about whether K itself is trivial, or about pentagon relations, is inferred.

## Sources independently opened

- ATLAS of Finite Group Representations, A9: https://brauer.maths.qmul.ac.uk/Atlas/v3/alt/A9/
- J. N. Bray, A9 presentation and group data: https://webspace.maths.qmul.ac.uk/j.n.bray/web/Pres/A9.html

The finite certificate `work_CE/code/check_common_kernel_alt9.py` and its saved output were inspected. It supplies the specified A9 generation, three seven-cycle types, outer-conjugation witnesses, the trivial simultaneous centralizer, the sixty-element tripod orbit, and the A4 normal closures. The full product and infinite joint quotient assertions are proved algebraically, not inferred from finite enumeration.

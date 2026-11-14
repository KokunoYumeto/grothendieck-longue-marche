# D.47: cyclic outer groups of arbitrary order

The proved source is `sections/D_cyclic_composite_agent.tex`. It extends D.45 from split prime-cyclic outer groups to every finite nonabelian simple group whose full outer automorphism group is cyclic. The actual sequence S -> Aut(S) -> C_M is retained; no section is assumed. The result gives equality of the complete literal generating fibres for every prescribed base conjugator over every finite base. The ordinary union over all base centralizers is also proved explicitly.

## Exact source mechanism

For an oriented surface character chi onto C_m, write j_i=chi(c_i). The intrinsic phase of a positive boundary-preserving source automorphism at c_i is in C_m/<j_i>. This quotient is forced by the actual cyclic centralizer of the primitive boundary. It is also the exact target ambiguity: if a has outer coordinate j_i and k=v*j_i, then t^k a^-v belongs to S and conjugates a to t^k a t^-k. This works for any actual lift t of the cyclic generator.

Let P be D.45.7 and T(a)=a, T(b)=ba, T(c)=c. They commute, both fix [a,b]c, and P fixes (ac)^-1. Thus P^N T^k has exact c-conjugator (ac)^-N, changes the b-character by Nj+k*chi(a), and fixes the a- and c-characters. At a prime-power factor ell^e of m where j=chi(c) is nonunit, choose a handle value a_0 which is a unit at ell, using a->ab if only the b-value is a unit. With the CRT idempotent N and k=-j/a_0 at this factor and zero elsewhere, the character change is exactly zero, while the c-phase -N(a_0+j) generates this primary component. Other boundaries are fixed.

If another boundary d supplies the unit, (J^2)^N has exact conjugators (cd)^N at c and (cd)^N d^-N at d. Their phases are N(j+chi(d)) and Nj. The latter lies in <chi(d)>, so its effective phase is zero. At a primary factor where j is already a unit, that whole component lies in <j> and fixes the target class already. These maps therefore realize all independent effective phases, retaining actual inverses and surjectivity of every source map.

Character matching is integral. Put d=gcd(m, all boundary values). The handle covectors reduce to primitive covectors modulo d. The actual elementary symplectic surface maps from D.41, with CRT parameters, match them modulo d. Their remaining difference is in the boundary ideal d(Z/m), and the actual bounding-pair translations by boundary classes correct it coordinate by coordinate. Additional based-path phases are then removed by the preceding maps.

## Actual nonsplit maps and all finite-base choices

Choose an actual t in Aut(S) above 1 in C_M, and L(a)=t^a for fixed integer representatives. The carries L(a)L(b)L(a+b)^-1 are elements of S and are never deleted. The gauge maps and intermediate injections use L(g_omega) z(p(omega)) L(g_(omega*d))^-1, so adjacent inverse factors cancel exactly. Every extending character epsilon_C:C->C_M is retained, and its target is the actual subgroup epsilon^-1(im epsilon_C).

The based Shapiro map, the intermediate injection j_C, and every boundary root/power intersection are displayed in D.47. The canonical element over h_i is an individual element of E_C, with components L(b_C(h_i,nu)); it is not asserted to be a homomorphism in h_i. Its exact conjugation transports the entire boundary intersection by one common phase. This supplies the character-preserving epimorphism bijection at every intermediate C.

For arbitrary finite bases, maps killing K_j are subtracted through the same actual epimorphism Phi:C->epsilon^-1(im epsilon_C). The map s_Phi(d)(nu)=Phi(R_nu d R_(nu*d)^-1) is an actual section over D, independent of the chosen source q_j. Its prescribed-base-conjugator difference lies in S^Omega, so it gives a bijection of the precise subtracted sets. The remaining maps have K_j-image S by simplicity.

The extension to a larger source subgroup exists exactly when it normalizes the actual K_j-kernel. Its uniqueness follows from C_Aut(S)(S)=1, and its image is the full preimage of its outer-character image. Möbius inversion on the actual subgroup interval D_* <= C <= D counts those kernels with minimal normalizer. Their distinct conjugate coordinate kernels force the full simple-product image by Goursat. The actual normalized Shapiro gauge contributes |S|^(|Omega|-1), giving equality of the complete literal generating fibres.

The ordinary union is also explicit. C_D(d_i) acts on the A-class of X_i by any lifted conjugator. Its orbit size r_i is intrinsic because different lifts differ by A. Conjugation by H_i identifies this orbit with all E-conjugacy classes above q_1(x_i). Distinct triples of A-classes give disjoint source fibres, and every one has the same cardinality by the proved theorem. Hence both ordinary fibres have size r_1 r_2 r_3 |S|^(|Omega|-1) e_0.

## Reproducible certificates

`code/a_cyclic_outer_composite.py/.out/.json` passed in the first execution (0.762 seconds reported by the command runner). It uses the existing exact word helpers in `a_relative_prop.py`, which imports `a_peripheral_count.py`.

* All forty distinct literal corrected push maps and their inverse substitutions are retained.
* Every onto one-handle/boundary character in moduli 2,3,4,5,6,8,9,10,12,15,18,20 is checked at every prime component.
* All boundary-supplier phases and their membership in the supplying boundary subgroup are checked.
* All 359268 genus-one handle/boundary characters in those moduli are partitioned under the exact symplectic and boundary-translation generators. Their orbit invariant is precisely gcd(m,a,b,c1,c2).

`code/a_cyclic_outer_nonsplit.py/.out/.json` and `_certificate.npz` passed in the first execution (0.762 seconds reported by the command runner). Its target is the actual nonsplit quotient Q16 x C3 -> C6, kernel Q8. The target group law is verified on all triples. Every element over 1 mod6 has order12 or24, so this quotient admits no section. The chosen lift has order24 and a nontrivial sixth power.

The base is Heisenberg(Z/6) of order216, with central stabilizer and36 factors. The program verifies all46656 base cocycle products, six intermediate character extensions, the actual gauge and embedding multiplications,804 nontrivial kernel carries, and6084 literal cycle-product transports. The Q8 test establishes these group identities; the theorem's simple-kernel and generation conclusions are proved separately in the text.

No mathematical formula or certificate failed. Three missing TeX backslashes and the placement of the boundary-ideal inclusion were corrected during initial drafting before the source was offered for audit. D.45 and all its artifacts were left unchanged.

## Exact remaining scope

D.47 proves every multiplier-one peripheral chief step with cyclic full outer group, over arbitrary finite bases and all specified conjugators. It retains the exact D.37 beta_Q source on P_n and the maximal pro-five quotient. It also retains an additional prescribed source with solvable kernel through the actual fibre product.

The full D.1/D.2 lift problem still requires control of all remaining chief and repeated-prime components and compatible choices across the complete profinite source. D.36's proved A6 obstruction has noncyclic outer group C2 x C2 and remains in its established scope. No unproved extension to those remaining components is asserted here.

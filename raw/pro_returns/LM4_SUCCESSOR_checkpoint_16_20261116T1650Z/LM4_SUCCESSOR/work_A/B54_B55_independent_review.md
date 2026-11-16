# Independent mathematical review of B.54–B.55

Reviewed the current sources `work_CE/B_pants_average.tex` and `sections/b_nonidentity.tex` on 16 November 2026. This review concerns the actual group construction, the transition to its first nonzero outer derivation, and the exact domains of the quotient maps. It does not replace the separately retained finite enumerations.

## Verdict

The proof chain is valid with one minor precision in the B.55 incidence paragraph: linear independence over F7 implies constancy of incidence multiplicities **modulo seven**, rather than equality as integers. This is enough for the result because the number of source cusps of a given target colour is 972, which is invertible modulo seven, and the total is 9720. The resulting coefficient is ten modulo seven for each distinct colour pair. Parent was notified of this wording correction.

No unsupported integration of a formal derivation is used. An actual arithmetic pro-seven automorphism is inserted into a genuine surface group. A fixed lift of its finite trace is obtained inside a closed pro-seven group of actual automorphisms, and R2 is applied only after actual peripheral extension and gluing have been proved.

## Detailed checks

1. **Arithmetic seed.** The non-seventh-power test makes L/k7 cyclic of order seven. The Kummer class transforms with exponent b^-2, so conjugation on its Galois C7 is b^3. Thus the derived subgroup is C7 and the maximal abelian subextension is k7. Since the complete cyclotomic extension is abelian, the chosen nonzero Kummer element extends to a multiplier-one absolute Galois element. The signed products and exponent representatives in the two cited conventions differ only by seventh powers and a rational sign, which do not change this restriction. The first coefficient is a seven-adic unit, not merely a nonzero rational seven-adic number.

2. **Primary coefficient normalization checked independently.** Opened Nakamura–Sakugawa–Wojtkowiak2017, primary published PDF, pages55–56, formulas(1.1)–(1.2): https://ir.library.osaka-u.ac.jp/repo/ouka/all/61898/ojm54_01_055.pdf. Opened Furusho2003, primary author-hosted published PDF, Section5, pages718–719: https://www.math.nagoya-u.ac.jp/~furusho/paper/SDA=NZ.pdf. Furusho's normalized Soulé element is the Kummer character divided by l^(m-1)-1, and his coefficient functional is this element divided by (m-1)!. Thus m=3,l=7 gives the stated denominator 2(7^2-1), a unit at seven. No conjecture about the full Galois Lie algebra is required.

3. **Boundary-fixed representative.** From f in gamma3, g0 is identity modulo gamma4. If g0(t)=ktk^-1, the degree-one part of k is a multiple of X+Y and may be removed by a right t-power. The remaining degree-two part is zero because a multiple of [X,Y] cannot centralize X+Y. Hence k lies in gamma3. Its leading part is -a[Y,[X,Y]], and the correction gives exactly (-aV4,aV4). The displayed non-innerness calculation is correct and excludes lower-degree inner terms because their leading term would centralize both free generators.

4. **Pair symmetry.** Substitution Z=-X-Y gives the two listed pair derivations. Their differences from the chosen seed are precisely the two indicated inner derivations. Swapping the two entries leaves the insertion derivative unchanged. Therefore every permutation of the three target cusp labels preserves the outer seed class. This is enough for comparing the geometric target markings.

5. **Insertion and coprime averaging.** Fixing the disc boundary exactly makes extension by the identity to the complement an actual free pro-seven automorphism, in positive genus as well. The Q-action supplied by a Schur–Zassenhaus complement has the required action on peripheral homology, since its outer action is the deck action and inner changes vanish on homology. The subgroup H is closed, pro-seven, Q-stable, pure peripheral and trivial modulo gamma4. Its class-four exponent-seven image is elementary abelian. For invariant v, Q and bQb^-1 are complements to W inside W semidirect Q; conjugating by W gives a genuine element of C_H(Q) above v. Thus the entire trace is retained at the actual group level.

6. **Extension to the modular relative group.** The torsion factors s,r retain their actual orders and common finite images, so the required P-conjugators follow from coprime complement conjugacy. The cusp c=tau^m is primitive, and its boundary homology class has exactly the cusp stabilizer. This proves C_E(c)=closure<tau>. The root with the specified finite image is unique because m is prime to seven. Thus the tau conjugator also lies in P, and all three frames glue with identity at other primes. R2 has its stated actual input.

7. **Original and resolvent comparison maps.** U is normal and its index in F is prime to seven, giving surjectivity U^(7) to F^(7). The exact filled images rho_±(U)=F_± give the other two surjections. Since the full lift acts identically on Q and its s/r frames are trivial in Q, each named J-torsion factor is preserved up to a U-conjugator. Hence the filling kernels and the target level-two kernels are invariant. The quotient diagrams commute. These facts justify descent of the trace; they are stronger than merely having three abstract isomorphic free groups.

8. **Outer quotient and normalization.** One can perform the computation with the raw R2 representatives, whose action on U^(7) is literally the chosen h. Later normalization to the standard gentle representative changes only inner classes. The descended automorphisms are identity through degree three because the pro-seven maps are surjective. Their degree-four first derivatives are therefore well-defined up to inner degree-three derivations. The nonzero outer class in the actual finite class-four exponent-seven quotient proves inequality of the full outer automorphisms.

9. **Positive-genus handle coordinates.** The construction retains the entire source trace, including its handle values. On the targets, homology is generated by the images of the source cusp classes; the original power five is a unit modulo seven. Evaluating on these cusp classes determines the descended derivation. No claim that arbitrary handle values vanish is needed.

10. **Scope.** B.54 provides full gentle elements outside the braid-image subgroup and outside the Galois image. B.55 supplies nonidentity witnesses for both actual resolvent homomorphisms. Neither proof imposes the pentagon, proves anything about all GT elements, or constructs an element of the full common kernel. These limitations are stated correctly.

## Editorial follow-up

B.12 in `sections/b_geometry.tex` still says that finding a nonidentity witness is undecided. Once B.55 is integrated, that sentence should point to B.55 and reserve Open for the proposed identity on all GT and the full common-kernel equality.

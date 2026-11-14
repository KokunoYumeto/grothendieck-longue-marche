# Root review of the finite-prime-support theta obstruction

The root read the complete candidate `A_finite_prime_theta_candidate.md` and independently opened the four exact primary source loci. The argument is accepted with the finite-level compact-type extension/base-change explanation retained and with “abelian tower” understood to mean covers abelian over the original curve C. It makes no assertion for arbitrary iterated abelian covers whose composite group can be nonabelian. The independent topos review is `A_finite_prime_theta_topos_review.md`.

## Mixed-primary fixed-field argument

For an S-supported point, the Frobenius orbit length has all prime divisors in S because the action on each primary part lies in its principal congruence group. If n is a nontrivial orbit length, tau=sigma^(n/ell) has order ell on the point for any prime ell dividing n. Every other r-primary component is fixed, since its tau-order is both an r-power and a divisor of ell. Thus the orbit difference T is ell-primary. The integral averaging operator is a unit modulo ell for every odd ell, including3, and gives ell*T=0. The full ell-point translated orbit then lies in the intersection of two distinct irreducible principal theta divisors. Their intersection number2 excludes it. The proof requires neither scalar Frobenius nor semisimple reduction.

If pi−1=ell*A_ell with A_ell invertible on the Tate module, the rational ell-primary kernel is exactly J[ell]. Combined with the mixed-primary lemma and theta avoidance of J[L], this excludes every S-supported theta point. This is an implication proved from the actual endomorphism, not from a determinant divisibility heuristic.

## The nonempty finite-level open

At an ordinary compact-type genus-two curve E1 union E2, a nontrivial odd torsion line bundle has either two nontrivial restrictions or exactly one trivial restriction. In the first case the normalization exact sequence gives its one-dimensional H1 as the node contribution; in the second case H1 is the ordinary elliptic H1 of the trivial component. Frobenius is bijective in both cases. The trivial line has the sum of the two ordinary elliptic H1 spaces. In a compact-type smoothing the relative Picard scheme is abelian, so its fixed prime-to-characteristic torsion level is finite etale and extends after the stated base change. Each nontrivial degree-zero character bundle has constant h0=0 and h1=1, so cohomology/base change gives line bundles and Frobenius arrows; bijectivity on the special fibre persists on a common open for the finitely many arrows. This supplies exactly the required smooth theta[J[L]] avoidance. No locally free theta sheaf on the nodal curve is assumed.

The opened generic theorem of Yang gives a compatible second justification, but neither it nor the degeneration proves one finite-field curve avoids every odd torsion order. The ordinary locus and finite-level avoidance open are geometrically irreducible opens in genus-two moduli.

## Mixed level and Frobenius realization

Deligne–Mumford Theorem5.15 is for the complete level N=L^2 over the chosen cyclotomic base. It directly supplies geometric connectedness; smoothness then gives geometric irreducibility. No independence of separate prime-adic representations is inferred. Tricanonical frames produce an actual scheme T with universal curve and GL5 fibres. Pulling it back to the level scheme gives an irreducible Y, and Y→T is the genuine Sp4(Z/N) torsor of symplectic bases. This removes the hyperelliptic automorphism ambiguity that a coarse-moduli argument would leave.

The diagonal g_ell=(1+ell,1+ell,(1+ell)^−1,(1+ell)^−1) has order ell and invertible first congruence derivative. CRT gives g of order L. Right multiplication by g^−1 is an automorphism over T and is defined over the finite base, so the specified continuous finite cyclic descent cocycle gives a genuine quasi-projective twist. It need not commute with every other right multiplication to define this descent. Lang–Weil supplies points over every sufficiently large extension; taking degree1 modulo L yields precisely g (or its inverse, depending on the convention) as the level Frobenius. Both conventions give the same invertibility and rational-torsion conclusion. Containment of the N-th roots of unity makes the Weil multiplier one, consistent with the chosen symplectic matrix.

## Entire abelian S-cover consequence

For a geometrically connected cover abelian over C, each nontrivial geometric character has a nontrivial torsion line bundle whose order is S-supported. No character lies on theta, so every Frobenius arrow is invertible and the whole cover is ordinary. All characters occur in the stable two-torsion representation, up to harmless duality, and they separate the odd abelian deck group. Thus the deck action is faithful already on geometric2-torsion. Quotients of an ordinary Jacobian are ordinary; a nonconstant map to a two-rank-zero abelian variety would give a positive-dimensional ordinary quotient inside it, a contradiction.

## Independently opened primary sources

- Deligne, P., & Mumford, D. (1969). The irreducibility of the space of curves of given genus. *Publications Mathematiques de l'IHES,36*,75–109. <https://www.numdam.org/item/PMIHES_1969__36__75_0.pdf>. Exact Jacobi-level definition5.14, Theorem5.15, and Lemma5.16, pp.108–109. The theorem treats the full composite level.
- Achter, J.D., & Pries, R. (2008). Monodromy of the p-rank strata of the moduli space of curves. *International Mathematics Research Notices,2008*,rnn053. <https://www.math.colostate.edu/~achter/math/prm0508.pdf>. Section5.1 and Lemma5.2, authorpp.17–18: tricanonical rigidification, GL_(5g−5), scheme representability and fundamental-group surjection.
- Yang, Y. (2016). *Abelian coverings of curves over Fp which are not new ordinary* (RIMS1844). <https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1844.pdf>. Definition1.2 and Proposition1.3 with proof, pp.2–3. Only generic new ordinariness is used here; no composite-order primitive-character shortcut is imported.
- Poonen, B. (2017). *Rational points on varieties* (Graduate Studies in Mathematics186). American Mathematical Society. <https://math.mit.edu/~poonen/papers/Qpoints.pdf>. Theorem7.7.1(ii–iii), p.222, and proof p.223: the fixed geometrically irreducible finite-type scheme has points over all sufficiently large finite extensions.

The theorem constrains one separation strategy and supplies no collision. Its curve may depend on S. A.C2.13 supplies the explicit single-prime illustration with successful change to degree7. The general A1 and A2 obligations remain.

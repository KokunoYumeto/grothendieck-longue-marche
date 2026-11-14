# Independent review: the general primitive-Prym criterion

**Reviewed:** audit/A_general_primitive_prym_candidate.md, Sections 1–9, 14 November 2026.

**Conclusion:** the stated all-genus, all-characteristic criterion passes independent review. The characteristic-two conclusion follows directly from the positive primitive rank computed from the complete quotient square. The odd-characteristic conclusion uses the already proved geometric genus-one quotient case A.29l, whose actual statement and finite-generation scope I read again.

## Annihilation and the controlled function

The definition \(P_n=\operatorname{im}(A)\), with \(A=\prod_{\ell\mid n}(1-\sigma^{n/\ell})\), is particularly useful here. A geometric \(p\)-primary torsion point has image in \(P_n[p^\infty](\overline K)\); this group is zero if \(f_p(P_n)=0\). This establishes the needed integral annihilation without any inference from an endomorphism's reduction modulo \(p\).

The expansion of the resulting principal divisor has \(2^{r+1}\) distinct points. The prime-order factors distinguish the subset products, and the two original deck orbits are disjoint. Consequently its positive and negative parts each have degree \(d=2^r\) and are reduced. The corresponding function is separable in every characteristic: a function with a simple valuation is not a \(p\)-th power. Thus its intermediate function-field extensions are also separable.

The controlled-field argument is the exact Poonen Proposition 2.1/Lemma 2.2/Corollary 2.3 argument already reviewed for A.C2.19. The inequality \(n>(2^r-1)^2\) also holds for the prime-power case \(r=1\), which is now included. Since \(g(D)=n(g(C)-1)+1\ge n+1\), the same contradiction excludes index one in every genus.

## The action and the quadratic quotient

The kernel of the induced odd deck action on the controlled subfield has order dividing the power-of-two extension degree \(e\), so it is trivial. The stronger freeness argument correctly uses multiplicity-weighted fibre degree. If a prime-order odd element fixed a point downstairs, its free action upstairs would partition that fibre into equal-multiplicity orbits of odd length, forcing an odd divisor of \(e\).

Hence the quotient action is free and Riemann–Hurwitz constrains the controlled curve's genus to one or at least \(n+1\). The controlled bound excludes the latter. The two-orbit support then gives \(e\le2\): a zero fibre of the descended function is reduced and has exactly \(e\) points, while each of the two deck orbits maps injectively to the quotient. Thus \(e=2\). The quadratic involution commutes with the odd deck action because its order-two group is normalized by that action. No uniqueness theorem for unrelated bielliptic involutions is used.

For \(r=1\), the controlled bound already gives genus at most zero when \(e=2\), contrary to the forced genus one. Retaining that immediate contradiction is correct; it is not necessary to manufacture a quadratic elliptic quotient in that case.

## The entire quotient square

The commuting actions have trivial intersection and give the faithful group \(G\times C_2\). It follows from the fixed-field lattice that the original curve \(C=D/G\) maps quadratically to \(E_0=Z/G\), and \(E_0\) has genus one.

For every \(m\mid n\), the fields \(k(C)\) and \(k(Z_m)\) have coprime degrees two and \(m\) over \(k(E_0)\), so they are linearly disjoint. Their compositum has the full degree \(2m\) of \(k(D_m)\). The fibre product is already smooth because it is an étale base change of the smooth curve \(C\). Therefore this is an actual Cartesian square of smooth curves, not merely an equality after a possibly ramified normalization.

This establishes \(r_m=m r_1\) for the numbers of geometric ramification points of the horizontal quadratic maps. The count is valid in characteristic two even when the different exponents exceed two: the Deuring–Shafarevich formula uses the number of ramification points, and the étale base change preserves each local quadratic extension. Riemann–Hurwitz gives \(r_1>0\), because the original quadratic curve has genus at least two and its target has genus one.

## The primitive-rank calculation

In characteristic two, all \(Z_m\) have the same two-rank \(\epsilon\), since the maps between them are isogenies. Crew's ramified Deuring–Shafarevich formula therefore gives
\[
f_2(D_m)=m r_1+2\epsilon-1.
\]
The odd-order averaging idempotents identify the \(H_m\)-invariant étale Tate module with that of \(J_{D_m}\). Pullback followed by norm is multiplication by the odd degree, hence invertible on the two-adic Tate module. There is consequently no hidden loss of integral invariant ranks.

If \(b_j\) denotes the exact conductor-\(j\) rank, then \(f_2(D_m)=\sum_{j\mid m}b_j\). The endomorphism defining \(P_n\) is nonzero precisely on primitive character summands and zero on every other summand. Its image thus has \(p\)-rank \(b_n\). Möbius inversion gives
\[
b_n=r_1\varphi(n)>0,
\]
since the constant term has zero Möbius sum for \(n>1\). This directly contradicts the hypothesis. No dimension-one character argument is used, so the calculation is valid beyond genus two.

In odd characteristic, the resulting geometrically Galois quadratic map \(C\to E_0\) has degree prime to \(p\). The actual A.29l statement covers every such genus-one quotient, over finite fields and, by its stated geometric spreading argument, finitely generated fields. This is an independent established theorem, not an illicit use of the characteristic-two Deuring–Shafarevich formula.

## Scope

The result assumes a primitive factor of zero \(p\)-rank. It does not obtain that condition from mere nonordinariness. Outside genus two in characteristic two, it does not replace that condition by meeting a theta divisor once along each character orbit: the relevant coherent-cohomology character spaces need not be one-dimensional.

The descent, finite-extension, geometric-form and proper-to-open reductions match A.3 and A.29l. I found no gap in the written criterion or in those scope qualifications.

Exact sources are the already opened Poonen (2007), author p.3, and Crew (1984), Corollary 1.8, printed pp.35–36, together with the checked statements A.3 and A.29l. Their use and precise hypotheses are recorded in the candidate and in audit/A_arbitrary_primitive_prym_topos_review.md.

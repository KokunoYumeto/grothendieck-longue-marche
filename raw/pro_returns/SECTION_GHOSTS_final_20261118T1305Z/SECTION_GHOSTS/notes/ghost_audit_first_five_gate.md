# Original factorial ghosts: the remaining first coefficient-five gate

## Status at 2026-11-18 10:06 UTC

E.205 is proved and has complete positive reviews by root and cohomology_audit. For a fixed legal minimal-shell first pair \(q_0,r_0\), consistency of E.202's finite affine system is equivalent to existence of an original-recursion continuation passing the **entire continuous coefficient-five class-three obstruction**, including the strict \(c_0\) condition. This is a coefficient-five assertion only. It is not a full class-three lift across all coefficients, and not a full pro-five section.

Put \(c_j=v_5((j+4)!)\), \(t_j=v_5(j+5)\), and \(e_j=c_j+t_j\). At stage \(j+1\), complementary old roots at \(q_j,r_j\) can be multiplied by \(\mu_{5^{e_j}}\). Their divided Kummer primitives vary surjectively modulo \(5^{c_j}\), while their central inertia variations contain \(n_j\) and vanish modulo that same power. Principal-unit retention at every earlier support place makes the whole finite central difference unramified outside five; the fixed-source \(H^1\) vanishes. Thus the central Frobenius values are already defined by the actual prefix, up to coboundaries which vanish at those Frobenii modulo \(5^{c_j}\). Extra nonzero Kummer Frobenius conditions make the remaining affine coefficients units. The resulting \(D_j\) are divisible by \(5^{c_j}\), so normalized residues have valuation at least \(c_j-t_j\), tending to infinity. Fixed-source weight-three \(H^2\) is zero, so this is genuine global obstruction vanishing.

The added nonzero Kummer conditions retain every original CRT and radical condition. At the A-prime, the desired fifth-root line of \(A_0=3q_0^{24}\) is totally ramified at three over the full cyclotomic CRT field; the required complementary radical's unique degree-five subextension is unramified there. At the B-prime the same argument uses the private valuation of \(B_0=-2r_0^{24}\) at two. Cyclotomic ramification indices at three and two are prime to five. The intersections are therefore trivial.

The proof is in sections/part_E_original_five_continuation.tex. The executed certificate code/ghost_audit_five_continuation.py and its saved outputs check 100,000 factorial indices, 19,520 root parameters and 26,040 finite affine equations. They claim no legal first pair or first-gate consistency.

## Exact first-prime and second-prime restrictions

The exponents remain \(n_0=24,n_1=120,n_2=720\). At stage zero the original old-prime set includes every prime at most \(121^4=214358881\). At each such prime \(p\), the CRT coordinates must be an actual unit solution of \(3X^{24}-2Y^{24}=1\). They have the prescribed extra congruences at primes dividing 120 and full error precision \(H_1(p)=2v_p(720)+4\). Thus a small numerical pair satisfying a few residues is not an original legal first pair.

The first prime must be in the resulting CRT class, split completely in \(\mathbb Q(\mu_{24},(-2)^{1/24})\), and exceed all original bounds. In the minimal-five-shell family it has \(q_0\equiv1\pmod{120}\) and \(q_0\equiv6\pmod{25}\). The second prime retains its actual old-root CRT class and the current residue \(r_0\equiv z_{q_0}\pmod{q_0}\), where \(-2z_{q_0}^{24}\equiv1\pmod{q_0}\). It splits completely in

\[
\mathbb Q\bigl(\mu_{120},(3q_0^{24})^{1/120}\bigr).
\]

It exceeds \(q_0\), and its minimal shell is \(r_0\equiv21\pmod{25}\). E.205 and E.208 retain all these conditions.

## What the fixed-field argument can prescribe

For a fixed legal \(q=q_0\), E.206 defines a weight-two class \(z_q\) and a weight-three class \(w_q\), both with residue one at \(q\), with \(w_q\) locally zero at five. Their degree-five fields over \(K=\mathbb Q(\zeta_5)\) have conjugation characters \(\chi^2,\chi^3\). Their joint maximal abelian subextension over \(\mathbb Q\) is exactly \(K\), so neither is lost after the full cyclotomic CRT enlargement.

The original second-prime radical has a unique degree-five subextension of character \(\chi\). The distinct characters of the order-four cyclotomic quotient prove joint disjointness from the two fixed fields. Consequently the original second-prime choice can impose simultaneously

\[
z_q(F_r)\ne0,\qquad w_q(F_r)\ne0.
\]

By E.206's transpose identities, these are the two off-diagonal entries of E.202's matrix. **One legal first prime with zero first diagonal therefore suffices**: the determinant is minus the product of those two nonzero off-diagonals, irrespective of the second diagonal. E.208 proves this conditional result; it does not prove such a first prime exists.

## Exact diagonal residue and the remaining unsuccessful step

Choose a primary generator \(\pi_q\equiv1\pmod{(1-\zeta_5)^3}\) of the selected prime above \(q\). Put \(s_a=\ell_q(\sigma_a\pi_q)\), with \(\sigma_a(\zeta_5)=\zeta_5^a\). Primary quintic reciprocity and Galois covariance give

\[
s_a=a\,s_{a^{-1}},\qquad s_4=0,\qquad s_3=3s_2.
\]

The norm identity and E.202's definition of \(U_q\) give

\[
\ell_q(U_q)=s_2+2s_3+3s_4=2s_2.
\]

Thus the sufficient first-prime condition is exactly

\[
\ell_q(3)+2\ell_q(\sigma_2\pi_q)=0.
\]

The numerator and denominator of the second term come from the same varying prime generator. The independent fixed fields used **after** \(q\) is chosen do not prescribe this value as \(q\) varies. No universal vanishing identity, fixed-field description, or applicable distribution theorem with the complete original CRT/radical restrictions has been established.

The saved exploratory code/ghost_audit_quintic_self_probe.py computes six small prime norms of elements \(a+b\zeta_5\) satisfying only \(p\equiv481\pmod{600}\) and the 24th-power condition on \(-2\). It does not check the enormous original old-prime CRT constraints, and no example is certified legal. Root's independent larger probe finds variation including a zero diagonal, again only for nonlegal examples. Neither computation proves the required prime-selection assertion.

## Primary literature inspected

Grant, D. (1996). A proof of quintic reciprocity using the arithmetic of \(y^2=x^5+1/4\). *Acta Arithmetica, 75*(4), 321–337. [Primary published PDF](https://euclid.colorado.edu/~grant/publications/quinticrec.pdf). **Verified:** Lemma 1(a)–(b), pp. 322–323, supplies primary associates and their independence modulo fifth powers; the Theorem (Kummer), p. 324, is the reciprocity law used above. It is not a prime-distribution result.

Koymans, P., & Uttenthal, P. V. (2025). Elliptic curves and spin. *Mathematical Proceedings of the Cambridge Philosophical Society, 179*, 519–539. https://doi.org/10.1017/S0305004125000428. [Opened primary published PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/12F8836B62AE3A482557F83E5E40F671/S0305004125000428a.pdf/elliptic_curves_and_spin.pdf). **Verified scope, not an applicable theorem here:** Theorem 1.2, p. 521, concerns cubic spin over an imaginary biquadratic field; Corollary 1.3, pp. 521–522, retains the specified abelian splitting conditions. The introduction pp. 520–522 distinguishes varying-prime splitting from a fixed-field Chebotarev condition. It does not establish the quintic cyclic-quartic distribution required above.

No absence-of-literature claim is made beyond this search and exact scope check. The sufficient construction stops at existence of a fully legal first prime satisfying the displayed quintic condition, or at an independent proof that E.202's affine obstruction is consistent for some fully legal first pair.

## 2026-11-18, 10:25 UTC: exact support matching and the adjointness warning

The complete saved proof of E.211 was independently read and passed. Its later-pair matrix over R = Z/5^e has reduction diag(-alpha,beta), so the first E.202 affine consistency condition is equivalent to existence of an original minimal-shell continuation matching the integral pro-five class-two point section at every support prime. This strengthens E.205; legal first-pair existence and all higher matching remain open.

The diagonal adjointness in E.206 supplies no further spin identity. With d_p = product sigma_a(pi)^(a^2), division by the rational p subtracts one from EVERY exponent. Thus the residue logarithm of d_p/p is 3 s_2 + 8 s_3 + 15 s_4 = 2 s_2, the same as that of U_p. Using a^2 instead of a^2-1 would create a false constraint involving the local epsilon correction. Even if a primary generator makes that correction zero, this calculation does not force the spin to vanish.

## 2026-11-18, 10:31 UTC: the first-system existence gate is resolved

E.213 now proves existence of a fully legal original first pair with invertible E.202 matrix, without proving or assuming a zero-spin prime. Choose two legal candidate A-primes with the same old local data. If either first diagonal is zero, E.208 applies. Otherwise use one common legal B-prime and prescribe the four fixed z/w Frobenius coordinates so the two products divided by the first diagonals are distinct. The B diagonal is identical for both pairs and cannot make both matrices singular. The joint compulsory radical over Q(mu120) has group C12 times C5 squared and maximal abelian subfield Q(mu120), which proves compatibility with the complete old CRT and both current-prime congruences. Weight-one radical characters remain disjoint from all four weight-two/three characters over the full cyclotomic CRT field.

The complete proof is in sections/part_E_two_first_primes.tex. Cohomology has independently full-read it positively. The owner-executed finite certificate is code/ghost_audit_two_first_primes.py/.out/.json. Combining E.213 with E.211 constructs an ordinary infinite-support member of the unchanged original factorial family with its unique integral pro-five class-two section matching every support point, and hence a global pro-five class-three lift. Other coefficients, class-three matching, and all-depth survival remain unproved. Earlier notes about a remaining spin condition describe the abandoned sufficient route, not the current first-system status.

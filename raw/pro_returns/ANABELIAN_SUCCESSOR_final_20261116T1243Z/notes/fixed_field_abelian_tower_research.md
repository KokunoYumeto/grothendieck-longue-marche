# Fixed-field abelian pullback tower: exact advance and missing input

16 November 2026, fourth research hour. AR.19–20 contain the proved reduction.
For the full multiplication-by-ell^n pullback of the pointed Abel curve, the
geometric deck group has rank 2g. It cannot act freely on an elliptic curve.
A scalar annihilator only needs to kill the rational lifted point difference;
the deck transformations may be nonrational. Therefore the relevant exponent
is exp J_Dn(k)[p-infinity] over the original finite field. If it is less than
ell^(gn)+1 at one level, a collision at the pointed base curve is impossible.

The first constant-deck fields have degrees m_n=m_1 ell^max(0,n-t).
Their p-parts are bounded, and the BASE Jacobian's rational p-primary
exponents are bounded there. No argument presently bounds the NEW factors.
Confusing those two assertions would leave the main step unproved.

## Literature check

Opened Bandini–Longhi, arXiv:2312.04666v3 (28 May 2025),
https://arxiv.org/pdf/2312.04666, especially Theorems 2.1, 4.10, 4.11,
and Examples 4.13–4.14. Publication metadata was also checked at
https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/jlms.70601
(Journal of the London Mathematical Society 113(6), e70601, 2026).
Their different-prime completed group algebra decomposes into unramified
cyclotomic integer rings. The convergence theorem concerns the tower-prime
adic metric, not a uniform exponent bound for the torsion prime. A product
of those rings permits coefficients with unbounded torsion-prime valuations;
finite presentation alone does not remove this issue. These results therefore
do not establish the estimate needed here.

An infinite fixed-field constant-deck abelian P-split tower is unavailable:
its abelian quotient is controlled by the finite group J_C(k). Our tower
is instead geometrically abelian with nonconstant arithmetic deck action.
The next question is whether the actual geometric Cartier/Frobenius cocycle
imposes an exponent bound absent for arbitrary completed group-ring modules.
No such theorem has been claimed or substituted for a proof.

## Exact variable-return obstruction

The criteria agent found the fixed Laurent unit A(X)=1−2X. At a primitive 3^n-th Teichmuller root, the full doubling return norm equals Phi_(3^n)(2)=1+2^(3^(n−1))+2^(2·3^(n−1)). The valuation of this unit minus1 is3^(n−1), despite the fixed degree of A and bounded two-part of the period. Over Q2(omega), the fourth-power orbit has odd length m=3^(n−1), and its partial norm is1−2^m omega, with the same growing valuation. This is an algebraic cocycle countermodel, not a Jacobian or weight-one realization. It prevents applying a one-function Tate–Voloch bound to variable-length norms.

The possible next restriction is genuine cohomological weight and global integrality, or a controlled unit-root isocrystal. A rank-one unit-root family extending over a proper parameter space might have constrained geometric monodromy. Neither extension nor overconvergence has been proved: the theta complement is open, unit-root subobjects may fail overconvergence, and the Cartier correspondence involves Verschiebung rather than the arithmetic Frobenius needed for rationality. These are research questions only.

## Subsequent geometric restrictions checked

AC43 gives both a bound for one fixed rank-one overconvergent unit-root isocrystal and a genuine two-fiber obstruction to the proposed interpolation. AG35 gives the fixed elliptic family y²+xy=x³+a over G_m/F4. Every odd m occurs as the exact parameter degree of a fiber with rational group Z/(2^(2m)) and unit-root return valuation2m. Thus geometric origin, pure weight one and prime-to-two parameter order alone do not yield the needed uniform bound. Membership in a fixed ell-primary parameter tower and realization in the Abel–Jacobi tower remain additional restrictions. No implication from this example to failure of AR20's actual estimate is claimed.

A further literature search for Washington-type different-prime class-number bounds recovered results on arithmetic constant towers and same-characteristic pro-p towers. Those do not apply to the fixed-field geometrically abelian tower with nonconstant arithmetic deck action. No such result is used as a theorem here.

## Fixed-prime refinement and the remaining distinction

AG36 now proves that the elliptic-family return valuations diverge at primitive3^n parameters. The proof uses actual finite frame torsors of ker(V^r), explicit local halving across the split multiplicative cusp, and Artin–Schreier–Witt traces. A finite monomial degree bound gives eventual splitting at each fixed torsion level; no estimate for the growth of these representative degrees with that level has been proved. Thus the result rules out a uniform return bound, including along one fixed prime-power sequence, but does not refute the weaker polynomial-in-conductor exponent bound in AR20.

For the genus-two Abel parameter system, q-Cartier sends the line-bundle cohomology at a to that at [q]a, whereas coefficient Frobenius sends it to the point F_J a. Their comparison evolves along Verschiebung V_q=F_J^(-1)[q], not automatically along arithmetic Frobenius. Artin–Schreier–Witt classifies characters for the latter. In the scalar case V_q=F_J a convergent interpolation remains possible, but finite classes can have poles along Theta; the torus monomial trace argument has no established replacement for those rational functions on the Jacobian. The overconvergent obstruction in AC43 must not be misread as excluding all convergent objects.

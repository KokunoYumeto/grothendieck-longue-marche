# Fixed-field Abel towers: the remaining arithmetic input

Status: research note. AR.19–20 and AC.42 are proved. AC.43 is a proved conditional obstruction, subject to the separately recorded independent review. No bound for the actual Jacobian tower, no universal A1 argument, and no universal A3 existence conclusion is asserted here.

## 1. The exact target

For a fixed pointed curve `(C,P)/F_q`, write `D_n=C ×_[J,[ell^n]] J`, and let `E_n` be the exponent of `J_Dn(F_q)[p^infinity]`. The full geometric deck group has rank `2g>=4`, so the scalar annihilator argument works without rational deck transformations. It suffices to prove `E_n-1 < ell^(gn)` at one level. Passing to constant-deck fields is unnecessary.

The root section correctly proves that the first constant-deck degrees have the form `m_1 ell^max(0,n-t)`. Their p-parts are bounded; this bounds the rational p-primary groups of the fixed base Jacobian. It gives no bound for new character factors of the changing Jacobians.

## 2. Why the usual cross-prime Iwasawa statements do not supply it

Bandini–Longhi, *The algebra Z_l[[Z_p^d]] and applications to Iwasawa theory*, arXiv:2312.04666v3, Theorem 2.1, identifies the cross-prime completed group ring with a product of unramified discrete valuation rings. Theorem 4.11 gives a convergence statement, not a uniform exponent bound. A single element of a product can have unbounded component valuations. Thus even cyclic finite presentation over this ring does not force bounded exponents. This is an algebraic limitation of a proposed inference, not a counterexample to a geometric class-group estimate.

Primary source opened: <https://arxiv.org/pdf/2312.04666>.

The fixed-field Abel pullbacks are only geometrically abelian Galois. Their arithmetic Galois closures incorporate Frobenius on the deck group; after an initial finite extension, the resulting group has a semidirect-product structure. It is therefore necessary to check the field and Galois hypotheses before importing results for abelian `Z_ell^d` extensions. The newer Iwasawa–Dieudonné results for pro-p towers have the wrong tower prime for this application.

## 3. What the genus-two Cartier coefficient does give

The P-rigidified Poincare family yields a rank-one coherent cohomology bundle away from its exceptional locus. The Cartier–Mumford calculation gives finite algebraic coefficient functions for its characteristic-p Frobenius maps. These functions detect whether a character's stable return has eigenvalue one modulo p. They do not determine how close a characteristic-zero unit root is to one modulo higher powers of p.

For scalar Jacobian Frobenius `[s]` with `s^2=q`, AC.35 compresses the characteristic-p return into one fixed finite etale Kummer torsor `z^(q-1)=A`. This works because `[q]=F_J^2`, and the change of basis is a `(q-1)`st power. It is a mod-p statement. A p-adic unit-root refinement would require integral/crystalline information beyond that coherent line bundle.

For nonscalar Frobenius, the rational-character periodicity condition is periodicity under the q-Verschiebung, not simply the arithmetic Frobenius on the parameter variety. The identities in the scalar proof no longer replace the long product by the norm of one Frobenius coefficient. A universal Poincare bundle does not by itself turn this correspondence into an arithmetic F-isocrystal on a fixed finite-type base.

## 4. An exact obstruction to the finite-type-only norm step

AC.42 takes the fixed function `A(X)=1-2X` and a primitive `3^n`-th root `zeta` with `zeta^(3^(n-1))=omega`, over the unramified quadratic field `Q_2(omega)`. Frobenius four has odd period `m=3^(n-1)`, and its return is exactly `1-2^m omega`. Thus the coefficient's difference from one always has valuation one, while the return's difference from one has valuation m.

The associated integral semilinear lattice has rational fixed quotient `(Z/2^m)^2`. The norm itself remains a unit; it is the norm minus one that acquires the large valuation. This example is not pure of Weil weight one: its complex norm squared is `4^m+2^m+1`, not `4^m`. It is not a Jacobian counterexample. It shows that bounded algebraic coefficients, prime-to-p torsion parameters, and prime-to-p orbit lengths are insufficient without additional geometric structure.

Files: `frobenius_norm_obstruction_section.tex`, `frobenius_norm_obstruction.py`, `frobenius_norm_obstruction_output.json`.

## 5. The exact overconvergence theorem and its limitation

Hartl–Pál, arXiv:1811.07084v3, Proposition 8.6, printed page 42, proves that a rank-one unit-root overconvergent F-isocrystal on a smooth finite-type variety has finite geometric monodromy and a tensor power is constant. This implies a bounded return-minus-one valuation on closed points whose degrees have bounded p-part, provided the return is not exactly one; the proof is included in AC.43.

Primary full proof opened: <https://arxiv.org/pdf/1811.07084>.

This theorem requires overconvergence of the object, including its connection. Etesse, arXiv:0910.4437v4, Theorem 5.4.3.5, Corollary 5.4.3.10 and Remark 5.4.3.11, printed pages 49–52, shows that the ordinary Legendre family's unit-root subobject fails that condition even though the full cohomology is overconvergent. An overconvergent Frobenius coefficient does not suffice when the connection is not overconvergent.

Primary full proof opened: <https://arxiv.org/pdf/0910.4437>.

## 6. A concrete two-fiber obstruction within the scalar example

For `C_0:y^2+y=x^5/F_16`, nonzero order-three parameters have degree two and ordinary quadratic character unit roots. The explicit order-thirteen parameter of AC.31 has degree three and an ordinary unit root alpha in a non-Galois quartic CM field, with real quadratic subfield `Q(sqrt(13))`. Every positive power of alpha still has degree four.

Consequently those two kinds of return values cannot belong to one rank-one object with finite geometric monodromy over a common connected base containing the prescribed fibers. A constant tensor power would force `alpha^(2N)=beta^(3N)` with beta quadratic. AC.43 supplies the full field calculation and its exact certificate. This does not establish that any intrinsic arithmetic unit-root interpolation exists. It instead rules out one particularly strong candidate if it is required to recover all those genuine fibers.

## 7. What remains open

A successful tower argument needs information specific to the entire geometrically defined character family. A uniform bound is not available from coherent Cartier data, an arbitrary norm cocycle, finite presentation over the cross-prime Iwasawa algebra, or the mere geometric origin of a unit-root summand. The exact return exponents of the actual Abel pullback Jacobians remain unbounded by the arguments presently available.


## 8. Genuine geometric-family growth and the fixed-prime check

AG.35 strengthens the abstract limitation: in the one fixed family `E_a:y^2+xy=x^3+a` over `G_m/F4`, every odd degree m occurs for a parameter with rational group `Z/2^(2m)`. This supplies actual integral weight-one cohomology and prime-to-two torsion parameters, but their orders are not restricted to one fixed prime. I independently reviewed its proof and primary sources.

The first fixed-prime experiment has been retained only as a finite check. Primitive3^n parameters for n1--5 have exact rational two-primary valuations2,6,8,14,14. In particular the trace-one pattern at orders3 and9 fails at order27. The halving certificate proves each listed valuation without a large field point count; it does not establish any asymptotic pattern or identify the family with an Abel pullback tower. No additional examples were pursued after this proposed pattern was resolved.

AG.36 now proves a genuine fixed-prime asymptotic statement without relying on those values: at primitive3^n parameters, the unit-root return valuations tend to infinity. For each finite2-power level, the frame torsor of ker(V^r) extends overA1/F2 and is split at0. Every such finite abelian2-torsor is an Artin--Schreier--Witt class with a finite expansion in positive Teichmuller monomials; the full primitive3^n orbit has zero trace on each fixed monomial once n is large. This proves eventual splitting at every fixed level. I independently audited the complete proof and its primary sources. It refutes a UNIFORM valuation bound even for a fixed geometric ordinary weight-one family and a fixed prime-power torsion sequence of odd F4-degrees. It supplies no growth rate and does not refute the polynomial exponent comparison required in AR.20.

The corresponding transfer to the actual genus-two character system remains unproved. Its coherent coefficient functions give a mod-p Verschiebung cocycle, not a constructed arithmetic Z_p-character. Even in the scalar case, where the parameter dynamics agrees with Frobenius, no integral unit-root family recovering all the character factors has been constructed. An Artin--Schreier--Witt description, if obtained, would have poles on the theta exceptional locus rather than a single affine-line monomial expansion. The elementary primitive-root trace cancellation therefore cannot simply be copied to the Jacobian parameter space.

## 9. A precise integral Fourier--Mukai reference

Yifei Zhao, *p-torsion etale sheaves on the Jacobian of a curve*, Journal of Algebra592(2022),64--99, author manuscript dated5November2021, was opened and read through the relevant constructions at <https://yifeizhao.com/wp-content/uploads/2022/04/mod-p.pdf>. Lemma1.4 (printedp6) requires an integrable connection and a Frobenius isomorphism to obtain an etale coefficient sheaf. Lemma2.2 and Remark2.3 (pp13--14) identify the finite Verschiebung-fixed scheme in the universal additive extension. Lemma2.7 (p16) is the Fourier--Mukai--Laumon transform for crystalline differential modules. Lemma2.8 (p17) exchanges Verschiebung pushforward with Frobenius pullback in that enhanced setting. The preceding paragraph explicitly rules out an analogous compatibility for the ordinary coherent Fourier--Mukai transform beyond the special fibre.

This is relevant positive structure for an integral formulation, but its hypotheses and parameter space do not automatically provide the desired single arithmetic rank-one object over the Jacobian's ordinary character locus. In particular, a mod-p coherent Cartier formula is not an integral connection, and the finite fixed locus for one field is not a simultaneous interpolation over all torsion orders and return periods. No exponent estimate or new collision exclusion follows merely from this categorical equivalence.

## 10. A stopped small-annihilator comparison

The retained Fermat21 spectrum also permits a free group of order63 over F64: with a primitive21st root xi, take `s=diag(1,xi,xi^5)` and the cyclic coordinate permutation tau. Then `tau s tau^-1=s^4` projectively, and the quotient has genus4. The known exponent8 of the Fermat Jacobian would meet the scalar bound `63>49`. This is not a new route beyond the relative criterion for that quotient. The normal subgroup `H=<s^3,tau>` has index3. Exact enumeration of the retained Jacobi sums shows that the ordinary characters invariant under `s^3` and under `s` coincide: six characters have trace9 and twelve have trace-9. The36 extra `s^3`-invariant characters all have trace-12. They occur in three-cycles under tau, so the intermediate cyclic3 cover has relative numerator `(1+12T+64T^2)^6` and relative class number `77^6`, which is odd. This concrete branch was stopped once that redundancy was established. The group freeness was independently checked by the geometric-routes agent.

## 11. The exact limitation of a naive dynamical Livsic assertion

The separate note `dynamical_livsic_research.md` and its exact polynomial certificate exhibit an ordinary elliptic curve and its Verschiebung for which every periodic multiplicative holonomy equals one, but the multiplier is not a rational coboundary. The obstruction is a nontrivial two-primary divisor class; it disappears in the perfection. The geometric-routes agent independently checked the full proof. This rules out the unqualified rational-coboundary inference. It neither proves nor refutes an appropriate perfected or line-bundle version, and it supplies no estimate for the actual Abel-pullback Jacobians. Even a valid corrected Livsic theorem would still need a stronger hypothesis than failure of (R): that failure only provides at least one obstructing character orbit in each cover, rather than trivial holonomy on every periodic orbit.

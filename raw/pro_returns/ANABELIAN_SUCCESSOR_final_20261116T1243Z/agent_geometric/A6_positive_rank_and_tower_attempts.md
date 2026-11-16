# Attempts after the nontrivial-cover counterexample

## Scope retained

AG.33--34 refute universal existence of a **nontrivial** odd cyclic cover with primitive p-rank zero. The prompt permits degree one literally, with P_1=J_C. The displayed supersingular curves therefore do not refute that literal variant. Its positive-p-rank residue remains open. All displayed supersingular curves already satisfy A1 by the base Jacobian test.

## 1. Why the same genus-two isogeny pencil cannot have positive p-rank

Fix an abelian surface A over an algebraically closed field of characteristic p, with p-rank f>=1. There are finitely many kernels of isogenies from A of any prescribed p-power degree p^N. This counts quotient isogenies up to target isomorphism, not arbitrary postcompositions by automorphisms.

For f=1, every isogenous quotient again has p-rank one and a-number at most one. An order-p subgroup scheme over the algebraically closed field is of type Z/p, mu_p, or alpha_p. There is at most one subgroup of each type: the etale and multiplicative ranks are one, while the alpha_p embeddings form a space of dimension at most one. Thus each step has at most three quotient kernels. Every finite p-power kernel has an order-p composition series, giving at most 3^N chains and hence finitely many final kernels. For f=2, there are p+1 etale lines and p+1 multiplicative lines, and no alpha_p line, giving the analogous bound [2(p+1)]^N. The a-number bound follows from the connected-etale and Cartier-dual decomposition of the p-torsion: the multiplicative and etale parts use up the ordinary height, leaving a local-local part of dimension at most 2-f.

Prime-to-p isogeny kernels of bounded degree are finite in number as well, since the relevant torsion is finite etale. A connected family of fixed-degree isogenies out of A is consequently constant in the quotient variety. Its polarization cannot vary continuously either: pullback puts its Neron-Severi class in the discrete Neron-Severi group of A. The positive-dimensional alpha_p pencil used in AG.33 depends on a-number two and p-rank zero. This explains precisely why replacing the supersingular elliptic product by a positive-p-rank abelian surface does not reproduce the construction.

This is retained as a route obstruction, not promoted to an additional main-paper theorem.

## 2. Higher-genus mixed slopes

A product E_ss^2 times an ordinary abelian variety has positive p-rank and at least two alpha_p directions, so the elementary finite-kernel obstruction disappears. A direct product polarization, however, stays decomposable under the alpha_p quotient: the kernel lies entirely in the supersingular factor. It does not yield a smooth genus-three Jacobian.

A prime-to-p gluing may remove that decomposability. For example, a maximal isotropic subgroup in the ell-torsion of an ordinary elliptic curve times a supersingular surface can mix a two-dimensional symplectic piece with the elliptic factor; one could then vary the alpha_p quotient on the supersingular part. An indecomposable principally polarized threefold would be a genus-three Jacobian over an algebraic closure. No complete family with all the needed theta and pointing data has been constructed here.

Even granting such a family leaves two independent failures of the AG.32 argument. Arithmetic Frobenius has an ordinary block and a supersingular block, so it is not scalar and does not preserve each cyclic torsion subgroup by a fixed integer multiplication. Also theta is now a surface: two translates intersect in a curve, so the genus-two bound of two ordered pairs per nonzero difference is unavailable. Intersecting more translates requires control of excess intersections, and theta can contain positive-dimensional abelian subvarieties in special cases. A moving family inside a fixed isogeny class alone supplies neither a uniform conductor cutoff nor a finite torsion-incidence exclusion.

An attempted bielliptic variant has the same limitation. Pullbacks of isogenies of an ordinary elliptic quotient are constrained by Deuring--Shafarevich, but a mixed cyclic character need not be stable under the elliptic involution. Passing to the composite with its involution-conjugate produces a rank-two abelian cover; Deuring--Shafarevich then constrains a sum of character ranks and does not isolate the chosen mixed cyclic factor. No assertion that all cyclic covers of an ordinary bielliptic curve have positive new p-rank has been justified.

## 3. The fixed-field scalar-annihilator tower

The scalar specialization of the group-ring argument requires no constant deck group. A collision supplies a rational class T=[Q'-P'] over the original finite field; an integer annihilator kills it geometrically, and all deck translates can be used over the algebraic closure. A free finite prime-to-p action on an elliptic curve is by translations, whose Sylow subgroups need at most two generators. Thus the obstruction applies to the full Abel pullbacks

    D_n = C x_{J_C,[ell^n]} J_C,
    G_n = J_C[ell^n](kbar) = (Z/ell^n)^(2g),

already over k, with the rational lift (P,0). Their geometric connectedness follows from the Abel map's surjection onto every geometric abelian pro-ell quotient. Root's AR.19--20 states the resulting exact condition: exp J_{D_n}(k)[p^infinity] - 1 < ell^(gn) at one level excludes a collision. I independently audited that statement and proof.

The growth of the base Jacobian's p-primary group over the fields that make decks constant is harmless: Frobenius orders are m_n=m_1 ell^max(0,n-t), so their p-parts are bounded. This does not control the new Jacobian factors and is not used as though it did.

## 4. Literature check on the exponent gap

Searches included 'function fields Z_l extension p class group bounded p not l characteristic p', 'Jacobian prime to p towers rational p torsion exponent bounded abelian covers', 'unramified Z ell towers curves p primary class groups growth', and the exact Selmer-tower title below. No applicable theorem supplying the required new-part exponent bound was found.

Andrea Bandini and Ignazio Longhi, *Selmer groups for elliptic curves in Z_l^d-extensions of function fields of characteristic p*, Annales de l'Institut Fourier59(2009),2301--2327, was opened in full at https://www.numdam.org/item/10.5802/aif.2491.pdf (retrieval turn322view0). Proposition4.3, printed pp.2311--2313, says that when the constant field does not contain its infinite Z_l extension, the only arithmetic Z_l extension of the function field is the constant extension. Its proof uses the Frobenius coinvariants of the Jacobian's Tate module. Thus the usual arithmetic abelian-tower control results do not apply directly to the geometrically abelian, nonconstant-deck Abel tower here. The paper's introduction also explicitly distinguishes the little-understood cross-prime completed group ring in its r!=l Selmer discussion.

The newly located Cais Iwasawa--Dieudonne paper concerns pro-p towers in characteristic p, rather than the prime-to-p tower needed here; it was not substituted for an exponent theorem in the present setting.

## 5. Finite-type coefficients do not bound return valuations

One proposed route was to represent Frobenius coinvariants by a finite matrix of controlled algebraic functions of prime-to-p character parameters, and use a torsion-distance or Noetherian argument to bound p-adic valuations. Arbitrary coefficients in Z_p[[Z_ell^d]] are insufficient: in its product decomposition one can place p^n in the nth component. A finite presentation alone does not prevent this.

More seriously, even a fixed degree-one coefficient function does not control an unbounded orbit product. Independently of the criteria agent, I reached the cyclotomic norm model now written and certified there as AC.42: at p=2, ell=3, the product of 1-2X around a primitive 3^n-th root's doubling orbit is Phi_(3^n)(2). Its difference from one has valuation 3^(n-1). The criteria agent also gives the q=4 version with wholly odd periods. Hence finite-type dependence at one step plus bounded p-part of the orbit length cannot yield the needed bound.

This is an algebraic cocycle, not a Jacobian Frobenius realization. Its individual multipliers are not pure of weight one. Separate-level purity alone is also insufficient: the ordinary Weil polynomial X^2-X+4^m has a 2-adic unit root beta with v_2(beta-1)=2m. Such separate Weil polynomials do not form a demonstrated compatible fixed-curve tower. The remaining requirement must exploit compatibility coming from one curve, its polarization, or its specific Cartier correspondence.

The universal Poincare bundle does parameterize finite-rank coherent character cohomology. Its one-step p-Frobenius maps compare the fibres at a and [p]a; equivalently one obtains a Verschiebung correspondence after factoring relative Frobenius. Rationality is controlled by the arithmetic Jacobian Frobenius orbit instead. These dynamics align in the scalar case used in AG.32 and the criteria agent's norm torsor, but not for an ordinary or mixed-slope Jacobian. An algebraic isogeny correspondence does not automatically become a bounded-degree arithmetic Frobenius determinant. No such comparison has been proved here.

## Current stopping point for this route

The nontrivial primitive-cover counterexample, its exact finite count, and the pointed hyperelliptic refinement are complete. Literal A6 on positive-p-rank curves and the universal exponent estimate in AR.20 remain open. The next useful step would have to control the actual iterated Cartier/unit-root return from one fixed curve, or supply a different geometric correspondence with genuinely separating rigid targets. Repeating finite censuses or reducing the e19 parameter bound would not resolve this obstruction.
# Further geometric constraints on the return problem (09:45 UTC)

The exact cocycle in AC.42 does not have Weil weight one: for the return U=1−2^m omega one has |U|²=4^m+2^m+1, whereas the required squared modulus over F_(4^m) would be 4^m. This excludes that particular spectrum from curve cohomology. It does not turn separate-level purity into a bound: the integral ordinary Weil polynomial X²−X+4^m has unit root beta satisfying v2(beta−1)=2m. No fixed curve or compatible tower realizing this sequence has been supplied.

There is an exact sufficient additional hypothesis. A rank-one unit-root **overconvergent F-isocrystal** has a tensor power which is constant (Hartl–Pál, arXiv:1811.07084v3, Proposition8.6, printed42). If its constant Frobenius is b and its return at a degree-m point is U, then U^N=b^m for a fixed N. Under weight one b is not a root of unity. For degrees m with bounded p-adic valuation, v_p(b^m−1), and therefore v_p(U−1) when U is close to one, are bounded. The elementary fixed-unit valuation argument supplies the last step; no uniformity in a varying isocrystal is asserted.

The missing premise cannot be taken from overconvergence of full R¹. Etesse, arXiv:0910.4437v4, Corollary5.4.3.10 (printed51–52), proves that the ordinary Legendre family's rank-one unit-root subobject is not overconvergent although full R¹ is. Remark5.4.3.11 further distinguishes an overconvergent Frobenius matrix from an overconvergent F-isocrystal: the connection may fail to be overconvergent. Thus a finite algebraic one-step coefficient, or overconvergence of the full geometric cohomology, does not establish the sufficient condition.

Both primary PDFs were opened and the exact passages read. The Poincaré coherent-cohomology family by itself is not a verified rank-one overconvergent F-isocrystal parametrizing these arithmetic returns. In particular, coherent Frobenius moves a line-bundle label by multiplication by p, while descent of a cover is controlled by the actual Jacobian Frobenius. No identification of these operations has been established in the general nonscalar case. The precise remaining target is a bound exploiting the compatibility of the **actual fixed Abel tower**, stronger than finite-type coefficients, separate-level purity, or arbitrary integral semilinear-module structure.



# Review after the A1 proof (2026-11-16, 12:00 UTC hour)

AG.40--42 now prove A1. This supersedes the earlier collision-open wording; it does not construct a relative-class-number witness or a primitive-rank-zero cover. The numerical exponent estimate discussed above remains a separate existence/growth question.

## A5: supersingular targets are still a stronger existence assertion

The point-separating-target part of A5 now follows by the identity cover and the identity map, since every curve is in the no-collision class. The demand for a prime-to-p unramified correspondence to a positive-genus supersingular curve remains stronger. A nonzero supersingular isogeny factor in the Jacobian of some allowed cover is enough for one nonconstant map to a supersingular elliptic curve, after a finite field extension; jointly separating all points is an additional requirement. The exact fixed-cover spectral test inserted after AG.1 decides the factor question for a specified cover, but does not produce such a cover.

We reopened Bogomolov--Tschinkel, Unramified correspondences (arXiv math/0202223), Theorem1.7, Lemma2.3 and Corollaries2.4--2.5. Their all-hyperelliptic statement is for p>=5, while the general universal-cover assertion is posed there as Conjecture2.6. The controlled prime-to-p version already established in AP-A.17--18 uses a double-cover construction and handles odd characteristic, including p=3, in its stated hyperelliptic/elliptic-quotient cases. It is not a theorem for arbitrary curves.

A characteristic-two replacement by a degree-three supersingular elliptic map was examined. A generic degree-three map from an elliptic curve to P1 has S3 Galois closure and a quadratic resolvent. Matching the wild quadratic local extensions after a base change can make the degree-three pullback unramified. That does not make its geometric Galois closure prime to two: unless the global quadratic resolvent is already contained in the base field, the residual S3 closure still has an unramified quadratic quotient. Local ramification cancellation alone does not eliminate this quotient. In the proposed construction from a ramified double cover of an elliptic curve, the global quadratic-resolvent equality is not supplied by choosing torsion branch values. This is the exact obstruction to using that attempted char2 repair. No correspondence is claimed from it.

A direct tame construction does give limited cases: in char2, a map C->P1 with three distinct branch values whose every ramification index is divisible by an odd n can be pulled back against x^n=y(y+1). The resulting normalized cover of C is etale by tame ramification cancellation and has cyclic degree dividing n; the target has 2-rank zero. Supersingularity of this particular target requires additional conditions (for example n divides 2^r+1), so this does not resolve the universal supersingular assertion. It is recorded as a route, not promoted to a new main theorem or used to replace the missing universal case.

## A6: why the positive-rank residue has not been removed

The positive-rank mixed-slope isogeny-family attempt remains at the two independent gaps described above: realizing a useful indecomposable Jacobian family, and controlling all primitive conductors without scalar Frobenius or the genus-two two-point theta-intersection bound. Passing to an Artin--Schreier ramified cover of the known supersingular counterexample can create positive p-rank, but arbitrary odd cyclic characters on that cover need not descend; the Deuring--Shafarevich formula then constrains sums of character contributions rather than the individual primitive factor. No implication transporting the counterexample has been proved.

We also rechecked the generic-ordinarity literature. Ozman--Pries, Ordinary and almost ordinary Prym varieties, arXiv1502.05959, treats every cover at each fixed prime degree on a generic p-rank stratum. Applying these open conditions for finitely many degrees is legitimate. Intersecting them for every degree does not produce a point over the countable field Fbar_p. Yang's RIMS1844 theorem that a curve over Fbar_p has a non-new-ordinary cyclic cover supplies a nonordinary factor, not primitive p-rank zero or nilpotence in every primitive orbit. Neither theorem closes the literal degree-one-permitted A6 question for positive-p-rank curves.

No new universal A5 or literal positive-rank A6 theorem was obtained during this review. A useful next step would require a genuine global prime-to-p correspondence construction, or a finite all-conductor obstruction for a positive-p-rank curve. Further isolated witnesses, larger censuses, or refinements of the already explicit supersingular counterexample would not resolve either gap.


## Last source check: tame Belyi maps do not supply the missing correspondence

Kedlaya--Litt--Witaszek, Tamely ramified morphisms of curves and Belyi's theorem in positive characteristic, arXiv2010.01130v2, Theorem1.5 (printed pp.2--3), was opened directly at https://arxiv.org/pdf/2010.01130 (retrieval turn630view1). For a smooth projective geometrically irreducible curve over a field algebraic over F_p, it gives a finite separable tame map to P1 branched only at 0,1,infinity, over that field. This includes characteristic two. The theorem neither bounds the global monodromy group to have prime-to-p order nor forces every ramification index over selected branch values to be divisible by the indices of a chosen supersingular target cover. Tameness of inertia alone is insufficient for either statement. Thus it cannot be substituted for the missing prime-to-p unramified correspondence.

The direct Bertini alternative on C times a supersingular target X0 also has a geometric obstruction. For a smooth curve D in the product, with projection degree N to C and M to X0, adjunction gives the total ramification degree over C as D^2+M(2g(X0)-2). A smooth ample divisor has D^2>0, so its projection cannot be etale when g(X0)>=1. Singular images followed by normalization would require a precisely controlled singularity correction; ordinary Bertini does not provide it. This observation is retained only as a failed route, not as a general nonexistence claim.

The old real-Frobenius-eigenvalue question was also opened directly at https://mathoverflow.net/questions/22672/does-every-hyperbolic-curve-over-a-finite-field-have-an-etale-cover-with-a-real/22708 (retrieval turn630view0). Its 2010 answer explicitly offers a speculative automorphic strategy and notes an unresolved injection step; it is not used as a theorem or as proof of current open status. Searches for later supersingular-factor and unramified-correspondence results did not yield an applicable universal theorem with the required prime-to-p Galois-closure condition.

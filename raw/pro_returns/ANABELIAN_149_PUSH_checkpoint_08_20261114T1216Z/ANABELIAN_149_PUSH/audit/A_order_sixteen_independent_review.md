# Independent adversarial review of the order-sixteen exclusion

Date: 2026-11-14. Reviewer: degeneration agent. Candidate reviewed: audit/A_order_sixteen_candidate.md, code/A_cubic_order_sixteen_candidate.py, and its JSON certificate. Those files were read without modification or execution of the candidate generator.

## Decision

**The candidate passes this independent review in its stated scope.** For the ordinary cubic auxiliary whose symmetric elliptic branch pair has exact order three, a non-Weierstrass value γ(P) cannot have exact order16. The geometric reduction includes every possible such point, and the universal polynomial certificate eliminates every coprime rational parametrization. No additional hypothesis on the parameter beyond those stated is needed.

The independent verifier code/A_order_sixteen_independent_review.py uses separate carryless binary polynomial arithmetic over F₂[v] and its fraction field, without SymPy. Its output is code/A_order_sixteen_independent_review.json. It independently expands the reduced norm identity and verifies every saved universal Bézout identity, the admissible denominator loci, the combined parameter obstructions, irreducibility of the exceptional degree-four polynomial, the exceptional-field Bézout relation, and the shared root of M and N. These are exact symbolic checks, not sampling at selected parameters.

This conclusion does not exclude orders32 and higher. It also does not remove the exact-order-three hypothesis on the elliptic branch pair.

## 1. Normalization and the principal divisor

The elliptic equation y²+y=x+a/x becomes Y_E²+xY_E=x³+ax after Y_E=xy. Its third division polynomial in characteristic two is x⁴+x³+a². Thus a point with x-coordinate b has exact order3 precisely when a²=b³(b+1), subject to the nonzero branch-point hypotheses already present. Here b≠0,1, since a≠0. Scaling the cubic coordinate by a cube root of b gives

\[
Y^2+HY=\beta H^3+\alpha H,\qquad
H=z^3+1,\quad \beta=b,\quad \alpha=a/b,
\]

and α²=β(β+1), β≠0,1. With β=t², perfection gives α=t²+t uniquely. A further fourth-root choice r=v⁴ with r²=t is exhaustive over the algebraic closure and gives β=v¹⁶, so the admissible parameter locus is exactly v≠0,1.

The cubic auxiliary has genus4, z has pole order2 at the unique point at infinity, and Y has pole order9. The affine model is smooth: away from H=0 its Y-derivative is nonzero, and at a root w of H the z-derivative is αw²≠0. Thus there is no hidden finite singularity affecting the divisor or function-space calculations.

If γ(P) has exact order16, its eightfold multiple is one of the nonzero Prym two-torsion classes [W_i−W_j]. This uses the previously established identification A[2](kbar) with the even-subset space on the three finite Weierstrass points. In particular P is not fixed by the cubic deck transformation, so its finite coordinate p is nonzero, and non-Weierstrassness gives p³≠1.

A function h with divisor 8P+W_j−8δP−W_i exists by the torsion relation. Multiplication by (z−ζp)⁸(z−w_i) gives exactly

\[
8P+8\iota\delta P+W_i+W_j-18\infty.
\]

There is no collision among the indicated fibres: p≠ζp and neither is a Weierstrass coordinate. The function space L(18∞) has basis z^j for 0≤j≤9 and z^jY for 0≤j≤4. These fifteen functions have distinct pole orders of the two parities, and Riemann–Roch gives dimension18−4+1=15. Hence its numerator has the asserted form A+BY.

Pushing this divisor through the hyperelliptic map gives the norm equation

\[
A^2+HAB+FB^2=KU^8V.
\]

The coefficient of z¹⁸ forces degA=9. At z¹⁷ the square A² contributes nothing, HAB has degree at most16, and FB² contributes βB₄²; the right-hand coefficient is K≠0. Therefore degB=4. This argument does not assume the degree bounds are attained in advance.

The gcd assertion is also exhaustive. At a nonbranch root of a common factor of A and B, the numerator would vanish at both points of the hyperelliptic fibre, whereas its zero divisor contains only one point over each of p and ζp and no point over any other nonbranch coordinate. At W_i or W_j a common polynomial factor has order at least2, whereas the required multiplicity is1. No zero is allowed at the third Weierstrass point. Thus gcd(A,B)=1.

Scaling z by the omitted cube root preserves H, F, and the deck action and makes the omitted root1. Then V=z²+z+1. At the two roots of V the norm identity forces A=0, so A=VC. The rational function X=C/B is reduced, and division by VB² gives the claimed equation with L=√K U⁴/B.

## 2. Riccati reduction without lost rational solutions

Differentiating the reduced norm equation uses V′=1 and H′=z² and gives

\[
HX'=X^2+z^2X+\beta H^2+\alpha.
\]

If X had a pole of order h>0 at a root of H, the left side would have valuation at least−h, whereas X² would have valuation−2h, strictly below the valuations of all other terms. Cancellation is impossible. Consequently X is regular at all three roots of H; since X=C/B is reduced, B is coprime to H.

For e,η∈F₂ and c²+c=t+η, direct expansion gives

\[
X_0=tz^3+ez^2+cz+c+\eta.
\]

The z² coefficient in the Riccati identity reduces to c²+c+η=t, and its constant coefficient reduces to c. There are exactly eight such polynomials. At each root w of H the value of a solution satisfies X²+w²X+α=0, which has exactly two distinct roots because w≠0. Distinct X₀ polynomials cannot agree at all three roots: their difference has degree at most2. The eight polynomials therefore realize all eight combinations of these local values. This proves that the choice matching X at all H-roots always exists.

The displayed L₀ follows from the reduced norm expression and r²=t. Its independence of the two possible c-values is consistent: replacing c by c+1 changes X₀ by z+1, and

\[
V(z+1)^2+H(z+1)=0.
\]

Let u=X−X₀. If u=0, reducedness would make B constant, contradicting degB=4. Otherwise the difference equation is Hu′=u²+z²u, whence

\[
\left(\frac{1/u}{H}\right)'=\frac1{H^2}
=\left(\frac z{H^2}\right)'.
\]

The kernel of d/dz on kbar(z) is kbar(z²), which equals the square subfield because kbar is perfect. Therefore there is a rational R such that

\[
u=\frac{H}{z+R^2}.
\]

This gives every nonzero rational solution u. It imposes no polynomiality assumption on R. Squaring the asserted formula for L−L₀ gives V u²+Hu because V+z=(z+1)², so that formula is forced by injectivity of the square map.

Write R=M/N with coprime polynomials and N≠0. For D=M²+zN² one has D′=N² and gcd(D,N)=1, hence D is squarefree. If a root w of H were also a root of D, cancellation of their simple factors in HN²/D would give u(w)=H′(w)=w²≠0, contradicting the chosen agreement X(w)=X₀(w). Thus gcd(D,H)=1. The denominator D of u is consequently reduced and remains the reduced denominator after adding polynomial X₀. No exceptional cancellation at an H-root or at a root of N is omitted.

Since the reduced denominator of X has degree4, so does D. The leading terms of M² and zN² have different parities and cannot cancel. It follows that degM=2 and degN≤1. After scaling M,N simultaneously, M is monic; after scaling the original numerator by a constant, B=D is monic. The coefficient at z¹⁷ now gives K=β. These scalings preserve X and L and all rational identities.

## 3. Completeness of the four finite coefficient systems

Writing M=z²+m₁z+m₀, N=n₁z+x, and L₀=tz⁴+ℓ₃z³+ℓ₂z²+ℓ₁z+b, direct expansion of

\[
L_0(M^2+zN^2)+H((z+1)N^2+MN)
\]

gives the z⁷ equation tn₁²+ℓ₃=0, and the z⁶ equation

\[
tm_1^2+\ell_3n_1^2+\ell_2+n_1^2+n_1=0.
\]

In characteristic two the square map is injective, so these determine n₁,m₁ uniquely. They give exactly the four table entries in the candidate. In each case n₁≠0 on v≠0,1.

For clarity, the z¹ coefficient before eliminating m₀ is

\[
C_1=\ell_1m_0^2+(b+1)x^2+m_1x+m_0n_1.
\]

When ℓ₁=0, this is a linear equation in m₀ with nonzero coefficient n₁, giving the first formula. When ℓ₁=1, the combination ℓ₂C₁+C₂ is linear in m₀, where C₂ is the z² coefficient. Its coefficient ℓ₂n₁ is nonzero because ℓ₂=v⁴+1. This gives the second formula. Requiring C₂=0 then also forces C₁=0. Thus the division in either branch is legitimate at every admissible parameter.

The z⁵,z²,z³ coefficients are precisely P₀,P₁,P₂. The right side tU⁴ has only degrees8,4,0 and satisfies C₄²=tC₀, giving P₃. These are necessary equations for every original solution. It is not necessary to prove that they alone reconstruct a valid point: eliminating all coprime solutions of this larger necessary system suffices.

The independent verifier re-expands the complete expression over the rational function field using the four explicit table entries, obtains all these coefficients, checks the solved z⁷,z⁶ equations, and checks the appropriate exact linear elimination identity for C₁. It also compares the resulting Pᵢ and m₀ with the serialized candidate polynomials.

## 4. Universal Bézout identities and the exceptional parameter

Every denominator in the necessary equations is supported at v=0 or v=1; the independent verifier checks this by division by v and v+1. Thus the equations and all specializations used below are defined on the whole admissible parameter range.

The saved identities UᵢP₀+WᵢPᵢ=dᵢ(v), with polynomial Uᵢ,Wᵢ, were independently checked by exact rational-function polynomial multiplication. A simultaneous root of P₀,P₁,P₂ at any admissible parameter forces both dᵢ to vanish. Removing factors supported at v=0,1 therefore preserves the required vanishing. The two additional saved polynomial Bézout identities give combined obstruction1 in cases(0,0),(1,0),(1,1), and Φ₅(v)² in case(0,1), where Φ₅=v⁴+v³+v²+v+1. Hence the only possible parameter locus is exactly the nontrivial fifth roots.

The polynomial Φ₅ has no linear factor and is not divisible by the only irreducible quadratic over F₂; it is therefore irreducible. Its quotient is F₁₆. The independent arithmetic verifies the saved identity expressing x+v³+v as a combination of P₀,P₁,P₂ in that field. Thus every surviving x equals v³+v. The additional divisibility of P₃ is checked, but is not needed for the contradiction.

Reducing the actual rational formulas for m₀,m₁,n₁, rather than assuming their stated values, yields

\[
n_0=v^3+v,\qquad n_1=v^3,\qquad
m_1=v^2+v,\qquad m_0=v^3+v+1.
\]

At z₀=v³+1 both N(z₀) and M(z₀) vanish. The verifier checks this in F₁₆. Every root of Φ₅ is an embedding of this same field, so this calculation covers every conjugate exceptional parameter. It contradicts the coprimality built into R=M/N. The apparent exceptional solutions are precisely nonreduced parametrizations and cannot come from an original order16 value.

## Consequence and limit

The order16 exclusion can therefore be promoted under the exact-order-three branch hypothesis. Together with the existing order2,4,8 exclusions and the twisted Frobenius argument, it extends the sufficient residue test to λ modulo32 lying outside the reduction of μ₆. If the normalized unit is not ±1 modulo4, squaring gives valuation2 as before. Otherwise a choice of sign makes it1 modulo4, and being outside μ₆ modulo32 gives valuation2,3,or4. This bounds every packet value by order16 and the exclusions leave the Weierstrass packet.

The higher-order case remains separate. The Riccati parametrization remains valid, but at order32 the reduced denominator can have degree12, with degM=6 and degN≤5. The degree-four elimination proved here cannot be substituted for that larger system.

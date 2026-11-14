# Proved order-sixteen exclusion for cubic order-three auxiliaries

Status: proved and integrated as A.29g after independent conceptual review by root and a separate binary-polynomial verification by the degeneration agent. The historical filename is retained for provenance. The statement is that, for the cubic ordinary elliptic auxiliary whose symmetric branch pair has exact order3, no non-Weierstrass γ(P) has exact order16. The argument uses a rational Riccati parametrization, followed by universal polynomial identities. It does not sample the parameter field. The independent review and certificate are audit/A_order_sixteen_independent_review.md and code/A_order_sixteen_independent_review.py/.json.

## 1. The norm equation and its reduced numerator

Use the normalized equation from A.29e:

\[
 Y^2+H Y=F,\qquad H=z^3+1,\qquad
 F=\beta H^3+\alpha H,
\]

where β≠0,1 and α²=β(β+1). The latter relation follows from exact order3 of the elliptic branch point. Write β=t² and choose r with r²=t. Then α=t²+t and β=r⁴.

Assume γ(P) has exact order16. Its eightfold multiple is a nonzero Prym two-torsion class [W_i−W_j]. Scale the coordinate by the omitted cube root so that the omitted root is1, and put

\[
 V=(z-w_i)(z-w_j)=z^2+z+1,
 \quad H=(z+1)V,
 \quad U=(z-p)(z-\zeta p),\quad p=z(P).
\]

The point is not deck-fixed and is not Weierstrass, so p≠0 and p³≠1. A function with divisor8P+W_j−8δP−W_i, multiplied by (z−ζp)⁸(z−w_i), has divisor

\[
 8P+8\iota\delta P+W_i+W_j-18\infty.
\]

Since z and Y have pole orders2 and9, its numerator is A+B Y with deg A≤9 and deg B≤4. Its norm is

\[
 A^2+HAB+FB^2=K U^8V,\qquad K\ne0. \tag{1}
\]

The coefficients of z¹⁸ and z¹⁷ show deg A=9 and deg B=4: the coefficient at z¹⁷ on the right is K, while HAB has degree≤16 and F B² has that coefficient only if deg B=4.

We have gcd(A,B)=1. A common nonbranch zero would give a whole hyperelliptic pair in the numerator's zero divisor, whereas the displayed divisor contains only one point over each of p and ζp. At W_i or W_j a common polynomial zero would give multiplicity at least2, whereas the displayed multiplicity is1. At the other branch point no zero is allowed. Therefore no common root is possible.

At w_i,w_j, equation(1) gives A²=0, so V divides A. Put A=V C. The rational function X=C/B is reduced. Dividing(1) by V B² gives

\[
 V X^2+H X+(z+1)(\beta H^2+\alpha)=L^2,
 \qquad L=\sqrt K\,U^4/B. \tag{2}
\]

Differentiating yields

\[
 H X'=X^2+z^2X+\beta H^2+\alpha. \tag{3}
\]

In particular X is regular at every zero of H. If it had a pole of order h>0 there, the left side would have valuation at least−h, whereas X² would have valuation−2h and could not cancel with the other terms. Hence B is coprime to H.

## 2. Polynomial solutions and a coprime rational parametrization

For e,η∈F₂ and c satisfying c²+c=t+η, the polynomial

\[
 X_0=t z^3+e z^2+c z+c+\eta \tag{4}
\]

satisfies(3). These are eight polynomials. At a zero w of H, equation(3) has exactly two possible values of X, since X²+w²X+α=0 and w≠0. The eight polynomials in(4) realize all eight choices at the three zeros of H: the difference of two has degree≤2, so two polynomials agreeing at all three roots are equal. Thus choose X_0 whose values agree with X at every zero of H.

The corresponding square root in(2) is

\[
 L_0=t z^4+(r+e)z^3+(r+e+\eta)z^2+(e+\eta)z+\eta
     =t z^4+r z^3+r z^2+V(ez+\eta). \tag{5}
\]

Both(4) and(5) are verified by direct substitution, using c²+c=t+η and α=t²+t.

Put u=X−X_0. If u=0, reducedness of C/B makes B constant, contrary to deg B=4. Otherwise, subtracting the Riccati equations gives H u'=u²+z²u. Thus

\[
 \left(\frac{1/u}{H}\right)'=\frac1{H^2}
                   =\left(\frac z{H^2}\right)'.
\]

Over the perfect constant field, the kernel of d/dz on kbar(z) is kbar(z²), hence its square subfield. Consequently

\[
 X=X_0+\frac{H}{z+R^2},\qquad
 L=L_0+\frac{H(z+1+R)}{z+R^2} \tag{6}
\]

for some rational R. The second formula follows by squaring and using V+z=(z+1)²; square roots are unique in characteristic two.

Write R=M/N with coprime polynomials M,N, and set D=M²+zN². Then D'=N² and gcd(D,N)=1, so D is squarefree. It is also coprime to H. Otherwise, at a shared root w, formula(6) would give

\[
 (X-X_0)(w)=H'(w)N(w)^2/D'(w)=w^2\ne0,
\]

contrary to the chosen agreement of X and X_0. Thus HN²/D is a reduced rational function, and the reduced denominator of X is D. After a scalar rescaling, B=D.

The even degree of M² and odd degree of zN² cannot cancel. Since deg D=4, we have deg M=2 and deg N≤1. Scale M,N together to make M monic. Write

\[
 M=z^2+m_1z+m_0,\qquad N=n_1z+n_0.
\]

Now B=D is monic; comparing z¹⁷ in(1) gives K=β and hence √K=t. Equation(6) is equivalent to

\[
 L_0(M^2+zN^2)+H\bigl((z+1)N^2+MN\bigr)=t U^4. \tag{7}
\]

The right side has only powers z⁸,z⁴,1, and its coefficients satisfy [z⁴]²=t[z⁰]. This is the exact finite-degree identity to be eliminated.

## 3. The four universal coefficient systems

For the four choices a=e,b=η in F₂, choose v with r=v⁴. Since β=r⁴≠0,1, we have v≠0,1. Put

\[
 t=v^8,\quad \ell_3=v^4+a,\quad
 \ell_2=v^4+a+b,\quad \ell_1=a+b.
\]

Comparing z⁷ and z⁶ in(7) determines n₁ and m₁ uniquely:

| (a,b) | n₁ | m₁ |
|---|---|---|
| (0,0) | v⁻² | (v⁴+v²+v+1)/v⁶ |
| (1,0) | (v²+1)/v⁴ | (v³+1)/v⁵ |
| (0,1) | v⁻² | (v⁴+v+1)/v⁶ |
| (1,1) | (v²+1)/v⁴ | (v³+v+1)/v⁵ |

All these denominators, and n₁, are nonzero. Write x=n₀. The coefficients at z¹ and z² eliminate m₀:

\[
 m_0=\frac{(b+1)x^2+m_1x}{n_1}\quad\text{if }a+b=0,
\]

and otherwise

\[
 m_0=\frac{(\ell_2(b+1)+1)x^2+\ell_2m_1x+
              b m_1^2+n_1^2+x+m_1n_1}{\ell_2n_1}.
\]

Here and throughout this coefficient system a+b and b+1 are in characteristic two; the program branches using XOR. In the second case ℓ₂=v⁴+1 is nonzero.

The remaining necessary coefficients z⁵,z²,z³ are the following polynomials in x over F₂(v):

\[
\begin{aligned}
 P_0={}&t x^2+\ell_3m_1^2+\ell_2n_1^2+\ell_1+n_1^2+x+m_1n_1,\\
 P_1={}&\ell_2m_0^2+\ell_1x^2+b m_1^2+n_1^2+x+m_1n_1,\\
 P_2={}&\ell_3m_0^2+(\ell_2+1)x^2+\ell_1m_1^2+b n_1^2
                       +m_0x+n_1^2+n_1.
\end{aligned} \tag{8}
\]

There is also the necessary coefficient relation P₃=[z⁴]²+t[z⁰], recorded in the program. The program independently re-expands(7) as a polynomial in z and verifies each coefficient in(8), the solved z⁷,z⁶ equations, and the exact linear combination eliminating z¹.

## 4. An exact Bézout certificate, not parameter sampling

The program `code/A_cubic_order_sixteen_candidate.py` and its adjacent JSON save the following exact identities. For i=1,2, extended Euclid over F₂(v)[x], followed by clearing all coefficient denominators, produces polynomials U_i,W_i in F₂[v,x] and d_i(v) in F₂[v] such that

\[
 U_iP_0+W_iP_i=d_i(v).
\]

The identity is checked by exact polynomial multiplication. Coefficients of the P_i have only powers of v and v+1 in their denominators, which are invertible on our parameter range. Remove those factors from d_i. Another explicitly saved and checked Bézout identity in F₂[v] gives:

| (a,b) | Degrees of the two obstruction polynomials | Their gcd |
|---|---:|---|
| (0,0) | 26,35 | 1 |
| (1,0) | 38,46 | 1 |
| (0,1) | 52,56 | (v⁴+v³+v²+v+1)² |
| (1,1) | 26,35 | 1 |

Thus the first, second, and fourth cases cannot have any common root of P₀,P₁,P₂. In the third case v is a nontrivial fifth root of unity. Work in the field F₂[v]/(v⁴+v³+v²+v+1); the polynomial is irreducible because ord₅(2)=4. Reducing the P_i in this field, the program supplies and verifies an extended-Euclid row with

\[
 \gcd(P_0,P_1,P_2)=x+v^3+v.
\]

It also verifies that P₃ is divisible by this linear polynomial. Therefore the only remaining coefficients are

\[
 n_0=v^3+v,\quad n_1=v^3,\quad
 m_1=v^2+v,\quad m_0=v^3+v+1.
\]

But z₀=v³+1 satisfies both N(z₀)=0 and M(z₀)=0. For the latter identity, substitution reduces to v⁴+v³+v²+v+1=0. This contradicts the required coprimality of M,N. The apparent exceptional algebraic solutions are therefore invalid rational parametrizations, not torsion points.

Every Bézout coefficient is stored explicitly as low-to-high binary coefficient arrays. The finite field calculation is a calculation over the irreducible cyclotomic residue field, hence applies to all its conjugate roots; it is not a numerical search over sample curves. The program checks all field inverses, every Euclidean identity, the coefficient expansion, and the final shared root.

## Candidate conclusion and remaining scope

If this geometric reduction and its certificate pass independent review, there is no non-Weierstrass γ-value of order16 for any cubic ordinary elliptic auxiliary with an exact order-three branch pair. Combined with A.29f, the corresponding positive residue test would enlarge from λ modulo16 outside μ₆ to λ modulo32 outside μ₆. This does not settle the remaining higher-order values or arbitrary ordinary elliptic covers. At order32, the same Riccati parametrization remains valid but the coprime polynomials have degrees6 and at most5; the present finite-degree elimination does not prove its conclusion there.

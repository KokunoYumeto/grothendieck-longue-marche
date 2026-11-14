# Exact Cartier criterion for two-point odd cyclic covers of an ordinary elliptic curve

Status: accepted and integrated as A.29j. Root and the degeneration agent independently checked the complete valuation, square-class, coincident-point, torsion-order, and reflection arguments. The historical candidate filename is retained. It is separate from the explicit geometric-simplicity obstruction A.29i.

## Statement

Let k be algebraically closed of characteristic two. Let E/k be ordinary with origin O and nonzero geometric two-torsion point T₂. Let n>1 be odd. Every connected cyclic n-cover of E fully ramified at exactly two points can, after translating one branch point to O and changing its cyclic generator, be written

\[
 z^n=f,\qquad \operatorname{div}(f)=n(P)+(A)-(n+1)(O),
 \qquad nP=-A\ne O.
\tag{1}
\]

Here the branch residues must be opposite and prime to n. The chosen point P records the Picard root. Let C denote this cover. Then g(C)=n. The Cartier operator on H⁰(C,Ω¹) is singular if and only if P has finite even order d≤n−1. In particular:

- Every such cover for which the elliptic branch difference A has odd order is ordinary, for every choice of its Picard root.
- Every reflection quotient C/〈τ〉 has genus(n−1)/2. If C is ordinary then so is that quotient, and neither curve maps nontrivially to a p-rank-zero abelian variety.
- When A has exact order n, P has exact order n², so the odd-order conclusion applies. For a prime-power n, every nonzero n-torsion branch difference has the same consequence.

The cyclic generator normalization in(1) uses that the original residue a is a unit modulo n; it is not asserted for a two-point cover with non-full ramification and an independent unramified factor. That separate case can be treated only after specifying its connected character and degree.

## 1. Kummer normal form and the full differential basis

With branch residues a and−a, where gcd(a,n)=1, replacing the Kummer generator by a unit power changes the residues to1 and−1. Hence div(f)=(A)−(O)+nD for a degree-zero divisor D. Represent [D] by [(P)−(O)] on E. Replacing f by f/uⁿ for a suitable rational u makes its divisor exactly(1). The principal-divisor condition is nP=−A in the elliptic group. Conversely every such P supplies the required function. Full tame ramification gives g(C)=n by Riemann–Hurwitz.

Choose the ordinary Weierstrass coordinate X with

\[
 \operatorname{div}(X)=2(T_2)-2(O),\qquad
 \omega_E=dX/X.
\]

The differential ω_E is nonzero, regular, and Cartier-fixed. For j=1,…,n−1 choose g_j with

\[
 \operatorname{div}(g_j)=j(P)+(-jP)-(j+1)(O).
\tag{2}
\]

It exists because the divisor has degree zero and elliptic sum zero. Define

\[
 \omega_j=g_j z^{-j}\omega_E.
\tag{3}
\]

These are regular. If P,A,O,−jP are distinct, their orders are0 above P, n−1−j above A, j−1 above O, and1 above each of the n points above−jP. There are no other zeros or poles.

All coincidences retain regularity. P≠O because A≠O. If A=P, the combined f-valuation at P is n+1 and its tame index is n; the order of ω_j is n−1−j, increased by n if−jP=P. If−jP=P but A≠P, the extra zero makes the order above P equal one. If−jP=A, the order above A increases by n. If−jP=O, the order above O increases by n. These cover every possible coincidence. Each resulting order is nonnegative, and the total degree is2n−2.

The n−1 forms(3) have distinct nontrivial characters of the cyclic deck group. Together with the pullback of ω_E they are n independent regular differentials, hence a basis. In particular every nontrivial character space has dimension one.

## 2. When a character differential is killed by Cartier

The function X is separating on C because the extension C/E is separable. In characteristic two, every coefficient u has a unique expression a²+Xb², and

\[
 \mathcal C(u\,dX)=b\,dX.
\]

Thus Cartier kills u dX exactly when u is a square in k(C). A function in k(E) cannot acquire a new square root in the separable extension k(C)/k(E).

For j even, the coefficient g_j/(Xz^j) differs from g_j/X by a square, so

\[
 \mathcal C(\omega_j)=0\quad\Longleftrightarrow\quad g_j/X\text{ is a square in }k(E).
\]

Its divisor is

\[
 j(P)+(-jP)+(1-j)(O)-2(T_2).
\tag{4}
\]

Modulo two, this divisor is (-jP)+(O). Thus it can be even only when jP=O. When that equality holds, its half-divisor has elliptic class

\[
 (j/2)P-T_2.
\]

A rational function over an algebraically closed constant field with an even divisor is a square exactly when that half-divisor is principal: if div(u)=2D and D=div(v), then u/v² is a constant square. Consequently

\[
 \boxed{\mathcal C(\omega_j)=0\iff [j/2]P=T_2\quad(j\text{ even}).}
\tag{5}
\]

For j odd, since j+n is even and zⁿ=f, the coefficient differs from g_j f/X by a square. Its divisor is

\[
 (j+n)(P)+(-jP)+(A)-(j+n)(O)-2(T_2).
\tag{6}
\]

Its parity is (-jP)+(A), so evenness requires(n−j)P=O. In that case the half-divisor class is

\[
 ((j+n)/2)P+A-T_2=((j-n)/2)P-T_2.
\]

Therefore

\[
 \boxed{\mathcal C(\omega_j)=0\iff [(n-j)/2]P=T_2\quad(j\text{ odd}).}
\tag{7}
\]

These are identities of divisors with multiplicities, so they remain valid when−jP=P, A=P, or P=T₂. No generic-position restriction was imposed.

## 3. Ordinariness and the exact exceptional torsion orders

Cartier permutes the nontrivial character labels by j↦2⁻¹j modulo n. The invariant elliptic line is Cartier-fixed. Since every other character space is one-dimensional, Cartier is bijective if and only if none of the arrows(5)–(7) vanishes.

As j runs from1 to n−1, the integers j/2 for even j and(n−j)/2 for odd j each run once through1,…,(n−1)/2. Thus the kernel is nonzero precisely when

\[
 [k]P=T_2\quad\text{for some }1\le k\le(n-1)/2.
\tag{8}
\]

If P has infinite order or finite odd order, this is impossible. If P has finite even order d, its unique order-two element is[d/2]P=T₂, since E has only one nonzero geometric two-torsion point. The smallest positive k satisfying(8) is d/2. Hence(8) holds exactly when d≤n−1. This proves the criterion.

If A has odd order, then P has odd order: nP=−A and n is odd, so a suitable odd multiple of n kills P. Hence every Picard root is ordinary. If A has exact order n, the equality ord(nP)=n forces ord(P)=n² prime by prime. More generally, for n=ell^a and a nonzero n-torsion A of order ell^b, ord(P)=ell^(a+b), again odd and greater than n.

One may also read off the p-rank of C. Let the multiplication-by-two orbits in (Z/n)\{0} be O. An orbit contributes its full length if it contains no index satisfying(5) or(7), and contributes zero otherwise; the invariant elliptic line contributes one. This follows by iterating the semilinear one-dimensional Cartier arrows and using the standard equality of p-rank with stable Cartier rank, opened in Pries (2024), Lemma4.2.6, printed p.37. No claim about an uncomputed orbit is needed for the ordinary conclusion.

## 4. Reflection quotients and scope

For the reflection ρ(t)=A−t, the divisor of fρ*f is n((P)+(ρP)−(O)−(A)). The divisor in parentheses is principal, since its elliptic sum is zero. Choose h with this divisor and adjust its constant so that hⁿ=fρ*f. The constant ratio ρ*h/h has order dividing both n and two, hence is one. Thus τ(t,z)=(ρt,h(t)/z) is an involution that inverts the cyclic deck group. There are two geometric fixed points on ordinary E; the branch pair A,O is exchanged. Each fixed elliptic fibre has exactly one fixed lift in the odd cyclic torsor. Because C/E is étale there, its completed local ring equals the corresponding ring of E. After translating a fixed point to the origin, inversion has parameter action u↦u/(1+u), so the different exponent is two; translation by the nonzero two-torsion point gives the same calculation at the other fixed point. Thus

\[
 2n-2=2(2g(H)-2)+4,\qquad g(H)=(n-1)/2.
\]

The quotient map C→H is finite separable. Its pullback on regular differentials is injective and commutes with Cartier. If Cartier on C is injective, so is Cartier on H; since the constant field is perfect, this proves H ordinary. Every positive-dimensional quotient of its Jacobian is ordinary by isogeny invariance and Poincaré reducibility. Hence no p-rank-zero abelian target can be obtained directly from any such reflection quotient when the elliptic branch difference has odd order.

This is a uniform obstruction to one hoped-for extension of the two-point method. It does not obstruct the cubic theorem A.29h: a genus-one quotient is detected there by additional ambient tame ramification and A.21, even though it is ordinary. For n=5, the quotient has genus two; A.29i additionally supplies one such quotient whose Jacobian is geometrically simple, excluding an elliptic target for that selected choice. Neither statement excludes a different geometric construction or further admissible covers, and neither refutes A1.

## Sources and exact supporting certificate

The general Cartier p-basis formula was opened in Elkin and Pries (2013), Section2f, printed p.513. Pries (2024), The Torelli locus and Newton polygons, Section4.2.3 and Lemma4.2.6, printed p.37, supplies the stable-Cartier-rank interpretation. Bouw (2001), Proposition8.1 and Corollary8.2, printed pp.319–321, concerns maximal p-rank for suitable generic branch positions, including ordinary elliptic bases; that statement is not an attribution for the explicit torsion criterion above. Targeted primary-source searches are recorded in sources/A_sources.md. No priority or novelty claim is made.

The standard-library program code/A_two_branch_cartier_certificate.py and its JSON output check547 torsion cases and10,968 character arrows for odd n from3 through31, including the coincident-point cases and exact half-divisor classes. These are independent finite consistency checks of the universal proof, not a replacement for it.

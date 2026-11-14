# A degree-five reflection quotient with an ordinary, geometrically simple Jacobian

Status: proved and integrated as A.29i after independent mathematical review and independent finite-field and polynomial verification by root. The historical filename is retained. This does not refute A1, and it does not rule out other Picard roots, other auxiliary covers, or further admissible covers. It refutes the assertion that every two-point quintic auxiliary with an order-five elliptic branch difference automatically has a p-rank-zero or elliptic target.

The exact counting program and output are `code/A_quintic_reflection_experiment.py/.json`. Root independently reproduced every count and all five local cancellation units in `code/root_A_quintic_independent_count.py/.json`, importing none of the candidate code and using local leading factors instead of product jets. It also independently checked the root-ratio obstruction and irreducibility modulo seven. The exact ordinary/simplicity polynomial certificate, using only rational polynomial arithmetic and finite arithmetic modulo seven, is `code/A_quintic_reflection_algebra_certificate.py/.json`.

## 1. Exact elliptic data and the two-point quintic cover

Let

\[
 k=\mathbb F_2[r]/(r^6+r+1),\qquad q=64,
\]

and use the binary encoding \(\sum b_i2^i\) for \(\sum b_i r^i\). Define the ordinary elliptic curve

\[
 E:\quad Y^2+XY=X^3+r^5X^2+(r^3+r^2+r).
\]

The encoded coefficients are a₂=32 and a₆=14. The curve is smooth because a₆≠0. It is ordinary: the nonzero point with X=0 is a geometric point of order two. Direct enumeration gives #E(k)=50. The point

\[
 P=(r^5+r^2+r,\;r^5+r^3+r^2+1),
\]

encoded (38,45), has exact order25. The exact group-law checks are [25]P=O and [5]P≠O. Put A=−[5]P; it has exact order five.

For elliptic points U,V not giving a vertical line, let L_{U,V} be their chord or tangent, and write v_W=X−X(W). The usual chord divisor is

\[
 \operatorname{div}(L_{U,V})=(U)+(V)+(-U-V)-3(O).
\]

Use the following explicit rational function:

\[
 f=\frac{L_{P,P}^{\,2}\,L_{2P,2P}\,L_{4P,P}}
          {v_{2P}^{\,2}v_{4P}}.
\tag{1}
\]

It is the Miller function f_{5,P}, multiplied by v_{5P}. Expanding the displayed chord divisors gives exactly

\[
 \operatorname{div}(f)=5(P)+(A)-6(O).
\tag{2}
\]

The code checks each chord restriction as a cubic polynomial identity, with its three specified intersection points, including the tangent multiplicity. Thus (2) is tied to the actual elliptic curve and the actual rational function, not inferred from its sampled values.

Let T be the normalization of z⁵=f over E. It is connected: the valuation one at A makes f a non-fifth-power. Its only ramification points over E are A and O, both of full tame index five. Thus g(T)=5. In particular the elliptic branch difference is the point A of exact order five, so this is within the odd-torsion branch family that a [5]-orbit extension would have to treat.

## 2. The involution and its genus-two quotient

Let ρ(t)=A−t. It exchanges A and O. In (2) the degree-zero divisor used in the Kummer construction is D=(P)−(O), and

\[
 D+\rho^*D=(P)+(A-P)-(O)-(A).
\]

Set

\[
 h_0=L_{P,A-P}/v_A.
\tag{3}
\]

Its chord divisor gives div(h₀)=D+ρ*D, so fρ*f/h₀⁵ is a nonzero constant κ. The saved exact witness evaluates this constant; in the stated normalization κ=1. More generally κ∈k* has a unique fifth root because gcd(5,63)=1, and the code includes this constant normalization. With h=κ^(1/5)h₀, one has

\[
 f\rho^*f=h^5,\qquad \rho^*h=h.
\tag{4}
\]

The second equality follows because its quotient is a constant fifth root of unity and applying ρ twice gives square one. The lift

\[
 \tau(t,z)=(\rho(t),h(t)/z)
\]

is therefore an involution defined over k and inverts the quintic deck action.

Exactly as in A.29h, the ordinary elliptic reflection has two geometric fixed points, neither at A,O. Each unramified five-point fibre has exactly one τ-fixed point. The local different exponent is two at each, inherited through the completed local étale isomorphism from E. For H=T/〈τ〉,

\[
 8=2g(T)-2=2(2g(H)-2)+4,
\]

so H is smooth proper of genus two.

## 3. Complete normalization-aware point counts

The extension field is

\[
 K=\mathbb F_2[s]/(s^{12}+s^3+1).
\]

The base generator r is embedded as the element encoded163. The script checks its defining equation and the injectivity of the resulting64-element embedding. It proves irreducibility of both binary field moduli by exhaustive polynomial trial division through half their degree. The embedded coefficients, points, chord lines, norm line, normalization constant, and witness are all saved in the JSON.

For any finite field F containing k, enumerate E(F) by solving

\[
 (Y/X)^2+Y/X=X+a_2+a_6/X^2\qquad(X\ne0),
\]

and add the unique X=0 point and O. The code also substitutes every resulting pair into the original equation.

For T(F), A and O each contribute exactly one point by full ramification. Every other elliptic point contributes the number of fifth roots of the local leading unit of f. This includes the fivefold zero at P: the normalization coordinate is z/(X−X(P)), not z itself, so the fibre is counted from the leading unit rather than as a single affine singular point.

The only finite apparent poles of formula(1) lie at ±2P and ±4P. They cancel, and the code evaluates their actual unit using formal local series. Since these points and P have X≠0, u=X−X(R) is a local parameter. Writing Y=\sum c_i u^i with c₀=Y(R), the equation gives the exact recurrence

\[
 X(R)c_i=c_{i-1}
   +\begin{cases}c_{i/2}^2,&i\text{ even},\\0,&i\text{ odd},\end{cases}
   +b_i,
\]

where b₁=X(R)², b₂=X(R)+a₂, b₃=1, and b_i=0 for i>3. The code uses ten terms, although every required cancellation has order at most two and the largest relevant zero order is five. It checks valuation five at P and valuation zero at every other nonbranch point. Thus every cancelled numerator/denominator case is accounted for. The saved table contains P and all four apparent-pole points with their resulting local units.

Since x↦x⁵ is a bijection of k* and hence of k, every unramified fibre over E(k) has exactly one k-point, including the normalized fibre at P. Therefore

\[
 \#T(k)=\#E(k)=50.
\]

Exact enumeration over K gives

\[
 \#E(K)=4000,\qquad \#T(K)=4442.
\tag{5}
\]

The elliptic count agrees independently with its degree-two Frobenius relation: its k-trace is15, so its K-trace is15²−2·64=97 and #E(K)=4097−97.

### Quotient counts without an assumed Jacobian decomposition

For any finite-field Frobenius Φ commuting with an involution τ, geometric τ-orbits give

\[
 2\#(T/\tau)(\mathbb F_{q^m})
   =\#\operatorname{Fix}(\Phi^m)
     +\#\operatorname{Fix}(\tau\Phi^m).
\tag{6}
\]

This includes ramified singleton orbits: each rational singleton is counted once in both fixed-point terms. For a stable two-point orbit, Frobenius acts either trivially or by τ, and the total is two. No free-action assumption is used.

The elliptic quotient E/ρ is rational over k, since its geometric genus is zero and the image of the rational pair {A,O} is rational. Applying (6) to E gives

\[
 \#\operatorname{Fix}(\rho\Phi^m)
   =2(q^m+1)-\#E(\mathbb F_{q^m}).
\tag{7}
\]

For m=1, these80 fixed elliptic points all lie in E(K), because (ρΦ)²=Φ². Neither A nor O is fixed. Nor is the unramified fivefold zero P fixed, since P is rational and ρ(P)≠P. Thus its entire fibre may be counted with the ordinary value f(t); the code checks that no displayed Miller cancellation occurs at any such t either. A τΦ-fixed lift satisfies

\[
 z^5=f(t),\qquad z^{65}=h(t).
\tag{8}
\]

The program enumerates all fifth roots in K and checks the norm equation for each. There are90 solutions in total. Equations(6) and(8) therefore give

\[
 \#H(k)=(50+90)/2=70.
\tag{9}
\]

For m=2 one need not enumerate E over k⁴. Since 4096≡1 modulo5, the action of τΦ² on an unramified quintic fibre is a reflection of the five-element torsor and has exactly one fixed lift above each ρΦ²-fixed elliptic point. Indeed its action on the deck group is ζ↦ζ^(−4096)=ζ^−1. Again the branch pair is exchanged and contributes no fixed point. By (7),

\[
 \#\operatorname{Fix}(\tau\Phi^2)
 =2\cdot4097-4000=4194.
\]

Consequently

\[
 \#H(K)=(4442+4194)/2=4318.
\tag{10}
\]

This derivation uses the actual involution and includes all singular affine presentations, all branch points, and all fixed singleton quotient fibres. It does not assume the desired genus-two Frobenius polynomial or a Prym isogeny decomposition.

## 4. The ordinary Weil polynomial

From(9)–(10), the first two Frobenius power sums for H are −5 and −221. Newton identities and reciprocity give

\[
 P_H(X)=X^4+5X^3+123X^2+320X+4096.
\tag{11}
\]

Its middle coefficient is odd, so J_H is ordinary. The equivalence between ordinariness and a middle coefficient prime to the characteristic is recorded, with its Newton-polygon justification, in van Bommel et al.(2025), Theorem2.1 and the last paragraph of its proof, printed p.1172/PDF p.6. The exact primary PDF was opened at https://link.springer.com/content/pdf/10.1007/s00208-024-03084-4.pdf . The individual computation(11) is new here and is not attributed to that source.

In particular J_H has no positive-dimensional p-rank-zero abelian quotient: p-rank is isogeny-invariant and additive, and Poincaré reducibility makes every quotient of an ordinary abelian variety ordinary.

## 5. Geometric simplicity, with a finite exhaustive certificate

The polynomial(11) is irreducible modulo seven. The standalone algebra certificate divides it by all seven monic linear and49 monic quadratic polynomials over F7 and finds a nonzero remainder in all56 cases. A reducible quartic would have a factor of degree at most two, so this is a complete irreducibility proof over F7 and therefore over Q.

Let its four roots be α,64/α,β,64/β. Put u=α+64/α and v=β+64/β. Then

\[
 u+v=-5,\qquad uv=123-128=-5.
\]

There are four nontrivial ratios inside the two reciprocal pairs, and four cross-pair ratios, each of the latter occurring twice in the full ordered list. Direct symmetric multiplication gives their two integer polynomials

\[
 B(Y)=4096Y^4+14144Y^3+20121Y^2+14144Y+4096,
\]

\[
 C(Y)=64Y^4+5Y^3-93Y^2+5Y+64.
\]

More explicitly, the reciprocal-pair ratios have sums (u²−128)/64 and (v²−128)/64. The cross ratios are α/β, β/α, αβ/64, and64/(αβ). Their sum is uv/64=−5/64, and their second elementary sum is (u²+v²)/64−2=−93/64. These identities give B and C directly. Equivalently, the full ratio resultant is

\[
 \operatorname{Res}_X(P_H(X),Y^4P_H(X/Y))
 =64^4(Y-1)^4 C(Y)^2B(Y).
\]

Every nontrivial eigenvalue ratio is therefore a root of the degree-eight polynomial BC. If such a ratio were a root of unity of order n>1, its cyclotomic degree φ(n) would be at most eight. The complete possible list, including one for reference, is

    1,2,3,4,5,6,7,8,9,10,12,14,15,16,18,20,24,30.

Completeness can be checked without a search cutoff: every prime divisor ℓ of n has ℓ−1≤8, hence ℓ∈{2,3,5,7}; the exponent bounds are4,2,1,1 respectively. Filtering those finitely many products by Euler's formula gives exactly the displayed list.

The certificate generates every corresponding cyclotomic polynomial by exact division of Yⁿ−1, and saves full rational-polynomial Bézout identities

\[
 U_n(Y)B(Y)C(Y)+V_n(Y)\Phi_n(Y)=1
\]

for all18 orders. Every identity is re-multiplied and checked. It uses no symbolic algebra package. Thus no quotient of distinct Frobenius eigenvalues is a root of unity.

Because P_H is irreducible of degree four, each power α^m has four distinct Galois conjugates for every m≥1: an equality of two such powers would make a quotient of distinct eigenvalues a root of unity. Its minimal polynomial therefore still has degree four and equals the Frobenius polynomial over k_m. This polynomial is irreducible for every m. If J_H had a proper positive-dimensional geometric abelian subvariety, it would be defined over some finite extension of k and give a proper factor of that extension's Frobenius polynomial. This is impossible. Hence J_H is geometrically simple.

A nonconstant map from H to an elliptic curve over kbar would induce a nonzero homomorphism from J_H onto that elliptic curve, contradicting geometric simplicity. This includes inseparable curve maps, since a nonconstant map still induces a nonzero pushforward homomorphism on the Jacobian.

## Exact consequence and limitation

The reflection quotient of this eligible two-point quintic cover is ordinary and has no nonconstant map to an elliptic curve or to any p-rank-zero abelian variety, over any finite extension or over the algebraic closure. Therefore neither direct target mechanism from the cubic proof automatically extends to every quintic auxiliary.

This is a method obstruction for one explicit auxiliary. It does not show that every possible Kummer root for the same branch pair has this property. It does not exclude a suitable further odd étale cover of H, or a different arrangement of auxiliary covers, or A1 itself for H or T. The precise next positive possibility is to choose or construct a different auxiliary/refinement with the necessary detection maps, rather than to assume that genus-two reflection quotients are always supersingular or elliptically decomposable.

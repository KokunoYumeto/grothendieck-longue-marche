# Prym detection on the ordinary genus-four auxiliary

## Proved result and its exact scope

Let c²+c+1=0 in F4. Let E be the smooth elliptic curve

\[
 E:\ y^2+y=x+c/x,
\]

with origin at infinity, and let B be the smooth proper curve

\[
 B:\ y^2+y=s^3+c+c/(s^3+c),\qquad x=s^3+c.
\]

The claim proved below is A1 for B over every finite extension of F4. It does not assert the general ordinary-elliptic case. It uses the exact examples and covers already proved in A.29a–A.29b, while employing a different detection mechanism: a small 2-primary point packet in a Prym, followed by a translated cover which removes that packet.

Let δ act by (s,y)↦(cs,y). Let ι be the hyperelliptic involution (s,y)↦(s,y+1). They commute. Write O_B for the unique point at infinity, W_0,W_1,W_2 for the three finite Weierstrass points, at s³+c=0, with indices chosen cyclically under δ. The δ-fixed points are O_B and the two points with s=0. On E, the finite Weierstrass points of B all map to the nonzero two-torsion point T above x=0.

Put

\[
 A=(\ker(\operatorname{Nm}_{B/E}:J_B\to E))^0,
 \qquad \gamma(P)=[P-\delta P].
\]

The image of γ lies in A: its norm is zero, it is connected, and it contains zero. We have dim A=3 and 2-rank A=2, since J_B has dimension4 and 2-rank3 and E is ordinary; the degree-three norm/pullback decomposition is an isogeny. Its Frobenius polynomial, from A.29a, is

\[
 R(X)=X^6+3X^5+9X^4+20X^3+36X^2+48X+64. \tag{1}
\]

## 1. Two elementary low-degree divisor facts

We use the usual uniqueness of reduced divisors of degree at most g on a hyperelliptic curve with a Weierstrass base point. In the present argument the needed degree is only two or three, while g=4. A direct justification is available: any function of degree at most3 which does not factor through the hyperelliptic degree-two map would give a birational map to a curve of bidegree (2,d) in P1×P1. Its arithmetic genus is d−1≤2, contradicting genus4. Thus every moving linear series of those degrees is the hyperelliptic pencil plus its remaining base divisor. This remains valid in characteristic two: the hyperelliptic extension is separable, and a function outside its quadratic subfield generates that extension.

### 1.1 γ is injective outside its zero fibre

If γ(P)=γ(Q), then

\[
 P+\delta Q\sim Q+\delta P. \tag{2}
\]

If these effective divisors are equal, either P=Q or both P and Q are δ-fixed. If they are distinct, they must be hyperelliptic fibres. Therefore δQ=ιP and δP=ιQ. Using δι=ιδ gives δ²P=P, hence δP=P, since δ has order3; then Q=ιP is δ-fixed too. Thus a nonzero γ-value has exactly one geometric preimage. Its zero fibre is precisely the δ-fixed locus, since the Abel map is injective.

### 1.2 A nonzero two-torsion translate cannot connect two non-Weierstrass γ-points

The three nonzero points of A[2](Fbar2) are exactly

\[
 [W_i-W_j],\qquad i\ne j.
\]

Indeed the finite Weierstrass differences lie in the norm kernel because all their E-images are T. They span a group of rank two: the three branch-point classes [W_i−O_B] form an independent basis of J_B[2], as verified in A.29a, and their pairwise differences span the even-sum subspace. The 2-rank of A is two.

Suppose P,Q are non-Weierstrass and

\[
 \gamma(P)-\gamma(Q)=[W_i-W_j]\ne0.
\]

Then

\[
 P+\delta Q+W_j\sim Q+\delta P+W_i. \tag{3}
\]

Each divisor has exactly one Weierstrass summand, respectively W_j and W_i. If neither contains a hyperelliptic pair, both are reduced degree-three divisors and must be equal, which is impossible because their Weierstrass summands differ. If exactly one contains a hyperelliptic pair, reduction leaves degree one on one side and degree three on the other, also impossible. If both contain pairs, they must be (P,δQ) and (Q,δP), since all four of these points are non-Weierstrass. Removing the pairs leaves W_j−O_B and W_i−O_B, which cannot be equal. This proves the assertion.

Equivalently, the moving degree-three system in (3), if any, is a hyperelliptic fibre plus a fixed base point. Its two different Weierstrass residual points cannot both be that base point.

## 2. Frobenius bounds every possible 2-primary γ-value

On A, the norm relation gives 1+δ+δ²=0. Since δ is defined over F4, its action commutes with the fourth-power Frobenius Φ. The geometric étale 2-adic Tate module T₂A has rank two over Z₂. The action of δ makes it a torsion-free rank-one module over

\[
 \mathcal O=\mathbb Z_2[\zeta_3],
\]

the unramified quadratic discrete valuation ring. Thus it is free of rank one, and Φ acts as multiplication by one unit λ∈O*. This is the module-theoretic input; point counts alone are not being used to infer the structure of the Tate module.

The exact determinants from (1), computed by the integral companion matrix, are

\[
 \begin{aligned}
 |A(\mathbb F_{4^3})|&=291772=2^2\cdot72943,\\
 |A(\mathbb F_{4^6})|&=70459436736=2^6\cdot1100928699.
 \end{aligned} \tag{4}
\]

The 2-primary geometric point group is (Frac(O)/O), with Frobenius λ. The 2-primary kernel of Φ^r−1 therefore has order 2^{2v_O(λ^r−1)}. In particular (4) gives

\[
 v_O(\lambda^3-1)=1,\qquad v_O(\lambda^6-1)=3. \tag{5}
\]

Let γ(P) have exact order 2^a with a≥4. Set

\[
 \sigma=\Phi^{6\cdot2^{a-4}}.
\]

Starting with λ⁶=1+8u, u∈O*, repeated squaring increases the valuation of the difference from1 by exactly one at each step. Indeed if v_O(v)≥2, then (1+v)²−1=2v+v² has valuation v_O(v)+1. Hence

\[
 v_O(\lambda^{6\cdot2^{a-4}}-1)=a-1.
\]

It follows that σγ(P)−γ(P) is a nonzero element of A[2]. A Weierstrass point has γ-value of order at most2, so P is non-Weierstrass; its Galois conjugate σP is non-Weierstrass too. Their γ-values differ by this nonzero two-torsion point, contrary to Section1.2. Therefore every 2-primary γ-value has order at most8.

Equation (5) says that Φ⁶ fixes A[8]. If γ(P) is nonzero and 2-primary, Section1.1 then forces Φ⁶P=P. Thus

\[
 P\in B(\mathbb F_{4^6})=B(\mathbb F_{4096}). \tag{6}
\]

There is no unproved uniform-exponent assumption: the bound is specific to this Prym, obtained from its O-module and its exact Frobenius valuation.

## 3. Exact finite certificate on F4096

The code is `code/A_genus4_prym_experiment.py`, with its adjacent JSON. It uses the field

\[
 \mathbb F_2[t]/(t^{12}+t^3+1),
\]

and certifies that t+1 has a full cycle of 4095 distinct nonzero powers and returns to1. This itself proves that every nonzero residue is a unit, so the quotient is a field. Field elements are encoded by binary coefficients, with c=72 satisfying c²+c+1=0.

Set H(s)=s³+c and Y=H(s)y. The curve has the odd-degree hyperelliptic equation

\[
 Y^2+H(s)Y=F(s),\qquad
 F=H^3+cH=s^9+c s^6+s^3+c. \tag{7}
\]

The code enumerates every s and every solution of its Artin–Schreier equation; rational pole points and infinity are added separately. It counts 4206 points. It tests one representative from each orbit of δ and ι, since δ preserves the order of γ and ι changes γ to −γ. There are 702 such orbits.

### 3.1 Why the divisor operations certify the exact class

A reduced divisor class on (7) is represented by a pair (u,v), with u monic, deg u≤4, deg v<deg u, and u dividing v²+Hv+F. It denotes the effective divisor cut out by u=0,Y=v, minus (deg u)O_B. The neutral element is (1,0); negation sends v to v+H modulo u. A finite point (s₀,Y₀) is represented by (s+s₀,Y₀).

The code implements the following composition, with all gcd and Bézout identities checked exactly. For input pairs (u₁,v₁),(u₂,v₂), put

\[
 d=\gcd(u_1,u_2,v_1+v_2+H)
   =a u_1+b u_2+e(v_1+v_2+H).
\]

Before reduction their sum is represented by

\[
 u=\frac{u_1u_2}{d^2},\qquad
 v=\frac{a u_1v_2+b u_2v_1+e(v_1v_2+F)}{d}\pmod u. \tag{8}
\]

To verify (8), multiply the ideals (u₁,Y+v₁),(u₂,Y+v₂) and use

\[
 (Y+v_1)(Y+v_2)=(H+v_1+v_2)Y+F+v_1v_2.
\]

The displayed Bézout combination yields dY plus the numerator in (8); cancellation of the common principal factor d gives the asserted semi-reduced class. The hyperelliptic reduction step is

\[
 u'=\frac{v^2+Hv+F}{u},\qquad
 v'=v+H\pmod{u'}, \tag{9}
\]

with u' rescaled to be monic. The divisor of Y+v proves (9): its other intersection divisor has the opposite class, hence the change v↦v+H. Iterate until deg u≤4. Every division and the defining congruence are verified at each step. Thus equality with (1,0) is an exact test of a trivial divisor class.

For an independent doubling calculation when gcd(u,H)=1, the code also uses Hensel lifting. Write R=(v²+Hv+F)/u and let H^{-1} denote its inverse modulo u. The doubled semi-reduced pair is

\[
 \bigl(u^2,\ v+u(RH^{-1}\bmod u)\bigr),
\]

followed by (9). It is compared with (8). The certificate includes 2103 agreeing independent doublings, 702 inverse-addition identities, and 702 identities γ(P)+γ(δP)+γ(δ²P)=0. These checks supplement the proved formulas; they are not their justification.

### 3.2 Exact output and packet classification

The only orbits with 8γ(P)=0 are:

| Affine orbit | Representative encoding | Exact order of γ | Type |
|---|---:|---:|---|
| s=0 | Y=521 | 1 | Two δ-fixed points, interchanged by ι |
| s³=c | s=32; orbit {32,2304,2336}; Y=0 | 2 | Three finite Weierstrass points |

Infinity is δ-fixed and has γ=0. Therefore, combining (6) with this finite certificate,

\[
 \gamma(P)\in A[2^\infty],\quad \gamma(P)\ne0
 \quad\Longrightarrow\quad
 P\in\{W_0,W_1,W_2\}. \tag{10}
\]

## 4. The translated cover removes the packet

Suppose P≠Q have equal geometrically prime-to-two section classes on B over a finite constant extension. The map B→E is cyclic cubic and ramified, so A.21 gives equal E-images. Hence Q=δ^jP with j=1 or2. The Kummer statement A.1 gives [P−Q] 2-primary. Since [P−δ²P]=−δ²γ(P), (10) shows that P,Q lie in the finite Weierstrass triple. Their common E-image is T.

Lift this collision to V of A.29b using A.3; V/B is étale of degree3. Let Z be its diagonal inertia subgroup and E₂=V/Z. The map V→E₂ is cyclic cubic and ramified (its branch set has nine points), so A.21 gives equal E₂-images of the lifted points. They consequently differ by z^j for a nontrivial z^j∈Z; nontriviality follows from their distinct images on B.

Let B_i retain the root of h_i=τ^{i*}h as in A.29b. Translation t↦t+id identifies B_i with B, and it identifies the central action z with the same deck action δ. The two V-points thus give a nontrivial δ-pair on each B_i whose divisor difference is 2-primary.

On B_i, the hyperelliptic involution covers

\[
 t\longmapsto -t-2id
\]

on E. Its Weierstrass points lie precisely over −id and T−id, the two fixed points of that elliptic involution. For i=1,2, neither of these base points is T: the nonzero id has order3, whereas T has order2. The two images on B_i over the actual base point T are therefore non-Weierstrass. This contradicts the packet classification (10), transported through the indicated isomorphism B_i≅B.

No nontrivial collision exists. This proves A1 for B over every finite constant extension, despite A.29a–A.29b proving that neither B nor this first refinement V has a nonconstant map to a p-rank-zero abelian variety.

### 3.3 Independent Riemann–Roch certificate

The root agent independently checked the packet without Jacobian addition. For a nonexceptional point P and Q=δP, 8(P−Q) is principal if and only if L(16∞) contains a nonzero function vanishing to order at least eight at P and ιQ. Indeed div((s−s(Q))⁸)=8Q+8ιQ−16∞, so this denominator converts precisely between the two conditions. The space has dimension13, with basis 1,s,…,s⁸,Y,sY,s²Y,s³Y: the pole orders of s and Y are2 and9. Expanding Y²+HY=F to precision8 at each point gives a16×13 matrix. The coefficient H(P) is nonzero and makes the expansion uniquely recursive.

The independent standard-library program `code/root_A29c_linear_certificate.py` recomputes the finite field and all points, checks every formal-series identity, and verifies rank13 for every one of the700 nonexceptional orbits. Its adjacent JSON records the rank histogram and a hash of all matrix entries. It independently confirms4206 total points. The s=0 and infinity cases are δ-fixed, and the finite Weierstrass differences have exact order2, by the geometric argument. This verifies the entire finite packet independently of the Mumford algorithm.

The full proof was independently reviewed by the root agent and integrated as Claim A.29c in `sections/A.tex`. The conceptual review covers the two divisor lemmas, the rank-one unramified quadratic 2-adic module, the Frobenius valuation bound, and the central-inertia translated packet elimination.

## Limits

The finite Frobenius and Mumford calculation is specific to the displayed F4 example. The geometric translate-exclusion lemma applies more widely, but the rank-one O-module and finite classification must be supplied again for another curve. No general ordinary-elliptic quotient theorem or universal A1 conclusion is inferred.

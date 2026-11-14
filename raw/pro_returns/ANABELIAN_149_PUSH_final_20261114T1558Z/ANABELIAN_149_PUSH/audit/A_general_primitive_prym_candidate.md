# An odd cyclic primitive Prym criterion in every genus and characteristic

Status: root and topos independently approved the complete proof. A.C2.20 is integrated in sections/A_general_primitive_prym.tex; the finite-field agent inserted its input and updated the claim ledger and report. A.C2.17 and A.C2.19 remain separate statements with their original scopes.

Question locus: 149; manuscript pp.17–17v; scans35–36. This is a derivation in the present audit, not a claim attributed to the manuscript or to the external sources.

## 1. Statement

Let $K$ be finitely generated over $\mathbf F_p$, let $C/K$ be smooth, proper and geometrically connected of genus $g\ge2$, and suppose that geometrically there is a connected cyclic étale cover

\[
                       D\longrightarrow C
\]

of odd degree $n>1$ prime to $p$. Let $\sigma$ generate its deck group. Define its primitive conductor-$n$ abelian subvariety by

\[
 P_n=\operatorname{im}(A)\subset J_D,\qquad
 A=\prod_{\ell\mid n}(1-\sigma^{n/\ell}),
\tag{GP.1}
\]

where the product is over the distinct prime divisors of $n$.
If $f_p(P_n)=0$, then the geometrically prime-to-$p$ point-section map of $C$ is injective.

The conclusion holds over every finite extension, for forms satisfying this geometric hypothesis, and for every hyperbolic open subcurve of $C$. No ordinariness assumption and no restriction on $g$ is imposed.

The image in (GP.1) is the usual primitive cyclic factor up to isogeny: on a character of index $i$, its scalar is nonzero precisely when $\gcd(i,n)=1$. In particular its isogeny class does not depend on the choice of generator. This statement assumes the geometric zero-$p$-rank condition; outside genus two it does not substitute a theta condition for it.

For genus two in characteristic two, A.C2.5 identifies the hypothesis with the primitive doubling-orbit condition of A.C2.19. Thus this theorem supplies a broader geometric criterion while retaining that explicit genus-two test.

## 2. A collision produces a small function supported on two deck orbits

Suppose that distinct $P,Q\in C(K)$ have equal geometrically prime-to-$p$ point-section classes. After finite extension define the cover, its generator, and a chosen rational lift $P'$. A.3 supplies a lift $Q'$ over $Q$ such that

\[
                       [P'-Q']\in J_D[p^\infty].
\]

The hypothesis $f_p(P_n)=0$ means that $P_n$ has no nonzero geometric $p$-primary torsion. The image $A([P'-Q'])$ belongs to that group and is therefore zero. This directly proves the required annihilation; it does not infer integral Tate-module vanishing merely from reduction modulo $p$.

Let $r=\omega(n)$ and $d=2^r$. For every subset $S$ of the distinct primes dividing $n$, put

\[
 a_S=\prod_{\ell\in S}\sigma^{n/\ell}.
\]

Expanding $A([P'-Q'])=0$ gives the principal divisor

\[
 \mathcal D=\sum_S(-1)^{|S|}(a_SP'-a_SQ'). \tag{GP.2}
\]

The $2^r$ elements $a_S$ are pairwise distinct: their factors lie in the cyclic subgroups of pairwise coprime prime orders, and projection to each such factor distinguishes the subsets. Each of the two deck orbits is free, and the two orbits are disjoint because their images on $C$ differ. Thus (GP.2) has exactly $d$ distinct zeros and $d$ distinct poles, each with coefficient one. It is the divisor of a separable rational function $f$ of degree $d$. All its zeros and poles lie in the union of the two deck orbits $GP'$ and $GQ'$.

The numerical inequality

\[
                         n>(d-1)^2 \tag{GP.3}
\]

holds for every odd $n>1$. For $r=1$, use $n\ge3>1$; for $r=2$, use $n\ge15>9$. For $r\ge3$, use $n\ge3\cdot5^{r-1}>4^r>(2^r-1)^2$, with the middle inequality true at $r=3$ and preserved by increasing $r$.

## 3. The controlled-field argument forces a quadratic elliptic quotient

Work over $k=\overline K$, and let

\[
                  M=k(\gamma f:\gamma\in G),\qquad
                  e=[k(D):M].
\]

Every generator has degree $d$. Poonen's controlled-field lemma gives

\[
                     e\mid d,\qquad
                     g(M)\le(d/e-1)^2. \tag{GP.4}
\]

For completeness, the induction behind this formula is as follows. Starting from a field $F$ with $[k(D):F]=d/s$ and $g(F)\le(s-1)^2$, adjoining another degree-$d$ function $h$ with $a=[F(h):F]$ gives

\[
[k(D):F(h)]=d/(as),\qquad [F(h):k(h)]=as.
\]

Castelnuovo–Severi gives

\[
g(F(h))\le a(s-1)^2+(a-1)(as-1)
         =(as-1)^2-as(a-1)(s-1)\le(as-1)^2.
\]

For a single generator the field is rational, so the induction proves (GP.4). The exact opened source is Poonen (2007), Section 2, Proposition 2.1, Lemma 2.2 and Corollary 2.3, author p.3.

The genus of $D$ is $n(g-1)+1\ge n+1$. Hence (GP.3) and (GP.4) exclude $e=1$. Since $e\mid d$, the integer $e>1$ is a power of two.

Let $Z$ be the smooth proper curve with function field $M$. Its field is $G$-stable, so $D\to Z$ is equivariant. The induced $G$-action on $Z$ is faithful: its kernel has order dividing the degree $e$ of the separable extension $k(D)/M$, and also divides the odd number $n$.

The action on $Z$ is free. A nontrivial stabilizer contains an element of odd prime order $\ell$. Its action on $D$ is free. The degree-$e$ fibre divisor above a fixed point is partitioned into orbits of length $\ell$ with constant ramification multiplicity, so $\ell\mid e$, a contradiction.

Thus $Z\to Z/G$ is étale of degree $n$, and

\[
                     g(Z)-1=n(g(Z/G)-1).
\]

It follows that $g(Z)$ is either one or at least $n+1$; genus zero for the quotient would give negative genus for $Z$. The upper bound (GP.4) is less than $n+1$, by (GP.3). Therefore $g(Z)=1$.

Since $f\in M$, it factors as $h\circ v$, where $v:D\to Z$ has degree $e$. Choose a zero of the nonconstant function $h$. Its full inverse-image divisor on $D$ is reduced, because the zero divisor (GP.2) is reduced. Thus the zero of $h$ is simple, $v$ is unramified above it, and the fibre consists of exactly $e$ geometric points.

Each of $GP'$ and $GQ'$ maps injectively to $Z$: two equal images would produce a nonidentity element of $G$ fixing a point on $Z$, contrary to freeness. The fibre just chosen is contained in those two orbits, and therefore has at most two points. Hence $e\le2$. Since $e>1$, necessarily $e=2$.

We have obtained a separable quadratic map $D\to Z$ with $g(Z)=1$. Its involution $\tau$ commutes with $G$, because the subfield $M$ is $G$-stable and the order-two deck group has no nontrivial automorphism. In the prime-power case $d=2$, (GP.4) would already say $g(Z)\le0$, an immediate contradiction. The remaining argument works uniformly whenever this hypothetical quadratic quotient has been obtained.

## 4. The complete quotient square and intermediate covers

The commuting actions give the faithful group $G\times\langle\tau\rangle$ on $D$. Put

\[
                       E_0=Z/G.
\]

The curve $E_0$ has genus one, and $Z\to E_0$ is an odd étale isogeny after choosing origins. Its invariant function field is

\[
k(E_0)=k(D)^{G\times\langle\tau\rangle}.
\]

Consequently $C=D/G\to E_0$ is a separable quadratic map. It is ramified, since $g(C)\ge2$ whereas $g(E_0)=1$.

For every divisor $m\mid n$, set

\[
H_m=\langle\sigma^m\rangle,\qquad
D_m=D/H_m,\qquad Z_m=Z/H_m.
\]

The degrees and quotient square are

\[
\begin{array}{ccc}
D_m&\longrightarrow&Z_m\\
\downarrow&&\downarrow\\
C&\longrightarrow&E_0 .
\end{array}
\tag{GP.5}
\]

Both horizontal maps are separable quadratic. Both vertical maps are étale of degree $m$, and $Z_m$ has genus one. Put $W=C\times_{E_0}Z_m$. The map $W\to C$ is étale, being the base change of $Z_m\to E_0$, so $W$ is smooth. The extensions $k(C)/k(E_0)$ and $k(Z_m)/k(E_0)$ have coprime degrees two and $m$, hence are linearly disjoint. Thus $W$ is integral and its function field is their compositum, of degree $2m$, which equals $k(D_m)$. This identifies the finite fibre product with $D_m$ and proves the Cartesian assertion.

This also proves the precise ramification count used below. If $r_1$ is the number of geometric ramification points of $C\to E_0$, then the number for $D_m\to Z_m$ is

\[
                             r_m=m r_1. \tag{GP.6}
\]

Each branch point has $m$ distinct inverse images under the étale isogeny, and the local quadratic extension is unchanged by that étale base change. Equivalently, if a lift of a $\tau$-fixed point satisfies $\tau P=hP$ with $h\in G$, commuting actions give $h^2P=P$; freeness and odd order force $h=1$, so all lifts are fixed.

## 5. Characteristic two: primitive rank is strictly positive

Suppose $p=2$. All genus-one curves $Z_m$ in (GP.5) have the same two-rank $\epsilon\in\{0,1\}$, since they are isogenous. The ramified Deuring–Shafarevich formula and (GP.6) give

\[
                  f_2(D_m)=m r_1+2\epsilon-1.
\tag{GP.7}
\]

Here $r_1>0$ is the actual ramification count, not a formal expression of unknown sign: the quadratic map $C\to E_0$ is ramified by Riemann–Hurwitz.

Let $b_j$ be the rank of the exact conductor-$j$ part of the geometric étale two-adic Tate representation of $J_D$, for $j\mid n$. Since $n$ is odd, taking invariants under $H_m$ is exact by the averaging idempotent, and pullback and norm identify these invariants with the Tate module of $J_{D_m}$. Hence

\[
                     f_2(D_m)=\sum_{j\mid m} b_j.
\]

On a primitive character every scalar in (GP.1) is nonzero; on every nonprimitive character one factor is zero. Thus $b_n=f_2(P_n)$. Möbius inversion and (GP.7) imply

\[
\begin{aligned}
f_2(P_n)
 &=\sum_{m\mid n}\mu(n/m)f_2(D_m)\\
 &=r_1\sum_{m\mid n}\mu(n/m)m
   +(2\epsilon-1)\sum_{m\mid n}\mu(n/m)\\
 &=r_1\varphi(n)>0,
\end{aligned}
\tag{GP.8}
\]

because $n>1$. This contradicts the zero-two-rank hypothesis.

No assumption that the individual nontrivial character spaces have dimension one occurs here. The calculation therefore applies to every genus $g\ge2$.

## 6. Odd characteristic

Suppose $p$ is odd. The derived map $C\to E_0$ is a geometrically Galois quadratic cover of a genus-one curve, and its degree is prime to $p$. The already proved A.29l therefore gives point-section injectivity for $C$, over finite fields and over finitely generated fields in the stated geometric-form scope. This contradicts the pair with equal sections from Section 2.

This use is independent of the primitive-Prym argument: A.29l was proved from the elliptic-image test and the finite orbifold-centralizer argument. No extension of the Deuring–Shafarevich formula to a prime-to-$p$ group is asserted.

## 7. Descent, forms, and open curves

The geometric cover, its action, and all quotient maps descend after a finite extension of the finitely generated ground field. Equality of section classes restricts to that extension; A.3 supplies the lifted two-primary or $p$-primary divisor difference there. The contradiction is geometric in characteristic two and uses the finite-extension form of A.29l in odd characteristic. Thus the conclusion holds over the original field and all finite extensions. The same argument applies to forms satisfying the geometric hypothesis. Equality of point sections on a hyperbolic open subcurve maps to equality on its compactification, giving the open assertion.

## 8. What remains unsupplied

The theorem is a sufficient geometric criterion. It does not prove that every curve admits an odd prime-to-$p$ cyclic étale cover with primitive factor of $p$-rank zero. Raynaud's nonordinary-cover theorem supplies nonordinariness, which is weaker than this zero-rank condition. In genus two and characteristic two, a theta point kills its doubling orbit, whereas the hypothesis requires all primitive orbits to be killed. No inference from one condition to the other is made.

## 9. Exact sources and dependencies

- Poonen, B. (2007). *Gonality of modular curves in characteristic p.* Mathematical Research Letters, 14(4), 691–701. Opened primary author PDF <https://math.mit.edu/~poonen/papers/gonality.pdf>, Section 2, Proposition 2.1, Lemma 2.2, Corollary 2.3, author p.3. Existing bibliography key A_PrimPoonen2007. The induction is reproduced above.
- Crew, R. M. (1984). *Étale p-covers in characteristic p.* Compositio Mathematica, 52(1), 31–45. Opened primary PDF <https://www.numdam.org/item/CM_1984__52_1_31_0.pdf>, Corollary 1.8, printed p.35, with proof p.36 and both formulas visually checked. Existing key A_PrimCrew1984. Only the characteristic-two quadratic formula is used.
- Current manuscript A.3 supplies the cover lifting and $p$-primary difference. A.29l supplies the odd-characteristic quadratic genus-one quotient case. A.C2.5 supplies the explicit genus-two theta characterization, used only to state its corollary.

The two-orbit support reduction, the Cartesian quotient square, and the primitive Möbius-rank contradiction are proved in this file.

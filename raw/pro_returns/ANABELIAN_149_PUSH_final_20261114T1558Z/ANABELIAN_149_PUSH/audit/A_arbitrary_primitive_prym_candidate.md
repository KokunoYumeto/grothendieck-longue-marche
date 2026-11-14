# All odd conductors: the primitive Prym suffices

Status: root and topos independently approved the complete proof. A.C2.19 is integrated in sections/A_arbitrary_primitive_prym.tex; the finite-field agent inserted its input and updated the claim ledger and report. Integrated A.C2.17 is retained unchanged as its direct two-prime special case.

Question locus: 149; manuscript pp.17–17v; scans35–36. The new deductions are not attributed to the manuscript. No universal theta-point existence statement is claimed.

## 1. Statement

Let $K$ be finitely generated over $\mathbf F_2$, and let $C/K$ be a smooth proper geometrically connected genus-two curve. Let $\Theta$ be its symmetric Raynaud theta curve. Suppose that over $\overline K$ there is a line bundle $L$ of exact odd order $n>1$ for which **every multiplication-by-two orbit on $(\mathbf Z/n)^\times$ meets $\{i:L^i\in\Theta\}$**.

Then the geometrically prime-to-two point-section map of $C$ is injective. The conclusion holds over every finite extension, for forms satisfying this geometric hypothesis, and for hyperbolic open subcurves. Neither ordinariness of $C$ nor a restriction on the number of prime divisors of $n$ is required.

Equivalently, it suffices that the primitive conductor-$n$ part of the cyclic étale cover associated with $L$ has two-rank zero. All smaller-conductor blocks may survive. The full cyclic deck action on geometric two-primary torsion may be faithful.

This strengthens A.C2.17 from conductors supported on two primes to all odd conductors. Its additional ingredient is the controlled-field form of Castelnuovo–Severi, followed by the fact that the divisor of a function arising from a collision is supported on only two deck orbits.

## 2. Controlled fields: exact statement and proof

Let $k$ be algebraically closed, let $F/k$ be a one-variable function field, and fix an integer $d\ge1$. Suppose that a subfield $M\subset F$ is generated over $k$ by finitely many functions each of degree $d$ on the smooth proper curve of $F$. Put $e=[F:M]$. Then

\[
 e\mid d,\qquad g(M)\le(d/e-1)^2. \tag{AP.1}
\]

This is Poonen (2007), author PDF Section 2, Lemma 2.2 and Corollary 2.3, author p.3. We reproduce its induction to specify every index and avoid replacing a many-generator compositum by a two-generator one without justification.

For one generator $z$, the field $k(z)$ has genus zero and $[F:k(z)]=d$, so the assertion holds. At an induction stage write

\[
 [F:M]=d/s,\qquad g(M)\le(s-1)^2
\]

for an integer $s\mid d$. Adjoin a further degree-$d$ function $h$, and put $a=[M(h):M]$. Then

\[
 [F:M(h)]=d/(as),\qquad [M(h):k(h)]=as.
\]

The fields $M$ and $k(h)$ generate $M(h)$. The Castelnuovo–Severi inequality, Poonen Proposition 2.1, gives

\[
\begin{aligned}
g(M(h))
&\le a(s-1)^2+(a-1)(as-1)\\
&=(as-1)^2-as(a-1)(s-1)\\
&\le(as-1)^2.
\end{aligned}
\]

This proves (AP.1) for the enlarged field and completes the induction. All fields have constant field $k$. In the application below the original functions are separable, so all intermediate extensions of $F$ are separable as well.

## 3. An elementary degree bound for odd conductors

Let $r\ge2$ be the number of distinct prime divisors of an odd integer $n$, and put $d=2^r$. Then

\[
                        n>(d-1)^2. \tag{AP.2}
\]

For $r=2$, the least possible $n$ is $3\cdot5=15>9$. For $r\ge3$, at most one of its distinct prime divisors is less than five, so

\[
n\ge3\cdot5^{r-1}>4^r>(2^r-1)^2.
\]

The middle inequality holds at $r=3$ because $75>64$, and its left-to-right ratio is multiplied by $5/4$ whenever $r$ increases. Prime powers in $n$ only increase the lower bound.

## 4. The primitive endomorphism and its collision divisor

If $n$ has only one prime divisor, A.C2.8 proves the assertion. Hence assume $r\ge2$, and let

\[
 G=\langle\sigma\rangle,\qquad |G|=n,
\]

act on the connected cyclic étale cover $D\to C$ associated with $L$. Its genus is $n+1$.

For every prime $\ell\mid n$, define

\[
a_\ell=\sigma^{n/\ell},
\qquad
A=\prod_{\ell\mid n}(1-a_\ell)\in\operatorname{End}(J_D).
\tag{AP.3}
\]

Each $a_\ell$ has order $\ell$. On the cyclic character indexed by $i$, the scalar in (AP.3) is nonzero exactly when $\ell\nmid i$ for every $\ell\mid n$, or equivalently when $\gcd(i,n)=1$.

A.C2.5 identifies the nonzero character spaces of $H^1(D,\mathcal O_D)$ with the one-dimensional spaces $H^1(C,L^i)$. Under the stated orbit hypothesis, all $\varphi(n)$ primitive characters have nilpotent Frobenius. Consequently

\[
 f(D)\le f(C)+n-1-\varphi(n)
       \le n+1-\varphi(n)<n-1, \tag{AP.4}
\]

since $r\ge2$ implies $\varphi(n)\ge8$.

The endomorphism $A$ kills $J_D[2^\infty](\overline K)$ integrally. To check this, extend $\mathbf Z_2$ by a finite unramified extension containing the $n$-th roots of unity. The character idempotents of the odd-order cyclic group are integral; their Tate-module summands are free and have ranks given by reduction modulo two. The Artin–Schreier identification shows that every primitive summand has rank zero. Duality can invert character indices but preserves primitivity. On every remaining summand at least one factor $1-a_\ell$ in (AP.3) is exactly zero. Hence $A$ is zero on the étale two-adic Tate module and on all geometric two-primary torsion. This does not use the false assertion that an arbitrary endomorphism zero modulo two is zero on the Tate module.

Suppose that distinct points $P,Q\in C(K)$ gave equal point-section classes. Descend the cover and its action after a finite extension and choose a rational lift $P'$. A.3 supplies a lift $Q'$ with $[P'-Q']$ two-primary. Applying $A$ shows that the degree-zero divisor

\[
 \mathcal D=
 \sum_{S\subset\{\ell:\ell\mid n\}}
 (-1)^{|S|}
 \left(a_SP'-a_SQ'\right),\qquad
 a_S=\prod_{\ell\in S}a_\ell, \tag{AP.5}
\]

is principal.

The $2^r$ elements $a_S$ are distinct. If two products were equal, their quotient would express a product of elements of pairwise coprime prime orders as one. Projecting to each prime-order factor of the cyclic group forces every exponent to be zero. The free deck action makes the corresponding points within either orbit distinct. The two orbits $GP'$ and $GQ'$ are disjoint because their images on $C$ differ.

It follows that (AP.5) has $d=2^r$ distinct zeros and $d$ distinct poles, all of multiplicity one. Indeed the terms of even and odd subset cardinalities have equal counts, and changing from $P'$ to $Q'$ reverses the signs. Thus there is a rational function $f$ of degree $d$ with this divisor. It is separable, because its zeros and poles are simple.

## 5. The field generated by the deck translates

Work over $k=\overline K$ and set

\[
                    M=k(\gamma f:\gamma\in G)
                    \subset k(D),\qquad e=[k(D):M].
\]

Every generator has degree $d$. By (AP.1),

\[
                      e\mid d,\qquad
                      g(M)\le(d/e-1)^2. \tag{AP.6}
\]

If $e=1$, (AP.2) and (AP.6) give

\[
g(D)=n+1>(d-1)^2\ge g(D),
\]

a contradiction. Therefore $e>1$. It is a power of two because $d=2^r$.

Let $Z$ be the smooth proper curve with function field $M$. The field $M$ is $G$-stable by construction, so $D\to Z$ is $G$-equivariant. The induced action of $G$ on $Z$ is faithful: its kernel is a group of automorphisms of the degree-$e$ separable extension $k(D)/M$, so its order divides $e$; its order also divides the odd number $n$, hence it is trivial.

The action on $Z$ is free. If a point stabilizer were nontrivial, it would contain an element of some odd prime order $\ell\mid n$. Its action on $D$ is free, and the degree-$e$ fibre divisor above this point is invariant. The fibre decomposes into orbits of length $\ell$, with constant multiplicity on each orbit. This forces $\ell\mid e$, impossible.

Thus $Z\to Z/G$ is an étale degree-$n$ cover, and

\[
                  g(Z)-1=n(g(Z/G)-1). \tag{AP.7}
\]

Genus zero for $Z/G$ would make $g(Z)=1-n<0$. Therefore $g(Z)$ is either one or at least $n+1$. But (AP.2) and (AP.6) imply $g(Z)<n+1$. Consequently

\[
                             g(Z)=1. \tag{AP.8}
\]

## 6. The two-orbit support forces the map to be quadratic

Since $f\in M$, write $f=h\circ v$ for $v:D\to Z$ and $h:Z\to\mathbf P^1$. Take a geometric zero $z$ of $h$. Such a zero exists because $h$ is nonconstant. Every point above $z$ is a zero of $f$. The divisor (AP.5) is reduced, so the order of $h$ at $z$ is one, every ramification index of $v$ above $z$ is one, and its fibre contains exactly $e$ distinct geometric points.

Each of the two deck orbits $GP'$ and $GQ'$ maps injectively to $Z$. If $v(\gamma P')=v(\gamma'P')$, equivariance makes $(\gamma')^{-1}\gamma$ fix $v(P')$, and the action on $Z$ is free; hence $\gamma=\gamma'$. The same holds for $Q'$.

The zero fibre just considered is entirely contained in these two orbits. It therefore contains at most two points. Hence $e\le2$. Together with $e>1$, this gives

\[
                                e=2. \tag{AP.9}
\]

The separable map $D\to Z$ is thus a quadratic cover of a genus-one curve. Its involution $\tau$ commutes with $G$: the subfield $M$ is $G$-stable, so $G$ normalizes the order-two group of this quadratic extension, and that group has no nontrivial automorphism. A separate uniqueness theorem for all bielliptic involutions is not needed in this step.

## 7. The final two-rank contradiction

The nonempty ramification set of $D\to Z$ is $G$-stable and has cardinal a positive multiple of $n$. The Riemann–Hurwitz different has degree $2g(D)-2=2n$. Each ramification point in a separable quadratic extension in characteristic two has different exponent at least two. Thus the ramification set has exactly $n$ points.

The ramified Deuring–Shafarevich formula, Crew (1984), Corollary 1.8, gives

\[
                  f(D)=2f(Z)+n-1\ge n-1,
\]

contradicting (AP.4).

Alternatively, the elementary torsion proof in A.C2.17 applies verbatim. The free action of $G$ on the genus-one curve is by translations by an order-$n$ subgroup. If $R_0,\ldots,R_{n-1}$ form the ramification orbit, then $n[R_i-R_0]$, $1\le i<n$, are independent classes of order two. A principal relation would be invariant under $\tau$, so its function would descend to $Z$ and have even valuations at ramification points, whereas a nonzero relation coefficient gives the odd valuation $n$. Hence $f(D)\ge n-1$ without using the Deuring–Shafarevich formula.

The contradiction excludes the original section collision. The field-extension, form, and open-curve statements follow exactly as in A.C2.17: the cover and the chosen lifts are defined after finite extension, A.3 supplies the two-primary difference, and the proof is geometric. No specialization of the theta condition is required.

## 8. Scope of the advance

The primitive Prym may have two-rank zero while the deck action on the entire Jacobian remains faithful. This proof detects that situation for any odd conductor, without restricting the number of its distinct prime divisors. The low-degree function is not assumed to have degree four: its degree is $2^{\omega(n)}$, and the many-translates field bound plus two-orbit support reduces the possible map to a quadratic elliptic quotient.

The missing universal step is still an existence assertion: one needs an odd-order line bundle for which every primitive doubling orbit meets theta. One arbitrary prime-to-two theta point need not have this property. Density does not imply orbit saturation, and projecting or powering a torsion point does not preserve theta. No universal A1 conclusion is inferred from this conditional theorem.

## 9. Exact opened sources

- Poonen, B. (2007). *Gonality of modular curves in characteristic p.* Mathematical Research Letters, 14(4), 691–701. Primary author PDF <https://math.mit.edu/~poonen/papers/gonality.pdf>, dated April 16, 2006; Section 2, Proposition 2.1, Lemma 2.2 and Corollary 2.3, author p.3. Web source turn678view0. The controlled-field induction and its degrees are reproduced in Section 2. Existing bibliography key A_PrimPoonen2007.
- Crew, R. M. (1984). *Étale p-covers in characteristic p.* Compositio Mathematica, 52(1), 31–45. Primary archival PDF <https://www.numdam.org/item/CM_1984__52_1_31_0.pdf>. Corollary 1.8 and proof, printed pp.35–36, both opened and visually checked. Web sources turn677view0, turn678view1, turn678view2. Existing key A_PrimCrew1984. An elementary proof of the only needed lower bound is also retained.
- A.3, A.C2.5, A.C2.8 and A.C2.17 provide the already checked lifting, theta-character and integral torsion arguments identified above.

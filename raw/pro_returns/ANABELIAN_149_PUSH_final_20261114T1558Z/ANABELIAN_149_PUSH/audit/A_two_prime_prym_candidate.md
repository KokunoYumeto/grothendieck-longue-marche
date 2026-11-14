# Primitive Pryms supported on two odd primes

Status: independently approved by root and topos and integrated as A.C2.17 in sections/A_primitive_prym.tex. The finite-field agent inserted its input before A.C2.18 and synchronized the A ledger/report. This file preserves the full research derivation.

Question locus: 149; manuscript pp.17–17v; scans35–36. These are deductions in this audit, not attributions to the manuscript or to the cited sources.

## 1. Statement

Let $K$ be finitely generated over $\mathbf F_2$, let $C/K$ be smooth, proper and geometrically connected of genus two, and let $\Theta\subset J_C$ be the symmetric Raynaud theta curve of A.C2.5. Suppose that, over an algebraic closure of $K$, there is a line bundle $L$ of exact order

\[
n=\ell^a m^b,\qquad \ell\ne m\text{ odd primes},\quad a,b\ge1,
\]

such that every multiplication-by-two orbit on $(\mathbf Z/n)^\times$ meets

\[
\{i:L^i\in\Theta\}. \tag{TP.1}
\]

Then the geometrically prime-to-two point-section map of $C$ is injective. The assertion holds after every finite extension of the ground field, for forms satisfying the geometric hypothesis, and for every hyperbolic open subcurve of $C$.

No condition is imposed on the smaller-conductor character blocks. Their simultaneous survival may make the entire cyclic deck action on geometric two-primary torsion faithful. The proof uses an endomorphism of the Jacobian rather than an element of the deck group.

A simple sufficient hypothesis is

\[
L\in\Theta\text{ of exact order }n,\qquad
\langle2,-1\rangle=(\mathbf Z/n)^\times. \tag{TP.2}
\]

Consequently, **every exact-order-fifteen theta point suffices**, without an assumption concerning theta three- or five-torsion. More generally, every exact theta point of order $3^a5^b$, $a,b\ge1$, suffices.

Combining this with the prime-power case A.C2.8 gives a compact form: for every odd $n>1$, a theta point of exact order $n$ satisfying $\langle2,-1\rangle=(\mathbf Z/n)^\times$ implies point-section injectivity. Indeed that group-generation condition forces $n$ to have at most two distinct prime divisors; see Section 6.

## 2. A geometric lemma excluding degree-four functions

**Lemma.** Let $k$ be algebraically closed of characteristic two. Let $D/k$ be a smooth proper curve of genus $n+1$, where $n\ge15$ is odd, with a free action of a cyclic group $G$ of order $n$. If

\[
f(D)<n-1, \tag{TP.3}
\]

then there is no nonconstant rational function on $D$ of degree at most four.

Here $f(D)$ is the two-rank. The lemma is geometric; the action and pencil need not be defined over an original finite field.

### 2.1. Genus bounds used

The Castelnuovo–Severi inequality says: if $F_1,F_2\subset F$ are function fields of smooth proper curves over a perfect field, $F=F_1F_2$, $d_i=[F:F_i]$, and their genera are $g,g_1,g_2$, then

\[
g\le d_1g_1+d_2g_2+(d_1-1)(d_2-1). \tag{TP.4}
\]

This is Proposition 2.1 in the opened primary author version of Poonen (2007), author p.3, stated over a perfect field without a restriction on its characteristic. Its reference is Stichtenoth's textbook proof; that separate proof is not represented here as opened. The applications below use the exact field degrees specified at each step. For two rational subfields the bound also follows from the arithmetic genus of the image curve in $\mathbf P^1\times\mathbf P^1$.

### 2.2. Hyperellipticity and invariant pencils

The curve $D$ is not hyperelliptic. Otherwise its unique hyperelliptic involution is centralized by $G$, and $G$ acts on its genus-zero quotient. This action is faithful, since its kernel is a subgroup of the order-two hyperelliptic deck group. A generator of a finite odd cyclic subgroup of $\operatorname{PGL}_2(k)$ has a fixed point. Its fibre has degree two and is $G$-invariant. A free $G$-action partitions the geometric points of this fibre into orbits of size $n$, with equal multiplicities within each orbit. Its degree would be divisible by $n$, a contradiction.

The same argument shows that a $G$-invariant rational subfield $k(z)\subset k(D)$ of degree $d<n$ is impossible. The induced cyclic action on $\mathbf P^1$ is either trivial, so every fibre is invariant, or nontrivial and has a fixed point, so the fibre above that point is invariant. In either case its degree $d$ must be divisible by $n$.

Degree one is excluded by the genus and degree two by nonhyperellipticity. A degree-three pencil is unique: two distinct rational subfields of index three generate $k(D)$, so (TP.4) would give $g(D)\le4$. Uniqueness makes this pencil $G$-invariant, which is impossible.

There is no inseparability exception. Over the perfect field $k$, an inseparable rational function is a square. If its degree is at most four, a square root has degree at most two. The preceding exclusions therefore also exclude every inseparable function of degree at most four.

### 2.3. Two distinct tetragonal pencils force a bielliptic quotient

Suppose that $z\in k(D)$ has degree four. It is separable by the preceding paragraph. Its rational subfield cannot be $G$-invariant, so for some $\delta\in G$ the fields $k(z)$ and $k(\delta z)$ differ. Put

\[
F=k(z,\delta z),\qquad e=[k(D):F].
\]

Then $e\mid4$. If $e=4$, the two rational subfields are equal. If $e=1$, (TP.4) gives $g(D)\le9$, contrary to $g(D)=n+1\ge16$. Hence $e=2$. Both maps from the smooth curve $E$ with function field $F$ to $\mathbf P^1$ have degree two and generate $F$, so (TP.4) gives $g(E)\le1$.

If $g(E)=0$, the degree-two map $D\to E$ makes $D$ hyperelliptic. Therefore $g(E)=1$. The extension $k(D)/F$ is separable because $k(D)/k(z)$ is separable. It is a Galois quadratic extension, with involution $\tau$.

This bielliptic involution is unique. Two distinct degree-two elliptic subfields generate $k(D)$, and (TP.4) with $d_1=d_2=2$ and $g_1=g_2=1$ would give $g(D)\le5$. Thus every automorphism of $D$, including every element of $G$, commutes with $\tau$.

### 2.4. Ramification and the two-rank contradiction

The finite fixed-point set of $\tau$ is nonempty: $D\to E$ has different of degree $2g(D)-2=2n$. This set is $G$-stable and its $G$-action is free. Its cardinal $r$ is a positive multiple of $n$. At each ramification point of a separable quadratic extension in characteristic two, the different exponent is at least two: the zeroth and first lower ramification groups both have order two. Thus $2r\le2n$, and $r=n$.

The Deuring–Shafarevich formula gives

\[
f(D)-1=2(f(E)-1)+n,\qquad
f(D)=2f(E)+n-1\ge n-1, \tag{TP.5}
\]

contrary to (TP.3). The exact ramified formula is Crew (1984), Corollary 1.8, printed p.35, with its proof p.36. Both pages and their formulas were opened and inspected. An étale-only formula is not being substituted here.

The needed lower bound also has an elementary proof. The action of $G$ on $E$ is faithful because its kernel is a subgroup of $\langle\tau\rangle$. A nonidentity element of $G$ cannot fix a point on $E$: it has odd order, so it acts trivially on an at-most-two-point geometric fibre and would fix a point of $D$. Every fixed-point-free elliptic automorphism is a translation. To see this, choose an origin and write it as $T_b\circ u$, where $u$ fixes the origin. If $u\ne1$, the nonzero endomorphism $1-u$ is surjective and produces a fixed point. Hence $G$ acts by translations by an order-$n$ subgroup.

Choose one ramification orbit $P_0,\ldots,P_{n-1}$ and write $b_i$ for its images on $E$. The differences $b_i-b_0$ are killed by $n$. Since every ramification index is two, the classes

\[
T_i=n[P_i-P_0],\qquad 1\le i<n,
\]

are killed by two. They are linearly independent over $\mathbf F_2$. Otherwise a nonempty relation with coefficients $\epsilon_i\in\{0,1\}$ would give a function $v$ with

\[
\operatorname{div}(v)=
n\left(\sum_{i=1}^{n-1}\epsilon_iP_i
-\left(\sum_{i=1}^{n-1}\epsilon_i\right)P_0\right).
\]

This divisor is $\tau$-invariant, so $\tau(v)/v$ is constant. Its square is one, and in characteristic two the constant is one. Thus $v\in k(E)$, and its valuation at each ramification point is even. A nonzero $\epsilon_i$ gives valuation $n$, which is odd. This contradiction proves that $J_D[2](k)$ contains $(\mathbf Z/2)^{n-1}$, independently establishing the lower bound in (TP.5).

This proves the geometric lemma.

## 3. The primitive endomorphism of the cyclic cover

Let $D\to C$ be the connected cyclic étale cover of degree $n$ associated with $L$, with deck generator $\sigma$. Then $g(D)=n+1$.

Each nonzero character space $H^1(C,L^i)$ has dimension one. By A.C2.5, its entire doubling orbit has nilpotent Frobenius precisely when the orbit meets theta. Hypothesis (TP.1) kills every primitive character. There are $\varphi(n)$ such characters, so

\[
f(D)\le f(C)+(n-1-\varphi(n))
\le n+1-\varphi(n)<n-1, \tag{TP.6}
\]

because $\varphi(n)\ge8$. The geometric lemma applies.

Set

\[
a_0=\sigma^{n/\ell},\qquad b_0=\sigma^{n/m},\qquad
A=(1-a_0)(1-b_0)\in\operatorname{End}(J_D). \tag{TP.7}
\]

The automorphisms $a_0,b_0$ have distinct odd prime orders $\ell,m$. On the character of index $i$, the scalar of $A$ is nonzero exactly when neither $\ell$ nor $m$ divides $i$, equivalently when $i$ is primitive modulo $n$. Hence $A$ annihilates all geometric two-primary torsion.

For the integral justification, enlarge $\mathbf Z_2$ by a finite unramified extension containing all $n$-th roots of unity. Since $n$ is odd, the cyclic character idempotents act integrally on the étale two-adic Tate module. Each character summand is free, and its rank is its dimension modulo two. The Artin–Schreier identification in A.C2.5 and A.C2.8 implies that the primitive summands have rank zero. On each remaining summand one factor of (TP.7) is exactly zero. Therefore $A$ vanishes on $T_2J_D$, and hence on $J_D[2^\infty](k)$. This does not infer that an arbitrary endomorphism zero modulo two vanishes on the Tate module; it uses the integral odd-order character decomposition.

Equivalently, the abelian subvariety $\operatorname{im}(A)$ has two-rank zero. It is the primitive Prym selected by the two prime divisors. Smaller-conductor factors may be ordinary.

## 4. Excluding a point-section collision

Suppose that distinct $P,Q\in C(K)$ have equal geometrically prime-to-two point-section classes. After a finite extension of $K$, define $L,D,\sigma$ and make a chosen lift $P'$ rational. A.3 supplies a rational lift $Q'$ over $Q$ for which

\[
[P'-Q']\in J_D[2^\infty].
\]

Applying (TP.7) gives

\[
P'+a_0b_0P'+a_0Q'+b_0Q'
\ \sim\
a_0P'+b_0P'+Q'+a_0b_0Q'. \tag{TP.8}
\]

The group elements $1,a_0,b_0,a_0b_0$ are distinct, since their two cyclic subgroups have coprime orders. The deck action is free, and $P',Q'$ lie above distinct base points. Thus the eight points in (TP.8) are all distinct. This equivalence between disjoint effective degree-four divisors gives a rational function of degree four. Its zeros and poles are simple, so it is separable. This contradicts the geometric lemma.

All geometric arguments take place over the algebraic closure. The cover lifting and two-primary divisor difference are obtained over a finite extension of the given finitely generated field by A.3. Thus no specialization of the theta condition is required for this field scope. Restriction handles finite-extension forms, and functoriality to the compactification handles hyperbolic open subcurves.

This proves the statement.

## 5. Arithmetic corollaries

The divisor $\Theta$ is symmetric. If $L\in\Theta$, both $L$ and $L^{-1}$ lie on it. Consequently (TP.2) implies (TP.1), since every primitive doubling orbit contains either $1$ or $-1$.

For $n=15$ the two primitive doubling orbits are

\[
\{1,2,4,8\},\qquad\{14,13,11,7\}.
\]

They are interchanged by negation. Smaller-conductor characters contribute at most $2+4$, so $f(D)\le8$. A bielliptic alternative would force $f(D)\ge14$. Thus the separate exact-order-fifteen theta certificate for
$C:y^2+y=x+\alpha/x+\alpha/(x+1)$, $\alpha^2+\alpha+1=0$, proves A1 for that curve once checked. The positive conclusion does not depend on the separate small-order absence computations.

For every $a,b\ge1$,

\[
\operatorname{ord}_{3^a}(2)=2\cdot3^{a-1},\qquad
\operatorname{ord}_{5^b}(2)=4\cdot5^{b-1}.
\]

For the first formula, start with $v_3(2^2-1)=1$, and expand $(1+3^ru)^3-1$ with $3\nmid u$: its valuation is $r+1$. For the second, start with $v_5(2^4-1)=1$, and expand $(1+5^ru)^5-1$: its valuation is $r+1$. Reduction modulo three or five then forces the exact displayed orders at every level. Their greatest common divisor is two. Thus two has order $\varphi(3^a5^b)/2$ modulo $3^a5^b$. Also $-1\notin\langle2\rangle$: reduction modulo three requires the exponent to be odd, whereas reduction modulo five requires it to be $2\bmod4$. Adjoining $-1$ therefore gives the full unit group.

## 6. Why the all-n sufficient condition is valid

For an odd integer $n$ with $r$ distinct prime divisors, the Chinese remainder theorem gives

\[
(\mathbf Z/n)^\times/\bigl((\mathbf Z/n)^\times\bigr)^2
\simeq(\mathbf Z/2)^r.
\]

Two elements generate at most a two-dimensional quotient here. Thus $\langle2,-1\rangle=(\mathbf Z/n)^\times$ forces $r\le2$. For $r=1$, A.C2.8 applies; for $r=2$, the present theorem applies. This proves the all-$n$ statement without overlooking composite conductors.

## 7. Exact scope and remaining universal step

The theorem strengthens the nonfaithful-deck-action criterion. At degree fifteen, surviving order-three and order-five characters may have trivial common kernel. The endomorphism (TP.7) still kills both, and it turns a collision into a degree-four divisor relation instead of a degree-two relation. The geometric lemma is the additional input.

No existence of a suitable theta point on every ordinary genus-two curve is claimed. Prime-to-two torsion density does not control the number of prime divisors of its order, the subgroup generated by two and minus one, or simultaneous intersection with all primitive doubling orbits. A.C2.14 also prevents a fixed finite set of allowed odd primes from proving the universal statement by this method. Those existence questions remain separate.

## 8. Sources actually opened

- Poonen, B. (2007). *Gonality of modular curves in characteristic p.* Mathematical Research Letters, 14(4), 691–701. Author PDF dated April 16, 2006: https://math.mit.edu/~poonen/papers/gonality.pdf. Opened Section 2, Proposition 2.1, author p.3: Castelnuovo–Severi over a perfect field. Web source turn678view0. The uses above specify the exact field degrees. Its modular-curve assertions are not used.
- Crew, R. M. (1984). *Étale p-covers in characteristic p.* Compositio Mathematica, 52(1), 31–45. https://www.numdam.org/item/CM_1984__52_1_31_0.pdf. Opened Corollary 1.8, printed p.35, and its complete proof p.36; inspected formulas in PDF pages5–6. Web sources turn677view0, turn678view1, turn678view2. This is the ramified Deuring–Shafarevich formula. Section 2.4 gives an independent elementary proof of the lower bound required here.
- Yang, Y. (2016). *Formulas for local and global p-ranks of coverings of curves.* RIMS-1863. https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1863.pdf. Opened Proposition 3.2, author p.12, which corroborates the ramified formula and cites Crew. Web sources turn675view1, turn676view2.
- A.C2.5 and A.C2.8 supply the checked theta/Frobenius character calculation. A.3 supplies finite-cover lifting and the two-primary divisor difference.

The new geometric and representation-theoretic deductions are proved above. The original Castelnuovo–Severi and Deuring–Shafarevich discovery papers were not represented as opened.

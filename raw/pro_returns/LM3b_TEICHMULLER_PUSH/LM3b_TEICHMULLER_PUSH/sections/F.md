# F. The pentagon, finite images, and abelianization

Throughout this part, weight means the ordinary bracket length in the free Lie algebra, not the motivic weight, which is its negative double in the conventions of Hain and Matsumoto. We use $W_n$ for the rational solutions of antisymmetry, the three-cycle equation, and the pentagon in $\mathfrak t_4$. We write $V_n$ for antisymmetry, three-cycle, and cabling, without the pentagon. These are different equation spaces. The relevant manuscript statements are §26, folios 162–165, scans 323–326; §29, scans 370–371; and §§34–35, scans 479, 487–488, 496–505.

### F.1. Proved — The exact invariant special-derivation equation space

For every field of characteristic zero and every $n\geq2$, there is a natural vector-space isomorphism
$$
V_n\simeq(\operatorname{OutSDer}_n(F_2))^{\mathfrak S_3},
$$
where $V_n$ is the space of degree-$n$ Lie polynomials $\psi$ satisfying
$$
\psi(x,y)+\psi(y,x)=0,\qquad
\psi(x,y)+\psi(y,z)+\psi(z,x)=0,
$$
$$
[x,\psi(x,y)]-[x+y,\psi(z,y)]=0,\qquad z=-x-y.
$$
The last equation must be retained when comparing with special derivations. The first two homogeneous equations alone are not this invariant space.

**Proof.** Every special outer derivation has a representative with $D(x+y)=0$, obtained by subtracting its inner part at the third puncture. For $n\geq2$ this representative is unique: a degree-$n$ Lie element commuting with the degree-one element $x+y$ is zero. Its tangential coefficients $a_x,a_y$ are also unique, because the centralizer of $x$ or $y$ in a free Lie algebra consists of its scalar multiples. Set
$$
a_x=\psi(z,x),\quad a_y=\psi(z,y),\quad
D(x)=[a_x,x],\quad D(y)=[a_y,y].
$$
Antisymmetry and the three-cycle equation give $a_x=a_y-\psi(x,y)$. Consequently
$$
D(x+y)=[\psi(z,y),x+y]-[\psi(x,y),x]=0
$$
by cabling. Interchanging $x,y$ interchanges the two coefficients. Under the cycle $(x,y,z)\mapsto(y,z,x)$ the triple of tangential coefficients $(a_x,a_y,0)$ becomes $(0,\psi(x,y),\psi(x,z))$. Subtracting the common inner coefficient $\psi(x,z)$ recovers $(a_x,a_y,0)$. Thus the outer derivation is invariant.

Conversely, normalize an invariant derivation by $a_z=0$ and define $\psi(X,Y)=a_y(-X-Y,Y)$. Transposition invariance gives $a_x=\psi(z,x)$. Cycle invariance, followed by the unique normalization at $z$, gives $\psi(z,x)=-\psi(x,z)$ and $\psi(z,y)=\psi(x,y)-\psi(x,z)$. These are antisymmetry and the three-cycle equation after invertible linear substitutions. The equation $D(x+y)=0$ is cabling. This proves surjectivity as well as injectivity. In weight one the residual inner derivation must be divided out; the outer invariant space is zero. $\square$

For clarity, the weight-four polynomial
$$
[x,[x,[x,y]]]-4[x,[[x,y],y]]+[[[x,y],y],y]
$$
satisfies the first two homogeneous equations but fails cabling. Its coefficients are produced by the exact nullspace calculation. Thus simply retaining the lowest homogeneous parts of (I) and (II), while dropping the loop-preserving and nonlinear lifting requirements, gives the wrong tangent space. This refutes that particular shortcut in Lead 4, not its correctly formulated invariant-space comparison.

### F.2. Proved — Direct pentagon bounds and exact dimensions through weight twelve

Our independent calculation gives the following table. The middle column is the exact rational dimension before imposing the pentagon, with cabling retained. The rank column is computed in the actual infinitesimal braid algebra, modulo the prime $65521$; it provides a rigorous upper bound on the rational kernel dimension. The final column is the exact rational dimension, obtained by matching this bound with the independently known motivic lower bound.

| Weight $n$ | $\dim V_n$ | Pentagon rank on $V_n$, modulo $65521$ | $\dim W_n$ |
|---:|---:|---:|---:|
| 1 | 1 before the outer quotient | 1 | 0 |
| 2 | 0 | 0 | 0 |
| 3 | 1 | 0 | 1 |
| 4 | 0 | 0 | 0 |
| 5 | 1 | 0 | 1 |
| 6 | 0 | 0 | 0 |
| 7 | 2 | 1 | 1 |
| 8 | 1 | 0 | 1 |
| 9 | 4 | 3 | 1 |
| 10 | 2 | 1 | 1 |
| 11 | 9 | 7 | 2 |
| 12 | 7 | 5 | 2 |

**Proof and computational certificate.** The program `fg_prepare.py` constructs the Lyndon basis, expands every bracket in the free associative algebra over $\mathbb Z$, and solves the three displayed equations over $\mathbb Q$. It stores integral multiples of a rational basis of $V_n$. Independence of their reductions modulo $65521$ is checked separately in `fg_certify.py`; this check matters, because an arbitrary integral rescaling could otherwise lose rank modulo the chosen prime.

For the pentagon we use the faithful decomposition
$$
\mathfrak t_4/Z(\mathfrak t_4)
 =L(u,v,w)\rtimes L(a,b),
$$
with $u=t_{14},v=t_{24},w=t_{34},a=t_{12},b=t_{23}$ and
$$
t_{13}=-a-b-u-v-w.
$$
The derivations of the free fibre are
$$
D_a(u)=[u,v],\quad D_a(v)=[v,u],\quad D_a(w)=0,
$$
$$
D_b(u)=0,\quad D_b(v)=[v,w],\quad D_b(w)=[w,v].
$$
The braid relations verify this semidirect presentation; conversely it recovers all generators and defining relations, with the single central generator restored separately. For weight at least two the centre has no component, so this model loses no equation. The five pentagon substitutions are evaluated in this model, not in a commuting or metabelian quotient. `fg_pentagon.cpp` calculates their free-fibre component using exact modular word arithmetic. Their base component cancels identically. It records pivot word indices and ranks. In weight one, the direct pentagon defect is $-\alpha t_{12}-\beta t_{34}$, which forces zero; weight two is killed by the three-cycle equation.

Cabling is a rational consequence of the three defining equations (Drinfeld, 1990, Proposition 5.7; Bar-Natan, 1998, Theorem 5). Using it first is therefore an exact elimination of redundant unknowns in the rational problem. We do not assert that adding it preserves the solution space over every finite field. If $K_n$ is the saturated rational kernel of the remaining pentagon matrix in the integral candidate lattice, its reduction injects into the modular kernel. The listed ranks therefore give the asserted rational upper bounds. Brown's Theorem 1.1 and its introductory deduction of the faithful mixed Tate action supply a free Lie subalgebra on one generator in each odd weight at least three. The Witt product formula gives its dimensions $1,0,1,0,1,1,1,1,2,2$ in weights $3$ through $12$. They match the upper bounds. No all-weight claim is inferred from this finite calculation. $\square$

### F.3. Proved — Strictness in the coprime pro-prime cases

For every prime $\ell\geq5$, the group of special, label-preserving outer automorphisms of the free pro-$\ell$ tripod group centralizing its geometric $\mathfrak S_3$ is strictly larger than its subgroup satisfying the pentagon. Under the usual normalizer interpretation of the pro-$\ell$ pair equations, this is
$$
\mathrm{GT}_{\ell}^{1}\subsetneq\mathrm{GT}_{0,\ell}^{1}.
$$
Here the superscript denotes multiplier one; these groups are distinct from the full profinite groups.

**Proof.** The positive filtration subgroup of special outer automorphisms is pro-$\ell$: it is contained in the quotient of the kernel of the action on the Frattini quotient of a finitely generated free pro-$\ell$ group. The integral lifting theorem in A realizes every integral special outer derivation. The coprime fixed-point lifting lemma proved there applies to the geometric $\mathfrak S_3$, since $6$ is a unit in $\mathbb Z_\ell$. Thus every invariant integral leading term lifts to an actual automorphism centralizing $\mathfrak S_3$.

In weight seven the invariant lattice has rank two, while the rational pentagon solution space has dimension one by F.2. Choose an integral invariant element outside that rational line and lift it. If its lift satisfied the group pentagon, the first nonzero homogeneous term of that relation would satisfy the Lie pentagon. This contradicts our choice. The normal form identifying this centralizer with the two-relation pair group is the same explicit normal-form calculation used in LM3 E.4–E.7: normalize the image of one inertia generator, then compare with the transposition and three-cycle. Its relations are group relations before passing to leading terms. $\square$

### F.4. Open — The small primes and the full profinite strictness question

We do not prove $\widehat{\mathrm{GT}}\ne\widehat{\mathrm{GT}}_0$. Nor do we prove pro-$2$ or pro-$3$ strictness by F.3. The exact unresolved assertions are: (i) that some invariant weight-seven integral derivation outside the pentagon line lifts to an actual fixed point when $\ell=2$ or $3$; (ii) that some such pro-prime witness lies in the image of the full profinite two-relation group. The first obstruction is nonabelian fixed-point lifting for a group of order divisible by $\ell$; the second is the image of the full profinite automorphism group in its pronilpotent realization. Neither is removed by the integral special-automorphism lifting in A, which does not impose the finite symmetry simultaneously.

This is an attack beyond a dimension comparison: we have identified the correct homogeneous invariant space, evaluated its pentagon map, and integrated the witness at every prime at least five. What remains is an exact lifting problem, already in the tripod. Consequently the prompt's proposed refutation of the §26 arithmetic conjecture at $(0,3)$ remains unproved here. No non-Galois full profinite GT element is asserted.

### F.5. Proved — All two-generated abelian finite images through order five hundred

For every finite two-generated abelian group $Q\simeq C_a\times C_b$, with $a\mid b$, the image of $\widehat{\mathrm{GT}}$ in $\operatorname{Aut}(Q)$, for any chosen quotient of the free group, is precisely
$$
\{q\mapsto \lambda q:\lambda\in(\mathbb Z/b)^\times\}.
$$
Every element of this image is realized by $G_{\mathbb Q}$. The program enumerates all **792 isomorphism types** with $ab\leq500$, including the trivial group, and records every scalar residue. This is an exhaustive abelian-family computation, not an enumeration of nonabelian quotients of order at most five hundred.

**Proof.** In a GT pair, $f$ belongs to the closed commutator subgroup, so it disappears in every abelian quotient. Both generators are raised to the same multiplier $\lambda$. A scalar is invertible precisely when its residue is a unit modulo the exponent $b$. Conversely the cyclotomic character maps onto $(\mathbb Z/b)^\times$, by the action on $\mathbb Q(\zeta_b)$, and $G_{\mathbb Q}$ embeds in $\widehat{\mathrm{GT}}$. This proves both inclusions and arithmetic realization, with no search for an unknown extension required.

For actual abelian GT-shadow objects, rather than just their actions on $F_2$-quotients, Dolgushev, Le, and Lorenz (2024), Theorem B.2 and Remark B.3, give the pairs $(m,1)$ with $\gcd(2m+1,N_{\rm ord})=1$. We reproduce the arithmetic realization: choose a cyclotomic multiplier congruent to $2m+1$ modulo $2N_{\rm ord}$. Then $(\lambda-1)/2\equiv m\pmod {N_{\rm ord}}$. This also distinguishes the two half-parameter choices when $N_{\rm ord}$ is even. `fh_finite.py` enumerates these for $N_{\rm ord}\leq22$, corresponding to the homocyclic $F_2$-quotients of order at most $22^2$.

The unmarked Fermat/Kummer cover can have field of moduli $\mathbb Q$ even though its deck marking requires roots of unity. Accordingly the arithmetic certificate is the cyclotomic action on the **marked** cover; its unmarked field of moduli alone would not certify all automorphisms of $Q$. $\square$

### F.6. Open — Nonabelian shadows and finite arithmetic exhaustion

For every nonabelian characteristic finite quotient $Q$ of $\widehat F_2$, determine whether every restriction of a genuine element of $\widehat{\mathrm{GT}}$ is the restriction of a Galois element. F.13 proves this for nilpotency class at most two, including an explicit quaternion dessin, but does not settle arbitrary $Q$. Moreover a solution of finitely many shadow equations need not lift to a genuine GT element; compatible lifting through the braid-tower quotients is an additional condition (Dolgushev et al., 2024, Theorem 3.8).

The settled families are the abelian quotients, including their even-level shadow half-parameters, and all characteristic quotients of nilpotency class at most two. In the latter family the commutator part of a GT pair acts trivially by conjugation. The first nilpotency class not covered by this reduction is three; there the conjugation by that part can be nontrivial. A concrete next test is the characteristic free class-three exponent-five quotient of order $5^5$, with its genuine GT image and its arithmetic image compared. This specifies a next finite instance, not a claim of minimality by group order. Nonnilpotent quotients are also untreated. We attach a complete quaternion computation, but no exhaustive nonabelian enumeration through order five hundred, and report no unrealized genuine shadow.

### F.7. Proved — Integral scalar coinvariants, including the prime two

For $w>0$ define $J_{\ell,w}=(u^w-1:u\in\mathbb Z_\ell^\times)\subset\mathbb Z_\ell$. Then
$$
\mathbb Z_\ell/J_{\ell,w}=
\begin{cases}
0,&\ell>2,\ (\ell-1)\nmid w,\\
\mathbb Z/\ell^{1+v_\ell(w)},&\ell>2,\ (\ell-1)\mid w,\\
\mathbb Z/2,&\ell=2,\ w\text{ odd},\\
\mathbb Z/2^{2+v_2(w)},&\ell=2,\ w\text{ even}.
\end{cases}
$$
Thus Lead 5's proposed nonvanishing in the integral scalar model is correct. In the odd generating weights $3,5,7,9,11$ the model has no odd-prime coinvariants but has a nonzero $\mathbb F_2$ quotient in every weight.

**Proof.** For odd $\ell$, a Teichmüller unit detects the failure of divisibility by $\ell-1$. When that divisibility holds, every unit has $u^w\equiv1\pmod\ell$, and the minimum valuation is $1+v_\ell(w)$, attained by $u=1+\ell$, by the binomial expansion. For $\ell=2$, $u=-1$ gives valuation one for odd $w$. For even $w$, factor $u^w-1$ successively by squaring; every odd $u$ gives valuation at least $2+v_2(w)$, attained by $u=3$. These arguments are valid for every prime, without replacing $\mathbb Z_2^\times$ by $1+4\mathbb Z_2$. The code verifies the predicted ideal in a sufficiently high finite residue ring for $w\leq12$ and $\ell=2,3,5,7,11,13$. $\square$

### F.8. Refuted — Automatic extension of a character from scalar coinvariants

For arbitrary group extensions, a nonzero conjugation-invariant character of the kernel need not extend to the whole group. This general inference is refuted below; no nonextending character inside the actual GT group is asserted. For a finite abelian coefficient group $A$ with trivial action, the obstruction in the actual cyclotomic extension is the transgression
$$
H^1(K,A)^{\mathbb Z_\ell^\times}\longrightarrow
H^2(\mathbb Z_\ell^\times,A)
$$
for the actual extension $1\to K\to\mathrm{GT}_\ell\to\mathbb Z_\ell^\times\to1$, whenever the displayed quotient is used. The kernel of transgression is the image of restriction from $H^1(\mathrm{GT}_\ell,A)$.

**Proof and counterexample.** In $1\to C_2\to Q_8\to C_2^2\to1$, the central kernel has a nonzero invariant character to $C_2$. Every homomorphism $Q_8\to C_2$ kills that kernel, since $-1=[i,j]$. Thus its nonzero character does not extend. The program constructs the multiplication table, checks associativity, enumerates all four homomorphisms to $C_2$, and verifies their trivial restrictions. The five-term cohomology sequence gives the stated obstruction for the actual cyclotomic extension as well, without asserting that its transgression is nonzero.

There is a useful distinction between primes. For odd $\ell$ and $\ell$-primary $A$, one has $H^2(\mathbb Z_\ell^\times,A)=0$, so every **actual** invariant kernel character does extend. Indeed, $\mathbb Z_\ell^\times\cong\mu_{\ell-1}\times\mathbb Z_\ell$; averaging kills higher cohomology of the first factor. For the second, the description $H^2(C_{\ell^m},A)=A/\ell^m A$ identifies inflation to $C_{\ell^{m+1}}$ with multiplication by $\ell$. Its direct limit is zero for finite $\ell$-primary $A$. At two, the torsion factor $C_2\subset\mathbb Z_2^\times$ means that this vanishing need not hold. Thus in the odd-prime case the unproved step is already the construction of an actual invariant kernel character from the graded coinvariants; at two, extension can require an additional argument. This vanishing concerns only the displayed $\mathbb Z_\ell^\times$ quotient; it does not apply automatically to the full profinite quotient $\widehat{\mathbb Z}^{\times}$, whose kernel is a different group. F.7 establishes neither such actual character nor an extra full profinite GT character. $\square$

### F.9. Known — The precise rational abelianization statement

In the category of affine pro-algebraic groups over a characteristic-zero field $k$, the scalar character induces
$$
\mathrm{GRT}^{\rm ab}\simeq\mathbb G_m.
$$
After the all-weight result verified in G, write $\mathfrak{grt}_{1,\mathrm{gr}}$ for the graded direct sum and $\widehat{\mathfrak{grt}}_1$ for its degree completion. Their graded and continuous Lie abelianizations, respectively, and the multiplier-one group abelianization are
$$
\begin{gathered}
\mathfrak{grt}_{1,\mathrm{gr}}^{\rm ab}=\bigoplus_{j\geq1} k\sigma_{2j+1},\qquad
(\widehat{\mathfrak{grt}}_1)^{\rm ab,cont}=\prod_{j\geq1} k\sigma_{2j+1},\\
\mathrm{GRT}_1^{\rm ab}=\prod_{j\geq1}\mathbb G_a(2j+1).
\end{gathered}
$$
An associator transports this statement to $\mathrm{GT}(k)$ in its pro-algebraic interpretation. The isomorphism with the graded form depends on that associator.

**Reduction to the cited results.** Hain and Matsumoto (2003), Theorem 7.3, compute the free graded Lie algebra of the weighted completion of $G_{\mathbb Q,\{\ell\}}$, initially including weight one. Their Theorem 8.4 identifies the rationalized graded image of the outer action; Lemma 8.5 kills weight one. Remark 8.6, using Ihara's nonvanishing of the Soulé classes, identifies its abelianization as the sum of odd Tate lines of weight at least three. Brown (2012), Theorem 1.1 and the deduction of faithfulness in its introduction, provide the free motivic lower bound. G supplies the matching upper bound for the entire equation algebra. This proves the multiplier-one formula, rather than merely identifying an arithmetic subalgebra.

For the full group, every positive-weight vector $v$ is a commutator with the torus in the abelian quotient: a scalar $2$ acts by $2^w$, and $2^w-1$ is invertible in $k$. Apply this successively to each finite weight quotient and take closed commutators before the inverse limit. The remaining quotient is $\mathbb G_m$. In fact this full-group argument needs positivity of the weights, not freeness. It is the exact rational analogue of the cyclotomic abelianization on scans 323–329. Division by $2^w-1$ is exactly the operation that fails in the integral calculation F.7. $\square$

### F.10. Known — Which Lie tower has automorphism group GT

Let $\mathrm{PaB}_k^{\rm un}$ be the parenthesized braid groupoid with unipotent completion on its pure braid groups, retaining permutation data, units, cabling, juxtaposition, and strand removal. Its structure-preserving automorphism group, allowing the braiding multiplier, is $\mathrm{GT}(k)$. Fixing the multiplier gives the corresponding kernel. An associator identifies it with the parenthesized infinitesimal-braid model and its graded automorphism group.

**Reduction.** Bar-Natan (1998), §2.1, Claim 2.6, §3, and Proposition 5.3, express the category by a braiding and one reassociation arrow. An automorphism is determined by their images: the former supplies the scalar and the latter the group-like series. The two hexagons and pentagon are precisely the relations required for these images to extend to a functor. Preservation of units and strand removal supplies the normalizations; invertibility supplies an automorphism. His Definition 2.4 fixes the braiding and therefore describes the multiplier-one group. Allowing chord scaling by $k^\times$, and transporting it across an associator, restores the scalar factor of the full GT group. His Theorem 4 provides that associator comparison; Theorem 5 removes the redundant infinitesimal cabling constraint in characteristic zero. This derives the automorphism assertion from a presentation, rather than from an equality of dimensions.

The strict boundary exit category of the manuscript also has noninvertible smoothing arrows. It is not the parenthesized braid **groupoid**. Thus this theorem proves the stated operadic Lie approximation. An unqualified assertion for an unspecified termwise completion of all exit-category Hom-sets would require an extra comparison and is not silently included. Neither version implies equality of full profinite groups: rational unipotent realization forgets finite torsion and does not provide finite-quotient arithmetic exhaustion. $\square$

### F.11. Proved — The finite-quotient counterpart of the upper bound, in the settled family

The exact full profinite counterpart is: for every open normal $V\triangleleft\widehat{\mathrm{GT}}$, the map $G_{\mathbb Q}\to\widehat{\mathrm{GT}}/V$ is onto. LM3 E.22 proves its equivalence with $G_{\mathbb Q}=\widehat{\mathrm{GT}}$ by compactness. F.5 proves this statement for every finite quotient obtained from a cyclotomic scalar action on an abelian quotient of $F_2$, with arbitrary modulus, not merely those in the table.

**Proof of the additional assertion.** Such a quotient is a quotient of $(\mathbb Z/m)^\times$. The field $\mathbb Q(\zeta_m)$ supplies the required surjection, and composing a surjection with any quotient remains surjective. This is a finite-exhaustion proof for a cofiltered family, but that family is not cofinal in all finite GT quotients. The missing cofinality cannot be supplied by rational dimension estimates. $\square$

### F.12. Open — The full profinite abelianization

Determine the kernel of $\lambda^{\rm ab}:\widehat{\mathrm{GT}}^{\rm ab}\to\widehat{\mathbb Z}^{\times}$. Our computations determine scalar coinvariants of individual integral graded lines and all abelian images of $F_2$ in the stated range. They do not determine the abelianization of the full GT group. The remaining tasks include the integral lattices in its actual filtration, construction of actual invariant kernel characters, extension transgressions where these are not forced to vanish as in F.8, and compatibility among all primes and nonabelian finite quotients. The first unresolved case in this attack is construction and extension of an actual degree-three $2$-primary kernel character across the cyclotomic extension. No absence or existence of an extra full profinite character is claimed.

### F.13. Proved — Class-two finite images and an explicit nonabelian quaternion dessin

Fix the standard based embedding of $\widehat{\mathrm{GT}}$ in $\operatorname{Aut}(\widehat F_2)$, with ordered generators $x,y$. Let $N$ be an open characteristic subgroup and let $Q=\widehat F_2/N$ have nilpotency class at most two. Then the images of $G_{\mathbb Q}$ and $\widehat{\mathrm{GT}}$ in $\operatorname{Aut}(Q)$ are equal. Their common image factors through the cyclotomic multiplier modulo the exponent of $Q$.

In particular, for the characteristic quaternion quotient $x\mapsto i$, $y\mapsto j$ of order eight, that genuine automorphism image has order two:
$$
\{1,\ (i\mapsto i^{-1},\ j\mapsto j^{-1})\}.
$$
Its outer image is trivial. An explicit geometrically regular dessin defined over $\mathbb Q$ and realizing the quotient is the smooth projective model of
$$
C:\quad Y^2=X^5-X,\qquad
t=\frac{(X^2+1)^2}{4X^2}:C\longrightarrow\mathbb P^1_{\mathbb Q}.
$$
The map has degree eight and ramification profiles $(4,4)$ over each of $0,1,\infty$.

**Proof.** Write a genuine GT automorphism as
$$
x\longmapsto x^\lambda,\qquad
y\longmapsto f^{-1}y^\lambda f,
\qquad f\in[\widehat F_2,\widehat F_2].
$$
Since $[Q,Q]\subseteq Z(Q)$, its induced automorphism sends the two chosen generator images to their $\lambda$-powers. These two values determine the entire homomorphism. If $e$ is the exponent of $Q$, they depend only on $\lambda\bmod e$. Choose $\sigma\in G_{\mathbb Q}$ with $\chi(\sigma)\equiv\lambda\pmod e$, using cyclotomic surjectivity. Its GT image induces exactly the same automorphism on $Q$. Characteristicness of $N$ ensures that both genuine automorphisms descend. This proves equality of the images. The description is by **powers of the chosen generators**; it does not identify the automorphism with the usually nonmultiplicative map $q\mapsto q^\lambda$ on all of a nonabelian group.

For $Q_8$, every ordered generating pair consists of two noncentral elements from distinct cyclic subgroups of order four. There are $6\cdot4=24$ such pairs. Each satisfies $u^2=v^2=-1$ and $vu=u^{-1}v$, so there is a unique automorphism sending $(i,j)$ to $(u,v)$. Consequently every epimorphism $\widehat F_2\to Q_8$ has the same kernel. That kernel is characteristic, since precomposition by an automorphism gives another epimorphism. The preceding image formula now gives the two displayed maps according to $\lambda\bmod4$. Both occur because $\chi\bmod4$ is onto. Simultaneous inversion of $i,j$ is conjugation by $ij$, which proves the outer assertion.

To verify the dessin directly, over $\mathbb Q(\sqrt{-1})$ put
$$
a(X,Y)=(-X,\sqrt{-1}Y),\qquad
b(X,Y)=(X^{-1},\sqrt{-1}Y/X^3),\qquad h(X,Y)=(X,-Y).
$$
These preserve the curve and $t$, and satisfy $a^2=b^2=h$, $h^2=1$, and $ab=hba$. They generate eight distinct deck transformations. The rational function of $X$ has degree four, while the hyperelliptic map has degree two, so these account for the full deck group. The polynomial $X^5-X$ is square-free; hence the curve has genus two. The identities
$$
t=\frac{(X^2+1)^2}{4X^2},\qquad
t-1=\frac{(X^2-1)^2}{4X^2}
$$
give order-two zeros on the $X$-line at $\pm\sqrt{-1}$ and $\pm1$, and order-two poles at $0,\infty$. Each is a branch point of the hyperelliptic map, so the composite has ramification index four there. Riemann--Hurwitz gives total ramification $18=2\cdot2-2+2\cdot8$, excluding any other branch point. Thus this is a geometrically Galois three-point cover defined over $\mathbb Q$, with geometric deck group $Q_8$ and displayed deck marking over $\mathbb Q(\sqrt{-1})$. Choose its identification with the ordered free-group quotient as above. Coefficient conjugation on the displayed deck formulas sends both $a,b$ to their inverses; its fixed deck subgroup is $\langle ab\rangle\simeq C_4$. In particular we do not assert that $\mathbb Q(C)/\mathbb Q(t)$ is $Q_8$-Galois over $\mathbb Q$. The arithmetic realization of the genuine quotient image is the cyclotomic argument already proved, not an inference from the unmarked field of moduli alone.

The independent program `quaternion_shadow.py` checks all $512$ associativity triples, all $24$ generating-pair automorphisms, the central commutator subgroup, both GT restrictions, all $64$ deck-composition identities, preservation of the curve and Belyi function, and coefficient conjugation. Its JSON and text output are included. This settles a genuine nonabelian quotient and the stated class-two family; it does not enumerate all nonabelian quotients of order at most five hundred. $\square$

# Characteristic-two point-separation extension: proof and audit

## Established statements

The parent independently reviewed and accepted the complete proofs of A.C2.1–A.C2.3. They are in `sections/A_char2_extension.tex`; their machine-readable rows are `audit/A_char2_results.json`.

| Statement | Result | Exact mechanism |
|---|---|---|
| A.C2.1 | Point-section injectivity for the ordinary genus-two family y²+y=ax+b/x+c/(x+1), abc≠0, (a+b+c)³+abc=0 | An explicit connected cyclic cubic étale cover has two jointly point-injective maps to one smooth supersingular elliptic curve. |
| A.C2.2 | Exact obstruction to that cubic construction | Such a supersingular elliptic quotient exists precisely on the stated hypersurface. Off it, every cyclic cubic cover has ordinary Jacobian. The explicit F4 example (1,1,α) lies off it. All lifted-involution cubic elliptic quotients of the 2-rank-one family are ordinary too. |
| A.C2.3 | Point-section injectivity for y²+y=sx³+x+s⁵/x, s≠0 | An explicit cyclic quintic étale cover has two jointly point-injective maps to a genus-two curve of 2-rank zero. |

The positive results hold over fields finitely generated over F2, after finite extensions, for forms that become isomorphic after finite extension, and for hyperbolic open subcurves. This field scope follows by applying A.1 and A.3 to the actual covers and maps; it does not assume the curve is constant over a finite field.

### Ordinary family

The parameterization is b=av³, c=a(v+1)³ with v≠0,1. The explicit cubic torsor is obtained from

- h=x²+x, Y=hy, f=ax⁵+(a+b+c)x³+cx²+bx;
- u=x²+v²;
- d²+d=a²v²+a;
- A=ax³+dx²+(d+a+b+c)x+b;
- Norm(A+Y)=a²u³ and z³=(A+Y)/a.

Its elliptic quotient is a[W³+(X²+v²Z²)W]=X²Z+XZ². Smoothness is checked by its partial derivatives. Supersingularity is proved by a direct Cech computation of Frobenius on H1(O): in characteristic two the scalar is the XYZ coefficient of the plane cubic, which is zero here. The proof explicitly checks the exceptional finite fibre and all three points at infinity for the two maps. Thus its geometric point-injectivity is not inferred from finite enumeration.

### Exhaustiveness of the cubic obstruction

The proof treats every nonzero geometric 3-torsion class. Its unique reduced degree-two divisor cannot have reduced degree one, because that would require a function with a single pole of order three at a genus-two Weierstrass point. The torsion function lies in L(6∞)=⟨1,x,x²,x³,Y⟩ and has nonzero Y coefficient: an invariant divisor would represent a class killed by two. The general norm equation is therefore exactly A²+hA+f=L²u³ with u monic quadratic; no exceptional torsor was discarded.

The quotient plane cubic has Hasse scalar Lu1. Setting u1=0 and comparing coefficients gives u0³=(b/a)² and u0²+u0+1=((b+c)/a)². These imply the stated parameter condition. The converse is the explicit positive construction. The proof of J_D isogenous to J_C×E² uses the dihedral action on an auxiliary rational Tate module and verifies that the two reflection-fixed subspaces intersect trivially and span the Prym. It remains valid in characteristic two.

The result is an obstruction to a **specified degree-three method**. It is not a counterexample to point-section injectivity, to all odd-degree covers, or to all correspondences.

### The quintic family

For C_s use Y=xy and d²+d=s⁸. Then

A=x⁵+sx⁴+x³+x²+dx+s⁵, u=x²+s², and Norm(A+Y)=u⁵.

The connected étale cover z⁵=A+Y has involution quotient obtained by putting w=z+u/z and t=(x+s)²+(x+s)w+w². The identity x=wt² gives

V²+V=(t⁴+t²+1)(t+s²)/s².

This is a genus-two Artin–Schreier curve with one pole of order five. Its regular differential basis dt,t dt has Cartier images 0,dt, so its 2-rank is zero. The two quotient maps are jointly injective for a group-theoretic reason: a collision for two different reflections would give a fixed point of a nontrivial deck transformation of the étale cyclic cover. This handles every geometric fibre simultaneously.

## Exact computations

`code/A_char2_extension_checks.py` and its output record **21 passing checks**, including both norm identities, parameter elimination, the plane-cubic Hasse scalar and partial derivatives, the rank-one cubic obstruction, the fifth Dickson identity, the birational quotient transformations, Cartier nilpotence, the dihedral representation calculation, and the explicit F4 obstruction. The finite enumeration over F4 finds only the triples (a,a,a) on the ordinary special locus among nonzero F4 parameter triples. That finite calculation is supplementary; it does not replace the general parameter proof.

## Additional thirteen-fold construction: independently reviewed

A.C2.4 is in `sections/A_char2_thirteen.tex`, kept separate for assembly. The finite-field agent independently reviewed and accepted its locally exact differential, twisted Frobenius, cyclic eigenspace, wild local ramification, Jacobian isogeny, and joint point-separation arguments. Its Proved row is now included in `A_char2_results.json`.

The curve is C0:y²+y=x³+1/x. Under u=1/x, V=u²y it becomes V²+u²V=u⁵+u. An explicit point R=(α,β) over F16, with α²+α+1=0 and β²+α²β=1, has [R−∞] of exact order thirteen. The displayed polynomial function has norm (u+α)¹³, vanishes at R, has nonzero conjugate value α, and has pole order thirteen at infinity.

The proof identifies the locally exact differential line bundle as O(∞), using div(d(1/u))=2∞ and the local square-coefficient description of exact differentials in characteristic two. Tensoring 0→O→F_*O→B→0 by L=O(R−∞) shows that Frobenius H1(L)→H1(L²) is zero. The twelve nontrivial character spaces of the cyclic thirteen-fold cover form one cycle under multiplication by two modulo thirteen, so the new Frobenius part is nilpotent. It follows that the covering curve has 2-rank one. The dihedral quotient has genus six and 2-rank zero by the same Jacobian isogeny calculation. Two conjugate quotient maps then provide point separation.

`code/A_char2_thirteen_checks.py` and its output record **11 passing exact checks** for this construction. In particular the full polynomial norm identity is verified in F2[α,β] modulo the two stated relations. The proof for the Frobenius and section steps is written separately; those steps are not inferred from the finite code.

This curve is the second split 2-rank-one genus-two normal form over F2. These calculations do not classify all ordinary genus-two curves over F2: their three branch points need not all be rational.

## Exact theta criterion and unresolved order selection

`sections/A_char2_theta.tex` contains A.C2.5 (Proved) and A.C2.6 (Unresolved), both independently reviewed by the parent. The criterion applies to every genus-two curve in characteristic two. The locally exact differential line bundle satisfies B²=ω, so its theta translate is symmetric. For an odd-order line bundle L, each nonzero H1(L^i) is one-dimensional, and its Frobenius map vanishes precisely when L^i lies on theta. Thus the new 2-rank is exactly the number of character indices in multiplication-by-two orbits that miss theta altogether.

If every orbit meets theta, a lifted hyperelliptic involution gives a genus-(n−1)/2 quotient of 2-rank zero. The complete proof includes the lift, wild different exponents, the general odd-dihedral Jacobian isogeny, and joint point separation by two reflection quotients. For prime ell, a nonzero ell-torsion theta point suffices when the subgroup generated by 2 and −1 is all of (Z/ell)×. This includes ell=7, where the two doubling orbits are exchanged by sign; primitivity of 2 alone is unnecessary.

The unresolved step is finding such a point, or enough simultaneous theta intersections, for an arbitrary curve over Fbar2. Yang's density theorem does not control its order or the distribution of its multiples among doubling orbits. Composite orders require proper-conductor blocks as well as primitive characters. This distinction is concrete: A.C2.2 implies that a 2-rank-one genus-two curve has theta∩J[3]={0}, so every cyclic degree divisible by three retains an ordinary order-three block. For ordinary curves off the cubic special locus, the corresponding statement is that **nonzero** theta 3-torsion is absent; zero is not on their theta divisor either.

`code/A_char2_theta_checks.py` and its output contain **fourteen passing arithmetic checks**, including the single cycle at thirteen, the two sign-exchanged cycles at seven, an unhit cycle at seventeen, the surviving order-three block at degree nine, 480 exact stable-rank cases, the odd-dihedral generator condition, the exact deck kernels at degrees 9, 15, 25 and 27, and the three-dimensional free-orbit example below. These are finite certificates for the arithmetic examples, not a substitute for the general proof.

The exact ratio f(D)/n is f(C)/n plus the proportion of character indices in unhit cycles. Therefore one theta intersection does not imply that normalized 2-rank can be made arbitrarily small. No such quantitative tower construction is claimed.

## A weaker deck-action criterion

`sections/A_char2_deck.tex` contains A.C2.7–8. These strengthen the theta application without asserting a 2-rank-zero quotient. Any nontrivial odd Galois étale cover D of a proper genus-at-least-two curve C is nonhyperelliptic: an odd-order deck transformation would otherwise descend to P1 and have a fixed point above a fixed base point. On this nonhyperelliptic D, a difference [Q′−P′] across distinct fibres has trivial deck stabilizer, because a stabilizer element would produce two distinct linearly equivalent effective degree-two divisors.

A hypothetical point-section collision supplies such a difference in two-primary torsion. Hence the deck action on J_D[2] must be faithful: a finite odd-order matrix congruent to the identity modulo two is the identity on the full two-adic étale Tate module. The averaging projector splits off the f(C)-dimensional invariant part integrally, so the remaining f(D)−f(C) dimensions must carry a faithful F2-representation. This proves a precise representation-theoretic lower bound. It does not establish a lower bound linear in the degree.

For cyclic genus-two covers the kernel is computed exactly by gcd(n, surviving character indices). At degree ell^a, eliminating every primitive-character orbit leaves a nontrivial subgroup of order at least ell in the kernel even when smaller-conductor blocks survive. Thus a prime-power torsion theta point with <2,−1> equal to all units suffices. Degree nine can therefore work despite the universal ordinary order-three block of the rank-one family. This is a conditional criterion: no suitable nine-torsion theta point is asserted to exist on an arbitrary curve. At degree fifteen, surviving order-three and order-five characters together give a faithful action, illustrating why merely eliminating all primitive characters is not enough for a general composite degree.

The faithful-action obstruction supplies a rigorous portion of the proposed fibre-pairing/logarithmic-differential route. The stronger assertion that such a collision forces f(D) at least the cover degree, and the existence of towers whose normalized p-rank tends to zero, remain unproved here.

The proposed linear-independence inference already fails for abstract modules. Let alpha satisfy alpha³+alpha+1=0 in F8, let a generator g of the cyclic group of order seven act by multiplication by alpha, and take v=1. The orbit of v consists of all seven nonzero vectors of the three-dimensional F2-vector space F8 and has trivial stabilizer. Nevertheless v+gv+g³v=0. The exact field computation is included in the certificate. Thus a free deck-equivariant orbit of torsion classes or logarithmic differentials does not by itself supply seven independent differentials. This is an obstruction to that abstract inference, not a geometric counterexample to a possible stronger theorem.

### Prime-power extraction attempt: exact failure

Let L in theta have odd order n=ell^a*m with gcd(ell,m)=1. The algebraic extraction L^m has ell-power order, but no argument preserves theta under this multiplication map. Theta is not a subgroup. In the rank-one genus-two case B=O(W) for a Weierstrass point W, a nonzero odd-order theta point is L=O(R−W) with R non-Weierstrass. Already L² cannot lie on theta: that would give 2R linearly equivalent to S+W for a point S, a pair of distinct effective degree-two divisors, forcing 2R to be the hyperelliptic fibre and R to be Weierstrass. This supplies a direct geometric warning against silently preserving theta under scalar operations.

Passing to an intermediate cover does not fix the missing step. If Y→C is the cyclic cover of degree m associated with the order-m subgroup generated by L^(ell^a), then the pullback of L has exact order ell^a. The projection formula decomposes H1(Y, pullback L^i) into m summands H1(C,L^(i+j*ell^a)). The single zero edge arising from L in theta kills one one-dimensional summand, not the whole m-dimensional character space on Y. One must still eliminate every summand carrying the relevant primitive ell-power character. This is exactly the surviving-character condition of A.C2.8 in different coordinates.

An additional primary source was checked to see whether it supplied prime or prime-power orders. Pop and Saïdi (2003), *On the Specialization Homomorphism of Fundamental Groups of Curves in Positive Characteristic*, printed pp.113–114, Propositions2.1–2.3, at <https://library.slmath.org/books/Book41/files/pop.pdf>, says “pairwise prime orders.” The proof on p.113 constructs a point whose order is relatively prime to a previously fixed integer r while prescribing one s-primary component. Consequently the phrase means **pairwise coprime orders** in that proof; it does not supply points of individually prime order. Other primary components remain uncontrolled. The stronger prime-degree phrasing in some later summaries is not used here. The full thirteen-page primary PDF was opened and the exact proof, not merely the theorem wording, was inspected.

The finite-field primary-component surjectivity behind that proof and behind Bogomolov–Tschinkel is useful, but a surjective projection of theta to one primary torsion subgroup does not assert that theta contains that subgroup's nonzero points: the unwanted components of the lifted point need not vanish. The extraction route therefore remains incomplete at a precisely identified geometric step.

## Opened sources and elementary inputs

The section-lifting and Kummer inputs are A.1, A.3, and A.10 of the current paper. The new norm identities, parameter conditions, local fibre checks, Cech Hasse computation, Cartier calculations, and dihedral arguments are proved in the extension itself. No inherited AI return is cited as a proof.

Yang, *Abelian Coverings of Curves over Fbar_p which are not New Ordinary*, RIMS-1844 (February 2016), was opened at <https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1844.pdf>. Definition 1.1 and the following Artin–Schreier identification give the Frobenius description of p-rank. Section 2 gives the locally exact differential sequence. Proposition 1.3 was inspected as a generic new-ordinariness lead; the explicit obstruction ultimately proved does not depend on invoking it without a specialization argument. Proposition 2.3 was used in the separate cross-ratio review, not as an automatic characteristic-two uniformization theorem.

Zapponi, *A singular property of the supersingular elliptic curve in characteristic 2*, arXiv:1004.3695v3, was opened at <https://arxiv.org/pdf/1004.3695>, especially the introduction and Proposition 2.1. Its Lamé-cover theorem was investigated as a possible alternate route. It was not used to claim a prime-to-two étale correspondence for an arbitrary ordinary elliptic curve or arbitrary hyperelliptic curve.

## Failed extensions retained explicitly

1. **Direct tame branch cancellation through the hyperelliptic quotient fails in characteristic two.** A local tame inertia group of odd order m remains nontrivial after a base change of ramification index one or two, since gcd(m,2)=1. A nontrivial cover of P1 with odd Galois closure therefore cannot become étale merely by pullback along the wild quadratic hyperelliptic map. The successful cubic and quintic functions above depend on Y, not only on the quotient coordinate x.

2. **Even valuations do not cancel Artin–Schreier ramification.** In K=k((t))⊂L=k((u)) with t=u²/(1+u), the extension has ramification index two. The pullback of z²+z=t⁻³ reduces modulo h²+h, h=u⁻³+u⁻²+u⁻¹, to u⁻⁵+u⁻¹. It still has an odd leading pole and remains ramified. Matching Kummer multiplicities is not a substitute for matching the wild local extension.

3. **Prime-to-two torsion density does not prescribe the order.** The single Frobenius-cycle argument for thirteen uses that 2 generates (Z/13)×. General prime-to-two torsion density on a theta translate does not guarantee a torsion point of prime order with this property. No such extrapolation is used to settle every characteristic-two hyperelliptic curve.

4. **A single map to a separated target is insufficient.** All positive results retain two quotient maps whose joint geometric point-injectivity is proved. No conclusion about point-section injectivity is drawn merely from the existence of a nonconstant map to a 2-rank-zero curve.

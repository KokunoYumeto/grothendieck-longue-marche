# A.C2.25 candidate: a complete primitive theta packet and all 48 ordinary F4 classes

**Status, 2026-11-14:** root and independent reviewer approved the entire proof; integrated as A.C2.25 in sections/A_F4_all_48.tex. All1296 exact relations and three independent orbit classifications pass. Reviews: audit/A_F4_all_48_root_review.md and audit/A_F4_large_theta_degeneration_review.md. Universal A1 and the final universal implication of A2 remain A.30, Unresolved.

## 1. Proposed statement and exact scope

Let alpha be a root of alpha^2+alpha+1 over F2, and let C0/F4 be the smooth proper model of

\[
 C_0:\qquad v^2+v=z+\frac{\alpha^2(z+1)}{z^2+z+\alpha}.
 \tag{1}
\]

The geometrically prime-to-two point-section map of C0 is injective over every finite extension of F4. The same holds for its coefficientwise-square conjugate, every finitely generated form of either geometric curve, and their hyperbolic open subcurves.

Together with A.C2.22 this proves A1 for **all 48 geometric ordinary genus-two moduli classes fixed by fourth-power Frobenius**. In particular it proves A1 for every ordinary genus-two curve over F4. This does not address arbitrary ordinary genus-two moduli points over Fbar2, arbitrary higher-genus curves, or universal A1.

The additional input is a connected cyclic etale cover of odd degree

\[
 M=7\cdot31\cdot2503\cdot4519=2\,454\,499\,369
 \tag{2}
\]

whose primitive conductor-M Jacobian factor has two-rank zero. Its construction is certified by a fixed torsion generator and 1296 exact theta multiples, one on every primitive multiplication-by-two orbit. No assertion that a single small conductor works universally is involved.

## 2. Curve, theta origin, and the two omitted moduli classes

Put

\[
 h(z)=z^2+z+\alpha,\qquad
 G(z)=z^3+z^2+z+\alpha^2,\qquad Y=h(z)v.
\]

Then (1) becomes

\[
                 Y^2+h(z)Y=f(z),\qquad f=hG.                 \tag{3}
\]

The polynomial f is monic of degree five. At a zero of h, G=alpha^2(z+1) is nonzero, so the affine model is smooth there; elsewhere its derivative with respect to Y is nonzero. There is one smooth point at infinity on the smooth proper model. Equivalently the Artin--Schreier equation (1) has three distinct simple poles: the two roots of h and infinity. Thus C0 has genus two and is ordinary.

Denote the points above the two finite poles by W1,W2 and the point above infinity by W_infinity. Their individual fields of definition are not being assumed to lie in the certificate field; their sum is rational. The different of the degree-two z-map is

\[
                    2W_1+2W_2+2W_\infty.
\]

Consequently

\[
 \operatorname{div}(dz)=2(W_1+W_2-W_\infty),\qquad
 B_\Theta=\mathcal O(W_1+W_2-W_\infty).                     \tag{4}
\]

The locally exact differential dz identifies this line bundle with the Raynaud bundle B used in A.C2.5. In particular

\[
 \Theta=\{L\in J_{C_0}:H^0(C_0,B_\Theta\otimes L)\ne0\}
       =\{[R-B_\Theta]:R\in C_0\}.                         \tag{5}
\]

The reduced Mumford class T=(h,0) represents W1+W2-2W_infinity and has order two: the divisor of h is twice that divisor. Hence for every affine point R

\[
 [R-W_\infty]+T=[R-B_\Theta].                              \tag{6}
\]

This checks the theta origin, including its sign; merely testing [R-W_infinity] would be incorrect.

For identification with the omitted class, take r with r^2+r=alpha and put x=z+r. Removing the resulting constant after a finite extension transforms (1) into C(a,b,c) of A.C2.22 with

\[
       (a,b,c)=(1,\alpha^2(r+1),\alpha^2r).
\]

Their elementary symmetric functions are alpha,0,alpha^2. Thus the unordered coefficient polynomial is Z^3+alpha Z^2+alpha^2, key203. Applying the F2-automorphism alpha -> alpha^2 gives Z^3+alpha^2 Z^2+alpha, key302. This automorphism transports every algebraic identity, theta class, and connected cyclic cover below. The prime-to-two section conclusion is also invariant under this base-field isomorphism. It therefore suffices to certify (1).

## 3. Immutable finite certificate and field encoding

The principal data file is

`code/A_F4_large_theta_witness.json`.

Its SHA256 is

`edcf6ed3d425eb72837ae72f521f7221ee91c8a53c1b005885a4c1280d530ae6`.

It contains all 1296 records (x,y,i), not a sample or a hash in place of the data. It is checked without regenerating the search.

The field is

\[
 F=\mathbf F_2[w]/(w^{18}+w^7+1)=\mathbf F_{4^9}.
 \tag{7}
\]

An integer a between 0 and 2^18-1 denotes the polynomial in w whose coefficients are the binary digits of a, in ascending powers. Addition is XOR; multiplication is polynomial multiplication modulo the binary modulus262273. The element encoded by2 is primitive, and alpha is encoded by114587. The independent checker verifies alpha^2+alpha=1 and a complete cycle of length262143 through all nonzero field elements. The parent's third verifier separately uses the polynomial irreducibility criterion: w^(2^18)=w modulo the modulus, and the gcds with w^(2^9)-w and w^(2^6)-w are1.

The exact theta generator is

\[
        R=(49,185454),\qquad \eta=[R-B_\Theta],
\]

in the original z,v coordinates. Its reduced Mumford pair in (3) is

\[
 U=z^2+124780z+171897,\qquad V=26069z+117672.                \tag{8}
\]

Each coefficient in this display uses (7), not integer arithmetic modulo2^18. The certificate verifies

\[
 [M]\eta=0,\qquad [M/p]\eta\ne0
           \quad(p=7,31,2503,4519).                        \tag{9}
\]

Trial division up to the square root verifies that all four factors are prime. Since M is squarefree, (9) proves exact order M.

The independent seven-primary witness is retained as requested. Let

\[
 R_H=(1,114586),\quad
 H=[4M/7]\,[R_H-B_\Theta].
\]

Its Mumford pair is

\[
                 U_H=z^2+z+1,\qquad V_H=114586z.            \tag{10}
\]

The verifier checks [7]H=0 and H is different from [jM/7]eta for every j=0,...,6. Thus H and A=[M/7]eta generate a subgroup C7^2, by seven exact non-equality checks, not by guessing the module from a point count.

The actual F4 Frobenius polynomial, established in A.C2.24, is

\[
                   P_4(X)=X^4+2X^3+X^2+8X+16.
\]

It gives

\[
 \#J(F)=68\,725\,982\,332
       =4\cdot7^2\cdot31\cdot2503\cdot4519=4\cdot7M,
 \qquad \#C_0(F)=262171.                                  \tag{11}
\]

The canonical verifier computes the first number as det(pi^9-I) on the integral companion matrix of P4. The parent's independent verifier recomputes both numbers by integer Newton recurrences. Their interpretation is the curve/Jacobian Frobenius formula (Milne, 2008, III, Theorem11.1 and Corollary11.4; II, Theorem1.1), already opened and cited for A.C2.24.

Combining (10)--(11), the entire odd subgroup is

\[
 J(F)_{\mathrm{odd}}\cong
 C_7^2\oplus C_{31}\oplus C_{2503}\oplus C_{4519},
 \tag{12}
\]

and its exponent is exactly M. The theorem only needs (9) and the 1296 identities below; (10)--(12) additionally certify the component structure used to discover the witnesses.

## 4. Why each polynomial check is an actual divisor identity

Here are the exact arithmetic rules, so the proof does not rely on an unnamed library or approximate numerical group calculation. On (3), a reduced pair (U,V) means U monic, degV<degU<=2, and

\[
                         U\mid V^2+hV+f.
\]

It represents D(U,V)-deg(U)W_infinity, where the finite divisor D is the ideal (U,Y-V) on the smooth affine curve. Reduced representation is unique; zero is (1,0). This is the Mumford representation in Lange (2005, Theorem2.2, author p.5).

For pairs (U1,V1),(U2,V2), compute the two monic extended gcds

\[
 d_1=a_0U_1+b_0U_2,\qquad
 d=e d_1+c(V_1+V_2+h),\qquad
 d_1=\gcd(U_1,U_2),\quad d=\gcd(d_1,V_1+V_2+h).
\]

Put a=e a0,b=e b0. Composition is

\[
 U=\frac{U_1U_2}{d^2},\qquad
 V=\frac{aU_1V_2+bU_2V_1+c(V_1V_2+f)}{d}\pmod U.          \tag{13}
\]

Make U monic. While degU>2 replace the pair by

\[
 U'=\frac{V^2+hV+f}{U},\qquad
 V'=V+h\pmod {U'},                                        \tag{14}
\]

again making U' monic. These are precisely Lange's Algorithms3.1--3.2, author pp.5--6, in characteristic two. That primary source explicitly allows even characteristic; the original odd-characteristic-only form of Cantor's algorithm is not being substituted.

For completeness the divisor meaning of the rules is as follows. Multiplication of the two ideals has generators

\[
 U_1U_2,\quad U_1(Y+V_2),\quad U_2(Y+V_1),
 \quad (V_1+V_2+h)Y+(V_1V_2+f).
\]

The displayed Bezout relation makes the corresponding linear combination d(Y+V). Locally at each finite fibre, d removes precisely the pairs of opposite points common to the two divisors; at a ramified point the repeated point is removed using div(z-z0)=2W-2W_infinity. This gives the ideal identity I1 I2=(d)I(U,V). It proves that (13) represents the sum of the divisor classes, including coincident points and ramification fibres.

For (14), the norm of Y+V is V^2+hV+f=UU'. Its zero divisor is D(U,V) plus D(U',V), counted with multiplicity, and its only pole is at infinity. Hence the class of D(U,V)-degU W_infinity is the negative of D(U',V)-degU' W_infinity. The latter negative is the hyperelliptic conjugate divisor, with Y-coordinate V+h. This is (14). Monic normalization multiplies a function by a nonzero constant and does not change its divisor. Iteration yields the unique reduced pair. Binary repeated addition using (13)--(14) therefore proves exact scalar relations in Pic^0.

The verifier checks every division in (13)--(14) has zero remainder, checks the congruence U | V^2+hV+f after every operation, and compares the final reduced pairs. It uses the general gcd algorithm, so no generic-position hypothesis or unhandled denominator exception enters the 60773 divisor operations.

For a certificate point (x,y), it first forms ([x,1],[h(x)y]), the class [R-W_infinity], and adds T=(h,0). Equation(6) then identifies this class with [R-B_theta]. Consequently every verified record gives the actual identity

\[
                      [i]\eta=[R_i-B_\Theta]\in\Theta.
 \tag{15}
\]

## 5. All 1296 primitive doubling orbits are represented

The fixed file contains 1296 records satisfying (15) with gcd(i,M)=1. The independent canonical verifier proves every one of these identities, and checks every curve point and every unit condition.

The local orders of2 at the four prime factors in their displayed order are

\[
                  3,\quad5,\quad1251,\quad753.
\]

Thus

\[
 \operatorname{ord}_M(2)=1\,570\,005,\qquad
 \varphi(M)=2\,034\,726\,480,\qquad
 \#((\mathbf Z/M)^\times/\langle2\rangle)=1296.             \tag{16}
\]

Every multiplication-by-two orbit on the units has that same length. Distinctness of the 1296 recorded orbits therefore proves exhaustion. Two independent finite recipes establish distinctness.

### 5.1 Integer lattice recipe in the canonical checker

The integer3 is verified to be a primitive root at each of the four primes. Discrete logarithms identify the unit group with

\[
             \mathbf Z/6\oplus\mathbf Z/30
                    \oplus\mathbf Z/2502\oplus\mathbf Z/4518.
\]

Let v be the four discrete logarithms of2, and let L be the integer lattice generated by the four diagonal period vectors and v. A general Hermite-normal-form computation gives the following basis, written in columns:

\[
 H=\begin{pmatrix}
 6&0&0&2\\0&6&0&0\\0&0&6&4\\0&0&0&6
 \end{pmatrix},\qquad \det H=1296.                          \tag{17}
\]

Reduce each integer log vector by these columns from right to left, reducing its diagonal coordinate to the range0,...,5. The 1296 witness vectors have distinct residues; v itself has residue zero. These are therefore all quotient classes.

### 5.2 Elementary generalized-CRT recipe in the third checker

For each prime p, enumerate the local doubling cycles directly in (Z/p)^*. Label an element by its smallest cycle representative and its time coordinate t_p in that cycle. No multiplicative discrete-log generator or HNF is needed. Two unit indices i,j belong to one global doubling orbit exactly when their local cycle representatives agree and the congruences

\[
                 k\equiv t_p(i)-t_p(j)\pmod {d_p}
\]

have a simultaneous solution. The elementary generalized Chinese remainder theorem says this happens exactly when every pair agrees modulo gcd(d_p,d_q). Thus a complete orbit signature is the four local representatives together with all pairwise differences t_p-t_q modulo gcd(d_p,d_q). All1296 signatures are different.

The parent's checker also independently verifies the original Artin--Schreier point equations by binary polynomial arithmetic. It reads the retained full search output and verifies that its original component indices were converted to the indices relative to the actual theta generator. The fixed witness file records precisely those converted indices; the canonical checker uses that file directly. The exact hashes of both files are recorded in the respective outputs.

## 6. From the finite certificate to the cyclic cover and A1

Over an algebraic closure let L represent eta and choose a trivialization L^M=O. The algebra direct sum of L^(-j), j=0,...,M-1, with multiplication from that trivialization, defines a finite etale mu_M-torsor D->C0, because M is odd. Its geometric connectedness follows from the exact order M of L: a proper cyclic quotient trivial on the torsor would give a smaller power of L trivial. After a finite constant extension it has the cyclic deck group CM. Its genus is M+1.

For each nonzero character i, the space H^1(C0,L^i) has dimension one. The characteristic-two exact sequence

\[
        0\longrightarrow L^i\longrightarrow F_*L^{2i}
          \longrightarrow B_\Theta\otimes L^i
          \longrightarrow0
\]

shows that the corresponding Frobenius arrow is zero precisely when L^i lies on theta. This is the exact argument of A.C2.5. By (15)--(17), every primitive character cycle contains such a zero arrow. Frobenius is consequently nilpotent on the entire primitive conductor-M part of H^1(D,O_D). The primitive Jacobian factor has two-rank zero, by the Cartier/Frobenius and Artin--Schreier identification used in A.C2.5. Characters of smaller conductor need not vanish and are not being claimed to vanish.

A.C2.19 now applies, without any restriction on the number of distinct prime divisors of M. Equivalently one can apply the all-genus primitive-zero criterion A.C2.20. In this instance omega(M)=4, and its primitive operator is the product of four factors (1-sigma^(M/p)); its support bound is16, while M>225. The existing proof of that criterion gives the section conclusion; this computation does not replace its geometric divisor argument.

The property is geometric and survives arbitrary extension of algebraically closed constants. For a form over any finitely generated field of characteristic two, the finite collection consisting of the isomorphism to C0, the torsion class, its trivialization, and the deck maps is defined after a finite extension of the entire base field. A.C2.19 already includes this formulation; A.3 and the descent/spreading argument of A.8 transfer the conclusion back to the stated curve. A collision of original rational points remains a collision after finite extension and would contradict the constructed criterion. Functoriality to the proper compactification gives the assertion for hyperbolic open subcurves. Coefficient conjugation, as checked in Section2, supplies key302 from key203. A.C2.22 then supplies the other46 geometric classes.

## 7. Reproduction, independence, and scope of the evidence

Run from the bundle's code directory:

```text
python A_F4_large_theta_canonical.py
python A_F4_large_theta_root_orbits.py
```

The first imports the earlier coefficient-list finite-polynomial and general Cantor routines. It imports no C source, accelerated polynomial engine, search driver, or tailored component/coset normalization. It rebuilds the binary field independently and verifies all1296 fixed relations, exact order, the independent seven-class, the group order, and all1296 HNF residues. Its output is `code/A_F4_large_theta_canonical.json`, PASS, 60773 divisor operations.

The second imports no search code, C arithmetic, Jacobian code, discrete-log normalization, or HNF. Its input is the retained full discovery data `code/A_F4_large_theta_search.json`, SHA256

`5158fb82718066afba081edc7a844e9120be81535f0960c346cf1af07b7c8eb9`.

It independently verifies irreducibility of the field modulus, all1296 original point equations, the integer Newton recurrence, and all1296 generalized-CRT signatures. Its output is `code/A_F4_large_theta_root_orbits.json`, PASS. The parent also independently reran the complete canonical checker.

Discovery files are `code/A_F4_large_theta.c`, `.py`, `.json`, and `code/A_F4_large_theta_search.py/.json`. The C source was checked against canonical arithmetic in1371 exact comparisons before the search. Its positive output stops when a complete packet is found and does not claim exhaustive enumeration of allF-points. The final theorem does not depend on a correct negative search, a heuristic on random torsion points, or treating all arithmetic modules of the same order as isomorphic.

All preceding negative results remain valid in their exact scope. A.C2.24 rules out the specified small primary/mixed packets and the entire73-power primitive-zero route; it never ruled out the mixed conductor(2). A.C2.14 says no fixed finite prime set works for every ordinary genus-two curve; it does not rule out this one explicit four-prime choice for C0. A.C2.23 restricts intermediate stages with abelian total normal closure and is not contradicted by the direct cyclic cover here. Universal A1 remains unresolved.

## 8. Opened primary reference for the arithmetic rules

Lange, T. (2005). Formulae for arithmetic on genus2 hyperelliptic curves. *Applicable Algebra in Engineering, Communication and Computing, 15*(5),295--328. https://doi.org/10.1007/s00200-004-0154-8

Author PDF: https://www.hyperelliptic.org/tanja/preprints/expl.pdf

Opened2026-11-14, web source `turn813view0`. Exact loci: Definition2.1, author p.4; Theorem2.2, author p.5; Algorithms3.1--3.2, author pp.5--6. These include the general h-polynomial and even-characteristic formulas actually used. No external-source quotation is reproduced. This reference should enter the owned bibliography/source ledger only after the integration freeze is released.

The primary Milne loci and all theta/primitive-cover sources are already opened and recorded under A.C2.5,A.C2.19--20,A.C2.24. This finite certificate is new work in the present bundle and is not attributed to the historical manuscript.


### Additional independent review and source access

The degeneration reviewer independently reran every canonical divisor relation and checked the theta origin, exact exponent, eight seven-primary directions, and the A.C2.20 implication. Its separate code/A_F4_large_theta_degeneration.py/.json uses different primitive roots, local log residues modulo(2,6,2,6), and two relative times modulo3, giving all1296 signatures without HNF or the search normalization. The full review is audit/A_F4_large_theta_degeneration_review.md. Root read every section and independently opened the Lange primary PDF as turn814view0, Theorem2.2 and Algorithms3.1–3.2, author pp5–6; the official TU/e publication metadata was opened as turn815search0/1. Root review: audit/A_F4_all_48_root_review.md.

# Arithmetic certificates for the D1 density step

These constructions verify the exact scope of the density problem using actual elliptic curves and genus-two Jacobians. They do not assert a counterexample to the finiteness of the Selmer section set of a proper hyperbolic curve. No local section theorem is used.

## 1. Distinct potential toric ranks and equal traces on a positive-density set

For a rational number a other than 3 and -1, put

\[
 E_a: v^2=u^3+a u^2+a u+1,\qquad
 C_a: y^2=x^6+2a x^4+4a x^2+8.
\]

Let E_a^(2) denote the quadratic twist in the model

\[
 2v^2=u^3+a u^2+a u+1.
\]

The sextic is squarefree: its discriminant is

\[
 -2^{21}(a-3)^6(a+1)^2,
\]

so the smooth proper completion of C_a has genus two. The two maps

\[
 \pi_1:C_a\longrightarrow E_a^{(2)},\quad
 (x,y)\longmapsto (x^2/2,y/4),
\]
\[
 \pi_2:C_a\longrightarrow E_a,\quad
 (x,y)\longmapsto (2/x^2,y/x^3)
\]

satisfy the target equations by direct substitution. Each is generically of degree two, and extends over the smooth proper completions by the valuative criterion for properness (the source is a nonsingular curve). Their invariant differential pullbacks are

\[
 \pi_1^*(du/v)=4x\,dx/y,
 \qquad \pi_2^*(du/v)=-4\,dx/y.
\]

These form a basis of the holomorphic differentials of C_a. Therefore the homomorphism

\[
 \Psi_a=(\pi_{1*},\pi_{2*}):J(C_a)\longrightarrow E_a^{(2)}\times E_a
\]

has an invertible differential. Its image is a closed connected subgroup of the same dimension as the target and its kernel is zero-dimensional; hence it is a Q-isogeny. This explicitly supplies the comparison between the Jacobian and the product. In particular, after tensoring with Q_l, the Tate-module map induced by Psi_a is an isomorphism of G_Q-representations: an isogeny admits a quasi-inverse whose composites are multiplication by an integer, which becomes invertible over Q_l.

For every good odd prime p, write a_p(E_a) for the elliptic Frobenius trace. The twist isomorphism over Q(sqrt(2)), with its nontrivial Galois action equal to [-1] on the elliptic curve, gives

\[
 V_l(E_a^{(2)})\simeq V_l(E_a)\otimes\chi_2,
 \quad
 a_p(J(C_a))=(1+\chi_2(p))a_p(E_a).
\]

The induced isomorphism is the exact arithmetic map used here. Consequently, at every good prime p with Legendre symbol (2/p)=-1, the genus-two Frobenius trace is zero, independently of a. These primes have Dirichlet density one half, by the quadratic case of Chebotarev for Q(sqrt(2))/Q (equivalently Dirichlet's theorem for p congruent to 3 or 5 modulo 8).

Now choose a=4 and a=0:

\[
 C_4:y^2=x^6+8x^4+16x^2+8,
 \qquad C_0:y^2=x^6+8.
\]

The Weierstrass invariants of E_a are

\[
 c_4(E_a)=16a(a-3),\qquad
 \Delta(E_a)=16(a-3)^3(a+1).
\]

At 5 the curve E_4 has c_4=64 and Delta=80, so it has multiplicative reduction and potential toric rank one. This equation is minimal at 5 because c_4 is a unit. The curve E_0 has Delta=-432, a 5-adic unit, so it has good reduction and potential toric rank zero. The same potential ranks hold for their quadratic twists, since each twist becomes isomorphic to the original curve after the explicitly given quadratic extension. The isogenies Psi_a identify the rational Tate modules; on a finite extension with semistable reduction, the toric rank equals the rank of the unipotent monodromy operator on V_l. Thus

\[
 t_5(J(C_4))=2,\qquad t_5(J(C_0))=0.
\]

The two Jacobians cannot become isogenous over any finite extension, because an isogeny would identify their rational Tate modules and hence these ranks. Nevertheless their Frobenius traces agree on the density-one-half set just exhibited. This refutes the proposed general implication from positive-density equality of traces to potential equivalence, even for actual weight-one Jacobian representations separated by potential toric rank.

The precise limitation is visible in the full polynomial. At an inert good prime, if b=a_p(E_a), then

\[
 P_{J(C_a),p}(T)
   =(T^2-bT+p)(T^2+bT+p)
   =T^4+(2p-b^2)T^2+p^2.
\]

The T^2 coefficients can distinguish the examples. At p=19, E_4 has trace -4 and E_0 has trace 8, so the two polynomials are T^4+22T^2+361 and T^4-26T^2+361. The assertion proved is equality of traces, which is exactly the invariant used in the connected-monodromy trace-separation argument. Equality of all characteristic polynomials has not been asserted for these two genus-two curves.

The set of primes with unequal traces is contained in the split primes of Q(sqrt(2)). It cannot have ordinary density one. After a finite extension containing Q(sqrt(2)) over which the joint algebraic monodromy group is connected, the trace-separation argument gives the required potential-density-one separation: the two semisimple representations remain nonisomorphic by their different potential toric ranks. Hence the two densities differ for these arithmetic objects, with the displayed restriction maps and isogenies, not only for an abstract pair of prime sets.

## 2. Full characteristic-polynomial equality for two non-potentially-isogenous elliptic curves

For a complementary certificate use

\[
 E_i:y^2=x^3-x,\qquad E_3:y^2=x^3+1.
\]

At every prime p congruent to 11 modulo 12 both traces are zero. For E_i, pair the terms x and -x in the quadratic-character sum: x^3-x changes sign, and -1 is a nonsquare for p congruent to 3 modulo 4. For E_3, cubing permutes F_p when p congruent to 2 modulo 3, so the character sum equals the zero sum of the quadratic character over F_p. Thus both full Frobenius characteristic polynomials are T^2+p at all these primes, a set of Dirichlet density one quarter.

They do not become isogenous over any finite extension. At 5, direct point counting gives traces -2 and 0, hence Frobenius eigenvalues

\[
 -1+2i,\ -1-2i \quad\hbox{and}\quad i\sqrt 5,\ -i\sqrt 5.
\]

The ratio of the first pair is (-3-4i)/5, which is not a root of unity: it lies in Q(i) and is not one of its four roots of unity. The ratio of the second pair is -1. At a place above 5 in a finite extension of residue degree f, the good-reduction Frobenius eigenvalues are the f-th powers of these pairs. Equality of their unordered multisets would force the f-th power of the first ratio to be (-1)^f or its reciprocal, hence a root of unity, which is impossible. Any isogeny over that finite extension would induce exactly this forbidden isomorphism on V_l, for l not equal to 5. Finally an isogeny over Qbar is defined over a finite extension, since its defining rational functions have finitely many algebraic coefficients. This proves the asserted failure of potential isogeny without importing a CM classification.

Both elliptic curves have potential toric rank zero at every place; the certificate in this section does not prove different toric ranks. The genus-two certificate above proves that stronger rank distinction for trace equality. The two scopes are recorded separately with their exact equations and maps.

## 3. Checked primary sources and the remaining D1 implication

Milne, *Elliptic Curves*, second edition (2021), Chapter II, section 3, printed page 60, states the discriminant/c4 tests for good and multiplicative reduction and the invariance of good or nodal reduction under finite extension. Chapter V, section 8 supplies the good-reduction Frobenius/Tate-module comparison. Primary PDF: https://www.jmilne.org/math/Books/EC2.pdf .

Kulkarni--Patankar--Rajan, *Locally potentially equivalent two dimensional Galois representations and Frobenius fields of elliptic curves*, arXiv:1403.5635v3, Theorems 1.1, 1.5 and 1.6, was read. The non-CM (equivalently here GL2 monodromy) hypothesis is explicit in the elliptic potential-equivalence result. Theorem 1.6 retains a connected-monodromy hypothesis for the trace statement. Primary PDF: https://arxiv.org/pdf/1403.5635 .

Patankar--Rajan, *On the structure of locally potentially equivalent Galois representations*, arXiv:1901.03820v4, Introduction and Example 1.1, was read together with the authors' erratum to their 2012 paper. The erratum identifies the false assertion that a power map sends each connected component onto a component; the normalizer of a torus in SL2 provides its counterexample. The 2020/2021 paper gives a replacement under its stated additional hypotheses, and does not license dropping connected monodromy in the D1 trace argument. Primary PDFs: https://arxiv.org/pdf/1901.03820 ; https://vijaympatankar.weebly.com/uploads/6/7/7/1/6771298/jrms-pote-eq-gal-reprs-rajan-patankar-errata.pdf .

These calculations strengthen the audit of the positive-density promotion. They supply no counterexample curve to the statement that all Selmer section classes are finite, and supply no proof of that statement. Betts--Stix provides finite individual localization images. Porowski's full-localization injectivity identifies the global classes with their compatible tuples; an injective map into the product of finite sets does not by itself make the source finite. The explicit compact arithmetic model LM6-D.7 already records the failure of the additional potential-density partition refinements to imply finiteness. No assertion has been made that a different arithmetic argument cannot establish a uniform bound.

Exact symbolic and finite-field verification is in `work/code/density_jacobian_check.py` and `work/code/density_jacobian_check_output.txt`. The finite tests verify the displayed algebra and illustrative counts. The all-prime trace identities and density assertions follow from the proofs above.

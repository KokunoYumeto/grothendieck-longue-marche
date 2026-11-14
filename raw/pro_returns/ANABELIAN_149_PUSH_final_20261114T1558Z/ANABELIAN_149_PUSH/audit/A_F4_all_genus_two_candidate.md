# A.C2.26 candidate: every genus-two curve over F4

**Status, 2026-11-14:** root and independent review PASS; integrated as A.C2.26 in sections/A_F4_all_genus_two.tex after checkpoint10 release. Both direct polynomial verifiers pass all seven fixed identities and twelve-class coverage. Reviews: audit/A_F4_all_genus_two_root_review.md and audit/A_F4_rank_one_degeneration_review.md. Universal A1 remains unresolved.

## 1. Proposed theorem

Every smooth proper geometrically connected genus-two curve over F4 satisfies A1, as does its base change to every finite extension. The conclusion also holds for every finitely generated form of one of these geometric curves and every hyperbolic open subcurve.

More explicitly, the twelve geometric p-rank-one genus-two moduli classes fixed by fourth-power Frobenius are

\[
 C(A,B):\quad y^2+y=A x^3+B x+\frac1x,
 \qquad A\in\mathbf F_4^*,\quad B\in\mathbf F_4.
 \tag{1}
\]

They all satisfy A1. A.C2.25 handles every ordinary genus-two class fixed by the same Frobenius. The p-rank-zero case follows directly from A.1 and the injectivity of the Abel map, without a finite-classification assumption.

This is a bounded finite-field theorem. It does not identify every genus-two moduli point over Fbar2 with one defined over F4 and does not resolve genus-two A1 over arbitrary finite fields.

## 2. Exact classification of the p-rank-one geometric classes

Over an algebraically closed field of characteristic two, the genus-two hyperelliptic quotient is separable and has an Artin--Schreier presentation y^2+y=phi(x). Reduce every pole order of phi to an odd integer by Artin--Schreier changes of the generator. The p-rank formula is the number of poles minus one; the genus formula is

\[
           2g-2=-4+\sum_j(m_j+1).
\]

For g=2 and p-rank one there are two poles, and their odd orders sum to four. They are therefore3 and1. Send the order-three pole to infinity and the order-one pole to zero. Removing even polynomial terms and an additive constant gives

\[
              y^2+y=a x^3+b x+c/x,
              \qquad ac\ne0.
\]

Rescaling x uniquely makes the coefficient of1/x equal to1, yielding (1) over the algebraic closure. This uses the same standard Artin--Schreier genus and p-rank calculation already proved/cited for the normal forms in A.C2.1--A.C2.5 and A.C2.22.

The pair(A,B) is a complete geometric invariant in this normalization. Indeed every isomorphism preserves the unique genus-two hyperelliptic pencil. The two branch points have different different exponents,2 and4, so it must fix them individually; its induced base map has the form x -> u x. Any change of Artin--Schreier generator has the form y -> y+v(x): the coefficient of y forces its nonzero multiplicative coefficient to be1. A nonconstant v has a pole, and the leading pole order of v^2+v is even. It cannot equal a difference of reduced functions having only the displayed odd pole orders. Thus v is constant. Comparison of the simple-pole coefficient now forces u=1, and the remaining coefficients force equality of A and B.

It follows that fourth-power Frobenius fixes the geometric class exactly when A^4=A and B^4=B. There are3*4=12 possibilities. Conversely each displayed equation defines an actual curve over F4. Thus no field-of-moduli descent inference is needed.

Under coefficientwise squaring, alpha -> alpha^2 for alpha^2+alpha+1=0. There are exactly seven representatives:

\[
 (1,0),(1,1),(1,\alpha),
 (\alpha,0),(\alpha,1),(\alpha,\alpha),(\alpha,\alpha^2).
 \tag{2}
\]

The first two are fixed by squaring and each other representative has a distinct conjugate. These account for all twelve classes.

## 3. Raynaud theta and an exact norm certificate

Let W0,W_infinity be the points above the two branch values. On C(A,B),

\[
 \begin{array}{c|cc}
       &x&y\\\hline
 W_0&2&-1\\
 W_\infty&-2&-3
 \end{array}
\]

The different is2W0+4W_infinity, whereas the pullback of the base divisor of dx is-4W_infinity. Hence

\[
              \operatorname{div}(dx)=2W_0,
              \qquad B_\Theta\simeq\mathcal O(W_0).
 \tag{3}
\]

This is the line bundle of locally exact differentials, with its Frobenius module structure. The theta divisor is therefore

\[
                       \Theta=\{[R-W_0]:R\in C\}.
\]

In particular0 belongs to theta in this stratum. It must not be counted as a nontrivial torsion witness.

Put Y=xy. Then

\[
              Y^2+xY=A x^5+B x^3+x.
\]

The Mumford pair(x,0) is[W0-W_infinity], of order two because div(x)=2W0-2W_infinity. Thus the exploratory search's addition of(x,0) to[R-W_infinity] gives[R-W0], as required. The final proof below does not depend on that Jacobian search.

Let n>1 be odd, d=(n-1)/2, and suppose a finite extension contains t!=0,y0 and polynomials a(x),b(x), together with c!=0, satisfying

\[
 \begin{split}
 &\deg a\le d,\qquad\deg b\le d-2,\\
 &x(a^2+ab)+b^2(Ax^4+Bx^2+1)=c(x+t)^n,                    \tag{4}\\
 &a(t)+b(t)y_0=0,\qquad b(0)b(t)\ne0,\\
 &y_0^2+y_0=A t^3+B t+1/t.
 \end{split}
\]

Write R=(t,y0). The function

\[
                       q=\frac{a(x)+b(x)y}{x^d}
\]

has its only pole at W0, of exact order2d+1=n: at that point b(0)y has valuation-1, strictly smaller than the polynomial a, and the denominator has valuation2d. It is regular at infinity since a/x^d has nonnegative valuation, while by/x^d has valuation at least1. It is regular at every other finite point.

The hyperelliptic conjugation sends y to y+1. Equation(4) is exactly

\[
             q\,\iota(q)=c\frac{(x+t)^n}{x^n}.
\]

Thus all zeros lie above x=t. At R the numerator vanishes; at its distinct conjugate it equals b(t), which is nonzero. The double cover is unramified at this nonbranch coordinate, so the norm identity assigns all n zeros to R. We obtain the full divisor identity

\[
                     \operatorname{div}(q)=n(R-W_0).       \tag{5}
\]

The class eta=[R-W0] is nonzero: a principal divisor R-W0 would define a degree-one map to the projective line, contrary to genus two. It is an odd-order theta class whose exact order e>1 divides n. Exact order n is not needed for the theorem.

## 4. The seven fixed positive records

The complete coefficients a(x),b(x),c of every identity(4), not merely point counts or rank outputs, are in

`code/A_F4_rank_one_witnesses.json`.

Its fixed SHA256 is

`82dd18cfcfac963e1a4217e03a55b39a47766ee521c6601f3704e9828b417ec3`.

Here is the exact table. Integer entries encode binary polynomials in the field generator w, with ascending powers. The columns alpha,t,y0 use that encoding.

| (A,B) overF4 | Field size | Binary modulus | Primitive generator | alpha | (t,y0) | n |
|---|---:|---:|---:|---:|---|---:|
| (1,0) |16|19|2|6|(6,2)|13|
| (1,1) |4|7|2|2|(1,2)|5|
| (1,alpha) |16|19|2|6|(7,2)|11|
| (alpha,0) |256|283|3|189|(80,242)|39|
| (alpha,1) |16|19|2|6|(6,4)|19|
| (alpha,alpha) |4|7|2|2|(1,2)|7|
| (alpha,alpha^2) |16|19|2|6|(7,2)|5|

The respective field moduli are w^2+w+1, w^4+w+1, and w^8+w^4+w^3+w+1. The recorded generators have complete cycles through all nonzero elements, certifying the field constructions. The alpha values satisfy alpha^2+alpha=1.

For example, the seventh-torsion row uses F4, A=B=alpha, t=1,y0=alpha, and

\[
 a(x)=\alpha^2+x+\alpha x^2+x^3,
 \qquad b(x)=1+\alpha x,
 \qquad c=1.
\]

The largest row has degree39 and uses only F256. Its coefficient vectors are retained explicitly here as well:

\[
\begin{split}
 a={}&[67,139,142,6,17,104,78,101,235,178,77,174,77,253,\
     &\hspace{28mm}38,164,165,192,1,12],\\
 b={}&[1,80,176,188,93,12,1,12,188,92,93,1,93,93,13,189,189,177].
\end{split}
\]

These are coefficients in ascending powers of x, interpreted in the binary field of modulus283. All coefficient vectors for all seven rows are in the fixed file, including the norm scalars.

The standalone verifier `code/A_F4_rank_one_norm_checks.py` imports no C arithmetic, search driver, jet solver, or Jacobian code. It builds the binary fields with shift/XOR multiplication, checks complete generator cycles and coefficient labels, directly multiplies both sides of(4), and checks every point and local nonvanishing condition. It also checks the complete unit groups below and verifies that the seven conjugacy representatives cover all twelve pairs. Its output `code/A_F4_rank_one_norm_checks.json` is PASS.

The discovery files `code/A_rank_one_theta.c`, `code/A_rank_one_arithmetic.py`, and `code/A_F4_rank_one_search.py/.json` were tested by canonical divisor comparisons before the search. `code/A_F4_rank_one_make_witnesses.py` uses exact formal jets and finite-field linear algebra to find the fixed polynomial coefficients. Neither the search's completeness nor the correctness of its reported exact orders is needed after the seven norm identities have been verified.

## 5. Primitive orbit saturation and the section conclusion

For each annihilator in the table,

\[
                      \langle2,-1\rangle=(\mathbf Z/n)^*.
 \tag{6}
\]

This is checked by direct multiplication for n=5,7,11,13,19,39. In particular at39 the doubling order is12 and negation supplies the second coset, yielding all24 units.

Let e be the actual nonzero odd order of eta from(5). Reduction(Z/n)^* -> (Z/e)^* is surjective, so(6) holds at e as well. Theta is symmetric: R+iota(R) is linearly equivalent to2W0, so -eta=[iota(R)-W0] also lies on theta. Every primitive doubling orbit at e therefore contains either eta or-eta. The associated connected cyclic etale cover of actual degree e has primitive Jacobian factor of two-rank zero by A.C2.5. The conditional theorem A.C2.19, or its all-genus extension A.C2.20, proves A1 for each row.

This argument deliberately uses an annihilator. No extraction of a primary component is made; such an extraction need not preserve theta. No claim that the composite39 cover has vanishing lower-conductor factors is needed.

Coefficientwise squaring transports every identity and cover to its conjugate pair, so all twelve rank-one geometric classes are covered. For a form over a finitely generated field, the finite isomorphism and cover data descend after a finite extension of the whole base field. Restriction of section equality and A.3/A.8 give the conclusion over the original field. Functoriality to the proper compactification handles open subcurves, as in A.C2.19--A.C2.25.

Finally let C/F4 be any genus-two curve. Its two-rank is0,1,or2. Rank1 is settled above. Rank2 is A.C2.25. At rank0 its Jacobian has no nonzero geometric two-primary torsion: J[2](Fbar2)=0, and repeated doubling excludes higher two-powers. A.1 says a section collision gives a two-primary point difference, which is therefore zero; the Abel map is injective. Thus rank0 is settled over every finitely generated field as well. This proves the proposed all-genus-two F4 assertion.

## 6. Review boundaries and provenance

The geometric classification, two different branch exponents, unique normalization and theta origin have been independently checked by degeneration. An intermediate proposed theta-five calculation from that reviewer was immediately corrected before use: for g=u x^2+v x+w,

\[
 x\operatorname{Norm}(y+g)=
 u^2x^5+Ax^4+(v^2+u)x^3+(B+v)x^2+(w^2+w)x+1.
\]

It yields the accepted A.C2.3 relation A^5=B^16, not B=0. No assertion based on the incorrect coefficient collection enters the table or proof.

The final direct norm certificates are independent of that derivation. The older A.C2.3/A.C2.4 positive results remain valid and have new direct witnesses in the table. The ordinary proof A.C2.25 and all its earlier method obstructions are unchanged. No universal A1 theorem or priority claim is inferred.


### Opened classification and scope sources

The exact normal form is independently supported by Cardona–Nart–Pujolàs2005 Proposition14, authorp14; Theorem20 and Theorem22/Corollary23, authorpp19,21–22, identify64 geometricF4 classes partitioned48+12+4. These primary passages and the publisher metadata were opened; full details and the narrow A1 literature search are in audit/A_F4_all_genus_two_literature.md. Elkin–Pries Notation1.1 was independently reopened by root and both reviewing agents. No prime-to-two section conclusion is attributed to those classification sources.

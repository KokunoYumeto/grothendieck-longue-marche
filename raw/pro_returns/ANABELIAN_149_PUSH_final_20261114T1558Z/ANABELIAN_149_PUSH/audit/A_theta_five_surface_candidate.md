# The complete ordinary theta-five locus and a two-dimensional positive family

Status: independently reviewed and integrated as A.C2.16 on14November2026.
The complete independent review is audit/A_theta_five_surface_degeneration_review.md;
the integrated proof is in sections/A_char2_deck.tex. This derivation is retained
as the authoring record, including the converse and every parameter exclusion.
Written by the root on14November2026. No priority is claimed.

## 1. Statement

Work over an algebraically closed field Omega of characteristic two. Let

\[
\mathscr P=\{(t,r)\in\mathbf A^2:\quad
 t(t+1)r(r+1)(r+t)(r^2+t)\ne0\}.
\]

For a pair in this nonempty irreducible open surface put

\[
\begin{split}
 u(x)&=x(x+1),\qquad
 d=\frac{r(r+1)}{r^2+t},\qquad
 \kappa=\frac{r^3(r+1)^3}{(r+t)^3(r^2+t)^2},\\
 a&=\kappa,\qquad b=\frac{\kappa t^5}{r^2},\qquad
 c=\frac{\kappa(t+1)^5}{(r+1)^2}.
\end{split}                                                    \tag{S5.1}
\]

The smooth proper curve

\[
 C_{t,r}:\quad y^2+y=\phi(x),\qquad
 \phi(x)=ax+\frac b x+\frac c{x+1}                              \tag{S5.2}
\]

is ordinary of genus two. Its Raynaud theta divisor contains a point of exact order five. The corresponding geometrically connected etale cyclic degree-five cover has genus six and two-rank two; its deck group acts trivially on every geometric two-primary torsion point of its Jacobian. The geometrically prime-to-two point-section map is consequently injective for every finitely generated form of this geometric curve over F2, after every finite extension, and for its hyperbolic open subcurves.

Conversely, for a normalized ordinary genus-two curve (S5.2) with a,b,c nonzero, its Raynaud theta contains a nonzero five-torsion point **if and only if** its coefficient triple is obtained from (S5.1) for some pair in P. Thus the formulas describe the entire theta-five locus in this normalized family, not merely a sufficient chart.

The parameter map P to normalized coefficient triples has finite geometric fibres. Its image in ordinary genus-two moduli has dimension two. A nonempty open part of this locus lies outside the cubic theta locus

\[
                         (a+b+c)^3+abc=0.                     \tag{S5.3}
\]

This does not claim that theta-five torsion exists on every ordinary genus-two curve, nor does it settle universal A1.

## 2. Genus, ordinariness and the theta normalization

All a,b,c are nonzero on P. The Artin–Schreier function has exactly the three simple poles0,1,infinity. Their different exponents are two, so Riemann–Hurwitz gives genus two. Let W0,W1,Winfinity be the three ramification points. As in the proved A.C2.11 and A.C2.13,

\[
 \operatorname{div}(dx)=2W_0+2W_1-2W_\infty,\qquad
 B_\theta=W_0+W_1-W_\infty,\qquad
 \mathcal B_C\simeq\mathcal O_C(B_\theta).
\]

The two regular logarithmic differentials dx/x and dx/(x+1) are independent and Cartier-fixed, so the curve is ordinary of two-rank two. The Raynaud theta convention is

\[
 \Theta=\{\mathcal O_C(R-B_\theta):R\in C(\Omega)\}.
\]

This is an irreducible principal theta divisor; twice B_theta is canonical. We use the established locally exact-differential convention, including its Frobenius twist, exactly as in A.C2.5 and A.C2.11. All identities below are geometric and transport canonically on odd torsion through that twist.

## 3. Exact norm and divisor

Put

\[
 \delta=\phi(t)=at+b/t+c/(t+1),\qquad
 \beta^2+\beta=\delta,\qquad R=(t,\beta).
\]

Let

\[
 A(x)=d(x+t),\qquad B(x)=x+r,\qquad
                       h=A+B(y+\beta).                       \tag{S5.4}
\]

The exact universal identity in Omega(x) is

\[
 u(A^2+AB)+B^2(u\phi+\delta u)
                         =\kappa(x+t)^5.                     \tag{S5.5}
\]

Here u*phi is a polynomial, so (S5.5) is a polynomial identity. The certificate proves it in the exact rational function field F2(x,t,r), not just at a sample of parameters.

A derivation explains the choice of parameters. Write

\[
 q_t(x)=\frac{(x+t)^5}{u(x)},\qquad
 q_t'(x)=\frac{(x+t)^4(x^2+t)}{u(x)^2}.
\]

At x=r both q_t and q_t' are nonzero. Set

\[
 \rho=\frac{q_t(r)}{q_t'(r)}
      =\frac{(r+t)r(r+1)}{r^2+t},\qquad
 v(x)=\frac\rho{x+r}+\frac\rho{t+r}.
\]

Then A=Bv and kappa=q_t(r)/q_t'(r)^2. The double and simple pole coefficients of kappa*q_t/B^2 at r are respectively rho^2 and rho. They are exactly cancelled by v^2+v. The resulting rational function has only simple poles0,1,infinity, with coefficients b,c,a as in (S5.1); it vanishes at x=t. It is therefore phi(x)+phi(t), proving (S5.5). This principal-part argument uses the explicit nonvanishing exclusions in P.

Since (y+beta)^2+(y+beta)=phi+delta, equation(S5.5) says

\[
                  N_{C/\mathbf P^1}(h)
                        =\frac{\kappa(x+t)^5}{u}.             \tag{S5.6}
\]

At R, h=0 and its Artin–Schreier conjugate equals B(t)=t+r, which is nonzero. The x-map is etale at R. The unique zero of the norm is consequently a zero of h of exact order five at R, with no zero at the conjugate point.

At W0 and W1, B has nonzero values r and r+1, and the y term gives a simple pole of h. At Winfinity, xy has pole order three, while A has pole order at most two and the remaining y term has pole order one. Thus no cancellation can remove the leading pole. There are no further poles. We have

\[
\operatorname{div}(h)=5R-W_0-W_1-3W_\infty,
\qquad \operatorname{div}(u)=2W_0+2W_1-4W_\infty,
\]

and hence

\[
                    \operatorname{div}(h/u^2)
                           =5(R-B_\theta).                  \tag{S5.7}
\]

The theta point eta=O(R−B_theta) is nonzero. Otherwise 2R would be canonical, making R a Weierstrass point of the genus-two hyperelliptic map. Its x-coordinate t is neither0,1 nor infinity. Thus eta has exact order five.

## 4. The degree-five cover and point-section injectivity

The normalization given geometrically by z^5=h/u^2 is connected because eta has exact order five; a fifth root in Omega(C) would make R−B_theta principal. It is etale because all valuations of h/u^2 are divisible by five, and five is prime to the characteristic. Its group is mu5, and Riemann–Hurwitz gives genus1+5(2−1)=6.

The four nonzero characters form the single doubling orbit

\[
                            1,2,4,3\pmod5.
\]

Each corresponding H1(C,L^i) is one-dimensional. The theta point eta makes one Frobenius arrow zero, so the entire nontrivial cycle is nilpotent. The invariant part is the ordinary H1(C,O_C) of stable rank two. The exact all-character formula in A.C2.5 therefore gives f(D)=2, and A.C2.8 gives the entire order-five deck group as the kernel on geometric two-primary torsion.

Apply the proved criterion A.C2.7. A collision downstairs would lift to a two-primary point-divisor difference upstairs. A nonidentity deck element fixes that difference and produces a linear equivalence between distinct effective divisors of degree two. The cover D is not hyperelliptic: a free odd-order deck element would otherwise descend to an odd-order automorphism of P1, whose fixed-point fibre has at most two points, forcing a fixed point upstairs. This contradicts the freeness of an etale deck action. Thus the divisor equivalence is impossible.

For a finitely generated field K/F2 and a K-form of the geometric curve, the parameters, isomorphism, finite etale cover and deck transformations descend after a finite extension of K. Equality of section classes restricts to that extension. After one further finite extension defining a chosen lift, A.3 supplies the colliding lift with two-primary difference, and the same contradiction applies. The proper-to-open comparison is the established A.8 functorial map on fundamental groups. These reductions preserve the actual full geometrically prime-to-two groups and do not replace them by abelianized groups.

## 5. Converse: every ordinary theta-five point has these parameters

Take a normalized curve(S5.2) with a,b,c nonzero and eta in Theta of exact order five. Write eta=O(R−B_theta). The point R is not a ramification point: for a Weierstrass point W, both2W and2B_theta are canonical, so O(W−B_theta) has order dividing two. Also eta is not zero, since C is ordinary and the origin is not on its Raynaud theta. Thus R=(t,beta) with t different from0,1 and beta^2+beta=phi(t).

Choose g with divisor5(R−B_theta), and let h=g*u^2. Its divisor is exactly5R−W0−W1−3Winfinity. Riemann–Roch gives

\[
 L(W_0+W_1+3W_\infty)
                   =\langle1,x,y,xy\rangle_\Omega.           \tag{S5.8}
\]

Indeed the divisor has degree five, hence its space has dimension four; the displayed four functions satisfy the pole bounds and are linearly independent because y is quadratic over Omega(x). Write h=A(x)+B(x)(y+beta) with A,B linear. The exact order-three pole at infinity forces B to have degree one. Scale h to make B monic, writing B=x+r. Since h(R)=0, A=d(x+t).

The poles at W0 and W1 imply r not in{0,1}. Also r is not t: if both A and B vanished at t, h would have zeros at both unramified points above t, contradicting its stated divisor. Its norm must be kappa*q_t for some kappa nonzero, with kappa=a by the leading coefficient at infinity. Evaluating the norm identity and its x derivative at x=r gives

\[
              A(r)^2=\kappa q_t(r),\qquad
                     A(r)=\kappa q_t'(r).                    \tag{S5.9}
\]

The left side A(r) is nonzero by the first equality. Therefore q_t'(r) is nonzero, so r^2 is not t. Dividing the two equations gives

\[
 \kappa=\frac{q_t(r)}{q_t'(r)^2},\qquad
 d=\frac{\kappa q_t'(r)}{r+t}=rac{r(r+1)}{r^2+t}.
\]

Taking residues at0 and1 gives exactly the b and c formulas in(S5.1). This proves the converse without a hidden separability chart or additional genericity assumption.

## 6. Moduli dimension and a finite example beyond the cubic locus

P is a nonempty open subset of A2, so is irreducible of dimension two. For a fixed normalized coefficient triple, possible R correspond injectively to points of the finite group J[5]; there are at most5^4 of them. For each R, the divisor of h is fixed, so h is unique up to a nonzero scalar. Making its y-coefficient monic fixes h and determines r. Thus the parameter map has finite geometric fibres, and its image has dimension two.

Passage from normalized coefficients to geometric genus-two moduli has finite fibres. A genus-two hyperelliptic map is unique; the three branch points can be sent to0,1,infinity in only six ways. An Artin–Schreier coordinate change preserving a function with only simple poles can add only a constant: any nonconstant rational correction has an even pole in f^2+f that cannot be cancelled by the simple poles. The remaining constant is removed in the normalized model. Hence no continuous coordinate freedom changes this dimension.

For an explicit point, let omega^4+omega+1=0 in F16 and take

\[
                        t=\omega,\qquad r=\omega^2.
\]

The formulas give

\[
 (a,b,c)=(1,\omega,\omega+1),\qquad
 d=\omega^2+\omega+1,\qquad
 \delta=\omega,\qquad \beta=\omega^3+\omega.
\]

Here beta^2+beta=omega. The cubic obstruction is

\[
                (a+b+c)^3+abc=\omega^2+\omega\ne0.
\]

Thus the explicit degree-five positive example, and a nonempty open part of the irreducible surface, lie outside the cubic locus. The certificate enumerates all168 allowed pairs(t,r) over F16;156 give nonzero cubic obstruction. This finite count is illustrative; the exact universal norm and finite-fibre argument establish the family theorem.

The finite example has distinct nonzero coefficients, so the only geometric automorphism is the hyperelliptic involution. Indeed an automorphism must permute the three branch points, and the generating changes x↦x+1 and x↦1/x permute the coefficient triple, up to a removable constant. Distinct coefficients leave no nontrivial permutation. In particular the example has no nontrivial odd-order geometric automorphism and does not itself lie in an odd-order Galois elliptic-quotient class.

## 7. Source and computational scope

The proof uses only the already proved A.C2.5, A.C2.7–8 and the exact theta normalization of A.C2.11–13, together with Riemann–Roch, the Artin–Schreier local different and the elementary norm calculation. Their opened primary sources remain those recorded in the corresponding earlier proofs. No generic theta-torsion existence theorem is invoked.

`code/A_theta_five_surface_checks.py` and its JSON verify(S5.5) in F2(x,t,r), the derivative and principal-part derivation, the exact F16 example, all168 allowed F16 parameter pairs, and the complete doubling orbit modulo five. The divisor, converse, moduli dimension and section consequence are proved above rather than inferred from the finite output.

# Independent review of the theta-seven parameter surface

**Reviewer:** topos. **File reviewed:** `audit/A_theta_seven_surface_candidate.md`, proposed A.C2.15. **Conclusion:** the complete construction passes this independent check in its stated scope. In particular the degree72 finite étale parameter space and the two-dimensional moduli image are justified. This supplies the stated family, not universal theta-torsion existence.

## 1. Degree and étaleness over the whole parameter base

I independently differentiated the two rational functions in characteristic two. With \(u=x(x+1)\), \(V=x^2+t\), one gets
\[
 q_t'=(x+t)^6V/u^2,\qquad
 H_t=q_t/(q_t')^2=u^3/((x+t)^5V^2),\qquad
 H_t'=u^2/((x+t)^6V).
\]
The zeros of \(H_t\) are \(0,1,\infty\), of order3 each, and its poles are \(t\) and \(\sqrt t\), of orders5 and4. These are distinct for the stated base \(t\ne0,1\). Thus the degree is9 and every point above a nonzero finite value is unramified.

The stronger scheme statement is also valid. Over the displayed ring \(R\), the polynomial
\(P=\lambda(x+t)^5V^2+u^3\) has unit leading coefficient and degree9, so its quotient algebra is finite free of rank9. Substitution at \(x=0,1,t\), or at \(V=0\), shows that \(x,x+1,x+t,V\) do not vanish at any geometric point of this quotient. They are therefore units in it. Using \(P=0\), its derivative becomes
\[
 P'=\lambda(x+t)^4V^2+u^2=u^2V/(x+t),
\]
which is a unit. The algebra is finite étale on all of the specified base, not just generically. The diagonal in its fibre square is open and closed. Removing it leaves degree \(9\cdot8=72\), smooth and pure of dimension2. No irreducibility of this surface is required or asserted.

## 2. Principal parts and the norm identity

At \(r\), writing \(z=x+r\) and \(e=r+s\ne0\),
\[
 B^{-2}=e^{-2}z^{-2}+\text{regular terms}.
\]
There is no extra simple-pole term in this expansion in characteristic two. The two principal coefficients of \(\kappa q_t/B^2\) are therefore exactly \(\kappa q_t(r)/e^2\) and \(\kappa q_t'(r)/e^2\). Since \(\kappa/e^2=H_t(r)\), they are \((q_t/q_t')^2(r)\) and \((q_t/q_t')(r)\), namely \(\rho_r^2,\rho_r\). This confirms both coefficients, rather than merely the double pole. The same holds at \(s\) by the equal-value equation. Cross terms disappear from the square, so the remaining partial fractions and constants introduce no hidden principal parts.

After cancellation the only poles are the original three simple ones. Their coefficients are exactly \(a,b,c\). Evaluation at \(t\), where \(q_t(t)=v(t)=0\) and \(B(t)\ne0\), fixes the remaining constant and gives (S7.9). Multiplying by \(B^2\) then gives the displayed Artin–Schreier norm (S7.10) with the correct sign, which is a plus in characteristic two.

The section of the quadratic function field \(h=A+B(y+\beta)\) has no poles outside \(W_0,W_1,W_\infty\). It has simple poles at the first two because \(B(0),B(1)\ne0\), and an exact order-five pole at infinity because the monic \(x^2y\) term is the unique term of that order. At \(R_t\), its conjugate has nonzero value (B(t)); the downstairs map is étale there, so the norm zero of order7 is entirely the zero of \(h\) on this sheet. No other zero is possible. Subtracting \(3\operatorname{div}(u)=6W_0+6W_1-12W_\infty\) gives precisely \(7(R_t-B_C)\).

The nonzero theta class has exact order7. The two doubling cycles modulo7 meet the symmetric theta at opposite classes, so the already proved A.C2.5–8 criterion applies to both cycles. Its deck-kernel and nonhyperellipticity argument is consequently applicable exactly as stated. The free order-seven action cannot occur on a hyperelliptic curve: its faithful image on the hyperelliptic line has a fixed point, and its action on the fibre of at most two geometric points there has to be trivial.

## 3. Finite coefficient fibres and dimension in moduli

Fix the actual normalized equation \(y^2+y=\phi(x)\), hence fixed \(a,b,c\ne0\). Every parameter triple yields a point \(R_t\) with nonzero theta class in (J[7]). The Abel map on a positive-genus curve is injective, so there are at most \(7^4-1\) possible \(R_t\). Either choice of the Artin–Schreier root is allowed; using these possible points rather than making a global choice of the root avoids any monodromy ambiguity.

For a fixed \(R_t\), the exact divisor of \(h\) makes it unique up to scalar. Its six displayed functions form a basis of
\(H^0(C,\mathcal O(W_0+W_1+5W_\infty))\): they have the allowed poles, are linearly independent because (1,y) form a quadratic function-field basis, and the divisor has degree7, so Riemann–Roch gives dimension6. The coefficient of \(x^2y\) is nonzero by the exact infinity pole; making \(B\) monic removes the scalar freedom. Its distinct roots leave at most two ordered pairs ((r,s)). The claimed bound \(2(7^4-1)\) for each geometric coefficient fibre therefore holds. Pure dimension2 of the source and the finite-fibre dimension theorem give dimension2 for every component image.

Passing to moduli does not introduce a positive-dimensional fibre. A genus-two isomorphism preserves the unique hyperelliptic pencil and permutes its branch set \(\{0,1,\infty\}\), so its induced Möbius transformation has only six possibilities. For each, an isomorphism of the quadratic Artin–Schreier fields changes \(y\) by a rational function (z(x)). If \(z\) had a pole, \(z^2+z\) would have an even highest pole of order at least2; the difference of the two normalized right sides has only simple poles. Thus \(z\) is constant. Its constant changes no residue coefficient. The coefficient chart has finite fibres over geometric isomorphism classes, so the moduli image retains dimension2.

The checked point with nonzero cubic obstruction lies on at least one surface component. The complement of the cubic equation on that component is a nonempty open, whose image still has dimension2 by the same finite-fibre result. This justifies the claim of a two-dimensional positive locus not contained in the earlier cubic locus.

## 4. Additional formula and finite certificate

I checked the one-parameter identity directly: with \(U=t(t+1)\), \(a=U^{-2}\), one has \(b=at^5\), \(c=a(t+1)^5\), and \(\phi(t)=a(t+1)\). The two polynomial expansions in \(z=x+t\) cancel to \(az^7\) exactly. Also \(a+b+c=(U+1)/U\) and \(abc=1/U\), giving the stated cubic obstruction \((U^3+U+1)/U^3\).

I read and reran `code/BC_theta_seven_surface_checks.py`. It passed all12 good unordered fibre pairs over F16, all12 corresponding nonzero cubic obstructions, all14 parameters of the simpler family, and the displayed norm coefficients and explicit example. These checks corroborate the finite examples; the all-parameter and dimension assertions were checked by the arguments above, not inferred from the sample.

No integrated A source or ledger was edited in this review. The existing external theta/Frobenius and section-collision inputs are exactly those already stated in A.C2.5–8; no additional existence theorem is needed for the new elementary construction.

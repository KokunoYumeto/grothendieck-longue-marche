# Fixed-curve algebraicity check

Post-freeze mathematical note by GPT-6 Astra Pro, primary run with independent scope review by uniformization_context; numerical effort setting not exposed. This does not alter any manuscript reading. It answers the fixed-curve question on scan 115 using classical analytic input, without a historical novelty claim.

## Statement and scope

Let X be a smooth connected algebraic curve of finite type over C. Its canonical uniformizing projective connection is algebraic on X, including when X is not complete. In the hyperbolic case its associated projective flat object is regular singular at the punctures. The construction is over C; no smaller-field descent, formula for accessory parameters, or general algebraic dependence on moduli is asserted.

## Hyperbolic case

Write X=barX−D, with barX the smooth projective compactification and D the finite reduced boundary. The classical finite-type cusp uniformization theorem says that near each puncture the inverse developing map is Möbius-equivalent to log(q), where q is a holomorphic parameter vanishing simply at that puncture. The exact double-pole behavior is also stated in Takhtajan, *Real projective connections…* (2014), §§2.1–2.2: the standard-Schwarzian coefficient is 1/(2t²)+O(1/t), hence the current G coefficient is −1/t²+O(1/t).

For clarity, retain the coordinate-change term. If q=t u(t), with u holomorphic and nonzero at 0, then

\[
G_t(\log q)=G_t(q)-\left(\frac{q'}q\right)^2
=-\frac1{t^2}+O(t^{-1}).
\]

Here G_t(q) is holomorphic, since q' is a unit. Thus the uniformizing projective connection has at most a double pole in the compactification parameter, with fixed leading coefficient −1.

Choose a holomorphic projective connection c_ref on barX, supplied by compact uniformization. Proper GAGA algebraizes that reference. The difference c_unif−c_ref is intrinsically a quadratic differential on X and, by the local calculation, extends to a holomorphic section of the line bundle omega_barX²(2D) on barX. GAGA identifies that section with an algebraic one. Adding it to c_ref and restricting to X produces the algebraic projective connection corresponding to the analytic uniformizing object. The canonical algebraic projective-bundle/section construction from the second jets identifies its associated marked triple.

Regular singularity can be checked independently of a naming convention. For u''=(mu/4)u with mu having at most a double pole, put v=t u'. Then

\[
d\binom u v=\frac{dt}{t}
\begin{pmatrix}
0&1\\
t^2\mu/4&1
\end{pmatrix}
\binom u v.
\]

The matrix in brackets is holomorphic at the boundary. This is a logarithmic system, so it gives the required regular singularity after local rank-two lifting and hence projectively.

## Remaining cases

If the universal cover is P1, X=P1 and compact GAGA applies. If it is C, X is C, C*, or a compact elliptic curve. The affine distribution dw+eta=0 in notes E09–E10 is algebraic for the first two cases; the elliptic case also follows from compact GAGA. These cover all nonhyperbolic finite-type cases.

## The three-puncture formula

For P1−{0,1,infinity}, set

\[
\mu(z)=-\frac{z^2-z+1}{z^2(z-1)^2}.
\]

The leading coefficients of its quadratic differential at 0, 1, and infinity are all −1. Any other coefficient with the same leading terms differs by a quadratic differential with at most simple poles at the three points. That line bundle has degree −4+3=−1 and no global section. Therefore the formula is the uniformizing connection, by existence and the cusp condition. The three leading-coefficient limits are checked in additional_checks.py.

The ordinary projective connection restricted from P1 has zero coefficient in z, so it is a different projective connection on the same punctured curve. Hua's later statement identifying the two cannot be adopted literally. No image beyond scan 134 was consulted.

## Limits of the conclusion

- Fixed complex accessory parameters are allowed as constants in algebraic geometry over C. An inability to express them by an algebraic formula in moduli is a different question.
- An algebraic connection over C need not descend to a chosen number field.
- The canonical Fuchsian section is not holomorphic in arbitrary moduli variation; this fixed-curve proof does not change F06.
- Deligne's regular algebraization theorem alone does not prove the marked section algebraic. The boundary argument supplies the additional step for this particular uniformizing object.

Primary source route: https://www.math.stonybrook.edu/~leontak/TMPh.pdf, §§2.1–2.2, printed1308–1309. Root and uniformization_context both opened and read the cited passage. Proper GAGA was checked in Serre's original1956 paper, §12, Theorems1–3. No new proof of the uniformization or GAGA theorems is claimed.

# Independent review of F.47: the henselization obstruction

**Reviewer:** degeneration agent.  
**Conclusion:** PASS in the candidate's stated scope.  
**Reviewed:** all eight sections of `audit/F_henselization_obstruction_candidate.md`, together with the complete existing F.32 and F.40 proofs.  
**Candidate SHA-256 at review:** `8cb46028ab58ee76ce7a8a77168606f6630de650ef07d39530fd3efe92611bc4`.

The review independently checks the algebraic closure, the action on every Galois element (including inertia), and the valuation corollary without a discreteness assumption. The conclusion concerns the actual closed-point-preserving relative-topos convention already fixed in Part F. It does not claim an intrinsic converse classification of all reconstruction fields.

## 1. The henselization identification

The current Stacks statements have exactly the hypotheses used: fields are excellent; finite-type extensions and localization preserve excellence; a Noetherian local domain which is a G-ring has henselization equal to the elements of its completion algebraic over its fraction field. Thus for \(R=F[t]_{(t)}\), \(R^h\) is the algebraic power-series ring inside \(F[[t]]\). Multiplication by a power of \(t\) proves
\[
 \operatorname{Frac}(R^h)=F((t))\cap F(t)^{\mathrm{alg}}=A_0(F).
\]
This is the ordinary henselization. No ramified roots of \(t\) have been inserted at this point. Its value group is \(\mathbf Z\) and its residue field is \(F\).

## 2. The closure and the Fourier/trace calculation

The independently opened van den Dries–Ribenboim proposition is specifically the bounded-coefficient statement needed here:
\[
 \Omega=\bigcup_{F'/F\ {\rm finite},\,n\geq1}F'((t^{1/n}))
\]
is an algebraic closure of \(F((t))\). It does not require treating arbitrary series with coefficients in \(\bar F\) as algebraic over \(F((t))\). The relative algebraic closure \(\Omega_0\) of \(F(t)\) in \(\Omega\) is algebraically closed, by transitivity of algebraicity applied to each polynomial's finitely many coefficients. It is therefore an algebraic closure of \(A_0(F)\).

The more precise generator identity (47.7) also checks directly. If \(u^n=t\) and \(a=\sum_k a_k u^k\), the finite Fourier sum in (47.8) is
\[
 \frac{u^{-j}}n\sum_{\zeta^n=1}\zeta^{-j}a(\zeta u)
       =\sum_{m\in\mathbf Z}a_{j+nm}t^m.
\]
There are finitely many negative exponents. Substitution \(u\mapsto\zeta u\) preserves \(F(t)\), so every resulting \(b_j\) remains algebraic over \(F(t)\).

After making \(F'/F\) finite Galois, the trace-dual coefficient expansion is valid in the finite extension \(F'((t))/F((t))\): an \(F\)-basis of \(F'\) is still a basis after passing to Laurent series, as coefficient comparison shows. Each \(b_{ij}\) is a finite sum of coefficientwise conjugates and is algebraic over \(F(t)\). Hence \(b_{ij}\in A_0(F)\). This proves that every element of \(\Omega_0\) is in a field \(A_0(F)F'(t^{1/n})\), not merely in an infinite completion of that field.

The semidirect-product description follows as written. Constant extensions have their original degrees; adjoining \(t^{1/n}\) has degree \(n\) by the discrete valuation; the compatible root multipliers give the entire inertia kernel. Coefficientwise \(G_F\) is a continuous splitting: every algebraic element under discussion has its coefficients in a single finite extension. The conjugation action on root multipliers is cyclotomic.

## 3. The substitution and commutation with all inertia

At each \(F'((u))\), the substitution
\[
 u\longmapsto u(1+u^n)^{1/n}
\]
is a formal-series automorphism because its linear coefficient is one. The roots with constant coefficient one make these automorphisms compatible under increasing \(n\). Its inverse is obtained from \(r+r^2=t\), \(r\in t\mathbf Q[[t]]\), using the unit root of \(r(t)/t\).

Both substitutions preserve the algebraic core: the image of \(t\) is respectively \(t+t^2\) or \(r(t)\), each algebraic over \(F(t)\). They restrict to mutually inverse automorphisms of \(A_0(F)\).

For an arbitrary \(g\in G_{A_0(F)}\), agreement of \(g\tau\) and \(\tau g\) is checked on actual field generators:

- On \(A_0(F)\), \(g\) is the identity and \(\tau\) preserves the field.
- On \(\bar F\), \(\tau\) is the identity and \(g\) preserves the algebraic constants.
- On \(u=t^{1/n}\), one has \(g(u)=\zeta_nu\) and
  \((1+t)^{1/n}\in A_0(F)\), so both composites send \(u\) to
  \(\zeta_nu(1+t)^{1/n}\).

The last bullet does not assume \(g\) is a coefficientwise automorphism: it applies to every root multiplier, hence to all inertia. Equation (47.7) then gives equality on all \(\Omega_0\). There is no illicit passage from agreement on coefficients to agreement on arbitrary infinite sums under an abstract field automorphism.

## 4. Topos obstruction and inheritance

The existing F.40 construction has precisely the needed hypotheses. The nonidentity field automorphism \(\sigma(t)=t+t^2\) has trivial outer Galois action, indeed a lift centralizing the full group. Its semilinear scheme automorphism of \(\mathbb G_m\) yields a pinned relative geometric automorphism under the chosen CHW convention.

Its map on rational points is \(a\mapsto\sigma^{-1}(a)\). A \(k\)-scheme map of \(\mathbb G_m\) is \(cT^m\). Fixing \(1\) and \(2\) forces \(c=1\) and \(m=1\); moving \(t\) contradicts that form. Thus this is a nonconstant full-topos counterexample, not only an outer-fundamental-group construction.

F.32 expressly covers arbitrary algebraic extensions, without normality or finiteness. Its contrapositive proves non-reconstruction for every algebraic extension \(E/A_0(F)\). The candidate correctly avoids claiming that the displayed substitution preserves any prescribed \(E\).

One optional exposition improvement was sent to the author: in comparing \(A_0(F)\) with the earlier Puiseux algebraic core \(A(F)\), first mention the immediate inclusion \(A_0(F)\subset A(F)\); algebraicity over \(F(t)\) then makes the latter an algebraic extension of the former. This is a clarification, not a gap.

## 5. Coefficient fields and nondiscrete valuations

The coefficient-field construction is valid for every equicharacteristic-zero henselian valuation. A maximal subfield of its valuation ring has algebraic residue extension, because a lift of a transcendental residue could be adjoined while all nonzero polynomial values remain units. A missing algebraic residue element is separable; Hensel lifting its minimal polynomial enlarges that subfield, a contradiction. No completeness, discreteness, or finite-rank hypothesis occurs.

For \(0\ne t\in\mathfrak m_v\), distinct powers of \(t\) have distinct valuations, so a polynomial over this coefficient field has a unique lowest-valuation term. Consequently \(t\) is transcendental over \(F\), and the restricted valuation ring on \(F(t)\) is \(F[t]_{(t)}\), even if the ambient value group is nondiscrete.

The exact residue-transcendence hypothesis is essential to the proof:
\[
 \operatorname{trdeg}_{\mathbf Q}F=d-1
 \quad\Longrightarrow\quad
 \operatorname{trdeg}_{\mathbf Q}F(t)=d
 \quad\Longrightarrow\quad K/F(t)\text{ is algebraic}.
\]
The universal property of henselization embeds \(A_0(F)\) into \(K\). The latter is then algebraic over it, so Section 4 applies. This proves precisely the stated necessary condition. It does not address arbitrary henselian valuations lacking the residue-degree equality, or arbitrary transcendental extensions of \(A_0(F)\).

## 6. Finite certificate

I independently reran the 27 exact identities using the arithmetic functions in `code/F_Puiseux_checks.py`, without invoking its output-writing main function and without modifying the existing output. All checks passed in \(\mathbf Q[t]/(t^{13})\): the two inverse compositions, \(r+r^2=t\), six unit-root equations, and all indicated divisibility compatibilities.

These finite checks are supplementary. The algebraic closure, infinite-series, Galois, and topos conclusions are justified by the preceding proofs, not by truncation.

## 7. Independently opened primary passages

1. The Stacks Project, Example 16.13.3, Tag 0A1W, entire example:
   https://stacks.math.columbia.edu/tag/0A1W.
   Review retrieval `turn847view0`.
2. The Stacks Project, Proposition 15.53.3 and Lemma 15.53.2:
   https://stacks.math.columbia.edu/tag/07QW and
   https://stacks.math.columbia.edu/tag/07QU.
   Review retrievals `turn847view1`, `turn849view3`.
3. van den Dries, L., & Ribenboim, P. (1984). The absolute Galois group of a rational function field in characteristic zero is a semi-direct product. *Canadian Mathematical Bulletin, 27*(3), 313–315. Proposition and proof, printed p. 314. Publisher PDF:
   https://www.cambridge.org/core/services/aop-cambridge-core/content/view/D25D46CEEAC14FF372584F2603E86360/S0008439500067916a.pdf/the-absolute-galois-group-of-a-rational-function-field-in-characteristic-zero-is-a-semi-direct-product.pdf.
   Review retrieval `turn849view0`; the exact proposition and proof were also returned at `turn848search12`.
4. Aschenbrenner, M., van den Dries, L., & van der Hoeven, J. (2017). *Asymptotic differential algebra and model theory of transseries*. Princeton University Press. Accessed 729-page author version:
   https://www.texmacs.org/joris/mt/mt.pdf.
   Proposition 3.3.8 and Lemma 3.3.9, author pp. 117–118, PDF pages 134–135 zero-indexed; henselization definition and Proposition 3.3.25, author p. 125, PDF page 142 zero-indexed. Review retrievals `turn849view1` and `turn849view2`. The author version's pagination is distinguished from the published book.

The complete existing internal proofs F.32 and F.40 were reread locally. No claim of novelty, exhaustive literature coverage, or a converse reconstruction classification is made.

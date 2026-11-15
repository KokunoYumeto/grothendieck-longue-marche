# Post-freeze mathematical diagnostics: simplex coefficients and the point test

**Status:** independent mathematical analysis of formulas supplied in the research task, authored 2026-11-15 after the transcription freeze. This analysis did not consult scans or transcription files. It neither identifies manuscript readings nor proposes changes to the frozen transcription. Its conclusions are conditional on the definitions and grading assumptions explicitly stated below; no historical priority or novelty claim is made.

## 1. The normalized simplex coefficient is one

Let

\[
\Delta_n=\{(x_0,\ldots,x_{n-1})\in\mathbb R^n:
x_a\geq0,\ \textstyle\sum_a x_a\leq1\}
\]

carry the orientation \(dx_0\wedge\cdots\wedge dx_{n-1}\). For nonnegative integers \(i_0,\ldots,i_{n-1}\), put

\[
I_n(i)=\int_{\Delta_n}\prod_{a=0}^{n-1}x_a^{i_a}\,dx_0\cdots dx_{n-1},
\qquad
\gamma_i=\frac{(n+\sum_a i_a)!}{\prod_a i_a!}I_n(i).
\]

Then

\[
I_n(i)=\frac{\prod_a i_a!}{(n+\sum_a i_a)!},
\qquad \boxed{\gamma_i=1}.
\tag{1}
\]

One proof uses induction on \(n\). Write \(r=n-1\), \(b=i_{n-1}\), \(a_j=i_j\) for \(j<r\), and \(A=\sum_{j<r}a_j\). For fixed \(x_{n-1}=t\), substitute \(x_j=(1-t)y_j\) in the other coordinates. The Jacobian contributes \((1-t)^r\), so

\[
I_n(a,b)=I_r(a)\int_0^1t^b(1-t)^{A+r}\,dt.
\]

For nonnegative integers \(p,q\), repeated integration by parts gives

\[
\int_0^1t^p(1-t)^q\,dt=\frac{p!q!}{(p+q+1)!}.
\]

Combining this identity with the induction hypothesis proves (1). The base case is the positively oriented zero-dimensional simplex, with \(I_0(\varnothing)=1\), empty product equal to one, and \(\gamma_{\varnothing}=1\). In dimension one, the claim is simply \((i+1)\int_0^1x^i\,dx=1\).

This calculation is self-contained. As a formula cross-check, the official *NIST Digital Library of Mathematical Functions*, equation 5.14.1, gives the same simplex integral after setting its parameters to \(z_{a+1}=i_a+1\) (National Institute of Standards and Technology [NIST], 2026). Its equation 5.14.2 is the more general formula with an additional power of the final barycentric coordinate. Neither equation supplies a claim about the historical manuscript.

## 2. Exact interpretation of the candidate recurrence

Assume throughout that

\[
C_{a,b}=\binom{a+b}{a}\quad(a,b\geq0).
\tag{2}
\]

This is an explicit hypothesis of this diagnostic, not an identification of an ambiguous letter or convention in the manuscript. With the preceding notation, set

\[
m=b+1,\quad L=\sum_{j<r}\ell_j,\quad
\lambda=m-L,\quad N=A+r+m=n+\sum_a i_a.
\]

The candidate recurrence is

\[
\gamma_{a_0,\ldots,a_{r-1},b}
=\sum_{\substack{\lambda,\ell_0,\ldots,\ell_{r-1}\geq0\\
\lambda+\sum_j\ell_j=m}}
(-1)^L
\left(\prod_{j<r}\binom{a_j+\ell_j}{a_j}\right)
\binom{\lambda+r+A+L}{\lambda}
\gamma_{a_0+\ell_0,\ldots,a_{r-1}+\ell_{r-1}}.
\tag{3}
\]

The upper entry of the last binomial coefficient is always \(N\). Every summation index is a nonnegative integer. Thus the sum is finite, and every coefficient is an integer.

### 2.1 Derivation from ordinary integration

Integrate in the final coordinate first. Since \(m=b+1\),

\[
I_n(a,b)=\frac1m\int_{\Delta_r}
\prod_{j<r}x_j^{a_j}\left(1-\sum_{j<r}x_j\right)^m
\,dx_0\cdots dx_{r-1}.
\tag{4}
\]

The multinomial expansion is

\[
\left(1-\sum_{j<r}x_j\right)^m
=\sum_{\lambda+L=m}
\frac{m!}{\lambda!\prod_j\ell_j!}
(-1)^L\prod_jx_j^{\ell_j}.
\]

Multiplying (4) by \(N!/(b!\prod_j a_j!)\), and using \(m!/(mb!)=1\), gives

\[
\gamma_{a,b}
=\sum_{\lambda+L=m}(-1)^L
\frac{N!}{\lambda!\prod_j a_j!\ell_j!}
I_r(a+\ell).
\]

Now substitute the *definition*

\[
I_r(a+\ell)
=\frac{\prod_j(a_j+\ell_j)!}{(r+A+L)!}\gamma_{a+\ell}.
\]

The resulting coefficient factors exactly as

\[
\frac{N!}{\lambda!(r+A+L)!}
\prod_j\frac{(a_j+\ell_j)!}{a_j!\ell_j!}
=C_{\lambda,r+A+L}\prod_jC_{a_j,\ell_j}.
\]

This proves (3), without first assuming that the lower-dimensional coefficients equal one. In particular, the final factor \(C_{\lambda,r+A+L}\) is required by this normalization.

### 2.2 Generating-function proof that the recurrence gives one

Set every lower-dimensional \(\gamma\) on the right of (3) to one. The right-hand side becomes

\[
R=\sum_{L=0}^m(-1)^L\binom{N}{m-L}
\sum_{\ell_0+\cdots+\ell_{r-1}=L}
\prod_{j<r}\binom{a_j+\ell_j}{a_j}.
\]

In the ring of formal power series \(\mathbb Z[[z]]\),

\[
\prod_{j<r}(1+z)^{-a_j-1}
=\sum_{\ell_0,\ldots,\ell_{r-1}\geq0}
(-1)^L\left(\prod_{j<r}\binom{a_j+\ell_j}{a_j}\right)z^L
=(1+z)^{-A-r}.
\]

Consequently,

\[
R=[z^m](1+z)^N(1+z)^{-A-r}
=[z^m](1+z)^m=1.
\tag{5}
\]

Only the coefficient of a fixed finite degree is used; no analytic convergence assertion is needed. For \(r\geq1\), the equivalent grouped sum is

\[
\sum_{L=0}^m(-1)^L\binom{N}{m-L}
\binom{A+r+L-1}{L}=1.
\]

The ungrouped form and the formal-power-series proof also handle \(r=0\). In that case the tuple \(\ell\) is empty, its sum is zero, \(\lambda=m\), and the only term is \(C_{m,0}\gamma_{\varnothing}=1\). Thus dimension one is valid without using a binomial coefficient with a negative upper entry. Given \(\gamma_{\varnothing}=1\), (3) determines all coefficients uniquely by induction on their tuple length, and (5) shows that every one of them is one.

## 3. Stokes and sign conventions

For the ordinary differential form

\[
\omega=\left(\prod_{j<r}x_j^{a_j}\right)x_r^b
\,dx_0\wedge\cdots\wedge dx_r,
\]

take the primitive

\[
\eta=\frac{(-1)^r}{b+1}
\left(\prod_{j<r}x_j^{a_j}\right)x_r^{b+1}
\,dx_0\wedge\cdots\wedge dx_{r-1}.
\]

Then \(d\eta=\omega\). Differentiating the earlier-coordinate factors gives zero because of repeated differentials; moving \(dx_r\) past the preceding \(r\) differentials cancels the explicit \((-1)^r\).

On each face \(x_j=0\) with \(j<r\), the pullback of \(dx_j\) is zero. On \(x_r=0\), the factor \(x_r^{b+1}\) is zero. Thus only the slanted face \(\sum_jx_j=1\) contributes. Parameterizing it by \((x_0,\ldots,x_{r-1})\) gives boundary orientation \((-1)^r\,dx_0\wedge\cdots\wedge dx_{r-1}\) under the outward-normal-first convention. This orientation sign cancels the sign in \(\eta\), producing (4). Its expansion therefore gives precisely \((-1)^L\) in (3).

There is **no additional factor \((-1)^m\)** if the summand has already been written with sign \((-1)^L\). However, because \(\lambda+L=m\),

\[
(-1)^{m+\lambda}=(-1)^L.
\]

An outside factor \((-1)^m\) together with an inside factor \((-1)^\lambda\) is therefore an equivalent sign convention, not an error. Reordering coordinates, reversing simplex orientation, or changing the boundary convention must be accounted for before comparing formulas. The computation here establishes consistency of the explicitly supplied formula under the conventions above; it does not establish which conventions an unexamined manuscript uses.

For \(n=1\), Stokes reduces to evaluating \(x_0^{b+1}/(b+1)\) at the endpoints: the value at zero vanishes, and the positively oriented endpoint at one contributes \(1/(b+1)\). This independently checks the edge case.

## 4. Exact arithmetic checks

The adjacent script `check_pd_diagnostics.py` enumerates the summands using integer arithmetic and checks both the ungrouped and grouped forms. It checks all **1,364** index tuples with \(1\leq n\leq5\) and each \(i_a\in\{0,1,2,3\}\). All checks passed. The adjacent `pd_diagnostics_checks.json` records the inputs, counts, individual example summands, and results. These checks verify indexing and arithmetic; equation (5), rather than a finite test set, proves the general identity.

The integral column below evaluates the factorial formula (1) exactly; it is not an independent numerical quadrature calculation. The summands are grouped by increasing \(L\).

| Indices \(i\) | \(I_n(i)\) | Grouped recurrence terms | Sum |
|---|---:|---|---:|
| \((0)\) | \(1\) | \(1\) | \(1\) |
| \((3)\) | \(1/4\) | \(1\) | \(1\) |
| \((0,0)\) | \(1/2\) | \(2,-1\) | \(1\) |
| \((1,0)\) | \(1/6\) | \(3,-2\) | \(1\) |
| \((0,1)\) | \(1/6\) | \(3,-3,1\) | \(1\) |
| \((1,1)\) | \(1/24\) | \(6,-8,3\) | \(1\) |
| \((0,0,0)\) | \(1/6\) | \(3,-2\) | \(1\) |
| \((1,1,1)\) | \(1/720\) | \(15,-24,10\) | \(1\) |

For \(i=(0,0)\), removing \(C_{\lambda,r+A+L}\) from the proposed expression gives \(1-1=0\), so that omission is detected in the first nontrivial dimension. Multiplying the already displayed \((-1)^L\) sum by an extra \((-1)^m\) gives \(-1\) in the same example. These are diagnostics of altered candidate formulas, not judgments about manuscript readings.

## 5. The point test for retaining every weight

The proposed point diagnostic is valid under the following explicit hypotheses. A chain-valued construction \(F\) sends the represented zero-simplex to \(A^0=S\); this complex is concentrated in chain degree zero with zero differential; \(S=\mathbb Z[u]\); and the powers of \(u\) are retained as an additional weight grading, rather than reassigned to nonzero chain degrees. Then

\[
H_0(F(\Delta^0))=S=\mathbb Z[u]
=\bigoplus_{j\geq0}\mathbb Z\,u^j,
\qquad H_k(F(\Delta^0))=0\quad(k\neq0).
\]

Ordinary integral homology of the represented point is \(H_0(\Delta^0;\mathbb Z)=\mathbb Z\). The retained-weight complex therefore cannot itself be quasi-isomorphic, as a complex of abelian groups, to ordinary integral chains on every space: the point already detects a mismatch. Being defined over \(\mathbb Z\) does not by itself mean that a complex computes ordinary homology with coefficient group \(\mathbb Z\). The displayed answer is consistent with a model having coefficient ring \(S\), or with a larger weighted object from which an ordinary chain model is subsequently extracted.

The condition \(F(\Delta^0)=A^0\) holds, for example, for the usual extension of a genuinely cosimplicial chain object by the colimit over the category of simplices: for the simplicial point, that category has final object its unique zero-simplex. For a construction on semisimplicial sets, the **represented** zero-simplex likewise has only its zero-simplex. It must not be confused with the terminal semisimplicial presheaf, which has one simplex in every dimension; a point test should specify which object is being used.

The conclusion is limited to the stated grading and realization assumptions. If \(u\) has positive chain degree in the total complex, the asserted computation of \(H_0\) need not apply. If the construction includes weight-zero extraction, an augmentation \(\mathbb Z[u]\to\mathbb Z\), or another specified weight/realization operation, that operation must be evaluated before making a comparison with ordinary chains. For the isolated point, weight zero is \(\mathbb Z\), and base change of the free degree-zero \(S\)-module along an augmentation gives \(\mathbb Z\); neither observation proves an equivalence on general spaces. No identification of an intended operation such as \(\tau_\infty\) is made here.

## 6. Scope for later interpretation

The recurrence check establishes an internally consistent integral coefficient identity. It does not, by itself, establish a multiplicative quasi-isomorphism with ordinary integral cochains, a fully faithful homotopy reconstruction theorem, or a relation between a weighted divided-power structure and any specified modern binomial or \(E_\infty\) model. Likewise, the point test rules out a particular unprocessed interpretation only under its explicit hypotheses. These distinctions preserve the possibility that a smaller divided-power ideal, a weight operation, a different total grading, or an additional realization step changes the comparison.

## Reference

National Institute of Standards and Technology. (2026). §5.14 Multidimensional integrals. In *NIST Digital Library of Mathematical Functions* (Version 1.2.8; released September 15, 2026), equations 5.14.1–5.14.2. https://dlmf.nist.gov/5.14

The reference is an official formula cross-check; all proofs and conditional diagnostics in this record are provided explicitly above.

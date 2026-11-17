# Independent checks of proposed counterexamples

Prepared after freeze at the parent reader's request. Only frozen TeX and the supplied modernised context were consulted; no scan images were read, and no transcription was changed. These are mathematical checks of statements as transcribed, not determinations of what the ink should say.

## 1. Pointwise polynomial ranks do not provide a uniform degree bound

Let \(p_1,p_2,\ldots\) be distinct primes, and let \(N\) be the nonnegative chain complex with \(N_0=0\), \(N_i=\mathbb Z/p_i\) for \(i\geq1\), and zero differential. Under inverse Dold–Kan,
\[
L_n\cong\bigoplus_{i=1}^{n}(\mathbb Z/p_i)^{\binom ni}.
\]
Thus every simplicial degree is finitely generated; ordinary tensor product commutes with this finite-sum construction, so
\[
\dim_{\mathbb F_{p_i}}(L_n\otimes\mathbb F_{p_i})=\binom ni,
\qquad L_n\otimes\mathbb Q=0,
\]
and every other residue field gives zero unless its prime is among the \(p_i\). The coefficient of \(\binom ni\), as a function on \(\operatorname{Spec}\mathbb Z\), is the indicator of the closed point \((p_i)\), hence constructible. Nevertheless \(H_i(N)=\mathbb Z/p_i\neq0\) in arbitrarily high degrees, so \(N\) is not perfect; constructibility of each member of an **infinite** coefficient family does not yield a common degree bound.

**Scope:** this disproves sufficiency of the pointwise residue-field polynomial condition in frozen scans 014(e)–015, assuming the quantified statement is exactly as transcribed. It also contradicts the assertion in **Hua, modernised reading of cote 137**, subsection *Définitions*, footnote to Proposition 1(e), that noetherian constructibility supplies its added uniform bound. It does **not** contradict Hua's corrected implication when a common bound is independently assumed, nor scan 014(c), whose projective-component hypothesis is stronger and is not satisfied by this example. All tensor products in the displayed rank calculation are ordinary; replacing them silently by derived fibers would change the statement under examination.

## 2. Perfection does not force polynomial ranks of an arbitrary representative

Let \(N_i=\mathbb Z\) for every \(i\geq0\), with \(d_i=1\) for odd \(i\) and \(d_i=0\) for even \(i\). The homotopy \(h_i=1\) for even \(i\), \(h_i=0\) for odd \(i\), satisfies \(dh+hd=1\); consequently \(N\) is contractible and represents the perfect zero object. But \(L=\mathrm{DK}(N)\) has
\[
L_n\cong\mathbb Z^{\sum_{i=0}^{n}\binom ni}=\mathbb Z^{2^n},
\]
so its residue-field rank functions are not eventually polynomial, even though all \(L_n\) are finite free. This refutes necessity for derived \(\partial\)-perfection, strengthening the same representative-dependence objection made in Hua's footnote using an infinite-rank contractible complex; it does not refute the strict-perfection criterion because the displayed normalization is unbounded.

## 3. A divided square of a special simplicial module need not be special

Take \(K=K(\mathbb Z,1)\) in its simplicial abelian-group model \(K_n=\mathbb Z^n\), and apply the homogeneous divided square \(\Gamma^2\) degreewise. Compute normalization as the quotient by degenerate simplices: its degree-one group is \(\mathbb Z\gamma_2(e)\), and in degree two the pure squares are degenerate, leaving \(\mathbb Z(e_1e_2)\). In degree \(n\geq3\), every basis monomial involves at most two coordinates and hence omits some coordinate; it lies in the image of the degeneracy inserting that zero coordinate, so the normalized quotient vanishes. The faces in degree two are \(d_0(a,b)=b\), \(d_1(a,b)=a+b\), and \(d_2(a,b)=a\), and the divided-power identity \(e^2=2\gamma_2(e)\) gives
\[
(d_0-d_1+d_2)(e_1e_2)=-2\gamma_2(e).
\]
Therefore \(H_1(N\Gamma^2K)=\mathbb Z/2\) and all other homology groups vanish. The input is a strictly special generator over \(\mathbb Z\), whereas the output has nonprojective homotopy; this refutes closure of all special simplicial modules under \(\Gamma^2\). It supplies a concrete mathematical reason that the broad operation-closure bracket in scan 010 cannot stand, but does not determine which operation the handwritten marginal cancellation was meant to target or settle the separate exterior-power claims in scan 012.

## Status

All three calculations are verified elementary examples, with high confidence in their stated scope; they are offered as this return's checks, not novelty claims. The third computation uses the quotient version of normalization, whose chain groups differ from the intersection-of-face-kernels presentation while giving the canonically isomorphic normalized complex. The sign of its degree-two differential depends on convention, but the coefficient's absolute value and resulting \(\mathbb Z/2\) do not.

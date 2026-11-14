# All-prime Legendre compatibility: the exact remaining finite-ramification step

Status: source audit and failed-route analysis. No finite-ramification theorem for an arbitrary noncuspidal section is claimed. The conditional residual-level reformulation below is proved, but does not supply its boundedness hypothesis. This note does not modify D.30 or D.31.

## 1. The question actually left by D.30

For a noncuspidal section of the rational tripod, D.6 and D.25 supply local ordinary or cuspidal sections and ordinary integral points on a density-one set of rational primes. D.30 proves absolute irreducibility of every Legendre coefficient representation, its potentially semistable coefficient-prime behavior, and the following equivalence:

\[
\begin{split}
&\text{one coefficient representation, for }\ell\ge5,\text{ is finitely ramified}\\
&\quad\Longleftrightarrow
\text{the local points are ordinary integral outside a finite set}\\
&\quad\Longleftrightarrow
\text{all coefficient representations have a common finite ramification set.}
\end{split}
\]

The additional hypothesis under investigation was agreement of all local rational Weil–Deligne parameters, across every coefficient prime, together with the known local point-or-cusp constraints. This is stronger than density-one agreement of characteristic polynomials. It is **not** automatic for arbitrary cuspidal splittings: D.30's \(e_5\kappa(13)\) example has zero monodromy at coefficient prime seven and nonzero monodromy at coefficient prime five.

Even if all local Weil–Deligne parameters are assumed to agree, none of the opened results below derives the first line of the displayed equivalence. Calling such a family a “strictly compatible system” without specifying the convention risks inserting finite ramification into the definition. Here “all-prime Weil–Deligne agreement” means only the local comparison assertion; finite support remains a separate question.

## 2. Exact primary-source boundaries

The following passages were opened directly on 14 November 2026.

| Primary source | Exact passage | What it supplies, and the remaining hypothesis |
|---|---|---|
| Helm and Voloch (2011), author PDF | Section 4, Theorem 4 and Proposition 6, author pp.5–7 | Starts with one **finite** set \(S\) and local elliptic curves with good reduction at every \(p\notin S\). The proof first bounds Serre weights and levels for infinitely many coefficient primes. Its uniform level bound uses support in \(S\); the finite-dimensional space of weight-two forms then supplies a repeated eigenform. |
| Pan (2021 author version; 2022 journal publication) | Conjecture 1.0.1, p.2, incorporated in Theorem 1.0.4, p.5 | Gives regular two-dimensional Fontaine–Mazur modularity for \(\ell\ge5\), retaining the explicit finite-ramification hypothesis. The distinct Hodge–Tate weights do not replace that hypothesis. |
| Khare, Larsen, and Ramakrishna (2003 author preprint) | Section 2.4, pp.23–24, especially the paragraph immediately before Corollary 14 | Constructs a **pair** of coefficient-prime lifts with common integral pure Frobenius polynomials on a density-one set. The paragraph explicitly declines matching ramified Weil–Deligne parameters. It does not construct an all-prime, everywhere-WD-compatible, section-realized system. |
| Khare and Rajan (2000 author preprint) | Theorem 1, p.1 | Semisimple finite-dimensional coefficient representations have ramification of density zero. This does not give finite support. |
| Lu and Zheng (2019 author version) | Introduction, Theorem 1.2 and Corollary 1.3, pp.1–2 | Concerns compatible sheaves on a scheme of finite type over a fixed henselian local trait, and their boundary behavior after stratification. It is not a theorem making an arbitrary representation of \(G_{\mathbf Q}\) lisse over some open subscheme of \(\operatorname{Spec}\mathbf Z\). |
| Das and Sarkar (2023 author version) | Definition 3.1, p.4; Section 6 | Their \(m\)-compatible systems permit finite inertia outside a finite \(m\)-ramification set. The finite-order inertia hypothesis excludes the nonzero unipotent monodromy relevant here. It supplies no uniform support bound for that monodromy. |

For Helm–Voloch the explicit bound in Proposition 6 has the shape
\[
N=2^{14}3^5\prod_{\substack{p\in S\\p\ne2,3}}p^2
\]
after restricting the coefficient primes to appropriate congruence classes. The essential point is that \(N\) is fixed. If the exceptional primes move with the coefficient prime or its precision, the argument has no finite-dimensional space in which to apply the repeated-eigenform step.

This source audit neither extrapolates KLR's pair construction to all primes nor treats the absence of an identified theorem as a proof of impossibility.

## 3. A precise conditional reformulation by residual levels

There is a useful exact reformulation of the missing boundedness. Let \(\mathcal P\) be the density-one set where the section is an ordinary integral point section. For \(\ell\in\mathcal P\), let \(\bar\rho_\ell\) denote the actual mod-\(\ell\) Legendre representation. Let \(N_\ell\) be its prime-to-\(\ell\) Artin conductor. This is finite for every individual \(\ell\), because \(\bar\rho_\ell\) has finite continuous image.

**Conditional residual-level criterion.** The conditions in D.30 are equivalent to the existence of an infinite set of coefficient primes \(\Lambda\subset\mathcal P\), all at least five, and an integer \(N\ge1\) such that
\[
                         N_\ell\mid N\qquad(\ell\in\Lambda).
                         \tag{1}
\]

Here is the complete argument for the direction requiring explanation. Discard the finitely many \(\ell\) dividing \(N\). At \(\ell\in\Lambda\), the local representation is the \(\ell\)-torsion of an elliptic curve with good reduction over \(\mathbf Q_\ell\), hence finite flat. For an irreducible residual representation the optimal Serre weight is therefore two, as in Helm–Voloch's proof.

First there can be only finitely many reducible \(\bar\rho_\ell\) in \(\Lambda\). If it is reducible, its semisimplification is
\[
                       \psi_\ell\oplus\bar\chi_\ell\psi_\ell^{-1}.
\]
For clarity, the local assertion here uses the actual good elliptic curve. If its reduction is supersingular, its mod-\(\ell\) representation over \(\mathbf Q_\ell\) is locally absolutely irreducible: the two distinct fundamental inertia characters of level two are exchanged by Frobenius. Thus global absolute reducibility forces ordinary good reduction. In that case the two inertia characters are \(1\) and \(\bar\chi_\ell\), including after extending the coefficient field. After exchanging the two global characters, write \(\psi_\ell=\varepsilon_\ell\), with \(\varepsilon_\ell\) unramified at \(\ell\). Its finite global character has conductor dividing \(N\): its conductor is at most the conductor of the residual representation, and it is unramified at \(\ell\). By class field theory over \(\mathbf Q\), it is a Dirichlet character modulo \(N\).

Choose once and for all a prime \(p\in\mathcal P\), \(p\nmid N\), with \(p\equiv1\pmod N\). Such a prime exists because the congruence class has positive density whereas the complement of \(\mathcal P\) has density zero. At this fixed prime, for every reducible \(\bar\rho_\ell\), \(\ell\ne p\),
\[
                   a_p\equiv1+p\pmod\ell,
\]
where \(a_p\in\mathbf Z\) is the trace of the actual good elliptic curve at \(p\). If infinitely many coefficient primes were reducible, this would give \(a_p=1+p\), contradicting \(|a_p|\le2\sqrt p\). Thus an infinite subset of \(\Lambda\) is absolutely irreducible. Over a finite field, a reducible representation after scalar extension still has characters over a finite extension; the same Dirichlet-character and trace argument applies, so the conclusion is absolute irreducibility.

Serre modularity now supplies weight-two newforms of level dividing \(N\), with the determinant prescribed by \(\bar\chi_\ell\). There are only finitely many such eigensystems and coefficient embeddings up to their finite coefficient fields. One eigensystem therefore occurs for infinitely many distinct residue characteristics. At every fixed \(p\in\mathcal P\), \(p\nmid N\), its coefficient is congruent to the fixed integer \(a_p\) at infinitely many primes of its coefficient field. Their difference, an algebraic integer, must be zero. The newform and each original coefficient representation consequently have the same trace and determinant on a density-one set. Chebotarev and semisimplicity identify their rational representations. In particular one coefficient representation is finitely ramified, so D.30 applies.

Conversely, under D.30 the system is the rational Tate-module system of one elliptic curve \(E/\mathbf Q\). For any stable lattice, reduction modulo \(\ell\) cannot increase its Artin conductor at a place \(v\ne\ell\): reduction injects the reduction of the saturated inertia-invariant lattice into residual invariants, and the higher wild-inertia invariants are computed by averaging in finite groups of order prime to \(\ell\). Thus the prime-to-\(\ell\) residual conductor divides the conductor of \(E\), independently of the chosen integral Legendre lattice. The cofinite set of good coefficient primes supplies \(\Lambda\), proving (1).

The criterion isolates a concrete missing uniform statement. Continuity gives a finite \(N_\ell\) for each \(\ell\), but has not been shown to give one \(N\) for an infinite subset of good coefficient primes. All-prime rational Weil–Deligne agreement supplies no such bound by itself.

## 4. Why rational monodromy agreement does not bound thickness

At a split multiplicative place \(v\ne\ell\), an integral Tate basis gives
\[
\rho_\ell(\tau)=
\begin{pmatrix}1&m_vt_\ell(\tau)\\0&1\end{pmatrix},
\qquad
m_v=v(q_v)\in\mathbf Z_{>0}.
\tag{2}
\]
The integer \(m_v\) is intrinsic to the integral Tate lattice. Modulo \(\ell^a\), inertia is trivial exactly when \(\ell^a\mid m_v\). Over \(\mathbf Q_\ell\), however, every nonzero multiple of the standard rank-one nilpotent operator is conjugate to every other by a diagonal matrix. Rational Weil–Deligne isomorphism therefore distinguishes \(m_v=0\) from \(m_v\ne0\), but not the positive integer \(m_v\), nor its divisibility.

For distinct primes \(q_i\), the sequence
\[
                              m_{q_i}=i!
                              \tag{3}
\]
has finite nonzero support modulo every integer, while all its entries are positive integers. For each fixed \(M\), every \(i\ge M\) has \(M\mid i!\). Thus (3) satisfies exactly the finite-level support restriction imposed by adelic continuity; it gives no finite support in characteristic zero.

This is a statement about the weakness of the proposed deduction. It does not assert that an arbitrary such assignment comes from an absolutely irreducible global section system. Neither the Hasse trace constraints nor the full nonabelian section conditions have been discarded in the actual open problem.

## 5. An actual cuspidal boundary example, with its precise excluded hypotheses

The numerical warning can be realized by a genuine **cuspidal** global section, so it is not merely a collection of unrelated local matrices. It still is not a counterexample for D.30's noncuspidal sections.

Choose an infinite sparse sequence of odd primes \(q_i\), for example recursively with \(q_i>2^{i^2}\). Define
\[
                     A=\lim_{r\longrightarrow\infty}
                             \prod_{i=1}^{r}q_i^{i!}
                     \quad\text{in }\widehat{\mathbf Q^\times}.
                     \tag{4}
\]
For each exponent \(M\), the images of the partial products in \(\mathbf Q^\times/(\mathbf Q^\times)^M\) are eventually constant, since every sufficiently late \(i!\) is divisible by \(M\). The resulting classes are compatible in \(M\). Kummer theory therefore gives a continuous class in \(H^1(\mathbf Q,\widehat{\mathbf Z}(1))\). Twist the tangent-one splitting at the rational cusp \(t=0\) by this class.

At every finite place \(v\), the valuation of the localized class is an ordinary integer: \(i!\) at \(v=q_i\), and zero elsewhere. The unit part belongs to the compact unit group of \(\mathbf Q_v\), whose Kummer completion is itself. Thus these local cusp splittings even have actual local tangent coefficients, though the global class (4) does not come from \(\mathbf Q^\times\), because its valuations have infinite support.

The Legendre Tate parameter at that cusp is
\[
                        q(t)=t^2u(t),\qquad u(0)=1/256.
\]
After the fixed quadratic splitting twist, the resulting local Tate extension class is the class of \(A^2/256\). At \(q_i\), its monodromy thickness is \(2i!\); at an odd \(v\notin\{q_i\}\), it is zero. Therefore every coefficient-prime representation is ramified at infinitely many \(q_i\), while every finite adelic quotient is ramified at only finitely many of them.

At every \(v\ne\ell\), the rational Weil–Deligne parameter is nevertheless defined over \(\mathbf Q\) and agrees across all coefficient primes: its semisimple Frobenius eigenvalues are the fixed quadratic twist of \(1,v\), and its nilpotent operator is zero or nonzero according to the same set of places. At two, the fixed leading coefficient and the fixed quadratic twist still give a common rational parameter. At its coefficient prime, the representation is potentially semistable because it is, after that quadratic twist, an extension of \(\mathbf Q_\ell\) by \(\mathbf Q_\ell(1)\), the specific case covered by Berger.

This example is globally reducible and fails the density-one elliptic Hasse bound: on the density-one unramified set its trace has absolute value \(v+1\). It therefore fails two essential hypotheses already proved for a noncuspidal section. It is included only to show that adelic continuity, actual local tangent coefficients, coefficient-prime potential semistability, and all-prime rational Weil–Deligne agreement do not alone control support.

## 6. What remains unsupplied

No argument in the inspected sources or in this audit establishes (1) for the given noncuspidal section. A proof would have to exploit additional global information beyond rational local monodromy agreement. Examples of a sufficient new input are a uniform residual Serre-level bound on infinitely many good coefficient primes, or a direct common finite-support theorem for the corresponding integral monodromy.

Even after such an input, the finite-cusp issue in D.31 remains: cofinite integrality alone still allows finitely many cuspidal local sections. No invocation of Stix's ordinary-local-point theorem is made without resolving that separate hypothesis.

## References and exact access notes

- Das, P., & Sarkar, S. (2023). *A base change version of Rasmussen–Tamagawa conjecture* (arXiv:2208.04170v3). Definition 3.1, p.4. https://arxiv.org/pdf/2208.04170
- Helm, D., & Voloch, J. F. (2011). Finite descent obstruction on curves and modularity. *Bulletin of the London Mathematical Society, 43*(4), 805–810. https://doi.org/10.1112/blms/bdr015. Opened author text: https://web.ma.utexas.edu/users/voloch/Preprints/modularity.pdf, Section 4, author pp.5–7. Local text: tmp/D_HelmVoloch2011.txt.
- Khare, C., Larsen, M., & Ramakrishna, R. (2003). *Constructing semisimple p-adic Galois representations with prescribed properties* (arXiv:math/0309283v1). Section 2.4, pp.23–24. https://arxiv.org/pdf/math/0309283. The precise scope here is attributed to this opened author version; the final 2005 publisher PDF was not opened in this audit.
- Khare, C., & Rajan, C. S. (2000). *The density of ramified primes in semisimple p-adic Galois representations* (arXiv:math/0011272). Theorem 1, p.1. https://arxiv.org/pdf/math/0011272
- Lu, Q., & Zheng, W. (2019). Compatible systems and ramification. *Compositio Mathematica, 155*(12), 2334–2353. https://doi.org/10.1112/S0010437X19007619. Opened author version: https://arxiv.org/pdf/1801.03221, Theorem 1.2 and Corollary 1.3, pp.1–2.
- Pan, L. (2022). The Fontaine–Mazur conjecture in the residually reducible case. *Journal of the American Mathematical Society, 35*(4), 1031–1169. https://doi.org/10.1090/jams/991. Opened author version arXiv:1901.07166v2, Conjecture 1.0.1, p.2, and Theorem 1.0.4, p.5: https://arxiv.org/pdf/1901.07166
- Berger's exact extension calculation and the cusp leading-term computation are the already opened sources and elementary calculation recorded in D.30 and audit/D_legendre_modularity_degeneration_review.md.

Search scope included exact phrases involving all-prime, adelic, strictly compatible, infinitely ramified, and finite ramification; the above primary sources were inspected at the cited statements. No novelty inference is drawn from the search result.

## Root review of this audit

On 14 November 2026 the root read the full audit, including the conditional residual-level equivalence and the factorial cuspidal example. The level argument uses one fixed bound on infinitely many good coefficient primes; it does not obtain that bound from continuity. The fixed congruence-class prime excludes infinitely many reducible residual representations by the elliptic Hasse bound, after which finite-dimensional weight-two modularity supplies one repeated eigensystem. The explicit cuspidal example remains globally reducible and fails the density-one elliptic trace bound, so it is not a counterexample to the noncuspidal assertion. The distinction from D.31 is retained: arbitrary completed cusp tangents need not be actual local multiplicative values, which is why a unit vanishing to order zero at every relevant cusp is a substantive additional hypothesis. No promotion of the unresolved finite-ramification or mixed-cusp claims is justified by this audit.

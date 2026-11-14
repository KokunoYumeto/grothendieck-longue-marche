# Independent adversarial review of the finite-prime theta candidate

**Reviewer:** topos. **Reviewed file:** `audit/A_finite_prime_theta_candidate.md`, proposed A.C2.14. **Conclusion:** the stated construction and its stated limitation of the abelian-cover strategy pass this review. No proof of A1 or counterexample to A1 is inferred. The two scope clarifications at the end should be retained.

## 1. Mixed-primary orbit argument

Let the finite set of odd primes be \(S\), and suppose the chosen Frobenius power (sigma) fixes \(J[\ell]\) for every \(\ell\in S\). On each finite \(\ell\)-primary torsion module its image lies in the congruence kernel, an \(\ell\)-group. Thus the orbit length of any \(S\)-primary torsion point has no prime factors outside \(S\).

If the orbit length is \(n>1\), choosing \(\ell\mid n\) and \(\tau=\sigma^{n/\ell}\) really does give an orbit of exact length \(\ell\). For \(r\ne\ell\), the orbit of the \(r\)-primary component under \(\tau\) has both \(r\)-power order and order dividing \(\ell\), so that component is fixed. The difference \(T=\tau\eta-\eta\) is therefore purely \(\ell\)-primary and nonzero. This is the necessary reduction; it does not assume that the original mixed torsion point is itself \(\ell\)-primary.

Writing \(\tau=1+\ell M\), the displayed operator \(U=(1+\tau+\cdots+\tau^{\ell-1})/\ell\) is integral and congruent to (1) modulo \(\ell\). For the last binomial term the coefficient is \(\ell^{\ell-2}\), which remains divisible by \(\ell\) when \(\ell=3\); the preceding coefficients are likewise divisible. The equality \(\ell UT=0\) therefore implies \(\ell T=0\). Since \(\tau\) fixes \(J[\ell]\), the orbit is the affine line \(eta+iT\). It lies in both theta translates. Their stabilizer is trivial because the polarization is principal, and the intersection number (2) excludes \(\ell\ge3\) distinct intersection points. This portion has no scalar-Frobenius or semisimplicity assumption.

The later derivative condition \(\pi-1=\ell A_\ell\), with \(A_\ell\) invertible over \(\mathbf Z_\ell\), gives precisely \(J(k)[\ell^\infty]=J[\ell]\). Combined with the orbit lemma, avoidance at squarefree level \(L\) consequently implies avoidance at every \(S\)-primary order.

## 2. The finite-level avoidance open

The condition is open because the bad locus is closed on the finite étale relative \(L\)-torsion scheme and its finite projection is closed. The (0)-section is excluded exactly on the ordinary locus. Yang's Proposition 1.3 asserts strong new ordinariness at the geometric generic moduli point. Its displayed proof uses the ordinary elliptic chain. This is the needed generic finite-level assertion and does not require the problematic composite-order primitive-character formulation elsewhere in that paper.

The optional compact-type argument also survives a direct check. For two ordinary elliptic components meeting once, the normalization sequence gives the following Frobenius-compatible descriptions for a multidegree-zero odd torsion line bundle \(\mathcal L\):

- both restrictions nontrivial: \(H^1(\mathcal L)\) is the one-dimensional node term;
- exactly one restriction trivial: it is \(H^1(\mathcal O)\) on that ordinary elliptic component;
- both trivial: \(\mathcal L\) is trivial, since the dual graph is a tree, and \(H^1\) is the sum of the two ordinary elliptic cohomology spaces.

Squaring preserves which restrictions are nontrivial. In the first case the Frobenius on the node fibre is a nonzero scalar times the scalar-field Frobenius, hence bijective; the other cases use elliptic ordinariness.

For a detailed smoothing proof, one can choose a smooth marked section and a strictly henselian characteristic-two DVR smoothing of this compact-type curve. Its relative \(\operatorname{Pic}^0\) is an abelian scheme, its \(L\)-torsion is finite étale and constant, and the section supplies rigidified Poincaré line bundles. Nonzero torsion sections stay nonzero on the special fibre. For such a bundle, \(h^0=0\) and \(h^1=1\) on the special and generic fibres; for the trivial bundle \(h^1=2\). Cohomology and base change therefore gives vector bundles of constant rank. The Frobenius-linearized map to the squared-bundle cohomology is an isomorphism on the special fibre and hence has invertible determinant over the DVR. This justifies the finite simultaneous avoidance after smoothing. No theta line bundle on the singular fibre is required.

## 3. Composite-level connectedness and rigidification

The opened Deligne–Mumford Theorem 5.15 concerns the complete level \(N\) over its cyclotomic base; it is not merely separate prime-by-prime monodromy. The preceding definition (5.14) supplies a scheme for \(N\ge3\). Since the level is invertible and the smooth-curve moduli stack is smooth, its fixed-multiplier level scheme is smooth. Geometric connectedness then implies geometric irreducibility: a regular noetherian scheme has disjoint open irreducible components. Its restriction to the nonempty avoidance open remains geometrically irreducible.

The tricanonical frame space is important. On a genus-two coarse level space, the hyperelliptic involution can identify a basis with its negative; one should not silently use a free full symplectic action there. Here \(T\to U\) is the frame torsor for \(H^0(\omega^3)\), with fibre \(\mathrm{GL}_5\). The frame kills all curve automorphisms, even in characteristic two because the tricanonical system is very ample. Achter–Pries §5.1 gives representability and the relevant connected-fibre/fundamental-group assertion.

The scheme \(Y=T\times_U U[N]\) is the actual symplectic-basis torsor of the universal Jacobian over \(T\), so its full \(mathrm{Sp}_4(\mathbf Z/N)\) action is free. Viewed instead over (U[N]), it is the frame torsor of the universal curve, with geometrically connected \(mathrm{GL}_5\) fibres. Thus \(Y\) is geometrically irreducible. These two descriptions resolve both the arithmetic basis bookkeeping and the possible hidden central quotient. No Goursat independence step is missing.

## 4. Twist, field degree, and first derivative

For each \(\ell\), the prescribed diagonal \(g_\ell\) is symplectic, has exact order \(\ell\), and has invertible derivative (operatorname{diag}(1,1,-1,-1)) modulo \(\ell\). Chinese remaindering gives an element of order \(L\). After choosing the finite field to contain \(mu_N\), the symplectic group and its deck action are constant. Right translation by the cyclic powers of \(g^{-1}\) defines an effective finite descent datum. Although right translations in a noncommutative group require an order convention, the cyclic powers involved here commute and give the displayed cocycle and fixed-point equation with a consistent convention.

The twist stays geometrically irreducible. The opened Lang–Weil statement gives points for every sufficiently large extension degree, so the infinite progression \(m\equiv1\pmod L\) is legitimate. The resulting basis satisfies \(operatorname{Frob}_{k_0}^m(y)=yg\). Its projection is an actual framed curve over \(k_0^m\), and hence gives the asserted matrix on its \(N\)-torsion. Using the inverse Frobenius convention replaces \(g\) by \(g^{-1}\) and preserves derivative invertibility. The pairing multiplier is compatible because \(|k_0|\equiv1\pmod N\).

The matrix modulo \(\ell^2\) is enough: on the full Tate module (pi-1) is divisible by \(\ell\), and its quotient has the invertible reduction just prescribed. No higher-level Frobenius control is being assumed.

## 5. Every abelian cover in the stated class

For a connected finite étale abelian odd-order cover \(D\to C\), the direct-image algebra splits over the algebraic closure into its distinct character line bundles. Every nontrivial character line bundle has nonzero \(H^1\) of dimension \(g(C)-1=1\). Theta avoidance makes all the Frobenius arrows between the character spaces invertible. The invariant summand is ordinary because \(C\) is, so \(D\) is ordinary.

For completeness, faithfulness follows already modulo (2). Artin–Schreier identifies \(H^1_{\mathrm{et}}(D,\mathbf F_2)\) with the fixed space of the bijective semilinear Frobenius on \(H^1(D,\mathcal O_D)\); after scalar extension to the algebraic closure this recovers the latter space, equivariantly for deck transformations. Every nontrivial character occurs there. These characters separate the odd-order abelian deck group, so its action is faithful on \(H^1_{\mathrm{et}}(D,\mathbf F_2)\), equivalently on the dual geometric Jacobian (2)-torsion, and hence on full geometric (2)-primary torsion.

An abelian quotient of an ordinary Jacobian is ordinary, by additivity of dimension and \(p\)-rank under an isogeny splitting. A nonconstant map to an abelian variety generates a positive-dimensional image of that Jacobian, which cannot sit in a (2)-rank-zero target. This is exactly the asserted obstruction to those particular mechanisms.

## Scope to preserve

“The abelian \(S\)-tower” means covers whose composite deck group over the original \(C\) is abelian. It does not mean arbitrary iterated abelian covers with a nonabelian total group. The candidate's final paragraph already excludes such nonabelian covers, and that qualification should remain conspicuous.

The curve and finite field depend on \(S\). Neither a single curve avoiding every odd order nor any collision of point sections is proved. Subject to these stated scopes, no mathematical gap was found.

## Primary sources independently opened in this review

- Deligne, P., & Mumford, D. (1969). *The irreducibility of the space of curves of given genus*. Publications Mathématiques de l'IHÉS, 36, 75–109. Definition 5.14 and Theorem 5.15, pp. 108–109. https://www.numdam.org/item/PMIHES_1969__36__75_0.pdf
- Achter, J. D., & Pries, R. (2008). *Monodromy of the p-rank strata of the moduli space of curves*. International Mathematics Research Notices, rnn053. §5.1 and Lemma 5.2, pp. 17–18. https://www.math.colostate.edu/~achter/math/prm0508.pdf
- Yang, Y. (2016). *Abelian coverings of curves over Fp which are not new ordinary*. RIMS-1844. Definition 1.2 and Proposition 1.3 with its proof, pp. 2–3. https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1844.pdf
- Poonen, B. (2017). *Rational points on varieties*. Graduate Studies in Mathematics, 186. Theorem 7.7.1(ii)–(iii), p. 222. https://math.mit.edu/~poonen/papers/Qpoints.pdf

## Addendum: explicit compact-type extension now inserted

The revised candidate replaces the implicit relative-Picard extension with an explicit finite étale torsor argument. I read that revision and independently opened Stacks Project Lemma 58.9.1, tag0A48, including its proof: https://stacks.math.columbia.edu/tag/0A48. Its hypotheses exactly cover the projective smoothing over the complete local ring. The equivalence extends each finite étale mu_L torsor, and full faithfulness extends the action and its torsor identity. The associated character line is therefore genuinely L-torsion on the entire surface.

The new injectivity argument is also correct. A geometric generic trivialization implies an ordinary generic one because H0 commutes with field extension and a nonzero section of a degree-zero line on the smooth generic curve has no zeros. On the regular surface its extension divisor is vertical, hence aE1+bE2. The two multidegrees are b−a and a−b. Since a torsion line has degree zero on each component, a=b, and the divisor is a multiple of the principal total fibre. Thus the special class was trivial. This supplies L^4 distinct geometric generic classes, exhausting the genus-two L-torsion. The subsequent constant-rank cohomology and Frobenius determinant argument is valid. No issue was found in this more explicit replacement.

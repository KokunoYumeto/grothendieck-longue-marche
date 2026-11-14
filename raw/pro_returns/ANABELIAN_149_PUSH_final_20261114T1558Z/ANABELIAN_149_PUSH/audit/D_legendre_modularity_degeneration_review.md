# Independent review of the Legendre finite-ramification criterion

Reviewer: degeneration agent. Reviewed file: audit/D_legendre_modularity_candidate.md, Sections 1–8, with particular attention to Sections 2–6. The reviewed statement is proposed D.30. This review does not assert finite ramification, eliminate the remaining finite cuspidal set, or prove the global section conjecture.

## Verdict and exact scope

The current candidate's main equivalence passes:

\[
\begin{gathered}
\text{finite ramification of one }\rho_{s,\ell},\quad\ell\ge5,\\
\Longleftrightarrow\quad
\text{ordinary integral local point sections outside a finite set},\\
\Longleftrightarrow\quad
\text{a common finite ramification set for the rational Tate system}.
\end{gathered}
\]

The unconditional absolute irreducibility argument and the conditional common elliptic realization also pass. This is conditional on the already integrated D.6 local classification and D.25 density-one theorem. Neither of those is silently strengthened here.

There is a necessary boundary to the conclusion. Cofinite integrality allows finitely many cuspidal local sections. The exact sufficient hypothesis of D.5 and Stix's Corollary 6 includes ordinary local points at every finite place. Thus finite ramification alone has not been shown equivalent to an actual rational point section. The candidate explicitly retains this distinction.

## 1. Coefficient-prime local representations

For an ordinary local point the representation is the actual Tate module of an elliptic curve over \(\mathbf Q_\ell\), so potential semistability and weights \(0,-1\) are the proper-smooth comparison inputs.

At a cusp the Legendre representation is potentially multiplicative. Its restriction to a cusp decomposition group becomes an extension of \(\mathbf Q_\ell\) by \(\mathbf Q_\ell(1)\) after a finite quadratic twist. Pullback along an arbitrary continuous cuspidal splitting produces an arbitrary class of \(H^1(\mathbf Q_\ell,\mathbf Q_\ell(1))\). It need not arise from an ordinary rational tangent.

Berger's opened Section II.4.4 explicitly establishes semistability for every such class: the logarithmic period is in \(B_{\mathrm{st}}\), and the unit classes lie in the crystalline subspace. The split extension is included. A finite quadratic twist preserves potential semistability and these weights. The infinity cusp's possible quadratic semisimple monodromy is therefore accounted for.

## 2. The global character lemma

The argument works over every finite coefficient extension \(E/\mathbf Q_\ell\); it does not assume that an invariant line is defined over \(\mathbf Q_\ell\).

The compact image of a continuous \(E^\times\)-valued character lies in \(\mathcal O_E^\times\). A fixed positive power lands in a torsion-free pro-\(\ell\) subgroup. Under Kronecker–Weber, each factor \(\mathbf Z_q^\times\), \(q\ne\ell\), maps trivially to that subgroup: its finite part has torsion image and its pro-\(q\) part has simultaneously pro-\(q\) and pro-\(\ell\) image. Finite-support elements are dense in the product, so all factors away from \(\ell\) are killed together.

For the remaining local character, the underlying \(\mathbf Q_\ell\)-representation is abelian and semisimple on inertia: multiplication by a characteristic-zero field is simultaneously diagonalizable after scalar extension. Serre's exact Theorem 3 therefore gives local algebraicity. The resulting \(\mathbf Q_\ell\)-defined cocharacter centralizes multiplication by \(E\), since this holds on an open, hence Zariski-dense, subgroup of \(\mathbf Z_\ell^\times\). It factors through \(\operatorname{Res}_{E/\mathbf Q_\ell}\mathbf G_m\). The coefficient embeddings form one Galois orbit, so an invariant cocharacter has one integer exponent. Removing that cyclotomic power leaves a finite character.

No finite-ramification hypothesis on the original two-dimensional representation enters this lemma.

## 3. Absolute irreducibility

An invariant line over \(\overline{\mathbf Q}_\ell\) is defined over a finite coefficient field. The line and quotient inherit Hodge–Tate structures. The two integer cyclotomic exponents must be \(0,1\), and the determinant makes their finite characters inverse. Thus the semisimplification would be

\[
\eta\oplus\eta^{-1}\chi_\ell.
\]

The primes splitting completely in the finite extension killing \(\eta\) have positive density. Their intersection with D.25's density-one set of ordinary integral local points is nonempty away from \(\ell\). At such a prime \(v\), the alleged trace \(1+v\) contradicts the Hasse bound \(2\sqrt v\) for the actual good elliptic fibre. This establishes absolute irreducibility for every coefficient prime.

## 4. Modularity and cofinite integrality

Pan's Theorem 1.0.4 incorporates all hypotheses of Conjecture 1.0.1, including finite ramification. The candidate states and uses this hypothesis. For \(\ell\ge5\), no residual-representation exception remains in that theorem. Oddness comes from the cyclotomic determinant; local potential semistability and distinct weights were checked above.

The weights and determinant normalize the modular form to weight two and trivial nebentype. Outside its finite level and the coefficient prime, its Frobenius trace has the weight-one bound.

At an ordinary local point, unramifiedness gives good reduction by Néron–Ogg–Shafarevich. For the Legendre \(j\)-function, an odd-place parameter outside \(U(\mathbf Z_v)\) has negative \(j\)-valuation, so cannot have good reduction.

At a cuspidal local point the two semisimple characters are \(\delta_v\chi_\ell,\delta_v\), where \(\delta_v^2=1\). The whole representation being unramified forces \(\delta_v\) unramified. Its trace is then \(\pm(v+1)\), contradicting the modular purity bound. This reasoning also excludes a locally split cuspidal extension at these good places; it does not assume a nonzero unipotent inertia operator.

The converse follows from the smooth Legendre family over the integral tripod away from two, uniformly in the coefficient prime. These implications establish precisely cofinite integrality, with no conclusion at the finite excluded set.

## 5. Conditional common elliptic realization

For the supplied modular newform, the density-one integral places give rational integer eigenvalues. Comparing every coefficient conjugate by Chebotarev and Brauer–Nesbitt makes the good-prime eigensystems equal. Away-from-level newform multiplicity one then gives a rational Hecke field. Eichler–Shimura supplies an elliptic curve over \(\mathbf Q\), up to isogeny.

For every other coefficient prime, the corresponding rational Tate representation and the section representation have identical traces on the same density-one set. The latter is absolutely irreducible by the unconditional argument; semisimplicity and Chebotarev identify the rational representations. This does not identify local Legendre parameters, integral lattices, or the original nonabelian section.

## 6. Cuspidal warning example

The Section 8 example is correctly confined to global cuspidal sections. The continuous cocycle \(e_5\kappa(13)\) exists in the full profinite cusp-inertia module. At the cusp zero the horizontal Tate parameter has order two and leading coefficient \(1/256\). The tangent-one reference class is a unit at 13. The quadratic splitting twist is trivial over \(\mathbf Q_{13}\), because \(-1\) is a square there.

Consequently the added tame Kummer term is nonzero at coefficient prime five and zero at seven. Zero versus nonzero monodromy is invariant under rational representation isomorphism, although both semisimplified Frobenius polynomials are \((T-1)(T-13)\). This is a valid warning against inferring strict cross-prime compatibility from semisimple polynomials. It is not a noncuspidal counterexample.

The separate KLR version audit in Section 9 is outside the principal independent check recorded here. This review does not replace the author's explicit version-qualified source audit for that paragraph.

## Opened source record

- Serre, J.-P. (1989/1968). *Abelian l-adic representations and elliptic curves*. Chapter III, Appendix A.7, Theorem 3, printed III-52–53. The exact equivalence of local algebraicity with Hodge–Tate type plus semisimple inertia, and its reduction to an \(E\)-valued character, were read in full. https://www.math.mcgill.ca/darmon/courses/18-19/gs/serre-mcgill.pdf. Independent web opening: turn728view0 and turn729view0. Local text: tmp/D_Serre1989.txt, lines 6775–6845.
- Berger, L. (2002). *An introduction to the theory of p-adic representations*. Section II.4.4, pp.18–19. The entire Kummer-extension semistability paragraph was read. https://arxiv.org/pdf/math/0210184. Independent openings: turn728view1 and turn729view1. Local text: tmp/D_Berger2002.txt, lines 937–966.
- Pan, L. (2021 author version; 2022 publication). *The Fontaine–Mazur conjecture in the residually reducible case*. Conjecture 1.0.1, p.2, and Theorem 1.0.4, p.5, arXiv:1901.07166v2. Independent openings: turn728view2 and turn729view2. Both the finite-ramification hypothesis and the restriction only at coefficient prime three were read explicitly.
- Stix, J. (supplied arXiv:1203.3236v3). The definitions of ordinary integral/degenerate/cuspidal places and the full local representation table were read in the supplied TeX, lines 950–1092. Its boundary hypothesis is semistable; the present review separately checks the finite quadratic twist needed by the actual Legendre infinity cusp. D.5's stated use of Corollary 6 was also checked against the integrated manuscript.

No integrated source file or claim ledger was modified by this review.

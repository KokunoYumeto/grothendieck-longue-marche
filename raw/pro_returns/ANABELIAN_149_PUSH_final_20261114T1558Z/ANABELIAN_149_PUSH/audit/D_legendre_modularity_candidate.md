# A single finite-ramification hypothesis for the Legendre section system

Status: complete candidate for independent review, proposed D.30. The finite-ramification hypothesis is not proved. This candidate does not assert the global section conjecture.

## 1. Precise statement

Let \(U=\mathbf P^1_{\mathbf Q}\setminus\{0,1,\infty\}\), let
\[
\mathcal E/U:\quad y^2=x(x-1)(x-t),
\]
and let \(s:G_{\mathbf Q}\to\pi_1(U)\) be a continuous noncuspidal section. Put
\[
\rho_{s,\ell}:G_{\mathbf Q}\longrightarrow
 \operatorname{GL}(V_\ell(\mathcal E_{\bar\eta})).
\]
The determinant is \(\chi_\ell\). Use D.6 to attach to each finite place either an actual local point \(x_v\in U(\mathbf Q_v)\) or a local cuspidal section. D.25 makes the first alternative integral on a density-one set of places.

Then:

1. Every \(\rho_{s,\ell}\) is absolutely irreducible. This assertion requires no finite-ramification hypothesis.
2. The following are equivalent:
   - for at least one prime \(\ell\ge5\), the representation \(\rho_{s,\ell}\) is ramified at only finitely many rational primes;
   - the associated local sections are ordinary integral point sections at all but finitely many primes, namely \(x_v\in U(\mathbf Z_v)\) there;
   - there is one finite set \(S\) such that, for every coefficient prime \(\ell\), \(\rho_{s,\ell}\) is unramified at every \(v\notin S\cup\{\ell\}\).
3. Under these equivalent conditions, each representation with \(\ell\ge5\) is the representation of a weight-two cuspidal eigenform with trivial nebentype. In fact the system is the rational Tate-module system of an elliptic curve over \(\mathbf Q\), up to isomorphism of rational representations. The latter assertion does not identify the section with a rational point section.

The equivalence reduces cofinite integrality to finite ramification for one coefficient prime. It does not derive finite ramification from density-one integrality, from continuity, or from the local point/cusp classification. Cofinite integrality still permits finitely many cuspidal local sections. D.5 and Stix's Corollary 6 require ordinary local points at every finite place, so they cannot be applied here without another argument eliminating those remaining cuspidal places.

## 2. Every local representation at its coefficient prime is potentially semistable

Fix \(\ell\). If \(s_\ell\) is an ordinary point section, its representation is the Tate module of the actual elliptic curve \(\mathcal E_{x_\ell}/\mathbf Q_\ell\). It is potentially semistable and has Hodge–Tate weights \(0,-1\), using the convention that \(\mathbf Q_\ell(1)\) has weight \(-1\).

Suppose instead that \(s_\ell\) is cuspidal. This includes every continuous splitting of the cusp decomposition group, without requiring a rational tangent vector. The Legendre family has potentially multiplicative reduction at every cusp. After a quadratic twist, its representation on a cusp decomposition group has the form
\[
0\longrightarrow\mathbf Q_\ell(1)\longrightarrow V
 \longrightarrow\mathbf Q_\ell\longrightarrow0.
\]
Pulling this sequence back along an arbitrary local cuspidal splitting gives an arbitrary class in
\[
H^1(\mathbf Q_\ell,\mathbf Q_\ell(1)).
\]
Every such extension is semistable. Berger, Section II.4.4, pp.18–19, proves this using the Kummer description and the periods of a Tate curve; it also explains that the unit classes give the crystalline subspace. Undoing the finite quadratic twist gives potential semistability and the same two Hodge–Tate weights. The split extension is included.

This argument does not infer semistability of an arbitrary extension of arbitrary de Rham representations. It uses the specific pair \(\mathbf Q_\ell,\mathbf Q_\ell(1)\), for which all the extension classes are semistable.

At the cusp infinity the Legendre family has a quadratic semisimple monodromy part. It must not be silently treated as semistable before twisting. The argument above retains that finite twist.

## 3. A character lemma over \(\mathbf Q\), including coefficient extensions

Let \(E/\mathbf Q_\ell\) be finite and let
\[
\psi:G_{\mathbf Q}\longrightarrow E^\times
\]
be a continuous character whose restriction at \(\ell\) is Hodge–Tate. Then
\[
\psi=\eta\chi_\ell^a
\]
for an integer \(a\) and a finite-order character \(\eta\).

Here is the proof, with no finite-ramification assumption on \(\psi\).

By compactness the image of \(\psi\) lies in \(\mathcal O_E^\times\). Choose \(h\ge1\) such that the \(h\)-th power of that unit group lands in a torsion-free pro-\(\ell\) group of principal units. Kronecker–Weber identifies
\[
G_{\mathbf Q}^{\mathrm{ab}}\simeq\widehat{\mathbf Z}^{\,\times}
 =\prod_q\mathbf Z_q^\times.
\]
For \(q\ne\ell\), a continuous homomorphism from \(\mathbf Z_q^\times\) into a torsion-free pro-\(\ell\) group is trivial: its finite factor has torsion image, and its open pro-\(q\) subgroup has both pro-\(q\) and pro-\(\ell\) image. Hence \(\psi^h\) kills every \(q\ne\ell\) factor. The direct sum of those factors is dense in their product, so continuity shows that \(\psi^h\) factors through \(\mathbf Z_\ell^\times\).

Tate's local algebraicity theorem, in Serre, Chapter III, Appendix A.7, Theorem 3, printed pp.III-52–53, applies to the underlying \(\mathbf Q_\ell\)-representation of the \(E\)-line. Its inertia action is semisimple: it acts by multiplication by elements of a characteristic-zero field, so it is diagonalizable after scalar extension. Thus on an open subgroup of inertia the character is algebraic.

There is one base-field embedding because the local base is \(\mathbf Q_\ell\). More explicitly, the algebraic inertia action is a morphism
\[
\mathbf G_m/\mathbf Q_\ell\longrightarrow\operatorname{GL}_{\mathbf Q_\ell}(E).
\]
It centralizes multiplication by \(E\), since this holds on the Zariski-dense open subgroup of \(\mathbf Z_\ell^\times\). It therefore factors through
\[
\operatorname{Res}_{E/\mathbf Q_\ell}\mathbf G_m.
\]
Every cocharacter of this restriction-of-scalars torus defined over \(\mathbf Q_\ell\) has the same integer exponent at all coefficient embeddings, since those embeddings form one Galois orbit. It is consequently \(u\mapsto u^a\). Up to the harmless local-reciprocity inverse convention, \(\psi\chi_\ell^{-a}\) is trivial on an open subgroup of \(I_\ell\).

Set \(\eta=\psi\chi_\ell^{-a}\). After raising to an integer power as above, \(\eta\) factors through \(\mathbf Z_\ell^\times\) and is trivial on an open subgroup there. Its image is finite. A character whose \(h\)-th power has finite image itself has finite image, because the \(h\)-th power map on \(E^\times\) has finite fibres. Thus \(\eta\) has finite order. In particular it is ramified at only finitely many places, since its finite quotient is continuous.

This proof deals with characters that become visible only after a finite coefficient extension. It does not assume that a potentially reducible two-dimensional representation already has a \(\mathbf Q_\ell\)-rational invariant line.

## 4. Absolute irreducibility

Suppose that \(\rho_{s,\ell}\) is reducible over \(\overline{\mathbf Q}_\ell\). An invariant line is defined over a finite coefficient extension \(E/\mathbf Q_\ell\); its character and the quotient character are continuous \(E\)-valued characters. Hodge–Tate representations are closed under subobjects and quotients, and their Hodge–Tate multisets add in short exact sequences. Section 2 therefore shows that the characters have cyclotomic exponents zero and one. By Section 3, their semisimplification is
\[
\eta\oplus\eta^{-1}\chi_\ell
\]
after interchanging the characters, for a finite-order character \(\eta\); the inverse relation follows from the determinant.

Let \(F/\mathbf Q\) be the finite abelian extension killing \(\eta\). The primes splitting completely in \(F\) have positive density. By D.25, their intersection with the density-one set of ordinary integral local sections still has positive density, in particular it contains some prime \(v\ne\ell\). At every such prime,
\[
\operatorname{tr}\rho_{s,\ell}(\operatorname{Frob}_v)=1+v.
\]
On the other hand, that representation is the Tate module of the good reduction elliptic curve \(\mathcal E_{x_v}\), so its integral trace satisfies
\[
\bigl|\operatorname{tr}\rho_{s,\ell}(\operatorname{Frob}_v)\bigr|
 \le 2\sqrt v.
\]
These inequalities are incompatible, since \(v+1>2\sqrt v\) for every prime \(v\). Thus \(\rho_{s,\ell}\) is absolutely irreducible.

Only the characters, rather than the original two-dimensional representation, were shown finitely ramified in this proof.

## 5. The exact modularity input

Assume that \(\rho_{s,\ell}\) is finitely ramified for one \(\ell\ge5\). Its absolute irreducibility was proved in Section 4. It is odd because its determinant is cyclotomic. Section 2 proves potential semistability at \(\ell\) and distinct Hodge–Tate weights.

These are exactly the hypotheses of Pan's Theorem 1.0.4, with Conjecture 1.0.1 supplying the explicitly incorporated finite-ramification hypothesis. For \(\ell\ge5\), the theorem has no extra residual-representation hypothesis. The exceptional residual condition in its statement occurs at \(\ell=3\), which is why the present statement uses a coefficient prime at least five.

Consequently the representation comes from a cuspidal eigenform up to twist. The twisting character is a de Rham subobject of \(\operatorname{Hom}(V_f,\rho_{s,\ell})\), so Section 3 makes it finite order times a Tate twist. The two consecutive Hodge–Tate weights make its classical weight two after normalization; the Tate twist is zero in the convention for Tate modules used here. Absorb the finite character twist into the eigenform. The determinant \(\chi_\ell\) then makes the nebentype trivial. At every prime outside a fixed finite set containing the level and \(\ell\), the two Frobenius roots are Weil numbers of weight one. In particular their trace has complex absolute value at most \(2\sqrt v\).

The weight-one purity here is an output of modularity under finite ramification. It is not an additional assumption on the original section.

## 6. Why finite ramification gives cofinite integrality

Enlarge the finite exceptional set to include two, the coefficient prime, the ramified primes of \(\rho_{s,\ell}\), and the modular level. Let \(v\) lie outside it.

If \(s_v\) is an ordinary point section at \(x_v\), the representation is the Tate module of the actual elliptic curve \(\mathcal E_{x_v}/\mathbf Q_v\), and it is unramified. Néron–Ogg–Shafarevich gives good reduction.

For the Legendre parameter,
\[
j(t)=256\,\frac{(t^2-t+1)^3}{t^2(1-t)^2}.
\]
At an odd place, every nonintegral tripod value has \(v(j(t))<0\). Explicitly, if \(v(t)>0\) or \(v(1-t)>0\), the numerator is a unit and the denominator gives negative valuation. If \(v(t)<0\), the valuation is \(2v(t)<0\). Such an elliptic curve is not potentially good, contradicting good reduction. Thus the ordinary point belongs to \(U(\mathbf Z_v)\).

If \(s_v\) is cuspidal, its representation has the form
\[
\delta_v\otimes
\begin{pmatrix}\chi_\ell& *\\0&1\end{pmatrix}
\]
for a quadratic character \(\delta_v\). The character need not be unramified a priori, especially at the infinity cusp. However the whole representation is unramified at our chosen \(v\), and \(\chi_\ell\) is unramified there. Its diagonal entries force \(\delta_v\) to be unramified. The trace of Frobenius is therefore
\[
\delta_v(\operatorname{Frob}_v)(v+1)=\pm(v+1).
\]
This contradicts the modular weight-one purity bound. The argument includes locally split cuspidal extensions: it does not require a nonzero unipotent inertia operator.

All places outside the fixed finite exceptional set are consequently ordinary and integral.

Conversely, if the local sections are ordinary integral at every \(v\notin S\), the Legendre elliptic curve over \(\mathbf Z_v\) is smooth for every odd such \(v\). Its Tate representation is unramified at every coefficient prime different from \(v\). Enlarge \(S\) by two. This proves the common-finite-set assertion for the entire system, and hence also the one-prime finite-ramification assertion. All three conditions are equivalent.

The same integrality implication holds upstairs on a fixed finite étale cover of \(U\), after removing finitely many model primes: normalization over the integral base is finite, and a point above an integral point is integral. This is precisely the already checked finite-étale transfer in D.25–26, not a claim about arbitrary maps or twists.

## 7. Global elliptic realization, and its limit

Here are the additional standard modular arguments for the elliptic realization in Section 1.

Let \(f\) be the normalized newform supplied above. On the density-one integral set, its good-prime coefficient \(a_v(f)\) is the rational integer trace of \(\mathcal E_{x_v}\). For every embedding \(\tau\) of the Hecke field, the representations of \(f\) and \(f^\tau\), embedded into one algebraic closure of \(\mathbf Q_\ell\), have equal traces on this density-one set. Frobenius elements from a density-one set are dense in every finite Galois quotient by Chebotarev. Continuity and semisimplicity give equality of the two characters, hence equal good-prime coefficients everywhere. Newform multiplicity one, in the exact form of Stein, Theorem 9.4 and the paragraph following Example 9.5, then gives \(f^\tau=f\) and hence a rational Hecke field. Those statements say that distinct newform systems remain distinct for the Hecke algebra away from the level; the familiar Hecke recurrences recover its coprime composite indices from the good-prime eigenvalues and the nebentype.

The Eichler–Shimura construction for a rational weight-two eigenform with trivial nebentype gives an elliptic curve \(E/\mathbf Q\) with that rational Tate representation. The existence direction is stated explicitly in Milne, Modular Functions and Modular Forms, Proposition 11.21, p.117; only existence up to isogeny is needed, not a bijection on elliptic-curve isomorphism classes.

For any other coefficient prime \(r\), the representations \(V_r(E)\) and \(\rho_{s,r}\) have the same integer traces at the common density-one set of integral good primes. Section 4 gives absolute irreducibility of the latter; the former is semisimple. Chebotarev and Brauer–Nesbitt give
\[
\rho_{s,r}\simeq V_r(E).
\]
Thus the full rational system has one elliptic realization.

This does not prove that \(s\) is an actual point section. The linear Legendre representation is a quotient of the full geometric fundamental group, and the argument has not reconstructed the missing nonabelian data. It does not prove equality of the local parameters \(x_v\) with one rational parameter merely from equality of local Tate representations.

## 8. Why strict cross-prime monodromy is not automatic

There is a concrete warning even among genuine continuous sections, if cuspidal sections are allowed.

Let \(e_5\in\widehat{\mathbf Z}\) have component one in \(\mathbf Z_5\) and zero in every other primary component, and take the continuous Kummer cocycle \(e_5\kappa(13)\). Twist the standard tangent-one splitting at the rational cusp \(t=0\) by this cocycle. It is an actual continuous global cuspidal section of the cusp decomposition group, hence of \(\pi_1(U)\).

At the prime 13, the quadratic splitting character of the Legendre nodal cubic is trivial because \(-1\) is a square in \(\mathbf Q_{13}\). The formal Tate parameter at \(t=0\) is
\[
q(t)=t^2u(t),\qquad u(0)=1/256,
\]
as follows from \(q=j^{-1}+O(j^{-2})\) and the displayed Legendre \(j\)-function. The reference tangent-one section therefore gives an unramified extension class at 13, for coefficient primes different from 13.

Twisting changes the coefficient-\(r\) Kummer extension by \(2(e_5)_r\kappa_r(13)\). Thus the Weil–Deligne monodromy operator at 13 is nonzero for \(r=5\) and zero for \(r=7\), while the semisimplified Frobenius polynomial for both is
\[
(T-1)(T-13).
\]
The zero versus nonzero monodromy distinction is invariant under isomorphism. Therefore the family need not be strictly compatible at ramified places merely because its semisimple Frobenius polynomials match. This example is cuspidal and supplies no counterexample to the conjectural classification of noncuspidal global sections.

## 9. The finite-ramification barrier and the inspected KLR version

Khare–Rajan's theorem says that a continuous semisimple representation over a finite \(\ell\)-adic coefficient field has ramification of density zero. It does not say that this set is finite.

The inspected primary author preprint of Khare–Larsen–Ramakrishna, arXiv:math/0309283v1, explicitly permits \(k=1\) in its Main Theorem and in Corollary 14. The full proof in Section 2.2, pp.19–21, chooses newly prescribed prime traces only after the bound \(v>(\ell^m/2)^{2/k}\); that argument works for \(k=1\). Thus the phrase “\(k\) chosen suitably large” in the earlier sketch is not a restriction in that version's full proof. Section 2.4, pp.23–24, constructs density-one compatible pairs and explicitly distinguishes this from matching Weil–Deligne parameters at ramified primes. The paper constructs infinitely ramified lifts with potentially semistable coefficient-prime local behavior and integral pure good-prime polynomials.

The journal metadata is American Journal of Mathematics 127(4) (2005), 709–734, DOI 10.1353/ajm.2005.0026. The final publisher PDF has not yet been retrieved in this audit. Exact theorem numbers and the weight range above are attributed to the opened 2003 author preprint, not silently to an unopened final version.

These examples do not assert realization by sections of the tripod, nor do they prove a counterexample to the stronger combination of all section constraints. They explain why the listed representation-theoretic properties alone cannot be replaced by a finite-ramification assumption without an additional theorem.

The concrete remaining global assertion for this route is:
\[
\text{for a noncuspidal }s,\ \text{some }\rho_{s,\ell},
\quad \ell\ge5,\quad\text{has finite ramification.}
\]
No proof of that assertion is supplied here. The exact D.27–D.29 restricted-product and translated-evaluation obstructions remain separate.

## 10. Exact opened primary sources

- Berger, L. (2002). An introduction to the theory of p-adic representations. arXiv:math/0210184v1, Section II.4.4, pp.18–19. https://arxiv.org/pdf/math/0210184. Opened text includes the full Kummer-extension semistability computation. Local files: tmp/D_Berger2002.pdf and .txt.
- Serre, J.-P. (1989; original 1968). Abelian l-adic representations and elliptic curves. Addison-Wesley. Chapter III, Appendix A.7, Theorem 3, pp.III-52–53 (PDF pp.144–145), and the definition of local algebraicity in III.1.1. https://www.math.mcgill.ca/darmon/courses/18-19/gs/serre-mcgill.pdf. The opened proof explicitly passes to a finite coefficient field \(E\). Local files: tmp/D_Serre1989.pdf and .txt.
- Pan, L. (2022). The Fontaine–Mazur conjecture in the residually reducible case. Journal of the American Mathematical Society, 35(4), 1031–1169. https://doi.org/10.1090/jams/991. Opened primary author version arXiv:1901.07166v2, Conjecture 1.0.1, p.2, and Theorem 1.0.4, p.5: https://arxiv.org/pdf/1901.07166. Local files: tmp/D_Pan2021.pdf and .txt.
- Stix, J. (2015). Supplied primary source arXiv:1203.3236v3, subsections “Families of elliptic curves and l-adic representations” and “Almost an l-adic representation,” supplied TeX lines 967–1092. These explicitly separate the missing conductor from Frobenius integrality and compatibility. The local table there assumes semistable boundary reduction; Section 6 above retains the potentially multiplicative quadratic twist for the actual Legendre infinity cusp.
- Milne, J. S. (2017). Modular functions and modular forms (Version 1.31). Proposition 11.21, p.117, and the Eichler–Shimura discussion in Sections 10–11. https://www.jmilne.org/math/CourseNotes/MF.pdf. Opened existence statement for the elliptic curve attached to a rational weight-two newform. No reliance is placed on that proposition's overcompressed isomorphism-versus-isogeny wording.
- Stein, W. A. (2007). Modular forms: A computational approach. American Mathematical Society. Section 9.2, Theorem 9.4 and the paragraph following Example 9.5, printed pp.162–163; Section 10.2, pp.178–179. https://wstein.org/books/modform/stein-modform.pdf. Opened author PDF and author HTML version https://wstein.org/books/modform/modform/newforms.html. These give the exact away-from-level multiplicity-one statement and the modular abelian variety construction.
- Khare, C., & Rajan, C. S. (2000 author preprint). The density of ramified primes in semisimple p-adic Galois representations. Theorem 1, p.1, and Corollary 3, p.4. https://arxiv.org/pdf/math/0011272. The finite-ramification conclusion for abelian semisimple representations is stronger than its general density-zero conclusion.
- Khare, C., Larsen, M., & Ramakrishna, R. (2003 author preprint; journal publication 2005). Constructing semisimple p-adic Galois representations with prescribed properties. Main Theorem and proof, Section 2.2, pp.19–21; Section 2.4 and Corollary 14, pp.23–24. https://arxiv.org/pdf/math/0309283. Local files: tmp/D_KLR2003.pdf and .txt. The final publisher text remains not opened; the precise version qualification is retained.

Existing manuscript dependencies are D.6 and D.25. There is no use of an unproved global section conjecture, cofinite adelicity assumption, or universal cuspidal-lifting assertion.

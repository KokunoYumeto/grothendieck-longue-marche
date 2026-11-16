# Independent A54 proof and certificate audit

Auditor: `/root/de_sections`. Completed 15 November 2026, 18:38 UTC.

**PASS**, with the typographical missing-backslash repairs already requested from the author. I read the entire draft `notes/fgh_A54_draft.tex` and the full certificate, reran the certificate preserving its JSON, and independently derived the claimed Gaussian isogeny coordinate from the addition and duplication law. The executed calculation is retained as `code/de_A54_independent_audit.py` and `.out`.

## Actual cover and the same multiplicity factor

The divisor of psi5 has simple zero at each nonzero E[5] point and pole order24 at O. Thus the connected cyclic cover is degree5, totally ramified at25 points, of genus51. Translation lifting gives the actual central extension of order125. The peripheral commutator excludes an abelian extension; sigma acts by inversion on E[5] and trivially on the kernel, so the additive fifth-power map is zero. This identifies the actual exponent-five Heisenberg group.

The rational noncentral algebra is M5(Q(zeta5)). Its homology multiplicity is rank5 over that field. The Fourier convention is consistent: AUA^-1=V, AVA^-1=U^-1, A² is j↦−j, and its eigenmultiplicities are (2,1,1,1). The actual quotient genera give the displayed three equations and the unique multiplicity (0,1,2,2) for T. Consequently the algebraic factors have dimensions2 and8.

For the explicit quotient, I separately computed x((2−i)P) from x(2P), y(2P), and addition with −iP. Its difference from the displayed rational expression is exactly zero over Q(i). The condition x(2P)=−x and y(2P)=iy selects x²=(1−2i)/5, so the two Gaussian kernels are correctly labelled. The divisor identity and exact constant 5(2−i)^4 give the actual degree5 map with the stated twist. Its equivariance under tau and c is literal because h_H is even. The sigma-stable noncentral subgroup has the even quadratic invariant vector, so A²=+1 on its invariant line and sigma=T² on the quotient multiplicity factor. This identifies the SAME A2 and B8, not merely factors with matching dimensions. The cyclic20 model recovers y and x and its primitive projector is exactly B8.

## Frobenius fields and exclusion of every CM factor

The branch sections remain distinct and tame at41 and61. The character-sum convention agrees with the deck eigenspace; all primitive local characters, including infinity, are nontrivial, so there is no omitted primitive boundary contribution. The q² sum uses the norm character and determines the determinant by the rank-two identity. All sums, discriminants, unit square-class witnesses, and persistence witnesses passed the exact rerun.

The square-class tests are statements about the fixed GLOBAL field K=Q(zeta20), with its labelled action. They show two nonsplit unequal quadratic K-extensions. At the indicated K-place over q the trace is a unit and determinant has positive valuation; the two roots therefore have different valuations, so their ratio is not a root of unity. Every positive Frobenius power still generates the same quadratic field. This handles arbitrary finite extension of the field of definition of endomorphisms.

The maximal CM Hodge subobject is preserved by K. Any proper nonzero one has K-rank1, and its quotient has K-rank1 as well; that quotient is CM because its Mumford–Tate group is in the rank-one K torus. Semisimplicity then makes all of B8 CM. Under this temporary assumption, a balanced Hodge embedding bounds the K-linear Hodge commutant by dimension2, while the CM torus gives the reverse bound; the commutant is a quadratic etale K-algebra of actual abelian-variety endomorphisms. Specialization is injective and commutes with a positive Frobenius power. Integral Tate faithfulness bounds the entire special K/Frobenius centralizer by dimension2, and it already contains the persistent quadratic field. Thus the same global Hodge algebra would have to equal both unequal fields. This excludes every geometric CM factor. No Tate-surjectivity theorem or use of an auxiliary Tate prime equal to the residue characteristic is hidden here.

## Nonsplit coefficient primes

For A2 the type {1,2} in Gal(Q(zeta5)/Q) has trivial stabilizer. Equality of two coefficient characters on an open global Galois subgroup would make their Hodge–Tate weights equal at every labelled number-field embedding, hence make two translates of that indicator equal. This forces the embeddings to coincide. At every prime not congruent1 modulo5, each local field factor has degree>1, including the totally ramified factor at5. A rational line would force the same character throughout one such local embedding orbit, a contradiction. B8 has no rational line after any finite extension by the checked Ruppert consequence. The actual map [5]q then sends any surviving proper-homology line nontrivially into the original elliptic factor, contradicting the already proved original normalizer theorem. The split-prime and other fixed-subgroup questions are correctly retained as open.

## Primary rechecks

I independently reopened Ruppert, https://arxiv.org/pdf/math/9803169, Section1 Corollary1 and its proof (turn836view0/2), and Milne, https://www.jmilne.org/math/CourseNotes/AV.pdf, Theorem10.15 and Lemma10.16, printed49–50 (turn836view1/3). The former turns a Galois-stable rational line into infinite abelian-extension torsion and hence a CM subvariety; the latter gives the required injection after tensoring Hom with Z_ell, not merely injectivity before tensoring. The Hodge full-faithfulness and labelled comparison are the exact previously checked primary inputs used in A51/A42 and retained in the project bibliography.

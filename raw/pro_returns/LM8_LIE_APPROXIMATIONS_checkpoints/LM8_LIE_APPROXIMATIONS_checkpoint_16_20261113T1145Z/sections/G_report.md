INCOMPLETE

# Part G: CM arithmetic image and inertia

| Task | Statements | State reached |
|---|---|---|
| G(a) | G.1–G.5 | Complete after correcting the unrestricted D_m notation. |
| G(b), pro-ell at every prime | G.8, G.10 | Proved for every cusp packet, including inert primes and2. |
| G(b), full profinite | G.20, G.22 | Reduced to the fixed subgroup in R; a proper cover detector lies in the Prym part of a genus-at-least-two cover; unresolved. |
| G(c) | G.6–G.7 | Three-dimensional special module; outer two arithmetic components exactly zero; middle component explicit and nonzero. |
| G(d), pro-ell | G.11–G.13 | Proved at every prime; primitive split eigenline has maximum class4. |
| G(d), full profinite | G.19–G.20, G.22 | Proved when one maximal pro-ell quotient detects the subgroup; punctured transport is proved under exact fibre and target hypotheses; unresolved for arbitrary C contained in R. |
| G(e), ambient/characters/brackets/Lyndon | G.3, G.14 | Exact computations completed through14. |
| G(e), arithmetic dimensions | G.15 | Exact rational character dimensions completed, using opened2026 preprint with verified hypotheses. |
| G(e), embedding through degree6 | G.21 | The first repeated-character line is explicitly determined using the universal mixed-Tate quotient and the corrected Kummer comparison. |
| G(e), higher embedded vectors/integral indices | G.16, G.23–G.24 | Degree8 character(4,4) remains the first rational placement. Universal equations admit every lambda; the saturated ambient plane and a finite nonmetabelian coordinate extractor are proved. |
| G(f) | G.17–G.18 | All standard-tangent N_r decided; first cocycle and field explicit; exceptional packet also computed. |

## Strongest results

The standard tangent has a_s=kappa_(1+i), not a vanishing degree2 term. Its restriction to Delta is surjective Z5, and packet twisting adds the packet Kummer cocycle. Exactly one packet class cancels this coefficient. At degree4, the CM order-four automorphism kills the (3,1) and (1,3) components; b0=kappa_11/48 is nonzero. The conductor-four comparison is b0=-d chi_2^(4)/48: both the determinant correction and Nakamura2013 p492's factor12 erratum to 1995 (3.11.4) are necessary. The raw theta-product character is twelve times the analytic coefficient character.

The actual arithmetic line of degree6 and character(3,3) is now resolved: V6=([F,[F,epsilon6]]-192Z3)/6, with coefficient chi3/1536. Z3 is the explicit invariant derivation in Dorigoni et al2026 (5.47), equal to Pollack's tree divided by12. The proof uses the constant mixed-Tate quotient of the universal lisse realization to transport only the invariant coefficient; the geometric coefficient is separately evaluated on the CM fibre by the factorization theorem. Ordinary elliptic W and relative Tate M are distinguished: the degree4 and degree6 Tate components have the same M-weight6, and Hain-Matsumoto Proposition29.1 identifies only the latter modulo geometry. Thus the degree4 term measures the single constant coefficient without transplanting that geometric term to CM. The projector eigenbasis is explicitly rescaled to be symplectic. The raw-Theta factor12 correction is essential. The first remaining rational-coordinate question is in degree8, character(4,4).

A new free-Lie argument proves that any multihomogeneous special derivation with nonzero metabelian image has kernel precisely the boundary line. This proves the fixed-subgroup assertion for every cusp packet at every prime: Nakamura's actual metabelian nonvanishing theorem supplies a derivation at every prime, and CM Frobenius projectors isolate a homogeneous character. No integral eigenbasis is needed at inert primes or2.

For normalizers, a finite-cover detector makes the same power character occur in a cover's homology, forcing the first lower-central degree to be1 or2 by weights. Inert and2-adic CM homology is irreducible; split eigenlines are obstructed by the surviving degree4 derivation. Thus the first degree is2 and the character is exactly cyclotomic. Nakamura1994 Theorem2.1.1 then places the subgroup in actual pro-ell inertia. The class5 obstruction needs b0 alone; b_minus is zero.

In the full profinite group one nonzero pro-ell image is enough for recognition: first apply Nakamura to the actual ell-component, then use the peripheral centralizer (including prime-supported exponents) to absorb the entire procyclic subgroup. The remaining full profinite groups lie in the common kernel of maximal pro-ell quotients. G.22 further confines a residual proper-homology detector to the Prym part of a cover of genus at least2. A detecting map to a punctured elliptic target would exclude a residual normalizer if the exact target has the proved recognition property, but such a map must have an entire fibre supported in the existing boundary. The degree bound and an explicit [2]-cover/[3]-quotient example show that a Jacobian quotient alone does not provide this map. A CM eigenline also gives an explicit failure of normalizer-preserving lifting after adding a puncture.

## Exact computed rows

For degrees2,4,6,8,10,12,14:

- Special dimensions: 1,3,6,13,37,99,284.
- CM-fixed dimensions: 1,1,4,5,21,45,150.
- All lower bracket ranks: 0,0,0,3,15,47,153.
- Even-lower bracket ranks: 0,0,0,3,15,47,147.
- CM lower-even bracket ranks: 0,0,0,0,4,11,41.
- Actual rational outer arithmetic dimensions: 0,1,3,3,8,11,24.
- New arithmetic generator counts: 0,1,3,3,5,5,7.

The three complete ambient CM bracket maps at10,12,14 are injective. Restricting them to the actual arithmetic spaces determines the rational dimensions without assuming freeness in unbounded degree or choosing unknown generator coordinates. The2026 generation theorem's hypotheses are checked by proving h(Q(zeta20))=1 with a Minkowski bound and an explicit norm5 element, and that K(25) has exactly two primes above5 using the ray group and Frobenius cosets.

The free-Lie ranks through14 are 2,1,2,3,6,9,18,30,56,99,186,335,630,1161. Every standard Lyndon expansion through14 has leading coefficient1; Witt character counts are checked through16 where needed for the derivation kernels.

## Programs and executions

- `g_lie_core.py`: self-contained exact Lyndon/associative algebra utilities adapted with attribution from the supplied LM3b implementation.
- `g_special.py`, `g_special.out`, `g_special_results.json`: exact ambient character kernels and lower-even brackets.
- `g_kernel.py`, `g_kernel.out`, `g_kernel_results.json`: T-kernels through degree10, and the extra odd7+7 contribution at14.
- `g_arithmetic.py`, `g_arithmetic.out`, `g_arithmetic_results.json`: exact arithmetic character dimensions, ray-class hypothesis certificates, and separating Frobenius point counts.
- `g_embedding.py`, `g_embedding.out`, `g_embedding_results.json`: explicit degree6 arithmetic vector; exact boundary, SL2, metabelian, Pollack-tree, and defining Tate-lift checks, with source normalization corrections recorded.
- `g_degree8.py`, `g_degree8.out`, `g_degree8_results.json`: exact one-parameter reduction of the degree8 middle line, including its Kummer normalization and a certificate that the verified finite tests do not distinguish the parameter. No parameter is asserted to be realized arithmetically.
- `g_degree8_nonmet.py`, `g_degree8_nonmet.out`, `g_degree8_nonmet.json`: saturated ambient Z5 plane and two nonmetabelian Magnus coordinates; actual Hall-group word expansions modulo125 verify ambient coordinate pairs (1,0),(1,1), inverses and peripheral preservation. No arithmetic value of the second coordinate is claimed.
- `g_cover_transport.py`, `g_cover_transport.out`, `g_cover_transport.json`: exact division-polynomial certificate for the detecting elliptic quotient whose restriction misses no point of the target; this refutes an automatic puncturing step, not G.20.
- `g_metadata.py`: reproducible PartG ledgers.

All listed programs were run. Rational rank calculations are explicitly distinguished from integral saturation assertions. The finite T-kernel checks are supplementary; the infinite fixed-subgroup result uses the proof in G.8.

## Remaining obligations and approaches actually tried

1. Full profinite fixed subgroup: all primewise images are inertia, so remove the single matching profinite inertia exponent. The remaining element is in R. A finite quotient and its cyclic subgroup always give an open-cover abelianization detecting a nonzero residual element. Descending this cover makes its class Delta-fixed. G.22 shows that its proper-homology class is in the Prym kernel of the pushforward to E, so the inherited E quotient cannot carry it and genus-one compactifications are excluded. Higher-genus Pryms can still have relevant CM factors. The missing step is a cofinal detecting-cover construction eliminating that component, or a puncture-compatible detecting map that also transports the actual lifted cusp-packet section. Nakamura/Stix recognition hypotheses were opened and checked; Stix's torus-versus-abelian-variety hypothesis fails over K^ab explicitly.
2. Full profinite normalizer: every subgroup detected at one prime is now recognized. For C contained in R, a finite-cover detector allows a weight-one Prym line as well as weight-two boundary. G.22 proves that a detecting map f to a pointed elliptic target with a proved normalizer criterion would rule it out, provided a whole fibre of f lies in the cover boundary. The necessary degree bound is deg(f) <= deg(Y/U). The detecting quotient [3] on the cover [2]:E minus E[2] -> U fails this condition for every target point. Adding punctures cannot be treated as an equivariant lifting step: the proper CM eigenline has no open-normalizer lift to P5. A higher-dimensional CM factor or a different CM field additionally requires its own elliptic quotient and target theorem. No argument supplies all these conditions for arbitrary covers; peripheral centralizers help only after a nonzero inertia component has been located.
3. Arithmetic placement: metabelian characters and ambient bracket injectivity determine all rational dimensions through14. The degree6 ambiguity was resolved in G.21 by combining the universal constant mixed-Tate quotient with the CM elliptic-character factorization, including the factor12 erratum. The degree8 middle projection is exactly d^3 chi4^(4)/267840 times (A8+lambda B8), with A8=F^3 epsilon8/120, B8=[epsilon4,F^2 epsilon4]/2 and a unique unknown scalar lambda. The new exact program shows all boundary, CM/conjugation symmetry, metabelian, universal-geometric and rank tests through14 are independent of lambda. The further Tate-formula attack is explicit: Dorigoni equations5.46 and7.22 give Sigma3[8]=[epsilon4,F epsilon4]/480, verified against the defining lift through word length9. This term has relative M-weight minus6 and zero image in the constant quotient, so it does not supply the missing CM weight4 coefficient. The additional Tate relation [Sigma,N]=0 cannot be transported to this CM generator: N begins with minusF, and F(A8),F(B8) are independent, so it would exclude every lambda. There is no even-weight constant mixed-Tate generator to determine the coefficient by the G.21 argument. The October2026 local Coleman-Ihara formula was also specialized at (4,4), giving scalar minus6048 in its own normalization. Its character vanishes on B8, so it supplies no equation for lambda; integral indices still require the Coates-Wiles image lattice and the comparison with the eighth Johnson subgroup. Remark5.6 corrects the older Coleman-Ihara corollary, not the Theorem1.7 factorization used in G.25. Exact higher iterated-Eisenstein specialization coordinates and integral indices are still missing.
The nonmetabelian follow-up G.23 proves that the entire parameter family exponentiates in the actual universal elliptic kernel to all orders; averaging in its positive prounipotent kernel transports it to every prescribed exact finite CM lift without changing the degree8 term. Thus those exact universal constraints cannot select lambda. G.24 supplies the missing measurement explicitly: alpha(D)=-[x^5y^4]D(x) and nu(D)=[x^4yxy^3]D(x)+4[x^5y^4]D(x), with lambda=31/20+nu/alpha on an actual eighth-Johnson element having nonzero alpha. The saturated ambient plane is Z5*(A8+(31/20)B8)+Z5*B8. A characteristic finite Magnus quotient modulo (5^r,I^10) reads both coordinates without logarithms or division by5. The actual Galois value of nu and the arithmetic image ideal of alpha remain uncomputed; no arithmetic saturation is inferred. Malkin2020 supplies a genuinely depth-two Hodge/Bianchi framework, but its Section2.2.3 conditions the etale transfer and its averaged-basepoint torsion-punctured setting lacks the required comparison to this once-punctured tangent. Enriquez Section7.5 full cusp-to-cusp Mellin formulas likewise do not supply the CM specialization.

4. Earlier inert-prime and integral-Malcev-conjugacy obstacles were resolved, not left open: the general metabelian kernel lemma handles the former, and cyclotomic normalization plus Nakamura handles the latter.

## Source audit

Opened and inspected the attached Nakamura1995, Tsunogai1995 and Pollack2009 documents, the CK E1–E3 and A6–A7 proofs, and LM3b D.1–D.5/A.7–A.16. Downloaded/read Nakamura's RIMS1691 preprint of the final2013 paper, Ishii2025, Ishii–Goto2026, Ishii2026 graded Lie preprint, Nakamura1994, Bannai–Kobayashi–Tsuji2010, and the October2026 Coleman–Ihara preprint. The final2013 PDF p492 erratum was independently opened and applied. Brown2015, the supplied Hain–Matsumoto source, and the primary HTML/PDF of Dorigoni et al2026 were inspected for G.21. The latter's equation5.53 sign inconsistency is detected by an exact boundary calculation, and equations5.41/5.46 fix the used normalization. Bibliography entries identify precisely which opened results are used and which remain only attempted routes. Recent preprints are marked as such. Enriquez2014 Sections4.7–4.8, Proposition4.19/equation(48), Proposition4.20 and Section7.5 were reopened for the all-order obstruction; Malkin2020 Sections2.2.3 and3–4, Lemma3 and Theorems11,15–16 were opened for the conditional depth-two route. These new readings are recorded in G_nonmet_readings.csv and the Malkin bibliography entry marks its precise conditional scope.

Downloaded third-party PDFs/TXTs in `notes/g_*` are reading material. The parent may omit those copies from the deliverable ZIP; their exact primary URLs and theorem references remain in the bibliography. No downloaded source is treated as a new mathematical artifact or as a substitute for a proof.

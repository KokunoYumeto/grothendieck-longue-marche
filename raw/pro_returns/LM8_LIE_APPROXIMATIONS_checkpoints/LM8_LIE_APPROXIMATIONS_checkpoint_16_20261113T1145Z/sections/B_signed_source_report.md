# Actual signed source: B.31–B.34

The actual §49 source, its kernel preservation and its continuous local/profinite relative actions are now proved. The full first modular image is computed. A compatible action of the entire profinite source over the rational base is refuted. These advances do not classify the retained conjugator images on the rank-five q2 stage or every higher relative stage, so B.24d remains Open with its former preservation and existence obligations removed.

## Source and topology

The original cote140-3 pages530,534,549,550,559,560 were extracted from the Montpellier archive and directly viewed. Scan numbers are physical PDF pages, including the cover; archive footers are one lower. Visible folios are568,570,578,583. Unnumbered versos are recorded as such in `source_checks/140-3-signed/concordance.json`; no folio numeral is invented from an interpolation.

Definition(7) on530 and definition(6) on549 are actual continuous automorphism sources. The separately recorded signs coincide with the reductions of the multiplier in this particular full modular group, by its Z/12 abelianization. The loop is a faithful copy of Zhat, so its image recovers the multiplier. This need not hold for the arbitrary groups used in the manuscript's general functor constructions.

For x=omega(sigma*rho)^2, the actual source fixes omega and sends x to x^mu. Since F is the closed normal closure of x, it preserves F and every characteristic Fermat kernel K_n. The signed normalizers, based fibre products and unbased quotient are given their own explicit action maps. An extra conjugator is not discarded merely because it disappears from the first modular automorphism.

All relative pro-prime groups and continuous Q_l prounipotent completions are constructed with their finite quotient of order12n² and free radical of rank n²+1. The proof uses actual coset cocycles and a universal property after preservation has been established. Abelian integral stages have actions over Z_l, coefficient by coefficient. No integral BCH model at a bad prime is assumed.

## Two entire Fermat families

B.32 proves intersection_n K_n'=F''. A finite metabelian quotient detects every element outside F'', and choosing n divisible by its abelian exponent kills K_n'. Compactness then identifies the inverse tower with C/F''. This gives an exact two-generator congruence test for the action kernel, while leaving the full lifting image unevaluated.

The relative pro-prime Fermat family, with n and the prime varying, detects exactly finite quotients with nilpotent derived subgroup. The reverse inclusion is proved by taking the Sylow factors of that derived subgroup. Thus the family is still a proper quotient of the free profinite group. The program verifies a generated A5 of order60 with perfect derived subgroup and trivial centre, providing a finite group outside this class. This argument concerns the complete collection, not only one omitted finite quotient map.

## Exact first image and the rational obstruction

B.33 proves that the actual D image on Delta=C/F' is Zhat semidirect Zhat^times. The canonical multiplier action sends the two braid generators to their mu powers; the GT correction vanishes because their squares commute on Delta. Every multiplier occurs in the actual Galois image. For multiplier one, the finite Dic3 action has two possibilities. Removing that parity leaves a direct integral cocycle calculation, whose only solutions are conjugations by x^t. This yields the unique form Int(e0^r)s_mu and the exact affine composition law.

The finite reductions for n1 through8 have group orders12,48,108,192,300,432,588,768 and source-image orders4,8,24,32,80,48,168,128. The code checks every element, all generator edges, all affine composition pairs and every normalized cocycle residue pair. It does not identify these images with every solution of equations on an isolated finite group.

B.34 chooses a true cyclotomic multiplier whose fifth-adic coordinate is the root sqrt6 congruent1 modulo5, with all other coordinates1. Its first Lie-layer matrix has trace2sqrt6, which cannot be the scalar extension of a rational matrix. The Q-defined action is therefore false, already at the first stage. Hensel lifts through5^12 are included in the code output; irrationality and all-level existence are proved in the text. This does not deny constant profinite scheme actions or the rational fine-data existence in B.24c.

## Remaining q2 information and a rejected shortcut

For u in the congruence kernel D0, the induced action on the six boundary classes of K2^ab is trivial. The remaining q2 action is a cocycle over H48 with values in its rank-five lattice. Averaging over Q_l reduces it to an inner vector fixed by e0 and killed by projection to the minimal rank-two lattice.

An attempted shortcut would identify the six-cusp permutation with the degree-six edge action of S4 and conclude that this fixed kernel is zero. The exact saved matrices refute that identification: e0 has cusp permutation `[0,1,4,5,3,2]`, of cycle type1+1+4, and its invariant lattice has rational rank2. The kernel of projection on that invariant space has rank1, generated in the B.24a basis by `(-1,1,0,1,0)`. Both `(1-R)` and `(1-S)` send that vector to the primitive vector `(-1,1,1,1,-1)`. Thus a genuine additional integral parameter survives; the q2 action does not collapse by the attempted argument. Its actual arithmetic and full-source image, with the retained sigma conjugator, is the next required computation.

These residuals are not recast as a missing universal property. The actions exist; their particular images and higher realization are the unfinished work. B.24d also retains the question whether arbitrary first-stage additive-polynomial lifts extend to all higher nonabelian stages.

## Files and review

`b_signed_source.py` uses the previously executed integral cocycle model and records its SHA256. It writes the exact finite tables, A5 certificate, Hensel lifts and scope in JSON and text. `b_signed_source_metadata.py` writes the four statement rows, five task rows, four reading rows and original-page concordance. The mathematical proofs and direct integral cocycle classification were independently reviewed by the CM agent; the finite program passed.

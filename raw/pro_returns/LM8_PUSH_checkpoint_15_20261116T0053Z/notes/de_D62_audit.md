# D.62 audit ledger

The candidate remains in `notes/de_alexander_all_lim1_draft.tex` until the checkpoint07 source freeze is released. It has not yet been added to the statement register.

## Independent root audit: PASS

The root read the entire proof, reread D.47 at the first coefficient level, and independently reopened Jannsen, Lemma 4.15, printed page 229; Milne ADT, II Proposition 2.9, printed pages 170–171; and I Theorem 4.10(a), printed pages 56–57. The audit checked the split-prime Gysin differences, finiteness of the actual inverse-limit image, the Mittag–Leffler contradiction, the uniform-cochain closure argument, and local invisibility.

## Independent FGH audit: PASS

FGH read the entire candidate and independently reopened Jannsen's Lemma 4.15 in the primary PDF (reference `turn711view0`). The finite-stage residue construction gives independent classes in the first finite-coefficient image without asserting that they lift integrally. If the tower were Mittag–Leffler, its eventual-image tower would have surjective maps and its limit would map onto its infinite-dimensional first term. D.47 instead makes the image of actual integral classes finite. This is the exact contradiction. FGH also checked the continuous lifts of finite-valued cochains and the local vanishing of the derived-limit correction. No fixed ramification set is used across coefficient levels.

## Sources checked by the author

- Uwe Jannsen, *Continuous étale cohomology*, https://epub.uni-regensburg.de/26684/1/jannsen12.pdf: Proposition 1.6, Theorem 2.2, and Lemma 4.15 (printed page 229). The last is the countable-group criterion that vanishing of the first derived inverse limit is equivalent to the Mittag–Leffler condition.
- J. S. Milne, *Arithmetic Duality Theorems*, https://www.jmilne.org/math/Books/ADTnot.pdf: I Theorem 4.10(a), I Corollary 2.3, and II Proposition 2.9. The finiteness of the finite-set global second cohomology uses part (a) and finite local groups, rather than part (c).

## Exact scope

Every completed abelian Kummer pair is allowed, even with infinitely many nonzero prime exponents and even if no metabelian section lifts the pair. The theorem proves that the unrestricted continuous second cohomology has a nonzero locally invisible first-derived-limit kernel, exactly its closure of zero for the displayed uniform-cochain quotient topology. It does not compute the isomorphism type of that kernel, the separated quotient for every twist, or any first finite-derived obstruction for the Fermat families.

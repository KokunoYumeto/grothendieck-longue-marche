# Scan 030: limited check of the affine implication

Main reader: GPT-6 Astra Pro; effort inherited, not independently exposed.
Prepared from the supplied letter text while the independent readers inspected
the ink. Main subsequently compared all three complete readings: each confirms
exactly the affine implication in the opening sentence. The limited argument
is connected to that observed wording in s030-note08; it changes no reading.

The letter uses: if X is affine, then X is quasi-compact and quasi-separated.
This elementary implication can be checked without looking up the propositions
mentioned elsewhere on the page.

Write X = Spec A. For any open cover, refine it by principal opens D(f_i).
If the f_i generated a proper ideal, a maximal ideal containing it would give
a point outside every D(f_i). Thus they generate the unit ideal. The expression
of 1 as a finite linear combination uses only finitely many f_i, whose
principal opens already cover X. Choosing the corresponding members of the
original cover proves quasi-compactness.

For quasi-separatedness, the absolute diagonal is the closed immersion

    Spec A -> Spec(A tensor_Z A)

induced by the surjective multiplication homomorphism
`a tensor b -> ab` (surjectivity follows from `a = image(a tensor 1)`).
A closed immersion is quasi-compact, so the diagonal is quasi-compact and X
is quasi-separated. The empty affine scheme is covered by the same argument
with the usual zero-ring convention, or directly.

The basis of principal opens, the existence of a maximal ideal over a proper
ideal, the affine description of products and closed immersions, and the
diagonal criterion for quasi-separatedness are standard background facts
used here, not independently reconstructed in this run. The finite-cover and
diagonal arguments themselves are the targeted check.

This does not check that the letter's proposition 2.1.1 reduces to affine X,
the reductions to 2.1.5 or transcendence degree one, the cited base-change
theorem, or the proposed interpretation in terms of champs. Those numbered
statements are not reproduced in full on the supplied sheet. No external
source or published version was consulted, and this argument changes no ink
reading.

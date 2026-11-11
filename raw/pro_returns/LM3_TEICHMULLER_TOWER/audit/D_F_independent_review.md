# Independent review of F.1–F.4, F.9–F.11, F.18

Reviewed by the Part D agent after completing the arithmetic section. No blocking mathematical error was found in these statements with their stated scopes.

## Primary source checks

The attached Jansen text was checked at Corollary 6.6 and Theorem 6.7: the exit category is the opposite-deformation Charney–Lee category, and constructible coefficients are covariant functors on that exit category. Its Theorem 6.7 contains a visibly inconsistent displayed stability inequality in the concluding special case; F correctly uses the stable condition from the definitions rather than importing that typo.

BGH's August 21, 2020 primary text was reopened at Proposition 12.6.4 and Corollaries 12.6.6–12.6.7. Corollary 12.6.7 identifies Gal(X/P) with the profinite *stratified* completion of the exit-path infinity-category. It does not identify strict finite-category quotients with that completion. F.9 and F.18 retain this distinction correctly. BGH Proposition 13.9.17 and Corollary 13.9.19 are the precise stack descent statements for F.15; the root agent has been notified of these exact numbers.

## Algebraic and categorical checks

**F.1.** The right-coset composition formula is well defined because g^{-1} Delta_tau g is contained in Delta_sigma. The exit/deformation variance agrees with the primary theorem. A finite-object skeleton changes the category by equivalence and retains its composition; it does not groupoidify the category.

**F.2.** Finite congruences are cofiltered under intersection. Surjectivity on each Hom set and the fixed finite object set are enough to lift composable pairs and descend functorial equations from the materialized inverse limit to one finite quotient. The same finite-object argument handles natural transformations and inverses. The equivalence asserted is restricted to this strict quotient system, not arbitrary pro-objects in a homotopy category.

**F.3.** The [1] versus point example is valid. Its coefficient-category distinction is witnessed by three versus two subobjects of the terminal object. This demonstrates why arbitrary transformations cannot be treated as equivalences; it does not contradict invariance under natural isomorphism.

**F.4.** Finite-valued representations factor through one finite quotient because finitely many finite stalks and finitely many ordered pairs of stalks are involved. The coproduct of Z/m!Z is a continuous discrete Zhat-set with no uniform finite quotient, and every orbit is finite. The distinction from the noncontinuous abstract regular action is also correct. No unsupported assertion about arbitrary rational local systems is used.

**F.9.** Finite covariant representables recover Hom_C(x,y) from natural transformations between the evaluation functors ev_x and ev_y, with the variance in the displayed formula correct. Passing through the quotient system recovers the inverse-limit Hom sets. Retaining the specified evaluation functors avoids a bare categorical reconstruction claim that would otherwise require further discussion. The finite-set comparison is sufficient for this reconstruction but does not by itself prove the higher comparison left unresolved in F.18.

**F.10.** The Galois action on finite boundary-constructible data descends through the reconstructed category. If a left action is intended, the transfer should explicitly use inverse pullback (sigma^{-1})^*; this minor convention was sent to the root agent for incorporation. The simultaneous cyclotomic action on local normal-crossings inertia is justified by the Kummer coordinate covers. The faithfulness direction from n=4 to n>4 is correct because forgetting gives a surjective map of the open-stratum groups. n=3 is correctly excluded.

**F.11.** With the stated transporter model and the split-label calculation, the relevant kernel is the diagonal (a,-a) in Zhat^2 and its lifting groupoid is B Zhat. The nonzero continuous H^1 with F_l coefficients disproves terminality of the required homotopy type. This is a derived or homotopy cofinality obstruction, and F explicitly does not claim that connectedness or ordinary Set-valued colimits detect it. The same cyclotomic exponent on both node directions preserves this kernel. Finite modulus computations supplement, rather than replace, the inverse-limit algebra.

**F.18.** Leaving the stronger comparison unresolved is logically consistent. It requires compatibility with all pi-finite homotopy coefficients and their gluing. Finite sets alone do not imply it. The n=4 compactification is P^1, so its unstratified two-dimensional class is a legitimate first test, even though the stratum groups are free. Nothing in this review proves a counterexample to the stronger comparison.

## Recommendations communicated

1. Use inverse pullback explicitly for the left Galois action.
2. Cite BGH Proposition 13.9.17 and Corollary 13.9.19 in the stack descent paragraph.
3. Retain the coefficient restrictions and the F.18 unresolved comparison when reporting the outcome; do not describe the strict finite-category comparison as a full infinity-categorical theorem.

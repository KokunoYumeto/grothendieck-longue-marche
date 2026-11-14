# Independent review of the F.48 Abhyankar valuation obstruction

Reviewer: finite-field agent, 14 November 2026.

**Verdict: PASS in the exact stated scope.** I read every section of audit/F_Abhyankar_valuation_obstruction_candidate.md, checked both topological inputs F.32 and F.40 in the integrated manuscript, and reopened the cited valued-field sources. No modification of the author's candidate or integrated F files was made.

## 1. Monomial valuation and constants

The integer monomial exponents have distinct values because the chosen gamma_i are rationally independent. Thus every polynomial has a unique least-valued monomial; the same argument proves multiplicativity. A value-zero rational function has equal least exponent vectors in its numerator and denominator, so its residue belongs to F. This verifies both the initial residue field and the exact free value lattice without imposing a rank-one or discrete order.

Henselization is immediate and algebraic. Every nonzero algebraic constant has valuation zero: otherwise either the constant or leading term of its minimal polynomial would be the unique least term. Reduction embeds the chosen algebraic closure of F.

For a finite constant extension F'/F, dividing an H-linear combination of an F-basis by a least-valued nonzero coefficient produces a nonzero residue by linear independence over F. This proves both the degree [HF':H]=[F':F] and the equality of its value group with Gamma_0. Its residue field is exactly F'. No unproved regularity or linear-disjointness assertion is needed.

## 2. All radical levels and the algebraic closure

The n^r parameter-root monomials have distinct value classes modulo Gamma_0, so they are linearly independent over HF'. The elementary degree upper bound is also n^r; hence they form a basis. Expanding in this basis proves the value group is exactly(1/n)Gamma_0. In a value-zero expansion the only possible least monomial has exponent vector zero modulo n; its coefficient gives a residue in F'. Thus the claimed residue field is exact, not only an inclusion.

Compatible parameter roots make these fields directed. Their union is algebraic over H, so it remains henselian. The union has divisible value group Gamma_0 tensor Q and algebraically closed residue field Fbar. ADH Corollary3.3.22 applies in residue characteristic zero and proves that this union is algebraically closed. Since it lies inside the chosen algebraic closure and contains H, it is that entire closure. There is no appeal to an unjustified multivariate Puiseux expansion or completeness assumption.

The resulting absolute Galois group description is correct. Coefficientwise G_F automorphisms fixing the compatible roots are well-defined by the established bases. The kernel is the full compatible root-multiplier group, with diagonal cyclotomic conjugation. These maps are continuous because every finite collection of coefficients and roots occurs at one finite level.

## 3. The substitution is an automorphism in arbitrary ordered rank

The new image of a monomial is the old monomial times a power of1+t1, a unit of residue one. Its value is unchanged. Distinct original monomial values remain distinct, so the least-valued term cannot cancel. This proves that the substitution is a valued-field embedding on the rational-function base, even when the value group has higher order rank or is nondiscrete archimedean.

Hensel's lemma supplies the unique positive-valued root r1 of X²+X-t1. It has the same value as t1 and r1/t1 has residue one. The inverse substitution therefore preserves the valuation by the same monomial argument. Henselization universality extends both maps; their composites agree with the identity on the base and hence on the henselization. The argument does not require convergence of an inverse series.

## 4. Root compatibility and centralization

For every n, the residue-one n-th root beta_n of1+t1 exists and is unique because n is a residue unit. Uniqueness makes beta_mn^m=beta_n. The proposed images of the parameter roots satisfy the transformed defining equations. The exact degree/basis calculation makes the induced field map well-defined; its image contains H, F' and every parameter root, so it is onto.

Compatibility across both coefficient extensions and root levels is explicit. The resulting closure automorphism fixes Fbar and maps each u_1,n to u_1,n beta_n. An arbitrary g in G_H multiplies each parameter root by an n-th root of unity in Fbar and fixes beta_n. Therefore the two composites agree on H, Fbar and every parameter root, hence on the entire algebraic closure. This is centralization of all G_H, not only inertia or an abelian quotient.

F.40 consequently applies. The rational values1 and2 force any algebraic monomial inducing the relative point function to be the identity, whereas t1 is moved. The passage to every algebraic extension uses F.32 contrapositively; it does not assume that this particular automorphism preserves an arbitrary algebraic overfield.

## 5. The intrinsic Abhyankar consequence

ADH supplies a coefficient field in the henselian valuation ring. Choose a positive rational basis of the value group inside actual values and lift its members to t_i. Unique monomial values prove algebraic independence over the coefficient field. The stated equality of residue transcendence degree plus rational rank with trdeg_Q K then makes K algebraic over F(t_1,...,t_r). Since K is henselian, the henselization embeds in it by the universal property. K is algebraic over that embedded henselization, so the previously proved obstruction applies.

The argument uses rational rank, not order rank; it permits a larger nondiscrete ambient value group. The assumptions of residue characteristic zero, finite transcendence degree and the exact Abhyankar equality are all retained. No extension to valuations with transcendence defect is inferred.

## 6. Independently opened primary source

Aschenbrenner, M., van den Dries, L., & van der Hoeven, J. (2017). *Asymptotic differential algebra and model theory of transseries*. Primary author PDF https://www.math.ucla.edu/~matthias/pdf/mt.pdf . Opened as turn871view0.

I read Proposition3.3.8 and Lemma3.3.9 with their coefficient-field proof (authorpp117–118; turn872view1 and turn873view0); Proposition3.3.11 and Corollary3.3.12 (pp119–120; turn873view1); Corollary3.3.22 (p124; turn872view0); and the definition of henselization, Proposition3.3.25, its uniqueness proof, and Corollary3.3.26 (p125; turn873view2). These statements apply to arbitrary ordered value groups under the exact hypotheses used here.

No numerical test was required for this review. The finite series identities mentioned in the candidate are not substituted for the henselian uniqueness or closure arguments. The conclusion remains a necessary obstruction to reconstruction, not a converse classification.

# Independent audit of E.46

**Auditor:** bc_fermat. **Result:** PASS, after the author corrected one harmless TeX comma and stated the inverse-Shapiro boundary sign explicitly.

I read the complete statement and proof in E_norm_sections.tex and independently checked the following actual maps.

- The section law gives the twisted action chi_g T^(A_g) f(T^chi_g); geometric conjugation gives exactly the stated change A'_g=A_g+(1-chi_g)s and the second-coordinate formula.
- Complex conjugation makes the first-coordinate normalizing s unique and continuous. The resulting fiber is the additive cocycle quotient for J_A, with the displayed origin.
- Evaluation at each chosen orbit point gives finite Shapiro. From the cocycle identity I obtained c_z=c+delta(m), with m_i=c(g_i)_i and delta(m)(g)=g m-m. This proves the actual inverse and its sign.
- Positional pushforward is corestriction and hence the Kummer norm. The Galois ratios of the product of conjugate roots give this equality directly. The inverse-deck convention in the residual action is correct.
- Compatible class representatives can be aligned by lifting the lower bounding elements through the surjective positional module maps. For injectivity, H^0 of every positional Tate module is zero, so the bounding elements themselves are uniquely compatible. This supplies the exact inverse-limit comparison without a compactness or norm-surjectivity assumption.
- The topology argument is valid: a bounding element in a finite module quotient lifts to the completed module, so finite-cohomology kernels are exactly the quotient neighborhoods. The exact J_A injection is topological because its finite residual bounding element is unique.
- The sequence with augmentation modulo three has H^0(Q,F_3(1))=0; its degree-one kernel is precisely the cube condition on u_0. The restricted prime-valuation description verifies division by three in the completed rational multiplicative group.
- For rational A=3 kappa(a), the actual root torsors have algebra Q[X_n]/(X_n^(3^n)-a^3), and cubing is the positional transition. The determinant identities give norms of X_n and 1-X_n even when the algebra is disconnected.
- The toric map divides both raw coordinates by three. It sends the explicit family to (kappa(a), r kappa(a)+z kappa(1-a^3)), as stated.
- For a=2, Eisenstein at two proves the two factors and all degrees; beta_n^(3^(n-1))=2 zeta_3 gives the K-factor and its degree. The fields and their cubing maps are the actual ones in the statement.

## Primary passages independently opened

James S. Milne, Class Field Theory v4.03:

- II Proposition 1.11, printed p.62 / PDF index70, statement and proof of Shapiro.
- II Example 1.27(a), printed pp.68–69 / PDF indices76–77, evaluation at the identity and its agreement with Shapiro.
- II Example 1.29, printed p.70 / PDF index78, the explicit induced-module transfer map and corestriction.

Source: https://www.jmilne.org/math/CourseNotes/CFT.pdf.

The continuous inverse-limit step is proved directly in the audited text, in addition to its reference to Jannsen.

## Independent program run

A copy of e_norm_sections.py was executed in research_e47/audit_e46. Its output and JSON were retained there and compared with the author's JSON; they are identical.

- 78,732 finite cocycle identities in the actual degree-162 splitting group.
- Actual norms 2 zeta_3 to 4 and the entire etale element X_1 to 8.
- Root-cubing transfer of zeta_3 becomes the displayed coboundary at both lower factors.
- Six affine orbit decompositions, all tested positional transitions, 30 total-norm examples, and five exact a=2 factorizations.

No mathematical gap remained in the written comparison. The result gives exact norm equations for all first-coordinate fibers and evaluates the stated explicit ramified families; it retains the kernels of the intrinsic maps to H.

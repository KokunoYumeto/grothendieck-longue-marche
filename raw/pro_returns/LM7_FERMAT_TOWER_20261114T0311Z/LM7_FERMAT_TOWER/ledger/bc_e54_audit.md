# Independent audit of E.54

Status: PASS.

Read the entire theorem and proof in E_class3_frobenius.tex. Independently opened Furusho’s original Annals paper, Theorem2 equation(5), its proof in section3, and Corollary12:

https://annals.math.princeton.edu/wp-content/uploads/annals-v171-n1-p13-p.pdf

The three-cycle convention gives 3β=m(m+1)/2 and hence the positive coefficient β=(χ²−1)/24. The actual geometric Galois conjugator lies in F′, so its degree-three part is central in the class-three quotient and disappears from conjugation. This gives the claimed genuine action without a higher-coefficient assumption.

Checked the surjectivity of h_* by its two independent mod3 Kummer characters. The non-cube assertion for h uses the divisor O−C₂ and the impossibility of a degree-one map from the elliptic curve to the projective line. The closed-image/Frattini argument then gives the stated surjection and its exact kernel. The metabelian kernel lies in γ₄N. For the single-cusp marked ideal, the degree-three bracket of three copies of its one degree-one peripheral generator vanishes, so γ₃(I_Q) lies in γ₄N as required for the displayed factorization.

Checked the based formal-disc transport, the unit constant a=ζλ^−3, the two actual root systems, their ratio ζ_(3^n)^2, and the corresponding signed inner transport. The local principal-unit roots are fixed, giving the exact new Frobenius value1 and old value−5. The global image is the entire displayed affine congruence group: λ is not a cube in the cyclotomic extension, by the explicit implication to a cube root of3 and the abelian-subextension contradiction.

Checked the integral Hall multiplication law and the local tame group. The class-two relation is exactly L=0. Changes of central inertia coordinates alter the error by60 times those coordinates. Thus divisibility by3 is necessary and sufficient, with the stated correction. The central local cohomology is Z₃(3)²/63, hence (Z/9)². The lower twisted stabilizer is trivial because its first nonzero graded coordinate would be fixed by4 or16; both minus-one operators are injective.

Fresh copied runs of a_class3_frobenius.py and a_class3_local.py produced JSON identical to the original retained certificates. Their outputs are retained in research_e54_bc_audit.

In addition, bc_class3_symbolic.py independently derives the full local relation in symbolic Hall coordinates and verifies every coefficient of L,R,S for all six lower coordinates. It verifies both Hall inverses, the exact central correction60(r,s), and the entire example family error5/2−4N. Its source, output, and JSON certificate are included in code.

No mathematical or typing correction was required.

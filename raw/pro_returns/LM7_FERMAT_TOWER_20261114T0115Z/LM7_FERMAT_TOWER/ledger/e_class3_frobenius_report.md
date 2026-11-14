# E.54 — an evaluated genuine class-three quotient

The actual morphism h=(x+y)/(x+zeta y) from the nine-punctured cubic to the thrice-punctured line induces a surjection of geometric free pro-three groups. The proof upgrades E31's finite surjection by the exact Frattini argument: the two geometric Kummer classes are independent, and the compact image is closed. Thus the intrinsic class-three group has the actual rank-two free class-three quotient C, with kernel h_*^{-1}(gamma4 F)/gamma4 N.

The tangential expansion is h=a s^3 u(s), a=zeta(1-zeta)^(-3), u(0)=1. The unique roots of the formal unit and the source tangent leave exactly the procyclic path cocycle x^{kappa_a}. This gives the actual isomorphism (w,g) -> (w x^{kappa_a(g)},g) between the induced arithmetic semidirect group and the standard target arithmetic group. The exact action is evaluated using only chi and this Kummer character. Its conjugator coefficient is +(chi^2-1)/24 for the convention c=[x,y], y -> f^-1 y^chi f. The three-cycle relation determines the sign and denominator directly. Terms of f in gamma3 are central in C, so they do not contribute to the action.

Every Hall generator image is displayed in E54.5. The full genuine arithmetic image over K is the faithful affine group Gamma_a defined by chi in 1+3Z3 and k congruent to (chi-1)/3 modulo3. The proof computes all its fibers: the cyclotomic kernel has kappa_lambda image Z3 because lambda cannot be a cube in the abelian cyclotomic field. The outer action is related by the literal inner factor Ad(x^k).

At the inert prime over two, the direct Teichmuller roots of a give kappa_a(Frob4)=1 exactly. The roots assembled from lambda give -5. Their ratio is zeta_(3^n)^2, and the actions are transported by Ad(x^-2) on the left and Ad(x^2) on the right. This is retained as an explicit morphism; neither representative is silently substituted for the other. The evaluated Frobenius sends x to x^4, y to y^4 c^4 e^(-15/2), c to c^16 d^40 e^24, and d,e to their64th powers.

The local lifting calculation describes every cocycle on the actual pro-three tame group at K_2. Six Hall coordinates specify a lower section exactly when the displayed polynomial L vanishes. Its two central class-three errors R,S are evaluated as explicit integral polynomials. The correction operator is 64-4=60, so the complete obstruction is their image in (Z/3)^2. A successful lift has the exact inertia correction d^(-R/60)e^(-S/60). Every geometric-conjugacy fiber has81 elements, with translation group (Z/9)^2, because central unramified cohomology is Z3^2/(64-1) and the twisted lower stabilizer is zero.

The small family inertia y and Frobenius x^-1 c^N has error e^(5/2-4N). Exactly N=1 mod3 lifts. At N=1 the literal lift is inertia y e^(1/40), Frobenius x^-1 c. At N=0 the target lower section does not lift, despite having the same abelian coordinates. These are sections of the specified actual quotient. The commutative maps from the full intrinsic section sets and the exact geometric kernel are stated, so the theorem does not assume an intrinsic preimage of every target section.

## Executed certificates

- a_class3_frobenius.py: nine exact hexagon checks through degree3;48 general Hall-action checks, including integral rational three-adic inputs;25 affine composition checks; exact Frobenius images; exact inner transport from -5 to1.
- a_class3_local.py:100 independent comparisons of the collected Hall group law, inverse and Frobenius with the noncommutative Magnus algebra;639 actual lower tame sections and both central correction signs; six simple-family cases; exact positive lift with exponent1/40.

The programs use rational arithmetic and symbolic polynomials. The proof supplies the all-input group identities and the three-adic continuity arguments, rather than inferring them from the finite sample checks.

## Source and scope

Furusho's official original was opened, read, downloaded and hashed. Theorem2 equation(5), the proof in Section3, and Corollary12 were checked. The source is used for the exact three-cycle convention; the coefficient is derived in the text. The pre-existing genuine Galois action and path convention are those of D23, E31 and E35. The full-class-three integral Hall model uses the actual lower central quotients proved in E41.

This is direct progress on the evaluated higher Frobenius input in E44 and the section problem at Section51.16, scans172-178. It evaluates the rank-two class-three target reached by h. The remaining components of the rank-ten intrinsic action are retained by the explicit kernel in E54.2.

## Independent audit

The complete theorem passed B and root mathematical audits. B reran both programs with identical JSON and added code/bc_class3_symbolic.py/.out/.json, verifying every coefficient of L,R,S in all six variables, both inverse formulas, the exact60 central shifts, and the full simple example family. The separate audit is ledger/bc_e54_audit.md.

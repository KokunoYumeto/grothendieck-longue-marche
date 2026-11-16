# A61 independent full proof, source, and certificate audit

Verdict: PASS. DE read the complete 479-line candidate and its entire exact certificate, independently reran the certificate at p=3,7,11,19, and freshly opened both primary Silverman inputs. The retained independent output is notes/de_A61_rerun.out. No mathematical correction was required.

## The uniform operator argument

The quarter-rotation gives D^p=0 in every inert characteristic, including three: D^p is again an invariant derivation, while its rotation eigenvalue is the opposite of that of D. Hence E(b)=D^p(b)/p modulo p is genuinely well-defined on the reduced integral affine coordinate ring and commutes with D.

The multinomial proof of E(b^p)=−(Db)^p is complete. Apart from the all-ones distribution and the single p-th derivative terms, every cyclic orbit has length p and its multinomial coefficient is itself divisible by p. The all-ones term contributes Wilson's sign, and the single p-th derivative terms have the extra integral p factor. For E(R^(p+1)), every other distribution has a higher derivative of R divisible by p, so its contribution also vanishes after division. No false derivation rule for E is used.

The exact division differential identity follows by all principal parts and the zero Laurent constant at O. The evenness of the actual division polynomial, rather than an arbitrary primitive of its differential, supplies that constant term. Substitution gives the integral T=D²h/p and the displayed relation with x−x^(p²). Applying D^(p−2) and E(b^p) identifies DR=a; the small pole bound forces a to be constant, and a=0 would force an impossible function with a single simple pole. The oddness argument fixes E(h)=−R exactly.

The roots R,A,S are uniquely defined over F_p. The bound on E(R) gives A in L(2O). Applying E to h=R^(p+1)/a+S^p gives DS=RA/a because a^(p−1)=1 in the actual coefficient field. At a simple zero of R this makes S−S(P) have order at least two, so the p-th-power term starts in degree2p. The otherwise invisible degree-p Taylor coefficient is therefore proved to vanish; ordinary differentiation alone is not being used to infer it.

## Actual geometry and scope

The source division recurrence and multiplication formulas apply in general characteristic for a nonsingular Weierstrass equation. The characteristic-zero divisor is used only for the branch calculation. In characteristic p the actual Frobenius endomorphism identity, monic numerator, and relative primality force psi_p modulo p to be a nonzero constant; the odd recurrence at (0,0) fixes its sign. The direct point count gives supersingularity and specialization of all p-torsion to O.

The p simple zeros of R are exactly the three finite two-torsion points and the two points over every root of Q. The latter roots are simple and avoid all two-torsion abscissae. Unramified lifts ensure that each vanishing lower Taylor coefficient is divisible by p itself. Both the ordinary-centre and two-torsion algebraic charts have the stated unit derivatives and invertible generic coordinate changes. Their reductions are actual integral Artin–Schreier curves; the scaled lower terms have strictly positive valuation. The infinity uniformizer gives the claimed different and tail genus without relying on a genus pattern.

Positive-genus persistence uses the already audited common regular resolution argument of A52/A58/A60. The main genus plus all p tail genera exhausts the exact characteristic-zero genus, so the stable graph is a tree and all remaining components are rational. The actual map to the good elliptic model has its entire degree on the main component. Consequently the tails lie over their finite centres and all cusps over O lie on a single rational marked tree. This gives exactly the hypotheses of A41/A42. The genuine Heisenberg deck group is obtained from actual translation lifts; its exponent-p assertion uses the invariant p-th-power homomorphism and the invertibility of [i]−1. A59 then supplies the normalizer assertion. No full-cofinality or unramified-cover theorem is imported into the ramified chart calculation.

## Independently reopened primary sources

- verified: Silverman, The Arithmetic of Elliptic Curves, second edition, Exercise III.3.7(a)–(d), printed105–106, primary https://www.math.ens.psl.eu/~obenoist/refs/Silverman.pdf . References turn965view0/1 and turn966view0. The exact exercise begins with a general Weierstrass equation; the short-form parenthesis is optional and imposes no characteristic-three restriction. Parts(b),(c),(d) give the monic numerator, relative primality and actual multiplication formula.
- verified: Same primary, Theorem V.2.3.1(b), printed142, references turn965view2 and turn966view1. It states the relation in the actual endomorphism ring. The proof explicitly uses degree to turn the Tate-module characteristic polynomial into equality of endomorphisms.
- The Liu positive-genus persistence and actual-map extension inputs, Crew's one-branch-point formula, and A41/A42/A59 were previously fully audited at the identical application scope; the new uniform chart and marking hypotheses were rechecked here.

Independent certificate output: p3 gives three genus3 tails and genus10; p7 seven genus21 tails and genus148; p11 eleven genus55 tails and genus606; p19 nineteen genus171 tails and genus3250. Every exact differential, Frobenius-root, lower Taylor coefficient, hidden degree-p coefficient, valuation and genus assertion passed. These finite checks support the uniform proof and are not used as its substitute.

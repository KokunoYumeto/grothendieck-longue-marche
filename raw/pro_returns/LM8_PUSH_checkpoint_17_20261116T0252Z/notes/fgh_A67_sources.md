# A67 primary sources and actual-model gates

Status: registered after full root and DE proof/source/executed-certificate audits PASS. Full proof in fgh_A67_draft.tex; executed exact certificate fgh_A67_certificate.py/.json/.out. Complete independent audit ledgers: notes/root_A67_audit.md and notes/de_A67_audit.md.

## Primary inputs

- **verified:** Silverman, *The Arithmetic of Elliptic Curves*, Proposition VII.5.5, printed197, and its proof's characteristic-two reference on printed199 to Appendix A.1.4(b). Primary URL: https://www.math.ens.psl.eu/~obenoist/refs/Silverman.pdf . Fresh opening turn1050view0; exact statement and surrounding proof turn1055view0 and turn1056view0; Appendix page424 (printed413) requested at turn1056view4. The input is potentially good reduction iff integral j, with residue characteristic two included. The complementary elliptic j value is derived from an actual map in the proof and certificate.
- **verified:** Serre–Tate, *Good reduction of abelian varieties*, Theorem1 and Corollary2, printed493. https://wstein.org/papers/bib/Serre-Tate-Good_Reduction_of_Abelian_Varieties.pdf . Fresh PDF opening turn1050view1, exact printed493 page requested at turn1055view1/turn1056view3; primary theorem text had already been read in turn1019search12 and independently reopened by root at turn1032view2. Used for actual isogeny/norm quotients of Jacobians, not for potential good curve reduction.
- **verified:** SGA1, Exposé XIII2.9–2.12, especially the prime-to-residue specialization equivalence and inertia comparison. https://arxiv.org/pdf/math/0206203 . Fresh opening turn1056view1; exact XIII2.9/2.10 at turn1058view0/1; actual specialization morphisms, XIII2.11 inertia, and XIII2.12 at turn1059view0. These give good proper reduction of the actual order-dividing12 cover at coefficient primes at least5. They are not invoked at residue3 for the wild quotient.
- **verified:** Liu, *Algebraic Geometry and Arithmetic Curves*, Theorem9.2.2/Proposition9.2.5/Theorem9.2.7, printed395–397, and Remark10.4.24, printed542. https://rexresearch1.com/GeometryLibrary/AlgebraicGeometryArithmeticCurvesLiu.pdf . Fresh opening turn1056view2, factorization passage turn1059view1, exact Picard/Néron comparison turn1059view2. The 9.2.5/9.2.7 exact text was also freshly read for A65 at turn1021view2, root turn1038view1. Used for domination/resolution and compact-type graph rank. The wild exceptional components are proved rational by genus exhaustion, not by assuming every wild quotient singularity has rational resolution.

## New arguments proved directly

1. Actual Tate normal coordinates are constructed from the inflection tangent at a rational point of order3.
2. The two translated x-functions, their product, and both summed isogeny coordinates are derived from the addition law. The target cubic and j1728 condition are verified exactly modulo the source equation.
3. The complementary elliptic map of the actual genus2 double quotient is explicit. Its j is 4608±2688sqrt3, giving good supersingular reduction at2 after extension.
4. Every A4 closure is included by the split F2[C3] residue sequence. There is one standard two-dimensional summand; the unramified two-dimensional summand is trivial and cannot create additional equivariant quadratic twists.
5. At3 only the chosen P and -P formal displacements are used; no false uniform radius assertion for all E'[3] occurs. Vertical orders of the actual Kummer functions vanish by the graph Laplacian. The tame V4 normalization gives an actual rational centre plus four supersingular elliptic tails.
6. The residual centre u=(v²+1)²/(v³-v) is exact. C3 has quotient w=v³-v, cusp values ±i, and node values0,∞. Its action is free at all six residual cusps.
7. For the wild C3 quotient, component residue fields are controlled by invariant characteristic polynomials. The centre has exactly k(w); the fixed elliptic tail has at most a pure Frobenius residue difference, hence remains genus1. The orbit of three tails gives another genus1 component. Genus2 and good Jacobian reduction exclude any extra positive genus or graph cycles. The two distinct marked points remain on the rational centre.
8. A42 supplies fixed inertia at all coefficient primes. A46 supplies normalizers at2 and3; A57 plus actual tame good models supplies all primes at least5. No pro-odd injection from the degree3 quotient is assumed.

Scope: all intermediates of every A4 closure, and its proper abelian quotient closures. No universal-cover or cofinality conclusion.

Canonical proof: sections/A_tetrahedral_covers.tex. Canonical exact certificate: code/a_tetrahedral_covers.py/.json/.out. The original candidate and outputs remain intact.

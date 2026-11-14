# Independent audit of D.6–D.9

**Verdict: passes.** The homotopy degrees, the Moore-space counterexample, the normalized fifth-stage invariant, and the mapping-space action in the classification are correct. No change of status or added hypothesis is required.

## D.6: fourth Postnikov stage and sign

Let `P` be the homotopy pullback of the Pontryagin square `K(Z/2,2) → K(Z/4,4)` and reduction `K(Z,4) → K(Z/4,4)`. The homotopy long exact sequence gives

- `pi2(P) = Z/2`;
- `pi4(P) = ker(Z → Z/4) = 4Z`, identified with `Z` by the fibre coordinate;
- all other positive homotopy groups vanish.

The characteristic relation has the correct sign for `p1(E) = -c2(E complexified)`: restriction to the universal oriented two-plane bundle gives both sides equal to the reduction modulo four of the square of its first Chern class. The restriction in degree four is injective by the oriented sphere-bundle Gysin sequence, whose possible kernel comes from degree one of the simply connected base. Thus the universal relation is proved without importing the differing convention in the Antieau–Williams formula.

The induced map from `BSO(3)` is an isomorphism on `pi2`. On `pi4`, its integral characteristic coordinate is multiplication by `-4`, by the adjoint Chern-root calculation. Its image is exactly the kernel `4Z`, so it is also an isomorphism on `pi4`. Consequently this is the fourth Postnikov stage. The equivalent fibre description uses the degree-five Bockstein of the Pontryagin square, as stated.

Maps into this pullback include the chosen homotopy between the two degree-four characteristic maps. Equality of their cohomology classes guarantees existence of that datum but does not determine its homotopy class. This distinction is necessary in D.7.

## D.7: four bundles on the Moore space

For `S = S3 union_4 e4`, the integral cellular cochain map from degree three to degree four is multiplication by four. Hence `H4(S;Z) = Z/4`, while `H1(S;Z/2) = H2(S;Z/2) = 0`.

Every oriented three-plane bundle therefore has a spin lift, and the lift is unique up to isomorphism. Bundles for `Spin(3) = SU(2)` on this four-dimensional CW complex are classified by `c2` in `H4(S;Z)`, because `BSU(2)` is three-connected and its fourth homotopy group is infinite cyclic. There are exactly four isomorphism classes. Their associated oriented three-plane bundles remain distinct, while `p1 = -4 c2 = 0` and `w2 = 0` for all four.

The explicit unqualified uniqueness sentence in Definition 2 of the opened Antieau–Williams version is therefore contradicted. This does not invalidate the separate homotopy-pullback and low-cohomology computations used in D.6/D.8. I inspected the primary Dold–Whitney introductory page: it expressly warns that characteristic classes alone do not classify bundles over arbitrary four-complexes and retains additional difference data. Thus the qualification in D.7 is supported by the original source.

## D.8: degree-six invariant

The next homotopy group is `pi5 BSO(3) = pi4 S3 = Z/2`. Thus the next Postnikov fibre is `K(Z/2,5)` and its classifying invariant lies in degree six on `P`, not in degree five.

The mod-two cohomology calculation is consistent in every degree used. In the base `K(Z/2,2)`, the generators through degree six are `x` in degree two, `y = Sq1 x` in degree three, and `z = Sq2 Sq1 x` in degree five. In the fibre `K(Z,4)`, the relevant classes are `v` in degree four and `Sq2 v` in degree six; `Sq1 v = 0`. The differential `d5(v) = z + xy` removes `xv` by `d5(xv) = xz + x2 y`, a nonzero base class.

The Steenrod identity is exact: `Sq2 z = Sq2 Sq2 y = Sq3 Sq1 y = 0`, and Cartan gives `Sq2(xy) = x2 y + xz`. Hence `Sq2(z+xy) = x(z+xy)`, which is already a `d5` boundary when it becomes the possible transgression of `Sq2 v`. Compatibility of squares with transgression is explicitly stated in the primary Serre text, Section 2, no.7 and the proof of Theorem 2. The stated survival and the three-dimensional degree-six group follow.

There is also an independent way to verify the survival without depending on any shorthand about spectral-sequence pages. The abstract fifth-stage invariant pulls back along the spin cover to the fifth-stage invariant of `BSU(2)`. The latter is nonzero: if its `K(Z/2,5)` extension over `K(Z,4)` split, the nonzero class `Sq2 rho2 iota4` would survive in degree six, whereas `BSU(2) → P5 BSU(2)` induces an injection from degree-six cohomology of the target and `H6(BSU(2);Z/2)=0`. Therefore the actual invariant on `P` restricts nontrivially to the fibre. Together with the two independent classes pulled back from `w2^3` and `w3^2`, this proves the asserted dimension and kernel of restriction. This is the same independent argument used in the primary Antieau–Williams Corollary 3.

The normalization uniquely specifies the invariant. Two classes with the prescribed fibre restriction differ by `lambda x3 + mu y2`. Pullback to `BSO(2)` kills `y` and detects `x3`, forcing `lambda=0`. For the diagonal Klein-four representation, direct expansion gives `x = a2+ab+b2` and `y = a2b+ab2`. Thus `y2 = a4b2+a2b4` is nonzero and forces `mu=0`. Existence follows because the actual invariant pulls back to zero along both representation maps, which factor through `BSO(3)`.

The representation maps here are the ones induced through the Postnikov map constructed in D.6. They carry their actual homotopy data; merely giving their characteristic pairs would not suffice on arbitrary sources. The present wording uses these actual induced maps and is correct.

## D.9: classification and the loop action

The map `BSO(3) → P5 BSO(3)` has five-connected fibre. A map from a five-complex lifts, and a homotopy of such maps lifts relative to the ends because the corresponding relative cells have dimension at most six. Thus it gives a bijection on homotopy classes from all CW complexes of dimension at most five, including complexes with infinitely many cells.

For a fixed actual map `f:S → P`, the nullhomotopies of `u f` have components forming a torsor under `H5(S;Z/2)`. The degree-six obstruction vanishes by dimension. When the base map is allowed to vary in its homotopy component, a loop `F:S times S1 → P` acts by translation by the slant product `F* u / [S1]`. This is precisely the homomorphism induced on fundamental groups by `Map(S,u)` into the mapping space of `K(Z/2,6)`.

Consequently the fibre over the component `[f]` is a torsor under `H5 / image(delta_f)`. The quotient is necessary, and D.9 includes it. Since the target Eilenberg–Mac Lane space is an abelian group object, this action is by translations; there is no additional nonabelian linear action omitted from the formula. The independent orientation factor is justified by the actual group splitting `O(3) = C2 times SO(3)`, with the stated adjustment `w2(E) = x+a2`.

Finally, for `S5`, the fourth-stage map is null and its mapping-space loop contribution is zero, leaving exactly `Z/2` in degree five, as required by `pi5 BSO(3)`. The degree shift and the simplest test therefore agree.

## Primary sources checked directly

- Antieau, B., & Williams, B. (2013 revision). *On the classification of oriented 3-plane bundles over a 6-complex*. arXiv:1209.2219v2, 30 August 2013. https://arxiv.org/pdf/1209.2219 . Complete four-page text opened; fourth-stage model, Definition 2, spin-cover argument, and Corollary 3 checked independently.
- Dold, A., & Whitney, H. (1959). Classification of oriented sphere bundles over a 4-complex. *Annals of Mathematics, 69*(3), 667–677. https://webhomes.maths.ed.ac.uk/~v1ranick/papers/doldwhit.pdf . Introductory page 667 inspected as an image, including its explicit warning and torsion-qualified theorem.
- Serre, J.-P. (1953). Cohomologie modulo 2 des complexes d’Eilenberg–MacLane. *Commentarii Mathematici Helvetici, 27*, 198–232. https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Serre-SESM.pdf . Section 2, nos.7–10, especially Theorems 2 and 3 and the transgression discussion, checked in the primary full text.

No new numerical test is needed for this audit. The claims at issue are homotopy-fibre, obstruction, and cohomology statements; the previously executed polynomial and cellular checks are consistent with these independent arguments.

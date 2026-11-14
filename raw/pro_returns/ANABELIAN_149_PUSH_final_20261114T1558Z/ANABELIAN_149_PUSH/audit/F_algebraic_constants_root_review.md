# Root review of F.45

Date: 14 November 2026. Reviewed source: `audit/F_algebraic_constants_function_fields_candidate.md`, including its revised high-degree argument and primary-literature comparison. The independent review is `audit/F_algebraic_constants_degeneration_review.md`.

**Decision: accept in the stated positive-transcendence scope.** This is an additional sufficient reconstruction class, not the necessary-and-sufficient classification requested in F2. The convention is the actual closed-point-preserving relative convention. The literal relative-only convention remains refuted.

## Field predicates and detection

For a finitely generated positive-transcendence extension L of Qbar, every finite extension has the same algebraically closed constant field. Divisors on a normal proper model identify the intersection of all power subgroups with Qbar*. Both directions are proved: valuations kill the divisor of an infinitely divisible element, properness makes it constant, and algebraic closedness supplies all roots of each nonzero constant.

The exact Hilbert input was independently opened by root in Bary-Soroker and Paran's author PDF, Theorem 1.2 and Corollary 3.2. It applies to every finitely generated transcendental extension of an arbitrary field. It therefore applies here despite the algebraically closed constant field. The full connected composite cover, rather than only its geometric component, is specialized to one field. The intermediate fibre is then one closed point and its residual torsor is connected. Riemann–Roch provides unbounded degrees. The cover-preserving curve reduction retains the arithmetic constant factor. Thus every finite arithmetic quotient is detected, which is the input required by the later spanning argument.

All finite data descend to a finitely generated field F over Q with L = F Qbar. This gives the normal subgroup G_L of G_F. The infinite Kummer class is not asserted to descend at this stage; only its finite geometric data do. The later equivariance argument uses finitely many actual point values to descend the relevant functional.

## Moved divisors and integrality

The equivariant affine model exists by adjoining the finite orbit of generators and normalizing. Its smooth locus and the complements of prescribed zero and pole divisors have a nonempty invariant intersection. A nonidentity automorphism has a proper fixed locus. On an affine open containing two distinct points z and sigma(z), CRT prescribes a nonzero linear term at z and a nonzero value at sigma(z). The unique divisor component through z is smooth there and is moved by sigma. Repeating after removing full finite orbits gives pairwise distinct valuation pairs.

All finitely many choices descend to one finite normal extension of the number-field constants. Components through rational smooth points can be followed without changing multiplicity. The separate semilocal Dedekind-ring argument is essential: it proves CRT for the chosen divisorial valuations without making the false claim that height-one ideals in an arbitrary higher-dimensional affine ring are already comaximal.

The central improvement is valid. A geometric DVR contains its constant field and is trivial on it. Tensoring with a finite separable extension of constants is finite étale, and every localized prolongation is an unramified DVR. A compatible prolongation through all algebraic constants therefore still has value group Z. Every individual element lies in a finite constant extension; no value with a new denominator appears in the union.

A missing finite geometric extension exists because L is Hilbertian. Taking a finite normal descent field M gives a nonidentity automorphism of M Qbar over L which fixes Qbar and preserves M. The valuation construction makes each P_i(alpha) have valuation one at its designated place and the other factors and all P_i(sigma(alpha)) have valuation zero. Evaluation and Galois equivariance give the level-n power relation. Applying one fixed integer-valued prolongation to this relation for every n makes each profinite coefficient an ordinary integer. This uses neither an unbounded sequence of norm fields nor an unproved bound on arithmetic ramification.

## Albanese, residues, and actual point functions

The integral Albanese comparison has the correct direction: its finite kernel disappears under Hom into a torsion-free Tate target. After normalization at the rational basepoint, roots of unity in L make the scalar Kummer class a homomorphism. Failure of the point Kummer images to span the coinvariants would produce a finite quotient trivial on every decomposition group, contradicting the detection theorem above.

Finitely many spanning images and their actual values lie in a finitely generated M over Q. Normality of G_L gives an action on the coinvariants; the conjugation coboundary dies there. Actual Kummer values transform by the cyclotomic character, so the geometric functional is G_M-equivariant. Jannsen's integral Tate-Hom theorem is applied over this finitely generated M. It is not applied directly over Qbar or L. Splitting the boundary components and normalizing at the basepoint fixes one unit lattice. Rational-line norms and transverse curves then force all residues to be ordinary integers. The injective integral divisor matrix forces the unit exponents to be integers as well: a rational number lying in the integral completion is an integer. Finite-level Hochschild–Serre and evaluation at the basepoint remove the remaining constant class.

The high-degree argument in the actual point-function step is exact. If a nonconstant function h has h(x) in L, the degree of x is at most the degree of the finite map h. Therefore a sufficiently high-degree point has h(x) outside L and in particular outside Qbar. The inverse-image open of T minus b is shown nonempty before choosing such a point. A nonzero rational function cannot have a zero of degree larger than its total pole degree, so the affine relation between the recovered units follows. Its coefficients lie in Qbar, allowing scalar comparison at nonconstant values. The T minus b argument then treats algebraic values without an unproved density assertion.

In the constant case, positive transcendence degree supplies beta in L with beta/h outside Qbar. Every closed-point image avoids beta, so the inverse image is empty. The recovered unit for T minus beta has all values in L; unbounded point degrees force it to be constant. Comparing its ratio with the original ratio proves equality of the actual point function. This is precisely where the algebraic case would fail, and the theorem excludes it.

Smooth curves through a prescribed point and the rational basepoint give the higher-dimensional comparison. Equality of their Kummer classes makes the quotient unit infinitely divisible; its divisor is zero and its normalized value is one. CHW Theorem 4.18(5) therefore applies in its exact stated scope and supplies the all-scheme result.

## Subfields, strictness, and source boundaries

For a positive-transcendence subfield k0 of L, K = k0 Qbar is finitely generated over Qbar. A transcendence basis B for K puts K inside the finite relative algebraic closure of Qbar(B) in L. The extension K/k0 is algebraic, so F.32 gives descent. This does not assert descent along a transcendental extension and does not include the algebraic subfield Qbar.

The strictness example Qbar(t) is outside F.44's virtually proper-formation class. Its normal closure over any finitely generated algebraic model has a quotient equal to the absolute Galois group of a number field. Every open subgroup of the latter has arbitrarily large symmetric quotients, incompatible with any proper hereditary extension-closed formation containing cyclic groups. Hence F.45 is a distinct sufficient mechanism. In particular it also proves that reconstruction is not preserved under arbitrary subfields.

The source comparison does not make a priority claim. The current Carlson–Stix and CHW statements retain their own sub-p-adic, finite-generation, or amenability hypotheses. The Bary-Soroker–Paran author-PDF date and arXiv-header discrepancy is recorded rather than silently identifying versions. F.9 remains unresolved.

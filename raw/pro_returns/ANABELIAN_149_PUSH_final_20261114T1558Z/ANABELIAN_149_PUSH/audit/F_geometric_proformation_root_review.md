# Root review of F.46

Date: 14 November 2026. Reviewed `audit/F_geometric_proformation_candidate.md`, Sections 1–10, including the geometric normal-closure equivalence. The independent degeneration review is retained separately.

**Decision: accept the stated sufficient class and its equivalent arithmetic description.** This combines F.44 and F.45 for positive-transcendence fields. It does not provide the necessary-and-sufficient classification of all reconstruction fields requested in F2; F.9 remains unresolved.

## 1. The two descent fields must be distinct

Choose D finitely generated over Q with K0 = D Qbar. An automorphism fixing D preserves K0 and carries each finite Galois C-extension of K0 to another such extension. Hence the maximal extension k is normal over D, even though its total arithmetic Galois group need not be pro-C.

For any finitely generated L/k, all finite data can be put in a finitely generated F/Q with D contained in F and L = Fk. Thus L/F is Galois. On the different base B = F Qbar, the extension L/B is genuinely pro-C by base change from k/K0. B is a finitely generated positive-transcendence extension of Qbar, so the independently opened Bary-Soroker–Paran theorem makes it Hilbertian. These are exactly the two separate facts required later. The proof never treats Gal(L/F) as pro-C.

## 2. Divisibility and missing finite extensions

The formation assumptions contain all finite abelian groups and are closed under extension, so adjoining roots of all conjugates of an element in a finite C-extension stays within k. This proves radical closedness.

For E/k finite and an infinitely divisible a in E, choose one finite normal M/D containing a and with E contained in Mk. Every chosen root z_n remains in Mk. If sigma fixes k and tau fixes M, they commute on both M and k: normality of M/D and k/D preserves the relevant factors. Since sigma fixes every root of unity, sigma(z_n)/z_n is tau-invariant, hence belongs to M. Thus sigma(a)/a is an nth power in the same finitely generated M for every n. Its divisible kernel is trivial by the earlier divisor and number-field argument. Therefore a is fixed over k. A normal proper model and the finite relative algebraic closure extend the conclusion to every finitely generated L/k.

The missing extension is geometric. Hilbert irreducibility over K0 supplies arbitrarily large symmetric extensions. The maximal C-intersection is exactly the quadratic subextension because C contains cyclic groups but excludes all sufficiently large alternating groups. The residual extension over k has group A_n. A finitely generated L/k has only a finite relative algebraic constant extension, so it cannot contain these residual fields of unbounded degree. This gives an automorphism fixing k but moving a finite geometric extension, as required by the divisor construction. No missing algebraic number-field constant is asserted.

## 3. Finite arithmetic quotient detection

The balanced-pencil argument is made over B, not over F. Its characteristic-zero geometry, literal symmetric subgroup and support-at-most-two base elements are exactly the conclusions proved in F.24. The finite cover stays connected over B because its base change to L is connected. Its finite constant field M has M intersect L equal to B.

Full-group specialization over the Hilbertian B gives H. Since L/B is Galois pro-C, the actual residual quotient H/J is in C. This implication is valid after specialization; it is not inferred merely from a geometric subgroup before specialization. Simplicity and subgroup closure force A_n inside J. The commutator calculation then returns each support label to every coordinate. The selected-coordinate stabilizer maps onto the geometric kernel N, and surjectivity to the constant quotient P plus an even permutation gives surjectivity to the full arithmetic group G. The alternating subgroup makes the block action transitive, so the detecting point has unbounded degree as the pencil degree grows.

The curve reduction for a higher-dimensional source retains the arithmetic component action. This proves precisely the decomposition-group detection used in the later functional span, including nongeometrically connected finite covers.

## 4. The fixed finite norm field

A finite Galois M over a rational Q-field contains the descent data, puncture roots and a finite descent of a missing geometric extension. A nonidentity sigma fixing L preserves M and fixes Qbar. F.45's moved-divisor construction therefore applies. Adding the required finite constants changes neither Mk nor the action of sigma on k.

The actual value b_alpha lies in one field F' = M S0, with S0/D finite inside k. This field is fixed before the radical level n is chosen. For a in F' having an nth root z in Mk, every tau fixing F' commutes with sigma on M and k; the roots of unity lie in k and are fixed by sigma. Hence sigma(z)/z belongs to F', and sigma(a)/a is an nth power in F'. Applying this to the evaluated Kummer relation gives its nth-power relation in F' at every level.

The character v_i composed with the norm from F' to M is integer-valued. On each puncture ratio it is minus [F':M] times the corresponding coordinate. It therefore proves that [F':M] times the profinite exponent is an ordinary integer. An element of the integral profinite completion with this property is itself an integer, as can be checked in every Z_l. The degree is independent of n, which is indispensable.

The proof explicitly does not extend F.45's unramified-constant valuation argument through the geometrically ramified pro-C extension. The fixed finite norm field repairs exactly that issue.

## 5. Albanese and point-function reconstruction

The arithmetic equivariance uses the normal subgroup G_L of G_F, with F finitely generated over Q. It does not require the quotient Gal(L/F) to be in C. Finite arithmetic quotient detection makes the projected point Kummer images span the relevant Tate coinvariants. A finite spanning collection and its actual values descend to one finitely generated Q-field M. Conjugation corrections vanish in the coinvariants, and actual multiplicative values transform by the cyclotomic character. This gives equivariance over M and permits Jannsen's original integral Tate-Hom theorem there.

The normalized unit lattice is common to all coefficient primes after splitting the boundary. Norms to punctured lines and transverse curves reduce the residue problem to the already checked fixed-field argument. The integral divisor matrix gives actual integral exponents; Galois descent and finite-level Hochschild–Serre remove the residual constant class.

The remaining divisible ambiguity is k*. High-degree points outside L give the affine unit comparison in the nonconstant case; the translated unit handles values in k. In the constant case, a missing geometric extension supplies beta/h outside k after one finite extension. This is sufficient, and all preceding predicates are stable under that finite extension. The closed-point comparison gives the geometric-point function needed by CHW Theorem 4.18(5), which supplies the full topos assertion.

## 6. Positive-transcendence subfields and the equivalent class description

For k0 contained in L, choose a nonempty finite transcendence basis T and put A = Q(T). The relative algebraic closure R of A in the finitely generated F is finite over A, and F/R is regular. For a in k0, regularity identifies the R-conjugates with the F-conjugates; normality of L/F puts the normal closure N/R inside L. Base-changing regularity to R Qbar gives N Qbar intersect F Qbar equal to R Qbar. Its Galois group is therefore a finite quotient of Gal(L/F Qbar), hence belongs to C. This embeds k0 in (R Qbar)^C. That containing field is algebraic over k0, so F.32 applies. The positive-transcendence hypothesis ensures the core theorem applies to R Qbar; algebraic subfields are excluded.

Section 10 correctly characterizes this embedding class. An open pro-C subgroup of the geometric normal-closure group has a finite fixed field over F0 Qbar, giving the required finitely generated geometric base. Conversely there are only finitely many conjugates of (R Qbar)^C over F0: each is determined by a conjugate of the finite field R. Before claiming pro-C, the proof explicitly composes each conjugate with R' Qbar. Their compositum is pro-C over that finite geometric base, and the desired normal closure is a quotient. This proves virtual pro-C for the geometric group, without imposing it on the total arithmetic group.

Taking the cofinal classes excluding one alternating subquotient gives the stated equivalent description of the union of sufficient classes. It is not a necessity statement for arbitrary reconstruction fields.

## 7. Strictness and boundaries

The field Qbar(t)^solv is radically closed and contains a transcendental element. If it embedded into a finitely generated extension E/Qbar, divisibility would put that transcendental element inside D(E*) = Qbar*, a contradiction. Thus it lies outside F.45. It also lies outside every F.44 class, because its total arithmetic normal-closure group has a number-field absolute Galois quotient, whose open subgroups admit arbitrarily large symmetric quotients. The combined theorem includes the positive-transcendence instances of both earlier mechanisms but does not replace the earlier positive algebraic-number-field cases.

The proof is mathematical and has no new finite numerical assertion requiring a separate computation. Its new use of the Hilbertian theorem remains within the already opened exact hypotheses. The candidate records a bounded literature search and makes no priority claim. Integration is approved after the independent reviewer has recorded the same conclusion.

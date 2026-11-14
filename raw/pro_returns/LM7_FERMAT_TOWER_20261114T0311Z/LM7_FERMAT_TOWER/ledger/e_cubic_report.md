# Cubic supplement: E.24, E.25, E.28

## Files completed

- sections/E_cubic.tex contains all three statements and full proofs.
- ledger/e_cubic_results.json contains the three matching result records.
- ledger/e_cubic_refs.bib contains only the three additional, verified bibliography keys EC_LiLongTu, EC_CoatesWiles, EC_CiperianiStix.
- code/e_cubic_abelian.py, .out, .json check the Weierstrass identity, cusp-frame relation, toric retraction, Smith presentations, eta coefficients against point counts, and D8 lift squares.
- code/e_cubic_class2.py, .out, .json check the finite cubic obstruction: all19683 elements, all729 central lift pairs, and exact arithmetic modulo109.

## Completed mathematics

E.24 computes the entire intrinsic geometrically abelian section set of the plus cubic, with its actual map to the rank-two minimum. The essential algebraic calculation is a retraction of the generalized Jacobian G onto Gm squared, defined by the coordinate units. Its kernel G' is an extension of the Fermat elliptic curve E by three copies of the restriction-of-scalars torus from Q(zeta3). The exact relation for a rational lift of a generator of E(Q) is

3z' = (lambda^-1, lambda^-2, zeta3^2 lambda^-3).

The primitive coefficient of the first lambda generator gives G'(Q) = mu6 cubed plus a countable free group. The analytic-rank-zero input is proved with the strictly positive eta-product Mellin integral. Coates-Wiles then gives algebraic rank zero; reduction at2 and the exact Weierstrass model show E(Q)=Z/3. Ciperiani-Stix Theorem18(2), in its exact unrestricted maximal-Div assertion, gives Div H1(Q,E)=Q/Z. The extension class is killed by3 and its torus has H1=0, so this divisible subgroup transfers to G'. Kummer inverse limits compute every section and fiber. The completion is explicitly the limit over multiplication by m and has the restricted-sequence, prodiscrete topology; no infinite discrete quotient is treated as finite or compact.

E.25 defines the Galois-stable markings required by an intrinsic depth filtration, and gives the precise quotient map and its kernel to inherited depth. Rational inherited depth is the split base quotient at every Fermat level. Integral inherited depth at every even level has a D8 pullback obstruction with class kappa2(-1) cup kappa2(-1). Both lifts of real conjugation have order4, so there is no section. The same finite quotient factors through the curve's own geometric abelianization, proving the all-even intrinsic assertion. It also compares marked depth and the third derived quotient by their actual common quotient and explicit noninclusion words.

E.28 gives a genuine cubic nonabelian result. The entire nonempty abelian fiber over the pro3 Kummer pair (6,109) fails to lift even to class two. The inherited class-two lattice has bracket multiplier9. Modulo27, at the local prime109, the Galois action is trivial. Every possible pair of lifts of the Kummer Frobenius and inertia values has nontrivial commutator9C, while the tame relation requires commutativity because the finite group has exponent27. This is a finite exact contradiction and uses no unresolved inverse-limit H2 identification. It applies to intrinsic class two, intrinsic metabelian, marked intrinsic depth, and inherited integral class two through the displayed maps. It is not applied to rational Q3 unipotent depth: that group has no reduction map extending the finite quotient.

## Independent checks

The A-structure agent independently audited the maximal-Div transfer, both inverse-limit vanishing arguments, the algebraic toric retraction and its basepoint translation, and the mod27 cubic obstruction including the covering divide-by3 map and the tame local relation. All passed after clarifying completion topology and tangential origins. The root owns the final combined audit and assembly.

## Exact remaining scope

These results complete the cubic abelian calculation, all-even integral nonexistence in the indicated quotients, and the stated nonempty cubic fiber obstruction. They do not supply the entire intrinsic rank10 pro3 class-two section set, the intrinsic metabelian section set, or the intrinsic marked-depth section set at the cubic. In particular the arbitrary completed toric pairs passing E.28 and the dependence on the extra rank8 abelian directions still require classification of the actual higher Galois action and its cocycles. The A-structure agent is separately studying all rational toric pairs in the inherited class-two quotient; that work must be tracked under its own statement and cannot by itself complete the intrinsic rank10 problem.

The independent audit of E.16--E.21 passed, including the real comparison in E.18. The finite-etale real comparison uses complex Riemann existence plus effective real descent, so no real rational point is assumed. E.5--E.15 audit is being continued, with E.10 prioritized.

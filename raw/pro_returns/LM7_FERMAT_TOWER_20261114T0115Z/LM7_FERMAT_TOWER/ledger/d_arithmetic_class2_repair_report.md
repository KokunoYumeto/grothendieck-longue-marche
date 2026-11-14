# D.57: actual arithmetic class-two repair

## Outcome and exact scope

D.57 constructs an actual continuous peripheral automorphism of

`X_* = Bhat / (R_h ∩ M_* ∩ L_{*,2})`.

It fixes `t`, has multiplier one, induces exactly the prescribed D.49 action on `W_h`, and gives an automorphism of the full class-two exponent-four quotient of the actual rank649 kernel over the actual order3888 arithmetic base. The underlying integral homology source is retained; its particular D.50 homology action is replaced by the repaired action. The normalized parameter still maps to the literal `f_h*`, through the existing metabelian and CM comparison maps.

This is an actual arithmetic quotient of the original source. It is not inferred from the separate order1080 calculation. The original full G3 invariant equation and the genuine full profinite GT0 realization remain unfinished.

## The marked genus-three source

The exact 48-state quotient is the deck group of

`C: y^4=x^3+1`,

with Belyi map `(x^6+20x^3-8)^2/(64(x^3+1)^3)`. The literal generators are

`s(x,y)=((2-x)/(x+1), sqrt(3)y/(x+1))`,

`r(x,y)=(zeta3*x,y)`.

All48 quartic automorphisms and all96 ordered marked edges are checked. The branch patterns are `2^24`, `3^16`, `12^4`; the cover has genus3 and four removed cusps, hence free rank9.

The map to the previously marked elliptic source has degree8. It is the degree2 map `(x,y)→(x,y²)` followed by multiplication by2 on `Y²=x³+1`. Explicitly

`u=x(x³−8)/(4(x³+1))`,

`v=(x⁶+20x³−8)/(8y⁶)`.

The target satisfies `v²=u³+1`, and the original Belyi map is `v²`. The generator images are exactly `(u,v)→(u,−v)` and `(u,v)→(zeta3*u,v)`. This proves that `t²` is the stated `zeta3²` CM operator. Two additional explicit elliptic quotient maps give the complementary CM factors with coefficients `3±2sqrt(3)`; the three pulled-back differentials prove the Jacobian isogeny.

The rational rank9 centralizer has dimension5, with constituents of dimensions2,3,4. The actual h action on the quartic CM constituent has finite order by the finite Hom-lattice action and the trivial inertia3 action on the two-adic Tate module of `y²=x³−x`. Its scalar is therefore in `mu4⊂Q2(i)`. This is a two-adic proof. The earlier attempt to infer a scalar from the ramified three-adic quotient was abandoned and preserved.

Exactly two of the four resulting rational matrices preserve the integral rank9 lattice. They are the quarter-turn branches `J` and `J³`, with the same exact elliptic scalar `(-3−8zeta3²)/7`. The even quarter-turn candidates have the actual entry `−1/14`. Both integral branches are evaluated; neither is selected by an unproved arithmetic assumption.

## Actual boundary spaces and equations

The actual order3888 marked graph has rank649, moving rank640, and compact rank326. Its 40 nonzero character pairs each have16-dimensional homology and a64-dimensional invariant exterior square. The complete invariant module has dimension2560. The marked augmentation relations have rank2486, so the central coinvariant space has dimension74.

The full norm has rank40, and the compact norm has rank6. The complete600-dimensional same-homology peripheral parameter space has local obstruction image of rank64. Thus the compact-norm kernel has dimension68 and retains a four-dimensional quotient after local correction. D.57 keeps that quotient in the equations. The quotient of all74 coordinates by the local image has dimension10.

The source contains exactly40 independent homology-derivation parameters. The certificate retains an actual complement in the full640-dimensional conjugator-pair kernel, all integral mod4 lifts, the74-to-10 quotient matrix, all40 linear coefficients, and all780 quadratic coefficients for each branch. The complete coefficient image has rank9; its exact annihilator is hexadecimal `0x5`, expressing coordinate0=coordinate2. Allten output coordinates remain in the recorded equations.

The saturated integral rank9 fixed lattices have ranks3 for s and1 for r. Their exact Smith transformations are retained. Every corresponding local obstruction and every doubled obstruction is zero; all moving/fixed polar cross terms are also checked. The eight s-framing cases are explicitly retained for each branch.

## Actual zeros and verification

For branch J, the fixed-seed search reaches mask `0xba190a8d71` at trial682. For branch J³, it reaches mask `0xdfd51862a6` at trial18. These searches establish existence; they do not claim a complete enumeration of all `2^40` parameters.

Every one of the16 framing cases has an explicit600-parameter local correction. The corrected cusp words have lengths114712–119132. Direct collection verifies zero abelian error and zero in all74 moving central coinvariant coordinates. Independent marked edge maps verify rank649, preservation of the full ribbon intersection form, commutation with both deck generators, and the exact rank9 arithmetic projection.

The printed words are not asserted to have a vanishing unrecorded plus-central coordinate. The proof supplies that step through the actual common quotient

`T_{*,2}/E_* ≅ G_* ×_{Q_*} J_{Q,2}`.

The prescribed W_h action on this quotient is exactly `(identity,h)`. Actual arithmetic conjugators are aligned through the onto exterior map to the plus-central module. This leaves the74 coordinates unchanged. The remaining error then lies in `Z_*`, and its zero coinvariant class is exactly the image of the two central cusp-correction maps. Those corrections make the cusp identity exact. The verified Frattini map proves generation. Higher integral homology corrections are fourth powers and retain the finite class-two action throughout the inverse limit.

## Programs and reproduction

Run in order from a directory containing the two immutable D.56 JSON inputs:

1. `d_arithmetic_rank9_seed.py`
2. `d_arithmetic_rank9_geometry.py`
3. `d_arithmetic_rank9_conjugators.py`
4. `d_arithmetic_invariant_module.py`
5. `d_arithmetic_local_transgression.py`
6. `d_arithmetic_affine_boundary.py`

Python3, NumPy and SymPy are used. All integer, rational, finite-field and Smith computations are exact. The sixth program also executes the local-transgression source in a nested mode; this rebuilds its mathematical state without overwriting the standalone fifth-stage certificate. The nested progress and timing are preserved in the sixth program's stdout.

The final manifest records every owned source, output, certificate and input hash. The author copies only the six sources and the two immutable inputs into a new directory, executes all stages, and compares the complete JSON and complete stdout after excluding only the explicitly named `elapsed_seconds` fields. No mathematical field is excluded.

## Remaining exact source maps

The full source kernel is `R_h ∩ M_* ∩ L_{*,2}`. It contains an actual nonzero commutator square, detected in the class-two exponent-eight quotient through the map `2 ubar∧vbar`. The exact source map from D.54 has kernel

`(R_h ∩ M_* ∩ L_{*,2}) / (R_h ∩ M_infty ∩ L_2)`.

The next task is to lift the new action across an actual further source quotient, starting with the full G3 integral homology source and retaining this solved class-two component. Full profinite realization is not claimed.

## Final author verification

All six final copied-source/input stages passed. Every complete JSON and stdout comparison matched after excluding only `elapsed_seconds`. The rref integrality exhaustion was strengthened before freeze: each solved coefficient has two-primary denominator at most2, and the program asserts the conservative bound4 before enumerating all1024 free residue tuples. Exact pre-change source/output/proof and the final diffs are preserved. Control-character, literal-command, environment and26-equation-tag checks pass. Parent/peer audit remains separate.

## Completed integration audit

D.57 evaluates the actual order3888 arithmetic boundary for both possible integral rank9 branches. Every one of the sixteen framing cases has a literal zero of the complete ten-coordinate polynomial. Its exact genus3-to-E3 map, exhaustive integral conjugator search, rank64 local image in74 coinvariants, separate plus-central alignment and augmentation correction give an actual automorphism of Bhat/(R_h intersect M_* intersect L_{*,2}), retaining the full D49 W_h action and prescribed parameter. The full G3 invariant equation and the full profinite source still require lifting across the explicit kernels.

The full root proof/source audit and fresh execution have passed. All exact outputs and source amendments are preserved; whole-paper rendering is a separate checkpoint.

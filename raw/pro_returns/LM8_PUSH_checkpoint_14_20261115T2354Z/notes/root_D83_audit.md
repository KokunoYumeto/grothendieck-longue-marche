# Root audit of D.83: a local image detects every finite class

**Verdict: PASS.** The complete notes draft was read, including the stronger finite-level localization isomorphism. No numerical search is needed for this theorem; its single logarithm residue is the already independently verified D.78 calculation.

## Exact images, including infinite support

Prime coefficients belong to c_0, while every chosen Kummer cocycle is integral. Thus the global cocycle series converges uniformly, not just pointwise. All local logarithm coefficients and all local integral coboundary primitives are bounded in Z_5. The local gauge is consequently a convergent sum in the closed away-five lattice L. Every away-five inertia supplies its entire corresponding pure translation line, while the global cocycle minus its Kummer-five graph coordinate takes values in L. These two inclusions prove the exact global image. D.82's actual descent of Kummer-five and D.78's local surjection and primitive unit kernel prove the exact local image. A gauge in L preserves the global subgroup. Hence the stated equality L=Z_5 z makes the actual local and global operator images equal, including zero and nonsaturated lattices.

This proof uses no formal enlargement of an arithmetic image. The graph complement remains present throughout, and no division by the generator of L occurs.

## Finite Sha and localization

The finite affine-image Chebotarev argument proves that a globally locally trivial finite cocycle vanishes on the kernel of the actual finite action. If its value on an element of that kernel were nonzero, the corresponding affine conjugacy class would occur at an unramified Frobenius, where a local coboundary must be zero. Conjugation preserves nonzeroness through an invertible linear action. The descended finite-image class is then detected at five because that decomposition group surjects onto the actual action image. Inflation is injective directly from the coboundary formula.

For every finite coefficient module W_j, the Cartier dual action still factors through the actual operator image, since it retains the cyclotomic character. Finite global duality gives Sha^2=0. Equality of global and five-local invariants makes the five-local reciprocity component an isomorphism by finite local duality. The two exact rows (D.63.13), reopened in the canonical source, therefore have zero K_j and give exactly the claimed localization isomorphism. This is proved at every original finite level; no inverse-limit exactness shortcut is needed. D.63 then supplies the specified topology and convergence condition.

The independent boundary-depth check is correct: applying each of x, y, x-y to L=Z_5 z identifies the global coefficient ideal with the local ideal, including the zero-axis convention of D.77. The nonseparated continuous kernel is explicitly retained, so this does not claim vanishing of actual continuous H^2 or arbitrary-pair section existence.

## Sources and examples

The root reopened Milne's primary author PDFs:

- https://www.jmilne.org/math/CourseNotes/CFT.pdf, Chapter V, Theorem 3.23, printed page 164; exact statement retrieved as `turn1079view0`.
- https://www.jmilne.org/math/Books/ADTnot.pdf, I, Theorem 4.10(a)-(c), printed page 57; exact statement retrieved as `turn1079view1`.

The first applies to the finite affine Galois extension, with a prescribed nonempty conjugacy class. The second applies to finite five-primary modules with the set of all places; it supplies the stated duality and exact sequence, with the real higher-cohomology summand zero. The necessary finite local duality and all-place comparison are already proved and sourced in D.63.

The infinite example has primitive coefficient at 2 and all other coefficients divisible by 5, so its local coefficient remains a unit. The actual point t=5 has Kummer pair (kappa(5),2 kappa(2)); the sign disappears in the pro-five completion. Its local unit vector generates the exact away-five lattice. Existence comes from the point itself, and the full metabelian fibre assertion uses D.74 only for that actual point.

One optional phrasing clarification was requested: describe the affine conjugation of m as an invertible linear image, rather than an invertible translate. No mathematical correction was required.

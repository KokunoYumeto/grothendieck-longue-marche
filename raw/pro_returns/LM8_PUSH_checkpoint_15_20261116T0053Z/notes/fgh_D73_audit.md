# Independent full audit of D.73

**PASS.** Read the complete stable 436-line `notes/de_all_cusps_class2_draft.tex`, the integrated D.70 and D.71 comparisons, and the D.72 compactness statement just independently audited. No mathematical correction is required.

## New one-cusp and two-cusp steps

For one geometric cusp, hyperbolicity forces positive proper genus. Its product-of-commutators boundary has the primitive integral degree-two class Omega in wedge²V, including at two. The quotient by its line is torsion-free; positive Frobenius weights exclude fixed vectors, giving the required integral H1 injection. A conjugator between central cocycles projects to a fixed vector of V, hence is central, so this injection remains an injection into the actual zero-abelian class-two fibre. Nothing identifies that whole fibre with the cusp line in genus greater than one.

For two cusps the surface relation really gives c2=c1^-1 Omega^-1 in the actual class-two group. A conjugacy of powers first forces their exponents to be opposite in abelianization. The remaining central equation puts a nonzero scalar multiple of Omega in [c1,V]. The linear exterior-square map to wedge²(T_l J) kills this latter subspace but preserves the primitive nonzero symplectic bivector. This excludes nonzero conjugate powers. Crucially the draft uses this linear map, not the proper class-two group quotient, where the surface relation would vanish. This reasoning is integral and applies at two without dividing any BCH coefficients.

The peripheral root and centralizer arguments from D.71 extend to the free group of every finite rank. A first primitive lower-central class in degree one or two precludes an l-th root. The closed two-generator free-subgroup argument forces the centralizer of every nonzero peripheral power to be the full peripheral group; inner actions on its first nonzero class then force its geometric normalizer to be the same group. Its intersection with gamma3 is trivial.

## Actual local and global comparison

The full source group and its good-reduction specialization have the same geometric pro-l kernel away from l. Thus the class-two separation identifies the chosen rational cusp after a splitting extension, while its full decomposition group and packet parameter are compared over the original local field. The local packet injection and vanishing of the class-two twisted fixed group make the adjustment conjugator an actual gamma3 element. A zero valuation forces the actual inertia image to vanish; a nonzero valuation gives an integral local gamma3 coboundary. The argument does not assume a local pro-l section conjecture.

These exact statements give fixed finite support modulo each characteristic Frattini quotient. Its actual finite action and support are frozen on an open parameter neighborhood. Each exceptional finite cocycle has an action-trivial but cocycle-nontrivial affine Frobenius witness. High-valuation principal-divisor perturbations preserve all frozen data, remain in the same torsion component, and make the witness valuation nonzero without cancellation. The new local coboundary then kills its finite Frobenius value, a contradiction. This proves genuine dense open finite-witness conditions, not merely an expected rank bound.

On the residual locus every actual cocycle factors continuously through the compact action image on gamma3. A chosen nonzero inertia subgroup of this image is normal because the actual tangent acts cyclotomically on c. Its gamma3 invariants are trivial by the peripheral centralizer calculation. The local coboundary kills the restriction to that subgroup; the nonabelian cocycle identity then forces every global value to be invariant and hence trivial. The final all-prime comparison uses exactly the proved D.24/D.56 comparison of actual full sections, not joint faithfulness of arbitrary primewise quotients. D.72 applies only after fixing class two, as stated.

## Primary source reopening

Independently opened Hoshi RIMS1742, <https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1742.pdf>, as `turn915view0`. DefinitionA.3 and RemarkA.3.1 were read at `turn916view1`; the geometric-kernel isomorphism gives the cartesian specialization square. PropositionA.6 and its proof were checked at `turn916view0`/`turn916view1`, printed pages41--42: nonzero inertia after specialization is contained in a peripheral group, with no restriction on the number of cusps. The remaining finite-support and exact-coboundary steps were checked directly against D.70--D.72.

No computational certificate is claimed for the all-degree or Baire assertions; this is an independent full-proof audit.

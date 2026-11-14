# Independent D audit of E.68

**PASS.** The exact induced filtration, nonlinear triangular map and full lifting-fibre description all check. The author clarified that the shifted rank-two test uses a separate nonpointed representative choice; the main theorem keeps its pointed Smith representatives.

## Strict kernels and actual groups

For an actual quotient P→Q, the preimage of the next lower-central subgroup is R gamma_(r+1)(P). Intersecting with gamma_r(P) gives exactly the induced filtration quotient in E68.4. The free integral quotient lattices proved in E.41 make these kernels saturated. The argument uses the induced filtration on R, throughout; it does not substitute its intrinsic lower-central filtration.

The free, metabelian and marked graded identifications are the actual ones from E.41. At degree four the metabelian kernel consists of all 990 Hall brackets of pairs of degree-two Hall words. The marked kernel consists of the nine triple-marked commutators. Their maps and arithmetic actions are functorial for the retained marked generator.

The inverse limits and compact topologies are correct. Ordered actual lifts of each integral graded basis provide continuous collected coordinates on the finite nilpotent stages and on the induced kernel stages.

## Normal forms and uniqueness

Every graded Frobenius eigenvalue has positive weight, so F−1 is rationally invertible on every full, quotient and kernel lattice. An inner twist changes no associated-graded matrix. Hence there is no nonidentity stabilizer at any filtered stage or in its separated inverse limit.

This gives the unique lower conjugator used in the recursion. The inverse in E68.12 is applied only to the exact integral image of F−1. Central conjugation subtracts (F−1)v, so its sign is correct. All representatives and normalizations are continuous, and the unique finite-stage conjugators are compatible. The resulting inverse-limit normal form is a homeomorphism.

For a fixed target, the only ambiguity in lifting its unique quotient conjugator is an element of the actual kernel R. Conversely any equivalence of two aligned representatives projects to the trivial stabilizer. This proves the exact twisted-kernel H1 fibre and the stated transport when the chosen lift z0 changes. Every target has a full unramified lift. E.61's nonzero abelian cusp inertia excludes ramified full preimages of these unramified targets.

## Exact comparison maps

Applying F−1 to the saturated short exact sequence gives the claimed short exact sequence of finite cokernels, since all three fixed modules vanish. Formula E68.14 is the actual inverse on the kernel of the cokernel projection: changing a source representative by a full coboundary changes its kernel representative by a kernel coboundary.

I checked E68.15–E68.17 directly. The lifted lower conjugator aligns the actual projected lower representative; its discrepancy is central. Projecting the next source Smith representative adds its actual graded image. Conjugation by v subtracts the full graded coboundary, so h_r=v_r hat(h) and the displayed inverse have the correct order and sign. Each correction retains the genuine higher Frobenius value on the chosen Hall lift. The finite set section plus the injected kernel coordinate gives every source coordinate uniquely, without a group splitting assumption.

## Integral computation and precision

The unimodular basis change fixes the actual B0 vector, and its inverse provides actual free pro-three generator words. The two rank-two blocks and six scalar blocks preserve the stated multidegrees. The complete full, quotient and kernel matrices are therefore computed in the small blocks, including their actual lattice maps.

I independently checked the degree-four determinant valuations. The full free Lie degree has 2475 dimensions and 376 eigenvalues of weight six, giving valuation 2851. Its metabelian kernel has 990 dimensions and 148 weight-six eigenvalues, giving valuation 1138. This leaves 1713 for the metabelian quotient. The marked nine-dimensional kernel has weights seven and eight only, giving valuation nine and quotient valuation 2842. These agree with the exact Smith computations and the short exact sequences.

The split-lattice comparison contains three times the original lattice. Its functorial degree-r composites are multiplication by 3^r; both maps preserve the derived ideal and the marked ideal. Thus they restrict to the induced kernel lattices as well as descend to the quotients. The scalar split action and the exact valuation formula give the stated precision bound on every factor.

## Actual nonlinear test and fresh run

The rank-two test uses the actual E.54 Frobenius, including all nonlinear terms. The normalizing denominators have exactly the indicated three-adic valuations and are applied to divisible numerators. The unique conjugator is recovered in all 500 tests.

For the shifted illustrative target choice, direct collection gives epsilon2=1+a−b modulo three. This choice is nonpointed: the identity source has target coordinates (0,0,1). The author now states this explicitly, so it does not conflict with the main theorem's sigma(0)=0 condition. The complete 2187-class enumeration gives 27 target classes with 81 elements in every fibre.

The copied-source run in d_e68_audit/code passed in 3.76 seconds, and its entire JSON is identical to the source certificate. It includes all first-four-degree Smith data, 952 exact cokernel-map certificates, and the complete nonlinear test. The script SHA256 is b7df6c7f93a99bce1a0cb691ea0f7169bc6d09bdee18b14499425e35d8219690. The exact corrected source hashes are in audit.json.

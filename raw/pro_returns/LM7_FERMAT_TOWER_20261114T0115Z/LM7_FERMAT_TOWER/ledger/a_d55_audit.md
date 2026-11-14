# Independent D.55 proof and map audit

Status: PASS.

I read the complete frozen theorem/proof and both complete owned programs. I also executed the independent focused verifier code/a_d55_maps.py. Root owns the fresh full reconstruction of the author's two programs; this note does not claim that separate execution.

Frozen section: D55_EXPERIMENTS/sections/D_arithmetic_boundary_norm.tex, SHA256 e907fe100902b9074c844345425a8515eeb971760c5fab15a2ee9f3866cbcc04. The verifier checks every file and runtime-input hash in the author's frozen manifest.

## Actual arithmetic orientation map

The regular marked modular cover has the stated cusp count and free rank. Capping the boundary gives the primitive cusp lattice modulo its single diagonal relation, hence the exact compact homology quotient after reduction modulo two.

For the actual class-two endomorphism, the image of the cusp generator is z t, with z in the central commutator module. The 36-term cusp sum and the actual cusp coset representatives together enumerate each element of the arithmetic group once. The additional conjugation correction is a wedge with the cusp class and is killed by the compact quotient. Consequently the full group norm is exactly the map appearing in the theorem.

The punctured-surface relation can be evaluated in the free class-two quotient obtained by killing the first c-1 boundary generators and retaining the handles. The last boundary word becomes the inverse handle commutator product. This supplies an actual homomorphism before computing the orientation identity; it does not require the original endomorphism to preserve a compact-surface relation. The resulting norm equals the compact bivector defect with the stated characteristic-two sign.

The same-action local image is killed by this norm. The residual sequence and its decomposition through the norm's Tate kernel are exact kernel/image sequences with their literal maps. Equality of the actual arithmetic norm kernel and the local image is left unevaluated. The finite equality in the separate order-1080 source is not transferred to the arithmetic group.

On the actual reduced zero fibre, the compact bivector is nondegenerate and preserved, so its supporting space is contained in the compact homology image. This proves surjectivity of that compact map. The cusp radical is already fixed pointwise, so the entire homology map is invertible. The integral and finite generation assertions then follow from the unit reduction and the actual two-group Frattini criterion. The proof does not infer nonemptiness of that fibre.

## Ordinary marked relative homology

The integral five-term sequence uses the actual marked abelianization Q to C6. Its being an isomorphism on the abelianization of B identifies H2(Q,Z) with the computed integral coinvariants. The two universal-coefficient terms give the stated two-dimensional modulo-two homology. The actual odd kernel from G3 to Q is acyclic for these coefficients by averaging.

The two central double covers have the exact marked generator lift orders. Their restrictions to the order-two and order-36 peripheral subgroups give the identity dual matrix. The relative boundary is therefore the diagonal kernel of (a,b) mapping to a+b. The profinite source has the same boundary kernel, while its procyclic cusp has vanishing degree-two homology. The original quotient preserves the two marked degree-one generators, proving the claimed relative orientation isomorphism.

## Independent focused execution

The independent verifier checks the compact projection's idempotence, rank 146, and both compositions with the inverse intersection bivector. It computes the 18 linear and 153 polar bivector coefficients directly by matrix multiplication, independently of the author's exterior-coordinate evaluation, and checks every coefficient through the actual 13-column norm map.

It checks norm rank 9, local-image rank 4, and containment; reconstructs all 1,080 literal ordered products in the subgroup transversals; independently recomputes both exact integral Smith lists; checks 2,304 cover projection edges, 2,304 central-involution commutation identities and 1,152 marked abelianization edges. The resulting peripheral restriction matrix is exactly the displayed identity matrix.

All focused assertions passed. The retained JSON has no timing fields or excluded comparison fields. The arithmetic zero locus, arithmetic residual norm kernel, and full profinite realization keep precisely their stated unevaluated status.

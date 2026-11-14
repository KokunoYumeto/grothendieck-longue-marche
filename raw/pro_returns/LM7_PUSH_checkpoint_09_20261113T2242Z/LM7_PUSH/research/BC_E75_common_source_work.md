# E75: whole E71 source and the full Gaussian pro-three group

This is a new working record after the frozen E70/E71 batches. The actual common-source calculation is in `bc_gaussian_kn_common.py`; the complete character comparison is in `bc_gaussian_kn_characters.py`. No frozen input is modified.

## Exact source

The domain is J=K6∩F′. Its image is computed from all97 original N words in the full11691-point E71 representation, with all2592 Gaussian detector points adjoined. The actual N image is derived before any point projection. The95 literal sixth powers from E71's integral kernel basis are then adjoined. Reusing only preimages of a generating set of the old finite image would omit an uncontrolled part of the new joint source; that replacement is not used.

The retained E71 image P has order 2^105·3^17. The Gaussian group H is the exact class-two pullback in E70, with H_ab=Z3^12. The twelve coordinates retain the six original Gaussian abelian values and the six weight-three values of the three differences `last*lift(first)^−1`. The detector S3 has order3^27 and gives the actual isomorphism H/Φ(H)→S3/Φ(S3).

## Every three-group quotient of P is elementary abelian

This follows from the actual retained target maps, without a claim that P′ is binary.

For a matrix block belonging to H0=GL2(F3) or SL2(F3), restriction to J has deck exponent zero and is literally

    (a,b): z ↦ a^−1 z b,

where a=qδ_n(w), b=q(w). These pairs form a homomorphism from the coordinate-zero source into H0×H0. The kernel of the displayed action of H0×H0 is the diagonal center: evaluating at z=1 forces a=b, and then evaluating all z forces a central. The center has order2. Each H0 has a Sylow3 subgroup of order3. Thus the full left/right action group, and every subgroup of it, has elementary abelian Sylow3 subgroups.

The separate coefficient block is the literal additive C24 action. Each retained E6 block is the actual direct product H96×C6, where |H96|=96 and its Sylow3 subgroup has order3. Its Sylow3 subgroup is therefore C3². The E62 factor is binary. The E67 image retained by E68 is elementary abelian of order3^9; E71 proves that the whole-J projection to these old factors remains exactly the E68 image. Consequently P embeds through its actual retained permutation coordinates in a product of groups with elementary abelian Sylow3 subgroups. Every Sylow3 subgroup of P is conjugate into a Sylow3 subgroup of that product, and so is elementary abelian.

For an epimorphism P→Q onto a finite3-group, a Sylow3 subgroup of P maps onto Q: its intersection with the normal kernel is a Sylow3 subgroup of that kernel, and the group-order formula gives the required surjectivity. Hence every finite3-group quotient Q of P is elementary abelian.

Arithmetic independently checked this entire target-factor argument, including the exact diagonal scalar kernel and the deck-zero gate.

## Consequence for the full common quotient

The common quotient supplied by Goursat for an actual closed subdirect product of P and H is finite, since P is finite, and is a three-group, since H is pro-three. The preceding argument makes it elementary abelian. Its H map therefore factors through the specific twelve-dimensional H/Φ(H) map, and thus through S3. The complete finite common image in P×S3 determines the entire possible common quotient with H. This is the exact finite-to-pro-three transfer used here.

The actual E67 comparison is retained explicitly: the six Gaussian translations in the old E71 permutation block are compared with the reduction of the six P3 Hall coordinates on every new joint input and every strong word. No order-only identification of a common quotient is made.

## Current computation

The four-stage source and character run is in progress. Its result will be recorded from the actual saved certificates before any fibre-product or target-survival assertion is made.

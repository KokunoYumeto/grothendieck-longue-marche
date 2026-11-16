# Independent full audit of D79

**PASS**, notes-only candidate, reviewed by pbc_groups on 2026-11-15. This audit concerns the entire written proof, not only its residual certificate. Integration remains subject to the parent's source freeze.

## Actual images, gauges and geometric comparisons

The two inertia columns are the columns of the invertible Z5 matrix. They generate the full translation lattice, so D78's faithful actual-image argument gives the same H semidirect I0. The local vector is primitive, and D78's full local kappa(6)-image of the I0-kernel gives the exact local line subgroup. Coinduction and finite affine-image Chebotarev descent apply to these actual images.

For t maps to 1/t, the Kummer identities are a maps to -a and b maps to b-a+kappa(-1), with kappa(-1)=0 at five. The map t to 1-t interchanges a,b. The draft transports arithmetic fundamental extensions and tangential frames. D35's actual three packet formulas make each transported unit tangent zero in abelian Kummer cohomology. The remaining integral abelian gauge identifies the reference actions; an inner commutator acts trivially on the Alexander module. Thus the actual coefficient modules and all finite/global/local localization diagrams are isomorphic. A bare coordinate substitution would not have sufficed, but that is not the argument used.

A primitive slope vector has at most one positive valuation among alpha, beta, alpha-beta. The geometric transformations place it on alpha with beta a unit. All three global divisibilities stay zero, since the two matrix rows and their difference are primitive.

## Three-unit and exact-boundary cases

At depth zero, the primitive local cubic coefficient stays a unit. D78's one fixed finite coefficient module trivializes the same integral cocycle everywhere. At two and three, constants are fixed by translations, the cocycle is unramified, and the cyclotomic difference is a unit. Changing the inertia columns therefore introduces no missing finite-level trivialization.

At the exact boundary the line action factors through Gamma. The coefficient inclusion lambda into D_lin stays injective on continuous Hom from N0. The order-four factor acts on lambda by a nontrivial unit scalar, so both H0 and H1 of Gamma with lambda vanish. Inflation-restriction makes the indicated local restriction injective.

## Integral finite-depth quotient

For N=5^d and alpha=N a0, Q=z^2((1+z)^N-1) is distinguished of degree N+2. Every cyclotomic-kernel multiplier differs from one by Q, and the primitive actual delta differs by Q times a unit. This uses exact three-boundary factorization and the unit residual cubic coefficient, with no division by N. The invariants are the Cartier duals of R/QR and zR/zQR with their stated Gamma invariants.

The four-term dual sequence is correct: dualize zR/zQR to R/QR, whose kernel is QR/zQR and cokernel is R/zR. The arithmetic character on QR/zQR is chi^2 times chi^3 = chi^5. Cartier duality adds chi, giving chi^-4. The lambda terms have zero H0 and H1; the entire possible restriction kernel therefore injects into (Q5/Z5(-4))^Gamma=F5.

## Independent operator derivation

I independently expanded S_gamma(t^beta) S_gamma(t^-alpha) beta_gamma to second order. Dividing its difference from gamma S_gamma(t^beta) by t^N-1 gives exactly

A_gamma = -a0 gamma^2(gamma-1)/2,

B_gamma = a0 gamma^2(gamma-1)[alpha(2gamma-1)/12 + N/4 - beta(7gamma-5)/24].

The beta contribution to the linear coefficient is -a0 beta gamma^2(gamma^2-1)/24, producing the stated 7gamma-5 after combining the two S factors. Every denominator is a unit at five. Both coefficients vanish modulo five when gamma is 1 modulo five.

For the actual power gamma=2^(4*5^(d-1)), gamma=1+3N modulo 5N. In characteristic five through degree N+2, phi_gamma(z)=z+3z^N+3z^(N+1), and the multiplier's first nonconstant coefficient is 3z^(N-1), since beta^(N-1)=1 modulo five. Its action on z^3 gives 3*3+3=12=2 modulo five at degree N+2. Every omitted degree exceeds the quotient's bound for N>=5. This is an actual operator on the complete finite quotient, rather than a leading-weight inference.

Every order-five invariant Cartier functional must kill Q. A higher-order extension cannot evade this: J^Gamma is the divisible group (Q5/Z5)^d. If v lifted the nonzero F5 quotient, solve 5d=5v inside that divisible subgroup; then v-d is an order-five lift with the same nonzero quotient, contradicting the operator identity. This proves the entire restriction kernel zero at every positive finite depth.

D77's continuous decomposition gives exactly the asserted compact groups. D74 is applied only conditionally to a nonempty section fibre. No arbitrary-pair existence, separated H2 splitting or broader nilpotent assertion is introduced.

## Independent execution

The certificate was run under a distinct runpy module name without changing owner outputs. Its entire serialized result equals the owner's JSON: PASS for both symbolic interpolation coefficients, actual cyclotomic powers at depths 1 through 6, twelve exact quotient matrices, and all 480 GL2(F5) matrices (240 unit-slope and 240 boundary-slope). The all-depth proof is not extrapolated from these tests.

Independent files: notes/pbc_D79_independent_rerun.json and notes/pbc_D79_independent_rerun.out.


SHA256 notes/de_sha_matrix_family_draft.tex: a53862e684c1cde23cb2a6b93724f00bdf0dbb37b89fb304dff83661ef08c6e9

SHA256 notes/de_sha_matrix_family_certificate.py: 358d9c680ff674a1ea3d5b33f80d66e08e3f22b37eccf36858823823808c603c

SHA256 notes/pbc_D79_independent_rerun.json: d67a16fd531bfa91c4e95ff274624f7946e471c04e9823302a0d4a433285fc65

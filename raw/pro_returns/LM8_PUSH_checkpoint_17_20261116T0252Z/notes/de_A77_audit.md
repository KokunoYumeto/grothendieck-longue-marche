# Independent A77 audit

**PASS: full written proof, complete exact certificate, and whole-JSON independent replay.** This retains the explicit audited A75/A76 dependencies and existing canonical geometric inputs.

Draft SHA-256 `7752d6addfa2162f0008ee82049a7a062420e4791b865ac6df809614a662e6e0`.

## Proof gates

1. For an actual two-generated finite group, derived subgroup C2 is central, hence the group is nilpotent and splits into its two-Sylow and odd abelian part. The abelian case is treated separately.
2. For each faithful irreducible quotient over the same auxiliary-adic splitting field, Schur makes the centre cyclic; central squares give Q/Z=C2². Exact class-two collection gives Z=<u²,v²,sigma>. A primitive square generates that centre, giving cyclic index2; the centre-order2 exception is handled by (uv)²=sigma.
3. The normal kernels define actual quotient curves. Divisor pullback and norm give q* q_*=sum_N and q_*q*=|N| even at ramified points. Each irreducible summand is fixed by its own kernel, so the actual sum of quotient-Jacobian pullbacks surjects after rational Tate comparison.
4. The proof correctly uses an isogeny quotient/factor of the product, not an isogeny from the entire product. The previously established potential-good quotient criterion and special-rank additivity then give the required two-rank-zero property.
5. Actual central inertia is precisely G-prime, giving genus1+|G|/4 and |G|/2 cusps. The elliptic C/I quotient and its kernel exponent give actual 2e-torsion cusp divisors. Frattini inclusion gives a distinct companion in every proper intermediate, and actual norms retain the needed geometry.
6. The odd abelian factor is retained through the exact connected field compositum, extended Abel map, good finite-etale isogeny, a separately proved nilpotent tree, and literal rational-subtree copies. No rank-zero assertion for the odd pullback is inferred.
7. The order32 example lies outside cyclic-index2, and all four actual D8/D8/D8/Q8 maps and complete character accounting were independently replayed. The unrounded nonlinear Gram numerators were separately checked to equal32 times the identity.

## Source scope

The actual compact-type Abel-map and nilpotent tree inputs are used at precisely the scope independently reopened for A75/A76: Dupuy-Rabinoff1.1/3.2 and Lehr-Matignon6.13. The quotient-good-reduction input is the existing canonical A40/A68-A75 Serre-Tate input; no new visual verification of that scanned primary is claimed in this audit. The group and actual Jacobian-spanning arguments are proved directly in the draft.

## Exact replay

Independent retained outputs: `notes/de_A77_certificate_rerun.json` and `.out`. Entire author JSON equality; source SHA-256 `c2b05f26e7b19bc767ad3903921e7ff63efa289fb51d2ded3b36e15fee704dda`, result SHA-256 `4909041203e23a0c9f82ffa7f9698a422ac84d1e97fdd691ddcf9f2f9f9fcdbb`. The unrounded four-by-four character Gram numerator matrix was also checked, avoiding reliance on integer division in the support script.

No canonical source or registered row changed.

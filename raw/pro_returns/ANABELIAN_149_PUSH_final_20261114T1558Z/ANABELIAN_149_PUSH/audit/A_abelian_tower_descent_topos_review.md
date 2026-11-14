# Independent review of A.C2.23

Reviewed the complete candidate at audit/A_abelian_tower_descent_candidate.md on 14 November 2026. Verdict: PASS in its stated abelian-total-cover scope.

The primitive operator on a cyclic subgroup H of order n is nonzero precisely on characters whose restriction to H has order n. For a proper divisor m of n, some prime valuation drops, and then m divides n/ell; this checks both directions of the scalar criterion, including prime powers and mixed conductors.

The geometric p-adic Tate module is used consistently. The Tate module of the image abelian variety is the image on rational Tate modules: quotienting by the connected kernel leaves an isogeny, and even a p-power isogeny becomes invertible over Q_p. Thus p-rank zero of the primitive factor really kills every faithful-restriction character space; mere nonordinarity would not imply this.

The faithful character of H extends to A because the root relation at each cyclic enlargement respects every relation. More explicitly, if a has order M and its image in A/B has order r, then r divides M and z^M=theta(ra)^(M/r)=1, so the chosen extension has finite image of order dividing the exponent of A. Its order N is divisible by n. Every exponent coprime to N is coprime to n; hence all primitive characters of A/ker(chi) remain faithful on H and have zero Tate spaces.

The pullback/norm identities identify T_p(J_D) with the K-invariants in T_p(J_W), already integrally because |K| is prime to p. The characters of that invariant module are exactly powers of chi. The vanishing of its primitive powers proves the desired cyclic quotient has zero-p-rank primitive factor.

No geometric realization assertion is inferred merely from a character-theoretic example. The actual cover W/C is part of the hypotheses, and its intermediate quotient is an actual connected étale cyclic cover. The final limitation correctly concerns only an abelian total Galois group. Iterated abelian stages with nonabelian normal closure are not included.

The finite-group program is supplemental; I reviewed the arbitrary-group proof above rather than treating its finite checks as a proof. No amendment is required.

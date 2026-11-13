INCOMPLETE

# G.20 follow-up: Prym detection and punctured elliptic transport

G.22 is proved and is input at the end of `sections/G.tex`. G.20 remains Open. The new argument narrows the finite-cover alternative and gives exact counterexamples to two proposed automatic transport steps; it does not construct a residual subgroup or disprove inertia recognition.

## New proved information

For a residual element in the common kernel R of all original maximal pro-ell quotients, its proper-homology image in a finite cover lies in the kernel of the cover Jacobian's pushforward to the original E. Thus the relevant component is in the Prym part. The inherited E quotient cannot carry it. A compactified cover of genus one is excluded, because its map to E is an isogeny and is injective on Tate modules.

A nonconstant map f from the compactification of a degree-d cover Y of the once-punctured E to another elliptic curve E' restricts to Y -> E' minus {q} if and only if the full geometric fibre over q is supported in the boundary S. Riemann-Hurwitz gives the necessary bound deg(f) <= |S|+2g(Ybar)-2 = d. Equality forces all boundary and ramification to occur over q and makes the restriction finite etale.

If such a map detects the proper-homology image of the proposed procyclic subgroup, arithmetic fundamental-group functoriality transports its open normalizer to the target. A proved normalizer criterion for that exact pointed target then makes its image cuspidal, contradicting its nonzero proper homology. In the present proof the target criterion is known when the pointed target becomes isomorphic to the original (E,O) over a finite extension. No theorem for an arbitrary isogenous curve, different CM field, or higher-dimensional factor is inferred.

## Exact failed shortcuts

Take Y = E minus E[2]. The map [2]:Y -> E minus {O} is a finite etale cover of degree4. The detecting Jacobian quotient [3]:E -> E acts by 3 on every Tate module, but its restriction to Y still has image all of E: every fibre has9 geometric points, while at most1 lies in E[2]. Hence it does not restrict to any once-punctured target. The standalone exact rational polynomial calculation derives psi3 = 3x^4-6x^2-1 from the doubling formula, checks its squarefreeness and coprimality with x^3-x, and verifies the eight nonzero3torsion points lie in Y. This is a counterexample to automatic puncturing, not to G.20. Postcomposition of any detecting quotient by sufficiently large [m] preserves detection and violates the same fibre-degree bound. Further surjective covers do not repair a fixed map whose image is already all of the elliptic curve.

Adding punctures instead requires lifting the subgroup with its arithmetic normalizer. That lift is not automatic: a primitive split CM eigenline in T5E has full arithmetic normalizer in the proper elliptic arithmetic fundamental group, while G.13 says that any procyclic subgroup upstairs in P5 with open arithmetic normalizer is cuspidal and therefore has zero image in T5E. G.10 gives the corresponding failure of fixed-element lifting for the specified cusp-packet action.

## Exact residual obligation

A detecting cover of genus at least2 may have a relevant fixed or weight-one CM component in its Prym. No construction here produces a detecting elliptic quotient, a fibre supported in the existing boundary, and a normalizer theorem for the exact pointed target simultaneously. A CM eigenline of a Tate module need not come from an elliptic quotient at all. The fixed-element argument additionally requires compatibility with the actual lifted cusp-packet section. These requirements, or a different argument eliminating the Prym alternative, remain unresolved.

## Durable source state

- Proof: `sections/g_cover_transport.tex`, G.22, already input by `sections/G.tex`.
- Exact certificate: `code/g_cover_transport.py`, `code/g_cover_transport.json`, `code/g_cover_transport.out`; the program was run successfully.
- Own ledgers: `sections/G_transport_results.json`, `sections/G_transport_coverage.json`, `sections/G_transport_readings.csv`, `sections/G_transport_refs.bib`.
- Existing G.20 proof, result notes, coverage, and Part G report updated precisely; G.16 and all signed-Fermat typesetting edits preserved.
- Primary source opened: The Stacks Project, Section53.12, Tag0C1B, Lemmas53.12.2 and53.12.4. Nakamura's exact target hypotheses are retained through the already established G.13.

No assembler, root metadata generator, build, or upload was run for this addition.

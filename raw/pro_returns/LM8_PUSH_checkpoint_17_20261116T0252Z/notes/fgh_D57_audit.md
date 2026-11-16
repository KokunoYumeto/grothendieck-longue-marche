# Independent audit of the unregistered D.57 draft

Auditor: fgh_geometry, 15 November 2026. Verdict: **PASS**, conditional on the separately audited D.54 theorem used by the draft. The parent and DE were informed. This note does not register the candidate or calculate its missing obstruction.

I read `notes/de_fermat_local_obstruction_draft.tex` in full and the actual D.20 construction in `sections/D.tex`, including its characteristic Haar-idempotent embedding j, equivariant retraction q, and jointly continuous family of cocycles.

1. The image of the local group in P_ar is closed. A missing Frattini direction gives a cyclic ell-extension of Q(zeta_ell) unramified outside its unique ell-prime and split there; class number one eliminates it. A proper closed subgroup of a pro-ell group is detected inside a proper subgroup of some finite ell-quotient and hence an index-ell subgroup. Thus the local map surjects P_ar. Total ramification of the cyclotomic constant extension gives the full Gamma_ell quotient. Inflation on actual H1 cocycles is injective because every Gamma_ell element has a local lift.

2. Both asserted local H0 vanishings hold coefficient prime by coefficient prime. Local Jacobian torsion is finite, so its Tate module has zero invariants. After splitting the cusps, boundary modules and their quotient by the primitive selected boundary line are sums of Tate modules of roots of unity, whose invariants vanish. These facts also justify the H0 claim for the nonsplit extension A and A/I_O.

3. A geometric conjugator between the zero-abelian-cocycle sections has invariant abelian image, hence lies in N'/N''. This module is abelian; conjugation by the cocycle values themselves acts trivially on it. Projecting the conjugator through q and then B therefore gives exactly a coboundary for the difference parameter. Local inflation injectivity excludes it unless the parameters agree.

4. The full all-prime Kummer map is the appropriate one: if the compactified point's class vanishes, it is divisible by every positive integer in the compact profinite group J(k), and hence is zero. Abel--Jacobi injectivity then forces the point to be O. The exact sequence with H0(A/I_O)=0 injects its whole cusp Kummer packet into H1(A). Thus only the unit tangent has zero abelian class. This avoids a false inference from a single coefficient-prime Kummer map.

5. The finite local cocycle sets are genuinely finite, including finite solvable nonabelian targets: use the last characteristic abelian derived subgroup and the usual twisted H1 fibres, each finite. Characteristic open quotients of the finitely generated prosolvable geometric group are cofinal. The inverse limit of their finite actual cocycle sets consists exactly of continuous cocycles, since continuity is tested in each finite quotient. Its compact group conjugation quotient is Hausdorff: the orbit equivalence relation is the image of a compact space.

6. A lift up to metabelian conjugacy can be made an exact lift of the selected actual cocycle by lifting its conjugator through the surjective geometric quotient. The resulting fibre is closed and compact. Nonempty fibres at every derived stage form an inverse system with a nonempty limit by the finite-intersection property: any finite set of compatibilities is supplied by one later stage. Surjective transition maps are unnecessary. The limit is an actual continuous cocycle in N^sol because every finite solvable quotient has finite derived length.

7. Images of the compact local section spaces in the Hausdorff metabelian section space are closed. Their preimages in the compact parameter module are nested closed sets with intersection {0}. Intersecting with the compact complement of ell^h proves a uniform empty stage there.

The draft correctly leaves the first obstructed derived length, a numerical finite quotient, and an explicit cohomological obstruction class open. It does not decide whether arbitrarily small nonzero parameters survive every fixed stage, or whether another noncuspidal family survives that stage. No stronger assertion follows from this compactness proof.

# Independent audit of A204

Auditor: local_preprint. Result: PASS.

Source: `sections/selmer_general_unramified_obstruction.tex`.
Independent execution of `python work/code/selmer_weight_four_inertia_certificate.py` passed all three fourth-layer cusp calculations, the primitive Hall extraction matrix, the Hall-Witt identity and all 130 strict-residue telescoping identities.

The integral Hall coordinate map is an actual continuous set section of the original lower-central quotient. Its defect lies in the central Hall layer with the stated cyclotomic action. At every physical prime different from the coefficient prime, the actual pointed action is unramified. The full ordinary/cusp comparison and lifting of geometric conjugators retain the literal local section and its three possible meridian inertia powers.

The compactness argument in A204.8--9 is valid: the inverse image of a fixed open coefficient subgroup is an open neighborhood of the entire compact first factor times zero. A finite subcover gives one exponent depth valid for every conjugator; taking a maximum handles all three cusp labels. The global abelian cocycles force their local inertia exponents to converge to zero. Hence the aligned central primitive family converges to zero in the actual coefficient module.

For weight r+1, direct expansion of the normalized coboundary gives the two terms q^(r+1)z(T)-z(T^q) and qz(T)-z(T^q). Their difference divided by q is exactly (q^r-1)z(T). The raw defect has the displayed negative sign. Thus its strict residue is in the literal image of the convergent-family differential. The exact localization map of A65.8 proves the claimed unramified-image containment, including its continuous inverse-limit contribution. The finite integer annihilator follows from the precise A65.7 statement.

For weight four, I reread A61.18--20. The odd-primary unramified groups vanish by the actual K6 computation. At two, the unramified group injects under real restriction. The assumed real full point/cusp lift makes the actual obstruction zero at the real place; any unramified preimage has that same restriction and is therefore zero. Product cochains provide a continuous primitive in all coefficient factors and an actual global class-four section. The scope correctly makes no local-matching assertion about this new lift.


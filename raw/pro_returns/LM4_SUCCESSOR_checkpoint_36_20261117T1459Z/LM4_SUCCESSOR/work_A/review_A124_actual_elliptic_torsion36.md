# Entire-source independent review: A124

Reviewer: /root/involutions. Result: PASS.

Reviewed source: work_root/A124_actual_elliptic_torsion_transport_proposed.tex.
SHA256: fd436ed98a15e581b7afed1c2e239ac2d8e2745dabd059a6c18d5217d110f9c0.
Size: 14446 bytes. The entire source was read in two untruncated, adjoining outputs, lines 1–150 and 150–end. No build or numerical producer was executed.

## Exact mathematical audit

1. The group is correctly the lift group, or orbifold fundamental group, of the actual reduced configuration space divided by S3. The source does not confuse this with the ordinary fundamental group of its coarse quotient. The diagonal translation loops and the reduced marked presentation give the indicated kernel P=pi1(Conf2(T minus 0)).

2. The forgetful fibration has free rank-three fiber and free rank-two base, and its aspherical total space gives a contractible universal cover. The free quotient splits the extension. Characteristic finite fiber quotients and the finite source-action image supply actual finite semidirect-product targets, proving the required full fiber topology and residual finiteness. The completion sequence is therefore the actual exact sequence.

3. The discrete and profinite LHS comparisons give goodness for finite modules. The finite graph-of-spaces model for the pure group, the finite-quotient resolution, and filtered unions extend the comparison to the stated discrete continuous F_p modules. Each such module is a union of finite invariant submodules: a vector has finite orbit under the compact group, and the F_p span of that orbit is finite. The resolutions/cohomology comparison commute with this union. The virtual cohomological-type and residual-finiteness hypotheses needed for the invoked prime-order theorem are explicitly verified.

4. I checked the finite-group cellular argument using ordinary cochains, hence products on infinite cell sets. The lifted admissible triangulation has dimension four; a cell fixed by a nontrivial element is a fixed vertex because its projection lies in an isolated or empty fixed locus. Positive group cohomology of regular cell-orbit cochains vanishes, also for the indicated products. In total degree above four, the fixed-vertex column has neither a possible incoming differential nor a possible surviving outgoing differential. Contractibility gives one-dimensional H^n(C_p,F_p), so the product indexed by fixed vertices has exactly one factor. This proves both nonexistence of order two and uniqueness of the fixed point of an order-three lift.

5. Every downstairs fixed point has the stated order-three lift fixing a chosen point above it. The cube is a deck transformation fixing a point and is trivial. Its stabilizer, normalizer and centralizer are exactly C3. The four S3-orbits of the eight fixed configurations give four subgroup classes, and the lack of normalizer inversion gives eight element classes.

6. Abelianization of the complete marked presentation gives precisely C2 times C3 squared, with no missing relation. The actual torus linear-homeomorphism action on total displacement modulo three gives all eight nonzero labels. Only an outer action on the configuration group is required. The source does not presume a literal SL2(Z) lift to its automorphism group.

7. The prime-order comparison applies to this group itself. The pure completion is torsion-free by its finite cohomological dimension and goodness, so every finite subgroup of the full completion injects into S3. Excluding order two leaves only C3. This justifies the statement about all nontrivial finite subgroups without an unstated general finite-subgroup theorem.

8. Every specified Pi_w has the same nonzero abelian label and the same S3 image as Pi0. The full conjugator can be adjusted on the right by a power of Pi0 to become pure. The centralizer intersection with the pure completion is trivial, giving uniqueness. Compactness of the pure group makes its continuous orbit map a homeomorphism onto its closed image, which proves continuity of w to p_w on the closed pentagon-word set.

9. The actual elliptic involution preserves the relevant label and permutation. Applying it twice gives Theta(h)h=1 by the pure centralizer computation. The cocycle z=h^{-1} has z Theta(z)=1, and z times the external involution centralizes Pi. The resulting C6 is actual. The formulas h'=Theta(a)h a^{-1} and z'=a z Theta(a)^{-1} have the correct order and show precisely constancy of the nonabelian H1 class and its stated triviality criterion.

## Primary and scope record

The primary reads used in the preceding read-only audit were Enriquez's complete Section 1.2 presentation and Proposition 2.5/action material, and the precise Boggi–Zalesskii definitions, prime-order theorem statements, Theorem 4.3, Lemma 4.4 and the entire prime-order proof. They were actually opened before this source review. This receipt does not claim a new whole-paper read, a new reading of every prime-power induction, or a new reading of the original Scheiderer book. The present source review independently checks the full application and every internal argument above.

No assertion that the C2 class is trivial, that the original boundary equation holds, or that a CM sign has been computed follows. The proposed strengthening p_w in the closed pure commutator subgroup is not used here and remains a separate audit.

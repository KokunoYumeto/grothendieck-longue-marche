# Independent root audit of B.38

Status: approved for the 179-page fourth checkpoint; actual integral phase remains open.

The root auditor read the full B.38 argument and both independent computation routes. Fresh executions of b_global_action_ambiguity.py, b_action_ambiguity_refinement.py and c_action_ambiguity_refinement.py completed successfully, with outputs retained under work/. The independent global matrices enumerate all 54 projective Fermat automorphisms rather than silently substituting the four-generator presentation. Both refinements exhaust the 81 coefficient vectors and obtain the same subgroup sizes 9, 9 and 3, despite using different four-coordinate bases.

The arithmetic torsion description uses the rational-coset connecting map and vanishing of rational invariants at a good Frobenius. The actual commutator module J is primitive of rank 90. Its integral inclusion requires only class-two BCH and the explicit cubic correction to a commutator, both with denominator two; no class-three integral BCH is invoked at three. The four-bracket lift of the affine-line cube sum lies literally in J and reduces to the recorded pure-boundary generator.

The surviving line is non-inner. Localization at two is injective on the global torsion, because Frobenius minus one is rationally invertible. The displayed C81 functional is a local coefficient quotient, and the statement that moduli 3, 9 and 27 miss the line is explicitly local. It is not extended to global coefficient cohomology. The inherited order-3^30 group kills J by its specified ambient tripod commutator relation; the once-punctured elliptic free group is not identified with that ambient tripod group.

The full manuscript was frozen during the build. The B.38 modulo-81 typesetting typo was corrected before the final 179-page build. All new B.38 proof pages were visually inspected, with no overflow, clipping or missing symbols. No claim identifies the actual one of the three remaining formal integral classes, or asserts that all three are geometric.

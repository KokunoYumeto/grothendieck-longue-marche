# Independent audit of E93

**Status: PASS.** The complete frozen theorem and proof, the complete program, and the cited internal maps were read. A fresh execution used a copied program and all five independently hash-checked, copied inputs. Both the entire JSON certificate and stdout are byte-identical to the frozen reference. No field was excluded.

## Mathematical checks

The actual global residue map from E37.20 is split by the uniformly convergent sum of Kummer cocycles. Its support topology is the inverse limit of discrete direct sums. The unramified term evaluates on the same actual free generator used by the local marking. The symbolic constants b and alpha are retained throughout the restriction and its inverse.

The signed exterior-to-Hall matrix is applied before every comparison. The Tate line is primitive in the relative rank22 kernel because its first coordinate is -2. This does not assert horizontal primitivity: the certificate retains the actual [w] vector, whose free coordinates have exact common divisibility3. The relative quotient, its rank21 section, and all horizontal finite torsion coordinates have literal integral inverse maps.

The actual joint coefficient map annihilates the Tate line already as a map of lattices. Therefore every ramified central Kummer summand has zero joint image. Its only remaining variation is the explicitly split horizontal rho coordinate. The Smith row, all14 finite coordinates, the full23-dimensional free kernel and every inverse are retained.

For the nonabelian transfer, the central action is independent of the chosen lower section. Vanishing of global and local H0(V) removes the lower stabilizer quotient. Thus each actual nonempty global class-two fibre is a torsor with exactly the displayed localization and joint maps. The statement consistently leaves the actual origin's quotient value unevaluated and gives its exact change under a different global origin.

## Fresh execution

```sh
python a_e93_audit/code/e_global_central_localization.py --source-code a_e93_audit/source_code > a_e93_audit/code/e_global_central_localization.out
```

Exit status0. The full certificate and stdout match byte for byte. The independent run repeats all matrix identities,1134 localization inverses and1458 full coordinate inverses. `audit.json` records the complete section, program, input and output hashes.

No mathematical or presentation correction was requested.

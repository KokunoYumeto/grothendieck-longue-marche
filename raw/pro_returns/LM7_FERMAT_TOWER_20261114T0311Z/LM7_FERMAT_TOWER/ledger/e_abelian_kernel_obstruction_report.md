# E.87: exact first-degree kernel and evaluated intrinsic obstructions

## Result

The actual local map from the ten-dimensional intrinsic abelian lattice to the joint three-dimensional lattice induces a surjection `Z3^15 x C3^3 -> Z3^5 x C3`, with kernel `Z3^10 x C3^3`. The section gives the literal coefficient matrix, both arithmetic intertwiners, a saturated rank-seven coefficient-kernel basis, and complete forward/inverse cohomology coordinates. The finite target carry is retained. Since all source torsion maps to zero, the exact sequence has no Z3-linear section.

For every intrinsic abelian class with the same B0 inertia coordinate and the same joint abelian image as E.85, the full class-two obstruction is evaluated. Its image is C3^3; three explicit residue conditions give its entire kernel, which is Z3^4 after the actual geometric gauge. Exact rational Smith inverses give integral particular central corrections for every point. The actual joint normalization and unique lower alignment preserve every nonlinear central term. The resulting image is `Z3 x 3Z3 x 0`, and each full conjugacy fibre in this entire inertia-fixed locus is `Z3^48 x C3^9 x C9^5`.

The actual open immersion filling the eight cusps other than O gives an equivariant quotient to the class-two once-punctured elliptic group. Its central map picks the free intrinsic obstruction coordinate. The rational coordinate swap is proved to be [-1] by the explicit degree-two rational quotient and the divisor norm/pullback identity. Its coherent formal-disc transport is given at every 3-power level, squares to the identity, and is defined over Q. The actual central basis correction, including its two coefficients and inverse, makes the arithmetic action exactly the evaluated elliptic Tate action. This is an explicit conjugacy of the genuine based action.

For every intrinsic abelian input, its exact free obstruction is `-7 t (U1 + 21 t/2)`. The filled local class-two image is exactly the two closed branches `t=0` and `U1=-21t/2`. Each point has fibre Z3^2; the proof gives the two values of the actual E.77 source, their full fixed conjugation law, and inverse normalization. The natural obstruction square transfers every exclusion to the intrinsic group.

## Verification

The executed program saved all forward and inverse Smith matrices, the coefficient and arithmetic matrices, the complete fifteen-coordinate horizontal obstruction, the seven-column integral particular correction and its joint-zero refinement. It checked 729 complete first-degree inverse identities, all 2,187 residue inputs for the horizontal obstruction, six formal-disc identities, the symbolic averaged action and norm word, and 729 filled elliptic gauge/inverse identities. All assertions passed. No timing fields or excluded JSON fields occur.

Run from the workspace with:

```bash
python research_e87/code/a_abelian_kernel_obstruction.py --source-code LM7_FERMAT_TOWER/code --smith-helper research_e82/code/e_cusp_local_smith.py
```

After installation, the program finds the integrated inputs and helper beside itself. Its five exact input hashes are recorded in the JSON. Root independently reran the copied program with all five copied and hash-verified inputs. Its complete stdout and JSON are byte-identical, with no ignored fields. Root read the entire proof and program and independently reopened the complete SGA1 XII 5.1/5.2 passages and proofs. The integrated citation adds those exact anchors; no mathematical source was changed.

## Sources and scope

The full original SGA1 PDF was reopened and the complete Exposé XII Theorem5.1/Corollary5.2 passages were read. The source-evidence ledger records the URL, exact pages, opened reference and each internal source hash. The new finite and profinite maps are proved in the section.

The fifteen finite class-two obstruction coordinates for general relative inputs remain to be evaluated. The two elliptic branches give a proved necessary condition for every intrinsic input; the complete inertia-fixed horizontal locus is already evaluated. No conclusion that E.23 is solved is made.

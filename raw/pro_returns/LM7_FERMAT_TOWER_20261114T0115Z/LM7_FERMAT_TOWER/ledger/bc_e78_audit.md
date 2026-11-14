# Independent audit of E.78

**Result: PASS.** The complete written proof was read, and a fresh copied execution of `a_wild_class3.py` completed with exit code zero. Its entire JSON output is byte-identical to the author’s frozen output; no field was omitted or normalized. The archive retains the matching source and JSON in code/a_wild_class3.py and code/a_wild_class3.json, and the independent stdout in code/bc_e78_a_wild_class3.out.

## Arithmetic and group maps

The conjugation of the E49 Frobenius generators preserves their free-basis property and gives the stated Kummer values. The root identity for the tangent parameter gives the two exact operators with parameters −5/2 and 1/2. The map from E77’s actual wild presentation is used before the Hall-coordinate calculation. The class-two and class-three relation defects, the factor 336 in central changes, and the complete stabilizer calculation all agree with the proof and independent computations.

The intrinsic examples use an actual cusp path. Conjugating its inertia to the chosen target generator and multiplying its accompanying Frobenius value by a cusp power preserves the exact relation. Central changes in the intrinsic class-two quotient then give every displayed family member. Thus the no-lift example and the full lift at the specified member follow through actual quotient maps. They do not use surjectivity alone as a section-lifting argument.

For an explicit origin comparison, the rational automorphism swapping x and z sends E34’s cusp P=[0:−1:1], with s=−x/z, to E78’s O=[1:−1:0], with s′=z/x=−s. All compatible pro-3 roots of −1 can be chosen equal to −1 over Q. The resulting Galois-invariant comparison of local tangential paths transports the full based N-action. This is an optional clarifying sentence, rather than a correction to the theorem.

## Independent execution

The fresh run reproduces 640 Hall–Magnus identities, eight actual source/root transports, 67 class-two and seven class-three lifts, and all 180/201/35 inverse coordinate checks in the three fiber calculations. The symbolic intrinsic-path transport retains its unknown higher coordinates. Every JSON field matches.

## Opened primary passage

Furusho’s original Annals PDF was opened at Theorem 2 and equation (5), printed p.547, and the proof in Section 3, printed pp.554–555, with Corollary 12. The precise arithmetic coefficient used here follows through the established E54 comparison.

Source: https://annals.math.princeton.edu/wp-content/uploads/annals-v171-n1-p13-p.pdf

## Frozen hashes

- `a_wild_class3.py`: `bf3ac6fedf08a9dcb714f7338c9f2450d79f91204ee379b7df38c67d3ccc101e`.
- `a_wild_class3.json`: `6ddad0a5f09f45af030b1cbfc9cab437018a387a34609ada9a5a548693c881a0`.
- `E_wild_class3.tex`: `0a821fbe940f636eb49721707ac014412edc292853c4a5e0e587ef40a3be377e`.

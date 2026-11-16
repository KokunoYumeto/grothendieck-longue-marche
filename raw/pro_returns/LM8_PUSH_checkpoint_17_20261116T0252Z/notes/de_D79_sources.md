# D.79 dependency, source, and exact-computation ledger

**Unregistered, notes only during the checkpoint12 source freeze.** Full stable candidate: `notes/de_sha_matrix_family_draft.tex`. Exact code and outputs: `notes/de_sha_matrix_family_certificate.py/.json/.out`. No diagnostic PDF.

## Exact scope

The candidate determines the whole separated compact kernel for every invertible Z5 matrix recombination of κ2 and κ3. It distinguishes three unit local slopes, a finite positive boundary depth, and an exact boundary. The retained inverse finite-localization kernel is Z/5 in the first case and zero in the other two; the full compact kernel is respectively Z/5, Z5^d, or the countable compact product. General section existence and the extension by the residue space remain separate questions.

## Established arithmetic and primary inputs

- **verified:** D.78's actual H⋊I0 operator-image computation, its local Frattini/Kummer saturation proof, continuous coinduction, and finite-image Chebotarev descent. The same proof applies to the two invertible matrix columns. The freshly checked underlying primary sources are Milne ADT I.4.10(a), `turn1023view3`, and Milne CFT V.3.23, `turn1023view4`; URLs https://www.jmilne.org/math/Books/ADTnot.pdf and https://www.jmilne.org/math/CourseNotes/CFT.pdf .
- **verified:** D.31/D.39 actual beta normalization and exact peripheral values. The degree-two coefficient is (χ²−1)uv/24. The unramified image and raw Soulé convention were freshly checked in Nakamura–Sakugawa–Wojtkowiak (1.1)–(1.2) and the following paragraph, `turn1022view1`, https://arxiv.org/pdf/1410.1045 . No unknown higher coefficient is assigned a value in this proof.
- **verified:** D.77 gives the whole actual local invariant group, including its divisibility, for all boundary depths. Its primitive local multiplier supplies the exact distinguished-polynomial annihilator used in the new proof. D.63 is the precise topological compact-kernel definition. D.74 supplies the conditional torsor statement for a nonempty finitely ramified fibre.

The tripod S3 comparison is proved using the actual rational automorphisms, transported tangential frames, and their inner gauges. The Kummer coordinate changes are written explicitly, including why the sign class vanishes at five. PBC separately confirmed that this gives an isomorphism of the actual twisted module and global/local cohomology diagrams, rather than only a formal coordinate permutation.

## New uniform argument

At boundary depth d≥1, Q=z²((1+z)^(5^d)−1). Its primitive local multiplier annihilator reduces the entire possible restriction kernel to a subgroup of F5. The actual arithmetic action on the finite line quotient is determined by the exact boundary restriction and its first two Taylor coefficients. Their formulas A_gamma and B_gamma both contain gamma−1 with five-integral coefficients.

For the actual power with gamma=2^(4·5^(d−1)), reduction modulo five gives an exact top term 2z^(5^d+2) in the image of gamma^−1 rho−1 applied to z³. Hence no invariant order-five functional detects Q. The preexisting invariant subgroup is divisible by D77, so any nonzero possible finite quotient would have an order-five lift. This contradiction excludes the entire restriction kernel, including possible lifts of higher order. The argument is uniform in d and in the two unit line coefficients.

## Executed computation

The certificate symbolically derives both Taylor coefficients from the two exact S_gamma factors and the degree-two beta term. Exact Lucas arithmetic checks the actual powers at depths1–6 and ten unit values; independent quotient matrices at depths1–3 have the expected residual dimensions. All480 GL2(F5) matrices are enumerated, with240 matrices in each residual slope case. The finite ranks are supporting checks only; the displayed all-depth operator identity and the divisible-group argument prove the theorem.

The earlier exploratory `de_sha_line_probe.py/.out` is retained. It suggested the boundary-depth distinction but is not cited as a proof or substituted for the uniform certificate.

## Integration after checkpoint12

D.79 is now Proved in `sections/D_alexander_matrix_family.tex` after root, FGH, and PBC full independent proof/source/exact-certificate audits. Canonical certificate: `code/de_sha_matrix_family.py` with adjacent JSON/stdout. The original candidate and all audit versions remain unchanged. No diagnostic PDF was created.

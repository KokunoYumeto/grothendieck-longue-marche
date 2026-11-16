# D77 candidate: source and dependency ledger

**Unregistered, notes only, pending full independent audit.** Candidate: notes/de_local_boundary_draft.tex. No diagnostic PDF was produced.

## Fresh primary checks

- **verified:** Nakamura–Sakugawa–Wojtkowiak, *Polylogarithmic analogue of the Coleman–Ihara formula, I*, arXiv v3, https://arxiv.org/pdf/1410.1045 , reopened November15 2026, browser ref turn979view0. Equations(1.1)–(1.2), manuscript page2, give the raw Kummer normalization on the cyclotomic kernel and the beta logarithmic coefficient. For p5 and weight3 the coefficient of uv(u+v) is κ3/48. This is the same exact normalization already proved in D35/D39. The local nonvanishing in this candidate is proved directly by the Eisenstein valuation calculation; no Coleman–Ihara special-value formula is used.
- **verified:** Milne, *Arithmetic Duality Theorems*, second edition, https://www.jmilne.org/math/Books/ADTnot.pdf , reopened November15 2026, browser refs turn979view1 and freshly located exact I.2.1/I.2.3 statements turn980view1/turn980view0. D63 already proves the exact finite-local duality and inverse-limit consequences used here from I.2.1/I.2.3 and I.4.10. The retained term is precisely the inverse limit of the finite global localization kernels in D63.5.

## Exact internal dependencies reread

- D35: actual twisted Fox multiplier for every abelian pair, raw unit factorization, and κ3/48 leading coefficient.
- D39: full beta factorization and exact diagonal reflection identity. In particular beta is1 on each of the three boundaries when chi1.
- D63: topological compact kernel, its exact sequence with the inverse finite-localization kernels, and the actual local/global Cartier-dual identification.
- D75: full affine image, all invariant functions modulo constants, compatible local/global gauges, and the logarithm formula for every completed Kummer class.
- D76: the actual three axis modules, integral rank3 relation cokernel, measure-polynomial degree bound, and the degree2 doubling argument.

## New arguments proved in the candidate

The local classes of φ and ζ5 are independent modulo fifth powers: after taking fourth powers, their nontrivial combinations have depth1 or2, while principal fifth powers have depth at least5. Thus the raw κ3 remains primitive on the local cyclotomic kernel. The actual compact image of(a,b,κ3) admits the integral C4 projector onto its third coordinate, yielding a realizable local δ with a=b0 and primitive κ3. Its multiplier minus1 is exactly uv(t1t2−1) times a unit.

Every invariant Cartier functional therefore factors through the union of the three boundaries. The finite relation module has characters chi2,chi2,chi3, hence its Cartier dual has characters chi−1,chi−1,chi−2. For an actual local/global element k with chi(k)=2, k−1 is invertible on that dual; the determinant is −3/16. The unique k-fixed lift of an invariant boundary functional is fixed by the whole cyclotomic kernel by the degree2 polynomial-defect calculation, then by the whole group since2 topologically generates Z5×. Thus the axis sums give the entire invariant groups, naturally for both global and local Galois groups.

The only uncomputed compact term after this candidate is the exact inverse limit S_s in D63.5. No assertion that it vanishes, no arbitrary-pair section-existence assertion, and no explicit first derived obstruction are made.

## Certificate

notes/de_local_boundary_certificate.py/.json/.out checks the24 exact nontrivial Kummer combinations in the Eisenstein ring, the raw first Soulé unit identity, the integral image projector, the rank3 jet matrix and Cartier determinant, and the order20 of2 modulo25. The infinite and cohomological statements follow from the written proof, not finite experimentation.

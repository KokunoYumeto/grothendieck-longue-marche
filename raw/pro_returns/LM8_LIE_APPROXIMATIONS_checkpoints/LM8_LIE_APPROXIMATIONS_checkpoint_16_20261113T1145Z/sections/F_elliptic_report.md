# Elliptic supplement to Part F(c): verification report

**COMPLETE through class eight for the stated two curves, prime, and local conditions.** Statements F.6–F.9 are proved. The separate exact arithmetic calculations F.16–F.18 establish every required dual Selmer vanishing. Both the full and metabelian global tables are therefore unconditional, as are the first strict dimension thresholds.

## Deliverables and scope

The manuscript is `sections/F_elliptic.tex`, with four reserved identifiers F.6–F.9. References, results, coverage, and readings are in the corresponding `F_elliptic_*` files. The executable computation is `code/f_elliptic_dimensions.py`; its actual results are saved as JSON, CSV, and `.out`. The metadata writer is `code/f_elliptic_metadata.py`.

The manuscript anchors are the end of §51, folio 734/scan 173 and folio 736/scan 178, and the type-(1,1) structures in §52, folios 743–746/scans 191–197. The calculations use explicit modern Selmer conditions; no ambiguous manuscript letter is used as an arithmetic theorem.

## What is unconditional

The examples are `E1: y²=x³−x` and `E6: y²=x³−36x`, both at the good ordinary prime 5, with rational base point `(0,0)`. Their ranks are exactly 0 and 1. Monsky's descent matrices have pure 2-Selmer nullities 0 and 1. On E6 the point P=(12,36) has 2P=(25/4,−35/8) and 8P≠O. Exact counts at 5 and 7 show that rational torsion has order dividing 8, proving P is not torsion. These operations are independently executed in the supplied program.

The full ordinary p-adic Selmer ranks equal the Mordell–Weil ranks. This uses a distinct input: LMFDB entries 32.a3 and 576.c3 give analytic ranks 0 and 1, and its reliability statement explicitly says that these analytic-rank computations are rigorous in the conductor/rank range at hand. Kolyvagin's own primary manuscript MPI/90-69, Theorem 1 on printed page 4, then gives finite Tate–Shafarevich groups. The inequality sign in the theorem was checked directly on the rendered source page after OCR omitted it. The manuscript does **not** infer finite 5-primary Sha from a 2-descent, or use the rounded analytic order of Sha as proof of its order.

Exact local dimensions through classes 1–8 are:

| Quotient | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Full free | 1 | 2 | 4 | 7 | 13 | 22 | 40 | 70 |
| Free metabelian | 1 | 2 | 4 | 7 | 11 | 16 | 22 | 29 |

The underlying geometric graded dimensions, complex-conjugation traces, minus eigenspaces, and every CM bidegree multiplicity are checked exhaustively through length 8. The program enumerates all binary words at those lengths, selects Lyndon words, and checks the character-Witt formulas. This computation is genuinely exhaustive in that finite range. It does not enumerate Galois cocycles, sample Hecke-character Selmer groups, or prove any arithmetic vanishing.

For the specified refined global spaces, the exact maximal dimensions at classes one and two are `r` and `r+|S|`. Here S means primes at which denominators are allowed. Bad primes outside S retain their integral local conditions; they are not silently counted as extra unit dimensions. This matters for E1 at 2 and E6 at 2 and 3. The class-two equality is proved using the involution fixing the chosen base point, a Galois-equivariant splitting of the class-two Lie algebra, a cocycle of the non-torsion point, and the independent valuations of rational S-units. The maximal component is obtained by choosing the cuspidal local reduction type at each denominator prime. Other reduction-type components can have smaller dimension.

Rank zero therefore gives a strict dimension inequality already at class one for |S|=0,1,2. Rank one with S empty gives it at class two. These yield unconditional finiteness by Kim's density theorem and the analytic zero argument. For E1 the entire rational group is explicitly determined, so the S-integral affine points are exactly `(−1,0),(0,0),(1,0)` for every S.

## The arithmetic obstruction and its evaluation

For a full free central layer L_n=Lie_n(V), n≥3, define

`δ_n(E)=dim H_f^1(Q,L_n^*(1))`.

There is a separate metabelian defect with its central layer. Poitou–Tate gives the exact strict graded dimension

`h_f^1(Q,L_n)=dim(L_n)^(c=−1)+δ_n(E)`.

This is an equality with the actual named invariant. Potential good reduction and weights imply that all non-p local H¹ and H² vanish in these degrees. At p all central H¹ classes are crystalline, while the dual-twist local finite group vanishes. Consequently δ_n is dual to the obstruction group `H²(G_Q,T,L_n)`. Its vanishing makes every lower Selmer class lift, with a fibre of exactly the indicated vector-space dimension. F.18 proves the vanishing in every required degree, so the numerical tables in F.9 are **equalities**.

With all relevant defects through class eight zero, the full-free baseline above class two is `0,1,3,6,11,20,36`; the metabelian baseline is `0,1,3,5,8,11,15`. Add `r+|S|` at classes 2–8 and use r at class one. All twelve tables are saved in the computational JSON and both sets of six rows appear in the manuscript. The first strict inequalities for rank one are classes 2,3,4 for |S|=0,1,2, unconditionally: class 2 is F.8, and the exact calculations F.16/F.17 prove δ3=δ4=0 for both examples. The full and metabelian groups coincide through class 4.

F.16 proves δ3=0 by an exact odd-branch modular-symbol calculation and Kato’s rational cyclotomic bound; F.17 proves δ4=0 using the weight-three level-16 CM form and a separate Artin–Tate argument. F.18 completes degrees five through eight, for both examples and both towers. It decomposes every dual layer into `W_m(−t)=Ind ψ^(−m)⊗χ5^(−t)` with `m+2t≤6` and explicitly counted Artin–Tate summands. Exact polynomial Manin-symbol systems at levels 32,16,32,4,32,16 produce nonzero modulo25 specializations for all twelve required pairs (m,t), including the values divisible by5. Each vector lies in a single checked parity period line. Kato’s height-one bound then makes the corresponding specialized cyclotomic Selmer coinvariants finite. Finite ramification and bounded restriction kernels rule out a nonzero divisible image of the rational finite Selmer space. The Artin–Tate summands vanish by the verified Soulé argument. Full matrices, paths, distribution checks, period involutions, and specializations are saved in the `F_advanced_cm_power_*` certificates; the complete proof and source audit are in `F_advanced.tex` and `F_advanced_report.md`.

The first defect concerns `H_f^1(Q,V^*)`, so the arithmetic calculation is separate from the Mordell–Weil rank input. The proof uses the exact dual representation and local conditions throughout. For other curves or primes, the displayed structural formula still requires evaluation of the defects and, when a defect is nonzero, the nonlinear obstruction map. Those broader cases are outside the stated finite computation.

## Alternative approaches checked

Bars (2007), Definition 2.2 and Corollary 2.9, proves the requisite second-cohomology vanishing under geometric regularity for E and K(E[5]). That regularity is not verified in this package. It is a concrete alternative hypothesis, not an unconditional fact about the chosen prime.

Kim (2010), Theorem 0.1, gives an unconditional eventual dimension inequality for a smaller CM quotient W; Theorem 0.2 gives an explicit level under specified p-adic L-value nonvanishing. The quotient kills bidegrees with both entries at least two and factors through the free metabelian quotient. It therefore supplies an alternative unconditional eventual finiteness argument, after enlarging S by the bad primes when needed. The exact full-free and full-metabelian tables through class eight instead use F.16–F.18.

## Numbering and source safeguards

Kim (2009), Theorem 1 on page 93, is a density theorem. The finiteness criterion is the deduction in §3; no numbered finiteness theorem is invented. Kim–Tamagawa (2008), Theorem 0.1 and Corollary 0.2, give the finite non-p integral images, and Corollary 0.3 plus §2 gives the elliptic rank-at-most-one application. Their U3 is the present class two. Kim (2010) changes to the present convention.

The modern refined comparison is supported by Leonhardt, Lüdtke, and Müller (2023), Theorem A, Remark 1.4, Lemma 3.2, and formula (5.6). Betts (2023), Corollary 3.1.11 and Theorem 6.2.1 A+B, verifies the local parameter spaces and the effective finiteness implication. For general elliptic curves with unknown Sha, the Mordell–Weil-restricted refinement of Remark 1.4 remains available; for these two curves finite Sha is established independently, so it is not necessary to replace the ordinary Selmer rank.

Any transfer to LM6 must retain the named curves, the prime5, the actual arithmetic Galois action, the refined integral/cuspidal local conditions, crystallinity at5, and the degree bound eight. Under these hypotheses F.18 supplies the required δ-vanishing. A normalizer calculation or an equality of Lie dimensions does not supply the arithmetic input for other settings.

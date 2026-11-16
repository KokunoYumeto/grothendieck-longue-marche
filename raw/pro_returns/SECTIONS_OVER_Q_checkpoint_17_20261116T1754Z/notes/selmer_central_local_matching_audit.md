# A205: exact central correction and fourth-weight matching

## Scope

Draft: `sections/selmer_central_local_matching.tex`. It remains unintegrated pending root and peer review. The finite certificate checks only explicit arithmetic; the source proves the continuous cohomology, centralizer, compactness and actual local section maps.

The global lift fibre above a fixed lower section is the actual continuous H1 torsor, because its geometric centralizer vanishes globally and at every finite place. At the real place the source retains the exact centralizer-to-H1 translation homomorphism. Local allowed sets are built from actual full point/cusp sections with chosen lower alignment; finite places retain up to three cusp labels.

Every integral Tate-weight cocycle of weight at least three is unramified away from its coefficient prime. Thus the full correction module is the product of compact fixed-support H1 modules. The simultaneous local matching problem is exactly a closed intersection, with finite-intersection solvability equivalent to full solvability.

## Exact fourth-weight calculation

A61 supplies the unramified H2 bound. Finite-coefficient Euler characteristic, with the same real normalization as A40.10, bounds the finite H1 groups. Their inverse limits are finite; dividing an annihilated cocycle gives the exact fractional-coboundary isomorphism from invariants in (Q_l/Z_l)(4). The fourth-power ideals have orders 16,3,5,1, giving C240 with literal generator (chi^4-1)/240. Every finite-place restriction is injective. The actual localization map to (Q3,l2),(Q2,l3),(Q2,l5) is k -> (k/3 mod16,k/16 mod3,k/16 mod5).

The fourth layer has rank three, giving 240^3=13,824,000 global classes. These three projections select one class after the corresponding local geometric images have been chosen. They do not prove the other local conditions. A failed full matching problem has a finite witness; an ordinary image at one finite place reduces the candidates to at most one.

## Primary pointers and exact dependencies

- Milne, Arithmetic Duality Theorems, I Theorem 4.10(c), Corollary 4.15, Theorem 5.1: fixed-support finiteness, higher real cohomology and the Euler characteristic. URL: https://www.jmilne.org/math/Books/ADTnot.pdf . Existing verified key BIR_MilneADT. A40.10 is the already checked identical real normalization.
- Jannsen, Continuous Etale Cohomology, (1.6), Theorem 2.2: actual inverse-limit/derived-limit comparison. URL: https://epub.uni-regensburg.de/26684/1/jannsen12.pdf . Existing verified key BIR_Jannsen1988.
- A60: exact local Frobenius H1 quotient and coefficient-specific matching maps. A61: unramified weight-four H2 and its retained real kernel. A204: existence of a global class-four lift for an all-place locally matching class-three section.
- Weibel, The K-book, VI 8.1--8.2 and 9.11 were reopened in the author PDF during this investigation. The proof does not identify H1 with K7 merely by matching cardinalities and does not need such a comparison. URL: https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.pdf .

## Executed certificate

`code/selmer_weight_four_matching_certificate.py` and its retained output/data prove the literal one-cocycle identity, finite fourth-power ideal checks, all 240 distinct CRT images, prime-to-residue restriction orders, and actual finite real-H3 reduction transitions. No continuous theorem is inferred from these finite tests.

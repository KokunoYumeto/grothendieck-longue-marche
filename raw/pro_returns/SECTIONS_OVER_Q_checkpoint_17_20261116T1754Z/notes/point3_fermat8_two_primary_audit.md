# A187: exact maps and primary source audit

Source: `sections/point3_fermat8_two_primary_selmer.tex`.

The isogeny Selmer orientation is explicit: alpha_b on E_b(k)
computes Sel^psi(E'_b/k), where psi:E'_b->E_b. The dual alpha
computes Sel^phi(E_b/k). The proof gives an isomorphism of each
quartic cover with E'_b over k(sqrt(d)), its inverse, and the
literal kernel-point conjugation. All necessary local filters in
A185 apply to the entire isogeny Selmer group, and all survivors
are attained globally. Both isogeny Sha kernels therefore vanish.

For each Prym, the proof uses unscaled elliptic targets for the
Galois descent, so conjugation exchanges q_+ and q_- literally.
The sum of their pullbacks is defined over Q, and
`g_P f_P = 2 + j_+ + j_- = [2]` on the actual anti-iota part.
After the actual Shapiro/local-decomposition maps, this kills the
full two-primary Prym Sha group by two.

For the A182 isogeny F, its kernel order is N=deg(F). The inverse
up to N is defined on the quotient by `G(F(P))=[N]P`. This gives
the concrete bound `2^(v2(N)+1)` on Sha(J8)[2-infinity]. A187 does
not claim a numerical value for N. Its continuous comparison is
proved by finite cocycle and zero-cochain inverse limits, rather
than an assumed fixed global ramification condition.

## Reopened original source

Milne, *Arithmetic Duality Theorems*, second edition (2006),
<https://www.jmilne.org/math/Books/ADTnot.pdf>:

- I, Corollary 4.15, printed page 62 (PDF page 70), proves
  finiteness of cohomology for a finite S and a finite module
  whose order is inverted. In A187 two is included in S.
- I, Proposition 6.4, printed page 75 (PDF page 83), gives the
  exact finite Mordell--Weil/Selmer/Sha sequence.
- I, Corollary 6.6 and Remark 6.7, printed pages 76--77
  (PDF page 85), compare the finite-S and all-place groups
  and conclude finiteness of the finite torsion of Sha.

These passages were reopened in the author's original PDF.
The existing bibliography key is `BIR_MilneADT`.

## Retained certificate

`code/point3_fermat8_two_primary_maps_certificate.py` checks
the actual quartic-torsor equation, inverse, psi composition,
kernel-point conjugation, both reciprocal quotient equations,
all four involution/quotient signs, and exact multiplier two.
Output and JSON data are retained beside it. The complete
arithmetic inputs remain the independently audited A185/A186
rank and squareclass certificates.

The conclusion is the exact global two-adic Selmer image of J8.
The transfer from a local Chabauty zero set to a classification
of full sections is not supplied by this argument.

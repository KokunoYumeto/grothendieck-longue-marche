# Further primary-source audit of the missing cubic étale regulator

Date: 16 November 2026. AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode).
This is a record of attempted routes, not an evaluation of the missing coefficient.

## Exact texts opened

1. Kings, G. (2001), *The Tamagawa number conjecture for CM elliptic curves*,
   Inventiones Mathematicae 143, 571–627, DOI 10.1007/s002220000115.
   Primary text: https://arxiv.org/pdf/math/0003113, author preprint of March 2000.
   Theorem 1.1.5, author p. 7, explicitly requires p different from 2 and 3 and
   p not dividing the norm of the CM conductor. Proposition 5.2.1 again uses
   p not dividing 6 N(f). The elliptic-polylogarithm specialization in §4.2.9
   cannot silently remove these hypotheses in the arithmetic lattice comparison.
   The theorem is therefore not an evaluation at coefficient prime 3 for E27.

2. Johnson-Leung, J., and Kings, G. (2011), *On the equivariant main conjecture
   for imaginary quadratic fields*, Journal für die reine und angewandte
   Mathematik 653, 75–114. Primary text: https://arxiv.org/pdf/0804.2828.
   Theorem 5.2 gives the characterwise main conjecture at all primes.
   Theorem 5.7 makes the equivariant determinant statement conditional on
   Conjecture 5.5, the stated height-one p-primary vanishing condition.
   Corollary 5.12 proves that condition for split p not dividing 6.
   Even the all-prime characterwise theorem does not identify the actual
   integral Ross-symbol Frobenius class used by B.4: the motivic comparison,
   integral normalization, specialization and comparison with the specified
   nonabelian action extension still have to be supplied. We do not infer an
   unknown étale scalar from equality of real regulators.

3. Asakura, M. (2023), *New p-adic hypergeometric functions and syntomic
   regulators*, Journal de théorie des nombres de Bordeaux 35(2), 393–451,
   DOI 10.5802/jtnb.1250.
   Published primary PDF: https://www.numdam.org/item/JTNB_2023__35_2_393_0.pdf.
   Theorem 4.11, p. 436, gives a Ross-symbol formula under p > max(N,M).
   For the cubic N=M=3 it does not apply at p=3. Conjecture 4.17 explicitly
   records a nonvanishing expectation for the relevant hypergeometric value
   under that theorem's own good-prime assumptions. No bad-prime value is
   obtained by substituting 3 in this formula.

4. Nemoto, Y. (2025), *L-function of CM elliptic curves and generalized
   hypergeometric functions*, International Journal of Number Theory 21(4),
   793–808. Primary author version: https://arxiv.org/pdf/2309.01059,
   version 2, 18 April 2024. Introduction, author pp. 1–2, explicitly
   distinguishes equality of real regulators at conductor 27 from the
   motivic equalities proved for conductors 36 and 64 in Propositions 4.3
   and 4.10. This does not close the conductor-27 étale comparison.

## Sources located with incomplete access

5. Besser, A. (2021), *The syntomic regulator for K2 of curves with arbitrary
   reduction*, in *Arithmetic L-Functions and Differential Geometric Methods*,
   Progress in Mathematics 338, 75–89, DOI 10.1007/978-3-030-65203-6_3.
   The author publication list and publisher page were opened. The publisher
   two-page preview at
   https://page-one.springer.com/pdf/preview/10.1007/978-3-030-65203-6_3
   was also opened and read. It defines the Vologodsky triple-index regulator
   candidate in (1.5), states Conjecture 1, and says the main result proves it
   under an additional hypothesis on the differential. That hypothesis begins
   after the accessible preview. The complete theorem was not opened; we do
   not claim it applies, and no numerical Vologodsky integral is supplied.
   The plausible next route would require the full theorem, a checked
   differential satisfying its hypothesis, an explicit potentially semistable
   model at 3, a certified integral evaluation, and the integral étale comparison.

6. Nemoto, Y. (2026), *On the syntomic regulator of the Hesse cubic curves
   and p-adic hypergeometric functions*, arXiv:2609.10340.
   The arXiv search metadata and the author's Waseda publication profile were
   found; an indexed version is v3. The abstract advertises Hesse-cubic
   syntomic formulas. Attempts to open the unversioned and v3 abstract/PDF/HTML,
   source endpoint and export PDF failed. The theorem text and hypotheses
   remain unverified. We neither assume that it excludes p=3 nor assume
   that it includes p=3. It cannot yet be invoked to settle B.4.

## Algebraic route checked separately

B.32 proves that the inherited tripod metabelian quotient kills the compact
determinant extension whose actual class is needed. The compact transfer
vectors lift to F', their commutator lies in F'', and the entire extension
cocycle vanishes in N/(F'' gamma_4 N). Thus direct use of the Jacobi-sum
action on F/F'' loses this particular datum. A reconstruction using extra
information is not ruled out, but no such reconstruction is proved here.

The smallest still undecided finite local question in B.31 is the order of
the actual class at 2: its exponent m_2 satisfies 0 <= m_2 <= 4, but the
computed coefficient-group exponent does not determine the class order.
The exact local matrix, its full Smith certificate, the convergence condition
and all nonempty class-three fibres are recorded in B.28 and B.31.

## Update at 03:45 UTC

B.35 now proves m_p>=1 at every good prime, including an integral non-inner
class at2. The exact m_2 remains in {1,2,3,4}. This supersedes the lower
bound zero in the preceding research-state paragraph. The actual rational
Ross coefficient remains unevaluated. A fresh attempt to open arXiv's
version3 PDF and HTML, export version1, and the ar5iv representation again
failed; search metadata is not substituted for theorem text.


### Update at 04:08 UTC: exact local order

B.36 has now passed independent proof and computation audits. The actual local class at two has exact order 27, so m_2=3, superseding the earlier interval 1 through 4. The framed generalized-Jacobian/path comparison is proved, not assumed. This conclusion alone does not prove rational global nonvanishing. Two independently executed quotient calculations additionally exclude every one of the 27 local candidates from the local image of global torsion; the ensuing automorphism projection to the Ross summand is under final proof audit in B.37.


### Arithmetic nonvanishing resolved in B.37

The B.37 argument and its independent audit now prove that the actual rational Ross cup-edge is nonzero. The exact comparison scalar is −1 relative to that specified edge (−1/6 relative to its tame multiple). This supersedes the earlier statements that arithmetic nonvanishing itself remained unproved. It does not remove the recorded source-access limits, claim a primitive integral generator, or evaluate the complete integral global Frobenius cocycle. The root auditor checked the five-entry mod-nine functional, both independently executed quotient calculations, all commutator multidegrees, the Galois-equivariant automorphism average, and the direct bad-prime-three computation of the one-dimensional arithmetic space.


## Subsequent resolution by the actual geometric extension

The source search and remaining-regulator remarks above record an earlier stage. B.37 proves arithmetic nonvanishing and identifies the action coefficient as -1 relative to the explicitly specified arithmetic Ross edge. B.40 subsequently computes the actual integral refinement from the multiplication-by-three cover and its full geometric automorphism extension, selecting b+6h9. The intrinsic detectors are57 modulo81 and19 modulo27. Thus B4 andLead3 are resolved in their requested arithmetic/integral scope without invoking an inaccessible syntomic formula. No numerical three-adic regulator is claimed. The full arbitrary-input class-three image is a separate open task.

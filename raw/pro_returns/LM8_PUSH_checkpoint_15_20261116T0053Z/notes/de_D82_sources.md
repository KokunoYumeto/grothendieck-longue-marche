# D.82 exact source, dependency, and computation ledger

**UNREGISTERED candidate.** Full proof: `notes/de_sha_valuation_draft.tex`. Exact certificate: `notes/de_sha_valuation_certificate.py/.json/.out`. No diagnostic PDF.

## New actual-image input

**verified:** Nakamura--Sakugawa--Wojtkowiak, original equations(1.1)–(1.2), freshly reopened in full at turn1052view0, https://arxiv.org/pdf/1410.1045 . Equation(1.1) on the cyclotomic kernel makes every raw odd Soulé character vanish when the actual beta series is1. Equation(1.2) is exactly the product of(1−zeta^a) with exponent a^(m−1). For m=1+4*5^(r−1), the exponent is1 mod5^r; the product is Phi_(5^r)(1)=5. This proves kappa(5) vanishes on the actual operator kernel and hence descends continuously. No limiting global integral cochain, special-value theorem, or unnamed reciprocity assertion is used.

The local image of kappa(5) on ker chi is Z5 by the elementary valuation4 versus cyclotomic Kummer line argument over Q5(zeta5). D78 supplies local surjectivity onto I0 and the exact unit-Kummer saturation. The proof keeps the valuation cocycle graph, rather than replacing it with an incorrect zero-translation complement. The new N1 quotient is the actual full affine group Z5(1) semidirect Gamma. Its H1(lambda) vanishing follows from the explicit weight−2 homomorphism module and the order-four averaging argument.

## Previously established inputs at their exact scope

- **verified:** D77's actual primitive local Soulé image and integral projector give an element in N1 with beta−1=P times a unit. Its full local-invariant calculation gives the divisible subgroup required to extract an order-five witness.
- **verified:** D81's elementary annihilator calculation and exact four-term dual sequence apply to the unit line even when nonprimitive or zero. The additional valuation translations have augmentation1, so the connecting character remains chi5.
- **verified:** D79's actual cyclotomic-power formula applies to any actual multiplier-two element. The written proof recalls the stronger order-five functional consequence, including exact boundary and all-depth finite boundary cases. The actual geometric boundary permutations preserve the augmentation and product-boundary ideals.
- **verified:** D80's finite local Tate/ML argument and one-common-finite-level construction apply away from five with arbitrary ramification. Existing primary Milne ADT I.Corollary2.3, printed28, https://www.jmilne.org/math/Books/ADTnot.pdf , was checked at turn1039view0 and again by all D80 auditors.
- **verified:** D74 is used for the explicitly realized point t=10 and the finite-support examples only; it gives no arbitrary section-existence conclusion.

## Executed exact certificate

The certificate checks all raw exponent congruences at levels1–6 (15624 unit exponents total), the three actual nonboundary line quotients and their unique cubic primitives, and all300 twisted residual actions on their pullbacks to the full ten-dimensional Cartier module. It also checks all20 zero-span operators, all625 local residual matrices (1 zero,72 nonboundary lines,72 boundary lines,480 full rank), and the actual point t=10 local/global coordinates. It uses the previously audited exact Fox multiplier rather than a formal graded replacement. The coinduction, whole-kernel bound, and all-depth boundary argument are written proofs, not inferred from the finite counts.

The hypothesis is specifically rank2 of inertia away from five. Globally independent pairs whose away-five inertia has smaller rank are not included. No new diagnostic PDF was created.

## Integration

Root, FGH, and PBC complete independent proof/source/certificate audits PASS. Canonical sections/D_alexander_valuation.tex and code/de_sha_valuation.py/.json/.out integrated after root authorization; the canonical rerun equals the entire audited candidate JSON. Original draft retained. See notes/root_D82_audit.md, notes/fgh_D82_audit.md, and notes/pbc_D82_audit.md. No new source or diagnostic PDF.

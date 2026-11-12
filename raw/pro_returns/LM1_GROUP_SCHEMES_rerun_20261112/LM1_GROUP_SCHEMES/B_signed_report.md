# Signed general construction: supplemental report

| Task contribution | Outcome | Statements | Exact scope |
|---|---|---|---|
| A.a, signed definitions | Proved for the identified formal construction | B.13 | The two distinct groups B and Z, quotient G, signed normalizers, starred normalizers, Gamma, M, S0Gamma and S0M are explicitly defined and matched to C3:530–560. This does not claim a complete audit of every symbol in §§49.V–VI. |
| A.b, signed formulas | Refuted and corrected where indicated | B.13–B.14 | The side of the sign factor, the inverse in the conjugator formula, and the centralizer in the starred exact sequence are corrected; the finite models verify the resulting identities. |
| B.c, signed exact sequences | Proved for the formal construction and the finite constant group schemes | B.13 | Exact kernels and all the fibre-product sequences of C3:559–560 are proved. The starred normalizers inject even when a generator has order 1 or 2. |
| B.g, full requested comparison | Partly settled | B.13–B.14, together with parent B.8/A.9 | The signed formal part and four finite quotients are complete. Universal signed realization and identification with all of the integral matrix-scheme dictionary remain separate questions; the distinct residuals are source-indexed in B.8.5 and B.15–B.18. |

## Mathematical result

The theorem treats both the linked-sign group B of scan 530 and the enlarged group Z of scan 549, in which the two signs are retained as independent numerical data. It imposes the common modular relation rho cubed = sigma squared = omega, rather than just separate order conditions. It retains the kernel L0 intersect Z(C) before assuming it trivial for the embedded quotient construction.

The signed normalizer is represented unambiguously by pairs (g,e) with gxg inverse = x to the e power. Its projection to G has a kernel of order two exactly when x squared is one. The condition e = chi_x(delta(g)) defines the starred subgroup; its projection is always injective and its exact kernel over gamma is C_C(x). The sign kernel in the starred group is Z_x intersect ker(chi_x delta), which can be strictly smaller than Z_x. S3 supplies an explicit counterexample to using the unrestricted centralizer.

The numerical kernel of Z to Aut(C) is exactly Lambda times E_rho times E_sigma, where Lambda consists of the multipliers fixing the loop generator and E_x consists of the signs for which x and x to that sign are conjugate. This numerical redundancy is distinguished from the manuscript's effectivity condition: effectivity means existence of an automorphism with the proposed generator images. The effective conjugator space is parametrized by S0Gamma, with a proved inverse and fibres C_rho times C_sigma. No realization hypothesis is silently deleted.

## Sources opened

The supplied checked transcriptions of C3:530–560 were read, including the definitions at 530, 549, the preliminary conjugator fibres at 542–545, and the revised starred groups and fibre products at 555–560. The attached photograph `background/scans/140-3/scan546.jpg` was opened directly. It places the orientation-reversing factor on the left in (64). The calculation in B.14 proves that the right factor is required by the displayed conjugation convention. No new external theorem or claim of priority is used. The abstract profinite topology reduction refers to the proof already supplied in B.11.

## Computation executed

`code/AB_signed_finite.py` is standalone Python. It builds S3, S4, SL2(F3) and SL2(Z/4), enumerates all automorphisms from generator images by full Cayley-graph consistency, builds both signed groups with numerical group U12, forms the actual antidiagonal quotients, and checks all normalizer images, kernels and starred fibres. It also enumerates all numerical loop solutions independently and verifies their effectivity in each of these four models. Every value of the conjugator parametrization and its inverse is checked. The output is saved in `AB_signed_finite.out` and `AB_signed_finite.json`; all assertions pass.

The automorphism orders are 6, 24, 24 and 48. The linked-sign B12 orders are 8, 16, 12 and 16; the enlarged Z12 orders are 32, 64, 24 and 32. The numerical kernels of the projections to automorphisms have orders 4, 2, 2, 2 for B12 and 16, 8, 4, 4 for Z12. Both signs can collapse in S3 and S4; the rho sign remains distinguishable in SL2(F3), and the sigma sign remains distinguishable in SL2(Z/4). These finite numerical groups are expressly separated from the full profinite groups, which are their fibre products with Zhat units over U12.

For scan 546's side-of-factor error, the program checks beta=rho over F3. Left multiplication by tau-prime gives the conjugated matrix [[2,2],[2,1]], while the required negative conjugate, obtained by right multiplication, is [[2,1],[1,1]].

## Scope of completion

The identified signed formal construction now has a complete theorem and proof, including its actual fibres and exceptional order-two cases. This suffices to upgrade the formal portion of A.a/B.g. It does not settle whether every signed numerical loop solution for the full profinite modular group induces a surjective endomorphism, nor identify arbitrary such profinite constructions with the entire integral scheme construction. The final audit records distinct exact assertions: B.8.5 is universal numerical realization; B.15 is the effective congruence image/kernel and explicit compatible-lifting instance; B.16 is the named geometric comparison; B.17 repairs a separate quotient-domain defect; B.18 records the restricted-conjugator comparisons; D.7 retains the three arithmetic-image comparisons. The finite computations are not extrapolated to those universal claims.

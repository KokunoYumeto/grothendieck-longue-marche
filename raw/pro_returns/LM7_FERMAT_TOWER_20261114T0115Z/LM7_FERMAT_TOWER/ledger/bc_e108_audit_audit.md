# E108 focused independent audit

**Outcome: PASS.** Reviewer: bc_fermat. This is a full read of the current theorem/proof with a focused arithmetic-support and central-character audit, together with independently written polynomial and character checks. It does not claim a fresh execution of the author's complete certificate.

## Actual comparisons checked

The four-coset Shapiro/augmentation inverse produces precisely the three stated Kummer inputs. The eleven peripheral coordinates follow by eliminating the positive B0 peripheral generator. Replacing the resulting cocycle by a Kummer representative is the unique coboundary determined by the vanishing of the Tate invariants, and E108.13 is the exact BCH conjugation with that coboundary. The independent check derives this identity by multiplication.

The coefficient of the arithmetic class-two action is `-q k cup x + p k cup y`. Expanding the three scalar coboundaries gives E108.12 with the displayed sign of the primitive. The four-coset construction is applied to the abelian central kernel of the pulled-back extension, so division by four changes neither the original section origin nor its abelian input.

The finite localization complex is formed after taking the direct limit over finite support sets. Its coefficient maps are termwise onto; its derived inverse limit is the restricted sequence complex with differential Q-1. The finite unramified H2/H3 vanishings and finite H1 give the asserted actual image, without passing to its closure. Bounded root changes alter the representative by a restricted boundary because each term contains an inertia valuation tending to zero. For rational coefficients a single denominator clears any continuous cochain; thus the quotient uses bounded-denominator sequences tending to zero. The literal tame relation has the factor Q retained before the support normalization divides by Q. These comparisons establish the unrestricted, rather than only finite-support, cup criterion.

The peripheral character basis is the actual Fourier basis of the three cusp orbits modulo their common diagonal. Its exterior multiplicities are (10,15,15,15). The free cohomology rank is 30 because exactly chi_-1 and chi_-2 are odd. The only integral invariant torsion in the displayed characters is C3 for the trivial character at three, yielding C3^10. At five the potentially matching cyclotomic-square character has conductor five and equals none of the conductor-eight characters. The tame fixed-vector equation removes additional unrestricted ramification. The Gaussian norm-kernel coordinates and the explicit CM contraction/section are correctly typed.

## Primary passages actually read

* Guo–Qin–Song, author PDF `research_e108/sources/GuoQinSong_tame_zeta8.pdf`, printed p.8, Theorem 3.5 and complete proof. The preceding reduction to the three unit symbols was read. Their unit is zeta8 times the real unit used in E108, as the displayed formulas require.
* Kahn, author PDF `research_e108/sources/Kahn_descentegaloisienne.pdf`, printed pp.97–98, Appendix 2, Proposition A2.1 and its complete proof. The theorem explicitly covers n invertible in O_S, includes p=2, proves prime-power surjectivity, and repairs injectivity using localization at an auxiliary trivial-class-group ring and the finite inverse-limit argument. The document has 46 physical PDF pages; an initial attempted extraction using the printed numbers as physical pages failed, after which the full text was extracted and the complete passage read. Web opening the two author URLs failed in this audit; these retained actual PDFs were used.

Both source hashes and the independent arithmetic checks are in `check.json`. The new program does not import any author implementation. It verifies the shifted cup identity, all exterior character multiplicities, the literal expression for two in Q(zeta8), and the BCH root transport.

## Corrections communicated

Five literal commas standing for thin spaces in E108.12/17 were reported. The author corrected those display-only artifacts before freeze. The symbolic source and mathematical formulas already used the products audited above. No mathematical correction remains.

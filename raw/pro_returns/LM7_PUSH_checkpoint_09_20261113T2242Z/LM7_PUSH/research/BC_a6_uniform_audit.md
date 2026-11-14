# Independent proof audit of E.57

Full proof audit: **PASS** at source SHA256
`cf54237143936a0825f2a9f97a6096366599a6139dc2bdcc1366acfd4bf017f5`
for `sections/E_a6_uniform_agent.tex`.

This was a complete proof read, with inspection of the saved source and
target certificates and the precise dependencies E.48.12, E.48.19--22,
E.54.17--20, E.53, and E.56. It was not an independent execution replay.
No peer source or certificate was modified.

The following actual maps and comparisons were checked.

1. The fresh rank-nine and rank-six commutator maps give
   ([\rho_J(H),\mathcal R_0]=\mathcal R_0). Together with the perfect
   common kernel and compact nested fibres, this gives precisely the
   claimed nilpotent-residual image.
2. Starting from (gamma_5\widehat N), repeated commutators with
   (widehat H) preserve the entire matrix image. Compactness gives
   (I=\gamma_5\widehat N\cap R_{\rm nil}(H)) onto
   (\operatorname{SL}_2(R)), with zero additive coordinate.
3. The literal relation (x^{120}=y^{120}=1) in the joint finite source
   gives an actual word in (I\cap\ker\rho_J). Its matrix commutator is
   ([E_{21}(240),E_{12}(1)]), with the printed modulo-25 value.
   The normal-subgroup argument supplies every prime at least seven and
   the complete first five-congruence subgroup. The specified signed map
   to (\operatorname{SL}_2(\mathbf F_5)) gives the reverse containment.
4. A common quotient of (\mathcal R_0) and (C_R) is perfect, by their
   actual abelianizations. The centre-exponent comparison then kills the
   additive factor. This proves the exact (U,U_I) and fibre-product
   equalities, rather than only projections onto their two factors.
5. The source words (x^{120},y^{120}) have even exponent coordinates
   ((60,0),(0,60)), whose closed spans are (5R^2). They give the whole
   remaining abelian kernel in the maximal common quotient.
6. E.48.12 applies to the entire old correction kernel. Thus every full
   E.55 word has the same required (P')-coset. The preimage in the exact
   source of E.57.3 preserves (G_L), the whole (G_R), (D_{23}), and
   every retained nilpotent boundary factor at once.
7. The added map (\Gamma\twoheadrightarrow\mathcal Q_m^{\!*}) is onto
   through the actual (F')-matrix image and ordinary exponent map.
   The common-source kernel and corrected-generation arguments retain
   these exact maps and do not assume finite-kernel invariance.
8. On targets the three quotient matrices are exactly the right-action
   convention of E.56. The order-60 relation excludes the specified
   projective maps at primes at least seven. At five the four literal
   Nielsen-kernel words generate the full projective group. The two
   commuting projection kernels then exclude that map through the joint
   signed/(A_6) target. Goursat, the solvable old quotient, and the
   (A_{96}) order comparison give the printed full products.

The correcting-image fibre in E.57.19 and the full profinite-word fibre
in E.57.20 are separately and correctly typed. No change was requested.

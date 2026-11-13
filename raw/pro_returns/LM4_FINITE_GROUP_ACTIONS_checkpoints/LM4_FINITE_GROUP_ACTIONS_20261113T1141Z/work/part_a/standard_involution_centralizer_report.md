# D.49: standard centralizer and exact orbit fibres

The proof computes C_P(δ)=N_P(<δ>)=<δ> in the full pure three-cusp group. It retains the normalized actual automorphism, forces its commutator coordinate to be one using C_F(δ)=1, and then uses D.35's r_sigma argument to place it in GT_0. The second cycle equation is evaluated in named finite Heisenberg quotients, giving μ²=1. D.34 supplies the global sign, so only the identity and δ remain.

The actual orbit map therefore has exactly the two-element fibres β,βδ. On this orbit the corresponding normalized conjugators have the same unique h and opposite multipliers; the exact change of the third-cusp conjugating element is u↦x^(−μ)u. This does not assert surjectivity onto all full involutions.

The usual GT centralizer theorem is already Lochak–Schneps Proposition4(ii). The original PDF at https://webusers.imj-prg.fr/~pierre.lochak/textes/inventiones.pdf was reopened, and Proposition4(ii), printed581, together with Lemma9, printed583, were read. The proof there uses only the first two relations and also applies to GT_0. D.49 includes the explicit passage from the full P-domain and the normalized orbit fibres. The existing R-LS bibliography entry suffices.

The executed program standard_involution_centralizer.py checks the named Heisenberg identity at sixteen moduli and the opposite-multiplier word identity. The global sign conclusion is proved by D.34, not inferred from finite depth.

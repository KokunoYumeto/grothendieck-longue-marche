# The actual coarse annular bundle and its height kernel

DE independent geometric/group review, checkpoint23. PASS. This concerns the actual quotient obtained by filling BOTH added A/B families; it does not discard translates of retained relations.

## 1. Actual locally trivial bundle

Over U_ann retain q and t. After both families are filled, the actual fiber condition is

  t in P1, t not in {1,-1}, q t^2 not equal1.

Thus the finite punctures are1,-1,q^{-1/2},-q^{-1/2}. On U_ann, q is nonzero and q=1 is absent, so the four punctures are distinct. Local square-root choices identify a genuine locally trivial four-punctured-sphere bundle. The previously filled critical fibers cause no degeneration in this retained configuration.

The involution t->-t swaps the two puncture pairs and has the two retained fixed points0,infinity. Its orbifold fiber is the sphere with two order-two cones and two ordinary punctures. Eliminating one ordinary peripheral gives exactly

  W0=C2(C_-) * C2(C_+) * Z(f).

The ordinary orientation kernel is free of rank3. The former A/B labels have been filled, not simply omitted from a relation list.

The actual base U_ann has group F2 on its inner and outer annular circles. Its universal cover is contractible, so the homotopy exact sequence gives the exact fiber extension. The actual based far/collar lifts k_-,k_+ project to those two free generators. Since the base is free, they define a splitting. Hence the full coarse orbifold group is W0 semidirect F(k_-,k_+), with the ACTUAL induced actions.

## 2. Complete retained action, not a shift approximation

Use the convention phi_i(x)=k_i x k_i^{-1}, inverse to positive geometric push. Filling a,B,d,e in the full9/36 presentation makes both selected cones equal their adapted cones and sends the outer branch word to f^{-1}. The six action formulas are

  phi_-(C_-)=f^{-1} C_- f,       phi_-(C_+)=C_+,
  phi_-(f)=f^{-1} C_- f C_- f;

  phi_+(C_-)=C_-,               phi_+(C_+)=f C_+ f^{-1},
  phi_+(f)=f C_+ f C_+ f^{-1}.

They are the inverse full-twist actions of the retained branch/cone pairs, with the opposite cone fixed by the corresponding actual cross relation. Equivalently the positive actions send

  psi_-(C_-)=C_- f C_- f^{-1} C_-, psi_-(f)=C_- f C_-, psi_-(C_+)=C_+;
  psi_+(C_+)=C_+ f^{-1} C_+ f C_+, psi_+(f)=C_+ f C_+, psi_+(C_-)=C_-.

These actions preserve the branch character chi(f)=1, chi(C_-)=chi(C_+)=0. Both actual base lifts have chi=0. The word substitutions are mutually inverse, using only the two cone squares.

## 3. Exact height kernel

Reidemeister--Schreier with representatives f^n gives

  N0=ker(W0 -> Z)
    = *_{n in Z} (C2(f^n C_- f^{-n}) * C2(f^n C_+ f^{-n})).

There is no extra free factor: this follows directly by rewriting the presentation with only the two cone-square relators. Since the actual base lifts have height0 and the actions preserve chi,

  ker(chi on the full coarse group) = N0 semidirect F(k_-,k_+).

The semidirect action is the restriction of the six formulas above. In particular it is NOT merely a permutation or shift of the displayed cone indices: the changed f word contributes based inner corrections for general n. These corrections must be retained in any later comparison with the actual nonlinear kernel.

The two free base lifts are not both selected fixed-source generators: the outer selected source lift has a branch correction. Their height0 property is used only for this split kernel calculation. No coarse source injection or actual unfilled-kernel conclusion is inferred here.

# The fixed stored frame and the next central test

This is a scoped computation, not a theorem that every parity-one lift fails. The original A56 witness JSON is unchanged.

The actual integral model uses free cusp rows first4 and binary s rows last4. Its center is O^6 plus k^30, where O=GR(4,3) and k=F8; the new kernel is2O^6. The original group-law program `check_A59_integral_center.py` checks the actual source relations, standard c, literal cusp fixation, the negative action square, and s-conjugacy. It transports the old central BFRAME through the full linear/coboundary coordinate isomorphism, including its central character determined at the actual source s. Thus the norm is evaluated on the literal old frame, rather than on an affine representative with center zero.

The resulting s-square is binary serialization48596, namely the k-vector

    (4,2,7,6,3,1)

in central coordinate order(01,02,03,12,13,23). Its first-plus-second coordinate is6.

The exact complementary CE calculation studies all doubled free cusp corrections in two families. The joint s/negative-frame invariant source has dimension48 overk and its norm image has rank3. The positive tau-invariant source has dimension16; its unconstrained norm map has rank6, but the simultaneous cusp commutator also has rank6. Requiring that commutator to vanish leaves dimension10 and norm image rank3. The combined constrained norm image has rank5, with annihilator(1,1,0,0,0,0). Hence it cannot cancel the displayed constant within this fixed-witness family.

The full-family exhaustiveness argument is being audited. It must account for every induced integral cohomology action, the literal central character forced by tau, every lift of the old s-frame, and the vanishing of Hom_H(Atilde,Mtilde). No impossibility result is asserted here before that audit.

Even if this fixed-datum audit succeeds, it will not obstruct the main existence problem. Multiplication of a frame by a central element of the six free O coordinates changes its norm by twice that element. This changes the new A56 central frame, while preserving its action and every older C/old-family frame. Proposed A61 uses that existential refinement and treats the conjugacy equations before the norm corrections.

The r-frame and any chosen cross-section transporter must be handled separately. A failure with a frozen r-frame never exhausts the full permitted frame family.

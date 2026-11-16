# C.42 final draft audit

**PASS; approved for canonical integration.** The complete draft `notes/pbc_C42_draft.tex` was read after the root's full homology and original-row audits. Its actual normal quotient chain, module ranks, integral spectral-sequence arguments, elementary order-54 bound and Hopf naturality agree with those audits.

The additional paragraph deriving the old two-primary bound is correct. For an abelian normal kernel of exponent r, its degree-one module and exterior-square homology are killed by r. The total-degree-two filtration therefore enlarges a quotient annihilator by at most r squared. The retained successive derived-factor exponents have product 2^7 times 3^4, giving the earlier bound 2^14 times 3^8; the independently proved three-primary bound sharpens this to 2^14 times 9.

The final literal certificate was checked against the statement: target e_12+e_24, 440 original identity rows, one genuine frame row with coefficient 3 and index 74, and 442 total replayed rows. All integer coefficients and all 351 residual coordinates are supplied in the retained certificate. The centralizer commutator has exponent dividing three because the corresponding cubic lift is central. Thus no forbidden power-word correction is used.

The target belongs to the Hopf torsion subgroup by exact free-abelianization cancellation. Since that three-primary subgroup is annihilated by nine, its map into the quotient of the finitely generated centralization kernel by nine is injective. This justifies the final inference, including its lift along the actual homology isomorphism. The two-primary component and C.31 are expressly left Open. The later failed G86 replay is not used anywhere in this theorem.

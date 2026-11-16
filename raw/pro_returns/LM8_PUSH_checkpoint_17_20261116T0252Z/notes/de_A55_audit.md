# Independent audit of A.55

**Result: PASS.** Reviewed the complete candidate in notes/fgh_A55_draft.tex on 15 November 2026, including the final explicit cohomological dualization in (A.55.6). This audit concerns the normalizer theorem and its stated Heisenberg-five consequence; it adds no fixed-subgroup claim.

## Primary reduction theorem

Independently opened the original first two pages of Michel Raynaud, *p-groupes et réduction semi-stable des courbes*, The Grothendieck Festschrift III (1990), printed pages 179–180, at https://page-one.springer.com/pdf/preview/10.1007/978-0-8176-4576-2_7. The successful independent source reference is turn883view0. Theorem 1 on printed page 179 assumes a finite étale Galois cover with a finite p-group over the generic fibre of a smooth proper curve over a complete discrete valuation ring. It gives potentially good reduction of the covering Jacobian, a tree for the semistable dual graph, and crystalline slopes strictly between zero and one for the components mapping to points of the base special fibre. The statement covers the full cyclic group of order p^n, with no restriction to degree p. These are exactly the hypotheses and conclusions used in A.55.

## Integral and geometric checks

The Schreier presentation has the saturated relations a_j=a_(j+1); its deck-invariant integral lattice pushes to Z_l a plus m times the other three symplectic directions. An integral vector lying in the rational old part is an actual invariant, so the modulo-m detector applies even to a divisible proper homology class.

An exact-order special Picard class makes the special Kummer function non-pth-power. Its p^n-root field is the unique Frobenius inverse function field of the one-variable perfect-residue-field function field. Finite flatness gives an integral special fibre. The hypersurface S2 argument and regularity at horizontal and vertical codimension-one points establish normality, also after finite base extension. There is one nonexceptional component, and its map to the original curve is radicial of degree p^n. On special Jacobians its norm is an isogeny; exceptional component norms vanish. Thus the Prym is, up to isogeny, precisely the product of the exceptional Jacobians, and Raynaud gives special p-rank zero for that Prym. A.46 applies to the actual stable line after dualizing to a crystalline H^1 quotient.

At split primes, the Cartier coefficient calculation gives ordinary reduction. The four integral CM summands form two polarized pairs, with an étale Picard direction in each pair. Choosing the other pair gives both vanishing of the cover character on the original vector and separation from its Poincaré-dual line modulo p^n. Exact-order Picard torsion and its rigidification descend at each finite level to a finite number field. The actual covering subgroup contains the normalized procyclic group, and intersecting its arithmetic group with the original normalizer preserves an open arithmetic image. The same integral generator therefore has a stable lifted proper line. The Prym exclusion and the integral old-part detector then contradict one another.

The final return uses A.54's actual maps, not only a homology decomposition. The removed fibres are the three genus-two cusps: the zero-root and infinity conditions are exactly the stated fifth-torsion fibres under the CM isogeny. The deck translates retain detection of the entire A_2 isotypic summand. The B_8 and original elliptic projections are handled by the already established A.54 inputs.

## Executed independent certificate

Command: python LM8_PUSH/notes/fgh_A55_certificate.py

The execution returned PASS for the integral Schreier/deck lattices at degrees 2, 3, 5, 11, 25, 121; for all 73 split primes below 2000 in the Cartier check; for 30 nonprimitive detection cases; and for the actual genus-two coordinate change. These finite checks support the displayed formulas. The uniform assertions are proved structurally and are not inferred from the finite range.

No mathematical correction remains. The only clarification requested during this audit was the explicit dualization from Tate homology to H^1 in the slope discussion; the current draft contains it.

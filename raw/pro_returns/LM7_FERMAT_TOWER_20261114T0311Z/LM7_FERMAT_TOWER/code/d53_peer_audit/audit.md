# Independent D.53 proof and source audit — PASS

Frozen theorem: D53_EXPERIMENTS/sections/D_arithmetic_correction_space.tex, SHA256 08715d0020ee2eb9ef82a4a3616b76d72c3d79742e8b1928350af2019235912b.

I read the complete proof and all three program sources. No mathematical correction is requested. Root owns the full copied-source execution of the three programs. This audit adds an independent finite-matrix/centralizer verification and does not claim to repeat the 4,220,100-letter word execution.

## Exact local and transgression maps

The central averaging idempotent for the actual odd normal subgroup A gives a projective resolution of the trivial module entirely in its block. Its Hom complex into the moving block is zero, proving every H^i(G,W), including H^0, vanishes. Inflation–restriction therefore gives the stated actual restriction isomorphism to Hom_G(V,W).

Separating the graph boundary image gives the exact sequence with W/(W^s+W^r) and H^1(<s>,W). The r-vertex module is projective, and the augmentation Ext terms vanish. The explicit edge/path derivation has values zero at s and (1-r)v at r, so its cusp value is s(1-r)v. Changing a local conjugator gives precisely (1-t)W. The augmentation identity proves surjectivity of this cusp map.

For a pair whose restriction to K3 is zero, its derivation inflates from G and is the unique inner derivation (1-g)d. Its zero cusp value puts d in W^t; the remaining pair entries differ from d by W^s and W^r. This proves both the full kernel map and its injectivity. The finite parameter space is a conjugator-pair space; its actual derivation image has the smaller dimension stated.

## Arithmetic fixed spaces and positive bound

The actual 576-state graph has rank97, with ranks52,63,29 for s-1, r-1 and (r-1)^2. These give 45 fixed s dimensions and r blocks J3^29 plus J2^5. The complete centralizer lifting equations are correctly oriented: a corrected lift v*c centralizes g exactly when (1-g)v plus the recorded commutator defect vanishes. All16 s-images lift; precisely the three powers of r lift. Thus the two exact G3 centralizer orders follow.

The s fixed-space formula uses the order-two Tate sequence and the difference of fixed vertex counts before/after odd averaging. The quotient centralizer map is onto by correction in the anti-invariant part of the odd kernel. The r formula follows from exact odd invariants and Burnside's r-vertex orbit count, with r and r^-1 distinct already in Q. Every quotient of the actual rank97 r-module has at most34 cyclic-module generators, proving the needed quotient-centralizer bound.

The cusp cyclic subgroup has order36 and is disjoint from every nontrivial elliptic conjugate already after projection to Q. The preimage is free; the five-term homology sequence contributes matching one-dimensional H1 and H2 terms for the even cyclic quotient, giving the precise fixed dimension. Subtracting the averaged graph gives the stated W^t formula. The resulting bound 80*3^95-4*3^45-4*3^34 is strictly positive with the displayed constants.

## Integral reduction and actual D50 automorphisms

The integral augmentation image on the moving Z2 module is all of that module. Its kernel is finite free of rank w, and the surjection splits over Z2, proving reduction of the integral cusp kernel onto the full modulo-two pair space. No assumed integral lift of an arbitrary abstract Hom class is used.

D50's actual fiber product has kernel exactly the integral moving module. Left multiplication of the two retained conjugators by 2b,2c changes the cusp by the displayed exact abelian-kernel expression. The lower source and its action remain unchanged. On the homology component the matrix is T0+2D; its invertible reduction proves an actual Z2 automorphism. The common quotient maps and literal conjugator coordinates agree, so the construction is an automorphism of the full specified D50 fiber product.

The ratio with the original automorphism acts modulo4 by 1+2*D*T0^-1. These matrices add their divided differences, so the generated closed subgroup has exactly the asserted elementary abelian image. Its kernel is precisely the identity action on U/4U. The normalized commutator parameter is retained through the unchanged complete D49 projection.

## Separate finite check and execution scope

The second program computes the 102-dimensional kernel of the pair-to-derivation map, verifies that every polar term on that kernel and against every parameter vanishes, and solves the rank4 same-action obstruction. The third reconstructs the new actual pair, checks its complete unquotiented class-two cusp word, generation, equality of all original homology columns, and compatible integral corrections. The remaining exponent-eight commutator square is explicitly evaluated. None of this assigns a value to the arithmetic invariant obstruction.

The owned bc_d53_exact_graph.py run passed: all18 manifest/runtime-input entries verified; all34 centralizer equations independently solved or proved unsolvable by augmented rank; independent ranks52,63,29; all576 marked matrices and the positive arithmetic dimension bound checked; the two finite certificates have identical retained homology columns and the same prescribed parameter. Full stdout and JSON are retained beside the source.

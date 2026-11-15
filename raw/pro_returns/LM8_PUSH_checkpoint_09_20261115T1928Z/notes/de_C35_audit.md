# Independent audit of C.35

**Verdict: PASS.** I read the entire candidate `notes/pbc_C35_draft.tex` and the exact algorithm `code/pbc_weight12_pentagon.py`, following the independent C.33 integral group/lattice audit.

## Exact coefficient certificate

The backward contraction formula is the ordinary Leibniz formula for a linear derivation whose generator images have degree two. Contracting an adjacent output pair chooses the letter that produced it. Recursing records the outer derivation as the first operator letter, so the operator order agrees with substitution into the associative expansion of the Lie word. The five signed derivation pairs agree with P.2's infinitesimal braid defect. The nineteen comparisons to the independent full degree-seven expansion are consistency checks; the contraction identity itself proves the algorithm at degree twelve.

I reran the complete script without overwriting the author's JSON. Independent stdout is `code/de_C35_pentagon_audit.out`. It reproduces the five exact integer coefficient rows, their rank five, and the exact identity

`698922 ell = -192329 R1 + 472 R2 - 26842 R3 - 107926 R4 - 11870 R5`.

The denominator is 3 modulo 13, hence a unit. The modular search only selects rows; the final identity is verified over the integers on all seven integral basis vectors.

## Actual pentagon subgroup comparison

The subgroup P∩U is closed in the actual finitely generated nilpotent pro-13 group U. Intersecting its finite central filtration gives finite-rank closed Z13 submodules, so it is finitely generated. The subgroup clause of the independently opened Lazard theorem therefore identifies its logarithm with an actual Z13 Lie sublattice.

The tame element t belongs to the arithmetic image and hence to the actual pentagon image. It normalizes P∩U. Its integral averaging projector e12 preserves this logarithmic lattice: addition, Z13 scalar multiplication, and the tame action all preserve it. The distinct-weight splitting established in C.33 puts e12 log(h) in the actual top filtration step. Exponentiation returns an actual element of P∩U, not merely a vector in a rational or graded closure.

A full pentagon preimage of that local element has local multiplier one and conjugator in gamma12. Indeed the kernel of the retained quotient is gamma13, contained in gamma12. Its first degree-twelve term therefore satisfies the linearized pentagon, without lower-degree cross terms. Applying the exact row relation proves that the same C.33 functional vanishes. No faithfulness of the infinitesimal braid representation is needed here: vanishing of the actual pentagon implies vanishing of every displayed image coefficient.

## Full multiplier passage

The restriction of the extended character to the actual pentagon image is zero on its multiplier-one kernel. For each remaining local multiplier, the cyclotomic character of G_Q supplies an arithmetic image element with that multiplier. Comparing the two elements reduces to the kernel. C.33's exact cyclotomic correction therefore kills the entire pentagon image, while preserving its nonzero global multiplier-one witness.

Combining the order-thirteen character with the independent quadratic characters uses finite coprime products and compactness, as in C.34. The conclusion is a quotient by the closed normal closure of the pentagon group; it makes no claim of an arithmetic-trivial character on the pentagon group itself.

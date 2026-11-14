# Independent audits of D.63 and D.64

Result: both complete written proofs and metadata PASS, without correction.

## D.63

The extension map is constructed from the actual full inverse image of the given outer involution in Aut(F); its faithfulness uses the nonidentity outer label and the center-free kernel. This does not presume a standard conjugator. The cusp conjugation and the half-exponent adjustment retain the exact multiplier and produce the unique representative with c→c^mu and v→c^i v. The uniqueness proof uses the full cusp centralizer and injectivity of multiplication by two in Zhat.

The exact all-unit transporter cosets from D.62 force the fixed-line homology sign to be (-1)^i. It is a single global sign because it is the actual action on the primitive full Zhat line, rather than a selection of primewise signs. The determinant equals the peripheral multiplier in every Heisenberg quotient. Commutation with the negative involution then gives the two rational eigenspace eigenvalues; the stated integral half-coefficients descend the matrix identity to every Z_p lattice, including the nonsplit dyadic lattice.

The IA identification with actual cusp-fixing, involution-commuting automorphisms has inverse maps and no residual inner ambiguity. It is closed and compact. D.55 excludes its torsion. On a finite subgroup, the dyadic multiplier is ±1, and primary faithfulness embeds the whole subgroup into precisely the four stated matrices. The proof does not infer triviality of an arbitrary IA kernel or a larger character image.

## D.64

The standard full free-product presentations and the factor-centralizer calculations are correct. Their cusp fixed subgroups are trivial. A normalized IA map fixes the actual fusion transporter and therefore fixes the unique other commuting reflection, or the unique outside square root, respectively. It fixes the full listed extension generators, proving the two IA kernels trivial.

For the two-class model, an arbitrary normalized centralizer map sends the other reflection into its actual other F-conjugacy class. The centralizer intersection with F is the full procyclic X factor. The primitive homology sign forces the image of X to be F-conjugate to X or X inverse with exactly that sign. The displayed dihedral quotient sends the named cusp to r squared and either transporter expression to r^mu. Its conjugacy condition at every integer modulus forces a single global sign by the finite-intersection argument. The finite computation is not used to replace the all-modulus proof. The two explicit commuting involutions realize the complete Klein four centralizer, and the orbit-fibre statement follows from that exact group.

For the one-class model, inversion of both free generators has the displayed peripheral conjugator and the sign/multiplier values. Injectivity of the characters gives exactly its multiplier-one C2 and the four ±1-multiplier elements. Because the centralizer is abelian, adjoining any torsion element to these four gives a finite subgroup; D.63 then places that torsion element in the same Klein four. The possibility of other infinite-order multipliers is kept unresolved.

## Executed check

I reran `work/part_c/code/standard_negative_centralizers_d64.py`; it passed. Its captured output is `work/part_a/d64_audit_stdout.txt`. It verifies 18 exact free-word identities and 9,310 dihedral transporter checks over all moduli 2 through 96. The source proof supplies the full-profinite and all-modulus conclusions.

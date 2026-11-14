# Independent audit of D.62

Result: PASS for the complete written core in `work/part_c/d62.tex` and its metadata, read on 2026-11-13. No correction is required.

The primitive-character centralizer proof is valid in the full free profinite group. A nonzero kernel element in C_F(g^n) has a nontrivial infinite procyclic p-component; it commutes with the p-component of g^n, whose primitive-character image is the nonzero subgroup n Z_p. The two closed factors have trivial intersection, so their multiplication embeds Z_p squared as a closed subgroup. Cohomological dimension rules this out. The subsequent subtraction h g^(-rho(h)) proves the exact centralizer, and applying rho to a normalizing conjugation proves the normalizer equality.

For every transporter g' in g C_F(v), the equations [g',v]=c and alpha(g')=c^(-1)g' are exact. D.59 preserves its primitive abelianization. Every outside centralizer element has the form hv, giving the stated conjugacy equivalence. Its square coefficient kappa and the Zhat times {0,1} coordinate law give the entire centralizer, not only a quotient. Even kappa at two yields the unique outside involution. Odd kappa at two is corrected independently at every odd prime to a full unit; the displayed unit power gives the unique outside square root. No assumption that the initial kappa is a full unit is made.

D.60's primitive torsion quotient forces the even coefficient in the two-section case. In the one-section case any outside involution is conjugate to v, whose fixed subgroup lies in the closed derived subgroup; it cannot centralize a homologically primitive transporter. These arguments select the claimed full centralizer structure.

The displayed standard-model maps have commutator exactly c and intertwine the actual involutions. D.61's full boundary test supplies surjectivity and the inverse maps. Conversely the image of X, or of XY in the one-class model, lies in precisely the transporter coset and supplies the required outside centralizer element. The claimed result is an exact equivalence on the specified normalized slice; it does not assert nonemptiness.

No additional numerical test was needed for this algebraic argument. The relevant exact standard-model identities were already independently rerun in the D.61 audit (12,787 checks).

## Proposed all-unit extension communicated by C

The proposed two transporters also check directly: c^((mu-1)/2) g conjugates v to c^mu v, and c^((mu+1)/2) g^(-1) conjugates cv to c^mu(cv). The half-exponents exist for every full unit mu. Their abelianizations are respectively [g] and -[g], and C_F(cv)=g C_F(v) g^(-1) retains zero ambient abelianization. The same primitive centralizer proof and the D.60 character therefore retain the full unit and each actual reflection label. This checks the communicated formulas; the future written continuation should still be read as a complete fragment.

## Written all-unit continuation: PASS

I subsequently read the complete `work/part_c/d62_unit_addendum.tex`, equations D.62q–w. Its transporter maps, exact coset equality, primitive homology signs, and both standard-model maps all agree with the checks above. The equation alpha_i(a)=c^(-mu)a follows from the actual commutator convention. The D.60 character has value (-1)^i and therefore still forces the full coefficient kappa to be twice an element in the two-class case. The converse maps use precisely the X or XY images of D.61, so the final equivalence covers every unit and both reflection labels. Full invertibility follows from the retained unit boundary, as stated. No existence assertion is introduced. The complete written continuation passes without correction.

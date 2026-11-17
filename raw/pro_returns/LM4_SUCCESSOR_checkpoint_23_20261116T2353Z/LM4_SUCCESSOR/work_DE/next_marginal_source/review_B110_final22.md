# Complete formal-source review of B110

DE read the entire `sections/b_slit_bad_centralizer.tex`, statement and
all seven proof sections. **PASS.** The result remains restricted to
the actual slit bad vertex and the specified reflected one-neck model.

The geometry review includes the actual disk/plane homeomorphism,
complete nine-value/ten-relation locus, the separated simultaneous
nodes and retained branch, the uniform cyclotomic deformation, and
the common first-neck lift. The separate independent initial-order
certificate supplies the (1/100\) projection-gap margin used in the
formal source.

The algebra review includes both directions of the same-sheet Nielsen
change, the branch/stable-letter change, the reversible use of the
seven base relations, and the precise HNN direction
\(wpw^{-1}=e,wrw^{-1}=\bar b\). The auxiliary stable letter is
explicitly its inverse under the other convention. The graph has
exactly the declared diagonal pairs and no extra (p/\bar p\) or

\(r/\bar r\) edge; the fixed-subgroup piling argument consequently
has the claimed four generators. The compatible finite-head proof
gives exact clique kernels and the full completion comparison rather
than an assumed profinite injection.

The source comparison agrees literally with the independently executed
`check_inner_fixed_source22.py`: unique even conjugators are obtained
before filling from the based Borel strip, the four source words reduce
using only cone relations, and the free-four detector kills all twenty
ordinary relators. Hence the retraction and actual compact source
topology are proved.

The final corollary correctly chooses reflected paired slits, not an
unproved identification between arbitrary marked slit presentations.
The two-region/one-overlap base (U_*\) is simply connected; the
selected quotient source is its four-puncture deletion. The source
double cover \(\sqrt{1-q}\) has two components on this domain.
The selected component is transferred by intersection with the actual
open index-two subgroup. The statement explicitly avoids B106's
inapplicable connected-source two-coset argument on this restriction.

One evidence-path precision was sent to root: the plan JSON records
the exact centers, base and halfside from which the corners are
specified, while the explicit fifty segment records occur in
`inner_bad_orbifold_braids22.json`. Cite both files in that sentence.
There is no mathematical correction.

The genuinely additional annular (q=0\) relations are separately
verified by `verify_inner_q0_HNN_independent22.py`; they do not affect
the stated slit or one-neck scope.

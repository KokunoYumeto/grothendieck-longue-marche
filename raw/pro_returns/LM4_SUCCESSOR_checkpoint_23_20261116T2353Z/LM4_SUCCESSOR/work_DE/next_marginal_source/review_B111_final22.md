# Complete B111 source and strict independent conjugacy review

DE read the entire `work_CE/B111_q0_diagonal_proposed.tex`, its
producer and genuine output. **PASS; no correction requested.**

The actual positive (q=0\) lasso, its clockwise inverse action,
and the common raw contact (r_{33}\) retain the same six-strand
marking as B110. The identities

\[
\psi_0^{-1}(x_5)=x_5,\qquad
\psi_0^{-1}(U)=VUV^{-1}
\]

are literal in the generic (C_2*F_5\). The displayed same-sheet
substitutions give (V=g e w S g^{-1}\), and only
\([a,\bar a]=1\) is used to remove (S\) from its conjugation of
the cone. The complete resulting conjugator is
\(a b^{-1}w p\); it is not omitted or replaced by a peripheral
conjugacy class.

The independent checker
`verify_inner_q0_diagonal_independent22.py` imports no CE oracle.
After replacing (e\) by (wpw^{-1}\), it verifies the entire
conjugacy in a graph group allowing **only** the single edge

\([a,\bar a]=1\), using a commuting-suffix cancellation algorithm.
Thus no unmentioned graph relation is used to make the witness
vanish. Its genuine `.out` and `.err` and
`inner_q0_diagonal_independent22.json` are retained.

The coordinate retraction onto the two nonadjacent vertices

\(p,\bar p\) proves the commutator nontrivial in the graph base.
B110's actual base injection proves discrete nontriviality in the
slit group, and its full-topology embedding together with graph-group
residual finiteness proves nontriviality in the full completion.
The actual annular conjugation relation kills precisely the displayed
inverse image of (r_{33}\), so it kills the conjugate commutator
and hence the commutator itself. The same killing persists upon
completion. There is no assumption that the old operator descends
to an automorphism of the slit quotient.

The final scope is exact: the inclusion-induced slit-to-annulus map
has a nontrivial discrete and completed kernel. This is not a
counterexample to the annular fixed-source equality and is not a
complete annular presentation simplification.

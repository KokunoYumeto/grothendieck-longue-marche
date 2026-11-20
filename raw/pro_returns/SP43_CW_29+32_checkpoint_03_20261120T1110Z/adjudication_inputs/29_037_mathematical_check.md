# Targeted mathematical check while reading 29/037

Main reader; GPT-6 Astra Pro, inherited effort not exposed; 2026-11-20.

The page claims that étale coverings of `(Z_i,G_i)` are equivalent to finite sets with `G_i` action when `Z_i` is strictly local. This is checked conditionally on the page's strictly-local hypothesis and on the standard splitting property below; it is not a verification that the preceding construction actually produces such `Z_i`.

Background used without an independent proof in this run: a finite étale cover of a strictly local scheme is a finite disjoint union of copies of the base. This is recorded as background, not as a new proof.

Conditional check: label the components of a finite étale cover by a finite set E. Every lifted G_i action permutes these components. On a component its map is determined by the prescribed action on the base, since that component maps isomorphically to Z_i. Thus the equivariant cover corresponds to a G_i action on E. Conversely E with a G_i action gives the constant cover E_{Z_i} with the diagonal action. Since Z_i is connected, maps of constant covers over Z_i correspond to maps of their finite component sets, and equivariance is exactly equivariance of these maps. These constructions give mutually inverse equivalences up to the ordinary choices of component labels.

Outcome: the finite-set description is coherent under the stated hypothesis. This check does not decide the overstruck action-of capital earlier in the page, does not replace the printed G over the final x by G_i, and does not fill any missing arrows. Those remain palaeographical decisions from the scan.

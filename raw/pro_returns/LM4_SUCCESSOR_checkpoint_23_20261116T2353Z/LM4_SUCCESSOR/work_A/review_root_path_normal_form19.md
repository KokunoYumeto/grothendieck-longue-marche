# Independent review of the full root-path normal form

Status: PASS, research only, 2026-11-16. Read the complete note
`work_CE/research_factored_full_chain_normal_form_19h.txt` and the genuine
output of `work_CE/code/root_path_chain_operations.py`.

The boundary map of a tree identifies its integral edge-chain group with
the augmentation ideal on its vertices. Hence all root paths L(a),a!=1,
are an actual free abelian basis, not merely a family of spanning paths.
Tensoring with the positive B-edge basis gives the claimed unique normal
form for the full product-tree2-chain module. The displayed boundary
formula and the B-step integration convention telescope to the original
edge loop, so the resulting collected dictionary is the complete chain.

The sparse G action uses an essential actual hypothesis. For retained
t in T, tau_t sends x_(g,i) to x_(tg,i), and tau_beta(t) sends the B
generator x_(g,j) to the single positive generator x_(beta(t)g,j).
Therefore the transformed B edge is still one edge. The transformed
A path is the path from u to u*tau_t(a), namely
L(u*tau_t(a))-L(u). Each G monomial thus produces at most two normal-form
terms from each input term. This statement is correct for the actual
G=(R_A times R_B) semidirect T. It is not asserted for old-base or source
operators, which can take edges to longer paths.

Consequently a plus/minus G monomial times the42-term original chain has
at most84 nonzero collected terms. The33162-term actual geometric-word
image cannot equal such a monomial multiple. The support test is exact
in a genuine integral basis; it is stronger than the prior augmented-row
or cyclic-word comparison. It says nothing about general finite sums of
G monomials, the full retained-deck span, whole-block intersections or
the kappa map. No mathematical correction requested.

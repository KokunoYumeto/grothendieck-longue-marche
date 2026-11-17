# Independent q0 witness and one-neck source comparison

**Checkpoint 22 — PASS, with the slit/annular boundary retained.**

## 1. Exact annular kernel witness

I read the complete `work_CE/code/check_inner_q0_HNN22.py`, its genuine twenty-image stdout, the relevant JSON entries, and the separate `work_CE/code/certify_inner_q0_diagonal22.py`. The complete Britton evaluator uses exact graph-group normal forms and coordinate-clique membership, rather than a bounded membership search. Its conclusion that the retained operator does not preserve the slit relator kernel is sound.

I additionally implemented a separate verification using only the actual input JSONs and free reduction in `C2*F5`. No CE graph-group or HNN evaluator is imported. The actual negative-q0 image of the beta33 relator is the displayed 46-letter word with four copies of

`R=a c a c a^-1 c a^-1`.

The literal identity `R c=[a,cac]` makes each copy equal to `c` using only one established cone relation. Substituting the single HNN identity `e=w p w^-1` then gives, by literal free reduction,

`psi0^-1(r33) = (a b^-1 w p) [p,cpc] (a b^-1 w p)^-1`.

The two vertices `p` and `bar p=cpc` are nonadjacent in the actual twelve-vertex graph. Killing every other vertex gives a retraction of its graph group onto `F(p,bar p)`, where the commutator is the freely reduced nonempty word `p bar p p^-1 bar p^-1`. The actual HNN base embeds. This proves nontriviality in the slit group without a profinite or representation argument.

The actual annular presentation imposes every retained-zero translate of each filled critical relation. Thus it kills the displayed conjugate and hence kills `[p,bar p]` itself. The slit-to-annulus homomorphism is consequently noninjective. This does not compute the full annular kernel or its centralizer.

Independent producer and genuine evidence:

- `work_A/code/review_q0_beta33_witness22.py`
- `work_A/code/review_q0_beta33_witness22.out`
- `work_A/code/review_q0_beta33_witness22.err`
- `work_A/review_q0_beta33_witness22.json`

An earlier separate short check is retained at `work_A/code/review_q0_beta24_witness22.py` and its stdout/JSON. Its negative beta24 image has four stable letters, with all three possible pinches excluded by individual exponent coordinates. It confirms the same slit/annular distinction but is not needed for the preferred printed beta33 proof.

The CE raw-cone derivation also checks: the raw involution `U` and positive generator `x5` satisfy `r33=[x5,U x5 U]`; the inverse-zero operator fixes `x5` and sends `U` to `V U V^-1`. The two marked changes make `U=g c g^-1`, `x5=g e g^-1`, with `g=a b^-1`. The factor `S=acac` centralizes `c` using `[a,cac]=1`, giving exactly the same conjugator and order above. No peripheral connector is discarded.

## 2. Selected source across the actual first neck

I read the entire `work_DE/next_marginal_source/one_neck_fixed_source_corollary22.md`. Its geometric and completion comparison passes.

For a unit parameter, direct conjugation of the rational formula gives `h_u(1/bar q)=1/bar(h_u(q))`. Hence `J(q,t)=(1/bar q,1/bar t)` preserves the excluded graphs and the equation `q t^2=1`, commutes with the involution, and exchanges the inner and outer bad fixed sections. Choosing the outer slit to be the mirror of the audited inner slit makes this an actual marked comparison; source basis inversion under orientation reversal does not alter its image or topology.

The two simply connected slit domains have a single contractible neck overlap. Their union is simply connected and omits every old base puncture. The selected fixed source is this union minus precisely the four outer contact values. It is therefore the same free rank-four source obtained from the outer bad vertex, with the common connector retained. The first-neck theorem reduces the selected cone centralizer to that vertex, both discretely and in full completion. The actual regional source retraction and the full vertex embedding give an injective completed source map; this is not a completion of an unspecified image.

Finally, the restriction of the actual free-swap double cover to this source is defined by `sqrt(1-q)`. Because the whole slit union is simply connected and excludes `q=1`, this square root exists on the union before the four contact points are removed. The source cover has two components, each isomorphic to the selected quotient source. The surface cover itself is connected, as witnessed by an ordinary fiber loop around a removed discriminant point. Thus its based group is the actual index-two subgroup, containing the selected source. Intersecting the proved fixed-subgroup equality with that subgroup, and then with its open full completion, gives the asserted ordinary and profinite equality for the selected component upstairs.

This last argument correctly avoids the global two-coset argument, whose source-surjectivity hypothesis fails on this disconnected source cover. It uses only the single first neck and excludes the retained zero loop and every other neck.

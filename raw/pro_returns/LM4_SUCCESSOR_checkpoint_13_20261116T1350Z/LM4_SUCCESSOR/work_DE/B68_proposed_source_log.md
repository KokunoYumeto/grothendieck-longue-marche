# B68 primary-source and finite-certificate log

Proposed statement, awaiting root integration. Verification date: 2026-11-16.

## Heusener and Weidmann (2019)

Published primary full text:
https://www.degruyterbrill.com/document/doi/10.1515/jgth-2018-0118/html

Author preprint:
https://www.math.uni-kiel.de/algebra/de/weidmann/research/material-research/whiteheadfoldings-pdf

The publisher confirms Journal of Group Theory 22(1), 15–21, DOI
10.1515/jgth-2018-0118, print year 2019 (online 2018).
Section 1 defines a separable set by conjugacy into factors of a nontrivial
free product. Published Corollary 3.5 states that such a set has disconnected
Whitehead graph or a cut vertex. This is exactly the required proper-free-factor
criterion, stronger than Corollary 3.4 for primitive elements. The preprint
uses different numbering (Corollary 3.3).

Fresh primary retrievals: turn571view0; turn573view2; turn573view4. The
source graph uses the pairs (x,-y) for cyclic adjacent x,y; our (-x,y)
graph is obtained by reversing every vertex sign.

## Kra (1981)

Original primary article scan:
https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6295-11511_2006_Article_BF02392465.pdf

DOI: https://doi.org/10.1007/BF02392465

The first-page footer and article pagination confirm Acta Mathematica 146
(1981), 231–270. Theorem 2′ (pp. 231–232) identifies irreducible point pushes
with essential loops; the next paragraph identifies irreducible maps with
pseudo-Anosov maps. Section 9 (p. 252) explicitly identifies essential loops
with filling loops. Theorem 2(b), pp. 252–253, is the detailed statement.
The underlying six-punctured sphere is nonexceptional for this application.

Fresh primary retrievals: turn571view1; turn573view1; turn573view3.

## Exact computation

`next_joint_rigid_symplectic/verify_full_Q_word_filling.py` reads the restored
common-base eleven-strand source words, performs its own strand deletion and
Artin/free-word operations, and recomputes the 144-letter fiber word.
It separately verifies both compositions with the inverse for each of six
Whitehead automorphisms. It verifies the final 15-edge graph is connected and
stays connected after any vertex deletion, saving all eleven spanning trees.
The genuine run output is `verify_full_Q_word_filling.out`; exact words and
witnesses are in `full_Q_word_filling_verification.json`.

The earlier exhaustive Whitehead minimization was discovery only. The proof
uses the six explicit verified automorphisms and does not require that the
final word be minimal. The extraction convention is an antihomomorphism;
inverting it gives the actual free-fiber homomorphism. Inversion preserves
the free-factor and filling conclusions used here.

No full theta5 injection, completed-kernel identification, or profinite
pseudo-Anosov centralizer conclusion is asserted.

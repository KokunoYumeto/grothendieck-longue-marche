# Selected fixed source across the one actual first neck

DE independent comparison, checkpoint22. This uses B108, the fully
reviewed actual slit-region presentation and its auxiliary centralizer
theorem, and the literal source identification in
`inner_fixed_source_identification22.md`. It makes no assertion about
an annular old-base loop or another neck.

## 1. Specify the paired slit geometry

The actual quotient surface has a real-analytic involution

\[
J(q,t)=\left(\frac1{\overline q},\frac1{\overline t}\right).
\]

It commutes with (F(q,t)=(q,-t)\). For each actual unit parameter

\(u\), direct substitution gives

\[
T_u(1/\overline q)=1/\overline{T_u(q)}.
\]

Thus (J\) preserves all projective excluded graph equations, the
retained (t=\pm1\), and the branch equation (qt^2=1\). It exchanges
inner and outer base regions and exchanges the two fixed sections.
It preserves the angular coordinate at the unit-circle neck, in
particular the literal lower-half-plane choice in B108.

For the corollary choose the outer slit (V_+\) to be the image of
the audited inner slit (V_-\) under (q\mapsto1/\overline q\).
Choose a sufficiently small invariant first-neck neighborhood. These
are permitted choices in B108. Then the actual outer bad vertex and
its cone at (t=0\) are identified by (J\) with the actual inner bad
vertex and its cone at (t=\infty\). The contact points satisfy

\[
J_q(\alpha_u)=\beta_u.
\]

The map reverses the orientation of the base plane, so a positive
outer source lasso is an inverse inner source lasso, with its actual
transported common whisker. This affects the choice of a free basis
by inversion and changes neither the source subgroup nor its topology.
No claim that unrelated slit choices have identical marked
presentations is needed.

## 2. Actual base and source topology

The two enlarged slit regions are simply connected, with one
contractible overlap in the neck. Their union (U_*\) is an open
simply connected planar domain by van Kampen. It excludes every old
base puncture, including (q=1\), and includes all nine inner and all
nine outer critical values. In particular,

\[
D_*:=D_0\cap\mathscr Q_{U_*}
\cong U_*\setminus\{\alpha_u:u\in\mu_5\setminus\{1\}\}.
\]

The four removed points are distinct and lie in the outer slit.
Therefore \(\pi_1(D_*)\cong F_4\), with the four positive outer
contact lassos as a geometric free basis. Enlarging the outer source
domain across the first neck and the inner simply connected region
adds no source generator: its inclusion into (D_*\) induces the
same (F_4\), with the common basepoint connector retained.

## 3. One-neck equality on the actual quotient surface

Write

\[
G_* = \pi_1(\mathscr Q_{U_*},\bar P)\rtimes\langle\tau\rangle.
\]

The selected cone (\tau\) at (t=0\) belongs to the outer bad
vertex (R_+\). B108 gives, discretely and in the full completions,

\[
C_{G_*}(\tau)=C_{R_+}(\tau),\qquad
C_{\widehat G_*}(\tau)=C_{\widehat R_+}(\tau).
\]

Transport by (J\) and the actual inner slit centralizer theorem
identify the right sides as the source (F_4\) times the cone (C_2\),
and the actual closed source \(\widehat F_4\) times (C_2\),
respectively. The previous section identifies that vertex source
with the entire selected source (D_*\), not merely with four
unbased peripheral conjugacy classes.

Intersect with the ordinary index-two subgroup

\(\Pi_*:=\pi_1(\mathscr Q_{U_*},\bar P)\). Since this finite-index
subgroup has its full topology and its completion is the corresponding
open kernel, this proves

\[
\Pi_*^F=I_*,\qquad
(\widehat{\Pi_*})^F=\overline{I_*},
\qquad I_*\cong F_4,
\quad\overline{I_*}\cong\widehat F_4,
\]

where (I_*\) is the actual image of \(\pi_1(D_*)\).

For the full-topology assertion, the source is an actual retract of
the ordinary regional vertex by the free-four detector. B108 embeds
the full vertex completion into the full one-neck completion. Thus
the completed source map is injective throughout, and its compact
image is precisely its closure. There is no completion of an
unexamined infinite-index image in this argument.

## 4. Transfer to the selected component of the original double cover

The actual free swap covering is

\[
Z_{U_*}\longrightarrow\mathscr Q_{U_*}.
\]

Its restriction to (D_*\) is obtained by adjoining

\(\sqrt{1-q}\). Since (U_*\) is simply connected and (1-q\)
never vanishes there, this square root exists on all of (U_*\),
including at the four subsequently omitted alpha points. The
restricted source cover therefore has **two components**, each
mapping isomorphically to (D_*\). Let (S_*^+\) be the component
containing the specified lift (P\).

The surface cover itself is connected: a regular quotient fiber has
a loop around either removed discriminant puncture with nontrivial
swap monodromy. Its based group is thus the index-two subgroup

\(\Pi_Z\le\Pi_*\) given by that cover. Every selected source loop
has trivial swap monodromy, by the preceding square-root argument,
so (I_*\le\Pi_Z\). The literal lift (F\) fixes (P\) and

\(S_*^+\), and its action is compatible with the based inclusion.
Consequently

\[
\Pi_Z^F=\Pi_Z\cap\Pi_*^F=I_*,
\]

where (I_*\) identifies with the actual image of

\(\pi_1(S_*^+)\). The same equality holds in the full completions:
\(\widehat{\Pi_Z}\) is an open subgroup of

\(\widehat{\Pi_*}\), and the actual compact source image is already
contained in it. Thus

\[
(\widehat{\Pi_Z})^F=\overline{\pi_1(S_*^+)},
\qquad
\pi_1(S_*^+)\cong F_4,
\quad
\overline{\pi_1(S_*^+)}\cong\widehat F_4.
\]

This is an intersection argument. The global B106 two-coset argument
does not apply here: the source cover over (U_*\) is disconnected,
and its source image does not surject onto the swap character.
The old base loops and all other unit-circle necks remain excluded.

# Actual node-orbit identities, invariant syzygies, and finite kappa representatives

Date: 2026-11-16. Research following B92. The protocol and bounded
old-zero identities below are exact, with the presentation distinction
specified in Section2. No nonzero kappa class or source equality is
asserted.

## 1. Keep all geometric node indices

Use B91–B92 notation

\[
 0\longrightarrow Z_2\longrightarrow P_{\rm node}
       \xrightarrow d\bar L\longrightarrow0,
 \qquad P=I_{\mathbb Z[R]}\otimes I_{\mathbb Z[R]}.
\]

Here (P_{\rm node}\) is free over (\mathbb Z[E]\),

\[
 E=R\times R,
\]

on actual nodes in the universal filled-surface cover. The involution
swaps the E coordinates and acts by negative swap on the oriented node
cells. Old-base and retained-deck translates are different node indices
unless the actual covering geometry identifies them. An E coefficient
does not replace a nontrivial retained-deck translate.

Let \(r_\nu\) be one actual based commutator and let an actual old
operator \(\alpha\) satisfy a literal free-word identity

\[
 \alpha(r_\nu)=g r_\mu g^{-1}.
\]

Split (g=nt\) using the fixed retained (F_5\) section, with

\[
 t=\operatorname{fill}_{F_5}(g),\qquad n=gt^{-1}\in K_s.
\]

Write \(\bar n\in E\) for the actual image. Then the exact
product-tree two-chain identity is

\[
 \alpha(d e_\nu)=\bar n\,d e_{t\nu}
\]

when \(\mu=\nu\), and with \(t\mu\) in general. Thus

\[
 z=e_{\alpha\nu}-\bar n e_{t\mu}\in Z_2.
\]

The notation \(\alpha\nu\) uses the transported cell corresponding
to that actual automorphism. For the stored geometric push of a base
loop (b\), this is the action of (b^{-1}\) under the convention
\(\alpha_b(x)=b^{-1}xb\). This inverse is retained when translating
to left Q-deck labels.

A literal word conjugacy is a sufficient certificate. More generally,
one may verify the entire two-chain equality directly, by comparing
every full E vertex and every pair of free generators. Equality only
after augmentation is insufficient.

## 2. The bounded old-zero test gives nonzero common-whisker syzygies

The finite computation uses the explicit **common-whisker** node
presentation. Denote its complete node-module map by
\(d_{\rm common}:P_{\rm common}\to P\), retaining all actual
old-base/deck translates, and write

\[
 Z_{2,\rm common}=\ker d_{\rm common}.
\]

This is not being identified with B92's equivariant-whisker kernel
\(Z_2\) merely because both maps have image \(\bar L\). An actual
invertible change of node generators and whiskers, or an explicit finite
common refinement carrying these relations, is required for that
identification. It has not been supplied by the present finite test.

Producer and genuine output:

`work_A/code/check_old_zero_node_orbit_identities.py/.out/.err`

Complete data:

`work_A/old_zero_node_orbit_identities.json`

The input is the corrected paired package. The producer tests only the
sixty-four seed relators under the actual old-zero geometric push; it
does not truncate the complete relation module and infer completeness.
It confirms literal F-commutation of that old operator.

There are two literal fixed words:

\[
 \alpha_0(r_{6,3})=r_{6,3},\qquad
 \alpha_0(r_{6,7})=r_{6,7}.
\]

Their reduced word lengths are eight and twelve. Therefore

\[
 e_{\alpha_0\nu}-e_\nu\in Z_{2,\rm common}
\]

is nonzero for each of these two indices. The cells are different:
the old-zero loop is a nontrivial deck translation on the universal
base, while the two-chain columns agree exactly. This supplies actual
full-coefficient common-whisker syzygies, rather than only repeated
augmented pairs.

Two further exact free conjugacies occur at \((6,2)\) and
\((6,4)\). Their retained deck words are, respectively,

\[
 x_4^{-1}x_{19}^{-1}x_{14}^{-1},\qquad
 x_9^{-1}x_4^{-1}x_{14}^{-1}
\]

in the retained paired slots. The full conjugators and their kernel
parts are recorded. These deck words must remain in the node indices;
they are not E coefficients.

The independent CE chain certificate is
`work_CE/code/check_old_zero_node_chain_identities.py/.out/.err`, with
`work_CE/next_symmetric_nodes/old_zero_node_chain_identities.json`.
It checks all four literal words, both complete two-chains, the E
left-translates, and each complete edge boundary. The fixed columns
each have three squares. The other two columns each have nine squares;
their E-coordinate word lengths are (8,6\) and (6,8\), respectively.
The same retained deck words in consecutively renumbered (F_5\)
coordinates are \((-2,-5,-4)\) and \((-3,-2,-4)\). This is the
same head data, not a change of the node index.

The physical nodes ((6,3)\) and ((6,7)\) are F-related, but the
stored common-whisker representatives have not thereby been identified
with the literal B92 equivariant cell basis. Their transformed chains
are explicitly available. Identifying the corresponding cell relations
with B92's F-action requires the based generator change or refinement
just specified.

## 3. Why a repeated column is not yet a kappa class

A syzygy (z\in Z_2\) contributes to (H^2(C_2,Z_2)\) only if
\(Fz=z\), and its class is taken modulo \((1+F)Z_2\).
In particular:

- replacing an arbitrary syzygy by (z+Fz\) only gives a **norm**;
  its (H^2\) class and its kappa value are zero;
- an equality between two F-fixed oriented node columns, with
  F-fixed coefficient, gives an **anti-invariant** relation because
  F reverses each node-cell orientation; it is not an (H^2\)
  representative;
- an actual invariant cycle must be checked on all formal node
  indices and all E coefficients, including every based transport.

Thus the two literal old-zero fixed words do not by themselves prove
a nonzero kappa value. They rule out injectivity of the explicit full
common-whisker node map. The invariant construction in the next section
applies in B92's equivariant presentation; the computed common-whisker
relations must first be carried there before it is applied to them.

## 4. A concrete two-cell invariant construction

There is a useful sufficient test. Suppose \(\nu\ne F\nu\) and
one verifies the full two-chain identity

\[
 d e_{F\nu}=a\,d e_\nu,
 \qquad a\in E,
 \qquad F(a)a=1.
\]

Since F swaps the E factors, every such group-element cocycle has the
form

\[
 a=t^{-1}F(t).
\]

For example, if \(a=(u,u^{-1})\), choose \(t=(1,u)\).
Put

\[
 p=t e_{F\nu},\qquad
 z=(1+F)p=t e_{F\nu}-t a e_\nu.
\]

Then (z\ne0\), (Fz=z\), and (dz=0\). It is an explicit
candidate in (H^2(C_2,Z_2)\), with

\[
 \kappa[z]
   =\operatorname{diagTate}(t\,d e_{F\nu})\pmod{J_I}.
\]

No assertion that its class is nonzero follows merely from (z\ne0\).
If (z=(1+F)z'\) for a syzygy (z'\), its kappa value is zero.

The chain test can be obtained from the stronger literal free-word
identity

\[
 F(r_\nu)=h r_\nu^{-1}h^{-1},\qquad h\in K_s,
\]

with (a\) the E image of (h\); the norm identity for a is checked
explicitly. If (h\) has a retained (F_5\) part, the correct target
cell index changes as in Section1. No such identity is assumed from
matching physical component labels.

More general finite collections of exact orbit identities can be
combined. A proposed invariant combination is verified by finite
group-ring comparison. This constructs candidates; it does not assert
that a selected finite list generates the full relation kernel.

## 5. Evaluate a candidate without dividing by two

The underlying abelian basis of (P_{\rm node}\) consists of pairs
\((e,\nu)\). Its F-action is negative permutation. For an invariant
finite-support syzygy (z\), coefficients on each free orbit
\(\lambda,F\lambda\) are opposite. Coefficients on fixed orbits
are zero. Choose one representative of each orbit and place its
coefficient in (p\) at that representative. Then

\[
 (1+F)p=z
\]

integrally. This is a finite exact operation and uses no division by
two. Compute (v=dp\). Its entire product-tree chain satisfies
\(Fv=-v\).

In the common R Cayley-tree basis, write a cell as a pair of oriented
edges \((u,i),(w,j)\). Negative swap implies that an anti-invariant
two-chain is symmetric. Its Tate diagonal is

\[
 \psi=\sum_{u,i}
   \bigl[\text{coefficient of }((u,i),(u,i))\bigr]
       u(x_i-1)\pmod2\ \in I_{\mathbb F_2[R]}.
\]

All off-diagonal cells disappear. This is the exact B91 diagonal map,
not augmentation of the whole two-chain. The required kappa
representative is \(\psi\bmod J_I\).

To **certify zero** modulo (J_I\), it suffices to exhibit a finite
identity

\[
 \psi=\sum_\ell g_\ell(i_\ell-1),\qquad i_\ell\in I,
\]

where each (i_\ell\) has an explicit word in the eight actual source
meridians and their eleven source-operator orbits. The completed
nineteen-source certificate now supplies those words and operators.
To certify a nonzero class, a genuine source-coset separator or other
complete membership argument is needed. Failure of rewriting in a
finite subset of source orbits does not provide that separator.

## 6. Current stopping point

Actual nonzero common-whisker syzygies are now exhibited by the
old-zero identities. Their passage to B92's equivariant kernel remains
an explicit presentation-comparison requirement. In an equivariant
presentation, symmetrizing a syzygy only gives a norm and no nonzero
kappa class. The next useful check is a full based F-orbit or multi-orbit identity
that yields a verified invariant syzygy not reduced merely to an
obvious norm, followed by the explicit diagonal calculation above.
The full old-base/deck indexing, relation-kernel effects, and actual
source cosets remain part of that check.

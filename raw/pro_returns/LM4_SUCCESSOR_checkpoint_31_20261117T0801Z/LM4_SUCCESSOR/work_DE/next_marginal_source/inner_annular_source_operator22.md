# Actual annular fixed source and its based zero-loop operator

DE research, checkpoint22. The exact computations are in
`check_inner_q0_source22.py/.out/.err` and `inner_q0_source22.json`.
This is an actual source and generic-fiber comparison. It does not
assert that the zero operator descends to the slit quotient: B111
proves that it does not.

## 1. The actual five source generators

In the inner bad region, the fixed source (z=0\) is

\[
\{0<|q|<1\}\setminus\{\beta_{11},\beta_{22},\beta_{33},\beta_{44}\}.
\]

Its fundamental group is the free group of rank five on the four
positive contact lassos and the actual positive zero lasso in the
same distinguished system. Before the other critical values are
filled, this source is the fixed section in the actual orbifold
bundle; after filling the five ordinary-node values their lassos
contract in the source.

In the original cone marking (c=x_2\), the four contact source
images are the already proved diagonal words

\[
\delta_a,\delta_d,\delta_e,\delta_b,
\qquad \delta_x=xcxc.
\]

Let (g_0\) be the actual positive far-section lift of the retained
zero lasso, with

\[
g_0^{-1}xg_0=\psi_0(x).
\]

As in the contact calculation, the fixed-section Borel strip gives
a unique even fiber word (v_0\) satisfying

\[
\psi_0(c)=v_0cv_0^{-1}.
\]

The actual fifth source generator is

\[
h_0=g_0v_0.
\tag{1}
\]

Both far and fixed-section lifts have even orientation. Uniqueness
uses the centralizer \(\langle c\rangle\) in the generic
\(C_2(c)*F_5\), before any filled relation is imposed. In contrast
to a contact lasso, the zero lasso is retained, so **(g_0\) is not
set to the identity**. The source generator is not the fiber word

\(v_0\) alone.

Its full raw word, in the original six indices, is

\[
v_0=(1,2,-1,3,5,6,-5,-3,1,2,-1,3,5,-6,-5,-3,-1,3,5,6,-5,-3,1).
\]

The certificate independently recomputes the chronological positive
and negative Artin arrays before peeling this unique even conjugator.

## 2. Corrected old-cone operator

The generic-fiber conjugation associated with the actual source lift is

\[
\chi_0=\operatorname{Inn}(v_0^{-1})\circ\psi_0,
\qquad h_0^{-1}xh_0=\chi_0(x),
\qquad \chi_0(c)=c.
\tag{2}
\]

For the negative loop, the unique even conjugator is

\[
v_- =\psi_0^{-1}(v_0^{-1}),
\]

and
\(\chi_0^{-1}=\operatorname{Inn}(v_-^{-1})\circ\psi_0^{-1}\).
All six images and all six inverse images are stored, and both
six-generator compositions reduce literally to the identity in

\(C_2(c)*F_5\). This is a true generic automorphism. In the full
annular presentation it acts on the fiber image after taking the
entire zero-operator saturation of the ten local relations; no
automorphism of the unsaturated slit quotient is inferred.

In the same-sheet B110 basis, followed by the root's (f\)-to-(w\)
change, the exact word may also be written

\[
v_0=c a^{-1}w^{-1}e^{-1}c e w
       [a,cac]a^{-1}w^{-1}e^{-1}.
\]

The single established contact relation \([a,cac]=1\) removes
that displayed commutator, if a shorter word in the slit presentation
is useful. The generator remains (g_0v_0\) in either notation.

## 3. Literal comparison with the q0-adapted basis

Use the actual q0 whisker

\[
W_0=(2,1,-2,-2,4,5,-4),\qquad
J=\operatorname{back}(W_0),\qquad Y_i=J(x_i).
\]

Here (J^{-1}=\operatorname{push}(W_0)\). The independently replayed
free-group substitutions are inverse on all six generators, before
imposing a cone square. In this local marking put

\[
C=Y_3=x_3^{-1}x_1c x_1^{-1}x_3,
\qquad F=Y_4=x_5x_6x_5^{-1},
\qquad K=x_3^{-1}x_1.
\]

Thus (C=KcK^{-1}\), (K\) is even, and in the B110 same-sheet
marking (K=ab^{-1}\). The other four (Y_i\), indexed by

\(i=1,2,5,6\), are denoted (U_i\).

The actual q0 action is the standard positive full twist on (C,F\)
and fixes the four (U_i\). The even lift associated with the
conjugate cone whisker is

\[
h_C=g_0CFC.
\]

Direct substitution yields all of the following, in the generic
orbifold group:

\[
[h_C,C]=1,\qquad h_C^{-1}Fh_C=CFC,
\qquad h_C^{-1}U_i h_C=(CFC)^{-1}U_i(CFC).
\tag{3}
\]

The actual old-cone source is the conjugate

\[
h_0=K^{-1}h_CK
   =g_0\,\psi_0(K)^{-1}CFC K.
\tag{4}
\]

The order in (4) follows from (K^{-1}g_0=g_0\psi_0(K)^{-1}\),
using the already calibrated positive-push convention. The independent
checker verifies the full fiber identity

\[
v_0=\psi_0(K)^{-1}CFC K
\]

literally, with no filled relation. Thus this is a based comparison
of the actual two cone whiskers, not just an abstract conjugacy of
involutions.

All four contact source words were also transported through this same
connector: in the (C\)-marking they are (K v_i K^{-1}\), and their
complete expressions in the (Y\)-basis are stored in the JSON, with
literal round trips. Together with (h_C\), these are the five
actual source generators in one common q0-adapted marking. They must
be used when a subsequent centralizer normal form is identified with
the geometric source.

## 4. Exact generic relative starting group and scope

For comparison with A's independently derived relative presentation,
put (k=h_CC\). Equation (3) gives

\[
[k,C]=[k,F]=1,\qquad g_0=kF^{-1}C.
\]

The generic mapping-torus group over the retained q0 circle, whose
quotient by the ten critical relations is the annular presentation,
is therefore

\[
\big((C_2(C)*\mathbb Z(F))\times\mathbb Z(k)\big)
 *_{\langle g_0\rangle}
 \big(F(U_1,U_2,U_5,U_6)\times\mathbb Z(g_0)\big).
\]

This follows by reversible substitutions in the generic mapping-torus
presentation. The edge is even, (k\) is odd, and (h_C=kC\) is
even. The ten actual based critical relations must still be imposed
simultaneously; they are not all relations of one of these factors.
No post-filling injection or fixed-subgroup theorem follows from this
generic amalgam alone.

The actual source has abstract rank five, and its image is generated
by the four stated contact images and (1), equivalently by the five
common (C\)-marked words above. The q-projection sends (h_0\) to
the generator of \(\pi_1(0<|q|<1)\cong\mathbb Z\), so this extra
source generator has infinite order and is not in the fiber image.
This does not by itself prove injectivity of the full free-five source
map, its full profinite topology, or the annular fixed-source equality.
Those remain separate geometric/group-theoretic gates.

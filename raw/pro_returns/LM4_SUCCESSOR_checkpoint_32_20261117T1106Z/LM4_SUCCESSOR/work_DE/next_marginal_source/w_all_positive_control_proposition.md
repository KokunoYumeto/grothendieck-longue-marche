# Research extension of B.83: all five positive old source lifts

**Status:** exact producer and proof completed after the checkpoint15 formal
cutoff; retained as research for independent review. The full marginal
equality is not claimed. B.83's frozen statement is unchanged.

Use the actual w-projection, source marking and source-adapted free basis

\[
(z,c_1,c_2,c_3,c_4,p_1,p_2,p_3,p_4,a,d,b)
\]

from `w_projection_common_transport.md`. Let `g_i`, `1<=i<=5`, be the
five actual source lifts over `w=zeta^{i-1}`. Their fiber actions are
arrays `1..5` in `w_source_adapted_basis.json`. Let `P_j=p_j^-` denote the
four other product source words. Put

\[
T_0=badb,\qquad C_3=c_4^{-1}c_3^{-1}c_4,\qquad
k=b^{-1}c_4b=\gamma_2^{-1}(c_4),\qquad
v_3=P_1^{-1}k^{-1}P_1k.
\]

The displayed equality for k is an actual source identity. Thus v3 is the
image of a word in the constant-family source kernel, and in particular
lies in J_c. The actual array3 action on `(b,C3)` is

\[
\gamma_3|_{\langle b,C_3\rangle}
=\operatorname{Inn}(v_3 C_3 b).
\]

Define the fourth deleted Nielsen generator

\[
c_2^*=c_4^{-1}c_3^{-1}z^{-1}T_0c_2^{-1}T_0^{-1}zc_3c_4.
\]

It is an actual constant-source-kernel element, with the literal witness

\[
c_2^*=(zc_3c_4)^{-1}
\gamma_1^{-1}(p_2^{-1}c_2^{-1}p_2)(zc_3c_4).
\]

The equality follows from the exact inverse w1 action, not from an
unbased peripheral identification. Replacing c2 by c2star is a Nielsen
change: its conjugator contains no c2, and the replacement inverts only
that generator. Both inverse substitutions on all twelve generators are
checked.

The actual array4 action on `(b,c2star)` is

\[
\gamma_4|_{\langle b,c_2^*\rangle}
=\operatorname{Inn}(v_4 c_2^* b).
\]

The correction v4 is not assumed to belong to J_c. Its exact source
expression is the following. Write `A=gamma4(P3)`,
`B=gamma4(P2)`, `C=gamma4(P1)`, and use the actual source k above. Then

\[
v_4=A P_3^{-1}P_2^{-1}k^{-1}P_2kP_2P_3A^{-1}
B^{-1}CBAP_3^{-1}P_2^{-1}P_1^{-1}.
\]

This identity is checked by free reduction in the actual generic fiber.
It was found by one targeted source-membership calculation using the
thirteen original source fiber words and their first old-action images;
the returned expression is independently substituted. The source word
vanishes after BOTH-family source filling: c4 and the old positive lift
g4 are killed, so k becomes1 and A,B,C become P3,P2,P1, after which the
displayed product freely reduces to1. Thus `v4 in I`, and certainly
`v4 in H`. No assertion `v4 in J_c` is used.

Set

\[
h_1=g_1,\quad h_2=g_2,\quad h_3=v_3^{-1}g_3,\quad
h_4=v_4^{-1}g_4,\quad h_5=g_5.
\]

These are all actual source words. The four h_i with i!=1 lie in the
actual both-family source kernel image I. Define

\[
\begin{aligned}
H_+&=\langle c_1,c_2^*,c_3,c_4,h_1,\ldots,h_5\rangle,\\
T_+&=\langle H_+,b\rangle,\\
J_+&=\langle\!\langle c_1,c_2^*,c_3,c_4\rangle\!\rangle_{H_+},\\
I_+&=\langle\!\langle c_1,c_2^*,c_3,c_4,h_2,h_3,h_4,h_5
\rangle\!\rangle_{H_+}.
\end{aligned}
\]

## Proposed exact conclusion

Let R_c and R be the actual ambient kernels for constant and both-family
filling, as in B.83. Then

\[
\begin{aligned}
T_+\cap R_c=T_+\cap J_c&=J_+,&
T_+/J_+&\simeq\mathbb Z\times F_5,\\
T_+\cap R=T_+\cap I&=I_+,&
T_+/I_+&\simeq\mathbb Z^2.
\end{aligned}
\]

The actual compact closures satisfy the same statements, with completed
free groups and integers. No full topology on abstract T_plus is assumed.

## Proof

Let eta_i be conjugation by h_i. The restrictions for eta2 and eta5 are
the ones in B.83. The corrected restrictions are

\[
\eta_3|_{\langle b,C_3\rangle}=\operatorname{Inn}(C_3b),\qquad
\eta_4|_{\langle b,c_2^*\rangle}=\operatorname{Inn}(c_2^*b).
\]

The ten signed b-conjugators can be chosen in the image K0 of

\[
\ker\bigl(F(b,c_1,c_2^*,c_3,c_4)\to\langle b\rangle\bigr).
\]

Explicitly, for eta1 through eta5 the forward conjugators are

\[
1,\quad c_4^{-1},\quad C_3,\quad c_2^*,\quad bc_1^{-1}b^{-1},
\]

and the inverse conjugators are

\[
1,\quad b^{-1}c_4b,\quad b^{-1}C_3^{-1}b,\quad
b^{-1}(c_2^*)^{-1}b,\quad c_1.
\]

All ten identities, all 120 whole-basis action/inverse identities, and
all 24 inverse Nielsen identities have passed the exact checker.

First K0 lies in J_plus. The eta2/eta5 node arguments give the whole b
strips of c4/c1. The eta3 node gives the whole b strip of C3; combining
with the c4 strip gives the whole c3 strip. The eta4 node gives the whole
c2star strip. These four strips generate the entire indicated free-group
kernel, including mixed products. Only their images in the actual
surface group are used.

Now apply the valid stage argument of B.83 to the orbit of K0 under the
five eta_i and their inverses. The correcting elements belong to K0
itself, so every successive stage is b-normal. The union equals J_plus:
it contains all four source seeds and is invariant under the five source
lifts, and conversely K0 was generated by their orbits of the seeds.
Thus J_plus is normal in T_plus.

Modulo J_plus, b commutes with all five h_i. The actual character chi_b
(minus conventional winding of `(vw-1)/(w-1)^2`) kills H_plus and sends
b to1. The actual w-base projection sends the five h_i to the five
positive-root basis members of F6; the correction words v3/v4 lie in the
fiber and therefore do not change those projections. The selected F5 is
a free factor of F6. These maps give the inverse detector to the
surjection `Z x F5 -> T_plus/J_plus`. They factor through the actual
constant-family filling. Hence its kernel on T_plus is exactly J_plus,
and so is T_plus intersect J_c.

The image of H_plus in this product quotient is exactly `{0} x F5`.
The four h_i with i!=1 are killed by the actual both-family source
filling, as proved by their explicit source words. Their normal closure
in F5 is normal in the entire product, and the quotient is Z^2. The
characters chi_b and winding of w-1 both factor through the both-family
filled surface and detect that product. This proves the second equality.

For the compact version, take the actual closures in the ambient full
completion. Use the abstract free presentation group F9 on the nine
selected source WORDS, and its free retraction killing the four deleted
seeds. Its compact image is the actual closure of H_plus, and the image
of its compact kernel is the closure of J_plus. The actual F5 base
detector identifies the surviving five-word quotient exactly. For the
both-family statement, use the analogous free retraction retaining only
h1. We do not assert that these nine words are a subset of a free basis
of F19, or that H_plus has its full induced topology there. The universal
pro-direct-product presentations give the surjections from Zhat x F5hat
and Zhat^2; the actual completed detectors are their left inverses. They
also factor through the actual filled completions. This proves the
compact equalities without identifying an abstract completion of T_plus
with its ambient closure.

## Exact scope and outstanding operators

This controls all mixed words in the displayed actual subgroup and all
five corrected positive old source operators. It does not include the
old zero operator or arbitrary retained source fiber conjugations.
Although the four deleted generators are a Nielsen replacement, this
does not show that every conjugate under the full source H lies in the
controlled subgroup. The original whole marginal and joint-source
conditions remain open.

Certificates: `check_w_fourth_strip_correction.py/.out`,
`w_fourth_strip_correction.json`, `check_w_all_positive_control.py/.out`,
`w_all_positive_control.json`. The separate corrected-c3 proof is
independently checked in `work_CE/research_third_product_strip_15h.txt`.

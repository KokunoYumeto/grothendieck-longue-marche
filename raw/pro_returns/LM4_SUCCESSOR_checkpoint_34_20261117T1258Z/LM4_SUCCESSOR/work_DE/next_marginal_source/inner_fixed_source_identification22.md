# Actual fixed-cone source in the inner slit bad region

DE independent proof and certificate, checkpoint22. This concerns the
inner **bad** vertex and its fixed section (t=\infty\), equivalently

\[
z=1/t=0,\qquad y=z^2=0.
\]

It does not identify this section with the other fixed section (t=0),
and makes no annular or global gluing assertion. The separate RAAG/HNN
centralizer theorem is not used to construct the source words.

## 1. Actual source and its four positive generators

The actual regional orbifold has the six trajectories

\[
0,\ q,\ h_1(q)^2,\ldots,h_4(q)^2,
\qquad
h_u(q)=\frac{u^2+(1-2u)q}{q+u^2-2u},
\]

where (0) is an order-two cone and (u=\zeta_5^i). Fix the common
base (q_*=4/5+i/2), the projected upper-comb marking of the complete
six-strand certificate, and its one radial disk-to-far connector. Let
\(\Omega\) be the simply connected slit subbase containing the nine
filled critical values and their nine distinguished lassos, and excluding
the old base puncture (q=0). Such a slit exists because the independent
path audit supplies one distinguished ten-lasso system, including the
lasso at zero. Cutting along the zero slit leaves precisely the nine
other based peripheral generators.

The fixed section (z=0) is deleted exactly at the four simple zeros

\[
\beta_{ii}=u_i^2/(2u_i-1),\qquad i=1,2,3,4.
\]

The branch (y=q) does not meet it on \(\Omega\), and the other five
critical values are ordinary nodes away from this section. Consequently
its actual source is

\[
D_\infty\cap Q_\Omega
\cong \Omega\setminus\{\beta_{11},\beta_{22},\beta_{33},\beta_{44}\},
\qquad \pi_1\cong F_4.
\]

Its four positive free generators are the same four contact lassos in
the certified distinguished system. The other five based critical
lassos contract in this source when their ordinary critical values are
filled. This is a statement about the actual fixed section, not a
choice of four abstract elements in a centralizer.

## 2. Based Borel transport fixes the conjugator unambiguously

First delete all nine critical values. The orbifold family is then a
genuine bundle, with generic group

\[
W=C_2(c)*F(a,b,d,e,f).
\]

The physical initial order is

\[
(a,c,b,d,e,f)=(x_1,x_2,x_3,x_4,x_5,x_6)
=[h_1^2,0,h_4^2,h_2^2,h_3^2,q].
\]

The orientation character \(\epsilon:W\to C_2\) sends only (c)
to the nontrivial element. It is the actual (z\mapsto z^2) cover
character. Choose the cone whisker from the common far basepoint once.
The global normal coordinate (z) makes the Borel space of the fixed
section a literal product with (BC_2). Its positive base loop, with
the identity in the (BC_2) factor, therefore has orientation zero.

The far section also has orientation zero: in the plane model its value
is the constant (y=10/\mathrm{ROT}), so one constant square root gives
its lift. The radial plane-to-disk homeomorphism has a radial lift and
does not change this sign. Thus the two based source/far lifts use the
same actual double cover.

Write (g_i\) for the positive far-section lift of a contact lasso, and
\(\psi_i\) for its actual geometric positive push. The certified
chronological convention is

\[
g_i^{-1}xg_i=\psi_i(x).
\tag{1}
\]

Let \(s_i\) denote the positive lift along the fixed cone, brought to
the far basepoint by the chosen cone whisker. The based Borel strip
along that section gives \([s_i,c]=1\), and the two lifts have the
same base loop. Hence in the actual bundle there is a unique fiber
element (v_i=g_i^{-1}s_i\) with

\[
s_i=g_i v_i,
\qquad \psi_i(c)=v_i c v_i^{-1},
\qquad \epsilon(v_i)=0.
\tag{2}
\]

This also checks the order and sign in (2) directly from (1):
\((g_i v_i)^{-1}c(g_i v_i)=c\). Conversely, in the generic free
product, the centralizer of the factor involution (c) is exactly
\(\langle c\rangle\), by reduced normal form. Thus all conjugators
of (c) in the displayed equation differ on the right by (1) or

\(c\), and exactly one has orientation zero. The unique even
conjugator extracted from the literal positive-push word is therefore
the actual source lift in (2), not an arbitrary conjugator selected
after the regional relations have been imposed.

The far section extends across each inserted critical disk. After its
filling (g_i=1\), so the actual positive fixed-source peripheral has
image exactly (v_i\). This establishes the geometric interpretation
before using any proposed centralizer structure of the filled group.

## 3. Exact four source words

Apply the same-sheet triangular change independently checked in both
directions in the regional normalization certificate. The new letters
keep the indices (1,2,3,4,5,6\), so they are denoted again by

\[
(a,c,b,d,e,f),
\]

but now the four contact relations are

\[
[a,cac]=[b,cbc]=[d,cdc]=[e,cec]=1.
\tag{3}
\]

For an ordinary letter (x\), write \(\bar x=cxc\),
and \(\delta_x=x\bar x\). The four exact even cone conjugators,
obtained from the actual `positive_push["2"]` arrays, are as follows.

| Actual positive contact lasso | Literal normalized source word | Reduction using only (3) |
|---|---|---|
| \(\beta_{11}\) | \(a\bar a\) | \(\delta_a\) |
| \(\beta_{22}\) | \(\bar d d\) | \(\delta_d\) |
| \(\beta_{33}\) | \(a[\bar e,e]a^{-1}\,e\bar e\) | \(\delta_e\) |
| \(\beta_{44}\) | \(a[\bar b,b]a^{-1}\,b\bar b\) | \(\delta_b\) |

In particular, none of these words contains the branch letter (f\),
and the later (f\)-to-(w\) change is immaterial to these four
equalities. The long raw words and the exact reduced normalized words
are all retained in the independent JSON; no whole-word conjugator
has been suppressed in this table.

The equality test uses the exact normal form in

\[
\Bigl(*_{x\in\{a,b,d,e\}}\mathbb Z^2(x,\bar x)\Bigr)
*F(f,\bar f),
\]

which is the orientation kernel after imposing only the four contact
relations. It therefore establishes the reductions before any of the
six remaining ordinary node relations are used.

## 4. Actual free-four detector and full topology

For the complete slit presentation, make the root's two-sided verified
change

\[
S=acac,\qquad
w=(ba^{-1}f^{-1}ab^{-1}e^{-1})S^{-1},
\qquad
f=ab^{-1}e^{-1}S^{-1}w^{-1}ba^{-1}.
\tag{4}
\]

On the orientation kernel define \(p\) by keeping the unbarred

\(a,b,d,e\) and killing all their barred partners and (w,\bar w\).
The independent checker verifies all ten full relators and their ten
cone conjugates under (p\). This is precisely the complete
Reidemeister--Schreier relator family for the index-two kernel; thus

\[
p:R_\Omega^0\longrightarrow F(a,b,d,e)
\]

is an actual homomorphism of the filled regional group.

The four source images have projections

\[
p(v_{11})=a,\quad p(v_{22})=d,\quad
p(v_{33})=e,\quad p(v_{44})=b.
\tag{5}
\]

These are the standard free basis in a permutation. The inverse basis
words are the corresponding permutation, not a finite-rank numerical
test. Therefore the actual source map (F_4\to R_\Omega^0\) is
injective, its image is exactly

\[
\langle\delta_a,\delta_b,\delta_d,\delta_e\rangle,
\]

and composing (p\) with the inverse of the permutation in (5) gives
a retraction onto this actual source subgroup.

It follows also that this subgroup has its full profinite topology in
the ordinary regional group: every finite source quotient extends by
the retraction. The ordinary group has index two in the orbifold group,
so its completion embeds in the orbifold completion. Consequently the
actual closed fixed-source image is a copy of \(\widehat F_4\).
If the separately proved slit centralizer theorem identifies the
centralizer of (c) with the diagonals (discretely or in the actual
completion), the source equality follows immediately from the present
based identification. No full centralizer theorem was needed to obtain
the four source words or their topology.

## 5. Genuine independent evidence and scope

Producer and genuine outputs:

- `work_DE/next_marginal_source/check_inner_fixed_source22.py`
- `work_DE/next_marginal_source/check_inner_fixed_source22.out`
- `work_DE/next_marginal_source/check_inner_fixed_source22.err`
- `work_DE/next_marginal_source/inner_fixed_source22.json`

The executed checker independently verifies four unique even
conjugators, all twelve Nielsen inverse substitutions, all twelve
branch/stable-letter inverse substitutions, the four cone-only
equalities, and all twenty complete ordinary relators under the
free-four detector. Its input hashes bind it to the actual based
six-strand record and the two marked normalization records.

The separate path/deformation and disk/plane comparisons are reviewed
in the regional audit. The present result concerns the actual simply
connected slit base. In particular, it does not assert stability under
the retained old (q=0\) monodromy, does not replace the annular group
by this slit group, and does not identify either natural mixed-neck
kernel with the whole source kernel.

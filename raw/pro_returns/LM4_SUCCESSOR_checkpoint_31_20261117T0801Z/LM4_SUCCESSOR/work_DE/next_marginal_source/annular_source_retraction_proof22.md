# Actual annular source: a free-five retract

DE complete research proof, checkpoint22. This strengthens the actual
source identification but by itself does not identify the full annular
cone centralizer. The genuine certificate is
`check_annular_source_retraction22.py/.out/.err` and
`annular_source_retraction22.json`.

## 1. Complete actual ordinary presentation

Use the common q0-adapted basis certified in
`inner_annular_source_operator22.md`:

\[
C=Y_3,\quad F=Y_4,\quad U_i=Y_i\ (i=1,2,5,6),\quad
\bar x=CxC,\quad h=h_C=g_0CFC.
\]

The orientation kernel of the generic orbifold fiber is the free
group on the ten elements (U_i,\bar U_i,F,\bar F\). The actual
source lift has conjugation

\[
\begin{aligned}
h^{-1}Fh&=\bar F,&h^{-1}\bar Fh&=F,\\
h^{-1}U_i h&=\bar F^{-1}U_i\bar F,
&h^{-1}\bar U_i h&=F^{-1}\bar U_iF.
\end{aligned}
\tag{1}
\]

These follow from the actual based positive q0 transport, not an
abstract replacement of that operator. Since (h\) is even and
commutes with (C\), Reidemeister--Schreier with representatives

\(1,C\) gives exactly these ten mapping relations for the ordinary
group. The full annular ordinary presentation adds the ten actual
node words and their ten (C\)-conjugates. Relations (1) then impose
all signed source translates automatically. No stability of the
ten-relator slit quotient under q0 is assumed.

The actual source is the punctured disk with the four contact points
and zero removed, so its abstract group is (F_5\). The five common

\(C\)-based source generators are (h\) and the four literal words

\(K v_i K^{-1}\), where (K=x_3^{-1}x_1\) and the four (v_i\)
are the unique even contact conjugators. These complete words in the

\(Y\)-basis were independently checked, not chosen merely by their
peripheral classes.

## 2. An actual whole-presentation detector

Let (T=F(X_1,X_2,X_3,X_4,H)\). Define a map on the preceding
ordinary presentation by

| Generator | Image | Conjugate generator | Image |
|---|---|---|---|
| (U_1\) | (X_1\) | (\bar U_1\) | (1\) |
| (U_2\) | (1\) | (\bar U_2\) | (X_2\) |
| (U_5\) | (X_3\) | (\bar U_5\) | (1\) |
| (U_6\) | (X_4\) | (\bar U_6\) | (1\) |
| (F\) | (H\) | (\bar F\) | (H\) |

and send (h\) to (H\). Each relation (1) is satisfied: both
branch images equal (H\), and every retained ordinary generator
is conjugated by (H^{-1}\) on both sides of its mapping relation.
The inverse mapping relations agree as well.

All twenty complete node relators have trivial image. This is
verified literally, with the simultaneous node's two words kept
separate. There is also a geometric explanation for the choice of
four killed peripherals: in the actual q0-adapted marking the
conjugator parities of (U_1,U_2,U_5,U_6\), relative to the initial
four (A\) sheets, are (0,1,0,0\). Thus the retained entries in
the table are precisely the four (A\) meridians and the killed
entries the four (B\) meridians. Every actual physical critical
node pairs an (A\) with a (B\); its commutator becomes trivial
under this filling. The literal twenty-word check independently
retains every transported whisker.

Consequently the assignment defines a homomorphism

\[
D:R_{\rm ann}^{0}\longrightarrow T
\tag{2}
\]

of the actual filled annular ordinary group. It is not merely a map
of the generic fiber or a finite set of orbit words.

## 3. Exact images of the actual source and the inverse basis

In the physical contact order (11,22,33,44\), followed by the zero
source loop, the five actual source images under (2) are

\[
X_2,\quad
(X_2HX_3)X_4(X_2HX_3)^{-1},\quad
X_3,\quad X_1,\quad H.
\tag{3}
\]

Write the five abstract source generators in that order as

\(s_1,s_2,s_3,s_4,s_5\). The inverse change of free basis is

\[
X_1=s_4,\quad X_2=s_1,\quad X_3=s_3,\quad H=s_5,\qquad
X_4=s_3^{-1}s_5^{-1}s_1^{-1}s_2s_1s_5s_3.
\tag{4}
\]

Both compositions of these five-generator substitutions are the
identity in a free group, as separately checked. Thus (D\) composed
with the actual source map is an isomorphism from its abstract

\(F_5\) onto (T\). The actual source map is injective. Composing

\(D\) with its inverse onto the actual source image gives a retraction
of (R_{\rm ann}^{0}\) onto that image.

## 4. Full profinite topology and exact scope

Every finite quotient of the source extends over the ordinary group
by the retraction. Its full profinite completion therefore embeds
in the ordinary ambient completion and equals its actual compact
source image. The ordinary group has index two in the orbifold group,
so its topology there is full by finite-index cores. The actual
closed source image in either completion is consequently

\(\widehat F_5\).

This proves source injection and its full topology in the actual
annular bad region. It does not, by itself, show that every cone-fixed
element is a source element. A subsequent independently established
annular centralizer normal form may use the actual detector and
literal source images (3) to identify its fixed subgroup with this
source. Rank equality alone is not used.

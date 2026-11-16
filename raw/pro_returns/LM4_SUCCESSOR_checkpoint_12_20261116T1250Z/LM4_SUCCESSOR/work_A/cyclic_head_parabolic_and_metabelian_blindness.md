# Cyclic-head parabolic cohomology and an exact metabelian limitation

Research proof and executed certificate, 16 November 2026. This is not
inserted into the formal register. It supplies a verified source example
and identifies a quotient family which cannot decide the full negative
order problem.

## 1. The general parabolic dimension calculation

Let `Pi=<s,r | s^2=r^3=1>^` and `tau=sr`. Let `V` be a finite-dimensional
continuous representation over a finite field `k`; write `S,R,T=SR` for
the three matrices, `d=dim V`, and `d_a=dim V^a`. Define parabolic
cohomology to be the subspace of `H^1(Pi,V)` whose restrictions to
`<s>`, `<r>` and the procyclic cusp `<tau>` are coboundaries. Then

\[
 \dim H^1_{\rm par}(\Pi,V)
 =d-d_s-d_r-d_\tau+\dim V^\Pi+\dim(V^\vee)^\Pi.       \tag{1}
\]

This formula also applies in characteristics two and three. A direct
proof avoids an implicit semisimplicity assumption. A cocycle trivial
on the two factor cohomology groups has source values in
`im(1-S)` and `im(1-R)`. The cusp condition is that their sum `a+Sb`
vanish in `V/im(1-T)`. The map to that cokernel has cokernel dual to
the simultaneous fixed vectors of `S` and `R` in `V^vee`: indeed
`1-SR=(1-S)+S(1-R)`. Its rank is therefore
`d_tau-dim(V^vee)^Pi`. Subtracting the coboundary dimension
`d-dim V^Pi` gives (1).

For our earlier irreducible36-dimensional coefficient over `F8`, the
fixed dimensions are20,12,4 and there are no global invariants. Thus
(1) is zero, consistently with the actual joint restriction isomorphism
used in the44/40-dimensional cochain argument. That vanishing is a
property of that coefficient, not a consequence of the free-product
presentation for arbitrary coefficients.

## 2. An actual cyclic-head example with nonzero parabolic space

Put `K=Pi'`, the closed derived subgroup. Its quotient is `C6`; the
images of `s,r,tau` are3,4,1 respectively. The index-six
Bass--Serre graph has edges indexed by `Z/6`, with edge `i` joining
the vertex `i mod3` of type `s` to the vertex `i mod2` of type `r`.
It is the complete bipartite graph with3 and2 vertices. The subgroup
`K` is full free profinite of rank2.

Choose the spanning-tree edges0,1,2,3. The two integral cycle vectors
associated with the remaining edges4 and5 are

\[
 (-1,-1,0,1,1,0),\qquad (1,0,-1,-1,0,1).
\]

Deck translation by `tau` and the actual canonical conjugation act on
this basis by

\[
 T=\begin{pmatrix}1&-1\\1&0\end{pmatrix},\qquad
 C=\begin{pmatrix}0&1\\1&0\end{pmatrix}.                 \tag{2}
\]

At edge level these are `i -> i+1` and `i -> 3-i`. The latter uses
the actual source formulas `c(s)=s`, `c(r)=sr^{-1}s`.
In particular `T^3=-I`, `T^6=I`, and `CTC=T^{-1}`.

Take `V=F5^2` with the action factoring through `C6`, so `S=T^3` and
`R=T^4`. None of `S,R,T` has a fixed vector. The representation is
irreducible over `F5`, since `X^2-X+1` is irreducible there. Formula
(1) gives

\[
 H^1_{\rm par}(\Pi,V)=H^1(\Pi,V)\simeq\mathbf F_5^2,
 \qquad H^1(C_6,V)=0.                                  \tag{3}
\]

The finite-head vanishing follows from coprime averaging. The source
calculation is equally direct: the cocycle values on `s` and `r` are
arbitrary vectors (four parameters), and the coboundaries have
dimension two. Every restriction is a coboundary because the three
matrices minus identity are invertible.

This is an actual source quotient, not a merely abstract module. In
`V semidirect C6`, with action `T`, set

\[
 a=(1,1),\qquad s_0=(a,3),\qquad r_0=(a,4).
\]

Then `s_0^2=r_0^3=1`, `s_0r_0=(0,1)`, and the source image is the
whole group of order150. For instance the commutator with the cyclic
section yields `a-Ta=(1,0)`, and its `T`-translate spans `V` with it.
Since `K/Phi_5(K)` has order25, the kernel of this source map is
exactly

\[
                \overline{[K,K]K^5}.                    \tag{4}
\]

It is characteristic in `Pi`. Thus the nonzero parabolic classes in
(3) really occur in the source's finite relation-module quotients.

## 3. Why this example does not obstruct negative order

In fact the complete metabelian quotient is blind to the negative
square of **every** full cusp-fixing automorphism.

Let `K'` mean the closed commutator subgroup of `K`. Reading `tau^6`
in the six-sheeted graph gives, at the `s`-vertex, the successive
oriented edge pairs

\[
             e_{j+3}\,e_{j+1}^{-1},\quad j=0,\ldots,5
                         \quad(\text{indices modulo six}).
\]

After the four tree edges are collapsed the word is exactly
`e4 e5 e4^-1 e5^-1`. Consequently `tau^6` is the primitive boundary
commutator in this free basis of `K`. In particular it vanishes in
`K^ab`, and the actual image of `tau` supplies a cyclic section:

\[
       \Pi/K'\simeq\widehat{\mathbf Z}^{\,2}\rtimes_T C_6.
                                                               \tag{5}
\]

One can also verify (5) from the affine source formula of Section2
over `Zhat`: its derived image is the entire translation module,
and the resulting surjection between two copies of `Zhat^2` is an
isomorphism. This keeps both the group extension and the source
section explicit.

Let `h` be any continuous automorphism of `Pi` fixing `tau` literally.
It acts trivially on `Pi/K=C6` and fixes the section in (5), so its
action there is a matrix `P` on the translation module, with

\[
                            PT=TP.                       \tag{6}
\]

Because `h(tau^6)=tau^6`, comparison in
`gamma_2(K)/gamma_3(K)=Zhat` using the primitive commutator just
computed gives

\[
                            \det P=1.                    \tag{7}
\]

The centralizer of the cyclic matrix `T` over `Zhat` is
`Zhat[T]`; write `P=uI+vT`. Since `T^{-1}=I-T`, direct multiplication
gives

\[
 CPC=uI+vT^{-1}=(u+v)I-vT=\operatorname{adj}(P).
\]

Combining this with (7) proves

\[
                  (hc)^2=1\quad\text{on }\Pi/K'.         \tag{8}
\]

No full order-two hypothesis on `hc` was used. Therefore every finite
quotient of (5), and their entire inverse limit, passes this negative
action-square test for every actual full positive `h`.

The actual factor-frame norms pass as well. The action of `hc` on
the cyclic head is inversion, so the norm of any actual factor
conjugator has zero cyclic image. By (8) it centralizes the relevant
factor. Inside the integral translation module the fixed spaces of
`s` and `r` are zero: their defining determinants are4 and3, which
are nonzero divisors on `Zhat`. Hence those projected norms are
literally one. The assertion concerns norms of actual full frames;
it does not assert uniqueness of all frame choices in every finite
quotient separately.

This explains why the example in (3) cannot itself obstruct a
parity-one involution. Nonzero parabolic cohomology alone is not a
negative norm obstruction. Its symplectic boundary condition and
the actual CM torus covariance make this quotient's negative square
automatic.

## 4. Executed certificate and scope

The standard-library program
`work_A/code/check_cyclic_head_parabolic.py` executed successfully.
It verifies the integral cycle matrices and the collapsed primitive
commutator, enumerates the actual150-element source group, verifies
canonical conjugation on all22500 products, lists the24 invertible
centralizer matrices over `F5`, and checks all900 negative squares
for its six determinant-one matrices. The output and exact matrices
are retained in

- `work_A/code/check_cyclic_head_parabolic.out`;
- `work_A/cyclic_head_parabolic_certificate.json`.

The integral argument in Section3 is separate from these finite
checks. The only group-theoretic structural inputs are the already
used open-subgroup Kurosh theorem, the explicit finite cover graph,
and the class-two commutator formula for a free profinite group.
There is no assertion that all finite quotient actions lift, that
all noncentral embedding problems are solvable, or that a full
negative involution has been constructed.

For the main task, the next useful input must go beyond this complete
metabelian quotient and must control the actual source action and
all permitted frames. The prescribed-frame obstruction A.76 and its
finite detector A.77 do that for their specified datum; A.78 shows
why the same six-cup calculation does not exclude every frame.

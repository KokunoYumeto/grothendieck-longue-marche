\documentclass[11pt,a4paper]{article}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage[a4paper,margin=27mm,headheight=14pt]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathrsfs,mathtools}
\usepackage{array,booktabs,longtable,tabularx,enumitem,graphicx}
\usepackage{xcolor,microtype}
\usepackage{hyperref}
\hypersetup{colorlinks=true,linkcolor=blue!45!black,citecolor=blue!45!black,
 urlcolor=blue!45!black,pdftitle={LM7: The Fermat tower in the metabelian approximation},
 pdfauthor={GPT-6 Astra, OpenAI, ChatGPT Pro mode}}
\urlstyle{same}
\setlength{\parindent}{1.3em}
\setlength{\parskip}{.22em}
\setlength{\emergencystretch}{2em}
\setlength{\LTpre}{.6em}
\setlength{\LTpost}{.6em}
\setlist{nosep}
\setcounter{secnumdepth}{0}
\setcounter{tocdepth}{1}
\allowdisplaybreaks[2]
\newenvironment{statement}[3]{%
 \par\addvspace{1.1em}\phantomsection\label{st:#1}%
 \noindent\textbf{#1. #3}\quad\textsf{\small[#2]}\par\nobreak\smallskip\ignorespaces
}{\par\smallskip}
\newcommand{\statementref}[1]{\hyperref[st:#1]{#1}}
\newcommand{\Sha}{\mathop{\mathrm{Sh}}}
\begin{document}
\subsection{An actual lift in the remaining arithmetic character blocks}

\begin{statement}{D.60}{Proved}{Integral projective covers repair twelve further central blocks over the actual arithmetic source}
Use the sources and maps of D.58--D.59, in particular
\[
 X=\widehat B/(R_{50}\cap L_2),\qquad
 Y=X/\mathcal K,\qquad
 \mathcal K=\ker(Z\to Z_*),\qquad
 \mathcal K_\Delta=\mathcal K^\Delta.
 \tag{D.60.1}
\]
Write \(\Pi_{59}\), \(\mathcal C_{59}\), and
\(\mathcal J_{59}=(1-\Pi_{59})\mathcal K_\Delta\)
for the projector and submodules of D.59.
The actual map of D.56 is
\[
 \phi:\Delta\twoheadrightarrow A_*=(\mathbb Z/3)^4,
 \qquad
 G\twoheadrightarrow G^\dagger=A_*\rtimes Q
       \twoheadrightarrow G_*=A_*\rtimes Q_*.
 \tag{D.60.2}
\]
Here \(|G^\dagger|=46656\), \(|G_*|=3888\),
\(\ker(G\to G^\dagger)\simeq(\mathbb Z/3)^{93}\),
and \(\ker(G^\dagger\to G_*)=A_4\), with its
literal embedding in \(Q\) from D.56. These are
quotients of the same marked source \(\widehat B\).

The forty nonzero unordered characters pulled back
from \(A_*\) split into the following four actual
\(Q\)-orbits. In the table \(\mathcal D_\ell\) is
the kernel of their invariant exterior map to the
small source, induced from the indicated orbit.
The two norm ranks use the full group norm, before
and after the actual compactification map.
\[
\begin{array}{c|r|r|r|r|r}
 \ell&|Q\{\ell,-\ell\}|&|\operatorname{Stab}_Q\{\ell,-\ell\}|
 &\dim(\mathcal D_\ell)_G
 &\operatorname{rank}\nu|_{\mathcal D_\ell}
 &\operatorname{rank}(\bigwedge^2\pi)\nu|_{\mathcal D_\ell}\\\hline
 (0,0,0,1)&8&72&126&118&36\\
 (0,0,1,1)&12&48&196&158&34\\
 (0,0,1,2)&12&48&196&158&34\\
 (0,1,0,0)&8&72&122&114&34
\end{array}
 \tag{D.60.3}
\]
Consequently their actual 366080-dimensional kernel
\(\mathcal D\subset\mathcal J_{59}\) has
\(\dim\mathcal D_G=640\). The compact norm has
rank 138 and kernel dimension 502 on these
coinvariants. This calculation keeps the kernel
of that comparison map.

In each of the two orbits of size eight there are
four explicit, mutually orthogonal, integral
\(G\)-equivariant projectors
\(e_{a,i}:U\to U\), where \(a=1,2\) and
\(1\leq i\leq4\). Their images
\(E_{a,i}\) have rank 128 over \(\mathbb Z_2\).
They satisfy
\[
 \theta_U E_{a,i}=0,\qquad
 e_{a,i}\mathcal R=0,\qquad
 \pi:E_{a,i}\hookrightarrow U/\mathcal R,
 \tag{D.60.4}
\]
where \(\mathcal R\) is the full integral cusp
homology. Their reductions, including the
affine embeddings and all stabilizer actions,
are the literal matrices in the certificates.

For orthogonal idempotents \(p,q\) put
\[
 (p\boxtimes q)(u\wedge v)
       =pu\wedge qv+qu\wedge pv.
\]
On the actual central module define
\[
 \begin{aligned}
 \Pi_{60}&=e_\Delta
        \sum_{a=1}^{2}\sum_{1\leq i<j\leq4}
                    (\bar e_{a,i}\boxtimes\bar e_{a,j}),\\
 \mathcal C_{60}&=\Pi_{60}Z,\qquad
 \mathcal J_{60}=(1-\Pi_{59}-\Pi_{60})\mathcal K_\Delta.
 \end{aligned}
 \tag{D.60.5}
\]
The bars denote reduction modulo two.
These are equivariant idempotents with disjoint
images, and
\[
 \begin{gathered}
 \mathcal C_{60}\subset\mathcal D,
 \qquad \mathcal J_{59}=\mathcal C_{60}\oplus\mathcal J_{60},\\
 \dim\mathcal C_{60}=12288,
 \qquad\dim(\mathcal C_{60})_G=28,\\
 \nu:(\mathcal C_{60})_G\xrightarrow{\ \sim\ }
                                  \mathcal C_{60}^{G},
 \qquad
 \bigwedge^2\pi\text{ is injective on }\mathcal C_{60}.
 \end{gathered}
 \tag{D.60.6}
\]

There is an actual continuous peripheral
automorphism of
\[
                         X_{60}=X/\mathcal J_{60}.
 \tag{D.60.7}
\]
It has multiplier one, fixes \(t\), is identity
on \(G\), and retains the complete D.57 action
and its chosen compatible conjugators on
\(X_*\). It retains the full prescribed
\(\mathcal W_h\) action, the literal normalized
parameter, and all established metabelian and
CM comparison maps through that projection.
Its homology matrix is identity on all eight
\(E_{a,i}\). The chosen D.59 homology action
is replaced on exactly the two stated
character-orbit summands and is unchanged
on their complement. The new action descends
to \(X_{59}\), but no assertion is made that
this is the previously chosen D.59 action.

All comparison maps are induced by the same
source, and their exact kernels are
\[
 \begin{aligned}
 \ker(X_{60}\to Y)
    &=(1-e_\Delta)\mathcal K
                   \oplus\mathcal C_{59}\oplus\mathcal C_{60},\\
 \ker(X_{60}\to X_{59})&=\mathcal C_{60},\\
 \ker(X\to X_{60})&=\mathcal J_{60},\\
 \dim\mathcal J_{60}
    &=48w-2560-5308416\kappa-12288.
 \end{aligned}
 \tag{D.60.8}
\]
Here \(w,\kappa\) retain their actual meanings
from D.59. The specified residual in the
forty small-character components now has
dimension 353792 and coinvariant dimension
612. In particular the remaining kernel is
nonzero. The exact full-source kernel is
\[
 \begin{aligned}
 S_{60}&=\{b\in R_{50}:
          \operatorname{im}_{\mathcal T_2}(b)\in\mathcal J_{60}\},\\
 S_{60}/(R_{50}\cap L_2)&=\mathcal J_{60}.
 \end{aligned}
 \tag{D.60.9}
\]
The remaining boundary in
\((\mathcal J_{60})_G\) and the full profinite
realization are not evaluated here.
The manuscript passages are Part D(e),
section 51.16, folio 734 verso, scan 174,
and section 51.15, folios 725--727,
scans 156--160.
\end{statement}
\begin{proof}
\emph{The two actual covers and their coefficient maps.}
Use D.56's affine marking on \(A_*\rtimes Q\):
\(s=(0,S)\) and \(r=(v_*,R)\), with
\(v_*=(1,1,1,0)\). Its full image is the
order-46656 group in (D.60.2); its projection
on the recorded four-dimensional representation
of \(Q\) gives the order-3888 image. The
restriction to \(\Delta\) is exactly \(\phi\).
It is onto \(A_*\), and its kernel therefore
has order \(3^{93}\). The second kernel is
the actual order-12 subgroup
\(A_4=\ker(Q\to Q_*)\); its translation
coordinate is zero. This proves both kernels
in (D.60.2), with the original source maps.

Let \(K^\dagger\) be the kernel of
\(B\to G^\dagger\). It has free rank
\(1+46656/6=7777\); the small kernel has
rank \(1+3888/6=649\). The quotient
\(K^\dagger/K_3\) is the indicated odd
group. For every finite coefficient ring
\(\mathbb Z/2^k\), its positive homology
vanishes by averaging. The five-term sequence
therefore identifies
\[
 (K_3^{\rm ab}/2^k)_{\ker\phi}
       \xrightarrow{\ \sim\ }
                     (K^\dagger)^{\rm ab}/2^k.
 \tag{D.60.10}
\]
The map sends the class of the same source
word to its class in the larger kernel.
Taking inverse limits proves the integral
identification. Thus the character blocks
pulled back from \(A_*\) in the full
arithmetic homology are exactly the blocks
of this marked finite cover. No other
finite source is substituted for them.

Put \(\mathcal O=\mathbb Z_2[\zeta_3]\).
For a nonzero character \(\ell\) of
\(A_*\), the \(\ell\)-part of the
Bass--Serre edge module has one basis vector
for each of the 576 states \(q\in Q\).
There is one vertex for each right
\(\langle s\rangle\)-coset and one for
each right \(\langle r\rangle\)-coset.
The latter identifications use the actual
factor \(\zeta_3^{\ell(qv_*)}\) when the
edge is multiplied on the right by \(r\).
This is obtained by projecting the literal
edge \((0,q)r=(qv_*,qR)\) onto its
character. The boundary map is onto,
because the character is nontrivial.
Consequently its cycle module has rank
\(576-288-192=96\) over \(\mathcal O\).
The corresponding target has
\(48-24-16=8\) cycles. On edges the
projection is simply \(e_q\mapsto e_{q_*}\),
with the same character phase.

The program \texttt{d\_arithmetic\_A4\_twisted.py}
uses exactly these edge and vertex maps over
\(\mathbb F_4=\mathbb F_2[\zeta_3]\).
It retains both complete cycle bases and
the actual onto matrix of rank eight.
For a pair-stabilizer element the action
is left translation of the edges. If it
exchanges \(\ell\) and \(-\ell\), the
coefficient map also applies the Frobenius
of \(\mathbb F_4/\mathbb F_2\).
All such semilinear matrices are retained.
The forty pairs give the orbit sizes
\(8,12,12,8\) in (D.60.3).

The cusp has order 12 in both finite bases.
The program expands the actual word
\(t^{12}\) and all its marked conjugates.
Their ranks in these character components
are 48 and four, and the projection of
the first cusp module onto the second has
rank four. Their compact quotients have
ranks 48 and four. Integrally the cusp
modules are primitive submodules of the
surface homology; the maps are onto
because the cusp widths agree. The map
from the full arithmetic cover sends
\([t^{36}]\) to \(3[t^{12}]\), which
has an invertible factor over \(\mathbb Z_2\).
Thus these are also the actual integral
cusp and compactification maps in (D.60.4).

\emph{The entire residual block and its norm kernel.}
For each unordered character pair the
\(\Delta\)-invariant exterior module is
the space of Hermitian \(96\)-by-\(96\)
matrices over \(\mathbb F_4\), of dimension
\(96^2\) over \(\mathbb F_2\). The basis
is the one in (D.59.17): a diagonal
coefficient lies in \(\mathbb F_2\), and
an off-diagonal coefficient lies in
\(\mathbb F_4\), with its conjugate in
the transposed position. A homology map
\(M\) acts by
\(H\mapsto MH\overline M^{\,T}\), with
coefficient conjugation as well when the
character pair is exchanged. The small
projection has this same formula with
the literal eight-by-96 matrix. It is
onto its 64-dimensional target.

For each of the four representatives the
program exhibits eight actual free
\(\mathbb F_4[A_4]\)-generators of the
96-dimensional cycle space. It checks all
twelve left permutations on the resulting
basis. In that basis the Hermitian
coinvariants under \(A_4\) have dimension
768: their orbit coordinates consist of
eight diagonal coordinates, 24 trace
coordinates for pairs with a swapping
stabilizer, and 368 two-dimensional
\(\mathbb F_4\)-coordinates. The exact
\(A_4\)-norm has rank 768.

The target is trivial under \(A_4\).
Moreover \(A_4^{\rm ab}=C_3\), so
\(H_1(A_4,\mathbb F_2)=0\). The
coinvariant sequence for the actual
exterior kernel is consequently exact
on the left as well as on the right:
\[
 0\longrightarrow (\ker\theta_Z)_{A_4}
   \longrightarrow C_{A_4}
   \longrightarrow C_*\longrightarrow0
 \quad\text{on each chosen pair}.
 \tag{D.60.11}
\]
Here \(C\) is its 9216-dimensional
Hermitian source. Thus the first module
in (D.60.11) has dimension \(768-64=704\).
The remaining stabilizer quotient has
order six or four. The program
\texttt{d\_arithmetic\_A4\_central.py}
retains its action on all 768 coordinates,
the complete 704-dimensional kernel basis,
and all quotient multiplication checks.
Taking its actual augmentation quotient
and actual norm gives (D.60.3).
For the compact norm the program quotients
by the stored 48 cusp columns before
taking the exterior map. These are the
maps whose ranks are in the final column.
In particular the sum of the exact
residual coinvariant dimensions is 640;
the compact norm kernel is \(640-138=502\).
No boundary value is set to zero in this
calculation.

\emph{The stabilizers and their projective compact summands.}
We now use precisely the two orbits of
size eight. For either representative let
\(H_0\) fix its oriented character and
let \(H\) fix its unordered pair.
The actual multiplication table gives
\[
 H_0=V_4\rtimes C_3^2,\qquad
 H=H_0\times\langle\sigma\rangle,
 \quad\sigma=5I,\qquad |H_0|=36,
 \tag{D.60.12}
\]
where \(\sigma\) exchanges the two
characters. In the 576-state marking
the subgroup \(V_4\) consists of states
\(0,572,574,575\), the complement is
generated by the commuting order-three
states 8 and 136, and \(\sigma\) is
state 573. The certificate checks their
orders, all required products, generation,
and the semilinear actions. The normal
subgroup \(A_4\) has index three in
\(H_0\).

Write \(S_\ell\) for the 96-dimensional
affine component, \(R_\ell\) for its
48-dimensional cusp component, and
\(P_\ell=S_\ell/R_\ell\).
The exact regular basis just constructed
shows that \(\bar S_\ell\) is free of
rank eight over \(\mathbb F_4[A_4]\).
The cusp module is free of rank four:
\(A_4\) acts freely on the 48 cusp
cosets, since its intersection with
every conjugate cusp stabilizer is
trivial. This last assertion follows
from equality of the cusp orders in
the two actual quotient bases.
Induction and the relative trace, with
the odd index three invertible, make
both modules projective over
\(\mathbb F_4[H_0]\). The cusp module
is also injective, since a finite group
algebra over a field is self-injective:
its regular module is its own linear
dual by the coefficient-of-one pairing.
The exact affine-to-compact sequence
therefore splits, and \(\bar P_\ell\)
is projective too.

The order-two action in (D.60.12) must
remain in this argument. It is genuinely
semilinear over \(\mathbb F_4\), and it
commutes with \(H_0\). Galois descent
writes each such module as
\(\mathbb F_4\otimes_{\mathbb F_2}M_0\),
with \(H_0\) acting on \(M_0\) and
\(\sigma\) acting on the first factor.
The normal basis \(\zeta_3,\zeta_3^2\)
identifies this first factor with the
regular \(\mathbb F_2[C_2]\)-module.
The descended \(M_0\) is projective
over \(\mathbb F_2[H_0]\): it is a
direct summand after restriction of
scalars of the projective module, using
any trace-one coefficient for the
retraction. The real pair module is
therefore projective over
\(\mathbb F_2[H]\). Induction along
the eight pair cosets proves projectivity
of the corresponding global \(G\)-modules.
For the intervening character subgroup
\(A_*\rtimes H\), restriction to \(H\)
detects projectivity: its index is odd,
and the relative averaging map splits
the induction--restriction counit.
The odd kernel in (D.60.2) causes no
loss: its averaging idempotent identifies
the inflated group algebra block with
the quotient group algebra.

All these assertions lift integrally.
A finite free \(\mathbb Z_2\)-lattice
whose reduction is projective over the
finite group algebra is projective over
\(\mathbb Z_2[G]\). Indeed lift its
matrix idempotent through successive
powers of two, map the resulting
projective lattice onto the given one
using its reduction isomorphism, and
apply Nakayama. Equal \(\mathbb Z_2\)
ranks make that map an isomorphism.
This also proves the assertion over
\(\mathcal O\); its unramified descent
and normal basis have the same integral
description. The source affine, cusp,
and compact lattices on these two
orbits are thus projective.
The target lattices are projective
over \(\mathbb Z_2[G_*]\) as well:
their oriented stabilizer is
\(H_0/A_4=C_3\), with the same
semilinear central exchange.

\emph{Literal projective-cover matrices and integral embeddings.}
Because \(V_4\) is a normal Sylow
two-subgroup of \(H_0\), its coinvariant
top is a module for \(C_3^2\).
It has dimension twelve on the compact
source and dimension four on the target.
The target is already trivial on
\(A_4\). The program
\texttt{d\_arithmetic\_A4\_projective.py}
uses the nine character projectors of
the displayed \(C_3^2\) complement.
For clarity, these are literally
\[
 p_{a,b}=\sum_{0\leq i,j<3}
           \zeta_3^{-ai-bj}M_{g^i h^j}
              \quad\text{over }\mathbb F_4;
 \tag{D.60.13}
\]
the omitted factor \(1/9\) equals one
in this coefficient field.
For \((0,0,0,1)\) the extra top consists
of three copies of the pair of weights
\((0,1),(0,2)\), and one copy of
\((1,0),(2,0)\). For \((0,1,0,0)\)
it consists of two copies of
\((0,1),(0,2)\) and two copies of
\((1,1),(2,2)\).
Each chosen weight vector, with its
four \(V_4\)-translates, is an actual
projective generator of dimension four.
Pairing it with its literal
\(\sigma\)-image gives dimension eight.

The resulting compact matrix is an
invertible 48-by-48 matrix, partitioned
into four blocks of width eight and
one final block of width sixteen.
The latter block \(P_0\) maps onto
the four-dimensional target and is
its projective cover. The four other
blocks map to zero. The program
lifts each of their generators to
affine homology by solving both the
compact and small-projection equations,
then applying (D.60.13) and the actual
semilinear exchange. It checks every
stabilizer action on those lifts.
Thus it constructs the finite
idempotents in (D.60.4), not just
their isomorphism types.
The program
\texttt{d\_arithmetic\_A4\_cross\_completion.py}
checks the individual four width-eight
blocks and every generator product
on them with its correct field action.

Here is an integral construction that
retains these exact finite matrices.
In the integral compact module lift
the five orthogonal idempotents.
This is possible because the reduction
map on its equivariant endomorphisms
is onto, by projectivity, and its
kernel consists of multiples of two.
The lift of \(P_0\) still maps onto
the target. For any other lifted
summand \(E\), lift its small-image
map through \(P_0\), and subtract
that lift from its embedding. Since
the small image of \(E\) was zero
modulo two, the subtraction can be
chosen divisible by two. This changes
neither the recorded finite matrix
nor the direct sum and makes
\(\theta E=0\) integrally.

Split the integral affine-to-compact
sequence using projectivity of the
compact module. Its reduction can
be prescribed to equal the recorded
affine embeddings on the four extra
summands: extend them on the
projective complement, lift the
resulting map, and invert its compact
composite, which is identity modulo
two. The map from source cusp
homology to target cusp homology
is onto. Adjusting this section
by a cusp-valued map therefore
makes it commute with a chosen
target section. The adjustment
vanishes modulo two on the four
extra summands, since their recorded
small images were zero. Its values
there can be chosen to cancel their
entire integral small images.
The resulting affine embeddings
have zero small image, give the
specified finite matrices, and
annihilate the cusp module under
the associated projections.
This proves (D.60.4) with integral
maps. Induction from each chosen
pair supplies the global
\(e_{a,i}\) and their rank 128.

\emph{An integral homology replacement with the exact small action.}
Let \(e_\Sigma\) be the central
integral character idempotent of
these two unordered orbits, and
put \(S=e_\Sigma U\). Its source
and target splittings just proved
have the form
\[
 \begin{aligned}
 S&=R\oplus\bigoplus_{a,i}E_{a,i}\oplus P_0,\\
 S_*&=R_*\oplus P_*,\qquad
 \theta|_{P_0}=\theta_0:P_0\twoheadrightarrow P_*.
 \end{aligned}
 \tag{D.60.14}
\]
Here the two orbit summands of
\(P_0\) and \(P_*\) are grouped
in the notation. The map sends
\(R\) onto \(R_*\), kills every
\(E_{a,i}\), and respects the
two displayed splittings.

Let \(T_*\) be the actual full
integral D.57 homology action.
It fixes \(R_*\) pointwise,
since it fixes the cusp and is
identity on the finite deck group.
In (D.60.14) write it as
\(\left(\begin{smallmatrix}1&B_*\\0&C_*\end{smallmatrix}\right)\).
Projectivity of \(P_0\) gives
equivariant lifts
\[
 \theta_0 C_0=C_*\theta_0,
 \qquad \theta_R B_0=B_*\theta_0,
 \quad C_0:P_0\to P_0,
 \quad B_0:P_0\to R.
 \tag{D.60.15}
\]
The endomorphism \(C_0\) is
invertible. Modulo two,
\(\theta_0\) is a projective
cover: its kernel is the
\(V_4\)-augmentation radical
of \(P_0\), as is also seen
from the literal top dimensions
and weight maps above. A lift
of an automorphism of its
quotient is consequently an
automorphism by Nakayama.
An integral matrix invertible
modulo two is invertible over
\(\mathbb Z_2\).

Define \(T_{60}\) on \(S\)
by identity on \(R\) and
all the \(E_{a,i}\), and by
\(v\mapsto B_0v+C_0v\)
on \(P_0\). On the complement
of \(S\), keep the chosen
D.59 homology action \(T_{59}\).
Then
\[
 \theta_U T_{60}=T_*\theta_U,
 \qquad T_{60}e_{a,i}=e_{a,i}T_{60}=e_{a,i},
 \qquad
 (T_{60}-T_{59})\mathcal R=0.
 \tag{D.60.16}
\]
It is an integral automorphism.
Its difference from \(T_{59}\)
has image in the actual saturated
kernel \(L=e_\Sigma\ker(U^-\to U_*^-)\).
Every character in this block
is active on \(A\), because
\(A\to A_*\) is onto.
Thus \(e_A L=0\).

\emph{The homology replacement is an actual peripheral source map.}
We give the local argument for
\(L\), rather than assuming
that projectivity of its ambient
module suffices. The exact
sequence
\[
                 0\longrightarrow L\longrightarrow S
                   \longrightarrow S_*\longrightarrow0
 \tag{D.60.17}
\]
is a sequence of integral lattices.
The source is projective over
\(\mathbb Z_2[G]\), and the
target is projective over
\(\mathbb Z_2[G_*]\), as proved
above. On the three cyclic
subgroups generated by \(s,r,t\)
the maps of their finite images
have orders
\[
                  2\to2,\qquad3\to3,\qquad36\to12.
 \tag{D.60.18}
\]
Their kernels are trivial or odd.
Inflating a projective lattice
across these odd kernels remains
projective, by the averaging
idempotent. Hence (D.60.17)
splits over each of these three
cyclic groups, and \(L\)
restricts projectively to each.
In particular their first
cohomology with these coefficients
vanishes and their cyclic norm
sequences are exact.

Odd averaging on the normal
subgroup \(A\) gives
\(H^j(G,L)=0\) for every
\(j\geq0\). Inflation--restriction
therefore gives the actual map
\[
 H^1(\widehat B,L)
   \xrightarrow{\ \sim\ }
                       \operatorname{Hom}_G(U,L).
 \tag{D.60.19}
\]
Use it for \(T_{60}-T_{59}\).
A representing continuous derivation
\(\delta\) is a coboundary
on \(\langle s\rangle\)
and \(\langle r\rangle\)
by the just-proved local
projectivity. Also
\(\delta(t^{36})=0\): its
restriction is the prescribed
homology difference and that
difference kills the cusp module.
Thus its restriction to the
procyclic cusp factors through
the finite order-36 image.
Projectivity there supplies
\(b_t\in L\) with
\(\delta(t)=(1-t)b_t\).
Subtract the inner derivation
\((1-g)b_t\). The resulting
derivation has the same homology
restriction and satisfies
\[
 \delta(s)=(1-s)b_s,
 \qquad\delta(r)=(1-r)b_r,
 \qquad\delta(t)=0,
 \qquad b_s,b_r\in L.
 \tag{D.60.20}
\]
These are exact continuous
semidirect-product equations.
They give actual left changes
to the two source conjugators.
Both changes lie in
\(L\subset\ker(Y\to X_*)\),
so their exact elements in the
D.57 source are unchanged.
The map on \(Y\) has the
invertible kernel map induced
by \(T_{60}\) and the retained
automorphism on \(X_*\).
It is therefore an automorphism.
Equivalently its maps to the
full homology source and to
\(X_*\) agree on the same
marked common quotient of
D.58; their fibre product is
the source \(Y\) in (D.60.1).
This proves the actual integral
peripheral replacement before
using a central obstruction.

\emph{The twelve cross norms and the actual central lift.}
The four rank-eight summands in
one oriented character component
give six cross modules. Each
has a matrix coordinate
\(X\in\operatorname{Mat}_8(\mathbb F_4)\),
of dimension 128 over
\(\mathbb F_2\). A stabilizer
element acts as
\[
 X\longmapsto M_i(g)X\overline{M_j(g)}^{\,T},
 \tag{D.60.21}
\]
with \(X\) conjugated as well
when \(g\) exchanges the
character pair.

The program
\texttt{d\_arithmetic\_A4\_cross\_completion.py}
retains every norm column for
all twelve such modules and
checks all semilinear generator
products. In the order
\((12),(13),(14),(23),(24),(34)\)
their coinvariant dimensions
and norm ranks are, respectively,
\[
 \begin{array}{c|rrrrrr|r}
  (0,0,0,1)&4&4&0&4&0&0&12\\
  (0,1,0,0)&4&2&2&2&2&4&16.
 \end{array}
 \tag{D.60.22}
\]
The equality of each norm rank
with its coinvariant dimension
proves injectivity. Surjectivity
onto invariants follows as well:
these cross modules are projective.
For example each factor is a
projective \(\mathbb F_4[H_0]\)
module; the diagonal tensor of
a projective module with any
module is projective, by the
map \(g\otimes v\mapsto
g\otimes g^{-1}v\) on a
regular tensor. The exchange
acts semilinearly on this
cross coordinate, so the
normal-basis descent used above
also gives projectivity over
\(\mathbb F_2[H]\).
The usual regular-module norm
is an isomorphism from
coinvariants to invariants,
and direct summands retain it.

Induction over the eight pair
cosets multiplies each central
dimension by eight and identifies
its \(Q\)-coinvariants and
invariants with those computed
at the stabilizer. The full
\(G\)-norm has the same map:
\(\Delta\) acts trivially on
the invariant exterior module
and has odd order. The total
dimension is therefore
\(2\cdot6\cdot8\cdot128=12288\),
and the coinvariant dimension
is \(12+16=28\). This proves
the norm assertions of (D.60.6)
with their literal action maps.

The affine projectors kill
the cusp module and so induce
projectors on compact homology.
Their summed images inject
under compactification by
(D.60.4). Consequently the
exterior compactification map
is injective on \(\mathcal C_{60}\).
It is in \(\ker\theta_Z\),
because every chosen homology
summand has zero small image.
All its characters are active
on \(A\), so it lies in the
actual module \(Z=W\wedge V\).
They are trivial on every
cusp class of \(N\), whereas
the D.59 characters are
nontrivial on all those classes.
The two Fourier projectors
are therefore orthogonal.
This proves all submodule and
idempotent assertions in
(D.60.5)--(D.60.6).

Lift the repaired \(Y\)
conjugators to the full source
\(X\). Their cusp error is
an actual \(z\in\mathcal K\).
Apply D.55's exact, unquotiented
orientation identity, and
project onto the compact
exterior image of \(\Pi_{60}\).
By (D.60.16), the homology
action commutes with its
projectors and is identity
on all their images. The
projected right hand side is
therefore zero. The left hand
side is exactly
\[
            (\bigwedge^2\pi)\nu([\Pi_{60}z]).
 \tag{D.60.23}
\]
Both maps in this composition
are injective on the indicated
module, as just proved. Thus
\([\Pi_{60}z]=0\) in
\((\mathcal C_{60})_G\).
This proves zero of these
actual arithmetic boundary
coordinates without choosing
an unknown arithmetic matrix.

The same argument of D.59
still applies to \(\mathcal C_{59}\),
because its homology support
and action were unchanged.
The component
\((1-e_\Delta)\mathcal K\)
has zero coinvariants by
odd averaging. In each of
these three retained modules
the error is consequently in
its exact augmentation image
\((1-s)M+s(1-r)M\).
Actual central changes to
the two conjugators kill it,
preserving their projection
to \(Y\) and to \(X_*\).
The remaining cusp error is
in \(\mathcal J_{60}\).

The homology map commutes
with every displayed projector
and preserves \(\ker\theta_Z\)
under its exterior square.
It therefore preserves
\(\mathcal J_{60}\).
The corrected source map
descends to
\(\mathcal T_2/\mathcal J_{60}\),
since it sends \(K_3\) into
a class-two exponent-four
kernel and kills the defining
relations of \(L_2\).
It is an automorphism there
by its invertible Frattini map
and identity map on \(G\).
Its map to the full homology
source with the prescribed
\(\mathcal W_h\) component
agrees on the actual common
quotient. The fibre product,
using the original source
kernels, is exactly
\(X/\mathcal J_{60}\).
This proves (D.60.7), including
the compatible conjugators.

\emph{Exact kernels and the surviving obstruction.}
The mutually orthogonal
central projectors give
\[
 \mathcal K=(1-e_\Delta)\mathcal K
       \oplus\mathcal C_{59}
       \oplus\mathcal C_{60}
       \oplus\mathcal J_{60}.
 \tag{D.60.24}
\]
All comparison kernels in
(D.60.8) follow from this
actual direct sum and the
same source quotient maps.
The new automorphism preserves
\(\mathcal C_{60}\), so it
descends to \(X_{59}\), with
the changed homology matrix
explicitly described above.
The parameter and CM maps
are retained through the
unchanged \(\mathcal W_h\)
projection throughout the
construction.

The character block
\(\mathcal D\) of (D.60.3)
is an equivariant direct
summand of \(\mathcal K_\Delta\).
Inside it the projector
\(\Pi_{60}\) gives
\(\mathcal D=\mathcal C_{60}
\oplus(1-\Pi_{60})\mathcal D\).
Dimensions and coinvariants
therefore subtract exactly:
\[
 \dim(1-\Pi_{60})\mathcal D=366080-12288=353792,
 \qquad
 \dim\bigl((1-\Pi_{60})\mathcal D\bigr)_G=640-28=612.
 \tag{D.60.25}
\]
This is an actual submodule
of \(\mathcal J_{60}\).
For a source element detecting
the remaining kernel, take
a nonzero vector in this
specified submodule and an
actual preimage under the
onto map \(R_{50}\to Z\)
proved in D.51. Its image
in \(X\) is that vector,
and its image in \(X_{60}\)
is one. The preimage formula
(D.60.9) is therefore exact
and its kernel is nonzero.
The surviving boundary is
the class of the remaining
literal cusp error in
\((\mathcal J_{60})_G\);
the present argument evaluates
only the twenty-eight new
coordinates whose injections
were proved above.
\end{proof}

\end{document}

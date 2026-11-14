\subsection{Marked compact isometries and fourteen further arithmetic boundary coordinates}

\begin{statement}{D.64}{Proved}{A compact isometry correction and actual source involutions lift a further 1930-dimensional layer}
Use the actual groups, lattices, compact projectors and maps of D.63:
\[
 X=\widehat B/(R_{50}\cap L_2),\qquad
 Y=X/\mathcal K,\qquad X_{63}=X/\mathcal J_{63},\qquad
 \mathcal L=\ker(U^-\longrightarrow U_*^-).
 \tag{D.64.1}
\]
Number the four character-pair orbits by
\(\ell_1=(0,0,0,1),\ell_2=(0,0,1,1),
\ell_3=(0,0,1,2),\ell_4=(0,1,0,0)\).
Their sizes are \(8,12,12,8\).
The compact orthogonal decomposition is
\(P_a=\widetilde E_a\perp M_a\), with fibre ranks
32 and 16 over the unramified quadratic coefficient ring.
Let
\[
 \phi_a:\overline M_a\longrightarrow \overline P_{*,a},
 \qquad
 K_a=\ker\bigl(\operatorname{Herm}(\phi_a):
       \operatorname{Herm}_{16}(\mathbb F_4)
       \longrightarrow\operatorname{Herm}_{4}(\mathbb F_4)\bigr).
 \tag{D.64.2}
\]
Bars on lattices denote reduction modulo two;
on a field coefficient they denote its square.
Here \(\operatorname{Herm}(\phi)(B)=\phi B\bar\phi^{\,t}\).
The actual semilinear pair stabilizer is \(H_a\leq Q\).
Put \(C_a=\operatorname{Ind}_{H_a}^{Q}K_a\), with the
inflated action of the full arithmetic group \(G\).
There are actual onto maps
\[
             q_a:\mathcal J_{63}\longrightarrow C_a
 \tag{D.64.3}
\]
given by compactification and the \(M_a\)-self projection.
Their joint map is onto. Their dimensions and full group norms are
\[
 \begin{array}{c|r|r|r|r}
 a&\dim C_a&\dim(C_a)_G&\operatorname{rank}\nu_a
                      &\dim\ker\nu_a\text{ on coinvariants}\\\hline
 1&1920&4&4&0\\
 2&2880&10&0&10\\
 3&2880&10&0&10\\
 4&1920&4&2&2
 \end{array}
 \tag{D.64.4}
\]
The norm is \(\nu_a(v)=\sum_{g\in G}gv\), viewed either
on \(C_a\) or on its coinvariants as indicated.

For both actual D.57 arithmetic branches, the two old
projective modules \(M_1,M_4\) have explicit equivariant
modulo-two isometries \(X_a\) satisfying
\[
 \phi_aX_a=T_{*,a}\phi_a,\qquad
 X_a^t H_a^{\rm int}\bar X_a=H_a^{\rm int},
 \qquad\det X_a\ne0.
 \tag{D.64.5}
\]
The matrix \(H_a^{\rm int}\) is the reduction of the
actual compact intersection form, computed from marked
integral cycle lifts. The superscript distinguishes this
matrix from the stabilizer group \(H_a\).
The complete affine parameter spaces and all their quadratic
isometry equations are retained in the certificate. Their
dimensions are eight and six, respectively. The two
eight-parameter solutions use masks \(\mathtt{c3},0\)
for branches one and three; both six-parameter solutions
use mask zero. The fixed-seed search trial counts are
\(62,1,1,1\). All sixteen D.57 framing choices are retained.

For \(a=2,3\), let \(I_a\subset(C_a)_G\) be the
four-dimensional image of the actual source-involution map
\[
       v\longmapsto[e_\Delta(v\wedge sv)]_G,
       \qquad v\in\ker\phi_a
       \text{ and its induced coset copies}.
 \tag{D.64.6}
\]
There are explicit retractions
\(p_a:(C_a)_G\to I_a\) that intertwine every equivariant
compact homology action with either of the two actual
D.57 small actions. Thus their kernels are invariant
under the actual retained homology action.
Define the onto equivariant map
\[
 \begin{aligned}
 \Phi_{64}:\mathcal J_{63}&\longrightarrow
       \mathcal E_{64}=C_1\oplus I_2\oplus I_3\oplus\nu_4(C_4),\\
 z&\longmapsto
    \bigl(q_1z,\ p_2[q_2z],\ p_3[q_3z],\ \nu_4q_4z\bigr),\\
 \mathcal J_{64}&=\ker\Phi_{64},\qquad X_{64}=X/\mathcal J_{64}.
 \end{aligned}
 \tag{D.64.7}
\]
The last three summands of \(\mathcal E_{64}\) have trivial
\(G\)-action. The first has the induced action specified
in (D.64.2)--(D.64.3). In particular
\[
 \dim\mathcal E_{64}=1930,\qquad
 \dim(\mathcal E_{64})_G=14,
 \qquad
 \ker(X_{64}\longrightarrow X_{63})=\mathcal E_{64}.
 \tag{D.64.8}
\]

There is an actual continuous peripheral automorphism
\(\alpha_{64}\) of \(X_{64}\), of multiplier one,
fixing the original cusp \(t\) and inducing identity
on \(G\). It retains the complete D.57 action and its
literal compatible conjugators, the full \(\mathcal W_h\)
action, and every established metabelian and CM comparison
through that map. Its projection to \(X_{63}\) is a
new representative, with the following exact comparison
on \(Y\). Write \(T_{63}\) for D.63's integral homology
action. There are integral equivariant maps
\(A_a:M_a\to\mathcal L\), for \(a=1,4\), and continuous
projective coefficient derivations \(\eta_a:Y\to M_a\),
with \(\eta_a|_U=m_a\) and \(\eta_a(t)=0\), such that
\[
 \begin{aligned}
 T_{64}&=T_{63}+A_1m_1+A_4m_4,\\
 \beta_Y(g)&=\bigl(A_1\eta_1(g)+A_4\eta_4(g)\bigr)
                                        \alpha_{63,Y}(g),\\
 \alpha_{64,Y}&=\operatorname{Int}(b_{t,Y})\beta_Y,
 \qquad
 b_t=\prod_j\prod_{k=0}^{35}t^ku_jt^{-k},\quad u_j\in S_{57}.
 \end{aligned}
 \tag{D.64.9}
\]
The reductions of the compact restrictions of \(T_{64}\)
are the isometries \(X_1,X_4\). Integral invertibility
and equivariance are proved; no equality of integral
intersection forms is asserted. The vectors used in
\(b_t\) are the earlier \(\widetilde E\)-self corrections.
The eight new corrections in (D.64.6) centralize the
source involution on \(Y\), so they cause no additional
change in (D.64.9).

The complete remaining source kernels are
\[
 \begin{aligned}
 \ker(X\to X_{64})&=\mathcal J_{64},\qquad
 \ker(X_{64}\to Y)=\mathcal K/\mathcal J_{64},\\
 \dim\mathcal J_{64}&=\dim\mathcal J_{63}-1930,\\
 \dim(\mathcal J_{64})_{\text{specified small characters}}
                                      &=282230,\\
 S_{64}&=\{b\in R_{50}:
        \operatorname{im}_{\mathcal T_2}(b)\in\mathcal J_{64}\},\\
 S_{64}/(R_{50}\cap L_2)&=\mathcal J_{64}.
 \end{aligned}
 \tag{D.64.10}
\]
This is a proper, nonzero remaining source kernel.
The tested involution and full-cusp maps on the entire
compact kernel have combined rank eight in its
22-dimensional norm kernel. Fourteen coordinates of
that particular coinvariant test remain. This count
is not used as a coinvariant-dimension formula for
\(\mathcal J_{64}\). The remaining arithmetic boundary
and the full profinite realization are unresolved.
The manuscript passages are Part D(e), section 51.16,
folio 734 verso, scan 174, and section 51.15,
folios 725--727, scans 156--160.
\end{statement}
\begin{proof}
\emph{The actual compact maps and the residual quotient.}
Use the four compact decompositions of D.63, including
their proved graph maps to the earlier markings.
The affine cusp lattice is \(\mathcal R\), and
\(\pi:U\to P=U/\mathcal R\) is compactification.
The small maps \(\theta_U,\theta_P\) fit into the two
actual exact sequences of cusp and compact homology.
The source cusp has width 36 and its small image has
width 12. Thus an oriented boundary loop maps to
three times its small boundary loop. Every small
cusp has a preimage, and three is a unit in
\(\mathbb Z_2\). It follows, with the single sum
relation retained, that
\[
 \theta_{\mathcal R}:\mathcal R\twoheadrightarrow\mathcal R_*,
 \qquad
 \mathcal L\twoheadrightarrow\ker\theta_P.
 \tag{D.64.11}
\]
The first integral homology map is onto by D.58.2;
the second assertion is the resulting kernel map
in the exact-sequence diagram. All these kernels
are saturated. Their reductions are therefore the
kernels of the reduced maps. The same statements
hold on the selected odd-character parts.

On an unordered nonzero character pair, odd averaging
identifies the self exterior module with Hermitian
matrices over \(\mathbb F_4\). In the basis
\(u_i,\omega u_i\) the diagonal coordinate is
\(u_i\wedge\omega u_i\); the two off-diagonal coordinates
are
\[
 \begin{aligned}
 H_{ij}=1&:\quad
 u_i\wedge\omega u_j+\omega u_i\wedge u_j,\\
 H_{ij}=\omega&:\quad
 u_i\wedge u_j+\omega u_i\wedge u_j
                              +\omega u_i\wedge\omega u_j.
 \end{aligned}
 \tag{D.64.12}
\]
The actual induced exterior map is consequently
\(B\mapsto\phi_aB\bar\phi_a^{\,t}\). Each
\(\phi_a\) has rank four, so this Hermitian map
has rank 16 and kernel dimension 240 over
\(\mathbb F_2\). Equivariant induction multiplies
this dimension by the corresponding orbit size.

Compactification of a vector of \(\mathcal J_{63}\)
has zero small image. Its remaining compact self
part is in the four \(M_a\)-blocks, hence gives
(D.64.3). To prove onto, start with any vector of
\(K_a\) and lift it into the \(M_a\)-self block of
the full central module. Its small affine image
has zero compact image, hence is in
\(\mathcal R_*\wedge\overline U_*\).
Both maps in (D.64.11) and \(\theta_U\) are onto,
so subtract a lift in
\(\overline{\mathcal R}\wedge\overline U\).
Every selected compact projector kills this lift.
Odd averaging and the character projector retain
the chosen orbit. The result lies in
\(\mathcal J_{63}\), with the prescribed compact
self coordinate. The same construction independently
on the four orbits proves joint surjectivity.

The program \path{d_residual_compact_norm.py}
computes each complete semilinear action on the
256-dimensional Hermitian module. It restricts
the action to the actual 240-dimensional kernel,
forms all relations \((g-1)K_a\), and sums every
stabilizer action. It checks that this sum kills
all relations and has invariant image.
Coinvariants and invariants of the induced module
are identified with those of this fibre by the
literal chosen coset representatives. Under these
identifications the group norm is the stabilizer
norm. The translation subgroup and the remaining
odd kernel have odd order and act trivially on
the averaged self module, so their norm factors
are one modulo two. These exact maps give
(D.64.4), including all four small comparison maps.

\emph{The integral ribbon pairing and its arithmetic marking.}
Let \(\mathcal O/4=\mathbb Z_2[\omega]/4\), with
\(\omega^2+\omega+1=0\). The graph has the actual
edges indexed by \(Q\), with the two vertex sets
\(Q/\langle s\rangle\) and \(Q/\langle r\rangle\).
The cyclic order at the latter is \(g,gr,gr^2\).
For the character \(\ell\), put
\(k_g=\ell(Q_gv_r)\) in \(\mathbb F_3\).
The twisted incidence matrix uses coefficient one
at the two-valent vertex and the consecutive
coefficients \(1,\omega^{-k_g},\ldots\) at a
three-valent vertex. These are the same edge and
vertex maps as D.60, now calculated modulo four.

Let \(U_0\) be the retained modulo-two cycle matrix,
and \(\widetilde U_0\) its coefficientwise lift to
\(\mathcal O/4\). The incidence map is onto on
this nontrivial character part. Solve
\[
 B_2D=\tfrac12 B_4\widetilde U_0,
 \qquad U_4=\widetilde U_0+2\widetilde D.
 \tag{D.64.13}
\]
The certificate verifies \(B_4U_4=0\) and
\(U_4\bmod2=U_0\). These cycles lift to actual
integral cycles: the incidence cokernel vanishes,
and the same correction solves the successive
integral equations. The computation never divides
a non-even coefficient by two.

For two integral cycles \(u,v\), the signed
half-ribbon formula, in these vertex markings, is
\[
 h(u,v)=\frac12\sum_{g\in Q/\langle r\rangle}
 \left(u_g\omega^{k_g}\bar v_{gr}
          -u_{gr}\omega^{-k_g}\bar v_g\right).
 \tag{D.64.14}
\]
Indeed displace one cycle to the two sides of the
oriented ribbon. At a three-valent vertex the
difference of the two crossing counts is the
displayed determinant; the sum-zero condition
eliminates the third edge. A two-valent vertex
contributes zero. Averaging the two signed counts
gives (D.64.14). The crossing number is integral,
so the displayed numerator is even. This proves
that the formula computes the actual intersection
pairing. Its reduction depends only on the cycle
coordinates modulo four. The Fourier sum over
the 81 translations multiplies this expression
by 81, which is one modulo four.

The odd quotient from \(G\) to \(G^\dagger\) has
degree \(d=3^{93}\). The actual pushforward and
transfer obey \(\theta\operatorname{tr}=d\), and
\[
 \langle d^{-1}\operatorname{tr}u,
         d^{-1}\operatorname{tr}v\rangle_G
              =d^{-1}\langle u,v\rangle_{G^\dagger}.
 \tag{D.64.15}
\]
This is the normalized transfer identification
used on the selected character lattice.
Its factor is one modulo two. Thus the finite
marked calculation is also the reduction of the
actual arithmetic intersection form on these
summands, with the specified map.

The program \path{d_residual_compact_pairing.py}
implements (D.64.13)--(D.64.14). Its affine pairing
has rank 48 on each 96-dimensional fibre and
kills exactly the 48-dimensional cusp subspace.
The small affine pairing has rank four on its
eight-dimensional fibre. The actual inclusion
of that fibre in D.57's complete 649-dimensional
marked cycle space satisfies
\[
                   E^t\Omega_{649}\bar E=h_*.
 \tag{D.64.16}
\]
Every entry is checked. On each \(M_a\) the
induced form has rank 16. Its restriction to
\(\ker\phi_a\) has rank eight and radical rank
four. The adjoint
\(\bar{(H_a^{\rm int})^{-1}\phi_a^tH_{*,a}^{\rm int}}\)
has rank four and is killed by \(\phi_a\).
All semilinear stabilizer maps preserve the
actual form, with coefficient conjugation on
character-exchanging elements.

Finally, applying each complete D.57 homology
matrix to \(E\) gives the actual small affine
action and its compact quotient \(T_{*,a}\).
The extension certificate verifies that all
eight framings in each branch have identical
complete homology matrices. Both branches are
therefore compared through their actual marked
maps in (D.64.16), without choosing an unrelated
symplectic model.

\emph{The complete isometry equations.}
For \(a=1,4\), the unknown matrix \(X\) has
512 binary entries. If \(A_g\) is a stabilizer
matrix and \(\epsilon_g\) records character
exchange, its exact equations are
\[
 A_g\overline X^{\,\epsilon_g}=XA_g,
 \qquad \phi_aX=T_{*,a}\phi_a,
 \tag{D.64.17}
\]
where \(\overline X^{\,0}=X\) and
\(\overline X^{\,1}=\bar X\).
The linear ranks are 504 and 506. The certificate
retains a particular solution \(X_0\) and every
homogeneous basis matrix \(D_i\), so all solutions
are exactly \(X_0+\sum_i e_iD_i\), \(e_i\in\mathbb F_2\).
Substitution into the isometry equation gives
the complete vector polynomial
\[
 c+\sum_i l_i e_i+\sum_{i<j}q_{ij}e_ie_j=0
       \quad\text{in }\operatorname{Herm}_{16}(\mathbb F_4).
 \tag{D.64.18}
\]
Every coefficient, including every zero coefficient,
is retained. Their spans have dimensions four
and two. The masks and trial counts in the
statement give literal zeros. Direct multiplication
then checks all 72 stabilizer equations, rank 16,
the marked small square, and the entire isometry
matrix. No sampling assertion is used to certify
these four solutions.

\emph{The integral correction and its actual source maps.}
The old \(M_1,M_4\) lattices are projective by
D.60 and remain the same lattices in D.63's
orthogonal graph decomposition. Write \(D_a\)
for the existing compact restriction of \(T_{63}\)
to \(M_a\). Both \(\bar D_a\) and the chosen
\(X_a\) satisfy the same small square, so
\[
          X_a-\bar D_a:\overline M_a
                         \longrightarrow\ker\bar\theta_P
 \tag{D.64.19}
\]
is an actual equivariant map. Projectivity lifts
it to an integral map through (D.64.11). Reduction
is onto here: both the kernel and its quotient
are saturated free lattices, and applying
\(\operatorname{Hom}_G(M_a,-)\) preserves the
surjections. Apply the orbit projector and then
\(1-e\), where \(e\) is the total
\(\widetilde E\)-projector. This gives
\(A_a:M_a\to\mathcal L\) with \(eA_a=0\),
the required reduction, and compact image in
the same \(M_a\). These are exact integral maps;
successive choices of lifts modulo \(2^n\) are
compatible by the same surjections and define
their continuous inverse limits.

The projective coefficient module \(M_a\) has
zero positive cohomology over \(G\).
Inflation--restriction therefore lifts the
actual affine projection \(m_a:U\to M_a\)
to a derivation of the full homology source.
It kills the cusp vector \([t^{36}]\).
Projectivity for the actual cyclic subgroup
\(\langle t\rangle\) gives the integral equality
\(\ker N_{36}(t)=(1-t)M_a\).
Subtracting its corresponding inner derivation
makes the value at \(t\) zero. The same exact
cyclic sequences give
\[
 \eta_a(s)=(1-s)d_{a,s},\qquad
 \eta_a(r)=(1-r)d_{a,r},\qquad
 \eta_a(t)=0.
 \tag{D.64.20}
\]
The homology kernel is killed, so the derivation
factors through \(Y\), as in D.63.22.
Composition with \(A_a\) takes values in its
actual abelian subgroup \(\mathcal L\).
Because \(\alpha_{63,Y}\) induces identity on
\(G\), the second line of (D.64.9) is a
homomorphism. The two conjugators change by
the actual vectors \(A_ad_{a,s},A_ad_{a,r}\).
They have zero images in \(X_*\) and
\(\mathcal W_h\), and each has a genuine lift
in \(S_{57}\) by D.58.2.

The homology matrix is the first line of
(D.64.9). It is identity on \(\widetilde E\),
preserves all cusp vectors, has the invertible
reductions \(X_1,X_4\) on the two changed compact
blocks, and has its old invertible blocks on
the others. It is therefore an integral
automorphism. The quotient and kernel maps
in D.58's actual fibre product are automorphisms,
so \(\beta_Y\) is an automorphism of \(Y\).
This proves the passage from the finite isometries
to actual integral peripheral source maps.

\emph{A stable quotient for the eight source-involution coordinates.}
For \(a=2,3\), repeat (D.64.17) with the actual
small action. The full affine space has dimension
16 in each branch; its linear rank is 496.
On the ten-dimensional space \((C_a)_G\), the
exterior action is the quadratic matrix polynomial
\[
 F_0+\sum_{i=1}^{16}e_iF_i+
                    \sum_{1\leq i<j\leq16}e_ie_jF_{ij}.
 \tag{D.64.21}
\]
All 137 coefficient matrices in each branch,
and all 274 in the two branches together,
are retained. Naturality of (D.64.6) shows that
its image \(I_a\) is invariant under every one
of these matrices; the program checks each
of these restrictions directly as well.

In the retained ten-coordinate bases, and the
ordered four-coordinate bases of \(I_a\), the
columns of the retractions are the following
binary masks, written in hexadecimal:
\[
 \begin{aligned}
 p_2&=(\mathtt a,\mathtt5,0,\mathtt2,\mathtt7,
                    \mathtt6,\mathtt9,\mathtt2,\mathtt5,0),\\
 p_3&=(\mathtt2,\mathtt2,\mathtt3,\mathtt9,\mathtt f,
                    \mathtt5,\mathtt d,\mathtt4,0,0).
 \end{aligned}
 \tag{D.64.22}
\]
The inclusion columns are respectively
\((\mathtt{136},\mathtt{75},\mathtt{2c},\mathtt{1e0})\)
and
\((\mathtt{254},\mathtt{353},\mathtt{2bc},\mathtt{2ab})\).
Here a mask lists binary coordinates from its
least significant bit upward. These inclusions
are the actual independent source-s correction
columns, not arbitrarily chosen subspaces.

The simultaneous equations
\[
 p_ai_a=1,
 \qquad p_aF=F|_{I_a}\,p_a
       \quad\text{for every coefficient in (D.64.21)}
 \tag{D.64.23}
\]
are linear in the 40 entries of \(p_a\).
They have rank 34 and are satisfied by (D.64.22).
It follows by polynomial substitution that the
same retraction intertwines every compact
homology action in either complete affine family.
In particular it intertwines the actual
\(T_{63}\), which remains unchanged on these
two compact blocks. Its kernel is consequently
invariant, with an invertible quotient action.
This proves the needed descent through the
eight-dimensional quotient without an assumption
about the unrecorded full homology matrix.

\emph{All actual source-involution and full-cusp terms.}
The program \path{d_residual_compact_cusp.py}
uses \(\ker\phi_a\), of fibre dimension 12
over \(\mathbb F_4\), as the source of the
correction maps. It induces this module with
the actual coset representatives and actual
affine generators
\[
 s=(0,S),\qquad r=(v_r,R),\qquad
 t=(Q_Sv_r,SR),\qquad Q_Sv_r=(1,1,0,1).
 \tag{D.64.24}
\]
It checks \(s^2=r^3=1\) and \(t=sr\)
on every column. It uses the full sum
\(N_{36}(t)=\sum_{j=0}^{35}t^j\), retaining
every term, even though this coefficient
action has period 12. In particular
\(t^{18}\) has Q-state 314 and translation
\((0,2,1,0)\); the pure Q-state 314 is not
substituted for this actual cusp power.

Formula (D.64.12) gives the averaged wedge of
two real vectors as
\(v\bar w^t+w\bar v^t\). All 496 real basis
wedge pairs are checked against the literal
sum over scalar multiplications by
\(1,\omega,\omega^2\).
After taking the actual kernel coinvariants,
the computed correction maps are
\[
 v\longmapsto[e_\Delta(v\wedge sv)]_G,
 \qquad
 v\longmapsto[e_\Delta(v\wedge N_{36}(t)v)]_G.
 \tag{D.64.25}
\]
All 238656 polar equations vanish. The first
map factors through the actual \(1+s\) norm;
the second factors through the actual full
\(N_{36}(t)\) norm. Their ranks are
\[
 \begin{array}{c|r|r|r|r}
 a&\dim\ker\nu_a&\operatorname{rank}(s\text{ correction})
       &\operatorname{rank}(t\text{ correction})
       &\text{uncovered tested coordinates}\\\hline
 1&0&0&0&0\\
 2&10&4&0&6\\
 3&10&4&0&6\\
 4&2&0&0&2
 \end{array}
 \tag{D.64.26}
\]
On the two retracted quotients, actual source
indices \((144,145,147,149)\) and
\((1,2,3,4)\) map to the four standard basis
vectors, respectively. All indices are zero
based in the retained induced source bases.

To realize these columns in the actual group,
lift a chosen compact vector through
(D.64.11) into \(\mathcal L\), and then to
\(u\in S_{57}\). Let \(\widetilde s\) be the
actual image of the source involution in a
preliminary peripheral lift. With the convention
\([a,b]=aba^{-1}b^{-1}\), put
\[
 b_s=u\widetilde s u\widetilde s^{-1},\qquad
 b_s\widetilde s b_s^{-1}\widetilde s^{-1}
                 =[u,\widetilde s u\widetilde s^{-1}].
 \tag{D.64.27}
\]
The image of \(b_s\) in \(Y\) is the s-fixed
vector \(v+sv\). Changing this source conjugator
therefore preserves the \(Y\)-action exactly.
Its class-two error has precisely the first
image in (D.64.25). Both comparison conjugators
in \(X_*\) and \(\mathcal W_h\) remain literally
unchanged. Compact lifts in these two \(M\)-blocks
have no \(\widetilde E\)-component, so their
errors have zero projections to all earlier
selected compact blocks and to the other two
compact self blocks.

For completeness the full cusp word is
\(b_t=U_0U_1\cdots U_{35}\), where
\(U_j=t^jut^{-j}\), and \(c=t^{36}\).
Exact class-two collection gives
\[
 b_ttb_t^{-1}t^{-1}
      =[u,U_1\cdots U_{35}][c,u]^{-1}.
 \tag{D.64.28}
\]
The wrap term is \(U_{36}=cuc^{-1}\).
Compactification kills the cusp factor in
\([c,u]\), and the remaining term is the
second map in (D.64.25). The certificate keeps
this entire 36-term map; its value on the
compact kernels is zero. Earlier \(\widetilde E\)
corrections still use these full words. They
give exactly the inner change in (D.64.9),
and their projection to every \(M\)-self
quotient here is zero.

\emph{Boundary zero, quotient descent and the remaining kernel.}
After the homology correction, the compact
action remains block diagonal for
\(\widetilde E_a\perp M_a\), with identity on
the first part. All earlier fixed-row norm
arguments remain valid. The D.62 self corrections
are re-applied in the actual
\(\widetilde E\)-lifts; they leave the new
compact quotient coordinates unchanged.
The earlier moving components are corrected
by their actual augmentation equations, which
also have zero image in the new compact quotient.
This produces a preliminary source lift whose
cusp defect \(z\) belongs to \(\mathcal J_{63}\).

D.55's unquotiented orientation identity applies
to these literal conjugators. On an old compact
self block its orientation bivector is represented
by \(\overline{(H_a^{\rm int})^{-1}}\).
Equation (D.64.5) implies
\[
 X_a\overline{(H_a^{\rm int})^{-1}}\bar X_a^t
                =\overline{(H_a^{\rm int})^{-1}},
 \qquad \nu_a(q_az)=0\quad(a=1,4).
 \tag{D.64.29}
\]
The last program checks this complete bivector
identity, all 256 norm-intertwining columns,
and the invertible induced kernel and norm-image
actions in both branches. By (D.64.4), the
coinvariant class of \(q_1z\) is zero. The
\(\nu_4(C_4)\)-coordinate itself is zero.

Use the eight actual involution words in
(D.64.27) to cancel the two coordinates
\(p_2[q_2z]\), \(p_3[q_3z]\). They do not
change (D.64.29). The only remaining defect
in \(\mathcal E_{64}\) is the augmentation
part of \(C_1\). Since the actual generators
\(s,r\) generate \(G\), the exact map
\[
        (b,d)\longmapsto(1-s)b+s(1-r)d
 \tag{D.64.30}
\]
has image the augmentation submodule. Lift its
chosen coefficients through the onto map
\(\Phi_{64}\). They are actual elements of
\(\mathcal J_{63}\), so these final central
changes preserve \(Y\) and every previous
comparison. The cusp defect now lies in
\(\mathcal J_{64}\).

The induced exterior action preserves
\(\mathcal J_{63}\). It preserves the kernel
of \(q_1\) and induces an automorphism on
\(C_1\), because the actual compact action
preserves \(M_1\) and its small square.
It commutes with the norm, hence preserves
the kernel of \(\nu_4q_4\) and induces an
automorphism on its image. The universal
identities (D.64.23) give the two remaining
kernel preservations. Consequently it
preserves their exact intersection
\(\mathcal J_{64}\). The class-two laws and
the invertible Frattini map give the automorphism
on the finite class-two factor. Its common
quotient with the full homology and
\(\mathcal W_h\) sources stays equivariant.
D.58's marked fibre product is exactly
\(X/\mathcal J_{64}\), proving the asserted
actual automorphism.

Joint surjectivity in (D.64.3), the retractions,
and the two-dimensional norm image prove
(D.64.8) and the dimension statements in
(D.64.10). No direct-sum splitting of
\(\mathcal J_{63}\) is required: this theorem
uses the actual quotient map \(\Phi_{64}\).
For example \(C_4\) has a 1918-dimensional
kernel of its norm. A nonzero vector there
has a lift in \(\mathcal J_{63}\) with zero
other orbit coordinates; that lift belongs
to \(\mathcal J_{64}\) and is nonzero.
This proves the remaining kernel assertion
with its literal source map.

The six programs retain the integral cycle lifts,
all finite coefficient matrices, complete polynomial
equations, actual source actions, kernel bases,
retractions and extension comparisons. Their
six complete author runs and separate copied-input
replays are recorded alongside the actual stdout.
The fourteen uncovered coordinates in (D.64.26)
are an exact limit of those two tested maps.
No conclusion about the rest of the nonzero
kernel in (D.64.10), or about a full
\(\widehat B\)-automorphism lifting this action,
is drawn from the finite calculations.
\end{proof}

# The whole actual modular central tower and a compatible full peripheral lift

Checkpoint34 research sequel. The complete first-step source remains unchanged at work_A/actual_next_modular_central_refinement34.md, SHA9ccc6406ec9558d4715ed7837feffb844af40606b2743d6574eb6ef399eba0b5. No new formal source or paper claim is added in this note.

## 1. Series, actual quotients and the precise conclusion

Use all actual full-GT canonical data and notation of that proof. In particular
\[
B=C_2(s)\amalg C_3(r),\quad F=\ker(B\to S_3),\quad
N=\ker q,\quad N_1=\overline{[N,F]},
\]
\[
O=\ker(F\to F^{(2)}),\qquad \overline B=B/O,\qquad
M_{21}=\overline{[M_2,F^{(2)}]}.
\]
Define a new, explicitly B-relative series
\[
L_0=N_1,\qquad L_{j+1}=\overline{[L_j,B]},\qquad
L_\infty=\bigcap_{j\ge0}L_j,
\]
and put \(B_j^\flat=B/L_j\), \(A_j=\pi_2(L_j)\le\overline B\). Thus \(B_0^\flat=B_1\) in the preceding notation; the indexing is not the F-relative series of A107.

For every finite j we prove:
\[
A_0=M_{21},\qquad A_{j+1}=\overline{[A_j,\overline B]},       \tag{1}
\]
\[
L_j/L_{j+1}\text{ is pro-two},\qquad
L_{j+1}=L_j\cap\pi_2^{-1}(A_{j+1}),\qquad H_d\in L_j.       \tag{2}
\]
Each \(B_j^\flat\) has a canonically identified closed normal subgroup \(D_o\), isomorphic to the odd fiber product in the first-step proof, and
\[
B_j^\flat/D_o=\overline B/A_j.                              \tag{3}
\]
The word assignments \(s\mapsto v=u^{-1}s\), \(\delta\mapsto\delta^d\) give genuine automorphisms \(\Psi_j\) of all these quotients, and of \(B/L_\infty\). They satisfy the actual involution intertwining there.

There exists a full peripheral automorphism \(\widetilde\Psi_\infty\) of B, with cusp \(\delta\mapsto\delta^d\), inducing these same compatible \(\Psi_j\) and hence their limit. This is an existence theorem for a full lift of the quotient actions, not an identification of its full pure action with the canonical \(\psi_d\), nor a full conjugacy of the original \(\alpha\) with \(c_B\).

In particular no cofinality assertion is made. Already
\[
N_1\cap O\subseteq L_\infty                                  \tag{4}
\]
follows from (2), so the construction explicitly retains that possible residual.

## 2. The odd group has unique splittings of central pro-two extensions

The actual \(D_o\) from the first-step proof has
\[
H^1(D_o,\mathbb Q_2/\mathbb Z_2)
=H^2(D_o,\mathbb Q_2/\mathbb Z_2)=0.
\]
The short exact sequence with multiplication by \(2^n\) on this divisible module gives
\[
H^1(D_o,\mathbb Z/2^n)=H^2(D_o,\mathbb Z/2^n)=0.             \tag{5}
\]
For H1, use surjectivity of multiplication by \(2^n\) on the invariant trivial module and the zero H1 above. For H2, use the two adjacent zero H1/H2 terms. Finite direct sums give (5) for every finite abelian two-group with trivial action.

Consequently every central extension of \(D_o\) by such a finite group has a unique continuous splitting. Existence is the zero continuous H2 class; uniqueness is the zero H1, equivalently the absence of homomorphisms from \(D_o\) to the finite kernel. A finite-kernel profinite extension has a continuous set section: choose an open subgroup meeting its finite kernel trivially, then use finitely many clopen cosets. Thus the usual continuous-cohomology classification applies.

The same assertion holds for a compact abelian pro-two central kernel Z. Quotient the extension by every open subgroup U of Z. Centrality makes U normal in the extension, and the resulting kernel Z/U is finite. Its unique splitting is compatible with every further quotient by uniqueness. Taking the inverse limit gives a continuous splitting of the original extension, because the extension is the inverse limit of these compact quotients and their kernels intersect in1. Uniqueness also follows from (5), by passing to every finite Z/U.

If this extension is the preimage of a normal copy of \(D_o\) in a larger compact group, its split copy is normal in that larger group. Conjugation transports the splitting, after correcting the base automorphism, to another splitting of the same extension. Uniqueness makes the copies equal. No arbitrary choice of incompatible finite complements is made.

## 3. Induction of the canonical odd subgroup and odd H2 vanishing

The base \(B_0^\flat=B_1\) has the exact normal \(D_o\) and quotient \(\overline B/M_{21}\) by the first-step proof. It also has zero odd-primary H2.

Suppose these assertions hold at stage j. Every B-invariant odd-primary character of \(L_j\) transgresses into
\[
H^2(B_j^\flat,\mathbb Q_\ell/\mathbb Z_\ell)=0
\quad(\ell\text{ odd}).
\]
Five-term exactness therefore makes it a restriction of a character of B. It vanishes since \(L_j\subseteq N_1\subseteq B'\). Continuous character separation shows that
\[
Z_j=L_j/L_{j+1}
\]
is pro-two. It is central in \(B_{j+1}^\flat\) by definition.

Restrict the extension \(B_{j+1}^\flat\to B_j^\flat\) to the canonical \(D_o\) at stage j. Section2 gives a unique split copy \(D_o\) at stage j+1, and its normality. The new copy maps isomorphically to the old one. The quotient of the pure subgroup \(F/L_{j+1}\) by this copy is a central pro-two extension of the previous pure pro-two quotient. It is therefore pro-two.

This identifies the odd subgroup with the actual image of O. Indeed the map from F to that pro-two quotient kills O by the defining universal property of the maximal pro-two quotient. Thus the image of O at stage j+1 lies in the new \(D_o\). Its projection to the old \(D_o\) is onto by induction, while the new \(D_o\) maps isomorphically to the old. Hence the image of O is exactly the new \(D_o\). We obtain the literal quotient identity
\[
B_{j+1}^\flat/D_o
 =B/(L_{j+1}O)=\overline B/\pi_2(L_{j+1}).                   \tag{6}
\]
This step is why the lower comparison continues to be the same actual \(\overline B\), rather than a newly chosen pro-two extension.

Finally the central kernel \(Z_j\) has zero positive cohomology with odd-primary discrete coefficients, by finite-two-group averaging and passage to continuous limits. Inflation therefore preserves the vanishing
\[
H^2(B_{j+1}^\flat,\mathbb Q_\ell/\mathbb Z_\ell)=0
\quad(\ell\text{ odd}).
\]
This completes the induction of the group structure and the odd vanishing.

## 4. Every next coordinate kernel and the same actual hexagon

The whole proof of (7)--(8) in the first-step source applies to the actual \(D_o\) at every stage:
\[
H^2(\overline B/A_j,\mathbb Q_2/\mathbb Z_2)
 \xrightarrow{\ \mathrm{inf}\ }
H^2(B_j^\flat,\mathbb Q_2/\mathbb Z_2)
\quad\text{is an isomorphism}.                              \tag{7}
\]
We retain the already proved
\(H^2(\overline B,\mathbb Q_2/\mathbb Z_2)=0\).
For the actual extension diagram
\[
\begin{array}{ccccccccc}
1&\to&L_j&\to&B&\to&B_j^\flat&\to&1\\
 &&\downarrow&&\downarrow&&\downarrow\\
1&\to&A_j&\to&\overline B&\to&\overline B/A_j&\to&1
\end{array}
\]
the same five-term naturality shows that every B-invariant two-primary character of \(L_j\) is
\[
\chi=\chi_{2,j}\circ\pi_2|_{L_j}+\lambda|_{L_j},              \tag{8}
\]
where \(\chi_{2,j}\) is \(\overline B\)-invariant on \(A_j\) and \(\lambda\) is a character of B. The odd characters were already shown to vanish.

Continuous images of closed commutator subgroups under a compact surjection give
\[
\pi_2(L_{j+1})
 =\overline{[\pi_2(L_j),\overline B]},
\]
proving (1). Commutator functoriality gives the forward inclusion in (2). For its reverse, (8) and the vanishing odd characters kill every element of
\(L_j\cap\pi_2^{-1}([A_j,\overline B])\); character separation of \(L_j/L_{j+1}\) gives exactly L_{j+1}. In particular
\[
L_j/L_{j+1}\simeq A_j/A_{j+1}
\]
as actual compact groups.

A106 gives \(H_d\in L_0\), and A89.3 gives its entire actual pro-two image1 for the same canonical u,d. The exact coordinate equality now proves inductively \(H_d\in L_j\) for every j. It also proves (4) immediately. Nothing in this argument makes that intersection trivial.

## 5. Genuine automorphisms, factor frames and all finite-stage full lifts

Because \(H_d\in L_j\), the exact ordered cubic identity gives a homomorphism
\[
B\to B_j^\flat,\qquad s\mapsto v,\quad r\mapsto v\delta^d.
\]
Its pure restriction is the actual \(\psi_d\). This homomorphism kills L_j. To see this without assuming a full source endomorphism of B, start with \(\psi_d(N_1)\subseteq N_1\), already proved in A107. The homomorphism sends each successive commutator subgroup \([L_i,B]\) into the corresponding image of \(L_{i+1}\). At i=j it therefore kills L_j. It descends to \(\Psi_j\).

If \(N^{F}_0=N\), \(N^{F}_{i+1}=[N^{F}_i,F]\) is the earlier F-relative series, then
\[
N^{F}_{j+1}\subseteq L_j.
\]
This follows from equality at j=0 and commutator induction. A107's automorphy on \(F/N^{F}_{j+1}\) makes the induced pure map on \(F/L_j\) surjective; it is therefore an automorphism by finite generation and Hopficity. The map on S3 is the identity. Thus \(\Psi_j\) is an automorphism of \(B_j^\flat\). The same actual generator identity gives \(\alpha\Psi_j=\Psi_jc_B\). The quotient maps commute with all these automorphisms.

For every finite j, the kernel of \(B_j^\flat\to B_1\) is pro-two: it is a finite iterated extension of the central pro-two groups in (2). Lift the A108 r-frame from B1 to stage j. The residual order-three cocycle is in this actual pro-two kernel. The complete coprime C3 lemma of A108 kills it, providing a factor frame upstairs. Equivalently apply the same correction at each central step. The s-frame exists already in the full source from v²=1 and the finite-factor torsion theorem. The cusp is literal \(\delta^d\).

In particular stage j+1 is the positive-peripheral central refinement required for lifting stage j, after the same actual multiplier reduction as in the first-step proof. Use an actual multiplier-d Galois automorphism. The original LM7_PUSH E65.15 covariance makes it preserve N, N1 and hence every L_j; the original cusp formula is literal. Composition with its inverse removes the common unit power, including the r-branch. Apply the closed-normal modular central criterion of A3/A34 to the kernel L_j and its next closed commutator [L_j,B]=L_{j+1}. It gives a full peripheral automorphism inducing \(\Psi_j\). Its cusp conjugator can be corrected inside L_j so that the cusp is literally \(\delta^d\), as in the first-step proof.

No unrestricted order-preserving or equivariant lifting theorem is used. The conclusion is a lift of each specified quotient automorphism, with its peripheral data.

## 6. Compact compatibility of the full lifts

The actual quotient B/L_infinity is the inverse limit of B/L_j: compatible cosets have a common point by compactness. The compatible automorphisms \(\Psi_j\) and their inverses therefore give an automorphism \(\Psi_\infty\) of this actual quotient.

The group Aut(B) is compact. One concrete justification is the standard bounded-order construction of cofinal fully invariant open subgroups in a finitely generated profinite group: only finitely many homomorphisms to finite groups of bounded order occur. The endomorphism generator-image space is compact, and invertibility on all these finite quotients is a closed condition. The peripheral conditions, the fixed multiplier d and the literal cusp equation are also closed, since the required conjugators range over compact B.

For each j, let C_j be the closed set of full peripheral automorphisms inducing \(\Psi_j\) and sending δ literally to δ^d. Section5 proves C_j nonempty. The sets are descending, because the quotient automorphisms are compatible. Compactness gives
\[
\widetilde\Psi_\infty\in\bigcap_j C_j.
\]
It induces \(\Psi_\infty\) and stabilizes L_infinity. This proves the asserted compatible full lift, without a prior choice of mutually compatible finite-stage conjugators.

Its conjugate \(\widetilde\Psi_\infty c_B\widetilde\Psi_\infty^{-1}\) agrees with the original \(\alpha\) on B/L_infinity. Equality on B has not been shown. Similarly its pure restriction agrees with the canonical \(\psi_d\) only on the displayed quotient system. The residual subgroup need not be cofinal or trivial, and the original coherent-frame/CM obstruction remains undetermined.

## 7. Audit scope

This note is a single all-level induction, not a finite-target census. Its base is the complete separately saved first-step proof9ccc6406, already independently read by CE and DE. The new compact splitting argument includes all topology and compatibility steps. The only primary finite-group input remains the already bound Beyl5.7 and the original source-bound lifting/covariance theorems. No additional source theorem, finite producer, private build, render or central file edit was used.

Complete independent source review is requested. Formal A106–A108 and the combined checkpoint34 PDF remain unchanged.


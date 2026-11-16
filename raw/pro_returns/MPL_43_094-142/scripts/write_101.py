from page_work import save_page
text=r'''\scanpage{101}
\mspage{100}
\mspage{22.}
proves one half of (6.5) in all cases.

The problem of determining the actual numbers $q_k$ in (6.5) is thus
seen to be a special case of the more general problem of determining
the structure of the group $J(X)$. An attack on this problem by the
methods of [2] and [3] will be given in a future publication.

We conclude with a few remarks on the relation between the methods of
this paper and those of James. The main tool of James is the ``intrinsic
join''. Actually he defines several ``intrinsic joins'', two of them
being maps
\[
\begin{aligned}
Q_{n,k}*P_{m,k}&\longrightarrow P_{m+n,k}\\
Q_{n,k}*Q_{m,k}&\longrightarrow Q_{m+n,k},
\end{aligned}
\]
where $X*Y$ denotes the join of $X$ and $Y$. Since
$X*Y=S(X\mathbin{\times\mkern-10mu\times}Y)$\inserted{${}^+$}
these two maps can, in view of (2.4) (4.3) and (5.4), be written
\[
\begin{aligned}
P_k^{(n-k)\xi\oplus\eta}\mathbin{\times\mkern-10mu\times}
P_k^{(m-k)\xi}&\longrightarrow P_k^{(m+n-k)\xi}\\
P_k^{(n-k)\xi\oplus\eta}\mathbin{\times\mkern-10mu\times}
P_k^{(m-k)\xi\unsure{\oplus\eta}}&\longrightarrow
P_k^{(m+n-k)\xi\oplus\unsure{\zeta|\eta}}.
\end{aligned}
\]
In view of (4.5) both these are maps of the type
\[
f:X^\alpha\mathbin{\times\mkern-10mu\times}X^\beta
\longrightarrow X^{\alpha+\beta+\tau}
\]
where $X$ is a compact differentiable manifold with tangent bundle
$\tau$. By (3.3), and the fact that the smash product commutes with
duality, the dual of $f$ is a map of the form:
\[
Df:X^{\gamma+\delta}\longrightarrow
X^\gamma\mathbin{\times\mkern-10mu\times}X^\delta
\]
where $\gamma=-\alpha-\tau$, $\delta=-\beta-\tau$. Now the diagonal map
$X\longrightarrow X\times X$ induces a map
\[
\Delta:X^{\gamma+\delta}\longrightarrow(X\times X)^{\gamma\times\delta}
=X^\gamma\mathbin{\times\mkern-10mu\times}X^\delta
\quad\text{by (2.3).}
\]
It would seem reasonable to suppose that the maps $Df$ and $\Delta$ are
of the same $S$-homotopy type.

In addition to the maps first mentioned James also defines an intrinsic
join for the Stiefel manifolds $O_{n,k}$. This has no counter-part here,
since we are not directly concerned with Stiefel manifolds.

\margin{$+$ up to homotopy type}
Pembroke College,\\
Cambridge.
'''
save_page(101,text,[('text','rotated upper right archive number','100'),('text','rotated upper right typed folio','22.'),('text','rotated top continuation','proves one half of (6.5)'),('text','rotated upper paragraph','The problem of determining'),('text','rotated next paragraph','We conclude with a few remarks'),('display','rotated upper middle two maps','Q n,k * P m,k; Q n,k * Q m,k'),('text','rotated middle','where X * Y denotes the join'),('insertion','after S(X smash Y)','plus footnote marker'),('display','rotated middle two maps','P k superscripts xi eta'),('text','rotated middle lower','In view of (4.5)'),('display','rotated middle lower','f:X alpha smash X beta'),('text','rotated lower','where X is a compact differentiable manifold'),('display','rotated lower','Df:X gamma+delta to X gamma smash X delta'),('text','rotated lower','where gamma=-alpha-tau'),('display','rotated lower','Delta:X gamma+delta to (X times X) gamma times delta'),('text','rotated lower','It would seem reasonable to suppose'),('text','rotated bottom paragraph','In addition to the maps first mentioned'),('margin note','rotated bottom in blue ink','plus up to homotopy type'),('text','rotated bottom address','Pembroke College Cambridge')],sheet_kind='reused_typed',observations='Printed leaf is upside down relative to scan numbering; whole and halves viewed in supplied orientation, then rotated 180 degrees and read line by line. Blue handwritten plus and footnote retained. The printed smash-product sign is reconstructed as two overlapping multiplication crosses rather than replaced by a modern wedge. Faint superscripts in the second P-map are marked.')

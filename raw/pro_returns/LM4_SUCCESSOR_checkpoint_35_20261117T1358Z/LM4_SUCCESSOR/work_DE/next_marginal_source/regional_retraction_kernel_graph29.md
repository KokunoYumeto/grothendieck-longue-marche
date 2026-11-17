# The actual regional neck-retraction kernel as a graph group

Checkpoint29 research. This note concerns the actual regional ordinary group and its specified neck retraction. It does not replace either ambient filling by a coordinate filling. Every checkpoint28 source remains unchanged.

## 1. The actual height graph and a useful auxiliary section

Use the complete B112 height presentation, already obtained by reversible transformations of all ten regional node words. Write

\[
R^0=A(\Gamma)\rtimes\langle h\rangle,
\quad U_n=h^nUh^{-n},\quad \bar U_n=h^nCUCh^{-n},
\quad k_0=k,\quad k_1=CkC.
\]

The vertices of \(\Gamma\) are \(U_n,\bar U_n\), for \(U=a,b,d,e\) and \(n\in\mathbb Z\), and \(k_0,k_1\). The complete edge list, at every integer n and with all barred images included, is

1. \(U_n--\bar U_n\), for the four U;
2. \(a_n--b_n,\ \bar a_n--d_n,\ \bar a_n--e_n,\ d_n--\bar e_n\);
3. \(b_n--d_{n+1},\ b_n--e_{n+1}\);
4. \(k_{n\bmod2}--U_n\), for the four U.

There is no edge between the two k vertices. The h action shifts every family index and exchanges the k vertices. The original parity has already been taken: all graph vertices and h belong to the actual ordinary group.

Put

\[
A_n=a_n,\quad B_n=\bar b_n,\quad D_n=d_n,\quad E_n=e_n,
\qquad \Delta=\{A_n,B_n,D_n,E_n:n\in\mathbb Z\}.
\]

No edge joins two vertices of \(\Delta\). Coordinate deletion of every other graph vertex therefore gives an h-equivariant retraction

\[
q_h:R^0\longrightarrow F(\Delta)\rtimes\langle h\rangle
          =K_h=F(a,B,d,e,h),\qquad B=CbC.
\tag{1}
\]

The last equality is an exact free presentation: conjugating the four level-zero generators by h gives every named level generator, with no relation among them.

The actual neck is instead \(K=F(a,B,d,e,f)\), where \(f=hk_0^{-1}\). Identify the abstract free group \(K_h\) with K by fixing the four family generators and sending h to the actual f. The composite of (1) with this identification is **the actual retraction** \(r:R^0\to K\): it fixes a,B,d,e and sends f=hk_0^{-1} to f. It kills k and the opposite four family generators. These are precisely the established B114/B117 retraction values on a generating set of \(R^0\).

Consequently

\[
N_R:=\ker(r:R^0\to K)=\ker(q_h)=\ker(A(\Gamma)\to F(\Delta)).
\tag{2}
\]

This changes the section used to describe the kernel; it does not silently identify h with f in \(R^0\).

## 2. An explicit general graph-kernel construction

Let \(\Gamma\) be any graph and \(\Delta\) an induced full subgraph. Write \(T=A(\Delta)\), and let \(\mathcal D\) be the remaining vertex set. For \(v\in\mathcal D\), put

\[
L_v=A(\operatorname{link}_\Gamma(v)\cap\Delta)\le T.
\]

Define a graph \(\Sigma\) as follows. Its vertices are

\[
(gL_v,v),\qquad v\in\mathcal D,\quad g\in T.
\tag{3}
\]

For every original edge \(v--w\) with both vertices in \(\mathcal D\), and every \(g\in T\), put an edge between \((gL_v,v)\) and \((gL_w,w)\). Repeated declarations make one edge. T acts by left multiplication on the coset coordinates. Then there is an exact marked isomorphism

\[
A(\Gamma)\cong A(\Sigma)\rtimes T,
\qquad\ker(A(\Gamma)\to T)=A(\Sigma).
\tag{4}
\]

Here is a full presentation proof, valid also for infinite graphs. Send the vertex \((gL_v,v)\) to \(gvg^{-1}\) in \(A(\Gamma)\). It is independent of the coset representative because every generator of \(L_v\) commutes with v. A displayed \(\Sigma\)-edge maps to a conjugate of an original deleted/deleted commutator, and the T action agrees with conjugation. This gives a map from the right side of (4).

In the other direction, send a retained vertex to its element of T and a deleted vertex v to \((L_v,v)\). Retained/retained relations hold in T. A retained vertex adjacent to v belongs to \(L_v\), so it stabilizes \((L_v,v)\) and commutes with it in the semidirect product. Every deleted/deleted relation is an edge with g=1. Thus every original relation holds. The two homomorphisms are inverse on T and all named graph vertices, proving (4). No unproved graph-kernel theorem, relation independence or finite approximation is needed.

Apply this construction to the actual graph of Section1. It proves that \(N_R\) is the explicitly described graph group \(A(\Sigma)\), with T here the countably generated free group \(F(\Delta)\).

## 3. The complete actual link table

Write the four deleted family types as

\[
\alpha_n=\bar a_n,\qquad \beta_n=b_n,\qquad
\delta_n=\bar d_n,\qquad \epsilon_n=\bar e_n.
\]

Their full retained links and their deleted neighbors are given by the following table. The entries in the middle column freely generate \(L_v\).

| Deleted vertex v | Retained link generators | Deleted neighbors |
|---|---|---|
| \(\alpha_n\) | \(A_n,B_n,D_n,E_n\) | \(k_{n+1\bmod2}\) |
| \(\beta_n\) | \(A_n,B_n,D_{n+1},E_{n+1}\) | \(k_{n\bmod2}\) |
| \(\delta_n\) | \(A_n,D_n,E_n,B_{n-1}\) | \(k_{n+1\bmod2}\) |
| \(\epsilon_n\) | \(A_n,D_n,E_n,B_{n-1}\) | \(k_{n+1\bmod2}\) |
| \(k_0\) | all \(A_{2j},D_{2j},E_{2j},B_{2j+1}\) | \(\beta_{2j},\alpha_{2j+1},\delta_{2j+1},\epsilon_{2j+1}\) |
| \(k_1\) | all \(A_{2j+1},D_{2j+1},E_{2j+1},B_{2j}\) | \(\beta_{2j+1},\alpha_{2j},\delta_{2j},\epsilon_{2j}\) |

Every entry follows from the complete four edge families in Section1. For example the \(B_{n-1}\) neighbor of \(\delta_n\) is the barred image of \(b_{n-1}--d_n\); no height translate is suppressed. The last two rows include all integers j.

Thus \(\Sigma\) is bipartite, between expanded k vertices and expanded family vertices. This does **not** make it a forest or make its graph group free. For example, \(\delta_n\) and \(\epsilon_n\) have the same retained link. Let \(\kappa=k_{n+1\bmod2}\). The retained letter \(A_n\) is in their common link but is not in \(L_\kappa\). Therefore the two distinct center vertices

\[
(L_\kappa,\kappa),\qquad(A_nL_\kappa,\kappa)
\]

are each adjacent to the same two family vertices \((L_{\delta_n},\delta_n)\) and \((L_{\epsilon_n},\epsilon_n)\). Their full induced graph is a square: the centers are nonadjacent, as are the two families. Its graph group is a genuine full coordinate \(F_2\times F_2\) subgroup of \(N_R\). This is an exact regional fact, not a statement about the geometric filling kernel M or the final source.

## 4. The local inclusion factor is literally a coordinate subgroup

Recall the actual subgroup \(E_1=C\langle K,k\rangle C\). It contains h, k0 and k1, and is generated by h together with the deleted level-zero family vertices and the centers. Indeed its specified generators are \(\bar a,b,\bar d,\bar e,f_1,k_1\), with \(f_1=CfC=h k_1^{-1}\); conversely h=f1k1 and k0=h^-1k1h.

Let \(\Gamma_{\mathcal D}\) be the full deleted-vertex subgraph of \(\Gamma\). The height presentation therefore gives

\[
E_1=A(\Gamma_{\mathcal D})\rtimes\langle h\rangle,
\qquad E^0:=E_1\cap N_R=A(\Gamma_{\mathcal D}).
\tag{5}
\]

The indicated graph subgroup is a full coordinate subgroup in \(A(\Gamma)\), and in the kernel model (3) it is exactly the full coordinate subgroup on

\[
\{(L_v,v):v\in\mathcal D\}\subset\Sigma.
\tag{6}
\]

There are no new edges on this set: a pair of its vertex types can be adjacent in \(\Sigma\) only when the same pair was an original deleted/deleted edge, and then g=1 already gives that edge.

In particular \(\Gamma_{\mathcal D}\) is the disjoint union of two infinite stars, by the table. Hence (5) also supplies the explicit free-product description

\[
E^0=(\mathbb Z(k_0)\times F(\mathcal L_0))*
     (\mathbb Z(k_1)\times F(\mathcal L_1)),
\tag{7}
\]

where \(\mathcal L_0=\{\beta_{2j},\alpha_{2j+1},\delta_{2j+1},\epsilon_{2j+1}\}\) and \(\mathcal L_1\) has the opposite parities. The factors are infinite-rank only in their displayed free leaf groups. This is an exact description of the retraction kernel in E1, not an abstract rank assertion.

## 5. The actual neck action keeps a specific nonlinear correction

Let \(\sigma\) denote the h-shift automorphism of T and \(A(\Sigma)\). On vertices it is

\[
\sigma(gL_v,v)=(\sigma(g)L_{\sigma(v)},\sigma(v)),
\]

where it shifts family levels and exchanges k0,k1. For \(u\in\{a,B,d,e\}\), conjugation by the actual neck generator u acts on \(\Sigma\) by left multiplication of its level-zero retained letter on g.

The actual branch generator is f=hk0^-1. Thus its action on the kernel is exactly

\[
\operatorname{Ad}(f)
  =\sigma\circ\operatorname{Inn}(k_0^{-1})
  =\operatorname{Inn}(k_1^{-1})\circ\sigma,
\qquad
\operatorname{Ad}(f^{-1})
  =\operatorname{Inn}(k_0)\circ\sigma^{-1}.
\tag{8}
\]

Both displayed k elements are the identity-coset center vertices of \(\Sigma\). They are not erased. Notice that f preserves the coordinate subgroup E0 of (5), since both the shift and its correcting center conjugation preserve it.

For an arbitrary actual neck word x, let \(\psi(x)\in K_h\) be the free basis substitution f↦h, fixing a,B,d,e. In the splitting of (1), its actual section has the unique form

\[
x=\omega(x)\psi(x),\qquad \omega(x)\in N_R,
\]

with

\[
\omega(a)=\omega(B)=\omega(d)=\omega(e)=1,
\quad\omega(f)=k_1^{-1},\quad\omega(f^{-1})=k_0,
\]

and the full ordered cocycle law

\[
\omega(xy)=\omega(x)\,\operatorname{Ad}(\psi(x))(\omega(y)).
\tag{9}
\]

Here \(\operatorname{Ad}(\psi(x))\) is a genuine graph permutation action generated by the retained T translations and the shift. Equations (8)–(9) therefore give the entire actual K action, at every word and every height, as a specified inner correction followed by a graph action. No source-orbit truncation is involved.

## 6. Consequence for the ambient two-filling problem, and the precise limit

The unfilled common-retract kernel of V is the ordinary free product of the two actual regional kernels, and the corresponding compact statement was proved separately in checkpoint28. Discretely the present result gives a fully explicit faithful presentation

\[
\ker(V\to K)=A(\Sigma_L)*A(\Sigma_R)
             =A(\Sigma_L\sqcup\Sigma_R).
\tag{10}
\]

Both initial relator families lie in this kernel: the retraction kills s, s', k1 and p(k1); each of the five target relations and each theta mate therefore has trivial K image. Their actual ambient normal closure is the normal closure in (10) of **all actual K translates**, with the actual maps and words from B134.

The two factor actions in (10) have their own cocycles (9), with the right marking transported by the complete eta. Although an inner correction can be ignored when taking a normal closure wholly inside one factor, two different factorwise corrections cannot be discarded on a mixed relator. In general they define a partial conjugation of the free product, not a single inner automorphism of it. Removing them would change the actual cross words. This is the exact obstruction to reading (10) as an immediate coordinate graph filling.

Thus the new information is concrete: the two regional kernels are explicit graph groups; the E0 local factors are actual full coordinate subgroups; their complete neck actions and discrepancies are known uniformly. To prove local filling survival or kappa-invariance, one must still control the normal closure of the mixed, eta-marked relations under these actions. Trivial unshifted intersection of Hi and Hj does not supply that control. Neither a filled RAAG presentation nor survival of either local quotient is asserted here.

No assertion is made that the completion of the infinite graph group in (2) equals its induced compact closure. The compact regional kernel can be treated by its actual closure and separate finite-target arguments, but this ordinary presentation does not silently establish that comparison.

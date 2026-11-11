# H.2. Strict categorical completion at the first compactified moduli level

The issue in LM3 F.18 is not the finite-set exodromy equivalence already proved there. It is comparison with finite homotopy types. We give that comparison at $\overline{\mathcal M}_{0,4}\simeq\mathbb P^1$, stratified by its three boundary points. We use the finite-object skeleton of the exit category, with arrows from a boundary point toward the open stratum. The comparison is in profinite stratified homotopy theory; an ordinary nerve of a finite category need not itself be a truncated finite homotopy type.

### H.6. Proved — A cofinal family of strict finite quotient categories

Let $G=F(x,y)$ be the discrete free group, let $c_1=x,c_2=y,c_3=(xy)^{-1}$, and let $I_i=\langle c_i\rangle$. The four-object exit category $C$ has objects $u,p_1,p_2,p_3$, with
$$
\operatorname{Aut}(u)=G,\quad\operatorname{Aut}(p_i)=1,
\quad\operatorname{Hom}(p_i,u)=G/I_i,
$$
and no other nonidentity morphisms. For each finite-index normal $N\triangleleft G$, define $C_N$ by replacing $G$ with $Q_N=G/N$ and $I_i$ with its image $I_{i,N}$. Then $(C_N)_N$ is cofinal in the strict finite-category quotient completion of $C$.

**Proof.** This description of $C$ is the $n=4$ specialization of the transporter model in Jansen (2023, Construction 3.18 and Theorem 6.7), already used in LM3 F.1. A finite congruence on $C$ has a finite group quotient of $G=\operatorname{Aut}(u)$; call its kernel $N$. Its action on each quotient of $G/I_i$ is well-defined. If $g'I_i=gnI_i$ modulo $NI_i$, with $n\in N$, then composition by $n$ is the identity in that quotient, so the two arrows have the same image. Thus $C_N\to C/R$ is defined on every Hom-set and respects composition. This proves cofinality. It also explains why an arbitrary larger stabilizer of a quotient arrow does not introduce an extra completion: refining by the group kernel restores the displayed coset system. $\square$

### H.7. Proved — Finite-coefficient cohomology of the strict nerve

For every finite abelian group $A$ with constant coefficients,
$$
\varinjlim_N H^q(NC_N;A)=
\begin{cases}A,&q=0,2,\\0,&q\ne0,2.
\end{cases}
$$
The degree-two class agrees, under the natural comparison, with the orientation class of $\mathbb P^1(\mathbb C)\simeq S^2$.

**Proof.** The groupoid of arrows $p_i\to u$, under target automorphisms, is the action groupoid of $Q_N$ on $Q_N/I_{i,N}$, and hence has classifying space $BI_{i,N}$. The realization of $NC_N$ is the homotopy pushout of the three diagrams
$$
BQ_N\longleftarrow BI_{i,N}\longrightarrow *.
$$
One can verify this without a nerve-realization interchange theorem: a nonconstant simplex has exactly one initial $p_i$ and then a string of target-group arrows. These are the mapping-cylinder simplices of the displayed action groupoid, and their faces give precisely the homotopy pushout.

Free groups and infinite cyclic groups are good for finite coefficients. In this case goodness follows directly from their one-dimensional free resolutions: the completed augmentation sequence for $\widehat F_2$ has two free profinite generators in degree one and no higher terms, and the procyclic analogue has one. Finite quotient cochains, taken in filtered colimit, compute their continuous cohomology. The topology induced on each $I_i$ is its full profinite topology: each $c_i$ is primitive in $F_2$ and admits a retraction to $\mathbb Z$; reduction of that retraction modulo any $m$ supplies the required finite-index intersections. Therefore
$$
\varinjlim_N H^q(Q_N;A)=H^q(\widehat F_2;A),\qquad
\varinjlim_N H^q(I_{i,N};A)=H^q(\widehat{\mathbb Z};A).
$$
The homotopy-pushout cochain triangle is compatible with $N$. Filtered colimits are exact on abelian groups. In degree zero its restriction map is
$$
A\oplus A^3\longrightarrow A^3,\quad
(a,b_1,b_2,b_3)\mapsto(a-b_1,a-b_2,a-b_3),
$$
which is onto and has diagonal kernel $A$. In degree one it is
$$
A^2\longrightarrow A^3,\quad(s,t)\mapsto(s,t,-s-t).
$$
This is injective; its cokernel is $A$, identified by the sum of the three coordinates. Higher group cohomology vanishes in the colimit. These facts prove the formula. The sum map is the boundary orientation relation of the three-punctured sphere, so its cokernel generator is the sphere's fundamental cohomology class. `fh_finite.py` checks the finite cochain kernel and cokernel for $A=\mathbb Z/m$, $2\leq m\leq39$; the proof applies to every finite $A$. No claim is made that the higher cohomology vanishes at each individual finite stage. $\square$

### H.8. Proved — The full profinite stratified comparison for four points

The nerve of the strict finite-category completion in H.6 represents the profinite stratified homotopy type of $(\mathbb P^1,\{0,1,\infty\})$. In particular, LM3 F.18 has an affirmative answer at $n=4$, with the same strict quotient system that was used for finite-set coefficients.

**Proof.** We supply the higher comparison rather than deducing it solely from H.7's constant cohomology. Let $P$ be the poset with the three boundary strata below the open stratum. It has rank one. Its spatial décollage consists of the four stratum groupoids and the three arrow groupoids; there are no chains of length two with three distinct strata. For the original exit category these spaces are
$$
BG,\quad *,*,*,\quad BI_1,BI_2,BI_3,
$$
with the evident inclusion maps. For the strict quotient system they are
$$
(BQ_N)_N,\quad *,*,*,\quad(BI_{1,N})_N,(BI_{2,N})_N,(BI_{3,N})_N.
$$
The same free-group and cyclic-group goodness argument works for all finite local systems, not only the constant ones in H.7. Together with the identical profinite fundamental groups, it identifies the profinite completions of $BG,BI_i$ with these group-quotient systems. Equivalently, obstruction theory into a finite Postnikov tower is computed by these finite local-system cohomology groups, so the comparison is an equivalence when tested on every $\pi$-finite space. It is compatible with each inclusion $I_i\hookrightarrow G$.

Barwick, Glasman, and Haine (2020), Theorem 2.7.4, reconstruct stratified spaces from their spatial décollages. Their Example 2.6.4 makes the Segal condition vacuous in rank at most one, and Construction 2.8.8 with equation (2.8.9) gives the profinite décollage equivalence. Therefore the objectwise profinite completion just verified is already a profinite stratified space with the universal completion property: there are no higher chains whose homotopy fibre products would require an additional comparison. This proves the desired equivalence of stratified pro-objects. Theorem 10.4.3 is the corresponding topos-theoretic form under its bounded coherent constructible hypotheses. Their Corollary 12.6.7 identifies this with the stratified étale homotopy type over $\mathbb C$. Proposition 10.5.1 identifies its unstratified realization with the profinite completion of the homotopy pushout, namely the sphere. Thus no step interchanges arbitrary completion and an infinite homotopy limit. $\square$

### H.9. Open — What must be added beyond four points

For all $n$, the desired comparison is the equivalence between the nerve of the strict finite-category quotient system of $C_n$ and the profinite stratified completion of $NC_n$. H.8 does not prove it once there are chains of three distinct strata. The first additional case is $n=5$.

Here is a precise sufficient condition, and the point at which our argument stops. For every chain $\tau$ in the stable-tree poset, form the groupoid of lifts of $\tau$ to $C_n$, with natural isomorphisms as arrows. Require that the groupoids obtained from the strict finite quotients form its full profinite homotopy completion, compatibly with chain restriction. In particular one must establish goodness of the stabilizer groups with the topology induced from the finite categorical quotients, and that these quotients compute the iterated homotopy fibre products for consecutive chains. Under this condition the décollage comparison is objectwise an equivalence, hence a stratified equivalence by the décollage reconstruction theorem. This proves the sufficiency of the named condition.

At $n=4$ the only nontrivial chain stabilizers are cyclic and the required topology is supplied by a retraction. At $n=5$ the two-step gluing compatibility is a new assertion; comparing only the stratum groups and finite sets does not prove it. We have computed the complete rank-one cohomology and higher comparison, but do not supply an all-$n$ chain-stabilizer and fibre-product proof. This is the exact remaining comparison, not a claimed counterexample for $n\geq5$.

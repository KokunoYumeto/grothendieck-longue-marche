# Auxiliary results for the remaining centralizer question

These results do not settle C.12. They identify an obstruction to a closed-subgroup-only argument and prove reductions for transitive actions, intrinsic one-dimensional orbits, proper open-orbit centralizers, and globally commuting or locally compact loop-generated groups. The numbered chain now runs through C.50. C.42–C.50 have passed root and independent C review; C.46 and C.48 are the parent's fragments in work/root, and the others are in the adjacent TeX files. All homeomorphism groups have the compact-open topology. The target remains the kernel of the inclusion-induced map in c_scope_audit.md.

## 1. Closed torsion-free subgroups can have nonzero fundamental group

There is a closed torsion-free Polish subgroup of `Homeo(D²,∂D²)` whose fundamental group is `Z`. Consequently the assertions that the hyperbolic identity homeomorphism group is contractible, that a centralizer is closed, and that there are no nontrivial compact circle actions do not, by themselves, prove C.12.

Here is a construction, including its topology. Let

`E = {f∈L¹([0,1],R) : f is integer-valued almost everywhere}`,

with addition and the `L¹` metric. This is a closed subgroup of the separable Banach space `L¹`: every `L¹`-convergent sequence has an almost-everywhere convergent subsequence, and an almost-everywhere limit of integer-valued functions is integer-valued. Hence `E` is a Polish group. For `0<s≤1` put

`D_s f(t)=f(t/s)` on `[0,s]`, and `D_s f(t)=0` on `(s,1]`; put `D_0 f=0`.

Then `||D_s f||₁=s||f||₁`. Dilation is strongly continuous on `L¹`, first for step functions and then by norm approximation, so `(s,f)↦D_s f` is continuous. It contracts `E` to zero and preserves each open norm ball about zero. Thus `E` is contractible and locally contractible.

The subgroup of constant integer functions is a closed discrete copy of `Z`. The quotient

`G=E/Z`

is a Polish topological group, and `E→G` is a covering map: translates by distinct integers of a ball of radius less than `1/3` are disjoint. Since `E` is simply connected, this is the universal cover and `π₁G=Z`. An explicit generator is

`s↦[1_[0,s]]`, `0≤s≤1`.

Its lift starts at the zero function and ends at the constant function `1`. On the other hand, `G` is torsion-free: `n[f]=0` means `nf` is a constant integer, so the integer-valued function `f` is constant and `[f]=0`.

Let `V=L¹([0,1],R)/R`, where the denominator consists of all constant real functions. The natural homomorphism

`G→V`, `[f]_Z↦[f]_R`,

is an isometric embedding for the quotient metrics. Indeed, for an integer-valued `h`, the function `c↦∫|h-c|` is linear on each interval between consecutive integers, and achieves its minimum at an integer median. Therefore

`inf_(c∈R)||h-c||₁ = inf_(n∈Z)||h-n||₁`.

The quotient metric on `G` is complete: for a Cauchy subsequence with successive quotient distances below `2^-k`, choose successive representatives differing by integer constants so that their `L¹` distances are below `2^-k`; these representatives converge in `E`. The whole Cauchy sequence then converges in `G`. The image in the Banach space `V` is consequently closed.

For clarity, the usual linear embedding of a separable Banach space into `C([0,1],R)` can be obtained without any change of topology. Let `K` be the weak-star compact metrizable unit ball of `V*`. The map `v↦(ℓ↦ℓ(v))` is an isometric linear embedding `V→C(K)`. A continuous surjection from the Cantor set to `K`, followed by linear interpolation on the complementary intervals of the Cantor set, gives an isometric linear embedding into `C([0,1])`. Place that interval in the middle third of `[0,1]` and interpolate linearly to zero at the two outside endpoints. This gives a closed isometric linear embedding

`T:V→C₀([0,1],R)`,

where `C₀` here means functions vanishing at both endpoints. Existence of the Cantor surjection follows by nested finite covers of the compact metric space with diameters tending to zero; pullback preserves the sup norm because the map is onto. The interpolation also preserves the sup norm.

On the rectangle `[-1,1]×[0,1]`, define, for `F∈C₀([0,1])`,

`Φ_F(x,y)=(tanh(artanh(x)+F(y)), y)` for `|x|<1`,

and fix the vertical sides. It fixes the whole boundary and satisfies `Φ_F Φ_Q=Φ_(F+Q)`. The map `F↦Φ_F` is continuous because `tanh` is Lipschitz. Its inverse on its image is continuous: evaluation at `(0,y)` recovers `tanh(F(y))`; near any given bounded profile, applying `artanh` recovers `F` uniformly. Its image is closed in the homeomorphism group. In fact a homeomorphism limit preserves the horizontal leaves and their endpoints; the image of the compact segment `{0}×[0,1]` stays a positive distance from the two vertical sides, so the recovered profiles are uniformly bounded and converge uniformly. This proves closedness as well as inverse continuity.

The composite `G→V→C₀([0,1])→Homeo(D²,∂D²)` is therefore a closed topological-group embedding. Extending its elements by the identity outside a closed coordinate disc gives the same kind of embedding into `Homeo₀(U)` for every hyperbolic surface `U`. The extension is a topological embedding because restriction to the compact disc recovers the original maps, and its image is closed because being the identity off that disc is a closed condition. Its generator is ambient-null but nontrivial in `G`.

**This construction cannot itself be the proposed full centralizer.** Its loop is already null in the larger real shear group by the displayed profile contraction. C.39 gives the stronger exact comparison: because the loop has commuting values and is ambient-null, it contracts in every centralizer containing those values. Hence the subgroup, whose generator is nonzero internally, cannot equal such a full centralizer. It remains a proved obstruction to reasoning from closedness, torsion-freeness, or the absence of circle subgroups alone.

## 2. A transitive centralizer cannot give a closed hyperbolic counterexample

For a closed orientable surface `X` of genus at least two, the centralizer in `Homeo(X)` of any transitive subgroup is finite.

Let `K` be the closure of that subgroup in `Homeo(X)`. It remains transitive and is Polish, and taking the closure does not change its centralizer `N`. Fix `x∈X` and put `K_x={k∈K:kx=x}`. The continuous transitive action of the Polish group `K` on the compact metrizable space `X` has an open evaluation map `K→X`. This is the ordinary-action case of the open mapping principle; a primary proof is Gómez–Pinedo–Uzcátegui, *The open mapping principle for partial actions of Polish groups*, arXiv:1709.01977, Theorem 3.5 (the domain for an ordinary action is all of `K`). Thus `K/K_x→X` is a homeomorphism.

Every element of `N` is determined by its value at `x`: commutation gives `n(kx)=k n(x)`. Its possible values are precisely

`N_K(K_x)/K_x ⊂ K/K_x = X`.

For the forward inclusion, `n(x)=kx` implies `K_x=K_(kx)=kK_xk⁻¹`. Conversely, an element of the normalizer gives the well-defined equivariant homeomorphism `gK_x↦gkK_x`. The normalizer of a closed subgroup is closed, so this subset of `X` is closed and hence compact.

Evaluation `N→X` is a homeomorphism onto this closed subset, not merely a continuous injection. Here is the uniform-continuity check. For any `y=g_y x` and a chosen `ε>0`, take a neighborhood `W_y` of the identity in `K` such that every `g_y w g_y⁻¹`, `w∈W_y`, moves all points of `X` by less than `ε/3`. The sets `g_y W_y x` are open neighborhoods of `y`, so finitely many cover `X`, with corresponding elements `g_1,…,g_m`. If `n(x)` is sufficiently close to `n₀(x)`, then each `g_i n(x)` is within `ε/3` of `g_i n₀(x)`. For `z=g_i w x` in the corresponding neighborhood, commutation gives

`n(z)=g_i w n(x)` and `n₀(z)=g_i w n₀(x)`.

The two small movements by `g_i w g_i⁻¹` and the middle `ε/3` bound show `d(n(z),n₀(z))<ε` uniformly in `z`. This proves inverse continuity. Hence `N` is compact.

The action of `N` is free in the sense that only the identity can fix a point: transitivity and commutation propagate one fixed point to all of `X`. Every homeomorphism isotopic to the identity on this closed surface has Lefschetz number `χ(X)=2-2g≠0`, and therefore has a fixed point. Thus

`N∩Homeo₀(X)=1`.

Projection to the discrete mapping-class group is consequently an injective continuous homomorphism on the compact group `N`. Its image is compact and discrete, hence finite. This proves the assertion.

In particular, when the subgroup generated by the values of a based centralizer loop is transitive on `X`, the operator image is contained in this finite centralizer. The finite-action theorem already proved in Part C then contracts the loop equivariantly. Therefore a closed-hyperbolic counterexample cannot arise from a loop whose generated subgroup is transitive. This argument does not classify the lower-dimensional or nonclosed orbits of a general path-generated subgroup, and it supplies no general contraction in that case.

Primary source checked for the open mapping step: https://arxiv.org/pdf/1709.01977, especially the introduction and Theorem 3.5. The rest of this section is the explicit evaluation/normalizer argument above.

## 3. Line centralizers: the exact contraction in C.27

For an arbitrary subgroup \(H\leq\operatorname{Homeo}(\mathbb R)\), every based loop \(f_t\) in its orientation-preserving centralizer has the contraction

\[
m_r(x)=\min_{0\leq u\leq r}f_u(x),\qquad
M_r(x)=\max_{0\leq u\leq r}f_u(x),\qquad
Q_{s,t}(x)=\operatorname{med}(m_{1-s}(x),f_t(x),M_{1-s}(x)).
\]

All maps in this formula are increasing homeomorphisms. For strict increase, the compact family supplies the positive gap \(\min_u(f_u(y)-f_u(x))>0\) whenever \(x<y\); compactness of the inverse family supplies uniform properness at both ends. Compact-uniform continuity gives continuity of the extrema in all parameters. An increasing commuting homeomorphism preserves the extrema; a decreasing one interchanges them. Every line homeomorphism preserves the median, so the contraction commutes with all of \(H\), including its orientation-reversing elements. The initial parameter is the original loop, the final parameter is the identity, and the two endpoints of each loop remain the identity. This proves \(\pi_1 C_{\operatorname{Homeo}^+(\mathbb R)}(H)=0\) without a finiteness or regularity assumption on \(H\). The formula is natural under every line conjugacy.

## 4. The exact plane-orbit reduction in C.28

For a based plane homeomorphism loop, put \(P=\{f_t\}\cup\{f_t^{-1}\}\) and \(G=\langle P\rangle\). Each orbit is exhausted by the nested compact Peano continua \(K_n=P^n x\). Every orbit is open, a point, a Jordan curve, or an intrinsically ordered line that has a continuous injective parametrization by \(\mathbb R\) embedding every compact interval.

The proof does not assume an orbit foliation. If an orbit contains a Jordan curve that some group element moves, an isotopy to that element sweeps the curve across an open set: points in the symmetric difference of the endpoint Jordan domains have different winding numbers, so the curve must pass through them. Transitivity makes the whole orbit open. If the group preserves that curve, it is the entire orbit.

In the remaining case each \(K_n\) is a dendrite. A countable dense set in a dendrite determines each branch point by three points in different complementary components, so its branch points are countable. Every triod point of the whole orbit is already a branch point of some \(K_n\), because its three outer endpoints determine the unique connecting arcs. Transitivity excludes this countable invariant set on a nontrivial arcwise connected orbit. Thus the \(K_n\) are nested arcs, and transitivity also excludes their at most two global endpoints. A cofinal exhaustion by arcs lying in each other's interiors gives the intrinsic line parametrization.

The restricted loop is continuous in this intrinsic line topology: a compact orbit arc lies in some \(K_m\), and all its images lie in the compact arc \(K_{m+1}\), where intrinsic and ambient topologies agree. A commuting operator sends \(K_n(x)\) exactly to \(K_n(hx)\), so it induces a homeomorphism of intrinsic lines. This is the precise map allowing the C.27 contraction on each such orbit. It does not establish that the global subspace topology of a nonclosed line orbit agrees with its intrinsic topology, or that the collection of orbits is a foliation.

## 5. Circle centralizers and the winding map in C.29

For arbitrary \(H\leq\operatorname{Homeo}(S^1)\), the inclusion
\(\pi_1 C_{\operatorname{Homeo}^+(S^1)}(H)\to\pi_1\operatorname{Homeo}^+(S^1)=\mathbb Z\)
is injective. Its image lies in the invariants of \(\mathbb Z\) under the orientation character of \(H\).

The exact covering group is
\(\{F\in\operatorname{Homeo}^+(\mathbb R):F(x+1)=F(x)+1\}\).
It is contractible by real linear interpolation with the identity, and its quotient by integer translations is \(\operatorname{Homeo}^+(S^1)\). A winding-zero loop has a unique based lift which is again a loop. Its commutator with any lift of any element of \(H\) is an integer translation depending continuously on time, hence is identically trivial. C.27 contracts this lifted loop while commuting with every operator lift and with the integer deck translation. It therefore descends to the asserted circle contraction. Median naturality makes this construction independent of circle coordinates, including reversed coordinates.

For a plane loop preserving a Jordan curve, a Schoenflies coordinate sends the curve to the unit circle. Evaluate at two distinct points and take the direction of their difference:

\[
\operatorname{Homeo}^+(\mathbb R^2)\longrightarrow
\operatorname{Conf}_2(\mathbb R^2)\longrightarrow S^1.
\]

If the angular lifts of their images satisfy
\(\alpha(t)<\beta(t)<\alpha(t)+2\pi\), both acquire the same increment \(2\pi n\), and

\[
e^{i\beta}-e^{i\alpha}
=2i e^{i(\alpha+\beta)/2}\sin((\beta-\alpha)/2).
\]

Thus this evaluated loop has exactly the restriction winding \(n\). An ambient-null plane loop maps to a null loop under these continuous maps, so \(n=0\). The canonical lift of a hyperbolic centralizer loop is ambient-null because it comes from the contractible hyperbolic identity homeomorphism group. Consequently C.29 contracts its restriction to every circle orbit, naturally with respect to all commuting operators between such orbits.

## 6. Proper open-orbit centralizers in C.30

For a closed Polish group \(K\) acting transitively on a connected second-countable surface \(V\), let \(N=C_{\operatorname{Homeo}(V)}(K)\). Evaluation gives a homeomorphism from \(N\) onto the closed subset \(N_K(K_x)/K_x\) of \(V=K/K_x\). Multiplication is reversed under this identification: the equivariant map attached to \(aK_x\) is right translation \(kK_x\mapsto kaK_x\).

Here is the extra argument needed for noncompact surfaces. Open evaluation, from the same verified Theorem 3.5 used in C.26, implies sequential microtransitivity: whenever \(x_j\to x\), choose \(k_j\to1\) with \(k_jx=x_j\) by a decreasing identity-neighborhood basis. This uses no local continuous section. If \(n_jx\to nx\), and \(y_j\to y=ax\) stays in a compact subset of \(V\), choose \(b_j\to1\) with \(b_jy=y_j\). Commutation gives

\[
n_jy_j=b_ja n_jx\longrightarrow a n x=n y.
\]

This proves compact-open inverse continuity of evaluation; a direct identical argument also controls inverses. Thus \(N\) is locally compact. It acts freely because one fixed point propagates by transitivity. If \(x_j\to x\) and \(n_jx_j\to y\), then

\[
n_jx=k_j^{-1}n_jx_j\longrightarrow y.
\]

Closedness of the evaluation image gives an element \(n\) with \(nx=y\), and inverse continuity gives \(n_j\to n\). Subsequence extraction over compact subsets of \(V\times V\) proves properness of \((n,z)\mapsto(z,nz)\).

For an open orbit \(O\) from C.28, use the closure of the restricted loop-generated group in \(\operatorname{Homeo}(O)\) as \(K\). The setwise operator stabilizer has the explicit restriction homomorphism \(h\mapsto h|_O\), whose kernel consists of operators fixing \(O\) pointwise. Its image is contained in \(N\), and the closure of that image has the asserted free proper action. This statement retains the compact-open image topology. It does not claim that a dense image regarded as a discrete group acts properly, or that the original group has trivial restriction kernel.

## 7. Fixed-stratum continuity in C.31

The orbitwise C.27/C.29 construction has an exact inverse identity:
\(Q[f]^{-1}=Q[f^{-1}]\). Inversion interchanges the pointwise minimum and maximum of a compact family of increasing line homeomorphisms, and the median is self-dual. The same identity descends through the circle covering. Consequently, on the union \(Y\) of nonopen orbits, the constructed maps and their inverses satisfy

\[
Q_{s,t}(x)\in\{f_u(x):0\leq u\leq1\},\qquad
Q_{s,t}^{-1}(x)\in\{f_u^{-1}(x):0\leq u\leq1\}.
\]

The common fixed set \(Z\) is fixed throughout. Compactness of the two original families gives uniform continuity at every point of \(Z\), for all contraction parameters. This proves continuity of both families along approaches within \(Y\) to \(Z\). It does not prove continuity at a nonfixed line or circle orbit, or control a contraction arriving from an open orbit.

## 8. Discrete proper operators and restriction in C.32

For a free proper action of a **discrete** group \(Q\) on a connected noncompact second-countable boundaryless surface \(O\), the quotient \(p:O\to V=O/Q\) is an actual regular covering with deck group \(Q\). Properness gives only finitely many translates of a compact neighborhood meeting it; freeness then allows a smaller neighborhood disjoint from all of its nonidentity translates. These are the evenly covered neighborhoods.

The exact homeomorphism-group input is Yagasaki, *Homotopy types of homeomorphism groups of noncompact 2-manifolds*, [arXiv:math/0010223](https://arxiv.org/pdf/math/0010223), Theorem 1.1 and compact-pair Lemma 2.1. For a one-point subpolyhedron, the identity component of the point-fixing homeomorphism group is contractible except for the sphere, projective plane and plane among boundaryless surfaces. Local point-moving sections give the evaluation fibration, so evaluation on the homeomorphism group induces an injection on \(\pi_1\) for every other surface. A noncompact connected covering cannot have sphere or projective-plane base; a plane base forces the trivial covering.

A centralizer loop \(f_t\) descends by the exact equation \(b_tp=pf_t\). If \(f_t\) is null in \(\operatorname{Homeo}(O)\), its evaluation loop is null, hence the evaluation loop of \(b_t\) is null and the evaluation injection fills \(b_t\) in \(\operatorname{Homeo}(V)\). For a filling \(B:D^2\to\operatorname{Homeo}(V)\) based at the identity, lift the map

\[
(x,z)\longmapsto B_z(p(x))
\]

on \(O\times D^2\), starting with the identity lift. The covering criterion applies because its fundamental-group image is exactly \(p_*\pi_1(O)\). Lifting the inverse family and using uniqueness proves that every lift is a homeomorphism. The same uniqueness proves exact agreement with \(f_t\) on the boundary and commutation with every deck operator. This establishes the inclusion injection \(\pi_1 C_{\operatorname{Homeo}(O)}(Q)\to\pi_1\operatorname{Homeo}(O)\).

C.32 also proves that an ambient-null plane loop preserving any connected open \(O\) restricts to a null loop there. Yagasaki contracts the identity homeomorphism group unless \(O\) is a plane or open annulus. In those exceptions the group has fundamental group \(\mathbb Z\), and the C.29 two-point winding map detects a model rotation with value one. That map extends to all ambient plane homeomorphisms, so the ambient-null loop has zero restricted class. This includes the plane exception, whose point-evaluation map by itself would not detect its rotation loop.

## 9. All proper open-orbit operators in C.33

For every closed locally compact \(Q\leq\operatorname{Homeo}(O)\) acting freely and properly on a connected noncompact second-countable boundaryless surface, the same inclusion is \(\pi_1\)-injective. C.32 handles the discrete case.

The remaining structural inputs have now been checked directly in primary sources. Pardon, *The Hilbert–Smith conjecture for three-manifolds*, [author PDF](https://web.math.princeton.edu/~jpardon/manuscripts/08_hilbertsmith.pdf), Theorem 1.5 with the introductory reduction, makes \(Q\) a Lie group by applying the theorem to the explicit faithful action \(q(x,s)=(qx,s)\) on \(O\times\mathbb R\). Palais, *On the existence of slices for actions of non-compact Lie groups*, DOI [10.2307/1970335](https://doi.org/10.2307/1970335), Theorem 2.3.3, supplies the free principal-bundle charts. The original author-uploaded text was checked. The same charts and their inverse are explicitly proved in Kramer–Murat García, *Fibrations and Coset Spaces for Locally Compact Groups*, DOI [10.1007/s00031-025-09903-5](https://doi.org/10.1007/s00031-025-09903-5), Theorem 3.7. No smooth structure on the action is assumed.

If \(\dim Q^0=2\), its orbits are open by invariance of domain, hence it is transitive. Freeness forces \(Q=Q^0\), and the centralizer is the group of right translations. Evaluation is a homeomorphism to \(O\), proving the needed injection.

If \(\dim Q^0=1\), put \(A=Q^0=\mathbb R\) or \(\mathbb R/\mathbb Z\). Its quotient is genuinely a one-manifold. The elementary verification is that a slice \(S\) with \(S\times(-1,1)\) a surface is locally path connected, and each open embedded arc in \(S\) is open by invariance of domain. At a point, an arc either has a second branch, giving an open arc through that point, or gives a half-interval neighborhood, whose product has the wrong local second homology. Thus the quotient is a line or circle. The principal \(A\)-bundle is trivial: local interval sections can be joined; on a circle, connectedness of \(A\) corrects the endpoint discrepancy. This gives the exact coordinates \(O=A\times B\).

The component group \(\Delta=Q/A\) acts freely and properly on \(B\). Freeness follows by correcting a fibre displacement with an element of \(A\); properness follows by lifting convergent basepoints through local sections, correcting representatives by \(A\), and applying properness on \(O\). Hence \(\Delta\) is trivial, is \(\mathbb Z\) acting by translation on a line, or is a finite cyclic group acting by rotation on a circle. In the latter case \(A=\mathbb R\), because the circle-times-circle total space would be compact.

A representative generator has the exact form \(q(a,b)=(\lambda a+\tau(b),\beta b)\). On a line base, choosing \(c(b+1)=\lambda c(b)+\tau(b)\) and replacing \(a\) by \(a-c(b)\) removes \(\tau\). On a circle base, write \(q^n=T_{a_0}\). The relations imply \(\lambda^n=1\) and \(\lambda a_0=a_0\). For \(\lambda=1\), replacing \(q\) by \(T_{-a_0/n}q\) makes \(q^n=1\). For \(\lambda=-1\), \(n\) is even and \(a_0=0\) already. Averaging the resulting finite affine action gives a continuous invariant fibre origin. Thus both signs of \(\lambda\) are retained in the coordinate formula \(q(a,b)=(\lambda a,\beta b)\).

The centralizer is then exactly

\[
h(a,b)=(a+\phi(b),\psi(b)),\qquad
\phi(\beta b)=\lambda\phi(b),\qquad
\psi\beta=\beta\psi.
\]

These coordinates give a topological product of the indicated function space and base centralizer; the inverse is \((a,b)\mapsto(a-\phi(\psi^{-1}b),\psi^{-1}b)\). Real-valued \(\phi\) contracts by scaling. For circle-valued \(\phi\), the evaluation of an ambient-null loop makes its based real lift a loop, and the integer discrepancy in its lifted equivariance equation vanishes by continuity from time zero; scaling that lift gives the contraction. C.27 contracts the line-base loop; C.29 contracts the circle-base loop because evaluation forces winding zero. The circle fibre with an additional \(\mathbb Z\)-translation on its line base is included with its exact translation-centralizer constraint.

Combining C.30, C.32 and C.33 gives an intrinsic equivariant contraction on **every open orbit** of the canonical hyperbolic plane loop, retaining the kernel of the original restriction homomorphism. These contractions have no established uniform frontier estimate.

## 10. Full nonopen-locus continuity in C.34

C.34 proves the previously missing continuity at all nonfixed line and circle strata. The proof uses the path action to exclude folds; convergence of compact sets alone is never used to infer their order.

At any nonfixed point \(q\), take a component \((a,b)\) of the times for which \(f_t(q)\ne q\). A short path

\[
g_s=f_{a+s\eta}f_a^{-1}
\]

starts at the identity and moves \(q\) a nonzero amount in one intrinsic direction. Its inverse path supplies the other direction. Shortening the interval keeps both paths arbitrarily small on compact sets and on the intrinsic neighborhood of \(q\). Each value is a product of two original generators, so it takes \(K_n(x)\) into \(K_{n+2}(x)\); the C.28 argument proves intrinsic continuity of all these point tracks.

Straighten a compact arc of a limit orbit. If nearby intrinsic arcs fold a definite distance past the interval between their limiting endpoints, choose a horizontal minimum or maximum on the offending subarc. At a minimum, both endpoints stay a definite distance to the right. In a small rectangle around the limiting minimum, the two first-exit points in the intrinsic directions therefore lie on the right edge. The intervening cap is an intrinsic subarc whose endpoints are outside the open rectangle. A short group path at the nonfixed limiting point moves it left while remaining in that rectangle. By compact-family continuity the same holds for nearby minimum points. Their intrinsically continuous paths cannot leave the cap without meeting one of its two first-exit endpoints, so their endpoints cannot move left of its minimum. This contradiction excludes the fold. The same argument excludes a whole Jordan curve collapsing to a nondegenerate interval.

Consequently, for subarcs inside a fixed finite word-track near a limit intrinsic line,

\[
u_j\to u,\quad v_j\to v,\quad
z_j\in[u_j,v_j]_j,\quad z_j\to z
\quad\Longrightarrow\quad z\in[u,v].
\]

This includes coincident limiting endpoints. A median is the common point of three pairwise intervals, so the implication proves continuity of medians. The prefix-track sets also converge in Hausdorff distance. Any limiting pair of their unordered endpoints must bound exactly the limiting prefix interval, by the same implication. This proves continuity with varying contraction parameters as well as varying points.

For a circle limit, choose a collar annulus \(W\) and a small disc \(V\) around the initial point such that the entire map \([0,1]\times V\to W\), \((t,x)\mapsto f_t(x)\), is defined in the collar. Lift that exact map to the annular universal cover. Its endpoint deck integer is continuous in \(x\), and is zero at the limit circle by C.29, so all these lifted point tracks are closed. Their limiting range is an interval on the lifted circle line. Each nearby track lies on a lifted intrinsic interval or on a lifted Jordan curve; the latter whole-curve case is excluded by the same cap argument. For that argument only a small injective covering rectangle is used: the original short group path is lifted there while its tracks stay in the chart. No global group action on the collar or on its cover is assumed.

The resulting formulas agree with the actual C.27 intrinsic-line and C.29 based-circle-lift medians. C.31 handles fixed points and gives the exact inverse-loop identity. Thus \(Q_{s,t}\) is a jointly continuous family of homeomorphisms of the full closed nonopen locus \(Y\), with jointly continuous inverse and exact operator equivariance.

When the canonical hyperbolic lift has no open orbit, \(Y\) is the entire plane. The maps commute with all deck transformations and descend by \(\overline Q_{s,t}p_U=p_UQ_{s,t}\) to a centralizer null-homotopy on the original surface. This proves the no-open-orbit case without changing the comparison map.

## 11. The fixed median extension is obstructed: C.35

The particular median family need not extend through the exact open-orbit centralizer. C.35 proves this with an explicit action and restriction morphism.

On the closed simplex \(\Delta=\{x,y,z\ge0:x+y+z=1\}\), let

\[
T_{a,b}(x,y,z)=
\frac{(e^a x,e^b y,z)}{e^a x+e^b y+z}.
\]

Double the simplex along its boundary to a sphere, then remove one fixed vertex. This gives a plane action. Each open triangle is a free proper \(\mathbb R^2\)-orbit in logarithmic coordinates \((\log(x/z),\log(y/z))\). The three edges are intrinsic line orbits with translation characters \(a,b,a-b\).

The based parameter loop \(0\to(1,1)\to(1,0)\to0\) generates all of \(\mathbb R^2\). It contracts globally and equivariantly by scaling its two parameters. At prefix endpoint \(r=1/3\) and current time \(t=2/3\), however, the C.34 median prescribes edge values \((1,0,0)\).

The exact boundary restriction morphism from the interior centralizer is

\[
\mathbb R^2\longrightarrow\mathbb R^3,\qquad
(A,B)\longmapsto(A,B,A-B).
\]

Its image is the kernel of \((r_1,r_2,r_3)\mapsto r_1-r_2-r_3\), whose value on \((1,0,0)\) is \(1\). Thus that single prescribed median map cannot extend equivariantly over either adjacent open orbit. Allowing the sheet exchange of the double gives the same restriction morphism and does not change the obstruction.

The executed rational certificate is work/part_b/code/c35_median_extension_certificate.py, with its adjacent JSON output. It records the prefix extrema, current values, median values, restriction matrix, annihilator, and residual \(1\). The explicit global scaling contraction proves that this is an obstruction to the fixed prescription, not a nontrivial centralizer fundamental-group class.

## 12. Compatible dimension-two closures in C.36

Let \(O\) be an open orbit for which the proper closed operator image \(Q_O\) has dimension two. C.33 identifies \(N_O=C_{\operatorname{Homeo}(O)}(Q_O)\) with \(Q_O^{\mathrm{op}}\), acting simply transitively on \(O\). The restricted original group \(G|_O\) is all of \(N_O\): transitivity finds an element with any prescribed evaluation, and simple transitivity makes that element unique on the orbit.

Set \(L=\overline G\) in the plane homeomorphism group. Limits and inverse limits preserve \(\partial O\) and hence \(O\), so restriction gives a continuous surjective homomorphism \(r_O:L\to N_O\). It is open by the verified Polish-group open mapping principle. Its kernel fixes \(\overline O\) pointwise. Therefore the map

\[
N_O\times\overline O\longrightarrow\overline O,\qquad
(n,z)\longmapsto lz\quad(r_O(l)=n)
\]

is well defined and jointly continuous, because \(r_O\times\mathrm{id}\) is an open quotient. A continuous section is not needed. Every \(n\) has a preimage in the original \(G\), so this closure action preserves the original boundary orbits and has exactly their original \(G\)-action.

The universal cover of \(N_O\) is additive \(\mathbb R^2\) or the positive affine group, with product \((a,b)(a',b')=(a+a',b+e^a b')\). In the latter case

\[
\exp(u,v)=\left(u,v\frac{e^u-1}{u}\right)
\]

is a global diffeomorphism, with the scalar factor interpreted as \(1\) at \(u=0\). The based restriction loop has a closed universal-cover lift by C.32 and the evaluation homeomorphism. Thus \(\exp((1-s)\log\widetilde n_O(t))\), projected to \(N_O\), gives a continuous contraction on the whole closure.

On a common nontrivial boundary orbit \(B\), the faithful images of adjacent \(N_O\)'s are the same set \(G|_B\). C.36 proves that their actual topologies agree: the homogeneous one-manifold orbit topology matches the C.28 intrinsic topology on compact arcs. A faithful transitive connected Lie group of dimension at most two on that one-manifold is the translation group, the rotation group, or the positive affine group. One or two point evaluations recover its group parameters continuously, so the image topology is its intrinsic compact-open topology.

The adjacent groups therefore have continuous quotient homomorphisms onto one common Lie group \(M_B\). Their unique based universal-cover lifts take the two original loop lifts to the same path. Naturality of the exponential, together with its global injectivity on these covers, makes the two contractions equal on \(B\). They agree on every overlap, including the dependent edge characters of C.35. The same calculation proves transport equivariance under the original operator group.

Finite closed-set pasting yields a jointly continuous family with jointly continuous inverse on every finite union of these closures. No estimate across an infinite accumulating family is supplied by that pasting argument.

## 13. Uniform dimension-two accumulation in C.37

The signed-measure theorem in Grandoni–Ravi–Singh–Zenklusen, *New approaches to multi-objective optimization*, Mathematical Programming 146 (2014), 525–554, DOI 10.1007/s10107-013-0703-7, gives an exact three-word estimate. Theorem 4.7 and its full proof in §4.3.2 of the [author version](https://people.idsia.ch/~grandoni/Pubblicazioni/GRSZ13mp.pdf) were independently read by three agents. For a planar continuous path from 0 to v, each rv is a difference of two path points or v plus such a difference. Apply the two-signed-measure theorem to polygonal derivatives and pass through uniform approximation. For the affine group, conjugate an endpoint (a,b) with a nonzero to (a,0); coordinates (a′/a,exp(−a′)b′) turn its left fractional powers into horizontal translations. Pure translations use (b′/b,a′). This proves the group word equation in the simply connected group, and hence with the specified based lift in a universal cover.

The compact family of actual plane isotopies is

\[
W_{\epsilon,a,b,t}(u)=f_{ut}^{\epsilon}f_{ub}f_{ua}^{-1},
\qquad \epsilon\in\{0,1\},\quad 0\leq a,b\leq t\leq1.
\]

Every fractional action on a dimension-two open orbit is its endpoint for suitable parameters, with equality of based universal-cover endpoints. Thus the estimates control original global maps and their isotopies, independently of the orbit.

Put \(X_2=\overline{\bigcup_{\dim Q_O=2}O}\). The metabelian identity holds for G on every such open orbit, hence on X₂. Each nontrivial nonopen orbit B in X₂ therefore has a path-connected transitive metabelian image. C.37 proves this image is R-translations, S¹-rotations, or the positive affine group. Its path-connected abelian derived subgroup, when nontrivial, has no common fixed point by transitivity; all its connected nontrivial orbits are open intervals, forcing it to be transitive. Free abelian evaluation, the Polish open mapping principle, and the one-dimensional Lie classification then give translations and the exact affine normalizer.

For points \(x_i\) in open orbits approaching a point of B, choose a convergent subsequence of the representing compact word isotopies. Let w be the limiting endpoint and let \(r_i\to r,t_i\to t\). For every fixed positive integer n, the residual

\[
\widetilde w_i^n\widetilde n_i(t_i)^{-\lfloor nr_i\rfloor}
\]

is again a fractional power and hence another member of the same three-word family. Identities pass to all of B by evaluating at \(h x_i\to h x\), for every fixed \(h\in G\). The limiting endpoint w commutes with \(f_t|_B\). On a line, logarithms of all residual words stay in one compact set, so division of the exact residual equation by n forces
\(\log w=r\log(f_t|_B)\).

On a circle, let θ be the based real rotation angle of the original restricted loop. The residual word equation must be checked over R. Its canonical word isotopy is a null loop in each open-orbit Lie group because the equality holds in the specified universal cover. Evaluate at two points \(x_i,hx_i\) approaching two distinct boundary points. Their difference-direction winding is zero and remains zero under uniform convergence. C.29 then gives the real residual identity
\(nA-m_n\theta(t)=C_n\), where \(|C_n|\leq3\max|\theta|\) and \(|m_n-nr|\leq1\). Division by n gives \(A=r\theta(t)\), even when the endpoint rotation is identity and its based angle is a nonzero integer.

These identities identify every subsequential limit from the dense open union. A diagonal approximation proves joint continuity on all of X₂. The inverse original loop gives the exact inverse family and its joint continuity. Equivariance holds on the dense open union and extends to X₂. Thus C.37 handles all infinite accumulation inside X₂.

## 14. The nonabelian one-dimensional case in C.38

For a transitive nonabelian subgroup T of the increasing homeomorphism group of an intrinsic line or circle B, C.38 identifies its full centralizer N, with the intrinsic compact-open topology, as discrete: N is trivial or infinite cyclic on a line and finite cyclic on a circle.

The closure L of T is Polish and transitive. The verified open orbit-map theorem identifies L/L_b with B. Evaluation identifies N homeomorphically with the closed normalizer quotient N_L(L_b)/L_b, and the exact microtransitivity argument of C.30 proves that its free action is proper. Thus N is locally compact. Its faithful product action on B times R² gives a Lie group of dimension at most one. A one-dimensional identity component would have open free orbits and would be transitive; its translation centralizer is abelian, forcing the original T to be abelian. Consequently N is discrete. The actual quotient B→B/N is a regular covering of a connected one-manifold, which gives the stated cyclic possibilities.

For the original operator stabilizer H_B, restriction has an exact kernel:

\[
1\longrightarrow K_B\longrightarrow H_B
 \longrightarrow P_B\longrightarrow1.
\]

Here K_B fixes B pointwise, P_B is the actual image subgroup of N, and B→B/P_B is the actual regular covering with deck group P_B. The intrinsic topology is retained. No continuity assertion from an ambient subspace topology to the topology of a recurrent intrinsic line, and no transverse extension conclusion, is added.

## 15. The global commuting-values theorem C.39

For a based ambient-null plane loop with pairwise commuting values, C.39 constructs an equivariant contraction on the entire plane, including every change and accumulation of orbit types. It applies to every operator subgroup commuting with the original loop.

The loop-generated group G is abelian. On each open orbit its closure in the homeomorphism group is abelian, transitive, and free. Polish open evaluation is a homeomorphism to that orbit; this makes the actual image a locally compact abelian Lie group. Transitivity and freeness show that the original image already equals its closure. The possibilities are R² or R×S¹. On an intrinsic line or circle the same argument gives R or S¹. Thus the simply connected actual image on every orbit is a vector group of dimension at most two.

The original restricted loop has a closed based universal-cover lift: C.32 and evaluation prove this for an open orbit, C.29 proves it for a circle, and a line has no covering kernel. Scale that lifted vector by r. The universal three-word lemma from C.37 represents each scaled value by the same compact family of actual global word isotopies. In dimension one the intermediate value theorem even gives a one-word representation. All representations retain the exact based universal-cover endpoint.

For a sequence of points in arbitrary, possibly different orbit types, compactness gives a subsequential word limit. On an open limit orbit all sufficiently nearby points already lie in it. At a fixed limit every word fixes the point. At a limiting line or circle, the integer residuals obtained by subtracting floor(nr) times the original lift are again represented by the same compact word family. On a line the bounded real residual equation determines the scaled parameter uniquely.

For a circle, the residual word isotopy is null in each actual image group of the approximating orbit, whether that orbit is open, a line, or a circle. Evaluation at two points of that orbit has difference-direction winding zero. Passing to two distinct limiting points preserves this integer. C.29 therefore gives an equality of real lifted angles, and division by n determines the unique limit. This includes an endpoint that is the identity rotation while its based real angle is a nonzero integer. Thus the proof controls the actual lifted residual rather than only its projection modulo integers.

Applying the same construction to the inverse original loop proves exact inverse continuity. Continuous isomorphisms of the actual abelian Lie images have linear based covering lifts, so scaling is natural under every commuting operator. This proves the global homeomorphism contraction.

For a connected admissible surface U, lift an actual ambient filling through the explicit map D²×Ũ→U. Lift its inverse family too; covering uniqueness makes every slice a homeomorphism. The resulting closed plane loop centralizes all operator lifts, including deck transformations. Both commutators with operator lifts and pairwise commutators of loop values are continuous deck-valued families starting at the identity, hence vanish identically. The global plane contraction descends through the actual covering. Therefore every inclusion-kernel class with a commuting-valued representative is zero on every connected admissible surface. The independent audit is retained in work/part_c/review_c39.txt.

## 16. The locally compact generated-closure theorem C.40

Let L be the closure in Homeo(U) of the subgroup generated by a based centralizer loop. It has exactly the induced compact-open topology. The centralizer is closed, so L remains inside it; finite products of the original paths show that L is connected. For locally compact L, its faithful action on U×R and the verified Hilbert–Smith theorem give a connected Lie group with this same topology.

Borel's principal theorem gives an actual multiplication homeomorphism K×Rᵈ→L, with connected maximal compact K and closed real one-parameter factors. Scaling those real coordinates is an explicit strong deformation retraction fixing the identity. It turns the given loop into a based loop in K through actual centralizer elements.

Averaging an inner product over the compact adjoint action gives a bi-invariant metric. On the universal covering group of K the connection on left-invariant fields is one half of the bracket; its geodesics are complete one-parameter subgroups. Hopf–Rinow gives a geodesic from the identity to the endpoint of the lifted loop. The two paths have the same endpoints in a simply connected space, so their projections are based homotopic. The projected geodesic is a one-parameter loop and hence has commuting values. This entire homotopy stays in the centralizer. C.39 contracts it when the original exact ambient class is zero.

The primary source is Armand Borel, *Sous-groupes compacts maximaux des groupes de Lie*, Séminaire Bourbaki 1 (1952), exposé 33, pp.271–279, [original scan](https://www.numdam.org/article/SB_1948-1951__1__271_0.pdf). The product notation and displayed decomposition were visually checked in §1, p.271. The semisimple-cover and general induction reductions were read in §§3–4, pp.277–278. The PDF and rendered pages are retained under work/part_b/research/borel1952_*. Root and C independently checked the source and argument; C's audit is work/part_c/review_c40.txt.

The result covers every loop contained in a closed locally compact centralizer subgroup. It proves that a locally compact full centralizer has injective inclusion on fundamental groups. It does not change the topology of any nonlocally compact subgroup or assert a representative reduction there.

## 17. A dense operator orbit: C.41

C.41 proves injectivity of the exact centralizer inclusion on fundamental groups for every connected admissible surface whenever the operator subgroup H has a dense orbit. No local compactness condition is imposed on H or on the loop-generated group.

For the ambient-null plane lift, let G be generated by the loop. Commutation gives h(Gx)=G(hx). If G has no open orbit, C.34 contracts the loop globally. Otherwise the union V of its open orbits is a nonempty H-invariant open set. It meets the dense H-orbit D, hence contains D and is dense. For each open G-orbit O choose y in D∩O. The exact equality Hy∩O=H_Oy follows because two G-orbits meeting at hy must coincide. Thus H_Oy is dense in O.

The actual closed restriction image Q_O acts freely and properly by C.30. Its orbit Q_Oy is closed and contains that dense subset; it is therefore all O. C.33 then gives dimension two. Every open G-orbit belongs to U₂, so X₂ is the entire plane and C.37 is the required global contraction.

On a general admissible surface, the ambient filling lifts through D²×Ũ→U as in C.39. The full operator lift group has orbit exactly p⁻¹(Hx), which is dense because the covering is open. Continuous deck-valued commutators are identically the identity, so the plane contraction retains every operator lift and descends to the original centralizer. The independent audit is work/part_c/review_c41.txt.

## 18. Proved auxiliary lemma: equivariant maps and operator limits

Let G be generated by the plane loop, let L be its closure in the ambient plane homeomorphism group, and let O be an open G-orbit. Fix x∈O and put J=L_x. The group L preserves O: all elements of G preserve its boundary, and forward and inverse limits preserve that closed boundary. A limit sends each point of O into its closure and away from its boundary, hence into O; applying the same argument to the inverse gives equality. Thus L is a Polish group acting continuously and transitively on O.

The already verified open orbit-map theorem makes

\[
q:L\longrightarrow O,\qquad q(l)=lx
\]

an open quotient and identifies O with L/J. Define the closed plane subset

\[
E=\operatorname{Fix}(J)=\{z:jz=z\text{ for every }j\in J\}.
\]

For z∈E the formula

\[
\Phi_z(lx)=lz
\]

is well defined: l₁x=l₂x implies l₂⁻¹l₁∈J, which fixes z. The jointly continuous map E×L→R², (z,l)↦lz, descends through the open quotient id_E×q. It therefore defines a jointly continuous map E×O→R².

Let Map_L(O,R²) carry the subspace compact-open topology from the space of continuous maps. Evaluation at x gives a homeomorphism

\[
\operatorname{Map}_L(O,\R^2)\longrightarrow E.
\]

To check bijectivity, equivariance forces every map with value z at x to equal Φ_z, and its value is fixed by J. Conversely Φ_z is L-equivariant. Evaluation is continuous. Its inverse is continuous by the compact-open exponential law applied to the displayed joint map; O is locally compact Hausdorff. Thus this statement retains the actual topology on both sides.

Every global homeomorphism h commuting with G commutes with L as well, and its restriction to O is Φ_(hx). Consequently, for any sequence of such operators with h_nx→z, one has z∈E and

\[
h_n|_O\longrightarrow\Phi_z
\]

uniformly on every compact subset of O. This is convergence of continuous maps; no inverse homeomorphism limit is asserted.

The range is the original G-orbit Gz. For l∈L choose g∈G with gx=lx, using transitivity of G on O. Then g⁻¹l∈J fixes z, giving lz=gz. Hence Lz=Gz exactly. In particular the limit map is constant when z is a common fixed point, and is a surjective equivariant map onto the indicated intrinsic line or circle when z lies on such an orbit. Continuity into the intrinsic line can also be checked: the image of each compact coordinate disk in O is a compact Peano continuum in that orbit. It contains neither a Jordan curve nor a triod by C.28, so it is a point or a compact arc. The intrinsic and ambient topologies agree on that arc. Such disks are neighborhoods of every point of O, proving the intrinsic continuity. For a circle its intrinsic and ambient subspace topologies already agree.

These limits impose an exact extension constraint. Suppose h_n belongs to the original operator subgroup H, u is a global H-equivariant homeomorphism, and u(O)=O. For w∈O, passing to the limit in h_nu(w)=u h_n(w) gives

\[
\Phi_z(u(w))=u(\Phi_z(w)).
\]

It follows that u preserves the range Gz and intertwines this particular quotient map with its boundary restriction. The lemma proves these necessary maps and identities. It does not construct a simultaneous homotopy satisfying all of them or prove a relative extension theorem.

### The quotient is open in the intrinsic one-dimensional topology

For a line or circle range B=Gz, the preceding map is more precisely the actual quotient

\[
\Phi_z:O=L/J\longrightarrow B=L/L_z,
\qquad lJ\longmapsto lL_z.
\]

Here the topology on B is its C.28 intrinsic topology. To verify this identification, first note that every l∈L maps B to B. Its restriction is an intrinsic homeomorphism: ambient homeomorphisms carry each compact arc to a compact arc, and C.28 identifies these with the intrinsic intervals.

For each b=gz choose w=gx∈O. Then l b=Φ_z(lw), so the already proved intrinsic continuity of Φ_z makes evaluation l↦lb continuous. On an intrinsically ordered line, pointwise convergence of homeomorphisms to a homeomorphism implies uniform convergence on compact intervals: choose a finite ordered partition whose images under the limiting map have small consecutive gaps and use monotonicity between partition points. Orientation is constant near the limiting homeomorphism, as detected on two points. Apply the same argument after inversion in L. The circle version uses a finite cyclic partition and three points to fix orientation. Thus the homomorphism L→Homeo(B) is compact-open continuous and the intrinsic action is jointly continuous.

The Polish orbit-map theorem now applies to the transitive action on the Polish one-manifold B, identifying it with L/L_z and making L→B open. Since J⊂L_z, the displayed quotient map Φ_z is open as well. Its fibre over z is the actual homogeneous space L_z/J. No local product chart or one-manifold description of that fibre has yet been proved.

### Fixed-frontier extension with compact quotient support

Continue with one open G-orbit O and its operator stabilizer H_O. Let Q be the closed restriction image in Homeo(O), and put V=⋃_(h∈H)hO. Suppose every point of ∂V is fixed by G. Let P be a compact metrizable parameter space and let ψ_p be a continuous family in C_Homeo(O)(Q), including continuous inverses. Assume the support of the whole family projects into one compact subset C of the proper quotient O/Q.

The family has an actual H-equivariant extension

\[
E_p(hw)=h\psi_p(w)\quad(h\in H,\ w\in O),
\qquad
E_p=\mathrm{id}\text{ on }\R^2\setminus V.
\]

This is well defined because two choices of h for one component differ by H_O and ψ_p centralizes its restriction image. It is an orbitwise bijection, and the same formula with ψ_p⁻¹ gives its inverse. It commutes with H. The remaining point is joint continuity at ∂V.

The free proper Lie action of Q has local principal-bundle sections by the exact C.33 result. Finitely many such sections over the compact set C provide a compact K⊂O with QK containing the support of every ψ_p. The sets ⋃_(p∈P)ψ_p(K) and ⋃_(p∈P)ψ_p⁻¹(K) are compact by joint continuity.

Take p_i→p and y_i→z∈∂V. Points unchanged by E_(p_i) need no further argument. For the other points write y_i=h_iq_i k_i with h_i∈H, q_i∈Q, and k_i∈K. Pass to a subsequence with k_i→k. Because the actual restriction image of H_O is dense in Q, choose s_i∈H_O approximating q_i at both k_i and ψ_(p_i)(k_i), closely enough that after applying h_i the two errors are below 1/i. Put a_i=h_i s_i∈H. Then

\[
a_i k_i\longrightarrow z,\qquad
E_{p_i}(y_i)-a_i\psi_{p_i}(k_i)\longrightarrow0
\]

in the Euclidean metric.

Microtransitivity at k gives l_i→1 in L with l_i k=k_i. Since each a_i commutes with L,

\[
a_i k=l_i^{-1}a_i k_i\longrightarrow z.
\]

Choose b∈L with bk=x. Every point of ∂V is fixed by G and hence by its closure L, so

\[
a_i x=b\,a_i k\longrightarrow bz=z.
\]

The proved quotient/evaluation lemma now makes a_i converge uniformly on every compact subset of O to the constant map with value z. Apply this to the compact set ⋃_pψ_p(K). It gives E_(p_i)(y_i)→z. The inverse family has the same uniform support and the same argument applies to ⋃_pψ_p⁻¹(K). This proves both joint continuity statements. Together with the already explicit inverse, it proves that every E_p is a global homeomorphism and that the parameter map has the actual compact-open group topology.

When O/Q is compact, the support condition is automatic for any compact parameter family. The intrinsic contraction of f_t|O supplied by C.32–C.33 therefore extends over V and its fixed frontier in this manner. It contracts the actual cut-off loop equal to f_t on V and to the identity off V. The argument covers arbitrary accumulation within this H-saturation. It supplies no uniform conclusion across infinitely many unrelated H-saturations and imposes no prescription at a nonfixed frontier point.

## 19. The exact abelian C.26 subgroup cannot be a full centralizer

Let G₀ denote the particular closed torsion-free Polish subgroup embedded by C.26 in a coordinate disk of an admissible surface. Its specified generator loop has pairwise commuting values, represents a nonzero element of π₁G₀, and is ambient-null by the explicit larger real-shear contraction.

For every operator subgroup H with G₀⊂C_A(H), C.39 applies to that same loop. Thus the actual inclusion

\[
\pi_1(G_0,1)\longrightarrow\pi_1(C_A(H),1)
\]

sends its nonzero specified generator to zero. In particular C_A(H) cannot equal this embedded G₀ with its induced topology: under that equality the displayed inclusion would be the identity on π₁G₀. This is an explicit consequence for the proposed realization of the exact C.26 subgroup, rather than an inference from its torsion-free or closed-subgroup properties. The broader centralizer problem is unchanged.

## 20. Verified fibre facts and an exact disconnected-fibre example

The quotient in §18 has additional ambient homogeneity, with no change of topology. Write \(F=\Phi_z^{-1}(z)\) and \(K=L_z\). For \(p,q\in F\), choose \(l\in L\) with \(lp=q\), using transitivity on O. Equivariance gives \(lz=\Phi_z(lp)=\Phi_z(q)=z\), so \(l\in K\). Hence K acts transitively on F. If p and q belong to one connected component C of F, the same l sends C onto C, since its image is a component containing q. Thus the component stabilizer acts transitively on C by actual ambient homeomorphisms.

The official primary source Beverly Brechner and Timo Erkama, *On topologically and quasiconformally homogeneous continua*, Annales Academiae Scientiarum Fennicae, Series A I Mathematica 4 (1978/1979), 207–208, DOI 10.5186/aasfm.1978-79.0402, was read in full at [the publisher PDF](https://www.acadsci.fi/mathematica/Vol04/vol04pp207-208.pdf). Their Theorem 2 states that a nondegenerate proper compact subcontinuum of the sphere homogeneous with respect to homeomorphisms defined on neighborhoods of that continuum is a simple closed curve. Applying the exact component action just proved shows that every nondegenerate compact component of F is a circle. This application does not classify a noncompact component or prove a local product chart.

There is also a direct restriction on embedded fibre circles. A circle contained in a fibre cannot bound a disk contained in O: lift the circle-valued quotient to a real function on the disk when necessary. Its boundary value is constant, so a nonconstant function has an interior maximum or minimum, contradicting openness; a constant disk contradicts openness as well. For a line-valued quotient, two parallel circles in the same fibre cannot cobound a compact annulus contained in O, by the same argument. For a circle-valued quotient, a real lift on that annulus exists, but its two boundary constants may differ by a nonzero integer. Therefore the last annulus exclusion applies only when those lifted constants agree.

Disconnected whole fibres do occur even in the exact loop and commuting-operator setting. The following example supplies all maps.

Use polar coordinates \((r,\theta)\) outside the origin. On \(r>1\), put \(s=\log(r-1)\). Let \(\beta_b:\mathbb R\to\mathbb R\) be the time-b flow of the complete vector field \(\sin(\delta)\,\partial_\delta\). It fixes every integer multiple of \(\pi\), satisfies
\[
\beta_b(\delta+2\pi)=\beta_b(\delta)+2\pi,\qquad
\beta_b\beta_c=\beta_{b+c},
\]
and is transitive on each interval \((k\pi,(k+1)\pi)\). On \((0,\pi)\) its explicit formula is
\[
\beta_b(\delta)=2\arctan\!\left(e^b\tan(\delta/2)\right).
\]
Each point stays in its interval, so \(|\beta_b(\delta)-\delta|\leq\pi\), uniformly in b and \(\delta\).

Define two plane actions by
\[
A_a(r,\theta)=
\begin{cases}
(r,\theta+a),&0\leq r\leq1,\\
(1+e^a(r-1),\theta+a),&r>1,
\end{cases}
\]
and define \(B_b\) to be the identity on \(r\leq1\), while on \(r>1\)
\[
B_b(s,\theta)=
\bigl(\theta+\beta_b(s-\theta),\,\theta\bigr).
\]
The displayed first coordinate for \(B_b\) is s, rather than r. Changing the representative of \(\theta\) by \(2\pi m\) does not change it. Its inverse is \(B_{-b}\). The uniform bound above gives
\[
e^{-\pi}(r-1)\leq r(B_b(r,\theta))-1
\leq e^\pi(r-1).
\]
Consequently the formulas and their inverses extend continuously across \(r=1\), depend jointly continuously on the parameters, and are proper at infinity. They are orientation preserving, since each is joined to the identity by its specified one-parameter action. The formula for \(A_a\) has the same properties directly. Since A changes s and \(\theta\) by the same amount, it preserves \(s-\theta\); the two actions commute exactly.

Let O be the open spiral strip described by
\[
(t,\delta)\in\mathbb R\times(0,\pi)
\longmapsto
\bigl(r=1+e^{t+\delta},\,\theta=t\bmod2\pi\bigr).
\]
This map is injective: equal angles give \(t'-t\in2\pi\mathbb Z\), whereas equal radii then give \(\delta-\delta'=t'-t\in(-\pi,\pi)\), hence both differences vanish. It is a local homeomorphism and therefore a homeomorphism onto its open image. On these coordinates,
\[
A_a(t,\delta)=(t+a,\delta),\qquad
B_b(t,\delta)=(t,\beta_b(\delta)).
\]
Thus the image of \((a,b)\mapsto A_aB_b\) acts simply transitively on O and is a copy of \(\mathbb R^2\) with its actual compact-open topology. It is closed in the plane homeomorphism group: forward and inverse limits preserve O, and evaluation at \((t,\delta)=(0,\pi/2)\) recovers
\[
a=t,\qquad b=\log\tan(\delta/2)
\]
continuously. A based triangular parameter loop
\[
(0,0)\longrightarrow(1,0)\longrightarrow(0,1)
\longrightarrow(0,0)
\]
generates this entire group G, since its first and last segments contain intervals in both one-parameter factors. Scaling its two parameters contracts it through actual plane homeomorphisms.

Take the original operator group \(H=\langle A_{-2\pi}\rangle\). It commutes with G. The restrictions of its powers to O form a closed proper discrete action, translating t by integer multiples of \(2\pi\). For \(h_n=A_{-2\pi n}\), compact-open convergence on O gives the exact boundary quotient
\[
h_n|_O\longrightarrow
\Phi(t,\delta)=(r=1,\theta=t\bmod2\pi).
\]
This is the quotient \(\Phi_z\) from §18 for the limit \(z=(1,0)\) of \(h_n(0,\pi/2)\). It is open onto the circle orbit. Its fibre over angle \(\theta_0\) is
\[
\coprod_{k\in\mathbb Z}
\{t=\theta_0+2\pi k,\ 0<\delta<\pi\},
\]
a disjoint union of proper intrinsic lines in O. The real lift \((t,\delta)\mapsto t\) has connected fibres. Thus an open equivariant circle quotient which is a compact-open limit of orientation-preserving ambient embeddings need not have a connected whole fibre. The example proves that exact obstruction to a connected-fibre argument. Its explicit global parameter contraction does not produce a centralizer fundamental-group kernel class.

## 21. Proper components of the actual real lifted boundary map: C.42

C.42 now supplies the complete component proof for the map in §18. The source and target coverings are retained in the equation `qF=Phi_z p`. The compatible triples `(l,a,b)` form a closed Polish subgroup of `L × Homeo(source covering plane) × Homeo-plus(R)`, and act transitively on the source. The real lift F is open and onto. Its fibre stabilizer is transitive on each whole fibre, and each component stabilizer is transitive on that component.

Frankel's Lemma 2.7 supplies a separating component of a real fibre. A complementary-domain stabilizer in its component stabilizer is open. Effros openness and connectedness then make that domain stabilizer transitive on the component. One accessible endpoint therefore makes every point accessible from that same domain. Three complementary domains would provide three disjoint embedded Y trees joining three common boundary points, and hence an embedded K3,3. There are exactly two domains. Compactification adds at most one inaccessible point, so Polulyakh's converse Jordan theorem gives a Jordan curve. A bounded circle component contradicts openness of F by the extreme-value argument on its disk. Every lifted component is consequently a proper line.

The exact disconnected-circle-fibre example in §20 is now accompanied by `code/c42_spiral_fibre_certificate.py` and its output JSON. All 50 symbolic identities pass; no floating-point computation is used. C.42 and the executed certificate passed independent C review in `work/part_c/review_c42.txt` and `review_c42_rerun.txt`.

## 22. An independent local-finiteness argument

Here is a proved auxiliary consequence of the C.42 action and proper-component result. It is not needed in the subsequent C.43 connectedness proof.

Fix a real fibre E and its transitive closed Polish stabilizer K. The complement of E has countably many domains, since each contains a member of a fixed countable basis. A domain stabilizer K_D is open in K: a small group element keeps one specified interior point in D, and hence preserves that complementary component. Effros makes every K_D-orbit open in E. Those orbits partition E into disjoint open sets, so each connected component meeting the invariant set ∂D lies entirely in ∂D.

Every component of E lies in the boundary of some complementary domain. To see this, begin with one accessible point of E, obtained by taking a straight segment from an interior point of a complement domain to a nearest boundary point. Transitivity carries this point to any specified point of E. The preceding paragraph then puts the entire component containing that point in the corresponding domain boundary.

For a fixed D, let C and C' be distinct proper-line components contained in ∂D. Write U_C for the side of C containing D, and V_C for the opposite open half-plane. Since C'⊂cl(D)⊂cl(U_C) and C' is disjoint from C, one has C'⊂U_C. Likewise C⊂U_(C'). The connected set V_C is disjoint from C' and meets U_(C'), because C is its boundary and lies in the open set U_(C'). Hence V_C⊂U_(C'), giving V_C∩V_(C')=∅. The pairwise disjoint opposite sides each contain a rational point. Thus only countably many components can lie in ∂D.

It follows that E is a countable union of its closed proper-line components. As E is a closed Polish subspace of the plane, Baire's theorem gives one component with nonempty relative interior. K-transitivity transports an interior point to every point of E and carries components to components. Every component is therefore open in E. These components are locally finite in the plane: otherwise a compact set meets infinitely many distinct components, and selected intersection points have a limit in the closed set E, contradicting the relative openness of its component.

## 23. Actual flowboxes, connected real fibres, and downstairs covering forms: C.43–C.44

The full proofs are in the adjacent `c43.tex` and `c44.tex`. The new sources were read in their primary texts:

- J. M. Aarts and L. G. Oversteegen, *Flowbox manifolds*, Transactions of the AMS 327 (1991), 449–463, Definition 5.3, Theorems 5.6–5.7, Main Theorem 0.5 and §4 including Remark 4.4. The author's full published text is available at <https://www.researchgate.net/publication/238598319_Flowbox_Manifolds>. Its cited local-section construction was also read in Aarts–Hagopian–Oversteegen, §3, <https://msp.org/pjm/1991/150-1/pjm-v150-n1-p01-s.pdf>.
- Mathieu Baillif and Alexandre Gabard, *Manifolds: Hausdorffness versus homogeneity*, Proceedings of the AMS 136 (2008), 1105–1111, Theorem 1.1 and its full proof in §4, <https://access.archive-ouverte.unige.ch/access/metadata/3dfff744-545f-4c92-a97d-5226fc787571/download>.

For each compact component arc I through v, an identity neighborhood in the compatible Polish group can require uniform displacement less than epsilon on I. Its evaluation image is open by Effros. Restricting the resulting group element to I gives exactly the Aarts–Oversteegen regularity condition, including the specified image of v. Their theorem produces flowboxes. The elementary C.33 product-cancellation proof makes the transverse factor an interval. In such a chart F factors through that interval; openness of F makes its interval function strictly monotone. Thus the charts use the actual F coordinate.

The quotient by connected fibre components is proved open directly: for a point v in the saturation of an open set U, take a compact leaf arc from v to w∈U and use the same small arc embeddings; every nearby v' has an image arc ending in U. This proof does not assume that an element stabilizing one component fixes every component. In an F-coordinate chart each leaf has at most one plaque, so the transverse interval identifies with an open subset of the actual leaf quotient. The quotient is second countable and homogeneous under the compatible action. Baillif–Gabard therefore makes it Hausdorff. It is a line, and its local homeomorphism to the real target is a global homeomorphism. This proves that the real lifted fibres are connected.

Plane orientation together with the F transverse orientation coherently orients the leaves. The Aarts–Oversteegen auxiliary flow has exactly these leaves and is free. Saturating an actual F-section gives a continuous bijection `R × I → F^(-1)(I)`, which is a homeomorphism by invariance of domain. The additive transition functions and a locally finite partition of unity produce a global section, hence a homeomorphism `T:R × R → source covering plane` with `F(T(u,t))=t`. No original-operator equivariance is claimed for this auxiliary flow.

For the original source covering, the deck relation is exactly `F gamma=F+eta(gamma)`, with eta taking integer values for a circle target and zero values for a line target. Its kernel K acts freely and properly on each real fibre, so K is trivial or infinite cyclic. A variable fundamental-interval formula conjugates the cyclic kernel to unit translation in the fibre direction. Nonzero eta image in that case would make the full source quotient the image of a compact cylinder strip, impossible for an open planar source. With K trivial and eta image mZ, a continuous interpolation followed by `rho_(t+m)=h_t rho_t` conjugates the deck generator to pure translation by m in the base coordinate.

Thus the source is a plane or annulus and the exact five forms in C.44.1 follow. Whole-circle-fibre component labels are `Z/eta(Gamma)`; each component is `R/K` in the displayed normalized coordinates. This also proves that the source covering maps onto every downstairs component, which had deliberately been left unasserted in C.42. These coordinates concern one quotient at a time. The simultaneous intrinsic assertions are now supplied by C.46, C.48, and C.49 as described below; the ambient relative extension is still retained.

## 24. Two coordinates and the one/two-foliation intrinsic assertions

C.45 puts two independent real boundary quotients into one closed Polish compatible lift group. Their pair map is a homeomorphism onto an open domain with interval coordinate sections. Each finite endpoint is an actual continuous open homogeneous quotient of the two target actions and is therefore a real-line homeomorphism. Explicit coordinate changes give the plane, the ordered half-plane x<y, or the unit band x<y<x+1, with their exact full increasing coordinate-pair groups. The actual global restriction kernel and all downstairs labels are retained.

For a full family of exactly two fiber partitions, C.46 applies the natural median in these coordinates. A commuting operator normalizes the source stabilizer J and satisfies the exact relation Phi_z h=Phi_(a_h z); hence it permutes the entire two-element family. Its source lifts have the actual coordinate-pair or exchanged-coordinate form. Median naturality proves equivariance with every operator and deck map. The target equations descend through the original covers.

C.48 handles exactly one partition. The full group of lifts of the proper closed restricted operator group remains free, proper, closed, and locally compact in its actual topology. Its induced real quotient action lies in the translation centralizer of the transitive loop-generated base group. The fiber kernel is exactly 1, Z, or R; the proof gives every resulting base/fiber action by explicit coordinate changes. A dense discrete base image is the rank-two deck lattice case. The actual quotient foliation is then a minimal torus foliation, and an explicit suspension conjugacy supplies its linear form. The base median and fiber interpolation preserve all operator equations.

C.46 and C.48 prove intrinsic contractions and all specified quotient relations. Their original proofs leave continuity at the ambient frontier unproved. C.52 now replaces their target families by exponential fractions on the actual metabelian images and the median on the other images, retaining every operator equation. For compact operator quotients, its direct interior limit and diagonal argument give a whole-closure extension agreeing with the prescribed exponential region. C.53 and C.55 extend this further as recorded below. A quotient equation alone is still not asserted to characterize the complete action on an arbitrary compactification.

## 25. Three quotients and the actual Lie groups: C.47–C.49

C.47 proves local compactness in the induced topology, rather than inferring it from determination by finitely many values. Sections recover each target map and its inverse, so the full three-quotient group is closed and Polish.

For a half-plane or band pair domain, the two target actions coincide. When the other pair domains are full, the third fibers are y=r_z(x), with increasing r_z above the identity. The unique equation r_s²(a)=b defines an invariant strict interior mean M(a,b)=r_s(a). A further nonfull pair instead identifies the third action by its finite endpoint homeomorphism. In a half-plane, ordered-pair transitivity forces every commuting endpoint map to be the identity; inverse equations produce the mean for an exterior third value. In a band its constant integer interval label, followed when necessary by (u,v)=(y,x+1), gives the mean. Recursive subdivision gives dense fixed points in an interval. Separate injectivity then propagates the fixed interval beyond either finite endpoint. Thus the point stabilizer is trivial and evaluation identifies the full group topologically with the source plane.

When all three pair images are planes, a displayed coordinate change makes the third map a global continuous ordered-loop multiplication with identity zero. Its automorphisms have compact evaluation strips: diagonal roots and negative division partners give uniform small elements; translation grids bound images; brackets prove equicontinuity; explicit positive bounds on inverse evaluation give the same controls for inverses. Arzelà–Ascoli proves compactness in the homeomorphism-group topology. After this local compactness is proved, Hilbert–Smith makes the stabilizer Lie. Its free Cartan right action on the still-Polish full group satisfies Palais' hypotheses, giving the actual local product with the source plane. The full group is consequently Lie of dimension two or three.

C.49 identifies the subgroup generated by the actual based source lifts. They commute with every source deck map. Countably many deck translates of compact finite-word tracks cover the source plane, so Baire gives an open orbit; every orbit is a deck translate and is open, hence connectedness gives transitivity. Ambient-null circle winding and pair injectivity make the based source lift a closed loop.

In dimension three, the three target stabilizer Lie algebras give three distinct lines in the tangent quotient by the one-dimensional source isotropy. Its adjoint action is scalar. Scalar zero would make isotropy a normal action kernel. Nonzero scalar gives an abelian two-dimensional eigenspace and exactly the scalar homothety Lie algebra. Connected isotropy and the contractible source quotient identify the simply connected homothety group and its actual standard plane action.

The original two-page proof of Yamabe, *On an arcwise connected subgroup of a Lie group*, Osaka Mathematical Journal 2(1) (1950), 13–14, DOI 10.18910/6228, was read at <https://ir.library.osaka-u.ac.jp/repo/ouka/all/6228/omj02_01_03.pdf>. Its analytic-subgroup conclusion is followed by a separate closedness proof: a proper two-dimensional homothety subgroup with a dilation direction preserves an affine line and cannot be transitive. Thus the actual transitive subgroup is all translations or all homotheties. The two-dimensional web group is already simply transitive. The actual lifted groups are precisely the stated R², positive affine line group, or scalar homothety group, each with global exponential and logarithm.

For each orbit, the closed Polish group of compatible pairs (l,n), with p n=(l|O)p, projects openly and onto the actual lifted group. Every element has a finite-word global preimage. The kernel fixes the whole orbit closure, so the open quotient gives a jointly continuous closure action. Exponential fractions contract the original loop there. Common intrinsic boundary images are the same actual group G|B with its verified Lie topology; based target-cover naturality proves compatibility on intersections and for all actual quotient equations. Operator conjugacy transports the exact source lifts. C.49 proves finite-union compatibility, and C.50 proves infinite accumulation.

## 26. The exact 1913-word bound and infinite accumulation: C.50

For a based homothety path k_s=(a_s,v_s), put A=max|a_s|. A maximizing path value or its inverse is a single-letter anchor of positive logarithmic scale A. Conjugating its fixed point to zero changes no word lengths. Its commutator with the path is the translation C_s=(0,(exp(A)−1)v_s).

For A at least log 2, the planar path identity supplies each required translation fraction by three commutator values. Translation extraction and an intermediate-value choice of logarithmic scale give a 25-letter construction.

For 0<A≤log 2, the three signed-measure identity represents r(a_t,v_t) additively by at most five signed path values. C.50 does not identify this sum with a group product. The exact inverse-letter prefix formula computes its complete error: translation coefficients are epsilon_j(exp(p_j)−1), with |p_j|≤5A. The discrepancy between linear interpolation and the true exponential fraction is theta(a_t,r)−r. Dividing by D=exp(A)−1 gives uniform absolute bounds 31 and 4, including a_t=0. Each coefficient is corrected by bounded integer products of planar fractional commutator words. The exact total is 5+12(4+5·31)=1913. For A=0 the planar translation result applies.

The primary Grandoni–Ravi–Singh–Zenklusen Theorem 4.7 and §4.3.2 were reopened at <https://people.idsia.ch/~grandoni/Pubblicazioni/GRSZ13mp.pdf>. The d=3 cut count is explicit: two intervals cut three times give at most five pieces, so one equal-mass half uses at most two. For the whole interval, three cuts give at most four pieces, again leaving a half with at most two intervals, which are also circular intervals. This retains the possible sign change at the identified origin. Uniform polygonal approximation gives the vector identity for arbitrary continuous paths.

The executable certificate work/part_b/code/c50_homothety_word_certificate.py and its JSON check 462 exact identities, including all 62 inverse-sign patterns of lengths one through five. It checks conjugacy, commutators, every prefix product, the complete correction residual, the zero-scale limit, and the integer count. No floating-point inputs occur. Both root and C independently reran it successfully.

All words belong to one compact family of actual plane word isotopies of length 1913. The residual identities hold in the specified simply connected source groups. At a limiting intrinsic line, bounded logarithms force the prescribed fraction. At a circle, evaluation of the null source residual at two distinct points proves the exact real angle identity, including an identity projected endpoint with nonzero based real angle. The inverse loop gives the jointly continuous inverse family.

The contraction is therefore jointly continuous on X_star=closure(U2 union U3), where U3 consists of the open orbits with at least three actual boundary partitions. This includes arbitrary accumulation of homothety cases, agrees with C.37 on X2, and commutes with every original operator. Independent reports are work/part_c/review_c47.txt, review_c49.txt, and review_c50.txt; C.43–C.46 are covered by review_c43_c46.txt.

## 27. Present status

No admissible infinite-operator level-0 counterexample, and no universal surface-centralizer fundamental-group injection, has been proved. C.26 rules out the globally transitive loop-generated case on closed hyperbolic surfaces. C.27–C.31 give the orbitwise formulas and operator structures. C.32–C.33 contract every restricted open-orbit loop. C.34 proves the full nonopen-locus homeomorphism family and settles every loop with no open lifted orbit.

C.35 proves that extending the particular median prescription is impossible in general; the boundary contraction must be allowed to change. C.36 supplies compatible closure contractions for dimension-two proper operator images. C.37 proves the uniform three-word estimate and extends this family continuously, with inverses, to X₂, including all infinite accumulation. C.38 gives the exact cyclic operator-cover structure on a nonabelian one-dimensional orbit.

C.39 proves the global kernel conclusion for every class with a commuting-valued representative. C.40 supplies such a representative whenever the loop-generated closure is locally compact in its actual induced topology. C.41 proves the full kernel conclusion for every operator action with a dense orbit. A remaining kernel class therefore has no commuting-valued representative and no representative with locally compact generated closure, and its operator action has no dense orbit. No general deformation to either class of representatives has been proved.

C.42–C.45 now identify each actual nontrivial boundary quotient and every pair: their real lifts are product projections, their sources and downstairs component labels are explicit, and two independent lifts give one of three exact pair-coordinate domains. C.46 and C.48 give all simultaneous quotient equations intrinsically for families of cardinality two and one. C.47–C.50 give the actual Lie groups, whole-closure contractions, and uniform infinite-accumulation control for every family with at least three partitions.

For the orbitwise route, C.54/C.56/C.58 now handle every two-metabelian-quotient source through arbitrary accumulation, including the full four-dimensional product affine group. C.52 supplies the exact mixed target replacement on each treated compact-quotient closure, and C.53/C.55 supply the global-family and full-local-centralizer improvements below. C.59 supplies actual globally continuous localized kernel perturbations without quotient cocompactness. C.60 makes every positive homotopy group of the relative one-partition quotient kernel vanish, with no compactness or finite-representative hypothesis, by exact compact-family point control and, for loops, forward and inverse prefix-track control.

C.61 first confined the intervals joining two equal-real-level prefix values to the nonopen locus in the limit. C.62 strengthens this to exact containment in one compact three-word image of the original input point. Thus such intervals cannot escape to infinity or approach a different nonopen orbit, and at a fixed frontier point the entire interval shrinks to that point. This control is independent of every source chart and works across arbitrarily varying open orbits and quotient choices, with the original real and deck labels retained.

C.63 now proves an actual moving-base lift and global relative contraction on every operator-invariant union of original open orbits whose full local centralizers have dimension one and whose frontier points are fixed by G. It constructs one compact family of labelled infinite products of original short increments and selects continuous fiber coefficients by relative partition-of-unity approximations in the exact affine line bundle. Both the map and inverse are bounded by compact global word families. The result includes empty global target families and arbitrary accumulation of open orbits.

The remaining global work includes the prescribed-value problem at nonfixed frontiers, the open orbits with zero-dimensional full local centralizer, and the relative extension over the exterior nonopen locus. C.60 supplies the quotient-kernel contraction, and C.63 now supplies the moving principal-base lift in its fixed-frontier case. C.62 controls the whole prefix-fiber interval, but on a nonfixed limit orbit its three-word image may contain several points and does not by itself select the required boundary value; the analogous compact-family estimate in C.63 has the same unresolved issue there. The explicit auxiliary example in section 37 also proves that choosing from the pointwise full-prefix fiber hull need not be continuous across source fibers. The mixed prescription is not asserted continuous on the entire nonopen locus; outside the treated closures, switching by target metabelianness alone does not solve transverse continuity. C.35 still prevents imposing the original fixed median prescription in all regions. No general relative equivariant extension theorem has been proved. These outstanding steps leave C.12 unresolved.

## 28. The relative compact-quotient extension: C.51–C.52

C.51 is the parent's proved compact-quotient frontier argument. A compact fundamental set gives x_n=q_n y_n with a convergent subsequence of y_n. Actual global operators approximate q_n on that set and all contraction and inverse images. Open evaluation supplies small l_n sending the limiting basepoint to y_n; exact commutation makes the operator image of the limiting basepoint converge to the frontier point. The C.42 evaluation homeomorphism then gives the entire compact-open equivariant quotient limit. Every nontrivial frontier orbit is represented by one of the actual quotients. Empty family therefore forces fixed frontier points.

C.52 makes the target prescription agree with C.50: use the actual Lie exponential on a transitive metabelian intrinsic target, and the natural median otherwise. The real group generated by the based target lifts is conjugate to all translations or the full positive affine group precisely in the metabelian branch. Circle projection and its based real lift are retained, including a nonzero integer angle at an intermediate identity projected value. Every line reparametrization, covering change and coordinate exchange conjugates the actual target path and therefore preserves the rule.

The two-coordinate product, diagonal half-plane and periodic band maps preserve their exact source domains. The one-coordinate fiber interpolation is unchanged; replacing its base median by an element of the actual target Lie group preserves every operator equation. Consequently all actual quotient relations are still exact.

The compact fundamental set proves every interior-to-frontier limit using these modified relations. It is unnecessary to assume prior transverse continuity of the mixed target prescription. For any varying frontier sequence, choose nearby interior points whose images approximate its proposed frontier images, using the already proved fixed-frontier limits. The interior limit applied a second time proves continuity of that frontier sequence. The same argument with inverse images proves joint inverse continuity.

Every nonopen target on X_star is metabelian because the second-derived group identity extends from its dense open Lie union. The new prescription is therefore exactly C.50's based fractional prescription there. Finite closed-set pasting gives the relative extension with X_star. Independent C audit passed in work/part_c/review_c52.txt.

## 29. Global quotient families and the full local centralizer: C.53–C.55

C.53 enlarges the family to all z fixed by L_x whose actual G-orbit is nonopen and nontrivial, without requiring z to lie on the source frontier. C.42 already has this exact global scope. The same compatible lift groups give C.43–C.49. For the Lie group N, the kernel of the closed Polish compatible-pair projection fixes every global quotient image by equivariance. Intrinsic restriction continuity makes that action descend through the open quotient, so every global quotient retains its exact exponential equation. All uniform C.50 word, residual and real-winding inputs remain valid, enlarging the closed exponential region to X_dagger.

For finitely many operator-orbit representatives with compact quotients, an accumulating sequence is h_n q_n y_n with y_n in one of finitely many compact fundamental sets. The exact global approximation is made after applying h_n, so no uniform modulus for the varying operators is assumed. The C.42 limit now gives a possibly remote global quotient, which is why the enlarged family is required. The same diagonal and inverse argument handles every accumulation of arbitrarily many translates. The detailed independent B audit is work/part_b/review_c53.txt; its single missing TeX backslash was corrected by the parent.

C.55 makes a further exact improvement. Put C_O equal to the full centralizer of G restricted to O, with its actual compact-open topology. C.30 makes it free, proper and locally compact, and C.33 makes it Lie. The original restriction map H_O to C_O and its kernel are retained; Q_O is the closure of that image.

Every local q in C_O commutes with L restricted to O. Thus q is itself a continuous L-equivariant map from O into the ambient plane, even when it has no global extension. Choosing a_q x=qx gives equality of source stabilizers and the exact formula Phi_z q=Phi_(a_q z). It follows that the full global quotient family is invariant under every local centralizer element. The C.46/C.48/C.52 intrinsic contractions consequently commute with this full group.

With compact O/C_O, the maps m_n=h_n q_n are actual members of Map_L(O,plane). Open evaluation and m_n(y)=l_n^(-1)x_n give their basepoint limit directly. The C.42 evaluation homeomorphism gives compact-open convergence to the required global quotient, without approximating q_n and without extending it globally. This proves the same finite-representative infinite-translate result using compact quotients by the full local centralizer. Its two-dimensional cases also enlarge the uniform exponential region to X_ddagger. The detailed B audit, including the empty-family C.32/C.33 and one-partition C.48 transfer, is work/part_b/review_c55.txt.

The mixed prescription is continuous on these treated closures by the direct limit argument. This is not a continuity assertion for the mixed rule on every nonopen orbit outside them.

## 30. A compact-support route that adds no original-loop case

On an open orbit of the group generated by the original loop, every point is moved by at least one loop value. Otherwise all generators fix that point and its generated orbit is a point. Hence the union of the generator supports is the entire open orbit.

It follows that requiring this original loop to have support inside the inverse image of one compact subset of O/Q already forces O/Q to be compact. That support condition does not add a noncocompact case. Compact support could still be useful for factors of a separately established fragmentation, but no quotient-compatible fragmentation or general frontier extension for those factors has been proved here.

## 31. Every two-metabelian-quotient source and its uniform limit: C.54, C.56, C.58

C.54 retains the actual closed source topology and all original quotient covers. Two independent metabelian target images put the actual source into precisely R², Aff⁺(R), a diagonal R² semidirect R with two real weights, or the full Aff⁺(R)². The half-plane source gives the displayed simply transitive affine action; the periodic band is excluded by the exact centralizer and transitivity equations. Every listed group has a globally invertible exponential map, including zero or opposite diagonal weights. The open compatible-pair quotient gives the entire closure action and every global quotient relation. Its exact certificate passed all 43 checks.

C.56 supplies the uniform 13,363,205-letter bound for all diagonal one-parameter sources. The complete independent B audit and rerun are work/part_b/review_c56.txt and c56_independent_rerun_stdout.txt. Its source contraction extends through every accumulation by the exact source residual and real circle-winding comparison.

C.58 supplies the remaining full-product bound 172,496,624,025,607. Seven signed values of the actual logarithmic path give the target Lie sum. The product's entire translation error is expressed through 21 actual commutators by a smooth antisymmetric radial identity. For i<j the coefficient is explicitly minus the divided difference of sigma at P_j and P_j+a_j, with its derivative value at zero. Both affine factors evaluate the same function at their two complete seven-dimensional scale vectors. Dividing by the product of seven fourth powers of exp(a)+exp(-a) gives a function with each tanh-coordinate derivative bounded by12. The exact two-node interpolation coefficients are bounded by86 and84. Integer Laurent conjugation paths and the planar three-letter identity realize every correction in actual original path values.

The certificate work/part_b/code/c58_affine_product_word_certificate.py passed 262,504 exact checks: 1,778 signed cases, every sign pattern of lengths one through seven in seven scale regimes, and 28,644 pair interpolations. Its arithmetic retains formal logarithms, zero scales and canceling prefixes; no floating-point approximation is used. Both root and C independently reran it. Their complete reviews are work/root/review_c58.txt and work/part_c/review_c58.txt.

All fractional words and residual identities hold in the specified source cover. Compactness of the one fixed finite word-parameter family and the exact real-angle comparison therefore give the contraction on X_flat, the closure of all the treated affine sources together with the earlier region. This includes every C.54 orbit, agrees on X_sharp, and retains the finite full-local-centralizer representative extension relative to X_flat. It does not settle exterior quotient lifting.

## 32. The exact two-partition full local centralizers: C.57

For the plane pair domain, every full local centralizer lift is an increasing coordinate pair; a coordinate swap would give a graph invariant under the transitive source action. Each actual line centralizer is exactly 1, Z or R after its proved conjugacy. All such pairs commute with the retained source deck group and descend, giving the exact product modulo that deck subgroup. The quotient spaces are plane, cylinder, line, torus, circle or point as displayed in C.57.

For the ordered half-plane, the complete increasing ordered-pair action forces the full centralizer to be trivial. For the periodic band, the fixed set of a point stabilizer is exactly its integer translates, proving that the period is primitive. The full lifted centralizer is generated by e(x,y)=(y,x+1); only even powers preserve source orientation, so the original deck subgroup is retained as an even cyclic subgroup. The exact coordinate change to (x+y,y−x−1/2) gives the glide reflection and its open Möbius quotient. The noncompact residual cases have full local groups 1, Z or R and the displayed plane, cylinder, line or Möbius quotients. These are exact action and quotient maps, not an ambient frontier assertion. Independent C review is work/part_c/review_c57.txt.

## 33. Actual noncocompact localized extensions: C.59

For one compact D⊂O, C.59 defines the closed local group V_O[D] by commutation with the full local centralizer, pointwise preservation of every actual global quotient map, and moving set inside C_O·D. Conjugation over all H-translates, followed by the identity on their complement, defines a continuous topological group embedding into the global H-centralizer. The exact H-stabilizer restriction makes the rule independent of the transporting operator.

For a moving sequence write x_n=h_n q_n y_n with y_n∈D. Small L-elements align its convergent basepoints; the maps h_n q_n are actual L-equivariant maps, even when q_n has no global extension. C.42 identifies their entire limit as a global quotient or a constant. The quotient-kernel equation forces the image limit to be x. Inverse moving sets are identical, so the same compact saturation gives the inverse proof. This works for arbitrary accumulation of infinitely many translates and a noncompact total quotient.

With two independent global partitions, any based path in the quotient kernel has zero increments in both original target covers. C.45's injective pair of real lifts then makes that path the identity. The entire kernel can still contain discrete deck phenomena; C.59 states only triviality of its identity path component. The useful localized path factors therefore lie in the zero/one-partition cases. Independent reviews are work/root/review_c59_c60.txt and work/part_c/review_c59.txt.

## 34. All positive homotopy groups of the relative one-partition kernel vanish: C.60

Let W be an H-invariant union of original open G-orbits with exactly one global partition. C.60 considers the actual global H-centralizer subgroup fixing the exterior of W, preserving each orbit and all its quotient maps. Every based sphere family in this subgroup contracts in the same subgroup; no compact support, quotient compactness or finite number of operator representatives is needed.

A nonempty global family supplies a nontrivial nonopen target orbit outside W. The loop fixes two distinct points there, so C.32's exact plane two-point winding is zero. The original source-cover lifts therefore close. The quotient-kernel relation makes each real lifted base coordinate fixed. In C.48's actual proper-operator coordinates all lifted operators are affine in the fiber coordinate. Interpolating the increasing fiber map with the identity preserves all those equations, including negative coefficients, every deck map and every global quotient.

The crucial uniform control uses the original global loop itself. At a point x, the interpolated fiber value lies between x and a_t(x); that entire interval lies in the actual prefix path a_s(x), 0≤s≤t, after projection from the specified cover. The inverse lies between x and a_t^(-1)(x), so it belongs to the actual inverse prefix track. H transport preserves both inclusions. At any frontier point fixed throughout the original loop, compactness of its time interval makes both tracks uniformly converge to that point. Thus every mixed-orbit and frontier limit is controlled, independently of the chosen affine charts. Both global families are jointly continuous.

For spheres of dimension at least two, the map from the product of the universal source cover and parameter sphere lifts directly because its domain is simply connected. Lifting the inverse family from the same basepoint proves the inverse identities. Connectedness of the parameter space makes every operator and target deck increment zero. A path from the parameter basepoint to a chosen sphere point supplies the fiber interval, so both interpolated point and inverse point belong to the image of the entire compact sphere family. No continuous choice of those paths is needed. Compactness gives the same frontier control, and the based interpolation descends to a cone filling.

C.60 proves vanishing of every positive homotopy group of this relative kernel, not contractibility of the entire topological group and not existence of a lift of a nontrivial quotient homotopy. For loops its proof only needs closed based source lifts; the two exterior fixed points establish that requirement automatically in its stated setting. Independent reviews, including the higher-degree addition, are work/root/review_c59_c60.txt and work/part_c/review_c60.txt.

## 35. The compact-strip reduction: C.61

C.61 considers the compact interval in the specified real fiber between two original source-lift prefix images at exactly the same real level. An alleged finite limit in an open orbit first forces all intervals into that one original orbit. One actual deck map then aligns an interior point of each interval inside a fixed source covering chart. Commutation with every original based lift gives the exact relation between the aligned endpoints through a member of the one compact prefix-product family. Their common bounded base coordinate and escape of the first endpoint force both endpoints to the same fiber end, by uniform properness of the increasing fiber maps. They cannot enclose the aligned bounded interior point.

This proves that every such interval eventually avoids every compact set in the open-orbit union. It was independently audited in work/part_c/review_c61.txt. The stronger C.62 below now also excludes the remote nonopen limits and ambient escape that the original C.61 statement deliberately retained.

## 36. Exact three-word containment of every prefix-fiber interval: C.62

For one excursion (a,b) of the actual real base path away from its endpoint level, put A=tilde f_a(tilde x), h_r=tilde f_r tilde f_a^(-1), and g=h_b. The first path h_r(A) lies strictly on one side of the original proper fiber. Since its induced base map is increasing, its inverse sends that level strictly to the opposite side; g preserves this side because its base map fixes the level. Hence the second path g h_r^(-1)(A) lies strictly on the opposite side and returns from g(A) to A.

These paths form the boundary, with one constant edge, of the actual source triangle h_u h_v^(-1)(A)=tilde f_u tilde f_v^(-1) tilde f_a(tilde x), where a≤v≤u≤b. Their winding is plus or minus one about every interior point of the fiber interval between A and g(A): each path contracts within its own strict half-plane to the appropriate side of an explicit diamond. If a fiber point were omitted by the triangle, this triangle would null-homotope that nonzero winding in the punctured source plane. Thus the entire interval is in the triangle image.

For a general closed zero set of the base path, retain the fiber coordinate on that zero set and interpolate it linearly on every complementary gap. Uniform continuity on small gaps and continuity at the finitely many large-gap endpoints prove that the extension is continuous. Its range contains the whole interval between the original endpoint fiber coordinates. Each of its values is therefore supplied either by the original zero-level track or by one of the excursion triangles. This proves the exact inclusion in the compact ordered three-word image.

Projection is through the original source cover, and original deck maps commute with every based source lift. A change of source lift therefore transports the whole interval and every word by that same deck map. The actual equation F delta=F+eta(delta) preserves equality in the real target; equality only modulo a target circle period is not used. Applying the identical proof to the inverse path gives the inverse-word version.

The projected global words are W(a,v,u;x)=f_u f_v^(-1) f_a(x), with 0≤a≤v≤u≤1. This one compact parameter set is independent of the source orbit and chart. For x_n→x, its joint continuity supplies one compact ambient set containing every interval and uniform convergence of the word values at x_n to those at x. Every interval limit therefore lies in the same G-orbit as x; no ambient escape is possible. When x is fixed, the whole compact word image is {x}, giving complete interval shrinking. Root and C audited the proof in full; the independent report is work/part_c/review_c62.txt.

At a nonfixed orbit, this compact word image may contain several points. The result does not identify which point a new moving-base lift must choose, and it does not construct that lift.

## 37. Two exact limitations of prefix-based lift selection

The first auxiliary example, work/part_b/prefix_lifting_audit.md, is an actual R² action (x,y)↦(x+b,e^a y). Its path makes a base running maximum plateau while the original point-track parameter must cross a decreasing excursion. There is no continuous lift constrained to the original point prefix. Filling the fiber interval repairs that particular example exactly. Its certificate work/part_b/code/prefix_selection_certificate.py passed 58 rational checks.

The stronger example, work/part_b/prefix_fiber_hull_selection_audit.md, uses the actual one-global-partition action (x,y)↦(lambda x+c,e^d y), with the vertical scalings as original operators. The displayed based loop generates Aff⁺(R)×R and has an explicit null-homotopy in their centralizer. For one fixed median parameter, its real base map near zero is M(v)=1+v+|v|/4. Even allowing every original time in the full prefix to the selected endpoint, the fiber hull of all crossings at level M(v) is [u+2,u+7/3] for v>0 and the singleton {u+3} for v<0. At zero the interval is [u+2,u+3]. The incompatible one-sided limits rule out every continuous selection from these filled hulls.

The exact affine formulas, complete crossing lists and strict one-sided separation are checked by work/part_b/code/prefix_fiber_hull_selection_certificate.py, which passed 41 symbolic rational checks. This example rules out the stated pointwise hull prescription; its explicit centralizer null-homotopy proves that it is not a counterexample to C.12. The actual three-word images of C.62 are larger and are not restricted by this no-selection conclusion.

## 38. The controlled moving-base lift at fixed frontiers: C.63

C.63 begins with the actual principal bundle O→O/C_O^0 of a dimension-one full local centralizer. Its section and the based covering isomorphism give precisely A×B and the two original deck labels, with at most one circle factor. The complete lifted operator group consists of fiber translations and, when present, one labelled generator (u,v)↦(lambda u+kappa,v+d). Negative lambda is retained. Commutation makes each original source lift a skew translation (u+phi_t(v),beta_t(v)), and C.32's ambient-null restriction makes that source path close.

In the closed compatible product of the global homeomorphism group and all countably many original source-cover groups, successive compact short-increment families are chosen so that their products change by a summable amount in a complete compatible metric. This controls global and source maps and inverses. The uniform infinite-product limit is a continuous map from one compact path-connected parameter product into the exact compatible group. It retains every source lift label, commutes with all operators and fixes every G-fixed point. Limits preserve each original open orbit, using its closed complement and the inverse equality.

For a desired base median, the finite-product family supplies a compact interval of fiber shifts whose base value is exactly that median. It is nonempty because the median lies between the initial and endpoint base values. The path t↦beta_t^(-1)(a) is nonconstant at every base point a; otherwise that point projects to a common fixed point of the transitive base action. Arbitrarily short original increments and their inverses therefore move a to both sides, while tending to the identity in the complete compatible topology. This gives the exact interlaced lower-limit inclusion from each finite-product interval to the next enlarged interval.

The intervals are treated as convex subsets of the actual real line bundle with transition c(v+d)=lambda c(v). This preserves negative coefficients and all discrete component and deck equations. On the four parameter boundary faces, replace each interval by the prescribed singleton; the lower-limit inclusion survives by continuity of that prescription. Locally finite partitions of unity give successive continuous approximate selections with summable differences and errors tending to zero. Their limit lies in the closed interval from the compact infinite-product family and attains every prescribed boundary value exactly.

The resulting skew translations are homeomorphisms, with their explicit jointly continuous inverses. They commute with the full local centralizer and descend through every original source cover. Transport over operator orbits is independent of the transporting element because its stabilizer restriction lies in that local centralizer; the original restriction kernel is retained.

For each point, the selected value lies between two actual labelled compact-family values at the same real target level. The C.62 triangle puts it in one compact global family K K^(-1) K applied to that point. Inverse bracketing gives the compact inverse-family estimate K^(-1) K K^(-1). Every map in both families fixes every G-fixed frontier point, so compact global evaluation proves the required joint frontier limits across arbitrarily varying open orbits. This supplies an actual relative null-homotopy, without a compact quotient or finite number of orbit representatives.

Independent full reviews are work/root/review_c63_f11.txt and work/part_c/review_c63.txt. The separate work/part_b/post_c63_frontier_audit.md records the precise remaining nonfixed and zero-dimensional cases, and proves a small-path homogeneity observation via the Polish based path group without asserting a continuous local section.

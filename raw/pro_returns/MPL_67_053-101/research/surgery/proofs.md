# Targeted checks behind the surgery notes

These are research arguments after the transcription freeze. They do not supply missing manuscript text. References W1–W4 are bibliographic records in `web_sources.md`; no claim of novelty is made. The root transcriber performed these checks personally after reading the context.

## P-S03. Two different boundary sheaves

On the closed upper half-disc choose the continuous square-root branch with argument in [0,π]. It is continuous at zero and holomorphic at every interior point. If it had a holomorphic extension g to a neighbourhood of zero, the identity theorem would give g²=z there. The order of a nonzero square at zero is even, while the order of z is one, a contradiction. Thus the large sheaf of continuous, interior-holomorphic functions is strictly larger than the sheaf of extendable holomorphic germs, even on the standard smooth model.

This checks the distinction stated on 67/054. It does not refute 67/056 when the quoted “est” means that the large sheaf determines the conformal charts, rather than equals their extendable-germ sheaf.

## P-S04. Counterexample to the isolated unqualified reflection sentence

For z=x+iy set f(z)=x+2iy. This is a real-linear homeomorphism of the closed upper half-plane onto itself and maps the real axis into itself. It is continuous, injective and open as a map of that closed-half-plane space. Its real and imaginary parts have u_x=1 and v_y=2, violating the Cauchy–Riemann equations on every interior open set. Therefore continuity and real boundary values alone do not imply holomorphicity.

The live Lemme 1 on scan55 separately assumes interior holomorphicity and is unaffected. The refined statement S04 restores this hypothesis in the following general reflection sentence. Hua's §VII already makes that repair; the present counterexample only checks its necessity.

## P-S05. Reflected boundary map has nonzero derivative

Assume the hypotheses of Lemme 1, reflect across the real boundary, translate the boundary point and its image to zero, and write the resulting germ as f(z)=a_n z^n+O(z^(n+1)), with a_n real and nonzero. Reflection implies real coefficients. If n≥2, choose two angles in (0,π) where a_n sin(nθ) has opposite signs. For sufficiently small positive r, the remainder cannot change those signs, so one image f(re^(iθ)) lies below the real axis. This contradicts the map's half-plane image. Thus n=1, giving a nonvanishing derivative and a local holomorphic inverse. This is the step compressed at the top of scan56 and spelled out in Hua §VII.

## P-S14. Intrinsic shadow and explicit failure of injectivity

For a pointed conformal disc (D,a) in X, let f:unit disc→Int(D) be a conformal map with f(0)=a. Its derivative sends the unit disc in T_0 C to a round disc in T_a X. Another such uniformization is f composed with a rotation, so this image disc is independent of the choice. This is the tangent shadow in the local holomorphic setting; no assertion is made about the absent Q1-07 comparison beyond this construction.

In a fixed chart about zero take f_ε(z)=r(z+εz²), for r>0 small enough that the disc of radius3r/2 stays in the chart, and |ε|<1/2. For z,w in the closed unit disc,

\[
f_\varepsilon(z)-f_\varepsilon(w)=r(z-w)(1+\varepsilon(z+w)).
\]

The last factor is nonzero because |ε(z+w)|<1. Thus f_ε is an embedding of the closed disc, holomorphic with nonzero derivative in its interior, and all shadows have radius r because f'_ε(0)=r. If two such image discs were equal, the two normalized Riemann maps would differ by a disc automorphism fixing zero with derivative 1, hence by the identity; their quadratic coefficients would be equal. This gives genuinely different embedded discs with equal shadows, but says nothing about admissibility.

For 0<λ≤1 the subdisc f(λ unit disc) has shadow λo(D), by the derivative of f(λz). This proves the concentric scaling identity on scan64 in this setting.

## P-S15. No unpointed-disc-invariant rotation structure

A toric boundary action compatible with the conformal disc is the rotation subgroup about its chosen centre. The centre is the unique common fixed point in the disc of that subgroup. If the action were canonical for the unpointed disc, conjugation by every conformal disc automorphism would preserve this subgroup and hence its unique fixed point. But disc automorphisms move the centre to arbitrary interior points. This contradiction verifies Hua's exception to “dans tous cas” on scan65; it does not concern the later hyperbolic surfaces with their specified canonical metric.

## P-S20. Hua's obstruction to unrestricted shadow surjectivity

Use the sphere with marked points 0,1,∞, a stable hyperbolic type (0,3). In a disjoint system of closed pointed discs, D_0 cannot contain 1 or ∞. Its interior is therefore a simply connected plane domain Ω omitting 1. Choose the normalized Riemann map f:unit disc→Ω, f(0)=0, and set r=|f'(0)|. The Koebe quarter theorem, with exactly this normalization, gives B(0,r/4)⊂Ω. Since 1 is omitted, r≤4. Therefore an assigned tangent disc of radius 5 at zero cannot be the shadow of D_0 in any such system, admissible or otherwise.

This is the argument of **Hua, modernised reading of cote67, §VIII**, p.67 footnote, checked here with the standard quarter-theorem normalization [W4]. It refutes the surjectivity part of the manuscript's map into all positive tangent-disc radii. It does not refute injectivity on an admissible locus, a homeomorphism onto a restricted feasible region, or an unrelated abstract R^ν parametrization of a fibre. No theorem is claimed here for the sharp simultaneous feasible region.

## P-S22. The marked sphere avoids the bare symmetry obstruction

Fix the standard round metric g₀ on P¹(C). For a conformal sphere X with a three-element marked subset A, let F be the six Möbius maps X→P¹(C) carrying A bijectively to {0,1,∞}. Define g=(1/6)Σ_(f∈F)f*g₀ and, if desired, rescale it to area one. This is a positive smooth metric on X. Every isomorphism of marked spheres permutes these six maps, so it pulls back the corresponding metric to g. Thus unmarked P¹'s lack of a metric invariant under all Möbius maps is not an obstruction to a functorial metric on this marked problem.

The averaged metric is not asserted to have constant curvature. Its tangent norms are not asserted to be the shadows of an admissible system. This is a check of the symmetry objection only, not a construction of the section conjectured on scans69–70.

## P-S24. Uniqueness with a boundary triple

A nonidentity Möbius transformation has at most two fixed points: after writing h(z)=(az+b)/(cz+d), its fixed-point equation is a quadratic unless h is the identity. Thus two disc automorphisms taking one specified ordered boundary triple to another must coincide. Existence follows by taking each cyclically ordered triple to (0,1,∞) on the projective real line; the cyclic order ensures the resulting projectivity preserves the chosen half-plane. This checks the normalization argument on scan72, independently of the existence of a welded slit.

## P-S25. Rectifiability of an increasing graph imposes no restriction

Let h:[0,1]→[0,1] be an increasing homeomorphism. For any partition t₀<⋯<t_n,

\[
\sum_j\sqrt{(t_j-t_{j-1})^2+(h(t_j)-h(t_{j-1}))^2}
\leq\sum_j(t_j-t_{j-1})+\sum_j(h(t_j)-h(t_{j-1}))=2.
\]

Taking the supremum gives graph length at most 2. Every such h therefore has a rectifiable graph, including singular increasing homeomorphisms. This does not decide which stronger meaning Grothendieck intended for “rectifiable”; it shows why the word cannot be silently expanded into a sufficient welding condition. Hua §IX explicitly interprets it as absolute continuity in both directions and still leaves the converse unresolved. No equivalence of that class with rectifiable-slit weldings is proved here.

## P-S28. Stability and cutting conventions

If a cut system were allowed to include a contractible simple closed curve bounding a disc, capping that disc and identifying the new centre with the other branch would produce a rational component with one special point. It violates 2g_v−2+n_v>0. Hence the stable-curve conclusion must rely on essential/nonparallel cutting conventions or stabilization. This conditional counterexample does not establish that the manuscript's intended Teichmüller cutting category admits such a cut.

## P-S30. The dimension identity checks only a count

For a connected stable dual graph with v vertices, e edges and ν legs, write g=Σg_v+e−v+1 and Σn_v=2e+ν. Then

\[
\sum_v(3g_v-3+n_v)=3g-3+\nu-e.
\]

Adding one nonzero complex propagation parameter per edge gives 3g−3+ν. This is the numerical identity used in Hua §X. It does not prove that the global admissible-disc data contribute exactly ν real parameters, that the proposed moduli spaces exist with the required structures, or that the specific morphism has invertible differential.

## P-S33. Scope of radius independence

With two fixed coordinate germs z,w and fixed t≠0, the sewing transition w=t/z is holomorphic on every permissible overlap annulus. Altering the cutoff radii while keeping them within those coordinate domains merely changes which representatives of the same overlap are used; the identity on the exterior pieces and the same transition on the collar give the canonical local comparison. This argument presupposes fixed coordinate germs and a common overlap. Replacing globally admissible discs by different embeddings with the same first derivative does not provide those hypotheses; P-S14 shows why a derivative cannot determine the coordinate germ.

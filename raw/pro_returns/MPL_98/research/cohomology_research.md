# Cohomology research memorandum

Status: completed 2026-11-18 02:07 UTC; initially saved for checkpoint at 01:52 UTC. Includes proofs, source checks, the parent's source comparisons, exact finite computation checks, and an independent peer check of COH06–COH07. This is not an alteration or a second transcription of the manuscript.

## Scope and validation handoff

The parent completed the sole manuscript reading and froze the transcription at 2026-11-18 01:36:35 UTC. The final mechanical report in `validation_final_prefreeze_2/validation_report.json` records 43 pages, 694 inventory rows, combined-file consistency, and successful combined compilation. The preserved research copies are `validation_final_report.json` and `validation_final_summary.json`. These are syntax and structure results, not mathematical validation. No transcription source or supplied scan was read for this research task, and no post-freeze source change or optional compilation was made by this agent.

Authorized context read: `context/README.md`, `context/hua_project/README.md`, `context/notes/RESULTS_STATE.md`, and Section III of `context/hua_project/98.modern.tex`. Hua is an AI-produced modernized reading, explicitly not a transcription or an established-result source. All manuscript locators below are provisional associations from Hua's stated page numbers; root must compare them with the frozen reading.

## Findings

### COH01 — The finite-orbit site is valid, but the Čech nerve may leave it

Hua III, “Les G-ensembles comme faisceaux,” page 15 (scan 016), identifies the topos of sheaves on finite-orbit G-sets with the topos of all G-sets. Root confirms that scan 016 literally specifies finiteness of E/G; this is not an inference from Hua alone. The statement is correct with the topology specified by jointly surjective covering sieves. Finite-orbit G-sets form a generating full subcategory, although not in general a category with fiber products. The comparison must therefore use the general sieve formulation, or first pass to a larger site. An explicit reconstruction proof, independent of an unverified comparison-theorem citation, appears in Appendix A.

There is a concrete issue in using the subsequent Čech formula on that small category alone: for an infinite group G and its left regular set T = G, the diagonal G-set G × G has one orbit for every element of G. Thus T belongs to the finite-orbit category but T² does not. The cohomology presheaf must be extended to all G-sets (or a suitable category closed under the required products), for example by H_A^q(S) = Ext^q_{Z[G]}(Z[S], A). Stacks Project, Lemma 21.13.2 (Tag 079Z), explicitly constructs the Čech spectral sequence for an epimorphism of sheaves and permits enlargement of the site. Tag 03A1 requires fiber-product closure and should not be quoted as directly settling this finite-orbit case.

### COH02 — Coinduced modules are acyclic; notation M^G must not mean invariants

Write Coind(M) = Map(G, M), with (g f)(h) = f(hg). There is a natural isomorphism Hom_G(S, Coind(M)) ≅ Map(S, M), given by evaluation at 1, with inverse a ↦ [s ↦ (g ↦ a(gs))]. Every G-module A embeds in Coind(A as an abelian group) by a ↦ [g ↦ ga]; if A is injective this embedding splits. Coind(M) itself need not be injective for arbitrary M: take G trivial and M = Z. Its positive group cohomology nevertheless vanishes, by Shapiro.

For a nonempty T, choose t*. The augmented Čech complex of Map(T^{p+1}, M) is contracted by insertion of t* in the first coordinate. Hence its positive Čech cohomology vanishes. This independently verifies the acyclicity argument used in Hua III, page 17 (scan 018). The notation M^G is genuinely ambiguous here: invariants of the trivial C2-module F2 have H^n(C2, F2) = F2 in all degrees, while the coinduced module Map(C2, F2) has positive cohomology zero. The two readings cannot be interchanged.

### COH03 — Exact construction of the G-set Čech-to-derived spectral sequence

For a nonempty G-set T let P_p = Z[T^{p+1}], with alternating coordinate-deletion differential and augmentation P_0 → Z. Its underlying abelian-group complex is contracted by choosing t* ∈ T, and is therefore exact as a complex of Z[G]-modules. The contraction need not be G-equivariant; equivariance of the differential and exactness of the underlying groups suffice.

For an injective resolution A → I^•, use C^{p,q} = Hom_G(P_p, I^q). Horizontal-first cohomology gives Hom_G(Z, I^q), because each I^q is injective. Vertical-first cohomology gives E_1^{p,q} = Ext_G^q(Z[T^{p+1}], A). The first-quadrant spectral sequence therefore has

\[
E_2^{p,q}=\check H^p(T/e,\mathcal H_A^q)\Longrightarrow H^{p+q}(G,A).
\]

Here H_A^q is the cohomology **presheaf**, not its sheafification. General primary references: Stacks Project, Lemma 21.10.6, Tag 03AZ, and Lemma 21.13.2, Tag 079Z. This is an independent proof of the exact statement with the nerve-enlargement requirement in COH01 made explicit.

### COH04 — Relative version, Shapiro, and Hochschild–Serre

For a surjection T → S of G-sets, replace T^{p+1} by T ×_S ··· ×_S T and the augmentation by Z[S]. The same bicomplex proves an abutment Ext_G^{p+q}(Z[S], A), equivalently the cohomology of the slice topos B_G/S. For S = G/F the slice is equivalent to B_F; the fiber over F of G/F' → G/F is F/F'. This proves that the transitive relative case is the absolute construction for F.

When F' is normal in F, Q = F/F' acts on H^q(F', A), and the nerve yields the usual cochain complex Map(Q^p, H^q(F', A)). Thus E_2^{p,q} = H^p(Q, H^q(F', A)), the Hochschild–Serre spectral sequence. Without normality F/F' is only a set, and the group-quotient formula is unavailable. For S3 with its order-two subgroup, the diagonal and off-diagonal orbits of (S3/C2)² have stabilizers C2 and 1 respectively, illustrating the extra stabilizer data.

Hua's comment that F\\G is inconsistent with left actions needs qualification: left multiplication on G/F is conventional, but F\\G also becomes a left G-set under g·Fx = Fxg^{-1}, and inversion identifies it with G/F. The action convention, not the bare notation, settles the issue. Original primary source: Hochschild and Serre (1953), Chapter I §3, Proposition 3 and its corollary (Shapiro), and Chapter II §4, Theorem 2 (the spectral sequence).

### COH05 — General sheaf version

For an epimorphism T → S in a topos and an abelian sheaf A, the general result is E_1^{p,q} = H^q(T^{p+1}_S, A) ⇒ H^{p+q}(S, A); E_2 is the Čech cohomology of the cohomology presheaf. This is the precise ordinary-cover formulation relevant to Hua III, page 19 (scan 020). Stacks Tags 03AZ and 079Z directly support it. For a hypercover K of X on a site with fiber products, the corresponding spectral sequence E_2^{p,q} = Čech H^p(K, underline H^q(A)) ⇒ H^{p+q}(X,A) is stated and proved in Stacks, Lemma 25.5.3 (Tag 01GY). This supplies a precise theorem for the broader suggestion while keeping its hypotheses explicit.

### COH06 — The proposed low-degree G_m sequence needs hypotheses

Hua III, page 21 (scan 022), explicitly supplies the assumption E_2^{p,1} = 0 for all p and marks the initial zero and the meaning of H³′ as editorial additions. Root reports that the frozen initial mark is uncertain between a bullet and zero, and that the same scan contains a diagram of fields with radical/Galois labels. Therefore the following is a conditional mathematical formulation; it does not identify an unambiguous false assertion in the manuscript. Under the row-vanishing assumption the first-quadrant spectral-sequence filtration does give

\[
0\to E_2^{2,0}\to H^2\to E_2^{0,2}\xrightarrow{d_3} E_2^{3,0}
\to H^3{}'\to E_2^{1,2}\xrightarrow{d_3}E_2^{4,0}\to E_4^{4,0}\to0,
\]

where H³′ = ker(H³ → E_2^{0,3}). The last term must not be silently replaced by H⁴: a later d_4 from E_4^{0,3} can enter E_4^{4,0}. For G_m, Pic(T^{p+1}_S) = 0 is a sufficient E_1-level hypothesis, since H¹(−, G_m) = Pic(−) (Stacks, Theorem 59.24.1, Tag 03P8). Vanishing of the entire q = 1 row is sufficient, not necessary for an individual cover; the identity cover provides elementary instances where the displayed conclusion holds despite a nonzero Picard group.

For the initial injection alone, the exact necessary-and-sufficient condition is that d_2:E_2^{0,1} → E_2^{2,0} vanish. In particular, Pic(T) = 0 suffices. Thus a field T already resolves this initial-injection concern. For a finite extension L/k, every nerve algebra L ⊗_k ··· ⊗_k L is Artinian, including when it has nilpotents, and has Picard group zero. Hence the entire q = 1 row vanishes for such field covers. The same ring-theoretic conclusion holds for algebraic extensions by filtered descent of invertible modules; the site must of course admit the cover being used. This is a verification of the natural field setting, not a correction of it. Details and primary references are in Appendix D.

### COH07 — Explicit counterexample to an unrestricted fixed-cover injection

Let S be the nonsplit real conic x² + y² + z² = 0, and T = S_C ≅ P¹_C. Then T → S is a finite étale C2-torsor. Its degree-zero Čech row is the C2 cochain complex of C×, so Čech H²(T/S, G_m) = R×/N(C×) ≅ Z/2, with nonzero class represented by −1. The invariant generator O(1) of Pic(P¹_C) has a nontrivial descent obstruction d_2 to this group.

Explicitly, the real involution on P¹_C is [z0:z1] ↦ [−bar(z1):bar(z0)]. Its antilinear lift J has matrix [[0,−1],[1,0]] and J² = −I. The induced lift on the tautological line (and its dual) therefore squares to −1. Rescaling by any c ∈ C× changes the square by c·bar(c), a positive real number, so it cannot turn −1 into 1. Consequently d_2([O(1)]) = [−1] ≠ 0. The spectral sequence identifies im(d_2) with the kernel of the **fixed-cover** map Čech H²(T/S, G_m) → H²(S, G_m), disproving unconditional injectivity of that map. This does not refute an assertion about fields in scan 022, nor a comparison using the colimit of Čech groups over all refinements. A refinement locally trivializing O(1) kills this particular obstruction in that colimit. Badr, Bars, and Lorenzo García (2018), Theorem 4.1, p. 1199, state the general Picard-to-Brauer obstruction for Brauer–Severi varieties and credit Lichtenbaum; the explicit proof here does not depend on their citation of a textbook proof.

### COH08 — The four fibrations require local coefficients

Hua III, page 23 (scan 024), lists the homotopy fibrations F → X → Y, X → Y → BF for a principal F-bundle, Y/F → BF → BY for a subgroup F ⊂ Y, and BF → BX → B(X/F) for a normal subgroup. Root confirms that the manuscript itself says the braces denote a local system and deletes “trivial.” The present note credits and rechecks that correction; it does not repair an omitted local-system convention. Under the usual hypotheses making these homotopy fibrations valid, the coefficient system comes from fundamental-group monodromy on fiber cohomology. Serre (1951), Chapter II §8, Proposition 6, p. 454, states this explicitly. For discrete groups the normal-subgroup case is Hochschild–Serre, and the subgroup case with discrete fiber reduces to Shapiro.

The mapping torus of reflection of S¹ is the Klein bottle. Its fiber H¹(S¹, Z) has sign monodromy. Thus H⁰(S¹, Z_sign) = 0 and H¹(S¹, Z_sign) = Z/2; the spectral sequence gives H¹(K, Z) = Z and H²(K, Z) = Z/2. Suppressing monodromy would instead predict Z² and Z, demonstrating why braces or an explicit local-system convention matter. For general topological groups, numerability and suitable quotient/classifying-space hypotheses must also be stated; the arbitrary-topological-group formulations are not certified here.

### COH09 — Cohomological monodromy does not factor through permutation of fiber components

Root reports an explicitly uncertain phrase in the third N.B. on scan 024, potentially relating the action of π₀(X) on H^q(X/F) to its action on π₀(X/F). One possible interpretation—that the former always factors through the component-permutation action—is false. This note refutes that interpretation only; it does not resolve the uncertain words.

Take X = O(2) and F = {I, diag(1,−1)}, the stabilizer of e₁. The equivariant map gF ↦ ge₁ identifies X/F with the connected circle S¹. The element diag(1,−1) belongs to the nonidentity component of O(2) and acts on S¹ by reflection, hence acts by −1 on H¹(S¹,Z). Its permutation of π₀(S¹) is trivial because that set has one element. Thus the correct action can factor through π₀(X), as isotopic elements act identically on cohomology, while retaining information beyond permutation of fiber components. The fibration S¹ → BF → BO(2) is within the standard Lie-group case. This concrete calculation complements, and does not contradict, the manuscript's explicit local-system convention.

## Context search and comparison disposition

Search hits with file and line locators are preserved in `cohomology_context_searches.json`. Hua Section III is the direct comparison source for COH01–COH08; these notes independently prove, qualify, or refute overly broad readings of those modernizations. They do not revise the frozen transcription. The context orientation's request to state the G-set spectral sequence and check special cases is directly addressed by COH01–COH05. `98-axiomatic-norms-can-section` concerns adjacent norm material, not an established cohomology result.

The selected open entries `LM7 E.23`, `FLAGGED_149 B9`, `LM1 D.11`, `LM4 D.12`, and `LM4 F.7` concern different problems (sections/points, an integral μ2 extension, GT torsion, and A5 centralizers). The present calculations provide background only and do not solve or claim to refine any of those entries. Context presence is not evidence that a claim is mathematically established.

## Appendix A — Direct reconstruction of the G-set topos

Here G is an abstract group, equivalently a group with discrete topology. Let C be a small skeleton of the finite-orbit left G-sets, with a sieve on S covering when the images of its arrows jointly exhaust S. Pulling back such a sieve along S′ → S again covers: for each point of S′ choose a point above its image in one of the covering domains, and use the orbit of that pair in the set-theoretic fiber product. That orbit is an object of C, regardless of whether the full fiber product belongs to C. The remaining topology axioms follow from surjectivity and composition.

Every G-set A gives a sheaf S ↦ Hom_G(S,A): an equivariant map is uniquely determined and glued from equivariant maps agreeing over a jointly surjective family. Conversely, for a sheaf P put A = P(G). For g ∈ G let r_g(x) = xg and give A the action g·a = P(r_g)(a). Since r_h ∘ r_g = r_{gh}, contravariance gives P(r_g)P(r_h) = P(r_{gh}), as required for a left action.

The cover G → G/H has relation set

\[
G\times_{G/H}G=\coprod_{h\in H}\{(x,xh):x\in G\}.
\]

Each displayed component is a copy of G and its two projections are id and r_h. The matching condition for its covering sieve is therefore precisely P(r_h)(a) = a for all h ∈ H. Thus P(G/H) ≅ A^H. A finite disjoint orbit decomposition S = ⨿_i G/H_i is a cover, so P(S) ≅ ∏_i A^{H_i} ≅ Hom_G(S,A), naturally in S. This proves the equivalence directly, with no assumption that C has fiber products.

For the product warning, the orbit of (g₀,g₁) ∈ G² is uniquely identified by g₀⁻¹g₁. Hence G² has |G| diagonal orbits. More generally the orbits of G/H × G/K are indexed by H\\G/K, with stabilizers conjugate to H ∩ gKg⁻¹. The nerve must be evaluated in the full topos, or on an enlargement containing these products. In the full category one has

\[
\mathcal H_A^q\!\left(\coprod_iG/H_i\right)
\cong\prod_i H^q(H_i,A),
\]

by Shapiro, the direct-sum decomposition of Z[S], and exactness of products in abelian groups. This provides the explicit extension needed by COH03.

Scope distinction: for a profinite group and **continuous actions on discrete sets**, finite-orbit objects are finite sets, hence their finite products remain finite; the infinite regular G-set is then not a continuous object. That is a different site from the abstract-group site just proved. Continuous group cohomology must be derived in the continuous module category, as in Stacks Tag 0A2H. No unmarked change between these settings is justified.

## Appendix B — Coinduction, contraction, and relative coefficients

For C = Map(G,M), evaluation at 1 sends an equivariant f:S → C to the function a(s) = f(s)(1). Equivariance forces f(s)(g) = a(gs), proving the adjunction formula in COH02. For the Čech coboundary

\[
(dc)(t_0,\ldots,t_{p+1})
=\sum_{i=0}^{p+1}(-1)^i c(t_0,\ldots,\widehat t_i,\ldots,t_{p+1}),
\]

define (hc)(t₀,…,t_{p−1}) = c(t*,t₀,…,t_{p−1}). The summand obtained by deleting t* is c, and all other summands in dh + hd cancel in pairs. Degree zero includes the augmentation by constant functions. The same cancellation in the free-chain complex proves exactness of the augmented P_• used in COH03.

For a surjection T → S, the augmented free-chain complex splits as a direct sum, indexed by s ∈ S, of the augmented complexes on the nonempty fibers T_s. Hence it resolves Z[S] as a chain complex, even though its individual terms need not be projective. Applying Hom_G(−,I^q) to it is exact because I^q is injective. The two filtrations of the resulting first-quadrant total complex yield the stated relative spectral sequence. Its finite filtration in every total degree gives the usual convergence; no boundedness of the whole nerve is required.

The equivalence B_G/(G/F) ≃ B_F sends a G-set over G/F to its fiber over F. Its inverse is B ↦ G ×_F B. For an abelian G-module A, the restricted coefficient object corresponds to Res_F A. Thus the abutment is H^*(F,A). If F′ is normal, the quotient Q acts on H^q(F′,A) by conjugation together with its action on A; different lifts of an element of Q differ by an inner F′-action, which is trivial on cohomology. The orbit decomposition of (F/F′)^{p+1} gives Map(Q^p,H^q(F′,A)), with the inhomogeneous group coboundary. This proves the Hochschild–Serre identification including its coefficient action.

For the C₂ notation test, the standard exact two-periodic free resolution has alternating maps σ−1 and 1+σ. On the trivial F₂-module both maps vanish. On Map(C₂,F₂), both become the matrix with all four entries equal to 1; its kernel and image coincide and have dimension one. The resulting positive cohomology is respectively F₂ and zero in every degree. The calculation file verifies this matrix fact; periodicity and the resolution are the mathematical reason it applies in all degrees.

## Appendix C — Filtration proof of COH06

Use cohomological differentials d_r:E_r^{p,q} → E_r^{p+r,q−r+1} and a decreasing filtration F^pH^n with graded pieces E_∞^{p,n−p}. If E_2^{p,1} = 0, inspecting possible incoming and outgoing arrows gives

\[
\begin{aligned}
E_\infty^{2,0}&=E_2^{2,0},\\
E_\infty^{0,2}&=\ker(d_3:E_2^{0,2}\to E_2^{3,0}),\\
E_\infty^{3,0}&=\operatorname{coker}(d_3:E_2^{0,2}\to E_2^{3,0}),\\
E_\infty^{1,2}&=\ker(d_3:E_2^{1,2}\to E_2^{4,0}),\\
E_4^{4,0}&=\operatorname{coker}(d_3:E_2^{1,2}\to E_2^{4,0}).
\end{aligned}
\]

No incoming differential can reach column zero, so E_∞^{0,3} embeds in E_2^{0,3}. The degree-three edge is H³ → E_∞^{0,3} ↪ E_2^{0,3}; its kernel is F¹H³. Since E_∞^{2,1} = 0, the latter fits into

\[
0\to E_\infty^{3,0}\to F^1H^3\to E_\infty^{1,2}\to0.
\]

Likewise 0 → E_∞^{2,0} → H² → E_∞^{0,2} → 0, because E_∞^{1,1} = 0. Splicing these sequences with the two d₃ maps gives COH06. Only the q = 1 entries at p = 0,1,2,3 are needed for this displayed portion; vanishing of the full row is a convenient sufficient formulation. The possible remaining map d₄:E₄^{0,3} → E₄^{4,0} explains the endpoint caution.

Without row vanishing, the bidegree (2,0) term instead satisfies

\[
E_\infty^{2,0}=E_2^{2,0}/\operatorname{im}
(d_2:E_2^{0,1}\to E_2^{2,0}).
\]

This term equals F²H² and injects into H². Therefore the fixed-cover degree-two edge is injective exactly when that d₂ is zero. Because E_2^{0,1} is a subgroup of H¹(T,A) for a single cover, H¹(T,A) = 0 is sufficient. The proof of Stacks Lemma 21.11.1 (Tag 0CJZ) explicitly uses the corresponding sufficient condition for a covering family.

## Appendix D — Field covers and the real-conic obstruction

Let L/k be finite and put R_p = L^{⊗_k(p+1)}. This commutative k-algebra has finite dimension, hence is Artinian and a finite product of local Artinian rings. A rank-one locally free module over each factor is free; taking their product shows Pic(R_p) = 0. More generally a finite locally free module of constant rank over a semilocal ring is free (Stacks, Lemma 10.78.7, Tag 02M9). Thus nilpotents arising from inseparability cause no Picard obstruction here. If L/k is algebraic but infinite, express L as the filtered union of finite subextensions L_i. The rings R_p are filtered colimits of L_i^{⊗_k(p+1)}. Every invertible module descends to one finite stage (Stacks, Lemma 32.10.3, Tag 0B8W), where it is free. This proves the same Picard vanishing. Finite separable extensions are étale covers; finite inseparable extensions are faithfully flat covers in the fppf topology; an infinite algebraic extension requires an admitting topology such as fpqc. The ring argument does not assert that an infinite extension is an étale or fppf covering morphism.

For the counterexample, the parametrization

\[
\phi([u:v])=[u^2-v^2:i(u^2+v^2):2uv]
\]

is an isomorphism P¹_C → S_C. Substitution verifies the conic equation. If j([u:v]) = [−bar(v):bar(u)], then φ∘j = conjugation∘φ: its three homogeneous coordinates are the negatives of the conjugates of those of φ. This also explicitly identifies the real form, which has no real point since a sum of three real squares vanishes only at the zero vector.

On the tautological line O(−1), the semilinear lift τ(v) = J bar(v), with J = [[0,−1],[1,0]], satisfies τ² = −id. Every other such lift differs from τ by a global unit c ∈ Γ(P¹_C,O×) = C×, and (cτ)² = c bar(c)(−id). Therefore none satisfies the descent cocycle condition. The normalized obstruction cocycle has value −1 on (σ,σ) and 1 when either argument is the identity. Its class is nonzero in

\[
H^2(C_2,\mathbf C^\times)
=\mathbf R^\times/N_{\mathbf C/\mathbf R}(\mathbf C^\times)
=\mathbf R^\times/\mathbf R_{>0}^\times\cong\mathbf Z/2.
\]

Dualizing leaves this order-two class unchanged, so d₂([O(1)]) is the same nonzero class. The Čech nerve of T → S has components indexed by C₂^p, with each component isomorphic to P¹_C. Consequently its units row is precisely the group-cochain complex just used, and the Picard descent cocycle is precisely the d₂ of its Čech-to-derived spectral sequence. Appendix C identifies it with the kernel of the fixed-cover edge. No assertion about the full Brauer group of S is needed.

For a refined cover on which O(1) is locally trivial, the pulled-back Picard class in the source of d₂ vanishes, and naturality makes its image vanish too. This is why the fixed-cover qualification cannot be dropped in favor of an assertion about a colimit over all refinements.

## Appendix E — Fibration conventions and the two monodromy checks

For ordinary cohomology with coefficient ring R, the relevant correspondences are as follows. Group letters are those of Hua's normalized table and are not corrections to the frozen notation.

| Hypotheses and homotopy fibration | Fiber coefficient in degree q | Monodromy source | Abutment |
|---|---|---|---|
| Serre fibration F → X → Y | H^q(F;R) as a local system | π₁(Y) | H^{p+q}(X;R) |
| Numerable principal F-bundle X → Y, classifying map Y → BF | H^q(X;R) | π₁(BF) ≅ π₀(F) in the standard classifying-space setting | H^{p+q}(Y;R) |
| Subgroup F ⊂ Y with the usual quotient bundle, Y/F → BF → BY | H^q(Y/F;R) | π₁(BY) ≅ π₀(Y) | H^{p+q}(BF;R) |
| Normal F ⊲ X, Y = X/F, and the associated BF → BX → BY | H^q(BF;R) | π₁(BY) ≅ π₀(Y), via conjugation | H^{p+q}(BX;R) |

Each E₂ term is cohomology of the base with that coefficient system. These descriptions apply in particular to discrete groups and to the usual closed-subgroup constructions for Lie groups. They are not an assertion that every quotient map of arbitrary topological groups is a fiber bundle. If the relevant monodromy is trivial, the local system becomes constant; simple connectedness of the base is sufficient but not necessary.

For a circle base and a module M with monodromy t, its cohomology is the cohomology of M → M with map t−1. The Klein bottle calculation follows by taking t = −1 on the fiber H¹: its invariants are zero, and its coinvariants are Z/2. Since the base has cohomological dimension one, no higher differential can change these terms. This verifies the significance of the local-system notation that root reports in the manuscript.

For the O(2) example in COH09, the stabilizer of e₁ is exactly {I,diag(1,−1)}. The induced identification of the homogeneous space with S¹ sends left multiplication by diag(1,−1) to (x,y) ↦ (x,−y). This map has degree −1. Its action on H¹ is therefore −1, whereas its action on the single connected component is the identity. Elements of O(2) in the same component are joined by a path, giving homotopic self-maps of the homogeneous space, so the cohomology action does factor through π₀(O(2)). This distinguishes the correct component-group statement from the false stronger component-permutation statement.

## Appendix F — Check record and context disposition by item

| Item | Context search and locator | What this research contributes |
|---|---|---|
| COH01 | “orbites”, “produits fibrés”, “comparaison”; Hua III lines 597–620 | Proves the site equivalence directly; makes the nerve-enlargement step explicit; parent confirms finite-orbit source wording. |
| COH02 | “co-induit”, “M^”, “injectif”, “facteur direct”; Hua III lines 666–676 | Re-proves the adjunction and contraction; preserves the distinction between original notation and Hua's added splitting explanation. |
| COH03 | “suite spectrale”, “recouvrement”, “préfaisceau”; Hua III lines 629–685 | States and proves the exact spectral sequence with ambient category and abutment fixed. |
| COH04–COH05 | “Shapiro”, “G/F”, “distingué”, “Leray”, “Hochschild”; Hua III lines 688–746 | Verifies the relative and normal-subgroup specializations and adds precise ordinary/hypercover references. |
| COH06–COH07 | “Pic”, “Brauer”, “q = 1”, “d_3”; Hua III lines 749–776 | Gives the exact conditional filtration sequence, weaker injection criterion, field-case verification, and a counterexample only to an unrestricted fixed-cover extension. |
| COH08 | “fibration”, “système local”, “trivial”; Hua III lines 779–814; root's source comparison | Credits and rechecks the manuscript's local-system correction rather than alleging an omission. |
| COH09 | Same subsection, particularly the third fibration; root's report of the uncertain third N.B. | Tests one tentative interpretation through O(2)/C₂; leaves the uncertain phrase unresolved. Hua's subsection does not develop that component-permutation interpretation. |
| Project relevance | RESULTS_STATE lines 15–25, 347–351, 460 onward | Addresses the orientation's spectral-sequence request; does not solve the five named open entries or claim a new norm result. |

The companion `cohomology_certificates.py` reads no input and produces `cohomology_certificates.json`. Its completed checks are exact finite algebra: the C₂ matrices over F₂, the insertion contraction on 63 basis simplices through chain degree four (including the augmentation), the conic parametrization and conjugation identities, J² = −I, and the reflection matrix. These are limited computation certificates. The general proofs, the geometric descent identification, and the spectral-sequence filtration arguments are in this memorandum and are not represented as machine formalizations. A separate peer review by the norm-research agent independently checked COH06–COH07, including the fixed-cover limitation and the field refinement; root retains that agent's separate review record.

## Primary references and precise locators

Badr, E., Bars, F., & Lorenzo García, E. (2018). The Picard group of Brauer–Severi varieties. *Open Mathematics, 16*, 1196–1203. https://doi.org/10.1515/math-2018-0101. Theorem 4.1, p. 1199. Author-hosted PDF: https://mat.uab.cat/~francesc/Brauer.pdf

Hochschild, G., & Serre, J.-P. (1953). Cohomology of group extensions. *Transactions of the American Mathematical Society, 74*(1), 110–134. https://doi.org/10.1090/S0002-9947-1953-0052438-8. Chapter I §3, Proposition 3 and corollary, pp. 113–114; Chapter I §7, Proposition 7, pp. 117–118 (spectral sequence and quotient action); Chapter II §4, Theorem 2, p. 125; Chapter III §4, Theorem 2, pp. 129–130 (vanishing assumptions and transgression); Chapter III §5, pp. 130–132 (simple algebras). Accessible original-paper PDF: https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/hochschild-serre.pdf

Serre, J.-P. (1951). Homologie singulière des espaces fibrés. Applications. *Annals of Mathematics, 54*(3), 425–505. Chapter II §8, Proposition 6, p. 454. Original-paper PDF: https://webhomes.maths.ed.ac.uk/~v1ranick/papers/serre.pdf

The Stacks Project Authors. (2026). *The Čech-to-cohomology spectral sequence* (Lemma 21.10.6, Tag 03AZ). https://stacks.math.columbia.edu/tag/03AZ

The Stacks Project Authors. (2026). *Cohomology of epimorphisms of sheaves* (Lemma 21.13.2, Tag 079Z). https://stacks.math.columbia.edu/tag/079Z

The Stacks Project Authors. (2026). *Group cohomology* (Section 59.57, Tag 0A2H). https://stacks.math.columbia.edu/tag/0A2H

The Stacks Project Authors. (2026). *Picard groups* (Theorem 59.24.1, Tag 03P8). https://stacks.math.columbia.edu/tag/03P8

The Stacks Project Authors. (2026). *Čech cohomology and hypercoverings* (Lemma 25.5.3, Tag 01GY). https://stacks.math.columbia.edu/tag/01GY

The Stacks Project Authors. (2026). *Second cohomology and gerbes* (Lemma 21.11.1, proof, Tag 0CJZ). https://stacks.math.columbia.edu/tag/0CJZ. The sentence proving fixed-cover degree-two injectivity uses only the H¹-vanishing on covering domains; the full lemma has additional hypotheses for its gerbe conclusion.

The Stacks Project Authors. (2026). *Finite projective modules* (Lemma 10.78.7, Tag 02M9). https://stacks.math.columbia.edu/tag/02M9

The Stacks Project Authors. (2026). *Descending relative objects* (Lemma 32.10.3, Tag 0B8W). https://stacks.math.columbia.edu/tag/0B8W

All Stacks references were consulted on November 18, 2026. SGA 4 III.4.1 and V.3.3 are comparison locators supplied by the modernized context, not independently verified original-text citations in this draft. Printed primary literature may be inspected for research; no supplied manuscript scan may be inspected by this agent.

# Formal tame inertia and Picard lifting: research memo

Run: MPL_29_049-094; researcher: GPT-6 Astra Pro, `/root/packaging_checks`; reasoning-effort setting not exposed to this agent. Date: 2026-11-18. This work began after the root reported the transcription frozen at 04:03:52 UTC and the context opened at 04:03:58 UTC. No images were consulted and no frozen transcription file was changed.

## Scope, context, and principal conclusions

The evidence read here is the frozen transcription of scans **088, 090, 092, 094**, with scans **089, 091, 093** used only for the neighbouring diagonalizable-group material. The four handwritten leaves are numbered 1–4 in the manuscript; the intervening leaves belong to a different typescript. The context read comprises `context/README.md`, all of `context/notes/RESULTS_STATE.md`, `context/hua_project/README.md`, and the relevant sections of `context/hua_project/29.modern.tex`.

The directly relevant RESULTS_STATE entry is **29-formal-tame-pi1-self-intersection**, credited there to **Hua, findings register**; its status is a claim to check, not an established result. Its modernised interpretation is credited below to **Hua, modernised reading of cote 29**. The listed **LM1 E.11** and **LM1 E.2** concern different group-scheme questions; none of the checks here settles E.11 or rechecks E.2.

| Context location | Hua page(s) | Our scan(s) | Evidence status |
|---|---:|---:|---|
| “Le π₁ modéré d'un schéma formel le long de sa fibre spéciale”; “La situation”, “La suite exacte”, “Lemme 1”, “Lemme 2” | 87, 89 | 088, 090 | Frozen transcription supplied |
| “Le cas où la classe s'annule : Picard formel” | 91, 93 | 092, 094 | Frozen transcription supplied |
| “Le théorème, et deux exemples”; “Exemple I : une courbe sur un corps algébriquement clos” | 95, 97 | 096, 098 | **Outside this package**; modernised context only, no scan verification |
| “Abhyankar semi-global, et la même classe une deuxième fois”; “Le programme kummérien” | 99, 100 | 100, 101 | **Outside this package**; context corroboration/lead only |

The strongest checks are: an explicit tame S₃ quotient disproves unconditional centrality; P¹ disproves the unqualified higher-cohomology curve margin; a degree-one normal bundle on an elliptic curve disproves the inference from π₂=0 to a split extension; and an explicit regular formal torus-torsor supplies prime-to-characteristic torsion in the Picard kernel, disproving the manuscript's unrestricted **unique** divisibility assertion. The existence of a prescribed prime-to-characteristic root of a line bundle can nevertheless be repaired by lifting the root **with its power isomorphism**, a weaker and sufficient route. The general comparison with the tame fundamental group, all formal-effectivity hypotheses, and the complete π₂ exact sequence are not proved here.

## Suggested notes for the final notes file

Each item below has at most four sentences in its proposed note text; detailed checks follow separately.

### FORMAL-01 — Inertia is a module with cyclotomic action

**Witness:** 29/088, immediately below the three-term sequence; **kind:** unpursued implication / own checked correction of context; **words:** “Opérations de … sur I₀ via opérations … sur μ”; **context:** Hua, “La suite exacte”, pp. 87/89 = scans 088/090; **RESULTS_STATE:** 29-formal-tame-pi1-self-intersection.

The manuscript explicitly retains the action on the root-of-unity quotient, whereas Hua calls the extension central without an accompanying trivial-action hypothesis. Over the formal disc over F₂, the tame cover F₄[[s]]/F₂[[t]], t=s³, has group S₃ and noncentral inertia C₃, so the unrestricted centrality assertion is false. The appropriate H² uses the induced, generally cyclotomic, module structure; centrality holds when the action on the actual inertia quotient is trivial. **Own check: high confidence**, from the explicit automorphisms in Appendix A, consistent with [S1].

### FORMAL-02 — Identify the base open U correctly

**Witness:** 29/088, first diagram; **kind:** reading question about the context; **words:** “D₀−D′₀”; **context:** Hua, “La situation” and “La suite exacte”, pp. 87/89 = scans 088/090; **RESULTS_STATE:** 29-formal-tame-pi1-self-intersection.

The frozen diagram identifies the base open with U=X₀−D′₀, whereas Hua defines 𝒰=𝔛−D₀ and then uses the special-fibre fundamental group. When D₀ is the special fibre defined by an ideal of definition, the literal open complement in the formal scheme is empty; a punctured formal neighbourhood requires a separate construction. This is a correction to the modernised interpretation, with no change proposed to the frozen transcription.

### FORMAL-03 — H¹ vanishing is justified at finite tame coefficients

**Witness:** 29/088, Lemme 1 and the margin “constant”; **kind:** unproved claim / targeted proof check; **words:** “H¹(Ũᵗ,J)=0”; **context:** Hua, “Lemme 1”, p. 87 = scan 088; **RESULTS_STATE:** 29-formal-tame-pi1-self-intersection.

For a finite constant coefficient group of order invertible along the relevant boundary, an H¹ torsor at a finite tame level is itself killed by a further finite tame cover, proving the asserted direct-limit vanishing in that range. The displayed low-degree Hochschild–Serre sequence then gives the injection ρ used in the argument, conditional on the standard covering spectral sequence. The manuscript's parenthetical use of the profinite group I requires a specified continuous/inverse-limit cohomology convention and its derived-limit check; finite-level vanishing alone does not automatically supply that extension of the claim.

### FORMAL-04 — The higher-cohomology curve margin has a P¹ exception

**Witness:** 29/088, English margin at Lemme 1; **kind:** own checked counterexample to an unqualified manuscript claim; **words:** “for all Hⁱ, i>0, true if D₀ is curve over a field”; **context:** Hua, “Lemme 1”, p. 87 = scan 088, and “Exemple I”, pp. 95/97 = **outside-package scans 096/098**; **RESULTS_STATE:** 29-formal-tame-pi1-self-intersection.

Take X₀=P¹ over an algebraically closed field and D′₀ empty: its finite étale universal cover is itself, yet H²(P¹,μₙ)=Z/n for every invertible n>1, so the margin as written is false. Hua's later context includes the P¹ exception, but those later scans have not been supplied here and cannot be entered as a verified manuscript withdrawal. **Own check: high confidence**, by Riemann–Hurwitz and the curve cohomology calculation [S2], with the argument recorded in Appendix B.

### FORMAL-05 — The π₂ relation predicts cyclic inertia, including a zero-degree case

**Witness:** 29/090, assertion of equality of the kernel and image; **kind:** own implication, checked conditionally on the proposed exact sequence; **words:** “le noyau est égal à cette image”; **context:** Hua, “Lemme 2” and “Exemple I”, pp. 89, 95/97 = scan 090 and **outside-package scans 096/098**; **RESULTS_STATE:** 29-formal-tame-pi1-self-intersection.

For X₀=P¹ over an algebraically closed field with no other boundary, evaluation of the normal-bundle Chern class of degree d sends the prime-to-characteristic π₂ generator to d times the inertia generator. The proposed quotient is therefore Ẑ⁽ᵖ′⁾(1)/dẐ⁽ᵖ′⁾(1), cyclic of order the prime-to-p part of |d| when d≠0, but the full infinite tame inertia when d=0. **Own check: high confidence for this quotient calculation**, not a proof here of the general formal π₂ exact sequence; Hua's finite-cyclic formulation needs the nonzero-degree qualification.

### FORMAL-06 — Verify the Chern-class identity at finite Kummer level

**Witness:** 29/090, Lemme 2; **kind:** unproved claim / targeted proof check; **words:** “ρ(α)=σ(β)”; **context:** Hua, “Lemme 2 : la classe est celle de l'auto-intersection”, p. 89 = scan 090, and the contextual “programme kummérien”, p. 100 = **outside-package scan 101**; **RESULTS_STATE:** 29-formal-tame-pi1-self-intersection.

For an invertible integer n, taking étale nth roots of the transition functions of the normal line bundle produces the μₙ-valued triple-overlap cocycle defining its Kummer Chern class. The same cocycle measures the failure of the local Kummer identifications to descend, providing a direct finite-level check of the class identity, with the sign tied to the normal/conormal and inertia-generator conventions. This check does not by itself prove the global tame-cover comparison or justify silently exchanging cohomology with the full inverse limit μ∞; [S3] supplies the Kummer sequence, and Appendix C gives the actual cocycle calculation.

### FORMAL-07 — π₂=0 does not imply a split extension

**Witness:** 29/088–090, H² extension class and π₂ quotient; **kind:** own checked counterexample to a context claim; **words:** “L'extension décrite par α∈H²(…)”; **context:** Hua, “Exemple I”, pp. 95/97 = **outside-package scans 096/098**; **RESULTS_STATE:** 29-formal-tame-pi1-self-intersection.

Hua infers an “extension triviale” for every geometric curve other than P¹, but π₂=0 only preserves the full inertia kernel and does not annul the H² extension class. On a complex elliptic curve, a normal line bundle of degree one has nonzero Chern class modulo every n>1; its punctured total space has the circle-bundle relation [a,b]=z, detected by finite Heisenberg quotients. **Own check: high confidence for the nonsplitting and the failed inference**, using the explicit presentation in Appendix B and finite-cover comparison [S4]; the corresponding general formal comparison is kept separate.

### FORMAL-08 — “Already at a finite level” must be applied one finite quotient at a time

**Witness:** 29/092, finite-level reduction; **kind:** unproved claim / own qualification; **words:** “elle est donc nulle déjà … à un niveau fini” and “par définition … lim”; **context:** Hua, “Le cas où la classe s'annule : Picard formel”, p. 91 = scan 092; **RESULTS_STATE:** 29-formal-tame-pi1-self-intersection.

For a fixed finite J₀ the direct-limit definition makes this implication valid, and the cover obtained can depend on J₀. No single finite cover need kill all compatible root-of-unity classes: for a degree-one line bundle on a complex elliptic curve, each class modulo n dies after a suitable multiplication cover, while pullback by any one finite cover has nonzero degree in the full profinite Chern class. **Own check: high confidence**, using degree multiplication [S5]; this distinguishes the finite inertia-realisation argument from an unjustified interchange of the two limits.

### FORMAL-09 — The boundary correction is necessary, and this Picard step does not require disjointness

**Witness:** 29/094, deleted nPic assertion and inserted divisor relation; **kind:** withdrawn/replaced assertion on the same page / own implication; **words:** “β₀=nγ₀+Σλᵢβ₀ⁱ”; **context:** Hua, “Le cas où la classe s'annule : Picard formel”, p. 93 = scan 094; **RESULTS_STATE:** 29-formal-tame-pi1-self-intersection.

Vanishing after restriction to U gives divisibility modulo the classes of the boundary components, not necessarily divisibility in Pic(X₀), and the insertion records exactly that correction. For a regular noetherian X₀ and a dense complement of Cartier divisors, extending a divisor representative of a line bundle on U proves this relation using every irreducible boundary component, even when the components meet. **Own check: high confidence for this localization step**; it does not remove the manuscript's disjointness reservations from the other tame-cover or π₂ steps.

### FORMAL-10 — The unrestricted uniqueness assertion for the Picard kernel is false

**Witness:** 29/094, the underlined divisibility assertion; **kind:** own checked counterexample; **words:** “uniquement divisibles par n”; **context:** Hua, “Le cas où la classe s'annule : Picard formel”, p. 93 = scan 094; **RESULTS_STATE:** 29-formal-tame-pi1-self-intersection.

The square-zero exact sequence gives a quotient of H¹(𝓘) by the boundary of global units, so unique n-divisibility does not pass to this kernel without control of that boundary. Over C, gluing E×Gₘ along a nonzero class a∈H¹(E,𝒪_E) by zⱼ=zᵢ(1+εaᵢⱼ) gives a kernel containing the nonzero n-torsion class represented by a/n modulo Za; the formal gluing zⱼ=zᵢexp(taᵢⱼ) gives a regular formal example satisfying the stated ambient setup. **Own check: high confidence**, with the nontriviality proof in Appendix D; Hua's filtration argument omits this global-unit quotient, and [S6] is used only for the exact sequence, not its separate unqualified torsion-invariance claim.

### FORMAL-11 — Root existence survives without unique divisibility

**Witness:** 29/094, desired formal γ and the boxed qualification; **kind:** own repair of an unproved step; **words:** “Donc il existe γ” and “à vérifier en détail”; **context:** Hua, “Le cas où la classe s'annule : Picard formel”, p. 93 = scan 094; **RESULTS_STATE:** 29-formal-tame-pi1-self-intersection.

If L is a line bundle on a nilpotent thickening and a root M₀ with a specified isomorphism M₀ⁿ≅L|X₀ is given, invertibility of n permits this root pair to lift even when the underlying Picard kernel has n-torsion. A local transition-function proof uses the unique nth root of a principal unit to repair the transitions and their triple-overlap relation, and it produces compatible root pairs through the formal tower. **Own check: high confidence for the finite-thickening root-pair statement**, with formal gluing under the usual adic local-noetherian hypotheses described in Appendix C; this supplies the needed existence without adopting the false unrestricted uniqueness claim.

### FORMAL-12 — The inverse-limit identification has its own hypothesis

**Witness:** 29/094, displayed Pic(𝔛)≃lim Pic(Xₘ); **kind:** unproved claim / proof obligation; **words:** “Pic(𝔛) … lim … Pic(Xₘ)”; **context:** Hua, “Le cas où la classe s'annule : Picard formel”, p. 93 = scan 094; **RESULTS_STATE:** 29-formal-tame-pi1-self-intersection.

Passing from compatible invertible sheaves with transition isomorphisms to the inverse limit of their isomorphism classes can hide a lim¹ of global unit groups. A Mittag–Leffler condition on these unit groups removes that obstruction, and Lipman's formal-Picard argument checks precisely such a condition in a proper setting [S7]. No properness or equivalent global-unit hypothesis is written in the opening setup of scan 088, so this displayed isomorphism should remain a separate obligation rather than follow merely from nilpotent local units.

### FORMAL-13 — Separate the proven containment from realising every finite inertia quotient

**Witness:** 29/090–092; **kind:** unproved claim / own clarification of the proof target; **words:** “s'annule sur Im π₂ᵗ(U)” and “prouver que c'est un isomorphisme”; **context:** Hua, “Lemme 2” and “Le cas où la classe s'annule”, pp. 89/91 = scans 090/092; **RESULTS_STATE:** 29-formal-tame-pi1-self-intersection.

The vanishing of the pulled-back Chern class gives the containment Im(π₂)⊂ker(μ₀→I₀), but the reverse containment requires the finite inertia-realisation argument begun on scan 092. In a profinite formulation one uses the closed image and checks every finite continuous quotient of μ₀/overline{Im(π₂)}, with its induced action; finite quotients then separate the remaining elements. **Own check: high confidence for this abstract separation argument**, not a complete proof here that every required quotient is realised by the intended formal tame covering category.

### FORMAL-14 — Preserve the manuscript's own reservations

**Witness:** 29/090 margin, 29/092 lower margin, 29/094 top insertion and boxed margin; **kind:** self-flagged; **words:** “à vérifier si … indispensable”, “faux” within an uncertain marginal reading, and “à vérifier en détail”; **context:** Hua, “Lemme 2” and “Le cas où la classe s'annule”, pp. 89/91/93 = scans 090/092/094; **RESULTS_STATE:** 29-formal-tame-pi1-self-intersection.

The disjointness hypothesis is explicitly questioned on scan 090 and retained provisionally on scan 094, while the formal Picard conclusion ends with a boxed request for detailed verification. The lower marginal “faux” on scan 092 is too uncertain and insufficiently attached in the frozen reading to identify confidently which statement it rejects. These are author-marked open steps; Hua's fluent concluding proof should not suppress them.

### FORMAL-15 — The intervening typescript clarifies the finite inertia coefficients

**Witness:** 29/089, 091, 093, compared with 29/088; **kind:** own cross-link; **words:** “D(Z/nᵢZ)” and “premier à la caractéristique”; **context:** no dedicated treatment of these interleaved diagonalizable typescripts was found in Hua's modernised cote 29; the nearest relevant discussion is its roots-of-unity inertia section, modern p.87 = our scan088; **RESULTS_STATE:** bears on 29-formal-tame-pi1-self-intersection, with no claimed consequence for LM1 E.11 or E.2.

The typescript's identification of the diagonalizable group associated with Z/nZ as μₙ supplies the finite group-scheme form of the coefficients used on scan 088. The derivative nTⁿ⁻¹ is invertible on μₙ exactly in the tame range, explaining why these root groups are finite étale there and why geometric point counts alone would lose p-primary infinitesimal information. **Own cross-link: high confidence**; the physical alternation of these texts is not evidence that the manuscript explicitly intended this connection.

### FORMAL-16 — The published comparison is identifiable, but not re-proved by bibliographic matching

**Witness:** 29/088–094 as a group; **kind:** literature link / research lead; **words:** “Lemme 2” and “à vérifier en détail”; **context:** Hua's corresponding formal-neighbourhood sections; **RESULTS_STATE:** 29-formal-tame-pi1-self-intersection.

Grothendieck–Murre's 1971 *The Tame Fundamental Group of a Formal Neighbourhood of a Divisor with Normal Crossings on a Scheme*, LNM 208, contains chapters on the irreducible-divisor tame group and comparison of two H² classes, matching the research direction of these leaves [S8]. This bibliographic match supports a precise follow-up against the published hypotheses; it does not establish the unrestricted formulations in the manuscript or in Hua's interpretation. The published theorem text was not available in full for verification in this run.

## Appendix A — Independent centrality counterexample

Let K=F₂((t)), let F₄=F₂(ζ) with ζ²+ζ+1=0, and put L=F₄((s)) with t=s³. The integral map F₂[[t]]→F₄[[s]] is finite, its residue extension has degree two, and its ramification index is three, hence it is tame. Define automorphisms τ(s)=ζs, τ|F₄=id and σ(s)=s, σ(c)=c² for c∈F₄. Then τ has order three, σ has order two, and στσ⁻¹=τ², so Gal(L/K)≃C₃⋊C₂≃S₃ and its inertia subgroup C₃ is not central.

The special fibre Spec F₂ is regular and connected and is the regular divisor t=0 of the regular formal disc. This is already within the stated setup, with no horizontal components needed. The corresponding finite extension is split but not central: thus “split” and “central” must themselves be kept distinct. More generally the action is the root-of-unity, or cyclotomic, action. Its triviality on I₀, not a choice of a geometric generator, is the condition for centrality. Source [S1] independently records the general local-field relation; the six-element example above was worked out here.

## Appendix B — Curve tests and the extension class

### B.1. P¹ and the all-Hⁱ claim

A connected finite étale cover Y→P¹ over an algebraically closed field has, by Riemann–Hurwitz, 2g(Y)−2=−2deg(Y→P¹), hence degree one. Thus the universal finite étale pro-cover of P¹ has no nontrivial connected levels. For invertible n, its H² with μₙ coefficients is Z/n [S2], so this H² does not disappear on the universal cover. This directly refutes the unqualified margin at 088; it does not refute the finite-coefficient H¹ assertion.

In the normal-bundle model with L=O(d), the Chern pairing on the pro-π₂ generator is multiplication by d. Conditional on the proposed inertia exact sequence, write M=∏ℓ≠p Zℓ(1); the quotient is M/dM. For nonzero d, only the prime-to-p factors of |d| survive and this quotient is finite cyclic; for d=0 it is M itself. The latter case should not be hidden in a phrase about a “prime-to-p part” of the degree.

### B.2. An elliptic curve can have a nontrivial extension despite π₂=0

Let E/C be elliptic and L a degree-one line bundle. The complex punctured total space L× retracts onto the oriented circle bundle with Euler class one. Cutting E into its usual fundamental polygon and lifting the boundary loop gives

\[
\pi_1(L^\times)=\langle a,b,z\mid [a,z]=[b,z]=1,\ [a,b]=z\rangle.
\]

The fibre generator z has infinite order; the base E is aspherical, so π₂(E)=0. Reducing the standard integral Heisenberg matrices modulo any integer n>1 gives a finite quotient in which the image of z is nontrivial and [a,b]=z. In particular the profinite group cannot be the product of the two abelian profinite groups that a trivial central extension of π₁(E) by the full inertia would give. Finite-cover comparison [S4] transfers these finite topological coverings to finite étale coverings of the smooth complex algebraic L×.

At finite cohomological level, c₁(L) modulo n is nonzero, and the tame universal pro-cover of E kills H²(−,μₙ) by finite isogenies. Consequently the Hochschild–Serre injection identifies this nonzero class with a nonzero extension class. This disproves the inference “π₂=0, therefore the extension is trivial”; proving the full formal-neighbourhood comparison is a separate task, not supplied by this argument. The nonsplitting example is a standard model used here as a test, with no novelty claim.

### B.3. Nonuniformity in n

For every fixed n, the multiplication-by-n map on E has degree n² and kills c₁(L) modulo n. By contrast, pullback under a fixed connected finite cover f of degree d sends the profinite Chern class to d in ∏ℓZℓ, which is nonzero. The equality of pullback with degree at finite coefficients is [S5]. Equivalently, along a tower of multiplication covers, `lim_n colim_m` of the relevant Z/n classes is zero although `colim_m lim_n` retains a nonzero class, because the transitions on Ẑ are multiplication by nonzero integers. The phrase “already at a finite level” is safe for each finite J₀, not for a single uniform level for μ∞.

## Appendix C — What can be proved in the Chern/root step

### C.1. The finite Kummer cocycle

Fix n invertible and a line bundle L with transition functions gᵢⱼ. After an étale refinement choose hᵢⱼ with hᵢⱼⁿ=gᵢⱼ. On a triple intersection, cᵢⱼₖ=hᵢⱼhⱼₖhₖᵢ lies in μₙ; changing the h's changes c by a coboundary. This is the connecting class of L in the Kummer sequence [S3]. Local nth-root covering identifications have precisely this triple-overlap obstruction. Using local equations of the divisor instead of transitions of its normal line bundle may invert the cocycle, so a sign convention must be fixed rather than silently corrected. This checks the finite coefficient class calculation, not every formal descent assertion in the surrounding argument.

### C.2. Existence of roots through a square-zero thickening

Let X₀⊂X′ have square-zero ideal 𝓘, let n be invertible, let L∈Pic(X′), and suppose a line bundle M₀ on X₀ has M₀ⁿ≃L|X₀. The obstruction to lifting M₀ lies in H²(𝓘). Multiplication by n sends it to the obstruction of M₀ⁿ, which vanishes because L exists; multiplication by n is invertible on H²(𝓘), so M₀ lifts. If M is one lift, L⊗M⁻ⁿ belongs to the Picard kernel, which is a quotient of H¹(𝓘) and therefore is n-divisible, even though it need not be uniquely n-divisible. Dividing that difference and correcting M produces a root of L with the requested restriction.

There is a sharper formulation which is better suited to the formal tower: retain the isomorphism θ₀:M₀ⁿ≃L|X₀ as part of the data. Locally lift frames and the units expressing θ₀. The error in the nth-power transition relation is a principal unit in 1+𝓘, and it has a unique nth root because (1+x)ⁿ=1+nx when 𝓘²=0. Correct the lifted transitions by those roots. Their triple product reduces to one and has nth power one, hence is one; therefore the corrected transitions glue. The same argument controls the isomorphisms of root pairs and extends through a nilpotent filtration.

For an adic locally noetherian formal scheme, applying this construction successively yields compatible root pairs; locally their inverse limits are rank-one free modules, and the transition functions glue them. This is a route to the existence needed in 094 that does not require the abstract kernel to be uniquely divisible or a blanket assertion that Pic is the inverse limit of its groups of classes. In étale language the same phenomenon is the invariance under nilpotent thickenings of the μₙ root gerbe [S9]. Fixing θ₀ matters: different trivializations on X₀ can give different underlying torsion line bundles after lifting, exactly as Appendix D shows.

### C.3. Boundary divisors

For regular noetherian integral X₀ and U=X₀−⋃Eᵢ, a divisor representative of a line bundle on U extends by closure to X₀ and remains Cartier. If L|U is n-divisible, extend a root from U and subtract its nth power: the remaining divisor is supported on the Eᵢ. Thus [L]=n[M]+Σaᵢ[O(Eᵢ)]. This proof uses the irreducible boundary components and does not require them to be pairwise disjoint.

Once such a relation is lifted formally, adjusting the coefficients by multiples of n yields an effective branch divisor with coefficient one on X₀. The usual cyclic root algebra then has inertia of order n at the generic point of X₀; in a normal-crossings chart this is the Kummer equation sⁿ=t₀∏tᵢ^{aᵢ}, with n invertible. This describes the intended finite inertia-realisation construction. The exact formal-cover category, finite normalization/effectivity assumptions in its generality, and all comparison maps remain obligations; this memo does not claim to have proved the entire theorem from these leaves.

## Appendix D — A counterexample to unrestricted unique divisibility

This is an independent construction, not copied from the context or an external source. It uses a nonproper X₀; no properness hypothesis appears in 088.

Let E/C be an elliptic curve, choose a finite affine cover (Uᵢ), and represent a nonzero class a∈H¹(E,𝒪_E) by an additive Čech cocycle aᵢⱼ. Glue

\[
U_i\times\mathbf G_m\times\operatorname{Spec}\mathbf C[\varepsilon]/(\varepsilon^2)
\]

using the identity on E and ε, and the coordinate changes zⱼ=zᵢ(1+εaᵢⱼ). The cocycle relation for the aᵢⱼ makes these gluing maps compatible. The resulting scheme X′ is a first-order thickening of X₀=E×Gₘ with ideal sheaf 𝓘≃𝒪_{X₀}.

Fix n>1 and define a line bundle M on X′ with transitions 1+εaᵢⱼ/n. Its restriction to X₀ is trivial. Its nth power has transitions 1+εaᵢⱼ=zⱼ/zᵢ and is therefore trivial, using the invertible local fibre coordinates zᵢ. Thus [M] belongs to both Pic(X′)[n] and ker(Pic(X′)→Pic(X₀)).

To show M is nontrivial, suppose its transitions were a coboundary of local units hᵢ. Their reductions would glue to a global unit on X₀, necessarily c zᵐ for c∈C* and m∈Z, because Γ(E×Gₘ,𝒪)=C[z,z⁻¹]. Write hᵢ=c zᵢᵐ(1+εbᵢ). The transition relation then implies

\[
(1/n-m)a_{ij}=b_j-b_i
\]

up to the harmless simultaneous convention for the direction of transitions. Pullback H¹(E,𝒪_E)→H¹(E×Gₘ,𝒪) is injective, since the section z=1 splits it. Hence the nonzero class a would satisfy (1/n−m)a=0, impossible over C. This proves that [M] is a nonzero n-torsion element of the Picard kernel. The kernel's portion in the direction a is concretely C a/Z a, and it is divisible but not uniquely divisible.

The example is not confined to a possibly nonregular first-order ambient object. Replace the transition maps by

\[
z_j=z_i\exp(t a_{ij})
\]

on Uᵢ×Gₘ×Spf C[[t]]. The formal exponential is well-defined t-adically in characteristic zero and preserves the cocycle relation. The glued formal scheme is regular and connected, with regular special-fibre divisor X₀=E×Gₘ, and the line bundle with transitions exp(taᵢⱼ/n) has nth power trivial and nontrivial first-order restriction. Its Picard kernel therefore also contains nonzero n-torsion. This is within the stated setup of 088, with D=D₀.

The failure is precisely the global-unit boundary in

\[
\Gamma(X',\mathcal O^*)\to\Gamma(X_0,\mathcal O^*)
\xrightarrow{\delta}H^1(X_0,\mathcal I)
\to\ker(\operatorname{Pic}(X')\to\operatorname{Pic}(X_0))\to0.
\]

Here δ(czᵐ)=m a, whose image Za is not n-saturated in the C-vector space. If this image is uniquely n-divisible—for example if the units all lift—then the quotient is uniquely n-divisible, but the hypothesis must be supplied. In proper geometrically connected situations over a field, lifting constants and controlling nilpotent global units can supply such a repair; it is not automatic in the general opening setup.

**External-source discrepancy requiring follow-up.** The retrieved version of Stacks Lemma 37.4.2 (Tag 0C6S, reached through [S6]) states an unqualified isomorphism on Pic[n] for all thickenings. That statement conflicts with the explicit example just proved; the retrieved page also contains a comment questioning the injectivity step. This memo uses only its preceding correct square-zero exact sequence and does **not** treat the separate torsion-invariance statement as a verified input. The counterexample is supplied in full so this discrepancy can be independently checked, rather than resolved by an appeal to authority.

## Appendix E — Profinite exactness and inverse limits

### E.1. The reverse containment in the inertia quotient

Suppose μ is profinite, K is the closed image of the proposed π₂ map, and μ→I is a continuous quotient with K in its kernel. To prove its kernel is exactly K, it suffices to show that every finite continuous quotient of μ/K factors through I in the prescribed compatible way: any element not in K is separated from K by one such finite quotient. This is the abstract content of the finite-J₀ argument in 092. The fact that μ is procyclic simplifies which finite kernels occur, but it does not justify omitting the action, compatibility, or the existence of the tame covering that realises them. If π₂ is being used as a pro-object instead of a compact group, the formulation should first be made at the finite coefficient level.

### E.2. Picard groups versus the groupoid of compatible line bundles

For a countable formal tower under the usual sheaf-effectivity hypotheses, the difference between compatible invertible sheaves and compatible isomorphism classes is measured by a lim¹ of Γ(Xₘ,𝒪*). Concretely, a line bundle trivial at every level can still be represented by a sequence of incompatible choices of trivializations; changing them modifies the sequence by the standard `1−shift` coboundary in the product of the unit groups. A Mittag–Leffler condition kills that obstruction. Lipman's proof [S7] checks precisely a unit/global-section Mittag–Leffler condition in its proper setting. This memo gives no example of a nonzero lim¹ for the manuscript's specific tower and therefore records this as a proof obligation, not as a blanket refutation of the displayed Picard-limit isomorphism.

## Primary sources consulted and exact scope of use

The sources below are primary mathematical texts or the Stacks project's own proofs. None is used to alter the frozen transcription.

**[S1]** Jeremy Booher, Sean Cotner, Shiang Tang, *Lifting G-Valued Galois Representations when ℓ≠p*, Forum of Mathematics, Sigma 12 (2024), e109, §5.1, Lemma 5.1. DOI: https://doi.org/10.1017/fms.2024.113 ; accessible article: https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/lifting-gvalued-galois-representations-when-ell-neq-p/1A84232602F99426E2C6AFE012A1632C . Used only for the tame-inertia/cyclotomic-action statement; the F₂ S₃ example was independently computed.

**[S2]** Stacks Project, Lemma 59.69.1, Tag 03RQ: https://stacks.math.columbia.edu/tag/03RQ . Used for H²(C,μₙ)=Z/n on a smooth proper geometric curve; the P¹ no-cover argument and quotient calculations are given here.

**[S3]** Stacks Project, §59.28, Kummer theory, Tag 03PK: https://stacks.math.columbia.edu/tag/03PK . Used for the étale Kummer sequence when n is invertible and its connecting class. The cocycle and root-lifting calculations in this memo are independent checks.

**[S4]** J.S. Milne, *Lectures on Étale Cohomology*, version 2.10 (2008), Theorems 21.1, 21.3, 21.5, printed pp.125–127: https://www.jmilne.org/math/CourseNotes/LEC210.pdf . Used only for comparison of finite complex topological and finite étale coverings/cohomology; no formal-neighbourhood comparison is attributed to it.

**[S5]** Stacks Project, Lemma 59.69.2, Tag 0AMB: https://stacks.math.columbia.edu/tag/0AMB . Used for degree multiplication on H² of smooth projective geometric curves. The nonuniform-finite-level example is the inference made here from that formula.

**[S6]** Stacks Project, §37.4, Tag 0C6Q, specifically Lemma 37.4.1/Tag 0C6R: https://stacks.math.columbia.edu/tag/0C6Q . Used for the full square-zero units–Picard exact sequence, including the global-unit boundary. Its separate Lemma 37.4.2/Tag 0C6S was scrutinized and **not accepted as an input** for the reasons in Appendix D.

**[S7]** Joseph Lipman, *Picard schemes of formal schemes; application to rings with discrete divisor class group* (1974), §2.4, printed pp.112–114; properness hypotheses are in §2.2, p.108. Author's copy: https://www.math.purdue.edu/~jlipman/papers-older/%5B1974%5D%20Picard%20schemes%20of%20formal%20schemes:%20application%20to%20rings%20with%20discrete%20divisor%20class%20group.pdf . Used only for the explicit Mittag–Leffler step in this proper setting.

**[S8]** Alexander Grothendieck and Jacob P. Murre, *The Tame Fundamental Group of a Formal Neighbourhood of a Divisor with Normal Crossings on a Scheme*, Lecture Notes in Mathematics 208 (1971): https://doi.org/10.1007/BFb0069608 ; publisher contents: https://link.springer.com/book/10.1007/BFb0069608 . Bibliographic/table-of-contents verification only; full theorem text not checked here.

**[S9]** Stacks Project, Proposition 59.45.4, Tag 03SI, and §59.45, Tag 04DY: https://stacks.math.columbia.edu/tag/03SI ; https://stacks.math.columbia.edu/tag/04DY . Used for invariance of the small étale site/cohomology under nilpotent thickenings; the root-pair argument is also spelled out directly above.

## Checks versus outstanding work

**Actually checked:** the finite S₃ relation and noncentrality; the P¹ H² counterexample; the elementary quotient M/dM; the elliptic circle-bundle/finite-Heisenberg obstruction to splitting; finite-level nonuniformity; the square-zero/global-unit counterexample and its regular formal extension; root existence with a fixed power isomorphism through nilpotent thickenings; the abstract profinite separation argument; the regular-scheme Picard localization step.

**Used with a stated external theorem:** geometric curve H², its pullback degree, Kummer exactness, complex finite-cover comparison, nilpotent étale invariance, and Lipman's proper Mittag–Leffler verification. Reading these statements is not counted as independently reproving them.

**Not established here:** the full general tame fundamental-group exact sequence; all coefficient/pro-homotopy conventions; the necessity of disjoint horizontal divisors in every step; universal finite normalization/effectivity in the original generality; automatic Picard-limit injectivity without a unit condition; the original text on absent scans 096/098/100/101; or any claim of novelty. The final notes should retain the manuscript's own verification flags and the conditional scope of the supporting arguments.

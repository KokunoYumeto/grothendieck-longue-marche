# LM_P045 (scans 441–450): research notes, checked against the corrected text

Each first-pass note (R01–R29, section 5 of `answers/unzipped/LM_P045/LM_P045_notes.md`) is checked against `second_pass/LM_P045_checked.tex` and marked **keep**, **correct** or **drop**, with a reason. Notes C1–C4 are new and labelled *Claude, second pass*. Scan numbers are file scans (manuscript pages 223–227). The theorem's hypotheses and the admitted Lemma are on scan 440 (package LM_P044): U an oriented surface (séparée, connexe, paracompacte), not S², σ an antiinvolution, ℰ the extension of Z/2 by π = Aut(Ũ/U).

## First-pass notes, checked

- **R01 — 441 — unproved claim — keep, context corrected.** "(Pour mémoire) U^σ est une sous-variété fermée de U de dim 1." The hypotheses are on 440, not missing. The claim is classical: a periodic homeomorphism of a surface is locally conjugate to an orthogonal map (Brouwer, Kerékjártó; Eilenberg 1934), and an orientation-reversing involution is then locally a reflection. develop: no.

- **R02 — 441 — own idea — keep.** Sc(ℰ, Z/2), now read with certainty, is the set of π-conjugacy classes of splittings, i.e. the non-abelian cohomology set H¹(Z/2, π) once one splitting is fixed. A standard reformulation. develop: no.

- **R03 — 441–442 — unpursued implication — keep, updated.** By (7) and d), the fixed subgroup of a lift is trivial for a line component and infinite cyclic for a circle, with π^{σ_i} = Im φ_i after replacing φ_i (the ink has φ_i, not g_i) by a conjugate. The text proves this on 444–445 ((11), (14)), so the "detection of compactness" is established here, modulo the Lemma. develop: no.

- **R04 — 442 — unpursued implication — correct.** The ink reads "quitte à remplacer φ_i par un conjugué". Replacing φ_i by int(α)∘φ_i is the same as replacing g_i by αg_iα⁻¹, so the point stands: the equality concerns the fixed subgroup of the chosen lift σ_i, up to that conjugation.

- **R05 — 442 — dependency on the Lemma — keep, context corrected.** The Lemma is stated on 440 and explicitly admitted ("On admettra le Lemme"): every antiinvolution of the disk or of C is conjugate to z ↦ z̄, so its fixed set is ≃ R, non-empty and connected. It is applied to Ũ ≃ R², since U is oriented and ≠ S². Classical (Brouwer, Kerékjártó; Eilenberg 1934). develop: no.

- **R06 — 443 — unpursued implication — correct.** The parenthesis reads "(assez triviale de ttes façons)": the author calls the factorisation of (5) through π₀(U^σ) rather trivial anyway. The first pass's "triviale de ses fibres", a claim about fibres, is not in the ink. The substantive step is the bijectivity of (6), which comes from (10).

- **R07 — 444, (10) — compressed step — keep, updated.** In the main-line insertion the target is written Ũ^{σ_i} with no index; the diagonal margin writes Ũ_i^{σ_i}, the consistent form. The step is complete modulo the Lemma: Z̃_i → Ũ_i|Z_i is a morphism of coverings of Z_i, so its image is open and closed; it lies in the connected Ũ_i^{σ_i} and so equals it; Ũ_i^{σ_i} ≃ R is simply connected, so the covering Z̃_i → Ũ_i^{σ_i} has one sheet. develop: no.

- **R08 — 444 — own idea — drop.** Testing the covering argument on a line and on a circle adds nothing: the text treats both cases explicitly, (11) for Z_i ≃ R and (12)–(14) for Z_i ≃ S¹.

- **R09 — 445 — claim without proof — keep.** "σ_i (opérant trivial^t sur T_i, et sur π_i par transport de structure) commute à l'hom injectif φ_i" is asserted. It holds because σ_i acts on the whole square (9)/(8) and fixes Z_i and Z̃_i pointwise, so conjugation by σ_i on deck groups is compatible with Z̃_i → Ũ_i. Routine. develop: no.

- **R10 — 445, margin — restriction — correct.** The margin "et X_g/σ non orientable...." is now read with certainty; it has no insertion mark, and the witnesses put it into the statement. It carries over the restriction in the margins of 439–440: the labelling σ_i ↔ i = card π₀(X^σ) classifies (X, σ) only when X/σ is non-orientable. Parts a)–c) do not need it: by the theorem, the number of Π_g-conjugacy classes of order-2 lifts is the number of fixed circles for every antiinvolution.

- **R11 — 445–446 — own idea — correct.** Comparing antiinvolutions with the same i but quotients of different orientability is the separating / non-separating distinction of Weichold's classification of real structures (non-separating: 0 ≤ i ≤ g; separating: 1 ≤ i ≤ g+1, i ≡ g+1 mod 2). This is known (Weichold 1883; see Natanzon's surveys on real algebraic curves). For the count of lift classes it changes nothing (see R10). develop: no.

- **R12 — 446 — slip of the pen — keep.** "Soit Y_{g,i} = X_g^{σ_i}, surface compacte à bord non orientable connexe de type (g−i, i)": the exponent is in the ink, but the description fits the quotient X_g/σ_i, not the fixed set. The witnesses keep the slip. The first index of Y is overwritten.

- **R13 — 446–447 — claim without proof — keep.** "Il est bien connu, et immédiat" that the automorphism group of Y acts transitively on π₀(∂Y): any permutation of the boundary circles of a connected compact surface is induced by a homeomorphism (classification of surfaces). Lifting to (X_g, σ_i) uses the correspondence of 439–440 for non-orientable quotients. develop: no.

- **R14 — 447 — compressed step — keep, updated.** The ink closes a parenthesis after h ("$h$), le choisir") with no opening one. The step is immediate: if u′_i = int(α)(int(h)u_i) with α ∈ Π_g, replace h by int(α)h, which has the same image ḣ and stays in 𝒢_g^+ because inner automorphisms preserve orientation. develop: no.

- **R15 — 447–448 — claim proved in the text — keep, with a warning on the witnesses.** "L'indice de 𝒢_g^{+u_i} dans 𝒯_g^{+σ_i} est i" means the image of 𝒢_g^{+u_i}, whose kernel is T. The proof on 448 is an orbit–stabiliser count: 𝒯_g^{+σ_i} acts on the i classes of 1 a) transitively (interlinear "transitivement", from c)) and the stabiliser of the class of u_i is the image. The CSG, IUT and CK print "opère trivialement", under which the index would be 1; readers of those editions should use the manuscript reading.

- **R16 — 447 — claim without proof — keep.** The two vertical inclusions have index 2 because u_i lies in 𝒢_g^{u_i} and σ_i in 𝒯_g^{σ_i}, and both reverse orientation; the "+" subgroups are the kernels of the orientation character. Immediate. develop: no.

- **R17 — 445, 447 — boundary case — keep, confirmed.** The ink has (0 ≤ i ≤ g); the witnesses print (1 ≤ i ≤ g). For i = 0 the theorem gives no order-2 lift (X^σ = ∅), so a) holds with 0 classes and b), c) and Corollaire 2, which choose u_i, are vacuous.

- **R18 — 447, (16) — own idea — keep; develop: yes.** The extension in (16) has kernel T ≅ Z, on which the quotient acts through ±1 (orientation of the fixed circle; see C4). **Statement to attack:** for g ≥ 2, 1 ≤ i ≤ g and X_g/σ_i non-orientable, decide whether 1 → Π_g^{u_i} → 𝒢_g^{+u_i} → Im(𝒢_g^{+u_i} → 𝒯_g^{+σ_i}) → 1 splits. **Status:** the orientable analogue, the boundary-capping extension 1 → Z → Mod(S_g^1) → Mod(S_{g,1}) → 1, is a non-split central extension classified by the Euler class; for this non-central, real (Klein-surface) version I know no reference.

- **R19 — 448 — own idea — keep, downgraded.** The passage from "int(γ)u_i Π-conjugué à u_i" to α⁻¹γ ∈ 𝒢_g^{+u_i} is the standard orbit–stabiliser argument in 1 → Inn(Π) → Aut(Π) → Out(Π) → 1 for a centre-free Π. Complete in the text. develop: no.

- **R20 — 448, cancelled Corollaire 3 — cancelled claim — correct.** With the corrected reading, the cancelled text says: for U a connected surface with boundary, not RP², Π = π₁(U) has torsion iff U is non-orientable and ∂U has at least one compact component; torsion elements have order 2, and their conjugacy classes correspond to the compact components of ∂U (not "non compactes"). Since π₁ of a surface other than RP² is torsion-free, Π must stand for the group ℰ of the theorem for the oriented double of U; but then, by (6)–(7), every boundary component, compact or not, gives a class of order-2 elements, and orientability of U plays no role. As read, the statement conflicts with the theorem; it is struck in the manuscript. develop: no.

- **R21 — 449 — construction aim — keep, updated.** "J'ai envie de construire une figure géométrique où on puisse mettre en évidence simultanément" the antiinvolutions giving the σ_i and the associated u_i, "(ce qui sera alors facile, par la recette générale)": the author expects the u_i to follow at once from the figure by the construction of (5) on 442. The construction begins on 449–450 and continues past this package.

- **R22 — 449 — claim invoked as known — keep.** "Nous savons que σ_i ∈ 𝒯_g s'obtient en regardant un X_g comme doublement orienté d'un Y = Y_{g−i,i}" refers to the Proposition on 439 (non-orientable quotients of type (γ, μ), γ + μ = g). The explicit model from RP² with g holes, g−i of them closed by Möbius bands, is checked in R25. develop: no.

- **R23 — 449 — unpursued implication — keep, updated.** The boxed V_{0,j} = Y_0 ∖ ⋃_j D̊_j (index j, now read) is called V_0 on 450; the j in V_{0,j} is a slip, since j is the union index. V_0 lies in both Y_0 and Y_{g−i,i} and agrees with Y along ∂Y = ⋃_{g−i+1 ≤ j ≤ g} ∂D_j, so it is the common piece from which all the σ_i can be built.

- **R24 — 450 — claim without proof — drop.** The restriction of the orientation cover X_0 → Y_0 to a closed disk D_j is trivial because D_j is simply connected, and its two sheets are the two orientations of D_j by definition of the orientation cover. Nothing to prove.

- **R25 — 450 — own idea — correct (check done).** χ(V_0) = χ(RP²) − g = 1 − g and the Möbius bands add 0, so Y has χ = 1 − g and i boundary circles; its oriented double has χ = 2 − 2g, genus g. So (21) must read Y_{g−i,i}, as on 449, whatever the doubtful sign in the ink. The author's "genre" g−i of Y is the number of Möbius bands added to RP² (crosscap number g−i+1), and the index of M_i in (20) is a slip for M_j.

- **R26 — 450, cancelled map — cancelled claim — correct.** The target of the cancelled map is X (X_{g−i,i} with the first index struck, or X_{g,i}), not Y. The witnesses show that the map returns after these pages as (24) U_0 → X_{g,i}, a homeomorphism once the ∂Δ_j for g−i+1 ≤ j ≤ g are contracted, so the abandoned formulation was resumed in corrected form.

- **R27 — 450 — own idea — keep.** X_{g,i} = X_g ∖ Int(M̃), the complement of the lifted Möbius bands, is the common subsurface on which the involutions for the various i can be compared; the text confirms this use in (23)–(24) beyond this package. develop: no.

- **R28 — 441–445 — own idea — keep; develop: yes.** The theorem is the discrete, topological core of the real section conjecture: π₀(U^σ) ≅ π-conjugacy classes of splittings, fixed subgroup 1 or ≅ Z. **Statement to attack:** for g ≥ 2 and an antiinvolution class σ_i with i ≥ 1 fixed circles, every order-2 lift u of σ_i to Aut(Π̂_g) is Π̂_g-conjugate to the completion of one of the i discrete lifts, and its fixed subgroup Π̂_g^{u} is the closure of Π_g^{u_k}, ≅ Ẑ. **Status:** the first part is equivalent to the real section conjecture for real curves (sections up to conjugacy ↔ π₀(X(R))), proved by Mochizuki (2003) and by Pál (2011) with Smith theory for pro-spaces; see also Stix, LNM 2054 (2013). I have not found the fixed-subgroup statement; given both, the profinite form of Corollaire 2 (index i) follows by the same orbit–stabiliser argument.

- **R29 — 443–445 — reading aid — keep.** Hatcher, *Algebraic topology*, §1.3 (lifting criterion, deck transformations) covers the covering-space steps; it does not replace the admitted Lemma. develop: no.

## New notes (Claude, second pass)

- **C1 — 445–446 — implication not pursued — Claude, second pass.** Corollaire 1 a) settles half of the hope stated on 440, "ces classes sont distinctes": the number of Π_g-conjugacy classes of order-2 lifts is an invariant of the class in 𝒯_g, so σ_i and σ_j with i ≠ j are not conjugate, as the text says. The other half, that every σ ∈ 𝒯_g satisfying (4) lies in one of the g+1 classes, is not addressed here. It needs Nielsen realisation for Z/2 (Nielsen 1942; Kerckhoff 1983), and without the margin's restriction it is false, since separating antiinvolutions give further classes (Weichold). develop: no (known).

- **C2 — 448 — cancelled claim, false as stated — Claude, second pass.** The struck first proof begins "1°) 𝒢_g^{+u_i} → 𝒯_g^{+σ_i} est surjectif". By Corollaire 2 the image has index i, so this fails for i ≥ 2. The struck argument cannot work: u′_i = int(γ).u_i is already conjugate to u_i by γ, so c) yields nothing new, and the author struck the exponent u_i of the h that c) provides (change 37), since c) gives h only in 𝒢_g^+. He replaced the claim by the stabiliser count.

- **C3 — 446 — notation — Claude, second pass.** 𝒢_g = Aut_lac(Π_g) (read lac, not loc). On earlier pages Aut_lac denotes automorphisms that respect the conjugacy classes of the loops ("lacets") around the holes; a closed surface group Π_g has none, so 𝒢_g = Aut(Π_g), 𝒢_g^+ is its orientation-preserving part, and 𝒯_g = A_g/A_g° ≅ 𝒢_g/Inn(Π_g) by Dehn–Nielsen–Baer. develop: no.

- **C4 — 447–448 — own idea — Claude, second pass.** Topological reading of Corollaire 2: an order-2 lift u_i corresponds to σ_i with a base point on one fixed circle Z, 𝒢_g^{u_i} to mapping classes of (X_g, σ_i) fixing that point, and T ≅ Z to pushing the point once around Z, on which the quotient acts by ±1 according as Z keeps or reverses its direction. In the quotient Y the index i is the index of the stabiliser of one boundary circle in a group permuting the i boundary circles transitively (R13), which checks Corollaire 2 independently. This dictionary, through the correspondence between the centraliser of σ_i and the mapping classes of Y, is my heuristic and is not stated in the manuscript; it frames the splitting question of R18.

# LM_P028 (scans 271–280): research notes checked against the corrected transcription

Each first-pass note (R01–R20) is checked against `LM_P028_checked.tex` and kept, corrected or dropped. Quotations follow the corrected text. Notes M01–M09 are the second pass's own, labelled as such. None of the first-pass notes is dropped.

## First-pass notes

### R01 — keep
**Scan 271 · claim to be proved.** The paragraph ends "A prouver que α et β sont homotopes": two paths α, β from f to g in Isom_Γ(U,U') that induce the same isomorphisms on the topossic diagram B_{D*,Γ} → B_{U,Γ} → B_Γ should be homotopic. Scan 272 reduces this to g = id, U = U_{g,ν}, f ∈ A^Γ_{g,ν}, and then to injectivity of π_1(A^Γ) → π_1(A). No proof is given in this package.

### R02 — correct (attribution now legible)
**Scan 272 · claim without proof.** The boxed "π_1(A^Γ) → π_1(A) est injectif" is derived from the case Γ = 1. The parenthesis attributes that case to Ladegaillerie (ink "Ladegallerie"); the first pass had it as illegible. Grothendieck then uses π_1(A) = 0 "(cas (g,ν) anabélien)" to reduce the claim to π_1(A^Γ) = 0. The exact statement of Ladegaillerie's result is not on the page and should be identified in the literature before the reduction is relied on.

### R03 — keep
**Scan 273 · provisional claim.** 1-faithfulness is stated as "∀ isomorphisme entre B_f et B_g provient d'un chemin de f à g". After the reductions it becomes an isomorphism of f* : (B_{D*} → B_U) → (B_{D*} → B_U) with the identity (the corrected text has "d'où f*" here). The sentence breaks off at "sauf erreur cette condition", and the rest of the page is blank. CSG and IUT silently end it at "l'identité."

### R04 — correct (notation)
**Scan 274 · claim without proof.** The Gr-category A̲ has the naive fundamental groupoid of A as underlying category and composition induced by A × A → A, with invariants π_0, π_1 and the action of π_0 on π_1. The page says that "l'associativité dans A̲ = ΠA est stricte"; the ink has Π without index, where the first pass read Π_1. Strictness holds because the product of points and of path classes is computed pointwise from the associative multiplication of A. The recovery of the π_0-action on π_1 is not written out.

### R05 — correct (quotation)
**Scan 274 · claim without proof.** Corrected quotation: "tout torseur sous A définit un 1-torseur sous la gr-catégorie A̲"; the first pass had "sur … sur". The relative version for a space S, or a topos locally a space, gives an A̲_S-champ which is a champ of A_S-torsors. No construction of the gluing or descent data is given.

### R06 — correct (reading of the levels)
**Scans 274–275 · claim without proof.** With the corrected reading the statement is: if π_i(A) = 0 for i ≥ 2, then for every n ∈ N, n ≥ 2, there is an n-équivalence (the n before "équivalence" is uncertain) between the n-category of torsors on S with group A_S and the n-category deduced from the 2-category of (gerbes?) A̲_S-torsors by extending it discretely. My reading in modern terms: A is a homotopy 1-type, so its torsors are classified by its Gr-category. The page gives no proof, and the inserted word read "gerbes" is unresolved.

### R07 — correct (formula)
**Scan 275 · claim without proof.** The display reads Transp_A(u,v) = {g ∈ A | v = int(g).u}; the first pass dropped the parentheses. The claim that the components of the 2-category correspond to conjugacy classes of homomorphisms Γ → A relies on every A-torsor over a point being trivial (see M05). Continuity of the action and the topology of Transp are not specified.

### R08 — keep
**Scan 276 · claim without proof.** The 0-isotopic and 1-isotopic categories replace Transp(u,v) by its π_0 and by its Π_1. Then Aut(u) ≃ Π_1 Trans(u), with Trans(u,u) = A^u the centraliser of u, and Isom(u,v) is empty "(si u,v ne sont conjugués)" or a torsor under Aut(u). The torsor claim comes from Transp(u,v), when non-empty, being a right A^u-torsor under multiplication. Compatibility of composition with paths and homotopies is not written out.

### R09 — correct (quotation)
**Scan 277 · question / programme.** Corrected quotation: "On aimerait encore exprimer des conditions pour que ce[t] 2-foncteur soit une 2-équivalence"; the first pass had "avoir exprimées". This is an explicit request for a criterion. Scans 278–280 answer it only in the simplified case π_1 = 0.

### R10 — keep
**Scans 277–278 · implication not pursued.** The text asks for the classification of equivalence classes of objects of the target 2-category, which are "de nature purement algébrique" in terms of A̲ and Γ. It identifies an action of Γ on the trivial A̲-torsor with a morphism of Gr-categories from the discrete Gr-category Γ to A̲. The classification beyond trivial torsors is not carried out.

### R11 — keep
**Scan 278 · open definition.** Hom(u,v) is to be a category, not only a set, defined as a sub-category Transp(u,v) of A̲ "à définir ad-hoc". The definition is left open on these pages.

### R12 — keep
**Scan 278 · simplification stated without proof.** Under π_1 = 0, A̲ "se réduit à π_0", and homomorphisms Γ → A̲ reduce to homomorphisms Γ → π_0. For a Gr-category with trivial π_1 this is an equivalence with the discrete Gr-category π_0. Everything on scans 279–280 is done under this hypothesis, as the insertion "si π_1(A^0) = 0" on scan 280 recalls (M08).

### R13 — keep
**Scan 279 · claim without proof.** 0-faithfulness holds if and only if π_1(A^u) = 0 for every u, and the NB rewrites the condition as π_1((A^0)^u) = 0 because A^u and (A^0)^u have the same identity component. The NB is valid when π_1 is taken at the identity, since π_1 of a topological group at 1 depends only on its identity path component. The superscript u of the first A^u is written over another letter.

### R14 — correct (scope of the insertion)
**Scan 279 · claim without proof.** 1-faithfulness: α, β ∈ Transp_A(u,v) with the same image in Transp_{π_0}(u̲,v̲) lie in the same component. Reducing to u = v gives injectivity of π_0(A^u) → π_0 and the boxed condition π_0((A^0)^u) = 0; M06 checks these steps. Correction: only "le sous-groupe ouvert" is interlinear, and the formula (A^u) ∩ A^0 = (A^0)^u stands in the line. The cancelled first draft of the argument remains largely illegible.

### R15 — correct (reading secured)
**Scan 280 · claim without proof.** 2-faithfulness: if u̲, v̲ are conjugate (or equal), then u, v are already conjugate, so a lift of u̲, if it exists, is unique up to conjugacy. The margin strengthens this to "Transp(u,v) → Transp(u̲,v̲) surjectif", equivalently "si u̲ = v̲, alors u et v sont conjugués par un élément de A^0". The reading is secure apart from the opening words; there is no "est" before "surjectif". M07 proves the stated equivalence, and M09 interprets the interlinear "(par un él^t de π̲_0)".

### R16 — keep
**Scan 280 · claim without proof.** Summary: if π_1(A^0) = 0, then 3-faithfulness holds if and only if every u̲ : Γ → π_0 = A/A^0 lifts to u : Γ → A, uniquely up to conjugacy, and (A^0)^u is then connected and simply connected. The inserted hypothesis belongs to the summary's scope. The sentence ends with a comma at the bottom of scan 280, so its continuation lies outside this package.

### R17 — keep
**Scans 278–280 · own idea (first pass).** Discrete A: A^0 = 1, π_0 = A, π_1 = 0. Every u̲ lifts uniquely and (A^0)^u = 1, so the criterion predicts a 2-equivalence, as it should. This is only a check of the indexing.

### R18 — keep, with a remark
**Scans 279–280 · own idea (first pass).** Take A = (R,+), Γ = Z and u_t(n) = nt. Then (A^0)^u = R is connected and simply connected, all u_t have the same image in π_0 = 1, and the u_t are pairwise non-conjugate. So 0- and 1-faithfulness hold and 2-faithfulness fails, in agreement with the written criterion. The example lies outside the intended case, where Γ is finite ("fini s'il le faut", scan 271) and A = A_{g,ν}.

### R19 — keep
**Scan 279 · own idea (first pass).** The ink confirms "le sous-groupe ouvert". For A = (Z/2)^N with the product topology, A^0 = {1} is not open, so openness of (A^u) ∩ A^0 in A^u needs a local hypothesis on A (local connectedness), which the page does not state. For the intended A_{g,ν} it should follow from the local contractibility of homeomorphism groups of compact manifolds (Černavskiĭ; Edwards–Kirby); the punctured case still has to be checked. As M06 shows, the connectedness criterion itself does not need openness.

### R20 — keep
**Scans 277–278 · own idea (first pass).** Compare a coherent action of Γ on an A̲-torsor, given by a morphism of Gr-categories Γ → A̲ with its coherence data, with the strict actions that come from homomorphisms Γ → A. This is the gap that "à définir ad-hoc" leaves open. The pages give no coherence equations and no obstruction classes.

## Second-pass notes (mine)

### M01 — conjecture (Grothendieck's), continued from scan 270
**Scan 271 · conjecture.** The package opens inside the conjecture of the preceding scan: the 2-functor from Γ-actions on surfaces (groupoids Π_f with finite fundamental groups) to the topossic/groupoid data is an "équivalence de 2-cat, i.e. qu'il est 3 fidèle". The 0-, 1-, 2- and 3-faithfulness analysis on scans 271–280 tests this conjecture, first for A_{g,ν} and then for an abstract topological group A.

### M02 — claim without proof
**Scan 272 · claim without proof.** "en fait on voit qu'elle est équivalente pour Γ, et pour son sous-groupe 1": the hypothesis on α, β (equality of the induced isomorphisms) is asserted to be the same with or without the Γ-action, with no argument. A proof would compare the natural transformations on the Γ-equivariant fundamental groupoids with their restrictions to the ordinary ones.

### M03 — claim without proof (literature to check)
**Scan 272 · claim without proof.** "Dans le cas π_1(A) = 0 (cas (g,ν) anabélien)": the vanishing of π_1 of the homeomorphism group A_{g,ν} in the anabelian case is used without proof. It agrees with the classical results on homeomorphism groups of hyperbolic surfaces (identity component contractible; Hamstrom). These should be cited for the punctured case that is actually used here.

### M04 — implication not pursued (own idea)
**Scans 271 and 274 · own idea.** The exclusion (g,ν) ≠ (0,0) on scan 271 fits the hypothesis π_i(A) = 0 for i ≥ 2 on scan 274. Homeo(S²) has the homotopy type of O(3) (Kneser), and π_3(O(3)) ≠ 0. For the other types, to my knowledge, the identity component is contractible or of the homotopy type of a circle or a torus. The pages do not say whether this is the reason for the exclusion, and the classical results should be checked before this is used.

### M05 — claim without proof, checked
**Scan 275 · claim without proof.** "Ces objets forment une 2-catégorie, dont les composantes connexes correspondent aux classes de conjugaison d'homomorphismes de Γ dans A". This holds because every A-torsor over a point is trivial, and an action of Γ on 1_A that commutes with the A-action is left multiplication through a homomorphism u. Morphisms (1_A,u) → (1_A,v) are then the elements of Transp(u,v). Continuity of u is part of the data and is not discussed.

### M06 — own check of the 1-faithfulness reduction
**Scan 279 · own idea.** If α ∈ Transp_A(u,v), left multiplication by α^{-1} maps Transp_A(u,v) homeomorphically onto A^u, compatibly with the maps to the π_0-transporters, so the case (u,v) reduces to (u,u) ("OPS u = v"). Each component of A^u lies in A^0 or misses it, so A^u ∩ A^0 is a union of components of A^u. The kernel of π_0(A^u) → π_0(A) is therefore trivial if and only if A^u ∩ A^0 = (A^0)^u is connected, which needs no openness. If π_0 means path components, as in the isotopic categories, the same argument runs with path components, and "connexe" should be read as path-connected.

### M07 — own check of the marginal equivalence
**Scan 280 · own idea.** The margin's equivalence holds when both statements are taken for all pairs (u,v). If every Transp(u,v) → Transp(u̲,v̲) is surjective and u̲ = v̲, a lift of 1 is an element of A^0 conjugating u to v. Conversely, given c ∈ Transp(u̲,v̲), pick a ∈ A over c: int(a).u and v have the same image in π_0, so v = int(g).int(a).u for some g ∈ A^0, and g·a lies over c.

### M08 — own check of the inserted hypothesis
**Scan 280 · own idea.** The inserted "si π_1(A^0) = 0" restates the standing assumption π_1 = 0 of scan 278, since π_1(A) at the identity equals π_1(A^0). The insertion thus marks the summary as proved only in the simplified case. According to the witnesses, the next scan turns to the general case.

### M09 — question on the interlinear "(par un él^t de π̲_0)"
**Scan 280 · question.** In "u,v sont déjà conjugués (par un él^t de π̲_0)", u and v take values in A, so they cannot be conjugated by an element of π_0. The addition presumably refers to the given conjugator of u̲, v̲ in π_0, which should lift to a conjugator of u, v. That is exactly the stronger formulation the margin then writes as surjectivity of Transp(u,v) → Transp(u̲,v̲). This is my interpretation; the page does not spell it out.

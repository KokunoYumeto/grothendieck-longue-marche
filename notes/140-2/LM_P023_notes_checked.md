# LM_P023 (scans 221–230): research notes checked against the corrected text

Each note gives its scan, kind and the decision taken. R01–R27 are the first pass's notes; M01–M09 are mine. "Own idea" marks a model's idea, not Grothendieck's.

## First-pass notes

**R01, scan 221, claim without proof: KEEP, corrected.** The canonical map from the surface-group extension to 1 → Π → Aut(Π) → Autext(Π) → 1 is justified only by "comme pour tte structure d'extension par un noyau de centre trivial". The ink says "noyau", not "groupe". The diagram is numbered (44), not (43); the theorem cites it as "par (44)", and (43) is the extension on scan 220. Injectivity of Π → Aut(Π) (trivial centre) and commutativity of the diagram are not written out.

**R02, scan 221, claim without proof: KEEP, corrected.** The "Théorème bien connu" (Γ_{g,ν} ≅ Autext_lac(Π_{g,ν}) and, by (44), Γ'_{g,ν+1} ≅ Aut_lac(Π_{g,ν})) is stated for the "cas anabélien" without proof. The margin note can now be read. It claims that the statement also holds for the couple (1,0) "(cf plus bas)", and even for (0,2) "si on définit ad hoc la notion de groupe à lacets (0,2)". The Conclusion commune on scans 229–230 supplies that ad hoc definition.

**R03, scan 222, claim without proof: KEEP, corrected.** The Corollary asserts two equivalences of categories, X ↦ π₁(X) and (X,s) ↦ π₁(X,s), from isotopic categories. The margin defines the arrows as "les classes d'isotopie d'homéomorph."; the first pass's "classes … à isotopie" is not in the ink. Essential surjectivity (every exterior group with loop structure of type (g,ν) comes from a surface) is not addressed.

**R04, scan 222, claim without proof: KEEP.** "Rappelons" recalls (45) Γ'_{g,ν+1} ≅ Γ_{g,ν} for 2g+ν ≤ 2. The source is the note on scan 220: the homomorphism is an isomorphism in the abelian cases. No proof is given on these pages.

**R05, scan 223, claim without proof: KEEP, corrected.** The torus statement, that a homeomorphism inducing the identity on π₁ is isotopic to the identity, is called "un résultat vrai (et connu)" and not proved. The struck "sur … pt marqué … a_{1,0}" shows a first formulation relative to the marked point. The surviving "le" leaves the corrected sentence ungrammatical, but the intended hypothesis is "induit l'identité sur π₁".

**R06, scan 223, claim without proof: KEEP, corrected.** (48) H × A_{g,ν+1} → A_{g,ν}, (g,u) ↦ gu, "est un homéomorphisme". The ink has no prime on A_{g,ν+1}, which is the stabiliser of 1_H. A proof needs continuity of φ ↦ (φ(1_H), φ(1_H)⁻¹·φ) in the compact-open topology; this holds because translations of a topological group are homeomorphisms.

**R07, scans 223–224, own idea (first pass): KEEP, confirmed on the ink.** (49) reads π_i(A_{g,ν+1}) ≃ π_i(A_{g,ν}) × π_i(H), with ν+1 on the left. But (48) gives A_{g,ν} ≅ H × A_{g,ν+1}, hence π_i(A_{g,ν}) ≅ π_i(H) × π_i(A_{g,ν+1}). The indices in (49) are swapped, an authorial slip that both witnesses copy; the next paragraph uses the correct direction, A°_{g,ν} ≃ H × A°_{g,ν+1}.

**R08, scan 224, claim without proof: KEEP, corrected.** The sentence reads "comme A°_{g,ν} ≃ H × A°_{g,ν+1} avec A°_{g,ν+1} contractile, on retrouve que H → A°_{g,ν} est un homotopisme". The first pass's "nous avons" was a misreading. The decomposition is a premise, and the contractibility of A°_{g,ν+1} in the anabelian case is assumed, not proved.

**R09, scan 224, claim without proof: CORRECT.** The ink says "structure de groupe ℂ-algébrique unique" and "variété algébrique X", not "analytique". My check of scope: for (0,2) and (0,1) the algebraic group structure (𝔾_m, 𝔾_a) lives on X = U_{g,ν}, not on X̂ = ℙ¹; only for (1,0) is X̂ = X, so "sur X̂" (if that is the reading) fits only that case. The statement that the identity component of Aut(X) consists of the translations holds for (1,0) and (0,2) but fails for (0,1), where Aut(𝔸¹) = Aff(1,ℂ) is connected and larger. That is why the text restricts it to "les cas limites".

**R10, scans 225–226, own idea (first pass): CORRECT; it becomes a definite finding (see M04).** The first pass suspected that the action on π₁ differs from the permutation of the ends. That is right, and (51) does not "s'identifier" with (51 bis) on all of Γ_{g,2}. Take s: z ↦ z⁻¹ and c: z ↦ z̄. On π₁(ℂ*) = ℤ, s and c both act by −1, so the kernel of (51) is {1, z ↦ 1/z̄}. The kernel of (51 bis) is Γ^!_{0,2} = {1, c}. The text's own example z ↦ z̄, given as a nontrivial element of Γ^!, therefore acts nontrivially on Π.

**R11, scan 226, claim without proof: KEEP.** The margin says "Cet hom. est tjrs surjectif" for χ and renames its kernel Γ^+ ("et non plus Γ^0!"). A proof needs an orientation-reversing homeomorphism of each type preserving the set of punctures; a reflection of a symmetric model works (see M08).

**R12, scan 226, Grothendieck's question/proposal: CORRECT.** The margin note can now be read: "Ceci suggère que pour une description isotopique de la cat. des surfaces (X) de type (0,2), il faut utiliser le couple de π₁(X) (≃ℤ) et de son module d'orientation T; itou plus bas à propos des cas des types (0,1), mais alors π = 0 et il suffit de T." The "(0,0)" in the first pass is not in the ink. The proposal is carried out in the Conclusion commune (scans 229–230).

**R13, scan 226, claim without proof: KEEP.** "Thm (bien connu!) Γ^{!+}_{0,2} = 1" is asserted without proof. It is equivalent to Γ^+_{0,2} ≅ 𝔖₂ via ρ^+ and to Γ^!_{0,2} ≅ {±1} via χ^!, which agrees with the computation in M04. The punctures must be kept as punctures, not as boundary circles fixed pointwise.

**R14, scans 226–227, implication not pursued: KEEP, sharpened by M05.** The bracketed "énoncé commun" (Γ^+ → Aut(Π) injective, with image the automorphisms of determinant 1) holds for (1,0), where Γ^+_{1,0} ≅ SL(2,ℤ). It fails as written for (0,2); see M05.

**R15, scan 227, claim without proof: KEEP.** Corollary (56): Γ^+_{0,3} ≅ 𝔖₃ via ρ^+_{0,3}, and Γ_{0,3} ≅ 𝔖₃ × {±1}. It is derived only through "modulo les isomorphismes Γ'_{g,3} ≃ Γ_{g,2}" and (55). The first subscript of Γ^+ remains doubtful (g|0).

**R16, scan 227, deleted claim: KEEP, corrected.** The paragraph struck with large crosses calls Γ_{0,3} an extension of {±1} (braces in the ink, not parentheses) by Γ^+_{0,3}, says it is split, and adds "Il en est ainsi de Γ_{g,ν} →χ {±1} quel que soit (g,ν)". This is a cancelled line of thought, not a retained theorem. The cancelled general claim is nevertheless true (M08).

**R17, scan 227, claim without proof: CORRECT.** The margin reads "cela redonne(?) bien que l'inclusion de G = Aff(1,ℂ) = Aut_ℂ(X)⁰ dans A_{g,1} est un homotopisme"; the first pass's "montre" is doubtful. As written the claim is too strong: (58) gives Γ_{0,1} ≅ {±1}, so A_{0,1} has two components, while Aff(1,ℂ) is connected (see R20).

**R18, scan 228, claim without proof: KEEP.** (58), Γ_{0,1} ≅ {±1} "par la signature", is stated as a corollary of Γ_{g,1} ≃ Γ'_{g,2} = Γ^!_{g,?} together with (55). See M07 on the doubtful subscript.

**R19, scans 228–229, claim without proof: CORRECT.** In both places "équivalence" is struck, so the claim is that (59) G ↪ A₀ "est un(e) … homotopisme". The argument uses simple transitivity on ordered triples, the homeomorphism (60) and the contractibility of A°_{0,3}. As in R20, it can hold only onto the identity component, because (61) gives Γ₀ ≅ {±1} while G ≅ GP(1,ℂ) is connected.

**R20, scans 227–229, own idea (first pass): KEEP, as a definite finding.** The inclusions Aff(1,ℂ) → A_{0,1} (margin of 227) and GP(1,ℂ) → A₀ (59) cannot be homotopy equivalences onto the whole groups, because π₀ is {±1} by (58) and (61) while the complex groups are connected. Read correctly, they are equivalences onto the identity components, as (50) states explicitly for A°_{g,2}.

**R21, scan 229, own idea (first pass): KEEP, sharpened.** The digit after "rg" looks like Grothendieck's 1. But type (1,0) has Π ≅ ℤ², and the same paragraph uses Λ²_ℤ Π, which is 0 in rank 1, and "c'est aussi son déterminant". Rank 2 is required, so this is probably an authorial slip; the witnesses print 2. The transcription keeps \unsure{1|2}.

**R22, scan 229, implication not pursued: KEEP, completed.** For type (0,2), automorphisms are "n'importe quel couple (u_Π, u_T)". With M04, g ↦ (action on π₁, χ) is an isomorphism Γ_{0,2} → Aut(Π) × Aut(T) = {±1}². This confirms the definition and explains why the action on Π alone, as in (51), does not suffice.

**R23, scan 230, implication not pursued: KEEP, corrected.** For types (0,1) and (0,0) the structure is the orientation module T alone. The margin requires the type in addition, "(sous-entendu g=0) le ν ∈ {0,1}"; the first pass's "le genre étant" is not in the ink. So Aut = Aut(T) = {±1} must be matched with (58) and (61).

**R24, scan 230, claim without proof: KEEP.** The Théorème (equivalence for every (g,ν) ∈ ℕ×ℕ, with arrows the isomorphism classes on both sides) is stated without proof. The proof would assemble the anabelian case (221–222) with the case-by-case computations (46)–(61).

**R25, scan 230, Grothendieck's reservation: KEEP, corrected.** The sentence breaks off at "récupérer" and continues on scan 231. The CSG witness gives the continuation, "l'extension de ce groupe par le dit π₁ !", which must be checked on that scan's ink. The reservation is explicit: "ce théorème n'est pas bien sûr pleinement satisfaisant".

**R26, scan 230, own idea (first pass): KEEP, low priority.** Testing the reservation with group actions through the translation group H is a reasonable example. According to the CSG witness, the author's own diagnosis follows on scan 231: the isotopic category neglects the homotopy type of the components of Homeo(X, X').

**R27, scan 230, own idea (first pass): DROP as an independent idea.** The proposed enrichment, keeping the topology of the homeomorphism groups, is what the author proposes on the next page according to the CSG witness: components seen as torsors under A°_{g,ν}, and an "∞-fidèle" description. It should be recorded as the author's line of thought when scan 231 is checked.

## My notes

**M01, scan 221, own idea (mine): check of a reference.** As read, "La structure d'extension (41) est déduite de (41) par image inverse par l'inclusion Γ^! → Γ" is circular. Pulling back along Γ^!_{g,ν} → Γ_{g,ν} must start from the extension of Γ_{g,ν}, which is (43), and both witnesses print (43). If the ink is (41), it is an authorial slip. The transcription marks \unsure{(41)|(43)}.

**M02, scan 222, claim without proof (Grothendieck).** The margin says "C'est même une équivalence au niveau des catégories ∞-isotopiques ce qui exprime seulement le fait que A°_{g,ν} et A°_{g,ν+1} sont contractiles". It asserts a homotopy-coherent strengthening of the Corollary. Its only input, the contractibility of the identity components in the anabelian range, is assumed, not proved.

**M03, scan 222, claim without proof (Grothendieck).** "(condition vide si ν = 0, d'ailleurs…)": for ν = 0 the loop structure imposes nothing, so the theorem gives Γ_{g,0} ≅ Autext(Π_g), all outer automorphisms, orientation-reversing ones included. This is the classical Dehn–Nielsen–Baer statement, used here without proof.

**M04, scans 225–226, own idea (mine): (51) and (51 bis) are different characters.** Γ_{0,2} ≅ {±1}² is generated by s: z ↦ z⁻¹ (swaps the ends, holomorphic) and c: z ↦ z̄ (fixes the ends, reverses orientation). Action on π₁(ℂ*) = ℤ: s ↦ −1, c ↦ −1. Permutation ρ of the ends: s ↦ −1, c ↦ +1. Orientation χ: s ↦ +1, c ↦ −1. So the π₁-action equals ρ·χ, and ker(51) = {1, z ↦ 1/z̄} ≠ Γ^!_{0,2} = ker(51 bis). The identification "(51) s'identifie à (51 bis)" holds only on Γ^+_{0,2}.

**M05, scans 226–227, own idea (mine): the "énoncé commun" fails for (0,2).** Γ^+_{0,2} = {1, z ↦ 1/z} maps isomorphically onto Aut(Π) = GL(1,ℤ) = {±1}, and its nontrivial element acts by −1, which has determinant −1. So "a comme image le groupe des autom. … qui sont de dét. 1" is false for rank 1. It would hold for Γ^{!+}_{0,2}, which is trivial by (55). The Conclusion on scan 229 treats (0,2) correctly, with T as extra data.

**M06, scan 226, own idea (mine): sign of the example.** If the ink really gives "(−1,−1)" as the image of z ↦ z⁻¹ under (ρ, χ), it is impossible: z ↦ z⁻¹ is holomorphic (χ = +1) and swaps the ends (ρ = −1), so the image is (−1, 1). The second example, z ↦ z̄ ↦ (1, −1), is consistent with ρ being the permutation character of (51 bis), not the π₁-action of (51), under which z̄ ↦ −1.

**M07, scan 228, own idea (mine): subscript in "On a ici".** In Γ_{g,1} ≃ Γ'_{g,2} = Γ^!_{g,?}: with two punctures, the stabiliser of one fixes the other, so Γ'_{g,2} = Γ^!_{g,2}. Only the subscript 2 is correct. The ink is doubtful (1|2), and the witnesses print Γ^!_{g,1}.

**M08, scan 227, own idea (mine): the cancelled splitting claim is true.** "Il en est ainsi de Γ_{g,ν} →χ {±1} quel que soit (g,ν)": embed the surface symmetrically in ℝ³ with the punctures on the mirror plane. The reflection is an orientation-reversing involution preserving the punctures, and its class splits χ. Grothendieck struck the paragraph, but the general claim in its NB stands.

**M09, scan 226, own idea (mine): "ρ et ρ".** The ink appears to read "mettant ensemble ρ et ρ". The homomorphism (54) that follows is g ↦ (ρ(g), χ(g)), so the second letter must mean χ. The transcription keeps \unsure{\rho|\chi}.

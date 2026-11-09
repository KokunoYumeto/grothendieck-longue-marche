# LM_P054 (scans 531–540): research notes, checked against the corrected transcription

The first pass's notes are `answers/unzipped/LM_P054/LM_P054_notes.md`, § 5. Each is checked here against `second_pass/LM_P054_checked.tex` and kept, corrected or dropped, with the reason. Section C adds the second-pass checker's own notes, labelled as such. Kinds: *question/programme* (Grothendieck's), *expectation* (Grothendieck's unproved belief), *claim without proof*, *implication not pursued*, *model's idea* (the first pass's), *checker's note* (mine).

## A. First-pass notes (§ 5.1)

**A1. Scan 531. Question/programme. Keep.** "Il est temps … de s'assurer qu'il en est bien ainsi": the homomorphism Π̂₀,₃ → T̂^{+′}₁,₁ just used should agree with Π̂₀,₃ → Π̂′₀,₃ of (10)–(20) through an isomorphism "qui reste à décrire", commuting with the exterior Γ-actions. *Reason:* the reading is confirmed. The target is a single T̂^{+′}₁,₁; the first pass had written the group twice (change 5).

**A2. Scan 532. Grothendieck's own diagnosis. Keep.** The "natural" homomorphism Π₀,₃ → T^{+′}₁,₁, obtained by factoring through Π₀,₃ →(can., surj) Π′₀,₃, "n'était pas du tout celui qu'on avait en vue". He gives up that route ("revenir à la charge"), and § 37 restarts from equivariant coverings. *Reason:* the text is confirmed.

**A3. Scan 533. Expectation (was: claim). Corrected.** The ink reads "en fait les deux doivent être équivalents". Grothendieck *expects* local faithfulness (each G_x faithful near x) and global faithfulness of G to coincide; he does not assert it. "Donc G_x est un groupe cyclique" and "Y = X/G est une surface top. paracompacte" remain claims without proof. *Reason:* the first pass's "les deux notions sont équivalentes" misread the ink (change 18). Note C1 says when the expectation holds.

**A4. Scan 533. Claim without proof. Keep.** The fixed-point set X^! = {x | G_x ≠ (1)} and its image Y^! are called discrete, and the ramification index is d_y = ord G_x. This needs local quotient charts of the form z ↦ z^d.

**A5. Scan 533, margin. Claim without proof. Corrected.** The Variante reads as follows. 𝒢 acts on X with a normal ("invariant") subgroup G satisfying the conditions "ci-contre". Setting Y = X/G "avec opér. de 𝒢/G = ℋ dessus", one gets Rev.(X,𝒢) ≊ Rev((Y,d),ℋ), hence Π₁(X,𝒢,x) ⥲ Π₁((Y,d,ℋ),y). A proof must check that ℋ preserves the signature d and define the covering category of (Y,d) with its ℋ-action. *Reason:* the first pass lost "opér. de", the action of ℋ on Y on which the statement rests (changes 27–30).

**A6. Scan 533, margin. Claim without proof. Corrected.** "Application: 𝔖₀,₃ ≃ T′₁,₁ (≃ Gl(2,Z)/±1), ext de T₀,₃ = 𝔖₃ × Z/2 par Π₀₃." This is the Variante with 𝒢 = T₀,₃ acting on U₀,₃(ℂ); the factor Z/2 is presumably complex conjugation. *Reason:* the group letter is the ornate S, not 𝒢 (change 34). Gl versus Sl stays open in the ink, but only Gl fits the stated extension (C2).

**A7. Scans 531–533. Model's idea. Keep.** Compare the failed and the intended homomorphisms through their actions on covering categories, with explicit path data. *Reason:* still a sensible check. § 37 itself takes this route through Rev(X,G).

**A8. Scan 534, (1). Claim without proof. Keep.** X′ ↦ X′/G gives an equivalence Rev(X,G) ⥲ Rev_d(Y) with ramified covers subordinate to d.

**A9. Scan 534, NB. Claim without proof. Keep.** The quasi-inverse is the "normalised" (X,G)-cover of X ×_Y Y′. The analogue for "schémas loc. noeth. réguliers de dim 1" is obtained by normalisation.

**A10. Scan 534, (2). Claim without proof. Keep.** A canonical isomorphism Π₁(X,G;·) ⥲ Π₁((Y,d),y). The basepoint letter in (2) is still a/x.

**A11. Scan 535, (3). Claim without proof. Keep.** The exact sequence 1 → Π₁(X,x) → Π₁((Y,d),y) → G → 1 for connected X. Grothendieck circles the term "Π₁((X,G→1),x)" and writes "Π₁(X,x)" in the margin, which confirms the kernel is the ordinary fundamental group.

**A12. Scan 535, NB. Expectation. Keep.** "On a ? un corollaire analogue" for regular 1-dimensional schemes. For smooth relative curves over S "il faudrait (si j'en ai besoin) faire un peu attention de préciser l'énoncé".

**A13. Scan 535, (4). Claim without proof. Keep, now checked.** The three orbits, their images 0, 1, ∞ and the indices 2, 2, 3 are correct; see A14, C3 and C4.

**A14. Scan 535. Model's idea. Corrected (carried out).** The invariant the first pass proposed to construct is f(λ) = 27λ²(λ−1)² / 4(λ²−λ+1)³ = 1728/j(λ). It sends {0,1,∞} to 0 with index 2, {2,−1,½} to 1 with index 2, by 4(λ²−λ+1)³ − 27λ²(λ−1)² = (λ+1)²(λ−2)²(2λ−1)², and the roots of λ²−λ+1 to ∞ with index 3. *Reason:* checked by the second pass.

**A15. Scan 536. Claim without proof. Keep.** One cannot take x = P = j, which is an orbifold point. One takes x outside the eight special points, with y = f(x) the "pt-base typique Q = j".

**A16. Scan 536. Claim without proof. Corrected.** A 𝔖₃-class of paths from the "point-base *initial*" P = j to x gives an "iso. *corr.*" (corresponding, not canonical) of the first member of (5bis) with Π₀,₃. Hence (6), which changes by an inner automorphism when the class of paths changes. *Reason:* the first pass read "orbital" and "iso. can." (changes 48–49). The ink separates the path-dependent "iso. corr." from the "iso. can." (6), which is canonical up to inner automorphisms.

**A17. Scan 536. Implication not pursued. Keep.** (7) is said to be (9bis) of § 36, now read as the homotopy exact sequence of 𝔖₃ acting on U₀,₃(ℂ). The comparison with § 36 is not carried out.

**A18. Scan 536. Model's idea. Keep.** Track the inner-automorphism ambiguity of (6) with explicit loops around the branch values.

**A19. Scan 537, (8). Claim without proof. Corrected.** The paired strokes beside the diagram are equality signs: Π̂₀,₃ = T̂⁺₀,₄, ℰ₀,₃ = N^!₀,₄ (the letter N is uncertain) and Γ₀,₄ = Γ_Q. The first two identify the geometric and arithmetic fundamental groups of U₀,₃ = M^!₀,₄ with Teichmüller-type groups of type (0,4). The equality Γ₀,₄ = Γ_Q amounts to the faithfulness of the outer Galois action on Π̂₀,₃, which is Belyi's theorem. *Reason:* the first pass only described "deux courts traits"; CSG/CK read "=" (change 53).

**A20. Scan 537. Implication not pursued. Keep.** "Mettre en relation U₀,₃, avec l'action de 𝔖₃ dessus, avec la multiplicité modulaire M₁₁" (indices Q understood) is the programme of § 37, carried out on scans 538–540 and beyond.

**A21. Scan 537. Model's idea. Corrected.** The base is Z[1/2], "i.e. en car. rés. ≠ 2" (the reading rés./tj. is still open). The first pass's suggestion to look at residue characteristic 3 separately is right, for a precise reason given in C5.

**A22. Scan 538. Claim without proof. Corrected.** Grothendieck calls his earlier identification U₀,₃ = M^!₀,₄ ≃ M₁,₁[2]′ "un peu vaseusement" (muddled). He corrects it to "(sur lequel M₁,₁[2] est une gerbe liée par Z/2)": M₁,₁[2] is a Z/2-gerbe over M₁,₁[2]′. *Reason:* the first pass read "oiseusement" (change 57); the witnesses' "sous lequel" is wrong.

**A23. Scan 538. Claim without proof. Corrected.** For elliptic curves, the statement that an automorphism inducing the identity on ₙE is the identity for n ≥ 3 is Serre's rigidity lemma. For abelian varieties "de dim quelconque" it is false without a polarisation (C6).

**A24. Scan 538. Claim without proof. Keep.** For n = 2, an automorphism trivial on ₂E is id_E over an open and closed part of S and −id_E on the complement. This holds over Z[1/2], where the only automorphisms acting trivially on E[2] are ±1.

**A25. Scan 538. Implication not pursued. Corrected.** "Coiffer M₁,₁[2] par un M₁,₁(n), où n est un multiple de 2": for M₁,₁(n) to be a scheme, the margin of scan 539 requires n ≥ 3, so n must be even and at least 4. Its image in Spec Z is the open set Spec Z[1/n]. *Reason:* the ink reads M₁,₁(n), and the "2n" alternative is dropped (change 60).

**A26. Scan 538. Model's idea. Keep.** Follow the residual sign automorphism through the presentation by M₁,₁(n) and its descent to level 2.

**A27. Scan 539, (9). Claim without proof. Keep.** Over Spec Z[1/n], M₁,₁ "se récupère comme" the pair (M₁,₁[n], Gl(2,Z/nZ)). The margin insists on Gl and not Sl.

**A28. Scan 539, second margin. Claim without proof. Keep.** The functor of full level-n structures is "représentable ssi n ≥ 3 (donc il ne l'est pas pour n = 1, 2)".

**A29. Scan 539, NB. Claim without proof. Keep.** M̃₁,₁ over Spec Z is "l'enveloppe représentable" of the functor of isomorphism classes, "itou sur un schém. de base … quelconque". In modern terms this is the coarse moduli space; see C7.

**A30. Scans 539–540. Implication not pursued. Keep.** Gl rather than Sl is needed because the determinant of the level structure gives the morphism to μₙ^*, along which M₁,₁[n] splits into geometric components.

**A31. Scan 539. Model's idea. Keep.** Before (10) the ink says "au dessus de Z/nZ", and after it "Z[1/n]"; all three witnesses also have Z/nZ. It is probably a slip of the pen for Z[1/n].

**A32. Scan 540. Model's idea. Corrected.** The Weil pairing identifies Λ²(ₙE) with μₙ, not μₙ^{⊗−1}. Either convention gives the next line, because an isomorphism Z/nZ ≅ μₙ^{⊗−1}(S) is the same thing as one Z/nZ ≅ μₙ(S), up to inversion. The ⊗−1 is a duality convention or a slip, and the argument does not depend on it.

**A33. Scan 540. Claim without proof. Corrected.** "Et c'est *ce* morphisme qui est à fibres géom. connexes *en car. 0*": the doubly underlined insertion is confirmed, and the subject is (11) itself (change 75). The fibres of M₁,₁[n] → μₙ^* are known to be geometrically connected in every characteristic prime to n (Igusa; Deligne–Rapoport). Grothendieck's restriction is therefore more cautious than necessary.

**A34. Scan 540, (12). Claim without proof. Keep.** Passing to the limit gives M₁,₁[∞] = lim M₁,₁[n] → μ_∞^* ≃ Spec Σ, marked "iso. can". Σ is defined in the lines that follow (scan 541 in the witnesses: the maximal cyclotomic extension).

**A35. Scans 539–540. Model's idea. Keep.** Track the change-of-basis action of Gl(2,Z/nZ) through the exterior square, level by level, and ask whether it is compatible with the limit.

## B. First-pass literature comparisons (§ 5.2)

**B1. Scans 533–537. Model's idea (Noohi, covering stacks). Keep.** It is relevant to the Variante (A5) and to (2)–(3).

**B2. Scans 539–540. Model's idea (Hain, level structures). Keep.**

**B3. Scans 535, 537–539. Model's idea (Deligne–Rapoport). Keep.** It is also the reference for A24, A33 and C7.

## C. Checker's notes (second pass)

**C1. Scan 533. Checker's note on Grothendieck's expectation "les deux doivent être équivalents".** Local faithfulness implies global faithfulness at once. Conversely, suppose 1 ≠ g ∈ G_x acts trivially near x. Then g has finite order, and by Newman's theorem a non-trivial periodic homeomorphism of a connected manifold cannot fix a non-empty open set pointwise. So the two conditions are equivalent for connected X. For disconnected X they differ: take Z/2 acting by an involution on one component and trivially on another.

**C2. Scan 533, margin. Checker's note supporting the reading Gl.** The map GL(2,Z) → GL(2,F₂) × {±1}, g ↦ (g mod 2, det g), is surjective with kernel Γ(2), which contains −1. So PGL(2,Z) = GL(2,Z)/±1 is an extension of 𝔖₃ × Z/2 by Γ(2)/±1, a free group of rank 2 (= Π₀,₃), exactly as the margin says. With Sl one gets PSL(2,Z), an extension of 𝔖₃ alone.

**C3. Scans 535–536. Checker's note on notation.** The fixed points of the order-3 elements of the anharmonic group (λ ↦ 1/(1−λ)) are the roots of λ²−λ+1, that is e^{±iπ/3}. With the usual French j = e^{2iπ/3} these are −j² and −j. So "(j, j̄) ↦ ∞" in (4), and P = j on scan 536, need j to name a primitive sixth root of unity, or the conventions of § 36. The same letter also names the base point Q = j of Y. Check § 36 before relying on these names.

**C4. Scans 535–536. Checker's note: claim confirmed.** Y = ℙ¹ ∖ {0} with signature 2{1}+3{∞} has orbifold fundamental group ⟨a, b | a² = b³ = 1⟩ ≅ Z/2 ∗ Z/3 ≅ PSL(2,Z). So (5bis)–(7) identify Π′₀,₃ with PSL(2,Z) and Π₀,₃ with its free normal subgroup Γ(2)/±1 of index 6. This agrees with T⁺₁,₁ = SL(2,Z) in § 36.

**C5. Scan 537. Checker's note: an implication not pursued.** Over Z[1/2], the tame description of U₀,₃/𝔖₃ breaks down at residue characteristic 3. Modulo 3, λ²−λ+1 = (λ+1)² and −1 = 2 = ½, so the single point λ = 2 is fixed by all of 𝔖₃: its stabiliser has order 6, divisible by 3, so the ramification is wild. The signature 2{1}+3{∞} holds over Z[1/6], not Z[1/2]. Diagram (8), over Q, is unaffected.

**C6. Scan 538. Checker's note: the claim needs a hypothesis.** On A = E × E the automorphism (P, Q) ↦ (P + nQ, Q) is the identity on A[n] for every n, yet it is not the identity. So the rigidity statement for abelian varieties "de dim quelconque" needs a polarisation, which makes the automorphism group finite; Serre's lemma then gives it for n ≥ 3. For elliptic curves no hypothesis is needed.

**C7. Scan 539. Checker's note (literature).** M̃₁,₁ is the affine j-line A¹ over Z (Deligne–Rapoport; Katz–Mazur). "L'enveloppe représentable" is the universal map from the stack to schemes, that is, the coarse moduli space (Keel–Mori). Over Z[1/n] this agrees with the quotient (10).

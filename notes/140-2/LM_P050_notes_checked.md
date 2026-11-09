# LM_P050 (scans 491–500): research notes checked against the corrected transcription

Package LM_P050 covers manuscript pp. 249–253 (archive pages 490–499) and the text in `LM_P050_checked.tex`. The 33 first-pass notes keep their numbers. Each note gives the scan, the kind, a verdict (keep, correct or drop) and a reason. Notes A–E are mine (second pass). Literature named in a note is a lead to check unless the note says it was read.

## First-pass notes

**1. Scan 491, margin · claim without proof (declared dependency) · keep.** The margin, now read without doubt as "démontré modulo le lemme 2 plus bas —", makes Théorème 1 conditional on Lemme 2. Lemme 1 uses both parts of Lemme 2. Part a), the trivial centre, turns int(g)^m = id into g^m = 1, and part b), torsion-freeness, then gives g = 1. Grothendieck admits he is stuck on part a) ("je cale sur a)", scan 496). *Reason:* the reading is settled and the dependency stands. The precise use of a) and b) has been added.

**2. Scan 491, Lemme 1 · claim without proof · keep.** "Il suffit de voir que l'opération extérieure de K sur π₁(V̄), où V = U₀,₃ ∖ {x}, est triviale" reduces the effective action based at x to the outer action on the punctured curve. The way back is "Repassant à π₁(V̄) … l'image de K dans Aut Π̂₀₃ est finie" on scan 493, which goes through the loop subgroup at the new cusp x and is not spelled out. *Reason:* the text is confirmed.

**3. Scan 491, Белый · claim without proof · correct.** The Белый map must be "défini sur Q" and send x ↦ 0. The step "π(V̄) est un quotient de π′" also needs U′ = f⁻¹(U₀,₃) ⊂ V, that is, f({0, 1, ∞, x}) ⊂ {0, 1, ∞}. The text leaves this condition implicit; Belyi's construction for the finite set {0, 1, ∞, x} provides it. *Reason:* the first-pass note did not name the implicit condition.

**4. Scan 492, normaliser paragraph · implication not pursued · correct.** The bracket ends "or N/π′ est fini" (first pass: "où"). The ink has N/π′ → Autext(π′) where the witnesses print N/Z, and "groupe extension" where they print "groupe extérieur". The argument runs as follows. E_K acts on π through π/Z, because K = Ker Θ acts by inner automorphisms. E′_K lands in N/Z. Hence the image of K in Autext(π′) lies in the image of the finite group N/π′. *Reason:* the reading is corrected. The extension lemma behind the step is elementary once K acts by inner automorphisms.

**5. Scan 493, Lemme 2 · claim without proof · keep.** Lemme 2 (trivial centre and no torsion in Π̂₀,₃) is deferred: "que je reporte pour plus tard". Part b) is proved on scans 496–497 by the Artin argument. Part a) stays open in this package. *Reason:* confirmed.

**6. Scan 494 · claim without proof · keep.** "mais cela n'est pas suffisant pour notre propos": finiteness of the outer action of K does not by itself give triviality. The rational point y ∈ V(ℚ) and the effective action it allows are the extra input. *Reason:* confirmed.

**7. Scan 494 · implication not pursued · keep.** Replacing U "par n'importe quelle courbe algébrique qu.proj. lisse géométriquement connexe" keeps the finiteness stage. Grothendieck pursues this in Corollaire 1 (scans 497–499). There a closed point over a finite extension replaces the rational point, and the finite kernel that remains is removed by Artin–Schreier. *Reason:* confirmed, with a cross-reference added.

**8. Scan 494 · model's idea (first pass) · drop.** The proposed comparison "with a version based on a closed point after finite scalar extension, keeping track of the residual finite kernel" is the proof of Corollaire 1 on scans 498–499. That proof takes y rational over k′, sets K′ = Γ′ ∩ K, concludes "Il en résulte que K est fini", and then uses Artin. *Reason:* the idea is not open; it is already in the text (see note 7).

**9. Scan 495, Lemme 4 · claim without proof · correct.** The action of K on I = S(ℚ̄₀) is said to be "déduite de l'action extérieure de K sur π₁(V̄)", through the conjugacy classes of "ss-groupes lacets". In both places K is written in bold over a lighter Γ; the three witnesses read Γ. No proof is given. A proof needs that distinct points of I have non-conjugate loop subgroups, and that these subgroups are Galois-equivariant. *Reason:* the subject letter is K in the ink. See note 11 for the case card I = 2.

**10. Scan 495 · implication not pursued · keep.** "Ceci étant vrai pour tt V" needs a cofinal family. The complements V = ℙ¹_ℚ ∖ S serve, where S is ∞ together with the zero set of a polynomial over ℚ; every algebraic number lies in such an S. *Reason:* confirmed, with the family made explicit.

**11. Scan 495 · model's idea (first pass) · correct (settled).** The proposed test at card I = 2 settles the question. In that case π₁(V̄) ≅ Ẑ(1), and the two loop subgroups coincide, so conjugacy classes of loop subgroups cannot separate the two points. The deduction needs card I ≥ 3, or oriented loops (generators) together with χ|_K = 1. The latter holds because K acts trivially on the abelianisation Ẑ(1)² of Π̂₀,₃. This does no harm to Lemme 4, since V may be shrunk. Confidence: high. *Reason:* the check has been carried out.

**12. Scan 496 · question (Grothendieck) · keep.** "Finalement je cale sur a)" leaves the trivial centre of a free profinite group of rank ≥ 2 unproved, with "Consulter Deligne à ce sujet !". The result is known; see notes 31 and C. *Reason:* confirmed.

**13. Scan 496 · question (Grothendieck) · keep.** He also does not see why "le centre de Γ (et de tt sous-groupe ouvert)" should be trivial; the abbreviation is now read as "tt". This is a separate question about absolute Galois groups (note C). *Reason:* the reading is settled.

**14. Scan 496 · claim without proof · correct.** The torsion argument uses "Comme π est libre" to obtain a continuous section of E_L → π, which holds because free profinite groups are projective. It also uses π ≅ π₁(U) with U = ℙ¹_K ∖ (n+1 points) and n = card I (the letter is n, not ν). *Reason:* the reading is corrected.

**15. Scan 496 · model's idea (first pass) · correct (settled).** With the corrected reading, the revised formula is U = ℙ¹_K ∖ (n+1 points), (n = card I). The n + 1 punctures give a free group of rank n = card I, matching "π libre sur I". *Reason:* the audit is complete and nothing in it remains open.

**16. Scan 497 · claim without proof (cited input) · keep.** "d'après Artin": a nontrivial automorphism τ of finite order of an algebraically closed field L̄ exists only when L̄ is a quadratic extension of an ordered maximal field R fixed by τ, so τ has order 2. This is the Artin–Schreier theorem, cited and not proved here. *Reason:* confirmed.

**17. Scan 497 · implication not pursued · keep.** The contradiction uses only that −1 is a square in K ⊂ L. The same argument makes Gal(L̄/L) torsion-free for any field L that cannot be ordered. That K is algebraically closed of characteristic 0 is needed earlier, to realise π as π₁(U) and as a quotient of E_L. *Reason:* confirmed.

**18. Scan 497 · conjecture · keep.** "Je présume que l'action extérieure de E_k^{k̄} sur π₁(X_{k̄}) est fidèle si U anabélien": the curve letter is X overwritten on U, while "si U anabélien" keeps U. Later literature is a lead to check, not used here: Matsumoto (1996) for affine hyperbolic curves, Hoshi–Mochizuki for proper ones. *Reason:* confirmed.

**19. Scan 497 · claim without proof · keep.** Corollaire 1 asserts only that some nonempty open V has a faithful outer action. Its proof (scans 498–499) rests on Lemme 5, which is admitted, and on the χ(τ) step (note A). *Reason:* confirmed.

**20. Scan 497 · model's idea (first pass) · correct.** The method transfers faithfulness upward, not downward. Corollaire 2 passes it from U to the étale covers V of U. The "présume" for X would need it on π₁(X̄), a quotient of π₁(V̄), and faithfulness on π₁(V̄) does not give that. Confidence: high. *Reason:* the first-pass idea was vague; it is replaced by the precise obstruction.

**21. Scan 498 · claim without proof · keep.** "D'après Белый, on sait qu'on peut trouver V ⊂ X, qui soit un revêtement étale de (U₀₃)_k": this needs a Belyi map X → ℙ¹ defined over k, with V the preimage of U₀,₃. V is geometrically connected because X is. *Reason:* confirmed (the text reads "qui soit", not "qui est").

**22. Scan 498, margin · claim without proof · correct.** The margin reads "prouvé seulement modulo vérification de (2),(4) ci-dessous — pour le corollaire (2) est d'ailleurs suffisant…". Grothendieck himself marks Lemme 5 as conditional on (2) (scan 500) and on (4), which lies beyond this package. *Reason:* the opening words are now read as "seulement", not "simplement".

**23. Scan 499 · claim without proof · keep.** "Admettons pour l'instant ce lemme": the conclusions K′ = (1) and K finite depend on Lemme 5. The faithfulness of Γ′ on π comes from Théorème 1 by restriction to the open subgroup Γ′ ⊂ Γ_ℚ. *Reason:* confirmed.

**24. Scan 499 · claim without proof · correct.** "par Artin on sait que les seuls sous-groupes finis ≠ (1) de Γ sont ceux engendrés par une conjugaison complexe τ". The ink revises the following phrase towards the singular, "correspondant à un sous-corps ordonné maximal". Then χ(τ) = −1 is said, without argument, to make the outer action of τ nontrivial. That step holds for hyperbolic curves and fails for ℙ¹_ℝ ∖ {±i} (note A). *Reason:* the reading is revised and the gap located.

**25. Scan 499 · model's idea (first pass) · keep.** Separating the finite-kernel step (Lemme 5 with Théorème 1) from the torsion step (Artin–Schreier with χ) shows which hypotheses each step uses. Corollaire 2 records that only these two steps were used. *Reason:* the suggestion is organisational and correct.

**26. Scans 499–500 · implication not pursued · correct.** Corollaire 2 is numbered in the ink; the witnesses print "Corollaire". It replaces "extension de type fini de ℚ" by "corps de car 0". The proof uses only a closed point of V, Lemme 5 for π₁(U_{k̄}), the hypothesis of faithfulness on U and Artin–Schreier. All of these are available over any field of characteristic 0, subject to the χ(τ) step (note A). *Reason:* the label is corrected and the scope made precise.

**27. Scan 500 · claim without proof · correct (settled).** "Il suffit de le prouver dans le cas respé — l'autre s'en déduit aussitôt". Suppose u induces int(g) on π′ with g ∈ π′. Then int(g)⁻¹ ∘ u is an automorphism of π that is the identity on π′, so the identity case gives u = int(g). *Reason:* the reduction is immediate and nothing in it remains unproved.

**28. Scan 500 · claim without proof · correct.** The revised passage reads "Si π a au moins une classe de lacets (cas d'une courbe alg. affine i.e. non propre), alors π est libre — et le lemme 5 est valable justement pour de tels groupes"; the first pass had "un disque de lacets". That π₁ of an affine curve in characteristic 0 is free is standard, by comparison with the topological fundamental group. "est valable" is then argued modulo (2). *Reason:* the reading is corrected.

**29. Scan 500 · claim without proof · keep.** Display (2), L_i = Centr_π(ℓ_i^n), is introduced by "nous admettrons" and marked "pas prouvé !". Whether the argument is ℓ_i^n or L_i^n, the centraliser is the same, because ℓ_i^n topologically generates L_i^n. See note E. *Reason:* confirmed; the letter ambiguity does not touch the mathematics.

**30. Scan 500 · model's idea (first pass) · correct.** The continuation on scan 501, as all three witnesses show, supplies the step from u(ℓ_i)ⁿ = ℓ_iⁿ to u(ℓ_i) = ℓ_i. By (2), u(ℓ_i) lies in L_i ≅ Ẑ, and since Ẑ is torsion-free, u(ℓ_i) = ℓ_i. *Reason:* the obligation is discharged in the text, modulo (2).

**31. Scans 493, 496 · literature (first pass) · keep.** Belyi's corollary c(F, F) = 1, for F the free profinite group on two generators, supplies Lemme 2 a). The page numbers were not rechecked in this pass.

**32. Scans 491, 498 · literature (first pass) · keep.** Belyi's construction for a finite set of algebraic points (his Theorem 4) gives the pointed and field-of-definition requirements of note 3. Not rechecked in this pass.

**33. Scans 497, 499 · literature (first pass) · keep.** Artin–Schreier (1927) is the source of the order-2 and real-closed statements used on scans 497 and 499. Not rechecked in this pass.

## Second-pass notes (mine)

**A. Scan 499 · claim without proof (gap located) · second pass.** The step "χ(τ) = −1, donc l'action extérieure de τ ne peut être triviale" fails for V = ℙ¹_ℝ ∖ {±i}. There π₁(V_ℂ) ≅ Ẑ(1), and complex conjugation sends the unit (z − i)/(z + i) to its inverse while also inverting μ_n, so it acts trivially. The step does hold for hyperbolic V. If τ acted trivially on H₁, then τ[ℓ_P] = −[ℓ_{τP}] would be impossible with two or more cusps, except for exactly two conjugate cusps. In that case, or with one cusp or none, the genus is at least 1, and τ acts on H² of the compactification by χ(τ)⁻¹ = −1. The V of Corollaire 1, étale over U₀,₃, is hyperbolic. Confidence: high.

**B. Scan 496 · model's idea · second pass.** Théorème 2 b) has a direct proof that also covers an infinite I. A free profinite group is projective, so it and all its closed subgroups have cohomological dimension ≤ 1. A nontrivial finite cyclic group has infinite cohomological dimension. This avoids Artin–Schreier and the realisation as π₁ (standard, e.g. Serre, *Cohomologie galoisienne* I §3–§4). Confidence: high.

**C. Scan 496 · literature lead · second pass.** For a): a free profinite group of rank ≥ 2 has trivial centre (Belyi's c(F, F) = 1, note 31; the general rank is standard, e.g. in Ribes–Zalesskii, *Profinite Groups*; locus to check). For Grothendieck's question on Γ and its open subgroups: absolute Galois groups of number fields have trivial centre (Neukirch–Schmidt–Wingberg, *Cohomology of Number Fields*, ch. XII; locus to check). Confidence: medium, from memory.

**D. Scan 496 · model's idea · second pass.** The inserted "fini" is needed only to realise π as π₁ of ℙ¹ minus finitely many points. For an infinite I, Grothendieck's own route still works through Douady's theorem: Gal(L̄/L) for L = K(x), with K algebraically closed of characteristic 0, is free of rank card K. Combined with projectivity and Artin–Schreier, this gives the result. Confidence: medium-high (lead: Douady 1964).

**E. Scan 500 · literature lead · second pass.** For a basis element ℓ of a free profinite group, (2) states that Centr(ℓⁿ) is the closed subgroup generated by ℓ. This follows from two facts: centralisers of nontrivial elements are procyclic, and ⟨ℓ⟩ is a free factor (Herfort–Ribes on centralisers in free profinite products; Ribes–Zalesskii; exact statements to check). So (2) is true in the free case that the manuscript treats first. Confidence: medium.

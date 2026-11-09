# LM_P053 (scans 521–530): research notes, checked against the corrected text

Source of the notes: `answers/unzipped/LM_P053/LM_P053_notes.md`, section 5 (numbered here R01–R44). Each is checked against `second_pass/LM_P053_checked.tex`. **Keep** means the note stands as written; **correct** gives the replacement; **drop** gives the reason. Notes S01–S10 at the end are the second pass's own, labelled as such. Matrix notation: A = [[1,2],[0,1]], B = [[1,0],[−2,1]], S = [[0,−1],[1,0]], T = [[1,1],[0,1]]; Γ(2) = Γ₂ = Ker(Sl(2,ℤ) → Sl(2,ℤ/2ℤ)).

## First-pass notes

**R01, scan 521, unproved claim. Correct.** The map is (22), not (27): "cet hom. (22) n'a rien d'injectif, par contre il est surjectif — et ses valeurs sont non dans Sl(2,ℤ)/±1, mais dans Sl(2,ℤ) lui-m̄!". (22) is Π₀₃ → Sl(2,ℤ) on scan 516 (LM_P052); (27) is the description of M₁₁ as a quotient stack. Non-injectivity is clear (Π₀₃ is free, Sl(2,ℤ) has torsion); surjectivity is asserted without proof.

**R02, scans 521–522, conjecture (stated programme). Correct.** The ink reads "une façon de donner un sens arithmético-géométrique remarquable à (22), et son extension aux groupes profinis correspondants" ("compatible à (27)" in the first pass). The programme is left open here; a later footnote to an earlier page (witness fn. 143) calls these pages "inutilement compliquées" and points to the Legendre curve, which appears on scan 527.

**R03, scan 522, unproved claim. Keep, with a reading note.** "analytique complexe" is now settled. Under T′⁺₁₁ in (34) the ink has Sl(2,ℤ/2ℤ)/±1, a slip for Sl(2,ℤ)/±1 (as in (35)); the witnesses correct it silently.

**R04, scan 522, conjecture. Keep.** The reading "Π̂′₀,₃ à T̂′⁺₁₁" is settled. The interpretation of (35) and (33) through diagram (9) (LM_P052) is deferred ("J'y reviendrai tantôt").

**R05, scans 522–523, conjecture. Keep.** The margin answer "Oui, on peut remonter, et c'est plus ou moins trivial… cf plus bas…" points ahead to the Legendre family of scan 527.

**R06, scan 523, unproved claim. Correct.** The parenthesis reads "(qui nécessairement, dans le cadre profini, respectent les réseaux discrets)": every profinite lift sends the discrete Π₀,₃ into the discrete Sl(2,ℤ). This and the count "d'exactement quatre façons" are checked in S01.

**R07, scan 523, conjecture. Keep.**

**R08, scan 523, conjecture. Keep.** The margin "pas tout à fait cf pg suivante pour une formulation plus raisonnable…" refers to scan 524, where the question moves from outer actions to the extension E₁₁ (R12).

**R09, scan 523, unproved claim. Keep.** The equivalence between a lift U₀,₃ → M₁₁ and a family with Jacobi rigidification of level 2 and invariant λ is the moduli interpretation of M₁₁ → M′₁₁, stated without proof.

**R10, scan 523, own idea (first pass). Drop.** Redundant: Grothendieck introduces the Γ-set E of the four lifts himself on scan 524 and derives the index "2 ou 4" and the contrast with the lift of extensions on scan 525.

**R11, scan 524, conjecture. Correct.** "Je doute qu'il en existe une" is withdrawn by the author on scan 527: the Legendre family is such a curve and its existence is "tout à fait triviale" (S02). The doubt should be recorded as superseded.

**R12, scan 524, unpursued implication. Keep.** Since T̂⁺₁₁ = Sl(2,ℤ)^ has centre ±1, outer actions lose information, and the question is moved to the extension E₁₁ = E_{M₁,₁} of Γ by T̂⁺₁,₁.

**R13, scans 524–525, unproved claim. Keep.** "ce qui est plus fort que de trouver un relèvement Π̂₀,₃ → T⁺₁₁ compatible avec les op. ext. de Γ": the T here is written without hat, a slip, since the target must be the profinite group.

**R14, scan 525, unproved claim. Correct.** The index is clearly "2 ou 4" (replacing a struck "divisant … 4, tel que" and a struck "4! = 24"). The argument is complete: if the continuous action of Γ on the four-element set E fixes no element, the orbit sizes are 2+2 or 4, so a stabilizer has index 2 or 4; the kernel of Γ → Aut(E) is open, so over a finite extension all four lifts commute with the action.

**R15, scan 525, conjecture. Correct.** The text is "rien ne prouve que l'on puisse trouver un “germe de relèvement” de E₀,₃ → E′₁,₁ en E₀,₃^G → E₁,₁^G (germes pris p.r. aux sous-groupes ouverts de E₀,₃ contenant Π̂₀,₃, ou m̄ de tt les sous-groupes ouverts)"; the first pass read "grand relèvement". A germ of lift is a lift on some open subgroup; the obstruction on E₀,₃ itself is α ∈ H²(E₀,₃, ℤ/2) (36). The doubt that α dies on an open subgroup is answered on scan 527 (S03).

**R16, scan 525, own idea (first pass). Keep, with the corrected wording "germe de relèvement".** For open subgroups containing Π̂₀,₃ the class does die (S03); the comparison with arbitrary open subgroups remains a sensible check.

**R17, scan 526, unproved claim. Keep.** The subscript "U₀,₂ | U₀,₃" and a possible strike through "les" ("forment les sections") remain open in the ink.

**R18, scan 526, unproved claim. Keep, with a reading note.** The ink has "(il suffirait qu'elle ne soit de type 0,0)" without "pas"; the sense is "not of type (0,0)", i.e. not ℙ¹. The underlying fact: a smooth connected curve over an algebraically closed field of characteristic 0 other than ℙ¹ is a K(π,1) for torsion coefficients, and the Hochschild–Serre spectral sequence carries this to the arithmetic group E_U.

**R19, scan 526, unproved claim. Keep.**

**R20, scan 526, own idea (first pass). Correct.** Pic(U₀,₃) = 0 (ℙ¹ minus three rational points), so the Kummer sequence gives H²(U₀,₃, μ₂) ≅ Br(U₀,₃)[2] with μ₂ = ℤ/2: here the "groupe de Brauer" identification is exact, with no line-bundle contribution.

**R21, scan 527, unproved claim. Keep.** See S03 for the derivation from (38).

**R22, scan 527, unproved claim. Keep.** H^q(Ū₀,₃) = 0 for q ≥ 2 because Ū₀,₃ is an affine curve over an algebraically closed field. The displayed sequence is the exact sequence of a spectral sequence with two nonzero rows (differentials d₂: E₂^{p,1} → E₂^{p+2,0}); S04 shows that both d₂ vanish here.

**R23, scan 527, unpursued implication. Correct.** The identification under the inner H¹(Ū) is drawn as ≀, an isomorphism with 𝔽₂². The Galois action on it is trivial (S05).

**R24, scan 527, unproved claim. Keep, with a check.** The Legendre curve y² = x(x−1)(x−λ) is smooth over U₀,₃ (discriminant 16λ²(λ−1)²), its 2-torsion points (0,0), (1,0), (λ,0) are sections, which give the level-2 rigidification, and its Legendre invariant is λ. This settles R11.

**R25, scan 528, conjecture. Keep.** "Je ne vais pas approfondir la question ici, dans quelle mesure ce choix est “naturel”": the choice is one of four quadratic twists (S06).

**R26, scan 528, unproved claim. Correct.** In (40) the identifications Π̂₀,₃ ≀ T̂^{!+}₀,₄, E₀,₃ ≀ N^!₀,₄ and T̂⁺₁₁ ≀ Sl(2,ℤ)^ are drawn as isomorphisms; E₁₁ = N₁,₁ and Γ = Γ as equalities.

**R27, scan 528, unproved claim. Keep.**

**R28, scan 528, unproved claim. Keep, with a check.** For the Legendre family the discrete monodromy is injective, with image ⟨A, B⟩ = {γ ∈ Γ(2) : a ≡ 1 mod 4} (S07). Injectivity after completion holds because ⟨A, B⟩ has finite index (12) in Sl(2,ℤ), so the profinite topology of Sl(2,ℤ) induces the full profinite topology on it and its completion embeds in Sl(2,ℤ)^.

**R29, scan 528, unproved claim. Correct.** The reading is "le sous-groupe de congruence du deuxième mb(?) …, soit Γ₂, soit produit direct de ce sous-groupe Π₀,₃ et de son centre ±1". It is true: Γ(2) = ⟨A, B⟩ × {±1} with ⟨A, B⟩ free of rank 2 (S07).

**R30, scans 527–528, own idea (first pass). Keep, made precise.** The four quadratic twists by 1, λ, 1−λ, λ(1−λ) realize the four lifts of E (S06).

**R31, scan 528, own idea (first pass). Keep.** A and B are the standard Legendre monodromies around λ = 0 and λ = 1 in a suitable basis. Their product AB = [[−3,2],[−2,1]] has trace −2, so the monodromy at ∞ is minus a unipotent (fibre of type I₂* there).

**R32, scan 527, own idea (first pass). Correct (answered).** The action is trivial and E₂^{1,1} ≅ H¹(ℚ, ℤ/2)² ≅ (ℚ*/ℚ*²)² (S05).

**R33, scan 529, unproved claim. Correct (checked).** There are exactly four complements of ±1 in Γ₂, and their intersection has index 8 in Γ₂ (a divisor of 16) and 4 in Π₀,₃ (a divisor of 8) (S07, S08).

**R34, scan 529, upper margin, unproved claim. Correct (checked).** The NB is true: the intersection is Γ(4) = Ker(Sl(2,ℤ) → Sl(2,ℤ/4ℤ)) (S08); in the profinite setting it is the corresponding kernel of Sl(2,ℤ)^ → Sl(2,ℤ/4ℤ).

**R35, scan 529, conjecture. Correct: the guess is false.** "Ça m'étonnerait pas que ce soit juste le groupe des commutateurs de Π₀,₃,) qui est d'indice 4" is false: the commutator subgroup of a free group of rank 2 has infinite index (abelianization ℤ², or ℤ̂² for the profinite group). The intersection is Π₀,₃²[Π₀,₃, Π₀,₃] = Ker(Π₀,₃ → H₁(Π₀,₃, 𝔽₂)), of index 4. The margin "c'est vrai et c'est ≃/m̄ trivial…" stands beside "il est d'indice un diviseur de 8", which is true.

**R36, scan 529, own idea (first pass). Keep.** It is the correct diagnosis of R35.

**R37, scan 529, lower margin, conjecture. Correct (answered).** The margin reads "Il n'est pas clair ~~si Π₀,₃~~ est invariant …, je présume que oui, puisque 𝔖₃ opère aussi extérieurement sur Π₀,₃". For the untwisted Legendre image the answer is no; exactly one of the four complements is normal in Sl(2,ℤ) (S09).

**R38, scan 529, lower margin, unpursued implication. Correct (answered).** For the normal complement, T⁺₁₁/Π₀,₃ is the dicyclic group of order 12, a non-split central extension of 𝔖₃ by ±1 (S09).

**R39, scan 529, own idea (first pass). Keep.** Carried out in S09: 𝔖₃ permutes the four complements with orbits of sizes 1 and 3.

**R40, scan 529, unproved claim. Keep, with readings.** "(défini mod autom. intérieurs)" is now read; the generators are written l₀, l₁, l₂ (the witnesses print l∞).

**R41, scan 530, unproved claim. Keep.** A proof sketch along the indicated lines is in S10.

**R42, scan 530, unproved claim. Keep.** According to the witnesses, the next scan completes the proof with the composite Γ_ℚ → Γ₁,₁ → Autext T̂⁺₁,₁ → Autext T̂′⁺₁,₁, injective by the theorem.

**R43, scan 530, unpursued implication. Keep.** The passage to the central quotient is covered by the argument of S10, which works with T̂′⁺₁,₁ directly.

**R44, scan 530, own idea (first pass). Keep.** It is the argument of the next page (per the witnesses).

## Second-pass notes (mine)

**S01, scan 523, unproved claim checked (mine).** The preimage of Sl(2,ℤ)/±1 under Sl(2,ℤ)^ → Sl(2,ℤ)^/±1 is Sl(2,ℤ)·{±1} = Sl(2,ℤ), so every lift of Π̂₀,₃ → Sl(2,ℤ)^/±1 sends the discrete Π₀,₃ into Sl(2,ℤ): "nécessairement … respectent les réseaux discrets" is immediate. Two lifts of a map into G/Z with Z central differ by a homomorphism into Z, so the lifts form a torsor under Hom(Π̂₀,₃, ±1) ≅ (ℤ/2)², which gives "d'exactement quatre façons".

**S02, scans 524 → 527, conjecture withdrawn by the author (mine).** The doubt of scan 524 is answered on scan 527 by the Legendre curve (R24). Since that curve is defined over ℚ, it gives (39) and the map of extensions (40), i.e. the strong form of the question (a lift E₀,₃ → E₁₁), and a fortiori a Γ-invariant element of E.

**S03, scans 525/527, unpursued implication (mine).** By (38) and H^q(Ū₀,₃) = 0 for q ≥ 2, a class of H²(U₀,₃, ℤ/2) dies over a finite extension of ℚ: its component in H¹(K, H¹(Ū)) dies over a finite extension, and the rest comes from H²(K, ℤ/2), which dies over a further one. Through H*(E_U, −) ≅ H*(U, −) this answers the "rien ne dit" of scan 525 for open subgroups containing Π̂₀,₃. Grothendieck does not draw this conclusion; he passes directly to the explicit curve.

**S04, scan 527, own idea (mine; confidence high).** U₀,₃(ℚ) is nonempty (λ = 2), so π₁(U₀,₃) → Γ has a section and H^n(ℚ, M) → H^n(U₀,₃, M) is injective (U₀,₃ is a K(π,1)). Hence both d₂ of the displayed sequence vanish and 0 → H²(ℚ, ℤ/2) → H²(U₀,₃, ℤ/2) → H¹(ℚ, ℤ/2)² → 0 is exact, using S05.

**S05, scan 527, unpursued implication answered (mine; confidence high).** By Kummer theory (Pic Ū₀,₃ = 0, μ₂ = ℤ/2), H¹(Ū₀,₃, ℤ/2) ≅ O(Ū)*/O(Ū)*² is spanned by the classes of λ and 1−λ, functions defined over ℚ; so Gal(ℚ̄/ℚ) acts trivially on the 𝔽₂² and E₂^{1,1} ≅ H¹(ℚ, ℤ/2)² ≅ (ℚ*/ℚ*²)².

**S06, scans 524–528, own idea (mine; confidence medium).** Twisting the Legendre curve by u multiplies its monodromy by the Kummer character of u, and the characters of u ∈ {1, λ, 1−λ, λ(1−λ)} are exactly Hom(Π̂₀,₃, ±1); so the four twists u·y² = x(x−1)(x−λ) realize the four lifts of E, and this is the ambiguity in Grothendieck's "choix". All four twists are defined over ℚ, which suggests that Γ fixes E pointwise; this should be checked against the outer-homomorphism convention and the "quitte à passer à une extension un peu plus grande" of scan 525.

**S07, scans 528–529, claims checked (mine).** γ ↦ a mod 4 (γ = [[a,b],[c,d]]) is a homomorphism ε: Γ(2) → ±1, since bc′ ≡ 0 mod 4; so do β(γ) = (−1)^{b/2} and κ(γ) = (−1)^{c/2}. Γ(2) is generated by A, B and −1, and ⟨A, B⟩ (free of rank 2, Sanov) lies in Ker ε, which does not contain −1; so ⟨A, B⟩ = Ker ε and Γ(2) = ⟨A, B⟩ × {±1}, which verifies (42) and the "produit direct". The four complements of ±1 are Ker ε, Ker εβ, Ker εκ, Ker εβκ: "exactement quatre".

**S08, scan 529, claims checked, one refuted (mine).** The intersection of the four complements is Ker ε ∩ Ker β ∩ Ker κ = Γ(4), of index 8 in Γ(2) and 4 in Π₀,₃: the NB of the upper margin is correct, and so are "diviseur de 16" and "diviseur de 8". The commutator-subgroup guess is false (R35).

**S09, scan 529, lower margin, conjecture answered (mine; confidence high for the group theory).** Conjugation by S fixes ε and swaps β, κ; conjugation by T sends ε ↦ εκ, β ↦ βκ, κ ↦ κ. So 𝔖₃ = Sl(2,ℤ)/Γ(2) permutes the four complements with orbits {Ker εβκ} and {Ker ε, Ker εβ, Ker εκ}: exactly one complement is normal in Sl(2,ℤ). The Legendre image Ker ε is not normal, so "je présume que oui" holds for one of the four lifts only (with R31's matrices, the twist by λ(1−λ)). For that one, Sl(2,ℤ)/Ker εβκ has order 12 and S has order 4 in it (S² = −1 ∉ Ker εβκ), so it is the dicyclic group ℤ/3 ⋊ ℤ/4, a non-split central extension of 𝔖₃ by ±1.

**S10, scan 530, own idea: proof of the theorem (mine; confidence medium).** Let K ⊂ Γ_ℚ act by inner automorphisms on T̂′⁺₁,₁. Since Π̂₀,₃ is normal in T̂′⁺₁,₁ with quotient 𝔖₃ (33), and the inclusion is Γ-compatible, K acts on Π̂₀,₃ through the image of 𝔖₃ in Out(Π̂₀,₃); the outer action of Γ_ℚ on Π̂₀,₃ is faithful (Belyi), so K embeds in a group of order dividing 6. A finite normal subgroup of Γ_ℚ is trivial (Artin–Schreier: its nontrivial finite subgroups have order 2 and are generated by complex conjugations, which are not normal), so K = 1; faithfulness on T̂⁺₁,₁ follows. The step through Out(Π̂₀,₃) needs care with the choice of the outer homomorphism.

# LM_C3-150-168 — research notes, checked against the corrected transcription

Source: Grothendieck, *La Longue Marche à travers la théorie de Galois* (1981), Montpellier archive cote 140-3, scans 150–168 (§44, ms. pp. 365–382). References are to `LM_C3-150-168_checked.tex`. Part A takes the first pass's notes in order (F1–F50) with a verdict; Part B adds notes written in the second pass (S1–S8).

## A. First-pass notes, checked

### Scans 150–154

- **F1. Scan 151 — unproved claim / expectation.** Keep. "On doit pouvoir vérifier que le schéma (sur Spec ℤ) des solutions de ces équations est de dim. relative 3 …", corrected in the margin to "non, il est de dim. rel totale 4"; a proof needs the exact equation set, the base and a fibre analysis. The corrected reading "de ces équations" does not change the note; S2 gives a likely account of the marginal 4.
- **F2. Scan 151 — unproved claim.** Keep, now checked (S1). The NB "cette dernière est conséquence des autres, compte tenu de C+D−B=1 et AD−BC=1" holds over any coefficient ring once μU=ε (equivalently μD=1 with D=εU) and RU−T²=1 are used; invertibility enters through U=ε/μ.
- **F3. Scan 152 — expository plan (first pass: conjecture / expectation).** Correct. The margin reads "en d'autres termes, on a μ≡ε (4) car U=t²+u²≡1 (4) … Ce serait le moment d'inclure [aussi|ici] la relation μ≡δ (3), cf. avec la démonstration idoine…": a restatement of the mod-4 result and a plan to insert the mod-3 relation with its proof, which the main text then gives ("On avait vu de façon toute analogue … que μ≡δ (3)"). Not a conjecture.
- **F4. Scan 152, (63) — own idea (first pass).** Keep. "Égal à 1 sss μ_p ∈ (ℤ_p*)²" is right at p=3 (μ≡1 mod 3) but not at p=2: the 2-adic unit squares are 1+8ℤ₂, whereas ε₂ is the mod-4 character with kernel 1+4ℤ₂ (μ=5 separates them). The transcription keeps the written criterion.
- **F5. Scan 152 — unpursued implication.** Keep. The modulus in "μ mod 3" is a 3 written over a 2 (doubt mark kept); with ε₃ ↔ μ mod 3, ε₂ ↔ μ mod 4, the margin's (ℤ/12ℤ)* ≃ (ℤ/4ℤ)*×(ℤ/3ℤ)* only re-expresses the pair of signs and imposes no further condition on μ.
- **F6. Scan 153, (65) — unpursued implication.** Keep, with an addition: the invariance is made explicit on scan 159 by (79), ℓ₀ⁿ leaving the lower row (t,u) unchanged, so g in (65) depends only on (t,u) and μ.
- **F7. Scan 153, left margin — unproved claim.** Keep, with the corrected reading: the note ends "alors que f etc sont [?] choix d'ambiguïtés f↦l₀ⁿf etc…", i.e. f is defined only up to f↦ℓ₀ⁿf, while α is claimed determined up to sign by the automorphism. The claim is not proved at this place.
- **F8. Scan 154, (68 bis)–(69) — unpursued implication.** Keep. The remaining freedom is u=αu₀ with u₀ in the centraliser of ρ, then cut down by (66), (67).
- **F9. Scan 154 — unproved claim recalled from earlier.** Keep. "Nous avons déjà remarqué que (67), (68) déterminent u seulement modulo … un scalaire λ∈ℤ̂*" refers to earlier pages outside this package.
- **F10. Scan 154 — expectation.** Keep. "On espère néanmoins tomber sur un choix canonique" is answered on scan 159 ("on va définir canoniquement, modulo signe, … la matrice u par la formule (75)") and questioned again at the end of scan 168.
- **F11. Scan 154, (70) — own idea (first pass).** Keep, verified: ρ=(0 1; −1 1) is cyclic (e₁, ρe₁ form a basis), so its centraliser in M₂(A) over any commutative ring A is A[ρ] = {p+qρ} = {(p q; −q p+q)}, and det(p+qρ)=p²+pq+q² as in (71).

### Scans 155–159

- **F12. Scan 155, after (73) — Grothendieck's conjecture.** Keep, with the reading corrected to "sss p≡1 (4)": he suspected that ε′=+1 exactly when the multiplier is ≡1 mod 4, after a first universal answer proved incompatible with class field theory. The Théorème on scan 158 confirms it in the form α₂≡0 (2) sss μ≡1 (4); see S5 on the letter p.
- **F13. Scan 155, margin "(⟺ sans doute, ε₂=1)" — conjecture.** Keep; settled on scans 156–158, where the commuting case is exactly ε₂=1.
- **F14. Scan 155, (71)–(73) — own idea (first pass).** Keep. (73) gives u₀=μ(cρ+d) directly, and (71) with p=d, q=c gives det(cρ+d)=c²+cd+d², the norm form of ℤ̂[ρ].
- **F15. Scan 156, margin "On pourrait aussi appliquer les formules §43 (78)" — unpursued implication.** Keep; §43 lies outside this package.
- **F16. Scan 156, final paragraph — conjecture.** Keep. The guess "au pif" for ε₂=−1 is tested and repaired on scan 157; S6 records the change of τ∞ made on the way.
- **F17. Scan 157 — unpursued implication.** Keep. The trial with the reflection on the left gives "2μut=0 i.e. ut=0 — décidément, ça déconne !", and placing it on the right works; both stages should be kept.
- **F18. Scan 158, (77) — own idea (first pass).** Correct. The minus sign itself is doubtful in the ink (a minute mark, now `\unsure{-|\cdot}`). From the "i.e." clause u(σ∞)=ε₂σ∞ one gets [u,σ∞]=uσ∞u⁻¹σ∞⁻¹=ε₂·id, and for ε₂=−1 the right factor τ=diag(1,−1) does give τσ∞τ⁻¹=−σ∞ (σ∞=(0 1; −1 0)); so (77) should read +ε₂·id.
- **F19. Scan 158, Corollaire — unproved claim.** Keep, with the group read as Ŝ⁺₀,₃ (script S, quotient 𝔖₃ ≃ Ŝ⁺₀,₃/Π̂₀,₃) rather than Ĝ/Γ̂. Descent to Sl(2,ℤ̂)′ and the identification with conjugation by a matrix of determinant μ are asserted, not proved, here; the margin on scan 159 says it has been done "pour le moment" only for u commuting with σ∞.
- **F20. Scan 159, NB in the margin — unproved claim.** Keep. The reduction to u commuting with σ∞ "quitte à conjuguer avec un autom. intérieur" is stated without the conjugating element.
- **F21. Scan 159, second margin — unpursued implication.** Keep: "On a fait ceci, pour le moment, pour u commutant à σ∞" limits the scope of the computations of scans 155–158.
- **F22. Scan 159, "modulo signe" and (79) — unpursued implication.** Keep. The canonical definition of u rests on (t,u) being determined mod sign; the remaining ambiguity is the simultaneous sign.
- **F23. Scan 159 — own idea (first pass).** Keep. The comparison of tσ∞+u with cρ+d is what scans 160–161 carry out, ending with (84) f(tσ∞+u)τ∞^{α₂}=δℓ₀^{−ν}α₀(cρ+d).

### Scans 160–164

- **F24. Scan 160, (80) — question.** Keep, with an addition: the inserted "sauf erreur" before "on doit avoir une relation" and the "?" over the equality mark the same provisional status; the margin points to the correcting factor δ=ε₃ of (82).
- **F25. Scan 161, (83)–(84) — unpursued implication.** Keep, with the reading corrected: "et sous cette forme la formule était en fait connue, comme le contenu essentiel de la relation des lacets sous forme matricielle (56) ou (57): ε₂U=D, ε₂T=C !" (*contenu* now read without doubt).
- **F26. Scans 161–162, Remarque — expectation.** Correct the quoted wording: "sous une fausse apparence d'arithmétique, on a fait par la bande des gammes d'algèbre linéaire, valables sur des anneaux quelconques et formulables sans doute sous des conditions beaucoup plus générales". The substance of the note (state the base ring, determinant and invertibility hypotheses before generalising) stands.
- **F27. Scan 162, final paragraph — expectation.** Keep, with the reading "Modulo des ajustements agréables, toutes les formules du présent § devraient pouvoir se développer dans ce contexte plus général (ainsi que des compléments substantiels)", followed by the hesitation "mais je ne sais si je vais expliciter ici…".
- **F28. Scan 162, (*) — own idea (first pass).** Keep; S8 checks that (*) is the matrix form of (56).
- **F29. Scan 163 — unproved claim.** Keep. "Schéma relatif lisse de dim relative 4" for the solutions of (*) is stated without proof; it agrees with the marginal correction "dim. rel totale 4" on scan 151 (S2).
- **F30. Scan 163 — own idea (first pass).** Keep: the Jacobians of t²+u² and c²+cd+d² degenerate in characteristics 2 and 3 respectively, so smoothness must be checked there.
- **F31. Scan 163, Proposition and (85) — proof obligation.** Keep. Scans 164–166 supply the construction (choice of r,s by (87), then a,b by (88)), and F42 below shows the solution set is a ℤ̂-torsor.
- **F32. Scan 163 — own idea (first pass).** Keep. The ink indeed has "(−ε₂,−ε₃,−ν)" against the inserted triple (ε₂,ε₃,2ν+1); μ↦−μ corresponds to ν↦−ν−1.
- **F33. Scan 163, (86) — own idea (first pass).** Keep, ink confirmed: the last term of (86) is u² (no ascender, same shape as in t²+u²), a slip for d²; (85), (96) and scan 165 have d².
- **F34. Scan 164 — unproved claim.** Keep, ink confirmed: the parenthesis reads "(car r²+s² ∈ ℤ̂* — donc ∀p, r_p et s_p ne sont pas tous deux dans pℤ_p)", whereas the existence of r,s with ur−ts=1 needs t²+u² ∈ ℤ̂*, i.e. (t,u) unimodular.
- **F35. Scan 164, (87) — own idea (first pass).** Keep, verified: if ur₀−ts₀=1 and ur−ts=1, then u(r−r₀)=t(s−s₀), and choosing α,β with αt+βu=1 gives (r−r₀, s−s₀)=λ(t,u) with λ=α(r−r₀)+β(s−s₀). So (r,s)=(r₀+λt, s₀+λu) gives all solutions; equal signs in the overwritten (87) only reparametrise λ.
- **F36. Scan 164, cancelled block — unpursued implication.** Keep. The cancelled route (D, C, B, then A=(1+BC)/D and the upper-left relation of (57)) is replaced on scan 165 by solving directly for a,b.

### Scan 165

- **F37. After (88) — unproved claim.** Keep, verified: the coefficient matrix of (88) in (a,b) is (d −c; c+d d), with determinant d²+c(c+d)=c²+cd+d²=1/(με₃), a unit, so the solution is unique.
- **F38. Middle — unpursued implication.** Keep. The ink is "μ≡ε₂ (2)"; modulo 2 cannot determine ε₂, and (87) on scan 163 has the correct "(4)".
- **F39. Lower paragraph — conjecture.** Keep: "les systèmes (t,u) comme (c,d) 'dépendent de 1 paramètre', chacun en un sens très concret qu'on pourrait sans doute préciser si on y tenait".

### Scan 166

- **F40. (89) — unproved claim.** Keep; F42 gives the proof.
- **F41. Remarque — unpursued implication.** Keep: the congruence conditions mod 2 are only begun here and on scan 167.
- **F42. (89) — own idea (first pass).** Keep, carried out: the homogeneous system forces (a,b)=κ(c,d), (r,s)=λ(t,u), and the third equation gives (ε₃/μ)(κ−λ)=0 since c²+cd+d²=ε₃/μ, t²+u²=ε₂/μ. So the kernel is ℤ̂·(c,d,t,u), and the solutions of (89) form a ℤ̂-torsor; the action of scan 168, (α₀,f)↦(ℓ₀ⁿα₀,ℓ₀ⁿf), is this action with λ=−2n.

### Scan 167

- **F43. (90) — unpursued implication.** Keep.
- **F44. Torsor paragraph — unproved claim.** Keep, now supported by F42: since d is odd, moving λ by 1 changes the parity of b, so the conditions (92) fix λ mod 2 and the lifts form a torsor under 2ℤ̂ ≃ ℤ̂, as stated ("Aucun mystère !").
- **F45. Own idea (first pass).** Keep.

### Scan 168

- **F46. Action formula — unproved claim.** Keep; verified by F42 (the action is λ=−2n on the ℤ̂-torsor of solutions of (89)). The reference now reads "(cf (87) et proposition qui va avec)".
- **F47. (95)–(97) — unpursued implication.** Keep.
- **F48. (96) — own idea (first pass).** Keep, ink confirmed: "ε₂(t²+u²)=ε₂(c²+cd+d²)=1/μ"; by (86) the second coefficient should be ε₃.
- **F49. Last paragraph — deferred question.** Correct: the extract ends "mais il me semble peu intéressant" (inserted, underlined *peu*), not "peu rationnel". Grothendieck recalls a natural normalisation of f in Π̂₀,₃ (§41, (24bis)), promises to return to it, and the sentence continues beyond scan 168.
- **F50. Own idea (first pass).** Keep.

## B. Notes added in the second pass (mine)

- **S1. Scan 151, NB beside (61) — claim checked (mine).** With C=εT, D=εU, B=C+D−1, AD−BC=1, RU−T²=1 (det f·ᵗf=1, S=T) and μU=ε: A=(1+BC)/D=ε(1+T²+TU−εT)/U=ε(R+T−εT/U)=ε(R−(μ−1)T). The fourth relation of (61) is therefore a consequence of the other three.
- **S2. Scan 151, margin "non, il est de dim. rel totale 4" — own idea (mine), confidence medium.** By S1 the system (48), (49), (61) has at most five independent equations in the nine variables a,b,c,d,r,s,t,u,μ, which leaves relative dimension 4 if they cut out a complete intersection. This would explain why Grothendieck corrected "3" to "4", and it agrees with "schéma relatif lisse de dim relative 4" on scan 163.
- **S3. Scan 151, (62) — claim checked (mine).** With ρ=(0 1; −1 1) and det α₀=δ, [α₀,ρ]=δ(a²+ab+b²−(ac+bc+bd), ac+bc+bd; ac+bd+ad−(c²+cd+d²), c²+cd+d²). This gives the four lines of (62), with +ab in the last line, and C+D−B=δ(ad−bc)=1.
- **S4. Scans 156–158, τ∞ — own idea (mine).** τ∞ is defined on scan 156 as diag(−1,1), but scans 157–158 compute with diag(1,−1) ((u t; t −u) in u·ᵗu, and diag(1,ε₂) in (75)). Since diag(−1,1)=−diag(1,−1), the switch changes u only by −1, inside the "modulo signe" of (75), and leaves (76)–(78) unchanged.
- **S5. Scan 155, "sss p≡1 (4)" — implication not pursued (mine).** The ink has p, but the condition that the later pages establish is on the multiplier (Théorème of scan 158: α₂≡0 (2) sss μ≡1 (4)); p is probably a hasty μ. The transcription keeps p.
- **S6. Scans 160–161, "si ε₂=+1" labels — claim checked (mine).** The two equalities so labelled (scan 160 bottom, scan 161 top) hold for both signs: −1+ε₂μu²=−ε₂μt² and 1−ε₂μt²=ε₂μu² are each equivalent to μ(t²+u²)=ε₂. This justifies Grothendieck's deletion of "si ε₂=1" after (82) and in (83); the surviving labels are leftovers.
- **S7. Scan 166 — implication not pursued (mine).** "Ce qui détermine ensuite r,s de façon unique" repeats r,s, which were just chosen with the parameter λ; by (88) it is a,b that are then determined uniquely. Probably a slip for a,b (the ink has r,s).
- **S8. Scan 162, (*) — claim checked (mine).** With ℰ₀(λ)=ε₀^λ=(1 −λ; 0 1), ℰ₀(μ−1)=(1 −2ν; 0 1)=ℓ₀^ν by (79). So (*) [α₀,ρ]=ε·ℰ₀(μ−1)[f,σ] with σ=σ∞ is exactly (56) ξ=εℓ₀^νφ, with ξ=α₀ρ(α₀)⁻¹ and φ=fσ∞(f)⁻¹.

# LM_C4-058-076 (scans 58–76): research notes, checked against the corrected text

Each first-pass note is listed with its verdict: keep, correct or drop, with a reason. Notes marked **own (2nd pass)** are added in this pass. Kinds: conjecture/question, unproved claim, unpursued implication, own idea (including verifications). Readings and equation numbers follow `LM_C4-058-076_checked.tex`; the group of units is written 𝕆*₁₂ there (the first pass had 𝔻*₁₂).

## Scans 58–62

| Scan | Kind | Note | Verdict |
|---|---|---|---|
| 58 | own idea | (92)–(93): « La condition μ̲ = 1 équivaut aux conditions » ν₂ = ν₃ = ν₀ = 0, which imply ν = ν′ = ν″ = 0. Recover the parameter functor from the preceding pages and test the equivalence over bases with 2- or 3-torsion. | keep: unchanged by the corrections; (93) does follow from (92) by (90) and (91). |
| 58 | **own (2nd pass)**, own idea (verification) | The overwritten operator in the second line of (90) must be « − ». With ν″ = ν₃ − ν₂ − 2ν₂ν₃ + 2ν₀, both lines of (91) give μ = 1 − 6ν₂ + 4ν₃ − 12ν₂ν₃ + 12ν₀ and the third line 2ν′ − ν₂ + ν₃ = 3ν″ holds; with « + » the two values of μ differ by 24ν₂ν₃. (141) on scan 75 (« ν″ + ν₂ − ν₃ + 2ν₂ν₃ divisible par 2 ») also needs « − ». The transcription keeps the doubt, since the ink is a blot. Confidence: high. | new |
| 59 | unproved claim | « Je vais admettre encore qu'on a une structure de groupe naturelle sur Z̃_{ρ,σ} », for which the projection to 𝕆*₁₂ is a homomorphism. The group law is assumed, not constructed. | keep |
| 59–60 | unproved claim | Z̃^{+0}_{ρ,σ} « est lisse en car. ≠ 3, mais pas en car. 3, où sa dim passe de la dim. relative 2 à la dim relative 3 ». | correct: the dimension statement is verified in the own note below; smoothness away from 3 still rests on the admitted group structure. |
| 59–60 | **own (2nd pass)**, own idea (verification) | Z̃^{+0} is the kernel of ℤ⁴ → ℤ², (a₀,a₁,b₀,b₁) ↦ (c₀,c₁) with c₀ = a₀ + a₁ + (b₁ − b₀), c₁ = 2a₁ − a₀ − (b₁ − b₀) (the formulas of (128), cf (61)). The 2×2 minors are 0 or ±3, so the rank is 2 over ℚ and over 𝔽_p for p ≠ 3, and 1 over 𝔽₃, where c₁ ≡ −c₀. The fibres have dimension 2 off 3 and 3 at 3, as stated, and the image has index 3 in M: it is M₀. Confidence: high. | new |
| 60 | conjecture | « ne peut, il me semble, être éliminé par une entourloupette »: there are « plus » d'automorphismes de 𝒢̲_k (pour k un corps alg. clos) with the required properties when k has characteristic 3. Which conditions a smoother replacement of Z̃_{ρ,σ} could keep is left open. | correct: the first pass quoted « pour le m̄ corps alg. clos »; the ink reads « pour k un corps alg. clos ». The substance stands. |
| 60 | conjecture | « il me semble qu'on peut construire un sous-schéma en groupes » N_{ρ,σ} of Z̃_{ρ,σ}, smooth over S₀ = Spec ℤ and equal to Z̃_{ρ,σ} over Spec ℤ[1/3]. Scans 61–63 carry the construction out. | keep |
| 61 | unpursued implication | Read in M̲₀, the loop equation (96) « devient ainsi plus stricte ». The vector bundle of the index-3 lattice M₀ must not be identified with the image of M̲ in characteristic 3. | keep |
| 61 | own idea | Compare the signs of (100)–(101) (+ν″(λ₁ − λ₀), +(1 − σ)(β₀)) with (96), (105) and (106) (−). | keep: this pass confirms « + » in the ink of (100) and (101) (both retraced) and « − » in (105); the discrepancy is the author's. |
| 62 | conjecture | Margin NB: the group N_{ρ,σ} « devrait pouvoir se noter aussi M_{ρ,σ}[0], sauf erreur », or rather (M^♯_{ρ,σ}/M_ρ)[0] « avec les notations du § 49, VI ». | correct: the first pass read Ñ_{ρ,σ}[0], a superscript b and « VI|IV »; the identification is still to be checked against § 49 VI. |
| 62 | unproved claim | « Il est clair que ce morphisme est encore un épi »: N_{ρ,σ} → 𝕆*₁₂ is onto, the fibre over μ̲ being the solutions of the linear equation (105) in M̲₀. | keep: the own note below supplies the missing step. |
| 62 | unproved claim | (106) is « un épi lisse », being associated with a hom M × M → M₀ « qui est maintenant épi »; hence « N_{ρ,σ} est lisse sur S₀ ». | correct: the first pass quoted « manifestement épi »; the claim is verified below. |
| 62 | own idea | Compute a Smith normal form of M × M → M₀ to check the surjectivity. | correct: not needed; the own note below shows that (1 − ρ_M) alone maps M isomorphically onto M₀. |
| 62 | **own (2nd pass)**, own idea (verification) | With ρ: λ₀ ↦ λ₁ ↦ λ_∞ = −λ₀ − λ₁ (as on scans 64 and 69), (1 − ρ_M)λ₀ = −δ and (1 − ρ_M)λ₁ = λ₀ + 2λ₁ = −δ + 3λ₁. So (1 − ρ_M) sends a basis of M to a basis of M₀ = ℤδ ⊕ ℤ·3λ₁ (108): it is an isomorphism M ⥲ M₀. Hence M × M → M₀ is split onto over ℤ, its kernel is free of rank 2, (106) is a smooth epimorphism, and N_{ρ,σ} is smooth over Spec ℤ, as claimed. Confidence: high. | new |

## Scans 63–67

| Scan | Kind | Note | Verdict |
|---|---|---|---|
| 63 | unproved claim | (107): N_{ρ,σ} is the schematic closure of Z̃_{ρ,σ}|(Spec ℤ ∖ {3}), « ce qui implique que c'est aussi un sous-schéma en groupes ». | keep: the step that makes it work is the flatness of N_{ρ,σ} over ℤ (it is smooth, scan 62); a closed subscheme flat over ℤ is the closure of its part over ℤ[1/3]. |
| 63 | unproved claim | (108)–(109): M₀ is stable under ρ, σ and τ_M = −id_M « par construction », hence « normalisé par 𝒢 » and distingué; it corresponds to a normal subgroup of 𝒢₀ = Gl(2, ℤ) of index 3 in Π₀. | keep |
| 64 | conjecture | « Je présume qu'il contient le sous-groupe de congruences relatif à 12 », i.e. that it corresponds to a normal subgroup of Sl(2, ℤ/12ℤ). | keep: established in the Proposition of scan 66 by the argument of scans 65–67. |
| 64 | question | « La question est donc si ce sous-groupe distingué de Sl(2, ℤ/12ℤ) est bel et bien d'ordre 32, donc d'indice 36. » | keep: answered yes on scan 65. |
| 64–65 | question | « Déjà quel est l'ordre de δ ? mod 12 ? » | keep: (111)–(112) answer it; see the own note below. |
| 65 | unproved claim | « Cela montre que c'est bien le sous-groupe distingué engendré par δ (dont l'ordre à priori était multiple de 32) ». | correct: the first pass asked where the divisibility comes from. The normal subgroup generated by δ̇ is the image of Π₀₀, whose index in Sl(2, ℤ) is 36, so its index in Sl(2, ℤ/12ℤ) divides 36 and its order is a multiple of 1152/36 = 32. Lying in Ker(u × v), of order 32, it equals that kernel. |
| 64–65 | **own (2nd pass)**, own idea (verification) | δ = (1 2; 2 5): δ² = (5 12; 12 29) ≡ 5·1 and δ⁴ ≡ 25·1 ≡ 1 mod 12, so δ has order 4 mod 12, of order 2 in Sl(2, ℤ/4ℤ) and 4 in Sl(2, ℤ/3ℤ), as (112) says. The indices 6, 2, 3 of (114) give 36, and |Sl(2, ℤ/12ℤ)| = 48·24 = 1152 = 36·32. Confidence: high. | new |
| 66 | own idea | Check the subgroup under Syl₂ in (116), written « ≃ D₄ », by listing its elements and their orders. | correct: done in the own note below; the cancelled word before « D₄ » is illegible, not « D₄ ». |
| 66 | **own (2nd pass)**, unproved claim (slip) | Sl(2, 𝔽₃) has exactly one element of order 2, namely −1, and no element of order 8. Its Sylow 2-subgroup, of order 8, is therefore the quaternion group Q₈; the dihedral group D₄ has five elements of order 2. The « Syl₂ ≃ D₄ » of (116) is a slip; the orders in (116) (48×24, 8×24, 4×24, 4×8) are right. Confidence: high. | new |
| 66 | unproved claim | Margin NB: (𝒢₀⁺)_ab ≃ ℤ/12ℤ « s'identifie à un quotient de H/Π₀₀^• par un ss-groupe d'ordre 3 », generated by (−ρ̇, 1). | keep: the orders agree (|H/Π₀₀^•| = 36, and 36/3 = 12 = |Sl(2, ℤ)^ab|); the generator still needs checking. |
| 67 | unpursued implication | « Le m̄ argument pouvait s'appliquer au cas de Π₀, Π₀^• »: every stage of the tower (114)/(116) can be treated by inclusion plus index. | keep |
| 67 | unpursued implication | The corollary factors Gl(2, ℤ) → Gl(2, ℤ/12ℤ)/Π₀₀^• through 𝒢 = Gl(2, ℤ)/[Π₀, Π₀] « étudié dans le présent § 51 », with inverse image M₀; the NB says the full map 𝒢₀⁺ → Sl(2, ℤ/12ℤ) does not factor. | correct: section number now 51 and the NB ends « l'un et l'autre »; the NB argument is checked below. |
| 67 | **own (2nd pass)**, own idea (verification) | Π₀ maps onto Π₀^• = 𝔰𝔩(2, 𝔽₂)′ × Sl(2, ℤ/3ℤ), because Π₀ is the inverse image of Π₀^• and Sl(2, ℤ) → Sl(2, ℤ/12ℤ) is onto. A factorisation through 𝒢⁺ would make Π₀^• a quotient of the abelian Π₀/[Π₀, Π₀] ≃ M, but Sl(2, ℤ/3ℤ) is not commutative. So the NB's argument is sound. Confidence: high. | new |
| 64–67 | own idea | An exhaustive computation modulo 12 could check the order of δ, the normal subgroup it generates and the orders in (116), taking each doubtful symbol as an explicit input. | keep: partly done in the own notes above. |

## Scans 68–72

| Scan | Kind | Note | Verdict |
|---|---|---|---|
| 68 | unproved claim | « On vérifie tout de suite que c'est une courbe de genre 1 »: the cyclic triple cover of U_{0,Q̄} given by Π₀₀. | correct: the first pass quoted « du reste »; the claim is verified below. |
| 68 | **own (2nd pass)**, own idea (verification) | Π₀/Π₀₀ ≃ M/M₀ ≃ ℤ/3, by c₀λ₀ + c₁λ₁ ↦ c₀ + c₁ (99). λ₀ and λ₁ map to 1 and λ_∞ = −λ₀ − λ₁ to −2 ≡ 1, so 0, 1 and ∞ are totally ramified, and Riemann–Hurwitz gives 2g − 2 = 3·(−2) + 3·2 = 0, so g = 1. The cover is y³ = t(t − 1); y ↦ ζ₃y is an automorphism of order 3 with fixed points, so j = 0, as the margin says. Over ℚ̄ it is isomorphic to the Fermat cubic. Confidence: high. | new |
| 68 | unproved claim | Margin: « c'est une courbe elliptique d'invariant 0 (car elle est munie d'un automorphisme d'ordre 3) ». | keep: verified in the note above (the automorphism has fixed points). |
| 68 | conjecture | Replace [Π₀, Π₀] by [Π₀,₀, Π₀,₀]: the extension of M by an « elliptique » group of rank 2 on which M acts « de façon hautement non triviale »; « il nous faudrait examiner cette action » and relate it to the action subordinated to Sl(2, ℤ)^∧ → Sl(2, ℤ̂). | keep |
| 68 | own idea | Write the conjugation action of the two generators of M on a basis of the rank-2 kernel and compare with the last homomorphism of the page. Base point and splitting conventions are not fixed here. | keep |
| 69 | question | « aura-t-on pour autant la relation des lacets » for int(ℓ)? The computation answers: only for ℓ = c₀λ₀. | keep |
| 69 | unpursued implication | (119)–(120) single out c₁ = 0 and introduce L̲₀^M = Im(ℤ̲ → M̲), c₀ ↦ c₀λ₀. Which lattice and scheme make the condition stable under base change is to be checked. | keep |
| 70 | unproved claim | The image of L̲₀^M → N̲_{ρ,σ} is invariant, the two actions deduced from (121) agreeing; « d'après la théorie générale » one gets M̲_{ρ,σ} and the diagram (123). | keep |
| 70 | unproved claim | « on a un hom de (124) dans (123) », whence M^♯_{ρ,σ} ⊂ M_{ρ,σ} (125). | keep |
| 70 | conjecture | Margin: « avec les notations du § 49 VI » the group M̲_{ρ,σ} « serait sans doute noté » M̲_{ρ,σ}/H_ρ, and M̲^♯_{ρ,σ} would be M̲^♯_{ρ,σ}/H_ρ (loc. cit. 8°). | keep |
| 71 | unproved claim | N^{0+}_{ρ,σ} is identified with the kernel of the hom M × M → M₀ of (128), described by c₀ = c₁ = 0 « cf (61) ». | correct: the first pass asked for a check; direct computation of (1 − ρ_M)(α₀) − (1 − σ_M)(β₀) gives exactly these c₀, c₁. |
| 71 | unproved claim | N^{0+}/ℤ is a free ℤ-module of rank 1, ℤ embedded by n ↦ (nλ₀, nλ₀). | correct: verified in the note below. |
| 71 | own idea | An integral normal form of the two coefficient equations would give explicit bases of the kernel and its quotient. | correct: carried out in the note below. |
| 71 | **own (2nd pass)**, own idea (verification) | Adding c₀ = 0 and c₁ = 0 gives 3a₁ = 0, so a₁ = 0 and b₀ = a₀ + b₁. Thus N^{0+} is free with basis (λ₀, λ₀) and (0, λ₀ + λ₁) = (0, −λ_∞); the first spans the image of (130), and N^{0+}/ℤ is free of rank 1, generated by the class of the second. This matches (131)–(132) and the ranks « rg 2 », « rg 1 » of (133). Confidence: high. | new |
| 72 | unproved claim | « Ainsi, tous les schémas en groupes qu'on vient de construire sont lisses sur Spec ℤ. » | keep |
| 72 | question | « Peut-on définir une section plus-ou-moins naturelle de l'extension (N_{ρ,σ} de Γ_{ρ,σ} par L₀^M, donc de) M^♯_{ρ,σ} de Γ_{ρ,σ} par M̲ ? » | keep |
| 72 | conjecture | « il semble qu'on trouve une telle section dès qu'on choisit un scindage » of the two sequences (133) of ℤ-modules. | keep: the splittings are explicit (own note below). |
| 72 | unproved claim | « il faut vérifier que les sections “ensemblistes” de schémas que ça permet de définir sont multiplicatives ». | keep |
| 72 | own idea | With explicit splittings, compute the defect s(x)s(y)s(xy)⁻¹ and its dependence on the choice. | keep |
| 72 | **own (2nd pass)**, own idea | Explicit splittings of (133): M₀ → M × M, m ↦ ((1 − ρ_M)⁻¹m, 0), which exists over ℤ because 1 − ρ_M: M → M₀ is an isomorphism (scan 62 note); and Γ⁰⁺ → N⁰⁺, generator ↦ (0, λ₀ + λ₁). These are the natural candidates for the multiplicativity test the text asks for. Confidence: high for the splittings, none claimed for multiplicativity. | new |

## Scans 73–76

| Scan | Kind | Note | Verdict |
|---|---|---|---|
| 73 | unproved claim | « et on aura » Z̲_{ρ,σ} ≃ Σ̲^{eff}_{ρ,σ} (137): automorphisms are described by (μ̲, ξ₀, η₀) with the loop equation in M̲₀ and the local image conditions (136). | keep |
| 73–74 | unproved claim | « donc (136) est une condition sur η₀ seulement », namely (136bis) η₀ ∈ Γ Im(G_a → M̲₀, λ ↦ λδ) = Γ Ker(M₀ → G_a, c₀λ₀ + c₁λ₁ ↦ c₀ + c₁). | correct: verified: (1 − ρ_M)(M) = M₀ (scan 62 note) makes the ξ₀ condition automatic, and (1 − σ_M)(b₀λ₀ + b₁λ₁) = (b₁ − b₀)δ, whose span ℤδ is the kernel of c₀ + c₁ on M₀. |
| 74 | unproved claim | (138)–(139): Σ̲^{eff}_{ρ,σ} ⥲ 𝕆*₁₂ × Z̲δ, because ξ₀ « se récupère avec μ̲, η₀ » by the loop equation; the boxed inverse computation is cancelled. | keep: ξ₀ = η₀ + ν″(μ̲)(3λ₁) by 1°) of (137) directly; the cancelled (1 − ρ_M)⁻¹ is legitimate over ℤ. |
| 74–75 | own idea | Investigate failure of the reconstruction of μ̲ from ξ₀, ν₂, ν₃ over bases with 2-torsion: the text recovers 2ν₀ and then ν₀ « sur une base où 2 est section régulière ». | keep |
| 75 | own idea | Audit the target factors {0, 1} of (140) against the components ε₂(μ̲), ε₃(μ̲), which are signs. | keep |
| 75 | own idea | Check the value under the brace in (141). | correct: this pass confirms the ink: multiplier 6, and « 1 − 2ν₃ − 2ν₂ν₃ + 6ν″ » under the brace; see the own note. |
| 75 | **own (2nd pass)**, unproved claim (slip) | For ν₂, ν₃ ∈ {0, 1}, (−5)^{ν₂}(+5)^{ν₃} + 6(ν″ + ν₂ − ν₃ + 2ν₂ν₃) = 1 − 2ν₃ − 12ν₂ν₃ + 6ν″ (at ν₂ = ν₃ = 1 both sides are 6ν″ − 13). This agrees with (91), μ = 1 − 2ν₃ + 6ν″, modulo 12ν₂ν₃; the « −2ν₂ν₃ » under the brace looks like a slip for −12ν₂ν₃. Confidence: medium. | new |
| 75 | unproved claim | « En tout état de cause on voit que Σ̲^{eff}_{ρ,σ} donc aussi Z̲_{ρ,σ} est lisse de dim relative 2 », with (142) 1 → Z̲^{+0}_{ρ,σ} → Z̲_{ρ,σ} → 𝕆*₁₂ → 1 and Z̲^{+0} ≃ G_a. | keep |
| 76 | unproved claim | « D'ailleurs on a un scindage canonique » (149) of Z̲_{ρ,σ} over γ_{ρ,σ} = 𝕆*₁₂, μ̲ ↦ (μ̲, ξ₀ = ν″(3λ₁), η₀ = 0); multiplicativity needs the composition law, including how ν″ transforms. | keep |
| 76 | own idea | Test the action (151) on the defining relations and on composition of parameters once the overwritten coefficient (6ν″|6ν) is settled. | keep |
| 76 | unpursued implication | Margin NB: « On pose G^♯_{ρ,σ} = 𝕆*₁₂·𝒢̲^♯ ⊂ G_{ρ,σ} », with γ_{ρ,σ} under 𝕆*₁₂ and M̲ under 𝒢̲^♯; compare with the action (151) and with M^♯_{ρ,σ} of scans 69–72. | keep |

## Editorial note on folios and the reference « p. 686 »

| Scan | Kind | Note | Verdict |
|---|---|---|---|
| 59–75, 73 | **own (2nd pass)**, own idea (editorial) | The tens digit of every folio in the package is retraced; the final readings 677–685 agree with the author's table (5) at p. 682, 6) at p. 684). On folio 684 (scan 73) ν″ is referred to « (cf p. v. p. 686) », although ν″ is defined in (90) on scan 58, the verso of the sheet before folio 677. If the sheets first carried numbers ten higher (687–695 for these folios), scan 58 was then the verso of p. 686 and « p. v. » may abbreviate that verso. This is a hypothesis about the numbering, not a reading. Confidence: medium. | new |

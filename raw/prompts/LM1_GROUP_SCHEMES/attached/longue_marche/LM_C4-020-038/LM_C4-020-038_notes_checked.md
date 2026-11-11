# LM_C4-020-038 (scans 20–38): research notes, checked against the corrected text

Each first-pass note is listed with its verdict: keep, correct or drop, with a reason. Notes marked **own (2nd pass)** are added in this pass. Kinds: conjecture/question, unproved claim, unpursued implication, own idea, verification. Readings and equation numbers follow `LM_C4-020-038_checked.tex`.

## Scan 20

| Kind | Note | Verdict |
|---|---|---|
| unproved claim | Below (35): (34) « se reconstitue à partir de (35) », and Φ induces the isomorphism 𝒢_{S₀}/M_{S₀} ⥲ 𝒢̲/M̲ (= H_{S₀}). The axiomatic description is asserted, not proved, on this page. | keep: unchanged by the corrections. |
| unproved claim | Margin: the hypothesis on H¹ is « entièrement inutile », because the M̲-torsors over S₀ defined by the inverse images of the h ∈ H are « évidemment triviaux ». | correct: the first pass asked for a separate proof, but the proof is immediate (own note below). The note opens « L'hyp. ». |
| own idea | Compare exactness of (37) on sections with the torsor obstruction for an arbitrary S. | correct: superseded by the own note below. Because the torsors are trivial, (37) is exact over every S, not only affine ones. |
| **own (2nd pass)**, verification | For h ∈ H choose g ∈ 𝒢 over h (𝒢 → H is onto). Then Φ(g) ∈ 𝒢̲(S₀) is a section of the fibre of 𝒢̲ → H_{S₀} over h, so that M̲-torsor is trivial. Given a locally constant h: S → H, the pieces where h is constant are open and closed and disjoint, so the lifts Φ(g_h) glue. Hence 𝒢̲(S) → H_{S₀}(S) is onto for every S, and (37) is exact without any H¹ condition, as the margin says. Confidence: high. | new |

## Scan 21

| Kind | Note | Verdict |
|---|---|---|
| unproved claim | The construction of 𝒢̲ from (27) is « manifestement fonctorielle p.r. à cette dernière ». Functoriality and compatibility with the maps of (38) and (41) are not written out. | keep |
| unproved claim | Margin: as a sheaf, 𝒢̲ is isomorphic to the « faisceau somme des H copies de M̲ », hence representable if M̲ is. | correct: add that the isomorphism depends on a choice of lifts g_h of the h ∈ H, the fibre over h being Φ(g_h)·M̲. The sum is then represented by the disjoint union of copies of M̲. |
| unpursued implication | Separate functoriality of the representing object from exactness after taking sections in (38)–(39). | correct: the H¹ hypothesis is not removed from the main text. The margin of scan 20 declares it useless. The point stands with that wording. |

## Scan 22

| Kind | Note | Verdict |
|---|---|---|
| unpursued implication | In (41), check whether each face of the cube commutes strictly or only up to the choices made in the construction. | keep |
| unproved claim | (43)–(44): H_i = 𝒢/M_i is the extension of H by M/M_i deduced from (27) by M → M/M_i, given M_i stable under H. | correct: the ink now reads « \unsure{l'\|une} extension » (« une » corrected to « l' »). The claim is the identification of 𝒢/M_i with the pushout, which is standard but not proved here. |
| own idea | Distinguish all finite-index subgroups of M from the H-stable ones before forming the inverse system. Confidence: high. | keep: the margin « prendre les nM ! » on scan 23 settles the cofinality. |

## Scan 23

| Kind | Note | Verdict |
|---|---|---|
| unproved claim | The H-stable finite-index M_i are cofinal among all finite-index subgroups (a stronger hypothesis on H was struck). Proof direction from the margin « prendre les nM ! »: if N has index n then nM ⊂ N, and nM is characteristic. | keep: the argument is correct. |
| unproved claim | The sequences (45) « forment un syst. projectif d'extensions »; ordering and transition maps are not specified. | keep |
| unproved claim | Transition maps 𝒢̲_j → 𝒢̲_i are « affines ». Locality on 𝒢̲_i reduces this to E(M_i,M_j) → E(M_i,M_i) = M̲_i. | keep: completed on scan 24 (finite sum of affine schemes). |
| own idea | Check that the affineness of the transitions does not depend on the cofinal family nM. Confidence: medium. | keep |

## Scan 24

| Kind | Note | Verdict |
|---|---|---|
| unproved claim | The limit of the 𝒢̲_i exists in schemes (the limit functor is representable). | keep: the general existence theorem for projective limits of schemes with affine transition morphisms (EGA IV, § 8.2) covers it. The page invokes it without reference. |
| conjecture/question | « il n'est peut être pas absurde de passer à la limite carrément … pas de t.f. »: work with the limit group scheme, which is not of finite type, instead of the pro-object. | keep |
| unproved claim | The pro-group depends only on the discrete group 𝒢 with a commensurability class of subgroups, « l'hypothèse à faire étant que » some of them are ℤ-modules of finite type. | correct: the quotation now reads « étant que », not « est que ». The independence claim itself stands. |

## Scan 25

| Kind | Note | Verdict |
|---|---|---|
| unproved claim | « ce proobjet ne dépend que de 𝒢 lui m̄ ». | keep |
| unproved claim | Env(𝒢) « dépend fonctoriellement de 𝒢 ». | keep |
| unproved claim | Multiplicativity (47) for products. | keep |
| unproved claim | Exact sequence (49) of envelopes for an exact sequence (48) of « métabéliens », in a sense to be made precise. | keep: in addition, the first Env in (49) carries a mid-height stroke and is now marked doubtful. |
| own idea | « métabélien » here means: some finite-index subgroup is commutative and of finite type over ℤ. Start from this condition, not from the name. Confidence: high. | keep: sharpened by the own note below. |
| **own (2nd pass)**, unpursued implication | In the usual sense (derived length ≤ 2) the class differs both ways. Every finite group, A₅ for example, is « métabélien » here (the trivial subgroup has finite index). The Baumslag–Solitar group ℤ[1/2] ⋊ ℤ is metabelian in the usual sense but has no finite-index subgroup of finite type that is commutative. So the term means "virtually ℤʳ" (a finite-index subgroup of finite type that is commutative, hence one isomorphic to ℤʳ). Confidence: high. | new |

## Scan 26

| Kind | Note | Verdict |
|---|---|---|
| unproved claim | « un hom fid plat dont le noyau est le bon » for the limit group schemes. | keep |
| unproved claim | The general case reduces « de façon assez immédiate » to 𝒢 = M = ℤ. | keep |
| unproved claim | The coordinate ring of 𝒢̲_n is a product of n copies of ℤ[T] « de façon pas bien canonique », through a set-theoretic section ℤ ∩ [0, n−1]. | keep |
| own idea | Write the group law with the carry ⌊(r+s)/n⌋ for the representatives 0,…,n−1. Confidence: high. | keep |

## Scan 27

| Kind | Note | Verdict |
|---|---|---|
| unproved claim | The transition maps between the 𝒢̲_n « n'ont rien de plat ». | keep: verified in the own note below. |
| unproved claim | The limit is an extension of (ℤ̂)_{S₀} by the limit of the 𝔾_a. | keep |
| unproved claim | « chose étrange »: the colimit ring is the subring of ℚ[T] whose constant term is an integer. | keep: verified in the own note below. |
| unproved claim | The analogous description for ℤⁿ (neutral component = Spec of polynomials in ℚ[T₁,…,T_n] with integral constant term). | keep |
| unpursued implication | « attention à l'abus de notation » for (ℤ̂ⁿ)_{S₀}. | keep |
| own idea | Compute the fibres of Spec(ℤ + Tℚ[T]) directly. Confidence: high. | keep: done in the own note below. |
| **own (2nd pass)**, verification | ⋃_n ℤ[T/n] = ℤ + Tℚ[T]: the coefficient of T^k (k ≥ 1) lies in n^{−k}ℤ, and every rational number is reached for a suitable n, while the constant term stays in ℤ. For A = ℤ + Tℚ[T], Tℚ[T] = p·Tℚ[T], so A/pA = 𝔽_p and every closed fibre is a reduced point (trivial group), while A ⊗ ℚ = ℚ[T] gives 𝔾_{a,ℚ}. This confirms scan 28 « toutes les fibres sont réduites au groupe unité, sauf la fibre générique ». On neutral components the transition 𝒢̲_{mn} → 𝒢̲_n is multiplication by m on 𝔾_a. It is zero on the fibres over p | m and an isomorphism generically, so it is not flat. Confidence: high. | new |

## Scan 28

| Kind | Note | Verdict |
|---|---|---|
| unproved claim | All fibres of the neutral component are trivial except the generic one, 𝔾_{a,ℚ}ⁿ. | keep: verified (scan 27 own note). |
| unproved claim | (51) is « une suite exacte canonique » with kernel Env⁰(𝒢) and quotient (𝒢̂)_{S₀}. | keep: in « comp. neutre de lim Env(𝒢) » the « lim » is overwritten and now doubtful. The intended object is still the limit. |
| unproved claim | (52) identifies lim_i M̲_i with lim_n n.M̲₀ (cofinality). | keep |
| unpursued implication | (53) M̲ = V̌(M) = Spec Sym_ℤ(M̌): keep track of covariant group-scheme maps versus contravariant algebra maps. | keep |
| own idea | Test whether the special fibres of the full limit envelope are exhausted by the profinite quotient. Confidence: medium. | keep |

## Scan 29

| Kind | Note | Verdict |
|---|---|---|
| unproved claim | The nM₀ are cofinal among all M_i, and a basis gives (54). | keep |
| unproved claim | ℰ¹ represents A ↦ {(x_n) | x_n = m x_{mn}}. | keep: verified in the own note below. |
| own idea | Identify the functor with Hom_ℤ(ℚ, A) by x_n = f(1/n). Confidence: high. | keep: verified in the own note below. |
| unproved claim | « il existe sans doute un tel n » when all residue characteristics of A are positive. The relation after nA was unresolved. | correct: the relation is now read nA = 0 (\unsure{=\|≃}, not ≥). The claim is then provable (own note below). |
| own idea | « A de car 0 »: a ℚ-algebra and a ring of characteristic 0 such as ℤ behave differently in (56). Confidence: high. | correct: this is a refutation, not only a test (own note below). |
| **own (2nd pass)**, verification | (56) describes Hom_ℤ(ℚ, A): an additive f: ℚ → A gives x_n = f(1/n) with m·x_{mn} = x_n, and conversely, since ℚ is the colimit of the (1/n)ℤ. Hence ℰ¹(A) ≅ A for every ℚ-algebra, and ℰ¹(A) = 0 when nA = 0 (f(1/k) = n·f(1/(nk)) = 0). The text writes this trivial group as « {1} ». Confidence: high. | new |
| **own (2nd pass)**, claim checked | « il existe sans doute un tel n »: if every prime ideal of A has residue characteristic > 0, then Spec(A ⊗ ℚ) is empty, so 1 ⊗ 1 = 0 and n·1 = 0 for some n ≥ 1. The claim holds when the residue characteristics are taken at all points of Spec A. It fails if only maximal ideals are meant (A = ℤ_(p)). « ce qui signifie que les car. résiduelles de A divisent n » is an equivalence only up to a power of n: A = ℤ/p², n = p. Confidence: high. | new |
| **own (2nd pass)**, refutation | « si par contre A de car 0, on a ℰ¹(A) ≃ A » is false as written: A = ℤ has characteristic 0 but ℰ¹(ℤ) = Hom(ℚ, ℤ) = 0. Equivalently, a ring map ℤ + Tℚ[T] → ℤ must send T to an integer divisible by every n, hence to 0. The statement holds for ℚ-algebras, for instance fields of characteristic 0. Confidence: high. | new |

## Scan 30

| Kind | Note | Verdict |
|---|---|---|
| unproved claim | Unipotence of H → G « se vérifie fibre par fibre ». | keep |
| unpursued implication | A homomorphism 𝒢 → Γ(G/S) is unipotent if the morphism 𝒢_S → G « qui lui correspond » is. Behaviour under base change is not pursued. | keep: in the ink only « qui » is inserted, and « lui correspond » runs on the line. The meaning is the same. |
| own idea | Test the fibrewise formulation over a nonreduced affine base with a matrix group. Confidence: medium. | keep |

## Scan 31

| Kind | Note | Verdict |
|---|---|---|
| unproved claim | (58): by « les propriétés des lim de syst. projectifs filtrants (à morphismes de transition affines) », Hom from the limit into a G locally of finite presentation is the colimit of the Hom_i. The group-law identities must also descend to a finite stage. | keep: this is the standard limit theorem for morphisms locally of finite presentation (EGA IV, § 8.13), which needs quasi-compactness hypotheses not stated here. |
| unpursued implication | (57) LEnv_S(𝒢) = LEnv(𝒢) ×_{S₀} S: separate existence of the limit from its compatibility with base change. | keep |
| own idea | (58): the right-hand term is written without L and the limit arrow points left. Check the convention against the later displays. Confidence: medium. | keep: (60)–(61) on scan 32 write Hom(LEnv_S(𝒢), G), so the missing L in (58) is a slip of the pen. |
| unpursued implication | (59)–(59 bis): injectivity and kernel of 𝒢_S → LEnv_S(𝒢) are not addressed. | keep |

## Scan 32

| Kind | Note | Verdict |
|---|---|---|
| unproved claim | Théorème: (61) is injective, with image the quasi-unipotent homomorphisms 𝒢 → G(S). | keep |
| unproved claim | The qualification « du moins si on suppose … que S est noeth. et G affine sur S ». | correct: the last symbol may read S₀ (now \unsure{S\|S_0}). « G affine sur S₀ » would mean G is an affine scheme, a stronger hypothesis than G affine over S. Which one is meant must be settled before the theorem is used. |
| unpursued implication | The revision from « bijective » to « injective, et a comme image … » makes quasi-unipotence substantive. | keep |
| own idea | Test with a cyclic source and targets 𝔾_a, 𝔾_m over an affine base. Confidence: medium. | keep: worked out in the own note below. |
| **own (2nd pass)**, own idea | For 𝒢 = ℤ and G = 𝔾_m over a field k of characteristic 0: any map from Env(ℤ) kills the 𝔾_a-parts (Hom(𝔾_a, 𝔾_m) = 0 over a reduced base), so it factors through some ℤ/n → μ_n and sends 1 to a root of unity. These are exactly the quasi-unipotent elements of k^*, consistent with the theorem. For G = 𝔾_a every element is unipotent, and every map ℤ → k extends through 𝔾_a. Confidence: medium. | new |

## Scan 33

| Kind | Note | Verdict |
|---|---|---|
| unproved claim | Π₀ is « engendré par les λ_i = −ℓ_i » (margin matrices), and (1) gives its abelianization as (ℤ(0)+ℤ(1)+ℤ(∞))/diagonale. | keep |
| unproved claim | (2): H = 𝒢₀/Π₀ ≅ GL(2,ℤ/4ℤ)/(ℓ̇₀, ℓ̇₁), without derivation. | keep |
| unproved claim | « Par générateurs et relations » (3) presents 𝒢; both directions are needed. | keep |
| unpursued implication | « le jeu des signes − »: replace an odd number of σ by σ⁻¹. | keep |
| own idea | Use ρ⁶ = σ⁴ = 1 and ρ³ = σ² to check each sign. Confidence: high. | keep: done in the own note below. |
| **own (2nd pass)**, verification | With −1 := ρ³ = σ² (central of order 2) and σ(x) = σxσ⁻¹: σρσρ = σ(ρ)σ²ρ = σ(ρ)ρ⁴, so −σρσρ = σ(ρ)ρ. This matches λ₀ = σ(ρ)ρ and explains the struck exponent 4. Likewise −ρσρσ = ρσ(ρ) = λ₁, and [λ₀, λ₁] = 1 gives σ(ρ)ρ²σ(ρ) = ρσ(ρ²)ρ, which is (4). The section is § 51 (« 5[1] », 1 written over 0), as in the author's table. Confidence: high. | new |

## Scan 34

| Kind | Note | Verdict |
|---|---|---|
| unproved claim | (6)–(7): λ_∞ = ρσρ⁻¹σρ = ρ(σ)σρ = −ρσ(ρ)⁻¹ρ = ρσρ⁻¹(σ), and the relation becomes [σ, λ_∞] = 1. | keep: the chain (6) checks with σ⁻¹ = −σ (own note below). The equivalence with the relation of scan 33 is not verified here. |
| unproved claim | NB: [ℓ₀,ℓ₁] = [λ₀,λ₁] = (σ(ρ)ρ⁻¹)³ and [σ,ℓ_∞] = (σ(ρ⁻¹)ρ)³ = int(σρ⁻¹)·[ℓ₀,ℓ₁]. | keep |
| unproved claim | 𝒢̲ is to be a group scheme over ℤ whose ℤ̂-points are « (à un isom. disons près) » the points of 𝒢^. | correct: the parenthesis now reads « à un isom. disons près » (uncertain), not « isom. \| disons ». It remains a qualification, not a hypothesis. |
| unproved claim | « faire opérer … à travers » (5): the action factors through 𝒢₃ × μ₂ ≃ 𝒢/M ≃ 𝒢_{0,3}/Π. | keep: the brace label is now \unsure{T_{0,3}\|Γ_{0,3}}. The intended comparison group is open. |
| unproved claim | Second (6)–(8): the actions σ, ρ, τ on λ̇₀, λ̇₁, λ̇_∞ with sum zero, « Ceci se voit d'abord pour i = 0, 1 ». | keep |
| own idea | Model the three generators modulo the diagonal and apply the printed permutations and the sign change. Confidence: high. | keep: the cyclic ρ (0→1→∞) and the transposition σ of 0,1 both preserve λ̇₀+λ̇₁+λ̇_∞ = 0, and so does τ: λ̇_i ↦ −λ̇_i. |
| **own (2nd pass)**, verification | ρ(σ)σρ = ρσρ⁻¹σρ and ρσρ⁻¹(σ) = ρσ·ρ⁻¹σρ agree directly. With σ⁻¹ = −σ, −ρσ(ρ)⁻¹ρ = −ρσρ⁻¹σ⁻¹ρ = ρσρ⁻¹σρ, so all four expressions in (6) are equal. Confidence: high. | new |

## Scan 35

| Kind | Note | Verdict |
|---|---|---|
| unproved claim | (11)–(12): « on aura un iso. canonique » 𝒢̲^Δ(S) ≃ 𝒢 ∧^M Γ(S, O_S ⊗ M), with an exact sequence. | keep |
| unproved claim | (13) 𝒢^ ≃ 𝒢̲^Δ(ℤ̂), « encore un fait général » for extensions with abelian kernel. | keep |
| unpursued implication | The diagonal restriction matters for a disconnected base, in particular Spec ℤ̂. | keep: ℤ̂ = ∏ ℤ_p has many idempotents, so Γ(H_S/S) (locally constant maps to H) is much larger than H for S = Spec ℤ̂. The diagonal is essential in (13). |
| own idea | Test (13) first on a split and then on a non-split extension of a finite group by ℤʳ. Confidence: medium. | keep |

## Scan 36

| Kind | Note | Verdict |
|---|---|---|
| unproved claim | Margin: « Je pense à la fin comparer les deux constructions possibles », the schematic and the profinite one. | keep |
| unproved claim | (15) d) « (automatique) u(𝒢^♮) ⊂ 𝒢^♮ ». | keep |
| unpursued implication | « ∃α », « ∃β » mean « l'existence locale »: a descent question for the automorphism functor. | keep |
| unproved claim | « u est déterminé par les valeurs » (16) u(ρ) = ξρ, u(σ) = ησ, with ξ, η ∈ ΓΠ̲. | keep: the margin now reads « M̲ \unsure{ss-gr.\|est gr.} d'indice 2 dans Π̲ ». The content (M̲ of index 2 in Π̲) is unchanged. |
| own idea | Describe the local conjugators as torsors under centralizers. Confidence: medium. | keep |

## Scan 37

| Kind | Note | Verdict |
|---|---|---|
| unproved claim | (17) c) « équation des lacets » ξ = η ℓ₁^ν with ν ∈ Γ𝔾_a and μ = 2ν+1 ∈ Γ𝔾_m. The meaning of the exponent needs explanation. | keep: ℓ₁ = ωλ₁ with λ₁ in the vector group M̲, so λ₁^ν = ν·λ₁ makes sense for ν ∈ Γ𝔾_a, while ω^ν needs ν mod 2. Scan 38 (20)–(21) addresses this. |
| unproved claim | « ρ et ρ⁻¹ ne sont conjugués sur aucune fibre », and likewise σ, σ⁻¹, so (18) is well defined. | keep |
| unpursued implication | Remarque: ωx ≠ −x, since ωx ∉ M and −x ∈ M. | keep |
| unpursued implication | (19)–(19 bis): ξ ∈ ΓM̲ always, and η ∈ Γ(ω^{ν₂(u)}·M̲). | keep: the group is M̲ (the M′ alternative is dropped). |
| own idea | Test the conjugacy claim in fibres of characteristic 2 and 3. Confidence: medium. | keep |
| **own (2nd pass)**, verification | With τ = στ′, τ′(ρ) = ρ⁻¹, τ′(σ) = σ⁻¹: τ(ρ)ρ⁻¹ = σρ⁻¹σ⁻¹ρ⁻¹ = (ρσρσ⁻¹)⁻¹ = λ₁⁻¹, and τ(σ)σ⁻¹ = σ⁻² = ω. These give the two second cases of (19): ξ = α₀λ₁⁻¹ρ(α₀)⁻¹ ∈ ΓM̲ and η = ωβ₀σ(β₀)⁻¹ ∈ ωM̲. Confidence: high. | new |

## Scan 38

| Kind | Note | Verdict |
|---|---|---|
| unproved claim | ν, ν′ are « morphismes de schémas bien définis » and μ, ε₂, ε₃ are homomorphisms of groups. | keep |
| unpursued implication | ν = 2ν′ + ν₂ in characteristic 2, where division by 2 is unavailable. | keep: ν₂ comes from the component condition (20), and ν′ needs ν − ν₂ ∈ 2·O(S), which is extra structure when 2 is not invertible. |
| unproved claim | The cancelled block (24)–(26) rewrites ℓ₁^ν with ℓ_i = a_iω. | keep: still cancelled, so no conclusion is endorsed. |
| unproved claim | Cancelled final paragraph: expand the a_i in λ₀, λ₁, λ_∞ (two of them for uniqueness). | keep |
| own idea | Compare the ν-decomposition and a_i-coordinates over ℤ, in characteristic 2, and with 2-torsion. Confidence: medium. | keep |
| **own (2nd pass)**, verification | (23) agrees with (21): 2ν+1 = 2(2ν′+ν₂)+1 = 4ν′+2ν₂+1. ε₂ = (−1)^{ν₂} matches (19 bis): η ∈ ωM̲ exactly when ε₂(u) = −1, that is, ν₂ = 1. The folio of this page reads 676 against the expected 667; this is an editorial point, not a research question. Confidence: high. | new |

# LM_P012 (scans 111–120): research notes, checked against the corrected text

The first pass's research notes R01–R27 are checked here against `LM_P012_checked.tex`. Each note gives its verdict (keep, correct or drop) with a reason, the note itself, and its scan and kind. "Unproved claim" means that these ten scans give no proof; it says nothing about the rest of the manuscript. The notes labelled **P** are the second pass's own.

## First-pass notes

**R01 — scan 111 — unproved claim — KEEP (minor correction).** Grothendieck says that the operation of Σ on π determines its action on the index set I, and hence "on récupère donc le K-schéma étale S" through S(K̄) ≃ (·) ∧_Σ Γ. The first factor is written over itself (I₀ or S̄₀). CSG reads S̄₀(K̄), which matches the identification I = S̄₀(K̄) on the previous page, so the claim does not depend on how the symbol is read. A proof needs the induced-set construction from the Σ-set I to a Γ-set.

**R02 — scan 111 — unproved claim — KEEP (corrected).** "Mais mieux, on récupère tout le diagramme Π_{D̄₀*} → [Π_{Ū₀} →] Π_Ū → Π_e" with the Σ-action, and from it a "diagramme des topos". The qualifier of "topos" is unresolved: the main line reads "des revêt.(?)", and a cancelled addition above it may read "classifiants". The claim covers the whole diagram with its equivariance data, not only the boundary set.

**R03 — scans 111–112 — unproved claim — KEEP (corrected).** Morphisms (X',S') → (X,S) "se décrivent simplement" by outer homomorphisms π' → π. These are compatible with Σ' ⊂ Σ and with the anabelian lacet structures. The compatibility is expressed by a Σ'-compatible map τ : I' ⊂ S̄'₀ → I = S̄₀ and by "un système d'entiers naturels (d_i)_{i∈I'}". The first pass had cancelled "⊂ S̄'₀" and read "une application d'entiers naturels"; both readings were wrong. The claim that these data suffice, and not merely follow, is unproved.

**R04 — scan 112 — unproved claim — KEEP (corrected).** For I = ∅ (S = ∅), the lacet structure is completed by a Kummer isomorphism κ : T^{⊗−1} ≃ H²(π,Ẑ), that is Ẑ ≃ H²(π,T), compatible with Σ. The bracket reads "en caractéristique p ≥ 0" (not "p > 0"): the restriction to l-adic components with l ≠ p is stated uniformly for every characteristic and is empty in characteristic 0. The equivariance of κ is asserted, not proved.

**R05 — scans 112–113 — unproved claim — KEEP (corrected).** The degree d (∈ ℕ) is "défini de façon unique par cette condition" (the commutative square), and the text also links it to "l'ordre de Coker f*" ("comme" or "ou aussi"; unresolved). Given the two identifications κ and κ', f* is multiplication by d on Ẑ, so Coker f* = Ẑ/dẐ has order d when d ≠ 0. That the index equals the geometric degree is not shown. On the direction "π → π'", see P02.

**R06 — scan 113 — conjecture — KEEP (corrected).** "Quand S(*?) = ∅, (S' ≠ ∅), il devrait y avoir encore […] une compatibilité pour les données kummériennes." The first pass had misread "kummériennes" as "harmoniciennes". The Kummer data have different natures on the two sides: lacets on π', and the purely cohomological κ on π. The required compatibility is announced, not formulated.

**R07 — scans 113–114 — question — KEEP (corrected).** "La question équivaut sans doute à celle de décrire une structure kummérienne “cohomologique” sur le groupe π̃'", where π̃' is obtained from π' by dividing out the lacets. Grothendieck adds that the question is the same in the topological and arithmetic settings ("il me faudra revenir dessus"). He also asks that π̃' → π̃ respect the lacet structure for a suitable degree. The first pass's sentence about the "uncertain adjective harmonicienne" is dropped: the word is "kummérienne".

**R08 — scan 114 — conjecture — CORRECT.** For pairs (X̄,S̄) defined over K̄, the datum is an outer group with T-lacets "muni d'une action (non de Γ mais des) noyau de groupe profini défini par Γ". The word is settled as "noyau", not "germe", and recurs in quotation marks as “noyau” on l. 19. The status of G stays open in the text: "(pro-fini ???)" and "(“discret” ???)". One must still decide which topology G and G → Γ carry.

**R09 — scan 114 — conjecture — KEEP (corrected).** G₀, the outer lacet automorphisms commuting with the action of the “noyau”, is "conjecturalement par la “conj. bordélique”" isomorphic to the finite group Aut_K̄(X̄,S̄). The epithet "bordélique" is legible. It refers to the manuscript's own earlier "conjecture bordélique" (CK witness: "Conjecture bordélique (7.1)", §7), not to an external result. Both a realisation statement and a faithfulness statement would be needed.

**R10 — scan 115 — conjecture — KEEP.** "La “restriction de (X̄,S̄) au corps K”" (the quotation covers the whole phrase) is expressed by a splitting Γ → G of G → Γ in 1 → G₀ → G → Γ. This is "on l'espère, de façon pleinement fidèle, si la conj. bordélique est valable". The hope covers morphisms, not only the existence of sections.

**R11 — scans 115–116 — unproved claim — CORRECT.** The relation ends in "= 0", and on these pages Grothendieck writes the trivial group as 0 ("π=0", "π≠0"), so this is his convention rather than an error. The bound "g=0, ν≤3" is in the ink, as in all the witnesses, but it is a slip (see P03). The freeness and rank claims of a) are standard consequences of the presentation and are not proved here.

**R12 — scan 116 — unproved claim — KEEP.** The canonical exact sequence 0 → T_π → ∏ L_i → π_ab → π̃_ab → 0 and the isomorphisms T_π → L_i hold under the added hypothesis "pour I ≠ ∅, π ≠ 0". The two margin notes treat the exception: π = 0 exactly when g = 0 and ν = 0 or 1, and otherwise the L_i are ≃ ℤ. Canonicity, meaning independence of the chosen representatives L_i, is taken up on scan 117.

**R13 — scan 116 — unproved claim — KEEP.** For I = ∅ and g ≠ 0, T_π is defined as H²(π,ℤ)^{⊗−1}. Grothendieck promises "on établira plus bas une relation entre les deux définitions de T_π"; the comparison is not on these pages.

**R14 — scan 116 — unpursued implication — KEEP (corrected).** "(donc g est uniquement déterminé par π et ν = card I." The phrase replaces the cancelled "la famille des ([L_i])": Grothendieck reduced the needed datum from the whole family to its cardinality. π alone does not determine (g,ν) when ν ≥ 1 (see R26).

**R15 — scan 117 — unproved claim — KEEP.** Apart from the abelian cases g = 0, ν = 1, 2, the conjugacy classes of the L_i are distinct. Every element normalising some L_i centralises it. The text calls this evident only for ν ≥ 2, where L_i → π_ab is injective. It follows that the members of one class are canonically isomorphic, which makes ∏ L_i and T_π → L_i intrinsic.

**R16 — scan 117 — open check — KEEP.** The margin note "voir à part le cas ν=1" points to the normaliser, in the free group on the x_α, y_α, of the subgroup generated by ∏[x_α,y_α]. It is a check left for later, not a proof.

**R17 — scans 117–118 — unproved claim — KEEP.** An action of Σ on the lacet structure induces an action on the invertible ℤ-module T_π, hence a character χ : Σ → ℤ* = {±1}. Conversely, one may speak of an action "compatible avec χ". The cancelled continuation about a T-structure à lacets ("et si Σ opère sur T (… χ) on dira qu'une action est compatible") is not a settled definition.

**R18 — scan 118 — conjecture — CORRECT.** The profinite variants are "(ou profinies premières à p, si p est premier donné…)": the prime-to-p variants are an alternative, not a special case. The first check, Norm_π(L_i) = Centr_π(L_i) = L_i, is qualified "dans le cas ν=1, sinon pas de pb", so the stated difficulty concerns only ν = 1. The discrete argument does not transfer automatically to the profinite case.

**R19 — scan 118 — conjecture — KEEP.** The second check is Centr(π) = (1) "(cas anabélien)", and more generally that the centraliser of every open subgroup of π is trivial. The margin says that this is not proved "pour le moment dans aucun cas anabélien profini !". This records the author's state of knowledge when he wrote; the second pass has not checked the present status.

**R20 — scan 119 — unproved claim — CORRECT.** "Par le topos|tapis d'Artin sur les ouverts du topos" (the noun is unresolved; the addition reads "du topos"), the constructible sheaves of sets on X that are locally constant on U correspond to triples (F_U, F_S, φ) with φ : F_S → j*i_*(F_U). This is Artin's gluing for an open-closed decomposition. The correspondence for all étale sheaves, constructibility apart, is asserted, not proved.

**R21 — scans 119–120 — unproved claim — KEEP.** The restriction is to F with F_U coming from the fundamental topos B_{Π₁(U)}, and "il n'y a pas lieu de supposer F_U à fibres finies". The admitted class must not be silently reduced to finite locally constant sheaves.

**R22 — scan 120 — unproved claim — KEEP (corrected).** The henselian disks D_s = Spec O_s ("disque en s") and D_s* = D_s − {s} = Spec K_s ("disque pointé") give the commutative diagram U ← D* → D → X with S (j₀) → D. The local hypothesis "dim_s S = 1" on scan 119 is in the ink but is inconsistent with S being discrete (see P04).

**R23 — scan 120 — unproved claim — CORRECT.** The sheaves on D are "“ess^t loc. constant”", that is essentiellement localement constants, not "ind loc. constant". The NB states that S → D induces an equivalence between "ces faisceaux" on D and the étale sheaves on S. For a henselian local ring this is the identification of the fundamental groups of the disk and of its closed point (see P05). The statement concerns only that class, not all étale sheaves on D.

**R24 — scan 120 — unproved claim — KEEP.** The gluing datum becomes F_D → σ_*ρ^*F_U ("ou encore", where the page ends). Comparing it with φ : F_S → j*i_*F_U needs base change and adjunction, and compatibility with morphisms of triples.

**R25 — scans 113, 116, 119–120 — first-pass model's idea — KEEP (clarified).** The idea is a relative cohomology of a group with its peripheral subgroups, to compare the kernel definition of T_π with the cohomological one. With the corrected reading "structure kummérienne “cohomologique”", this comparison is exactly the question Grothendieck poses on scan 113. It remains a research direction, not a result.

**R26 — scans 115–117 — first-pass model's idea — KEEP.** The types (0,3) and (1,1) both give a free π of rank 2g+ν−1 = 2. So π alone does not determine (g,ν), which agrees with "g est uniquement déterminé par π et ν = card I". The peripheral data must therefore be part of any reconstruction.

**R27 — scans 119–120 — first-pass model's idea — KEEP (minor correction).** The proposal is to express the local gluing datum through the punctured henselian disks, with F_D essentially locally constant ("ess^t", not "ind"). The page shows the start of this ("ou encore …"), and CSG continues with the description by the fundamental topoi B_{Π₁D*}, B_{Π₁U} and B_{Π₁D}. Finite fibres must not be assumed.

## Second-pass notes (own)

**P01 — scan 113 — Grothendieck's question (own note).** The corrected passage makes the problem explicit. When S = ∅ but S' ≠ ∅, a morphism must be compatible with the Kummer data even though one side has lacets (π') and the other only the cohomological κ (π). Grothendieck reduces this, "sans doute", to defining a cohomological Kummer structure on π̃' = π'/⟨⟨lacets⟩⟩, the "bouchage des trous" of the margin and the subject of §14. He leaves it open ("il me faudra revenir dessus").

**P02 — scans 112–113 — apparent slip (own note).** "que l'hom π → π' induit un diagramme commutatif": the morphism of pairs gives π' → π (scan 112, l. 1), and f* : H²(π,T) → H²(π',T) is the map induced contravariantly by π' → π. "π → π'" is therefore apparently a slip for π' → π. The first pass and IUT keep "π → π'".

**P03 — scan 116 — error in the manuscript (own check).** For ν ≥ 1, π is free of rank 2g+ν−1 and so abelian iff g = 0 and ν ≤ 2. For ν = 0 it is abelian iff g ≤ 1 (trivial or ℤ²). The bracket "π ≃ π_{g,ν} est abélien ssi g=0, ν≤3 ou g=1, ν≤0" should therefore read "ν≤2": π_{0,3} is free of rank 2. The corrected bound agrees with a) "sauf si g=0, ν≤2" and with the exclusion "g=0, ν≤2" on scan 117. All the witnesses reproduce "ν ≤ 3".

**P04 — scan 119 — slip in a hypothesis (own check).** As written, "S un sous-schéma fermé réduit discret tel que ∀s∈S, dim_s S = 1" is contradictory, since a discrete S has dim_s S = 0. The consequence drawn, "(donc S défini par une partie fermée discrète de X)", suggests that the intended condition is dim O_{X,s} = 1 (codimension 1 in X), which with dim X = 1 makes S discrete. The later addition "réduit discret" makes the condition redundant in any case.

**P05 — scan 120 — claim without proof, standard argument (own note).** The NB "l'inclusion S → D définit une équivalence" for essentially locally constant sheaves is the henselian property. For O_s henselian, the finite étale covers of D_s are those of the closed point, so π₁(D_s) ≅ π₁(s) and the locally constant sheaves agree. "ess^t loc. constant" is not defined on this page. CSG's continuation identifies these sheaves with the objects of the fundamental (multigaloisian) topoi.

**P06 — scan 114 — interpretation (own idea, low confidence).** "(non de Γ mais des) noyau de groupe profini défini par Γ": a pair (X̄,S̄) over K̄ is defined over some finite extension, so only open subgroups of Γ act, and only up to shrinking. The quoted word “noyau” seems to be a provisional name for this system of open subgroups, and G → Γ has open image. That would explain why Grothendieck hesitates over whether G is "pro-fini ???" or "discret ???".

**P07 — scan 115 — possible cancellation (own observation).** In the definition of a lacet structure, "∀i∈I" before "un L_i ∈ [L_i]" may be cancelled (a stroke through "∈ I" and an overwritten ∀). If so, the quantifier over i must be read from the context ("un L_i ∈ [L_i], un générateur l_i ∈ L_i"). The mathematics does not change, because a representative L_i and a generator l_i are chosen for every i in any case.

**P08 — scan 118 — status of the two checks (own note).** The two profinite checks have different scopes. The first, Norm = Centr = L_i, is said to be a problem only for ν = 1. The second asks for trivial centralisers of all open subgroups, which is much stronger than a trivial centre. The margin's "dans aucun cas anabélien profini" applies to the whole list. The second pass has not checked which of these statements were later proved, or by whom.

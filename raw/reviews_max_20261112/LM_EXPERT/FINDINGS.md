# La Longue Marche expert line: running list of findings and implications

Kept by the LM field expert (section 1: Claude Fable 5.2, effort max, 12 Nov 2026, after reading Part I, cote 140-2,
in full). Every entry says what it is, where in Grothendieck's text it bears (cote:scan), on what it rests, and how
far it is checked. "From memory" means: stated from the expert's knowledge of the literature, the source not yet
re-read in this line; such entries must be confirmed against the primary text before they are used in a review or a
prompt as settled. Entries are numbered F1, F2, ... and never renumbered.

## A. Results proved here (to be checked by GPT-6 Astra, effort Pro)

**F1. Uniqueness in Nielsen realization, by Teichmüller's uniqueness theorem (answers the second half of 2:sc102).**
Grothendieck asks (2:sc101–102, p. 49') whether every finite Σ ⊂ 𝒯_{g,ν} = A/A^0 lifts to A = Homeo(U_{g,ν}) and
"si deux tels relèvements sont conjugués par un a ∈ A^0". Existence is Kerckhoff's theorem (1983; from memory).
Uniqueness: let S be of type (g,ν) with 2g+ν ≥ 3, G finite, ρ_1, ρ_2: G → Homeo(S) two actions with the same image in
the (extended) mapping class group, [ρ_1(g)] = [ρ_2(g)] for all g.
*Claim.* There is h ∈ Homeo_0(S) with ρ_2(g) = h ρ_1(g) h^{-1} for all g.
*Proof.* (i) Each ρ_i leaves invariant a conformal structure c_i of finite type on S (a finite group action on a
surface is locally linear, by the Kerékjártó–Eilenberg theorem that Grothendieck's "lemme fondamental" 2:sc141–148
reproves; so S/ρ_i(G) is a surface with boundary and cone points, and a conformal structure of the quotient orbifold
pulls back; orientation-reversing elements act anti-conformally). (ii) By Teichmüller's theorem there is a unique
extremal quasiconformal map h: (S,c_1) → (S,c_2) in the isotopy class of the identity (existence and uniqueness for
finite-type hyperbolic surfaces). (iii) For g ∈ G the map h_g := ρ_2(g)^{-1} ∘ h ∘ ρ_1(g): (S,c_1) → (S,c_2) is
again quasiconformal with the same maximal dilatation as h, because ρ_1(g), ρ_2(g) are conformal or anti-conformal
automorphisms of c_1, c_2 (both of the same kind, since they have the same mapping class); its isotopy class is
[g]^{-1}·1·[g] = 1. By uniqueness h_g = h, i.e. h ρ_1(g) = ρ_2(g) h. ∎
Status: proved here modulo the three cited classical facts (local linearity of finite group actions on surfaces;
existence of a G-invariant conformal structure of finite type; Teichmüller's uniqueness theorem with punctures).
Consequence: in his list of fidelities (2:sc279–280) the "2-fidélité" holds for A = A_{g,ν}, 2g+ν ≥ 3.

**F2. His classification conjecture for finite group actions (2:sc270–271) is a theorem obtained by assembling
classical results.** With A = Homeo(U_{g,ν}), 2g+ν ≥ 3, Γ finite, u: Γ → A: his four conditions (2:sc279–280) are
3-fidelity = every Γ → π_0(A) lifts = Kerckhoff 1983; 2-fidelity = F1; 1-fidelity = (A^0)^u connected = the
Birman–Hilden property for finite group actions on hyperbolic surfaces (Birman–Hilden 1973, MacLachlan–Harvey 1975:
a fibre-preserving homeomorphism isotopic to the identity is so through fibre-preserving ones); 0-fidelity =
π_1((A^0)^u) = 0 = contractibility of the identity component of the homeomorphism group of the punctured quotient
surface V' (Hamstrom; Earle–Eells; Earle–Schatz), since the identity component of Homeo(U)^Γ maps isomorphically
onto Homeo_0(U/Γ rel branch points) (the kernel Z(Γ) of Homeo(U)^Γ → Homeo(U/Γ) meets the identity component
trivially). His §24 computation (identity component of Aut(U)^{0Γ} ≃ Aut(V')^0; π_0 ⊂ π_1(Mon(S^!,U))^Γ) is the same
statement; the "relation" he wants, H^0(Γ, π_1(Mon(S^!,U))) = 1, follows from Birman–Hilden. Status: assembled from
memory of the four sources; each must be pinned down (exact hypotheses: punctures, orientation-reversing elements,
topological versus smooth category) before it is called settled. Bears on: LM4 (the prompt must use these, not ask
for them as open), 2:sc102, 2:sc270–294.

## B. Identifications with the later literature (to confirm on the primary texts)

**F3. The normalizer groups of §§25bis–27 are the Drinfeld–Ihara groups GT_0 and GT (from memory; to confirm).**
For (0,3): Γ'_{0,3} := centralizer of S_3 = 𝒯^+_{0,3} in 𝒯̂̂^!_{0,3} ⊂ Autext_lac(Π̂_{0,3}) (2:sc315, 2:sc342) is the group of
inertia-preserving outer automorphisms of F̂_2 = π̂_1(M_{0,4}) commuting with S_3, i.e. Out^♯_4 of Harbater–Schneps
(Trans. AMS 352 (2000)) = GT_0 (pairs (λ,f) with the 2-cycle and 3-cycle relations, no pentagon). For (0,4): an
element of N^!(𝒯̂^+_{0,4}) normalizes 𝒯̂^{!+}_{0,4} = π̂_1(M_{0,4}) inside Out(π̂_{0,4}), hence acts on its preimage in
Aut(π̂_{0,4}), which is π̂_1(M_{0,5}); so Γ'_{0,4} maps to the S_5-commuting, fibration- and inertia-preserving outer
automorphisms of π̂_1(M_{0,5}), which is GT (Harbater–Schneps: Out^♯_5 = GT = Out^♯_n for n ≥ 5). Consequences:
(a) Grothendieck's "hasty" corollary Γ_{0,ν} ≃ Γ_{0,3} for all ν ≥ 3 (2:sc349), read with the normalizer definitions,
fails exactly at the step (0,4) → (0,3) unless GT = GT_0, and holds from ν = 4 on: this is the two-level principle
of the Esquisse (M_{0,4}, M_{0,5}) seen inside the Longue Marche. (b) His own retraction (2:sc349 NB; §29, 2:sc367–370:
the Galois image must lie in the subgroup H normalizing the fibre subgroups π'_i ↪ 𝒯̂^{!+}) is the pentagon in
disguise: condition (e) of §32 (2:sc396) at the level (0,5)/(0,4). (c) His conjecture (27) for (0,3) with the
normalizer definition says Γ_Q = GT_0, with ν ≥ 4 it says Γ_Q = GT. To confirm: the exact match of "lacets"
(he allows permutation of the classes and a common multiplier χ ∈ Ẑ^*) with "inertia-preserving", and whether
GT ≠ GT_0 is proved in the profinite setting.

**F4. His admitted injectivity 𝔖̂_{g,ν} → 𝔖̂̂_{g,ν} (2:sc320; equivalently 𝒯̂_{g,ν} ↪ 𝒯̂̂_{g,ν} = Out(π̂_{g,ν})) is the congruence
subgroup property for mapping class groups** (from memory: true in genus 0 and 1 (Asada 2001), genus 2 (Boggi;
Hoshi–Iijima); open for g ≥ 3 as far as known to me; 2026 status to search). §36 uses the case (1,1):
SL(2,Z)^ ↪ Out(F̂_2). Bears on LM3/LM3b and on every statement that treats 𝒯̂_{g,ν} as a subgroup of 𝒯̂̂_{g,ν}.

**F5. The profinite statements he could not prove (2:sc118 "pas démontré dans aucun cas anabélien profini";
2:sc496 "je cale sur a)"; 2:sc500 (2), (4) "pas prouvé")**: centre-freeness of profinite surface groups and of their
open subgroups, torsion-freeness, self-normalization of loop (inertia) subgroups L_i = N_π(L_i) = Centr_π(L_i^n):
all standard now (from memory: free profinite groups of rank ≥ 2 have trivial centre (Ribes–Zalesskii); profinite
surface groups: Anderson 1974, Nakamura 1994, Mochizuki–Tamagawa 2008 for the inertia statements). With them his
§35 Théorème 1 (injectivity of Γ_Q → Out(Π̂_{0,3}), by Belyi) and Lemme 5 are complete proofs.

**F6. §34: the loop structure is determined by the Galois action (2:sc483)**: from memory this is Nakamura's weight
characterization of inertia subgroups (J. reine angew. Math. 411 (1990) for genus 0; later general) and the
Hom-form with open image is Mochizuki's Theorem A (Invent. Math. 138 (1999), sub-p-adic fields); "le commutant de
Γ_{0,3} dans 𝒯̂̂_{0,3} est réduit à S_3" (2:sc485) follows from the Isom-form for P^1∖{0,1,∞} over Q. So the
"description heuristique" of §34 is, for morphisms, a theorem; what stays conjectural there is the essential image
for *points* (sections).

**F7. Sections (§8 case III, §9, §14bis, §32, §34)**: his corrected conjecture (2:sc79) is the section conjecture with
cuspidal sections; his "famille transcendante" at a cusp, a torsor under H^1(K, T(G_m)) = lim K^*/n containing the
K^*-torsor of tangential sections (2:sc77–79), is the standard description of cuspidal sections. Injectivity by
Mordell–Weil (2:sc64) is the standard argument. Claimed recently (OpenAI family 019, 6 Oct 2026, unrefereed, no
formal proof): the local p-adic section conjecture for smooth proper curves of genus ≥ 2 over finite extensions of
Q_p (Theorem 1.1 there), and the global conjecture when the finite-descent locus equals the rational points
(X_0(N), X_1(N) of genus ≥ 2 over Q). Not covered by 019: affine curves (his cuspidal packets), general number
fields, and his relative version over a base S (2:sc433–436), where he observes that non-disjoint sections break
surjectivity.

**F8. (f) of §32 (2:sc396–398: the kernels of Θ_{g,ν}: Γ_Q → Γ_{g,ν} do not depend on ν; "il ne serait pas impossible
que (f) soit faux")**: from memory all Θ_{g,ν} are injective: Belyi for g = 0; Matsumoto 1996 (affine curves),
Hoshi–Mochizuki 2011 (all hyperbolic curves over number fields) for the faithfulness of the outer Galois action,
hence on π_1 of the moduli stacks. His finer question (2:sc505: is Γ_Q → Out(Π̂_{1,1}) modulo 𝒯̂^+_{1,1} injective) he
answers himself in §36.

**F9. §31 (2:sc393): (a) splittings of the discrete extension E versus its completion Ê, (b) π̂^G = 1.** From memory:
for a Fuchsian group E every finite subgroup of Ê is conjugate to a finite subgroup of E, with the right count of
conjugacy classes (Bridson–Conder–Reid 2016). (b) should follow from the same circle (centralizers of torsion in
profinite completions of good groups). To confirm; if confirmed, §31's two "conjectures sans vergogne" are known for
orientation-preserving actions, and the LM4 prompt should ask for the orientation-reversing and loop-structure
refinements instead.

**F10. μ_E (2:sc155–160: is the rotation-number map on torsion elements intrinsic in the extension E?)**: for
isomorphisms of extensions preserving the loop structure, yes (from memory: automorphisms of finitely generated
Fuchsian groups preserving the peripheral structure are geometric, Zieschang–Vogt–Coldewey; an orientation-preserving
homeomorphism preserves rotation numbers, an orientation-reversing one inverts them, as his T-twist predicts). Also
a corollary of F1/F2. His abelian counterexample (elliptic curve, the choice of one eigenvalue) stands.

**F11. Corrections to §33.** (a) The count of conjugacy classes of anti-involutions of X_g: his margins already
correct the first statement (g+1 classes) by adding the doubles of orientable surfaces with boundary; the total is
(g+1) + ⌊(g+2)/2⌋ = ⌊(3g+4)/2⌋ (classes with k fixed circles and non-orientable quotient, 0 ≤ k ≤ g; orientable
quotient, 1 ≤ k ≤ g+1, k ≡ g+1 mod 2). Checked here by his own Euler characteristic formulas (g = γ+μ and
g = 2γ+μ−1); it is the classical Weichold–Klein classification of real curves. (b) H = ⟨ρ_j⟩ ≃ Z^g (2:sc454–470): each
ρ_j is the Dehn twist about the core circle of T_j (the rotation angle in (29) runs from 0 to 2π across the tube),
and the g circles form a cut system. H is not a maximal free abelian subgroup for g ≥ 2 (from memory: the maximal
rank is 3g−3, Birman–Lubotzky–McCarthy 1983); its normalizer is the stabilizer of the multicurve. His "tore
maximal" analogy is the curve-complex/Tits-building analogy of Harvey.

**F12. §37 constants.** a = 6: j(λ) = 2^8 (λ^2−λ+1)^3 / (λ^2(λ−1)^2), critical value 1728 = 2^6·3^3 (classical; his b = 3
is right; he leaves a undetermined, 2:sc564–565).

## C. Structural observations on the manuscript

**F13. Three successive definitions of "Γ_{g,ν}".** (i) §19: Γ_{g,ν} = π_0(Aut(U_{g,ν})), the discrete (extended)
mapping class group; renamed 𝒯_{g,ν} at 2:sc314. (ii) §25bis–§28: bold Γ_{g,ν} = Norm_{𝒯̂̂}(𝒯̂^+)/𝒯̂^+ (purely
group-theoretic; F3). (iii) from §29 (2:sc371): bold Γ_{g,ν} = N_{g,ν}/𝒯̂^+ with N_{g,ν} the image of π_1(M_{g,ν,Q}) (a
quotient of Γ_Q by construction; (ii) is then written Γ'_{g,ν}). A statement about "Γ_{g,ν}" is ambiguous unless the
scan is given; reviews and prompts must say which. With (iii), "Γ_Q ≃ Γ_{g,ν}" is faithfulness (F8); with (ii) it is
the GT-type question (F3).

**F14. The Teichmüller tower of the Esquisse appears in Part I as**: the tower (84) of Teichmüller spaces
(2:sc260); the fundamental exact sequences (9), (10) of §32 (2:sc399); the "structure simpliciale d'extensions
successives" and "structure à l'infini" of π_1(M_{g,ν}) (2:sc370); the correspondences of §28 and second §33
(finite coverings, change of genus); and the reduction of everything to (0,3) through Belyi (2:sc481–482, 2:sc484).
The dessins ("cartes") enter in §36–37 (Π'_{0,3}, the cartographic group; regular triangulated polyhedra and
M_{1,1}[n], n = 2,3,4,5).

## D. Compared with the earlier review

(To be written only after this line's own LM3 and LM3b reviews are complete; see the handoff, addition G.)

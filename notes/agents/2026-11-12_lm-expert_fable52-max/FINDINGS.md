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

## E. Confirmations and corrections of F1-F14 against the primary texts (successor line, 12 Nov 2026)

Written 12 Nov 2026, 14:08 UTC (clock read) by fork D of the successor (Claude Fable 5.2, effort max) from the
forks' notes `work\lit\LIT_LM4_surfaces.md` (fork A), `LIT_LM6_sections.md` (fork B1), `LIT_LM6_anabelian.md`
(fork B2) and from the texts the main agent read before 13:55 UTC (F3, F4). All four readers: Claude Fable 5.2,
effort max. Local copies: `C:\Users\user\Documents\Free or receipted\free\lm-expert-20261112\<folder>\`. "Through
X" = only X, which quotes the theorem, was read. Sections A-D above are unchanged; where an entry below corrects one,
the entry below holds.

| Entry | Result | Exact citation (folder of the copy read) | Read by |
|---|---|---|---|
| F1 | Confirmed; **not new**. The proof holds after one amendment: step (i) needs local linearity of the finite stabilizer *groups*, not only of single periodic maps. No anti-conformal form of Teichmüller's theorem is needed (the map `ρ_2(g)^{-1} h ρ_1(g)` is orientation preserving). | Classical for closed surfaces and orientation-preserving groups: Harvey, *On branch loci in Teichmüller space*, Trans. AMS 153 (1971), Thm 2, Cor. 3 (`harvey-1971-branch-loci`); MacLachlan–Harvey, Proc. LMS 30 (1975) (through Margalit–Winarski). The three facts: Constantin–Kolev, Enseign. Math. 40 (1994), Lemma 2.5, Thm 3.1 (`constantin-kolev-kerekjarto`), and Kolev, Enseign. Math. 52 (2006) for groups (`kolev-compact-subgroups-sphere`); Bers, Bull. AMS 5 (1981), §3 (D), type (p, n) (`bers-1981-finite-dim-teichmuller`). | fork A |
| F2 | 3-fidelity: confirmed for ν = 0, orientation-reversing classes included; ν > 0 still from memory. 2-fidelity = F1. 1-fidelity: confirmed for orientation-preserving Γ; the theorem is MacLachlan–Harvey's (Birman–Hilden's own needs the cover unbranched or solvable); reflections are not covered by the quoted statements. 0-fidelity: confirmed; the homeomorphism theorem is Hamstrom's and Scott's, not Earle–Eells's. | Kerckhoff, Bull. AMS 2 (1980), Thm 1, 2 (`kerckhoff-1980-announcement`; Ann. of Math. 117 (1983) not obtained); Margalit–Winarski, arXiv:1703.03448, Thm 2.1, 2.2, Prop. 3.1 (`margalit-winarski-birman-hilden`); Yagasaki, arXiv:math/0010223, Lemma 2.1, Thm 1.1 (`yagasaki-homeo-noncompact-surfaces`); Earle–Eells, Bull. AMS 73 (1967), Thm 1 (`earle-eells-1967-announcement`). | fork A |
| F3 | Confirmed for (0,3): the centralizer of `S_3` in the loop-preserving outer automorphisms of `F̂_2` is `Out^♯_4 ≅ GT_0`. **Notation corrected**: "GT_0" (pairs satisfying (I), (II)) is the notation of Lochak–Schneps and Harbater–Schneps, not Drinfeld's; in Drinfeld `GT_0(k)` is the set of pairs with `λ = 0`. For (0,ν), ν ≥ 5: `Out^♯_ν ≅ GT` (Harbater–Schneps), and with no inertia condition `Out(π̂_1(M_{0,ν})) = GT × S_ν` (Hoshi–Minamide–Mochizuki). The identification of his normalizer groups `Γ'_{0,ν}` with these, and the case (0,4), are for the LM3 review. Not found in the texts read: a proof that `GT ≠ GT_0` for the profinite groups. | Drinfeld, Algebra i Analiz 2:4 (1990) 149–181, §4 (`drinfeld-1990-gt\aa199.pdf`, pp. 164–167): equations (4.3) `f(Y,X) = f(X,Y)^{-1}`, (4.4) `f(X_3,X_1)X_3^m f(X_2,X_3)X_2^m f(X_1,X_2)X_1^m = 1` for `X_1X_2X_3 = 1`, `m = (λ−1)/2`, (4.10) the pentagon in `K_4`; the semigroup of endomorphisms of the profinite completion of `B_3`/centre that keep the subgroup generated by `σ_1` and act trivially on `S_3` is anti-isomorphic to the pairs satisfying (4.3), (4.4); "GT is the automorphism group of the tower of the `T̂_{0,ν}`", (4.10) being necessary and sufficient for extension from `T̂_{0,4}` to `T̂_{0,5}`; injectivity of `Gal(Q̄/Q) → GT` by Belyi. Harbater–Schneps, Trans. AMS 352 (2000), Main Theorem, Theorem A (`harbater-schneps-2000`). Hoshi–Minamide–Mochizuki, RIMS-1870 (Kodai Math. J. 45 (2022)), Cor. B, C (`hoshi-minamide-mochizuki-rims1870`). Minamide–Nakamura, arXiv:1904.06749, Thm A, B, 1.1, Cor. C (`minamide-nakamura-1904.06749`). | main agent |
| F4 | Confirmed and made exact: the congruence subgroup property is known for genus ≤ 2 and only there. "Hoshi–Iijima" in F4 was not read. No 2026 claim for genus ≥ 3 found (arXiv searches of 12 Nov). The property for type (g, r) is equivalent to injectivity of the universal monodromy representation (Hoshi–Mochizuki, Cor. 6.5). | Boggi, arXiv:2408.12486v2, §1.1 ("known to have a positive answer for g(S) ≤ 2", citing Asada, JPAA 159 (2001); Boggi, Hiroshima Math. J. 39 (2009); Boggi, J. Algebra 546 (2020)) (`boggi-2408.12486`); Boggi, arXiv:2011.15075v6, §2.3 ("known to be true only for g(S) ≤ 2") (`boggi-2011.15075`); Hoshi–Mochizuki, Hiroshima Math. J. 41 (2011), Cor. 6.5 (`hoshi-mochizuki-nodnon`). | main agent; fork B2 |
| F5 | Confirmed statement by statement; attribution corrected. Centre trivial: Nakamura 1994, Cor. (1.3.4) (for `F̂_2` already Belyi 1979, Lemma 1 and Corollary). Centralizer of open subgroups trivial: Mochizuki 2004, Lemma 1.3.1; Mochizuki–Tamagawa, Prop. 1.4. No torsion: Mochizuki–Tamagawa, Remarks 1.2.2, 1.1.5. `N_π(L_i) = L_i` for every ν ≥ 1 and `Centr_π(L_i^n) = L_i`: Mochizuki 2004, Lemma 1.3.7. Distinct classes not commensurable: Mochizuki 2007, Prop. 1.2. (2) of 2:sc500 and (4) of 2:sc501 for ν ≥ 1: Nakamura 1994, Lemma (2.1.2). **(4) for ν = 0: no theorem found**; not needed, since Lemme 5 of §35 follows from slimness alone (F20). | Nakamura, J. Math. Sci. Univ. Tokyo 1 (1994) (`nakamura-1994-profinite-calculus`); Mochizuki, *The absolute anabelian geometry of hyperbolic curves* (2004) (`mochizuki-absolute-anabelian`); Mochizuki–Tamagawa, Hokkaido Math. J. 37 (2008) (`mochizuki-tamagawa-config`); Mochizuki, Tohoku Math. J. 59 (2007) (`mochizuki-combgc`); Belyi, Izv. AN SSSR 43 (1979) (`belyi-1979`). | fork B2 |
| F6 | **Corrected.** The loop structure from the Galois action is Nakamura's theorem for elements with a *cyclotomic normalizer* (any genus, affine, number fields); his wording of 2:sc483 is false as written (F17). Hom-form with open image: confirmed. Commutant of the Galois image = `S_3`: confirmed, a stated corollary. | Nakamura 1994, Thm (2.1.1) (Crelle 411 (1990) not obtained); Mochizuki, Invent. Math. 138 (1999), Thm A (`mochizuki-local-pro-p`); Tamagawa, Compositio Math. 109 (1997), Thm (0.3), Remark (7.3)(i) (`tamagawa-1997-affine`); Mochizuki 2004, Thm 1.3.4. | fork B2 |
| F7 | Confirmed, with four corrections: F15, F16, and: the affine local statement with packets follows from 019 (F24); over number fields 019 gives an equivalence (F24). | Grothendieck, letter to Faltings, 27 June 1983, pp. 52, 54, 56–58 (`grothendieck-faltings-1983`); Stix, arXiv:0809.0017, Prop. 8, Thm 14, 17, 45 (`stix-cuspidal`); Esnault–Hai, arXiv:math/0703877, Thm 5.1, Prop. 5.3, Thm 5.5, 6.5, Cor. 6.9 (`esnault-hai`); Deligne 1989, §15.13–15.26 (`deligne-1989`); 019 read in full (`work\papers2\019_main.txt`). | fork B1 |
| F8 | Confirmed with the exact source: every `Θ_{g,ν}` is injective, ordered or unordered points (F21). Faithfulness for every hyperbolic curve over number fields and p-adic fields: Hoshi–Mochizuki, Thm C (affine case: Matsumoto 1996, through Mochizuki 2004, Thm 1.3.6). | Hoshi–Mochizuki 2011, Thm C, Cor. 6.4 (`hoshi-mochizuki-nodnon`); Matsumoto, Crelle 474 (1996) and Matsumoto–Tamagawa, Amer. J. Math. 122 (2000) not obtained. | fork B2 |
| F9 | (a) confirmed for `G = G⁺`, with a short argument passing from `Ê`-conjugacy to `π`-conjugacy. (b) **corrected**: `π̂^G = 1` is not in Bridson–Conder–Reid; it follows from the centralizer condition (cocompact case read; free case from memory, Herfort–Ribes). Open in the texts read: groups with reflections, dihedral subgroups. | Bridson–Conder–Reid, arXiv:1401.3645, Thm 5.1, Cor. 5.2, 5.3 (`bridson-conder-reid`); Minasyan–Zalesskii, arXiv:1504.00613, Thm 1.1, Cor. 3.5 (`minasyan-zalesskii-vcsh-conjugacy`); Minasyan, arXiv:0905.1282, Prop. 3.2 (`minasyan-hcs-raag`). | fork A |
| F10 | Confirmed as a corollary of F1; the formula for μ on closed surfaces is Harvey's Theorem 7. "Zieschang–Vogt–Coldewey" stays from memory and is not needed. | Harvey 1971, §3, Thm 7. | fork A |
| F11 | (a) confirmed: `(g+1) + ⌊(g+2)/2⌋ = ⌊(3g+4)/2⌋`. (b) confirmed: rank `3g − 3 + p`; `H` is not maximal for `g ≥ 2`. | Gross–Harris, Ann. Sci. ENS 14 (1981), Prop. 3.1 (`gross-harris-real-curves`); Birman–Lubotzky–McCarthy through Behrstock–Minsky, arXiv:math/0512352 (`behrstock-minsky-rank`). | fork A |
| F12 | Not checked in this pass (classical formula; no source read). | — | — |
| F13, F14 | Observations on the manuscript; no literature involved; unchanged. | — | — |

**F15. Injectivity of points → splittings (2:sc64; letter to Faltings, p. 52): the reason he gives is false, the
statement is true.** "`G(K)` de type fini" fails as soon as the generalized Jacobian has a non-trivial torus (`K^×`
is not finitely generated); the true input is that `G(K)` has no non-trivial divisible element (Esnault–Hai,
Prop. 5.3; Stix, Thm 45, Remark 46). His excluded cases are `g = 0` with `ν ≤ 1`. Source: fork B1, Part 2 items 1, 3.
Checked: both cited statements read; the divisibility argument for semi-abelian `G` is sketched there, not written out.

**F16. 2:sc79: packets of distinct cusps are not distinct in the extension by `π_ab` when `g = 0`.** On
`P¹ ∖ {0,1,∞}` the abelianized class of a point `x` is `(x, 1−x)`, the packet at `0` is `{(a, 1)}`, at `1` is
`{(1, b)}`, and the tangential classes "0 towards 1" and "1 towards 0" both give `(1, 1)`. True for `g ≥ 1`; inside
one packet the abelianized classes all coincide when `ν = 1`. In the full group the statement is Stix's Thm 14.
Source: fork B1's own computation (Part 2 item 2); not checked by a second reader; asked of GPT-6 Astra in LM6 B (a).

**F17. 2:sc483 is false as written.** "The `L_i` are the maximal subgroups of `π` whose normalizer in `E` has open
image in `Γ`": `π` itself, every open subgroup of `π` normal in `E`, and the closure of `[π, π]` have the property.
True: Nakamura 1994, Thm (2.1.1) (a non-trivial element lies in an inertia group iff it has a cyclotomic
normalizer). Open: whether the cyclotomic condition can be dropped for procyclic subgroups (CM factors give
weight −1 lines); uniqueness of the invariant loop structure (one step not in the literature read). Over finite
extensions of `Q_p` that proof is not available (Tate curves). Source: fork B2, 2.3; fork B1, (iii).

**F18. Over R every class of sections comes from a component of `U(R)`; a real cusp carries a packet of two
classes, those of its two adjacent components.** So "π_0(U(R)) ≅ non-cuspidal sections" (H7 as written, and the v1
Part C (a) of LM6) is false. His §33 theorem with centralizers is Mochizuki 2003, Thm 3.6, Cor. 3.7; the profinite
bijection for all hyperbolic real curves is Cor. 3.13 and Bresciani–Vistoli. Not found: the profinite centralizers
for curves. Source: fork B1, Part 2 item 5 (`mochizuki-topics`, `bresciani-vistoli`, `stix-period-index`).

**F19. Belyi 1979 already contains what §35 lacks.** Lemma 1 and its Corollary: `c(F, F) = 1` for the free
profinite group on two generators (the centre statement on which he "cale", 2:sc496); the lift of `G_Q` to
`A = {x ↦ x^α, y ↦ u^{-1} y^α u, (xy) ∼ (xy)^α, u ∈ F'} ⊂ Aut F` with `A ∩ Int F = 1`; injectivity; and the closing
question, to describe the image group-theoretically. Source: fork B2, 0.1 (`belyi-1979`, page images, its translation).

**F20. Lemme 5 and Corollaire 2 of §35 (2:sc498–501) follow from slimness alone**; (2), (4) of 2:sc500–501 are not
needed. Proof (three lines) in `LIT_LM6_anabelian.md`, 0.3. So §35 is complete as it stands, given Mochizuki 2004,
Lemma 1.3.1.

**F21. (f) of §32 (2:sc396–398).** All `Θ_{g,ν}: Γ_Q → Γ_{g,ν}` (definition (iii) of F13) are injective, for every
type with `2g − 2 + ν > 0` (Hoshi–Mochizuki, Cor. 6.4; derivation in `LIT_LM6_anabelian.md`, 0.4), so his doubt is
removed and the stronger faithfulness of the Remarque of §35 holds for all types. What is not settled is his
isomorphism (6) `N^!_{g,ν} ≅ M^!_{g,ν−1}`: it is equivalent to a comparison of congruence kernels (Cor. 6.5), i.e. to
F4; his reduction of (6) to "same kernel" silently uses the congruence subgroup property.

**F22. The lemma he leaves at 2:sc146–147 is false as written**: `u(z) = z̄` has order 2, commutes with `z ↦ z+1`
and fixes 0. With "orientation preserving" it follows from Constantin–Kolev, Cor. 4.2; the whole "lemme
fondamental" for topological actions follows from Kolev's theorem. Source: fork A, section 1.

**F23. Where his statements sit in the later literature (dates).** §33 theorem (π_0(U^σ) ≅ classes of splittings,
with centralizers): Mochizuki 2003. (III) of 2:sc292 for ν = 0: Eckmann–Müller 1980, Cor. 2 (the route through
realization was not available in 1981: Zieschang's 1971 footnote). The contractibility theorem of 2:sc215:
Earle–Eells 1967 state that their result confirms a conjecture of Grothendieck (Séminaire Cartan 1960/61, exposé 7).
His §9 construction is Deligne's tangential base point (1989, §15). Sources: forks A, B1.

**F24. What 019 gives beyond its statement (claims, conditional on 019; derivations of fork B1, section 1.C).**
(T1) For every hyperbolic `U` over a finite extension `k` of `Q_p`: `U(k) ⊔ ⊔_{y ∈ S(k)} (packet at y) →` classes
of sections is bijective, by the neighbourhood argument; this is his corrected conjecture of 2:sc79 with `K`
replaced by `k`. (T2) For proper `C` of genus ≥ 2 over a number field: the section conjecture for `C` ⇔
`C(A_K)_•^{f-cov} = C(K)`. Fork B1 followed 019 line by line and found no gap; the deep external input is
Mochizuki–Tsujimura's resolution of nonsingularities (RIMS-1974, unrefereed).

**F25. An absolute Hom-form for hyperbolic curves over number fields would follow from 031 and Mochizuki's
Theorem A** (dominant morphisms of schemes ↔ open homomorphisms of `π_1` up to inner automorphisms). Derivation of
fork B2 (`LIT_LM6_anabelian.md`, 1.2 (c)); unchecked; asked in LM6 A (b).

**F26. Fermat (2:sc65).** Steklov (arXiv:2602.17746, Thm A): all Selmer sections over `Q` of the affine Fermat
curve of exponent `ℓ ≥ 7` are cuspidal; with 019 and (T1) every section would be Selmer, hence cuspidal. Chain
noted by fork B1, to be checked; asked in LM6 E (c); belongs also to LM7.

**F27. Pointers from the main agent's reading before the fork (statements read in the introductions; the
consequences for his groups `Γ'_{g,ν}` and for (27), (28) of 2:sc332 are to be drawn in the LM3 review, not here).**
Hoshi–Minamide–Mochizuki, Cor. C: `Out(π̂_1(M_{0,ν})) = GT × S_ν` for ν ≥ 5, with no condition on the
automorphisms. Minamide–Nakamura: `Out(B̂_n) ≅ GT × (1 + n(n−1)Ẑ)^×` and `GT ≅ Out(B̂_n/centre)` for n ≥ 4;
`GT ≅ Out(Γ̂_{1,2})`. Boggi, arXiv:2011.15075v6 (22 Apr 2026, unrefereed), Thm A–C: for modular dimension > 1 the
outer automorphisms of the *procongruence* mapping class group preserving the class of a non-separating twist form
`GT` (times `Σ_n` for the pure group, `S ≠ S_{1,2}`); `GT ≅ Aut` of the procongruence Teichmüller tower; `GT` embeds
in the corresponding group for the profinite completion. Lochak–Nakamura–Schneps, arXiv:2602.12462 (Feb 2026):
the full `GT` acts on `Γ̂_{g,0}`, `Γ̂_{g,1}` for all g ≥ 1 (Thm 1.1, explicit formulas). Hirose, arXiv:2610.23719
(Oct 2026; abstract only): a second proof of the Deligne–Drinfeld conjecture, independent of 008. Bonatto–Robertson,
arXiv:2606.01466 (abstract only): a modular operad for the higher-genus tower with a faithful action of the
Nakamura–Schneps subgroup. 008 was read in full by the main agent (no error found in one reading; not certified).

## G. From LM8 and the drafting of LM8_PUSH (Claude Fable 5.2, effort max, agent a125034fd35557818, 13 Nov 2026)

Each line says how far it is checked. All are leads of the prompt `pro_prompts_draft_20261111\LM8_PUSH\PROMPT.md` unless marked otherwise.

- **F28 (manuscript; for the editors).** Cote 140-4, scan 243, margin at the top left: this agent reads "cela est fait par Olivier Leroy ?" on the scan image (enlarged crop). The first-pass transcription (`answers\unzipped\LM_C4-229-247\LM_C4-229-247_transcription.tex`, line 758) has "cela ne fait pas aller loin ?" marked unsure. One reader. If right, Grothendieck asks beside his "limit topos" parenthesis whether Leroy (thesis on the fundamental groupoid of a topos, Montpellier 1979) has done it.
- **F29 (reading settled).** Scans 242–243: the parenthesis is about a topological space with a filter and the projective limit of the sheaf topoi of its members, hedged twice by insertions. LM8 E.11 refutes it for residual germs (proof re-read: correct). The 2-limit of the `Sh(S_i)` is sheaves on the sublocale `⋂ S_i`: the point for the germ at a point of a regular space, empty for the residual germ of a Hausdorff space (Lead 14; short locale argument, not written out).
- **F30 (§47 as a fixed-point condition; derived, unchecked).** Descent along `φ : F̂_2 → C_2 ∗̂ C_3` and extension from the level-two subgroup give two homomorphisms `GT̂_0 → Out(C_2 ∗̂ C_3)`; the first restricted to the level-two subgroup is an endomorphism `D` of `GT̂_0` ("restrict to the sphere minus eight points over the `j`-tripod and fill five points"), and the §47 subgroup `C^φ` of LM2 E.3 is `Fix(D)`. With the 2-cycle relation `F(σ_1σ_2σ_1) = f^{-1}(σ_1σ_2σ_1)^λ`: §47 says that `f` is the `Int(s)`-coboundary of its own image `f(s, sr)`. The covering factors as `w = 4λ(1−λ)`, `j = 64(4−w)³/w²` (checked exactly), which points to the harmonic and equianharmonic equations of Nakamura–Tsunogai (from memory; not opened).
- **F31 (multiplier-one torsion at the metabelian level; checked on characters).** The beta function `1 − 2e_0` of LM8 A.22 is `𝔖₃`-invariant and fails the cocycle identity. For `g = 1 − 2e_1` (`e_1` an inversion-invariant idempotent of `Ẑ[[Ẑ]]` vanishing at the trivial characters), `g(X)g(Y)g(Z)` is an `𝔖₃`-invariant coboundary of order two and defines a non-inner pure peripheral involution of multiplier one of `F̂_2/F̂_2''`. So neither the 2-cycle and 3-cycle relations nor the Γ-factorization exclude such torsion in the metabelian image; lifting to `F̂_2` is the question (LM8_PUSH B.3).
- **F32 (the CM curve, first cover; by hand, unchecked).** The `[i]`-stable `𝔖₃`-cover of `y² = x³ − x` minus the origin is `v² = w⁷ − w` (genus 3, two cusps at Weierstrass points, Jacobian isogenous to `E³`); an open subgroup of `Gal(K̄/K^ab)` fixes its whole `H_1`. In general the fixed part of `H_1` of a cover should be the boundary plus the `E`-isotypic part orthogonal to the non-torsion cuspidal classes (Lead 2). The finite-cover attack on LM8 G.20 through abelianizations therefore cannot work for this curve; the decision is in degree two of the graded Lie algebras of the covers or needs another idea.
- **F33 (class three at 5).** `H¹_cts(G_Q, Z_5(3)) = Z_5` and `H²_cts(G_Q, Z_5(3))` is families tending to zero modulo `diag(q² − 1)`, with a non-zero lim¹ part (Lead 12; the proof of LM8 F.21 transposed; LM7_PUSH F.1 is the general statement, Proved at its checkpoint 04, unreviewed).

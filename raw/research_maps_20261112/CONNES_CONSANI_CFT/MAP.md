# MAP: Connes–Consani's geometric class field theory ↔ Γ°, sections and cusps in Grothendieck's cote 149

Written 2026-11-13 00:24 WEST by Claude (Fable 5.2, effort max), as a sub-agent of the main session. No sub-agents.

**Purpose.** A map along which a result on either side can be carried to the other: each link is an exact
statement with its number or label, an exact construction, and the scope of what is proved. Their papers were
read in the arXiv TeX, not end to end; each statement used was read with its hypotheses and, where the map
leans on it, with its proof.

**Flags.** **[opened]** = I read the statement in the source. **[memory]** = not checked against a source.
**[derived]** = proved in this file from [opened] statements; the proof is written where it is used.
**Speculation** is marked. Status of a link: **checked**, **fails** (with proof and scope), or **open** (with
what a check takes).

**Notation.** Γ_K = Gal(K̄/K); χ : Γ_K → Ẑ^* the cyclotomic character; Γ_K° = ker χ = Gal(K̄/K(μ_∞));
T = Ẑ(1) = T_∞(K̄^*); for a curve U/K: π = π_1(U_K̄), E_U = π_1(U), I_c ⊂ D_c the inertia and decomposition
groups of a lifted cusp c; C(s) = C_π(s(Γ_K°)) for a section s. On their side: A = A_Q, Y_Q = Q^×\A,
X_Q = Q^×\A/Ẑ^*, C_Q = Q^×\A^× = Ẑ^* × R_+^*, C_p ⊂ X_Q the periodic orbit of length log p,
H = ∏_{v≠p, v<∞} Z_v^*.

## 0. Sources

Their side, in `papers\<id>\src\`. Statement numbers of CC25 and CC24 are computed from the TeX counters (one
counter per section for theorems, propositions, lemmas, definitions, remarks, facts); "Theorem 3.12" is
confirmed by the citation "[CC3, Theorem 3.12]" in CC26. For the other papers I cite the TeX labels.

| Short | Reference | Read |
|---|---|---|
| CC25 | Connes, Consani, *Knots, primes and class field theory*, arXiv:2501.06560 (`arxiv-pisa.tex`) | §1 Introduction with Theorems 1–3 and its three tables; §2 Notations; §3 complete: Def. 3.1, Lemma 3.2, Lemma 3.3, Prop. 3.4, Def. 3.5, Prop. 3.6, Cor. 3.7, Rem. 3.8, Thm 3.9, Cor. 3.10, Fact 3.11, Thm 3.12, Rem. 3.13, with proofs; §4 complete: Prop. 4.1, Thm 4.2, table; §5.3 Prop. `ergodic23`. §5.1–5.2, §5.4, §6: headings only. Searched for "non-abelian", "anabelian", "absolute Galois", Q̄: no occurrence. |
| CC24 | Connes, Consani, *Knots, Primes and the adele class space*, arXiv:2401.08401 | all: Thm 1.1, Thm 1.2, §2, §3 Prop. `ergodic23` and the list of the eight orbits, (pi1), §4 Prop. `bciso`, the final Remark. Same search: no occurrence. |
| CC26 | Connes, Consani, *On the Jacobian of Spec Z-bar*, arXiv:2602.15941 (`Jacobian.tex`) | abstract; Introduction: Thm `xqthm` (statement), the map Θ, diagram (3floora), Thm `thm:fibers`, the uniformization theorem (framed and rooted arithmetic divisors); §`sectuniv`: the two Propositions and two Theorems on the fibres F_p and F_∞ with proofs, the Remark after them; line 2255. Rest not read. |
| CC21 | Connes, Consani, *BC-system, absolute cyclotomy and the quantized calculus*, arXiv:2112.08820 | Introduction: the BC-system paragraph with its four properties; the Arithmetic Site and Scaling Site paragraph; Thm `w0s1`, (defnsig), (newrhos), Thm `rabi10` (statements). Rest not read. |
| CC14 | Connes, Consani, *The Arithmetic Site*, arXiv:1405.4527 | Thms `thmpointswnt`, `structure2`, `structure3`, `mainthm`, `thmcomp` (statements). |
| CMR | Connes, Marcolli, Ramachandran, *KMS states and complex multiplication*, arXiv:math/0501424 | the comparison table (GL_1, GL_2, CM); the modular field with (cyclhom), (shimuraexseq); Prop. `AKsymm`; Thm `KMSCM` with (KMSbeta1), (intertwGalK); (FtauKab), (Shirec), (Shirecdiagr). Rest not read. |
| HP | Ha, Paugam, *Bost–Connes–Marcolli systems for Shimura varieties I*, arXiv:math/0507101 | introduction (BC and CM paragraphs); Question `classif-etats-KMS-general`; the Bost–Connes pair of a number field: Sh(Res G_m, X_F) ≅ π_0(C_F); Prop. `compute-out-tot-F`. Rest not read. |
| — | `LISTING_ABSTRACTS.md` | searched for non-abelian and Galois terms; abstracts of 2609.00299 and 2606.06604 read. |

Not read: arXiv:2609.00299, 2606.06604 (abstracts only), 2611.13129; Bost–Connes 1995; Connes–Marcolli I.

Our side.

| Short | File | Read |
|---|---|---|
| CK | the return CYCLOTOMIC_KERNEL (GPT-6 Astra, ChatGPT Pro mode), `CYCLOTOMIC_KERNEL_paper.tex`, `sections\conventions.tex`, results CSV | conventions; CSV rows A1, A2, A6, A7, A9, B1, B2, B6, B7, C1–C3, D0a, D0b, D1, D2, D5, D7, D11, D13, D14, D15, AE1, AE2, AE4, E1, E3, E4; in the paper the statements A1, A6, A7, B1, B2, D0b, D2, D5, D7, AE2, AE4, D14, E1, with the proofs of A1, A6, A7, AE2, AE4 |
| REV | `CYCLOTOMIC_REVIEW_OPUS\REVIEW.md` (Claude Opus 5.5, effort max) | all. Statuses below are its verdicts: 43 correct, 9 known, 4 open as stated, 0 wrong. |
| SHAPE | `GLOBAL_SHAPE_AFTER_CYCLOTOMIC_20261112.md` | all |
| F149 | `FLAGGED_149\PROMPT.md` | lines 1–58 (rows F1–F26, G1–G4, and what is attached); its "New since" paragraph in the review's replacement text |
| GR | `GOOD_REDUCTION\PROMPT.md` | "Where this comes from", the setting, R1–R9, Leads 1–8, Parts A–D |
| LM6 | `LM6_POINTS_AS_SECTIONS\PROMPT.md` | the opening of "What is to be settled"; Parts A–F, each item's first 260 characters; in full: B (a), B (f), C (b), C (c), (F3), F (g) |
| G149 | cote 149, first-pass transcription, `MPL_149_001-090` | scans 45, 53–56, 59–63, 80–86 |

The items of F149, GR and LM6 are open questions, not results. Not read: the rest of the CK paper, LM6 and
cote 149; Longue Marche scans (LM6 B (f) cites scan 480); every paper cited by CK or REV.

## 1. The dictionary

One row per link; the notes after the table carry the constructions and proofs.

| # | Link | Their statement | Our statement | Status |
|---|---|---|---|---|
| L1 | Ẑ^* = Γ_Q/Γ° | θ : Ẑ^* = lim (Z/m)^* → Gal(Q^ab/Q), θ(r)ζ_m = ζ_m^r, "canonical isomorphism" (CC25 before Thm 3.12, Fact 3.11); "C_Q is lifted in ideles as the subgroup Ẑ^* × R_+^*" (proof of Prop. 3.4 (ii)); table of §4: π_1^et(Spec Q)^ab ↔ C_Q modulo its connected component **[opened]** | Γ_K° = "Kernel of χ : Γ_K → Ẑ^×" (CK conventions); "Γ°, noyau du caractère cyclotomique Γ → Ẑ^*" (G149 scan 63; scan 45 for E°) **[opened]** | checked: χ ∘ θ = id |
| L2 | Γ° on their side | Y_Q → X_Q is the quotient by Ẑ^*; γ(L) = Y_Q ×_{Ẑ^*} Gal(L/Q) for L finite abelian (Def. 3.1, Thm 3.12); BC: symmetries Ẑ^*, values of zero-temperature KMS states on the arithmetic subalgebra generate Q^cycl, "the class field theory isomorphism intertwines the action of the symmetries and the Galois action on the values of states" (CC21) **[opened]** | Γ° is the kernel of the Γ_Q-action on each of these | checked. No group above Ẑ^* occurs in CC25 or CC24 (searched); CC26 calls the pull-back of Y_Q "the universal cover" |
| L3 | places and fibres | each place v of Q is covered by an orbit: C_p, a point for ∞, the generic orbit η (CC25 §1); fibres of the pull-back of Y_Q: C_Q over η, C_Q/Q_p^× over p, "Ẑ^× ≅ Gal(Q^ab/Q)" over ∞ (CC26 Thm `thm:fibers`, §`sectuniv`) **[opened]** | pro-points: "X' = Ũ^" (G149 scans 59–61); for Spec Z the places of Q̄ over v, the Γ_Q-set Γ_Q/D_w | checked: π_0(fibre over v) = Ẑ^*/χ(D_w) = places of Q(μ_∞) over v = Γ°-orbits of places of Q̄ over v. The fibre over ∞ is Ẑ^*/{±1}; CC26's "≅ Ẑ^×" **fails** as written (note L3) |
| L4 | Frobenius ↔ periodic orbit | π^{-1}(C_p) ≅ mapping torus of multiplication by p on H (Prop. 3.4); π_1^et(Spec Z_(p))^ab ≅ H and r^*(Frob_p) = p (Prop. 4.1); Thm 4.2; for L abelian and p unramified the monodromy of C_p in γ(L) is Frob_p and the components over C_p are "circles labeled by the places of L over p" (Thm 3.12 (iii), (iv)) **[opened]** | Γ_{F_p} → π_1^et(Spec Z_(p)) = Γ_Q/⟨⟨I_w⟩⟩ is a germ of section at the closed point p (sections over open subgroups: G149 scan 53; germs: CK A7) | checked; extended to ramified p **[derived]**; orientation fixed (note L4). The non-abelian Frobenius class: open on their side |
| L5 | inertia, decomposition ↔ isotropy | stabilizer in G of a point over x is χ(∏_{v∈Z(x)} Z_v^*) (Lemma 3.2 (ii)); unramified outside S ⟺ C(χ) ⊂ S, and ∞ ∈ S always (Prop. 3.6, Cor. 3.7); "the isotropy subgroup associated with the adeles that vanish exactly at a place v of K is K_v^×" (§1); π_1^et(Spec Z[1/q])^ab ≅ Z_q^* (CC24) **[opened]** | I_c ≅ Ẑ(1), N_π(I_c) = I_c, D_c acts on I_c through χ (CK A2, C1; G149 scan 54 (2)); for a divisor in characteristic 0: 1 → I_x̃ → N_x̃ → Gal → 1 with I_x̃ ≃ T_∞(K̄^*) (G149 scan 84 (7), (8)) | checked for the places: χ(I_w) = Z_p^*, χ(D_w) = Z_p^* × closure of p^Z. "A prime is a cusp" **fails** in the abelian layer (note L5) |
| L6 | Kummer torsor ↔ ideles | A^× = Q^× × Ẑ^* × R_+^* (used in Prop. 3.4 (ii) and in CC26) **[opened]** | splittings at a cusp form a torsor under H^1(Γ, T) ≃ K̂^* = lim K^*/n (G149 scan 54 (3); CK C1); the geometric ones a sub-torsor under G_m(S) (scan 85 (22)); LM6 F (g) (3), (4) | checked for Q **[derived]**: lim_n A^×/n = Q̂^* × Ẑ^*, and Q^× = Q̂^* ∩ A_f^×. Number fields: open |
| L7 | orientations of T | a zero-temperature state "selects a group isomorphism of the abstract group Q/Z with the group of roots of unity in C" (CC21); rooted arithmetic divisors: ρ : Q/Z → torsion of Hom(L, Q/Z), "the phase ambiguity (Galois ambiguity) has been resolved by fixing a specific configuration of roots of unity" (CC26) **[opened]** | T = T_∞(K̄^*); L_i ≃ T (G149 scan 54 (2)) | checked **[derived]**: over each orbit the fibre of Y_Q → X_Q is the torsor of generators of the Tate module of G_m at that place (note L7) |
| L8 | BC algebra ↔ cusp group; G_m | integral BC-system Z[Q/Z] ⋊ N, σ_n(e(γ)) = e(nγ), ρ̃_n(e(γ)) = Σ_{nγ'=γ} e(γ') (CC21 (defnsig), (newrhos), Thm `rabi10`); Hecke pair P^+(Z) ⊂ P^+(Q) of the ax+b group **[opened]** | I_c ≅ Ẑ(1); on G_m, E_U = Ẑ(1) ⋊ Γ_K and C(s) = Ẑ(1) for every s (CK C3, REV §2) | checked **[derived]**: Z[Q/Z] = R(I_c), σ_n = restriction and ρ̃_n = induction along nI_c ⊂ I_c; E_{G_m}/s(Γ°) = Ẑ(1) ⋊ χ(Γ_K) |
| L9 | sections | Frob_p ↦ p ∈ H is "the linking of the prime p with all other primes"; n ↦ p^n ∈ Z_q^* is injective (CC25 §1, Prop. 3.4 (iii)) **[opened]** | Théorème 3 and its failure over Q(μ_∞) (CK D7); Conjecture A (G149 scan 56) and D5; uniqueness D0b, D2 | checked: abelianized Frobenius germs separate primes; χ has no continuous splitting over any open subgroup **[derived, with Artin–Schreier from memory]**; over Γ° every extension splits (REV F8) |
| L10 | Γ_Q from Γ° and Ẑ^* | Ẑ^* is the group of the cover and of the BC symmetries | C_{G_Q}(G_{k(μ∞)}) = 1 (CK B1, correct; B2 known: Minamide–Tsujimura Thm 2.12, per REV) | checked **[derived]**: Z(Γ°) = 1, Ẑ^* → Out(Γ°) is injective, Γ_Q ≅ Aut(Γ°) ×_{Out(Γ°)} Ẑ^* |
| L11 | the layer above, over C_p | field K of fractions of the strict henselization of Z_(p), Q(ζ_ℓ : (ℓ,p) = 1) ⊂ K ⊂ Q_p^un (proof of Prop. 4.1) **[opened]** | Δ = G_{K(μ∞)} for K/Q_p finite; under good marked reduction C_{π^(p')}(s_x(Δ)) = π^(p') (CK D14, correct by spot check) | checked for the groups: D_w ∩ Γ° = Γ_{Q_p(μ_∞)}. The local system over C_p: open (note L11) |
| L12 | CM system ↔ E1, E3 | extremal KMS_∞ states of the CM system "evaluated on the arithmetic subalgebra 𝒜_{K,Q}, take values in K^ab", symmetries A_{K,f}^*/K^*, (intertwGalK); F_τ = K^ab (FtauKab) (CMR Thm `KMSCM`) **[opened]** | K = Q(i), E : y² = x³ − x, Δ = Γ_{K^ab}: N_2^{s(Δ)} = N_2, N_2^{s(Γ_K°)} = γ_2P/γ_3P ≃ Z_5(1) (CK E1, correct); E3 open as stated | checked: Δ is the kernel of the Galois action on the values of the CM system. E3 in their terms: open |
| L13 | A6 in the congruence quotient | Aut(F) ≅ Q^*\GL_2(A_f) for the modular field F (CMR (shimuraexseq)); (Shirec) at a CM point **[opened]** | C(s) ≠ 1 ⟺ s cuspidal, and then C(s) = I_c (CK A6, known in substance: Stix Cor. 22 and Thm 14 over K(μ_∞), per REV) | **fails** in the congruence quotient at CM points: the centralizer contains an open subgroup of the norm-one torus; proof in note L13, with two classical inputs from memory |
| L14 | covers for non-abelian L | Y_K = K^×\A_K with the action of C_K is defined for every global field K (CC25 §1) **[opened]**; γ is defined on abelian L only | open subgroups Γ' ⊂ Γ_Q and Γ'° (G149 scan 45) | open: for L = Q(i) the periodic orbits of γ(L) and of the zeta sector of L agree in number and length **[derived]**, the generic parts differ; the comparison of the two spaces is not in the papers read (note L14) |

### Notes to the links

**L1.** For r ∈ Ẑ^*, χ(θ(r)) = r by the definition of θ. So their deck group Ẑ^* is Γ_Q/Γ°, their
W(L) = {g ∈ Ẑ^* : g|L = id} (CC25 (wl)) is χ(Γ_L) for L ⊂ Q^ab, and for a number field K the group χ(Γ_K)
is W(K ∩ Q^ab), open in Ẑ^*. The cyclotomic quotient of Γ_K sees K ∩ Q^ab only, as γ does.
*Convention.* CC25 never uses the idelic Artin map; it uses θ. With the arithmetic normalization the
reciprocity map restricted to Ẑ^* ⊂ C_Q is u ↦ θ(u^{-1}) **[memory]**; nothing below depends on it.

**L3.** (a) *Fibres.* By CC26 (§`sectuniv`, Theorem on F_p) **[opened]**, π^{-1}(C_p) ≅ C_Q/ι_p(Q_p^×) as
topological groups; this is the mapping torus p^Z\(H × R_+^*) of Prop. 3.4. The map to H/closure(p^Z) is
continuous with connected fibres (mapping tori of a minimal translation of a compact monothetic group), so
π_0 = H/closure(p^Z) = Ẑ^*/(Z_p^* × closure(p^Z)) = Ẑ^*/χ(D_w), the set of places of Q(μ_∞) over p. The places
of Q̄ over p form the Γ_Q-set Γ_Q/D_w, and Γ°\Γ_Q/D_w = Ẑ^*/χ(D_w). So their fibre is the set of
Γ°-orbits of pro-points over p, thickened by a solenoid; the pro-points inside one orbit, the set
Γ°/(Γ° ∩ D_w), are absent from their space.
(b) *The fibre over ∞.* F_∞ is the set of classes of adeles (u, 0), u ∈ Ẑ^* (CC26, proof of the
Proposition on F_∞ **[opened]**). Two such are in one Q^×-class iff u' = qu with q ∈ Q^× ∩ Ẑ^* = {±1}. So
F_∞ = Ẑ^*/{±1} = C_Q/R^× = Gal(Q^ab/Q)/⟨complex conjugation⟩, the set of archimedean places of Q(μ_∞). This is
CC25 Rem. 3.13: "the fiber F_c is the quotient G/χ(−1) ... identical with the set of archimedean places"
**[opened]**. CC26 states "ℱ_∞ ≅ C_Q/R_+^× ≅ Ẑ^× ≅ Gal(Q^ab/Q)" (Thm `thm:fibers` and the Theorem of
§`sectuniv`); its proof finds that the kernel of A^× → ℱ_∞ is "the image of R^×" and then divides by R_+^×
only: the idele (−1_f, 1) is in the kernel and is not in R_+^×·Q_+^×. *Scope:* the identification of ℱ_∞
only; that ℱ_∞ is a compact group stands. Ẑ^*/{±1} and Ẑ^* are isomorphic as abstract profinite groups, not by
the map of the theorem.

**L4.** (a) *Ramified primes* **[derived]**. Formula (prelim) of CC25, π_χ^{-1}(C_p) = π^{-1}(C_p) ×_{Ẑ^*} G,
does not use p ∉ C(χ). On π^{-1}(C_p) the factor Z_p^* acts trivially and H acts simply transitively on the
H-coordinate, so π_χ^{-1}(C_p) ≅ p^Z\((G/χ(Z_p^*)) × R_+^*), the mapping torus of χ(p) on G/I_p (p ∈ H; I_p =
χ(Z_p^*) is the inertia group, by the "standard fact" quoted in the proof of Thm 3.12 (ii)). Its components
are the orbits of χ(p) on G/I_p, the set G/D_p of places of L over p; each is a circle of length f·log p; a
fibre has |G|/e points. So efg = [L : Q] is read off the cover at every prime. CC25 states (iii), (iv) for
unramified p only.
(b) *Orientation* **[derived]**. The idele with p at the place p and 1 elsewhere lies in the isotropy group of
every point over C_p and equals (p^{-1}, p^{-1}) in C_Q = Ẑ^* × R_+^*, with H-component p^{-1}. So the scaling
by λ ↦ p^{-1}λ acts on π^{-1}(C_p) as multiplication by p on H: "monodromy = Frob_p" is for the loop traversed
against the direction of growing λ.
(c) *The scheme side above the abelian layer.* CC25 uses the exact sequence π_1(Spec K) → π_1(Spec Q) →
π_1(Spec Z_(p)) → 1 (Stacks, Lemma 58.11.4, as cited there **[opened]**): π_1^et(Spec Z_(p)) = Γ_Q/N_p, N_p
the closed normal subgroup generated by an inertia group I_w. Its abelianization is Γ_Q/N_pΓ° = Ẑ^*/Z_p^* = H,
and Γ° maps onto its commutator subgroup. In Γ_Q/N_p the map r^* is defined up to conjugacy (a choice of
w | p); CC24: "The abelianization takes care of the need to specify the base point" **[opened]**. No space
whose fibre over C_p carries Γ_Q/N_p is constructed in the papers read.
(d) H = Aut(F̄_p^*) and p ∈ H is the Frobenius x ↦ x^p **[derived]**: F̄_p^* is the group of roots of unity of
order prime to p.

**L5.** For a place w | p of Q̄: χ(I_w) = Z_p^* (the isotropy of Lemma 3.2) and χ(D_w) = Z_p^* × closure(p^Z).
*Fails:* "the prime p of Spec Z[1/p] is a cusp in the sense of CK A2". *Proof.* For a cusp, I_c is
torsion-free procyclic and D_c acts on it through χ, non-trivially. The inertia at p in the abelian layer is
Z_p^* = π_1^et(Spec Z[1/p])^ab (CC24), which contains the torsion group μ_{p−1} and on which the decomposition
group acts trivially, the group being abelian. *Scope:* the abelian layer. In Γ_Q itself the tame quotient
I_w/P_w ≅ ∏_{ℓ≠p} Z_ℓ(1) carries the action of Frobenius by p **[memory]**, so it is cusp-like; its image in
the abelianization is μ_{p−1} only. The cusp-like part of a prime lies in Γ°-territory, above their cover.
What their side has in its place: Cor. 3.7, the archimedean place is ramified in every non-trivial cover.

**L6** **[derived]**. Every idele of Q is uniquely q·(u, λ), q ∈ Q^×, u ∈ Ẑ^*, λ > 0. Hence
A^×/(A^×)^n = Q^×/n × Ẑ^*/n and, in the limit over n, **lim_n A^×/(A^×)^n = Q̂^* × Ẑ^***, since
lim_n Ẑ^*/(Ẑ^*)^n = Ẑ^* (Ẑ^* is compact and its n-th powers are closed with trivial intersection). The left
side is the group of
compatible families of local Kummer classes: H^1(Q_p, Ẑ(1)) = lim Q_p^*/n = p^Ẑ × Z_p^*, H^1(R, Ẑ(1)) = {±1},
with, for each n, a unit class modulo n at almost all p. So such a family is uniquely the product of a global
class in Q̂^* = H^1(Q, Ẑ(1)) and an element of Ẑ^* = Γ_Q/Γ°: for the family (p^{a_p}u_p)_p with sign ε, the
second component is (ε·u_p·∏_{ℓ≠p} ℓ^{−a_ℓ})_p. At a rational cusp: families of local splittings of (2) of scan
54, compatible in this sense, modulo the global splittings, form a torsor under the group of the cover
Y_Q → X_Q.
Further, Q̂^* = {±1} × {(a_p) ∈ ∏_p Ẑ : for each n, n | a_p for almost all p}, and a ∈ Q̂^* lies in Q^× iff
a_p ∈ Z for all p and a_p = 0 for almost all p, that is iff its local classes lie in Q_p^× for all p and in
Z_p^* for almost all p. This proves LM6 F (g) (3). So Q^× = Q̂^* ∩ A_f^×: the group by which Connes divides
the adeles is the group of geometric splittings of scan 85.
*Number fields: open.* Expected **[memory]**: K̂^* ∩ A_{K,f}^× = K^×·closure(O_K^*), the closure being the
profinite completion of the units (Chevalley), and its classes ε^α of LM6 F (g) (4) lie in the connected
component of C_K, the kernel of reciprocity, whose solenoids number r_1 + r_2 − 1 (Artin–Tate). A check takes
the two references and one page.

**L7** **[derived]**. Hom(Q/Z, μ_∞(K̄)) = lim μ_n = T, and the isomorphisms Q/Z → μ_∞ are the topological
generators of T, a torsor under Ẑ^* on which Γ_K acts through χ. Fibre by fibre:
- over a point of η the fibre of Y_Q → X_Q is a Ẑ^*-torsor (C_Q → R_+^*); in CC26's terms the roots ρ of the
  divisor L = Z; with e(s) = exp(2πis) (CC25 before Thm 3.12) it is the torsor of generators of T(C);
- over a point of C_p the fibre is H = Aut(roots of unity of order prime to p), the torsor of generators of
  T(G_m ⊗ F̄_p) = ∏_{ℓ≠p} Z_ℓ(1) (μ_{p^n}(F̄_p) = 1), and the monodromy p is Frobenius on it. The collapse
  from Ẑ^* to Ẑ^*/Z_p^*, which CC25 calls ramification (Lemma 3.2, (rami0)), is the vanishing of μ_{p^∞} in
  characteristic p;
- over ∞ the fibre is Ẑ^*/{±1} (L3): generators of T(C) up to complex conjugation.
So a point of Y_Q over the visible part of X_Q is an orientation of Grothendieck's T at a place; since
L_i ≃ T canonically, it is a topological generator of the loop group of any rational cusp, read at that place.
The values of the zero-temperature states are in CC21 from a survey sentence; Bost–Connes was not opened.

**L8** **[derived]**. (a) The continuous complex characters of I_c ≅ Ẑ(1) form the group Q/Z (after an
orientation), so the representation ring R(I_c) is Z[Q/Z]. For the open subgroup nI_c ≅ I_c: restriction of
characters is e(γ) ↦ e(nγ) = σ_n, and induction is e(γ) ↦ Σ_{nγ'=γ} e(γ') = ρ̃_n. So the integral BC-system
Z[Q/Z] ⋊ N (CC21 Thm `rabi10`, where σ_n, ρ̃_n are Frobenius and Verschiebung of W_0) is R(I_c) with the
restrictions and inductions along the subgroups nI_c, which are the cusp groups of the covers ramified to order
n at c (written L_i^d in LM6 A (c); his text for them was not opened). Γ_K acts on R(I_c) through χ, as the BC
symmetries. Equivalently for G_m: e(γ) is the
Kummer local system of monodromy e(γ), σ_n and ρ̃_n are pull-back and push-forward by x ↦ x^n.
(b) On G_m, E_U = Ẑ(1) ⋊ Γ_K (REV §2) and s(Γ_K°) is normal in E_U for every section s (Γ° acts trivially on
Ẑ(1)); E_U/s(Γ_K°) = Ẑ(1) ⋊ χ(Γ_K) ⊂ Ẑ(1) ⋊ Ẑ^*, the Ẑ-points of the ax+b group of the BC Hecke pair
P^+(Z) ⊂ P^+(Q): the completion of the translations P^+(Z) with the symmetries Ẑ^*. The subgroup s(Γ°) depends
on s through the restriction of its Kummer class to Γ°, which is where D7 lives: the classes of 1 and ζ_6
agree on Γ_{Q(μ_∞)}.

**L9.** (a) The image of Frob_p in π_1^et(Spec Z[1/S])^ab = ∏_{q∈S} Z_q^* is p, for p ∉ S (CC24 Thm 1.2 for
S = {q}, (pi1) for two primes, CC25 Prop. 4.1 **[opened]**; general finite S **[memory]**). Two primes p ≠ p' outside S ≠ ∅ have different images, Z injecting into
Z_q. This is Théorème 3 for the arithmetic curve: the abelianized germs at closed points separate the points
as soon as one prime is removed, and carry nothing on Spec Z itself (π_1 = 1). The procyclic subgroups they
generate can coincide.
(b) *Existence side* **[derived]**. For a number field K the extension 1 → Γ_K° → Γ_K → χ(Γ_K) → 1 has no
continuous splitting over any open subgroup V of χ(Γ_K): V contains ∏_{p∤N} Z_p^* for some N, hence elements
of order 3 (in Z_p^*, p ≡ 1 mod 3), and Γ_K has no element of order 3 (Artin–Schreier **[memory]**; it is F149 row F2, second claim). So
the group of their cover does not act on Q̄. On the other side Γ° = G_{Q^ab} is projective (cd ≤ 1, REV F8),
so every extension restricted to Γ° splits and Conjecture A has no content there (CK D5; the content is
Clark's curves without Q^ab-points). The field Q^ab is the function field of their maximal cover (table of
CC25 §1: "Maximal abelian extension Q^ab" ↔ 𝒴_Q → 𝒳_Q).

**L10** **[derived]** from B1 with k = Q. Z(Γ°) = Γ° ∩ C(Γ°) = 1. If g ∈ Γ_Q acts on Γ° as conjugation by
h ∈ Γ°, then gh^{-1} ∈ C(Γ°) = 1, so g ∈ Γ°: the outer action Ẑ^* → Out(Γ°) is injective. The map
g ↦ (c_g, χ(g)) is then an isomorphism of abstract groups Γ_Q → Aut(Γ°) ×_{Out(Γ°)} Ẑ^*: injective by B1;
onto, since for (α, u) with [α] the image of u and g with χ(g) = u, α = c_{gh} for some h ∈ Γ°. So the
extension above their cover has no class beyond the outer action: any object on their side that extends γ to
Γ° must carry a faithful outer action of the group of the cover.

**L11.** Q_p(μ_∞) = Q_p^un(μ_{p^∞}) is the maximal abelian extension of Q_p **[memory]**, and
D_w ∩ Γ° = Γ_{Q_p(μ_∞)}, χ being compatible with D_w ≅ Γ_{Q_p}. So CK D14's group Δ, for K = Q_p, is the
stabilizer in Γ° of the pro-point w: the pro-points inside one Γ°-orbit over p (L3) form Γ°/Δ. D14 says that Δ
fixes all of π^(p') at an integral point of a curve with good marked reduction; since K(μ_∞) ⊃ K^un, Δ lies in
inertia. *Open, what a check takes:* that under good reduction at p the outer action of D_w on π^(p') factors
through D_w/I_w = Γ_{F_p} with Frobenius acting as on the special fibre (specialization, SGA 1 XIII; Oda,
Tamagawa: GR R9, not opened). Given that, each curve U/Q with good reduction at p gives an outer local system
on the circle C_p with fibre π^(p') and monodromy the Frobenius, and on a cusp group I_c^(p') = ∏_{ℓ≠p} Z_ℓ(1)
the monodromy is p: the torsor of generators of that rank-one piece is π^{-1}(C_p) → C_p (L7).

**L12.** For E with complex multiplication by O_K defined over K, Γ_K acts on T(E) through an abelian quotient
and the values at τ of the modular functions generate K^ab (CMR (FtauKab)), so Δ = Γ_{K^ab} is the subgroup of
Γ_K fixing every value of the CM system, as Γ_K° fixes every value of the BC-system. E1 in their terms: on the
class-two pro-5 quotient N_2 of π_1(E ∖ O) at the tangential base point, Γ_K acts through the symmetry group
A_{K,f}^*/K^* of the CM system; the subgroup Γ_K°/Δ = Gal(K^ab/K(μ_∞)) fixes exactly the centre Z_5(1). That
group is the kernel of the norm A_{K,f}^*/K^* → Ẑ^* **[memory: reciprocity is compatible with norm and
restriction]**. E3 asks whether Δ fixes the compatible system of the N_r; if it does not, the action leaves
the CM system's group at some r ≥ 3.

**L13.** *Setting.* U = Y(N), N ≥ 3, over a number field K ⊃ Q(μ_N); x ∈ U(K) with elliptic curve E_x; the
composite of the point section s_x with E_U → GL_2(Ẑ) is the representation ρ on T(E_x), and π maps onto the
closure of Γ(N) in SL_2(Ẑ) **[memory, standard]**; det ρ = χ. *Proof of the failure.* Let E_x have complex
multiplication by O_K', K' ⊂ K. Then ρ(Γ_K) is an open subgroup of (O_K' ⊗ Ẑ)^* **[memory, CM theory]** and
ρ(Γ_K°) = ρ(Γ_K) ∩ T^1, T^1 the elements of norm 1, open in T^1. At each p an open subgroup of T^1(Z_p)
contains a non-scalar element, whose centralizer in M_2(Z_p) is O_K' ⊗ Z_p. So the centralizer of ρ(s_x(Γ_K°))
in the image of π is T^1(Ẑ) ∩ closure(Γ(N)), an infinite group, while s_x is not cuspidal and C(s_x) = 1 in π
(A6). *Scope:* the congruence quotient, which is where Aut(F) = Q^*\GL_2(A_f) and (Shirec) act; A6 itself is
untouched. The three cases in that quotient: E_x without complex multiplication, centralizer inside {±1}
(Serre's open image theorem **[memory]**); complex multiplication, open in T^1(Ẑ); a cusp, the image of I_c, a
unipotent group ≅ Ẑ(1). The kernel of π → SL_2(Ẑ) is what turns the three cases into the two of A6.

**L14** **[derived]**. For L abelian, the periodic orbits of γ(L) over C_p are G/D_p circles of length
f·log p (L4 (a)). Put X_L = L^×\A_L/(Ô_L^*·K_∞), K_∞ the maximal compact subgroup of (L ⊗ R)^*; for L = Q this
is X_Q. The classes of adeles vanishing at one finite place w only, with unit components elsewhere, form the
group C_L/(Ô_L^*·K_∞·L_w^×). For L = Q(i) (class number 1, one archimedean place) this is the circle
R_+^*/N(w)^Z of length log N(w) = f·log p: two circles of length log p for p ≡ 1 mod 4, one of length 2 log p
for p ≡ 3 mod 4, one of length log 2 for p = 2, as in γ(L). The generic parts differ: two copies of R_+^* in
γ(L), one in X_L. For class number h > 1 the same set is |Cl/⟨[w]⟩| circles of length ord([w])·log N(w), and
for r_1 + r_2 > 1 it has dimension r_1 + r_2: X_L is then the analogue of the Picard group, as CC26 says of
X_Q, not of the curve. X_L exists for every finite L/Q, with Aut(L/Q) acting and the norm X_L → X_Q. *Open,
what a check takes:* the exact relation of γ(L) to X_L for L = Q(i) (one page), then for abelian L through
the Hilbert class field; if there is one, the system of the Y_L with norms is the candidate for the functor on
all finite extensions.

## 2. Transport

| Link | From their side to ours | From our side to theirs | Scope |
|---|---|---|---|
| L1, L2 | A statement on a cover γ(L) is a statement on the Γ_Q-set Gal(L/Q), L ⊂ Q(μ_∞). | A statement on Γ° has trivial image under γ: Γ° acts trivially on every γ(L), on Y_Q and on the BC values. | All of CC25, CC24. Their constructions say nothing about the layer above the abelian one; they neither assert nor exclude a cover above Y_Q. |
| L3 | The fibre C_Q/Q_v^× gives the set of Γ°-orbits of pro-points over v with its Ẑ^*-action. | D0b ("at most one fixed pro-point", Γ°- and Γ-fixed sets equal) has the following analogue to state on Spec Z: the stabilizer in Γ° of a place w is Γ_{Q_p(μ_∞)} and fixes w alone if Γ_{Q_p(μ_∞)} lies in no other decomposition group. Open; the full-group statement is Neukirch's **[memory]**. | The correction F_∞ = Ẑ^*/{±1} is on their side and is independent of ours. |
| L4 | Thm 3.12 with L4 (a): the decomposition of p in every abelian L as the cycle structure of one loop. Nothing on non-abelian L. | The Frobenius class in Γ_Q/N_p, and through L11 the outer Frobenius on π^(p'), are the data a non-abelian cover must have as monodromy over C_p. | Abelian L proved; non-abelian: a requirement, no construction. |
| L5 | Cor. 3.7 (∞ ramifies in every cover) is the abelian shadow of F149 F2: τ generates the decomposition group at ∞, and Ẑ^*/{±1} is the set Γ°\Γ_Q/⟨τ⟩. | CK A2 (N_π(I_c) = I_c, C_π(z) = I_c) has no counterpart in the abelian layer. | The failure "prime = cusp" is for the abelian layer; tame inertia in Γ_Q is cusp-like **[memory]**. |
| L6 | The product decomposition of the ideles of Q settles LM6 F (g) (3) and identifies the obstruction group for local families of cuspidal splittings with Ẑ^*. | His sub-torsor of geometric splittings (scan 85) is, over Q, the group Q^× by which the adeles are divided; over K the defect closure(O_K^*)/O_K^* is expected to be the profinite part of the connected component of C_K. | Q proved here; K open. |
| L7, L8 | The cover Y_Q → X_Q and the BC algebra are functions of the Γ_Q-module T alone. A cusp of any curve gives a copy: R(I_c) with restriction and induction. | A6: under a cuspidal section the part of π fixed by Γ° is one copy of T, the module from which their cover is built; under a non-cuspidal section nothing is fixed. A7, AE2: for Δ ⊃ an open subgroup of Γ°, the fixed part is ∏_{ℓ : χ_ℓ|Δ = 1} Z_ℓ(1). Read with L7: the ℓ-components of the orientation that Δ no longer moves. | A6, A7, AE2 over number fields and finitely generated fields (AE1). |
| L9 | "Linking" p ∈ ∏ Z_q^* is the abelianized germ at a closed point; it gives the analogue of Théorème 3 on Spec Z[1/S]. | D5 and REV F8: over the field of their maximal cover every section exists, so existence statements need the quotient Ẑ^* = Γ/Γ° (SHAPE); and that quotient does not lift (L9 (b)). D0b, D2: uniqueness holds over K(μ_∞). | Number fields. |
| L10 | — | B1 gives the form of any extension of γ: the group Γ° with a faithful outer action of their Ẑ^*. | Abstract groups. |
| L11 | Prop. 4.1's field K is where D14's Δ lives. | D14 gives the fibre of the candidate non-abelian local system over C_p in the prime-to-p quotient, for integral points and integral tangents, and (E.4) for twisted cusp sections. | Good marked reduction; the full group and bad reduction are D15, open. |
| L12 | (intertwGalK), (Shirec): the Galois action on N_2 for the CM curve is an action of the CM system's symmetry group. | E1: the BC subgroup Γ_K° fixes the centre of N_2 only; the CM subgroup Δ fixes N_2. E3 would decide whether the CM system suffices for all N_r. | K = Q(i), y² = x³ − x, pro-5, class two. |
| L13 | Aut(F) acts on the congruence quotient only. | A6 does not descend to it; the centralizer of the image of Γ° there separates CM points, other points and cusps. | Modular curves; inputs from memory. |
| L14 | Y_L for every L. | The system of open subgroups Γ_L with Γ_L° has, on their side, the system of the Y_L with norms. | Open. |

**What their constructions say about the layer above the abelian one.** In the papers read: nothing is
constructed above Y_Q, and "universal cover" in CC26 means the pull-back of Y_Q. Three things on their side
reach beyond Γ_Q/Γ°: the adele class spaces Y_L of all number fields (L14); the GL_2-system, whose group Aut(F)
contains the congruence image of the geometric π_1 of modular curves and meets Γ_K only through abelian
quotients at CM points (L13, L12); and the BC algebra as R(I_c), which attaches their abelian system to every
cusp of every curve (L8).

**What our results give back.** The shape of the missing layer: Γ° is centre-free with trivial centralizer in
Γ_Q, the group Ẑ^* of their cover acts on it outer-faithfully and does not lift (L10, L9 (b)); over C_p the
missing fibre is Γ°/Γ_{Q_p(μ_∞)} (L3, L11); under a cuspidal section the Γ°-fixed part of π is exactly the
module T of their cover (A6 with L7), with the primewise form for larger subgroups (AE2); and one correction
to CC26 (L3 (b)).

## 3. Our prompts

Sentences to add; no prompt was edited. Each is a reference, a lead or an item, marked.

**FLAGGED_149.**
- Row F2 (reference): "The abelian shadow of the last two claims: χ(τ) = −1, and the set of archimedean places
  of Q(μ_∞) is Ẑ^*/{±1}, the fibre over the archimedean point of the cover Q^×\A_Q → Q^×\A_Q/Ẑ^* (Connes,
  Consani, arXiv:2501.06560, Remark 3.13). State the full statement beside it: the conjugates of τ are in
  bijection with Γ_Q/{1, τ}, the archimedean places of Q̄, and Γ° acts on this set with orbit space Ẑ^*/{±1}."
- Row F8 (item): "Corollaries of the centralizer statement, each to be proved: the centre of Γ° is trivial;
  the outer action Ẑ^* = Γ_Q/Γ° → Out(Γ°) is injective; Γ_Q is the fibre product Aut(Γ°) ×_{Out(Γ°)} Ẑ^*, with
  the topology on Aut(Γ°) for which this is an isomorphism of topological groups made explicit; for every
  number field K the sequence 1 → Γ_K° → Γ_K → χ(Γ_K) → 1 has no continuous splitting over any open subgroup of
  χ(Γ_K)."
- Rows F14, F15 (reference and item): "For S = Spec K the frame of scans 82–85 is the completed idele
  sequence. Prove: lim_n A_Q^×/(A_Q^×)^n = Q̂^* × Ẑ^* (from A_Q^× = Q^× × Ẑ^* × R_+^×), and for a number
  field K determine the kernel and the cokernel of K̂^* → lim_n A_K^×/(A_K^×)^n and the subgroup of K̂^* of
  classes whose local components lie in K_v^× for all v and in O_v^× for almost all v."

**GOOD_REDUCTION.**
- After B8 (item): "Residue field finite. Let K/Q_p be finite, U_η a hyperbolic curve over K, π^(p') the
  maximal prime-to-p quotient of π, and replace (30) by 1 → I_K → Γ_K → Γ_k → 1. Prove or refute: the pair has
  good reduction if and only if I_K acts trivially (outer) on π^(p'); in that case the outer action of Γ_K on
  π^(p') is the action of Frobenius on the prime-to-p fundamental group of the special fibre, and on a cusp
  group it is the q-th power map, q = #k. Then determine, for split stable reduction, the image of the tame
  inertia ∏_{ℓ≠p} Z_ℓ(1) in Out(π^(p')) as in A1 (iii). Reference for the rank-one case: for G_m this
  Frobenius is the monodromy p of the periodic orbit C_p on ∏_{ℓ≠p} Z_ℓ^* = π_1^et(Spec Z_(p))^ab (Connes,
  Consani, arXiv:2501.06560, Proposition 3.4, Proposition 4.1, Theorem 4.2), and CYCLOTOMIC_KERNEL D14 is the
  statement for the subgroup G_{K(μ_∞)} of inertia."
- Part C, C3 (lead): "For K = Q_p the group G_{K(μ_∞)} is the stabilizer, in the kernel Γ° of the cyclotomic
  character of Γ_Q, of a place of Q̄ over p; so C3 in residue characteristic p computes what Γ° fixes at one
  pro-point over p."

**LM6_POINTS_AS_SECTIONS.**
- F (g), after (3) (item; (3) itself is proved in three lines in note L6): "(3 bis) Prove: lim_n A_Q^×/(A_Q^×)^n = Q̂^* × Ẑ^*; a family of local Kummer classes at a rational
  cusp, compatible modulo every n, is uniquely a global class times an element of Ẑ^* = Gal(Q(μ_∞)/Q); compute
  that element from the restrictions of local sections to the decomposition groups, and prove or refute that
  it is the obstruction to a family of local cuspidal sections of E_U → Γ_Q coming from one global cuspidal
  section. For a number field K with a unit of infinite order, prove or refute: the classes ε^α of (4) are
  exactly the classes of K̂^* that are everywhere locally geometric and not global, and their images in the
  idele class group lie in its connected component."
- F (d) (item; it sharpens the remark of the shape note): "Prove: Γ_K is determined by Γ_K° with the outer
  action of χ(Γ_K) (CYCLOTOMIC_KERNEL B1); a section s of E_U → Γ_K is determined by s|Γ_K° together with the
  action of s(Γ_K) on it by conjugation; determine the classes of sections of E_U over Γ_K° that extend to Γ_K,
  as the classes fixed by χ(Γ_K) for which an obstruction class vanishes, and compute that class (the sequence
  1 → Γ_K° → Γ_K → χ(Γ_K) → 1 does not split)."
- C (b), (c) (reference): "The map from the conjugates of complex conjugation to the archimedean places of
  Q(μ_∞) is the quotient by Γ°, with image Ẑ^*/{±1} (arXiv:2501.06560, Remark 3.13)."
- B (f) (lead; scan 480 was not read by the author of this sentence): "A necessary condition 'faisant
  intervenir les Frobenius': for almost all p the outer action of a decomposition group at p on π^(p') factors
  through Frobenius, which acts on each loop group by the p-th power; the loop-group part of this condition is
  the cover Q^×\A_Q → Q^×\A_Q/Ẑ^* over the periodic orbit C_p."
- A (d) (reference): "The integral Bost–Connes algebra Z[Q/Z] ⋊ N with σ_n(e(γ)) = e(nγ),
  ρ̃_n(e(γ)) = Σ_{nγ'=γ} e(γ') (arXiv:2112.08820, Theorem `rabi10`) is the representation ring of a loop group
  L_i ≅ Ẑ(1) with restriction and induction along L_i^n; the ρ ∈ Ẑ^* of scans 86–87 act on it as the symmetries
  of that system."

**LM8 (elliptic tables; E3).**
- (item) "For K = Q(i), E : y² = x³ − x, U = E ∖ O and the pro-5 quotients N_r of CYCLOTOMIC_KERNEL E1–E3:
  the action of Γ_K on N_2 factors through Gal(K^ab/K) = A_{K,f}^*/K^*, the symmetry group of the CM system of
  Connes, Marcolli, Ramachandran (arXiv:math/0501424, Theorem `KMSCM`), and Γ_K°/Γ_{K^ab} is the kernel of the
  norm to Ẑ^*. For each r decide whether the action on N_r factors through Gal(K^ab/K); for the least r where
  it does not, give the cocycle on Γ_{K^ab} and the field it cuts out. Lead (from memory, unverified):
  Nakamura's elliptic Soulé characters (1995) are the expected first obstruction."

## 4. Open items, by cost

1. *Minutes.* The three [derived] proofs of L3 (b), L4 (a), L6 for Q are written above; a second reader
   checks them in one sitting.
2. *An hour.* Open Bost–Connes 1995 and Connes–Marcolli I for the exact statements behind L7 (the extremal
   KMS_∞ states as embeddings Q/Z → C^*) and L13 (the GL_2-system; what the values at a non-CM point generate).
3. *An hour.* L6 for number fields: Chevalley's theorem on units and the structure of the connected component
   of C_K (Artin–Tate, Neukirch), then one page.
4. *Half a day.* L14 for L = Q(i): compare γ(L) with X_L = L^×\A_L/(Ô_L^*·K_∞) point by point.
5. *Half a day.* L13 with opened sources (Serre 1972; Shimura or Lang for CM; the identification of the
   congruence image of a point section), and the statement of the trichotomy as a proposition.
6. *Half a day.* L11: open SGA 1 XIII and Tamagawa 1997 (5.3); write the outer local system over C_p for
   P^1 ∖ {0, 1, ∞}, which has good reduction at every p.
7. *A Pro item.* E3 in the form of the LM8 sentence of §3.
8. *A Pro item.* L3's analogue of D0b on Spec Z: fixed pro-points of Γ_{Q_p(μ_∞)} acting on the places of Q̄.
9. *Research.* A space above Y_Q with Γ° in its deck group (Speculations S2, S3).
10. *Reading.* arXiv:2606.06604 and 2609.00299 for whether the absolute curve (Spec Z)_{F_1} carries more than
    Ẑ^*; 2611.13129 was not needed by any link.

## 5. My own arguments and hunches

**S1. Speculation: Y_Q is the space of adelic tangent vectors at a rational cusp, modulo rational scalars.**
For a one-dimensional Q-vector space V, Q^×\(V ⊗ A_Q) is canonically Y_Q (two bases differ by q ∈ Q^×, which
acts trivially). With V the tangent line at a rational cusp c: the generic orbit, a C_Q-torsor, is the set of
nowhere-vanishing adelic tangent vectors modulo rational ones, that is, of adelic families of local tangential
base points modulo global ones (L6 is its Kummer form); the points over C_p are the families that vanish at p.
*What would test it:* CK D14 (E.4) computes what G_{K(μ_∞)} fixes for the section twisted by a Kummer class of
valuation b ∈ Ẑ: everything in π^(p') if b = 0, the cusp group otherwise. The adeles complete the valuation
group Z to Z ∪ {∞}, Kummer theory to Ẑ, and p^{m!} tends to 0 in the first and to 1 in the second. A statement
relating the two limits for the sections s_{p^n v} would confirm it; a proof that no topology on sections makes
s_{p^n v} converge as n → ∞ in Z would refute it.

**S2. Speculation: the non-abelian cover is a torsor of markings.** By L7 the cover Y_Q → X_Q is the torsor
of orientations of T, place by place. Replace T by π = π_1 of P^1 ∖ {0, 1, ∞} with its outer Γ_Q-action, which
is faithful (Belyi **[memory]**): over η the Γ_Q-orbit of a marking of π, over C_p the markings of π^(p') with
monodromy the outer Frobenius (L11), over ∞ the markings up to the real structure (LM6 Part C). The map
"marking ↦ induced generator of the loop group at 0" sends it to Y_Q, and Γ° is the group of this map.
*What would test it:* (i) the first layer where it differs from Y_Q. On the class-two quotient of the pro-ℓ π
the Galois action is given by χ alone; at class three the Soulé character κ_3 : Γ_{Q(μ_{ℓ^∞})} → Z_ℓ(3) enters
**[memory]**. So the first test is a cover of X_Q with group Z_ℓ(3) ⋊ Z_ℓ^* whose monodromy over C_p is the
class of (κ_3(Frob_p), p). (ii) Whether a global topology exists: in CC25 the topology of the covers comes from
the adeles; here it would have to come from a sheaf on the scaling site, with CC25 Theorem 3 (the sheaf of
semilocal algebras on Spec Z, label `structure1`) as the model.

**S3. Speculation: the simplest layer above Q(μ_∞) is already on their side, in the ax+b group.** The field
Q(μ_∞, a^{1/n} : a ∈ Q^×, n ≥ 1) is cut out by the homomorphism ((κ_a)_a, χ) : Γ_Q → Hom(Q^×, Ẑ(1)) ⋊ Ẑ^*,
κ_a the Kummer cocycle of a: one copy of the group of L8 (b) for each prime. Its image is not everything
(√±p lies in Q(μ_∞)) **[memory]**. It is the field cut out by the point sections of G_m at all rational
points, restricted to Γ°. Since the BC-system is the Hecke algebra of the ax+b group, a "BC-system with
base point a" for each a ∈ Q^×, with group Ẑ(1) ⋊ Ẑ^* in place of Ẑ^*, would be the first non-abelian
extension of their picture, and its zero-temperature values would be the a^{1/n}. *What would test it:* the
Hecke pair (P(Q), P(Z)) with the full ax+b group P in place of P^+ and its KMS states; whether any of the 60
listed papers treats it was not checked.

**S4. Speculation (a hunch on L13).** The congruence kernel of π → SL_2(Ẑ) is what removes the CM centralizers. For the
GL_2-system this says that the symmetry group Q^*\GL_2(A_f) cannot see A6, and that a system built on the full
profinite completion of SL_2(Z) (non-congruence modular functions) would have trivial centralizers at all
non-cuspidal points. *What would test it:* compute C_π(s_x(Γ°)) in the quotient of π by the kernel of one
non-congruence cover of Y(N) at a CM point x.

**S5. Speculation (a hunch on L3).** The fibre C_Q/Q_p^× is connected-by-profinite: a solenoid over the set of places of
Q(μ_∞) over p. The solenoid is the closure of the Frobenius flow; in the function-field column of CC25's table
it is the orbit of a closed point under Frobenius. For Grothendieck's X' this suggests a version of Conjecture
B on Spec Z in which the fixed pro-point of a decomposition group is replaced by a closed orbit of the scaling
flow. *What would test it:* state D0b for the action of R_+^* × Γ° and check it on γ(L) for L = Q(i).

# Family 019 read in full, and the literature of the section conjecture (for F7, H5, H7 and the LM6 Parts)

Author: Claude Fable 5.2, effort max (fork B1 of the LM expert successor). Written 12 Nov 2026, 13:09–13:39 UTC
(clock read at start and end). Scope: OpenAI family 019 (two papers), then the primary sources on sections of
arithmetic fundamental groups. Copies read are in `<local>/Documents\Free or receipted\free\lm-expert-20261112\`
(one folder per file; list with SHA-256 in `LM_EXPERT\work\lit\downloads_B1.jsonl`); the 019 texts were re-extracted
as UTF-8 to `LM_EXPERT\work\papers2\019_main.txt` and `019_companion.txt` (the extraction in `work\papers\` had lost
the mathematical symbols).

Words used below. **Verified**: I followed the argument line by line and found it correct. **Checked**: I compared
the paper's citation with the cited text itself (a free copy) and the cited statement says what the paper says it
says. **Not checked**: neither. Scans of La Longue Marche are cited as `2:scN` (cote 140-2).

---

## Part 1. Family 019

### 1.A The main paper: *The p-adic section conjecture* (OpenAI, 6 October 2026, 24 pp.)

**Standing notation of the paper.** p a prime; k/Q_p finite; X/k smooth, proper, geometrically connected, of genus
≥ 2; K = k(X); K0 = k̄(X); K̃ ⊂ K^sep the compositum of the function fields of all connected finite étale covers of
X, so Gal(K̃/K) = π_1(X). For a real-valued rank-one norm on K^sep extending the p-adic norm (|p| = 1/p):
E = completion of K^sep, H = closure of K̃ in E, Ω = completion of k̄ (a subfield of H, algebraically closed, value
group Q). The fixed embedding K0 → H with Ω → H is an H-valued point of X_Ω; its image in the Berkovich space
X_Ω^an is called ξ (its projection to X_k̄ is the generic point; ξ itself may be of any type, including an
Ω-rational point not in X(k̄)). "Horizontal ramification indices" of a finite F/K0: the ramification indices at
closed points of the corresponding cover of X_k̄. ℓ: a fixed odd prime ≠ p. L_ℓ ⊂ K^sep: the compositum of all
finite Galois F/K0 whose horizontal indices divide ℓ.

**Every numbered statement, with hypotheses and my verdict.**

| No. | Statement (hypotheses in full) | Verdict |
|---|---|---|
| Thm 1.1 | For every prime p, every finite k/Q_p and every smooth proper geometrically connected X/k of genus ≥ 2: X(k) → {continuous sections of π_1(X) → G_k}/conjugation by π_1(X_k̄) is bijective. | Follows from Thm 1.2 + Pop–Stix + Koenigsmann as the paper says; the deduction (Section 7) is **verified**. |
| Thm 1.2 | Same k, X. For every real-valued rank-one norm on K̃ extending the normalized p-adic norm and every prolongation to K^sep: K^sep ⊂ H inside E. Equivalently: the completion of K̃ at every rank-one valuation above p is algebraically closed. | Proof (Sections 3–6) **verified** step by step, given the external theorems listed below. |
| Lemma 3.1 | f: C → X_k̄ finite surjective, C smooth proper connected; b ∈ X(k̄); t_b a rational function that is a local parameter at b. Then there is an open disc B_b ∋ b in X_Ω^an with coordinate t_b whose full inverse image in C_Ω^an is a disjoint union of open discs with coordinates z_c, t_b = z_c^{e_c} (e_c the ramification index; no condition p ∤ e_c). For finitely many b the discs can be taken pairwise disjoint and not containing ξ. | Verified (p-adic exp/log for the e_c-th root of a unit close to 1; compactness for the full inverse image). |
| Prop 3.2 | f, degree d, branch set B, discs B_b as in 3.1; m_b a positive multiple of all ramification indices over b; g: Y → X_Ω finite surjective from a smooth proper connected curve; radii 0 < r_b < R_b in the value group, inside B_b, such that g^*t_b has an analytic m_b-th root on the **whole** inverse image of A_b = {r_b < abs(t_b) < R_b}. Put U = X_Ω^an minus the closed discs {abs(t_b) ≤ r_b}. Then there are a smooth proper connected V_Ω, a finite étale surjective V_Ω → Y and an analytic map (V_Ω^an) restricted over U → C_Ω^an over X_Ω^an. | Verified: over g^{-1}(A_b) the pulled-back cover is Z^{e_c} = g^*t_b, split by the given root; glue with the trivial cover over the discs; algebraize by GAGA; take a component. |
| Lemma 3.3 | In 3.2, if V_Ω → X_Ω is, over X_Ω, the base change of a finite V → X_k̄ (V smooth proper connected), ξ ∈ U, and k̄(V) has a K0-embedding into H, then k̄(C) has a K0-embedding into H. | Verified (an H-valued point of V_Ω over the fixed H-point of X_Ω is carried by the analytic map to an H-valued point of C_Ω over it; finiteness of C → X_k̄ makes its support generic). |
| Lemma 3.4 | Fix n ≥ 1. Among finite extensions of K0, "all horizontal indices divide n" is preserved by subextensions, finite composita, Galois closures, normalized pullback along finite morphisms of smooth proper curves, and composition on top with a finite étale cover. Hence every finite cover of X_k̄ with indices dividing ℓ has a K0-embedding of its function field into L_ℓ. | Verified (local fields k̄((t)), residue characteristic 0, cyclic extensions). |
| Lemma 4.1 | An analytic unit on an open disc over Ω has constant absolute value in the value group. On an open annulus A = {r < abs(S) < R} every unit is u = c S^d (1+h), c ∈ Ω^×, d ∈ Z, abs(h) < 1 pointwise; 1+h has an analytic ℓ-th root on A; so u has an ℓ-th root on any analytic cover of A on which S has one. | Verified (standard). |
| Lemma 4.2 | C/Ω smooth proper connected of genus ≥ 2 with its stable skeleton; A a node annulus with coordinate S. Then there is a connected finite étale C' → C such that S has an analytic ℓ-th root on the entire inverse image of A; one cover serves finitely many node annuli. | Construction verified: a degree-ℓ tame covering of the metrized complex, expansion factor ℓ along a simple circuit through the edge (cyclic ℓ-covers of the residue curves totally ramified at the two circuit marks, from ℓ-divisibility of Pic^0), ℓ identity copies elsewhere; separating edges first made non-separating by an unramified degree-ℓ covering. Uses ABBR Thm 7.7 (**checked**, with Definitions 2.19, 2.21: conditions (1)–(3) and vanishing ramification divisor hold for the construction). |
| Lemma 4.3 | C/k̄ smooth proper connected of genus ≥ 2; distinct b_1..b_s ∈ C(k̄); small disjoint coordinate discs B_i with coordinates t_i defined over k̄. Then there are a connected finite étale Y → C_Ω and concentric collars A'_i = {r_i < abs(t_i) < R_i} ⊂ B_i such that t_i has an analytic ℓ-th root on the entire inverse image of A'_i in Y^an. | Verified, given the resolution-of-nonsingularities input: blow up a semistable model at the sections to create node annuli inside B_i; take a finite étale cover Y_0 whose **stable** model maps to that model (Mochizuki–Tsujimura Prop. 2.4 (iv), **checked**); at an irrational level a inside the target annulus every point above lies in a source node annulus over the target node (type-2 points and disc tubes give rational values); compactness gives a collar; apply 4.2 to the source node annuli and 4.1. |
| Prop 4.4 | L_ℓ ⊂ H ("first stage"). | Verified: 3.1 + 4.3 (roots of order ℓ) + 3.2 + descent of finite étale covers from Ω to k̄ (SGA 1 X 1.8) + 3.3 + normality. |
| Lemma 5.1 | J an abelian variety over Ω with analytic uniformization q: T^an → J^an, T a split torus, kernel Λ a free lattice acting by translation, q a topological covering and local analytic isomorphism; a: A → T^an analytic; m ≥ 1; B = A ×_{q∘a, J^an, [m]} J^an. Then for every character χ of T the pullback of χ∘a to B has an analytic m-th root (no condition p ∤ m). | Verified (local lifts t of the projection to J; t^m/a ∈ Λ locally constant; normalize on the clopen pieces indexed by Λ/Λ^m; glue because Λ is torsion-free). |
| Prop 5.2 | m ≥ 1; D an integer > v_p(m) + 1/(p−1); α ∈ k^× with a = v(α) > 2D. Then there are a smooth proper connected Q/k and a finite Q → P^1_k with ramification indices dividing ℓ such that the pullback of the coordinate T has an analytic m-th root on the entire inverse image, over Ω, of {D < v(T) < a − D}. | Verified: Z: y^ℓ = T(T−1)/(T−α), genus ℓ−1, stable model two rational components joined by ℓ nodes of thickness a (checked by reduction on both components); Jacobian totally degenerate; on each node annulus A_j the character of the cycle e_j − e_j' composed with the lifted Abel–Jacobi map is a unit of slope 1 (Baker–Rabinoff Prop. 6.1, Cor. 6.6, **checked**), so equals c'T(1+h_j) with abs(h_j) < p^{−D} on the middle collar; pull back by [m] on the Jacobian (5.1); (1+h_j)^{1/m} by exp(log/m). |
| Proof of Thm 1.2 (Section 6) | For a finite Galois F/K0 with branch set B ≠ ∅: pull the covers Q of 5.2 (m = m_b = lcm of the indices over b) back along T = t_b/β_b: X_k̄ → P^1, take the compositum W (indices divide ℓ by 3.4), apply 3.2 with Y = W_Ω, descend V_Ω → W_Ω to V → W; k̄(V) ⊂ L_ℓ ⊂ H by 4.4; 3.3 gives F → H; normality gives F ⊂ H. | Verified. The image of an embedding F → H ⊂ E over K0 is the chosen copy of F because the elements of E algebraic over K0 are exactly K^sep (characteristic 0) and F/K0 is normal. |
| Cor 7.1 | k, X as above; w̃ a real-valued rank-one valuation of K̃ extending the p-adic valuation, w^sep a prolongation to K^sep. Then restriction D_{w^sep}(K^sep/K) → D_{w̃}(K̃/K) is an isomorphism of profinite groups. | Verified from Thm 1.2 (an element of the kernel is an isometry fixing a dense subfield of H ⊇ K^sep). |
| Lemma 7.2 | For every rank-one valuation w of K extending the p-adic valuation and every prolongation w̃ to K̃, D_{w̃}(K̃/K) → G_k has no continuous section. | Verified: lift by 7.1 to a section of G_K → G_k; Koenigsmann puts its image in the decomposition group of a k-rational point a (**checked**); the fixed field then carries two inequivalent henselian rank-one valuations and is not separably closed; contradiction by F. K. Schmidt's theorem, proved inline by an explicit square-root argument (q_r = d + (1−d) z^r/(1+z^r), z = p^N/t), which I checked, p = 2 included. |
| Surjectivity in 1.1 | Pop–Stix Thm 26 (**checked**) gives a valuation w̃ of K̃ above p with s(G_k) ⊂ D_{w̃}. Rank ≤ 2. Rank one: excluded by 7.2. Rank two: the rank-one coarsening is either above p (excluded by 7.2) or trivial on k, hence ord_a for a closed point a; s surjects onto G_k, so k(a) = k and s = s_a (Pop–Stix 6.1, **checked**). | Verified; the case analysis by rank is complete. |
| Injectivity in 1.1 | Kummer theory on the Jacobian: equal classes ⇒ i_a(b) ∈ ∩ nJ(k) = 0 because J(k) has an open subgroup ≅ Z_p^{g[k:Q_p]}; then a = b since genus ≠ 0. | Verified (the classical argument; also Stix 2008, Thm 45 and Remark 46). |
| Prop 8.1 | C/K smooth proper geometrically connected of genus ≥ 2 over a number field. Then loc(Sec(C/K)) = C(A_K)_•^{f-cov} (the set of modified adelic points surviving every torsor under a finite K-group scheme). | Verified from Thm 1.1, the real section theorem (**checked**: Bresciani–Vistoli, Mochizuki Cor. 3.13) and Harari–Stix Thm 2.1 with U = 1, S = ∅ (**checked**). |
| Thm 8.2 | If C(A_K)_•^{f-cov} = C(K), then C(K) → Sec(C/K) is bijective. | Verified: 8.1 + Stix 2015 Cor. 5 (a non-cuspidal Selmer section with finite support comes from a rational point; **checked**) + local injectivity. |
| Cor 8.3 | Bijectivity if (i) there is a non-constant K-morphism C → A, A an abelian variety with A(K) finite and Sha(A/K)_div = 0, or (ii) J(K) finite and Sha(J/K)_div = 0. | Stoll Thm 8.6 and Cor. 8.1 (**checked**, in the author's revised preprint) + 8.2. |
| Cor 8.4 | C/Q with a non-constant Q-morphism to an elliptic curve E with p^∞-Selmer corank 0 at one prime p: bijective. | Depends on another unrefereed OpenAI paper ("The Selmer converse for elliptic curves at every prime", 7 Oct 2026). **Not checked.** |
| Cor 8.5 | X_0(N)/Q and X_1(N)/Q of genus ≥ 2: bijective. | Stoll Cor. 8.8 (**checked**: "If C/Q is one of the modular curves X_0(N), X_1(N), X(N) and such that the genus of C is positive, then C is excellent w.r.t. abelian coverings") + 8.2. |
| (8.4) and the last paragraph | Every ordinary adelic representative of a localization tuple survives linear descent and lies in the Brauer–Manin set; if K contains no CM subfield, loc_v(Sec(C/K)) ⊂ C(K_v) is finite for every finite v. | Harari–Stix Cor. 3.1, Thm 4.1 (statements seen, **checked**); Betts–Stix Thm A (Annals 2025) **not checked**. |

**Architecture.** Collar roots → patching → density → decomposition groups → birational lift → two valuations.

- Stage 1 (ℓ-th roots, ℓ ≠ p): 4.1 → 4.2 (ABBR lifting) → 4.3 (resolution of nonsingularities) → 3.1 + 3.2 + 3.3 → 4.4: L_ℓ ⊂ H.
- Stage 2 (m-th roots, any m, p | m allowed): 5.1 + 5.2 (a Mumford curve and multiplication by m on its Jacobian) → pullback to X, composita (3.4) → 3.2 + 3.3 with Stage 1 → Thm 1.2: K^sep ⊂ H.
- Section 7: Thm 1.2 → Cor 7.1 → Lemma 7.2 (Koenigsmann + two henselian valuations) → Thm 1.1 with Pop–Stix localization.
- Section 8: Thm 1.1 + real case + Harari–Stix → Prop 8.1; + Stix's finite-support theorem → Thm 8.2; + Stoll → Cor 8.3–8.5.

**External theorems the proof of Theorems 1.1 and 1.2 rests on.**

| Citation as the paper gives it | Used in | The cited statement, and whether it is what the paper says |
|---|---|---|
| [17] Mochizuki–Tsujimura, *Resolution of nonsingularities, point-theoreticity, and metric-admissibility for p-adic hyperbolic curves*, RIMS Preprint 1974, revision of 30 March 2024, Thm A and Prop. 2.4 (iv) | Lemma 4.3 | **Checked** (author's page). Thm A: "Suppose that Σ ⊆ Primes is a subset of cardinality ≥ 2 that contains p, and that K is a p-adic local field. Let X be a hyperbolic curve over K; L a mixed characteristic complete discrete valuation field of residue characteristic p that contains K as a topological subfield. Then X_L satisfies Σ-RNS if and only if the residue field of L is algebraic over the finite field of cardinality p." Prop. 2.4 (iv): "Suppose that X satisfies Σ-RNS. Let 𝒳 be a compactified model of X over O_K. Then, after possibly replacing K by a suitable finite extension field of K, there exists a connected geometrically pro-Σ finite étale Galois covering Y → X over K, together with a compactified stable model 𝒴 of Y over O_K, such that the covering Y → X extends to a morphism 𝒴 → 𝒳." This is exactly the form used. Status of [17]: a 103-page preprint; I did not read its proof. |
| [1] Amini–Baker–Brugallé–Rabinoff, *Lifting harmonic morphisms I*, arXiv:1303.4812v3, Thm 7.7 | Lemma 4.2 | **Checked.** "Let (X, V ∪ D) be a triangulated punctured K-curve, let Σ = Σ(X, V ∪ D), and let φ: Σ' → Σ be a tame covering of Λ-metrized complexes of k-curves. Then there exists a tame covering (X', V' ∪ D') → (X, V ∪ D) of triangulated punctured K-curves lifting φ." With D = ∅ the lift is branched nowhere (their Theorem B: "branched only over D"). |
| [3] Baker–Rabinoff, arXiv:1308.3864v1, Prop. 6.1, Cor. 6.6, §§4.1–4.2, 4.5.2 | Prop 5.2 | **Checked** (Abel–Jacobi commutes with retraction to the skeleton; the skeleton of J is Jac(Γ) with the edge-length pairing; the uniformizing torus has character lattice H_1(X^an, Z)). |
| [22] Pop–Stix, arXiv:1111.1354v1, Thm 26 and Section 6.1 | Surjectivity | **Checked.** Thm 26: "Let X be a smooth, hyperbolic, geometrically connected curve over a finite extension k of Q_p. Then for any section s of π_1(X/k) there exists a valuation w̃ ∈ Val_v(K̃), such that the image s(Gal_k) is contained in the decomposition subgroup D_{w̃ over w}." 6.1: if w is of type 2h then s = s_a with a ∈ X(k); "The p-adic section conjecture thus reduces to the task of eliminating valuations w ∈ Val_v(K) of type other than 2h in Theorem 26." |
| [13] Koenigsmann, arXiv:math/0305226v1, Prop. 2.4 (2), Def. 1.4, Obs. 1.3 | Lemma 7.2 | **Checked.** Prop. 2.4: "Let K be a p-adically closed or real closed field. Then: 1. bsp(X/K) holds for all smooth complete curves X/K. 2. BSP(X/K) holds for all smooth complete curves X/K iff K is a local field, i.e. K is a finite extension of Q_p or K = R." BSP: all sections of G_{K(X)} → G_K are geometric; Obs. 1.3: geometric iff the image lies in a decomposition subgroup of a point of X(K̄), and then the point is K-rational (characteristic 0). |
| [24] F. K. Schmidt 1933 (a field henselian for two independent valuations is separably closed) | Lemma 7.2 | Not consulted; not needed, since the paper proves the instance it uses, and I verified that proof. |
| [20] Poineau (GAGA for finite algebras on proper Berkovich curves), [29] Temkin (étaleness and H-points after analytification), [10] SGA 1 X 1.8, [2] Baker–Payne–Rabinoff, [16] Milne, [23], [6], [5] (uniformization of abelian varieties) | 3.2, 3.3, 4.x, 5.2 | **Not checked**; all are standard statements used in their standard form. |
| [11] Harari–Stix (author preprint of 11 Feb 2011), Thm 2.1, Rem. 2.2 (1); [25] Stix, arXiv:1203.3236v3, Cor. 5; [26] Stoll (revised preprint), Cor. 8.1, Thm 8.2, Thm 8.6, Cor. 8.8; [8] Bresciani–Vistoli, arXiv:2012.06278v2 | Section 8 | **Checked** (statements quoted in Part 2, items 5 and 7, and in 1.C). |
| [4] Betts–Stix, [7] Bresciani (toric sections), [19] Pajwani, [21] Pop, [28] Tamagawa, [14] Lepage, [18] OpenAI (Selmer converse) | Introduction; Cor 8.4; last paragraph of 8.3 | **Not checked**; none enters Theorems 1.1, 1.2, 8.2, Cor. 8.5. |

**Assessment of the proof.** I found no gap and no error in the paper's own arguments; every lemma and every
step of Sections 3–7 was followed and is correct as written, and the eight citations that carry weight were compared
with the cited texts. What I could not certify: the proof of the Mochizuki–Tsujimura theorem (the one deep external
input that is itself recent and, to my knowledge, unrefereed), and the standard foundational citations marked "not
checked". Three remarks on why the result is consistent with what was known:

1. The mechanism is the known p-adic one. A finite étale cover of X can restrict over a small disc to a cover whose
   skeleton meets the disc (resolution of nonsingularities; such a restriction has degree divisible by p, since a
   connected Galois cover of a disc has no non-trivial quotient of order prime to p), and on node annuli of stable models tame covers ramified "along the skeleton" exist (Lemma 4.2).
   Roots of order divisible by p come from multiplication by m on a totally degenerate Jacobian, as on a Tate curve.
2. Known non-geometric sections live on quotients where the argument is not available: Hoshi's pro-p sections
   (Publ. RIMS 46 (2010) 829–848; Hoshi–Tsujimura RIMS-1950, 2021: Stage 1 needs a prime ℓ ≠ p) and Saïdi's sections
   of geometrically metabelian and nilpotent-by-abelian quotients over p-adic fields (arXiv:1510.06864,
   arXiv:2109.14882: the covers used here are not of bounded solvable length). No contradiction.
3. Mochizuki–Tsujimura themselves (Theorem F (i) of [17]) prove, for a section of a proper hyperbolic curve over a
   p-adic field, that it fixes exactly one point of the pro-Berkovich space of the universal cover and that it "arises
   from an Ω^H-rational point ... if and only if its image is a maximal stabilizer" of a point. The 2026 paper
   closes exactly that last gap, by showing (Cor. 7.1) that the stabilizer of a point of type 2, 3 or 4 is the full
   birational decomposition group, where Koenigsmann's theorem applies.

The paper has no formal (Lean) proof and no referee; treat Theorem 1.1 as claimed, with a proof that survives a
careful reading.

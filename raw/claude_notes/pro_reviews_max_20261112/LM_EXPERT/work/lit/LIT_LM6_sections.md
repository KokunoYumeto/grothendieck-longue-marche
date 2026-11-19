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

### 1.B The companion: *Étale covers with a prescribed exterior sheet* (OpenAI, 24 September 2026, 7 pp.)

It is not cited by the main paper and is not used in the proof of Theorems 1.1 and 1.2; it is an earlier,
independent consequence of the same resolution-of-nonsingularities input.

| No. | Statement (hypotheses in full) | Verdict |
|---|---|---|
| Thm 1.1 | k/Q_p finite, Ω the completion of k̄; X/k̄ smooth proper connected of genus ≥ 2; distinct b_1..b_d ∈ X(k̄) (d ≥ 1) with rational local parameters t_i; pairwise disjoint open discs B_i = {abs(t_i) < R_i}; radii r_i in the value group, 0 < r_i < R_i; V_i = {abs(t_i) < r_i}; U = X^an minus the V_i, assumed non-empty with an Ω-rational point. Then there are a smooth proper connected Y/k̄ and a finite étale surjective g: Y → X such that (i) a connected component of g^{-1}(U) maps isomorphically to U; (ii) for every i, every connected component of g^{-1}(V_i) maps to V_i with degree divisible by p. | Proof verified (below), given the positive-genus form of resolution of nonsingularities. |
| Lemma 2.1 | f: C → X connected finite étale Galois with group G; D = U or some V_i. Every component of f^{-1}(D) is finite étale and surjective over D; G is transitive on components; a component with stabilizer B has degree order(B). | Verified. |
| Prop 2.2 | There is a connected finite étale Galois Z → X whose stable skeleton contains, for each i, an embedded circle lying entirely above V_i. | Verified: two positive-genus stable vertices above V_i (input), a skeletal path between them above V_i, an F_ℓ-torsor on the special fibre connected on the two end components (surjectivity of H^1 of the special fibre onto the H^1 of the normalized components; lifting by SGA 1 IX 1.10), Betti number of the inverse graph ≥ ℓ − 1 > 0; Galois refinement keeps a circle. |
| Lemma 3.1 | For every i there is a connected cyclic finite étale cover of Z of degree p, trivial over all of U_Z = Z^an ×_{X^an} U, whose restriction to at least one component above V_i is connected. | Verified: a cyclic degree-p covering of the skeleton cut at a type-3 point of the circle (retraction fibre a single point, so the image of U_Z avoids the cut); topological coverings of a Berkovich curve are analytic (de Jong, Lemma 2.6) and algebraize. |
| Section 4 | Proof of Thm 1.1: T = a component of the fibre product of all conjugates, G = Gal(T/X), P = Gal(T/Z) elementary abelian p; H = stabilizer of a component over U; H ∩ P = 1; B ∩ P ≠ 1 for every stabilizer B of a component over V_i; Y = T/H. | Verified (degree of the image of a component with stabilizer B is [B : B ∩ H]; it is 1 for B = H and divisible by order(B ∩ P) over V_i). |

External input: the "alternative formulation" of Σ-RNS stated before Theorem A of Mochizuki–Tsujimura (**checked**,
verbatim: "Let 𝒵 be a compactified model of Z over O_K; z ∈ 𝒵_s a closed point. Then, after possibly replacing K by a
suitable finite extension field of K, there exist a connected geometrically pro-Σ finite étale Galois covering
Y → Z ..., a compactified stable model 𝒴 of Y ..., a morphism 𝒴 → 𝒵 ... that restricts to the finite étale Galois
covering Y → Z, an irreducible component D of 𝒴_s whose normalization is of genus ≥ 1, and whose image in 𝒵_s is
z"), Baker–Payne–Rabinoff (skeleta and models; not checked), de Jong, Poineau, SGA 1 (not checked).
Assessment: correct as far as I can check; no gap found. Relation to Bresciani's theorem that a non-geometric
section has a neighbourhood of index divisible by p (quoted in the main paper's introduction): the companion gives
covers with p dividing the degree over every disc while one exterior sheet is kept; it is not a statement about
sections.

### 1.C What family 019 gives, and does not give, for La Longue Marche

**Given (claimed).**
1. The local p-adic section conjecture for **proper** curves of genus ≥ 2 over **finite extensions of Q_p**
   (Thm 1.1): in his language (2:sc63–64, case III of §8 with I = ∅), the map from K-points to π-conjugacy classes
   of splittings of E → Γ is bijective when Γ = G_k and X is complete of genus ≥ 2.
2. Decomposition groups in π_1(X) of rank-one valuations above p equal the birational ones (Cor. 7.1), and none of
   them contains a section image (Lemma 7.2). Every section is therefore birationally liftable.
3. Over a number field K, for proper C of genus ≥ 2: every section is a Selmer section (locally a point at every
   finite place by Thm 1.1, a component at every real place), and loc(Sec(C/K)) = C(A_K)_•^{f-cov} (Prop. 8.1).
   Hence the exact equivalence, in both directions:
   **the section conjecture holds for C/K if and only if C(A_K)_•^{f-cov} = C(K)** ("C is excellent with respect
   to all coverings" in Stoll's terms; ⇐ is Thm 8.2; ⇒: if every section is s_a, then loc(Sec) = C(K), and Prop. 8.1
   gives the equality). Stoll's Remark 8.9 had the implication ⇒ under the section property.
4. The section conjecture for the curves where that equality is a theorem: a non-constant map to an abelian variety
   with finite Mordell–Weil group and Sha_div = 0; Jacobian with these properties; X_0(N), X_1(N) of genus ≥ 2 over Q.
   For these his finiteness statement of 2:sc65 (finitely many π-classes of splittings) is a theorem (the classes
   are the rational points).
5. Finiteness of the local images loc_v(Sec(C/K)) when K has no CM subfield (Betts–Stix with item 3). With
   Porowski's theorems (arXiv:2509.15660; arXiv:2607.27746, Thm 1.5) a section is determined by its reductions at
   any set of places of strongly positive density. Finiteness of Sec(C/K) itself does not follow: what is missing is
   injectivity (or finite fibres) of loc_v at one place.

**Affine curves and cuspidal sections: not in the paper, but they follow.** Let U = X ∖ S be hyperbolic over a
finite k/Q_p, s a section of π_1(U) → G_k. For open H ⊇ s(G_k) let U_H be the cover and X_H its smooth completion.
The H with genus(X_H) ≥ 2 are cofinal (take H = N·s(G_k) with N characteristic open in the geometric group). By
Thm 1.1 the section induced on X_H is s_{x_H} for a unique x_H ∈ X_H(k); uniqueness makes (x_H) a compatible
system. The fibres of the pro-system of compactified geometric covers over the x_H are non-empty profinite sets, so
there is a point ỹ over all x_H; for γ ∈ s(G_k), γỹ and ỹ have the same image in every X_H, i.e. γỹ ∈ (H ∩ π̄)ỹ for
all H, and ∩(H ∩ π̄) = 1, so γỹ = ỹ. Hence s(G_k) lies in the decomposition group of ỹ, and s is the section of a
point of U(k) or a cuspidal section at a point of S(k). (This is the standard neighbourhood argument: Tamagawa;
Stix, arXiv:1203.3236, 2.1.2 and the proof of Cor. 5.) Injectivity and disjointness of the packets hold over local
fields (Stix, arXiv:0809.0017, Thm 14 with Remark 15 (2) and Thm 45, Remark 46). So, granted Thm 1.1:

> for every hyperbolic curve U over a finite extension k of Q_p,
> U(k) ⊔ ⊔_{y ∈ S(k)} {classes of sections of π_1(U_y) → G_k} → {classes of sections of π_1(U) → G_k} is bijective,

which is his corrected conjecture of 2:sc79 with K replaced by k, and the packet at y is a torsor under
H^1(k, Ẑ(1)) = the profinite completion of k^× ≅ Ẑ × O_k^×. The map Θ: k^× → H^1(k, Ẑ(1)) **is injective** for
such k (k^× ≅ Z × finite × Z_p^n has no non-trivial divisible element); its cokernel is Ẑ/Z. (Over R it is not
injective: H^1(R, Ẑ(1)) = Z/2.)

**Not given.**
- Number fields in general: only the equivalence of item 3; the equality C(A_K)_•^{f-cov} = C(K) "remains a separate
  arithmetic hypothesis" (the paper's words).
- Genus 0 and 1. For genus 1 the statement is false over p-adic fields: sections of π_1(E) → G_k are H^1(k, T E),
  and E(k) → H^1(k, TE) is injective with cokernel the Tate module of H^1(k, E) ≅ Hom(E(k), Q/Z), which contains
  Z_p^{[k:Q_p]}. Punctured genus 0 and genus 1 curves that are hyperbolic are covered by the affine statement above.
- Fields other than finite extensions of Q_p: nothing for finitely generated extensions of Q_p, for p-adically
  closed fields that are not local (there the birational statement fails: Koenigsmann Prop. 2.4 (2)), or for
  function fields.
- Relative versions (his family over a base, 2:sc433–436): nothing.
- Quotients of π_1: nothing; and the statement is false for the pro-p and the geometrically metabelian quotients
  (Hoshi; Saïdi; Part 2, item 7).
- His characterization by Ker χ (letter to Faltings, PS; 2:sc431–433 "peut-être même π^{Γ⁺} = 1"): untouched.
- The Hom-form and Isom-form: untouched (they are Mochizuki's and Tamagawa's).

---

## Part 2. Primary sources

All paths are under `Free or receipted\free\lm-expert-20261112\`.

### 1. Grothendieck, *Brief an G. Faltings*, 27 June 1983

- Source: German text as printed in *Geometric Galois Actions 1* (LMS Lecture Note Series 242, 1997, pp. 49–58),
  copy at `https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/Letters/GanF.pdf` (the Grothendieck Circle,
  page of L. Schneps, co-editor of the volume; the editors' note says Faltings gave permission to reproduce it).
  This is an editor's page, not the author's; the shelf already holds EGA and FGA from the same host. Local:
  `grothendieck-faltings-1983\grothendieck_brief_an_faltings_GanF.pdf`. Read in full.
- **The conjecture (7), p. 54.** For an anabelian curve X over an "absolute" field K (finitely generated over the
  prime field; characteristic 0 assumed): "Es sei Γ(X/K) die Menge aller K-wertigen Punkte (also 'Schnitte') von X
  über K, man betrachtet die Abbildung (7) Γ(X/K) → Hom ext_{π_1(K)}(π_1(K), π_1(X)), wo die zweite Menge also die
  Menge aller 'Spaltungen' der Gruppenerweiterung (3) ist ..., oder vielmehr die Menge der üblichen
  Konjugationsklassen solcher Spaltungen via Aktion der Gruppe π_1(X̄). Es ist bekannt, dass (7) injektiv ist, und die
  Hauptvermutung sagt aus, dass sie bijektiv ist. [siehe unten Berichtigung]"
- **Third formulation and the correction, pp. 56–57.** With X̃ the universal covering and X̃^ its normalized
  completion: for a given splitting, "Die Vermutung ist nun, dass letztere Aktion (genau) einen Fixpunkt besitzt"
  (on X̃^(K̄)). Then: "die Formulierung von der Hauptvermutung via (7) ... nur im Fall wo X eigentlich ist eine
  korrekte ist ... Im Falle hingegen, wo X nicht eigentlich ist, also 'unendlich ferne Punkte' besitzt, so liefert
  jeder dieser Punkte auf naheliegende Weise ein erkleckliches Paket von Spaltungsklassen (deren Mächtigkeit das des
  Kontinuums ist), die sich nicht durch im endlichen liegende Punkte erhalten lassen. Diese entsprechen dem Fall
  eines Fixpunktes in X̃^, der nicht in X̃ liegt. Die Einzigkeit des Fixpunktes besagt unter anderen, ausser der
  Injektivität von (7), dass die 'Pakete', die verschiedenen Punkten im Unendlichen entsprechen, leeren Durchschnitt
  haben, also dass jede Spaltungsklasse, die keinem endlichen Punkt entspricht, einem eindeutig bestimmten Punkt im
  Unendlichen entspringt."
- **The PS, p. 58: a group-theoretic characterization of the image of (7)** ("mutmasslich ... in beiden
  Richtungen"): with π_1(K)° = Kern von π_1(K) → Ẑ^* (cyclotomic character): for a splitting, "π_1(K)° operiert auf
  π_1(X̄) ... Die Bedingung ist nun, dass die Fixpunktgruppe dieser Aktion nur aus 1 bestehen soll!"
- **On injectivity, p. 52:** "Der Beweis ergibt sich ziemlich einfach aus dem Mordell–Weilschen Satz, dass die Gruppe
  A(K) ein endlich erzeugter Z-Modul ist, wo A die 'jacobienne généralisée' von Y ist".
- Bears on: F7, H5; 2:sc63–64 (case III), 2:sc77–79, 2:sc431–433.
- Verdict: **confirms** F7. The 1981 text (2:sc77–79) already has the 1983 conjecture in the same form: at each
  rational point at infinity a torsor of classes under H^1(K, T(G_m)) = lim K^×/n ("famille transcendante"; in 1983
  "Paket ... Mächtigkeit des Kontinuums"), the classes for distinct points at infinity distinct, and "peut-être n'y
  a-t-il pas d'autres scindages" = existence of the fixed point. Both take the **whole** packet, not only its
  K^×-subtorsor of tangential sections. Two corrections to carry: (a) in both texts the injectivity is credited to
  "G(K) (resp. A(K)) de type fini" for the generalized Jacobian; this is false when the toric part is non-trivial
  (K^× is not finitely generated); what is true and suffices is that G(K) has no non-trivial divisible element
  (item 3). (b) The criterion of the PS is the precise form of his "peut-être même π^{Γ⁺} = 1" (2:sc433) and of
  "π̂_{0,3}^{Γ''⁺} = 1" (2:sc480–482); the weaker condition π^Γ = 1 does not separate points from cusps (item 6).

### 2. Cuspidal sections and tangential base points

**Stix, *On cuspidal sections of algebraic fundamental groups*, arXiv:0809.0017v1 (2008).** Local:
`stix-cuspidal\`. k of characteristic 0, U = X ∖ Y a curve, U_y the scheme of nearby points at y ∈ Y.
- Definition (1.3): "A cuspidal section of π_1(U/k) is a section that factors over some π_1(U_y) for a point y ∈ Y
  with residue field κ(y) = k." "There is also a version of the section conjecture for affine curves stating that
  all but cuspidal sections come from rational points."
- Prop. 8: "The extension π_1(U_y/κ(y)) splits and there is a natural free transitive action on S_{π_1(U_y/κ(y))} by
  [the pro-N completion of] κ(y)^*" (= H^1(κ(y), Ẑ(1))).
- For U hyperbolic. Prop. 11: inertia groups at distinct cusps of the universal cover meet trivially. Cor. 12: "The
  normalizer of I_{ỹ/y} in π_1(U ⊗ k^alg) (resp. π_1(U)) are I_{ỹ/y} (resp. D_{ỹ/y})." Cor. 13: "Let A be an abelian
  subgroup of π_1(U) that nontrivially intersects an inertia subgroup I_{ỹ/y}. Then A is contained in I_{ỹ/y}."
- Thm 14: "Let us assume that the injectivity part of the section conjecture holds for proper curves of genus at
  least 2 over finite extensions of k. Then the following holds. (1) A cuspidal section uniquely determines the cusp
  y for which it factors over π_1(U_y). (2) Let y be a k-rational cusp of U. The natural map S_{π_1(U_y/k)} →
  S_{π_1(U/k)} is injective and the image disjoint from the sections induced by rational points u ∈ U(k) or cuspidal
  sections originating from a different cusp." Remark 15: the image "is called the 'Paket' ... in [Gr83]"; the
  assumption holds when A(k) has no divisible elements for every abelian variety A/k.
- Thm 17 (abelianized extension): for k with non-trivial Kummer theory and (i) no non-trivial divisible torsion in
  A(k) or (ii) infinite Ẑ-rank of the completion of k^*: "The natural map S_{π_1(U_y/k)} → S_{π_1(U/k)} has
  uncountable image", already in the extension by π_1^ab.
- Thm 20 (Nakamura), Cor. 21, 22: for k that "distinguishes tori from abelian varieties" (Hom_{Gal_k}(T S, T A) = 0;
  e.g. number fields k with kQ^ab/Q^ab finite, Lemma 19) and U hyperbolic: a non-trivial closed subgroup lies in an
  inertia group iff it is pro-cyclic and (essentially) cyclotomically normalized; "the set of inertia subgroups in
  π_1(U) coincides with the set of maximal closed subgroups of π_1(U) among those which are pro-cyclic and
  cyclotomically normalized"; "A section s ∈ S_{π_1(U/k)} is cuspidal if and only if the image s(Gal_k)
  cyclotomically normalizes a pro-cyclic subgroup of π_1(U)."
- Listed by Stix as missing (1.4): "(2) recognize tangential sections within cuspidal sections".

**Esnault–Hai, *Packets in Grothendieck's section conjecture*, arXiv:math/0703877v2 (2007).** Local: `esnault-hai\`.
- Conjecture 2.2 (their statement of the letter): U hyperbolic over k of finite type over Q. (SC1) U(k) → sections
  injective. (SC2) a geometric section has a unique fixed point on the compactified universal cover, above the
  point. "(SC3) For a non-geometric section, the resulting action of Γ on X(U_ū) has also a unique fixed point, which
  lies at infinity ..., and projects on a point in (X ∖ U)(k). This implies in particular that the set of non-geometric
  sections is divided into disjoint 'packets' P_x, x ∈ (X ∖ U)(k). (SC4) Each packet P_x has the cardinality of the
  continuum."
- Proved there: Thm 5.1 (SC1 for U "elliptic or hyperbolic" over k of finite type over Q; "The ellipticity
  assumption is sharp", A^1 fails); Prop. 5.3 (semi-abelian A/k: A(k) → classes of fibre functors injective, by
  "Since k is of finite type over Q, there are no k-rational points which are infinitely divisible"); Thm 5.5 (at
  most one fixed point); Thm 6.5 (for U hyperbolic over any k of characteristic 0, T_x = P_x: the packet at x is
  exactly the set of fibre functors coming from the punctured tangent space at x); Cor. 6.9 (for k of finite type
  over Q, P_x has the cardinality of the continuum). Open there: SC3 (existence of the fixed point).

**Deligne, *Le groupe fondamental de la droite projective moins trois points* (1989), §15 "Points base à l'infini".**
Source: IAS, `https://publications.ias.edu/sites/default/files/61_LeGroupeFondamentalDroite.pdf`; local `deligne-1989\`
(OCR text layer; §15 read, pp. 229–242 of the original). 15.13–15.26: for a curve X̄ over k of characteristic 0,
S finite, X = X̄ − S, s ∈ S, T_s the tangent space and T_s^0 = T_s − {0}: a functor R ↦ R^(s) from finite étale
covers of X to finite étale covers of T_s^0, by principal parts (15.14–15.15), valid over non-closed k (15.18), with
the algebraic form T_s^0 = Spec Gr(K_s) for the filtered local field (15.20–15.21) and the description through a
formal isomorphism φ of (T_s, 0) with (X̄, s) with φ'(0) = 1 (15.24–15.26). A k-rational non-zero tangent vector is
then a fibre functor on the covers of X, i.e. a base point "à l'infini" defined over k.
- Bears on: F7; 2:sc75–77 (his construction: a uniformizer t gives a section; t and tu, u ∈ 1 + m, give the same
  class; the classes form a torsor under H^1(k, T(G_m)); (m/m²)^* embeds as a Θ(k^*)-subtorsor).
- Verdict: **confirms** F7. His 1981 construction is Deligne's tangential base point (dependence only on the
  tangent vector = on t mod m²), and the two torsors are Stix's Prop. 8 and Esnault–Hai's Thm 6.5. **One
  correction to his text**: 2:sc79 says the classes for distinct points at infinity are distinct "même en se ramenant
  aux scindages correspondants de l'extension de Γ par π_ab". In the full group this is Stix's Thm 14. In the
  extension by π_ab it holds for genus ≥ 1 (the classes map to the classes of the distinct points y_i in the
  extension by π_ab(X), Jacobian argument) but **fails in genus 0**: on U = P^1 ∖ {0,1,∞} the abelianized class of a
  point x is (x, 1−x) ∈ (completion of K^×)², the packet at 0 is {(a, 1)}, the packet at 1 is {(1, b)}, and the
  tangential sections "0 towards 1" and "1 towards 0" both give (1, 1). (Equivalently: the Galois cocycle f_σ
  comparing these two base points lies in the closure of the commutator subgroup.) Within one packet the abelianized
  classes all coincide when ν = 1 (the loop subgroup dies in π_ab). So the abelianized form is true for distinct
  cusps when g ≥ 1, false in general when g = 0, and inside one packet it needs at least ν ≥ 2 (Stix's Thm 17 then
  gives an uncountable image under its hypotheses).

### 3. Injectivity of points → sections

- Stix, arXiv:0809.0017, Appendix B, Thm 45: "Let k be a field such that the group of k-rational points A(k) has no
  nontrivial divisible elements for any abelian variety A/k. Let x, y ∈ X(k) be k-rational points of a variety X/k
  that immerses into an abelian variety such that the associated sections s_x, s_y ∈ S_{π_1(X/k)} agree. Then x equals
  y." Remark 46: "The assumptions ... are valid for number fields (resp. local fields) by the Mordell–Weil Theorem
  (resp. compactness). In particular the injectivity part of the section conjecture holds for hyperbolic curves over
  such fields as the Albanese map is eventually an immersion for suitable finite étale covers."
- Esnault–Hai Thm 5.1 and Prop. 5.3 (item 2): k of finite type over Q; curves that are elliptic or hyperbolic
  (genus ≥ 1, or genus 0 inside G_m); semi-abelian varieties. This is exactly the generality of 2:sc64 ("g = 0 ⇒
  ν ≥ 2": no component isomorphic to P^1 or the affine line; G_m is allowed).
- Mochizuki, *The local pro-p anabelian geometry of curves* (1999), Thm 19.1 (sub-p-adic fields, complete curves of
  genus > 1): **primary not obtained in this fork**; quoted by Koenigsmann (Remark 1.2 (2)): "By Theorem 19.1 of
  [Mo], σ_{X/K} is injective for any smooth complete curve X of genus > 1 over a sub-p-adic field K".
- The 2026 paper's own proof for finite k/Q_p (Section 7).
- Verdict for 2:sc64: **confirms** the statement, **corrects** the reason: the input is "G(K) has no non-trivial
  divisible element" for the semi-abelian G (true for K finitely generated over Q: for the abelian quotient by
  Mordell–Weil–Lang–Néron, for the torus because K^× is a finitely generated group times a free abelian group, and
  the extension is handled by multiplying by the exponent of the torsion of A(K)); "G(K) de type fini" is false as
  soon as the torus is non-trivial. His excluded cases are g = 0 with ν ≤ 1 (not ν = 2).

### 4. The birational and the valuative theorems over p-adic fields

- Koenigsmann, *On the 'section conjecture' in anabelian geometry*, arXiv:math/0305226v1 (J. reine angew. Math. 588
  (2005)). Local: `koenigsmann-2005\`. Def. 1.1 (SP): σ_{X/K}: X(K^perf) → {non-branch sections}/conj. bijective,
  "where a section is called non-branch section, if the image is not in a decomposition subgroup of π_1(X) w.r.t. a
  branch point, i.e. a point in X̃ ∖ X". Prop. 2.4 (quoted in 1.A). Cor. 2.6: a section of G_{K(X)} → G_K over a
  number field K forces points over all completions. Lemma 1.7: for K finite over Q_p, finitely generated over Q, or
  finite, the (birational) section property for all curves is equivalent to the weak one for all curves (limit
  argument; Faltings or compactness).
- Pop, *On the birational p-adic section conjecture*, MPIM preprint 2007-102 (Compositio Math. 146 (2010)). Local:
  `pop-birational-2007\`. Thm A (k/Q_p finite containing μ_p, K the function field of a complete smooth curve X):
  "1) Every k-rational point x of X gives rise to a bouquet of liftable sections s_x: G'_k → G'_K. 2) Let s': G'_k →
  G'_K be a liftable section. Then there exists a unique k-rational point x of X such that s' equals one of the
  sections s_x", where ' is the maximal Z/p-elementary abelian quotient and "liftable" means liftable to the Z/p
  metabelian quotients.
- Pop–Stix, arXiv:1111.1354v1 (J. reine angew. Math. 725 (2017)). Local: `pop-stix-2011\`. Thm 26 and 6.1 (quoted
  in 1.A); classification of the valuations above p (Appendix A: types 1v, 2h, 2v, 2u); 6.2: the valuation given by
  Thm 26 is never of type "2u smooth".
- Mochizuki–Tsujimura [17], Thm F (i): for H ⊂ G_K closed with H ∩ I_K ↠ Z_l and a section s_X: H → Π_X^{(Σ)} of a
  proper hyperbolic curve defined over a p-adic local field: at most one fixed point in the pro-Berkovich space of
  the universal covering (exactly one if the l-adic cyclotomic character has open image on H); "s_X arises from an
  Ω^H-rational point ∈ X(Ω^H) if and only if its image is a maximal stabilizer ... of a point".
- Bears on: F7 (its sentence on 019), 2:sc63–64 over local fields. Verdict: **confirms** what F7 says about the
  local theorem and its ingredients.

### 5. The real section conjecture

- Mochizuki, *Topics surrounding the anabelian geometry of hyperbolic curves* (2003), §3 (author's page; local
  `mochizuki-topics\`).
  - Thm 3.6 ("General Discrete Real Section Conjecture"): (X, ι) a real complex manifold with an ι-invariant metric
    whose universal cover satisfies (*): "the correspondence Y ↦ ι_Y defines a bijection π_0(X(R)) ≅
    Hom_{Gal(C/R)}(Gal(C/R), π_1(X^ι)) from the set of connected components of the real locus X(R) to the set of
    conjugacy classes of sections of π_1(X^ι) → Gal(C/R) (or, equivalently, involutions in π_1(X^ι)). Moreover, the
    centralizer of an involution ι_Y ∈ π_1(X^ι) is the image of π_1(Y^ι) in π_1(X^ι)."
  - Cor. 3.7: the same for every hyperbolic real Riemann surface (compact or not). Remark after it: "there is no
    discussion of 'tangential sections' ... every tangential section arising from a real point at infinity may be
    obtained as a limit of a sequence of real points that are not at infinity ..., hence is 'automatically
    included' in the connected component containing those real points."
  - Cor. 3.8: the same for the moduli stacks M_{g,r} (2g − 2 + r > 0), discrete groups: π_0(M_{g,r}(R)) ≅ classes of
    involutions of the extended mapping class group lying over complex conjugation, with centralizers.
  - Cor. 3.13 ("Profinite Real Section Conjecture for Real Hyperbolic Curves"): "Let X be a hyperbolic curve over R.
    Then ... π_0(X(R)) ≅ Hom_{Gal(C/R)}(Gal(C/R), π_1^alg(X))" (classes of sections). X need not be proper.
  - Cor. 3.15: the profinite statement with centralizers for M_{g,r}, g ≤ 2 only (goodness of the mapping class
    group is not known for g > 2).
- Stix, arXiv:0802.4125 (Amer. J. Math. 132 (2010)), Appendix A, Thm 26: "Let X/R be a smooth, projective curve of
  genus ≥ 1. Then the map π_0(X(R)) → S_{π_1(X/R)} ... is a bijection of finite sets." Local `stix-period-index\`.
- Bresciani–Vistoli, arXiv:2012.06278v2: "The real section conjecture holds for ... (1) Torsors for semiabelian
  varieties. (2) Smooth quasiprojective curves, with the exception of the projective curves of genus 0 without real
  points." Local `bresciani-vistoli\`; proof read.
- Pál (J. London Math. Soc. 83 (2011)), Wickelgren (Math. Ann. 358 (2014)), Esnault–Wittenberg (Mosc. Math. J. 9
  (2009), Remark 3.7 (iv)): **primaries not obtained**; their results are as summarized in the introduction of
  Bresciani–Vistoli (other proofs of the same bijection for curves).
- Bears on: H7, F7; his theorem of 2:sc440–445 (§33) and (29)–(30) of 2:sc377–378.
- Verdict: **confirms** H7 and sharpens it. (a) His §33 theorem (π_0(U^σ) ≅ classes of splittings over Z/2; the
  centralizer π^{σ_i} is 1 for a component ≅ R and Z for an oval) is Mochizuki's Thm 3.6 / Cor. 3.7 (2003), with the
  same centralizer statement; he proved it in 1981 modulo the lemma on anti-involutions of the disc. (b) The profinite
  bijection is a theorem for all hyperbolic real curves, affine included (Mochizuki Cor. 3.13; Bresciani–Vistoli).
  (c) **Correction to the picture with cusps**: over R all sections come from components of U(R); the packet at a
  real cusp has exactly two elements (H^1(R, Ẑ(1)) = Z/2, the two half-branches), and each is the class of the
  adjacent component of U(R). So "π_0(U(R)) ≅ non-cuspidal sections" is false; the non-cuspidal classes are the ovals
  of X(R) that carry no cusp. (d) Not found in the literature read: the profinite centralizers of the involutions for
  curves (expected 1 and Ẑ; Mochizuki states the profinite centralizer only for moduli in genus ≤ 2).

### 6. "Proper case plus cuspidal sections gives the affine case" (H5; his axiom ⑤, 2:sc418)

In the literature in substance, as the neighbourhood (limit) argument:
- Koenigsmann Lemma 1.7 and Def. 1.1 (statement for affine curves with non-branch sections);
- Stix, arXiv:1203.3236v3, 2.1.2 ("the limit argument") and the proof of Cor. 5: "The limit argument ... implies that
  s = s_a for any a ∈ im(X_s(k) → X(k)). Since we assumed s not to be cuspidal, we may even deduce that a ∈ X(k)
  [the open curve]";
- Bresciani, arXiv:2108.13397 (abstract): "the section conjecture is equivalent to the cuspidalization of all
  sections over all finitely generated fields";
- Steklov, arXiv:2602.17746v2, Introduction: the conjecture stated as bijectivity of
  V(k) ⊔ ⊔_{y ∈ Y(k)} S_{π_1(V_y/k)} → S_{π_1(V/k)}.
What is proved this way: if surjectivity holds for all proper curves of genus ≥ 2 over k (number field: with
Faltings' finiteness for the limit; local field: compactness), then every section of an affine hyperbolic curve over
k is the section of a point or cuspidal; the derivation is written out in 1.C for local fields. Together with Stix
Thm 14 (packets injective and disjoint) this is his ⑤ a), b), c) for a hole fixed by Γ. I did not find his axioms
①–⑥ themselves compared with the standard forms anywhere; that comparison is new work, but each arrow is of this
kind.
On "admissible = normalizes no loop subgroup": a section is cuspidal iff its image lies in D_ỹ = the normalizer of
I_ỹ (Stix Cor. 12), so every member of a packet, tangential or "transcendental", normalizes a loop subgroup; over
fields distinguishing tori from abelian varieties, cuspidal ⇔ cyclotomically normalizes a pro-cyclic subgroup
(Stix Cor. 22). So his admissible sections are exactly the non-cuspidal ones there. His rigidity condition
π^Γ = 1 holds for point sections and for cuspidal sections alike (for a cuspidal section the centralizer lies in
I_ỹ ≅ Ẑ(1), where Γ has no fixed point); only the kernel of χ sees the difference: Ker χ centralizes I_ỹ.
Verdict: **H5 confirmed in substance**; the equivalence with his axioms is to be written; his "π^Γ = 1" must be
replaced by "π^{Ker χ} = 1" (his own 1983 PS) wherever it is meant to exclude cusps.

### 7. Search for 2026 (and late 2025) results (claims, unchecked unless said)

Searched 12 Nov 2026 (web search; arXiv abstract pages read directly).
- **Steklov, *Fermat's Last Theorem for Selmer sections*, arXiv:2602.17746v2 (3 March 2026).** Introduction read.
  Thm A: "All Selmer sections s ∈ S_{π_1(V_ℓ/Q)} of the Fermat curve V_ℓ/Q are cuspidal for ℓ ≥ 7" (V_ℓ: X^ℓ + Y^ℓ + Z^ℓ
  = 0, XYZ ≠ 0; Selmer: rational or cuspidal at every place). Thm B: "The section conjecture for all hyperbolic curves
  over all finite extensions of k, implies the section conjecture for all hyperbolic DM-curves over k" (e.g. the
  moduli stack of elliptic curves). Thm C: for k sub-p-adic, "the fully faithfulness in the section conjecture holds
  for all hyperbolic DM-curves over k". **Consequence to check**: with Thm 1.1 of 019 and the affine derivation of
  1.C, every section over Q of an affine hyperbolic curve is a Selmer section, so every section of π_1(V_ℓ) → G_Q
  would be cuspidal for ℓ ≥ 7: the section conjecture for the affine Fermat curves, which is the statement behind
  his remark of 2:sc65 on Fermat.
- **Porowski, *On reductions of Selmer sections*, arXiv:2509.15660 (19 Sep 2025)**: "the conjugacy class of a
  noncuspidal Selmer section is uniquely determined by its reduction on a set of density one"; ***Families of curves
  separating points*, arXiv:2607.27746v1 (30 July 2026)**, Thm 1.5: for proper hyperbolic X with stable reduction
  over a number field, the reduction map on Selmer sections is injective for every set of places of strongly
  positive density; "It is an important open problem to show that the map red_Ω is injective whenever the set Ω is
  infinite".
- **Bresciani, *The section conjecture for the toric fundamental group over p-adic fields*, arXiv:2409.07923v5
  (14 Sep 2026)**: the analogue of the conjecture for the toric fundamental group over p-adic fields; "a new
  interpretation of Selmer sections as toric Galois sections".
- **Sun, *The absolute anabelian geometry of virtual curves of arbitrary genus*, arXiv:2604.23485 (26 April 2026)**:
  "group-theoretic conditions under which a section of an arithmetic fundamental group arises from a rational point"
  (abstract only).
- **Yamaguchi, arXiv:2601.07112v4 (24 May 2026)** (the item on the reading-list card): "the maximal m-step solvable
  quotients of the étale and tame fundamental groups of a hyperbolic curve over a separably closed field are
  torsion-free and center-free", m ≥ 2. (For F5, not for sections.)
- Older, needed as limits of what can be asked: Hoshi, *Existence of nongeometric pro-p Galois sections of hyperbolic
  curves*, Publ. RIMS 46 (2010) 829–848 (primary not obtained; cited from Hoshi–Tsujimura RIMS-1950 (2021), read:
  explicit non-geometric pro-p sections of punctured projective lines over finite extensions of Q and of Q_p; open:
  the same for an irregular prime); Saïdi, arXiv:1510.06864 and arXiv:2109.14882 (non-geometric sections of the
  "étale-by-geometrically abelian", geometrically metabelian and pro-nilpotent-by-abelian quotients over p-adic
  local fields; abstracts read).
- Not found: any independent check, erratum or public discussion of the OpenAI paper of 6 Oct 2026; any 2026 preprint
  by other authors claiming the p-adic or the global conjecture.

---

## Closing lists

### (i) The findings and hunches this literature step was for

| Entry | Verdict | What changes |
|---|---|---|
| **F7** (sections: his corrected conjecture of 2:sc79 is the section conjecture with cuspidal sections; the "famille transcendante" is the standard packet; injectivity by Mordell–Weil; what 019 claims and does not cover) | **Confirmed, with four corrections.** | (1) Citations: letter to Faltings pp. 54, 56–58; Stix arXiv:0809.0017 Prop. 8, Thm 14, Thm 17; Esnault–Hai Conj. 2.2, Thm 5.1, Prop. 5.3, Thm 5.5, Thm 6.5, Cor. 6.9; Deligne 1989 §15.13–15.26. (2) The reason for injectivity is "no divisible elements in G(K)", not "G(K) of finite type" (false with a torus). (3) His claim that packets of distinct cusps are already distinct in the extension by π_ab is false in genus 0 (P^1 ∖ {0,1,∞}: the tangential classes at 0 and 1 coincide abelianized); true for g ≥ 1. (4) "Not covered by 019: affine curves" is too weak a description: the affine local statement with packets follows from Thm 1.1 by the neighbourhood argument (1.C); and over number fields 019 gives the equivalence "section conjecture for C ⇔ C(A_K)_•^{f-cov} = C(K)". |
| **H5** (his admissible sections are the non-cuspidal ones; axioms ①–⑥ of §32 equivalent to the section conjecture for all open subcurves; ⑤ (c) = affine case from the proper case) | **Confirmed in substance; one correction.** | Admissible = non-cuspidal: Stix Cor. 12 and Cor. 22 (after Nakamura), over fields that distinguish tori from abelian varieties. ⑤ from the proper case: the neighbourhood argument (Koenigsmann Lemma 1.7; Stix arXiv:1203.3236, 2.1.2 and Cor. 5; Bresciani arXiv:2108.13397). Not in the literature: the comparison with his axioms as he states them. Correction: his rigidity condition π^Γ = 1 holds for cuspidal sections too; the condition that excludes cusps is π^{Ker χ} = 1 (his own PS of 1983; 2:sc433 "peut-être même π^{Γ⁺} = 1"), and that one is conjectural for point sections. |
| **H7** (§33 is the real section conjecture; profinite version known; real cuspidal packets; fixed groups) | **Confirmed; one correction.** | §33's theorem with centralizers = Mochizuki 2003 Thm 3.6, Cor. 3.7; profinite: Mochizuki Cor. 3.13 (all hyperbolic real curves), Stix 2010 Thm 26 (proper), Bresciani–Vistoli (quasi-projective curves, semi-abelian torsors). Correction: over R the cuspidal sections are not extra classes; the packet at a real cusp has two elements, the classes of the adjacent components of U(R). Still to prove: the profinite fixed groups (1 for a line, Ẑ for an oval). |

### (ii) For the LM6 Parts (`PUSH_REDO\LM6_PARTS_redo_20261112.md`): concrete changes, each with its reason

Opening paragraph of the Parts.
1. Say what Theorem 1.1 of the 2026 paper rests on, so that "check the step you rely on" has a target: Mochizuki–
   Tsujimura's resolution of nonsingularities (RIMS-1974, Thm A, Prop. 2.4 (iv)), the lifting theorem of
   Amini–Baker–Brugallé–Rabinoff (Thm 7.7), Pop–Stix Thm 26, Koenigsmann Prop. 2.4 (2). Reason: these are the only
   external inputs of weight (1.A); the paper's own steps check out.
2. Add to the tools, as statements to be derived in a few lines and then used: (a) for finite k/Q_p and every
   hyperbolic U, every section is the section of a point of U(k) or cuspidal, and the packets are disjoint torsors
   under the profinite completion of k^× (1.C); (b) for proper C of genus ≥ 2 over a number field, the section
   conjecture for C is equivalent to C(A_K)_•^{f-cov} = C(K) (1.C, item 3). Reason: both follow from the paper plus
   the standard neighbourhood argument, and several asks below are otherwise spent on them.
3. Add the known limits: non-geometric sections exist for the geometrically pro-p quotient (Hoshi 2010;
   Hoshi–Tsujimura 2021) and for the geometrically metabelian and nilpotent-by-abelian quotients over p-adic fields
   (Saïdi, arXiv:1510.06864, arXiv:2109.14882); over elliptic curves over p-adic fields the section map is not
   surjective. Reason: any "pro-ℓ form" or "modulo a metabelian quotient" fallback must not assume geometricity.

Part B.
4. B (a): cite as tools Stix (Prop. 8, Thm 14, Thm 17), Esnault–Hai (Thm 6.5, Cor. 6.9), Deligne §15; and change
   "Prove his assertion of scan 79 ... already in the extension by π_ab" to "decide it": true for g ≥ 1, false for
   g = 0 (the classes of the tangential sections at 0 and at 1 of P^1 ∖ {0,1,∞} coincide in the extension by π_ab),
   and inside one packet the abelianized classes coincide when ν = 1. New target in its place: compute, for every
   (g, ν), the fibres of {packets and points} → {classes in the extension by π_ab}. Reason: item 2 of Part 2.
5. B (a), added target: characterize group-theoretically the K^×-subtorsor of tangential sections inside the packet.
   Reason: Stix lists exactly this as missing ("recognize tangential sections within cuspidal sections"); it is the
   one point of §9 that the literature read does not settle.
6. B (b): correct the wording. He excludes g = 0 with ν ≤ 1 (P^1 and the affine line), not ν = 2; G_m is included.
   And the proof cannot use "G(K) de type fini" (false when the torus is non-trivial): ask for the proof from
   "no non-trivial divisible element in G(K)" (Esnault–Hai Prop. 5.3; Stix Thm 45), with the proof of that property
   for semi-abelian G over K finitely generated over Q, and the list of fields where injectivity fails (R; a
   p-adically closed field that is not sub-p-adic: Koenigsmann Prop. 2.3 (1)).
7. B (c): the sentence on the "transcendental" sections has a definite answer to be proved, not decided: every member
   of a packet has image in the normalizer of the loop subgroup (Stix Cor. 12), so none is admissible, and his
   formulation of 2:sc79 coincides with the letter of 1983 (both use the whole packet, "Mächtigkeit des Kontinuums").
   Replace "say exactly how the two differ" by the three-way comparison that is open: (i) prove π^{Γ'} = 1 for every
   point section and every cuspidal section, Γ' open (so his condition (a) of 2:sc431–433 does not exclude cusps);
   (ii) prove that Ker χ fixes the loop subgroup of a cuspidal section; (iii) prove or refute the 1983 PS: for a point
   section, the fixed group of Ker χ in π is trivial. For (iii) a start to check: by Ribet's theorem (torsion of an
   abelian variety over K(μ_∞) is finite) the fixed group Z maps to zero in the abelianization of every open
   subgroup containing Z·s(Γ), for proper X, hence Z equals the closure of its commutator subgroup; what remains is
   to exclude a non-trivial perfect closed subgroup. Reason: items 1 and 6 of Part 2.
8. B (c), on ⑤: name the neighbourhood argument as the tool and ask for the equivalence with ⑤ a), b), c) written in
   his terms, then the list of which of ①–⑥ are now theorems (for Γ = G_k, k/Q_p finite, granted the 2026 theorem;
   over number fields for the curves with C(A_K)_•^{f-cov} = C(K)). Reason: item 6 of Part 2.
9. B (d): delete "Θ is no longer injective". For finite k/Q_p, Θ: k^× → H^1(k, Ẑ(1)) is injective with cokernel
   Ẑ/Z; it fails to be injective over R. The dichotomy "point or cuspidal" is tool 2 (a), so the asks that remain
   are: the tangential subtorsor and its closure in the packet (which packet members are limits of point sections
   s_x, x → y); complete curves of genus 0 and 1 over k (compute the section sets; for an elliptic curve the
   cokernel of E(k) → H^1(k, T E) is the Tate module of H^1(k, E)); which of ①–⑥ hold for Γ = G_k; and the same
   over finitely generated extensions of Q_p, where nothing is claimed. Reason: 1.C.
10. B (e): add as a tool Mochizuki–Tsujimura Thm F (ii) (for a dominant morphism of hyperbolic curves, a section
    upstairs arises from a rational point iff its image does), next to the Hom-form. Reason: it is the functoriality
    statement his relative version needs, and it is proved over p-adic fields.
11. B (f): add Steklov's Theorems B and C (hyperbolic DM-curves, in particular the moduli stack of elliptic curves:
    the section conjecture follows from the one for curves over finite extensions; injectivity over sub-p-adic
    fields). For (0,4) say that the local statement is now a consequence of tool 2 (a), so that the ask is the
    global one. Reason: item 7 of Part 2.

Part C.
12. C (a): the statement to prove is wrong as written. Over R: π_0(U(R)) → **all** classes of sections is bijective
    for every hyperbolic real curve, affine or proper (Mochizuki Cor. 3.13; Bresciani–Vistoli); a class is cuspidal
    at a real cusp y iff y lies in the closure of its component; the packet at y has two elements. Ask instead:
    derive these in his language (his §33 theorem is Mochizuki's Thm 3.6 / Cor. 3.7); prove what the classes recover
    of the position of the cusps (which cusps are real, on which oval, and their cyclic order up to reversal, from
    the pairs of cusps to which each class is cuspidal); prove the profinite fixed groups (1 for a line, Ẑ for an
    oval), which the literature read gives only in the discrete case. Reason: item 5 of Part 2.
13. C (c): "the six real cuspidal packets" should be "the three real packets (two classes each)"; the computation to
    demand is the three classes of involutions and the six identifications of tangential classes with them (the
    tangential class at 0 towards 1 and the one at 1 towards 0 are both the class of the interval (0,1), and so on).
    Reason: same.

Part D.
14. D (a): put the equivalence "section conjecture for C ⇔ C(A_K)_•^{f-cov} = C(K)" (given the 2026 theorem) into the
    diagram, with Stoll's Remark 8.9; and say that the set of classes of sections of the extension by π_ab is a torsor
    under H^1(K, T J), which contains the completion of J(K) with quotient the Tate module of H^1(K, J), so that the
    question "finite?" has the answer no in general and the ask is to compute it and its Selmer part.
15. D (b): the statement is Cor. 8.5 of the paper; the chain to check is Thm 1.1, Harari–Stix Thm 2.1, Stix
    arXiv:1203.3236 Cor. 5, Stoll Cor. 8.8 (all four statements verified against the sources here).
16. D (c): "every section is locally geometric, and what this gives globally" is Prop. 8.1 of the paper. Ask
    beyond it: finiteness of loc_v(Sec(C/K)) for K without CM subfield (Betts–Stix Thm A with Thm 1.1); rigidity
    (Porowski: a section is determined by its reductions on a set of places of strongly positive density); then
    prove or refute finiteness of Sec(C/K) itself, naming the missing statement (finite fibres of loc_v at one
    place). Reason: this is the present frontier of his "Mordell through splittings" (2:sc65).

Part E (Fermat; not redone by the predecessor) and LM7.
17. Steklov's theorem (all Selmer sections over Q of the affine Fermat curve of exponent ℓ ≥ 7 are cuspidal) with
    tool 2 (a) and the real case would give: every section of π_1(V_ℓ) → G_Q is cuspidal for ℓ ≥ 7. This is the
    section-conjecture form of Fermat's theorem that 2:sc65 points to. Ask Pro to check the chain (in particular that
    "Selmer" in Steklov's sense is what the 2026 theorem delivers at every place, 2 and ℓ included) and to treat ℓ = 5
    and ℓ = 3, where Steklov's method stops.

### (iii) Noticed in passing, outside this fork's task

- Mochizuki–Tsujimura, Thm G: with Σ = Primes, "the various p-adic versions of the Grothendieck–Teichmüller group
  that appear in the literature in fact coincide", and the metrized GT is commensurably terminal in GT. Bears on
  the LM3/LM3b reviews (GT), not on sections.
- Mochizuki 2003, Cor. 3.8: components of M_{g,r}(R) ↔ classes of involutions over complex conjugation in the
  extended mapping class group, with centralizers. This is the statement behind F11 (a) (the count of classes of
  anti-involutions is the number of components of the real moduli) and behind Cor. 1–2 of his §33; for LM4.
- 2:sc483 as written ("the L_i are the maximal subgroups of π whose normalizer in E has open image in Γ") needs
  "pro-cyclic and cyclotomically normalized" to be true (otherwise π itself qualifies); in that form it is
  Nakamura's theorem as stated by Stix (Thm 20, Cor. 21) for fields that distinguish tori from abelian varieties.
  Finite extensions of Q_p do not (a Tate curve has Z_ℓ(1) inside its Tate module), so the p-adic case of LM6 A (e)
  cannot be had by that route; this last remark is my reasoning, not a quotation.
- Yamaguchi, arXiv:2601.07112v4: centre-freeness and torsion-freeness of the maximal m-step solvable quotients
  (m ≥ 2) of geometric fundamental groups of hyperbolic curves; for F5.

### (iv) Not obtained

- Mochizuki, *The local pro-p anabelian geometry of curves* (Invent. Math. 138 (1999)), Thm 19.1: not fetched in this
  fork (statement taken from Koenigsmann's Remark 1.2 (2)).
- Hoshi, Publ. RIMS 46 (2010) 829–848: listed on the author's page with a link to the publisher only; statement taken
  from Hoshi–Tsujimura RIMS-1950.
- Pál 2011, Wickelgren 2014, Esnault–Wittenberg 2009 (real case): not fetched; their content as summarized by
  Bresciani–Vistoli.
- Tamagawa 1997 (Compositio 109), Prop. 2.8 (the original neighbourhood argument): not fetched; used through
  Koenigsmann and Stix.
- Betts–Stix (Annals 2025), Bresciani's toric paper (v5, Sept 2026) beyond its abstract, Pajwani 2025, the OpenAI
  "Selmer converse" paper: not read.
- Pop's note of 28 Sep 2025 on the t-birational section conjecture
  (`https://www2.math.upenn.edu/~pop/Research/files-Res/2025-09-28_t-BSC.pdf`): the server answered 403 to the
  download; not read.
- Stix's monograph (LNM 2054) is paywalled; not used.

### (v) Downloads

Twenty files, all under `Free or receipted\free\lm-expert-20261112\<short-name>\`, each with its text extraction
beside it; paths, sizes, SHA-256, titles and source URLs are in `LM_EXPERT\work\lit\downloads_B1.jsonl`. Hosts: arXiv
(11), kurims.kyoto-u.ac.jp author pages (4), IAS (1), MPIM preprint archive (1), authors' university pages (2:
Harari, Stoll), the Grothendieck Circle page of L. Schneps (1, the letter; editor's page, see item 1). They are not
yet entered in `CLAUDE_FREE_SHELF.json`.

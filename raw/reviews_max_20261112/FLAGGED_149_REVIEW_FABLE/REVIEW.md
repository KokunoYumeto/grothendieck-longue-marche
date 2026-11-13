# Intake of the return FLAGGED_149, 13 November 2026

Reviewer: Claude Fable 5.2 (Anthropic), effort max, no sub-agents, 13 November 2026 00:44 WEST. Return: GPT-6 Astra
(OpenAI, ChatGPT Pro mode), 96 minutes, marked INCOMPLETE by itself; 107 statements (57 Proved, 31 Refuted, 15 Known,
4 Open by its own labels). Unpacked at `longue_marche_pro_pilot_20261104\answers\FLAGGED_149_unzipped\`.

## What was read

- The return: `sections\F_agent.tex` lines 278–1057 (F17.1–F17.8) in full; `CF_Z_agent.tex`, `DE_Z_agent.tex`,
  `Z_root.tex`, `C_agent.tex`, `DE_agent.tex`, `AB_agent.tex`, `AB_Z_agent.tex`, `F_root.tex`, `F7_test.tex`,
  `F7_test5.tex` in full; of `F_agent.tex` lines 1–277 (F9.1–F9.5) and of `G_root.tex` (G1–G11) every statement and
  the first 560 and last 220 characters of every proof; `FLAGGED_149_results.csv` (all 107 rows, first 300
  characters of each statement); `code\README.md`. Not read: `FLAGGED_149_report.md`, the readings CSV, `audit\`,
  the bibliography, the PDF.
- The prompt `pro_prompts_archive_20261112\FLAGGED_149\PROMPT.md`, lines 1–58 (all rows), read for the map of
  12 November; GOOD_REDUCTION in its `_work` version and LM6 as listed in
  `research_maps_20261112\CONNES_CONSANI_CFT\MAP.md` §0; the review of CYCLOTOMIC_KERNEL (Claude Opus 5.5) in full.
- Grothendieck's text: cote 149 scans 45, 53–56, 59–63, 80–86 (first-pass transcription), read for the map. No scan
  image was opened in this intake; the return's readings were not checked.
- No source cited by the return was opened. Every "known" below is "known, source not opened".

## Programs

Rerun (`rerun\COMPARISON.txt`): the eight mathematical programs with `python -I` (Python 3.13.9, SymPy 1.13.1): all
exit 0, empty stderr; the eight JSON outputs equal the shipped ones as parsed data (`G_checks_output.json` differs
in the key `sympy_version` only). Own program, written from the paper (`rerun\own\own_checks.py`, output
`own_checks.out`): the discriminants of F17.2 and F17.8; the factorizations and the discriminant of Z142e; #D over
F_3, F_9, F_27 for B14 (6, 10, 36) by my own field arithmetic; E(F_3) for B14 and E(F_5) for B15 and B7; the
hyperplane incidence of B9 (15 and 7); the 216 branch-triple values of ZCF4 (none zero). All agree with the return.
By hand: the stable model of F17.2, the class-two computation of F17.3, the conic model (B14.4), #J(F_27) = 25920
from the three counts, the normal bundles of E5.

# Part I. The statements

## 1. Verdict counts

| Verdict | Number | Statements |
|---|---|---|
| correct | 86 | all others |
| correct with a gap | 0 | — |
| known (source not opened) | 17 | the return's 15 (A1, A2, A6, D1, D4, F8a, F10b, F9.2, F9.5, F17.1, G1, G4, ZCF1, ZD11, Z142b), and ZCF5 (CYCLOTOMIC_KERNEL A6, A7: Stix in substance), ZCF7 (CYCLOTOMIC_KERNEL D5: Clark's curve) |
| open as stated | 4 | B9, ZCF6, ZD10, Z142g |
| wrong | 0 | — |

Depth: V = proof followed in full; S = statement and the opening and close of the proof; C = recomputed by my own
code or by hand; R = program rerun, identical.

## 2. The decisive results

**F17.6 (Proved; correct, V).** R henselian DVR, residue field k finitely generated over Q, U/K hyperbolic with a
stable marked model (𝒞, 𝒟) over R, Π = π_1(U_K̄) full profinite, s any continuous section of G_K → G_k,
E_s = π_1(U) ×_{G_K,s} G_k. (i) Every geometric node gives an injected I_e ≅ Ẑ(1) ⊂ Π, defined up to conjugacy,
essentially cyclotomically normalized in E_s (after a finite extension of k fixing the node and its branches a
closed subgroup of the normalizer maps onto G_k and acts by χ), for every s. (ii) Distinct nodes and cusps give
distinct conjugacy classes of maximal procyclic subgroups. (iii) If 𝒞_k has a node, E_s is not isomorphic over G_k
to the extension of any smooth hyperbolic curve over k, nor after any finite extension of k. (iv) The number of
classes of essentially cyclotomically normalized maximal procyclic subgroups is r (the number of cusps) exactly
when the stable model is smooth, and at least r + n with n > 0 nodes otherwise.
*The proof, as followed.* Completion changes nothing (both Galois groups are extensions of G_k by Ẑ(1)). With the
log structures, 𝒞 is log regular and proper over the trait; the square π_1(𝒞_k^log) ≅ π_1(U) over
π_1(k^log) ≅ G_K (F.9) comes from two quoted theorems (Illusie, Thm 7.6: Kummer étale covers of a log regular
scheme are the tame covers of its open of triviality; Hoshi, Cor. 3.9: a proper log regular scheme over a complete
local ring has the Kummer étale covers of its closed log fibre). The geometric kernel is the group of the
semi-graph of the stable curve (Mochizuki, Example 2.5), with injected edge groups (Hoshi–Mochizuki, Lemma 2.11).
At a node of thickness m the log point has group T_P ⋊ G_k, T_P = {(a,b,c) ∈ T³ : a + b = mc}, mapping onto
G_K = T ⋊ G_k by (a,b,c,g) ↦ (c,g) with kernel the antidiagonal T; the inverse image of s(G_k) is closed, maps
onto s(G_k) and acts on that kernel by χ. No complement is chosen, so the argument holds for every s. Distinctness
and maximality: Mochizuki, Prop. 1.2 (commensurable terminality). Non-realization, three cases: dual graph with
b_1 > 0: H_1(Π, Q_ℓ) has a nonzero quotient with trivial action of an open subgroup of G_k (F.12), and H_1 of a
smooth curve has none (the sequence (F.13), χ_ℓ of infinite image, and AE1 of CYCLOTOMIC_KERNEL for the dual
abelian variety); tree and proper: a realizing curve is proper (H²(Π, Z/ℓ) ≠ 0) and Stix's Theorem 20 forbids the
node group; tree and affine: dim Hom_{G_k}(Q_ℓ(1), H_1(Π, Q_ℓ)) = r − 1 by (F.14), so a realizing curve has r
cusps, hence r classes (Stix, Thm 20, Cor. 21), against r + n. Each step was followed and holds.
*What it rests on, not opened by me:* Illusie 7.6, Hoshi 3.9, Mochizuki Example 2.5 and Prop. 1.2,
Hoshi–Mochizuki 2.11, Stix Thm 20 and Cor. 21. This is the missing half of CYCLOTOMIC_KERNEL E4 (H2 (b)).

**F17.7 (Proved; correct, V).** Same R, K, k, U, no stable model assumed; s any continuous residue splitting.
Equivalent: (1) U has good marked reduction after a finite extension of K; (2) the outer action ρ_U ∘ s is that
of a smooth hyperbolic curve over k; (3) it is so after restriction to G_{k'} for some finite k'/k. So "some
splitting" and "every splitting" give the same condition e), and the finite residue extension changes nothing.
*Proof followed.* (1) ⇒ (2): K_1/K finite Galois with good reduction, G = Gal(K_1/K); the semilinear G-action
extends to the smooth marked model (uniqueness of stable models) and reduces to isomorphisms λ_σ of the special
pair over k_1; α : G_k → G_K → G has kernel G_{k_2}; λ_{α(γ)} with γ on scalars is a Galois descent datum for
k_2/k, effective through ω(D)^{⊗3}; the descended curve V_s has outer action ρ_U ∘ s, because ρ_U factors through
Q = G ×_{Gal(k_1/k)} G_k (kernel I_{K_1}, trivial by good reduction) and q ∘ s(g) = (α(g), g). (3) ⇒ (1): stable
reduction over a finite K_1 (Knudsen); the comparison (F.16)–(F.17) gives a finite L ⊃ K_1 with residue field
k_2 and section s|; a node would contradict F17.6. This is the theorem asked as A3 of GOOD_REDUCTION, with its
Leads 1 and 4, and Lead 6 in the form "the realizing curve is the descent of the special fibre by α".

**F17.8 (Refuted; correct, V, C).** y² = (x²+1)²(x²−2) + t over Q[[t]]: a stable degeneration whose special fibre
is irreducible with the two nodes (±i, 0); G_Q exchanges them, so neither node class is invariant under G_Q. The
discriminant −46656 t²(t−2)(t−4)² is confirmed. What is refuted is the literal form of the war game's H2 (b), not
a sentence of Grothendieck.

**ZCF12 (Proved; correct, V).** k of characteristic 0. A semilinear G_k-action on the universal pro-cover 𝒰 of a
hyperbolic curve over k̄, for which every f ∈ Ω (the union of the function fields of the levels) has open
stabilizer, has a finite hyperbolic quotient W/k: 𝒰 → W_k̄ equivariant, its deck group normalized by G_k, the
action coming from a continuous section of E_W → G_k; W can be taken finite étale over any prescribed level.
Hence Conjecture B with the Γ° clause of scan 61 and Conjecture B′ with this continuity clause, each over all
hyperbolic curves over the same k, are equivalent. *Proof followed:* finite orbits of field generators give a
G_k-stable finite level L; the action descends from 𝒰 to the open curve W_k̄ (Stacks 32.6.1 and descent along a
finite Galois level), then to k_i (normal core of the stabilizers), then to k by effective Galois descent as in
F17.7. It is CYCLOTOMIC_KERNEL D11, which the review of that return had read in outline only; here it is proved
in full. The existence of the fixed point is not proved (ZCF6 (4) for abstract actions, ZCF6 (1) for all).

**B9 (Open; open as stated; the partial results correct, V, C).** Not settled: injectivity of point sections in
the geometrically prime-to-p group for hyperbolic curves over fields finitely generated over F_p. Proved there:
(a) an affine collision in genus ≥ 2 gives a proper collision of the same genus; (b) a collision over a finitely
generated field specializes to one over a finite field (SGA 1 XIII 4); so the question is exactly the proper case
of genus ≥ 2 over finite fields; (c) the exceptional set of Saïdi–Tamagawa is stable under covers
(|E_V| = d|E_U|) and is empty iff injectivity holds over all finite constant extensions; (d) in genus 2, odd p:
the fifteen double covers are the quotients of Z = C ×_{J,[2]} J; a successful lift in each is r_H(Q̃) for the
single point Q̃ = (Q, b), 2b = [Q − P]; the identity

  [8] = Σ_H r_H^* (r_H)_* − 7 π^* π_*  on J_Z

holds (the identity of G = F_2⁴ lies in 15 hyperplanes, every other element in 7: Σ_H N_H = 8 + 7 N_G; recounted),
so the joint kernel K_2 of the fifteen norms lies in J_Z[8]; ker π^* = J_C[2] and π^* J_C[8] ≅ (Z/4)⁴ ⊂ K_2, so
K_2 ≠ 0. If all fifteen tests succeed, p^a[Q̃ − P̃] ∈ K_2: a class killed by 8 that the norm identities do not
determine. **B14 (correct, V, C):** y³ − y = x + 1/x over F_3, P, Q over 0, ∞: the étale double cover
D : W² = 1 − t² − t⁴ − t⁸ over F_27 has lifts P′ = (1,−1), Q_± with g(Q_+) − g(P′) of order 5 on
E : w² = u⁴+u³+2u²+u+2 (5 points over F_3) and [Q_− − P′] of exact order 6 (f^*f_* + g^*g_* = 2, and order 3 is
excluded by the bidegree (2,3) genus bound); a cover of degree 640, geometrically prime to 3, with a rational
point over P and none over Q. **B15 (correct, V, C):** y² = x⁵ + (x²+1)² over F_5, P = (0,1), Q = ∞, [P − Q] of
order 5: the double cover v² = x − 1 has elliptic quotient w² = x⁴+2x³+2x²−x−1 with 8 points; both lifts of Q
have nonzero 2-primary image; a cover of degree 16 separates.

**ZD10 (Open; open as stated) and ZD11 (Known, not opened).** ZD10: for U = P¹ ∖ {0,1,∞} over Q, every section
of π_1(U) → G_Q lifts to a section of G_{Q(t)} → G_Q; and every section of G_{Q(t)} → G_Q lies in the
decomposition group of a rational place. Neither is proved; point and cuspidal sections lift. ZD11: for C/k
hyperbolic, k finitely generated over Q: "every section of C_F/F is geometric or cuspidal for all finitely
generated F/k" ⟺ "every such section lifts through G_{F(C)} → π_1(C_F)" (Bresciani, Theorems A and B, as quoted;
it agrees with what I remember of arXiv:2108.13397). So the lifting assertion of his conjecture (b) of scan 127
has the strength of the section conjecture.

**D4 (Known, not opened; proof read, V) and D5 (Proved; correct, V).** D4: I_v ≅ Hom(Γ_v, T) with cyclotomic
action, 1 → I_v → D_v → G_{κ(v)} → 1 split; I_v ≅ ∏_ℓ Z_ℓ(1)^{r_ℓ}, r_ℓ = dim Γ_v/ℓ ≤ rational rank ≤ trdeg L −
trdeg κ(v); Γ_v = Q gives I_v = 1 and Γ_v = Z[1/2] gives ∏_{ℓ≠2} Z_ℓ(1). So "des T_∞^α, α la codim" is false
in general. D5: for I_v ≠ 1, with Δ_v the largest divisible convex subgroup of Γ_v and w the coarsening by it:
I_w = I_v, N_{G_L}(I_v) = D_w, N_P(I_v) = D_w ∩ P, 1 → I_v → N_P(I_v) → G_{κ(w)K̄} → 1. So N_{G_L}(I_v) = D_v
iff v/w is henselian on κ(w) (always for rank one, so for DVRs), and N_P(I_v) = I_v iff κ(w)K̄ is separably
closed. The proof identifies w on F = L̄^{I_v} as the coarsest henselian valuation with separably closed residue
field (F. K. Schmidt, through Kuhlmann 9.44, 9.45, not opened), which every automorphism preserves.

**E4 (Proved; correct, V) and E5 (Refuted; correct, V, C).** E4: for an open stratum S = D_J° of a normal
crossings boundary, π_2(S) → T^J → π_1(P) → π_1(S) → 1 with P the product of the punctured normal bundles, the
boundary map a ↦ (⟨c_1(N_{D_j/X}), a⟩)_j, and the same sequence for the punctured tubular neighbourhood; (37) is
left exact iff these vanish iff for every n some connected finite étale S′ → S makes every N_j|S′ an n-th power.
E5: U = (P¹ ∖ {0,1,∞})³, blow up (0,2,2): the stratum S = D′ ∩ E ≅ P¹ has normal bundles O(1), O(−1) (recomputed)
and boundary map a ↦ (a, −a) ≠ 0. So (37) is not left exact for every normal crossings compactification of an
elementary anabelian variety; his "On va donc admettre" of scan 135 fails.

**Z142e (Refuted; correct, V, C).** f_t = (z³ − 3z + t)², restricted to X_t → Y = P¹ ∖ {9, 16, ∞}, is a composite
of two finite étale maps and two puncture fillings, of degree 6, source type (0,20); for t = 0 it has two finite
critical values (0, 4), for 0 < t ≤ 1/10 three (0, (t±2)²). A two-sided conjugacy extends to the compactified
spheres and preserves the number of critical values, so the path t ↦ f_t η_t through étale maps leaves the
two-sided orbit. With fixed ramification data and fixed incidence of the marked images, local path isotopy does
stay in one orbit. So "isotopie" in the enlarged category of scans 18–19 cannot be path-connectedness in the space
of étale maps.

## 3. All statements

| ID | Return | Verdict | Depth and note |
|---|---|---|---|
| A1 | Known | known | S; cd_ℓ P = n, cd_ℓ E = n + 2, ∞ at 2 iff K formally real |
| A2 | Known | known | V; Artin–Schreier; Minamide–Tsujimura cited as "Theorem 2.7" (version of 15 Feb 2022); the Opus review found the same theorem as 2.12 in the version of 19 May 2022 |
| A3 | Proved | correct | V; torsion-freeness and centre by the faithful H_1 of finite covers |
| A4 | Proved | correct | V; I_c ∩ I_d = 1, N_P(I_c) = I_c |
| A5 | Proved | correct | V |
| A6 | Known | known | V; Hoshi–Mochizuki Thm C (ii) quoted |
| B1 | Proved | correct | V; G(K) = finite ⊕ free; his "de type fini" is false |
| B2 | Proved | correct | V; Théorème 3 |
| B3 | Proved | correct | V; a ∈ G, not a ∈ Y |
| B4 | Refuted | correct | V; the lemma of scan 37 fails exactly for type (1,1) |
| B5 | Proved | correct | V; π^Γ = 1 for every section over a finitely generated field |
| B6 | Proved | correct | V; Lang torsor |
| B7 | Refuted | correct | V, C; kernel G(K)[p^∞] |
| B8 | Proved | correct | V; punctured genus one, by the modulus |
| B9 | Open | open as stated | V, C; see §2 |
| B10 | Proved | correct | V |
| B14 | Proved | correct | V, C, R |
| B15 | Proved | correct | V, C, R |
| C1 | Proved | correct | V; Bierstone–Milman quoted |
| C2 | Proved | correct | V; fails for (0,1) |
| C3 | Proved | correct | V; I_K → Π is κ_q ∘ [μ]; his "Je présume" of scan 77 is right |
| C4 | Proved | correct | V; rests on Holzschuh–Schmidt–Stix 2026, Thm 5.6, quoted |
| C5 | Proved | correct | V |
| C6 | Proved | correct | V; the class is c_1 of the normal line with the positive Kummer convention |
| C7 | Proved | correct | V; (C.5) splits iff the normal line is trivial; surjectivity alone does not split it |
| C8 | Proved | correct | V; the torsor under O(S)^* inside the torsor under its completion |
| C9 | Proved | correct | V |
| D1 | Known | known | V |
| D2 | Proved | correct | V; a DVR of Q(x,y) with residue field Q |
| D3 | Proved | correct | V |
| D4 | Known | known | V; see §2 |
| D5 | Proved | correct | V; see §2 |
| D6 | Refuted | correct | V |
| D7 | Refuted | correct | V |
| D8 | Proved | correct | V |
| D9 | Refuted | correct | V; = CYCLOTOMIC_KERNEL B8 |
| D10 | Proved | correct | V |
| E1 | Proved | correct | S |
| E2 | Refuted | correct | V; the product compactification of two hyperbolic curves is terminal |
| E3 | Proved | correct | V |
| E4 | Proved | correct | V; see §2 |
| E5 | Refuted | correct | V, C; see §2 |
| E6 | Refuted | correct | S |
| F8a | Known | known | V; = CYCLOTOMIC_KERNEL B1 |
| F10a | Proved | correct | V |
| F10b | Known | known | V; Stix Thm 14 |
| F10c | Refuted | correct | V; = CYCLOTOMIC_KERNEL C3 |
| F9.1 | Proved | correct | S; rests on Carlson–Stix Lemma 5.4, quoted |
| F9.2 | Known | known | S |
| F9.3 | Refuted | correct | S |
| F9.4 | Refuted | correct | S |
| F9.5 | Known | known | S |
| F17.1 | Known | known | V; Tamagawa (5.3) quoted; a) ⇒ e) for every splitting |
| F17.2 | Refuted | correct | V, C; y² = (x³ − t⁶)(x³ − 1): two copies of Y² = 1 − X³ at a node VW = t; trivial on Π/Γ_3 |
| F17.3 | Refuted | correct | V, C; class-two computation redone |
| F17.4 | Refuted | correct | V; five cyclotomically normalized lines against at most four cusps |
| F17.5 | Refuted | correct | V; y² = x³ − t²x: e) holds for every splitting, with bad reduction |
| F17.6 | Proved | correct | V; see §2 |
| F17.7 | Proved | correct | V; see §2 |
| F17.8 | Refuted | correct | V, C; see §2 |
| G1 | Known | known | S |
| G2 | Proved | correct | S; n = 2 fails on the punctured torus |
| G3 | Proved | correct | S |
| G4 | Known | known | S |
| G5 | Refuted | correct | V |
| G6 | Proved | correct | S; the long construction was not followed |
| G7 | Refuted | correct | V |
| G8 | Proved | correct | S |
| G9 | Refuted | correct | V |
| G10 | Proved | correct | S |
| G11 | Proved | correct | S |
| B11 | Refuted | correct | V |
| A7 | Proved | correct | V |
| A8 | Proved | correct | V |
| A9 | Proved | correct | V; E ≅ Aut(P) ×_{Out(P)} Γ for Z(P) = 1 |
| B12 | Refuted | correct | V |
| B13 | Refuted | correct | V, C |
| ZCF1 | Known | known | V; Mochizuki Thm 17.1 quoted |
| ZCF2 | Proved | correct | V |
| ZCF3 | Refuted | correct | V |
| ZCF4 | Refuted | correct | V, C, R; the Gröbner part by rerun only |
| ZCF5 | Proved | known | V; = CYCLOTOMIC_KERNEL A6, A7, C6 |
| ZCF6 | Open | open as stated | V |
| ZCF7 | Refuted | known | V; = CYCLOTOMIC_KERNEL D5 |
| ZCF8 | Proved | correct | V; = CYCLOTOMIC_KERNEL D10, now with a full proof |
| ZCF9 | Proved | correct | S |
| ZCF10 | Proved | correct | V |
| ZCF11 | Proved | correct | V |
| ZCF12 | Proved | correct | V; see §2 |
| ZD1 | Proved | correct | V |
| ZD2 | Proved | correct | V |
| ZD3 | Proved | correct | V |
| ZD4 | Refuted | correct | V |
| ZD5 | Refuted | correct | V |
| ZD6 | Refuted | correct | V; depends on the reading of the margin of scan 127 |
| ZD7 | Refuted | correct | V |
| ZD8 | Proved | correct | V |
| ZD9 | Proved | correct | V |
| ZD10 | Open | open as stated | V |
| ZD11 | Known | known | V |
| Z142a | Proved | correct | V |
| Z142b | Known | known | S; Bertin–Romagny, Noohi, Bresciani quoted |
| Z142c | Refuted | correct | V; y^p − y = tx |
| Z142d | Proved | correct | V |
| Z142e | Refuted | correct | V, C; see §2 |
| Z142f | Proved | correct | V |
| Z142g | Open | open as stated | V |

# Part II. Findings

**F1. No statement is wrong; none has a gap that I found.** 86 correct, 17 known, 4 open as stated. Eighteen
statements were checked by statement and proof ends only (A1, E1, E6, F9.1–F9.5, G1–G4, G6, G8, G10, G11, ZCF9,
Z142b); for those "correct" means no error seen at that depth.

**F2. The main question of GOOD_REDUCTION is answered.** F17.7: for every splitting, condition e) holds iff the
reduction is potentially good; F17.6: with stable bad reduction no residue action is that of a smooth curve over
any finite extension of k. Hypotheses: residue field finitely generated over Q, R henselian. His table becomes:
a) ⇔ b) ⇒ c) ⇒ d); a) ⇒ e); c), d) ⇏ a) (F17.2, F17.3); c), d) ⇏ e) (F17.4); e) ⇏ a) (F17.5); and, from
F17.5 (inertia acts by −1 on H_1), e) ⇏ c), e) ⇏ d), which the return does not state.

**F3. F17.6 rests on five quoted theorems that nobody on our side has opened.** Illusie 7.6, Hoshi 3.9, Mochizuki
Example 2.5 and Proposition 1.2, Hoshi–Mochizuki Lemma 2.11, with Stix Theorem 20 and Corollary 21. The argument
from them is complete. A check that reads these six places is the one thing between F17.6 and a citable theorem.

**F4. Two corollaries the return does not draw.** From F17.1: the image of T in Out(Π) is finite iff the
reduction is potentially good, and then, with n its order, good reduction holds over K(ϖ^{1/n}) (the inertia of
that field is nT, which acts trivially). This is the first half of Lead 6 of GOOD_REDUCTION.

**F5. ZCF12 completes CYCLOTOMIC_KERNEL D11.** Continuous semilinear actions are section actions of a finite
quotient over the same field. Conjecture B′ without continuity stays open (ZCF6 (4) = D13).

**F6. The four open statements are of two kinds.** ZCF6 (1)–(3) and ZD10 are the section conjecture for
P¹ ∖ {0,1,∞} over Q, the birational section conjecture for Q(t), and cuspidalization; by ZD11 the last has the
strength of the section conjecture over all finitely generated fields. B9 and Z142g are not known conjectures in
that sense: B9 is the emptiness of the Saïdi–Tamagawa exceptional set for proper curves over finite fields, with
an exact residual class in genus 2; Z142g asks for three constructions, one of which (the wild category) Z142c
shows cannot keep his base-invariance.

**F7. B9's reductions and the joint-cover identity are right.** Recounted: 15 and 7. K_2 ⊂ J_Z[8], and
π^* J_C[8] ≅ (Z/4)⁴ ⊂ K_2. B14 and B15 separate their pairs; my counts agree.

**F8. D5 gives the exact form of F19.** N_{G_L}(I_v) = D_w for the coarsening w by the largest divisible convex
subgroup. His "N_{x′} = Norm(I_{x′})" holds for DVRs and for rank one; his "I_{x′} = Norm_π(I_{x′})" holds iff
κ(w)K̄ is separably closed, so for curves and not for divisors on surfaces.

**F9. E5 refutes the admitted extension (37) in dimension 3; in dimension 2 it is not refuted.** For a product of
two hyperbolic curves E2 proves that the product compactification is terminal and all its local meridian maps are
injective. The return does not state whether ∂ can be nonzero for some compactification of such a surface. My
argument, not in the return: every normal crossings compactification maps to the product one (E2), hence is an
iterated blow-up of it at boundary points; every one-dimensional open stratum is then affine (an exceptional
curve or a strict transform, minus its crossing points) or a complete curve {c} × C̄_2 of genus ≥ 2, and in both
cases π_2 = 0. So (37) is left exact for every such compactification of a product of two hyperbolic curves,
which answers the last question of row F26 in dimension 2.

**F10. Statements already in CYCLOTOMIC_KERNEL.** F8a (B1), F10c (C3), D9 (B8), ZCF5 (A6, A7, C6), ZCF7 (D5),
ZCF8 (D10), ZCF12 (D11). The return cites that return for each.

**F11. Credits.** F17.5 is the transcriber's note RN103-03/04 and F17.2, F17.3 are RN100-03, RN103-01/02 (cited
in the prompt's row F17); F17.7 names "the correction proposed in the reader's notes"; the route of F17.6 through
the logarithmic fundamental group is route (i) of Lead 2 of the unsent GOOD_REDUCTION prompt, which the return did
not see. G5 and the leads of rows F19–F26 are the prompt's.

**F12. Readings.** The return's corrections of the text are mathematical and are marked so: Z(L_i) is the
normalizer (F10a), a ∈ G (B3), U for L in (32)–(33) (D9), the normal line with the stated sign (C6). None was
checked against a scan image in this intake.

**F13. Minor.** The two citations of Minamide–Tsujimura (Theorem 2.7 here, 2.12 in the Opus review) are two
versions of one preprint; a companion text should cite the published numbering. ZD6 refutes the margin of scan
127 in its widest reading; with "sous-groupe" restricted to the image of Γ° the statement is D9.

## Limits

No cited source opened; no scan image opened; the report, the readings ledger and the audit folder not read; the
PDF not inspected; G6 and Z142b not followed in full; the Gröbner computation of ZCF4 and the Frobenius polynomial
of B14 accepted from the rerun and from my hand computation of #J(F_27).

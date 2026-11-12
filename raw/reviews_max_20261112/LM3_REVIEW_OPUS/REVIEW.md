# Review of the Pro return LM3_TEICHMULLER_TOWER

Claude Opus 5.5 (effort max), 12 Nov 2026.

**Reviewed.** The return of GPT-6 Astra (ChatGPT Pro mode) to the research prompt LM3_TEICHMULLER_TOWER on Grothendieck's
*La Longue Marche*: `answers\LM3_TEICHMULLER_TOWER_2026-11-11.zip`, extracted unchanged (Python, `-I`) into
`return\LM3_TEICHMULLER_TOWER\` of this folder. All 110 numbered statements (A.1–A.13, B.1–B.15, C.1–C.13, D.1–D.23,
E.1–E.28, F.1–F.18) were read with their proofs in `sections\*.tex`. The 42 statements cited by the blocks "After the
returns … (added 12 November 2026)" of LM4, LM5 and LM6 were reviewed first; they are table 2.1.

**Context used.** The transcription of cote 140-2 (`second_pass\LM_P0nn_checked_fixed.tex`, else `_checked.tex`) at
the scans each statement needs: 17, 187–189, 224–227, 321–326, 352–358, 395–401, 431–436, 483–486, 496–505. The LM
expert's `LM_EXPERT\FINDINGS.md` (F3, F5, F6, F13, F17, F18, F20, F21 bear on LM3). Local copies of the sources
(`Documents\Free or receipted\free\lm-expert-20261112\`), read for the exact statements used: Nakamura 1994
(Thm (2.1.1), Lemma (2.1.2), Lemma (2.1.4), Thm A), Hoshi–Mochizuki 2011 (Thm 6.1, Cor. 6.4, Cor. 6.5), Mochizuki 2007
"combinatorial Grothendieck conjecture" (Prop. 1.2), Koenigsmann 2005 (Prop. 2.4), Pop–Stix 2011 (Thm 26), Stix
arXiv:1203.3236 (Cor. 5), Stoll "Finite descent obstructions" (Cor. 8.8). The Lean file of E.27, from
`pro_prompts_done_20261111\LM3_TEICHMULLER_TOWER\LM3_TEICHMULLER_TOWER_background.zip`.

**Computations.** The four programs of the return (`af_checks.py`, `bc_counterexamples.py`, `d_counterexamples.py`,
`e_deletion_checks.py`) were copied to `rerun\code\` and rerun with `python -I`: all exit 0, and every output is
identical to the shipped one (`rerun\*.out`, `rerun\audit\E_computation.json`). The finite claims that carry weight
were redone independently in `rerun\indep_checks.py` (output `rerun\indep_checks.out`): the matrices
[[1,t],[0,1]] and [[0,1],[1,1]] over F_2[t]/(t³+t+1) have orders 2 and 3 and generate all 504 elements of SL_2(F_8),
which is simple (B.4); (12345) and (123) generate A_5, which is perfect (D.2); disc(t³−2) = −108 (B.5, D.20); the
residues of the profinite integer of B.15.

## 1. Result

| Verdict | Number | Statements |
|---|---|---|
| correct | 65 | of which conditional on an unrefereed 2026 claim, as the return says: D.8, D.9, D.10, D.12, E.17, E.20, E.24 |
| correct with a gap | 3 | B.10, C.12, C.13 |
| known in the literature | 30 | A.2, A.3, A.5, A.6, B.2, C.3, C.9, D.3, D.4, D.14, D.16, D.17, E.2–E.5, E.9, E.12, E.13, E.15, E.16, E.18, E.19, E.21, E.25, E.28, F.1, F.5, F.9, F.17 |
| unproved (left open) | 12 | open problems B.3, E.8; unrefereed 2026 claims D.7, D.13, E.26; left open by the return B.7, B.14, C.8, D.23, E.14, F.16, F.18 |
| wrong | 0 | — |

The return's own register (57 Proved, 30 Known, 11 Refuted, 12 Open) holds: every "Refuted" statement has a valid
counterexample, every "Open" statement is honestly open, and no "Proved" statement fails. Three proofs have a gap
(§3); none changes the conclusion that LM4–LM6 use, but C.12 is cited by LM6 in a form that is false (§5). Two
consequences that the return does not draw are in §4: Grothendieck's isomorphism (6) of scan 396 holds for every
type (from C.4, C.6, C.7), which corrects FINDINGS F21; and the element γ of scan 354 can be written down explicitly.

## 2. The statements

Verdicts: **correct**; **gap** (correct with a gap, §3); **known** (with the reference; "not reopened" means the
reference is the return's and its text was not available here); **unproved**; **wrong**. Scan numbers are cote 140-2.

### 2.1 Statements cited by LM4–LM6 (42)

| Id | Claim | Verdict | Reason | Cited by LM4/5/6 |
|---|---|---|---|---|
| A.3 | Birman sequences 1→Π_{g,n}→M^±_{g,n+1,*}→M^±_{g,n}→1 (old punctures permutable, orientation reversal allowed) and 1→Π→P_{g,n+1}→P_{g,n}→1; filling on π_1 kills the last loop | known | Birman exact sequence, Farb–Margalit Thm 4.6; the extended form has the same fibration proof. Checked against scans 187–189: his announced 1→π→Autext(π′,i)→Autext(π)→1 is this sequence, and his 𝒯^{00} sequence (identity on I and on T) is its pure orientation-preserving subgroup, of index 2·ν! by A.1: his "à un sous-groupe d'indice 2ν! près" is right | yes (LM4) |
| A.8 | Discr(π) = Isom_lac(Π̂,π)/Aut_lac(Π); Pré = I^out/Σ^±, Pré⁺ = I^out/Σ; oriented → unoriented is 2 to 1 | correct | formal; the 2-to-1 uses that the multiplier is ±1 on Σ^± and that −1 occurs | yes (LM6) |
| A.13 | pullback Ã = A ×_M M_*: kernels Π, A_0 and A_0 × Π (direct); π_1 of the homotopy quotient is M_* | correct | contractibility of A_0 (hyperbolic) and U = A/A_*; the product in (75) of §21 is direct | yes (LM4) |
| B.4 | the closure H of M^± is a proper subgroup of O_{g,n} = Out_lac(π̂) for every hyperbolic type | correct | the multiplier is ±1 on H; a curve over a number field gives elements with cyclotomic multiplier outside ±1 (scan 322, "n'est jamais un iso"). Finite witness for (1,0): SL_2(F_8) is a quotient of PSL_2(Z), simple of order 504, not a congruence factor; recomputed | yes (LM4) |
| B.5 | H_{0,3} = S_3 × ⟨c⟩ is not normal in O_{0,3} | correct | S_3 × G_Q ↪ O_{0,3}; normality would make ⟨c⟩ normal in G_Q, which the S_3-extension of t³−2 forbids; recomputed. Answers his margin question of scan 322 for 𝒯̂ | yes (LM4) |
| B.6 | conjugates of Σ ↔ O/N_O(Σ); fibres of O/Σ → O/N_O(Σ) are N_O(Σ)/Σ-torsors | correct | formal; his (17) of scan 326 | yes (LM6) |
| B.8 | N_{D̂}(D) = D for D free non-abelian or a closed surface group of genus ≥ 2 | correct | conjugacy separability and Grossman's Property A, then trivial centre of D̂ | yes (LM4, LM6) |
| B.9 | D ↦ D ∩ V is injective on based discretizations, V open | correct | for V normal, D_i = N_π(D_i ∩ V) by B.8; general V through the normal core. This is his Corollaire of scan 353 | yes (LM4) |
| B.10 | V ◁ π open, G = π/V: Λ ⊂ V extends, uniquely, iff G → Out_lac(V) factors through Out⁺_lac(Λ) | gap | pullback extension E ↪ π, Ê ≅ π, E torsion-free, Fuchsian by Kerckhoff's Thm 7; the loop step proves only that the closure of each maximal parabolic subgroup of E lies in an inertia group of π, not equality (§3). His conjecture of scan 352 | yes (LM4) |
| B.11 | surjectivity of Discr(π) → Discr(V) fails for z ↦ z² from type (0,4) to (0,3) | correct | C_B(s) is not open (s moves a twist of P_{0,4} ≅ F_2; unique roots), so by Baire some u in the closure B of P_{0,4} puts u⁻¹su outside the countable discrete group; B.10 forbids the extension. This proves his own NB of scans 353–354 ("ne doit pas tjs être bijective", "Un tel γ existe"); an explicit u is in §4.2 | yes (LM4) |
| C.1 | filling a Galois-stable set S_0 of punctures is the quotient by the closed normal subgroup generated by the inertia at S_0 | correct | standard (finite covers of U′ = covers of U unramified over S_0; char 0) | yes (LM5) |
| C.4 | C_{g,n+1} → C_{g,n} is an isomorphism (congruence kernels) | correct | snake lemma on the full Birman sequence (C.2) and the procongruence one (C.3); no congruence property assumed | yes (LM6) |
| C.5 | G_Q ≅ N^{arith,!}_{g,n}/P̌_{g,n} for every hyperbolic type; ker of universal monodromy = C_{g,n} | correct | Hoshi–Mochizuki 2011 Cor. 6.4 (read) gives J ∩ G_L = 1; G_Q has no non-trivial finite normal subgroup | yes (LM6) |
| C.6 | 1 → π̂_{g,n} → N^{arith,!}_{g,n+1} → N^{arith,!}_{g,n} → 1 is exact | correct | quotient of the universal-curve sequence by C_{g,n+1} ≅ C_{g,n} (C.4), with C_{g,n+1} ∩ π̂ = 1 (C.3). It is his (9) of scan 399 (read; N or M in the transcription). With C.7 it gives his (6) of scan 396 (§4.1) | yes (LM6) |
| C.10 | the classifying topos of π_1 of a curve is not its small étale topos | correct | two subterminal objects against all Zariski opens | yes (LM5) |
| C.11 | over a sub-p-adic K the arithmetic extension reconstructs X and Sh(X_ét), functorially for K-isomorphisms, on the essential image | correct | formal corollary of Mochizuki 1999 Thm A (Isom form); the basis-of-the-site argument is standard | yes (LM5) |
| C.12 | U(K) = U′(K) ∖ {x}; the point-induced section classes correspond in the same way | gap | the second sentence needs the point map of U′ to be injective, which is not among the hypotheses (§3); for all sections it is false | yes (LM6) |
| C.13 | for families, distinct sections can meet: in S × S → S, t ↦ (t,t) and t ↦ (2,t) meet over 2 | gap | correct for sections of the family, and it is his own withdrawal of scans 433–435 ("deux sections distinctes de U sur S peuvent ne pas être disjointes"); the closing claim that it is also an example for splittings over π_1(S) is not proved (§3) | yes (LM6) |
| D.2 | "the L_i are the maximal subgroups of π whose normalizer has open image" (scan 483) and its margin are false | correct | π itself; the closure of [π,π] is not procyclic (A_5 quotient; recomputed). Agrees with FINDINGS F17 | yes (LM6) |
| D.3 | U affine hyperbolic over a number field: z ≠ 1 lies in a cuspidal inertia group iff it has a cyclotomic normalizer | known | Nakamura 1994, Thm (2.1.1) (read) | yes (LM6) |
| D.5 | lifts transported from (V, v ∈ V(K), equivariant outer iso Δ_V ≅ Δ_U) are in bijection with U(K) | correct | D.1, Isom form, injectivity of points → sections | yes (LM6) |
| D.6 | the tangential section at 0 of P¹∖{0,1,∞} over Q is the section of no rational point | correct | its Kummer class under t is trivial; ∩_m Q^{×m} = {1} and 1 ∉ U | yes (LM6) |
| D.8 | the completion statement (D.7.1) of the 2026 paper gives X(k) ≅ Sec(X/k) for proper X of genus ≥ 2 | correct (conditional on (D.7.1)) | decomposition groups agree; Koenigsmann Prop. 2.4 (2) and Pop–Stix Thm 26 (both read) are used as stated; the explicit Hensel argument with q_r, p = 2 included, checked | yes (LM6) |
| D.9 | granted the local theorem: loc(Sec(C/K)) = C(A_K)_•^{f-cov}, and the section conjecture for C ⇔ that set is C(K) | correct (conditional) | Harari–Stix Thm 2.1; Stix Cor. 5 (read: the points are the non-cuspidal Selmer sections with finite support) | yes (LM6) |
| D.10 | granted the local theorem: a section of Y_1(N), g(X_1(N)) ≥ 2, becomes on X_1(N) the section of a unique rational cusp; cuspidality on Y_1(N) does not follow | correct (conditional on the 2026 local theorem) | Stoll Cor. 8.8 (read: X_1(N) of positive genus is excellent w.r.t. abelian coverings), D.9, Mazur | yes (LM6) |
| D.11 | an open homomorphism Π_U → Π_V of arithmetic groups over number fields maps Δ_U into Δ_V | correct | the image of Δ_U in G_L is a finitely generated closed normal subgroup, hence trivial (Mochizuki 2006, Thm 2.4; Hilbertian fields) | yes (LM6) |
| D.12 | granted Thm 1.1 of the 2026 open-Hom paper: the absolute Hom form (D.12.1) | correct (conditional) | base change, D.4, slimness for the conjugacy ambiguity | yes (LM6) |
| D.14 | profinite free groups of rank ≥ 2 and profinite surface groups are torsion-free and slim; G_K slim for number fields | known | Nakamura 1994 Cor. (1.3.4); Mochizuki 2004 Lemma 1.3.1; finite cohomological dimension (FINDINGS F5) | yes (LM4) |
| D.15 | slim G: an automorphism trivial on an open subgroup is trivial; C_G(x^m) = closure of ⟨x⟩ for x in a free basis, or x a standard simple generator of a closed surface group | correct | first part: normal-core argument (proves Lemme 5, scan 498, without (2), (4)); free case Nakamura 1994 Lemma (2.1.2) (read); closed case ν = 0 ((4) of scan 501): Boggi–Zalesskii 2019 Prop. 3.6 as cited (not reopened), and independently Mochizuki 2007 Prop. 1.2 (ii) (read), §4.3 | yes (LM4) |
| D.17 | G_Q ≅ N^arith_{g,n}/Σ_{g,n}, ordered and unordered points | known | Hoshi–Mochizuki 2011 Cor. 6.4 (read) and slimness; same as C.5 | yes (LM6) |
| D.19 | for the tripod over a sub-p-adic K, the centralizer of ρ_U(G_K) in Out(Δ_U) is S_3 | correct | D.1 and Isom form; also known (Mochizuki 2004 Thm 1.3.4, F6). Answers his NB of scan 485 | yes (LM6) |
| D.22 | over a number field the only G_K-invariant loop structure of type (0,3) on π_1(P¹∖{0,1,∞}) is the usual one | correct | primitive abelian images force the cyclotomic exponent; then D.3 and maximality | yes (LM6) |
| D.23 | invariant-loop uniqueness in other affine types; classification of admissible moduli splittings | unproved | left open by the return; the primitive-vector argument fails at (1,1) | yes (LM6) |
| E.2 | G_Q ≅ Γ^arith_{g,n} for every hyperbolic type | known | Hoshi–Mochizuki 2011 Cor. 6.4 (= D.17) | yes (LM6) |
| E.7 | normalizer quotients: Γ^norm_{0,3} ≅ GT̂_0, Γ^norm_{0,n} ≅ GT̂ for n ≥ 4 | correct | n ≥ 4: E.6 with E = P̂_{0,n+1}, Out(E) = GT̂ × S_{n+1} (Hoshi–Minamide–Mochizuki), the point stabilizer S_n is self-normalizing; n = 3: N(S_3) = S_3 × C(S_3) and C(S_3) = Out^♯_4 = GT̂_0 (Harbater–Schneps). Agrees with FINDINGS F3 | yes (LM4) |
| E.10 | Γ^norm_{1,1} ≅ GT̂ | correct | E = P̂_{1,2}, Out(E) = GT̂ (Minamide–Nakamura); π̂_{1,1} characteristic through K = C_2 ∗̂ C_2 ∗̂ C_2; the peripheral element ζ_3² goes to its λ-th power | yes (LM4) |
| E.17 | granted Cor. 8.5 of the 2026 section paper: a modular section on Y_1(N) compactifies to a rational cusp section | correct (conditional) | as D.10 | yes (LM6) |
| F.2 | strict completion of a category with finitely many objects by its finite congruences; continuous functors to finite categories are the functors of the pro-object | correct | surjective transitions make every finite datum factor through one stage | yes (LM5) |
| F.3 | functors may not be identified under arbitrary natural transformations: [1] against the point, 3 against 2 subterminal objects | correct | finite counterexample | yes (LM5) |
| F.4 | Fun_cts(lim C/R, FinSet) ≃ colim Fun(C/R, FinSet); continuous sets need not factor through one stage | correct | Ẑ acting on ⊔ Z/m!Z | yes (LM5) |
| F.9 | finite boundary-constructible étale sheaves of sets on M̄_{0,n} ≃ Fun_cts(Ĉ_n, FinSet), with stalks | known | Barwick–Glasman–Haine 2020 Prop. 12.6.4, Cor. 12.6.6–7, and Jansen 2023 (not reopened), with F.2 | yes (LM5) |
| F.18 | is the nerve of the strict completion the full profinite stratified ∞-category? | unproved | left open; the return names n = 4 as the first test | yes (LM5) |

### 2.2 The other statements (68)

| Id | Claim | Verdict | Reason | Cited by LM4/5/6 |
|---|---|---|---|---|
| A.1 | M^± → S_n and the orientation character are onto; their joint kernel is P_{g,n}; homeomorphisms of U extend to X | correct | standard; his Γ_{g,ν} permutes punctures and has χ onto ±1 (scans 225–226) | no |
| A.2 | presentation of Π_{g,n}; free of rank 2g+n−1 for n ≥ 1; M^± ≅ Out_lac(Π) | known | Farb–Margalit Thms 8.1, 8.8 | no |
| A.4 | a finite covering gives 1 → N_Π(H)/H → Lift(p) → L_H → 1, a correspondence | correct | lifting criterion; periodic maps are not isotopic to 1 | no |
| A.5 | moduli stack [𝒯/P]; M_{0,3} = Spec Q, M_{0,[3]} = BS_3 | known | Teichmüller contractibility (Farb–Margalit Thm 10.6), Riemann existence for DM stacks | no |
| A.6 | arithmetic and universal-curve exact sequences; ρ: A^arith → O | known | homotopy exact sequences; Hoshi–Mochizuki 2011 Cor. 6.4 | no |
| A.7 | M̂⁺ ↠ Σ (closure), kernel the congruence kernel | correct | formal | no |
| A.9 | N^arith ⊆ N^norm, G_Q ↠ N^arith/Σ | correct | formal | no |
| A.10 | the fibres of I^out/Σ → I^out/N^arith are N^arith/Σ-torsors | correct | formal | no |
| A.11 | non-hyperbolic types; for (0,2) ρ_π = ρ_perm·ε | correct | read: his identification of the two ρ (scan 225) is false (his own z ↦ z̄ fixes both punctures and acts by −1 on Π); "dét. 1" (scan 227) is false in rank 1 (z ↦ 1/z acts by −1) | no |
| A.12 | complex curves are orientable; real structure is an extension by G_R; char 0 scope | correct | | no |
| B.1 | C_{g,n} = 1 ⇔ congruence topology = profinite ⇔ cofinality; no statement about normality | correct | | no |
| B.2 | CSP holds in genus 0, 1 (n ≥ 1), 2 (all n), also with permutations and orientation reversal | known | Asada 2001; Boggi 2009 Thm 3.5; Boggi 2020 Thm 1.4 (ii) (closed genus 2); range confirmed in FINDINGS F4 | no |
| B.3 | CSP for g ≥ 3, first case (3,0) | unproved | open problem | no |
| B.7 | Σ ◁ O_{g,n}? | unproved | left open; at (0,3) it is equivalent to O^!_{0,3} = GT̂_0 (§4.4); LM3b A.3, A.14 claim the pro-ℓ analogue fails | no |
| B.12 | restriction descends to strict and non-strict prediscretizations | correct | his scan-357 argument for the strict case; density and continuity for the closure case | no |
| B.13 | coset criteria: injective ⇔ f⁻¹(B′) = B, onto ⇔ A′ = f(A)B′; normalizer comparison | correct | formal; his ⓐ–ⓒ of scan 358 | no |
| B.14 | bijectivity of prediscretizations under finite covers | unproved | left open; injectivity of restriction of automorphisms shown by slimness | no |
| B.15 | raw discretization injectivity fails under filling (0,4) → (0,3) | correct | conjugation by x^α, α ∈ Ẑ∖Z. It refutes a hypothesis of the prompt; scan 400 asserts only the bijection (14) of prediscretization torsors | no |
| C.2 | 1 → π̂_{g,n} → P̂_{g,n+1} → P̂_{g,n} → 1 is exact | correct | centre-freeness gives injectivity; right exactness of completion | no |
| C.3 | the procongruence Birman sequence is exact | known | Boggi 2020 Cor. 4.7 (not reopened) | no |
| C.7 | a cusp class gives θ_i: O_{g,n+1,i} → Aut_lac(π′) | correct | N_π(I_i) = I_i | no |
| C.8 | the "??" row of scan 399 ⇔ θ_i iso ⇔ bijection of prediscretizations | unproved | the equivalences are proved; the row is left open (LM3b B.4–B.5 claim it fails at (0,4) → (0,3)) | no |
| C.9 | combinatorial cuspidalization: injective for n ≥ 1, bijective for n ≥ 3 (affine), n ≥ 4 (proper) | known | Hoshi–Mochizuki 2011 Thm 6.1 (read: n_0 = 2 affine, 3 proper, bijective for n ≥ n_0 + 1) | no |
| D.1 | a centre-free extension is the pullback of Aut → Out | correct | standard | no |
| D.4 | relative Hom form over sub-p-adic fields | known | Mochizuki 1999 Thm A | no |
| D.7 | the 2026 claim: proper p-adic section conjecture | unproved | unrefereed external claim; not used unconditionally | no |
| D.13 | the 2026 claim: Hom form of Neukirch–Uchida for solvably closed extensions | unproved | unrefereed external claim | no |
| D.16 | ρ_U is faithful for every hyperbolic curve over number fields and p-adic fields | known | Hoshi–Mochizuki 2011 Thm C, Cor. 6.3; Belyi for the tripod | no |
| D.18 | faithfulness passes to finite étale covers | correct | D.15; his Corollaire 2 (scans 499–500) | no |
| D.20 | faithfulness fails for (0,0), (0,1), (0,2), (1,0) | correct | CM by Z[i] over Q(i); cyclotomic character for G_m | no |
| D.21 | quotienting by orientation reversal kills complex conjugation; real sections ↔ π_0(U(R)) | correct | Bresciani–Vistoli for the real statement (agrees with FINDINGS F18) | no |
| E.1 | G_Q ↠ Γ^arith ↪ Γ^norm; the conjectures of §26 and §29 differ | correct | formal | no |
| E.3 | (Γ^arith)^ab ≅ Ẑ^× | known | E.2 and Kronecker–Weber | no |
| E.4 | Out^♯(P̂_{0,4}) ≅ GT̂_0, Out^♯(P̂_{0,m}) ≅ GT̂ for m ≥ 5 | known | Harbater–Schneps 2000, Main Theorem (FINDINGS F3) | no |
| E.5 | Out(P̂_{0,m}) ≅ GT̂ × S_m for m ≥ 5 | known | Hoshi–Minamide–Mochizuki, Kodai 2022 (F3, F27) | no |
| E.6 | normalizer lemma N/S^! ↪ Out(E) | correct | | no |
| E.8 | G_Q → GT̂ surjective? | unproved | open problem | no |
| E.9 | P_{1,2} ≅ B_4/Z(B_4), Out(P̂_{1,2}) ≅ GT̂ | known | Minamide–Nakamura (F27) | no |
| E.11 | Γ^norm_{1,2} ≅ A/S_2 | correct | exact reduction through E.6 | no |
| E.12 | refined actions with quilts (Nakamura–Schneps 2000, Hatcher–Lochak–Schneps 2000) | known | not reopened | no |
| E.13 | automorphisms of the procongruence outer tower = GT̂ | known (preprint, unrefereed) | Boggi arXiv:2011.15075v6, Thm 6.23 (F27) | no |
| E.14 | every element of A in E.11 preserves non-separating inertia | unproved | left open | no |
| E.15 | Pop's tripod reconstruction needs the birational system | known | Pop 2018 (not reopened) | no |
| E.16 | Hoshi–Mochizuki–Tsujimura 2025 Thm C (ii) characterizes the GT̂-conjugates of G_Q | known | not reopened | no |
| E.18 | pro-ℓ Galois rigidity of M_{0,m}, ℓ odd | known | Nakamura 1994 Thm A (read) | no |
| E.19 | the rational solution Lie algebra W is grt_1; Brown's injection | known | Drinfeld 1990; Bar-Natan 1998; Brown 2012 | no |
| E.20 | granted the 2026 all-weight bound: G_MT ≅ GRT | correct (conditional) | dimension squeeze | no |
| E.21 | G_Q ↪ GT̂ → GT_ℓ ↪ GT(Q_ℓ); the second arrow is not injective; the images are not open | known | the arguments given are also correct | no |
| E.22 | surjectivity ⇔ density ⇔ exhaustion of finite quotients | correct | formal | no |
| E.23 | equal unipotent completions do not give profinite equality (1 ⊂ C_2) | correct | | no |
| E.24 | granted the 2026 freeness: abelianizations of W, GRT_1, GRT | correct (conditional) | | no |
| E.25 | the odd generators are dual to Ext¹(Q(0), Q(2k+1)) | known | Brown 2012; Hain–Matsumoto 2003 | no |
| E.26 | the 2026 all-weight upper bound | unproved | unrefereed external claim | no |
| E.27 | the attached Lean comparator is not a checked proof | correct | checked: `DeligneDrinfeld.lean` in the LM3 background zip ends with `theorem main : MainStatement := by sorry` | no |
| E.28 | status record: Willwacher arXiv:2610.15592v4 | known (record) | not reopened | no |
| F.1 | Jansen's exit category C_n; 4 and 26 objects for n = 4, 5 | known | Jansen 2023 (not reopened); the counts 1+3 and 1+10+15 recomputed | no |
| F.5 | profinite curve complex and multitwist stabilizers in genus 0 | known | Boggi 2020 (not reopened) with genus-0 CSP | no |
| F.6 | the completion of a stabilizer is its closure; H_σ, Δ_σ closed | correct | five lemma; conjugacy separability | no |
| F.7 | the transporter quotients C_{n,V} are cofinal; Hom = closure(A_st)/Δ̄ | correct | A_st is one coset H_{σ_t}r; the cofinality argument checked | no |
| F.8 | forgetting, clutching, relabelling extend to the completion | correct | | no |
| F.10 | continuous outer G_Q-action on Ĉ_n, faithful for n ≥ 4 | correct | Belyi at n = 4, forgetting above | no |
| F.11 | the lifting groupoid at q_{12,34} is BẐ, so smoothness fails | correct | kernel {(a,−a)} | no |
| F.12 | an autoequivalence of Ĉ_n is detected on the open stratum; inertia-preserving automorphisms extend | correct | relies on Boggi–Funar 2023 and Boggi 2026 Prop. 3.5 (imported) | no |
| F.13 | automorphisms of the decorated two-level boundary tower = GT̂ | correct | F.12 and Harbater–Schneps; coherence from trivial centres | no |
| F.14 | the same for the whole genus-0 boundary tower | correct | same | no |
| F.15 | the elliptic types (1,1), (1,2) keep their stack isotropy after completion | correct | sketch; genus-1 CSP | no |
| F.16 | positive-genus automorphism comparison | unproved | left open | no |
| F.17 | rational operadic analogue: GT(k), GRT(k) | known | Drinfeld 1990; Bar-Natan 1998 | no |

## 3. Wrong items and gap items in full

**Wrong: none.**

**B.10 (gap in the loop step; the conclusion holds).** After E has been shown to be a torsion-free Fuchsian group
with E ∩ V = Λ, the proof says that the closure P̄ of a maximal parabolic subgroup P of E "is the centralizer in π
of the corresponding peripheral subgroup of V", citing Boggi–Zalesskii Prop. 3.6. That proposition gives
C_π(I_V) = I_π, where I_V is the closure of P ∩ Λ and I_π the inertia group of π containing it; since P centralizes
P ∩ Λ, it gives P̄ ⊆ I_π, not equality. Missing: [P̄ : I_V] = [I_π : I_V]. Proof of the missing step: I_π/I_V is the
stabilizer in G of the V-conjugacy class of I_V (because N_π(I_V) = I_π); P/(P ∩ Λ) is the stabilizer in G of the
corresponding cusp of the surface of Λ; the deck action on Λ induces that on V, so the cusps of Λ and the inertia
classes of V correspond G-equivariantly and the two stabilizers coincide. Every inertia class of π is reached
because G-orbits correspond. With this, the loop structures of E and π agree and B.10 holds as stated.

**C.12 (missing hypothesis).** The statement is for "a smooth curve U′ over a field K". Its second sentence, the
bijection of point-induced section classes, holds only when the point map U′(K) → Sec(U′/K) is injective; the proof
quotes D.5 (hyperbolic curves over sub-p-adic fields) for this. It fails for K algebraically closed (one section
class) and for U′ = P¹ or A¹. Correct statement: U′ hyperbolic (or G_m) over a number field or a finite extension
of Q_p. Separately, the statement is about point-induced classes only, and the return says so: for the full section
sets, deleting x adds the cuspidal packet at the new cusp x, and these sections map onto the class of x in
Sec(U′/K), so the class of x is not deleted from the image of Sec(U) → Sec(U′).

**C.13 (scope).** The counterexample is correct for sections of the family (morphisms S → S × S): the diagonal does
not survive the deletion of the constant section 2. The last sentences of the proof say that this "also gives a
geometric example for the acting group π_1(S)", i.e. for splittings of the extension of π_1 of the family. That is
not proved: a splitting for the deleted family (S∖{2}) × S lifting the diagonal's splitting is a G_Q-compatible
homomorphism φ: π_1(S) → π_1(S∖{2}) whose composite with the filling map is the identity. Over Q̄ such φ exist (a
free profinite group is projective); over Q their non-existence is a relative section statement the example does not
decide. Grothendieck's own argument (scan 434) is made with sections of U over S, "moralement" identified with
splittings, so C.13 refutes the formula in that form. To close: restrict C.13 to sections of the family, or prove
that the filling map has no G_Q-compatible splitting here.

## 4. Consequences and checks that are not in the return

**4.1 His isomorphism (6) of scan 396 holds for every type with (g, ν−1) hyperbolic.** On scans 396–397 he states
(6) N^!_{g,ν} ≅ M^!_{g,ν−1}: ψ_i: 𝒯̂̂^!_{g,ν} = Out_lac(π̂_{g,ν}) → 𝔊̂̂^!_{g,ν−1} = Aut_lac(π̂_{g,ν−1}) maps the
arithmetic image N^!_{g,ν} isomorphically onto M^!_{g,ν−1}, the image of the arithmetic universal-curve group in
Aut_lac(π̂_{g,ν−1}), which is the inverse image of N^!_{g,ν−1} there. His ψ_i is θ_i of C.7. Proof from LM3:
if ψ_i(n) = 1 for n ∈ N^!_{g,ν}, then n maps to 1 in N^!_{g,ν−1}, so by C.6 n lies in the point-pushing copy of
π̂_{g,ν−1}, on which θ_i is the inner embedding (C.7); hence n = 1. For β in the inverse image of N^!_{g,ν−1}, C.6
gives n with the same outer class, and ψ_i(n)β⁻¹ is inner, hence ψ_i of a point-pushing element. So (6) is
equivalent to (9), and (9) is C.6. In terms of kernels: the kernel of π_1(M_{g,ν}) → Out(π̂_{g,ν}) is C_{g,ν} (C.5),
that of π_1(M_{g,ν}) → Aut(π̂_{g,ν−1}) is the lift of C_{g,ν−1} centralizing the fibre, and the two coincide because
C_{g,ν} → C_{g,ν−1} is an isomorphism (C.4). No congruence subgroup property is used: C.4 rests on the full and the
procongruence Birman sequences (C.2, C.3). This corrects FINDINGS F21 and
`LM_EXPERT\work\lit\LIT_LM6_anabelian.md` 0.4 (c), which reduce (6) to a comparison of congruence kernels and take
that comparison to be the congruence subgroup property (F4): C.4 is that comparison, and it holds unconditionally.
His own reduction on scan 397 ((6) bijective ⇔ Θ_{g,ν}, Θ_{g,ν−1} have the same kernel) is valid when 𝒯̂ is read as
the closure, the reading his N^! forces; with C.5 both kernels are trivial.

**4.2 The element γ of scan 354, explicitly.** In B.11 take u = T_a^α with α ∈ Ẑ∖Z and a a curve on
P¹∖{0,∞,1,−1} moved by the deck involution s (z ↦ −z), for instance a separating {0,1} from {−1,∞}. Then
u⁻¹su = s·T_{s(a)}^{−α}T_a^{α}. If this lay in the discrete group, T_{s(a)}^{−α}T_a^{α} would be a discrete element
of the closure of P_{0,4}, hence in P_{0,4}; but its image in P̂_{0,4}^{ab} = Ẑ² (basis the classes of T_a and
T_{s(a)}, two of the three boundary loops of M_{0,4}) is (α, −α) ∉ Z². So Λ′ = ũ(Λ) is a discretization of V that
does not extend to π̂_{0,3}: this is his γ for π = π̂_{0,3} and π′ of index 2, as LM4 Part D (c) asks, without the
Baire argument.

**4.3 D.15 for ν = 0 has a second source in the literature already read for LM4.** Mochizuki 2007 ("A combinatorial
version of the Grothendieck conjecture"), Prop. 1.2 (ii), read in the local copy: edge-like subgroups of the
PSC-fundamental group are commensurably terminal. For a non-separating simple loop x of a closed surface of genus
≥ 2, the closure of ⟨x⟩ is the edge-like subgroup of the one-node degeneration that pinches x; an element
centralizing x^m commensurates it, so C(x^m) = N(closure of ⟨x^m⟩) = closure of ⟨x⟩. This is (4) of scan 501 for
ν = 0, independently of Boggi–Zalesskii Prop. 3.6 (which this review could not reopen). FINDINGS F5 ("(4) for ν = 0:
no theorem found") is answered by both.

**4.4 B.7 at (0,3) in exact form.** Σ_{0,3} = S_3 is normal in O_{0,3} if and only if every label-preserving element
of O_{0,3} commutes with S_3, i.e. O^!_{0,3} = C(S_3) = Out^♯_4 = GT̂_0. (If S_3 is normal, [O^!, S_3] ⊂ O^! ∩ S_3 = 1;
conversely O = O^! ⋊ S_3 becomes a direct product.) So B.7 at (0,3) asks whether the symmetry and hexagon relations
follow from the inertia conditions alone in Aut(F̂_2).

**4.5 Manuscript passages checked against the return's readings.** Scan 189 (A.3: index 2ν!, correct); scans 225,
227 (A.11: both errors of the manuscript confirmed); scan 322 (B.4: "n'est jamais un iso"; B.5: the margin's
"question judicieuse" whether 𝒯̂ is normal, answered no); scans 352–358 (B.9 is his Corollaire, B.10 his
Conjecture, B.11 his NB, B.12 his scan-357 argument, B.13 his ⓐ–ⓒ); scans 395–401 (C.6 is his (9); (14) of scan 400
concerns prediscretization torsors, not raw discretizations); scans 433–435 (C.13 is his withdrawal); scans 483–486
(D.2 quotes the conjecture and margin exactly; D.19 answers the NB of scan 485); scans 496–501 (D.14, D.15, D.18
match his Théorème 2, Lemme 5, (2), (4) and Corollaire 2).

**4.6 A wording point in B.4.** "Read as an assertion about bare fundamental groups outside that range, it is false"
is true only for (0,0) and (0,1); for (0,2) and (1,0) the inclusion is still proper, as the proof itself shows.

## 5. What LM4, LM5 and LM6 must change in their "After the returns" blocks

**All three blocks.** The sentence "None has been reviewed line by line yet" / "Neither has been reviewed line by
line yet" becomes: "LM3 was reviewed line by line on 12 November 2026 by Claude Opus 5.5 (effort max)
(`LM3_REVIEW_OPUS\REVIEW.md`, attached): no statement wrong, three with gaps (B.10, C.12, C.13); LM2 and LM3b are not
yet reviewed." Attach this review beside `LM3_return/` and name it in WHAT IS ATTACHED.

**LM4_FINITE_GROUP_ACTIONS**

| Bullet | LM3 statements | Action | Text to use |
|---|---|---|---|
| Profinite groups with loops | D.14 | keep | — |
| same | D.15 | correct | replace from "which no theorem read for this prompt gives" to the end of the bullet by: "Checked (review of 12 Nov): D.15 holds, ν = 0 included. (4) for ν = 0 is Boggi–Zalesskii 2019 Prop. 3.6, and also Mochizuki 2007 Prop. 1.2 (ii) applied to the one-node degeneration pinching x_i (edge-like subgroups are commensurably terminal); Lemme 5 needs only the trivial centralizers of open subgroups. Part A (c) starts from D.15; its weight moves to the abstract axioms and to the m-step solvable quotients." |
| Discretizations along coverings | B.8, B.9 | keep | add "(checked)" |
| same | B.10 | correct | add: "checked; one step is to be written out: the closure of each maximal parabolic subgroup of the extension is a full inertia group of π (LM3 proves only the inclusion; equality follows by comparing the stabilizers in G of the cusps of Λ and of the inertia classes of V)." |
| same | B.11 | correct | replace "(Refuted there): surjectivity fails … which is his γ of scan 354" by: "(Refuted there, checked): surjectivity fails for the covering of degree 2 of the sphere with three holes, as his own NB of scans 353–354 says. An explicit γ: conjugation by T_a^α, α ∈ Ẑ∖Z, for a curve a moved by the deck involution; then u⁻¹su = s·T_{s(a)}^{−α}T_a^{α} has abelian image (α, −α) ∉ Z² and is not discrete (review §4.2)." In "Check B.9–B.11 and C.2" keep only "Check C.2" (LM3b). |
| The centralizer of S_3 … | E.7, E.10 | keep | add "(checked)" |
| How large the full groups are | B.4, B.5 | keep | add "(checked)" |
| The exact groups in his drilling theorem | A.3, A.13 | correct | replace "Check them against … before proving Part A (d)" by: "Checked against scans 187–189: his announced 1 → π → Autext(π′, i) → Autext(π) → 1 is A.3's extended sequence, and his 𝒯^{00} sequence is its pure orientation-preserving subgroup, of index 2·ν! (A.1): the index is right." |

**LM5_MULTI_GALOIS_TOPOI**

| Bullet | LM3 statements | Action | Text to use |
|---|---|---|---|
| The mixed topos … | C.10, C.1 | keep | — |
| same | C.11 | keep | may add "(a formal corollary of Mochizuki 1999, Thm A, on the essential image)" |
| Functors up to isomorphism … | F.2, F.4, F.3 | keep | — |
| Stratified versions | F.9 | correct | "finite étale covers of M̄_{0,n} constructible along its boundary" → "finite étale sheaves of sets on M̄_{0,n} constructible along its boundary, with their stalks" |
| same | F.18 | correct | "LM3 F.18 and LM3b H.9 (Open there): … the first case is n = 5" → "LM3 F.18 (Open there) leaves the comparison for all finite homotopy types open and names n = 4 as the first test; LM3b H.8 claims n = 4 and H.9 leaves n = 5, the first case with chains of three strata." |

**LM6_POINTS_AS_SECTIONS**

| Bullet | LM3 statements | Action | Text to use |
|---|---|---|---|
| The loop structure … | D.2, D.3, D.22 | keep | add "(checked)" to "check D.2, D.3" |
| Hom-forms, the commutant … | D.11, D.12, D.19 | keep | — |
| Sections | D.5, D.6, D.8, D.9 | keep | D.6 and D.9 "checked" |
| same | D.10, E.17 | correct | "D.10 and E.17: every section …" → "D.10 and E.17, granted the local section theorem of the 2026 paper (unrefereed; for E.17 its Cor. 8.5), with Stoll Cor. 8.8 and Mazur: every section …" |
| same | C.12 | correct | "LM3 C.12: deleting a rational point deletes exactly its class of sections" → "LM3 C.12: deleting x ∈ U′(K) removes exactly x from the rational points, hence the class of x from the point-induced section classes when the point map of U′ is injective (U′ hyperbolic over a number field or a p-adic field); the full section set of U′ ∖ {x} gains the cuspidal packet at x, which maps onto the class of x." |
| same | C.13 | correct | after "this is his own withdrawal of scans 433–435" add: "(for sections of the family; whether the diagonal's splitting of π_1 survives the deletion is not decided by the example)." In "check D.6, D.9, D.10 and C.13", these four are checked; the ask "decide what E.17 leaves" stays. |
| The modular side | C.5, D.17, E.2, C.4, C.6 | keep, and add | after "C.6: his fundamental exact sequence (9) of scan 399 is exact." add: "With C.4 and C.7 this gives his isomorphism (6) of scan 396, N^!_{g,ν} ≅ M^!_{g,ν−1}, for every type with (g, ν−1) hyperbolic, without the congruence subgroup property (review §4.1)." |
| same | D.23 | keep | — |
| The lattice of a rational point | B.8, A.8, B.6 | keep | — |

**Outside the blocks (for whoever assembles the prompts; the review changes no file).** (1) LM4 Part A (c) asks to
"prove what the literature named here does not give: (4) for ν = 0"; by §4.3 it is given by Mochizuki 2007 Prop. 1.2
(named there) and by Boggi–Zalesskii Prop. 3.6, so the ask becomes "write out (4) for ν = 0 from these". (2) LM4
Part D (c) is answered by B.9, B.10 (with the step of §3) and B.11 with §4.2; what remains of it is the image for
non-normal π′ and the fixed sets. (3) LM6 Part B (f) says "what remains of his isomorphism (6) is a statement about
congruence kernels, known for g ≤ 2": by §4.1 (6) holds for all types; that sentence is to be corrected, and FINDINGS
F21 with it.

## 6. Limits of this review

The imported theorems marked "not reopened" (Boggi 2009, 2020, 2026; Boggi–Zalesskii 2019; Boggi–Funar 2023;
Kerckhoff 1983; Jansen 2023; Barwick–Glasman–Haine 2020; Minamide–Nakamura; Hoshi–Minamide–Mochizuki; Harbater–
Schneps; Pop 2018; Hoshi–Mochizuki–Tsujimura 2025; Nakamura–Schneps; Hatcher–Lochak–Schneps; Brown; Hain–Matsumoto;
Willwacher) were taken at the statement the return gives; where FINDINGS confirms one (F3, F4, F5, F27), that is said
in the table. The three 2026 proof packs (D.7, D.13, E.26) were not audited; the review checked only that the return
uses them conditionally and that each conditional deduction (D.8–D.10, D.12, E.17, E.20, E.24) is valid. F.8 and
F.11–F.15 were checked at the level of the arguments given, which rest on the imported Boggi–Funar and
Harbater–Schneps theorems. LM3b and LM2 were not reviewed; their statements in the blocks were left as they are.

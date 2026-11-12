# Review of the return LM3b_TEICHMULLER_PUSH, statement by statement

Claude Opus 5.5 (effort max), 12 Nov 2026 (written 17:46–18:30 UTC).

The return: GPT-6 Astra (ChatGPT Pro mode), 11 November 2026, `answers\LM3b_TEICHMULLER_PUSH.zip`, extracted unchanged
into `return\` beside this file. It has 93 numbered statements (53 Proved, 11 Refuted, 14 Open, 15 Known). This review
reads every statement against its proof in `LM3b_TEICHMULLER_PUSH_paper.md` (the same text as the `.tex`).

## Verdicts in one line

| Verdict | Count | Statements |
|---|---:|---|
| correct | 62 | all Proved and Refuted rows except G.8, G.9 |
| correct with a gap | 2 | G.8, G.9 |
| unproved (the 14 Open rows; the return says they are open) | 14 | A.4, A.16, B.8, B.11, C.7, C.9, D.4, E.4, E.9, F.4, F.6, F.12, H.5, H.9 |
| wrong | 0 | — |
| known | 15 | A.8, B.6, C.3, D.6, D.7, D.10, D.11, D.12, D.13, E.6, E.7, E.8, F.9, F.10, G.10 |

No statement was found false. Of the 35 statements that LM4, LM5 and LM6 cite, 27 are correct, 3 known and 5 open as
the return says. Two descriptions of them in the prompts are inaccurate (C.10 in LM4, H.7 in LM5) and are corrected in
the last section. Every Open row describes its obstruction accurately. For four Known rows (D.6, D.7, D.10, E.6) and
for the theorem numbers of D.12, A.8 and H.8, the source was not read here: the verdict records the reduction, which
was checked, and the attribution the return gives.

## How the review was done

- **Proofs.** Every proof was read and its steps were rederived, by hand where the argument is algebraic. Where a step
  rests on a cited theorem, the review checks that the theorem, as the return states it, gives the step.
- **Computations rerun.** All sixteen programs of `code\` were read and then run from a copy (`rerun\code\`), each under
  `python -I -B` through a small runner (`checks\runner.py`) that appends the code folder to `sys.path`; the two C++
  programs were compiled with g++ 13.2.0 (MinGW). Environment: Python 3.13.9, SymPy 1.13.1 (the return used 3.12.14,
  SymPy 1.14.0, GCC 14.2.0). Every output equals the shipped one: JSON structurally, the CSV row by row (after
  dropping the blank rows that Windows line endings add), the C++ logs (except the line naming the output path) and
  the 64 regenerated certificates exactly (`checks\cmp.py`; logs in `rerun\logs\`). The return's own runner
  `reproduce.py` was not used, because it builds in the system temporary folder. Nothing reached the network.
- **Independent checks (own code, sharing nothing with the return).**
  `checks\indep_c5.py`: C.5 recomputed from scratch, with the degree-4 terms of the conjugator kept as unknowns
  (120 unknowns instead of 39). `checks\indep_lie.py`: the explicit witnesses of A.3, B.3, A.14, F.1 and C.5.
  `checks\indep_g10.py`: the mechanism of G.10 run on the actual grt₁ solutions of weights 3, 5 and 8, with a negative
  control in weight 7. Outputs are the `.out` files beside them.
- **Manuscript.** `second_pass\LM_P0NN_checked_fixed.tex` (else `_checked.tex`) at scans 124, 129, 322–324, 348,
  362–363, 399 and 483–486, wherever a statement reads or corrects the manuscript.
- **The LM expert's findings** (`LM_EXPERT\FINDINGS.md`): F3, F4, F17, F20, F24, F27 were used where they bear on a
  statement.

## The table

The 35 statements cited by LM4–LM6 come first, then the other 58. "Open" rows are given the verdict *unproved (open)*.

### Statements cited by LM4, LM5 or LM6

| Id | Claim | Verdict | Reason | Cited |
|---|---|---|---|---|
| A.3 | For every prime ℓ, 2 and 3 included, the geometric S₃ is not normal in Out_lac(F₂^(ℓ)). | correct | A degree-5 special derivation whose outer class is moved by the transposition (A.2) lifts to a special automorphism (A.1). A label-preserving element that normalizes S₃ centralizes it, because the special subgroup is normal and meets S₃ trivially. The witness was rederived with the review's own code. No division by 6 is used. | LM4 |
| A.4 | Open: whether S₃ is normal in the full profinite Out_lac(F̂₂). | unproved (open) | The obstruction is stated correctly: A.1's corrections kill the error only in nilpotent quotients. Same status as LM3 B.7. The expert found no proof of GT̂ ≠ GT̂₀ (F3). | LM4 |
| A.6 | Σ₀,₄ is not normal in O₀,₄, in the full profinite group and in every pro-ℓ group. | correct | Pro-ℓ: the lift of B.3's E lies in ker θₓ; if it normalized Σ it would normalize the point-pushing group K and, being in ker θₓ, centralize it, but its bracket with v is nonzero (rechecked). Profinite: B.5's b would lie in N(K), where the filling kernel is K (B.6), so b ∈ K, which is false. | LM4 |
| A.9 | In the pro-ℓ types (0,3), (0,4), (1,1) the conjugates of Σ form a Cantor space containing a closed copy of Z_ℓ. | correct | t ↦ a^t·N is injective on Z_ℓ, since (t−s) times a non-invariant leading class stays non-invariant in a torsion-free module (A.13); a compact homogeneous space without isolated points is a Cantor space. | LM4 |
| A.11 | For ℓ ∤ 6, every S₃-invariant class of S_n/S_{n+1} lifts to the centralizer of S₃ in S_n. | correct | S_n is pro-ℓ (inside the kernel on the Frattini quotient), S₃ acts coprimely, and fixed points lift through finite ℓ-quotients and by compactness. | LM4 |
| A.13 | The IA part of Out(F_r^(ℓ)), r ≥ 2, has no torsion, ℓ = 2 included. | correct | The graded pieces embed in Hom(H, L_{n+1})/ad L_n; ad L_n is saturated (an element commuting with all generators mod ℓ is scalar in the free associative algebra); ⋂ O_n = 1 by compactness; a torsion element would have leading term mD = 0. | LM4 |
| A.14 | For every ℓ, 2 included, the geometric subgroup Σ₁,₁^(ℓ) is not normal in O₁,₁^(ℓ). | correct | c = −I is the only nontrivial central involution of Σ (A.13 applied to z and zc), so every normalizing element commutes with c. The degree-7 derivation satisfies [D(a),b] + [a,D(b)] = 0 (checked by hand and by code) and is not inner; its lift fixing [a,b] (A.12) is moved by c to leading term −D, and 2D ≠ 0. | LM4 |
| A.16 | Open: profinite normality at (1,1), and the elliptic normalizer quotient in all degrees. | unproved (open) | Correctly isolated. | LM4 |
| B.4 | The outer filling map fₓ and the genuine map θₓ are onto, profinitely and pro-ℓ. | correct | A special automorphism of F̂(y,z) fixing yz extends by x ↦ x to F̂(x) ∐ F̂(y,z), and so does its inverse; permutations are geometric; multipliers come from G_Q; point-pushing supplies the inner part of θₓ. | LM6 |
| B.5 | The sequence marked "??" on scan 399 fails in the middle already for (0,4) → (0,3); θₓ of scan 348 is onto and not injective. | correct | b = a representative fixing xy of a nontrivial element of G_{Q^ab}, extended by z ↦ z. Filling x gives the identity; filling z gives β ≠ 1, so b is not in the closure of the pure geometric group. Scans 348 and 399 read: the "??" sequence is the outer sequence of the pure groups 𝒯̂̂^!; the refutation applies under either reading of the doubtful target symbol on scan 348. | LM6 |
| B.6 | 1 → K → N(K) → GT̂ × S₃ → 1 for the point-pushing group K of the tripod. | known | Hoshi–Minamide–Mochizuki 2022: Out π̂₁(M₀,₅) = GT̂ × S₅ (read by the LM expert, F3, F27); Hoshi–Mochizuki 2011, Thm 6.1 (injectivity of restriction). The pullback reduction and the label count (the stabilizer of F and of the diagonal cusp is S₃) were checked. The last sentence ("the same proof works pro-ℓ") is asserted, not derived; nothing else uses it. | LM6 |
| C.1 | The index-2 subgroup V₂ is normal but not characteristic; V₄ = ker(G → G^ab/2) is characteristic, of type (0,6). | correct | Interchanging x and y moves V₂. Schreier ranks 3 and 5, ramification (2,1,2) and (2,2,2), genus 0. Scan 363 reads "(sans supposer π' caract.) on suppose π' d'indice 2", then the kernel of π → (π_ab)₂. | LM4 |
| C.2 | For V open normal with C_G(V) = 1: Aut(G;V) ≅ {a ∈ Aut V : [a] normalizes D}, Out(G;V) ≅ N(D)/D; likewise with loops. | correct | C_G(V) = 1 identifies G with the preimage of D in Aut V. Loops: downstairs inertia is the normalizer of its intersection with V. | LM4 |
| C.5 | Pro-2, index-2 cover: Out_lac(V₂^(2)) ≠ N(D)·Σ(V₂^(2)). | correct | Recomputed independently: ⟨t₁,t₂⟩ has order 128 in Aut(Q), δ has 64 conjugates, and for none of them does any unit of F₂⟨X,Y,Z⟩/(deg ≥ 5) intertwine it with αδα⁻¹, degree-4 terms of the unit included. The reduction to pure geometric classes (the centralizer of (xz) is realized by w ↦ −w, w ↦ 1/w) and to the finite quotient Q is sound. The witness is a genuine pro-2 automorphism (A.1; corrections lie in γ₅). | LM4 |
| C.9 | Open: covering surjectivity for the full profinite groups. | unproved (open) | Correctly isolated. | LM4 |
| C.10 | Pro-2, characteristic V₄ cover: Out_lac(W) ≠ N(D₄)·Σ(W). | correct (depends on C.3) | A transfer from C.5 through W ⊂ V₂ ⊂ G, C.2, and the pro-2 descent of geometric deck normalizers in C.3; the argument is valid. It is **not** proved by finite certificates. The descent rests on Boggi–Zalesskii 2025 applied to a dense embedding that is not a profinite completion (see C.3). | LM4 |
| D.2 | A procyclic L ≠ 1 whose normalizer has open image and acts by χ up to a finite character at one prime component lies in a cusp inertia group. | correct | Nakamura 1994, Lemma 2.1.4, and the weight argument (Frobenius weight 1 on V_ℓJ against q for χ). The prime the lemma produces is one where L has a nontrivial component. L ⊂ I by the centralizer statement of Boggi–Zalesskii 2019, Prop. 3.6. | LM6 |
| D.3 | Over a number field, the cuspidal loop structure is the only Galois-invariant loop structure in its Aut(Δ)-orbit, for every affine hyperbolic type. | correct | D.1 gives det = λ^{g+n−1} for the candidate classes and the Galois determinant is χ^{g+n−1}, so ψ^d = χ^d on the normalizer of a candidate subgroup; D.2 and maximality finish. This proves the first sentence of the conjecture of scan 483 ("Ce n'est pas la peine…") and supplies the step the expert found missing (F17). | LM6 |
| D.4 | Open: every maximal procyclic subgroup whose normalizer has open image is cuspidal, with no condition on the character. | unproved (open) | The dichotomy is correct: in a suitable cover the line of z lies in the boundary module (cyclotomic) or maps to V_ℓJ (weight one). Same status as F17. | LM6 |
| D.5 | In the class-two pro-5 quotient of y² = x³ − x over Q(i), a CM eigenline is maximal procyclic, not cuspidal, with normalizer of full image. | correct | Checked by hand: conjugation by y^{t/α} removes the central term c^t; the cusp is generated by [x,y], which has zero abelianization. | LM6 |
| D.8 | G_Q is its own commensurator in the label-preserving Out(F̂₂); in all of Out it is G_Q × S₃. | correct | Neukirch–Uchida reduces to the centralizer of an open ρ(G_L), which is Aut_L(P¹∖{0,1,∞}) = S₃ by Mochizuki's Isom theorem; S₃ meets the label-preserving group trivially. | LM6 |
| D.9 | The stabilizer in GT̂ (and GT̂₀) of the family of section images, taken with their arithmetic domains, is G_Q. | correct | The section of the rational point 2 forces aG_Qa⁻¹ to be open in G_Q; D.8. | LM6 |
| D.11 | The centralizer of ρ_U(G_K) in Out(Δ_U) is Aut_K(U); explicit groups for (0,4), (0,5), (1,1). | known | Mochizuki, Invent. Math. 138 (1999), Thm A (Isom form). The explicit groups were checked: V₄ for a generic rational quadruple, trivial for a generic quintuple, a conic with an odd-degree divisor has a point, μ₂/μ₄/μ₆ for (1,1). | LM4, LM6 |
| D.12 | For odd ℓ the pro-ℓ Galois centralizers on M₀,m are S₃ (m = 4) and S_m (m ≥ 5). | known | Nakamura 1994, Thms A and B, as the return cites them; theorem numbers not checked here. | LM6 |
| G.1 | On the [m]-pullback of a toric uniformization every torus character has an analytic m-th root. | correct | Local lifts adjusted by periods glue because the lattice is torsion-free. | LM6 |
| G.2 | Manuscript 019, Proposition 5.2 (an m-th root of T on the whole inverse image of the middle annulus). | correct | Stable model of y^ℓ = T(T−1)/(T−α): two rational components joined by ℓ nodes of thickness a, genus ℓ−1; slope-one characters (Baker–Rabinoff); |b_r| ≤ 1, |b_{−r}| ≤ |α|^r give v(h) > D on the collar; G.1 on Z ×_{J,[m]} J. The expert's reader also found no gap in 019 (F24). | LM6 |
| G.3 | Manuscript 031, Lemma 3.1: if m > n(n−1), the logarithms of u₁,…,u_m span Kⁿ. | correct | Zero estimate by translates of a component, interpolation determinant, product formula; n/r ≥ n/(n−1) > 1 + n/m. The statement matches 031 (its course, Theorem 2.1). It is a special case of the ℓ-adic rank theorem of Waldschmidt. | LM6 |
| G.4 | The finite-character separation used in 031, Proposition 4.3. | correct | V ≅ F₂[R₁]^{m₁} by valuations; (g−1)V ⊆ H_{i,R} by normality; the character of Ind_⟨c⟩ sign gives the kernel bound. | LM6 |
| G.5 | Manuscript 031, Proposition 4.3. | correct | Uses Uchida 1981 (local trichotomy) and Frobenius detection from G.3; the averaging over ⟨δ⟩ and the U-equivariant projection are sound. | LM6 |
| G.6 | Manuscript 031, Proposition 5.3: at most 2[K:Q] missed primes away from ℓ. | correct | Kummer classes unramified outside ℓ; S-units; equivariant Dirichlet; the orbit count matches 031. | LM6 |
| G.7 | Manuscript 031, Theorem 4.4: β is surjective and log χ_ℓ∘β = log χ_{k,ℓ} for ℓ ≡ 1 mod [k:Q]!. | correct | gcd(f, ℓ−1) = 1 forces f = 1; the difference of logarithms vanishes at infinitely many degree-one primes and is zero by G.3. | LM6 |
| H.6 | The quotients C_N (N of finite index in F₂) are cofinal among the finite congruence quotients of the exit category. | correct | A finite congruence restricts to a normal N in Aut(u) and factors through C_N. | LM5 |
| H.7 | lim_N H^q(NC_N; A) = A for q = 0, 2 and 0 otherwise, the class in degree 2 being the orientation class of P¹(C). | correct | Mayer–Vietoris for the homotopy pushout of BQ_N ← ⊔BI_{i,N} → ⊔*, goodness of F₂ and Z, the induced topology on each I_i. The statement is about the direct limit; single finite stages do not have this cohomology (the return says so). | LM5 |
| H.8 | The strict finite-category completion represents the profinite stratified homotopy type of (P¹, {0,1,∞}). | correct | Rank-one poset: the décollage consists of stratum and link spaces, completed objectwise by goodness, with no Segal condition. Rests on Barwick–Glasman–Haine, *Exodromy* (theorem numbers not checked here). | LM5 |
| H.9 | Open: the same comparison for n ≥ 5. | unproved (open) | The sufficient condition (chain-stabilizer goodness and fibre products) is stated correctly. | LM5 |

### The other statements

| Id | Claim | Verdict | Reason | Cited |
|---|---|---|---|---|
| A.1 | Every positive-degree special derivation over Z_ℓ is the leading term of a special automorphism of F_r^(ℓ), ℓ = 2, 3 included; relative and strong forms for filling x₁. | correct | (bᵢ) ↦ Σ[bᵢ,xᵢ] − [b₀,S] is onto integrally; corrections converge in the pro-ℓ group; I_m = Σ[I_{m−1},xᵢ] for the strong form. | no |
| A.2 | The S₃-character of the special outer derivations of the tripod through weight 12. | correct | [V⊗L_n(V)] − [L_{n+1}(V)] derived; weights 3 and 5 recomputed by hand; rerun identical. | no |
| A.5 | The normalizer of point-pushing in s₃ through degree 6; the quotient is grt₁ there. | correct | Rerun identical; the canonical map grt₁ → N/p is injective. | no |
| A.7 | Dimensions of boundary-preserving outer derivations of L(a,b). | correct | Formula and values checked by hand. | no |
| A.8 | The elliptic geometric Lie image through degree 12: 3, 5, 10, 24, 50 in degrees 4–12. | known | Hain–Matsumoto 2020 (the image is generated by the SL₂-orbits of the ε₂m). Dimensions rerun; through degree 12 the SL₂-decomposition is that of the free Lie algebra on the orbits (no relation in this range). | no |
| A.10 | Corrections to scans 322–326. | correct | Scans 322–324 read: the margin "complètement déconnant et ultra-faux" withdraws self-normalization; scan 323 guesses that 𝒯̂⁺ is invariant; (14)–(15) as described. | no |
| A.12 | Integral lifting with [a′,b′] = [a,b] exactly. | correct | Same scheme as A.1, with L_m = [L_{m−1},a] + [L_{m−1},b]. | no |
| A.15 | Elliptic normalizer quotient through degree 12: one class in degrees 6 and 10. | correct | Upper bounds rerun (trivial multiplicities; in degree 10 the rank rises from 109 to 111); lower bounds from Hain–Matsumoto 2020, §29. | no |
| B.1 | Filling s₃ → s₂ is a split surjection; dimensions through degree 6. | correct | Extension by D(x) = 0 is a Lie section; dimensions checked. | no |
| B.2 | Minimal ideal generators of the filling kernel: 2, 0, 3, 0, 13, 0. | correct | Rerun identical. | no |
| B.3 | The pro-ℓ filling kernel is larger than point-pushing; θₓ is not injective (degree-3 witness E). | correct | Witness rechecked with own code: E(x+y+z) = 0, fillings, ranks 2→3 and 3→4, [E,u] = 0. | no |
| B.7 | With FC-admissibility, filling on N(K) is exact onto its image J. | correct | Injectivity of Hoshi–Mochizuki 2011; surjectivity holds by definition of J. | no |
| B.8 | Open: removing the FC condition in general type. | unproved (open) | Correctly isolated. A lead not checked here: the group-theoreticity results for configuration groups of Hoshi–Minamide–Mochizuki 2022. | no |
| B.9 | The prediscretization map is onto, not injective; on N(K) it is bijective onto GT̂. | correct | From B.4, B.5, B.6; refutes "la bijectivité" of scan 348. | no |
| B.10 | ker fₓ = Q ⋊ K with Q = ker θₓ ≠ 1; graded dimensions 0, 0, 3, 3, 19, 27. | correct | θₓ restricted to K splits; filtrations are strict. | no |
| B.11 | Open: an all-degree presentation of the filling Lie kernel. | unproved (open) | — | no |
| C.3 | Coset injectivity for both test covers, profinite and pro-2. | known | Boggi–Zalesskii, BLMS 57 (2025), Thm A(iii) = Thm 4.3, and LM3 B.13. Not read here. For the pro-2 case the return applies the theorem to the dense embedding Γ₀,ₙ → R (R the pro-2 geometric closure, not a profinite completion) after writing out the cohomological comparison; its bibliography says this form was checked. C.10 depends on it. | no |
| C.4 | The degree-3 rational graded obstruction for both covers. | correct | Character arithmetic checked by hand (fixed dimensions 4 and 17); sum rank 5 rerun. | no |
| C.6 | The arithmetic-image quotients compare by the identity of G_K. | correct | — | no |
| C.7 | Open: descent to the §26 quotients needs normalizing all of Σ(V). | unproved (open) | This is exactly Grothendieck's own doubt at scan 362 (read). | no |
| C.8 | Readings at scans 361–363: the upstairs ambient group; 2g + ν − 1. | correct | Scan 363 read: the plus sign gives (Z/2)² at (0,3). | no |
| D.1 | det(u | F^ab) = λ^{g+n−1} for a peripheral automorphism, ℓ = 2, 3 included. | correct | Pfaffian identity on the class-two quotient modulo W∧H. | no |
| D.6 | Pop's localized tripod functor has automorphism group G_Q. | known | Pop, *Finite tripod variants of I/OM*, Invent. Math. 216, Thm 2.7(1), as the return cites it; not read here. The rigidity check (only h = z among the six Möbius maps) rerun. | no |
| D.7 | The maximal closed AA subgroups of GT̂ are the GT̂-conjugates of G_Q. | known | Hoshi–Mochizuki–Tsujimura 2025, Thm 5.17(ii), as cited; not read here. | no |
| D.10 | The stabilizer of D.9 satisfies the Nakamura–Schneps relations (III′), (IV). | known | Nakamura–Schneps 2000, as cited; the formula ρ₂(σ) = −A_σ(−1,1) not checked here. | no |
| D.13 | Curves over K with dominant maps embed fully faithfully into open G_K-homomorphisms modulo inner automorphisms. | known | Mochizuki 1999, Thm A; constant maps through Thm C. Matches scan 484. | no |
| D.14 | The essential image: open subgroups of the arithmetic tripod, then filling Galois-stable cusps. | correct | Belyi's construction stays over K; matches scan 484. | no |
| E.1 | A^I/S₂ ≅ GT̂ for P̂Γ₁,₃. | correct | Rests on Boggi 2026 (arXiv:2011.15075v6), Thms 3.12 and A(ii), which the expert read in substance (F27). | no |
| E.2 | The automorphism 2-group of BP̂Γ₁,₂ → BP̂Γ₁,₁ has π₀ = GT̂, π₁ = 1. | correct | π₀ = Out(G₂; ker q), π₁ = Z(G₂) = 1; Out(Γ̂₁,₂) ≅ GT̂ is Minamide–Nakamura (F27); ker q is characteristic. | no |
| E.3 | The decorated elliptic boundary pair has trivial π₁. | correct | Transporter argument of LM3 F.12, F.15. | no |
| E.4 | Open: elliptic clutching coherence and the orbifold normalizer comparisons. | unproved (open) | — | no |
| E.5 | Orbifold quotients and the parity-kernel restriction maps ρ_r. | correct | Euler characteristics; K₃ ≅ π̂₁,₁, K₄ ≅ π̂₁,₂; loop preservation; descent modulo the deck involution. | no |
| E.6 | What the quilt theorems of Nakamura–Schneps and Hatcher–Lochak–Schneps give. | known | NS 2000, HLS 2000, as cited; not read here. | no |
| E.7 | The automorphism group of the procongruence outer tower is GT̂. | known | Boggi 2026, Thm 6.23, Cor. 6.24 (F27). | no |
| E.8 | The modular-stack exact sequence; at (0,3) the stack is BS₃. | known | The standard sequence for π₁ of M_{g,[n]} over Q; Boggi 2026, §7.1. | no |
| E.9 | Open: automatic nonseparating inertia in genus one. | unproved (open) | — | no |
| F.1 | V_n (antisymmetry, 3-cycle, cabling) ≅ S₃-invariant special outer derivations. | correct | Both directions checked; the weight-4 polynomial satisfies the first two equations and fails cabling (own code). | no |
| F.2 | The pentagon through weight 12; dim grt₁ = 1,0,1,0,1,1,1,1,2,2 in weights 3–12. | correct | Rerun identical (C++ recompiled); matches Brown's lower bound. | no |
| F.3 | For ℓ ≥ 5, GT¹_ℓ ⊊ GT¹_{0,ℓ} (pro-ℓ, multiplier one). | correct | A weight-7 invariant class outside the pentagon line lifts to the centralizer of S₃ (A.1, A.11); its pentagon defect has nonzero leading term. | no |
| F.4 | Open: GT̂ ≠ GT̂₀; the primes 2 and 3. | unproved (open) | Consistent with F3 of the expert. | no |
| F.5 | Abelian finite images of GT̂ are the scalars, all realized by G_Q; 792 types of order ≤ 500. | correct | The count 792 = Σ_{a≤22} ⌊500/a²⌋ checked by hand. | no |
| F.6 | Open: finite exhaustion beyond class two. | unproved (open) | — | no |
| F.7 | Z_ℓ/J_{ℓ,w} for all ℓ, w. | correct | Teichmüller units, lifting the exponent, u = −1 and u = 3 at 2. | no |
| F.8 | An invariant character of a kernel need not extend (Q₈). | correct | — | no |
| F.9 | GRT^ab ≅ G_m; the abelianization of grt₁ is ⊕ kσ_{2j+1}. | known | GRT^ab ≅ G_m needs only positive weights; the grt₁ part is Hain–Matsumoto 2003 with Brown 2012 and G.10. | no |
| F.10 | Aut(PaB^un_k) = GT(k). | known | Drinfeld 1990; Bar-Natan 1998. | no |
| F.11 | G_Q → GT̂/V is onto for the cyclotomic-scalar family of quotients. | correct | — | no |
| F.12 | Open: the full profinite abelianization of GT̂. | unproved (open) | — | no |
| F.13 | For characteristic quotients of class ≤ 2, G_Q and GT̂ have the same image; the Q₈ dessin Y² = X⁵ − X, t = (X²+1)²/(4X²). | correct | f is central in the quotient; deck relations a² = b² = h, ab = hba, ramification (4,4) and Riemann–Hurwitz checked by hand. | no |
| G.8 | Manuscript 008, Proposition 3.2 (the filtered transfer). | correct with a gap | See below. | no |
| G.9 | Manuscript 008, §4 (deletion and residual-kernel induction). | correct with a gap | See below. | no |
| G.10 | grt₁ over Q is free on one generator in each odd weight ≥ 3 (upper bound via Willwacher). | known | Willwacher 2026 (unrefereed) for the upper bound, Brown 2012 for the lower bound. The rederivation is complete and correct: every operator identity was checked by hand, the representation check rerun, and the mechanism run end to end on the actual solutions of weights 3, 5 and 8 (own code: identity (G.3) and f = f(d, L_C)(1) hold, while two of the three weight-7 candidates outside the solution line fail (G.3)). Two other 2026 proofs are on record (008; Hirose, F27). | no |
| G.11 | The G.10 argument uses neither G.8 nor G.9. | correct | Checked against the text of G.10. | no |
| H.1 | C_E(P) ≅ C₃,₀. | correct | Centre-free P. | no |
| H.2 | Z(Γ̂₃,₀) ⊂ C₃,₀; torsion-freeness under a stated condition. | correct | — | no |
| H.3 | Homology representations of finite covers are congruence representations. | correct | — | no |
| H.4 | |π₃/L| = 64·3²⁵⁸; a separating twist acts nontrivially. | correct | Rerun; T ≠ 1 of order 3 cannot come from an inner automorphism, which acts through a deck group of order 2. | no |
| H.5 | Open: the genus-three congruence kernel. | unproved (open) | Open in the literature (F4). | no |

## Wrong items

None.

## Gap items in full

**G.8 (manuscript 008, Proposition 3.2).** The statement (a congruence among four evaluations of the lowest-count
component χ in the type-B₃ arrangement algebra reduced mod 2, modulo words of length m + r with fewer than r letters
u) is plausible and the strategy is sound. Missing: (1) the full list of source corrections; the proof shows two
identities ([aᵢ,H], [aᵢ,Vᵢ]) and says the others "are obtained from the same two derivations and likewise add two U
letters"; (2) the target side, where agreement of the count-preserving tables is asserted from the flats
(zᵢ = z_d = 0 for the a-row, signed three-hyperplane flats for the u,v-rows) without the computation; (3) the
independence of ordered source words, asserted through a prefix-code remark. The review did not reconstruct these and
did not compare the statement with 008 itself. Nothing else in the return or in LM4–LM6 depends on G.8: G.10 proves
the upper bound without it.

**G.9 (manuscript 008, §4).** Injectivity of χ ↦ χ(0,C,B) on gr^r_F of the saturated lattice. Missing: the deletion
representation is justified only in outline (flatness of the logarithmic one-form "by the triangle identities",
residues at a hyperplane and a codimension-two flat); the edge table is stated, not derived; the final induction
(every coefficient equal to one value λ, then 3λ = λ for m ≥ 2, and the cases m = 1, r ≤ 2) is compressed to a few
lines. Same remark as for G.8: G.10 does not use it.

**Dependencies to keep in view (not gaps in the proofs).**
- C.10 depends on the pro-2 descent of C.3, which applies Boggi–Zalesskii 2025 to the pro-2 geometric closure of
  Γ₀,ₙ. The return writes out the cohomological hypotheses it needs; the source was not read in this review.
- F.9 (the grt₁ part) and the all-weight remarks of F depend on G.10, that is, on 2026 manuscripts (unrefereed),
  whose argument the review checked.
- B.6: the closing sentence about pro-ℓ versions is asserted without proof; no statement uses it.

## What LM4–LM6 must change in their "After the returns … (added 12 November 2026)" blocks

No cited statement is false, so none has to be removed (RECORD.md, open point (c)). The changes are a status line, two
corrections, and precisions.

### All three blocks

1. Replace "None has been reviewed line by line yet" (LM4) and "Neither has been reviewed line by line yet" (LM5,
   LM6) by a sentence of this form: "LM3b has since been reviewed statement by statement (Claude Opus 5.5, effort
   max, 12 November 2026; attached as `LM3b_review/REVIEW.md`): none of the statements cited here was found false;
   C.10 depends on the pro-2 descent of C.3. LM2 and LM3 are not yet reviewed." (In LM5 and LM6 leave out LM2.) Keep
   "Each cited statement is a claim: check its proof …", since the review is not authority.
2. Attach this review: add `LM3b_review/REVIEW.md` (this file) to each `ZIP_LIST.tsv` and to the sentence of WHAT IS
   ATTACHED that names `LM3b_return/`.

### LM4 (`pro_prompts_draft_20261111_work\LM4_FINITE_GROUP_ACTIONS\PROMPT.md`, line 56 and line 59)

3. **Correction (line 56).** "C.5, C.10 (Refuted there, pro-2): `Out_lac(V) ≠ N(D)·Σ(V)` for both coverings, by 64
   finite certificates" misdescribes C.10. Replace by: "C.5 (Refuted there, pro-2): for the index-2 cover,
   `Out_lac(V₂^(2)) ≠ N(D)·Σ(V₂^(2))`, by an explicit special automorphism (the A.1 lift of the degree-3 derivation
   with conjugators `[[x,y],y]`, `[x,[x,y]]`, `1`) and 64 dual certificates in `F₂⟨X,Y,Z⟩/(deg ≥ 5)`, recomputed
   independently in the review. C.10 (Refuted there, pro-2): the same for the characteristic cover `V₄`, by transfer
   from C.5 through C.2 and the pro-2 descent of geometric deck normalizers in C.3, not by certificates; C.3 applies
   Boggi–Zalesskii, BLMS 57 (2025), Thm A(iii), to a dense embedding that is not a profinite completion: check that
   application before building on C.10."
4. **Addition (line 59, the bullet on his drilling theorem).** The profinite analogue of the theorem of scans 186–189
   is false for loop-preserving groups: "LM3b B.4, B.5, B.10 (reviewed: correct): for `(0,4) → (0,3)` the map from
   the cusp stabilizer in `Out_lac(π̂')` to `Aut_lac(π̂)` is onto with kernel `Q ≠ 1`, and the outer filling kernel is
   `Q ⋊ π̂`; B.6 restores exactness on the normalizer of the point-pushing subgroup, with image `GT̂ × S₃`. Part A (d)
   and Part C must keep the discrete theorem apart from its profinite analogue."
5. **Optional addition (line 57, the bullet on GT₀ and torsion).** LM3b F.3 (pro-ℓ, ℓ ≥ 5: `GT¹_ℓ ⊊ GT¹_{0,ℓ}`,
   reviewed correct) and F.4 (open: `GT̂ ≠ GT̂₀`, and ℓ = 2, 3) bear on "his condition on the two lifts" in
   Part E (b).

### LM5 (`…\LM5_MULTI_GALOIS_TOPOI\PROMPT.md`, line 67)

6. **Correction.** "the cohomology of their nerves with finite constant coefficients `A` is `A` in degrees 0 and 2 and
   zero elsewhere" misstates H.7: replace by "the direct limit over the system of the cohomology of their nerves with
   finite constant coefficients `A` is `A` in degrees 0 and 2 and zero elsewhere (no single finite stage has this
   cohomology)".
7. **Precision.** The margin that says the comparison fails "à cause du genre 0" is on scan 129 (beside the Corollary
   of the Proposition), not on scan 124, which states question b). H.7 is the constant-coefficient case; H.8 is the
   stratified statement from which the comparison for coefficients constructible along `S` follows. Suggested: "H.7
   (constant coefficients) and H.8 answer his question b) of scan 124 for `P¹` with three points; his margin on
   scan 129 says the comparison fails for locally constant coefficients on `X` itself in genus 0."
8. **Status (line 69).** "Part E (c) may take the case n = 4 as proved in LM3b H.8, after checking it" may add:
   "(reviewed: correct; it rests on Barwick–Glasman–Haine, *Exodromy*, whose theorem numbers were not checked)".

### LM6 (`…\LM6_POINTS_AS_SECTIONS\PROMPT.md`, lines 25, 26 and 28)

9. **Precision of the ask (line 25).** A lift of D.5's eigenline through every class of the lower central series of
   the pro-5 group would refute only the pro-5 analogue of D.4; D.4 concerns the full profinite `Δ` with the
   normalizer taken in the arithmetic profinite group. Rewrite the last sentence as: "… lift the eigenline of D.5 step
   by step through the lower central series of the pro-5 group, by program as far as it goes; if it lifts through
   every class, this refutes the pro-5 analogue of D.4, and it remains to decide whether the subgroup comes from `Δ`;
   otherwise find the class at which it stops and prove that it stops."
10. **Precision (line 28).** The sentence on B.4, B.5 joins two scans. Suggested: "the sequence marked '??' on scan 399
    (outer, pure groups) is not exact in the middle for the full groups, already for `(0,4) → (0,3)`: the outer
    filling map is onto (B.4) and its kernel is `Q ⋊ π̂` with `Q = ker θₓ ≠ 1` (B.5, B.10), where `θₓ` is the genuine
    map of scan 348 from the stabilizer of a hole in `Autext_lac` to `Aut_lac` of the plugged group, onto and not
    injective."
11. **Precision (line 26).** After "LM3b G.3–G.7 (Proved there)" add: "reviewed: correct; G.3 is a special case of
    the ℓ-adic rank theorem of Waldschmidt; these check the named steps of 031, not its main theorem (the return
    says so)". The same holds for G.1, G.2 and 019 (line 27).

## Files in this folder

- `REVIEW.md`: this review.
- `return\LM3b_TEICHMULLER_PUSH\`: the return, extracted by `checks\extract.py` (path-traversal check; 143 entries).
- `rerun\code\`: copy of the return's `code\` after the rerun (regenerated outputs);
  `rerun\regenerated_ceh_pro2_certificates.json`; `rerun\logs\`: stdout and stderr of every program, compile logs,
  timings in `long_status.txt`. The compiled executables were removed after the run.
- `checks\`: the review's own programs and their outputs (`indep_c5`, `indep_lie`, `indep_g10`), the runner and the
  comparison script.

Rerun timings on this machine: `ab_lie.py 6` 15 s, `ab_elliptic_normalizer.py` 49 s, `fg_prepare.py 12` 17 s,
`fg_pentagon` 27 s, `fh_finite.py` 17 s, every other program 3 s or less.

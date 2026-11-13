# LM7: the three items (E.32, E.25, the push prompt's items for E.23, D.13, D.19)

Claude Fable 5.2, effort max, 13 Nov 2026. Inputs: the return's `sections\E_completed_pairs.tex`, `E_cubic.tex`, `E_cuspidally_central.tex`, `E_intrinsic_positive.tex`, `D.tex`, `D_cm_shadow.tex`, `D_cm_refine.tex`; `NOTES_FOR_PUSH_PROMPT_20261113.md`; `SHAPE_MAP_REVISION_20261113.md` (revision 1; 1b, H2, H6 first row). CYCLOTOMIC C9 was not read: the "germs" item is taken from the notes.

Notation: `T_n = Z/3ⁿ(2)`, `T = Z₃(2)`, `S = {3, ∞}`, `P*` the primes `q ≠ 3`, `e_q = v₃(q−1)`, `A_n = ⊕_{q∈P*} Z/3ⁿ`, `R = lim_n A_n` (families of 3-adic integers tending to zero), `d(z)_q = (q−1)z_q`, `C_n = [A_n → A_n]` with differential `d` in degrees 0, 1, `K_n = H⁰(C_n) = ⊕_q (Z/3ⁿ)[q−1]`.

## Part 1. E.32: the obstruction is a lim¹ class

**Statement.** Under the isomorphism `H²_cts(G_Q, T) ≅ R/dR` of (E.32d), Jannsen's sequence

`0 → lim¹_n H¹(G_Q, T_n) → H²_cts(G_Q, T) → lim_n H²(G_Q, T_n) → 0`

is the sequence

`0 → {z ∈ R : z_q ∈ (q−1)Z₃ for all q}/dR → R/dR → lim_n ⊕_q Z/(3ⁿ, q−1) → 0`.

(a) The residue map induces `lim¹_n H¹(G_Q, T_n) ≅ lim¹_n K_n`, and `lim¹_n K_n` is the left-hand term, which is (E.32e).
(b) For a set `Σ ⊂ P*` the tower `n ↦ ⊕_{q∈Σ} (Z/3ⁿ)[q−1]` is Mittag-Leffler if and only if `sup_{q∈Σ} v₃(q−1) < ∞`. For `Σ = P*` the supremum is infinite (Dirichlet), so the tower is not Mittag-Leffler.
(c) The obstruction `9α∪β` of the pair (E.32f) is a non-zero element of `lim¹_n H¹(G_Q, T_n)`: its image in every `H²(G_Q, T_n)` and in every local group is zero, and it is not zero.

**Proof.** *Step 1 (levelwise, from the proof of E.32, checked).* `H²(G_S, T_n) = H³(G_S, T_n) = 0` and `H¹(G_S, T_n)` is finite (E.32g: `T₁ = F₃` with trivial action, `|H⁰| = |H¹| = 3`, Euler characteristic 1, dévissage). The localization triangle (E.32h), in the limit over finite sets of primes, gives for each `n`, compatibly in `n`:

`0 → H¹(G_S, T_n) → H¹(G_Q, T_n) → K_n → 0`, `H²(G_Q, T_n) ≅ H¹(C_n) = ⊕_q Z/(3ⁿ, q−1)`.

*Step 2 (the two Milnor sequences).* Jannsen (1.6) is the Milnor sequence of `Rlim_n RΓ(G_Q, T_n)`, and (2.2) identifies its cohomology with continuous cochain cohomology (the `T_n` are finite). The map of triangles gives a map of Milnor sequences

`0 → lim¹ H¹(G_Q, T_n) → H²_cts(G_Q, T) → lim H²(G_Q, T_n) → 0`
`0 → lim¹ K_n → H¹(Rlim C_n) → lim H¹(C_n) → 0`.

The middle arrow is an isomorphism (E.32i: `H²` and `H³` of `Rlim RΓ(G_S, T_n)` vanish, because `lim¹` of the finite groups `H¹(G_S, T_n)` and of `H² = 0` vanish). The right arrow is an isomorphism by Step 1. So the left arrow is one (five lemma). Directly: `lim¹` is right exact on towers and `lim¹ H¹(G_S, T_n) = 0`.

*Step 3 (the terms).* The transition maps of `A_n` are onto, so `Rlim C_n = [R → R]` and `H¹(Rlim C_n) = R/dR`, with the image of `d` and no closure. Put `I_n = dA_n = ⊕_q (q−1)Z/3ⁿ`. From `0 → K_n → A_n → I_n → 0`, with `lim K_n = ker(d | R) = 0` and `lim¹ A_n = 0`: `lim¹ K_n = (lim I_n)/dR`. From `0 → I_n → A_n → H¹(C_n) → 0`, with `lim¹ I_n = 0` (onto transitions): `R → lim H¹(C_n)` is onto with kernel `lim I_n = {z ∈ R : z_q ≡ 0 mod (3ⁿ, q−1) for all n} = {z ∈ R : z_q ∈ (q−1)Z₃}`. This proves the displayed sequence and (a).

*Step 4 (Mittag-Leffler).* For `m ≥ n` the image of `K_m → K_n` at the coordinate `q` is the reduction of `3^{m−min(m,e_q)}Z/3^m`: all of `Z/3ⁿ` if `e_q ≥ m`, and `3^{m−e_q}Z/3ⁿ` if `e_q < m`, which is zero exactly when `m ≥ e_q + n`. The images are constant from `m₀` on if and only if `e_q ≤ m₀ − n` for every `q ∈ Σ`. So the tower is Mittag-Leffler iff `e_q` is bounded on `Σ`; if `e_q ≤ E` then `K_{n+E} → K_n` is zero and `lim¹ = 0`; equivalently `z_q/(q−1)` tends to zero whenever `z_q` does. For `Σ = P*` and every `m` there are primes `q ≡ 1 mod 3^m` (own count below 200000: 8988, 2996, 1004, 341, 106, 39, 10, 5, 2 primes with `e_q ≥ 1, …, 9`). This proves (b). The complexes `C_n` themselves have onto transitions; it is the system of their `H⁰` that fails.

*Step 5 (the class).* For (E.32f): `a = κ₃`, `b = Σ_j b_{q_j}κ_{q_j}`, `b_{q_j} = (q_j−1)/(9r_j)`. At `q = q_j`: `a_q = 0`, `A_q = r_j`, so `9(A_q b_q − B_q a_q) = q_j − 1`; at the other `q`: 0. The representative `z = (q_j − 1)_j` lies in `lim I_n` and its only preimage under `d` is the family equal to 1 at every `q_j`, which does not tend to zero. So the class is non-zero in `lim¹`, zero in `lim H²`. The local groups are `H²_cts(Q_q, T) = Z₃/(q−1)` (`q ≠ 3`), 0 at 3 and at `∞`; `z_q ≡ 0`. Recomputed: `q_j` = 109, 163, 487, 1459, 39367, 131221 for `j` = 3, …, 8, `r_j` a unit, `c_{q_j} = −1` each time (`checks_author\check_finite.out`). ∎

**Two remarks.** (1) The same computation for `Z₃(1)`: the residue differential is 0, `K_n = A_n` has onto transitions, `lim¹ = 0`, and `H²_cts(G_Q, Z₃(1))` injects into the product of the local groups. Phantom classes begin at weight −3. (2) `lim¹ K_n ≅ {y ∈ ∏_q Z₃ : (q−1)y_q → 0}/{y → 0}`: a class is a family of corrections that is integral and does not tend to zero.

## Part 2. E.25: `κ₂(−1) ∪ κ₂(−1) = (−1,−1)`

**Verified, with one correction.**
- The extension (E25.4) is the pull-back of `1 → ⟨c⟩ → D₈ → (Z/2)² → 1` along `(ε, ε)`, `ε = κ₂(−1)` the character of `Q(i)/Q`. The class of `D₈` (with `x² = y² = 1`, `(xy)² = c`) is the product of the two coordinate characters, so the pulled-back class is `ε ∪ ε ∈ H²(G_Q, Z/2) = Br(Q)[2]`, the class of the quaternion algebra `(−1,−1)`.
- Local invariants: non-zero at `∞` (`x²+y²+z²` is definite; in group terms both lifts of complex conjugation square to `c`), **non-zero at 2** (`x²+y²+z² ≡ 0 mod 8` has no primitive solution), zero at every odd prime (a non-singular zero mod `p` lifts). So the class is non-zero **exactly at 2 and ∞**. "Non-zero exactly at the real place" is false: by reciprocity no class of `Br(Q)` is non-zero at one place only.
- What it is: the Brauer class of the conic `X₂⁺: x²+y²+z² = 0`. For even `n` the map `U_n⁺ → X₂⁺`, `[x:y:z] ↦ [x^{n/2}:y^{n/2}:z^{n/2}]`, pulls it back; `X₂⁺` has no point over `R` and none over `Q₂`. E.25's proof uses the real place only, which suffices.

## Part 3. Items for the push prompt

### 3.0 Which failure is which (proved here)

**Lemma (finite sets).** Let `(X_i)_{i∈I}` be an inverse system of finite sets over a directed set and `J ⊂ I` a directed subset. For `x ∈ lim_J X_j` and `i ∈ I` let `Y_i(x) ⊂ X_i` be the elements whose image in `X_j` is `x_j` for every `j ∈ J` below `i`. Then `x` is in the image of `lim_I → lim_J` if and only if every `Y_i(x)` is non-empty. *Proof.* The `Y_i(x)` form an inverse system of finite sets with limit the fibre over `x`; a limit of non-empty finite sets is non-empty. ∎ So in a system of finite sets "every finite stage passes" always gives a limit element: there is no lim¹. A computation can be inconclusive there only because the stages examined are not cofinal.

- **D.13: cofinality.** `GT̂₀` is the limit of the finite sets `GT(K)` over all finite-index `K ⊲ B₃` inside `PB₃` (D.22); `Out^♯(F̂₂)` is the limit of finite sets of loop-preserving outer automorphisms of the characteristic finite quotients. D.12 realizes each leading term over the subsystem `J` of ℓ-power quotients. That subsystem is not cofinal: a non-nilpotent finite quotient contains no `Γ_m`. By the lemma a pro-ℓ special automorphism comes from the profinite group iff its fibre is non-empty at every finite quotient.
- **D.19: cofinality**, in both parts. Part (i) is D.13. Part (ii): D.26 proves the twelve nonarithmetical shadows survive the tower `Ñ_j` and exhibits `J ⊂ [N,N]N⁶` with `[N,N] ⊄ J`, so that tower is not cofinal. Since the sets `GT(K)` are finite, the decreasing images `R_{K,Ñ₆}(GT(K))` are constant from some finite `K₀` on: one finite quotient decides, and no bound for it is known.
- **E.23: lim¹**, after the tame tests. The quotient `N/γ₃N` has finite rank, so the coefficient tower `3ⁿ` is cofinal by construction. The obstruction to lifting a class of E.36 lies in `H²_cts(G_Q, 𝒦)`, `𝒦 = ker(Λ²V → Λ²T)` of rank 44, an extension of `Λ²W` (rank 28, weight −4) by `T ⊗ W` (rank 16, weight −3), `W = Z₃(1)[D]/Z₃(1)δ`. The groups `H¹(G_Q, 𝒦/3ⁿ)` are infinite. On the residue module `𝒦(−1)` the operator `Frob_q − 1` is injective (weights −1, −2), and `v₃ det(Frob_q − 1)` is unbounded over `q` (primes split in `Q(E[3^m], μ_{3^m})`). As in Part 1 the tower `⊕_q H⁰(F_q, 𝒦(−1)/3ⁿ)` is not Mittag-Leffler and `lim¹_n H¹(G_Q, 𝒦/3ⁿ) ≠ 0` (it maps onto `lim¹` of that tower up to the finite groups `H²(G_S, 𝒦/3ⁿ)`). The metabelian and depth-two quotients of E.23 have infinite rank; for them cofinality of the finite-rank quotients used must be proved as well.

### 3.1 Item E.23-a: the rank-44 lift, complete

Setting: E.36, (E36.1)–(E36.2). For `α ∈ H¹(Q, V)` and `a ∈ ℛ_P(Z₃)` let `s(α, a)` be the section class of `N^cc ⋊ G_Q` of E.36.

Prove:
1. The continuous cohomology `H²_cts(G_Q, 𝒦)` as the first cohomology of an explicit residue complex `[ℛ(𝒦(−1)) → ℛ(𝒦(−1))]`, differential `Frob_q − 1`, together with the contribution of `RΓ(Z[1/3], 𝒦)`, which is to be computed (it is zero for `Z₃(2)` by (E.32g); here the action is through `G_{Q(ζ₃),{3}}`). Then Jannsen's sequence for `𝒦` with its lim¹ term as in Part 1.
2. The obstruction `ob(α, a) ∈ H²_cts(G_Q, 𝒦)` as an explicit family of residues at the primes `q ≠ 3`, in the coordinates of E.24 (the five torus coordinates `(a, b, A, B, C)` and the class of `z′`), with the origin terms of (E31.7) kept.
3. The exact set of `(α, a)` with `ob(α, a) = 0`: the tame condition at each `q`, then the convergence condition (the lim¹ check). Each fibre of the lifts as a torsor under an explicitly computed group.
4. A class in the lim¹ term: an `(α, a)` whose local and finite-coefficient obstructions all vanish and which has no continuous lift; or a proof that for `𝒦` no such class is of the form `ob(α, a)`.

Done when: 1–4 are proved, the set in 3 is given by formulas a program evaluates, and the program reproduces E.28, E.31 (the coset `α + 3𝒦`), E.34 (every class unramified outside 3 lifts) and E.35 as special cases. Not accepted: the obstruction given only as a product of local classes; a criterion without the convergence condition; "open, see E.23".

### 3.2 Item E.23-b: the rank-44 test (E.36, E.31), corrected

As received: "no section class of E.32 outside the point and cusp classes survives the rank-44 lift". The review finds this contradicted by E.34 (REVIEW_author.md, finding 4); that argument is the reviewer's and unchecked.

Prove or refute, each completely:
1. (Refutation of the statement as received.) Compute the three cuspidal packets of `U₃⁺/Q` (at `O`, `P`, `Q`) as subsets of `H¹(Q, V)` in the coordinates of E.24, and of the classes of E.32. Decide whether `κ(3)(e_O + e_P)` lies in a packet. With E.34, conclude.
2. (The statement for ramified classes.) For a class `s(α, a)` that lifts to `(N/γ₃N) ⋊ G_Q` and a prime `q ≠ 3` at which `α` is ramified, determine the possible tame-inertia vectors `t_q ∈ W`. Test statement T1: `t_q` is a multiple of the inertia vector of one cusp fixed by `Frob_q`. Test statement T2: a class that lifts and is ramified at infinitely many primes is cuspidal.
3. The same two statements one layer up, for `N/γ₄N`, with the classes of E.34 included: which of them are cuspidal, and which non-cuspidal ones survive every nilpotent layer (they all do, by E.34: state what distinguishes the cuspidal ones group-theoretically, by the centralizer or the weight of their inertia).

Done when: 1 is decided with the packets written out; T1 and T2 are each proved or refuted by an explicit class; 3 is answered with proofs. Not accepted: a test on finitely many primes without the lim¹ check of 3.1.

### 3.3 Item E.23-c: germs

Pose E.23 for every open subgroup: for a number field `L` let `Sec(L)` be the set of section classes of `(N/γ₃N) ⋊ G_L`. Prove: the description of `Sec(L)` by 3.1 with `Q` replaced by `L` (residue complex over the primes of `L`, the lim¹ term, the tame conditions); the restriction maps `Sec(L) → Sec(L′)`; the action of `Gal(L/Q)` on `Sec(L)` for `L/Q` Galois and the comparison of `Sec(Q)` with the invariants; the direct limit over `L` (germs) and the image of `Sec(Q)` in it. Decide whether the lim¹ class of E.32 dies in the limit over `L` (its witness uses primes of `Q` with `v₃(q−1) → ∞`; over `L ⊃ μ_{3^m}` the valuations shift by `m`, they stay unbounded).

Done when: each of these is a theorem with proof, and the last question is decided.

### 3.4 Item D.13: the full profinite images

Decide, each by proof:
1. `dim` of the image of `Out^♯(F̂₂)` in weight 5 of the pro-ℓ metabelian special derivations: 3, 2 or 1.
2. `dim` of the image of `GT̂₀` in weight 9 of the `S₃`-invariant part: 2 or 1; equivalently whether an element of `GT̂₀` has leading term outside the line of `((X+Y)⁹ − X⁹ − Y⁹)/(XY)`.
3. The same for `GT̂` is settled (D.21, dimension 1); state what the pentagon removes at the level of finite shadows.

The failure to transfer D.12 is one of cofinality (3.0), so the work is one of: (a) a proof that the fibre of 3.0 is non-empty at every finite quotient (a lifting theorem for special automorphisms from the pro-ℓ to the profinite free group, where D.24 shows that Gaschütz lifting loses the peripheral condition); (b) one finite quotient `K` of `B₃` and an ℓ at which every element of `GT(K)` has zero component along the extra direction, which bounds the image by D.22.

Done when: 1 and 2 each carry a number with a proof. Not accepted: the pro-ℓ value restated; a computation over ℓ-power quotients only.

### 3.5 Item D.19: the CM coset

Decide whether `GT̂₀` contains an element with CM coordinates in the coset missed by Galois (D.16), that is whether one of the twelve shadows of D.25 lies in `⋂_K R_{K,Ñ₆}(GT(K))`.

By 3.0 this is decided at one finite quotient. Work: compute `R_{K,Ñ₆}(GT(K))` for quotients `K` outside the homology tower, starting with the `J` of D.26 (kernel not containing `[N,N]`) and continuing through the quotients of `B` whose pure part surjects onto `H ≅ C₂² × SL₂(F₃)` (D.26, last paragraph), until either a `K` removes all twelve shadows (then the image of `GT̂₀` is the Galois image, and LM2 C.d5 is settled for `GT̂₀`), or a proof that the fibre is non-empty at every `K` (then `GT̂₀` fills the coset). State also what the answer gives for `GT̂` (pentagon added).

Done when: the coset is proved to be in the image or proved not to be. Not accepted: survival along a non-cofinal tower presented as an answer.

### 3.6 Standing instruction for these items

Every test of the tame relation `φτφ⁻¹ = τ^q` made prime by prime (E.28, E.31) is followed by the lim¹ check of Part 1 for the coefficient module in play; the check is stated with its residue complex and its convergence condition.

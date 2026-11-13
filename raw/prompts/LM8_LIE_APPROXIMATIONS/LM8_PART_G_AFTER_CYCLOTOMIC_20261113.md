# LM8_LIE_APPROXIMATIONS: a Part G from CYCLOTOMIC_KERNEL E3, ready to paste

Written by Claude Fable 5.2 (effort max), reader R-149, 13 November 2026 (date from the session; the clock was not read: the context guard stopped all commands). For the main session, which pastes and lints. The prompt itself was not edited.

**State of this text.** Not linted (the guard stopped commands before the lint). I wrote it without the phrases the lint bans. The leads in it are mine and unchecked, except the two marked "re-derived", which I worked through by hand today.

## Where it goes

In `longue_marche_pro_pilot_20261104\pro_prompts_draft_20261111\LM8_LIE_APPROXIMATIONS\PROMPT.md` (133 lines when read):
- **Block 1** (the inputs): a new section before line 58 (`## What the outcome must be`), after the block "After LM1" that ends on line 56.
- **Block 2** (Part G): after line 99 (`*Part F, after LM2.*`), before the `---` of line 101.
- Point 1 of the outcome section asks for a row per lettered task: (a)–(e) of Part G fall under it with no further change.

## Block 1

```
## After CYCLOTOMIC_KERNEL (added 13 November 2026)

The prompt CYCLOTOMIC_KERNEL (on Grothendieck's anabelian notes of 1983, cote 149 of the Montpellier archive) was answered by GPT-6 Astra (ChatGPT Pro mode) on 12 November 2026 (56 statements) and reviewed statement by statement by Claude Opus 5.5 (effort max) the same day (`CYCLOTOMIC_review/REVIEW.md`: no statement wrong; 9 known in the literature; 4 open as stated). Statements are cited as CK E.n (`CYCLOTOMIC_return/`). The review is not authority. Part G stands on these; check the step you use of each.

- **Setting.** `K = Q(i)`, `E : y² = x³ − x`, `U = E ∖ {O}`, `P` the maximal pro-5 quotient of `π_1(U_K̄)`, free on `x, y` taken in the two eigenlines of the complex multiplication on `V = P^ab = T_5 E` (5 splits in `Z[i]`), `c = [x, y]` a generator of the image of the inertia group at `O`, `N_r = P/γ_{r+1}P`, `Δ = Gal(K̄/K^ab)`, `s` the tangential section at `O`.
- **CK E1** (Proved there; checked in full by the review: correct). `s(Δ)` acts trivially on `N_2`; the subgroup of `N_2` fixed by the kernel of the cyclotomic character is its centre. The proof uses an involution of `P` that commutes with the Galois action and is −1 on `V`, +1 on the centre.
- **CK E2** (Proved there; checked in full: correct; it is LM3b D.5). A primitive eigenline in `N_2` is maximal procyclic and its normalizer maps onto `G_K`.
- **CK E3** (Open in the return; "open as stated" in the review, by spot check). For every `r` the last layer `γ_rP/γ_{r+1}P` of `N_r` is fixed by `s(Δ)`; for `r ≥ 3` it contains fixed elements outside the image of inertia (ranks of the layers for `r = 1, …, 10`: 2, 1, 2, 3, 6, 9, 18, 30, 56, 99). Not decided there: whether `P^{s(Δ)} = lim N_r^{s(Δ)}` contains an element outside the image of inertia; the same in the full profinite group; LM3b D.4. The first obstruction it names: for `v ∈ N_2`, the homomorphism `δ ↦ s(δ)(ṽ)·ṽ⁻¹` from `Δ` to `γ_3P/γ_4P`.
- **CK A6, A7** (Proved there; checked in full; A6 known in substance: Stix, *On cuspidal sections of algebraic fundamental groups*, Corollary 22 and Theorem 14, applied over `K(μ_∞)`). For the kernel `Γ°` of the cyclotomic character, the centralizer of `s(Γ°)` in the full geometric fundamental group is the inertia group at `O`. The proof uses that Tate modules have no invariants under the subgroup; this fails for `Δ` and this curve, since `Δ` fixes `V`.
```

## Block 2

```
**G. The Galois image on the once-punctured CM curve, degree by degree (CK E1–E3; LM3b D.4, D.5).** Notation of "After CYCLOTOMIC_KERNEL". `L = ⊕_r γ_rP/γ_{r+1}P` is the free Lie algebra over `Z_5` on `V`; a derivation of `L` is special if it kills `c`. `G_1 = Gal(K̄/K(E[5^∞]))` is the kernel of the action on `V`; for `δ ∈ G_1` and `m ≥ 1`, `D_m(δ)` is the part of degree `m` of the action of `s(δ)` on `P`. The leads are by Claude Fable 5.2 (effort max), 13 November 2026, checked by no one.
(a) Prove or refute: (1) every special derivation of degree 2 is a multiple of `ad(c)`, so that `D_2(δ) = a_s(δ)·ad(c)` with `a_s : G_1 → Z_5` continuous; (2) `D_m` vanishes on `G_1` for every odd `m` (by the involution of CK E1); (3) for every `m ≥ 1` the images of `Δ` and of `G_1` in degree `m` span the same `Q_5`-space (lead: for `g ∈ G_1` and `t ∈ G_K` the commutator of `t` and `g` lies in `Δ`, and `t` acts on the special derivations of degree `m` through characters `ψ^a ψ̄^b` of the CM torus with `a + b = m`, none of them trivial). Determine `a_s` for the tangential section of the parameter `x/y` as the Kummer character of an explicit element of `K*`, and for every section of the packet at `O`.
(b) (CK E3.) Prove or refute: for every section `s` of the packet at `O`, `P^{s(Δ)}` is the image of the inertia group. Lead: true. When `a_s` is not zero on `Δ` it follows from (a)(1): in a fixed element, the term of lowest degree outside `Q_5 c` is moved by `a_s(δ)·ad(c)`, because the centralizer of `c` in `L ⊗ Q_5` is `Q_5 c`. For the sections with `a_s | Δ = 0` it needs (c). Then prove or refute the same for the pro-ℓ quotients at the primes ℓ that do not split in `Z[i]`, and for the full profinite group.
(c) Determine the special derivations of degree 4 (lead, from memory: a free module of rank 3, the `sl_2`-module generated by Tsunogai's derivation `ε_4`, which sends `x` to `ad(x)⁴(y)`), their characters under the CM torus (lead: `ψ³ψ̄`, `ψ²ψ̄²`, `ψψ̄³`, where `ψ` is the character of the eigenline of `x`), and the three components `b_+, b_0, b_− : G_1 → Z_5` of `D_4`. Prove or refute that each is non-zero on `Δ`. Sources to open and quote: Nakamura's Eisenstein–Kummer characters for open elliptic curves; the specialization of the elliptic polylogarithm at a CM curve; `b_0` is a class in `H¹(K, Z_5(2))`.
(d) (LM3b D.4 for this curve.) Prove or refute: no closed procyclic subgroup of `P` outside the conjugates of the image of inertia has a normalizer in the arithmetic group with open image in `G_K`. Determine the largest `r` for which the eigenline of CK E2 lifts to a procyclic subgroup of `N_r` with that property. Lead: it lifts through `N_4` and stops at `N_5`: `ad(c)` moves `x` inside its conjugacy class, `ε_4` sends `x` into `[x, L]`, and the two other weight vectors of the module of (c) do not; so the answer turns on `b_0` and `b_−` being non-zero on `Δ`. Then prove or refute the statement for the full profinite group.
(e) By program, for every even degree `m` from 2 through 14: the module of special derivations of degree `m`, its characters under the CM torus, the image of the brackets of the lower degrees, and the place of the Galois image, set against the elliptic tables of Part B (d) and LM3b A.12–A.16. Rerun the Lyndon computation of CK E3 through degree 14.
Done for Part G: each of (a)–(d) is a theorem with its complete proof, or a refutation with the true statement proved in its place; the tables of (e) are computed, with code and output attached.
```

## What I checked of the leads

- (a)(1), re-derived: with `D(x) = α[x,c] + β[y,c]`, `D(y) = γ[x,c] + ε[y,c]` and `[x,[y,c]] = [y,[x,c]]`, `D(c) = γ[x,[x,c]] + (ε − α)[x,[y,c]] − β[y,[y,c]]`; so `D(c) = 0` forces `β = γ = 0`, `ε = α`, that is `D = −α·ad(c)`.
- (b), first case, re-derived: `Δ` acts trivially on `N_2` (CK E1), so the first term of the action is `a_s(δ)·ad(c)` in degree 2. For a fixed `v` with logarithm `v_1 + v_2 + …`: if `v_1 ≠ 0` the degree-3 term `a_s(δ)[c, v_1]` is not zero; if `v_1 = 0`, `v_2 = βc` and `v_k` is the first later non-zero term, the degree-`(k+2)` term is `a_s(δ)[c, v_k] ≠ 0` (the other contributions are `D_j` applied to `0` or to `βc`). So `v` is a power of `c`.
- Changing the section by a Kummer cocycle `κ` changes `a_s` by `±κ`, and a Kummer character of an element of `K*` that is not a root of unity does not vanish on `Δ`; so (lead) `a_s | Δ = 0` for one section of the pro-5 packet only.
- (a)(2): the involution is induced by `[−1]`, which sends the parameter `x/y` to its negative; `−1` is a 5-power, so it commutes with the Galois action on `P`; it acts by `(−1)^k` in degree `k`.
- Not checked: the formula for `ε_4` (Tsunogai, as in Pollack; from memory); that the middle and lowest weight vectors do not send `x` into `[x, L]`; the non-vanishing of `b_+, b_0, b_−`.

## Files the LM8 zip must add

Seen in the current `LM8_LIE_APPROXIMATIONS_background.zip`: `LM3b_return/` with the report and the results register only, `LM3b_review/REVIEW.md`, several papers of Hain and Matsumoto. To add:

| Place in the zip | Source | Why |
|---|---|---|
| `CYCLOTOMIC_return/` | `C:\Users\user\Documents\longue_marche_pro_pilot_20261104\answers\CYCLOTOMIC_KERNEL_unzipped\CYCLOTOMIC_KERNEL\`: `CYCLOTOMIC_KERNEL_paper.pdf`, `CYCLOTOMIC_KERNEL_paper.tex` (E1–E3 are in its part `sections/E_root.tex`), `CYCLOTOMIC_KERNEL_results.csv`, `CYCLOTOMIC_KERNEL_report.md` | CK E1–E3, A6, A7 with their proofs |
| `CYCLOTOMIC_return/code/` | the program of that return with the Lyndon and Heisenberg checks and its output (I believe `code\root_math_checks.py` with `root_math_checks_output.json`; not verified: the guard stopped the check) | (e) reruns it |
| `CYCLOTOMIC_review/REVIEW.md` | `C:\Users\user\Documents\grothendieck_archive_montpellier\pro_reviews_archive_20261112\CYCLOTOMIC_REVIEW_OPUS\REVIEW.md` | the verdicts quoted in Block 1 |
| `LM3b_return/` (more of it) | from the LM3b return: the sections that hold A.12–A.16 (the elliptic computation to degree 14) and D.4, D.5, with the elliptic programs | (d), (e) |
| `papers/` | Stix, *On cuspidal sections* (`C:\Users\user\Documents\Free or receipted\free\lm-expert-20261112\stix-cuspidal\stix_cuspidal_sections_arxiv_0809.0017.pdf`), if not there yet | CK A6 |
| `papers/` (to fetch; references from memory, verify each) | H. Nakamura, *On exterior Galois representations associated with open elliptic curves*, J. Math. Sci. Univ. Tokyo 2 (1995); H. Tsunogai, *On some derivations of Lie algebras related to Galois representations*, Publ. RIMS 31 (1995); A. Pollack, *Relations between derivations arising from modular forms* (thesis, 2009); R. Hain, M. Matsumoto, *Universal mixed elliptic motives* (arXiv:1512.03975) | (a), (c): the degree-2 and degree-4 characters; the derivations `ε_{2n}` |

## Handoff (R-149)

- The original R-149 task is complete; its record is `wargame_work\R149_NOTES_20261112.md`. After it: `GLOBAL_SHAPE_AFTER_CYCLOTOMIC_20261112.md` (the shape note), `GOOD_REDUCTION\PROMPT.md` with `ZIP_LIST.md` (lint-clean; packaged by the main session), and this file.
- Open on my side: this Part was not linted; the name of the E-program in the return was not verified; the four references of the last table row are from memory.
- My context is past 70 %: no further reading is possible in this session.

# LM7_FERMAT_TOWER: review of the 103 statements

Reviewer: Claude Fable 5.2, effort max (successor of the Longue Marche expert), 13 Nov 2026.
Return reviewed: `answers\LM7_FERMAT_TOWER_20261113T0227Z_unzipped\LM7_FERMAT_TOWER\` (GPT-6 Astra, ChatGPT Pro mode; marked INCOMPLETE by its author; 79 Proved, 12 Known, 9 Refuted, 3 Open).

## What this review rests on

- Read in full: all twenty files of `sections\` (the paper's LaTeX, 393 KB), the results register (index), the prompt, the expert's relay (KNOWLEDGE_HANDOFF, READING_BASE, FINDINGS), the notes for the push prompt, and the LM7 passages of `SHAPE_MAP_REVISION_20261113.md` (revision 1; revision 1b, H2 and H6 first row).
- **Not read** (compute bound of about 400K tokens): the return's `code\` (no program was opened or run), `report.md`, the ledgers, the run trace, and the manuscript itself. Cote 140-4 (§§50–53) was never read by this expert line (handoff, 1.2). So every claim of the form "this proves his formula (n) of scan s" is checked only as mathematics; whether the return quotes the manuscript correctly is **not checked**. Marked M below.
- Own checks, written and run here: `checks_author\check_finite.py` and `check_lie.py` with their outputs. They recompute: A.2–A.4, A.12, B.6, B.10, B.11, B.13 (H⁰, H¹), D.4 (two examples), D.7 (one case), D.10 (every certificate), D.11 (the whole table), D.17 (through 16 and 27), D.21 (the gamma line and the weight-9 vector), E.3 and E.4 (the relation and the ranks), E.25 (Hilbert symbols), E.26 (the group identity), E.28/E.29 (the examples), E.32 (the witness).
- Cited sources: none was opened in this review. Existence was confirmed on the arXiv listing for Borne–Emsalem–Stix (arXiv:1301.4429), Dolgushev–Guynee (arXiv:2401.06870) and Çiperiani–Stix (arXiv:1106.4255, 1308.4528). Theorem numbers are unverified everywhere. Marked S. Added after the review, while the push prompt was built: the statement of Borne–Emsalem–Stix used by E.36 was read in the arXiv TeX (the one theorem of its section "Lifting to F_D over the rationals": for X/Q smooth projective of positive genus and D a union of torsion sub-packets, every Galois section of π₁(X) lifts to π₁(F_D)); it is the statement E.36 uses.

Basis codes: **P** proof followed step by step; **C** confirmed by own program; **R** rests on a finite computation of the return that was not rerun; **S** rests on a cited source not opened here; **M** the correspondence with the manuscript's formulas was not checked.

Outcome words: correct, wrong, gap, known, open (as in the brief). A "Refuted" statement of the return is "correct" when the refutation and the replacement are right.

## Result

- correct: 88 (all 79 Proved and all 9 Refuted). Of these, 7 rest in part on computations not rerun (R: B.7, B.13, D.7, D.25, D.26, E.12, E.26) and 10 on a source not opened (S: A.10, A.16, A.17, D.21, D.23, E.24, E.29, E.30, E.33, E.36); they are marked. D.25 and D.26 depend on their computations entirely.
- known: 12 (the 12 Known; the reduction was followed in each, the source was not opened).
- open: 3 (D.13, D.19, E.23), stated precisely below and classified in `PUSH_ITEMS.md`.
- wrong: 0. gap: 0 in the steps followed.

## Table

| Id | Return | Outcome | Basis | Reason |
|---|---|---|---|---|
| A.1 | Proved | correct | P, M | Finite stage `∐_H A²` with cocycle `c(h,k)`; change of section is `(m,h) ↦ (m−d_h,h)`. |
| A.2 | Proved | correct | P, C | `λ₀ = ωσρσρ`, `λ₁ = ωρσρσ`, the four conjugations and the table of image orders (1, 6, 12, …) recomputed; freeness by the Bass–Serre quotient graph (5 vertices, 6 edges). |
| A.3 | Proved | correct | P, C | Normal closure of `δ = λ₁λ₀⁻¹` mod 12 has order 32, is `V₄ × Q₈`, is normal in `GL₂(Z/12)`; `T^m` lies in it only for `12 | m`; index 36. |
| A.4 | Proved | correct | P, C | Orders 1152, 2304, 4608; `[λ₀,λ₁] ≡ (1 4; 4 5)` mod 12, inside `K₃₂`, so reduction to `SL₂(Z/12)` does not factor through `𝔖_d`. |
| A.5 | Proved | correct | P | Ring law `(n+N[x])(m+N[y]) = nm+N[ny+mx+Nxy]`; unit locus `r+Nt` invertible. General `A[J]` argument followed. |
| A.6 | Refuted | correct | P, M | The three counterexamples are valid for the pushout as defined. |
| A.7 | Proved | correct | P, M | (A.7.1)–(A.7.3) rechecked by hand, including `(−5)^a5^b = 1−6a+4b−24ab`. |
| A.8 | Proved | correct | P, M | (A.8.1), (A.8.2) rechecked; `u(λ₀) = λ₀^{2ν+1}` rechecked in `𝔖_d`. |
| A.9 | Refuted | correct | P, M | Image of `F` is `M₀` (the coordinate sum is `3a₁`); raw scheme has the `3z = 0` fibre. |
| A.10 | Proved | correct | P, S | Coordinate change is integral both ways. LM1's scheme taken as quoted. |
| A.11 | Proved | correct | P, M | Follows from (A.8.5)–(A.8.6). |
| A.12 | Proved | correct | P, C, M | The cocycle `(a+b)b′` gives a group with orders 1, 2⁵, 4²: `D₈`. |
| A.13 | Refuted | correct | P, M | Image of the literal subgroup is `{ε₂ = ε₃}`. |
| A.14 | Proved | correct | P, M | Fibre products; law (A.14.2). |
| A.15 | Proved | correct | P, M | Point counts 32 and 72 and the unit conditions rechecked. |
| A.16 | Proved | correct | P, S | Fibre computation of `H₄₈` followed; the §48 groups and LM1 B.2–B.5 taken as quoted. |
| A.17 | Proved | correct | P, S | Matrix reduction `c(1+μc) = 0`, `c` a unit, followed. Input (Lochak–Schneps Lemma 5; Harbater–Schneps §1.3) not opened. |
| A.18 | Proved | correct | P | `ψ₃ = 3x⁴−4(1+λ)x³+6λx²−λ²` rederived; field `Q(ζ₁₂, ∛2)`. Agrees with D.18: `−8κ₂` mod 12 takes the values 0, 4, 8. |
| A.19 | Proved | correct | P, M | Central factor `ω^{ν+a} = 1`. |
| B.1 | Proved | correct | P, M | Models, deck group, `X₄⁺(R) = ∅`. |
| B.2 | Proved | correct | P | Monodromy `x ↦ (1,0)`, `y ↦ (0,1)`. |
| B.3 | Refuted | correct | P, M | Stabilizers computed on points. |
| B.4 | Proved | correct | P | Fox chain of `[x,y]` is `(1−Y, X−1)`. |
| B.5 | Proved | correct | P | Kernel of `f ↦ f·c` is `Z·N_n`. |
| B.6 | Proved | correct | P, C | Identities for `P_n` rechecked; own Smith forms for `n ≤ 6`: `R_n/I_n` torsion-free of rank `(n−1)(n−2)`. |
| B.7 | Proved | correct | P, R | Ranks follow from B.5, B.6; the matrices in the JSON were not opened. |
| B.8 | Proved | correct | P | The three limits argued directly (`lim nẐ² = 0`, peripheral part pro-zero, `P_{dn} ↦ dP_n + C(d,2)N_n`). Otsubo not needed for the proof. |
| B.9 | Proved | correct | P | `r(c) = c`, `s(c) = c⁻¹` rechecked by free reduction. |
| B.10 | Proved | correct | P, C | `H⁰ = H¹ = 0` for all `I`; brute force for `N` = 2, 3, 4, 6, 8, 12. |
| B.11 | Proved | correct | P, C | `ρ′³ = σ′² = (ρ′σ′)² = 1`, fixed point `(2/3, 1/3)`. |
| B.12 | Proved | correct | P, M | Translation `(1−μ)p`; uniqueness by B.10. |
| B.13 | Proved | correct | C, R | `|H²(S₃, M/N)| = gcd(N,3)` confirmed by a Sylow argument (review); the cochain verification of the actual class was not rerun, but the class is the reduction of an integral class and `H²(S₃, M) = 0`. |
| B.14 | Proved | correct | P | Kernel and quotient are identified, B.10 gives uniqueness. |
| C.1 | Known | known | S | Deligne, Hodge III, 10.1–10.3 (not opened); the reduction to it was followed. |
| C.2 | Refuted | correct | P | Ranks `n²+1` against 2; exact sequence (C.4) from B.5. |
| C.3 | Proved | correct | P | Kernel `I_n` by B.6. |
| C.4 | Proved | correct | P | `H(Q) = ⟨n−1, n⟩` has `g` gaps; a proper divisor `d ≤ n/2 < n−1` is a gap. |
| C.5 | Proved | correct | P | Class is `D ↦ [D]`; order `n` by C.4. |
| C.6 | Known | known | S | Rohrlich 1977, Theorem 1 (not opened; the statement agrees with the theorem as the reviewer knows it; `3², 5⁸, 7¹⁴` equal `(Z/n)^{3n−7}`). |
| C.7 | Proved | correct | P | Cartesian square on the torus chart. |
| C.8 | Refuted | correct | P, M | Mathematics correct; the reading of scans 143–153 was not checked. |
| D.1 | Proved | correct | P, M | Parity of `κ_{−1/2}` is the character of `Q(√−2)`; image on `G_K` is `2Ẑ(1)`. |
| D.2 | Proved | correct | P | `a ∈ K^{×n} ⟺ n | 2e_i` (a real Galois field has at most two real roots of `Xⁿ−a`). |
| D.3 | Proved | correct | P, M | `u−1 = dv` construction and (D.3) followed; counterexamples valid. |
| D.4 | Proved | correct | P, C | Formula (D.4) rederived; `v₁₁(3¹⁰−1) = 2`, `v₇(19⁶−1) = 3`. |
| D.5 | Known | known | S | Otsubo (6.1, 6.2, 7.2), Anderson, Ihara: not opened. |
| D.6 | Known | known | S | Otsubo 8.1 not opened; the plus-model twist `θ(−1)^{a+b}` followed. |
| D.7 | Proved | correct | C, R | Own count for `(p,n) = (43,6)`: 12 and 108 points. The rest of the range not rerun. |
| D.8 | Known | known | S | Ihara–Kaneko–Yukinari not opened; the formula has the form of Ihara's ICM 1990 statement as the reviewer remembers it. |
| D.9 | Known | known | S | Ichimura–Kaneko not opened. |
| D.10 | Proved | correct | C | Every witness recomputed: each odd `m ∈ [3, ℓ−2]` is certified by a listed `q` for all 13 primes; only irregular pair below 50 is (37, 32). |
| D.11 | Proved | correct | C | Whole table recomputed modulo two primes: special 0,0,1,0,3,0,6,4,13,12; image 0,0,1,0,3,0,5,0,7,0; invariant 0,0,1,0,1,0,2,1,4,2; image 0,0,1,0,1,0,1,0,2,0. |
| D.12 | Proved | correct | P | Successive approximation; `[·,y]` and `[·,x+y]` span `L_m`; fixed points lift for a group of order prime to `ℓ`. |
| D.13 | Open | open | — | Statement below. |
| D.14 | Proved | correct | P | Norm residues; LM2 C.d2 as quoted. |
| D.15 | Known | known | P, S | Twists at `λ = 1/2` and `λ² − λ + 1 = 0` rechecked by hand; the match with LM2 C.d4 and the CM references were not opened. |
| D.16 | Proved | correct | P | `[E : Q^ab] ≤ 2` and `M = Q(i, ∜3) ⊂ E`; rests on D.15. |
| D.17 | Proved | correct | C | Table recomputed at 2, 4, 8, 16, 3, 9, 27 (level 32 not rerun). |
| D.18 | Known | known | S | Tate-curve reference not opened; `q = λ²/256·(…)` gives `−8κ₂`; consistent with A.18. |
| D.19 | Open | open | — | Statement below. |
| D.20 | Known | known | S | Ihara, beta and gamma functions II, and Anderson 8.6.3: not opened. |
| D.21 | Proved | correct | C, S | Gamma line lies in the invariant image in weights 3, 5, 7, 9; `X²Y²(X+Y)³` is in the weight-9 image and independent of it (own program). Upper bound rests on Furusho 2011, lower bound on Hain–Matsumoto: not opened. |
| D.22 | Known | known | P, S | Compactness argument followed; Dolgushev–Guynee 5.2, 5.4, 5.5 not opened. |
| D.23 | Proved | correct | P, S | (D.24), the Haar idempotent, the inertia-at-2 witness followed; (D.25) rests on Ihara's Theorem 1. |
| D.24 | Known | known | P, S | `A₅` example followed; Gaschütz lemma (Bleher–Chinburg–Lubotzky) not opened. |
| D.25 | Proved | correct | P, R | Field identities followed; the counts of (D.25.2) (rank-97 computation in `G₂`, `G₃`, `G₆`) rest on the return's program. |
| D.26 | Proved | correct | P, R | Isolation argument and the non-cofinal quotient `J` followed; Smith forms `(1⁹⁶, 2)` and `(1⁹⁷)` rest on the return's program. |
| E.1 | Proved | correct | P | Cellular chains of the cover with group `F/F″`. |
| E.2 | Proved | correct | P | Elimination; `⌊(n−1)/2⌋`. |
| E.3 | Known | known | C, S | `{σ₃,σ₉} − 3{σ₅,σ₇} = 0` exactly, ranks 1, 1, 1, 2 in weights 8–14 (own program). Hain–Matsumoto and Brown not opened. |
| E.4 | Proved | correct | P, C | `{σ₃,σ₅} ≠ 0`. |
| E.5 | Proved | correct | P | Tests against `BH`; pseudolimit argument for relative Theorem A. |
| E.6 | Proved | correct | P | Kernel is `NV(F)/V(F)`. |
| E.7 | Proved | correct | P | Element `[a, tat⁻¹]`. |
| E.8 | Proved | correct | P | Frattini ranks. |
| E.9 | Proved | correct | P | Roots in unipotent groups. |
| E.10 | Proved | correct | P | The three constructions `V ⋊ F` followed, including the metabelian one. |
| E.11 | Proved | correct | P | `b[a,b] = a` for `a = (12)`, `b = (13)` rechecked. |
| E.12 | Proved | correct | R | Enumeration not rerun; the general statements are E.6–E.9. |
| E.13 | Proved | correct | P | Specialization. |
| E.14 | Proved | correct | P | Averaging over `G`. |
| E.15 | Proved | correct | P | Magnus coefficient argument. |
| E.16 | Proved | correct | P | `H¹(Q, Ẑ(1)) = lim Q^×/m`. |
| E.17 | Refuted | correct | P | Leading coefficients `(1, −1)` at both cusps. |
| E.18 | Proved | correct | P | `N^ab = Z ⊕ Z[C₂]⁸`; class of `a²` in `Ĥ⁰ = Z/2`. |
| E.19 | Proved | correct | P | Rational 3-torsion point is not divisible by 3. |
| E.20 | Proved | correct | P | `(2,3)₃ = −1`. |
| E.21 | Refuted | correct | P | Swap sends `[y,[y,[y,x]]]` out of `D³`. |
| E.22 | Refuted | correct | P | `[h₃, h₅]` dies in `M(0)` and acts by a multiple of `B_{2,4}`. |
| E.23 | Open | open | — | Statement below. |
| E.24 | Proved | correct | P, S | `Y²+Y−X³+7 = 27(x³+y³+z³)/(x+y)³` rechecked; curve 27a1. (E24.8) rests on Çiperiani–Stix (not opened); it also follows from Cassels–Poitou–Tate with `E(Q)` finite (review, sketch). |
| E.25 | Proved | correct | P, C | See item 2 below. |
| E.26 | Proved | correct | P, C, R | `(xρ)³ = [x,y]`, `((xρ)σ)² = 1` recomputed in `PSL₂(Z)`; `H²(S₃, Z(sign)) = Z/3`; the order-162 enumeration not rerun (not needed: (E.26i)). |
| E.27 | Proved | correct | P | Riemann–Hurwitz. |
| E.28 | Proved | correct | P, C | 6 has order 108 mod 109; the tame relation forces commuting images in exponent 27. |
| E.29 | Proved | correct | P, C, S | Tame symbol; `H¹(Q, Z₃(2)) = Z/3`; examples recomputed. Tate's `K₂(Q)` from the K-book (not opened; classical). |
| E.30 | Proved | correct | P, S | Unipotent and scalar at once forces zero; Nikolov–Segal for the abstract case. |
| E.31 | Proved | correct | P | Divisors of `h`, `1−h`; local computation at `(3+ζ)`. |
| E.32 | Proved | correct | P, C | See item 1 below. |
| E.33 | Proved | correct | P, S | Euler characteristic and Leopoldt for abelian fields. |
| E.34 | Proved | correct | P | `G_{Q(ζ₃),{3}}(3)` free of rank 2; embedding problems solvable. |
| E.35 | Proved | correct | P | Cyclic algebra split iff `b` is a norm. |
| E.36 | Proved | correct | P, S | Presentation and rank 44 followed. Existence of lifts rests on Borne–Emsalem–Stix 5.10 (not opened); supported by a reciprocity argument (review): the obstruction lies in `H²_cts(Q, Z₃(1))`, which injects into the local groups, and every local term outside 3 vanishes. |

## The three open statements, precisely

- **D.13.** Let `Out^♯(F̂₂)` be the loop-preserving outer automorphisms of the free profinite group and `GT̂₀` the centralizer of `S₃` in it. Their images in the graded Lie algebra of pro-ℓ special outer derivations modulo `L″` lie in rows 2 and 4 of (D.11). Open: (i) whether the image of `Out^♯(F̂₂)` in weight 5 has dimension 3 (the pro-ℓ value), 2 or 1 (the Galois value); (ii) whether the image of `GT̂₀` in weight 9 has dimension 2 or 1, that is, whether it contains a vector outside the line of `((X+Y)⁹−X⁹−Y⁹)/(XY)`, for instance `X²Y²(X+Y)³`.
- **D.19.** (i) the same two questions; (ii) whether some element of `GT̂₀` has CM coordinates `(T, W)` in the coset that Galois misses (D.16), equivalently whether one of the twelve nonarithmetical shadows of D.25 at `Ñ₆` lies in `⋂_K R_{K,Ñ₆}(GT(K))` (D.22).
- **E.23.** The set of continuous section classes of `(N/γ₃N) ⋊ G_Q`, `N` the geometric pro-3 group of `U₃⁺` (free of rank 10), as a subset of the classes of `N^cc ⋊ G_Q` computed in E.36, with its fibres; then the same for the metabelian and marked depth-two quotients.

## Findings

1. **No statement was found wrong and no step followed has a gap.** This covers the proofs as written. It does not cover the return's programs, the cited theorem numbers, or the manuscript correspondences (marks R, S, M).
2. **E.32 is a lim¹ class (item 1).** Proved in `PUSH_ITEMS.md`, Part 1: under `H²_cts(G_Q, Z₃(2)) ≅ R/dR`, Jannsen's sequence is `0 → {z ∈ R : (q−1) | z_q}/dR → R/dR → lim_n ⊕_q Z/(3ⁿ, q−1) → 0`, the left term is `lim¹_n H¹(G_Q, Z/3ⁿ(2)) ≅ lim¹_n ⊕_q (Z/3ⁿ)[q−1]`, and that tower is Mittag-Leffler exactly when `v₃(q−1)` is bounded. The witness of (E.32f) recomputed: `q_j` = 109, 163, 487, 1459, 39367, 131221, each with `c_q = −1`.
3. **E.25: the class is `(−1,−1)`, and it is nonzero at two places, not one (item 2).** `κ₂(−1) ∪ κ₂(−1)` is the Hamilton quaternion class. Its local invariants are nonzero exactly at `∞` and at 2 (`x²+y²+z²` is anisotropic over `Q₂`: no primitive zero mod 8) and zero at every odd prime. A class in `Br(Q)` cannot be nonzero at one place only (reciprocity). The sentence "nonzero exactly at the real place" is false; "its invariant at ∞ is nonzero" (the wording of the shape map, H2) is true. The class is the Brauer class of the conic `X₂⁺: x²+y²+z² = 0`, pulled back along `U_n⁺ → X₂⁺` for even `n`: this conic has no point over `R` and none over `Q₂`. The line "Both are archimedean" in H2 needs "and 2-adic".
4. **The rank-44 test statement, as worded in the notes, is contradicted by E.34.** "No section class of E.32 outside the point and cusp classes survives the rank-44 lift" fails for classes unramified outside 3: by E.34 every class of `H¹(G_{Q,{3,∞}}, V) ≅ Z₃⁶ ⊕ (Z/3)³` lifts to the whole pro-3 geometric group, hence through the rank-44 kernel, while the cuspidal classes unramified outside 3 lie on three cosets of rank one (`U₃⁺(Q) = ∅`; only the three rational cusps give sections over `Q`). Example: `κ(3)·(e_O + e_P)`, the sum of the inertia directions at two rational cusps, is in none of the three cosets (its image in `H¹(Q, T₃E)` is zero and its `e_P`-component is not). The reviewer's argument is short and unchecked by a second reader; `PUSH_ITEMS.md` asks for its proof and for the corrected statement.
5. **Where lim¹ can and cannot occur.** For weight −2 coefficients `Z₃(1)` the tower `H¹(G_Q, μ_{3ⁿ}) = Q^×/3ⁿ` has surjective transitions, so `H²_cts(G_Q, Z₃(1))` injects into the product of the local groups: no phantom class (this is why E.36 has no obstruction). In the rank-44 kernel the weights are −3 (`T ⊗ W`, rank 16) and −4 (`Λ²W`, rank 28); there `Frob_q − 1` on the residue module is injective with unbounded 3-adic determinant, so the lim¹ term is nonzero. E.23 is therefore exposed to the failure of E.32. D.13 and D.19 are not: they are limits of finite sets, where Mittag-Leffler is automatic, and what fails is cofinality, as in D.26.
6. **Cross-check A.18 against D.18.** The level-12 image `{(μ t; 0 1) : t ∈ {0,4,8}}` (found through the 3-division polynomial of the Legendre curve) and the Tate-curve formula `t = −8κ₂` (found through `q = λ²/256·(…)`) agree: `−8κ₂` mod 12 is `4κ₂` mod 12, with kernel field `Q(ζ₁₂, ∛2)`. Two independent routes.
7. **For the editors.** The return reports many corrections to the manuscript's formulas ((54), (55), (59), (67b), (68), (77), (83), (100)–(101), (151), (171)–(172), (194)–(195), the coefficients `−3ab`, `−2ab`). Each is mathematically valid for the objects as the return defines them. None was compared with the scans here.

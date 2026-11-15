# Intake of LM8_LIE_APPROXIMATIONS, 167 rows (checkpoint 16, the run's last state; INCOMPLETE)

Reader: Claude Fable 5.2 (Anthropic), effort high, 13 Nov 2026. Return: GPT-6 Astra (OpenAI, ChatGPT Pro mode),
`answers\LM8_LIE_APPROXIMATIONS_checkpoint_16_20261113T1145Z_unzipped\LM8_LIE_APPROXIMATIONS\`.
This is an intake at effort high. The sections are about 900 KB of TeX; about 110 KB of it was read.

## Result

- CONSISTENT 161 (122 Proved, 24 Refuted, 15 Known). OPEN 6 (A.12, B.24d, B.28, F.12, G.16, G.20). DOUBT 0. WRONG 0.
- Of the 161: **32 with the proof read and followed, re-derived or recomputed here** (basis P, D or C; for B.16
  and B.18 only the first rows of the tables); **129 at statement level only** (basis S). A statement-level verdict says that the statement is well formed,
  agrees with the rows it depends on and with what I know; it is not a check of the proof.
- Read in full with the proof: A.2, A.7, B.11, B.12, B.17, C.6, D.4, D.10, D.14, D.23, E.4, E.5, E.10, E.11, F.4,
  F.15, F.21, G.6, G.10, G.11. Re-derived here from the statement (basis D): A.22, B.6, B.7, B.32, B.34.
  Recomputed by hand or script (basis C): the three dimension formulas of B.10, B.16 (first row), B.18 (first row),
  F.3 (the three thresholds), the eight primes of F.21 (`v_5(q−1) = n`, 5 not a fifth power; all prime).
- Not opened: `code\` (no program read or run), the readings CSV, the bibliography, the trace beyond its headings,
  the manuscript and its scans. Every "his scan n says" is unchecked (basis M). Sources cited by the return were
  not opened (basis L). Several are 2025–2026 preprints (Ishii 2025; Ishii–Goto 2026; Ishii 2026; Goto–Ishii 2026;
  Dorigoni et al. 2026; Boggi 2026; Lochak–Nakamura–Schneps 2026): recent and unrefereed, existence not verified here.

Basis codes: **P** proof read and followed; **D** re-derived by the reader; **C** recomputed; **S** statement level
only; **R** rests on the return's programs (not rerun); **L** rests on a source not opened here; **M** manuscript
correspondence not checked.

## The rows a manuscript correction rests on (all read in full unless marked)

| Row | Passage | Correction | Verdict |
|---|---|---|---|
| A.2 | §52.1, scans 190–191 | germ axioms do not fix the defining subgroup up to commensurability (`P_{2,0} × P_{2,0}`); the class is data | CONSISTENT (P, M) |
| A.7 | §52.1, scans 185–188 | `PSL_2(Z)` is not characterized by trivial `Out_L^+` and trivial centralizers (`C_2 * C_4`) | CONSISTENT (P, M) |
| A.15 | scans 188, 193–195 | `Out_L = C_2` does not pass to the completion (`Ẑ^×` appears) | CONSISTENT (S, M) |
| B.24 | §51.2, scan 41 | the signed conjugator datum does not lift to the integral `q_2` Fermat stage over `F_2[ε]` | CONSISTENT (S, R, M) |
| D.3, D.4, D.10 | scans 213–217, (53)–(57) | fibrewise unipotent ⇏ integral parameter; smooth closure ⇏ primitive lattice; (57) does not present the sheaf | CONSISTENT (D.4, D.10: P; D.3: S; M) |
| D.14 | §50.2, scans 10–11 | "quasi-compact base" is not enough (non-quasi-separated gluing, `α_p(t) = t + ε(t^p − t)`); true for qcqs (D.21) | CONSISTENT (P, M; D.21: S) |
| D.23 | scan 213 | `M → H(Z)` is impossible with open cyclotomic image; no uniqueness from (45)–(49) | CONSISTENT (P, M) |
| E.4 | scans 228, 232 (18), 233 (23) | `u(z)/|u(z)|`; shift `(2n, −3n)`; reflection `t ↦ 1/4 − t` | CONSISTENT (P, M) |
| E.5 | cote 140-1, scans 29, 35–36 | the "?" extension is `B_3` over `SL_2(Z)`, class 1 of `Z/12` with his sign (class 5 with the other) | CONSISTENT (P, M) |
| E.11 | scans 242–243 | the inverse limit of the sheaf topoi of shrinking punctured discs is the empty topos; the covering germ is `BZ` | CONSISTENT (P, M); scope remark below |
| E.13 | scans 242–243, 273–280 | topological and differentiable germ groups differ; infinite-sheet germs need cofinality | CONSISTENT (S, M) |
| F.4 | (371)–(373), scans 173, 178 | tangential sections at 0 and 1 coincide in every abelian approximation | CONSISTENT (P) |

Scope remark on E.11 (reader, from memory of SGA 4 VI §8 and VII §5, not opened): the proof is right for the
classical topology (a join of zeros equal to 1). For coherent topoi with coherent transition maps the limit topos
is well behaved (its coherent objects are the 2-colimit; cohomology commutes): the étale topoi of the punctured
henselian neighbourhoods have limit the étale topos of the fraction field of the henselization, which is `BẐ(1)`
on a curve in characteristic 0. So "fails as written" holds for the topological reading only; whether scans
242–243 mean the topological one was not checked. See PUSH_ITEMS.

## Table

| Id | Return | Claim (short) | Verdict | Basis | Reason / remark |
|---|---|---|---|---|---|
| A.1 | Proved | discrete L structure as a filtered colimit; ΠL not defined in the body | CONSISTENT | S, M | scans 179–182 absent from the package |
| A.2 | Refuted | germ-only LT axioms | CONSISTENT | P, M | above |
| A.3 | Known | hyperbolic L-group = orbifold extension of a finite action | CONSISTENT | S, L | Nielsen realization (Kerckhoff) |
| A.4 | Proved | centralizer = finite ineffective kernel | CONSISTENT | S | |
| A.5 | Proved | exceptional types; criterion fails for torus translations | CONSISTENT | S | |
| A.6 | Proved | realizations are `Aut_L` / `Out_L` torsors; three examples | CONSISTENT | S | |
| A.7 | Refuted | characterization of `PSL_2(Z)` | CONSISTENT | P, M | above |
| A.8 | Proved | `C_2 * C_3`: `Out_L^+ = 1`, `Out_L = C_2`, `Aut_L = PGL_2(Z)` | CONSISTENT | S | |
| A.9 | Proved | `Out_L(P × A)` for finite abelian `A` | CONSISTENT | S | |
| A.10 | Proved | enumeration (24 groups of order ≤ 12, 42 rows, 17 realizable) | CONSISTENT | S, R | |
| A.11 | Proved | profinite extension is a completion iff the outer action lifts to the discrete group | CONSISTENT | S | |
| A.12 | Open | unrestricted profinite finite-action realization | OPEN | S | reduced to: does the involution of A.22 lift from `F̂_2/F̂_2''` (and its relative pro-5 lifts A.23–A.26) to `F̂_2`, or is there a finite obstruction; mixed multipliers remain |
| A.13 | Known | profinite L definition (Boggi–Zalesskii 2019, 3.6) | CONSISTENT | S, L | |
| A.14 | Proved | centralizer criterion and torsors, profinite | CONSISTENT | S | |
| A.15 | Refuted | `Out_L = C_2` in the completion | CONSISTENT | S, M | |
| A.16 | Refuted | mixed-prime involution: semidirect product is not a completion | CONSISTENT | S, R | |
| A.17 | Proved | finite subgroups of the geometric closure, `S_{1,1}`; solvable ones, genus ≤ 2 | CONSISTENT | S, L | |
| A.18 | Proved | necessary conditions; tripod realization ⇒ finite subgroups of `GT` are 1 or `C_2` | CONSISTENT | S, L | |
| A.19 | Proved | normalized lifts `x ↦ x^u, y ↦ f^{-1}y^u f`; norm equations; invisible pro-prime | CONSISTENT | S | |
| A.20 | Proved | mixed sign passes nilpotent tests, fails in `D_24` (250 groups of order ≤ 48) | CONSISTENT | S, R | the count 250 is right |
| A.21 | Proved | pure involution problem = finite inverse system (A–I); trivial in the `S_3` quotient | CONSISTENT | S, R | |
| A.22 | Proved | `F̂_2/F̂_2''` has a non-inner order-two pure peripheral automorphism with multiplier one | CONSISTENT | D | re-derived: on `F'/F'' = Λ[x,y]` take `λ = 1 − 2e`, `e` the idempotent of a `Z_5[ζ_3]`-component with `x, y ↦ ζ`; `u = −2e/((x−1)(y−1))` exists there, `(1+λ)u = 0`; `xy − 1` is a unit there, so the third class is preserved; `e ↦ 0` in every pro-prime quotient |
| A.23 | Proved | lift to the quotient with free class-two pro-5 kernel | CONSISTENT | S, R | |
| A.24 | Proved | lifting families at classes 3, 4 (dimensions 4, 20) | CONSISTENT | S, R | |
| A.25 | Proved | class 5: affine `Z_5^{90}` | CONSISTENT | S, R | |
| A.26 | Proved | lift through the whole relative pro-5 completion of the index-3 kernel | CONSISTENT | S | |
| B.1 | Proved | his Galois–Teichmüller axioms and "Lie approximation" as a definition (adelic, diagonal rationality) | CONSISTENT | S, M | |
| B.2 | Proved | universal pro-object of admissible targets | CONSISTENT | S | |
| B.3 | Refuted | Lead 1 (nilpotent tower) is not his object | CONSISTENT | S, M | |
| B.4 | Proved | two chosen Malcev stages for (0,3), (0,4), (1,1) | CONSISTENT | S | |
| B.5 | Proved | `V(F) = lim F/[K,K]`; exact on finite covers | CONSISTENT | S | |
| B.6 | Proved | `W_𝔞` is a fundamental localizer for ab, metabelian, class `c`, pro-ℓ, unipotent, `V` | CONSISTENT | D | `W_𝔞` = maps `f` with `Map(f, BG)` an equivalence for all `G` with `𝔞G = G`; such a class is closed under homotopy colimits |
| B.7 | Proved | comparison maps for finite quotients (images, kernels) | CONSISTENT | D | rank `d − 1` by Schreier |
| B.8 | Proved | Fermat cover: dimensions `n²+1, 2, n²−1`; `H_1(N,Q) = Q ⊕ Q[H]` | CONSISTENT | S | |
| B.9 | Proved | intrinsic finite coverings: ℓ-group monodromy (pro-ℓ); trivial (unipotent); none (ab, metabelian, nilpotent); all (`V`) | CONSISTENT | S | settles the second lead of the prompt |
| B.10 | Proved | exact sequence for special derivations; tripod table to weight 14 | CONSISTENT | C | formula recomputed: 0,0,1,0,3,0,6,4,13,12 (agrees with LM7 D.11) |
| B.11 | Proved | every integral special leading term lifts, every prime | CONSISTENT | P | successive correction; Burnside basis; Hopfian |
| B.12 | Proved | ℓ ≥ 5: `S_3`-invariant terms lift; pro-ℓ `GT_0 ⊋ GT` (`q_7`, defect 16 on `a⁵bcb`) | CONSISTENT | P, R, L | confirms the reviewer's result; Harbater–Schneps 2000 not opened; the pentagon coefficient is the return's and LM2's |
| B.13 | Proved | modular `H^1, H^2(S_3, M_n)`, `p = 2, 3`, `n ≤ 9` | CONSISTENT | S, R | |
| B.14 | Proved | lifting at every prime; `q_7, 2q_7, 3q_7` lift at 2 and 3 | CONSISTENT | S | through B.14d |
| B.14a | Proved | integral jet through class 13 | CONSISTENT | S, R | |
| B.14b | Proved | class 14 system (5030 × 2497, rank 2066) | CONSISTENT | S, R | |
| B.14c | Proved | `H^1(S_3, T_n) = 0` integrally, `n ≤ 9` | CONSISTENT | S, R | consistent with B.13 through `H^1(T/p) ≅ H^2(T)` |
| B.14d | Proved | `H^1(S_3, T_n) = 0` for all `n` at 2, 3; infinite lifts | CONSISTENT | S, L | Bryant–Kovács–Stöhr 2002, Kovács–Stöhr 2000 not opened |
| B.15 | Refuted | at (0,3) the Lie normalizer is everything; the finite `S_3` must be kept | CONSISTENT | S | |
| B.16 | Proved | (0,4) table through degree 6 | CONSISTENT | C, R | first row recomputed (2,1,6,6,28,36); the others rest on the program |
| B.17 | Refuted | filling (0,4) → (0,3): exact on the normalizer with image `GT × S_3`, not onto `GT_0 × S_3` | CONSISTENT | P, L | Hoshi–Minamide–Mochizuki 2022, Hoshi–Mochizuki 2011 not opened |
| B.18 | Known | elliptic table through degree 12; normalizer quotient in degrees 6, 10 | CONSISTENT | C | `𝔢_n` and `𝔲_n` recomputed by hand (3; 5; 10; 24; 50) |
| B.19 | Refuted | normalizer mod geometry at (1,1) is not the `ε`-algebra | CONSISTENT | S | follows from B.18 |
| B.20 | Proved | integral envelope of a virtually abelian stage (LM1 E.14 form) | CONSISTENT | S | |
| B.21 | Proved | filling is split surjective on `V`, envelopes, Malcev truncations | CONSISTENT | S | |
| B.22 | Proved | comparison maps to weighted and Teichmüller completions; no identification | CONSISTENT | S | |
| B.23 | Proved | all 74 groups of order ≤ 24, 9,714 epimorphisms, 65 two-generated | CONSISTENT | S, R | 74 and 65 agree with my count |
| B.24 | Refuted | minimal integral comparison fails over `F_2[ε]` | CONSISTENT | S, R, M | |
| B.24a | Proved | integral `q_2` stage; Smith entries 2, 2 | CONSISTENT | S, R | |
| B.24b | Proved | liftable locus `t² = t`; kernel | CONSISTENT | S, R | |
| B.24c | Proved | rational lifts exist at the first stage | CONSISTENT | S | |
| B.24d | Open | conjugator images on `q_2` and higher stages; kernels; polynomial lifts | OPEN | S | reduced by B.31–B.35 to the stages above the first |
| B.25 | Proved | `F_2 → C_2 * C_3`: rank-7 relative radical over `S_3` | CONSISTENT | S, M | |
| B.26 | Proved | graded joint surjectivity | CONSISTENT | S | |
| B.27 | Proved | compatible-image dimensions, weights 1–9 | CONSISTENT | S, R | |
| B.28 | Open | whether a given profinite automorphism (every pentagon solution) satisfies the §47 equation | OPEN | S | reduced to computing the relative action induced by a full profinite word; graded and filtered forms are B.26, B.30 |
| B.29 | Refuted | preserving the finite factors of `C_2 ⨿ C_3` ⇏ preserving the cusp (`PSL_2(F_13)`: 13 → 7) | CONSISTENT | S, R, L | |
| B.30 | Proved | filtered surjectivity over `Q`, and pro-ℓ for ℓ ≥ 5 | CONSISTENT | S | |
| B.31 | Proved | the signed source preserves every Fermat kernel; local and profinite actions | CONSISTENT | S, M | |
| B.32 | Proved | `⋂ [K_n, K_n] = F''`; what the pro-prime Fermat family detects | CONSISTENT | D | first claim re-derived (residual finiteness of `F/F''`) |
| B.33 | Proved | image on `C/F'` is `Ẑ ⋊ Ẑ^×` | CONSISTENT | S, R | |
| B.34 | Refuted | no `Q`-defined action of the whole profinite source (multiplier `√6 ∈ Z_5`) | CONSISTENT | D | |
| B.35 | Proved | first-stage images of `N_ρ^*`, `N_σ^*` | CONSISTENT | S, R, L | |
| C.1 | Known | global quotient ⇔ étale scheme cover ⇔ injective inertia (Behrend–Noohi) | CONSISTENT | S, L | |
| C.2 | Refuted | effective exceptions: teardrops and unequal footballs | CONSISTENT | S, L | |
| C.3 | Refuted | gerbe exceptions | CONSISTENT | S, L | |
| C.4 | Proved | existence descends from `Q̄` to `Q` | CONSISTENT | S | |
| C.5 | Proved | covers of the complement of a boundary meeting every residue characteristic extend | CONSISTENT | D, L | re-derived from SGA 1 XIII 5.3 (tame group prime to the residue characteristic); source not opened |
| C.6 | Proved | `π_1^ét(M_{1,1,Z}) = 1`; no `[C/G]` | CONSISTENT | P | Weierstrass atlas, purity, Minkowski |
| C.7 | Known | `M_{1,1} = [Y(3)/GL_2(F_3)]` over `Z[1/3]` | CONSISTENT | S, L | |
| C.8 | Proved | `π_1^ét(M_{0,4,Z}) = π_1^ét(M_{0,5,Z}) = 1` | CONSISTENT | S | |
| C.9 | Proved | quotient stacks have `π_1 = S_4, S_5` | CONSISTENT | S | |
| C.10 | Proved | finite checks | CONSISTENT | S, R | |
| D.1 | Proved | quasi-unipotent germ ⇒ unique one-parameter group | CONSISTENT | S | |
| D.2 | Proved | integral extension ⇔ divided powers; positive power lies on `G_a` (linear) | CONSISTENT | S | LM1 E.3, E.10 |
| D.3 | Refuted | fibrewise unipotent ⇏ undilated parameter (rank 5, `X⁴/4! = E_15/2`) | CONSISTENT | C | `1·2·3·2/24 = 1/2` |
| D.4 | Refuted | smooth closure ⇏ primitive lattice | CONSISTENT | P, M | |
| D.5 | Proved | additive subgroups spanning the Lie algebra generate a smooth group | CONSISTENT | S | |
| D.6 | Proved | Dehn twists on Malcev classes 1, 2; denominators at 2, 3 | CONSISTENT | S | |
| D.7 | Proved | braid, reflection, centre-square identities, classes 1–4 | CONSISTENT | S, R | |
| D.8 | Proved | over `Z/p^e`: finite order on the special fibre ⇒ finite order | CONSISTENT | S | |
| D.9 | Proved | positive-power theorem on qcqs bases; scan 213 question answered by D.22 | CONSISTENT | S, M | |
| D.10 | Refuted | (57) does not present the integral sheaf (Heisenberg, `t^p − t`) | CONSISTENT | P, M | |
| D.11 | Proved | dual numbers in characteristic 0, any separated f.p. group | CONSISTENT | S | |
| D.12 | Proved | uniqueness after dilation; descent | CONSISTENT | S, L | |
| D.13 | Proved | base killed by `N`: quasi-unipotent sections are torsion | CONSISTENT | S | |
| D.14 | Refuted | quasi-compact alone | CONSISTENT | P | above |
| D.15 | Proved | regular one-dimensional `Q`-schemes | CONSISTENT | S, L | |
| D.16 | Proved | integral Noetherian with small rational fibre | CONSISTENT | S | |
| D.17 | Proved | denominators of rational functions with integer values | CONSISTENT | S, L | |
| D.18 | Proved | Noetherian `Q`-schemes | CONSISTENT | S | |
| D.19 | Proved | extension over a local ring after dilation | CONSISTENT | S | |
| D.20 | Proved | all Noetherian bases | CONSISTENT | S | |
| D.21 | Proved | all qcqs bases | CONSISTENT | S | the main result of Part D; not read; first for the expert |
| D.22 | Known | smooth affine `Z`-model containing a compact adelic image (BLR) | CONSISTENT | S, L | |
| D.23 | Refuted | scan 213 recap; no uniqueness | CONSISTENT | P, M | |
| E.1 | Proved | universal cover of `SL_2(R)`, signed extension of `GL_2(R)_{±1}` | CONSISTENT | S | |
| E.2 | Proved | positive integral lifted group is `B_3`; kernel = centre squared | CONSISTENT | S | standard |
| E.3 | Proved | `ST_{1,1} ≅ GL_2(Z)^~ = B_3 ⋊ C_2` (not central) | CONSISTENT | S, M | corrects Lead 2's "central extension" for the full group |
| E.4 | Refuted | three formulas | CONSISTENT | P, M | |
| E.5 | Proved | the 140-1 draft extension | CONSISTENT | P, M | |
| E.6 | Known | `GT̂` action on `B̂_3` | CONSISTENT | S, L | |
| E.7 | Proved | normalizer of `B̂_3` is a split extension of `GT̂` by `B̂_3` | CONSISTENT | S, L | Minamide–Nakamura 2022, Asada 2001 not opened |
| E.8 | Known | Tate–Weierstrass section; Kummer correction `a^{−8ρ_2}` | CONSISTENT | S, L | |
| E.9 | Proved | charming GT-shadows, `|Q_3(m)| ≤ 1000` | CONSISTENT | S, R | |
| E.10 | Proved | covering germs of a puncture = `Z`-sets; tangent rays as fibre functors | CONSISTENT | P | |
| E.11 | Refuted | limit of the sheaf topoi is degenerate | CONSISTENT | P, M | above |
| E.12 | Known | Homeo/Diff comparison for marked surfaces | CONSISTENT | S, L | |
| E.13 | Refuted | unrestricted germ assertions | CONSISTENT | S, M | |
| E.14 | Proved | 1,946 marked `B_3` quotient kernels of order ≤ 1000 | CONSISTENT | S, R | |
| E.15 | Proved | every bounded pair is a projection of a full shadow | CONSISTENT | S, R | |
| E.16 | Proved | class-two images: `(χ² − 1)/24`; 180 fake shadows; order 486 example | CONSISTENT | S, R | |
| E.17 | Proved | the published targets `N_0, N_1, N_2` | CONSISTENT | S, R | |
| F.1 | Proved | sections = `H^1_cts(G_k, U)`; Selmer schemes are subsets | CONSISTENT | S | |
| F.2 | Proved | tripod Selmer and local dimensions through class 8 | CONSISTENT | S, L | rests on the free Galois Lie algebra (Hain–Matsumoto) |
| F.3 | Known | first drops at classes 1, 2, 4 for `|S| = 0, 1, 2` | CONSISTENT | C, L | thresholds recomputed from F.2 |
| F.4 | Refuted | abelian approximations do not separate cusps | CONSISTENT | P | |
| F.5 | Proved | the `q_7` element is invisible below class 8 | CONSISTENT | S | |
| F.6 | Proved | `E_1`, `E_6`: ranks 0, 1; `a_5 = −2` | CONSISTENT | S, L | `a_5 = −2` agrees with G.10's count |
| F.7 | Proved | local dimensions 1,2,4,7,13,22,40,70 | CONSISTENT | C | cumulative `ℓ_j(2)` minus 1 |
| F.8 | Proved | refined local conditions: `r`, `r + |S|` at classes 1, 2 | CONSISTENT | S, L | |
| F.9 | Proved | all global dimensions through class 8, unconditional | CONSISTENT | S, R, L | through F.16–F.18 |
| F.10 | Proved | central extension obstruction | CONSISTENT | S | standard |
| F.11 | Proved | restriction of a section to a cover | CONSISTENT | S | |
| F.12 | Open | unrestricted Fermat section sets, higher integral metabelian quotients | OPEN | S | computed: abelian (F.4), real pro-2 metabelian (F.19), pro-5 class 2 with any ramification (F.20, F.21), classes 3–5 over `Z[1/30]` (F.22, F.23); remaining: unrestricted ramification from class 3, the Alexander module |
| F.13 | Proved | the normalizer version gives no Selmer problem by itself | CONSISTENT | S | |
| F.14 | Proved | lemmas for the point-section problem, with hypotheses | CONSISTENT | S | to LM6 Part E |
| F.15 | Proved | `H^1(G, lim P_n) → lim H^1(G, P_n)`: onto always; bijective for compact towers and rational BCH towers; fails for `Z ⊕ Z/2^n` | CONSISTENT | P | every step followed; the counterexample is `Z_2/Z = lim¹(2^n Z)` |
| F.16 | Proved | class 3 dual Selmer defect vanishes (`p = 5`) | CONSISTENT | S, R, L | see note 2 |
| F.17 | Proved | class 4 defect vanishes | CONSISTENT | S, R, L | see note 2 |
| F.18 | Proved | all defects in degrees 3–8 vanish | CONSISTENT | S, R, L | see note 2 |
| F.19 | Proved | real pro-2 metabelian section set: three classes | CONSISTENT | S, L | three components of `P¹(R) ∖ {0,1,∞}` |
| F.20 | Proved | pro-5 class-two sections over `G_{Q,S}`: tame-symbol locus | CONSISTENT | S, L | |
| F.21 | Proved | unrestricted class two: `H^2(G_Q, Z_5(2)) = C(I)/D C(I)`; a cup product zero at every finite level and non-zero integrally | CONSISTENT | P, C | complex `[C(I) → C(I)]`, cup formula at cochain level, Chebotarev; the eight primes recomputed. It is LM7 E.32 at 5 with an actual section obstruction |
| F.22 | Proved | classes 3, 4 over `Z[1/30]` | CONSISTENT | S, L | |
| F.23 | Proved | class 5 obstruction; `(κ(2), 2κ(2))` has no lift | CONSISTENT | S, R | |
| F.24 | Proved | the three unit cusp sections separate first in integral class 3 | CONSISTENT | S, L | |
| G.1 | Refuted | `D_m` is not an intrinsic Johnson map; filtered form | CONSISTENT | S | |
| G.2 | Proved | odd degrees vanish; characters need `a ≡ b mod 4` | CONSISTENT | S | used in G.6 |
| G.3 | Proved | special derivations; degree 2 is `Z_5 ad(ω)` | CONSISTENT | S | lead G(a)(1) holds |
| G.4 | Known | degree-2 coefficient is `κ_{1+i}`, onto `Z_5` on `Δ` | CONSISTENT | S, L | `κ_64/12 = κ_2/2 = κ_{1+i}` checked |
| G.5 | Proved | packet twists add their Kummer cocycle; one packet cancels | CONSISTENT | S | |
| G.6 | Refuted | of `b_+, b_0, b_−` only `b_0` survives (CM automorphism of order 4) | CONSISTENT | P | refutes the expert's lead G(c) in two of three components |
| G.7 | Known | `b_0 = κ_11/48`-type, non-zero on `Δ` | CONSISTENT | S, L | Nakamura 1995 with the 2013 erratum; 2025–2026 preprints |
| G.8 | Proved | constants of a metabelian-detected special derivation = boundary line | CONSISTENT | S | |
| G.9 | Known | unbounded family of extreme `ε` derivations at split primes | CONSISTENT | S, L | |
| G.10 | Proved | `P_ℓ^{s(Δ)} = inertia`, every prime, every packet | CONSISTENT | P, L | settles CK E3 pro-ℓ; Nakamura 1995, Tsunogai 1995 not opened |
| G.11 | Proved | the CM eigenline lifts through `N_4` and stops at `N_5` | CONSISTENT | P | `T(x) ∉ [x, L_4]`; confirms the lead G(d) |
| G.12 | Proved | open normalizer ⇒ first term is a boundary multiple in degree 2 | CONSISTENT | S, L | |
| G.13 | Proved | pro-ℓ: procyclic with open arithmetic normalizer ⇒ conjugate into inertia | CONSISTENT | S, L | LM3b D.4 for this curve, pro-ℓ |
| G.14 | Proved | special modules, characters, bracket ranks through degree 14 | CONSISTENT | S, R | |
| G.15 | Known | rational Galois dimensions 0,1,3,3,8,11,24 | CONSISTENT | S, L | a 2026 preprint |
| G.16 | Open | embedded generators beyond degree 6; the scalar `λ` in `A_8 + λB_8` | OPEN | S | reduced to one arithmetic coefficient `ν/α` of an eighth-Johnson Galois element (G.24); universal equations cannot fix it (G.23) |
| G.17 | Proved | factorization through `G_K^ab` holds at `N_1, N_2`, fails at `N_3` | CONSISTENT | S | consistent with G.4 |
| G.18 | Known | CM system symmetry (Connes–Marcolli–Ramachandran) | CONSISTENT | S, L | |
| G.19 | Proved | full profinite: one non-zero pro-ℓ image suffices | CONSISTENT | S, L | |
| G.20 | Open | full profinite fixed subgroups and undetected procyclic normalizers | OPEN | S | residual cases lie in the common kernel of all maximal pro-ℓ quotients; narrowed by G.22 |
| G.21 | Proved | the degree-6 (3,3) line | CONSISTENT | S, L | |
| G.22 | Proved | finite-cover transport criterion | CONSISTENT | S | |
| G.23 | Proved | every `A_8 + λB_8` exponentiates in the universal elliptic kernel | CONSISTENT | S, L | |
| G.24 | Proved | saturated lattice; coordinates `α, ν` | CONSISTENT | S, R | |

## Notes for the expert

1. What to read first (statement level here, and carrying much): D.21 (with D.17–D.20), E.7, B.14d, B.30,
   B.31–B.35, F.22–F.24, G.12–G.13, G.19, G.21–G.24.
2. F.16–F.18 pass from a non-zero value modulo 25 of a `p`-adic `L`-function at one specialization, through
   Kato 2004 (Theorem 17.4 (1)–(2), "divisibility away from 5"), to the vanishing of `H^1_f(Q, ·)` for the
   Tate twists of the CM symmetric powers. I could not check this passage and name no faulty step; it is the place
   in Part F where a second reader is most needed. F.9 and the thresholds 2, 3, 4 for `E_6` depend on it.
3. A.22 is true by a five-line argument (in the table). It gives 2-torsion with multiplier one in the pure
   peripheral outer automorphisms of `F̂_2/F̂_2''` that no pro-prime quotient sees. Whether the element satisfies
   the `GT` relations in the metabelian quotient is not addressed by the return.
4. G.6 refutes the expert's lead that `b_+, b_0, b_−` are all non-zero on `Δ`; G.11 shows the conclusion of the
   lead (lifts through `N_4`, stops at `N_5`) holds through `b_0` alone.
5. E.3 corrects Lead 2: `ST_{1,1}^+ = B_3` is a central extension of `SL_2(Z)` by `Z` (kernel the centre squared);
   the full `GL_2(Z)^~ = B_3 ⋊ C_2` is not central.

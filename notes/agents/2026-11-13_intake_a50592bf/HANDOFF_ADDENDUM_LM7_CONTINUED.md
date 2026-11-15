# Addendum for LM_EXPERT\KNOWLEDGE_HANDOFF.md: LM7, the continued run (section to append)

Written by Claude Fable 5.2 (Anthropic), the intake reader of the continued run (not an expert of this line),
13 Nov 2026, about 14:10–15:10 UTC (clock read 14:56 UTC). Files: `pro_intake_20261113\INTAKE_LM7_CONTINUED.md`
(verdict table, implications), `PUSH_ITEMS_LM7_CONTINUED.md`.

## What the intake is

- Return: `answers\LM7_FERMAT_TOWER_20261113T1435Z_unzipped\LM7_FERMAT_TOWER\` (zip built 13:44 UTC; INCOMPLETE;
  178 statements: 154 Proved, 9 Refuted, 12 Known, 3 Open). Against the first return: 75 new rows (D.27–D.49,
  E.37–E.62, E.64–E.89; there is no E.63), all Proved; no status changed; D.20 widened; D.13, D.19, E.23 still open.
- Read with proofs, no gap found (17): D.27, D.34, D.36, D.45, D.46, D.47, E.37–E.44, E.61, E.66, E.73.
  Statement level only (58): the rest; D.48, D.49 with the first part of the proof. No error found.
- No program was run; ten outputs were opened and agree with the text. One source opened (abstract only):
  Enriquez, arXiv math/0408035, states `GT_K = GT̂` (D.20's new claim).

## Do not take as checked

- D.28–D.33, D.35, D.37–D.44, D.48, D.49 and 41 of the 52 E rows: statements only.
- D.35 (statement level) and D.25 (first return; rests on its program) carry D.36's arithmetic graph, hence the
  claim "outside the Galois image" of D.46–D.49.
- Every "no genuine lift" statement (D.27, D.30, D.32, D.45) is about a recorded action and rests on rank
  computations of the return's programs (not rerun).
- E.37 was not compared with LM7_PUSH A.3, A.8.

## Facts to carry

- **E.23, class two, is settled by E.37**: a lift of `α ∈ H¹(Q, V)` to `N/γ_3N` exists iff the rank-44
  corrections are integral at every prime and tend to zero; fibres `ℛ(Z_3) ⊕ Z_3^24 ⊕ (Z/3)^9 ⊕ (Z/9)^5`.
  E.44 is the same criterion at every layer `r ≥ 3` for `N`, `N/N″`, `N/γ_3I_Q`, with the genuine higher Frobenius
  words left as input.
- **Selection starts in a metabelian quotient of the tripod group.** In `F/[I_y, I_y] = Z_3[[U]] ⋊ Z_3` a local
  section with inertia `c ≠ 0` in the `y`-direction and Frobenius `x`-coordinate `b` exists iff
  `b/(q − 1) ∈ Z_3`; the inertia is then `cT^{−b/(q−1)}` (E.42). E.38, E.43: the classes
  `α_P + 3^kκ_3(p)e_Q` (`p ≡ 1` mod 9, 2 a non-cube; density 1/9) have class-two sections and none higher.
- **E.61**: at `v ∤ 3` the ramified local sections of the full pro-3 group are the nine cusp families; proof by
  the weight argument on the Jacobian of a cover over the residue field. E.66 (read): the same for `N/N″`, with
  one full lift; E.71: the marked quotient (statement level). E.41 (read): all sections unramified outside 3,
  `∏_i 𝒞_i(W)`. E.73 (read): global sections are local packets coupled by Frobenius words.
- **D.19 (ii)**: the candidate is "the Galois commutator `h` on the 2-part, the identity on the odd parts", pair
  `(T_4, W_3) = (I, [i])`. It exists on the relative pronilpotent completion over `Q` (D.46), on all Fermat levels
  and on `F̂/F̂″` (D.47), over the maximal `h`-fixed base (D.49). Quotients that are fibre products of pro-`p`
  groups over an `h`-fixed base cannot decide the coset. First deciding places named by the return:
  `J_{3,2} = B̂/(K_3′K_3²)` and the `S_7`-marking of (D.46.9).
- **D.13**: untouched by the continued run. All 23 new D rows are about the CM coset.
- **D.20**: for all of `GT̂`, `φ_n(f) = y^{c_n(f)}f` and `c_{mn} = c_m + c_n` (Enriquez).

## This intake's own arguments (unchecked; leads for the successor prompt)

1. `F̂/F̂″` splits off the pro-ℓ metabelian group by the idempotent `e_0` of `Z_ℓ[[Ẑ²]]`; every special
   automorphism of the pro-ℓ metabelian group extends to `F̂/F̂″`. So the metabelian profinite images in weights
   5 and 9 are 3 and 2, and D.13 is purely a question of lifting from `F̂/F̂″` to `F̂` (hunch H4 with a proof
   sketch).
2. PS-3 is false as worded: cuspidal sections twisted by a class of `H¹(Q, Z_3(1))` with infinitely many
   non-zero valuations lift to `N` and are ramified at infinitely many primes. It needs "non-cuspidal".
3. PS-5 as worded fails on the relative pro-2 completion over `Q_0 = S_3 × C_3`: an element trivial at 3 commutes
   with the deck element of `w³ = z(z − 1)` and acts `Z_2[ζ_3]`-linearly on `T_2`; complex conjugation acts
   antilinearly. On the pure pro-2 completion of `F` nothing is excluded.
4. PS-4 (c) is not supported: D.45's obstruction belongs to one lower action; D.46 passes the bases `S_4`,
   `A_4 × C_2`.
5. The additive distribution relation of D.20 holds for the D.47 element; it does not separate `GT̂` from it.

## Next

- Second reader, in order: E.37 against LM7_PUSH A.3, A.8; rerun the D.27 and D.45 programs; D.35 with its
  proof; the five arguments above; D.48, D.49 to the end.
- LM8_PUSH (unsent): update R14 and task C.7 with D.47–D.49; task B.1 must account for D.47 and argument 1; Part D
  can take E.38, E.42, E.44, E.61, E.73 as its model (the tripod formulas transfer to `ℓ = 5`). Details:
  `INTAKE_LM7_CONTINUED.md`, 4.5.
- The run may still be going: a later zip needs the same row diff (scripts named in the intake's header).
- Not done: the PDF check of the 13:44 UTC paper.

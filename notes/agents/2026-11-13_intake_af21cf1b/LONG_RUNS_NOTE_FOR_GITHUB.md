# Three long runs on §§12–31 and §§51–53 of *La Longue Marche* (13 November 2026)

Three development prompts on Grothendieck's *La Longue Marche à travers la théorie de Galois* (1981) were run on
12–13 November 2026 by GPT-6 Astra (ChatGPT Pro mode). Each return is a paper with its LaTeX, a register of numbered
statements (`*_results.csv`: Proved, Refuted, Known, Open), code with outputs, and the prompt as sent. The statements
are AI-produced claims. What has been read by a second model is said at the end. This note was written by
Claude Fable 5.2 at effort high.

## LM7_FERMAT_TOWER (§51): 220 statements; 196 proved, 9 refuted, 12 known, 3 open

- §51 answered. The level 12 and the order 32 explained (A.3); three formulas of the manuscript corrected (A.6, A.9,
  A.13); `F'/F''` free of rank one over `Z[Z²]`, and profinitely over `Ẑ[[Ẑ²]]` (B.4, B.8); the freeness he struck
  out is false (B.3); the splitting of scan 136 holds (B.11–B.13); the Kummer maps, their images and independence
  (D.1–D.4).
- Sections of the Fermat cubic minus its flexes, pro-3: the class-two section map with every fibre (E.37); a
  lifting criterion at every layer (E.44); an obstruction that vanishes at every finite level and not continuously
  (E.32); all sections unramified outside 3 (E.41); ramified local sections away from 3 are cuspidal (E.61, E.66).
- The Fermat quartic has no section over `Q` (E.18). Its class-two images at 3 and 5 (E.115, E.117); a class tied to
  the Ceresa cycle (E.109).
- Open: D.13 (the image of the full profinite loop-preserving group in weights 5 and 9), D.19 (does the full
  `GT_0` reach the CM coset that Galois misses; D.46–D.49 give a candidate), E.23 (all sections of the metabelian
  and marked quotients; open from class three).
- E.102 (a degree-four kernel `Z_3^504 ⊕ C_3^144 ⊕ C_9^56 ⊕ C_27^30 ⊕ C_81^9`) was recomputed independently by
  Claude Opus 5.5 at effort max, and Claude Fable 5.2 at effort max found a closed formula for it, which also
  reproduces the groups of E.34, E.37 and E.40.

## LM4_FINITE_GROUP_ACTIONS (§§12–18, 23–25 bis, 31): 264 statements; 233 proved, 25 refuted, 3 known, 3 open

- His conjectured equivalence of 2-categories holds, in a corrected form, for finite groups on hyperbolic surfaces
  (C.1, C.8), and fails for infinite groups at levels one and two (C.11).
- Sections are fixed points, and ovals for reflections (B.3–B.5); the "lemme fondamental" of §18 holds (B.6); six
  statements of §§15–33 are refuted with their true form (B.7, B.8, B.10, B.11, B.15, B.20).
- A census of the finite subgroups of the extended mapping class groups for `2g + ν ≤ 6` and parts of genus three
  (B.23–B.41), with section counts.
- Completion keeps finite subgroups and lifts (D.2, D.3). A torsion-free finite extension is again a surface pair
  in the pro-`p` case (D.18–D.20) and not in the full profinite case (D.29, D.30). In the full profinite group of
  type (0,3) every finite-order element has a global multiplier `±1` (D.34, D.42), and so has every element of
  2-power order in type (1,1) (D.43, D.70).
- Open: C.12 (level zero for an infinite operator group; settled for cocompact discrete groups, C.90, C.91), D.12
  (is every torsion element of the full `GT_0` conjugate to complex conjugation), F.7 (the centralizer of a
  geometric `A_5` in the completed mapping class group; the return could not verify one step of the cited proofs and
  claims no counterexample).

## LM8_LIE_APPROXIMATIONS (§§52–53): 167 statements; 122 proved, 24 refuted, 15 known, 6 open

- The run ended without a final answer; checkpoint 16 is its last state.
- One-parameter subgroups through a positive power exist over every quasi-compact quasi-separated base (D.21) and
  not over every quasi-compact base (D.14). `M_{1,1}` over `Z` is not a quotient of a curve by a finite group
  (C.6). Lifts of special derivations exist at every prime (B.11, B.14d). `ST_{1,1} ≅ B_3 ⋊ C_2` (E.3).
- Sections of an inverse limit against the limit of sections (F.15, F.21). On the once-punctured CM curve the fixed
  points of the Galois image are the inertia group (G.10).
- Open: A.12, B.24d, B.28, F.12, G.16, G.20.

## What has been checked

LM7: the first 103 statements were reviewed by Claude Fable 5.2 at effort max (none found wrong; programs not
rerun), and 17 later proofs were read by Claude Fable 5.2 at effort high. LM8: 32 proofs read or recomputed by
Claude Fable 5.2 at effort high, none found wrong. LM4: statements read, no proof reviewed yet. The other statements
stand as the returns give them.

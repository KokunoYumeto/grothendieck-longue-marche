
## 4. LM8: the intake, folded in (written by Claude Fable 5.2, effort max, agent a125034fd35557818, 13 Nov 2026, 14:10 UTC, clock read)

Source: `C:\Users\user\Documents\pro_intake_20261113\HANDOFF_ADDENDUM_LM.md`, written by the intake agent (Claude Fable 5.2, effort high; not an expert of this line; 13 Nov, 13:22–13:49 local time). Reworded here; where this agent re-read something itself, the line says so.

### 4.1 What the intake is

- The return: `answers\LM8_LIE_APPROXIMATIONS_checkpoint_16_20261113T1145Z_unzipped\LM8_LIE_APPROXIMATIONS\` (GPT-6 Astra, ChatGPT Pro mode). The run stopped; checkpoint 16 is its last state; marked INCOMPLETE. 167 statements: 122 Proved, 24 Refuted, 15 Known, 6 Open.
- The intake (`pro_intake_20261113\INTAKE_LM8.md`) gives every row an outcome and a basis code. Result: 161 consistent, 6 open (A.12, B.24d, B.28, F.12, G.16, G.20), none doubtful, none wrong. Only 32 of the 161 were checked with their proofs (read, re-derived or recomputed); 129 are statement-level verdicts, which say that a statement is well formed and agrees with its neighbours, not that its proof holds.
- From the intake the prompts LM6 and LM5 were updated (`PROMPT_IMPACT.md`); LM4 and LM7_PUSH were left alone. `IMPLICATIONS.md` reads LM8 together with TOTAL_EXACT_2 (candidates P1–P5); `PUSH_ITEMS.md` ranks what a follow-up must settle.

### 4.2 What nobody has checked (do not take these as checked)

- About 110 KB of the 900 KB of TeX was read by the intake. Statement level only: Part D except D.4, D.10, D.14, D.23 (so the main result D.21 is unread); Part C except C.6; Part A except A.2, A.7, A.22; B.14a–d and B.20–B.35 except B.32, B.34; E.1–E.3, E.6–E.9, E.12–E.17; F.1–F.3, F.5–F.14, F.16–F.20, F.22–F.24; Part G except G.6, G.10, G.11.
- No program of the return was opened or rerun; no cited source was opened. Several sources are 2025–2026 preprints; this agent confirmed on arXiv that these exist with the titles the return gives: Ishii 2312.04175, Ishii–Goto 2412.18846, Ishii 2602.00615, Goto–Ishii 2610.21052, Lochak–Nakamura–Schneps 2602.12462, Malkin 2010.07238 (TeX fetched; content not read).
- The manuscript side of the thirteen correction rows (A.2, A.7, A.15, B.24, D.3, D.4, D.10, D.14, D.23, E.4, E.5, E.11, E.13): checked as mathematics only. Exception since this session: E.11 against scans 242–243 (5.3 below).
- F.16–F.18 (vanishing of the dual Selmer defects for `E_1`, `E_6` at 5 through Kato's Theorem 17.4): the intake could not follow the passage from a value modulo 25 to `H¹_f = 0`. F.9 and the thresholds 2, 3, 4 for `E_6` hang on it.
- Checkpoint 16 has no PDF; the PDF check (overfull boxes, rendered pages) is not done.

### 4.3 Facts to carry

- **F.21 = LM7 E.32 at the prime 5, with a section.** `H²_cts(G_Q, Z_5(2))` is families tending to zero modulo the image of `diag(5^{v_5(q−1)})`, no closure; the pair `(κ(5), Σ 5^n κ(q_n))` lifts to every finite Heisenberg quotient and to no integral class-two section. The intake recomputed the eight primes.
- **F.15** is the criterion for "sections at every level give a section": always onto; bijective for compact towers and rational unipotent towers; false for `Z ⊕ Z/2^n`.
- **E.11.** The 2-limit of the sheaf topoi of shrinking punctured discs is the degenerate topos; the covering germ is `BZ` (E.10). Proof re-read by this agent: correct (the outer annuli pull back to zero and cover).
- **A.22.** `F̂_2/F̂_2''` has a non-inner involution of multiplier one that preserves the three peripheral classes and acts on the Alexander module by `1 − 2e`, `e` the idempotent of a `Z_5[ζ_3]`-component; it is invisible in every pro-prime quotient. A.23–A.26 lift it through the relative pro-5 completion of the index-3 kernel. Re-derived by this agent; more in 5.3.
- **The LM7 reviewer's results are proved in LM8**: special derivations lift at every prime (B.11); pro-ℓ `GT_0 ⊋ GT` for every ℓ (B.12, B.14d); the tables (tripod special 0,0,1,0,3,0,6,4,13,12; (0,4): 2,1,6,6,28,36, normalizer quotient 0,0,1,0,1,0, B.16); filling (0,4) → (0,3) is exact on the normalizer with image `GT × S_3`, not onto `GT_0 × S_3` (B.17); at (1,1) the normalizer quotient is in degrees 6 and 10 (B.18, B.19).
- **Part G.** G.6 refutes the lead "`b_+, b_0, b_−` all non-zero on Δ": only `b_0`. G.10 settles CK E3 in every pro-ℓ quotient (fixed points of `s(Δ)` are inertia). G.11 confirms "lifts through `N_4`, stops at `N_5`". G.13 is LM3b D.4 for this curve, pro-ℓ. Full profinite: G.19 (if one prime sees the subgroup), G.20 open.
- **Lead 2 of the LM8 prompt, corrected** (E.2, E.3, E.5): `ST_{1,1}^+ = B_3`, central over `SL_2(Z)` with kernel the square of the centre; `GL_2(Z)^~ = B_3 ⋊ C_2` is not central; the extension of the 140-1 draft is class 1 of `Z/12` with his sign.
- **§52.3 is not a nilpotent tower** (B.1–B.3): his "approximation de Lie" is an adelic representation into a `Q`-group of finite type with diagonal rationality on the discrete geometric group.
- With TOTAL_EXACT_2: all limits in LM8 are over directed sets, so only the coefficients decide (F.15); a limit over the Teichmüller tower itself would be over a non-filtered index (candidate P3 of `IMPLICATIONS.md`, low confidence; not taken into LM8_PUSH).

### 4.4 The intake's next steps, and where they stand

1. Intake of LM7_PUSH and LM4 when they end: comes to this expert. LM7_PUSH Part F meets F.15 and F.21.
2. The push prompt for LM8: written (section 5). Scans 242–243 are read (5.3).
3. The manuscript side of the correction rows, for an expert with cotes 140-4, 140-1, 140-3 open: not done; not a Pro item.
4. Build the LM8 paper and run the PDF check: not done.

## 5. LM8_PUSH (same agent; 13 Nov 2026, 13:23–14:15 UTC, clock read at both ends; stopped once by mistake and resumed)

### 5.1 What was done

- Read in: this file, the four intake files, the LM7 review and its `PUSH_ITEMS.md`, the template `claude_tools\prompt_lessons_20261112\PROMPT_TEMPLATE_PUSH.md`, the LM7_PUSH prompt. Of LM8: the register rows of the six open items and of the rows they rest on (A.11–A.26, B.12–B.35, E.10–E.13, F.2–F.24, G.7–G.24); in full with proofs G.10–G.13, G.19, G.20, G.22, E.10, E.11; the statements of A.19, A.21, A.22, B.25, B.28, F.16–F.18, G.16, B.24d. Of LM2: E.1–E.4 in full, the rows B.m2, B.m3, C.d4, C.d5. The manuscript: cote 140-4 scans 242–243, transcription and scan images.
- Written: `pro_prompts_draft_20261111\LM8_PUSH\PROMPT.md` (48 KB; `push_rule_pro_prompts.py --lint-math`: failing lint 0; closing paragraph, typesetting check, checkpoints present) and `LM8_PUSH_background.zip` (1,788,805 bytes, 215 entries, no PDF). Work folder `pro_prompts_draft_20261111_work\LM8_PUSH\`: `build_zip_20261113.py`, `MANIFEST.tsv`, `fetch_arxiv_20261113.py`, `arxiv_lookup_20261113.py`, `check_leads_20261113.py` and `.out`, `shelf_and_tally_20261113.py`, `CONSULT_FOR_LM7_REVIEWER.md` (five questions for the previous expert; the main session passes them on).
- Records: 68 source files entered in `Free or receipted\free\CLAUDE_FREE_SHELF.json` (backup beside it); LM8_PUSH is in `claude_tools\maths_prompt_tally.py` as READY (backup beside it). Thirteen arXiv e-prints fetched into `Free or receipted\free\arxiv-eprints-lm-20261113\` (1710.05532, 1512.03975, 1003.1012, 1504.04737, 2610.21052, 2602.00615, 2602.12462, 2010.07238, 1410.1045, math_0003113, math_0610163, 2312.04175, 2412.18846), each checked by its title line.
- The user sends Pro prompts. Not sent.

### 5.2 What the prompt asks (Parts; R1–R21 settled material; Leads 1–15)

A. LM8 G.20, the main question: `π^{s_b(Δ)} = I` and "procyclic with open arithmetic normalizer ⇒ in a conjugate of `I`" for the full profinite group of `y² = x³ − x` minus the origin over `Q(i)`; the structure `Fix = Θ ⋊ I`; the abelian layer on every cover; the first covers (three `𝔖₃`-covers, the two covers of order 8); the pro-ℓ statement on every cover; the sections that agree on Δ.
B. LM8 A.12 on the tripod: all finite-order elements in the metabelian pure peripheral group; which pass the metabelian 2-cycle, 3-cycle and pentagon tests; is `𝒫₁` torsion-free (lift the involution of A.22 or find the finite obstruction); torsion with λ = 1 in `GT̂₀`, `GT̂`; multiplier −1 and other multipliers.
C. LM8 B.28: §47 as the fixed points of an endomorphism `D` of `GT̂₀`; comparison with Nakamura–Tsunogai and Nakamura–Schneps (III′); `GT̂ ⊆ C^φ`; `C^φ = GT̂₀`; the pairs `(F^(ℓ), D(F)^(ℓ))`; level four and beyond; the CM coordinates.
D. LM8 F.12: `H^i_cts(G_Q, Z_5(j))`, j = 3, 4, 5, with lim¹; `Sec(T_3)`, `Sec(T_4)`, `Sec(T_5)` with unrestricted ramification; the metabelian quotient; the Fermat kernels.
E. LM8 F.16–F.18 by Rubin's theorem and the two-variable `p`-adic `L`-function (24 characters), the certificates recomputed, the passage through Kato's theorem checked step by step.
F. LM8 E.11: the limit of the sheaf topoi of a germ (sublocale `⋂ S_i`), the germs for which his parenthesis holds, the coherent (étale, henselian) theorem, Leroy's thesis.
G. LM8 G.16: λ, the lattice, the embedded image in degrees 8–14.
H. LM8 B.24d: images and kernels above the first Fermat stage; the additive-polynomial lifts.

### 5.3 Found while drafting (this agent's; status on each line; also in FINDINGS.md, F28–F33)

- **Scans 242–243 read on the images** (`LM_C4-229-247\LM_C4-229-247_scan242.jpg`, `_scan243.jpg`). The text is about a topological space with a filter and the projective limit of the "(petits) topos étales" of the members: the topological reading. So E.11 refutes what he wrote, for residual germs; he hedged twice (both hedges are insertions). **The marginal note on scan 243 reads, as far as this agent can see, "cela est fait par Olivier Leroy ?"**; the first-pass transcription (`answers\unzipped\LM_C4-229-247\`, line 758) has "cela ne fait pas aller loin ?" marked unsure. A reading point for the editors; Leroy's thesis (fundamental groupoid of a topos, Montpellier 1979) is the source to open. One reader, enlarged crop; not confirmed by a second.
- **§47 as a fixed-point condition** (Lead 8; derived here, not checked): every pure peripheral outer automorphism of `F̂_2` descends along `φ : F̂_2 → C_2 ∗̂ C_3`, and every element of `GT̂_0` extends from the level-two subgroup; the descent restricted to the level-two subgroup is an endomorphism `D` of `GT̂_0` (restrict to the `𝔖₃`-cover of the `j`-tripod, a sphere minus eight points, and fill five), and `C^φ = Fix(D)`. With the 2-cycle relation, `F(σ_1σ_2σ_1) = f^{-1}(σ_1σ_2σ_1)^λ`, so §47 says: `f` is the `Int(s)`-coboundary of its own image `f(s, sr)`.
- **The metabelian relations of `GT̂` do not exclude multiplier-one torsion** (Leads 5–7; checked on characters by `check_leads_20261113.py`). The beta function `1 − 2e_0` of A.22 is `𝔖₃`-invariant and fails the cocycle identity `β(X,Y)β(XY,W) = β(Y,W)β(X,YW)`. But for any inversion-invariant idempotent `e_1` of `Ẑ[[Ẑ]]` vanishing at the trivial characters, `g = 1 − 2e_1` gives `β_g = g(X)g(Y)g(Z)`: an order-two unit, `𝔖₃`-invariant, a coboundary, defining a non-inner pure peripheral involution of multiplier one of the free profinite metabelian group. Whether the cocycle identity is exactly the metabelian shadow of the pentagon (Ihara's Γ-factorization) is from memory, source not opened.
- **The first cover for G.20** (Lead 3; by hand, unchecked): the `[i]`-stable `𝔖₃`-cover of `E ∖ O` is `v² = w⁷ − w`, genus 3, two cusps at Weierstrass points, Jacobian isogenous to `E³`. An open subgroup of Δ fixes its whole `H_1`; the abelian layer excludes nothing there. In general (Lead 2) the Δ-fixed part of `H_1` of a cover is the boundary plus the `E`-isotypic part orthogonal to the non-torsion cuspidal classes (Ribet's Kummer theory over `K(E_tors) = K^ab`).
- **`H¹_cts(G_Q, Z_5(3)) = Z_5` and `H²_cts(G_Q, Z_5(3))` has a lim¹ part** (Lead 12; by the proof of F.21 with `q² − 1`; not written out).
- **The limit topos** (Lead 14): the 2-limit of the `Sh(S_i)` is sheaves on the sublocale `⋂ S_i`; the point for the germ at a point of a regular space, empty for a residual germ of a Hausdorff space. His "good cases" hold for germs around points, not for the residual germs he goes on to use.

### 5.4 Not covered; to do before sending

- R10–R13, R17, R20, R21 of the prompt are statement-level (the prompt says so). LM2 was not reviewed by this line.
- Sources named from memory in the prompt (Ihara's beta and gamma papers, Nakamura–Tsunogai and sequels, Ribet 1979, Leroy 1979, Moerdijk 1989): bibliographic data unverified; the prompt says "check each citation".
- The answers to `CONSULT_FOR_LM7_REVIEWER.md` may change Lead 11, task C.5, Lead 12 and the wording of the full-profinite tasks.
- The zip attaches the first LM7 return (02:27 UTC). LM7 kept working (a later state is in `answers\LM7_FERMAT_TOWER_20261113T1314Z_unzipped`); if its final state changes D.15–D.17, D.25, D.26 or E.32, rebuild the zip.

### 5.5 Overlaps with the runs still going (LM4, LM7, LM7_PUSH)

- **LM4_FINITE_GROUP_ACTIONS ↔ Part B.** LM8 A.12 for general surfaces and finite groups is LM4's subject (the LM8 return notes "LM4 not supplied"). Part B is restricted to the tripod and says so. When LM4 returns: check whether it proves or refutes profinite realization in a form that decides B.3, and whether it treats multiplier-one torsion.
- **LM7_PUSH Parts D, E ↔ Part C.** LM7_PUSH D.1, D.2 (images of `Out^♯(F̂_2)` and `GT̂_0` in pro-ℓ weights 5 and 9) and E.2, E.3 (the CM coset) were open at its checkpoint 04 (tally entry). C.5 (pairs `(F^(ℓ), D(F)^(ℓ))`), C.7 and Lead 11 (the CM coordinates on `C^φ`) are the same kind of full-profinite separation; an answer to LM7_PUSH E.2 bears directly on C.4 through Lead 11.
- **LM7_PUSH Part F ↔ Part D.** LM7_PUSH F.1 asks for the general theorem (residue complex, lim¹, Mittag-Leffler) for any lattice; D.1 and Lead 12 are its cases `Z_5(3)`, `Z_5(4)`, `Z_5(5)`. If LM7_PUSH F.1 comes back proved, D.1 becomes an R-item and D.2–D.4 start from it.
- **LM7_PUSH Parts A–C ↔ Part D.** Both compute section sets beyond class two with unrestricted ramification (the Fermat cubic at 3 there; the tripod at 5 here); the methods should agree (tame condition plus convergence condition).
- **LM6 Part A (e)** now asks the G.20 question (intake); Part A of LM8_PUSH is the full treatment. If both are sent, the returns must be compared.
- **LM7 (still running).** Its later states may add to D.13, D.19; nothing in LM8_PUSH depends on more than the first return.

### 5.6 Working facts

- Own context: `python -I -B work\ctx3.py` (transcript of agent a125034fd35557818; a successor changes the path). At the end of this task: about 47 % of 1M.
- The scans are on disk per package: `longue_marche_pro_pilot_20261104\LM_<KEY>\LM_<KEY>_scanNNN.jpg` (about 0.5 MB each; an image costs a few thousand tokens; crop with PIL for margins).
- Register rows are read cheaply with a small script that prints chosen ids of a results CSV to a file (the returns' CSV columns: id, statement, status, where_proved, depends_on, manuscript passages, notes).
- The returns' bibliographies carry arXiv ids and "verified" notes: grep them before searching.
- Thinking stays in the context during a tool loop: this task went from 25 % to 45 % of the window with about 100 KB of reading.

### 5.7 Next, in order

1. Pass `CONSULT_FOR_LM7_REVIEWER.md` to the previous expert; apply the answers to the prompt; lint again; rebuild the zip if files change.
2. Intake of LM4, LM7 (final state) and LM7_PUSH when they end; fold LM7_PUSH F.1 and E.2 into LM8_PUSH if it has not been sent, or into the reading of its return if it has.
3. Not started: the manuscript side of the correction rows of LM8 (needs cote 140-4 read in full, still unread in this line except scans 242–243); the read of D.21; the LM8 paper build and PDF check.

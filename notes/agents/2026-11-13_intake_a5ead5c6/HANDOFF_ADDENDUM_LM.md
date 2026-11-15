# Addendum to the Longue Marche expert's handoff: intake of LM8 (13 Nov 2026)

## 4. LM8 section by Claude Fable 5.2, effort high (intake agent, not the expert; launched 13 Nov 2026; work done 13:22–13:49 local, clock read at the start and at the end)

The handoff file itself was not edited.

### 4.1 What was done

- Intake of `answers\LM8_LIE_APPROXIMATIONS_checkpoint_16_20261113T1145Z_unzipped\LM8_LIE_APPROXIMATIONS\` (GPT-6
  Astra, ChatGPT Pro mode; INCOMPLETE, the run stopped; 167 statements: 122 Proved, 24 Refuted, 15 Known, 6 Open).
  Output: `C:\Users\user\Documents\pro_intake_20261113\INTAKE_LM8.md`.
- Result: CONSISTENT 161, OPEN 6 (A.12, B.24d, B.28, F.12, G.16, G.20), DOUBT 0, WRONG 0. Of the 161, 32 with the
  proof read, re-derived or recomputed; 129 at statement level only.
- LM6 and LM5 were updated from it (see `PROMPT_IMPACT.md`); LM4 and LM7_PUSH were not touched.

### 4.2 What the intake does not cover (a successor must not take these as checked)

- About 110 KB of 900 KB of TeX was read. Statement level only: all of Part D except D.4, D.10, D.14, D.23; Part C
  except C.6; Part A except A.2, A.7, A.22; B.14a–d, B.20–B.35 except B.32, B.34; E.1–E.3, E.6–E.9, E.12–E.17;
  F.1–F.3, F.5–F.14, F.16–F.20, F.22–F.24; all of G except G.6, G.10, G.11.
- No program was opened; no source; the manuscript and its scans were not opened. Cote 140-4 is still unread in
  this expert line, so every correction to the manuscript (list in the intake) is checked as mathematics only.
- F.16–F.18 (vanishing of the dual Selmer defects through Kato's theorem) could not be judged: intake note 2.
- Checkpoint 16 has no PDF; the PDF check has not been done.

### 4.3 Facts worth carrying

- **F.21 is E.32 at the prime 5 with an actual section.** `H²_cts(G_Q, Z_5(2)) = 𝒞(I)/D𝒞(I)`,
  `D = diag(5^{v_5(q−1)})`; the pair `(κ(5), Σ 5^n κ(q_n))` lifts to every finite Heisenberg quotient and to no
  integral class-two section. The eight primes 11, 101, 751, 13751, 37501, 62501, 937501, 9375001 were rechecked.
- **F.15** is the criterion for "sections of all levels give a section": onto always; bijective for compact
  towers and rational unipotent towers; false for `Z ⊕ Z/2^n` (`H¹ = Z_2/Z`).
- **E.11**: the limit of the sheaf topoi of shrinking punctured discs is empty; the covering germ is `BZ` (E.10).
  Intake's remark: this refutes the topological reading; for étale topoi of henselian neighbourhoods (coherent)
  the limit is expected to be right. Which reading scans 242–243 have is unchecked.
- **A.22** (re-derived in five lines): `F̂_2/F̂_2''` has a non-inner involution of multiplier one preserving the
  three peripheral classes, acting by `1 − 2e` on the Alexander module (`e` the idempotent of a `Z_5[ζ_3]`
  component); invisible in every pro-prime quotient. A.23–A.26 lift it through relative pro-5 quotients. This
  bears on target (vi) of section 2.2 (torsion in `GT_0`, `GT`).
- **The reviewer's results are proved**: special derivations lift (B.11, every prime); pro-ℓ `GT_0 ⊋ GT` for
  ℓ ≥ 5 (B.12) and at 2, 3 (B.14d); the tables: tripod special 0,0,1,0,3,0,6,4,13,12 (formula recomputed here),
  (0,4): 2,1,6,6,28,36 with normalizer quotient 0,0,1,0,1,0 (B.16); filling is exact on the normalizer with image
  `GT × S_3` and not onto `GT_0 × S_3` (B.17); at (1,1) the normalizer quotient sits in degrees 6, 10 (B.18, B.19).
- **Part G**: G.6 refutes the lead "`b_+, b_0, b_−` all non-zero" (only `b_0`); G.10 decides CK E3 in every pro-ℓ
  quotient; G.11 confirms "lifts through `N_4`, stops at `N_5`"; G.13 is LM3b D.4 pro-ℓ for the CM curve; the full
  profinite case is G.19 (partial) and G.20 (open).
- **Lead 2 corrected** (E.2, E.3, E.5): `ST_{1,1}^+ = B_3`, kernel over `SL_2(Z)` the square of the centre;
  `GL_2(Z)^~ = B_3 ⋊ C_2` is not central; the 140-1 draft's extension is class 1 in `Z/12` with his sign.
- **§52.3 is not a nilpotent tower** (B.1–B.3): his Lie approximation is an adelic representation into a
  finite-type `Q`-group with diagonal rationality on the discrete geometric group.
- With TOTAL_EXACT_2 (see `IMPLICATIONS.md`): every limit in LM8 is over a directed set, so only the coefficients
  decide (F.15); a limit over the Teichmüller tower itself is over a non-filtered index, where the conditions of
  TOTAL_EXACT_2 (quasi-filtered, total, exact) are the relevant ones (candidate P3, low confidence).

### 4.4 Next steps

1. When LM7_PUSH and LM4 end: their intake comes to the same agent; LM7_PUSH Part F meets F.15, F.21.
2. The push prompt for LM8: `PUSH_ITEMS.md`, Longue Marche 1–9. Before sending: read cote 140-4 scans 242–243
   for item 6, and decide with the user whether item 7 (manuscript side) is done by the expert.
3. Build the LM8 paper and run the PDF check.

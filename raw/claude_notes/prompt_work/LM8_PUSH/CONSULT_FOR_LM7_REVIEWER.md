# Consultation for the LM7 reviewer (previous Longue Marche expert) on the draft LM8_PUSH

From: the Longue Marche expert for LM8_PUSH (Claude Fable 5.2, effort max), 13 Nov 2026, 14:10 UTC (clock read).
Draft: `<local>/Documents\longue_marche_pro_pilot_20261104\pro_prompts_draft_20261111\LM8_PUSH\PROMPT.md`
(Parts A–H, Leads 1–18, R1–R23; lint passes). Short answers are enough; no reading work is asked of you. Answer from
what you already know of LM7, LM7_PUSH and CYCLOTOMIC_KERNEL.

Taken from your `BUILD_ON_20261113.md` since these questions were first written: H1 is Lead 16 and task D.7 (at the prime 5); H2 is in task C.7 (is `(T, W)` a homomorphism) and R14 now records LM7 D.27, D.46 and LM7_PUSH E.9, E.10; H4 is in task B.1; LM4 D.29, D.30, D.63–D.65 are R22. Your question on LM8 A.22: its beta function is `𝔖₃`-invariant (checked on characters; Lead 5). LM7_PUSH F.1 is R23, so question 3 is now only: does F.1 give Lead 12 for `Z₅(3)`, `Z₅(4)`, `Z₅(5)` as stated?

1. **Lead 11 and task C.7 (the CM coordinates).** In LM7 D.15–D.17, where does the index-two condition on Galois in
   the coordinates `(T, W)` come from (equality of the two restrictions to `Q(i, ∜3)`)? Is it visibly a consequence of
   functoriality for the open immersion of the `j`-line minus three points into the orbifold `j`-line, that is, of
   the §47 compatibility, or does it come from the determinant and the two CM fields alone? In the second case
   Lead 11 is aimed wrong and C.7 has to be restated.

2. **C.5 against LM7_PUSH D.1, D.2, E.2, E.3.** C.5 asks for the set of pairs `(F^(ℓ), D(F)^(ℓ))`, `F ∈ GT̂₀`, where
   `D` is "restrict to the `𝔖₃`-covering of the `j`-tripod and fill five punctures". In your reading, is this a new
   question, or does it stand or fall with LM7_PUSH D.1, D.2 (the images of `Out^♯(F̂₂)` and `GT̂₀` in weights 5 and 9),
   which were still open at checkpoint 04? Should C.5 name them as items it uses?

3. **Lead 12 and task D.1 against LM7_PUSH F.1.** From your proof that LM7 E.32 is a lim¹ class: does the argument
   go through as written for `Z₅(3)`, `Z₅(4)`, `Z₅(5)`, where `H¹(Z[1/5], Z₅(3)) ≠ 0` and `H⁰(Q, Q₅/Z₅(4)) = Z/5`?
   Is "`H²_cts(G_Q, Z₅(3)) = c₀/diag(q²−1)c₀`, with the image and no closure" right as a lead, or does a term from
   `RΓ(Z[1/5], ·)` have to be added?

4. **Part A (LM8 G.20).** The obstacle is that `Δ = Gal(K̄/K^ab)` fixes the Tate module of every factor of a Jacobian
   isogenous to `E`, so the "tori against abelian varieties" step of Stix and of CK A6, A7 fails. From CK and from the
   sources you opened for LM7_PUSH (Borne–Emsalem–Stix, Stix, Esnault–Hai): do you know a statement that handles a
   base field of this kind, which the prompt should name as a result or a lead?

5. **Wording, from the LM7_PUSH run.** At checkpoint 04 LM7_PUSH had Parts A, B, C, F complete and D.1, D.2, E.2, E.3
   open, all four statements about the full profinite groups. Did the wording of its Parts D and E ("one finite `K`
   decides", "continue until a `K` removes all twelve shadows") lead the run into a search without end? Parts A, B.3,
   C.3, C.4 of LM8_PUSH are of the same kind. Should they be worded differently, and should the eight Parts go out as
   one prompt or as two (A–C full profinite; D–H)?

# Knowledge handoff: La Longue Marche development prompts

For a successor who continues the Pro-mode prompt work on *La Longue Marche*. Written by Claude (Fable 5.2), 12 November 2026 (local date; 11 November 23:50 UTC). The Dérivateurs side is in `C:\Users\user\Documents\derivateurs_companion_20261109\pro_reviews_20261110\KNOWLEDGE_HANDOFF.md`; its method for reviewing a Pro return applies here unchanged (read the register, the report and the sections; never run the return's code; write your own checks in `checks_author\`; a verdict per statement; say plainly what is false; list what is not verified).

## Files that carry the state

- Prompts: upload folders in `..\pro_prompts_draft_20261111\<name>\` (only `PROMPT.md` and the zip); everything else here, per prompt. `..\pro_prompts_draft_20261111\README.md` has the history; `_COMMON_BLOCK.md` there is the shared second half (rules 1–11).
- LM4–LM8 are **generated**: `push_rewrite_20261111.py` rebuilds each `PROMPT.md` from `PROMPT_before_push_20261111.md` plus the texts in the script, `followups_block.py` (Dérivateurs follow-ups L1–L6), `after_lm2_block.py` ("After LM2"), `outcome_block.py` ("What the outcome must be"; someone added a clause 5 on disconnects on 11 Nov) and the current common block. Edit the scripts, not the prompts, or the next run drops the edit. The script also rewrites `PUSH_REWRITE_RECORD_20261111.md`; the LM1/LM2 section of the record lives in `RECORD_LM12_SECTION.md` for that reason.
- `lm12_push_20261111.py` built LM1 and LM2 and their zips. **Do not rerun it**: it writes into the upload folders, and LM2 has been sent.
- Standard: `PUSH_STANDARD_AND_AUDIT_20261111.md` (rule 0: the outcome section; then the push standard).
- Returns: LM3 in `..\pro_returns_20261111\LM3_TEICHMULLER_TOWER\`; LM3b in `..\pro_returns_20261111\LM3b_TEICHMULLER_PUSH\` (93 statements; **not reviewed by me**); LM2 in `..\answers\LM2_LOOP_EQUATIONS\LM2_LOOP_EQUATIONS\`.
- Reviews: `..\pro_reviews_20261111\LM3_TEICHMULLER_TOWER\` and `..\pro_reviews_20261111\LM2_LOOP_EQUATIONS\`, each with `REVIEW_author.md` and `checks_author\`.

## State of each prompt (11 November 23:50 UTC)

| Prompt | State |
|---|---|
| LM1_GROUP_SCHEMES | Packaged, not sent as far as I know. Has "After LM3", "After BISITE", the outcome section. Does **not** have rule 11 or an "After LM2" section: add them before sending (LM2 C.d1–C.d5, C.a15–C.a16 and D.5 bear on its Parts B and D: the adelic group, the two tori, the norm form, the action of `GT̂_0` on `SL_2(Z/n)`). |
| LM2_LOOP_EQUATIONS | Sent, answered, reviewed. |
| LM3_TEICHMULLER_TOWER | Sent, answered, reviewed. |
| LM3b_TEICHMULLER_PUSH | Sent, answered; review is the next task. Its Lead 4 is corrected by LM2 B.g4 (below). |
| LM4–LM8 | Unsent; wait for second passes of the transcription (README table). Carry "After LM3", "After BISITE", "After LM2", the outcome section, rule 11. No zips. `CHANGES_20261112_LM2.md` in each folder. |

## What is established (with who checked it)

- **Two groups.** `𝕀Γ_{g,ν}` of §26 is `N_O(Σ)/Σ`; of §29 it is the arithmetic image modulo `Σ`. For §29 the conjecture fondamentale is a theorem (Hoshi–Mochizuki 2011, Cor. 6.4; I opened it). For §26: `GT̂_0` at `(0,3)`, `GT̂` at `(0,n)`, `n ≥ 4`, and `(1,1)` (LM3 E.7, E.10; proofs followed in outline).
- **§46 is the system (I), (II)** (LM2 B.m2), so `M̃^!_{0,3}` is an extension of `GT̂_0` by `F̂_2`.
- **Congruences are formal.** Every element of `GT̂_0` acts on `SL_2(Z/n)` by conjugation with a matrix of determinant `μ`; outer images of Galois, `GT̂`, `GT̂_0` agree and are units modulo squares (LM2 C.d1, C.a16, C.r1). C.d1 was **not followed** by me.
- **Three graded spaces at `(0,3)`** (recomputed by me, weights ≤ 9): raw two- and three-cycle solutions 1, 0, 1, 1, 2, 3, 6, 10, 19; special `𝔖_3`-invariants 0, 0, 1, 0, 1, 0, 2, 1, 4 (the graded envelope of `GT_0`: antisymmetry and `J(ψ) = 0`); `grt_1` 0, 0, 1, 0, 1, 0, 1, 1, 1. All special derivations modulo inner: 0, 0, 1, 0, 3, 0, 6, 4.
- **Witnesses** (recomputed): `q_4` raw and not special; `q_7` special and failing the pentagon, coefficient 16 on `a⁵bcb`.
- **One condition of §§38–47 beyond `GT̂`**: compatibility with `φ: F̂_2 → (C_2 * C_3)^` (§47); Galois satisfies it (LM2 E.1); whether `GT̂` does is open (E.3).

## My own results (unverified by anyone else; all are labelled leads in the prompts)

1. Lifting lemma: every special derivation over `Z_ℓ` is the leading term of a special automorphism of the free pro-ℓ group (any choice at each step extends). LM3 review.
2. Pro-ℓ: the geometric `𝔖_3` is not normal in `Out_lac` at `(0,3)` (weight 5); the sequence "??" for `(0,4) → (0,3)` is not exact in the middle (weight 3). LM3 review.
3. Pro-ℓ, `ℓ ≥ 5`: the centralizer of `𝔖_3` has an element with leading term `q_7`, so the pro-ℓ `GT_0` is larger than the pro-ℓ `GT` (invariants of a group of order prime to ℓ are exact on the filtration). LM2 review, Proposition 1. Missing: the pro-ℓ form of Harbater–Schneps Theorem 2; ℓ = 2, 3; the profinite group.
4. Reductions in the LM2 review: E.3 as the fixed points of an endomorphism `δ` of `GT̂_0`; D.6 through an invariant `χ` and a CM case of the section conjecture; C.d5 through the open image of two CM characters; B.f7 through the types of the 57 classes of `PSL_2(F_7)`.

## Where I was wrong

- LM3 prompt, Lead 1 (one group where there are two) and Lead 4 (normality is not the congruence property).
- LM3 review and LM2 prompt: I identified the special invariants with the solutions of the two linear cycle equations. False (LM2 B.g4). The lesson is rule 11: a linearization is a statement to prove.
- The Stallings lead was right (LM2 B.f8) but the map is not a loop automorphism.

## Open, in order of what I would do next

1. Review LM3b (93 statements, 50 programs). Check first what it says on B.7, C.8 and my Leads 1–3, on `GT̂ ≠ GT̂_0`, and on E.14/F.16.
2. E.3: compute `δ` on the shadows of the `𝔖_4`-envelope (order 442368). A prompt of its own may be worth it: "special loci for `GT̂`".
3. The profinite form of result 3: does the image of `GT̂_0` in the pro-ℓ centralizer contain an element outside `grt_1` in leading term.
4. LM1: add rule 11 and "After LM2", rebuild its zip with `LM2_return/`, `LM2_review/`.
5. The recent-results fold for LM6–LM8 listed in the README is still partly undone.

## Cautions

- `OVERVIEW.md` is in sent zips and is not edited; its corrections are in the LM3 review.
- Dates in the files I wrote on this last stretch say 12 November (local time); UTC was still 11 November.
- The user's rules that shaped this: Pro does only what is asked (push standard); every prompt states its outcome (rule 0); never run Pro's code; credit returns as AI-produced by GPT-6 Astra (ChatGPT Pro mode); mark everything not verified.

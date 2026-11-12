# Redo of the push rewrite of the unsent LM prompts: record

Section 1: Claude Fable 5.2, effort max (LM field expert), 12 Nov 2026. State: **not finished**. No `PROMPT.md` in
`pro_prompts_draft_20261111_work\` was changed, no `PROMPT_before_redo_20261112.md` was made, no upload folder was
touched.

## What exists

New Parts, written from a full reading of cote 140-2 (Part I, §§1–37) and to the push standard, as separate files in
this folder, ready to be placed under `## Parts` of each prompt:

| Prompt | File | Covers | Not covered |
|---|---|---|---|
| LM4_FINITE_GROUP_ACTIONS | `LM4_PARTS_redo_20261112.md` | Parts A–F (items 1–7) | — |
| LM5_MULTI_GALOIS_TOPOI | `LM5_PARTS_redo_20261112.md` | Parts A–E | — |
| LM6_POINTS_AS_SECTIONS | `LM6_PARTS_redo_20261112.md` | Parts A–D | Part E (Fermat, §51.16): its passages are in cote 140-4, which this expert has not read |
| LM7_FERMAT_TOWER | none | — | everything: §51 (cote 140-4) not read |
| LM8_LIE_APPROXIMATIONS | none | — | everything: §52 (cote 140-4) not read |

They were written before this line's LM3 and LM3b reviews exist (those reviews are not done). A successor rereads
them after the reviews and adjusts Part F of LM4 and Parts B–C of LM6 if the reviews change what is settled.

## What each set of Parts demands

- **LM4.** A: proofs of the whole rigidity list for discrete and profinite groups with loops, type by type, his
  unproved (2), (4) of scan 500, his theorem `Autext(π', i) ≅ Aut(π)` with its omitted compatibilities. B: the two
  gaps of his "lemme fondamental" closed; the section/fixed-point theorems including anti-involutions with
  punctures; §18's lemma without the realizability assumption, questions c), d), e), the counterexample behind
  "faux !"; a formula for `μ` and its intrinsic character; the complete classification of anti-involutions and the
  questions on `H ≅ Z^g`; a program over all types with `2g + ν ≤ 6`. C: his 2-equivalence conjecture proved level
  by level (a proposed chain: realization, Teichmüller uniqueness, Birman–Hilden, contractibility; each link to be
  checked); `A^{0Γ}` and `H⁰(Γ, π_1(Mon)) = 1`; the drilling conjecture and programme I–III; the criterion of scan
  294; the theorem of scan 304 with the extension class computed. D: his two profinite "conjectures sans vergogne",
  finite subgroups of `Autext_lac(π̂)` not stabilizing a discretization (decide for `(0,3)` at least, by program and
  proof), the image of `Discrét(π) → Discrét(π')`, the profinite torsion-free extension statement. E: `SE`, `SΓ`
  constructed and compared; the two-group situation decided discretely and reduced profinitely to a statement on
  pairs `(λ, f)`. F: three labelled lemmas for §§26–32, proved.
- **LM5.** A: Proposition 1.1 decided (a ⇒ b), every statement of §§1–2, 4 proved or corrected, 1.12 and §3 written,
  the tower `E_[i]` constructed, the two examples of 2.3 constructed. B: `B_{X,U}`, the comparison with étale
  cohomology with the complete list of exceptions, the canonical isomorphisms of scans 130–131, the trace, mixed
  morphisms. C: the 2-cartesian and 2-pushout statements of §16 with the 2-category in which they hold, acyclicity
  decided, group actions on topoi, `B_π` with operators. D: the extension `Ã_0`, the classification (70)–(71) proved
  (his own argument stops), the next Postnikov invariants, the fidelity bounds decided, the arithmetic 2-category
  of forms of `P¹`. E: the shape of a topos; which statements extend to all levels.
- **LM6 (A–D).** A: the category `B` with his three unverified assertions proved; Conjecture 7.1 case by case with the
  reduction to the Isom/Hom theorems written; case IV b) directly; the Kummer data from the loop structure; §11 (d)
  for `ρ = −1` explicitly; the loop structure from the Galois action; the commutant `S_3`. B: cuspidal sections and
  the tangential subtorsor under morphisms; injectivity; the diagram of implications between his axioms ①–⑥ and the
  section conjecture in its forms; the `p`-adic affine case from the 2026 theorem; the relative version over a
  base; his admissibility criteria; the lattice attached to a rational point. C: the profinite real section
  statement with cusps and their cyclic order, (29)–(30) of §29, explicit computation for `P¹ ∖ {0,1,∞}` over `Q`.
  D: the logical relations between his finiteness statement, the section conjecture and Faltings; finiteness for
  `X_0(N)`, `X_1(N)`; the strongest finiteness provable in general.

## Check of every Part against the push test (coordinator addition D) and the push standard

Each lettered ask was reread for its verb. Result: every ask has a producing verb (prove, refute, decide,
construct, compute, classify, write out a missing section with proofs); every Part ends with a "Done for Part X"
sentence; known theorems are named as tools with the demand to derive his statement from them (LM4 header; LM5
header; LM6 header and A (b)). Places where the wording is closest to a status ask, to be watched when the prompts
are assembled: LM6 A (b) "say which theorem gives it over which fields" (kept because it is followed by "write the
proof of the reduction"); LM6 C (b) "state precisely what the conjectural identification adds" (a statement, not a
proof: acceptable only as the second half of the ask); LM4 F and LM5 E depend on other packages. No ask says
"briefly", "a table of", "status", "survey", "cite or prove", "say what remains". Programs are demanded in LM4 B (f),
C (e), D (b), E (b), LM6 C (c). Not yet checked: that the Parts fill a Pro run (rule 7) against the measured lengths
of the Dérivateurs prompts; LM4's Parts are about 2,800 words, LM5's about 1,800, LM6's (A-D) about 2,100 (counted with wc -w, comment headers included).

## How to assemble each prompt (not done)

1. Copy the current `PROMPT.md` to `PROMPT_before_redo_20261112.md`.
2. Start from `PROMPT_before_push_20261111.md`.
3. Keep from the later states: the section "What the outcome must be" with its disconnect item (it is in
   `PROMPT_before_disconnect_clause_20261111.md` without the disconnect item and in the current `PROMPT.md` with
   it; take the current one); for LM4 the second-pass edits of 12 Nov (`second_pass_edits_20261112.py`, written by
   Claude Opus 5.5 at effort max): they correct the wording and the quotations of "What is to be settled" and of
   the background, but they were applied to a text in which the void rewrite had appended an "**Asked:**" clause to
   each item: carry over the corrected descriptions and leave out every "**Asked:**" clause (the Parts now carry the
   asks).
4. Do NOT carry over without a decision of the coordinator: the blocks "After LM3", "After BISITE and the seven
   Dérivateurs returns" and "After LM2" of the current prompts. They were generated by the void rewrite
   (`push_rewrite_20261111.py`, `after_lm2_block.py`) and rest on reviews under `pro_reviews_20261111\`, which this
   line was told are discarded. Rule 11 of the common block came with "After LM2". The blocks "After CATHOT / GALOIS
   / STRATA / PATHS" are in `PROMPT_before_push` and stay, but they cite reviews "by the author of this prompt" that
   are being redone at effort max by the Dérivateurs line: update them from that line's results before sending.
5. Replace the Parts by the file of this folder. In LM6 keep Part E from `PROMPT_before_push` until it is redone.
6. Correct in LM5 the scan ranges of the heading sentences (§14: scans 119–137; §16: 160–178; §20: 233–250; the
   quotation "bien profond" is at scan 259, in §21, not §20). In LM6 item 3 the scans "436–470" for §33 are
   437–471; "136–148" are 137–151.
7. Reread every Part against the push test once more and add the result here.

## Also for the prompts (from FINDINGS.md and HUNCHES.md)

- A result proved by this expert (FINDINGS F1: uniqueness of Nielsen realization up to conjugation by a
  homeomorphism isotopic to the identity, by Teichmüller's uniqueness theorem) is folded into LM4 Part C (b) as a
  chain to be checked link by link.
- Hunches H3, H4 are folded into LM4 Parts C (d) and D; H5, H6, H7 into LM6 Parts B (c), (g) and C. H1 (the loop
  equation of Part II against the relations of GT_0 and the pentagon) and H2 (his hole-plugging map on full
  automorphism groups) need Part II and the LM3/LM3b reviews; no draft exists yet under `LM_EXPERT\PRO_PROMPTS\`.

# LM2_LOOP_EQUATIONS: files to add to the background (11 Nov 2026, recent results)

The prompt's section "Recent results (state: 10 Nov 2026)" relies on one manuscript. Add its proof pack to the zip, besides the list in BACKGROUND.md, under `proof_packs/008_The-Deligne-Drinfeld-conjecture-/` (source root: `C:\Users\user\Documents\recent_results_20261110\proof_packs\008_The-Deligne-Drinfeld-conjecture-\`):

- `C:\Users\user\Documents\recent_results_20261110\proof_packs\008_The-Deligne-Drinfeld-conjecture-\008_The-Deligne-Drinfeld-conjecture-September-23-2026.pdf` -> `proof_packs/008_The-Deligne-Drinfeld-conjecture-/008_The-Deligne-Drinfeld-conjecture-September-23-2026.pdf`
- `C:\Users\user\Documents\recent_results_20261110\proof_packs\008_The-Deligne-Drinfeld-conjecture-\PACK.md` -> `proof_packs/008_The-Deligne-Drinfeld-conjecture-/PACK.md`

The prompt quotes the Lean scope note and the Lean statement of the main theorem. They are not in the pack folder; fetch them and put them beside the manuscript, so that the model can compare the statement itself:

- https://raw.githubusercontent.com/openai/math/main/lean/docs/008.md -> `proof_packs/008_The-Deligne-Drinfeld-conjecture-/lean/008.md`
- https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/DeligneDrinfeld.lean -> `proof_packs/008_The-Deligne-Drinfeld-conjecture-/lean/DeligneDrinfeld.lean` (the statement only: its proof is replaced by `sorry` in this file by design, and the proof itself is elsewhere in the repository)

Note on `PACK.md`: its Lean line gives only the exclusion from the scope note. The prompt states the scope in full (the statement of Theorem 1.1 is formalized; Proposition 7.1 and the graph-complex corollary are not).

Papers the new section names from memory, to resolve by title and add under `papers/` if freely readable: R. Hain, M. Matsumoto, *Weighted completion of Galois groups and Galois actions on the fundamental group of P^1 − {0, 1, ∞}*, Compositio Math. 139 (2003) (m); F. Brown, *Mixed Tate motives over Z*, Ann. of Math. 175 (2012) (arXiv:1102.1312) (m).

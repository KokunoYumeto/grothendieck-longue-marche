# Notes for assembling the successor prompts (main session, procedural)

Kept by the main session (Claude Opus 5.5 at effort max), 14 Nov 2026. Read before building any of the successor
prompts of the anabelian line (SECTIONS_OVER_Q, the ANABELIAN successor, the Fermat successor from PUSH_ITEMS_20261114
Part 1, LM8_PUSH and any other prompt whose rows rest on the local theorem).

## The OpenAI local theorem goes in, to be used and checked while working (the user, 14 Nov ~17:5x UTC)

The user: "Given the unrefereed OpenAI local theorem of 6 October, then that's the kind of stuff that you throw in the
zip for Astra to integrate and check and run over again. I generally have faith in AI theorems as being at the level
of highly professional preprints. So it's worth taking seriously and putting in there, but making it, check it while
working is fine."

- Attach the LaTeX sources, not the PDFs (rule: zips carry LaTeX), from
  `pro_intake_20261114/debate_20261114/background_sources/`:
  - `The-p-adic-section-conjecture-October-6-2026/build/` (main.tex, sections 01-08, references.bib, figures):
    OpenAI, *The p-adic section conjecture*, unrefereed preprint of 6 October 2026,
    github.com/openai/math/tree/main/preprints/The-p-adic-section-conjecture-October-6-2026 (fetched 14 Nov 2026,
    commit 4eaee87548);
  - `Open-Homomorphisms-of-Global-Solvably-Closed-Galois-Groups-October-5-2026/build/`: OpenAI, *Open homomorphisms of
    global solvably closed Galois groups*, unrefereed preprint of 5 October 2026 (same repository and fetch).
- The clause in each prompt that uses them: treat the preprint as a professional preprint; use its Theorem 1.1 where
  the work needs it; check the steps you use as you go; LM6 D.6 reports a gap in its Section 8 (global sections):
  settle that gap (prove the step, repair it, or refute it) as part of the work, and say which results of the return
  depend on it.
- Prompts concerned: SECTIONS_OVER_Q (LM6 B.27, D1, everything after E.12), the Fermat successor (item 1.13: E.6-E.12
  with the sources opened), the ANABELIAN successor where its Part D rows remain, LM8_PUSH where its new results lines
  cite LM6 rows that rest on Theorem 1.1.

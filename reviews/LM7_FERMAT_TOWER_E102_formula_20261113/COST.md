# What finding the E.102 formula took (13 Nov 2026)

- Main session, Claude Opus 5.5 at effort max: the identification K_4 = Lambda^2(Lambda^2 V), the independent recomputation
  of E.102 from the degree-one data, and the split-model formula (RESULT.md, e102_formula.py). Not metered separately;
  roughly 40-60k tokens of the session's context, and two program runs of under a minute each.
- Claude Fable 5.2 at effort max, one agent, no sub-agents: the closed formula, its derivation and 28 variation tests
  (FORMULA.md, fable_*.py, fable_step3_tests.out): 287,112 tokens, 35 tool calls, 30.8 minutes.
- The statement itself (E.102) is by GPT-6 Astra (ChatGPT Pro mode), in the LM7_FERMAT_TOWER return.

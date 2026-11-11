# La Longue Marche: development prompts LM4_FINITE_GROUP_ACTIONS to LM5_MULTI_GALOIS_TOPOI (draft)

**PROVISIONAL.** Written by Claude (Fable 5.2), 11 November 2026, for GPT-6 Astra (ChatGPT Pro mode). Design only: nothing is packaged, downloaded or sent. The stack will be revised as the remaining second passes come in. Each folder holds `PROMPT.md` (complete, with the shared rules appended) and `BACKGROUND.md` (what its zip needs: packages, scans, papers). `OVERVIEW.md` is the reading of the whole manuscript the prompts come from; `_COMMON_BLOCK.md` is the shared second half of every prompt.

The prompts follow the author's own programme: each takes one of the things he set out to do, collects his statements and questions on it across the manuscript with their scans, and asks for the mathematics to be carried through. Leads marked "Lead" are my inferences and are labelled unverified in each prompt. The prompts do not fix how the results enter the book: they ask for a self-contained text.

## Run now, or wait

| Prompt | Subject (his sections) | Verdict | Depends on |
|---|---|---|---|
| `LM1_GROUP_SCHEMES` | The group schemes `M_{ρ,σ}` over `Z`; schematic envelopes (§§48–50) | **Can run now.** **NOT SENT** (user, 11 Nov). Rewritten to the push standard with the outcome section (rule 0) and repackaged on 11 Nov: see the last section. | Cote 140-3 scans 264–696 and cote 140-4 scans 1–57, all second-passed. Many open places remain in these packages (15 to 70 each); the prompt makes the model report on them. |
| `LM2_LOOP_EQUATIONS` | The equation of loops in types (0,3), (1,1), against `GT̂` (§§36–47) | **Can run now**, once LM_P060 is decided or with both returns attached. **NOT SENT** (user, 11 Nov). Rewritten to the push standard with the outcome section (rule 0) and repackaged on 11 Nov: see the last section. | Cote 140-2 scans 491–575 and cote 140-3 scans 1–282, second-passed. LM_P060 (140-3 scans 11–20) has two first-pass returns. The 140-1 draft (C1) is optional and not second-passed. |
| `LM3_TEICHMULLER_TOWER` | The Teichmüller tower, profinite forms, the "conjecture fondamentale" (§§19, 21, 26–36) | **Can run now, all parts**, better after the 33 open fixes of P011–P040 are merged. Part F no longer waits: the answer to the Dérivateurs prompt `5_STRATA` came back on 11 Nov and is folded in (see the last section). | Cote 140-2 scans 201–550, second-passed; `merge_fixes_open.md` touches P033–P040. |
| `LM4_FINITE_GROUP_ACTIONS` | Finite groups acting on surfaces and on groups with loops (§§12–18, 23–25 bis, 31) | **Wait** for the second pass of the pilot packages LM_P06–P10 (scans 51–100) and the merge of the open fixes of P011–P040. | Its first two items (rigidity of loops; §§12–13 bis) sit in the unpassed pilot scans. |
| `LM5_MULTI_GALOIS_TOPOI` | Multi-Galois topoi, the topos at the missing points, van Kampen, §20 (§§1–4, 14, 16, 20) | **Wait** for the second pass of LM_P01, P02 (scans 1–20). Part E also uses the output of the Dérivateurs prompt `4_GALOIS` (returned 11 Nov; folded into the prompt, see the last section). | §§1–4 exist only in the first pass. |
| `LM6_POINTS_AS_SECTIONS` | Points as sections; real structures; Mordell and Fermat through splittings (§§5–11, 13, 32–33, 51.16) | **Wait** for LM_P02, P04–P10 (scans 11–100: the statement of the fundamental conjecture) and LM_C4-153-171, C4-172-190 (§51.16). | Both ends of its subject are in unpassed packages. |
| `LM7_FERMAT_TOWER` | The Fermat tower in the metabelian approximation (§51.1–15) | **Wait** for LM_C4-115-133, C4-134-152, C4-153-171 (and C4-172-190). | §51.11–15 are in unpassed packages. Uses LM1_GROUP_SCHEMES, Part E. |
| `LM8_LIE_APPROXIMATIONS` | Lie approximations, L-groups, `ST_{1,1}` (§§52–53) | **Wait** for LM_C4-172-190 to C4-267-280 and C1. **The prompt must be rewritten** when the checked text exists: it is drafted from the first pass and the table of contents. | All of its text is unpassed. |

Suggested order: LM1_GROUP_SCHEMES, LM2_LOOP_EQUATIONS, LM3_TEICHMULLER_TOWER (A–E); then LM4_FINITE_GROUP_ACTIONS, LM5_MULTI_GALOIS_TOPOI, LM6_POINTS_AS_SECTIONS; then LM7_FERMAT_TOWER, LM8_LIE_APPROXIMATIONS. Dependencies between prompts: LM7_FERMAT_TOWER and LM8_LIE_APPROXIMATIONS use LM1_GROUP_SCHEMES (Part E); LM6_POINTS_AS_SECTIONS (Part E) uses LM7_FERMAT_TOWER and LM8_LIE_APPROXIMATIONS; LM3_TEICHMULLER_TOWER and LM6_POINTS_AS_SECTIONS cite the lemmas of LM4_FINITE_GROUP_ACTIONS (Part F); LM2_LOOP_EQUATIONS's dictionary helps LM1_GROUP_SCHEMES and LM7_FERMAT_TOWER.

Not covered by a prompt: §37 (Legendre, level 4: computations, folded into LM2_LOOP_EQUATIONS only as background); §21 (Teichmüller spaces) beyond what LM3_TEICHMULLER_TOWER needs; prime-to-`p` variants. The notes files `NOTES_B` (unpursued implications) and `NOTES_C` (unproved claims, model ideas) have not been read for this draft: a later revision should add what they contain to the prompts' item lists.

## Overlaps with the Dérivateurs prompts

The Dérivateurs prompts are in `C:\Users\user\Documents\derivateurs_companion_20261109\pro_prompts_20261110\` (folders renumbered there in running order: 1_CATHOT, 2_TOTAL_ASPHERICITY, 3_POLES, 4_GALOIS, 5_STRATA, 6_PATHS, 7_BISITE).

| Theme | Dérivateurs side | Longue Marche side | How the work is divided |
|---|---|---|---|
| The Teichmüller tower, `M̄_{0,n}`, the Esquisse | `5_STRATA`, Part F: the exit-path category `T_{0,n}` of the boundary stratification as an ordinary category, with coefficients on it | `LM3_TEICHMULLER_TOWER`, Part F: its profinite completion, the action of `Gal(Q̄/Q)`, the comparison with `GT̂` | STRATA builds the category and its functors (topology, no arithmetic) and now uses his §19 and §§26–27 definitions; LM3_TEICHMULLER_TOWER starts from that output and does the Galois side. **Edited:** STRATA Part F got item (iv) and three Longue Marche packages in its background. |
| Fundamental groupoids without base points; locally constant coefficients; Galois reconstruction | `4_GALOIS`, Parts A and F: the localizer of equivalences on locally constant coefficients, for any coefficient theory, on small categories | `LM5_MULTI_GALOIS_TOPOI`, Parts A and E: multi-Galois topoi (set-valued coefficients, general topoi) | GALOIS states the reconstruction theorem so that it specializes to a locally connected topos; LM5_MULTI_GALOIS_TOPOI does the 1-topos theory in his generality and cites it. **Edited:** GALOIS Part F got one sentence and LM_P01–P02 in its background. |
| Gluing along an open and its closed complement | `5_STRATA`, Part C: collages of categories, homotopy links, gluing of topoi (SGA 4 IV 9.5) | `LM5_MULTI_GALOIS_TOPOI`, Parts B–C: the topos `B_{X,U}` at the missing points, van Kampen for topoi, filling and drilling holes | Different objects (categories and stratified spaces there, topoi of curves here). No edit; each should cite the other's result when it exists. |
| Levels of faithfulness | Audited Chapter VIII (the three-level criterion for 1-types) and `4_GALOIS`, Part E (the tower by levels) | `LM4_FINITE_GROUP_ACTIONS`, Part C ("3-fidèle") and `LM5_MULTI_GALOIS_TOPOI`, Part D (the fidelity bounds of §20) | No edit. LM4_FINITE_GROUP_ACTIONS and LM5_MULTI_GALOIS_TOPOI work at levels 1 and 2 only. |
| Unipotent and nilpotent approximations | `4_GALOIS`, Part C (`D(Q)`, rational homotopy with `π_1`) | `LM6_POINTS_AS_SECTIONS` Part E, `LM7_FERMAT_TOWER` Part E, `LM8_LIE_APPROXIMATIONS` Parts B and F (Lie approximations, splittings) | No edit. The Dérivateurs side is about spaces, this side about Galois actions and sections. |
| Homotopy types with Galois action | `4_GALOIS`, Part F (shape, fundamental pro-∞-groupoid) | `LM3_TEICHMULLER_TOWER`, Parts E–F (the étale homotopy type of the moduli stacks) | No edit. |

Changes made to the Dérivateurs prompts on 11 November, and only these: `5_STRATA\PROMPT.md` (Part F, item (iv)) and `5_STRATA\BACKGROUND.md` (LM_P021–P024, LM_P034–P036, the table of contents); `4_GALOIS\PROMPT.md` (one sentence in Part F) and `4_GALOIS\BACKGROUND.md` (LM_P01–P02). Their zips were built before this and need those files added, and the manifests updated. `1_CATHOT` (already submitted), `2_TOTAL_ASPHERICITY`, `3_POLES`, `6_PATHS` and `7_BISITE` have no Longue Marche counterpart and are unchanged.

## What this draft rests on

See `OVERVIEW.md`, section 0. In short: the author's table of contents, the coordinator's global pass over the notes on his conjectures and questions, the second-pass correction lines of the board card, the source audit's two open findings, and a few passages read directly. The 96 checked texts were not read line by line for this draft, and `PLAN_RECORD.md` was read in full for Q1–Q57 and through its sections 2–5 and addendum for the rest. Every scan reference in the prompts comes from the global pass or the card and must be checked against the current text when a package is assembled.

## Assembling a package (when the user decides to run one)

Copy the current text and the `_notes_checked.md` of the packages listed in `BACKGROUND.md` (current text = the first that exists of `second_pass\LM_<KEY>_checked_fixed.tex`, `second_pass\LM_<KEY>_checked.tex`, `answers\fixed\…`, `answers\unzipped\<KEY>\…`), the scan images named there, the table of contents, `OVERVIEW.md`, and the papers (arXiv source where there is a number, otherwise the freely readable PDF; "(m)" entries are from memory and must be resolved by title first). Write a manifest with every file, its source and its SHA-256. ChatGPT takes at most 20 files per message, so the attachment is one zip and the prompt is pasted as text.

## 11 November 2026: after the first Dérivateurs return

The CATHOT answer of the Dérivateurs series bears on two prompts here: `LM5_MULTI_GALOIS_TOPOI` and `LM4_FINITE_GROUP_ACTIONS` each got a section before their Parts and a `CHANGES_20261110.md` naming the parts of that answer to attach. The other six are unchanged, and the run-now-or-wait table above is unchanged.

## 11 November 2026: recent results (state: 10 Nov 2026)

Source: `C:\Users\user\Documents\recent_results_20261110\` (`BRIEF_FOR_PROMPTS.md`, `RECENT_RESULTS.md`, `SCOREBOARD.md`, `proof_packs\`). All "OpenAI NNN" items are AI-produced manuscripts of github.com/openai/math, unrefereed. A prompt that relies on one carries its proof pack and asks the model to work through the steps it uses.

Done for the three prompts that can run: `LM2_LOOP_EQUATIONS` got a section before its Parts (OpenAI 008); `LM3_TEICHMULLER_TOWER` got one (OpenAI 008, 019, 031; the survey of B. Collas, arXiv:2603.02848v2); `LM1_GROUP_SCHEMES` is unchanged (nothing bears). Each folder has a `CHANGES_20261110.md` with what was considered and left out, and LM2 and LM3 a `BACKGROUND_ADD.md` with the pack files. The run-now-or-wait table is unchanged.

Not yet done, for when LM4 to LM8 are revised (their prompts are unchanged):

- `LM4_FINITE_GROUP_ACTIONS`: nothing bears as a premise or a result to cite. Context for Part D only: OpenAI 252, a torsion-free hyperbolic group with an element that dies in every finite quotient (Lean per the repository, scope note not read by us; our course `a-hyperbolic-group-that-is-not-residually-finite`). Surface groups and their finite extensions are residually finite, so no statement of the prompt changes.
- `LM5_MULTI_GALOIS_TOPOI`: nothing found.
- `LM6_POINTS_AS_SECTIONS`: OpenAI 019 (the local `p`-adic section conjecture for proper curves of genus ≥ 2; no Lean) bears most here. Lead 2 ("Open in general") must be rewritten with the exact status. Part B: the Frobenius conditions of scan 480 against Theorem 1.1 and the localization of global sections (Proposition 8.1: the classes of sections of a proper curve over a number field are the finite-cover descent locus). Part D: Mordell through splittings, with Proposition 8.1 and Theorem 8.2. Part E: Corollary 8.3 (curves with a map to an abelian variety with finite Mordell–Weil group and no divisible part in Ш) applies to proper Fermat curves that have such a quotient; the affine `U_n` and its cuspidal sections, which §51.16 is about, are not covered. Part C: the manuscript cites Bresciani–Vistoli for the real section theorem. Also OpenAI 031 (Uchida's conjecture; no Lean; our 8-lesson course) for the field case of Conjecture 5.5 in Part A, and OpenAI 009 (Bogomolov–Pop; Lean for uniqueness only) as context: it is birational, over algebraically closed constants, outside his base fields. Packs: `019_…`, `031_…`.
- `LM7_FERMAT_TOWER`: OpenAI 008 (the Lie algebra of solutions of antisymmetry, 3-cycle and pentagon is free on one generator in each odd weight ≥ 3; Lean statement of the main theorem) bears on Part E (the next approximations: rationally, the graded Lie algebra acting on the deeper quotients of `π_1` of type `(0,3)` is claimed to be this free Lie algebra and no larger). The metabelian level itself (Parts B–D, Ihara's power series) sees only the depth-one part of the generators, which was known before (Ihara; Drinfeld; Proposition 7.3 and Lemma 8.1 of the manuscript restate it). Pack: `008_…`.
- `LM8_LIE_APPROXIMATIONS`: OpenAI 008 bears directly: Lead 1 compares his Lie approximations with the pro-unipotent `GT` and `grt`. Part B (types `(0,3)`, `(0,4)`): compare each approximation with the solution space `W` of the manuscript weight by weight, using `dim W_n = 1, 0, 1, 0, 1, 1, 1, 1, 2, 2` for `n = 3, …, 12`. Type `(1,1)` and §53 are not covered by it. Part F (splittings): OpenAI 019 as for LM6. Packs: `008_…`, `019_…`.
- For LM6 and LM8, as context: B. Collas, *Anabelian perspectives in Galois–Teichmüller theory*, arXiv:2603.02848v2 (human; survey; abstract read only).

## Former names

Renamed on 10 Nov 2026 in run order (like the Dérivateurs prompts); the old numbers continued the transcription packages and are kept here for reference.

| Now | Before |
|---|---|
| `LM1_GROUP_SCHEMES` | `LM_P165` |
| `LM2_LOOP_EQUATIONS` | `LM_P164` |
| `LM3_TEICHMULLER_TOWER` | `LM_P162` |
| `LM4_FINITE_GROUP_ACTIONS` | `LM_P161` |
| `LM5_MULTI_GALOIS_TOPOI` | `LM_P168` |
| `LM6_POINTS_AS_SECTIONS` | `LM_P163` |
| `LM7_FERMAT_TOWER` | `LM_P166` |
| `LM8_LIE_APPROXIMATIONS` | `LM_P167` |

## 11 November 2026: after the GALOIS answer of the Dérivateurs series

The Dérivateurs prompt `4_GALOIS` has been answered (GPT-6 Astra, ChatGPT Pro mode; 74 statements; under review, so cited as unverified). Record: `C:\Users\user\Documents\derivateurs_companion_20261109\pro_reviews_20261110\4_GALOIS\PROMPT_UPDATES.md`.

- `LM5_MULTI_GALOIS_TOPOI`: section "After GALOIS" before the Parts (Part E's input now exists: the statement for a locally connected topos, F.4; the levels; the direct van Kampen axiom at all levels; CATHOT E.17 claimed proved). `BACKGROUND.md` lists the files to attach. No zip. Still waits for the second pass of LM_P01, P02.
- `LM3_TEICHMULLER_TOWER`: short section "After GALOIS" (Part F: what a profinite completion remembers; Part E: two rational theories). Zip rebuilt with ten files under `GALOIS_return/`; the previous zip is `LM3_TEICHMULLER_TOWER_background_v1.zip`; `MANIFEST.tsv`, `ASSEMBLY.md`, `BACKGROUND_ADD.md` updated.
- `LM4_FINITE_GROUP_ACTIONS`: short section "After GALOIS" (the ladder of conditions on `π_{≤ r+1}` for Part C). `BACKGROUND.md` lists the files. No zip.
- `LM1_GROUP_SCHEMES`, `LM2_LOOP_EQUATIONS`, `LM6_POINTS_AS_SECTIONS`, `LM7_FERMAT_TOWER`, `LM8_LIE_APPROXIMATIONS`: unchanged. For LM1 and LM8 (schematic envelopes, Lie approximations) one statement is worth knowing when they are revised and was not put in: GALOIS C.13–C.14, the rational theory that keeps the discrete fundamental group is strictly finer than Toën's schematization, which sees the pro-algebraic completion.

No lead of this stack is refuted or settled by GALOIS; the run-now-or-wait table is unchanged.

## 11 November 2026: after the STRATA answer of the Dérivateurs series

The Dérivateurs prompt `5_STRATA` has been answered (GPT-6 Astra, ChatGPT Pro mode; 81 statements: 54 Proved, 14 Known, 9 Refuted, 4 Open) and reviewed by Claude (Fable 5.2): no statement labelled Proved, Known or Refuted was found false. Record: `C:\Users\user\Documents\derivateurs_companion_20261109\pro_reviews_20261110\5_STRATA\PROMPT_UPDATES.md`; review: `REVIEW_author.md` beside it.

- `LM3_TEICHMULLER_TOWER`: section "After STRATA" before "Recent results" (the category `T_{0,n}` and its opposite, the cases `n = 4, 5`, his groups of §19, the forgetful and clutching functors with their properties, and five suggestions for Part F marked as unverified inferences); the sentence of Part F that said "if its output is attached" now says that it is. Zip rebuilt with 37 added files (`STRATA_return/`, `STRATA_review/`, Jansen's paper, *Exodromy*); the previous zip is `LM3_TEICHMULLER_TOWER_background_v2.zip`; `MANIFEST.tsv`, `ASSEMBLY.md`, `BACKGROUND_ADD.md`, `CHANGES_20261110.md` updated. **Ready to send, all parts.**
- `LM4_FINITE_GROUP_ACTIONS`: short section "After STRATA" (a group with loops as a category in which every endomorphism is invertible; his groups of §19). `BACKGROUND.md` lists the files. No zip; still waits for the second pass of LM_P06–P10.
- `LM5_MULTI_GALOIS_TOPOI`: section "After STRATA" (gluing a topos from an open part, a closed part and the link; two candidate comparisons for `B_{X,U}`, marked as an unverified inference; the forgetful functor and its fibres). `BACKGROUND.md` lists the files. No zip; still waits for the second pass of LM_P01, P02.
- `LM1_GROUP_SCHEMES`, `LM2_LOOP_EQUATIONS`, `LM6_POINTS_AS_SECTIONS`, `LM7_FERMAT_TOWER`, `LM8_LIE_APPROXIMATIONS`: unchanged (no contact with STRATA).

No lead of this stack is refuted or settled by STRATA.


## 11 November 2026: after the PATHS answer of the Dérivateurs series

The Dérivateurs prompt `6_PATHS` has been answered (GPT-6 Astra, ChatGPT Pro mode; 76 statements: 40 Proved, 19 Refuted, 11 Known, 6 Open); under review by Claude (Fable 5.2), so cited as unverified. Record: `C:\Users\user\Documents\derivateurs_companion_20261109\pro_reviews_20261110\6_PATHS\PROMPT_UPDATES.md`.

- `LM4_FINITE_GROUP_ACTIONS`: short section "After PATHS" before the Parts (strict against homotopy-coherent actions, PATHS D.1, D.4, D.11, D.13; a reading of the essential-surjectivity problem in three layers, marked as an unverified inference). `BACKGROUND.md` lists the files. No zip; still waits for the second pass of LM_P06–P10.
- `LM5_MULTI_GALOIS_TOPOI`: section "After PATHS" before the Parts (a second proof of GALOIS B.11–B.12; finite tests do not determine a morphism of classifying topoi, PATHS E.13, with an unverified inference on profinite completions; the shapes of Kaledin's theorem; filtered colimits of categories). `BACKGROUND.md` lists the files. No zip; still waits for the second pass of LM_P01, P02.
- `LM3_TEICHMULLER_TOWER`: not edited (it was being sent). What of PATHS bears on its answer is listed in the record above.
- `LM1_GROUP_SCHEMES`, `LM2_LOOP_EQUATIONS`, `LM6_POINTS_AS_SECTIONS`, `LM7_FERMAT_TOWER`, `LM8_LIE_APPROXIMATIONS`: unchanged (no contact with PATHS).

No lead of this stack is refuted or settled by PATHS; the run-now-or-wait table is unchanged.

## 11 November 2026: after the LM3 answer; the push rewrite of LM4–LM8; LM3b

`LM3_TEICHMULLER_TOWER` has been answered (GPT-6 Astra, ChatGPT Pro mode; 110 statements: 57 Proved, 30 Known, 11 Refuted, 12 Open) and reviewed by Claude (Fable 5.2): `..\pro_reviews_20261111\LM3_TEICHMULLER_TOWER\REVIEW_author.md`, with `checks_author\`. No statement labelled Proved, Known or Refuted was found false. Its main result: `𝕀Γ_{g,ν}` has two definitions (§26: normalizer of the geometric subgroup; §29: arithmetic image); for the second the "conjecture fondamentale" is a theorem (Hoshi–Mochizuki 2011, Corollary 6.4), for the first the group is `GT̂_0` at `(0,3)` and `GT̂` at `(0,n)`, `n ≥ 4`, and `(1,1)`. Leads 1 and 4 of the LM3 prompt and two sentences of `OVERVIEW.md` (§2 on the conjecture fondamentale, §3 on the faithfulness he doubted and on the centre of `Gal`) are corrected in the review; `OVERVIEW.md` itself is in the sent stack and was not edited.

The audit of 11 November (`..\pro_prompts_draft_20261111_work\PUSH_STANDARD_AND_AUDIT_20261111.md`) found that the task lists of the LM prompts asked for status more than for mathematics. The unsent prompts LM4–LM8 were rewritten to its push standard in the work tree (`..\pro_prompts_draft_20261111_work\<name>\PROMPT.md`; before-copies `PROMPT_before_push_20261111.md`; record `PUSH_REWRITE_RECORD_20261111.md`; the texts are generated by `push_rewrite_20261111.py` and `followups_block.py` there):

| Prompt | Parts words before | verbs before | Parts words after | verbs after |
|---|---|---|---|---|
| LM4_FINITE_GROUP_ACTIONS | 275 | 10 | 2302 | 86 |
| LM5_MULTI_GALOIS_TOPOI | 291 | 4 | 1920 | 75 |
| LM6_POINTS_AS_SECTIONS | 387 | 9 | 1867 | 62 |
| LM7_FERMAT_TOWER | 298 | 6 | 1380 | 58 |
| LM8_LIE_APPROXIMATIONS | 213 | 3 | 1663 | 59 |

Each got: a demand at the end of every item of "What is to be settled"; a section "After LM3"; a section "After BISITE and the seven Dérivateurs returns" with the follow-ups L1–L6 of `derivateurs_companion_20261109\pro_reviews_20261110\7_BISITE\FOLLOW_UPS.md` (L1, L2 in LM5; L3, L6 in LM4; L4 in LM6; L5 in LM7 and LM8); and new Parts. The leads, the earlier "After …" sections and the common block are unchanged. The run-now-or-wait table is unchanged: all five still wait for their second passes, and no zip was built. Still not done for LM6–LM8: the fold of the recent-results brief (the list in the section "recent results" above); the "After LM3" sections of LM6, LM7, LM8 carry what LM3 established about the manuscripts 008, 019, 031, which covers part of it.

New draft: `LM3b_TEICHMULLER_PUSH` (work tree only; `PROMPT.md`, `BACKGROUND.md`; Parts: 1859 words, 82 demanding verbs by the same count). It attacks the twelve Open rows of LM3 and derives his statements from the theorems LM3 cited without using. Its first three leads are results of the review (pro-ℓ analogues of LM3 B.7 and C.8, by a computation with special derivations): unverified by anyone else. It can run on the LM3 package (all second-passed) once the user has seen it.

Added about 14:10 UTC: LM3b_TEICHMULLER_PUSH is packaged at the request of the coordinator. Upload folder LM3b_TEICHMULLER_PUSH/ holds PROMPT.md and LM3b_TEICHMULLER_PUSH_background.zip (297 files, 92.8 MB; manifest in the zip and in the work folder). The user has not yet seen the prompt; its first leads are unverified results of the LM3 review.

## 11 November 2026, 18:45 UTC: LM1 and LM2 were not sent; rewritten and repackaged; rule 0

The user corrected the record: `LM1_GROUP_SCHEMES` and `LM2_LOOP_EQUATIONS` had NOT been sent (only LM3 and, later, `LM3b_TEICHMULLER_PUSH`, which has returned). Both were redone like LM4–LM8 (`..\pro_prompts_draft_20261111_work\lm12_push_20261111.py`): a demand at the end of each item; sections "After LM3" and "After BISITE and the seven Dérivateurs returns"; new Parts; today's common block (rules 9–10) in place of the old one; and, for LM2, a paragraph on the two first-pass returns of LM_P060 (both attached; the second pass checked the later one against the scans and did not decide between them). Figures: `PUSH_REWRITE_RECORD_20261111.md` in the work tree. Upload folders hold `PROMPT.md` and the rebuilt zip (LM1: 186 files, 68.8 MB; LM2: 191 files, 39.3 MB; each with `MANIFEST.tsv` inside); the previous prompts and zips are in the work tree as `PROMPT_before_push_20261111.md` and `<name>_background_v1.zip`.

Rule 0 (user, 11 Nov, P3193; text in `PUSH_STANDARD_AND_AUDIT_20261111.md`): LM1, LM2 and LM4–LM8 each have a section "What the outcome must be" before the Parts (`outcome_block.py`). LM3b was sent before the rule and was not changed.

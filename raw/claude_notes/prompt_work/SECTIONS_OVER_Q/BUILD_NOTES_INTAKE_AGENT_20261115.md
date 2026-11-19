# Build notes of the intake agent (Claude Fable 5.2 at effort high) for the two successor prompts

Kept so that the job survives a compaction of my context. If you are me after a compaction: the summary is not
reliable; read this file, the coordinator's job message (below, in my words), and the two drafts, then go on.

## The job (main session, Claude Opus 5.5 at effort max, 14 Nov ~23:4x UTC; the user: the designers write their prompts)

Write two complete, sendable prompts from my item drafts.
1. SECTIONS_OVER_Q: draft `longue_marche_pro_pilot_20261104/pro_prompts_draft_20261111/02_SECTIONS_OVER_Q_DRAFT/ITEMS_DRAFT.md`.
   Build as folder `02_SECTIONS_OVER_Q` beside it, holding only `PROMPT.md` and the zip. Drafts and backups move to
   `pro_prompts_draft_20261111_work/SECTIONS_OVER_Q/`. Apply decision 4.4 of `CONSOLIDATED_REGISTER_20261114.md`:
   D4 becomes a pointer to the Fermat successor (its 1.14), A10 is thinned (the table is the Fermat successor's
   1.16), A5 stays, FS 1.20 becomes a pointer there (the Fermat successor is written by agent abbb9cee).
2. ANABELIAN successor: draft `grothendieck_archive_montpellier/pro_prompts_archive_20261112/02_ANABELIAN_SUCCESSOR_DRAFT/ITEMS_DRAFT.md`.
   Build as `02_ANABELIAN_SUCCESSOR` beside it; work files in `pro_prompts_archive_20261112_work/ANABELIAN_SUCCESSOR/`.
3. Both: frame from `longue_marche_pro_pilot_20261104/pro_prompts_draft_20261111/01_LM8_PUSH/PROMPT.md` and
   `_COMMON_BLOCK.md` (what is to be settled; results; WHAT THE OUTCOME MUST BE with the push paragraph and the
   three-hour check; parts; conventions; what is attached; rules of proof; "long by design"; typesetting check;
   hourly checkpoint clause via `claude_tools/prompts/checkpoint_rule.py`, apply()). Follow
   `pro_intake_20261114/debate_20261114/ASSEMBLY_NOTES_SUCCESSORS.md`: the two OpenAI preprints of 5 and 6 October
   go in as LaTeX from `debate_20261114/background_sources/`, with the check-while-working clause. Zip carries
   LaTeX, not PDFs; upload folder holds at most 20 files; every model named with its effort; no escape clauses, no
   minimums. Lint: `python -I -B <local>/Documents/claude_tools/push_rule_pro_prompts.py --lint-math <PROMPT.md>`
   until it passes. Bound about 250k tokens; no sub-agents; read only what the writing needs.
   Final message: for each prompt its folder, the zip (entries, size), the lint result.

## Facts found (15 Nov, early)

- Both drafts were edited by someone else at 19:15 on 14 Nov (backups `ITEMS_DRAFT_before_ghost_lambency_20261114.md`
  beside them): look at what was added (compare with `diff --strip-trailing-cr`, output cut with head) and keep it.
- NEVER run a plain `diff` of these files or print whole files: line endings differ and the output floods the context.
- The LM8_PUSH frame: headings `## What is attached`, `## Where this comes from`, `## Setting and notation`,
  `## Results this builds on`, `## Leads`, `## What the outcome must be` (line 110), `## Parts` (132),
  `WHAT TO DELIVER` (225) and what follows it.
- My drafts carry "Changes of the consolidation" notes at the end: their content has to be worked into the body
  (in SECTIONS_OVER_Q: the sentence "By the lead L1 below they are one question" is wrong and must go; Conjecture A
  and b) are two statements; b) with statement (G) of L19 gives A).

## State (update as I go)

- [ ] frame read  - [ ] build script written (build_prompt_20261115.py in each work folder)
- [ ] SECTIONS_OVER_Q PROMPT.md  - [ ] its zip  - [ ] lint
- [ ] ANABELIAN_SUCCESSOR PROMPT.md  - [ ] its zip  - [ ] lint
- [ ] drafts and backups moved to the work folders; `_DRAFT` folders removed when empty

## State at 15 Nov, after writing the prompts

- DONE: both PROMPT.md written by hand (02_SECTIONS_OVER_Q/PROMPT.md, 02_ANABELIAN_SUCCESSOR/PROMPT.md). Lead numbers in the prompts differ from the ITEMS_DRAFT numbering (renumbered in reading order).
- DONE: build_zips_20261115.py written (this folder); run it with python -I -B.
- TO DO: run the zip script; checkpoint_rule.apply on both PROMPT.md; lint --lint-math both until pass; move the *_DRAFT folders contents to the work folders; final message (folder, zip entries and size, lint).

## Finished, 15 Nov

- Zips built: SECTIONS_OVER_Q_background.zip 265 entries, 1,864,932 bytes; ANABELIAN_SUCCESSOR_background.zip 258 entries, 1,724,098 bytes; no PDF in either. Manifests beside the build script and in the ANABELIAN work folder.
- checkpoint_rule.apply run on both (clause placed before the disconnect section). Lint --lint-math: failing 0 for both.
- Drafts and backups moved to the two work folders; the *_DRAFT folders are gone. Upload folders hold PROMPT.md and the zip only.
- Not done: literature named "not attached" in the prompts was not fetched; the lead numbers of the prompts differ from the ITEMS_DRAFT numbers used in CONSOLIDATED_REGISTER_20261114.md.

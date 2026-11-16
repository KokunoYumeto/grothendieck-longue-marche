# The Longue Marche companion: plan sketch (16 Nov 2026, ~23:2x UTC; 17 Nov local time)

Written by Claude (Claude Opus 5.5 at effort max), main session, at the user's word:

> "feel free to plan or sketch what all goes in the Long March companion, which should, by rights, include this, since
> it's born digital" ... "or at least plan to sketch the plan for the Long March Companion together with the agents,
> because at some stage that needs to be organized as well."

It is a plan for making the plan. The outline itself is drafted with the field expert (step 3) and settled with the
user. Earlier words that bind it:
- **Successors.** "those successors, they don't have to be, literally five different successors. If they all bear on
  the same stuff, they could be one successor".
- **Expert drafting.** Experts "can also write some new prompts or draft them where necessary, or like integrate in the
  existing ones in a way that sort of like tries to put as much of the same stuff in the same place".
- **Planning ahead.** Experts "can also plan prompts for future not yet fully transcribed / written stuff that needs a
  second pass ... they can also start sketching, even if it isn't fully done".

## 1. What the companion is

The companion is the born-digital publication of everything our runs established about *La Longue Marche* and the
programme around it. That covers:
- the group schemes and the equation of loops;
- the Teichmüller tower and GT;
- the multi-Galois topoi;
- points as sections;
- the Fermat tower;
- the Lie approximations;
- the finite group actions;
- the anabelian lines;
- the tower of moduli spaces of cotes 143-148.

It is the paper of record for these results, so the paper rules hold in full (AGENTS.md, 16 Nov 2026):
- every result goes in with its complete proof, never a pointer to a repository;
- checked and unchecked results go in separate parts;
- every proof is checked before publication, and the record of each check says who checked it and how, with model,
  effort and date;
- `paper_completeness_lint.py` passes on every writing prompt.

**Born digital.** Besides the text, it carries:
- the interactive plates (the first set: `math_viz_20261116`, on GitHub in
  `grothendieck-longue-marche/visualizations/`);
- the data files and code of every computation;
- the finite certificates;
- the statement tables;
- the full provenance: each run, its prompt as sent, its checks.

## 2. What exists to build it from

- **The statement inventory.** `INVENTORY_LM_STATEMENTS_20261117.tsv` holds 3,484 statements of 19 runs, from the
  newest results table of each (2,885 proved, 289 refuted, 166 known, 137 open, 7 unresolved; all the runs' own
  claims):

  | Run | Statements | Run | Statements | Run | Statements |
  |---|---|---|---|---|---|
  | LM1 | 84 | LM2 | 79 | LM4 | 272 |
  | LM5 | 129 | LM6 | 225 | LM7 | 229 |
  | LM7_PUSH | 218 | LM8 | 167 | LM8_PUSH | 304 |
  | FLAGGED_149 | 107 | EXIT_ONE_TYPE | 63 | CYCLOTOMIC_KERNEL | 56 |
  | ANABELIAN_149_PUSH | 221 | ANABELIAN_SUCCESSOR | 157 | EXIT_TOWER | 283 |
  | SECTIONS_OVER_Q | 245 | LM4_SUCCESSOR | 280 | FERMAT_SUCCESSOR | 144 |
  | DELTA_ON_GT | 221 | | | | |

- **The checks so far:**
  - the referee reports of 14 Nov: LM7_PUSH D.44, D.50, E.58, E.61-E.67, and LM4 D.32, D.34, all proved as claimed
    (`pro_intake_20261114/referee/`);
  - the intakes (`pro_intake_20261113/`, `pro_intake_20261114/`);
  - the expert files (`pro_intake_20261114/`, `pro_intake_20261116/`).
- **The expert's reading of the newest claims:**
  - `pro_intake_20261116/EXPERT_GT_TOWER_AND_GHOSTS_20261116.md`;
  - `pro_intake_20261116/EXPERT_E49_IMPLICATIONS_20261117.md`: E.49 answers E.3, the "Moot" list, the "Referee
    tasks" list, the next questions.
- **The completion questions:** `pro_intake_20261113/COMPANION_COMPLETION_*.md`.
- **The field's handoff:** `longue_marche_pro_pilot_20261104/pro_prompts_draft_20261111_work/KNOWLEDGE_HANDOFF_LM.md`.
- **The transcription and readers:** `grothendieck-longue-marche` (readers, notes, `notes/RESEARCH_TOPICS.md`).
- **The model to follow:** `s6_pro_prompts_20261112/09_S6_PAPERS`. One GPT-6 Astra (ChatGPT Pro mode) run writes
  coherent companion papers from an inventory, with everything attached.

## 3. How it gets made, with the agents

1. **Inventory (done tonight, by script).** Next, the script adds a dependency column (which statement uses which)
   and marks superseded statements (a later run proving the same or more).
2. **Referee the load-bearing claims first.** E.44 and E.49 (the expert's ranked points 1-4), with DELTA_ON_GT A.103
   against E.49 beside them. Then the claims each part of the companion rests on. Either Claude Opus 5.5 at effort
   max referees, as on 14 Nov, or a GPT-6 Astra (ChatGPT Pro mode) check prompt; the user decides.
3. **The outline, with the field expert.** A Claude Fable 5.2 at effort max expert of the Longue Marche field drafts:
   - the parts and their order;
   - which statements go where, and which are superseded or moot (the E.49 file already lists the moot ones);
   - the dependency spine of each part;
   - which plates each part needs;
   - what is missing and needs a run.

   Candidates:
   - abbb9ceeb78661b2a, which owns the LM7 continuation items (compacted; about 650k free);
   - a rolled-back copy of a125034f at row 637 or earlier, with more room.

   The user settles the outline.
4. **One consolidated successor (not five).** One GPT-6 Astra (ChatGPT Pro mode) prompt that pushes what the companion
   still lacks:
   - the referee items I1 (E.44, E.49: where the pentagon is used) and the finite check of E.49 (the level at which
     every pentagon shadow has parity zero);
   - I4 (the involutions of GT-hat by E.44's method);
   - I5 / G1 (a ghost surviving the whole pronilpotent tower has finite support);
   - DELTA_ON_GT A.84 and B.33 against EXIT_TOWER E.49 and B.25;
   - EXIT_TOWER's open E.24, E.45 and E.T3;
   - the expert's next questions (does §47 imply the pentagon; which finite quotients of GT-hat_0 see it);
   - the open items of LM4_SUCCESSOR (A) and (B).

   The expert drafts it, it is linted (`--lint-math`), and it goes out at night. Items for folders not yet
   transcribed are sketched now and filled in when their transcription lands (the user, 17 Nov).
5. **The writing run.** As with 09_S6_PAPERS: one Pro run, given the inventory, every return's TeX, the checks, the
   expert files and the readers, writes the companion volumes coherently. Checked and unchecked go in separate parts,
   and every proof is in full. It is split into several runs only if one cannot hold it.
6. **The plates.** Claude (main session) makes one plate set per part, from the runs' data, in the style of the first
   set.

## 4. Timing

On 16 Nov ~23:2x UTC weekly usage stood at 90 % (all models) and 60 % (Fable); both reset 18 Nov 07:00 UTC. So the
agent steps (3, 4, and step 2 if it uses Claude referees) run after the reset. Step 1's dependency column and the
plates can go on before then.

## 5. For the user to decide

- The referees for E.44 and E.49: Claude Opus 5.5 at effort max, or a GPT-6 Astra (ChatGPT Pro mode) check prompt.
- The expert for the outline: abbb9cee, or a rolled-back copy of the LM expert.
- Scope: whether the companion takes in EXIT_TOWER, the tower of cotes 143-148, which goes beyond the 1981 manuscript.
  The proposal is yes, as its own part.

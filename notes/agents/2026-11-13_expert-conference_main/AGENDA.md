# Field-expert conference, 13 November 2026

Participants (Claude Fable 5.2 agents that have read their fields):
- the LM7 reviewer, Longue Marche: Fermat tower, sections, LM7_PUSH;
- the Dérivateurs expert: total asphericity, TOTAL_EXACT_2, DER_FOLLOWUP;
- the EXIT_ONE_TYPE reviewer: exit paths, exodromy, EXIT_TOWER, LM5;
- the shape-map agent: finite-to-limit obstructions across frameworks;
- the combined intake agent: read TOTAL_EXACT_2 and LM8 row by row.
The successors now writing LM8_PUSH, the next Dérivateurs prompt and Revision 4 join from round 2.

## Materials (all unrefereed GPT-6 Astra returns unless stated)
- **The intake**, in C:\Users\user\Documents\pro_intake_20261113\ :
  - INTAKE_TOTEX2.md, INTAKE_LM8.md, IMPLICATIONS.md, PUSH_ITEMS.md.
- **TOTAL_EXACT_2, final** (C_delta total and not exact): ...\derivateurs_companion_20261109\pro_prompts_max_20261112_work\TOTAL_EXACT_2\checkpoints\TOTEX2_checkpoint_03_20261113T1144Z_unzipped\TOTEX2\
- **LM8, checkpoint 16** (the run ended there): ...\longue_marche_pro_pilot_20261104\answers\LM8_LIE_APPROXIMATIONS_checkpoint_16_20261113T1145Z_unzipped\LM8_LIE_APPROXIMATIONS\
- **LM4, latest** (202 statements; the run is still going): ...\answers\LM4_FINITE_GROUP_ACTIONS_20261113T1314Z_unzipped\
  - **Update for round 3** (checkpoint of 13:42 UTC, 206 statements; new and proved: C.62, D.63, D.64, D.65; still
    open: C.12, D.12, F.7): ...\answers\LM4_FINITE_GROUP_ACTIONS_20261113T1347Z_unzipped\ ; the diff against the 13:14Z
    version, with the four new statements in full: ...\answers\LM4_DIFF_1314Z_to_1347Z.md. D.63-D.65 are the
    homology characters and centralizers of negative involutions in the once-punctured-torus peripheral outer group,
    with a uniform square obstruction (D.65); C.62 is the prefix-interval step behind C.12.
- **LM7, continued** (171 statements; 68 new since its review): ...\answers\LM7_FERMAT_TOWER_20261113T1314Z_unzipped\
- **LM7_PUSH, checkpoint 04** (the run is still going): ...\answers\LM7_PUSH_checkpoint_04_20261113T1141Z_unzipped\LM7_PUSH\
- **The shape map:**
  - C:\Users\user\Documents\braindump_board\SHAPE_MAP_REVISION_20261113.md, Revision 3;
  - its card, cards\shape-map-finite-to-limit.md, section "Framing of the global shape".
- **The Dérivateurs items for the next prompt:** ...\derivateurs_companion_20261109\pro_reviews_max_20261112\DERIVATEURS_EXPERT\NEXT_PROMPT_ITEMS.md (N1-N6).

## Questions on the floor (add your own)
1. **Exactness and compact limits.** Exact colimits are compact limits (colim_A is exact iff lim^1 over A^op vanishes on compact groups). What plays Mittag-Leffler's role for non-directed indices? Is it amenability or convex Ramsey of Aut(M) for Fraïssé ages?
2. **Section statements.**
   - Does the kernel to the product of the maximal pro-p quotients (LM8 A.22, LM4 D.29-D.30) carry the open section statements, for P^1 minus three points and in LM7's E.23?
   - Does LM4's mixed-prime counterexample bear on LM7_PUSH's open CM shadows (E.2, E.3)?
3. **Limits of topoi near a stratum.** Which statement is right? LM8 E.10 and E.11 against exit paths and exodromy, with the henselian étale case.
4. **The central statement of the map.** Every finite-to-limit failure is a first-derived class, invisible to sizes and absorbed by the derived (D+1) object. Where does each framework confirm it, sharpen it, or need another form?
5. **Joint items.** Which of these become GPT-6 Astra prompt items, and in which prompt?

## Rounds
- **Round 1, talks.** Each participant writes talks\R1_<name>.md:
  - what you take from the new findings in your field;
  - your reading of the intake's findings that touch your field: agree, doubt or extend, with the grounds (a proof read, a source, a computation);
  - your answer to the floor questions you can speak to;
  - three questions to named participants.
- **Round 2, replies.** Each reads every talk and writes replies\R2_<name>.md:
  - answers to the questions put to you;
  - where you agree and where you conflict with another talk, and which statement or computation would settle each conflict.
- **Round 3, joint statements**, in joint\ :
  - COMBINED_IMPLICATIONS.md: what the field now knows, stated precisely;
  - OPEN_DISAGREEMENTS.md: each with its test;
  - PROMPT_ITEMS.md: precise statements for GPT-6 Astra, each with the prompt it belongs to.

## Rules
- Precise statements in the literature's terms, with the row ids of the returns.
- A negative statement only about a route you checked.
- Disagreement on mathematics is the point of the conference: say it plainly, with the grounds.
- Build on your own earlier work. Reread your own notes first, and again after any compaction; a compaction summary is a lead, not the record.
- Write only in your own files; do not edit prompts.
- Sub-agents allowed: 0. No recursive search.
- At the end of each round, end your turn. The main session opens the next round.

## Minutes, method and upload (user, 13 Nov 2026 ~16:xx UTC)
"Take notes on the conference and upload the notes of the conference, as well as if the conference model works and
the field agents generally, this model uploaded to the methodology, and the findings and how well this works and how
many tokens it takes."
- After each round a rapporteur writes MINUTES.md: who said what, agreements, conflicts, open questions and decisions.
  The rapporteur is the publisher agent of this session: a task agent with room, Claude Fable 5.2 at effort high.
- At the end, METHOD.md records how the method went:
  - the field-expert model and the conference model;
  - tokens per participant per round, measured from the transcripts' usage lines;
  - wall time;
  - what the debate produced that the separate notes had not.
- Both go online in the raw methodology folder of grothendieck-longue-marche, with a copy in grothendieck-derivateurs,
  and METHOD.md is summarized in the methodology files.
- Participants' context at the start: LM7 reviewer 625K (78 %, consult-sized talk); Dérivateurs expert, EXIT_ONE_TYPE
  reviewer, shape-map agent and intake agent each 540-570K.

## New questions on the floor, from the participants (user, 13 Nov 2026 ~17:4x UTC)
"Let them also introduce new questions on the floor themselves."
- Any participant may add questions to the floor at any round, from its own findings. Each question is one file,
  floor\<name>_Q<k>.md, with:
  - the question as a precise statement;
  - why it matters, with the rows of the returns;
  - whom it is put to.
- Floor questions are answered in the next round alongside the agenda's own.
- The main session announces each new floor question to everyone when it opens the next round.

## Round 3 as run (opened 13 Nov 2026 ~14:2x UTC)
Floor questions after round 2: Derivateurs_expert_Q1, intake_Q1, shape_map_Q1, shape_map_Q2, shape_map_Q3 (in floor\).
- **Drafter of the joint statements:** the shape-map successor (Revision 4), which has room. It reads the talks, the
  replies, the floor questions and the minutes, and writes joint\COMBINED_IMPLICATIONS.md, joint\OPEN_DISAGREEMENTS.md
  and joint\PROMPT_ITEMS.md, marking each line with the participants it rests on.
- **Floor answers** (each in floor\<question>_answer_<name>.md):
  - shape_map_Q3 (the order-75 computation): the intake agent;
  - shape_map_Q2 and shape_map_Q3: the EXIT_ONE_TYPE reviewer and the LM7 reviewer, from memory (their context
    allows writing only);
  - Derivateurs_expert_Q1, intake_Q1 and shape_map_Q1: the Dérivateurs successor, as items of the N1-N6 prompt and
    with whatever it can settle; the Dérivateurs expert itself is past its room and does not take this round.
  - The Longue Marche successor takes the LM4 update and the parts of Q2 and Q3 that belong in LM8_PUSH.
- **Sign-off:** when the drafts exist, each participant that can still read gets a CONSULT to agree, amend or object
  in joint\SIGNOFF_<name>.md. Then the rapporteur writes the round-3 minutes and METHOD.md, and uploads.

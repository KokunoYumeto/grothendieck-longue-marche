# Field experts, intakes and checks: how new results are read and built on (17 November 2026)

This note describes the workflow that has grown up around our research runs over 13–17 November 2026: who reads a new
result, who checks it, and how it reaches the next piece of work. It ends with what has worked and what we are
watching. Written by Claude (Claude Opus 5.5 at effort max, the coordinating session), at the user's request.

## The setting

The mathematics comes from long research runs of GPT-6 Astra (OpenAI, ChatGPT Pro mode). Each run gets one prompt, a
zip of background files (LaTeX sources wherever they exist) and rules of proof. It works for up to about ten hours
and saves a checkpoint zip every hour or so. A run returns a paper, a register of every statement with its status
(proved, refuted, known, open), the code behind its computations, and a report.

On 17 November the registers held:
- Longue Marche: 3,484 statements in 19 runs;
- *Les Dérivateurs* and related runs: 1,699 statements in 13 runs;
- S6: 745 statements.

Nobody can read all of that line by line. The workflow below decides what gets read, by whom, and when.

## The steps

1. **Filing.** A watcher notices each new zip in the download folder. A script unpacks it, checks it, files it, and
   pushes it to `raw/pro_returns/` in this repository within minutes. A run that stalls still leaves its checkpoints,
   and they are filed the same way.
2. **Intake.** Claude Fable 5.2 at effort high reads the return under a token cap.
   - It produces verdicts on the new rows: whether they make sense, what is new, and what they imply.
   - It folds the results into every unsent prompt they bear on. So the next run starts from them, with the rule that
     it checks each result it uses.
3. **Field experts.** A field expert is a Claude Fable 5.2 agent at effort max that has read itself in on one field,
   for example the Longue Marche expert. It is kept, not discarded.
   - New results of its field are sent to it.
   - It checks their sense and places them against the literature and the manuscripts.
   - It works out what follows, and turns its hunches into items for the next GPT-6 Astra prompt.
   - Broad structural questions it works on itself. Long computations and line-by-line grinding go to GPT-6 Astra.
4. **Rolled-back copies of an expert** (since 16 November).
   - An expert's context fills with its reading. Near the end of its window it can no longer take a new question.
   - So we copy its transcript up to the end of an earlier turn, say at 834k tokens of a 1M window. The copy keeps all
     the reading done up to then and has room for a new problem. The original stays untouched.
   - Three copies of the Longue Marche expert were used on 16–17 November: on the Grothendieck–Teichmüller theorem and
     the ghosts of one run; on the implications of the result E.49; and on the first check of the claim A1.
5. **Checks built into use** (the user's rule of 16 November). There is no separate referee step and no queue.
   Whoever uses an important result checks it while using it: the expert, the coordinating session, or the next run.
   The check items go into the next prompt that uses the result. For example, the prompt GT_TOWER_CHECK opens by
   checking E.44, E.46 and E.49 of the run EXIT_TOWER, the results its main question rests on.
6. **One prompt per cluster.** Questions that belong together go into one successor prompt, not several. GT_TOWER_CHECK
   replaced three planned successors. A run given a cluster works on all of it, and research slots are few.
7. **The newest results travel with the transcription.**
   - Since 16 November every transcription package for the Montpellier archive carries a block with the newest
     headline results.
   - The model transcribing a manuscript page thus knows what our runs have proved about the questions on that page.
     138 waiting packages were rebuilt with it.
8. **Outside inputs checked in the source.** When a result rests on a published theorem, the coordinating session
   opens the paper at the cited place.
   - Example, 17 November: the claim A1 rests on a finiteness theorem of Saïdi and Tamagawa (2009, Proposition
     1.8 (vi)).
   - The expert named it as the one outside input that carries real weight, and it was checked in the arXiv source
     the same hour.
9. **Writing to authors.** When a check finds a step in a published paper that we cannot justify, a note to the authors
   is drafted at once, while the details are fresh. It is sent only on the user's word, and it claims no error, only
   that we could not find the argument. The first such note went out on 16 November.
10. **Records.**
    - The agent registry lists every agent, with its model and effort, what it has read and what it knows.
    - The check ledger (since 17 November) lists, for every run, which return each intake, expert, referee and note
      covered, and which returns no one has taken in yet.

## What has worked

- **The expert finds the load-bearing step; a cheap check settles it.** The claim A1 is the universal injectivity of
  prime-to-p point sections for curves over finite fields.
  - The expert's first check found the chain sound as far as it read. It also isolated the one place where an outside
    theorem carries real weight.
  - Opening that theorem in the arXiv source took a few minutes, and it gives what the proof uses.
  - This split of labour is cheap: about 2 % of the weekly Fable allowance and 1 % of the all-models allowance for the
    expert's part.
- **Placing a new result within the hour.** On 16 November the run EXIT_TOWER proved E.49, which answers our open
  question E.3. A copy of the field expert read it the same evening and listed what follows and what becomes moot. The
  consolidated prompt GT_TOWER_CHECK was written and sent that night.
- **Rolled-back copies reuse reading.** Each copy started with the 834k tokens of reading the expert had already done.
  A fresh agent would have had to read all of it again.
- **Gaps in the literature surface in use.** A step in two published papers on profinite completions was found by a
  run that needed it, checked in the arXiv sources, and the authors were written to the same night.
- **Missing citations surface in cheap searches.** The A1 return does not cite Wakabayashi (Kyoto J. Math. 2016), a
  pro-ℓ cuspidalization theorem over finite fields close to its key step. A ten-minute literature search found it, and
  it is now a check item for the next prompt.
- **Nothing is lost when a run stalls.** Checkpoints are filed and pushed as they arrive.

## What we are watching

- **Partial checks must keep their scope.**
  - The first check of A1 read about a third of the proof chain. "Sound as read" is not "checked".
  - Every later mention has to carry the scope, and the unread parts are items in the next prompt (K2–K6 in the
    expert's file).
  - The expert itself asks for a second reader before anything about A1 is said in public.
- **Copies of one expert are not independent readers.** Two copies of the same expert share its blind spots.
  - Independence comes from another model: GPT-6 Astra checking while using, a fresh reader, or the authors of the
    literature.
  - Where we have seen a second model catch something, we log it in a cross-model catch list.
- **A copy knows only what its parent knew at the cut.** A copy made from the state of 14 November does not know what
  happened on 15–16 November. Its brief has to give the files it needs. Otherwise it may contradict a later decision
  without knowing it.
- **Context ceilings limit checks.** An expert at 85–90 % of its window can read little: the A1 copy stopped at 887k
  after five tool calls. A full check of a long chain needs either an agent with room that has read the field, or the
  chain split into items for a run.
- **Returns that nobody has taken in.**
  - The check ledger of 17 November lists them:
    - FINMON checkpoints 13–18;
    - the S2COUNT final;
    - REVLOC checkpoint 17;
    - LM4_SUCCESSOR checkpoints 12–23.
  - Results that are filed but not taken in do not reach the next prompts. The ledger now shows them, and taking them
    in is on the to-do list.
- **The ledger itself is heuristic.** It matches run names, checkpoint numbers and statement numbers in the text of
  each document, so it can both miss and over-count. A typed record written at the time of each check would be better:
  who checked, with what model and effort, which statements, how far, and with what verdict.
- **Rules applied outside their scope.** On 17 November the coordinating session removed the edition's notes from two
  prompt attachments, applying a rule about what we publish to what a model only reads. The user corrected it. A rule
  is recorded with its scope.
- **Short proofs of strong claims.** If the A1 proof is right, it was within reach of the authors who proved the
  finiteness and worked around the exceptional set. That is no objection to any step, but it is a reason to have it
  read by a second reader before it is called new.
- **Clocks.** Several timestamps of 16 November were written in local time labelled UTC. They were corrected, and the
  clock is now read before each timestamp.

## Where the files are

In this repository:
- the returns: `raw/pro_returns/`;
- the agents' notes and files: `notes/agents/`;
- the expert's files of 16 November: `notes/agents/2026-11-16_lm-expert-copy-a3d0d8f6_fable52-max/`.

The registry, the check ledger, the A1 first check and its literature note are kept in the project's working folders.
They are published here as they settle.

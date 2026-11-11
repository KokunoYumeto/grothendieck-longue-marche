# Are the new prompts softer? Audit of 11 Nov 2026, and the standard that follows from it

Asked by the user, 11 Nov 2026 (P3185-P3187): "do an audit of the new prompts against yesterday's prompts. Check if
this new fable agent isn't being way too soft in the way it asks these, to be completed ... The AI won't do more work
than it's asked to do." Audit by Claude (Opus 5.5), 13:35-13:50 UTC.

## Findings

1. **The shared rules are not softer.** The common block of the Longue Marche prompts (LM1-LM8) and that of the
   Dérivateurs prompts (1-7) say the same about effort: "This task is long by design. Work through all parts
   completely; do not stop at an outline, a sample or a plan ... Ignore any clock", complete proofs, every statement
   labelled Proved / Refuted / Known / Open. The LM block adds "find the strongest true statement in its place" and
   "carry it to where it stops; it is not a survey". It lost one clause: "Never write it up as proved, and never drop
   it" (rule 9).
2. **The task lists of the LM prompts ask for less.** The parts of LM1-LM3 are 269-360 words with 9-10 demanding
   verbs (prove, decide, construct, compute ...); those of the Dérivateurs prompts are 424-782 words with 14-19.
   Their wording asks for status more than for mathematics. LM3: "what is proved in the literature ..., what is open"
   (B); "cite or prove, and say exactly what remains" (D); "the known inclusions ..., with proofs or citations; which
   ... are theorems ... and which are open ... give the status of each" (E); a table of definitions (A). Against
   4_GALOIS: "Prove or refute that each is a fundamental localizer ... Decide accessibility. Decide which of ...
   axioms"; "Complete proofs for: sets; groupoids; n-types; spaces; D(k) ...; spectra; K(n)-local ... as far as you
   can"; "Construct D′ ... or show what obstructs". The LM wording lets "Known, see [ref]" and "Open" count as
   answers.
3. **The returns show it.** BISITE (a Dérivateurs prompt, returned today) is the largest return so far: 126
   statements (72 Proved, 32 Refuted, 18 Known, 4 Open), 38,645 words of TeX, 75 code files. LM3 has about the same
   volume (110 statements, 33,496 words), but 30 Known (27 %) and 12 Open (11 %) against 10-18 Known (12-17 %) and
   2-6 Open in the seven Dérivateurs returns, and 12 code files against 33-83.

| Return | Statements | Proved | Refuted | Known | Open | TeX words | Code files |
|---|---|---|---|---|---|---|---|
| 1_CATHOT | 90 | 59 | 14 | 11 | 6 | 30,567 | 83 |
| 2_TOTAL_ASPHERICITY | 107 | 84 | 11 | 10 | 2 | 27,964 | 44 |
| 3_POLES | 104 | 75 | 14 | 13 | 2 | 35,229 | 69 |
| 4_GALOIS | 74 | 52 | 7 | 10 | 5 | 32,828 | 40 |
| 5_STRATA | 81 | 54 | 9 | 14 | 4 | 26,580 | 47 |
| 6_PATHS | 76 | 40 | 19 | 11 | 6 | 28,361 | 33 |
| 7_BISITE | 126 | 72 | 32 | 18 | 4 | 38,645 | 75 |
| LM3_TEICHMULLER_TOWER | 110 | 57 | 11 | 30 | 12 | 33,496 | 12 |

Part of the difference is the subject (the Grothendieck-Teichmüller and anabelian questions have a large literature
and famous open problems), but the wording points the same way. So the impression was right for the LM prompts and
wrong for BISITE. LM1 and LM2 (sent overnight) have the same kind of task list as LM3.

## Rule 0: every prompt states its outcome (user, 11 Nov 2026, P3193)

"make a clear rule about prompting needs to be very, very clear about what the outcome needs to be." This applies to
every prompt: Pro prompts, API batches, Codex tasks, Fable and other subagent briefs, and transcription packages.

Each prompt has a section "What the outcome must be", placed before the parts. It states:
1. **The deliverables:** the files, their names and form, with one row per item and its status.
2. **What counts as done for each item.**
   - For mathematics, one of:
     - (a) proved, in his form or in its strongest correct form, with a complete proof;
     - (b) refuted by a complete counterexample, checked by program when finite, with the strongest true statement
       in its place, proved;
     - (c) partly settled: the cases proved, the computations run, and the obstruction stated exactly, with the
       smallest undecided instance.

     "Known" counts only together with the derivation of his statement from the cited theorem.
   - For transcription: every element of every page transcribed, with each page's row marked complete = yes.
3. **What is not acceptable:**
   - a survey or a status report;
   - "open, see [reference]";
   - a plan, a sample or an outline;
   - a summary of what would be done;
   - an item dropped without a row.
4. **When the work is finished:** only when every item meets the bar. Anything short of it is reported as unfinished,
   item by item.

5. **If the execution environment disconnects** (user, 11 Nov 2026, after three Pro runs lost their workspaces):
   - wait for it and retry for at least 10 minutes;
   - if it does not come back, write the work out in the chat as text: every file in full, each in its own code
     block headed by its file name, taken from the code that saved it;
   - then continue the work in the chat as far as possible;
   - an answer that only reports the disconnection or asks for the files again is not acceptable.

   The user copies the chat output into Claude Code, and Claude rebuilds the files. Wording per prompt type:
   archive Method step 6; LM outcome item 5 (`outcome_block.py`); Gelfand `PROMPT_TEMPLATE.md`.

Check this section before anything is packaged or sent.

## The push standard (applies to every new or revised Pro prompt)

1. Every part asks for mathematics with a verb that produces it: prove, refute, decide, construct, compute,
   classify. "Survey", "list what is known", "give the status", "cite or prove", "say what remains" are never a task
   on their own.
2. Known results are cited with theorem numbers and then used: derive his statement from them in the form he states
   it, with the proof of the reduction. A row "Known [reference]" without that derivation is unfinished.
3. Open items are not end points. For each: prove the strongest partial result within reach (the cases he names, the
   smallest cases, pro-ℓ, metabelian or abelianized versions, or under one extra hypothesis named exactly), compute
   evidence by program, refute a stronger form, or isolate the obstruction as an exact statement with the smallest
   undecided instance. The row records what was tried.
4. Say how far: "as far as you can", "carry each to where it stops", and what counts as done (a theorem with proof, or
   a counterexample checked by program).
5. Nothing implies that less output suffices: no "briefly", "a table of", "status", "need not", "at most", except to
   exclude something done elsewhere, and then say where.
6. Ask for programs wherever a computation can decide or test a case (finite groups, small types, explicit covers).
7. The parts fill the run: the run is long by design, so the list of asks is long enough for it.

Clause added to the LM common block (rule 9 and a new rule 10), for every LM prompt not yet sent:
"9. What you cannot settle stays on the page as an exact statement, with what you tried, the step that fails and the
smallest undecided instance. Never write it up as proved, and never drop it.
10. Known and Open are not end points. A Known statement is derived from the cited theorem in the form he states it,
with the proof of the reduction. An Open statement records your own attack: the strongest partial result you proved,
the computations you ran, the obstruction as an exact statement. A row 'open, see [reference]' without your own
attempt is unfinished."

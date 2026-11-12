# La Longue Marche expert line (redo of 12 Nov 2026): knowledge handoff

Kept by the field expert for Grothendieck's *La Longue Marche à travers la théorie de Galois* and the research prompts
on it (LM3, LM3b, LM4–LM8). Model and effort of every section's author are named in its heading. A successor reads this
file in full first, then `GROTHENDIECK_NOTES.md`, then `READING_BASE.md`, then what the step in hand needs.

Base folder: `C:\Users\user\Documents\longue_marche_pro_pilot_20261104`. Everything of this line is written in
`pro_reviews_max_20261112\` (`LM_EXPERT\`, `LM3\`, `LM3b\`, `PUSH_REDO\`; scratch in `LM_EXPERT\work\`), except step 5,
which edits the five unsent prompts in `pro_prompts_draft_20261111_work\<name>\PROMPT.md`.

## 0. The task, as given (launch brief of 12 Nov 2026, about 12:20 UTC)

The method, in the user's words: "they will read the appropriate literature before making comments, and then they will
be asked to think about it at max effort. And they will also have to reread every single one of those returns and
consider them." And: "Remember how the first one read the entirety of the Long March transcription before starting ...
Read the math, then work on the topic. Not YOLO."

1. Grothendieck first. Read La Longue Marche in order, in full, as far as the context allows. Current text per package:
   `second_pass\LM_<KEY>_checked_fixed.tex`, else `second_pass\LM_<KEY>_checked.tex`, else the first pass in `answers\`.
   Keep `LM_EXPERT\GROTHENDIECK_NOTES.md` as you go (structure, definitions, results, conjectures, open questions, scan
   locations).
2. Literature: primary sources of the field (Drinfeld, Ihara, Deligne's "Le groupe fondamental de la droite projective
   moins trois points", Nakamura, Schneps, Lochak, Hatcher–Lochak–Schneps, Pop, Mochizuki, Tamagawa, and what each
   return cites). The primary texts themselves; freely accessible copies only. Write `LM_EXPERT\READING_BASE.md`:
   source, location, statements relied on with full hypotheses, what could not be obtained.
3. Review LM3 from scratch: prompt `pro_prompts_draft_20261111\LM3_TEICHMULLER_TOWER\`, return
   `answers\LM3_TEICHMULLER_TOWER_2026-11-11.zip` (unzip into the work folder; read its code, do not run it; write and
   run own checks). Every item: verdict (correct / wrong / gap / unproved) with own proof, counterexample or exact
   citation; attack what it leaves open; record anything new. Output `LM3\REVIEW.md`.
4. The same for LM3b: `pro_prompts_draft_20261111\LM3b_TEICHMULLER_PUSH\`, `answers\LM3b_TEICHMULLER_PUSH.zip`. Output
   `LM3b\REVIEW.md`.
5. Redo the rewrite of the five unsent prompts LM4_FINITE_GROUP_ACTIONS, LM5_MULTI_GALOIS_TOPOI, LM6_POINTS_AS_SECTIONS,
   LM7_FERMAT_TOWER, LM8_LIE_APPROXIMATIONS (work tree `pro_prompts_draft_20261111_work\<name>\`). The "push rewrite" of
   11 Nov is void. Start from `<name>\PROMPT_before_push_20261111.md`; keep the later changes that were not part of it
   (the disconnect clause of 11 Nov: compare `PROMPT_before_disconnect_clause_20261111.md` with the next state; for LM4
   the second-pass edits of 12 Nov: `CHANGES_20261112_*.md` and `PROMPT_before_second_pass_20261112.md`). Rewrite each
   prompt's Parts so that they demand mathematics (proofs, constructions, computations, refutations, attacks on open
   items, exact pointers into the transcription; never status reports or "cite or prove"). Standard:
   `pro_prompts_draft_20261111_work\PUSH_STANDARD_AND_AUDIT_20261111.md`. Each prompt says what counts as done per item,
   what is unacceptable, when it is finished. Before overwriting a `PROMPT.md`, copy it to
   `PROMPT_before_redo_20261112.md` beside it. Record changes in `PUSH_REDO\RECORD.md`. No ZIPs; do not touch the upload
   folders in `pro_prompts_draft_20261111\`.
6. Keep this file current.

Do not open (discarded work): `pro_prompts_draft_20261111_work\KNOWLEDGE_HANDOFF_LM.md`,
`pro_prompts_draft_20261111_work\PUSH_REWRITE_RECORD_20261111.md`, anything under `pro_reviews_20261111\`, any other
review of LM3 or LM3b.

Done when `LM3\REVIEW.md` and `LM3b\REVIEW.md` give every item a verdict with an argument, the five prompts are
rewritten with the record, and `READING_BASE.md`, `GROTHENDIECK_NOTES.md`, `KNOWLEDGE_HANDOFF.md` exist. Unacceptable: a
verdict without an argument; labels copied from a return; taking a return's word for what a source says; working on a
topic before reading the Grothendieck passages it concerns. If the context runs low: finish the step in hand, update
this file, say exactly where you stopped. Final message: for LM3 and LM3b the number of items per verdict and the most
important findings; then, per prompt, what its Parts now demand.

### Additions from the coordinator while the work ran (12 Nov, 12:25–12:31 UTC), all to be honoured

A. Many conjectures pertinent to this work were resolved recently, a good part by OpenAI's models, after the training
   cutoff. Before calling anything open or known, read `C:\Users\user\Documents\recent_results_20261110\`
   `SCOREBOARD.md`, `RECENT_RESULTS.md`, `BRIEF_FOR_PROMPTS.md`, `OPENAI_MATH_INVENTORY.md` (skip the .json; do not open
   `proof_packs\` or any .lean file), and search arXiv and the announcements for 2026 results in the field, since the
   scoreboard dates from 10 Nov. Everything used goes into `READING_BASE.md` with date and location. The rewritten
   prompts must not ask GPT-6 Astra to prove what is already settled, and should use what is settled.
B. Required reading named by the user, in the papers themselves (the mathematics, not the Lean): family 008, the
   Deligne–Drinfeld conjecture (grt_1 free on one generator in each odd weight >= 3; claimed 23 Sep 2026; with Brown's
   theorem it makes grt_1 the motivic Lie algebra of MT(Z)); family 019, the section conjecture (local p-adic case for
   proper curves of genus >= 2; global case for X_0(N), X_1(N) over Q; 6 Oct); family 009, Bogomolov–Pop
   reconstruction (transcendence degree >= 2); family 031, Uchida's Hom-form of Neukirch–Uchida. `RECENT_RESULTS.md`
   (links L1, L1q, L2, L2q, L3) says how each bears on La Longue Marche and the Esquisse. Treat them as claimed,
   unrefereed results: check what is used. The LM3/LM3b reviews and the LM4–LM8 prompts must take them into account.
C. The papers are on disk: `C:\Users\user\Documents\recent_results_20261110\papers\`:
   `008_The-Deligne-Drinfeld-conjecture-September-23-2026.pdf`; `019_The-p-adic-section-conjecture-October-6-2026.pdf`
   and `019_Etale-covers-with-a-prescribed-exterior-sheet-September-24-2026.pdf`;
   `009_The-Bogomolov-Pop-reconstruction-theorem-September-23-2026.pdf` and the two 009 Milnor K-theory papers;
   `031_Open-Homomorphisms-of-Global-Solvably-Closed-Galois-Groups-October-5-2026.pdf`. Do not open `proof_packs\`.
D. From the user, for the LM4–LM8 prompts: "Make sure to check the prompting too. For requesting that ProMode push the
   math, not just comment on the math. That was a previous error." Each Part must ask GPT-6 Astra (effort Pro) to do
   mathematics (prove, construct, compute, refute, attack the open items with a stated target), never to describe,
   summarize, classify by status or comment. Before finishing, reread every Part of every prompt against that test and
   against `PUSH_STANDARD_AND_AUDIT_20261111.md`, and record the check in `PUSH_REDO\RECORD.md`.
E. Required reading from the user: the board card `C:\Users\user\Documents\braindump_board\cards\reading-list.md`
   lists, per topic, the recent results and our own results (`C:\Users\user\Documents\grant_evidence\EVIDENCE.md`; the
   results registers of the returns) to know while reading, as claims to check. Read it after the Longue Marche and
   before the returns.

F. Note on the recent-results files (coordinator, between 12:31 and 12:46 UTC): `RECENT_RESULTS.md` and `BRIEF_FOR_PROMPTS.md` (and
   the scoreboard's "bears on our work" column) were written by a Claude Fable 5.2 agent at effort medium. Use them
   only as pointers to the papers; read the papers themselves (`recent_results_20261110\papers\`) and form an own view
   of how each bears on La Longue Marche. The LM1-LM3 prompts were also framed by medium-effort agents; the returns
   themselves are GPT-6 Astra's work at effort Pro.

## 1. Section by Claude Fable 5.2, effort max (agent abe2444c773a49d2a, started 12 Nov 2026, 12:22 UTC)

### 1.1 Working facts

- The manuscript in packages, in order (116 files): `LM_EXPERT\work\READING_ORDER.tsv` (number, key, source file).
  Cote 140-2 = files 001–058 = Part I, §§1–37, ms pp. 1–292. Cote 140-3 = files 059–099 = Part II "Variations sur
  l'équation des lacets", §§38–49, ms pp. 291–650. Cote 140-4 = files 100–114 = §§50–53 (schematic envelopes; the
  Fermat tower §51; Lie approximations of Galois–Teichmüller systems §52; the special Teichmüller group ST_{1,1} §53),
  ms pp. 650bis–787. Cote 140-1 = files 115–116 = the draft (37 scans).
- Reading copies: `LM_EXPERT\work\reading2\NNN_<KEY>.txt`, made by `work\compact.py` + `work\trim_reading.py` from the
  current text of each package. They keep every word and formula; the diplomatic macros are shortened
  (`x(?)` = unsure reading, `{a|b}?` = alternative readings, `[illeg n]`, `<<...>>` = deleted text longer than 30
  characters (shorter deletions dropped), `[mg: ...]` = margin, `_x_` = underlined, `=====SCAN N=====`, `[p.N]` = his
  page number). Quote from the source .tex, not from a reading copy.
- Sizes: 140-2 767 KB, 140-3 1,243 KB, 140-4 436 KB, 140-1 67 KB of reading copy; measured 3.4 bytes per token, so
  about 226k + 366k + 128k + 20k = 740k tokens for the whole manuscript. The context window is 1M (auto-compaction of
  earlier agents at about 966k). This agent started the reading at about 170k.
- Own context can be measured: `python work\ctx.py` (reads this agent's transcript; a successor must change the
  transcript path in it).
- Scripts with backslashes are written with the Write tool, never through a Bash here-document (it eats backslashes).
  Printing through Python mangles accents on this console; read with `cat`/`head -c`/`sed -n`.

### 1.2 State (updated at each checkpoint; newest last)

- 12 Nov 12:31 UTC: folders made; reading copies built; reading of cote 140-2 starts at file 001.
- 12 Nov (time not read from the clock): files 001-011 read (2:sc1-110, pp. 1-53, §§1-12 and the start of §13); notes written up to there.
- 12 Nov (time not read from the clock): CORRECTION of the size estimate in 1.1: measured on the transcript, the reading copies cost about
  1.8 bytes per token (LaTeX-heavy French), not 3.4. So cote 140-2 is about 425k tokens, 140-3 about 690k, 140-4 about
  240k, 140-1 about 37k: the whole manuscript is about 1.4M tokens and cannot be read inside one 1M context. Thinking
  blocks also stay in the context during a tool loop. Consequence for this agent: Part I (cote 140-2, §§1-37) is read
  in full, in order, with notes; it holds every passage that LM3 and LM3b point to (their prompts name §§19, 21, 26-30,
  32-36 and §§30-33bis; §§38-53 only as context) and the passages of LM4, LM5, LM6. Parts II-IV (cotes 140-3, 140-4,
  140-1) are left for a successor, who needs them in full before LM7 (§51) and LM8 (§52) are touched.
  Files 012-015 read (2:sc111-150, pp. 54-74: §13, §13bis, §14, start of §15).
- Coordinator addition G (time not read from the clock), from the user: keep a running list `LM_EXPERT\FINDINGS.md` of every
  potential finding and implication noticed (new results, sharpenings, consequences for Grothendieck's text, connections
  to the Dérivateurs returns or to recent results), even small ones. Only after the own LM3 and LM3b reviews are
  complete, open the earlier reviews (`pro_reviews_20261111\LM3_TEICHMULLER_TOWER\` and any LM3b review there; written
  at effort medium) and add to FINDINGS.md a section "Compared with the earlier review": what they missed, where they
  were wrong or too weak, where they were right. The ban on those files is lifted only for that comparison and only
  after the own reviews are done.
- Coordinator addition H (time not read from the clock), the purpose of the work, from the user: build mathematics prompts for
  GPT-6 Astra (effort Pro) from what is read and found, besides the LM4-LM8 rewrite. Two kinds: (1) a result proved
  outright by the expert: write it up fully and draft a prompt asking GPT-6 Astra to check it and push it further;
  (2) hunches (suspected, not proved): record each in `LM_EXPERT\HUNCHES.md` with reasons, and draft prompts asking
  GPT-6 Astra to prove, refute or develop them, or fold them into the Parts of LM4-LM8 where they belong. New drafts
  go in `LM_EXPERT\PRO_PROMPTS\<short-name>\PROMPT.md`. Every prompt pushes the math, states exactly what counts as
  done, what is unacceptable and when it is finished, and points to the exact scans of the transcription. Later the
  three experts (CATHOT, Les Derivateurs, La Longue Marche) read each other's notes for combined implications, so the
  notes must be readable to another expert.
- 12 Nov (time not read from the clock): files 016-022 read (2:sc151-220, pp. 75-110: end of §15, §§16-18, §19 up to (43)); notes
  written up to 2:sc210. Heredocs with apostrophes fail here: write note parts with the Write tool
  (`work\notes_parts\part_NN.md`) and append with cat.
- 12 Nov 12:53 UTC (clock read): STEP 1 for Part I is complete: cote 140-2 (files 001-058, scans 1-575, pp. 1-292, sections 1-37)
  read in full; GROTHENDIECK_NOTES.md holds the notes (about 100 KB). Parts II-IV (cotes 140-3, 140-4, 140-1; files
  059-116 of work/reading2) are NOT read: a successor must read them in order (about 1.1M tokens: more than one
  context; cote 140-4 with sections 50-53 is needed in full before LM7 and LM8 are touched; Part II before any
  statement on the loop equation).
  Written besides the notes: FINDINGS.md (F1-F14), HUNCHES.md (H1-H7), READING_BASE.md (what was read, what was only
  read in part, the literature still to obtain). The Write tool refuses a file named FINDINGS.md from a subagent:
  stage the text as work/notes_parts/part_F.md and copy it over.
  Timestamps: earlier state lines in this file were written without reading the clock; the whole of step 1 for
  Part I ran between 12:22 and 12:46 UTC on 12 Nov.
  NOT done: step 2 (literature) beyond the two introductions listed in READING_BASE; step 3 (LM3 review); step 4
  (LM3b review); the comparison with the earlier review (addition G); the arXiv search (addition A).
- 12 Nov 12:59 UTC (clock read): STOPPED HERE, context at about 855k of 1M. Last things done: HUNCHES.md, READING_BASE.md,
  FINDINGS.md; new Parts for LM4, LM5, LM6 (A-D) in PUSH_REDO (files LM4/LM5/LM6_PARTS_redo_20261112.md) with
  PUSH_REDO/RECORD.md (what they demand, the push check, the assembly recipe). No PROMPT.md was changed.

### 1.3 What a successor does, in order

1. Read this file, then FINDINGS.md, HUNCHES.md, READING_BASE.md, PUSH_REDO/RECORD.md, then GROTHENDIECK_NOTES.md.
2. Literature (step 2): the list in READING_BASE section 3; the 008 paper in full before any GT statement; the
   2026 search (addition A); confirm or correct every "from memory" entry of FINDINGS (F2-F10 first).
3. LM3 review (step 3): its prompt names sections 19, 21, 26-30, 32-36 of Part I: reread those in full from
   work/reading2 files 020-053 before judging (the notes are a map, not a substitute). Keep in mind F3 and F13:
   "Gamma_{g,nu}" has three meanings in the manuscript; with the normalizer definition the (0,3) group is expected
   to be GT_0 and the (0,nu>=4) groups GT; H1 says his loop equation should be the GT_0 relations. Then LM3b.
   Then the comparison with the earlier review (addition G).
4. Parts II-IV of the manuscript (files 059-116): in full before LM7, LM8, LM6 Part E and before H1 is drafted.
5. Assemble LM4, LM5, LM6 by the recipe in PUSH_REDO/RECORD.md; write LM7, LM8 and LM6 Part E; then the final
   push check of every Part.

## 2. Section by Claude Fable 5.2, effort max (successor, agent a84ed26721eb851ea, started 12 Nov 2026, 13:00 UTC)

### 2.1 Working facts (successor)

- Own context: `python work\ctx2.py` (transcript of agent a84ed26721eb851ea). Budget rule of the brief: stop at about 75 %.
- Sizes that decide the plan: rereading sections 19-36 (reading copies 021-054) is about 490 KB = about 270k tokens; the
  LM3 return is about 250 KB of TeX plus a 67 KB register and code; the LM3b return about 260 KB of text plus a 78 KB
  register and code. One context cannot hold the literature, the reread and both returns. So bounded pieces go to forks
  of this agent (same model, same effort, same context up to the fork point); each writes its own file and this agent
  merges.
- Source rule for literature (memory free-or-receipted-library): read only freely accessible copies (arXiv, Numdam,
  EuDML, GDZ, journal open archives, IAS, the author's own page or own university page); new downloads go to
  `C:\Users\user\Documents\Free or receipted\free\lm-expert-20261112\<short>\`, logged per fork in
  `work\lit\downloads_*.jsonl` (to be merged into `free\CLAUDE_FREE_SHELF.json`; not done yet).
- The account is Ultra (checked with the usage tool at 13:10 UTC: weekly Fable 37 %).

### 2.2 State (newest last; times read from the clock)

- 12 Nov 13:39 UTC: read in full: this file, GROTHENDIECK_NOTES, FINDINGS, HUNCHES, READING_BASE, PUSH_REDO\RECORD and
  the three Parts files, the reading-list card, AGENTS_MATHEMATICS.md, the push standard. Four forks (Claude Fable 5.2,
  effort max) ran 13:12-13:39 UTC and finished:
  - fork A (agent acc40e3febe7a2a2f): `work\lit\LIT_LM4_surfaces.md` (F1, F2, F9, F10, F11 against the primary texts);
  - fork B1 (agent a4b99aa24f5c36f33): `work\lit\LIT_LM6_sections.md` (019 read in full with a per-step check; F7, H5,
    H7; 17 proposed changes to the LM6 Parts);
  - fork B2 (agent a5ba42d8a204daf74): `work\lit\LIT_LM6_anabelian.md` (F5, F6, F8; 009 and 031 read in full; 8
    proposed changes);
  - fork C (agent a94b06c138e9a154d): `PUSH_REDO\assemble_20261112.py`, `PUSH_REDO\build_frames_20261112.py`,
    `PUSH_REDO\assembly\<name>\{head,mid,tail,after_blocks}.md`, `PUSH_REDO\assembly\NOTES.md` (no PROMPT.md changed;
    `--install` not run).
  Next for this agent: 008 in full; the GT primary sources (Drinfeld, Ihara, Schneps, Lochak-Schneps, Harbater-Schneps,
  Hatcher-Lochak-Schneps, Nakamura 1994, the congruence subgroup problem with a 2026 search); then the reread of
  sections 19-36; then the reviews.

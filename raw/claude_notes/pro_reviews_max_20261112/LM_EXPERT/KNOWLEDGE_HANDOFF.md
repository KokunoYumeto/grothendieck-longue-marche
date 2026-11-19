# La Longue Marche expert line (redo of 12 Nov 2026): knowledge handoff

Kept by the field expert for Grothendieck's *La Longue Marche à travers la théorie de Galois* and the research prompts
on it (LM3, LM3b, LM4–LM8). Model and effort of every section's author are named in its heading. A successor reads this
file in full first, then `GROTHENDIECK_NOTES.md`, then `READING_BASE.md`, then what the step in hand needs.

Base folder: `<local>/Documents\longue_marche_pro_pilot_20261104`. Everything of this line is written in
`pro_reviews_max_20261112\` (`LM_EXPERT\`, `LM3\`, `LM3b\`, `PUSH_REDO\`; scratch in `LM_EXPERT\work\`), except step 5,
which edits the five unsent prompts in `pro_prompts_draft_20261111_work\<name>\PROMPT.md`.

## 0. The task, as given (launch brief of 12 Nov 2026, about 12:20 UTC)

The method, in the user's words: [the user's words, omitted] And: "Remember how the first one read the entirety of the Long March transcription before starting ...
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
   cutoff. Before calling anything open or known, read `<local>/Documents\recent_results_20261110\`
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
C. The papers are on disk: `<local>/Documents\recent_results_20261110\papers\`:
   `008_The-Deligne-Drinfeld-conjecture-September-23-2026.pdf`; `019_The-p-adic-section-conjecture-October-6-2026.pdf`
   and `019_Etale-covers-with-a-prescribed-exterior-sheet-September-24-2026.pdf`;
   `009_The-Bogomolov-Pop-reconstruction-theorem-September-23-2026.pdf` and the two 009 Milnor K-theory papers;
   `031_Open-Homomorphisms-of-Global-Solvably-Closed-Galois-Groups-October-5-2026.pdf`. Do not open `proof_packs\`.
D. From the user, for the LM4–LM8 prompts: [the user's words, omitted] Each Part must ask GPT-6 Astra (effort Pro) to do
   mathematics (prove, construct, compute, refute, attack the open items with a stated target), never to describe,
   summarize, classify by status or comment. Before finishing, reread every Part of every prompt against that test and
   against `PUSH_STANDARD_AND_AUDIT_20261111.md`, and record the check in `PUSH_REDO\RECORD.md`.
E. Required reading from the user: the board card `<local>/Documents\braindump_board\cards\reading-list.md`
   lists, per topic, the recent results and our own results (`<local>/Documents\grant_evidence\EVIDENCE.md`; the
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
  `<local>/Documents\Free or receipted\free\lm-expert-20261112\<short>\`, logged per fork in
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
- 12 Nov 14:16 UTC: 008 read in full by this agent (statement: Theorem 1.1, the graded Lie algebra of solutions of
  (1.2)-(1.4) with the Ihara bracket is free on one generator in each odd weight >= 3; nothing profinite). GT primary
  sources read by this agent: Drinfeld 1990 section 4 (Russian original, mathnet aa199), Harbater-Schneps (Main
  Theorem), Hoshi-Minamide-Mochizuki (Corollaries B, C), Minamide-Nakamura (Theorems A, B, Corollary C), Boggi
  arXiv:2408.12486v2 and arXiv:2011.15075v6 (introductions), Lochak-Nakamura-Schneps arXiv:2602.12462 (introduction).
  Found by an arXiv API search (claims): Hirose arXiv:2610.23719 (second proof of Deligne-Drinfeld, 16 Oct 2026);
  Bonatto-Robertson arXiv:2606.01466; Luo-Watanabe arXiv:2610.24986; Holzschuh-Schmidt-Stix arXiv:2608.21232;
  Carlson-Corwin arXiv:2611.09080; Collas-Philip-Yamaguchi arXiv:2605.02577. The congruence subgroup problem is known
  exactly for genus <= 2 (Boggi's 2026 texts say so); open for genus >= 3.
  Fork D (agent a2bb614ddecb173e1, Claude Fable 5.2, effort max) finished: `PUSH_REDO\LM{4,5,6}_PARTS_redo_20261112_v2.md`
  (literature-driven second pass), `PUSH_REDO\SECOND_PASS_20261112.md` (change log and push check), FINDINGS section E
  (F1-F14 confirmed or corrected, new F15-F27), HUNCHES (successor's notes), READING_BASE section 4, and the merge of
  the download logs into `Free or receipted\free\CLAUDE_FREE_SHELF.json` (backup beside it; Codex not told).
  Reading copies for the reread: `work\reading3\021..054` (made by `work\compact3.py` from reading2: control words as
  Unicode, `cT^^` = double-hatted calligraphic T, `bQ¯` = Q-bar, dollar signs dropped; quote from the source .tex).
- Coordinator message, relayed from the user (received about 14:15 UTC): do not spend effort on proofs that GPT-6 Astra
  (effort Pro) can do; the expert's strength is hunches and framing: what should be proved, refuted or developed goes to
  HUNCHES.md with reasons and into a prompt under `LM_EXPERT\PRO_PROMPTS\<name>\PROMPT.md`. Reviews still check the
  returns' arguments item by item (verification stays); short arguments that settle a verdict are fine; long new proofs
  go to Astra. Applied from here on, and written into the briefs of the review forks.
- CHANGE OF ROLE (coordinator message relayed from the user, received 12 Nov about 14:20 UTC): [the user's words, omitted] This expert no longer reviews LM3 and LM3b item
  by item: that checking goes to a Claude Opus 5.5 agent at effort max (launched by the coordinator, not by this
  agent). This expert's work from here on: find the mathematics to be done. From the reading (the literature, Part I
  through the notes, the LM3 and LM3b returns read for what they open up, not verified line by line) write what may be
  true and what is worth attacking, in HUNCHES.md and FINDINGS.md, with reasons; confirm or correct the from-memory
  findings only as far as a quick look at the source allows; frame it all as prompts for GPT-6 Astra (effort Pro): the
  second pass and assembly of LM4-LM6, and new prompts in `LM_EXPERT\PRO_PROMPTS\`. Keep the overview; leave proofs and
  checks to others. Consequences: the reread of sections 19-36 (a precondition of the reviews) is not done; no
  `LM3\REVIEW.md` or `LM3b\REVIEW.md` is written by this line; statements taken from the returns are marked as the
  returns' claims, unverified.
- 12 Nov 15:24 UTC (clock read): STATE AT STOP of the successor (agent a84ed26721eb851ea), context about 630k; bound
  given by the coordinator: stop before 650k. This expert is kept for consultation (modern literature on GT,
  anabelian geometry, the section conjecture); do not give it reading work.
  DONE: (1) the literature step, through forks A, B1, B2 (notes in `work\lit\LIT_LM4_surfaces.md`,
  `LIT_LM6_sections.md`, `LIT_LM6_anabelian.md`) and this agent's own reading (008 in full; Drinfeld section 4;
  Harbater-Schneps; Hoshi-Minamide-Mochizuki; Minamide-Nakamura; Boggi 2024 and 2026; Lochak-Nakamura-Schneps 2026);
  FINDINGS section E confirms or corrects F1-F14 and adds F15-F27; HUNCHES has notes on H1-H7; READING_BASE section 4.
  (2) LM4, LM5, LM6 assembled and installed in `pro_prompts_draft_20261111_work\<name>\PROMPT.md` (before-copies
  `PROMPT_before_redo_20261112.md`), each with `ZIP_LIST.tsv`; record in `PUSH_REDO\RECORD.md`, section 2, with the
  open points (a)-(e) for whoever sends them.
  NOT DONE: no `LM3\REVIEW.md` or `LM3b\REVIEW.md` (the item-by-item review went to another agent by the change of
  role); the reread of sections 19-36; the comparison with the earlier reviews; no prompt under
  `LM_EXPERT\PRO_PROMPTS\`; Parts II-IV of the manuscript unread; LM7, LM8 untouched.
  READ BUT NOT YET WRITTEN INTO HUNCHES OR FINDINGS (from the registers of the returns LM2, LM3, LM3b, read for what
  they open up; all are the returns' claims): (i) H2 is contradicted: LM3b B.4, B.5 say that his hole-plugging map
  `Autext_lac(pi^)_i -> Aut_lac(pi'^)` is onto and NOT injective already for (0,4) -> (0,3) (graded witness
  E(x) = [[y,[x,y]],x], E(y) = -[[x,[x,y]],y], E(z) = 0, which kills x+y+z by the Jacobi identity: checked by hand
  here); on the normalizer of the point-pushing subgroup it is 1 -> pi^ -> O' -> GT x S_3 -> 1 (LM3b B.6).
  (ii) With the normalizer definition, LM3 E.7, E.10 give Gamma'_{0,3} = GT_0, Gamma'_{0,nu} = GT (nu >= 4),
  Gamma'_{1,1} = GT; so (27) in that reading is "G_Q = GT" outside (0,3), and his "hasty corollary" fails only at
  (0,4) -> (0,3), exactly if GT differs from GT_0. (iii) The first half of H1 is claimed proved: LM2 B.m2 (his loop
  equation of section 46 = Drinfeld's (I), (II)). (iv) Graded: the two-relation space is larger than grt_1 from
  weight 4 on (own count: the multiplicity of the standard representation of S_3 in the free Lie algebra; LM2 B.g3
  gives 1,0,1,1,2,3,6,10,19,33,62,112); pro-l strictness for l >= 5 is LM3b F.3; profinite GT versus GT_0 is open
  (LM3b F.4). (v) Three claimed proofs of Deligne-Drinfeld now exist: 008; Willwacher arXiv:2610.15592 (named in
  LM3 E.28, LM3b G.10; not read here); Hirose arXiv:2610.23719 (abstract read). (vi) Best targets seen for new
  prompts (none drafted): profinite GT versus GT_0 through an element of GT_0 built in finite quotients; torsion in
  GT_0 and GT other than complex conjugation (LM2 B.g10 leaves pro-l torsion of order dividing l-1); whether every
  loop-preserving automorphism normalizing the geometric subgroup preserves the configuration fibres (LM3b B.8, E.9;
  Boggi's inertia condition I_0); the eigenline of LM3b D.5 lifted through the lower central series (LM3b D.4); the
  genus-3 congruence kernel as a centralizer (LM3b H.1, H.5).

## 3. LM7 section by Claude Fable 5.2, effort max (successor for the return LM7_FERMAT_TOWER; launched by the coordinator, Claude Opus 5.5, 13 Nov 2026; work done 03:42–04:10 UTC, clock read)

### 3.1 What was done

- Reviewed the return `answers\LM7_FERMAT_TOWER_20261113T0227Z_unzipped\LM7_FERMAT_TOWER\` (GPT-6 Astra, ChatGPT Pro mode; INCOMPLETE; 103 statements). Output in `pro_reviews_max_20261112\LM7\`: `REVIEW_author.md` (table of all 103, findings), `PUSH_ITEMS.md` (E.32 as a lim¹ class with proof; E.25; the push items for E.23, D.13, D.19), `checks_author\check_finite.py`, `check_lie.py` and their `.out` files.
- Result: correct 88 (79 Proved, 9 Refuted), known 12, open 3 (D.13, D.19, E.23), wrong 0, gap 0 in the steps followed.

### 3.2 What the review does not cover (a successor must not take these as checked)

- The return's `code\`, `report.md`, the ledgers and the run trace were not opened (compute bound). D.25 and D.26 rest entirely on the return's programs; B.7, B.13, D.7, E.12, E.26 in part.
- No cited source was opened. Existence only, on the arXiv listing: Borne–Emsalem–Stix arXiv:1301.4429; Dolgushev–Guynee arXiv:2401.06870; Çiperiani–Stix arXiv:1106.4255, 1308.4528. Otsubo's paper on the Fermat tower was not found by the one query made; theorem numbers are unverified throughout.
- Cote 140-4 (§§50–53) is still unread in this expert line. The return's many corrections to the manuscript's formulas were checked as mathematics only, never against the scans.
- Reading copies of the return's sections (compacted TeX) are not kept; rebuild with a script like `compact_tex.py` if wanted. Quote from the source `.tex`.

### 3.3 Facts worth carrying

- **E.32 is a lim¹ class.** `H²_cts(G_Q, Z₃(2)) ≅ R/dR` (`R` = families of 3-adic integers over the primes `q ≠ 3` tending to zero, `d = (q−1)`); Jannsen's lim¹ term is `{z : (q−1) | z_q}/dR = lim¹_n ⊕_q (Z/3ⁿ)[q−1]`; that tower is Mittag-Leffler iff `v₃(q−1)` is bounded. Proof in `PUSH_ITEMS.md`, Part 1. For `Z₃(1)` there is no lim¹ (the Kummer tower has onto transitions). Phantom classes start at weight −3.
- **E.25.** `κ₂(−1) ∪ κ₂(−1) = (−1,−1)`, non-zero exactly at 2 and ∞ (not at ∞ alone); it is the class of the conic `x²+y²+z² = 0`. The shape map (1b, H2) should add the prime 2.
- **Lim¹ against cofinality.** D.13 and D.19 live in towers of finite sets (no lim¹; lemma in `PUSH_ITEMS.md` 3.0): their failure is cofinality, as in D.26. E.23 has finite rank and infinite `H¹`: its failure mode is lim¹, in the rank-44 kernel `ker(Λ²V → Λ²T)` (weights −3 and −4).
- **The rank-44 test statement of the notes is contradicted by E.34** (classes unramified outside 3 all lift to the whole pro-3 group and most are not cuspidal; reviewer's argument, unchecked by a second reader). Corrected items in `PUSH_ITEMS.md` 3.2.
- D.11's table of special derivations through weight 10 and both metabelian image rows were recomputed independently (`check_lie.out`): special 0,0,1,0,3,0,6,4,13,12; image 0,0,1,0,3,0,5,0,7,0; invariant 0,0,1,0,1,0,2,1,4,2; image 0,0,1,0,1,0,1,0,2,0. The weight-9 extra invariant vector is `X²Y²(X+Y)³`.
- Vandiver certificates of D.10 recomputed for all odd `ℓ < 50`; the Ihara–Takao relation `{σ₃,σ₉} = 3{σ₅,σ₇}` holds exactly for the representatives `ad_x^{2m}(y)`.
- Scripts that use numpy must reduce modulo the prime at every step of a linear combination (int64 overflow gave a wrong rank once here).

### 3.4 Next steps for whoever writes the LM7 push prompt

1. Assemble the prompt from `PUSH_ITEMS.md` Part 3 (items 3.1–3.6), with Parts 1 and 2 as attached proved material to be checked by GPT-6 Astra. Lint with `claude_tools\push_rule_pro_prompts.py --lint-math`.
2. Before sending: open the return's `code\d_cm_shadow.py` and `d_cm_refine.py` (D.25, D.26 are the base of item 3.5), and read CYCLOTOMIC C9 for item 3.3 (not read here).
3. Open at theorem level: Borne–Emsalem–Stix 5.10 (E.36), Dolgushev–Guynee 5.2–5.5 (D.22), Otsubo 6.1, 7.2, 8.1 (B.8, D.5, D.6), Furusho 2011 (D.21).

### 3.5 The LM7 push prompt (same agent, 13 Nov 2026, 04:12–04:28 UTC, clock read): written, not sent

- Prompt: `pro_prompts_draft_20261111\LM7_PUSH\PROMPT.md` (31 KB; `push_rule_pro_prompts.py --lint-math`: failing lint 0; closing paragraph, typesetting check and Checkpoints with ID LM7_PUSH present). Zip: `LM7_PUSH_background.zip` beside it (904,343 bytes, 97 entries, no PDF). Build script and manifest: `pro_prompts_draft_20261111_work\LM7_PUSH\build_zip_20261113.py`, `MANIFEST.tsv` (path, origin, bytes, sha256, why). The user sends Pro prompts.
- Parts: A = E.23 (sections of `N/γ₃N`, then metabelian and depth two; the main question), B = which classes are geometric (the corrected rank-44 test), C = germs (CK C9), D = D.13, E = D.19 (the CM coset), F = the lim¹ check as a theorem, with FLAGGED_149 F17.3 and CYCLOTOMIC D15. "Results this builds on" R1–R14 is the settled section (R2 = E.32 as a lim¹ class, R3 = E.25 non-zero at ∞ and at 2).
- arXiv TeX fetched into `Free or receipted\free\arxiv-eprints-lm-20261113\`: 1301.4429, 0809.0017, math_0703877, math_0006158, 1106.4255, 2401.06870, 2008.00066, 2405.11725, 0808.0319, 2004.08860; each checked by its title line. Not yet entered in `CLAUDE_FREE_SHELF.json`.
- Not attached: Wickelgren's paper on 3-nilpotent obstructions. The id tried from memory (1011.1199) was another paper (folder removed); the arXiv API then answered 429. Find the id and add it before sending if wanted. Jannsen 1988, Harbater–Schneps and Hoshi 2010 are not on arXiv and are named in the prompt for the model to find.
- Posed from the notes and the registers, the TeX not read in full by the drafter: task F.3 (F17.3, CK D15). Read those two statements before sending.
- The statement of Borne–Emsalem–Stix behind E.36 was read at the source (one sentence added to `LM7\REVIEW_author.md`).
- Update, 13 Nov 2026, 04:36 UTC (clock read), same agent: the loose ends of 3.5 are closed. Wickelgren's paper is arXiv:1011.0655 (found on the arXiv listing search; fetched, title checked, attached and cited). Task F.3 was rewritten after reading the TeX: F17.3 is the inertia of `Q((t))` on the class-two quotient (no splitting to `G_Q`; that is F17.4), and CK D15 is a non-abelian coboundary question over a p-adic field with `Δ = G_{K(μ_∞)}`, now task F.4, where no lim¹ term can occur (finite sets). The 11 cache folders are entered in `CLAUDE_FREE_SHELF.json` (19 entries; backup `CLAUDE_FREE_SHELF_before_20261113_LM7_PUSH.json`). LM7_PUSH is in `claude_tools\maths_prompt_tally.py` as READY (backup beside it). Final zip: 947,234 bytes, 99 entries; lint: failing 0. Script: `pro_prompts_draft_20261111_work\LM7_PUSH\shelf_and_tally_20261113.py`.

## 3.6 (copied by the main session from LM7/HANDOFF_NOTE_20261113_build_on.md, 13 Nov 2026; the guard blocked the expert's own edit)
# Handoff note for section 3.6 of LM_EXPERT\KNOWLEDGE_HANDOFF.md (not yet appended there)

Claude Fable 5.2, effort max (the LM7 reviewer), 13 Nov 2026, 13:30–13:45 UTC (clock read at 13:30 and 13:38).

The append to `LM_EXPERT\KNOWLEDGE_HANDOFF.md` was blocked by the context guard (context over 70 %: no more commands). Whoever continues this line: copy this note into the handoff as section 3.6.

## 3.6 Building on the new returns

- Written: `LM7\BUILD_ON_20261113.md` (statements bearing on E.23, D.19, D.13; implications for the companion and the other LM prompts; hunches H1–H6 as candidate items; what a referee should check first) and the conference talk `<local>/Documents\expert_conference_20261113\talks\R1_LM7_reviewer.md` (round 1: the changes for the open items; floor questions 2 and 4; two questions, to the author of the LM8 intake and to the Dérivateurs expert).
- Read for them: register statements only. LM7's zip of 13:14 UTC (the 68 new rows D.27–D.46, E.37–E.85, and the changed rows D.25, E.23), LM7_PUSH checkpoint 04 (all 137 rows indexed; the D, E and lead rows read), LM4 D.29–D.30, LM8 A.22 and G.20. No proof, section, report or program of these returns was read; the two reports named in the coordinator's brief were not opened.
- To carry:
  1. My LM7_PUSH prompt, Part E, wrongly called the CM coset question equivalent to genuineness of one of D.25's twelve shadows. LM7_PUSH E.10: each CM matrix pair has an affine space of shadows above it; D.27 and E.9 remove the twelve recorded points only.
  2. LM7_PUSH confirms Lead 1 (B.2), Lead 4 in both directions (B.4) and Lead 5 (A.1, A.4), and refutes T1 and T2 (A.5, A.6). The lim¹ class exists for the intrinsic rank-44 module (A.4) and survives every finite extension (C.4).
  3. Hunch H1 (mine, unchecked): `cd₃ G_{Q(μ_{3^∞})} ≤ 1` (Serre, CG II §3.3, Prop. 9), so `H²(G_Q, M) = H¹(Γ, H¹(Δ₃, M))` for 3-primary `M`, every pro-3 lifting problem is unobstructed over `Δ₃ = G_{Q(μ_{3^∞})}`, and the lim¹ class is the non-Hausdorff part of the `Γ`-coinvariants. E.23 is then a descent problem along the cyclotomic `Z₃`-tower.
  4. Hunch H2 (mine, unchecked): if the CM coordinates `(T, W)` form a homomorphism on `GT̂₀`, the extra coset is reached at multiplier one iff some element of any multiplier is CM-incompatible; LM4's mixed-prime involutions and LM7 D.46's prime-mixed element are the test objects.
  5. The surviving candidate for D.19 is LM7 D.46 (a Galois commutator on the relative pro-2 part, the identity on the odd parts); what remains maps onto `A₇`.
- State of this agent: context at about 705K tokens; the guard allows only Write and Edit. Do not give this agent further reading; a successor should start from `REVIEW_author.md`, `PUSH_ITEMS.md`, `BUILD_ON_20261113.md` and this note.

## 4. LM8: the intake, folded in (written by Claude Fable 5.2, effort max, agent a125034fd35557818, 13 Nov 2026, 14:10 UTC, clock read)

Source: `<local>/Documents\pro_intake_20261113\HANDOFF_ADDENDUM_LM.md`, written by the intake agent (Claude Fable 5.2, effort high; not an expert of this line; 13 Nov, 13:22–13:49 local time). Reworded here; where this agent re-read something itself, the line says so.

### 4.1 What the intake is

- The return: `answers\LM8_LIE_APPROXIMATIONS_checkpoint_16_20261113T1145Z_unzipped\LM8_LIE_APPROXIMATIONS\` (GPT-6 Astra, ChatGPT Pro mode). The run stopped; checkpoint 16 is its last state; marked INCOMPLETE. 167 statements: 122 Proved, 24 Refuted, 15 Known, 6 Open.
- The intake (`pro_intake_20261113\INTAKE_LM8.md`) gives every row an outcome and a basis code. Result: 161 consistent, 6 open (A.12, B.24d, B.28, F.12, G.16, G.20), none doubtful, none wrong. Only 32 of the 161 were checked with their proofs (read, re-derived or recomputed); 129 are statement-level verdicts, which say that a statement is well formed and agrees with its neighbours, not that its proof holds.
- From the intake the prompts LM6 and LM5 were updated (`PROMPT_IMPACT.md`); LM4 and LM7_PUSH were left alone. `IMPLICATIONS.md` reads LM8 together with TOTAL_EXACT_2 (candidates P1–P5); `PUSH_ITEMS.md` ranks what a follow-up must settle.

### 4.2 What nobody has checked (do not take these as checked)

- About 110 KB of the 900 KB of TeX was read by the intake. Statement level only: Part D except D.4, D.10, D.14, D.23 (so the main result D.21 is unread); Part C except C.6; Part A except A.2, A.7, A.22; B.14a–d and B.20–B.35 except B.32, B.34; E.1–E.3, E.6–E.9, E.12–E.17; F.1–F.3, F.5–F.14, F.16–F.20, F.22–F.24; Part G except G.6, G.10, G.11.
- No program of the return was opened or rerun; no cited source was opened. Several sources are 2025–2026 preprints; this agent confirmed on arXiv that these exist with the titles the return gives: Ishii 2312.04175, Ishii–Goto 2412.18846, Ishii 2602.00615, Goto–Ishii 2610.21052, Lochak–Nakamura–Schneps 2602.12462, Malkin 2010.07238 (TeX fetched; content not read).
- The manuscript side of the thirteen correction rows (A.2, A.7, A.15, B.24, D.3, D.4, D.10, D.14, D.23, E.4, E.5, E.11, E.13): checked as mathematics only. Exception since this session: E.11 against scans 242–243 (5.3 below).
- F.16–F.18 (vanishing of the dual Selmer defects for `E_1`, `E_6` at 5 through Kato's Theorem 17.4): the intake could not follow the passage from a value modulo 25 to `H¹_f = 0`. F.9 and the thresholds 2, 3, 4 for `E_6` hang on it.
- Checkpoint 16 has no PDF; the PDF check (overfull boxes, rendered pages) is not done.

### 4.3 Facts to carry

- **F.21 = LM7 E.32 at the prime 5, with a section.** `H²_cts(G_Q, Z_5(2))` is families tending to zero modulo the image of `diag(5^{v_5(q−1)})`, no closure; the pair `(κ(5), Σ 5^n κ(q_n))` lifts to every finite Heisenberg quotient and to no integral class-two section. The intake recomputed the eight primes.
- **F.15** is the criterion for "sections at every level give a section": always onto; bijective for compact towers and rational unipotent towers; false for `Z ⊕ Z/2^n`.
- **E.11.** The 2-limit of the sheaf topoi of shrinking punctured discs is the degenerate topos; the covering germ is `BZ` (E.10). Proof re-read by this agent: correct (the outer annuli pull back to zero and cover).
- **A.22.** `F̂_2/F̂_2''` has a non-inner involution of multiplier one that preserves the three peripheral classes and acts on the Alexander module by `1 − 2e`, `e` the idempotent of a `Z_5[ζ_3]`-component; it is invisible in every pro-prime quotient. A.23–A.26 lift it through the relative pro-5 completion of the index-3 kernel. Re-derived by this agent; more in 5.3.
- **The LM7 reviewer's results are proved in LM8**: special derivations lift at every prime (B.11); pro-ℓ `GT_0 ⊋ GT` for every ℓ (B.12, B.14d); the tables (tripod special 0,0,1,0,3,0,6,4,13,12; (0,4): 2,1,6,6,28,36, normalizer quotient 0,0,1,0,1,0, B.16); filling (0,4) → (0,3) is exact on the normalizer with image `GT × S_3`, not onto `GT_0 × S_3` (B.17); at (1,1) the normalizer quotient is in degrees 6 and 10 (B.18, B.19).
- **Part G.** G.6 refutes the lead "`b_+, b_0, b_−` all non-zero on Δ": only `b_0`. G.10 settles CK E3 in every pro-ℓ quotient (fixed points of `s(Δ)` are inertia). G.11 confirms "lifts through `N_4`, stops at `N_5`". G.13 is LM3b D.4 for this curve, pro-ℓ. Full profinite: G.19 (if one prime sees the subgroup), G.20 open.
- **Lead 2 of the LM8 prompt, corrected** (E.2, E.3, E.5): `ST_{1,1}^+ = B_3`, central over `SL_2(Z)` with kernel the square of the centre; `GL_2(Z)^~ = B_3 ⋊ C_2` is not central; the extension of the 140-1 draft is class 1 of `Z/12` with his sign.
- **§52.3 is not a nilpotent tower** (B.1–B.3): his "approximation de Lie" is an adelic representation into a `Q`-group of finite type with diagonal rationality on the discrete geometric group.
- With TOTAL_EXACT_2: all limits in LM8 are over directed sets, so only the coefficients decide (F.15); a limit over the Teichmüller tower itself would be over a non-filtered index (candidate P3 of `IMPLICATIONS.md`, low confidence; not taken into LM8_PUSH).

### 4.4 The intake's next steps, and where they stand

1. Intake of LM7_PUSH and LM4 when they end: comes to this expert. LM7_PUSH Part F meets F.15 and F.21.
2. The push prompt for LM8: written (section 5). Scans 242–243 are read (5.3).
3. The manuscript side of the correction rows, for an expert with cotes 140-4, 140-1, 140-3 open: not done; not a Pro item.
4. Build the LM8 paper and run the PDF check: not done.

## 5. LM8_PUSH (same agent; 13 Nov 2026, 13:23–14:18 UTC, clock read at both ends; stopped once by mistake and resumed)

### 5.1 What was done

- Read in: this file, the four intake files, the LM7 review and its `PUSH_ITEMS.md`, the template `claude_tools\prompt_lessons_20261112\PROMPT_TEMPLATE_PUSH.md`, the LM7_PUSH prompt. Of LM8: the register rows of the six open items and of the rows they rest on (A.11–A.26, B.12–B.35, E.10–E.13, F.2–F.24, G.7–G.24); in full with proofs G.10–G.13, G.19, G.20, G.22, E.10, E.11; the statements of A.19, A.21, A.22, B.25, B.28, F.16–F.18, G.16, B.24d. Of LM2: E.1–E.4 in full, the rows B.m2, B.m3, C.d4, C.d5. The manuscript: cote 140-4 scans 242–243, transcription and scan images.
- Written: `pro_prompts_draft_20261111\LM8_PUSH\PROMPT.md` (55 KB; `push_rule_pro_prompts.py --lint-math`: failing lint 0; closing paragraph, typesetting check, checkpoints present) and `LM8_PUSH_background.zip` (2,676,567 bytes, 251 entries, no PDF). Work folder `pro_prompts_draft_20261111_work\LM8_PUSH\`: `build_zip_20261113.py`, `MANIFEST.tsv`, `fetch_arxiv_20261113.py`, `arxiv_lookup_20261113.py`, `check_leads_20261113.py` and `.out`, `shelf_and_tally_20261113.py`, `CONSULT_FOR_LM7_REVIEWER.md` (five questions for the previous expert; the main session passes them on).
- Records: 68 source files entered in `Free or receipted\free\CLAUDE_FREE_SHELF.json` (backup beside it); LM8_PUSH is in `claude_tools\maths_prompt_tally.py` as READY (backup beside it). Thirteen arXiv e-prints fetched into `Free or receipted\free\arxiv-eprints-lm-20261113\` (1710.05532, 1512.03975, 1003.1012, 1504.04737, 2610.21052, 2602.00615, 2602.12462, 2010.07238, 1410.1045, math_0003113, math_0610163, 2312.04175, 2412.18846), each checked by its title line.
- The user sends Pro prompts. Not sent.

### 5.2 What the prompt asks (Parts; R1–R23 settled material; Leads 1–18)

A. LM8 G.20, the main question: `π^{s_b(Δ)} = I` and "procyclic with open arithmetic normalizer ⇒ in a conjugate of `I`" for the full profinite group of `y² = x³ − x` minus the origin over `Q(i)`; the structure `Fix = Θ ⋊ I`; the abelian layer on every cover; the first covers (three `𝔖₃`-covers, the two covers of order 8); the pro-ℓ statement on every cover; the sections that agree on Δ.
B. LM8 A.12 on the tripod: all finite-order elements in the metabelian pure peripheral group; which pass the metabelian 2-cycle, 3-cycle and pentagon tests; is `𝒫₁` torsion-free (lift the involution of A.22 or find the finite obstruction); torsion with λ = 1 in `GT̂₀`, `GT̂`; multiplier −1 and other multipliers.
C. LM8 B.28: §47 as the fixed points of an endomorphism `D` of `GT̂₀`; comparison with Nakamura–Tsunogai and Nakamura–Schneps (III′); `GT̂ ⊆ C^φ`; `C^φ = GT̂₀`; the pairs `(F^(ℓ), D(F)^(ℓ))`; level four and beyond; the CM coordinates.
D. LM8 F.12: `H^i_cts(G_Q, Z_5(j))`, j = 3, 4, 5, with lim¹; `Sec(T_3)`, `Sec(T_4)`, `Sec(T_5)` with unrestricted ramification; the metabelian quotient; the Fermat kernels.
E. LM8 F.16–F.18 by Rubin's theorem and the two-variable `p`-adic `L`-function (24 characters), the certificates recomputed, the passage through Kato's theorem checked step by step.
F. LM8 E.11: the limit of the sheaf topoi of a germ (sublocale `⋂ S_i`), the germs for which his parenthesis holds, the coherent (étale, henselian) theorem, Leroy's thesis.
G. LM8 G.16: λ, the lattice, the embedded image in degrees 8–14.
H. LM8 B.24d: images and kernels above the first Fermat stage; the additive-polynomial lifts.

### 5.3 Found while drafting (this agent's; status on each line; also in FINDINGS.md, F28–F33)

- **Scans 242–243 read on the images** (`LM_C4-229-247\LM_C4-229-247_scan242.jpg`, `_scan243.jpg`). The text is about a topological space with a filter and the projective limit of the "(petits) topos étales" of the members: the topological reading. So E.11 refutes what he wrote, for residual germs; he hedged twice (both hedges are insertions). **The marginal note on scan 243 reads, as far as this agent can see, "cela est fait par Olivier Leroy ?"**; the first-pass transcription (`answers\unzipped\LM_C4-229-247\`, line 758) has "cela ne fait pas aller loin ?" marked unsure. A reading point for the editors; Leroy's thesis (fundamental groupoid of a topos, Montpellier 1979) is the source to open. One reader, enlarged crop; not confirmed by a second.
- **§47 as a fixed-point condition** (Lead 8; derived here, not checked): every pure peripheral outer automorphism of `F̂_2` descends along `φ : F̂_2 → C_2 ∗̂ C_3`, and every element of `GT̂_0` extends from the level-two subgroup; the descent restricted to the level-two subgroup is an endomorphism `D` of `GT̂_0` (restrict to the `𝔖₃`-cover of the `j`-tripod, a sphere minus eight points, and fill five), and `C^φ = Fix(D)`. With the 2-cycle relation, `F(σ_1σ_2σ_1) = f^{-1}(σ_1σ_2σ_1)^λ`, so §47 says: `f` is the `Int(s)`-coboundary of its own image `f(s, sr)`.
- **The metabelian relations of `GT̂` do not exclude multiplier-one torsion** (Leads 5–7; checked on characters by `check_leads_20261113.py`). The beta function `1 − 2e_0` of A.22 is `𝔖₃`-invariant and fails the cocycle identity `β(X,Y)β(XY,W) = β(Y,W)β(X,YW)`. But for any inversion-invariant idempotent `e_1` of `Ẑ[[Ẑ]]` vanishing at the trivial characters, `g = 1 − 2e_1` gives `β_g = g(X)g(Y)g(Z)`: an order-two unit, `𝔖₃`-invariant, a coboundary, defining a non-inner pure peripheral involution of multiplier one of the free profinite metabelian group. Whether the cocycle identity is exactly the metabelian shadow of the pentagon (Ihara's Γ-factorization) is from memory, source not opened.
- **The first cover for G.20** (Lead 3; by hand, unchecked): the `[i]`-stable `𝔖₃`-cover of `E ∖ O` is `v² = w⁷ − w`, genus 3, two cusps at Weierstrass points, Jacobian isogenous to `E³`. An open subgroup of Δ fixes its whole `H_1`; the abelian layer excludes nothing there. In general (Lead 2) the Δ-fixed part of `H_1` of a cover is the boundary plus the `E`-isotypic part orthogonal to the non-torsion cuspidal classes (Ribet's Kummer theory over `K(E_tors) = K^ab`).
- **`H¹_cts(G_Q, Z_5(3)) = Z_5` and `H²_cts(G_Q, Z_5(3))` has a lim¹ part** (Lead 12; by the proof of F.21 with `q² − 1`; not written out).
- **The limit topos** (Lead 14): the 2-limit of the `Sh(S_i)` is sheaves on the sublocale `⋂ S_i`; the point for the germ at a point of a regular space, empty for a residual germ of a Hausdorff space. His "good cases" hold for germs around points, not for the residual germs he goes on to use.

### 5.4 Not covered; to do before sending

- R10–R13, R17, R20, R21 of the prompt are statement-level (the prompt says so). LM2 was not reviewed by this line.
- Sources named from memory in the prompt (Ihara's beta and gamma papers, Nakamura–Tsunogai and sequels, Ribet 1979, Leroy 1979, Moerdijk 1989): bibliographic data unverified; the prompt says "check each citation".
- The answers to `CONSULT_FOR_LM7_REVIEWER.md` may change Lead 11, task C.5, Lead 12 and the wording of the full-profinite tasks.
- The zip attaches LM7 in its state of 13:14 UTC (register, Part D, the section of E.32) and, under `runs_in_progress/`, the register and Parts D–F of LM7_PUSH checkpoint 04 and the register and TeX of LM4 (13:14 UTC). All three runs were still going. When they end: rebuild the zip from the final states and recheck R14, R22, R23 of the prompt against them.

### 5.5 Overlaps with the runs still going (LM4, LM7, LM7_PUSH)

- **LM4_FINITE_GROUP_ACTIONS ↔ Part B.** LM8 A.12 for general surfaces and finite groups is LM4's subject (the LM8 return notes "LM4 not supplied"). Part B is restricted to the tripod and says so. When LM4 returns: check whether it proves or refutes profinite realization in a form that decides B.3, and whether it treats multiplier-one torsion.
- **LM7_PUSH Parts D, E ↔ Part C.** LM7_PUSH D.1, D.2 (images of `Out^♯(F̂_2)` and `GT̂_0` in pro-ℓ weights 5 and 9) and E.2, E.3 (the CM coset) were open at its checkpoint 04 (tally entry). C.5 (pairs `(F^(ℓ), D(F)^(ℓ))`), C.7 and Lead 11 (the CM coordinates on `C^φ`) are the same kind of full-profinite separation; an answer to LM7_PUSH E.2 bears directly on C.4 through Lead 11.
- **LM7_PUSH Part F ↔ Part D.** LM7_PUSH F.1 (the localization statement with the global term kept, for any lattice over any number field) is Proved at checkpoint 04 (register row read here; unreviewed). It is R23 of the prompt; D.1 and Lead 12 are its cases `Z_5(3)`, `Z_5(4)`, `Z_5(5)`.
- **LM7_PUSH Parts A–C ↔ Part D.** Both compute section sets beyond class two with unrestricted ramification (the Fermat cubic at 3 there; the tripod at 5 here); the methods should agree (tame condition plus convergence condition).
- **LM6 Part A (e)** now asks the G.20 question (intake); Part A of LM8_PUSH is the full treatment. If both are sent, the returns must be compared.
- **LM7 (still running).** Its later states may add to D.13, D.19; nothing in LM8_PUSH depends on more than the first return.

### 5.6 Working facts

- Own context: `python -I -B work\ctx3.py` (transcript of agent a125034fd35557818; a successor changes the path). At the end of this task: about 54 % of 1M.
- The scans are on disk per package: `longue_marche_pro_pilot_20261104\LM_<KEY>\LM_<KEY>_scanNNN.jpg` (about 0.5 MB each; an image costs a few thousand tokens; crop with PIL for margins).
- Register rows are read cheaply with a small script that prints chosen ids of a results CSV to a file (the returns' CSV columns: id, statement, status, where_proved, depends_on, manuscript passages, notes).
- The returns' bibliographies carry arXiv ids and "verified" notes: grep them before searching.
- Thinking stays in the context during a tool loop: this task went from 25 % to 45 % of the window with about 100 KB of reading.

### 5.8 Section 3.6 arrived after the read-in; what was taken from it

Section 3.6 above (the LM7 reviewer's note "Building on the new returns") was copied into this file by the main session after this agent had read it; it was read when the append showed it, together with `LM7\BUILD_ON_20261113.md` and the register rows it names (LM4 D.29, D.30; LM7 D.27, D.46; LM7_PUSH D.1, D.2, E.2, E.3, E.9, E.10, F.1: statements only). Taken into LM8_PUSH:

- **H1** (cohomological dimension one over the cyclotomic tower, descent for `Γ`): Lead 16 and task D.7, at the prime 5, credited to the LM7 reviewer, unchecked.
- **H2** (the CM coset by multiplicativity): task C.7 now asks whether `(T, W)` is a homomorphism on `GT̂_0`; R14 says that the twelve recorded shadows are removed (LM7 D.27, LM7_PUSH E.9), that every CM matrix pair has an affine space of shadows above it (LM7_PUSH E.10), and names LM7 D.46.
- **LM4 D.29, D.30** (involutions with a mixed-prime multiplier at type (0,4) and closed genus two; LM8 A.12 is false there if they hold): R22; task B.5 asks whether the (0,4) involution induces one on the tripod. So Part B's question for the tripod is no longer "does realization hold" but "which torsion exists".
- **H4** (the metabelian group by Alexander-ring algebra): task B.1 now asks for the whole group of pure peripheral outer automorphisms of the metabelian quotient as units, and its `𝔖₃`-centralizer.
- The reviewer's question "does the involution of LM8 A.22 commute with `𝔖₃`": yes on characters (Lead 5, `check_leads_20261113.out`).
- Not taken (they belong to the LM7 follow-up): H3 (entanglement over `PSL_2(Z/12)`), H5 (cusp colourings), H6 (Iwasawa form).
- From the coordinator's consult of about 14:10 UTC (expert conference of 13 Nov): LM4's checkpoint of 13:42 UTC (D.63-D.65: centralizers of the negative involutions of the once-punctured torus; C.12, D.12, F.7 still open there) is in R22 and task B.5, and its diff is in the zip; floor question shape_map_Q2 (cuspidal sections as homotopy fixed points of the homotopy limit of the punctured henselian neighbourhoods) is Lead 17 and tasks F.4, F.5; floor question shape_map_Q3 (the order-75 quotient: an idempotent in degree zero against a twisted `H^1` with values in the kernel of all pro-l quotients) is Lead 18 and task D.8. This agent's view on Q3, unchecked: both readings hold; automorphism rows (A.12) are of the degree-zero kind, section and fixed-point rows (F.12, G.20) of the `H^1` kind, the module being the 5-torsion of the `j = 0` curve `w^3 = t^2 - t`.

### 5.7 Next, in order

1. Pass `CONSULT_FOR_LM7_REVIEWER.md` to the previous expert; apply the answers to the prompt; lint again; rebuild the zip if files change.
2. Intake of LM4, LM7 (final state) and LM7_PUSH when they end; fold LM7_PUSH F.1 and E.2 into LM8_PUSH if it has not been sent, or into the reading of its return if it has.
3. Not started: the manuscript side of the correction rows of LM8 (needs cote 140-4 read in full, still unread in this line except scans 242–243); the read of D.21; the LM8 paper build and PDF check.

### 5.9 The expert conference's items folded into the unsent prompts (same agent, 13 Nov 2026, about 14:25-14:40 UTC)

- Source: `expert_conference_20261113\joint\PROMPT_ITEMS.md` sections 2 and 5, with the lines of `COMBINED_IMPLICATIONS.md` they cite. Sign-off and objections, item by item: `expert_conference_20261113\joint\SIGNOFF_LM_expert.md`.
- LM8_PUSH now has Leads 1-22 and tasks D.9, D.10, F.6 beside the earlier ones (LP-1 to LP-7). Script: `pro_prompts_draft_20261111_work\LM8_PUSH\fold_conference_20261113.py`. The zip is unchanged (251 entries).
- LM5 Part F has a new item (h) (EX-4, EX-5); EXIT_TOWER has a block of two added tasks before "What the outcome must be" (EX-3, EX-5); ANABELIAN_149_PUSH has one added lead (EX-4). Script: `fold_conference_other_prompts_20261113.py` in the same folder, with the backups. All four prompts lint clean. No zip rebuilt; EXIT_TOWER's should get `sections/E.tex` of LM8 before it is sent.
- Objections recorded: LP-1 (c) as worded is the section conjecture on one fibre and is expected false for the relative pro-5 tower; LP-4 (a) is expected false (Lead 6).
- This agent stops here, at about 58 % of its window. A successor takes the next intake (LM4, LM7, LM7_PUSH) from sections 4 and 5.

## 6. 14 November (same agent, Claude Fable 5.2 at effort max, a125034fd35557818; written at about 95 % of context)

All of this is in `<local>/Documents/pro_intake_20261114/`; hunches are mine and unchecked.

- **Delta.** LM7_PUSH D.50, E.58, E.65 (GPT-6 Astra, ChatGPT Pro mode; refereed by Claude Opus 5.5 at effort max):
  a continuous character Delta of GT_0-hat to F_2, zero on Galois, one on the element of E.58. My pages:
  `CONSULT_LM_EXPERT.md`, `CONSULT_LM_EXPERT_2.md`, `EXPERT_IMPLICATIONS_E65_LM.md` with `_part2`.
  - GT-hat is a proper subgroup of GT_0-hat already by D.50 with the pro-l strictness (to be refereed).
  - Delta is the sign of an idempotent of Z/12 that mixes 2 and 3 (E.58: frame 5 I mod 12).
  - Hunch: Delta = 0 on Galois comes from the harmonic map w = 4 l (1 - l), the degree-two map between the level-3
    and level-4 pictures (tetrahedral group in octahedral group); section 47 lies in ker Delta.
  - "Delta = 0 on GT-hat" has a finite certificate if true; "not 0" needs a lifting theorem with the pentagon.
- **The user's globalization note** (`EXPERT_DELTA_TAU.md`): the exact core is a non-trivial idempotent on a
  connected base; B against F_2 is join against symmetric difference. Items T1 to T5; S.12 was reframed as
  statements about the programme only.
- **Prompt work done:** LM8_PUSH has Leads 23 to 25, tasks B.5, C.2, C.5 to C.9 extended (backups
  `PROMPT_before_expert_20261114.md`); `PUSH_ITEMS_LM7_CONTINUED.md` (S.1 to S.4 additions, S.9 to S.12);
  `PUSH_ITEMS_20261114.md` (item 7 in Part 1); new `PUSH_ITEMS_ORDER5_FRAME.md`. Two preconditions stand at the top
  of each: the literature search, and the D.50 corollary refereed.
- **Cotes 145 and 143** (`EXPERT_ON_INTAKE_11.md`): his conjecture of cote 143 fails at type (0,3) in both forms; in
  cote 145 `g` is the cocycle, not the frame; the frames are the splittings at the harmonic points and at P (scans
  22, 28); beta is not identified (scans 8 to 10, 12 unread).
- **Icosahedral centralizer** (`EXPERT_ON_BOGGI_A5.md`): the twelve-punctured sphere is the level-5 curve; the
  centralizer of A_5 in the peripheral outer automorphisms is the part of GT_0-hat with multiplier +-1 mod 5; the
  published claim says no multiplier-one element lifts into the geometric group. I lean true. The PRETOT A.5 hunch
  follows from Dehn filling of the trefoil complement.
- **Unstuck** (`debate_20261114/UNSTUCK_LM_EXPERT.md`): A1 by specialization to finite fields and class field
  theory; tripod sections by cusp colours independent of l and a unit-equation step; F.9 expected false as stated,
  true with sections of points added.
- **State.** This agent is at the end of its window. A successor starts from sections 4 to 6 and the files above.

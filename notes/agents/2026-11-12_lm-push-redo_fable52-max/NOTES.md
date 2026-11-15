# Assembly of LM4, LM5, LM6 (redo of 12 Nov 2026): notes

Author: Claude Fable 5.2, effort max (fork C of the LM expert successor). Written 12 Nov 2026, 13:10–13:31 UTC
(14:10–14:31 on the machine's clock, WEST), clock read with `date`. No `PROMPT.md` was changed, no `PROMPT_before_redo_20261112.md` was made,
the upload folders in `pro_prompts_draft_20261111\` were not touched (those of LM4, LM5, LM6 are empty).

## 0. What exists and how to use it

All under `pro_reviews_max_20261112\PUSH_REDO\`.

| File | What it is |
|---|---|
| `build_frames_20261112.py` | Builds the frames from the work tree by the recipe of `RECORD.md`, with every step asserted (it fails if an input is not what the recipe assumes). Already run. Rerun only if an input changes; it overwrites edited frames only with `--force`, keeps the `"apply"` decisions, and never touches `after_blocks.md`. |
| `assemble_20261112.py` | The one command. `python -I assemble_20261112.py` writes `assembly\<name>\PROMPT_assembled.md` and `STRUCTURE.txt` and prints warnings and problems. `--install` (not run on the work tree) copies each current `PROMPT.md` to `PROMPT_before_redo_20261112.md` if absent and then writes `PROMPT.md`; it installs nothing if any prompt has a problem. `--only LM4,LM6` selects; `--parts LM4=file` takes another Parts file. |
| `assembly\<name>\head.md` | The prompt up to where new After-blocks belong: title, DRAFT line, "What is to be settled", Leads, and (LM4, LM5) the blocks After CATHOT / GALOIS / STRATA / PATHS of the base. |
| `assembly\<name>\after_blocks.md` | Empty. The expert writes the new blocks here. Empty = the prompt is assembled without one (a warning is printed). |
| `assembly\<name>\mid.md` | The section "What the outcome must be" (five items, the fifth is the disconnect clause). |
| `assembly\<name>\tail.md` | After the Parts: the `---` line and the common block of the base (rules 1–10). For LM6 it begins with Part E of the base. |
| `assembly\<name>\proposed_edits.json` | Edits I did not apply. Set `"apply": true` on an entry to accept it; the assembler applies it to its frame (its `old` must occur exactly once). |
| `assembly\<name>\void_guard.json` | Hashes of the sentences (50 characters or more) of the current, void `PROMPT.md` that are in no frame. The assembler refuses a prompt that contains one of them, wherever it comes from (After-blocks, Parts, a hand-edited frame). |
| `assembly\<name>\BUILD_REPORT.json`, `STRUCTURE.txt` | What was baked in and dropped; headings, words per section, scans named. |

Assembled text = `head` + `after_blocks` (if not empty) + `mid` + the Parts file with its leading HTML comment
stripped + `tail`, each piece trimmed and joined by one blank line, LF line ends, UTF-8.

The assembler stops (exit 1, nothing installed) on: a missing or doubled "## What the outcome must be", "## Parts",
common block, disconnect item, rule 9 or rule 10; "Asked:"; the three void headings; rule 11; an HTML comment; a
sentence of the void rewrite; placeholder words in `after_blocks.md` (TODO, TBD, PLACEHOLDER, XXX, "[...]", "to be
written", "to be filled"); Part letters that are not A, B, C, … in order (this catches a Part E written into the LM6
Parts file while the base's Part E is still in `tail.md`: delete it from `tail.md` then). It warns on: an empty
`after_blocks.md`; a Part without a line "Done for Part X"; a Part without lettered tasks; the words "follow-up task".

Tested: the install path, twice, on a scratch copy of the three `PROMPT.md` (`--work-root`, in the session
scratchpad): the copy to `PROMPT_before_redo_20261112.md` is made once and not overwritten, the installed file equals
`PROMPT_assembled.md`. The guards were tested on a scratch copy of `assembly\` (a void sentence, "TODO", a doubled
Part E, all proposals accepted). `--install` was never run on the work tree.

## 1. LM4_FINITE_GROUP_ACTIONS

### 1.1 Structure of the assembled prompt (7,143 words, 42,920 characters)

```
   25  # LM4_FINITE_GROUP_ACTIONS: finite groups acting on surfaces and on groups with loops (§§12–18, 23–25 bis, 31)
 1023  ## What is to be settled                                   (intro + items 1–7)
  191  ## Leads (unverified; prove or refute each)                (Leads 1–3)
  179  ## After the first Dérivateurs return (added 11 November 2026)   (CATHOT)
  226  ### After GALOIS (added 11 November 2026)
  547  ### After STRATA (added 11 November 2026)
  524  ### After PATHS (added 11 November 2026)
       [new After-blocks go here]
  503  ## What the outcome must be
  116  ## Parts                                                   (intro paragraph of the Parts file)
  453      Part A. Groups with loops: the rigidity statements          tasks a b c d
  775      Part B. Finite groups acting on surfaces: sections, fixed points, μ   a b c d e f
  629      Part C. The 2-equivalence, realization, drilling            a b c d e
  403      Part D. The profinite theory                                a b c d
  245      Part E. §25 and §25 bis                                     a b
  141      Part F. What the later sections use                         (1) (2) (3), no letters
  270  THE TEXT YOU ARE GIVEN
   70  WHAT IS ATTACHED
  493  RULES OF PROOF (rules 1–10)
  198  WHAT TO DELIVER
   44  (closing paragraph)
```
Pieces: head 2,775 words, mid 509, Parts 2,763, tail 1,096.

### 1.2 What came from which file

- `head.md`: `PROMPT_before_push_20261111.md`, lines 1–50, except: lines 7, 9, 10, 11, 13, 14 (the intro and items
  1, 2, 3, 5, 6 of "What is to be settled") are those of the current `PROMPT.md` with the "**Asked:**" clause cut off
  (second-pass edits E1–E6 of `second_pass_edits_20261112.py`, Claude Opus 5.5, effort max); line 3 has the second
  pass's date (E0: "DRAFT, provisional (12 November 2026)"). Items 4 and 7 were not changed by the second pass.
  Checked by the script: the void rewrite changed lines 1–50 of the base only by appending the seven "Asked:"
  clauses; the second pass changed, outside "What is to be settled", only line 3 (E0) and lines 31, 38, 46 (E8a–e);
  `head.md` with the five proposals LM4-P1..P5 applied is exactly the current head without the "Asked:" clauses.
- `mid.md`: current `PROMPT.md`, lines 78–94; items 1–4 are word for word those of
  `PROMPT_before_disconnect_clause_20261111.md`, item 5 is the disconnect clause; one referential change (1.4, R1).
- Parts: `PUSH_REDO\LM4_PARTS_redo_20261112.md`.
- `tail.md`: `PROMPT_before_push_20261111.md`, lines 65–96 (the `---` line and the common block).

Second-pass edits not carried, and why: E7, E8f–h, E13a–b sit in the dropped blocks; E9a–c, E3b, E10, E11, E12a–b
sit in the Parts of the void rewrite. Of these, the following corrections of reading are in neither the head nor the
new Parts (for the second pass of the Parts):
- E9a: `I = ∅` is not excluded (scan 82, now read without doubt), so the rank `2g + ν − 1` of `π_ab` (scan 86) holds
  only for `ν ≥ 1`; `(S², pt)` is admitted "où pourtant on a π=0" (scans 91–92), the one admitted type where `κ_i` is
  not injective (scans 92, 97).
- E9b: scan 98 derives "extension of Σ by π = homomorphism Σ → Autext(π)" from the trivial centre and excepts only the
  annulus; the torus is omitted (P10 note R15). The head still says "the torus is omitted there, see Part A" (1.4, R2).
- E11: scan 166, the `Π_1` in the subscript of the bottom object is read as struck, so the object is `B_X` (fix
  01-030). This concerns LM5 Part C (a), which cites scans 163–169 without it.
E9c, E3b, E10, E12 are covered by the new Parts A (c), B (c), B (d) and by item 5 as carried (E5).

### 1.3 Dropped

| What | First line | Length |
|---|---|---|
| Block | `### After LM3 (added 11 November 2026)` | 5,361 characters, 908 words |
| Block | `### After BISITE and the seven Dérivateurs returns (added 11 November 2026)` | 2,037 characters, 337 words |
| Block | `### After LM2 (added 12 November 2026)` | 3,412 characters, 609 words |
| Parts of the void rewrite | `Every part asks for mathematics: a theorem with its proof, …` | 17,997 characters, 3,078 words |
| Rule 11 of the common block | `11. A linearization is a statement to prove. …` | 486 characters |
| "**Asked:**" clauses | items 1–7 | 7 clauses, 397 words |

The Parts of the base that the new Parts replace: 1,735 characters, 275 words.

### 1.4 References that the new Parts no longer match

Applied (purely referential):
- **R1** (`mid.md` line 3; the same in LM5 and LM6). "for each lettered task (a), (b), … and each numbered follow-up
  task of every part" → "… and each numbered task of every part". "Follow-up" tasks existed only in the void Parts;
  the new Parts have numbered tasks (Part C (d) I–III, Part F (1)–(3)).

Listed, not applied:
- **R2** (`head.md` line 9, item 1): "the torus is omitted there, see Part A". The new Part A (b) treats `Centr(π)`
  for the four abelian types, so the pointer holds, but nothing in it asks about scan 98's statement on extensions
  and outer actions, which is what fails for the torus. Either add that to Part A (b) (text of E9b in
  `second_pass_edits_20261112.py`) or leave the pointer as it is.
- **R3** (`mid.md` lines 3, 12, 14): the report table has "one line per item, per lead and per lettered task" and the
  work is finished when "every item, every lead and every lettered task" has reached the bar. Part F has numbered
  lemmas (1)–(3) and no letters, so it has no line and no bar. Fix in the Parts: letter Part F's lemmas (a), (b), (c);
  or change "lettered task" to "lettered or numbered task" in the three places of `mid.md`.
- **R4** (`head.md` line 10, item 2): "Ça doit être le seul contre-exemple" (scan 179, margin, on the orientation
  reversing case). No Part asks whether it is the only one (the void Parts did; the new Part B (d) asks only for
  d ⇒ a of scans 180–181). Proposed: add to Part B (d) "prove or refute that the example of scan 179 is the only one".
- **R5** (`head.md` line 13, item 5): "Le plus agréable serait que ce soit un homotopisme" (281). The new Part C (a)
  cites the margin of scan 281 for the corrected conditions in the abelian types; no ask says what the homotopy
  statement is and proves it (the base's Part C did). Proposed: one sentence in Part C (a) or (c).
- **R6** (`head.md` lines 25, 38, 46): the blocks After CATHOT, STRATA, PATHS say "followed step by step by the author
  of this prompt", "reviewed by the author of this prompt (Claude, Anthropic; the review is to be attached as
  `STRATA_review/REVIEW_author.md`)". `RECORD.md` step 4: these reviews are being redone at effort max by the
  Dérivateurs line; update before sending. The five second-pass changes "to be attached" → "attached" in these blocks
  are the proposals LM4-P1..P5 (not applied: the blocks were to stay as in the base).
- **R7** (`tail.md` line 10, common block, all three prompts): "`OVERVIEW.md` (… from which the leads below come)" and
  rule 7 "the leads marked "Lead" below": the Leads are above. Wording of the shared common block; left.

### 1.5 Asks that are status-shaped (push standard, rules 1–7), and contradictions with the Parts

- `head.md` line 27 (After CATHOT): "In Part C, say exactly which level of the mapping spaces … each of his fidelity
  conditions concerns … and where the excluded types … fail". Line 33 (After GALOIS): "When you say which level …,
  place it on this ladder for `r = 0, 1, 2`, or say why it is not of this form." Line 48 (After PATHS): "In Part C say
  to which layer each of his statements belongs …, and which of them survive for infinite or profinite `Γ`." Verb
  "say" on its own (rule 1). They are tied to Part C, whose (a) and (b) demand the proofs; rewording them is a change
  to blocks that were to stay as in the base, so they are left.
- `tail.md` line 29 (common block, all three prompts): "`<ID>_report.md` (what you read, what you computed,
  corrections to the leads and to the notes, what remains open)". "What remains open" describes a file; rule 10 and
  the outcome section bound it. Left.
- No contradiction found between head, mid, tail and the new Parts of LM4.

## 2. LM5_MULTI_GALOIS_TOPOI

### 2.1 Structure of the assembled prompt (6,990 words, 42,531 characters)

```
   38  # LM5_MULTI_GALOIS_TOPOI: the topoi of the Longue Marche. … (§§1–4, 14, 16, 20)
  282  ## What is to be settled                                   (intro on §§1–4 + three items: §14, §16, §20)
  281  ## Leads (unverified; prove or refute each)                (Leads 1–4)
  237  ## After the first Dérivateurs return (added 11 November 2026)   (CATHOT)
  132  ### After the second review of CATHOT (added 11 November 2026)
  843  ### After GALOIS (added 11 November 2026)
 1001  ### After STRATA (added 11 November 2026)
  711  ### After PATHS (added 11 November 2026)
       [new After-blocks go here]
  503  ## What the outcome must be
  110  ## Parts
  533      Part A. §§1–4: multi-Galois topoi                            tasks a b c d e f
  371      Part B. §14: the mixed topos and the cohomology of hole plugging   a b c d
  294      Part C. §16 and §12: van Kampen, group actions on topoi, classifying topoi of exterior groups   a b c d
  339      Part D. §20: the 2-isotopic description of 2-spheres         a b c d
  129      Part E. Relation to the higher theory                        no letters
  270  THE TEXT YOU ARE GIVEN
   70  WHAT IS ATTACHED
  493  RULES OF PROOF (rules 1–10)
  198  WHAT TO DELIVER
   44  (closing paragraph)
```
Pieces: head 3,608 words, mid 509, Parts 1,777, tail 1,096.

### 2.2 What came from which file

- `head.md`: `PROMPT_before_push_20261111.md`, lines 1–62, with recipe step 6 (four changes in lines 9–11, see 5).
  Checked by the script: the current head is the base head plus three "Asked:" clauses and nothing else.
- `mid.md`: current `PROMPT.md`, lines 88–104 (R1 applied). It says "each of the 3 items of "What is to be settled"".
- Parts: `PUSH_REDO\LM5_PARTS_redo_20261112.md`.
- `tail.md`: `PROMPT_before_push_20261111.md`, lines 75–106; identical to LM4's.

### 2.3 Dropped

| What | First line | Length |
|---|---|---|
| Block | `### After LM3 (added 11 November 2026)` | 3,428 characters, 566 words |
| Block | `### After BISITE and the seven Dérivateurs returns (added 11 November 2026)` | 1,876 characters, 308 words |
| Block | `### After LM2 (added 12 November 2026)` | 2,353 characters, 410 words |
| Parts of the void rewrite | `Every part asks for mathematics: a theorem with its proof, …` | 12,031 characters, 2,061 words |
| Rule 11 of the common block | as in LM4 | 486 characters |
| "**Asked:**" clauses | the three items | 3 clauses, 130 words (never taken: the head is the base's) |

The Parts of the base that the new Parts replace: 1,900 characters, 291 words.

### 2.4 References that the new Parts no longer match

Applied: R1 (as in LM4).

Listed, not applied:
- **R8** (title, line 1, and "What is to be settled"): the prompt is announced for "§§1–4, 14, 16, 20" and has three
  items. The new Part C (d) adds §12, scans 103–109 (classifying topoi of exterior groups), which no item, no lead and
  not the title name; `BACKGROUND.md` does not list package LM_P011 (scans 101–110). Proposed: a fourth item for it
  (then "3 items" in `mid.md` line 3 becomes "4 items") and "(§§1–4, 12, 14, 16, 20)" in the title.
- **R9** (`mid.md` lines 3, 12, 14): Part E has no lettered task, so by the outcome section it has no line in the
  report table (as R3). Proposed: letter its three demands (construct the common generalization; prove that `E_[1]`
  is its 1-truncation and the tower of Part A (c) its Postnikov tower; decide which statements extend).
- **R10** (`head.md` line 30, After the second review of CATHOT: "say for each of his statements whether it is about
  the pro-object or about its limit, and prove it for the one he uses"; line 36, After GALOIS: "his own definitions in
  §§1 and 3"). The new Part A (e) reads §3 as a bare title (scan 16) that the answer has to write; he has no
  statements or definitions there. The two sentences then apply to what Part A (e) constructs. Rewording is a change
  inside base blocks: left.
- **R11** (`head.md` line 48, After STRATA: "Decide from his definition (scans 116–134) which of the two `B_{X,U}`
  is"): the same wrong range as in the heading sentence; proposal LM5-P1 (not applied because the block was to stay
  as in the base). Without it the assembled prompt gives two ranges for §14 (119–137 in line 9, 116–134 in line 48).
- **R12** (`head.md` line 49, After STRATA: "LM3_TEICHMULLER_TOWER starts from it"): LM3 has been answered; the new
  After-block will say so.
- **R13** (`head.md` line 3): "waits for the second pass of the pilot packages (cote 140-2, scans 1–100)". Every
  package this prompt uses has a second-pass text now; proposal LM5-P4.
- **R14** (`head.md` lines 22, 45, 55): "the author of this prompt" as reviewer of CATHOT, STRATA, PATHS (as R6).

### 2.5 Status-shaped asks, and contradictions with the Parts

- `head.md` line 24: "use it to state which of his constructions extend to higher levels …"; line 37: "for each
  statement of Parts A–C name the level and the coefficient theory at which it holds"; line 38: "In Part C say
  whether his statement for topoi is of the direct kind, and in Part E whether B.3's proof … has a counterpart";
  line 47: "should be stated so that these are instances, or the difference said"; line 50: "add them to the list of
  Part E, with their exact hypotheses". Verbs "state", "name", "say" on their own; the new Part E turns the first two
  into "decide, with proof or counterexample". Left (base blocks).
- **Lead 2 against Part B (a).** Lead 2 says `B_{X,U}` is the Kummer-étale or logarithmic topos of `(X, S)`; After
  STRATA (line 48) asks to decide between that (candidate (b)) and the constructible topos (candidate (a)); the new
  Part B (a) asks to prove that `B_{π_1,U} → B_{X,U}` is an open induction morphism "with closed complement
  `B_{π_1,D}` and gluing functor `σ_* ρ^*`", which is candidate (a). Not a contradiction (leads are to be proved or
  refuted), but the Parts now presuppose the answer that the head asks to decide. No Part names Lead 2; the outcome
  section still requires a numbered statement for it.

## 3. LM6_POINTS_AS_SECTIONS

### 3.1 Structure of the assembled prompt (4,458 words, 27,019 characters)

```
   25  # LM6_POINTS_AS_SECTIONS: points as sections. … (§§5–11, 13, 32–33, 51.16, 52.3)
  405  ## What is to be settled                                   (intro on §§5–13 + items 1–4)
  238  ## Leads (unverified; prove or refute each)                (Leads 1–4)
       [new After-blocks go here; the base has none]
  503  ## What the outcome must be
  153  ## Parts
  556      Part A. His conjecture of §§5–13 against the theorems        tasks a b c d e
  819      Part B. Sections and points                                  a b c d e f g
  290      Part C. Real structures                                      a b c
  214      Part D. Mordell through splittings                           a b c
  116      Part E. Fermat (item 4)            from the base (in tail.md); no letters, no "Done for Part E"
  270  THE TEXT YOU ARE GIVEN
   70  WHAT IS ATTACHED
  493  RULES OF PROOF (rules 1–10)
  198  WHAT TO DELIVER
   44  (closing paragraph)
```
Pieces: head 704 words, mid 509, Parts A–D 2,034, tail 1,211 (Part E 115 + common block 1,096).

### 3.2 What came from which file

- `head.md`: `PROMPT_before_push_20261111.md`, lines 1–20 (CRLF in that file; the frames are LF), with recipe step 6
  in line 11 (item 3). The current head is the base head plus four "Asked:" clauses and nothing else (checked).
- `mid.md`: current `PROMPT.md`, lines 50–66 (R1 applied). "each of the 4 items".
- Parts A–D: `PUSH_REDO\LM6_PARTS_redo_20261112.md`.
- `tail.md`: line 31 of the base (Part E), then lines 33–64 (the `---` line and the common block).

### 3.3 Dropped

| What | First line | Length |
|---|---|---|
| Block | `## After LM3 (added 11 November 2026)` | 4,363 characters, 724 words |
| Block | `## After BISITE and the seven Dérivateurs returns (added 11 November 2026)` | 1,628 characters, 274 words |
| Block | `## After LM2 (added 12 November 2026)` | 3,240 characters, 558 words |
| Parts of the void rewrite | `Every part asks for mathematics: a theorem with its proof, …` | 11,941 characters, 2,027 words |
| Rule 11 of the common block | as in LM4 | 486 characters |
| "**Asked:**" clauses | items 1–4 | 4 clauses, 155 words (never taken) |

Parts A–D of the base that the new Parts replace: 272 of the base's 387 words of Parts.

### 3.4 References that the new Parts no longer match

Applied: R1.

Listed, not applied:
- **R15** (`head.md` line 10, item 2): "pathological lifts (413)" and "conditions "faisant intervenir les Frobenius"
  and an intrinsic description of admissible outer actions (480)". Neither scan 413 nor the Frobenius conditions is
  named in the new Parts (the base's Part B asked for both). Proposed: add both to Part B (c) or (f).
- **R16** (`head.md` line 11, item 3): "classes in `𝒯_g`, "Nous montrerons (on l'espère !)" (440); anti-involutions of
  a cylinder (457); "Ce sont peut-être les sous-groupes abéliens-libres maximaux" (470), with the strips as rank-one
  subgroups". The new Part C sends the classification and `H ≅ Z^g` to LM4 Part B (e) ("do not redo them here"). LM4
  Part B (e) covers 440, 449–470 and three questions of scan 470 (intrinsic characterization, maximal free abelian,
  normalizer); the third question on that scan in the transcription is the one on the `SL(2, Z)_j` of the
  "lanières" as rank-one subgroups, which no Part of LM4 or LM6 asks. Proposed: add it to LM4 Part B (e); and say in
  item 3 of LM6 that these points are asked in LM4.
- **R17** (`head.md` line 18, Lead 3) against Part C: the Leads are "prove or refute each" and the outcome section
  wants a numbered statement per lead; Lead 3 is about the Weichold–Harnack classification and the maximal free
  abelian subgroups (Birman–Lubotzky–McCarthy), which Part C tells the model not to redo. This is a contradiction
  between head and Parts. Proposed: cut Lead 3 down to its middle clause (the real section conjecture) with a pointer
  to LM4 for the rest.
- **R18** (`head.md` line 17, Lead 2): "Known: … the birational `p`-adic case (Koenigsmann; Pop) … Open in general."
  The intro of the new Parts names the 2026 claim (local `p`-adic section conjecture for proper curves of genus ≥ 2)
  as a tool; Lead 2 does not mention it. Not a contradiction over number fields; the lead is stale against the Parts.
- **R19** (`tail.md` line 1, Part E of the base): no lettered tasks and no "Done for Part E", unlike Parts A–D (as R3);
  it ends "… and say what a proof of Fermat along his lines would still require" (status-shaped, rule 1).
  `RECORD.md`: Part E is to be redone after §§50–52 are read.
- **R20** (files): the intro of the new Parts says the 2026 paper is "attached". `BACKGROUND.md` of LM6 names only
  "the proof pack `019_…`" in its void section "after LM3 and after BISITE"; the PDF
  `recent_results_20261110\papers\019_The-p-adic-section-conjecture-October-6-2026.pdf` has to be on the list.

### 3.5 Status-shaped asks

Only R19. Head and mid of LM6 have no asks besides the Leads' "prove or refute each".

## 4. The form of an After-block of the base (for the new blocks)

Example: `### After GALOIS (added 11 November 2026)` in LM4, 226 words (the others: 179 to 1,001 words).
- Heading: "After <package> (added <day month year>)". In LM4 and LM5 the blocks after the first are level 3, under
  "## After the first Dérivateurs return (added 11 November 2026)"; the void rewrite put "### After LM3" at level 3
  there and "## After LM3" at level 2 in LM6, which has no such section. The assembler accepts both levels. A block
  on LM3 and LM3b is not a Dérivateurs return, so level 2 ("## After LM3 and LM3b (added 12 November 2026)") fits the
  outline of all three prompts; level 3 in LM4 and LM5 continues the existing run. Either way it lands between the
  last base block (or the Leads) and "## What the outcome must be".
- Opening paragraph: the package and what it is; who answered ("GPT-6 Astra, ChatGPT Pro mode"); how its statements
  are cited ("by their numbers"); the state of the review in one sentence, with what was followed in full and what
  was not ("the author of this prompt has read them in statement only, and the review is not finished: verify what
  you use"); where the cited sections are attached (`GALOIS_return/`).
- Then bullets. Each starts with a bold title that names the Part it serves ("**A ladder of levels to state the
  fidelity conditions against (Part C).**"), gives the cited statements by number with their exact content and
  hypotheses ("GALOIS C.4–C.5: for a map of spaces `v` …"), marks inferences of the prompt's author as "unverified",
  and ends with what to do with it in that Part.
- Last bullet: the effect on the leads ("Nothing in the leads of this prompt is refuted or settled by GALOIS.").
- The base blocks name the answering model without its effort setting and the reviewer as "Claude, Anthropic". New
  blocks should carry both in full: "GPT-6 Astra, effort Pro (ChatGPT Pro mode)"; "Claude Fable 5.2, effort max".
- A heading "After LM3 and LM3b …" passes the assembler; only the void headings ("After LM3 (added 11 November 2026)",
  "After BISITE and the seven Dérivateurs returns", "After LM2 (added 12 November 2026)") and void sentences are
  refused. `grep -c "After LM3"` will then no longer be 0, by design.

## 5. The recipe, step by step, and what did not check

1. Copy of `PROMPT.md` to `PROMPT_before_redo_20261112.md`: left to `--install`.
2. Base `PROMPT_before_push_20261111.md`: yes.
3. Outcome section with the disconnect item from the current `PROMPT.md`: yes (`mid.md`). LM4 second-pass edits:
   E0–E6 carried without the "Asked:" clauses (1.2).
4. Blocks After LM3, After BISITE, After LM2 and rule 11: dropped; the void guard proves that none of their
   sentences is in an assembled prompt. Blocks After CATHOT / GALOIS / STRATA / PATHS: as in the base, byte for byte
   (LM4 and LM5; LM6 has none).
5. Parts replaced; LM6 keeps Part E of the base.
6. Scan corrections, each checked in `LM_EXPERT\work\reading2\` (markers `=====SCAN N=====`):
   - LM5 §14 "scans 116–134" → "119–137": heading "14. Digression cohomologique" on scan 119; the last paragraph of
     §14 and the heading of §15 are on scan 137. Checks.
   - LM5 §16 "scans 158–178" → "160–178": heading on scan 160. The start checks. The end does not quite: the last
     sentence of §16 ("Le temps / semble donc mûr enfin pour s'expliquer sur l'opération inverse hypothétique de
     « forage de trous »") runs onto the first three lines of scan 179, before the heading of §17. Applied as the
     recipe says (178); to be exact it would be 160–179.
   - LM5 §20 "scans 231–260" → "233–250": heading "_20_ Description 2-isotopique de la cat. des sphères topologiques"
     on scan 233 (scans 231–232 are the end of §19); §21 starts on scan 251. Checks. (GROTHENDIECK_NOTES gives
     2:sc232–250 for §20; the heading is on 233.)
   - LM5 "bien profond" (259): on scan 259, in §21 ("… soit simplement connexe … est bien profond"). Checks. The
     sentence now reads: "bien profond" for the simple connectedness of the Teichmüller space `M̃_{g,ν}` (scan 259,
     which is in §21, not in §20).
   - LM6 item 3 "136–148, 436–470" → "137–151, 437–471": §15 heading on scan 137, theorem on 148–149, corollary on
     150–151; first §33 heading on scan 437, its last lines on scan 471, second §33 on scan 472. Checks.
   Found beside them, not applied (proposals): the range "scans 116–134" again in LM5's After STRATA (LM5-P1); the
   title of §20 quoted from the Grothendieck Circle table ("… de la catégorie des isomorphismes topologiques") where
   the text has "des sphères topologiques" and his own table of contents "des 2-sphères(?) topologiques" (LM5-P2);
   "Au concours !" placed at the fidelity bounds of scans 247–248 where it is on scan 236, about the ∞-isotopic
   description (LM5-P3; the new Part D (b) has it right).
7. Push check of the Parts: not mine; 1.5, 2.5, 3.5 give what head, mid and tail contribute.

Rules 9 and 10 of the push standard are in the common block of all three bases, in the standard's wording (rule 10
with double quotes around "open, see [reference]"); nothing was added.

## 6. `_COMMON_BLOCK.md` against the common rules in the base prompts

- The common block embedded in the three bases (from the `---` line to the end) is the same text in all three: 32
  lines, 1,096 words, rules 1–10.
- `pro_prompts_draft_20261111\_COMMON_BLOCK.md` (changed by the void rewrite, 12 Nov 00:47) is that text plus one
  line, rule 11 ("A linearization is a statement to prove. …", 486 characters), and nothing else. The current
  `PROMPT.md` of the three prompts ends with exactly this file.
- So a prompt regenerated from `_COMMON_BLOCK.md` gets rule 11 back. Rule 11 came with "After LM2" and is dropped
  here by instruction; its content does not depend on a review, so the expert can re-add it on its own authority
  (as a line in `tail.md` after rule 10; the assembler's check for rule 11 then has to be removed from `FORBIDDEN`).

## 7. Open decisions for the expert

1. Write `after_blocks.md` for the three prompts (form: 4). Heading level: 2 or 3 in LM4 and LM5.
2. LM4-P1..P5 (second-pass "attached" for "to be attached" in the blocks After GALOIS, STRATA, PATHS): accept when
   the zip holds those folders, or leave.
3. LM5-P1 (scan range in After STRATA), LM5-P2 (title of §20), LM5-P3 ("Au concours !" at scan 236), LM5-P4 and
   LM6-P1 (DRAFT line: date 12 November; LM5 no longer waits for a second pass).
4. R3, R9, R19: Parts without lettered tasks (LM4 F, LM5 E, LM6 E) fall outside the outcome section's table and bar.
5. R4, R5, R15, R16: elements of the items that no new Part asks (scan 179 "seul contre-exemple"; scan 281
   "homotopisme"; scan 413 pathological lifts; scan 480 Frobenius conditions; scan 470 "lanières").
6. R8: §12 (scans 103–109) is in LM5 Part C (d) and in no item, lead or title.
7. R17, R18 (LM6 Leads 2 and 3 against the Parts) and the remark on Lead 2 of LM5 (2.5).
8. §16's range: 160–178 as in the recipe, or 160–179.
9. Rule 11: stays out, or back in on the expert's authority.
10. The reviews cited in the base blocks ("by the author of this prompt") are being redone (R6, R14).
11. The second-pass readings that lived only in the void Parts (1.2: E9a, E9b, E11).

## 8. `BACKGROUND.md` (not touched)

The three `BACKGROUND.md` in the work tree are packaging lists; they do not enter the prompt. Before a zip is built:
each ends with a section "Added 11 November 2026: after LM3 and after BISITE (push rewrite)" that lists the void
reviews under `pro_reviews_20261111\` and, for LM6, proof packs; LM5's and LM6's scan lists carry the old ranges
(LM5: "116–134, 158–178, 231–260"; LM6: "136–139, 148, … 457–470"); LM5's still says P01, P02 are not second-passed;
the scans named by the new Parts go well beyond the lists. `STRUCTURE.txt` of each prompt gives the scans named in
the assembled prompt and in the Parts alone (the cote is not distinguished: LM6 also names scans 172–178 of cote
140-4, and LM5's "1–100" comes from its DRAFT line).

## 9. Final check (12 Nov 2026, 13:26 UTC)

sha256 of the work-tree `PROMPT.md`, at the start (13:10 UTC) and at the end, identical:
```
250eaf50f20986c091791f5f36bc8cb159ea09a35a025f15db5dd15b4f256206  LM4_FINITE_GROUP_ACTIONS\PROMPT.md
a1168c845c6e356f3ecb2da33c94754b5ca73431c57224bac66c8fbc672efc01  LM5_MULTI_GALOIS_TOPOI\PROMPT.md
4ce3afc40326093f8eb6de87930dd79379b82709992703c97d7b7a947f6e5255  LM6_POINTS_AS_SECTIONS\PROMPT.md
```
No `PROMPT_before_redo_20261112.md` exists in the work tree.

`grep -c` on `assembly\<name>\PROMPT_assembled.md` (LM4, LM5, LM6), with the counts in the current `PROMPT.md` for
contrast:
```
"Asked:"        0 0 0     (current: 7 3 4)
"After LM3"     0 0 0     (current: 3 2 2)
"After BISITE"  0 0 0     (current: 1 1 1)
"After LM2"     0 0 0     (current: 1 1 1)
```
Also 0 in all three: "LM2", "BISITE", "LM3b", "11. A linearization", "follow-up", "pro_reviews_20261111".

sha256 of the assembled prompts (empty `after_blocks.md`, no proposal applied) and of the Parts files they were
assembled from:
```
2f655f3bc9ac3645c25d76444f822033a5adf85ac9e0f7ddd3d9a36a742667b5  LM4_FINITE_GROUP_ACTIONS\PROMPT_assembled.md
f2822f0401302a2a15a1a67a20141d74308c5c03dd4f2ba696f854fe52954edf  LM5_MULTI_GALOIS_TOPOI\PROMPT_assembled.md
1fab77e53e4bfb26cce0eb0236ccb9054cda01d3fa39eaf7a832dba57b34dcc3  LM6_POINTS_AS_SECTIONS\PROMPT_assembled.md
1604fcb53ac8a8795c0d98fb7626864c4237d15231e5fc5f0b433b546e3553af  LM4_PARTS_redo_20261112.md
17e92606e268f98f417e24e30649b9767d9d55e53a113e239991756cc382edba  LM5_PARTS_redo_20261112.md
5b02db7038d7ebad8010a1d15f2fe1d161a6f9c8a5dbaa05e39303c9b8dc6852  LM6_PARTS_redo_20261112.md
```
The assembled files change as soon as `after_blocks.md`, a Parts file, a frame or a proposal changes: rerun
`python -I assemble_20261112.py` and read its warnings and `STRUCTURE.txt`.

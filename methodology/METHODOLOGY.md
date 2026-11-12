# La Longue Marche à travers la théorie de Galois: how the transcription is made

Working log of the method, kept for a later write-up (GitHub provenance, a methodology section, a post). Numbers are
measured unless marked as estimates. Dates are 2026.

## 1. Source

- Grothendieck's manuscript *La Longue Marche à travers la théorie de Galois* (1981), digitized by the Université de
  Montpellier (Institut Montpelliérain Alexander Grothendieck): four archive files, cote 140-1 (draft, 37 scan
  pages), 140-2 (manuscript pages 1–292, 575 scans), 140-3 (pages 293–650, 696 scans), 140-4 (pages 650bis–787,
  280 scans): 1,588 scan pages. Each scan is framed by the archive: a header band and a footer with the archive's
  page number.
- Earlier transcriptions used only as witnesses for the second pass, never shown to the first pass: the CSG draft of
  February 2026, Carmona's earlier edition ("galoisI", from the typescript), the Carmona–Künzer typeset 207 pages
  (and its Software Heritage copy), and the Grothendieck Circle's table of contents. They come from one group and
  normalise (abbreviations expanded, deletions and insertions dropped).

## 2. First pass: ChatGPT Pro, one blind package at a time

**Who does what.** The editor runs the packages by hand in ChatGPT Pro (the Pro mode of the editor's ChatGPT
subscription; the model is the one ChatGPT's Pro mode used on the day). Claude (Claude Code) prepares the packages,
the prompt, and the second pass.

**Package:** a folder with ten scan pages and one prompt. Images (`make_lm_packages.py`, then
`make_lm_packages_v2.py`): each page rendered from the archive PDF at 3× (about 1,790 × 2,375 px, close to the
archive's own resolution), the header band cut off, autocontrast (1 % cut-off) and an unsharp mask (radius 2, 120 %,
threshold 3), JPEG quality 88. From version 2 on, a landscape spread is split into a left and a right image.

**Running a package:** open a new Pro chat, drag in everything in the folder (prompt and images), write "Follow the
attached prompt.", and save the single zip Pro returns in `answers`.

**The prompt** (`PROMPT_TEMPLATE.md`; version 1 in `PROMPT_TEMPLATE_v1.md`):
- a diplomatic LaTeX transcription: only what is on the page, Grothendieck's French, spelling, accents, punctuation,
  abbreviations and numbering as written, mathematics with the same letters, alphabets, indices and arrows;
- the state of the page with a few macros (`\scanpage`, `\mspage`, `\deleted`, `\inserted`, `\margin`, `\uline`,
  `\diagram`, `\figure`) and explicit doubt (`\unsure{a}`, `\unsure{a|b}`, `\illegible{n}`): "A wrong confident
  reading is far worse than an honest mark of doubt";
- a method: read the page, transcribe line by line, re-read the image against the text, only then the next page;
- returned with the transcription: a table of doubts, the abbreviations met, a note on legibility;
- **research notes** (added 4 November at the editor's request), kept apart from the transcription: Grothendieck's
  own conjectures and questions, claims he leaves without proof (and what a proof would need), implications he does
  not pursue on these pages, and the model's own ideas, labelled as such with confidence and reason. Each note gives
  the scan page and its kind. "The notes never change the transcription";
- **one zip** with two files, `<package>_transcription.tex` and `<package>_notes.md` (added 4 November: one download
  per package).

**Version 2 (5 November)**, after the measured pilot (section 4): a section "Where readings go wrong" naming the
typical errors with real examples (a plausible mathematical word in place of the ink; a short condition or symbol
dropped; an insertion attached to the wrong place; inequalities and arrow directions read from the argument rather
than the ink), with the instruction to mark a word `\unsure` whenever not every letter was seen; the archive file
named in each prompt; spreads as two images. On 5 November the remaining 150 packages were generated with version 2
(LM_P011–LM_P160: the rest of 140-2, then 140-3, 140-4 and the draft 140-1; `PACKAGES.md`); none of those scans is a
landscape spread.

## 2a. The prompt is revised in a loop

The prompt is not written once. It is run on a few packages, the output is checked against the scans, the mistakes
that recur are named, and the prompt is changed accordingly; then the next packages are run with the new version and
checked the same way. The changes are kept small, so that each version can be compared with the one before it.

| Step | Date | What was run | What was checked | What changed |
|---|---|---|---|---|
| 1 | 4 Nov | v1 on P01–P02 (scans 1–20) | the whole of both packages, scan by scan, against the archive images and four other transcriptions (`COMPARISON_P01_P02.md`) | research notes added to the task; delivery as one zip |
| 2 | 4–5 Nov | v1 (with notes and zip) on P03–P10 | format and notes of P05–P07; scan 41 spot-checked; P03 in full by the second pass | v2: the section "Where readings go wrong" (the pilot's typical misreadings, with real examples), the archive file named, spreads as two images |
| 3 | 5 Nov | v2 on P011–P019 | quick check of all nineteen returned packages against the two complete witnesses (section 4: disagreement rate, share of disagreements with a doubt mark, format of every zip); one disputed word read at zoom on the scan | v3 from P023: one item added to "Where readings go wrong", on his own spellings (a word normalized to its dictionary form, e.g. *toposique* for *topossique*) and on word endings read from the grammar instead of the ink. P020–P022 kept v2 (they may already have been running) |
| 4 | 5 Nov (done for v2) | v2 on P011–P015 (v3 on its first packages: next) | the second pass on these packages, compared with the v1 packages: errors per word, share of errors carrying a doubt mark, consequential errors | v4 only if a kind of error still recurs, or the doubt marks become too many to be useful |

At each checkpoint the measured numbers go into section 4, and the reasons for each change into this table.

## 3. Second pass: Claude, against the scans and the witnesses

Per package, one Claude subagent (`second_pass/SECOND_PASS_PROMPT.md`):
- images extracted from the archive PDF at the archive's own resolution (`second_pass/prep_images.py`: the embedded
  JPEG of each page, about 1,690 × 2,370 px, plus two overlapping halves);
- the first pass checked line by line against the halves, with crops where a word is hard;
- every scan collated with the witnesses (text extracted with `pdftotext` into `second_pass/witness`): each
  difference beyond normalisation settled on the image; the witnesses are evidence, never authority;
- output: the corrected transcription, a table of changes (first-pass reading, corrected reading, evidence,
  confidence), unresolved places, the witnesses' own errors, and the research notes checked against the corrected
  text (kept, corrected or dropped, with reasons) plus the second pass's own notes.

The research notes of all packages are collected in `NOTES_LEDGER.md` and checked against the rest of the manuscript
and the literature.

## 4. Measured: the pilot packages P01–P02 (scans 1–20)

Compared by Claude scan by scan with the archive images at native resolution and with the witnesses
(`COMPARISON_P01_P02.md`):
- main text (about 1,600 words): Pro made about 22 reading errors (1.4 %); 16 of them carried no doubt mark;
- the table of contents (two low-resolution scans, one a squeezed spread): 14 errors (3.3 %);
- witnesses on the same text: CSG draft about 2 errors, Carmona's earlier edition about 9, Carmona–Künzer about 17
  (several change the mathematics, e.g. ≤ for ≥);
- about 80 % of Pro's doubt marks were right, but only about 30 % of its errors were marked;
- Pro's errors read fluently (a plausible word for the ink), so they cannot be found by reading its text alone;
- Pro kept what the witnesses drop: deletions, insertions, abbreviations, Grothendieck's own forms;
- verdict: Pro is a good blind first pass, not a final text; every package gets the second pass.

**P03 (scans 21–30, about 1,100 words), second pass in full** (`second_pass/LM_P03_changes.md`): 36 changes to Pro's
reading (15 high, 14 medium, 7 low confidence) and 18 places still unresolved; the high-confidence changes alone are
about 1.4 % of the words, as in the pilot. Recurring: *pointé* for *ponctué* (as in P01), whole phrases replaced by a
plausible paraphrase ("Rendons précis" for *Quand on passe à*, "cela revient à" for *cela correspond à*, "comme on
sait" for *comme au n°4*), Grothendieck's sign m̄ (*même*) left as a doubt three times, and one letter read with more
confidence than the ink allows (ρ_s, which may be p_s). Cost: about 0.5 million tokens and 555 tool calls (crops)
for one package; the second-pass prompt now asks for crops only where the readings still disagree.
Prompt v2 got one addition from this (before any v2 package ran): Grothendieck's signs and abbreviations, with m̄
(*même*) spelled out.

P03–P07 were run on 4–5 November (P05–P07 with the zip delivery). Spot check of P05 (scan 41) against the native
image: the reading matches, with doubt marks where the hand is unclear; the research notes follow the requested form.

**Quick check of v1 against v2 (5 November, P01–P019, about 17,400 words; `quick_pass_check.py`,
`quick_pass_filter.py`, output in `quick_pass_20261105/`).** A full second pass costs about half a million tokens per
package, so the prompt versions were first compared mechanically. Each transcription is reduced to plain words
(deletions dropped, the first reading of each `\unsure` kept, mathematics left out) and aligned word by word with the
CSG draft and with Carmona's earlier edition. A *disagreement* is a replacement of one or two words, found against both
witnesses, that is not an abbreviation or a split word. It is not an error count: it misses omissions and formulas,
and it includes the witnesses' own errors and normalisations. Calibration on P03: Pro's text 0.75 disagreements per
100 words, the same pages after the second pass 0.30 (the witness side).

| | words | words inside a doubt mark | disagreements per 100 words | disagreements carrying a doubt mark |
|---|---|---|---|---|
| v1, P01–P10 | 8,556 | 4.0 % | 1.38 | 23 % |
| v2, P011–P019 | 8,821 | 5.2 % | 1.22 | 29 % |

So v2 is no worse than v1, perhaps slightly better: a little fewer disagreements, more doubt marks, and a larger share
of the disagreements marked. Most misreadings still carry no mark, so the second pass stays necessary for every
package. Every v2 zip has both files, ten `\scanpage` markers in order, the four sections of notes and five to fifteen
research notes; the m̄ sign added to v2 now appears (none in v1 after P03, one to six per v2 package). Among the v2
disagreements, besides plausible-word substitutions of the kind v2 already names (*en dessous* / *au dessus*,
*cocartésiens* / *cartésiens*, *maximales* / *invariantes*), two kinds recur: Grothendieck's own spellings given in
their dictionary form (*toposique* for *topossique*, twice in P019; at zoom, scan 183 shows a double s, as both
witnesses read), and word endings that follow the grammar of the sentence (*extérieurs* / *extérieures*, *désignant* /
*désignons*, *noter* / *notons*). These went into v3 as one more item under "Where readings go wrong". Some of these
disagreements may be the witnesses' normalisations rather than Pro's errors: the item asks only to read the ending from
the ink and to mark doubt, so it does not push the reading either way.

**Second pass of the v2 packages P011–P015 (5 November; the checkpoint of step 4).** Same method as for P03:

| | words (plain count) | changes | of which high confidence | high-confidence changes per 100 words | places left unresolved | changes of the mathematics |
|---|---|---|---|---|---|---|
| P03 (v1) | 670 | 36 | 15 | 2.2 | 18 | (not counted) |
| P011–P015 (v2) | 4,926 | 286 | 64 | 1.3 | 200 | 7–10 per package |

Per package: P011 46 changes (12 high), P012 47 (13), P013 63 (9), P014 70 (16), P015 60 (14). With v2 the first pass
makes fewer confident misreadings (1.3 against 2.2 high-confidence changes per 100 words; one v1 package is a thin
baseline) and marks more doubt, so the second pass settles more medium and low places and leaves more open (about 40
per package). Each package still has 7–10 corrections that change the mathematics (a hypothesis restored, Γ read for
T, "épi" for "iso", ≃ read where the first pass left a sign, a cancelled assumption, a sub-module for a sub-algebra),
mostly unmarked in the first pass. Conclusion: v2 is better, not good enough to skip the second pass; every package
keeps it. Cost of the second pass: 0.43–0.46 million tokens per package (P011–P015). Quick-check calibration: the
packages the quick check flagged (e.g. "harmoniciennes", "classes locales") were indeed first-pass misreadings.

## 5. Costs

- First pass: one ChatGPT Pro request per package (about 150 packages for the whole manuscript). Pro requests are
  limited; the editor expects the Pro allowance to change in December 2026.
- Second pass: Claude subagents, about 10 % of the editor's weekly Claude allowance in the week of 3–10 November.

## API route test (6 November)

P057 (scans 561–570) through the OpenAI Responses API instead of ChatGPT: model gpt-6-astra, reasoning effort `max`
(the highest the API accepts; `ultra` is refused), background mode, the same prompt and the same ten package images,
plus one delivery paragraph (the two files as text, since the API cannot return a zip). Script and output:
`api_test_20261106/` (api_run.py; LM_P057/ holds the two files and the raw output).

- Time 24.9 minutes. Tokens: 31,779 input (prompt and images), 54,937 output, of which 42,842 reasoning.
- Cost at list price ($10 input, $50 output per million tokens): $3.06 ($0.32 input, $2.75 output). At that rate the
  remaining packages P058–P160 would cost about $315.
- Quick check against the two witnesses (no agents): 1,009 words; disagreement with CSG 10.5 per 100 words (ChatGPT
  P041–P048: 8.4–14.4, mean about 11); doubt marks 9.2 per 100 words (ChatGPT P036–P048: mean about 19); 133 words
  marked illegible (ChatGPT P041–P048: 11–51). It marks fewer doubts and leaves more words illegible instead of guessing.
- Second pass of this API version running (labelled LM_P057api, so that it does not collide with the ChatGPT P057).
- Second pass of the API version (LM_P057api, 6 November): 61 changes, 19 of them high confidence, 44 places left
  unresolved; 1.9 high-confidence changes per 100 words, against 0.93 (P011–P022), 0.87 (P023–P031) and 0.59
  (P032–P035) for ChatGPT, and 2.1 for ChatGPT's weakest package (P040). Several of its misses are margins it left
  unread (567, 568, 570), consistent with its many illegible marks. One package on hard pages is not a verdict: the
  fair comparison is the ChatGPT P057 on the same pages, second-passed the same way.

## Fix packages and the strict prompt (7-8 November 2026)

- The v2 prompt allowed diagrams and drawings to be described in brackets and put no limit on illegible marks. It was
  replaced by a strict template (complete transcription; every diagram in tikz-cd, every drawing in TikZ; a crop only
  for a picture that cannot be drawn; illegible marks only for physically unreadable ink; a per-page inventory).
- Already returned packages were not redone: 16 targeted fix packages (LM_FIX_01-16) sent only the faulty places
  (described diagrams and drawings, bracketed descriptions, illegible marks inside formulas) with their scans.
  Returned so far: 01, 03-06, 08-16 (02 and 07 outstanding).
- Strict-prompt packages LM_C3-340 to 567 (12 packages, 19 scans each): no images, no described diagrams, no illegible
  mark inside a formula, every scan in the inventory (strict_check.py). Five displays use arrays with vertical
  identifications rather than tikz-cd; that is a correct transcription.
- A bug in apply_fixes.py: when Pro restated a whole line and its wording did not match the transcription exactly,
  the alignment cut text after the corrected place (35 of 330 reading fixes, and some diagram fixes). Found by
  checking that the text after each \illegible mark survived (check_m_items.py) and that every page keeps its braces
  and math delimiters balanced (audit_all_fixed.py). Repaired: 31 reading fixes restored in place; 26 damaged pages
  taken back from the original transcription with their fixes re-applied in a safe form (only the reading replaces
  the mark; exact snippets only), the readings it could not place were then placed by hand from the scope Pro's notes give (18), or kept as illegible where Pro found the ink unreadable (5). Three more pages that had lost a numbered display were restored the same way (lost_equations.py).
- After the repairs, all 66 fixed transcriptions compile (compile_all_fixed.py). The check wrapper now typesets a
  diagram or drawing inside a formula as a box, lets the colour macros span paragraphs, and prints margin notes inside
  boxes in place; tikz-cd inside a macro argument gets the ampersand setting, and a gathered block holding only a
  diagram is removed. The reader build needs the same definitions.

## Intake of the strict packages for cote 140-3, scans 568-681 (8 November 2026)

- Six strict-prompt packages returned: LM_C3-568-586, -587-605, -606-624, -625-643, -644-662, -663-681 (19 scans
  each, 114 in all). strict_check.py on all six: no images; 197 diagrams, all in tikz-cd; 5 figures, all drawn in
  TikZ, none left as a crop candidate; no bracketed descriptions; no illegible mark inside a formula; every scan in
  the inventory.
- Coverage after intake (coverage.py): cote 140-2 complete (575 of 575 scans); cote 140-3 681 of 696 (682-696 open);
  cotes 140-1 (37 scans) and 140-4 (280 scans) not yet returned. Prepared and waiting to be run: LM_C3-682-696,
  LM_C1-001-019, LM_C1-020-037 and fifteen LM_C4 packages (scans 1-280).
- Fix packages 02 and 07 are fully applied: the two diagrams of 02 accepted by hand (apply_accepted_02.py), the seven
  readings of 07 placed from Pro's notes (place_readings_by_hand_3.py).
- Second passes resumed after a usage limit: LM_P041 (completing an interrupted run),
  LM_P042, LM_P043; LM_P045-P056 follow, three at a time.
- Second passes finished 8 Nov 2026 (subagents, archive resolution, witnesses CSG/IUT/Carmona where they cover the
  scans): LM_P041 (scans 401-410; run cut off at the usage limit and completed by a second run that reread every
  scan): 99 table rows (confidence given: 10 high, 52 medium, 22 low), 54 places unresolved. LM_P042 (411-420): 68
  changes (10 high, 39 medium, 19 low), 14 unresolved, 0.47 million tokens, 46 minutes; it corrects several readings
  that change the mathematics (416 "qui n'est pas la composée"; 411 the psi_i inducing M_{g,nu} -> M_{g,nu-1}; 412
  the open subgroups of the arithmetic groups; 414 a stated bijection read as a definition). LM_P043 (421-430): 67
  changes (14 high, 40 medium, 13 low), 22 unresolved, 0.40 million tokens, 32 minutes (421 N_a/N_{a'} for N_0;
  423-426 the order signs > read as inclusions; 430 the upper-margin note cancelled). Open: LM_P045-P056.
- Cost of the second passes (8 Nov 2026, list-price API-equivalent from the subagent transcripts): LM_P042 $18.03 (118 requests, 0.30 million output and 33.6 million cache-read tokens), LM_P043 $14.01 (105 requests, 0.22 million output, 26.3 million cache-read); about $1.40-1.80 per manuscript scan. Prompts: second_pass/PROMPT_LM_Pxxx.md.

## Intake of cote 140-4 and of 140-3 scans 682-696 (8 November 2026)

- Fifteen strict-prompt packages for cote 140-4 (LM_C4-001-019 to -267-280; 280 scans) and LM_C3-682-696 (saved as
  "LM_C3-682-696(1).zip") returned. strict_check.py: no images; 442 diagrams, 436 in tikz-cd, the other six arrays
  (a sign table and aligned correspondences: a correct transcription, as for the five arrays of 140-3); 21 drawings, all
  in TikZ; no bracketed descriptions; three \illegible marks inside struck-out text (\deleted{...}), crossed-out ink,
  allowed by the strict prompt; every scan in the inventory. No fix package needed.
- Coverage (coverage.py): cotes 140-2, 140-3 and 140-4 complete (575 + 696 + 280 scans); cote 140-1 (37 scans, two
  packages) open.
- Pro prompts for La Longue Marche so far (for the cost ledger): 110 transcription packages returned (65 for 140-2,
  30 for 140-3, 15 for 140-4) and 16 fix packages; two (140-1) to go: about 128 in all, plus the pilot re-runs.

## Compile repairs of cote 140-4 for the reader (8 November 2026)

- compile_reader_sources.py compiles, one by one, every text the draft reader uses, after the reader build's own
  mechanical repairs. After the intake of cote 140-4, five of its transcriptions failed (LM_C4-039-057, -058-076,
  -153-171, -191-209, -248-266). They were repaired in four rounds, each a script that changes LaTeX markup only,
  never the reading, and writes the fixed copy in answers/fixed: fix_c4_compile.py (math delimiters for mathematics
  the reader sets in text mode, four packages; an empty node {} in the empty cell an arrow of (106) points to),
  fix_c4_compile_2.py (every \diagram of LM_C4-039-057 and -058-076 holding an array or \left...\right outside
  $...$ put in $...$), fix_c4_compile_3.py ((51) of LM_C4-039-057 in $...$; the same node for (124) of
  LM_C4-058-076) and fix_c4_compile_4.py.
- fix_c4_compile_4.py starts from the two files as they were before it, saved in answers/fixed/backup_20261108 and
  checked by hash. LM_C4-039-057, (81): cell 2-3 of the tikz-cd holds an array{rcl}; the build turns every & of a
  tikz-cd without ampersand replacement into \&, the array's too, which broke the array ("Extra alignment tab has
  been changed to \cr"). The tikz-cd now carries ampersand replacement=\& itself, with \& between its own cells (4
  separators), and the array keeps its 4 &. LM_C4-058-076, (130) and (133): the phantom brace arrow from the cell of
  the number pointed to the empty first cell of the other row ("No shape named tikz@f@...-2-1", resp. -1-1); that
  cell now holds an empty node {}, as in (106) and (124). The script checks that undoing these changes gives back
  the saved text; the diff against the backups shows only them (3 lines and 2 lines): no word, symbol, index,
  \unsure, \deleted, \inserted or \margin changed. Rendered, the array of (81) keeps its two aligned rows and the
  braces of (130) and (133) stand between the two rows.
- Result (compile_reader_sources_20261108f.log): 114 sources, 0 failing. The four reader drafts compile: cote 140-1
  1 page (its 37 scans not yet transcribed), 140-2 210 pages, 140-3 405 pages, 140-4 137 pages.
- 8 Nov 2026, 17:51 local: the two cote 140-1 packages (LM_C1-001-019, LM_C1-020-037; 37 scans) returned. strict_check.py: no images; 70 diagrams, 65 in tikz-cd, the other five arrays; 13 drawings, all in TikZ; no bracketed descriptions; no illegible mark in a formula; every scan in the inventory. The first pass of La Longue Marche is complete: all four cotes (1,588 scans). Pro prompts for the first pass: 112 transcription packages and 16 fix packages.
- Compile check after the 140-1 intake (compile_reader_sources_20261108j.log): 116 sources, 0 failing; reader drafts 140-1 24 pages, 140-2 210, 140-3 405, 140-4 137 (776 pages). The reader preamble (answers/fixed/build/wrap.tex) now loads decorations.pathreplacing (a brace decoration in LM_C1-001-019).

## Raw research outputs (11 November 2026)

The folder [`raw/`](../raw/README.md) holds raw outputs of two further kinds of work, published as returned. This
section says how each was made. Paths are relative to `raw/`.

### Research prompts on *La Longue Marche*

The research prompts on *La Longue Marche* follow Grothendieck's own programme: each takes one of the things he set
out to do, collects his statements and questions on it across the manuscript with their scans, and asks for the
mathematics to be carried through. Claude Fable 5.2 wrote them from its reading of the transcription
([prompts/OVERVIEW.md](../raw/prompts/OVERVIEW.md); index and state of every prompt in
[prompts/README.md](../raw/prompts/README.md)). Each prompt has a part specific to its question (what is to be
settled, leads marked as the author's unverified inferences, Parts) and a shared second half
([prompts/_COMMON_BLOCK.md](../raw/prompts/_COMMON_BLOCK.md)) with the rules of proof and the deliverables: a paper in
LaTeX with its PDF, every statement numbered and labelled Proved, Refuted, Known or Open, a register of the
statements, a report, a bibliography, and every program run with its output. The user pasted each prompt into ChatGPT
with its background zip; the model was GPT-6 Astra in ChatGPT Pro mode. For every prompt,
`prompts/<name>/ATTACHMENTS.md` lists every file of the zip: our own files link to where they are published, and
papers by other authors are listed with their citation and address and are not re-published. Four prompts have been
answered so far.

**`LM1_GROUP_SCHEMES`: the group schemes `M_{ρ,σ}` over `Z` and the schematic envelopes of discrete groups (§§48–50).**

- Prompt: [prompts/LM1_GROUP_SCHEMES/PROMPT.md](../raw/prompts/LM1_GROUP_SCHEMES/PROMPT.md); attached:
  [ATTACHMENTS.md](../raw/prompts/LM1_GROUP_SCHEMES/ATTACHMENTS.md).
- Model and run: GPT-6 Astra (ChatGPT Pro mode), 11 November 2026. The model's workspace disconnected during the final
  assembly, and the model then wrote every file into the chat as text, as the prompt provides. The files in
  `pro_returns/LM1_GROUP_SCHEMES/` are split by a script
  ([tools/lm1_text_copy/lm1_split.py](../raw/tools/lm1_text_copy/lm1_split.py)) from the text copy of the chat saved at
  21:03 UTC, which is beside them (`chat_text_copy_2026-11-11T2103Z.md`; the note it was saved in was overwritten a
  minute later, and the copy was read back from the note application's file-recovery snapshot,
  [tools/lm1_text_copy/recover_obsidian_snapshot.py](../raw/tools/lm1_text_copy/recover_obsidian_snapshot.py)). Each file
  keeps its lines as copied; the chat around the files (status lines and the model's short messages) is left out, and
  the log of the split lists every line left out. Checks of the split: `code/e_additional.out` has exactly the 1,723
  bytes the model reports for it, and the registers have the 97 statement rows and 57 reading rows its build script
  expects. The model kept working after the copy (on A.10 and a citation of Stix); that part is not included. The
  model reports that its original workspace files were lost: several of its Python programs are replaced by
  reconstructions, marked as such in `report.md`, and its two build helpers (`build_reconstruction.py`,
  `integrate_and_build_recovery.py`) are supplied unexecuted.
- Statements by the model's own labels: 97 in `results.csv` (71 Proved, 16 Refuted, 4 Known, 5 Open, 1 Unfinished),
  and C.12, Proved, in `RECOVERY_UPDATE.md` and `sections/C12_addendum.tex`.
- Build: as delivered, the paper does not compile. Its displayed formulas put amsmath's `split` inside `$$...$$`,
  which LaTeX rejects, and the run stops without a PDF. With the 159 displays written as `\[...\]` and the two text
  repairs the model lists (A.2, F.1), it compiles to 46 pages without errors; three citation keys (four citations)
  are missing from the bibliography. The files here are as delivered.
- Review: not yet made. Every statement of this answer is unchecked.

**`LM2_LOOP_EQUATIONS`: the equation of loops in types (0,3) and (1,1); Grothendieck's conditions on the image of
Galois, against the Grothendieck–Teichmüller relations (§§36–47).**

- Prompt: [prompts/LM2_LOOP_EQUATIONS/PROMPT.md](../raw/prompts/LM2_LOOP_EQUATIONS/PROMPT.md); attached:
  [ATTACHMENTS.md](../raw/prompts/LM2_LOOP_EQUATIONS/ATTACHMENTS.md).
- Model and run: GPT-6 Astra (ChatGPT Pro mode); returned 11 November 2026 with the paper and its PDF, the
  registers, the report, and 27 programs with their outputs and build logs.
  79 statements by its own labels: 51 Proved, 12 Known, 10 Refuted, 6 Open.
- Review: Claude Fable 5.2, the author of the prompt, 12 November 2026
  ([reviews/LM2_LOOP_EQUATIONS/REVIEW_author.md](../raw/reviews/LM2_LOOP_EQUATIONS/REVIEW_author.md)). It read the
  register (all 79 rows), the report, the new conditions, the proofs of B.g1, B.g2, B.g4, B.g5, B.g11, E.1 to E.4,
  B.f5, B.f7, B.f8, C.d5, D.6 and D.7, and the other sections in the register only; it ran none of the return's
  programs. Its own programs (`checks_author/check_lm2.py`, exact arithmetic, and `checks_author/check_psl27.py`)
  recompute B.g2 to B.g5 through weight 9 (the pentagon coefficient 16 of the element of weight 7 included), C.r1, C.r2,
  C.a3, D.5 and the 57 classes of generating pairs of `PSL_2(F_7)` (B.f5). Each of the 79 statements has a verdict,
  many of them "not followed" (statement read, proof not read). No statement labelled Proved, Known or Refuted was
  found false among those it checked; C.d1, on which the congruence results rest, was not followed. The return
  corrects the LM3 review: the solution space of the two linear cycle equations first exceeds that of `grt_1` in
  weight 4, not in weight 7 (B.g4), and the review says so. The review adds results of its own, checked by no one
  else: for every ℓ ≥ 5, an element with leading term `q_7` in the pro-ℓ centralizer of `𝔖_3`, outside the pro-ℓ
  `GT` (the pro-ℓ half of B.g11 and F.3), and reductions of E.3, D.6, C.d5 and B.f7. The readings register was not
  reviewed row by row.
- Path forward: sections "After LM2" in the prompts `LM4` to `LM8`, which will be published with their answers.

**`LM3_TEICHMULLER_TOWER`: the Teichmüller tower, its profinite forms and the "conjecture fondamentale" (§§19, 21,
26–30, 32–36).**

- Prompt: [prompts/LM3_TEICHMULLER_TOWER/PROMPT.md](../raw/prompts/LM3_TEICHMULLER_TOWER/PROMPT.md); attached:
  [ATTACHMENTS.md](../raw/prompts/LM3_TEICHMULLER_TOWER/ATTACHMENTS.md); notes and the record of the sections added
  after answers to the prompts on *Les Dérivateurs* came back (`work/CHANGES_20261110.md`, `work/BACKGROUND_ADD.md`).
- Model and run: GPT-6 Astra (ChatGPT Pro mode); returned 11 November 2026; the return records no run time.
  110 statements by its own labels: 57 Proved, 30 Known, 11 Refuted, 12 Open.
- Review: Claude Fable 5.2, the author of the prompt
  ([reviews/LM3_TEICHMULLER_TOWER/REVIEW_author.md](../raw/reviews/LM3_TEICHMULLER_TOWER/REVIEW_author.md)). It read
  the register (all 110 rows), the readings of the manuscript (42 rows), the report and Parts B to F with their proofs
  (Part A in statement only); it opened Hoshi–Mochizuki, Hoshi–Minamide–Mochizuki, Harbater–Schneps, a Lean
  comparator attached to the prompt and the transcription at scan 483, and lists the sources it did not open; its own
  program (`checks_author/check_lm3.py`, exact arithmetic) checks B.4, B.5, D.2, D.20, E.20 and F.11 and two pro-ℓ
  results of the review itself. Each statement has a verdict (proved; proved in outline; known, checked; known, not
  opened; open). No statement labelled Proved, Known or Refuted was found false; two labels claim less than they seem
  to (D.2, E.27).
- Path forward: the second prompt on the tower, `LM3b_TEICHMULLER_PUSH`, takes the rows the answer left open and the
  statements that rest on theorems the answer only cited, with the answer, the review and the reviewer's programs
  attached.

**`LM3b_TEICHMULLER_PUSH`: the Teichmüller tower, second run.**

- Prompt: [prompts/LM3b_TEICHMULLER_PUSH/PROMPT.md](../raw/prompts/LM3b_TEICHMULLER_PUSH/PROMPT.md); attached:
  [ATTACHMENTS.md](../raw/prompts/LM3b_TEICHMULLER_PUSH/ATTACHMENTS.md). It was written to a stricter standard for
  what a prompt must demand (proofs and attacks on the open items, a stated outcome for every item); the standard and
  the record of the rewrite of the later prompts are in `prompts/work/`, and the scripts in `tools/prompts/`.
- Model and run: GPT-6 Astra (ChatGPT Pro mode); returned 11 November 2026; the return records no run time.
  93 statements: 53 Proved, 11 Refuted, 15 Known, 14 Open.
- Review: not yet made. Every statement of this answer is unchecked.

The other Longue Marche prompts (`LM4` to `LM8`) have not been answered yet; they will be
published with their answers. Inserts for them that came out of the review of the prompts on *Les Dérivateurs* are
published in the repository `grothendieck-derivateurs`, in `raw/reviews/7_BISITE/FOLLOW_UPS.md`.

### First-pass transcriptions of the manuscripts around *La Longue Marche*

The Montpellier archive (<https://grothendieck.umontpellier.fr>) groups cotes 146, 147 and 149 with *La Longue
Marche*. Their scans are being transcribed in packages of up to 90 scans, by the same two-pass method as the
manuscript itself (sections 2 and 3 above). The scripts in [tools/archive/](../raw/tools/archive/) download the
archive's scans, enhance the page images and build each package: a prompt filled from the template
[tools/archive/ARCHIVE_PROMPT_TEMPLATE.md](../raw/tools/archive/ARCHIVE_PROMPT_TEMPLATE.md) (its three earlier versions
are beside it, with the message used when a run's execution environment disconnects), a zip of the page images, and a
zip of context: the transcription of *La Longue Marche* and the first passes of the earlier packages. The prompt asks
for a diplomatic transcription into LaTeX, page by page, with every doubt marked, an inventory of every element of
every page, a list of doubts, and research notes on what the pages contain. For each package,
`prompts/<name>/ATTACHMENTS.md` lists every page image with its place in the archive's own scan file, and
`prompts/<name>/work/MANIFEST.json` records how each page was enhanced and which blank scans were skipped.

The model was GPT-6 Astra (ChatGPT Pro mode). Each return keeps a `progress.log` with the time of every page; the run
times below are read from it.

| Package | Run (11 Nov 2026, UTC) | Checked |
|---|---|---|
| `MPL_147_003-047` | 00:29–02:06; the 45 pages took 59 minutes in one stream, the notes the rest | sample check of eight pages |
| `MPL_147_048-137` | 09:14–10:56; the 90 pages took 45 minutes in four parallel streams. The context zip the model received was empty (its log records 0 entries), so its notes make no comparison with earlier material | sample check of eight pages |
| `MPL_147_138-190` | 14:19–15:30 | not yet |
| `MPL_149_091-136` | from 15:44; the last time logged is 17:11 | not yet |
| `MPL_146_001-099` | 16:12–17:15 | not yet |
| `MPL_146_100-134` | 21:56–23:02; the transcription was frozen at 22:33, before the context zip was opened | not yet |

The sample checks are by Claude Opus 5.5 ([reviews/MPL_147_003-047/SAMPLE_CHECK.md](../raw/reviews/MPL_147_003-047/SAMPLE_CHECK.md),
[reviews/MPL_147_048-137/SAMPLE_CHECK.md](../raw/reviews/MPL_147_048-137/SAMPLE_CHECK.md)). Each compared eight pages
with the scans, word by word and sign by sign, counted the errors per 100 words (all errors, misread words and
symbols, errors without a doubt mark) and the minutes per page, and wrote the eight pages corrected (`pages_checked/`).
The first had 0.73 errors per 100 words, 0.27 of them without a doubt mark; the second 2.15 and 1.52, ten of its 24
errors being one notation decision repeated on one scan. Their recommendations set the size of the later packages
(90 scans) and added a rule to the template: parallel streams first write one shared table of notation. The second pass of these packages, against the scans, has not been made yet.

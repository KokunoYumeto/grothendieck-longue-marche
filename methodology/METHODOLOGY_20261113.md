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

**Who does what.** The user runs the packages by hand in ChatGPT Pro (the Pro mode of the user's ChatGPT
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
- **research notes** (added 4 November at the user's request), kept apart from the transcription: Grothendieck's
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
  limited; the user expects the Pro allowance to change in December 2026.
- Second pass: Claude subagents, about 10 % of the user's weekly Claude allowance in the week of 3–10 November.

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
- Second passes resumed after the usage limit on the first account: LM_P041 (completing an interrupted run),
  LM_P042, LM_P043; LM_P045-P056 follow, three at a time.
- Second passes finished 8 Nov 2026 (subagents, archive resolution, witnesses CSG/IUT/Carmona where they cover the
  scans): LM_P041 (scans 401-410; run cut off at the usage limit and completed by a second run that reread every
  scan): 99 table rows (confidence given: 10 high, 52 medium, 22 low), 54 places unresolved. LM_P042 (411-420): 68
  changes (10 high, 39 medium, 19 low), 14 unresolved, 0.47 million tokens, 46 minutes; it corrects several readings
  that change the mathematics (416 "qui n'est pas la composée"; 411 the psi_i inducing M_{g,nu} -> M_{g,nu-1}; 412
  the open subgroups of the arithmetic groups; 414 a stated bijection read as a definition). LM_P043 (421-430): 67
  changes (14 high, 40 medium, 13 low), 22 unresolved, 0.40 million tokens, 32 minutes (421 N_a/N_{a'} for N_0;
  423-426 the order signs > read as inclusions; 430 the upper-margin note cancelled). Open: LM_P045-P056.
- Cost of the second passes (8 Nov 2026, list-price API-equivalent from the subagent transcripts; ledger C:\Users\user\Documents\compute_cost_ledger): LM_P042 $18.03 (118 requests, 0.30 million output and 33.6 million cache-read tokens), LM_P043 $14.01 (105 requests, 0.22 million output, 26.3 million cache-read); about $1.40-1.80 per manuscript scan. Prompts: second_pass/PROMPT_LM_Pxxx.md.

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

## Model provenance, 10-11 November 2026

- Second passes C3 and C4 (per package): Claude Opus 5.5 subagents (session default effort), against the archive images.
- Provisional development prompts pro_prompts_draft_20261111 (OVERVIEW.md, LM_P161-LM_P168, README.md): Claude Fable 5.2 (Anthropic), subagent, high effort; also edits to Derivateurs prompts 4_GALOIS and 5_STRATA for the overlap.
- Source-of-record audit of the Longue Marche (SOURCE_OF_RECORD_AUDIT_20261110/sections/longue_marche.md): a subagent of the Fable 5.2 audit.

## Research prompts: how a Pro run is kept on a problem for ten hours (13 November 2026)

The mathematics prompts (LM1-LM8 and their pushes, the Dérivateurs prompts) go to GPT-6 Astra in ChatGPT Pro mode: one
PROMPT.md and one background ZIP per run. On 13 November four of them ran overnight. All figures below are the runs'
own claims; refereeing was in progress when this was written.

| Run | Sent (UTC) | Last state seen | Statements (proved / refuted / known / open) |
|---|---|---|---|
| LM4_FINITE_GROUP_ACTIONS | 02:32 | still working at 12:06, 9.5 h in; 300-page paper | 195 (164 / 25 / 3 / 3) |
| LM7_PUSH | 04:36 | still working after its checkpoint 04 at 10:51 | 137 (123 / 7 / 3 / 4) |
| LM8_LIE_APPROXIMATIONS | 02:01 | checkpoint 16 at 07:10, then silent; delivery timed out | 167 (122 / 24 / 15 / 6) |
| TOTAL_EXACT_2 | about 01:05 | complete, every item settled, about 4.5 h | 89 (74 / 13 / 2 / 0) |

LM4 had isolated its last three open items by its first checkpoint (160 statements). It spent the following hours
attacking them and added 35 proved statements around them, without settling any of the three. It saved its ZIP to the
ChatGPT Library about nine times. TOTAL_EXACT_2 is a second round. The first round (TOTAL_EXACT, 12 November) came back
after 50 minutes with its main question open, because its prompt counted "partly settled" as an outcome. The second
round, with that clause removed, settled the main question by an explicit construction.

What in the prompt produces this (template: claude_tools/prompt_lessons_20261112/PROMPT_TEMPLATE_PUSH.md; standard and
audit: pro_prompts_draft_20261111_work/PUSH_STANDARD_AND_AUDIT_20261111.md):
1. **Every part asks for mathematics**: "prove or refute", "decide", "construct, or show what obstructs". Never "give
   the status" or "cite or prove". In the audit of 11 November, status-shaped parts came back 27 % Known and 11 % Open;
   push-shaped parts came back 12-17 % Known.
2. **Only proved or refuted finishes an item.** The outcome section:
   - the main question first, with most of the time;
   - when one approach stalls, the next one;
   - no delivery while an item is undecided and an untried approach remains;
   - a gap in a proof is an undecided step, attacked, never papered over.
3. **No way out.** None of these appear:
   - a "partly settled" outcome;
   - "if the general case fails, do special cases";
   - "as far as you can", "where possible", "if time permits";
   - "report what is unfinished" as a way to finish;
   - a plan or a sample in place of the work;
   - minimums ("at least N");
   - a cheaper alternative deliverable.

   A model told the least acceptable amount delivers exactly that. On 12 November a prompt asking for "at least three"
   examples got exactly three, and one offered a reduction as an alternative delivered the reduction.
4. **INCOMPLETE only when the environment ends the session.** The return then gives the state reached, every approach
   tried and where it failed, and the next step.
5. **Time**: "Take the time the work needs." An earlier "Ignore any clock." coincided with a safety block and was
   replaced.
6. **Checkpoints**: after every finished Part, a ZIP saved to the Library under a new name, never overwritten. A lost
   workspace or a failed delivery then costs only the work since the last checkpoint: LM8's checkpoint 16 is its return.
7. **Deliverables that can be checked**:
   - a numbered register of results (id, statement, status, where proved, depends on);
   - the paper in LaTeX;
   - the programs and their outputs;
   - the run's own independent audits;
   - a typesetting check (overfull boxes from the log, rendered pages inspected).
8. **Background in LaTeX**: arXiv e-prints, our transcriptions and the earlier returns go in as source, never as PDF
   where source exists. The background also carries the earlier referee reports and the items they left open.
9. **A lint before sending**: claude_tools/push_rule_pro_prompts.py --lint-math rejects escape clauses, minimums and
   cheaper alternatives.

After the run, a Claude Fable 5.2 intake (effort high) gives verdicts and implications. The field expert of the subject
(Claude Fable 5.2, effort max) turns them into the next prompt, and the items still open go into a push prompt.

Practical limits:
- A run holds one of the account's slots for its whole length. Two long runs per account at once has held; three led to
  lost workspaces on 11-12 November.
- A run that dies can go silent for hours before the interface says so (LM8: about four hours).
- Each checkpoint rebuilds and page-checks the whole paper. LM4 did this about eleven times as it grew from 83 to 300
  pages. Checkpoints that carry only sources, with one build at the end, are under consideration.


## Appendix: the LM4 prompt as sent, 13 November 2026, 02:32 UTC

This prompt kept GPT-6 Astra (ChatGPT Pro mode) working on finite group actions on surfaces for more than nine hours
(table above). It went out before the checkpoint paragraph existed. Its deliverable is a ZIP, and its item 5 (the
disconnect clause) says the work must reach us even if the workspace is lost. The run saved its ZIP to the ChatGPT
Library about nine times on its own, each time with the paper, the register, the programs and the audits so far.

Since 13 November every mathematics prompt also carries this paragraph (here with LM4's file name):

`````markdown
**Checkpoints.** Save a checkpoint ZIP to the Library after every finished Part, each under a new name, `LM4_FINITE_GROUP_ACTIONS_checkpoint_<NN>.zip` with `NN` counting up; never overwrite, rename or delete an earlier checkpoint. If the workspace comes back empty, restore it from the newest checkpoint and from this conversation before you continue. The final ZIP holds everything the checkpoints held: a file or passage left out of the final is listed in the report with the reason (superseded by which file, or wrong).
`````

Each checkpoint ZIP lands in the ChatGPT Library of the account. The Library keeps it when the chat itself times out or
loses its workspace, so whatever the run was working on and saving can still be downloaded. LM8's last checkpoint was
downloaded there about four hours after its run had gone silent.

The prompt as sent (its background ZIP carried the transcription of the relevant manuscript pages in LaTeX, the earlier
returns and referee reports, and the cited arXiv sources as LaTeX):

`````markdown
# LM4_FINITE_GROUP_ACTIONS: finite groups acting on surfaces and on groups with loops (§§12–18, 23–25 bis, 31)

DRAFT, provisional (12 November 2026). Development prompt for Grothendieck, *La Longue Marche à travers la théorie de Galois* (1981). File prefix for your deliverables: `LM4_FINITE_GROUP_ACTIONS`.

## What is to be settled

In §12 Grothendieck convinces himself that, in the anabelian cases, the whole system of groupoids attached to a curve with marked points can be expressed by an *exterior group with loops* ("groupe extérieur à lacets"): the fundamental group `π` with the conjugacy classes of its loop subgroups `L_i`. From there to §31 he studies a finite group `Γ` acting on a surface, or acting exteriorly on `π`, discrete or profinite, with two operations: filling holes ("bouchage") and drilling holes ("forage de trous"). His aim is stated at 140-2 scans 270–271, of the 2-functor from topological `Γ`-actions on surfaces to the group-theoretic data: "Je conjecture que c'est une équivalence de 2-cat, i.e. qu'il est 3 fidèle" ("de 2-cat" is inserted above the line; its "de" and the "3" are doubtful readings). He defines the levels 0- to 3-fidélité on scans 271–273 and 279–280, and scan 293 has "2-fidèle (pas néc. 3-fidèle)". What he asks, in his order:

1. Rigidity of the loop structure. He states it in §§7–13 bis for the profinite groups of the arithmetic setting (`Γ = Gal(K̄/K)`, `π` profinite, `E → Γ` with kernel `π`): the Hom-categories are discrete (scan 53); `α ∈ Γ` is "probablement uniquement déterminé", and the `α_{i'}` are determined modulo the normalizers of the `E_i` ("du moins des transporteurs", scan 54; "probablement" and "des normalisateurs|du normalisateur" are doubtful readings); is `Trans_E(L_i^d, L_i)` reduced to `E_i` for every `d ∈ N*` (scan 69, a question); `α^{-1}g ∈ E_i`, "probablement" (scan 84); the centre of `π` is trivial except for the annulus (scan 98; the torus is omitted there, see Part A); and on scan 118, "deux pts à vérifier": `Norm_π(L_i) = Centr_π(L_i) = L_i` "dans le cas ν=1, sinon pas de pb", `Centr(π) = (1)` in the anabelian case, and "plus généralement, le centralisateur de tt ss-groupe ouvert de π est réduit à 1", with the margin "Ce n'est démontré pour le moment dans aucun cas anabélien profini !". The trivial centralizers of scans 54 and 62 ("Le centralisateur dans Γ d'un ss-groupe ouvert est réduit à l'unité"; `Cent(Γ) = {1}`) are said of the Galois group `Γ`, not of `π`, and are not asked here; on scan 62 the second pass reads "sans doute" as struck.
2. §§15, 17–18: critical orbits of splittings; fixed points against classes of sections, "Cette application est-elle bijective ??" (scan 139), and the theorem of scans 148–149 for a finite group acting faithfully on `U` with `Ũ` not compact: a) "Cette application est bijective", b) `π^{Γ'} = (1)` for every section subgroup `Γ'`, c) `Γ` cyclic or dihedral when a splitting exists; the "lemme fondamental" of §18 (scan 193: a direct outer automorphism of finite order of a group with loops that fixes a class of loops `i`, and for which the extension of `Z/nZ` by `L_i` that it defines is trivial, is trivial; corollary on scan 194) and its expected validity in the two abelian cases `(g, ν) = (0, 2)` and `(1, 0)` (scan 194: "Pourtant le résultat doit être valable aussi dans ces cas"; the "lemme fondamental" of §15, scans 141–148, on a finite group acting on `D ≃ R²`, is a different statement, from which he derives the theorem of scans 148–149); the theorem marked "Ultra fort!" (scan 198: for a finite subgroup `Γ_0 ≠ 1` of `Aut_lac(π)^0` the normalizer equals the centralizer; "Si g=0" in the margin, doubtful) and the lemma he marks "faux !" (scan 200), in a passage of scans 198–200 that a thin oblique stroke of unsettled scope may cancel (second pass; the first pass had plain text); "Ça doit être le seul contre-exemple" (scan 179); his note that the abelian case is "pas tout à fait démontré", for want of the topological classification of finite group actions on `C*` and on `S¹ × S¹` (scan 181).
3. The invariant `μ` on elements of finite order (scans 155–160): "J'ignore si cette application μ peut se définir intrinsèquement"; the torus case, his first non-trivial case ("le cas abélien (où π≃Z (card I=2) ou π≃Z² (I=∅))", scan 157), where he classifies the extensions by `H²(Γ, π) ≅ H¹(Γ, X_0(π))`, torsors under the torus `X_0(π)`.
4. Questions c), d), e) of scans 197–198: is `π^Γ = 1` for finite `Γ ⊂ Aut_lac(π)`; a unique maximal section subgroup (his proof, scans 201–203); finitely many classes of lifts. He reduces c) and e) to realizability of cyclic outer actions.
5. Essential surjectivity, "un problème ouvert sur lequel les gens sèchent" (scans 101–102), and the realizability criterion of scan 294: a faithful outer action is realizable if and only if, after drilling holes, it lifts to an admissible action whose extension is a group with loops; the bijection (∗) of scans 289–290; `Π_1^Γ = 1` (288), `H^1(Γ, B^0) = 1` (285); the theorem of scan 304, `π_0(SA_{g,ν}) ≅ SΓ^{!+}` with `(SA_{g,ν})^0` ∞-connected; "Le plus agréable serait que ce soit un homotopisme" (281; "homotopisme" is a doubtful reading); the programme of scans 292–293 (points I–III), to be carried out first "pour les groupes cycliques (opérant de façon directe), et procéder dans ce cas par dévissage" (second pass; the first pass read "de ce cas"), so that the dévissage is inside the cyclic case, with his reduction of scan 195 to cyclic groups of prime order ("sauf erreur ce résultat est bien connu (m̄ pour les groupes résolubles ...)").
6. "J'ai l'impression que ça ne doit pas être très vache à prouver — ce serait comme si on savait déjà que tte extension "sans torsion" d'un groupe fini par un groupe à lacets est (de la façon canonique) un groupe à lacets" (scan 353; second pass "comme", first pass "connu"; "sans torsion" is inserted, "tte" doubtful); and the relèvements of §31 (scans 391–394): for the canonical map from the classes of lifts of `G` into the discrete extension `E` to those into its profinite completion `Ê`, his questions a) "la bijectivité de cette appl." and b) "si π^G=1 (rigidité), pour G≠(1)", followed by "J'ai envie de conjecturer sans vergogne qu'il en est ainsi" (scan 393).
7. §25 and §25 bis: the special Teichmüller groups and the case of two groups of operators.

## Leads (unverified; prove or refute each)

- **Lead 1.** Essential surjectivity in the discrete case is the Nielsen realization problem, solved by Kerckhoff (1983); contractibility of the identity components is Earle–Eells and Hamstrom. What Grothendieck states beyond this, and what does not seem to be in the literature as a statement, is the 2-categorical form: an equivalence between the 2-category of surfaces with `Γ`-action (isotopies as 2-arrows) and a 2-category of exterior groups with loops with `Γ`-action.
- **Lead 2.** His "forage" criterion is a form of the Birman–Hilden correspondence together with the theory of Fuchsian and NEC groups; the torsion-free extension statement in the discrete case is the classical theorem that a torsion-free finite extension of a surface group is a surface group (Zieschang; Eckmann–Müller for the closed case), and with loops kept, its relative form.
- **Lead 3.** The profinite counterparts (triviality of centralizers of open subgroups; normalizers of the `L_i`; finite subgroups of the profinite completion and their conjugacy to discrete ones; the profinite realization statement) are partly theorems (Nakamura; Anderson; Bridson–Conder–Reid and others for Fuchsian groups) and partly open; the profinite torsion-free extension statement is, as far as I know, open in general.

## After the first Dérivateurs return (added 11 November 2026)

Package CATHOT of the companion work on *Les Dérivateurs* has been answered (GPT-6 Astra, ChatGPT Pro mode). The statements below are from that answer; those marked *checked* were followed step by step by the author of this prompt. The named sections of that answer are attached.

- **What the group-theoretic side of the 2-functor can see** (CATHOT C.1–C.4, B.11; *checked*). Categories and functors modulo zigzags of natural transformations represent homotopy classes of maps into 1-types and nothing more, and the reflection onto them is the fundamental groupoid. Surfaces of the anabelian types are 1-types, which is why his passage from surfaces to exterior groups with loops loses nothing at the level of objects and arrows; the 2-arrows (isotopies) are where a statement beyond this is needed. In Part C, say exactly which level of the mapping spaces of the homeomorphism groups each of his fidelity conditions concerns ("3-fidèle" in his usage), and where the excluded types `(0,0)`, `(0,1)`, `(0,2)`, `(1,0)` fail because the surface, or the identity component of its homeomorphism group, is not a 1-type or not contractible.

### After GALOIS (added 11 November 2026)

Package GALOIS of the companion work on *Les Dérivateurs* (locally constant coefficients) has been answered (GPT-6 Astra, ChatGPT Pro mode). Its statements are cited by their numbers; the author of this prompt has read them in statement only, and the review is not finished: verify what you use. The named section is to be attached under `GALOIS_return/`.

- **A ladder of levels to state the fidelity conditions against (Part C).** GALOIS C.4–C.5: for a map of spaces `v` and coefficients in `r`-truncated spaces (`r = 0`: sets; `r = 1`: groupoids), restriction of locally constant coefficients along `v` is (i) bijective on morphisms between constant coefficients iff `v` is an isomorphism on `π_i` for `i ≤ r`; (ii) fully faithful iff moreover `π_{r+1}(v)` is onto at every base point; (iii) an equivalence iff `π_{r+1}(v)` is an isomorphism. All three inclusions are strict, and the middle class fails two-out-of-three (`* → K(A, r+1) → *`). So "faithful", "fully faithful" and "equivalence" at the level of locally constant `r`-types are three different conditions on `π_{≤ r+1}`. When you say which level of the mapping spaces each of his conditions concerns ("3-fidèle" in his usage), place it on this ladder for `r = 0, 1, 2`, or say why it is not of this form.
- Nothing in the leads of this prompt is refuted or settled by GALOIS.

### After STRATA (added 11 November 2026)

Package STRATA of the companion work on *Les Dérivateurs* (small categories as stratified spaces; the moduli spaces `M̄_{0,n}` stratified by dual trees) has been answered (GPT-6 Astra, ChatGPT Pro mode). Its statements are cited by their numbers; a review of it was made at reduced effort; it does not count as a check and is not attached, and no review of STRATA at full effort exists. Every statement of STRATA cited here is a claim of the return, to be checked in the attached sections before you build on it. The named sections are to be attached under `STRATA_return/`.

- **A group with loops as a category (Parts A and C).** STRATA B.1: a category in which every endomorphism is invertible is the same thing as a category with a conservative functor to a poset; its data are the automorphism groups of the objects and, for non-isomorphic objects, the Hom-sets with the two actions and the composition. F.1–F.2 (with Jansen, arXiv:2308.09551, for the identification with exit paths): for the sphere with three marked points, stratified by the points and their complement, the exit-path category has one object `u` with `Aut(u) = π`, the fundamental group of the complement, three objects `p_i` with trivial automorphism group, and `Hom(p_i, u) = π/L_i`, `L_i` the loop subgroup at the `i`-th point, with `π` acting on the left; this is an ordinary category because the `L_i → π` are injective (F.3: without that the mapping spaces are not discrete). The same description holds for the strict fibres of the forgetful functors (F.13: a stable curve stratified by its marked points and nodes). An inference of the author of this prompt, unverified: for a surface of anabelian type with marked points, the exterior group with loops `(π; (L_i))` of §12 and this category determine each other, natural isomorphisms of functors between such categories being the inner automorphisms; and for a finite group `Γ` acting, the exit-path category of the quotient orbifold stratified by isotropy has the extension `E` at the generic object, the stabilizers at the special points, and the cosets `E/E_i` as bimodules, with `E_i = Norm_E(L_i)` (item 1). If this holds, the 2-category of exterior groups with loops with `Γ`-action of Part C is a full sub-2-category of categories over `BΓ` with functors and natural isomorphisms, and "3-fidèle" becomes a statement about functors between such categories. Prove it, correct it, or say why his 2-category is not of this form; the excluded types are where the `L_i` are not injective or the centre is not trivial.
- **His groups, as read there (Part E, Part F).** STRATA F.16, from §19, folio 102, scans 204–205, equations (3)–(11): `A_{g,ν}` preserves the set of marked points, `A^!_{g,ν}` fixes each, `Γ_{g,ν} = π_0(A_{g,ν})`, `Γ^!_{g,ν} = π_0(A^!_{g,ν})`, orientation not imposed by the symbols. F.9: filling a puncture gives the Birman sequence `1 → π_1 → Γ_{n+1} → Γ_n → 1` on the pure oriented groups, strictly functorial on fixed surfaces, while relabelling the points is functorial only up to specified natural isomorphisms (no splitting over the symmetric group is chosen). Part F's lemmas for LM3_TEICHMULLER_TOWER should name the group (with or without permutations, with or without orientation reversal) in each statement, in these symbols.
- Nothing in the leads of this prompt is refuted or settled by STRATA.

### After PATHS (added 11 November 2026)

Package PATHS of the companion work on *Les Dérivateurs* (path categories and mapping spaces; when strict diagrams in a category with weak equivalences represent the homotopy-coherent ones) has been answered (GPT-6 Astra, ChatGPT Pro mode; 76 statements: 40 Proved, 19 Refuted, 11 Known, 6 Open). Its statements are cited by their numbers; a review of it was made at reduced effort; it does not count as a check and is not attached. Every statement of PATHS cited here is a claim of the return, to be checked in the attached section before you build on it. The named section is to be attached under `PATHS_return/`.

- **Realization as a question of strict against coherent actions (Part C; items 5 and 6).** PATHS D.1, D.4: for a category `M` with weak equivalences `W` and a small category `A`, there is a comparison from strict diagrams `A → M`, modulo pointwise weak equivalences, to `A`-diagrams in the ∞-categorical localization; `(M, W)` is *rectifiable at `A`* when it is an equivalence. D.11: finite simplicial sets are rectifiable at every finite partially ordered set and not at the one-object category of `Z`: a strict action of `Z` on a finite simplicial set is by an automorphism of finite order, while a self-equivalence of a wedge of two circles acting on `H_1` by a unipotent matrix of infinite order gives a coherent action that no strict one represents. D.13: a partially ordered set whose localization is the classifying space of `C_2`, in which every strict `C_2`-diagram is constant, so that the identity of `C_2` is missed. An inference of the author of this prompt, unverified, to prove, correct or discard: his essential-surjectivity problem (scans 101–102) has three layers that these examples keep apart, with `A` the one-object category of `Γ`. (i) From an outer action `Γ → Out(π)` to a coherent action of `Γ` on the homotopy type of the surface: for a centre-free `π` the classifying space of self-equivalences of a `K(π, 1)` is that of `Out(π)`, so there is no obstruction and no choice, for every group `Γ`; with a centre an obstruction in `H³(Γ; Z(π))` appears, which is one place where the excluded types differ. (ii) From a coherent action to a strict action on some space of that homotopy type: always possible (rectification of homotopy actions; resolve the reference by title). (iii) From there to a strict action on the surface itself, by homeomorphisms preserving the marked points: this is the step that depends on the class of models and on `Γ`, as in D.11; for finite `Γ` it is Kerckhoff's theorem (Lead 1), and for infinite `Γ` it can fail (for the whole mapping class group there are non-realization theorems of Morita and of Markovic, cited from memory: resolve them by title and state them with their hypotheses). In Part C say to which layer each of his statements belongs (the theorem of scan 304, the statement of scan 281, the criterion of scan 294, the bijection (∗)), and which of them survive for infinite or profinite `Γ`.
- Nothing in the leads of this prompt is refuted or settled by PATHS.

## After the returns LM2, LM3 and LM3b and the literature step (added 12 November 2026)

Three packages on *La Longue Marche* have been answered since this prompt was drafted, all by GPT-6 Astra (effort Pro, ChatGPT Pro mode) on 11 November 2026: LM2_LOOP_EQUATIONS, LM3_TEICHMULLER_TOWER and LM3b_TEICHMULLER_PUSH (attached under `LM2_return/`, `LM3_return/`, `LM3b_return/`; statements cited by their numbers, with the status the return gives them). LM3 and LM3b have since been reviewed statement by statement by Claude Opus 5.5 (effort max) on 12 November 2026 (attached as `LM3_review/REVIEW.md` and `LM3b_review/REVIEW.md`): no statement of either was found wrong; LM3 has three with gaps (B.10, C.12, C.13) and LM3b two (G.8, G.9, which nothing here uses); LM3b C.10 depends on the pro-2 descent of C.3. LM2 is not yet reviewed. The reviews are not authority either. Each cited statement is a claim: check its proof in the attached return before you build on it, correct it where it fails, and then go beyond it. A row that only repeats one of them is unfinished. The literature read for this prompt on 12 November (by Claude Fable 5.2, effort max) is named, with theorem numbers, at the head of the Parts; the notes are attached under `LM_EXPERT_notes/` (`FINDINGS.md`, section E and F15–F27; `LIT_LM4_surfaces.md`; `LIT_LM6_anabelian.md`), the texts under `literature/`. Results of 2025–2026 are unrefereed unless said.

- **Profinite groups with loops (Part A (c)).** LM3 D.14 (Known there): non-abelian free profinite groups and profinite surface groups are torsion-free with trivial centralizers of open subgroups. LM3 D.15 (Proved there): an automorphism fixing an open subgroup pointwise is the identity, and the centralizer of a non-zero power of a generator of a base is its procyclic closure. That is his Lemme 5 and his (2), (4) of scans 500–501, the closed case `ν = 0` included. Checked (LM3 review): D.15 holds, `ν = 0` included. (4) for `ν = 0` is Boggi–Zalesskii 2019, Prop. 3.6, and also Mochizuki 2007, Prop. 1.2 (ii), applied to the one-node degeneration pinching `x_i` (edge-like subgroups are commensurably terminal); Lemme 5 needs only the trivial centralizers of open subgroups. Part A (c) starts from D.15; its weight moves to the abstract axioms and to the `m`-step solvable quotients.
- **Discretizations along coverings (Part D (c), Part F (a)).** LM3 B.8 (Proved there, checked): a discrete non-abelian free or closed surface lattice is its own normalizer in its profinite completion. B.9 (checked): restriction of discretizations to an open subgroup is injective. B.10: for a normal finite cover a lattice upstairs extends, uniquely, if and only if the deck group acts on it through discrete automorphisms preserving orientation and loops; checked, with one step to be written out: the closure of each maximal parabolic subgroup of the extension is a full inertia group of `π` (LM3 proves only the inclusion; equality follows by comparing the stabilizers in `G` of the cusps of `Λ` and of the inertia classes of `V`). B.11 (Refuted there, checked): surjectivity fails for the covering of degree 2 of the sphere with three holes, as his own NB of scans 353–354 says. An explicit `γ`: conjugation by `T_a^α`, `α ∈ Ẑ ∖ Z`, for a curve `a` moved by the deck involution `s`; then `u⁻¹su = s·T_{s(a)}^{−α}T_a^{α}` has abelian image `(α, −α) ∉ Z²` and is not discrete (LM3 review, §4.2). LM3b C.1: the subgroup of index 2 used there is normal but not characteristic for loop-preserving automorphisms; the kernel `V_4` of reduction modulo 2 of the abelianization (type `(0,6)`) is characteristic. C.2: the automorphisms stabilizing an open normal `V` are the automorphisms of `V` whose class normalizes the deck group. C.5 (Refuted there, pro-2): for the index-2 cover, `Out_lac(V₂^(2)) ≠ N(D)·Σ(V₂^(2))`, by an explicit special automorphism (the A.1 lift of the degree-3 derivation with conjugators `[[x,y],y]`, `[x,[x,y]]`, `1`) and 64 dual certificates in `F₂⟨X,Y,Z⟩/(deg ≥ 5)`, recomputed independently in the LM3b review. C.10 (Refuted there, pro-2): the same for the characteristic cover `V₄`, by transfer from C.5 through C.2 and the pro-2 descent of geometric deck normalizers in C.3, not by certificates; C.3 applies Boggi–Zalesskii, BLMS 57 (2025), Thm A(iii), to a dense embedding that is not a profinite completion: check that application before building on C.10. C.9 (Open there): the same for the full profinite groups. Check C.2; then determine the image and the fixed sets completely, and attack C.9 (a loop-preserving automorphism of the free profinite group with the pro-2 obstruction, or an obstruction found directly in finite quotients, by program).
- **The centralizer of `S_3`, his two lifts, and torsion (Part E (b), Part D (b)).** LM3 E.7 (Proved there, checked): with the normalizer definition of §§26–27 the quotient `Γ'_{0,3}` is `GT_0` and `Γ'_{0,ν}` is `GT` for `ν ≥ 4`; E.10 (checked): `Γ'_{1,1}` is `GT`. LM2 B.m2 (Proved there): his loop equation of §46 (cote 140-3) is equivalent to Drinfeld's relations (I) and (II); LM2 A.3. LM2 B.m7 (Known there): complex conjugation is its own centralizer in `GT_0`. LM2 B.g10 (Proved there): the pro-`ℓ` group of normalized solutions with `λ = 1` has no torsion, and finite subgroups of the pro-`ℓ` solution group inject into the roots of unity of `Z_ℓ`. LM3b A.13: the outer IA group of a free pro-`ℓ` group is torsion-free, `ℓ = 2` included. LM3b A.11: for `ℓ ∤ 6` every `S_3`-invariant graded class lifts to the centralizer of `S_3`. For Part E (b) start from E.7 and B.m2, then settle his condition on the two lifts; LM3b F.3 (pro-`ℓ`, `ℓ ≥ 5`: `GT¹_ℓ ⊊ GT¹_{0,ℓ}`; reviewed: correct) and F.4 (Open there: `GT̂ ≠ GT̂₀`, and `ℓ = 2, 3`) bear on it. For Part D (b) in type `(0,3)`: B.g10 leaves room, in each pro-`ℓ` group, for elements of order dividing `ℓ − 1` that are not conjugate to complex conjugation. Decide whether the profinite `GT_0`, and `GT`, contain an element of finite order whose multiplier `λ` is a root of unity of `Ẑ*` other than `±1`: construct one (by program in finite quotients, with the proof that it lifts) or prove that every element of finite order is conjugate to `(−1, 1)`.
- **How large the full groups are (Part D (b), Part F (b)).** LM3 B.4, B.5 (checked): the extended geometric group is a proper subgroup of `Autext_lac(π̂)` for every hyperbolic type and is not normal at `(0,3)`. LM3b A.3, A.14 (Refuted there, pro-`ℓ`, every `ℓ`): the geometric subgroups of types `(0,3)` and `(1,1)` are not normal; A.6: `Σ_{0,4}` is not normal in the full profinite group either; A.4, A.16 (Open there): the full profinite types `(0,3)` and `(1,1)`; A.9: in the pro-`ℓ` types `(0,3)`, `(0,4)`, `(1,1)` the conjugates of the geometric subgroup form a Cantor space. LM3b D.11 (Known there): the centralizer of the Galois image in the outer automorphisms of the geometric group of a hyperbolic curve `U` over a number field `K` is `Aut_K(U)`. Part F (b) compares centralizers of finite groups in `𝒯̂` and in `𝒯̂̂`: these statements say that the two ambient groups differ by a great deal, so prove each comparison and do not transfer it.
- **The exact groups in his drilling theorem (Part A (d), Part C).** LM3 A.3 and A.13 name the Birman group with permutations of the old punctures and with orientation-reversing classes, and the three lift extensions with the mixed fundamental group. Checked against scans 187–189 (LM3 review): his announced `1 → π → Autext(π′, i) → Autext(π) → 1` is A.3's extended sequence, and his `𝒯^{00}` sequence is its pure orientation-preserving subgroup, of index `2·ν!` (A.1): the index is right. The profinite analogue of the theorem of scans 186–189 is false for loop-preserving groups: LM3b B.4, B.5, B.10 (reviewed: correct): for `(0,4) → (0,3)` the map from the cusp stabilizer in `Out_lac(π̂′)` to `Aut_lac(π̂)` is onto with kernel `Q ≠ 1`, and the outer filling kernel is `Q ⋊ π̂`; B.6 restores exactness on the normalizer of the point-pushing subgroup, with image `GT̂ × S₃`. Part A (d) and Part C must keep the discrete theorem apart from its profinite analogue.

## What the outcome must be

**The rule that governs everything below: push.** The work is to settle the questions, not to describe them. Give most of the time to the hardest item, the main question first. Partial results (cases proved, reductions, computations, the smallest undecided instance) are steps you write down and then build on; they never finish an item. When an approach stalls, take the next one: a different method; a reduction to a theorem you find, open and check; a larger or smarter search for a counterexample; a stronger statement that implies the item; a weaker one that it implies, which you then push up. Do not deliver while an item is undecided and an untried approach remains. A gap in a proof is an undecided step: mark it and attack it; never paper over it, and never present a proof with a gap as a proof.

**1. The deliverables.** One ZIP with: `LM4_FINITE_GROUP_ACTIONS_paper.tex` and its PDF; `LM4_FINITE_GROUP_ACTIONS_results.csv`; `LM4_FINITE_GROUP_ACTIONS_readings.csv`; `LM4_FINITE_GROUP_ACTIONS_references.bib`; `LM4_FINITE_GROUP_ACTIONS_report.md`; `code/` with every program and its output (their form is fixed under WHAT TO DELIVER below). `LM4_FINITE_GROUP_ACTIONS_results.csv` has one row for every numbered statement of the paper, with its status, and the paper has at least one numbered statement for each of the 7 items of "What is to be settled", for each lead, and for each lettered task (a), (b), … and each numbered task of every part. `LM4_FINITE_GROUP_ACTIONS_report.md` opens with a table: one line per item, per lead and per lettered task, giving the statement numbers that answer it and its outcome, (a) or (b), or, in a return marked INCOMPLETE, the state reached.

**2. What counts as done, for each item, lead and task.** Exactly one of:
- (a) **proved**: in his form, or in its strongest correct form, with a complete proof;
- (b) **refuted**: by a complete counterexample, checked by a program when it is finite, together with the strongest true statement in its place, proved;
Partly settled is not an outcome. The cases proved, the computations run, the obstruction as an exact statement and the smallest undecided instance are the state of an item you are still working on: record them as you go, then attack the obstruction, starting from that instance.

A statement labelled Known counts only together with the derivation of his statement from the cited theorem, in the form he gives it, with the proof of the reduction. A statement may be labelled Open only in a return marked INCOMPLETE (rule 4), with the cases proved, the computations run, the obstruction, the smallest undecided instance, and every approach tried with where it failed.

**3. What is not acceptable.** A survey or a status report; "open, see [reference]"; a plan, a sample or an outline; a summary of what would be done; a computation described and not run; an item, a lead or a lettered task without a row.

**4. When the work is finished.** Only when every item, every lead and every lettered task is proved (a) or refuted (b). Keep working until then: do not stop because the remaining items are hard, because a partial result looks presentable, or because much has already been done. If the session itself ends first (the environment stops you, not your choice), the first line of `LM4_FINITE_GROUP_ACTIONS_report.md` reads INCOMPLETE, and its table marks every undecided line with the state reached, every approach tried with where it failed, and the next step you would take. Never present such a return as complete or as following an allowed alternative: there is none.

**5. If the execution environment disconnects.** Wait for it and retry for at least 10 minutes. If it does not come back, the work must still reach us, so write it out in this chat as text: every file in full, each in its own code block headed by its file name. That means the paper's LaTeX as far as it is written, the results and readings CSV, the references, the report, and every program you ran with its output (the code you ran to save each file contains its text: take it from there). Then continue the remaining parts directly in the chat, in the same form, until every part is written. Say at the start which files were lost and which parts are not yet written. An answer that only reports the disconnection, describes what was saved or asks for the files again, without writing out the work, is not acceptable.

## Parts

Every lettered ask below is one or more rows of the results register. A row is done only in one of the three ways of "What the outcome must be": proved in his form or in its strongest correct form; refuted by a complete counterexample with the strongest true statement proved in its place; or partly settled, with the cases proved, the computations run and the obstruction as an exact statement with the smallest undecided instance. Theorems of the literature are tools here, not answers: each time one is used, state it with its hypotheses and theorem number and then derive Grothendieck's statement from it in the form he gives, with the proof of the reduction.

Tools named in the asks (statements read for this prompt in freely accessible copies; "through X" means that only X, which quotes the theorem, was read, so state the theorem you use from its source). Periodic maps and finite groups of homeomorphisms of the disc, the plane and the sphere: Constantin–Kolev, Enseign. Math. 40 (1994), Lemma 2.5, Theorems 3.1 and 4.1, Corollary 4.2; Kolev, Enseign. Math. 52 (2006) (a compact group of homeomorphisms of `S²` is conjugate to a closed subgroup of `O(3)`). Realization: Kerckhoff, Ann. of Math. 117 (1983), read in the announcement Bull. AMS 2 (1980) (closed surfaces of genus ≥ 2, orientation-reversing classes allowed; the announcement says that the method covers geodesic boundary and cone points and does not name punctures). Teichmüller's theorem for type `(p, n)`: Bers, Bull. AMS 5 (1981), §3 (D). Fixed sets of finite groups in Teichmüller space and rotation angles: Harvey, Trans. AMS 153 (1971), Theorem 2, Corollary 3, Theorem 7. The Birman–Hilden property: Margalit–Winarski, arXiv:1703.03448, Theorem 2.1 (Birman–Hilden: unbranched or solvable covers), Theorem 2.2 (MacLachlan–Harvey: all finite regular branched covers of hyperbolic surfaces), Proposition 3.1. Homeomorphism groups: Hamstrom and Scott through Yagasaki, arXiv:math/0010223, Lemma 2.1 and Theorem 1.1; Earle–Eells, Bull. AMS 73 (1967), Theorem 1 (diffeomorphisms, closed surfaces). Torsion-free finite extensions: Eckmann–Müller, Comment. Math. Helv. 55 (1980), Theorem 2 and Corollary 2; Eckmann–Linnell, ibid. 58 (1983). Anti-involutions: Gross–Harris, Ann. Sci. ENS 14 (1981), Proposition 3.1; Mochizuki, *Topics surrounding the anabelian geometry of hyperbolic curves* (2003), Theorem 3.6, Corollaries 3.7, 3.8, 3.13, 3.15. Abelian subgroups: Birman–Lubotzky–McCarthy, Duke Math. J. 50 (1983), through Behrstock–Minsky, arXiv:math/0512352. Profinite completions: Bridson–Conder–Reid, arXiv:1401.3645, Theorem 5.1, Corollaries 5.2 and 5.3; Minasyan–Zalesskii, arXiv:1504.00613, Theorem 1.1 and Corollary 3.5, with Minasyan, arXiv:0905.1282, Proposition 3.2; Boggi, arXiv:2408.12486v2 (January 2026, unrefereed), Theorem C; Boggi–Zalesskii, *Finite subgroups of the profinite completion of good groups*, Bull. London Math. Soc. 57 (2025) 236–255 (known to this prompt by its title only). Profinite groups with loops: Nakamura, J. Math. Sci. Univ. Tokyo 1 (1994), Corollary (1.3.4), Lemma (2.1.2), Theorem (2.1.1); Mochizuki, *The absolute anabelian geometry of hyperbolic curves* (2004), Lemmas 1.3.1 and 1.3.7; Mochizuki, Tohoku Math. J. 59 (2007), Proposition 1.2; Mochizuki–Tamagawa, Hokkaido Math. J. 37 (2008), Proposition 1.4 and Remark 1.2.2. The groups `GT_0` and `GT`: Harbater–Schneps, Trans. AMS 352 (2000), Main Theorem and Theorem A.

**A. Groups with loops: the rigidity statements (item 1; §12, §13 bis, §18; scans 91–92, 98–100, 115–118, 182–190).**
(a) Write his definition of a group with loops of type `(g, ν)` and of an exterior group with loops, discrete and profinite, with the orientation module `T_π` in both of his forms (kernel of `∏ L_i → π_ab`, scan 116; `H²(π, Z)^{⊗-1}` for `ν = 0`; and the cohomological form `H²_!(B_{π_1 U}, Ẑ) ≅ T_π^{⊗-1}` of scan 130, margin), and prove that the three agree wherever two are defined, with the canonical isomorphism written out. Correct the bracket of scan 116 ("π abélien ssi g = 0, ν ≤ 3 ou g = 1, ν = 0") and prove the corrected list. State for which types each of his formulas holds: the rank `2g + ν − 1` of `π_ab` (scan 86) is for `ν ≥ 1` only (`I = ∅` is allowed, scan 82), and `(S², pt)` is admitted with `π = 0` (scans 91–92), the one admitted type in which `κ_i` is not injective (scans 92, 97).
(b) For every anabelian type and for the four abelian types `(0,0)`, `(0,1)`, `(0,2)`, `(1,0)` treated on scans 222–230, prove or refute, in the discrete case: `Centr(π) = 1`; the centralizer in `π` of every subgroup of finite index is trivial; `Norm_π(L_i) = Centr_π(L_i) = L_i`, including his separate case `ν = 1` (scan 117, margin: the normalizer of the subgroup generated by `∏[x_α, y_α]` in the free group); `Centr_π(L_i^n) = L_i` for every `n ≥ 1`; the classes `[L_i]` are pairwise distinct; `Norm_E(L_s) = E_i` for an extension `E` of a group `Γ` by `π` coming from an action (scan 99); `Trans_E(L_i^d, L_i) = E_i` for every `d ∈ N*` (scan 69). For each excluded type give the element that makes the statement fail. Prove his statement of scan 98 (since the centre of `π` is trivial, an extension of `Σ` by `π` is the same, up to unique isomorphism, as a homomorphism `Σ → Autext(π)`), which he excepts only for the annulus: determine what classifies the extensions for the annulus and for the torus, which he omits there (`π = Z²` has non-trivial centre too), and correct the statement.
(c) The same list for the profinite completions `π̂_{g,ν}` (his margin on scan 118: "Ce n'est démontré pour le moment dans aucun cas anabélien profini"), with (2) and (4) of scans 500–501 (`L_i = Centr_π(L_i^n)`; `Centr_π(Λ_i^n) = Λ_i` for the procyclic subgroups generated by the elements `x_i, y_i` of a base), which he marks "pas prouvé". Most of it is now in the literature: derive each of his statements, in his form and for every anabelian type, from the theorem that gives it (trivial centre: Nakamura 1994, Corollary (1.3.4); trivial centralizer of every open subgroup: Mochizuki 2004, Lemma 1.3.1, or Mochizuki–Tamagawa, Proposition 1.4; no torsion: Mochizuki–Tamagawa, Remark 1.2.2; `Norm_π(L_i) = L_i`, hence `Centr_π(L_i^n) = L_i`, and distinct classes not commensurable: Mochizuki 2004, Lemma 1.3.7, and Mochizuki 2007, Proposition 1.2; (2) and (4) for `ν ≥ 1`: Nakamura 1994, Lemma (2.1.2)), writing out each reduction, and prove his Lemme 5 and Corollaire 2 of scans 498–501 from the trivial centralizers of open subgroups alone, so that (2) and (4) are not needed for them. Then write out (4) for `ν = 0`, that is `Centr_π(⟨x_i⟩^n) = ⟨x_i⟩` for a base element of the profinite completion of a closed surface group of genus ≥ 2, from the two sources that give it (Boggi–Zalesskii 2019, Prop. 3.6; Mochizuki 2007, Prop. 1.2 (ii), applied to the one-node degeneration pinching `x_i`; see LM3 D.15 and the LM3 review, §4.3); decide whether the statements of the list follow from his axioms for an abstract profinite group with loops (the presentation of scan 318, relation (4)) alone: a proof, or a profinite group satisfying the axioms in which one of them fails; and decide which statements of the list survive in the maximal `m`-step solvable quotients of `π̂_{g,ν}`, `m ≥ 2` (centre- and torsion-freeness are claimed in arXiv:2601.07112v4, 2026, unrefereed: check the step you use; the loop-subgroup statements are yours to prove or refute, with the smallest `m` for each).
(d) Prove his theorem of scans 186–189 (for `π'` of type `(g, ν+1)` and `π = π'/⟨⟨L'_i⟩⟩` both anabelian, `Autext(π', i) → Aut(π)` is an isomorphism) completely, including the "vérifications de compatibilité" he leaves and the passage "à un sous-groupe d'indice 2ν! près" (scan 189): determine exactly which subgroups of `Autext_lac` and `Aut_lac` correspond (orientation, permutation of the classes), and correct the index if it is wrong. Then decide the same statement for the types where exactly one of `π', π` is abelian.
Done for Part A: every statement of (b) and (c) has a proof or a counterexample for every type; (d) is a theorem with all compatibilities proved.

**B. Finite groups acting on surfaces: sections, fixed points, `μ` (items 2–4; §§15, 17, 18, 33; scans 137–160, 179–203, 437–471).**
(a) Prove the "lemme fondamental" of scans 141–148 completely, for topological actions with no smoothness assumed, closing the two gaps he leaves. The first is the lemma of scans 146–147 (a homeomorphism of finite order of `C` commuting with `z ↦ z+1` and fixing `0` is the identity; "On doit pouvoir terminer par la suite spectrale d'Adams"): as written it is false, since `z ↦ z̄` has order 2, commutes with `z ↦ z+1` and fixes `0`; state it with the hypothesis it needs (he is in the case `Γ = Γ⁰`), prove it, and show where his own argument uses the hypothesis. The second is the local form of an anti-involution at a fixed point (scan 148, margin; scan 440, the admitted lemma). Tools: Constantin–Kolev (Lemma 2.5, Theorems 3.1 and 4.1, Corollary 4.2) for one periodic map; Kolev's theorem for finite groups. Derive parts (a) and (b) of the lemma from them, with the invariant disc around a fixed point constructed for a finite group and not only for one map; then give a proof of the lemma of scans 146–147 along his own line (the action induced on `C/Z`, which he hopes to finish by a spectral sequence), or prove that this line cannot be completed.
(b) Prove the theorem of scans 148–149 and the corollary of scans 150–151 in full, and answer the question of scan 139 in all cases, including `Γ⁰ = 1`, `Γ = {1, σ}` (the map `π_0(X^Γ − S^Γ) →` classes of splittings): that is his theorem of scans 440–445; prove it with (c) `π^{σ_i} = 1` for a component `≅ R` and (d) `π^{σ_i} = Im φ_i ≅ Z` for an oval, for surfaces with punctures (he treats `ν = 0` only: do the case where the anti-involution permutes or fixes punctures, and prove what the classes of splittings see of the position of the punctures on the real components, as his margin of scan 437 asks). His theorem with the centralizers is Mochizuki 2003, Theorem 3.6 and Corollary 3.7 (hyperbolic real Riemann surfaces, compact or not): derive it in his form, and prove what he could not, the local form at a fixed point with no smoothness (Part B (a)). With punctures on the real locus each real puncture is adjacent to two half-branches: prove that the classes of splittings recover which punctures are real, on which component of `X^σ` each lies and their cyclic order on it up to reversal, and nothing more.
(c) Complete §18. Prove the "lemme fondamental" of scan 193 and its corollary of scan 194 for every anabelian type without assuming the action realizable, by deriving them from the realization theorem for finite cyclic groups (state the theorem you use with its source: the announcement of Kerckhoff's theorem is for closed surfaces; for punctured surfaces either cite the statement that covers them or prove that case, for instance from the theorem that convergence groups are Fuchsian (Gabai, Bull. AMS 25 (1991), Theorem 1) or, for torsion-free extensions, from Eckmann–Müller, Theorem 2; and prove the reduction he sketches on scans 194–196); prove them in the two abelian cases `(0,2)` and `(1,0)` or refute them there (scan 194, margin). Then settle his questions c), d), e) of scans 197–198 for every finite `Γ ⊂ Aut_lac(π)`, orientation-reversing elements included: `π^Γ = 1`? a unique maximal section subgroup up to `π`-conjugacy (check his proof of scans 201–203 line by line and repair it if needed)? finitely many `π`-classes of lifts? Write out the counterexample behind "pas vrai !" and "faux !" (scans 198–200: the deleted theorem on the normalizer of a finite `Γ_0 ⊂ Aut_lac(π)⁰` and the lemma on roots `u^d = u_0`), with explicit groups, and prove the strongest true statement about `Norm(Γ_0)`, `Centr(Γ_0)` and the finite subgroups containing `Γ_0`.
(d) The invariant `μ` (scans 155–160). Prove that `μ_E` is determined by the extension `E` together with its loop structure and `T`, by giving a formula for `μ(u)` in terms of the action of `u` on a suitable subgroup (he proposes the normalizers `E_i`, margin of scan 159), valid in every anabelian case; decide whether the loop structure is needed (two geometric extensions isomorphic as abstract extensions with different `μ`, or a proof that none exist); compute `μ` for every finite group acting on the torus and on the annulus, completing scans 157–159, including the statement he doubts on scan 180–181 (d ⇒ a in the abelian case, "pas prouvé !": prove it by classifying finite group actions on `C*` and `S¹ × S¹` up to conjugacy, or refute it). Prove or refute his margin of scan 179 ("Ça doit être le seul contre-exemple (dans le cas renvers. d'une orientation ...)"): that, up to conjugacy, `z ↦ 1/z̄` on `C*` generates the only faithful action of a finite group on a surface of abelian type that is homotopically trivial without being an action by translations, and that any such action is by an anti-involution. For closed surfaces Harvey 1971, Theorem 7, reads the rotation angles from the epimorphism onto `Z_n`: derive your formula for `μ` from it, extend it to punctured surfaces and to groups with reflections, and define `μ` on the torsion of the profinite completion `Ê` (Part D (a)).
(e) §33. Classify the conjugacy classes of anti-involutions of `X_g` and of `U_{g,ν}` in `A_{g,ν}` and in `𝒯_{g,ν}`: his proposition of scan 439 with its two marginal corrections gives two families (quotient non-orientable, `g = γ + μ`; quotient orientable, `g = 2γ + μ − 1`); prove the complete list with the count for every `g` (expected `(g+1) + ⌊(g+2)/2⌋ = ⌊(3g+4)/2⌋`, the classification of real curves of Weichold and Klein: Gross–Harris, Proposition 3.1), extend it to `ν > 0` with the position of the punctures as part of the invariant, and prove that distinct classes in `A_g` stay distinct in `𝒯_g` (he hopes so on scan 440; derive it from the uniqueness of realization of Part C (b)). Prove Corollaries 1 and 2 of scans 445–448 in both families (he proves them only when `X_g/σ` is non-orientable), and derive from them and from Mochizuki 2003, Corollary 3.8 (the components of `M_{g,r}(R)` correspond to the classes of involutions over complex conjugation in the extended mapping class group, with their centralizers) the number of components of `M_{g,ν}(R)` for every `(g, ν)`. For his group `G = H ⋊ {1, τ}`, `H = ⟨ρ_j⟩ ≅ Z^g` (scans 449–470): identify the `ρ_j` as mapping classes, compute the exterior action of `D̃_{2g}·H` on `π_g` on explicit generators (his task 1 of scan 467), prove or correct the presentation (52) of scan 469, and settle his questions of scan 470 with proofs: is `H` a maximal free abelian subgroup (the maximal rank is `3g − 3`, Birman–Lubotzky–McCarthy, so for `g ≥ 2` exhibit the larger subgroup, and then find and prove the property that does characterize `H`, for instance among subgroups generated by Dehn twists about curves whose union does not disconnect `X_g`); what is its normalizer and how does it act on `H`; and do the groups `SL(2, Z)_j` attached to the "lanières" through the tubes `T_j` (his task 2 of scans 467–469: the one-holed torus made of `T_j` and a strip, with its special Teichmüller group) play the part of the rank-one subgroups of a reductive group: construct them in `𝒯_g`, compute their commutation relations with `H` and with each other, decide whether `H` and these subgroups generate `𝒯_g⁺`, and state and prove the analogy in the strongest form that is true.
(f) By program: for every type `(g, ν)` with `2g + ν ≤ 6` list the conjugacy classes of finite subgroups of `𝒯_{g,ν}` (from the classification of group actions on surfaces of those types), and for each compute `Φ(π, Γ)`, the stabilizers, the values of `μ`, and the numbers of classes of full and partial splittings; check (b), (c), (d) on the whole list. Attach code and tables.
Done for Part B: (a)–(e) are theorems or refutations with every case named; the table of (f) exists and agrees with them.

**C. The 2-equivalence, realization, drilling (item 5; §12, §§23–24; scans 101–102, 264–294).**
(a) Define both 2-categories and the 2-functor of scans 264–271 exactly (objects, arrows, 2-arrows; admissible surfaces; the loop condition `M_lac`), and his four levels of fidelity as he defines them on scans 271–273 and 279–280 for a topological group `A` with `π_i(A) = 0` for `i ≥ 2`. Prove his translation: for `A = A_{g,ν}` and a finite group `Γ`, 0-, 1-, 2-, 3-fidelity are respectively `π_1((A⁰)^u) = 0`, `(A⁰)^u` connected, uniqueness of lifts of `Γ → π_0(A)` up to conjugation by `A⁰`, existence of lifts; and write the corrected conditions in the abelian types, where `π_1(A⁰) ≠ 0` (his margin on scan 281: "Trop brutal ! ... à reprendre avec soin"). On the same scan he adds "Le plus agréable serait que ce soit un homotopisme ... qui exprimerait qu'on a une ∞-équivalence": identify the map he means, state it as the comparison between the fixed points of `Γ` in `A` (for the action by conjugation through `u`) and the homotopy fixed points, and prove that it is a homotopy equivalence for finite `Γ` in the anabelian types; decide each abelian type.
(b) Prove his conjecture of scans 270–271 for every anabelian type and every finite `Γ`, orientation-reversing elements allowed, in the topological category: each of the four levels with a complete proof. The statement is classical for closed surfaces and orientation-preserving groups (Harvey 1971, Theorem 2 and Corollary 3: the fixed set of a finite group in Teichmüller space is the image of one Teichmüller space; MacLachlan–Harvey 1975): what is asked is the proof in his generality, with punctures, orientation-reversing elements and actions by homeomorphisms with no smoothness. The following chain is proposed and is not authority; check every link with its exact hypotheses and replace any link that fails. Existence of lifts: the realization theorem for finite subgroups of the extended mapping class group (for punctured surfaces state the theorem you use with its source, or prove that case from the closed one). Uniqueness up to `A⁰`: if `ρ_1, ρ_2: Γ → A` have the same image in `π_0(A)`, choose invariant conformal structures `c_1, c_2` of finite type (this needs the quotient to be a surface with boundary, cone points and corner points, hence local linearity of the finite stabilizer groups and not only of single periodic maps: Kolev's theorem; prove this step); the extremal quasiconformal map `h: (S, c_1) → (S, c_2)` isotopic to the identity is unique (Bers, §3 (D), for type `(p, n)`), and `ρ_2(g)^{-1} h ρ_1(g)` is orientation preserving, has the same maximal dilatation and is isotopic to the identity, hence equals `h`. Connectedness of `(A⁰)^u`: fibre-preserving homeomorphisms isotopic to the identity are so through fibre-preserving ones (Margalit–Winarski, Theorem 2.2; the quoted statements are for orientation-preserving deck groups: prove the case with reflections). `π_1((A⁰)^u) = 0`: the identity component of `A^u` is the identity component of the homeomorphism group of the quotient surface with its branch points and punctures marked and its mirror boundary (Yagasaki, Lemma 2.1; prove that no exceptional pair of that lemma occurs for hyperbolic `U`). State the final theorem as an equivalence of 2-categories, and prove for each abelian type and for infinite `Γ` which levels fail (give an infinite `Γ` for which each level fails).
(c) §24. Prove his description of `A^{0Γ}` (scans 282–286): the neutral component is `Aut(V')⁰`, and `π_0(A^{0Γ})` is the subgroup of `π_1(Mon(S^!, U))^Γ` he names; then prove or refute `H⁰(Γ, π_1(Mon(S^!, U))) = 1` and `H¹(Γ, B⁰) = 1` (scan 285), and deduce the exact value of `π_0(A^{0Γ})` (expected for hyperbolic `U`: both vanish and `A^{0Γ}` is connected, by the Birman–Hilden property for `U → U/Γ` and the uniqueness of realization applied to `V = U ∖ S^!`; write the proof, groups with reflections included, where the quoted Birman–Hilden statements do not apply).
(d) Prove the conjecture of scans 286–288 (existence and uniqueness up to unique isomorphism of the drilled group `(Π', I'^!) → Π` with torsion-free extension) and carry out the programme I, II, III of scans 292–293: (I) the bijection (∗) `Φ(Π', Γ) ⊔ I'^! → Φ(Π, Γ)` of scan 290 in general (he has it only for realizable actions and for `I'^!` a single element); (II) full faithfulness of the drilling functor of scan 291; (III) an extension of a finite group by a group with loops without elements of finite order is a group with loops, with the classes of the centralizers of the `L_i` as loop classes (also scan 353; for `ν = 0` this is Eckmann–Müller 1980, Corollary 2, and the extension can be a non-orientable surface group when the finite group reverses the orientation, so his statement has to be corrected to allow it; for `ν ≥ 1` derive it from Stallings's theorem on torsion-free virtually free groups and Eckmann–Müller, Theorem 2, on pairs, proving the step that makes `(E; centralizers of the L_i)` a duality pair). Then prove his criterion of scan 294 (a faithful exterior action is realizable if and only if it lifts by drilling at `Φ(π, Γ)` to an admissible action whose extension is a group with loops), as a theorem about abstract groups with loops, with a proof that does not pass through surfaces wherever you can give one; where you cannot, isolate the step that uses the geometry as an exact statement.
(e) The theorem of scan 304 (`π_0(SA_{g,ν}) ≅ SΓ^{!+}_{g,ν}`, an extension of `Γ^{!+}_{g,ν}` by `T^{S_{g,ν}}`, and `(SA_{g,ν})⁰` ∞-connected, with the two abelian cases of scans 303–304): prove it, identify the extension class in `H²(Γ^{!+}_{g,ν}, T^I)`, prove his remark of scan 306 that the extension is non-trivial over every non-trivial finite subgroup of `Γ_i⁺`, and compute the class for `(0,3)`, `(0,4)`, `(1,1)`, `(1,2)`.
Done for Part C: (b) is a theorem with four proved levels; (c), (d), (e) are theorems or refutations; nothing is left as "known".

**D. The profinite theory (items 1 and 6; §31; scans 118, 352–354, 384, 388–394).**
(a) For a finite `G ⊂ 𝒯(π_0)` (an exterior action stabilizing a discretization `π_0 ⊂ π = π̂_0`), with discrete extension `E` and completion `Ê`: prove his two "conjectures sans vergogne" of scan 393 for orientation-preserving `G` from the named theorems, writing each reduction: the bijection of classes of splittings from Bridson–Conder–Reid, Theorem 5.1 (every finite subgroup of `Ê` is conjugate into `E`; maximal finite subgroups conjugate in `Ê` are conjugate in `E`), by the passage from `Ê`-conjugacy to `π`-conjugacy; and `π^G = 1`, which is not in that paper, from the centralizer condition `C_Ê(k) = closure of C_E(k)` (for cocompact `E`: Minasyan–Zalesskii, Theorem 1.1, with Minasyan, Proposition 3.2; for `ν > 0`, where `E` is a free product of cyclic groups, prove it, stating the theorem on centralizers of torsion in free profinite products that you use). Then prove what these do not give: both statements when `G` contains orientation-reversing elements (`E` is then a group with reflections; for anti-involutions the bijection of classes of elements of order 2 follows from Minasyan–Zalesskii, Corollary 3.5; decide the dihedral subgroups, and compute `π^G` for them: expected `Ẑ` for the reflection in an oval and `1` for a line, as in his theorem of scans 440–445); the profinite forms of the theorem of scans 148–149 (every finite subgroup of `Ê` meeting `π` trivially is cyclic or dihedral; finitely many classes; unique maximal section subgroups) and of c), d), e) of scans 197–198; and the profinite `μ`: prove that the multiplier of Part B (d) extends to the torsion of `Ê` with values in `T̂ ⊗ Q/Z` and is invariant under the automorphisms of `Ê` that preserve the loop structure.
(b) Without the hypothesis that `G` stabilizes a discretization (his remark on scan 384: "ce n'est sans doute pas automatique"): decide, for the types `(0,3)`, `(0,4)`, `(1,1)`, whether every finite subgroup of `𝒯̂̂_{g,ν} = Autext_lac(π̂_{g,ν})` is conjugate to a subgroup of `𝒯_{g,ν}`. The question has two layers. For finite subgroups of the completion `𝒯̂_{g,ν}` (it embeds in `𝒯̂̂_{g,ν}` for `g ≤ 2`, where the congruence subgroup property is known) Boggi, arXiv:2408.12486v2, Theorem C, states for genus ≤ 2: the classes of solvable finite subgroups of the mapping class group and of its profinite completion correspond bijectively, torsion elements are conjugacy distinguished, and the centralizer of a finite subgroup `G` in the completion is the closure of its centralizer in the discrete group (unrefereed: check the step you use; state also what Boggi–Zalesskii give). Derive from it the answer for this layer, extend it to orientation-reversing elements, and settle the finite subgroups that are not solvable (in genus ≤ 2 these are icosahedral groups acting on the sphere with marked points: prove that this is the list). For finite subgroups of `𝒯̂̂_{g,ν}` outside `𝒯̂_{g,ν}` nothing is known to this prompt: either prove that every finite subgroup is conjugate into `𝒯̂_{g,ν}`, or construct one that is not (for instance of order 2 or 3 in `Autext_lac` of the free profinite group of rank 2, by a program working in finite quotients and a proof that the examples lift), or prove the pro-`ℓ` form and state exactly what is missing. For `(0,3)` this is a statement about torsion in the centralizer of `S_3`, the group `GT_0` of Part E (b): decide whether its elements of finite order are the conjugates of the element `(−1, 1)`.
(c) Scan 352–354: his corollary that `Discrét(π) → Discrét(π')` is injective for `π'` of finite index, the description of its image for `π'` normal (the discretizations `π'_0` such that `G = π/π'` acts through `𝒯(π'_0)`), and the element `γ` of scan 354 ("Un tel γ existe toujours") for `π = π̂_{0,3}`, `π'` of index 2, are answered by LM3 B.9, B.10 and B.11, with the explicit `γ` of the LM3 review, §4.2 (see the block of 12 November): write out the step of B.10 named there. What remains is the image for `π'` not normal, and the fixed sets: determine both.
(d) The profinite form of (III) of Part C: is a torsion-free extension of a finite group by `π̂_{g,ν}` (with exterior action preserving the loop structure) the completion of a group with loops? Prove it when the action stabilizes a discretization; in general prove the pro-`ℓ` version or give the smallest undecided case, with what you tried. Collas–Philip–Yamaguchi (arXiv:2605.02577, May 2026, unrefereed) study the profinite analogues of Fuchsian groups (their Theorems 1.3 and 2.4: such a group has a torsion-free open normal subgroup, with a bound on the derived length of the quotient): state exactly what they give for this question, check the step you use, and prove the rest.
Done for Part D: (a) is settled; (b) is decided for at least `(0,3)`, with the program attached; (c), (d) each end in a theorem, a counterexample, or an exact obstruction with the smallest undecided instance.

**E. §25 and §25 bis (item 7; scans 294–317).**
(a) Construct `SE^!`, `SE`, `SΓ^!`, `SΓ` as he does on scans 296–300 (pairs `(u, (g_i))`; classes of auto-equivalences of `B_I → B_{D*} → B_U`), prove that the two constructions agree and that `SE` is an extension of `Γ` by `T^I × π`, and prove the compatibility of scan 305–306 (the extension of `Γ_i` by `T` obtained from `SΓ` by `pr_i` is the group of loop automorphisms of `π_i` normalizing `L_i`).
(b) The two-group situation of scans 307–312 (`𝒢 = Γ·G` acting, `G` finite): prove every assertion: the lifting `r` of `G_Q` forces the lifting of `Γ_Q`; `Norm_E(r(G_Q)) → 𝒢` is injective with image `𝒢_Q`; and decide his question of scan 312: for `Γ'^♮ = ∩_Q Γ'(Q)` in `Γ' = Autext_lac(π)`, is `Γ^♮ = Centr_{Γ'^♮}(G)`, and is `Γ` recovered as a normalizer? Do it in the discrete case for `π = π_{0,3}`, `G = S_3` and for `π = π_{1,1}`, `G = Z/4, Z/6`, by explicit computation, and then in the profinite case for `π̂_{0,3}`, `G = S_3` (his case, scan 312), where the question becomes: describe the subgroup of the centralizer of `S_3` in `Autext_lac(π̂_{0,3})` of elements that have a lift commuting with `ρ` and a lift commuting with `σ_0` (scans 316–317), and decide whether it is the whole centralizer. The centralizer itself is the group `GT_0` of Harbater–Schneps (Main Theorem (a)): pairs `(λ, f) ∈ Ẑ* × F̂_2'` satisfying (I) and (II), which by their Theorem A are the conditions `[θ, F] = inn(f)` and `[ω, F] = inn(y^m f)`, `m = (λ − 1)/2`, on the lift `F: x ↦ x^λ, y ↦ f^{-1} y^λ f`, with `θ, ω` lifts of a transposition and of a 3-cycle. So his condition asks whether these inner automorphisms can be removed by changing the lift within its class: write it as a statement about the classes of lifts of order 2 and of order 3 and settle it (expected, to prove or refute: the transposition `z ↦ 1 − z` has one fixed point in `U`, hence one `π̂`-class of lifts of order 2 by Bridson–Conder–Reid, Theorem 5.1, so the first condition holds for every element of the centralizer; the 3-cycle has the two fixed points `e^{±iπ/3}`, hence two classes of lifts of order 3, which an element of the centralizer preserves or exchanges, so the second condition cuts out a subgroup of index at most 2 that contains the image of `Gal(Q̄/Q(√−3))`: determine it in terms of `(λ, f)`).
Done for Part E: (a) proved; (b) decided discretely with explicit groups and, profinitely, either decided or reduced to an exact statement about pairs `(λ, f)`.

**F. What the later sections use (§§26–32; scans 318–436).** Each of the following is a numbered lemma with a stable label (LM4-F.a, LM4-F.b, LM4-F.c), stated in the form in which §§26–32 use it and proved; LM3_TEICHMULLER_TOWER and LM6_POINTS_AS_SECTIONS cite these labels.
(a) The action of a finite group on the sets of discretizations and of prediscretizations of `π̂` and its fixed points (scans 352–358): determine the fixed sets and prove the answer.
(b) For a finite `G ⊂ 𝒯⁺`, the statements (c), (d) of scans 383–387 (finiteness of `Z`; open image of `N_a ∩ Z(G) → Γ_a`), translated into statements about `Centr_{𝒯̂̂}(G)` and `Centr_{𝒯̂}(G)` that do not mention `N_a`: prove or refute each in that form. For genus ≤ 2, Boggi's Theorem C gives the centralizer of `G` in the completion `𝒯̂⁺` as the closure of the discrete centralizer: derive what follows for (c) and (d), and prove or refute the same equality for the centralizer in `𝒯̂̂`, in the smallest type where it is not clear.
(c) The lifting statement of scans 390–393 (the stabilizer of a point `P` of `[U^!]` in `𝒯(π_0)^G` lifts canonically to `𝔖(π_0)^G`), and its profinite form: prove both, with the exact group to which the stabilizer lifts.
Done for Part F: each of (a), (b), (c) is a labelled lemma, proved or refuted; none is only stated.

---

THE TEXT YOU ARE GIVEN
- Grothendieck wrote *La Longue Marche à travers la théorie de Galois* by hand between January and June 1981. It was never prepared for print. What is attached is a transcription of the manuscript made by AI from scans (first pass: GPT-6 Astra, ChatGPT Pro mode; second pass, line by line against the scans: Claude, Anthropic), by package. The manuscript is in four archive files: cote 140-2 (folios 1–292, §§1–37), cote 140-3 (folios 293–650, §§38–49), cote 140-4 (folios 650bis–787, §§50–53) and cote 140-1 (a draft of 37 scans). `\scanpage{n}` marks the scan, `\mspage{n}` his folio number.
- Marks in the transcription: `\unsure{a|b}` a doubtful reading with its alternatives; `\illegible{n}` unread words; `\deleted{…}` struck by the author; `\inserted{…}` added by him; `\margin{…}` a marginal note. A reading is never final. Where your mathematics depends on a doubtful or unread place, say so at that place, work with each alternative that makes sense, and report which one the mathematics supports as evidence for the editors, with the scan number. Do not silently choose, and do not call any reading settled. The scans of the pages that matter are attached: look at them.
- His notation changes as he goes, sometimes within a section ("Notations définitives (?)", §46). Fix yours on the first page with a table giving, for each symbol you use, his symbol and the scan where he introduces it.
- He marks his own doubts ("un peu faux", "ultra-faux", "sauf erreur", "peut-être est-ce tout à fait faux ?", "Théorème (!)"). These are part of the text: a statement he doubts is treated as a question, one he withdraws as withdrawn.

WHAT IS ATTACHED
A zip with: the transcription packages listed in the manifest (the current text of each), the scans of the pages named in this prompt, his table of contents, the checked research notes of those packages (notes by the transcribing models on his conjectures, unproved claims and unpursued implications; drafts, not authority), the background papers, and `OVERVIEW.md` (a reading of the whole manuscript by Claude, from which the leads below come). Also attached, for the block of 12 November 2026: the returns LM2_LOOP_EQUATIONS, LM3_TEICHMULLER_TOWER and LM3b_TEICHMULLER_PUSH (`LM2_return/`, `LM3_return/`, `LM3b_return/`), the reviews of LM3 and LM3b (`LM3_review/`, `LM3b_review/`; Claude Opus 5.5, effort max, 12 November 2026), the notes of the literature step (`LM_EXPERT_notes/`) and the texts it read (`literature/`). Returns, reviews and notes are claims and drafts, not authority.

RULES OF PROOF (they bind every statement you deliver)
1. State the actual claim with all its data: which group (discrete, profinite, pro-ℓ), which field, which type `(g, ν)`, outer or genuine actions, base points and the choices they involve, which topology, which of his numbered conditions in which version. Do not replace it by a convenient special case; if you prove a special case, name it as one and keep attacking the general statement.
2. Type every map: source, target, the category in which it is a morphism, and each property you use (continuous, open, compatible with which outer action, defined up to which inner automorphisms).
3. Every reduction ("we may assume", "pass to an open subgroup", "fill the holes", "replace by a covering") comes with its comparison map and a proof that the exact property needed transfers in the direction needed.
4. "Up to" names the ambiguity. Keep apart: a homomorphism and its class modulo inner automorphisms; an isomorphism and a canonical isomorphism; injective, with open image, bijective; a discrete group and its profinite completion (and say when the completion map is injective); a statement over `Q` and over a finite extension.
5. Check the cases he sets aside or forgets: types `(0,0)`, `(0,1)`, `(0,2)`, `(1,0)`; `(0,3)` and `(1,1)` against the general anabelian type; residue characteristics 2 and 3; non-orientable and real cases; trivial and non-trivial centres.
6. A counterexample is given completely and, when finite or computable, checked by a program whose code and output you attach. One verified counterexample refutes the statement: say "false", and then find the strongest true statement in its place. An invalid proof alone shows a gap, not falsity.
7. No authority. His assertions, the notes of the transcribing models, and the leads marked "Lead" below (inferences by Claude from one reading, checked by no one) are all to be proved or refuted. If a lead is wrong, say so plainly.
8. Later work (Belyi, Drinfeld, Ihara, Nakamura, Matsumoto, Tamagawa, Mochizuki, Pop, Hoshi, Boggi and others) is to be used, with exact theorem numbers, wherever it proves or refutes what he asks. The task is to do the mathematics he set out, with everything now available, and to carry it through to proofs and refutations; it is not a survey. Never invent a reference; mark each bibliography entry `verified` (you opened it) or `unverified`. Before calling anything new, say what you searched.
9. What is not yet settled stays on the page as an exact statement, with what you tried and the step that fails, and you go on attacking it; it never finishes an item. Never write it up as proved, and never drop it.
10. Known and Open are not end points. A Known statement is derived from the cited theorem in the form he states it, with the proof of the reduction. A statement may be labelled Open only in a return marked INCOMPLETE (point 4 of "What the outcome must be"); it then records your own attack: the strongest partial result you proved, the computations you ran, the obstruction as an exact statement. A row "open, see [reference]" is not acceptable.

WHAT TO DELIVER
One ZIP containing:
- `<ID>_paper.tex` and its PDF (LuaLaTeX, compiles cleanly): the mathematics in the order of the parts, every statement numbered and labelled Proved / Refuted / Known (with citation) / Open, with complete proofs; each statement that answers a passage of the manuscript cites it by section, folio and scan. English, first person plural, the register of a careful research paper; quote Grothendieck in French where his wording matters, and never write in his voice. This text is meant for a book that reproduces his text and builds it out; how it will be placed there is not decided, so make it readable on its own.
- `<ID>_results.csv`: one row per numbered statement: `id, statement, status, where_proved, depends_on, manuscript_passages (section; folio; scan), depends_on_doubtful_reading (scan, alternatives), notes`.
- `<ID>_readings.csv`: every place where the mathematics bears on a doubtful reading: `package, scan, the \unsure or \illegible place, what the mathematics supports, how strongly`.
- `<ID>_references.bib`, `<ID>_report.md` (what you read, what you computed, corrections to the leads and to the notes, and, only in a return marked INCOMPLETE, the state of every undecided line), and `code/`.
The work is AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); credit it so, attribute nothing to any person, and claim no priority.

This task is long by design. Work through all parts completely; do not stop at an outline, a sample or a plan, and do not ask whether to continue. Take the time the work needs. Write the files from the start and extend them as you go, so that an interruption loses little.

**Typesetting check.** Every PDF you deliver is published as it is. Before you deliver one, read its build log: no overfull box may stick out by more than 2pt, whether a diagram, a display or a line of text. Fix each one in the source (scale or split a wide diagram, break a wide display, let a line break) and compile again. Then render pages to images and look at them: every page that had an overflow, and a sample spread over the document. Give the counts before and after in the report.
`````

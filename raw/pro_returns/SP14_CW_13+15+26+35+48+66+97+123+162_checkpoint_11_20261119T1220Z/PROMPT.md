# Second pass and research notes SP14_CW_13+15+26+35+48+66+97+123+162: Alexander Grothendieck's papers, Montpellier archive, cotes 13, 15, 26, 35, 48, 66, 97, 123, 162-1 and 162-6

You are making the second pass over **126 scan pages** from the Montpellier archive of Alexander Grothendieck,
and then writing the research notes on them:
- `13.pdf`: "Groupe de Galois motivique : notes manuscrites (s.d.), lettre (1965)." (1965), scans 2-52, 44 pages
- `15.pdf`: "Théorie arithmétique. Théorie de Galois des motifs (1965) : notes manuscites (s.d.), tapuscrit (s.d.)." (1965-[vers 1977][15]), scans 27-188, 27 pages
- `26.pdf`: "EGA VI. Plans, notations, problèmes ouverts[25] : notes manuscrites (s.d.)." ([après 1967]), scans 2-11, 10 pages
- `35.pdf`: "Plan [SGA 7] : notes manuscrites (s.d.), tapuscrit annoté (s.d.)." ([vers 1967-1973]), scans 2-5, 4 pages
- `48.pdf`: "Plan EGA VII[41] : notes manuscrites (s.d.)." ([à partir de 1967][40]), scans 2-6, 5 pages
- `66.pdf`: "Problèmes : notes manuscrites (1964)." (1964), scans 2-5, 4 pages
- `97.pdf`: "Classes de Chern des représentations[85] : lettre (1966), notes manuscrites (s.d.)." ([vers 1966][84]), scans 2-19, 7 pages
- `123.pdf`: "[Autour de Kostant] : tapuscrits (s.d.), notes manuscrites (s.d.), lettre (1969)." (1969), scans 2-40, 11 pages
- `162-1.pdf`: "Papiers prêtés [liste de noms et de références documentaires] : notes manuscrites (s.d.)." ([à partir de 1967][183]), scans 2-10, 9 pages
- `162-6.pdf`: "[Documents isolés][185] : notes manuscrites (s.d.)." (s.d.), scans 2-6, 5 pages

Two transcriptions of these pages exist already. Both were made by AI models from the same scans, independently of
each other, and neither has been checked against the ink by a person:

- **Witness C (Codex):** a diplomatic LaTeX transcription by GPT-6 Astra at reasoning effort max, in Codex web, one
  session per folder of 4 to 12 scans (13-15 Nov 2026), one file per scan, with its doubts table, inventory, audit
  and short notes. Its notes were written without any context: they list the steps the pages mark as unverified and
  the titles and page counts, and nothing else. For the folder `B15-02` there are two independent runs of the same task; the second is in `codex/B15-02_run2/` (column `codex_file_run2` of `page_map.tsv`): compare both with the ink and with H.
- **Witness H (Hua's):** the transcription of the Commutator project of Michel Hua (github.com/Commutator-IO/
  grothendieck-project, commit `aef7db2`), made by Claude Opus 5 and Claude Opus 5.5 and read again in part by Claude
  Fable 5.2 (efforts not recorded), in that project's own LaTeX macros, one file per batch of about twenty archive
  pages. Their page number n is our scan number n + 1. Witness H has transcribed text for 97 of these
  126 scans; only a description in a note for 1 and nothing for 28 (`page_map.tsv` lists them; those pages are checked against the ink with witness C alone).

Your job has two halves, both required:

1. **One consolidated diplomatic transcription of every page, from the ink,** in our conventions, with a record of
   every place where it differs from witness C or from witness H and of what the scan shows there.
2. **The research notes** that a first transcription of these pages would have written with our earlier work as
   context: his conjectures, questions, unproved claims, unpursued implications, your own ideas, and the links to our
   results, from the context packet attached for this purpose.

Witness C is a careful text: our checks of such returns found about 0.2 errors per 100 words. That is why the pages
are checked here rather than transcribed again, and why the notes are half of this task, not an afterthought.

## The attachments

- `SP14_CW_13+15+26+35+48+66+97+123+162_scans.zip`: for every scan page N three images: `<folder>_<cote>_scanNNN.jpg` (the whole page) and
  `<folder>_<cote>_scanNNN_a.jpg`, `<folder>_<cote>_scanNNN_b.jpg` (its top and bottom halves, or left and right
  halves of a landscape sheet, overlapping a little, at full resolution), where `<folder>` is the Codex folder that
  holds the scan (column `folder` of `page_map.tsv`). N is the page number in the archive's PDF. The images are
  contrast-enhanced and sharpened. The scans of each cote that are not in this package are other tasks: `13.pdf` scans 3, 13, 22, 26, 33, 36, 45; `15.pdf` scans 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60-61, 65-80, 83-135, 137-169, 172-180, 182-187; `97.pdf` scans 5-7, 9, 11-13, 15-18; `123.pdf` scans 4-15, 21, 24-27, 29-39.
- `SP14_CW_13+15+26+35+48+66+97+123+162_witnesses.zip`: `README.md` (start there); `page_map.tsv` (for each scan: the Codex folder, cote, our
  scan, their page, the witness C file, the witness H batch file, whether H has text, only a description, or nothing
  for it, and the context folder that covers it); `codex/<folder>/`, one folder per Codex session (witness C:
  `pages/`, the combined transcription, doubts, inventory, audit, notes, `progress.log`, `PREAMBLE.tex`, which
  defines the macros, and `PROMPT.md`, the task it was given); `codex/B15-02_run2/` (the second run of `B15-02`); `hua/` (witness H: the batch files and
  drawing files of these pages under `transcripts/<cote>/`, their preamble `transcripts/preamble/grothendieck.sty`,
  their `CONTRIBUTING.md` and `RIGHTS.md`).
- `SP14_CW_13+15+26+35+48+66+97+123+162_context.zip`: our earlier work on the neighbouring material, for the research notes. **Leave it closed
  until the transcription is frozen** (method, step 8).

Unzip the first two in your sandbox. **Look at every image yourself**, the whole page first and then the halves for
the small writing, and enlarge (crop and scale) every place you decide. Reading software (OCR, a PDF text layer, any
text-recognition library) is not a substitute for looking and must not be used on these pages.

## The witnesses are drafts, the ink is the authority

**The task is a complete and correct transcription of every page from the ink: every word, symbol, formula, diagram,
drawing, deletion, insertion and marginal note, in the order on the page.** The witnesses tell you where to look; they
never settle a reading.

- **Where C and H differ,** look at the ink and decide. The answer may be C, H, or neither.
- **Where C and H agree,** the reading still has to be seen in the ink before it goes in. Both are AI readings of the
  same scans, and both models put a plausible word where the ink is hard; agreement between them is not evidence.
  Read every agreed word, sign and index against the image as you go.
- **Where only one witness has a passage,** check from the ink whether it is there and what it says; where neither has
  it, transcribe it.
- **What the earlier checks found.** Witness C: about 0.2 errors per 100 words, most of them without a doubt mark: a
  struck word or letter given live or a live one given struck, an insertion attached to the wrong place, a misread
  index or exponent, a word ending read from the grammar, a margin note in fragments; and doubt marks left on readings
  the ink settles. Witness H: about 1.5 errors per 100 words on light pages and 3 to 8 on dense ones; plausible prose
  in place of the ink, sometimes whole clauses; struck text given as live text; abbreviations expanded and spelling
  modernised; margins and slanted notes left out or given in fragments; readable words left as `\ill{}`; drawings
  described in a note instead of drawn. Look for each of these kinds on every page.
- **A doubt mark of witness C** is a place to decide in the ink: resolve it where the ink settles it, keep it where
  it does not, and record either in the changes log.
- **Never fill in from memory, from published texts or from what the mathematics should say.** If the page says
  something surprising, transcribe the surprise. A correction of his text belongs in a research note, never in the
  transcription.

## Our conventions

Use exactly the macros of `codex/<folder>/PREAMBLE.tex` and the rules of `codex/<folder>/PROMPT.md` (they are the same
in every folder): `\cotefile{C}` and `\scanpage{N}`, `\mspage{n}`, `\deleted{…}`, `\inserted{…}`, `\margin{…}`,
`\uline{…}`, `\uuline{…}`, `\diagram{…}` in `tikz-cd`, `\figure{…}` in TikZ, `\unsure{reading}`,
`\unsure{reading|alternative}`, `\illegible{n}`, and the other macros that preamble defines.

1. **Transcribe only what you see,** in his language (mostly French, sometimes English or German). No translation, no
   modernization, no correction: his spelling, accents (or their absence), punctuation, abbreviations ("cat.", "gr.",
   "resp.", "cf.", "th.", "prop.", "dém.", …) and his own numbering exactly as written. Never expand an abbreviation in
   the text.
2. **Mathematics exactly as written**: the same letters, alphabets, indices, exponents, arrows, bars, hats and
   tildes. An exclamation-mark exponent is `^!`, a prime is `'`; read which one the ink shows, every time.
3. **A diagram is typeset, never described**, with every object, arrow, label, direction and decoration, including
   struck parts. **A drawing is reproduced in TikZ, never described**, with its shape, the relative positions of its
   parts and every written label; only a genuine picture too complex for TikZ gets the comment
   `% crop-candidate: scan N` after its best approximation.
4. **Doubt is marked in place, never resolved by a guess,** and a mark of doubt is never a reason to leave something
   out. The first reading in `\unsure{a|b}` is what the ink shows, not the expected form. `\illegible{n}` only for
   ink that is physically unreadable at the highest zoom, never for a symbol inside a formula or a diagram.
5. **Pages that are not his notes** (typescripts, letters by others, printed or typed sheets, lists, covers) are
   transcribed in full all the same, and so is everything he or anyone else wrote on them.
6. His double quotation marks are two backticks and two apostrophes; « » only where he drew guillemets. Keep his
   paragraphing and the order of the text on the page.

## Method

1. Before the first page, write the current time (UTC) as the first line of `progress.log`, and start the notation
   table (step 6).
2. For each scan page, in order: look at the whole image, then both halves. Read witness C's page file and witness H's
   text for that page. Go through the page line by line in the ink, comparing each word, abbreviation, symbol, index,
   sign, inequality, arrow, parenthesis, underline, deletion, insertion and margin note with both witnesses. Enlarge
   every place where they differ, every doubt mark of C, every place where a symbol decides the mathematics, and every
   margin, slanted or struck note, rotated upright.
3. Then make the page inventory: every text block, display, diagram, drawing, margin note, insertion and deletion on
   the page, top to bottom, and check that each one is in the consolidated text, complete. Look specifically for what
   both witnesses missed.
4. **As soon as a page is done:** write its file in `pages/` (named as in witness C), add its rows to the changes
   log, the collation list and the inventory, and append `scan NNN done <current UTC time>` to `progress.log`. Only
   then go to the next page.
5. Read the first page as slowly as the last. The pages done fastest are where errors cluster.
6. **One stream, one notation.** Do the pages yourself, in one stream, in the given order: do not split them among
   parallel workers or sub-agents. Keep one notation table from the first page on: his recurring signs, exponents,
   alphabets, quotation marks and abbreviations, each with how it is written. Witness C was made in separate sessions
   of a few pages each, so the same sign may be written differently from one folder to the next: before the text is
   final, compare how each recurring sign was read across all the pages, check every difference against the ink, and
   make the readings agree. Put the table at the top of the doubts file.
7. **A second reading of every page.** When every page is done, read each page once more against its image, as a
   second reader would; correct, or mark doubt, and append `scan NNN audited <current UTC time>` to `progress.log`.
8. **A frozen transcription, then the context.** Write the SHA-256 of every page file and of the combined
   transcription to `progress.log` with the line `transcription frozen <current UTC time>`. Only then append
   `context opened <current UTC time>`, unzip `SP14_CW_13+15+26+35+48+66+97+123+162_context.zip` and read its `README.md`, and write the research
   notes (below). At the end, check that the hashes are unchanged and say so in `progress.log`.
9. **Checkpoints.** Save a checkpoint ZIP to the user's Library, or wherever files survive the loss of the execution
   environment, once every 45 minutes of work, each under a new name, `SP14_CW_13+15+26+35+48+66+97+123+162_checkpoint_<NN>.zip` with `NN` counting up;
   never overwrite, rename or delete an earlier checkpoint, and put no earlier checkpoint ZIP inside a checkpoint. If
   the workspace comes back empty, restore it from the newest checkpoint and from this conversation before you
   continue. The final ZIP holds everything the checkpoints held. Save checkpoints once every 45 minutes and at no other time:
   none after a page, part, section, cote, folder, chapter or reader. A checkpoint is one ZIP holding every
   deliverable written so far and everything that documents the work (page files, changes log, collation list,
   inventory, doubts, notes, progress log, scripts), so that a new session can continue from it and the files attached
   to this prompt. Leave the attached files themselves out of it, the scans, the witnesses and the context: we have
   them. It is never a JSON file, a recovery file, a summary, or an export of the newest pages only. Each checkpoint zip holds the current deliverables and documentation; earlier checkpoints are not copied into it. The checkpoints
   are what keeps the work if this session dies: work that is in no checkpoint is lost.
10. **If the execution environment fails.** A failed or unavailable environment does not end the task. Retry at
    intervals for as long as this session lasts, without writing recovery text into the chat. When the environment is
    back, restore your work from your newest checkpoint and the earlier checkpoints its file list names, redo what you
    had done after that checkpoint, and continue to the end. Do not write files out in this chat instead: the work
    reaches us only through checkpoint ZIPs and the final ZIP.

This task is long by design: 126 pages, each read in the ink against two witnesses and recorded, then the research
notes. Work through all of it completely; do not stop at a sample or a plan, and do not ask whether to continue.
Ignore any clock. When the last page is frozen, give the notes real time: in earlier work of this kind they found
conjectures, gaps and links that matter.

## The research notes, with our earlier work as context

`SP14_CW_13+15+26+35+48+66+97+123+162_context.zip` holds, for each part of these pages, the context packet that was built for the first-pass
package of the same scans: the packets of 11 first-pass packages (`MPL_13`, `MPL_15_034-086`, `MPL_15_087-138`, `MPL_15_139-194`, `MPL_12_150-168+15_002-033`, `MPL_23_063-099+26`, `MPL_35+48+102+127`, `MPL_66+68_002-032`, `MPL_94+97`, `MPL_123`, `MPL_68_033-056+162-1+162-6`), each file once: `MPL_16+47+54+44_doubts.md`, `MPL_16+47+54+44_notes.md`, `MPL_16+47+54+44_transcription.tex`, `Oda_1969_first_de_Rham_cohomology_Dieudonne_modules.pdf`, `ega_fr/EGA_I_introduction_plan_of_the_treatise.tex`, `ega_fr/EGA_chap0_ega0-12.tex`, `ega_fr/EGA_chap0_ega0-13.tex`, `ega_fr/EGA_chap0_ega0-15.tex`, `ega_fr/EGA_chap0_ega0-16.tex`, `ega_fr/EGA_chap0_ega0-17.tex`, `ega_fr/EGA_chap0_ega0-18.tex`, `ega_fr/EGA_chap0_ega0-19.tex`, `ega_fr/EGA_chap0_ega0-20.tex`, `ega_fr/EGA_chap0_ega0-21.tex`, `ega_fr/EGA_chap0_ega0-22.tex`, `ega_fr/EGA_chap0_ega0-23.tex`, `ega_fr/ega2-indexes-and-contents-fr.tex`, `ega_fr/ega4-backmatter-contents-fr.tex`, `notes/RESULTS_STATE.md`. Its `README.md` says which folder covers which scans.

Use it for the research notes only:
- for each note, search the context for the same objects, notation and words (grep works well on these files), and
  say where our materials already have the point (file and scan) and whether these pages add to it, restate it,
  differ from it or contradict it;
- add notes for links between these pages and the context that he does not make on these pages;
- the notes in the context are leads from earlier runs, not results: never cite one as established.

**Our own results on these subjects: `RESULTS_STATE.md`** (in each context folder's `notes/`, or once at the top of
the zip when every folder has the same one). It lists what our own work has already established on the subjects of
these folders: statements of our research returns, our intake and implication notes, the open items we are pushing,
and the questions of our planning document, each entry with its id, its status and its source file. Read it before
you write the notes. Connect each note to the entries it bears on, by id (for example "bears on LM4 C.12"). Do not
re-derive what an entry already settles: cite it by id and add only what these pages change. Where the manuscript
bears on an open item, record it under that id: the scan and his words, and how the pages bear on it (a proof or its
key step, a counterexample, a different statement of the item, a method, or a sign that he knew the point). A status
there is our runs' claim unless the entry says it was reviewed.

**The transcription does not change after you open the context.** If the context suggests a different reading of
something on these pages, leave the transcription as it is and record a reading question in the notes (scan, line,
your reading, the reading the context suggests, and why).

What the notes cover, for every page:
- **Grothendieck's own conjectures, questions and expectations**: a "?", "il est probable que", "je conjecture", "il
  serait intéressant de", "on devrait pouvoir", a hope or a doubt he writes down;
- **claims stated without proof** or left for later ("on verra", "il est facile de voir", "sans doute", "on peut
  montrer"), and what a proof would need;
- **implications he does not pursue on these pages**: consequences, special cases, links to other parts of mathematics
  or to known results;
- **your own ideas**: what might follow, what might be false, an example or construction worth trying, a link he does
  not make. Label these clearly as yours.

Two standing questions, answered in a short section of their own: **which steps the manuscript itself marks as
unverified** ("à vérifier", "sauf erreur", "je présume", "admis", "il faudrait vérifier", a "?" on a step), each with
its scan and his words; and **which title sheets, dates and page counts it carries** (a title, a "19 pages", a "Pages
1–67" on a sheet or cover), each with its scan. Witness C's notes answer these two questions per folder: check each of
its items against the consolidated text, keep, correct or drop it with the reason, and add what it missed.

One note per item: scan page (and line if you can), kind (conjecture / unproved claim / unpursued implication / own
idea / reading question / self-flagged: a step he himself marks as unverified / withdrawn in the same text: a
statement he corrects or retracts later in these pages, with both scans), the note in one to four sentences, the ids
of `RESULTS_STATE.md` it bears on, and for your own ideas your confidence and your reason. When a note is about
something he wrote, quote his words briefly. He may take a point up later in the file or elsewhere in the archive:
note it anyway, because every note is checked against the rest of the manuscripts and the literature. Do not present
an idea as established or as new. Pages that are typescripts, letters by others or lists get notes on what they
record (who wrote to whom, when, about what, what is asked or promised, what mathematics is stated). The notes never
change the transcription.

**Check events.** For every statement your work checks, uses or refutes (a claim in your notes, by its note; an entry of our results state, by its id; a statement of the text, by its place), record its check events in `CHECK_EVENTS.tsv`, one row per event: statement id, date, who (model, effort, run), type (targeted proof check / independent re-proof / computation or formal certificate / used and rechecked in this run / carried as background without fault found / refuted, with the refined statement's id), outcome. Give each event the type of what actually happened, neither more nor less: reading a statement while transcribing it is not a check of it. `CHECK_EVENTS.tsv` goes into every checkpoint and into the final ZIP.

## What to return

One zip file, `SP14_CW_13+15+26+35+48+66+97+123+162.zip`, offered as the only download. It holds:

1. **The consolidated transcription:** `pages/` with one file per scan, named as in witness C, and
   `SP14_CW_13+15+26+35+48+66+97+123+162_transcription.tex`, all pages in order, one LaTeX fragment (no preamble), using only the macros of
   `PREAMBLE.tex` plus standard LaTeX, `tikz-cd` and TikZ.
2. **`SP14_CW_13+15+26+35+48+66+97+123+162_changes.md`, the changes log, per page:** one section per scan, with one table row for every place where
   the consolidated reading differs from witness C or from witness H: place (line, display, margin), C's reading, H's
   reading, the final reading, what the scan shows (the letters, strokes, lines or marks you saw, with the crop you
   used), and confidence (high, medium, low). Then, per scan, the places still unresolved. At the top: the counts per
   page and in all (changes against C, changes against H, by confidence) and the consequential corrections, those that
   change the mathematics, one per line.
3. **`SP14_CW_13+15+26+35+48+66+97+123+162_collation.tsv`, the collation list,** one row per place where witness H's reading differs from the
   consolidated reading, with the columns `folder, their_page, our_scan, line, their_reading, codex_reading,
   final_reading, scan_shows, kind, marked_in_H, confidence`. `kind` is one of: misread word, misread symbol or index,
   omission, text not on the page, deletion state (struck given live or live given struck), insertion or placement,
   abbreviation expanded or spelling modernised, readable ink left as `\ill{}`, drawing or diagram, other.
   `marked_in_H` says whether H carried a doubt mark there. Differences of macro syntax alone (the same reading in the
   two macro sets) are not rows. Where H has no text for a page, the page has no rows.
4. **`SP14_CW_13+15+26+35+48+66+97+123+162_doubts.md`** (in English, the readings as on the page): the notation table; a table of the remaining
   doubts (scan, line, reading, alternatives, confidence); the abbreviations met, each with what you think it stands
   for (in this list only); and a short honest note on how legible these pages were, which parts you trust least, and
   how the two witnesses compared on them.
5. **`SP14_CW_13+15+26+35+48+66+97+123+162_inventory.csv`** with the columns `scan,sheet_kind,hand,element,kind,position,first_words_or_objects,
   transcribed`: one row per element of every page (kind: text, display, diagram, drawing, margin note, insertion,
   deletion), with `transcribed` = yes for every row. `sheet_kind` is `text` (his notes on the subject of the folder),
   `reused_typed` (a typed page of another text that he wrote on or whose back he used), `typescript`, `letter`,
   `list`, `cancelled_draft` (a draft of his own that he struck through) or `cover`; `hand` says whose hand or machine
   wrote the element (his hand, another named or unnamed hand, typewriter, print).
6. **`SP14_CW_13+15+26+35+48+66+97+123+162_notes.md`:** the research notes, in English, as above, with the two standing questions and the check of
   witness C's notes.
7. `progress.log`.

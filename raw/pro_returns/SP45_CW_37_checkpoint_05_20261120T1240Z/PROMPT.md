# Second pass SP45_CW_37: Alexander Grothendieck's papers, Montpellier archive, cote 37

You are making the second pass over **30 scan pages** from the Montpellier archive of Alexander Grothendieck:
- `37.pdf`: "Rééditions SGA, EGA [SGA 4 à SGA 7, EGA I et EGA II] : tapuscrits et copies de tapuscrit annoté (s.d.), lettres (1967-1971, s.d.), notes manuscrites (s.d.)." (1967-1971), scans 3-68, 30 pages

Two transcriptions of these pages exist already. Both were made by AI models from the same scans, independently of
each other, and neither has been checked against the ink by a person:

- **Witness C (Codex):** a diplomatic LaTeX transcription by GPT-6 Astra at reasoning effort max, in Codex web, one
  session per folder of 4 to 12 scans (13-15 Nov 2026), one file per scan, with its doubts table, inventory, audit
  and short notes. Its notes were written without any context: they list the steps the pages mark as unverified and
  the titles and page counts, and nothing else.
- **Witness H (Hua's):** the transcription of the Commutator project of Michel Hua (github.com/Commutator-IO/
  grothendieck-project, commit `aef7db2`), made by Claude Opus 5 and Claude Opus 5.5 and read again in part by Claude
  Fable 5.2 (efforts not recorded), in that project's own LaTeX macros, one file per batch of about twenty archive
  pages. Their page number n is our scan number n + 1. Witness H has transcribed text for 19 of these
  30 scans; only a description in a note for 11 (`page_map.tsv` lists them; those pages are checked against the ink with witness C alone).

Your job: **one consolidated diplomatic transcription of every page, from the ink,** in our conventions, with a
record of every place where it differs from witness C or from witness H and of what the scan shows there.

**Three readers, one decision.** You work as the main reader with three sub-agents, and every page is read by all
three. Give each sub-agent every page, in order: each reads the page from the scan on its own, line by line, against
witnesses C and H, without seeing the other two readings, and returns its reading of the page and every place where it
differs from either witness, with what it saw in the ink. Then compare the three readings. A place where all three
agree and the ink confirms it is settled. Every place where two readers disagree, or a reader and a witness disagree,
you decide yourself on a crop of that place (step 2 of the method), and you record the decision with the readings it chose between.

**The mathematics while reading.** Each reader follows the mathematics of the page as it reads: a formula that does
not parse, an index that does not match, a sign, inequality or arrow that contradicts the argument is a place to look
at the ink again, and the ink decides, never the expected form. What the page claims and what the mathematics showed
go briefly into the notes (section "Notes while reading"); nothing beyond these pages is researched. Witness C's
notes and doubt table (in its folder in the witnesses zip) list what an earlier reader questioned on each page:
use them to find places to look again, and let the ink decide. Fidelity to the ink comes first throughout.

Witness C is a careful text: our checks of such returns found about 0.2 errors per 100 words. That is why the pages
are checked here rather than transcribed again.

## The attachments

- `SP45_CW_37_scans.zip`: for every scan page N three images: `<folder>_<cote>_scanNNN.jpg` (the whole page) and
  `<folder>_<cote>_scanNNN_a.jpg`, `<folder>_<cote>_scanNNN_b.jpg` (its top and bottom halves, or left and right
  halves of a landscape sheet, overlapping a little, at full resolution), where `<folder>` is the Codex folder that
  holds the scan (column `folder` of `page_map.tsv`). N is the page number in the archive's PDF. The images are
  contrast-enhanced and sharpened. The scans of each cote that are not in this package are other tasks: `37.pdf` scans 6, 8, 14, 17, 19-22, 26, 28-29, 32-33, 36-38, 46-65.
- `SP45_CW_37_witnesses.zip`: `README.md` (start there); `page_map.tsv` (for each scan: the Codex folder, cote, our
  scan, their page, the witness C file, the witness H batch file, whether H has text, only a description, or nothing
  for it, and the context folder that covers it); `codex/<folder>/`, one folder per Codex session (witness C:
  `pages/`, the combined transcription, doubts, inventory, audit, notes, `progress.log`, `PREAMBLE.tex`, which
  defines the macros, and `PROMPT.md`, the task it was given); `hua/` (witness H: the batch files and
  drawing files of these pages under `transcripts/<cote>/`, their preamble `transcripts/preamble/grothendieck.sty`,
  their `CONTRIBUTING.md` and `RIGHTS.md`).

Unzip them in your sandbox. **Look at the images yourself.** Reading software (OCR, a PDF text layer, any
text-recognition library) is not a substitute for looking and must not be used on these pages. How to look is the
reading workflow of the method (step 2): the page and its two halves once each, then one crop for each place they
leave open.

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
2. **The reading workflow, for each scan page in order.** Give each page to three fresh sub-agents. Each starts with
   only this page's images, witness C's and witness H's texts for it, our conventions and your notation table so far;
   it does a to d on its own, returns, and is then done. The next page gets three new sub-agents, so that no reader
   carries earlier pages' images: an image kept in a reader's context is read again at every later step. You, the main
   reader, keep only their returns and the crops of the places you decide, and do e.
   **The readers' brief.** Before the first page, write the brief each reader receives with its page: steps a to d,
   our conventions and the notation table so far. After each page, look at where the three readings differed and why.
   Where a difference came from the brief (a convention a reader did not know, a kind of mark it misread, a crop it
   made that the halves had settled, a place it left uncropped that needed one), improve the brief for the next page's
   readers. Keep each version of the brief with the page it was first used on.
   a. Look at the whole image once, for the layout: the text blocks, displays, diagrams, drawings, margins,
      insertions and deletions, and where each sits.
   b. Read the two halves once each, line by line, with witness C's page file and witness H's text for that page
      beside them. Compare each word, abbreviation, symbol, index, sign, inequality, arrow, parenthesis, underline,
      deletion, insertion and margin note with both witnesses, and settle from the halves everything they settle.
      The halves are at full resolution: enlarging a whole half again shows nothing new.
   c. List the places the halves leave open: a reading that still differs from a witness, a doubt mark of C, a small
      symbol or index that decides the mathematics, a slanted, struck or crowded note. Crop each of them once, tightly
      (the word or formula and a line around it), and zoom in deep: scale the crop up to a few thousand pixels across
      (LANCZOS) until every stroke is plain, raise its contrast (autocontrast, and sharpen where the ink is faint),
      and rotate it upright where slanted. One crop settles one place: do not crop what the halves have settled, and
      do not crop a decided place again.
   d. Return the reading of the page and the list of places where it differs from either witness, each with what
      the half or the crop showed.
   e. Compare the three readings. A place where all three agree, and the halves show it, is settled. For each place
      where they differ, look at the crops the readers made of it, or make one crop of it yourself if none did, and
      decide.
3. Then make the page inventory: every text block, display, diagram, drawing, margin note, insertion and deletion on
   the page, top to bottom, and check that each one is in the consolidated text, complete. Look specifically for what
   both witnesses missed.
4. **As soon as a page is decided** (its three readings compared and every disagreement settled on the scan): write its file in `pages/` (named as in witness C), add its rows to the changes
   log, the collation list and the inventory, and append `scan NNN done <current UTC time>` to `progress.log`. Only
   then go to the next page.
5. Read the first page as slowly as the last. The pages done fastest are where errors cluster.
6. **One notation.** The pages are read in the given order, each by all three readers; never split the pages among
   readers. Keep one notation table from the first page on: his recurring signs, exponents,
   alphabets, quotation marks and abbreviations, each with how it is written. Witness C was made in separate sessions
   of a few pages each, so the same sign may be written differently from one folder to the next: before the text is
   final, compare how each recurring sign was read across all the pages, check every difference against the ink, and
   make the readings agree. Put the table at the top of the doubts file.
7. **The three readings in the record.** In the changes log, a place where the readers differed lists all
   three readings and the one the ink supports, with what the scan shows.
8. **A frozen transcription.** When every page is decided, write the SHA-256 of every page file and of the
   combined transcription to `progress.log` with the line `transcription frozen <current UTC time>`. At the
   end, check that the hashes are unchanged and say so in `progress.log`.
9. **Checkpoints.** Save a checkpoint ZIP to the user's Library, or wherever files survive the loss of the execution
   environment, once every 45 minutes of work, each under a new name, `SP45_CW_37_checkpoint_<NN>.zip` with `NN` counting up;
   never overwrite, rename or delete an earlier checkpoint, and put no earlier checkpoint ZIP inside a checkpoint. If
   the workspace comes back empty, restore it from the newest checkpoint and from this conversation before you
   continue. The final ZIP holds everything the checkpoints held. Save checkpoints once every 45 minutes and at no other time: none after a page, part, section, cote, folder, chapter or reader. A checkpoint is one ZIP holding every
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


This task is long by design: 30 pages, each read three times in the ink against two witnesses, decided and recorded.
Work through all of it completely; do not stop at a sample or a plan, and do not ask whether to continue.
Ignore any clock.

## Notes while reading

`SP45_CW_37_notes.md`, in English, per page, briefly: what the page states, computes or asks; every place where the
mathematics led to a reading decision (scan, line, the readings, why); his own slips, checks and doubts ("à vérifier",
"sauf erreur", "je présume", a "?" on a step), each with his words; and the title sheets, dates and page counts the
pages carry, each with its scan. Pages that are typescripts, letters by others or lists get a line on what they
record. Nothing beyond these pages is researched, and the notes never change the transcription.

**Check events.** For every statement your work checks, uses or refutes (a claim in your notes, by its note; a statement of the text, by its place), record its check events in
`CHECK_EVENTS.tsv`, one row per event: statement id, date, who (model, effort, run), type (targeted proof check /
independent re-proof / computation or formal certificate / used and rechecked in this run / carried as background
without fault found / refuted, with the refined statement's id), outcome. Give each event the type of what actually
happened, neither more nor less: reading a statement while transcribing it is not a check of it. `CHECK_EVENTS.tsv`
goes into every checkpoint and into the final ZIP.

## What to return

One zip file, `SP45_CW_37.zip`, offered as the only download. It holds:

1. **The consolidated transcription:** `pages/` with one file per scan, named as in witness C, and
   `SP45_CW_37_transcription.tex`, all pages in order, one LaTeX fragment (no preamble), using only the macros of
   `PREAMBLE.tex` plus standard LaTeX, `tikz-cd` and TikZ.
2. **`SP45_CW_37_changes.md`, the changes log, per page:** one section per scan, with one table row for every place where
   the consolidated reading differs from witness C or from witness H: place (line, display, margin), C's reading, H's
   reading, the final reading, what the scan shows (the letters, strokes, lines or marks you saw, with the crop you
   used), and confidence (high, medium, low). Then, per scan, the places still unresolved. At the top: the counts per
   page and in all (changes against C, changes against H, by confidence) and the consequential corrections, those that
   change the mathematics, one per line.
3. **`SP45_CW_37_collation.tsv`, the collation list,** one row per place where witness H's reading differs from the
   consolidated reading, with the columns `folder, their_page, our_scan, line, their_reading, codex_reading,
   final_reading, scan_shows, kind, marked_in_H, confidence`. `kind` is one of: misread word, misread symbol or index,
   omission, text not on the page, deletion state (struck given live or live given struck), insertion or placement,
   abbreviation expanded or spelling modernised, readable ink left as `\ill{}`, drawing or diagram, other.
   `marked_in_H` says whether H carried a doubt mark there. Differences of macro syntax alone (the same reading in the
   two macro sets) are not rows. Where H has no text for a page, the page has no rows.
4. **`SP45_CW_37_doubts.md`** (in English, the readings as on the page): the notation table; a table of the remaining
   doubts (scan, line, reading, alternatives, confidence); the abbreviations met, each with what you think it stands
   for (in this list only); and a short honest note on how legible these pages were, which parts you trust least, and
   how the two witnesses compared on them.
5. **`SP45_CW_37_inventory.csv`** with the columns `scan,sheet_kind,hand,element,kind,position,first_words_or_objects,
   transcribed`: one row per element of every page (kind: text, display, diagram, drawing, margin note, insertion,
   deletion), with `transcribed` = yes for every row. `sheet_kind` is `text` (his notes on the subject of the folder),
   `reused_typed` (a typed page of another text that he wrote on or whose back he used), `typescript`, `letter`,
   `list`, `cancelled_draft` (a draft of his own that he struck through) or `cover`; `hand` says whose hand or machine
   wrote the element (his hand, another named or unnamed hand, typewriter, print).
6. **`SP45_CW_37_notes.md`:** the notes made while reading (above).
7. `progress.log`.
8. **`SP45_CW_37_workflow.md`:** how you ran the readers, for our next runs: the readers' brief as first written and
   as last used, each change between them with the page and the disagreements that led to it, the number of crops per
   page, and what in the workflow worked and what did not.

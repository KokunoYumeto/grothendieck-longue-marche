**The attached files.** Besides this file there is one ZIP, `IM02_6-9.zip`. Unpack it once: it holds every file named below. The folders named below are already unpacked inside it, so there is nothing more to unpack; every other file is at the top level under its own name.

# Putting decided corrections into the transcription, IM02_6-9: Alexander Grothendieck's papers, Montpellier archive

You are putting **92 corrections** into **58 pages** of our diplomatic LaTeX transcription of the Montpellier archive
of Alexander Grothendieck (cotes 6, 7, 8, 9). Every correction was found by an earlier reader: a sweep through the archive
by readers of Claude Opus 5.5 at effort max, a second pass (GPT-6 Astra, ChatGPT Pro mode), Michel Hua's checks on the
facsimile (read by a person), or a second model (Claude Opus 5.5 at effort high) that looked again at hard places. They
are listed in `IM02_6-9_corrections.tsv`, most of them in plain notation, not in the page's LaTeX. Your job: decide every row
and put every correction that is a correction of our reading into its page, exactly, and nothing else.

**Three sub-agents on different pages.** Pro gives you three sub-agents: use all three at once, each on a page of its
own. Give each sub-agent one page at a time, in the given order (the next page goes to the first sub-agent that is
free), with only that page's LaTeX, its scan, its rows of the corrections table, our conventions and the decisions
below. It returns, for each row, its decision, the exact edit and what the ink showed. You, the main reader, check each
return, decide every row it left open, and write the page.

## The attachments

- `IM02_6-9_pages/`: our transcription of each page as it stands now, `<cote>_scanNNN.tex`, in the macros of `PREAMBLE.tex`.
- `IM02_6-9_scans/`: the scan of each page, `<cote>_scanNNN.jpg`, at the resolution of the archive's PDF, with its contrast
  raised and sharpened. Crop and enlarge it yourself where a row needs the ink: one tight crop for each place, scaled up
  to a few thousand pixels across, with its contrast raised.
- `IM02_6-9_corrections.tsv`: one row per correction, with the columns `id`, `cote`, `scan`, `kind`, `source`,
  `as_the_page_reads` (what the earlier reader saw in our text), `should_read` (the correction), `evidence` and
  `checked_on_scan` (yes when the earlier reader decided it on the scan).
- `PREAMBLE.tex`: the macros of the transcription.

Look at the images yourself. Reading software (OCR, a PDF text layer, any text-recognition library) is not a substitute
for looking and must not be used.

## The decision for each row

- **(a) Our misreading.** Our text does not show what the ink shows, and the row gives what it shows: change the page to
  the ink, in the page's own macros.
- **(b) His own slip, or a refinement of his mathematics.** The ink is as our text has it, and the row says what he
  meant: the transcription stays as written, and the row goes in the notes with what he meant.
- **(c) Already as the row asks:** no change.
- **(d) Not on this page:** no change; say where it is, if you see it.
- **Rows you decide on the ink.** Every row with `checked_on_scan` = no, every row whose kind is a flag, open, not
  sorted, or from the second model, and every row where the row and our text disagree on what is written: look at the
  ink and decide (a) to (d) from what you see. Where the ink does not settle it, put a doubt mark in place
  (`\unsure{reading|alternative}`), never a guess.
- **Michel Hua's checks** were read by a person on the facsimile: apply them, unless the ink plainly shows something
  else, and then say so with what it shows.

Change nothing else on a page: no other correction, no normalisation, no reformatting. The transcription is diplomatic:
his spelling, accents, abbreviations, notation and slips stay as written; diagrams stay typeset in `tikz-cd`; a struck
word is `\deleted{…}`, an insertion `\inserted{…}`, a margin note `\margin{…}`, a doubt `\unsure{…}`, illegible ink
`\illegible{n}`, as in the macros of `PREAMBLE.tex`. The paper's watermark (« EXTRA STRONG ») and specks of the paper
are not ink and are never transcribed.

## Method

1. Before the first page, write the current time (UTC) as the first line of `progress.log`.
2. For each page (the sub-agent that has it): find the place of each of its rows in the page's LaTeX; decide (a) to (d),
   looking at the ink where the rows above ask for it; make the edit; and record the row.
3. You check each returned page: every edit changes only its row's place, and the span it replaces stands once on the
   page as given; decide every row the sub-agent left open.
4. As soon as a page is done: write it to `edited_pages/` (named as given), add its rows to `placements.tsv`, and append
   `scan NNN done <current UTC time> cote <cote>` to `progress.log`. Only then is the page finished.
5. **Checkpoints.** Save a checkpoint ZIP to the user's Library, or wherever files survive the loss of the execution
   environment, once every 45 minutes of work, each under a new name, `IM02_6-9_checkpoint_<NN>.zip` with `NN` counting up;
   never overwrite, rename or delete an earlier checkpoint, and put no earlier checkpoint ZIP inside a checkpoint. If the
   workspace comes back empty, restore it from the newest checkpoint and from this conversation before you continue.
   The final ZIP holds everything the checkpoints held. Save checkpoints once every 45 minutes and at no other time:
   none after a page, part, section, cote, folder, chapter or reader. A checkpoint is one ZIP holding every deliverable
   written so far and everything that documents the work (`placements.tsv`, `edited_pages/`, the notes, the crops in
   `crops/`, `CHECK_EVENTS.tsv`, `progress.log`, scripts), so that a new session can continue from it and the files
   attached to this prompt. Leave the attached files themselves out of it: we have them. It is never a JSON file, a
   recovery file, a summary, or an export of the newest pages only. Each checkpoint zip holds the current deliverables
   and documentation; earlier checkpoints are not copied into it. The checkpoints are what keeps the work if this
   session dies: work that is in no checkpoint is lost.
6. **If the execution environment fails.** A failed or unavailable environment does not end the task. Retry at
   intervals for as long as this session lasts, without writing recovery text into the chat. When the environment is
   back, restore your work from your newest checkpoint and the earlier checkpoints its file list names, redo what you
   had done after that checkpoint, and continue to the end. Do not write files out in this chat instead: the work
   reaches us only through checkpoint ZIPs and the final ZIP.

This task is long by design: 92 rows on 58 pages, each decided and, where it is a correction of our reading, put into
its page exactly. Work through all of it completely; do not stop at a sample or a plan, and do not ask whether to
continue. Ignore any clock.

**Check events.** For every statement your work checks, uses or refutes (here a statement is a row of the corrections
table, by its id), record its check events in `CHECK_EVENTS.tsv`, one row per event: statement id, date, who (model,
effort, run), type (targeted proof check / independent re-proof / computation or formal certificate / used and
rechecked in this run / carried as background without fault found / refuted, with the refined statement's id),
outcome. Give each event the type of what actually happened, neither more nor less: reading a row is not a check of it.
`CHECK_EVENTS.tsv` goes into every checkpoint and into the final ZIP.

## What to return

One zip file, `IM02_6-9.zip`, offered as the only download. It holds:

1. **`placements.tsv`**, one row per row of the corrections table, in its order, with the columns `id`, `cote`, `scan`,
   `decision` (a, b, c or d), `find` (for a: the exact span of the page as given, long enough to stand once on it),
   `replace` (for a: the same span corrected; empty for b, c and d), `what_the_ink_shows` (for every row decided on the
   scan: the strokes you saw, with the crop), and `confidence` (high, medium, low).
2. **`edited_pages/`**: every page of this piece after its edits, named as given.
3. **`notes.md`**: every (b) row with its id, what is written and what he meant; every (d) row with where its place is,
   if you saw it; and a short note on the rows the ink did not settle.
4. **`crops/`**, **`CHECK_EVENTS.tsv`** and **`progress.log`**.

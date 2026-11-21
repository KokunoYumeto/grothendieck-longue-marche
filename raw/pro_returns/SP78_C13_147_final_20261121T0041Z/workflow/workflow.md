## Method

1. Before the first page, write the current time (UTC) as the first line of `progress.log`, and start the notation
   table (step 6).
2. **The reading workflow, for each scan page: a to d by the sub-agent that has the page, e by you.**
   a. Look at the whole image once, for the layout: the text blocks, displays, diagrams, drawings, margins,
      insertions and deletions, and where each sits.
   b. Read the two halves once each, line by line, with witness C's page file and witness H's text for that page
      beside them. Compare each word, abbreviation, symbol, index, sign, inequality, arrow, parenthesis, underline,
      deletion, insertion and margin note with both witnesses, and settle from the halves everything they settle, except the places that always get a crop (c).
      The halves are at full resolution: enlarging a whole half again shows nothing new.
      Then go once through every `\deleted` and every `\inserted` of witness C on this page and answer for
      each from the image: does the stroke cross these letters and only these, and where does the insertion's stroke
      end. A strike or an insertion the halves do not show plainly is a place for c.
   c. List the places the halves leave open: a reading that still differs from a witness, a doubt mark of C, a
      small symbol or index that decides the mathematics, a slanted, struck or crowded note, and every place of a kind
      in the error sheet that the halves do not settle. Some places always get a crop, whatever the halves show: every
      place where C and H read different words, and every doubt mark of C that you would resolve. Crop each of them once, tightly (the word or formula and a line
      around it), and zoom in deep: scale the crop up to a few thousand pixels across (LANCZOS) until every stroke is
      plain, raise its contrast (autocontrast, and sharpen where the ink is faint), and rotate it upright where
      slanted. One crop settles one place: do not crop what the halves have settled, and do not crop a decided place
      again. Save each crop in `crops/`, named by its scan and place, and record it in the changes log by that file name and its
      box in the original image's pixels (x0, y0, x1, y1).
   d. Decide each open place on its crop, and return the reading of the page with every place where it differs from
      either witness and what the half or the crop showed.
   e. You check the return: look at the crop of every place the sub-agent left open or that disagrees with a witness,
      or make one crop of it yourself, decide, and record the decision with the readings it chose between.
3. Then make the page inventory: every text block, display, diagram, drawing, margin note, insertion and deletion on
   the page, top to bottom, and check that each one is in the consolidated text, complete. Look specifically for what
   both witnesses missed.
4. **As soon as a page is done** (every open place decided on the scan): write its file in `pages/` (named as in
   witness C), add its rows to the changes log, the collation list, the inventory and `decisions.tsv`, and append
   `scan NNN done <current UTC time> cote <cote>: L lines read, P places cropped, R rows` to `progress.log` (the lines of the page, the places cropped on it, the rows it added
   to the changes log). Only then go to the next page.
5. Read the first page as slowly as the last. The pages done fastest are where errors cluster.
6. **One notation.** The pages go to the sub-agents in the given order. You keep the one notation table and give its
   current state to each sub-agent with each page. Keep one notation table from the first page on: his recurring signs, exponents,
   alphabets, quotation marks and abbreviations, each with how it is written. Before the text is final, compare how each
   recurring sign was read across all the pages, check every difference against the ink, and make the readings agree.
   Put the table at the top of the doubts file.
7. **A second reading, written down before it is compared.** When every page is done, each page goes to a sub-agent
   that has not read it, for its hardest places. First write the page's box list, `second/<page>_boxes.tsv` (`<page>`
   is the page file's name without `.tex`; columns `box`, `kind`, `x0`, `y0`, `x1`, `y1`, in the original image's
   pixels), with a box for every insertion, every margin note, every struck passage, every formula in which witness C
   or your page has a doubt mark (the whole formula), every number written by pen, every word written by hand on a
   typescript, every place where C and H read different words, and every place where your page departs from witness C
   with less than high confidence; and write your page's reading of each box, in our conventions, to
   `second/<page>_first.tsv` (columns `box`, `reading`). The sub-agent gets the page's images and the box list, and
   nothing else: not your page file, not `_first.tsv`, not witness C, not witness H, not your notes. It crops each box,
   reads it from the ink and writes its reading, in our conventions, to `second/<page>_second.tsv` (columns `box`,
   `reading`). Then compare the two readings of each box by script, token by token; decide every difference on a crop
   of that place, correct or mark doubt, and enter every changed place in the changes log with both readings. For each
   page append `scan NNN audited <current UTC time>: B boxes read, D differences, K changed` to `progress.log`.
8. **A frozen transcription.** When every page is decided, write the SHA-256 of every page file and of the
   combined transcription to `progress.log` with the line `transcription frozen <current UTC time>`. At the
   end, check that the hashes are unchanged and say so in `progress.log`.
9. **Checkpoints.** Save a checkpoint ZIP to the user's Library, or wherever files survive the loss of the execution
   environment, once every 45 minutes of work, each under a new name, `SP78_C13_147_checkpoint_<NN>.zip` with `NN` counting up;
   never overwrite, rename or delete an earlier checkpoint, and put no earlier checkpoint ZIP inside a checkpoint. If
   the workspace comes back empty, restore it from the newest checkpoint and from this conversation before you
   continue. The final ZIP holds everything the checkpoints held. Save checkpoints once every 45 minutes and at no
   other time: none after a page, part, section, cote, folder, chapter or reader. A checkpoint is one ZIP holding every
   deliverable written so far and everything that documents the work (page files, changes log, collation list,
   inventory, decisions, doubts, notes, hand log, crops, progress log, the second readings in `second/`, scripts), so that a new session can continue from it and
   the files attached to this prompt. Leave the attached files themselves out of it, the scans and the texts: we have
   them. The crops in `crops/` go into every checkpoint and the final ZIP; the halves you made do not (we can make them
   again). It is never a JSON file, a
   recovery file, a summary, or an export of the newest pages only. Each checkpoint zip holds the current deliverables
   and documentation; earlier checkpoints are not copied into it. The checkpoints are what keeps the work if this
   session dies: work that is in no checkpoint is lost.
10. **If the execution environment fails.** A failed or unavailable environment does not end the task. Retry at
    intervals for as long as this session lasts, without writing recovery text into the chat. When the environment is
    back, restore your work from your newest checkpoint and the earlier checkpoints its file list names, redo what you
    had done after that checkpoint, and continue to the end. Do not write files out in this chat instead: the work
    reaches us only through checkpoint ZIPs and the final ZIP.

This task is long by design: 24 pages, each read in the ink against two witnesses, read a second time, decided and
recorded. Work through all of it completely; do not stop at a sample or a plan, and do not ask whether to continue.
Ignore any clock.

## Notes while reading

`SP78_C13_147_notes.md`, in English, per page, briefly: what the page states, computes or asks; every place where the
mathematics led to a reading decision (scan, line, the readings, why), with the reading the mathematics or his notation
forces beside the one the ink shows where the two differ; his own slips, checks and doubts ("à vérifier", "sauf
erreur", "je présume", a "?" on a step), each with his words; and the title sheets, dates and page counts the pages
carry, each with its scan. Pages that are typescripts, letters by others or lists get a line on what they record.
Nothing beyond these pages is researched, and the notes never change the transcription.

**Check events.** For every statement your work checks, uses or refutes (a claim in your notes, by its note; a statement of the text, by its place), record its check events in
`CHECK_EVENTS.tsv`, one row per event: statement id, date, who (model, effort, run), type (targeted proof check /
independent re-proof / computation or formal certificate / used and rechecked in this run / carried as background
without fault found / refuted, with the refined statement's id), outcome. Give each event the type of what actually
happened, neither more nor less: reading a statement while transcribing it is not a check of it. `CHECK_EVENTS.tsv`
goes into every checkpoint and into the final ZIP.

## What to return

One zip file, `SP78_C13_147.zip`, offered as the only download. It holds:

1. **The consolidated transcription:** `pages/` with one file per scan, named as in witness C, and
   `SP78_C13_147_transcription.tex`, all pages in order, one LaTeX fragment (no preamble), using only the macros of
   `PREAMBLE.tex` plus standard LaTeX, `tikz-cd` and TikZ.
2. **`SP78_C13_147_changes.md`, the changes log, per page:** one section per scan, with one table row for every place where
   the consolidated reading differs from witness C or from witness H: place (line, display, margin), C's reading, H's
   reading, the final reading, what the scan shows (the letters, strokes, lines or marks you saw, with the crop you used, by its file name and pixel box), and confidence (high, medium, low). Then, per scan, the places still unresolved.
   At the top: the counts per page and in all (changes against C, changes against H, by confidence) and the
   consequential corrections, those that change the mathematics, one per line.
3. **`SP78_C13_147_collation.tsv`, the collation list,** one row per place where witness H's reading differs from the
   consolidated reading, with the columns `folder, their_page, our_scan, line, their_reading, codex_reading,
   final_reading, scan_shows, kind, marked_in_H, confidence` (`folder` is the cote, `codex_reading` is witness C's
   reading). `kind` is one of: misread word, misread symbol or index, omission, text not on the page, deletion state
   (struck given live or live given struck), insertion or placement, abbreviation expanded or spelling modernised,
   readable ink left as `\ill{}`, drawing or diagram, other. `marked_in_H` says whether H carried a doubt mark there.
   Differences of macro syntax alone (the same reading in the two macro sets) are not rows. Where H has no text for a
   page, the page has no rows.
4. **`decisions.tsv`**, one row per mark of `MARKS.tsv`, in its order, with the columns `id`, `cote`, `scan`,
   `decision` (`first` = the first reading of the mark; `alternative` = another of its listed readings; `other` =
   another reading; `undecided` = the ink does not settle it), `reading` (as it stands in the consolidated text),
   `what the ink shows`, `crop` (scan and pixel box, or `page` for a mark that stays undecided; a mark you resolve has its crop) and `confidence`.
5. **`SP78_C13_147_doubts.md`** (in English, the readings as on the page): the notation table; a table of the remaining
   doubts (scan, line, reading, alternatives, confidence); the abbreviations met, each with what you think it stands
   for (in this list only); and a short honest note on how legible these pages were, which parts you trust least, and
   how the two witnesses compared on them.
6. **`SP78_C13_147_inventory.csv`** with the columns `scan,sheet_kind,hand,element,kind,position,first_words_or_objects,
   transcribed`: one row per element of every page (kind: text, display, diagram, drawing, margin note, insertion,
   deletion), with `transcribed` = yes for every row. `sheet_kind` is `text` (his notes on the subject of the folder),
   `reused_typed` (a typed page of another text that he wrote on or whose back he used), `typescript`, `letter`,
   `list`, `cancelled_draft` (a draft of his own that he struck through) or `cover`; `hand` says whose hand or machine
   wrote the element (his hand, another named or unnamed hand, typewriter, print).
7. **`SP78_C13_147_notes.md`:** the notes made while reading (above), and `CHECK_EVENTS.tsv`.
8. `progress.log`, and `second/`: for every page its box list, your readings of the boxes and the second
   reading (method, step 7).
9. **`SP78_C13_147_sheet_feedback.md`:** for our next runs: for each kind in the error sheet, how many places on these pages
   were of that kind, and every recurring error you met that the sheet does not name, with its places; and
   **`SP78_C13_147_hand_log.md`**, the hand log (the error sheet's last section).

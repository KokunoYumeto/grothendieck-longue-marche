**The attached files.** Besides this file there is one ZIP, `SP71_C13_142.zip`. Unpack it once: it holds every file named below. Each ZIP named below is already unpacked inside, as a folder of the same name without `.zip` (for example `SP71_C13_142_scans.zip` is the folder `SP71_C13_142_scans/`), so there is nothing more to unpack; every other file is at the top level under its own name.

# Second pass SP71_C13_142: Alexander Grothendieck's papers, Montpellier archive

You are making the second pass over **24 scan pages** of the Montpellier archive of Alexander Grothendieck (cote 142: "Action de Galois sur Teichmüller[147] : notes manuscrites (s.d.).").

Two transcriptions of these pages exist already, both made by AI models from the same scans, and neither has been
checked against the ink by a person:

- **Witness C (ours):** a diplomatic LaTeX transcription, made by GPT-6 Astra (ChatGPT Pro mode) and checked by Claude
  Opus 5.5 at effort max on 13 Nov 2026, one file per scan, with its doubt marks (`\unsure{...}`, `\illegible{n}`).
- **Witness H (Hua's):** the transcription of the Commutator project of Michel Hua (github.com/Commutator-IO/
  grothendieck-project), made with Claude models, in that project's own LaTeX macros, for 23 of these 24 pages.

Your job: **one consolidated diplomatic transcription of every page, from the ink,** in our conventions, with a
record of every place where it differs from witness C or from witness H and of what the scan shows there.

**One reader, every page, then a second reading.** You read every page yourself, in one stream, in the given order,
line by line from the scan against witnesses C and H, and decide every place on the ink; when every page is done, you
read each page a second time against its image (method, step 7). Before the first page, read the section "The errors
that recur in these papers": it lists the kinds of error earlier passes found most often in these papers, and you look
for each of them on every page.

**The mathematics while reading.** Follow the mathematics of the page as you read: a formula that does not parse, an
index that does not match, a sign, inequality or arrow that contradicts the argument is a place to look at the ink
again, and the ink decides, never the expected form. What the page claims and what the mathematics showed go briefly
into the notes (section "Notes while reading"); nothing beyond these pages is researched. Fidelity to the ink comes
first throughout.

Witness C is a careful text, which is why the pages are checked here rather than transcribed again. It is not a final
one: earlier second passes of this archive changed the first readings at about 11 places a page, two thirds of them at
places not marked as doubtful.

## The attachments

- `SP71_C13_142_scans.zip`: one image per page, `<cote>_scanNNN.jpg`, the scan as the archive's PDF holds it (its native
  resolution, about 1680x2152 pixels), contrast-enhanced and sharpened. Before reading a page, make its two halves
  once, at full resolution, with Pillow: top and bottom, overlapping by about a tenth (left and right for a landscape
  sheet).
- `SP71_C13_142_texts.zip`:
  - `pages/<cote>_scanNNN.tex`: witness C, the transcription of each page as it stands now, with its marks;
  - `MARKS.tsv`: the doubt marks of witness C in live text, in page order, each with its id (`M0001` ...), its cote and
    scan, its kind, the mark as written and the LaTeX around it: known places to decide, among all the others;
  - `hua/hua_<cote>_scanNNN.tex`: witness H for the pages where his project has one;
  - `PREAMBLE.tex`: the macros of the transcription.

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
- **What the earlier checks found** is the next section, the error sheet: read it before the first page.
- **A doubt mark of witness C** (in live or in struck-out text) is a place to decide in the ink: resolve it where the
  ink settles it, keep it, narrowed to what the ink allows, where it does not, and record either.
- **Never fill in from memory, from published texts or from what the mathematics should say.** If the page says
  something surprising, transcribe the surprise. A correction of his text belongs in a note, never in the
  transcription.

## The errors that recur in these papers: read this before the first page

Where these come from: the 6,439 places where earlier second passes of this archive (ChatGPT Pro, GPT-6 Astra, 23 runs,
470 pages) changed witness C's reading, sorted by the passes' own kinds, and the places Michel Hua checked by eye on the
facsimile against witness H. Two thirds of those changes (3,211 of the 5,032 that changed the text) were at places
witness C had not marked as doubtful: look for these kinds everywhere, not only at its doubt marks. The counts say where
the errors were; they never decide a reading. The ink decides.

**Where witness C was wrong, most often first (places on those 470 pages):**

1. **Symbols and indices (1,075).**
   - Letters with a hook or a tail: ξ and ζ, γ and Γ, ρ and p, δ and λ, Λ and A, Δ and 2. Fix the letter where the page
     or the run defines it, then read every occurrence the same way: on cote 12 one definition settled 27 places.
   - Small digits, primes and exponents: a prime dropped or added; 1 and 2, 0 and 1, 1 and I, l and 1. Read them by the
     degree, count or date the page forces, and never regularise one silently.
   - Worn signs: a short stroke between two terms may be a map, a minus or a plus; two ticks or a ∩ between the rows of
     a diagram may be = or ⊂. Read them by the formula and the rows of the diagram, then confirm on the ink.
   - Pairs he writes one for the other (i and j, m and n, X and Y, K and k, V and W): keep the letter as written, even
     where the argument needs the other; the meant one goes in the notes.
   - Letters his hand forms alike are a different case from such slips. Where his p looks like an n, or his ζ like a
     ξ, the ink alone does not decide: his notation on these pages and the mathematics decide which letter it is, and
     the habit goes into the hand log (last section). A slip is a clear letter that is wrong, and it stays.
2. **Words (1,032).**
   - His coined terms read as familiar words of the same outline (« préfigure » as « polygone », « strates » as
     « structures »): where a strange word recurs, check it where he defines it.
   - His own spellings, his English words and his accents stay as written: the earlier readings normalised 4 of the 6
     places checked (« because » given as « avec », « systématiques » as « systématique »).
   - Endings (a final s, de and des, le and les): the grammar does not decide them; he breaks agreement himself (2 of
     the 6 endings checked by eye).
3. **Omissions (1,009).**
   - A one-word insertion (la, le, de, un, et, des, ne, même) is the hardest word on the page: of 10 checked by eye,
     witness C had another word in 5.
   - Prefixes are written above the line (sous-, quasi-, ⊗-, Δ-, pseudo-, contra-): 28 of the 30 checked by eye are on
     the page. Look above the line before taking a prefix as absent.
   - Margin notes, slanted notes, the punctuation that survives a cancellation.
4. **Drawings and diagrams (886).** What looks like a drawing may be a crossing-out, a hatched formula, a matrix or a
   diagram to set (17 such cases checked by eye). In a real figure, count the sides, points and strokes twice.
5. **Readable ink left as illegible (711).** The full-resolution halves, or one tight crop, usually read it.
6. **Insertions put in the wrong place (500).** Decide where an insertion attaches (which word, line, item, margin or
   leaf) separately from what it says.
7. **Struck text (417).** Three separate questions: which words are struck, whether the line is a strike at all, and
   which words replace them. A struck word given as live, or a live one given as struck, is witness C's commonest silent
   error.
8. **Abbreviations expanded, spelling modernised (389).** His short forms stay in the text: tt, ess., t.f., il f. et il
   s., tot^t, néc^t, ss-, ½, and = standing for « même ». An expansion goes only in the abbreviations list.
9. **Text that is not on the page (128).** A word the sentence needs is either an insertion that was missed or not on
   the page. If it is not on the page, it is not transcribed, not even as a doubtful reading; it goes in the notes.
10. **Other (292).**

**Witness H.** Its page n is our scan n + 1. Its editorial page markers, synopses and notes are not source text; its
`\emph` may stand for an underline; its drawings are in separate drawing files. Witness C and witness H can agree on
the same wrong reading (« ab » for « k »; a « c » that is not on the page), so their agreement is not evidence.

**The sheet.** On a typescript, a blank the machine left for a symbol stays a blank unless it was inked. Settle first
whether a sheet is turned or upside down, and how it joins the next leaf; a sentence need not continue on the next scan.

**How a place is decided.** Nothing is normalised: his spelling, his notation and his slips are transcribed as written.
- Where the ink is clear, it stands, even where the argument needs another letter; the meant one goes in the notes.
- Where the ink admits two readings, his notation on these pages and the mathematics decide between them, and one
  decision settles every occurrence of the same notation.
- His short forms come from his own list (item 8).

The mathematics shows where to look again; it never puts on the page what is not there: a « sous- » the argument needs
can be absent.

**What does not need time** (none of it changes a reading):
- **Macro syntax.** A difference of macro syntax alone (the same reading in two macro sets, a handwriting wrapper alone,
  a line-wrap %, an archive-number comment against H's page marker) is not a row and needs no crop.
- **Certainty alone.** A change of certainty alone (1,237 of the 6,439 changes) is one line in the doubts file; once the
  halves show the reading, it needs no crop.
- **Crops.** One crop for each place the halves leave open; no second crop of a decided place; no TeX compilation.

**The hand log: learn his hand as you read.** Keep `SP71_C13_142_hand_log.md` from the first page. Enter every habit of his
hand or his notation that can mislead a reader: a letter he forms like another (a p like an n, a u like an n, a ζ like a
ξ), a sign he draws like another, a notation of his own. For each habit, record:
- the pages where you met it;
- whether it holds at every occurrence of that letter or sign on these pages;
- the places where witness C or witness H misread because of it.

Once a habit holds, read every later occurrence of that letter with it in mind, and confirm each one on the ink. The log
is returned with the transcription, so that the next runs start from it.

## Our conventions

Use exactly the macros of `PREAMBLE.tex` (in the texts folder) and the conventions of witness C's pages: `\cotefile{C}`
and `\scanpage24`, `\mspage{n}`, `\deleted{…}`, `\inserted{…}`, `\margin{…}`, `\uline{…}`, `\uuline{…}`, `\diagram{…}`
in `tikz-cd`, `\figure{…}` in TikZ, `\unsure{reading}`, `\unsure{reading|alternative}`, `\illegible{n}`, and the other
macros that preamble defines.

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
2. **The reading workflow, for each scan page in order, done by you.**
   a. Look at the whole image once, for the layout: the text blocks, displays, diagrams, drawings, margins,
      insertions and deletions, and where each sits.
   b. Read the two halves once each, line by line, with witness C's page file and witness H's text for that page
      beside them. Compare each word, abbreviation, symbol, index, sign, inequality, arrow, parenthesis, underline,
      deletion, insertion and margin note with both witnesses, and settle from the halves everything they settle.
      The halves are at full resolution: enlarging a whole half again shows nothing new.
   c. List the places the halves leave open: a reading that still differs from a witness, a doubt mark of C, a
      small symbol or index that decides the mathematics, a slanted, struck or crowded note, and every place of a kind
      in the error sheet that the halves do not settle. Crop each of them once, tightly (the word or formula and a line
      around it), and zoom in deep: scale the crop up to a few thousand pixels across (LANCZOS) until every stroke is
      plain, raise its contrast (autocontrast, and sharpen where the ink is faint), and rotate it upright where
      slanted. One crop settles one place: do not crop what the halves have settled, and do not crop a decided place
      again. Record each crop in the changes log by its scan and its box in the original image's pixels (x0, y0, x1,
      y1); the crop images themselves are not returned (step 9).
   d. Decide each open place on its crop, and record the decision with the readings it chose between.
3. Then make the page inventory: every text block, display, diagram, drawing, margin note, insertion and deletion on
   the page, top to bottom, and check that each one is in the consolidated text, complete. Look specifically for what
   both witnesses missed.
4. **As soon as a page is done** (every open place decided on the scan): write its file in `pages/` (named as in
   witness C), add its rows to the changes log, the collation list, the inventory and `decisions.tsv`, and append
   `scan NNN done <current UTC time> cote <cote>` to `progress.log`. Only then go to the next page.
5. Read the first page as slowly as the last. The pages done fastest are where errors cluster.
6. **One stream, one notation.** Do the pages yourself, in one stream, in the given order: do not split them among
   parallel workers or sub-agents. Keep one notation table from the first page on: his recurring signs, exponents,
   alphabets, quotation marks and abbreviations, each with how it is written. Before the text is final, compare how each
   recurring sign was read across all the pages, check every difference against the ink, and make the readings agree.
   Put the table at the top of the doubts file.
7. **A second reading of every page.** When every page is done, read each page once more against its image, as a
   second reader would, first at the places of the kinds in the error sheet; correct, or mark doubt, record every
   change in the changes log, and append `scan NNN audited <current UTC time>` to `progress.log`.
8. **A frozen transcription.** When every page is decided, write the SHA-256 of every page file and of the
   combined transcription to `progress.log` with the line `transcription frozen <current UTC time>`. At the
   end, check that the hashes are unchanged and say so in `progress.log`.
9. **Checkpoints.** Save a checkpoint ZIP to the user's Library, or wherever files survive the loss of the execution
   environment, once every 45 minutes of work, each under a new name, `SP71_C13_142_checkpoint_<NN>.zip` with `NN` counting up;
   never overwrite, rename or delete an earlier checkpoint, and put no earlier checkpoint ZIP inside a checkpoint. If
   the workspace comes back empty, restore it from the newest checkpoint and from this conversation before you
   continue. The final ZIP holds everything the checkpoints held. Save checkpoints once every 45 minutes and at no
   other time: none after a page, part, section, cote, folder, chapter or reader. A checkpoint is one ZIP holding every
   deliverable written so far and everything that documents the work (page files, changes log, collation list,
   inventory, decisions, doubts, notes, hand log, progress log, scripts), so that a new session can continue from it and
   the files attached to this prompt. Leave the attached files themselves out of it, the scans and the texts: we have
   them. No image is returned: leave every crop, every half and every other image file out of each checkpoint and out
   of the final ZIP (each crop is recorded by its scan and pixel box in the changes log). It is never a JSON file, a
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

`SP71_C13_142_notes.md`, in English, per page, briefly: what the page states, computes or asks; every place where the
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

One zip file, `SP71_C13_142.zip`, offered as the only download. It holds:

1. **The consolidated transcription:** `pages/` with one file per scan, named as in witness C, and
   `SP71_C13_142_transcription.tex`, all pages in order, one LaTeX fragment (no preamble), using only the macros of
   `PREAMBLE.tex` plus standard LaTeX, `tikz-cd` and TikZ.
2. **`SP71_C13_142_changes.md`, the changes log, per page:** one section per scan, with one table row for every place where
   the consolidated reading differs from witness C or from witness H: place (line, display, margin), C's reading, H's
   reading, the final reading, what the scan shows (the letters, strokes, lines or marks you saw, with the crop you
   used, by its scan and pixel box), and confidence (high, medium, low). Then, per scan, the places still unresolved.
   At the top: the counts per page and in all (changes against C, changes against H, by confidence) and the
   consequential corrections, those that change the mathematics, one per line.
3. **`SP71_C13_142_collation.tsv`, the collation list,** one row per place where witness H's reading differs from the
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
   `what the ink shows`, `crop` (scan and pixel box, or `page` if the page view settled it) and `confidence`.
5. **`SP71_C13_142_doubts.md`** (in English, the readings as on the page): the notation table; a table of the remaining
   doubts (scan, line, reading, alternatives, confidence); the abbreviations met, each with what you think it stands
   for (in this list only); and a short honest note on how legible these pages were, which parts you trust least, and
   how the two witnesses compared on them.
6. **`SP71_C13_142_inventory.csv`** with the columns `scan,sheet_kind,hand,element,kind,position,first_words_or_objects,
   transcribed`: one row per element of every page (kind: text, display, diagram, drawing, margin note, insertion,
   deletion), with `transcribed` = yes for every row. `sheet_kind` is `text` (his notes on the subject of the folder),
   `reused_typed` (a typed page of another text that he wrote on or whose back he used), `typescript`, `letter`,
   `list`, `cancelled_draft` (a draft of his own that he struck through) or `cover`; `hand` says whose hand or machine
   wrote the element (his hand, another named or unnamed hand, typewriter, print).
7. **`SP71_C13_142_notes.md`:** the notes made while reading (above), and `CHECK_EVENTS.tsv`.
8. `progress.log`.
9. **`SP71_C13_142_sheet_feedback.md`:** for our next runs: for each kind in the error sheet, how many places on these pages
   were of that kind, and every recurring error you met that the sheet does not name, with its places; and
   **`SP71_C13_142_hand_log.md`**, the hand log (the error sheet's last section).

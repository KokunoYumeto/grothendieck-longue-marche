# Second pass SP116_CW_75: Alexander Grothendieck's papers, Montpellier archive, cote 75

You are making the second pass over **14 scan pages** from the Montpellier archive of Alexander Grothendieck:
- `75.pdf`: "Cours C4, DEA : notes manuscrites (s.d.), lettre (1978), tapuscrit (1977-1978)." (1977-1978), scans 2-15, 14 pages

Two transcriptions of these pages exist already. Both were made by AI models from the same scans, independently of
each other, and neither has been checked against the ink by a person:

- **Witness C (Codex):** a diplomatic LaTeX transcription by GPT-6 Astra at reasoning effort max, in Codex web, one
  session per folder of 4 to 12 scans (13-15 Nov 2026), one file per scan, with its doubts table, inventory, audit
  and short notes. Its notes were written without any context: they list the steps the pages mark as unverified and
  the titles and page counts, and nothing else.
- **Witness H (Hua's):** the transcription of the Commutator project of Michel Hua (github.com/Commutator-IO/
  grothendieck-project, commit `aef7db2`), made by Claude Opus 5 and Claude Opus 5.5 and read again in part by Claude
  Fable 5.2 (efforts not recorded), in that project's own LaTeX macros, one file per batch of about twenty archive
  pages. Their page number n is our scan number n + 1. Witness H has transcribed text for 13 of these
  14 scans; nothing for 1 (`page_map.tsv` lists them; those pages are checked against the ink with witness C alone).

Your job: **one consolidated diplomatic transcription of every page, from the ink,** in our conventions, with a
record of every place where it differs from witness C or from witness H and of what the scan shows there.

**Three sub-agents on different pages, then a second reading.** Pro gives you three sub-agents: use all three at
once, each on a page of its own. Give each sub-agent one page at a time, in the given order (the next page goes to the
first sub-agent that is free), with only that page's images, witness C's and witness H's texts for it, the section "The
errors that recur in these papers", our conventions and your notation table as it stands. It reads its page line by
line from the scan against both witnesses (method, step 2, a to d) and returns its reading of the page and every place
where it differs from either witness, with what it saw in the ink. You, the main reader, check each return on the scan,
decide every place it left open or that disagrees with a witness, and write the page. When every page is done, each page
is read a second time by a different sub-agent from the one that read it first (method, step 7).

**The mathematics while reading.** Follow the mathematics of the page as you read: a formula that does
not parse, an index that does not match, a sign, inequality or arrow that contradicts the argument is a place to look
at the ink again, and the ink decides, never the expected form. What the page claims and what the mathematics showed
go briefly into the notes (section "Notes while reading"); nothing beyond these pages is researched. Witness C's
notes and doubt table (in its folder in the witnesses zip) list what an earlier reader questioned on each page:
use them to find places to look again, and let the ink decide. Fidelity to the ink comes first throughout.

Witness C is a careful text, which is why the pages are checked here rather than transcribed again. It is not a
final one: earlier second passes of this archive changed its reading at about 11 places a page, two thirds of them
at places it had not marked as doubtful.

## The attachments

- `SP116_CW_75_scans.zip`: for every scan page N three images: `<folder>_<cote>_scanNNN.jpg` (the whole page) and
  `<folder>_<cote>_scanNNN_a.jpg`, `<folder>_<cote>_scanNNN_b.jpg` (its top and bottom halves, or left and right
  halves of a landscape sheet, overlapping a little, at full resolution), where `<folder>` is the Codex folder that
  holds the scan (column `folder` of `page_map.tsv`). N is the page number in the archive's PDF. The images are
  contrast-enhanced and sharpened. The scans of each cote that are not in this package are other tasks: none.
- `SP116_CW_75_witnesses.zip`: `README.md` (start there); `page_map.tsv` (for each scan: the Codex folder, cote, our
  scan, their page, the witness C file, the witness H batch file, whether H has text, only a description, or nothing
  for it, and the context folder that covers it); `codex/<folder>/`, one folder per Codex session (witness C:
  `pages/`, the combined transcription, doubts, inventory, audit, notes, `progress.log`, `PREAMBLE.tex`, which
  defines the macros, and `PROMPT.md`, the task it was given); `hua/` (witness H: the batch files and
  drawing files of these pages under `transcripts/<cote>/`, their preamble `transcripts/preamble/grothendieck.sty`,
  their `CONTRIBUTING.md` and `RIGHTS.md`).
- `SP116_CW_75_sweep3.zip`: our sweep of 18-19 November 2026 (readers of Claude Opus 5.5 at effort max), in its files
  that bear on these cotes (`cotes71_75`): each file's reading (`readings/<file>.md`), the readings it decided on the
  images (`readings/<file>_CORRECTIONS.tsv`), its check events, dependencies and deliverables, and the topic's
  `STUDY.md` (`study/`). Their CORRECTIONS rows are witness S for the transcription (next section); 2 of those rows
  name a page of this piece by its scan. The rest may be read for the mathematics of these pages.

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
- **Witness S, the sweep's decided readings** (`readings/<cote>_CORRECTIONS.tsv` in the sweep zip): each row is a
  reading our sweep decided on the images, mostly where the mathematics turns on it. Treat each as you treat C and H:
  look at the ink, then confirm it or overturn it, and record which in the changes log with the row's id. A row of S
  never settles a reading by itself, and a page it does not cover is read as fully as any other.
- **A doubt mark of witness C** is a place to decide in the ink: resolve it where the ink settles it, keep it where
  it does not, and record either in the changes log.
- **Never fill in from memory, from published texts or from what the mathematics should say.** If the page says
  something surprising, transcribe the surprise. A correction of his text belongs in a research note, never in the
  transcription.

## The errors that recur in these papers: read this before the first page

Where these come from: the 6,439 places where earlier second passes of this archive (GPT-6 Astra (ChatGPT Pro mode), 23 runs,
470 pages) changed witness C's reading, sorted by the passes' own kinds, and the places Michel Hua checked by eye on the
facsimile against witness H. Two thirds of those changes (3,211 of the 5,032 that changed the text) were at places
witness C had not marked as doubtful: look for these kinds everywhere, not only at its doubt marks. The counts say where
the errors were; they never decide a reading. The ink decides.

**Where the first readings were changed most often** (559 pages read twice, token by token; tokens changed per 100,
on average 7):
- words inside a doubt mark of witness C: 30;
- Greek letters: 11 in all, and most where a capital and its lower case look alike: Φ 53, Π 29, γ 20, π 16 (Π read
  as π was the commonest swap of a sign);
- handwritten words on a typescript 15, words in an insertion 13, words in a margin note 12;
- struck text: its mathematics 10, its words 9;
- the signs +, → and ⊗: 10 to 11 (⊖ read as ⊗);
- plain words in the line: 5.

**A letter read for another inside words belongs to one cote:** q read as g on cote 103, u and f read as n on cote
123, J read as T or Y on cote 13. When you find such a swap, check every occurrence of that letter on these pages, and
enter it in the hand log.

**Further places that were changed more often than the rest** (same 559 pages):
- the mathematics next to a doubt mark in a formula: 14 in 100; when one sign of a formula is doubtful, read the
  whole formula again, not the marked sign alone;
- an insertion that was struck again: 17 in 100; it is small, above the line and under a stroke at once: it gets its
  own crop;
- arrows with a hook, a bar, two shafts or a label: 13 in 100; look at both ends of every arrow, and take a label
  above it as part of it;
- digits written by pen, in a margin or under a strike: no pair of digits is safe; a 5 may be a 6 or a 3;
- capitalised words inside a sentence (names): 10 in 100; read them letter by letter and compare them with the names
  of the same cote;
- a superscript + whose upright stops at the bar looks like ⊤ (cote 81): where a minus stands on the same line, it is
  a +;
- he writes the empty set as ϕ (cotes 71, 156-4): write what he writes, and enter « ϕ : l'ensemble vide » in the
  notation table once.

**A doubt mark of witness C is not a default.** Its first reading stood in 514 of the 920 marks the second passes
settled (56 in 100); the alternative or another reading in the rest.

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

**What is not ink.** Specks, bleed-through from the other side and the paper's watermark are not transcribed. The
watermark of his paper reads « EXTRA STRONG » (sometimes with a maker's name), large and pale, often sideways or
mirrored, and only partly visible (« ng Extra Stro », « RONG … EXTRA STR »); earlier readings transcribed it as text on 92
pages of cotes 156-1, 156-2, 156-3, 126 and 13. Name it once in the notes of the cote, never in the transcription and
never as a doubt mark. A faint dot is punctuation only where the sentence or the
formula gives it a place, and only if it is as dark as the writing around it; a second model, reading 366 hard places,
took 27 of the marks the passes had added for specks of the paper.

**Typescripts.**
- **A letter typed over another:** record the letter underneath, where it can be read, as `\deleted{x}` before the
  letter that stands (`\deleted{\illegible{1}}` where it cannot). This is the same decision on every page.
- **Typing errors:** both earlier readers corrected them silently, writing the word they recognised (64 of 118 places).
  Read letter by letter the words you recognise at once: a typed word may be misspelt, and it stays misspelt.
- **What the machine cannot type:** a doubled capital typed for a double-struck letter, or an x for ×. Enter the keyed
  form once in the notation table, and do not doubt it at each place.

**Small things that were changed often.**
- **Accents:** an accent is one short stroke whose slant need not tell acute from grave. Where a stroke is there, write
  the accent the word has in French; note a missing accent only where no stroke is there.
- **Letters of one cote in formulas:** on cote 156-3 a capital E in a formula may be his ε; compare it with an ε of
  the same page.
- **Page numbers:** look at the head of the sheet for his own page number before the first line. Earlier readings left
  it out on many pages.
- **Formula numbers:** his formula numbers stand at the left of the formula. Write them as the conventions do; their side
  is set once for the edition.

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

**The hand log: learn his hand as you read.** Keep `SP116_CW_75_hand_log.md` from the first page. Enter every habit of his
hand or his notation that can mislead a reader: a letter he forms like another (a p like an n, a u like an n, a ζ like a
ξ), a sign he draws like another, a notation of his own. For each habit, record:
- the pages where you met it;
- whether it holds at every occurrence of that letter or sign on these pages;
- the places where witness C or witness H misread because of it.

Once a habit holds, read every later occurrence of that letter with it in mind, and confirm each one on the ink. The log
is returned with the transcription, so that the next runs start from it.

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
2. **The reading workflow, for each scan page: a to d by the sub-agent that has the page, e by you.**
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
      again. Save each crop in `crops/`, named by its scan and place, and record it in the changes log by that file name and its
      box in the original image's pixels (x0, y0, x1, y1).
   d. Decide each open place on its crop, and return the reading of the page with every place where it differs from
      either witness and what the half or the crop showed.
   e. You check the return: look at the crop of every place the sub-agent left open or that disagrees with a witness,
      or make one crop of it yourself, decide, and record the decision with the readings it chose between.
3. Then make the page inventory: every text block, display, diagram, drawing, margin note, insertion and deletion on
   the page, top to bottom, and check that each one is in the consolidated text, complete. Look specifically for what
   both witnesses missed.
4. **As soon as a page is done** (every open place decided on the scan): write its file in `pages/` (named as in witness C), add its rows to the changes
   log, the collation list and the inventory, and append `scan NNN done <current UTC time>` to `progress.log`. Only
   then go to the next page.
5. Read the first page as slowly as the last. The pages done fastest are where errors cluster.
6. **One stream, one notation.** Do the pages yourself, in one stream, in the given order: do not split them among
   parallel workers or sub-agents. Keep one notation table from the first page on: his recurring signs, exponents,
   alphabets, quotation marks and abbreviations, each with how it is written. Witness C was made in separate sessions
   of a few pages each, so the same sign may be written differently from one folder to the next: before the text is
   final, compare how each recurring sign was read across all the pages, check every difference against the ink, and
   make the readings agree. Put the table at the top of the doubts file.
7. **A second reading of every page.** When every page is done, give each page to a different sub-agent from the one
   that read it first, to read once more against its image, first at the places of the kinds in the error sheet; decide
   every difference it finds on the scan, correct or mark doubt, record every change in the changes log, and append `scan NNN audited <current UTC time>` to `progress.log`.
8. **A frozen transcription.** When every page is decided, write the SHA-256 of every page file and of the
   combined transcription to `progress.log` with the line `transcription frozen <current UTC time>`. At the
   end, check that the hashes are unchanged and say so in `progress.log`.
9. **Checkpoints.** Save a checkpoint ZIP to the user's Library, or wherever files survive the loss of the execution
   environment, once every 45 minutes of work, each under a new name, `SP116_CW_75_checkpoint_<NN>.zip` with `NN` counting up;
   never overwrite, rename or delete an earlier checkpoint, and put no earlier checkpoint ZIP inside a checkpoint. If
   the workspace comes back empty, restore it from the newest checkpoint and from this conversation before you
   continue. The final ZIP holds everything the checkpoints held. Save checkpoints once every 45 minutes and at no other time: none after a page, part, section, cote, folder, chapter or reader. A checkpoint is one ZIP holding every
   deliverable written so far and everything that documents the work (page files, changes log, collation list,
   inventory, doubts, notes, progress log, scripts), so that a new session can continue from it and the files attached
   to this prompt. Leave the attached files themselves out of it, the scans, the witnesses and the context: we have
   them. The crops in `crops/` go into every checkpoint and the final ZIP. It is never a JSON file, a recovery file, a summary, or an export of the newest pages only. Each checkpoint zip holds the current deliverables and documentation; earlier checkpoints are not copied into it. The checkpoints
   are what keeps the work if this session dies: work that is in no checkpoint is lost.
10. **If the execution environment fails.** A failed or unavailable environment does not end the task. Retry at
    intervals for as long as this session lasts, without writing recovery text into the chat. When the environment is
    back, restore your work from your newest checkpoint and the earlier checkpoints its file list names, redo what you
    had done after that checkpoint, and continue to the end. Do not write files out in this chat instead: the work
    reaches us only through checkpoint ZIPs and the final ZIP.


This task is long by design: 14 pages, each read in the ink against two witnesses, read a second time, decided and recorded.
Work through all of it completely; do not stop at a sample or a plan, and do not ask whether to continue.
Ignore any clock.

## Notes while reading

`SP116_CW_75_notes.md`, in English, per page, briefly: what the page states, computes or asks; every place where the
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

One zip file, `SP116_CW_75.zip`, offered as the only download. It holds:

1. **The consolidated transcription:** `pages/` with one file per scan, named as in witness C, and
   `SP116_CW_75_transcription.tex`, all pages in order, one LaTeX fragment (no preamble), using only the macros of
   `PREAMBLE.tex` plus standard LaTeX, `tikz-cd` and TikZ.
2. **`SP116_CW_75_changes.md`, the changes log, per page:** one section per scan, with one table row for every place where
   the consolidated reading differs from witness C or from witness H: place (line, display, margin), C's reading, H's
   reading, the final reading, what the scan shows (the letters, strokes, lines or marks you saw, with the crop you
   used, by its file name and pixel box), and confidence (high, medium, low). Then, per scan, the places still unresolved. At the top: the counts per
   page and in all (changes against C, changes against H, by confidence) and the consequential corrections, those that
   change the mathematics, one per line.
3. **`SP116_CW_75_collation.tsv`, the collation list,** one row per place where witness H's reading differs from the
   consolidated reading, with the columns `folder, their_page, our_scan, line, their_reading, codex_reading,
   final_reading, scan_shows, kind, marked_in_H, confidence`. `kind` is one of: misread word, misread symbol or index,
   omission, text not on the page, deletion state (struck given live or live given struck), insertion or placement,
   abbreviation expanded or spelling modernised, readable ink left as `\ill{}`, drawing or diagram, other.
   `marked_in_H` says whether H carried a doubt mark there. Differences of macro syntax alone (the same reading in the
   two macro sets) are not rows. Where H has no text for a page, the page has no rows.
4. **`SP116_CW_75_doubts.md`** (in English, the readings as on the page): the notation table; a table of the remaining
   doubts (scan, line, reading, alternatives, confidence); the abbreviations met, each with what you think it stands
   for (in this list only); and a short honest note on how legible these pages were, which parts you trust least, and
   how the two witnesses compared on them.
5. **`SP116_CW_75_inventory.csv`** with the columns `scan,sheet_kind,hand,element,kind,position,first_words_or_objects,
   transcribed`: one row per element of every page (kind: text, display, diagram, drawing, margin note, insertion,
   deletion), with `transcribed` = yes for every row. `sheet_kind` is `text` (his notes on the subject of the folder),
   `reused_typed` (a typed page of another text that he wrote on or whose back he used), `typescript`, `letter`,
   `list`, `cancelled_draft` (a draft of his own that he struck through) or `cover`; `hand` says whose hand or machine
   wrote the element (his hand, another named or unnamed hand, typewriter, print).
6. **`SP116_CW_75_notes.md`:** the notes made while reading (above).
7. `progress.log`.
8. **`SP116_CW_75_sheet_feedback.md`:** for our next runs: for each kind in the error sheet, how many places on these
   pages were of that kind, and every recurring error you met that the sheet does not name, with its places;
   and **`SP116_CW_75_hand_log.md`**, the hand log (the error sheet's last section).

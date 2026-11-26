**The attached files.** Besides this file there is one ZIP, `SR06_10.zip`. Unpack it once: it holds every file named below. The folders named below are already unpacked inside it, so there is nothing more to unpack; every other file is at the top level under its own name.

# The second reading, SR06_10: Alexander Grothendieck's papers, Montpellier archive

You are making the second reading of **30 scan pages** of the Montpellier archive of Alexander Grothendieck (cotes
10). Each page has been read twice already, by AI models, and neither reading has been checked against the ink by a
person:

- **Witness C (ours):** our first diplomatic LaTeX transcription of the page, made from the scan.
- **The earlier second pass:** GPT-6 Astra (ChatGPT Pro mode) read each page from the scan against witness C and witness
  H (the transcription of the Commutator project of Michel Hua, github.com/Commutator-IO/grothendieck-project, an AI
  transcription) and wrote the text you are given in `SR06_10_pages/`. Corrections decided later on the scans are in it too.
- **Witness P (the print), for 1 of these 30 pages:** these pages are drafts, typescripts or copies of a published
  text (SGA 4), and the printed text of the same passages is attached. The print is, as a rule, a later state of the
  text, edited by others, and not a reading of this ink: it shows where to look and never settles a reading (section
  "Witness P: the print").

That pass was made by one reader, and its second reading of each page was brief or missing: where it logged one, it
took under a minute a page and changed almost nothing. Where witness C and witness H read different words, it kept
witness C nearly every time. Your job: **the second reading it did not do.** At the places where errors are most often,
a reader who has not seen any text of the page reads the ink first; then the two readings are compared, and the text is
corrected wherever the ink shows otherwise, with every change recorded exactly.

**Three sub-agents on different pages, and you.** Pro gives you three sub-agents: use all three at once, each on a page
of its own (the next page goes to the first sub-agent that is free). You, the main reader, prepare each page's boxes,
give the sub-agent only the page's image and its box list, compare its readings with the text by script, and decide
every difference on the ink.

## The attachments

- `SR06_10_pages/<cote>_scanNNN.tex`: the text of each page as it stands now: the text to check and to correct.
- `SR06_10_scans/<cote>_scanNNN.jpg`: the scan of each page, at the resolution of the archive's PDF, with its contrast raised
  and sharpened.
- `SR06_10_witnesses/C/<cote>_scanNNN.tex`: witness C, our first transcription of the page.
- `SR06_10_witnesses/H/<cote>_scanNNN.tex`: witness H's text of the page, for 30 of these 30 pages. His page n is our scan
  n + 1; his editorial page markers, synopses and notes are not source text; his `\emph` may stand for an underline.
- `SR06_10_text_H_differences.tsv`: made by script before this run: for each page, every place where the text and witness H
  differ (their words, markup set aside), with the words before it and its `kind`: `different reading` (up to three
  words or signs on each side), `only in witness H` or `only in the text` (up to eight words that one side has alone),
  `longer`, `long stretch` (a passage one side skipped, or witness H's editorial matter) and `TikZ options`.
- `SR06_10_text_C_differences.tsv`: made by script the same way: for each page, every place where the text departs from
  witness C (the earlier pass's corrections and the later ones), with the same kinds.
- `SR06_10_witnesses/P/<cote>_scanNNN.tex`: witness P for 1 of these 30 pages: the printed passages of the page, each
  under a header that names the work, the volume and section, the edition file and its lines, how close the passage is
  (verbatim draft, close draft, paraphrase or reworking) and how many words of the page it matched.
- `SR06_10_text_P_differences.tsv`: made by script the same way: for each page with witness P, every place where the text
  and witness P differ (formulas and diagrams, shown as FORMULA, the print's labels and references, and the page's
  struck passages set aside; the edges of each passage trimmed), with the same kinds (`only in witness P` for `only in
  witness H`) and three more, `abbreviation or truncation`, `spacing or hyphenation` and `accent`.
- `SR06_10_earlier_pass/<run>/`: the record of the earlier second pass of these pages: its changes log (every place it
  changed, with what the scan showed, its crop and its confidence), its decisions on the doubt marks where it kept such a
  table, its notation table (at the top of its doubts file) and its hand log where it kept one.
- `PREAMBLE.tex`: the macros of the transcription.

**Look at the images yourself.** Reading software (OCR, a PDF text layer, any text-recognition library) is not a
substitute for looking and must not be used on these pages.

## The boxes of a page

For each page, list its boxes in `second/<page>_boxes.tsv` (`<page>` is the page file's name without `.tex`; columns
`box`, `kind`, `x0`, `y0`, `x1`, `y1`, in the scan's pixels), one box for each of these places:

- every insertion, every margin note and every struck passage;
- every formula in which the text or witness C has a doubt mark (the whole formula);
- every number written by pen, and every word written by hand on a typescript;
- every row of `SR06_10_text_H_differences.tsv` of kind `different reading` or `only in witness H` (a few words witness H
  has and the text lacks may be words the text missed);
- every row of `SR06_10_text_C_differences.tsv` of kind `different reading`, `only in witness C` or `only in the text`,
  unless the earlier pass's changes log gives that place high confidence and names its crop;
- the rows of the other kinds (`longer`, `long stretch`, `TikZ options`) are mostly passages one witness skipped or
  set differently: look at each once on the page, and give it a box where it holds a reading question;
- every row of `SR06_10_text_P_differences.tsv` of kind `different reading` or `abbreviation or truncation`;
- every doubt mark of witness C that the earlier pass resolved without a crop (its decisions table says `page`, or its
  changes log names no crop for it).

A box holds the place and a line around it. Then write the text's reading of each box, in our conventions, to
`second/<page>_first.tsv` (columns `box`, `reading`).

## Witness P: the print

For 1 of these pages the same text is in print (SGA 4), and witness P is that printed passage, cut from a LaTeX
text of the printed work. It is a witness of another kind than witness C, witness H and the text. They are readings of this ink; the print is,
as a rule, a later state of the text, prepared by its editors, who expanded abbreviations, corrected slips and typing
errors, renumbered and sometimes rewrote, and its LaTeX can carry slips of its own. Nothing is filled in from it.

- **A difference between the page and the print is often real.** Each row of `SR06_10_text_P_differences.tsv` is a place to look at in the
  ink, and the ink decides which of these it is: the text misread the ink and the print has what the ink shows
  (the page changes, step 4a, from the ink, not from the print); the page has an earlier state, another word, order or formula (the text stands, step 4b); an abbreviation, a slip or a typing
  error that the print expanded or corrected (it stays as written, in our conventions); an error of the print or of
  its LaTeX; or a difference made by the comparison (a formula set differently, a line cut at the edge of a passage, a
  margin note set beside the text). When 30 such differences were checked on the scans (24 Nov 2026), 13 were earlier
  states, 4 abbreviations the edition expands, 8 made by the comparison, 3 misreadings of ours and 2 undecided; one of
  the three misreadings was a typing error («monodormie») that our reading had corrected silently and the print had
  kept as typed.
- **Rows of kind `different reading` and `abbreviation or truncation` get a box (above):** read the place letter by letter and
  record what the ink shows.
- **Where the strokes fit both words** (a d with a flat stroke for de, des, du or dans; m against mm), write
  `\unsure{...|...}` with the reading the mathematics needs first, and say in the row that the ink does not decide.
  The edition has readings of its own that the ink does not support: « alors » where he wrote « donc », « par » for
  « pas », « dans » for his « de » (checked on the scans, 24 Nov 2026). Never take its word, or its expansion of an
  abbreviation, for his.
- **Where witness P agrees with the text, the ink still decides.** Editors correct slips and typing errors, and so do
  readers: where both carry the same corrected word, the ink may still have the slip.
- **Every row is recorded** in `SR06_10_print.tsv` (What to return), with what the ink showed; a place where your page
  differs from the print and the list has no row gets a row of its own. These rows are the differences between the
  draft and the print, a result in their own right.

## Method

1. Before the first page, write the current time (UTC) as the first line of `progress.log`. Read the earlier pass's
   notation tables and hand logs for these cotes: they are its readings of his habits, to be checked on the ink like
   everything else. Keep one notation table for this run, at the top of `SR06_10_notes.md`.
2. **For each page,** write its boxes and the text's reading of them (above).
3. **The blind reading.** The sub-agent that has the page gets the page's image and `second/<page>_boxes.tsv`, and nothing
   else: not the text, not `_first.tsv`, not witness C, witness H or witness P, not the earlier pass's record, not your notes. It
   crops each box tightly and zooms in deep: it scales the crop up to a few thousand pixels across (LANCZOS) until every
   stroke is plain, raises its contrast (autocontrast, and sharpen where the ink is faint), and rotates it upright where
   slanted. It reads each box from the ink and writes its reading, in our conventions, to `second/<page>_second.tsv`
   (columns `box`, `reading`), with `\unsure{reading|alternative}` where the ink admits two readings. Save each crop in
   `crops/`, named by its page and box.
4. **The comparison.** Compare `second/<page>_first.tsv` and `second/<page>_second.tsv` box by box, token by token, by
   script. For every difference, look at the crop yourself (make a tighter one where it helps), with the text, both
   witnesses and the earlier pass's record beside it, and decide:
   - **(a) the page changes:** the text misreads the ink, and you write what the ink shows; or the ink does not settle
     it, and you put a doubt mark in place (`\unsure{reading|alternative}`), never a guess;
   - **(b) the text stands:** the ink shows what the text has.
   A misreading you see in a crop outside its box is decided the same way, as a row of its own.
5. **As soon as a page is done:** write it to `edited_pages/` (named as given), add its rows to `placements.tsv`, and
   append `scan NNN audited <current UTC time> cote <cote>: B boxes read, D differences, K changed` to `progress.log`.
   Only then is the page finished.
6. Change nothing on a page except through a row of `placements.tsv`: no other edit, no normalisation, no reformatting.
7. **Checkpoints.** Save a checkpoint ZIP to the user's Library, or wherever files survive the loss of the execution
   environment, once every 45 minutes of work, each under a new name, `SR06_10_checkpoint_<NN>.zip` with `NN` counting up;
   never overwrite, rename or delete an earlier checkpoint, and put no earlier checkpoint ZIP inside a checkpoint. If the
   workspace comes back empty, restore it from the newest checkpoint and from this conversation before you continue.
   The final ZIP holds everything the checkpoints held. Save checkpoints once every 45 minutes and at no other time:
   none after a page, part, section, cote, folder, chapter or reader. A checkpoint is one ZIP holding every deliverable
   written so far and everything that documents the work (`placements.tsv`, `edited_pages/`, `second/`, the crops in
   `crops/`, the notes, the hand log, `CHECK_EVENTS.tsv`, `progress.log`, scripts), so that a new session can continue
   from it and the files attached to this prompt. Leave the attached files themselves out of it: we have them. It is
   never a JSON file, a recovery file, a summary, or an export of the newest pages only. Each checkpoint zip holds the
   current deliverables and documentation; earlier checkpoints are not copied into it. The checkpoints are what keeps
   the work if this session dies: work that is in no checkpoint is lost.
   **Crops: one dump, at the end.** In the checkpoints and the final ZIP, `crops/` holds only `crops/CROPS.tsv`: each
   crop's file name, its page, its box in pixels of the attached scan, and the place it decided. With the final ZIP,
   deliver the crop images once, as `SR06_10_crops.zip`: the crops of the places you changed or left undecided, as
   greyscale JPEG at quality 85; the boxes in `CROPS.tsv` let us cut any other crop again from our scans. Keep
   `SR06_10_crops.zip` under 200 MB: if it would be larger, lower the JPEG quality or the size, and leave out no crop
   of a change. Each ChatGPT account has 100 GB of storage, and crops repeated in every checkpoint fill it.
8. **If the execution environment fails.** A failed or unavailable environment does not end the task. Retry at
   intervals for as long as this session lasts, without writing recovery text into the chat. When the environment is
   back, restore your work from your newest checkpoint and the earlier checkpoints its file list names, redo what you
   had done after that checkpoint, and continue to the end. Do not write files out in this chat instead: the work
   reaches us only through checkpoint ZIPs and the final ZIP.

**No copies of sources in any ZIP you return.** No ZIP you return holds an unchanged copy of an attached file, or a
copy or plain text extraction of another author's paper, book or scan. We have the attached files; for a source you
fetched yourself, record the citation, the address, the SHA-256 and the pages used. Whatever this task asks you to
deliver (transcriptions, translations, editions, notes, programs, figures) always goes in.

This task is long by design: 30 pages, each with every box read blind from the ink, compared with the text, and every
difference decided on the scan and recorded. Work through all of it completely; do not stop at a sample or a plan, and
do not ask whether to continue. Ignore any clock.

## The errors that recur in these papers: read this before the first page

Where these come from: the 6,439 places where earlier second passes of this archive (GPT-6 Astra (ChatGPT Pro mode), 23 runs,
470 pages) changed witness C's reading, sorted by the passes' own kinds, and the places Michel Hua checked by eye on the
facsimile against witness H. Two thirds of those changes (3,211 of the 5,032 that changed the text) were at places
witness C had not marked as doubtful: look for these kinds everywhere, not only at its doubt marks. The counts say where
the errors were; they never decide a reading. The ink decides.

**Where the errors are densest (23 Nov refresh, 1,218 second-passed pages, 17,827 reading corrections).** Formula-dense
pages and pages with diagrams in his late hand (cotes 141-152 and 156) carry about 13 reading corrections per 100
words and 15-16 a page; prose pages and typescripts carry 2-4 per 100 words and about 5 a page. Give the dense pages
the most crops. Even on them, two corrections in three are in the words between the formulas and in the struck,
inserted and margin text, not inside the formulas: read those words as closely as the formulas. And read every line
of every manuscript page against the scan, not only the boxes: about one correction in five lies where witnesses C
and H agree and C has no doubt mark.
The one-line refinements that name runs (SP72-SP83, SP114-SP117) come from those runs' own feedback of 20-21 Nov.

**Where the first readings were changed most often** (559 pages read twice, token by token; tokens changed per 100,
on average 7):
- words inside a doubt mark of witness C: 30;
- Greek letters: 11 in all, and most where a capital and its lower case look alike: Φ 53, Π 29, γ 20, π 16 (Π read
  as π was the commonest swap of a sign);
- handwritten words on a typescript 15, words in an insertion 13, words in a margin note 12;
- struck text: its mathematics 10, its words 9;
- the signs +, → and ⊗: 10 to 11 (⊖ read as ⊗);
- plain words in the line: 5.

These rates were measured on pages whose witness C is a Codex-web reading (GPT-6 Astra at reasoning effort max). On
pages read by another route, take them as places to look, not as rates.

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
settled (56 in 100); the alternative or another reading in the rest. **A doubt mark is resolved only on a crop of it:**
the changes log gives the crop's box and the stroke that decides. A doubt mark inside struck text stays unless every
letter is plain on the crop. A doubt mark in a formula is decided with the whole formula: the signs next to a doubtful
sign were wrong twice as often as the others.
In every \unsure{a|b} you keep, the first alternative is the one the text uses: put first the reading the ink and the
sentence favour, never a misspelling or a non-word when a real word fits the strokes (40 kept marks after earlier
passes had it the wrong way round: analognous|analoguous, invarient|invariant, plui|plus). Check the order of every
doubt mark you keep before you freeze the page. When a crop settles a doubt, remove the mark in the page itself, not
only in the log.

**Where witness C was wrong, most often first (places on those 470 pages):**

1. **Symbols and indices (1,075).**
   - Greek letters: Φ and φ, Π and π, γ and ψ were changed 2 to 8 times as often as the average letter in witness C;
     Π read as π (25 places) and ψ read as μ (4) were its commonest swaps. Witness H's reader confused other letters (ξ
     and ζ, ρ and p, δ and λ, Λ and A, Δ and 2), which witness C read well: they matter where you take a reading from
     H. Fix the letter where the page or the run defines it, then read every occurrence the same way: on cote 12 one
     definition settled 27 places.
   - Small digits, primes and exponents: a prime dropped or added; 1 and 2, 0 and 1, 1 and I, l and 1. Read them by the
     degree, count or date the page forces, and never regularise one silently.
   - Worn signs: a short stroke between two terms may be a map, a minus or a plus; two ticks or a ∩ between the rows of
     a diagram may be = or ⊂. Read them by the formula and the rows of the diagram, then confirm on the ink.
   - A relation written vertically (two upright strokes between stacked objects) stays vertical: it is neither a
     horizontal = nor an arrow (SP74, SP83).
   - Pairs he writes one for the other (i and j, m and n, X and Y, K and k, V and W): keep the letter as written, even
     where the argument needs the other; the meant one goes in the notes.
   - Letters his hand forms alike are a different case from such slips. Where his p looks like an n, or his ζ like a
     ξ, the ink alone does not decide: his notation on these pages and the mathematics decide which letter it is, and
     the habit goes into the hand log (last section). A slip is a clear letter that is wrong, and it stays.
   - A symbol that names one object is read the same way throughout the page and the cote (ξ and ζ for one object on
     16/53, [K_0:K] for [K_0:Q] on 15/142 survived a pass): check it against the notation table, and crop every
     instance that differs.
   - A curly capital: decide script (\mathscr) or calligraphic (\mathcal) from his clearest instance on these pages,
     enter it in the notation table, and hold it; the two were swapped in both directions.
2. **Words (1,032).**
   - His coined terms read as familiar words of the same outline (« préfigure » as « polygone », « strates » as
     « structures »): where a strange word recurs, check it where he defines it.
   - His own spellings, his English words and his accents stay as written: the earlier readings normalised 4 of the 6
     places checked (« because » given as « avec », « systématiques » as « systématique »).
   - Endings (a final s, de and des, le and les): the grammar does not decide them; he breaks agreement himself (2 of
     the 6 endings checked by eye). Read an ending on a crop of the word; when H's ending differs
     from C's, crop it even if the rest of the word agrees.
   - A terminal pen return is not a letter: compare the ending with an ending of the same page (SP83).
3. **Omissions (1,009).**
   - A one-word insertion (la, le, de, un, et, des, ne, même) is small and easily misread: words in an insertion were
     changed at 13 in 100 in witness C, against 5 for a plain word; of 10 such words Michel Hua checked by eye, witness H
     had another word in 5.
   - Prefixes are written above the line (sous-, quasi-, ⊗-, Δ-, pseudo-, contra-): 28 of the 30 checked by eye are on
     the page. Look above the line before taking a prefix as absent.
   - Margin notes, slanted notes, the punctuation that survives a cancellation.
   - A curved leader that carries an insertion to its place is not a parenthesis, a strike or a comma: trace its path
     first, and record the attachment apart from the words (SP74, SP75, SP78, SP83).
4. **Drawings and diagrams (886).** What looks like a drawing may be a crossing-out, a hatched formula, a matrix or a
   diagram to set (17 such cases checked by eye). In a real figure, count the sides, points and strokes twice. A label's side of its arrow (above or
   below, left or right) and which arrow it labels are part of the reading: earlier passes put labels on the wrong
   side.
   Running text is never drawn: a word, letter or sign of the text is transcribed, with `\unsure` where in doubt, never
   set as a picture (on the calibration pages of 21 Nov the three-reader passes drew inserted words, struck letters
   and typed overstrikes as TikZ, and the reading was lost). A real figure keeps its open and filled points, pen gaps,
   line weights and layers: never a generic graph, never a description in words (SP78, SP82, SP83).
5. **Readable ink left as illegible (711).** The full-resolution halves, or one tight crop, usually read it.
6. **Insertions put in the wrong place (500).** Decide where an insertion attaches (which word, line, item, margin or
   leaf) separately from what it says.
7. **Struck text (417).** Three separate questions: which words are struck, whether the line is a strike at all, and
   which words replace them. A struck word given as live, or a live one given as struck, is witness C's commonest silent
   error. Mark \deleted only where a stroke crosses that word on a tight crop; a stroke of the line above or
   below, or an underline, is not a cancellation (« entre 14 orbites » was marked struck with no stroke on it).
   A descender from the line above, or a leader or a drawing that crosses a word, is not a strike: follow the stroke
   to its letter (SP75, SP82, SP83).
8. **Abbreviations expanded, spelling modernised (389).** His short forms stay in the text: tt, ess., t.f., il f. et il
   s., tot^t, néc^t, ss-, ½, and = standing for « même ». An expansion goes only in the abbreviations list.
   A stop is read, not supplied (autom, mod, gén without a dot stay so; four points stay four), and inside a doubt
   mark the alternatives keep the written short form (SP75, SP79; the calibration of 21 Nov).
9. **Text that is not on the page (128).** A word the sentence needs is either an insertion that was missed or not on
   the page. If it is not on the page, it is not transcribed, not even as a doubtful reading; it goes in the notes.
   Nothing is completed: an unbalanced parenthesis, a word cut at the paper's edge, a label missing from a sequence
   stay as they are (SP78, SP79, SP82). But a reading that starts or ends mid-word, or a bracket without its partner, at the edge of a
   crop means the crop cut the phrase: widen the crop to the whole phrase and read again (« tion avec coh-mologie
   cristall]ine » on 66/2). Two witnesses agreeing on a word the sentence wants is no evidence: in SP78
   both added « en » where only « une » is written, in SP83 both dropped a detached accent.
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
Show-through from the other face, or the reversed listing of a reused sheet, is not text: settle the face of the
sheet first (SP82, SP83). Thin foliation numbers in another hand are not his numbering (SP82).

**Typescripts.**
- **A letter typed over another:** record the letter underneath, where it can be read, as `\deleted{x}` before the
  letter that stands (`\deleted{\illegible{1}}` where it cannot). This is the same decision on every page.
- **Two letters in one cell, read as two letters,** make false words. Seen in the Pursuing Stacks typescript, against
  the print (24 Nov 2026): "comrresponding" (r typed over m, 134-4/28), "descripttion" (134-3/27), "hontractible"
  and "hamotopy" (134-4/85), "particubar" (134-6/93). Where a typed word has a doubled or unexpected letter and
  the print or the sense has the plain word, look for a darker cell, two shapes in one place, before writing both
  letters; then apply the rule above.
- **Typing errors:** both earlier readers corrected them silently, writing the word they recognised (64 of 118 places).
  Read letter by letter the words you recognise at once: a typed word may be misspelt, and it stays misspelt.
- **What the machine cannot type:** a doubled capital typed for a double-struck letter, or an x for ×. Enter the keyed
  form once in the notation table, and do not doubt it at each place.
- **A double-struck letter inside a French word** (po$\mathbb{l}$arisations, m$\mathbb{i}$xtes) is an artefact of the
  first reading: read it as the plain letter.

**Small things that were changed often.**
- **Accents:** an accent is one short stroke whose slant need not tell acute from grave. Where a stroke is there, write
  the accent the word has in French; note a missing accent only where no stroke is there.
  A proper name's accent is read on each leaf: Teichmuller and Teichmüller both occur (SP78).
- **Letters of one cote in formulas:** on cote 156-3 a capital E in a formula may be his ε; compare it with an ε of
  the same page.
- **Page numbers:** look at the head of the sheet for his own page number before the first line. Earlier readings left
  it out on many pages.
- **Formula numbers:** his formula numbers stand at the left of the formula. Write them as the conventions do; their side
  is set once for the edition.

**His short words** (40 places of Les Dérivateurs checked on the ink against the printed edition, 24 Nov 2026).
- **de, des, du and « ds » (dans)** are often a d with a short tail in his fast hand. An e-loop after the d gives de or
  des (157-4/375 « sont des Cof_W »); two humps, or an s-curl right after the d, gives dans or his « ds » (157-3/191,
  157-2/344); a bare d with no tail is de (157-4/278). Where the shape is only a d and a flat stroke, the ink does not
  decide: write `\unsure{…|…}` with the reading the mathematics needs first (dans before a class or category such as W
  or Cof_W, du before a singular noun). His « ds » stays « ds ». Where earlier readings have « de » and the print
  « dans », about a third were misreadings.
- **« sch.lie » is scholie** (a reduced o), never « salade »; it follows « théorème » or « th. » and a number (157-3/268,
  270, 276).
- **canulé** (« je me suis canulé ») is c, a round letter, two humps, l, é; « coulé » has one hump less (157-1/71,
  157-2/15, 157-2/347).
- **donc and alors:** « donc » is a d and a wave ending in a down-stroke, with no ascender; « alors » begins with a tall
  a-l. The printed edition has « alors » at places where « donc » is plain (157-1/84, 157-2/42, 157-4/165): the ink
  decides.
- **pas and par** are both a p and a flat tail: read them by sense. The printed edition has « par » where the same shape
  reads « pas » in the next line (157-2/169).
- **An article follows its noun:** where le, la, les, du or des differs from another witness, read the noun after it
  first, its number, gender and the word itself (157-2/170 « caractère »; 157-1/28 « du produit »).

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
- **Adding a doubt.** A doubt mark you add, a change of certainty alone (1,237 of the 6,439 changes were such), is one
  line in the doubts file and needs no crop. Resolving a doubt mark is a reading, and it needs its crop (above).
- **Crops.** One crop for each place the halves leave open and for each place that always gets one (method, step 2c);
  no second crop of a decided place outside the second reading (method, step 7); no TeX compilation.
- **A crop that decides** is at most 40 % of the scan's width, cut from the full-resolution scan and enlarged, never
  shrunk; a strip of a whole line is a page view and decides nothing (on earlier returns 36 % of the decisions had
  no such crop, and they are read again). Record each crop's box in scan pixels.

**The leaf in its folder.** The passes keep the scan order and record what lies on one page; they rarely see what
spans pages. Of 130 codicological findings by Michel Hua's project (its review campaign of 24 Nov 2026, credited to it),
checked on our scans and readings (90 confirmed, 24 partly, none refuted), our record had caught 28 outright; most of the
rest were page order, and in most of those our own transcription already held the evidence. Run these checks over the
whole package before the last page is finished. Record what they find in the notes; the transcription keeps the scan
order.
1. **His numbers against the archive order.** Record his page, sheet, typescript and formula numbers and the archivists'
   pencil number on every page; where they run out of step with the scans, give the reading order (cote 48: a typescript
   "(30" filed before its "(29").
2. **Joins.** Compare the last words of each page with the first words of the next page and of the two after it: a
   sentence that resumes two scans later marks a reversed pair or an interposed leaf (161-3; 82/16 continues on 82/18).
3. **Gaps.** Note pencil-number jumps, gaps in his pagination, and pages that stop with nothing to continue them (129:
   pencil 80 then 83; cote 6: eleven ahead).
4. **A leaf of another text.** A typescript, printed or photocopied leaf, or a leaf on another subject, with its own
   pagination or section numbers: name it (which work, which section), say whether its numbering belongs to another
   series, and do not treat it as a draft of the folder. Where it copies a printed text, the printed text is a second
   witness for the reading (127/9 is EGA IV 21.10; cote 136 carries the typescript of SGA 7 I IX on 89 scans).
5. **A leaf that continues a text elsewhere.** A leaf outside the numbered series, on another subject, or opening
   mid-sentence: look for its text in the neighbouring pages and cotes (151, p. 17 continues "Hyperrecouvrements";
   161-4 continues 161-6).
6. **Versos.** Identify the typescript or printout on the back by its numbers; its order often explains the binding
   order (55/10 and 55/12).
7. **A second ink or another hand.** A paler ink, pencil, red or blue margins are a later campaign until shown otherwise:
   record them as a layer. Name another hand even when it cannot be attributed (66: the list in brown ink, the margins in
   pale grey; 81: a school hand).
8. **Dating from the paper.** Letterhead, listing paper, stamps, notices and printouts date the paper, not the writing:
   an earliest date only. Describe it and record the date; copy no personal data (64/157: a notice of June 1981; 148/39:
   a printout dated 11-06-82).
9. **A page or drawing crossed out whole** is one deleted block and its own thread: keep it in place, follow the live
   text across it, and say what replaces it (35: a dependency graph struck and redrawn as two; 130/46 and 130/48).
10. **A revision sheet** ("la feuille jointe", marked as such in a margin) revises the text it annotates: note which
    passages it withdraws (4/2).
11. **The folder against its inventory.** Note once where the content does not match the inventory's title, series, page
    count or date range (159, filed under Dérivateurs, is on connections on curves; the wrapper of 26 says "V" where the
    inventory says EGA VI).

**The hand log: learn his hand as you read.** Keep `SR06_10_hand_log.md` from the first page. Enter every habit of his
hand or his notation that can mislead a reader: a letter he forms like another (a p like an n, a u like an n, a ζ like a
ξ), a sign he draws like another, a notation of his own. For each habit, record:
- the pages where you met it;
- whether it holds at every occurrence of that letter or sign on these pages;
- the places where witness C or witness H misread because of it.

Once a habit holds, read every later occurrence of that letter with it in mind, and confirm each one on the ink. The log
is returned with the transcription, so that the next runs start from it.

## Our conventions

Use exactly the macros of `PREAMBLE.tex` and the conventions of the pages you are given: `\cotefile{…}` (the cote)
and `\scanpage{…}` (the scan number), `\mspage{…}` (his own page number), `\deleted{…}`, `\inserted{…}`, `\margin{…}`, `\uline{…}`, `\uuline{…}`, `\diagram{…}` in
`tikz-cd`, `\figure{…}` in TikZ, `\unsure{reading}`, `\unsure{reading|alternative}`, `\illegible{n}`, and the other macros
that preamble defines.

1. **Transcribe only what you see,** in his language (mostly French, sometimes English or German). No translation, no
   modernization, no correction: his spelling, accents (or their absence), punctuation, abbreviations ("cat.", "gr.",
   "resp.", "cf.", "th.", "prop.", "dém.", …) and his own numbering exactly as written. Never expand an abbreviation in
   the text.
2. **Mathematics exactly as written**: the same letters, alphabets, indices, exponents, arrows, bars, hats and tildes.
   An exclamation-mark exponent is `^!`, a prime is `'`; read which one the ink shows, every time.
3. **A diagram is typeset, never described**, with every object, arrow, label, direction and decoration, including
   struck parts, in `tikz-cd`.
4. **Doubt is marked in place, never resolved by a guess,** and a mark of doubt is never a reason to leave something
   out. The first reading in `\unsure{a|b}` is what the ink shows, not the expected form. `\illegible{n}` only for ink
   that is physically unreadable at the highest zoom, never for a symbol inside a formula or a diagram.
5. His double quotation marks are two backticks and two apostrophes; « » only where he drew guillemets.

**Check events.** For every statement your work checks, uses or refutes (here a statement is a box of a page, by its
id), record its check events in `CHECK_EVENTS.tsv`, one row per event: statement id, date, who (model, effort, run),
type (targeted proof check / independent re-proof / computation or formal certificate / used and rechecked in this run /
carried as background without fault found / refuted, with the refined statement's id), outcome. Give each event the type
of what actually happened, neither more nor less: reading a box is not a check of it. `CHECK_EVENTS.tsv` goes into every
checkpoint and into the final ZIP.

## Page files: what they hold

These rules hold wherever another section of this prompt says less.

- **`edited_pages/` holds finished pages only.** Keep a page in work in `drafts/`. Move it into `edited_pages/` when you
  write its line `scan NNN audited <current UTC time> cote <cote>` in the progress log, never before. A page file without that line is taken as
  not done (an earlier run left an undecided page there, and it was counted as finished).
- **His writing is text, wherever it stands on the sheet.** Lists, columns, notes beside one another and struck
  blocks are set as text, as a table or as margin notes, in reading order. A TikZ picture holds a drawing's
  lines and that drawing's own labels, nothing else. A drawing is drawn stroke by stroke, never traced from
  the pixels.
- **Page files carry no records.** Readers' candidates, crop coordinates, reasons and provenance go to the
  logs, not into TeX comments. The only comments in a page file are those this prompt names.
- **A printed administrative list of other people on a reused sheet** (names, personal numbers) is not his
  text: do not copy it, whatever a witness has. Transcribe his own writing on that sheet in full, and record
  the scan in the notes as `reused sheet: personal list`.

## What to return

Two files, offered as downloads: `SR06_10_final.zip`, which holds everything below, and `SR06_10_crops.zip`, the one crop dump (under Checkpoints). It holds:

1. **`placements.tsv`**, one row per difference decided and per other misreading found, in page order, with the
   columns `id` (`<page>-<box>`, or `<page>-x<n>` for a place outside the boxes), `cote`, `scan`, `decision` (a or b),
   `find` (for a: the exact span of the page as given, long enough to stand once on it), `replace` (for a: the same
   span as the ink shows it; empty for b), `first` (the text's reading of the box), `second` (the blind reading),
   `what_the_ink_shows` (the strokes you saw, with the crop's file name and box) and `confidence` (high, medium, low).
2. **`edited_pages/`**: every page of this piece after its changes, named as given.
3. **`second/`**: for every page its box list, the text's readings of the boxes and the blind readings.
4. **`SR06_10_notes.md`**: the notation table; every place where his own slip or his notation decided a reading, with what
   is written and what he meant; and a short note on the boxes the ink did not settle.
5. **`SR06_10_hand_log.md`**: every habit of his hand or his notation that misled the text or a witness on these pages, with
   its pages, whether it holds at every occurrence, and the places it decided.
6. **`crops/`**, **`CHECK_EVENTS.tsv`** and **`progress.log`**.
7. **`SR06_10_print.tsv`, the print list,** for the pages with witness P: one row per row of
   `SR06_10_text_P_differences.tsv` and per further place where the page as edited differs from witness P, with the columns
   `page, line, words_before, print_reading, text_reading, final_reading, scan_shows, verdict, crop, confidence`;
   `verdict` is one of `misreading of the text, corrected`, `earlier state`, `abbreviation, slip or typing error kept`,
   `error of the print`, `made by the comparison`, `undecided`.

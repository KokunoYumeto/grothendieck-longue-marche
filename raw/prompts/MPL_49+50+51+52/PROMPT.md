# Transcription task MPL_49+50+51+52: Alexander Grothendieck, manuscript notes from the Montpellier archive, cotes 49, 50, 51 and 52

You are transcribing mathematical notes in Alexander Grothendieck's own hand. The attached zip `MPL_49+50+51+52_scans.zip` holds
**58 scan pages** from 4 files of the Montpellier archive, separate folders of notes, in this
order:
- `49.pdf`: "Picard des schémas abéliens : notes manuscrites (s.d.)." (s.d.), scans 1-10, 10 pages kept
- `50.pdf`: "Sur bouquin Lang : notes manuscrites (s.d.)." ([à partir de 1965][42]), scans 1-11, 11 pages kept
- `51.pdf`: "" Bonne réduction " (Shimura-Koizumi) : notes manuscrites (s.d.)." (s.d.), scans 1-23, 23 pages kept
- `52.pdf`: "Théorème de Torelli : notes manuscrites (s.d.)." (s.d.), scans 1-14, 14 pages kept

Transcribe the files in this order. For every scan page N of file C there are three images: `MPL_49+50+51+52_C_scanNNN.jpg` (the
whole page) and `MPL_49+50+51+52_C_scanNNN_a.jpg`, `MPL_49+50+51+52_C_scanNNN_b.jpg` (its top and
bottom halves, or left and right halves of a landscape sheet, overlapping a little, at full resolution). N is the page
number in that file's PDF. The images are contrast-enhanced and sharpened. Scan pages that are blank were left out:
none.

Unzip the file in your sandbox and **look at every image yourself**, the whole page first and then the halves for
the small writing. Reading software (OCR) is not a substitute for looking and must not be used on these pages.
A second zip, `MPL_49+50+51+52_context.zip`, is for the research notes at the end. Leave it closed until the transcription is
finished (see "After the transcription" below).

**Questions for the notes.** Answer these in the research notes, after the transcription is frozen; they never steer a reading, and the transcription never changes because of them. A guess to test: these short notes are the research end of his work on abelian varieties, like cotes 47 (a Fourier transform on abelian schemes) and 44 (intermediate Jacobians). Is there a second witness of 47 with its compatibility check done? Our own question: do 51 (good reduction) and 52 (Torelli) hold the proof for abelian varieties he recalls in 1983 ("je l'ai démontré, dans le contexte des VA, il y a belle lurette !")? The README in the context zip says more.

The handwriting is fast and hard. Your job is a **diplomatic transcription into LaTeX**: exactly what is on the
page, in Grothendieck's language (mostly French, sometimes English or German), nothing more and nothing less.
Besides the transcription, you keep **research notes** on what these pages leave open (item 4 at the end).

**The task is a complete transcription: every word, symbol, formula, diagram, drawing, deletion, insertion and
marginal note on every page, in the order on the page.** Anything left out is an error. Accuracy is required as
well: a wrong confident reading is worse than an honest mark of doubt, but a mark of doubt is never a reason to leave
something out. Take the time this needs. Work page by page and line by line.

**A description is not a transcription.** You never replace content by a description, a summary, a paraphrase,
"[...]", "etc.", "and so on", or a note that something is there. You never include an image. If you cannot read
something, you transcribe what you can and mark the rest with the doubt macros (rule 5), in place.

## Absolute rules

1. **Transcribe only what you see.** Do not fill in from memory, from published texts, from what the mathematics
   "should" say, or from your knowledge of Grothendieck's published work. If the page says something surprising,
   transcribe the surprise.
2. **No translation, no modernization, no correction.** Keep his spelling, accents (or their absence),
   punctuation, abbreviations ("cat.", "gr.", "resp.", "cf.", "th.", "prop.", "dém.", …) and his own numbering
   ("N° 3", "Prop. 1.7", "§ 2") exactly as written. Never expand an abbreviation in the text.
3. **Mathematics exactly as written**, in LaTeX: the same letters, the same alphabet (script, Gothic, bold, Greek),
   the same indices and exponents, the same arrows, bars, hats and tildes. Do not "fix" notation. If a symbol could
   be two things, mark it (rule 5).
4. **Mark the state of the page**, with these macros only:
   - `\cotefile{C}` before the first page of each archive file C (for example `\cotefile{49}`);
   - `\scanpage{N}` at the top of each scan page (N as above, the page number within its file);
   - `\mspage{n}` where Grothendieck's own page or sheet number is visible;
   - `\deleted{…}` for struck-through text you can still read; `\deleted{\illegible{2}}` if you cannot;
   - `\inserted{…}` for words added above the line or in the margin and meant to go in at that place;
   - `\margin{…}` for marginal notes that are not insertions;
   - `\uline{…}` for underlined words; keep double underlining as `\uuline{…}`;
   - `\diagram{…}`: every diagram typeset in `tikz-cd` (or an array for a table), with every object, arrow, label,
     direction and decoration exactly as written, including struck-out parts (`\deleted` inside the diagram). A
     diagram is **never** described in words; if part of it is hard to read, typeset it anyway and put `\unsure` or
     `\illegible` inside the diagram at that place;
   - `\figure{…}` for drawings that are not diagrams (curves, graphs, regions, pictures): **reproduce the drawing in
     TikZ**, with its shape, the relative positions of its parts and every written label, as closely as you can. A
     verbal description of a drawing is not allowed. Only if a drawing is a genuine picture too complex for TikZ (not
     text, not a formula, not a diagram), give your best TikZ approximation and add the comment
     `% crop-candidate: scan N` after it.
5. **Doubt, explicitly:**
   - `\unsure{reading}` for a reading you believe but are not certain of;
   - `\unsure{reading|alternative}` when two readings are possible;
   - `\illegible{n}` for n words whose ink is physically unreadable at the highest zoom (estimate n). Before you use
     it, try a reading and prefer `\unsure{…}`. Never use it for a symbol inside a formula or a diagram: give your
     best reading there with `\unsure`.
   - In `\unsure{reading|alternative}` the first reading is what the ink shows, not the expected form: his spelling
     ("standart", not "standard"), his agreement ("défini" where he wrote it so), a plain dash where he drew no
     arrowhead. A correction of his text belongs in a research note, never in the transcription.
   Never silently guess.
6. Keep his paragraphing and the order of the text on the page. Line breaks inside a paragraph need not be kept.
   A page that is not mathematics (a letter, an envelope, a printed sheet, a form) is transcribed all the same.

## Where readings go wrong

On his manuscripts about one word in seventy was misread in earlier work of this kind, and only a third of the
misreadings carried a doubt mark. The typical errors, to guard against:
- **A plausible mathematical word in place of the ink.** The context makes the wrong word look right. If you have not
  seen every letter of a word, mark it `\unsure`, however well it fits.
- **A short condition or symbol left out**: a "≠ 0", an inclusion sign between two lines of a display, an "Ob",
  inner parentheses. After each display, margin note and insertion, check symbol by symbol that everything on the
  page is in your text.
- **An insertion attached to the wrong place.** Put each insertion where its caret, arrow or line points.
- **Inequalities and arrow directions.** ≤ and ≥, ⇒ and ⇐, the direction of an arrow, of an inclusion and of an
  isomorphism: read them from the ink, never from what the argument needs.
- **His own spellings, and word endings.** Write the form on the page, not the dictionary form. Read each ending
  (singular or plural, -é or -er, -ant or -ent) from the ink, not from the grammar; if the ending is only a stroke,
  mark the word `\unsure`.
- **A struck word read as live text.** Before you write a word as live text, look for a line through it; a struck
  word goes in `\deleted{…}`, however clear it is. Write the word when he writes the word and the symbol when he
  writes the symbol: a struck "tout" is neither live text nor "∀".
- **Letters and digits that look alike**: E and F, 3 and 5, u and n, an index 1 and l. Read them from the ink; if the
  stroke does not decide, mark them `\unsure`.
- **An abbreviation written out** ("mb." as "membre"): write exactly the letters on the page.
- **Signs read differently in different parts of a package.** In the third package of this archive the pages were
  split among parallel workers that did not share their readings: two of them wrote his exclamation-mark exponent
  (`D^!_d`, `f^!`) as a prime, unmarked, on twenty scans, and the workers wrote his quotation marks in two different
  ways. An exclamation-mark exponent is `^!` and a prime is `'`: read which one the ink shows, every time. Write his
  double quotation marks in LaTeX as two backticks and two apostrophes (``...''); write « » only where he drew
  guillemets.

The pages done fastest are where errors cluster. In the first package of this archive, the pages finished in the
first minutes had three times as many errors as the later ones, and two thirds of all errors carried no doubt mark.
Read the first page as slowly as the last.

## Method

1. Before the first page, write the current time (UTC) as the first line of `progress.log`.
2. For each scan page: read the whole page once, then transcribe it line by line. Re-read the image (and its halves)
   against your transcription, line by line; correct, or mark doubt. Then make the page **inventory**: every text
   block, display, diagram, drawing, margin note, insertion and deletion on the page, top to bottom, and check that
   each one is in your transcription, complete. Fix any gap.
3. **As soon as a page is done**, write it to its own file `pages/MPL_49+50+51+52_C_scanNNN.tex`, add its rows to the inventory
   file, and append a line `C scan NNN done <current UTC time>` to `progress.log`. Only then go to the next page. If the
   work is interrupted, everything finished so far is on disk.
4. If the mathematics tempts you to fill in, complete or correct a reading, do not: put that thought in the research
   notes (item 4 below), never in the transcription.
5. **One stream, one notation.** Transcribe the pages yourself, in one stream, in the order given: do not split
   them among parallel workers or sub-agents. When the pages of an earlier package of this archive were split among
   workers, the same signs were read in different ways and the errors went unmarked. Keep one notation table for the
   package from the first page on: his recurring signs and exponents, the letters of each alphabet, his quotation
   marks and abbreviations, each with how it is written in LaTeX. Before the transcription is final (and before any
   context is opened), compare how each recurring sign was read across all the pages, check every difference
   against the ink, and make the readings agree. Put the table at the top of the doubts file.
6. **If the execution environment disconnects.** Wait for it and retry for at least 10 minutes. If it does not come
   back, the work must still reach us, so write it out in this chat as text: every file in full, each in its own
   code block headed by its file name. That means every page file finished so far (the code you ran to save each
   page contains its text: take it from there), the progress log, the inventory rows, the doubts table and the notes
   so far. Then go on transcribing, directly in the chat and in the same form, every further page you can still see,
   and then write the research notes. Say at the start which pages are done, which are not, and which images you can
   no longer see. An answer that only reports the disconnection, describes the checkpoint or asks for the files
   again, without writing out the work, is not acceptable.
7. **Checkpoints that survive a disconnection.** After every ten finished pages, save a checkpoint ZIP of
   everything so far (page files, inventory, progress log, doubts) to the user's Library, or wherever files survive
   the loss of the execution environment, named `MPL_49+50+51+52_checkpoint_NNN.zip`, where NNN is the last finished scan.
   Save the final ZIP there too.
8. **A second reading of every page, then a frozen transcription.** When every page is done, read each page once
   more against its image, as a second reader would: correct, or mark doubt, and append
   `scan NNN audited <current UTC time>` to `progress.log`. Then write the SHA-256 of each page file and of the
   combined transcription to `progress.log` with the line `transcription frozen <current UTC time>`; only then open
   the context zip, if there is one. At the end, check
   that the hashes are unchanged and say so in `progress.log`.

This task is long by design: 58 pages, then the research notes. Work through all of it completely; do not stop
at a sample or a plan, and do not ask whether to continue. Ignore any clock. The notes are half of the task, not an
afterthought: in earlier work of this kind they found conjectures, gaps and links that matter. When the last page is
written, give them real time.

## After the transcription: the notes, with our earlier work as context

The second zip, `MPL_49+50+51+52_context.zip`, holds what we already have on the neighbouring material: a short README with our guess about this folder, made from its title before anyone read it, for your notes to confirm or refute.
Do not open it before the transcription is finished. When every page file is written, append the line
`context opened <current UTC time>` to `progress.log`; only then unzip it and read its `README.md`.

Use it for the research notes only:
- for each note, search the context for the same objects, notation and words (grep works well on these files), and
  say where our materials already have the point (file and scan) and whether these pages add to it, restate it,
  differ from it or contradict it;
- add notes for links between these pages and the context that he does not make on these pages;
- the notes in the context are leads from earlier runs, not results: never cite one as established.

**The transcription does not change after you open the context.** If the context suggests a different reading of
something on these pages, leave the transcription as it is and record a reading question in the notes (scan, line,
your reading, the reading the context suggests, and why).

## What to return

One zip file, `MPL_49+50+51+52.zip`, offered as the only download. It holds:

1. `MPL_49+50+51+52_transcription.tex`: all pages in order, one LaTeX fragment (no preamble, no `\documentclass`), starting with
   `\cotefile{C}` and `\scanpage{N}` of the first page, using only the macros above plus standard LaTeX and `tikz-cd`; and the folder
   `pages/` with one file per page.
2. `MPL_49+50+51+52_doubts.md`, in English (the readings as on the page): a table of doubts (file, scan page, line approximately, your
   reading, the alternatives, your confidence high / medium / low); the abbreviations met, each with what you think it
   stands for (in this list only, never in the text); and a short honest note on how legible these pages were and
   which parts you trust least.
3. `MPL_49+50+51+52_inventory.csv` (columns `cote,scan,sheet_kind,element,kind,position,first_words_or_objects,transcribed`): one row per
   element of every page (kind: text, display, diagram, drawing, margin note, insertion, deletion), with
   `transcribed` = yes for every row. A row that is not yes means the transcription is not finished. The column `sheet_kind` says what the sheet is: `text` (his notes on the subject of the folder), `reused_typed`
   (a typed page of another text that he wrote on or whose back he used), `cancelled_draft` (a draft of his own that
   he struck through), or `cover` (a folder cover or title sheet). A reused or cancelled sheet is still transcribed in
   full.
4. `MPL_49+50+51+52_notes.md`: **research notes**, in English, kept apart from everything above. Note what in these pages is
   worth studying further:
   - **Grothendieck's own conjectures, questions and expectations**: a "?", "il est probable que", "je conjecture",
     "il serait intéressant de", "on devrait pouvoir", a hope or a doubt he writes down;
   - **claims stated without proof** or left for later ("on verra", "il est facile de voir", "sans doute",
     "on peut montrer"), and what a proof would need;
   - **implications he does not pursue on these pages**: consequences, special cases, links to other parts of
     mathematics or to known results;
   - **your own ideas**: what might follow, what might be false, an example or construction worth trying, a link he
     does not make. Label these clearly as yours.

   Two standing questions, answered for every package in a short section of their own: **which steps the manuscript
   itself marks as unverified** ("à vérifier", "sauf erreur", "je présume", "admis", "il faudrait vérifier", a "?" on a
   step), each with its scan and his words; and **which title sheets and page counts it carries** (a title, a "19
   pages", a "Pages 1–67" on a sheet or cover), each with its scan, since texts inside one cote have their own.

   One note per item: file and scan page (and line if you can), kind (conjecture / unproved claim / unpursued implication /
   own idea / reading question / self-flagged: a step he himself marks as unverified / withdrawn in the same text: a
   statement he corrects or retracts later in these pages, with both scans), the note in one to four sentences, and for your own ideas your confidence and your
   reason. When a note is about something he wrote, quote his words briefly. He may take a point up later in the
   file or elsewhere in the archive: note it anyway, because every note is checked against the rest of the
   manuscripts and the literature. Do not present an idea as established or as new. The notes never change the
   transcription.
5. `progress.log`.

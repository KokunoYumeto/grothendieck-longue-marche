**This file is the task: carry it out in full, now. The other attached files are its materials.**

# Transcription task {ID}: Alexander Grothendieck's papers, Montpellier archive, cote {COTE}, {COUNT} scan pages

You are making a **diplomatic transcription into LaTeX** of {COUNT} scan pages from the Montpellier archive of
Alexander Grothendieck: the file `{COTE}.pdf`, "{TITLE}" ({DATE}). The pages are scans {SCANS} of that PDF, in this
order. {MATERIAL} The language is mostly French, sometimes English or German: keep the language of the page.

The attached zip `{ID}_scans.zip` holds, for every scan page N (its page number in the archive's PDF), four images:

- `{ID}_{COTE}_scanNNN.jpg`: the whole page, for the layout;
- `{ID}_{COTE}_scanNNN_s1.jpg`, `_s2.jpg`, `_s3.jpg`: the top, middle and bottom thirds of the same page (left, middle
  and right thirds of a landscape sheet) at full resolution, overlapping a little, for small writing, indices,
  exponents, accents and corrections.

`MANIFEST.tsv` lists every image with its size, SHA-256 and scan. The images were taken from the archive's PDF
(https://grothendieck.umontpellier.fr/{COTE}.pdf), contrast-enhanced and sharpened.

**Look at every image yourself** with your image-viewing tool: the whole page first, then the three thirds. Reading
software (OCR, a PDF text layer, any text-recognition library) is not a substitute for looking and must not be used.
If you cannot view the images, stop at once and say so in your final message; do not produce a transcription by any
other means.

**The task is a complete transcription: every word, symbol, formula, diagram, drawing, deletion, insertion and
marginal note on every page, in the order on the page.** Anything left out is an error. Accuracy is required as
well: a wrong confident reading is worse than an honest mark of doubt, but a mark of doubt is never a reason to leave
something out. Take the time this needs. Work page by page and line by line.

**A description is not a transcription.** Never replace content by a description, a summary, a paraphrase, "[...]",
"etc.", "and so on", or a note that something is there. Never include an image. If you cannot read something,
transcribe what you can and mark the rest with the doubt macros (rule 6), in place.

## Absolute rules

1. **Transcribe only what you see.** Do not fill anything in from memory, from published texts (some of this material
   was later printed or transcribed elsewhere; do not look for, use or reproduce any such text), from what the
   mathematics "should" say, or from your knowledge of Grothendieck's work. If the page says something surprising,
   transcribe the surprise.
2. **No translation, no modernization, no correction.** Keep the spelling, accents (or their absence), punctuation,
   abbreviations ("cat.", "resp.", "cf.", "th.", "prop.", "dém.", ...) and numbering ("N° 3", "Prop. 1.7", "§ 2")
   exactly as written or typed. Never expand an abbreviation in the text. A slip of the pen or a typing error stays as
   it is on the page; list it in the doubts file (deliverable 2), never correct it in the text.
3. **Mathematics exactly as written**, in LaTeX: the same letters, the same alphabet (script `\mathscr`, calligraphic
   `\mathcal`, Gothic `\mathfrak`, bold, blackboard `\mathbb`, Greek), the same indices and exponents and their
   placement, the same brackets, signs, arrows, bars, hats, tildes, dots and primes. Nothing is simplified, expanded
   or rewritten. Do not define your own notation macros. **Typescripts have no bold type.** A typed letter struck
   twice, or typed over itself so that it looks heavier or doubled, is a double-struck letter (`\mathbb{R}`); a
   letter written in by hand on a typed page is read from its own strokes (a hand-drawn double stroke is `\mathbb`, a
   script capital `\mathscr` or `\mathcal`). Decide every such letter on its own crop: check every capital in a
   heading or in a functor name (R, L, D, H, ...) for double striking separately; a notation-table entry made for the
   body of the text does not cover a heading.
4. **Mark the state of the page**, with these macros only (they are defined in the attached `PREAMBLE.tex`):
   - `\cotefile{{COTE}}` once, at the very start; then `\scanpage{N}` at the top of each scan page (N as above);
   - `\mspage{n}` where a page or sheet number of the text itself is visible: his own numbering, or the typed page
     number of a typescript ("- 16 -"); a document number typed at the top ("n° 296") is typed text and is
     transcribed. The archive's own pencilled sheet number in a lower corner is not part of the text: note it only as
     a comment line `% archive sheet number: NN`;
   - `\handwritten{...}` for words or symbols written by hand on a typed page (inside a word or formula, around the
     handwritten part only);
   - `\deleted{...}` for struck-through or typed-over text you can still read (typed `xxxx` over a word included);
     `\deleted{\illegible{2}}` if you cannot;
   - `\inserted{...}` for words added above the line or in the margin and meant to go in at that place, where the
     caret, arrow or line points;
   - `\margin{...}` for marginal notes that are not insertions;
   - `\uline{...}` for underlined words; double underlining is `\uuline{...}`;
   - `\diagram{...}`: every diagram typeset in `tikz-cd` (or an array for a table), with every object, arrow, label,
     direction and decoration exactly as on the page (inside the macro write
     `\begin{tikzcd}[ampersand replacement=\&]` and separate the cells with `\&`, or the diagram will not compile),
     struck-out parts included (`\deleted` inside the diagram). A diagram is **never** described in words; if part of it is hard to read, typeset it anyway with `\unsure` or
     `\illegible` inside the diagram at that place;
   - `\figure{...}` for drawings that are not diagrams (curves, regions, pictures): **reproduce the drawing in TikZ**,
     with its shape, the relative positions of its parts and every label. Only for a genuine picture too complex for
     TikZ, give your best TikZ approximation and add the comment `% crop-candidate: scan N`;
   - displays: `\[ ... \]`; a display on several lines: `\begin{aligned} ... \end{aligned}` inside `\[ ... \]`, broken
     where the page breaks it; a display label as written: `\tag*{<label>}`;
   - a printed letterhead or printed form on the sheet is text: transcribe it, with the comment line `% letterhead`
     (or `% printed form`) above it. Library or archive stamps are noted only as `% stamp: <what it is>`.
5. **Letters.** For a letter, transcribe the place and date, the salutation, the body, the closing and the signature
   as written, in their order and lines; an address or a note added by the recipient is transcribed where it stands
   (`\margin{...}` if it is in the margin). Who wrote the sheet (Grothendieck or a correspondent, by hand or typed)
   goes in the inventory (deliverable 3), not in the text.
6. **Doubt, explicitly:**
   - `\unsure{reading}` for a reading you believe but are not certain of;
   - `\unsure{reading|alternative}` when two or more readings are possible: list **every** candidate the ink allows
     (`\unsure{E|F}`, `\unsure{3|5}`), the first being what the ink shows, not the expected form: his spelling
     ("standart", not "standard"), his agreement, a plain dash where he drew no arrowhead. If the surrounding text
     favours another candidate, say so in the doubts file; never change the reading for it. Do not mark a glyph whose
     shape decides it;
   - **a recurring ambiguous glyph** (the same letter or sign that could be ℰ or 𝒞 every time it occurs): record the
     doubt once in the notation table, with every candidate, and mark it `\unsure{...|...}` at its **first occurrence
     on each page**; its other occurrences on that page are written with the first candidate, unmarked;
   - `\illegible{n}` for n words whose ink is physically unreadable at the highest zoom (estimate n). Before you use
     it, try a reading and prefer `\unsure{...}`. Never use it for a symbol inside a formula or a diagram: give your
     best reading there with `\unsure`.
   Never guess silently, never leave a gap.
7. Keep the paragraphing and the order of the text on the page. Words hyphenated at a line end are joined; hyphens
   that belong to the word stay. One blank line between paragraphs; line breaks inside a paragraph are not kept
   (except in the lines of a letter's heading, closing and signature, which end with `\\`).

## Where readings go wrong

On Grothendieck's manuscripts about one word in seventy was misread in earlier work of this kind, and two thirds of
the misreadings carried no doubt mark. On typed and printed pages the error rate is lower, and the errors that remain
are of a few known kinds. Guard against all of them:

- **The expected word in place of the written one.** A typescript of a related series had "soit èxact à gauche" with
  a grave accent; the transcription wrote "exact" with no mark. Another had "le même resultat vaut", "la
  divisibilitié des", "par voie I-adique" (a capital I) and "(á paraître)"; the transcription wrote résultat,
  divisibilité, l-adique and à paraître. **Read every word letter by letter; check which way each accent points and
  whether it is there at all; tell I, l and 1 apart.** A word that looks right to you is where the risk is. Write
  what is on the page and list the slip in the doubts file.
- **A plausible mathematical word in place of the ink**, on handwritten lines and handwritten corrections: if you
  have not seen every letter of a word, mark it `\unsure`, however well it fits. Read each ending (singular or plural,
  -é or -er, -ant or -ent) from the ink, not from the grammar.
- **A short condition or symbol left out**: a "≠ 0", an inclusion sign, a subscript on one of several equal letters,
  inner parentheses, a minus sign, a dual or a star, an "Ob". After each display, margin note and insertion, check
  symbol by symbol that everything on the page is in your text.
- **A handwritten correction on a typed page attached to the wrong place, or left out.** Typed pages in this archive
  carry his corrections: words crossed out by hand, words typed over with x, carets with an insertion above the line,
  symbols filled in by hand in blanks the typist left. Every one goes in, at its place, with its macro.
- **A struck word read as live text.** Before you write a word as live text, look for a line through it.
- **i and j, and other look-alikes, in indices and exponents**: j has a descender and i does not; index `1`, `l`, `i`
  and `\ell`; `v` and `\nu`; `n` and `\eta`; `u` and `\mu`; `\epsilon`, `\varepsilon` and `\in`; `\phi` and
  `\varphi`; `o`, `0` and `\circ`; E and F; 3 and 5; u and n; script, calligraphic and roman capitals; `*`, `\bullet`
  and `\cdot` in exponents; an exclamation-mark exponent `^!` and a prime `'`; prime and comma; tilde, bar and hat.
  Read each from the ink, one by one, even where the line above has the other; if the ink does not decide, mark it.
- **Directions**: `\leq` and `\geq`, `\Rightarrow` and `\Leftarrow`, the direction of every arrow, inclusion and
  isomorphism, upper and lower indices (`H^i` and `H_i`, `f_*` and `f^*`, `f_!` and `f^!`): from the ink, never from
  what the argument needs.
- **Quotation marks**: his double quotation marks are written ``...'' (two backticks, two apostrophes); « » only
  where guillemets are drawn or typed.
- **Accents and French text**: é and è, à and a, ô and o, ç; accents on capitals exactly as on the page.
- **The first pages done fastest.** In earlier work of this kind the pages done in the first minutes had three times
  as many errors as later ones. Read the first page as slowly as the last.

## Method

1. Unpack `{ID}_scans.zip` into your working folder and check its files against `MANIFEST.tsv` (names and SHA-256).
   Create the folder `out/` beside them, with its subfolder `pages/`, and copy the attached `PREAMBLE.tex` into
   `out/`. Read nothing but the attached files. No internet access is needed; do not search the web.
2. Write the current time (UTC) as the first line of `out/progress.log`.
3. For each scan page, in order: read the whole page once, then transcribe it line by line from the three thirds.
   Re-read the images against your transcription, line by line; correct, or mark doubt. Then make the page
   **inventory**: every text block, letter part, display, diagram, drawing, margin note, insertion, deletion and
   handwritten addition on the page, top to bottom; check that each one is in your transcription, complete. Fix any
   gap.
4. **As soon as a page is done**, write it to its own file `out/pages/{ID}_{COTE}_scanNNN.tex`, add its rows to
   `out/{ID}_inventory.csv`, append a line `scan NNN done <current UTC time>` to `out/progress.log`. Saving these
   files is your checkpoint. Only then go to the next page.
5. **One stream, one notation.** Transcribe the pages yourself, in one stream, in order: do not split them among
   parallel workers or sub-agents. When the pages of an earlier package of this archive were split among workers,
   the same signs were read in different ways and the errors went unmarked. Keep a notation table from the first page
   on: the recurring signs and exponents, the letters of each alphabet, the quotation marks and abbreviations, each
   with how it is written in LaTeX. **Build every entry from the image, not from convention**, with the scan and line
   where you looked; for each recurring ambiguous glyph, its candidates (rule 6). The table is a set of readings, not
   facts: check each entry again on every new page. Before the transcription is final, compare how each recurring
   sign was read across all the pages, check every difference against the images, and make the readings agree where
   the page agrees.
6. **A second reading of every page, as a second reader.** When every page is done, read each page again from the
   start against its three thirds. This is a full reading, not a skim: in an earlier series a "second reading" of
   11-35 seconds per page found none of its six errors; a page needs several minutes. For each page, **first** read
   the crops line by line and write down, before you open the page file, every accent and every word that looks
   misspelled or unusual, as you see it in the crop; **then** open the page file and compare. Write a section per page
   in `out/{ID}_audit.md`: the start and end time (UTC); that list of words and accents from the crops; every display
   and inline formula, checked symbol by symbol (list them); every i and j in an index or exponent; every handwritten
   correction on a typed page and where it went; every double-struck or script candidate with what you saw; and every
   change made, as `before -> after` (or "no change"). Correct, or mark doubt, and append
   `scan NNN audited <current UTC time>` to `out/progress.log`.
7. **Assemble and check.** Write `out/{ID}_transcription.tex`: the page files in order, concatenated, as one LaTeX
   fragment (no preamble, no `\documentclass`). Write `out/{ID}_standalone.tex`: `\input{PREAMBLE.tex}`
   `\begin{document}` `\input{{ID}_transcription}` `\end{document}`. **Do not try to compile**: this sandbox has no
   working LuaLaTeX (earlier tasks of this kind spent their time building formats that could not work); we compile
   the return ourselves. Instead check with a short script that braces, `\[ \]`, `$ $` and environments balance in
   every page file, and fix what does not (the fix is syntax only and never changes a reading). Then write the
   SHA-256 of each page file and of the assembled file to `out/progress.log` with the line
   `transcription frozen <current UTC time>`. Then make `{ID}_out.zip` of the whole `out/` folder and offer it as a
   download.
8. **If time or context runs short.** If the environment tells you that time or context is running out, do not stop
   silently: at once write the assembled file, the doubts file and the inventory for the pages finished so far, list
   the unfinished pages in `out/progress.log` and in your final message, and offer `{ID}_out.zip` of what is finished
   as a download. Work that is not delivered is lost.

This task is long by design: {COUNT} pages, each read twice. Work through all of it completely; do not stop at a
sample or a plan, and do not ask whether to continue.

## What to deliver (all in `out/`, zipped as `{ID}_out.zip` and offered as a download at the end)

1. `pages/{ID}_{COTE}_scanNNN.tex`, one file per scan page, and `{ID}_transcription.tex`, the assembled fragment
   starting with `\cotefile{{COTE}}` and the `\scanpage` of the first page, using only the macros above plus standard
   LaTeX, `amsmath`, `amssymb`, `mathrsfs`, `tikz-cd`, `tikz`, `enumitem` and `ulem`; and `{ID}_standalone.tex`.
2. `{ID}_doubts.md`, in English (readings as on the page): the notation table (method 5) at the top; then a table of
   doubts (scan, line approximately, your reading, every alternative, confidence high / medium / low, and which
   candidate the surrounding text favours, if any, and why); then the slips kept as written (scan, line, as written,
   apparently intended, why); then the abbreviations met, each with what you think it stands for (in this list only,
   never in the text); then a short honest note on how legible these pages were and which parts you trust least.
3. `{ID}_inventory.csv` with the columns
   `cote,scan,sheet_kind,hand,element,kind,position,first_words_or_objects,transcribed`: one row per element of every
   page (kind: text, letter part, display, diagram, drawing, margin note, insertion, deletion, handwritten), with
   `transcribed` = yes for every row. A row that is not yes means the transcription is not finished. `sheet_kind` says
   what the sheet is: `text` (notes or a typescript on the subject of the folder), `letter`, `reused_typed` (a typed
   page of another text that he wrote on or whose back he used), `cancelled_draft` (a draft struck through), or
   `cover` (a folder cover or title sheet). `hand` says who wrote that element as far as the page shows it:
   `typed`, `Grothendieck` (his hand, as the folder's notes show it), `other hand`, or `unknown`.
4. `{ID}_audit.md`, the second reading page by page (method 6).
5. `{ID}_notes.md`, in English, two short sections answered from these pages only: **the steps the pages themselves
   mark as unverified** ("à vérifier", "sauf erreur", "je présume", "admis", "il faudrait vérifier", a "?" on a step),
   each with its scan and the words; and **the title sheets, dates and page counts they carry** (a title, a date, a
   "19 pages", the numbering of a typescript), each with its scan. Write "none" where there is none.
6. `progress.log`.

Your final message: the download link of `{ID}_out.zip`, the pages done and audited, the number of `\unsure`,
`\illegible` and `\deleted` marks, how the balance check came out, and any page that is not finished.

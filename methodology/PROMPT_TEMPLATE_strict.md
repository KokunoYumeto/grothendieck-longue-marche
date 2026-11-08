# Transcription task {PKG}: Grothendieck, *La Longue Marche à travers la théorie de Galois* (1981)

You are transcribing a mathematical manuscript in Alexander Grothendieck's own hand. The attached images
(`{PKG}_scan…jpg`, in scan order) are **{COUNT} scan pages** (scans {FIRST}–{LAST} of the Montpellier archive file
*{FILE}*), contrast-enhanced for legibility. A landscape spread (two sheets side by side) comes as two images,
`…_scanNNNa.jpg` (left) and `…_scanNNNb.jpg` (right): it is one scan page N, left sheet first. The handwriting is fast and hard. Your job is a **diplomatic transcription into
LaTeX**: exactly what is on the page, in Grothendieck's French, nothing more and nothing less. Separately from the
transcription, you also keep **research notes** on what these pages leave open (item 5 at the end).

**The task is a complete transcription: every word, symbol, formula, diagram, drawing, deletion, insertion and
marginal note on every page, in the order on the page.** Anything left out is an error. Accuracy is required as
well: a wrong confident reading is worse than an honest mark of doubt, but a mark of doubt is never a reason to leave
something out. Take the time this needs. Work page by page and line by line.

**A description is not a transcription.** You never replace content by a description, a summary, a paraphrase,
"[...]", "etc.", "and so on", or a note that something is there. You never include an image. If you cannot read
something, you transcribe what you can and mark the rest with the doubt macros (rule 5), in place.

## Absolute rules

1. **Transcribe only what you see.** Do not fill in from memory, from published transcriptions, from what the
   mathematics "should" say, or from your knowledge of Grothendieck's later work. If the page says something
   surprising, transcribe the surprise.
2. **No translation, no modernization, no correction.** Keep his spelling, accents (or their absence),
   punctuation, abbreviations ("cat.", "gr.", "rev.", "resp.", "cf.", …) and his own numbering ("Déf 1.6",
   "Prop. 1.7", "n° 12") exactly as written. Never expand an abbreviation in the text.
3. **Mathematics exactly as written**, in LaTeX: the same letters, the same alphabet (script, Gothic, bold,
   Greek), the same indices and exponents, the same arrows. Do not "fix" notation. If a symbol could be two
   things, mark it (rule 5).
4. **Mark the state of the page**, with these macros only:
   - `\scanpage{N}` at the top of each scan page (N = the scan number given above, first page = {FIRST});
   - `\mspage{n}` where Grothendieck's own page number is visible (also `\mspage{12bis}` etc.);
   - `\deleted{…}` for struck-through text you can still read; `\deleted{\illegible{2}}` if you cannot;
   - `\inserted{…}` for words added above the line or in the margin and meant to go in at that place;
   - `\margin{…}` for marginal notes that are not insertions;
   - `\uline{…}` for underlined words (his emphasis); keep double underlining as `\uuline{…}`;
   - `\diagram{…}`: every diagram typeset in `tikz-cd` (or an array for a table), with every object, arrow,
     label, direction and decoration exactly as written, including struck-out parts (`\deleted` inside the
     diagram). A diagram is **never** described in words; if part of it is hard to read, typeset it anyway and put
     `\unsure` or `\illegible` inside the diagram at that place;
   - `\figure{…}` for drawings that are not diagrams (curves, surfaces, pictures, dessins): **reproduce the
     drawing in TikZ**, with its shape, the relative positions of its parts and every written label, as closely as you
     can. A verbal description of a drawing is not allowed. Only if a drawing is a genuine picture too complex for
     TikZ (not text, not a formula, not a diagram), give your best TikZ approximation and add the comment
     `% crop-candidate: scan N` after it, so that the editor can insert a crop of the scan as an illustration.
5. **Doubt, explicitly:**
   - `\unsure{reading}` for a reading you believe but are not certain of;
   - `\unsure{reading|alternative}` when two readings are possible;
   - `\illegible{n}` for n words whose ink is physically unreadable at the highest zoom (estimate n). Before
     you use it, try a reading and prefer `\unsure{…}`. Never use it for a symbol inside a formula or a
     diagram: give your best reading there with `\unsure`.
   Never silently guess.
6. Keep his paragraphing and the order of the text on the page. Line breaks inside a paragraph need not be kept.

## Where readings go wrong

This task was tested against the scans. About one word in seventy was misread, and only a third of the misreadings
carried a doubt mark. The typical errors, to guard against:
- **A plausible mathematical word in place of the ink.** "fonctorielle" for *tangentielle*, "homotopique" for
  *heuristique*, "propres" for *quasi-*, "pointé" for *ponctué*, "intuition" for *intention*. The context makes the
  wrong word look right. If you have not seen every letter of a word, mark it `\unsure`, however well it fits.
- **A short condition or symbol left out.** "S ≠ ∅" after "Ω = Q̄"; an inclusion sign between two lines of a display;
  the "Ob" in "S ∈ Ob E₀"; inner parentheses. After each display, margin note and insertion, check symbol by symbol
  that everything on the page is in your text.
- **An insertion attached to the wrong place.** Put each insertion where its caret, arrow or line points.
- **Inequalities and arrow directions.** ≤ and ≥, ⇒ and ⇐, the direction of an arrow and of an isomorphism: read
  them from the ink, never from what the argument needs.
- **His own spellings, and word endings.** He spells some words his own way (*topossique*, with a double s) and often
  ends a word with a short stroke. Write the form on the page, not the dictionary form. Read each ending (singular or
  plural, *-é* or *-er*, *-ant* or *-ent*, *-ons*) from the ink, not from what the grammar of the sentence wants; if
  the ending is only a stroke, mark the word `\unsure`.

## Vocabulary that may occur

Use these only if the image supports them; they are here to help you recognize his abbreviations, not to
replace a reading: Teichmüller (groupe de Teichmüller, tour de Teichmüller), groupe fondamental, groupoïde
fondamental, revêtement, revêtement universel, topos, catégorie multigaloisienne, profini, extérieur
(Aut ext, $\mathrm{Autext}$), lacet, pincement, multiplicité, surface (de type $(g,\nu)$), $\Pi_{g,\nu}$,
$\widehat{\Pi}$, $\mathrm{Gal}(\overline{\mathbb Q}/\mathbb Q)$, corps de nombres, compactification, courbe,
orbite, stabilisateur, action extérieure, sous-groupe d'indice fini. His signs and abbreviations include $\overline{\mathrm m}$
(a short bar over a wavy *m*: *même*, as in "au m̄", "quand m̄"), "rev.", "isom.", "resp.", "cat.", "gr.", "pt", "néc.",
"loc.", "t.f." (de type fini); transcribe them as written (`$\overline{\mathrm m}$` for the m̄ sign).

## Method

1. For each scan page: read the whole page once, then transcribe it line by line.
2. Re-read the image against your transcription, line by line. Correct, or mark doubt.
   Then make the page **inventory**: every text block, display, diagram, drawing, margin note, insertion and
   deletion on the page, top to bottom, and check that each one is in your transcription, complete. Fix any gap.
3. Only then go to the next page.
4. While you read, write down on the side anything worth studying further (item 5 below). If the mathematics tempts
   you to fill in, complete or correct a reading, put that thought in the notes, never in the transcription.

## What to return

Deliver everything as **one zip file**, `{PKG}.zip`, so that it can be downloaded in one go. It holds three files:
`{PKG}_transcription.tex` (item 1), `{PKG}_notes.md` (items 2–5) and `{PKG}_inventory.csv` (item 6). Offer only that one download: no separate
files.

1. **The transcription**: one LaTeX fragment (no preamble, no `\documentclass`), starting with
   `\scanpage{{FIRST}}`, using only the macros above plus standard LaTeX and `tikz-cd`.
2. **A table of doubts**: scan page, line (approximately), your reading, the alternatives, and your confidence
   (high / medium / low).
3. **Abbreviations met**: each abbreviation as written, with what you think it stands for (in this list only,
   never in the text).
4. **A short honest note** on how legible these pages were and which parts you trust least.
5. **Research notes**, in English, kept apart from everything above. Note what in these pages is worth studying
   further:
   - **Grothendieck's own conjectures, questions and expectations**: a "?", "il est probable que", "je conjecture",
     "il serait intéressant de", "on devrait pouvoir", a hope or a doubt he writes down;
   - **claims stated without proof** or left for later ("on verra", "il est facile de voir", "sans doute",
     "on peut montrer"), and what a proof would need;
   - **implications he does not pursue on these pages**: consequences, special cases, links to other parts of
     mathematics or to known results;
   - **your own ideas**: what might follow, what might be false, an example or construction worth trying, a link he
     does not make. Label these clearly as yours.

   One note per item: scan page (and line if you can), kind (conjecture / unproved claim / unpursued implication /
   own idea), the note in one to four sentences, and for your own ideas your confidence and your reason. When a note
   is about something he wrote, quote his words briefly. He may take a point up later in the manuscript: note it
   anyway, because every note is checked against the rest of the manuscript and the literature. Do not present an
   idea as established or as new. The notes never change the transcription.

6. **The inventory** (`{PKG}_inventory.csv`, columns `scan,element,kind,position,first_words_or_objects,transcribed`):
   one row per element of every page (kind: text, display, diagram, drawing, margin note, insertion, deletion),
   with `transcribed` = yes for every row. A row that is not yes means the transcription is not finished.

If a scan page is blank, a cover, or not part of the manuscript, write `\scanpage{N}` followed by
`% blank` or `% not manuscript: <what it is>`.

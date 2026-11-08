# Transcription task {PKG}: Grothendieck, *La Longue Marche à travers la théorie de Galois* (1981)

You are transcribing a mathematical manuscript in Alexander Grothendieck's own hand. The 10 attached images
(`{PKG}_scan…jpg`, in scan order) are **10 scan pages** (scans {FIRST}–{LAST} of the Montpellier archive file *cote 140-2, pages 1–292*),
contrast-enhanced for legibility. The handwriting is fast and hard. Your job is a **diplomatic transcription into
LaTeX**: exactly what is on the page, in Grothendieck's French, nothing more and nothing less. Separately from the
transcription, you also keep **research notes** on what these pages leave open (item 5 at the end).

Accuracy matters more than completeness. **A wrong confident reading is far worse than an honest mark of doubt.**
Take the time this needs. Work page by page and line by line.

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
   - `\diagram{…}`: a commutative diagram in `tikz-cd` when it is clear, otherwise a precise description of it
     (objects, arrows, labels, directions) in brackets;
   - `\figure{…}` for drawings that are not diagrams (curves, surfaces, pictures), described precisely.
5. **Doubt, explicitly:**
   - `\unsure{reading}` for a reading you believe but are not certain of;
   - `\unsure{reading|alternative}` when two readings are possible;
   - `\illegible{n}` for n words you cannot read at all (estimate n).
   Never silently guess.
6. Keep his paragraphing and the order of the text on the page. Line breaks inside a paragraph need not be kept.

## Vocabulary that may occur

Use these only if the image supports them; they are here to help you recognize his abbreviations, not to
replace a reading: Teichmüller (groupe de Teichmüller, tour de Teichmüller), groupe fondamental, groupoïde
fondamental, revêtement, revêtement universel, topos, catégorie multigaloisienne, profini, extérieur
(Aut ext, $\mathrm{Autext}$), lacet, pincement, multiplicité, surface (de type $(g,\nu)$), $\Pi_{g,\nu}$,
$\widehat{\Pi}$, $\mathrm{Gal}(\overline{\mathbb Q}/\mathbb Q)$, corps de nombres, compactification, courbe,
orbite, stabilisateur, action extérieure, sous-groupe d'indice fini.

## Method

1. For each scan page: read the whole page once, then transcribe it line by line.
2. Re-read the image against your transcription, line by line. Correct, or mark doubt.
3. Only then go to the next page.
4. While you read, write down on the side anything worth studying further (item 5 below). If the mathematics tempts
   you to fill in, complete or correct a reading, put that thought in the notes, never in the transcription.

## What to return

Deliver everything as **one zip file**, `{PKG}.zip`, so that it can be downloaded in one go. It holds two files:
`{PKG}_transcription.tex` (item 1) and `{PKG}_notes.md` (items 2–5). Offer only that one download: no separate
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

If a scan page is blank, a cover, or not part of the manuscript, write `\scanpage{N}` followed by
`% blank` or `% not manuscript: <what it is>`.

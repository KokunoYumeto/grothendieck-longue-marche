## Absolute rules

1. **Transcribe only what you see.** Do not fill anything in from memory, from published texts (some of this material
   was later printed or transcribed elsewhere; do not look for, use or reproduce any such text, except an attached
   draft in the one way the section "The attached draft" allows), from what the mathematics "should" say, or from
   your knowledge of Grothendieck's work. If the page says something surprising, transcribe the surprise.
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
   - `\cotefile{37}` once, at the very start; then `\scanpage{N}` at the top of each scan page (N as above);
   - `\mspage{n}` where a page or sheet number of the text itself is visible: his own numbering, or the typed page
     number of a typescript ("- 16 -"); a document number typed at the top ("n° 296") is typed text and is
     transcribed. The archive's own pencilled sheet number in a lower corner is not part of the text: note it only as
     a comment line `% archive sheet number: NN`;
   - `\handwritten{...}` for words or symbols written by hand on a typed page (inside a word or formula, around the
     handwritten part only). On a page written entirely by hand it is not used: the hand is recorded in the
     inventory's `hand` column. Text typed into a handwritten page (a typed slip, a stamp) is noted in the inventory;
   - a word or sign written over another one (a correction made by writing on top): the visible final form as live
     text, the form underneath as `\deleted{...}` just before it, if you can read it;
   - `\deleted{...}` for struck-through or typed-over text you can still read (typed `xxxx` over a word included);
     `\deleted{\illegible{2}}` if you cannot;
   - `\inserted{...}` for words added above the line or in the margin and meant to go in at that place, where the
     caret, arrow or line points;
   - `\margin{...}` for marginal notes that are not insertions, written sideways or slanted ones included (transcribe
     them as text, at the place where they stand, and add the comment `% margin note written sideways` or
     `% slanted`);
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

## Reading handwriting

On Grothendieck's manuscripts about one word in fifty to seventy was misread in earlier work of this kind, and two
thirds of the misreadings carried no doubt mark. On clear handwritten letters of this archive the rate was about one
in a hundred, mostly punctuation. The errors found in checked transcriptions of these handwritten pages, each of
which you must guard against:

- **Slanted and sideways margin notes.** A short oblique note in a margin reading "pas prouvé" was transcribed as
  "pour journé". Turn your attention to every note written at an angle or along the edge: read it letter by letter on
  the crop, in its own direction, and mark every letter you have not seen clearly. Never let a margin note pass
  because it is short.
- **Symbols written into formulas.** Handwritten indices and separators were misread: an index `ih` read as `jh`, a
  semicolon in "(x₀ ; y₀)" given as a comma. In every formula, read each index, exponent, separator, prime and
  bracket from its own ink, even where the line above has the other form.
- **Punctuation and small words.** A comma left out, double quotation marks given as single ones, "papers" read as
  "paper". Copy the punctuation stroke by stroke; read each ending (plural s, -é or -er, -ant or -ent) from the ink.
- **Struck words given as live text.** Before you write a word as live text, look for a line, a scribble or a cross
  through it, including a light pencil line and a line through a whole block. A struck block is still transcribed,
  inside `\deleted{...}`.
- **E and F, 3 and 5**, and the other look-alikes listed below: decide each from its own strokes; if the strokes do
  not decide, write `\unsure{E|F}` or `\unsure{3|5}` at that place.
- **His hand reduces letters to strokes.** In his faster hand the middles of words become a wave or a line, and the
  ends of words are often a single stroke. Do not complete a word from what it should be: a word whose letters you
  have not all seen is marked `\unsure{reading}` (with every candidate the ink allows), however well it fits.
- **Insertions placed wrongly.** Follow every caret, arrow, loop and line from the inserted words to the exact point
  in the line where they go, and put the `\inserted{...}` there.

**Every doubtful reading is marked.** If you are not sure of a word, letter, sign or punctuation mark, it carries
`\unsure` (rule 6); an unmarked reading is a claim that you saw every stroke of it. Marks of doubt are expected on
handwritten pages, and many of them; a page of handwriting with no mark at all is a warning sign, not a success.

## Where readings go wrong

On typed pages, and in handwriting too, the errors that remain are of a few further known kinds. Guard against all
of them:

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


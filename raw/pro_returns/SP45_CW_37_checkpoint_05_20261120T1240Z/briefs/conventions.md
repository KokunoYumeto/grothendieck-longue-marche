# Transcription conventions (original C prompt rules only; current task workflow supersedes the older workflow)

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
   - `\cotefile{37}` once, at the very start; then `\scanpage{N}` at the top of each scan page (N as above);
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


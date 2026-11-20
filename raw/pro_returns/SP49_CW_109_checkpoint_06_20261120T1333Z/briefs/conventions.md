# Transcription conventions



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
   - `\cotefile{109}` once, at the very start; then `\scanpage{N}` at the top of each scan page (N as above);
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


**The attached files.** Besides this file there is one ZIP, `SP118_RD_37.zip`. Unpack it once: it holds every file named below. Each ZIP named below is already unpacked inside, as a folder of the same name without `.zip` (for example `SP118_RD_37_scans.zip` is the folder `SP118_RD_37_scans/`), so there is nothing more to unpack; every other file is at the top level under its own name.

# Second pass SP118_RD_37: Alexander Grothendieck's papers, Montpellier archive

You are making the second pass over **19 scan pages** of the Montpellier archive of Alexander Grothendieck (cote 37: "Rééditions SGA, EGA [SGA 4 à SGA 7, EGA I et EGA II] : tapuscrits et copies de tapuscrit annoté (s.d.), lettres (1967-1971, s.d.), notes manuscrites (s.d.).").

Two transcriptions of these pages exist already, both made by AI models from the same scans, and neither has been
checked against the ink by a person:

- **Witness C (ours):** our current text of record for each page, the best reading we have, made by AI models (GPT-6.2 Astra at reasoning effort max in ChatGPT Work), one file per scan, with its doubt marks (`\unsure{...}`, `\illegible{n}`).
- **Witness H (Hua's):** the transcription of the Commutator project of Michel Hua (github.com/Commutator-IO/
  grothendieck-project), an AI transcription in that project's own LaTeX macros, for 16 of these 19 pages.

Your job: **one consolidated diplomatic transcription of every page, from the ink,** in our conventions, with a
record of every place where it differs from witness C or from witness H and of what the scan shows there.

**Three sub-agents on different pages, then a second reading.** Pro gives you three sub-agents: use all three at
once, each on a page of its own. Give each sub-agent one page at a time, in the given order (the next page goes to the
first sub-agent that is free), with only that page's images, witness C's and witness H's texts for it, its rows of the C/H differences list, the section "The
errors that recur in these papers", our conventions and your notation table as it stands. It reads its page line by
line from the scan against both witnesses (method, step 2, a to d) and returns its reading of the page and every place
where it differs from either witness, with what it saw in the ink. You, the main reader, check each return on the scan,
decide every place it left open or that disagrees with a witness, and write the page. When every page is done, a sub-agent that has not read a page reads its
hardest places again from the image alone, without either witness or your page, and you decide every difference on a
crop (method, step 7).

**The mathematics while reading.** Follow the mathematics of the page as you read: a formula that does not parse, an
index that does not match, a sign, inequality or arrow that contradicts the argument is a place to look at the ink
again, and the ink decides, never the expected form. What the page claims and what the mathematics showed go briefly
into the notes (section "Notes while reading"); nothing beyond these pages is researched. Fidelity to the ink comes
first throughout.

Witness C is a draft, as witness H is: earlier second passes of this archive changed its reading at about 11 places a page, two thirds of them at
places not marked as doubtful.

## The attachments

- `SP118_RD_37_scans.zip`: one image per page, `<cote>_scanNNN.jpg`, the scan as the archive's PDF holds it (its native
  resolution, about 1680x2152 pixels), contrast-enhanced and sharpened. Before reading a page, make its two halves
  once, at full resolution, with Pillow: top and bottom, overlapping by about a tenth (left and right for a landscape
  sheet).
- `SP118_RD_37_texts.zip`:
  - `pages/<cote>_scanNNN.tex`: witness C, the transcription of each page as it stands now, with its marks;
  - `MARKS.tsv`: the doubt marks of witness C in live text, in page order, each with its id (`M0001` ...), its cote and
    scan, its kind, the mark as written and the LaTeX around it: known places to decide, among all the others;
  - `hua/hua_<cote>_scanNNN.tex`: witness H for the pages where his project has one;
  - `PREAMBLE.tex`: the macros of the transcription.

- `SP118_RD_37_hand_logs_of_these_cotes.md`: what earlier readers of these cotes logged about his hand (168 rows); check each habit on these pages before you rely on it.

Unzip them in your sandbox. **Look at the images yourself.** Reading software (OCR, a PDF text layer, any
text-recognition library) is not a substitute for looking and must not be used on these pages. How to look is the
reading workflow of the method (step 2): the page and its two halves once each, then one crop for each place they
leave open.

## The witnesses are drafts, the ink is the authority

**The task is a complete and correct transcription of every page from the ink: every word, symbol, formula, diagram,
drawing, deletion, insertion and marginal note, in the order on the page.** The witnesses tell you where to look; they
never settle a reading.

- **Where C and H differ,** look at the ink and decide. The answer may be C, H, or neither.
- **Where C and H read a place as different words, the place gets a crop.** A word on which the two witnesses differ
  (`SP118_RD_37_C_H_differences.tsv` lists the differences of each page) is never settled from the halves: crop it, read it
  letter by letter, and write in the changes log which letters are plain and which are not.
- **Where C and H agree,** the reading still has to be seen in the ink before it goes in. Both are AI readings of the
  same scans, and both models put a plausible word where the ink is hard; agreement between them is not evidence.
  Read every agreed word, sign and index against the image as you go.
- **Where only one witness has a passage,** check from the ink whether it is there and what it says; where neither has
  it, transcribe it.
- **What the earlier checks found** is the next section, the error sheet: read it before the first page.
- **A doubt mark of witness C** (in live or in struck-out text) is a place to decide in the ink: resolve it where a crop of it settles it (method, step 2c), keep it, narrowed to what the ink allows, where it does not, and record either.
- **Never fill in from memory, from published texts or from what the mathematics should say.** If the page says
  something surprising, transcribe the surprise. A correction of his text belongs in a note, never in the
  transcription.

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

**The hand log: learn his hand as you read.** Keep `SP118_RD_37_hand_log.md` from the first page. Enter every habit of his
hand or his notation that can mislead a reader: a letter he forms like another (a p like an n, a u like an n, a ζ like a
ξ), a sign he draws like another, a notation of his own. For each habit, record:
- the pages where you met it;
- whether it holds at every occurrence of that letter or sign on these pages;
- the places where witness C or witness H misread because of it.

Once a habit holds, read every later occurrence of that letter with it in mind, and confirm each one on the ink. The log
is returned with the transcription, so that the next runs start from it.

## Our conventions

Use exactly the macros of `PREAMBLE.tex` (in the texts folder) and the conventions of witness C's pages: `\cotefile{C}`
and `\scanpage{N}` (N: the scan number), `\mspage{n}`, `\deleted{…}`, `\inserted{…}`, `\margin{…}`, `\uline{…}`, `\uuline{…}`, `\diagram{…}`
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
2. **The reading workflow, for each scan page: a to d by the sub-agent that has the page, e by you.**
   a. Look at the whole image once, for the layout: the text blocks, displays, diagrams, drawings, margins,
      insertions and deletions, and where each sits.
   b. Read the two halves once each, line by line, with witness C's page file and witness H's text for that page
      beside them. Compare each word, abbreviation, symbol, index, sign, inequality, arrow, parenthesis, underline,
      deletion, insertion and margin note with both witnesses, and settle from the halves everything they settle, except the places that always get a crop (c).
      The halves are at full resolution: enlarging a whole half again shows nothing new.
      Then go once through every `\deleted` and every `\inserted` of witness C on this page and answer for
      each from the image: does the stroke cross these letters and only these, and where does the insertion's stroke
      end. A strike or an insertion the halves do not show plainly is a place for c.
   c. List the places the halves leave open: a reading that still differs from a witness, a doubt mark of C, a
      small symbol or index that decides the mathematics, a slanted, struck or crowded note, and every place of a kind
      in the error sheet that the halves do not settle. Some places always get a crop, whatever the halves show: every
      place where C and H read different words, and every doubt mark of C that you would resolve. Crop each of them once, tightly (the word or formula and a line
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
4. **As soon as a page is done** (every open place decided on the scan): write its file in `pages/` (named as in
   witness C), add its rows to the changes log, the collation list, the inventory and `decisions.tsv`, and append
   `scan NNN done <current UTC time> cote <cote>: L lines read, P places cropped, R rows` to `progress.log` (the lines of the page, the places cropped on it, the rows it added
   to the changes log). Only then go to the next page.
5. Read the first page as slowly as the last. The pages done fastest are where errors cluster.
6. **One notation.** The pages go to the sub-agents in the given order. You keep the one notation table and give its
   current state to each sub-agent with each page. Keep one notation table from the first page on: his recurring signs, exponents,
   alphabets, quotation marks and abbreviations, each with how it is written. Before the text is final, compare how each
   recurring sign was read across all the pages, check every difference against the ink, and make the readings agree.
   Put the table at the top of the doubts file.
7. **A second reading, written down before it is compared.** When every page is done, each page goes to a sub-agent
   that has not read it, for its hardest places. First write the page's box list, `second/<page>_boxes.tsv` (`<page>`
   is the page file's name without `.tex`; columns `box`, `kind`, `x0`, `y0`, `x1`, `y1`, in the original image's
   pixels), with a box for every insertion, every margin note, every struck passage, every formula in which witness C
   or your page has a doubt mark (the whole formula), every number written by pen, every word written by hand on a
   typescript, every place where C and H read different words, and every place where your page departs from witness C
   with less than high confidence; and write your page's reading of each box, in our conventions, to
   `second/<page>_first.tsv` (columns `box`, `reading`). The sub-agent gets the page's images and the box list, and
   nothing else: not your page file, not `_first.tsv`, not witness C, not witness H, not your notes. It crops each box,
   reads it from the ink and writes its reading, in our conventions, to `second/<page>_second.tsv` (columns `box`,
   `reading`). Then compare the two readings of each box by script, token by token; decide every difference on a crop
   of that place, correct or mark doubt, and enter every changed place in the changes log with both readings. For each
   page append `scan NNN audited <current UTC time>: B boxes read, D differences, K changed` to `progress.log`.
8. **A frozen transcription.** When every page is decided, write the SHA-256 of every page file and of the
   combined transcription to `progress.log` with the line `transcription frozen <current UTC time>`. At the
   end, check that the hashes are unchanged and say so in `progress.log`.
9. **Checkpoints.** Save a checkpoint ZIP to the user's Library, or wherever files survive the loss of the execution
   environment, once every 45 minutes of work, each under a new name, `SP118_RD_37_checkpoint_<NN>.zip` with `NN` counting up;
   never overwrite, rename or delete an earlier checkpoint, and put no earlier checkpoint ZIP inside a checkpoint. If
   the workspace comes back empty, restore it from the newest checkpoint and from this conversation before you
   continue. The final ZIP holds everything the checkpoints held. Save checkpoints once every 45 minutes and at no
   other time: none after a page, part, section, cote, folder, chapter or reader. A checkpoint is one ZIP holding every
   deliverable written so far and everything that documents the work (page files, changes log, collation list,
   inventory, decisions, doubts, notes, hand log, crops, progress log, the second readings in `second/`, scripts), so that a new session can continue from it and
   the files attached to this prompt. Leave the attached files themselves out of it, the scans and the texts: we have
   them. The crops in `crops/` go into every checkpoint and the final ZIP; the halves you made do not (we can make them
   again). It is never a JSON file, a
   recovery file, a summary, or an export of the newest pages only. Each checkpoint zip holds the current deliverables
   and documentation; earlier checkpoints are not copied into it. The checkpoints are what keeps the work if this
   session dies: work that is in no checkpoint is lost.
   **Crops: one dump, at the end.** In the checkpoints and the final ZIP, `crops/` holds only `crops/CROPS.tsv`: each
   crop's file name, its page, its box in pixels of the attached scan, and the place it decided. With the final ZIP,
   deliver the crop images once, as `SP118_RD_37_crops.zip`: the crops of the places you changed or left undecided, as
   greyscale JPEG at quality 85; the boxes in `CROPS.tsv` let us cut any other crop again from our scans. Keep
   `SP118_RD_37_crops.zip` under 200 MB: if it would be larger, lower the JPEG quality or the size, and leave out no crop
   of a change. Each ChatGPT account has 100 GB of storage, and crops repeated in every checkpoint fill it.
10. **If the execution environment fails.** A failed or unavailable environment does not end the task. Retry at
    intervals for as long as this session lasts, without writing recovery text into the chat. When the environment is
    back, restore your work from your newest checkpoint and the earlier checkpoints its file list names, redo what you
    had done after that checkpoint, and continue to the end. Do not write files out in this chat instead: the work
    reaches us only through checkpoint ZIPs and the final ZIP.

**No copies of sources in any ZIP you return.** No ZIP you return holds an unchanged copy of an attached file, or a
copy or plain text extraction of another author's paper, book or scan. We have the attached files; for a source you
fetched yourself, record the citation, the address, the SHA-256 and the pages used. Whatever this task asks you to
deliver (transcriptions, translations, editions, notes, programs, figures) always goes in.

This task is long by design: 19 pages, each read in the ink against two witnesses, read a second time, decided and
recorded. Work through all of it completely; do not stop at a sample or a plan, and do not ask whether to continue.
Ignore any clock.

## Page files: what they hold

These rules hold wherever another section of this prompt says less.

- **`pages/` holds finished pages only.** Keep a page in work in `drafts/`. Move it into `pages/` when you
  write its line `scan NNN done <current UTC time> cote <cote>` in the progress log, never before. A page file without that line is taken as
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

## Notes while reading

`SP118_RD_37_notes.md`, in English, per page, briefly: what the page states, computes or asks; every place where the
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

Two files, offered as downloads: `SP118_RD_37_final.zip`, which holds everything below, and `SP118_RD_37_crops.zip`, the one crop dump (under Checkpoints). It holds:

1. **The consolidated transcription:** `pages/` with one file per scan, named as in witness C, and
   `SP118_RD_37_transcription.tex`, all pages in order, one LaTeX fragment (no preamble), using only the macros of
   `PREAMBLE.tex` plus standard LaTeX, `tikz-cd` and TikZ.
2. **`SP118_RD_37_changes.md`, the changes log, per page:** one section per scan, with one table row for every place where
   the consolidated reading differs from witness C or from witness H: place (line, display, margin), C's reading, H's
   reading, the final reading, what the scan shows (the letters, strokes, lines or marks you saw, with the crop you used, by its file name and pixel box), and confidence (high, medium, low). Then, per scan, the places still unresolved.
   At the top: the counts per page and in all (changes against C, changes against H, by confidence) and the
   consequential corrections, those that change the mathematics, one per line.
3. **`SP118_RD_37_collation.tsv`, the collation list,** one row per place where witness H's reading differs from the
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
   `what the ink shows`, `crop` (scan and pixel box, or `page` for a mark that stays undecided; a mark you resolve has its crop) and `confidence`.
5. **`SP118_RD_37_doubts.md`** (in English, the readings as on the page): the notation table; a table of the remaining
   doubts (scan, line, reading, alternatives, confidence); the abbreviations met, each with what you think it stands
   for (in this list only); and a short honest note on how legible these pages were, which parts you trust least, and
   how the two witnesses compared on them.
6. **`SP118_RD_37_inventory.csv`** with the columns `scan,sheet_kind,hand,element,kind,position,first_words_or_objects,
   transcribed`: one row per element of every page (kind: text, display, diagram, drawing, margin note, insertion,
   deletion), with `transcribed` = yes for every row. `sheet_kind` is `text` (his notes on the subject of the folder),
   `reused_typed` (a typed page of another text that he wrote on or whose back he used), `typescript`, `letter`,
   `list`, `cancelled_draft` (a draft of his own that he struck through) or `cover`; `hand` says whose hand or machine
   wrote the element (his hand, another named or unnamed hand, typewriter, print).
7. **`SP118_RD_37_notes.md`:** the notes made while reading (above), and `CHECK_EVENTS.tsv`.
8. `progress.log`, and `second/`: for every page its box list, your readings of the boxes and the second
   reading (method, step 7).
9. **`SP118_RD_37_sheet_feedback.md`:** for our next runs: for each kind in the error sheet, how many places on these pages
   were of that kind, and every recurring error you met that the sheet does not name, with its places; and
   **`SP118_RD_37_hand_log.md`**, the hand log (the error sheet's last section).

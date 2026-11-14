# La Longue Marche à travers la théorie de Galois: five readers, French and English, that fit the page and link every doubtful reading to its scan

You are GPT-6 Astra in ChatGPT Pro mode, with a Python and LaTeX environment. Three ZIP files are attached:
`LM_FR.zip`, `LM_EN.zip` and `LM_TYPESET.zip`. Each has `MANIFEST.tsv` at its root (path in the zip, source, bytes,
SHA-256, role); read the manifests first. Drafted by Claude Fable 5.2 (Anthropic, effort high) from the records of the
transcription, of the translation and of the draft readers.

## What this is for

Alexander Grothendieck's research notes *La Longue Marche à travers la théorie de Galois* (1981) are kept in the
Grothendieck archive of the Université de Montpellier as cotes 140-1 (a draft, 37 scans), 140-2 (575 scans, his pages
1–292), 140-3 (696 scans, pages 293–650) and 140-4 (280 scans, pages 650bis–787): 1,588 scans of handwriting. All of
it has been transcribed into diplomatic LaTeX (AI-transcribed by GPT-6 Astra, every line then checked against the
archive images by Claude Opus 5.5) and translated into English (AI-translated by GPT-6.1 Sol, checked by script, unit
by unit). All of that is attached. What exists as books is only draft readers: the packages set one after another,
with a typesetting pass that scales whatever is too wide. What is missing is the readers: finished books, one per
form and language, in which nothing runs off the page, every doubtful or illegible reading opens its scan, and the
apparatus says exactly what the manuscript has. You build them, by script and diff. The text is far too long to read
whole, so work from the records, and look at the text wherever a decision needs it.

The companion to La Longue Marche is a separate book under construction. It is not part of this task.

## The five readers

Build one book per form and language, each a single LaTeX file that compiles with LuaLaTeX of a standard TeX Live:

| File | Language | Form |
|---|---|---|
| `LM_FR_diplomatique.tex` | French | **Diplomatic**: the transcription as it stands, cote by cote and scan by scan: his deletions (grey), insertions (teal), marginal notes, underlining, abbreviations and spellings as written, the transcriber's doubt (`\unsure{A|B}`, blue) and `\illegible{n}`, the scan marks and his own page numbers |
| `LM_FR_corrige_apparat.tex` | French | **Corrected, with apparatus**: the text he ended with. Struck-out words leave the running text and go to the apparatus; insertions are integrated and marked; a slip of the pen (a misspelt word, a missing bracket, an index that the same formula two lines on shows to be a slip) is corrected only where the context settles it, and the apparatus gives the manuscript's reading, the correction and the reason; every doubtful and illegible reading stays marked |
| `LM_FR_texte_de_lecture.tex` | French | **Reading text**: the corrected text with no apparatus; doubtful and illegible readings stay marked and linked; scan numbers and his page numbers in the margin only; a short preface says what was left out |
| `LM_EN_corrected_apparatus.tex` | English | **Corrected, with apparatus**: the English of the same corrected text, with the same apparatus entries, in English |
| `LM_EN_reading.tex` | English | **Reading text**: as for the French |

**Build the forms of a language from one annotated master** (`LM_FR_master_annotated.tex`,
`LM_EN_master_annotated.tex`). Mark every place where the manuscript and the corrected text differ, for instance with
a macro `\var{manuscript reading}{corrected reading}{kind}{source id}`, and generate the forms from the master by
switching the macro. The forms then cannot drift apart. A French slip that does not change the English (a spelling,
for example) gets no variant in the English. The English master carries the same variant ids as the French one.

## Sources of record

- **French** (`LM_FR.zip`): `fr/texts/<package>.tex`, the checked transcription of each of the 116 packages (the
  source of record; `fr/records/CURRENT_TEXT_INDEX.tsv` lists them with cote, scans and the counts of doubt marks).
  `fr/changes/` holds the second pass's table of changes for each package, with the evidence and a confidence;
  `fr/notes/` the notes checked against the corrected text; `fr/records/` the reports of the close of the second pass
  and the fixes left open at the merge. Each scan begins with `\scanpage{n}`; `\mspage{n}` is his own page number.
  `build/wrap.tex` is the preamble with the macros of the transcription (`\unsure`, `\illegible`, `\deleted`,
  `\inserted`, `\margin`, `\diagram`, `\figure`); `build/coverage.json` gives the order of the packages in each cote;
  `build/rebuild_readers.py` and the three repair scripts are the build of the French draft readers, for reference.
- **English** (`LM_EN.zip`): `en/packages/<package>_en.tex`, the English of each package (the source of record of
  the translation); `en/units/` and `en/french_units/`, the same text cut into the 245 units in which it was
  translated, English and French side by side by file name; `en/MANIFEST.json`, the packages and units with cote and
  scans. `en/checks/FIXES.jsonl` (41 fixes, all applied to the units and packages) and `en/checks/WAIVERS.jsonl` (34
  check failures accepted, each with its reason); `en/checks/REPORT.md`, `SUMMARY.md` and
  `GLOSSARY_APPLIED_AND_FLAGGED.md`; `en/glossary/` (the glossary of the translation: `GLOSSARY_LM.csv`,
  `entries_LM.txt`, `terms_LM.txt`); `en/README.md` (how the translation was made and checked); `en/COMPILE.tsv`
  (which packages need the mechanical LaTeX repairs to compile: run them on those packages only); `en/scripts/` (the
  scripts of the translation and of the draft reader, for reference). The formulas of the English are the French's,
  character for character, and the marks of the transcription are the same on every scan; `check_units.py` tests
  both.
- **Typesetting records** (`LM_TYPESET.zip`): `typeset/TYPESETTING_FINDINGS.md` (read it in full: what ran off the
  page in the draft readers, the causes, and how the links to the scans work); `typeset/OVERFULL_BEFORE.tsv` (the 382
  overfull boxes of the English draft reader before any repair, with page, source lines and kind);
  `typeset/TYPESET_PASS_CHANGES.tsv` (every display and line the draft readers' pass scales or turns);
  `draft_readers/` (the sources of the five draft readers, with the pass in their preamble); `typeset/scripts/` (the
  pass, the check of ink against the sheet, the contact sheets, the list of links).
- **Scans.** None are attached. No reading is decided again in this task: every `\unsure` and `\illegible` stays as
  the checked transcription has it, and links to its scan. The archive's viewer shows scan `n` of a cote at
  `https://grothendieck.umontpellier.fr/web/viewer.html?file=../<cote>.pdf#page=<n>`, with `<cote>` one of `140-1`,
  `140-2`, `140-3`, `140-4`.

## Rules

1. **Keep his notation and language** in every form: his letters, indices and arrows, his own forms (Sl, Gl,
   Autext, the doubled Γ), his abbreviations in the French. Correct a slip only where the context settles it, with the
   reason in the apparatus. Never standardize notation silently. You may write one consistent macro set, but it must
   not change what prints.
2. **No reading changes without a record.** The diplomatic reader prints the checked transcription. Every difference
   between it and the corrected form is a variant in the master, with a kind (deletion, insertion, slip corrected,
   marginal note placed) and a source id.
3. **The English** is that of `en/packages/`, with the glossary's terms. Where the corrected French changes a place,
   make the same change in the English and record it in the English change log. List every French term the English
   renders in more than one way in `GLOSSARY_INCONSISTENCIES.md`; make the English consistent where the variation is
   plainly a slip, and record each change.
4. **Links.** In every reader, every `\unsure{...}`, every `\illegible{n}` and every scan mark is a link to the scan
   it stands on, by the URL pattern above. Count the links of each PDF and compare the counts with the marks of its
   source; the number of distinct scan pages linked from the readers of a cote is the number of its scans.
5. **Marginal notes.** A note that fits in the margin in three lines stays in the margin. Every other note is set in
   the text block at the place it belongs to, and reads as a marginal note (small type, a rule, a label). No note is
   dropped, cut or moved to another page than its line's without a mark at that line.
6. **The archive's footer.** Where the foot of a scan was transcribed with the archive's own line (the URL and the
   postal address of the Université de Montpellier, `typeset/TYPESETTING_FINDINGS.md`, cause 2), his page number is
   manuscript and the archive's line is not. Decide how the readers show such a place, apply the decision to every
   occurrence in all five readers, and list every occurrence in `ARCHIVE_FOOTERS.tsv` (package, scan, the text, what
   each reader prints).
7. **Typesetting, repaired in the source.** Every place of `OVERFULL_BEFORE.tsv` and every place of
   `TYPESET_PASS_CHANGES.tsv` is repaired where it stands, in the master: a wide tikzcd diagram gets column and row
   separations, a font size and, where it has to be, line breaks in its entries that let it fit; a diagram that at
   70 % of its size is still wider than the line is turned onto a landscape page or split into parts joined by
   repeated objects, and the apparatus says so; a wide display is broken where the mathematics breaks (`multline`,
   `aligned`, `split`); a formula in running text that cannot break is given breakpoints or moved to a display line
   with a mark. A blanket scaling pass over the book is not a repair. Record every place in `TYPESETTING_FIXES.tsv`
   (reader, package, scan, source line, what was wrong, what was done).
8. **Credit and rights.** Each reader's front matter carries:
   - the author, the title, the year, the archive and the cotes;
   - "AI-transcribed by GPT-6 Astra (OpenAI, ChatGPT Pro mode), checked against the scans by Claude Opus 5.5
     (Anthropic)"; in the English readers also "AI-translated by GPT-6.1 Sol (OpenAI, reasoning effort max, API Flex
     tier); prompts, checks and fixes by Claude (Anthropic)"; and "this edition built by GPT-6 Astra (OpenAI, ChatGPT
     Pro mode)". Never "AI-assisted";
   - the sources and the earlier work exactly as `records/README_published.md` names them (the scans of the
     Université de Montpellier; the earlier transcriptions consulted as witnesses and not reproduced, with the names
     of the people who made them). Keep every human contribution it names;
   - this rights statement, in the reader's language: "The rights in the original work belong to its author or the
     author's representatives or heirs. Where we hold rights, in the AI-produced transcription, translation,
     corrections and typesetting, they are dedicated to the public domain under CC0 1.0. This edition is published for
     educational, non-profit purposes, and we claim no rights we do not hold. If you hold rights in this work and
     object to its publication here, please open a GitHub issue and we will take it down."
9. **Privacy.** Never copy a local file path into a reader or a record; refer to files by their path inside the ZIP.
   Copy no e-mail address.

## What to deliver

Deliver one ZIP per language and one for the records, named `LM_READERS_FR.zip`, `LM_READERS_EN.zip` and
`LM_READERS_RECORDS.zip`:

- the five reader `.tex` files and the two annotated masters, each with its PDF;
- `CHANGES_FR.tsv`: every difference between the corrected French reader and the diplomatic one (cote, scan, place,
  manuscript reading, corrected reading, kind, reason);
- `CHANGES_EN.tsv`: every difference between the corrected English reader and `en/packages/`;
- `APPARATUS_COUNTS.md`: per cote and form, the number of apparatus entries by kind;
- `TYPESETTING_FIXES.tsv`, `ARCHIVE_FOOTERS.tsv` and `GLOSSARY_INCONSISTENCIES.md`;
- `TYPESETTING_REPORT.md`: for each of the seven PDFs, the overfull boxes of its log before and after (count, and
  the widest), the pages with ink outside the sheet and outside the type area (`page_bounds_20261113.py`), the
  missing characters, the number of links, and the list of the pages you rendered and looked at with what you saw on
  each;
- `README.md`: what each file is, how each form was made, the counts, and the compile status of each reader with its
  LaTeX errors and warnings;
- your build scripts, with their outputs.

## When it is done

Do everything: every fix integrated, every page checked, and the notes and records written.

**Each item is done when:**
- **A reader** compiles with LuaLaTeX without errors; it holds the text of every one of the 1,588 scans (the French
  readers) or of every one of the 245 units (the English readers), checked by script against the sources of record,
  with the counts in the README; and its scan marks agree with `\scanpage` in the sources.
- **The apparatus** has one entry for each difference between the diplomatic and the corrected form, and none for
  anything else.
- **Typesetting.** The log of every PDF has no overfull box wider than 2pt, whether a diagram, a display or a line
  of text, and no missing character; no page has ink beyond the sheet, and none has ink outside the type area except
  the overhang of a single letter. You have rendered to images and looked at every page that had an overflow in
  `OVERFULL_BEFORE.tsv` or a change in `TYPESET_PASS_CHANGES.tsv` (found again by its scan mark), every landscape
  page, and forty pages spread evenly over each reader.
- **Links.** Every `\unsure`, `\illegible` and scan mark of every reader is a link to its scan, and the counts are in
  the report.
- **Every occurrence of the archive's footer** is listed with what each reader prints.

**Not acceptable:**
- a reader that drops, summarizes or paraphrases any part of the text;
- a correction in one form and missing from another, or in the French and missing from the English where it changes
  the English;
- an apparatus entry without a kind and a reason;
- a reading of the checked transcription changed, or a doubt mark removed;
- a silent change of notation;
- a diagram or formula made to fit by a scale below 70 %, or by a scaling pass over the whole book;
- a box wider than the line by more than 2pt left in a log, or hidden by raising `\hfuzz`;
- local paths or e-mail addresses in any output.

**The task is finished** only when all five readers and the two masters, with their PDFs, the change logs, the
typesetting records and report, the glossary list and the README are in the three ZIPs, and every condition above
holds for every reader.

## Working method

- Start from the manifests, `fr/records/CURRENT_TEXT_INDEX.tsv`, `en/MANIFEST.json` and
  `typeset/TYPESETTING_FINDINGS.md`.
- Build the annotated masters by script from the package texts, generate the forms, compile, and check the counts.
- Repair the typesetting place by place, largest overflow first, compiling the package on its own before the whole
  reader. The French and the English share their formulas and diagrams: a repair of a diagram goes into both masters.
- After each finished reader, save a checkpoint ZIP of everything so far to the user's Library, or wherever files
  survive the loss of the execution environment. Save the final ZIPs there too.
- This task is long by design. Work through it completely; do not stop at an outline, a sample or a plan, and do not
  ask whether to continue. Ignore any clock. Write the files from the start and extend them as you go, so that an
  interruption loses little.

**Typesetting check.** Every PDF you deliver is published as it is. Before you deliver one, read its build log: no overfull box may stick out by more than 2pt, whether a diagram, a display or a line of text. Fix each one in the source (scale or split a wide diagram, break a wide display, let a line break) and compile again. Then render pages to images and look at them: every page that had an overflow, and a sample spread over the document. Give the counts before and after in the report.

**Checkpoints.** Save a checkpoint ZIP to the Library after every finished Part, each under a new name, `LM_READERS_checkpoint_<NN>.zip` with `NN` counting up; never overwrite, rename or delete an earlier checkpoint. If the workspace comes back empty, restore it from the newest checkpoint and from this conversation before you continue. The final ZIP holds everything the checkpoints held: a file or passage left out of the final is listed in the report with the reason (superseded by which file, or wrong).

## If the execution environment fails

If the workspace disconnects or an attached ZIP cannot be opened, wait and retry for ten minutes. If it does not come
back, write the work out in the chat as text:
- the change logs, the typesetting records, the README and the report so far, each in full in its own code block
  headed by its file name;
- your build scripts in full, so that the readers can be rebuilt from the attached sources;
- which readers were finished and where their checkpoints are.

Then continue the remaining work in the chat in the same form until every part is written. An answer that only
reports the failure or asks for the files again is not acceptable.
